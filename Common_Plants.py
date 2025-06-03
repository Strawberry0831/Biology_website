import streamlit as st
import os

st.set_page_config(page_title="Famous Plants Explorer", layout="centered")


col1, col2 = st.columns(2)
with col1:
    st.page_link("Welcome_page.py", label="Home", icon="🏠")
with col2:
    st.page_link("Content.py", label="Overview", icon="⭐️")

st.subheader("🌸Common Plants🍄")
st.write("Discover the most well-known plants around the world!")


plant_data = {
    "Houseplants": {
        "Aloe Vera": {
            "image_path": "DT_Aloe Vera.png",  # Adjust filename if different
            "description": "Aloe vera is a perennial, succulent plant. It stores water in its leaves and is used for minor cuts and burns.",
            "fact": "There are around 250 species of aloe vera, but only 4 are commonly used for health."
        },
        "Snake Plant": {
            "image_path": "DT_Snake Plant.jpg",  # Replace with your actual file name
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
            "fact": "Mint's scientific name is Mentha requienni,a nd was derived from the Greek mythological figure Minthe."
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

#User Selection
category = st.selectbox("Choose a plant category:", list(plant_data.keys()))
plant = st.selectbox("Choose a plant:", list(plant_data[category].keys()))
plant_info = plant_data[category][plant]


image_path = plant_info.get("image_path")
if os.path.exists(image_path):
    st.image(image_path, use_container_width=True)
else:
    st.warning(f"Image not found: {image_path}")

st.markdown("### 📖 Description")
st.write(plant_info["description"])
st.markdown("### 🌟 Fun Fact")
st.write(plant_info["fact"])


st.write("Citations")
st.write("“10 Fascinating Basil Facts You Never Knew.” Sacla’, www.sacla.co.uk/blogs/news/10-fascinating-basil-facts-you-never-knew. Accessed 20 May 2025.Brightspark. “10 Fast Facts about Cherry Blossom Trees.” Www.brightsparktravel.ca, 11 Apr. 2022, www.brightsparktravel.ca/blog/10-fast-facts-about-cherry-blossom-trees. Accessed 20 May 2025.Britannica. “Rice | Description, History, Cultivation, & Uses.” Encyclopædia Britannica, 2019, www.britannica.com/plant/rice.Brown, Blair. “All about Cherry Blossom Trees: Facts and Planting Tips.” BrighterBlooms.com, 9 Mar. 2020, www.brighterblooms.com/pages/all-about-cherry-blossom-trees. Accessed 20 May 2025.“Common Oak Tree | Kew.” Kew.org, Kew, 2020, www.kew.org/plants/oak-tree. Accessed 20 May 2025.“Common Sunflower | Kew.” Www.kew.org, www.kew.org/plants/sunflower. Accessed 20 May 2025.“Did You Know: Aloe Vera.” CCHC Online, 7 Oct. 2019, cchc-online.org/2019/10/07/did-you-know-aloe-vera/. Accessed 20 May 2025.“Mint | Plant.” Encyclopedia Britannica, www.britannica.com/plant/Mentha. Accessed 20 May 2025.Mount Sinai. “Aloe Information | Mount Sinai - New York.” Mount Sinai Health System, www.mountsinai.org/health-library/herb/aloe. Accessed 20 May 2025.“Oak Tree Facts: Lesson for Kids | Study.com.” Study.com, 2025, study.com/academy/lesson/oak-tree-facts-lesson-for-kids.html. Accessed 20 May 2025.Only, By Association. “10 Interesting Facts about Roses.” Sophie Allport, www.sophieallport.com/blogs/lifestyle/10-interesting-facts-about-roses. Accessed 20 May 2025.“Roses - Rosa | Plants | Kew.” Www.kew.org, www.kew.org/plants/roses. Accessed 20 May 2025.Rupp, Jessica. “Fun Facts about Potatoes - Extension Potato, Sugarbeet, and Pulse Pathology | Montana State University.” Www.montana.edu, www.montana.edu/extension/pspp/funspudfacts.html. Accessed 20 May 2025.“Snake Plant | Kew.” Www.kew.org, www.kew.org/plants/snake-plant. Accessed 20 May 2025.“Snake Plant: Everything You Need to Know.” RollingNature, 17 Mar. 2018, www.rollingnature.com/blogs/news/snake-plant-everything-you-need-to-know. Accessed 20 May 2025.“Sweet Basil | San Diego Zoo Animals & Plants.” Animals.sandiegozoo.org, animals.sandiegozoo.org/plants/sweet-basil. Accessed 20 May 2025.“U.S. Rice Facts.” Default, www.usarice.com/thinkrice/discover-us-rice/us-rice-facts. Accessed 20 May 2025.“What You Probably Didn’t Know about Mint.” Fine Dining Lovers, 2024, www.finedininglovers.com/explore/articles/what-you-probably-didnt-know-about-mint. Accessed 20 May 2025.Wikipedia Contributors. “Rice.” Wikipedia, Wikimedia Foundation, 2 Feb. 2019, en.wikipedia.org/wiki/Rice. Accessed 20 May 2025.Study.com, 2022, study.com/academy/lesson/potato-overview-origin-examples.html. Accessed 20 May 2025.")
