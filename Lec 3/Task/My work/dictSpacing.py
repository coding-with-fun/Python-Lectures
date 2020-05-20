dic = {"key": 'value', 'name': 'Nimesh', "marks": 99, 'k6': "Harshal", "k7": {"key": 'value', 'name': 'Nimesh', "marks": 99, 'k6': "Harshal", "k7": 88.8}}

for j in dic:
    if type(dic[j]) == dict:
        for k in dic[j]:
            print("     ", dic[j][k])
    else:
        print(dic[j])