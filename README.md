# anatomy_figures

**One capability bit from GBT V8, packaged standalone.** No. 8 of 341,
`creation` domain (Creation).

<p>
<img alt="python" src="https://img.shields.io/badge/python-3.9%2B-blue">
<img alt="license" src="https://img.shields.io/badge/license-MIT-green">
<img alt="deps" src="https://img.shields.io/badge/runtime%20dependencies-0-brightgreen">
</p>

> Anatomy 等轴详解图（外部成熟件 · 主人 2026-10-19 指名抓取「这两个能力不就可以完美补齐缺失了吗」 · 上游 wheresryan22/anatomy · MIT · 15.9k★）：**把一个概念做成一台真机器**的等轴 SVG 图（零件级 40~150 件 · 四色明暗 · 画家排序 · 卡框带活读数）+ 可交互 HTML（悬停/键盘/巡览/WebGL 火水光焦散同一等轴相机）+ 会转的 3D 图（turn*.mjs 逐帧重投影 + 轨道审计）+ A4/Letter 三种版式 PDF（poster/drawing/detailed）。**几何自证** `--audit`（互不穿插/终端落在实处/无折/深度序）+ **线端自证** `lines.mjs`（line ends: 0）。本机依赖只三个：node≥20.10（现读 v24.15）、Chrome（标准位在）、无 npm 依赖无 postinstall；**零付费接口、零出网**（上游 publish.mjs 提 PR 那条不接）。op=status/examples/docs/where（纯读）· build/verify（写盘+起 node ⇒ filesystem_write 门在处理器层）。生成新图：模型按 SKILL.md+references/craft.md 写 examples/<名>/build.mjs → build → verify

That description is copied verbatim from the registry. `tests/test_spec.py` pins it,
so documentation drift fails the build instead of shipping quietly.

## What this package actually is

It is the **contract** for one capability: its name, its parameters, the values it
accepts, and whether it can change state that cannot be restored. It is not the
implementation — that lives in the runtime this bit was extracted from.

So `run()` goes through a narrow `Backend` protocol, and the default backend is a
stub that **says so**:

```
status="validated"   backend="stub"   data={"executed": false}
```

Never `status="ok"`. A stub that reports success is worse than no stub, because the
caller stops looking for the real thing.

## Install

```bash
git clone https://github.com/gbtweilai-star/gbt-anatomy-figures.git
cd gbt-anatomy-figures
python -m pip install -e ".[dev]"
```

## Use

```bash
python -m gbt_anatomy_figures info                  # capability card
python -m gbt_anatomy_figures spec --json           # machine-readable contract
python -m gbt_anatomy_figures check --payload '{}'
python -m gbt_anatomy_figures run   --payload '{}'
```

Real `info` output from this machine:

```text
anatomy_figures  (creation)  v1.0.0
----------------------------------------
Anatomy 等轴详解图（外部成熟件 · 主人 2026-10-19 指名抓取「这两个能力不就可以完美补齐缺失了吗」 · 上游 wheresryan22/anatomy · MIT · 15.9k★）：**把一个概念做成一台真机器**的等轴 SVG 图（零件级 40~150 件 · 四色明暗 · 画家排序 · 卡框带活读数）+ 可交互 HTML（悬停/键盘/巡览/WebGL 火水光焦散同一等轴相机）+ 会转的 3D 图（turn*.mjs 逐帧重投影 + 轨道审计）+ A4/Letter 三种版式 PDF（poster/drawing/detailed）。**几何自证** `--audit`（互不穿插/终端落在实处/无折/深度序）+ **线端自证** `lines.mjs`（line ends: 0）。本机依赖只三个：node≥20.10（现读 v24.15）、Chrome（标准位在）、无 npm 依赖无 postinstall；**零付费接口、零出网**（上游 publish.mjs 提 PR 那条不接）。op=status/examples/docs/where（纯读）· build/verify（写盘+起 node ⇒ filesystem_write 门在处理器层）。生成新图：模型按 SKILL.md+references/craft.md 写 examples/<名>/build.mjs → build → verify

gated      : True   <- needs explicit consent
external   : False
multi-op   : True
params     : (none)
values     : poster, drawing, detailed
```

Wire a real implementation:

```python
from gbt_anatomy_figures import run

class MyBackend:
    name = "my-backend"
    def invoke(self, cap, payload):
        return {"cap": cap, "handled": sorted(payload)}

result = run({}, backend=MyBackend())
assert result.status == "ok"
```

## Parameters

| name | required | notes |
|---|---|---|
| — | no | the registry declares no required parameters |

Registry hint (`params_hint`): (empty)

**注册表登记的取值 / 子动作（3 个）**：`poster`、`drawing`、`detailed`

Types are deliberately absent: the registry does not declare them, and an invented
type is worse than no type, because callers believe it.

## Boundaries

- Gated: this bit is marked `safe: false` in the registry — it can change state that no inverse action restores.
- No external service dependency declared.
- Multi-op (`multi_op: true`): several sub-actions share one name — read `op` before calling.
- No implementation ships here. Bring a backend; the protocol is one method.

## What this is not

Not a wrapper around a hosted API. Not a model. Not a promise that calling it does
anything on its own. It is the typed seam plus the validation, which is the part that
stays correct even when the implementation changes.

## Tests

```bash
python -m pytest
```

```text
20 passed, 3 skipped in 0.16s
```

## Provenance

| field | value |
|---|---|
| capability | `anatomy_figures` |
| domain | `creation` |
| handler | `anatomy_figures` |
| safe | `False` (gated = `True`) |
| external | `False` |
| atlas page | [creation/anatomy_figures](https://github.com/gbtweilai-star/gbt-caps/blob/main/caps/creation/anatomy_figures.md) |
| full index | [https://github.com/gbtweilai-star/gbt-caps](https://github.com/gbtweilai-star/gbt-caps) |

The parent README says 348 capabilities; an AST pass over the registry enumerates
`341 + 0 unimplemented + 0 disabled = 341`. The extra 7 are historical duplicates.
Numbering here follows 341 and matches the `gbt-caps` index one-to-one.

## License

MIT.
