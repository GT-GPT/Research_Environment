templates = {
    'two_shots': f"""Q: What are useful visual features for distinguishing a lemur in a photo?
A: There are several useful visual features to tell there is a lemur in a photo:
- four-limbed primate
- black, grey, white, brown, or red-brown
- wet and hairless nose with curved nostrils
- long tail
- large eyes
- furry bodies
- clawed hands and feet

Q: What are useful visual features for distinguishing a television in a photo?
A: There are several useful visual features to tell there is a television in a photo:
- electronic device
- black or grey
- a large, rectangular screen
- a stand or mount to support the screen
- one or more speakers
- a power cord
- input ports for connecting to other devices
- a remote control
""",

    'one_shot':f"""Q: What are useful visual features for distinguishing a lemur in a photo?
A: There are several useful visual features to tell there is a lemur in a photo:
- four-limbed primate
- black, grey, white, brown, or red-brown
- wet and hairless nose with curved nostrils
- long tail
- large eyes
- furry bodies
- clawed hands and feet """,


    'three_shots': f"""Q: What are useful visual features for distinguishing a lemur in a photo?
A: There are several useful visual features to tell there is a lemur in a photo:
- four-limbed primate
- black, grey, white, brown, or red-brown
- wet and hairless nose with curved nostrils
- long tail
- large eyes
- furry bodies
- clawed hands and feet

Q: What are useful visual features for distinguishing a television in a photo?
A: There are several useful visual features to tell there is a television in a photo:
- electronic device
- black or grey
- a large, rectangular screen
- a stand or mount to support the screen
- one or more speakers
- a power cord
- input ports for connecting to other devices
- a remote control

Q: What are useful visual features for distinguishing a pelican in a photo?
A: There are several useful visual features to tell there is a pelican in a photo:
- very large water birds
- long beak
- large throat pouch
- huge gular pouch to the lower
- white or brown plumage 
- black primary and secondary remiges
""",



    'one_shot_detailed_description' : f"""Q: What are useful visual features for distinguishing a lemur in a photo?
A: There are several useful visual features to tell there is a lemur in a photo:
- Lemurs have a distinct facial appearance with large, round, reflective eyes adapted for nighttime activity, often surrounded by dark patches or "masks."
- Many lemur species possess long, bushy tails, often with stripes or bands, which can be longer than their bodies.
- Lemurs have a compact body with elongated limbs, especially rear legs, adapted for leaping between trees, and often display a hunched posture.
""",
    

    'two_shot_detailed_description' : f"""Q: What are useful visual features for distinguishing a lemur in a photo?
A: There are several useful visual features to tell there is a lemur in a photo:
- Lemurs have a distinct facial appearance with large, round, reflective eyes adapted for nighttime activity, often surrounded by dark patches or "masks."
- Many lemur species possess long, bushy tails, often with stripes or bands, which can be longer than their bodies.
- Lemurs have a compact body with elongated limbs, especially rear legs, adapted for leaping between trees, and often display a hunched posture.

Q: What are useful visual features for distinguishing a television in a photo?
A: There are several useful visual features to tell there is a television in a photo:
- Televisions possess a clear rectangular screen, often surrounded by bezels. When off, it's typically black; when on, it displays images or colors, distinguishing it from other objects.
- TVs either sit on distinct stands, such as central pillars or side feet, or are wall-mounted using brackets, setting them apart.
- Visible cables, connecting to ports like HDMI or USB, highlight the TV's function as an entertainment hub, aiding in its identification.
""",


    'three_shot_detailed_description' : f"""Q: What are useful visual features for distinguishing a lemur in a photo?
A: There are several useful visual features to tell there is a lemur in a photo:
- Lemurs have a distinct facial appearance with large, round, reflective eyes adapted for nighttime activity, often surrounded by dark patches or "masks."
- Many lemur species possess long, bushy tails, often with stripes or bands, which can be longer than their bodies.
- Lemurs have a compact body with elongated limbs, especially rear legs, adapted for leaping between trees, and often display a hunched posture.

Q: What are useful visual features for distinguishing a television in a photo?
A: There are several useful visual features to tell there is a television in a photo:
- Televisions possess a clear rectangular screen, often surrounded by bezels. When off, it's typically black; when on, it displays images or colors, distinguishing it from other objects.
- TVs either sit on distinct stands, such as central pillars or side feet, or are wall-mounted using brackets, setting them apart.
- Visible cables, connecting to ports like HDMI or USB, highlight the TV's function as an entertainment hub, aiding in its identification.

Q: What are useful visual features for distinguishing a pelican in a photo?
A: There are several useful visual features to tell there is a pelican in a photo:
- Pelicans are known for their long bills with a distinctive, expandable throat pouch used for catching fish. This pouch is especially pronounced when feeding.
- In flight, pelicans display a broad wingspan, often gliding gracefully with a slight V-shaped neck.
- Pelicans possess stout bodies and short legs with fully webbed feet, adapting them to aquatic habitats and aiding in swimming.
""",


'two_shots_one_feature': f"""Q: What are useful visual features for distinguishing a lemur in a photo?
A: There are several useful visual features to tell there is a lemur in a photo:
- large eyes

Q: What are useful visual features for distinguishing a television in a photo?
A: There are several useful visual features to tell there is a television in a photo:
- a large, rectangular screen
""",

'two_shots_two_features': f"""Q: What are useful visual features for distinguishing a lemur in a photo?
A: There are several useful visual features to tell there is a lemur in a photo:
- wet and hairless nose with curved nostrils
- large eyes

Q: What are useful visual features for distinguishing a television in a photo?
A: There are several useful visual features to tell there is a television in a photo:
- a large, rectangular screen
- a power cord
""",

'two_shots_three_features': f"""Q: What are useful visual features for distinguishing a lemur in a photo?
A: There are several useful visual features to tell there is a lemur in a photo:
- wet and hairless nose with curved nostrils
- long tail
- large eyes

Q: What are useful visual features for distinguishing a television in a photo?
A: There are several useful visual features to tell there is a television in a photo:
- a large, rectangular screen
- a power cord
- input ports for connecting to other devices
"""

}