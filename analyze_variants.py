from cyvcf2 import VCF
import pandas as pd
import plotly.express as px
from consts import *

vcf = VCF(vcf_path)

rows = []
for v in vcf:
    csq = v.INFO.get('CSQ')
    if csq:
        parts = csq.split('|')
        gene = parts[3]
        consequence = parts[1]
        rows.append({"GENE": gene, "CONSEQUENCE": consequence})

df = pd.DataFrame(rows)
fig = px.bar(df["GENE"].value_counts().head(10).reset_index(), x="index", y="GENE",
             title="TOP 10 genów z mutacjami")
fig.show()
