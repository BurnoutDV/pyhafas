import pytz

from pyhafas.profile import BaseProfile
from pyhafas.profile.nasa.requests.journey import NASAJourneyRequest
from pyhafas.profile.nasa.helper.LegHelper import NASAParseLegHelper


class NASAProfile(NASAJourneyRequest, BaseProfile):
    """
    Profile for the HaFAS of " Nahverkehr Sachsen-Anhalt (NASA)" (INSA) - local transportation provider

    Base Profile copied from the VSN Example
    """
    baseUrl = "https://reiseauskunft.insa.de/bin/mgate.exe"
    # https://reiseauskunft.insa.de/bin/mgate.exe?rnd=1655065842564  unix time and rnd parameter?
    defaultUserAgent = "nasa/1.44 (iPhone OS 11.2.5)"

    salt = 'SP31mBufSyCLmNxp'
    addMicMac = False

    locale = 'de-DE'
    timezone = pytz.timezone('Europe/Berlin')

    requestBody = {
        'client': {
            'id': 'NASA',
            'v': '4000200',
            'type': 'IPH',
            'name': 'nasaPROD',
            'os': 'iOS 13.3'
        },
        'ver': '1.44',
        'lang': 'de',
        'auth': {
            'type': 'AID',
            'aid': 'nasa-apps'
        }
    }

    availableProducts = {
        'nationalExpress': [1],  # ICE
        'national': [2],  # IC/EC/CNL
        'regional': [8],  # RE/RB
        'suburban': [16],  # S
        'tram': [32],  # tram
        'bus': [64, 128],  # BUS
        'tourismTrain': [256],  # TT
        'trambus': [512]
    }

    defaultProducts = [
        'nationalExpress',
        'national',
        'regional',
        'suburban',
        'tram'
        'bus',
        'tourismTrain',
        'trambus'
    ]
