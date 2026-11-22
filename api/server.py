from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime
from pathlib import Path
import json

FILE = Path(__file__).with_name("tasks.json")

data = json.loads(FILE.read_text()) if FILE.exists() else {
	"points": 0,
	"tasks": {}
}

class API(BaseHTTPRequestHandler):

	def reply(self, body, status=200):
		self.send_response(status)
		self.send_header("Content-Type", "application/json")
		self.end_headers()
		self.wfile.write(json.dumps(body).encode())

	def do_GET(self):
		if self.path == "/tasks":
			self.reply(data)
		else:
			self.reply({"success": False}, 404)

	def do_POST(self):
		body = json.loads(self.rfile.read(
			int(self.headers["Content-Length"])
		))
		tag = body["tag_id"]

		if self.path == "/register":
			if tag in data["tasks"]:
				return self.reply({"error": "Task already exists"}, 409)

			data["tasks"][tag] = {
				"name": body["name"],
				"last_completed": None
			}

		elif self.path == "/complete":
			if tag not in data["tasks"]:
				return self.reply({"error": "Task not found"}, 404)

			data["tasks"][tag]["last_completed"] = (
				datetime.now().isoformat(timespec="seconds")
			)
			data["points"] += 1

		else:
			return self.reply({"success": False}, 404)

		FILE.write_text(json.dumps(data, indent=2))
		self.reply({"success": True})

HTTPServer(("0.0.0.0", 8080), API).serve_forever()