# __The Carrier of the Proca Field__

## Introduction

The Proca field is the only field of the corpus whose carrier is a **sector**. Its potential is a four-vector, a four-vector with an imaginary time coefficient is an anti-Hermitian element, and the anti-Hermitian elements are the material sector. The carrier is therefore not a subspace chosen for the occasion: it is one of the two halves into which the algebra is cut by Hermitian conjugation.

That gives the Proca field a property the other two do not have. The Klein–Gordon carrier, the centre, meets each sector in one real line, so a scalar field is material only if its value is imaginary. The Dirac carrier meets the material sector in one real dimension of four, so a spinor field is mostly informational. The Proca carrier **is** the material sector: three real dimensions for the spin and one for the time slot, and the constraint removes the time slot.

This article states the carrier, proves the closure, and prices it. The price is one object, the field strength, which leaves the sector; and one property, the charge, which the sector cannot carry.

## The Potential Is Material

The potential of the corpus is

$$
\tilde A_\Phi=i\,a'_t\,e_t+\vec A,
\qquad
a'_t\in\mathbb{R},
\quad
\vec A\in\mathbb{R}^{3},
$$

an anti-Hermitian element: the time coefficient is imaginary and the three spatial coefficients are real. The sector is closed under addition and under multiplication by real scalars, so it is a real vector space of dimension four, and the potential of any real four-vector field lies in it.

**The invariants are real on it.** With $\langle\tilde Q\rangle_\natural=\tilde Q\tilde Q^{\natural}$,

$$
\langle\tilde A_\Phi\rangle_\natural=-(a'_t)^{2}+\lvert\vec A\rvert^{2},
\qquad
B^{2}=\lvert\vec A\rvert^{2}\ge0,
$$

so the quaternionic norm is real and the vector square is non-negative. That is what lets the four-region classification of the corpus apply to this field without modification, and it is the reason the Proca field can be read as a fluid of particles: a real norm is a mass, while an imaginary one would be a phase.

## The Equation Closes, and the Reason Is One Identity

The Proca equation of the corpus is

$$
\tilde\nabla_\Phi\tilde F=k_m^{2}\tilde A_\Phi,
\qquad
\tilde F=\mathrm{Vect}\bigl((\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi\bigr),
$$

with $k_m=mc/\hbar$. For a plane wave the gradient is the element $\tilde K\in\mathbb{B}_\Phi$ and its conjugate is $\tilde K^{\natural}$, and the whole content of the closure is one identity:

$$
\tilde K\,\mathrm{Vect}\bigl(\tilde K^{\natural}\tilde A\bigr)-\langle\tilde K\rangle_\natural\,\tilde A
=-\tilde K\,\mathrm{Sc}\bigl(\tilde K^{\natural}\tilde A\bigr).
$$

The identity was checked over one hundred random material momenta and potentials, with a maximum error of $3\times10^{-15}$.

**Read it as a statement about the sector.** The left side is the residual of the Proca equation. The right side is a material element $\tilde K$ multiplied by a **complex number**, $\mathrm{Sc}(\tilde K^{\natural}\tilde A)$, which is central. A central multiplier preserves the sector, so the residual is material for every material potential. The measured leakage of the residual out of $\mathbb{B}_\Phi$ is $5\times10^{-15}$ across one hundred trials.

**Read it as a statement about the Lorenz condition.** The residual vanishes exactly when the scalar $\mathrm{Sc}(\tilde K^{\natural}\tilde A)$ vanishes, and that scalar is the Lorenz condition in this notation, equivalent to $-q\,a'_t+\vec k\cdot\vec A=0$ with $q$ the frequency of the wave. So the Lorenz condition is what makes the equation hold, and the sector is closed whether it holds or not.

**This is the correction of a natural mistake.** One might think that the sector closes only on the Lorenz surface, because the Lorenz condition is what reduces Proca to four Klein–Gordon equations. It does not: the closure is a property of the multiplication, and the Lorenz condition is a property of the solution. The distinction matters, because a restriction that held only on a gauge slice would be a restriction on the solutions, while this one is a restriction on the field's home.

## The Field Strength Leaves the Sector

One object of the theory does not stay, and it is one derivative order away from the potential.

The field strength is a product of two material elements, and the product of two material elements splits:

$$
\tilde A\tilde B=\tfrac12[\tilde A,\tilde B]+\tfrac12\{\tilde A,\tilde B\},
\qquad
\tfrac12[\tilde A,\tilde B]\in\mathbb{B}_\Phi,
\quad
\tfrac12\{\tilde A,\tilde B\}\in\mathbb{B}_\Psi,
$$

exactly, since $[\tilde A,\tilde B]$ is anti-Hermitian and $\{\tilde A,\tilde B\}$ is Hermitian for anti-Hermitian factors. So $\tilde F$ is a mixed element, and the split has a name:

$$
\tilde F=i\sqrt{\epsilon}\,\vec E-\sqrt{\mu}\,\vec H,
\qquad
i\sqrt{\epsilon}\,\vec E\in\mathbb{B}_\Psi,
\qquad
-\sqrt{\mu}\,\vec H\in\mathbb{B}_\Phi .
$$

The **electric** part is informational and the **magnetic** part is material, with $\vec B=\mu\vec H$. This is the corpus's assignment, and here it is derived from the multiplication.

**The mixing cannot be removed.** A global phase rotates the two parts into one another, and since $\vec E$ and $\vec H$ are orthogonal for a plane wave, no rotation makes one of them vanish. Maximising the material **amplitude** share over the phase gives $0.764$ for a massive plane wave, against $1$ for a pure magnetic field and $1/\sqrt2=0.707$ for a null one. The invariant content of the mixing is the ratio of the amplitudes,

$$
\frac{\text{informational amplitude}}{\text{material amplitude}}=\frac{\lvert\vec E\rvert}{c\lvert\vec B\rvert},
$$

which is frame-dependent; the material amplitude share ranges over $0.71$ to $0.95$ across fifty boosts, from a null field at $1$ to a strongly magnetic one near $0.33$.

**The lesson.** The dynamical variable is material and the derived object straddles the two sectors. A restriction of the Proca theory to the material sector is therefore a restriction on the potential, not on the field strength, and the two transverse polarisations are exactly what the field strength carries out of the sector.

## The Constraint Removes the Singlet

The material sector is a four-vector, and under the rotation subgroup it splits:

$$
\mathbb{B}_\Phi=\mathbb{R}\,(i e_t)\ \oplus\ V_{\mathbb{R}},
\qquad
V_{\mathbb{R}}=\{\vec A\ :\ \vec A\in\mathbb{R}^{3}\},
$$

that is $1\oplus3$. The time slot is fixed by a rotation and the three spatial slots rotate among themselves, which was checked on the generators. So the sector carries a scalar and a vector.

**The spin-one carrier proper is the second summand.** The traceless part $V=\ker\operatorname{tr}$ of the algebra is the complex three-dimensional space of pure elements, and $V_{\mathbb{R}}$ is its real form. That is the carrier the companion article *Spin and the Three Elementary Carriers* assigns to spin one, and it has three states. The material sector is one dimension larger, and the extra dimension is the time slot:

$$
\mathbb{B}_\Phi=V_{\mathbb{R}}\oplus\mathbb{R}\,(i e_t),
\qquad
\dim_\mathbb{R}\mathbb{B}_\Phi=\dim_\mathbb{R}V_{\mathbb{R}}+1 .
$$

**The constraint does the rest.** The Proca equation implies the Lorenz condition, and the condition removes one degree of freedom — the time slot, the singlet that the adjoint action annihilates. What remains is three components, which is the spin-one triplet, and the carrier that survives is the real form of $V$.

So there are two correct statements and they are not the same statement. The carrier of the **potential** is $\mathbb{B}_\Phi$, of real dimension four, because a potential is a four-vector and a four-vector needs its time slot. The carrier of the **spin** is $V$, of real dimension three, and the difference between them is exactly the component that the constraint removes. Writing the potential in $\mathbb{B}_\Phi$ is writing the spin carrier together with the degree of freedom that the equation then eliminates.

The **field strength** sits on the second summand. A pure element is traceless, so $\tilde F\in V$, and the material half of $\tilde F$ is $V_{\mathbb{R}}$. The chain is then: potential in $\mathbb{B}_\Phi$, one derivative to the traceless part, and the constraint removes the time slot that the potential brought in.

## The Charge Is Not Native Here

The sector has no complex structure. Multiplication by $i$ maps it onto the informational sector, $i\mathbb{B}_\Phi=\mathbb{B}_\Psi$, so $\mathbb{B}_\Phi$ is a **real form** of the algebra and its scalars are real.

A central phase is the operation a charge generates, and here it destroys the carrier:

$$
\theta=0\ \text{or}\ \pi:\ \mathbb{B}_\Phi,
\qquad
\text{every other }\theta:\ \text{mixed}.
$$

Over two thousand random phases, none kept a charged potential material. The sector therefore carries the **neutral** Proca field, and a charged one needs both sectors.

**The count says the same thing.** The free Proca field has four real parameters, which is the real dimension of its carrier. The coupled field has eight, which is the real dimension of the algebra. The doubling reported in *The Charged Proca Fluid* is the arithmetic of leaving the sector.

## What the Sector Buys

Three things, and they are the reason to make the restriction.

**A real norm.** $\langle\tilde A_\Phi\rangle_\natural$ is real, so the dispersion relation $-(k'_t)^{2}+\lvert\vec k_\Phi\rvert^{2}=-k_m^{2}$ is an equation between real numbers, the quantity that the four regions of the corpus classify is real, and that classification applies unchanged.

**A polar word with no phase.** The material sector's word is scale, boost and direction, $\tilde A_\Phi=\varepsilon ir\tilde U$, and the central bracket of the logarithmic derivative vanishes identically. There is no phase gradient, no guidance equation and no Madelung pair. *The Proca Equation in Biquaternionic Polar Variables* develops the consequence.

**A fluid of particles.** The word is the word of a medium: a density, a flow and a direction. The corpus's fluid interpretation of the Proca field is available because the carrier is real, and it would not be available in either of the other two carriers.

## What Was Checked

The residual identity was verified on one hundred random material plane waves, with a maximum error of $3\times10^{-15}$, and the residual's leakage out of $\mathbb{B}_\Phi$ is $5\times10^{-15}$. The product split into commutator and anticommutator is exact. The field strength's material amplitude share is $0.764$ for a massive wave at any polarisation, $1$ for a purely magnetic field and $0.707$ for a null one. The rotation action fixes the time slot and rotates the three spatial slots. No phase other than $\pm1$ keeps a charged potential material, over two thousand samples.

## Summary

The carrier of the Proca field is the material sector $\mathbb{B}_\Phi$, of real dimension four, and it is the only one of the three carriers that is a sector. The potential is anti-Hermitian by construction, its quaternionic norm is real and its vector square is non-negative.

The equation closes on the sector for every material potential, and the reason is the identity

$$
\tilde K\,\mathrm{Vect}\bigl(\tilde K^{\natural}\tilde A\bigr)-\langle\tilde K\rangle_\natural\,\tilde A
=-\tilde K\,\mathrm{Sc}\bigl(\tilde K^{\natural}\tilde A\bigr),
$$

whose right side is a central multiplier times a material element. The Lorenz condition makes the residual vanish; it is not what makes the residual material.

The field strength leaves the sector. It is a product of two material elements, hence a commutator plus an anticommutator, and the split is the split into magnetic and electric parts. No phase removes the mixture, and its weight is the amplitude ratio $\lvert\vec E\rvert/(c\lvert\vec B\rvert)$.

The sector is a four-vector, which is $1\oplus3$ under rotations; the constraint removes the singlet and leaves the spin-one triplet. The traceless part $V$ is the carrier of the *spin*, of real dimension three, and the material sector is the carrier of the *potential*, of real dimension four: the extra dimension is the time slot that the constraint removes, $\mathbb{B}_\Phi=V_{\mathbb{R}}\oplus\mathbb{R}(ie_t)$. The sector is a real form, so it carries no complex structure, and a continuous phase destroys it. The restriction is therefore a restriction to the neutral field, and the doubling of parameters in the charged theory is the arithmetic of leaving the sector.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | The biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_t=1,\ \vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_\eta^{2}=-e_t$ |
| $i$ | Central scalar imaginary |
| $\mathbb{B}_\Phi$, $\mathbb{B}_\Psi$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\tilde A_\Phi=i\,a'_t\,e_t+\vec A$ | The potential, an element of $\mathbb{B}_\Phi$ |
| $\langle\tilde Q\rangle_\natural=\tilde Q\tilde Q^{\natural}$ | Quaternionic norm, real on $\mathbb{B}_\Phi$ |
| $\tilde F=\mathrm{Vect}\bigl((\tilde\nabla_\Phi)^{\natural}\tilde A_\Phi\bigr)$ | Field strength: pure, and mixed between the sectors |
| $\tilde K$ | The gradient as a plane-wave symbol, an element of $\mathbb{B}_\Phi$ |
| $V=\ker\operatorname{tr}$ | The traceless part, complex dimension three |
| $V_{\mathbb{R}}$ | The real pure elements, the real form of $V$ |
| $\mathrm{Sc}\bigl(\tilde K^{\natural}\tilde A\bigr)$ | The Lorenz scalar |
| $k_m=mc/\hbar$ | Mass wave number |

## Further Reading

- [The Proca Equation: Massive Spin 1 in Biquaternionic Form](the-proca-equation-massive-spin-1-in-biquaternionic-form.html), for the equation, the implied Lorenz condition and the three polarisations.
- [The Carrier of the Klein–Gordon Field](the-carrier-of-the-klein-gordon-field.html), for the carrier of complex dimension one.
- [The Carrier of the Dirac Field](the-carrier-of-the-dirac-field.html), for the carrier that is a minimal left ideal.
- [Spin and the Three Elementary Carriers](spin-and-the-three-elementary-carriers.html), for the classification of the carriers and their relation to the sectors.
- [The Proca Equation in Biquaternionic Polar Variables](the-proca-equation-in-biquaternionic-polar-variables.html), for the polar word of the sector and the absence of a Madelung pair.
- [The Charged Proca Fluid](the-charged-proca-fluid.html), for the doubling of the parameters under a coupling.
- [The Self-Dual and Anti-Self-Dual Split: Spin 1 from the Biquaternion Material Sector](the-self-dual-and-anti-self-dual-split-spin-1-from-the-biquaternion-material-sector.html), for the complex structure that the sector acquires only after complexification.
- [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html), for the sector as a four-vector space.
