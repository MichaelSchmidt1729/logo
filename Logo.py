from svgwrite import Drawing

# Create an SVG drawing
svg_filename = "/mnt/data/Logo.svg"
dwg = Drawing(svg_filename, profile='tiny')

# Add lines and text based on the image layout and content
dwg.add(dwg.line(start=(10, 20), end=(120, 20), stroke=svgwrite.rgb(10, 10, 16, '%')))
dwg.add(dwg.line(start=(10, 20), end=(10, 100), stroke=svgwrite.rgb(10, 10, 16, '%')))
dwg.add(dwg.text('Sachverständigenbüro', insert=(15, 50), fill='black', font_size='20px', font_family='Arial'))
dwg.add(dwg.text('Dipl.-Ing. Thomas Lehnert', insert=(15, 80), fill='black', font_size='20px', font_family='Arial'))
dwg.add(dwg.line(start=(15, 85), end=(200, 85), stroke=svgwrite.rgb(10, 10, 16, '%')))

# Save the SVG file
dwg.save()
