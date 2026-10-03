# Day 38 · TaskGroup、超时与取消

第 6 周 · 每天 60–90 分钟 · [返回目录](../DAILY_INDEX.md)

## 今日知识

结构化并发、asyncio.timeout、CancelledError、ExceptionGroup/except*。

## 主练习（约30–40分钟）

用 TaskGroup 同时运行3个任务，其中一个抛 ValueError，其余在 finally 记录清理；再用 asyncio.timeout 包裹一个慢任务。

## 验收标准

证明失败后兄弟任务被取消且清理执行；用 except* 处理分组错误；超时在上下文外按 TimeoutError 处理。

除题目另有规定，写出正常、空输入、边界/非法输入的测试。说明你的接口约定，不要为了通过一个样例硬编码。

## 短练习 / 易错点（约10–15分钟）

比较 gather 默认异常传播与 TaskGroup 的失败处理；把 CancelledError 吞掉会有什么后果？

## 面试口述（约10分钟）

取消是请求还是立即杀死？为什么清理后一般需要重新抛出 CancelledError？

先闭卷回答，再查 [面试要点](../INTERVIEW_REVIEW.md)。每个回答至少一个最小例子和一个适用边界。

<details>
<summary>卡住20分钟后再看提示</summary>

用事件协调任务启动，使测试可重复；别依赖偶然的调度顺序。

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

- [ ] 自己的实现、测试或实验记录；可放 `exercises/day38.py`，项目日继续同一个项目。
- [ ] 正确性/边界说明；算法题附时间与空间复杂度。
- [ ] 两道口述题的自己的回答；不会的地方明确标记。
- [ ] 更新 [进度表](../PROGRESS.md) 和 [错题本](../MISTAKES.md)。
