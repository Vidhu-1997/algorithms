cmake_minimum_required(VERSION 3.30.1)

project(MyProject)

add_executable(myexample ./*.c)
message(STATUS "CMAKE_C_COMPILER: ${CMAKE_C_COMPILER}")
message(STATUS "CMAKE_CXX_COMPILER: ${CMAKE_CXX_COMPILER}")
