import os
import uuid
import asyncio
import edge_tts
from playsound import playsound


async def speak(text: str):
    output_file = f"speech_{uuid.uuid4().hex}.mp3"
    communicate = edge_tts.Communicate(text, "en-US-AriaNeural")
    
    await communicate.save(output_file)
    
    playsound(output_file)
    os.remove(output_file)
    
    await asyncio.sleep(0.1)
    
def speak_sync(text: str):
    asyncio.run(speak(text))