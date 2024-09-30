import streamlit as st
import pandas as pd
import plotly.express as px

# Add the Green Analytics logo to the header and center it
logo_url = "https://www.greenanalyticsllc.com/logo.png"
st.markdown(
    f"""
    <div style='text-align: center;'>
        <img src='{logo_url}' width='200'>
    </div>
    """, 
    unsafe_allow_html=True
)

# Title and Client Information
st.title("Green Analytics NY, LLC - Certificate of Analysis")
st.subheader("Full Compliance Test")

# Use tabs to organize information for better navigation
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
    "Client & Sample Info", "Potency & Cannabinoid Analysis", "Terpene Profile", 
    "Metals", "Residual Solvents", "Microbial Testing", 
    "Pesticides", "Mycotoxins"
])

# Client Information Tab
with tab1:
    st.header("Client Information")
    st.write("""
    - **Client Name:** CuraLeaf NY
    - **Sample Name:** SEE, Nano Bites, (S) Tangerine 20-1 (20 x 5 mg) 100mg
    - **Sampling Location:** Ravena, New York
    - **Contact Name:** Phil Donohue
    - **Contact Email:** Philip.Donohue@curaleaf.com
    - **Sample Subtype:** Gummy
    - **License Number:** MM1001M
    - **Package ID:** 20461
    - **Medical/Adult Use:** Medical
    - **Batch Lot ID:** P-AUN052023-952A
    - **Sampling Date:** 12/07/2023
    - **Batch Size:** 2250
    - **Serving Size (g):** 3.2
    """)

# Potency and Cannabinoid Analysis Tab
with tab2:
    st.header("Potency and Cannabinoid Analysis")
    potency_data = {
        "Analyte": ["CBDV", "CBDA", "CBGA", "CBG", "CBD", "THCV", "CBN", "D9-THC", "D8-THC", "D10-THC-S", "D10-THC-R", "CBC", "THCA"],
        "Percentage (% w/w)": ["< MRL", "< MRL", "< MRL", "< MRL", "< MRL", "< MRL", "< MRL", "0.159", "< MRL", "< MRL", "< MRL", "< MRL", "< MRL"],
        "mg/serving": ["< MRL", "< MRL", "< MRL", "< MRL", "< MRL", "< MRL", "< MRL", "5.072", "< MRL", "< MRL", "< MRL", "< MRL", "< MRL"]
    }
    potency_df = pd.DataFrame(potency_data)

    # Interactive Line Chart for Potency Results
    st.write("### Potency Analysis Chart")
    fig = px.line(potency_df, x="Analyte", y="Percentage (% w/w)", title="Potency Analysis", markers=True)
    st.plotly_chart(fig)

    # Table for Potency Data
    st.write("### Potency Measurement Table")
    st.table(potency_df)

    # Summary
    st.write("""
    **Summary**:
    - The total THC is 0.159% (5.072 mg/serving), and no significant levels of CBD or other cannabinoids were detected.
    """)

# Terpene Profile Tab
with tab3:
    st.header("Terpene Profile")
    terpene_data = {
        "Analyte": ["alpha-Pinene", "Camphene", "beta-Pinene", "beta-Myrcene", "Carene", "alpha-Terpinene", "p-Cymene", "Limonene", "Eucalyptol"],
        "Result (% w/w)": ["< MRL", "< MRL", "< MRL", "< MRL", "< MRL", "< MRL", "< MRL", "0.07", "< MRL"]
    }
    terpene_df = pd.DataFrame(terpene_data)

    # Interactive Line Chart for Terpenes
    st.write("### Terpene Profile Chart")
    fig4 = px.line(terpene_df, x="Analyte", y="Result (% w/w)", title="Terpene Profile", markers=True)
    st.plotly_chart(fig4)

    # Table for Terpene Data
    st.write("### Terpene Measurement Table")
    st.table(terpene_df)

    # Summary
    st.write("""
    **Summary**:
    - The only terpene detected was Limonene at 0.07% (w/w), which contributes to a citrus aroma and potential mood-enhancing effects.
    """)

# Metals Tab
with tab4:
    st.header("Metals Testing Results")

    # Metals Data
    metals_data = {
        "Metal": ["Antimony", "Arsenic", "Cadmium", "Chromium", "Copper", "Lead", "Mercury", "Nickel"],
        "Result (ug/g)": ["< MRL", "< MRL", "< MRL", "< MRL", "< MRL", "< MRL", "< MRL", "< MRL"],
        "Limit (ug/g)": [120.0, 1.5, 0.5, 1100.0, 300.0, 0.5, 3.0, 20.0]
    }
    metals_df = pd.DataFrame(metals_data)

    # Interactive Line Chart for Metals Data
    st.write("### Metals Testing Results Chart")
    fig2 = px.line(metals_df, x="Metal", y="Result (ug/g)", title="Metals Testing Results", markers=True)
    st.plotly_chart(fig2)

    # Table for Metals Data
    st.write("### Metals Measurement Table")
    st.table(metals_df)

    # Summary
    st.write("""
    **Summary**:
    - All heavy metals, including lead and mercury, were detected below the minimum reporting limit (MRL) and passed within safe limits.
    """)

# Residual Solvents Tab
with tab5:
    st.header("Residual Solvents Testing Results")

    solvents_data = {
        "Solvent": ["1,2-Dichloroethane", "2-Propanol", "Acetone", "Acetonitrile", "Butanes, total", "Benzene", "Chloroform"],
        "Result (ug/g)": ["< MRL", "< MRL", "< MRL", "< MRL", "< MRL", "< MRL", "< MRL"],
        "Limit (ug/g)": [5, 5000, 5000, 410, 5000, 2, 60]
    }
    solvents_df = pd.DataFrame(solvents_data)

    # Residual Solvents Chart
    st.write("### Residual Solvents Testing Results Chart")
    fig6 = px.line(solvents_df, x="Solvent", y="Result (ug/g)", title="Residual Solvents Testing Results", markers=True)
    st.plotly_chart(fig6)

    # Table for Residual Solvent Data
    st.write("### Residual Solvents Measurement Table")
    st.table(solvents_df)

    # Summary
    st.write("""
    **Summary**:
    - All tested solvents were detected below the MRL, indicating that no harmful residual solvents were found in the product.
    """)

# Microbial Testing Tab
with tab6:
    st.header("Microbial Testing Results")

    microbial_data = {
        "Analyte": ["Total Aerobic Bacteria", "Total Yeast & Mold", "Salmonella spp", "STEC", "Aspergillus"],
        "Result (CFU/g)": ["70", "< MRL", "Absent", "Absent", "Absent"],
        "Limit (CFU/g)": ["10000", "1000", "Absent", "Absent", "Absent"]
    }
    microbial_df = pd.DataFrame(microbial_data)

    # Microbial Testing Chart
    st.write("### Microbial Testing Results Chart")
    fig7 = px.line(microbial_df, x="Analyte", y="Result (CFU/g)", title="Microbial Testing Results", markers=True)
    st.plotly_chart(fig7)

    # Table for Microbial Data
    st.write("### Microbial Measurement Table")
    st.table(microbial_df)

    # Summary
    st.write("""
    **Summary**:
    - The microbial screen passed for all tests, with no harmful microorganisms like Salmonella or E. coli detected.
    """)

# Pesticides Tab
with tab7:
    st.header("Pesticides Testing Results")

    pesticides_data = {
        "Analyte": ["Abamectin", "Acephate", "Acetamiprid", "Azadirachtin", "Azoxystrobin"],
        "Result (ug/g)": ["< MRL", "< MRL", "< MRL", "< MRL", "< MRL"],
                "Limit (ug/g)": [0.50, 0.40, 0.20, 1.00, 0.20]
    }
    pesticides_df = pd.DataFrame(pesticides_data)

    # Pesticides Testing Chart
    st.write("### Pesticides Testing Results Chart")
    fig8 = px.line(pesticides_df, x="Analyte", y="Result (ug/g)", title="Pesticides Testing Results", markers=True)
    st.plotly_chart(fig8)

    # Table for Pesticides Data
    st.write("### Pesticides Measurement Table")
    st.table(pesticides_df)

    # Summary
    st.write("""
    **Summary**:
    - The pesticides screen passed, with no harmful pesticides detected above the minimum reporting limits (MRL).
    """)

# Mycotoxins Tab
with tab8:
    st.header("Mycotoxins Testing Results")

    mycotoxins_data = {
        "Analyte": ["Ochratoxin", "Total Aflatoxins"],
        "Result (ug/g)": ["< MRL", "< MRL"],
        "Limit (ug/g)": [0.02, 0.02]
    }
    mycotoxins_df = pd.DataFrame(mycotoxins_data)

    # Mycotoxins Testing Chart
    st.write("### Mycotoxins Testing Results Chart")
    fig9 = px.line(mycotoxins_df, x="Analyte", y="Result (ug/g)", title="Mycotoxins Testing Results", markers=True)
    st.plotly_chart(fig9)

    # Table for Mycotoxins Data
    st.write("### Mycotoxins Measurement Table")
    st.table(mycotoxins_df)

    # Summary
    st.write("""
    **Summary**:
    - The mycotoxins test passed, with no detectable levels of harmful mycotoxins like ochratoxin or aflatoxins.
    """)

# Footer with a link to the original report
st.write("**Analysis Date:** 12/12/2023")
st.write("**Lab:** Green Analytics NY, LLC, Pearl River, NY")

# Link to the original report
st.markdown("""
    **[View Original Report](https://www.greenanalyticsllc.com/reports/20231207-CRLN-015.pdf)**
""")
