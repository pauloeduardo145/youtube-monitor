import feedparser
import time
import subprocess

CANAL_ID = ""

URL = f"https://youtube.com/feeds/videos.xml?channel_id{CANAL_ID}"

ultimo_video = None

while True:
    try:
        feed = feedparser.parse(URL)

        if not feed.entries:
            print("Nenhum video encontrado.")
            time.sleep(60)
            continue

        video = feed.entries[0]

        titulo = video.title
        link = video.link

        if ultimo_video is None:
            ultimo_video = link
            print("Monitorando o canal...")

        elif link != ultimo_video:
            ultimo_video = link

            subprocess.run([
                "termux-notification",
                "--title", "Novo video!",
                "--content", titulo
            )]

            print(f"Novo video: {titulo}")
            print(link)

        time.sleep(300)

    except Exception as erro:

        print("Erro:",erro)
        time.sleep(60) 
