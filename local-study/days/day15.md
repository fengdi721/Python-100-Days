# Day 15 · 类、dataclass 与对象状态

第 3 周 · 每天 60–90 分钟 · [返回目录](../DAILY_INDEX.md)

## 今日知识

实例属性/类属性、__init__、dataclass、default_factory、frozen、repr。

## 主练习（约30–40分钟）

实现 CartItem(sku, unit_price_cents, quantity) 和 Cart；金额/数量需非负整数；Cart.add 后 total 返回总金额；每个购物车拥有自己的 items。

## 验收标准

两个 Cart 不共享列表；拒绝负数和 bool；同 SKU 可作为不同条目累加；repr 可用于调试。

除题目另有规定，写出正常、空输入、边界/非法输入的测试。说明你的接口约定，不要为了通过一个样例硬编码。

## 短练习 / 易错点（约10–15分钟）

修复 class Cart: items=[] 的共享状态；验证 frozen dataclass 中列表字段是否可 append。

## 面试口述（约10分钟）

dataclass 自动生成哪些方法？frozen 是深度不可变吗？

先闭卷回答，再查 [面试要点](../INTERVIEW_REVIEW.md)。每个回答至少一个最小例子和一个适用边界。

<details>
<summary>卡住20分钟后再看提示</summary>

可变字段使用 field(default_factory=list)；业务不变量仍要显式验证。

</details>

## 阅读入口（约10–15分钟）

以下为本周参考池。只查当天知识对应的小节，不需要每天重读全部章节；涉及现代版本时优先看官方文档。

- [主教材：18.面向对象编程入门](../../Day01-20/18.%E9%9D%A2%E5%90%91%E5%AF%B9%E8%B1%A1%E7%BC%96%E7%A8%8B%E5%85%A5%E9%97%A8.md)
- [主教材：19.面向对象编程进阶](../../Day01-20/19.%E9%9D%A2%E5%90%91%E5%AF%B9%E8%B1%A1%E7%BC%96%E7%A8%8B%E8%BF%9B%E9%98%B6.md)
- [主教材：20.面向对象编程应用](../../Day01-20/20.%E9%9D%A2%E5%90%91%E5%AF%B9%E8%B1%A1%E7%BC%96%E7%A8%8B%E5%BA%94%E7%94%A8.md)
- [主教材：31.Python语言进阶](../../Day31-35/31.Python%E8%AF%AD%E8%A8%80%E8%BF%9B%E9%98%B6.md)
- [官方：数据模型](https://docs.python.org/3.14/reference/datamodel.html)
- [官方：dataclasses](https://docs.python.org/3.14/library/dataclasses.html)

## 今天交付

- [ ] 自己的实现、测试或实验记录；可放 `exercises/day15.py`，项目日继续同一个项目。
- [ ] 正确性/边界说明；算法题附时间与空间复杂度。
- [ ] 两道口述题的自己的回答；不会的地方明确标记。
- [ ] 更新 [进度表](../PROGRESS.md) 和 [错题本](../MISTAKES.md)。
