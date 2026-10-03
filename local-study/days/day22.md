# Day 22 · collections 与队列

第 4 周 · 每天 60–90 分钟 · [返回目录](../DAILY_INDEX.md)

## 今日知识

Counter、defaultdict、deque、ChainMap、namedtuple；容器复杂度。

## 主练习（约30–40分钟）

实现 recent_counts(events, window)：事件为 (非递减整数秒时间戳, user)，返回每个事件到达后区间 (t-window,t] 内事件总数。window 必须为正。

## 验收标准

窗口10，时间戳[0,5,10,10] → [1,2,2,3]；支持空输入；每条事件入队出队至多一次，总 O(n)。

除题目另有规定，写出正常、空输入、边界/非法输入的测试。说明你的接口约定，不要为了通过一个样例硬编码。

## 短练习 / 易错点（约10–15分钟）

用 Counter 统计字符并按次数降序、字符升序输出；解释 deque.popleft 与 list.pop(0) 的复杂度差别。

## 面试口述（约10分钟）

defaultdict 的读取何时会插入键？Counter 与普通 dict 有何行为区别？

先闭卷回答，再查 [面试要点](../INTERVIEW_REVIEW.md)。每个回答至少一个最小例子和一个适用边界。

<details>
<summary>卡住20分钟后再看提示</summary>

窗口左端开区间，因此移除 timestamp <= t-window 的事件。

</details>

## 阅读入口（约10–15分钟）

以下为本周参考池。只查当天知识对应的小节，不需要每天重读全部章节；涉及现代版本时优先看官方文档。

- [主教材：21.文件读写和异常处理](../../Day21-30/21.%E6%96%87%E4%BB%B6%E8%AF%BB%E5%86%99%E5%92%8C%E5%BC%82%E5%B8%B8%E5%A4%84%E7%90%86.md)
- [主教材：22.对象的序列化和反序列化](../../Day21-30/22.%E5%AF%B9%E8%B1%A1%E7%9A%84%E5%BA%8F%E5%88%97%E5%8C%96%E5%92%8C%E5%8F%8D%E5%BA%8F%E5%88%97%E5%8C%96.md)
- [主教材：23.Python读写CSV文件](../../Day21-30/23.Python%E8%AF%BB%E5%86%99CSV%E6%96%87%E4%BB%B6.md)
- [主教材：30.正则表达式的应用](../../Day21-30/30.%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F%E7%9A%84%E5%BA%94%E7%94%A8.md)
- [官方：标准库目录（按当天模块名查阅）](https://docs.python.org/3.14/library/index.html)
- [官方：SQLite](https://docs.python.org/3.14/library/sqlite3.html)

## 今天交付

- [ ] 自己的实现、测试或实验记录；可放 `exercises/day22.py`，项目日继续同一个项目。
- [ ] 正确性/边界说明；算法题附时间与空间复杂度。
- [ ] 两道口述题的自己的回答；不会的地方明确标记。
- [ ] 更新 [进度表](../PROGRESS.md) 和 [错题本](../MISTAKES.md)。
