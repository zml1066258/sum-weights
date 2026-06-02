# sum-weights

计算 `rl_init_final_weights` / `sft_init_final_weights` 等权重列表的左右列和与总总和。

## 安装

```bash
git clone <repo-url>
cp -r sum-weights/.claude/skills/sum-weights ~/.claude/skills/sum-weights
```

或者在已有项目中添加为 submodule：

```bash
git submodule add <repo-url> .claude/skills/sum-weights
```

## 使用

在 Claude Code（或兼容 `.claude/skills/` 的其他 agent）中粘贴权重列表，然后输入：

```
/sum-weights
```

Skill 会自动提取数字并调用计算器求和。

## 支持的 agent

- Claude Code
- OpenCode（兼容 `.claude/skills/` 格式）
- Codex
- 其他兼容 `.claude/skills/` 约定的 agent

## 项目结构

```
sum-weights/
└── .claude/skills/sum-weights/
    ├── SKILL.md          # Skill 定义
    └── sum_weights.py    # 加法计算器
```
