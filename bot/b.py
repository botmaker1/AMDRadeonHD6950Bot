import os
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user.name}({bot.user.id})")

@bot.command()
async def 숨목록(ctx):
    await ctx.send("숨겨진 명령어 목록입니다. 여기 명령어들은 대부분 !가 필요 없습니다.(있는 것은 ! 쳐져있음)")
    await ctx.send("fuck(또는 Fuck) : Lily Allen의 Fuck You 음악 뮤비 유튜브 주소를 보여드립니다.")
    await ctx.send("!섹온비 : 섹온비 유튜브 주소를 띄웁니다.")
    await ctx.send("!ijhs : Lonely Island의 I Just Had Sex 유튜브 뮤비 주소를 띄웁니다.")
    await ctx.send("숨숨목록 : 궁금하면 해보세요")
    if __name__ == "__main__":
    bot.run(TOKEN)

@.command()
async def 따라하기(ctx, *, text):
    await ctx.send(text)
    
if __name__ == "__main__":
    bot.run(TOKEN)
