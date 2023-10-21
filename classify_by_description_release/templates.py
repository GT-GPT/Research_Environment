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

'two_shots_one_feature': f"""Q: What are useful visual features for distinguishing a lemur in a photo?
A: There are several useful visual features to tell there is a lemur in a photo:
- wet and hairless nose with curved nostrils

Q: What are useful visual features for distinguishing a television in a photo?
A: There are several useful visual features to tell there is a television in a photo:
- a large, rectangular screen
""",

'two_shots_two_features': f"""Q: What are useful visual features for distinguishing a lemur in a photo?
A: There are several useful visual features to tell there is a lemur in a photo:
- four-limbed primate
- wet and hairless nose with curved nostrils

Q: What are useful visual features for distinguishing a television in a photo?
A: There are several useful visual features to tell there is a television in a photo:
- electronic device
- a large, rectangular screen
""",

'two_shots_three_features': f"""Q: What are useful visual features for distinguishing a lemur in a photo?
A: There are several useful visual features to tell there is a lemur in a photo:
- four-limbed primate
- wet and hairless nose with curved nostrils
- long tail

Q: What are useful visual features for distinguishing a television in a photo?
A: There are several useful visual features to tell there is a television in a photo:
- electronic device
- a large, rectangular screen
- a stand or mount to support the screen
""",

'two_shots_four_features': f"""Q: What are useful visual features for distinguishing a lemur in a photo?
A: There are several useful visual features to tell there is a lemur in a photo:
- four-limbed primate
- wet and hairless nose with curved nostrils
- long tail
- large eyes

Q: What are useful visual features for distinguishing a television in a photo?
A: There are several useful visual features to tell there is a television in a photo:
- electronic device
- a large, rectangular screen
- a stand or mount to support the screen
- input ports for connecting to other devices
""",

'two_shots_five_features': f"""Q: What are useful visual features for distinguishing a lemur in a photo?
A: There are several useful visual features to tell there is a lemur in a photo:
- four-limbed primate
- wet and hairless nose with curved nostrils
- long tail
- large eyes
- furry bodies

Q: What are useful visual features for distinguishing a television in a photo?
A: There are several useful visual features to tell there is a television in a photo:
- electronic device
- a large, rectangular screen
- a stand or mount to support the screen
- a power cord
- input ports for connecting to other devices
""",

'two_shots_six_features': f"""Q: What are useful visual features for distinguishing a lemur in a photo?
A: There are several useful visual features to tell there is a lemur in a photo:
- four-limbed primate
- wet and hairless nose with curved nostrils
- long tail
- large eyes
- furry bodies
- clawed hands and feet

Q: What are useful visual features for distinguishing a television in a photo?
A: There are several useful visual features to tell there is a television in a photo:
- electronic device
- a large, rectangular screen
- a stand or mount to support the screen
- one or more speakers
- a power cord
- input ports for connecting to other devices
""",

'two_shots_seven_features': f"""Q: What are useful visual features for distinguishing a lemur in a photo?
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
- a large, rectangular screen
- a stand or mount to support the screen
- one or more speakers
- a power cord
- input ports for connecting to other devices
- a remote control
""",

"two_shots_with_role" : 
f"""You are a visual description generator. For a given category or object, create visual descriptions that distinctly explain that category or object.

Q: What are useful visual features for distinguishing a lemur in a photo?
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

"two_shots_with_rule" : 
f"""Create only static visual features. Avoid creating dynamic visual features, such as movements.
Create features that are not shared in other object categories.
Create features without considering their background features.
If more than one object exists, create each unique visual features.
Create a particularly unique feature of the design or shape of this object.

Q: What are useful visual features for distinguishing a lemur in a photo?
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

"two_shots_with_role_and_rule" : 
f"""You are a visual description generator. For a given category or object, create visual descriptions that distinctly explain that category or object.

Create only static visual features. Avoid creating dynamic visual features, such as movements.
Create features that are not shared in other object categories.
Create features without considering their background features.
If more than one object exists, create each unique visual features.
Create a particularly unique feature of the design or shape of this object.

Q: What are useful visual features for distinguishing a lemur in a photo?
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

"two_shot_detailed_one_features" :
f"""Q: What are useful visual features for distinguishing a lemur in a photo?
A: There are several useful visual features to tell there is a lemur in a photo:
- Most lemurs sport long, bushy tails. Some species, like the ring-tailed lemur, have alternating black and white bands, which is a signature feature.

Q: What are useful visual features for distinguishing a television in a photo?
A: There are several useful visual features to tell there is a television in a photo:
- Televisions predominantly feature a rectangular screen. This screen is usually black or displays colorful images when turned on, and is the most prominent feature of any TV set.
""",

"two_shot_detailed_two_features" :
f"""Q: What are useful visual features for distinguishing a lemur in a photo?
A: There are several useful visual features to tell there is a lemur in a photo:
- Lemurs often have distinct facial markings. Many species exhibit a contrasting white face mask against a darker surrounding fur, making their facial features prominent.
- Most lemurs sport long, bushy tails. Some species, like the ring-tailed lemur, have alternating black and white bands, which is a signature feature.

Q: What are useful visual features for distinguishing a television in a photo?
A: There are several useful visual features to tell there is a television in a photo:
- Televisions predominantly feature a rectangular screen. This screen is usually black or displays colorful images when turned on, and is the most prominent feature of any TV set.
- Modern televisions often have thin bezels surrounding the screen. Older models might exhibit broader, more pronounced bezels, sometimes housing buttons or dials.
""",

"two_shot_detailed_three_features" :
f"""Q: What are useful visual features for distinguishing a lemur in a photo?
A: There are several useful visual features to tell there is a lemur in a photo:
- Lemurs often have distinct facial markings. Many species exhibit a contrasting white face mask against a darker surrounding fur, making their facial features prominent.
- Most lemurs sport long, bushy tails. Some species, like the ring-tailed lemur, have alternating black and white bands, which is a signature feature.
- Unique to lemurs, they often cling to trees in a vertical posture, using their long limbs and digits to grip onto the bark.

Q: What are useful visual features for distinguishing a television in a photo?
A: There are several useful visual features to tell there is a television in a photo:
- Televisions predominantly feature a rectangular screen. This screen is usually black or displays colorful images when turned on, and is the most prominent feature of any TV set.
- Modern televisions often have thin bezels surrounding the screen. Older models might exhibit broader, more pronounced bezels, sometimes housing buttons or dials.
- Many televisions have the manufacturer's logo or brand name displayed on the bezel, stand, or occasionally on the screen itself during startup.
""",

"two_shot_detailed_four_features" :
f"""Q: What are useful visual features for distinguishing a lemur in a photo?
A: There are several useful visual features to tell there is a lemur in a photo:
- Lemurs often have distinct facial markings. Many species exhibit a contrasting white face mask against a darker surrounding fur, making their facial features prominent.
- Most lemurs sport long, bushy tails. Some species, like the ring-tailed lemur, have alternating black and white bands, which is a signature feature.
- Unique to lemurs, they often cling to trees in a vertical posture, using their long limbs and digits to grip onto the bark.
- Lemurs have a wet, dog-like nose (rhinarium), distinguishing them from other primates. This feature is most noticeable in species like the sifaka, emphasizing their reliance on scent.

Q: What are useful visual features for distinguishing a television in a photo?
A: There are several useful visual features to tell there is a television in a photo:
- Televisions predominantly feature a rectangular screen. This screen is usually black or displays colorful images when turned on, and is the most prominent feature of any TV set.
- Modern televisions often have thin bezels surrounding the screen. Older models might exhibit broader, more pronounced bezels, sometimes housing buttons or dials.
- Many televisions have the manufacturer's logo or brand name displayed on the bezel, stand, or occasionally on the screen itself during startup.
- While not part of the TV itself, remote controls are often associated with and found near televisions in photos. Their presence can suggest a TV is nearby.
""",

"two_shot_detailed_five_features" :
f"""Q: What are useful visual features for distinguishing a lemur in a photo?
A: There are several useful visual features to tell there is a lemur in a photo:
- Lemurs often have distinct facial markings. Many species exhibit a contrasting white face mask against a darker surrounding fur, making their facial features prominent.
- Lemurs have large, round eyes which are adapted for night vision. Their eyes can vary in color, often appearing as bright and reflective.
- Most lemurs sport long, bushy tails. Some species, like the ring-tailed lemur, have alternating black and white bands, which is a signature feature.
- Unique to lemurs, they often cling to trees in a vertical posture, using their long limbs and digits to grip onto the bark.
- Lemurs have a wet, dog-like nose (rhinarium), distinguishing them from other primates. This feature is most noticeable in species like the sifaka, emphasizing their reliance on scent.

Q: What are useful visual features for distinguishing a television in a photo?
A: There are several useful visual features to tell there is a television in a photo:
- Televisions predominantly feature a rectangular screen. This screen is usually black or displays colorful images when turned on, and is the most prominent feature of any TV set.
- Modern televisions often have thin bezels surrounding the screen. Older models might exhibit broader, more pronounced bezels, sometimes housing buttons or dials.
- The backside of a television generally houses various ports such as HDMI, USB, and audio outputs. This array of connections is distinctive of TV sets.
- Many televisions have the manufacturer's logo or brand name displayed on the bezel, stand, or occasionally on the screen itself during startup.
- While not part of the TV itself, remote controls are often associated with and found near televisions in photos. Their presence can suggest a TV is nearby.
""",

"two_shot_detailed_six_features" :
f"""Q: What are useful visual features for distinguishing a lemur in a photo?
A: There are several useful visual features to tell there is a lemur in a photo:
- Lemurs often have distinct facial markings. Many species exhibit a contrasting white face mask against a darker surrounding fur, making their facial features prominent.
- Lemurs have large, round eyes which are adapted for night vision. Their eyes can vary in color, often appearing as bright and reflective.
- Most lemurs sport long, bushy tails. Some species, like the ring-tailed lemur, have alternating black and white bands, which is a signature feature.
- Unique to lemurs, they often cling to trees in a vertical posture, using their long limbs and digits to grip onto the bark.
- Lemurs range from the tiny mouse lemur to the larger indri. Their body shape is typically slender, with a slightly hunched back, and they possess dexterous fingers and toes.
- Lemurs have a wet, dog-like nose (rhinarium), distinguishing them from other primates. This feature is most noticeable in species like the sifaka, emphasizing their reliance on scent.

Q: What are useful visual features for distinguishing a television in a photo?
A: There are several useful visual features to tell there is a television in a photo:
- Televisions predominantly feature a rectangular screen. This screen is usually black or displays colorful images when turned on, and is the most prominent feature of any TV set.
- Modern televisions often have thin bezels surrounding the screen. Older models might exhibit broader, more pronounced bezels, sometimes housing buttons or dials.
- TVs usually come with stands for table placement or mounts for wall-hanging. These supports may vary in design but are typically centered beneath or on the back of the device.
- The backside of a television generally houses various ports such as HDMI, USB, and audio outputs. This array of connections is distinctive of TV sets.
- Many televisions have the manufacturer's logo or brand name displayed on the bezel, stand, or occasionally on the screen itself during startup.
- While not part of the TV itself, remote controls are often associated with and found near televisions in photos. Their presence can suggest a TV is nearby.
""",


"two_shot_detailed_seven_features" :
f"""Q: What are useful visual features for distinguishing a lemur in a photo?
A: There are several useful visual features to tell there is a lemur in a photo:
- Lemurs often have distinct facial markings. Many species exhibit a contrasting white face mask against a darker surrounding fur, making their facial features prominent.
- Lemurs have large, round eyes which are adapted for night vision. Their eyes can vary in color, often appearing as bright and reflective.
- Most lemurs sport long, bushy tails. Some species, like the ring-tailed lemur, have alternating black and white bands, which is a signature feature.
- Unique to lemurs, they often cling to trees in a vertical posture, using their long limbs and digits to grip onto the bark.
- Lemurs range from the tiny mouse lemur to the larger indri. Their body shape is typically slender, with a slightly hunched back, and they possess dexterous fingers and toes.
- Although this is auditory rather than visual, in videos or sequences of photos, lemurs can be seen making distinct calls, characterized by loud shrieks, chatters, or howls.
- Lemurs have a wet, dog-like nose (rhinarium), distinguishing them from other primates. This feature is most noticeable in species like the sifaka, emphasizing their reliance on scent.

Q: What are useful visual features for distinguishing a television in a photo?
A: There are several useful visual features to tell there is a television in a photo:
- Televisions predominantly feature a rectangular screen. This screen is usually black or displays colorful images when turned on, and is the most prominent feature of any TV set.
- Modern televisions often have thin bezels surrounding the screen. Older models might exhibit broader, more pronounced bezels, sometimes housing buttons or dials.
- TVs usually come with stands for table placement or mounts for wall-hanging. These supports may vary in design but are typically centered beneath or on the back of the device.
- The backside of a television generally houses various ports such as HDMI, USB, and audio outputs. This array of connections is distinctive of TV sets.
- Many televisions have the manufacturer's logo or brand name displayed on the bezel, stand, or occasionally on the screen itself during startup.
- While not part of the TV itself, remote controls are often associated with and found near televisions in photos. Their presence can suggest a TV is nearby.
- Most televisions have a 16:9 aspect ratio, making them wider horizontally. This is distinct from older models which had a squarer 4:3 ratio. The shape can help identify the TV's era.
"""


}