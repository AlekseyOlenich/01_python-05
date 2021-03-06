import pandas as pd

data = pd.Series(["Январь", "Февраль", "Март", "Апрель"],
                 index=['Первый', "Второй", "Третий", "Четвёртый"])
print(data)

print(data.loc[["Первый", "Третий"]])

data = pd.Series(list(range(10, 1001)))
print(data.loc[10] + data.loc[23] - data.loc[245] + data.iloc[122])

df = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
print(df)

df = pd.DataFrame([[1, 2, 3], [2, 3, 4]],
                  columns=['foo', 'bar', 'baz'],
                  index=['foobar', 'foobaz'])
print(df)

df = pd.DataFrame({'Тестовая колонка': [1, 5]})
print(df)
