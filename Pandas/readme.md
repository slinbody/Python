import pandas

df1 = pandas.read_csv('/tmp/file-1')
df2 = pandas.read_csv('/tmp/file-2')
df3 = pandas.read_csv('/tmp/file-3')

df_total = pandas.concat([df1, df2, df3]) # 合併
df_total = df_total[['Col-A','Col-B','Col-C']] # 只取某部分欄位資料

df_total.columns = ['Col-1','Col-2','Col-3']  # 欄位重新命名

df.groupby(df.columns.tolist(), as_index=False).size() # 依欄位排序
