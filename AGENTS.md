# Agent Notes

This is a personal dotfiles repository managed with GNU Stow, not a buildable application. Tracked dotfiles live at the repository root and are intended to be linked into `$HOME`.

## Workflow

- From the repository root, apply the package with `stow .`. Stow targets the repository's parent by default, so the checkout should be directly under `$HOME` for this command to target `$HOME`.
- This checkout is under `~/git/pessoal/dotfiles`; apply it to the home directory with `stow --target="$HOME" .` instead of relying on the default target.
- On host `alduin`, do not apply the tracked OpenCode config unless explicitly requested; use `stow --target="$HOME" --ignore='opencode' .` for the normal workflow.
- Host-specific workflows for `alduin`, `diaspar.lan` (Debian homelab), and `MiniMac` (macOS work machine) are documented in `README.md`; do not apply the `alduin` OpenCode exclusion to the other hosts without a reason.
- `.stow-local-ignore` deliberately excludes `README*`, `AGENTS*`, VCS metadata, and the Homebrew helper/list from installation.
- There is no build, test, lint, formatter, package-manager, or CI workflow. Do not invent a project verification command.
- `./install-brew-apps.py` is an optional Homebrew-only helper. It reads `brews-installed-list.txt`, continues after individual failures, and currently exits successfully after reporting failures.

## Runtime Dependencies

- `.zshrc` requires Oh My Zsh at `$HOME/.oh-my-zsh`, plus `eza`, `bat`, `fzf`, `fd`, `thefuck`, `micro`, and `$HOME/.local/fzf-git.sh/fzf-git.sh`.
- `.zshenv` unconditionally sources `$HOME/.cargo/env`; without Rust/cargo, every new zsh emits a non-fatal missing-file warning.
- `.claude/settings.json` references untracked hooks under `~/.claude/hooks/cbm-*`.
- `alduin` is Fedora Linux with `/home/lauri` as `$HOME`, `/usr/bin/zsh` as the shell, and `dnf` as the system package manager.
- On `alduin`, `.zshrc` also loads NVM, `$HOME/.local/bin/env`, pnpm, and machine-specific dummy-plug display defaults; preserve these when merging `.zshrc`.
- On `alduin`, install the base tools with `sudo dnf install tealdeer thefuck eza bat fd-find fzf stow`; do not use the Debian `apt` command.
- On `alduin`, `fresh` and `uv` are user-owned installs under `$HOME/.local`, and `fzf-git.sh` lives at `$HOME/.local/fzf-git.sh`.

## Sensitive Configuration

- `.zshrc` and `.config/opencode/opencode.json` contain API keys and machine-specific configuration, including a local MCP binary path. Do not expose or broadly share their values; preserve local paths unless intentionally making the configuration portable.
