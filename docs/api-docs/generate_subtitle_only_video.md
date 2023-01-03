<!-- markdownlint-disable -->

<a href="https://github.com/yasutak/karaokit/blob/main/generate_subtitle_only_video.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `generate_subtitle_only_video`





---

<a href="https://github.com/yasutak/karaokit/blob/main/generate_subtitle_only_video.py#L5"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `generate_subtitle_only_video`

```python
generate_subtitle_only_video(
    media_file: str,
    ass_file: str,
    output_file_dir: str,
    resolution: str = 'md',
    dry_run: bool = False
) → None
```

Generate a subbed video from an mp3 and ass file. 



**Args:**
 
 - <b>`mp3_file`</b> (str):  The path to the input mp3 file 
 - <b>`ass_file`</b> (str):  The path to the input ass file 
 - <b>`output_file_dir`</b> (str):  The path to the output subbed video file (.mp4 or .mkv) 
 - <b>`resolution`</b> (str, optional):  The resolution of the output video. Defaults to "md". 
 - <b>`dry_run`</b> (bool, optional):  If True, the ffmpeg command will not be run. Defaults to False. 


