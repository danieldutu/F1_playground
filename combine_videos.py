import subprocess



command = [r'D:\ffmpeg-2022-05-12-git-30e2bb0f64-essentials_build\bin\ffmpeg.exe', '-y', '-i', r'D:\F1_playground\ver_lap_edited.mp4', '-i', r'D:\F1_playground\telemetry.mp4', 
           '-filter_complex', '[0:v]setpts=PTS-STARTPTS[va];[1:v]scale=1920x1080,setsar=1,setpts=PTS-STARTPTS,fps=50.00[vb];[va][vb]hstack=inputs=2',
           '-vsync', 'vfr', 'output.mp4']


subout = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
print(subout.stdout)