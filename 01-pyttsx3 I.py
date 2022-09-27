import pyttsx3

engine = pyttsx3.init()
engine.setProperty("voice", "brazil")
engine.say("Olá mundo. Seja bem vindo à linguagem Python")
engine.runAndWait()