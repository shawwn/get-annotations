# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['get_annotations']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'get-annotations',
    'version': '0.1.2',
    'description': "A backport of Python 3.10's inspect.get_annotation() function",
    'long_description': '# get-annotations\n\nA backport of Python 3.10\'s [`inspect.get_annotations()`](https://docs.python.org/3/library/inspect.html#inspect.get_annotations) function.\n\n## Install\n\n```\npip3 install -U get-annotations\n```\n\n## Usage\n\n```py\nfrom get_annotations import get_annotations\n\ndef foo(x: int) -> str: ...\n\nprint(get_annotations(foo))\n# {\'x\': <class \'int\'>, \'return\': <class \'str\'>}\n```\n\n\nIf your module uses `from __future__ import annotations`, you\'ll want to set `eval_str=True`, otherwise `get_annotations` will return strings:\n\n```py\nfrom __future__ import annotations\nimport typing as t\n\ndef bar(x: t.List[MyObject]): ...\n\nclass MyObject:\n  pass\n\nprint(get_annotations(bar))\n# {\'x\': \'t.List[MyObject]\'}\n\nprint(get_annotations(bar, eval_str=True))\n# {\'x\': typing.List[__main__.MyObject]}\n```\n\nNote that it does _not_ work with old-style forward ref annotations, such as `t.List["MyObject"]`:\n\n```py\n>>> from typing import List\n>>> def foo(a: int) -> List["MyObject"]: ...\n...\n>>> class MyObject: ...\n...\n>>> print(get_annotations(foo, eval_str=True)) # Note that \'MyObject\' is returned as a string!\n{\'a\': <class \'int\'>, \'return\': typing.List[ForwardRef(\'MyObject\')]}\n>>>\n>>> print(get_annotations(foo, eval_str=False)) # Identical\n{\'a\': <class \'int\'>, \'return\': typing.List[ForwardRef(\'MyObject\')]}\n```\n\n\nIf you _really_ don\'t want to use `from __future__ import annotations` for some reason, you can surround an entire type annotation in quotes to forward ref it:\n\n```py\n>>> def foo(a: int) -> "List[MyObject]": ...\n...\n>>> print(get_annotations(foo, eval_str=True)) # This works now\n{\'a\': <class \'int\'>, \'return\': typing.List[__main__.MyObject]}\n>>>\n>>> print(get_annotations(foo, eval_str=False)) # For comparison\n{\'a\': <class \'int\'>, \'return\': \'List[MyObject]\'}\n```\n\n\n## License\n\nMIT\n\n## Contact\n\nA library by [Shawn Presser](https://www.shawwn.com). If you found it useful, please consider [joining my patreon](https://www.patreon.com/shawwn)!\n\nMy Twitter DMs are always open; you should [send me one](https://twitter.com/theshawwn)! It\'s the best way to reach me, and I\'m always happy to hear from you.\n\n- Twitter: [@theshawwn](https://twitter.com/theshawwn)\n- Patreon: [https://www.patreon.com/shawwn](https://www.patreon.com/shawwn)\n- HN: [sillysaurusx](https://news.ycombinator.com/threads?id=sillysaurusx)\n- Website: [shawwn.com](https://www.shawwn.com)\n\n',
    'author': 'Shawn Presser',
    'author_email': 'None',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/shawwn/get-annotations',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
