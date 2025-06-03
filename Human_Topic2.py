import streamlit as st
from PIL import Image
col1, col2 = st.columns(2)
with col1:
    st.page_link("Welcome_page.py", label="Home", icon="🏠")
with col2:
    st.page_link("Content.py", label="Overview", icon="⭐️")

st.subheader("Healthy Habits")
st.write(":blue[What are some habits that we need to maintain?]")
st.divider()
st.write("Healthy habits are everyday behaviors that positively impact you on several aspects, such as physical, emotional and mental wellbeing. These habits can help you prevent diseases in the long term, and maintain a high quality of life. These habits change your life bit by bit, so it’s not about instant results. It is something you need to stick on to a while in order for it’s benefits to completely show-consistency is vital here. Over time, these habits will become a part of your life and you will be improving and maintaining your health unconsciously through these habits!")
st.write("Sleeping is one of the most important healthy habits! There are too many benefits about sleeping. A good sleep keeps you in a better mood, sharpens your memory and focus, and helps you learn new things. In the long term, a good sleep lowers the risk of gaining unhealthy weight and lowers the risk of heart diseases. It repairs cells and makes the mind lively again after a long, exhausting day. People with different ages have different recommended sleep length, and you should sleep accordingly in order to reach optimal benefits of sleep. Sleeping schedule is also important-you would want to set a specific time period of when to sleep, and stick to that even on weekends. ")
image = Image.open("Sleep_Recommendation.png")
st.image(image, caption="Above is a sleep schedule recommended by experts for people in different age groups, and the optimal amount of sleep they should get each night. Feel free to see if any of the categories matches you, and try sleeping in that way tonight! Hopefully, you will wake up refreshed and rejuvenated. However, it is important to note that different people might vary a bit on the optimal sleeping length, so it is important that you keep adjusting it until you find your own sleep length.", use_container_width=True)
st.write("Exercising is also important! Regular physical activity is very important to improve brain healthy, manage weight, reduce risk of disease, and make your bone and muscles stronger according to the Center for Disease Control and Prevention. Exercising also makes your mood better. Understanding how hard it may be to fit big amounts of exercise in your schedule every day and persevere, you can start with simply taking a walk each day. It’s a simple and effective habit that also counts as exercising.")
st.write("Eating healthy can also impact our body with numerous benefits. As mentioned in the topic before this, eating provides direct impact on the body since the body get energy and nutrients from food. A balanced diet will get you all the vitamins and nutrients your body needs in order to stay strong. Adding plant-based foods (fruits and vegetables) is a really good option because they provide nutrients as well as maintaining blood pressure levels, reducing the risk of long-term diseases. It is always important to try to not eat or at least control your consumption of processed foods, alcohol, sugar and caffeine (especially at a young age, you shouldn’t be touching alcohol!!).")
st.write("Taking small breaks is also important as it lets you be aware of yourself, help remove your mental fatigue and make your focus better. After a period of work, regularly have breaks and leave the work desk to look outside the window, breath deeply, stretch and move around to prevent sedentariness.")
st.write("Stay hydrated! Hydration supports digestion, improves your brain performance, and increases your energy, not mentioning that it is an indispensable factor for you to even live. ")
st.divider()


st.write("Let's check how many healthy habits you are currently maintaining!🌿")
healthy_habits = [
    "Exercise regularly (at least 3 times a week)",
    "Eat a balanced diet with fruits and vegetables",
    "Get 7–9 hours of sleep each night",
    "Stay hydrated throughout the day",
    "Manage stress through relaxation or mindfulness",
    "Avoid smoking and limit alcohol intake",
    "Maintain a regular sleep schedule",
    "Take regular breaks from screens",
    "Stay socially connected with friends/family",
    "Go for regular health checkups",
    "Practice good posture",
    "Limit processed food and sugar intake",
    "Get sunlight or Vitamin D daily",
    "Read or engage your brain in learning",
    "Practice gratitude or journaling",
    "Avoid late-night snacking",
    "Wash your hands frequently",
    "Spend time in nature regularly",
    "Limit caffeine intake",
    "Avoid multitasking—focus on one task at a time"
]

selected_habits = st.multiselect("✅ Which of these habits do you already practice?", healthy_habits)

#Counts how many are selected using len(), and stores the number in the 2 variables.
if selected_habits:
    num_selected = len(selected_habits)
    total_habits = len(healthy_habits)

    st.write(f"You selected {num_selected} out of {total_habits} healthy habits.")

    if num_selected >= total_habits / 2:
        st.success("🎉 You're doing a great job! Keep up those good habits!")
    else:
        st.warning("💪 You're on the right path, but there can definitely be room for improvement! Keep working!")
st.divider()
st.write("Citations")
st.write("Mosunic, Chris. “13 Healthy Habits to Start Daily for a Healthier Lifestyle.” Calm Blog, 6 Sept. 2023, www.calm.com/blog/healthy-habits.“Redirect Notice.” Google.com, 2025, www.google.com/url?sa=i&url=https%3A%2F%2Fwww.sleepfoundation.org%2Fhow-sleep-works%2Fhow-much-sleep-do-we-really-need&psig=AOvVaw2kUJRS9MyhbQGRtB9j6LVV&ust=1746060913794000&source=images&cd=vfe&opi=89978449&ved=0CBcQjhxqFwoTCNDiuvfF_owDFQAAAAAdAAAAABAE. Accessed 30 Apr. 2025.WebMD. “12 Habits of Super-Healthy People.” WebMD, 2019, www.webmd.com/fitness-exercise/ss/twelve-habits-super-healthy-people.")
st.divider()