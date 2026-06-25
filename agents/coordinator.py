from agents.eligibility_agent import EligibilityAgent
from agents.scheme_agent import SchemeAgent


class CoordinatorAgent:

    def __init__(self):

        self.eligibility_agent = EligibilityAgent()
        self.scheme_agent = SchemeAgent()

    def process(self, occupation, income):

        schemes = self.eligibility_agent.check(
            occupation,
            income
        )

        return self.scheme_agent.format_schemes(
            schemes
        )