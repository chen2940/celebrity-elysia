# output/ — 技能打包产物目录

本目录用于存放打包后的技能产物（zip / tar.gz / 安装包等），**产物不纳入 git 版本库**（见根目录 `.gitignore`）。

用法示例：

```bash
# 打包完整技能目录（排除 .git / .workbuddy / versions 等）
tar -czf output/celebrity-elysia.tar.gz \
  --exclude='.git' --exclude='.workbuddy' --exclude='versions' \
  SKILL.md work.md persona.md work_skill.md persona_skill.md \
  manifest.json meta.json README.md elysia.jpg

# 或打成 zip（Windows）
Compress-Archive -Path SKILL.md,work.md,persona.md,work_skill.md,persona_skill.md,manifest.json,meta.json,README.md,elysia.jpg -DestinationPath output/celebrity-elysia.zip
```

用户拿到产物后，解压放入任意 Harness 的 skills 目录即可使用（`~/.claude/skills`、`~/.dsh/skills`、`~/.workbuddy/skills`、`~/.trae/skills` 等）。
