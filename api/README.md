# Chorewand API

## Endpoints
| Method | Endpoint | Description |
|---|---|---|
| GET | `/tasks` | Retrieve all tasks and statistics |
| POST | `/register` | Associate an NFC tag with a task |
| POST | `/complete` | Record task completion and award a point |


## Server Management
To start the python server:
```
python3 app/server.py
```

## Register a task
```curl localhost:8080/register -d '{"tag_id":"123","name":"Make the bed"}'```

**Expected output:** 
```{"success": true}```

## Complete a task
```curl localhost:8080/complete -d '{"tag_id":"123"}'```

**Expected output:**
```{"success": true}```

## Query Stats
```curl localhost:8080/tasks```

**Expected output:** 
```
{
  "points": 1,
  "tasks": {
    "123": {
      "name": "Make the bed",
      "last_completed": "2026-11-21T20:47:00"
    }
  }
}
```