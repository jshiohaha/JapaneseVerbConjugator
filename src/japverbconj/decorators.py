from .exceptions import (
    InvalidJapaneseVerbEndingError,
    InvalidJapaneseVerbLengthError,
    NonJapaneseCharacterError,
)
from .constants.particle_constants import (
    BU_PARTICLE,
    GU_PARTICLE,
    KU_PARTICLE,
    MU_PARTICLE,
    NU_PARTICLE,
    RU_PARTICLE,
    SU_PARTICLE,
    TSU_PARTICLE,
    U_PARTICLE,
)


def contains_only_japanese_characters(verb):
    """Compute whether or not a verb contains only japanese characters

    Args:
        verb (str): Japanese verb

    Returns:
        bool: False if non-japanese characters are found, True otherwise
    """
    ranges = [
        # https://stackoverflow.com/questions/30069846/how-to-find-out-chinese-or-japanese-character-in-a-string-in-python
        {"from": ord("\u3300"), "to": ord("\u33ff")},  # compatibility ideographs
        {"from": ord("\ufe30"), "to": ord("\ufe4f")},  # compatibility ideographs
        {"from": ord("\uf900"), "to": ord("\ufaff")},  # compatibility ideographs
        {
            "from": ord("\U0002F800"),
            "to": ord("\U0002fa1f"),
        },  # compatibility ideographs
        {"from": ord("\u3040"), "to": ord("\u309f")},  # Japanese Hiragana
        {"from": ord("\u30a0"), "to": ord("\u30ff")},  # Japanese Katakana
        {"from": ord("\u2e80"), "to": ord("\u2eff")},  # cjk radicals supplement
        {"from": ord("\u4e00"), "to": ord("\u9fff")},
        {"from": ord("\u3400"), "to": ord("\u4dbf")},
        {"from": ord("\U00020000"), "to": ord("\U0002a6df")},
        {"from": ord("\U0002a700"), "to": ord("\U0002b73f")},
        {"from": ord("\U0002b740"), "to": ord("\U0002b81f")},
        {
            "from": ord("\U0002b820"),
            "to": ord("\U0002ceaf"),
        },  # included as of Unicode 8.0
    ]

    for char in verb:
        if not any([range["from"] <= ord(char) <= range["to"] for range in ranges]):
            return False
    return True


def validate_japanese_verb(func):
    def wrapper(self, verb, *args, **kwargs):
        if len(verb) < 2:
            raise InvalidJapaneseVerbLengthError(
                "Invalid Japanese Verb Length", len(verb), verb
            )

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
            raise InvalidJapaneseVerbEndingError(
                "Invalid Japanese Verb Ending Particle", verb[-1:]
            )

        if not contains_only_japanese_characters(verb):
            raise NonJapaneseCharacterError("Non-Japanese Character Found", verb)

        # assuming *args and **kwargs will always have the correct arguments because initial function call succeeded
        return func(self, verb, *args, **kwargs)

    return wrapper
