- [setdefault](#setdefault)
- [defaultdict](#defaultdict)
- [\_\_missing__](#missing)
#### setdefault
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
#### defaultdict
* 在实例化一个 defaultdict 的时候，需要给构造方法提供一个可调用对象，这个可调用对象会在 \_\_getitem__ 碰到找不到的键的时候被调用，让 \_\_getitem__ 返回某种默认值。
* 比如，我们新建了这样一个字典:dd = defaultdict(list)，如果键'new-key'在dd中还 不存在的话，表达式 dd['new-key'] 会按照以下的步骤来行事。
  * (1) 调用 list() 来建立一个新列表。
  * (2) 把这个新列表作为值，'new-key' 作为它的键，放到 dd 中。 
  * (3) 返回这个列表的引用。
* 而这个用来生成默认值的可调用对象存放在名为 default_factory 的实例属性里。
* eg:
    ~~~python
    index = {}
    index[word].append(location)
    ~~~
  * 如果 index 并没有 word 的记录，那么 default_factory 会被调用，为查询不到的键创造一个值。这个值在这里是一个空的列表，然后这个空列表被赋值给 index[word]，继而被当作返回值返回，因此 .append(location) 操作总能成功。
#### \_\_missing__
* 所有的映射类型在处理找不到的键的时候，都会牵扯到 \_\_missing__ 方法。
* \_\_missing__ 方法只会被 \_\_getitem__ 调用(比如在表达式 d[k] 中)。提供 \_\_missing__ 方法对 get 或者 \_\_contains__(in 运算符会用到这个方法)这些 方法的使用没有影响。这也是我在上一节最后的警告中提到，defaultdict 中 的 default_factory 只对 \_\_getitem__ 有作用的原因。
