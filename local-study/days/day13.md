# Day 13 · 类型标注与现代泛型

第 2 周 · 每天 60–90 分钟 · [返回目录](../DAILY_INDEX.md)

## 今日知识

list[str]、X|None、TypedDict、Protocol、TypeVar/泛型、Callable、运行时验证边界。

## 主练习（约30–40分钟）

实现 `first_match[T](items: Iterable[T], predicate: Callable[[T], bool]) -> T | None`；为日志记录定义 TypedDict；为统计函数添加类型标注。

## 验收标准

整数与字符串输入保持返回类型；空输入/无匹配返回 None；实现接受生成器；用静态检查器验证或手工列出三个会被检查器拒绝的调用。

除题目另有规定，写出正常、空输入、边界/非法输入的测试。说明你的接口约定，不要为了通过一个样例硬编码。

## 短练习 / 易错点（约10–15分钟）

给 age:int 赋字符串并实际运行，解释为何标注不等于运行时校验；写 Literal 状态与 match 处理。

## 面试口述（约10分钟）

Any 和 object 有何不同？Protocol 与继承某个具体基类有什么区别？

先闭卷回答，再查 [面试要点](../INTERVIEW_REVIEW.md)。每个回答至少一个最小例子和一个适用边界。

<details>
<summary>卡住20分钟后再看提示</summary>

先把函数参数写成行为接口 Iterable，不要无必要要求 list。

</details>

## 阅读入口（约10–15分钟）

以下为本周参考池。只查当天知识对应的小节，不需要每天重读全部章节；涉及现代版本时优先看官方文档。

- [主教材：16.函数使用进阶](../../Day01-20/16.%E5%87%BD%E6%95%B0%E4%BD%BF%E7%94%A8%E8%BF%9B%E9%98%B6.md)
- [主教材：17.函数高级应用](../../Day01-20/17.%E5%87%BD%E6%95%B0%E9%AB%98%E7%BA%A7%E5%BA%94%E7%94%A8.md)
- [主教材：31.Python语言进阶](../../Day31-35/31.Python%E8%AF%AD%E8%A8%80%E8%BF%9B%E9%98%B6.md)
- [官方：模块](https://docs.python.org/3.14/tutorial/modules.html)
- [官方：typing](https://docs.python.org/3.14/library/typing.html)
- [官方：contextlib](https://docs.python.org/3.14/library/contextlib.html)

## 今天交付

- [ ] 自己的实现、测试或实验记录；可放 `exercises/day13.py`，项目日继续同一个项目。
- [ ] 正确性/边界说明；算法题附时间与空间复杂度。
- [ ] 两道口述题的自己的回答；不会的地方明确标记。
- [ ] 更新 [进度表](../PROGRESS.md) 和 [错题本](../MISTAKES.md)。
