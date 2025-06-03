import streamlit as st

pages = {
    "Basic Information": [
        st.Page("Welcome_page.py", title="Home", icon="🌷"),
        st.Page("Content.py", title="Overview", icon="🎈")
    ],
    "Human": [
        st.Page("Human_Topic1.py", title="Topic 1", icon="🍇"),
        st.Page("Human_Topic2.py", title="Topic 2", icon="🍀"),
        st.Page("Human_Topic3.py", title="Topic 3", icon="⭐️"),
    ],
    "Plant": [
        st.Page("Plants_Topic1.py", title="Topic 1", icon="🌸"),
        st.Page("Plants_Topic2.py", title="Topic 2", icon="🍄"),
        st.Page("Plants_Topic3.py", title="Topic 3", icon="🍁"),
    ],
    "Animals": [
        st.Page("Animals_Topic1.py", title="Topic 1", icon="🐳"),
        st.Page("Animals_Topic2.py",title="Topic 2", icon="🐶"),
        st.Page("Animals_Topic3.py",title="Topic 3", icon="🐙"),
    ],
    "Gallery": [
        st.Page("Common_Plants.py", title="Plants Gallery", icon="🍓"),
        st.Page("Common_Animals.py", title="Animals Gallery", icon="🦋"),
    ],
    "Fun Facts": [
        st.Page("Fun_Facts.py", title="Click Here to Access Fun Facts!!", icon="🧸"),
    ],
    "Additional":[
        st.Page("Poodles.py", title="Poodles", icon="🐩")
    ]


}

pg = st.navigation(pages)

pg.run()