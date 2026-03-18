def change_coords(dict):
    x, y = dict["coords"]
    dict["coords"] = [[x, y], [dict["width"], dict["height"]]]
    return dict


figures = [
    {"width": 7, "height": 6, "color": "blue", "coords": (0, 0)},
    {"width": 5, "height": 4, "color": "red", "coords": (0, 0)},
    {"width": 10, "height": 20, "color": "blue", "coords": (1, -1)}
]

print(figures)

for figure in figures:
    figure = change_coords(figure)
    
print(figures)