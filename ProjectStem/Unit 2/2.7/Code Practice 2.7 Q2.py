"""
In this exercise, we will analyze data mapping by looking at the path of a wild green sea turtle.

In geography, longitude represents the x-axis or movement horizontally, and latitude represents the y-axis or movement vertically (in other words, how far you are from the equator). Latitude increases as you go north, and the longitude gets larger as you go east for this area of the globe.

For example, the coordinates for Times Square in New York City are Latitude 40.7577° N, Longitude 73.9857° W.

The tracking data for a green sea turtle can be found here:

Signals of Spring Maps (Links to an external site.)

This data table lists dates that the green sea turtle's location was tracked, along with its latitude and longitude on that date. You can take any one of these points and plug it into Google Maps and see the turtle's location. On June 8th, 2022, written as 6/8/22 in the data set, it is near French-Martinique, shown as a black pin on the map below:

https://files.projectstem.org/CSFundamentals/CSF_Images/2.7_CP2_turtle_map.png

Map of turtle locations, indicated with black pins

The following lines of code represent some locations of a sea turtle that are denoted with black pins in latitudes and longitudes.

lat = [15.18, 15.11, 15.12, 15.12, 15.08, 14.95, 14.87, 14.81, 14.81, 14.75, 14.73, 14.68, 14.55]
lon = [-62.942, -62.807, -62.622, -62.499, -62.438, -62.372, -62.352, -62.318, -62.321, -62.201, -62.150, -62.154, -61.915]

The lat list indicates how far north and south the positions are, and the lon list represents how far east and west the positions are. The larger the latitude value, the further north the seal was located, and for this area of the world, the larger the longitude value, the further east the turtle is located.

Write a program to calculate the farthest in each direction that the turtle was located throughout its travels. Add four print statements to the lines of code above that output the following, where the number signs are replaced with the correct values from the correct list:

Farthest north is #
Farthest west is #
Farthest south is #
Farthest east is #
"""

lat = [15.18, 15.11, 15.12, 15.12, 15.08, 14.95, 14.87, 14.81, 14.81, 14.75, 14.73, 14.68, 14.55]
lon = [-62.942, -62.807, -62.622, -62.499, -62.438, -62.372, -62.352, -62.318, -62.321, -62.201, -62.150, -62.154, -61.915]

print("Farthest north is " + str(max(lat)))
print("Farthest west is " + str(min(lon)))
print("Farthest south is " + str(min(lat)))
print("Farthest east is " + str(max(lon)))