
- == 运算符比较两个对象的值(对象中保存的数据)，调用的是\_\_equal__方法；而 is 比较对象的标识（内存地址）,调用的是id方法。 
- 通常，我们关注的是值，而不是标识，因此 Python 代码中 == 出现的频率比 is 高。
- 然而，在变量和单例值之间比较时，应该使用 is。目前，最常使用 is 检查变量绑定的值 是不是 None。下面是推荐的写法:
    ~~~python
    x is None
    ~~~
- 否定的正确写法是:
    ~~~python
    x is not None
    ~~~
- is 运算符比 == 速度快，因为它不能重载，所以 Python 不用寻找并调用特殊方法，而是直 接比较两个整数ID。而a == b是语法糖，等同于a.\_\_eq__(b)。继承自object的\_\_eq__ 方法比较两个对象的 ID，结果与 is 一样。但是多数内置类型使用更有意义的方式覆盖了 \_\_eq__ 方法，会考虑对象属性的值。相等性测试可能涉及大量处理工作，例如，比较大型 集合或嵌套层级深的结构时。