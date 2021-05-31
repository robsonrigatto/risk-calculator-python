class Balance():
    def __init__(self, value):
        self.value = value
    
    def decrease(self, delta):
        self.value = self.value - delta

    def increase(self, delta):
        self.value = self.value + delta