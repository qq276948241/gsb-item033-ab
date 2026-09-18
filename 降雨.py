#!/usr/bin/env python3
# 按毫米降雨量报雨势。分级不要改。
import sys

缺数据 = "没法报雨：缺了降雨量\n"
负数错 = "没法报雨：降雨量不能是负的\n"
别的错 = "没法报雨：请给出一个不小于零的整数降雨量\n"


def 是非负整数字符(文本):
    if not 文本:
        return False
    for 字 in 文本:
        if 字 < "0" or 字 > "9":
            return False
    return True


def 是负整数字符(文本):
    if len(文本) < 2 or 文本[0] != "-":
        return False
    return 是非负整数字符(文本[1:])


def 报雨(参数):
    if len(参数) != 1 or 参数[0] == "" or 参数[0] == "缺":
        return 2, "", 缺数据
    文本 = 参数[0]
    if 是负整数字符(文本):
        return 2, "", 负数错
    if not 是非负整数字符(文本):
        return 2, "", 别的错
    量 = int(文本)
    if 量 <= 9:
        势 = "小雨"
    elif 量 <= 24:
        势 = "中雨"
    elif 量 <= 49:
        势 = "大雨"
    else:
        势 = "暴雨"
    return 0, 势 + "\n", ""


def 主程序(参数):
    码, 出, 错 = 报雨(参数)
    if 出:
        sys.stdout.write(出)
    if 错:
        sys.stderr.write(错)
    return 码


if __name__ == "__main__":
    raise SystemExit(主程序(sys.argv[1:]))
