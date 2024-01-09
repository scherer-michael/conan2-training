from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMake, cmake_layout
from conan.tools.scm import Git
from conan.tools.build import check_max_cppstd, check_min_cppstd


class trainingRecipe(ConanFile):
    name = "training"
    version = "1.0"
    package_type = "application"

    # Optional metadata
    license = "MIT"
    author = "Michael Scherer <ms@mscherer.eu>"
    url = "https://github.com/scherer-michael/conan2-training"
    description = "Long description of the training repo"
    topics = ("tag1", "tag2", "tag3")

    # Binary configuration
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    
    exports_sources = "CMakeLists.txt", "src/*", "tests/*"

    def requirements(self):
        self.requires("spdlog/1.12.0")

        self.test_requires("gtest/1.13.0")

    def build_requirements(self):
        self.tool_requires("cmake/[^3]")

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()
        cmake.ctest()

    def package(self):
        cmake = CMake(self)
        cmake.install()
