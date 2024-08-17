calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    task1 = (len(string), string.upper(), string.lower())
    count_calls()
    return task1

def is_contains(string, list_to_search):
    for i in list_to_search:
        if string.lower() in i.lower():
            task2 = True
        else:
            task2 = False
    count_calls()
    return task2

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)