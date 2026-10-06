"""
Utility functions for logging, terminal formatting, and report output.
"""
from datetime import datetime, timezone
import json
import os

def get_timestamp() -> str:
    """Returns current ISO formatted timestamp."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%SZ")

def format_status(status: str) -> str:
    """Formats status indicators with clean terminal characters."""
    status_upper = status.upper()
    if status_upper in ("HEALTHY", "PASS"):
        return f"[ PASS ] {status_upper}"
    elif status_upper == "WARNING":
        return f"[ WARN ] {status_upper}"
    else:
        return f"[ FAIL ] {status_upper}"

def save_report(report_data: dict, output_dir: str = "reports") -> str:
    """Saves generated health monitoring report to a JSON file."""
    os.makedirs(output_dir, exist_ok=True)
    filename = f"health_report_{datetime.now(timezone.utc).strftime('%Y%m%d_%H%M%S')}.json"
    filepath = os.path.join(output_dir, filename)
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(report_data, f, indent=2)
    return filepath
