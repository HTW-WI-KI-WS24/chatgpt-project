skip_command = "/skip"
repeat_command = "/repeat"


def should_skip_process(user_input: str) -> bool:
    user_input = user_input.strip()

    if user_input == skip_command:
        return True

    return False


def should_repeat_process(user_input: str) -> bool:
    user_input = user_input.strip()

    if user_input == repeat_command:
        return True

    return False
