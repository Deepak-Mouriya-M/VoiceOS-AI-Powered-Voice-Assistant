import speech_recognition as sr


recognizer = sr.Recognizer()

recognizer.energy_threshold = 400
recognizer.dynamic_energy_threshold = True
recognizer.pause_threshold = 0.8


def listen():

    try:
        with sr.Microphone() as source:

            print("Listening...")

            recognizer.adjust_for_ambient_noise(
                source,
                duration=0.5
            )

            try:
                audio = recognizer.listen(
                    source,
                    timeout=5,
                    phrase_time_limit=6
                )

            except sr.WaitTimeoutError:
                print("No speech detected.")
                return ""

    except Exception as e:
        print(f"Microphone error: {e}")
        return ""

    try:

        text = recognizer.recognize_google(audio)

        print(f"You: {text}")

        return text

    except sr.UnknownValueError:

        print("Sorry, I couldn't understand that.")
        return ""

    except sr.RequestError as e:

        print(f"Speech recognition error: {e}")
        return ""

    except Exception as e:

        print(f"Recognition error: {e}")
        return ""