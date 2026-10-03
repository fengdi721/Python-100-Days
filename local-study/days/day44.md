# Day 44 · 工程结构、依赖与打包

第 7 周 · 每天 60–90 分钟 · [返回目录](../DAILY_INDEX.md)

## 今日知识

venv、python -m pip、pyproject.toml、src layout、构建后端、锁定依赖、入口。

## 主练习（约30–40分钟）

把 logtool 整理为独立小包，编写 pyproject.toml 和命令入口；在隔离环境本地安装并从仓库外目录调用 --help。

## 验收标准

声明 requires-python；包可导入；测试可运行；README 有最短启动步骤；不发布到 PyPI。

除题目另有规定，写出正常、空输入、边界/非法输入的测试。说明你的接口约定，不要为了通过一个样例硬编码。

## 短练习 / 易错点（约10–15分钟）

解释运行依赖、开发依赖、版本约束、锁文件的区别；比较 python -m pip 与裸 pip。

## 面试口述（约10分钟）

虚拟环境隔离的是哪些内容？为什么在项目目录内能 import 不代表安装包完整？

先闭卷回答，再查 [面试要点](../INTERVIEW_REVIEW.md)。每个回答至少一个最小例子和一个适用边界。

<details>
<summary>卡住20分钟后再看提示</summary>

遵循 PyPA 官方打包教程；已有工具即可，无需为了课程安装多个包管理器。

</details>

## 阅读入口（约10–15分钟）

以下为本周参考池。只查当天知识对应的小节，不需要每天重读全部章节；涉及现代版本时优先看官方文档。

- [主教材：96.软件测试和自动化测试](../../Day91-100/96.%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%92%8C%E8%87%AA%E5%8A%A8%E5%8C%96%E6%B5%8B%E8%AF%95.md)
- [主教材：99.面试中的公共问题](../../Day91-100/99.%E9%9D%A2%E8%AF%95%E4%B8%AD%E7%9A%84%E5%85%AC%E5%85%B1%E9%97%AE%E9%A2%98.md)
- [PyPA：打包指南](https://packaging.python.org/en/latest/tutorials/packaging-projects/)
- [官方：unittest](https://docs.python.org/3.14/library/unittest.html)
- [官方：3.14变化](https://docs.python.org/3.14/whatsnew/3.14.html)

## 今天交付

- [ ] 自己的实现、测试或实验记录；可放 `exercises/day44.py`，项目日继续同一个项目。
- [ ] 正确性/边界说明；算法题附时间与空间复杂度。
- [ ] 两道口述题的自己的回答；不会的地方明确标记。
- [ ] 更新 [进度表](../PROGRESS.md) 和 [错题本](../MISTAKES.md)。
