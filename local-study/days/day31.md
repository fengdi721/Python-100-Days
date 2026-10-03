# Day 31 · 栈、队列与 BFS

第 5 周 · 每天 60–90 分钟 · [返回目录](../DAILY_INDEX.md)

## 今日知识

栈、deque、visited、图的广度优先搜索。

## 主练习（约30–40分钟）

实现 shortest_path(graph,start,goal)，无权邻接表图返回最短节点路径或 None；节点为字符串，所有邻接节点均视为合法节点。

## 验收标准

覆盖环、断开图、start==goal、邻接缺项；同长度路径按邻接列表顺序选择；O(V+E) 时间。

除题目另有规定，写出正常、空输入、边界/非法输入的测试。说明你的接口约定，不要为了通过一个样例硬编码。

## 短练习 / 易错点（约10–15分钟）

用栈实现括号检查，只接受 ()[]{}；'([)]' 为 False，空串为 True，其他字符拒绝。

## 面试口述（约10分钟）

为什么 BFS 用队列而 DFS 用栈？visited 在入队还是出队时设置更合适？

先闭卷回答，再查 [面试要点](../INTERVIEW_REVIEW.md)。每个回答至少一个最小例子和一个适用边界。

<details>
<summary>卡住20分钟后再看提示</summary>

记录 parent 后回溯重建路径，避免在队列里不断复制整条路径。

</details>

## 阅读入口（约10–15分钟）

以下为本周参考池。只查当天知识对应的小节，不需要每天重读全部章节；涉及现代版本时优先看官方文档。

- [主教材：31.Python语言进阶](../../Day31-35/31.Python%E8%AF%AD%E8%A8%80%E8%BF%9B%E9%98%B6.md)
- [算法实现参考（做完再对照）](https://github.com/TheAlgorithms/Python)
- [官方：heapq](https://docs.python.org/3.14/library/heapq.html)
- [官方：bisect](https://docs.python.org/3.14/library/bisect.html)

## 今天交付

- [ ] 自己的实现、测试或实验记录；可放 `exercises/day31.py`，项目日继续同一个项目。
- [ ] 正确性/边界说明；算法题附时间与空间复杂度。
- [ ] 两道口述题的自己的回答；不会的地方明确标记。
- [ ] 更新 [进度表](../PROGRESS.md) 和 [错题本](../MISTAKES.md)。
