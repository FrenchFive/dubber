print('Hello World')

import os
import uuid
import shutil
import json
import zdubdeepl as deepl
import zdubelevenlabs as elevenlabs
import zdubwhisper as whisper

#SETUP A PROJECT
script_path = os.path.dirname(__file__)
os.makedirs(os.path.join(script_path, 'project'), exist_ok=True)

project_id = str(uuid.uuid4())
project_folder = os.path.join(script_path, 'project', project_id)
os.makedirs(project_folder, exist_ok=True)

video_path = f'{script_path}/test/billieandhugo_short.mp4'

shutil.copy(video_path, f'{project_folder}/original.mp4')
#convert the video to audio
os.system(f'ffmpeg -i {project_folder}/original.mp4 -vn {project_folder}/original.wav')

#WHISPER TRANSCRIPTION 
transcription = whisper.transcription(f'{project_folder}/original.wav')
print(transcription)

extract = transcription['segments']

# dict to json file
with open(f'{project_folder}/transcription.json', 'w') as transcription_file:
    json.dump(extract, transcription_file)


'''
#TRANSLATE THE TRANSCRIPTION 
lang = 'FR'
lang_folder = os.path.join(project_folder, lang)
os.makedirs(lang_folder, exist_ok=True)

translation = deepl.translate('Hello World', lang)
print(translation)

#GENERATE THE AUDIO FILE
version = 1
voiceid = 'pFZP5JQG7iQjIQuC4Bku'
audio_folder = os.path.join(lang_folder, 'audio_files')
os.makedirs(audio_folder, exist_ok=True)

audio = elevenlabs.audio(translation, voiceid)
with open(f'{audio_folder}/elevenlabs_{lang}_{str(version).zfill(5)}.mp3', 'wb') as audio_file:
            audio_file.write(audio)
'''

#MIX THE AUDIO TO THE FILE (FFMEG ??? )