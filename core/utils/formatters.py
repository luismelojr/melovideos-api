def format_serializer_error(errors: dict) -> str:
    if not errors:
        return "Ocorreu um erro de validação."

    for field, messages in errors.items():
        if field == "non_field_errors":
            field = "erro"

        if isinstance(messages, list) and messages:
            return f"{field}: {messages[0]}"
        elif isinstance(messages, dict):
            nested_message = format_serializer_error(messages)
            return f"{field}: {nested_message}"

    return "Ocorreu um erro de validação."
