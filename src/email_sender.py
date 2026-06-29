from pathlib import Path
import mimetypes
import smtplib
from datetime import datetime

from email.message import EmailMessage

from config import (
    SENDER_EMAIL,
    EMAIL_PASSWORD,
    TO_EMAILS,
    CC_EMAILS,
    BCC_EMAILS,
    SMTP_SERVER,
    SMTP_PORT
)


# ======================================================
# Project Paths
# ======================================================

project_path = Path(__file__).resolve().parent.parent

newsletter_path = project_path / "output" / "weekly_newsletter.html"

images_path = project_path / "images"


# ======================================================
# Send Newsletter
# ======================================================

def send_newsletter(kpis):

    # Read HTML Newsletter
    with open(
        newsletter_path,
        "r",
        encoding="utf-8"
    ) as f:

        html = f.read()

    # Create Email
    msg = EmailMessage()

    week_number = kpis["week_number"]

    report_date = datetime.today().strftime("%d %b %Y")

    msg["Subject"] = (
        f"Weekly Sales Newsletter | "
        f"Week {week_number} | "
        f"{report_date}"
    )

    msg["From"] = SENDER_EMAIL

    msg["To"] = ", ".join(TO_EMAILS)

    if CC_EMAILS:
        msg["Cc"] = ", ".join(CC_EMAILS)

    msg.set_content(
        "Your email client does not support HTML."
    )

    # Add HTML Version
    msg.add_alternative(
        html,
        subtype="html"
    )

    # HTML Part
    html_part = msg.get_payload()[1]

    # Images to Embed
    image_files = [

        "top_sales_rep.png",

        "top_regions.png",

        "top_products.png",

        "deal_status.png",

        "priority_distribution.png",


    ]

    # Attach Images
    for image_name in image_files:

        image_path = images_path / image_name

        with open(image_path, "rb") as img:

            image_data = img.read()

        mime_type, _ = mimetypes.guess_type(image_path)

        if mime_type is None:
            mime_type = "image/png"

        maintype, subtype = mime_type.split("/")

        cid = image_name.replace(".png", "")

        html_part.add_related(
            image_data,
            maintype=maintype,
            subtype=subtype,
            cid=f"<{cid}>"
        )

    # Send Email
    print("Connecting to Gmail...")

    with smtplib.SMTP(
        SMTP_SERVER,
        SMTP_PORT
    ) as server:

        server.starttls()

        server.login(
            SENDER_EMAIL,
            EMAIL_PASSWORD
        )

        all_recipients = (
            TO_EMAILS +
            CC_EMAILS +
            BCC_EMAILS
        )

        server.send_message(
            msg,
            to_addrs=all_recipients
        )

    print("Newsletter email sent successfully!")
