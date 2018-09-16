# manimProjects
Playing around with manim - animation engine used by 3Blue1Brown
## Installation
1. Clone [Manim repository by 3b1b](https://github.com/3b1b/manim) 

>    git clone https://github.com/3b1b/manim.git

   
2. Follow the Installation instructions from [here](https://github.com/3b1b/manim#install-requirements) 

3. Open `constants.py` and set `MEDIA_DIR` 
to point to the directory in your system where image and animation files will be written

>   #Change this to your own directory
>
>   MEDIA_DIR = os.path.join(
os.path.expanduser('~'),
"Dropbox (3Blue1Brown)/3Blue1Brown Team Folder"
)


4. Try running the following:

>   python extract_scene.py example_scenes.py SquareToCircle -pl

5. If this doesn't work for you. Check the dependencies or check the [issues page](https://github.com/3b1b/manim/issues?utf8=%E2%9C%93&q=is%3Aissue+is%3Aclosed) for your errors 

## Scripts and Demos
Gif demos of the scripts I have experimented with
### Hello World
![Alt Text](https://github.com/sujay-mahadik/manimProjects/blob/master/gifs/hello_world.gif)

[Hello World Script](https://github.com/sujay-mahadik/manimProjects/blob/master/scripts/hello_world.py)
