# Person

## Description
This class represents a class, from subclasses can inherit.

## Parent class
None

## Attributes

* ```first_name```
  * data type: string
  * description: stores person's first name
* ```last_name```
  * data type: string
  * description: stores person's last name
* ```year_of_birth```
   * data type: int
   * description: stores year of birth
* ```gender```
  * data type: string
  * description: stores gender of person
* ```stress```
  * data type: int
  * description: stores stress level
* ```mood```
  * data type: dictionary
  * description: stores a key (a mood) and a value(a number, which helps to detect if the mood is negative or positive) pair
* ```coffeedrinker```
  * data type: boolean
  * description: stores if the person drinks coffee or not


## Class methods

### ```generate_local```

Creates a ```Person``` object having some basic data from the persons that will be than later instanced in other sublasses.

#### Arguments
None

#### Return value

.```Person``` object

## Instance methods

### ```__init__```
The constructor of the object.

#### Arguments

All of the arguments of the class itself.

#### Return value
None

### ```gender```
Gives back if given gender is a right value. If not, gives back error.

#### Arguments
gender

#### Return value
none

###```full_name```

Creates full name from first and last name.

#### Arguments

first_name, last_name

### Return value
Full name
