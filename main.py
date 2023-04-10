import argparse
import whisper
from pytube import YouTube


youtube_url = 'https://www.youtube.com/watch?v=NT2H9iyd-ms'
audio_file = 'audio.mp4'

def download_video(url):
    yt = YouTube(url)
    print('downloading video: {}'.format(yt.title))
    yt.streams.filter(only_audio=True).first().download(filename=audio_file)

def transcribe_audio(output_file):
    model = whisper.load_model('base')
    print('whisperring....')
    output = model.transcribe(audio_file)
    with open(output_file, 'w') as f:
        f.write(output['text'])
    print('transcription complete, saved to {}'.format(output_file))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--youtube_url', type=str, default=youtube_url)
    parser.add_argument('--output_file', type=str, default='output.txt')
    args = parser.parse_args()

    download_video(args.youtube_url)
    transcribe_audio(args.output_file)

if __name__ == '__main__':
    main()
