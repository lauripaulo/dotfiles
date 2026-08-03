# dotfiles

Personal dotfiles managed with [GNU Stow](https://www.gnu.org/software/stow/).

## Apply

From the repo root:

```bash
stow .
```

This symlinks the tracked files into `$HOME`. The parent directory of the repo is used as the default target, so the repo should live directly under `$HOME` (e.g. `~/dotfiles`).

`.stow-local-ignore` keeps README, LICENSE, `.git`, and a few other files from being stowed.

## What's included

- `.zshrc` — Zsh / Oh My Zsh configuration
- `.zshenv` — Zsh environment loader
- `.claude/settings.json` — Claude Code settings
- `.config/opencode/opencode.json` — OpenCode configuration

## Prerequisites

`.zshrc` expects these tools to be installed independently:

- [Oh My Zsh](https://ohmyz.sh/) at `$HOME/.oh-my-zsh`
- [eza](https://eza.rocks/), [bat](https://github.com/sharkdp/bat), [fzf](https://github.com/junegunn/fzf), [fd](https://github.com/sharkdp/fd), [thefuck](https://github.com/nvbn/thefuck), [micro](https://micro-editor.github.io/)
- [fzf-git.sh](https://github.com/junegunn/fzf-git.sh) at `$HOME/.local/fzf-git.sh/fzf-git.sh`

This repo does not install or update them.

## Notes

- `.zshenv` sources `$HOME/.cargo/env`. If Rust/cargo is not installed, zsh will print a non-fatal warning on every shell start.
- `.zshrc` and `.config/opencode/opencode.json` contain API keys and local paths. Do not share the repo without stripping those values first.
- `.claude/settings.json` references Claude hooks at `~/.claude/hooks/cbm-*` that are not tracked in this repo.
