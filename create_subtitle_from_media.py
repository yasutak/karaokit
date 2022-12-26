import pathlib
import subprocess


def convert_mp4_to_mp3(input_file: str) -> str:
    """Convert an mp4 file to an mp3 file.

    Args:
        input_file (str): The path to the input mp4 file

    Returns:
        str: The path to the output mp3 file
    """
    if pathlib.Path("converted").exists():
        pass
    else:
        pathlib.Path("converted").mkdir()

    output_file_path = f"converted/{pathlib.Path(input_file).stem}.mp3"

    ffmpeg_command = [
        "ffmpeg",
        "-i",
        input_file,
        output_file_path,
    ]
    subprocess.run(ffmpeg_command)
    return output_file_path


def create_subtitle_from_media(
    media_file: str,
    output_file_dir: str,
    language: str,
    model: str = "large",
    dry_run: bool = False,
) -> None:
    """Generate a subtitle file from an mp3 file with whisperX.

    Args:
        input_file (str): The path to the input file (mp3 or mp4)
        output_file_dir (str): The path to the output subtitle
        language (str): The language of the audio
        model (str, optional): The model of the audio. Defaults to "large".
    """

    if media_file.__str__().endswith(".mp4"):
        mp3_file = convert_mp4_to_mp3(input_file=media_file)
    elif media_file.__str__().endswith(".mp3"):
        mp3_file = media_file
    else:
        raise Exception(f"Input file must be mp3 or mp4, not {media_file.__str__().split('.')[-1]}")

    wihsperx_command = [
        "whisperx",
        "--model",
        model,
        "--language",
        language,
        mp3_file,
        "--output_dir",
        output_file_dir,
    ]

    result = subprocess.run(wihsperx_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, encoding="utf-8")
    if result.returncode != 0:
        raise Exception(f"WhisperX failed to generate subtitle file in create_subtitle_from_media", {result.stderr})


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="The path to the input mp3 or mp4 file")
    parser.add_argument("output_file_dir", help="The path to the output subbed video file")
    parser.add_argument("--language", help="The language of the audio", default="en")
    parser.add_argument("--model", help="The model of the audio", default="large")
    args = parser.parse_args()

    create_subtitle_from_media(
        args.input_file,
        args.output_file_dir,
        args.language,
        args.model,
        args.dry_run,
    )
