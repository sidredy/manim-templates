# Project: Manim-Templates
# Copyright(c) 2024 Skillbanc.com, Inc.
# License: MIT License
# Contributor(s):   
#   Sudhakar Moparthy
#   Rohit Vailla

from cloup import Color
from manim import*


class CVO:
  
  def setPosition(self,pos):
    self.pos = pos
    return self
  
  def setangle(self,angle):
    self.angle = angle
    return self
  
  def setc1nameposition(self,c1nameposition):
    self.c1nameposition = c1nameposition
    return self
  
  def seto1nameposition(self,o1nameposition):
    self.o1nameposition = o1nameposition
    return self
  
  def setduration(self,duration):
    self.duration = duration
    return self
  
  def CreateCVO(self,cname,oname):
    self.c1nameposition = None
    self.o1nameposition = None
    self.oname = oname
    self.cname = cname
    self.circle_radius=1
    self.circle_color = Color.blue
    self.cvolist = []
    self.pos = [0,0,0]
    self.angle = TAU/4
    self.duration = 1
    self.cnameMObject = None
    self.onameMObject = None
    return self

  