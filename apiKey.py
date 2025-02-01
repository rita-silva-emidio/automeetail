import assemblyai as aai

FileURL = "/home/ritasilva/Documents/Rita/Impacta/automeetail/0c1dcdc2-3f58-4258-a2a5-fd041a22a01c.mp3"

aai.settings.api_key = "56d62a316b094fea9654e73db3303ab2"
transcriber = aai.Transcriber()

configuracoes = aai.TranscriptionConfig(
   speaker_labels=True,
   speakers_expected=2,
   language_code="pt"
)

transcript = transcriber.transcribe(FileURL, config=configuracoes)

if transcript.status == aai.TranscriptStatus.error:
    print(transcript.error)
else:
    for utt in transcript.utterances:
        print(f"{utt.speaker}: {utt.text}")
        print('\n')