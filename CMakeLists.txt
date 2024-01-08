cmake_minimum_required(VERSION 3.15)
project(training CXX)

find_package(spdlog REQUIRED)

add_executable(${PROJECT_NAME}
    src/my_class.h
    src/my_class.cpp
    src/main.cpp
)

target_link_libraries(${PROJECT_NAME}
    PRIVATE
        spdlog::spdlog
)

enable_testing()
add_subdirectory(tests)

install(training)
