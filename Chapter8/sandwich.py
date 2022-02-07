def make_sandwich(sammich, *ingredients):
    print(f"Making a {sammich} sandwich with the following ingredients:")
    for ingredient in ingredients:
        print(f"- {ingredient}")
        


make_sandwich('Italian', 'salami', 'capicola', 'onion', 'cheese', 'basil', 'oregano', 'tomato')
make_sandwich('Tuna', 'onions', 'mayo', 'celery', 'carrots', 'avocado')
make_sandwich('Roast beef', 'roast beef', 'cheese', 'mustard', 'pickle')

