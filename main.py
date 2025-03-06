import streamlit as st

def convert_unit(val , from_unit , to_unit):

    conversions ={
        "meters_kilometers": 0.001,
        "kilometers_meters":1000,
        "grams_kilograms":0.001,
        "kilograms_grams":1000
    }
    key = f"{from_unit}_{to_unit}"

    if key in conversions:
        conversion = conversions[key]
        return val * conversion
    else :
        return "Conversion not Supported 🙁"
    
st.title("Unit Converter 🔄")

val = st.number_input("Enter the value:",min_value=1.0 , step=1.0)
from_unit = st.selectbox("Convert from:",["meters","kilometers","grams","kilograms"])
to_unit = st.selectbox("Convert to:",["meters","kilometers","grams","kilograms"])
if st.button("Convert"):
    result = convert_unit(val , from_unit , to_unit)
    st.write(f"Converted Value: {result}")

    
