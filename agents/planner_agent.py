class PlannerAgent:

    def create_plan(
        self,
        required_docs,
        uploaded_docs
    ):

        missing_docs = []

        for doc in required_docs:

            if doc not in uploaded_docs:
                missing_docs.append(doc)

        plan = ""

        plan += "## Document Status\n\n"

        plan += "Uploaded Documents:\n"

        if uploaded_docs:

            for doc in uploaded_docs:
                plan += f"✅ {doc}\n"

        else:
            plan += "None\n"

        plan += "\n\nMissing Documents:\n"

        if missing_docs:

            for doc in missing_docs:
                plan += f"❌ {doc}\n"

        else:
            plan += "None\n"

        plan += "\n\nAction Plan:\n"

        step = 1

        for doc in missing_docs:

            plan += (
                f"\n{step}. Obtain {doc}"
            )

            step += 1

        if not missing_docs:

            plan += (
                "\nAll required documents are available."
            )

        return plan