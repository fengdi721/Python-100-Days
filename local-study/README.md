# Python 8 周学习与面试训练

适用：已有 PHP、Node.js 编程基础；每天 60–90 分钟，共 56 天（约 56–84 小时）。制定日期：2026-10-03。

目标：系统覆盖 Python 核心语法、对象模型、常用标准库、并发和工程实践，能独立解决中等难度问题并解释取舍。8 周足够完成一轮系统训练；“掌握所有 Python”不是有限课表能保证的结果，C 扩展实现、大型框架和数据科学生态另作专项。

## 从这里开始

1. 先打开 [Day 01](days/day01.md)，完成对象模型诊断和 `normalize_tags`。
2. 题目写在 `days/`；自己的代码放在 `exercises/`，测试放在 `tests/`，毕业项目放在 `projects/logtool/`。
3. 完成后更新 [进度表](PROGRESS.md)，并在 [错题本](MISTAKES.md) 记录原因。
4. 全部题目见 [56 天目录](DAILY_INDEX.md)，语法查漏见 [知识覆盖表](KNOWLEDGE_MAP.md)，面试复盘见 [回答要点](INTERVIEW_REVIEW.md)，跨语言对照见 [PHP/Node迁移表](PHP_NODE_TO_PYTHON.md)。

每日补充安排保存在 [`daily-briefs/`](daily-briefs/)；它用于当天热身和复习，不代表题目已完成。`local-study/` 已纳入你的 [GitHub fork](https://github.com/fengdi721/Python-100-Days) 的 `master` 分支；原作者仓库保留为 `upstream`。每天 09:00（Europe/Paris）的计划更新会检查进度并写一份简短安排，只有产生实际内容变化才提交并推送，不创建空提交。

本学习包位于教程的 `local-study/`，是为你编写的补充材料，不属于上游作者教程。上游原文保留；学习时按主题选读，不需要顺序读完100天。

## 每天怎么学

| 时间 | 内容 |
|---|---|
| 10–15 分钟 | 阅读当天知识点对应的教程或官方文档 |
| 30–40 分钟 | 独立完成主练习、边界测试和复杂度说明 |
| 10–15 分钟 | 短练习：先预测，再运行，再解释 |
| 10 分钟 | 口述两道面试题，写错题与复习记录 |

只有60分钟时采用10+30+10+10；有90分钟时增加反例和重构。选做项不计入必做。卡住20分钟可先看提示；仍不能完成时缩小输入做最小例子，第二天优先补完核心题。每隔7天做一次验收，复习时间替代当日阅读，不额外堆任务。

复习间隔：做错后 D+1、D+3、D+7 重做或口述。请先独立写，再用 AI 做代码评审；看懂答案不等于完成。

## 8 周安排

| 周 | 日期编号 | 核心内容 | 验收产物 |
|---|---|---|---|
| 1 | D01–07 | 对象绑定、容器、控制流、函数、异常、文件 | 可测试的日志分析函数 |
| 2 | D08–14 | 闭包、装饰器、生成器、上下文管理、模块、类型 | 流式日志处理管道 |
| 3 | D15–21 | dataclass、数据模型、继承、描述符、哈希、内存 | 订单领域模型与存储接口 |
| 4 | D22–28 | collections、itertools、文件格式、时间、CLI、SQLite | 能保存历史的命令行工具 |
| 5 | D29–35 | 哈希、双指针、窗口、BFS、二分、堆、回溯、DP | 限时算法题与复杂度分析 |
| 6 | D36–42 | 线程/进程、GIL、asyncio、取消、背压、锁 | 有界并发批处理器 |
| 7 | D43–49 | 测试、打包、类型接口、性能、HTTP边界、高级机制 | 一轮代码评审与修复 |
| 8 | D50–56 | 项目整合、交付验证、两场模拟面试、复盘 | 日志分析 CLI 与能力评估 |

基础语法不从“什么是变量”慢讲，但默认参数、浅拷贝、真值、闭包和 coroutine 启动语义必须动手验证。暂缓主教材中的前端入门、Linux入门、大量办公文档处理、爬虫、机器学习章节；这些不是本轮语言核心目标。

## 环境与第一道题

已核实本机有 `/opt/homebrew/bin/python3.14`（3.14.7），而当前终端默认 `python3` 指向旧的3.7.9。使用学习目录独立虚拟环境，避免误用旧版本。环境实际创建情况见 [SETUP.md](SETUP.md)。

```sh
cd ~/sources/python/learn-python/local-study
source .venv/bin/activate
python --version
python -m unittest discover -s tests -v
```

提供的 Day 01 实现刻意保留 `NotImplementedError`，因此初次测试应有10项报错；这是待完成的练习，不是10项已经通过。实现 `normalize_tags` 后再次运行，测试文件不需要改。通过测试后仍要解释代码与复杂度。

前六周主要使用标准库即可。第七周可以选装 pytest、mypy、ruff 等工具；题目也允许 stdlib unittest，不把工具安装当学习重点。现代语法以3.14学习，并注明：match 为3.10+；TaskGroup、except*、asyncio.timeout 为3.11+；新泛型/type 语法为3.12+；t-string 与新的注解求值规则属于3.14。

## 如何判断达标

每日验收：正常输入、空输入、边界/非法输入至少各一个测试；能解释副作用；需要算法分析时说明时间和空间；用自己的话口述两道题。

最终评分（这是自测标准，不是录用承诺）：

| 项目 | 分值 | 满分条件 |
|---|---:|---|
| 语言与对象语义 | 25 | 闭卷解释绑定、默认参数、闭包、迭代、哈希和对象协议，并能举反例 |
| 编程与算法 | 25 | 限时题正确、边界齐全、复杂度合理 |
| 并发与可靠性 | 20 | 正确区分线程/进程/协程，能处理超时、取消与共享状态 |
| 工程与测试 | 20 | 包可安装，入口可运行，关键行为有测试，失败可诊断 |
| 沟通与复盘 | 10 | 主动澄清约束、解释取舍、承认未知并查证 |

80分以上且无核心语义误解作为本轮通过；60–79分针对最弱两类补练一周；低于60分重做相关周验收。高级机制中的元类、解释器实现和新版本细节以“能阅读、解释、查文档”为目标，主线要求能独立实现。

## 资料与选择理由

GitHub 没有统一质量评分，这里用 Stars 衡量受欢迎程度，再看内容是否适合系统学习。下表为2026-10-03从 GitHub API 读取的快照，不代表完整榜单或质量保证。

| 仓库 | Stars | 用途 |
|---|---:|---|
| [vinta/awesome-python](https://github.com/vinta/awesome-python) | 324,802 | 框架/工具索引，用于查生态 |
| [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) | 225,220 | 算法实现参考，先独立解题再对照 |
| [jackfrued/Python-100-Days](https://github.com/jackfrued/Python-100-Days) | 187,043 | 本次主教材；核实的系统教程候选中 Stars 最高，中文且覆盖广 |
| [Asabeneh/30-Days-Of-Python](https://github.com/Asabeneh/30-Days-Of-Python) | 75,106 | 英文基础教程，可补漏 |
| [trekhleb/learn-python](https://github.com/trekhleb/learn-python) | 18,337 | 小型语法示例与测试 |
| [dabeaz-course/practical-python](https://github.com/dabeaz-course/practical-python) | 10,892 | 偏实践的课程，可后续精读 |

实际克隆主教材到 `~/sources/python/learn-python`，使用 depth=1 保留当前完整文件而省去大部分历史。上游提交：`44b2575bf42a02d0a38d9dada3f60335c95c5ec2`。若将来需要完整历史，可以自行执行 `git fetch --unshallow`。

所有每日练习与课表为本次定制。语义以 [Python 官方教程](https://docs.python.org/3.14/tutorial/)、[语言参考](https://docs.python.org/3.14/reference/) 和 [标准库](https://docs.python.org/3.14/library/) 为准；官方教程本来就面向已有编程基础、刚开始学 Python 的人。

现代主题补充：[asyncio](https://docs.python.org/3.14/library/asyncio-task.html)、[free-threading](https://docs.python.org/3.14/howto/free-threading-python.html)、[Python 3.14 变化](https://docs.python.org/3.14/whatsnew/3.14.html)、[PyPA 打包](https://packaging.python.org/en/latest/tutorials/packaging-projects/)、[pytest 参数化](https://docs.pytest.org/en/stable/how-to/parametrize.html)。主教材旧例子若与当前版本冲突，先缩小到最小复现再查官方文档，不整包安装旧依赖。

无需固定开始日期。每天打开相应任务即可；你可以在这个聊天里发送“检查 Day 05 的代码”或“开始 Day 12 的模拟面试”，并附上代码或给出本地文件路径。
