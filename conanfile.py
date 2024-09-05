import os
from conan import ConanFile
from conan.tools.cmake import CMakeToolchain, CMakeDeps, cmake_layout
from conan.tools.files import copy
from conan.tools.scm import Git


class PackageConan(ConanFile):
    name = "qtils"
    version = "0.0.4"
    license = "MIT"
    settings = "os", "compiler", "build_type", "arch"
    url = "https://github.com/simbahebinbo/conan-qtils.git"
    require = {
        "boost/1.84.0",
        "fmt/10.1.1"
    }

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()
        deps = CMakeDeps(self)
        deps.generate()

    def source(self):
        git = Git(self)
        if not os.path.exists(os.path.join(self.source_folder, ".git")):
            git.clone("https://github.com/simbahebinbo/qtils.git", target=".")
        else:
            self.run("git pull")

        branch_name = "develop"
        git.checkout(branch_name)

    def build(self):
        # 只有头文件，没有需要编译的源文件，因此跳过 build 步骤
        pass

    def package(self):
        # 将头文件安装到包的 include 目录中
        include_folder = os.path.join(self.source_folder, "src")
        copy(self, "*.hpp", dst=os.path.join(self.package_folder, "include"), src=include_folder, keep_path=True)

    def package_info(self):
        # 只有头文件，没有库文件需要链接
        self.cpp_info.libdirs = []  # 清空 libdirs 避免找不到库的错误
        self.cpp_info.libs = []  # 没有库文件
        self.cpp_info.includedirs = ["include"]  # 指定头文件目录
