import os

from kivy.uix.modalview import ModalView
from kivy.utils import get_color_from_hex, get_hex_from_color

from kivymd.color_definitions import palette, colors
from kivymd.theming import ThemableBehavior


class AyeBaseDialog(ThemableBehavior, ModalView):
    pass


class AyeDialogDev(AyeBaseDialog):
    pass


class AyeDialogLicense(AyeBaseDialog):
    def on_open(self):
        with open(
            os.path.join(os.environ["Aye_ROOT"], "LICENSE"),
            encoding="utf-8",
        ) as license:
            self.ids.text_label.text = license.read().format(
                COLOR=get_hex_from_color(self.theme_cls.primary_color)
            )


class AyeDialogChangeTheme(AyeBaseDialog):
    def set_list_colors_themes(self):
        for name_theme in palette:
            self.ids.rv.data.append(
                {
                    "viewclass": "AyeOneLineLeftWidgetItem",
                    "color": get_color_from_hex(colors[name_theme]["500"]),
                    "text": name_theme,
                }
            )
