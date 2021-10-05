from seaborn.widgets import choose_colorbrewer_palette
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data = pd.read_csv('train.csv')
st.title('Trung tâm tin học')
st.header('Data Science')

menu = ["Display Text", "Display Data","Display Chart","Display Interactive Widget"]

choice = st.sidebar.selectbox('Menu', menu)
if choice == 'Display Text':
    st.subheader('Hành trang tốt nghiệp data science')
    st.text('Khóa học thiết kế ôn tập và bổ sung kiến thức')
    st.markdown("### có 5 chủ đề: ")
    st.write("""
    - chủ đề 1
    - chủ đề 2
    - ...""")
    st.write("### Ngôn ngữ lập trình: python")
    st.code("st.display_text_function('Nội dung')",language="python")
elif choice == 'Display Data':
    st.write('## Display Data')
    st.dataframe(data.head(3))
    st.table(data.head(3))
    st.json(data.head(3).to_json())
elif choice == 'Display Chart':
    st.write('## Dispaly Chart')
    count_Pclass = data[['PassengerId','Pclass']].groupby('Pclass').count()
    st.bar_chart(count_Pclass)
    fig, ax = plt.subplots()
    ax = sns.boxplot(x='Pclass',y='Fare',data=data)
    st.pyplot(fig)
else:
    st.write("## Display Interactive Widget")
    st.write("## Input your information")
    name = st.text_input("Name:")
    sex = st.radio("Sex",options=['Male','Female'])
    age = st.slider("Age",1,100,1)
    jobtime = st.selectbox('You have',options=['parttime','fulltime'])
    hobbies = st.multiselect('Hobbies',options=['cooking','reading','travel','writing','other'])
    house = st.checkbox('Have house/apartment')
    submit = st.button('Submit')
    if submit:
        st.write("### Your Information:")
        st.write("Name:",name,
        "- Sex:", sex,
        "- Age:", age,
        "- You have a", jobtime,
        "and a house/apartment" if house else "",
        "- Hobbies:",', '.join(map(str,hobbies)))