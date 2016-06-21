# Mentor

## Description
Class represents mentors working at codecool

## Parent class
Person

## Attributes

* ```nickname```
  * data type: string
  * description: Stores the nickname of codecool mentors
* ```teaching_level```
  * data type: integer
  * description: stores the teaching ability of mentors


## Class methods



## Instance methods

### ```__init__```
The constructor of the object.

#### Arguments

All of the arguments of the class itself.

#### Return value
None

### ```teach```

Change the ```student``` 's knowledge and energy level.

#### Arguments
* ```teaching_level```
  * data_type: int
  * modify the change of knowledge and energy level. Higher number makes higher change in knowledge and smaller in energy level


#### Return value

* ```d_knowledge``` and ```d_energy```

### ```check_energy_level```

If a  ```student```'s energy level is under a constant, puts it into a list. print something nice for every item of a list', raise energy
#### Arguments


#### Return value
* ```energy level```

### ```check_mood```
Calculate the average mood of the class, if it's under a value, print something nice, change everybody's mood to max

#### Arguments

#### Return value
* energy_level
