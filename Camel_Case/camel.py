camelCase = input('camelCase: ')
snake_case = ''
for i in range(len(camelCase)):
    if camelCase[i].isupper():
        snake_case += '_' + camelCase[i]
        snake_case = snake_case.lower()
    else:
        snake_case += camelCase[i]
print('snake_case',snake_case)
