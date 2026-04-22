# agent-dev

> 🤖 AI Agent 开发最佳实践 Skill — 让 AI 帮你写出更正确、更高质量的 Agent 代码

## 这是什么？

`agent-dev` 是一个面向 AI 编码助手的 **Skill 文件**，当开发者使用 AI（如 Copilot、Claude、Cursor 等）编写 AI Agent 代码时，此 Skill 会自动引导 AI 遵循业界最佳实践，确保生成的代码在架构设计、安全性、可维护性和生产就绪度上达到高标准。

## 覆盖的知识领域

基于微软 [AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners) 全部 15 课及业界实践总结：

| 领域 | 核心内容 |
|------|---------|
| **架构选型** | 决策树：何时用单 Agent / 多 Agent / RAG / CUA |
| **System Prompt 工程** | 四步法框架 + 反模式识别 |
| **Tool Use / Function Calling** | 工具 Schema 规范 + 设计清单 + 实现模式 |
| **Agentic RAG** | Maker-Checker 迭代循环 + 自纠正 + 反模式 |
| **多智能体系统** | 编排模式选择 + 实现清单 + 代码模式 |
| **规划模式** | 任务分解 + 结构化输出 + 迭代规划 |
| **可信 Agent** | 威胁模型 + Human-in-the-Loop + 安全编码清单 |
| **上下文工程** | 上下文类型 + 管理策略 + 四种故障模式 |
| **Agent 记忆** | 六种记忆类型 + 自改进模式 |
| **生产部署** | 可观测性（OTel）+ 监控指标 + 成本管理 + 评估体系 |
| **Agentic 协议** | MCP / A2A / NLWeb 选择指南 |
| **元认知** | 自反思模式 + 决策理由记录 |
| **浏览器自动化** | Agent vs Actor 选择 + 最佳实践 |

## 如何使用

### 方式一：手动安装

将 `SKILL.md` 文件放到你的 AI 编码助手的 skills 目录中：

```bash
# Aone Copilot
cp SKILL.md ~/.aone_copilot/skills/aigents/SKILL.md

# Claude Code
cp SKILL.md ~/.claude/skills/aigents/SKILL.md

# 通用 .agents 目录
mkdir -p ~/.agents/skills/aigents
cp SKILL.md ~/.agents/skills/aigents/SKILL.md
```

### 方式二：直接引用

在你的项目根目录创建 `.agents/skills/aigents/` 目录，将 `SKILL.md` 放入即可。

## 适用场景

当你向 AI 编码助手提出以下类型的请求时，此 Skill 会自动生效：

- "帮我设计一个客服 Agent"
- "实现一个带 RAG 的问答系统"
- "写一个多 Agent 协作的旅行规划系统"
- "给这个 Agent 添加 Function Calling"
- "帮我优化这个 Agent 的 System Prompt"
- "如何让 Agent 记住用户偏好"
- "部署 Agent 到生产环境需要注意什么"

## 贡献

欢迎提交 Issue 和 PR 来完善这份最佳实践指南。

## License

MIT
