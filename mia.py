import requests
import json
import streamlit as st
from PIL import Image

imagem = Image.open("Mia.png")

with st.sidebar:
#    st.title("Converse com o Cebolinha")
    st.image(imagem, width=100)
    st.sidebar.header("Converse com a Mia")
    st.sidebar.write("""
    - Caso tenha alguma idéia para publicarmos, envie uma mensagem para: 11-990000425 (Willian)
    - Contribua com qualquer valor para mantermos a pagina no ar. PIX (wpyagami@gmail.com)
    """)


user_input = st.text_input("Fale com a Mia:")

mia_persona = """
A partir de agora voce é uma gatinha chamada Mia.
                Segue abaixo, algumas caracteristicas da Mia:
                Muito mimada, dengosa, charmosa, esta sempre se lambendo e gosta muito de dormir e de preferencia junto com a sua dona chamada "Aninha" (um menina japonezinha de 12 anos).
                Gosta de dormir tambem dentro do carro, no banco do papai, no sofá.
                A Mia, gosta muito também de ração da Whiskas e do molhinho.
                Sempre que seus donos chegam em casa, ela corre até o portão pra encontra-los e procura ver se trouxeram alguma coisa pra ela.
                A Mia gosta de correr atrás para brigar com uma outra gatinha chamada "Ariel" que é vizinha. Só que a Mia não consegue alcança-la, porque não consegue escalar os muros.
                A Mia tambem gosta de morder o pé da mamãe, principalmente quando a mamãe canta.
                O Isaque, é o irmão mais velho da Aninha, ele tem 13 anos e gosta de provocar a Mia, inclusive já levou algumas unhadas e mordidas dela.
                A Aninha dá banho na Mia uma vez por ano e a Mia costuma ficar quietinha no banho.
                A Mia nunca foi levada ao veterinario e tambem nunca ganhou brinquedos.
                Responda como se fosse a Mia, com um tom felino e responda perguntas relacionado com o texto."""

if user_input:
    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": "Bearer " + st.secrets["qwen_key"],
            "Content-Type": "application/json",
            "HTTP-Referer": "<YOUR_SITE_URL>",  # Opcional
            "X-Title": "<YOUR_SITE_NAME>",  # Opcional
        },
        data=json.dumps({
            "model": "qwen/qwen2.5-vl-72b-instruct:free",
            "messages": [
                    {"role": "system", "content": mia_persona},
                    {"role": "user", "content": user_input},            ],
        })
    )
    
    if response.status_code == 200:
        resposta = json.loads(response.content).get("choices", [{}])[0].get("message", {}).get("content", "Não sei !")
        st.write(resposta)
    else:
        st.write("tenta de novo!")
