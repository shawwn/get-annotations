# get-annotations

A backport of Python 3.10's `inspect.get_annotation()` function

## Install

```
pip3 install -U get-annotations
```

## Usage

```py
from get_annotations import get_annotations

def foo(x: int) -> str: ...

print(get_annotations(foo))
# {'x': <class 'int'>, 'return': <class 'str'>}
```


If your module uses `from __future__ import annotations`, you'll want to set `eval_str=True`, otherwise `get_annotations` will return strings:

```
from __future__ import annotations
import typing as t

def bar(x: t.List[MyObject]): ...

class MyObject:
  pass

print(get_annotations(bar))
# {'x': 't.List[MyObject]'}

print(get_annotations(bar, eval_str=True))
# {'x': typing.List[__main__.MyObject]}
```

Note that it does _not_ work with old-style forward ref annotations, such as `t.List["MyObject"]`:

```
>>> from typing import List
>>> def foo(a: int) -> List["MyObject"]: ...
...
>>> class MyObject: ...
...
>>> print(get_annotations(foo, eval_str=True)) # Note that 'MyObject' is returned as a string!
{'a': <class 'int'>, 'return': typing.List[ForwardRef('MyObject')]}
>>>
>>> print(get_annotations(foo, eval_str=False)) # Identical
{'a': <class 'int'>, 'return': typing.List[ForwardRef('MyObject')]}
```


If you _really_ don't want to use `from __future__ import annotations` for some reason, you can surround an entire type annotation in quotes to forward ref it:

```
>>> def foo(a: int) -> "List[MyObject]": ...
...
>>> print(get_annotations(foo, eval_str=True)) # This works now
{'a': <class 'int'>, 'return': typing.List[__main__.MyObject]}
>>>
>>> print(get_annotations(foo, eval_str=False)) # For comparison
{'a': <class 'int'>, 'return': 'List[MyObject]'}
```


## License

MIT

## Contact

A library by [Shawn Presser](https://www.shawwn.com). If you found it useful, please consider [joining my patreon](https://www.patreon.com/shawwn)!

My Twitter DMs are always open; you should [send me one](https://twitter.com/theshawwn)! It's the best way to reach me, and I'm always happy to hear from you.

- Twitter: [@theshawwn](https://twitter.com/theshawwn)
- Patreon: [https://www.patreon.com/shawwn](https://www.patreon.com/shawwn)
- HN: [sillysaurusx](https://news.ycombinator.com/threads?id=sillysaurusx)
- Website: [shawwn.com](https://www.shawwn.com)

