from pathlib import Path
from datetime import datetime

import matplotlib.pyplot as plt

from config import AUTO_DETECT_WEEK, REPORT_WEEK


# ======================================================
# Project Paths
# ======================================================

project_path = Path(__file__).resolve().parent.parent

images_path = project_path / "images"

images_path.mkdir(exist_ok=True)


# ======================================================
# Helper Function
# ======================================================

def get_weekly_df(df):
    """
    Returns the dataframe for the selected report week.
    """

    if AUTO_DETECT_WEEK:
        week_number = datetime.today().isocalendar().week
    else:
        week_number = REPORT_WEEK

    weekly_df = df[df["Week_Number"] == week_number].copy()

    if weekly_df.empty:
        weekly_df = df.copy()

    return weekly_df, week_number


# ======================================================
# Top Sales Representatives
# ======================================================

def generate_top_sales_rep_chart(df):

    weekly_df, week_number = get_weekly_df(df)

    top5_sales = (
        weekly_df.groupby("Sales_Rep")["Booking_Value_INR"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )

    plt.figure(figsize=(7, 4))

    bars = plt.bar(
        top5_sales.index,
        top5_sales.values / 10000000,
        color="#0071CE"
    )

    plt.title(
        f"Top 5 Sales Representatives (Week {week_number})",
        fontsize=16,
        fontweight="bold"
    )

    plt.xlabel("Sales Representative")

    plt.ylabel("Revenue (Crores ₹)")

    plt.xticks(rotation=30)

    plt.grid(axis="y", linestyle="--", alpha=0.5)

    for bar in bars:

        height = bar.get_height()

        plt.text(
            bar.get_x() + bar.get_width()/2,
            height,
            f"{height:.1f}",
            ha="center",
            va="bottom",
            fontsize=10
        )

    plt.tight_layout()

    plt.savefig(
        images_path / "top_sales_rep.png",
        dpi=200
    )

    plt.close()


# ======================================================
# Top Regions
# ======================================================

def generate_top_regions_chart(df):

    weekly_df, week_number = get_weekly_df(df)

    top5_regions = (
        weekly_df.groupby("Region")["Booking_Value_INR"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )

    plt.figure(figsize=(7, 4))

    bars = plt.bar(
        top5_regions.index,
        top5_regions.values / 10000000,
        color="#0071CE"
    )

    plt.title(
        f"Top 5 Regions (Week {week_number})",
        fontsize=16,
        fontweight="bold"
    )

    plt.xlabel("Region")

    plt.ylabel("Revenue (Crores ₹)")

    plt.grid(axis="y", linestyle="--", alpha=0.5)

    for bar in bars:

        height = bar.get_height()

        plt.text(
            bar.get_x() + bar.get_width()/2,
            height,
            f"{height:.1f}",
            ha="center",
            va="bottom"
        )

    plt.tight_layout()

    plt.savefig(
        images_path / "top_regions.png",
        dpi=200
    )

    plt.close()


# ======================================================
# Top Products
# ======================================================

def generate_top_products_chart(df):

    weekly_df, week_number = get_weekly_df(df)

    top5_products = (
        weekly_df.groupby("Product")["Booking_Value_INR"]
        .sum()
        .sort_values(ascending=False)
        .head(5)
    )

    plt.figure(figsize=(7, 4))

    bars = plt.bar(
        top5_products.index,
        top5_products.values / 10000000,
        color="#0071CE"
    )

    plt.title(
        f"Top 5 Products (Week {week_number})",
        fontsize=16,
        fontweight="bold"
    )

    plt.xlabel("Product")

    plt.ylabel("Revenue (Crores ₹)")

    plt.grid(axis="y", linestyle="--", alpha=0.5)

    plt.xticks(rotation=20)

    for bar in bars:

        height = bar.get_height()

        plt.text(
            bar.get_x() + bar.get_width()/2,
            height,
            f"{height:.1f}",
            ha="center",
            va="bottom"
        )

    plt.tight_layout()

    plt.savefig(
        images_path / "top_products.png",
        dpi=200
    )

    plt.close()

 # ======================================================
# Deal Status Distribution
# ======================================================


def generate_deal_status_chart(df):

    weekly_df, week_number = get_weekly_df(df)

    deal_status = (
        weekly_df["Deal_Status"]
        .value_counts()
    )

    plt.figure(figsize=(5.5, 5.5))

    plt.pie(
        deal_status,
        labels=deal_status.index,
        autopct="%1.1f%%",
        startangle=90,
        explode=[0.05] * len(deal_status),
        colors=["#0071CE", "#FFC220", "#D9E2EC"],
        shadow=True
    )

    plt.title(
        f"Deal Status Distribution (Week {week_number})",
        fontsize=16,
        fontweight="bold"
    )

    plt.savefig(
        images_path / "deal_status.png",
        dpi=200
    )

    plt.close()


# ======================================================
# Priority Distribution
# ======================================================

def generate_priority_distribution_chart(df):

    weekly_df, week_number = get_weekly_df(df)

    priority = (
        weekly_df["Priority"]
        .value_counts()
    )

    plt.figure(figsize=(6.5, 4))

    bars = plt.bar(
        priority.index,
        priority.values,
        color="#FFC220"
    )

    plt.title(
        f"Priority Distribution (Week {week_number})",
        fontsize=16,
        fontweight="bold"
    )

    plt.xlabel("Priority")

    plt.ylabel("Number of Deals")

    plt.grid(axis="y", linestyle="--", alpha=0.4)

    for bar in bars:

        height = bar.get_height()

        plt.text(
            bar.get_x()+bar.get_width()/2,
            height,
            f"{height}",
            ha="center",
            va="bottom"
        )

    plt.tight_layout()

    plt.savefig(
        images_path / "priority_distribution.png",
        dpi=200
    )

    plt.close()



# ======================================================
# Generate All Charts
# ======================================================

def generate_all_charts(df):

    generate_top_sales_rep_chart(df)

    generate_top_regions_chart(df)

    generate_top_products_chart(df)

    generate_deal_status_chart(df)

    generate_priority_distribution_chart(df)

    print("All charts generated successfully!")
