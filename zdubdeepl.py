def translate(text, lang):
    import deepl

    #get authkey from a file
    with open('deepl.secret', 'r') as file:
        authkey = file.read().replace('\n', '')
    
    translator = deepl.Translator(authkey)
    result = translator.translate_text(text, target_lang=lang)
    return(result)