import discord
from discord.ext import commands
import random


# 起動時に通知してくれる処理
@client.event # イベントを受信するための構文（デコレータ）
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message): # 発言を受信したら処理をする関数
    # 「おはよう」で始まるか調べる
    if message.content.startswith("おはよう"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージを書きます
            m = "おはようございます" + message.author.name + "さん！"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await client.send_message(message.channel, m)
# 「/neko」と発言したら「にゃーん」が返る処理
@client.event
async def on_message(message):
    if message.content.startswith('/neko'):
        reply = 'にゃーん'
        await client.send_message(message.channel, reply)

bot.run("NTYwMzc0OTgyNzU3MTg3NTg1.XLFPpw.h_oh6Be4PfZm40rZvyo589oc7IM")
