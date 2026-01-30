from flask import Blueprint, request, jsonify
from services.event_service import (
    handle_push_event,
    handle_pull_request_event,
    handle_merge_event
)

webhook_bp = Blueprint("webhook", __name__)

@webhook_bp.route("/webhook", methods=["POST"])
def handle_webhook():
    event_type = request.headers.get("X-GitHub-Event")
    payload = request.get_json()

    if not event_type or not payload:
        return jsonify({"error": "Invalid webhook"}), 400

    if event_type == "push":
        handle_push_event(payload)

    if event_type == "pull_request":
        handle_pull_request_event(payload)
        handle_merge_event(payload)

    return jsonify({"status": "processed"}), 200
