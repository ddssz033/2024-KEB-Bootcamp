#8.1
e2f = {"dog": "chien", "cat": "chat", "walrus": "morse"}
print(e2f)

#8.2
print(e2f.get("walrus"))

#8.3
f2e = {v: k for k, v in e2f.items()}
print(f2e)

#8.4
print(f2e.get("chien"))

#8.5
print(e2f.keys())

#8.6
life = dict(animals={'cats':["Henry", "Grumpy", "Lucy"], "octopi": " ", "emus": " " }, plants={}, other={})

#8.7
top_level_keys = [x for x in life.keys()]
print(top_level_keys)

#8.8
print(life['animals'])

#8.9

#8.10
