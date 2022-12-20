import pathlib
import sys
import unittest

sys.path.append("..")

from create_subtitle_from_audio import generate_subtitle_file_from_audio
from generate_subbed_video import generate_subbed_video

ja_song_mp3_path = pathlib.Path("../examples/ja_song.mp3").resolve()
ja_song_ass_path = pathlib.Path("../examples/ja_song.ass").resolve()
output_ja_song_ass_path = pathlib.Path("../examples/output_ja_song.ass")
output_ja_song_mp4_path = pathlib.Path(
    "../examples/output_ja_song.mp4"
).resolve()


class TestGenerateSubtitleFileFromAudio(unittest.TestCase):
    def test_generate_subtitle_file_from_audio(self):
        generate_subtitle_file_from_audio(
            mp3_file=ja_song_mp3_path,
            output_file=output_ja_song_ass_path,
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


if __name__ == "__main__":
    unittest.main()
