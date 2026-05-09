# apt-terminal

Python CLI for [`agenticregistry`](https://github.com/agentic-cookbook/agenticregistry)
(persona definitions + LLM provider integrations) and
[`my-agentic-storage`](https://github.com/agentic-cookbook/my-agentic-storage)
(buckets, lists, kv, counters, events, queues, memory, keywords).

Two subcommand groups, both authenticated with per-user API keys:

- `apt storage …` — administer your storage account: buckets and the
  primitives inside them.
- `apt registry …` — administer your registry account: personas, LLM
  service connections, public search.

Out of scope today: chat / try-out (`apt try <slug>`). That waits on the
M1 architectural decision; neither service exposes a chat-completion
endpoint yet.

## Install (editable)

```bash
cd terminal
python3.11 -m venv .venv
. .venv/bin/activate
pip install -e ".[dev]"
```

This puts `apt` on your `$PATH`.

## First-time setup

```bash
apt storage login         # paste an API key from your storage account
apt registry login        # paste an API key from your registry account
apt storage whoami        # confirm
apt registry whoami       # confirm
```

Config is stored at `~/.config/apt/config.toml` (mode 0600). Override path
with `$APT_CONFIG`.

Env vars override the config when present:

```
APT_STORAGE_URL   APT_STORAGE_KEY
APT_REGISTRY_URL  APT_REGISTRY_KEY
```

## Smoke run — storage

```bash
apt storage bucket create scratch
apt storage bucket use scratch
apt storage kv set hello '"world"'
apt storage kv get hello
apt storage list new tasks
apt storage list append tasks '"draft the spec"'
apt storage list show tasks
apt storage bucket delete scratch -y
```

## Smoke run — registry

```bash
apt registry service templates
apt registry service add --template <id> --name claude --api-key-stdin
apt registry persona create --slug bob --name Bob --prompt "You are Bob."
apt registry persona show bob
apt registry persona edit bob          # opens $EDITOR with TOML
apt registry persona delete bob -y
```

## Layout

```
terminal/
  pyproject.toml
  src/apt_terminal/
    cli.py, config.py, http.py, output.py, errors.py
    storage/   client.py, commands.py, schemas.py
    registry/  client.py, commands.py, schemas.py
  tests/
```

## Develop

```bash
ruff check src tests
ruff format src tests
mypy
pytest
```
