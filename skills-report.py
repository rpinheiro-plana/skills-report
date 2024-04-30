import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(layout='wide')

column_indexes_to_show = [3, 4, 5]

with st.sidebar:
    st.title('Skills Report')
    uploaded_file = st.file_uploader("Please add the questionaire .csv file", type="csv")


if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    with st.sidebar:
        resource_names = df["Your name and surname:"].unique().tolist()
        resource_name_selected = st.selectbox("Resource Names", resource_names, index=None,)

        options = [4, 8, 7, 6, 5,]
        labels = ["0", "1", "2", "3", "4"]

        skill_level = st.radio("Skill Level:", options=options, format_func=lambda x: labels[options.index(x)])
 
        if resource_name_selected:
            df = df[df["Your name and surname:"] == resource_name_selected]
        
          
    st.write("Complete Resources Skills Answers")
    st.dataframe(df, use_container_width=True, hide_index=True)


    if resource_name_selected and skill_level:
        # Selecione a coluna desejada pelo índice
        column_index = skill_level  # Substitua pelo índice da coluna que você deseja
        selected_column = df.iloc[:, column_index]

        # Exiba o nome da coluna selecionada
        nome_coluna = df.columns[column_index]
        st.write(f'{nome_coluna.split(" (")[0]}')

        # Remova o índice
        selected_column = selected_column.reset_index(drop=True)

        # Exiba os dados da coluna selecionada sem truncamento
        for value in selected_column:
            st.text(value)
    


