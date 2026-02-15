import uuid


def generate_trace_id() -> str:
    return f"DEC-{uuid.uuid4().hex[:8].upper()}"
