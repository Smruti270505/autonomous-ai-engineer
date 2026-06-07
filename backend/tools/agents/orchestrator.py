from tools.agents.planner_agent import planner_agent
from tools.agents.coder_agent import coder_agent
from tools.agents.reviewer_agent import reviewer_agent

def run_multi_agent(task):

    plan = planner_agent(task)

    code_solution = coder_agent(task)

    review = reviewer_agent(code_solution)

    return f"""
=== PLAN ===

{plan}

=== IMPLEMENTATION ===

{code_solution}

=== REVIEW ===

{review}
"""