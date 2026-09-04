# Origin Power AI（源力AI开放平台）

[English](../README.md)

Dify 模型供应商插件，接入**源力AI开放平台**——统一 OpenAI 兼容网关，一把 API Key 即可使用 GLM、MiniMax 等主流模型。

## 安装

- **插件市场**：上架后搜索 `origin-power-ai`。
- **GitHub**：Dify → 插件 → 通过 GitHub 安装 → `Ikki6666/origin-power-ai`；或在 [Releases](https://github.com/Ikki6666/origin-power-ai/releases) 下载 `.difypkg` 后从「本地文件」安装。
- **内部分发**：直接把 `.difypkg` 文件发给同事安装。

## 配置

1. 在[源力AI开放平台](https://origin-power-ai.mintlifysite.com/quickstart)创建 API Key（`agw_` 前缀）。
2. Dify → 设置 → 模型供应商 → **源力AI开放平台** → 授权。填写 **API Base URL**（网关根地址，含版本前缀，如 `https://your-gateway.example.com/v1`）和 API Key。
3. 下方预定义模型开箱即用；在「默认模型设置」中把其中之一设为系统推理模型，全工作空间成员即默认可用。

### 预定义模型

| Model ID | 上下文¹ | 最大输出 | 输入 / 输出（¥ / 百万 token）² | 视觉 | 工具调用 | 思考 |
|---|---|---|---|---|---|---|
| `glm-5.3-flash` | 1,048,576 | 131K | ¥0.40 / ¥1.40 | ✅（含视频输入） | ✅ | 不可关闭（low/high/max） |
| `glm-5-turbo` | 202,752 | 131K | ¥7.00 / ¥26.00 | – | ✅ | 可选 |
| `glm-4.7` | 202,752 | 131K | ¥4.00 / ¥16.00 | – | ✅ | 可选 |
| `glm-5.3` | 1,048,576 | 131K | ¥8.00 / ¥28.00 | – | ✅ | 不可关闭（low/high/max） |
| `glm-5.2` | 262,144 | 262K | ¥8.00 / ¥28.00 | – | ✅ | 可选（high/xhigh） |

¹ 取平台目录的 `top_provider.context_length`（实际部署上限），而非宣传训练上下文，避免超限报错。
² 截稿时点列价格；实际计费一律以网关响应中的 `usage` 为准。缓存命中的折扣价未体现在 Dify 的价格展示中。

五个模型均支持 `response_format`（JSON object 模式）；GLM-4.7 / 5.2 / 5.3 / Flash 额外支持 Dify 结构化输出工作流，推理模型提供 `reasoning_effort` 参数以在思考深度与 token 成本间取舍。

### 自定义模型

网关模型目录会持续更新，新增模型可手动接入：供应商卡片 → **添加模型** → 填写准确的 model ID（可用 `GET /v1/models` 查询）、Base URL 和 Key。

## 开发与调试

```bash
uv sync                       # 创建/刷新 .venv
uv run pytest tests           # 运行单元测试
```

远程调试（对任意自托管 Dify 实例，需 plugin daemon 开放 5003）：

1. Dify → 插件 → 调试插件，复制调试 Key 与地址。
2. 复制 `.env.example` 为 `.env`，填 `REMOTE_INSTALL_URL` / `REMOTE_INSTALL_KEY`。
3. `uv run python -m main`，插件实时注册进 Dify 实例。

打包：`dify plugin package ./origin-power-ai` 生成 `.difypkg`。

## 贡献与许可

代码基于 [dify-official-plugins](https://github.com/langgenius/dify-official-plugins) 的 `openai_api_compatible` 适配（Apache License 2.0），本插件沿用同一许可；模型目录与供应商逻辑在本仓库维护。
