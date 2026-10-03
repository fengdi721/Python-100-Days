# 本地环境

本机核实：`/opt/homebrew/bin/python3.14` 为 Python 3.14.7；原终端默认 `python3` 为3.7.9。

学习目录：`/Users/fengdi/sources/python/learn-python/local-study`。

准备方式：使用已安装的3.14解释器创建本目录 `.venv`；不需要安装新的Python，也不需要全局切换版本。

```sh
cd ~/sources/python/learn-python/local-study
source .venv/bin/activate
python --version
python -m unittest discover -s tests -v
```

也可以不激活环境，直接运行：

```sh
~/sources/python/learn-python/local-study/.venv/bin/python -m unittest discover \
  -s ~/sources/python/learn-python/local-study/tests \
  -t ~/sources/python/learn-python/local-study
```

推荐先使用上面的 `cd` 方式。若课程文件复制到另一台电脑，不要复制 `.venv`，请用那台电脑的现代Python重新执行 `python3.14 -m venv .venv`。

第01天只有标准库依赖。其他天的第三方工具按需要安装在此环境内；本次不自动安装教程全部依赖。

Day 01 初始实现故意未完成。10项测试均因 `NotImplementedError` 报错属预期；你实现函数后应全部通过。测试框架已用独立的内存参考实现验证10项通过，参考答案未写入练习文件。
