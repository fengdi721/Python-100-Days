# Day 06 · 异常、文件与最小测试

第 1 周 · 每天 60–90 分钟 · [返回目录](../DAILY_INDEX.md)

## 今日知识

try/except/else/finally、raise from、自定义异常、with、Path、JSON、unittest。

## 主练习（约30–40分钟）

实现 load_settings(path)：读取 UTF-8 JSON，要求顶层是字典且 port 是 1..65535 的非布尔整数；将读取、JSON 和配置校验错误包装为 ConfigError，并保留 cause。

## 验收标准

用临时目录测试正常配置、缺失文件、坏 JSON、顶层列表、非法端口；没有裸 except；异常路径也关闭文件。

除题目另有规定，写出正常、空输入、边界/非法输入的测试。说明你的接口约定，不要为了通过一个样例硬编码。

## 短练习 / 易错点（约10–15分钟）

预测 try 中 return、finally 中 return 同时存在时的结果，并删掉 finally 的 return；解释为什么生产代码应避免这种写法。

## 面试口述（约10分钟）

什么时候捕获异常、什么时候继续向上传递？with 比手写 close 好在哪里？

先闭卷回答，再查 [面试要点](../INTERVIEW_REVIEW.md)。每个回答至少一个最小例子和一个适用边界。

<details>
<summary>卡住20分钟后再看提示</summary>

捕获具体的 OSError/JSONDecodeError；用 raise ConfigError(...) from exc 保留上下文。

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

- [ ] 自己的实现、测试或实验记录；可放 `exercises/day06.py`，项目日继续同一个项目。
- [ ] 正确性/边界说明；算法题附时间与空间复杂度。
- [ ] 两道口述题的自己的回答；不会的地方明确标记。
- [ ] 更新 [进度表](../PROGRESS.md) 和 [错题本](../MISTAKES.md)。
