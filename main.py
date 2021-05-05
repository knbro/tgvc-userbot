# import logging
from os import environ

from pyrogram import Client, idle

API_ID = int(environ["3626638"])
API_HASH = environ["7f7fb4f0479bb0fa47efa8005a0cc8d9"]
SESSION_NAME = environ["AQCBA-2BWb12efBwyUtX6ZWh8YvqLY84fiMxaUcBbk2T1LjvIjuHGzD3JSfKRl8waFCGnuQrx7b-MpaT7nQfFZ2j5jV9rbVUUVYCQ86ntCVNaNGXtTOK9qry8FnYobRB3aAmhiDGnL5zZ0hKEjSmT8EStw3kn9bx6qT9caAzwHBerNBfvRY4_wigFeFY4-xxRNL_uPedEa5YHI8jNNbYKCl8ksvdg236oeqHIgTP7_Ik6pxC7QQNkG786MHW48d1yKoPqUgFP38qeaB2orDFGqcz5i_Ce7nx5F7nc7w2-9yAN0APgMzesOxMSLHPFCgoFS8SvAC7iv1wWr7FiFxni1RjYG0zYAA"]

PLUGINS = dict(
    root="plugins",
    include=[
        "vc.player",
        "ping",
        "sysinfo"
    ]
)

app = Client(SESSION_NAME, API_ID, API_HASH, plugins=PLUGINS)
# logging.basicConfig(level=logging.INFO)
app.start()
print('>>> USERBOT STARTED')
idle()
app.stop()
print('\n>>> USERBOT STOPPED')
