class cashier:

    def __init__(self, c):
        self.cash = c
    
    def top_up(self, x):
        self.cash += x
    
    def take_away(self, x):
        self.cash -= x
    
    def count_1000(self):
        return int(self.cash / 1000)

c = cashier(10000)
print(c.count_1000())
c.top_up(10000)
print(c.count_1000())
c.take_away(10000)
print(c.count_1000())