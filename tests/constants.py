from src.japverbconj.constants.enumerated_types import VerbClass

korean_with_japanese = "한국어처리기む"
english_with_japanese = "Heloむ"
verb_incorrect_particle_ending = "飲ま"


class GodanVerbNomu:
    # http://www.japaneseverbconjugator.com/VerbDetails.asp?txtVerb=%E9%A3%B2%E3%82%80
    verb = "飲む"  # plain positive nonpast
    verb_class = VerbClass.GODAN

    # Formal Verb Forms
    polite_positive_nonpast = "飲みます"
    polite_positive_past = "飲みました"
    polite_negative_nonpast = "飲みません"
    polite_negative_past = "飲みませんでした"

    # Plain Verb Forms
    plain_positive_past = "飲んだ"  # ta form
    plain_negative_nonpast = "飲まない"  # nai form
    plain_negative_past = "飲まなかった"  # katta form

    te_form = "飲んで"

    # Conditional Verb Forms
    conditional_polite = "飲みましたら"  # tara form
    conditional_plain = "飲んだら"

    # Volitional Verb Forms
    volitional_polite_positive = "飲みましょう"
    volitional_polite_negative = "飲まないでしょう"
    volitional_plain_positive = "飲もう"
    volitional_plain_negative = "飲まないだろう"

    # Potential Verb Forms
    potential_plain_positive = "飲める"
    potential_plain_negative = "飲めない"
    potential_polite_positive = "飲めます"
    potential_polite_negative = "飲めません"

    # Imperative Verb Forms
    imperative_plain_positive = "飲め"
    imperative_plain_negative = "飲むな"
    imperative_polite_positive = "飲んでください"
    imperative_polite_negative = "飲まないでください"

    # Causative Verb Forms
    causative_plain_positive = "飲ませる"
    causative_plain_negative = "飲ませない"
    causative_polite_positive = "飲ませます"
    causative_polite_negative = "飲ませません"

    # Passive Verb Forms
    passive_plain_positive = "飲まれる"
    passive_plain_negative = "飲まれない"
    passive_polite_positive = "飲まれます"
    passive_polite_negative = "飲まれません"

    # Provisional Verb Forms
    provisional_plain_positive = "飲めば"
    provisional_plain_negative = "飲まなければ"


class IchidanVerbTaberu:
    # http://www.japaneseverbconjugator.com/VerbDetails.asp?txtVerb=%E9%A3%9F%E3%81%B9%E3%82%8B
    verb = "食べる"  # plain positive nonpast
    verb_class = VerbClass.ICHIDAN

    # Formal Verb Forms
    polite_positive_nonpast = "食べます"
    polite_positive_past = "食べました"
    polite_negative_nonpast = "食べません"
    polite_negative_past = "食べませんでした"

    # Plain Verb Forms
    plain_positive_past = "食べた"  # ta form
    plain_negative_nonpast = "食べない"  # nai form
    plain_negative_past = "食べなかった"  # katta form

    te_form = "食べて"

    # Conditional Verb Forms
    conditional_polite = "食べましたら"  # tara form
    conditional_plain = "食べたら"  # tara form

    # Volitional Verb Forms
    volitional_plain_positive = "食べよう"
    volitional_plain_negative = "食べないだろう"
    volitional_polite_positive = "食べましょう"
    volitional_polite_negative = "食べないでしょう"

    # Potential Verb Forms
    potential_plain_positive = "食べられる"
    potential_plain_negative = "食べられない"
    potential_polite_positive = "食べられます"
    potential_polite_negative = "食べられません"

    # Imperative Verb Forms
    imperative_plain_positive = "食べろ"
    imperative_plain_negative = "食べるな"
    imperative_polite_positive = "食べてください"
    imperative_polite_negative = "食べないでください"

    # Causative Verb Forms
    causative_plain_positive = "食べさせる"
    causative_plain_negative = "食べさせない"
    causative_polite_positive = "食べさせます"
    causative_polite_negative = "食べさせません"

    # Passive Verb Forms
    passive_plain_positive = "食べられる"
    passive_plain_negative = "食べられない"
    passive_polite_positive = "食べられます"
    passive_polite_negative = "食べられません"

    # Provisional Verb Forms
    provisional_plain_positive = "食べれば"
    provisional_plain_negative = "食べなければ"


class IrregularVerbSuru:
    # http://www.japaneseverbconjugator.com/Suru.asp
    verb = "勉強する"  # plain positive nonpast
    verb_class = VerbClass.IRREGULAR

    # Formal Verb Forms
    polite_positive_nonpast = "勉強します"
    polite_positive_past = "勉強しました"
    polite_negative_nonpast = "勉強しません"
    polite_negative_past = "勉強しませんでした"

    # Plain Verb Forms
    plain_positive_past = "勉強した"  # ta form
    plain_negative_nonpast = "勉強しない"  # nai form
    plain_negative_past = "勉強しなかった"  # katta form

    te_form = "勉強して"

    # Conditional Verb Forms
    conditional_plain_positive = "勉強したら"  # tara form
    conditional_polite_positive = "勉強しましたら"  # tara form
    conditional_plain_negative = "勉強しなかったら"  # tara form
    conditional_polite_negative = "勉強しませんでしたら"  # tara form

    # Volitional Verb Forms
    volitional_plain_positive = "勉強しよう"
    volitional_polite_positive = "勉強しましょう"
    volitional_plain_negative = "勉強しないだろう"
    volitional_polite_negative = "勉強しないでしょう"

    # volitional_plain_positive_past = "勉強したろう"
    # volitional_polite_positive_past = "勉強しましたろう"
    # volitional_plain_negative_past = "勉強しなかっただろう"
    # volitional_polite_negative_past = "勉強しなかたでしょう"

    # Potential Verb Forms
    potential_plain_positive = "勉強できる"
    potential_plain_negative = "勉強できない"
    potential_polite_positive = "勉強できます"
    potential_polite_negative = "勉強できません"

    # Imperative Verb Forms
    imperative_plain_positive = "勉強しろ"
    imperative_plain_negative = "勉強するな"
    imperative_polite_positive = "勉強してください"
    imperative_polite_negative = "勉強しないでください"

    # Causative Verb Forms
    causative_plain_positive = "勉強させる"

    # Passive Verb Forms
    passive_plain_positive = "勉強される"

    # Provisional Verb Forms
    provisional_plain_positive = "勉強すれば"
    provisional_plain_negative = "勉強しなければ"
    provisional_polite_positive = "勉強しませば"
    provisional_polite_negative = "勉強しませんなら"


class IrregularVerbKuru:
    # http://www.japaneseverbconjugator.com/Kuru.asp
    verb = "くる"  # plain positive nonpast
    verb_class = VerbClass.IRREGULAR

    # Formal Verb Forms
    polite_positive_nonpast = "きます"
    polite_positive_past = "きました"
    polite_negative_nonpast = "きません"
    polite_negative_past = "きませんでした"

    # Plain Verb Forms
    plain_positive_past = "きた"  # ta form
    plain_negative_nonpast = "こない"  # nai form
    plain_negative_past = "こなかった"  # katta form

    te_form = "きて"

    # Conditional Verb Forms
    conditional_plain_positive = "きたら"  # tara form
    conditional_polite_positive = "きましたら"  # tara form
    conditional_plain_negative = "こなかったら"  # tara form
    conditional_polite_negative = "きませんでしたら"  # tara form

    # Volitional Verb Forms
    volitional_polite_positive = "きましょう"
    volitional_polite_negative = "こないでしょう"
    volitional_plain_positive = "こよう"
    volitional_plain_negative = "こないだろう"

    # volitional_plain_positive_past = "きたろう"
    # volitional_polite_positive_past = "きたでしょう"
    # volitional_plain_negative_past = "こなかっただろう"
    # volitional_polite_negative_past = "こなかったでしょう"

    # Potential Verb Forms
    potential_plain_positive = "こられる"
    potential_plain_negative = "こられない"
    potential_polite_positive = "こられます"
    potential_polite_negative = "こられません"

    # Imperative Verb Forms
    imperative_plain_positive = "こい"
    imperative_plain_negative = "くるな"
    imperative_polite_positive = "きてください"
    imperative_polite_negative = "こないでください"

    # Causative Verb Forms
    causative_plain_positive = "こさせる"
    causative_plain_negative = "こさせない"
    causative_polite_positive = "こさせます"
    causative_polite_negative = "こさせません"

    # Passive Verb Forms
    passive_plain_positive = "こられる"

    # Provisional Verb Forms
    provisional_plain_positive = "くれば"
    provisional_plain_negative = "こなければ"
    provisional_polite_positive = "きませば"
    provisional_polite_negative = "きませんなら"


class IrregularVerbKuruKanji:
    # http://www.japaneseverbconjugator.com/Kuru.asp
    verb = "来る"  # plain positive nonpast
    verb_class = VerbClass.IRREGULAR

    # Formal Verb Forms
    polite_positive_nonpast = "来ます"
    polite_positive_past = "来ました"
    polite_negative_nonpast = "来ません"
    polite_negative_past = "来ませんでした"

    # Plain Verb Forms
    plain_positive_past = "来た"  # ta form
    plain_negative_nonpast = "来ない"  # nai form
    plain_negative_past = "来なかった"  # katta form

    te_form = "来て"

    # Conditional Verb Forms
    conditional_plain_positive = "来たら"  # tara form
    conditional_polite_positive = "来ましたら"  # tara form
    conditional_plain_negative = "来なかったら"  # tara form
    conditional_polite_negative = "来ませんでしたら"  # tara form

    # Volitional Verb Forms
    volitional_polite_positive = "来ましょう"
    volitional_polite_negative = "来ないでしょう"
    volitional_plain_positive = "来よう"
    volitional_plain_negative = "来ないだろう"

    # volitional_plain_positive_past = "来たろう"
    # volitional_polite_positive_past = "来たでしょう"
    # volitional_plain_negative_past = "来なかっただろう"
    # volitional_polite_negative_past = "来なかったでしょう"

    # Potential Verb Forms
    potential_plain_positive = "来られる"
    potential_plain_negative = "来られない"
    potential_polite_positive = "来られます"
    potential_polite_negative = "来られません"

    # Imperative Verb Forms
    imperative_plain_positive = "来い"
    imperative_plain_negative = "来るな"
    imperative_polite_positive = "来てください"
    imperative_polite_negative = "来ないでください"

    # Causative Verb Forms
    causative_plain_positive = "来させる"
    causative_plain_negative = "来させない"
    causative_polite_positive = "来させます"
    causative_polite_negative = "来させません"

    # Passive Verb Forms
    passive_plain_positive = "来られる"

    # Provisional Verb Forms
    provisional_plain_positive = "来れば"
    provisional_plain_negative = "来なければ"
    provisional_polite_positive = "来ませば"
    provisional_polite_negative = "来ませんなら"


class CopulaDa:
    plain_positive = "だ"
    polite_positive = "です"
    conditional = "なら"
    presumptive_plain = "だろう"
    presumptive_polite = "でしょう"
    te_form_plain = "で"
    te_form_polite = "でして"
    plain_past = "だった"
    polite_past = "でした"
    tara_plain = "だったら"
    tara_polite = "でしたら"
    plain_negative = "ではない"
    polite_negative = "ではありません"
    presumptive_plain_negative = "ではないだろう"
    presumptive_polite_negative = "ではないでしょう"
    plain_past_negative = "なかった"
    polite_past_negative = "ではありませんでした"


PARAMETER_LIST = [
    ("godan_nomu", GodanVerbNomu),
    ("ichidan_taberu", IchidanVerbTaberu),
    ("irreg_suru", IrregularVerbSuru),
    ("irreg_kuru", IrregularVerbKuru),
    ("irreg_kuru_kanji", IrregularVerbKuruKanji),
]
