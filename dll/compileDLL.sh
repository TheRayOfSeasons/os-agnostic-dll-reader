#!/bin/bash

gcc -c HelloWorld.c
gcc -shared -o HelloWorld.dll HelloWorld.o
