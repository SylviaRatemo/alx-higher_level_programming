#!usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        sentence[0] = None
    new_t = (len(sentence), sentence[0])
    return (new_t)
