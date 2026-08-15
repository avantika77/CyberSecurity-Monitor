import pandas as pd


def load_logs():
    """Load security logs."""

    file_path = "data/security_logs.csv"

    logs = pd.read_csv(file_path)

    return logs


def detect_failed_logins(logs, threshold=3):
    """
    Detect IP addresses with multiple failed
    login attempts.
    """

    failed = logs[
        logs["event_type"] == "LOGIN_FAILED"
    ]

    attempts = (
        failed
        .groupby("source_ip")
        .size()
        .reset_index(name="failed_attempts")
    )

    suspicious = attempts[
        attempts["failed_attempts"] >= threshold
    ]

    return suspicious