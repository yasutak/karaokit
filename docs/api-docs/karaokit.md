<!-- markdownlint-disable -->

<a href="https://github.com/yasutak/karaokit/blob/main/karaokit.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `karaokit`





---

<a href="https://github.com/yasutak/karaokit/blob/main/karaokit.py#L8"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `karaokit`

```python
karaokit(
    media_file: str,
    output_file_dir: str,
    language: str,
    model: str = 'large',
    resolution: str = 'md',
    dry_run: bool = False
) → None
```

Generate a subbed video from an media file. 



**Args:**
 
 - <b>`media_file`</b> (str):  The path to the input media file (mp3 or mp4) 
 - <b>`output_file_dir`</b> (str):  The path to the output subbed video file 
 - <b>`language`</b> (str):  The language of the media 
 - <b>`model`</b> (str, optional):  The size of the transcription model, Whisper. Defaults to "large". 
 - <b>`resolution`</b> (str, optional):  The resolution of the video. Defaults to "md". 


