# Day 04 · Python 控制流与推导式

第 1 周 · 每天 60–90 分钟 · [返回目录](../DAILY_INDEX.md)

## 今日知识

for/while、range、enumerate、zip、break/continue、循环 else、推导式、:=、match/case。

## 主练习（约30–40分钟）

实现 dispatch(command)：用 match 匹配字典命令 {op:add, a:int, b:int} 和 {op:echo, text:str}，分别返回和与文本；未知或类型不符抛 ValueError，布尔值不作为数字。

## 验收标准

覆盖两种正常命令、字段缺失、错误类型、未知操作与 True；给 add 增加 guard；允许无关额外字段。

除题目另有规定，写出正常、空输入、边界/非法输入的测试。说明你的接口约定，不要为了通过一个样例硬编码。

## 短练习 / 易错点（约10–15分钟）

用 for/else 判断列表是否含负数；再用 any 改写。写一个只调用一次解析函数的 := 过滤例子，并解释可读性取舍。

## 面试口述（约10分钟）

match 是 switch 的同义语法吗？循环 else 在什么情况下执行？

先闭卷回答，再查 [面试要点](../INTERVIEW_REVIEW.md)。每个回答至少一个最小例子和一个适用边界。

<details>
<summary>卡住20分钟后再看提示</summary>

mapping pattern 默认允许额外键；类型模式中的 int 也会匹配 bool，需要 guard。

</details>

## 阅读入口（约10–15分钟）

以下为本周参考池。只查当天知识对应的小节，不需要每天重读全部章节；涉及现代版本时优先看官方文档。

- [主教材：03.Python语言中的变量](../../Day01-20/03.Python%E8%AF%AD%E8%A8%80%E4%B8%AD%E7%9A%84%E5%8F%98%E9%87%8F.md)
- [主教材：04.Python语言中的运算符](../../Day01-20/04.Python%E8%AF%AD%E8%A8%80%E4%B8%AD%E7%9A%84%E8%BF%90%E7%AE%97%E7%AC%A6.md)
- [主教材：05.分支结构](../../Day01-20/05.%E5%88%86%E6%94%AF%E7%BB%93%E6%9E%84.md)
- [主教材：08.常用数据结构之列表-1](../../Day01-20/08.%E5%B8%B8%E7%94%A8%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84%E4%B9%8B%E5%88%97%E8%A1%A8-1.md)
- [主教材：13.常用数据结构之字典](../../Day01-20/13.%E5%B8%B8%E7%94%A8%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84%E4%B9%8B%E5%AD%97%E5%85%B8.md)
- [主教材：14.函数和模块](../../Day01-20/14.%E5%87%BD%E6%95%B0%E5%92%8C%E6%A8%A1%E5%9D%97.md)
- [主教材：21.文件读写和异常处理](../../Day21-30/21.%E6%96%87%E4%BB%B6%E8%AF%BB%E5%86%99%E5%92%8C%E5%BC%82%E5%B8%B8%E5%A4%84%E7%90%86.md)
- [官方：控制流与函数](https://docs.python.org/3.14/tutorial/controlflow.html)
- [官方：数据结构](https://docs.python.org/3.14/tutorial/datastructures.html)

## 今天交付

- [ ] 自己的实现、测试或实验记录；可放 `exercises/day04.py`，项目日继续同一个项目。
- [ ] 正确性/边界说明；算法题附时间与空间复杂度。
- [ ] 两道口述题的自己的回答；不会的地方明确标记。
- [ ] 更新 [进度表](../PROGRESS.md) 和 [错题本](../MISTAKES.md)。
