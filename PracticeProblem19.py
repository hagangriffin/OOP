import streamlit as st
from PIL import Image
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

def email():
    msg = MIMEMultipart()
    msg['Subject'] = 'Test'
    msg['From'] = em
    msg['To'] = 'haganzgriffin@gmail.com'
    msg.preamble = 'Test'

    s = smtplib.SMTP('localhost')
    s.sendmail(em, 'haganzgriffin@gmail.com', msg.as_string())
    s.quit()

col1, col2 = st.columns((4,5))

with col1:
    st.title("My Resume")
    st.header("Hagan Griffin")

    st.divider()

    name = st.text_input("Your Name: ")
    em = st.text_input("Your Email: ")

    st.text_area("Your Message: ")
    st.button("Send Message", on_click=email())
with col2:
    image = Image.open("95491254_1793332580791165_476135126632235008_n.jpg")
    st.image(image, width=200)

    st.divider()

    st.markdown("**About Me**")
    st.text("I am a Cybersecurity Tech, Cook, and Mechanic")



