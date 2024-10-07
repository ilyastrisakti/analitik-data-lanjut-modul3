import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#judul app
st.title('Streamlit Simple App')

#navigasi sidebar
page = st.sidebar.radio("Pilih halaman", ["Dataset", "Visualisasi"])

if page == "Dataset":
    st.header("Halaman Dataset")

    #read file csv
    data = pd.read_csv("pddikti_example.csv")

    #view data
    st.write(data)

elif page == "Visualisasi":
    st.header("Halaman Visualisasi")
    
    #read csv
    data = pd.read_csv("pddikti_example.csv")

    #filter berdasarkan univ
    selected_university = st.selectbox('Pilih Universitas', data['universitas'].unique())
    filtered_data = data[data['universitas'] == selected_university]

    #visualiasi
    plt.figure(figsize=(12, 6))

    for prog_studi in filtered_data['program_studi'].unique():
        subset = filtered_data[filtered_data['program_studi'] == prog_studi]

        #urutkan data berdasarkan 'id' dengan urutan menurun
        subset = subset.sort_values(by="id", ascending=False)

        plt.plot(subset['semester'], subset['jumlah'], label=prog_studi)

    plt.title(f"Visualisasi Data untuk {selected_university}")
    plt.xlabel('Semester')
    plt.xticks(rotation=90) #rotasi tabel x vert
    plt.ylabel('Jumlah')
    plt.legend()

    st.pyplot()