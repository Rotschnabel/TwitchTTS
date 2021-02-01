import os
import time

import playsound
from gtts import gTTS
from twitchio.ext import commands
from pydub import AudioSegment
from pydub.playback import play


from config import *


def speak(text):
    tts = gTTS(text=text, lang=TTS_LANGUAGE)
    filename = TEMPORARY_FILE
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(TEMPORARY_FILE)

def speakPyDub(text):
    tts = gTTS(text=text, lang=TTS_LANGUAGE)
    filename = TEMPORARY_FILE
    tts.save(filename)
    audio = AudioSegment.from_mp3(filename)
    play(audio)
    os.remove(TEMPORARY_FILE)

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            irc_token=TOKEN,
            client_id='...',
            nick=NICKNAME,
            prefix='!',
            initial_channels=[CHANNEL],
        )

    # Events don't need decorators when subclassed
    async def event_ready(self):
        print(f'Ready | {self.nick}')

    async def event_message(self, message):
        print(message.author.name + ': ' + message.content)
        # if userlist is empty or user exists in ttsusers-list
        if len(TTS_USERS) == 0 or TTS_USERS.count(message.author.name) == 1:
            speakPyDub(message.content)
            await self.handle_commands(message)
        else:
            pass

    # Commands use a decorator...
    @commands.command(name='test')
    async def my_command(self, ctx):
        await ctx.send(f'Hello {ctx.author.name}!')


bot = Bot()
bot.run()
