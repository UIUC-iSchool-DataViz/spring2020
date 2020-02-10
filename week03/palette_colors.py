import palettable

def grab_names_palettable(kind="Diverging"):
    return list(palettable.colorbrewer.COLOR_MAPS[kind].keys())

def get_cb_diverging(name = "Spectral", number = 9):
    number = min(number, max(int(_) for _ in palettable.colorbrewer.COLOR_MAPS["Diverging"][name]))
    m = palettable.colorbrewer.get_map(name, map_type="diverging", number=number)
    m.show_discrete_image(size=(12,2))
    m.show_continuous_image(size=(12,2))

def get_cb_qualitative(name = "Set1", number = 9):
    number = min(number, max(int(_) for _ in palettable.colorbrewer.COLOR_MAPS["Qualitative"][name]))
    m = palettable.colorbrewer.get_map(name, map_type="qualitative", number=number)
    m.show_discrete_image(size=(12,2))
    m.show_continuous_image(size=(12,2))

def get_cb_sequential(name = "Blues", number = 9):
    number = min(number, max(int(_) for _ in palettable.colorbrewer.COLOR_MAPS["Sequential"][name]))
    m = palettable.colorbrewer.get_map(name, map_type="sequential", number=number)
    m.show_discrete_image(size=(12,2))
    m.show_continuous_image(size=(12,2))
