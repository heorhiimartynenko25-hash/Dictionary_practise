import sys
# why key? but bread taste better than key...
rectangle = {
    "width": 7,
    "height": 6,
    "color" : "blue",
    "coords" : (0, 0)
}
#if he was green, he would die...
if rectangle["color"] == "green":
    print("x_x")
    sys.exit()
print("I'm blue, if I was green, I would die.")

rectangle["area"] = rectangle.get("width") * rectangle.get("height")
rectangle["perimeter"] = 2 * (rectangle.get("width") * rectangle.get("height"))

print(rectangle)
