# Copyright (c) Paillat-dev
# SPDX-License-Identifier: MIT

import os

import discord
from dotenv import load_dotenv

from discord_progress_bar import ProgressBar, ProgressBarManager

# Load environment variables from .env file
load_dotenv()

bot = discord.Bot(cache_app_emojis=True)


class MyCog(discord.Cog):
    def __init__(self, bot: discord.Bot) -> None:
        self.bot: discord.Bot = bot
        self.progress_bar_manager: ProgressBarManager = ProgressBarManager(self.bot)
        self.progress_bar: ProgressBar | None = None

    @discord.Cog.listener()
    async def on_ready(self) -> None:
        print(f"Logged in as {bot.user} (ID: {bot.user.id})")  # pyright: ignore [reportOptionalMemberAccess]
        print("------")
        await self.progress_bar_manager.load()
        self.progress_bar = await self.progress_bar_manager.progress_bar("green", length=10)
        print("Progress bar manager loaded.")

    @discord.slash_command()  # pyright: ignore [reportUntypedFunctionDecorator]
    async def get_progress_bar(self, ctx: discord.ApplicationContext, percent: float | None = None) -> None:
        """Send a progress bar message."""
        if not self.progress_bar:
            await ctx.respond("Progress bar manager is not loaded yet.")
            return

        if percent is None or percent > 1:
            percent = 1

        await ctx.respond(f"Progress: {self.progress_bar.partial(percent)}")


bot.add_cog(MyCog(bot))
bot.run(os.environ["DISCORD_TOKEN"])
