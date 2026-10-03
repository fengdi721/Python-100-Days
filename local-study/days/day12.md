# Day 12 · 模块、包与导入

第 2 周 · 每天 60–90 分钟 · [返回目录](../DAILY_INDEX.md)

## 今日知识

import/from、__name__、__main__、sys.path、相对导入、导入缓存和循环依赖。

## 主练习（约30–40分钟）

将第一周日志分析器拆成 logtool/parser.py、stats.py、__main__.py；支持 python -m logtool FILE，导入模块本身不能读文件或打印。

## 验收标准

从包的父目录可运行；提供 --help；不存在文件返回非零状态；用测试验证 import 无输出、核心函数可独立调用。

除题目另有规定，写出正常、空输入、边界/非法输入的测试。说明你的接口约定，不要为了通过一个样例硬编码。

## 短练习 / 易错点（约10–15分钟）

制造 parser↔stats 循环导入，记录失败原因，再把共享类型提取到 model.py。

## 面试口述（约10分钟）

为什么项目中的 json.py 可能破坏 import json？python file.py 与 python -m package 有哪些差别？

先闭卷回答，再查 [面试要点](../INTERVIEW_REVIEW.md)。每个回答至少一个最小例子和一个适用边界。

<details>
<summary>卡住20分钟后再看提示</summary>

入口负责参数与 I/O，模块内部不要通过修改 sys.path 修补设计。

</details>

## 阅读入口（约10–15分钟）

以下为本周参考池。只查当天知识对应的小节，不需要每天重读全部章节；涉及现代版本时优先看官方文档。

- [主教材：16.函数使用进阶](../../Day01-20/16.%E5%87%BD%E6%95%B0%E4%BD%BF%E7%94%A8%E8%BF%9B%E9%98%B6.md)
- [主教材：17.函数高级应用](../../Day01-20/17.%E5%87%BD%E6%95%B0%E9%AB%98%E7%BA%A7%E5%BA%94%E7%94%A8.md)
- [主教材：31.Python语言进阶](../../Day31-35/31.Python%E8%AF%AD%E8%A8%80%E8%BF%9B%E9%98%B6.md)
- [官方：模块](https://docs.python.org/3.14/tutorial/modules.html)
- [官方：typing](https://docs.python.org/3.14/library/typing.html)
- [官方：contextlib](https://docs.python.org/3.14/library/contextlib.html)

## 今天交付

- [ ] 自己的实现、测试或实验记录；可放 `exercises/day12.py`，项目日继续同一个项目。
- [ ] 正确性/边界说明；算法题附时间与空间复杂度。
- [ ] 两道口述题的自己的回答；不会的地方明确标记。
- [ ] 更新 [进度表](../PROGRESS.md) 和 [错题本](../MISTAKES.md)。
