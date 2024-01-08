#include "my_class.h"

#include <spdlog/spdlog.h>

void MyClass::print() const
{
    SPDLOG_INFO("MyClass Info Level log. member_ = {}", member_);
}

int MyClass::member() const
{
    SPDLOG_INFO("MyClass custom member getter. member_ = {}", member_);
    return member_;
}

MyClass::MyClass(int argument): member_(argument)
{
    SPDLOG_INFO("MyClass custom constructor. member_ = {}", member_);
}