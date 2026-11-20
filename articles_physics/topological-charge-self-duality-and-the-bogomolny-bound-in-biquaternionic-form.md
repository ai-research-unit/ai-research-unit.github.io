# __Topological Charge, Self-Duality and the Bogomolny Bound in Biquaternionic Form__

## Introduction

**The object.** A field configuration can be classified by an integer that no continuous deformation changes. For a gauge field the integer is the integral of a density built from the field strength, and it is fixed by the behaviour of the field at infinity rather than by its shape. Configurations with nonzero charge are **instantons** in the Euclidean theory; the same charge in the Lorentzian theory would be carried by solitons, and the two cases differ in what makes a configuration stable.

**What this article is.** The general theory, with no sector attached: the density, its primitivity, the self-duality condition, the bound that self-dual configurations saturate, and the reason the framework's own invariants supply the abelian density and not the non-abelian one. It is used by the strong sector, where the objects are the non-perturbative configurations of the colour gauge theory.

**Where the applications are.**

- The strong sector. The application is [Instantons and Solitons in Biquaternionic Form](instantons-and-solitons-in-biquaternionic-form.html), which exhibits the BPST solution inside the framework's compact factor and states what the framework's invariants can and cannot supply.
- The electroweak sector, nowhere. The weak sector's non-perturbative configurations belong to the same topology but are not what that sector's articles treat.

## The Density and Its Primitivity

**The density.** For a gauge field with field strength $F_{\mu\nu}$,

$$
\varrho=\frac{1}{16\pi^2}\,\mathrm{Tr}\left(F_{\mu\nu}\tilde F_{\mu\nu}\right),
\qquad
\tilde F_{\mu\nu}=\tfrac12\epsilon_{\mu\nu\rho\sigma}F_{\rho\sigma},
$$

and the charge is its integral, $Q=\int d^4x\ \varrho$.

**The primitivity.** The density is a total derivative,

$$
\boxed{\;\mathrm{Tr}\left(F\wedge F\right)=d\,\Omega_{\mathrm{CS}}\;}
$$

with $\Omega_{\mathrm{CS}}$ the Chern–Simons form. The identity is what makes the charge topological: the integral depends only on the boundary, so it is invariant under any deformation that does not cross the boundary, and it is an integer when the field is defined on a closed manifold. A density that were not a total derivative would give a charge that varies continuously, and there would be no sectors to sum over.

**The abelian case.** For an abelian field the density reduces to the divergence of a four-vector,

$$
\varrho=\partial_\mu J_{\mathrm{CS},\mu},
\qquad
J_{\mathrm{CS},\mu}=\tfrac14\epsilon_{\mu\nu\rho\sigma}A_\nu F_{\rho\sigma},
$$

and $J_{\mathrm{CS}}$ is gauge dependent while $\varrho$ is not. The primitive is therefore a computational device, not an invariant, and this distinction matters when the question is whether the framework can write the density at all.

**The abelian charge vanishes.** On $\mathbb R^4$ with finite action the boundary term vanishes, so there is no abelian instanton. Instantons are intrinsically non-abelian.

## Self-Duality and the Bound

**The star.** On two-forms the Hodge star satisfies $\star^2=-1$ in Lorentzian signature and $\star^2=+1$ in Euclidean. Consequently $F=\star F$ forces $F=0$ on real Lorentzian fields, and the self-duality condition is a Euclidean condition. This is the single reason instantons are defined on the Euclidean continuation and not on spacetime.

**The bound.** Writing the action as a square plus a topological term,

$$
S=\frac{1}{2g^2}\int\mathrm{Tr}\left(F\pm\star F\right)^2+\frac{8\pi^2}{g^2}|Q|,
$$

gives

$$
\boxed{\;S\ \ge\ \frac{8\pi^2}{g^2}\,|Q|\;}
$$

with equality exactly when $F=\pm\star F$. The self-dual configurations are therefore the minima of the action in each topological sector, and the second-order equation of motion follows from the first-order self-duality condition rather than the other way round.

**What the bound buys.** Existence can be shown by solving a first-order equation; stability in a fixed sector needs no potential; and the value of the action is fixed by the charge and the coupling alone. The bound is the reason instantons control the semiclassical expansion.

## What the Framework Supplies

- **Supplied.** Two invariants of the abelian field, $I_1=\vec E^2-c^2\vec B^2$ and $I_2=\vec E\cdot\vec B$, and the identity $\sum_{\mu,\nu}F_{\mu\nu}\star F_{\mu\nu}=4I_2$ in the Euclidean case, so the imaginary part of the biquaternion norm **is** the abelian density.
- **Not supplied.** The non-abelian density. $\mathrm{Tr}(F\wedge F)$ needs a matrix trace over the gauge algebra, and the biquaternion norm is a rank-two bilinear with a single algebra slot; the norm of the biquaternion representative is not gauge invariant under $F_{\mu\nu}\mapsto\tilde UF_{\mu\nu}\tilde U^{-1}$. This is a recorded gap, not an oversight.
- **Imported.** The star, the bound and the Chern–Simons primitive.

**Where the application is.** [Instantons and Solitons in Biquaternionic Form](instantons-and-solitons-in-biquaternionic-form.html) applies every statement above to the framework's compact factor: it writes the density for both cases, verifies the total-derivative identity symbolically, checks the non-invariance numerically, and exhibits the BPST solution with its charge and action.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F_{\mu\nu}$ | the field strength |
| $\tilde F_{\mu\nu}$ | its dual |
| $\varrho$ | the topological density |
| $Q$ | the topological charge, an integer |
| $\Omega_{\mathrm{CS}}$ | the Chern–Simons form |
| $J_{\mathrm{CS},\mu}$ | the abelian Chern–Simons current |
| $g$ | the gauge coupling |

## Further Reading

- A. A. Belavin, A. M. Polyakov, A. S. Schwarz and Yu. S. Tyupkin, "Pseudoparticle Solutions of the Yang–Mills Equations," *Physics Letters B* **59** (1975) 85–87, the BPST instanton.
- E. B. Bogomolny, "Stability of Classical Solutions," *Soviet Journal of Nuclear Physics* **24** (1976) 449, the bound.
- S. Coleman, *Aspects of Symmetry*, Chapter 7, for the topological charge and its consequences.
