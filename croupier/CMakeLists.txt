cmake_minimum_required(VERSION 3.2.2)
project(Bio)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++14")

include_directories(".")

set(SOURCE_FILES main.cpp Dice.cpp Croupier.cpp)
add_executable(Bio ${SOURCE_FILES})