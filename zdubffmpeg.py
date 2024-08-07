from pydub import AudioSegment
import json
import os


#from a path get all the audio files in a list
def get_audio_files(path):
    audio_files = []
    for file in os.listdir(path):
        if file.endswith('.mp3'):
            audio_files.append(file)
    return(audio_files)

script_path = os.path.dirname(__file__)
lang = 'FR'
path = f'{script_path}/project/a0a3d89f-80c6-43d5-99ec-535a71a4c9ac/{lang}/audio_files'
audio_files = get_audio_files(path)

lang_folder = f'{script_path}/project/a0a3d89f-80c6-43d5-99ec-535a71a4c9ac/{lang}'
with open(f'{lang_folder}/transcription.json', 'r') as json_file:
    lang_transcription = json.load(json_file)

original_audio_file = f'{script_path}/project/a0a3d89f-80c6-43d5-99ec-535a71a4c9ac/original.wav'
duration = AudioSegment.from_file(original_audio_file).duration_seconds * 1000
print(duration)

combined = AudioSegment.silent(duration=duration)

count = 0
for segment in lang_transcription:
    print(f'{audio_files[count]} :: {segment["start"]} :: {segment["text"]}')
    audio = AudioSegment.from_file(f'{path}/{audio_files[count]}')
    combined = combined.overlay(audio, position=segment['start']*1000)
    count += 1

combined.export(f"{lang_folder}/{lang}_audio.mp3", format="mp3")