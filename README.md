# TwitchTTS

## Installation

1. Install the dependencies (gTTS, playsound, twitchio) via pip in the command line.

```
pip install gTTS && pip install playsound && pip install twitchio
```

or seperately:

```
pip install gTTS
pip install playsound
pip install twitchio
```

or with pipenv:

```
pipenv sync
pipenv shell
```

2. Visit http://twitchapps.com/tmi and get your oauth token

3. Change the "nickname" and "channel" variables to your twitch username.
Paste your generated oauth token into the "token" variable.

4. Simply run the script with python
5. 
```
python twitch_tts.py
```


## Notes
1. If you want only some users to be able to generate TTS, add them into the "ttsusers" list.
e.g: 
```
ttsusers=['frankerz','alphastar','twitchbot123']
```

Tested with python 3.9.1 64bit on Windows 10
