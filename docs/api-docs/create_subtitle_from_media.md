<!-- markdownlint-disable -->

<a href="https://github.com/yasutak/karaokit/blob/main/create_subtitle_from_media.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `create_subtitle_from_media`





---

<a href="https://github.com/yasutak/karaokit/blob/main/create_subtitle_from_media.py#L5"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `convert_mp4_to_mp3`

```python
convert_mp4_to_mp3(input_file: str) → str
```

Convert an mp4 file to an mp3 file. 



**Args:**
 
 - <b>`input_file`</b> (str):  The path to the input mp4 file 



**Returns:**
 
 - <b>`str`</b>:  The path to the output mp3 file 


---

<a href="https://github.com/yasutak/karaokit/blob/main/create_subtitle_from_media.py#L31"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `create_subtitle_from_media`

```python
create_subtitle_from_media(
    media_file: str,
    output_file_dir: str,
    language: str,
    model: str = 'large',
    dry_run: bool = False
) → None
```

Generate a subtitle file from an mp3 file with whisperX. 



**Args:**
 
 - <b>`input_file`</b> (str):  The path to the input file (mp3 or mp4) 
 - <b>`output_file_dir`</b> (str):  The path to the output subtitle 
 - <b>`language`</b> (str):  The language of the audio 
 - <b>`model`</b> (str, optional):  The model of the audio. Defaults to "large". 


