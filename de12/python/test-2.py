import pandas as pd
import japanize_matplotlib

#Excelファイルを読み込む
df = pd.read_excel('C:/Users/haru-/mygit/xbp/de12/python/filespy/家計簿.xlsx')

#データフレームを出力する
print(df)

# データを追加
new_entry = {'日付': '2023-10-31', '詳細': 'アルバイト', '金額': 74000, '収支': '収入'}
new_entry = {'日付': '2023-10-31', '詳細': '食費', '金額': 500, '収支': '支出'}
new_entry = {'日付': '2023-10-31', '詳細': 'その他', '金額': 2000, '収支': '支出'}
new_entry = {'日付': '2023-11-05', '詳細': '衣類', '金額': 10000, '収支': '支出'}

se = pd.Series(new_entry).to_frame().T
df = pd.concat([df, se], axis=0)
# df = df.append(new_entry, ignore_index=True)

# データをExcelファイルに書き込み
df.to_excel('C:/Users/haru-/mygit/xbp/de12/python/filespy/家計簿.xlsx', index=False)
# 収支を計算
income = df[df['収支'] == '収入']['金額'].sum()
expenses = df[df['収支'] == '支出']['金額'].sum()
balance = income - expenses
import matplotlib.pyplot as plt

# カテゴリー別の支出をプロット
category_expenses = df[df['収支'] == '支出'].groupby('詳細')['金額'].sum()
category_expenses.plot(kind='bar')
plt.xlabel('カテゴリー')
plt.ylabel('支出')
plt.title('カテゴリー別支出')
plt.show()

# import pandas as pd

# initial_data = {
#     '日付': [],
#     '詳細': [],
#     '金額': [],
#     '収支': []
# }

# df = pd.DataFrame(initial_data)

# # 新しいExcelファイルを作成
# df.to_excel('家計簿.xlsx', index=False)

