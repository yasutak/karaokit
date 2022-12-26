import pathlib
import sys
import unittest

sys.path.append("..")

from add_subtitle_to_video import add_subtitle_to_video
from create_subtitle_from_media import create_subtitle_from_media
from generate_subtitle_only_video import create_subtitle_only_video
from karaokit import karaokit

if not pathlib.Path("output").exists():
    pathlib.Path("output").mkdir(parents=True, exist_ok=True)

ja_song_mp3_path = pathlib.Path("../examples/ja_song.mp3").resolve()
ja_song_mp4_path = pathlib.Path("../examples/ja_song.mp4").resolve()
ja_song_ass_path = pathlib.Path("../examples/ja_song.ass").resolve()
output_dir = pathlib.Path("../tests/output/").resolve()


class TestKaraokit(unittest.TestCase):
    def test_karaokit_audio(self):
        karaokit(
            mp3_file=ja_song_mp3_path,
            output_file_dir=".",
            language="ja",
            model="large",
            resolution="md",
            dry_run=False,
        )

    def test_karaokit_video(self):
        karaokit(
            mp4_file=ja_song_mp3_path,
            output_file_dir=".",
            language="ja",
            model="large",
            resolution="md",
            dry_run=False,
        )


if __name__ == "__main__":
    unittest.main()
