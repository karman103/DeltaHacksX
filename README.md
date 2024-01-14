# Delta_hacks_X_project
# Inspiration
The major inspiration for our team for thsi project came from seeing that even though there are correct garbage disposals sometimes it is hard to disregard in the respective trash cans. Furthermore, we also saw that

# what it does
# ow it does what it does and How we built it
# Challenges We run into
There were number of challenges we faced. From coming to this Hackathon in a snow storm to waking up for more than 24 hrs straight, at the end we learnt there was no such challenge that could stop us from having a memorable hackathon. On the technical side Computer Vision and Frontend devlopment were new fields for all of us so sometimes it took us more time on trivial issues like centring a div. On the Computer Vision side we faced a problem where our model was doing pretty well in given images but was performing poorly when given real images from our camera (we took snapshots when our camera video was on) . We theorized it could be because of many objects showna at a given time. we solved this problem via YoloV8 multiclass classification of objects in a given image. Then we used our model to classify evry object.

# What we learned
# Accomplishments we are proud of
We are extremly proud that we went out of our comfort zones and experienced field w`e werent at all famiiar with that is Computer Vision. In doing so we also did our part in having an eco-friendly future wher our solutiuon is implemted. Other than that we are also proud to take part

# Future of Eco Wiz
Talking about long term ambitions we at Eco wiz strive for a more eco friendly future. For that we see that are technology has a future in the waste management industry. We think that our technology would have an int

# Technologies usesd:
We primarily used ResNet-50 CNN deep learning model for classifying Garbage. Additionaly we leveraged YoloV8 model to solve the problem of prediction of multiple objects. We did this by taking a snapshot of the video and splitting evry recognized object by YoloV8 model into their own seperate images. Then we used the ResNet-50 model to classify evry given object. We used python and flask in the backend. In the Frontend we used Javascript, HTML, CSS, Vite and React.

