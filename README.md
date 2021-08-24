# MuxsX
#### Introduction

###### It is used to process large files, rename, sort, and number. You can build scripts for subsequent file processing. But this is only in the concept, the code is still in the test phase!

 · Building, please stay tuned
 · 건물, 계속 지켜봐주십시오.
 · 建物は、ご期待ください

#### Install

```
↪ sudo ln -s ~/Downloads/GitHub/MuxsX/muxsx.command /usr/local/bin/muxsx
```

#### Description
 `usage: muxsx [-h] [-d delelt] [-a add] [-r replace] [-type Type] [-dx DeleteFile] [-s] [-F Filter] path`


 optional arguments:
  | 参数 | 说明 |
  | :-----| :------|
  |*positional arguments*||
  |**path** |Specify the file path, which can be a folder or file name |
  |*optional arguments:*||
  |-h, --help|show this help message and exit|
  |-d delete |Delete specified characters，Ex -d xxx or -d xxx,yyy,zzz|
  |-a add|Add string to file name -a ddd or -a ddd@-5|
  |-r Replace|Replace the string specified in the file name -r xxx:yyyy|
  |-type type|Specify file type -type mp4 or -type "mp4|jpg"|
  |-dx delete from file|Read the file to delete the list, then modify the file -dx ~/deldict[file]|
  |-p path|Specify the file path, which can be a folder or file name|
  |-F Filter|Regular expression filtering file list|
  |-s | show file list|

#### Examples
```
muxsx -p ~/Downloads -type mkv -dx Examples
```
###### Examples: This is a file, the project has `Examples` file, one word per line, no comment support


------
 `JogFeelingVI`

