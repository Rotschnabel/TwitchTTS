from gtts import gTTS
import os
import time
import playsound
from twitchio.ext import commands

#https://www.learndatasci.com/tutorials/how-stream-text-data-twitch-sockets-python/


def speak(text):
    tts = gTTS(text=text, lang='de') # change de to e.g en for english
    filename = 'tts.mp3'
    tts.save(filename)
    playsound.playsound(filename)
    os.remove('tts.mp3')

server = 'irc.chat.twitch.tv'
port = 6667
nickname = 'username' #paste your twitch username here
token = 'oauth:m14t7y8q1d20fcm653bdj2eoarl6zhg' # (example key) paste your oauth-key here, you get it from: #http://twitchapps.com/tmi
channel = 'username' #paste your twitch username here




class Bot(commands.Bot):
    def __init__(self):
        super().__init__(irc_token=token, client_id='...', nick=nickname, prefix='!',
                         initial_channels=[channel])

    # Events don't need decorators when subclassed
    async def event_ready(self):
        print(f'Ready | {self.nick}')

    async def event_message(self, message):
        print(message.author)
        speak(message.content)
        await self.handle_commands(message)

    # Commands use a decorator...
    @commands.command(name='test')
    async def my_command(self, ctx):
        await ctx.send(f'Hello {ctx.author.name}!')


bot = Bot()
bot.run()