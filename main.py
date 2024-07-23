print('Hello World')

import os
import uuid
import shutil
import json
from unidecode import unidecode
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

transcription = transcription['segments']
# dict to json file
with open(f'{project_folder}/transcription.json', 'w') as transcription_file:
    json.dump(transcription, transcription_file)

langs = ['FR', 'ES', 'IT',]

for lang in langs:
    #TRANSLATE THE TRANSCRIPTION 
    lang_folder = os.path.join(project_folder, lang)
    os.makedirs(lang_folder, exist_ok=True)

    lang_transcription = transcription
    for segment in lang_transcription:
        translation = deepl.translate(segment['text'], lang)
        segment['text'] = unidecode(str(translation))
    
    # dict to json file
    with open(f'{lang_folder}/transcription.json', 'w') as transcription_file:
        json.dump(lang_transcription, transcription_file)
    
for lang in langs:
    lang_folder = os.path.join(project_folder, lang)
    with open(f'{lang_folder}/transcription.json', 'r') as json_file:
        lang_transcription = json.load(json_file)
    
    count = 0
    audio_folder = os.path.join(lang_folder, 'audio_files')
    os.makedirs(audio_folder, exist_ok=True)
    
    for segment in lang_transcription:
        count += 1
        voiceid = 'XrExE9yKIg1WjnnlVkGX'

        text = unidecode(str(segment['text']))

        audio = elevenlabs.audio(text, voiceid, (lang.lower()))
        with open(f'{audio_folder}/elevenlabs_{lang}_{str(count).zfill(5)}.mp3', 'wb') as audio_file:
            audio_file.write(audio)
        
        
#MIX THE AUDIO TO THE FILE (FFMEG ??? )