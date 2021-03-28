:date: 2020-03-26 07:00:23

:title: C++ and CMake

:author: SergeM

:slug: cpp-and-cmake

:tags: c++, cpp, cmake, conan, gtest, catch2, testing, example, pybind11


CMake in VSCode
===============================

VSCode is a free open source IDE with a lot of nice features. In addition one can chose from a variety of extensions.
Looks like Cmake-tools kind of works, but
the hotkeys and some settings are far from intuitive.

In my previous attempt I ended up removing ``cmake tools`` plugin and moving forward with custom task.json and launch.json scripts.
Here is a template I made back then.
`https://github.com/serge-m/vscode_cmake_template <https://github.com/serge-m/vscode_cmake_template>`_.

Recently I managed to make it more of less convenient (maybe some updates played a role here as well).
Here are some settings I needed to make it usable and comparable to CLion.


Separate build directory per build type
-------------------------------------------

If you have only one directory for your build
you will need to rebuild everything when you switch between debug and release.
In order to have a `separate build directory <https://github.com/microsoft/vscode-cmake-tools/issues/151>`_
per build type (Debug/Release) add the following to your `settings.json`:

    "cmake.buildDirectory": "${workspaceRoot}/build-${buildType}"

By default VSCode and CmakeTools use ninja as a generator for cmake. Often one need to use make. Add

    "cmake.generator": "Unix Makefiles"

to switch from ninja to make.

Debugging settings
-----------------------------

In launch.json update "program" parameter:

    "program": "${command:cmake.launchTargetPath}",

Cmake Tools will substitute the corresponding path.
(from `docs of CmakeTools <https://vector-of-bool.github.io/docs/vscode-cmake-tools/debugging.html#debugging-with-cmake-tools-and-launch-json>`_)


Configure cmake settings
------------------------------------

add `cmake.configureSettings <https://vector-of-bool.github.io/docs/vscode-cmake-tools/settings.html#cmake-configuresettings>`_ to `settings.json`:

     "cmake.configureSettings": {
        "USE_MYMATH": "ON"
    }





Getting started with Gtest
=====================================

For any decent project in Cpp it's good to set up testing system. For C++ the standard solution is to use Gtest.

Installing Gtest in your ubuntu is not very straightforward. You have to install the package containing source code and then compile it with cmake with sudo rights.

.. code-block:: none

    sudo apt-get install libgtest-dev
    sudo apt-get install cmake # install cmake
    cd /usr/src/gtest
    sudo cmake CMakeLists.txt
    sudo make

    # copy or symlink libgtest.a and libgtest_main.a to your /usr/lib folder
    sudo cp *.a /usr/lib


Many projects use alternative approach. They clone GTest sources from github into the source tree of the project and compile it in-place.
That requires some custom scripting in your cmake files.

See also:
---------------------------------------

* `Getting started with Google Test (GTest) on Ubuntu <https://www.eriksmistad.no/getting-started-with-google-test-on-ubuntu/>`_




Handling dependencies in CMake
=====================================================

If i need to import a compiled 3rdparty library to my cmake project:

.. code-block:: none

    add_library(some_library SHARED IMPORTED)
    set_property(TARGET some_library PROPERTY IMPORTED_LOCATION "${CMAKE_CURRENT_SOURCE_DIR}/lib/some_library.so")
    set_property(TARGET some_library PROPERTY INTERFACE_INCLUDE_DIRECTORIES "${CMAKE_CURRENT_SOURCE_DIR}/include/")



CMake with Conan and Catch2
=====================================================

Here is a sample CMake project that uses Conan for dependency management and Catch2 for testing:

`tst_conan <https://github.com/serge-m/code-training/tree/master/cpp/tst_conan>`_


Python bindings for C++ code
=============================================


`Hybrid Python/C++ packages, revisited <https://www.benjack.io/2018/02/02/python-cpp-revisited.html>`_. an approach
using pybind11 and cmake.
