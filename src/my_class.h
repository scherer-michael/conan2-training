#pragma once

class MyClass
{
    public:
        MyClass() = default;
        MyClass(int argument);
        void print() const;
        int member() const;

    private:
        int member_ = 0;
};
