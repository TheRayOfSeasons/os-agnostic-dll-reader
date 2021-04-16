# OS Agnostic DLL Reader

This is a barebones logic for an OS agnostic DLL reader for python.

# How to run

1. Install python. (preferably 3.8.0)
2. `cd` into the project directory.
3. Run `python run.py`.

# How to compile the DLL file.

Either run the `compileDLL.sh` bash script or run each command separately while inside the dll folder:

```bash
gcc -c HelloWorld.c
gcc -shared -o HelloWorld.dll HelloWorld.o
```

You must have `gcc` installed beforehand.
