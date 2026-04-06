import json
import random as rnd

dict_from_json = {}

for num in range(1,101):
    size_arr = rnd.randint(100, 10_000)
    arr = [rnd.randint(0, rnd.randint(2, 10000)) for _ in range(size_arr)]
    dict_from_json[num] = arr
    print(num,arr)
print(dict_from_json)
with open("test_dataset.json","w") as f:
    json.dump(dict_from_json,f,indent=4)
  
