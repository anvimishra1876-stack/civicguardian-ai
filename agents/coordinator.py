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

        # Agent 1
        eligible_schemes = (
            self.eligibility_agent.check(
                occupation,
                income
            )
        )

        # Agent 2
        formatted_schemes = (
            self.scheme_agent.format_schemes(
                eligible_schemes
            )
        )

        # Agent 3
        explanation = (
            self.explainer_agent.explain(
                occupation,
                income,
                formatted_schemes
            )
        )

        return {
            "eligible_schemes": eligible_schemes,
            "formatted_schemes": formatted_schemes,
            "explanation": explanation
        }