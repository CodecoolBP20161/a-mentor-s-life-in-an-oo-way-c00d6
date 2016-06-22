# CoffeeMachine

## Description
This class represents the Coffee machine in the office.
It's either working or not.
## Parent class
None

## Attributes

* ```is_working```
  * data type: boolean value
  * description: decides whether the machine is operational or not
* ```coffee_level```
  * data type: integer
  * description: if it hits 0 the machine wont work until it is refilled
* ```water_level```
   * data type: integer
   * description: if it hits 0 the machine wont work until it is refilled
* ```is_clean```
  * data type: boolean value
  * description: the machine only works if it's clean
* ```powered```
  * data type: boolean value
  * description: the machine only works if it's on

## Class methods

### ```None```

#### Arguments
None

#### Return value

None

## Instance methods

### ```__init__```
The constructor of the object.

#### Arguments

All of the arguments of the class itself.

#### Return value
None

### ```toggle_power```

Turns the machine on or off

#### Arguments
* ```self```


#### Return value
```powered``` value

### ```get_cleaned```

#### Arguments
* ```self```
  * data_type: boolean
  * description: someone cleans the machine

#### Return value
```is_clean``` value

### ```get_filled_coffee```

#### Arguments
* ```self```
  * data_type: integer
  * description: raises the coffee_level

#### Return value
```coffee_level``` value

### ```get_filled_water```

#### Arguments
* ```self```
  * data_type: integer
  * description: raises the water_level

#### Return value
```water_level``` value

### ```check_if_working```

#### Arguments
* ```self ```
  * data_type: boolean
  * description: checks whether the working conditions are true

#### Return value
```is_working``` value
