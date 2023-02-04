import subprocess



command = [r'D:\ffmpeg-2022-05-12-git-30e2bb0f64-essentials_build\bin\ffmpeg.exe', '-y', '-i', r'D:\F1_playground\ver_lap_edited.mp4', '-i', r'D:\F1_playground\telemetry.mp4', 
           '-filter_complex', '[0:v]setpts=PTS-STARTPTS[va];[1:v]scale=1920x1080,setsar=1,setpts=PTS-STARTPTS,fps=50.00[vb];[va][vb]hstack=inputs=2',
           '-vsync', 'vfr', 'output.mp4']



# def ffmpeg_command_concat(ffmpeg_path, bev_video_path, out_file_path, out_file_path_cut, fps):
#     bev_video = f'{ffmpeg_path} -y -vsync 2 -r {fps:0.01f} -i "{bev_video_path}"'
#     camera_video = f'-i "{out_file_path_cut}"' ' -filter_complex "[1][0]scale2ref=oh*mdar:ih[camera][bev];[camera][bev]hstack"'
#     output_file = f'"{out_file_path}"'
#     commands_arr = [bev_video, camera_video, output_file]

#     return ' '.join(commands_arr)

# bev_command = ffmpeg_command_concat(ffmpeg_path = r'D:\ffmpeg-2022-05-12-git-30e2bb0f64-essentials_build\bin\ffmpeg.exe', 
#                                     bev_video_path = r'D:\F1_playground\telemetry.mp4', #r'D:\F1_playground\ver_lap_edited.mp4', 
#                                     out_file_path = r'D:\F1_playground\output.mp4', 
#                                     out_file_path_cut= r'D:\F1_playground\ver_lap_edited.mp4',  
#                                     fps = 50)
# subprocess.run(bev_command)



subout = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
print(subout.stdout)