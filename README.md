![](https://github.com/vbhaip/hacktj2019/blob/master/CodeBlocks%20Logo.png?raw=true)


# CodeBlocks

This repository contains our 2019 HackTJ project. You can check out the Devpost submission [here](https://devpost.com/software/codeblocks).

### What it does

The project parses physical blocks of code that can be put under a web cam into actual code that is run. Basically, its like  [Scratch](https://en.wikipedia.org/wiki/Scratch_(programming_language)), but using physical blocks.

### Why did we make it

Getting into computer science at a young age can be intimidating, and students generally prefer a visual hands-on experience to process information better. Additionally, we wanted to make a more accessible and fun way for people to get involved in coding.

### How'd we do it

The first step was to detect the blocks under the webcam. We detected the contours of the physical blocks, and found attributes (color, number of vertices) of them. The color of the block told what the type of the block was.

|Color  |Type of Block|
|---    |----   |
|Pink   |Structural (If, Else, For)|
|Yellow |Parameters (Conditions for If, Iterator for For)|
|Green  |Actions (Opening Spotify, Search Google, etc.)|

The number of vertices allowed us to tell what the specific function of a block was and to account for that in the code.

The Computer Vision aspect of the program detects the different blocks and creates an array of tuples, with each tuples representing a block having the features of the top x and y coordintes, the color, and the number of points. Additionally, we detect a play button that when pressed (covered up), executes the code itself.

The array of tuples is then parsed into Objects we made to encapsulate the functionality of the code. We designed this so that programs are generalizeable - you can nest loop statements and move around blocks as if it was real code.

The last part of the program was evaluating whether conditions were true or not and running actions. The Object classes which contained the structure of the parsed code had methods set for the actions and evaluting conditions, so we created methods to just evaluate the objects after the run button was pressed.

### Demo

[![Video Demonstration](http://img.youtube.com/vi/JLW0_6bc3CM/0.jpg)](http://www.youtube.com/watch?v=JLW0_6bc3CM)


