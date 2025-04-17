# 🌿 LLM-Powered Web Scraper for Crop/Product Pricing

## 🚀 Features
- Accepts a single URL input from the user
- Scrapes the raw webpage content using Firecrawl
- Extracts structured JSON product data using a Mistral LLM
- Output in a web UI
- Download the output JSON file

---

## 🛠 Tools & APIs Used
- 🔥 **Firecrawl** – For scraping structured/HTML/markdown data from webpages
- 🤖 **Mistral (via Groq)** – For LLM-based extraction using a custom JSON-based prompt
- 🧠 **Langchain** – For LLM workflow
- 🌐 **Streamlit** – For building a front-end UI

---

## 📄 Prompt Used
```text
Extract product pricing data in EXACTLY this JSON format:
[{"product": "Name", "price_per_kg": number}]

RULES:
1. Extract only product names and prices in ₹/kg
2. Skip bundles, subscriptions, delivery info
3. If no products found, return empty array []
4. NEVER add explanations or comments
5. STRICT JSON ONLY
6. The output should NEVER mention Organically Grown
```

---

## 🌐 Product Websites
- [Blue Lettuce](https://www.bluelettuce.in/our-products/)
- [Only Hydroponics](https://onlyhydroponics.in/collections/herbs)
- [Dhakad Hydroponic](https://www.dhakadhydroponic.com/shop/Seeds?cid=3702493)
- [Jags Fresh](https://www.jagsfresh.com/subcategory/vegetables/hydroponics)

---

## 💾 Project Structure
```bash
.
├── app.py               # Main Streamlit app
├── scraper.py           # Firecrawl-based scraping logic
├── llm_parser.py        # LLM parsing logic using Groq
├── requirements.txt     # Python dependencies
└── README.md            
```

---

## 📸 Output Screenshots

### 🥬 Product Extraction Interface
![Product Extraction UI](https://github.com/Suzain1/LLM-Powered-Web-Scraper-for-Crop-and-Product-Pricing/blob/main/Output/output_img_1.png)

### 🧾 JSON Output View
![JSON Output](https://github.com/Suzain1/LLM-Powered-Web-Scraper-for-Crop-and-Product-Pricing/blob/main/Output/output_img_2.png)

---

