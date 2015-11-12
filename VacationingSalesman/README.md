To run the program:

	1. Edit the location.txt file to include all the desired locations. Similarly, you could add your own txt file.
	
	2. Run the file in Python and call the "salesman" function. This function takes in one argument which is the name of the txt file in the form of a string.
		For example: salesman(location.txt)

	3. The program will then prompt you whether you want distances returned in kilometers or miles. Input km if you want distances in kilometers or mi if you want distances in miles

	4. Watch the magic unfold.

I chose to use Python because it is the language I am most comfortable with. Having used it in my current CS course as well as in a couple hackathons, I felt I could code the fastest in Python. 

As for calculating the actual distances, I decided to use the Google Maps API because it seemed to be the most well documents API. Using the API, I was able to retrieve the longitudinal and latitudinal coordinates of all the locations. Initially, I wanted to use the Google Maps API to calculate the distances between these locations as well but I ran into some issues. The API didn't seem to be able to use locations outside of the United States. I commented out the code and decided to use teh Haversine function to calculate distances instead. 