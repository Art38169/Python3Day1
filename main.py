class Circle:
    def __init__(self, radius, x, y):
        self.radius = radius
        self.x = x
        self.y = y
        
    def draw(self):
        print(f"{self.x}, {self.y}")
    
    def move(self, shift_x, shift_y):
            self.x += shift_x
            self.y += shift_y
        
        
        
        

if __name__ == "__main__":
    c = Circle(10, 100, 100)
    
    window_width = 300
    window_height = 300
    vx = 1
    vy = 1
    
    for i in range(1000):
        c.move(vx, vy)
        c.draw()
        if c.x > window_width or c.x < 0:
            vx = -vx
        if c.y > window_height or c.y < 0:
            vy = -vy
    