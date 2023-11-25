def should_abort_process(user_input: str) -> bool:
    user_input = user_input.strip()

    if user_input == "skip":
        return True

    return False
