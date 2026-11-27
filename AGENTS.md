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
  belong to **Biquaternion Universe Free of Force**; Relativity may point there by name.
- Operator identities (gradient, d'Alembertian, Clifford root, Maxwell's Bianchi identity) are not
  free particle equations and may stay.
- The four-wavevector `\tilde\Upsilon_\Phi = i\omega/c\,e_t + 2\pi\vec\nu_\Phi` is kinematic and
  stays; `\nu_m` (mass wave number) does not.

## Verification

After edits inside a block, audit the rendered HTML, not only the sources: grep the deploy tree for
the banned patterns over the block's article list, and rebuild before reporting.
