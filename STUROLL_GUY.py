import discord
import os
client = discord.Client()

@client.event
async def on_ready():
    print("""내 목숨을 "MGLD"에!""".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == 'ㅏㅡㅑ명령어':
        await message.channel.send('ㅏㅡㅑ안녕, ㅏㅡㅑ샌즈, ㅏㅡㅑ우주최강PSG, ㅏㅡㅑ주원, ㅏㅡㅑ, ㅏㅡㅑ24시간구동, ㅏㅡㅑ내목숨을**에!, ㅏㅡㅑ친구얼굴놀리는건')
    if message.content == 'ㅏㅡㅑ안녕':
        await message.channel.send('으응...(아 찐따새끼)')
    if message.content == 'ㅏㅡㅑ샌즈':
        await message.channel.send('와 샌즈! 언더테일 아시는구나! 혹시 모르시는분들에 대해 설명해드립니다 샌즈랑 언더테일의 세가지 엔딩루트중 몰살엔딩의 최종보스로 진.짜.겁.나.어.렵.습.니.다 공격은 전부다 회피하고 만피가 92인데 샌즈의 공격은 1초당 60이 다는데다가 독뎀까지 추가로 붙어있습니다.. 하지만 이러면 절대로 게임을 깰 수 가없으니 제작진이 치명적인 약점을 만들었죠. 샌즈의 치명적인 약점이 바로 지친다는것입니다. 패턴들을 다 견디고나면 지쳐서 자신의 턴을 유지한채로 잠에듭니다. 하지만 잠이들었을때 창을옮겨서 공격을 시도하고 샌즈는 1차공격은 피하지만 그 후에 바로날아오는 2차 공격을 맞고 죽습니다')
    if message.content == 'ㅏㅡㅑ주원':
        await message.channel.send('병신 아 아니...멋진 사람^^;;ㅎ')
    if message.content == 'ㅏㅡㅑ우주최강PSG':
        await message.channel.send('아 PSG아는구나 진짜 ㅈㄴ 최강이긴하지 만약 팬이 아니라면 어서 팬이 돼라!')
    if message.content == 'ㅏㅡㅑMGLD':
        await message.channel.send('위-대-한-우-리-의-***')
    if message.content == 'ㅏㅡㅑ':
        await message.channel.send('ㅏㅡㅑ')
    if message.content == 'ㅏㅡㅑ24시간구동':
        await message.channel.send('몰라 나도 하고싶어 시발')
    if message.content == 'ㅏㅡㅑ내목숨을MGLD에!':
        await message.channel.send('뭐야 이 명령어 어떻게알았어 좀치네? https://open.kakao.com/o/syMgSMvd')
    if message.content == 'ㅏㅡㅑ내목숨을**에!':
        await message.channel.send('야레야레다나')
    if message.content == '와!':
        await message.channel.send('샌즈!')
    if message.content == '언더테일':
        await message.channel.send('아시는구나 혹시 모르시는분들에 대해 설명해드립니다 샌즈랑 언더테일의 세가지 엔딩루트중 몰살엔딩의 최종보스로 진.짜.겁.나.어.렵.습.니.다 공격은 전부다 회피하고 만피가 92인데 샌즈의 공격은 1초당 60이 다는데다가 독뎀까지 추가로 붙어있습니다.. 하지만 이러면 절대로 게임을 깰 수 가없으니 제작진이 치명적인 약점을 만들었죠. 샌즈의 치명적인 약점이 바로 지친다는것입니다. 패턴들을 다 견디고나면 지쳐서 자신의 턴을 유지한채로 잠에듭니다. 하지만 잠이들었을때 창을옮겨서 공격을 시도하고 샌즈는 1차공격은 피하지만 그 후에 바로날아오는 2차 공격을 맞고 죽습니다')
    if message.content == 'ㅏㅡㅑ친구얼굴놀리는건':
        await message.channel.send('나빠요~') 
    if message.content == 'ㅏㅡㅑ김영재':
        await message.channel.send('유행어로는 억까하지마세요. 가있고 특징으로는 폰을 절대 사용하지 않는 사람이다. 물론 전화도 받지 않는다.')
    if message.content == 'ㅏㅡㅑ무경':
        await message.channel.send('해적왕이 될 아 아니 제 2의 일론머스크가 될 거야!')
    if message.content == 'ㅏㅡㅑ공민재':
        await message.channel.send('희대의 찐따. 본인은 인싸이며 잘생겼다고 생각한다')   
    if message.content == 'ㅏㅡㅑ정뽀뽀':
        await message.channel.send('천국에서 기다리고 있을거에요')
    if message.content == 'ㅏㅡㅑ롤':
        await message.channel.send('Tlqkf 팀운 ㅈ망겜 내 MMR어떡해 ㅠㅠㅠ')
    if message.content == 'ㅏㅡㅑㅇㅅㅇ':
        await message.channel.send('군~~~바')
    if message.content == '5+5':
        await message.channel.send('7')
    if message.content == 'ㅏㅡㅑ정5':
        await message.channel.send('병정5신(전 시켜서 한 것 입니다 절대 자의로 하지 않았어요)')
    if message.content == 'ㅏㅡㅑ협박받은명령어':
        await message.channel.send('병정5신 밖에 없어요')
    if message.content == 'ㅏㅡㅑ신중한신중':
        await message.channel.send('"신중하지 않은" 신중')
    if message.content == 'ㅏㅡㅑ김기태':
        await message.channel.send('"광장중학교" 외모 TOP3')
    if message.content == '아 그 병신같은 봇?':
        await message.channel.send('98년도 틀딱겜 기반으로한 봇이 지랄하네')
    if message.content == '병신같은 봇이 지랄하네 ㅋ':
        await message.channel.send('진짜 뒤질라고')
access_token = os.environ["BOT_TOKEN"]
client.run('access_token')


