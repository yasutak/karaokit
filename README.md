# karaokit

Simple karaoke-style video generator, using [whisper](https://www.google.com/search?q=whisper+openai&oq=whisper+openai&aqs=chrome..69i57j0i512l3j69i60l3j69i65.6087j0j7&sourceid=chrome&ie=UTF-8) for transcription and [whisperx](https://github.com/m-bain/whisperX) for token-wise text alignment.

## requirements

- GPU-equipped machine
- `ffmpeg`

- `pip install -r requirements.txt`

<!-- markdownlint-disable -->

## usage

```bash
$ python karaokit.py media_file{mp3 or mp4} output_file_dir
```


## API Overview

## Modules

- [`karaokit`](docs/api-docs/karaokit.md#module-karaokit)

### Functions

- [`karaokit.karaokit`](docs/api-docs/karaokit.md#function-karaokit): Generate a subbed video from an media file.


## credits

- ja_song.mp3 from
[BGMusic](https://bgmusic.jp/freevocaloid/vocaloid2/)
