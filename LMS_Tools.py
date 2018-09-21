from canvasapi import Canvas
import config

canvas = Canvas(config.API_URL, config.API_KEY)

user = canvas.get_user(161540)
print(user)
