<table align="center"><tr><td align="center" width="9999">
<img src="https://blogs.perficient.com/files/openai-avatar.png" align="center" width="150" alt="Project icon">
|
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1024px-Python-logo-notext.svg.png" align="center" width="150" alt="Project icon">

</td></tr></table>

<div align="center">
<h1>GPT-4 Text to Speech Assistant</h1>
</div>

This project demonstrates the use of GPT-4, a large language model by OpenAI, as a voice-based text assistant. The assistant listens to the user's questions, fetches responses from GPT-4, and reads them aloud.

# Clone the reqpository
```bash
git clone https://github.com/mgcollie/voice2GPT.git
```

# Move into the directory
```bash
cd voice2GPT
```

# Requirements
To run this voice assistant, we assume you already have python 3.9+ installed and you will need to  
create a virtual environment and install the following packages:

- openai
- pyttsx3
- SpeechRecognition

```bash
python -m venv venv
.venv\Scripts\activate
pip install -r requirements.txt
```

# Setup
To use this voice assistant, you need an API key for the OpenAI GPT-4 model. Store the API key in an environment variable called OPEN_API_KEY. You can do this in your shell or terminal before running the script:


# Usage
```bash
python voice_assistant.py
```

The voice assistant will ask how many tokens you want to use. Wait until you see `Listening...` in the terminal. Speak your response, and the assistant will transcribe it.

Next, the voice assistant will ask for your question. Wait until you see `Listening...` in the terminal. Speak your question, and the assistant will transcribe it and send it to the GPT-4 model. The GPT-4 model's response will be converted to speech and played.

If there is any issue during transcription, the voice assistant will inform you and exit the program.

# Troubleshooting
If you face any issues related to the microphone, ensure that your system's microphone is working correctly and that the correct audio device is selected.

In case of issues with the GPT-4 API, check your API key and make sure it's set up correctly.

# License
This project is licensed under the MIT License. See the [LICENSE](https://github.com/mgcollie/voice2GPT/blob/main/LICENSE) file for more information.

