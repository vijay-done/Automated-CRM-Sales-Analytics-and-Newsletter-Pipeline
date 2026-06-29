from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()


"""
Application Configuration
"""

# ======================================================
# Development Mode
# ======================================================

AUTO_DETECT_WEEK = True

# Used only when AUTO_DETECT_WEEK = False
REPORT_WEEK = 26

# ======================================================
# Email Configuration
# ======================================================

SENDER_EMAIL = os.getenv("SENDER_EMAIL")

EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

SMTP_SERVER = "smtp.gmail.com"

SMTP_PORT = 587

# ======================================================
# Email Recipients
# ======================================================

TO_EMAILS = [
    "vijaydone93@gmail.com",
    "joginprashant@gmail.com"
]

CC_EMAILS = [
    "priyankadone35@gmail.com"
]

BCC_EMAILS = [
]
