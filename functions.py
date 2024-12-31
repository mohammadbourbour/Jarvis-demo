import os
import pyttsx3
import random
import datetime
import json
import speech_recognition as sr
from termcolor import colored
import pyjokes
import time
import random
import datetime
import json
import string
import requests


class Abilities:
    def __init__(self):
        self.engine = pyttsx3.init()
        self.r = sr.Recognizer()
        self.r.energy_threshold = 400
        self.r.dynamic_energy_threshold = True
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[0].id)
        self.engine.setProperty('rate', 150)
        self.user_info_file = "user_info.json"  
        self.news_api = "Your API Key" # Get it from : https://newsapi.org
        
    def speak(self, text):
        """تبدیل متن به گفتار"""
        try:
            print(colored(f"JARVIS: {text}", color="green"))
            self.engine.say(text)
            self.engine.runAndWait()

        except Exception as e:
            print(f"Error in speak function: {e}")

    def listen(self):
        """تبدیل گفتار به متن"""
        with sr.Microphone() as source:
            print(colored("\nListening...", color="red"))
            audio = self.r.listen(source)
            try:
                recognized_text = self.r.recognize_google(audio)
                print(colored(f"\nYou: {recognized_text}\n", color="yellow"))
                return recognized_text
            except sr.UnknownValueError:
                print(colored("\nCould not understand audio", color="red"))
            except sr.RequestError as e:
                print(f"Could not request results:\n {e}")
        return None

    def get_user_info(self):
        """گرفتن اطلاعات کاربر"""
        if not os.path.exists(self.user_info_file):
            self.speak("Hello, I am Jarvis, your personal assistant. What should I call you?")
            user_name = input("Your name: ").strip()

            self.speak("Nice to meet you! How old are you?")
            user_age = input("Your age: ").strip()

            self.speak("Which country are you in?")
            user_country = input("Your country: ").strip()

            self.speak(f"Great! And which city in {user_country}?")
            user_city = input("Your city: ").strip()

            user_info = {
                "name": user_name,
                "age": user_age,
                "country": user_country,
                "city": user_city
            }
            with open(self.user_info_file, "w") as f:
                json.dump(user_info, f)

            self.speak(f"Thank you, {user_name}. Your details have been saved.")
            return user_info
        else:
            with open(self.user_info_file, "r") as f:
                user_info = json.load(f)
                return user_info

    def greet_user(self, user_info):
        """خوشامدگویی بر اساس اطلاعات کاربر"""
        now = datetime.datetime.now()
        hour = now.hour
        greeting = "Good night"
        if hour < 12:
            greeting = "Good morning"
        elif hour < 18:
            greeting = "Good afternoon"

        self.speak(f"Hi {user_info['name']}! {greeting}. How can I assist you today?")
        
    def tell_joke(self):
        joke = pyjokes.get_joke()
        self.speak(joke)

    def greet(self):
        """خوشامدگویی به کاربر"""
        greetings = ["Hello! How can I help you?", "Hi there! What can I do for you?"]
        self.speak(random.choice(greetings))

    def exit(self):
        """خروج از برنامه"""
        farewells = ["Goodbye! Have a great day!", "Bye! See you soon!"]
        self.speak(random.choice(farewells))
        exit()

    def get_time(self):
        """گرفتن زمان فعلی"""
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        self.speak(f"The current time is {current_time}")

    def motivate_user(self):
        """انگیزه دادن به کاربر"""
        motivational_quotes = [
            "The best way to get started is to quit talking and begin doing.",
            "Don’t let yesterday take up too much of today.",
            "You learn more from failure than from success.",
            "The only limit to our realization of tomorrow is our doubts of today."
        ]
        self.speak(random.choice(motivational_quotes))

    def focus_mode(self):
        """تکنیک پومودورو"""
        self.speak("Focus mode activated. Starting a 25-minute timer.")
        time.sleep(25 * 60)
        self.speak("Time's up! Take a 5-minute break.")

    def play_music(self):
        """پخش موزیک"""
        self.speak("Playing your favorite music.")
        music_dir = "/music" 
        if os.path.exists(music_dir):
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, random.choice(songs)))
        else:
            self.speak("Music directory not found. Please check the path.")

    def generate_password(self):
        """ساخت پسوورد قوی"""
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(12))
        self.speak(f"Your new password is: {password}")
        return password

    def get_news(self):
        """خواندن سرخط خبر ها"""
        self.speak("Fetching the latest news headlines.")
        api_key = self.news_api 
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
        response = requests.get(url).json()
        headlines = [article['title'] for article in response.get('articles', [])[:5]]
        for headline in headlines:
            self.speak(headline)

    def tell_story(self):
        """داستان تعریف کردن"""
        stories = [
            "Once upon a time, in a small village, there was a brave boy who saved his town from a wildfire...",
            "There was a curious cat who always wanted to explore the world beyond the mountains...",
            "Long ago, in a hidden forest, there lived a magical bird that granted wishes..."
        ]
        self.speak(random.choice(stories))

    def exercise_guide(self):
        """تمرین ورزشی"""
        exercises = [
            "Do 10 push-ups.",
            "Stretch your arms and legs for 5 minutes.",
            "Take a short walk around your room.",
            "Do 15 jumping jacks."
        ]
        self.speak(random.choice(exercises))

    def random_fact(self):
        
        facts = [
            "Did you know? Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old!",
            "The shortest war in history was between Britain and Zanzibar on August 27, 1896. Zanzibar surrendered after 38 minutes.",
            "Octopuses have three hearts, and two of them stop beating when they swim."
        ]
        self.speak(random.choice(facts))

    def set_daily_goal(self):
        """تعیین هدف روزانه"""
        self.speak("What is your main goal for today?")
        goal = self.listen()
        self.speak(f"Got it. Your goal for today is: {goal}. Let's work towards it!")
        with open("daily_goal.txt", "w") as f:
            f.write(goal)
