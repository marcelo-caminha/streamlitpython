import streamlit as st
import time

print(f'Script rodou às {time.strftime("%H:%M:%S")}')

st.title('Testando o modelo de execução do Streamlit')

contador = 0 

valor = st.slider('Escolha um valor', 0, 10)

contador += 1
st.write(f'Você escolheu o valor: {valor}')
st.write(f'Contador: {contador}')