def transcription(path):
    import whisper

    model = whisper.load_model("base")
    result = model.transcribe(path)

    return(result)

