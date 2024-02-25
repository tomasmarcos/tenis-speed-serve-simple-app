import streamlit as st
from streamlit_extras.switch_page_button import switch_page
# from st_pages import Page, show_pages, hide_pages
#"""
#show_pages([
    #Page("videoslider_streamlit.py","Step 1: Upload video"),
    #Page("./pages/serve_start.py","Step 2: Identify when serve starts (contact point)"),
    #Page("./pages/serve_end.py","Step 3: Identify when the serve surpases the net."),
    #Page("./pages/calculate_speed.py","Step 4: Review information and calculate speed."),
    
#])
#"""
st.set_page_config(page_title="Step3", layout="wide")
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
 

print("[INFO] Switching to page 3!")

ssession_keys = st.session_state.keys()
requires_objetts = ["n_frames","frames","frame_number_start"]
all_required_objets_in_memory = len ( set(requires_objetts)-set(ssession_keys) ) == 0
if not all_required_objets_in_memory:
    st.markdown(f"## You have to upload the video and click process first, go back to Step 1.")
else:
    n_frames = st.session_state["n_frames"]
    frames_prep_list = st.session_state["frames"]
    frame_number_start = st.session_state["frame_number_start"]
    print("N_frames second page!",n_frames)


    frame_number_end = st.slider('Select the frame where you think the ball crosses the net', 0, n_frames, frame_number_start+10)
    # frame_number_end = st.number_input("Or enter the frame number...", value=0, placeholder="Type a number...")
    st.markdown(f"# Selected frame number: {frame_number_end}")
    st.image(frames_prep_list[frame_number_end], caption=None, width=None,
            use_column_width=None, clamp=False,
                channels="RGB", output_format="auto")


    selected_frame_button: bool = st.button('Select frame')
    if selected_frame_button:
        st.session_state["frame_number_end"] = frame_number_end
        print(f"[INFO] Saving selected frame as: {frame_number_end}")
        switch_page("Step 4: Review information and calculate speed")
        #switch_page("calculate speed")
