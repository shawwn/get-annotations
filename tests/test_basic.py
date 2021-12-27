from __future__ import annotations
import unittest
from get_annotations import get_annotations

from typing import List

def my_function(objs: List[MyObject]) -> int:
    return len(objs)

class TestCase(unittest.TestCase):
    def test_basic(self):
        notes = get_annotations(my_function)
        self.assertIn('objs', notes)
        self.assertIn('return', notes)
        self.assertEqual(notes['objs'], 'List[MyObject]')
        self.assertEqual(notes['return'], 'int')
        notes = get_annotations(my_function, eval_str=True)
        self.assertIn('objs', notes)
        self.assertIn('return', notes)
        self.assertIs(notes['return'], int)
        self.assertEqual(notes['objs']._name, 'List')
        self.assertEqual(len(notes['objs'].__args__), 1)
        self.assertIs(notes['objs'].__args__[0], MyObject)

class MyObject:
    pass

if __name__ == '__main__':
    unittest.main()
