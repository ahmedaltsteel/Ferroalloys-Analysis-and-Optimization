import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_2 = pd.read_csv('Raw_ZQM_MTC_RESULTS202403.csv')
zqm_limits = pd.read_csv('new_data/ZQM_LIMITS_SMP.csv')

merged_df = pd.merge(df_2, zqm_limits, on='MATKL', how='left')

composition_mapping = {
    "ZCARBON": "Carbon",
    "ZNITRO": "Nitrogen",
    "ZSILICON": "Silicon",
    "ZPHOS": "Phosphorus",
    "ZSULP": "Sulfur",
    "ZCOPP": "Copper",
    "ZCHROM": "Chromium",
    "ZMOLY": "Molybdenum",
    "ZNICK": "Nickel",
    "ZVAND": "Vanadium",
    "ZBORON": "Boron",
    "ZCEQ": "Carbon Equivalent"
}

key_value_pairs = {
    "ZCARBON": ('Z_C_HI', 'Z_C_LOW'),
    "ZNITRO": ('Z_N2_HI', 'Z_N2_LOW'),
    "ZSILICON": ('Z_SI_HI', 'Z_SI_LOW'),
    "ZPHOS": ('Z_PH_HI', 'Z_PH_LOW'),
    "ZSULP": ('Z_S_HI', 'Z_S_LOW'),
    "ZCOPP": ('Z_CU_HI', 'Z_CU_LOW'),
    "ZCHROM": ('Z_CR_HI', 'Z_CR_LOW'),
    "ZMOLY": ('Z_MB_HI', 'Z_MB_LOW'),
    "ZNICK": ('Z_NI_HI', 'Z_NI_LOW'),
    "ZVAND": ('Z_VN_HI', 'Z_VN_LOW'),
    "ZBORON": ('Z_B_HI', 'Z_B_LOW'),
    "ZCEQ": ('Z_CEQ_HI', 'Z_CEQ_LOW'),
}

st.title("Material Analysis Dashboard")
selected_element = st.selectbox('Select an element for analysis', list(composition_mapping.keys()))

def check_ranges_seaborn(df, element):
    high, low = key_value_pairs[element]
    plot_data = df[['MATKL', element, high, low]].copy()
    plot_data.rename(columns={element: 'actual_value', high: 'high_value', low: 'low_value'}, inplace=True)
    plot_data['element'] = element

    plt.figure(figsize=(10, 5))
    sns.scatterplot(data=plot_data, x='MATKL', y='actual_value', label='Actual Value')
    sns.scatterplot(data=plot_data, x='MATKL', y='high_value', label='High Limit')
    sns.scatterplot(data=plot_data, x='MATKL', y='low_value', label='Low Limit')
    plt.title(f'Analysis for {composition_mapping[element]}')
    plt.xlabel('MATKL')
    plt.ylabel('Values')
    plt.xticks(rotation=90)
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
    plt.tight_layout()
    st.pyplot(plt)

if st.button('Analyze'):
    check_ranges_seaborn(merged_df, selected_element)
