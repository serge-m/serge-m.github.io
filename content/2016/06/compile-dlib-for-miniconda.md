Title: compile dlib for miniconda
Author: SergeM
Date: 2016-06-25 22:43:00
Slug: compile-dlib-for-miniconda
Tags: 

Activate miniconda environment (my environment is called py3):
```bash
source activate py3
```

Produce initial steps from the readme:

```bash
cd examples
mkdir build
cd build
cmake ..
cmake --build . --config Release
```

inside function  `build_dlib()` of file `setup.py` add the highlighted code:
```python
if platform_arch == '64bit' and sys.platform == "win32":
    # 64bit build on Windows

#.................. bla bla ...................

    for ext in [py_ver.replace(".", "") + '.lib', py_ver + 'mu.lib', py_ver + 'm.lib', py_ver + 'u.lib']:
        py_lib = os.path.abspath(os.path.join(inc_dir, '../libs/', 'python' + ext))
        if os.path.exists(py_lib):
            cmake_extra_arch += ['-DPYTHON_LIBRARY={lib}'.format(lib=py_lib)]
            break
else:
    cmake_extra_arch += ['-DPYTHON_LIBRARY=/home/user/miniconda/envs/py3/lib/libpython3.so']
    cmake_extra_arch += ['-DPYTHON_INCLUDE_DIR=/home/user/miniconda/envs/py3/include/python3.5m']


build_dir = os.path.join(script_dir, "./tools/python/build")
#......................bla bla.....................................
```

Replace `/home/user/miniconda` by your path to miniconda

Run `python setup.py install` (as usual)
