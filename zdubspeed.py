import os 
def speed(path):
    import json
    from pydub import AudioSegment
    
    audio_files = []
    for file in os.listdir(path+'/audio_files'):
        if file.endswith('.mp3'):
            audio_files.append(file)

    with open(f'{path}/transcription.json', 'r') as json_file:
        transcription = json.load(json_file)
    
    count = 0
    for segment in transcription:
        duration = segment['end'] - segment['start']
        ac_duration = AudioSegment.from_file(f'{path}/audio_files/{audio_files[count]}').duration_seconds
        print(f'{audio_files[count]} :: {ac_duration} :: {duration}')
        if ac_duration > duration:
            audio = AudioSegment.from_file(f'{path}/audio_files/{audio_files[count]}')
            audio = audio.speedup(playback_speed=ac_duration/duration)
            audio.export(f'{path}/audio_files/{audio_files[count]}', format='mp3')
            ac_duration = AudioSegment.from_file(f'{path}/audio_files/{audio_files[count]}').duration_seconds
            print(f'{audio_files[count]} :: {ac_duration} :: {duration}')
        count += 1



script_path = os.path.dirname(__file__)
lang = 'ES'
path = f'{script_path}/project/270855f2-d3b0-41ac-9235-083346bb3725/{lang}'
speed(path)