import json
import hashlib
import random


def _block_id():
    return hashlib.md5(str(random.random()).encode()).hexdigest()[:8]


class BlockBuilder:
    def __init__(self):
        self.blocks = {}
        self._next_id = 0

    def _new_id(self):
        self._next_id += 1
        return _block_id()

    def motion_movesteps(self, steps, parent_id=None):
        bid = self._new_id()
        self.blocks[bid] = {
            "opcode": "motion_movesteps",
            "next": None,
            "parent": parent_id,
            "inputs": {"STEPS": [4, [4, steps]]},
            "fields": {},
            "shadow": False,
            "topLevel": parent_id is None,
            "x": 0, "y": 0 if parent_id is None else None
        }
        return bid

    def motion_turnright(self, degrees, parent_id=None):
        bid = self._new_id()
        self.blocks[bid] = {
            "opcode": "motion_turnright",
            "next": None, "parent": parent_id,
            "inputs": {"DEGREES": [4, [4, degrees]]},
            "fields": {}, "shadow": False, "topLevel": parent_id is None,
            "x": 0, "y": 0
        }
        return bid

    def motion_turnleft(self, degrees, parent_id=None):
        bid = self._new_id()
        self.blocks[bid] = {
            "opcode": "motion_turnleft",
            "next": None, "parent": parent_id,
            "inputs": {"DEGREES": [4, [4, degrees]]},
            "fields": {}, "shadow": False, "topLevel": parent_id is None,
            "x": 0, "y": 0
        }
        return bid

    def motion_gotoxy(self, x, y, parent_id=None):
        bid = self._new_id()
        self.blocks[bid] = {
            "opcode": "motion_gotoxy",
            "next": None, "parent": parent_id,
            "inputs": {"X": [4, [4, x]], "Y": [4, [4, y]]},
            "fields": {}, "shadow": False, "topLevel": parent_id is None,
            "x": 0, "y": 0
        }
        return bid

    def motion_goto(self, target, parent_id=None):
        bid = self._new_id()
        self.blocks[bid] = {
            "opcode": "motion_goto",
            "next": None, "parent": parent_id,
            "inputs": {"TO": [1, target]},
            "fields": {}, "shadow": False, "topLevel": parent_id is None,
            "x": 0, "y": 0
        }
        return bid

    def motion_changexby(self, dx, parent_id=None):
        bid = self._new_id()
        self.blocks[bid] = {
            "opcode": "motion_changexby",
            "next": None, "parent": parent_id,
            "inputs": {"DX": [4, [4, dx]]},
            "fields": {}, "shadow": False, "topLevel": parent_id is None,
            "x": 0, "y": 0
        }
        return bid

    def motion_changeyby(self, dy, parent_id=None):
        bid = self._new_id()
        self.blocks[bid] = {
            "opcode": "motion_changeyby",
            "next": None, "parent": parent_id,
            "inputs": {"DY": [4, [4, dy]]},
            "fields": {}, "shadow": False, "topLevel": parent_id is None,
            "x": 0, "y": 0
        }
        return bid

    def motion_setx(self, x, parent_id=None):
        bid = self._new_id()
        self.blocks[bid] = {
            "opcode": "motion_setx",
            "next": None, "parent": parent_id,
            "inputs": {"X": [4, [4, x]]},
            "fields": {}, "shadow": False, "topLevel": parent_id is None,
            "x": 0, "y": 0
        }
        return bid

    def motion_sety(self, y, parent_id=None):
        bid = self._new_id()
        self.blocks[bid] = {
            "opcode": "motion_sety",
            "next": None, "parent": parent_id,
            "inputs": {"Y": [4, [4, y]]},
            "fields": {}, "shadow": False, "topLevel": parent_id is None,
            "x": 0, "y": 0
        }
        return bid

    def motion_ifonedgebounce(self, parent_id=None):
        bid = self._new_id()
        self.blocks[bid] = {
            "opcode": "motion_ifonedgebounce",
            "next": None, "parent": parent_id,
            "inputs": {}, "fields": {}, "shadow": False,
            "topLevel": parent_id is None, "x": 0, "y": 0
        }
        return bid

    def looks_say(self, message, parent_id=None):
        bid = self._new_id()
        self.blocks[bid] = {
            "opcode": "looks_say",
            "next": None, "parent": parent_id,
            "inputs": {"MESSAGE": [1, message]},
            "fields": {}, "shadow": False, "topLevel": parent_id is None,
            "x": 0, "y": 0
        }
        return bid

    def looks_show(self, parent_id=None):
        bid = self._new_id()
        self.blocks[bid] = {
            "opcode": "looks_show",
            "next": None, "parent": parent_id,
            "inputs": {}, "fields": {}, "shadow": False,
            "topLevel": parent_id is None, "x": 0, "y": 0
        }
        return bid

    def looks_hide(self, parent_id=None):
        bid = self._new_id()
        self.blocks[bid] = {
            "opcode": "looks_hide",
            "next": None, "parent": parent_id,
            "inputs": {}, "fields": {}, "shadow": False,
            "topLevel": parent_id is None, "x": 0, "y": 0
        }
        return bid

    def looks_switchcostumeto(self, costume, parent_id=None):
        bid = self._new_id()
        self.blocks[bid] = {
            "opcode": "looks_switchcostumeto",
            "next": None, "parent": parent_id,
            "inputs": {"COSTUME": [1, costume]},
            "fields": {}, "shadow": False, "topLevel": parent_id is None,
            "x": 0, "y": 0
        }
        return bid

    def looks_setsizeto(self, size, parent_id=None):
        bid = self._new_id()
        self.blocks[bid] = {
            "opcode": "looks_setsizeto",
            "next": None, "parent": parent_id,
            "inputs": {"SIZE": [4, [4, size]]},
            "fields": {}, "shadow": False, "topLevel": parent_id is None,
            "x": 0, "y": 0
        }
        return bid

    def looks_changesizeby(self, change, parent_id=None):
        bid = self._new_id()
        self.blocks[bid] = {
            "opcode": "looks_changesizeby",
            "next": None, "parent": parent_id,
            "inputs": {"CHANGE": [4, [4, change]]},
            "fields": {}, "shadow": False, "topLevel": parent_id is None,
            "x": 0, "y": 0
        }
        return bid

    def event_whenflagclicked(self):
        bid = self._new_id()
        self.blocks[bid] = {
            "opcode": "event_whenflagclicked",
            "next": None, "parent": None,
            "inputs": {}, "fields": {}, "shadow": False,
            "topLevel": True, "x": 0, "y": 0
        }
        return bid

    def event_whenkeypressed(self, key, parent_id=None):
        bid = self._new_id()
        self.blocks[bid] = {
            "opcode": "event_whenkeypressed",
            "next": None, "parent": parent_id,
            "inputs": {"KEY_OPTION": [1, key]},
            "fields": {}, "shadow": False, "topLevel": parent_id is None,
            "x": 0, "y": 0
        }
        return bid

    def event_broadcast(self, message, parent_id=None):
        bid = self._new_id()
        self.blocks[bid] = {
            "opcode": "event_broadcast",
            "next": None, "parent": parent_id,
            "inputs": {"BROADCAST_INPUT": [1, message]},
            "fields": {}, "shadow": False, "topLevel": parent_id is None,
            "x": 0, "y": 0
        }
        return bid

    def control_wait(self, secs, parent_id=None):
        bid = self._new_id()
        self.blocks[bid] = {
            "opcode": "control_wait",
            "next": None, "parent": parent_id,
            "inputs": {"DURATION": [4, [4, secs]]},
            "fields": {}, "shadow": False, "topLevel": parent_id is None,
            "x": 0, "y": 0
        }
        return bid

    def control_repeat(self, times, substack_id=None, parent_id=None):
        bid = self._new_id()
        self.blocks[bid] = {
            "opcode": "control_repeat",
            "next": None, "parent": parent_id,
            "inputs": {"TIMES": [4, [4, times]], "SUBSTACK": [2, substack_id] if substack_id else [2, []]},
            "fields": {}, "shadow": False, "topLevel": parent_id is None,
            "x": 0, "y": 0
        }
        return bid

    def control_forever(self, substack_id=None, parent_id=None):
        bid = self._new_id()
        self.blocks[bid] = {
            "opcode": "control_forever",
            "next": None, "parent": parent_id,
            "inputs": {"SUBSTACK": [2, substack_id] if substack_id else [2, []]},
            "fields": {}, "shadow": False, "topLevel": parent_id is None,
            "x": 0, "y": 0
        }
        return bid

    def control_if(self, condition, substack_id=None, parent_id=None):
        bid = self._new_id()
        self.blocks[bid] = {
            "opcode": "control_if",
            "next": None, "parent": parent_id,
            "inputs": {
                "CONDITION": [1, condition],
                "SUBSTACK": [2, substack_id] if substack_id else [2, []]
            },
            "fields": {}, "shadow": False, "topLevel": parent_id is None,
            "x": 0, "y": 0
        }
        return bid

    def control_wait_until(self, condition, parent_id=None):
        bid = self._new_id()
        self.blocks[bid] = {
            "opcode": "control_wait_until",
            "next": None, "parent": parent_id,
            "inputs": {"CONDITION": [1, condition]},
            "fields": {}, "shadow": False, "topLevel": parent_id is None,
            "x": 0, "y": 0
        }
        return bid

    def sensing_touchingobject(self, target, parent_id=None):
        bid = self._new_id()
        self.blocks[bid] = {
            "opcode": "sensing_touchingobject",
            "next": None, "parent": parent_id,
            "inputs": {"TOUCHINGOBJECTMENU": [1, target]},
            "fields": {}, "shadow": False, "topLevel": parent_id is None,
            "x": 0, "y": 0
        }
        return bid

    def operator_add(self, num1, num2, parent_id=None):
        bid = self._new_id()
        self.blocks[bid] = {
            "opcode": "operator_add",
            "next": None, "parent": parent_id,
            "inputs": {"NUM1": [4, [4, num1]], "NUM2": [4, [4, num2]]},
            "fields": {}, "shadow": False, "topLevel": parent_id is None,
            "x": 0, "y": 0
        }
        return bid

    def operator_subtract(self, num1, num2, parent_id=None):
        bid = self._new_id()
        self.blocks[bid] = {
            "opcode": "operator_subtract",
            "next": None, "parent": parent_id,
            "inputs": {"NUM1": [4, [4, num1]], "NUM2": [4, [4, num2]]},
            "fields": {}, "shadow": False, "topLevel": parent_id is None,
            "x": 0, "y": 0
        }
        return bid

    def operator_random(self, from_val, to_val, parent_id=None):
        bid = self._new_id()
        self.blocks[bid] = {
            "opcode": "operator_random",
            "next": None, "parent": parent_id,
            "inputs": {"FROM": [4, [4, from_val]], "TO": [4, [4, to_val]]},
            "fields": {}, "shadow": False, "topLevel": parent_id is None,
            "x": 0, "y": 0
        }
        return bid

    def data_setvariableto(self, var_name, value, parent_id=None):
        bid = self._new_id()
        self.blocks[bid] = {
            "opcode": "data_setvariableto",
            "next": None, "parent": parent_id,
            "inputs": {"VALUE": [4, [4, value]]},
            "fields": {"VARIABLE": [10, var_name]},
            "shadow": False, "topLevel": parent_id is None,
            "x": 0, "y": 0
        }
        return bid

    def data_changevariableby(self, var_name, value, parent_id=None):
        bid = self._new_id()
        self.blocks[bid] = {
            "opcode": "data_changevariableby",
            "next": None, "parent": parent_id,
            "inputs": {"VALUE": [4, [4, value]]},
            "fields": {"VARIABLE": [10, var_name]},
            "shadow": False, "topLevel": parent_id is None,
            "x": 0, "y": 0
        }
        return bid

    def twsettings_setFramerate(self, fps, parent_id=None):
        bid = self._new_id()
        self.blocks[bid] = {
            "opcode": "twsettings_setFramerate",
            "next": None, "parent": parent_id,
            "inputs": {"FPS": [4, [4, fps]]},
            "fields": {}, "shadow": False, "topLevel": parent_id is None,
            "x": 0, "y": 0
        }
        return bid

    def twsettings_setInterpolation(self, mode, parent_id=None):
        bid = self._new_id()
        self.blocks[bid] = {
            "opcode": "twsettings_setInterpolation",
            "next": None, "parent": parent_id,
            "inputs": {"MODE": [1, mode]},
            "fields": {}, "shadow": False, "topLevel": parent_id is None,
            "x": 0, "y": 0
        }
        return bid

    def twsettings_setStageSize(self, size, parent_id=None):
        bid = self._new_id()
        self.blocks[bid] = {
            "opcode": "twsettings_setStageSize",
            "next": None, "parent": parent_id,
            "inputs": {"SIZE": [1, size]},
            "fields": {}, "shadow": False, "topLevel": parent_id is None,
            "x": 0, "y": 0
        }
        return bid

    def twsettings_setHighQualityPen(self, mode, parent_id=None):
        bid = self._new_id()
        self.blocks[bid] = {
            "opcode": "twsettings_setHighQualityPen",
            "next": None, "parent": parent_id,
            "inputs": {"MODE": [1, mode]},
            "fields": {}, "shadow": False, "topLevel": parent_id is None,
            "x": 0, "y": 0
        }
        return bid

    def twsettings_setCloneLimit(self, limit, parent_id=None):
        bid = self._new_id()
        self.blocks[bid] = {
            "opcode": "twsettings_setCloneLimit",
            "next": None, "parent": parent_id,
            "inputs": {"LIMIT": [4, [4, limit]]},
            "fields": {}, "shadow": False, "topLevel": parent_id is None,
            "x": 0, "y": 0
        }
        return bid

    def twsettings_toggleTurboMode(self, parent_id=None):
        bid = self._new_id()
        self.blocks[bid] = {
            "opcode": "twsettings_toggleTurboMode",
            "next": None, "parent": parent_id,
            "inputs": {}, "fields": {}, "shadow": False,
            "topLevel": parent_id is None, "x": 0, "y": 0
        }
        return bid

    def twsettings_setDragMode(self, mode, parent_id=None):
        bid = self._new_id()
        self.blocks[bid] = {
            "opcode": "twsettings_setDragMode",
            "next": None, "parent": parent_id,
            "inputs": {"MODE": [1, mode]},
            "fields": {}, "shadow": False, "topLevel": parent_id is None,
            "x": 0, "y": 0
        }
        return bid

    def link_blocks(self, from_id, to_id):
        if from_id in self.blocks:
            self.blocks[from_id]["next"] = to_id
        if to_id in self.blocks:
            self.blocks[to_id]["parent"] = from_id

    def get_blocks(self):
        return self.blocks
