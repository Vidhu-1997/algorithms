cmake_minimum_required(VERSION 3.30.1)

project(MyProject)

set(CMAKE_C_COMPILER "C:/MinGW/bin/gcc.exe")
set(CMAKE_CXX_COMPILER "C:/MinGW/bin/g++.exe")

set(CMAKE_GENERATOR "MinGW Makefiles")

add_executable(myexample ./*.c)

