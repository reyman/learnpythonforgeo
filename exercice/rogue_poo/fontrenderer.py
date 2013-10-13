import pygame
class FontRenderer(object):
  
  def __init__(self, fontname="lmmono10-regular.otf", size=28):
    self.font = pygame.font.Font(fontname, size) 
    self.cache = {}
    
  def render(self, text, color=(255,255,255)):
    key = text, color
    if not key in self.cache.keys():
      self.cache[key] = self.font.render(text, True, color)
    return self.cache[key]