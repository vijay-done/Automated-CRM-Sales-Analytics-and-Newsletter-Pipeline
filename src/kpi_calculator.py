from config import AUTO_DETECT_WEEK, REPORT_WEEK
from datetime import datetime


def calculate_kpis(df):
    """
    Calculate all KPI values from the CRM dataset.
    """

    # --------------------------------------------------
    # Determine report week
    # --------------------------------------------------
    if AUTO_DETECT_WEEK:
        week_number = datetime.today().isocalendar().week
    else:
        week_number = REPORT_WEEK

    # --------------------------------------------------
    # Filter data for the selected week
    # --------------------------------------------------
    weekly_df = df[df["Week_Number"] == week_number].copy()

    # If no data exists for the selected week,
    # use the complete dataset as a fallback.
    if weekly_df.empty:
        weekly_df = df.copy()

    # --------------------------------------------------
    # Total Revenue
    # --------------------------------------------------
    total_revenue = weekly_df["Booking_Value_INR"].sum()
    total_revenue = f"₹{total_revenue/1_000_000:.1f}M"

    # --------------------------------------------------
    # Target Revenue
    # --------------------------------------------------
    total_target = weekly_df["Target_Value_INR"].sum()
    total_target = f"₹{total_target/1_000_000:.1f}M"

    # --------------------------------------------------
    # Win Rate
    # --------------------------------------------------
    closed_deals = (weekly_df["Deal_Status"] == "Closed").sum()
    total_deals = len(weekly_df)

    win_rate = (closed_deals / total_deals) * 100
    win_rate = f"{win_rate:.2f}%"

    # --------------------------------------------------
    # Total Opportunities
    # --------------------------------------------------
    total_opportunities = total_deals

    # --------------------------------------------------
    # Top Region
    # --------------------------------------------------
    top_region = (
        weekly_df.groupby("Region")["Booking_Value_INR"]
        .sum()
        .idxmax()
    )

    # --------------------------------------------------
    # Top Sales Representative
    # --------------------------------------------------
    top_sales_rep = (
        weekly_df.groupby("Sales_Rep")["Booking_Value_INR"]
        .sum()
        .idxmax()
    )

    # --------------------------------------------------
    # Top Product
    # --------------------------------------------------
    top_product = (
        weekly_df.groupby("Product")["Booking_Value_INR"]
        .sum()
        .idxmax()
    )

    # --------------------------------------------------
    # Open Deals
    # --------------------------------------------------
    open_deals = (
        weekly_df["Deal_Status"] == "Open"
    ).sum()

    open_percentage = (
        open_deals / total_deals
    ) * 100

    open_percentage = f"{open_percentage:.1f}%"

    # --------------------------------------------------
    # Weekly Summary
    # --------------------------------------------------
    weekly_summary = (
        f"{top_region} region generated the highest revenue this week. "
        f"{top_sales_rep} was the top sales representative with the highest bookings. "
        f"Overall win rate remained {win_rate}."
    )

    # --------------------------------------------------
    # Return KPIs
    # --------------------------------------------------
    kpis = {

        "week_number": week_number,

        "total_revenue": total_revenue,

        "total_target": total_target,

        "win_rate": win_rate,

        "total_opportunities": total_opportunities,

        "top_region": top_region,

        "top_sales_rep": top_sales_rep,

        "top_product": top_product,

        "open_percentage": open_percentage,

        "weekly_summary": weekly_summary
    }

    return kpis
