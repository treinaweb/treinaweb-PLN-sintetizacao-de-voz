import pyttsx3
engine = pyttsx3.init()

arquivo = open("texto.txt", "r", encoding="utf-8")
conteudo = arquivo.read()

engine.setProperty("voice", "brazil")
engine.say(conteudo)
engine.runAndWait()