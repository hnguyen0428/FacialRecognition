def calculate_stats(result):
    dict = {}
    if len(result) != 0:
        keys = result[0]['faceAttributes']['emotion'].keys()
        for emotion in keys:
            dict.update({emotion:0.0})

    for item in result:
        keys = item['faceAttributes']['emotion'].keys()
        for emotion in keys:
            dict[emotion] += item['faceAttributes']['emotion'][emotion]
    return dict

def determine_emotion(dict):
    keys = dict.keys()
    largest = 0.0
    general_emotion = ''
    for item in keys:
        if largest < dict[item]:
            largest = dict[item]
            general_emotion = item
    return general_emotion

