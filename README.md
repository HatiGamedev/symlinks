# Symlinks

Symlinks is a small python tool to setup and share symlink setups for multiple platforms.

Generally I use it to avoid having game project plugins / git projects contained inside a library folder.
Most useful it is to strip out specific parts of bigger (git) repositories. To avoid dealing with sub-folders.

Example:
```
<repo-root>
|
+ folderA
+ folderB
+ folderC
```

But your tool expects a flat hirarchy it becomes messy to include folderA,B,C into a flat hierarchy.

## Usage

To create symlinks from a definition use the following

```
py symlinks.py somefile.symlinks
```

The format of the file to use is the following:

```
SourceFolderPath -> ../../RelativeTarget
../RelativeSourceFolderPath -> C:/full/path/to/folder
# This is a comment
```

It will then only create symlinks for target folders that currently do not exist and "update" existing symlinks.
The tool will warn you about regular folders already existing in the target path and not overwrite / delete them if they are not symlinks yet.
