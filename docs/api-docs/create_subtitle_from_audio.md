<!-- markdownlint-disable -->

<a href="https://github.com/yasutak/karaokit/blob/main/create_subtitle_from_audio.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `create_subtitle_from_audio`





---

<a href="https://github.com/yasutak/karaokit/blob/main/create_subtitle_from_audio.py#L4"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `create_subtitle_from_audio`

```python
create_subtitle_from_audio(
    mp3_file: str,
    output_file_dir: str,
    language: str,
    model: str = 'large'
) → None
```

Generate a subtitle file from an mp3 file with whisperX. 



**Args:**
 
 - <b>`mp3_file`</b> (str):  The path to the input mp3 file 
 - <b>`output_file_dir`</b> (str):  The path to the output subtitle 
 - <b>`language`</b> (str):  The language of the audio 
 - <b>`model`</b> (str, optional):  The model of the audio. Defaults to "large". 


