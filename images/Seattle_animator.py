import os

frame_rate=10
file_name='Seattle'
file_end='.png'
moviename=file_name+".mp4"
# e.g do: ffmpeg -r 10 -i Seattle_%d.png Seattle.mp4
ffmpegCmd = 'ffmpeg -r {:d} -i {:s}_%d.png {:s}'.format(frame_rate,file_name,moviename) #reads in all files in current directory
print(ffmpegCmd)
os.system( ffmpegCmd )
