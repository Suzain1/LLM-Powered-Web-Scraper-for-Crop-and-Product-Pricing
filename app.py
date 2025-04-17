import streamlit as st
from scraper import scrape_with_firecrawl
from llm_parser import extract_products_with_llm
import time

# Configure Streamlit page
st.set_page_config(
    page_title="Crop and Product Price Scraper",
    page_icon="🌱",
    layout="centered"
)

# Custom CSS styling
st.markdown("""
    <style>
        .stTextInput input {
            height: 3rem;
            font-size: 1rem;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            height: 3rem;
            width: 100%;
            font-size: 1rem;
        }
        .product-card {
            border: 1px solid #ddd;
            border-radius: 8px;
            padding: 15px;
            margin: 10px 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .product-name {
            font-weight: bold;
            font-size: 1.2rem;
            color: #2e7d32;
        }
        .product-price {
            color: #d32f2f;
            font-size: 1.1rem;
        }
    </style>
""", unsafe_allow_html=True)

# App title and description
st.title("🌱Crop and Product Price Scraper")
st.markdown("""
Extract structured product pricing data from hydroponic farming websites.
Enter a URL from the approved list below to get clean product data.
""")

groq_key = "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"
# Sidebar for Groq API key
with st.sidebar:

    st.markdown("Approved Websites")
    st.markdown("""
    - [Blue Lettuce](https://www.bluelettuce.in/our-products/)
    - [Only Hydroponics](https://onlyhydroponics.in/collections/herbs)
    - [Dhakad Hydroponic](https://www.dhakadhydroponic.com/shop/Seeds?cid=3702493)
    - [Jags Fresh](https://www.jagsfresh.com/subcategory/vegetables/hydroponics)
    """)


# Main content area
url = st.text_input(
    "Enter URL from approved list:",
    placeholder="https://www.bluelettuce.in/our-products/",
    help="Only works with approved hydroponic product websites"
)

if st.button("Extract Product Data"):
    if not url:
        st.warning("Please enter a URL")
        st.stop()

    if not groq_key:
        st.error("Please provide your Groq API key")
        st.stop()

    # Initialize progress bar
    progress_bar = st.progress(0)
    status_text = st.empty()

    try:
        # Step 1: Scrape the URL
        status_text.text("Scraping website content...")
        progress_bar.progress(25)

        scraped_content = scrape_with_firecrawl(url)

        # Step 2: Parse with LLM
        status_text.text("Extracting product data with AI...")
        progress_bar.progress(60)

        products = extract_products_with_llm(scraped_content, groq_key)

        # Step 3: Display results
        status_text.text("Formatting results...")
        progress_bar.progress(90)

        if not products:
            st.warning("No products found or unable to extract data from this page.")
        else:
            st.success(f"Found {len(products)} products!")
            st.markdown("### Extracted Product Data")

            # Display products in cards

            # Show raw JSON
            with st.expander("View raw JSON data"):
                st.json(products)

        progress_bar.progress(100)
        status_text.text("Done!")
        time.sleep(1)
        status_text.empty()
        progress_bar.empty()

    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        progress_bar.empty()
        status_text.empty()
