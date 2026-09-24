# __Lagrangian and Hamiltonian Mechanics in Biquaternionic Form__

## Introduction

Classical mechanics admits two great formulations. In the **Lagrangian** formulation a mechanical system is specified by a configuration space, a Lagrangian $L(q,\dot q,t)$, and the variational principle $\delta S=0$, whose Euler–Lagrange equations are the equations of motion. In the **Hamiltonian** formulation the same system is specified by a phase space, a Hamiltonian $H(q,p,t)$ obtained from $L$ by the Legendre transform, and Hamilton's first-order equations; the observables then carry the Poisson bracket, and the dynamics is the Hamiltonian flow.

Both formulations are usually written in coordinates. This article writes them in the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ of the companion articles. The purpose is not to derive new mechanics. It is to exhibit which parts of the two formulations the algebra fixes, and to be explicit about the boundary beyond which it does not reach.

Three structural statements organise the article, and they are worth stating at the outset.

1. **The kinetic energy is the norm form.** For a configuration whose generalized coordinates are assembled into a real quaternion $\tilde q$, the kinetic energy of a free particle is $\tfrac{m}{2}N(\dot{\tilde q})=\tfrac{m}{2}\dot{\tilde q}\,\bar{\dot{\tilde q}}$, the norm form of the velocity. The norm form is the algebra's own quadratic form, and the free Lagrangian is a scalar multiple of it.
2. **The phase-space coordinate is one biquaternion.** The position and the momentum assemble into $\tilde Z=\tilde q+i\tilde p$, whose anti-Hermitian part is the position and whose Hermitian part is $i$ times the momentum. The algebra's two sectors thus separate a kinematic configuration from its conjugate momentum, and the algebra's complex structure is the phase-space complex structure.
3. **The boundary is finite-dimensional.** The algebra $\mathbb{B}\cong M_2(\mathbb{C})$ is eight-dimensional over $\mathbb{R}$. It carries the configuration of a system with at most four real degrees of freedom, and it carries the *rotational* bracket exactly; it does not carry the canonical Heisenberg structure, as the companion article *Similitudes Between the Poisson Bracket and the Quantum Commutator* establishes and as the companion article *The Harmonic Oscillator in Biquaternionic Form* confirms. This article is classical throughout: no commutator is introduced, and no canonical relation of the form $[\tilde q,\tilde p]=i\hbar$ is used or needed.

The conventions are those of the read list. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$; the quaternion basis is $e_0=1,e_1,e_2,e_3$ with $e_k^2=-e_0$ and $e_je_k=-\delta_{jk}e_0+\varepsilon_{jkl}e_l$; the scalar imaginary $i$ is central with $i^2=-1$. The anti-Hermitian subspace $\mathbb{M}_-$ (imaginary scalar, real vector) is the material sector, and the Hermitian subspace $\mathbb{M}_+$ (real scalar, imaginary vector) is the informational sector, with $\mathbb{B}=\mathbb{M}_-\oplus\mathbb{M}_+$. The real-quaternion subspace is $\mathbb{H}_{\mathbb{B}}$, and the trace is normalized by $\mathrm{Tr}(e_0)=2$. The symbol $c=1/\sqrt{\epsilon\mu}$ is the speed of light in the medium, and $c_0$ its vacuum value. Throughout, $\tilde q$ denotes a configuration quaternion, $\tilde p$ its conjugate momentum, and the scalar pairing of two real quaternions $\tilde a,\tilde b$ is $\mathrm{Sc}(\bar{\tilde a}\,\tilde b)=\sum_\mu a_\mu b_\mu$.

The companion articles supply the pieces:
- Companion article *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*, for the material sector, the norm form, and the four-vectors.
- Companion article *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*, for the Hermitian sector, the trace formula, and the conjugation action.
- Companion article *Similitudes Between the Poisson Bracket and the Quantum Commutator*, for the classical bracket conventions and the boundary between the classical and quantum brackets.
- Companion article *Similitudes Between Biquaternion Rotors and Hamiltonian Flow*, for the rotor and the Hamiltonian flow on the coadjoint orbit.
- Companion article *The Harmonic Oscillator in Biquaternionic Form*, for the phase plane and the sector structure of a mode.

## The Standard Formulation

The standard Lagrangian and Hamiltonian formalism is recalled here in the form the biquaternion transcription will take; nothing in this section is new.

The formalism is not an independent postulate. It follows from **D'Alembert's principle of virtual work** — the infinitesimal virtual work done by the impressed forces across displacements consistent with the constraints vanishes, which is the statement that the constraint forces do no work. Eliminating those forces is what allows the constraints to be absorbed into the geometry of the coordinates: a system of $\mathcal N$ constituents in three dimensions with $\kappa$ independent constraints has $3\mathcal N-\kappa$ **degrees of freedom**, described by the same number of **generalized coordinates** $q_i$, one per degree of freedom. These are not curvilinear coordinates. The number of curvilinear coordinates is the dimension of the position space — three, for three-dimensional space — whereas the number of generalized coordinates is the number of degrees of freedom, which constraints reduce and additional constituents raise; the two counts need not agree. A constraint expressible as $\mathbf r=\mathbf r(q,t)$ holding for all $t$ is **holonomic**; it is **scleronomic** when the relation carries no explicit time and **rheonomic** when it does. The Lagrange equation obtained below is the generalized form of Newton's second law that results, and the stationary-action statement is its equivalent formulation in integral form.

Let a system have $n$ generalized coordinates $q=(q_1,\dots,q_n)$ and velocities $\dot q$. The **Lagrangian** is a smooth real function $L(q,\dot q,t)$, and the **action** is the functional

$$
S[q]=\int_{t_1}^{t_2}L(q,\dot q,t)\,dt .
$$

The **principle of stationary action** states that the physical trajectory is a stationary point of $S$ among paths with fixed endpoints. For an arbitrary variation $\delta q(t)$ vanishing at the endpoints,

$$
\delta S=\int_{t_1}^{t_2}\left(\frac{\partial L}{\partial q_i}\,\delta q_i+\frac{\partial L}{\partial \dot q_i}\,\delta\dot q_i\right)dt
=\int_{t_1}^{t_2}\left(\frac{\partial L}{\partial q_i}-\frac{d}{dt}\frac{\partial L}{\partial \dot q_i}\right)\delta q_i\,dt ,
$$

after an integration by parts. Stationarity for all $\delta q$ gives the **Euler–Lagrange equations**

$$
\frac{d}{dt}\frac{\partial L}{\partial \dot q_i}-\frac{\partial L}{\partial q_i}=0 .
$$

The Lagrangian is **not unique**, and the extent of the ambiguity is a boundary term. For any smooth $F(q,t)$, the Lagrangians $L$ and

$$
L'=L+\frac{d}{dt}F(q,t)
$$

have the same Euler–Lagrange equations. The added term enters both terms of the Euler–Lagrange operator as the same expression, $d/dt(\partial F/\partial q_i)$: once as $\partial_{q_i}(dF/dt)$, and once as $d/dt\big(\partial_{\dot q_i}(dF/dt)\big)=d/dt(\partial F/\partial q_i)$, since the mixed partials of $F$ commute. The two contributions cancel. The action is ambiguous in the corresponding way,

$$
S'=S+F\big(q(t_2),t_2\big)-F\big(q(t_1),t_1\big) ,
$$

the difference being an endpoint term, which a variation with fixed endpoints cannot see. What the formalism determines is therefore the **equations of motion**, not the Lagrangian, and the ambiguity is exactly a boundary term: the same structure the companion article *The Action Principle and the Classical Limit as Stationary Phase in Biquaternionic Form* meets from the other side, where the boundary term of $\delta S$ is the symplectic potential. The Hamiltonian carries the analogous freedom — a generating function of the coordinates, momenta and time shifts it by a partial time derivative — and that is the freedom a canonical transformation exploits.

The **conjugate momenta** are $p_i=\partial L/\partial \dot q_i$. In the Hamiltonian description the coordinates, velocities and momenta are **mutually independent** variables: the relation $p_i=\partial L/\partial\dot q_i$ is used once, to eliminate the velocities in favour of the momenta, and does not thereafter act as a constraint among the phase-space variables. So $H(q,p)$ is differentiated with respect to $p_i$ at fixed $q$, with $\dot q$ already eliminated; holding $\dot q$ fixed while varying $p_i$ would describe a different object. This is what makes the passage a change of variables rather than a definition, and it is why the phase-space element $\tilde Z=\tilde q+i\tilde p$ constructed below is a coordinate. When the Hessian matrix $\partial^2L/\partial\dot q_i\partial\dot q_j$ is non-singular, the map $(q,\dot q)\mapsto(q,p)$ is invertible, and the **Legendre transform**

$$
H(q,p,t)=p_i\dot q_i-L(q,\dot q,t)
$$

defines the **Hamiltonian**. Its differential gives **Hamilton's equations**

$$
\dot q_i=\frac{\partial H}{\partial p_i},\qquad
\dot p_i=-\frac{\partial H}{\partial q_i}.
$$

For observables $f(q,p)$, $g(q,p)$, the **Poisson bracket** is

$$
\{f,g\}=\frac{\partial f}{\partial q_i}\frac{\partial g}{\partial p_i}-\frac{\partial f}{\partial p_i}\frac{\partial g}{\partial q_i},
$$

and the dynamics is $\dot f=\{f,H\}$. The bracket is bilinear, antisymmetric, and satisfies the Jacobi identity; it is a derivation of the commutative algebra of observables under pointwise multiplication.

## The Biquaternionic Configuration

### Coordinates and the Gradient

Assemble the generalized coordinates of a system with at most four degrees of freedom into a **real quaternion**

$$
\tilde q=q_0\,e_0+q_1\,e_1+q_2\,e_2+q_3\,e_3\in\mathbb{H}_{\mathbb{B}} ,
$$

with real components $q_\mu$. The physical three-space is the pure real part $\mathbf q=q_1e_1+q_2e_2+q_3e_3\in\mathbb{H}_{\mathbb{B}}\cap\mathbb{M}_-$, and the central coordinate $q_0e_0\in\mathbb{C}_{\mathbb{B}}\cap\mathbb{H}_{\mathbb{B}}$ is a fourth, scalar degree of freedom. A system with three degrees of freedom is the special case $q_0=0$; the pure-vector configuration is the one that carries the spatial interpretation.

For a central-valued function $F(\tilde q)$ — a function taking values in $\mathbb{C}_{\mathbb{B}}$ — define the **quaternion gradient** componentwise,

$$
\partial_{\tilde q}F=\sum_{\mu=0}^{3}e_\mu\,\frac{\partial F}{\partial q_\mu}.
$$

Because $F$ is central, this gradient is unambiguous: the quaternion product does not enter the definition, and the left and right derivatives of a central-valued function of real quaternion variables agree. The pairing that makes it a derivative is the scalar pairing,

$$
dF=\mathrm{Sc}\!\left(\overline{\partial_{\tilde q}F}\;d\tilde q\right)
=\sum_{\mu=0}^{3}\frac{\partial F}{\partial q_\mu}\,dq_\mu ,
$$

which uses $\mathrm{Sc}(\bar e_\mu e_\nu)=\delta_{\mu\nu}$. This is the statement, in the algebra, that the natural scalar product on the real-quaternion subspace is the scalar part of a quaternion product.

### The Kinetic Energy Is the Norm Form

Let $\tilde q(t)$ be a trajectory and $\dot{\tilde q}$ its velocity. The **kinetic energy** of a particle of mass $m$ is

$$
T=\tfrac{1}{2}m\,N(\dot{\tilde q})=\tfrac{1}{2}m\,\dot{\tilde q}\,\bar{\dot{\tilde q}}=\tfrac{1}{2}m\sum_{\mu=0}^{3}\dot q_\mu^2 .
$$

For a pure-vector configuration the central term is absent and $T=\tfrac{1}{2}m|\dot{\mathbf q}|^2$, the familiar kinetic energy. The kinetic energy is therefore the **norm form** of the velocity, and this is the first structural fact of the biquaternion formulation of mechanics: the algebra's own quadratic form is the free kinetic energy. The norm form on $\mathbb{H}_{\mathbb{B}}$ is positive definite, so $T\ge0$ with equality only for $\dot{\tilde q}=0$; no sign choice has to be made.

The free Lagrangian is

$$
L_0=\tfrac{1}{2}m\,N(\dot{\tilde q}),
$$

and a particle in a central potential $V(\tilde q)$ has

$$
L=\tfrac{1}{2}m\,N(\dot{\tilde q})-V(\tilde q).
$$

### The Euler–Lagrange Equations

Vary the action $S[\tilde q]=\int L\,dt$ with fixed endpoints. Using the scalar pairing, the first variation is

$$
\delta S=\int\left[\mathrm{Sc}\!\left(\overline{\partial_{\tilde q}L}\;\delta\tilde q\right)+\mathrm{Sc}\!\left(\overline{\partial_{\dot{\tilde q}}L}\;\delta\dot{\tilde q}\right)\right]dt ,
$$

and an integration by parts turns the second term into a total derivative plus

$$
\delta S=\int \mathrm{Sc}\!\left[\overline{\left(\partial_{\tilde q}L-\frac{d}{dt}\partial_{\dot{\tilde q}}L\right)}\;\delta\tilde q\right]dt
+\left[\mathrm{Sc}\!\left(\overline{\partial_{\dot{\tilde q}}L}\;\delta\tilde q\right)\right]_{t_1}^{t_2}.
$$

The endpoint term vanishes because $\delta\tilde q(t_1)=\delta\tilde q(t_2)=0$. Since $\delta\tilde q$ is an arbitrary real quaternion at each time, stationarity of $S$ requires the bracket to vanish, and the **Euler–Lagrange equation** takes the quaternion form

$$
\boxed{\;\frac{d}{dt}\frac{\partial L}{\partial\dot{\tilde q}}-\frac{\partial L}{\partial\tilde q}=0\;}
\qquad\text{with}\qquad
\frac{\partial L}{\partial\dot{\tilde q}}=\sum_\mu e_\mu\frac{\partial L}{\partial\dot q_\mu},\quad
\frac{\partial L}{\partial\tilde q}=\sum_\mu e_\mu\frac{\partial L}{\partial q_\mu}.
$$

This single quaternion equation is the four real Euler–Lagrange equations, one for each component $q_\mu$.

**Free particle.** For $L_0=\tfrac{1}{2}mN(\dot{\tilde q})$ the gradient is $\partial L_0/\partial\dot{\tilde q}=m\dot{\tilde q}$ and $\partial L_0/\partial\tilde q=0$, so the equation is $m\ddot{\tilde q}=0$: straight-line motion at constant velocity, as it must be.

**Central potential.** For $L=\tfrac{1}{2}mN(\dot{\tilde q})-V(\tilde q)$, the equation is

$$
m\ddot{\tilde q}=-\partial_{\tilde q}V .
$$

When $V$ is a function of the real-quaternion modulus $N(\tilde q)$ alone, the right-hand side is $-\partial_{\tilde q}V=-2V'(N)\tilde q$, a central force. The biquaternion equation is then the vector equation of a central-force problem; the specific force laws belong to the subcategory on effects without intrinsic magnetism, and are not developed here.

## The Legendre Transform

### Momentum and Hamiltonian

The **conjugate momentum** is the real quaternion

$$
\tilde p=\frac{\partial L}{\partial\dot{\tilde q}}=\sum_\mu e_\mu p_\mu,\qquad p_\mu=\frac{\partial L}{\partial\dot q_\mu}.
$$

For the free particle $\tilde p=m\dot{\tilde q}$. The **Hamiltonian** is the Legendre transform

$$
H(\tilde q,\tilde p)=\mathrm{Sc}\!\left(\bar{\tilde p}\,\dot{\tilde q}\right)-L(\tilde q,\dot{\tilde q})
=\sum_\mu p_\mu\dot q_\mu-L ,
$$

with $\dot{\tilde q}$ eliminated in favour of $\tilde p$ using the inverse of $\tilde p=\partial L/\partial\dot{\tilde q}$. The scalar pairing $\mathrm{Sc}(\bar{\tilde p}\dot{\tilde q})=\sum_\mu p_\mu\dot q_\mu$ is the quaternion form of the contraction $p_i\dot q_i$; the conjugate is required, because $\mathrm{Sc}(\tilde p\dot{\tilde q})$ reverses the sign of the vector-part contribution.

**Free particle.** With $\tilde p=m\dot{\tilde q}$ one has $\mathrm{Sc}(\bar{\tilde p}\dot{\tilde q})=mN(\dot{\tilde q})=2T$, and

$$
H_0=\frac{N(\tilde p)}{2m}=\frac{\tilde p\,\bar{\tilde p}}{2m}=\frac{1}{2m}\sum_{\mu=0}^{3}p_\mu^2 ,
$$

the free Hamiltonian, which reduces to the familiar $\mathbf p^2/2m$ for a pure-vector momentum, $p_0=0$. The structural statement is the mirror of the one for $L_0$: **the free Hamiltonian is the norm form of the momentum, divided by $2m$.** The norm form thus appears at both ends of the Legendre transform, once on velocity and once on momentum, because the Legendre transform of a quadratic form is its own inverse up to the mass factor.

**Harmonic oscillator.** For $L=\tfrac{1}{2}mN(\dot{\tilde q})-\tfrac{1}{2}m\omega^2N(\tilde q)$ the momentum is again $\tilde p=m\dot{\tilde q}$ and

$$
H=\frac{N(\tilde p)}{2m}+\frac{m\omega^2}{2}N(\tilde q).
$$

The Hamiltonian is a sum of two norm forms with positive coefficients, one in the momentum and one in the coordinate. Its level sets $H=E$ are ellipsoids in the eight-dimensional real phase space.

**When is the Hamiltonian the energy?** The identification of $H$ with $T+V$ is not automatic, and the condition is one this transcription satisfies by construction. If the kinetic energy is a **homogeneous function of degree two** in the generalized velocities, $T(\lambda\dot q)=\lambda^2T(\dot q)$, then Euler's theorem on homogeneous functions gives $\dot q_\mu\partial T/\partial\dot q_\mu=2T$. When the potential depends on the coordinates alone, $p_\mu=\partial T/\partial\dot q_\mu$, and therefore

$$
\mathrm{Sc}\!\left(\bar{\tilde p}\,\dot{\tilde q}\right)=p_\mu\dot q_\mu=2T,\qquad H=2T-(T-V)=T+V ,
$$

so $H$ is the total energy, and it is conserved when $L$ has no explicit time dependence. For the systems of this article the hypothesis is not an assumption but a property of the kinetic term: $T=\tfrac12 mN(\dot{\tilde q})$ is a quadratic form in the velocities and hence homogeneous of degree two. The condition can fail — a relativistic kinetic energy is not homogeneous of degree two — and where it fails $H$ remains the Legendre transform of $L$ but is no longer the energy.

Explicit time dependence, by contrast, is preserved by the transform. Differentiating $H=p_\mu\dot q_\mu-L$ with respect to $t$ at fixed coordinates and momenta, the terms in $\partial\dot q_\mu/\partial t$ cancel against $p_\mu=\partial L/\partial\dot q_\mu$, leaving

$$
\frac{\partial H}{\partial t}=-\frac{\partial L}{\partial t}.
$$

So $L$ carries explicit time dependence exactly when $H$ does, with the sign reversed.

### Legendre Involution

The Legendre transform is an involution. Writing $H$ for the transform of $L$, the inverse relation is

$$
L=\mathrm{Sc}\!\left(\bar{\tilde p}\,\dot{\tilde q}\right)-H,\qquad
\dot{\tilde q}=\frac{\partial H}{\partial\tilde p},
$$

provided the Hessian $\partial^2L/\partial\dot q_\mu\partial\dot q_\nu$ is non-singular, which for $L=\tfrac{1}{2}mN(\dot{\tilde q})-V$ it is: the Hessian is $m\delta_{\mu\nu}$.

### Hamilton's Equations

Differentiating $H(\tilde q,\tilde p)=\sum_\mu p_\mu\dot q_\mu-L(\tilde q,\dot{\tilde q})$ and using the definition of $\tilde p$ gives **Hamilton's equations** in quaternion form,

$$
\boxed{\;\dot{\tilde q}=\frac{\partial H}{\partial\tilde p},\qquad \dot{\tilde p}=-\frac{\partial H}{\partial\tilde q}.\;}
$$

**Check on the free particle.** $H_0=N(\tilde p)/2m$ gives $\partial H_0/\partial\tilde p=\tilde p/m=\dot{\tilde q}$ and $\partial H_0/\partial\tilde q=0$, hence $\dot{\tilde p}=0$: constant momentum.

**Check on the oscillator.** With $H$ as above, $\dot{\tilde q}=\tilde p/m$ and $\dot{\tilde p}=-m\omega^2\tilde q$, whose second-order form is $\ddot{\tilde q}=-\omega^2\tilde q$. The flow is a rotation of the $(\tilde q,\tilde p)$ plane at frequency $\omega$, and after a quarter period the configuration has become the momentum and the momentum (up to sign) the configuration. In the biquaternion picture this exchange is the action of the complex structure, as the next section states.

### The Routhian: the Partial Legendre Transform

The Legendre transform need not be applied to all the coordinates at once. When a Lagrangian has $s$ **cyclic** coordinates $q=(q_1,\dots,q_s)$ — coordinates of which $L$ is independent, so that their conjugate momenta are conserved — the transform can be applied to those alone, leaving the remaining coordinates $\zeta=(\zeta_1,\dots,\zeta_{n-s})$ in Lagrangian form. The result is the **Routhian**

$$
R(q,p,\zeta,\dot\zeta)=\mathrm{Sc}\!\left(\bar p\,\dot q\right)-L ,
$$

in which the $s$ transformed coordinates obey Hamilton's equations and the $n-s$ others obey Lagrange's. The Routhian has the form of a Hamiltonian and the role of a Lagrangian: the remaining coordinates satisfy the same Lagrange equations as a system of $n-s$ degrees of freedom whose potential is shifted by the momenta that were removed. A central potential shows the mechanism. The angle $\theta$ is cyclic, its momentum $p_\theta=\ell$ is conserved, and the Routhian is a function of $r$ alone, whose Lagrange equation is

$$
m\ddot r=-V'(r)+\frac{\ell^2}{mr^3},
$$

the centrifugal term appearing as a consequence of the transform rather than as an inserted fictitious force. The partition is arbitrary — nothing requires the transformed coordinates to be the cyclic ones, and choosing them so is a convenience. This article applies the transform to the whole configuration, which is the case $s=n$; the partial case is recorded because it is the general form, and because it shows that which variable is eliminated is a choice of description and not of physics. The other classical reformulation worth naming is **Appell's**, whose equations of motion are written in the **generalized accelerations** $\alpha_r=\ddot q_r$ rather than in the generalized velocities, with the generalized forces of D'Alembert's principle.

## Phase Space as a Single Biquaternion

For a system with three degrees of freedom the position and momentum are pure real quaternions, $\tilde q,\tilde p\in\mathbb{H}_{\mathbb{B}}\cap\mathbb{M}_-$, and they combine into the single biquaternion

$$
\tilde Z=\tilde q+i\tilde p\in\mathbb{B}.
$$

Its anti-Hermitian and Hermitian parts are

$$
\tilde Z_{-}=\tfrac{1}{2}\!\left(\tilde Z-\tilde Z^\dagger\right)=\tilde q\in\mathbb{M}_-,\qquad
\tilde Z_{+}=\tfrac{1}{2}\!\left(\tilde Z+\tilde Z^\dagger\right)=i\tilde p\in\mathbb{M}_+,
$$

as follows from $\tilde q^\dagger=-\tilde q$ and $(i\tilde p)^\dagger=i\tilde p$ for pure real $\tilde q,\tilde p$. The phase-space coordinate is thus a general biquaternion; its **material part is the configuration** and its **informational part is $i$ times the momentum**. The two sectors of the algebra separate position from conjugate momentum, and the decomposition $\mathbb{B}=\mathbb{M}_-\oplus\mathbb{M}_+$ is the algebraic form of the split of the phase space into configuration and momentum.

The algebra's **complex structure** is the map $\tilde Z\mapsto i\tilde Z$. Since $i\mathbb{M}_\pm=\mathbb{M}_\mp$, it exchanges the two parts; explicitly,

$$
i\tilde Z=i\tilde q-\tilde p .
$$

Multiplication by $i$ therefore turns the configuration into (minus) the momentum and the momentum into the configuration, up to the sector assignment. This is why the oscillator's quarter-period evolution exchanges the two: the oscillator flow is a rotation in the plane spanned by $\tilde q$ and $\tilde p$, and the complex structure is that rotation by $\pi/2$. It is also the structural statement behind the observation, in the companion article *The Harmonic Oscillator in Biquaternionic Form*, that the oscillator's phase is generated by the sector-exchanging element $ie_0$.

The same assembly works for a system with four degrees of freedom, with $\tilde q,\tilde p$ general real quaternions, and the sector split then reads

$$
\tilde Z_{+}=\tfrac{1}{2}\!\left(\tilde Z+\tilde Z^\dagger\right)=q_0\,e_0+i\,\mathbf p ,\qquad
\tilde Z_{-}=\tfrac{1}{2}\!\left(\tilde Z-\tilde Z^\dagger\right)=i\,p_0\,e_0+\mathbf q ,
$$

so that the two vector parts separate as configuration and momentum while the two scalar components pair the other way: the configuration scalar $q_0$ is Hermitian and the momentum scalar $i\,p_0$ is anti-Hermitian. The clean statement — material part the configuration, informational part $i$ times the momentum — is the three-degree-of-freedom case $q_0=p_0=0$, which is also the one that carries the spatial reading.

## The Poisson Bracket

### The Biquaternion Form

For central-valued observables $f(\tilde q,\tilde p)$, $g(\tilde q,\tilde p)$, the Poisson bracket is the scalar part of a quaternion expression. Define the gradients

$$
\nabla_{\tilde q}f=\sum_\mu e_\mu\frac{\partial f}{\partial q_\mu},\qquad
\nabla_{\tilde p}f=\sum_\mu e_\mu\frac{\partial f}{\partial p_\mu}.
$$

Using $\mathrm{Sc}(\bar{\tilde a}\tilde b)=\sum_\mu a_\mu b_\mu$ for real quaternions, the bracket is

$$
\boxed{\;\{f,g\}=\mathrm{Sc}\!\left(\overline{\nabla_{\tilde q}f}\;\nabla_{\tilde p}g\right)
-\mathrm{Sc}\!\left(\overline{\nabla_{\tilde p}f}\;\nabla_{\tilde q}g\right).\;}
$$

Only the scalar part of each quaternion product enters. For pure $\tilde a,\tilde b$ the product $\bar{\tilde a}\tilde b$ has a vector part as well, $-\tilde a\times\tilde b$; in general the vector part is $a_0\mathbf b-b_0\mathbf a-\mathbf a\times\mathbf b$, and only the cross-product term is intrinsic to the pairing. The Poisson bracket discards it, and the discarded part is precisely the cross-product structure that reappears as the angular-momentum bracket below. This is the algebraic content of the statement that the classical bracket is the antisymmetric scalar pairing of two gradients.

Because the bracket is built from scalar parts of quaternion products, it is automatically bilinear and antisymmetric, and in these coordinates it is the canonical bracket in disguise, so it satisfies the Jacobi identity. The derivation property $\{f,gh\}=\{f,g\}h+g\{f,h\}$ holds for the commutative product of central-valued functions, exactly as in the standard theory.

### Canonical Brackets

For the coordinate and momentum functions $q_\mu$, $p_\nu$ one has $\nabla_{\tilde q}q_\mu=e_\mu$, $\nabla_{\tilde q}p_\nu=0$, and so

$$
\{q_\mu,q_\nu\}=0,\qquad \{p_\mu,p_\nu\}=0,\qquad \{q_\mu,p_\nu\}=\delta_{\mu\nu}.
$$

These are the standard canonical brackets, written with the algebra's basis rather than with an index list. Hamilton's equations take the bracket form

$$
\dot f=\{f,H\},
$$

which for $f=q_\mu,p_\nu$ reproduces $\dot q_\mu=\partial H/\partial p_\mu$, $\dot p_\nu=-\partial H/\partial q_\nu$.

### Canonical Transformations

A change of phase-space variables $(\tilde q,\tilde p)\to(\tilde Q,\tilde P)$ that preserves the form of Hamilton's equations is a **canonical transformation**, and the test is a statement about the bracket alone:

$$
\{Q_\mu,Q_\nu\}=0,\qquad \{P_\mu,P_\nu\}=0,\qquad \{Q_\mu,P_\nu\}=\delta_{\mu\nu},
$$

evaluated with the original bracket. A transformation satisfying these is canonical; one that fails any of them is not. The criterion is worth recording for a reason specific to this article: it is **scalar**. It never asks what the discarded vector part of the quaternion product does. That is the sharpest support for the claim made below in *What the Bracket Is Not*: the classical structure of the theory, including which changes of variable are permitted, lives entirely in the scalar projection of the quaternion product, while the vector part carries the rotations. The generating functions of such transformations are the ones whose freedom the Standard Formulation notes: the Hamiltonian is fixed only up to the partial time derivative of an arbitrary function of coordinates, momenta and time.

### Angular Momentum

For a particle the quantity

$$
\tilde L=\tilde q\,\tilde p
$$

decomposes, for the pure-vector configuration $\tilde q,\tilde p$ that carries the spatial reading, as $\tilde L=-\mathbf q\cdot\mathbf p+\mathbf q\times\mathbf p$; the scalar part is (minus) the contraction of position and momentum, and the **vector part is the angular momentum** $\mathbf L=\mathbf q\times\mathbf p$. This is the biquaternion form of the cross-product formula $\mathbf L=\mathbf r\times\mathbf p$. Its components satisfy, as in the companion article *Similitudes Between Biquaternion Rotors and Hamiltonian Flow*,

$$
\{L_i,L_j\}=\varepsilon_{ijk}L_k,\qquad \{L_i,q_j\}=\varepsilon_{ijk}q_k,\qquad \{L_i,p_j\}=\varepsilon_{ijk}p_k .
$$

The first of these is the statement that the components of angular momentum close into $\mathfrak{su}(2)$ under the Poisson bracket; it is the bracket that the biquaternion algebra realizes **exactly**, because the quaternion product already carries the cross product, with no deformation parameter. The companion article *Similitudes Between Biquaternion Rotors and Hamiltonian Flow* identifies the corresponding one-parameter group: on the coadjoint orbit, the flow generated by $H=2G\cdot\mathbf S$ is the rotor conjugation by $\exp(tG)$, and the generators agree term for term.

### What the Bracket Is Not

The bracket defined above is the classical Poisson bracket of a commutative algebra of central-valued functions. It is not a commutator, and it does not require or imply one. The companion article *Similitudes Between the Poisson Bracket and the Quantum Commutator* shows that the two brackets are not isomorphic, and that the canonical algebra of a Heisenberg pair cannot be realized inside the finite-dimensional algebra $\mathbb{B}$; the companion article *The Harmonic Oscillator in Biquaternionic Form* confirms the obstruction in the oscillator setting. Nothing in the present article uses that obstruction, because the classical formulation needs no commutator; the bracket is the scalar pairing of gradients, and the algebra supplies it directly.

## The Action, Symmetries, and Conservation

The action of the biquaternion formulation is

$$
S[\tilde q]=\int L(\tilde q,\dot{\tilde q},t)\,dt ,
$$

a central-valued functional of a real-quaternion path. Its stationarity gives the Euler–Lagrange equation derived above; the next article develops the action principle and the stationary-phase statement of the classical limit.

The symmetries that the algebra makes visible are the following.

**Time translation.** If $L$ has no explicit time dependence, Noether's theorem gives the conserved energy $E=\mathrm{Sc}(\bar{\tilde p}\dot{\tilde q})-L=H$.

**Configuration-space rotations.** A rotation of the configuration acts by the **rotor conjugation**

$$
\tilde q\longmapsto \tilde R\,\tilde q\,\tilde R^\dagger,\qquad \tilde R\in\mathbb{H}_{\mathbb{B}},\quad \tilde R\bar{\tilde R}=e_0 .
$$

The norm form is invariant, $N(\tilde R\tilde q\tilde R^\dagger)=N(\tilde q)$, because the rotor has unit norm form. If the potential is rotationally invariant, so is the Lagrangian, and the conserved Noether charge is the angular momentum $\tilde L=\tilde q\tilde p$ of the previous section, that is its vector part $\mathbf q\times\mathbf p$. This is the classical mechanics reading of the rotor: the rotation group is the group of unit real quaternions $SU(2)$, acting on the configuration by conjugation. The companion article *Similitudes Between Biquaternion Rotors and Hamiltonian Flow* develops the rotor-flow correspondence, and the companion article *Noether's Theorem in Biquaternionic Form* develops the general current construction.

**The central phase.** Because $i$ is central, a central phase acts on the biquaternion-valued configuration by $\tilde q\mapsto e^{i\alpha}\tilde q$. For a real-quaternion configuration it does not preserve the real subspace — $e^{i\alpha}\tilde q$ is a complex biquaternion unless $\tilde q=0$ — so it is a symmetry of the complexified formulation rather than of the real configuration space; it becomes a genuine internal symmetry only for a complex biquaternion-valued field, where it is the $U(1)$ of the companion article *The Gauge Principle in Biquaternionic Form*. It also acts on the free Lagrangian, $L=\tfrac12mN(\dot{\tilde q})\mapsto e^{2i\alpha}L$, so a real Lagrangian is invariant only for $e^{2i\alpha}=1$: the transformation is a symmetry of the complexified formulation and not of the real one. In the present classical setting it acts on the phase-space biquaternion $\tilde Z$ and is the algebra's complex structure; its consequences for the action and for the symplectic structure are developed in the companion articles *The Action Principle and the Classical Limit as Stationary Phase in Biquaternionic Form* and *The Symplectic Form and the Biquaternion Norm-Form Cone*.

## What the Formulation Does and Does Not Give

The transcription is exact within its domain, and the domain is worth stating plainly.

**What it gives.** For a system whose configuration is a real quaternion — a particle in three dimensions with an optional scalar degree of freedom — the Lagrangian and Hamiltonian formalism is written without index clutter: the kinetic energy is the norm form, the momentum is its Legendre conjugate, the Hamiltonian of a free particle is the norm form of the momentum, the Euler–Lagrange and Hamilton equations are single quaternion equations, and the Poisson bracket is the scalar pairing of two quaternion gradients. The phase-space coordinate is one biquaternion whose sectors are the configuration and the momentum. The rotational bracket is exact, with the quaternion product's cross product supplying the structure constants.

**What it does not give.** The algebra is finite dimensional; it cannot carry the configuration space of a system with more than a few degrees of freedom, nor an infinite-dimensional field configuration except through its coefficients. The Poisson bracket is a scalar projection of a quaternion product, and the vector part it discards is not a second bracket. And the canonical Heisenberg sector is absent: there is no pair $\tilde q,\tilde p$ inside $\mathbb{B}$ whose bracket is a central constant, as the companion articles *Similitudes Between the Poisson Bracket and the Quantum Commutator* and *The Harmonic Oscillator in Biquaternionic Form* prove. None of these limitations is a defect of the transcription; they are properties of the algebra, and they mark where the biquaternion language is a convenience and where it is a constraint.

## Summary

The Lagrangian and Hamiltonian formulations of classical mechanics take the following form in the biquaternion algebra.

- The configuration is a real quaternion $\tilde q\in\mathbb{H}_{\mathbb{B}}$, with the physical three-space as its pure-vector part; the kinetic energy is the norm form, $T=\tfrac{1}{2}mN(\dot{\tilde q})$.
- The action $S[\tilde q]=\int L\,dt$ is stationary at the physical path, and stationarity gives the single quaternion Euler–Lagrange equation $\frac{d}{dt}\partial_{\dot{\tilde q}}L-\partial_{\tilde q}L=0$, equivalent to the four real equations.
- The conjugate momentum is $\tilde p=\partial L/\partial\dot{\tilde q}$, and the Hamiltonian is the Legendre transform $H=\mathrm{Sc}(\bar{\tilde p}\dot{\tilde q})-L$. For a free particle $H=N(\tilde p)/2m$: the free Hamiltonian is the norm form of the momentum.
- Hamilton's equations are $\dot{\tilde q}=\partial_{\tilde p}H$, $\dot{\tilde p}=-\partial_{\tilde q}H$.
- Position and momentum combine into the phase-space biquaternion $\tilde Z=\tilde q+i\tilde p$, whose anti-Hermitian part is the configuration and whose Hermitian part is $i$ times the momentum. The algebra's complex structure $i$ exchanges the two parts.
- The Poisson bracket is $\{f,g\}=\mathrm{Sc}(\overline{\nabla_{\tilde q}f}\nabla_{\tilde p}g)-\mathrm{Sc}(\overline{\nabla_{\tilde p}f}\nabla_{\tilde q}g)$, the scalar part of a quaternion expression; the discarded vector part is the cross product that makes the angular-momentum bracket $\{L_i,L_j\}=\varepsilon_{ijk}L_k$ exact.
- Rotational symmetry acts by rotor conjugation $\tilde q\mapsto\tilde R\tilde q\tilde R^\dagger$, and its Noether charge is $\tilde L=\tilde q\tilde p$.
- The Lagrangian is determined only up to a total time derivative: $L$ and $L+dF(q,t)/dt$ have the same equations of motion, and their actions differ by the endpoint term $F(t_2)-F(t_1)$, which a variation with fixed endpoints cannot see. This is the same boundary freedom that appears as the symplectic potential in the variation of the action.
- The Legendre transform may be applied to a subset of the coordinates. The partial transform is the **Routhian**, which puts the transformed coordinates — conventionally the cyclic ones, whose momenta are conserved — in Hamiltonian form and the rest in Lagrangian form; for a central potential it produces the centrifugal term as a transformed potential.
- In the Hamiltonian description coordinates, velocities and momenta are **mutually independent** variables; the relation $\tilde p=\partial L/\partial\dot{\tilde q}$ is used only to eliminate the velocity. This is what makes the transform a change of variables and $\tilde Z=\tilde q+i\tilde p$ a coordinate.
- $H=T+V$ is not automatic. It requires $T$ homogeneous of degree two in the velocities, which $T=\tfrac12mN(\dot{\tilde q})$ satisfies by construction; with $L$ time-independent, $H$ is then the conserved energy. Explicit time dependence is preserved by the transform, $\partial H/\partial t=-\partial L/\partial t$.
- A change of phase-space variables is **canonical** exactly when it preserves the brackets $\{Q_\mu,P_\nu\}=\delta_{\mu\nu}$. The criterion is scalar, so the permitted changes of variable live in the scalar projection of the quaternion product alone.

The formulation is a transcription, exact for configurations that fit in a real quaternion. It introduces no commutator and no $\hbar$; the canonical Heisenberg structure is absent from the finite-dimensional algebra, and the classical bracket that the algebra does carry is the scalar part of a quaternion product.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_0=1,e_1,e_2,e_3$ | Quaternion basis, $e_k^2=-e_0$ |
| $i$ | Central scalar imaginary, $i^2=-1$ |
| $\mathbb{M}_-,\mathbb{M}_+$ | Anti-Hermitian (material) and Hermitian (informational) sectors |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace |
| $\tilde q=q_0e_0+\mathbf q$ | Configuration quaternion (real) |
| $\dot{\tilde q}$ | Configuration velocity |
| $N(\tilde q)=\tilde q\bar{\tilde q}$ | Norm form |
| $L(\tilde q,\dot{\tilde q},t)$ | Lagrangian |
| $F(\tilde q,t)$, $L'=L+dF/dt$ | Arbitrary function and the total-derivative ambiguity of the Lagrangian |
| $S[\tilde q]=\int L\,dt$ | Action; ambiguous by the endpoint term $F(t_2)-F(t_1)$ |
| $R=\mathrm{Sc}(\bar p\,\dot q)-L$ (over the transformed block) | Routhian: the partial Legendre transform, shown in the general case, of which this article uses $s=n$ |
| $T(\lambda\dot{\tilde q})=\lambda^2T(\dot{\tilde q})$ | Homogeneity of the kinetic energy; gives $\mathrm{Sc}(\bar{\tilde p}\dot{\tilde q})=2T$ and $H=T+V$ |
| $\partial H/\partial t=-\partial L/\partial t$ | Explicit time dependence is preserved with reversed sign |
| $\{Q_\mu,P_\nu\}=\delta_{\mu\nu}$ | Canonical-transformation criterion (scalar) |
| $\partial_{\tilde q}L=\sum_\mu e_\mu\partial L/\partial q_\mu$ | Quaternion gradient of a central-valued function |
| $\tilde p=\partial L/\partial\dot{\tilde q}$ | Conjugate momentum (real quaternion) |
| $H=\mathrm{Sc}(\bar{\tilde p}\dot{\tilde q})-L$ | Hamiltonian (Legendre transform) |
| $\tilde Z=\tilde q+i\tilde p$ | Phase-space biquaternion |
| $\nabla_{\tilde q}f,\nabla_{\tilde p}f$ | Gradients of an observable |
| $\{f,g\}$ | Poisson bracket |
| $\tilde L=\tilde q\tilde p$ | Angular momentum (vector part $\mathbf q\times\mathbf p$) |
| $\tilde R\in\mathbb{H}_{\mathbb{B}}$, $N(\tilde R)=e_0$ | Rotation rotor |
| $\mathrm{Tr}(e_0)=2$ | Trace normalization |

## Further Reading

- H. Goldstein, C. P. Poole, and J. L. Safko, *Classical Mechanics* (Addison-Wesley, 2002), for the standard Lagrangian and Hamiltonian formulation, the Legendre transform, and the Poisson bracket.
- L. D. Landau and E. M. Lifshitz, *Mechanics* (Pergamon, 1976), for the action principle, Noether's theorem, and canonical equations.
- V. I. Arnold, *Mathematical Methods of Classical Mechanics* (Springer, 1989), for the symplectic and Poisson-geometric formulation of Hamiltonian mechanics.
- W. R. Hamilton, *Lectures on Quaternions* (Hodges and Smith, 1853), for the quaternion algebra and the quaternion product.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for quaternions, rotors, and their relation to the Lorentz group.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric-algebra treatment of rotors, rigid bodies, and mechanics.
- David Hestenes, *New Foundations for Classical Mechanics* (Reidel, 1986), for a treatment of classical mechanics in a real Clifford algebra closely related to the quaternion one.
