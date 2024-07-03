from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
import json
import glob
import random
from pathlib import Path
from datetime import datetime

Builder.load_file("design.kv")


class LoginScreen(Screen):
    def sign_up(self):
        self.manager.current = "Signup_Screen"

    def login(self, uname, pword):
        with open("users.json") as file:
            users = json.load(file)
        if uname in users and users[uname]['password'] == pword:
            self.manager.current = "Login_Screen_Success"
        else:
            self.ids.login_wrong.text = "Wrong Username or Password"


class SignupScreen(Screen):
    def add_user(self, uname, pword):
        with open("users.json") as file:
            users = json.load(file)
        users[uname] = {"username": uname, "password": pword,
                        "created": datetime.now().strftime("%y-%m-%d %H-%M-%S")}

        with open("users.json", 'w') as file:
            json.dump(users, file)
            self.manager.current = "Signup_Success_Screen"


class SignupSuccessScreen(Screen):
    def go_to_login(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "Login_Screen"


class LoginScreenSuccess(Screen):
    def log_out(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "Login_Screen"

    def get_quote(self, feel):
        feel = feel.lower()
        available_feelings = glob.glob("quotes/*txt")

        available_feelings = [Path(filename).stem for filename
                              in available_feelings]

        if feel in available_feelings:
            with open(f"quotes/{feel}.txt", errors='ignore') as file:
                quotes = file.readlines()
            self.ids.quote.text = random.choice(quotes)
        else:
            self.ids.quote.text = "Try another feeling"


class RootWidget(ScreenManager):
    pass


class ImageButton(ButtonBehavior, HoverBehavior, Image):
    pass


class MainApp(App):
    def build(self):
        return RootWidget()


if __name__ == "__main__":
    MainApp().run()
