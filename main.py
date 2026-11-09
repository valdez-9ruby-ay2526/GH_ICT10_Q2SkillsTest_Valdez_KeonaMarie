# Periodic Table Information Finder
from pyscript import document

# Database of non-metal elements
non_metals = {
    "H": {"name": "Hydrogen", "atomic_number": 1, "atomic_mass": "1.008"},
    "HE": {"name": "Helium", "atomic_number": 2, "atomic_mass": "4.0026"},
    "C": {"name": "Carbon", "atomic_number": 6, "atomic_mass": "12.011"},
    "N": {"name": "Nitrogen", "atomic_number": 7, "atomic_mass": "14.007"},
    "O": {"name": "Oxygen", "atomic_number": 8, "atomic_mass": "15.999"},
    "F": {"name": "Fluorine", "atomic_number": 9, "atomic_mass": "18.998"},
    "NE": {"name": "Neon", "atomic_number": 10, "atomic_mass": "20.180"},
    "P": {"name": "Phosphorus", "atomic_number": 15, "atomic_mass": "30.974"},
    "S": {"name": "Sulfur", "atomic_number": 16, "atomic_mass": "32.06"},
    "CL": {"name": "Chlorine", "atomic_number": 17, "atomic_mass": "35.45"},
    "AR": {"name": "Argon", "atomic_number": 18, "atomic_mass": "39.948"},
    "SE": {"name": "Selenium", "atomic_number": 34, "atomic_mass": "78.971"},
    "BR": {"name": "Bromine", "atomic_number": 35, "atomic_mass": "79.904"},
    "KR": {"name": "Krypton", "atomic_number": 36, "atomic_mass": "83.798"},
    "I": {"name": "Iodine", "atomic_number": 53, "atomic_mass": "126.90"},
    "XE": {"name": "Xenon", "atomic_number": 54, "atomic_mass": "131.29"},
    "RN": {"name": "Radon", "atomic_number": 86, "atomic_mass": "222"},
    "TS": {"name": "Tennessine", "atomic_number": 117, "atomic_mass": "294"},
    "OG": {"name": "Oganesson", "atomic_number": 118, "atomic_mass": "294"}
}

def check_element(event):
    symbol_input = document.querySelector("#symbol").value.strip()
    key = symbol_input.upper()
    result_div = document.querySelector("#result")

    if key in non_metals:
        info = non_metals[key]
        formatted_symbol = symbol_input.capitalize()

        result_div.innerHTML = f"""
            <strong>Symbol:</strong> {formatted_symbol}<br>
            <strong>Element:</strong> {info['name']}<br>
            <strong>Atomic Number:</strong> {info['atomic_number']}<br>
            <strong>Atomic Mass:</strong> {info['atomic_mass']}
        """
    else:
        if symbol_input == "":
            result_div.innerHTML = "<span style='color: red;'>Please enter an element symbol.</span>"
        else:
            result_div.innerHTML = f"<span style='color: red;'>Element '{symbol_input}' not found or is not a non-metal element.</span>"