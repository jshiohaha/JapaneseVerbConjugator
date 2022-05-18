from .constants.ParticleConstants import BU_PARTICLE
from .constants.ParticleConstants import GU_PARTICLE
from .constants.ParticleConstants import KU_PARTICLE
from .constants.ParticleConstants import MU_PARTICLE
from .constants.ParticleConstants import NU_PARTICLE
from .constants.ParticleConstants import RU_PARTICLE
from .constants.ParticleConstants import SU_PARTICLE
from .constants.ParticleConstants import TSU_PARTICLE
from .constants.ParticleConstants import U_PARTICLE


def containsJapaneseCharacters(verb):
    """Compute whether or not a Japanese verb contains any kanji characters

    Args:
        verb (str): Japanese verb in kana or kanji

    Returns:
        bool: True if kanji is found, false otherwise
    """
    ranges = [
        # https://stackoverflow.com/questions/30069846/how-to-find-out-chinese-or-japanese-character-in-a-string-in-python
        # compatibility ideographs
        {
            "from": ord("\u3300"),
            "to": ord("\u33ff")
        },
        # compatibility ideographs
        {
            "from": ord("\ufe30"),
            "to": ord("\ufe4f")
        },
        # compatibility ideographs
        {
            "from": ord("\uf900"),
            "to": ord("\ufaff")
        },
        # compatibility ideographs
        {
            "from": ord("\U0002F800"),
            "to": ord("\U0002fa1f")
        },
        {
            "from": ord("\u3040"),
            "to": ord("\u309f")
        },  # Japanese Hiragana
        {
            "from": ord("\u30a0"),
            "to": ord("\u30ff")
        },  # Japanese Katakana
        # cjk radicals supplement
        {
            "from": ord("\u2e80"),
            "to": ord("\u2eff")
        },
        {
            "from": ord("\u4e00"),
            "to": ord("\u9fff")
        },
        {
            "from": ord("\u3400"),
            "to": ord("\u4dbf")
        },
        {
            "from": ord("\U00020000"),
            "to": ord("\U0002a6df")
        },
        {
            "from": ord("\U0002a700"),
            "to": ord("\U0002b73f")
        },
        {
            "from": ord("\U0002b740"),
            "to": ord("\U0002b81f")
        },
        # included as of Unicode 8.0
        {
            "from": ord("\U0002b820"),
            "to": ord("\U0002ceaf")
        },
    ]

    for char in verb:
        if not any(
            [range["from"] <= ord(char) <= range["to"] for range in ranges]):
            return False
    return True


def validateJapaneseVerbDecorator(func):

    def wrapper(self, verb, *args, **kwargs):
        if len(verb) < 2:
            raise Exception("Invalid Japanese Verb Length", len(verb), verb)

        if verb[-1:] not in [
                U_PARTICLE,
                KU_PARTICLE,
                GU_PARTICLE,
                SU_PARTICLE,
                TSU_PARTICLE,
                NU_PARTICLE,
                BU_PARTICLE,
                MU_PARTICLE,
                RU_PARTICLE,
        ]:
            raise Exception("Invalid Japanese Verb Ending Particle", verb[-1:])

        if not containsJapaneseCharacters(verb):
            raise Exception("Non-Japanese Character Found", verb)

        # assuming *args and **kwargs will always have the correct arguments because initial function call succeeded
        return func(self, verb, *args, **kwargs)

    return wrapper
