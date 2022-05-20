from enum import Enum


class Formality(Enum):
    PLAIN = 1
    POLITE = 2


class Polarity(Enum):
    POSITIVE = 1
    NEGATIVE = 2


class Tense(Enum):
    PAST = 1
    NONPAST = 2


class VerbClass(Enum):
    GODAN = 1
    ICHIDAN = 2
    IRREGULAR = 3
    NONIRREGULAR = 4
