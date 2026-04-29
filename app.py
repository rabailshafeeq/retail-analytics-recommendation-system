import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Retail Analytics Portfolio",
    layout="wide"
)

st.title("Retail Analytics & Recommendation System")

# -----------------------------
# DATA LOADING (OPTIMIZED)
# -----------------------------
@st.cache_data
def load_data():
    df = pd.read_excel("uci_online_retail.xlsx", engine="openpyxl")

    df = df.dropna(subset=["CustomerID"])

    df["CustomerID"] = df["CustomerID"].astype(int)
    df["StockCode"] = df["StockCode"].astype(str)

    df["TotalPrice"] = df["Quantity"] * df["UnitPrice"]

    return df

df = load_data()

# -----------------------------
# SIDEBAR FILTER
# -----------------------------
country = st.sidebar.selectbox(
    "Select Country",
    ["All"] + sorted(df["Country"].dropna().unique())
)

if country != "All":
    df = df[df["Country"] == country]

# -----------------------------
# KPI CARDS
# -----------------------------
st.subheader("Business Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Customers", df["CustomerID"].nunique())
col2.metric("Orders", df["InvoiceNo"].nunique())
col3.metric("Revenue", round(df["TotalPrice"].sum(), 2))

st.markdown("---")

# -----------------------------
# MENU
# -----------------------------
menu = st.sidebar.radio(
    "Navigation",
    ["Customer Insights", "Product Analysis", "Recommendation System"]
)

# -----------------------------
# CUSTOMER INSIGHTS
# -----------------------------
if menu == "Customer Insights":

    st.header("Customer Insights")

    top_customers = df.groupby("CustomerID")["InvoiceNo"].count().sort_values(ascending=False).head(10)
    top_countries = df["Country"].value_counts().head(10)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Top Customers")
        st.bar_chart(top_customers)

    with col2:
        st.subheader("Top Countries")
        st.bar_chart(top_countries)

    st.info("Insight: A small group of customers drives most of the orders (Pareto principle).")

# -----------------------------
# PRODUCT ANALYSIS
# -----------------------------
elif menu == "Product Analysis":

    st.header("Product Analysis")

    top_products = df.groupby("Description")["Quantity"].sum().sort_values(ascending=False).head(10)
    revenue_products = df.groupby("Description")["TotalPrice"].sum().sort_values(ascending=False).head(10)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Top Products (Quantity)")
        st.bar_chart(top_products)

    with col2:
        st.subheader("Revenue Drivers")
        st.bar_chart(revenue_products)

    st.info("Insight: Revenue is concentrated in a small number of products.")

# -----------------------------
# RECOMMENDATION SYSTEM (HIGH VALUE VERSION)
# -----------------------------
elif menu == "Recommendation System":

    st.header("Product Recommendation System")

    customer_id = st.number_input(
        "Enter Customer ID",
        value=int(df["CustomerID"].iloc[0])
    )

    st.write(f"Analyzing behavior for Customer: {customer_id}")

    # -----------------------------
    # CREATE CUSTOMER-PRODUCT MATRIX
    # -----------------------------
    customer_product = df.pivot_table(
        index="CustomerID",
        columns="Description",
        values="Quantity",
        aggfunc="sum",
        fill_value=0
    )

    # -----------------------------
    # SIMILARITY MATRIX
    # -----------------------------
    similarity_matrix = cosine_similarity(customer_product)

    similarity_df = pd.DataFrame(
        similarity_matrix,
        index=customer_product.index,
        columns=customer_product.index
    )

    # -----------------------------
    # GET SIMILAR CUSTOMERS
    # -----------------------------
    try:
        similar_customers = similarity_df[customer_id].sort_values(ascending=False)[1:6]

        st.subheader("Customer Similarity Score")

        st.dataframe(similar_customers)

        # -----------------------------
        # GET PRODUCTS FROM SIMILAR CUSTOMERS
        # -----------------------------
        similar_customer_ids = similar_customers.index

        recommended_products = df[df["CustomerID"].isin(similar_customer_ids)]["Description"].value_counts().head(10)

        st.subheader("Recommended Products")

        for product, score in recommended_products.items():
            st.markdown(f"""
            **Product:** {product}  
            **Frequency Score:** {score}
            """)

        st.markdown("---")

        st.subheader("How It Works")

        st.success("""
        This recommendation system uses Collaborative Filtering:

        - Finds customers with similar purchase behavior  
        - Computes cosine similarity between customers  
        - Recommends products frequently bought by similar users  
        - Uses real similarity scoring (not random output)
        """)

    except:
        st.error("Customer ID not found in dataset")