from core.listener import listen


print("================================")
print("       VOICE OS - LISTENER")
print("================================")
print("Speak something...\n")


while True:

    text = listen()

    if text.lower() == "exit":
        print("Voice OS shutting down...")
        break