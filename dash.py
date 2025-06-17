import dash
from dash import dcc, html
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

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("VCF Annotacja – Dashboard"),
    dcc.Graph(
        figure=px.histogram(df, x="CONSEQUENCE", title="Typy konsekwencji mutacji")
    ),
    dcc.Graph(
        figure=px.bar(df["GENE"].value_counts().head(10).reset_index(),
                      x="index", y="GENE", title="Top 10 genów")
    )
])

if __name__ == "__main__":
    app.run_server(debug=True)
