from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

filename = "El Hombre De Tu Vida - Capítulo 21 - Parte 2.mp4"

ffmpeg_extract_subclip(
    filename=filename,
    t1=265,
    t2=329,
    targetname=f"crop_{filename}"
)
