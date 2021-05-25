import pandas as pd
from pandasgui import show

# using spotrac injury data
url2015 = 'https://www.spotrac.com/mlb/disabled-list/2015/cumulative-player/'
url2016 = 'https://www.spotrac.com/mlb/disabled-list/2016/cumulative-player/'
url2017 = 'https://www.spotrac.com/mlb/disabled-list/2017/cumulative-player/'
url2018 = 'https://www.spotrac.com/mlb/disabled-list/2018/cumulative-player/'
url2019 = 'https://www.spotrac.com/mlb/disabled-list/2019/cumulative-player/'
url2020 = 'https://www.spotrac.com/mlb/disabled-list/2020/cumulative-player/'

table2015 = pd.read_html(url2015, match='Neftali Feliz')
table2016 = pd.read_html(url2016, match='Carlos Carrasco')
table2017 = pd.read_html(url2017, match='David Paulino')
table2018 = pd.read_html(url2018, match='Christian Walker')
table2019 = pd.read_html(url2019, match='Jeff McNeil')
table2020 = pd.read_html(url2020, match='Luis Torrens')

df2015 = pd.DataFrame(data=table2015[0])
df2016 = pd.DataFrame(data=table2016[0])
df2017 = pd.DataFrame(data=table2017[0])
df2018 = pd.DataFrame(data=table2018[0])
df2019 = pd.DataFrame(data=table2019[0])
df2020 = pd.DataFrame(data=table2020[0])

df2015 = df2015[['Player (408)', 'Team', 'Dates', 'Days']]
df2015.columns = ['Player', 'Team', 'Span', 'Days']
df2015['Year'] = '2015'

df2016 = df2016[['Player (472)', 'Team', 'Dates', 'Days']]
df2016.columns = ['Player', 'Team', 'Span', 'Days']
df2016['Year'] = '2016'

df2017 = df2017[['Player (527)', 'Team', 'Dates', 'Days']]
df2017.columns = ['Player', 'Team', 'Span', 'Days']
df2017['Year'] = '2017'

df2018 = df2018[['Player (574)', 'Team', 'Dates', 'Days']]
df2018.columns = ['Player', 'Team', 'Span', 'Days']
df2018['Year'] = '2018'

df2019 = df2019[['Player (563)', 'Team', 'Dates', 'Days']]
df2019.columns = ['Player', 'Team', 'Span', 'Days']
df2019['Year'] = '2019'

df2020 = df2020[['Player (456)', 'Team', 'Dates', 'Days']]
df2020.columns = ['Player', 'Team', 'Span', 'Days']
df2020['Year'] = '2020'

df_list = [df2020, df2019, df2018, df2017, df2016, df2015]
df = pd.concat(df_list, axis=0)
df['Year'] = df['Year'].astype(str)
df['WAR Lost'] = df.apply(lambda row: (0.85 * row.Days * 1.50) / 150, axis=1)

# initial = input('Give the initial for which team you would like info on.')
# team = df[df["Team"] == initial]

show(df)
# df.to_csv(r'E:/baseball/dataframe.csv', index=False)

