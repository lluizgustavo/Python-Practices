

class Car: 
    def __init__(self, model: str, year: int, speed: float) -> None:
        self.model = model.capitalize()
        self.year = year
        self.speed = speed

    def increase_speed(self, speed_index: float):
        return f'Current speed of {self.model}: {self.speed + speed_index}'
    
    def decrease_speed(self, speed_index: float):
        if self.speed - speed_index <= 0:
            return f'Your speed can''t be less / equal to zero.'
        return f'Current Speed of {self.model}: {self.speed - speed_index}'

    def show_car_description(self):
        print(f'''=== {self.model} description ===\n- Model: {self.model}\n- Year: {self.year}\n- Current Speed: {self.speed}''')
        
