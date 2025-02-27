import streamlit as st # type: ignore

# Title of the app
st.title("Unit Converter 📏⚖️🌡️")

# Sidebar for unit type selection
unit_type = st.sidebar.selectbox("Select Unit Type", ["Length", "Weight", "Temperature" ])

# Function to convert length
def convert_length(value, from_unit, to_unit):
    conversion_factors = {
        "Meters": 1,
        "Kilometers": 0.001,
        "Centimeters": 100,
        "Millimeters": 1000,
        "Feet": 3.28084,
        "Inches": 39.3701,
        "Miles": 0.000621371,
        "Yards": 1.09361,
    }
    # Convert to meters first
    meters = value / conversion_factors[from_unit]
    # Convert to target unit
    result = meters * conversion_factors[to_unit]
    return result

# Function to convert weight
def convert_weight(value, from_unit, to_unit):
    conversion_factors = {
        "Kilograms": 1,
        "Grams": 1000,
        "Milligrams": 1e6,
        "Pounds": 2.20462,
        "Ounces": 35.274,
        "Tons": 0.00110231,
    }
    # Convert to kilograms first
    kilograms = value / conversion_factors[from_unit]
    # Convert to target unit
    result = kilograms * conversion_factors[to_unit]
    return result

# Function to convert temperature
def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "Kelvin":
            return value + 273.15
        else:
            return value
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        else:
            return value
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        else:
            return value
    else:
        return value

# Main conversion logic
if unit_type == "Length":
    st.header("Length Converter 📏")
    length_units = ["Meters", "Kilometers", "Centimeters", "Millimeters", "Feet", "Inches", "Miles", "Yards"]
    from_unit = st.selectbox("From", length_units)
    to_unit = st.selectbox("To", length_units)
    value = st.number_input("Enter value", value=1.0)
    result = convert_length(value, from_unit, to_unit)
    st.success(f"**{value} {from_unit} = {result:.4f} {to_unit}**")

elif unit_type == "Weight":
    st.header("Weight Converter ⚖️")
    weight_units = ["Kilograms", "Grams", "Milligrams", "Pounds", "Ounces", "Tons"]
    from_unit = st.selectbox("From", weight_units)
    to_unit = st.selectbox("To", weight_units)
    value = st.number_input("Enter value", value=1.0)
    result = convert_weight(value, from_unit, to_unit)
    st.success(f"**{value} {from_unit} = {result:.4f} {to_unit}**")

elif unit_type == "Temperature":
    st.header("Temperature Converter 🌡️")
    temp_units = ["Celsius", "Fahrenheit", "Kelvin"]
    from_unit = st.selectbox("From", temp_units)
    to_unit = st.selectbox("To", temp_units)
    value = st.number_input("Enter value", value=0.0)
    result = convert_temperature(value, from_unit, to_unit)
    st.success(f"**{value} {from_unit} = {result:.4f} {to_unit}**")