# __The Light Cone as the Biquaternion Zero-Divisor Cone__

## Introduction

The biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ is not a division algebra. It contains nonzero elements whose biquaternion norm vanishes, and those elements annihilate other nonzero elements. This article is about the physical meaning of that fact in its simplest case: the set on which the biquaternion norm vanishes is the **light cone** of the material sector, and its algebraic character as the **zero-divisor set** is what makes the cone a boundary of the algebra and not merely a surface in spacetime.

The starting observation is one line long. For the material coordinate $\tilde{R} = ict\,e_t + x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$, the biquaternion norm is

$$
\langle\tilde{R}\rangle_{\natural} = \langle\tilde{R},\tilde{R}\rangle_{\natural} = \tilde{R}\,\tilde{R}^{\natural} = -c^2t^2 +x^2+y^2+z^2 ,
$$

so the equation $\langle\tilde{Q}\rangle_{\natural} = 0$ is exactly the equation of the light cone, $|x\,\vec e_x+y\,\vec e_y+z\,\vec e_z| = c|t|$. The Minkowski interval is not imported into the algebra and then made to vanish; it is the algebra's own quadratic form, and the cone is its zero set. What the zero-divisor structure adds is a classification of the points of the cone and a reason why the cone is special: it is the locus where elements of the algebra fail to be invertible, and the failure is precisely the existence of lightlike propagation.

Three threads are developed below.

- **The algebraic criterion.** A nonzero biquaternion has vanishing biquaternion norm if and only if it is a zero divisor, and the zero divisors split into two families — the **nilpotents**, whose scalar part vanishes and whose square is zero, written $\tilde\Upsilon$ where the nilpotency is the point (§*The Nilpotent Convention* of *Conventions in the Biquaternion Universe*), and the **idempotent multiples**, whose scalar part does not. The cone of the material sector is made of the second family, and that is the family that generates the algebra's minimal ideals.
- **The cone in the remarkable subspaces.** The complex scalar line and the real-quaternion subspace are division algebras and contain no zero divisors. The two Hermitian-type subspaces $\mathbb{M}_-$ and $\mathbb{M}_+$ each contain a cone, and the $\mathbb{M}_-$ cone is the physical light cone.
- **The cone as the locus of propagation.** The d'Alembertian is the biquaternion norm of the gradient, $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural}$, and a four-wavevector $\tilde P$ is null exactly when $\langle\tilde P\rangle_{\natural} = \langle\tilde P,\tilde P\rangle_{\natural} = 0$. For such a $\tilde P$ every function of the phase $\mathrm{Sc}(\tilde P\tilde{Q}^{\natural}) = \langle\tilde P,\tilde{Q}\rangle_{\natural}$ solves the wave equation, so the null directions are the directions in which the algebra propagates without dispersion. The light cone is where the biquaternion norm degenerates, the wave operator factorizes, and signals travel at $c$.

**Conventions.** We use those of the read list unchanged. The biquaternion algebra is $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the quaternion basis is $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ with $\vec e_\mu^2 = -e_t$ and $\vec e_\mu \vec e_\nu = -\delta_{\mu\nu}e_t + \varepsilon_{\mu\nu\lambda}\vec e_\lambda$, and $i$ is the central scalar imaginary. The subspaces are $\mathbb{M}_-$ (anti-Hermitian: imaginary scalar, real vector — the material sector), $\mathbb{M}_+$ (Hermitian: real scalar, imaginary vector — the informational sector), $\mathbb{H}_{\mathbb{B}}$ (real quaternions) and $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_t, ie_t\}$ (the centre). The conjugations are ${}^{\natural}$, $\bar{\cdot}$, ${}^{*} = ({}^{\natural})^{\,*}$ and ${}^\flat = -{}^{*}$. The gradient is $\tilde{\nabla} = e_t\partial/\partial Q_t + \vec e_x\partial/\partial Q_x + \vec e_y\partial/\partial Q_y + \vec e_z\partial/\partial Q_z$, with $\tilde{\nabla}^{\natural} = e_t\partial/\partial Q_t - \vec e_x\partial/\partial Q_x - \vec e_y\partial/\partial Q_y - \vec e_z\partial/\partial Q_z$ and $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural} = \tilde{\nabla}^{\natural}\tilde{\nabla} = \partial^2/\partial Q_t^2 + \Delta$. The biquaternion norm is $\langle\tilde{Q}\rangle_{\natural} = \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = \sum_\mu Q_\mu^2$ — level 1, the identity $\mathrm{diag}(+1,+1,+1,+1)$ on $\mathbb{C}$, restricting to the level-2 form $\eta = \mathrm{diag}(-1,+1,+1,+1)$ on the real material slice — and the material coordinate is $\tilde{R} = ict\,e_t + x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$. Throughout, $c = 1/\sqrt{\epsilon\mu}$ is the speed of light in the medium and $c_0$ its vacuum value. The trace formula is $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H) = 2\langle\tilde{P},\tilde{H}\rangle$.

## The Biquaternion Norm and Its Vanishing Set

The biquaternion norm on $\mathbb{B}$ is

$$
\langle\tilde{Q}\rangle_{\natural} = \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \tilde{Q}\,\tilde{Q}^{\natural} = Q_t^2 + Q_x^2 + Q_y^2 + Q_z^2 ,
\qquad
\tilde{Q} = Q_te_t + Q_x\vec e_x + Q_y\vec e_y + Q_z\vec e_z ,
$$

a nondegenerate complex quadratic form on $\mathbb{C}^4$. It is the determinant of the matrix realization of $\tilde{Q}$ and the natural quadratic invariant of the algebra. Its **zero set** is the quadric cone

$$
\mathcal{Z} = \{\, \tilde{Q}\in\mathbb{B} : \tilde{Q}\neq 0,\ \langle\tilde{Q}\rangle_{\natural} = 0 \,\},
$$

a complex cone of complex dimension three with the origin removed. Since the form is isotropic, the algebra is split by it, and the elements of $\mathcal{Z}$ are exactly the **zero divisors**: a nonzero $\tilde{Q}$ has $\langle\tilde{Q}\rangle_{\natural} = \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = 0$ if and only if there is a nonzero $\tilde{Q}'$ with $\tilde{Q}\tilde{Q}' = 0$ (or with $\tilde{Q}'\tilde{Q} = 0$).

On the **real material slice**, writing $\tilde{R} = ict\,e_t + x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$ with $(t,x,y,z)\in\mathbb{R}^4$, the form becomes

$$
\langle\tilde{R}\rangle_{\natural} = (ic\,t)^2 +x^2+y^2+z^2 = -c^2t^2 +x^2+y^2+z^2 ,
$$

and the trichotomy of causal type is the trichotomy of sign:

$$
\text{timelike}: \langle\tilde{Q}\rangle_{\natural} < 0,
\qquad
\text{null}: \langle\tilde{Q}\rangle_{\natural} = 0,
\qquad
\text{spacelike}: \langle\tilde{Q}\rangle_{\natural} > 0 .
$$

The vanishing set is therefore the pair of cones $|x\,\vec e_x+y\,\vec e_y+z\,\vec e_z| = c|t|$, and the future timelike region, the past timelike region and the spacelike exterior are, respectively, the interior of the future cone, the interior of the past cone, and the exterior of both. In the $ict$ convention the minus sign in $\langle\cdot\rangle_{\natural}$ is carried by the coordinate itself: $(ic\,t)^2 = -c^2t^2$. This is the level-2 Minkowski form $\eta = \mathrm{diag}(-1,+1,+1,+1)$ appearing as the restriction of the level-1 identity form of the algebra. The cone is not put into the algebra; it is where the algebra's form degenerates.

## Zero Divisors: the Criterion and the Two Families

The two families are separated by the scalar part.

**Pure family.** If $Q_t = 0$ then $\tilde{Q} = \vec Q$ is a pure vector and

$$
\tilde{Q}^2 = \vec Q\vec Q = -\vec Q\cdot\vec Q = -\langle\tilde{Q}\rangle_{\natural} = 0 ,
$$

where the middle equality uses $\vec Q\vec Q = -\vec Q\cdot\vec Q + \vec Q\times\vec Q$ and $\vec Q\times\vec Q = 0$. A pure zero divisor is therefore **nilpotent**, $\tilde{Q}^2 = 0$, and the pure zero divisors form the nilpotent cone $\vec Q\cdot\vec Q = 0$ inside the complex vector space $\mathrm{Vect}(\mathbb{B})\cong\mathbb{C}^3$. The simplest example is $\tilde{Q} = \vec e_x + i\vec e_y$, for which $N = 1^2 + i^2 = 0$ and $\tilde{Q}^2 = 0$.

**Non-pure family.** If $Q_t\neq 0$, write $\tilde{Q} = Q_t(e_t + \vec w)$ with $\vec w = \vec Q/Q_t$. The biquaternion norm is $\langle\tilde{Q}\rangle_{\natural} = Q_t^2(1 + \vec w\cdot\vec w)$, so vanishing requires

$$
\vec w\cdot\vec w = -1 ,
\qquad\text{equivalently}\qquad
\vec w^2 = +e_t .
$$

Then

$$
\tilde{Q}^2 = Q_t^2(e_t + \vec w)^2 = Q_t^2(e_t + 2\vec w + \vec w^2) = Q_t^2(2e_t + 2\vec w) = 2Q_t\,\tilde{Q},
$$

using $e_t^2 = e_t$, the cross term $2\vec w$, and $\vec w^2 = +e_t$. Hence a non-pure zero divisor satisfies the algebraic identity

$$
\boxed{\; \tilde{Q}^2 = 2Q_t\,\tilde{Q} \;}
\qquad\Longleftrightarrow\qquad
\tilde\Pi := \frac{\tilde{Q}}{2Q_t}\ \text{ is idempotent, }\ \tilde\Pi^2 = \tilde\Pi,\quad \tilde\Pi\neq 0 .
$$

The nonzero complex multiples of idempotents are therefore exactly the non-pure zero divisors. The standard idempotent is

$$
\tilde\Pi(\vec u) = \tfrac12\left(e_t + i\vec u\right),
\qquad
\vec u = u_x\vec e_x + u_y\vec e_y + u_z\vec e_z,\quad \vec u\cdot\vec u = 1 ,
$$

for which $\langle\tilde\Pi\rangle_{\natural} = \tfrac14(1 - (i\vec u)^2) = \tfrac14(1 - \vec u\cdot\vec u) = 0$ and $\tilde\Pi^2 = \tilde\Pi$, using $(i\vec u)^2 = +\vec u\cdot\vec u$ and $\vec u\cdot\vec u=1$. The verification is one line in explicit quaternion arithmetic:

$$
\tilde\Pi^2 = \tfrac14\left(e_t + 2i\vec u + (i\vec u)^2\right)
= \tfrac14\left(e_t + 2i\vec u - \vec u\vec u\right)
= \tfrac14\left(e_t + 2i\vec u + e_t\right)
= \tilde\Pi .
$$

The two families are disjoint, because the vanishing of the scalar part is what separates them, and they exhaust the zero divisors. The set $\mathcal{Z}$ is the union of the nilpotent cone and the cone of idempotent multiples — a single complex cone of complex dimension three, stratified by the vanishing of $Q_t$.

**The pacwoman property.** A null element of the non-pure family carries a one-line multiplication rule that is used whenever a transformation is applied to a lightlike object. With $\vec u$ a real unit vector, the element $e_t + i\vec u$ is **gobbled** by its own vector part:

$$
\left(i\vec u\right)\left(e_t + i\vec u\right)
\;=\;
\left(e_t + i\vec u\right)\left(i\vec u\right)
\;=\;
e_t + i\vec u ,
$$

since $(i\vec u)^2 = +\vec u\cdot\vec u = +e_t$. In the material sector the same statement reads, for the null four-wavevector direction $\vec u_k$ of a real unit vector,

$$
\vec u_k\left(i + \vec u_k\right) \;=\; i\left(i + \vec u_k\right) \;=\; \left(i + \vec u_k\right)\vec u_k,
$$

which is the form in which it appears in the boost of a plane wave. The name, due to Baylis, records that a null element can absorb a factor matched to its own direction without changing. It is a property of the null cone alone: for a general element $e_t+\vec q$ the product with $\vec q$ is $\vec q-\vec q\cdot\vec q$, which equals $e_t+\vec q$ only when $\vec q\cdot\vec q=-1$, that is, only when $e_t+\vec q$ is itself null.

## The Cone in the Remarkable Subspaces

Which real subspaces meet $\mathcal{Z}$ is the question that gives the cone its **physical interpretation**.

**The scalar line and the real quaternions are division subalgebras.** On $\mathbb{C}_{\mathbb{B}} = \mathrm{span}_{\mathbb{R}}\{e_t, ie_t\}$ a general element is $\tilde{Q} = (a + ib)e_t$ and $\langle\tilde{Q}\rangle_{\natural} = (a+ib)^2$, which vanishes only at $a = b = 0$. On $\mathbb{H}_{\mathbb{B}}$ a general element is a real quaternion $\tilde{Q} = a_0e_t + \vec a$ with $\langle\tilde{Q}\rangle_{\natural} = a_0^2 + \vec a^2$, a sum of real squares, which likewise vanishes only at the origin. Neither subspace contains a zero divisor: they are the division subalgebras of $\mathbb{B}$, and on them the biquaternion norm is anisotropic. The set $\mathcal{Z}$ lives in the complement of those two subspaces.

**The material cone.** On $\mathbb{M}_-$ the general element is $\tilde{Q} = i x_0e_t + x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$ with $x_0, x_1, x_2, x_3$ real, and

$$
\langle\tilde{Q}\rangle_{\natural} = (i x_0)^2 +x^2+y^2+z^2 = -x_0^2 +x^2+y^2+z^2 .
$$

Identifying $x_0 = ct$, the vanishing locus is the light cone of Minkowski space. For a nonzero null element with $x_0\neq 0$, writing $x\,\vec e_x+y\,\vec e_y+z\,\vec e_z = x_0\vec u_x$ with $\vec u_x$ a real unit vector gives

$$
\tilde{Q} = i x_0\left(e_t - i\vec u_x\right) = 2i x_0\,\tilde\Pi(-\vec u_x),
\qquad
\tilde\Pi(-\vec u_x) = \tfrac12\left(e_t - i\vec u_x\right),
$$

so every future (or past) null point of the real material slice is a real multiple of an idempotent: the material cone is the non-pure family, realized over the reals. The apex $\tilde{Q} = 0$ is excluded from $\mathcal{Z}$ by the definition, since it is not a zero divisor. The real pure case would require $\langle x\,\vec e_x+y\,\vec e_y+z\,\vec e_z\rangle_{\natural} =x^2+y^2+z^2 = 0$ with $(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)\neq 0$ and real, which is impossible; the nilpotent family on the material cone therefore needs complex spatial components, and the real cone is entirely of the idempotent type.

**The informational cone.** On $\mathbb{M}_+$ the general element is $\tilde{Q} = q_te_t + i\vec q$ with $q_t, \vec q$ real, and $\langle\tilde{Q}\rangle_{\natural} = q_t^2 - \vec q^2$. Its vanishing set is a cone with the real scalar $q_t$ as the distinguished coordinate — the future and past cones of the informational sector. It is a genuine cone of the same type, but its **physical interpretation** is the informational one and belongs to the companion article *The Informational Sector: States, Observables and Probability*; here it is recorded only to make the point that both Hermitian-type subspaces, and only those, carry the zero-divisor cone.

The distribution is therefore forced by the topology of the four real slices: the two division slices $\mathbb{C}_{\mathbb{B}}$ and $\mathbb{H}_{\mathbb{B}}$ are anisotropic, and the two slices on which $i$ appears with a relative sign — $\mathbb{M}_-$ and $\mathbb{M}_+$ — carry the cone. The physical light cone is the branch of $\mathcal{Z}$ that lies in the material sector.

## The Cone and the Wave Operator

The biquaternion norm is not only the interval; it is also the d'Alembertian. Composing the gradient with its quaternion conjugate gives

$$
\tilde{\nabla}\tilde{\nabla}^{\natural} = \tilde{\nabla}^{\natural}\tilde{\nabla} = \partial^2/\partial Q_t^2 + \Delta =: \Box ,
$$

because the cross terms cancel and the spatial part gives $+\sum_{\mu\in\{x,y,z\}}\partial^2/\partial Q_\mu^2$, the minus sign in $\tilde{\nabla}^{\natural}$ combining with $\vec e_\mu^2 = -e_t$. The wave operator is thus the biquaternion norm of the gradient biquaternion, exactly as $\langle\tilde{Q}\rangle_{\natural} = \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural}$ is the biquaternion norm of $\tilde{Q}$. The factorization $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural}$ is available in the algebra and is not available in a scalar wave operator; it is the algebraic statement that the second-order operator is a product of first-order ones.

Now let $\tilde P$ be a four-wavevector, meaning an element of $\mathbb{M}_-$ written as

$$
\tilde P = i\,\frac{\omega}{c}\,e_t + \vec k,
\qquad
\langle\tilde P\rangle_{\natural} = -\frac{\omega^2}{c^2} + \vec k^2 .
$$

For a plane wave $\Phi = f(s)$ with $s = \mathrm{Sc}(\tilde P\tilde{Q}^{\natural}) = -\omega t + \vec k\cdot(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)$, the chain rule gives

$$
\partial/\partial Q_t\,s = \frac{-\omega}{ic} = \frac{i\omega}{c} = K_0,
\qquad
\partial/\partial Q_k s = k_k ,
$$

so that

$$
\Box f(s) = \left[(\partial/\partial Q_t\,s)^2 + \sum_{\mu\in\{x,y,z\}}(\partial/\partial Q_\mu s)^2\right] \frac{d^2f}{ds^2}(s)
+ \bigl(\Box s\bigr) \frac{df}{ds}(s)
= \left[-\frac{\omega^2}{c^2} + \vec k^2\right] \frac{d^2f}{ds^2}(s)
= \langle\tilde P\rangle_{\natural}\,\frac{d^2f}{ds^2}(s),
$$

since $s$ is linear and $\Box s = 0$. Hence

$$
\boxed{\; \Box f(s) = 0 \ \text{ for every smooth } f \;}
\qquad\Longleftrightarrow\qquad
\langle\tilde P\rangle_{\natural} = 0 .
$$

A four-wavevector supports a dispersionless wave precisely when it is null, and the null condition is the zero-divisor condition: $\tilde P\in\mathcal{Z}$. The wave travels at the speed $c$ because $\langle\tilde P\rangle_{\natural} = 0$ reads $\omega = c|\vec k|$, and it is the biquaternion norm of the wavevector, not a separate postulate, that fixes $c$ as the propagation speed. Equivalently, the lightlike $\tilde P = i(\omega/c)e_t + \vec k$ with $\omega = c|\vec k|$ has the form $i(\omega/c)(e_t - i\vec u_k) = 2i(\omega/c)\tilde\Pi(-\vec u_k)$, an idempotent multiple, so the null wavevectors are exactly the non-pure zero divisors of the material sector, in parallel with the null positions of the previous section.

A superposition of three such modes checks the cancellation explicitly. Let
$$
\Phi(\tilde{Q}) = \exp(is_1) + \tfrac12 \exp(is_2) + \tfrac13 \exp(is_3),
\qquad
\vec k_1 = (1,0,0),\quad \vec k_2 = (0,1,0),\quad \vec k_3 = (0.6,0.8,0),
$$

with $\omega_i = c|\vec k_i|$ and $c = 1$, so that each $\langle\tilde P_i\rangle_{\natural} = 0$. Evaluating $\Box\Phi = \partial^2/\partial Q_t^2\Phi + \Delta\Phi$ numerically at a generic event gives $|\Box\Phi| \sim 10^{-8}$ at the finite-difference resolution used, i.e. zero. The cross terms between different modes, which the single-mode test cannot see, are the content of the check and they cancel because each mode is separately in the kernel of $\Box$.

The factorization has a second face. Because $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural}$ and the two factors commute, the wave equation is also $\tilde{\nabla}(\tilde{\nabla}^{\natural}\Phi) = 0$, and the cone is the set of directions in which the first-order operator $\tilde{\nabla}^{\natural}$ has a nontrivial kernel of the special form $f(\mathrm{Sc}(\tilde P\tilde{Q}^{\natural}))$. The light cone is the characteristic cone of the operator, and it is the same object as the zero set of the biquaternion norm.

## Invariance of the Cone

The cone is preserved by the group that preserves the biquaternion norm. A **rotor** is a unit-norm biquaternion,

$$
\tilde{U}\tilde{U}^{\natural} = e_t ,
$$

and it acts on the material sector by conjugation, $\tilde{Q}\mapsto\tilde{U}\tilde{Q}\tilde{U}^{*}$. Since

$$
\langle\tilde{U}\tilde{Q}\tilde{U}^{*}\rangle_{\natural}
= \langle\tilde{U}\rangle_{\natural}\,\langle\tilde{Q}\rangle_{\natural}\,\langle\tilde{U}^{*}\rangle_{\natural}
= \langle\tilde{Q}\rangle_{\natural} ,
$$

using the multiplicativity of the biquaternion norm and $\langle\tilde{U}\rangle_{\natural} = 1$, $\langle\tilde{U}^{*}\rangle_{\natural} = 1$, the action carries a null element to a null element and a timelike (or spacelike) element to one of the same type. The rotor also maps $\mathbb{M}_-$ to itself, because $(\tilde{U}\tilde{Q}\tilde{U}^{*})^{*} = \tilde{U}\tilde{Q}^{*}\tilde{U}^{*} = -\tilde{U}\tilde{Q}\tilde{U}^{*}$ for $\tilde{Q}\in\mathbb{M}_-$. The cone is therefore a Lorentz-invariant set, and the causal classification is frame-independent. Conversely, the cone determines the causal structure, and the group that preserves the cone is the group generated by the rotors together with the discrete transformations that do not preserve the arrows of time and space; the identity component is exactly the connected Lorentz group.


Two consequences are worth stating because they are the reason the cone is a physical object and not a coordinate artefact. First, the cone has an intrinsic characterization: it is the set where the algebra's biquaternion norm degenerates, and this characterization is invariant under every algebra automorphism, not merely under the rotors. Second, the cone is the boundary of the region in which the free particle of the companion article *The Relativistic Particle in Biquaternionic Form* can move: its timelike worldline stays strictly inside, and the mass-shell hyperboloid $\langle\tilde{P}\rangle_{\natural} = -m^2c^2$ approaches the cone as $m\to 0$. In this precise sense the zero-divisor cone is the boundary of the massive, invertible, subluminal sector of the algebra.

## The Cone in the Algebra's Other Guises

The same set appears wherever the biquaternion norm is evaluated, and three guises are worth naming, because they show that the cone is one object seen in different variables.

- **Momentum space.** The four-momentum $\tilde{P} = iE/c\,e_t + \vec p$ is null when $E = c|\vec p|$: the massless shell. The zero-divisor condition on momentum is the statement that the particle is massless, and for a massive particle $\langle\tilde{P}\rangle_{\natural} = -m^2c^2 < 0$ keeps the momentum strictly timelike.
- **Field space.** The field-strength biquaternion $\tilde{F} = i\sqrt{\epsilon}\,\vec E - \sqrt{\mu}\,\vec H$ is a pure vector $(F_0 = 0)$, so its biquaternion norm is $\langle\tilde{F}\rangle_{\natural} = \langle\tilde{F},\tilde{F}\rangle_{\natural} = \tilde{F}\tilde{F}^{\natural} = \sum_k F_k^2$, and it vanishes exactly for a **null (radiative) field**: $\vec E\perp\vec H$ and $|\vec E| = c|\vec B|$. This is the zero-divisor cone realized inside the six-dimensional complex vector space of the field strength, and it is developed in the companion article *The Field-Strength Biquaternion and Its Invariants*. The energy–momentum tensor of such a field has rank one, as the companion exercise *Exercise: The Electromagnetic Energy–Momentum Tensor* shows.
- **Wave space.** The four-wavevector $\tilde P$ is null when the plane wave is dispersionless, as derived above.

In each case the statement is the same: a physically distinguished class of objects — massless particles, radiative fields, dispersionless waves — is exactly the class on which the algebra's biquaternion norm vanishes, and the class is closed under the Lorentz group.

## The Cone as the Boundary of Invertibility

The name "zero divisor" records the property that makes the cone a boundary rather than an ordinary surface. An element $\tilde{Q}$ is invertible in $\mathbb{B}$ exactly when $\langle\tilde{Q}\rangle_{\natural}\neq 0$, with the two-sided inverse

$$
\tilde{Q}^{-1} = \frac{\tilde{Q}^{\natural}}{\langle\tilde{Q}\rangle_{\natural}},
\qquad
\tilde{Q}\tilde{Q}^{-1} = \frac{\tilde{Q}\tilde{Q}^{\natural}}{\langle\tilde{Q}\rangle_{\natural}} = e_t ,
$$

and the corresponding right inverse is the same expression. Off the cone the biquaternion norm is a nonzero complex number, the inverse exists, and the element is a unit that generates the whole algebra as a two-sided ideal. On the cone the inverse does not exist, and the failure is not a limit that can be repaired: $\langle\tilde{Q}\rangle_{\natural} = \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = 0$ makes every candidate inverse of the form $\tilde{Q}^{\natural}/\langle\tilde{Q}\rangle_{\natural}$ undefined, and the existence of a nonzero annihilator is exactly the statement that multiplication by $\tilde{Q}$ has a nontrivial kernel.

The **physical interpretation** of this algebraic boundary is the content of the preceding sections. A massive particle has $\langle\tilde{P}\rangle_{\natural} = -m^2c^2 \neq 0$, so its momentum is invertible and its worldline lies in the interior of the cone; a massless particle has $\langle\tilde{P}\rangle_{\natural} = 0$, so its momentum is a zero divisor and lies on the boundary. A timelike worldline can be continuously deformed into a lightlike one only at the cost of sending $m\to 0$, where the invertibility of the momentum is lost. The cone is therefore not merely the set of paths that light follows; it is the locus where the algebra's multiplication loses invertibility, and the two statements are the same statement in this framework.


## What the Algebra Supplies and What It Is Standard

**Supplied by the algebra.** The identification of the interval with the biquaternion norm, hence of the light cone with the zero set of the algebra's quadratic form; the criterion that the non-pure zero divisors are exactly the idempotent multiples, with the identity $\tilde{Q}^2 = 2Q_t\tilde{Q}$; the placement of the real light cone in the non-pure family; the factorization $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural}$ and the resulting characterization of null propagation as the kernel of the first-order operator; and the invariance of the cone under rotor conjugation, which is multiplicativity of the biquaternion norm.

**Standard physics transcribed.** The light-cone structure of Minkowski space, the dispersion relation $\omega = c|\vec k|$, the classification of the electromagnetic field as null/radiative when both invariants vanish, and the characteristic-cone interpretation of a second-order hyperbolic operator are all standard. The algebra reproduces them; it does not add a new propagation law.

**Interpretation.** The interpretation of the material cone as physical spacetime's causal structure, and of its zero-divisor character as the boundary of the invertible sector, is the framework's structural hypothesis. The mathematics is exact and standard; the physical assignment is the hypothesis.

## Open Questions

1. **The cone and the manifold structure of $\mathcal{Z}$.** The zero-divisor set is a complex cone with a singularity at the origin and a stratification by the scalar part. Does the physical state space, restricted to the material real slice, inherit a natural stratification, and does the apex play any role in the classical theory?

2. **Complexified spacetime.** The Maxwell article complexifies $\tilde{A}$ and $\tilde{F}$. In the fully complexified theory the cone of the algebra and the real light cone of the material slice are different subsets — the complex null cone is larger. Which of the two is the causal cone of the complexified theory is not settled by the algebra alone.

3. **The cone and the medium.** The propagation speed is $c = 1/\sqrt{\epsilon\mu}$, so the biquaternion norm and the cone it defines are local in a medium. Does a spatially varying medium deform the cone into a field of cones, and can this be written as a position-dependent biquaternion norm on $\mathbb{M}_-$ without leaving the algebra?

4. **The nilpotent family in physics.** The real light cone is entirely of the idempotent type; the nilpotent family requires genuinely complex spatial components. Are there classical configurations — complexified momenta, geometric-optics rays, Regge-type constructions — for which the nilpotent branch of $\mathcal{Z}$ is the physically relevant one?

5. **The cone and the metric levels.** The cone is the zero set of the level-1 identity form on $\mathbb{C}$, whose restriction to the real material slice is the level-2 form $\eta$. A reader moving to the level-3 Clifford metric $g$ must not conflate the three; whether the Clifford translation of the cone adds anything to its algebraic definition is an open question of the series rather than of this article.

The conventions of the construction are those of the following companion articles:

- Companion article *Introduction to the Biquaternion Universe*, for the notation, the biquaternion norm and the causal trichotomy.
- Companion article *Conventions in the Biquaternion Universe*, for the algebra and basis, the conjugations, the real subspaces and the metric (its three levels are ruled on in *The Four Forms and the Four Algebraic Norms*).
- Companion article *The Material Sector: Four-Vectors, Interval and Lorentz Action*, for the real quaternion slice and the four-vector representation.
- Companion article *The Relativistic Particle in Biquaternionic Form*, for the particle's four-momentum, mass shell and causal classification.
- Companion article *The Field-Strength Biquaternion and Its Invariants*, for the field strength on the null cone and its invariants.
- Companion article *Exercise: The Electromagnetic Energy–Momentum Tensor*, for the null field's energy–momentum and its rank-one form.

## Summary

The biquaternion norm of the biquaternion algebra is $\langle\tilde{Q}\rangle_{\natural} = \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = \sum_\mu Q_\mu^2$. Its vanishing set is the zero-divisor set $\mathcal{Z}$, a complex cone of complex dimension three, stratified into a **pure** family ($Q_t = 0$, nilpotent, $\tilde{Q}^2 = 0$) and a **non-pure** family ($Q_t\neq 0$, idempotent multiple, $\tilde{Q}^2 = 2Q_t\tilde{Q}$). On the real material slice $\tilde{R} = ict\,e_t + x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$ the form restricts to

$$
\langle\tilde{R}\rangle_{\natural} = -c^2t^2 +x^2+y^2+z^2 ,
$$

so $\mathcal{Z}$ meets the material sector exactly in the light cone $|x\,\vec e_x+y\,\vec e_y+z\,\vec e_z| = c|t|$, and every nonzero real null point is a real multiple of an idempotent $\tilde\Pi(-\vec u_x) = \tfrac12(e_t - i\vec u_x)$. The division subalgebras $\mathbb{C}_{\mathbb{B}}$ and $\mathbb{H}_{\mathbb{B}}$ contain no zero divisors; the cones in the two Hermitian-type sectors $\mathbb{M}_-$ and $\mathbb{M}_+$ are the two real faces of $\mathcal{Z}$, of which the material one is the physical light cone.

The cone is also the locus of propagation. Because $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural}$ is the biquaternion norm of the gradient, a four-wavevector $\tilde P$ satisfies $\Box f(\mathrm{Sc}(\tilde P\tilde{Q}^{\natural})) = \langle\tilde P\rangle_{\natural}\frac{d^2f}{ds^2}$ for every smooth $f$; the wave equation holds for every such phase precisely when $\langle\tilde P\rangle_{\natural} = 0$, which is $\omega = c|\vec k|$ and the zero-divisor condition on $\tilde P$. The cone is invariant under rotor conjugation because the biquaternion norm is multiplicative, and its three physical guises — the massless shell in momentum space, the null field in field space, and the dispersionless wavevector in wave space — are one algebraic locus.

The light cone is the set on which elements of the biquaternion algebra cease to be invertible; the algebra's failure of division is the algebraic form of the existence of lightlike propagation.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra; basis $e_t=1,\vec e_x,\vec e_y,\vec e_z$, $\vec e_\mu^2=-e_t$ |
| $i$ | Central scalar imaginary, $i^2=-1$ |
| $\langle\tilde{Q}\rangle_{\natural} = \langle\tilde{Q},\tilde{Q}\rangle_{\natural} = \tilde{Q}\tilde{Q}^{\natural} = \sum_\mu Q_\mu^2$ | Biquaternion norm (level 1: identity on $\mathbb{C}$) |
| $\mathcal{Z} = \{\tilde{Q}\neq0 : \langle\tilde{Q}\rangle_{\natural}=0\}$ | Zero-divisor set: the cone |
| $\mathbb{M}_-, \mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathbb{C}_{\mathbb{B}}, \mathbb{H}_{\mathbb{B}}$ | Division subalgebras: complex scalar line (centre); real quaternions |
| $\tilde{R} = ict\,e_t + x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$ | Material coordinate, $\mathbb{M}_-$ |
| $\langle\tilde{Q}\rangle_{\natural} = -c^2t^2 +x^2+y^2+z^2$ | Interval; zero set is the light cone |
| $\tilde\Pi(\vec u) = \tfrac12(e_t + i\vec u)$ | Idempotent; $N=0$, $\tilde\Pi^2=\tilde\Pi$ |
| $\tilde{Q}^2 = 2Q_t\tilde{Q}$ | Non-pure zero-divisor identity |
| $\tilde{\nabla}, \tilde{\nabla}^{\natural}$, $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural} = \partial^2/\partial Q_t^2+\Delta$ | Gradient, conjugate gradient, d'Alembertian |
| $\tilde P = i\frac{\omega}{c}e_t + \vec k$ | Four-wavevector, $\mathbb{M}_-$ |
| $\langle\tilde P\rangle_{\natural} = -\omega^2/c^2 + \vec k^2$ | Null condition $\Leftrightarrow$ dispersionless wave |
| $\tilde{U}\tilde{U}^{\natural} = e_t$ | Lorentz rotor (unit norm) |
| $\tilde{Q}\mapsto\tilde{U}\tilde{Q}\tilde{U}^{*}$ | Rotor conjugation; preserves the cone |
| $c = 1/\sqrt{\epsilon\mu}$, $c_0$ | Speed of light in the medium; in vacuum |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle$ | the general plain bilinear form, the scalar part of the general plain bilinear product, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2)$ |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}$ | the general plain sesquilinear form, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2^{*})$; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{*}=\sum_\mu\lvert Q_{2\mu}\rvert^{2}$ |

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
