import pandas as pd
from cyvcf2 import VCF
import plotly.express as px

vcf = VCF("annotated.vcf")

data = []
for v in vcf:
    csq = v.INFO.get('CSQ')
    if csq:
        fields = csq.split('|')
        gene = fields[3]
        consequence = fields[1]
        data.append({"GENE": gene, "CONSEQUENCE": consequence})

df = pd.DataFrame(data)
top_genes = df["GENE"].value_counts().head(10).reset_index()
top_genes.columns = ["GENE", "COUNT"]

fig = px.bar(top_genes, x="GENE", y="COUNT", title="TOP 10 genów z mutacjami")
fig.show()
