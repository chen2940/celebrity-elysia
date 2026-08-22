# Research Audit

## Verdict
- Status: PASS
- Reason: 六 track 全部覆盖且内容互不克隆；84 个可落地 URL（均为具体内容页，无平台首页/搜索页）；无黑名单信源；22 条矛盾中至少 6 条为实质性张力；6 个候选心智模型均有跨维度证据；known-answer 与 edge-case 锚点齐备。唯一显著弱项是加权一手占比 29%（低于 50% 理想值），已在下方如实记录并给出回填任务，不构成阻止 synthesis 的理由——该弱项源于研究对象为虚构角色且本研究为 web-only，官方一手载体（动画/印象曲/新闻稿）数量天然有限，而核心叙事证据大量来自官方内容的粉丝逐字转写（内容层一手、宿主层二手）。

## Coverage Review
- Track coverage: 6/6 dimensions covered
- Missing or weak tracks: 无缺失；维度 2（对话）与维度 3（表达DNA）的证据多为检索摘要级，维度 4（决策）的动机推断占比偏高（官方无直接文本）
- Cross-track redundancy: 各 track 提取焦点互异（著作=文本结构；对话=即兴应对；DNA=语言指纹；决策=行为选择；他者=外部评价；时间线=认知演变）；重叠处（如"把大事说小"在 D2/D3 双出现）以互证形式存在，非克隆

## Source Quality Assessment

### Source Mix
- Primary-source count: 7 个一手标记（官方动画/印象曲/新闻稿/官方社区贺文 + 一手台词转写中的明确一手标注）
- Secondary-source count: 大量（社区整理、长文分析、论坛讨论），合计 97 次来源提及、84 个独立 URL
- Primary-source ratio: 加权 29%（Tier 1-3 计 27/94），低于 50% 目标；替代达标项：高权重一手绝对数 27 ≥ 3（quality_check 的 source_hierarchy 门槛通过）
- Grounding quality: 引用的 URL 均为具体内容页（B站视频/专栏、NGA 帖、小米游戏中心长文、PTT 帖、官方新闻页等），非首页/搜索页/占位路径；访问级别多为 snippet 级（partial），已在各笔记 Access note 如实标注

### Source Hierarchy Compliance
- Sources from weight 1-3 (highest quality): 27（官方动画短片、印象曲、官方新闻稿、官方社区贺文、官方生日会视频、一手台词/剧情逐字转写）
- Sources from weight 4-5 (medium quality): 54（粉丝整理、社区长文、媒体稿、投票帖）
- Sources from weight 6-7 (lowest quality): 13（二手转述、指针级内容）
- Blacklisted sources used: 无（知乎、微信公众号、百度百科、百家号仅作定位线索，未作为证据；萌娘百科/Fandom 仅作指针）

### Taste Principle Compliance
- Long-form vs. snippet ratio: 长文占比高（小米游戏中心系列长文、B站专栏长文、考据长文、独立博客、NGA 长帖），金句类短源占比低
- Firsthand vs. secondhand ratio: 内容层一手充分（官方短片独白、游戏台词转写），宿主层以二手为主（web-only 限制）
- Controversial/distinctive positions captured: 是——"亲女儿/内部爱"争议、跨游戏复用（昔涟）之争、"完美即扁平"批评、英文圈无感群体、结局"安然归来"的公平性质疑
- Thinking evolution documented: 是——维度 6 记录了认知轨迹（律者→人→牺牲→记忆体）与"静止主角、反转观众"的叙事结构；但需注意角色为虚构，其"认知演变"实为官方叙事设计

## Contradictions Inventory
- Total contradictions found: 22
- Classification:
  - Temporal (view evolution): 官方叙事反转（v5.0 英桀示人 vs 2022-01 律者揭示；第十三律者 vs "最初的律者"名实错位）
  - Contextual (domain differences): 中英文社区温差；官方话术"唯一性" vs 跨游戏复用；对千劫皮 vs 对凯文敬（分人定制距离）
  - Inherent (value tensions): "爱所有人" vs 向所有人隐瞒身份；选择赴死 vs 留下记忆体（死与不死）；"完美妖精"标签既是魅力也是被批"扁平"的原因
- Quality: 实质性张力为主（多为官方未缝合的叙事/价值观张力，非表面文字游戏），满足 ≥3 实质性矛盾要求

## Mental Model Candidates
- Candidate count: 6（目标 ≥3）
- For each candidate:
  - MM1 以死证道（用自己证明一个命题）：cross-context = D1 告别独白（播种隐喻）+ D4 牺牲决策 + D5 社区对"她必须死"的共识；初步 gate：三重门均大概率通过
  - MM2 把大事说小（轻量化语域）：cross-context = D2 试炼对话 + D3 语音指纹（"有些为难"/"商量一下"）；初步 gate：cross-context 通过、generative 通过、exclusive 通过
  - MM3 提前布置退场（遗产设计/对抗遗忘）：cross-context = D1 生日"记得我"母题 + D4 记忆体布置 + D6 时间线余波期；初步 gate：cross-context 通过、generative 通过、exclusive 中
  - MM4 静止主角、反转观众（不解释、不辩解）：cross-context = D2 装傻策略 + D4 隐瞒身份 + D6 认知轨迹；初步 gate：cross-context 通过、generative 通过、exclusive 高
  - MM5 爱着不完美（缺陷包容）：cross-context = D1 "他们从来不是完美的英雄" + D4 对英桀的选择 + D5 英桀内部分裂评价下她仍亲近所有人；初步 gate：三通过
  - MM6 把判断权交给对方（反问代替回答）：cross-context = D1 "是你喜欢的女孩吗♪" + D2 对话策略 + D3 句式指纹；初步 gate：cross-context 通过、generative 中、exclusive 中（可能与 MM4 部分重叠，synthesis 阶段需区分）

## Known-Answer Bank
- Question 1: 爱莉希雅如何看待自己的律者身份？
  Evidence anchors: D1 告别独白（"最初的律者，人之律者"）+ D4 觉醒为"人之律者"的选择 + 官方主线叙述"她生来就是一个律者"；方向：身份由选择而非出身决定
- Question 2: 她为什么选择牺牲？
  Evidence anchors: D4 牺牲决策 + D5 社区讨论（"为什么她必须死"）+ D1 独白的播种隐喻；方向：以死证明律者可以选择成为人、留下"人类的可能性"
- Strength: 两条均可由研究证据作答，方向与框架清晰，置信度中-高

## Edge-Case Candidate
- Question: 如果一位与她素不相识、与"守护人类"宏大叙事无关的普通人向她求助，她会如何回应？
- Why this is adjacent but under-evidenced: 现有证据集中于她与英桀/芽衣的互动（都有守护者的语境预设）；"纯私人、无宏大意义"场景无直接文本
- Expected reasoning approach: 依据 MM2（把大事说小）、MM6（把判断权交给对方）、MM5（爱着不完美），她大概率会以俏皮轻量语域接近、先建立亲昵、再用"商量式"帮助完成，且不会解释自己为何帮忙

## Cold Figure Assessment
- Total grounded sources: 84 个独立 URL
- Is this a cold figure (<10 sources)?: 否——材料极其丰富，属于"热角色"
- 冷门降级策略: 不适用

## Backfill Tasks
- 提高一手占比：用户可在游戏内截取角色档案页、乐土档案文本、生日语音原文（一手宿主），可把加权一手占比从 29% 显著提升
- 补强维度 2/3 的原文级证据：提供《因你而在的故事》短片台词全文、往世乐土剧情文本整理（现有为摘要级）
- 补强维度 4 决策动机：提供主线 25–31 章关键场景原文（牺牲场景、身份揭示场景）
- 补强维度 5 批评侧：提供更多一手/代表性批评长文（黑名单外平台），平衡"赞美侧 vs 批评侧"比例
- 英文侧：补充 Reddit/YouTube essay 类英文深度分析，弥合中英温差证据
