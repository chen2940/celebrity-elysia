# 打包与核验

在仓库根目录运行相应命令。两种格式都从当前工作目录取文件，适合打包已检出的版本和本地修改。输出位于 `output/`，清单保留主入口、拆分入口、安装脚本、文档与完整的 `knowledge/`。

## Windows PowerShell

```powershell
New-Item -ItemType Directory -Force -Path output | Out-Null
$releaseItems = @(
    'SKILL.md', 'persona.md', 'work.md', 'persona_skill.md', 'work_skill.md',
    'manifest.json', 'meta.json', 'README.md', 'PACKAGING.md',
    'elysia.jpg', 'chat_dsh.png', 'chat_workbuddy.png', 'chat_trae.png',
    'install.ps1', 'install.sh', 'tools', 'knowledge'
)
Compress-Archive -LiteralPath $releaseItems -DestinationPath output/celebrity-elysia.zip
python -m zipfile -t output/celebrity-elysia.zip
python -m zipfile -l output/celebrity-elysia.zip
```

## macOS / Linux

```bash
mkdir -p output
tar -czf output/celebrity-elysia.tar.gz \
  SKILL.md persona.md work.md persona_skill.md work_skill.md \
  manifest.json meta.json README.md PACKAGING.md \
  elysia.jpg chat_dsh.png chat_workbuddy.png chat_trae.png \
  install.ps1 install.sh tools knowledge
tar -tzf output/celebrity-elysia.tar.gz
```

## 检查与安装

1. 在包清单中检查 `SKILL.md`、`persona_skill.md`、`work_skill.md`、`tools/install.py` 和 `knowledge/docs/bh3text_canon.md`。`knowledge/research/` 下应包含原始研究、合并摘要与评审记录。
2. 解压到名为 `celebrity-elysia` 的目录，确认 `SKILL.md` 直接位于该目录下。
3. 在解压目录运行 `python tools/install.py --host codex --dry-run` 确认目标位置，按所用宿主替换 `--host`。安装命令与手动路径见[安装说明](README.md#安装)。
