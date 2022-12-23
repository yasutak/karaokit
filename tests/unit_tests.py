import pathlib
import sys
import unittest

sys.path.append("..")

from create_subtitle_from_audio import generate_subtitle_from_audio
from generate_subtitle_only_video import generate_subtitle_only_video
from karaokit import karaokit

if not pathlib.Path("output").exists():
    pathlib.Path("output").mkdir(parents=True, exist_ok=True)

ja_song_mp3_path = pathlib.Path("../examples/ja_song.mp3").resolve()
output_dir = pathlib.Path("../tests/output/").resolve()
ja_song_ass_path = pathlib.Path("../tests/output/ja_song.mp3.ass").resolve()


class TestGenerateSubtitleFileFromAudio(unittest.TestCase):
    def test_generate_subtitle_from_audio(self):
        generate_subtitle_from_audio(
            mp3_file=ja_song_mp3_path,
            output_file_dir=output_dir.__str__(),
            language="ja",
            model="tiny",
        )


class TestGenerateSubbedVideos(unittest.TestCase):
    def test_generate_subbed_video(self):
        generate_subbed_video(
            mp3_file=ja_song_mp3_path,
            ass_file=ja_song_ass_path,
            output_file_dir=output_dir.__str__(),
            resolution="md",
            dry_run=True,
        )


def suite():
    suite = unittest.TestSuite()
    suite.addTest(
        TestGenerateSubtitleFileFromAudio("test_generate_subtitle_from_audio")
    )
    suite.addTest(TestGenerateSubbedVideos("test_generate_subbed_video"))
    return suite


"""
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
"""

if __name__ == "__main__":
    runner = unittest.TextTestRunner(failfast=True)
    runner.run(suite())
