import os
import assemblyai as aai
import streamlit as st

# Replace with your API key
aai.settings.api_key = os.getenv('API_KEY')

def timestamp_string(milliseconds):
	seconds = milliseconds // 1000
	minutes, seconds = divmod(seconds, 60)
	hours, minutes = divmod(minutes, 60)
	return f"{hours:02}:{minutes:02}:{seconds:02}"

def generate_results(transcript):

	## Full Transcription
	st.subheader("Full Audio Transcription")
	with st.expander("Transcription"):
		sentences = transcript.get_sentences()

		for sentence in sentences:
			st.write(f"{timestamp_string(sentence.start)}: {sentence.text}")


	## Summary
	st.subheader("Transcription Summary")
	with st.expander("Summary"):
		st.write(transcript.summary)


	## Speaker Labels
	st.subheader("Speaker Labels")
	with st.expander("Speakers"):

		for utterance in transcript.utterances:
			st.write(f"Speaker {utterance.speaker}: {utterance.text}")


	## Sentiment analysis
	st.subheader("Sentiment Analysis")
	with st.expander("Sentiment"):

		for sent in transcript.sentiment_analysis:

			text = f"{timestamp_string(sent.start)}: Speaker {sent.speaker}: {sent.text}"

			if sent.sentiment == "NEUTRAL":
				st.warning(text)
				
			elif sent.sentiment == "POSITIVE":
				st.success(text)
			
			else:
				st.error(text)

	## Topics
	st.subheader("Topics")
	with st.expander("Topics"):

		for topic, relevance in transcript.iab_categories.summary.items():
			st.write(f"Audio is {relevance * 100}% relevant to {topic}")


def main():

	st.title("Audio Analysis Toolkit")

	audio_file = st.file_uploader("Please upload a file")

	if audio_file is not None:
		st.audio(audio_file, start_time = 0)

		st.write('File uploaded, transcribing now with AssemblyAI...')

		config = aai.TranscriptionConfig(speaker_labels=True,
										 iab_categories=True, 
										 speakers_expected=2,
										 sentiment_analysis=True,
										 summarization=True,
										 language_detection=True)

		transcriber = aai.Transcriber()
		transcript = transcriber.transcribe(audio_file, config=config)

		st.write('Audio Transcribed...Generating Results')

		generate_results(transcript)

		st.divider()

		message = st.text_input("Ask questions about the audio", placeholder = "What was the conversation about?")

		if message:

			prompt = f"Based on the transcript, answer the following question: {message}"

			result = transcript.lemur.task(prompt, final_model=aai.LemurModel.claude3_5_sonnet)

			st.subheader("Response")
			with st.expander("Response"):

				st.write(result.response.strip())

if __name__=="__main__":
	main()