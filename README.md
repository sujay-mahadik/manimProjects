# manimProjects
Playing around with manim - animation engine used by 3Blue1Brown
## Installation
1. Clone [Manim repository by 3b1b](https://github.com/3b1b/manim) 

```
git clone https://github.com/3b1b/manim.git
```

   
2. Follow the Installation instructions from [here](https://github.com/3b1b/manim#install-requirements) 

3. Open `constants.py` and set `MEDIA_DIR` 
to point to the directory in your system where image and animation files will be written
```
#Change this to your own directory
MEDIA_DIR = os.path.join(
os.path.expanduser('~'),
"Dropbox (3Blue1Brown)/3Blue1Brown Team Folder"
)
```

4. Try running the following:
The `-p` is for previewing, meaning the the video file will automatically open when it is done rendering. Use `-l` for a faster rendering at a lower quality. Use `-s` to skip to the end and just show the final frame. Use `-n (number)` to skip ahead to the n'th animation of a scene. Use `-f` to show the file in directory.
```
python3 extract_scene.py example_scenes.py SquareToCircle -pl
```


5. If this doesn't work for you. Check the dependencies or check the [issues page](https://github.com/3b1b/manim/issues?utf8=%E2%9C%93&q=is%3Aissue+is%3Aclosed) for your errors 

## Scripts and Demos
Gif demos of the scripts I have experimented with
### Hello World
 <img src="https://github.com/sujay-mahadik/manimProjects/blob/master/gifs/hello_world.gif" alt="Hello World">

[Hello World Script](https://github.com/sujay-mahadik/manimProjects/blob/master/scripts/hello_world.py)

Run:
```
python3 extract_scene.py scripts/hello_world.py HelloWorld -pl
```

 We are calling the Python3 interpreter with the `python3` command. The first argument `extract_scene.py` is the part of manim code that runs your script, imports necessary files and creates files. This argument will always be needed. The second argument `scripts/hello_world.py` is the name of the file with custom scripts. The third argument `HelloWorld` is the name of class for which you are creating the scene. A single file can contain multiple classes, you need to specify the class name for which you are creating the scene. The last arguments are well documented in installation section
