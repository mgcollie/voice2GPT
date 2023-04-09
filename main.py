import os
import openai
import pyttsx3
import speech_recognition as sr
from typing import Optional

engine = pyttsx3.init()

recognizer = sr.Recognizer()
openai.api_key = os.getenv('OPEN_API_KEY')


def text_to_speech(text: str) -> None:
    """
    Convert the given text to speech and play it.

    Args:
        text (str): The text to be converted to speech.
    """

    print(text)
    engine.say(text)
    engine.runAndWait()


def call_openai(prompt: str, temperature: float = 0.5, max_tokens: int = 100) -> str:
    """
    Call the GPT-4 chat model and fetch the response for the given prompt.

    Args:
        prompt (str): The prompt for the GPT-4 model.
        temperature (float, optional): The sampling temperature. Defaults to 0.5.
        max_tokens (int, optional): The maximum number of tokens to be returned. Defaults to 100.

    Returns:
        str: The GPT-4 model's response.
    """

    prompt = prompt.strip()

    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
        n=1,
        stop=None,
    )
    return response.choices[0].message.content.strip()


def listen_and_transcribe(prompt: str) -> Optional[str]:
    """
    Record audio, transcribe it, and return the transcribed text.

    Args:
        prompt (str): The prompt to be spoken before listening to the audio.

    Returns:
        Optional[str]: The transcribed text, or None if the transcription failed.
    """

    text_to_speech(prompt)

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)  # Added this line
        print("Listening...")
        audio = recognizer.listen(source)

    try:
        print("Transcribing...")
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand the audio")
        return None
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
        return None


def main() -> int:
    prompt = "How many tokens do you want to use?"
    response = listen_and_transcribe(prompt)
    if response:
        try:
            max_tokens = int(response)
            print('You said: ', max_tokens)
        except ValueError:
            print("Invalid input. Please provide an integer value.")
            return -1
    else:
        return -1

    prompt = "What is your question?"
    question = listen_and_transcribe(prompt)
    if question:
        print('You said: ', question)
        data = call_openai(question, max_tokens=max_tokens)
        text_to_speech(data)
        return 0
    else:
        return -1
    
    
if __name__ == "__main__":
    main()
