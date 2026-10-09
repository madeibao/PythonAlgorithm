# -*- coding: utf-8 -*-
# @Author: Mayuan
# @Time: 2026/10/9/星期五 17:43
# @File: optionaldemo


from typing import Optional

def find_user(user_id: int) -> Optional[str]:
    """根据 id 查找用户名，找不到返回 None"""
    users = {1: "Alice", 2: "Bob"}
    return users.get(user_id)

if __name__ == '__main__':
    print(find_user(1))   # Alice
    print(find_user(99))  # None