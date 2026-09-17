
# __Relativistic Mechanics in Biquaternionic Form__

## Introduction

The equations of relativistic mechanics — the four-position, the invariant interval, the four-velocity, the four-momentum, the mass-shell relation, the four-force, the action, the conserved current, and the relativistic wave equations — are usually written in the language of four-vectors and Minkowski tensors. This article expresses them in the biquaternion algebra $\mathbb{B} = \mathbb{C} \otimes_\mathbb{R} \mathbb{H}$, using the $ict$ convention in which the complex time coordinate absorbs the minus sign of the Minkowski metric.

The purpose is not to derive new physics. The purpose is to rewrite the established equations of relativistic mechanics in the biquaternion language, so that the algebraic structure of the theory is manifest. The biquaternion formulation makes the following structural facts explicit:

- The invariant interval is the **square of a biquaternion**.
- The four-velocity and four-momentum are **biquaternions of the anti-Hermitian subspace** $\mathbb{M}_-$.
- The mass-shell relation is the statement that the **norm form** of the four-momentum is a fixed negative constant.
- The conserved current is characterized by the **scalar part of the quaternion-conjugate gradient** vanishing.

These identities are algebraic, not physical. They are the reason the biquaternion algebra is the natural home of relativistic mechanics.

The conventions are those of the companion articles: the biquaternion algebra is $\mathbb{B} = \mathbb{C} \otimes_\mathbb{R} \mathbb{H}$, the quaternion basis is $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$, the scalar imaginary is $i$, and the biquaternionic gradient is $\tilde{\nabla} = e_0 \partial_{ict} + e_1 \partial_x + e_2 \partial_y + e_3 \partial_z$. Its quaternion conjugate is $\bar{\tilde{\nabla}} = e_0 \partial_{ict} - e_1 \partial_x - e_2 \partial_y - e_3 \partial_z$. The Minkowski metric has signature $(-,+,+,+)$, so that $\partial_{ict}^2 = -\partial_t^2/c^2$. Throughout, the symbol $c$ denotes the **speed of light in the medium**, $c = 1/\sqrt{\epsilon\mu}$, and $c_0$ denotes the **vacuum speed of light**, $c_0 = 1/\sqrt{\epsilon_0\mu_0}$. In vacuum, $c = c_0$. The symbol $v$ (or $\mathbf{v}$) is reserved for particle and frame velocities.

## The Four-Position

The **four-position biquaternion** is

$$
\tilde{X} = ic\,t\,e_0 + x\,e_1 + y\,e_2 + z\,e_3,
$$

where $t \in \mathbb{R}$ is the ordinary time coordinate, $x, y, z \in \mathbb{R}$ are the ordinary spatial coordinates, and $c$ is the speed of light in the medium. The scalar part of $\tilde{X}$ is the complex time coordinate $ict$, and the vector part is the spatial position $\mathbf{x} = x\,e_1 + y\,e_2 + z\,e_3$. In compact form,

$$
\tilde{X} = ic\,t\,e_0 + \mathbf{x}.
$$

The four-position biquaternion lives in the **anti-Hermitian subspace** $\mathbb{M}_-$ (imaginary scalar part, real vector part), matching the structure of the four-vector $x^\mu = (ict, \mathbf{x})$ in the $ict$ convention.

## The Invariant Interval

The **invariant interval** is the square of the biquaternion displacement:

$$
ds^2 = d\tilde{X} \circ d\tilde{X} = (ic\,dt)^2 + dx^2 + dy^2 + dz^2 = -c^2\,dt^2 + d\mathbf{x}^2.
$$

This is the biquaternion form of the Minkowski interval. The minus sign in the time–time component arises algebraically from $i^2 = -1$, not from an independently postulated metric signature. The biquaternion formulation makes the **algebraic origin of the Lorentzian signature** explicit.

Two quadratic forms are used in this article and its companions: the **square** $\tilde{Q} \circ \tilde{Q}$ (used here for the interval), and the **norm form** $\tilde{Q}\bar{\tilde{Q}}$ (used for the four-velocity and four-momentum normalizations). For an element of the anti-Hermitian subspace $\mathbb{M}_-$, the two differ by the sign of the vector part: $\tilde{Q} \circ \tilde{Q} = (Q_0)^2 + \mathbf{Q}^2$, while $\tilde{Q}\bar{\tilde{Q}} = (Q_0)^2 - \mathbf{Q}^2$. The interval uses the square; the normalizations use the norm form.

The interval is invariant under the Lorentz group, which in the biquaternion framework is the group of **rotor conjugations** (see the companion article on the Lorentz transformation).

## The Four-Velocity

The **four-velocity biquaternion** of a particle with velocity $\mathbf{v}$ is

$$
\tilde{U} = \gamma\left(ic\,e_0 + \mathbf{v}\right),
$$

where

$$
\gamma = \frac{1}{\sqrt{1 - \mathbf{v}^2/c^2}}
$$

is the Lorentz factor. The scalar part of $\tilde{U}$ is **imaginary** ($i\gamma c$) and the vector part is **real** ($\gamma\mathbf{v}$), so $\tilde{U}$ lies in the anti-Hermitian subspace $\mathbb{M}_-$, like the four-position. In compact form,

$$
\tilde{U} = ic\,\gamma\,e_0 + \gamma\mathbf{v}.
$$

The four-velocity satisfies the **normalization condition**

$$
\tilde{U}\bar{\tilde{U}} = \gamma^2\left(-c^2 + \mathbf{v}^2\right) = -c^2,
$$

which is the biquaternion form of the standard relativistic normalization $u^\mu u_\mu = -c^2$. The normalization is the statement that the four-velocity has a **fixed negative norm** determined by the speed of light. It is a **constraint**, not an identity: not every biquaternion satisfies it, only the four-velocities of physical particles.

## The Four-Momentum

The **four-momentum biquaternion** is

$$
\tilde{P} = m\tilde{U} = \gamma m\left(ic\,e_0 + \mathbf{v}\right) = i\frac{E}{c}\,e_0 + \mathbf{p},
$$

where $m$ is the rest mass, $E = \gamma m c^2$ is the relativistic energy, and $\mathbf{p} = \gamma m\mathbf{v}$ is the relativistic three-momentum. The scalar part of $\tilde{P}$ is $iE/c$ and the vector part is $\mathbf{p}$, so $\tilde{P}$ also lies in the anti-Hermitian subspace $\mathbb{M}_-$.

## The Mass-Shell Relation

The four-momentum satisfies the **mass-shell relation**

$$
\tilde{P}\bar{\tilde{P}} = m^2 \tilde{U}\bar{\tilde{U}} = -m^2 c^2.
$$

Expanding in components,

$$
\tilde{P}\bar{\tilde{P}} = \left(i\frac{E}{c}\right)^2 + \mathbf{p}^2 = -\frac{E^2}{c^2} + \mathbf{p}^2 = -m^2 c^2,
$$

which is the standard relativistic energy–momentum relation

$$
E^2 = \mathbf{p}^2 c^2 + m^2 c^4.
$$

The mass-shell relation is the **constraint that defines the physical four-momenta**. In the biquaternion language, it is the statement that the **norm form of the four-momentum is a fixed negative constant**, determined by the rest mass and the speed of light. Particles of different masses lie on different shells (different values of $\tilde{P}\bar{\tilde{P}}$); massless particles lie on the **null shell** $\tilde{P}\bar{\tilde{P}} = 0$, corresponding to the light cone.

## The Four-Force

The **four-force biquaternion** is the proper-time derivative of the four-momentum:

$$
\tilde{F} = \frac{d\tilde{P}}{d\tau},
$$

where $\tau$ is the **proper time** of the particle, defined by $d\tau = dt/\gamma$. The four-force biquaternion lies in the anti-Hermitian subspace $\mathbb{M}_-$, like $\tilde{P}$.

Since $\tilde{P}\bar{\tilde{P}} = -m^2 c^2$ is constant along the worldline, differentiating gives

$$
\tilde{F}\bar{\tilde{P}} + \tilde{P}\bar{\tilde{F}} = 0,
$$

which is the biquaternion form of the standard orthogonality condition $f^\mu p_\mu = 0$: the four-force is orthogonal to the four-momentum. This is the reason the four-force can change the direction of the four-momentum but not its norm, and hence not the rest mass.

For a charged particle in an electromagnetic field, the four-force in component form is

$$
\tilde{F} = i\gamma\frac{q}{c}\left(\mathbf{E}\cdot\mathbf{v}\right)e_0 + \gamma q\left(\mathbf{E} + \mathbf{v}\times\mathbf{B}\right),
$$

where $q$ is the charge, $\mathbf{E}$ and $\mathbf{B}$ are the electric and magnetic fields, and $\mathbf{v}$ is the particle velocity. The scalar part is the **power** delivered to the particle (imaginary, as required by the $ict$ convention for a four-vector), and the vector part is the **relativistic three-force** $\gamma q(\mathbf{E} + \mathbf{v}\times\mathbf{B})$.

**Note on the biquaternion expression.** The component formula above is standard and unambiguous. The expression of the same four-force as a **biquaternion product** of the field-strength biquaternion $\tilde{F}_{\text{EM}}$ and the four-velocity $\tilde{U}$ is **not** simply the real part of $\tilde{F}_{\text{EM}}\circ\tilde{U}$; the correct expression involves the representation theory of $\mathbb{B}$ in the even subalgebra of $\mathrm{Cl}_{1,3}$, and it needs to be worked out carefully. This is left as an open question, to be addressed when the relevant literature on the biquaternion formulation of the Lorentz force is reviewed. The structural fact — that the four-force is an element of $\mathbb{M}_-$ built from the field strength and the four-velocity — is correct; the explicit formula in terms of $\tilde{F}_{\text{EM}}$ and $\tilde{U}$ is deferred.

## The Action

The **relativistic action** for a free particle of rest mass $m$ is

$$
S = -mc\int\sqrt{-d\tilde{X} \circ d\tilde{X}},
$$

where the square root is the ordinary real square root of the positive quantity $-d\tilde{X} \circ d\tilde{X} = c^2\,dt^2 - d\mathbf{x}^2 = c^2\,d\tau^2$. Since $d\tau = dt/\gamma$, we have $c\,d\tau = c\,dt/\gamma$, and the action becomes

$$
S = -mc^2\int\frac{dt}{\gamma} = -mc^2\int\sqrt{1 - \mathbf{v}^2/c^2}\,dt,
$$

which is the standard relativistic action. The biquaternion form makes the **invariant character** of the action manifest: the integrand is built from the biquaternion interval, which is a Lorentz scalar.

## The Conserved Current

The **four-current biquaternion** is

$$
\tilde{J} = ic\,\rho\,e_0 + \mathbf{j},
$$

where $\rho$ is the charge density and $\mathbf{j}$ is the current density. The current biquaternion lies in $\mathbb{M}_-$ (imaginary scalar part, real vector part). The **conservation of charge** is expressed by the biquaternion equation

$$
\mathrm{Sc}\!\left(\bar{\tilde{\nabla}}\tilde{J}\right) = 0,
$$

where $\bar{\tilde{\nabla}} = e_0\partial_{ict} - e_1\partial_x - e_2\partial_y - e_3\partial_z$ is the quaternion conjugate of the biquaternionic gradient. Expanding the scalar part,

$$
\mathrm{Sc}\!\left(\bar{\tilde{\nabla}}\tilde{J}\right) = \partial_{ict}(ic\rho) + \mathrm{div}\,\mathbf{j} = \frac{\partial \rho}{\partial t} + \mathrm{div}\,\mathbf{j},
$$

so the condition is the standard continuity equation

$$
\frac{\partial \rho}{\partial t} + \mathrm{div}\,\mathbf{j} = 0.
$$

The condition is the **scalar part** of $\bar{\tilde{\nabla}}\tilde{J} = 0$. The full equation $\bar{\tilde{\nabla}}\tilde{J} = 0$ is stronger, because the vector part of $\bar{\tilde{\nabla}}\tilde{J}$ does not vanish in general: it involves the spatial derivatives of $\rho$ and $\mathbf{j}$, and it does not correspond to a standard physical conservation law. So the continuity equation is the scalar projection of the biquaternion conservation law.

## The Klein–Gordon Equation

The **Klein–Gordon equation** for a relativistic scalar field $\tilde{\Phi}$ of mass $m$ is

$$
\left(\tilde{\nabla}\bar{\tilde{\nabla}} - \frac{m^2 c^2}{\hbar^2}\right)\tilde{\Phi} = 0.
$$

Here $\tilde{\nabla}\bar{\tilde{\nabla}} = \Box = \partial_{ict}^2 + \Delta$ is the d'Alembertian in the biquaternion form, and $\hbar$ is the reduced Planck constant. Expanding,

$$
\Box\tilde{\Phi} = \frac{m^2 c^2}{\hbar^2}\tilde{\Phi},
$$

which is the standard Klein–Gordon equation $(\Box - m^2 c^2/\hbar^2)\phi = 0$ with $\Box = -\partial_t^2/c^2 + \Delta$. The biquaternion form is compact and manifestly Lorentz-covariant.

## The Dirac Equation

The **Dirac equation** for a relativistic spinor field $\tilde{\Psi}$ of mass $m$ is

$$
\tilde{\nabla}\tilde{\Psi} = m\tilde{\Psi}^\flat,
$$

where $\tilde{\Psi}^\flat = -\tilde{\Psi}^\dagger$ is the anti-Hermitian conjugate of $\tilde{\Psi}$. In the massless case ($m = 0$), the equation reduces to

$$
\tilde{\nabla}\tilde{\Psi} = 0,
$$

which is identical in form to the source-free biquaternion Maxwell equation. The massive case includes the mass term $m\tilde{\Psi}^\flat$, which is the biquaternion form of the standard Dirac mass term. The full treatment of the Dirac equation in biquaternionic form is given in the companion article.

## Summary of the Ten Formulas

| Quantity | Biquaternion formula | Constraint |
|---|---|---|
| Four-position | $\tilde{X} = ic\,t\,e_0 + \mathbf{x}$ | — |
| Invariant interval | $ds^2 = d\tilde{X} \circ d\tilde{X}$ | $= -c^2 dt^2 + d\mathbf{x}^2$ |
| Four-velocity | $\tilde{U} = \gamma(ic\,e_0 + \mathbf{v})$ | $\tilde{U}\bar{\tilde{U}} = -c^2$ |
| Four-momentum | $\tilde{P} = m\tilde{U}$ | $\tilde{P}\bar{\tilde{P}} = -m^2 c^2$ |
| Mass-shell relation | $\tilde{P}\bar{\tilde{P}} = -m^2 c^2$ | — |
| Four-force | $\tilde{F} = d\tilde{P}/d\tau$ | $\tilde{F}\bar{\tilde{P}} + \tilde{P}\bar{\tilde{F}} = 0$ |
| Action | $S = -mc\int\sqrt{-d\tilde{X}\circ d\tilde{X}}$ | — |
| Current | $\tilde{J} = ic\rho\,e_0 + \mathbf{j}$ | $\mathrm{Sc}(\bar{\tilde{\nabla}}\tilde{J}) = 0$ |
| Klein–Gordon | $(\tilde{\nabla}\bar{\tilde{\nabla}} - m^2c^2/\hbar^2)\tilde{\Phi} = 0$ | — |
| Dirac | $\tilde{\nabla}\tilde{\Psi} = m\tilde{\Psi}^\flat$ | — |

## Structural Observations

**The four-vectors live in $\mathbb{M}_-$.** The four-position, four-velocity, four-momentum, four-force, four-potential, and four-current all lie in the anti-Hermitian subspace $\mathbb{M}_-$ (imaginary scalar part, real vector part). This subspace is the biquaternion image of the Minkowski four-vector space, and it is closed under the natural Lorentz-covariant operations (addition, scalar multiplication by real numbers, and rotor conjugation).

**The mass-shell relation is a norm condition.** The statement $\tilde{P}\bar{\tilde{P}} = -m^2 c^2$ is the statement that the **norm form** of the four-momentum is a fixed negative constant. Massless particles satisfy $\tilde{P}\bar{\tilde{P}} = 0$, which is the condition that the four-momentum lies on the **zero divisor cone** of the algebra (see the companion article on biquaternion zero divisors). So the light cone of Minkowski space is, in the biquaternion language, the **zero divisor set** of the algebra.

**The conserved current is a scalar projection of the biquaternion conservation law.** The continuity equation is the scalar part of $\bar{\tilde{\nabla}}\tilde{J} = 0$. The full biquaternion equation is stronger, and the vector part of $\bar{\tilde{\nabla}}\tilde{J}$ does not have an independent physical interpretation as a conservation law.

**The wave equations are factorization.** The Klein–Gordon and Dirac equations are related by the factorization $\tilde{\nabla}\bar{\tilde{\nabla}} = \Box$. The Dirac equation is the **first-order factor** of the Klein–Gordon equation, and the mass term is the term that distinguishes the massive case from the massless one. This factorization is the biquaternion form of the standard Dirac factorization of the Klein–Gordon operator.

## Open Questions

1. **The Lorentz transformation of four-vectors.** The four-vectors in $\mathbb{M}_-$ transform under the Lorentz group by a **rotor conjugation** involving the boost biquaternion. The precise form of this transformation, and its relation to the standard four-vector transformation, is the subject of the companion article on the Lorentz transformation.

2. **The Lorentz force in biquaternion form.** The four-force in component form is standard: $\tilde{F} = i\gamma q(\mathbf{E}\cdot\mathbf{v})/c\,e_0 + \gamma q(\mathbf{E} + \mathbf{v}\times\mathbf{B})$. Its expression as a biquaternion product of the field-strength biquaternion $\tilde{F}_{\text{EM}}$ and the four-velocity $\tilde{U}$ is **not** simply the real part of $\tilde{F}_{\text{EM}}\circ\tilde{U}$; the correct expression involves the representation theory of $\mathbb{B}$ in the even subalgebra of $\mathrm{Cl}_{1,3}$, and it remains to be worked out cleanly. This is left for a future revision, and it may be addressed by the scientific literature on the biquaternion formulation of the Lorentz force.

3. **The Lagrangian formulation.** The biquaternion action $S = -mc\int\sqrt{-d\tilde{X}\circ d\tilde{X}}$ is a real Lorentz scalar. Can the full Lagrangian formulation of relativistic mechanics (including interactions) be expressed in biquaternion form?

4. **The Hamiltonian formulation.** The biquaternion form of the relativistic Hamiltonian and the associated Hamilton equations have not been developed.

5. **Field-theoretic generalizations.** The biquaternion mechanics presented here describes a single particle. How does the formulation extend to fields and to many-particle systems?

6. **Quantization.** The biquaternion framework is classical. How does it extend to the quantized theory, and what is the role of the biquaternion algebra in quantization?

These questions are open.

## Summary

The ten basic formulas of relativistic mechanics — four-position, invariant interval, four-velocity, four-momentum, mass-shell relation, four-force, action, current, Klein–Gordon, and Dirac — can all be expressed in the biquaternion algebra $\mathbb{B}$ using the $ict$ convention. The biquaternion formulation makes the following structural facts explicit:

- The invariant interval is the square of the four-position biquaternion.
- The four-velocity, four-momentum, four-force, four-potential, and four-current lie in the anti-Hermitian subspace $\mathbb{M}_-$.
- The mass-shell relation is the norm-form condition $\tilde{P}\bar{\tilde{P}} = -m^2 c^2$.
- The light cone is the zero divisor set of the algebra.
- The conserved current is characterized by the scalar part of the quaternion-conjugate gradient vanishing.
- The wave equations are the factorization of the d'Alembertian.

These identities are algebraic, not physical. They are the reason the biquaternion algebra is the natural home of relativistic mechanics, and they are the starting point for the biquaternion formulation of Lorentz transformations, fields, and interactions developed in the companion articles. The biquaternion expression of the Lorentz force remains to be worked out and is flagged as an open question.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra |
| $\mathbb{M}_-$ | Anti-Hermitian subspace (four-vectors) |
| $c = 1/\sqrt{\epsilon\mu}$ | Speed of light in the medium |
| $c_0 = 1/\sqrt{\epsilon_0\mu_0}$ | Speed of light in vacuum |
| $\mathbf{v}$ | Particle three-velocity |
| $\gamma = 1/\sqrt{1 - \mathbf{v}^2/c^2}$ | Lorentz factor |
| $\tilde{X} = ict\,e_0 + \mathbf{x}$ | Four-position biquaternion |
| $\tilde{U} = \gamma(ic\,e_0 + \mathbf{v})$ | Four-velocity biquaternion |
| $\tilde{P} = m\tilde{U}$ | Four-momentum biquaternion |
| $\tilde{F} = d\tilde{P}/d\tau$ | Four-force biquaternion |
| $\tilde{J} = ic\rho\,e_0 + \mathbf{j}$ | Four-current biquaternion |
| $\tilde{\nabla} = e_0\partial_{ict} + \sum_k e_k\partial_k$ | Biquaternionic gradient |
| $\bar{\tilde{\nabla}} = e_0\partial_{ict} - \sum_k e_k\partial_k$ | Quaternion-conjugate gradient |
| $\Box = \tilde{\nabla}\bar{\tilde{\nabla}}$ | d'Alembertian |
| $\tau$ | Proper time |
| $m$ | Rest mass |

## Further Reading

- Albert Einstein, "Zur Elektrodynamik bewegter Körper," *Annalen der Physik* **17** (1905) 891–921, for the original special relativity.
- Hermann Minkowski, "Space and Time" (1908), reprinted in *The Principle of Relativity* (Dover), for the four-dimensional formulation.
- Lev Landau and Evgeny Lifshitz, *The Classical Theory of Fields* (Pergamon, 1975), for the standard relativistic mechanics.
- J. D. Jackson, *Classical Electrodynamics* (Wiley, 1999), for the standard four-vector formulation.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the geometric algebra formulation of relativistic mechanics.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the modern geometric algebra treatment.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the connection to Clifford algebras.
- L. A. Alexeyeva, "Differential algebra of biquaternions. Dirac equation and its generalized solutions," *Progress in Analysis, Proceedings of the 8th Congress of the ISAAC* (Moscow, 2013), pp. 153–161, for the biquaternion formulation of relativistic wave equations.

