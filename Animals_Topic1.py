import streamlit as st
from PIL import Image
col1, col2 = st.columns(2)
with col1:
    st.page_link("Welcome_page.py", label="Home", icon="🏠")
with col2:
    st.page_link("Content.py", label="Overview", icon="⭐️")
st.snow()
st.subheader(":rainbow[Knowing a few animals]🐙")
st.text("What are some common animals that we see in our life?")
st.divider()
animal = st.radio("Choose an animal to learn about:", ("Dog", "Cat", "Rabbit"))
if animal == "Dog":
    st.subheader("🐕Domestic Dog🐶")
    st.text("Dog breeds can have a lot of varieties in terms of shape, size and color. They have around 42 teeth that make up their strong jaws and  they have a really strong sense of smell and hearing compared to human. However, their defect is that they’re visually really weak. Dogs are domesticated mammals. Dog’s scientific name is Canis lupus familiaris. They are one of the most popular domestic animals in the world. For more information of a specific species of dog, please refer to the additional information part. Domestic dogs are really loyal and protective animals. They can guard homes, hunt, herd, and even help you fish sometimes. Fun fact: Dogs actually evolved from a wolf that is now extinct already.")
    from PIL import Image

    image = Image.open("Cute Dog Picture Topic1.jpg")

    st.image(image, caption='A picture of a cute domestic dog.', use_container_width=True)
    st.divider()
elif animal == "Cat":
    st.subheader("🐱Domestic Cats🐈")
    st.text("Domestic cats (Felis catus) are also really popular for humans because of its ability to kill insects and mouse. Its claws are retractable and they can easily kill small preys such as mice and rats, which is very useful for human. It has a really strong but flexible body and reacts quickly. They also have sharp teeth and impressive night vision and sense of smell. They’re believed to be the only mammal who cannot taste sweetness. Cats have 18 toes and can jump up to 6 times their length, making it easy to approach high places together with their flexibility. There is a special pad in the cat’s vocal cords which allows them to make the folds in their vocal cords vibrate at low frequencies, producing the purr sound that differentiates them from the other roaring animals (lions, tigers, leopards, etc.) in the Felidae family. It is important to know that although dogs adapted and changed a lot after domestication for more than 30,000 years, domestic cats are almost still the same as wild, not domesticated cats.")

    image = Image.open("Cute Cat Picture Topic 1.jpg")

    st.image(image, caption='A picture of a cute domestic cat.', use_container_width=True)
    st.divider()
elif animal == "Rabbit":
    st.subheader("🐰Rabbits🐇")
    st.text("Rabbits are warm blooded mammals. They live in groups and underground to seek for protection. They eat plants (herbivores), and they’re a prey to many predators. Rabbits can live up to 12 years, and they have good eyesight. They’re small, furry and they have long ears, short fluffy tails and strong back legs that allow them to jump, and act as a main source of support for their body. They have sharp front teeth called incisors. ")

    image = Image.open("Cute Rabbit Picture Topic1.jpg")

    st.image(image, caption='A picture of a rabbit wearing some flowers.', use_container_width=True)

st.divider()
st.text("Citations")
st.text("Charlottesville Cat Care Clinic. “Charlottesville Cat Care Clinic.” Charlottesville Cat Care Clinic, 2018, cvillecatcare.com/veterinary-topics/101-amazing-cat-facts-fun-trivia-about-your-feline-friend/. Accessed 12 May 2025.Helgren, J. Anne. “Cat.” Encyclopædia Britannica, 14 Jan. 2019, www.britannica.com/animal/cat. Accessed 12 May 2025.McClure, Diane. “Description and Physical Characteristics of Rabbits - All Other Pets.” Veterinary Manual, 2020, www.msdvetmanual.com/all-other-pets/rabbits/description-and-physical-characteristics-of-rabbits. Accessed 12 May 2025.National Geographic Kids. “Dog Facts for Kids!” National Geographic Kids, 21 Mar. 2022, www.natgeokids.com/uk/discover/animals/general-animals/dog-facts/. Accessed 12 May 2025.“Redirect Notice.” Google.com.hk, 2025, www.google.com.hk/url?sa=i&url=https%3A%2F%2Fwww.pinterest.com%2Fpin%2Fadorable-bunny-with-flowers--6051780742213944%2F&psig=AOvVaw2EW31ygwnoZD5PAvXATKUl&ust=1747098932850000&source=images&cd=vfe&opi=89978449&ved=0CBcQjhxqFwoTCJiih-3gnI0DFQAAAAAdAAAAABAQ. Accessed 12 May 2025.Vanacore, Constance B. “Dog | History, Domestication, Physical Traits, & Breeds.” Encyclopædia Britannica, 24 Jan. 2019, www.britannica.com/animal/dog.Wikipedia Contributors. “Cat.” Wikipedia, Wikimedia Foundation, 19 Mar. 2019, en.wikipedia.org/wiki/Cat. Accessed 12 May 2025.---. “Dog.” Wikipedia, Wikimedia Foundation, 14 Jan. 2019, en.wikipedia.org/wiki/Dog. Accessed 12 May 2025.Wildlife, Louis. “St. Louis Wildlife Project.” St. Louis Wildlife Project, 2025, stlwildlifeproject.org/most-commonly-seen-animals. Accessed 12 May 2025.")
