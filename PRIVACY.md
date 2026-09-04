# Privacy Policy / 隐私政策

- English

This plugin is a model provider for Dify. It forwards prompts, conversation
history, files, and tool definitions **only to the API endpoint that the Dify
administrator configures when connecting this provider** (the Origin Power AI
gateway or any other OpenAI-compatible gateway of their choice).

- The plugin itself does **not** collect, store, or transmit any data to the
  plugin author or to any third-party service beyond the configured endpoint.
- API keys are stored by the Dify workspace that installed the plugin and are
  never sent anywhere except to the configured endpoint as `Authorization: Bearer` credentials.
- Querying billing, quotas, or logs is the responsibility of the endpoint
  operator; see the platform's own privacy policy for details.

- 中文

本插件是 Dify 的模型供应商插件。插件会把提示词、对话上下文、文件与工具定义
**仅转发给 Dify 管理员在配置该供应商时填写的 API 地址**（源力AI开放平台网关，
或管理员选择的其他 OpenAI 兼容网关）。

- 插件自身**不会**向插件作者或配置地址以外的任何第三方收集、存储或传输数据。
- API Key 由安装插件的 Dify 工作空间保管，除作为凭据发送给所配置端点外不会被发送到任何地方。
- 用量、配额与日志的查询由端点运营方负责，请参阅相应平台的隐私政策。
