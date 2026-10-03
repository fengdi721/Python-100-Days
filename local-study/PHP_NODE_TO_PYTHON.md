# PHP / Node.js → Python：优先改掉的直觉

这里比较的是常见语义，不把所有语言版本和特殊对象行为混为一谈。最有效的学法是为每一行写一个可运行反例。

| 已有经验 | Python 中需要重新确认 | 对应日 |
|---|---|---|
| PHP array 同时承担列表与映射 | 明确选择 list、dict、set；索引列表与按键映射分开 | 03 |
| PHP 数组值语义/写时复制经验 | Python list/dict 赋值形成别名，不会自动复制外层 | 01、19 |
| JavaScript 对象比较经验 | Python == 可按值比较或由 __eq__ 定制；is 才是身份比较 | 01、19 |
| PHP 中字符串 '0' 为假 | Python 非空字符串 '0' 为真；空 list/dict 则为假，和 JS 空数组/对象不同 | 02 |
| JS 默认参数每次调用求值 | Python 默认参数在函数定义执行时求值，可能共享可变对象 | 05 |
| JS const 的直觉 | Python 通常没有相同的局部常量声明；不可变对象也不等于名称不能重新绑定 | 01 |
| JS let 与循环闭包经验 | Python 闭包可能共享同一外层循环绑定，需显式冻结当前值 | 08 |
| Promise 与 async/await | Python 调用 async def 先得到 coroutine，需要 await 或调度；不能把调用视为已启动 | 37 |
| Node 事件循环经验 | 阻塞 I/O 同样会卡住协程调度；await 本身不保证 CPU 并行 | 36–37 |
| PHP/JS 类体系 | Python 广泛使用协议与鸭子类型；多继承、MRO、描述符需要专门理解 | 16–18 |
| 私有属性的经验 | 前导下划线主要是约定；双下划线名称改写不是安全隔离 | 15–18 |
| TypeScript/PHP 类型经验 | Python 标注通常不强制运行时验证；外部数据仍需校验 | 13、45 |
| npm/composer 工作流 | 区分解释器、venv、安装工具、pyproject声明、构建后端与锁文件 | 44 |
| finally 的直觉 | Python finally 中 return 会压过之前返回/异常；资源管理优先 with | 06、11 |
| 所有并发都类比 Promise.all | 明确 TaskGroup/gather 的失败策略、取消传播、队列背压与线程同步 | 38–42 |

附加口述：Python 浮点与 JavaScript Number 都有二进制浮点表示问题，但 Python int 不受固定64位整型范围限制（受可用资源约束）。金额练习用 Decimal 并明确舍入规则，不仅是把显示格式改成两位小数。
