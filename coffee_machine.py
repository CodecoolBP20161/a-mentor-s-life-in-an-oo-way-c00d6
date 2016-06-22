class CoffeeMachine():
    def __init__(self, is_working, coffee_level, water_level, is_clean, powered):
        self.is_working = is_working
        self.coffee_level = coffee_level
        self.water_level = water_level
        self.is_clean = is_clean
        self.powered = powered

    def toggle_power(self):
        if self.powered:
            self.powered = False
        else:
            self.powered = True
        return(self.powered)

    def get_cleaned(self):
        if not self.is_clean:
            self.is_clean = True
        return(self.is_clean)

    def get_filled_coffee(self):
        self.coffee_level = 100
        return(self.coffee_level)

    def get_filled_water(self):
        self.water_level = 100
        return(self.water_level)

    def check_if_working(self):
        self.is_working = True
        if not self.powered:
            print(" You gotta turn me on first bro")
            self.is_working = False
        elif not self.is_clean:
            print("I'm not gona make you anything as long as i'm this filthy")
            self.is_working = False
        elif self.water_level == 0:
            print("Let's trade! Gimme some water and i'll give you coffe")
            self.is_working = False
        elif self.coffee_level == 0:
            print("You need coffee to make coffee bro")
            self.is_working = False
        return(self.is_working)

        def make_coffee(self):
            if self.is_working:
                self.water_level -= 20
                self.coffee_level -= 10
                print("Here is your caffee, drink it while it's hot!")
            else:
                print("Sorry but somthing's not right")
            return(self.water_level, self.coffee_level)
