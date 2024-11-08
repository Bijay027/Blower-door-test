# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 12:37:28 2024

@author: bsharma
"""

import streamlit as st

def main():
    st.title("Flow Rate and Methane Leakage Calculator")
    st.write("Calculate CFM, methane leakage, and Delta CH₄ (I-O) for various ACH levels.")

    # Input parameters
    floor_area = st.number_input("House floor area (sqft)", min_value=0.0, format="%f")
    ceiling_height = st.number_input("Ceiling height (ft)", min_value=0.0, format="%f")
    ach_low = st.number_input("House ACH (low) [per hour]", min_value=0.25, format="%f")
    ach_medium = st.number_input("House ACH (medium) [per hour]", min_value=0.30, format="%f")
    ach_high = st.number_input("House ACH (high) [per hour]", min_value=0.50, format="%f")
    outdoor_ch4 = st.number_input("Outdoor CH₄ (ppm)", min_value=0.0, format="%f")
    indoor_ch4 = st.number_input("Indoor CH₄ (ppm)", min_value=0.0, format="%f")
    target_ach = st.number_input("Target ACH [per hour]", min_value=0.0, format="%f")

    # Step 1: Calculate Volume (cuft)
    volume = floor_area * ceiling_height
    st.write(f"**Volume (cuft)**: {volume:.2f}")

    # Step 2: Calculate House CFM for low, medium, and high
    house_cfm_low = (volume * ach_low) / 60
    house_cfm_medium = (volume * ach_medium) / 60
    house_cfm_high = (volume * ach_high) / 60
    st.write(f"**House CFM (low)**: {house_cfm_low:.2f}")
    st.write(f"**House CFM (medium)**: {house_cfm_medium:.2f}")
    st.write(f"**House CFM (high)**: {house_cfm_high:.2f}")

    # Step 3: Calculate Delta CH₄ (ppm)
    delta_ch4 = indoor_ch4 - outdoor_ch4
    st.write(f"**Delta CH₄ (ppm)**: {delta_ch4:.2f}")

    # Step 4: Calculate CH₄ Leakage for low, medium, and high
    ch4_leakage_low = (delta_ch4 * house_cfm_low * 40776.259094 * 0.657) / (1000000)
    ch4_leakage_medium = (delta_ch4 * house_cfm_medium * 40776.259094 * 0.657) / (1000000)
    ch4_leakage_high = (delta_ch4 * house_cfm_high * 40776.259094 * 0.657) / (1000000)
    st.write(f"**CH₄ Leakage (low) (g/day)**: {ch4_leakage_low:.6f}")
    st.write(f"**CH₄ Leakage (medium) (g/day)**: {ch4_leakage_medium:.6f}")
    st.write(f"**CH₄ Leakage (high) (g/day)**: {ch4_leakage_high:.6f}")

    # Step 5: Calculate Target CFM
    target_cfm = (volume * target_ach) / 60
    st.write(f"**Target CFM**: {target_cfm:.2f}")

    # Step 6: Calculate Delta CH₄ (I-O) for low, medium, and high
    delta_ch4_io_low = (delta_ch4 * house_cfm_low * 1000) / target_cfm if target_cfm != 0 else 0
    delta_ch4_io_medium = (delta_ch4 * house_cfm_medium * 1000) / target_cfm if target_cfm != 0 else 0
    delta_ch4_io_high = (delta_ch4 * house_cfm_high * 1000) / target_cfm if target_cfm != 0 else 0

    # Display results
    st.subheader("Results")
    st.write(f"**Target CFM**: {target_cfm:.2f}")
    st.write(f"**Delta CH₄ (I-O) (low) (ppb)**: {delta_ch4_io_low:.6f}")
    st.write(f"**Delta CH₄ (I-O) (medium) (ppb)**: {delta_ch4_io_medium:.6f}")
    st.write(f"**Delta CH₄ (I-O) (high) (ppb)**: {delta_ch4_io_high:.6f}")

if __name__ == "__main__":
    main()
