import discord
import asyncio
import random
from time import sleep

client = discord.Client()

@client.event
async def on_ready():
    print('Pronto')

@client.event
async def on_member_join(member):
    canal = client.get_channel('470017776120102923')
    regras = client.get_channel('470029497303957507')
    msg = "Bem vindo, {}! Leia as {}!".format(member.mention, regras.mention)
    await client.send_message(canal, msg)


@client.event
async def on_message(message):
    if message.channel == client.get_channel('470024457755426827'):
        if message.content.lower().startswith('a!guess'):
            escolha = random.randint(0, 10)
            await client.send_message(message.channel, 'Tente adivinhar um número que eu pensei de 0 a 10;')
            palpite = await client.wait_for_message(timeout=999, author=message.author)
            try:
                while True:
                    if int(palpite.content) == escolha:
                        await client.send_message(message.channel, "Parabéns, você acertou!")
                        break
                    elif int(palpite.content) > escolha:
                        await client.send_message(message.channel, "Tente um número menor.")
                        palpite = await client.wait_for_message(timeout=999, author=message.author)
                    elif int(palpite.content) < escolha:
                        await client.send_message(message.channel, 'Tente um número maior.')
                        palpite = await client.wait_for_message(timeout=999, author=message.author)
            except TypeError:
                await client.send_message(message.channel, 'Você não digitou um número inteiro, ou não digitou um número. Tente novamente.')
        if message.content.lower().startswith('a!jokenpo'):
            await client.send_message(message.channel, '[ 0 ] para PEDRA'
                                                       '\n[ 1  ] para PAPEL'
                                                       '\n[ 2 ] para TESOURA')
            jogada_c = random.randint(0, 2)
            jogada = await client.wait_for_message(timeout=999, author=message.author)
            await client.send_message(message.channel, 'JO...')
            sleep(2)
            await client.send_message(message.channel, 'KEN...')
            sleep(2)
            await client.send_message(message.channel, 'PÔ!!!')
            sleep(1.5)
            if int(jogada.content) == jogada_c:
                await client.send_message(message.channel, 'Empate! Fim de jogo.')
            if int(jogada.content) == 0 and jogada_c == 1:
                await client.send_message(message.channel, 'Eu ganhei! Fim de jogo.')
            if int(jogada.content) == 0 and jogada_c == 2:
                await client.send_message(message.channel, 'Você ganhou! Fim de jogo.')
            if int(jogada.content) == 1 and jogada_c == 0:
                await client.send_message(message.channel, 'Você ganhou! Fim de jogo.')
            if int(jogada.content) == 1 and jogada_c == 2:
                await client.send_message(message.channel, 'Eu ganhei! Fim de jogo.')
            if int(jogada.content) == 2 and jogada_c == 0:
                await client.send_message(message.channel, 'Eu ganhei! Fim de jogo.')
            if int(jogada.content) == 2 and jogada_c == 1:
                await client.send_message(message.channel, 'Você ganhou! Fim de jogo.')
    else:
        msg = await client.send_message(message.channel, 'Comandos apenas em {}!'.format(client.get_channel('470024457755426827').mention))
        sleep(1.5)
        await client.delete_message(msg)

client.run("NDcwMDIzNDg5NTc1ODQ1ODg5.DjQRAQ.yArFU1fmyQ14cS4PkVTmIS6llxE")