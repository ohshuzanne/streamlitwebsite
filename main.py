import streamlit as st
from streamlit_lottie import st_lottie
import requests
from PIL import Image
from streamlit_extras.let_it_rain import rain

#set up the page's configurations like sidebars and stuff
#emoji website is on webfx emoji cheat sheets or sumn like that
#default layout is centered, but wide makes it take up the whole screen width
st.set_page_config(page_title="Shu's Website", page_icon = ":cookie:", layout="wide",)

#default
soc_med_links= {
    "LinkedIn": "https://www.linkedin.com/in/suzanne-lai-tzi-syuen-034103254/",
    "GitHub": "https://github.com/ohshuzanne",
}

#functions
def lottie_loader(url):
    getReq = requests.get(url)
    if getReq.status_code != 200:
        return None
    return getReq.json()

def run_snow_animation():
    rain(emoji="❄️", font_size=20, falling_speed=5, animation_length="infinite")

#css styling
def my_css(file):
    with open(file) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html= True)

my_css("style/style.css")


#assets
lottie_polyfox = "https://lottie.host/f8f6abbe-7797-48cb-9d72-e3f006de0987/kzrdAgrilI.json"
img_savvy = Image.open("image_assets/1.png")
img_kitajom = Image.open("image_assets/KitaJombanner.png")

run_snow_animation()


#header
with st.container():
    st.subheader("My name is Shu :baby_chick:")
    st.markdown('<h1 class="gradient-title">Badminton fan first, AI engineer second</h1>', unsafe_allow_html=True)
    st.write("I'm currently a second-year student finding the joy in using Python (the only language I'm good at) (jk) to optimize every aspect of my life")
    socmed_html = '<div class="socmed-links">' + ' '.join([f'<a href="{link}">{platform}</a>' for platform, link in soc_med_links.items()]) + '</div>'
    st.markdown(socmed_html, unsafe_allow_html=True)


#about me
with st.container():
    st.write("---")
    left_section, right_section = st.columns(2, gap="medium")
    with left_section:
        st.header("About me")
        st.write("""
                 
                 Here's a summary of what I do:
                 - I play Valorant. A lot of it
                 - Making technology accessible is incredibly important to me
                 - Bionics engineering is a deeply rooted passion of mine
                 - I'm proficient in Python, Java, and Dart
                 
                 """)
    with right_section:
        st_lottie(lottie_polyfox, height = 250, key="polyfox")

#projects
with st.container():
    st.write("---")
    st.header("My Projects")
    image_section, text_section = st.columns((1,2), gap="large")
    with image_section:
        st.image(img_savvy)

    with text_section:
        st.subheader("Savvy: A debt management application")
        st.write("""
                 - First place in Varsity Hackathon 2024
                 - Gamifies debt repayment and financial education
                 - Motivates users through virtual "Savvy Pets"
                 - Integrates Gemini for in-app chat feature, AI categorization and summarization
                 - FlutterFire and Gemini
                 """)
        st.markdown("[Click me!](https://github.com/ohshuzanne/savvy)")
with st.container():
    image_section, text_section = st.columns((1,2), gap="large")
    with image_section:
        st.image(img_kitajom)

    with text_section:
        st.subheader("KitaJom: A sustainable travelling app for vendors")
        st.write("""
                 - Individual university assignment (4.0)
                 - Sustainable travelling application for vendors to manage their listings, bookings, user reviews and so on
                 - Created to promote responsible travel practices within the country
                 - FlutterFire

                 """)
        st.markdown("[Click me!](https://github.com/ohshuzanne/kitajom_vendor)")

#contact me

with st.container():
    st.write("---")
    st.header("Get in touch!")

    contact_form = """
    <form action="https://formsubmit.co/suzannelts02@gmail.com" method="POST">
    <input type ="hidden" name="_captcha" value='false'>
        <input type="text" name="name" placeholder = "Your name" required>
        <input type="email" name="email" placeholder = "Your e-mail" required>
        <textarea name="message" placeholder = "Enter your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """

    left_section, right_section = st.columns(2)
    with left_section:
        st.markdown(contact_form, unsafe_allow_html= True)
    with right_section:
        st.empty()