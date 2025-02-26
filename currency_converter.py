import streamlit as st
import requests

# API Details
API_KEY = "O3hFRjmEp59WLQT-9XhO"  # Replace with your actual API key
BASE_URL = "https://marketdata.tradermade.com/api/v1/convert"

# Function to fetch supported currencies
def fetch_supported_currencies():
    url = f"https://marketdata.tradermade.com/api/v1/live_currencies_list?api_key={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return list(data.get("available_currencies", {}).keys())
    else:
        st.error(f"Error {response.status_code}: {response.text}")
        return None

# Function to convert currency
def convert_currency(amount, from_currency, to_currency):
    url = f"{BASE_URL}?api_key={API_KEY}&from={from_currency}&to={to_currency}&amount={amount}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data["quote"], data["total"]
    return None, None

# Streamlit App
def currency_converter():
    st.title("K6 DevOps Group: Currency Converter Project")

    st.image("C:/Users/ACTNET SYSTEM/Desktop/K6Group_logo-01.jpeg", width=200)

    amount = st.number_input("ENTER AMOUNT:", value=500, step=1)

    supported_currencies = fetch_supported_currencies()

    if supported_currencies:
        from_currency = st.selectbox("FROM CURRENCY:", supported_currencies, index=44)
        to_currencies = st.multiselect("TO CURRENCIES:", supported_currencies, default=["GBP"])

        if st.button("CONVERT"):
            st.write("CONVERSION RESULTS:")
            for to_currency in to_currencies:
                try:
                    rate, converted_amount = convert_currency(amount, from_currency, to_currency)
                    if rate:
                        st.write(f"{amount} {from_currency} = {converted_amount} {to_currency} (1 {from_currency} = {rate} {to_currency})")
                    else:
                        st.write(f"Exchange rate not available for {from_currency} to {to_currency}.")
                except Exception as e:
                    st.error(f"Error: {e}")

# Run the app
if __name__ == "__main__":
    currency_converter()
