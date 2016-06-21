# Student

## Description
This class represents a real Student, containing the student's coding knowledge level and stores the student's energy level.

## Parent class
#### ```person```

## Attributes

* ```knowledge_level```
  * data type: integer
  * description: stores the student's coding knowledge level
* ```energy_level```
  * data type: integer
  * description: stores the student's energy level

## Class methods
none

#### Arguments
None

#### Return value
None

## Instance methods

### ```__init__```
The constructor of the object.


### ```use_EKI(name)```
The student uses an instance of EKI class called name, which modifies the student's knowledge level, and energy level
#### Arguments    
* ```name```
  * data_type: string
  * description: holds the name of the EKI which will be used

#### Return value
```knowledge_level, energy_level``` value

### ```ask_for_help(try_count)```
If the CODE class Get_worked_on() method returns FALSE three times, call the MENTOR class teach() method.
#### Arguments
* ```try_count```
  * data_type: integer
  * description: holds the value of the CODE class try_count's value

#### Return value
```knowledge_level``` value
