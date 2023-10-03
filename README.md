This program made for education putpose
It download photo from Nasa, Space_X and send it in telegram chanal
 
This program consists of two parts.
The first part is a program that allows you to upload photos on specified topics from NASA and SpaceX websites.
The second part is the publication of them in the Telegram channel.

To upload a photo, you are given the opportunity to see what kind of photos they will be.

Enter --ID_launch launch number for a photo from the NASA Website
Enter --POD and the number of photos to download for the Space_X Site
Enter --EPIC to get an EPIC photo from Space_X
If the function does not receive arguments, then the photo of the last launch will be loaded.

The second part sends photos from the list to the telegram channel. You can set the time how often the photos will be published. If you do not set a timer, by default it will happen once every 4 hours.