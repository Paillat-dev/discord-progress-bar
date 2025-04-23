# Copyright (c) Paillat-dev
# SPDX-License-Identifier: MIT

from collections import defaultdict
from typing import Self, cast

import aiofile
import aiohttp
import discord

from .default_bars import DEFAULT_PROGRESS_BARS
from .types import ProgressBarEmojiMapping, ProgressBarPart, ProgressBarPathMapping, ProgressBarUrlMapping


class ProgressBar:
    def __init__(self, mapping: ProgressBarEmojiMapping, length: int = 5) -> None:
        if length < 2:
            raise ValueError("Length must be at least 2.")
        self._mapping: ProgressBarEmojiMapping = mapping
        self._length: int = length

    def full(self) -> str:
        return "".join(
            [
                str(self._mapping[ProgressBarPart.LEFT_FILLED])
                + str(self._mapping[ProgressBarPart.MIDDLE_FILLED]) * (self._length - 2)
                + str(self._mapping[ProgressBarPart.RIGHT_FILLED])
            ]
        )

    def empty(self) -> str:
        return "".join(
            [
                str(self._mapping[ProgressBarPart.LEFT_EMPTY])
                + str(self._mapping[ProgressBarPart.MIDDLE_EMPTY]) * (self._length - 2)
                + str(self._mapping[ProgressBarPart.RIGHT_EMPTY])
            ]
        )

    def partial(self, percent: float) -> str:
        if percent < 0 or percent > 1:
            raise ValueError("Percent must be between 0 and 1.")
        filled_length = round(self._length * percent)
        empty_length = self._length - filled_length

        # Handle edge cases
        if filled_length == 0:
            return self.empty()
        if filled_length == self._length:
            return self.full()

        # For partial progress, ensure we have the correct number of middle emojis
        middle_filled_count = max(0, filled_length - 1)  # At least one for left filled
        middle_empty_count = max(0, empty_length - 1)  # At least one for right empty

        return "".join(
            [
                str(self._mapping[ProgressBarPart.LEFT_FILLED])
                + str(self._mapping[ProgressBarPart.MIDDLE_FILLED]) * middle_filled_count
                + str(self._mapping[ProgressBarPart.MIDDLE_EMPTY]) * middle_empty_count
                + str(self._mapping[ProgressBarPart.RIGHT_EMPTY])
            ]
        )


class ProgressBarManager:
    def __init__(self, bot: discord.Bot) -> None:
        self._bot: discord.Bot = bot
        self._emojis: dict[str, ProgressBarEmojiMapping] = defaultdict(dict)

    async def __new__(cls, bot: discord.Bot) -> Self:
        obj = super().__new__(cls)
        obj.__init__(bot)
        await obj.load()
        return obj

    async def load(self) -> None:
        await self._bot.wait_until_ready()
        for emoji in self._bot.app_emojis:
            if emoji.name.startswith("pb_"):
                key: str = emoji.name.split("_")[1]
                part: ProgressBarPart = cast("ProgressBarPart", int(emoji.name.split("_")[2]))
                self._emojis[key][part] = emoji

    async def create_emojis_from_urls(self, name: str, emojis: ProgressBarUrlMapping) -> None:
        async with aiohttp.ClientSession() as session:
            for key, url in emojis.items():
                emoji_name = f"pb_{name}_{key}"
                response = await session.get(url)
                response.raise_for_status()
                image = await response.read()
                emoji = await self._bot.create_emoji(
                    name=emoji_name,
                    image=image,
                )
                self._emojis[name][key] = emoji

    async def create_emojis_from_files(self, name: str, emojis: ProgressBarPathMapping) -> None:
        for key, path in emojis.items():
            emoji_name = f"pb_{name}_{key}"
            async with aiofile.async_open(path, "rb") as f:
                image = await f.read()
            emoji = await self._bot.create_emoji(
                name=emoji_name,
                image=image,
            )
            self._emojis[name][key] = emoji

    async def progress_bar(self, name: str, *, length: int = 5) -> ProgressBar:
        if name not in self._emojis:
            if default := DEFAULT_PROGRESS_BARS.get(name):
                await self.create_emojis_from_urls(name, default)
            else:
                raise ValueError(f"Progress bar {name} not found.")
        return ProgressBar(self._emojis[name], length=length)
