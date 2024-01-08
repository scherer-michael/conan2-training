#include "../../src/my_class.h"

#include <gtest/gtest.h>

namespace
{
    TEST(TrainingTest, BasicConstructor)
    {
        MyClass myClass;
        EXPECT_EQ(0, myClass.member());
        EXPECT_NE(5, myClass.member());
    }
}