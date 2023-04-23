#!/usr/bin/env python3
"""test_utils module
"""
import unittest
import requests
from unittest.mock import patch
from parameterized import parameterized
access_nested_map = __import__('utils').access_nested_map
from utils import get_json


#class TestAccessNestedMap(unittest.TestCase):
#    """An access_nested_map function test class"""
#    @parameterized.expand([
#        ({"a": 1}, ("a",), 1),
#        ({"a": {"b": 2}}, ("a",), {"b": 2}),
#        ({"a": {"b": 2}}, ("a", "b"), 2),
#        ({}, ("a",), "KeyError: 'a'"),
#        ({"a": 1}, ("a", "b"), "KeyError: 'b'"),
#    ])
#    def test_access_nested_map(self, nested_map, path, expected):
#        """Test to access nested map with key path.
#        Parameters
#        ----------
#            nested_map: A nested map
#            path: A sequence of key representing a path to the value
#            expected: Expected result from the function
#        """
#        self.assertEqual(access_nested_map(nested_map, path), expected)

#    def test_access_nested_map_exception(self, nested_map, path):
#        """Test to access nested map with key path.
#        Parameters
#        ----------
#            nested_map: A nested map
#            path: A sequence of key representing a path to the value
#            expected: Expected result from the function
#        """
#        with self.assertRaises(KeyError):
#           access_nested_map(nested_map, path)

class TestGetJson(unittest.TestCase):
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    def test_get_json(self, test_url, expected):
        with patch('utils.get_json') as mock:
            mock.get.return_value = expected
            assert get_json(test_url) == expected
