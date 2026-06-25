import json


class SchemeServer:

    def get_schemes(self):

        with open(
            "data/schemes.json",
            "r"
        ) as file:

            return json.load(file)

    def get_schemes_by_occupation(
        self,
        occupation
    ):

        schemes = self.get_schemes()

        matches = []

        for scheme in schemes:

            if (
                scheme["category"].lower()
                ==
                occupation.lower()
            ):
                matches.append(scheme)

        return matches