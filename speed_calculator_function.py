# According to this source:https://www.vts-tenis.com/images/blog/2020/dimensiones-pista-tenis-01.jpg ,  a tenis court is 23.76 meters long
tenis_court_half_long_meters = 23.76/2 # meters

def meters_to_kilometers(distance):
    "convert a distance in meters to kilombeters by dividing it by 1000"
    return distance/1000

def frames_to_time(frames_diff, fps):
    """
    Given FPS and frames diff ; this will convert it this diff to many units of time (hours seconds and minutes).
    Args:
        FPS: Stands for frames per seconds
        frames_diff: how much frames to convert to hours
    Returns:
        Dict: With Frames diff but with  differents units of measurements (hours, secs, minutes)
        Returning a dict is usefull for the explanation.
    """
    seconds_diff = frames_diff/fps 
    miliseconds_diff = (frames_diff/fps)*1000
    minutes_diff =  seconds_diff / fps
    hours_diff = seconds_diff / 3600 # 60*60
    return {
        "miliseconds_diff":miliseconds_diff,
        "seconds_diff":seconds_diff,
        "minutes_diff":minutes_diff,
        "hours_diff":hours_diff
    }

def calculate_serve_speed(frames_diff, fps, add_explanation_text = True):
    output_dict = dict()
    tenis_court_half_long_meters = 23.76/2 # meters
    frames_in_time = frames_to_time(frames_diff, fps)
    miliseconds_diff, seconds_diff = frames_in_time["miliseconds_diff"], frames_in_time["seconds_diff"]
    minutes_diff, hours_diff = frames_in_time["minutes_diff"], frames_in_time["hours_diff"]
    tenis_court_half_long_kilometers = meters_to_kilometers(tenis_court_half_long_meters)
    serve_speed = round(tenis_court_half_long_kilometers/hours_diff,2)
    output_dict["serve_speed"] = serve_speed
    if add_explanation_text:
        explanation_text = f"""
        Since there are fps Frames per seconds, in takes frames_diff/fps seconds tu get to the net
        {fps} frames = 1 second = 1000 ms
        1 frame = 1/{fps} seconds
        {frames_diff} frames = ({frames_diff}/{fps}) seconds to get to the net.
        [INFO] It takes {miliseconds_diff} for the ball to get to the net;
            this is equivelent to {seconds_diff} seconds  equivalent to {hours_diff} hours.   
            According to this source:https://www.vts-tenis.com/images/blog/2020/dimensiones-pista-tenis-01.jpg ,  a tenis court is 23.76 meters long
            - So to get to the middle of the court, we divide by two:
            tenis_court_half_long_meters = 23.76/2 
            # 1000m = 1 km
            - Convert meters to kilometers:
            tenis_court_half_long_kilometers = tenis_court_half_long_meters/1000
        [INFO] Half of a tenis court is: {tenis_court_half_long_meters} meters
            and therefore {tenis_court_half_long_kilometers} kilometers.
        So it takes {hours_diff} hours for the ball to get to the net (which is: {tenis_court_half_long_kilometers} kilometers).
        The serve speed is the ratio between the distance and hours:  {tenis_court_half_long_kilometers}/{hours_diff} ->  {serve_speed} km/h
        """
 

        output_dict["explanation_text"] = explanation_text

    
    return output_dict