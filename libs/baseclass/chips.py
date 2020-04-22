from kivy.uix.screenmanager import Screen


class AyeChips(Screen):
    def callback_for_menu_items(self, instance, value):
        from kivymd.toast import toast

        toast(value)
