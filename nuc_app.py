import streamlit as st
from pyvis.network import Network
import networkx as nx

#Page title
st.set_page_config(page_title="Energy Knowledge Graph", layout="wide")
# 3 tabs creation
tab1, tab2, tab3 = st.tabs(["Renewable Energy", "Nuclear Energy", "Deforestation"])

#Info for tab 1 (you can place your node network here)
with tab1:
    st.header("Renewable Energy")
    st.write("Placeholder for Renewable Energy knowledge graph.")

# Info for tab 2 (all nuclear information goes in here)
with tab2:
    st.header("Nuclear Energy")

    # Building the network graph
    visual = nx.Graph()

    # This is how the edges connect to all the nodes
    edges = [
        ("Nuclear Energy", "Nuclear Fission"),
        ("Nuclear Fission", "Uranium-235"),
        ("Nuclear Fission", "Plutonium-239"),
        ("Nuclear Fission", "Nuclear Reactor"),
        ("Nuclear Fission", "PUREX"),
        ("Nuclear Fission", "Heat (Steam)"),
        ("Heat (Steam)", "Turbines"),
        ("Turbines", "Electricity"),
        ("Nuclear Reactor", "Pressurized water"),
        ("Nuclear Reactor", "Boiling water"),
        ("Nuclear Reactor", "Fast breeder"),
        ("Nuclear Reactor", "Small modular"),
        ("Plutonium-239", "Neptunium (Np-239)"),
        ("Neptunium (Np-239)", "U-239"),
        ("U-239", "U-238"),
        ("Uranium-235", "U-238"),
        ("U-238", "Mining"),
        ("Mining", "Open-pit"),
        ("Mining", "Underground"),
        ("Mining", "In-situ leaching (ISL)"),
        ("U-238", "Yellowcake (U308)"),
        ("Yellowcake (U308)", "UO₂ > UF₄ > UF₆"),
        ("UO₂ > UF₄ > UF₆", "Enrichment"),
        ("Enrichment", "Gas centrifuge"),
        ("Enrichment", "Gaseous diffusion"),
        ("Enrichment", "Laser enrichment"),
    ]
    # Adding the edge connections to the graph
    visual.add_edges_from(edges)

    # Graph customizable features (I played around with this for a little while)
    nuclear_net = Network(height="750px", width="100%", bgcolor="#111", font_color="white")

    nuclear_net.set_options("""
    {
      "nodes": {
        "shape": "dot",
        "size": 50,
        "font": {
          "size": 20,
          "face": "arial",
          "color": "white"
        }
      },
      "edges": {
        "length": 150,
        "color": {
          "color": "#888"
        }
      },
      "physics": {
    "enabled": false
  }
    }
    """)
    # Adding custom features to the graph
    nuclear_net.from_nx(visual)

    # I made the main node here red for easier viewing
    nuclear_net.get_node("Nuclear Energy")["color"] = "red"

    # Made other nodes grey to stick closer to my diagram (just personal preference)
    for node in visual.nodes:
        if node != "Nuclear Energy":
            nuclear_net.get_node(node)["color"] = "#888"

    # Render and display visual
    nuclear_net.save_graph("nuclear_graph.html")

    with open("nuclear_graph.html", "r", encoding="utf-8") as f:
        html_string = f.read()
        st.components.v1.html(html_string, height=800, scrolling=True)
        
# Third tab information goes in here
with tab3:
    st.header("Deforestation")
    st.write("Placeholder for Deforestation knowledge graph.")
