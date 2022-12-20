import pathlib
import sys
import unittest

sys.path.append("..")

from create_subtitle_from_audio import generate_subtitle_from_audio
from generate_subbed_video import generate_subbed_video
from karaokit import karaokit

ja_song_mp3_path = pathlib.Path("../examples/ja_song.mp3").resolve()
ja_song_ass_path = pathlib.Path("../examples/ja_song.ass").resolve()
output_ja_song_ass_path = pathlib.Path("../examples/output_ja_song.ass")
output_ja_song_mp4_path = pathlib.Path(
    "../examples/output_ja_song.mp4"
).resolve()


class TestGenerateSubtitleFileFromAudio(unittest.TestCase):
    def test_generate_subtitle_from_audio(self):
        generate_subtitle_from_audio(
            mp3_file=ja_song_mp3_path,
            output_file=output_ja_song_ass_path.__str__(),
            language="ja",
            model="large",
        )


class TestGenerateSubbedVideos(unittest.TestCase):
    def test_generate_subbed_video(self):
        generate_subbed_video(
            mp3_file=ja_song_mp3_path,
            ass_file=ja_song_ass_path,
            output_file=output_ja_song_mp4_path,
            resolution="md",
            dry_run=True,
        )


class TestKaraokit(unittest.TestCase):
    def test_karaokit(self):
        karaokit(
            mp3_file=ja_song_mp3_path,
            output_file_dir=".",
            language="ja",
            model="large",
            resolution="md",
            dry_run=False,
        )


if __name__ == "__main__":
    unittest.main()
