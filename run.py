import ctypes
import os
import pathlib


BASE_DIR = pathlib.Path(__file__).parent.absolute()

hello_world = ctypes.cdll.LoadLibrary(
    os.path.join(BASE_DIR, 'dll/HelloWorld.dll')
)
hello_value = hello_world.hello()
added_value = hello_world.add(1, 2)

# Test
assert val == 0 # Hello World is just printed into the console. 0 is returned.
assert added_val == 3

# Print into console for verification.
print(val)
print(added_val)
