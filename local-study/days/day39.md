# Day 39 · 限流、背压与异步协议

第 6 周 · 每天 60–90 分钟 · [返回目录](../DAILY_INDEX.md)

## 今日知识

Semaphore、Queue(maxsize)、async for/with、异步生成器。

## 主练习（约30–40分钟）

实现3个 worker 的生产消费队列，处理10个编号任务；队列容量2；用哨兵关闭，每个成功取出的任务都调用 task_done。

## 验收标准

每个编号恰好处理一次；最大活跃数<=3；queue.join 可结束；空输入也能退出；输出次序可不同。

除题目另有规定，写出正常、空输入、边界/非法输入的测试。说明你的接口约定，不要为了通过一个样例硬编码。

## 短练习 / 易错点（约10–15分钟）

写一个逐项产生数据的 async generator 并用 async for 消费；说明并发限制与“每秒请求数”不是同一个指标。

## 面试口述（约10分钟）

为什么队列需要有界？Semaphore 能单独保证 QPS 吗？

先闭卷回答，再查 [面试要点](../INTERVIEW_REVIEW.md)。每个回答至少一个最小例子和一个适用边界。

<details>
<summary>卡住20分钟后再看提示</summary>

每个 worker 都需要收到结束信号；失败路径也要处理 task_done。

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

- [ ] 自己的实现、测试或实验记录；可放 `exercises/day39.py`，项目日继续同一个项目。
- [ ] 正确性/边界说明；算法题附时间与空间复杂度。
- [ ] 两道口述题的自己的回答；不会的地方明确标记。
- [ ] 更新 [进度表](../PROGRESS.md) 和 [错题本](../MISTAKES.md)。
