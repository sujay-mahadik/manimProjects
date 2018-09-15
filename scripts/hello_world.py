from big_ol_pile_of_manim_imports import *

class HelloWorld(Scene):
#Adding text on the screen
    def construct(self):
        my_first_text=TextMobject("Hello World")
        second_line=TextMobject("This is Sujay Mahadik")
        third_line=TextMobject("and I'm trying around the manim animation engine")
        third_line.next_to(second_line,DOWN)
        fourth_line=TextMobject("inspired by 3Blue1Brown")
        fourth_line.set_color(BLUE)
        fourth_line.next_to(second_line,DOWN)
        blank = TextMobject("")
 
        self.add(my_first_text)
        self.wait(2)
        self.play(Transform(my_first_text,second_line))
        self.wait(2)
        self.play(Transform(blank, third_line))
        self.wait(4)
        self.play(Transform(blank, fourth_line))
        self.wait(2)
        