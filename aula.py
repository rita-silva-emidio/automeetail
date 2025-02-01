
import uuid
from moviepy import AudioFileClip

def mp4_to_mp3(mp4_filename, mp3_fileneme):
    audio = AudioFileClip(mp4_filename)
    audio.write_audiofile(mp3_fileneme)
    audio.close()

if __name__ == "__main__":
    mp4_filename = "/home/ritasilva/Documents/Rita/Impacta/automeetail/entrevista de Boechat com Jô Soares curto.mp4"
    mp3_filename = str(uuid.uuid4()) + ".mp3"  

    mp4_to_mp3(mp4_filename, mp3_filename)