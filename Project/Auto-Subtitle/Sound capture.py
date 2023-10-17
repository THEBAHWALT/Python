from moviepy.editor import VideoFileClip

input_file = "C:\\Users\\walt314\\Downloads\\Weekly Report_1016_20231016-01.mp4"    #要截取的音檔
output_file = "C:\\Users\\walt314\\Downloads\\Weekly Report_1016_20231016-01.wav"   #擷取後的音檔

video = VideoFileClip(input_file)
audio = video.audio
audio.write_audiofile(output_file)

print("音檔擷取完成")