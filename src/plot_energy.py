from imports_and_setup import *
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd

def plot_xtb_gnf2_energies(dfc, dfs):
    dfcs = pd.DataFrame({'xtb_gnf2':dfc['energy'], 'xtb_gnf2_solvent':dfs['energy']})
    
    fig = make_subplots(rows=1, cols=2,subplot_titles=('xtb_gnf2', 'xtb_gnf2_solvent'))

    fig.add_trace(
        go.Histogram(x=dfcs['xtb_gnf2'], name='xtb_gnf2', marker_color='#FF6692', nbinsx=100),
        1, 1)
    
    fig.add_trace(
        go.Histogram(x=dfcs['xtb_gnf2_solvent'], name='xtb_gnf2_solvent', marker_color='#0D2A63', nbinsx=100),
        1, 2)

    fig.update_layout(xaxis={"title": "energies"}, 
                    yaxis={"title": "count"})

    fig.update_layout(title_text='Energy distribution from XTB GnFF2', showlegend=False)
    fig.update_layout(autosize=False, width=1000, height=600)
    # Overlay both histograms
    fig.update_layout(barmode='overlay')
    # Reduce opacity to see both histograms
    fig.update_traces(opacity=0.85)
    fig.update_layout(title_text="",
        paper_bgcolor='rgba(255,255,255,1)',\
    plot_bgcolor='rgba(255,255,255,1)',\
                title_font_size=30)
    # # Show the figure
    fig.write_image('/terray/data/rdkit_geom/conformer_c_s1.png', scale=20)
    fig.show()
