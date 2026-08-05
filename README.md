## Formal Verification of Computational Origami

A Lean formalization of Huzita's origami axioms, plus a web UI to stack
axiom calls visually and compile the resulting construction with Lean. See
`project description.txt` for the full pipeline specification.

### Structure
- Origami/     : Lean formalization (Huzita axioms in `Origami/lightweight_definitions`)
- origami_api.py    : stacks Huzita axiom calls and generates the Lean construction
- origami_server.py : routes the web UI to the Python API and to `lake env lean`
- origami-sim/ : Web UI (crease pattern viewer as the picking surface) + Rust/WASM core

### How to run and use
You need a Rust toolchain installed (cargo + rustc).
First run can take a while because it downloads Mathlib and compiles Rust/WASM.

Clone with submodules, then run the helper script from the repo root:

```bash
git clone --recurse-submodules git@github.com:celioboulay/origami-formalization.git
cd origami-formalization
chmod +x run-origami.sh
./run-origami.sh
```

Open `http://localhost:8000/`, then:
1) (Optional) Upload a `.fold` file as the paper — a unit square loads by default.
2) In the **Huzita Axioms** panel, pick an axiom (A1–A7), then click `Pick` for
   each required point/line and click it on the canvas.
3) Click `Add to stack` — the call is validated, sent to the Python API, and
   appended to the **Construction Stack**.
4) Repeat to stack more axiom calls; picked entities are reused when you click
   the same point/crease again, so later axioms can build on earlier folds.
5) Click `Build Lean sequence` to write the generated Lean file and compile it
   with `lake env lean`; the result is reported back in the panel.
