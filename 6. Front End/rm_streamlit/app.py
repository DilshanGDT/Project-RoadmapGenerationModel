import streamlit as st
from pyvis.network import Network
import networkx as nx
import tempfile
import os

# ----------------- Backend Functions -----------------
def generate_roadmap(destination, trip_type, budget):
    return {
        "title": f"{trip_type.capitalize()} Trip to {destination}",
        "days": [
            {"day": 1, "activity": "Arrive and relax"},
            {"day": 2, "activity": f"Explore {destination}'s wild side"},
            {"day": 3, "activity": "Safari Adventure"},
        ]
    }

def generate_graph():
    G = nx.Graph()
    G.add_edges_from([
        ("Start", "National Park"),
        ("National Park", "Safari"),
        ("Safari", "End")
    ])
    net = Network(height="400px", width="100%", bgcolor="#ffffff")
    net.from_nx(G)
    temp_dir = tempfile.mkdtemp()
    html_path = os.path.join(temp_dir, "graph.html")
    net.show(html_path)
    return html_path

# ----------------- Streamlit Frontend -----------------
st.title("🗺️ Travel Roadmap Generator")

# User inputs
destination = st.text_input("Enter Destination", "Sri Lanka")
trip_type = st.selectbox("Select Trip Type", ["wildlife", "nature"])
budget = st.slider("Select Budget ($)", 100, 5000, 1000)

if st.button("Generate Roadmap"):
    # Generate itinerary
    roadmap = generate_roadmap(destination, trip_type, budget)
    st.subheader(roadmap["title"])

    for day in roadmap["days"]:
        st.markdown(f"**Day {day['day']}**: {day['activity']}")

    # Embed Graph
    st.subheader("Visual Roadmap")
    graph_path = generate_graph()
    with open(graph_path, 'r', encoding='utf-8') as f:
        html_code = f.read()
    st.components.v1.html(html_code, height=450)