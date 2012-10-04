import sys, pygame
import constants as c

colorRules = {}

def drawInit():
 pygame.init()

def drawScreen(t_view,speed): 
 
 grid_size = grid_rows, grid_cols = len(t_view), len(t_view)
 square_pixels = 15
 base_offset = 30
 size = width, height = (2*base_offset)+(grid_cols*square_pixels), (2*base_offset)+(grid_rows*square_pixels)
 
 screen = pygame.display.set_mode(size)
 clock = pygame.time.Clock()
 
 render_steps = True
 screen.fill(c.cBlack)
 
 for event in pygame.event.get():
  if event.type == pygame.QUIT: sys.exit()
 
 for row in xrange(grid_rows):
  for col in xrange(grid_cols):
   for ncolor in colorRules.keys():
     if (t_view[row][col] == ncolor):
      FillSquare(screen, base_offset, square_pixels,(row, col), colorRules[ncolor])

 #draw the outer border
 border_rect = (base_offset, base_offset, (grid_cols*square_pixels), (grid_rows*square_pixels))
 pygame.draw.rect(screen, c.cGrey, border_rect, 2)
    
 pygame.display.flip()
 clock.tick(speed)


def FillSquare(screen, base_offset, square_pixels, loc, color):
 row = loc[0]
 col = loc[1]
 off_x = base_offset + col * square_pixels
 off_y = base_offset + row * square_pixels
 rect = (off_x+4, off_y+4,  square_pixels - 6, square_pixels - 6)
 pygame.draw.rect(screen, color, rect)
 
def addColorRules(num, color):
	colorRules[num] = color

def events():
 for event in pygame.event.get():
  if event.type == pygame.QUIT: sys.exit()
