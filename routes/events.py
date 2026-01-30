from flask import Blueprint, request, jsonify
from db.mongo import events_collection

events_bp = Blueprint("events", __name__)

@events_bp.route("/events", methods=["GET"])
def get_events():
    since = request.args.get("since")

    query = {}
    if since:
        query = {"timestamp": {"$gt": since}}

    events = list(
        events_collection
        .find(query, {"_id": 0})
        .sort("timestamp", 1)
    )

    return jsonify(events), 200
