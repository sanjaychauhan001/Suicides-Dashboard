import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("suicide_data.csv")
df['age'] = df['age'].str.split(" ").str[0]
st.set_page_config(layout='wide',page_title='Suicide Analysis')

def Overall_suicides():

    col1,col2 = st.columns(2)

    suicide_per_year = df.groupby("year")['suicides/100k pop'].mean().reset_index()

    with col1:
        st.subheader('suicides by year')
        fig,ax = plt.subplots()
        ax.plot(suicide_per_year['year'], suicide_per_year['suicides/100k pop'])
        st.pyplot(fig)

    suicides_by_gender = df.groupby('sex')['suicides/100k pop'].sum()

    with col2:
        st.subheader("suicides by Gender")
        fig2,ax2 = plt.subplots()
        ax2.pie(suicides_by_gender.values, labels=suicides_by_gender.index, autopct='%1.1f%%')
        st.pyplot(fig2)

    col3 ,col4 = st.columns(2)

    suicide_by_age = df.groupby('age')['suicides/100k pop'].sum()
    with col3:
        st.subheader("suicides by Age")
        fig3,ax3 = plt.subplots()
        ax3.pie(suicide_by_age.values, labels=suicide_by_age.index, autopct='%1.1f%%')
        st.pyplot(fig3)

    with col4:
        st.subheader("Top 7 countries by scicides")
        top7 = df.groupby('country')['suicides/100k pop'].mean().sort_values(ascending=False).head(7).reset_index()
        fig4, ax4 = plt.subplots()
        sns.barplot(data=top7, x="country",y='suicides/100k pop',ax=ax4)
        st.pyplot(fig4)

    st.subheader("mean suicide")
    st.metric("suicides/100k (1985-2016)", df['suicides/100k pop'].mean())

def load_suicides_by_gender():
    col5,col6 = st.columns(2)
    male_suicides = df[df['sex'] == 'male'].groupby('year')['suicides/100k pop'].mean().reset_index()
    female_suicides = df[df['sex'] == 'female'].groupby('year')['suicides/100k pop'].mean().reset_index()

    with col5:
        st.subheader("for male")
        fig5,ax5 = plt.subplots()
        ax5.plot(male_suicides['year'],male_suicides['suicides/100k pop'])
        st.pyplot(fig5)

    with col6:
        st.subheader("for female")
        fig6,ax6 = plt.subplots()
        ax6.plot(female_suicides['year'],female_suicides['suicides/100k pop'])
        st.pyplot(fig6)

def load_suicides_by_age():

    age5_14 = df[df['age'] == '5-14'].groupby('year')['suicides/100k pop'].mean().reset_index()
    age15_24 = df[df['age'] == '15-24'].groupby('year')['suicides/100k pop'].mean().reset_index()
    age25_34 = df[df['age'] == '25-34'].groupby('year')['suicides/100k pop'].mean().reset_index()
    age35_54 = df[df['age'] == '35-54'].groupby('year')['suicides/100k pop'].mean().reset_index()
    age55_74 = df[df['age'] == '55-74'].groupby('year')['suicides/100k pop'].mean().reset_index()
    age75 = df[df['age'] == '75+'].groupby('year')['suicides/100k pop'].mean().reset_index()
    col7,col8 = st.columns(2)
    with col7:
        st.subheader("for age 5-14")
        fig7,ax7 = plt.subplots()
        ax7.plot(age5_14['year'],age5_14['suicides/100k pop'])
        st.pyplot(fig7)

    with col8:
        st.subheader("for age 15-24")
        fig8,ax8 = plt.subplots()
        ax8.plot(age15_24['year'],age15_24['suicides/100k pop'])
        st.pyplot(fig8)

    col9,col10 = st.columns(2)
    with col9:
        st.subheader("for age 25-34")
        fig9,ax9 = plt.subplots()
        ax9.plot(age25_34['year'],age25_34['suicides/100k pop'])
        st.pyplot(fig9)

    with col10:
        st.subheader("for age 35-54")
        fig10,ax10 = plt.subplots()
        ax10.plot(age35_54['year'],age35_54['suicides/100k pop'])
        st.pyplot(fig10)

    col11,col12 = st.columns(2)
    with col11:
        st.subheader("for age 55-74")
        fig11,ax11 = plt.subplots()
        ax11.plot(age55_74['year'],age55_74['suicides/100k pop'])
        st.pyplot(fig10)
    with col12:
        st.subheader("for age over 75")
        fig12,ax12 = plt.subplots()
        ax12.plot(age75['year'],age75['suicides/100k pop'])
        st.pyplot(fig12)

st.sidebar.title("Suicide Dashboard")

selected_option = st.sidebar.selectbox("select One",['Overall suicides', "Suicides by gender",'Suicides by age'])
if (selected_option == 'Overall suicides'):
    Overall_suicides()

elif(selected_option == 'Suicides by gender'):
    load_suicides_by_gender()

else:
    load_suicides_by_age()
