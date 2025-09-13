import streamlit as st
import pandas as pd
import plotly.express as px

# --- Caching Functions ---
@st.cache_data
def load_data(uploaded_file):
    df = pd.read_csv(uploaded_file, parse_dates=['Ride_Request_Time', 'Pickup_Time', 'Dropoff_Time'])

    # Pre-calculate necessary columns
    df['Route'] = df['Source_Zone'] + " to " + df['Destination_Zone']
    df['Hour_of_Day'] = df['Ride_Request_Time'].dt.hour
    df['Day_of_Week'] = df['Ride_Request_Time'].dt.day_name()
    df['Date'] = df['Ride_Request_Time'].dt.date  # For daily aggregation

    # ✅ Add Ride Duration safely (only if Pickup & Dropoff are valid)
    df['Ride_Duration_Minutes'] = (df['Dropoff_Time'] - df['Pickup_Time']).dt.total_seconds() / 60
    df['Ride_Duration_Minutes'] = df['Ride_Duration_Minutes'].fillna(0)

    return df

@st.cache_data
def get_completed_rides(df):
    return df[df['Ride_Status'] == 'Completed'].copy()  # Use .copy() to avoid SettingWithCopyWarning

# --- Main App ---
st.set_page_config(layout="wide")  # Use wide layout
st.title("NYC Ride-Hailing Analytics Dashboard")

# --- File Upload ---
uploaded_file = st.sidebar.file_uploader("Upload your CSV data", type=["csv"])

if uploaded_file is None:
    st.info("Please upload a CSV file to begin analysis.")
    st.stop()
else:
    df_original = load_data(uploaded_file)
    df = df_original.copy()  # Work with a copy for filtering

# --- Sidebar Filters ---
st.sidebar.header("Filters")
# Date Range Filter
min_date = df['Ride_Request_Time'].min().date()
max_date = df['Ride_Request_Time'].max().date()
start_date = st.sidebar.date_input("Start Date", min_date, min_value=min_date, max_value=max_date)
end_date = st.sidebar.date_input("End Date", max_date, min_value=start_date, max_value=max_date)

# Convert to datetime for comparison
start_datetime = pd.to_datetime(start_date)
end_datetime = pd.to_datetime(end_date) + pd.Timedelta(days=1)  # Include the whole end day

# Apply date filter
df_filtered = df[(df['Ride_Request_Time'] >= start_datetime) & (df['Ride_Request_Time'] < end_datetime)].copy()

if df_filtered.empty:
    st.warning("No data available for the selected filters.")
    st.stop()

# --- Dashboard Tabs/Sections ---
tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📊 Performance Snapshot", "🕒 Temporal Demand", "🗺️ Geospatial Insights",
    "💰 Financial Deep Dive", "⭐ Service Quality", "⚙️ Operational Efficiency"
])

with tab1:  # Performance Snapshot
    st.header("Overall Performance Snapshot")
    df_completed = get_completed_rides(df_filtered)

    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("Total Rides", f"{df_filtered.shape[0]:,}")
    col2.metric("Total Revenue", f"${df_completed['Fare'].sum():,.2f}")
    col3.metric("Average Fare", f"${df_completed['Fare'].mean():.2f}" if not df_completed.empty else "$0.00")
    col4.metric("Avg. Ride Duration", f"{df_filtered['Ride_Duration_Minutes'].mean():.1f} min" if not df_filtered.empty else "0 min")

    total_rides = len(df_filtered)
    cancelled_rides = len(df_filtered[df_filtered['Ride_Status'] != 'Completed'])
    cancellation_rate = (cancelled_rides / total_rides * 100) if total_rides > 0 else 0
    col5.metric("Cancellation Rate", f"{cancellation_rate:.1f}%")

    st.subheader("Ride Volume Over Time")
    rides_over_time = df_filtered.groupby(df_filtered['Date'])['Ride_ID'].count().reset_index()
    fig_rides_trend = px.line(rides_over_time, x='Date', y='Ride_ID', title="Daily Ride Volume")
    fig_rides_trend.update_layout(yaxis_title="Number of Rides")
    st.plotly_chart(fig_rides_trend, use_container_width=True)


with tab2:  # Temporal Demand Patterns
    st.header("Temporal Demand Patterns")

    st.subheader("Rides by Hour of Day")
    rides_by_hour = df_filtered['Hour_of_Day'].value_counts().sort_index().reset_index()
    rides_by_hour.columns = ['Hour_of_Day', 'Number of Rides']
    fig_hourly = px.bar(rides_by_hour, x='Hour_of_Day', y='Number of Rides', title="Rides per Hour")
    st.plotly_chart(fig_hourly, use_container_width=True)

    st.subheader("Rides by Day of Week")
    days_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    rides_by_day = df_filtered['Day_of_Week'].value_counts().reindex(days_order).reset_index()
    rides_by_day.columns = ['Day_of_Week', 'Number of Rides']
    fig_daily = px.bar(rides_by_day, x='Day_of_Week', y='Number of Rides', title="Rides per Day of Week")
    st.plotly_chart(fig_daily, use_container_width=True)


with tab3:  # Geospatial Insights
    st.header("Geospatial Hotspots & Routes")
    TOP_N = 10

    col1, col2 = st.columns(2)
    with col1:
        st.subheader(f"Top {TOP_N} Pickup Zones")
        popular_pickup = df_filtered['Source_Zone'].value_counts().nlargest(TOP_N).reset_index()
        popular_pickup.columns = ['Zone', 'Number of Rides']
        fig_pickup = px.bar(popular_pickup, y='Zone', x='Number of Rides', orientation='h', title="Top Pickup Zones")
        fig_pickup.update_layout(yaxis={'categoryorder': 'total ascending'})
        st.plotly_chart(fig_pickup, use_container_width=True)

    with col2:
        st.subheader(f"Top {TOP_N} Drop-off Zones")
        popular_dropoff = df_filtered['Destination_Zone'].value_counts().nlargest(TOP_N).reset_index()
        popular_dropoff.columns = ['Zone', 'Number of Rides']
        fig_dropoff = px.bar(popular_dropoff, y='Zone', x='Number of Rides', orientation='h', title="Top Dropoff Zones")
        fig_dropoff.update_layout(yaxis={'categoryorder': 'total ascending'})
        st.plotly_chart(fig_dropoff, use_container_width=True)

    st.subheader(f"Top {TOP_N} Routes")
    popular_routes = df_filtered['Route'].value_counts().nlargest(TOP_N).reset_index()
    popular_routes.columns = ['Route', 'Number of Rides']
    fig_routes = px.bar(popular_routes, y='Route', x='Number of Rides', orientation='h', title="Top Routes")
    fig_routes.update_layout(yaxis={'categoryorder': 'total ascending'})
    st.plotly_chart(fig_routes, use_container_width=True)


with tab4:  # Financial Deep Dive
    st.header("Financial Insights")
    df_completed = get_completed_rides(df_filtered)

    if not df_completed.empty:
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("Fare Distribution (Completed Rides)")
            fig_fare_dist = px.histogram(df_completed, x="Fare", nbins=30, title="Distribution of Fares")
            st.plotly_chart(fig_fare_dist, use_container_width=True)
        with col2:
            st.subheader("Distance Distribution (Completed Rides)")
            fig_dist_dist = px.histogram(df_completed, x="Distance_Miles", nbins=30, title="Distribution of Distances")
            st.plotly_chart(fig_dist_dist, use_container_width=True)

        st.subheader("Fare vs. Distance (Completed Rides)")
        fig_fare_vs_dist = px.scatter(
            df_completed, x="Distance_Miles", y="Fare",
            trendline="ols",
            title="Fare vs. Distance with Trendline"
        )
        st.plotly_chart(fig_fare_vs_dist, use_container_width=True)
    else:
        st.info("No completed rides in the selected period for financial analysis.")


with tab5:  # Service Quality
    st.header("Service Quality & Ratings")

    st.subheader("Distribution of Driver Ratings")
    rating_dist = df_filtered['Driver_Rating_by_Customer'].value_counts().sort_index().reset_index()
    rating_dist.columns = ['Rating', 'Count']
    fig_rating_dist = px.bar(rating_dist, x='Rating', y='Count', title="Driver Ratings Distribution")
    st.plotly_chart(fig_rating_dist, use_container_width=True)


with tab6:  # Operational Efficiency
    st.header("Operational Efficiency")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Ride Status Breakdown")
        status_counts = df_filtered['Ride_Status'].value_counts().reset_index()
        status_counts.columns = ['Ride_Status', 'Count']
        fig_status_pie = px.pie(status_counts, names='Ride_Status', values='Count', title="Ride Statuses")
        st.plotly_chart(fig_status_pie, use_container_width=True)

    with col2:
        st.subheader("Cancellation Reasons")
        cancelled_df = df_filtered[df_filtered['Ride_Status'] != 'Completed'].copy()
        if not cancelled_df.empty:
            cancel_reasons = cancelled_df['Cancelled_By'].value_counts(dropna=False).reset_index()
            cancel_reasons.columns = ['Cancelled_By', 'Count']
            cancel_reasons['Cancelled_By'] = cancel_reasons['Cancelled_By'].fillna('Unknown')
            fig_cancel_reasons = px.bar(cancel_reasons, x='Cancelled_By', y='Count', title="Reasons for Cancellation")
            st.plotly_chart(fig_cancel_reasons, use_container_width=True)
        else:
            st.info("No cancelled rides in the selected period.")

    st.subheader("Ride Duration Distribution")
    if not df_filtered.empty:
        fig_duration = px.histogram(df_filtered, x="Ride_Duration_Minutes", nbins=40, title="Distribution of Ride Durations (Minutes)")
        st.plotly_chart(fig_duration, use_container_width=True)
    else:
        st.info("No ride duration data available.")
