class Camera:
    def take_photo(self):
        print("Photo taken")

class Phone:
    def make_call(self):
        print("Calling someone")

class SmartPhone(Camera, Phone):
    def use_apps(self):
        print("Opening an app")

mobile = SmartPhone()
mobile.take_photo()
mobile.make_call()
mobile.use_apps()
