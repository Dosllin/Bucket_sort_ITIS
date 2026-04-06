import json
import pandas as pd
from BucketSort import *
import time
import matplotlib.pyplot as plt
import docx

try:
    with open('test_dataset.json','r') as f:
        dict_from_json = json.load(f)
except FileNotFoundError:
    raise FileNotFoundError('test_dataset.json не найден, пожалуйста, воспользуйтесь Write_data.py')

dict_result = {}
count = 1
for array in dict_from_json.values():
    print("Изначальный: ", array)
    start = time.time()
    steps = bucket_sort(array)
    end = time.time()
    execution_time = end - start
    print("После сортировки: ",array)
    print(f"Данные: время выполнения = {execution_time:.9f}, количество шагов/итераций = {steps}")
    print('-----------------')
    dict_result[count] = [execution_time,steps,len(array)]
    count += 1

df = pd.DataFrame.from_dict(dict_result,orient='index',columns = ['execution_time','steps','len_array'])
df.to_excel("results_table.xlsx", index=True)

fig, (first_space, second_space) = plt.subplots(nrows=1, ncols=2, figsize=(14, 6))

df.plot(x='len_array', y='execution_time', kind='scatter', ax=first_space, color='blue', alpha=0.6)
first_space.set_title('Зависимость времени от размера массива')
first_space.set_xlabel('Размер массива (количество элементов)')
first_space.set_ylabel('Время выполнения (секунды)')
first_space.grid(True)

df.plot(x='len_array', y='steps', kind='scatter', ax=second_space, color='red', alpha=0.6)
second_space.set_title('Зависимость количества итераций от размера')
second_space.set_xlabel('Размер массива (количество элементов)')
second_space.set_ylabel('Количество шагов (итераций)')
second_space.grid(True)

plt.tight_layout()
plt.show()
