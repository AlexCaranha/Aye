Componentes a utilizar:
Snackbar: barra que aparece momentaneamente na parte inferior.

MDToolbar:
    title: "Simple toolbar"
    pos_hint: {'center_x': .5, 'center_y': .75}
    md_bg_color: get_color_from_hex(colors['Teal']['500'])
    background_palette: 'Teal'
    background_hue: '500'

MDTextField:
    hint_text: "Helper text on focus"
    helper_text: "This will disappear when you click off"
    helper_text_mode: "on_focus"

AyeBottomSheetItemButton:
    text: "Open custom bottom sheet"
    callback: lambda: root.show_example_custom_bottom_sheet("custom")
    pos_hint: {"center_y": .35}

TwoLineAvatarListItem:
    type: "two-line"
    text: "Two-line item..."
    secondary_text: "with avatar"
    ImageLeftWidget:
        source: f'{environ["Aye_ASSETS"]}avatar.png'

Expansion Panel
    ...

