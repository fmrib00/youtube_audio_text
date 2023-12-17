import argparse
# import whisper
from pytube import YouTube
from pytube.exceptions import VideoUnavailable


def download_video(url: str, audio_only: bool) -> None:
    try:
        yt = YouTube(url)
        if audio_only:
            print('downloading audio: {}'.format(yt.title))
            yt.streams.filter(only_audio=True).first().download()
        else:
            yt.streams.filter(progressive=True).get_highest_resolution().download()
        print('download complete')
    except VideoUnavailable:
        print('video is unavailable')
    except Exception as e:
        print(e)
        print('download failed')

# def transcribe_audio(output_file):
#     model = whisper.load_model('base')
#     print('whisperring....')
#     output = model.transcribe(audio_file)
#     with open(output_file, 'w') as f:
#         f.write(output['text'])
#     print('transcription complete, saved to {}'.format(output_file))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--url', type=str, required=True)
    parser.add_argument('--audio_only', action='store_true')
    args = parser.parse_args()

    download_video(args.url, args.audio_only)
    # transcribe_audio(args.output_file)

if __name__ == '__main__':
    main()
