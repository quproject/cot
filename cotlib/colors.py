# -*- coding: utf-8 -*-

"""
The Color class handles the colors objects
used in the application.
"""

from dataclasses import dataclass
import re

from typing import Union, Optional, Any

class Color:
    def __init__(self, color: str):
        self.color = Components.get_color_datas(color, ColorDatas())

@dataclass
class ColorDatas:
    """All usefull informations about the color"""
    color_name: Union[str, None] = None,
    color_string: Union[str, None] = None,
    color_format: Union[str, None] = None,
    components: Union[dict[str, str], None] = None

class Components:
    color_formats: dict[str, str] = {
        "named": re.compile("^(?P<name>[a-zA-Z0-9 ]+)$"),
        "rgb": re.compile(r"rgb\((?P<red>[0-9]{1,3}), ?(?P<green>[0-9]{1,3}), ?(?P<blue>[0-9]{1,3})\)"),
        "rgba": re.compile(r"rgba\((?P<red>[0-9]{1,3}), ?(?P<green>[0-9]{1,3}), ?(?P<blue>[0-9]{1,3}), ?(?P<alpha>[0-1]?\.?[0-9]*)\)"),
        "hex": re.compile("#(?P<red>[a-fA-F0-9]{2})(?P<green>[a-fA-F0-9]{2})(?P<blue>[a-fA-F0-9]{2})"),
        "hsl": re.compile(r"hsl\((?P<hue>[0-9]{1,3}), ?(?P<saturation>[0-9]{1,3})%, ?(?P<light>[0-9]{1,3})%\)"),
        "hsla": re.compile(r"hsla\((?P<hue>[0-9]{1,3}), ?(?P<saturation>[0-9]{1,3})%, ?(?P<light>[0-9]{1,3})%, ?(?P<alpha>0|1\.[0-9])\)"),
        "lch": re.compile(r"lch\((?P<light>[0-9]{1,3}\.?[0-9]*)% (?P<chroma>[0-9]+\.?[0-9]*) (?P<hue>[0-9]+\.?[0-9]*)\)"),
        "lcha": re.compile(r"lch\((?P<light>[0-9]{1,3}\.?[0-9]*)% (?P<chroma>[0-9]+\.?[0-9]*) (?P<hue>[0-9]+\.?[0-9]*)\) / (?P<alpha>[0-9]+\.?[0-9]*)"),
        "lab": re.compile(r"lab\((?P<light>[0-9]{1,3}\.?[0-9]*)% (?P<aaxis>[0-9]+\.?[0-9]*) (?P<baxis>[0-9]+\.?[0-9]*)\)"),
        "laba": re.compile(r"lab\((?P<light>[0-9]{1,3}\.?[0-9]*)% (?P<aaxis>[0-9]+\.?[0-9]*) (?P<baxis>[0-9]+\.?[0-9]*) / (?P<alpha>[0-9]+\.?[0-9]*)\)"),
        "display-p3": re.compile(r"color\(display\-p3 (?P<val1>0|1\.?[0-9]*) (?P<val2>0|1\.?[0-9]*) (?P<val3>0|1\.?[0-9]*)\)"),
        "display-p3a": re.compile(r"color\(display\-p3 (?P<val1>0|1\.?[0-9]*) (?P<val2>0|1\.?[0-9]*) (?P<val3>0|1\.?[0-9]*) / (?P<alpha>[0-9]+\.?[0-9]*)\)")
    }

    def __init__(self, color_string: str, color_datas: ColorDatas):
        self.color_datas = color_datas
        self.color_datas.color_string = color_string
        #self.get_color_component()

    @classmethod
    def get_color_datas(cls, color_string, color_datas) -> Union[str, bool]:
        #color_datas = ColorDatas()

        for key, val in cls.color_formats.items():
            if _m := val.match(color_string):
                color_datas.color_format = key

                if key == "named":
                    color_datas.color_name = _m.group("name")
                    # Todo: read datas/colors.json → find name + color datas
                    break

                grpn = _m.groupdict()
                color_datas.components = {}
                for k, v in grpn.items():
                    color_datas.components[k] = v

        return cls(color_string, color_datas)
