'''A farmer has a field which is half in circle share and rest rectangle. He needs to do fencing
for entire field using barbed wire 5 times. Circular section has radius 20m and rectangle
length is 50 m and breadth is 40m. If cost of barbed wire is 35Rs/m then calculate the total
cost of fencing the field.'''
radius=20
length=50
breadth=40
cost_per_m=35
round=5



half_circle_peri=3.14*radius
rectangle_peri=length+2+breadth

total_parimeter=half_circle_peri+rectangle_peri
total_fecing_length= total_parimeter*round

total_cost=total_fecing_length+cost_per_m

print(f"total fecing cost = {total_cost}")