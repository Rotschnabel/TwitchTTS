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

2. Visit http://twitchapps.com/tmi and get your oauth token

3. Change the "nickname" and "channel" variables to your twitch username.
   Change the "token" variable to match your generated oauth token.
   
4. Simply run the script with python
```
python twitch_tts.py
```


## Notes
Tested with python 3.9.1 64bit on Windows 10
