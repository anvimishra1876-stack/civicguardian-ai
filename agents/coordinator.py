from agents.eligibility_agent import EligibilityAgent
from agents.scheme_agent import SchemeAgent
from agents.explainer_agent import ExplainerAgent


class CoordinatorAgent:

    def __init__(self):

        self.eligibility_agent = EligibilityAgent()
        self.scheme_agent = SchemeAgent()
        self.explainer_agent = ExplainerAgent()

    def process(
        self,
        occupation,
        income
    ):

        schemes = self.eligibility_agent.check(
            occupation,
            income
        )

        formatted = self.scheme_agent.format_schemes(
            schemes
        )

        explanation = (
            self.explainer_agent.explain(
                occupation,
                income,
                formatted
            )
        )

        return explanation