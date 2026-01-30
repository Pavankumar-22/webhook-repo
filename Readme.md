## GitHub Webhook Event Tracker

### Overview
This project implements a GitHub webhook receiver using Flask that listens to repository
events, stores only the required event data in MongoDB, and displays the latest activity
through a minimal polling-based UI.

The solution focuses on clean data extraction, correct event handling, and a simple,
readable architecture as per the assessment requirements.

---

### Features
- Receives GitHub webhook events for:
  - Push
  - Pull Request
  - Merge (bonus)
- Extracts and stores only minimal required data
- Prevents duplicate event entries
- Formats timestamps in human-readable UTC format
- UI polls backend every 15 seconds and displays latest events
- Clean separation of routes, services, and utilities

---

### Event Display Format
<pre>
**Push**
{author} pushed to {to_branch} on {timestamp}


**Pull Request**
{author} submitted a pull request from {from_branch} to {to_branch} on {timestamp}

**Merge**
{author} merged branch {from_branch} to {to_branch} on {timestamp}
</pre>

---

### Tech Stack
- Python
- Flask
- MongoDB
- GitHub Webhooks
- HTML + JavaScript

---

### Repositories
- **action-repo**  
  Dummy GitHub repository used to trigger push, pull request, and merge events.

- **webhook-repo**  
  Flask application that receives webhook events, stores data in MongoDB,
  and serves the polling UI.

---

### Project Structure

---

### Tech Stack
- Python
- Flask
- MongoDB
- GitHub Webhooks
- HTML + JavaScript

---

### Repositories
- **action-repo**  
  Dummy GitHub repository used to trigger push, pull request, and merge events.

- **webhook-repo**  
  Flask application that receives webhook events, stores data in MongoDB,
  and serves the polling UI.

---

### Project Structure
<pre>
  webhook-repo/
  │
  ├── app.py
  ├── requirements.txt
  │
  ├── db/
  │ └── mongo.py
  │
  ├── models/
  │ └── event_model.py
  │
  ├── routes/
  │ ├── webhook.py
  │ └── events.py
  │
  ├── services/
  │ └── event_service.py
  │
  ├── utils/
  │ └── date_utils.py
  │
  ├── ui/
  │ └── index.html
  │
  └── README.md
</pre>



---

### Application Flow

<pre>
  action-repo (GitHub Event)
          ↓
  Flask Webhook Receiver
          ↓
  MongoDB
          ↓
  Polling UI (every 15 seconds)
</pre>



---

### How to Run Locally

1. Start MongoDB
2. Create and activate a virtual environment
3. Install dependencies:

      pip install -r requirements.txt

4. Run the Flask application:
   
      python app.py

6. Open the UI:
   
      ui/index.html


---

### Notes
- The Flask development server is used for local execution.
- Webhook endpoint is configurable via GitHub settings.
- UI automatically updates without manual refresh.
- Demo walkthrough video is provided separately as part of submission.

---

### Author
Pavan Kumar
