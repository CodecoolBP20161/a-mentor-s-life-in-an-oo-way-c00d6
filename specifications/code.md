# Code

## Description
This class represents the Code assignments that  the students have to work on.

## Parent class

None

## Attributes

* ```is_working```
  * data type: boolean value
  * description: This variable stores True if the Code is in usable condition, and False if the Code is useless.
* ```name```
  * data type: string
  * description: stores the name of the current Coding assignment

## Class methods

None

## Instance methods

### ```__init__```
The constructor of the object.

#### Arguments

All of the arguments of the class itself.

#### Return value
None

### ```get_worked_on```

Returns a value for is_working based on the students knowledge, energy, and the random factor.
#### Arguments
* ```student```
  * data_type: Student
  * description: A class containing all the important attributes about a student.

#### Return value
* is_working
* try_count
