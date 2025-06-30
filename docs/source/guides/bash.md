# Bash

> **Note:** This page is largely inspired by [https://intranet.neuro.polymtl.ca/geek-tips/bash-shell/README.html](https://intranet.neuro.polymtl.ca/geek-tips/bash-shell/README.html).

## References and tutorials

* [Bash scripting cheatsheet](https://devhints.io/bash)
* [Unix for Neuroimagers YouTube tutorial](https://www.youtube.com/playlist?list=PLIQIswOrUH69xOiblvvEz5KBwWaNRMEUp)

## File/Folders

### **Copy (and synchronize) with rsync**

```bash
rsync -azP <FILE_SRC> <FILE_DEST>
rsync -azP <FOLDER_SOURCE> <FOLDER_DEST>  # will create FOLDER_SOURCE inside FOLDER_DEST (if it does not exist), and will copy the content of FOLDER_SOURCE inside it
rsync -azP <FOLDER_SOURCE>/ <FOLDER_DEST>  # will copy the content of FOLDER_SOURCE inside FOLDER_DEST
# For nii.gz files, no need to further compress so -z can be dropped
```

### Finding

```bash
find . -name "dti*"
```

To be case-insensitive, use:
```bash
find . -iname "dti*"
```

To only look for folders/directories:
```bash
find . -type d -iname "dti*"
```

To only look for files:
```bash
find . -type f -iname "dti*.*"
```


### Deleting

#### **Delete non-empty folder**

```bash
rm -rf <FOLDER>
```

#### **Delete a bunch of files**

```bash
find . -name "dti*" -delete
```

or the more complicated version:

```bash
find . -name "dti*" | while read F; do rm $F; done
```

When you are trying to delete too many files using `rm`, you may get error message: `/bin/rm Argument list too long`. Use `xargs` to avoid this problem.

```bash
find ~ -name ‘*.log’ -print0 | xargs -0 rm -f
```

### Renaming

#### Rename files with a given extension

```bash
ls *.<EXT> | while read F; do mv $F <NEW_FILE_NAME>_$F; done
```

Do it recursively:

```bash
find . -name "t2_seg.nii.gz" -exec bash -c 'mv $(dirname $1)/$(basename $1) $(dirname $1)/t2_seg_manual.nii.gz' -- {} \;
```

**Do something on files modified for the past 10 days**

```bash
find . -type f -name '*.*' -mtime +10 -exec echo "do something on this file: {}" \;
```

**Set created/modification date on a file**

```bash
touch -mt YYYYMMDDhhmm <FILE>
```

On Maverick and later, the creation date is not updated if newer than the existing. So you should use:

```bash
SetFile -d 'DD/MM/YYYY HH:MM:SS' <FILE>
```


### Size of folder

```bash
du -sh <FOLDER>
```

or for all folders in the path

```
du -csh *
du -sm * | sort -nr  # in MB and reverse-ordered by size
du -hcs * | sort -h  # in human-readable
```


### Number of files

**Get number of files that match a pattern**

```
ls -dq *pattern* | wc -l
```

**Get number of files in a folder (recursively)**

```
find .//. ! -name . -print | grep -c //
```

only counts files modified for the past 24h:

```
find .//. ! -name . -mtime -1 -print | grep -c //
```

**List files modified for the past 24h**

```
find . -mtime -1 -print
```

List number of files per folder

```
find . -maxdepth 1 -mindepth 1 -type d -exec sh -c 'echo "{} : $(find "{}" -type f | wc -l)" file\(s\)' \;
```

### Permissions

#### **Change permissions**

```bash
chmod 644    # make a file readable by anyone and writable by the owner only.
chmod 755	 # make a file readable/executable by everyone and writable by the owner only.
chmod 701	 # r/w/x for the owner, no access for everyone
```

#### **Change owner of a file**

```bash
sudo chown <OWNER> <FILE>
```

#### **Look for group owner & permission**

```bash
ls -la
```

**Find most recently changed files (less than 1 day ago)**

```
find  -mtime -1 -ls
```

**Search files**

Files with specific string inside:

```
find . -name "string"
```

Files that have been modified for the past 24 hours:

```
find ~/Documents -type f -ctime -0 | more
```

## Compression/Extraction

### **tar**

compress:

```
tar -czf /path/to/output/folder/filename.tar.gz /path/to/folder
```

extract:

```
tar -zxvf filename.tar.gz
```

### **zip**

compress folder:

```
zip -r archive.zip folder/

# Exclude a sub-folder:
zip -r archive.zip folder/ -x '*subfoldertoexclude*'
```

extract:

```
unzip archive.zip
```

#### Checksum

This procedure creates a unique signature for your files and folders. It enables to check for integrity when you share data.

```
find FOLDER -type f -exec md5sum {} \; | md5sum
```

## .bash\_profile

The `.bash_profile` file is launched when you open a new terminal. You can configure your environment variables from there. It is located in your home folder (`$HOME`).

To load it:

```bash
source ~/.bash_profile
```

## Processes

### **Check Processes**

```
htop
```

### **Killing Processes**

#### **kill a process based on PID**

```bash
kill -9 <"PID">
```

#### **kill a process from a user**

```bash
pkill -U <USER> 
```

## Internet / Network

### Download file from internet

```bash
curl -o filename -L <URL>
# Example for OSF file (note the "?action=download" added after the URL):
curl -o data.zip -L https://osf.io/76jkx/?action=download
```

Alternatively:

```bash
wget -O data <URL>
```

### Copying

#### **Copy from a remote station**

```bash
rsync username@station.domain:</PATH/FILE> . # copy file
rsync -r username@station.domain:</PATH/> .  # copy folder
```

### Network

**Connect to another station**

```
ssh IP
or:
ssh username@station.domain
```

## Tmux (for background processes)

If you connect to a remote station and want to run a script for several hours, closing your laptop or disconnecting will stop the script unless you use a terminal multiplexer like `tmux`. `tmux` allows you to create persistent terminal sessions that continue running even if you disconnect.

Step-by-step procedure:

1. Connect to a station via `ssh`.
2. Start a new tmux session:
    ```bash
    tmux
    ```
    Or give your session a specific name:
    ```bash
    tmux new -s <SESSION_NAME>
    ```
3. Run your long process or script inside the tmux session.

Detach from the tmux session (leave it running in the background):

- Press <kbd>CTRL</kbd>+<kbd>B</kbd>, then <kbd>D</kbd>.

List all tmux sessions:

```bash
tmux ls
```

Reattach to a session:

```bash
tmux attach -t <SESSION_NAME>
```
Or, if you have only one session:
```bash
tmux attach
```

Kill a tmux session:

```bash
tmux kill-session -t <SESSION_NAME>
```

Scroll inside a tmux session:

- Press <kbd>CTRL</kbd>+<kbd>B</kbd>, then <kbd>[</kbd>. Use the arrow keys (<kbd>↑</kbd> and <kbd>↓</kbd>) to scroll.

For more advanced usage, see the [tmux cheat sheet](https://tmuxcheatsheet.com/).

## Nano Text Editor

A simple, user-friendly text editor available on most systems.

Basic commands (shown at the bottom of the editor):

- <kbd>Ctrl</kbd>+<kbd>O</kbd> : Write (save) file
- <kbd>Ctrl</kbd>+<kbd>X</kbd> : Exit
- <kbd>Ctrl</kbd>+<kbd>K</kbd> : Cut line
- <kbd>Ctrl</kbd>+<kbd>U</kbd> : Uncut (paste) line
- <kbd>Ctrl</kbd>+<kbd>W</kbd> : Search

To enable syntax highlighting, ensure you have the `nano` syntax files (usually enabled by default). You can customize highlighting in `~/.nanorc`.

Open a file with nano:

```bash
nano <filename>
```
