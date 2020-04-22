from kivy.properties import StringProperty, ListProperty
from kivy.uix.widget import Widget

from kivymd.uix.list import (
    OneLineAvatarListItem,
    ILeftBody,
    TwoLineAvatarListItem,
    IRightBodyTouch,
    OneLineIconListItem,
)
from kivymd.uix.selectioncontrol import MDCheckbox


class AyeOneLineLeftAvatarItem(OneLineAvatarListItem):
    divider = None
    source = StringProperty()


class AyeTwoLineLeftAvatarItem(TwoLineAvatarListItem):
    icon = StringProperty()
    secondary_font_style = "Caption"


class AyeTwoLineLeftIconItem(TwoLineAvatarListItem):
    icon = StringProperty()


class AyeOneLineLeftIconItem(OneLineAvatarListItem):
    icon = StringProperty()


class AyeOneLineIconListItem(OneLineIconListItem):
    icon = StringProperty()


class AyeOneLineLeftWidgetItem(OneLineAvatarListItem):
    color = ListProperty()


class LeftWidget(ILeftBody, Widget):
    pass


class IconRightSampleWidget(IRightBodyTouch, MDCheckbox):
    pass
