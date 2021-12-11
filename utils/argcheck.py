#!/usr/bin/env python3
from typing import Tuple
"""Temporary arg check solution"""


def do_key_input_check(arg:str):
    args = arg.split()
    if len(args) != 2:
        print("Requires 2 inputs. key:str, interval:int")

    try:
        key, interval = args[0], int(args[1])
        return key, interval
    except:
        print("Interval needs to be an int.")

    return None, None

def do_craft_input_check(arg:str, macro_list:list):
    """Return: (str|None, str|None, int|None)"""
    args = arg.split()
    amt = None
    commands = ["list"]
    if len(args) < 1:
        print("Requires atleast 1 input. Use craft help for details.")
        return None, None, None

    # One of the commands
    if args[0] not in macro_list and args[0] in commands:
        command = args[0]
        return command, None, amt

    # Formatting
    if ".txt" not in args[0]:
        idx = macro_list.index((args[0] + ".txt"))
    else:
        idx = macro_list.index(args[0])

    # Optional: amt
    if len(args) == 2:
        try:
            amt = int(args[1])
        except:
            print("Amt needs to be an integer.")
            return None, None, None

    if idx:
        return "craft", macro_list[idx], amt

    print("Wrong input. Use craft help for details.")
    return None, None, amt
