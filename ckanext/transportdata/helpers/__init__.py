from ckanext.transportdata.helpers.lists import NUTS1_BE, GEOREFERENCING_METHOD, DATASET_TYPE, NAP_TYPE
from ckanext.transportdata.utils.forms import map_for_form_select

def ontology_helper(context):
    ontology = context.get("benap_helper_ontology", None)
    if ontology == "language":
        return map_for_form_select([
            ('http://publications.europa.eu/resource/authority/language/FRA', {
                "en": "French",
                "fr": "Français",
                "nl": "Frans",
                "de": "Französisch"
            }),
            ('http://publications.europa.eu/resource/authority/language/ENG', {
                "en": "English",
                "fr": "Anglais",
                "nl": "Engels",
                "de": "Englisch"
            }),
            ('http://publications.europa.eu/resource/authority/language/NLD', {
                "en": "Dutch",
                "fr": "Néerlandais",
                "nl": "Nederlands",
                "de": "Niederländisch"
            }),
            ('http://publications.europa.eu/resource/authority/language/DEU', {
                "en": "German",
                "fr": "Allemand",
                "nl": "Duits",
                "de": "Deutsch"
            }),
        ])

    elif ontology == "EU-language":
        return map_for_form_select([
            ('http://publications.europa.eu/resource/authority/language/BUL', {
                "en": "Bulgarian",
                "fr": "Bulgare",
                "nl": "Bulgaars",
                "de": "Bulgarisch"
            }),
            ('http://publications.europa.eu/resource/authority/language/HRV', {
                "en": "Croatian",
                "fr": "Croate",
                "nl": "Kroatisch",
                "de": "Kroatisch"
            }),
            ('http://publications.europa.eu/resource/authority/language/CES', {
                "en": "Czech",
                "fr": "Tchèque",
                "nl": "Tsjechisch",
                "de": "Tschechisch"
            }),
            ('http://publications.europa.eu/resource/authority/language/DAN', {
                "en": "Danish",
                "fr": "Danois",
                "nl": "Deens",
                "de": "Dänisch"
            }),
            ('http://publications.europa.eu/resource/authority/language/NLD', {
                "en": "Dutch",
                "fr": "Néerlandais",
                "nl": "Nederlands",
                "de": "Niederländisch"
            }),
            ('http://publications.europa.eu/resource/authority/language/ENG', {
                "en": "English",
                "fr": "Anglais",
                "nl": "Engels",
                "de": "Englisch"
            }),
            ('http://publications.europa.eu/resource/authority/language/EST', {
                "en": "Estonian",
                "fr": "Estonien",
                "nl": "Ests",
                "de": "Estnisch"
            }),
            ('http://publications.europa.eu/resource/authority/language/FIN', {
                "en": "Finnish",
                "fr": "Finnois",
                "nl": "Fins",
                "de": "Finnisch"
            }),
            ('http://publications.europa.eu/resource/authority/language/FRA', {
                "en": "French",
                "fr": "Français",
                "nl": "Frans",
                "de": "Französisch"
            }),
            ('http://publications.europa.eu/resource/authority/language/DEU', {
                "en": "German",
                "fr": "Allemand",
                "nl": "Duits",
                "de": "Deutsch"
            }),
            ('http://publications.europa.eu/resource/authority/language/ELL', {
                "en": "Greek",
                "fr": "Grec",
                "nl": "Grieks",
                "de": "Griechisch"
            }),
            ('http://publications.europa.eu/resource/authority/language/HUN', {
                "en": "Hungarian",
                "fr": "Hongrois",
                "nl": "Hongaars",
                "de": "Ungarisch"
            }),
            ('http://publications.europa.eu/resource/authority/language/GLE', {
                "en": "Irish",
                "fr": "Irlandais",
                "nl": "Iers",
                "de": "Irisch"
            }),
            ('http://publications.europa.eu/resource/authority/language/ITA', {
                "en": "Italian",
                "fr": "Italien",
                "nl": "Italiaans",
                "de": "Italienisch"
            }),
            ('http://publications.europa.eu/resource/authority/language/LAV', {
                "en": "Latvian",
                "fr": "Letton",
                "nl": "Lets",
                "de": "Lettisch"
            }),
            ('http://publications.europa.eu/resource/authority/language/LIT', {
                "en": "Lithuanian",
                "fr": "Lituanien",
                "nl": "Litouws",
                "de": "Litauisch"
            }),
            ('http://publications.europa.eu/resource/authority/language/MLT', {
                "en": "Maltese",
                "fr": "Maltais",
                "nl": "Maltees",
                "de": "Maltesisch"
            }),
            ('http://publications.europa.eu/resource/authority/language/POL', {
                "en": "Polish",
                "fr": "Polonais",
                "nl": "Pools",
                "de": "Polnisch"
            }),
            ('http://publications.europa.eu/resource/authority/language/POR', {
                "en": "Portuguese",
                "fr": "Portugais",
                "nl": "Portugees",
                "de": "Portugiesisch"
            }),
            ('http://publications.europa.eu/resource/authority/language/RON', {
                "en": "Romanian",
                "fr": "Roumain",
                "nl": "Roemeens",
                "de": "Rumänisch"
            }),
            ('http://publications.europa.eu/resource/authority/language/SLK', {
                "en": "Slovak",
                "fr": "Slovaque",
                "nl": "Slowaaks",
                "de": "Slowakisch"
            }),
            ('http://publications.europa.eu/resource/authority/language/SLV', {
                "en": "Slovenian",
                "fr": "Slovène",
                "nl": "Sloveens",
                "de": "Slowenisch"
            }),
            ('http://publications.europa.eu/resource/authority/language/SPA', {
                "en": "Spanish",
                "fr": "Espagnol",
                "nl": "Spaans",
                "de": "Spanisch"
            }),
            ('http://publications.europa.eu/resource/authority/language/SWE', {
                "en": "Swedish",
                "fr": "Suédois",
                "nl": "Zweeds",
                "de": "Schwedisch"
            }),
        ])
    elif ontology == "EU_COUNTRY":
        return map_for_form_select([
            ('http://publications.europa.eu/resource/authority/country/BEL', {
                "en": "Belgium",
                "fr": "Belgique",
                "nl": "België",
                "de": "Belgien"
            }),
            ('http://publications.europa.eu/resource/authority/country/NLD', {
                "en": "Netherlands",
                "fr": "Pays-Bas",
                "nl": "Nederland",
                "de": "Niederlande"
            }),
            ('http://publications.europa.eu/resource/authority/country/FRA', {
                "en": "France",
                "fr": "France",
                "nl": "Frankrijk",
                "de": "Frankreich"
            }),
            ('http://publications.europa.eu/resource/authority/country/DEU', {
                "en": "Germany",
                "fr": "Allemagne",
                "nl": "Duitsland",
                "de": "Deutschland"
            }),
            ('http://publications.europa.eu/resource/authority/country/LUX', {
                "en": "Luxembourg",
                "fr": "Luxembourg",
                "nl": "Luxemburg",
                "de": "Luxemburg"
            }),
            ('http://publications.europa.eu/resource/authority/country/GBR', {
                "en": "United Kingdom",
                "fr": "Royaume-Uni",
                "nl": "Verenigd Koninkrijk",
                "de": "Vereinigtes Königreich"
            }),
            ('http://publications.europa.eu/resource/authority/country/BGR', {
                "en": "Bulgaria",
                "fr": "Bulgarie",
                "nl": "Bulgarije",
                "de": "Bulgarien"
            }),
            ('http://publications.europa.eu/resource/authority/country/CZE', {
                "en": "Czechia",
                "fr": "Tchéquie",
                "nl": "Tsjechië",
                "de": "Tschechien"
            }),
            ('http://publications.europa.eu/resource/authority/country/DNK', {
                "en": "Denmark",
                "fr": "Danemark",
                "nl": "Denemarken",
                "de": "Dänemark"
            }),
            ('http://publications.europa.eu/resource/authority/country/EST', {
                "en": "Estonia",
                "fr": "Estonie",
                "nl": "Estland",
                "de": "Estland"
            }),
            ('http://publications.europa.eu/resource/authority/country/IRL', {
                "en": "Ireland",
                "fr": "Irlande",
                "nl": "Ierland",
                "de": "Irland"
            }),
            ('http://publications.europa.eu/resource/authority/country/GRC', {
                "en": "Greece",
                "fr": "Grèce",
                "nl": "Griekenland",
                "de": "Griechenland"
            }),
            ('http://publications.europa.eu/resource/authority/country/ESP', {
                "en": "Spain",
                "fr": "Espagne",
                "nl": "Spanje",
                "de": "Spanien"
            }),
            ('http://publications.europa.eu/resource/authority/country/HRV', {
                "en": "Croatia",
                "fr": "Croatie",
                "nl": "Kroatië",
                "de": "Kroatien"
            }),
            ('http://publications.europa.eu/resource/authority/country/ITA', {
                "en": "Italy",
                "fr": "Italie",
                "nl": "Italië",
                "de": "Italien"
            }),
            ('http://publications.europa.eu/resource/authority/country/CYP', {
                "en": "Cyprus",
                "fr": "Chypre",
                "nl": "Cyprus",
                "de": "Zypern"
            }),
            ('http://publications.europa.eu/resource/authority/country/LVA', {
                "en": "Latvia",
                "fr": "Lettonie",
                "nl": "Letland",
                "de": "Lettland"
            }),
            ('http://publications.europa.eu/resource/authority/country/LTU', {
                "en": "Lithuania",
                "fr": "Lituanie",
                "nl": "Litouwen",
                "de": "Litauen"
            }),
            ('http://publications.europa.eu/resource/authority/country/HUN', {
                "en": "Hungary",
                "fr": "Hongrie",
                "nl": "Hongarije",
                "de": "Ungarn"
            }),
            ('http://publications.europa.eu/resource/authority/country/MLT', {
                "en": "Malta",
                "fr": "Malte",
                "nl": "Malta",
                "de": "Malta"
            }),
            ('http://publications.europa.eu/resource/authority/country/AUT', {
                "en": "Austria",
                "fr": "Autriche",
                "nl": "Oostenrijk",
                "de": "Österreich"
            }),
            ('http://publications.europa.eu/resource/authority/country/POL', {
                "en": "Poland",
                "fr": "Pologne",
                "nl": "Polen",
                "de": "Polen"
            }),
            ('http://publications.europa.eu/resource/authority/country/PRT', {
                "en": "Portugal",
                "fr": "Portugal",
                "nl": "Portugal",
                "de": "Portugal"
            }),
            ('http://publications.europa.eu/resource/authority/country/ROU', {
                "en": "Romania",
                "fr": "Roumanie",
                "nl": "Roemenië",
                "de": "Rumänien"
            }),
            ('http://publications.europa.eu/resource/authority/country/SVN', {
                "en": "Slovenia",
                "fr": "Slovénie",
                "nl": "Slovenië",
                "de": "Slowenien"
            }),
            ('http://publications.europa.eu/resource/authority/country/SVK', {
                "en": "Slovakia",
                "fr": "Slovaquie",
                "nl": "Slowakije",
                "de": "Slowakei"
            }),
            ('http://publications.europa.eu/resource/authority/country/FIN', {
                "en": "Finland",
                "fr": "Finlande",
                "nl": "Finland",
                "de": "Finnland"
            }),
            ('http://publications.europa.eu/resource/authority/country/SWE', {
                "en": "Sweden",
                "fr": "Suède",
                "nl": "Zweden",
                "de": "Schweden"
            }),
        ])
    elif ontology == "NUTS1_BE":
        return map_for_form_select(NUTS1_BE)
    elif ontology == "NUTS3_BE":
        return map_for_form_select([
            ('http://data.europa.eu/nuts/code/BE100', {
                "en": "Arr. de Bruxelles-Capitale / Arr. van Brussel-Hoofdstad",
                "fr": "Arr. de Bruxelles-Capitale / Arr. van Brussel-Hoofdstad",
                "nl": "Arr. de Bruxelles-Capitale / Arr. van Brussel-Hoofdstad",
                "de": "Arr. de Bruxelles-Capitale / Arr. van Brussel-Hoofdstad"
            }),
            ('http://data.europa.eu/nuts/code/BE211', {
                "en": "Arr. Antwerpen",
                "fr": "Arr. Antwerpen",
                "nl": "Arr. Antwerpen",
                "de": "Arr. Antwerpen"
            }),
            ('http://data.europa.eu/nuts/code/BE212', {
                "en": "Arr. Mechelen",
                "fr": "Arr. Mechelen",
                "nl": "Arr. Mechelen",
                "de": "Arr. Mechelen"
            }),
            ('http://data.europa.eu/nuts/code/BE213', {
                "en": "Arr. Turnhout",
                "fr": "Arr. Turnhout",
                "nl": "Arr. Turnhout",
                "de": "Arr. Turnhout"
            }),
            ('http://data.europa.eu/nuts/code/BE221', {
                "en": "Arr. Hasselt",
                "fr": "Arr. Hasselt",
                "nl": "Arr. Hasselt",
                "de": "Arr. Hasselt"
            }),
            ('http://data.europa.eu/nuts/code/BE222', {
                "en": "Arr. Maaseik",
                "fr": "Arr. Maaseik",
                "nl": "Arr. Maaseik",
                "de": "Arr. Maaseik"
            }),
            ('http://data.europa.eu/nuts/code/BE223', {
                "en": "Arr. Tongeren",
                "fr": "Arr. Tongeren",
                "nl": "Arr. Tongeren",
                "de": "Arr. Tongeren"
            }),
            ('http://data.europa.eu/nuts/code/BE231', {
                "en": "Arr. Aalst",
                "fr": "Arr. Aalst",
                "nl": "Arr. Aalst",
                "de": "Arr. Aalst"
            }),
            ('http://data.europa.eu/nuts/code/BE232', {
                "en": "Arr. Dendermonde",
                "fr": "Arr. Dendermonde",
                "nl": "Arr. Dendermonde",
                "de": "Arr. Dendermonde"
            }),
            ('http://data.europa.eu/nuts/code/BE233', {
                "en": "Arr. Eeklo",
                "fr": "Arr. Eeklo",
                "nl": "Arr. Eeklo",
                "de": "Arr. Eeklo"
            }),
            ('http://data.europa.eu/nuts/code/BE234', {
                "en": "Arr. Gent",
                "fr": "Arr. Gent",
                "nl": "Arr. Gent",
                "de": "Arr. Gent"
            }),
            ('http://data.europa.eu/nuts/code/BE235', {
                "en": "Arr. Oudenaarde",
                "fr": "Arr. Oudenaarde",
                "nl": "Arr. Oudenaarde",
                "de": "Arr. Oudenaarde"
            }),
            ('http://data.europa.eu/nuts/code/BE236', {
                "en": "Arr. Sint-Niklaas",
                "fr": "Arr. Sint-Niklaas",
                "nl": "Arr. Sint-Niklaas",
                "de": "Arr. Sint-Niklaas"
            }),
            ('http://data.europa.eu/nuts/code/BE241', {
                "en": "Arr. Halle-Vilvoorde",
                "fr": "Arr. Halle-Vilvoorde",
                "nl": "Arr. Halle-Vilvoorde",
                "de": "Arr. Halle-Vilvoorde"
            }),
            ('http://data.europa.eu/nuts/code/BE242', {
                "en": "Arr. Leuven",
                "fr": "Arr. Leuven",
                "nl": "Arr. Leuven",
                "de": "Arr. Leuven"
            }),
            ('http://data.europa.eu/nuts/code/BE251', {
                "en": "Arr. Brugge",
                "fr": "Arr. Brugge",
                "nl": "Arr. Brugge",
                "de": "Arr. Brugge"
            }),
            ('http://data.europa.eu/nuts/code/BE252', {
                "en": "Arr. Diksmuide",
                "fr": "Arr. Diksmuide",
                "nl": "Arr. Diksmuide",
                "de": "Arr. Diksmuide"
            }),
            ('http://data.europa.eu/nuts/code/BE253', {
                "en": "Arr. Ieper",
                "fr": "Arr. Ieper",
                "nl": "Arr. Ieper",
                "de": "Arr. Ieper"
            }),
            ('http://data.europa.eu/nuts/code/BE254', {
                "en": "Arr. Kortrijk",
                "fr": "Arr. Kortrijk",
                "nl": "Arr. Kortrijk",
                "de": "Arr. Kortrijk"
            }),
            ('http://data.europa.eu/nuts/code/BE255', {
                "en": "Arr. Oostende",
                "fr": "Arr. Oostende",
                "nl": "Arr. Oostende",
                "de": "Arr. Oostende"
            }),
            ('http://data.europa.eu/nuts/code/BE256', {
                "en": "Arr. Roeselare",
                "fr": "Arr. Roeselare",
                "nl": "Arr. Roeselare",
                "de": "Arr. Roeselare"
            }),
            ('http://data.europa.eu/nuts/code/BE257', {
                "en": "Arr. Tielt",
                "fr": "Arr. Tielt",
                "nl": "Arr. Tielt",
                "de": "Arr. Tielt"
            }),
            ('http://data.europa.eu/nuts/code/BE258', {
                "en": "Arr. Veurne",
                "fr": "Arr. Veurne",
                "nl": "Arr. Veurne",
                "de": "Arr. Veurne"
            }),
            ('http://data.europa.eu/nuts/code/BE310', {
                "en": "Arr. Nivelles",
                "fr": "Arr. Nivelles",
                "nl": "Arr. Nivelles",
                "de": "Arr. Nivelles"
            }),
            ('http://data.europa.eu/nuts/code/BE321', {
                "en": "Arr. Ath",
                "fr": "Arr. Ath",
                "nl": "Arr. Ath",
                "de": "Arr. Ath"
            }),
            ('http://data.europa.eu/nuts/code/BE322', {
                "en": "Arr. Charleroi",
                "fr": "Arr. Charleroi",
                "nl": "Arr. Charleroi",
                "de": "Arr. Charleroi"
            }),
            ('http://data.europa.eu/nuts/code/BE323', {
                "en": "Arr. Mons",
                "fr": "Arr. Mons",
                "nl": "Arr. Mons",
                "de": "Arr. Mons"
            }),
            ('http://data.europa.eu/nuts/code/BE324', {
                "en": "Arr. Mouscron",
                "fr": "Arr. Mouscron",
                "nl": "Arr. Mouscron",
                "de": "Arr. Mouscron"
            }),
        ])

    elif ontology == "encoding":
        return map_for_form_select([
            ('ASCII', {
                "en": "ASCII",
                "fr": "ASCII",
                "nl": "ASCII",
                "de": "ASCII"
            }),
            ('UTF-8', {
                "en": "UTF-8",
                "fr": "UTF-8",
                "nl": "UTF-8",
                "de": "UTF-8"
            }),
            ('UTF-16', {
                "en": "UTF-16",
                "fr": "UTF-16",
                "nl": "UTF-16",
                "de": "UTF-16"
            }),
            ('ISO-8859-1', {
                "en": "ISO-8859-1",
                "fr": "ISO-8859-1",
                "nl": "ISO-8859-1",
                "de": "ISO-8859-1"
            }),
            ('ISO-8859-15', {
                "en": "ISO-8859-15",
                "fr": "ISO-8859-15",
                "nl": "ISO-8859-15",
                "de": "ISO-8859-15"
            }),
            ('Other', {
                "en": "Other",
                "fr": "Autre",
                "nl": "Andere",
                "de": "Andere"
            }),
        ])

    elif ontology == "syntax":
        return map_for_form_select([
            ('XML', {
                "en": "XML",
                "fr": "XML",
                "nl": "XML",
                "de": "XML"
            }),
            ('JSON', {
                "en": "JSON",
                "fr": "JSON",
                "nl": "JSON",
                "de": "JSON"
            }),
            ('CSV', {
                "en": "CSV",
                "fr": "CSV",
                "nl": "CSV",
                "de": "CSV"
            }),
            ('ASN.1 encoding rules', {
                "en": "ASN.1 encoding rules",
                "fr": "Règles d'encodage d'ASN.1",
                "nl": "ASN.1 coderingsregels",
                "de": "ASN.1 Kodierunsregel"
            }),
            ('Protocol buffers', {
                "en": "Protocol buffers",
                "fr": "Tampons de protocole",
                "nl": "Protocolbuffers",
                "de": "Protokoll-Buffer"
            }),
            ('Other', {
                "en": "Other",
                "fr": "Autre",
                "nl": "Andere",
                "de": "Andere"
            }),
        ])

    elif ontology == "grammar":
        return map_for_form_select([
            ('http://publications.europa.eu/resource/authority/file-type/SCHEMA_XML', {
                "en": "XSD",
                "fr": "XSD",
                "nl": "XSD",
                "de": "XSD"
            }),
            ('JSON Schema', {
                "en": "JSON Schema",
                "fr": "Schéma JSON",
                "nl": "JSON-schema",
                "de": "JSON-Schema"
            }),
            ('http://purl.org/ASN/schema/core/StandardDocument', {
                "en": "ASN.1",
                "fr": "ASN.1",
                "nl": "ASN.1",
                "de": "ASN.1"
            }),
            ('Protocol buffers', {
                "en": "Protocol buffers",
                "fr": "Tampons de protocole",
                "nl": "Protocolbuffers",
                "de": "Protokoll-Buffer"
            }),
            ('Other', {
                "en": "Other",
                "fr": "Autre",
                "nl": "Andere",
                "de": "Andere"
            }),
        ])

    elif ontology == "datamodel":
        return map_for_form_select([
            ('DATEX II profile', {
                "en": "DATEX II profile",
                "fr": "Profil DATEX II",
                "nl": "DATEX II profiel",
                "de": "DATEX II-Profil"
            }),
            ('OCIT-C', {
                "en": "OCIT-C",
                "fr": "OCIT-C",
                "nl": "OCIT-C",
                "de": "OCIT-C"
            }),
            ('DATEX II Light', {
                "en": "DATEX II Light",
                "fr": "DATEX II Light",
                "nl": "DATEX II Light",
                "de": "DATEX II Light"
            }),
            ('NeTEX', {
                "en": "NeTEX (CEN/TS 16614)",
                "fr": "NeTEX (CEN/TS 16614)",
                "nl": "NeTEX (CEN/TS 16614)",
                "de": "NeTEX (CEN/TS 16614)"
            }),
            ('SIRI', {
                "en": "SIRI (CEN/TS 15531)",
                "fr": "SIRI (CEN/TS 15531)",
                "nl": "SIRI (CEN/TS 15531)",
                "de": "SIRI (CEN/TS 15531)"
            }),
            ('GTFS', {
                "en": "GTFS",
                "fr": "GTFS",
                "nl": "GTFS",
                "de": "GTFS"
            }),
            ('GBFS', {
                "en": "GBFS",
                "fr": "GBFS",
                "nl": "GBFS",
                "de": "GBFS"
            }),
            ('MDS', {
                "en": "MDS",
                "fr": "MDS",
                "nl": "MDS",
                "de": "MDS"
            }),
            ('VDV Standard', {
                "en": "VDV Standard (VDV 452, 455, 462,…)",
                "fr": "VDV Standard (VDV 452, 455, 462,…)",
                "nl": "VDV Standard (VDV 452, 455, 462,…)",
                "de": "VDV Standard (VDV 452, 455, 462,…)"
            }),
            ('IFOPT', {
                "en": "IFOPT",
                "fr": "IFOPT",
                "nl": "IFOPT",
                "de": "IFOPT"
            }),
            ('ETSI / ISO Model', {
                "en": "ETSI / ISO Model (DENM, CAM, SPAT/MAP, IVI,…)",
                "fr": "ETSI / ISO Model (DENM, CAM, SPAT/MAP, IVI,…)",
                "nl": "ETSI / ISO Model (DENM, CAM, SPAT/MAP, IVI,…)",
                "de": "ETSI / ISO Model (DENM, CAM, SPAT/MAP, IVI,…)"
            }),
            ('tpegML Model', {
                "en": "tpegML Model (TPEG2-TEC, TPEG2-PKI,…)",
                "fr": "tpegML Model (TPEG2-TEC, TPEG2-PKI,…)",
                "nl": "tpegML Model (TPEG2-TEC, TPEG2-PKI,…)",
                "de": "tpegML Model (TPEG2-TEC, TPEG2-PKI,…)"
            }),
            ('http://publications.europa.eu/resource/authority/file-type/KML', {
                "en": "KML",
                "fr": "KML",
                "nl": "KML",
                "de": "KML"
            }),

            ('http://publications.europa.eu/resource/authority/file-type/MPEG4', {
                "en": "MPEG-4",
                "fr": "MPEG-4",
                "nl": "MPEG-4",
                "de": "MPEG-4"
            }),
            ('MDM-Container', {
                "en": "MDM-Container",
                "fr": "MDM-Container",
                "nl": "MDM-Container",
                "de": "MDM-Container"
            }),
            ('DINO', {
                "en": "DINO",
                "fr": "DINO",
                "nl": "DINO",
                "de": "DINO"
            }),
            ('OpenAPI', {
                "en": "OpenAPI",
                "fr": "OpenAPI",
                "nl": "OpenAPI",
                "de": "OpenAPI"
            }),
            ('Other', {
                "en": "Other",
                "fr": "Autre",
                "nl": "Andere",
                "de": "Andere"
            }),
        ])

    elif ontology == "protocol":
        return map_for_form_select([
            ('SOAP', {
                "en": "SOAP",
                "fr": "SOAP",
                "nl": "SOAP",
                "de": "SOAP"
            }),
            ('OTS2', {
                "en": "OTS2",
                "fr": "OTS2",
                "nl": "OTS2",
                "de": "OTS2"
            }),
            ('http://publications.europa.eu/resource/authority/file-type/MSG_HTTP', {
                "en": "HTTP/HTTPS",
                "fr": "HTTP/HTTPS",
                "nl": "HTTP/HTTPS",
                "de": "HTTP/HTTPS"
            }),
            ('FTP', {
                "en": "FTP",
                "fr": "FTP",
                "nl": "FTP",
                "de": "FTP"
            }),
            ('http://publications.europa.eu/resource/authority/file-type/RSS', {
                "en": "RSS",
                "fr": "RSS",
                "nl": "RSS",
                "de": "RSS"
            }),
            ('AMQP', {
                "en": "AMQP",
                "fr": "AMQP",
                "nl": "AMQP",
                "de": "AMQP"
            }),
            ('MQTT', {
                "en": "MQTT",
                "fr": "MQTT",
                "nl": "MQTT",
                "de": "MQTT"
            }),
            ('gRPC', {
                "en": "gRPC",
                "fr": "gRPC",
                "nl": "gRPC",
                "de": "gRPC"
            }),
            ('Other', {
                "en": "Other",
                "fr": "Autre",
                "nl": "Andere",
                "de": "Andere"
            }),
        ])

    elif ontology == "communication":
        return map_for_form_select([
            ('Push', {
                "en": "Push",
                "fr": "Push",
                "nl": "Push",
                "de": "Push"
            }),
            ('Push on occurence', {
                "en": "Push on occurrence",
                "fr": "Push on occurrence",
                "nl": "Push on occurrence",
                "de": "Push on occurrence"
            }),
            ('Pull', {
                "en": "Pull",
                "fr": "Pull",
                "nl": "Pull",
                "de": "Pull"
            }),
        ])
    elif ontology == "contract_license":
        return map_for_form_select([
            ('nolinoco', {
                "en": "No license – No contract",
                "fr": "Pas de licence - Pas de contrat",
                "nl": "Geen licentie - Geen contract",
                "de": "Keine Lizenz - Kein Vertrag"
            }),
            ('lifree', {
                "en": "Licence and Free of charge",
                "fr": "Licence et gratuit",
                "nl": "Licentie en gratis",
                "de": "Lizenz und kostenlos"
            }),
            ('linotfree', {
                "en": "Licence and Fee",
                "fr": "Licence et frais",
                "nl": "Licentie en vergoeding",
                "de": "Lizenz und Gebühr"
            }),
            ('cofree', {
                "en": "Contract and Free of charge",
                "fr": "Contrat et gratuit",
                "nl": "Contract en gratis",
                "de": "Vertrag und kostenlos"
            }),
            ('conotfree', {
                "en": "Contract and Fee",
                "fr": "Contrat et frais",
                "nl": "Contract en vergoeding",
                "de": "Vertrag und Gebühr"
            }),
            ('notrelevant', {
                "en": "Not relevant",
                "fr": "Non pertinent",
                "nl": "Niet relevant",
                "de": "Nicht relevant"
            }),
        ])

    elif ontology == "data-theme":
        return map_for_form_select([
            ('http://publications.europa.eu/resource/authority/data-theme/TRAN', {
                "en": "Transport",
                "fr": "Transports",
                "nl": "Vervoer",
                "de": "Verkehr"
            })
        ])
    elif ontology == "frequency":
        return map_for_form_select([
            ('On occurence', {
                "en": "On occurence",
                "fr": "Dès que disponible",
                "nl": "Zodra beschikbaar",
                "de": "sofort"
            }),
            ('Up to 1min', {
                "en": "Up to 1min",
                "fr": "Jusqu'à une fois par minute",
                "nl": "Tot één keer per minuut",
                "de": "Bis einmal pro Minute"
            }),
            ('Up to 5min', {
                "en": "Up to 5min",
                "fr": "Jusqu'à une fois toutes les 5 minutes",
                "nl": "Tot één keer per 5 minuten",
                "de": "Bis einmal pro 5 Minuten"
            }),
            ('Up to 10min', {
                "en": "Up to 10min",
                "fr": "Jusqu'à une fois toutes les 10 minutes",
                "nl": "Tot één keer per 10 minuten",
                "de": "Bis einmal pro 10 Minuten"
            }),
            ('Up to 15min', {
                "en": "Up to 15min",
                "fr": "Jusqu'à une fois toutes les 15 minutes",
                "nl": "Tot één keer per 15 minuten",
                "de": "Bis einmal pro 15 Minuten"
            }),
            ('http://publications.europa.eu/resource/authority/frequency/BIHOURLY', {
                "en": "Up to 30min",
                "fr": "Jusqu'à une fois toutes les 30 minutes",
                "nl": "Tot één keer per 30 minuten",
                "de": "Bis einmal pro 30 Minuten"
            }),
            ('http://publications.europa.eu/resource/authority/frequency/HOURLY', {
                "en": "Up to 1h",
                "fr": "Jusqu'à une fois toutes les heures",
                "nl": "Tot één keer per uur",
                "de": "Bis einmal pro Stunde"
            }),
            ('Up to 2h', {
                "en": "Up to 2h",
                "fr": "Jusqu'à une fois toutes les 2 heures",
                "nl": "Tot één keer per 2 uren",
                "de": "Bis einmal pro 2 Stunden"
            }),
            ('Up to 3h', {
                "en": "Up to 3h",
                "fr": "Jusqu'à une fois toutes les 3 heures",
                "nl": "Tot één keer per 3 uren",
                "de": "Bis einmal pro 3 Stunden"
            }),
            ('http://publications.europa.eu/resource/authority/frequency/DAILY_2', {
                "en": "Up to 12h",
                "fr": "Jusqu'à une fois toutes les 12 heures",
                "nl": "Tot één keer per 12 uren",
                "de": "Bis einmal pro 12 Stunden"
            }),
            ('http://publications.europa.eu/resource/authority/frequency/DAILY', {
                "en": "Up to 24h",
                "fr": "Jusqu'à une fois toutes les 24 heures",
                "nl": "Tot één keer per 24 uren",
                "de": "Bis einmal pro 24 Stunden"
            }),
            ('http://publications.europa.eu/resource/authority/frequency/WEEKLY', {
                "en": "Up to Weekly",
                "fr": "Jusqu'à une fois par semaine",
                "nl": "Tot één keer per week",
                "de": "Bis einmal pro Woche"
            }),
            ('http://publications.europa.eu/resource/authority/frequency/MONTHLY', {
                "en": "Up to Monthly",
                "fr": "Jusqu'à une fois par mois",
                "nl": "Tot één keer per maand",
                "de": "Bis einmal pro Monat"
            }),
            ('http://publications.europa.eu/resource/authority/frequency/QUARTERLY', {
                "en": "Up to every 3month",
                "fr": "Jusqu'à une fois tous les trois mois",
                "nl": "Tot één keer per drie maanden",
                "de": "Bis einmal pro drei Monaten"
            }),
            ('http://publications.europa.eu/resource/authority/frequency/ANNUAL_2', {
                "en": "Up to every 6month",
                "fr": "Jusqu'à une fois tous les six mois",
                "nl": "Tot één keer per zes maanden",
                "de": "Bis einmal pro sechs Monaten"
            }),
            ('http://publications.europa.eu/resource/authority/frequency/ANNUAL', {
                "en": "Up to yearly",
                "fr": "Jusqu'à une fois par an",
                "nl": "Tot één keer per jaar",
                "de": "Bis einmal pro Jahr"
            }),
            ('Less frequent than yearly', {
                "en": "Less frequent than yearly",
                "fr": "Moins qu'une fois par an",
                "nl": "Minder vaak dan één keer per jaar ",
                "de": "Weniger häufig als einmal pro Jahr"
            }),

        ])
    elif ontology == "georeferencing_method":
        return map_for_form_select(GEOREFERENCING_METHOD)
    elif ontology == "dataset_type":
        return map_for_form_select(DATASET_TYPE)
    elif ontology == "nap_type":
        return map_for_form_select(NAP_TYPE)

    return None



def get_helpers():
    return {
        "benap_ontology_helper": ontology_helper,
    }
