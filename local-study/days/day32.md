# Day 32 · 二分、堆与 Top K

第 5 周 · 每天 60–90 分钟 · [返回目录](../DAILY_INDEX.md)

## 今日知识

bisect、heapq、二分边界、排序成本。

## 主练习（约30–40分钟）

手写 lower_bound(sorted_nums,target)，返回首个 >=target 的位置；再实现 kth_largest(iterable,k)，允许重复，使用大小为 k 的最小堆。

## 验收标准

lower_bound([1,2,2,4],2)=1；目标5返回4；空返回0。kth_largest([3,1,3,2],2)=3；k<=0 或超过数量拒绝；O(n log k)。

除题目另有规定，写出正常、空输入、边界/非法输入的测试。说明你的接口约定，不要为了通过一个样例硬编码。

## 短练习 / 易错点（约10–15分钟）

解释 heap[0] 为什么不是“第一个插入的元素”；列出排序、全量堆、固定大小堆的成本。

## 面试口述（约10分钟）

二分查找的不变量是什么？有序列表用 bisect 查到位置后插入仍是 O(log n) 吗？

先闭卷回答，再查 [面试要点](../INTERVIEW_REVIEW.md)。每个回答至少一个最小例子和一个适用边界。

<details>
<summary>卡住20分钟后再看提示</summary>

二分统一使用左闭右开区间；堆大小不能无限增加。

</details>

## 阅读入口（约10–15分钟）

以下为本周参考池。只查当天知识对应的小节，不需要每天重读全部章节；涉及现代版本时优先看官方文档。

- [主教材：31.Python语言进阶](../../Day31-35/31.Python%E8%AF%AD%E8%A8%80%E8%BF%9B%E9%98%B6.md)
- [算法实现参考（做完再对照）](https://github.com/TheAlgorithms/Python)
- [官方：heapq](https://docs.python.org/3.14/library/heapq.html)
- [官方：bisect](https://docs.python.org/3.14/library/bisect.html)

## 今天交付

- [ ] 自己的实现、测试或实验记录；可放 `exercises/day32.py`，项目日继续同一个项目。
- [ ] 正确性/边界说明；算法题附时间与空间复杂度。
- [ ] 两道口述题的自己的回答；不会的地方明确标记。
- [ ] 更新 [进度表](../PROGRESS.md) 和 [错题本](../MISTAKES.md)。
