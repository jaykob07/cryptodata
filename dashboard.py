import streamlit as st
import os
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
from my_streamlit_app import show_file_selection, load_data, get_selected_date, \
    filter_data_by_date, plot_custom_chart, plot_candlestick_chart



def find_and_process_csv():
    folder_path = "csvs"
    files = os.listdir(folder_path)


    if not files:
        st.warning("No hay archivos en la carpeta")
        return

    selected_file = show_file_selection(files)

    if selected_file is not None:
        file_path = os.path.join(folder_path, selected_file)
        data = load_data(file_path)

        selected_date = get_selected_date()

        if selected_date is not None:
            filtered_data = filter_data_by_date(data, selected_date)

            if not filtered_data.empty:
                button_clicked = plot_custom_chart(filtered_data)

                if button_clicked:
                    plot_candlestick_chart(data)
        
        else:
            st.write("")   


if __name__ == "__main__":
    find_and_process_csv()


