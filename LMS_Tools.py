from canvasapi import Canvas
import config

canvas = Canvas(API_URL, API_KEY)

user = canvas.get_user(161540)
print(user)
