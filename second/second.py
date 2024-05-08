# 40대 여행 동반자 - word cloud
# import pandas as pd
# from wordcloud import WordCloud
# import matplotlib.pyplot as plt

# file_path = r"C:\Users\utw09\Desktop\정노을\본캠 프로젝트\travel\trippartner_f.csv"

# df = pd.read_csv(file_path)

# text_data = " ".join(df['AGE40'].astype(str))

# word_freq = pd.Series(text_data.split()).value_counts()

# def random_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
#     colors = ['#001f3f', '#0074cc', '#00a1e4', '#00bcd4', '#4caf50', '#8bc34a', '#cddc39', '#ffeb3b', '#ffc107', '#ff5722']
#     return colors[random_state.randint(0, len(colors))]

# wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_data)

# plt.figure(figsize=(10, 5))
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis('off')
# plt.show()

#여행 동반자 - 원형 그래프
# import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib import font_manager, rc
# import numpy as np

# file_path = r"C:\Users\utw09\Desktop\정노을\본캠 프로젝트\travel\tp.csv"

# df = pd.read_csv(file_path, encoding='utf-8')

# font_path = "C:\\Windows\\Fonts\\malgun.ttf"
# font_name = font_manager.FontProperties(fname=font_path).get_name()
# rc('font', family=font_name)

# print(df.head())

# plt.figure(figsize=(8, 8))
# areas = np.pi * (df['RANK'] / df['RANK'].sum()) * 1000
# plt.pie(df['RANK'], labels=df['AGE40'], autopct='%1.1f%%', startangle=90, counterclock=False, wedgeprops=dict(width=0.4),radius=1, textprops={'fontsize': 14})

# plt.title('Trip Partner', fontsize=16)

# plt.show()

#40대 여행 테마
# import pandas as pd
# from wordcloud import WordCloud
# import matplotlib.pyplot as plt

# file_path = r"C:\Users\utw09\Desktop\정노을\본캠 프로젝트\travel\tripact_f.csv"

# df = pd.read_csv(file_path)

# text_data = " ".join(df['AGE40'].astype(str))

# word_freq = pd.Series(text_data.split()).value_counts()

# def random_color_func(word, font_size, position, orientation, random_state=None, **kwargs):
#     colors = ['#001f3f', '#0074cc', '#00a1e4', '#00bcd4', '#4caf50', '#8bc34a', '#cddc39', '#ffeb3b', '#ffc107', '#ff5722']
#     return colors[random_state.randint(0, len(colors))]

# wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_data)

# plt.figure(figsize=(10, 5))
# plt.imshow(wordcloud, interpolation='bilinear')
# plt.axis('off')
# plt.show()

# 연령별 출산율 1993 ~ 2022
# import pandas as pd
# import matplotlib.pyplot as plt

# file_path = r"C:\Users\utw09\Desktop\정노을\본캠 프로젝트\travel\birthrate_total.csv"

# df = pd.read_csv(file_path)

# age_column = 'age'

# years = ['year1993_2022']
# birth_rate_data = df[['age'] + years]

# # birth_rate_data['year1993_2022'] = birth_rate_data['year1993_2022'].astype('float')
# plt.plot(birth_rate_data[age_column], birth_rate_data['year1993_2022'], label='year1993_2022')

# plt.title('Birth Rates by Age Group')
# plt.xlabel('AGE')
# plt.ylabel('Birth Rate')

# plt.legend()

# plt.show()

# 연령별 출산율 - 1993_2022,2023
import pandas as pd
import matplotlib.pyplot as plt

# file_path = r"C:\Users\utw09\Desktop\정노을\본캠 프로젝트\travel\birth_t.csv"
file_path = r"C:\Users\utw09\Desktop\정노을\본캠 프로젝트\travel\birtrh_t.csv"
df = pd.read_csv(file_path)

age_column = 'AGE'

years = ['YEAR1993_2022', 'YEAR2023']
birth_rate_data = df[['AGE'] + years]

plt.plot(birth_rate_data[age_column], birth_rate_data['YEAR1993_2022'], label='year1993_2022')
plt.plot(birth_rate_data[age_column], birth_rate_data['YEAR2023'], label='year2023')

plt.title('Birth Rates by Age Group')
plt.xlabel('AGE')
plt.ylabel('Birth Rate')

plt.legend()

plt.show()

# 지역별 여행테마 - HISTORY
# import pandas as pd
# import matplotlib.pyplot as plt

# file_path = r"C:\Users\utw09\Desktop\정노을\본캠 프로젝트\travel\triptheme_f.csv"

# df = pd.read_csv(file_path, encoding='utf-8')

# plt.rcParams['font.family'] = 'Malgun Gothic'

# categories = df['HISTORY']
# ranks = df['RANK']

# plt.bar(categories, ranks, color='skyblue')

# plt.xlabel('REGION')
# plt.ylabel('RANK')
# plt.title('Historical Sites')

# plt.show()

#지역별 여행테마 - THEMEPARK

# import pandas as pd
# import matplotlib.pyplot as plt

# file_path = r"C:\Users\utw09\Desktop\정노을\본캠 프로젝트\travel\triptheme_f.csv"

# df = pd.read_csv(file_path, encoding='utf-8')

# plt.rcParams['font.family'] = 'Malgun Gothic'

# categories = df['THEMEPARK']
# ranks = df['RANK']

# plt.bar(categories, ranks, color='YELLOW')

# plt.xlabel('REGION')
# plt.ylabel('RANK')
# plt.title('Theme Park Locations')

# plt.show()

# #지역별 여행테마 - total themepark

# import pandas as pd
# import matplotlib.pyplot as plt

# file_path = r"C:\Users\utw09\Desktop\정노을\본캠 프로젝트\travel\region_f.csv"

# df = pd.read_csv(file_path, encoding='utf-8')

# plt.rcParams['font.family'] = 'Malgun Gothic'

# categories = df['THEMEPARK']
# ranks = df['RANK']

# plt.bar(categories, ranks, color='YELLOW')

# plt.xlabel('REGION')
# plt.ylabel('RANK')
# plt.title('Theme Park Locations')

# plt.show()