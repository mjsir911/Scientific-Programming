# Scientific Programming

A scientific programming course learning the concepts of python--
integrated with pre-calculus 

## What is this?

This project is developed on parallel to a 
[repository](https://github.com/jelkner/ScientificProgramming) maintained and
developed by my teacher, [Jeff Elkner](https://github.com/jelkner).

This module is composed of four parts, all found in the src directory:

### Geometry
The [geometry.py](Scientific-Programming/tree/stable/src/geometry.py) module
consists of various spacial objects & methods to help with more complex topics.

This module experiments with classes to a heavy extent, including features such
as object inheritance and overloading object creation.

### Gaussian Jordan
The [gaussjordan](Scientific-Programming/tree/stable/src/gaussjordan) module
consists of a few files.

[tools.py](Scientific-Programming/tree/stable/src/gaussjordan/tools.py) has
some methods and an class used for converting matrices into a reduced row
echelon form using Gaussian elimination. This object heavily relies on
the geometry module since it uses Vector and Matrix objects to
simplify complex mathematical procedures done on matrices.

### Matrices
The [matrices](Scientific-Programming/tree/stable/src/matrices) module
is mainly focussed around opening and converting a non-pythonic file
to a python object(in this case a matrix object).

It includes a file that is setup as a layout, [unaugmented.dat](
Scientific-Programming/tree/stable/src/matrices/unaugmented.dat
), which contains a matrix that has one set of solutions and is styled in a way
as to pose a challenge to be converted to python(not really though).

The rules for the matrices dat files are as follows:
0. Multiple matrices may be separated by a `##`
0. The lines of a matrix are separated by a newline `\n`
0. Columns of a row are delimited by semicolons `;`

[dat2lit.py](Scientific-Programming/tree/stable/src/matrices/unaugmented.dat)
contains two functions that do the exact same thing, currently undergoing
efficiency tests and trying to find out which one is preferable. Both
functions load a `.dat` file in the format previously mentioned and return a
list of matrix objects.

The ops.py file simply showcases the valid operations that can be done on a
matrix

### Dictionaries
This module is simply a review on dictionaries.

### Prerequisities

What things you need to install the software and how to install them

```
Give examples
```

### Installing

A step by step series of examples that tell you have to get a development env running

Stay what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment

Add additional notes about how to deploy this on a live system

## Built With

* ViM - Test editor
* Maven - Maybe
* Atom - ergaerga

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Marco Sirabella** - *Initial work* - [mjsir911](https://github.com/mjsir911)

See also the list of [contributors](https://github.com/mjsir911/project/docs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc

