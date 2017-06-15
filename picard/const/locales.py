# -*- coding: utf-8 -*-
#
# Picard, the next-generation MusicBrainz tagger
#
# Copyright (C) 2007 Lukáš Lalinský
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.


# List of alias locales
ALIAS_LOCALES = {
    'aa': 'Afar',
    'aa_DJ': 'Afar (Djibouti)',
    'aa_ER': 'Afar (Eritrea)',
    'aa_ER_SAAHO': 'Afar (Eritrea) (Saho)',
    'aa_ET': 'Afar (Ethiopia)',
    'af': 'Afrikaans',
    'af_NA': 'Afrikaans (Namibia)',
    'af_ZA': 'Afrikaans (South Africa)',
    'ak': 'Akan',
    'ak_GH': 'Akan (Ghana)',
    'sq': 'Albanian',
    'sq_AL': 'Albanian (Albania)',
    'am': 'Amharic',
    'am_ET': 'Amharic (Ethiopia)',
    'ar': 'Arabic',
    'ar_DZ': 'Arabic (Algeria)',
    'ar_BH': 'Arabic (Bahrain)',
    'ar_EG': 'Arabic (Egypt)',
    'ar_IQ': 'Arabic (Iraq)',
    'ar_JO': 'Arabic (Jordan)',
    'ar_KW': 'Arabic (Kuwait)',
    'ar_LB': 'Arabic (Lebanon)',
    'ar_LY': 'Arabic (Libya)',
    'ar_MA': 'Arabic (Morocco)',
    'ar_OM': 'Arabic (Oman)',
    'ar_QA': 'Arabic (Qatar)',
    'ar_SA': 'Arabic (Saudi Arabia)',
    'ar_SD': 'Arabic (Sudan)',
    'ar_SY': 'Arabic (Syria)',
    'ar_TN': 'Arabic (Tunisia)',
    'ar_AE': 'Arabic (United Arab Emirates)',
    'ar_YE': 'Arabic (Yemen)',
    'hy': 'Armenian',
    'hy_AM': 'Armenian (Armenia)',
    'hy_AM_REVISED': 'Armenian (Armenia) (Revised Orthography)',
    'as': 'Assamese',
    'as_IN': 'Assamese (India)',
    'cch': 'Atsam',
    'cch_NG': 'Atsam (Nigeria)',
    'az': 'Azerbaijani',
    'az_AZ': 'Azerbaijani (Azerbaijan)',
    'az_Cyrl': 'Azerbaijani (Cyrillic)',
    'az_Cyrl_AZ': 'Azerbaijani (Cyrillic) (Azerbaijan)',
    'az_Latn': 'Azerbaijani (Latin)',
    'az_Latn_AZ': 'Azerbaijani (Latin) (Azerbaijan)',
    'eu': 'Basque',
    'eu_ES': 'Basque (Spain)',
    'be': 'Belarusian',
    'be_BY': 'Belarusian (Belarus)',
    'bn': 'Bengali',
    'bn_BD': 'Bengali (Bangladesh)',
    'bn_IN': 'Bengali (India)',
    'byn': 'Blin',
    'byn_ER': 'Blin (Eritrea)',
    'bs': 'Bosnian',
    'bs_BA': 'Bosnian (Bosnia and Herzegovina)',
    'bg': 'Bulgarian',
    'bg_BG': 'Bulgarian (Bulgaria)',
    'my': 'Burmese',
    'my_MM': 'Burmese (Myanmar [Burma])',
    'ca': 'Catalan',
    'ca_ES': 'Catalan (Spain)',
    'zh': 'Chinese',
    'zh_CN': 'Chinese (China)',
    'zh_HK': 'Chinese (Hong Kong SAR China)',
    'zh_MO': 'Chinese (Macau SAR China)',
    'zh_Hans': 'Chinese (Simplified Han)',
    'zh_Hans_CN': 'Chinese (Simplified Han) (China)',
    'zh_Hans_HK': 'Chinese (Simplified Han) (Hong Kong SAR China)',
    'zh_Hans_MO': 'Chinese (Simplified Han) (Macau SAR China)',
    'zh_Hans_SG': 'Chinese (Simplified Han) (Singapore)',
    'zh_SG': 'Chinese (Singapore)',
    'zh_TW': 'Chinese (Taiwan)',
    'zh_Hant': 'Chinese (Traditional Han)',
    'zh_Hant_HK': 'Chinese (Traditional Han) (Hong Kong SAR China)',
    'zh_Hant_MO': 'Chinese (Traditional Han) (Macau SAR China)',
    'zh_Hant_TW': 'Chinese (Traditional Han) (Taiwan)',
    'cop': 'Coptic',
    'kw': 'Cornish',
    'kw_GB': 'Cornish (United Kingdom)',
    'hr': 'Croatian',
    'hr_HR': 'Croatian (Croatia)',
    'cs': 'Czech',
    'cs_CZ': 'Czech (Czech Republic)',
    'da': 'Danish',
    'da_DK': 'Danish (Denmark)',
    'dv': 'Divehi',
    'dv_MV': 'Divehi (Maldives)',
    'nl': 'Dutch',
    'nl_BE': 'Dutch (Belgium)',
    'nl_NL': 'Dutch (Netherlands)',
    'dz': 'Dzongkha',
    'dz_BT': 'Dzongkha (Bhutan)',
    'en': 'English',
    'en_AS': 'English (American Samoa)',
    'en_AU': 'English (Australia)',
    'en_BE': 'English (Belgium)',
    'en_BZ': 'English (Belize)',
    'en_BW': 'English (Botswana)',
    'en_CA': 'English (Canada)',
    'en_Dsrt': 'English (Deseret)',
    'en_Dsrt_US': 'English (Deseret) (United States)',
    'en_GU': 'English (Guam)',
    'en_HK': 'English (Hong Kong SAR China)',
    'en_IN': 'English (India)',
    'en_IE': 'English (Ireland)',
    'en_JM': 'English (Jamaica)',
    'en_MT': 'English (Malta)',
    'en_MH': 'English (Marshall Islands)',
    'en_NA': 'English (Namibia)',
    'en_NZ': 'English (New Zealand)',
    'en_MP': 'English (Northern Mariana Islands)',
    'en_PK': 'English (Pakistan)',
    'en_PH': 'English (Philippines)',
    'en_Shaw': 'English (Shavian)',
    'en_SG': 'English (Singapore)',
    'en_ZA': 'English (South Africa)',
    'en_TT': 'English (Trinidad and Tobago)',
    'en_UM': 'English (U.S. Minor Outlying Islands)',
    'en_VI': 'English (U.S. Virgin Islands)',
    'en_GB': 'English (United Kingdom)',
    'en_US': 'English (United States)',
    'en_US_POSIX': 'English (United States) (Computer)',
    'en_ZW': 'English (Zimbabwe)',
    'eo': 'Esperanto',
    'et': 'Estonian',
    'et_EE': 'Estonian (Estonia)',
    'ee': 'Ewe',
    'ee_GH': 'Ewe (Ghana)',
    'ee_TG': 'Ewe (Togo)',
    'fo': 'Faroese',
    'fo_FO': 'Faroese (Faroe Islands)',
    'fil': 'Filipino',
    'fil_PH': 'Filipino (Philippines)',
    'fi': 'Finnish',
    'fi_FI': 'Finnish (Finland)',
    'fr': 'French',
    'fr_BE': 'French (Belgium)',
    'fr_CA': 'French (Canada)',
    'fr_FR': 'French (France)',
    'fr_LU': 'French (Luxembourg)',
    'fr_MC': 'French (Monaco)',
    'fr_SN': 'French (Senegal)',
    'fr_CH': 'French (Switzerland)',
    'fur': 'Friulian',
    'fur_IT': 'Friulian (Italy)',
    'gaa': 'Ga',
    'gaa_GH': 'Ga (Ghana)',
    'gl': 'Galician',
    'gl_ES': 'Galician (Spain)',
    'gez': 'Geez',
    'gez_ER': 'Geez (Eritrea)',
    'gez_ET': 'Geez (Ethiopia)',
    'ka': 'Georgian',
    'ka_GE': 'Georgian (Georgia)',
    'de': 'German',
    'de_AT': 'German (Austria)',
    'de_BE': 'German (Belgium)',
    'de_DE': 'German (Germany)',
    'de_LI': 'German (Liechtenstein)',
    'de_LU': 'German (Luxembourg)',
    'de_CH': 'German (Switzerland)',
    'el_POLYTON': 'Greek',
    'el': 'Greek',
    'el_CY': 'Greek (Cyprus)',
    'el_GR': 'Greek (Greece)',
    'gu': 'Gujarati',
    'gu_IN': 'Gujarati (India)',
    'ha': 'Hausa',
    'ha_Arab': 'Hausa (Arabic)',
    'ha_Arab_NG': 'Hausa (Arabic) (Nigeria)',
    'ha_Arab_SD': 'Hausa (Arabic) (Sudan)',
    'ha_GH': 'Hausa (Ghana)',
    'ha_Latn': 'Hausa (Latin)',
    'ha_Latn_GH': 'Hausa (Latin) (Ghana)',
    'ha_Latn_NE': 'Hausa (Latin) (Niger)',
    'ha_Latn_NG': 'Hausa (Latin) (Nigeria)',
    'ha_NE': 'Hausa (Niger)',
    'ha_NG': 'Hausa (Nigeria)',
    'ha_SD': 'Hausa (Sudan)',
    'haw': 'Hawaiian',
    'haw_US': 'Hawaiian (United States)',
    'he': 'Hebrew',
    'he_IL': 'Hebrew (Israel)',
    'hi': 'Hindi',
    'hi_IN': 'Hindi (India)',
    'hu': 'Hungarian',
    'hu_HU': 'Hungarian (Hungary)',
    'is': 'Icelandic',
    'is_IS': 'Icelandic (Iceland)',
    'ig': 'Igbo',
    'ig_NG': 'Igbo (Nigeria)',
    'id': 'Indonesian',
    'id_ID': 'Indonesian (Indonesia)',
    'ia': 'Interlingua',
    'iu': 'Inuktitut',
    'ga': 'Irish',
    'ga_IE': 'Irish (Ireland)',
    'it': 'Italian',
    'it_IT': 'Italian (Italy)',
    'it_CH': 'Italian (Switzerland)',
    'ja': 'Japanese',
    'ja_JP': 'Japanese (Japan)',
    'kaj': 'Jju',
    'kaj_NG': 'Jju Nigeria',
    'kl': 'Kalaallisut',
    'kl_GL': 'Kalaallisut (Greenland)',
    'kam': 'Kamba',
    'kam_KE': 'Kamba (Kenya)',
    'kn': 'Kannada',
    'kn_IN': 'Kannada (India)',
    'kk': 'Kazakh',
    'kk_Cyrl': 'Kazakh (Cyrillic)',
    'kk_Cyrl_KZ': 'Kazakh (Cyrillic) (Kazakhstan)',
    'kk_KZ': 'Kazakh (Kazakhstan)',
    'km': 'Khmer',
    'km_KH': 'Khmer (Cambodia)',
    'rw': 'Kinyarwanda',
    'rw_RW': 'Kinyarwanda (Rwanda)',
    'ky': 'Kirghiz',
    'ky_KG': 'Kirghiz (Kyrgyzstan)',
    'kok': 'Konkani',
    'kok_IN': 'Konkani (India)',
    'ko': 'Korean',
    'ko_KR': 'Korean (South Korea)',
    'kfo': 'Koro',
    'kfo_CI': 'Koro (Côte d’Ivoire)',
    'kpe': 'Kpelle',
    'kpe_GN': 'Kpelle (Guinea)',
    'kpe_LR': 'Kpelle (Liberia)',
    'ku': 'Kurdish',
    'ku_Arab': 'Kurdish (Arabic)',
    'ku_Arab_IR': 'Kurdish (Arabic) (Iran)',
    'ku_Arab_IQ': 'Kurdish (Arabic) (Iraq)',
    'ku_Arab_SY': 'Kurdish (Arabic) (Syria)',
    'ku_IR': 'Kurdish (Iran)',
    'ku_IQ': 'Kurdish (Iraq)',
    'ku_Latn': 'Kurdish (Latin)',
    'ku_Latn_TR': 'Kurdish (Latin) (Turkey)',
    'ku_SY': 'Kurdish (Syria)',
    'ku_TR': 'Kurdish (Turkey)',
    'lo': 'Lao',
    'lo_LA': 'Lao (Laos)',
    'lv': 'Latvian',
    'lv_LV': 'Latvian (Latvia)',
    'ln': 'Lingala',
    'ln_CG': 'Lingala (Congo - Brazzaville)',
    'ln_CD': 'Lingala (Congo - Kinshasa)',
    'lt': 'Lithuanian',
    'lt_LT': 'Lithuanian (Lithuania)',
    'nds': 'Low German',
    'nds_DE': 'Low German (Germany)',
    'mk': 'Macedonian',
    'mk_MK': 'Macedonian (Macedonia)',
    'ms': 'Malay',
    'ms_BN': 'Malay (Brunei)',
    'ms_MY': 'Malay (Malaysia)',
    'ml': 'Malayalam',
    'ml_IN': 'Malayalam (India)',
    'mt': 'Maltese',
    'mt_MT': 'Maltese (Malta)',
    'gv': 'Manx',
    'gv_GB': 'Manx (United Kingdom)',
    'mr': 'Marathi',
    'mr_IN': 'Marathi (India)',
    'mo': 'Moldavian',
    'mn': 'Mongolian',
    'mn_CN': 'Mongolian (China)',
    'mn_Cyrl': 'Mongolian (Cyrillic)',
    'mn_Cyrl_MN': 'Mongolian (Cyrillic) (Mongolia)',
    'mn_MN': 'Mongolian (Mongolia)',
    'mn_Mong': 'Mongolian (Mongolian)',
    'mn_Mong_CN': 'Mongolian (Mongolian) (China)',
    'ne': 'Nepali',
    'ne_IN': 'Nepali (India)',
    'ne_NP': 'Nepali (Nepal)',
    'se': 'Northern Sami',
    'se_FI': 'Northern (Sami Finland)',
    'se_NO': 'Northern (Sami Norway)',
    'nso': 'Northern Sotho',
    'nso_ZA': 'Northern Sotho (South Africa)',
    'no': 'Norwegian',
    'nb': 'Norwegian Bokmål',
    'nb_NO': 'Norwegian Bokmål (Norway)',
    'nn': 'Norwegian Nynorsk',
    'nn_NO': 'Norwegian Nynorsk (Norway)',
    'ny': 'Nyanja',
    'ny_MW': 'Nyanja (Malawi)',
    'oc': 'Occitan',
    'oc_FR': 'Occitan (France)',
    'or': 'Oriya',
    'or_IN': 'Oriya (India)',
    'om': 'Oromo',
    'om_ET': 'Oromo (Ethiopia)',
    'om_KE': 'Oromo (Kenya)',
    'ps': 'Pashto',
    'ps_AF': 'Pashto (Afghanistan)',
    'fa': 'Persian',
    'fa_AF': 'Persian (Afghanistan)',
    'fa_IR': 'Persian (Iran)',
    'pl': 'Polish',
    'pl_PL': 'Polish (Poland)',
    'pt': 'Portuguese',
    'pt_BR': 'Portuguese (Brazil)',
    'pt_PT': 'Portuguese (Portugal)',
    'pa': 'Punjabi',
    'pa_Arab': 'Punjabi (Arabic)',
    'pa_Arab_PK': 'Punjabi (Arabic) (Pakistan)',
    'pa_Guru': 'Punjabi (Gurmukhi)',
    'pa_Guru_IN': 'Punjabi (Gurmukhi) (India)',
    'pa_IN': 'Punjabi (India)',
    'pa_PK': 'Punjabi (Pakistan)',
    'ro': 'Romanian',
    'ro_MD': 'Romanian (Moldova)',
    'ro_RO': 'Romanian (Romania)',
    'ru': 'Russian',
    'ru_RU': 'Russian (Russia)',
    'ru_UA': 'Russian (Ukraine)',
    'sa': 'Sanskrit',
    'sa_IN': 'Sanskrit (India)',
    'sr_YU': 'Serbian',
    'sr': 'Serbian',
    'sr_BA': 'Serbian (Bosnia and Herzegovina)',
    'sr_Cyrl': 'Serbian (Cyrillic)',
    'sr_Cyrl_YU': 'Serbian (Cyrillic)',
    'sr_Cyrl_BA': 'Serbian (Cyrillic) (Bosnia and Herzegovina)',
    'sr_Cyrl_ME': 'Serbian (Cyrillic) (Montenegro)',
    'sr_Cyrl_RS': 'Serbian (Cyrillic) (Serbia)',
    'sr_Cyrl_CS': 'Serbian (Cyrillic) (Serbia and Montenegro)',
    'sr_Latn': 'Serbian (Latin)',
    'sr_Latn_YU': 'Serbian (Latin)',
    'sr_Latn_BA': 'Serbian (Latin) (Bosnia and Herzegovina)',
    'sr_Latn_ME': 'Serbian (Latin) (Montenegro)',
    'sr_Latn_RS': 'Serbian (Latin) (Serbia)',
    'sr_Latn_CS': 'Serbian (Latin) (Serbia and Montenegro)',
    'sr_ME': 'Serbian (Montenegro)',
    'sr_RS': 'Serbian (Serbia)',
    'sr_CS': 'Serbian (Serbia and Montenegro)',
    'sh': 'Serbo-Croatian',
    'sh_YU': 'Serbo-Croatian',
    'sh_BA': 'Serbo-Croatian (Bosnia and Herzegovina)',
    'sh_CS': 'Serbo-Croatian (Serbia and Montenegro)',
    'ii': 'Sichuan Yi',
    'ii_CN': 'Sichuan (Yi China)',
    'sid': 'Sidamo',
    'sid_ET': 'Sidamo (Ethiopia)',
    'si': 'Sinhala',
    'si_LK': 'Sinhala (Sri Lanka)',
    'sk': 'Slovak',
    'sk_SK': 'Slovak (Slovakia)',
    'sl': 'Slovenian',
    'sl_SI': 'Slovenian (Slovenia)',
    'so': 'Somali',
    'so_DJ': 'Somali (Djibouti)',
    'so_ET': 'Somali (Ethiopia)',
    'so_KE': 'Somali (Kenya)',
    'so_SO': 'Somali (Somalia)',
    'nr': 'South Ndebele',
    'nr_ZA': 'South Ndebele (South Africa)',
    'st': 'Southern Sotho',
    'st_LS': 'Southern Sotho (Lesotho)',
    'st_ZA': 'Southern Sotho (South Africa)',
    'es': 'Spanish',
    'es_AR': 'Spanish (Argentina)',
    'es_BO': 'Spanish (Bolivia)',
    'es_CL': 'Spanish (Chile)',
    'es_CO': 'Spanish (Colombia)',
    'es_CR': 'Spanish (Costa Rica)',
    'es_DO': 'Spanish (Dominican Republic)',
    'es_EC': 'Spanish (Ecuador)',
    'es_SV': 'Spanish (El Salvador)',
    'es_GT': 'Spanish (Guatemala)',
    'es_HN': 'Spanish (Honduras)',
    'es_MX': 'Spanish (Mexico)',
    'es_NI': 'Spanish (Nicaragua)',
    'es_PA': 'Spanish (Panama)',
    'es_PY': 'Spanish (Paraguay)',
    'es_PE': 'Spanish (Peru)',
    'es_PR': 'Spanish (Puerto Rico)',
    'es_ES': 'Spanish (Spain)',
    'es_US': 'Spanish (United States)',
    'es_UY': 'Spanish (Uruguay)',
    'es_VE': 'Spanish (Venezuela)',
    'sw': 'Swahili',
    'sw_KE': 'Swahili (Kenya)',
    'sw_TZ': 'Swahili (Tanzania)',
    'ss': 'Swati',
    'ss_ZA': 'Swati (South Africa)',
    'ss_SZ': 'Swati (Swaziland)',
    'sv': 'Swedish',
    'sv_FI': 'Swedish (Finland)',
    'sv_SE': 'Swedish (Sweden)',
    'gsw': 'Swiss German',
    'gsw_CH': 'Swiss German (Switzerland)',
    'syr': 'Syriac',
    'syr_SY': 'Syriac (Syria)',
    'tl': 'Tagalog',
    'tg': 'Tajik',
    'tg_Cyrl': 'Tajik (Cyrillic)',
    'tg_Cyrl_TJ': 'Tajik (Cyrillic) (Tajikistan)',
    'tg_TJ': 'Tajik (Tajikistan)',
    'ta': 'Tamil',
    'ta_IN': 'Tamil (India)',
    'trv': 'Taroko',
    'trv_TW': 'Taroko (Taiwan)',
    'tt': 'Tatar',
    'tt_RU': 'Tatar (Russia)',
    'te': 'Telugu',
    'te_IN': 'Telugu (India)',
    'th': 'Thai',
    'th_TH': 'Thai (Thailand)',
    'bo': 'Tibetan',
    'bo_CN': 'Tibetan (China)',
    'bo_IN': 'Tibetan (India)',
    'tig': 'Tigre',
    'tig_ER': 'Tigre (Eritrea)',
    'ti': 'Tigrinya',
    'ti_ER': 'Tigrinya (Eritrea)',
    'ti_ET': 'Tigrinya (Ethiopia)',
    'to': 'Tonga',
    'to_TO': 'Tonga (Tonga)',
    'ts': 'Tsonga',
    'ts_ZA': 'Tsonga (South Africa)',
    'tn': 'Tswana',
    'tn_ZA': 'Tswana (South Africa)',
    'tr': 'Turkish',
    'tr_TR': 'Turkish (Turkey)',
    'kcg': 'Tyap',
    'kcg_NG': 'Tyap (Nigeria)',
    'ug': 'Uighur',
    'ug_Arab': 'Uighur (Arabic)',
    'ug_Arab_CN': 'Uighur (Arabic) (China)',
    'ug_CN': 'Uighur (China)',
    'uk': 'Ukrainian',
    'uk_UA': 'Ukrainian (Ukraine)',
    'ur': 'Urdu',
    'ur_IN': 'Urdu (India)',
    'ur_PK': 'Urdu (Pakistan)',
    'uz': 'Uzbek',
    'uz_AF': 'Uzbek (Afghanistan)',
    'uz_Arab': 'Uzbek (Arabic)',
    'uz_Arab_AF': 'Uzbek (Arabic) (Afghanistan)',
    'uz_Cyrl': 'Uzbek (Cyrillic)',
    'uz_Cyrl_UZ': 'Uzbek (Cyrillic) (Uzbekistan)',
    'uz_Latn': 'Uzbek (Latin)',
    'uz_Latn_UZ': 'Uzbek (Latin) (Uzbekistan)',
    'uz_UZ': 'Uzbek (Uzbekistan)',
    've': 'Venda',
    've_ZA': 'Venda (South Africa)',
    'vi': 'Vietnamese',
    'vi_VN': 'Vietnamese (Vietnam)',
    'wal': 'Walamo',
    'wal_ET': 'Walamo (Ethiopia)',
    'cy': 'Welsh',
    'cy_GB': 'Welsh (United Kingdom)',
    'wo': 'Wolof',
    'wo_Latn': 'Wolof (Latin)',
    'wo_Latn_SN': 'Wolof (Latin) (Senegal)',
    'wo_SN': 'Wolof (Senegal)',
    'xh': 'Xhosa',
    'xh_ZA': 'Xhosa (South Africa)',
    'yo': 'Yoruba',
    'yo_NG': 'Yoruba (Nigeria)',
    'zu': 'Zulu',
    'zu_ZA': 'Zulu (South Africa)',
}