# Day 10 · 迭代器与生成器

第 2 周 · 每天 60–90 分钟 · [返回目录](../DAILY_INDEX.md)

## 今日知识

iter/next、StopIteration、yield、yield from、生成器表达式、惰性求值。

## 主练习（约30–40分钟）

实现 chunks(iterable, size) 生成器，每次产生最多 size 个元素的 list；接受只能遍历一次的输入；size<=0 抛 ValueError。

## 验收标准

range(5),2 → [[0,1],[2,3],[4]]；空输入没有输出；不提前耗尽输入；空间 O(size)；注明参数错误发生在调用还是首次迭代。

除题目另有规定，写出正常、空输入、边界/非法输入的测试。说明你的接口约定，不要为了通过一个样例硬编码。

## 短练习 / 易错点（约10–15分钟）

对同一生成器连续 list() 两次，解释结果；将两个小生成器用 yield from 串接。选做：用 send 实现累计器。

## 面试口述（约10分钟）

iterable 与 iterator 的关系是什么？为什么生成器不能直接重复使用？

先闭卷回答，再查 [面试要点](../INTERVIEW_REVIEW.md)。每个回答至少一个最小例子和一个适用边界。

<details>
<summary>卡住20分钟后再看提示</summary>

在 yield 前创建新缓冲区，避免后续原地修改已返回的列表。

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

- [ ] 自己的实现、测试或实验记录；可放 `exercises/day10.py`，项目日继续同一个项目。
- [ ] 正确性/边界说明；算法题附时间与空间复杂度。
- [ ] 两道口述题的自己的回答；不会的地方明确标记。
- [ ] 更新 [进度表](../PROGRESS.md) 和 [错题本](../MISTAKES.md)。
