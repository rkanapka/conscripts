from types import MappingProxyType

import requests


class Conscripts:
    regions: MappingProxyType = MappingProxyType(
        {
            "Alytus": 1,
            "Kaunas": 2,
            "Klaipeda": 3,
            "Panevezys": 4,
            "Siauliai": 5,
            "Vilnius": 6,
        }
    )
    base_url: str = "https://sauktiniai.karys.lt/"
    headers: dict = {
        "Range": "0-100000",
        "Referer": base_url,
    }
    responses: dict = {}

    def get_conscripts(self) -> dict:
        for region_name, region_number in self.regions.items():
            url = f"{self.base_url}list.php?region={region_number}"
            response = requests.get(url, headers=self.headers).json()
            self.responses[region_name] = response
        return self.responses
