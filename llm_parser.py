from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import json
import logging
import re


def extract_products_with_llm(content, groq_api_key):
    """
    Robust product extraction with fixed prompt template
    """
    if not content.strip():
        return []

    try:
        llm = ChatGroq(
            groq_api_key="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",
            model_name="mistral-saba-24b",
            temperature=0.3
        )

        # Fixed prompt template - properly escaped variables
        prompt_template = ChatPromptTemplate.from_messages([
            ("system", """
            Extract product pricing data in EXACTLY this JSON format:
            [{{"product": "Name", "price_per_kg": number}}]

            RULES:
            1. Extract only product names and prices in ₹/kg
            2. Skip bundles, subscriptions, delivery info
            3. If no products found, return empty array []
            4. NEVER add explanations or comments
            5. STRICT JSON ONLY
            6. The output should NEVER mention Organically Grown
            """),
            ("human", "Extract from this content:\n{content}")
        ])

        chain = prompt_template | llm
        response = chain.invoke({"content": content})

        # Multiple JSON parsing attempts
        raw_response = response.content
        json_str = None

        # Try extracting JSON from markdown code block first
        code_block_match = re.search(r'```(?:json)?\n([\s\S]*?)\n```', raw_response)
        if code_block_match:
            json_str = code_block_match.group(1)
        else:
            # Fallback to extracting the first JSON array found
            array_match = re.search(r'\[[\s\S]*\]', raw_response)
            if array_match:
                json_str = array_match.group(0)
            else:
                json_str = raw_response

        if json_str:
            try:
                products = json.loads(json_str)
                if isinstance(products, list):
                    return products
            except json.JSONDecodeError as e:
                logging.error(f"JSON decode failed: {str(e)}\nContent: {json_str}")

        logging.error(f"No valid JSON found in response: {raw_response}")
        return []

    except Exception as e:
        logging.error(f"LLM processing failed: {str(e)}")
        return []