## GitHub Webhook Event Tracker

### Description
Tracks GitHub Push, Pull Request, and Merge events using webhooks.
Stores minimal data in MongoDB and displays activity via a polling UI.

### Tech Stack
- Flask
- MongoDB
- GitHub Webhooks
- HTML + JavaScript

### Repositories
- action-repo: Dummy repo to trigger GitHub events
- webhook-repo: Webhook receiver, DB, and UI

### How to Run
1. Start MongoDB
2. `pip install -r requirements.txt`
3. `python app.py`
4. Open `ui/index.html` in browser
