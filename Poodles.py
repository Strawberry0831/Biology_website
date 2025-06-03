import streamlit as st
st.subheader("🐶Information About Poodles 🐩")
st.write("Citation to the information provided on this page:Poodle Dog Breed Information. American Kennel Club, www.akc.org/dog-breeds/poodle-standard/. Accessed 10 Mar. 2025.")
st.divider()
st.write("Poodles come in three size varieties: Standards should be more than 15 inches tall at the shoulder; Miniatures are 15 inches or under; Toys stand no more than 10 inches. All three varieties have the same build and proportions. At dog shows, Poodles are usually seen in the elaborate Continental clip. Most pet owners prefer the simpler Sporting clip, in which the coat is shorn to follow the outline of the squarely built, smoothly muscled body.  Forget any preconceived notions about Poodles you may have: Poodles are eager, athletic, and wickedly smart dogs of remarkable versatility. The Standard, with his greater size and strength, is the best all-around athlete of the family, but all Poodles can be trained with great success.")
st.divider()


st.write("")


left, right = st.columns(2)
with left:
    st.image("poodle.jpg", caption="This is a cute poodle picture found on Pinterest.")
    st.button("Close", type="primary")

with right:
    if st.button("Health info"):
        st.write("Most Poodles live long, happy, healthy lives thanks to the efforts of dedicated, responsible breeders who routinely test all breeding stock. As with all breeds, however, some health issues can occur, including hip dysplasia and several eye disorders. Idiopathic epilepsy, sebaceous adenitis, von Willebrands disease, and immune-mediated disorders are also seen in the breed on occasion. Two orthopedic problems, Legg-Calve-Perthes and luxating patellas, are more likely to occur in Toy and Miniature Poodles than in Standards. The Standard variety are more at risk for gastric dilatation with volvulus (bloat) and sebaceous adenitis.")
    else:
     st.write("More info?")
    if st.button ("Grooming"):
        st.write ("Unless you plan to keep your Poodle clipped in a short trim, you will need to learn how to brush them daily to keep their coat from matting. If you do not brush and comb a full-coated Poodle completely to the skin, the hair will mat near the roots and will have to be shaved off to start all over with new growth. Most pet owners opt to keep the Poodle in a shorter trim. Some owners learn to do this clipping and trimming themselves, while others choose to take their dog to a professional dog groomer every four to six weeks for a bath, grooming, and nail trim. The breed's relatively non-shedding coat makes the breed a good choice for people with allergies.")

    if st.button ("Excercise Requirements"):
        st.write ("Poodles of any size are very active dogs who require good exercise every day to suit their high energy level. Poodles are eager for all kinds of activity, and they enjoy keeping busy. Swimming is great exercise for them, and most Poodles love to get in the water. Bred as hunting dogs, their impulse is to retrieve, so tossing toys, sticks, or balls for them will exercise both their mind and body. They also thrive on going for jogs or long walks with their human.")

    if st.button ("Training Requirements"):
        st.write ("Poodles are extremely intelligent and are easily trained. They are agile and graceful as well as smart, and they enjoy and excel in a variety of canine sports, including agility, obedience, and tracking. They are excellent water-retrievers and also compete in dock diving and retriever hunt tests. Poodles are very people-oriented, and if your training routines are fun and positive, they are quick to please you. Just be sure that you are being consistent with what you ask.")

    if st.button ("Nutrition and Eating Choices"):
        st.write ("No matter which size Poodle has stolen your heart, you will want to feed him or her the best possible dog food. Your vet or breeder can help you decide on the right food for your dogs age, activity level, and size. Some dogs are prone to getting overweight, so watch your dogs calorie consumption and weight level. If you choose to give your dog treats, do so in moderation. Treats can be an important aid in training, but giving too many can cause obesity. Never feed a dog cooked bones or fatty table scraps. Learn about which human foods are safe for dogs, and which are not. Check with your vet if you have any concerns about your dogs weight or diet.")

st.divider()
st.write("On a 1-5 Scale, we rate Poodles' personality traits.")

import pandas as pd


data = {
    "Trait": [
        "Affection with Family",
        "Interaction with Young Children",
        "Friendliness to Other Dogs",
        "Shedding level",
        "Coat Grooming Frequency",
        "Drooling Level",
        "Openness To Strangers",
        "Playfulness",
        "Alertness",
        "Adaptability",
        "Easy to train?",
        "Overall Energy",
        "Barking Level",
        "Mental stimulation Needs"
    ],
    "Explanation": [
        "How affectionate a breed is likely to be with family members, or other people he knows well. Some breeds can be aloof with everyone but their owner, while other breeds treat everyone they know like their best friend.",
        "A breed's level of tolerance and patience with childrens' behavior, and overall family-friendly nature. Dogs should always be supervised around young children, or children of any age who have little exposure to dogs.",
        "How generally friendly a breed is towards other dogs. Dogs should always be supervised for interactions and introductions with other dogs, but some breeds are innately more likely to get along with other dogs, both at home and in public.",
        "How much fur and hair you can expect the breed to leave behind. Breeds with high shedding will need to be brushed more frequently, are more likely to trigger certain types of allergies, and are more likely to require more consistent vacuuming and lint-rolling.",
        "How frequently a breed requires bathing, brushing, trimming, or other kinds of coat maintenance. Consider how much time, patience, and budget you have for this type of care when looking at the grooming effort needed. All breeds require regular nail trimming.",
        "How drool-prone a breed tends to be. If you're a neat freak, dogs that can leave ropes of slobber on your arm or big wet spots on your clothes may not be the right choice for you.",
        "How welcoming a breed is likely to be towards strangers. Some breeds will be reserved or cautious around all strangers, regardless of the location, while other breeds will be happy to meet a new human whenever one is around!",
        "How enthusiastic about play a breed is likely to be, even past the age of puppyhood. Some breeds will continue wanting to play tug-of-war or fetch well into their adult years, while others will be happy to just relax on the couch with you most of the time.",
        "A breed's tendency to alert you that strangers are around. These breeds are more likely to react to any potential threat, whether it's the mailman or a squirrel outside the window. These breeds are likely to warm to strangers who enter the house and are accepted by their family.",
        "How easily a breed handles change. This can include changes in living conditions, noise, weather, daily schedule, and other variations in day-to-day life.",
        "How easy it will be to train your dog, and how willing your dog will be to learn new things. Some breeds just want to make their owner proud, while others prefer to do what they want, when they want to, wherever they want!",
        "The amount of exercise and mental stimulation a breed needs. High energy breeds are ready to go and eager for their next adventure. They'll spend their time running, jumping, and playing throughout the day. Low energy breeds are like couch potatoes - they're happy to simply lay around and snooze.",
        "How often this breed vocalizes, whether it's with barks or howls. While some breeds will bark at every passer-by or bird in the window, others will only bark in particular situations. Some barkless breeds can still be vocal, using other sounds to express themselves.",
        "How much mental stimulation a breed needs to stay happy and healthy. Purpose-bred dogs can have jobs that require decision-making, problem-solving, concentration, or other qualities, and without the brain exercise they need, they'll create their own projects to keep their minds busy -- and they probably won't be the kind of projects you'd like."


    ],
    "Rating (1-5)": [5, 5, 3, 1, 4, 1, 5, 5, 5, 4, 5, 4, 4, 5]
}


df = pd.DataFrame(data)

# Display table in Streamlit
st.table(df)
