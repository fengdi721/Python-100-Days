# Day 42 · 第六周验收：异步批处理器

第 6 周 · 每天 60–90 分钟 · [返回目录](../DAILY_INDEX.md)

## 今日知识

并发上限、失败策略、超时、资源清理。

## 主练习（约30–40分钟）

实现 run_jobs(jobs, concurrency=3)：jobs 是 (id,delay,should_fail)，用本地模拟 I/O；每个任务独立超时，返回成功/失败/超时结果，不因单个业务失败放弃其他任务。

## 验收标准

输入20项，每项恰有一个结果；最大并发<=3；未知系统性异常仍可传播；外部取消触发清理且不被转换成普通业务失败。

除题目另有规定，写出正常、空输入、边界/非法输入的测试。说明你的接口约定，不要为了通过一个样例硬编码。

## 短练习 / 易错点（约10–15分钟）

口述“单任务失败隔离”与“整组立即失败”两种策略；指出何时选择 TaskGroup 加内部异常转换。

## 面试口述（约10分钟）

Node.js 的 Promise.all 经验哪些可迁移、哪些会误导？如何防止重试放大服务压力？

先闭卷回答，再查 [面试要点](../INTERVIEW_REVIEW.md)。每个回答至少一个最小例子和一个适用边界。

<details>
<summary>卡住20分钟后再看提示</summary>

显式规定失败策略；使用有界 worker 队列即可复用上一题。

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

- [ ] 自己的实现、测试或实验记录；可放 `exercises/day42.py`，项目日继续同一个项目。
- [ ] 正确性/边界说明；算法题附时间与空间复杂度。
- [ ] 两道口述题的自己的回答；不会的地方明确标记。
- [ ] 更新 [进度表](../PROGRESS.md) 和 [错题本](../MISTAKES.md)。
