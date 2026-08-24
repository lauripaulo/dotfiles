# dotfiles

Personal configuration managed with [GNU Stow](https://www.gnu.org/software/stow/).
The repository is intended to be used as a Stow package, not built as an application.

## Apply

Run Stow from the repository root. Its default target is the repository's parent, so
`stow .` is only correct when the checkout is directly under `$HOME`:

```bash
stow .
```

For this checkout (`~/git/pessoal/dotfiles`), target the home directory explicitly:

```bash
stow --target="$HOME" .
```

Stow does not merge regular files. Back up any existing target before applying, or
remove only files already captured in a backup. `.stow-local-ignore` excludes README,
AGENTS, VCS metadata, and the Homebrew helper/list from installation.

## Managed Files

- `.zshrc` and `.zshenv` -- Zsh / Oh My Zsh configuration and environment loading
- `.gitconfig` -- Git identity, editor, hooks path, and whitespace settings
- `.claude/settings.json` -- Claude Code settings and hook references
- `.config/ghostty/config.ghostty` -- Ghostty terminal configuration
- `.config/opencode/opencode.json` -- OpenCode providers and MCP configuration

The OpenCode file is tracked, but it is intentionally not applied on `alduin`. To
apply this package on that machine without touching OpenCode, use:

```bash
stow --target="$HOME" --ignore='opencode' .
```

## Hosts

### alduin

`alduin` is Fedora Linux (`x86_64`) with `/home/lauri` as `$HOME`, `/usr/bin/zsh`
as the login shell, and `dnf` as the system package manager. The current setup has
Oh My Zsh, Rust, `eza`, `bat`, `fzf`, `fd`, `thefuck`, `micro`, `fresh`, `uv`, pnpm,
and `fzf-git.sh` installed.

The host-specific `.zshrc` configuration includes NVM, the local `uv` environment
loader, pnpm, and display defaults for the dummy-plug automation. It uses `micro` as
the local editor and `vim` over SSH.

Use the host-specific Stow command on `alduin` to leave OpenCode untouched:

```bash
stow --target="$HOME" --ignore='opencode' .
```

Bootstrap the command-line dependencies on `alduin` with Fedora's package manager:

```bash
sudo dnf install tealdeer thefuck eza bat fd-find fzf stow
```

Install the user-owned tools used by this setup:

```bash
curl https://raw.githubusercontent.com/sinelaw/fresh/refs/heads/master/scripts/install.sh | sh
curl -LsSf https://astral.sh/uv/install.sh | sh
git clone git@github.com:junegunn/fzf-git.sh.git "$HOME/.local/fzf-git.sh"
```

The first two commands install under `$HOME/.local`; run the clone command only when
`$HOME/.local/fzf-git.sh` does not already exist. Do not use the Debian `apt` command
on this host.

### diaspar.lan

`diaspar.lan` is the Debian homelab server. Its base packages are installed with
APT; the shell dependencies used by this repository can be installed with:

```bash
sudo apt install tealdeer thefuck eza bat fd-find fzf
```

### MiniMac

`MiniMac` is the macOS work machine. Homebrew package provisioning uses the helper
described below and the package list tracked in `brews-installed-list.txt`.

## Dependencies

`.zshrc` expects these external paths and commands; this repository does not install
or update them:

- `$HOME/.oh-my-zsh`
- `eza`, `bat`, `fzf`, `fd`, `thefuck`, and `micro`
- `$HOME/.local/fzf-git.sh/fzf-git.sh`
- `$HOME/.cargo/env` (loaded unconditionally by `.zshenv`)

If Rust is absent, starting Zsh prints a non-fatal warning because `.zshenv` cannot
source `$HOME/.cargo/env`.

## Homebrew Helper

`install-brew-apps.py` is an optional Homebrew-only helper for `MiniMac` and other
Homebrew machines. Run it from the repository root:

```bash
./install-brew-apps.py
```

It reads `brews-installed-list.txt`, skips blank/comment lines, continues after
failed packages, and currently exits successfully even when it reports failures. To
refresh the list on a Homebrew machine:

```bash
brew list --full-name -1 > brews-installed-list.txt
```

## Sensitive Configuration

`.zshrc` and `.config/opencode/opencode.json` contain API keys and machine-specific
paths, including a local MCP binary path. Do not expose their values or make those
paths portable unless that is intentional. `.claude/settings.json` references
untracked hooks under `~/.claude/hooks/cbm-*`.
