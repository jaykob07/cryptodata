import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import os

st.header(":bar_chart: Here you can filter the crypto along with the date you want")



def show_file_selection(files):

    return st.sidebar.selectbox("SELECT A CRYPTO TO SEE ITS PRICE", files, index=None, placeholder="Choose...")

def load_data(file_path):
    file_name_without_extension = os.path.splitext(os.path.basename(file_path))[0]

    st.sidebar.write(f"Selected file: {file_name_without_extension}")
    return pd.read_csv(file_path)

def get_selected_date():
    return st.sidebar.date_input("NOW SELECT A DATE", value=None)

def filter_data_by_date(data, selected_date):
    return data.loc[data["date"] == str(selected_date), ["open", "low", "high", "close"]]



def plot_custom_chart(data):
    row_transposed = data.transpose()
    colors = ['blue', 'red', 'green', 'grey']

    # Sección de Streamlit para mostrar el gráfico y la tabla
    st.write("Movimientos del Día:")
    st.table(data)

    # Crear una figura con subplots en una sola fila
    fig, axes = plt.subplots(1, len(data.columns), figsize=(15, 5))

    # Iterar sobre los datos y crear gráficos individuales en cada eje
    for i, (column, color) in enumerate(zip(data.columns, colors)):
        axes[i].bar(column, data[column], color=color)
        axes[i].set_title(column)

    # Ajustar el diseño y mostrar la figura
    plt.tight_layout()
    st.pyplot(fig)

    # Sección de Streamlit para mostrar el gráfico con Bokeh
    st.line_chart(row_transposed)

    return st.button("Haz clic en el botón para generar gráfico")


# def plot_custom_chart(data):
#     row_transposed = data.transpose()
#     colors = ['blue', 'red', 'green', 'grey']

#     # Sección de Streamlit para mostrar el gráfico y la tabla
#     st.write("Performance Of The Day : :chart_with_upwards_trend:")
#     st.table(data)

#     # Gráfico de barras
#     fig, ax = plt.subplots()
#     ax.bar(data.columns, data.values.flatten(), color=colors)

#     # Sección de Streamlit para mostrar el gráfico
#     st.pyplot(fig)

#     # Sección de Streamlit para mostrar el gráfico con Bokeh
#     st.line_chart(row_transposed)

#     return st.button("Click on the button to see its historical movement")

def plot_candlestick_chart(data):
    fig = go.Figure(data=[go.Candlestick(x=data['date'],
                    open=data['open'],
                    high=data['high'],
                    low=data['low'],
                    close=data['close'])])
    return fig.show()
