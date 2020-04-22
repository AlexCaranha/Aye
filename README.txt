Componentes a utilizar:
Snackbar: barra que aparece momentaneamente na parte inferior.

MDTextField:
    hint_text: "Helper text on focus"
    helper_text: "This will disappear when you click off"
    helper_text_mode: "on_focus"

AyeBottomSheetItemButton:
    text: "Open custom bottom sheet"
    callback: lambda: root.show_example_custom_bottom_sheet("custom")
    pos_hint: {"center_y": .35}

Expansion Panel
    ...

