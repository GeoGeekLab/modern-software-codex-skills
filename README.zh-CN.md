# modern-software-codex-skills

`CS146S -> Codex`

这是对 [CS146S: The Modern Software Developer](https://themodernsoftware.dev/) 公开 prompt / skill 材料的 Codex 整理版。

目标很简单：保留有效的软件工程工作流，移除运行时耦合，并整理成可安装、可验证、可维护的 Codex skills。

```text
需求
 |
 v
Explore     快速建立代码地图
 |
 v
Research    固定当前事实
 |
 v
Proposals   比较实现路径
 |
 v
Plan        形成可执行设计
 |
 v
Implement   按计划修改
 |
 v
Review      检查实际 diff
```

## 使用

验证：

```bash
make validate
```

安装全部 skills：

```bash
./scripts/install.sh all
```

安装部分 skills：

```bash
./scripts/install.sh explore research-codebase plan implement review
```

默认目录：

```text
${CODEX_HOME:-$HOME/.codex}/skills
```

已有 skill 目录默认保持不变。使用 `--force` 覆盖。

构建发布包：

```bash
make dist
```

## 整理原则

- 原始 skill 保留原意和主要结构。
- Claude 专属工具名、路径和运行时语义只做 Codex 兼容替换。
- 长原文放进 `references/`。
- 调研、方案、计划、实现、审查保持分层。
- 小修改使用短流程。
- 有意改动记录在 `SOURCE-MAP.md`。

## 来源

来源：[themodernsoftware.dev](https://themodernsoftware.dev/)。

`SOURCE-MAP.md` 记录课程材料、原文快照和 Codex 适配文件之间的映射。

## License

本仓库原创的适配层、脚本和文档使用 MIT License。

`references/original-*` 中的课程原文快照保留原来源归属，不包含在上述 MIT 授权范围内。详见 `NOTICE.md`。
