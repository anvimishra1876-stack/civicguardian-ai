import json


class EligibilityAgent:

    def __init__(self):
        with open("data/schemes.json", "r") as f:
            self.schemes = json.load(f)

    def check(self, occupation, income):

        eligible = []

        for scheme in self.schemes:

            if (
                scheme["category"].lower()
                == occupation.lower()
                and income <= scheme["income_limit"]
            ):
                eligible.append(scheme)

        return eligible