import pathlib

from add_subtitle_to_video import add_subtitle_to_video
from create_subtitle_from_media import create_subtitle_from_media
from generate_subtitle_only_video import generate_subtitle_only_video


def karaokit(
    media_file: str,
    output_file_dir: str,
    language: str,
    model: str = "large",
    resolution: str = "md",
    dry_run: bool = False,
) -> None:
    """Generate a subbed video from an media file.

    Args:
        media_file (str): The path to the input media file (mp3 or mp4)
        output_file_dir (str): The path to the output subbed video file
        language (str): The language of the media
        model (str, optional): The size of the transcription model, Whisper. Defaults to "large".
        resolution (str, optional): The resolution of the video. Defaults to "md".
    """

    create_subtitle_from_media(
        media_file=media_file,
        output_file_dir=output_file_dir,
        language=language,
        model=model,
        dry_run=dry_run,
    )
    stem_file_name = pathlib.Path(media_file).stem
    if media_file.__str__().endswith(".mp3"):
        generate_subtitle_only_video(
            media_file=media_file,
            ass_file=f"{output_file_dir}/{stem_file_name}.ass",
            output_file_dir=output_file_dir,
            resolution=resolution,
            dry_run=dry_run,
        )
    elif media_file.__str__().endswith(".mp4"):
        add_subtitle_to_video(
            media_file=media_file,
            ass_file=f"{output_file_dir}/{stem_file_name}.ass",
            output_file_dir=output_file_dir,
            resolution=resolution,
            dry_run=dry_run,
        )
    else:
        raise Exception(f"Input file must be mp3 or mp4, not {media_file.__str__().split('.')[-1]}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("media_file", help="The path to the input media file (mp3 or mp4)")
    parser.add_argument(
        "--output_file_dir",
        help="The path to the output subbed video file",
        default="output",
    )
    parser.add_argument("--language", help="The language of the media", default="ja")
    parser.add_argument("--model", help="The model of the media", default="large")
    parser.add_argument("--resolution", help="The resolution of the video", default="md")
    parser.add_argument("--dry_run", help="Dry run", default=False)

    args = parser.parse_args()

    karaokit(
        media_file=args.media_file,
        output_file_dir=args.output_file_dir,
        language=args.language,
        model=args.model,
        resolution=args.resolution,
        dry_run=args.dry_run,
    )
