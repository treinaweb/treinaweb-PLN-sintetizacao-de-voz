from gtts import gTTS
from playsound import playsound

def cria_audio(mensagem):
    tts = gTTS(mensagem, lang="pt-br")
    tts.save("mensagem.mp3")
    playsound("mensagem.mp3")

# --- Utilização Direta ---
#cria_audio("Palmeiras é o líder do campeonato brasileiro")

# --- Utilização via Input ---
#frase = input("Digite a frase a ser falada \n")
#cria_audio(frase)

# --- Utilização via leitura de arquivo ---
arquivo = open("texto.txt", "r", encoding="utf-8")
conteudo = arquivo.read()
cria_audio(conteudo)