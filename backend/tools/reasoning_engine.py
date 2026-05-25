def generate_reasoning(plan):

    reasoning_steps = []

    for tool in plan:

        reasoning_steps.append(
            f"Detected tool: {tool}"
        )

    return "\n".join(reasoning_steps)