d1 = {"a": 10, "b": 20, "c": 30}
d2 = {"b": 5, "c": 15, "d": 40}

result = {}

for i in d1:
    result[i] = d1[i]

for i in d2:
    if i in result:
        result[i] += d2[i]
    else:
        result[i] = d2[i]

print(result)