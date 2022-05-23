from datetime import datetime
from time import strftime

def decabot_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "Sup?", "Sup", "how far?", "how far", "what's good?", "what's good"):
        return "Hey! How's it going?"

    # if user_message in ("Who are you", "Who are you?"):
    #     return "I am Decabot, Warden of Decaden, Pleasure to make your acquiantance"

    if user_message in ("time", "time?"):
        now = datetime.now()
        date_time = now.strftime("%H:%M, %d/%m")

        return str(date_time)

    return "I don't understand you"