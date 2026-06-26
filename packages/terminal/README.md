# apt

CLI for the Agentic Developer backend (`api.agenticdeveloperhub.com`),
built on a generated `openapi-python-client` client.

## Auth
    apt auth login            # email/password → JWT (stored per profile)
    apt auth whoami
    apt auth tokens list | create --set name=ci | delete <id>
    apt auth logout

## Resources (uniform CRUD)
    apt <domain> <resource> <verb> [id] [--set FIELD=VALUE …] [--json]

    verbs: list (ls) · get <id> · create · update <id> · delete (rm)

    apt persona services list
    apt persona services create --set name=openai --set provider_kind=openai --set base_url=https://api.openai.com
    apt persona services connect <id>            # named action
    apt persona personas list
    apt public persona <slug>                    # no auth

Config: `~/.config/apt/config.toml` — one `base_url` + JWT tokens per profile.
Override with `APT_BASE_URL`, `APT_TOKEN`, `APT_CONFIG`, `--profile`.

## Install (editable)

```bash
cd terminal
python3.11 -m venv .venv
. .venv/bin/activate
pip install -e ".[dev]"
```

This puts `apt` on your `$PATH`.

## Develop

```bash
ruff check src tests
ruff format src tests
mypy src/apt_terminal
pytest
```
