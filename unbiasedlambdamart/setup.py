from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize


exts = [
    Extension(
        name="lambdaobj",
        sources=["lambdaobj.pyx"],
        libraries=["argsort"],
        library_dirs=["."],
        extra_compile_args=["-fopenmp", "-I/usr/lib/gcc/x86_64-linux-gnu/9/include/"],
        extra_link_args=["-lstdc++", "-fopenmp", "-L/usr/lib/gcc/x86_64-linux-gnu/9/include"],
        language="c++"
    )
]

setup(ext_modules=cythonize(exts, language_level="3"))