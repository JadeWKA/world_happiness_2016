import streamlit as st
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

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


