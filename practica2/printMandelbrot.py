import time
from PIL import Image

# Función que pinta en una ventana y salva en formato PPM el fractal de Mandelbrot. Nota: iteraciones tiene que ser menor que 1000
def pintaMandelbrot(x1, y1, x2, y2, ancho, iteraciones, nombreFicheroPPM):
  xa = x1
  xb = x2
  ya = y1
  yb = y2
  maxIt = iteraciones
  # image size
  imgx = ancho
  imgy = int(abs (y2 - y1) * ancho / abs(x2 - x1))
   
  im = Image.new('RGB', (imgx, imgy), color = 'black')
  
  for y in range(imgy):
    zy = y * (yb - ya) / (imgy - 1)  + ya
    
    for x in range(imgx):
      zx = x * (xb - xa) / (imgx - 1)  + xa
      z = zx + zy * 1j
      c = z
      
      for i in range(maxIt):
        if abs(z) > 2.0: break 
        z = z * z + c
        
      i = maxIt - i
      
      col = (i%10*25, i%16*16, i%8*32)
        
      im.putpixel((x, y), col)

  im.save(nombreFicheroPPM)   # Grabamos en formato PPM