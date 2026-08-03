# Agent Notes

This is a personal dotfiles repository, not a buildable project. All useful files are tracked dotfiles at the repo root and are meant to be symlinked into `$HOME` with GNU Stow.

## Stow workflow

- Apply dotfiles from the repo root to `$HOME`:  
  `stow .` (default target is the parent directory of the repo, i.e. `$HOME`).
- The repo contains a `.stow-local-ignore` that excludes README, LICENSE, `.git`, and a few other files from stowing.
- There is no install script, Makefile, or test suite.

## Shell start-up noise

`.zshenv` unconditionally sources `$HOME/.cargo/env`. If Rust/cargo is not installed, every new zsh prints:  
`/Users/lauri/.zshenv:.:1: no such file or directory: /Users/lauri/.cargo/env`  
This is non-fatal but expected when cargo is missing. Either install cargo or guard the line in `.zshenv` if you want it silent.

## External dependencies (not managed here)

`.zshrc` assumes these tools are installed independently:

- Oh My Zsh at `$HOME/.oh-my-zsh`
- `eza`, `bat`, `fzf`, `fd`, `thefuck`, `micro`
- `fzf-git.sh` at `$HOME/.local/fzf-git.sh/fzf-git.sh`

Nothing in this repo installs or checks them.

## Secrets and local paths

The following tracked files contain secrets or machine-specific paths:

- `.zshrc`: `export CONTEXT7_API_KEY="..."`
- `.config/opencode/opencode.json`: `CONTEXT7_API_KEY` header and a local MCP server path `/Users/lauri/.local/bin/codebase-memory-mcp`

Do not share the repository or commit diffs without stripping these values.

## Known stale / hand-managed files

- `.claude/settings.json` references Claude hooks at `~/.claude/hooks/cbm-*` that are not tracked in this repo.
- `.config/opencode/opencode.json` is tracked but tied to local MCP binaries and a remote API key.

## What not to expect

- No package manager, no build step, no formatter/linter config, no CI.
- No tests or verification command.
- No automated provisioning of macOS or external dependencies.
