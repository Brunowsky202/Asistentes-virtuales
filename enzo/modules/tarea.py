import os
import google.generativeai as genai 
import urllib.parse
import urllib
import webbrowser
import yt_dlp 

funtions=[]
API_KEY="AIzaSyD--kHOT3Vp6QiuaXNyBA_Zx0L6CQ-lUls"
genai.configure(api_key=API_KEY)

config={
    "temperature":0.8,
    "top_p":0.95,
    "top_k":64,
    "max_output_tokens":8192,
    "response_mine_type":"text/plain"
}
activado=False
def buscar_en_liena_o_en_la_web(busqueda:str):
    global activado
    """buscar en liena
    description: es una funcion que va a buscar en navegador
    lo que se 
    le indique cuando el usuaria diga 'que es...'  
    args: 
    busqueda:la busqueda de que el usario indique """

    url=f"https://www.youtube.com/results?search_query={urllib.parse.quote(busqueda)}" 
    os.system(f"start msedge {url}")
    download_video(url)
    activado=True

model= genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config =config,
    tools=[buscar_en_liena_o_en_la_web]
)
chat=model.start_chat(enable_automatic_function_calling=True)
def answer(text:str):
    result=chat.send_message(text)
    return result.text.replace("*","").replace("/","")

video= input('busqueda:')
buscar_en_liena_o_en_la_web(video)

def download_video(video_url):
        yld_ops= {
            'format': 'bestvideo',
            'outtmpl':'%(title)s.%(ext)s',
            'mergue_output_format': 'mp4'
        }
        try:
            with yt_dlp.YoutubeDL(yld_ops) as ydl:
                ydl.download([video_url])
            print("listo")
        except Exception as e:
            print("esta malo"[e])
