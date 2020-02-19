cmake_minimum_required(VERSION 3.8)

project(TestCode)

set(CMAKE_C_STANDARD 99)
set(CMAKE_CXX_STANDARD 11)

set(CMAKE_BUILD_TYPE Debug)

add_subdirectory(googletest)
include_directories(googlemock/include googletest/include)

enable_testing()

set(TEST_SOURCES
    main.cpp
    testcases.cpp
    TestCode.c
)
set(TEST_HEADERS
    TestCode.h
)

add_executable(TestCode ${TEST_SOURCES})
target_link_libraries(TestCode
    gmock_main
)