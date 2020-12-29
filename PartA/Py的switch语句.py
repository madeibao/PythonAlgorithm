def switch_test_item(item):
    switcher = {
        "CPU": 0,
        "Memory":1,
        "BIOSVER":2,
        "FAN":3,
        "BIOSSETUP":4,
    }
    return switcher.get(item,None)


print(switch_test_item("CPU"))



# 0

#  字典的内容还可以转化成表达式的形式。


def debug(msg):
    print(msg)


def error(msg):
    print(msg)


def warning(msg):
    print(msg)


def other(msg):
    print(msg)


def notify_result(num, msg):
    numbers = {
        0: success,
        1: debug,
        2: warning,
        3: error
    }

    method = numbers.get(num, None)
    if method:
        method(msg)


if __name__ == "__main__":
    notify_result(0, "success")
    notify_result(1, "debug")
    notify_result(2, "warning")
    notify_result(3, "error")
    notify_result(4, "other")
