from src.constants.EnumeratedTypes import Formality, Polarity, Tense, VerbClass

# regex for kanji / kana: "[一-龯ぁ-んァ-ン]+"

class GodanVerbNomu:
    # http://www.japaneseverbconjugator.com/VerbDetails.asp?txtVerb=%E9%A3%B2%E3%82%80
    Verb = "飲む" # plain positive nonpast
    Verb_Class = VerbClass.GODAN

    # Formal Verb Forms
    PolitePositiveNonpast = "飲みます"
    PolitePositivePast = "飲みました"
    PoliteNegativeNonpast = "飲みません"
    PoliteNegativePast = "飲みませんでした"

    # Plain Verb Forms
    PlainPositivePast = "飲んだ" # ta form
    PlainNegativeNonpast = "飲まない" # nai form
    PlainNegativePast = "飲まなかった" # katta form

    TeForm = "飲んで"

    # Conditional Verb Forms
    ConditionalPolite = "飲みましたら" # tara form
    ConditionalPlain = "飲んだら"

    # Volitional Verb Forms
    VolitionalPolitePositive = "飲みましょう"
    VolitionalPoliteNegative = "飲まないでしょう"
    VolitionalPlainPositive = "飲もう"
    VolitionalPlainNegative = "飲まないだろう"

    # Potential Verb Forms
    PotentialPlainPositive = "飲める"
    PotentialPlainNegative = "飲めない"
    PotentialPolitePositive = "飲めます"
    PotentialPoliteNegative = "飲めません"

    # Imperative Verb Forms
    ImperativePlainPositive = "飲め"
    ImperativePlainNegative= "飲むな"
    ImperativePolitePositive = "飲んでください"
    ImperativePoliteNegative = "飲まないでください"

    # Causative Verb Forms
    CausativePlainPositive = "飲ませる"
    CausativePlainNegative = "飲ませない"
    CausativePolitePositive = "飲ませます"
    CausativePoliteNegative = "飲ませません"

    # Passive Verb Forms
    PassivePlainPositive = "飲まれる"
    PassivePlainNegative = "飲まれない"
    PassivePolitePositive = "飲まれます"
    PassivePoliteNegative = "飲まれません"

    # Provisional Verb Forms
    ProvisionalPlainPositive = "飲めば"
    ProvisionalPlainNegative = "飲まなければ"


class IchidanVerbTaberu:
    # http://www.japaneseverbconjugator.com/VerbDetails.asp?txtVerb=%E9%A3%9F%E3%81%B9%E3%82%8B
    Verb = "食べる" # plain positive nonpast
    Verb_Class = VerbClass.ICHIDAN

    # Formal Verb Forms
    PolitePositiveNonpast = "食べます"
    PolitePositivePast = "食べました"
    PoliteNegativeNonpast = "食べません"
    PoliteNegativePast = "食べませんでした"

    # Plain Verb Forms
    PlainPositivePast = "食べた" # ta form
    PlainNegativeNonpast = "食べない" # nai form
    PlainNegativePast = "食べなかった" # katta form

    TeForm = "食べて"

    # Conditional Verb Forms
    ConditionalPolite = "食べましたら" # tara form
    ConditionalPlain = "食べたら" # tara form

    # Volitional Verb Forms
    VolitionalPlainPositive = "食べよう"
    VolitionalPlainNegative = "食べないだろう"
    VolitionalPolitePositive = "食べましょう"
    VolitionalPoliteNegative = "食べないでしょう"

    # Potential Verb Forms
    PotentialPlainPositive = "食べられる"
    PotentialPlainNegative = "食べられない"
    PotentialPolitePositive = "食べられます"
    PotentialPoliteNegative = "食べられません"

    # Imperative Verb Forms
    ImperativePlainPositive = "食べろ"
    ImperativePlainNegative= "食べるな"
    ImperativePolitePositive = "食べてください"
    ImperativePoliteNegative = "食べないでください"

    # Causative Verb Forms
    CausativePlainPositive = "食べさせる"
    CausativePlainNegative = "食べさせない"
    CausativePolitePositive = "食べさせます"
    CausativePoliteNegative = "食べさせません"

    # Passive Verb Forms
    PassivePlainPositive = "食べられる"
    PassivePlainNegative = "食べられない"
    PassivePolitePositive = "食べられます"
    PassivePoliteNegative = "食べられません"

    # Provisional Verb Forms
    ProvisionalPlainPositive = "食べれば"
    ProvisionalPlainNegative = "食べなければ"


class IrregularVerbSuru: 
    # http://www.japaneseverbconjugator.com/Suru.asp
    Verb = "勉強する" # plain positive nonpast
    Verb_Class = VerbClass.IRREGULAR

    # Formal Verb Forms
    PolitePositiveNonpast = "勉強します"
    PolitePositivePast = "勉強しました"
    PoliteNegativeNonpast = "勉強しません"
    PoliteNegativePast = "勉強しませんでした"

    # Plain Verb Forms
    PlainPositivePast = "勉強した" # ta form
    PlainNegativeNonpast = "勉強しない" # nai form
    PlainNegativePast = "勉強しなかった" # katta form

    TeForm = "勉強して"

    # Conditional Verb Forms
    ConditionalPlainPositive = "勉強したら" # tara form
    ConditionalPolitePositive = "勉強しましたら" # tara form
    ConditionalPlainNegative = "勉強しなかったら" # tara form
    ConditionalPoliteNegative = "勉強しませんでしたら" # tara form

    # Volitional Verb Forms
    VolitionalPlainPositive = "勉強しよう"
    VolitionalPolitePositive = "勉強しましょう "
    VolitionalPlainNegative = "勉強しないだろう"
    VolitionalPoliteNegative = "勉強しないでしょう"

    # VolitionalPlainPositivePast = "勉強したろう"
    # VolitionalPolitePositivePast = "勉強しましたろう"
    # VolitionalPlainNegativePast = "勉強しなかっただろう"
    # VolitionalPoliteNegativePast = "勉強しなかたでしょう"

    # Potential Verb Forms
    PotentialPlainPositive = "勉強できる"
    PotentialPlainNegative = "勉強できない"
    PotentialPolitePositive = "勉強できます"
    PotentialPoliteNegative = "勉強できません"

    # Imperative Verb Forms
    ImperativePlainPositive = "勉強しろ"
    ImperativePlainNegative= "勉強するな"
    ImperativePolitePositive = "勉強してください"
    ImperativePoliteNegative = "勉強しないでください"

    # Causative Verb Forms
    CausativePlainPositive = "勉強させる"

    # Passive Verb Forms
    PassivePlainPositive = "勉強される"

    # Provisional Verb Forms
    ProvisionalPlainPositive = "勉強すれば"
    ProvisionalPlainNegative = "勉強しなければ"
    ProvisionalPolitePositive = "勉強しませば"
    ProvisionalPoliteNegative = "勉強しませんなら"


class IrregularVerbKuru: 
    # http://www.japaneseverbconjugator.com/Kuru.asp
    Verb = "くる" # plain positive nonpast
    Verb_Class = VerbClass.IRREGULAR

    # Formal Verb Forms
    PolitePositiveNonpast = "きます"
    PolitePositivePast = "きました"
    PoliteNegativeNonpast = "きません"
    PoliteNegativePast = "きませんでした"

    # Plain Verb Forms
    PlainPositivePast = "きた" # ta form
    PlainNegativeNonpast = "こない" # nai form
    PlainNegativePast = "こなかった" # katta form

    TeForm = "きて"

    # Conditional Verb Forms
    ConditionalPlainPositive = "きたら" # tara form
    ConditionalPolitePositive = "きましたら" # tara form
    ConditionalPlainNegative = "こなかったら" # tara form
    ConditionalPoliteNegative = "きませんでしたら" # tara form

    # Volitional Verb Forms
    VolitionalPolitePositive = "きましょう"
    VolitionalPoliteNegative = "こないでしょう"
    VolitionalPlainPositive = "こよう"
    VolitionalPlainNegative = "こないだろう"

    # VolitionalPlainPositivePast = "きたろう"
    # VolitionalPolitePositivePast = "きたでしょう"
    # VolitionalPlainNegativePast = "こなかっただろう"
    # VolitionalPoliteNegativePast = "こなかったでしょう"

    # Potential Verb Forms
    PotentialPlainPositive = "こられる"
    PotentialPlainNegative = "こられない"
    PotentialPolitePositive = "こられます"
    PotentialPoliteNegative = "こられません"

    # Imperative Verb Forms
    ImperativePlainPositive = "こい"
    ImperativePlainNegative= "くるな"
    ImperativePolitePositive = "きてください"
    ImperativePoliteNegative = "こないでください"

    # Causative Verb Forms
    CausativePlainPositive = "こさせる"
    CausativePlainNegative = "こさせない"
    CausativePolitePositive = "こさせます"
    CausativePoliteNegative = "こさせません"

    # Passive Verb Forms
    PassivePlainPositive = "こられる"

    # Provisional Verb Forms
    ProvisionalPlainPositive = "くれば"
    ProvisionalPlainNegative = "こなければ"
    ProvisionalPolitePositive = "きませば"
    ProvisionalPoliteNegative = "きませんなら"