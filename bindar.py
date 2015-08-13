# coding: utf-8
# 自分の得意な言語で
# Let's チャレンジ！！
from __future__ import division
import math

def get_exist_page(position,one_page_num):
    return int(math.ceil(position/(one_page_num*2)))

def prev_last_num(one_page_num,now_page):
    return one_page_num * 2 * (now_page - 1)
    
def now_page_first_num(one_page_num,now_page):
    return prev_last_num(one_page_num,now_page) + 1

def page_to_page_distance(page,one_page_num,position):
    return page * one_page_num * 2 - position

n,m = map(int,raw_input().rstrip().split())
exist_page = get_exist_page(m,n)
print now_page_first_num(n,exist_page) +  page_to_page_distance(exist_page,n,m)