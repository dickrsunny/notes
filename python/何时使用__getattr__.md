
属性查找失败后，解释器会调用 \_\_getattr__ 方法。简单来说，对 my_obj.x 表达式，Python 会检查 my_obj 实例有没有名为 x 的属性;如果没有，到类(my_obj.\_\_class__)中查找;如果 还没有，顺着继承树继续查找。如果依旧找不到，调用 my_obj 所属类中定义的 \_\_getattr__ 方法，传入 self 和属性名称的字符串形式(如 'x')。
