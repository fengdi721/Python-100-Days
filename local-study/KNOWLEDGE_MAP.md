# Python 核心语法与知识覆盖表

“核心”要求能写、能解释、能用反例证明；“阅读”要求能认出、查证、评估是否需要。学完对应日期后，在进度表记录掌握程度。

| 类别 | 必须掌握的范围 | 对应日 |
|---|---|---|
| 词法与结构 | 缩进、注释、字符串转义、多行、命名与关键字、表达式/语句、PEP 8 | 01–04 |
| 对象语义 | 名称绑定、身份/值、可变/不可变、truthiness、None、别名 | 01、05、19 |
| 内置类型 | bool/int/float/complex（了解）、str/bytes/bytearray、list/tuple/dict/set/frozenset、range | 01–03、22 |
| 运算符 | 算术、整除/取模、比较链、逻辑短路、成员/身份、位运算、优先级、增强赋值 | 02–04 |
| 序列操作 | 索引、正负切片、解包、星号解包、排序、可哈希性 | 03、05、16 |
| 控制流 | if/elif/else、条件表达式、for/while、break/continue/pass、循环else、match/case/guard | 04 |
| 推导式 | list/set/dict推导式、生成器表达式、嵌套、作用域、:= | 04、08、10 |
| 函数 | def/return、默认值、参数种类、*args/**kwargs、lambda、高阶函数、文档字符串 | 05、08–09 |
| 作用域 | LEGB、global/nonlocal、闭包晚绑定、导入命名空间 | 08、12 |
| 异常 | try/except/else/finally、raise/from、自定义异常、assert（调试用）、ExceptionGroup/except* | 06、38 |
| 资源管理 | with/as、__enter__/__exit__、contextmanager、ExitStack、async with | 06、11、39 |
| 迭代 | iterable/iterator、iter/next、StopIteration、yield/yield from；send/throw/close（阅读） | 10、14、39 |
| 模块和包 | import/from/as、__name__/__main__、相对导入、sys.path、缓存、循环导入 | 12、44 |
| 面向对象 | class、属性、实例/类/静态方法、继承、super/MRO、ABC与组合 | 15–18 |
| 数据模型 | repr/str、len/iter/contains/getitem、eq/hash、NotImplemented、property/描述符 | 16–19 |
| 生命周期 | del/引用、copy/deepcopy、GC/weakref、slots、CPython与语言保证的区别 | 19–20、46 |
| 高级机制 | __new__/__init__、__getattr__/__getattribute__、类装饰器、__init_subclass__；元类（阅读） | 48 |
| 类型 | 容器泛型、联合、Optional、Callable、TypedDict、Protocol、Literal、TypeVar、Generic/type语句 | 13、45 |
| 输入输出 | Path/open/encoding、文本/二进制、JSON/CSV、序列化的信任边界 | 06、24 |
| 常用标准库 | collections/itertools/functools、re、datetime/zoneinfo、decimal、enum、logging、argparse、sqlite3、subprocess | 22–28 |
| 算法 | 哈希、双指针、窗口、栈队列、BFS/DFS、二分、堆、回溯、DP、排序复杂度 | 29–35、55 |
| 并发 | threading/锁、concurrent.futures、multiprocessing、GIL、free-threaded区别 | 36、40–41 |
| 异步 | async def/await、Task、event loop、TaskGroup、取消/超时、Queue、async for/with | 37–42 |
| 工程 | 测试/fixture/mock、虚拟环境、打包依赖、静态检查、性能测量、输入验证 | 43–49 |
| 版本意识 | 3.10 match、3.11异常组/TaskGroup、3.12泛型/type、3.14 t-string/注解求值 | 04、13、38、48 |

## 语法查漏短题（在相应日的90分钟版本中选做）

1. D02：创建 complex，查看 real/imag；修改 bytearray，解释 bytes 的不可变性。
2. D03：用 `(a,b)=(b,a)` 交换变量；删除 dict 中一个键；解释 del 与 pop 的区别。
3. D04：用条件表达式改写一个简单 if；写带两个 for 的推导式，并说明何时普通循环更清晰。
4. D06：写 assert 做内部不变量检查，再用 `python -O` 验证其可能被移除，解释为什么不能用于外部输入安全校验。
5. D10：用生成器 send 接收值，调用 close，观察 finally；throw 只需阅读和最小验证。
6. D13：在3.12+写 `type UserId = int` 与泛型别名，并说明别名不等于运行时新类型。
7. D16：说明对象的 `__bool__` 与 `__len__` 如何影响真值；写一个 `__call__` 可调用实例。
8. D24：解释 pickle 不可信数据为何可能执行代码；交换外部数据优先用可验证的格式。
9. D48：解释 Ellipsis (`...`) 作为占位与真正函数实现的区别；比较注解查看API在当前版本的行为。

可查 [完整语言参考](https://docs.python.org/3.14/reference/index.html)；不要求背完整标准库。C API、字节码/JIT实现、元类框架设计、Django/FastAPI全栈、NumPy/Pandas与机器学习属于后续专门路线。
