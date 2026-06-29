from data_loader import load_data
from kpi_calculator import calculate_kpis
from chart_generator import generate_all_charts
from render_newsletter import render_newsletter
from email_sender import send_newsletter

# Load CRM Data
df = load_data()

# Calculate KPIs
kpis = calculate_kpis(df)

# Generate Charts
generate_all_charts(df)

# Render HTML Newsletter
render_newsletter(kpis)

# Send Newsletter Email
send_newsletter(kpis)

print("Automation completed successfully!")
