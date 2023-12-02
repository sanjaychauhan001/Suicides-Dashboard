import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("suicide_data.csv")
df['age'] = df['age'].str.split(" ").str[0]
st.set_page_config(layout='wide', page_title='Suicide Analysis')

def Overall_suicides():

    suicide_per_year = df.groupby("year")['suicides/100k pop'].mean().reset_index()
    fig = px.line(suicide_per_year, x='year', y='suicides/100k pop',
                  title="Worldwide Suicides by year", markers=True)
    fig.add_hline(y=df['suicides/100k pop'].mean(), line_dash='dot', line_color="green"
                   , annotation_text="mean")
    st.plotly_chart(fig)

    suicides_by_gender = df.groupby('sex')['suicides/100k pop'].sum().reset_index()
    fig2 = px.pie(suicides_by_gender, names='sex', values='suicides/100k pop',
                  title="suicides by Gender")
    st.plotly_chart(fig2)

    suicide_by_age = df.groupby('age')['suicides/100k pop'].sum().reset_index()
    fig3 = px.pie(suicide_by_age, names='age', values='suicides/100k pop',
                  title="suicides by Age")
    st.plotly_chart(fig3)

    top7 = df.groupby('country')['suicides/100k pop'].mean().sort_values(ascending=False).head(7).reset_index()
    fig4 = px.bar(top7, x='country', y='suicides/100k pop', title="Top 7 countries by suicides")
    st.plotly_chart(fig4)

    st.subheader("mean suicide")
    st.metric("suicides/100k (1985-2016)", df['suicides/100k pop'].mean())

def load_suicides_by_gender():
    male_suicides = df[df['sex'] == 'male'].groupby('year')['suicides/100k pop'].mean().reset_index()
    female_suicides = df[df['sex'] == 'female'].groupby('year')['suicides/100k pop'].mean().reset_index()
    temp_df = male_suicides.merge(female_suicides, on='year')
    temp_df.rename(columns={"suicides/100k pop_x": 'Male',
                           'suicides/100k pop_y': 'Female'}, inplace=True)

    fig5 = px.line(temp_df, x='year', y=temp_df.columns, markers=True,
                   title='Worldwide suicide by Gender')
    fig5.add_hline(y=df['suicides/100k pop'].mean(), line_dash='dot', line_color="green"
                   ,annotation_text="mean")
    st.plotly_chart(fig5)
def load_suicides_by_age():
    temp_df1 = pd.pivot_table(df,index='year', columns='age', values='suicides/100k pop')
    fig6 = px.line(temp_df1, x=temp_df1.index, y=temp_df1.columns, markers=True,
                   title="Worldwide suicides by age")
    fig6.add_hline(y=df['suicides/100k pop'].mean(), line_dash='dot', line_color="green"
                   ,annotation_text="mean")
    st.plotly_chart(fig6)

st.sidebar.title("Suicide Dashboard")

selected_option = st.sidebar.selectbox("select One", ['Overall suicides', "Suicides by gender",'Suicides by age'])
if (selected_option == 'Overall suicides'):
    Overall_suicides()

elif(selected_option == 'Suicides by gender'):
    load_suicides_by_gender()

else:
    load_suicides_by_age()
