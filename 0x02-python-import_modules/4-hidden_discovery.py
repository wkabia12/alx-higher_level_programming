#!/usr/bin/python3
import inspect
import importlib.util

module_name = "hidden_4"
module_path = "."
spec = importlib.util.spec_from_file_location(module_name, module_path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

defines = inspect.getmembers(module, inspect.isfunction)
for name in defines:
    print(name[0])
