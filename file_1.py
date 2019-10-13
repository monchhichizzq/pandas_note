import pandas as pd
import numpy as np

'''
查看pandas版本信息
'''
print(pd.__version__)

'''
pandas 有两个主要的数据结构：Series 和 DataFrame
Series: 一维数组对象， array， 包括一组数据还包含一组索引
'''


# Pandas structure : Series
def creating_series():
    '''
    Transfer list to series
    :return: s1: series
    '''
    arr = [5, 53, 22, 33, 43]
    s1 = pd.Series(arr,index=['a','b','c','d','e'])
    s1_index = s1.index
    s1_values = s1.values
    print(s1_index, s1_values)
    return s1

def dir_to_serie():
    '''
    Transfer directory to series
    :return: series_data: completed series, series_data_miss: series with miss data
    '''
    data_directory = {'index_1': 35000, 'index_2': 71000, 'index_3': 16000, 'index_4': 5000}
    series_data = pd.Series(data_directory)
    print('series_data:', series_data)
    states = ['index_0','index_1','index_2','index_3']
    series_data_miss = pd.Series(data_directory, index=states)
    print('series_data_miss:', series_data_miss)
    return series_data, series_data_miss

def detect_miss():
    '''
    Functions isnull and notnull in pandas is used to detect the missing data, output bool value
    :return:
    '''
    series_data, series_data_miss = dir_to_serie()
    # detect the missing data, boolean output
    series_isnull = pd.isnull(series_data_miss)
    print('isnull', series_isnull)
    # detect the missing data, boolean output
    series_notnull = pd.notnull(series_data_miss)
    print('notnull', series_notnull)


def operation():
    '''
    numpy array operation
    Features: it automatically aligns data from different indexes in arithmetic operations.
    :return:
    '''
    s1 = creating_series()
    s1_larger_30 = s1[s1>30]
    print('values >= 30:')
    print(s1_larger_30)
    s1_2 = s1*s1
    print('multiplication:')
    print(s1_2)

def name():
    '''
    The Series object itself and its index have a name attribute that is closely related to other key functions of pandas.
    :return:
    '''
    series_data, series_data_miss = dir_to_serie()
    series_data_miss.name = 'population'
    series_data_miss.index.name = 'state'
    print(series_data_miss)

def attach_value():
    '''
    Series index can be modified locally by ways of assignment
    :return:
    '''
    s1 = creating_series()
    # s1 series with new indexes
    s1.index = ['Bob','Steven','Jeff','Ryan', 'Tom']
    print('s1_new_index:', s1)
    # Attach value to s1 series
    s1['Bob'] = 15
    print('s1_new_Bob:', s1)

# Pandas structure : Dataframe
def create_dataframe():
    '''
    Create a new dataframe (2D array)
    :return: a: Dataframe
    '''
    a = pd.DataFrame(np.random.rand(4,5), index=list('ABCD'), columns=list('abcde'))
    print(a)
    return a


def operation():
    '''
    Add/change columns or rows in Dataframe
    :return:
    '''
    a = create_dataframe()
    # Add column f
    a['f'] = [1,2,3,4]
    # Add row D
    a.ix['D'] = 1
    # Add another dataframe on the bottom
    S = pd.DataFrame(np.random.rand(4, 6), index=list('EFGH'), columns=list('abcdef'))
    a = a.append(S)
    # 切片 take b and e column
    col_b_e= a[['b','e']]
    print(col_b_e)
    # Take row 'A'-'D' and column 'a','c','f'
    square_AD_acf = a.loc['A':'D',['a','c','f']]
    










if __name__ == "__main__":
    '''
    whenever the python interpreter reads a source fil, it does two things:
        it sets a few special variables like __name__, and then
        it executes all of the code found in the file
        
    通俗的理解__name__ == '__main__'：
    假如你叫小明.py，在朋友眼中，你是小明(__name__ == '小明')；
                   在你自己眼中，你是你自己(__name__ == '__main__')

    if __name__ == '__main__'的意思是：
    当.py文件被直接运行时，if __name__ == '__main__'之下的代码块将被运行；
    当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行。
    '''
    # s1 = creating_series()
    # print(s1)
    # attach_value()
    operation()