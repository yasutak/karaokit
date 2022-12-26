import subprocess


def generate_subtitle_from_audio(mp3_file: str, output_file_dir: str, language: str, model: str = "large") -> None:
    """Generate a subtitle file from an mp3 file with whisperX.

    Args:
        mp3_file (str): The path to the input mp3 file
        output_file_dir (str): The path to the output subtitle
        language (str): The language of the audio
        model (str, optional): The model of the audio. Defaults to "large".
    """
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
        raise Exception(f"WhisperX failed to generate subtitle file, {result.stderr}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("mp3_file", help="The path to the input mp3 mp3 file")
    parser.add_argument("output_file_dir", help="The path to the output subbed video file")
    parser.add_argument("--language", help="The language of the audio", default="en")
    parser.add_argument("--model", help="The model of the audio", default="large")
    args = parser.parse_args()

    generate_subtitle_from_audio(
        args.mp3_file,
        args.output_file_dir,
        args.language,
        args.model,
        args.dry_run,
    )
