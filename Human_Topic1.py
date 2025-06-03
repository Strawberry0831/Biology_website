import streamlit as st
col1, col2 = st.columns(2)
with col1:
    st.page_link("Welcome_page.py", label="Home", icon="🏠")
with col2:
    st.page_link("Content.py", label="Overview", icon="⭐️")

st.subheader("Human Topic 1")
st.write(":rainbow[Why do we need food?]")
st.divider()
st.write("Food is one of the most essential things in our life, and it is one of the requisites for us to live. It gives us energy for exercise, sports, and schoolwork. As young children, it helps us grow tall, and ensures that all our organs are working properly. Food provides nutrients and energy that is necessary for the body to grow and function properly. Without food, we wouldn’t sustain a long period of time. The energy in food is measured in the unit of calories.")
st.divider()
st.write("Food Digestion")
st.write("The definition of digestion is the process of breaking down food into smaller and absorbable molecules, so that the body can use it for energy, growth, and repair. There are both mechanical and chemical digestion. Mechanical digestion can include your teeth splitting food into smaller pieces, and mechanical digestion can be stomach acid chemically breaking down food into small pieces so they can be successfully absorbed by the small intestine.")
st.write("During digestion, large food molecules are broken into smaller molecules, and these molecules eventually make it inside cells. In there, chemical reactions rearrange the molecules’ atoms, which makes them form new molecules. Smaller units of food are transported into the blood stream so they can be used by the body.")
st.divider()
st.write(":orange[3 Main Types of Food]")
if "show_carb" not in st.session_state:
    st.session_state.show_carb = False
if "show_protein" not in st.session_state:
    st.session_state.show_protein = False
if "show_fat" not in st.session_state:
    st.session_state.show_fat = False
    #this defines the state of the text at the start since streamlit reruns everything once something is clicked by default
col1, col2, col3= st.columns(3)
with col1:
    if st.button("Carbohydrates", key="carbs_button"):
        st.session_state.show_carb = not st.session_state.show_carb
    if st.session_state.show_carb:
        st.write("Carbohydrates, which consists of things such as rice, bread, pasta, sugar and sweet potatoes.")
#This changes the code to the opposite of the state the "showxxx" was in, so if you click it once then it shows, and click another time it hides (and so on).
with col2:
    if st.button("Protein", key="protein_button"):
        st.session_state.show_protein = not st.session_state.show_protein
    if st.session_state.show_protein:
        st.write("Proteins, which consists of things such as chicken, beef, eggs, peanuts, and cheese.🥕🌽🍆")

with col3:
    if st.button("Fat", key="dessert_button"):
        st.session_state.show_fat = not st.session_state.show_fat
    if st.session_state.show_fat:
        st.write("Fats, which can be represented by food such as avocado, nuts, butter, olive oil, cheese.🍩🍪🎂")
st.write("Of course, there are many other ways to sort food, such as by how they are processed, such as processed/unprocessed food. By sorting them into the 3 main categories, we are sorting them by macronutrients, which are the big building blocks in terms of food. Each one of them have unique benefits to the body.")

st.divider()
st.write("Citations")
st.write("National Geographic. “Food | National Geographic Society.” Education.nationalgeographic.org, National Geographic, 20 May 2022, education.nationalgeographic.org/resource/food/.SInger, Erica. “Why Do We Need to Eat?” Allied Physicians Group, 11 May 2021, alliedphysiciansgroup.com/patient-resources/patient-education/why-do-we-need-to-eat/.“Peptamen®.” Peptamen®, www.peptamen.com/how-body-uses-food.")
st.write("Credits to chat gpt for writing and modifying some parts, as well as helping me fix some of the code.")