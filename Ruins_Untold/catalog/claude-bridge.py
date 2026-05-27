#!/usr/bin/env python3
"""
claude-bridge.py

Tiny HTTP server that exposes the local Claude CLI to Docker-based n8n.
Runs on the host machine. Docker containers reach it via:
  http://host.docker.internal:3333/generate

Usage:
  python3 claude-bridge.py

Keep this running in a terminal tab whenever you use the n8n catalog workflow.
"""

import json
import subprocess
import sys
from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = 3333


class ClaudeHandler(BaseHTTPRequestHandler):

    def do_POST(self):
        if self.path != "/generate":
            self.send_error(404, "Only POST /generate is supported")
            return

        try:
            length = int(self.headers.get("Content-Length", 0))
            body = json.loads(self.rfile.read(length))
            prompt = body.get("prompt", "").strip()

            if not prompt:
                self.send_error(400, "Missing 'prompt' in request body")
                return

            print(f"[bridge] Running claude -p (prompt length: {len(prompt)} chars)")

            result = subprocess.run(
                ["claude", "-p", prompt],
                capture_output=True,
                text=True,
                timeout=180,  # 3-minute ceiling — idea gen can take a moment
            )

            if result.returncode != 0:
                print(f"[bridge] Claude exited {result.returncode}: {result.stderr[:200]}")

            response_body = json.dumps({
                "output":   result.stdout,
                "exitCode": result.returncode,
                "error":    result.stderr if result.returncode != 0 else "",
            })

            status = 200 if result.returncode == 0 else 500
            self.send_response(status)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(response_body.encode())

        except subprocess.TimeoutExpired:
            print("[bridge] ERROR: Claude timed out after 180s")
            self.send_error(504, "Claude timed out")
        except json.JSONDecodeError:
            self.send_error(400, "Invalid JSON body")
        except FileNotFoundError:
            print("[bridge] ERROR: 'claude' not found in PATH")
            self.send_error(500, "claude binary not found — check PATH")
        except Exception as exc:
            print(f"[bridge] ERROR: {exc}")
            self.send_error(500, str(exc))

    def log_message(self, fmt, *args):
        # Clean single-line log instead of n8n's default verbose format
        print(f"[bridge] {self.address_string()}  {fmt % args}")


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", PORT), ClaudeHandler)
    print(f"[bridge] Claude bridge running on port {PORT}")
    print(f"[bridge] n8n endpoint → http://host.docker.internal:{PORT}/generate")
    print(f"[bridge] Press Ctrl+C to stop\n")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n[bridge] Stopped.")
        sys.exit(0)
