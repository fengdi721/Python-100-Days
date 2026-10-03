# Day 23 · itertools 与函数工具

第 4 周 · 每天 60–90 分钟 · [返回目录](../DAILY_INDEX.md)

## 今日知识

chain/islice/groupby/product/combinations、partial、cache/lru_cache。

## 主练习（约30–40分钟）

实现连续分段 runs(iterable)，返回 (值,连续出现次数)；输入可以为生成器；再给递归 Fibonacci 添加 lru_cache 并观察 cache_info。

## 验收标准

['a','a','b','a'] → [('a',2),('b',1),('a',1)]；groupby 结果及时消费；缓存函数说明键需可哈希。

除题目另有规定，写出正常、空输入、边界/非法输入的测试。说明你的接口约定，不要为了通过一个样例硬编码。

## 短练习 / 易错点（约10–15分钟）

比较 groupby 与 SQL GROUP BY；用 islice 取无限计数器的前5项，避免 list 无限输入。

## 面试口述（约10分钟）

缓存什么时候会返回过期数据？groupby 为什么通常只处理相邻分组？

先闭卷回答，再查 [面试要点](../INTERVIEW_REVIEW.md)。每个回答至少一个最小例子和一个适用边界。

<details>
<summary>卡住20分钟后再看提示</summary>

连续分段不排序，否则会改变本题语义。

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

- [ ] 自己的实现、测试或实验记录；可放 `exercises/day23.py`，项目日继续同一个项目。
- [ ] 正确性/边界说明；算法题附时间与空间复杂度。
- [ ] 两道口述题的自己的回答；不会的地方明确标记。
- [ ] 更新 [进度表](../PROGRESS.md) 和 [错题本](../MISTAKES.md)。
