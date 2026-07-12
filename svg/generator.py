from xml.sax.saxutils import escape


class Color:
    def __init__(self, r=0, g=0, b=0, a=1):
        self.r, self.g, self.b, self.a = r, g, b, a

    @classmethod
    def hex(cls, hex_str, a=1):
        h = hex_str.lstrip('#')
        return cls(int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16), a)

    @classmethod
    def rgb(cls, r, g, b, a=1):
        return cls(r, g, b, a)

    @classmethod
    def named(cls, name):
        palette = {
            'red': (255,0,0), 'green': (0,200,0), 'blue': (0,0,255),
            'yellow': (255,255,0), 'orange': (255,165,0), 'purple': (128,0,128),
            'pink': (255,192,203), 'brown': (139,69,19), 'black': (0,0,0),
            'white': (255,255,255), 'gray': (128,128,128), 'cyan': (0,255,255),
            'magenta': (255,0,255), 'lime': (0,255,0), 'navy': (0,0,128),
            'teal': (0,128,128), 'maroon': (128,0,0), 'olive': (128,128,0),
        }
        r, g, b = colors.get(name.lower(), (0, 0, 0))
        return cls(r, g, b)

    def to_hex(self):
        return f'#{self.r:02x}{self.g:02x}{self.b:02x}'

    def to_rgba(self):
        if self.a < 1:
            return f'rgba({self.r},{self.g},{self.b},{self.a})'
        return self.to_hex()


class _Element:
    def __init__(self, tag, **attrs):
        self.tag = tag
        self.attrs = {}
        for k, v in attrs.items():
            if v is not None:
                self.attrs[k.replace('_', '-')] = v
        self.children = []

    def add(self, *elements):
        self.children.extend(elements)
        return self

    def attr(self, key, value):
        self.attrs[key.replace('_', '-')] = value
        return self

    def to_xml(self, indent=0):
        pad = '  ' * indent
        attr_str = ' '.join(f'{k}="{v}"' for k, v in self.attrs.items())
        if not self.children:
            return f'{pad}<{self.tag} {attr_str}/>'
        lines = [f'{pad}<{self.tag} {attr_str}>']
        for child in self.children:
            lines.append(child.to_xml(indent + 1))
        lines.append(f'{pad}</{self.tag}>')
        return '\n'.join(lines)


class Rect(_Element):
    def __init__(self, x=0, y=0, width=100, height=100, rx=None, ry=None,
                 fill='#4A90D9', stroke=None, stroke_width=None, opacity=None,
                 transform=None):
        super().__init__('rect', x=x, y=y, width=width, height=height,
                         rx=rx, ry=ry, fill=fill, stroke=stroke,
                         stroke_width=stroke_width, opacity=opacity,
                         transform=transform)


class Circle(_Element):
    def __init__(self, cx=0, cy=0, r=50, fill='#4A90D9', stroke=None,
                 stroke_width=None, opacity=None, transform=None):
        super().__init__('circle', cx=cx, cy=cy, r=r, fill=fill,
                         stroke=stroke, stroke_width=stroke_width,
                         opacity=opacity, transform=transform)


class Ellipse(_Element):
    def __init__(self, cx=0, cy=0, rx=50, ry=30, fill='#4A90D9',
                 stroke=None, stroke_width=None, opacity=None, transform=None):
        super().__init__('ellipse', cx=cx, cy=cy, rx=rx, ry=ry, fill=fill,
                         stroke=stroke, stroke_width=stroke_width,
                         opacity=opacity, transform=transform)


class Line(_Element):
    def __init__(self, x1=0, y1=0, x2=100, y2=100, stroke='#000',
                 stroke_width=2, opacity=None, transform=None):
        super().__init__('line', x1=x1, y1=y1, x2=x2, y2=y2, stroke=stroke,
                         stroke_width=stroke_width, opacity=opacity,
                         transform=transform)


class Polygon(_Element):
    def __init__(self, points, fill='#4A90D9', stroke=None, stroke_width=None,
                 opacity=None, transform=None):
        points_str = ' '.join(f'{x},{y}' for x, y in points)
        super().__init__('polygon', points=points_str, fill=fill,
                         stroke=stroke, stroke_width=stroke_width,
                         opacity=opacity, transform=transform)


class Polyline(_Element):
    def __init__(self, points, fill='none', stroke='#000', stroke_width=2,
                 opacity=None, transform=None):
        points_str = ' '.join(f'{x},{y}' for x, y in points)
        super().__init__('polyline', points=points_str, fill=fill,
                         stroke=stroke, stroke_width=stroke_width,
                         opacity=opacity, transform=transform)


class Path(_Element):
    def __init__(self, d='', fill='none', stroke='#000', stroke_width=2,
                 opacity=None, transform=None):
        super().__init__('path', d=d, fill=fill, stroke=stroke,
                         stroke_width=stroke_width, opacity=opacity,
                         transform=transform)


class Text(_Element):
    def __init__(self, x=0, y=0, text='', font_size=24, font_family='Arial',
                 fill='#000', text_anchor=None, font_weight=None,
                 opacity=None, transform=None):
        super().__init__('text', x=x, y=y, font_size=font_size,
                         font_family=font_family, fill=fill,
                         text_anchor=text_anchor, font_weight=font_weight,
                         opacity=opacity, transform=transform)
        self.text_content = text

    def to_xml(self, indent=0):
        pad = '  ' * indent
        attr_str = ' '.join(f'{k}="{v}"' for k, v in self.attrs.items())
        return f'{pad}<{self.tag} {attr_str}>{escape(self.text_content)}</{self.tag}>'


class Group(_Element):
    def __init__(self, fill=None, stroke=None, stroke_width=None, opacity=None,
                 transform=None):
        super().__init__('g', fill=fill, stroke=stroke,
                         stroke_width=stroke_width, opacity=opacity,
                         transform=transform)


class LinearGradient:
    def __init__(self, id, x1='0%', y1='0%', x2='100%', y2='0%'):
        self.id = id
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
        self.stops = []

    def add_stop(self, offset, color, opacity=None):
        self.stops.append((offset, color, opacity))
        return self

    def to_xml(self, indent=0):
        pad = '  ' * indent
        lines = [f'{pad}<linearGradient id="{self.id}" x1="{self.x1}" y1="{self.y1}" x2="{self.x2}" y2="{self.y2}">']
        for offset, color, opacity in self.stops:
            a = f'offset="{offset}" stop-color="{color}"'
            if opacity is not None:
                a += f' stop-opacity="{opacity}"'
            lines.append(f'{pad}  <stop {a}/>')
        lines.append(f'{pad}</linearGradient>')
        return '\n'.join(lines)


class RadialGradient:
    def __init__(self, id, cx='50%', cy='50%', r='50%'):
        self.id = id
        self.cx, self.cy, self.r = cx, cy, r
        self.stops = []

    def add_stop(self, offset, color, opacity=None):
        self.stops.append((offset, color, opacity))
        return self

    def to_xml(self, indent=0):
        pad = '  ' * indent
        lines = [f'{pad}<radialGradient id="{self.id}" cx="{self.cx}" cy="{self.cy}" r="{self.r}">']
        for offset, color, opacity in self.stops:
            a = f'offset="{offset}" stop-color="{color}"'
            if opacity is not None:
                a += f' stop-opacity="{opacity}"'
            lines.append(f'{pad}  <stop {a}/>')
        lines.append(f'{pad}</radialGradient>')
        return '\n'.join(lines)


class Filter:
    def __init__(self, id):
        self.id = id
        self.children = []

    def add(self, *elements):
        self.children.extend(elements)
        return self

    def to_xml(self, indent=0):
        pad = '  ' * indent
        lines = [f'{pad}<filter id="{self.id}">']
        for child in self.children:
            lines.append(child.to_xml(indent + 1))
        lines.append(f'{pad}</filter>')
        return '\n'.join(lines)


class _FilterElement(_Element):
    def __init__(self, tag, **attrs):
        super().__init__(tag, **attrs)


class Defs:
    def __init__(self):
        self.children = []

    def add(self, *elements):
        self.children.extend(elements)
        return self

    def to_xml(self, indent=0):
        if not self.children:
            return ''
        pad = '  ' * indent
        lines = [f'{pad}<defs>']
        for child in self.children:
            lines.append(child.to_xml(indent + 1))
        lines.append(f'{pad}</defs>')
        return '\n'.join(lines)


class SVG:
    def __init__(self, width=480, height=360, viewbox=None):
        self.width = width
        self.height = height
        self.viewbox = viewbox or f'0 0 {width} {height}'
        self.children = []
        self.defs = Defs()

    def add(self, *elements):
        self.children.extend(elements)
        return self

    def to_xml(self):
        lines = [
            '<?xml version="1.0" encoding="UTF-8"?>',
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.width}" height="{self.height}" viewBox="{self.viewbox}">'
        ]
        if self.defs.children:
            lines.append(self.defs.to_xml(1))
        for child in self.children:
            lines.append(child.to_xml(1))
        lines.append('</svg>')
        return '\n'.join(lines)

    def save(self, path):
        with open(path, 'w', encoding='utf-8') as f:
            f.write(self.to_xml())

