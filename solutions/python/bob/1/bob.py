def response(hey_bob):
    responses = ["Sure.", "Whoa, chill out!", "Calm down, I know what I'm doing!", "Fine. Be that way!", "Whatever."]
    if len(hey_bob) != 0:
        if(hey_bob.isspace()):
            is_question = False
        else:
            is_question = hey_bob.strip()[-1] == "?"
    else:
        is_question = False
    is_yell = hey_bob.isupper()
    is_question_yell = is_question and hey_bob.isupper()
    is_silence = hey_bob == "" or hey_bob.isspace()
    if(is_question_yell):
        return responses[2]
    elif(is_question):
        return responses[0]
    elif(is_yell):
        return responses[1]
    elif(is_silence):
        return responses[3]
    return responses[4]