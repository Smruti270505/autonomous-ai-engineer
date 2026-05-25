ACTION_HISTORY = []

def save_action(action):

    ACTION_HISTORY.append(action)

def get_history():

    if not ACTION_HISTORY:
        return "No actions recorded."

    return "\n\n".join(ACTION_HISTORY)