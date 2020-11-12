import os
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")

@bot.command()
async def 야스(ctx):
    await ctx.send("야스봇 v7.0")
    await ctx.send("명령어 목록입니다. 모든 명령어 앞에는 !를 입력하세요.")
    await ctx.send("!오늘 : 오늘의 날짜를 알려드립니다.")
    await ctx.send("!시간 : 지금 시간을 알려드립니다.")
    await ctx.send("!숙제 : 현재 해야 할 숙제를 알려드립니다.")
    await ctx.send("!(요일)시간표(ex. /월시간표) : 월요일 ~ 금요일까지의 시간표를 알려드립니다.")
    await ctx.send("!따라하기 (적을거) : 말을 따라합니다. /따라하기 뒤에 띄어쓰기를 해야 제대로 실행됩니다.")
    await ctx.send("!주사위 : 1부터 6까지 중 숫자 하나를 무작위로 뽑습니다.")
    await ctx.send("!유튭 : 이 봇 제작자의 유튜브 채널 주소를 알려드립니다.")
    await ctx.send("!코 : 중국산 코로나 관련 정보를 알려드립니다.")
    await ctx.send("!숨목록 : 숨겨진 명령어 목록을 알려드립니다.")
    await ctx.send("!역사 : 역사 시험범위 제외 부분을 알려드립니다.")
    if __name__ == "__main__":
    bot.run(TOKEN)
