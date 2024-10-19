def fuel_cost(distance,cost_per_litre = 50,km_per_litre = 60):
    fuel_cost = distance/km_per_litre*cost_per_litre 
    return  fuel_cost
print(fuel_cost(100))


