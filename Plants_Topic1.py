import streamlit as st
import time


col1, col2 = st.columns(2)
with col1:
    st.page_link("Welcome_page.py", label="Home", icon="🏠")
with col2:
    st.page_link("Content.py", label="Overview", icon="⭐️")


st.subheader(":green[Different Kinds of Plants]")
st.write(":rainbow[What are some basic kinds of plants that we encounter a lot in our lives?]")
st.divider()
st.write(":rainbow[Mosses]🌿")
st.write("Mosses are non-vascular plants, meaning they lack specialized tissues (xylem and phloem) for water and nutrient transport. Instead, they absorb water directly through their leaves and rely on diffusion for internal transport. This limitation confines them to moist environments and restricts their size .")
st.write("They reproduce via spores and exhibit an alternation of generations, with the gametophyte (haploid) stage being dominant. Fertilization requires water for the motile sperm to reach the egg.")

st.divider()
st.write(":rainbow[Ferns]🌱")
st.write("Ferns are vascular plants possessing true roots, stems, and leaves (fronds). They have specialized tissues (xylem and phloem) for efficient water and nutrient transport, allowing them to grow larger than bryophytes .")
st.write(" Ferns reproduce via spores and also exhibit an alternation of generations, but with the sporophyte (diploid) stage being dominant. The gametophyte is a small, independent organism known as a prothallus .")
st.divider()

st.write(":rainbow[Flowering Plants]🌸")
st.write("Flowering plants, or angiosperms, are the most diverse group of plants on Earth, encompassing over 330,000 species, including roses, apple trees, sunflowers, and corn. They are characterized by their ability to produce flowers, which serve as reproductive structures. Within the flower, male parts produce pollen, while female parts contain ovules. After pollination, typically facilitated by wind or animals, the ovule develops into a seed enclosed within a fruit. This enclosed seed structure distinguishes angiosperms from other plant groups. Their adaptability allows them to thrive in various environments, making them integral to ecosystems and human agriculture.")
st.divider()

st.write(":rainbow[Conifers]🌲")
st.write("Conifers are a prominent group within gymnosperms, which are seed-producing plants that do not form flowers. Instead, they reproduce using cones; male cones release pollen, and female cones house ovules. After fertilization, seeds develop on the surface of the scales of female cones, hence the term 'naked seeds.' Conifers, such as pine and fir trees, typically have needle-like leaves and are well-adapted to colder climates. They play a significant role in forest ecosystems, especially in the Northern Hemisphere.")
st.divider()

st.write(":rainbow[Succulents]🌵")
st.write("Succulents are plants adapted to arid environments by developing thick, fleshy tissues that store water. This adaptation allows them to survive in regions with limited rainfall. Some succulents, like cacti, store water primarily in their stems and may have reduced or no leaves to minimize water loss. Others, such as agaves, store water mainly in their leaves. These plants often have extensive root systems to absorb moisture efficiently. Their unique appearance and low maintenance requirements make them popular as ornamental plants.")
st.divider()

st.write(":rainbow[Grasses]🌾")
st.write("Grasses belong to the Poaceae family, a group of monocotyledonous flowering plants that includes wheat, corn, rice, and bamboo. They are characterized by hollow stems, narrow leaves with parallel veins, and small flowers typically arranged in clusters called spikelets. Grasses are incredibly versatile, growing in diverse habitats across all continents except Antarctica. They are of immense economic importance, providing staple foods for humans and forage for animals. Their ability to grow rapidly and adapt to various environments makes them a dominant component of many ecosystems.")


st.title("🌱 Plant Identification Quiz")
st.write("Test your knowledge about different plant groups!")

# Define quiz Q&A to be used in options and answers part.
quiz_data = [
    {
        "question": "Which plant group stores water in its leaves or stems?",
        "options": ["Conifers", "Succulents", "Grasses", "Flowering plants"],
        "answer": "Succulents"
    },
    {
        "question": "Which plant group reproduces using cones instead of flowers?",
        "options": ["Grasses", "Flowering plants", "Conifers", "Succulents"],
        "answer": "Conifers"
    },
    {
        "question": "Which plant group has the most species on Earth?",
        "options": ["Conifers", "Succulents", "Grasses", "Flowering plants"],
        "answer": "Flowering plants"
    },
    {
        "question": "Which plant group includes wheat, corn, and rice?",
        "options": ["Succulents", "Conifers", "Grasses", "Flowering plants"],
        "answer": "Grasses"
    },
    {
        "question": "Which plant group often has needle-like leaves?",
        "options": ["Flowering plants", "Conifers", "Grasses", "Succulents"],
        "answer": "Conifers"
    },
    {
        "question": "Which plant group produces seeds enclosed in fruits?",
        "options": ["Succulents", "Grasses", "Conifers", "Flowering plants"],
        "answer": "Flowering plants"
    },
    {
        "question": "Which plant group is most commonly used in landscaping for dry climates?",
        "options": ["Grasses", "Succulents", "Conifers", "Flowering plants"],
        "answer": "Succulents"
    },
    {
        "question": "Which group has plants with hollow stems and small clustered flowers?",
        "options": ["Succulents", "Grasses", "Conifers", "Flowering plants"],
        "answer": "Grasses"
    },
]

# Initial score/index (question that I'm on)
if "score" not in st.session_state:
    st.session_state.score = 0
if "q_index" not in st.session_state:
    st.session_state.q_index = 0
if "quiz_done" not in st.session_state:
    st.session_state.quiz_done = False

# The Actual Quiz
if not st.session_state.quiz_done:
    current_q = quiz_data[st.session_state.q_index]
    st.write(f"Question {st.session_state.q_index + 1}:")
    user_answer = st.radio(current_q["question"], current_q["options"], key=f"q{st.session_state.q_index}")
#Creates the subheader like question 1...
#Checks the Answer after user clicks the submit answer part. If it matches the answer of the current question stored in the quiz data part, it shows a green text and adds score, otherwise shows a red text and shows the correct answer from the quiz data part.
    if st.button("Submit Answer"):
        if user_answer == current_q["answer"]:
            st.success("Correct!")
            st.session_state.score += 1
        else:
            st.error(f"Incorrect. The correct answer is {current_q['answer']}.")

        time.sleep(3)

        st.session_state.q_index += 1
        #Checks after the submission which question I'm on, and calculates the length of the quiz data and see if it's already the end of the quiz.
        if st.session_state.q_index >= len(quiz_data):
            st.session_state.quiz_done = True

        #Refreshes the whole page and saves the score and quiz index part.
        st.rerun()
else:
    #The end of the quiz part, shows score in terms of the length of the quiz (#/8).
    st.success(f"You finished the quiz! Your score: {st.session_state.score} / {len(quiz_data)}")
    #Restart the quiz button, resets all values and reruns the code.
    if st.button("Restart Quiz"):
        st.session_state.q_index = 0
        st.session_state.score = 0
        st.session_state.quiz_done = False
        st.rerun()

st.write("Sources")
st.write("“6.2: Pteridophyta - the Ferns.” Biology LibreTexts, 3 Jan. 2019, bio.libretexts.org/Bookshelves/Botany/Introduction_to_Botany_%28Shipunov%29/06%3A_Growing_Diversity_of_Plants/6.02%3A_Pteridophyta_-_the_Ferns?utm_source=chatgpt.com. Accessed 6 May 2025.Mickel, John T, and Ernest M Gifford. “Fern.” Encyclopædia Britannica, 14 Feb. 2019, www.britannica.com/plant/fern.“Moss: Characteristics, Life Cycle and Uses.” BYJUS, byjus.com/biology/moss-characteristics-life-cycle-and-uses/. Accessed 6 May 2025.Petruzzello, Melissa. “Succulent | Plant | Britannica.” Encyclopædia Britannica, 2019, www.britannica.com/plant/succulent. Accessed 6 May 2025.“Plant Types / RHS Gardening.” Www.rhs.org.uk, www.rhs.org.uk/plants/types.Wikipedia Contributors. “Flowering Plant.” Wikipedia, Wikimedia Foundation, 16 Apr. 2019, en.wikipedia.org/wiki/Flowering_plant.---. “Poaceae.” Wikipedia, Wikimedia Foundation, 19 Mar. 2019, en.wikipedia.org/wiki/Poaceae. Accessed 6 May 2025.---. “Succulent Plant.” Wikipedia, Wikimedia Foundation, 19 Dec. 2019, en.wikipedia.org/wiki/Succulent_plant. Accessed 6 May 2025.")
st.write("Credit to Chat GPT for generating some useful websites and texts, and also for walking through the quiz code creation with me.")
