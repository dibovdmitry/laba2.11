#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def foo(t):
    def inner(s):
        if t == list:
            return list(map(int, s.split()))
        return tuple(map(int, s.split()))

    return inner


print(foo(list)('1 2 3 4'))
print(foo(tuple)('1 2 3 4 5'))
