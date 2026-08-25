# output/ — 技能打包产物目录

本目录用于存放打包后的技能产物（zip / tar.gz / 安装包等），**产物不纳入 git 版本库**（见根目录 `.gitignore`）。

> **产物必须包含 `knowledge/`**（研究知识库：6-track 原始研究 / 合并摘要 / 审计复核报告 / 参考文档），它是技能的证据基础与诚实边界来源，缺了会影响质量说明与置信度标注。

用法示例（推荐整目录打包，`knowledge`、`tools` 等自动包含，不易漏文件）：

```bash
# macOS / Linux：整目录打包，排除缓存与历史
tar -czf output/celebrity-elysia.tar.gz \
  --exclude='.git' --exclude='.workbuddy' --exclude='versions' --exclude='output' \
  .

# Windows (PowerShell)：整目录打包（同样包含 knowledge/）
$items = @('SKILL.md','work.md','persona.md','work_skill.md','persona_skill.md',`
          'manifest.json','meta.json','README.md','elysia.jpg',`
          'chat_dsh.png','chat_workbuddy.png','chat_trae.png',`
          'knowledge','tools')
Compress-Archive -Path $items -DestinationPath output/celebrity-elysia.zip
```

打包后建议自检产物完整性：

```bash
tar -tzf output/celebrity-elysia.tar.gz | grep -E 'knowledge|SKILL.md|tools'
```

用户拿到产物后，解压放入任意 Harness 的 skills 目录即可使用（`~/.claude/skills`、`~/.dsh/skills`、`~/.workbuddy/skills`、`~/.trae/skills` 等）；`tools/install.py` 也可在解压后直接运行完成安装。
