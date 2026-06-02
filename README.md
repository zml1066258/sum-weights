# sum-weights

计算 `rl_init_final_weights` / `sft_init_final_weights` 等权重列表的左右列和与总总和。

## 安装

### Claude Code 全局安装

```bash
mkdir -p ~/.claude/skills
git clone https://github.com/zml1066258/sum-weights.git /tmp/sum-weights
rm -rf ~/.claude/skills/sum-weights
cp -r /tmp/sum-weights/.claude/skills/sum-weights ~/.claude/skills/sum-weights
```

### opencode 全局安装

```bash
mkdir -p ~/.config/opencode/skills
git clone https://github.com/zml1066258/sum-weights.git /tmp/sum-weights
rm -rf ~/.config/opencode/skills/sum-weights
cp -r /tmp/sum-weights/.claude/skills/sum-weights ~/.config/opencode/skills/sum-weights
```

### 软链接复用方式

如果已经安装到了 Claude Code 目录，也可以让 opencode 复用同一份：

```bash
mkdir -p ~/.config/opencode/skills
ln -s ~/.claude/skills/sum-weights ~/.config/opencode/skills/sum-weights
```

这种方式可以避免维护两份 skill。

### 项目内安装

也可以在已有项目中添加为 submodule：

```bash
git submodule add https://github.com/zml1066258/sum-weights.git .claude/skills/sum-weights
```

## 使用

在 Claude Code、opencode 或其他兼容 skills 约定的 agent 中粘贴权重列表，然后输入：

```
/sum-weights
```

Skill 会自动提取数字并调用计算器求和。

## 支持的 agent

- Claude Code
- opencode
- Codex
- 其他兼容 skills 约定的 agent

## 项目结构

```
sum-weights/
└── .claude/skills/sum-weights/
    ├── SKILL.md          # Skill 定义
    └── sum_weights.py    # 加法计算器
```
