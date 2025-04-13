import logging as lg
import streamlit as st
from scraper import Scraper
from prompt_parse import Parse
from dotenv import load_dotenv

load_dotenv()
scraper = Scraper()
parse = Parse()

lg.basicConfig(filename='logs/streamlit_app.log',
               level=lg.INFO,
               format='%(levelname)s:%(asctime)s:%(message)s',
               datefmt="%Y-%m-%d %H:%M:%S")

st.title("Advanced Web Scraper")
st.markdown("Made by [Onat Karabulut](https://github.com/onatkarabulut)")
url = st.text_input("Enter a URL: ")

if st.button("Scrape"):
    st.write("Scraping the website")
    raw_html = scraper.scrape_website(website=url)
    html_body = scraper.extract_html(html=raw_html)
    clean_html = scraper.clean_html(html_body=html_body)
    st.session_state.dom_content = clean_html
    st.session_state.show_view = True  

if "dom_content" in st.session_state and st.session_state.get("show_view", False):
    with st.expander("View"):
        st.text_area("Raw Content", st.session_state.dom_content, height=400)

if "dom_content" in st.session_state:
    content_desc = st.text_area("What would you like to parse?")

    if st.button("Parse Content"):
        if content_desc:
            with st.spinner("Analyzing..."):
                doms = scraper.split_html_dom(st.session_state.dom_content)
                result = parse.ollama_parse(doms=doms, parse_desc=content_desc)
            st.write(result)
            st.session_state.show_view = False  
