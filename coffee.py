class Coffee():
    """ Coffee class to track an individual's consumption """
    def __init__(self):
        self.cups = 0
    
    def __str__(self):
        return f'cups: {self.cups}'

    def check_cups(self):
        print(f'You have consumed {self.cups} cups of coffee so far today')

    def check_over_caffeinated(self):
        if self.cups == 0:
            print(f'You have not consumed any coffee today.')
        elif self.cups > 5:
            print(f'You have consumed too much coffee today!')
        else:
            print(f'You have consumed a reasonable amount of coffee so far today.')

    def drink(self):
        self.cups += 1
        self.check_cups()
        self.check_over_caffeinated()
    
starbucks_drinker = Coffee()

print(starbucks_drinker)
starbucks_drinker.drink()
starbucks_drinker.drink()
starbucks_drinker.drink()
starbucks_drinker.drink()
starbucks_drinker.drink()
starbucks_drinker.drink()
starbucks_drinker.drink()
starbucks_drinker.drink()
starbucks_drinker.drink()
starbucks_drinker.drink()