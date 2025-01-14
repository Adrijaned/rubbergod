import random

import discord
from discord.ext import commands

from logic import roll_dice
from config.app_config import Config
from config.messages import Messages
import utils

# Logic (functionality used by features or rubbergod directly)
roll_dice = roll_dice.Roll()


class Random(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.cooldown(rate=5, per=20.0, type=commands.BucketType.user)
    @commands.command(brief=Messages.random_diceroll_brief, description=Messages.rd_help)
    async def diceroll(self, ctx, *, arg=""):
        await ctx.send(roll_dice.roll_dice(arg))

    @commands.cooldown(rate=5, per=20.0, type=commands.BucketType.user)
    @commands.command(brief=Messages.random_pick_brief, usage=Messages.random_pick_usage)
    async def pick(self, ctx, *args):
        """"Pick an option"""
        for i, arg in enumerate(args):
            if "?" in arg:
                args = args[i + 1 :]
                break
        if not len(args):
            await ctx.send(utils.get_command_signature(ctx))
            return

        option = discord.utils.escape_mentions(random.choice(args))
        if option:
            await ctx.send(f"{option} {ctx.author.mention}")

    @commands.cooldown(rate=5, per=20.0, type=commands.BucketType.user)
    @commands.command(brief=Messages.random_flip_brief)
    async def flip(self, ctx):
        await ctx.send(random.choice(["True", "False"]))

    @commands.cooldown(rate=5, per=20.0, type=commands.BucketType.user)
    @commands.command(
        aliases=["random", "randint"],
        brief=Messages.random_roll_brief,
        description=Messages.rng_generator_format,
    )
    async def roll(self, ctx, first: int, second: int = 0):
        if first > second:
            first, second = second, first

        option = str(random.randint(first, second))
        await ctx.send(option)

    @diceroll.error
    @pick.error
    @roll.error
    @flip.error
    async def command_error(self, ctx, error):
        if isinstance(error, (commands.MissingRequiredArgument, commands.BadArgument)):
            await ctx.send(utils.get_command_signature(ctx))
        if isinstance(error, commands.CheckFailure):
            await ctx.message.channel.send(
                utils.fill_message("bot_room_redirect", user=ctx.message.author.id, bot_room=Config.bot_room)
            )

    async def cog_after_invoke(self, ctx):
        if ctx.channel.id not in Config.allowed_channels:
            await ctx.message.channel.send(
                utils.fill_message("bot_room_redirect", user=ctx.message.author.id, bot_room=Config.bot_room)
            )

    async def cog_check(self, ctx):
        if not Config.enable_room_check:
            return True
        return ctx.channel.id in Config.allowed_channels


def setup(bot):
    bot.add_cog(Random(bot))
