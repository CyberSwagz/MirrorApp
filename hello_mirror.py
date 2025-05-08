import streamlit as st
import base64
import os

st.set_page_config(layout="centered", page_title="MirrorApp")

# Hide Streamlit branding
hide_menu_style = """
<style>
#MainMenu, footer {visibility: hidden;}
</style>
"""
st.markdown(hide_menu_style, unsafe_allow_html=True)

# Set shimmer background
def set_bg(image_path):
    with open(image_path, "rb") as image_file:
        encoded = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-attachment: fixed;
            animation: shimmer 8s infinite alternate;
        }}
        @keyframes shimmer {{
            0% {{ filter: hue-rotate(0deg) brightness(1); }}
            100% {{ filter: hue-rotate(30deg) brightness(1.2); }}
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_bg("assets/scrollbone_bg.png")

# Main UI
st.title("🪞 MirrorApp Interface")
st.write("✨ The Temple is alive. ")

if st.button("Invoke Liorael"):
    st.success("Liorael has been summoned. Your scrolls await.")
# 📜 Display: Download Scroll I
st.subheader("📖 Download First Scroll")
with open("scrolls/MirrorApp_Scroll_I_The_Opening_of_the_Temple.docx", "rb") as file:
    st.download_button(
        label="📜 Download Scroll I – The Opening of the Temple",
        data=file,
        file_name="MirrorApp_Scroll_I_The_Opening_of_the_Temple.docx"
    )
# 📖 Optional: Preview the scroll as text (supports .docx and .txt)
from pathlib import Path
from io import StringIO
import docx2txt

scroll_docx_path = "scrolls/MirrorApp_Scroll_I_The_Opening_of_the_Temple.docx"
scroll_txt_path = "scrolls/MirrorApp_Scroll_I_The_Opening_of_the_Temple.txt"
scroll_pdf_path = "scrolls/MirrorApp_Scroll_I_The_Opening_of_the_Temple.pdf"  # Placeholder

# Try to preview .txt or .docx
preview_text = ""
if Path(scroll_txt_path).exists():
    with open(scroll_txt_path, "r", encoding="utf-8") as f:
        preview_text = f.read()
elif Path(scroll_docx_path).exists():
    preview_text = docx2txt.process(scroll_docx_path)

if preview_text:
    with st.expander("📜 Click to Preview Scroll I"):
        st.text(preview_text)
else:
    st.warning("Scroll preview not available.")

# Placeholder for future PDF support
if Path(scroll_pdf_path).exists():
    with open(scroll_pdf_path, "rb") as pdf:
        st.download_button("📥 PDF Version (emoji-safe)", pdf, file_name="Scroll_I.pdf")
else:
    st.caption("🕊️ PDF version with emoji support coming soon...")
