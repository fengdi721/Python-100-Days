# Day 41 · 进程池与批量处理

第 6 周 · 每天 60–90 分钟 · [返回目录](../DAILY_INDEX.md)

## 今日知识

可 pickle 对象、spawn、顶层函数、任务粒度、future 异常。

## 主练习（约30–40分钟）

实现 count_primes_batch(limits)：用顶层纯函数分别计算小于每个 limit 的素数数量；进程池返回与输入同序结果；顺序版用于验证。

## 验收标准

[10,20] → [4,8]；覆盖0/1/2；进程入口有保护；任务异常能在主进程观察；不传 lambda/打开的文件句柄。

除题目另有规定，写出正常、空输入、边界/非法输入的测试。说明你的接口约定，不要为了通过一个样例硬编码。

## 短练习 / 易错点（约10–15分钟）

故意把 worker 设为局部函数，记录错误并解释；估计序列化大列表的额外成本。

## 面试口述（约10分钟）

为何 macOS 上不能假设进程像线程一样共享 Python 对象？什么时候应增加批次大小？

先闭卷回答，再查 [面试要点](../INTERVIEW_REVIEW.md)。每个回答至少一个最小例子和一个适用边界。

<details>
<summary>卡住20分钟后再看提示</summary>

限制输入规模；核心是并发边界，不是素数算法优化。

</details>

## 阅读入口（约10–15分钟）

以下为本周参考池。只查当天知识对应的小节，不需要每天重读全部章节；涉及现代版本时优先看官方文档。

- [主教材：63.Python中的并发编程-1](../../Day61-65/63.Python%E4%B8%AD%E7%9A%84%E5%B9%B6%E5%8F%91%E7%BC%96%E7%A8%8B-1.md)
- [主教材：63.Python中的并发编程-2](../../Day61-65/63.Python%E4%B8%AD%E7%9A%84%E5%B9%B6%E5%8F%91%E7%BC%96%E7%A8%8B-2.md)
- [主教材：63.Python中的并发编程-3](../../Day61-65/63.Python%E4%B8%AD%E7%9A%84%E5%B9%B6%E5%8F%91%E7%BC%96%E7%A8%8B-3.md)
- [官方：asyncio任务](https://docs.python.org/3.14/library/asyncio-task.html)
- [官方：concurrent.futures](https://docs.python.org/3.14/library/concurrent.futures.html)
- [官方：free-threading](https://docs.python.org/3.14/howto/free-threading-python.html)

## 今天交付

- [ ] 自己的实现、测试或实验记录；可放 `exercises/day41.py`，项目日继续同一个项目。
- [ ] 正确性/边界说明；算法题附时间与空间复杂度。
- [ ] 两道口述题的自己的回答；不会的地方明确标记。
- [ ] 更新 [进度表](../PROGRESS.md) 和 [错题本](../MISTAKES.md)。
