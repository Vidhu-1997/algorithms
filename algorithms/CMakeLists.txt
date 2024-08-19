cmake_minimum_required(VERSION 3.30.1)

project(MyProject)

add_executable(myexample ./*.c)
cmake -G "MinGW Makefiles" -DCMAKE_C_COMPILER=C:/MinGW/bin/gcc.exe -DCMAKE_CXX_COMPILER=C:/MinGW/bin/g++.exe ..
message(STATUS "CMAKE_C_COMPILER: ${CMAKE_C_COMPILER}")
message(STATUS "CMAKE_CXX_COMPILER: ${CMAKE_CXX_COMPILER}")
