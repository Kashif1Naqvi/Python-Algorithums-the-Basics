items1 = {"key1":1,"key2":"hello","key3":"naqvi","key4":{
  "key":"value"
}}
item = dict(items1)

#  search specific value if exists
print(items1["key3"])
# loop through all values in hash table

for key , value in items1.items():
    print("keys:",key,"values:",value) 
