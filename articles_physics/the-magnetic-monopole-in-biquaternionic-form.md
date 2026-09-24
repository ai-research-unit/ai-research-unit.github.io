# __The Magnetic Monopole in Biquaternionic Form__

## Introduction

In the standard formulation, Maxwell's equations treat electricity and magnetism asymmetrically. Electric charge and current source the field through

$$
\mathrm{div}\,\mathbf{D} = \rho_e, \qquad \mathrm{rot}\,\mathbf{H} = \frac{\partial \mathbf{D}}{\partial t} + \mathbf{J}_e,
$$

while the remaining two equations,

$$
\mathrm{div}\,\mathbf{B} = 0, \qquad \mathrm{rot}\,\mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t},
$$

are homogeneous: they hold identically once the field is written in terms of a potential. There is no magnetic charge, and the symmetry that would exchange the electric and magnetic halves of the field is broken by the absence of magnetic sources.

The preceding articles established two facts that bear directly on this asymmetry. First, the field-strength biquaternion

$$
\tilde{F} = i\sqrt{\epsilon}\,\mathbf{E} - \sqrt{\mu}\,\mathbf{H}
$$

carries the electric field in its imaginary half, in the Hermitian subspace $\mathbb{M}_+$, and the magnetic field in its real half, in the anti-Hermitian subspace $\mathbb{M}_-$: the two halves of the electromagnetic field occupy the two complementary sectors of the algebra. Second, the electric–magnetic duality rotation acts on $\tilde{F}$ by multiplication by a scalar phase, so it is a rotation *inside* the algebra rather than a Lorentz transformation. This article asks what the biquaternion algebra says about the object that would restore the symmetry on the source side: the magnetic monopole.

The fit is real, and it should be shown rather than asserted. Magnetic sources extend the single biquaternionic Maxwell equation cleanly, with the electric and magnetic source terms assembling into one complex biquaternion; the duality rotation then becomes an exact internal symmetry of the *sourced* equations, not only of the source-free ones; and the Dirac quantisation condition appears as a condition on the holonomy of the biquaternionic potential. The monopole is, in this precise sense, the object for which the second, magnetic half of the electromagnetic structure is needed.

The article is equally concerned with what the framework does **not** do. The biquaternion algebra is classical; it contains no $\hbar$, and it neither predicts that a monopole exists nor fixes its mass or charge. No magnetic monopole has ever been observed. The algebra accepts a monopole; it does not manufacture one.

## Maxwell's Equations with Magnetic Sources

Let the medium have permittivity $\epsilon$ and permeability $\mu$, with $\mathbf{D} = \epsilon\mathbf{E}$, $\mathbf{B} = \mu\mathbf{H}$ and $c = 1/\sqrt{\epsilon\mu}$. Admit a magnetic charge density $\rho_m$ and a magnetic current density $\mathbf{J}_m$, and write the symmetric Maxwell system

$$
\mathrm{div}\,\mathbf{D} = \rho_e, \qquad
\mathrm{rot}\,\mathbf{H} = \frac{\partial \mathbf{D}}{\partial t} + \mathbf{J}_e,
$$

$$
\mathrm{div}\,\mathbf{B} = \rho_m, \qquad
\mathrm{rot}\,\mathbf{E} = -\frac{\partial \mathbf{B}}{\partial t} - \mathbf{J}_m .
$$

With $\rho_m = \mathbf{J}_m = 0$ this is the system of the parent article. The electric source is the four-current biquaternion of that article, now written with a subscript,

$$
\tilde{R}_e = \frac{i\rho_e}{\sqrt{\epsilon}} + \sqrt{\mu}\,\mathbf{J}_e \in \mathbb{M}_-,
$$

and the magnetic source is the analogous biquaternion

$$
\tilde{R}_m = \frac{i\rho_m}{\sqrt{\mu}} + \sqrt{\epsilon}\,\mathbf{J}_m \in \mathbb{M}_- .
$$

Both sources are four-currents and therefore lie in the material subspace $\mathbb{M}_-$; the factors of $1/\sqrt{\mu}$ and $\sqrt{\epsilon}$ are the magnetic counterparts of the electric normalizations, chosen so that the combined equation below carries no explicit $\epsilon$ or $\mu$. With these definitions the four symmetric Maxwell equations collapse into the single biquaternionic equation

$$
\boxed{\;\tilde{\nabla}\tilde{F} = -\tilde{R}_e - i\,\tilde{R}_m\;}
$$

with the gradient $\tilde{\nabla} = e_0\partial_{ict} + e_1\partial_x + e_2\partial_y + e_3\partial_z$ of the parent article. The factor of $-i$ in front of the magnetic source is not decoration: it is the same scalar phase that implements duality, and it is what places the magnetic contribution in the complementary sector of the algebra.

The reduction is best seen by taking scalar and vector parts. For a pure-vector field strength, $\tilde{\nabla}\tilde{F}$ has scalar part $-\mathrm{div}\,\mathbf{F}$ and vector part $\partial_{ict}\mathbf{F} + \mathrm{rot}\,\mathbf{F}$. The scalar part of the equation gives

$$
\mathrm{div}\,\mathbf{F} = \frac{i\rho_e}{\sqrt{\epsilon}} - \frac{\rho_m}{\sqrt{\mu}},
$$

and the vector part gives

$$
\partial_{ict}\mathbf{F} + \mathrm{rot}\,\mathbf{F} = -\sqrt{\mu}\,\mathbf{J}_e - i\sqrt{\epsilon}\,\mathbf{J}_m .
$$

Substituting $\mathbf{F} = i\sqrt{\epsilon}\mathbf{E} - \sqrt{\mu}\mathbf{H}$ and separating real and imaginary parts returns the four equations above. Two cases verify the signs independently of the case that suggested them. For a **magnetostatic configuration** with $\rho_e = \mathbf{J}_e = \mathbf{J}_m = 0$ and $\partial_t = 0$, the scalar equation reads $\mathrm{div}\,\mathbf{F} = -\rho_m/\sqrt{\mu}$; since $\mathbf{F} = -\mathbf{B}/\sqrt{\mu}$ and $\mathrm{div}\,\mathbf{B} = \rho_m$, both sides equal $-\rho_m/\sqrt{\mu}$, and the vector part is zero on both sides because $\mathrm{rot}\,\mathbf{H} = 0$. For a **static magnetic current** with $\rho_m = 0$, $\mathrm{rot}\,\mathbf{E} = -\mathbf{J}_m$ and $\mathrm{rot}\,\mathbf{H} = 0$, the vector equation gives $\mathrm{rot}\,\mathbf{F} = i\sqrt{\epsilon}\,\mathrm{rot}\,\mathbf{E} = -i\sqrt{\epsilon}\,\mathbf{J}_m$, matching the right-hand side. The two checks use different components and different source types.

Charge conservation has a magnetic counterpart. Just as the electric source is constrained by $\mathrm{Sc}(\bar{\tilde{\nabla}}\tilde{R}_e) = 0$, which is $\mathrm{div}\,\mathbf{J}_e + \partial_t\rho_e = 0$, the magnetic source satisfies $\mathrm{Sc}(\bar{\tilde{\nabla}}\tilde{R}_m) = 0$, which is $\mathrm{div}\,\mathbf{J}_m + \partial_t\rho_m = 0$. Magnetic charge is conserved for exactly the algebraic reason electric charge is: the conservation law is the integrability condition of the field equation, and the two sources are subject to it separately because they occupy the two complementary sectors under $\mathrm{Sc}$.

## The Dual Field-Strength Biquaternion

The symmetric system invites a second field-strength biquaternion. Define the dual field configuration by the duality transformation of the field-strength article at $\theta = \pi/2$,

$$
\mathbf{E} \mapsto c\,\mathbf{B}, \qquad \mathbf{B} \mapsto -\frac{1}{c}\,\mathbf{E},
$$

and let $\tilde{F}_\star$ be the field-strength biquaternion built from the dual fields. Using $\mathbf{B} = \mu\mathbf{H}$ and $c = 1/\sqrt{\epsilon\mu}$,

$$
\tilde{F}_\star = i\sqrt{\epsilon}\,(c\mathbf{B}) - \sqrt{\mu}\left(-\frac{1}{c\mu}\mathbf{E}\right)
= \frac{i}{\sqrt{\mu}}\,\mathbf{B} + \sqrt{\epsilon}\,\mathbf{E}
= -i\,\tilde{F},
$$

the last equality following from $\tilde{F} = i\sqrt{\epsilon}\mathbf{E} - \mathbf{B}/\sqrt{\mu}$. The dual field-strength biquaternion is therefore not an independent object: **Hodge duality is multiplication by the scalar phase $-i$**. This is the algebraic fact behind the Riemann–Silberstein linearization, and it is why the dual carries the electric and magnetic parts with their roles exchanged — the real and imaginary halves of $-i\tilde{F}$ are exactly the magnetic and electric halves of $\tilde{F}$, in the opposite slots.

A reader arriving from a tensor formulation might expect the combination $\tilde{F} + i\tilde{F}_\star$ to double the field content. It does not: $\tilde{F} + i\tilde{F}_\star = \tilde{F} + i(-i\tilde{F}) = 2\tilde{F}$. The field strength already *is* the complexified object, its electric and magnetic halves being its Hermitian and anti-Hermitian parts. Where the complexification genuinely adds content is in the **sources**. They combine into

$$
\tilde{\mathcal{R}} = \tilde{R}_e + i\tilde{R}_m,
$$

whose $\mathbb{M}_-$ part is electric and whose $\mathbb{M}_+$ part is magnetic, and the field equation becomes $\tilde{\nabla}\tilde{F} = -\tilde{\mathcal{R}}$. This is the object on which duality acts nontrivially, and it is the reason a magnetic source is not a mere relabelling of the electric one: it enters through the other sector.

## Duality as an Internal Rotation

The field-strength article established that for a real angle $\theta$ the duality transformation rotates the Riemann–Silberstein vector, $\mathbf{V} \mapsto e^{-i\theta}\mathbf{V}$. In biquaternion terms, and since $\tilde{F} = i\sqrt{\epsilon}\,\mathbf{V}$, this is

$$
\tilde{F} \;\longmapsto\; e^{-i\theta}\,\tilde{F}.
$$

The verification is direct and does not rely on the special value $\theta = \pi/2$: substituting the general rotation $\mathbf{E} \mapsto \mathbf{E}\cos\theta + c\mathbf{B}\sin\theta$, $\mathbf{B} \mapsto \mathbf{B}\cos\theta - c^{-1}\mathbf{E}\sin\theta$ into the definition of $\tilde{F}$, the coefficient of the electric term is $i\sqrt{\epsilon}\cos\theta + \sqrt{\epsilon}\sin\theta$ and the coefficient of the magnetic term is $i(\sin\theta)/\sqrt{\mu} - (\cos\theta)/\sqrt{\mu}$, which are precisely the coefficients in $e^{-i\theta}\tilde{F} = (\cos\theta - i\sin\theta)(i\sqrt{\epsilon}\mathbf{E} - \mathbf{B}/\sqrt{\mu})$. The identity holds for every $\theta$, and the special case $\theta = \pi/2$ reproduces the dual field of the previous section.

The phase $e^{-i\theta}$ is a complex scalar of the algebra, an element of the scalar subspace $\mathbb{C}_{\mathbb{B}}$; it commutes with the quaternion units $e_1, e_2, e_3$ and hence with every element of $\mathbb{B}$, including every Lorentz rotor. Consequently:

- Duality **commutes with the Lorentz group**. It is not a Lorentz transformation and cannot be absorbed into one; it is an internal $U(1)$ symmetry generated by the scalar imaginary $i$.
- Duality **mixes the two sectors**. Since $\tilde{F} = i\sqrt{\epsilon}\mathbf{E} - \sqrt{\mu}\mathbf{H}$, the rotated field $e^{-i\theta}\tilde{F}$ has both a Hermitian and an anti-Hermitian part for generic $\theta$, and the electric and magnetic halves are exchanged continuously.
- Duality **rotates the norm form**. Because $N$ is bilinear, $N(e^{-i\theta}\tilde{F}) = e^{-2i\theta}N(\tilde{F})$, in agreement with the doubled-angle rotation of the pair $(I_1, 2cI_2)$ recorded in the field-strength article.

The new content of the sourced theory is that duality is a symmetry of the equations **with** sources. If $(\tilde{F}, \tilde{\mathcal{R}})$ satisfies $\tilde{\nabla}\tilde{F} = -\tilde{\mathcal{R}}$, then so does $(e^{-i\theta}\tilde{F}, e^{-i\theta}\tilde{\mathcal{R}})$, because $\tilde{\nabla}$ commutes with the scalar phase. At $\theta = \pi/2$ the rotation sends $\tilde{\mathcal{R}} = \tilde{R}_e + i\tilde{R}_m$ to $-i\tilde{R}_e + \tilde{R}_m$: the electric source is replaced by a magnetic one and vice versa, up to the scalar phase. Without magnetic charge there is no partner for the electric source, and duality is a symmetry only of the source-free equations — the observation recorded in the field-strength article. With magnetic charge the rotation closes on a symmetry of the full sourced theory, and it exchanges electric and magnetic charge. This is the precise sense in which the monopole is the object the second half of the electromagnetic structure is needed for.

## The Monopole Field

The static sector of the parent article carries over verbatim. With $\partial_t = 0$ the gradient reduces to $\tilde{\nabla}_{\mathrm{stat}} = e_1\partial_x + e_2\partial_y + e_3\partial_z$, and the sourced equation becomes

$$
\tilde{\nabla}_{\mathrm{stat}}\tilde{F} = -\tilde{R}_e - i\tilde{R}_m .
$$

For a point magnetic charge $g$ at the origin, $\rho_m = g\,\delta(\mathbf{x})$ and $\mathbf{J}_m = 0$, so $\tilde{R}_m = ig\,\delta(\mathbf{x})e_0/\sqrt{\mu}$ and the right-hand side is the real scalar source $g\,\delta(\mathbf{x})e_0/\sqrt{\mu}$. The parent article's static Green's function then gives

$$
\tilde{F}(\mathbf{x}) = -\frac{g}{4\pi\sqrt{\mu}}\,\frac{\hat{\mathbf{x}}}{\|\mathbf{x}\|^2},
\qquad
\mathbf{B}(\mathbf{x}) = \frac{g}{4\pi}\,\frac{\hat{\mathbf{x}}}{\|\mathbf{x}\|^2},
\qquad
\mathbf{E} = 0,
$$

the biquaternionic form of the Dirac monopole field $\mathbf{B} = g\hat{\mathbf{x}}/(4\pi\|\mathbf{x}\|^2)$. Substituting back confirms the equation, and the sign is fixed by the scalar part: $\mathrm{div}\,\mathbf{F} = -\rho_m/\sqrt{\mu}$ while $\mathrm{div}\,\mathbf{B} = \rho_m$.

The monopole field has a structural feature worth isolating. The electric Coulomb field of a point charge $q$ is, from the parent article, $\tilde{F} = iq\hat{\mathbf{x}}/(4\pi\sqrt{\epsilon}\|\mathbf{x}\|^2)$: a purely **imaginary** vector, hence an element of the Hermitian subspace $\mathbb{M}_+$. The magnetic Coulomb field above is a purely **real** vector, hence an element of the anti-Hermitian subspace $\mathbb{M}_-$. A static electric charge is thus a source whose field lies in the informational half of the algebra; a static magnetic charge is a source whose field lies in the material half. The duality rotation, which multiplies by $-i$, interchanges the two. This is the sharpest statement the framework makes about the monopole: it is the source whose field populates the sector complementary to the electric one.

The field is also classically singular in the familiar way. Its energy density $W = \tfrac{1}{2}\mu\mathbf{H}^2 = \mathbf{B}^2/(2\mu) \propto g^2/r^4$ integrates to a linearly divergent total energy for a point source, so the classical point monopole has infinite self-energy. Its mass is therefore not a prediction of the algebra but a model-dependent quantity: finite-mass monopoles arise only when the point singularity is resolved by additional structure, as in the 't Hooft–Polyakov solitons. The biquaternion algebra is silent on that structure.

## The Two Invariants and Magnetic Charge

The norm form of the field strength was computed in the previous article as

$$
N(\tilde{F}) = -\epsilon\left(I_1 + 2ic\,I_2\right),
\qquad
I_1 = \mathbf{E}^2 - c^2\mathbf{B}^2,
\qquad
I_2 = \mathbf{E}\cdot\mathbf{B}.
$$

The first invariant $I_1$ is an ordinary scalar; the second, $I_2$, is a pseudoscalar, odd under parity, and it is the imaginary part of the complex norm form. Because $N(\tilde{F}) \mapsto e^{-2i\theta}N(\tilde{F})$ under duality, the second invariant is exactly the one that duality rotates into the first: the pair $(I_1, 2cI_2)$ turns by the doubled angle.

Two different objects in this framework have a claim to the name "second invariant", and the monopole is responsible for only one of them. The **pointwise** second invariant is $I_2 = \mathbf{E}\cdot\mathbf{B}$, proportional to the Pontryagin density $F_{\mu\nu}\star F^{\mu\nu}$ of the field tensor. On a static pure monopole it vanishes: $\mathbf{E} = 0$ implies $I_2 = 0$, while $I_1 = -c^2\mathbf{B}^2 < 0$, so the monopole is a purely *magnetic-type* field in the invariant classification, on the negative-$I_1$ branch. The second invariant is nonzero only for a **dyon**, a source carrying both electric and magnetic charge, where the electric and magnetic fields are both present and generally not orthogonal. The monopole does not make $I_2$ nonzero; it is the dyon that does.

The **topological** second invariant is the magnetic charge itself. The electric charge is measured by the flux of $\mathbf{D}$ through a closed surface, $Q_e \propto \oint_{S^2}\mathbf{D}\cdot d\mathbf{A}$, and the magnetic charge by the flux of $\mathbf{B}$,

$$
Q_m \propto \oint_{S^2}\mathbf{B}\cdot d\mathbf{A},
$$

which is why $\rho_m$ appears in the scalar equation. This charge is conserved by the magnetic integrability condition of the second section, and it is a topological characteristic of the field configuration rather than the integral of a local density. If the brief phrase "the second invariant" is read as the second *conserved charge* of the theory, it is apt: electric charge is the first, magnetic charge is the second, and without monopoles the second is identically zero for every configuration. If it is read as the pointwise invariant $I_2$, it is not: that quantity vanishes on every static monopole. The framework supports the first reading and corrects the second, and the two should not be conflated.

## The Dirac Quantisation Condition

A point monopole cannot be described by a single smooth potential, and this is where the algebra meets quantum mechanics. If $\tilde{F}$ were the vector part of $\bar{\tilde{\nabla}}\tilde{A}$ for one biquaternionic potential $\tilde{A}$ defined everywhere, then the Bianchi identity would hold and no magnetic source could appear. A monopole forces a patchwise potential, with the two patches related on their overlap by a gauge transformation $\tilde{A}' = \tilde{A} - \tilde{\nabla}\Gamma$ with a multivalued $\Gamma$ — the biquaternionic form of the Dirac string. A charged particle transported around the string accumulates the Aharonov–Bohm phase

$$
\exp\left(\frac{i e}{\hbar c}\oint \mathbf{A}\cdot d\boldsymbol{\ell}\right)
= \exp\left(\frac{i e g}{\hbar c}\right),
$$

using that the flux through a surface bounded by the loop is the monopole charge $g$ in the normalization of the previous section. The phase must be trivial, $\exp(ieg/\hbar c) = 1$, so the product of the two charges is quantised:

$$
\boxed{\;e\,g = 2\pi n\,\hbar c\;}, \qquad n \in \mathbb{Z}.
$$

This is the **Dirac quantisation condition**, written in Heaviside–Lorentz units (the numerical prefactor absorbs factors of $4\pi$ and $\epsilon_0$ in other systems, and $n$ is the winding number of the multivalued gauge parameter). Because $e$ and $g$ appear only as a product, the condition relates them: given the electric charge, it fixes the magnetic charge to be $g = 2\pi n\hbar c/e$. Equivalently, the magnetic fine-structure constant is

$$
\alpha_m = \frac{g^2}{4\pi\hbar c} = \frac{n^2}{4\alpha},
$$

where $\alpha = e^2/(4\pi\hbar c)$ is the electric one. With $\alpha \approx 1/137$, this gives $\alpha_m \approx 34.25\,n^2$: the monopole couples *strongly*, at a strength of order the inverse of the electric coupling. That is the physical content the biquaternion formulation gathers into a single statement — the phase of the biquaternionic gauge freedom around the string must be trivial, and the charge product is quantised in units of $\hbar c$ accordingly.

The condition is a **re-expression, not a prediction**. It is a statement about the consistency of quantum mechanics in the presence of a magnetic charge; it constrains the product $eg$ given that a monopole exists. It does not assert that any monopole exists, it does not fix $e$ or $g$ individually, and it says nothing about the monopole's mass. It also imports $\hbar$ from outside the algebra: the biquaternion framework is a complexified classical structure, and every step of the derivation above is classical until the single-valuedness of the phase is imposed. The algebra supplies the home for the gauge freedom; quantum mechanics supplies the quantum.

## What the Framework Does Not Say

The temptation with a symmetry this clean is to read a prediction out of it. It is not there, and the gap is worth stating plainly.

- **Existence.** Nothing in the algebra privileges a configuration with $\rho_m \neq 0$ over one with $\rho_m = 0$. The sourced equation accepts magnetic charge; it does not require it. The symmetric system is a larger theory of which the physical one — with $\rho_m \equiv 0$ — is a consistent special case.
- **Mass.** The point monopole has divergent classical self-energy, so the algebra cannot fix a mass. Finite masses come from the mechanism that resolves the core and are model-dependent: the 't Hooft–Polyakov soliton mass is of order $4\pi M_W/g^2$, and grand-unified monopoles are enormous. None of this is in the algebra.
- **Observation.** No magnetic monopole has been observed; the null results bound the monopole flux, not the algebra. The framework is consistent with them because it predicts nothing.
- **Quantum structure.** The qubit operator algebra of $\mathbb{M}_+$ is available, but nothing here couples it to the integer $n$ of the Dirac condition. Whether that integer can be tied to the discrete structure of the informational sector is not addressed and is recorded as open.

The honest summary is that the biquaternion framework is an excellent *language* for the monopole, and that language is a language of reformulation. Whether it can be made to say something new — a mass, a coupling, a selection rule — is the open question.

## Summary

Maxwell's equations with magnetic sources extend the biquaternionic Maxwell equation to

$$
\tilde{\nabla}\tilde{F} = -\tilde{R}_e - i\tilde{R}_m,
\qquad
\tilde{R}_m = \frac{i\rho_m}{\sqrt{\mu}} + \sqrt{\epsilon}\,\mathbf{J}_m,
$$

with the factor of $-i$ placing the magnetic source in the sector complementary to the electric one. The two sources assemble into the single complex source biquaternion $\tilde{\mathcal{R}} = \tilde{R}_e + i\tilde{R}_m$, and the dual field-strength biquaternion is $\tilde{F}_\star = -i\tilde{F}$: Hodge duality is internal multiplication by a scalar phase, not an independent field.

The duality rotation $\tilde{F} \mapsto e^{-i\theta}\tilde{F}$ is generated by a scalar in $\mathbb{C}_{\mathbb{B}}$, commutes with the quaternion units and with every Lorentz rotor, and is therefore an internal $U(1)$ symmetry, not a spacetime one. It rotates the two sectors of the field into one another, and with magnetic sources present it becomes a symmetry of the *sourced* equations, exchanging electric and magnetic charge. That is the structural role of the monopole in this framework.

The static monopole field is $\tilde{F} = -g\hat{\mathbf{x}}/(4\pi\sqrt{\mu}\|\mathbf{x}\|^2)$, a purely real vector in $\mathbb{M}_-$, in contrast with the electric Coulomb field, a purely imaginary vector in $\mathbb{M}_+$. A static monopole has $I_2 = \mathbf{E}\cdot\mathbf{B} = 0$ and $I_1 < 0$; the second pointwise invariant is nonzero only for a dyon. The genuinely "second" quantity is the topological magnetic charge $Q_m \propto \oint_{S^2}\mathbf{B}\cdot d\mathbf{A}$, conserved because it is the integrability condition of the magnetic equation.

The Dirac quantisation condition $eg = 2\pi n\hbar c$ (Heaviside–Lorentz units) emerges from the single-valuedness of the biquaternionic gauge phase around the Dirac string, equivalently $\alpha_m = n^2/(4\alpha)$. It constrains the product of the charges; it does not predict the monopole's existence or mass, and it imports $\hbar$ from quantum mechanics. The framework re-expresses the monopole and its quantisation faithfully, and it is silent where the standard theory is silent.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\mathbb{C}_{\mathbb{B}}, \mathbb{H}_{\mathbb{B}}$ | Scalar subspace, real-quaternion subspace |
| $\mathbb{M}_+, \mathbb{M}_-$ | Hermitian and anti-Hermitian subspaces |
| $\tilde{\nabla}$ | Biquaternionic gradient |
| $\tilde{F} = i\sqrt{\epsilon}\,\mathbf{E} - \sqrt{\mu}\,\mathbf{H}$ | Field-strength biquaternion (pure vector) |
| $\mathbf{E}, \mathbf{H}, \mathbf{B} = \mu\mathbf{H}$ | Electric field, magnetic field, magnetic induction |
| $\epsilon, \mu$ | Permittivity and permeability of the medium |
| $c = 1/\sqrt{\epsilon\mu}$ | Speed of light in the medium |
| $\tilde{F}_\star = -i\tilde{F}$ | Dual field-strength biquaternion |
| $\tilde{R}_e = i\rho_e/\sqrt{\epsilon} + \sqrt{\mu}\,\mathbf{J}_e$ | Electric source biquaternion |
| $\tilde{R}_m = i\rho_m/\sqrt{\mu} + \sqrt{\epsilon}\,\mathbf{J}_m$ | Magnetic source biquaternion |
| $\tilde{\mathcal{R}} = \tilde{R}_e + i\tilde{R}_m$ | Complex source biquaternion |
| $\rho_e, \mathbf{J}_e; \rho_m, \mathbf{J}_m$ | Electric and magnetic charge and current densities |
| $N(\tilde{F}) = -\epsilon(I_1 + 2icI_2)$ | Norm form of the field strength |
| $I_1 = \mathbf{E}^2 - c^2\mathbf{B}^2$ | First invariant (scalar) |
| $I_2 = \mathbf{E}\cdot\mathbf{B}$ | Second invariant (pseudoscalar) |
| $\mathbf{V} = \mathbf{E} + ic\mathbf{B}$ | Riemann–Silberstein vector, $\tilde{F} = i\sqrt{\epsilon}\mathbf{V}$ |
| $g$ | Magnetic charge |
| $Q_m \propto \oint_{S^2}\mathbf{B}\cdot d\mathbf{A}$ | Magnetic (topological) charge |
| $e$ | Electric charge |
| $n \in \mathbb{Z}$ | Winding number in the Dirac condition |
| $\alpha, \alpha_m$ | Electric and magnetic fine-structure constants |

## Further Reading

- P. A. M. Dirac, "Quantised singularities in the electromagnetic field", *Proceedings of the Royal Society A* 133 (1931) 60–72, for the original derivation of the quantisation condition.
- G. 't Hooft, "Magnetic monopoles in unified gauge theories", *Nuclear Physics B* 79 (1974) 276–284, for the finite-mass monopole of a spontaneously broken gauge theory.
- A. M. Polyakov, "Particle spectrum in quantum field theory", *JETP Letters* 20 (1974) 194–195, for the independent soliton construction.
- J. Preskill, "Magnetic monopoles", *Annual Review of Nuclear and Particle Science* 34 (1984) 461–530, for the cosmological and experimental status of monopoles.
- Y. M. Shnir, *Magnetic Monopoles* (Springer, 2005), for a systematic account of monopole theory.
- E. Witten, "Dyons of charge $e\theta/2\pi$", *Physics Letters B* 86 (1979) 283–287, for the interplay of the pseudoscalar invariant and magnetic charge.
- J. D. Jackson, *Classical Electrodynamics* (Wiley, 1999), for the standard treatment of Maxwell's equations with magnetic sources and of the Dirac condition.
- Iwo Białynicki-Birula and Zofia Białynicka-Birula, "The role of the Riemann–Silberstein vector in classical and quantum theories of electromagnetism", *Journal of Physics A* 46 (2013) 053001, for the complex-vector and duality structure.
- Ludwik Silberstein, "Elektromagnetische Grundgleichungen in bivektorieller Behandlung", *Annalen der Physik* 22 (1907) 579–586, for the original complex-vector formulation of the electromagnetic field.
