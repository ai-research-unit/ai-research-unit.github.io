# __Ostrogradsky, or Why No Rung Goes Past Two Derivatives__

## Introduction

**The claim.** A nondegenerate Lagrangian that depends on a field's second derivative — or any higher one — has a Hamiltonian that is linear in one of its momenta, and a linear Hamiltonian is unbounded below. **That is Ostrogradsky's theorem**, and it is why every rung of this corpus is built from the field and its first derivative only. The corpus never states the theorem and never needs to: it is a structural reason for a structural fact, and the fact is that no density in the chain contains a second derivative of a field.

**What is established.** Four things. First, the construction: the extra canonical pair, the momentum that appears linearly, and the resulting state of unbounded energy. Second, the count: an $N$-th order density gives $2N$ pieces of canonical data, and half of the extra ones carry the wrong sign. Third, what the corpus's second-order *appearances* actually are — the Madelung transformation's $\nabla^{2}\varrho/\varrho$, the Korteweg stress, the quantum pressure — and that none of them is a higher-derivative term in an action. Fourth, the two escapes the theorem allows, degeneracy and effective-field-theory truncation, and which of the two each of the corpus's cases uses.

**Why it belongs here.** The section's other articles are apparatus the chain assumes; this one is a *prohibition* the chain obeys. **It answers the question a careful reader will ask at the first gradient correction: why is $\nabla^{2}\varrho$ allowed in the pressure and not in the action?**

**What is not new.** The theorem is Ostrogradsky's, 1850, and its modern reading as an instability is a twentieth-century result. **What the corpus adds is the audit**: which of its own second-order quantities are genuine higher-derivative terms and which are not, and why its actions are all first-order bilinears.

## The Theorem

**The construction, in three lines.** Take a density $\mathcal L(q,\dot q,\ddot q)$ that depends on $\ddot q$ and is nondegenerate in it, and define the two momenta,

$$
p_2:=\frac{\partial\mathcal L}{\partial\ddot q},\qquad
p_1:=\frac{\partial\mathcal L}{\partial\dot q}-\frac{d}{dt}p_2 .
$$

**Two momenta for one coordinate means that $\dot q$ has become an independent canonical variable**, so the phase space is $(q,\dot q,p_1,p_2)$: four pieces of data where a second-order density would have two.

**The Hamiltonian, and the linearity.** Inverting $p_2=\partial\mathcal L/\partial\ddot q$ for $\ddot q$ and Legendre-transforming,

$$
H=p_1\dot q+p_2\ddot q-\mathcal L
=p_1\dot q+\bigl[p_2\ddot q-\mathcal L\bigr]_{\ddot q=\ddot q(q,\dot q,p_2)} .
$$

**The first term is linear in $p_1$ with coefficient $\dot q$, and nothing else in $H$ depends on $p_1$.** So $H$ is unbounded below: send $p_1\to-\infty$ at fixed $\dot q>0$ and the energy falls without limit. **That is the instability**, and it is not a technicality of the Legendre transform — it is the statement that the extra canonical pair contributes a state whose energy can be made arbitrarily negative.

**The count, stated generally.** A density with derivatives up to order $N$ has canonical variables $q,\dot q,\dots,q^{(N-1)}$ and their $N$ momenta, hence $2N$ pieces of data. **The ground state of the second-order theory has two; each additional order adds a pair, and each added pair is a ghost** — a state with the wrong sign of energy that can be excited together with positive-energy states while conserving total energy.

**Why the theorem is about nondegeneracy.** If $\mathcal L$ is degenerate in the highest derivative — if $\partial^{2}\mathcal L/\partial\ddot q^{2}=0$, or if the highest derivative appears only linearly — the inversion fails, the extra momentum is a constraint rather than a coordinate, and the extra state can be removed. **That is the escape the corpus's first-order densities use and the one the Dirac–Bergmann algorithm performs**: a degenerate higher-derivative theory is a lower-order theory in disguise.

## Where the Instability Lives: Energy, Norm, and the Corpus's Scalar Part

**The standard reading.** The ghost is a state of negative energy, so the vacuum is unstable: positive- and negative-energy states can be pair-produced while conserving total energy, and the decay rate is infinite without a cutoff.

**The sharper reading in this corpus, and it is why the theorem is worth its own page here.** Energies in the corpus are read as the scalar part of a Hermitian element — $T_{00}=\mathrm{Sc}(\tilde\Sigma_\Psi)=\mathcal H$ — and norms are read through the indefinite Hermitian form. **A state with negative energy and a state with negative norm are therefore read in the same display**: a ghost's scalar part is negative and its norm is negative together, so **stability and unitarity fail as one failure rather than two**. In a positive-definite formalism the two must be argued separately; here the algebra exhibits them at once.

**What this does not mean.** It does not mean that every negative-norm direction is a ghost: the indefinite form's spacelike directions are negative-norm and perfectly healthy, because their scalar part is not the energy. **The identification is between the *scalar part of the energy element* and the norm, and only a state whose energy is that scalar part can be called a ghost by this route.**

**The first-order case, which is the control.** A density linear in $\dot q$ has a vanishing Hessian, so its "extra" momentum is a constraint and no ghost survives: the Dirac field is the corpus's example, and [the Dirac–Bergmann article](the-dirac-bergmann-algorithm-first-and-second-class-constraints.html) shows the constraint doing the removing. **So the ladder is not "higher order bad"; it is "nondegenerate higher order bad, degenerate higher order fine".**

## Why the Corpus's Rungs Are All Second Order

**One gradient, one bilinear.** Every density in the chain is built from the field and its first derivative, because the algebra supplies one gradient operator $\nabla_\Phi$ and a rung's density is a bilinear in it. **A second derivative would be a bilinear in a composition of gradients**, which is a different object and appears in the corpus only as a correction. **That is the structural reason**, and it is why the prohibition is invisible: no one ever wrote the forbidden term.

**The ladder, with the corpus's instances.**

| highest derivative in the density | canonical data | is the energy bounded below? | the corpus's instance |
| --- | --- | --- | --- |
| none | the field only | no dynamics at all | a potential term alone |
| one, linear in $\dot q$ | the field, with a constraint | yes, after the constraint | the Dirac density |
| one, quadratic in $\dot q$ | the field and its momentum | yes, if the kinetic coefficient is positive | every scalar, vector and matrix rung |
| two | the field, its first derivative, two momenta | **no** | none |

**The corpus's rungs occupy the third row and its first-order density the second.** The fourth row is empty, and the theorem is why.

### The Second-Order Equation That Is Not a Second-Order Action

**This is the point most easily missed, and it is the article's practical use.** The polar reading of the wave equation produces

$$
p_{\mathrm{qnt}}\ \propto\ \frac{h^{2}}{4\pi^{2}}\,\frac{\nabla^{2}\varrho}{\varrho},
$$

a second derivative of the amplitude, and a reader may conclude that the fluid's equation has a higher-derivative origin. **It does not.** The quantum pressure comes from a gradient energy in the density,

$$
\mathcal E_{\mathrm{grad}}\propto|\vec\nabla_\Phi\varrho|^{2},
$$

which is **first order in each factor** — a bilinear in one gradient, exactly the third row of the table. **The $\nabla^{2}\varrho$ appears when the first-order energy is varied**, and a variation raises the order of the equation without raising the order of the action. **So the Madelung transformation converts a second-order *equation* into a second-order *equation* written differently, and adds no canonical pair.**

**The same reading applies to the Korteweg stress.** Its gradient term is a gradient energy of a density, first order in the field's gradient and second order only after the divergence of the stress is taken. **A gradient energy is not an Ostrogradsky term**, and the corpus's own remark that the Korteweg stress is constitutive rather than bookkeeping — made in [the Belinfante–Rosenfeld article](belinfante-rosenfeld-why-the-canonical-stress-tensor-is-not-symmetric.html) — is the same distinction read thermodynamically.

**The test, in one line.** Count the derivatives in the *density*, not in the equation. **Second-order equations from first-order densities are the normal case**; second-order densities are the pathological one.

## The Two Escapes, and Which the Corpus Uses

**Escape one: degeneracy.** If the highest derivative's coefficient is a constraint, the extra pair is removed. The Dirac density is the corpus's case and $f(R)$ gravity is the standard one — a fourth-order-looking theory that is a scalar-tensor theory with no extra state. **The corpus's first-order rungs are degenerate in exactly this sense**, and the Dirac–Bergmann article is where the removal is performed.

**Escape two: the cutoff.** If the higher-derivative term is a correction rather than a fundamental term, the ghost's mass sits at the cutoff and the state is not in the low-energy theory. **The corpus's $\frac{h^{2}}{4\pi^{2}}$ corrections are of this kind**: they are what integrating out a scale produces, and the expansion is truncated where the ghost would appear. **The corpus uses this escape every time it keeps a gradient correction and drops the next one**, and the price is that the truncation must come with a power counting that says when the next term matters.

**Neither is an evasion.** The theorem forbids a nondegenerate higher-derivative *fundamental* density; it says nothing about a degenerate one or about an effective expansion. **A reader who invokes Ostrogradsky to forbid every gradient correction has misread it**, and a reader who keeps a gradient correction without a cutoff has misread the other half.

**The discrete face of the same trade.** On the lattice the derivative is a difference, and a higher-order difference operator produces extra low-energy states — the doublers — whose removal costs a term of the same order. **The Wilson term is the lattice's Ostrogradsky price paid in advance**, and [the discrete lattice article](the-discrete-lattice-and-the-thermal-circle.html) is where the corpus's discreteness lives. The analogy is structural and is not a derivation.

## What It Does Not Give

**It does not forbid a higher-derivative rung in principle.** It says what such a rung would cost: an extra canonical pair with unbounded energy, removable only by degeneracy or by a cutoff. **A future rung with four derivatives would be legitimate if it were degenerate or effective**, and this article states the condition rather than a ban.

**It does not establish that the corpus's truncation is controlled.** That needs a power counting for $\frac{h}{2\pi}$ and a statement of which scale is integrated out; the corpus has the expansion and not the counting, and this article does not supply it.

**It does not address the ghost's own quantisation.** A ghost field's propagator has the wrong sign, and its treatment — indefinite metric, or a PT-symmetric reading, or a Lee–Wick contour — is a subject of its own. The corpus does not need it, because it has no ghost.

**It does not explain why the potential has the depth it has.** Stability against a ghost and stability of a vacuum are different questions; the second belongs to the field's potential and not to the order of its derivatives.

## Summary

A nondegenerate density with a second or higher derivative gives an extra canonical pair, and its Hamiltonian is linear in the extra momentum — hence unbounded. **That is Ostrogradsky's theorem**, and its count is $2N$ pieces of canonical data for a density of order $N$, with each pair beyond the first a ghost.

In this corpus the ghost's scalar part is negative and its norm is negative together, because the energy is the scalar part of a Hermitian element and the norm is the indefinite form's. **Stability and unitarity fail as one display**, which is the theorem's sharpest form here.

No rung goes past two derivatives because every density is a bilinear in one gradient. **The second-order *appearances* are not second-order *actions***: the quantum potential's $\nabla^{2}\varrho/\varrho$ and the Korteweg stress come from gradient energies that are first order in each factor, and a variation raises the equation's order without raising the density's. The test is to count derivatives in the density.

Two escapes are available and the corpus uses both: degeneracy, which removes the pair as a constraint, and the cutoff, which puts the ghost's mass out of reach. Neither evades the theorem; both are what the theorem permits. The lattice's doublers are the discrete face of the same trade.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\mathcal L(q,\dot q,\ddot q)$ | A density with a second derivative; the theorem's subject |
| $p_2=\partial\mathcal L/\partial\ddot q$ | The second momentum; its invertibility for $\ddot q$ is the nondegeneracy |
| $p_1=\partial\mathcal L/\partial\dot q-\frac{d}{dt}p_2$ | The first momentum, shifted by the second's total derivative |
| $H=p_1\dot q+p_2\ddot q-\mathcal L$ | The Ostrogradsky Hamiltonian; linear in $p_1$ |
| $2N$ | The canonical data of a density of order $N$; a ghost per pair beyond the first |
| $\mathrm{Sc}(\tilde\Sigma_\Psi)=\mathcal H$ | The energy as the scalar part; the display in which a ghost's sign is read |
| $p_{\mathrm{qnt}}\propto\frac{h^{2}}{4\pi^{2}}\frac{\nabla^{2}\varrho}{\varrho}$ | The quantum pressure; second order in the equation, first order in the density |
| $\mathcal E_{\mathrm{grad}}\propto|\vec\nabla_\Phi\varrho|^{2}$ | The gradient energy behind it; the third row of the ladder |
| $\frac{h^{2}}{4\pi^{2}}$ | The expansion parameter of the gradient corrections; the cutoff's bookkeeping |
| $f(R)$ | The degenerate higher-derivative case, a scalar-tensor theory with no extra state |

## Further Reading

- M. Ostrogradsky, "Mémoires sur les équations différentielles, relatives au problème des isopérimètres," *Mémoires de l'Académie Impériale des Sciences de St. Pétersbourg* 6 (1850), 385–517, the original theorem.
- Richard P. Woodard, "Ostrogradsky's theorem on Hamiltonian instability," *Scholarpedia* 10 (2015), 32243, the modern statement and its use in higher-derivative gravity.
- Marc Henneaux and Claudio Teitelboim, *Quantization of Gauge Systems* (Princeton University Press, 1992), for degenerate higher-derivative systems and the constraint removal.
- Thomas P. Sotiriou and Valerio Faraoni, "*f(R)* theories of gravity," *Reviews of Modern Physics* 82 (2010), 451–497, for the degenerate case and the equivalent scalar-tensor reading.
- Kenneth G. Wilson, "Confinement of quarks," *Physical Review D* 10 (1974), 2445–2459, and the lattice literature, for the doubler problem and the Wilson term.
- [The Dirac–Bergmann Algorithm: First- and Second-Class Constraints](the-dirac-bergmann-algorithm-first-and-second-class-constraints.html), for the constraint that removes the degenerate pair.
- [Belinfante–Rosenfeld: Why the Canonical Stress Tensor Is Not Symmetric](belinfante-rosenfeld-why-the-canonical-stress-tensor-is-not-symmetric.html), for the Korteweg stress as constitutive rather than bookkeeping.
- [Viscosity and the Rayleigh Dissipation Function](viscosity-and-the-rayleigh-dissipation-function.html), for a second-order appearance in the equations that is not one in the density.
- [The Three Scales: $c$, $\hbar$ and $k_B$ as the Three Continuations](the-three-scales-c-hbar-and-k-b-as-the-three-continuations.html), the section's other result about the shape of the chain.
- [The Discrete Lattice and the Thermal Circle](the-discrete-lattice-and-the-thermal-circle.html), for the corpus's discreteness and the doublers' home.
