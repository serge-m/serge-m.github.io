:date: 2020-03-26 07:00:23

:title: C++ and CMake

:author: SergeM

:slug: cpp-and-cmake

:tags: c++, cpp, cmake


CMake in VSCode
===============================


VSCode is a free open source IDE with a lot of nice features. In addition one can chose from a variety of extensions.
I couldnt find a good extension for CMake integration that works out of box. I tried to make use of Cmake-tools and it kind of works, but
the hotkeys and some settings are far from intuitive now (2020-03).

Therefore I ended up removing ``cmake tools`` plugin and moving forward with custom taks.json and launch.json scripts.

Here is my VSCode+Cmake template for small projects:
`https://github.com/serge-m/vscode_cmake_template <https://github.com/serge-m/vscode_cmake_template>`_.



Getting strted with Gtest
=====================================

For any decent project in Cpp it's good to set up testing system. For C++ the standard solution is to use Gtest.

Installing Gtest in your ubuntu is not very straightforward. You have to install the package containing source code and then compile it with cmake with sudo rights.

.. code-block::
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
===============================

* `Getting started with Google Test (GTest) on Ubuntu <https://www.eriksmistad.no/getting-started-with-google-test-on-ubuntu/>`_

