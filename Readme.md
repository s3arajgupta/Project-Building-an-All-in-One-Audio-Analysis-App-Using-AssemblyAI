# Audio Analysis App using AssemblyAI API

This project demonstrates how to build a comprehensive audio analysis application using the [AssemblyAI API](https://www.assemblyai.com/) and [Streamlit](https://streamlit.io/) for the web interface. The app takes an audio file as input and performs the following tasks:

1. **Transcribes the audio**.
2. **Performs sentiment analysis on the audio**.
3. **Summarizes the audio**.
4. **Identifies named entities mentioned in the audio**.
5. **Extracts broad ideas from the audio**.
6. **Enables interaction with the audio in natural language**.

## Features

- **Audio Transcription**: Transcribes the provided audio file into text.
- **Sentiment Analysis**: Analyzes the sentiment of each sentence in the transcript.
- **Audio Summarization**: Generates a summary of the audio content.
- **Named Entity Recognition (NER)**: Identifies and extracts entities mentioned in the audio.
- **Broad Ideas Extraction**: Detects and displays topics using IAB categories.
- **Natural Language Interaction**: Allows the user to interact with the audio transcript using AssemblyAI's LeMUR framework.

Enable features like speaker labels, summarization, and sentiment analysis by configuring the `TranscriptionConfig` object:

```python
config = aai.TranscriptionConfig(
    speaker_labels=True,
    iab_categories=True,
    sentiment_analysis=True,
    summarization=True,
    language_detection=True
)
```

## App Workflow

1. The user uploads an audio file.
2. The audio file is sent to AssemblyAI for transcription and additional analyses such as sentiment analysis, language identification, summarization, etc.
3. The transcript is returned, and the results are displayed in the app.
4. The user can chat with the transcript using natural language to extract more insights, ask questions, and interact with the content.

## Interacting with the Audio

LeMUR allows natural language interaction with the transcript:

```python
prompt = "Provide insights about the audio"
response = transcript.lemur(prompt)
st.write(response)
```

## Prerequisites

To run this app, you will need:

- A free [AssemblyAI API key](https://www.assemblyai.com/), which provides $50 worth of free transcription credits.
- Python installed on your machine.
- [Streamlit](https://docs.streamlit.io/) for building the web interface.

## Installation

1. Clone the repository:

   ```bash
   git clone <repository_url>
   ```

2. Install the required Python packages:

   ```bash
   pip install assemblyai streamlit
   ```

3. Set your AssemblyAI API key in the environment:

   ```python
   api_key = 'your_assemblyai_api_key'
   ```

4. Run the application:

   ```bash
   streamlit run app.py
   ```

## A Departing Note

AssemblyAI’s Universal-1 model is a state-of-the-art multimodal speech recognition model trained on 12.5 million hours of multilingual audio data, offering:

- 10% or greater accuracy improvement in English, Spanish, and German.
- 30% lower hallucination rate compared to OpenAI's Whisper Large-v3.
- Supports multiple languages in a single audio file.

Enjoy building with AssemblyAI! Feel free to contribute and improve this repository.
```

This `README.md` provides a full overview of the app's functionality, installation, and usage instructions, and is ready to be placed in your Git repository.