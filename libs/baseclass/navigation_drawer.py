from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen

from libs.baseclass.list_items import AyeOneLineLeftIconItem


class AyeNavigationDrawer(Screen):
    def on_enter(self):
        if not self.ids.content_drawer.ids.box_item.children:
            for items in {
                "home-circle-outline": "Home",
                "update": "Check for Update",
                "settings-outline": "Settings",
                "exit-to-app": "Exit",
            }.items():
                self.ids.content_drawer.ids.box_item.add_widget(
                    AyeOneLineLeftIconItem(
                        text=items[1], icon=items[0], divider=None
                    )
                )


class AyeContentNavigationDrawer(BoxLayout):
    pass
