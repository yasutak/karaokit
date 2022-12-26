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


class TestGenerateSubtitleFileFromAudio(unittest.TestCase):
    def test_generate_subtitle_from_audio(self):
        create_subtitle_from_media(
            input_file=ja_song_mp3_path.__str__(),
            output_file_dir=output_dir.__str__(),
            language="ja",
            model="tiny",
        )


class TestGenerateSubbedVideos(unittest.TestCase):
    def test_generate_subbed_video(self):
        create_subtitle_only_video(
            mp3_file=ja_song_mp3_path,
            ass_file=ja_song_ass_path,
            output_file_dir=output_dir.__str__(),
            resolution="md",
            dry_run=True,
        )


class TestAddSubtitleToVideo(unittest.TestCase):
    def test_add_subtitle_to_video(self):
        add_subtitle_to_video(
            mp3_file=ja_song_mp3_path,
            ass_file=ja_song_ass_path,
            output_file_dir=output_dir.__str__(),
            resolution="md",
            dry_run=False,
        )


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
    runner = unittest.TextTestRunner(failfast=True)
    runner.run(suite())
