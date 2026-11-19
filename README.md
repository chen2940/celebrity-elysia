# 爱莉希雅（Elysia）· Celebrity Skill

《崩坏3》爱莉希雅的第一人称对话技能。它参考剧情中的表达和选择，用于日常聊天、往世乐土与十三英桀的剧情问答，以及关系、抉择和告别场景。

**当前版本 v10 · 2026-11-19**

<img src="elysia.jpg" alt="人之律者爱莉希雅" width="100%">

## 安装

### 从当前目录安装

在仓库根目录或解压后的技能目录运行。示例将技能安装到 Codex，使用其他宿主时替换 `--host` 参数。macOS / Linux 可用 `python3`。

```bash
python tools/install.py --host codex --dry-run
python tools/install.py --host codex
```

`--dry-run` 显示目标位置。省略 `--host` 会检测已有的宿主技能目录。已有同名安装时，添加 `--force` 可用当前目录的版本替换它。安装后重启或重载宿主。

### 从 GitHub 安装

快捷脚本下载 GitHub `main` 分支并调用 Python 安装器。

```bash
# macOS / Linux
curl -fsSL https://raw.githubusercontent.com/chen2940/celebrity-elysia/main/install.sh | bash
```

```powershell
# Windows PowerShell
irm https://raw.githubusercontent.com/chen2940/celebrity-elysia/main/install.ps1 | iex
```

### 手动安装路径

也可以把整个项目目录放在宿主的技能目录下。安装后的入口路径形如 `<技能目录>/celebrity-elysia/SKILL.md`，同级保留 `knowledge/` 和人物、工作文档。

| 宿主 | `--host` | 技能目录 |
| --- | --- | --- |
| Claude Code | `claude-code` | `~/.claude/skills` |
| OpenClaw | `openclaw` | `~/.openclaw/skills` 或 `~/.openclaw/workspace/skills` |
| Codex | `codex` | `~/.codex/skills` |
| Hermes | `hermes` | `~/.hermes/skills` |
| DeepSeek Harness | `dsh` | `~/.dsh/skills`，设置 `DSH_HOME` 时使用其 `skills/` 子目录。项目级安装可放入 `<项目>/.dsh/skills`。 |
| WorkBuddy | `workbuddy` | `~/.workbuddy/skills` |
| TRAE Work | `trae` | `~/.trae/skills` |
| Cursor | `cursor` | `~/.cursor/skills` |

## 使用

按技能名 `celebrity-elysia` 激活。支持斜杠命令的宿主可尝试 `/celebrity-elysia`。首次激活时会提示这是根据剧情和公开文本构建的 AI 视角，此后用第一人称回应。独立发送 `exit` 或 `退出`，或明确要求退出，即可切回普通模式。

| 我想使用 | 入口 | 用途 |
| --- | --- | --- |
| 完整技能 | [SKILL.md](SKILL.md) | 角色对话、剧情问答和工作方法 |
| 人物性格 | [persona_skill.md](persona_skill.md) | 表达、关系距离、剧情视角和多轮接话 |
| 工作方法 | [work_skill.md](work_skill.md) | 缓和冲突、分析抉择和交接经验 |

普通目录安装以 `SKILL.md` 为主入口，可直接在对话里指定只用人物性格或工作方法。独立调用方式取决于宿主。拆分文件及命令标识见[技能清单](manifest.json)。

> 以爱莉希雅的视角和我聊聊。我刚看完《崩坏3》主线第 28 章，后面的剧情先别剧透。

<details>
<summary>角色资料与历史对话截图</summary>

| 项目 | 内容 |
| --- | --- |
| 名称 | 爱莉希雅 / Elysia / 粉色妖精小姐♪ / 爱莉 |
| 出典 | 米哈游《崩坏3》（Honkai Impact 3rd） |
| 所属 | 前文明逐火十三英桀第Ⅱ席「真我」 |
| 律者称谓 | 人之律者、始源之律者 |
| 生日 | 11 月 11 日 |
| 童年成长地 | 沃斯托克-51 |
| 剧情视角 | 前文明本人、往世乐土记忆体 |

历史对话截图：[DeepSeek Harness](chat_dsh.png) · [WorkBuddy](chat_workbuddy.png) · [TRAE Work](chat_trae.png)

</details>

## 版本与剧情依据

| 版本 | 更新 |
| --- | --- |
| v10 | 补入六段往世乐土对话，调整接受纠正、转向正事、听到拒绝和核对台词归属的规则。剧透进度在追问中继续有效。 |
| v9 | 核对了往世乐土第一章与主线第 29–31 章选段，订正律者称谓、十三英桀提案与审批、记忆体与心象世界的语境。 |
| v8 | 恢复日常对话轻快、话密的表达。 |

剧情事实优先查已核对的场次与说话者。BH3Text 是游戏文本的第三方存档。资料卡细节、人物动机与权能机制按各自的证据说明。章节链接、剧透范围和旧版六路研究见[知识库索引](knowledge/README.md)。

## 维护

修改人物规则或工作方法时，同步对应的拆分入口正文，并按需要更新主入口。人物文档中有 8 道单轮题和 6 组多轮题，可在宿主会话里检验更改。 [人物文档](persona.md) · [工作文档](work.md)

技能 ID 为 `meta-skill.celebrity.elysia`，dot-skill 预设为 `dot.celebrity.v1`，研究配置为 `budget-unfriendly`。历史版本快照位于 `versions/`。版本、资料卡和来源记录见[元信息](meta.json)。

发布包包含完整的 `knowledge/`，以便技能在解压后仍能按章节查证。打包命令和自检步骤见[打包与核验](PACKAGING.md)。
