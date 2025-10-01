class Distance:
    
    def __init__(self, km, m, cm):
        self.km = km
        self.m = m
        self.cm = cm
    
    def __add__(self, other):
        # Add centimeters
        total_cm = self.cm + other.cm
        extra_m = total_cm // 100
        cm = total_cm % 100

        # Add meters (including extra from cm)
        total_m = self.m + other.m + extra_m
        extra_km = total_m // 1000
        m = total_m % 1000

        # Add kilometers (including extra from m)
        km = self.km + other.km + extra_km

        return f"KM: {km} METER: {m} CENTIMETER: {cm}"
    
    def __del__(self):
        print("call distructor")


# Create two objects
obj1 = Distance(10, 6780, 299800)
obj2 = Distance(20, 34569, 50885)
obj1.distructor()
# Add and print
print(obj1 + obj2)



