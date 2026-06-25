class PlannerAgent:

    def create_plan(
        self,
        required_docs,
        uploaded_docs
    ):

        missing = []

        for doc in required_docs:

            if doc not in uploaded_docs:
                missing.append(doc)

        plan = "### Action Plan\n\n"

        if missing:

            plan += "Missing Documents:\n"

            for doc in missing:
                plan += f"❌ {doc}\n"

            plan += "\nRecommended Steps:\n"

            step = 1

            for doc in missing:
                plan += (
                    f"{step}. Obtain {doc}\n"
                )
                step += 1

        else:

            plan += (
                "✅ All required documents available.\n"
            )

        return plan