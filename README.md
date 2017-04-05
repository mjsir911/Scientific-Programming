# Scientific Programming

A scientific programming course learning the concepts of python-- integrated
with pre-calculus 

## What is this?

This project is developed on parallel to a
[repository](https://github.com/jelkner/ScientificProgramming) maintained and
developed by my teacher, [Jeff Elkner](https://github.com/jelkner).

This module is composed of four parts, all found in the src directory:

### Geometry

The [geometry.py](
https://github.com/mjsir911/Scientific-Programming/src/geometry.py) module
consists of various spacial objects & methods to help with more complex topics.

This module experiments with classes to a heavy extent, including features such
as object inheritance and overloading object creation.

### Gaussian Jordan

The [gaussjordan](
https://github.com/mjsir911/Scientific-Programming/src/gaussjordan) module
consists of a few files.

[tools.py](
https://github.com/mjsir911/Scientific-Programming/src/gaussjordan/tools.py)
has some methods and an class used for converting matrices into a reduced row
echelon form using Gaussian elimination. This object heavily relies on the
geometry module since it uses Vector and Matrix objects to simplify complex
mathematical procedures done on matrices.

### Matrices

The 
[matrices](https://github.com/mjsir911/Scientific-Programming/src/matrices)
module is mainly focussed around opening and converting a non-pythonic file to
a python object(in this case a matrix object).

It includes a file that is setup as a layout, [unaugmented.dat](
https://github.com/mjsir911/Scientific-Programming/src/matrices/unaugmented.dat),
which contains a matrix that has one set of solutions and is styled in a way as
to
pose a challenge to be converted to python(not really though).

The rules for the matrices dat files are as follows:
0. Multiple matrices may be separated by a `##`
0. The lines of a matrix are separated by a newline `\n`
0. Columns of a row are delimited by semicolons `;`

[dat2lit.py](
https://github.com/mjsir911/Scientific-Programming/src/matrices/unaugmented.dat)
contains two functions that do the exact same thing, currently undergoing
efficiency tests and trying to find out which one is preferable. Both functions
load a `.dat` file in the format previously mentioned and return a list of
matrix objects.

The ops.py file simply showcases the valid operations that can be done on a
matrix

### Dictionaries This module is simply a review on dictionaries.

## Setting up 

### Prerequisities

Built in python, so [python3](www.python.org)

### Running the tests

Testing is currently in development, but singular files
do have doctests so if you want to test anything just run

    python3 -m doctest <file>.py

and that will run the tests inside a specific file


## Built With

* ViM - Text editor

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available,
see the [tags on this
repository](https://github.com/mjsir911/Scientific-Programming/tags). 

## Authors

* **Marco Sirabella** - *Initial work* -
  [mjsir911](https://github.com/mjsir911)

## License

This project is licensed under the MIT License - see the
[LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* [Jeff Elkner](https://github.com/jelkner) for helping me refine my python
  skills
