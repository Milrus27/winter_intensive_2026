def people_with_age_drink(age):
    conditions = {lambda x: x < 14: 'drink toddy', 
            lambda x: 14 <= x < 18: 'drink coke', 
            lambda x: 18 <= x < 21: 'drink beer', 
            lambda x: x >= 21: 'drink whisky'}
    
    for condition, drink in conditions.items():
        if condition(age):
            return drink
