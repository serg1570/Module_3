calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    line_str = str(string)
    result = (len(line_str), line_str.upper(), line_str.lower())
    count_calls()
    return result


def is_contains(string, list_to_search):
    global result
    string = str(string).lower()
    list_to_search = list(list_to_search)
    count_calls()
    for i in range(len(list_to_search)):
        if str(list_to_search[i]).lower() == string:
            result = True
            break
        else:
            result = False
            continue
    return result


print(string_info('Alarm'))
print(string_info('Tornado'))
print(string_info('Parktronic'))

print(is_contains('Artist', ['ArtiFact', 'aRtIsT', 'ARTistry']))
print(is_contains('base', ['basement', 'basic', 'baseline']))
print(is_contains('Banan', ['NanBA', 'baNAnan', 'baNAN']))

print(calls)
