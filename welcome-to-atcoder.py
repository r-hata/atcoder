# -*- coding: utf-8 -*-
"""
問題文
高橋君はデータの加工が行いたいです。
整数 a , b , cと、文字列 sが与えられます。
整数 a + b + cと、文字列 sを並べて表示しなさい。

入力
入力は以下の形式で与えられる。

a
b c
s

1行目は、整数 a (1 <= a <= 1,000) が与えられる。
2行目は、整数 b, c (1 <= b, c <= 1,000) が与えられる。
3行目は、文字列 s が与えられる。この文字列の長さは 1文字以上 100文字以下である。

出力
a + b + cと sを空白区切りで 1行に出力せよ。
"""

a = int(input())
b, c = (int(x) for x in input().split())
numbers = (a, b, c)
sumNumber = sum(numbers)
s = input()

print("{} {}".format(sumNumber, s))

