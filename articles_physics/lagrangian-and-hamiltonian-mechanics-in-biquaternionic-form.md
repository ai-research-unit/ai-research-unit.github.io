# __Lagrangian and Hamiltonian Mechanics in Biquaternionic Form__

## Introduction

Classical mechanics admits two great formulations. In the **Lagrangian** formulation a mechanical system is specified by a configuration space, a Lagrangian $L(q,dq/dt,t)$, and the variational principle $\delta S=0$, whose Euler–Lagrange equations are the equations of motion. In the **Hamiltonian** formulation the same system is specified by a phase space, a Hamiltonian $H(q,p,t)$ obtained from $L$ by the Legendre transform, and Hamilton's first-order equations; the observables then carry the Poisson bracket, and the dynamics is the Hamiltonian flow.

Both formulations are usually written in coordinates. This article writes them in the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ of the companion articles. The purpose is not to derive new mechanics. It is to exhibit which parts of the two formulations the algebra fixes, and to be explicit about the boundary beyond which it does not reach.

Three structural statements organise the article, and they are worth stating at the outset.

1. **The kinetic energy is the biquaternion norm.** For a configuration whose generalized coordinates are assembled into a real quaternion $\tilde q$, the kinetic energy of a free particle is $\tfrac{m}{2}\langle\,d\tilde q/dt\rangle_{\natural}=\tfrac{m}{2}d\tilde q/dt\,\overline{d\tilde q/dt}$, the biquaternion norm of the velocity. The biquaternion norm is the algebra's own quadratic form, and the free Lagrangian is a scalar multiple of it.
2. **The phase-space coordinate is one biquaternion.** The position and the momentum assemble into $\tilde Z=\tilde q+i\tilde p$, whose anti-Hermitian part is the position and whose Hermitian part is $i$ times the momentum. The algebra's two sectors thus separate a kinematic configuration from its conjugate momentum, and the algebra's complex structure is the phase-space complex structure.
3. **The boundary is finite-dimensional.** The algebra $\mathbb{B}\cong M_2(\mathbb{C})$ is eight-dimensional over $\mathbb{R}$. It carries the configuration of a system with at most four real degrees of freedom, and it carries the *rotational* bracket exactly; it does not carry the canonical Heisenberg structure, as the companion article *Similitudes Between the Poisson Bracket and the Quantum Commutator* establishes and as the companion article *The Harmonic Oscillator in Biquaternionic Form* confirms. This article is classical throughout: no commutator is introduced, and no canonical relation of the form $[\tilde q,\tilde p]=i\hbar$ is used or needed.

The conventions are those of the read list. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$; the quaternion basis is $e_t=1,\vec e_x,\vec e_y,\vec e_z$ with $\vec e_k^2=-e_t$ and $\vec e_\mu \vec e_\nu=-\delta_{\mu\nu}e_t+\varepsilon_{\mu\nu\lambda}\vec e_\lambda$; the scalar imaginary $i$ is central with $i^2=-1$. The anti-Hermitian subspace $\mathbb{M}_-$ (imaginary scalar, real vector) is the material sector, and the Hermitian subspace $\mathbb{M}_+$ (real scalar, imaginary vector) is the informational sector, with $\mathbb{B}=\mathbb{M}_-\oplus\mathbb{M}_+$. The real-quaternion subspace is $\mathbb{H}_{\mathbb{B}}$, and the trace is normalized by $\mathrm{Tr}(e_t)=2$. The symbol $c=1/\sqrt{\epsilon\mu}$ is the speed of light in the medium, and $c_0$ its vacuum value. Throughout, $\tilde q$ denotes a configuration quaternion, $\tilde p$ its conjugate momentum, and the scalar pairing of two real quaternions $\tilde q_1,\tilde q_2$ is $\mathrm{Sc}(\tilde q_1^{\natural}\,\tilde q_2)=\sum_\mu q_{1\mu} q_{2\mu}$.

The companion articles supply the pieces:
- Companion article *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*, for the material sector, the biquaternion norm, and the four-vectors.
- Companion article *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*, for the Hermitian sector, the trace formula, and the conjugation action.
- Companion article *Similitudes Between the Poisson Bracket and the Quantum Commutator*, for the classical bracket conventions and the boundary between the classical and quantum brackets.
- Companion article *Similitudes Between Biquaternion Rotors and Hamiltonian Flow*, for the rotor and the Hamiltonian flow on the coadjoint orbit.
- Companion article *The Harmonic Oscillator in Biquaternionic Form*, for the phase plane and the sector structure of a mode.

## The Standard Formulation

The standard Lagrangian and Hamiltonian formalism is recalled here in the form the biquaternion transcription will take; nothing in this section is new.

The formalism is not an independent postulate. It follows from **D'Alembert's principle of virtual work** — the infinitesimal virtual work done by the impressed forces across displacements consistent with the constraints vanishes, which is the statement that the constraint forces do no work. Eliminating those forces is what allows the constraints to be absorbed into the geometry of the coordinates: a system of $\mathcal N$ constituents in three dimensions with $\kappa$ independent constraints has $3\mathcal N-\kappa$ **degrees of freedom**, described by the same number of **generalized coordinates** $q_i$, one per degree of freedom. These are not curvilinear coordinates. The number of curvilinear coordinates is the dimension of the position space — three, for three-dimensional space — whereas the number of generalized coordinates is the number of degrees of freedom, which constraints reduce and additional constituents raise; the two counts need not agree. A constraint expressible as $\vec r=\vec r(q,t)$ holding for all $t$ is **holonomic**; it is **scleronomic** when the relation carries no explicit time and **rheonomic** when it does. The Lagrange equation obtained below is the generalized form of Newton's second law that results, and the stationary-action statement is its equivalent formulation in integral form.

Let a system have $n$ generalized coordinates $q=(q_x,\dots,q_n)$ and velocities $dq/dt$. The **Lagrangian** is a smooth real function $L(q,dq/dt,t)$, and the **action** is the functional

$$
S[q]=\int_{t_1}^{t_2}L(q,dq/dt,t)\,dt .
$$

The **principle of stationary action** states that the physical trajectory is a stationary point of $S$ among paths with fixed endpoints. For an arbitrary variation $\delta q(t)$ vanishing at the endpoints,

$$
\delta S=\int_{t_1}^{t_2}\left(\frac{\partial L}{\partial q_i}\,\delta q_i+\frac{\partial L}{\partial \left(dq_{i}/dt\right)}\,\delta\left(dq_{i}/dt\right)\right)dt
=\int_{t_1}^{t_2}\left(\frac{\partial L}{\partial q_i}-\frac{d}{dt}\frac{\partial L}{\partial \left(dq_{i}/dt\right)}\right)\delta q_i\,dt ,
$$

after an integration by parts. Stationarity for all $\delta q$ gives the **Euler–Lagrange equations**

$$
\frac{d}{dt}\frac{\partial L}{\partial \left(dq_{i}/dt\right)}-\frac{\partial L}{\partial q_i}=0 .
$$

The Lagrangian is **not unique**, and the extent of the ambiguity is a boundary term. For any smooth $F(q,t)$, the Lagrangians $L$ and

$$
L'=L+\frac{d}{dt}F(q,t)
$$

have the same Euler–Lagrange equations. The added term enters both terms of the Euler–Lagrange operator as the same expression, $d/dt(\partial F/\partial q_i)$: once as $\partial/\partial q_i\,(dF/dt)$, and once as $d/dt\big(\partial/\partial\left(dq_{i}/dt\right)\,(dF/dt)\big)=d/dt(\partial F/\partial q_i)$, since the mixed partials of $F$ commute. The two contributions cancel. The action is ambiguous in the corresponding way,

$$
S'=S+F\big(q(t_2),t_2\big)-F\big(q(t_1),t_1\big) ,
$$

the difference being an endpoint term, which a variation with fixed endpoints cannot see. What the formalism determines is therefore the **equations of motion**, not the Lagrangian, and the ambiguity is exactly a boundary term: the same structure the companion article *The Action Principle and the Classical Limit as Stationary Phase in Biquaternionic Form* meets from the other side, where the boundary term of $\delta S$ is the symplectic potential. The Hamiltonian carries the analogous freedom — a generating function of the coordinates, momenta and time shifts it by a partial time derivative — and that is the freedom a canonical transformation exploits.

The **conjugate momenta** are $p_i=\partial L/\partial \left(dq_{i}/dt\right)$. In the Hamiltonian description the coordinates, velocities and momenta are **mutually independent** variables: the relation $p_i=\partial L/\partial\left(dq_{i}/dt\right)$ is used once, to eliminate the velocities in favour of the momenta, and does not thereafter act as a constraint among the phase-space variables. So $H(q,p)$ is differentiated with respect to $p_i$ at fixed $q$, with $dq/dt$ already eliminated; holding $dq/dt$ fixed while varying $p_i$ would describe a different object. This is what makes the passage a change of variables rather than a definition, and it is why the phase-space element $\tilde Z=\tilde q+i\tilde p$ constructed below is a coordinate. When the Hessian matrix $\partial^2L/\partial\left(dq_{i}/dt\right)\partial\left(dq_{j}/dt\right)$ is non-singular, the map $(q,dq/dt)\mapsto(q,p)$ is invertible, and the **Legendre transform**

$$
H(q,p,t)=p_i\,dq_{i}/dt-L(q,dq/dt,t)
$$

defines the **Hamiltonian**. Its differential gives **Hamilton's equations**

$$
dq_{i}/dt=\frac{\partial H}{\partial p_i},\qquad
\,dp_{i}/dt=-\frac{\partial H}{\partial q_i}.
$$

For observables $f(q,p)$, $g(q,p)$, the **Poisson bracket** is

$$
\{f,g\}=\frac{\partial f}{\partial q_i}\frac{\partial g}{\partial p_i}-\frac{\partial f}{\partial p_i}\frac{\partial g}{\partial q_i},
$$

and the dynamics is $df/dt=\{f,H\}$. The bracket is bilinear, antisymmetric, and satisfies the Jacobi identity; it is a derivation of the commutative algebra of observables under pointwise multiplication.

### The Rayleigh Dissipation Function

Friction has no place in the mechanical Lagrangian. A force proportional to the velocity, such as a Stokes drag, is not the gradient of a potential $V(q,t)$, so it cannot be absorbed into $L=T-V$. The classical device that keeps the equations in Lagrangian form adds it instead as a **generalized force** on the right-hand side,

$$
\frac{d}{dt}\frac{\partial L}{\partial\left(dq_{i}/dt\right)}-\frac{\partial L}{\partial q_i}=-\frac{\partial F}{\partial\left(dq_{i}/dt\right)},
$$

with **Rayleigh's dissipation function** $F=\tfrac12b_{ij}dq^{i}/dt dq^{j}/dt$, the quadratic form whose gradient is the viscous force. For a single coordinate and the mechanical Lagrangian this is the damped oscillator $md^2q/dt^2+bdq/dt+V'(q)=0$. The energy $E=\sum_idq^{i}/dt\partial L/\partial\left(dq^{i}/dt\right)-L$ is no longer conserved; it decreases at the rate

$$
\frac{dE}{dt}=-\sum_idq^{i}/dt\frac{\partial F}{\partial\left(dq^{i}/dt\right)}=-2F,
$$

the last equality because $F$ is homogeneous of degree two in the velocities. The dissipation function is therefore half the rate at which the energy falls, and it vanishes only at rest.

What the device does not do is restore the symmetry of the formalism: the force is inserted by hand rather than derived from a Lagrangian, and the energy, the conserved quantity of the autonomous case, becomes a decreasing function. It is the classical face of the dichotomy drawn in the article *Quantum Channels and the Reversible/Irreversible Dichotomy*, where the evolution generated inside the algebra is reversible and the dissipative evolution is not.

## The Biquaternionic Configuration

### Coordinates and the Gradient

Assemble the generalized coordinates of a system with at most four degrees of freedom into a **real quaternion**

$$
\tilde q=q_t\,e_t+q_x\,\vec e_x+q_y\,\vec e_y+q_z\,\vec e_z\in\mathbb{H}_{\mathbb{B}} ,
$$

with real components $q_\mu$. The physical three-space is the pure real part $\vec q=q_x\vec e_x+q_y\vec e_y+q_z\vec e_z\in\mathbb{H}_{\mathbb{B}}\cap\mathbb{M}_-$, and the central coordinate $q_te_t\in\mathbb{C}_{\mathbb{B}}\cap\mathbb{H}_{\mathbb{B}}$ is a fourth, scalar degree of freedom. A system with three degrees of freedom is the special case $q_t=0$; the pure-vector configuration is the one that carries the spatial interpretation.

For a central-valued function $F(\tilde q)$ — a function taking values in $\mathbb{C}_{\mathbb{B}}$ — define the **quaternion gradient** componentwise,

$$
\partial F/\partial\tilde q=\sum_{\mu\in\{t,x,y,z\}}e_\mu\,\frac{\partial F}{\partial q_\mu}.
$$

Because $F$ is central, this gradient is unambiguous: the quaternion product does not enter the definition, and the left and right derivatives of a central-valued function of real quaternion variables agree. The pairing that makes it a derivative is the scalar pairing,

$$
dF=\mathrm{Sc}\!\left(\overline{\partial F/\partial\tilde q}\;d\tilde q\right)
=\sum_{\mu\in\{t,x,y,z\}}\frac{\partial F}{\partial q_\mu}\,dq_\mu ,
$$

which uses $\mathrm{Sc}(\bar e_\mu e_\nu)=\delta_{\mu\nu}$. This is the statement, in the algebra, that the natural scalar product on the real-quaternion subspace is the scalar part of a quaternion product.

### The Kinetic Energy Is the Biquaternion Norm

Let $\tilde q(t)$ be a trajectory and $d\tilde q/dt$ its velocity. The **kinetic energy** of a particle of mass $m$ is

$$
T=\tfrac{1}{2}m\,\langle\,d\tilde q/dt\rangle_{\natural}=\tfrac{1}{2}m\,d\tilde q/dt\,\overline{d\tilde q/dt}=\tfrac{1}{2}m\sum_{\mu\in\{t,x,y,z\}}\left(dq_{\mu}/dt\right)^{2} .
$$

For a pure-vector configuration the central term is absent and $T=\tfrac{1}{2}m|d\vec q/dt|^2$, the familiar kinetic energy. The kinetic energy is therefore the **biquaternion norm** of the velocity, and this is the first structural fact of the biquaternion formulation of mechanics: the algebra's own quadratic form is the free kinetic energy. The biquaternion norm on $\mathbb{H}_{\mathbb{B}}$ is positive definite, so $T\ge0$ with equality only for $d\tilde q/dt=0$; no sign choice has to be made.

The free Lagrangian is

$$
L_0=\tfrac{1}{2}m\,\langle\,d\tilde q/dt\rangle_{\natural},
$$

and a particle in a central potential $V(\tilde q)$ has

$$
L=\tfrac{1}{2}m\,\langle\,d\tilde q/dt\rangle_{\natural}-V(\tilde q).
$$

### The Euler–Lagrange Equations

Vary the action $S[\tilde q]=\int L\,dt$ with fixed endpoints. Using the scalar pairing, the first variation is

$$
\delta S=\int\left[\mathrm{Sc}\!\left(\overline{\partial L/\partial\tilde q}\;\delta\tilde q\right)+\mathrm{Sc}\!\left(\overline{\partial L/\partial\left(d\tilde q/dt\right)}\;\delta\,d\tilde q/dt\right)\right]dt ,
$$

and an integration by parts turns the second term into a total derivative plus

$$
\delta S=\int \mathrm{Sc}\!\left[\overline{\left(\partial L/\partial\tilde q-\frac{d}{dt}\partial L/\partial\left(d\tilde q/dt\right)\right)}\;\delta\tilde q\right]dt
+\left[\mathrm{Sc}\!\left(\overline{\partial L/\partial\left(d\tilde q/dt\right)}\;\delta\tilde q\right)\right]_{t_1}^{t_2}.
$$

The endpoint term vanishes because $\delta\tilde q(t_1)=\delta\tilde q(t_2)=0$. Since $\delta\tilde q$ is an arbitrary real quaternion at each time, stationarity of $S$ requires the bracket to vanish, and the **Euler–Lagrange equation** takes the quaternion form

$$
\boxed{\;\frac{d}{dt}\frac{\partial L}{\partial\left(d\tilde q/dt\right)}-\frac{\partial L}{\partial\tilde q}=0\;}
\qquad\text{with}\qquad
\frac{\partial L}{\partial\left(d\tilde q/dt\right)}=\sum_\mu e_\mu\frac{\partial L}{\partial\left(dq_{\mu}/dt\right)},\quad
\frac{\partial L}{\partial\tilde q}=\sum_\mu e_\mu\frac{\partial L}{\partial q_\mu}.
$$

This single quaternion equation is the four real Euler–Lagrange equations, one for each component $q_\mu$.

**Free particle.** For $L_0=\tfrac{1}{2}mN(d\tilde q/dt)$ the gradient is $\partial L_0/\partial\left(d\tilde q/dt\right)=m\,d\tilde q/dt$ and $\partial L_0/\partial\tilde q=0$, so the equation is $md^2\tilde q/dt^2=0$: straight-line motion at constant velocity, as it must be.

**Central potential.** For $L=\tfrac{1}{2}mN(d\tilde q/dt)-V(\tilde q)$, the equation is

$$
md^2\tilde q/dt^2=-\partial V/\partial\tilde q .
$$

When $V$ is a function of the real-quaternion modulus $\langle\tilde q\rangle_{\natural}$ alone, the right-hand side is $-\partial V/\partial\tilde q=-2V'(N)\tilde q$, a central force. The biquaternion equation is then the vector equation of a central-force problem; the specific force laws belong to the subcategory on effects without intrinsic magnetism, and are not developed here.

## The Legendre Transform

### Momentum and Hamiltonian

The **conjugate momentum** is the real quaternion

$$
\tilde p=\frac{\partial L}{\partial\left(d\tilde q/dt\right)}=\sum_\mu e_\mu p_\mu,\qquad p_\mu=\frac{\partial L}{\partial\left(dq_{\mu}/dt\right)}.
$$

For the free particle $\tilde p=m\,d\tilde q/dt$. The **Hamiltonian** is the Legendre transform

$$
H(\tilde q,\tilde p)=\mathrm{Sc}\!\left(\tilde p^{\natural}\,d\tilde q/dt\right)-L(\tilde q,d\tilde q/dt)
=\sum_\mu p_\mu\,dq_{\mu}/dt-L ,
$$

with $d\tilde q/dt$ eliminated in favour of $\tilde p$ using the inverse of $\tilde p=\partial L/\partial\left(d\tilde q/dt\right)$. The scalar pairing $\mathrm{Sc}(\tilde p^{\natural}d\tilde q/dt)=\sum_\mu p_\mu\,dq_{\mu}/dt$ is the quaternion form of the contraction $p_i\,dq_{i}/dt$; the conjugate is required, because $\mathrm{Sc}(\tilde pd\tilde q/dt)$ reverses the sign of the vector-part contribution.

**Free particle.** With $\tilde p=m\,d\tilde q/dt$ one has $\mathrm{Sc}(\tilde p^{\natural}d\tilde q/dt)=mN(d\tilde q/dt)=2T$, and

$$
H_0=\frac{\langle\tilde p\rangle_{\natural}}{2m}=\frac{\tilde p\,\tilde p^{\natural}}{2m}=\frac{1}{2m}\sum_{\mu\in\{t,x,y,z\}}p_\mu^2 ,
$$

the free Hamiltonian, which reduces to the familiar $\vec p^2/2m$ for a pure-vector momentum, $p_t=0$. The structural statement is the mirror of the one for $L_0$: **the free Hamiltonian is the biquaternion norm of the momentum, divided by $2m$.** The biquaternion norm thus appears at both ends of the Legendre transform, once on velocity and once on momentum, because the Legendre transform of a quadratic form is its own inverse up to the mass factor.

**Harmonic oscillator.** For $L=\tfrac{1}{2}mN(d\tilde q/dt)-\tfrac{1}{2}m\omega^2\langle\tilde q\rangle_{\natural}$ the momentum is again $\tilde p=m\,d\tilde q/dt$ and

$$
H=\frac{\langle\tilde p\rangle_{\natural}}{2m}+\frac{m\omega^2}{2}\langle\tilde q\rangle_{\natural}.
$$

The Hamiltonian is a sum of two biquaternion norms with positive coefficients, one in the momentum and one in the coordinate. Its level sets $H=E$ are ellipsoids in the eight-dimensional real phase space.

**When is the Hamiltonian the energy?** The identification of $H$ with $T+V$ is not automatic, and the condition is one this transcription satisfies by construction. If the kinetic energy is a **homogeneous function of degree two** in the generalized velocities, $T(\lambda\,dq/dt)=\lambda^2T(dq/dt)$, then Euler's theorem on homogeneous functions gives $dq_{\mu}/dt\partial T/\partial\left(dq_{\mu}/dt\right)=2T$. When the potential depends on the coordinates alone, $p_\mu=\partial T/\partial\left(dq_{\mu}/dt\right)$, and therefore

$$
\mathrm{Sc}\!\left(\tilde p^{\natural}\,d\tilde q/dt\right)=p_\mu\,dq_{\mu}/dt=2T,\qquad H=2T-(T-V)=T+V ,
$$

so $H$ is the total energy, and it is conserved when $L$ has no explicit time dependence. For the systems of this article the hypothesis is not an assumption but a property of the kinetic term: $T=\tfrac12 mN(d\tilde q/dt)$ is a quadratic form in the velocities and hence homogeneous of degree two. The condition can fail — a relativistic kinetic energy is not homogeneous of degree two — and where it fails $H$ remains the Legendre transform of $L$ but is no longer the energy.

Explicit time dependence, by contrast, is preserved by the transform. Differentiating $H=p_\mu\,dq_{\mu}/dt-L$ with respect to $t$ at fixed coordinates and momenta, the terms in $\partial\left(dq_{\mu}/dt\right)/\partial t$ cancel against $p_\mu=\partial L/\partial\left(dq_{\mu}/dt\right)$, leaving

$$
\frac{\partial H}{\partial t}=-\frac{\partial L}{\partial t}.
$$

So $L$ carries explicit time dependence exactly when $H$ does, with the sign reversed.

### Legendre Involution

The Legendre transform is an involution. Writing $H$ for the transform of $L$, the inverse relation is

$$
L=\mathrm{Sc}\!\left(\tilde p^{\natural}\,d\tilde q/dt\right)-H,\qquad
\,d\tilde q/dt=\frac{\partial H}{\partial\tilde p},
$$

provided the Hessian $\partial^2L/\partial\left(dq_{\mu}/dt\right)\partial\left(dq_{\nu}/dt\right)$ is non-singular, which for $L=\tfrac{1}{2}mN(d\tilde q/dt)-V$ it is: the Hessian is $m\delta_{\mu\nu}$.

### Hamilton's Equations

Differentiating $H(\tilde q,\tilde p)=\sum_\mu p_\mu\,dq_{\mu}/dt-L(\tilde q,d\tilde q/dt)$ and using the definition of $\tilde p$ gives **Hamilton's equations** in quaternion form,

$$
\boxed{\;d\tilde q/dt=\frac{\partial H}{\partial\tilde p},\qquad \,d\tilde p/dt=-\frac{\partial H}{\partial\tilde q}.\;}
$$

**Check on the free particle.** $H_0=\langle\tilde p\rangle_{\natural}/2m$ gives $\partial H_0/\partial\tilde p=\tilde p/m=d\tilde q/dt$ and $\partial H_0/\partial\tilde q=0$, hence $d\tilde p/dt=0$: constant momentum.

**Check on the oscillator.** With $H$ as above, $d\tilde q/dt=\tilde p/m$ and $d\tilde p/dt=-m\omega^2\tilde q$, whose second-order form is $d^2\tilde q/dt^2=-\omega^2\tilde q$. The flow is a rotation of the $(\tilde q,\tilde p)$ plane at frequency $\omega$, and after a quarter period the configuration has become the momentum and the momentum (up to sign) the configuration. In the biquaternion picture this exchange is the action of the complex structure, as the next section states.

### The Routhian: the Partial Legendre Transform

The Legendre transform need not be applied to all the coordinates at once. When a Lagrangian has $s$ **cyclic** coordinates $q=(q_x,\dots,q_s)$ — coordinates of which $L$ is independent, so that their conjugate momenta are conserved — the transform can be applied to those alone, leaving the remaining coordinates $\zeta=(\zeta_1,\dots,\zeta_{n-s})$ in Lagrangian form. The result is the **Routhian**

$$
R(q,p,\zeta,d\zeta/dt)=\mathrm{Sc}\!\left(\bar p\,dq/dt\right)-L ,
$$

in which the $s$ transformed coordinates obey Hamilton's equations and the $n-s$ others obey Lagrange's. The Routhian has the form of a Hamiltonian and the role of a Lagrangian: the remaining coordinates satisfy the same Lagrange equations as a system of $n-s$ degrees of freedom whose potential is shifted by the momenta that were removed. A central potential shows the mechanism. The angle $\theta$ is cyclic, its momentum $p_\theta=\ell$ is conserved, and the Routhian is a function of $r$ alone, whose Lagrange equation is

$$
md^2r/dt^2=-V'(r)+\frac{\ell^2}{mr^3},
$$

the centrifugal term appearing as a consequence of the transform rather than as an inserted fictitious force. The partition is arbitrary — nothing requires the transformed coordinates to be the cyclic ones, and choosing them so is a convenience. This article applies the transform to the whole configuration, which is the case $s=n$; the partial case is recorded because it is the general form, and because it shows that which variable is eliminated is a choice of description and not of physics. The other classical reformulation worth naming is **Appell's**, whose equations of motion are written in the **generalized accelerations** $\alpha_r=d^2q_{r}/dt^2$ rather than in the generalized velocities, with the generalized forces of D'Alembert's principle.

## Phase Space as a Single Biquaternion

For a system with three degrees of freedom the position and momentum are pure real quaternions, $\tilde q,\tilde p\in\mathbb{H}_{\mathbb{B}}\cap\mathbb{M}_-$, and they combine into the single biquaternion

$$
\tilde Z=\tilde q+i\tilde p\in\mathbb{B}.
$$

Its anti-Hermitian and Hermitian parts are

$$
\tilde Z_{-}=\tfrac{1}{2}\!\left(\tilde Z-\tilde Z^{*}\right)=\tilde q\in\mathbb{M}_-,\qquad
\tilde Z_{+}=\tfrac{1}{2}\!\left(\tilde Z+\tilde Z^{*}\right)=i\tilde p\in\mathbb{M}_+,
$$

as follows from $\tilde q^{*}=-\tilde q$ and $(i\tilde p)^\dagger=i\tilde p$ for pure real $\tilde q,\tilde p$. The phase-space coordinate is thus a general biquaternion; its **material part is the configuration** and its **informational part is $i$ times the momentum**. The two sectors of the algebra separate position from conjugate momentum, and the decomposition $\mathbb{B}=\mathbb{M}_-\oplus\mathbb{M}_+$ is the algebraic form of the split of the phase space into configuration and momentum.

The algebra's **complex structure** is the map $\tilde Z\mapsto i\tilde Z$. Since $i\mathbb{M}_\pm=\mathbb{M}_\mp$, it exchanges the two parts; explicitly,

$$
i\tilde Z=i\tilde q-\tilde p .
$$

Multiplication by $i$ therefore turns the configuration into (minus) the momentum and the momentum into the configuration, up to the sector assignment. This is why the oscillator's quarter-period evolution exchanges the two: the oscillator flow is a rotation in the plane spanned by $\tilde q$ and $\tilde p$, and the complex structure is that rotation by $\pi/2$. It is also the structural statement behind the observation, in the companion article *The Harmonic Oscillator in Biquaternionic Form*, that the oscillator's phase is generated by the sector-exchanging element $ie_t$.

The same assembly works for a system with four degrees of freedom, with $\tilde q,\tilde p$ general real quaternions, and the sector split then reads

$$
\tilde Z_{+}=\tfrac{1}{2}\!\left(\tilde Z+\tilde Z^{*}\right)=q_t\,e_t+i\,\vec p ,\qquad
\tilde Z_{-}=\tfrac{1}{2}\!\left(\tilde Z-\tilde Z^{*}\right)=i\,p_t\,e_t+\vec q ,
$$

so that the two vector parts separate as configuration and momentum while the two scalar components pair the other way: the configuration scalar $q_t$ is Hermitian and the momentum scalar $i\,p_t$ is anti-Hermitian. The clean statement — material part the configuration, informational part $i$ times the momentum — is the three-degree-of-freedom case $q_t=p_t=0$, which is also the one that carries the spatial interpretation.

## The Four-Hamiltonian and the Exactness of the Action Form

The phase-space biquaternion $\tilde Z=\tilde q+i\tilde p$ packages the **configuration** with the **momentum**. There is a second packaging, and it is the covariant one: the Hamiltonian with the canonical momentum in the same biquaternion. Gsponer and Hurni call it the **four-Hamiltonian**

$$
\Pi = \left[H(t,x\,\vec e_x+y\,\vec e_y+z\,\vec e_z,\vec\pi)\,;\,-i\vec\pi(t,x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)\right],
$$

a bireal — that is, Hermitian — biquaternion whose scalar part is the Hamiltonian and whose vector part carries the canonical momentum. For $n$ point particles in a time-independent external field it is assembled from the four-momenta and the potential,

$$
\Pi = \sum_n P_n + ϙ_n A(X_n), \qquad P_n = [E_n\,;\,-ic\vec p_n], \qquad A = [\phi\,;\,-i\vec A],
$$

in the source's notation, so the scalar part is the Hamiltonian $H=E+ϙ\phi$ and the vector part the canonical momentum $\vec\pi=\vec p+ϙ\vec A$. Up to the central factor $-i$ — the corpus's placement of the time component in the scalar slot — the four-momenta here are the corpus's four-momentum $\tilde P$, and the source's mass-shell statement $|P|^2=m^2$ (units with $c=1$) is the corpus's $\langle\tilde P\rangle_{\natural}=-m^2c^2$.

The reason to introduce the object is the action. The source's **action postulate** is

$$
\tilde\nabla S = i\Pi ,
$$

that is, the four-Hamiltonian derives from a single invariant scalar $S$, the action. In the corpus's vocabulary the content of the postulate is that $\Pi$ is, up to the central factor $-i$, a gradient: the components satisfy $\partial_\mu\Pi_\nu=\partial_\nu\Pi_\mu$, which is the statement that the one-form $\Pi$ is **closed** and therefore locally exact. The source writes the same condition as $\tilde\nabla\wedge\Pi=0$, and reads it as $d\Pi$ being a total differential, equivalently

$$
\oint dX\circ\Pi = 0 ,
$$

which for two fixed endpoints is Hamilton's principle, $\delta\int_{X_1}^{X_2} dX\circ\Pi = 0$. Hamilton's principle is thus, in this formulation, the **exactness of the four-Hamiltonian one-form**; and for a Hamiltonian with no explicit time dependence the same condition is equivalent to Hamilton's equations $d(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)/dt=d H/d\vec\pi$, $d\vec\pi/dt=-d H/d(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z)$.


**Two packagings, two sectors.** The contrast with the previous section is exact. The phase-space biquaternion $\tilde Z$ pairs a material part with an informational part; the four-Hamiltonian $\Pi$ lies **entirely** in the Hermitian (informational) sector, its two halves being the Hamiltonian and the momentum rather than a position and a momentum. The corpus has both objects: $\tilde Z$ for the configuration–momentum split and $\Pi$ for the covariant energy–momentum-plus-potential object whose potential is the action.

**The Hamilton–Jacobi rewriting.** With the four-Hamiltonian in hand the relativistic mass-shell identity converts the action postulate into the **relativistic Hamilton–Jacobi equation** for a charged particle in an electromagnetic field: the source's form sets the quaternion square of $i\tilde\nabla S+e\tilde A$ equal to $m^2$, the sign of the $e\tilde A$ term following the charge-sign convention. The non-relativistic Hamilton–Jacobi equation and its biquaternion-norm interpretation are the subject of the companion article *The WKB Approximation and the Hamilton–Jacobi Equation in Biquaternionic Form*; the four-Hamiltonian is the covariant object beneath that equation, and the corpus records it here.

## The Poisson Bracket

### The Biquaternion Form

For central-valued observables $f(\tilde q,\tilde p)$, $g(\tilde q,\tilde p)$, the Poisson bracket is the scalar part of a quaternion expression. Define the gradients

$$
\nabla_{\tilde q}f=\sum_\mu e_\mu\frac{\partial f}{\partial q_\mu},\qquad
\nabla_{\tilde p}f=\sum_\mu e_\mu\frac{\partial f}{\partial p_\mu}.
$$

Using $\mathrm{Sc}(\tilde q_1^{\natural}\tilde q_2)=\sum_\mu q_{1\mu} q_{2\mu}$ for real quaternions, the bracket is

$$
\boxed{\;\{f,g\}=\mathrm{Sc}\!\left(\overline{\nabla_{\tilde q}f}\;\nabla_{\tilde p}g\right)
-\mathrm{Sc}\!\left(\overline{\nabla_{\tilde p}f}\;\nabla_{\tilde q}g\right).\;}
$$

Only the scalar part of each quaternion product enters. For pure $\tilde q_1,\tilde q_2$ the product $\tilde q_1^{\natural}\tilde q_2$ has a vector part as well, $-\tilde q_1\times\tilde q_2$; in general the vector part is $q_{10}\vec q_2-q_{20}\vec q_1-\vec q_1\times\vec q_2$, and only the cross-product term is intrinsic to the pairing. The Poisson bracket discards it, and the discarded part is precisely the cross-product structure that reappears as the angular-momentum bracket below. This is the algebraic content of the statement that the classical bracket is the antisymmetric scalar pairing of two gradients.

Because the bracket is built from scalar parts of quaternion products, it is automatically bilinear and antisymmetric, and in these coordinates it is the canonical bracket in disguise, so it satisfies the Jacobi identity. The derivation property $\{f,gh\}=\{f,g\}h+g\{f,h\}$ holds for the commutative product of central-valued functions, exactly as in the standard theory.

### Canonical Brackets

For the coordinate and momentum functions $q_\mu$, $p_\nu$ one has $\nabla_{\tilde q}q_\mu=e_\mu$, $\nabla_{\tilde q}p_\nu=0$, and so

$$
\{q_\mu,q_\nu\}=0,\qquad \{p_\mu,p_\nu\}=0,\qquad \{q_\mu,p_\nu\}=\delta_{\mu\nu}.
$$

These are the standard canonical brackets, written with the algebra's basis rather than with an index list. Hamilton's equations take the bracket form

$$
df/dt=\{f,H\},
$$

which for $f=q_\mu,p_\nu$ reproduces $dq_{\mu}/dt=\partial H/\partial p_\mu$, $dp_{\nu}/dt=-\partial H/\partial q_\nu$.

### Canonical Transformations

A change of phase-space variables $(\tilde q,\tilde p)\to(\tilde Q,\tilde P)$ that preserves the form of Hamilton's equations is a **canonical transformation**, and the test is a statement about the bracket alone:

$$
\{Q_\mu,Q_\nu\}=0,\qquad \{P_\mu,P_\nu\}=0,\qquad \{Q_\mu,P_\nu\}=\delta_{\mu\nu},
$$

evaluated with the original bracket. A transformation satisfying these is canonical; one that fails any of them is not. The criterion is worth recording for a reason specific to this article: it is **scalar**. It never asks what the discarded vector part of the quaternion product does. That is the sharpest support for the claim made below in *What the Bracket Is Not*: the classical structure of the theory, including which changes of variable are permitted, lives entirely in the scalar projection of the quaternion product, while the vector part carries the rotations. The generating functions of such transformations are the ones whose freedom the Standard Formulation notes: the Hamiltonian is fixed only up to the partial time derivative of an arbitrary function of coordinates, momenta and time.

### Angular Momentum

For a particle, the product of position and momentum is

$$
\tilde q\,\tilde p=-\vec q\cdot\vec p+\vec L,\qquad \vec L=\vec q\times\vec p,
$$

for the pure-vector configuration $\tilde q,\tilde p$ that carries the spatial interpretation. The scalar part is (minus) the contraction of position and momentum, and the **vector part is the angular momentum** $\vec L$. This is the biquaternion form of the cross-product formula $\vec L=\vec r\times\vec p$. Its components satisfy, as in the companion article *Similitudes Between Biquaternion Rotors and Hamiltonian Flow*,

$$
\{L_i,L_j\}=\varepsilon_{ijk}L_k,\qquad \{L_i,q_j\}=\varepsilon_{ijk}q_k,\qquad \{L_i,p_j\}=\varepsilon_{ijk}p_k .
$$

The first of these is the statement that the components of angular momentum close into $\mathrm{SU}(2)$ under the Poisson bracket; it is the bracket that the biquaternion algebra realizes **exactly**, because the quaternion product already carries the cross product, with no deformation parameter. The companion article *Similitudes Between Biquaternion Rotors and Hamiltonian Flow* identifies the corresponding one-parameter group: on the coadjoint orbit, the flow generated by $H=2G\cdot\vec S$ is the rotor conjugation by $\exp(tG)$, and the generators agree term for term.

### What the Bracket Is Not

The bracket defined above is the classical Poisson bracket of a commutative algebra of central-valued functions. It is not a commutator, and it does not require or imply one. The companion article *Similitudes Between the Poisson Bracket and the Quantum Commutator* shows that the two brackets are not isomorphic, and that the canonical algebra of a Heisenberg pair cannot be realized inside the finite-dimensional algebra $\mathbb{B}$; the companion article *The Harmonic Oscillator in Biquaternionic Form* confirms the obstruction in the oscillator setting. Nothing in the present article uses that obstruction, because the classical formulation needs no commutator; the bracket is the scalar pairing of gradients, and the algebra supplies it directly.

## The Action, Symmetries, and Conservation

The action of the biquaternion formulation is

$$
S[\tilde q]=\int L(\tilde q,d\tilde q/dt,t)\,dt ,
$$

a central-valued functional of a real-quaternion path. Its stationarity gives the Euler–Lagrange equation derived above; the next article develops the action principle and the stationary-phase statement of the classical limit.

The symmetries that the algebra makes visible are the following.

**Time translation.** If $L$ has no explicit time dependence, Noether's theorem gives the conserved energy $E=\mathrm{Sc}(\tilde p^{\natural}d\tilde q/dt)-L=H$.

**Configuration-space rotations.** A rotation of the configuration acts by the **rotor conjugation**

$$
\tilde q\longmapsto \tilde u\,\tilde q\,\tilde u^{*},\qquad \tilde u\in\mathbb{H}_{\mathbb{B}},\quad \tilde u\tilde u^{\natural}=e_t .
$$

The biquaternion norm is invariant, $\langle\tilde u\tilde q\tilde u^{*}\rangle_{\natural}=\langle\tilde q\rangle_{\natural}$, because the rotor has unit norm. If the potential is rotationally invariant, so is the Lagrangian, and the conserved Noether charge is the angular momentum $\vec L=\vec q\times\vec p$ of the previous section. This is the classical mechanics reading of the rotor: the rotation group is the group of unit real quaternions $SU(2)$, acting on the configuration by conjugation. The companion article *Similitudes Between Biquaternion Rotors and Hamiltonian Flow* develops the rotor-flow correspondence, and the companion article *Noether's Theorem in Biquaternionic Form* develops the general current construction.

**The central phase.** Because $i$ is central, a central phase acts on the biquaternion-valued configuration by $\tilde q\mapsto \exp(i\alpha)\tilde q$. For a real-quaternion configuration it does not preserve the real subspace — $\exp(i\alpha)\tilde q$ is a complex biquaternion unless $\tilde q=0$ — so it is a symmetry of the complexified formulation rather than of the real configuration space; it becomes a genuine internal symmetry only for a complex biquaternion-valued field, where it is the $\mathrm{U}(1)$ of the companion article *The Gauge Principle in Biquaternionic Form*. It also acts on the free Lagrangian, $L=\tfrac12mN(d\tilde q/dt)\mapsto \exp(2i\alpha)L$, so a real Lagrangian is invariant only for $\exp(2i\alpha)=1$: the transformation is a symmetry of the complexified formulation and not of the real one. In the present classical setting it acts on the phase-space biquaternion $\tilde Z$ and is the algebra's complex structure; its consequences for the action and for the symplectic structure are developed in the companion articles *The Action Principle and the Classical Limit as Stationary Phase in Biquaternionic Form* and *The Symplectic Form and the Biquaternion Norm Cone*.

## What the Formulation Does and Does Not Give

The transcription is exact within its domain, and the domain is worth stating plainly.

**What it gives.** For a system whose configuration is a real quaternion — a particle in three dimensions with an optional scalar degree of freedom — the Lagrangian and Hamiltonian formalism is written without index clutter: the kinetic energy is the biquaternion norm, the momentum is its Legendre conjugate, the Hamiltonian of a free particle is the biquaternion norm of the momentum, the Euler–Lagrange and Hamilton equations are single quaternion equations, and the Poisson bracket is the scalar pairing of two quaternion gradients. The phase-space coordinate is one biquaternion whose sectors are the configuration and the momentum. The rotational bracket is exact, with the quaternion product's cross product supplying the structure constants.

**What it does not give.** The algebra is finite dimensional; it cannot carry the configuration space of a system with more than a few degrees of freedom, nor an infinite-dimensional field configuration except through its coefficients. The Poisson bracket is a scalar projection of a quaternion product, and the vector part it discards is not a second bracket. And the canonical Heisenberg sector is absent: there is no pair $\tilde q,\tilde p$ inside $\mathbb{B}$ whose bracket is a central constant, as the companion articles *Similitudes Between the Poisson Bracket and the Quantum Commutator* and *The Harmonic Oscillator in Biquaternionic Form* prove. None of these limitations is a defect of the transcription; they are properties of the algebra, and they mark where the biquaternion language is a convenience and where it is a constraint.

**The field case.** The one direction in which the finite-dimensional transcription is extended rather than limited is the field, and it is the subject of the companion article *Hamiltonian Field Theory in Biquaternionic Form*. There the single conjugate momentum becomes a conjugate momentum field, the Legendre transform acts on a density, the bracket becomes a bracket on functionals with $\{\phi(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z),\pi(\vec y)\}=\delta^3(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z-\vec y)$, the Hamiltonian becomes the integral of a density whose Hermitian-form expression is the energy density, and the conservation law becomes the continuity equation for the energy flux, whose density and flux are the scalar and vector parts of one Hermitian biquaternion. The central scalar field is the case in which the algebra's contribution is the packaging and the sector interpretation rather than a change of the bracket, and it is the case that the article on canonical quantization takes over unchanged.

## Summary

The Lagrangian and Hamiltonian formulations of classical mechanics take the following form in the biquaternion algebra.

- The configuration is a real quaternion $\tilde q\in\mathbb{H}_{\mathbb{B}}$, with the physical three-space as its pure-vector part; the kinetic energy is the biquaternion norm, $T=\tfrac{1}{2}mN(d\tilde q/dt)$.
- The action $S[\tilde q]=\int L\,dt$ is stationary at the physical path, and stationarity gives the single quaternion Euler–Lagrange equation $\frac{d}{dt}\partial L/\partial\left(d\tilde q/dt\right)-\partial L/\partial\tilde q=0$, equivalent to the four real equations.
- The conjugate momentum is $\tilde p=\partial L/\partial\left(d\tilde q/dt\right)$, and the Hamiltonian is the Legendre transform $H=\mathrm{Sc}(\tilde p^{\natural}d\tilde q/dt)-L$. For a free particle $H=\langle\tilde p\rangle_{\natural}/2m$: the free Hamiltonian is the biquaternion norm of the momentum.
- Hamilton's equations are $d\tilde q/dt=\partial H/\partial\tilde p$, $d\tilde p/dt=-\partial H/\partial\tilde q$.
- Position and momentum combine into the phase-space biquaternion $\tilde Z=\tilde q+i\tilde p$, whose anti-Hermitian part is the configuration and whose Hermitian part is $i$ times the momentum. The algebra's complex structure $i$ exchanges the two parts.
- The Poisson bracket is $\{f,g\}=\mathrm{Sc}(\overline{\nabla_{\tilde q}f}\nabla_{\tilde p}g)-\mathrm{Sc}(\overline{\nabla_{\tilde p}f}\nabla_{\tilde q}g)$, the scalar part of a quaternion expression; the discarded vector part is the cross product that makes the angular-momentum bracket $\{L_i,L_j\}=\varepsilon_{ijk}L_k$ exact.
- Rotational symmetry acts by rotor conjugation $\tilde q\mapsto\tilde u\tilde q\tilde u^{*}$, and its Noether charge is $\vec L=\vec q\times\vec p$.
- The Lagrangian is determined only up to a total time derivative: $L$ and $L+dF(q,t)/dt$ have the same equations of motion, and their actions differ by the endpoint term $F(t_2)-F(t_1)$, which a variation with fixed endpoints cannot see. This is the same boundary freedom that appears as the symplectic potential in the variation of the action.
- The Legendre transform may be applied to a subset of the coordinates. The partial transform is the **Routhian**, which puts the transformed coordinates — conventionally the cyclic ones, whose momenta are conserved — in Hamiltonian form and the rest in Lagrangian form; for a central potential it produces the centrifugal term as a transformed potential.
- In the Hamiltonian description coordinates, velocities and momenta are **mutually independent** variables; the relation $\tilde p=\partial L/\partial\left(d\tilde q/dt\right)$ is used only to eliminate the velocity. This is what makes the transform a change of variables and $\tilde Z=\tilde q+i\tilde p$ a coordinate.
- $H=T+V$ is not automatic. It requires $T$ homogeneous of degree two in the velocities, which $T=\tfrac12mN(d\tilde q/dt)$ satisfies by construction; with $L$ time-independent, $H$ is then the conserved energy. Explicit time dependence is preserved by the transform, $\partial H/\partial t=-\partial L/\partial t$.
- A change of phase-space variables is **canonical** exactly when it preserves the brackets $\{Q_\mu,P_\nu\}=\delta_{\mu\nu}$. The criterion is scalar, so the permitted changes of variable live in the scalar projection of the quaternion product alone.

The formulation is a transcription, exact for configurations that fit in a real quaternion. It introduces no commutator and no $\hbar$; the canonical Heisenberg structure is absent from the finite-dimensional algebra, and the classical bracket that the algebra does carry is the scalar part of a quaternion product.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_k^2=-e_t$ |
| $i$ | Central scalar imaginary, $i^2=-1$ |
| $\mathbb{M}_-,\mathbb{M}_+$ | Anti-Hermitian (material) and Hermitian (informational) sectors |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace |
| $\tilde q=q_te_t+\vec q$ | Configuration quaternion (real) |
| $d\tilde q/dt$ | Configuration velocity |
| $\langle\tilde q\rangle_{\natural} = \langle\tilde q,\tilde q\rangle_{\natural}=\tilde q\tilde q^{\natural}$ | Biquaternion norm |
| $L(\tilde q,d\tilde q/dt,t)$ | Lagrangian |
| $F(\tilde q,t)$, $L'=L+dF/dt$ | Arbitrary function and the total-derivative ambiguity of the Lagrangian |
| $S[\tilde q]=\int L\,dt$ | Action; ambiguous by the endpoint term $F(t_2)-F(t_1)$ |
| $R=\mathrm{Sc}(\bar p\,dq/dt)-L$ (over the transformed block) | Routhian: the partial Legendre transform, shown in the general case, of which this article uses $s=n$ |
| $T(\lambda\,d\tilde q/dt)=\lambda^2T(d\tilde q/dt)$ | Homogeneity of the kinetic energy; gives $\mathrm{Sc}(\tilde p^{\natural}d\tilde q/dt)=2T$ and $H=T+V$ |
| $\partial H/\partial t=-\partial L/\partial t$ | Explicit time dependence is preserved with reversed sign |
| $\{Q_\mu,P_\nu\}=\delta_{\mu\nu}$ | Canonical-transformation criterion (scalar) |
| $\partial L/\partial\tilde q=\sum_\mu e_\mu\partial L/\partial q_\mu$ | Quaternion gradient of a central-valued function |
| $\tilde p=\partial L/\partial\left(d\tilde q/dt\right)$ | Conjugate momentum (real quaternion) |
| $H=\mathrm{Sc}(\tilde p^{\natural}d\tilde q/dt)-L$ | Hamiltonian (Legendre transform) |
| $\tilde Z=\tilde q+i\tilde p$ | Phase-space biquaternion |
| $\nabla_{\tilde q}f,\nabla_{\tilde p}f$ | Gradients of an observable |
| $\{f,g\}$ | Poisson bracket |
| $\vec L=\vec q\times\vec p$ | Angular momentum |
| $\tilde u\in\mathbb{H}_{\mathbb{B}}$, $\langle\tilde u\rangle_{\natural}=e_t$ | Rotation rotor |
| $\mathrm{Tr}(e_t)=2$ | Trace normalization |
| $\langle\tilde{P},\tilde{Q}\rangle_{*}$ | the general plain sesquilinear form, $\mathrm{Sc}(\tilde{P}\tilde{Q}^{*})$; on the diagonal $\langle\tilde{Q},\tilde{Q}\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^{2}$ |

## Further Reading

- H. Goldstein, C. P. Poole, and J. L. Safko, *Classical Mechanics* (Addison-Wesley, 2002), for the standard Lagrangian and Hamiltonian formulation, the Legendre transform, and the Poisson bracket.
- L. D. Landau and E. M. Lifshitz, *Mechanics* (Pergamon, 1976), for the action principle, Noether's theorem, and canonical equations.
- V. I. Arnold, *Mathematical Methods of Classical Mechanics* (Springer, 1989), for the symplectic and Poisson-geometric formulation of Hamiltonian mechanics.
- W. R. Hamilton, *Lectures on Quaternions* (Hodges and Smith, 1853), for the quaternion algebra and the quaternion product.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for quaternions, rotors, and their relation to the Lorentz group.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric-algebra treatment of rotors, rigid bodies, and mechanics.
- David Hestenes, *New Foundations for Classical Mechanics* (Reidel, 1986), for a treatment of classical mechanics in a real Clifford algebra closely related to the quaternion one.
- *Hamiltonian Field Theory in Biquaternionic Form* (`articles_physics/hamiltonian-field-theory-in-biquaternionic-form.md`), companion article, for the extension of the Legendre transform, the bracket and the conservation law to a field, where the conjugate momentum is a field and the density and flux are one Hermitian biquaternion.
- A. Gsponer and J.-P. Hurni, "The physical heritage of Sir W. R. Hamilton," arXiv:math-ph/0201058, §5, for the four-Hamiltonian $\Pi=[H;-i\vec\pi]$, the action postulate $\tilde\nabla S=i\Pi$, and the interpretation of Hamilton's principle as the exactness of the one-form $dX\circ\Pi$.
- W. R. Hamilton, *Elements of Quaternions*, Vol. II, art. 419 (2nd ed., enlarged by C. J. Joly, 1899–1901), for the quaternion resolution of the Kepler problem and the conservation of the angular-momentum and Runge–Lenz vectors.
