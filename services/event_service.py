from db.mongo import events_collection
from models.event_model import create_event_document
from utils.date_utils import format_utc_timestamp


def handle_push_event(payload):
    request_id = payload["after"]

    # Prevent duplicates
    existing = events_collection.find_one({"request_id": request_id})
    if existing:
        return

    author = payload["pusher"]["name"]
    to_branch = payload["ref"].split("/")[-1]
    timestamp = format_utc_timestamp(payload["head_commit"]["timestamp"])
    event = create_event_document(
        request_id=request_id,
        author=author,
        action="PUSH",
        from_branch=None,
        to_branch=to_branch,
        timestamp=timestamp
    )

    events_collection.insert_one(event)

def handle_pull_request_event(payload):
    action_type = payload.get("action")

    # Only care about newly opened PRs
    if action_type != "opened":
        return

    pr = payload["pull_request"]
    request_id = str(pr["id"])

    # Prevent duplicates
    existing = events_collection.find_one({"request_id": request_id})
    if existing:
        return

    author = pr["user"]["login"]
    from_branch = pr["head"]["ref"]
    to_branch = pr["base"]["ref"]
    timestamp = format_utc_timestamp(pr["created_at"])

    event = create_event_document(
        request_id=request_id,
        author=author,
        action="PULL_REQUEST",
        from_branch=from_branch,
        to_branch=to_branch,
        timestamp=timestamp
    )

    events_collection.insert_one(event)

def handle_merge_event(payload):
    if payload.get("action") != "closed":
        return
    pr = payload.get("pull_request")
    if not pr or not pr.get("merged"):
        return

    request_id = f"merge-{pr['id']}"
    if events_collection.find_one({"request_id": request_id}):
        return

    event = create_event_document(
        request_id=request_id,
        author=pr["user"]["login"],
        action="MERGE",
        from_branch=pr["head"]["ref"],
        to_branch=pr["base"]["ref"],
        timestamp=format_utc_timestamp(pr["merged_at"])
    )
    events_collection.insert_one(event)
