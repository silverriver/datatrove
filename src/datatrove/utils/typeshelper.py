from dataclasses import dataclass


@dataclass
class NiceRepr:
    emoji: str
    name: str

    def __post_init__(self):
        self.name = self.name.capitalize()

    def get_name(self):
        return f"---> {self.emoji} {self.name}\n"


class Languages:
    # iso 639-1
    afar = "aa"
    abkhaz = "ab"
    avestan = "ae"
    afrikaans = "af"
    akan = "ak"
    amharic = "am"
    aragonese = "an"
    arabic = "ar"
    assamese = "as"
    avaric = "av"
    aymara = "ay"
    azerbaijani = "az"
    bashkir = "ba"
    belarusian = "be"
    bulgarian = "bg"
    bihari = "bh"  # Deprecated
    bislama = "bi"
    bambara = "bm"
    bengali = "bn"
    central = "bo"
    breton = "br"
    bosnian = "bs"
    catalan = "ca"
    chechen = "ce"
    chamorro = "ch"
    corsican = "co"
    cree = "cr"
    czech = "cs"
    old_bulgarian = "cu"
    chuvash = "cv"
    welsh = "cy"
    danish = "da"
    german = "de"
    maldivian = "dv"
    dzongkha = "dz"
    ewe = "ee"
    greek = "el"
    english = "en"
    esperanto = "eo"
    spanish = "es"
    estonian = "et"
    basque = "eu"
    persian = "fa"
    pular = "ff"
    finnish = "fi"
    fijian = "fj"
    faroese = "fo"
    french = "fr"
    western_frisian = "fy"
    irish = "ga"
    gaelic = "gd"
    galician = "gl"
    guarani = "gn"
    gujarati = "gu"
    manx = "gv"
    hausa = "ha"
    hebrew = "he"
    hindi = "hi"
    hiri_motu = "ho"
    croatian = "hr"
    haitian_creole = "ht"
    hungarian = "hu"
    armenian = "hy"
    herero = "hz"
    interlingua = "ia"
    indonesian = "id"
    interlingue = "ie"
    igbo = "ig"
    nuosu = "ii"
    inupiaq = "ik"
    ido = "io"
    icelandic = "is"
    italian = "it"
    inuktitut = "iu"
    japanese = "ja"
    javanese = "jv"
    georgian = "ka"
    kongo = "kg"
    gikuyu = "ki"
    kuanyama = "kj"
    kazakh = "kk"
    greenlandic = "kl"
    khmer = "km"
    kannada = "kn"
    korean = "ko"
    kanuri = "kr"
    kashmiri = "ks"
    kurdish = "ku"
    komi = "kv"
    cornish = "kw"
    kirghiz = "ky"
    latin = "la"
    luxembourgish = "lb"
    ganda = "lg"
    limburger = "li"
    lingala = "ln"
    lao = "lo"
    lithuanian = "lt"
    luba_katanga = "lu"
    latvian = "lv"
    malagasy = "mg"
    marshallese = "mh"
    maori = "mi"
    macedonian = "mk"
    malayalam = "ml"
    mongolian = "mn"
    marathi = "mr"
    malay = "ms"
    maltese = "mt"
    burmese = "my"
    nauruan = "na"
    norwegian_bokmal = "nb"
    northern_ndebele = "nd"
    nepali = "ne"
    ndonga = "ng"
    dutch = "nl"
    norwegian_nynorsk = "nn"
    norwegian = "no"
    southern_ndebele = "nr"
    navaho = "nv"
    nyanja = "ny"
    occitan = "oc"
    ojibwa = "oj"
    oromo = "om"
    oriya = "or"
    ossetic = "os"
    punjabi = "pa"
    pali = "pi"
    polish = "pl"
    pashto = "ps"
    portuguese = "pt"
    quechua = "qu"
    romansh = "rm"
    kirundi = "rn"
    romanian = "ro"
    russian = "ru"
    kinyarwanda = "rw"
    sanskrit = "sa"
    sardinian = "sc"
    sindhi = "sd"
    northern_sami = "se"
    sango = "sg"
    serbocroatian = "sh"  # Deprecated
    sinhala = "si"
    slovak = "sk"
    slovenian = "sl"
    samoan = "sm"
    shona = "sn"
    somali = "so"
    albanian = "sq"
    serbian = "sr"
    swati = "ss"
    southern_sotho = "st"
    sundanese = "su"
    swedish = "sv"
    swahili = "sw"
    tamil = "ta"
    telugu = "te"
    tajik = "tg"
    thai = "th"
    tigrinya = "ti"
    turkmen = "tk"
    tagalog = "tl"
    tswana = "tn"
    tonga = "to"
    turkish = "tr"
    tsonga = "ts"
    tatar = "tt"
    twi = "tw"
    tahitian = "ty"
    uyghur = "ug"
    ukrainian = "uk"
    urdu = "ur"
    uzbek = "uz"
    venda = "ve"
    vietnamese = "vi"
    volapuk = "vo"
    walloon = "wa"
    wolof = "wo"
    xhosa = "xh"
    yiddish = "yi"
    yoruba = "yo"
    chuang = "za"
    chinese = "zh"
    zulu = "zu"
    # iso 639-3
    konkani = "kok"
    cebuano = "ceb"
    war = "war"
    south_azerbaijani = "azb"
    sorani = "ckb"
    northern_kurdish = "kmr"
    nigerian_pidgin = "pcm"
    gothic = "got"
    western_armenian = "hyw"
    coptic = "cop"
    ancient_hebrew = "hbo"
    old_russian = "orv"
    russia_buriat = "bxr"
    old_french = "fro"
    lower_sorbian = "dsb"
    ancient_greek = "grc"
    literary_chinese = "lzh"
    upper_sorbian = "hsb"
    erzya = "myv"
    ligurian = "lij"


class StatHints:
    total = "total"
    dropped = "dropped"
    forwarded = "forwarded"


class ExtensionHelperSD:
    stage_1_signature = ".c4_sig"
    stage_2_duplicates = ".c4_dup"
    index = ".c4_index"


class ExtensionHelperES:
    stage_1_sequence = ".es_sequence"
    stage_1_sequence_size = ".es_sequence.size"
    stage_2_big_sequence = ".big_sequence"
    stage_2_bytes_offset = ".info"
    stage_3_bytes_ranges = ".bytearange"
