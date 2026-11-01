# modern-software-codex-skills

面向 Codex 的六个软件开发 Skill，覆盖代码探索、现状研究、方案比较、实施规划、代码修改与审查。

[English](README.md) · [CS146S 课程](https://themodernsoftware.dev/) · [来源映射](SOURCE-MAP.md)

## Skills

| Skill | 用途 |
| --- | --- |
| `explore` | 梳理入口、依赖、文件结构和数据流。 |
| `research-codebase` | 基于文件路径和行号记录代码库现状。 |
| `make-proposals` | 根据代码研究文档比较实现方案。 |
| `plan` | 使用配套模板编写设计与实施计划。 |
| `implement` | 根据指定的 Markdown 计划文件实施修改。 |
| `review` | 审查暂存区和未暂存的代码改动，按优先级给出行动项。 |

## 安装

```bash
git clone https://github.com/GeoGeekLab/modern-software-codex-skills.git
cd modern-software-codex-skills
./scripts/install.sh all
```

按需安装：

```bash
./scripts/install.sh explore research-codebase plan implement review
```

默认安装位置：`${CODEX_HOME:-$HOME/.codex}/skills`。使用 `--force` 覆盖已有安装。

## 使用

在 Codex 中通过 `$skill-name` 调用：

```text
$explore 梳理认证模块的入口、依赖和数据流。
$research-codebase 记录当前会话过期机制，并标注文件与行号。
$make-proposals 基于 research/sessions.md 比较实现方案。
$plan 为会话过期功能编写实施计划。
$implement 执行 plans/session-expiration.md。
$review 审查暂存区和未暂存的代码改动。
```

每个 Skill 位于 `skills/<name>/SKILL.md`，配套资料与来源文本位于对应的 `references/` 目录。

## 开发命令

```bash
make validate   # 检查 Skill 文件、来源映射和测试用例格式
make list       # 列出全部 Skill
make dist       # 生成 ZIP 安装包
```

触发测试用例与运行记录模板见 [`evals/`](evals/README.md)。

## 参考资料

- [Stanford CS146S · The Modern Software Developer](https://themodernsoftware.dev/)
- [CS146S 课程作业](https://github.com/mihail911/modern-software-dev-assignments)
- [Skill 来源映射](SOURCE-MAP.md)
- [来源与许可说明](NOTICE.md)
