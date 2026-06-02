---
name: sum-weights
description: 计算 rl_init_final_weights / sft_init_final_weights 等权重列表的左右列和与总总和。输入格式灵活，由我理解后提取数字，交给计算器做精确加法。
---

# Sum Weights

当用户粘贴包含权重列表的文本（如 `rl_init_final_weights: [...]`、`sft_init_final_weights: [...]`、或类似格式）时，按以下步骤处理。

## 步骤 1：理解输入

无论列表叫什么名字、有几段、注释格式如何，都由我来解析：
- 找到所有形如 `[value, value]` 的 pair
- 跳过以 `#` 开头的行为注释
- `_zero` 标记视为 `0`
- 支持整数和小数
- 可能同时包含 `rl` 和 `sft` 两个列表，也可能只有一个

## 步骤 2：准备计算器输入

将提取到的 pair 逐行写入临时文件，每行格式：
```
{左列值} {右列值}
```
注意：
- 值保留原始精度（整数或小数），不要做任何转换
- 每行一个 pair

## 步骤 3：调用计算器

```bash
python3 /home/luzm/.claude/skills/sum-weights/sum_weights.py < temp_file
```

## 步骤 4：输出结果

读取计算器输出，格式化为以下形式展示给用户：

```
### rl_init_final_weights（N 个条目）
- 左列总和：xxx
- 右列总和：xxx
- 所有数字总和：xxx
```

如果同时有 rl 和 sft，分别输出。如果某个列表条目较多且包含分块注释，可额外注明分块情况。

## 步骤 5：清理

删除临时文件。
