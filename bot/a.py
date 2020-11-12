import os
from discord.ext import commands

bot = commands.Bot(command_prefix="/")
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")

@bot.command()
async def 야스(ctx):
    await ctx.send("야스봇 v7.0")
    await ctx.send("명령어 목록입니다. 모든 명령어 앞에는 /를 입력하세요.")
    await ctx.send("/오늘 : 오늘의 날짜를 알려드립니다.")
    await ctx.send("/시간 : 지금 시간을 알려드립니다.")
    await ctx.send("/숙제 : 현재 해야 할 숙제를 알려드립니다.")
    await ctx.send("/(요일)시간표(ex. /월시간표) : 월요일 ~ 금요일까지의 시간표를 알려드립니다.")
    await ctx.send("/따라하기 (적을거) : 말을 따라합니다. /따라하기 뒤에 띄어쓰기를 해야 제대로 실행됩니다.")
    await ctx.send("/주사위 : 1부터 6까지 중 숫자 하나를 무작위로 뽑습니다.")
    await ctx.send("/유튭 : 이 봇 제작자의 유튜브 채널 주소를 알려드립니다.")
    await ctx.send("/코 : 중국산 코로나 관련 정보를 알려드립니다.")
    await ctx.send("/숨목록 : 숨겨진 명령어 목록을 알려드립니다.")
    await ctx.send("/역사 : 역사 시험범위 제외 부분을 알려드립니다.")

@bot.command()
async def hhub(ctx):
    await ctx.send("www.pornhub.com")
    await ctx.send("DNS 쓰는 거 아시죠?")

@bot.command()
async def 숨숨목록(ctx):
    await ctx.send("/hhub : 그 허브 주소를 알려드립니다.")
    await ctx.send("/xx : 그 Videos 주소를 알려드립니다.")

@bot.command()
async def 숨목록(ctx):
    await ctx.send("숨겨진 명령어 목록입니다. 여기 명령어들은 대부분 슬래쉬가 필요 없습니다.(있는 것은 슬래쉬 쳐져있음)")
    await ctx.send("fuck(또는 Fuck) : Lily Allen의 Fuck You 음악 뮤비 유튜브 주소를 보여드립니다.")
    await ctx.send("/섹온비 : 섹온비 유튜브 주소를 띄웁니다.")
    await ctx.send("/ijhs : Lonely Island의 I Just Had Sex 유튜브 뮤비 주소를 띄웁니다.")
    await ctx.send("/숨숨목록 : 궁금하면 해보세요")

@bot.command()
async def xx(ctx):
    await ctx.send("xvideos.com")
    await ctx.send("DNS 쓰는 거 아시죠?")

@bot.command()
async def 버스티드():
    await ctx.send("Busted")
    await ctx.send("머스타드")

@bot.command()
async def 따라하기(ctx, *, text):
    await ctx.send(text)

if __name__ == "__main__":
    bot.run(TOKEN)
