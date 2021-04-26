![github version](https://d25lcipzij17d.cloudfront.net/badge.svg?id=gh&type=6&v=2.0.1&x2=0)
# FFXIV Auto Crafter
Terminal tool for FFXIV crafting

---

## Setup :wrench:
Install Python for Windows
https://www.python.org/downloads/windows/

### Download 64 bit and run it
```Download Windows x86-64 executable installer```

### Check PATH during installation
![path_check](../assets/pythonpathcheck.PNG)

### Requirements
Run/double-click `cmd.bat`

It should make an env\ folder and install python requirements

### Caveats
In order to be fully automatic while doing other things in the background, **FFXIV needs to be in windowed mode on your display #2**

![ffxivauto2](../assets/ffxivauto2.PNG)

![ffxivauto1](../assets/ffxivauto1.png)

---

## Instructions
#### Make a text file in the macros\\ folder with the key you press for your macro, and the macro below it like in the image below:
![demo1](../assets/demo1.PNG)

### Creating a macro profile
The text file you created is the macro profie
List your profiles with:
```
python main.py list
```

### Updating a macro profile
Update the text file, it will immediately change after saving the file

### Deleting a macro profile
To delete a profile, delete the text file.

### Crafting with a macro profile
Before starting the craft command:
 - Make sure **only** your craft window is out
 - The craft you want to do is highlighted
 - Your last action was **not** a chat message
 
Start crafting with this command in cmd:
```
python main.py craft whitescripts 8
```
* python main.py craft PROFILE_NAME CRAFT_AMOUNT


### Crafting options
WIP

---

## Auto Cookie (BETA)

Automatically turn in cookie leves

### Requirements

**2 macros**
 - key 1: `/tnpc`
 - key 2: `/ta <f>`

### Setup
- [https://sourceforge.net/projects/capture2text/files/Capture2Text/Capture2Text_v4.6.2/](https://sourceforge.net/projects/capture2text/files/Capture2Text/Capture2Text_v4.6.2/)
  - Download the 64bit ver zip file
- Unzip the folder in `utils/`
- Run the .exe version to find your window location for converting immage to text
- Set the window position in autoleve_settings.py
- Set your language in autoleve_settings.py

### Instructions

- Move FFXIV to your sub monitor (If you want to full auto afk)
- Button 1 will handle targeting Eirikur
- Focus target Moyce, and button 2 will handle targeting Moyce.
- Stand in FRONT of Eirikur
- Run the program on your main monitor

---

## Author
* [kai-dg](https://github.com/kai-dg)
