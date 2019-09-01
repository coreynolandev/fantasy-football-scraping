# Corey Nolan 2019.09.01

import requests
import pandas as pd


# base url
url = 'https://www.espn.com/fantasy/football/story/_/id/25759239/fantasy-football-2019-updated-top-200-ppr-rankings-matthew-berry'

# gets html of fantasy football website
html = requests.get(url).content
df_list = pd.read_html(html)

# discover what tables consist of, printing index of table
# i = 0
# for df in df_list:
#     print("\nTable#" + str(i) + "\n")
#     print(df.iloc[:3])
#     i += 1

# all tables
berry_all_ppr_ranks = df_list[1]
berry_qb_ppr_ranks = df_list[2]
berry_rb_ppr_ranks = df_list[3]
berry_wr_ppr_ranks = df_list[4]
berry_te_ppr_ranks = df_list[5]
berry_dst_ppr_ranks = df_list[7]
berry_k_ppr_ranks = df_list[6]


for index, row in berry_all_ppr_ranks.iterrows():
    row[0] = ''.join(x for x in row[0] if x.isalpha())

# write to csv
# berry_all_ppr_ranks.to_csv('all_ppr_ranks_matt_berry.csv')


# https://www.espn.com/fantasy/football/story/_/id/26415022/fantasy-football-updated-2019-ppr-rankings-mike-clay
url = 'https://www.espn.com/fantasy/football/story/_/id/26415022/fantasy-football-updated-2019-ppr-rankings-mike-clay'

# gets html of fantasy football website
html = requests.get(url).content
df_list = pd.read_html(html)

# discover what tables consist of, printing index of table
# print("\nClay\n")
# i = 0
# for df in df_list:
#     print("\nTable#" + str(i) + "\n")
#     print(df.iloc[:3])
#     i += 1

# all tables
clay_all_ppr_ranks = df_list[1]
clay_qb_ppr_ranks = df_list[2]
clay_rb_ppr_ranks = df_list[3]
clay_wr_ppr_ranks = df_list[4]
clay_te_ppr_ranks = df_list[5]
clay_dst_ppr_ranks = df_list[7]
clay_k_ppr_ranks = df_list[6]

clay_list = []

for index, row in clay_all_ppr_ranks.iterrows():
    row[0] = ''.join(x for x in row[0] if x.isalpha())
    clay_list.append(row[0])


# https://www.espn.com/fantasy/football/story/_/id/26701720/fantasy-football-updated-2019-ppr-rankings-tristan-h-cockcroft
url = 'https://www.espn.com/fantasy/football/story/_/id/26701720/fantasy-football-updated-2019-ppr-rankings-tristan-h-cockcroft'

# gets html of fantasy football website
html = requests.get(url).content
df_list = pd.read_html(html)


# discover what tables consist of, printing index of table
# print("\nCockcroft\n")
# i = 0
# for df in df_list:
#     df = df[df.columns.drop(list(df.filter(regex='Unnamed')))]
#     print("\nTable#" + str(i) + "\n")
#     print(df.iloc[:3])
#     i += 1
# want to delete the Unnamed: 2 column

# all tables
cockcroft_all_ppr_ranks = df_list[1]
cockcroft_qb_ppr_ranks = df_list[2]
cockcroft_rb_ppr_ranks = df_list[3]
cockcroft_wr_ppr_ranks = df_list[4]
cockcroft_te_ppr_ranks = df_list[5]
cockcroft_dst_ppr_ranks = df_list[7]
cockcroft_k_ppr_ranks = df_list[6]

cockcroft_list = []

for index, row in cockcroft_all_ppr_ranks.iterrows():
    row[2] = ''.join(x for x in row[2] if x.isalpha())
    cockcroft_list.append(row[2])


# https://www.espn.com/fantasy/football/story/_/id/25848947/2019-updated-fantasy-football-ppr-rankings-field-yates
url = 'https://www.espn.com/fantasy/football/story/_/id/25848947/2019-updated-fantasy-football-ppr-rankings-field-yates'

# gets html of fantasy football website
html = requests.get(url).content
df_list = pd.read_html(html)

# discover what tables consist of, printing index of table
# print("\nYates\n")
# i = 0
# for df in df_list:
#     print("\nTable#" + str(i) + "\n")
#     print(df.iloc[:3])
#     i += 1

# all tables
yates_all_ppr_ranks = df_list[1]
yates_qb_ppr_ranks = df_list[2]
yates_rb_ppr_ranks = df_list[3]
yates_wr_ppr_ranks = df_list[4]
yates_te_ppr_ranks = df_list[5]
yates_dst_ppr_ranks = df_list[7]
yates_k_ppr_ranks = df_list[6]

yates_list = []

for index, row in yates_all_ppr_ranks.iterrows():
    row[0] = ''.join(x for x in row[0] if x.isalpha())
    yates_list.append(row[0])


total_cols = len(berry_all_ppr_ranks.columns)


def ret_pos(use_list, name):
    if name in use_list:
        return use_list.index(name) + 1
    else:
        return 1000

final_clay = []
final_cockcroft = []
final_yates = []

for index, row in berry_all_ppr_ranks.iterrows():
    final_clay.append(ret_pos(clay_list, row[0]))
    final_cockcroft.append(ret_pos(cockcroft_list, row[0]))
    final_yates.append(ret_pos(yates_list, row[0]))


berry_all_ppr_ranks.insert(total_cols, 'Berry\'s Ranks', range(1, 1+len(berry_all_ppr_ranks)))
berry_all_ppr_ranks.insert(total_cols + 1, 'Clay\'s Ranks', final_clay)
berry_all_ppr_ranks.insert(total_cols + 2, 'Cockcroft\'s Ranks', final_cockcroft)
berry_all_ppr_ranks.insert(total_cols + 3, 'Yates\' Ranks', final_yates)

print(berry_all_ppr_ranks)

berry_all_ppr_ranks.to_csv('expert_PPR_ranks.csv')
