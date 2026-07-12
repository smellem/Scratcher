import hashlib
import random


def _md5(data):
    return hashlib.md5(data.encode() if isinstance(data, str) else data).hexdigest()


def _asset_id():
    return hashlib.md5(str(random.random()).encode()).hexdigest()[:32]


class Costume:
    def __init__(self, name, svg_xml, center_x=0, center_y=0):
        self.name = name
        self.svg_xml = svg_xml
        self.center_x = center_x
        self.center_y = center_y
        self.asset_id = _asset_id()
        self.data_format = 'svg'
        self.rotation_center_x = center_x
        self.rotation_center_y = center_y

    def to_dict(self):
        return {
            "name": self.name,
            "dataFormat": self.data_format,
            "assetId": self.asset_id,
            "md5ext": f"{self.asset_id}.svg",
            "rotationCenterX": self.rotation_center_x,
            "rotationCenterY": self.rotation_center_y
        }


class Sound:
    def __init__(self, name, rate=44100, sample_count=0):
        self.name = name
        self.rate = rate
        self.sample_count = sample_count
        self.asset_id = hashlib.md5(str(random.random()).encode()).hexdigest()[:32]
        self.data_format = 'wav'

    def to_dict(self):
        return {
            "name": self.name,
            "assetId": self.asset_id,
            "dataFormat": self.data_format,
            "format": "",
            "rate": self.rate,
            "sampleCount": self.sample_count,
            "md5ext": f"{self.asset_id}.wav"
        }


class Sprite:
    def __init__(self, name='Sprite1', is_stage=False):
        self.name = name
        self.is_stage = is_stage
        self.variables = {}
        self.lists = {}
        self.broadcasts = {}
        self.blocks = {}
        self.comments = {}
        self.current_costume = 0
        self.costumes = []
        self.sounds = []
        self.volume = 100
        self.layer_order = 1 if not is_stage else 0
        self.visible = True
        self.x = 0
        self.y = 0
        self.size = 100
        self.direction = 90
        self.draggable = False
        self.rotation_style = 'all around'

    def add_costume(self, costume):
        self.costumes.append(costume)

    def add_sound(self, sound):
        self.sounds.append(sound)

    def set_blocks(self, blocks):
        self.blocks = blocks

    def to_dict(self):
        result = {
            "isStage": self.is_stage,
            "name": self.name,
            "variables": {},
            "lists": {},
            "broadcasts": {},
            "blocks": self.blocks,
            "comments": {},
            "currentCostume": self.current_costume,
            "costumes": [c.to_dict() for c in self.costumes],
            "sounds": [s.to_dict() for s in self.sounds],
            "volume": self.volume,
            "layerOrder": self.layer_order,
        }
        if not self.is_stage:
            result.update({
                "visible": self.visible,
                "x": self.x,
                "y": self.y,
                "size": self.size,
                "direction": self.direction,
                "draggable": self.draggable,
                "rotationStyle": self.rotation_style
            })
        return result
