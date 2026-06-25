class SchemeAgent:

    def format_schemes(self, schemes):

        if not schemes:
            return "No matching schemes found."

        result = ""

        for scheme in schemes:

            result += f"""
Scheme: {scheme['name']}

Required Documents:
{", ".join(scheme['documents'])}

--------------------
"""

        return result