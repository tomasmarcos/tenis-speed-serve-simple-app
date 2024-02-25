# This is a very basic app to measure the speed. This is hosted on streamlit and every frame goes into memory so try to not overload it. Suggestions are welcomed (pr & see contact bellow).

## Tenis serve speed app hosted on streamlit (does not contain any machine learning for now).
## I) Detailed guide on how to use it:")
Step 1) Upload a video where you are serving, in the bottom left corner of this screen. Make sure the video has only your serve.
Step 2) Identify the moment 'frame' your raquet makes contact with the ball, using the slideryou can do this using the slider. 
Step 3) Identify the moment 'frame' the ball crosses the net, you can do this using the slider. Then click select.
Step 4) You will be prompted to check if the you selected the right images, if you agree with  it , click on calculate  speed.
## II) Assumptions & biases
1) We assume the ball travels in a straight motion, which might not be the case. Nevertheless the error due to this cause should be small.
"2) The camera setting should be correct. The higher the FPS of the camera, the less error this will have. The error should be still small
## III) Future work: 
1) Add a ball tracker and raquet tracker to use computer vision in order to automate this.
2) Add a depth estimator for use different approaches
3) Add pose estimation & identify error of the user that is serving.


Feel free to reach me out if you have any CV project, want to contribute to this one or have any suggestion!
Contact: m.tomasmarcos@gmail.com