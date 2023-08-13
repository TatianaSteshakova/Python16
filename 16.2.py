class turtle:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.s = 1
    
    def go_up(self):
        self.y += self.s
    
    def go_down(self):
        self.y -= self.s
    
    def go_left(self):
        self.x -= self.s
    
    def go_right(self):
        self.x += self.s
    
    def evolve(self):
        self.s += 1
    
    def degrade(self):
        if self.s - 1 <= 0:
            print("S может стать меньше или равным 0. Отмена.")
        self.s -= 1
    
    def count_moves(self, x2, y2):
        return (abs(x2 - self.x) // self.s) + (abs(y2 - self.y) // self.s)
    

t = turtle()
print (t.count_moves(2, 2))