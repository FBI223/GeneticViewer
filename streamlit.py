import streamlit as st
import pandas as pd
from cyvcf2 import VCF
from consts import *

st.title("VCF Viewer + VEP Annotacje")

vcf = VCF(vcf_path)
rows = []
for v in vcf:
    csq = v.INFO.get('CSQ')
    if csq:
        fields = csq.split('|')
        rows.append({
            "CHROM": v.CHROM,
            "POS": v.POS,
            "GENE": fields[3],
            "CONSEQUENCE": fields[1]
        })

df = pd.DataFrame(rows)

gene = st.selectbox("Wybierz gen:", df["GENE"].unique())
subset = df[df["GENE"] == gene]

st.dataframe(subset)
st.bar_chart(subset["CONSEQUENCE"].value_counts())
