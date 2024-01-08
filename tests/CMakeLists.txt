cmake_minimum_required(VERSION 3.15)
project(training_test CXX)

find_package(spdlog REQUIRED CONFIG)
find_package(GTest REQUIRED CONFIG)

add_executable(training_test
    unit/my_class_test.cpp
    "../src/my_class.cpp"
)

target_link_libraries(training_test
    PRIVATE
        spdlog::spdlog
        GTest::gtest
        GTest::gtest_main
)

include(GoogleTest)
gtest_discover_tests(training_test)
