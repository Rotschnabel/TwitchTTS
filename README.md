# TwitchTTS

## Installation with Python

1. Install the dependencies (gTTS, playsound, twitchio) via pip in the command line.

```bash
pip install -r requirements.txt
```

or with pipenv:

```bash
pipenv sync
pipenv shell
```

1. Visit http://twitchapps.com/tmi and get your oauth token

2. Configure

Copy `config.py.example` to `config.py`.
Change the `config.py`-variables to your needs.
Paste your generated oauth token into the "token" variable.

4. Simply run the script with python

```bash
python twitch_tts.py
```

### Ubuntu

TwitchTTS uses playsound witch requires gstreamer and its python bindungs.
To install on Ubuntu use:

```bash
sudo apt install python3-gst-1.0
```

### Windows

1. Unzip the archive.
2. Visit http://twitchapps.com/tmi and get your oauth token
2. Run "EDIT_CONFIGURATION.bat". That should open the config.py file in the bin folder. Paste your generated token into the "TOKEN" variable. Also change the "NICKNAME" variable to your twitch username.
3. (Optional) Change TTS_USERS or TTS_LANGUAGE, see NOTES below
4. Run "RUN_TTSBOT.bat" or alternatively the twitch_tts.exe in the bin folder.

## Notes
1. If you want only some users to be able to generate TTS, add them into the "TTS_USERS" list. e.g:

```
TTS_USERS = [ 'frankerz', 'alphastar', 'twitchbot123' ]
```

Tested with python 3.9.1 64bit on Windows 10

Reference:
https://twitchio.readthedocs.io/en/rewrite/twitchio.html
