from servers.scheme_server import SchemeServer


class SchemeAgent:

    def __init__(self):

        self.server = SchemeServer()

    def find_schemes(
        self,
        occupation
    ):

        return (
            self.server.get_schemes_by_occupation(
                occupation
            )
        )

    def format_schemes(
        self,
        schemes
    ):

        if not schemes:
            return (
                "No matching schemes found."
            )

        result = ""

        for scheme in schemes:

            result += f"""
Scheme: {scheme['name']}

Required Documents:
{", ".join(scheme['documents'])}

--------------------
"""

        return result