import os

from kivy.properties import ObjectProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen

from demos.Aye.libs.baseclass.list_items import (
    AyeOneLineLeftAvatarItem,
)
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineAvatarIconListItem


class AyeDialogsCustomContent(BoxLayout):
    pass


class AyeItemConfirm(OneLineAvatarIconListItem):
    divider = None

    def set_icon(self, instance_check):
        instance_check.active = True
        check_list = instance_check.get_widgets(instance_check.group)
        for check in check_list:
            if check != instance_check:
                check.active = False


class AyeDialogs(Screen):
    app = ObjectProperty()
    simple_dialog = None
    alert_dialog = None
    custom_dialog = None
    confirmation_dialog = None

    def show_example_confirmation_dialog(self):
        if not self.confirmation_dialog:
            self.confirmation_dialog = MDDialog(
                title="Phone ringtone",
                type="confirmation",
                items=[
                    AyeItemConfirm(text="Callisto"),
                    AyeItemConfirm(text="Luna"),
                    AyeItemConfirm(text="Night"),
                    AyeItemConfirm(text="Solo"),
                    AyeItemConfirm(text="Phobos"),
                    AyeItemConfirm(text="Diamond"),
                    AyeItemConfirm(text="Sirena"),
                    AyeItemConfirm(text="Red music"),
                    AyeItemConfirm(text="Allergio"),
                    AyeItemConfirm(text="Magic"),
                    AyeItemConfirm(text="Tic-tac"),
                ],
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        text_color=self.app.theme_cls.primary_color,
                    ),
                    MDFlatButton(
                        text="OK", text_color=self.app.theme_cls.primary_color
                    ),
                ],
            )
        self.confirmation_dialog.open()

    def show_example_simple_dialog(self):
        if not self.simple_dialog:
            self.simple_dialog = MDDialog(
                title="Set backup account",
                type="simple",
                items=[
                    AyeOneLineLeftAvatarItem(
                        text="user01@gmail.com",
                        source=f"{os.environ['Aye_ASSETS']}heattheatr.png",
                    ),
                    AyeOneLineLeftAvatarItem(
                        text="user02@gmail.com",
                        source=f"{os.environ['Aye_ASSETS']}mountaino.png",
                    ),
                    AyeOneLineLeftAvatarItem(
                        text="Add account",
                        source=f"{os.environ['Aye_ASSETS']}twitter-round.png",
                    ),
                ],
            )
        self.simple_dialog.open()

    def show_example_custom_dialog(self):
        if not self.custom_dialog:
            self.custom_dialog = MDDialog(
                title="Address:",
                type="custom",
                content_cls=AyeDialogsCustomContent(),
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        text_color=self.app.theme_cls.primary_color,
                    ),
                    MDFlatButton(
                        text="OK", text_color=self.app.theme_cls.primary_color
                    ),
                ],
            )
        self.custom_dialog.open()

    def show_example_alert_dialog(self):
        if not self.alert_dialog:
            self.alert_dialog = MDDialog(
                title="Reset settings?",
                text="This will reset your device to its default factory settings.",
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        text_color=self.app.theme_cls.primary_color,
                    ),
                    MDFlatButton(
                        text="ACCEPT",
                        text_color=self.app.theme_cls.primary_color,
                    ),
                ],
            )
        self.alert_dialog.open()
