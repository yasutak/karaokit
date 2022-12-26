import pathlib
import subprocess


def generate_subtitle_only_video(
    mp3_file: str,
    ass_file: str,
    output_file_dir: str,
    resolution: str = "md",
    dry_run: bool = False,
) -> None:
    """Generate a subbed video from an mp3 and ass file.

    Args:
        mp3_file (str): The path to the input mp3 file
        ass_file (str): The path to the input ass file
        output_file_dir (str): The path to the output subbed video file (.mp4 or .mkv)
        resolution (str, optional): The resolution of the output video. Defaults to "md".
        dry_run (bool, optional): If True, the ffmpeg command will not be run. Defaults to False.
    """
    if resolution == "lg":
        resolution = "4504X2000"
    elif resolution == "md":
        resolution = "2252X1000"
    elif resolution == "sm":
        resolution = "1126X500"
    elif resolution == "xs":
        resolution = "563X250"

    dry_run = ["-f", "null -"] if dry_run else []
    output_file_name = pathlib.Path(mp3_file).stem + ".mp4"
    ffmpeg_command = [
        "ffmpeg",
        "-f",
        "lavfi",
        "-i",
        f"color=size={resolution}:rate=25:color=black",
        "-i",
        mp3_file,
        "-vf",
        f"subtitles={ass_file}:force_style='Fontsize=40",
        "-shortest",
        output_file_dir.__str__() + "/" + output_file_name,
    ] + dry_run
    subprocess.run(ffmpeg_command)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("mp3_file", help="The path to the input mp3 file")
    parser.add_argument("ass_file", help="The path to the input ass subtitle file")
    parser.add_argument("output_file_dir", help="The path to the output subbed video file")
    parser.add_argument("--resolution", help="The resolution of the output video", default="md")
    parser.add_argument(
        "--dry_run",
        help="If True, the ffmpeg command will not be run",
        default=False,
    )
    args = parser.parse_args()

    generate_subtitle_only_video(
        args.mp3_file,
        args.ass_file,
        args.output_file_dir,
        args.resolution,
        args.dry_run,
    )
