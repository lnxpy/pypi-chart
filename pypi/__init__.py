import requests
import json


class Stats:
    def __init__(self, package_name: str) -> None:
        self.package_name = package_name

    def get_data(self, limit: int):
        # endpoint = f"https://pypistats.org/api/packages/{self.package_name}/overall"

        # r = requests.get(endpoint, params={"mirrors": True}).json()
        from consts import data

        r = json.loads(data)["data"][-limit:]

        return {i["date"][-5:]: i["downloads"] for i in r}
