# Video Editing
# pip install moviepy
from moviepy.editor import *
# Triming the video
clip_1 = VideoFileClip("sample_video.mp4").subclip(40, 50)
clip_2 = VideoFileClip("sample_video.mp4").subclip(68, 91)
final_clip = concatenate_videoclips([clip_1, clip_2])
final_clip.write_videofile("output.mp4")
# Adding VFX
clip_1 = (VideoFileClip("sample_video.mp4").subclip(40,
50).fx(vfx.colorx, 1.2).fx(vfx.lum_contrast, 0, 30, 100))
clip_2 = (VideoFileClip("sample_video.mp4").subclip(68,
91).fx(vfx.invert_colors))
final_clip = concatenate_videoclips([clip_1, clip_2])
final_clip.write_videofile("output.mp4")

# Add Audio to Video
clip = VideoFileClip("sample_video.mp4")
# Add audio to only first 5 sec
clip = clip.subclip(0, 5)
audioclip = AudioFileClip("audio.mp3").subclip(0, 5)
videoclip = clip.set_audio(audioclip)
final_clip.write_videofile("output.mp4")