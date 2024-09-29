import streamlit as st
import pandas as pd
import plotly.express as px

# Add the lab's logo (if available) to the header and center it
logo_url = "https://www.greenanalyticsllc.com/logo.png"  # Replace this URL with the actual logo
st.markdown(
    f"""
    <div style='text-align: center;'>
        <img src='{logo_url}' width='200'>
    </div>
    """, 
    unsafe_allow_html=True
)

# Title and Lab Information
st.title("Certificate of Analysis")
st.subheader("Green Analytics NY, LLC - License # OCMPPCL-00013")
st.write("ISO 17025 Certificate No.: 4356.09")

# Use tabs to organize information for better navigation
tab1, tab2, tab3, tab4, tab5, tab6, tab7, tab8 = st.tabs([
    "Client & Sample Info", "Potency & Cannabinoid Analysis", "Terpene Profile", 
    "Metals and Mycotoxins", "Moisture & Filth", "Residual Solvents", "Microbial Testing", 
    "Pesticide Testing"
])

# Client Information Tab
with tab1:
    st.header("Client & Sample Information")
    st.write("""
    - **Client Name:** CuraLeaf NY
    - **Contact Name:** Phil Donohue
    - **Email:** Philip.Donohue@curaleaf.com
    - **License Number:** MM1001M
    - **Sample Name:** SEE, Nano Bites, (S) Tangerine 20-1 (20 x 5 mg) 100mg
    - **Sample Matrix:** Edible
    - **Sample Sub-Type:** Gummy
    - **Sampling Location:** Ravena, New York
    - **Sampling Date:** 12/07/2023 08:00:00
    - **Sample ID:** 20231207-CRLN-015
    - **Batch Lot ID:** P-AUN052023-952A
    - **Batch Size:** 2250 units
    """)

# Potency and Cannabinoid Analysis Tab
with tab2:
    st.header("Potency and Cannabinoid Analysis")
    potency_data = {
        "Analyte": [
            "CBDV", "CBDA", "CBGA", "CBG", "CBD", "THCV", 
            "CBN", "D9-THC", "D8-THC", "D10-THC-S", "D10-THC-R", 
            "CBC", "THCA"
        ],
        "Percentage (% w/w)": ["< MRL", "< MRL", "< MRL", "< MRL", "< MRL", "< MRL", "< MRL", "0.159", "< MRL", "< MRL", "< MRL", "< MRL", "< MRL"],
        "mg/serving": ["< MRL", "< MRL", "< MRL", "< MRL", "< MRL", "< MRL", "< MRL", "5.072", "< MRL", "< MRL", "< MRL", "< MRL", "< MRL"],
        "MRL (% w/w)": ["0.002"] * 13
    }
    potency_df = pd.DataFrame(potency_data)

    # Interactive Line Chart for Potency Results
    st.write("### Potency Analysis Chart")
    selected_analytes = st.multiselect("Select Analytes to Display", options=potency_df['Analyte'], default=potency_df['Analyte'])
    filtered_potency_df = potency_df[potency_df['Analyte'].isin(selected_analytes)]
    
    fig = px.line(filtered_potency_df, x="Analyte", y="Percentage (% w/w)", title="Potency Analysis", markers=True)
    fig.update_layout(xaxis_title="Analyte", yaxis_title="Percentage (% w/w)")
    st.plotly_chart(fig)

    # Summary of Potency Findings
    st.write("""
    **Summary**:
    - Total THC: 0.159% (5.072 mg/serving)
    - Total CBD: < MRL
    - Total Cannabinoids: 0.159%
    """)

    # Table for Potency Data
    st.write("### Potency Measurement Table")
    st.table(potency_df)

# Terpene Profile Tab
with tab3:
    st.header("Terpene Profile")
    terpene_data = {
        "Terpene": [
            "alpha-Pinene", "Camphene", "beta-Pinene", "beta-Myrcene", 
            "Carene", "alpha-Terpinene", "p-Cymene", "Limonene", "Eucalyptol", 
            "Ocimene", "gamma-Terpinene", "Terpinolene", "Linalool", 
            "Isopulegol", "Geraniol", "Beta-Caryophyllene", "alpha-Humulene", 
            "cis-Nerolidol", "trans-Nerolidol", "Caryophyllene oxide", 
            "Guaiol", "alpha-Bisabolol"
        ],
        "Result (% w/w)": ["< MRL"] * 7 + ["0.07"] + ["< MRL"] * 14,
        "MRL (% w/w)": ["0.01"] * 22
    }
    terpene_df = pd.DataFrame(terpene_data)

    # Interactive Line Chart for Terpene Profile
    st.write("### Terpene Profile Chart")
    selected_terpenes = st.multiselect("Select Terpenes to Display", options=terpene_df['Terpene'], default=terpene_df['Terpene'])
    filtered_terpene_df = terpene_df[terpene_df['Terpene'].isin(selected_terpenes)]
    
    fig4 = px.line(filtered_terpene_df, x="Terpene", y="Result (% w/w)", title="Terpene Profile", markers=True)
    fig4.update_layout(xaxis_title="Terpene", yaxis_title="Percentage (% w/w)")
    st.plotly_chart(fig4)

    # Summary of Terpene Findings
    st.write("""
    **Summary**:
    - Total Terpenes: 0.07% (PASS)
    """)

    # Table for Terpene Data
    st.write("### Terpene Measurement Table")
    st.table(terpene_df)

# Metals and Mycotoxins Tab
with tab4:
    st.header("Metals and Mycotoxins Testing Results")

    # Metals Data
    metals_data = {
        "Metal": ["Antimony", "Arsenic", "Cadmium", "Chromium", "Copper", "Lead", "Mercury", "Nickel"],
        "Result (μg/g)": ["< MRL", "< MRL", "< MRL", "< MRL", "< MRL", "< MRL", "< MRL", "< MRL"],
        "Limit (μg/g)": ["120.0", "1.5", "0.5", "1100.0", "300.0", "0.5", "3.0", "20.0"],
        "MRL (μg/g)": ["1.00", "0.10", "0.10", "8.00", "8.00", "0.20", "0.05", "1.00"]
    }
    metals_df = pd.DataFrame(metals_data)

    # Summary of Metals & Mycotoxins Findings
    st.write("""
    **Summary**:
    - All tested heavy metals were below the minimum reporting limit (PASS).
    """)

    # Table for Metals Data
    st.write("### Metals Measurement Table")
    st.table(metals_df)

    # Mycotoxins Data
    mycotoxins_data = {
        "Analyte": ["Ochratoxin", "Total Aflatoxins"],
        "Result (μg/g)": ["< MRL", "< MRL"],
        "Limit (μg/g)": ["0.02", "0.02"],
        "MRL (μg/g)": ["0.01", "0.01"]
    }
    mycotoxins_df = pd.DataFrame(mycotoxins_data)

    # Table for Mycotoxins Data
    st.write("### Mycotoxins Measurement Table")
    st.table(mycotoxins_df)

# Moisture Content & Filth Testing Tab
with tab5:
    st.header("Moisture Content and Filth Testing")

    # Data for moisture content and filth testing
    moisture_data = {
        "Test": ["Moisture Content", "Water Activity"],
        "Result": ["-", "0.69"],
        "Limit": ["-", "0.85"]
    }
    moisture_df = pd.DataFrame(moisture_data)

    # Summary of Moisture & Filth Findings
    st.write("""
    **Summary**:
    - Water Activity: 0.69 (PASS).
    """)

    # Table for Moisture Data
    st.write("### Moisture Measurement Table")
    st.table(moisture_df)

# Residual Solvents Tab
with tab6:
    st.header("Residual Solvents Testing Results")

    solvents_data = {
        "Solvent": ["1,2-Dichloroethane", "2-Propanol", "Acetone", "Acetonitrile", "Butanes, total", "Benzene", 
                    "Chloroform", "Dichloromethane", "Dimethyl Sulfoxide", "Ethanol", "Ethyl acetate", "Ethyl ether", 
                    "n-Heptane", "Hexanes, total", "Methanol", "Pentanes, total", "Propane", "Toluene", "Trichloroethane", "Xylenes, total"],
        "Result (μg/g)": ["< MRL"] * 20,
        "Limit (μg/g)": ["5", "5000", "5000", "410", "5000", "2", "60", "600", "5000", "5000", "5000", "5000", "5000", "290", "3000", "5000", "5000", "890", "1500", "2170"],
        "MRL (μg/g)": ["0.206", "30.864", "6.173", "2.531", "30.864", "0.041", "0.370", "3.704", "55.556", "30.864", "30.864", "30.864", "30.864", "1.790", "18.519", "30.864", "30.864", "5.494", "55.556", "13.395"]
    }
    solvents_df = pd.DataFrame(solvents_data)

    # Summary of Residual Solvents Findings
    st.write("""
    **Summary**:
    - All tested solvents were below the minimum reporting limit (PASS).
    """)

    # Table for Residual Solvents Data
    st.write("### Residual Solvents Measurement Table")
    st.table(solvents_df)

# Microbial and Pesticides Testing Tab
with tab7:
    st.header("Microbial Testing Results")

    # Microbial Data
    microbial_data = {
        "Analyte": ["Total Aerobic Bacteria", "Total Yeast & Mold", "Salmonella spp", "Shiga toxin-producing E. coli", "Aspergillus (fumigatus, flavus, niger, terreus)"],
        "Result (CFU/g)": ["70", "< MRL", "Absent", "Absent", "Absent"],
        "Limit (CFU/g)": ["10000", "1000", "Absent", "Absent", "Absent"]
    }
    microbial_df = pd.DataFrame(microbial_data)

    # Summary of Microbial Findings
    st.write("""
    **Summary**:
    - Microbial tests for pathogens and aerobic bacteria were within acceptable limits (PASS).
    """)

    # Table for Microbial Data
    st.write("### Microbial Measurement Table")
    st.table(microbial_df)

# Pesticide Testing Tab
with tab8:
    st.header("Pesticide Testing Results")

    # Pesticide Data
    pesticide_data = {
        "Analyte": ["Abamectin", "Acephate", "Acequinocyl", "Acetamiprid", "Aldicarb", "Azadirachtin", "Azoxystrobin", 
                    "Bifenazate", "Bifenthrin", "Boscalid", "Captan", "Carbaryl", "Carbofuran", "Chlorantranilprole", 
                    "Chlordane", "Chlorfenapyr", "Chlormequat chloride", "Chlorpyrifos", "Clofentezine", "Coumaphos", 
                    "Cyfluthrin", "Cypermethrin", "Daminozide", "Diazinon", "Dichlorvos", "Dimethoate", "Dimethomorph", 
                    "Ethoprophos", "Etofenprox", "Etoxazole", "Fenhexamid", "Fenoxycarb", "Fenpyroximate", "Fipronil", 
                    "Flonicamid", "Fludioxonil", "Hexythiazox", "Imazalil", "Imidacloprid", "Indole-3-butyric acid", 
                    "Kresoxim-methyl", "Malathion", "Metalaxyl", "Methiocarb", "Methomyl", "Methyl Parathion", "Mevinphos", 
                    "MGK-264 I/II", "Myclobutanil", "Naled", "Oxamyl", "Paclobutrazol", "Pentachloronitrobenzene", 
                    "Permethrins, total", "Phosmet", "Piperonyl butoxide", "Prallethrin", "Propiconazole", "Propoxur", 
                    "Pyrethrins", "Pyridaben", "Spinetoram, Total", "Spinosad, Total", "Spiromesifen", "Spirotetramat", 
                    "Spiroxamine", "Tebuconazole", "Thiacloprid", "Thiamethoxam", "Trifloxystrobin"],
        "Result (μg/g)": ["< MRL"] * 67,
        "Limit (μg/g)": ["Varied"] * 67,
        "MRL (μg/g)": ["Varied"] * 67
    }
    pesticide_df = pd.DataFrame(pesticide_data)

    # Summary of Pesticide Findings
    st.write("""
    **Summary**:
    - All tested pesticides were below the minimum reporting limit (PASS).
    """)

    # Table for Pesticide Data
    st.write("### Pesticide Measurement Table")
    st.table(pesticide_df)

# Footer
st.write("**Date Reported:** 12/12/2023")
st.write("**Lab:** Green Analytics NY, LLC, Pearl River, NY")
st.markdown("""
    **[View Original Report](https://transparencyprod.blob.core.windows.net/coa/uploads/952_A_8b5bfc2dd5.pdf)**
""")
