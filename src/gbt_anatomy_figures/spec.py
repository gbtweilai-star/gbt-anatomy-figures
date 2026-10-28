"""The capability contract, copied verbatim from the GBT V8 registry.

Do not hand-edit: ``tests/test_spec.py`` pins every field against the
registry snapshot so drift fails the build instead of shipping quietly.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Any, Dict, List, Tuple

_RAW = r"""{
 "name": "anatomy_figures",
 "domain": "creation",
 "desc": "Anatomy 等轴详解图（外部成熟件 · 主人 2026-10-19 指名抓取「这两个能力不就可以完美补齐缺失了吗」 · 上游 wheresryan22/anatomy · MIT · 15.9k★）：**把一个概念做成一台真机器**的等轴 SVG 图（零件级 40~150 件 · 四色明暗 · 画家排序 · 卡框带活读数）+ 可交互 HTML（悬停/键盘/巡览/WebGL 火水光焦散同一等轴相机）+ 会转的 3D 图（turn*.mjs 逐帧重投影 + 轨道审计）+ A4/Letter 三种版式 PDF（poster/drawing/detailed）。**几何自证** `--audit`（互不穿插/终端落在实处/无折/深度序）+ **线端自证** `lines.mjs`（line ends: 0）。本机依赖只三个：node≥20.10（现读 v24.15）、Chrome（标准位在）、无 npm 依赖无 postinstall；**零付费接口、零出网**（上游 publish.mjs 提 PR 那条不接）。op=status/examples/docs/where（纯读）· build/verify（写盘+起 node ⇒ filesystem_write 门在处理器层）。生成新图：模型按 SKILL.md+references/craft.md 写 examples/<名>/build.mjs → build → verify",
 "handler": "anatomy_figures",
 "safe": false,
 "external": false,
 "requires_params": false,
 "params": [],
 "params_hint": "",
 "multi_op": true,
 "ops": [
  "poster",
  "drawing",
  "detailed"
 ],
 "ops_hint": ""
}"""


@dataclass(frozen=True)
class CapSpec:
    """Immutable description of one capability bit."""

    name: str
    domain: str
    desc: str
    handler: str
    safe: bool
    external: bool
    requires_params: bool
    params: Tuple[str, ...] = ()
    params_hint: str = ""
    multi_op: bool = False
    ops: Tuple[str, ...] = ()
    ops_hint: str = ""

    @property
    def gated(self) -> bool:
        """True when the registry marks this bit ``safe: false``.

        Gated does not mean "dangerous"; it means the action can change state
        that cannot be restored by running the inverse action.
        """
        return not self.safe

    @property
    def summary(self) -> str:
        """First clause of the description, for one-line listings."""
        for sep in ("\uff08", "\uff1b", "\u3002", ";"):
            if sep in self.desc:
                head = self.desc.split(sep, 1)[0].strip()
                if head:
                    return head
        return self.desc.strip()

    def as_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "domain": self.domain,
            "desc": self.desc,
            "handler": self.handler,
            "safe": self.safe,
            "gated": self.gated,
            "external": self.external,
            "requires_params": self.requires_params,
            "params": list(self.params),
            "params_hint": self.params_hint,
            "multi_op": self.multi_op,
            "ops": list(self.ops),
            "ops_hint": self.ops_hint,
        }


_data = json.loads(_RAW)

SPEC = CapSpec(
    name=_data["name"],
    domain=_data["domain"],
    desc=_data["desc"],
    handler=_data["handler"],
    safe=_data["safe"],
    external=_data["external"],
    requires_params=_data["requires_params"],
    params=tuple(_data["params"]),
    params_hint=_data["params_hint"],
    multi_op=_data["multi_op"],
    ops=tuple(_data["ops"]),
    ops_hint=_data["ops_hint"],
)
