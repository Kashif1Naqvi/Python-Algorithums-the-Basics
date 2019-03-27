items = [
  "apple","banana","orange","pear","mango"
]
filter = dict()

for key in items:
  filter[key] = 0


result = set(filter.keys())
print(result)