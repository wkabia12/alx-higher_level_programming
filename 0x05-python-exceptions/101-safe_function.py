#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return result
    except IndexError as ie:
        print("Exception: {}".format(ie), file=sys.stderr)
        return None
    except ZeroDivisionError as ze:
        print("Exception: {}".format(ze), file=sys.stderr)
        return None
    except TypeError as te:
        print("Exception: {}".format(te), file=sys.stderr)
        return None
    except NameError as ne:
        print("Exception: {}".format(ne), file=sys.stderr)
        return None
