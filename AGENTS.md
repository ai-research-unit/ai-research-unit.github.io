# Repository memory

Physics site *Biquaternion Universe*. Sources in `articles_*/*.md`, site menu in `physics.md`,
rendered output in `../ai-research-unit-deploy/`.

## Build

- `python3 build.py` — full sweep (≈90 s, ~3559 pages, EXIT=0).
- `python3 build_diff.py` — incremental, use after small edits.
- Build scripts carry a read-only warning: do not edit them without explicit approval.

## Block invariants

- **Relativity is kinematics only.** No Planck constant or its shadows (`\hbar`, `\frac{h}{2\pi}`,
  `\nu_m`, `2\pi m`, `4\pi^2m^2`, `mc/h`), no named free equations (Klein–Gordon, Dirac, Proca,
  Schrödinger), no mass-term displays. Free equations, Lagrangians, fluids and thermodynamics
  belong to **Biquaternion Universe Force-Free**; Relativity may point there by name.
- Operator identities (gradient, d'Alembertian, Clifford root, Maxwell's Bianchi identity) are not
  free particle equations and may stay.
- The four-wavevector `\tilde\Upsilon_\Phi = i\omega/c\,e_t + 2\pi\vec\nu_\Phi` is kinematic and
  stays; `\nu_m` (mass wave number) does not.

## Verification

After edits inside a block, audit the rendered HTML, not only the sources: grep the deploy tree for
the banned patterns over the block's article list, and rebuild before reporting.

## The reading order of the constants

The categories are read downwards and each one may use only what precedes it:

1. *Relativity* — kinematics, no constant of the quantum.
2. *Action* — integrand, Lagrangian, Helmholtz conditions, variation, currents, connection.
   **No action quantum and no `h` here.** The action quantum enters once, in
   *From the Field Equation to the Quantum Field* (the promotion of the bracket), and nowhere earlier.
3. *Fluid Physics and Thermodynamics* — assumes the quantisation; a thermal state is not
   definable without it.
4. Particular categories: *Force-Free* first, then *Primordial Force*, then the forces.

Consequence for the gauge articles of the Action block: the covariant derivative carries one
coupling, `\kappa`, and every `\frac{2\pi i\varkappa}{h}` there is written `i\kappa`. The bridge
`\kappa = 2\pi\varkappa/h` is stated once, in *The Lagrangian and the Second Quantisation*.
The standing exception is the reference apparatus in *Biquaternion Universe* (Conventions &
Notations), which defines units and therefore names the constant; it is a lookup block, not the
reading path.

## Auditing the constants

Do not grep for the constant and do not trust a remembered count. The measurement is a script:

```
python3 _reserve/py/audit-h-presence.py            # per category, in menu order
python3 _reserve/py/audit-h-presence.py --fine     # every site with its line
python3 _reserve/py/audit-h-presence.py --rendered # the deployed HTML
```

Green is `Relativity 93 0 0`, `Action before the promotion: 22 articles, 0 sites`, and
`first article in reading order with a site: ai-physics-review`. The reports are
`articles_internal/audits/audit-h-presence.md` — the three claims, their verdicts, and the
article-by-article inventory in §8; it is internal and never committed.

Two traps the script exists to carry. The letter `h` is overloaded: helicity, the vector part of a
state, the Cartan subalgebra, a finite-difference step, `\tanh`/`\cosh`/`\sinh`. And the constant
can be written `h c` with a space, which no `{h}` grep will ever see.

## Auditing the carrier roster

`articles_internal/audits/audit-lagrangian-existence.md` lists one line per spin per category.
Two traps it exists to carry, both found by outside review:

- **A "no" line is a statement about the roster, never about field theory.** The roster is the
  algebra's three carriers (dim $1,2,3$), so a colour-triplet scalar, the Rarita–Schwinger field
  of spin $3/2$, and the Fronsdal/Vasiliev higher-spin fields are ordinary fields with functionals
  of their own and simply are not carriers here. Never write "no irreducible carrier to write on".
- **The corpus's own verdict on spin $3/2$ is narrower than "impossible".** It has the
  Rarita–Schwinger *equation* and not the *action*
  (`articles_internal/archives/the-lagrangian-and-the-rarita-schwinger-equation.md`): the missing
  object is an algebra element that contracts the vector index with the chiral structure, which is
  what the two multipliers need. The field is imported as $S\otimes V=4\oplus2$ with its constraint.

Two physics traps in the same ledger: a $\mathrm{U}(1)$ mass term is gauge invariant, so the
electron mass is allowed in QED (the *electroweak* line is where the scalar is required), and a
massless chiral half is a legitimate charged field — the mass is what pairs the halves. Gauge
bosons have no *explicit* mass term; a generated mass is not the same statement.

The audit's first ledger column is the **gauged group** — the group whose connection the row's
density carries, never the carrier (spin is the next column). The four force groups are the
corpus's own: $\mathrm{SU}(4)$ (15, rank 3), $\mathrm{SU}(3)=\mathrm{Stab}_{\mathrm{SU}(4)}(\mathbb{C}e_t)$
(8, 2), $\mathrm{SU}(2)_L\times\mathrm{U}(1)_Y$ (4, 2) and $\mathrm{SU}(1)=\{e\}$ (0, 0). Note the
electroweak subtlety the ledger must keep: the Standard Model's group is the *product*, while the
algebra's compact group is $\mathrm{U}(2)=(\mathrm{SU}(2)\times\mathrm{U}(1))/\mathbb{Z}_2$ — same
algebra and dimension, different group.
