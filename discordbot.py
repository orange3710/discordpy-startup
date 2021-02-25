from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

# 処理

@bot.event
async def on_message(message):
    # 処理
    await bot.process_commands(message)
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, reason=None):
    kicknoti = discord.Embed(title='メンバーをキックしました', description='Kickしたメンバーにまた来てもらうには再招待してください', color=discord.Color.red())
    kicknoti.add_field(name='執行人', value=f'{ctx.author.mention}')
    kicknoti.add_field(name='Kickされた人', value=f'{member.mention}')
    kicknoti.set_thumbnail(url=member.avatar_url)
    await ctx.send(embed=kicknoti)
    await member.kick(reason=reason)

@bot.event
async def on_ready():
    print('Logged in as {0} ({0.id})'.format(bot.user))
    print('------')
