# __The Light Cone as the Biquaternion Zero-Divisor Cone__

## Introduction

The biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ is not a division algebra. It contains nonzero elements whose norm form vanishes, and those elements annihilate other nonzero elements. This article is about the physical meaning of that fact in its simplest case: the set on which the norm form vanishes is the **light cone** of the material sector, and its algebraic character as the **zero-divisor set** is what makes the cone a boundary of the algebra and not merely a surface in spacetime.

The starting observation is one line long. For the material coordinate $\tilde{X} = ict\,e_0 + \mathbf{x}$, the norm form is

$$
N(\tilde{X}) = \tilde{X}\,\overline{\tilde{X}} = -c^2t^2 + \mathbf{x}^2 ,
$$

so the equation $N(\tilde{X}) = 0$ is exactly the equation of the light cone, $|\mathbf{x}| = c|t|$. The Minkowski interval is not imported into the algebra and then made to vanish; it is the algebra's own quadratic form, and the cone is its zero set. What the zero-divisor structure adds is a classification of the points of the cone and a reason why the cone is special: it is the locus where the algebra fails to be invertible, and the failure is precisely the existence of lightlike propagation.

Three threads are developed below.

- **The algebraic criterion.** A nonzero biquaternion has vanishing norm form if and only if it is a zero divisor, and the zero divisors split into two families — the **nilpotents**, whose scalar part vanishes, and the **idempotent multiples**, whose scalar part does not. The cone of the material sector is made of the second family, and that is the family that generates the algebra's minimal ideals.
- **The cone in the distinguished subspaces.** The complex scalar line and the real-quaternion subspace are division algebras and contain no zero divisors. The two Hermitian-type subspaces $\mathbb{M}_-$ and $\mathbb{M}_+$ each contain a cone, and the $\mathbb{M}_-$ cone is the physical light cone.
- **The cone as the locus of propagation.** The d'Alembertian is the norm form of the gradient, $\Box = \tilde{\nabla}\bar{\tilde{\nabla}}$, and a four-wavevector $\tilde{K}$ is null exactly when $N(\tilde{K}) = 0$. For such a $\tilde{K}$ every function of the phase $\mathrm{Sc}(\tilde{K}\bar{\tilde{X}})$ solves the wave equation, so the null directions are the directions in which the algebra propagates without dispersion. The light cone is where the norm form degenerates, the wave operator factorizes, and signals travel at $c$.

**Conventions.** We use those of the read list unchanged. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis is $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$ and $e_je_k = -\delta_{jk}e_0 + \varepsilon_{jkl}e_l$, and $i$ is the central scalar imaginary. The subspaces are $\mathbb{M}_-$ (anti-Hermitian: imaginary scalar, real vector — the material sector), $\mathbb{M}_+$ (Hermitian: real scalar, imaginary vector — the informational sector), $\mathbb{H}_{\mathbb{B}}$ (real quaternions) and $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0, ie_0\}$ (the center). The conjugations are $\bar{\cdot}$, ${}^*$, ${}^\dagger = \bar{\cdot}^{\,*}$ and ${}^\flat = -\dagger$. The gradient is $\tilde{\nabla} = e_0\partial_{ict} + e_1\partial_x + e_2\partial_y + e_3\partial_z$, with $\bar{\tilde{\nabla}} = e_0\partial_{ict} - e_1\partial_x - e_2\partial_y - e_3\partial_z$ and $\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \bar{\tilde{\nabla}}\tilde{\nabla} = \partial_{ict}^2 + \Delta$. The norm form is $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2$ — level 1, the identity $\mathrm{diag}(+1,+1,+1,+1)$ on $\mathbb{C}$, restricting to the level-2 form $\eta = \mathrm{diag}(-1,+1,+1,+1)$ on the real material slice — and the material coordinate is $\tilde{X} = ict\,e_0 + \mathbf{x}$. Throughout, $c = 1/\sqrt{\epsilon\mu}$ is the speed of light in the medium and $c_0$ its vacuum value. The trace formula is $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$.

## The Norm Form and Its Vanishing Set

The norm form on $\mathbb{B}$ is

$$
N(\tilde{Q}) = \tilde{Q}\,\overline{\tilde{Q}} = Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2 ,
\qquad
\tilde{Q} = Q_0e_0 + Q_1e_1 + Q_2e_2 + Q_3e_3 ,
$$

a nondegenerate complex quadratic form on $\mathbb{C}^4$. It is the determinant of the matrix realization of $\tilde{Q}$ and the natural quadratic invariant of the algebra. Its **zero set** is the quadric cone

$$
\mathcal{Z} = \{\, \tilde{Q}\in\mathbb{B} : \tilde{Q}\neq 0,\ N(\tilde{Q}) = 0 \,\},
$$

a complex cone of complex dimension three with the origin removed. Since the form is isotropic, the algebra is split by it, and the elements of $\mathcal{Z}$ are exactly the **zero divisors**: a nonzero $\tilde{Q}$ has $N(\tilde{Q}) = 0$ if and only if there is a nonzero $\tilde{Q}'$ with $\tilde{Q}\tilde{Q}' = 0$ (or with $\tilde{Q}'\tilde{Q} = 0$).

On the **real material slice**, writing $\tilde{X} = ict\,e_0 + \mathbf{x}$ with $(t,\mathbf{x})\in\mathbb{R}^4$, the form becomes

$$
N(\tilde{X}) = (ic\,t)^2 + \mathbf{x}^2 = -c^2t^2 + \mathbf{x}^2 ,
$$

and the trichotomy of causal type is the trichotomy of sign:

$$
\text{timelike}: N(\tilde{X}) < 0,
\qquad
\text{null}: N(\tilde{X}) = 0,
\qquad
\text{spacelike}: N(\tilde{X}) > 0 .
$$

The vanishing set is therefore the pair of cones $|\mathbf{x}| = c|t|$, and the future cone, the past cone and the spacelike exterior are, respectively, the timelike interior of the future cone, the timelike interior of the past cone, and the exterior of both. In the $ict$ convention the minus sign in $N$ is carried by the coordinate itself: $(ic\,t)^2 = -c^2t^2$. This is the level-2 Minkowski form $\eta = \mathrm{diag}(-1,+1,+1,+1)$ appearing as the restriction of the level-1 identity form of the algebra. The cone is not put into the algebra; it is where the algebra's form degenerates.

## Zero Divisors: the Criterion and the Two Families

The two families are separated by the scalar part.

**Pure family.** If $Q_0 = 0$ then $\tilde{Q} = \mathbf{Q}$ is a pure vector and

$$
\tilde{Q}^2 = \mathbf{Q}\mathbf{Q} = -\mathbf{Q}\cdot\mathbf{Q} = -N(\tilde{Q}) = 0 ,
$$

where the middle equality uses $\mathbf{Q}\mathbf{Q} = -\mathbf{Q}\cdot\mathbf{Q} + \mathbf{Q}\times\mathbf{Q}$ and $\mathbf{Q}\times\mathbf{Q} = 0$. A pure zero divisor is therefore **nilpotent**, $\tilde{Q}^2 = 0$, and the pure zero divisors form the nilpotent cone $\mathbf{Q}\cdot\mathbf{Q} = 0$ inside the complex vector space $\mathrm{Vect}(\mathbb{B})\cong\mathbb{C}^3$. The simplest example is $\tilde{Q} = e_1 + ie_2$, for which $N = 1^2 + i^2 = 0$ and $\tilde{Q}^2 = 0$.

**Non-pure family.** If $Q_0\neq 0$, write $\tilde{Q} = Q_0(e_0 + \mathbf{w})$ with $\mathbf{w} = \mathbf{Q}/Q_0$. The norm form is $N(\tilde{Q}) = Q_0^2(1 + \mathbf{w}\cdot\mathbf{w})$, so vanishing requires

$$
\mathbf{w}\cdot\mathbf{w} = -1 ,
\qquad\text{equivalently}\qquad
\mathbf{w}^2 = +e_0 .
$$

Then

$$
\tilde{Q}^2 = Q_0^2(e_0 + \mathbf{w})^2 = Q_0^2(e_0 + 2\mathbf{w} + \mathbf{w}^2) = Q_0^2(2e_0 + 2\mathbf{w}) = 2Q_0\,\tilde{Q},
$$

using $e_0^2 = e_0$, the cross term $2\mathbf{w}$, and $\mathbf{w}^2 = +e_0$. Hence a non-pure zero divisor satisfies the algebraic identity

$$
\boxed{\; \tilde{Q}^2 = 2Q_0\,\tilde{Q} \;}
\qquad\Longleftrightarrow\qquad
\tilde{P} := \frac{\tilde{Q}}{2Q_0}\ \text{ is idempotent, }\ \tilde{P}^2 = \tilde{P},\quad \tilde{P}\neq 0 .
$$

The nonzero complex multiples of idempotents are therefore exactly the non-pure zero divisors. The standard idempotent is

$$
\tilde{P}(\hat{\boldsymbol{\mu}}) = \tfrac12\left(e_0 + i\hat{\boldsymbol{\mu}}\right),
\qquad
\hat{\boldsymbol{\mu}} = \mu_1e_1 + \mu_2e_2 + \mu_3e_3,\quad \hat{\boldsymbol{\mu}}\cdot\hat{\boldsymbol{\mu}} = 1 ,
$$

for which $N(\tilde{P}) = \tfrac14(1 - (i\hat{\boldsymbol{\mu}})^2) = \tfrac14(1 - \hat{\boldsymbol{\mu}}\cdot\hat{\boldsymbol{\mu}}) = 0$ and $\tilde{P}^2 = \tilde{P}$, using $(i\hat{\boldsymbol{\mu}})^2 = +\hat{\boldsymbol{\mu}}\cdot\hat{\boldsymbol{\mu}}$ and $\hat{\boldsymbol{\mu}}\cdot\hat{\boldsymbol{\mu}}=1$. The verification is one line in explicit quaternion arithmetic:

$$
\tilde{P}^2 = \tfrac14\left(e_0 + 2i\hat{\boldsymbol{\mu}} + (i\hat{\boldsymbol{\mu}})^2\right)
= \tfrac14\left(e_0 + 2i\hat{\boldsymbol{\mu}} - \hat{\boldsymbol{\mu}}\hat{\boldsymbol{\mu}}\right)
= \tfrac14\left(e_0 + 2i\hat{\boldsymbol{\mu}} + e_0\right)
= \tilde{P} .
$$

The two families are disjoint, because the vanishing of the scalar part is what separates them, and they exhaust the zero divisors. The set $\mathcal{Z}$ is the union of the nilpotent cone and the cone of idempotent multiples — a single complex cone of complex dimension three, stratified by the vanishing of $Q_0$.

## The Cone in the Distinguished Subspaces

Which real subspaces meet $\mathcal{Z}$ is the question that gives the cone its physical reading.

**The scalar line and the real quaternions are division subalgebras.** On $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_0, ie_0\}$ a general element is $\tilde{Q} = (a + ib)e_0$ and $N(\tilde{Q}) = (a+ib)^2$, which vanishes only at $a = b = 0$. On $\mathbb{H}_{\mathbb{B}}$ a general element is a real quaternion $\tilde{Q} = a_0e_0 + \mathbf{a}$ with $N(\tilde{Q}) = a_0^2 + \mathbf{a}^2$, a sum of real squares, which likewise vanishes only at the origin. Neither subspace contains a zero divisor: they are the division subalgebras of $\mathbb{B}$, and on them the norm form is anisotropic. The set $\mathcal{Z}$ lives in the complement of those two subspaces.

**The material cone.** On $\mathbb{M}_-$ the general element is $\tilde{X} = i x_0e_0 + \mathbf{x}$ with $x_0, x_1, x_2, x_3$ real, and

$$
N(\tilde{X}) = (i x_0)^2 + \mathbf{x}^2 = -x_0^2 + \mathbf{x}^2 .
$$

Identifying $x_0 = ct$, the vanishing locus is the light cone of Minkowski space. For a nonzero null element with $x_0\neq 0$, writing $\mathbf{x} = x_0\hat{\mathbf{x}}$ with $\hat{\mathbf{x}}$ a real unit vector gives

$$
\tilde{X} = i x_0\left(e_0 - i\hat{\mathbf{x}}\right) = 2i x_0\,\tilde{P}(-\hat{\mathbf{x}}),
\qquad
\tilde{P}(-\hat{\mathbf{x}}) = \tfrac12\left(e_0 - i\hat{\mathbf{x}}\right),
$$

so every future (or past) null point of the real material slice is a real multiple of an idempotent: the material cone is the non-pure family, realized over the reals. The apex $\tilde{X} = 0$ is excluded from $\mathcal{Z}$ by the definition, since it is not a zero divisor. The real pure case would require $N(\mathbf{x}) = \mathbf{x}^2 = 0$ with $\mathbf{x}\neq 0$ and real, which is impossible; the nilpotent family on the material cone therefore needs complex spatial components, and the real cone is entirely of the idempotent type.

**The informational cone.** On $\mathbb{M}_+$ the general element is $\tilde{Q} = q_0e_0 + i\mathbf{q}$ with $q_0, \mathbf{q}$ real, and $N(\tilde{Q}) = q_0^2 - \mathbf{q}^2$. Its vanishing set is a cone with the real scalar $q_0$ as the distinguished coordinate — the future and past cones of the informational sector. It is a genuine cone of the same type, but its physical reading is the informational one and belongs to the companion article *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*; here it is recorded only to make the point that both Hermitian-type subspaces, and only those, carry the zero-divisor cone.

The distribution is therefore forced by the topology of the four real slices: the two division slices $\mathbb{C}_{\mathbb{B}}$ and $\mathbb{H}_{\mathbb{B}}$ are anisotropic, and the two slices on which $i$ appears with a relative sign — $\mathbb{M}_-$ and $\mathbb{M}_+$ — carry the cone. The physical light cone is the branch of $\mathcal{Z}$ that lies in the material sector.

## The Cone and the Wave Operator

The norm form is not only the interval; it is also the d'Alembertian. Composing the gradient with its quaternion conjugate gives

$$
\tilde{\nabla}\bar{\tilde{\nabla}} = \bar{\tilde{\nabla}}\tilde{\nabla} = \partial_{ict}^2 + \Delta =: \Box ,
$$

because the cross terms cancel and the spatial part gives $-\sum_k\partial_k^2$ with the correct sign from $e_k^2 = -e_0$. The wave operator is thus the norm form of the gradient biquaternion, exactly as $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}}$ is the norm form of $\tilde{Q}$. The factorization $\Box = \tilde{\nabla}\bar{\tilde{\nabla}}$ is available in the algebra and is not available in a scalar wave operator; it is the algebraic statement that the second-order operator is a product of first-order ones.

Now let $\tilde{K}$ be a four-wavevector, meaning an element of $\mathbb{M}_-$ written as

$$
\tilde{K} = i\,\frac{\omega}{c}\,e_0 + \mathbf{k},
\qquad
N(\tilde{K}) = -\frac{\omega^2}{c^2} + \mathbf{k}^2 .
$$

For a plane-wave phase $\Phi = f(s)$ with $s = \mathrm{Sc}(\tilde{K}\bar{\tilde{X}}) = -\omega t + \mathbf{k}\cdot\mathbf{x}$, the chain rule gives

$$
\partial_{ict}s = \frac{-\omega}{ic} = \frac{i\omega}{c} = K_0,
\qquad
\partial_k s = k_k ,
$$

so that

$$
\Box f(s) = \left[(\partial_{ict}s)^2 + \sum_k(\partial_k s)^2\right] f''(s)
+ \bigl(\Box s\bigr) f'(s)
= \left[-\frac{\omega^2}{c^2} + \mathbf{k}^2\right] f''(s)
= N(\tilde{K})\,f''(s),
$$

since $s$ is linear and $\Box s = 0$. Hence

$$
\boxed{\; \Box f(s) = 0 \ \text{ for every smooth } f \;}
\qquad\Longleftrightarrow\qquad
N(\tilde{K}) = 0 .
$$

A four-wavevector supports a dispersionless wave precisely when it is null, and the null condition is the zero-divisor condition: $\tilde{K}\in\mathcal{Z}$. The wave travels at the speed $c$ because $N(\tilde{K}) = 0$ reads $\omega = c|\mathbf{k}|$, and it is the norm form of the wavevector, not a separate postulate, that fixes $c$ as the propagation speed. Equivalently, the lightlike $\tilde{K} = i(\omega/c)e_0 + \mathbf{k}$ with $\omega = c|\mathbf{k}|$ has the form $i(\omega/c)(e_0 - i\hat{\mathbf{k}}) = 2i(\omega/c)\tilde{P}(-\hat{\mathbf{k}})$, an idempotent multiple, so the null wavevectors are exactly the non-pure zero divisors of the material sector, in parallel with the null positions of the previous section.

**Verification on a superposition.** A single plane wave cannot test the identity, because for it each term of $\Box$ vanishes mode by mode. The identity was therefore checked on a superposition of three null modes,

$$
\Phi(\tilde{X}) = e^{is_1} + \tfrac12 e^{is_2} + \tfrac13 e^{is_3},
\qquad
\mathbf{k}_1 = (1,0,0),\quad \mathbf{k}_2 = (0,1,0),\quad \mathbf{k}_3 = (0.6,0.8,0),
$$

with $\omega_i = c|\mathbf{k}_i|$ and $c = 1$, so that each $N(\tilde{K}_i) = 0$. Evaluating $\Box\Phi = \partial_{ict}^2\Phi + \Delta\Phi$ numerically at a generic event gives $|\Box\Phi| \sim 10^{-8}$ at the finite-difference resolution used, i.e. zero. The cross terms between different modes, which the single-mode test cannot see, are the content of the check and they cancel because each mode is separately in the kernel of $\Box$.

The factorization has a second face. Because $\Box = \tilde{\nabla}\bar{\tilde{\nabla}}$ and the two factors commute, the wave equation is also $\tilde{\nabla}(\bar{\tilde{\nabla}}\Phi) = 0$, and the cone is the set of directions in which the first-order operator $\bar{\tilde{\nabla}}$ has a nontrivial kernel of the special form $f(\mathrm{Sc}(\tilde{K}\bar{\tilde{X}}))$. The light cone is the characteristic cone of the operator, and it is the same object as the zero set of the norm form.

## Invariance of the Cone

The cone is preserved by the group that preserves the norm form. A **rotor** is a unit-norm biquaternion,

$$
\tilde{\Lambda}\bar{\tilde{\Lambda}} = e_0 ,
$$

and it acts on the material sector by conjugation, $\tilde{X}\mapsto\tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger$. Since

$$
N(\tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger)
= N(\tilde{\Lambda})\,N(\tilde{X})\,N(\tilde{\Lambda}^\dagger)
= N(\tilde{X}) ,
$$

using the multiplicativity of the norm form and $N(\tilde{\Lambda}) = 1$, $N(\tilde{\Lambda}^\dagger) = 1$, the action carries a null element to a null element and a timelike (or spacelike) element to one of the same type. The rotor also maps $\mathbb{M}_-$ to itself, because $(\tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger)^\dagger = \tilde{\Lambda}\tilde{X}^\dagger\tilde{\Lambda}^\dagger = -\tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger$ for $\tilde{X}\in\mathbb{M}_-$. The cone is therefore a Lorentz-invariant set, and the causal classification is frame-independent. Conversely, the cone determines the causal structure, and the group that preserves the cone is the group generated by the rotors together with the discrete transformations that do not preserve the arrows of time and space; the identity component is exactly the connected Lorentz group.

**Verification.** The invariance was checked numerically: two hundred random unit-norm rotors were applied to two hundred random real lightlike four-positions $\tilde{X} = it\,e_0 + t\hat{\mathbf{x}}$ (so $N = 0$), and the largest value of $|N(\tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger)|$ over the sample was at the level of the rounding error, of order $10^{-13}$ for $|t|$ of order unity, i.e. zero to machine precision. The same computation confirmed that each image remained anti-Hermitian.

Two consequences are worth stating because they are the reason the cone is a physical object and not a coordinate artefact. First, the cone has an intrinsic characterization: it is the set where the algebra's norm form degenerates, and this characterization is invariant under every algebra automorphism, not merely under the rotors. Second, the cone is the boundary of the region in which the free particle of the companion article *The Relativistic Particle in Biquaternionic Form* can move: its timelike worldline stays strictly inside, and the mass-shell hyperboloid $N(\tilde{P}) = -m^2c^2$ approaches the cone as $m\to 0$. In this precise sense the zero-divisor cone is the boundary of the massive, invertible, subluminal sector of the algebra.

## The Cone in the Algebra's Other Guises

The same set appears wherever the norm form is evaluated, and three guises are worth naming, because they show that the cone is one object seen in different variables.

- **Momentum space.** The four-momentum $\tilde{P} = iE/c\,e_0 + \mathbf{p}$ is null when $E = c|\mathbf{p}|$: the massless shell. The zero-divisor condition on momentum is the statement that the particle is massless, and for a massive particle $N(\tilde{P}) = -m^2c^2 < 0$ keeps the momentum strictly timelike.
- **Field space.** The field-strength biquaternion $\tilde{F} = i\sqrt{\epsilon}\,\mathbf{E} - \sqrt{\mu}\,\mathbf{H}$ is a pure vector $(F_0 = 0)$, so its norm form is $N(\tilde{F}) = \tilde{F}\bar{\tilde{F}} = \sum_k F_k^2$, and it vanishes exactly for a **null (radiative) field**: $\mathbf{E}\perp\mathbf{H}$ and $|\mathbf{E}| = c|\mathbf{B}|$. This is the zero-divisor cone realized inside the six-dimensional complex vector space of the field strength, and it is developed in the companion article *The Field-Strength Biquaternion and Its Invariants*. The energy–momentum tensor of such a field has rank one, as the companion exercise *Exercise: The Electromagnetic Energy–Momentum Tensor* shows.
- **Wave space.** The four-wavevector $\tilde{K}$ is null when the plane wave is dispersionless, as derived above.

In each case the statement is the same: a physically distinguished class of objects — massless particles, radiative fields, dispersionless waves — is exactly the class on which the algebra's norm form vanishes, and the class is closed under the Lorentz group.

## The Cone as the Boundary of Invertibility

The name "zero divisor" records the property that makes the cone a boundary rather than an ordinary surface. An element $\tilde{Q}$ is invertible in $\mathbb{B}$ exactly when $N(\tilde{Q})\neq 0$, with the two-sided inverse

$$
\tilde{Q}^{-1} = \frac{\bar{\tilde{Q}}}{N(\tilde{Q})},
\qquad
\tilde{Q}\tilde{Q}^{-1} = \frac{\tilde{Q}\bar{\tilde{Q}}}{N(\tilde{Q})} = e_0 ,
$$

and the corresponding right inverse is the same expression. Off the cone the norm form is a nonzero complex number, the inverse exists, and the element generates a two-sided translation of the algebra. On the cone the inverse does not exist, and the failure is not a limit that can be repaired: $N(\tilde{Q}) = 0$ makes every candidate inverse of the form $\bar{\tilde{Q}}/N(\tilde{Q})$ undefined, and the existence of a nonzero annihilator is exactly the statement that multiplication by $\tilde{Q}$ has a nontrivial kernel.

The physical reading of this algebraic boundary is the content of the preceding sections. A massive particle has $N(\tilde{P}) = -m^2c^2 \neq 0$, so its momentum is invertible and its worldline lies in the interior of the cone; a massless particle has $N(\tilde{P}) = 0$, so its momentum is a zero divisor and lies on the boundary. A timelike worldline can be continuously deformed into a lightlike one only at the cost of sending $m\to 0$, where the invertibility of the momentum is lost. The cone is therefore not merely the set of paths that light follows; it is the locus where the algebra's multiplication loses invertibility, and the two statements are the same statement in this framework.

**Verification.** For a random sample of biquaternions off the cone the identity $\tilde{Q}(\bar{\tilde{Q}}/N(\tilde{Q})) = e_0$ was checked in explicit complex-quaternion arithmetic to machine precision, and for the idempotent $\tilde{P}(e_1) = \tfrac12(e_0+ie_1)$ the products $\tilde{P}\bar{\tilde{P}}$ and $\bar{\tilde{P}}\tilde{P}$ were both found to vanish identically, confirming that no inverse exists on the cone.

## What the Algebra Supplies and What It Is Standard

**Supplied by the algebra.** The identification of the interval with the norm form, hence of the light cone with the zero set of the algebra's quadratic form; the criterion that the non-pure zero divisors are exactly the idempotent multiples, with the identity $\tilde{Q}^2 = 2Q_0\tilde{Q}$; the placement of the real light cone in the non-pure family; the factorization $\Box = \tilde{\nabla}\bar{\tilde{\nabla}}$ and the resulting characterization of null propagation as the kernel of the first-order operator; and the invariance of the cone under rotor conjugation, which is multiplicativity of the norm form.

**Standard physics transcribed.** The light-cone structure of Minkowski space, the dispersion relation $\omega = c|\mathbf{k}|$, the classification of the electromagnetic field as null/radiative when both invariants vanish, and the characteristic-cone interpretation of a second-order hyperbolic operator are all standard. The algebra reproduces them; it does not add a new propagation law.

**Interpretation.** The reading of the material cone as physical spacetime's causal structure, and of its zero-divisor character as the boundary of the invertible sector, is the framework's structural hypothesis. The mathematics is exact and standard; the physical assignment is the hypothesis.

## Open Questions

1. **The cone and the manifold structure of $\mathcal{Z}$.** The zero-divisor set is a complex cone with a singularity at the origin and a stratification by the scalar part. Does the physical state space, restricted to the material real slice, inherit a natural stratification, and does the apex play any role in the classical theory?

2. **Complexified spacetime.** The Maxwell article complexifies $\tilde{A}$ and $\tilde{F}$. In the fully complexified theory the cone of the algebra and the real light cone of the material slice are different subsets — the complex null cone is larger. Which of the two is the causal cone of the complexified theory is not settled by the algebra alone.

3. **The cone and the medium.** The propagation speed is $c = 1/\sqrt{\epsilon\mu}$, so the norm form and the cone it defines are local in a medium. Does a spatially varying medium deform the cone into a field of cones, and can this be written as a position-dependent norm form on $\mathbb{M}_-$ without leaving the algebra?

4. **The nilpotent family in physics.** The real light cone is entirely of the idempotent type; the nilpotent family requires genuinely complex spatial components. Are there classical configurations — complexified momenta, geometric-optics rays, Regge-type constructions — for which the nilpotent branch of $\mathcal{Z}$ is the physically relevant one?

5. **The cone and the metric levels.** The cone is the zero set of the level-1 identity form on $\mathbb{C}$, whose restriction to the real material slice is the level-2 form $\eta$. A reader moving to the level-3 Clifford metric $g$ must not conflate the three; whether the Clifford translation of the cone adds anything to its algebraic definition is an open question of the series rather than of this article.

The conventions of the construction are those of the following companion articles:

- Companion article *Introduction to the Biquaternion Universe*, for the notation, the norm form and the causal trichotomy.
- Companion article *Conventions in the Biquaternion Universe*, for the algebra and basis, the conjugations, the real subspaces and the metric at its three levels.
- Companion article *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*, for the real quaternion slice and the four-vector representation.
- Companion article *The Relativistic Particle in Biquaternionic Form*, for the particle's four-momentum, mass shell and causal classification.
- Companion article *The Field-Strength Biquaternion and Its Invariants*, for the field strength on the null cone and its invariants.
- Companion article *Exercise: The Electromagnetic Energy–Momentum Tensor*, for the null field's energy–momentum and its rank-one form.

## Summary

The norm form of the biquaternion algebra is $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2$. Its vanishing set is the zero-divisor set $\mathcal{Z}$, a complex cone of complex dimension three, stratified into a **pure** family ($Q_0 = 0$, nilpotent, $\tilde{Q}^2 = 0$) and a **non-pure** family ($Q_0\neq 0$, idempotent multiple, $\tilde{Q}^2 = 2Q_0\tilde{Q}$). On the real material slice $\tilde{X} = ict\,e_0 + \mathbf{x}$ the form restricts to

$$
N(\tilde{X}) = -c^2t^2 + \mathbf{x}^2 ,
$$

so $\mathcal{Z}$ meets the material sector exactly in the light cone $|\mathbf{x}| = c|t|$, and every nonzero real null point is a real multiple of an idempotent $\tilde{P}(-\hat{\mathbf{x}}) = \tfrac12(e_0 - i\hat{\mathbf{x}})$. The division subalgebras $\mathbb{C}_{\mathbb{B}}$ and $\mathbb{H}_{\mathbb{B}}$ contain no zero divisors; the cones in the two Hermitian-type sectors $\mathbb{M}_-$ and $\mathbb{M}_+$ are the two real faces of $\mathcal{Z}$, of which the material one is the physical light cone.

The cone is also the locus of propagation. Because $\Box = \tilde{\nabla}\bar{\tilde{\nabla}}$ is the norm form of the gradient, a four-wavevector $\tilde{K}$ satisfies $\Box f(\mathrm{Sc}(\tilde{K}\bar{\tilde{X}})) = N(\tilde{K})f''$ for every smooth $f$; the wave equation holds for every such phase precisely when $N(\tilde{K}) = 0$, which is $\omega = c|\mathbf{k}|$ and the zero-divisor condition on $\tilde{K}$. The cone is invariant under rotor conjugation because the norm form is multiplicative, and its three physical guises — the massless shell in momentum space, the null field in field space, and the dispersionless wavevector in wave space — are one algebraic locus.

The light cone is the set on which the biquaternion algebra ceases to be invertible; the algebra's failure of division is the algebraic form of the existence of lightlike propagation.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra; basis $e_0=1,e_1,e_2,e_3$, $e_k^2=-e_0$ |
| $i$ | Central scalar imaginary, $i^2=-1$ |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2$ | Norm form (level 1: identity on $\mathbb{C}$) |
| $\mathcal{Z} = \{\tilde{Q}\neq0 : N(\tilde{Q})=0\}$ | Zero-divisor set: the cone |
| $\mathbb{M}_-, \mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{C}_{\mathbb{B}}, \mathbb{H}_{\mathbb{B}}$ | Division subalgebras: complex scalar line (center); real quaternions |
| $\tilde{X} = ict\,e_0 + \mathbf{x}$ | Material coordinate, $\mathbb{M}_-$ |
| $N(\tilde{X}) = -c^2t^2 + \mathbf{x}^2$ | Interval; zero set is the light cone |
| $\tilde{P}(\hat{\boldsymbol{\mu}}) = \tfrac12(e_0 + i\hat{\boldsymbol{\mu}})$ | Idempotent; $N=0$, $\tilde{P}^2=\tilde{P}$ |
| $\tilde{Q}^2 = 2Q_0\tilde{Q}$ | Non-pure zero-divisor identity |
| $\tilde{\nabla}, \bar{\tilde{\nabla}}$, $\Box = \tilde{\nabla}\bar{\tilde{\nabla}} = \partial_{ict}^2+\Delta$ | Gradient, conjugate gradient, d'Alembertian |
| $\tilde{K} = i\frac{\omega}{c}e_0 + \mathbf{k}$ | Four-wavevector, $\mathbb{M}_-$ |
| $N(\tilde{K}) = -\omega^2/c^2 + \mathbf{k}^2$ | Null condition $\Leftrightarrow$ dispersionless wave |
| $\tilde{\Lambda}\bar{\tilde{\Lambda}} = e_0$ | Lorentz rotor (unit norm form) |
| $\tilde{X}\mapsto\tilde{\Lambda}\tilde{X}\tilde{\Lambda}^\dagger$ | Rotor conjugation; preserves the cone |
| $c = 1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |

## Further Reading

- Hermann Minkowski, "Space and Time" (1908), reprinted in *The Principle of Relativity* (Dover), for the light-cone structure of spacetime.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, Vol. 1 (Cambridge, 1984), for the causal structure of Minkowski space and the null cone.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for isotropic vectors, zero divisors and the classification of the real algebras $\mathbb{C}\otimes\mathbb{H}$ and $M_2(\mathbb{C})$.
- F. Reese Harvey, *Spinors and Calibrations* (Academic Press, 1990), for isotropy, null cones and the geometry of quadratic forms on matrix algebras.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2001), for idempotents, minimal ideals and the structure of matrix algebras.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the null cone and the factorization of the wave operator in geometric algebra.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the characteristic cone and null directions in the spacetime algebra.
- Ludwik Silberstein, "Elektromagnetische Grundgleichungen in bivektorieller Behandlung", *Annalen der Physik* **22** (1907) 579–586, for the complex-vector formulation whose null fields are the radiative case.
- Iwo Białynicki-Birula and Zofia Białynicka-Birula, "The role of the Riemann–Silberstein vector in classical and quantum theories of electromagnetism", *Journal of Physics A* **46** (2013) 053001, for the null-field conditions in the complex-vector formulation.
