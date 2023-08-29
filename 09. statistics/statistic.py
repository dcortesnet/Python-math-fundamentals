import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('data.csv')

print(data) 
"""
     name  age  score
0    Juan   25     85
1   Maria   28     92
2    Luis   22     78
3     Ana   24     90
4  Carlos   27     88
"""

mean_age = np.mean(data['age'])
median_age = np.median(data['age'])
des_age = np.std(data['age'])

print(mean_age) # 25.2
print(median_age) # 25.0
print(des_age) # 2.1354156504062622

plt.bar(data['name'], data['age'])
plt.xlabel('Name')
plt.ylabel('Age')
plt.title('Age of persons')
plt.xticks(rotation=45)
plt.show()