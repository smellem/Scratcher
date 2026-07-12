from .generator import SVG, Circle, Rect, Ellipse, Polygon, Group, LinearGradient, RadialGradient


def sprite_circle(radius=50, color='#4A90D9', label=None):
    svg = SVG(width=radius*2+20, height=radius*2+20, viewbox=f'{-radius-10} {-radius-10} {radius*2+20} {radius*2+20}')
    svg.add(Circle(cx=0, cy=0, r=radius, fill=color, stroke='#333', stroke_width=2))
    if label:
        from .generator import Text
        svg.add(Text(x=0, y=5, text=label, font_size=radius, fill='#fff',
                     text_anchor='middle', font_weight='bold'))
    return svg


def sprite_rect(width=80, height=80, color='#E74C3C', rx=8):
    svg = SVG(width=width+20, height=height+20, viewbox=f'{-width//2-10} {-height//2-10} {width+20} {height+20}')
    from .generator import Rect
    svg.add(Rect(x=-width//2, y=-height//2, width=width, height=height,
                 rx=rx, fill=color, stroke='#333', stroke_width=2))
    return svg


def sprite_star(size=60, color='#F1C40F'):
    svg = SVG(width=size+20, height=size+20, viewbox=f'{-size//2-10} {-size//2-10} {size+20} {size+20}')
    from .generator import Polygon
    cx, cy = 0, 0
    points = []
    for i in range(5):
        outer_angle = -90 + i * 72
        inner_angle = -90 + i * 72 + 36
        import math
        points.append((cx + size/2 * math.cos(math.radians(outer_angle)),
                       cy + size/2 * math.sin(math.radians(outer_angle))))
        points.append((cx + size/4 * math.cos(math.radians(inner_angle)),
                       cy + size/4 * math.sin(math.radians(inner_angle))))
    svg.add(Polygon(points, fill=color, stroke='#333', stroke_width=2))
    return svg


def sprite_arrow(size=50, color='#2ECC71', direction='right'):
    svg = SVG(width=size+20, height=size+20, viewbox=f'{-size//2-10} {-size//2-10} {size+20} {size+20}')
    from .generator import Polygon
    if direction == 'right':
        pts = [(-size//2, -size//3), (-size//2, size//3), (size//2, 0)]
    elif direction == 'left':
        pts = [(size//2, -size//3), (size//2, size//3), (-size//2, 0)]
    elif direction == 'up':
        pts = [(-size//3, size//2), (size//3, size//2), (0, -size//2)]
    else:
        pts = [(-size//3, -size//2), (size//3, -size//2), (0, size//2)]
    svg.add(Polygon(pts, fill=color, stroke='#333', stroke_width=2))
    return svg


def backdrop_grid(rows=3, cols=4, color1='#FFFFFF', color2='#CCCCCC'):
    svg = SVG(width=480, height=360)
    cell_w, cell_h = 480 // cols, 360 // rows
    for r in range(rows):
        for c in range(cols):
            color = color1 if (r + c) % 2 == 0 else color2
            from .generator import Rect
            svg.add(Rect(x=c*cell_w, y=r*cell_h, width=cell_w, height=cell_h, fill=color))
    return svg


def backdrop_color(color='#87CEEB'):
    svg = SVG(width=480, height=360)
    from .generator import Rect
    svg.add(Rect(x=0, y=0, width=480, height=360, fill=color))
    return svg
