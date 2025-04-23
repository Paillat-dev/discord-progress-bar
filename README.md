<div align="center">
  <h1>Discord Progress Bar</h1>

<!-- badges -->

![PyPI - Version](https://img.shields.io/pypi/v/discord-progress-bar)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/discord-progress-bar)
![PyPI - Types](https://img.shields.io/pypi/types/discord-progress-bar)
![PyPI - License](https://img.shields.io/pypi/l/discord-progress-bar)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/Paillat-dev/discord-progress-bar/CI.yaml)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/Paillat-dev/discord-progress-bar/main.svg)](https://results.pre-commit.ci/latest/github/Paillat-dev/discord-progress-bar/main)

<!-- end badges -->

A Python library for creating customizable progress bars with Discord emojis in your
Discord bot messages.

</div>

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Core Concepts](#core-concepts)
  - [How It Works](#how-it-works)
  - [Key Components](#key-components)
- [Features](#features)
  - [Type Safety](#type-safety)
- [Usage Examples](#usage-examples)
  - [Basic Progress Bar](#basic-progress-bar)
  - [Different Progress Bar States](#different-progress-bar-states)
  - [Custom Progress Bar Length](#custom-progress-bar-length)
- [Configuration](#configuration)
  - [Bot Configuration](#bot-configuration)
  - [Progress Bar Manager Initialization](#progress-bar-manager-initialization)
  - [Custom Progress Bar Styles](#custom-progress-bar-styles)
- [Limitations](#limitations)
- [Getting Help](#getting-help)
- [Development](#development)
  - [Local Testing](#local-testing)
  - [Contributing](#contributing)
- [License](#license)

## Overview

Discord Progress Bar is a Python library that allows you to create visually appealing
progress bars in your Discord bot messages using custom emojis. It provides a simple API
to generate progress bars of different styles and lengths, making it easy to display
progress, loading states, or completion percentages in your Discord applications.

Built on:

- [py-cord](https://github.com/Pycord-Development/pycord) - A modern, easy-to-use,
  feature-rich, and async-ready API wrapper for Discord
- Custom Discord emojis - Used to create visually consistent progress bar segments

## Installation

```bash
pip install discord-progress-bar --prerelease=allow
```

<!-- prettier-ignore -->
> [!NOTE]
> The package is currently in pre-release.

## Quick Start

<!-- quick-start -->
<!-- prettier-ignore -->
> [!TIP]
> Create beautiful progress bars in your Discord bot with just a few lines of code!

```python
import discord
from discord_progress_bar import ProgressBarManager

# Create a Discord bot with emoji caching enabled
bot = discord.Bot(cache_app_emojis=True)

@bot.event
async def on_ready():
    # Initialize the progress bar manager
    progress_bar_manager = await ProgressBarManager(bot)
    # Get a progress bar with the "green" style
    progress_bar = await progress_bar_manager.progress_bar("green")

    # Use it in your commands
    @bot.slash_command()
    async def show_progress(ctx, percent: float = 0.5):
        await ctx.respond(f"Progress: {progress_bar.partial(percent)}")

# Run your bot
bot.run("YOUR_TOKEN")
```

<!-- prettier-ignore -->
> [!NOTE]
> For a complete example, check the [examples directory](/examples).

## Core Concepts

### How It Works

Discord Progress Bar works by using custom Discord emojis to create visually appealing
progress bars in your bot messages. Here's how it works:

1. **Progress Bar Structure**: Each progress bar consists of multiple emoji segments:

- Left edge (filled or empty)
- Middle sections (filled or empty)
- Right edge (filled or empty)

2. **Emoji Management**: The `ProgressBarManager` class handles:

- Loading existing emojis from your bot
- Creating new emojis from URLs or files if needed
- Providing the appropriate emojis to the `ProgressBar` class

3. **Progress Bar Rendering**: The `ProgressBar` class handles:

- Rendering full progress bars (100%)
- Rendering empty progress bars (0%)
- Rendering partial progress bars (any percentage)

4. **Default Styles**: The library comes with a default "green" style, but you can
   create custom styles by providing your own emoji images.

### Key Components

- **ProgressBarManager**: Initializes with your Discord bot and manages emoji resources
- **ProgressBar**: Renders progress bars with different percentages
- **ProgressBarPart**: Enum defining the different parts of a progress bar (LEFT_EMPTY,
  LEFT_FILLED, etc.)
- **Default Bars**: Pre-configured progress bar styles that can be used out of the box

## Features

- **Easy Integration**: Seamlessly integrates with Discord bots built using py-cord
- **Customizable Progress Bars**: Create progress bars with different styles and lengths
- **Default Styles**: Comes with a pre-configured "green" style ready to use
- **Custom Styles**: Create your own progress bar styles using custom emoji images
- **Flexible Rendering**: Render progress bars at any percentage (0-100%)
- **Async Support**: Fully supports asynchronous operations for Discord bots
- **Emoji Management**: Automatically handles emoji creation and management

### Type Safety

Discord Progress Bar is fully type-annotated and type-safe. It uses `basedpyright` for
type checking.

<!-- prettier-ignore -->
> [!NOTE]
> While Discord Progress Bar itself is fully typed, the underlying py-cord library has limited type annotations, which may affect type checking in some areas.

## Usage Examples

### Basic Progress Bar

```python
@discord.slash_command()
async def show_progress(self, ctx: discord.ApplicationContext, percent: float = 0.5) -> None:
    """Display a progress bar with the specified percentage."""
    # Get a progress bar with the default "green" style
    progress_bar = await self.progress_bar_manager.progress_bar("green", length=10)
    # Render the progress bar at the specified percentage
    await ctx.respond(f"Progress: {progress_bar.partial(percent)}")
```

### Different Progress Bar States

```python
@discord.slash_command()
async def show_progress_states(self, ctx: discord.ApplicationContext) -> None:
    """Display different progress bar states."""
    progress_bar = await self.progress_bar_manager.progress_bar("green", length=10)

    # Empty progress bar (0%)
    empty = progress_bar.empty()

    # Partial progress bar (50%)
    half = progress_bar.partial(0.5)

    # Full progress bar (100%)
    full = progress_bar.full()

    await ctx.respond(f"Empty: {empty}\nHalf: {half}\nFull: {full}")
```

### Custom Progress Bar Length

```python
@discord.slash_command()
async def show_different_lengths(self, ctx: discord.ApplicationContext) -> None:
    """Display progress bars with different lengths."""
    # Short progress bar (5 segments)
    short_bar = await self.progress_bar_manager.progress_bar("green", length=5)

    # Medium progress bar (10 segments)
    medium_bar = await self.progress_bar_manager.progress_bar("green", length=10)

    # Long progress bar (20 segments)
    long_bar = await self.progress_bar_manager.progress_bar("green", length=20)

    await ctx.respond(
        f"Short (5): {short_bar.partial(0.7)}\n"
        f"Medium (10): {medium_bar.partial(0.7)}\n"
        f"Long (20): {long_bar.partial(0.7)}"
    )
```

For more examples, check the [examples directory](/examples) in the repository.

## Configuration

### Bot Configuration

When creating your Discord bot, make sure to enable emoji caching:

```python
bot = discord.Bot(cache_app_emojis=True)
```

This is required for the `ProgressBarManager` to properly load and manage emojis.

### Progress Bar Manager Initialization

Initialize the `ProgressBarManager` after your bot is ready:

```python
@discord.Cog.listener()
async def on_ready(self) -> None:
    self.progress_bar_manager = await ProgressBarManager(self.bot)
```

### Custom Progress Bar Styles

You can create custom progress bar styles by providing your own emoji images:

#### From URLs

```python
from discord_progress_bar import ProgressBarPart

# Define URLs for each part of the progress bar
custom_style = {
    ProgressBarPart.LEFT_EMPTY: "https://example.com/left_empty.png",
    ProgressBarPart.LEFT_FILLED: "https://example.com/left_filled.png",
    ProgressBarPart.MIDDLE_EMPTY: "https://example.com/middle_empty.png",
    ProgressBarPart.MIDDLE_FILLED: "https://example.com/middle_filled.png",
    ProgressBarPart.RIGHT_EMPTY: "https://example.com/right_empty.png",
    ProgressBarPart.RIGHT_FILLED: "https://example.com/right_filled.png",
}

# Create emojis from URLs
await self.progress_bar_manager.create_emojis_from_urls("custom_style", custom_style)
```

#### From Files

```python
import pathlib
from discord_progress_bar import ProgressBarPart

# Define file paths for each part of the progress bar
custom_style = {
    ProgressBarPart.LEFT_EMPTY: pathlib.Path("path/to/left_empty.png"),
    ProgressBarPart.LEFT_FILLED: pathlib.Path("path/to/left_filled.png"),
    ProgressBarPart.MIDDLE_EMPTY: pathlib.Path("path/to/middle_empty.png"),
    ProgressBarPart.MIDDLE_FILLED: pathlib.Path("path/to/middle_filled.png"),
    ProgressBarPart.RIGHT_EMPTY: pathlib.Path("path/to/right_empty.png"),
    ProgressBarPart.RIGHT_FILLED: pathlib.Path("path/to/right_filled.png"),
}

# Create emojis from files
await self.progress_bar_manager.create_emojis_from_files("custom_style", custom_style)
```

## Limitations

<!-- prettier-ignore -->
> [!WARNING]
> Please be aware of the following limitations:
>
> - **Python Version**: Requires Python 3.12 only
> - **Discord Bot Framework**: Currently only supports py-cord, not discord.py or other Discord API wrappers
> - **Emoji Creation**: Requires bot permissions to create and manage emojis in at least one server
> - **Emoji Limits**: Subject to Discord's emoji limits (50 custom emojis for regular servers, 200 for servers with Nitro boosts)
> - **Pre-release Status**: This package is currently in alpha stage and may have unexpected behaviors or breaking changes in future versions
> - **Custom Styles**: Creating custom styles requires providing all six emoji parts (LEFT_EMPTY, LEFT_FILLED, MIDDLE_EMPTY, MIDDLE_FILLED, RIGHT_EMPTY, RIGHT_FILLED)

## Getting Help

If you encounter issues or have questions about discord-progress-bar:

- **GitHub Issues**:
  [Submit a bug report or feature request](https://github.com/Paillat-dev/discord-progress-bar/issues)
- **Discord Support**:
  - For py-cord related questions: Join the
    [Pycord Official Server](https://discord.gg/pycord)
  - For discord-progress-bar specific help: Join the
    [Pycord Official Server](https://discord.gg/pycord) and mention `@paillat`

<!-- prettier-ignore -->
> [!TIP]
> Before asking for help, check if your question is already answered in the [examples directory](/examples) or existing GitHub issues.

## Development

### Local Testing

To set up a local development environment:

1. Clone the repository:

   ```bash
   git clone https://github.com/Paillat-dev/discord-progress-bar.git
   cd discord-progress-bar
   ```

2. Create a virtual environment and install dependencies:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   pip install -e ".[dev]"    # Install the package in development mode with dev dependencies
   ```

3. Create a `.env` file with your Discord bot token:

   ```
   DISCORD_TOKEN=your_discord_bot_token
   ```

4. Run the example bot:
   ```bash
   python examples/basic.py
   ```

### Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run linter, formatter and type checker: `ruff check .`,`ruff format .`,
   `basedpyright .`
5. Submit a pull request

**Development Tools**:

- **uv**: For dependency management
- **Ruff**: For linting and formatting
- **HashiCorp Copywrite**: For managing license headers
- **basedpyright**: For type checking

<!-- prettier-ignore -->
> [!CAUTION]
> This is an early-stage project and may have unexpected behaviors or bugs. Please report any issues you encounter.

## License

MIT License - Copyright (c) 2025 Paillat-dev

---

Made with ❤ by Paillat-dev
