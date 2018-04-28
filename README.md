# mpu
Martins Python Utilities (mpu) is a collection of utility functions and classes
with no other dependencies.

The total size of the package will never be bigger than 10 MB. This makes it
a candidate to include into AWS Lambda projects.


## Installation

```
$ pip install git+https://github.com/MartinThoma/mpu.git
```

It can, of course, also be installed via PyPI.


## Usage

### Datastructures

```
from mpu.datastructures import EList

>>> l = EList([2, 1, 0])
>>> l[2]
0

>>> l[[2, 0]]
[0, 2]

>>> l[l]
[0, 1, 2]
```

### Shell

To enchance your terminals output, you might want to do something like:

```
from mpu.shell import Codes
print('{c.GREEN}{c.UNDERLINED}Works{c.RESET_ALL}'.format(c=Codes))
```


### Quick Examples

Creating small example datastructures is a task I encounder once in a while
for StackExchange answers.

```
from mpu.pd import example_df
df = example_df()
print(df)
```

gives

```
     country   population population_time    EUR
0    Germany   82521653.0      2016-12-01   True
1     France   66991000.0      2017-01-01   True
2  Indonesia  255461700.0      2017-01-01  False
3    Ireland    4761865.0             NaT   True
4      Spain   46549045.0      2017-06-01   True
5    Vatican          NaN             NaT   True
```
