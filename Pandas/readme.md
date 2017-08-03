import pandas

df1 = pandas.read_csv('/tmp/file-1')<br>
df2 = pandas.read_csv('/tmp/file-2')<br>
df3 = pandas.read_csv('/tmp/file-3')<br>

df_total = pandas.concat([df1, df2, df3]) # 合併<br>
df_total = df_total[['Col-A','Col-B','Col-C']] # 只取某部分欄位資料<br>

df_total.columns = ['Col-1','Col-2','Col-3']  # 欄位重新命名

df_group = df.groupby(df.columns.tolist(), as_index=False).size() # 依欄位排序

df_group = pandas.DataFrame({'Count': df_group}).reset_index() # 排序過的資料轉成DataFrame

df_group[-1] = [ data ]              # 插入資料<br>
df_group.index = df_group.index + 1<br>
df_group = df_group.sort()<br>


df_group = df_group.sort('NUM', ascedning=False) # 以某欄位進行排序，反向排序

df_group.to_csv('/tmp/result.csv', sep=',', index=False, encoding='utf-8')
