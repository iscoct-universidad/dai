import random
import svgwrite

def create_image():
    minViewportSize = 0
    minSize = 120
    maxViewportSize = 1280
    width = random.randint(minSize, maxViewportSize)
    height = random.randint(minSize, maxViewportSize)

    number = random.randint(0, 4)
    dwg = svgwrite.Drawing(profile='tiny')
    dwg.viewbox(minx=minViewportSize, miny=minViewportSize,
        width=maxViewportSize, height=maxViewportSize)

    color = get_color()

    if number < 2:
        maxDistance = min(maxViewportSize - width + minSize, maxViewportSize - height + minSize)
        radio = random.randint(minSize, maxDistance)

        if number == 0:
            shape = dwg.circle(center=(height, width), r=radio, stroke=color, fill=color)
        else:
            shape = dwg.rect(insert=(height, width), size=(radio, radio), stroke=color, fill=color)

    else:
        maxHeight = maxViewportSize - height
        maxWidth = maxViewportSize - width
        radioX = random.randint(minSize, maxViewportSize - maxWidth + minSize)
        radioY = random.randint(minSize, maxViewportSize - maxHeight + minSize)

        if number == 2:
            shape = dwg.ellipse(center=(height, width), r=(radioX, radioY), stroke=color, fill=color)
        else:
            shape = dwg.rect(insert=(height, width), size=(radioX, radioY), stroke=color, fill=color)

    dwg.add(shape)
    dwg.saveas('static/newImage.svg')

def get_color():
    red = random.randint(0, 256)
    green = random.randint(0, 256)
    blue = random.randint(0, 256)

    return svgwrite.rgb(red, green, blue, '%')