import base64


def revert(
    s: str
) -> str:
    return base64.b32decode(s).decode('utf-8')