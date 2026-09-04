# Origin Power AI

[中文说明](readme/README_zh_Hans.md)

A [Dify](https://dify.ai) model provider plugin for the **Origin Power AI** platform — a unified OpenAI-compatible gateway that aggregates GLM, MiniMax and other mainstream models behind a single API key.

## Install

**Marketplace**: search `origin-power-ai` (after the plugin is listed).

**GitHub**: Dify → Plugins → Install via GitHub → `Ikki6666/origin-power-ai`, or download the `.difypkg` from [Releases](https://github.com/Ikki6666/origin-power-ai/releases) and install via *Local Package File*.

**Local file** (for internal distribution): hand the `.difypkg` to your users and install it from the Plugins page.

## Configure

1. Get an API key (prefix `agw_`) from the [Origin Power AI console](https://origin-power-ai.mintlifysite.com/quickstart).
2. Dify → Settings → Model Provider → **Origin Power AI** → Setup. Fill in your **API Base URL** — the root of the gateway including the version prefix, e.g. `https://your-gateway.example.com/v1` — and your API Key.
3. The models below are predefined; pick one as the system default model to make it available to every workspace member.

### Predefined models

| Model ID | Context | Max output | Input / Output (CNY per 1M tokens)¹ | Vision | Tool call |
|---|---|---|---|---|---|
| `glm-5.3-flash` | 1.25M | 131K | ¥0.40 / ¥1.40 | ✅ | ✅ |
| `glm-5-turbo` | 200K | 131K | ¥7.00 / ¥26.00 | – | ✅ |
| `glm-4.7` | 200K | 131K | ¥4.00 / ¥16.00 | – | ✅ |
| `glm-5.3` | 1M | 131K | ¥8.00 / ¥28.00 | – | ✅ |
| `glm-5.2` | 1M | 262K | ¥8.00 / ¥28.00 | – | ✅ |
| `minimax-h3` | approx. 131K² | 131K | see platform pricing | ✅ | – |

¹ List prices at the time of writing; billing always follows the `usage` field returned by the gateway. Cached-input discounts are not reflected in Dify's price display.
² Specs for `minimax-h3` are approximate; add it with precise parameters via **Add Model** (customizable model) if your plan differs.

### Custom models

The gateway catalog grows over time. Any new model can be added by hand: on the provider card click **Add Model**, enter the exact model ID (use `GET /v1/models` to list), the Base URL, and the key.

## Development

```bash
uv sync                       # create/refresh .venv
uv run pytest tests           # run unit tests
```

Remote debugging against a running Dify instance (works for self-hosted Dify ≥ 1.x with the plugin daemon exposed):

1. In Dify → Plugins → Debug Plugin, copy the key/host.
2. Copy `.env.example` to `.env`, set `REMOTE_INSTALL_URL` / `REMOTE_INSTALL_KEY`.
3. `uv run python -m main` — the plugin registers with your Dify instance live.

Package: `dify plugin package ./origin-power-ai` produces the `.difypkg`.

## Contributions & License

Code adapted from [dify-official-plugins](https://github.com/langgenius/dify-official-plugins) (`openai_api_compatible`), Apache License 2.0. This plugin keeps the same license; model YAMLs and provider logic are maintained in this repository.
