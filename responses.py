import random


def handle_response(user_id, message) -> str:
    print(f"message : {message}")
    p_message = message.lower()

    if "chu" in message:
        return f"Get Some Help <@{user_id}>"

    if "hello" in message:
        return 'Halo.. siapa km? >:('

    if "roll dice" in message:
        return str(random.randint(1, 6))

    if "roll double dice" in message:
        return str(random.randint(1, 12))

    if "help" in message:
        return "Get Some Help!"

    return "Ngomong apa kamu? >:("
