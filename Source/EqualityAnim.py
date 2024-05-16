# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License

import json
from os import remove
from manim import *
from scipy.spatial import transform
from AbstractAnim import AbstractAnim

import cvo

class EqualityAnim(AbstractAnim):

    # use the appropriate method based on how the data is stored
    def construct(self):
        self.RenderEquality1()
       
        
    # render using CVO data object
    def RenderEquality1(self):
        
        textArray = []
        playedTextArray = []
        
        textArray.append("1=1")
        textArray.append("1+1=1+1")
        # textArray.append("1+1=2")
        # textArray.append("2=2")
        # textArray.append("2+1=2+1")
        
        grp1 = VGroup()
        text0 = Tex(textArray[0],color=BLUE)
        self.play(Create(text0))
        grp1.add(text0)
        
        for i in range(1,len(textArray)):
                    
          
           
           text1 = Tex(textArray[i],color=BLUE)
           
           #self.play(Transform(text0,text1))
           
           text0.remove()
           self.play(Create(text1))
           text0 = text1
           
           #grp1.shift(UP *0.5)
           
           #self.play(Create(text1))
           #grp1.add(text1)
           
        self.wait(2)
        
if __name__ == "__main__":
    scene = EqualityAnim()
    scene.render()
    