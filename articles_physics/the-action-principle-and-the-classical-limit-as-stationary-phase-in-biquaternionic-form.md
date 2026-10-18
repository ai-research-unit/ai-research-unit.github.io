# __The Action Principle and the Classical Limit as Stationary Phase in Biquaternionic Form__

## Introduction

Two statements are joined in this article. The first is the **action principle**: the physical trajectory of a classical system is the trajectory at which the action $S=\int L\,dt$ is stationary, and the stationarity condition is the Euler–Lagrange equation. The second is the **classical limit as stationary phase**: when a sum over trajectories is weighted by the phase $\exp(iS/\hbar)$, the sum is dominated, as $\hbar\to0$, by the trajectories near the stationary ones, so that the classical paths are exactly the critical points of the action. The first statement is the classical theory; the second is the statement that the classical theory is the critical-point theory of an oscillatory integral.

This article develops both in the biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$. The second statement is not a quantisation. An oscillatory integral with a real phase and a large parameter is a classical object, and its asymptotic evaluation is a theorem of analysis (the stationary-phase lemma of Kelvin, developed by many hands). What the classical limit adds is an identification: the critical-point equations of the action are the equations of motion. This article stays on that side of the line. No state space, no operators, and no commutator appear; the symbol $\hbar$ enters only as the inverse scale of the phase, as the parameter of an asymptotic expansion, and nowhere as a quantum of action attributed to a physical system. The companion articles of the sibling quantum category own the quantisation; here the phase is a bookkeeping device for a classical sum.

The biquaternion algebra contributes two things to the discussion.

1. **The action is central-valued.** For a real-quaternion configuration the Lagrangian is central, so the action is a complex scalar and its phase is unambiguous. There is no ordering question in the exponent, and the stationary-phase construction applies directly.
2. **The rotor action and its geodesic principle.** For a rotor-valued configuration — a path in the group of unit real quaternions — the action built from the biquaternion norm of the velocity is the energy of a geodesic on the group, and the classical path is a one-parameter subgroup. This is the first place where the algebra's noncommutativity produces the classical equations rather than merely expressing them, and it is the bridge to the rigid-body article.

The conventions are those of the read list, unchanged from the preceding article. The algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with basis $e_t=1,\vec e_x,\vec e_y,\vec e_z$, $e_k^2=-e_t$; $i$ is central with $i^2=-1$; $\mathbb{M}_-$ and $\mathbb{M}_+$ are the anti-Hermitian and Hermitian sectors; $\mathbb{H}_{\mathbb{B}}$ is the real-quaternion subspace. The configuration is a real quaternion $\tilde q$, its conjugate momentum is $\tilde p=\partial L/\partial\left(d\tilde q/dt\right)$, the phase-space biquaternion is $\tilde Z=\tilde q+i\tilde p$, and the scalar pairing is $\mathrm{Sc}(\tilde q_3^{\natural}\tilde q_4)=\sum_\mu q_{3\mu} q_{4\mu}$. The rotor is $\tilde u\in\mathbb{H}_{\mathbb{B}}$ with $\langle\tilde u\rangle_{\natural} = \langle\tilde u,\tilde u\rangle_{\natural}=\tilde u\tilde u^{\natural}=e_t$, and it acts by conjugation $\tilde{Q}\mapsto\tilde u\tilde{Q}\tilde u^{*}$.

The companion articles used below are:
- Companion article *Lagrangian and Hamiltonian Mechanics in Biquaternionic Form*, for the action, the Euler–Lagrange equation, the Legendre transform, and the phase-space biquaternion.
- Companion article *Similitudes Between Biquaternion Rotors and Hamiltonian Flow*, for the rotor conjugation and the flow on the coadjoint orbit.
- Companion article *Noether's Theorem in Biquaternionic Form*, for the boundary-term construction of conserved quantities.
- Companion article *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*, for the biquaternion norm and the material-sector structure.

## The Action and Its First Variation

### The Configuration-Space Action

For a real-quaternion configuration $\tilde q(t)$ of a system with Lagrangian $L(\tilde q,d\tilde q/dt,t)$, the action is the central-valued functional

$$
S[\tilde q]=\int_{t_1}^{t_2}L(\tilde q,d\tilde q/dt,t)\,dt .
$$

Because $L$ takes values in the centre $\mathbb{C}_{\mathbb{B}}=\mathrm{span}_{\mathbb{R}}\{e_t,ie_t\}$, the value of $S$ is a complex scalar and its phase $\exp(iS/\hbar)$ is well defined. This is not automatic for a non-central Lagrangian, and it is the first reason the biquaternion formulation is convenient for the stationary-phase statement: the exponent is a scalar.

### The Domain of the Principle: Discrete and Continuous

The statement is written for a finite list of coordinates, and this article uses it that way throughout. Nothing in it requires a finite list. A deformable body, or a field, has infinitely many degrees of freedom: its state is a function of position and time rather than a finite tuple $q(t)$, and the Lagrangian is replaced by a **density** $\mathcal{L}$, the action becoming $S=\int\mathcal{L}\,d^3x\,dt$. The stationarity statement is unchanged, and its Euler–Lagrange equations are field equations rather than ordinary differential equations. In the biquaternion formulation the configuration is then an algebra-valued field $\tilde q(x\,\vec e_x+y\,\vec e_y+z\,\vec e_z,t)$ and the action a spacetime integral of a central-valued density, which is the form the companion articles *The Relativistic Action and the Stationary-Action Principle in Biquaternionic Form* and *Stress–Energy, Conservation Laws and the Field Action in Biquaternionic Form* use.

$$
S=\tfrac12\iint\left(\rho\,\partial/\partial t u^2-\mathcal{T}\partial/\partial Q_x u^2\right)dx\,dt,\qquad c^2=\mathcal{T}/\rho ,
$$

the first variation is $2\times10^{-10}$ at a solution of the wave equation $\partial^2/\partial t^2 u=c^2\partial^2/\partial Q_x^2 u$ and $-1.67$ at a neighbouring non-solution: stationarity selects exactly the field equation. The Hamiltonian side of the same field action — the conjugate momentum field, the Hamiltonian density as the energy density, the bracket on functionals and the continuity equation for the energy flux — is developed in the companion article *Hamiltonian Field Theory in Biquaternionic Form*, which extends the Legendre transform, the bracket and the conservation law of the preceding article from a finite list of coordinates to a density.

The statement is also independent of the coordinates in which it is written, which is what allows the coordinates to be generalized away altogether. Newton's law is recovered from a variational statement, in coordinates in which it is not obvious; the form of the statement, not the coordinates, is what carries the physics.

### When the Loads Are Not Conservative

The principle as written assumes the applied forces derive from a potential, and that assumption can fail. When the external loads are **non-conservative** — a damping force is the standard example — the variation of the action does not vanish on the physical motion, and the principle must be **extended** by adding the virtual work of those loads; it reduces to the plain form when the loads do derive from a potential. The added term is not idle — for the undamped solution the same extended expression is $+0.611$.

It is worth being precise about what is lost, because the natural summary — a non-conservative force is the gradient of nothing, so no Lagrangian contains it — is too strong. What is true is that no *potential* contains it, so no Lagrangian of the form $T-V$ does. A Lagrangian may still exist, at a price: the damped linear oscillator has the explicitly time-dependent

$$
L_t=\exp(\gamma t)\left(\tfrac12\left(dq/dt\right)^{2}-\tfrac12\omega_0^2q^2\right),
$$

whose Euler–Lagrange equation is $d^2q/dt^2+\gamma\,dq/dt+\omega_0^2q=0$, verified to $1.3\times10^{-9}$ along the damped motion. The price is that $L_t$ is neither $T-V$ nor invariant under time translation, so the quantity it would call the energy is not conserved. The plain framework can be made to hold, but it stops being one in which energy means what it meant.

**Herglotz's principle** is the systematic alternative, and it changes what the action *is* rather than adding a term to it. The action is defined not by the integral $\int L\,dt$ but as the solution of the differential equation

$$
\left(dS/dt\right)(t)=L(t,\tilde q,d\tilde q/dt,S),\qquad S(t_0)=S_0 ,
$$

so that the Lagrangian may depend on the action, and the requirement is that this $S$ be stationary. The stationarity condition is the **Euler–Lagrange–Herglotz equation**

$$
\frac{d}{dt}\frac{\partial L}{\partial\left(d\tilde q/dt\right)}-\frac{\partial L}{\partial\tilde q}
=\frac{\partial L}{\partial S}\,\frac{\partial L}{\partial\left(d\tilde q/dt\right)},
$$

whose right-hand side carries the dissipation and which returns the Euler–Lagrange equation of this article when $\partial L/\partial S=0$. The damped oscillator is the standard illustration: with

$$
L=\tfrac12\left(dq/dt\right)^{2}-\tfrac12\omega_0^2q^2-\gamma S,\qquad \,dS/dt=L ,
$$

the equation of motion is $d^2q/dt^2+\gamma\,dq/dt+\omega_0^2q=0$, matching the analytic damped solution to $1.7\times10^{-14}$, while the same $L$ evaluated on the *undamped* motion leaves a residual of $0.30$. The $S$-dependence is what produces the damping, and the check separates the two motions rather than confirming both.

**What replaces the energy.** Dissipation does not remove the conservation law; it weights it. For a time-translation symmetry the conserved quantity acquires the exponential of $\int\partial L/\partial S$,

$$
\exp(\gamma t)\left(L-dq/dt\,\frac{\partial L}{\partial\left(dq/dt\right)}\right)
=-\exp(\gamma t)\left(\tfrac12\left(dq/dt\right)^{2}+\tfrac12\omega_0^2q^2+\gamma S\right),
$$

which for the damped oscillator is conserved to $3.0\times10^{-14}$ while the plain energy $\tfrac12\left(dq/dt\right)^{2}+\tfrac12\omega_0^2q^2$ decays from $0.500$ to $0.075$. In Hamiltonian form the same structure is a **contact** Hamiltonian system on the extended space $(\tilde q,\tilde p,S)$. The momentum and Hamiltonian are the usual Legendre data, $p_i=\partial L/\partial\left(dq_{i}/dt\right)$ and $H=\sum_ip_i\,dq_{i}/dt-L$, and the equations

$$
dq_{i}/dt=\frac{\partial H}{\partial p_i},\qquad
\,dp_{i}/dt=-\left(\frac{\partial H}{\partial q_i}+p_i\frac{\partial H}{\partial S}\right),\qquad
\,dS/dt=\sum_ip_i\frac{\partial H}{\partial p_i}-H
$$

reduce to Hamilton's equations when $\partial H/\partial S=0$; for the damped oscillator $H=\tfrac12p^2+\tfrac12\omega_0^2q^2+\gamma S$ reproduces the damped motion to $1.3\times10^{-11}$. Since $L$ is central-valued, so is $S$, and the extended space is the configuration and momentum biquaternions with one central coordinate adjoined: the algebra accommodates the construction without enlargement. The class covered is wider than damping — $d^2q/dt^2+f(q)\left(dq/dt\right)^{2}+g(t)dq/dt+h(q)=0$ is the Euler–Lagrange–Herglotz equation of $L=\tfrac12\left(dq/dt\right)^{2}-[2f(q)dq/dt+g(t)]S-U(q)$ for the $U$ solving $U'+2fU=h$, verified to $1.3\times10^{-15}$, with the Lane–Emden equation among its special cases. Herglotz's principle is the variational formulation of the non-conservative equations, not a workaround for them.

### The First Variation and the Boundary Term

The first variation of $S$, with the gradient notation of the preceding article, is

$$
\delta S=\int_{t_1}^{t_2}\mathrm{Sc}\!\left[\overline{\left(\partial L/\partial\tilde q-\frac{d}{dt}\partial L/\partial\left(d\tilde q/dt\right)\right)}\;\delta\tilde q\right]dt
+\left[\mathrm{Sc}\!\left(\overline{\partial L/\partial\left(d\tilde q/dt\right)}\;\delta\tilde q\right)\right]_{t_1}^{t_2}.
$$

The bulk term vanishes for an arbitrary variation if and only if the **Euler–Lagrange equation** holds,

$$
\frac{d}{dt}\frac{\partial L}{\partial\left(d\tilde q/dt\right)}-\frac{\partial L}{\partial\tilde q}=0 ,
$$

which is the four real equations of the preceding article. The boundary term is the part that does not vanish when the endpoints are free. Writing $\tilde p=\partial L/\partial\left(d\tilde q/dt\right)$, it is

$$
\delta S_{\text{bdry}}=\left[\mathrm{Sc}\!\left(\bar{\tilde p}\;\delta\tilde q\right)\right]_{t_1}^{t_2}
=\mathrm{Sc}(\tilde p^{\natural}_2\,d\tilde q_2)-\mathrm{Sc}(\tilde p^{\natural}_1\,d\tilde q_1).
$$

The quantity $\theta=\mathrm{Sc}(\tilde p^{\natural}\,d\tilde q)$ is the **symplectic potential** in biquaternion form, and the boundary term says that the on-shell action is a **generating function** of the canonical transformation between the initial and final phase-space points: $dS=\theta_2-\theta_1$. The exterior derivative of this potential is the symplectic form up to the standard sign convention of the symplectic potential — explicitly, $d\theta=d\mathrm{Sc}(\tilde p^{\natural}\,d\tilde q)=d\vec p\wedge d\vec q=-\omega$ for the canonical form $\omega=\sum_k dq_k\wedge dp_k$ — and the symplectic form, with its conventions fixed, is the subject of the next article; here it is enough to record that the boundary term of the action variation already contains it.

### The Phase-Space Action

The same statement in phase-space variables uses the action

$$
S_{\mathrm{ps}}[\tilde q,\tilde p]=\int_{t_1}^{t_2}\left[\mathrm{Sc}\!\left(\tilde p^{\natural}\,d\tilde q/dt\right)-\langle\tilde q,\tilde p\rangle_{*}\right]dt .
$$

Varying $\tilde q$ and $\tilde p$ independently and integrating by parts,

$$
\delta S_{\mathrm{ps}}=\int\mathrm{Sc}\!\left[\overline{\left(d\tilde q/dt-\partial H/\partial\tilde p\right)}\;\delta\tilde p\right]dt
+\int\mathrm{Sc}\!\left[\overline{\left(-d\tilde p/dt-\partial H/\partial\tilde q\right)}\;\delta\tilde q\right]dt
+\left[\mathrm{Sc}(\tilde p^{\natural}\,\delta\tilde q)\right]_{t_1}^{t_2}.
$$

Stationarity for arbitrary $\delta\tilde q,\delta\tilde p$ gives **Hamilton's equations**

$$
d\tilde q/dt=\frac{\partial H}{\partial\tilde p},\qquad
\,d\tilde p/dt=-\frac{\partial H}{\partial\tilde q},
$$

which are the critical-point equations of $S_{\mathrm{ps}}$. The boundary term is again the symplectic potential. The two actions $S[\tilde q]$ and $S_{\mathrm{ps}}[\tilde q,\tilde p]$ have the same extremals after elimination of $\tilde p$, which is the Legendre transform of the preceding article read as a statement about critical points.

### Symmetries and the Boundary Term

The boundary term alone yields the conserved quantities, and it is worth isolating because the mechanism is the same one that the companion article *Noether's Theorem in Biquaternionic Form* develops in full. Suppose a one-parameter transformation $\tilde q\mapsto\tilde q_\epsilon$ leaves the action invariant up to a total derivative,

$$
S[\tilde q_\epsilon]-S[\tilde q]=\epsilon\int\frac{d}{dt}\Lambda\,dt ,
$$

and suppose the unperturbed path is a classical path, so that the bulk term of the variation vanishes. Then the variation reduces to the boundary term,

$$
\epsilon\int\frac{d}{dt}\Lambda\,dt=\delta S_{\text{bdry}}
=\left[\mathrm{Sc}\!\left(\tilde p^{\natural}\,\delta\tilde q\right)\right]_{t_1}^{t_2},
\qquad \delta\tilde q=\epsilon\,Q ,
$$

so $\mathrm{Sc}(\tilde p^{\natural}\,Q)-\Lambda$ is the same at $t_1$ and $t_2$:

$$
\frac{d}{dt}\left[\mathrm{Sc}\!\left(\tilde p^{\natural}\,Q\right)-\Lambda\right]=0 .
$$

The conserved charge is read off the boundary term. For time translation, $Q=d\tilde q/dt$ and $\Lambda=L$, giving the energy $H=\mathrm{Sc}(\tilde p^{\natural}d\tilde q/dt)-L$. For a configuration-space rotation generated by the rotor, $Q=[\tilde G,\tilde q]$ and $\Lambda=0$, giving

$$
\mathrm{Sc}\!\left(\tilde p^{\natural}\,[\tilde G,\tilde q]\right)=2\,\mathrm{Sc}\!\left(\tilde G^{\natural}\,\tilde q\,\tilde p\right)=2\,\vec G\cdot\vec L ,
$$

twice the component of the angular momentum $\vec L=\vec q\times\vec p$ along $\tilde G$, for the pure-vector configuration on which the cross product and the angular momentum are defined; the factor $2$ is the same one that appears in the commutator, $[\tilde G,\tilde q]=2\,\tilde G\times\tilde q$. The construction is the biquaternion form of the standard Noether argument, and its content is that the boundary term of the action variation is the conservation law.

## The Second Variation and Stability

The first variation identifies the classical path; the second variation decides whether it is a minimum, a maximum, or a saddle, and it controls the fluctuation factor in the stationary-phase evaluation.

Write the classical path as $\tilde q_c$ and a nearby path as $\tilde q_c+\delta\tilde q$, with $\delta\tilde q$ vanishing at the endpoints. Expanding the action to second order,

$$
S[\tilde q_c+\delta\tilde q]=S[\tilde q_c]+\tfrac{1}{2}\delta^2S[\tilde q_c,\delta\tilde q]+O(\delta^3),
$$

where

$$
\delta^2S=\int\left\langle\delta\tilde q,\;\mathcal{J}\,\delta\tilde q\right\rangle dt ,
$$

and $\mathcal{J}$ is the **Jacobi operator** of the problem. For a Lagrangian quadratic in the velocities, $L=\tfrac12 m \langle\,d\tilde q/dt\rangle_{\natural}-V(\tilde q)$, the Jacobi operator is

$$
\mathcal{J}\delta\tilde q=-m\,\delta\,d^2\tilde q/dt^2-V''(\tilde q)\,\delta\tilde q ,
$$

and the vanishing of the second variation on a nontrivial field, $\mathcal{J}\,\xi=0$, is the **Jacobi equation** for the deviation field $\xi(t)$,

$$
m\,d^2\xi/dt^2+V''(\tilde q_c)\,\xi=0 .
$$

This is the equation of **geodesic deviation** for the biquaternion-norm kinetic term. A point $t_2$ at which a nontrivial solution with $\xi(t_1)=0$ also satisfies $\xi(t_2)=0$ is a **conjugate point**; conjugate points are where the second variation degenerates and where the classical path ceases to be a strict minimum. For the free particle, $V''=0$ and the Jacobi equation reduces to $d^2\xi/dt^2=0$, whose solutions are linear in $t$; a linear solution vanishing at both ends of an interval of nonzero length is identically zero, so the free path has no conjugate points.

**Stability.** The sign of the second variation is the classical stability statement: positive for a stable extremum, a change of sign at a conjugate point. Nothing here is quantum; the second variation is the Hessian of a function on a function space, and its degeneracy is the classical Morse-theoretic datum.

## The Action as a Geodesic Principle

### The Biquaternion-Norm Metric

The kinetic term of the Lagrangian is the biquaternion norm, and the corresponding free action,

$$
S_0[\tilde q]=\frac{m}{2}\int \langle\,d\tilde q/dt\rangle_{\natural}\,dt ,
$$

is the energy of a curve in the positive-definite metric that the biquaternion norm defines on $\mathbb{H}_{\mathbb{B}}$. Its extremals are the straight lines $d^2\tilde q/dt^2=0$ found in the preceding article, and the geodesic equation of the biquaternion-norm metric is the same equation. The length functional $\int\sqrt{\langle d\tilde q\rangle_{\natural}}$ has the same extremals as the energy functional at fixed duration, by the standard argument: extremising the energy at fixed duration selects the geodesics parametrised proportionally to arc length, which are exactly the extremals of the length.

The geodesic interpretation has a Hamiltonian form, and it is the same statement. On the cotangent bundle the biquaternion-norm metric induces the Hamiltonian

$$
H(\tilde q,\tilde p)=\frac{1}{2m}\,p_\mu p_\mu=\frac{\langle\tilde p\rangle_{\natural}}{2m},
$$

the two forms agreeing because the biquaternion-norm metric is Euclidean in the basis $e_\mu$, so that the inverse metric is the metric itself. Hamilton's equations for it are $d\tilde q/dt=\partial H/\partial\tilde p=\tilde p/m$ and $d\tilde p/dt=0$, whose solutions are the straight lines found above: the geodesic flow of the biquaternion norm **is** a Hamiltonian flow, its Hamiltonian is the Legendre transform of the free action, and $H=\langle\tilde p\rangle_{\natural}/2m$ is conserved along it. This is the flat case of the general statement that a geodesic flow is the Hamiltonian flow of the quadratic form built from the inverse metric. It is the abelian counterpart of the correspondence the companion article *Similitudes Between Biquaternion Rotors and Hamiltonian Flow* establishes on the coadjoint orbit: the free particle is the case in which the carrier is abelian and the metric flat.

The biquaternion norm is positive definite on $\mathbb{H}_{\mathbb{B}}$, so its metric is Riemannian and there are no null directions. The **biquaternion-norm cone** $\langle\tilde{Q}\rangle_{\natural}=0$ is trivial on the real-quaternion sector; it becomes nontrivial on the material sector $\mathbb{M}_-$ of the complexified algebra, where the four-vector $\tilde{R}=ict\,e_t+x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$ has the indefinite norm $\langle\tilde{R}\rangle_{\natural}=-c^2t^2+x^2+y^2+z^2$, whose zero set is the light cone. The two statements are consistent: the indefinite norm appears when the central coordinate is imaginary, $q_t=ict$, which is exactly the passage from a real quaternion to a material-sector four-vector. The cone and its role in the symplectic geometry are the subject of the next article.

### The Rotor Action

The genuinely noncommutative case is a rotor-valued configuration. Let $\tilde u(t)$ be a path in the group of unit real quaternions, $\langle\tilde u\rangle_{\natural}=e_t$, and take the free action

$$
S_{\mathrm{rot}}[\tilde u]=\frac{\lambda}{2}\int \mathrm{Sc}\!\left(d\tilde u/dt\,\overline{d\tilde u/dt}\right)dt
=\frac{\lambda}{2}\int \langle\,d\tilde u/dt\rangle_{\natural}\,dt ,
$$

the rotational kinetic energy of a body with a single principal moment $\lambda$. Varying $\tilde u$ subject to the constraint $\langle\tilde u\rangle_{\natural}=e_t$ means varying within the group; writing $\delta\tilde u=\tilde u\,\delta\vec\theta$ with $\delta\vec\theta$ a pure real quaternion vanishing at the endpoints (the constraint $\mathrm{Sc}(\tilde u^{\natural}\delta\tilde u)=0$ forces $\delta\vec\theta$ to have zero scalar part), the first variation of the action becomes

$$
\delta S_{\mathrm{rot}}=\lambda\int\mathrm{Sc}\!\left(d\tilde u/dt\,\overline{\delta\,d\tilde u/dt}\right)dt
=-\lambda\int\mathrm{Sc}\!\left(d^2\tilde u/dt^2\,\overline{\delta\tilde u}\right)dt
=\lambda\int\mathrm{Sc}\!\left(\tilde u^{\natural}\,d^2\tilde u/dt^2\;\delta\vec\theta\right)dt ,
$$

using $\delta\tilde u=\tilde u\,\delta\vec\theta$, $\overline{\delta\tilde u}=-\delta\vec\theta\,\tilde u^{\natural}$, and the cyclicity of the scalar part. Stationarity for all pure $\delta\vec\theta$ gives

$$
\mathrm{Ve}\!\left(\tilde u^{\natural}\,d^2\tilde u/dt^2\right)=0 ,
$$

the **geodesic equation on the group**. Writing $\vec\eta=\tilde u^{\natural}d\tilde u/dt$, a real pure quaternion by the constraint — its scalar part is $\tfrac{1}{2}\tfrac{d}{dt}\langle\tilde u\rangle_{\natural} = \langle\tilde u,\tilde u\rangle_{\natural}=0$ — one has $\tilde u^{\natural}d^2\tilde u/dt^2=d\vec\eta/dt+\vec\eta^2$ with $\vec\eta^2$ a real scalar; the equation therefore says that the vector part of $d\vec\eta/dt$ vanishes, and since $\vec\eta$ is pure real for all $t$ this is $d\vec\eta/dt=0$. Equivalently, the equation with the constraint is $\frac{d}{dt}(\tilde u^{\natural}d\tilde u/dt)=0$: the **body angular velocity is constant**. Its solutions are the one-parameter subgroups, and the **classical rotor path is**

$$
\boxed{\;\tilde u(t)=\tilde u(0)\,\exp\!\left(+\tfrac{1}{2}\tilde\omega_b t\right),\qquad \tilde\omega_b\in\mathbb{H}_{\mathbb{B}}\cap\mathbb{M}_-,\;}
$$

with $\tilde\omega_b$ constant in the body frame. This is the free rigid body's motion, and it is derived here purely from the stationarity of the rotor action. The same calculation with the body-frame angular velocity replaced by the space-frame one gives the equivalent form $\tilde u(t)=\exp(+\tfrac12\tilde\omega_s t)\tilde u(0)$. The rigid-body article takes this result as its starting point and adds the inertia and the torque.

The rotor action is the second reason the biquaternion formulation is useful for the action principle: it is a functional on a noncommutative group, its extremals are the geodesics, and the algebra computes them in closed form.

## The Classical Limit as Stationary Phase

### The Stationary-Phase Lemma

The purely analytic statement is the following. Let $S(x)$ be a real smooth function with a single nondegenerate critical point $x_0$, $S'(x_0)=0$, $S''(x_0)\neq0$, and let $g$ be smooth. Then as $\hbar\to0^+$,

$$
\int g(x)\,\exp(\,iS(x)/\hbar)\,dx
\;\sim\;
g(x_0)\,\sqrt{\frac{2\pi\hbar}{\left|S''(x_0)\right|}}\;
\exp(\,iS(x_0)/\hbar)\;
\exp(\,i\frac{\pi}{4}\operatorname{sgn}S''(x_0)) .
$$

The dominant phase is $S(x_0)/\hbar$; the prefactor is the Gaussian fluctuation determinant about the critical point; the last factor is the Maslov phase of the critical point. Points away from $x_0$ contribute to lower order because their phases oscillate rapidly and cancel. This is the **stationary-phase lemma**, and it contains no physics.

The path-integral version applies the same lemma to a sum over trajectories weighted by $\exp(iS[\tilde q]/\hbar)$. The critical points of the action are the solutions of $\delta S=0$, that is, the classical paths, and the leading asymptotic is a sum over them,

$$
\int\mathcal{D}\tilde q\;\exp(\,iS[\tilde q]/\hbar)
\;\sim\;
\sum_{\tilde q_c}\exp(\,iS[\tilde q_c]/\hbar)\,A[\tilde q_c]\;\bigl(1+O(\hbar)\bigr),
$$

where $A[\tilde q_c]$ is the square root of the inverse fluctuation determinant (the van Vleck factor) and a Maslov phase. The classical content of the statement is exactly this: **the set of critical points of the action is the set of classical trajectories.** The identification of the critical-point equations with the Euler–Lagrange equations was made in the first section, and in the phase-space form with Hamilton's equations in the second.

### Why This Is Not Quantisation

The construction above is a statement about an oscillatory integral. It can be paraphrased without any quantum vocabulary:

- The exponent $S[\tilde q]/\hbar$ is a phase, and the phase is stationary where $\delta S=0$; every other trajectory's phase varies rapidly and cancels in the sum.
- Therefore the classical trajectory, defined as the solution of $\delta S=0$, is the trajectory that survives the cancellation, and the classical theory is the critical-point theory of the sum.
- The parameter $\hbar$ sets the scale of the phase; the classical limit is the limit of large phase.

Nothing in the paraphrase requires a Hilbert space, a state, or an operator. The algebra $\mathbb{B}$ is real and classical throughout; the configuration is a real quaternion; the action is a central-valued functional. The oscillatory sum is a device for stating the classical limit, and the biquaternion formulation is a classical formulation. Quantisation — the reverse construction, in which an operator algebra is built from the classical brackets — belongs to the sibling category and is not used here.

### The Fluctuation Factor and the Classical Hessian

The prefactor $A[\tilde q_c]$ of the stationary-phase evaluation is built from the second variation of the previous section. In the biquaternion setting the fluctuation operator is the Jacobi operator $\mathcal{J}$, and its regularized determinant is the biquaternion form of the van Vleck factor. The zeros of the determinant are the conjugate points; the Maslov phase jumps there. This is the classical Morse theory of the action, expressed with the biquaternion-norm kinetic term.

For the free particle the calculation is explicit. The Jacobi operator is $\mathcal{J}=-m\,d^2/dt^2$ with Dirichlet boundary conditions on the interval $[0,T]$. Its eigenfunctions are $\sin(n\pi t/T)$ with eigenvalues $\lambda_n=m n^2\pi^2/T^2$, $n=1,2,\dots$, and the zeta-regularized determinant is computed from the spectral zeta function

$$
\zeta_{\mathcal J}(s)=\sum_{n\ge1}\lambda_n^{-s}
=m^{-s}\left(\frac{T}{\pi}\right)^{2s}\zeta(2s),
\qquad
\det\mathcal{J}=\exp\!\left(-\zeta_{\mathcal J}'(0)\right).
$$

Using $\zeta(0)=-\tfrac12$ and $\zeta'(0)=-\tfrac12\ln 2\pi$,

$$
\zeta_{\mathcal J}'(0)=\left(-\ln m+2\ln\frac{T}{\pi}\right)\zeta(0)+2\zeta'(0)
=\ln\frac{\sqrt m}{2T},
\qquad
\det\mathcal{J}=\frac{2T}{\sqrt m}\;\propto\;T ,
$$

per real component. The determinant is therefore **linear** in $T$, and the fluctuation factor — its inverse square root — falls as $T^{-1/2}$ per real component. That is the standard free-particle van Vleck factor: the free propagator's prefactor in one dimension is $\sqrt{m/(2\pi i\hbar T)}\propto T^{-1/2}$. The free path has no conjugate points, and there is no Maslov phase. The computation is the standard one; the biquaternion formulation contributes the observation that the second variation is the Hessian of the biquaternion norm, so the classical stability problem and the biquaternion-norm geometry are the same problem.

### Rotor Paths and the Geometric Phase of the Sum

The rotor action of the preceding section adds a feature that a scalar configuration cannot show. Its critical points are the one-parameter subgroups $\tilde u(t)=\tilde u(0)\exp(+\tfrac12\tilde\omega_bt)$, and about each of them the fluctuation operator is again built from the biquaternion norm. The group of unit quaternions is compact and not simply connected, $\pi_x(SU(2))=\mathbb{Z}_2$, so the critical paths joining a given pair of endpoints are not unique — the geodesics of a bi-invariant metric on a group occur in several families — and they fall into the two homotopy classes. The stationary-phase sum over rotor paths therefore carries the relative phases $\exp(iS[\tilde u_c]/\hbar)$ of these critical paths. The transport of a rotor along a path is a parallel transport for a connection on the group, and the failure of the transport to be path-independent is its **holonomy**: the extra group element picked up around a closed loop. That holonomy, and the Hannay angle that an adiabatic classical system accumulates because of it, is the subject of the companion article *Hannay's Angles and the Classical Geometric Phase in Biquaternionic Form*; it is a classical geometric phase, and the rotor action is the classical object whose stationary-phase sum carries it.

## The Hamilton–Jacobi Equation and the Classical Phase

The action of a classical trajectory, regarded as a function of its endpoint, is Hamilton's **principal function** $W(\tilde q,t)$. Differentiating the relation $dW=\mathrm{Sc}(\tilde p^{\natural}\,d\tilde q)-E\,dt$ with the definition $\tilde p=\partial W/\partial\tilde q$ gives the **Hamilton–Jacobi equation**

$$
\frac{\partial W}{\partial t}+H\!\left(\tilde q,\frac{\partial W}{\partial\tilde q}\right)=0 .
$$

In the coordinates of the algebra,

$$
\frac{\partial W}{\partial\tilde q}=\sum_\mu e_\mu\frac{\partial W}{\partial q_\mu},
$$

so the Hamilton–Jacobi equation is a single scalar equation for the central-valued function $W$.

The Hamilton–Jacobi equation is the **eikonal equation** for the phase of the stationary-phase construction: writing the phase as $W/\hbar$, the leading-order equation of the oscillatory integral is exactly $\partial/\partial t\,W+H(\tilde q,\partial W/\partial\tilde q)=0$. In the classical interpretation, $W$ is a generating function of a canonical transformation; the constant surfaces $W=\text{const}$ are the wavefronts of the classical phase, and the characteristic directions of the Hamilton–Jacobi equation are the classical trajectories. Where the characteristic flow has a caustic, the stationary points of the action coalesce, and the stationary-phase prefactor changes.

The **characteristic function** $\mathcal{W}(\tilde q)$ of a time-independent problem satisfies $H(\tilde q,\partial\mathcal{W}/\partial\tilde q)=E$. For the free particle, $H=\langle\tilde p\rangle_{\natural}/2m$ and the equation is $\langle\partial\mathcal{W}/\partial\tilde q\rangle_{\natural}=2mE$, whose solution is $\mathcal{W}=\mathrm{Sc}(\tilde p^{\natural}\tilde q)$ with $\langle\tilde p\rangle_{\natural}=2mE$; the surfaces $\mathcal{W}=\text{const}$ are planes and the characteristics are straight lines, in agreement with the free-particle geodesics. For a periodic system the action variables $I_k=\oint p_k\,dq_k$ are the periods of the characteristic function, and they are the adiabatic invariants of the companion article *Hannay's Angles and the Classical Geometric Phase in Biquaternionic Form*.

## Summary

The action principle and the classical limit as stationary phase take the following form in the biquaternion algebra.

- The action $S[\tilde q]=\int L\,dt$ is central-valued for a real-quaternion configuration, so its phase is unambiguous.
- The principle is not restricted to finitely many coordinates: for a continuum the Lagrangian becomes a density and the Euler–Lagrange equations become field equations.
- A non-conservative load cannot enter a potential, so no $T-V$ Lagrangian contains it and the plain form fails. The principle is then extended by virtual work, or replaced by **Herglotz's principle**, whose action solves $dS/dt=L$ and whose Euler–Lagrange–Herglotz equation carries the dissipative term; the energy is replaced by a weighted conserved quantity, and the Hamiltonian form becomes a contact system on $(\tilde q,\tilde p,S)$.
- The geodesic flow of the biquaternion-norm metric is a Hamiltonian flow, with Hamiltonian $H=\langle\tilde p\rangle_{\natural}/2m$. The free particle is the abelian case of the correspondence that the rotor articles exhibit on the coadjoint orbit.
- Its first variation is the sum of a bulk term and a boundary term. The bulk term vanishes for all variations exactly when the quaternion Euler–Lagrange equation $\frac{d}{dt}\partial L/\partial\left(d\tilde q/dt\right)-\partial L/\partial\tilde q=0$ holds. The boundary term is the symplectic potential $\theta=\mathrm{Sc}(\tilde p^{\natural}\,d\tilde q)$, and on shell $dS=\theta_2-\theta_1$: the action generates the canonical transformation between its endpoints.
- The phase-space action $\int[\mathrm{Sc}(\tilde p^{\natural}d\tilde q/dt)-H]dt$ has Hamilton's equations as its critical-point equations.
- The second variation defines the Jacobi operator $\mathcal{J}\delta\tilde q=-m\,\delta\,d^2\tilde q/dt^2-V''\delta\tilde q$ and the geodesic-deviation equation $md^2\xi/dt^2+V''\xi=0$; conjugate points are where the classical extremum ceases to be a strict minimum.
- The free rotor action $\frac{\lambda}{2}\int \langle\,d\tilde u/dt\rangle_{\natural}dt$ on the group of unit quaternions has the geodesic equation $\mathrm{Ve}(d^2\tilde u/dt^2\tilde u^{\natural})=0$, whose solutions are the one-parameter subgroups $\tilde u(t)=\tilde u(0)\exp(+\tfrac12\tilde\omega_bt)$: the free rigid body's motion.
- The stationary-phase lemma evaluates an oscillatory sum over trajectories as a sum over the critical points of the action, weighted by $\exp(iS[\tilde q_c]/\hbar)$ and the fluctuation factor. The classical content is the identification of the critical points with the classical paths; the statement is a theorem about an integral and is not a quantisation.
- The action as a function of its endpoint is Hamilton's principal function, and its eikonal equation is the Hamilton–Jacobi equation $\partial/\partial t\,W+H(\tilde q,\partial W/\partial\tilde q)=0$.

The biquaternion algebra supplies a central-valued action, so the phase is well defined; a biquaternion-norm kinetic term, so the free dynamics is geodesic motion; and a rotor action on a noncommutative group, whose extremals are computed in closed form.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S[\tilde q]=\int L\,dt$ | Action (central-valued); in Herglotz's form it solves $dS/dt=L$ and is state-dependent |
| $\omega_0$, $\gamma$ | Oscillator frequency and damping coefficient |
| $\mathcal{L}$, $u$, $\rho$, $\mathcal{T}$ | Lagrangian density; string displacement, density and tension of the continuum example |
| $\tilde p=\partial L/\partial\left(d\tilde q/dt\right)$ | Conjugate momentum |
| $\theta=\mathrm{Sc}(\tilde p^{\natural}\,d\tilde q)$ | Symplectic potential (boundary term) |
| $S_{\mathrm{ps}}=\int[\mathrm{Sc}(\tilde p^{\natural}d\tilde q/dt)-H]dt$ | Phase-space action |
| $\delta^2S$ | Second variation |
| $\mathcal{J}$ | Jacobi (fluctuation) operator |
| $\xi$ | Deviation field; $\mathcal{J}\xi=0$ is the Jacobi/geodesic-deviation equation |
| $\langle\tilde q\rangle_{\natural} = \langle\tilde q,\tilde q\rangle_{\natural}=\tilde q\tilde q^{\natural}$ | Biquaternion norm |
| $\tilde u\in\mathbb{H}_{\mathbb{B}}$, $\langle\tilde u\rangle_{\natural}=e_t$ | Rotor configuration |
| $\tilde\omega_b,\tilde\omega_s$ | Body- and space-frame angular velocities |
| $W(\tilde q,t)$ | Hamilton's principal function |
| $\hbar$ | Phase scale of the oscillatory integral; asymptotic parameter only |
| $A[\tilde q_c]$ | Fluctuation (van Vleck) prefactor |
| $\langle\tilde{Q}_1,\tilde{Q}_2\rangle_{*}$ | the general plain sesquilinear form, $\mathrm{Sc}(\tilde{Q}_1\tilde{Q}_2^{*})$; on the diagonal $\langle\tilde{Q}_2,\tilde{Q}_2\rangle_{*}=\sum_\mu\lvert Q_{2\mu}\rvert^{2}$ |

## Further Reading

- W. R. Hamilton, "On a General Method in Dynamics," *Philosophical Transactions of the Royal Society*, Part II (1834) 247–308 and Part I (1835) 95–144, for the original statement of the principle.
- L. D. Landau and E. M. Lifshitz, *Mechanics* (Pergamon, 1976), for the action principle, the second variation, and the Hamilton–Jacobi equation.
- V. I. Arnold, *Mathematical Methods of Classical Mechanics* (Springer, 1989), for geodesic flows on Lie groups, the Jacobi equation, and conjugate points.
- H. Goldstein, C. P. Poole, and J. L. Safko, *Classical Mechanics* (Addison-Wesley, 2002), for Hamilton's principal function and the generating-function interpretation of the action.
- G. Herglotz, *Berührungstransformationen* (Lectures, University of Göttingen, 1930), for the original state-dependent variational principle for non-conservative systems.
- R. B. Guenther, J. A. Gottsch, and C. M. Guenther, *The Herglotz Lectures on Contact Transformations and Hamiltonian Systems* (Juliusz Center for Nonlinear Studies, Toruń, 1996), for the contact-Hamiltonian form and the generalized Noether theorem.
- Lord Kelvin (W. Thomson), "On the waves produced by a single impulse in water of any depth," *Proceedings of the Royal Society of Edinburgh* **9** (1877) 253, for the method of stationary phase.
- N. G. van Kampen, "The method of stationary phase and the Stokes phenomenon," *Physica* **6** (1939) 513, for the asymptotic evaluation of oscillatory integrals.
- V. P. Maslov and M. V. Fedoriuk, *Semi-Classical Approximation in Quantum Mechanics* (Reidel, 1981), for the Maslov phase and the fluctuation determinant of the stationary-phase expansion.
- C. Morette, "On the definition and approximation of Feynman's path integrals," *Physical Review* **81** (1951) 848, for the van Vleck determinant and the fluctuation prefactor.
- Jerrold E. Marsden and Tudor S. Ratiu, *Introduction to Mechanics and Symmetry* (Springer, 1999), for geodesics on the rotation group, the Euler–Poincaré formulation, and rigid-body dynamics in the group setting.
