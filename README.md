# TwitchTTS

## Installation with Python

1. Install the dependencies (gTTS, playsound, twitchio) via pip in the command line.

```
pip install -r requirements.txt
```

or with pipenv:

```
pipenv sync
pipenv shell
```

1. Visit http://twitchapps.com/tmi and get your oauth token

2. Configure

Copy `config.py.example` to `config.py`.
Change the `config.py`-variables to your needs.
Paste your generated oauth token into the "token" variable.

4. Simply run the script with python

```
python twitch_tts.py
```

## Installation on Windows
1. Unzip the archive.
2. Visit http://twitchapps.com/tmi and get your oauth token
2. open config.py and change paste your generated token into the "TOKEN" variable. Also change the "NICKNAME" variable to your twitch username.
3. (Optional) Change TTS_USERS or TTS_LANGUAGE, see NOTES below

## Notes
1. If you want only some users to be able to generate TTS, add them into the "TTS_USERS" list. e.g:

```
TTS_USERS = [ 'frankerz', 'alphastar', 'twitchbot123' ]
```

Tested with python 3.9.1 64bit on Windows 10

Refference:
https://www.learndatasci.com/tutorials/how-stream-text-data-twitch-sockets-python/
