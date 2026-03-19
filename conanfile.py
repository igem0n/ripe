from conan import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain, CMakeDeps, cmake_layout
import os

class ripe(ConanFile):
    name = "ripe"
    version = "4.2.2"
    settings = "os", "arch", "compiler", "build_type"
    exports_sources = "CMakeLists.txt", "src/*", "include/*", "test/*", "lib/*"

    options = {
        "shared": [True, False],
        "fPIC": [True, False],
        "with_executable": [True, False]
    }

    default_options = {
        "shared": False,
        "fPIC": True,
        "with_executable": False
    }
    
    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def configure(self):
        if self.options.shared:
            self.options.rm_safe("fPIC")
        
    def requirements(self):
        self.requires("cryptopp/8.2.0")
        self.requires("cryptopp-pem/8.2.0")
        self.requires("zlib/1.3.1")

    def build_requirements(self):
        self.test_requires("easyloggingpp/9.97.1")
        self.test_requires("gtest/1.17.0")
        
    def generate(self):
        tc = CMakeToolchain(self)
        tc.cache_variables["BUILD_EXCUTABLE"] = self.options.with_executable
        tc.generate()
        deps = CMakeDeps(self)
        deps.generate()

    def layout(self):
        cmake_layout(self)

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["ripe"]

