#!/usr/bin/env python
# deoplete-openscad
# Copyright (c) 2019  Michael Sasser <Michael@MichaelSasser.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import re

from .base import Base
from deoplete.util import load_external_module

__author__: str = "Michael Sasser"
__email__: str = "Michael@MichaelSasser.org"


load_external_module(__file__, "sources/openscad")


class Source(Base):
    def __init__(self, vim):
        super().__init__(vim)

        self.filetypes = ["openscad"]
        self.mark = "[openscad]"
        self.name = "openscad"
        self.events = ["InsertEnter"]
        self.sorters = ["sorter_len"]
        self.max_candidates = 25
        self.min_pattern_length = 1
        # self.match_pattern = re.compile(r"[A-Z$][^:\s\@\[\]\{\}\(\)\/\*\+\&\%\-]*$")
        self.match_pattern = re.compile(r"[a-zA-Z0-9_]*$")

    def gather_candidates(self, context):
        return OPENSCAD_KEYWORDS

    def get_complete_position(self, context):
        match = self.match_pattern.search(context["input"])
        # match = re.search("[a-zA-Z0-9_]*$", context["input"])
        return match.start() if match is not None else -1


OPENSCAD_KEYWORDS = [
    "module",
    "function",
    "include",
    "use",
    "undef",
    "PI",
    "$fa",
    "$fs",
    "$fn",
    "$t",
    "$vpr",
    "$vpt",
    "$vpd",
    "$children",
    "$preview",
    "*",
    "!",
    "#",
    "%",
    "circle",
    "square",
    "square",
    "polygon",
    "polygon",
    "text",
    "import",
    "projection",
    "sphere",
    "cube",
    "cube",
    "cylinder",
    "cylinder",
    "polyhedron",
    "import",
    "linear_extrude",
    "rotate_extrude",
    "surface",
    "translate",
    "rotate",
    "rotate",
    "scale",
    "resize",
    "mirror",
    "multmatrix",
    "color",
    "color",
    "color",
    "offset",
    "hull",
    "minkowski",
    "union",
    "difference",
    "intersection",
    "Generate",
    "Generate",
    "Flatten",
    "Conditions",
    "Conditions",
    "Assignments",
    "for",
    "intersection_for",
    "if",
    "let",
    "is_undef",
    "is_bool",
    "is_num",
    "is_string",
    "is_list",
    "echo",
    "render",
    "children",
    "assert",
    "assign",
    "concat",
    "lookup",
    "str",
    "chr",
    "ord",
    "search",
    "version",
    "version_num",
    "parent_module",
    "abs",
    "sign",
    "sin",
    "cos",
    "tan",
    "acos",
    "asin",
    "atan",
    "atan2",
    "floor",
    "round",
    "ceil",
    "ln",
    "len",
    "let",
    "log",
    "pow",
    "sqrt",
    "exp",
    "rands",
    "min",
    "max",
    "norm",
    "cross",
]

# vim: set ft=python :
