import pathlib

from create_subtitle_from_media import generate_subtitle_from_media
from generate_subtitle_only_video import generate_subtitle_only_video


def karaokit(
    mp3_file: str,
    output_file_dir: str,
    language: str,
    model: str = "large",
    resolution: str = "md",
    dry_run: bool = False,
) -> None:
    """Generate a subbed video from an mp3 file.

    Args:
        mp3_file (str): The path to the input mp3 file
        output_file_dir (str): The path to the output subbed video file
        language (str): The language of the audio
        model (str, optional): The model of the audio. Defaults to "large".
        resolution (str, optional): The resolution of the video. Defaults to "md".
    """

    generate_subtitle_from_media(
        mp3_file=mp3_file,
        output_file_dir=output_file_dir,
        language=language,
        model=model,
        dry_run=dry_run,
    )
    stem_file_name = pathlib.Path(mp3_file).stem
    generate_subtitle_only_video(
        mp3_file=mp3_file,
        ass_file=f"{output_file_dir}/{stem_file_name}.ass",
        output_file_dir=output_file_dir,
        resolution=resolution,
        dry_run=dry_run,
    )


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("mp3_file", help="The path to the input mp3 mp3 file")
    parser.add_argument(
        "--output_file_dir",
        help="The path to the output subbed video file",
        default="output",
    )
    parser.add_argument("--language", help="The language of the audio", default="ja")
    parser.add_argument("--model", help="The model of the audio", default="large")
    parser.add_argument(
        "--resolution", help="The resolution of the video", default="md"
    )
    parser.add_argument("--dry_run", help="Dry run", default=False)

    args = parser.parse_args()

    karaokit(
        mp3_file=args.mp3_file,
        output_file_dir=args.output_file_dir,
        language=args.language,
        model=args.model,
        resolution=args.resolution,
        dry_run=args.dry_run,
    )
