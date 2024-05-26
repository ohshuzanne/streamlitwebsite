import streamlit as st

#set up the page's configurations like sidebars and stuff
#emoji website is on webfx emoji cheat sheets or sumn like that
#default layout is centered, but wide makes it take up the whole screen width
st.set_page_config(page_title="Shu's Website", page_icon = ":cookie:", layout="wide", )

#header
with st.container():
    st.subheader("My name is Shu :baby_chick:")
    st.title("Badminton fan first, AI engineer second")
    st.write("I'm currently a second-year student finding the joy in using Python (the only language I'm good at) (jk) to optimize every aspect of my life")
    st.write("[Learn More >](https://www.linkedin.com/in/suzanne-lai-tzi-syuen-034103254/)")