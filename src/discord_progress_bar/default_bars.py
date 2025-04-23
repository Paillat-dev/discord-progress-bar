# Copyright (c) Paillat-dev
# SPDX-License-Identifier: MIT

from .types import ProgressBarPart, ProgressBarUrlMapping

DEFAULT_PROGRESS_BARS: dict[str, ProgressBarUrlMapping] = {
    "green": {
        # From https://emoji.gg/user/ravenastar
        ProgressBarPart.LEFT_EMPTY: "https://cdn3.emoji.gg/emojis/5499-lb2-g.png",
        ProgressBarPart.LEFT_FILLED: "https://cdn3.emoji.gg/emojis/5988-lb-g.png",
        ProgressBarPart.MIDDLE_EMPTY: "https://cdn3.emoji.gg/emojis/2827-l2-g.png",
        ProgressBarPart.MIDDLE_FILLED: "https://cdn3.emoji.gg/emojis/3451-l-g.png",
        ProgressBarPart.RIGHT_EMPTY: "https://cdn3.emoji.gg/emojis/2881-lb3-g.png",
        ProgressBarPart.RIGHT_FILLED: "https://cdn3.emoji.gg/emojis/3166-lb4-g.png",
    }
}
