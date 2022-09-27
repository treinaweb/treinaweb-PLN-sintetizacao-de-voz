import pyttsx3

engine = pyttsx3.init()
engine.setProperty("voice", "brazil")
frase = input("Digite a frase\n")
engine.say(frase)
engine.runAndWait()