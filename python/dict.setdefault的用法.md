

~~~python
my_dict.setdefault(key, []).append(new_value)
~~~
* 获取key的出现情况列表，如果key不存在，把key和一个空列表放进映射，然后返回 这个空列表，这样就能在不进行第二次查找的情况下更新列表了。

* 和
~~~python
if key not in my_dict:
         my_dict[key] = []
     my_dict[key].append(new_value)
~~~
* 二者的效果是一样的，只不过后者至少要进行两次键查询——如果键不存在的话，就是三次，用 setdefault 只需要一次就可以完成整个操作。
