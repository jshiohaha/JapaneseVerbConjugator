from .constants.ParticleConstants import U_PARTICLE, KU_PARTICLE, GU_PARTICLE, SU_PARTICLE, TSU_PARTICLE, NU_PARTICLE, BU_PARTICLE, MU_PARTICLE, RU_PARTICLE

def containsJapaneseCharacters(verb):
    ''' Compute whether or not a Japanese verb contains any kanji characters

    Args:
        verb (str): Japanese verb in kana or kanji

    Returns:
        bool: True if kanji is found, false otherwise
    '''
    ranges = [
        # https://stackoverflow.com/questions/30069846/how-to-find-out-chinese-or-japanese-character-in-a-string-in-python
        {"from": ord(u"\u3300"), "to": ord(u"\u33ff")},         # compatibility ideographs
        {"from": ord(u"\ufe30"), "to": ord(u"\ufe4f")},         # compatibility ideographs
        {"from": ord(u"\uf900"), "to": ord(u"\ufaff")},         # compatibility ideographs
        {"from": ord(u"\U0002F800"), "to": ord(u"\U0002fa1f")}, # compatibility ideographs
        {'from': ord(u'\u3040'), 'to': ord(u'\u309f')},         # Japanese Hiragana
        {"from": ord(u"\u30a0"), "to": ord(u"\u30ff")},         # Japanese Katakana
        {"from": ord(u"\u2e80"), "to": ord(u"\u2eff")},         # cjk radicals supplement
        {"from": ord(u"\u4e00"), "to": ord(u"\u9fff")},
        {"from": ord(u"\u3400"), "to": ord(u"\u4dbf")},
        {"from": ord(u"\U00020000"), "to": ord(u"\U0002a6df")},
        {"from": ord(u"\U0002a700"), "to": ord(u"\U0002b73f")},
        {"from": ord(u"\U0002b740"), "to": ord(u"\U0002b81f")},
        {"from": ord(u"\U0002b820"), "to": ord(u"\U0002ceaf")}  # included as of Unicode 8.0
    ]

    for char in verb:
        if not any([range["from"] <= ord(char) <= range["to"] for range in ranges]):
            return False
    return True

def validateJapaneseVerbDecorator(func):
    def wrapper(self, verb, *args, **kwargs):
        if len(verb) < 2:
            raise Exception("Invalid Japanese Verb Length", len(verb), verb)

        if verb[-1:] not in [U_PARTICLE, KU_PARTICLE, GU_PARTICLE, SU_PARTICLE, TSU_PARTICLE, NU_PARTICLE, BU_PARTICLE, MU_PARTICLE, RU_PARTICLE]:
            raise Exception("Invalid Japanese Verb Ending Particle", verb[-1:])
        
        if not containsJapaneseCharacters(verb):
            raise Exception("Non-Japanese Character Found", verb)

        # assuming *args and **kwargs will always have the correct arguments because initial function call succeeded
        return func(self, verb, *args, **kwargs)
    return wrapper
    