#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def string():
    def sophia(a):
        a = list(map(int, input("Напишите строки через запятую: ").split()))
        print("<ol>\n<li>строка {count}</li>\n<li>строка {count}</li>\n</ol>")
    return sophia()


if __name__ == '__main__':
    strong = string(2)