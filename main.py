import discord
import os
from discord.ext import commands

CHANNEL_ID=1064875419184148490
client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    # 起動したらターミナルにログイン通知が表示される
    print('ログインしました')
    await greet()

async def greet():
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('我が名はmkdk･･･起動完了')


@client.event
async def on_message(message):
    # メッセージ送信者がBotだった場合は無視する
    if message.author.bot:
        return
    # 「oimo」と発言したら「おいも」が返る処理
    if message.content in ['すみません','すみません！','すみません。','すみませんでした','ごめんなさい']:
        await message.channel.send('謝罪をするな！')
    elif message.content == '金子くん、それは謝ったほうがいいよ':
        await message.channel.send('謝罪をしろ！')


client.run(os.environ["DISCORD_TOKEN"])
