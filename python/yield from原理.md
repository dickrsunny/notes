- 一个例子
```python
from collections import namedtuple

Result = namedtuple('Result', 'count average')


# the subgenerator
def averager():  # 1
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield  # 2
        if term is None:  # 3
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)  # 4


# the delegating generator
def grouper(results, key):  # 5
    #  while True:  # 6
        # results[key] = yield from averager() # 7

    _i = iter(averager())  # 1

    try:
        _y = next(_i)  # 2
    except StopIteration as _e:
        _r = _e.value  # 3
    else:
        while 1:  # 4
            _s = yield _y  # 5
            try:
                _y = _i.send(_s)  # 6
            except StopIteration as _e:  # 7
                _r = _e.value
                break

    results[key] = _r


#  the client code, a.k.a. the caller
def main(data):  # 8
    results = {}
    for key, values in data.items():
        group = grouper(results, key)  # 9
        next(group)  # 10
        for value in values:
            group.send(value)  # 10

        try:
            group.send(None)  # important! # 12
        except StopIteration:
            pass

    # print(results)  # uncomment to debug
    report(results)


# output report
def report(results):
    for key, result in sorted(results.items()):
        group, unit = key.split(';')
        print('{:2} {:5} averaging {:.2f}{}'.format(result.count, group,
                                                    result.average, unit))


data = {
    'girls;kg': [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
    'girls;m': [1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
    'boys;kg': [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
    'boys;m': [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46],
}

if __name__ == '__main__':
    main(data)
```
- yield from 等价代码
``` python
# BEGIN YIELD_FROM_EXPANSION
_i = iter(EXPR)  # <1>
try:
    _y = next(_i)  # <2>
except StopIteration as _e:
    _r = _e.value  # <3>
else:
    while 1:  # <4>
        try:
            _s = yield _y  # <5>
        except GeneratorExit as _e:  # <6>
            try:
                _m = _i.close
            except AttributeError:
                pass
            else:
                _m()
            raise _e
        except BaseException as _e:  # <7>
            _x = sys.exc_info()
            try:
                _m = _i.throw
            except AttributeError:
                raise _e
            else:  # <8>
                try:
                    _y = _m(*_x)
                except StopIteration as _e:
                    _r = _e.value
                    break
        else:  # <9>
            try:  # <10>
                if _s is None:  # <11>
                    _y = next(_i)
                else:
                    _y = _i.send(_s)
            except StopIteration as _e:  # <12>
                _r = _e.value
                break

RESULT = _r  # <13>
# END YIELD_FROM_EXPANSION
```
  - 简化版
``` python
# BEGIN YIELD_FROM_EXPANSION_SIMPLIFIED
_i = iter(EXPR)  # <1>
try:
    _y = next(_i)  # <2>
except StopIteration as _e:
    _r = _e.value  # <3>
else:
    while 1:  # <4>
        _s = yield _y  # <5>
        try:
            _y = _i.send(_s)  # <6>
        except StopIteration as _e:  # <7>
            _r = _e.value
            break

RESULT = _r  # <8>
# END YIELD_FROM_EXPANSION_SIMPLIFIED
```

