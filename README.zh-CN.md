# modern-software-codex-skills

本仓库仅保留六个 **以已有来源快照为依据** 的 Codex Skill 适配版本。

**本仓库不是斯坦福官方项目，也不是 CS146S 官方 Skill 合集。** 2026 年第三周的[官方作业](https://github.com/mihail911/modern-software-dev-assignments/blob/master/week3/assignment.md)要求学生自行挑选一个重复性工作流程、手动执行、编写 Skill 并测试触发与真实执行，并未规定六个必须安装的 Skill。

这六份原始 `SKILL.md` 快照来自此仓库此前收录、标注为 2026-10-01 课程链接资料的文件。**本次核查无法独立打开其原始 Drive 文件夹，不能据此断言这些样例是课程官方原创。** 参见 [SOURCE-MAP.md](SOURCE-MAP.md)。

## 保留的六个样例

| Skill | 原始职责 |
| --- | --- |
| `explore` | 阅读代码，解释入口、调用关系、文件布局和数据流；除非要求，否则不运行代码 |
| `research-codebase` | 仅记录现状，提供文件和行号，不提改进方案 |
| `make-proposals` | 基于已有研究文档比较解决方案 |
| `plan` | 使用原始设计文档模板撰写计划，不实施 |
| `implement` | 执行指定的计划 Markdown 文件 |
| `review` | 审查暂存区和未暂存的改动，按原样例的红／黄／绿等级输出 |

这六项**不是课程规定的强制顺序**。此前添加的工作流路由器及由系统提示词、压缩提示词等衍生的 Skill 已移除。

## 安装

```bash
make validate
./scripts/install.sh all
```

指定安装：

```bash
./scripts/install.sh explore research-codebase review
```

默认位置是 `${CODEX_HOME:-$HOME/.codex}/skills`。不会默认覆盖已有 Skill；需要覆盖时使用 `--force`。

## 与原文的差异

- 移除 Claude 专属的 `disable-model-invocation` 元数据。这意味着 Codex 的自动触发语义可能与原样例不同。
- 将原样例 `/skill-name` 调用写法换成 Codex `$skill-name`。
- 将 `implement` 中的占位路径换成当前提供的计划文件。
- `make-proposals` 原文同时出现“至多两个”和“两或三个”，适配版采用“至多两个”，并记录这一取舍。
- 将原始 `design_doc_template.md` 放到 `plan` 目录下。
- `research-codebase` 的原文 `context7` 依赖保持不变；本仓库不会自动安装它。

`make validate` 仅检查**静态格式、原文对应关系和测试用例文件**，不等于已验证模型触发或端到端执行。

官方第三周要求每个 Skill 测试三个应触发提示、一个不应触发提示，并完成真实运行。仓库提供[待执行用例](evals/cases.jsonl)和[记录模板](evals/RUN-REPORT-TEMPLATE.md)，**没有伪造测试成绩**。

课程来源：[官网](https://themodernsoftware.dev/) · [官方作业仓库](https://github.com/mihail911/modern-software-dev-assignments) · [第三周作业](https://github.com/mihail911/modern-software-dev-assignments/blob/master/week3/assignment.md)。

来源可信度、适配细节和授权边界分别见 [SOURCE-MAP.md](SOURCE-MAP.md)、[docs/SCOPE.md](docs/SCOPE.md)、[NOTICE.md](NOTICE.md)。
