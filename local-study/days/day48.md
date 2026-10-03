# Day 48 · 高级机制与版本差异

第 7 周 · 每天 60–90 分钟 · [返回目录](../DAILY_INDEX.md)

## 今日知识

__getattr__/__getattribute__、__new__/__init__、__init_subclass__、metaclass；3.14 注解延迟求值与 t-string 概念。

## 主练习（约30–40分钟）

用 __init_subclass__ 实现插件注册表，每个带 name 的子类自动登记，重复名称拒绝；再用 __getattr__ 为配置对象转发缺失属性并正确抛 AttributeError。

## 验收标准

两个子类可按名称查到；重复名异常；hasattr 缺失项为 False；未知属性无无限递归；能说明为何本题无需元类。

除题目另有规定，写出正常、空输入、边界/非法输入的测试。说明你的接口约定，不要为了通过一个样例硬编码。

## 短练习 / 易错点（约10–15分钟）

阅读3.14变更：比较 f-string 结果 str 与 t-string 的 Template；说明注解何时求值可能受版本与 future import 影响。选做：写元类版注册表对比。

## 面试口述（约10分钟）

什么时候需要元类、什么时候类装饰器或 __init_subclass__ 已足够？__getattribute__ 容易如何递归？

先闭卷回答，再查 [面试要点](../INTERVIEW_REVIEW.md)。每个回答至少一个最小例子和一个适用边界。

<details>
<summary>卡住20分钟后再看提示</summary>

先掌握可读的实现，元类以能解释/阅读为目标；版本特性不靠背旧面试答案。

</details>

## 阅读入口（约10–15分钟）

以下为本周参考池。只查当天知识对应的小节，不需要每天重读全部章节；涉及现代版本时优先看官方文档。

- [主教材：96.软件测试和自动化测试](../../Day91-100/96.%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%92%8C%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95.md)
- [主教材：99.面试中的公共问题](../../Day91-100/99.%E9%9D%A2%E8%AF%95%E4%B8%AD%E7%9A%84%E5%85%AC%E5%85%B1%E9%97%AE%E9%A2%98.md)
- [PyPA：打包指南](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- [官方：unittest](https://docs.python.org/3.14/library/unittest.html)
- [官方：3.14变化](https://docs.python.org/3.14/whatsnew/3.14.html)

## 今天交付

- [ ] 自己的实现、测试或实验记录；可放 `exercises/day48.py`，项目日继续同一个项目。
- [ ] 正确性/边界说明；算法题附时间与空间复杂度。
- [ ] 两道口述题的自己的回答；不会的地方明确标记。
- [ ] 更新 [进度表](../PROGRESS.md) 和 [错题本](../MISTAKES.md)。
