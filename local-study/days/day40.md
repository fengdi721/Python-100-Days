# Day 40 · 共享状态与锁

第 6 周 · 每天 60–90 分钟 · [返回目录](../DAILY_INDEX.md)

## 今日知识

竞态、Lock、死锁、线程安全、asyncio.Lock、GIL 不等于业务原子性。

## 主练习（约30–40分钟）

用 Barrier 制造两个线程同时读取相同计数再写回，稳定复现丢失更新；再用 Lock 保护完整读改写，使两次递增得到2。

## 验收标准

先稳定得到错误结果1；修复版本得到2；Barrier 不放在只允许一个线程进入的锁内部；测试设置超时防卡死。

除题目另有规定，写出正常、空输入、边界/非法输入的测试。说明你的接口约定，不要为了通过一个样例硬编码。

## 短练习 / 易错点（约10–15分钟）

写两个协程在“读计数”和“写计数”间 await，复现竞态，再用 asyncio.Lock 修复。

## 面试口述（约10分钟）

有 GIL 为什么仍需要锁？为何不能持有 threading.Lock 时 await 等待另一个协程？

先闭卷回答，再查 [面试要点](../INTERVIEW_REVIEW.md)。每个回答至少一个最小例子和一个适用边界。

<details>
<summary>卡住20分钟后再看提示</summary>

人为制造调度点比寄希望于随机跑出竞态更可靠。

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

- [ ] 自己的实现、测试或实验记录；可放 `exercises/day40.py`，项目日继续同一个项目。
- [ ] 正确性/边界说明；算法题附时间与空间复杂度。
- [ ] 两道口述题的自己的回答；不会的地方明确标记。
- [ ] 更新 [进度表](../PROGRESS.md) 和 [错题本](../MISTAKES.md)。
