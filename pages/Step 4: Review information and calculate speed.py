import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from st_pages import Page, show_pages, hide_pages
import sys
sys.path.append("..")
from speed_calculator_function import calculate_serve_speed
#"""
#show_pages([
    #Page("videoslider_streamlit.py","Step 1: Upload video"),
    #Page("./pages/serve_start.py","Step 2: Identify when serve starts (contact point)"),
    #Page("./pages/serve_end.py","Step 3: Identify when the serve surpases the net."),
    #Page("./pages/calculate_speed.py","Step 4: Review information and calculate speed."),
    
#])
#"""

st.set_page_config(page_title="Step4", layout="wide")
st.markdown("""
    <style>
        .reportview-container {
            margin-top: -2em;
        }
        #MainMenu {visibility: hidden;}
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
    </style>
""", unsafe_allow_html=True)

print("[INFO] Switching to page 4!")

ssession_keys = st.session_state.keys()
requires_objetts = ["n_frames","frames","frame_number_start","frame_number_end"]
all_required_objets_in_memory = len ( set(requires_objetts)-set(ssession_keys) ) == 0
if not all_required_objets_in_memory:
    st.markdown(f"## You have to upload the video and click process first, go back to Step 1.")
else:
  n_frames = st.session_state["n_frames"]
  frames_prep_list = st.session_state["frames"]
  frame_number_start = st.session_state["frame_number_start"]
  frame_number_end = st.session_state["frame_number_end"] 
  fps = st.session_state["fps"]
  st.markdown("# Please review your information before calculating speed:")
  st.markdown("Bear in mind that the worse you identify this moments, the worse the speed accuracy it will be.")

  st.markdown("### This is the moment when you make contact with the ball: ")
  st.image(frames_prep_list[frame_number_start], caption=None, width=None,
            use_column_width=None, clamp=False,
              channels="RGB", output_format="auto")

  st.markdown("### This is the moment when the ball overpasses the net:")
  st.image(frames_prep_list[frame_number_end], caption=None, width=None,
            use_column_width=None, clamp=False,
              channels="RGB", output_format="auto")


  calculate_speed_button: bool = st.button('Calculate speed')
  if calculate_speed_button:
      frame_diff = frame_number_end-frame_number_start
      st.session_state["frame_diff"] = frame_diff
      serve_speed = calculate_serve_speed(frame_diff,fps, add_explanation_text=False)
      serve_speed = serve_speed["serve_speed"]
      st.session_state["serve_speed"] = serve_speed
      st.markdown(f"## Your Serve speed is: {serve_speed} KM/H (Kilometers per hour)")
      st.write(f" Please send me an email if you wnat me to include the detailed explanation.")
      st.markdown("#### Question: How to have a good speed accuracy when calculating this?")
      st.markdown("Answer: Have good video quality (high FPS); identify accurately the moment when you hit the ball and when it crossed the net")
      # st.write(f"## See the explanation bellow in case you need it:")
