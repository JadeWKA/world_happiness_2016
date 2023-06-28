import streamlit as st
import numpy as np
import pandas as pd
import altair as alt
import seaborn as sns
import matplotlib.pyplot as plt

st.header('World Happiness Data 2016 :smile:')

df = pd.read_csv('world_happiness_2016.csv')

if st.button('expand'):
    st.write(df)
    st.button('collapse')
else:
    st.write(df.head(5))

st.write('Dataset Details: ')

df1 = pd.DataFrame(columns=['Details', 'Values'])



details = {'Countries': df.Country.nunique(),
           'Regions': df.Region.nunique(),
           'Highest Happiness Score: ': df['Happiness Score'].max().round(3),
           'Lowest Happoness Score: ': df['Happiness Score'].min().round(3),
           'Average Happiness Score: ': df['Happiness Score'].mean().round(3),
           'Highest Happiness Score Country: ' : df.loc[df['Happiness Score'].idxmax()]
            }

st.write(details)

corr_df = df.select_dtypes(include=np.number).corr()

st.write(corr_df)

fig, ax = plt.subplots()
sns.heatmap(corr_df, vmin=-1, vmax=1, annot=True)
st.write(fig)


# st.write(df1)

# st.write(df)

# df2 = pd.DataFrame(
#     np.random.randn(200,3),
#     columns = ['a','b','c'])
# c = alt.Chart(df2).mark_circle().encode(
#     x = 'a', y = 'b', size = 'c', color = 'c', tooltip = ['a','b','c']
# )

# st.write(c)

# sns.heatmap(df.select_dtypes(include=np.number).corr(), vmin=-1, vmax=1, annot=True, ax=ax)
