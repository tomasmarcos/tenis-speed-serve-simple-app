import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from st_pages import Page, show_pages, hide_pages
import video_processor as vp
import tempfile


import streamlit as st

st.set_page_config(page_title="Step1", layout="wide")
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

#show_pages([
    #Page("/mount/src/tenis-serve-speed-app/videoslider_streamlit.py","Step 1: Upload video"),
    #Page("/mount/src/tenis-serve-speed-app/pages/serve_start.py","Step 2: Identify when serve starts (contact point)"),
    #Page("/mount/src/tenis-serve-speed-app//pages/serve_end.py","Step 3: Identify when the serve surpases the net."),
    #Page("/mount/src/tenis-serve-speed-app/pages/calculate_speed.py","Step 4: Review information and calculate speed."),
    
#])

# hide_pages(['Home',"Serve Start","Serve End"])
st.markdown(f"# Upload your serve video and then click on process video button bellow:")
# col1, col2, col3 = st.beta_columns(3)
col1, col2, col3 = st.columns(3) # for older versions of streamlit
with col2:
  start_processing_button: bool = st.button('Process Video', type="primary")
st.markdown(f"## I) Detailed guide on how to use it:")
st.markdown(f"Step 1) Upload a video where you are serving, in the bottom left corner of this screen. Make sure the video has only your serve, cut it otherwise.")
st.markdown(f"Step 2) Identify the moment 'frame' your raquet makes contact with the ball, using the slideryou can do this using the slider. Then click select.")
st.markdown(f"Step 3) Identify the moment 'frame' the ball crosses the net, you can do this using the slider. Then click select.")
st.markdown(f"Step 4) You will be prompted to check if the you selected the right images, if you agree with  it , click on calculate  speed to check your speedserve.")
st.markdown(f"## II) Assumptions & biases")
st.markdown(f"1) We assume the ball travels in a straight motion, which might not be the case. Nevertheless the error due to this cause should be small.")
st.markdown(f"2) The camera setting should be correct. The higher the FPS of the camera, the less error this will have. The error should be still small")
st.markdown(f"## III) Future work: ")
st.markdown(f"1) Add a ball tracker and raquet tracker to use computer vision in order to automate this.")
st.markdown(f"2) Add a depth estimator for use different approaches")
st.markdown(f"3) Add pose estimation & identify error of the user that is serving.")
st.markdown(f" Feel free to reach me out if you have any CV project, want to contribute to this one or have any suggestion!")
st.markdown(f"Contact: m.tomasmarcos@gmail.com")

uploaded_file = st.sidebar.file_uploader("Upload a video", type=["mp4"])



if start_processing_button:
  if uploaded_file is not None:
    print(f"TEMP UPLOADED FILENAME: {uploaded_file}")
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())
    video_info_dict = vp.video_to_frames(tfile.name,
                                preprocessing_func = vp.preprocessing_frame_pipe
                                )
    
    print("[INFO] Saving session_state variables!")
    st.session_state["frames"] = video_info_dict["frames_prep_list"] 
    st.session_state["n_frames"] = video_info_dict["n_frames_metadata"] 
    st.session_state["fps"] = video_info_dict["fps"] 
    n_frames, image_shape = video_info_dict["n_frames_metadata"], video_info_dict["frames_prep_list"][0].shape
    print(f"NFRAMES: {n_frames} ; IMAGE SHAPE: {image_shape}")
    
    switch_page("Step 2: Identify when serve starts (contact point)")
    #switch_page("serve start")

