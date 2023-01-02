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


def generate_subtitle_from_media(
    input_file: str,
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

    if input_file.endswith(".mp4"):
        input_file = convert_mp4_to_mp3(input_file=input_file)

    wihsperx_command = [
        "whisperx",
        "--model",
        model,
        "--language",
        language,
        input_file,
        "--output_dir",
        output_file_dir,
    ]

    subprocess.run(wihsperx_command)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("input_file", help="The path to the input mp3 mp3 file")
    parser.add_argument(
        "output_file_dir", help="The path to the output subbed video file"
    )
    parser.add_argument("--language", help="The language of the audio", default="en")
    parser.add_argument("--model", help="The model of the audio", default="large")
    args = parser.parse_args()

    generate_subtitle_from_media(
        args.input_file,
        args.output_file_dir,
        args.language,
        args.model,
        args.dry_run,
    )