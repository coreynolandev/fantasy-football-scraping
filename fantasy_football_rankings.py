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
all_ppr_ranks = df_list[1]
qb_ppr_ranks = df_list[2]
rb_ppr_ranks = df_list[3]
wr_ppr_ranks = df_list[4]
te_ppr_ranks = df_list[5]
dst_ppr_ranks = df_list[7]
k_ppr_ranks = df_list[6]

# write to csv
all_ppr_ranks.to_csv('all_ppr_ranks.csv')
