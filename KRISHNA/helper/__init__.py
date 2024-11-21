import os
import sys
from pyrogram import Client



def restart():
    os.execvp(sys.executable, [sys.executable, "-m", "KRISHNA"])

async def join(client):
    try:
        await client.join_chat("GOSIP_PLANET")
    except BaseException:
        pass
