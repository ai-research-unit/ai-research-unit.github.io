# __The Non-Quantum Limit of the Action Principle and the Lagrangian__

## Introduction

**Two formulations and two statements are joined in this article.** Classical mechanics admits a Lagrangian formulation, in which a system is specified by a configuration space and a function $\mathrm{Lag}(q,dq/dt',r'_t)$ whose variational principle selects the motion, and a Hamiltonian formulation, in which the same system is specified by a phase space and a Hamiltonian $H(q,p,r'_t)$ obtained by the Legendre transform. The principle those formulations serve is the **action principle**: the physical trajectory is the one at which the action is stationary,

$$
S[\tilde q]=\int \mathrm{Lag}\,dt',\qquad \delta S=0\quad\Longleftrightarrow\quad \frac{d}{dt'}\frac{\partial \mathrm{Lag}}{\partial\left(d\tilde q/dt'\right)}-\frac{\partial \mathrm{Lag}}{\partial\tilde q}=0 .
$$

The **non-quantum limit** is the second statement. When a sum over trajectories is weighted by the phase $\exp(i\theta_{\mathrm{act}})$, the sum is dominated as $h\to0$ by the trajectories near the stationary ones, so the classical paths are exactly the critical points of the action. That is a theorem of analysis — the stationary-phase lemma of Kelvin, developed by many hands — and it is not a quantisation.

**Nothing here is new in the physics.** Both formulations and both statements are textbook material, and this article derives none of them. What it does is write them in the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ and state exactly which parts of the two formulations the algebra fixes and which it does not reach.

**What the algebra supplies, in five statements.**

1. **The kinetic energy is the biquaternion norm.** For a configuration assembled into a real quaternion $\tilde q$, the free kinetic energy is $\tfrac{m}{2}\langle\,d\tilde q/dt'\rangle_{\natural}$, the algebra's own quadratic form, and the free Lagrangian is a scalar multiple of it.
2. **The phase-space coordinate is one biquaternion.** Position and momentum assemble into $\tilde Q_3=\tilde q+i\tilde p$, whose anti-Hermitian part is the configuration and whose Hermitian part is $i$ times the momentum. The algebra's complex structure is the phase-space complex structure.
3. **The action is central-valued.** For a real-quaternion configuration the Lagrangian is central, so the action is a complex scalar and its phase is unambiguous. There is no ordering question in the exponent, and the stationary-phase construction applies directly.
4. **A rotor-valued path has a geodesic action.** For a path in the group of unit real quaternions, the action built from the biquaternion norm of the velocity is the energy of a geodesic on the group, and the classical path is a one-parameter subgroup. This is the one place where the algebra's noncommutativity produces the classical equations rather than merely expressing them.
5. **The boundary is finite-dimensional.** The algebra is eight-dimensional over $\mathbb{R}$. It carries the configuration of a system with at most four real degrees of freedom, and it carries the *rotational* bracket exactly. It does not carry the canonical Heisenberg structure: there is no pair $\tilde q,\tilde p$ inside $\mathbb{B}$ whose commutator is a nonzero central constant, as the companion articles *Similitudes Between the Poisson Bracket and the Quantum Commutator* and *The Harmonic Oscillator in Biquaternionic Form* establish.

**The boundary is stated once and kept.** This article is classical throughout. No commutator is introduced, no state space and no operator appears, and no relation of the form $[\tilde q,\tilde p]=i \frac{h}{2\pi}$ is used or needed. The symbol $\frac{h}{2\pi}$ enters in one section only, as the inverse scale of the phase in an asymptotic expansion. The two halves of the article take the same side of that line: the first writes the two formulations, and the second writes the principle and its classical limit.

**The place of the article in the series.** This is the one article on which the fifty family articles rest. The configuration, the Lagrangian, the Euler–Lagrange equation, the Legendre transform, the phase-space biquaternion, the Poisson bracket, the canonical criterion and the conservation laws are established in the first half. The first variation and the boundary term that gives the symplectic potential, the second variation and the Jacobi operator, the geodesic principle for a rotor-valued path, the stationary-phase evaluation of the classical limit, and the Hamilton–Jacobi equation are established in the second half. The family's articles apply that principle to one equation each, in an element form and in a polar form, and add nothing to the formalism established here.

## Conventions

**The algebra.** $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$; the quaternion basis is $e_t=1,\vec e_x,\vec e_y,\vec e_z$ with $\vec e_{\imath}^2=-e_t$ and $\vec e_{\imath}\vec e_{\jmath}=-\delta_{\imath\jmath}e_t+\varepsilon_{\imath\jmath k}\vec e_{\imath}$; the scalar imaginary $i$ is central with $i^2=-1$. The anti-Hermitian subspace $\mathbb{B}_{\Phi}$ (imaginary scalar, real vector) is the material sector, the Hermitian subspace $\mathbb{B}_{\Psi}$ (real scalar, imaginary vector) is the informational sector, and $\mathbb{B}=\mathbb{B}_{\Phi}\oplus\mathbb{B}_{\Psi}$. The real-quaternion subspace is $\mathbb{B}_{H}$.

**The configuration and its conjugates.** The configuration is a real quaternion $\tilde q\in\mathbb{B}_{H}$, with the physical three-space as its pure-vector part and $r'_t$ the time of the read list. Its conjugate momentum is

$$
\tilde p=\frac{\partial \mathrm{Lag}}{\partial\left(d\tilde q/dt'\right)},
$$

the phase-space biquaternion is $\tilde Q_3=\tilde q+i\tilde p$, and the scalar pairing is $\mathrm{Sc}(\tilde q_3^{\natural}\tilde q_4)=\sum_{\imath} q_{3\imath}q_{4\imath}$. The quaternion gradient of a central-valued function is $\partial \mathrm{Lag}/\partial\tilde q=\sum_{\imath} e_{\imath}\,\partial \mathrm{Lag}/\partial q_{\imath}$.

**The companion articles.** The pieces are supplied as follows.

- Companion article *The Material Sector: Four-Vectors, Interval and Lorentz Action*, for the material sector, the biquaternion norm and the four-vectors.
- Companion article *The Informational Sector: States, Observables and Probability*, for the Hermitian sector, the pairing formula and the conjugation action.
- Companion article *Similitudes Between the Poisson Bracket and the Quantum Commutator*, for the classical bracket conventions and the boundary between the classical and quantum brackets.
- Companion article *Similitudes Between Biquaternion Rotors and Hamiltonian Flow*, for the rotor and the Hamiltonian flow on the coadjoint orbit.
- Companion article *The Harmonic Oscillator in Biquaternionic Form*, for the phase plane and the sector structure of a mode.
- Companion article *Noether's Theorem in Biquaternionic Form*, for the boundary-term construction of conserved quantities.

## The Standard Formulation

The standard Lagrangian and Hamiltonian formalism is recalled here in the form the biquaternion transcription will take; nothing in this section is new.

The formalism is not an independent postulate. It follows from **D'Alembert's principle of virtual work** — the infinitesimal virtual work done by the impressed forces across displacements consistent with the constraints vanishes, which is the statement that the constraint forces do no work. Eliminating those forces is what allows the constraints to be absorbed into the geometry of the coordinates: a system of $\mathcal N$ constituents in three dimensions with $\kappa$ independent constraints has $3\mathcal N-\kappa$ **degrees of freedom**, described by the same number of **generalized coordinates** $q_i$, one per degree of freedom. These are not curvilinear coordinates. The number of curvilinear coordinates is the dimension of the position space — three, for three-dimensional space — whereas the number of generalized coordinates is the number of degrees of freedom, which constraints reduce and additional constituents raise; the two counts need not agree. A constraint expressible as $\vec r=\vec r(q,r'_t)$ holding for all $r'_t$ is **holonomic**; it is **scleronomic** when the relation carries no explicit time and **rheonomic** when it does. The Lagrange equation obtained below is the generalized form of Newton's second law that results, and the stationary-action statement is its equivalent formulation in integral form.

Let a system have $n$ generalized coordinates $q=(q_1,\dots,q_n)$ and velocities $dq/dt'$, where $t'=r'_t/c$ is the time in seconds and $r'_t$ the temporal coordinate. The **Lagrangian** is a smooth real function $\mathrm{Lag}(q,dq/dt',r'_t)$, and the **action** is the functional

$$
S[q]=\int_{t'_1}^{t'_2}\mathrm{Lag}(q,dq/dt',r'_t)\,dt' .
$$

The **principle of stationary action** states that the physical trajectory is a stationary point of $S$ among paths with fixed endpoints. For an arbitrary variation $\delta q(r'_t)$ vanishing at the endpoints,

$$
\delta S=\int_{t'_1}^{t'_2}\left(\frac{\partial \mathrm{Lag}}{\partial q_i}\,\delta q_i+\frac{\partial \mathrm{Lag}}{\partial \left(dq_{i}/dt'\right)}\,\delta\left(dq_{i}/dt'\right)\right)dr'_t
=\int_{t'_1}^{t'_2}\left(\frac{\partial \mathrm{Lag}}{\partial q_i}-\frac{d}{dt'}\frac{\partial \mathrm{Lag}}{\partial \left(dq_{i}/dt'\right)}\right)\delta q_i\,dt' ,
$$

after an integration by parts. Stationarity for all $\delta q$ gives the **Euler–Lagrange equations**

$$
\frac{d}{dt'}\frac{\partial \mathrm{Lag}}{\partial \left(dq_{i}/dt'\right)}-\frac{\partial \mathrm{Lag}}{\partial q_i}=0 .
$$

The Lagrangian is **not unique**, and the extent of the ambiguity is a boundary term. For any smooth $F(q,r'_t)$, the Lagrangians $\mathrm{Lag}$ and

$$
\mathrm{Lag}_2=\mathrm{Lag}+\frac{d}{dt'}F(q,r'_t)
$$

have the same Euler–Lagrange equations. The added term enters both terms of the Euler–Lagrange operator as the same expression, $d/dt'(\partial F/\partial q_i)$: once as $\partial/\partial q_i\,(dF/dt')$, and once as $d/dt'\big(\partial/\partial\left(dq_{i}/dt'\right)\,(dF/dt')\big)=d/dt'(\partial F/\partial q_i)$, since the mixed partials of $F$ commute. The two contributions cancel. The action is ambiguous in the corresponding way,

$$
S_2=S+F\big(q(t'_2),t'_2\big)-F\big(q(t'_1),t'_1\big) ,
$$

the difference being an endpoint term, which a variation with fixed endpoints cannot see. What the formalism determines is therefore the **equations of motion**, not the Lagrangian, and the ambiguity is exactly a boundary term: the same structure the companion article *The Lagrangian and the Non-Quantum Limit: The Action Principle* meets from the other side, where the boundary term of $\delta S$ is the symplectic potential. The Hamiltonian carries the analogous freedom — a generating function of the coordinates, momenta and time shifts it by a partial time derivative — and that is the freedom a canonical transformation exploits.

The **conjugate momenta** are $p_i=\partial \mathrm{Lag}/\partial \left(dq_{i}/dt'\right)$. In the Hamiltonian description the coordinates, velocities and momenta are **mutually independent** variables: the relation $p_i=\partial \mathrm{Lag}/\partial\left(dq_{i}/dt'\right)$ is used once, to eliminate the velocities in favour of the momenta, and does not thereafter act as a constraint among the phase-space variables. So $H(q,p)$ is differentiated with respect to $p_i$ at fixed $q$, with $dq/dt'$ already eliminated; holding $dq/dt'$ fixed while varying $p_i$ would describe a different object. This is what makes the passage a change of variables rather than a definition, and it is why the phase-space element $\tilde Q_3=\tilde q+i\tilde p$ constructed below is a coordinate. When the Hessian matrix $\partial^2\mathrm{Lag}/\partial\left(dq_{i}/dt'\right)\partial\left(dq_{j}/dt'\right)$ is non-singular, the map $(q,dq/dt')\mapsto(q,p)$ is invertible, and the **Legendre transform**

$$
H(q,p,r'_t)=p_i\,dq_{i}/dt'-\mathrm{Lag}(q,dq/dt',r'_t)
$$

defines the **Hamiltonian**. Its differential gives **Hamilton's equations**

$$
dq_{i}/dt'=\frac{\partial H}{\partial p_i},\qquad
\,dp_{i}/dt'=-\frac{\partial H}{\partial q_i}.
$$

For observables $f(q,p)$, $g(q,p)$, the **Poisson bracket** is

$$
\{f,g\}=\frac{\partial f}{\partial q_i}\frac{\partial g}{\partial p_i}-\frac{\partial f}{\partial p_i}\frac{\partial g}{\partial q_i},
$$

and the dynamics is $df/dt'=\{f,H\}$. The bracket is bilinear, antisymmetric, and satisfies the Jacobi identity; it is a derivation of the commutative algebra of observables under pointwise multiplication.

### The Rayleigh Dissipation Function

Friction has no place in the mechanical Lagrangian. A force proportional to the velocity, such as a Stokes drag, is not the gradient of a potential $V(q,r'_t)$, so it cannot be absorbed into $\mathrm{Lag}=T-V$. The classical device that keeps the equations in Lagrangian form adds it instead as a **generalized force** on the right-hand side,

$$
\frac{d}{dt'}\frac{\partial \mathrm{Lag}}{\partial\left(dq_{i}/dt'\right)}-\frac{\partial \mathrm{Lag}}{\partial q_i}=-\frac{\partial F}{\partial\left(dq_{i}/dt'\right)},
$$

with **Rayleigh's dissipation function** $F=\tfrac12\sum_{ij}b_{ij}\,dq_i/dt'\,dq_j/dt'$, the quadratic form whose gradient is the viscous force. For a single coordinate and the mechanical Lagrangian this is the damped oscillator $m\,d^2q/d{t'}^2+b\,dq/dt'+dV/dq=0$. The energy $E=\sum_i dq_i/dt'\,\partial \mathrm{Lag}/\partial\left(dq_i/dt'\right)-\mathrm{Lag}$ is no longer conserved; it decreases at the rate

$$
\frac{dE}{dt'}=-\sum_i dq_i/dt'\,\frac{\partial F}{\partial\left(dq_i/dt'\right)}=-2F,
$$

the last equality because $F$ is homogeneous of degree two in the velocities. The dissipation function is therefore half the rate at which the energy falls, and it vanishes only at rest.

What the device does not do is restore the symmetry of the formalism: the force is inserted by hand rather than derived from a Lagrangian, and the energy, the conserved quantity of the autonomous case, becomes a decreasing function. It is the classical face of the dichotomy drawn in the article *Quantum Channels and the Reversible/Irreversible Dichotomy*, where the evolution generated inside the algebra is reversible and the dissipative evolution is not.

## The Biquaternionic Configuration

### Coordinates and the Gradient

Assemble the generalized coordinates of a system with at most four degrees of freedom into a **real quaternion**

$$
\tilde q=q_t\,e_t+q_x\,\vec e_x+q_y\,\vec e_y+q_z\,\vec e_z\in\mathbb{B}_{H} ,
$$

with real components $q_{\imath}$. The physical three-space is the pure real part $\vec q=q_x\vec e_x+q_y\vec e_y+q_z\vec e_z\in\mathbb{B}_{H}\cap\mathbb{B}_{\Phi}$, and the central coordinate $q_te_t\in\mathbb{B}_{C}\cap\mathbb{B}_{H}$ is a fourth, scalar degree of freedom. A system with three degrees of freedom is the special case $q_t=0$; the pure-vector configuration is the one that carries the spatial interpretation.

For a central-valued function $F(\tilde q)$ — a function taking values in $\mathbb{B}_{C}$ — define the **quaternion gradient** componentwise,

$$
\partial F/\partial\tilde q=\sum_{\imath\in\{t,x,y,z\}}e_{\imath}\,\frac{\partial F}{\partial q_{\imath}}.
$$

Because $F$ is central, this gradient is unambiguous: the quaternion product does not enter the definition, and the left and right derivatives of a central-valued function of real quaternion variables agree. The pairing that makes it a derivative is the scalar pairing,

$$
dF=\mathrm{Sc}\!\left((\partial F/\partial\tilde q)^{\natural}\,d\tilde q\right)
=\sum_{\imath\in\{t,x,y,z\}}\frac{\partial F}{\partial q_{\imath}}\,dq_{\imath} ,
$$

which uses $\mathrm{Sc}(e_{\imath}^{\natural}e_{\jmath})=\delta_{\imath\jmath}$. This is the statement, in the algebra, that the natural scalar product on the real-quaternion subspace is the scalar part of a quaternion product.

### The Kinetic Energy Is the Biquaternion Norm

Let $\tilde q(r'_t)$ be a trajectory and $d\tilde q/dt'$ its velocity. The **kinetic energy** of a particle of mass $m$ is

$$
\boxed{\;T=\tfrac{1}{2}m\,\langle\,d\tilde q/dt'\rangle_{\natural}=\tfrac{1}{2}m\,d\tilde q/dt'\,(d\tilde q/dt')^{\natural}=\tfrac{1}{2}m\sum_{\imath\in\{t,x,y,z\}}\left(dq_{\imath}/dt'\right)^{2}\;}.
$$

For a pure-vector configuration the central term is absent and $T=\tfrac{1}{2}m|d\vec q/dt'|^2$, the familiar kinetic energy. The kinetic energy is therefore the **biquaternion norm** of the velocity, and this is the first structural fact of the biquaternion formulation of mechanics: the algebra's own quadratic form is the free kinetic energy. The biquaternion norm on $\mathbb{B}_{H}$ is positive definite, so $T\ge0$ with equality only for $d\tilde q/dt'=0$; no sign choice has to be made.

The free Lagrangian is

$$
L_0=\tfrac{1}{2}m\,\langle\,d\tilde q/dt'\rangle_{\natural},
$$

and a particle in a central potential $V(\tilde q)$ has

$$
\mathrm{Lag}=\tfrac{1}{2}m\,\langle\,d\tilde q/dt'\rangle_{\natural}-V(\tilde q).
$$

### The Euler–Lagrange Equations

Vary the action $S[\tilde q]=\int \mathrm{Lag}\,dt'$ with fixed endpoints. Using the scalar pairing, the first variation is

$$
\delta S=\int\left[\mathrm{Sc}\!\left((\partial \mathrm{Lag}/\partial\tilde q)^{\natural}\,\delta\tilde q\right)+\mathrm{Sc}\!\left((\partial \mathrm{Lag}/\partial\left(d\tilde q/dt'\right))^{\natural}\,\delta\,d\tilde q/dt'\right)\right]dr'_t ,
$$

and an integration by parts turns the second term into a total derivative plus

$$
\delta S=\int \mathrm{Sc}\!\left[\left(\partial \mathrm{Lag}/\partial\tilde q-\frac{d}{dt'}\partial \mathrm{Lag}/\partial\left(d\tilde q/dt'\right)\right)^{\natural}\,\delta\tilde q\right]dr'_t
+\left[\mathrm{Sc}\!\left((\partial \mathrm{Lag}/\partial\left(d\tilde q/dt'\right))^{\natural}\,\delta\tilde q\right)\right]_{t'_1}^{t'_2}.
$$

The endpoint term vanishes because $\delta\tilde q(t'_1)=\delta\tilde q(t'_2)=0$. Since $\delta\tilde q$ is an arbitrary real quaternion at each time, stationarity of $S$ requires the bracket to vanish, and the **Euler–Lagrange equation** takes the quaternion form

$$
\boxed{\;\frac{d}{dt'}\frac{\partial \mathrm{Lag}}{\partial\left(d\tilde q/dt'\right)}-\frac{\partial \mathrm{Lag}}{\partial\tilde q}=0\;}
\qquad\text{with}\qquad
\frac{\partial \mathrm{Lag}}{\partial\left(d\tilde q/dt'\right)}=\sum_{\imath} e_{\imath}\frac{\partial \mathrm{Lag}}{\partial\left(dq_{\imath}/dt'\right)},\quad
\frac{\partial \mathrm{Lag}}{\partial\tilde q}=\sum_{\imath} e_{\imath}\frac{\partial \mathrm{Lag}}{\partial q_{\imath}}.
$$

This single quaternion equation is the four real Euler–Lagrange equations, one for each component $q_{\imath}$.

**Free particle.** For $L_0=\tfrac{1}{2}m\langle d\tilde q/dt'\rangle_{\natural}$ the gradient is $\partial L_0/\partial\left(d\tilde q/dt'\right)=m\,d\tilde q/dt'$ and $\partial L_0/\partial\tilde q=0$, so the equation is $md^2\tilde q/d{r'_{t}}^2=0$: straight-line motion at constant velocity, as it must be.

**Central potential.** For $\mathrm{Lag}=\tfrac{1}{2}m\langle d\tilde q/dt'\rangle_{\natural}-V(\tilde q)$, the equation is

$$
md^2\tilde q/d{r'_{t}}^2=-\partial V/\partial\tilde q .
$$

When $V$ is a function of the real-quaternion modulus $\langle\tilde q\rangle_{\natural}$ alone, the right-hand side is $-\partial V/\partial\tilde q=-2\,\frac{dV}{d\langle\tilde q\rangle_{\natural}}\,\tilde q$, a central force. The biquaternion equation is then the vector equation of a central-force problem; the specific force laws belong to the subcategory on effects without intrinsic magnetism, and are not developed here.

## The Legendre Transform

### Momentum and Hamiltonian

The **conjugate momentum** is the real quaternion

$$
\tilde p=\frac{\partial \mathrm{Lag}}{\partial\left(d\tilde q/dt'\right)}=\sum_{\imath} e_{\imath} p_{\imath},\qquad p_{\imath}=\frac{\partial \mathrm{Lag}}{\partial\left(dq_{\imath}/dt'\right)}.
$$

For the free particle $\tilde p=m\,d\tilde q/dt'$. The **Hamiltonian** is the Legendre transform

$$
H(\tilde q,\tilde p)=\mathrm{Sc}\!\left(\tilde p^{\natural}\,d\tilde q/dt'\right)-\mathrm{Lag}(\tilde q,d\tilde q/dt')
=\sum_{\imath} p_{\imath}\,dq_{\imath}/dt'-\mathrm{Lag} ,
$$

with $d\tilde q/dt'$ eliminated in favour of $\tilde p$ using the inverse of $\tilde p=\partial \mathrm{Lag}/\partial\left(d\tilde q/dt'\right)$. The scalar pairing $\mathrm{Sc}(\tilde p^{\natural}d\tilde q/dt')=\sum_{\imath} p_{\imath}\,dq_{\imath}/dt'$ is the quaternion form of the contraction $p_i\,dq_{i}/dt'$; the conjugate is required, because $\mathrm{Sc}(\tilde pd\tilde q/dt')$ reverses the sign of the vector-part contribution.

**Free particle.** With $\tilde p=m\,d\tilde q/dt'$ one has $\mathrm{Sc}(\tilde p^{\natural}d\tilde q/dt')=m\langle d\tilde q/dt'\rangle_{\natural}=2T$, and

$$
H_0=\frac{\langle\tilde p\rangle_{\natural}h/(mc) c}{4\pi  \frac{h}{2\pi}}=\frac{\tilde p\,\tilde p^{\natural}h/(mc) c}{4\pi  \frac{h}{2\pi}}=\frac{h/(mc) c}{4\pi  \frac{h}{2\pi}}\sum_{\imath\in\{t,x,y,z\}}p_{\imath}^2 ,
$$

Here $\frac{1}{2\pi\nu_m}$ is the mass length.

the free Hamiltonian, which reduces to the kinetic term $\vec p^2\frac{h}{2\pi (mc) c}/(2\frac{h}{2\pi})$ for a pure-vector momentum, $p_t=0$. The structural statement is the mirror of the one for $L_0$: **the free Hamiltonian is the biquaternion norm of the momentum, divided by $2m$.** The biquaternion norm thus appears at both ends of the Legendre transform, once on velocity and once on momentum, because the Legendre transform of a quadratic form is again a quadratic form, with the mass inverted.

**Harmonic oscillator.** For $\mathrm{Lag}=\tfrac{1}{2}m\langle d\tilde q/dt'\rangle_{\natural}-\tfrac{1}{2}m\omega^2\langle\tilde q\rangle_{\natural}$ the momentum is again $\tilde p=m\,d\tilde q/dt'$ and

$$
H=\frac{\langle\tilde p\rangle_{\natural}h/(mc) c}{4\pi  \frac{h}{2\pi}}+\frac{m\omega^2}{2}\langle\tilde q\rangle_{\natural}.
$$

The Hamiltonian is a sum of two biquaternion norms with positive coefficients, one in the momentum and one in the coordinate. Its level sets $H=E$ are ellipsoids in the eight-dimensional real phase space.

**When is the Hamiltonian the energy?** The identification of $H$ with $T+V$ is not automatic, and the condition is one this transcription satisfies by construction. If the kinetic energy is a **homogeneous function of degree two** in the generalized velocities, $T(\digamma_{\mathrm{scl}}\,dq/dt')=\digamma_{\mathrm{scl}}^2T(dq/dt')$, then Euler's theorem on homogeneous functions gives $dq_{\imath}/dt'\partial T/\partial\left(dq_{\imath}/dt'\right)=2T$. When the potential depends on the coordinates alone, $p_{\imath}=\partial T/\partial\left(dq_{\imath}/dt'\right)$, and therefore

$$
\mathrm{Sc}\!\left(\tilde p^{\natural}\,d\tilde q/dt'\right)=p_{\imath}\,dq_{\imath}/dt'=2T,\qquad H=2T-(T-V)=T+V ,
$$

so $H$ is the total energy, and it is conserved when $\mathrm{Lag}$ has no explicit time dependence. For the systems of this article the hypothesis is not an assumption but a property of the kinetic term: $T=\tfrac12 m\langle d\tilde q/dt'\rangle_{\natural}$ is a quadratic form in the velocities and hence homogeneous of degree two. The condition can fail — a relativistic kinetic energy is not homogeneous of degree two — and where it fails $H$ remains the Legendre transform of $\mathrm{Lag}$ but is no longer the energy.

Explicit time dependence, by contrast, is preserved by the transform. Differentiating $H=p_{\imath}\,dq_{\imath}/dt'-\mathrm{Lag}$ with respect to $r'_t$ at fixed coordinates and momenta, the terms in $\partial\left(dq_{\imath}/dt'\right)/\partial r'_t$ cancel against $p_{\imath}=\partial \mathrm{Lag}/\partial\left(dq_{\imath}/dt'\right)$, leaving

$$
\frac{\partial H}{\partial r'_t}=-\frac{\partial \mathrm{Lag}}{\partial r'_t}.
$$

So $\mathrm{Lag}$ carries explicit time dependence exactly when $H$ does, with the sign reversed.

### Legendre Involution

The Legendre transform is an involution. Writing $H$ for the transform of $\mathrm{Lag}$, the inverse relation is

$$
\mathrm{Lag}=\mathrm{Sc}\!\left(\tilde p^{\natural}\,d\tilde q/dt'\right)-H,\qquad
\,d\tilde q/dt'=\frac{\partial H}{\partial\tilde p},
$$

provided the Hessian $\partial^2\mathrm{Lag}/\partial\left(dq_{\imath}/dt'\right)\partial\left(dq_{\jmath}/dt'\right)$ is non-singular, which for $\mathrm{Lag}=\tfrac{1}{2}m\langle d\tilde q/dt'\rangle_{\natural}-V$ it is: the Hessian is $m\delta_{\imath\jmath}$.

### Hamilton's Equations

Differentiating $H(\tilde q,\tilde p)=\sum_{\imath} p_{\imath}\,dq_{\imath}/dt'-\mathrm{Lag}(\tilde q,d\tilde q/dt')$ and using the definition of $\tilde p$ gives **Hamilton's equations** in quaternion form,

$$
\boxed{\;d\tilde q/dt'=\frac{\partial H}{\partial\tilde p},\qquad \,d\tilde p/dt'=-\frac{\partial H}{\partial\tilde q}\;}.
$$

**Check on the free particle.** $H_0=\langle\tilde p\rangle_{\natural}/2m$ gives $\partial H_0/\partial\tilde p=\tilde p/m=d\tilde q/dt'$ and $\partial H_0/\partial\tilde q=0$, hence $d\tilde p/dt'=0$: constant momentum.

**Check on the oscillator.** With $H$ as above, $d\tilde q/dt'=\tilde p/m$ and $d\tilde p/dt'=-m\omega^2\tilde q$, whose second-order form is $d^2\tilde q/d{t'}^2=-\omega^2\tilde q$. The flow is a rotation of the $(\tilde q,\tilde p)$ plane at frequency $\omega$, and after a quarter period the configuration has become the momentum divided by $m\omega$, and the momentum has become minus $m\omega$ times the configuration. In the biquaternion picture this exchange is the action of the complex structure, as the next section states.

### The Routhian: the Partial Legendre Transform

The Legendre transform need not be applied to all the coordinates at once. When a Lagrangian has $s$ **cyclic** coordinates $q=(q_1,\dots,q_s)$ — coordinates of which $\mathrm{Lag}$ is independent, so that their conjugate momenta are conserved — the transform can be applied to those alone, leaving the remaining coordinates $\varkappa_{\mathrm{crd}}=(\varkappa_{\mathrm{crd},1},\dots,\varkappa_{\mathrm{crd},n-s})$ in Lagrangian form. The result is the **Routhian**

$$
R(q,p,\varkappa_{\mathrm{crd}},d\varkappa_{\mathrm{crd}}/dt')=\mathrm{Sc}\!\left(p^{\natural}\,dq/dt'\right)-\mathrm{Lag} ,
$$

in which the $s$ transformed coordinates obey Hamilton's equations and the $n-s$ others obey Lagrange's, with $R$ itself and not $-R$ in the place of the Lagrangian. The Routhian has the form of a Hamiltonian and the role of a Lagrangian: the remaining coordinates satisfy the same Lagrange equations as a system of $n-s$ degrees of freedom whose potential is shifted by the momenta that were removed. A central potential shows the mechanism. The angle $\theta$ is cyclic, its momentum $p_\theta=\ell$ is conserved, and the Routhian is a function of $r$ alone, whose Lagrange equation is

$$
md^2r/d{r'_{t}}^2=-dV/dr(r)+\frac{\ell^2}{mr^3},
$$

the centrifugal term appearing as a consequence of the transform rather than as an inserted fictitious force. The partition is arbitrary — nothing requires the transformed coordinates to be the cyclic ones, and choosing them so is a convenience. This article applies the transform to the whole configuration, which is the case $s=n$; the partial case is recorded because it is the general form, and because it shows that which variable is eliminated is a choice of description and not of physics. The other classical reformulation worth naming is **Appell's**, whose equations of motion are written in the **generalized accelerations** $\alpha_r=d^2q_{r}/d{r'_{t}}^2$ rather than in the generalized velocities, with the generalized forces of D'Alembert's principle.

## Phase Space as a Single Biquaternion

For a system with three degrees of freedom the position and momentum are pure real quaternions, $\tilde q,\tilde p\in\mathbb{B}_{H}\cap\mathbb{B}_{\Phi}$, and they combine into the single biquaternion

$$
\boxed{\;\tilde Q_3=\tilde q+i\tilde p\in\mathbb{B}\;}.
$$

Its anti-Hermitian and Hermitian parts are

$$
\tilde Q_{3-}=\tfrac{1}{2}\!\left(\tilde Q_3-\tilde Q_3^{*}\right)=\tilde q\in\mathbb{B}_{\Phi},\qquad
\tilde Q_{3+}=\tfrac{1}{2}\!\left(\tilde Q_3+\tilde Q_3^{*}\right)=i\tilde p\in\mathbb{B}_{\Psi},
$$

as follows from $\tilde q^{*}=-\tilde q$ and $(i\tilde p)^{*}=i\tilde p$ for pure real $\tilde q,\tilde p$. The phase-space coordinate is thus a general biquaternion; its **material part is the configuration** and its **informational part is $i$ times the momentum**. The two sectors of the algebra separate position from conjugate momentum, and the decomposition $\mathbb{B}=\mathbb{B}_{\Phi}\oplus\mathbb{B}_{\Psi}$ is the algebraic form of the split of the phase space into configuration and momentum.

The algebra's **complex structure** is the map $\tilde Q_3\mapsto i\tilde Q_3$. Since $i\,\mathbb{B}_{\Psi}=\mathbb{B}_{\Phi}$, it exchanges the two parts; explicitly,

$$
i\tilde Q_3=i\tilde q-\tilde p .
$$

Multiplication by $i$ therefore turns the configuration into (minus) the momentum and the momentum into the configuration, up to the sector assignment. This is why the oscillator's quarter-period evolution exchanges the two: the oscillator flow is a rotation in the plane spanned by $\tilde q$ and $\tilde p$, and the complex structure is that rotation by $\pi/2$. It is also the structural statement behind the observation, in the companion article *The Harmonic Oscillator in Biquaternionic Form*, that the oscillator's phase is generated by the sector-exchanging element $ie_t$.

The same assembly works for a system with four degrees of freedom, with $\tilde q,\tilde p$ general real quaternions, and the sector split then reads

$$
\tilde Q_{3+}=\tfrac{1}{2}\!\left(\tilde Q_3+\tilde Q_3^{*}\right)=q_t\,e_t+i\,\vec p ,\qquad
\tilde Q_{3-}=\tfrac{1}{2}\!\left(\tilde Q_3-\tilde Q_3^{*}\right)=i\,p_t\,e_t+\vec q ,
$$

so that the two vector parts separate as configuration and momentum while the two scalar components pair the other way: the configuration scalar $q_t$ is Hermitian and the momentum scalar $i\,p_t$ is anti-Hermitian. The clean statement — material part the configuration, informational part $i$ times the momentum — is the three-degree-of-freedom case $q_t=p_t=0$, which is also the one that carries the spatial interpretation.

## The Four-Hamiltonian and the Exactness of the Action Form

The phase-space biquaternion $\tilde Q_3=\tilde q+i\tilde p$ packages the **configuration** with the **momentum**. There is a second packaging, and it is the covariant one: the Hamiltonian with the canonical momentum in the same biquaternion. Gsponer and Hurni call it the **four-Hamiltonian**

$$
\Pi = \left[H(r'_t, r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z,\vec\pi)\,;\,-i\vec\pi(r'_t, r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)\right],
$$

a bireal — that is, Hermitian — biquaternion whose scalar part is the Hamiltonian and whose vector part carries the canonical momentum. For $n$ point particles in a time-independent external field it is assembled from the four-momenta and the potential,

$$
\Pi = \sum_n P_n + ϙ_n A(X_n), \qquad P_n = [E_n\,;\,-ic\vec p_n], \qquad A = [\xi_{\mathrm{scp}}\,;\,-i\vec A],
$$

in the source's notation, with $ϙ_n$ the charge of the $n$-th particle and $A$ the four-potential; the scalar part is the Hamiltonian $H=E+ϙ\xi_{\mathrm{scp}}$ and the vector part the canonical momentum $\vec\pi=\vec p-q\vec A$. Up to the central factor $-i$ — the corpus's placement of the time component in the scalar slot — the four-momenta here are the corpus's four-momentum $\tilde P_{\Phi}$, and the source's mass-shell statement $|P|^2=m^{2}c^{2}$ is the corpus's $\langle\tilde P_{\Phi}\rangle_{\natural}=-m^2c^2$.

The reason to introduce the object is the action. The source's **action postulate** is

$$
\tilde\nabla_\Phi S = i\Pi ,
$$

that is, the four-Hamiltonian derives from a single invariant scalar $S$, the action. In the corpus's vocabulary the content of the postulate is that $\Pi$ is, up to the central factor $-i$, a gradient: the components satisfy $\partial/\partial R_{\imath}\Pi_{\jmath}=\partial/\partial R_{\jmath}\Pi_{\imath}$, which is the statement that the one-form $\Pi$ is **closed** and therefore locally exact. The source writes the same condition as $\tilde\nabla_\Phi\wedge\Pi=0$, and reads it as $d\Pi$ being a total differential, equivalently

$$
\oint dX\circ\Pi = 0 ,
$$

which for two fixed endpoints is Hamilton's principle, $\delta\int_{X_1}^{X_2} dX\circ\Pi = 0$. Hamilton's principle is thus, in this formulation, the **exactness of the four-Hamiltonian one-form**; and for a Hamiltonian with no explicit time dependence the same condition is equivalent to Hamilton's equations $d(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)/dt'=d H/d\vec\pi$, $d\vec\pi/dt'=-d H/d(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)$.

**Two packagings, two sectors.** The contrast with the previous section is exact. The phase-space biquaternion $\tilde Q_3$ pairs a material part with an informational part; the four-Hamiltonian $\Pi$ lies **entirely** in the Hermitian (informational) sector, its two halves being the Hamiltonian and the momentum rather than a position and a momentum. The corpus has both objects: $\tilde Q_3$ for the configuration–momentum split and $\Pi$ for the covariant energy–momentum-plus-potential object whose potential is the action.

**The Hamilton–Jacobi rewriting.** With the four-Hamiltonian in hand the relativistic mass-shell identity converts the action postulate into the **relativistic Hamilton–Jacobi equation** for a charged particle in an electromagnetic field: the source's form sets the quaternion square of $i\tilde\nabla_\Phi S+ϙ\tilde A_{\Phi}$ equal to $m^2$, the sign of the $ϙ\tilde A_{\Phi}$ term following the charge-sign convention. The non-relativistic Hamilton–Jacobi equation and its biquaternion-norm interpretation are the subject of the companion article *The Non-Quantum Limit of the Free Schrödinger Equation*; the four-Hamiltonian is the covariant object beneath that equation, and the corpus records it here.

## The Poisson Bracket

### The Biquaternion Form

For central-valued observables $f(\tilde q,\tilde p)$, $g(\tilde q,\tilde p)$, the Poisson bracket is the scalar part of a quaternion expression. Define the gradients

$$
\nabla_{\tilde q}f=\sum_{\imath} e_{\imath}\frac{\partial f}{\partial q_{\imath}},\qquad
\nabla_{\tilde p}f=\sum_{\imath} e_{\imath}\frac{\partial f}{\partial p_{\imath}}.
$$

Using $\mathrm{Sc}(\tilde q_1^{\natural}\tilde q_2)=\sum_{\imath} q_{1\imath} q_{2\imath}$ for real quaternions, the bracket is

$$
\boxed{\;\{f,g\}=\mathrm{Sc}\!\left((\nabla_{\tilde q}f)^{\natural}\,\nabla_{\tilde p}g\right)
-\mathrm{Sc}\!\left((\nabla_{\tilde p}f)^{\natural}\,\nabla_{\tilde q}g\right)\;}.
$$

Only the scalar part of each quaternion product enters. For pure $\tilde q_1,\tilde q_2$ the product $\tilde q_1^{\natural}\tilde q_2$ has a vector part as well, $-\tilde q_1\times\tilde q_2$; in general the vector part is $q_{1,0}\vec q_2-q_{2,0}\vec q_1-\vec q_1\times\vec q_2$, and only the cross-product term is intrinsic to the pairing. The Poisson bracket discards it, and the discarded part is precisely the cross-product structure that reappears as the angular-momentum bracket below. This is the algebraic content of the statement that the classical bracket is the antisymmetric scalar pairing of two gradients.

Because the bracket is built from scalar parts of quaternion products, it is automatically bilinear and antisymmetric, and in these coordinates it is the canonical bracket in disguise, so it satisfies the Jacobi identity. The derivation property $\{f,gh\}=\{f,g\}h+g\{f,h\}$ holds for the commutative product of central-valued functions, exactly as in the standard theory.

### Canonical Brackets

For the coordinate and momentum functions $q_{\imath}$, $p_{\jmath}$ one has $\nabla_{\tilde q}q_{\imath}=e_{\imath}$, $\nabla_{\tilde q}p_{\jmath}=0$, and so

$$
\{q_{\imath},q_{\jmath}\}=0,\qquad \{p_{\imath},p_{\jmath}\}=0,\qquad \{q_{\imath},p_{\jmath}\}=\delta_{\imath\jmath}.
$$

These are the standard canonical brackets, written with the algebra's basis rather than with an index list. Hamilton's equations take the bracket form

$$
df/dt'=\{f,H\},
$$

which for $f=q_{\imath},p_{\jmath}$ reproduces $dq_{\imath}/dt'=\partial H/\partial p_{\imath}$, $dp_{\jmath}/dt'=-\partial H/\partial q_{\jmath}$.

### Canonical Transformations

A change of phase-space variables $(\tilde q,\tilde p)\to(\tilde Q,\tilde P_{\Phi})$ that preserves the form of Hamilton's equations is a **canonical transformation**, and the test is a statement about the bracket alone:

$$
\{Q_{\imath},Q_{\jmath}\}=0,\qquad \{P_{\imath},P_{\jmath}\}=0,\qquad \{Q_{\imath},P_{\jmath}\}=\delta_{\imath\jmath},
$$

evaluated with the original bracket. A transformation satisfying these is canonical; one that fails any of them is not. The criterion is worth recording for a reason specific to this article: it is **scalar**. It never asks what the discarded vector part of the quaternion product does. That is the sharpest support for the claim made below in *What the Bracket Is Not*: the classical structure of the theory, including which changes of variable are permitted, lives entirely in the scalar projection of the quaternion product, while the vector part carries the rotations. Such transformations have generating functions, and the freedom in the Hamiltonian noted in the Standard Formulation is of the same kind: the Hamiltonian is fixed only up to the partial time derivative of an arbitrary function of coordinates, momenta and time.

### Angular Momentum

For a particle, the product of position and momentum is

$$
\tilde q\,\tilde p=-\vec q\cdot\vec p+\vec L,\qquad \vec L=\vec q\times\vec p,
$$

for the pure-vector configuration $\tilde q,\tilde p$ that carries the spatial interpretation. The scalar part is (minus) the contraction of position and momentum, and the **vector part is the angular momentum** $\vec L$. This is the biquaternion form of the cross-product formula $\vec L=\vec r\times\vec p$. Its components satisfy, as in the companion article *Similitudes Between Biquaternion Rotors and Hamiltonian Flow*,

$$
\{L_{\mathrm{orb},i},L_{\mathrm{orb},j}\}=\varepsilon_{\imath\jmath\ell}L_{\mathrm{orb},k},\qquad \{L_{\mathrm{orb},i},q_j\}=\varepsilon_{\imath\jmath\ell}q_{\imath},\qquad \{L_{\mathrm{orb},i},p_j\}=\varepsilon_{\imath\jmath\ell}p_{\imath} .
$$

The first of these is the statement that the components of angular momentum close into $\mathrm{SU}(2)$ under the Poisson bracket; it is the bracket that the biquaternion algebra realizes **exactly**, because the quaternion product already carries the cross product, with no deformation parameter. The companion article *Similitudes Between Biquaternion Rotors and Hamiltonian Flow* identifies the corresponding one-parameter group: on the coadjoint orbit, the flow generated by $H=2G\cdot\vec S$ is the rotor conjugation by $\exp(r'_t\,G)$, and the generators agree term for term.

### What the Bracket Is Not

The bracket defined above is the classical Poisson bracket of a commutative algebra of central-valued functions. It is not a commutator, and it does not require or imply one. The companion article *Similitudes Between the Poisson Bracket and the Quantum Commutator* shows that the two brackets are not isomorphic, and that the canonical algebra of a Heisenberg pair cannot be realized inside the finite-dimensional algebra $\mathbb{B}$; the companion article *The Harmonic Oscillator in Biquaternionic Form* confirms the obstruction in the oscillator setting. Nothing in the present article uses that obstruction, because the classical formulation needs no commutator; the bracket is the scalar pairing of gradients, and the algebra supplies it directly.

## The Action, Symmetries, and Conservation

The action of the biquaternion formulation is

$$
S[\tilde q]=\int \mathrm{Lag}(\tilde q,d\tilde q/dt',r'_t)\,dt' ,
$$

a central-valued functional of a real-quaternion path. Its stationarity gives the Euler–Lagrange equation derived above; the next article develops the action principle and the stationary-phase statement of the classical limit.

The symmetries that the algebra makes visible are the following.

**Time translation.** If $\mathrm{Lag}$ has no explicit time dependence, Noether's theorem gives the conserved energy $E=\mathrm{Sc}(\tilde p^{\natural}d\tilde q/dt')-\mathrm{Lag}=H$.

**Configuration-space rotations.** A rotation of the configuration acts by the **rotor conjugation**

$$
\tilde q\longmapsto \tilde u\,\tilde q\,\tilde u^{*},\qquad \tilde u\in\mathbb{B}_{H},\quad \tilde u\tilde u^{\natural}=e_t .
$$

The biquaternion norm is invariant, $\langle\tilde u\tilde q\tilde u^{*}\rangle_{\natural}=\langle\tilde q\rangle_{\natural}$, because the rotor has unit norm. If the potential is rotationally invariant, so is the Lagrangian, and the conserved Noether charge is the angular momentum $\vec L=\vec q\times\vec p$ of the previous section. This is the classical mechanics reading of the rotor: the rotation group is the group of unit real quaternions $SU(2)$, acting on the configuration by conjugation. The companion article *Similitudes Between Biquaternion Rotors and Hamiltonian Flow* develops the rotor-flow correspondence, and the companion article *Noether's Theorem in Biquaternionic Form* develops the general current construction.

**The central phase.** Because $i$ is central, a central phase acts on the biquaternion-valued configuration by $\tilde q\mapsto \exp(i\theta_{\mathrm{cen}})\tilde q$. For a real-quaternion configuration it does not preserve the real subspace — $\exp(i\theta_{\mathrm{cen}})\tilde q$ is a complex biquaternion unless $\tilde q=0$ — so it is a symmetry of the complexified formulation rather than of the real configuration space; it becomes a genuine internal symmetry only for a complex biquaternion-valued field, where it is the $\mathrm{U}(1)$ of the companion article *The Gauge Principle in Biquaternionic Form*. It also acts on the free Lagrangian, $\mathrm{Lag}=\tfrac12m\langle d\tilde q/dt'\rangle_{\natural}\mapsto \exp(2i\theta_{\mathrm{cen}})\mathrm{Lag}$, so a real Lagrangian is invariant only for $\exp(2i\theta_{\mathrm{cen}})=1$: the transformation is a symmetry of the complexified formulation and not of the real one. In the present classical setting it acts on the phase-space biquaternion $\tilde Q_3$ and is the algebra's complex structure; its consequences for the action and for the symplectic structure are developed in the companion articles *The Lagrangian and the Non-Quantum Limit: The Action Principle* and *The Symplectic Form and the Biquaternion Norm Cone*.

## What the Formulation Does and Does Not Give

The transcription is exact within its domain, and the domain is worth stating plainly.

**What it gives.** For a system whose configuration is a real quaternion — a particle in three dimensions with an optional scalar degree of freedom — the Lagrangian and Hamiltonian formalism is written without index clutter: the kinetic energy is the biquaternion norm, the momentum is its Legendre conjugate, the Hamiltonian of a free particle is the biquaternion norm of the momentum, the Euler–Lagrange and Hamilton equations are single quaternion equations, and the Poisson bracket is the scalar pairing of two quaternion gradients. The phase-space coordinate is one biquaternion whose sectors are the configuration and the momentum. The rotational bracket is exact, with the quaternion product's cross product supplying the structure constants.

**What it does not give.** The algebra is finite dimensional; it cannot carry the configuration space of a system with more than a few degrees of freedom, nor an infinite-dimensional field configuration except through its coefficients. The Poisson bracket is a scalar projection of a quaternion product, and the vector part it discards is not a second bracket. And the canonical Heisenberg sector is absent: there is no pair $\tilde q,\tilde p$ inside $\mathbb{B}$ whose commutator is a nonzero central constant, as the companion articles *Similitudes Between the Poisson Bracket and the Quantum Commutator* and *The Harmonic Oscillator in Biquaternionic Form* prove. None of these limitations is a defect of the transcription; they are properties of the algebra, and they mark where the biquaternion language is a convenience and where it is a constraint.

**The field case.** The one direction in which the finite-dimensional transcription is extended rather than limited is the field, and it is the subject of the companion article *Hamiltonian Field Theory in Biquaternionic Form*. There the single conjugate momentum becomes a conjugate momentum field, the Legendre transform acts on a density, the bracket becomes a bracket on functionals with $\{\xi_{\mathrm{scp}}(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z),\pi(\vec y)\}=\delta^3(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z-\vec y)$, the Hamiltonian becomes the integral of a density whose Hermitian-form expression is the energy density, and the conservation law becomes the continuity equation for the energy flux, whose density and flux are the scalar and vector parts of one Hermitian biquaternion. The central scalar field is the case in which the algebra's contribution is the packaging and the sector interpretation rather than a change of the bracket, and it is the case that the article on canonical quantization takes over unchanged.

**The tools are established; the rest of the article is the principle they serve.** The variation, the second variation, the geodesic principle, the stationary-phase statement of the classical limit and the Hamilton–Jacobi equation follow, in that order.

## The Action and Its First Variation

### The Configuration-Space Action

For a real-quaternion configuration $\tilde q(r'_t)$ of a system with Lagrangian $\mathrm{Lag}(\tilde q,d\tilde q/dt',r'_t)$, where $t'=r'_t/c$ is the time in seconds, the action is the central-valued functional

$$
S[\tilde q]=\int_{t'_1}^{t'_2}\mathrm{Lag}(\tilde q,d\tilde q/dt',r'_t)\,dt' .
$$

Because $\mathrm{Lag}$ takes values in the centre $\mathbb{B}_{C}=\mathrm{span}_{\mathbb{R}}\{e_t,ie_t\}$, the value of $S$ is a complex scalar and its phase is well defined. This is not automatic for a non-central Lagrangian, and it is the first reason the biquaternion formulation is convenient for the stationary-phase statement: the exponent is a scalar. Write the phase as one angle and one weight,

$$\exp\!\left(\frac{2\pi i\,S}{h}\right)=\exp\!\left(i\theta_{\mathrm{act}}\right)\exp\!\left(-\kappa_{\mathrm{act}}\right),\qquad \theta_{\mathrm{act}}=\frac{2\pi \mathrm{Re}\,S}{h},\qquad \kappa_{\mathrm{act}}=-\frac{2\pi \mathrm{Im}\,S}{h}.$$

Both symbols are real. $\theta_{\mathrm{act}}$ is the classical phase: it is the real part of the action over $\frac{h}{2\pi}$, and it is the only factor that oscillates. $\kappa_{\mathrm{act}}$ is a weight: a positive imaginary part of the action damps the trajectory, and the damped trajectories do not contribute to the stationary-phase limit. For a real Lagrangian the second factor is one, the action is real, $\kappa_{\mathrm{act}}=0$, and the weight is a pure phase. The split matters for a complex Lagrangian, and it is the reason the centre is named here: a complex scalar action is the general case, and the phase alone would hide the decay.

### The Domain of the Principle: Discrete and Continuous

The statement is written for a finite list of coordinates, and this article uses it that way throughout. Nothing in it requires a finite list. A deformable body, or a field, has infinitely many degrees of freedom: its state is a function of position and time rather than a finite tuple $q(r'_t)$, and the Lagrangian is replaced by a **density** $\mathcal{L}$, the action becoming $S=\int\mathcal{L}\,d^3r\,dt'$. The stationarity statement is unchanged, and its Euler–Lagrange equations are field equations rather than ordinary differential equations. In the biquaternion formulation the configuration is then an algebra-valued field $\tilde q(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z,r'_t)$ and the action a spacetime integral of a central-valued density, which is the form the companion articles *The Relativistic Particle and the Lagrangian: The Stationary-Action Principle* and *Stress–Energy, Conservation Laws and the Field Action in Biquaternionic Form* use.

For a string of density $\rho$ and tension $\mathcal{T}$ with displacement $u(r_x,r'_t)$, the action is
$$
S=\tfrac12\iint\left[\rho\left(\partial u/\partial r'_t\right)^2-\mathcal{T}\left(\partial u/\partial r_x\right)^2\right]dx\,dr'_t,\qquad c^2=\mathcal{T}/\rho ,
$$

the residual of the Euler–Lagrange operator vanishes to $2\times10^{-10}$ on a solution of the wave equation $\partial^2 u/\partial {r'_{t}}^2=c^2\,\partial^2 u/\partial r_x^2$, and is $-1.67$ on a neighbouring function: stationarity selects exactly the field equation. The Hamiltonian side of the same field action — the conjugate momentum field, the Hamiltonian density as the energy density, the bracket on functionals and the continuity equation for the energy flux — is developed in the companion article *Hamiltonian Field Theory in Biquaternionic Form*, which extends the Legendre transform, the bracket and the conservation law of the preceding article from a finite list of coordinates to a density.

The statement is also independent of the coordinates in which it is written, which is what allows the coordinates to be generalized away altogether. Newton's law is recovered from a variational statement, in coordinates in which it is not obvious; the form of the statement, not the coordinates, is what carries the physics.

### When the Loads Are Not Conservative

The principle as written assumes the applied forces derive from a potential, and that assumption can fail. When the external loads are **non-conservative** — a damping force is the standard example — the variation of the action does not vanish on the physical motion, and the principle must be **extended** by adding the virtual work of those loads; it reduces to the plain form when the loads do derive from a potential. The added term is not idle: it is what makes the variation vanish on the damped motion rather than on the undamped one.

It is worth being precise about what is lost, because the natural summary — a non-conservative force is the gradient of nothing, so no Lagrangian contains it — is too strong. What is true is that no *potential* contains it, so no Lagrangian of the form $T-V$ does. A Lagrangian may still exist, at a price: the damped linear oscillator has the explicitly time-dependent

$$
L_t=\exp(\gamma r'_t/c)\left(\tfrac12\left(dq/dt'\right)^{2}-\tfrac12\omega_0^2q^2\right),
$$

whose Euler–Lagrange equation is $d^2q/d{t'}^2+\gamma\,dq/dt'+\omega_0^2q=0$, with $t'=r'_t/c$; the residual of its left-hand side vanishes to $1.3\times10^{-9}$ along the analytic damped solution. The price is that $L_t$ is neither $T-V$ nor invariant under time translation, so the quantity it would call the energy is not conserved. The plain framework can be made to hold, but it stops being one in which energy means what it meant.

**Herglotz's principle** is the systematic alternative, and it changes what the action *is* rather than adding a term to it. The action is defined not by the integral $\int \mathrm{Lag}\,dt'$ but as the solution of the differential equation

$$
\left(dS/dt'\right)(r'_t)=\mathrm{Lag}(r'_t,\tilde q,d\tilde q/dt',S),\qquad S(r'_{t,0})=S_0 ,
$$

so that the Lagrangian may depend on the action, and the requirement is that this $S$ be stationary. The stationarity condition is the **Euler–Lagrange–Herglotz equation**

$$
\frac{d}{dt'}\frac{\partial \mathrm{Lag}}{\partial\left(d\tilde q/dt'\right)}-\frac{\partial \mathrm{Lag}}{\partial\tilde q}
=\frac{\partial \mathrm{Lag}}{\partial S}\,\frac{\partial \mathrm{Lag}}{\partial\left(d\tilde q/dt'\right)},
$$

whose right-hand side carries the dissipation and which returns the Euler–Lagrange equation of this article when $\partial \mathrm{Lag}/\partial S=0$. The damped oscillator is the standard illustration: with

$$
\mathrm{Lag}=\tfrac12\left(dq/dt'\right)^{2}-\tfrac12\omega_0^2q^2-\gamma S,\qquad \,dS/dt'=\mathrm{Lag} ,
$$

the equation of motion is $d^2q/d{t'}^2+\gamma\,dq/dt'+\omega_0^2q=0$, with $t'=r'_t/c$, matching the analytic damped solution to $1.7\times10^{-14}$, while the same $\mathrm{Lag}$ evaluated on the *undamped* motion leaves a residual of $0.30$. The $S$-dependence is what produces the damping, and the check separates the two motions rather than confirming both.

**What replaces the energy.** Dissipation does not remove the conservation law; it weights it. For a time-translation symmetry the conserved quantity acquires the exponential of $\int\partial \mathrm{Lag}/\partial S$,

$$
\exp(\gamma r'_t/c)\left(\mathrm{Lag}-dq/dt'\,\frac{\partial \mathrm{Lag}}{\partial\left(dq/dt'\right)}\right)
=-\exp(\gamma r'_t/c)\left(\tfrac12\left(dq/dt'\right)^{2}+\tfrac12\omega_0^2q^2+\gamma S\right),
$$

which for the damped oscillator is conserved to $3.0\times10^{-14}$ while the plain energy $\tfrac12\left(dq/dt'\right)^{2}+\tfrac12\omega_0^2q^2$ decays from $0.500$ to $0.075$. In Hamiltonian form the same structure is a **contact** Hamiltonian system on the extended space $(\tilde q,\tilde p,S)$. The momentum and Hamiltonian are the usual Legendre data, $p_i=\partial \mathrm{Lag}/\partial\left(dq_{i}/dt'\right)$ and $H=\sum_ip_i\,dq_{i}/dt'-\mathrm{Lag}$, and the equations

$$
dq_{i}/dt'=\frac{\partial H}{\partial p_i},\qquad
\,dp_{i}/dt'=-\left(\frac{\partial H}{\partial q_i}+p_i\frac{\partial H}{\partial S}\right),\qquad
\,dS/dt'=\sum_ip_i\frac{\partial H}{\partial p_i}-H
$$

reduce to Hamilton's equations when $\partial H/\partial S=0$; for the damped oscillator $H=\tfrac12p^2+\tfrac12\omega_0^2q^2+\gamma S$ reproduces the damped motion to $1.3\times10^{-11}$. Since $\mathrm{Lag}$ is central-valued, so is $S$, and the extended space is the configuration and momentum biquaternions with one central coordinate adjoined: the algebra accommodates the construction without enlargement. The class covered is wider than damping — $d^2q/d{t'}^2+f(q)\left(dq/dt'\right)^{2}+g(r'_t)dq/dt'+h(q)=0$ is the Euler–Lagrange–Herglotz equation of $\mathrm{Lag}=\tfrac12\left(dq/dt'\right)^{2}-[2f(q)dq/dt'+g(r'_t)]S-U(q)$ for the $U$ solving $dU/dq+2fU=h$, verified to $1.3\times10^{-15}$, with the Lane–Emden equation among its special cases. Herglotz's principle is the variational formulation of the non-conservative equations, not a workaround for them.

### The First Variation and the Boundary Term

The first variation of $S$, with the quaternion gradient of §*Conventions*, is

$$
\delta S=\int_{t'_1}^{t'_2}\mathrm{Sc}\!\left[\left(\partial \mathrm{Lag}/\partial\tilde q-\frac{d}{dt'}\partial \mathrm{Lag}/\partial\left(d\tilde q/dt'\right)\right)^{\natural}\,\delta\tilde q\right]dr'_t
+\left[\mathrm{Sc}\!\left((\partial \mathrm{Lag}/\partial\left(d\tilde q/dt'\right))^{\natural}\,\delta\tilde q\right)\right]_{t'_1}^{t'_2}.
$$

The bulk term vanishes for an arbitrary variation if and only if the **Euler–Lagrange equation** holds,

$$
\boxed{\;\frac{d}{dt'}\frac{\partial \mathrm{Lag}}{\partial\left(d\tilde q/dt'\right)}-\frac{\partial \mathrm{Lag}}{\partial\tilde q}=0\;},
$$

which are the four real equations of §*The Standard Formulation*. The boundary term is the part that does not vanish when the endpoints are free. Writing $\tilde p=\partial \mathrm{Lag}/\partial\left(d\tilde q/dt'\right)$, it is

$$
\delta S_{\text{bdry}}=\left[\mathrm{Sc}\!\left(\tilde p^{\natural}\,\delta\tilde q\right)\right]_{t'_1}^{t'_2},
$$

with $\delta\tilde q$ a **virtual** variation at fixed time. A second statement is often conflated with this one, and the two are different. On shell the action is a function of the two endpoint phase-space points, and the change of that function when the endpoints are moved is the differential $d\tilde q$, not the virtual variation:

$$
dS=\mathrm{Sc}(\tilde p^{\natural}_2\,d\tilde q_2)-\mathrm{Sc}(\tilde p^{\natural}_1\,d\tilde q_1).
$$

The two expressions take the same numerical value, because the virtual variation of a free endpoint may be chosen equal to its displacement, but they are not the same object: $\delta\tilde q$ varies the path while the endpoint data are held fixed, and $d\tilde q$ moves the endpoint data. The quantity $\varpi=\mathrm{Sc}(\tilde p^{\natural}\,d\tilde q)$ is the **symplectic potential** in biquaternion form. The identity $dS=\varpi_2-\varpi_1$ says that the on-shell action is a **generating function** of the canonical transformation between the initial and final phase-space points. The exterior derivative of this potential is the symplectic form up to the standard sign convention of the symplectic potential — explicitly, $d\varpi=d\mathrm{Sc}(\tilde p^{\natural}\,d\tilde q)=d\vec p\wedge d\vec q=-\omega$ for the canonical form $\omega=\sum_{\imath\in\{x,y,z\}} dq_{\imath}\wedge dp_{\imath}$ — and the symplectic form, with its conventions fixed, is the subject of the next article; here it is enough to record that the boundary term of the action variation already contains it.

### The Phase-Space Action

The same statement in phase-space variables uses the action

$$
S_{\mathrm{ps}}[\tilde q,\tilde p]=\int_{t'_1}^{t'_2}\left[\mathrm{Sc}\!\left(\tilde p^{\natural}\,d\tilde q/dt'\right)-H(\tilde q,\tilde p)\right]dr'_t .
$$

Varying $\tilde q$ and $\tilde p$ independently and integrating by parts,

$$
\delta S_{\mathrm{ps}}=\int\mathrm{Sc}\!\left[\left(d\tilde q/dt'-\partial H/\partial\tilde p\right)^{\natural}\,\delta\tilde p\right]dr'_t
+\int\mathrm{Sc}\!\left[\left(-d\tilde p/dt'-\partial H/\partial\tilde q\right)^{\natural}\,\delta\tilde q\right]dr'_t
+\left[\mathrm{Sc}(\tilde p^{\natural}\,\delta\tilde q)\right]_{t'_1}^{t'_2}.
$$

Stationarity for arbitrary $\delta\tilde q,\delta\tilde p$ gives **Hamilton's equations**

$$
d\tilde q/dt'=\frac{\partial H}{\partial\tilde p},\qquad
\,d\tilde p/dt'=-\frac{\partial H}{\partial\tilde q},
$$

which are the critical-point equations of $S_{\mathrm{ps}}$. The boundary term is again the symplectic potential. The two actions $S[\tilde q]$ and $S_{\mathrm{ps}}[\tilde q,\tilde p]$ have the same extremals after elimination of $\tilde p$, which is the Legendre transform of the preceding article read as a statement about critical points.

### Symmetries and the Boundary Term

The boundary term alone yields the conserved quantities, and it is worth isolating because the mechanism is the same one that the companion article *Noether's Theorem in Biquaternionic Form* develops in full. Suppose a one-parameter transformation $\tilde q\mapsto\tilde q_\epsilon$ leaves the action invariant up to a total derivative,

$$
S[\tilde q_\epsilon]-S[\tilde q]=\epsilon\int\frac{d}{dt'}\Lambda\,dt' ,
$$

and suppose the unperturbed path is a classical path, so that the bulk term of the variation vanishes. Then the variation reduces to the boundary term,

$$
\epsilon\int\frac{d}{dt'}\Lambda\,dt'=\delta S_{\text{bdry}}
=\left[\mathrm{Sc}\!\left(\tilde p^{\natural}\,\delta\tilde q\right)\right]_{t'_1}^{t'_2},
\qquad \delta\tilde q=\epsilon\,Q ,
$$

so $\mathrm{Sc}(\tilde p^{\natural}\,Q)-\Lambda$ is the same at $t'_1$ and $t'_2$:

$$
\frac{d}{dt'}\left[\mathrm{Sc}\!\left(\tilde p^{\natural}\,Q\right)-\Lambda\right]=0 .
$$

The conserved charge is read off the boundary term. For time translation, $Q=d\tilde q/dt'$ and $\Lambda=\mathrm{Lag}$, giving the energy $H=\mathrm{Sc}(\tilde p^{\natural}d\tilde q/dt')-\mathrm{Lag}$. For a configuration-space rotation with generator $\vec G$, $Q=[\vec G,\tilde q]$ and $\Lambda=0$, giving

$$
\mathrm{Sc}\!\left(\tilde p^{\natural}\,[\vec G,\tilde q]\right)=2\,\mathrm{Sc}\!\left(\vec G^{\natural}\,\tilde q\,\tilde p\right)=2\,\vec G\cdot\vec L ,
$$

twice the component of the angular momentum $\vec L=\vec q\times\vec p$ along $\vec G$, for the pure-vector configuration on which the cross product and the angular momentum are defined; the factor $2$ is the same one that appears in the commutator, $[\vec G,\tilde q]=2\,\vec G\times\tilde q$. The construction is the biquaternion form of the standard Noether argument, and its content is that the boundary term of the action variation is the conservation law.

## The Second Variation and Stability

The first variation identifies the classical path; the second variation decides whether it is a minimum, a maximum, or a saddle, and it controls the fluctuation factor in the stationary-phase evaluation.

Write the classical path as $\tilde q_c$ and a nearby path as $\tilde q_c+\delta\tilde q$, with $\delta\tilde q$ vanishing at the endpoints. Expanding the action to second order,

$$
S[\tilde q_c+\delta\tilde q]=S[\tilde q_c]+\tfrac{1}{2}\delta^2S[\tilde q_c,\delta\tilde q]+O(\delta^3),
$$

where

$$
\delta^2S=\int\left\langle\delta\tilde q,\;\mathcal{J}\,\delta\tilde q\right\rangle dr'_t ,
$$

and $\mathcal{J}$ is the **Jacobi operator** of the problem. For a Lagrangian quadratic in the velocities, $\mathrm{Lag}=\tfrac12 m \langle\,d\tilde q/dt'\rangle_{\natural}-V(\tilde q)$, the Jacobi operator is

$$
\mathcal{J}\delta\tilde q=-m\,d^2(\delta\tilde q)/d{r'_{t}}^2-\frac{d^2V}{d\tilde q^2}(\tilde q)\,\delta\tilde q ,
$$

and the vanishing of the second variation on a nontrivial field, $\mathcal{J}\,\zeta=0$, is the **Jacobi equation** for the deviation field $\zeta(r'_t)$,

$$
m\,d^2\zeta/d{r'_{t}}^2+\frac{d^2V}{d\tilde q^2}(\tilde q_c)\,\zeta=0 .
$$

This is the equation of **geodesic deviation** for the biquaternion-norm kinetic term. A point $r'_{t,2}$ at which a nontrivial solution with $\zeta(r'_{t,1})=0$ also satisfies $\zeta(r'_{t,2})=0$ is a **conjugate point**; conjugate points are where the second variation degenerates and where the classical path ceases to be a strict minimum. For the free particle, $\frac{d^2V}{d\tilde q^2}=0$ and the Jacobi equation reduces to $d^2\zeta/d{r'_{t}}^2=0$, whose solutions are linear in $r'_t$; a linear solution vanishing at both ends of an interval of nonzero length is identically zero, so the free path has no conjugate points.

**Stability.** The sign of the second variation is the classical stability statement: positive for a stable extremum, a change of sign at a conjugate point. Nothing here is quantum; the second variation is the Hessian of a function on a function space, and its degeneracy is the classical Morse-theoretic datum.

## The Action as a Geodesic Principle

### The Biquaternion-Norm Metric

The kinetic term of the Lagrangian is the biquaternion norm, and the corresponding free action,

$$
S_0[\tilde q]=\frac{m}{2}\int \langle\,d\tilde q/dt'\rangle_{\natural}\,dt' ,
$$

is the energy of a curve in the positive-definite metric that the biquaternion norm defines on $\mathbb{B}_{H}$. Its extremals are the straight lines $d^2\tilde q/d{r'_{t}}^2=0$ of §*The Poisson Bracket*, and the geodesic equation of the biquaternion-norm metric is the same equation. The length functional $\int\sqrt{\langle d\tilde q\rangle_{\natural}}$ has the same extremals as the energy functional at fixed duration, by the standard argument: extremising the energy at fixed duration selects the geodesics parametrised proportionally to arc length, which are exactly the extremals of the length.

The geodesic interpretation has a Hamiltonian form, and it is the same statement. On the cotangent bundle the biquaternion-norm metric induces the Hamiltonian

$$
H(\tilde q,\tilde p)=\frac{1}{2\,m}\sum_{\imath}  p_{\imath} p_{\imath}=\frac{\langle\tilde p\rangle_{\natural} c}{2\,m\,c},
$$

Here $\nu_m=\frac{mc}{h}$ is the mass wave number, the inverse of the mass length.

the two forms agreeing because the biquaternion-norm metric is Euclidean in the basis $e_{\imath}$, so that the inverse metric is the metric itself. Hamilton's equations for it are $d\tilde q/dt'=\partial H/\partial\tilde p=\tilde p/m$ and $d\tilde p/dt'=0$, whose solutions are the straight lines found above: the geodesic flow of the biquaternion norm **is** a Hamiltonian flow, its Hamiltonian is the Legendre transform of the free action, and $H=\langle\tilde p\rangle_{\natural}/2m$ is conserved along it. This is the flat case of the general statement that a geodesic flow is the Hamiltonian flow of the quadratic form built from the inverse metric. It is the abelian counterpart of the correspondence the companion article *Similitudes Between Biquaternion Rotors and Hamiltonian Flow* establishes on the coadjoint orbit: the free particle is the case in which the carrier is abelian and the metric flat.

The biquaternion norm is positive definite on $\mathbb{B}_{H}$, so its metric is Riemannian and there are no null directions. The **biquaternion-norm cone** $\langle\tilde{Q}\rangle_{\natural}=0$ is trivial on the real-quaternion sector; it becomes nontrivial on the material sector $\mathbb{B}_{\Phi}$ of the complexified algebra, where the four-vector $\tilde R_\Phi=i r'_t\,e_t+r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z$ has the indefinite norm $\langle\tilde R_\Phi\rangle_{\natural}=-{r'_{t}}^2+r_x^2+r_y^2+r_z^2$, whose zero set is the light cone. The two statements are consistent: the indefinite norm appears when the central coordinate is imaginary, $q_t=i r'_t$, which is exactly the passage from a real quaternion to a material-sector four-vector. The cone and its role in the symplectic geometry are the subject of the next article.

### The Rotor Action

The genuinely noncommutative case is a rotor-valued configuration. Let $\tilde u(r'_t)$ be a path in the group of unit real quaternions, $\langle\tilde u\rangle_{\natural}=e_t$, and take the free action

$$
S_{\mathrm{rot}}[\tilde u]=\frac{\digamma_{\mathrm{inr}}}{2}\int \mathrm{Sc}\!\left(d\tilde u/dt'\,(d\tilde u/dt')^{\natural}\right)dr'_t
=\frac{\digamma_{\mathrm{inr}}}{2}\int \langle\,d\tilde u/dt'\rangle_{\natural}\,dt' ,
$$

the rotational kinetic energy of a body with a single principal moment $\digamma_{\mathrm{inr}}$. Varying $\tilde u$ subject to the constraint $\langle\tilde u\rangle_{\natural}=e_t$ means varying within the group; writing $\delta\tilde u=\tilde u\,\delta\vec\theta$ with $\delta\vec\theta$ a pure real quaternion vanishing at the endpoints (the constraint $\mathrm{Sc}(\tilde u^{\natural}\delta\tilde u)=0$ forces $\delta\vec\theta$ to have zero scalar part), the first variation of the action becomes

$$
\delta S_{\mathrm{rot}}=\digamma_{\mathrm{inr}}\int\mathrm{Sc}\!\left(d\tilde u/dt'\,(\delta\,d\tilde u/dt')^{\natural}\right)dr'_t
=-\digamma_{\mathrm{inr}}\int\mathrm{Sc}\!\left(d^2\tilde u/d{r'_{t}}^2\,(\delta\tilde u)^{\natural}\right)dr'_t
=\digamma_{\mathrm{inr}}\int\mathrm{Sc}\!\left(\tilde u^{\natural}\,d^2\tilde u/d{r'_{t}}^2\;\delta\vec\theta\right)dr'_t ,
$$

using $\delta\tilde u=\tilde u\,\delta\vec\theta$, $(\delta\tilde u)^{\natural}=-\delta\vec\theta\,\tilde u^{\natural}$, and the cyclicity of the scalar part. Stationarity for all pure $\delta\vec\theta$ gives

$$
\mathrm{Ve}\!\left(\tilde u^{\natural}\,d^2\tilde u/d{r'_{t}}^2\right)=0 ,
$$

the **geodesic equation on the group**. Writing $\\vec\\varsigma_{\mathrm{acc}}=\tilde u^{\natural}d\tilde u/dt'$, a real pure quaternion by the constraint — its scalar part is $\tfrac{1}{2}\tfrac{d}{dt'}\langle\tilde u\rangle_{\natural} = \langle\tilde u,\tilde u\rangle_{\natural}=0$ — one has $\tilde u^{\natural}d^2\tilde u/d{r'_{t}}^2=d\\vec\\varsigma_{\mathrm{acc}}/dt'+\\vec\\varsigma_{\mathrm{acc}}^2$ with $\\vec\\varsigma_{\mathrm{acc}}^2$ a real scalar; the equation therefore says that the vector part of $d\\vec\\varsigma_{\mathrm{acc}}/dt'$ vanishes, and since $\\vec\\varsigma_{\mathrm{acc}}$ is pure real for all $r'_t$ this is $d\\vec\\varsigma_{\mathrm{acc}}/dt'=0$. Equivalently, the equation with the constraint is $\frac{d}{dt'}(\tilde u^{\natural}d\tilde u/dt')=0$: the **body angular velocity is constant**. Its solutions are the one-parameter subgroups, and the **classical rotor path is**

$$
\boxed{\;\tilde u(r'_t)=\tilde u(0)\,\exp\!\left(+\tfrac{1}{2}\vec\omega_b r'_t/c\right),\qquad \vec\omega_b\in\mathbb{B}_{H}\cap\mathbb{B}_{\Phi}\;},
$$

with $\vec\omega_b$ constant in the body frame. This is the free rigid body's motion, and it is derived here purely from the stationarity of the rotor action. The same calculation with the body-frame angular velocity replaced by the space-frame one gives the equivalent form $\tilde u(r'_t)=\exp(+\tfrac12\vec\omega_s r'_t/c)\tilde u(0)$. The rigid-body article takes this result as its starting point and adds the inertia and the torque.

The rotor action is the second reason the biquaternion formulation is useful for the action principle: it is a functional on a noncommutative group, its extremals are the geodesics, and the algebra computes them in closed form.

## The Classical Limit as Stationary Phase

### The Stationary-Phase Lemma

The purely analytic statement is the following. Let $S(x)$ be a real smooth function with a single nondegenerate critical point $x_0$, $dS/dx(x_0)=0$, $d^2S/dx^2(x_0)\neq0$, and let $g$ be smooth. Then as $h\to0^+$,

$$
\boxed{\;\int  g(x)\,\exp\!\left(i\frac{2\pi S(x)}{h}\right)dx
\;\sim\;
g(x_0)\,\sqrt{\frac{2\,\pi\,h}{2\pi \left|\frac{d^2S}{dx^2}(x_0)\right|}}\;
\exp\!\left(i\frac{2\pi S(x_0)}{h}\right)\;
\exp(i\theta_{\mathrm{msl}})\;}.
$$

The phase at the critical point is $S(x_0)\frac{2\pi}{h}$, which is $\theta_{\mathrm{act}}$ of the first section when the action is real; the prefactor is the Gaussian fluctuation determinant about the critical point; the last factor is the Maslov phase of the critical point, $\theta_{\mathrm{msl}}=\frac{\pi}{4}\operatorname{sgn}(d^2S/dx^2)(x_0)$, real because the sign is $\pm1$ and $\pi/4$ is a real number. Points away from $x_0$ contribute to lower order because their phases oscillate rapidly and cancel. This is the **stationary-phase lemma**, and it contains no physics.

The path-integral version applies the same lemma to a sum over trajectories weighted by $\exp(iS[\tilde q]\frac{2\pi}{h})$. The critical points of the action are the solutions of $\delta S=0$, that is, the classical paths, and the leading asymptotic is a sum over them,

$$
\boxed{\;\int\mathcal{D}\tilde q\;\exp\!\left(i\frac{2\pi S[\tilde q]}{h}\right)
\;\sim\;
\sum_{\tilde q_c}\exp\!\left(i\frac{2\pi S[\tilde q_c]}{h}\right)A[\tilde q_c]\;\bigl(1+O(\frac{h}{2\pi})\bigr)\;},
$$

where $A[\tilde q_c]$ is the square root of the inverse fluctuation determinant (the van Vleck factor) and a Maslov phase. The classical content of the statement is exactly this: **the set of critical points of the action is the set of classical trajectories.** The identification of the critical-point equations with the Euler–Lagrange equations was made in the first section, and in the phase-space form with Hamilton's equations in the second.

### Why This Is Not Quantisation

The construction above is a statement about an oscillatory integral. It can be paraphrased without any quantum vocabulary:

- The exponent $S[\tilde q]\frac{2\pi}{h}$ is a phase, and the phase is stationary where $\delta S=0$; every other trajectory's phase varies rapidly and cancels in the sum.
- Therefore the classical trajectory, defined as the solution of $\delta S=0$, is the trajectory that survives the cancellation, and the classical theory is the critical-point theory of the sum.
- The parameter $\frac{h}{2\pi}$ sets the scale of the phase; the classical limit is the limit of large phase.

Nothing in the paraphrase requires a Hilbert space, a state, or an operator. The formulation is real and classical throughout; the configuration is a real quaternion; the action is a central-valued functional. The oscillatory sum is a device for stating the classical limit, and the biquaternion formulation is a classical formulation. Quantisation — the reverse construction, in which an operator algebra is built from the classical brackets — belongs to the sibling category and is not used here.

### The Fluctuation Factor and the Classical Hessian

The prefactor $A[\tilde q_c]$ of the stationary-phase evaluation is built from the second variation of the previous section. In the biquaternion setting the fluctuation operator is the Jacobi operator $\mathcal{J}$, and the prefactor is the inverse square root of its regularized determinant, taken relative to the free reference and with $\frac{h}{2\pi}$ restored; that combination is the biquaternion form of the van Vleck factor. The zeros of the determinant are the conjugate points; the Maslov phase jumps there. This is the classical Morse theory of the action, expressed with the biquaternion-norm kinetic term.

For the free particle the calculation is explicit. The Jacobi operator is $\mathcal{J}=-m\,d^2/d{r'_{t}}^2$ with Dirichlet boundary conditions on the interval $[0,T]$. Its eigenfunctions are $\sin(n\pi r'_t/T)$ with eigenvalues $\eta_n=m n^2\pi^2/T^2$, $n=1,2,\dots$, and the zeta-regularized determinant is computed from the spectral zeta function

$$
\zeta_{\mathcal J}(s)=\sum_{n\ge1}\eta_n^{-s}
=m^{-s}\left(\frac{T}{\pi}\right)^{2s}\zeta(2s),
\qquad
\det\mathcal{J}=\exp\!\left(-\left.\frac{d\zeta_{\mathcal J}}{ds}\right|_{s=0}\right).
$$

Using $\zeta(0)=-\tfrac12$ and $\left.\frac{d\zeta}{ds}\right|_{s=0}=-\tfrac12\ln 2\pi$,

$$
\left.\frac{d\zeta_{\mathcal J}}{ds}\right|_{s=0}=\left(-\ln m+2\ln\frac{T}{\pi}\right)\zeta(0)+2\left.\frac{d\zeta}{ds}\right|_{s=0}
=\tfrac12\ln\frac{m}{m_0}-\ln\frac{2T}{T_0},
\qquad
\frac{\det\mathcal{J}(T)}{\det\mathcal{J}(T_0)}=\frac{T}{T_0}\;\propto\;T ,
$$

per real component, with $m_0=1\ \mathrm{kg}$ and $T_0$ the reference length: the determinant is quoted against that reference because the regularised determinant carries a dimension and only the ratio is a number. The determinant is therefore **linear** in $T$, and the fluctuation factor — its inverse square root — falls as the inverse square root of $T$ per real component. That is the standard free-particle van Vleck factor: the free propagator's prefactor in one dimension is $\sqrt{m\,c\big/\big(2\,\pi\,i\,\frac{h}{2\pi}\,T\big)}$, a reciprocal length that falls as the inverse square root of $T$ (the $c$ belongs there because $T$ is a length and not a time; without it the radicand is not a squared reciprocal length). The free path has no conjugate points, and there is no Maslov phase. The computation is the standard one; the biquaternion formulation contributes the observation that the second variation is the Hessian of the biquaternion norm, so the classical stability problem and the biquaternion-norm geometry are the same problem.

### Rotor Paths and the Geometric Phase of the Sum

The rotor action of the preceding section adds a feature that a scalar configuration cannot show. Its critical points are the one-parameter subgroups $\tilde u(r'_t)=\tilde u(0)\exp(+\tfrac12\vec\omega_br'_t/c)$, and about each of them the fluctuation operator is again built from the biquaternion norm. $SU(2)$ is the unit sphere $S^3$, compact and simply connected, with $\pi_1(S^3)=0$; the fundamental group $\mathbb{Z}_2$ belongs to the quotient $SO(3)=S^3/\{\pm e_t\}$, and the distinction matters here. Two statements follow, and they must be kept apart. First, the critical paths joining a given pair of endpoints are not unique. The geodesics of a bi-invariant metric on a group are its one-parameter subgroups, so a geodesic from $\tilde u_1$ to $\tilde u_2$ is a solution of $\exp(X)=\tilde u_1^{-1}\tilde u_2$; the solution is unique while the geodesic distance is below $\pi$, and at distance $\pi$ a whole two-sphere of directions qualifies, so the stationary-phase sum runs over a family. Second, a closed loop of rotations lifts to two rotor paths, one closed and one ending at $-e_t$, so the rotor path remembers a sign that the rotation path forgets. That sign, and not a homotopy class of $S^3$, is the source of the double-valuedness. The transport of a rotor along a path is a parallel transport for a connection on the group, and the failure of the transport to be path-independent is its **holonomy**: the extra group element picked up around a closed loop. That holonomy, and the Hannay angle that an adiabatic classical system accumulates because of it, is the subject of the companion article *Hannay's Angles and the Classical Geometric Phase in Biquaternionic Form*; it is a classical geometric phase, and the rotor action is the classical object whose stationary-phase sum carries it.

## The Hamilton–Jacobi Equation and the Classical Phase

The action of a classical trajectory, regarded as a function of its endpoint, is Hamilton's **principal function** $W(\tilde q,r'_t)$. Differentiating the relation $dW=\mathrm{Sc}(\tilde p^{\natural}\,d\tilde q)-E\,dt'$ with the definition $\tilde p=\partial W/\partial\tilde q$ gives the **Hamilton–Jacobi equation**

$$
\frac{\partial W}{\partial r'_t}+H\!\left(\tilde q,\frac{\partial W}{\partial\tilde q}\right)=0 .
$$

In the coordinates of the algebra,

$$
\frac{\partial W}{\partial\tilde q}=\sum_{\imath} e_{\imath}\frac{\partial W}{\partial q_{\imath}},
$$

so the Hamilton–Jacobi equation is a single scalar equation for the central-valued function $W$.

The Hamilton–Jacobi equation is the **eikonal equation** for the phase of the stationary-phase construction: writing the phase as $\frac{2\pi W}{h}$, the leading-order equation of the oscillatory integral is exactly $\partial/\partial r'_t\,W+H(\tilde q,\partial W/\partial\tilde q)=0$. In the classical interpretation, $W$ is a generating function of a canonical transformation; the constant surfaces $W=\text{const}$ are the wavefronts of the classical phase, and the characteristic directions of the Hamilton–Jacobi equation are the classical trajectories. Where the characteristic flow has a caustic, the stationary points of the action coalesce, and the stationary-phase prefactor changes.

The **characteristic function** $\mathcal{W}(\tilde q)$ of a time-independent problem satisfies $H(\tilde q,\partial\mathcal{W}/\partial\tilde q)=E$. For the free particle, $H=\langle\tilde p\rangle_{\natural}/2m$ and the equation is $\langle\partial\mathcal{W}/\partial\tilde q\rangle_{\natural}=2mE$, whose solution is $\mathcal{W}=\mathrm{Sc}(\tilde p^{\natural}\tilde q)$ with $\langle\tilde p\rangle_{\natural}=2mE$; the surfaces $\mathcal{W}=\text{const}$ are planes and the characteristics are straight lines, in agreement with the free-particle geodesics. For a periodic system the action variables $I_{\imath}=\oint p_{\imath}\,dq_{\imath}$ are the periods of the characteristic function, and they are the adiabatic invariants of the companion article *Hannay's Angles and the Classical Geometric Phase in Biquaternionic Form*.

## Summary

The Lagrangian and Hamiltonian formulations, and the action principle they serve, take the following form in the biquaternion algebra.

- The configuration is a real quaternion $\tilde q\in\mathbb{B}_{H}$, with the physical three-space as its pure-vector part; the kinetic energy is the biquaternion norm, $T=\tfrac{1}{2}m\langle d\tilde q/dt'\rangle_{\natural}$.
- The action $S[\tilde q]=\int \mathrm{Lag}\,dt'$ is stationary at the physical path, and stationarity gives the single quaternion Euler–Lagrange equation $\frac{d}{dt'}\partial \mathrm{Lag}/\partial\left(d\tilde q/dt'\right)-\partial \mathrm{Lag}/\partial\tilde q=0$, equivalent to the four real equations.
- The conjugate momentum is $\tilde p=\partial \mathrm{Lag}/\partial\left(d\tilde q/dt'\right)$, and the Hamiltonian is the Legendre transform $H=\mathrm{Sc}(\tilde p^{\natural}d\tilde q/dt')-\mathrm{Lag}$. For a free particle $H=\langle\tilde p\rangle_{\natural}/2m$: the free Hamiltonian is the biquaternion norm of the momentum.
- Hamilton's equations are $d\tilde q/dt'=\partial H/\partial\tilde p$, $d\tilde p/dt'=-\partial H/\partial\tilde q$.
- Position and momentum combine into the phase-space biquaternion $\tilde Q_3=\tilde q+i\tilde p$, whose anti-Hermitian part is the configuration and whose Hermitian part is $i$ times the momentum. The algebra's complex structure $i$ exchanges the two parts.
- The Poisson bracket is $\{f,g\}=\mathrm{Sc}((\nabla_{\tilde q}f)^{\natural}\nabla_{\tilde p}g)-\mathrm{Sc}((\nabla_{\tilde p}f)^{\natural}\nabla_{\tilde q}g)$, the scalar part of a quaternion expression; the discarded vector part is the cross product that makes the angular-momentum bracket $\{L_{\mathrm{orb},i},L_{\mathrm{orb},j}\}=\varepsilon_{\imath\jmath\ell}L_{\mathrm{orb},k}$ exact.
- Rotational symmetry acts by rotor conjugation $\tilde q\mapsto\tilde u\tilde q\tilde u^{*}$, and its Noether charge is $\vec L=\vec q\times\vec p$.
- The Lagrangian is determined only up to a total time derivative: $\mathrm{Lag}$ and $\mathrm{Lag}+dF(q,r'_t)/dt'$ have the same equations of motion, and their actions differ by the endpoint term $F(t'_2)-F(t'_1)$, which a variation with fixed endpoints cannot see. This is the same boundary freedom that appears as the symplectic potential in the variation of the action.
- The Legendre transform may be applied to a subset of the coordinates. The partial transform is the **Routhian**, which puts the transformed coordinates — conventionally the cyclic ones, whose momenta are conserved — in Hamiltonian form and the rest in Lagrangian form; for a central potential it produces the centrifugal term as a transformed potential.
- In the Hamiltonian description coordinates, velocities and momenta are **mutually independent** variables; the relation $\tilde p=\partial \mathrm{Lag}/\partial\left(d\tilde q/dt'\right)$ is used only to eliminate the velocity. This is what makes the transform a change of variables and $\tilde Q_3=\tilde q+i\tilde p$ a coordinate.
- $H=T+V$ is not automatic. It requires $T$ homogeneous of degree two in the velocities, which $T=\tfrac12m\langle d\tilde q/dt'\rangle_{\natural}$ satisfies by construction; with $\mathrm{Lag}$ time-independent, $H$ is then the conserved energy. Explicit time dependence is preserved by the transform, $\partial H/\partial r'_t=-\partial \mathrm{Lag}/\partial r'_t$.
- A change of phase-space variables is **canonical** exactly when it preserves the brackets $\{Q_{\imath},P_{\jmath}\}=\delta_{\imath\jmath}$. The criterion is scalar, so the permitted changes of variable live in the scalar projection of the quaternion product alone.

The formulation is a transcription, exact for configurations that fit in a real quaternion. It introduces no commutator and no $\frac{h}{2\pi}$; the canonical Heisenberg structure is absent from the finite-dimensional algebra, and the classical bracket that the algebra does carry is the scalar part of a quaternion product.

The principle itself adds the following.

- The action $S[\tilde q]=\int \mathrm{Lag}\,dt'$ is central-valued for a real-quaternion configuration, so its phase is unambiguous.
- The principle is not restricted to finitely many coordinates: for a continuum the Lagrangian becomes a density and the Euler–Lagrange equations become field equations.
- A non-conservative load cannot enter a potential, so no $T-V$ Lagrangian contains it and the plain form fails. The principle is then extended by virtual work, or replaced by **Herglotz's principle**, whose action solves $dS/dt'=\mathrm{Lag}$ and whose Euler–Lagrange–Herglotz equation carries the dissipative term; the energy is replaced by a weighted conserved quantity, and the Hamiltonian form becomes a contact system on $(\tilde q,\tilde p,S)$.
- The geodesic flow of the biquaternion-norm metric is a Hamiltonian flow, with Hamiltonian $H=\langle\tilde p\rangle_{\natural}/2m$. The free particle is the abelian case of the correspondence that the rotor articles exhibit on the coadjoint orbit.
- Its first variation is the sum of a bulk term and a boundary term. The bulk term vanishes for all variations exactly when the quaternion Euler–Lagrange equation $\frac{d}{dt'}\partial \mathrm{Lag}/\partial\left(d\tilde q/dt'\right)-\partial \mathrm{Lag}/\partial\tilde q=0$ holds. The boundary term is the symplectic potential $\varpi=\mathrm{Sc}(\tilde p^{\natural}\,d\tilde q)$, and on shell $dS=\varpi_2-\varpi_1$: the action generates the canonical transformation between its endpoints.
- The phase-space action $\int[\mathrm{Sc}(\tilde p^{\natural}d\tilde q/dt')-H]dr'_t$ has Hamilton's equations as its critical-point equations.
- The second variation defines the Jacobi operator $\mathcal{J}\delta\tilde q=-m\,\delta\,d^2\tilde q/d{r'_{t}}^2-\frac{d^2V}{d\tilde q^2}\,\delta\tilde q$ and the geodesic-deviation equation $md^2\zeta/d{r'_{t}}^2+\frac{d^2V}{d\tilde q^2}\,\zeta=0$; conjugate points are where the classical extremum ceases to be a strict minimum.
- The free rotor action $\frac{\digamma_{\mathrm{inr}}}{2}\int \langle\,d\tilde u/dt'\rangle_{\natural}dr'_t$ on the group of unit quaternions has the geodesic equation $\mathrm{Ve}(d^2\tilde u/d{r'_{t}}^2\tilde u^{\natural})=0$, whose solutions are the one-parameter subgroups $\tilde u(r'_t)=\tilde u(0)\exp(+\tfrac12\vec\omega_br'_t/c)$: the free rigid body's motion.
- The stationary-phase lemma evaluates an oscillatory sum over trajectories as a sum over the critical points of the action, weighted by $\exp(i\theta_{\mathrm{act}})$ and the fluctuation factor. The classical content is the identification of the critical points with the classical paths; the statement is a theorem about an integral and is not a quantisation.
- The action as a function of its endpoint is Hamilton's principal function, and its eikonal equation is the Hamilton–Jacobi equation $\partial/\partial r'_t\,W+H(\tilde q,\partial W/\partial\tilde q)=0$.

The biquaternion algebra supplies a central-valued action, so the phase is well defined; a biquaternion-norm kinetic term, so the free dynamics is geodesic motion; and a rotor action on a noncommutative group, whose extremals are computed in closed form.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_{\imath}^2=-e_t$ |
| $i$ | Central scalar imaginary, $i^2=-1$ |
| $\mathbb{B}_{\Phi},\mathbb{B}_{\Psi}$ | Anti-Hermitian (material) and Hermitian (informational) sectors |
| $\mathbb{B}_{H}$ | Real-quaternion subspace |
| $\tilde q=q_te_t+\vec q$ | Configuration quaternion (real) |
| $d\tilde q/dt'$ | Configuration velocity |
| $\langle\tilde q\rangle_{\natural} = \langle\tilde q,\tilde q\rangle_{\natural}=\tilde q\tilde q^{\natural}$ | Biquaternion norm |
| $\mathrm{Lag}(\tilde q,d\tilde q/dt',r'_t)$ | Lagrangian |
| $F(\tilde q,r'_t)$, $\mathrm{Lag}_2=\mathrm{Lag}+dF/dt'$ | Arbitrary function and the total-derivative ambiguity of the Lagrangian |
| $S[\tilde q]=\int \mathrm{Lag}\,dt'$ | Action; ambiguous by the endpoint term $F(t'_2)-F(t'_1)$ |
| $R=\mathrm{Sc}(p^{\natural}\,dq/dt')-\mathrm{Lag}$ (over the transformed block) | Routhian: the partial Legendre transform, shown in the general case, of which this article uses $s=n$ |
| $T(\digamma_{\mathrm{scl}}\,d\tilde q/dt')=\digamma_{\mathrm{scl}}^2T(d\tilde q/dt')$ | Homogeneity of the kinetic energy; gives $\mathrm{Sc}(\tilde p^{\natural}d\tilde q/dt')=2T$ and $H=T+V$ |
| $\partial H/\partial r'_t=-\partial \mathrm{Lag}/\partial r'_t$ | Explicit time dependence is preserved with reversed sign |
| $\{Q_{\imath},P_{\jmath}\}=\delta_{\imath\jmath}$ | Canonical-transformation criterion (scalar) |
| $\partial \mathrm{Lag}/\partial\tilde q=\sum_{\imath} e_{\imath}\partial \mathrm{Lag}/\partial q_{\imath}$ | Quaternion gradient of a central-valued function |
| $\tilde p=\partial \mathrm{Lag}/\partial\left(d\tilde q/dt'\right)$ | Conjugate momentum (real quaternion) |
| $H=\mathrm{Sc}(\tilde p^{\natural}d\tilde q/dt')-\mathrm{Lag}$ | Hamiltonian (Legendre transform) |
| $\tilde Q_3=\tilde q+i\tilde p$ | Phase-space biquaternion |
| $\nabla_{\tilde q}f,\nabla_{\tilde p}f$ | Gradients of an observable |
| $\{f,g\}$ | Poisson bracket |
| $\vec L=\vec q\times\vec p$ | Angular momentum |
| $\tilde u\in\mathbb{B}_{H}$, $\langle\tilde u\rangle_{\natural}=e_t$ | Rotation rotor |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}$ | the general plain sesquilinear form, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2^{*})$; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{*}=\sum_{\imath}\lvert Q_{2\imath}\rvert^{2}$ |
| $S[\tilde q]=\int \mathrm{Lag}\,dt'$ | Action (central-valued); in Herglotz's form it solves $dS/dt'=\mathrm{Lag}$ and is state-dependent |
| $\omega_0$, $\gamma$ | Oscillator frequency and damping coefficient |
| $\mathcal{L}$, $u$, $\rho$, $\mathcal{T}$ | Lagrangian density; string displacement, density and tension of the continuum example |
| $\tilde p=\partial \mathrm{Lag}/\partial\left(d\tilde q/dt'\right)$ | Conjugate momentum |
| $\varpi=\mathrm{Sc}(\tilde p^{\natural}\,d\tilde q)$ | Symplectic potential (boundary term) |
| $S_{\mathrm{ps}}=\int[\mathrm{Sc}(\tilde p^{\natural}d\tilde q/dt')-H]dr'_t$ | Phase-space action |
| $\delta^2S$ | Second variation |
| $\mathcal{J}$ | Jacobi (fluctuation) operator |
| $\zeta$ | Deviation field; $\mathcal{J}\zeta=0$ is the Jacobi/geodesic-deviation equation |
| $\tilde u\in\mathbb{B}_{H}$, $\langle\tilde u\rangle_{\natural}=e_t$ | Rotor configuration |
| $\vec\omega_b,\vec\omega_s$ | Body- and space-frame angular velocities |
| $W(\tilde q,r'_t)$ | Hamilton's principal function |
| $\frac{h}{2\pi}$ | Phase scale of the oscillatory integral; asymptotic parameter only |
| $A[\tilde q_c]$ | Fluctuation (van Vleck) prefactor |

## Further Reading

- H. Goldstein, C. P. Poole, and J. L. Safko, *Classical Mechanics* (Addison-Wesley, 2002), for the standard Lagrangian and Hamiltonian formulation, the Legendre transform, and the Poisson bracket.
- L. D. Landau and E. M. Lifshitz, *Mechanics* (Pergamon, 1976), for the action principle, Noether's theorem, and canonical equations.
- V. I. Arnold, *Mathematical Methods of Classical Mechanics* (Springer, 1989), for the symplectic and Poisson-geometric formulation of Hamiltonian mechanics.
- W. R. Hamilton, *Lectures on Quaternions* (Hodges and Smith, 1853), for the quaternion algebra and the quaternion product.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for quaternions, rotors, and their relation to the Lorentz group.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric-algebra treatment of rotors, rigid bodies, and mechanics.
- David Hestenes, *New Foundations for Classical Mechanics* (Reidel, 1986), for a treatment of classical mechanics in a real Clifford algebra closely related to the quaternion one.
- [Hamiltonian Field Theory in Biquaternionic Form](hamiltonian-field-theory-in-biquaternionic-form.html), companion article, for the extension of the Legendre transform, the bracket and the conservation law to a field, where the conjugate momentum is a field and the density and flux are one Hermitian biquaternion.
- A. Gsponer and J.-P. Hurni, "The physical heritage of Sir W. R. Hamilton," arXiv:math-ph/0201058, §5, for the four-Hamiltonian $\Pi=[H;-i\vec\pi]$, the action postulate $\tilde\nabla_\Phi S=i\Pi$, and the interpretation of Hamilton's principle as the exactness of the one-form $dX\circ\Pi$.
- W. R. Hamilton, *Elements of Quaternions*, Vol. II, art. 419 (2nd ed., enlarged by C. J. Joly, 1899–1901), for the quaternion resolution of the Kepler problem and the conservation of the angular-momentum and Runge–Lenz vectors.
- W. R. Hamilton, "On a General Method in Dynamics," *Philosophical Transactions of the Royal Society*, Part II (1834) 247–308 and Part I (1835) 95–144, for the original statement of the principle.
- G. Herglotz, *Berührungstransformationen* (Lectures, University of Göttingen, 1930), for the original state-dependent variational principle for non-conservative systems.
- R. B. Guenther, J. A. Gottsch, and C. M. Guenther, *The Herglotz Lectures on Contact Transformations and Hamiltonian Systems* (Juliusz Center for Nonlinear Studies, Toruń, 1996), for the contact-Hamiltonian form and the generalized Noether theorem.
- Lord Kelvin (W. Thomson), "On the waves produced by a single impulse in water of any depth," *Proceedings of the Royal Society of Edinburgh* **9** (1877) 253, for the method of stationary phase.
- N. G. van Kampen, "The method of stationary phase and the Stokes phenomenon," *Physica* **6** (1939) 513, for the asymptotic evaluation of oscillatory integrals.
- V. P. Maslov and M. V. Fedoriuk, *Semi-Classical Approximation in Quantum Mechanics* (Reidel, 1981), for the Maslov phase and the fluctuation determinant of the stationary-phase expansion.
- C. Morette, "On the definition and approximation of Feynman's path integrals," *Physical Review* **81** (1951) 848, for the van Vleck determinant and the fluctuation prefactor.
- Jerrold E. Marsden and Tudor S. Ratiu, *Introduction to Mechanics and Symmetry* (Springer, 1999), for geodesics on the rotation group, the Euler–Poincaré formulation, and rigid-body dynamics in the group setting.
