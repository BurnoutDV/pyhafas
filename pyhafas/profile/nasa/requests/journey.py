from typing import Dict, List

from pyhafas.profile import ProfileInterface
from pyhafas.profile.base import BaseJourneyRequest
from pyhafas.profile.interfaces.requests.journey import JourneyRequestInterface
from pyhafas.types.fptf import Journey
from pyhafas.types.hafas_response import HafasResponse


class NASAJourneyRequest(BaseJourneyRequest, JourneyRequestInterface):
    def format_journey_request(
            self: ProfileInterface,
            journey: Journey) -> dict:
        """
        Creates the HaFAS (NASA-deployment) request for refreshing journey details

        :param journey: Id of the journey (ctxRecon)
        :return: Request for HaFAS (NASA-deployment)
        """
        return {
            'req': {
                'outReconL': [{
                    'ctx': journey.id
                }]
            },
            'meth': 'Reconstruction'
        }

    def parse_journeys_request(
            self: ProfileInterface,
            data: HafasResponse) -> List[Journey]:
        """
        Parses the HaFAS response for a journeys request

        :param data: Formatted HaFAS response
        :return: List of Journey objects
        """
        journeys = []

        for jny in data.res['outConL']:
            # TODO: Add more data
            date = self.parse_date(jny['date'])
            journeys.append(
                Journey(
                    jny['recon']['ctx'], date=date, duration=self.parse_timedelta(
                        jny['dur']), legs=self.parse_legs(
                        jny, data.common, date)))
        return journeys