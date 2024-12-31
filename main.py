import os
import sys
import time
import pyfiglet
from functions import Abilities


class JarvisAssistant:
    def __init__(self):
        self.abilities = Abilities()

        self.intent_keywords = {
            "greet": ["hello", "hi", "hey", "good morning", "good afternoon"],
            "time_command": ["time", "what time is it", "current time"],
            "joke": ["joke", "make me laugh", "tell me a joke"],
            "exit_command": ["exit", "bye", "quit", "goodbye"],
            "motivate_user": ["motivate me", "motivation", "inspire me"],
            "focus_mode": ["focus mode", "start focus", "pomodoro"],
            "play_music": ["play music", "start music", "music"],
            "generate_password": ["generate password", "create password", "password"],
            "news_headlines": ["news", "latest news", "headlines"],
            "tell_story": ["tell me a story", "story", "bedtime story"],
            "exercise_guide": ["exercise", "workout", "fitness"],
            "random_fact": ["random fact", "tell me a fact", "fact"],
            "daily_goal": ["daily goal", "set goal", "goal for today"]

        }

    @staticmethod
    def display_banner(self, message="JARVIS"):
        banner_text = pyfiglet.figlet_format(message)
        print(banner_text)
        print(f"Welcome to {message}!")

    def detect_intent(self, user_input):
        for intent, keywords in self.intent_keywords.items():
            for keyword in keywords:
                if keyword in user_input.lower():
                    return intent
        return "unknown"

    def perform_action(self, intent):
        if intent == "greet":
            self.abilities.greet()
        elif intent == "time_command":
            self.abilities.get_time()
        elif intent == "joke":
            self.abilities.tell_joke()
        elif intent == "exit_command":
            self.abilities.exit()
        elif intent == "motivate_user":
            self.abilities.motivate_user()
        elif intent == "focus_mode":
            self.abilities.focus_mode()
        elif intent == "play_music":
            self.abilities.play_music()
        elif intent == "generate_password":
            self.abilities.generate_password()
        elif intent == "news_headlines":
            self.abilities.get_news()
        elif intent == "tell_story":
            self.abilities.tell_story()
        elif intent == "exercise_guide":
            self.abilities.exercise_guide()
        elif intent == "random_fact":
            self.abilities.random_fact()
        elif intent == "daily_goal":
            self.abilities.set_daily_goal()
        else:
            self.abilities.speak("I didn't understand that. Please try again.")

    def run(self, mode="voice"):

        time.sleep(2)

        try:
            while True:
                user_input = self.abilities.listen() if mode == "voice" else input("Type your input: ").strip()
                if user_input:
                    intent = self.detect_intent(user_input)
                    self.perform_action(intent)
        except KeyboardInterrupt:
            self.abilities.speak("Goodbye!")
            sys.exit()
        except Exception as e:
            print(f"Error: {str(e)}")


if __name__ == '__main__':
    os.system('cls')
    assistant = JarvisAssistant()

    assistant.user_info = assistant.abilities.get_user_info()

    assistant.display_banner()
    assistant.abilities.greet_user(assistant.user_info)
    mode = input("Enter 1 for Chat Mode or 2 for Voice Mode: ").strip()
    assistant.run(mode="chat" if mode == "1" else "voice")
