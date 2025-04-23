# ruff: noqa: A005
# Copyright (c) Paillat-dev
# SPDX-License-Identifier: MIT

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import pathlib
from enum import IntEnum

import discord


class ProgressBarPart(IntEnum):
    """Enum for the different parts of a progress bar."""

    LEFT_EMPTY = 0
    LEFT_FILLED = 1
    MIDDLE_EMPTY = 2
    MIDDLE_FILLED = 3
    RIGHT_EMPTY = 4
    RIGHT_FILLED = 5


type ProgressBarUrlMapping = dict[ProgressBarPart, str]
type ProgressBarPathMapping = dict[ProgressBarPart, pathlib.Path]
type ProgressBarEmojiMapping = dict[ProgressBarPart, discord.AppEmoji]
