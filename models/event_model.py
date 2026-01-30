def create_event_document(
    request_id,
    author,
    action,
    from_branch,
    to_branch,
    timestamp
):
    return {
        "request_id": request_id,
        "author": author,
        "action": action,
        "from_branch": from_branch,
        "to_branch": to_branch,
        "timestamp": timestamp
    }
