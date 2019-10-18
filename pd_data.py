
import numpy as np
import pandas as pd

df = pd.DataFrame({
  'col1': ['A', 'A', 'B', np.nan, 'D', 'C'],
'col2': [2, 1, 9, 8, 7, 4],
 'col3': [0, 1, 9, 4, 2, 3],
})


df_ = pd.DataFrame(columns=['A', 'B'])
for i in range(5):
    df_ = df_.append({'A': i, 'B':i+1}, ignore_index=True)
print(df_)
print(df_['A'])
print(df_.columns)

print(df, '\n')
print(df.info())
print(df['col2'])
print(df.sort_values(by=['col2']))


df_label = pd.read_excel('labeled_images_order.xlsx', index_col=0)
print(df_label[5:20])




# Index(['A', 'B'], dtype='object')
# Index(['site', 'media', 'barcode', 'light_top', 'light_bot', 'incubation',
#        'SQ', 'truth'],
#       dtype='object')