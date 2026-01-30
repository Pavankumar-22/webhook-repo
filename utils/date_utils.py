from datetime import datetime

def format_utc_timestamp(iso_ts: str) -> str:
    dt = datetime.fromisoformat(iso_ts.replace("Z", "+00:00"))

    day = dt.day
    suffix = "th" if 11 <= day <= 13 else {1:"st",2:"nd",3:"rd"}.get(day % 10, "th")

    return dt.strftime(f"{day}{suffix} %B %Y - %I:%M %p UTC")
