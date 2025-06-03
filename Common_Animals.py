import streamlit as st
import os

st.set_page_config(page_title="Common Animals", layout="centered")


col1, col2 = st.columns(2)
with col1:
    st.page_link("Welcome_page.py", label="Home", icon="🏠")
with col2:
    st.page_link("Content.py", label="Overview", icon="⭐️")

st.subheader("🐶Common Animals🦊")
st.write("Discover the most well-known animals around the world!")


animal_data = {
    "Houseplants": {
        "Aloe Vera": {
            "image_path": "DT_Aloe Vera.png",
            "description": "Aloe vera is a perennial, succulent plant. It stores water in its leaves and is used for minor cuts and burns.",
            "fact": "There are around 250 species of aloe vera, but only 4 are commonly used for health."
        },
        "Snake Plant": {
            "image_path": "DT_Snake Plant.jpg",
            "description": "Snake plants have a web-like underground root. It has a unique banded pattern. It flowers only once per year, producing cream-coloured flowers. These flowers may produce small orange fruits..",
            "fact": "Did you know that snake plants can purify air by breathing in the toxin and purifying it through the leaves and produce pure oxygen?"
        },
    },
    "Crops": {
        "Rice": {
            "image_path": "DT_Rice Plant.webp",
            "description": "Rice is an annual grass that grows about 1.2m. The leaves are long and they have hollow stems. Rice is a grain and it is the staple food of over half the world's population.",
            "fact": "Did you know that the least allergenic of all the grains is rice?"
        },
        "Potato": {
            "image_path": "DT_Potato.jpg",
            "description": "Potatoes are a starchy plant of the Solanum tuberosum. Tubers are a type of organ that some plants use to store nutrients. Potatoes are one type of root vegetable. This name refers to any underground part of a plant that is eaten by humans, regardless of whether it actually is a root. ",
            "fact": "Did you know that potatoes were the first vegetable grown in space (1995)? ."
        },
    },
    "Herbs": {
        "Basil": {
            "image_path": "DT_Basil.webp",
            "description": "Basil belongs to the Lamiaceae family of mints and is an annual herbaceous plant.  Its leaves are spherical, slightly cupped, and curve to form a point at the tip of its square stems, which have leaves growing on opposing sides.  Though some types have reddish or purplish leaves, the leaves are typically pale green.",
            "fact": "Did you know that in ancient Greece, basil was fobidden to be harvested with anything other than gold/silver?"
        },
        "Mint": {
            "image_path": "DT_Mint.jpg",
            "description": "Mint is a refreshing herb that has square stems and aromatic leaves that are opposite to each other. They can spread a lot in gardens. Their flowers are often small, with the color pale purple, white, or pink and in clusters.",
            "fact": "Mint's scientific name is Mentha requienni,and was derived from the Greek mythological figure Minthe."
        },
    },
    "Flowers": {
        "Rose": {
            "image_path": "DT_Rose.jpg",
            "description": "Roses are plants with prickly stems and green glossy leaves. The flower can be varied in terms of size and shape, and they have a lot of colors such as the most iconic red, to pink, peach cream, yellow, and orange. A lot of roses are fragrant.",
            "fact": "Did you know that a rose bush can be 5.6m high?"
        },
        "Sunflower": {
            "image_path": "DT_Sunflower.jpg",
            "description": "The typical sunflower grows to a height of around 2 meters and has a green, upright stem coated in coarse hairs.  The large, serrated-edged leaves are placed alternately on the stem.  The common sunflower's 'flower' is actually a pseudanthium, or flowerhead, which is composed of several tiny blooms.",
            "fact": "Sunflowers turn their heads to follow the sun!"
        },
    },
    "Trees": {
        "Oak": {
            "image_path": "DT_Oak Trees.jpg",
            "description": "Oak trees can grow over 20m tall. Their trunks can be really wide with dark brown bark, and can grow over 8 meters wide. Their leaves are dark green and pale green.",
            "fact": "A single oak tree can produce 1000 acorns/year!"
        },
        "Cherry Blossom": {
            "image_path": "DT_Cherry Blossom.jpg",
            "description": "Cherry blossoms trees often grow in different shapes and sizes. Many bloom early in the spring while others bloom later. They have medium pink petals, and they are native to Japan.",
            "fact": "Did you know that Amsterdam has 400 individually named cherry blossom trees?"
        },
    }
}


category = st.selectbox("Choose a plant category:", list(animal_data.keys()))
animal = st.selectbox("Choose a plant:", list(animal_data[category].keys()))
animal_info = animal_data[category][animal]


image_path = animal_info.get("image_path")
if os.path.exists(image_path):
    st.image(image_path, use_container_width=True)
else:
    st.warning(f"Image not found: {image_path}")

st.markdown("### 📖 Description")
st.write(animal_info["description"])
st.markdown("### 🌟 Fun Fact")
st.write(animal_info["fact"])


st.write("Citations")