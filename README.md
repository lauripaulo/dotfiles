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
- `.gitconfig` — Git configuration (user identity, push, core settings, hooks path)
- `.claude/settings.json` — Claude Code settings
- `.config/ghostty/config.ghostty` — Ghostty terminal emulator configuration
- `.config/opencode/opencode.json` — OpenCode configuration

## Helper scripts

These files are kept in the repo but excluded from stowing:

- `install-brew-apps.py` — reads `brews-installed-list.txt` and runs `brew install` for each package.
- `brews-installed-list.txt` — list of Homebrew packages to install on a fresh machine.

### Installing Homebrew packages

Run the helper script from the repo root:

```bash
./install-brew-apps.py
```

To export the list run:
```bash
brew list --full-name -1 > brews-installed-list.txt
```

The script skips empty lines and comments, then runs `brew install <package>` for each entry in `brews-installed-list.txt`. Homebrew resolves and installs dependencies automatically. If a single package fails, the script continues with the rest and reports the failure at the end.

## Prerequisites

`.zshrc` expects these tools to be installed independently:

- [Oh My Zsh](https://ohmyz.sh/) at `$HOME/.oh-my-zsh`
- [eza](https://eza.rocks/), [bat](https://github.com/sharkdp/bat), [fzf](https://github.com/junegunn/fzf), [fd](https://github.com/sharkdp/fd), [thefuck](https://github.com/nvbn/thefuck), [micro](https://micro-editor.github.io/)
- [fzf-git.sh](https://github.com/junegunn/fzf-git.sh) at `$HOME/.local/fzf-git.sh/fzf-git.sh`

This repo does not install or update them.

### Linux install (Debian)

```
sudo apt install tealdeer thefuck eza bat fd-find fzf
```

- Fresh editor install
```
curl https://raw.githubusercontent.com/sinelaw/fresh/refs/heads/master/scripts/install.sh | sh
```

- Python uv install
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

- Install fzf-git.sh
```
cd /home/lauri/.local/
git clone 
```
## Notes

- `.zshenv` sources `$HOME/.cargo/env`. If Rust/cargo is not installed, zsh will print a non-fatal warning on every shell start.
- `.zshrc` and `.config/opencode/opencode.json` contain API keys and local paths. Do not share the repo without stripping those values first.
- `.claude/settings.json` references Claude hooks at `~/.claude/hooks/cbm-*` that are not tracked in this repo.

## Future Stow candidates

These files in `$HOME` are good candidates to pull into this repo next:

- `~/.config/git/` — includes the `ignore` file and `post-commit`/`post-checkout` hooks.
  The hooks invoke `tokensave`, so that tool must be installed on the machine.
- `~/.zprofile`
- `~/.config/btop/`
- `~/.config/topgrade.toml` + `~/.config/topgrade.d/`
- `~/.config/micro/` — only the `bindings.json` file; exclude runtime dirs
  `backups/` and `buffers/`.

Use with care:

- `~/.config/zed/settings.json` — good config, but the surrounding `prompts/` and
  `themes/` directories may be machine-generated or personal.
- `~/.config/iterm2/` — mostly runtime symlinks and sockets; only useful if you
  add minimal plist files.

Avoid stowing:

- Secrets or state: `~/.ssh/`, `~/.tokensave/`, `~/.cache/`, `~/.zsh_history`,
  `~/.zcompdump*`, `~/.local/`, `~/.claude/` (runtime), `~/.oh-my-zsh/`.

If these are added, the recommended layout is modular packages (e.g. `zsh/`, `git/`,
`btop/`, `micro/`, `topgrade/`, `zed/`) so you can apply them per machine:

```bash
stow -d . -t ~ zsh git btop micro topgrade zed claude opencode ghostty
```
