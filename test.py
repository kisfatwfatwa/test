def capitalize(String):
    return String.title()
capitalize("shop") # [Shop]
capitalize("python programming") # [Python Programming]
capitalize("how are you!") # [How Are You!]


def merge(dic1,dic2):
    dic3=dic1.copy()
    dic3.update(dic2)
    return dic3
dic1={1:"hello", 2:"world"}
dic2={3:"Python", 4:"Programming"}
merge(dic1,dic2) # {1: 'hello', 2: 'world', 3: 'Python', 4: 'Programming'}
