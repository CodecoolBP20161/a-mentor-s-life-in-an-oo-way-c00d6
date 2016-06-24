class CoffeeMachine():

    def __init__(self, coffee_level, water_level, is_clean, powered):
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
        print("Luckily Csibi, not being an addict, can handle the situation and fills the machine with water.")
        return(self.water_level)

    def check_if_working(self):
        is_working = True
        if not self.powered:
            print(" You gotta turn me on first bro")
            is_working = False
        elif not self.is_clean:
            print("please clean the unit")
            is_working = False
        elif self.water_level == 0:
            print("The machine is out of water")
            is_working = False
        elif self.coffee_level == 0:
            print("The machine is out of coffee")
            is_working = False
        return(is_working)

    def make_coffee(self):
        print ("Dani tries to make his latte.")
        is_working = self.check_if_working()
        if is_working:
            self.water_level -= 20
            self.coffee_level -= 10
            print("Dani finally gets his coffee!")
        else:
            print("As he realizes that he won't get his coffee, he panics and starts to cry.")
        return(self.water_level, self.coffee_level)
