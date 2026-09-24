
# __Lagrangian and Hamiltonian Systems__

## Introduction

A Lagrangian system is a mechanical system described by a function on the tangent bundle of a configuration space, and its equation is the Euler–Lagrange equation of the action integral; a Hamiltonian system is the same system described by a function on the cotangent bundle, and its equation is the first-order system defined by a symplectic form. The passage between the two descriptions is the Legendre transform, which pairs velocities with momenta, and the two pictures are equivalent whenever the transform is invertible. This article develops that equivalence and the structure of each picture: the Lagrangian mechanics, with its variational principle, its symmetries and its Noether conservation laws; the symplectic and Poisson formulation of Hamiltonian mechanics; the conservation laws of the Hamiltonian flow, among them the preservation of phase volume and the recurrence theorem; the finite-dimensional theory of complete integrability, with the Liouville–Arnold theorem, invariant tori and action-angle variables; and the classical examples — the oscillator, the pendulum, the Kepler problem, the rigid body and the geodesic flow.

The article is the finite-dimensional counterpart of the theory of integrable systems of the two preceding articles. There the integrability is that of an infinite-dimensional system, detected by a Lax pair and solved by an inverse scattering transform; here it is the integrability of a finite-dimensional Hamiltonian system, detected by a supply of independent integrals in involution and solved by quadrature, and the two theories meet in the travelling-wave reductions of the integrable equations, which are finite-dimensional Hamiltonian systems. The variational statement of the equation of the system — the Euler–Lagrange equation, the Legendre transform, the Hamilton–Jacobi equation and Noether's theorem — has been established in the article of this Part on the calculus of variations, and is used here rather than re-derived; the symplectic form and the Poisson bracket are the structures of Part I, developed in *Symplectic Forms and Poisson Brackets*, and the geometry of symplectic manifolds is the subject of Part II, written in parallel.

## Lagrangian Systems

### The Variational Principle

**Definition.** Let $Q$ be a smooth manifold, the **configuration space**, with tangent bundle $TQ$ and coordinates $(q,\dot q)$; let $L : TQ\times\mathbb{R}\to\mathbb{R}$ be a smooth **Lagrangian**, $L=L(q,\dot q,t)$. The **action** of a curve $q : [t_0,t_1]\to Q$ with fixed endpoints is

$$
S[q] = \int_{t_0}^{t_1}L(q(t),\dot q(t),t)\,dt ,
$$

and the **Euler–Lagrange equations** of $L$ are

$$
\frac{d}{dt}\frac{\partial L}{\partial\dot q^i} - \frac{\partial L}{\partial q^i} = 0, \qquad i = 1,\dots,n .
$$

**Theorem (Hamilton's principle).** A curve $q$ is a critical point of the action among curves with fixed endpoints if and only if it satisfies the Euler–Lagrange equations.

*Proof.* This is the first variation of the functional of the calculus of variations, applied to the Lagrangian $L(q,\dot q,t)$ with the roles of the independent variable $x$ and the field $u$ taken by $t$ and $q$; the derivation, the du Bois-Reymond argument and the natural boundary conditions are those of that article. $\square$

**Definition.** The system is **autonomous** if $L$ is independent of $t$. For an autonomous Lagrangian the **energy** is

$$
E = \sum_{i=1}^n\dot q^i\frac{\partial L}{\partial\dot q^i} - L ,
$$

and it is constant along every solution, by the Beltrami identity.

### The Legendre Transform and the Hamiltonian

**Definition.** The **Legendre transform** or **fibre derivative** of $L$ is the map $\mathbb{F}L : TQ\to T^*Q$ given in coordinates by

$$
(q,\dot q)\mapsto (q,p), \qquad p_i = \frac{\partial L}{\partial\dot q^i}(q,\dot q) .
$$

The Lagrangian is **regular** if $\mathbb{F}L$ is a local diffeomorphism, equivalently if the Hessian matrix $\bigl(\partial^2L/\partial\dot q^i\partial\dot q^j\bigr)$ is everywhere nonsingular; it is **hyperregular** if $\mathbb{F}L$ is a global diffeomorphism.

**Theorem (the Hamiltonian).** If $L$ is hyperregular, then the function

$$
H(q,p) = \sum_{i=1}^n p_i\dot q^i - L(q,\dot q), \qquad \dot q = (\mathbb{F}L)^{-1}(q,p) ,
$$

is well defined, and a curve $q$ satisfies the Euler–Lagrange equations of $L$ if and only if the curve $(q,p)=(\mathbb{F}L)(q,\dot q)$ satisfies **Hamilton's equations**

$$
\dot q^i = \frac{\partial H}{\partial p_i}, \qquad \dot p_i = -\frac{\partial H}{\partial q^i} .
$$

*Proof.* The Legendre transform of the calculus of variations, computed for the case in which $L$ is convex in $\dot q$; the envelope theorem gives $H_{p_i}=\dot q^i$ and $H_{q^i} = -L_{q^i}$, so that $\dot p_i = \frac{d}{dt}L_{\dot q^i}=L_{q^i}=-H_{q^i}$ along a solution. The invertibility of $\mathbb{F}L$ makes the change of variables from $(q,\dot q)$ to $(q,p)$ a diffeomorphism. $\square$

**Example (the mechanical Lagrangian).** For a Riemannian metric $g$ on $Q$ and a potential $V : Q\to\mathbb{R}$, the Lagrangian

$$
L(q,\dot q) = \frac12g_{ij}(q)\dot q^i\dot q^j - V(q)
$$

is hyperregular, with $p_i = g_{ij}\dot q^j$ and

$$
H(q,p) = \frac12g^{ij}(q)p_ip_j + V(q) ,
$$

the sum of the kinetic and potential energies. The Euler–Lagrange equation of the pure kinetic Lagrangian, $V=0$, is the geodesic equation of $g$, so a free particle on a Riemannian manifold moves along a geodesic; the metric, the Christoffel symbols and the geodesic equation are those of Part II. The corresponding Hamiltonian flow on $T^*Q$ is the geodesic flow, whose dynamical properties are treated in the article of this Part on the geodesic flow, written in parallel.

**Example (the oscillator and the pendulum).** For $Q=\mathbb{R}$ and $L=\frac12\dot q^2-\frac12\omega^2q^2$ the Hamiltonian is $H=\frac12(p^2+\omega^2q^2)$ and the flow is the linear oscillator, with the level sets $H=\text{const}$ being ellipses. For the pendulum, $L = \frac12\dot q^2+\cos q$, the Hamiltonian is $H=\frac12p^2-\cos q$; the level sets with $H<1$ are closed orbits (librations), the separatrix $H=1$ joins the unstable equilibrium at $q=\pi$, and the level sets with $H>1$ are open (rotations). The example is the first place where the topological classification of the level sets of $H$ governs the qualitative dynamics.

## Hamiltonian Systems and the Symplectic Structure

### The Symplectic Form

**Definition.** A **symplectic manifold** $(M,\omega)$ is a smooth manifold with a closed nondegenerate $2$-form $\omega$. For a function $H : M\to\mathbb{R}$, the **Hamiltonian vector field** $X_H$ is defined by

$$
\iota_{X_H}\omega = dH ,
$$

and the **Poisson bracket** of $f,g\in C^\infty(M)$ is

$$
\{f,g\} = \omega(X_f,X_g) .
$$

**Theorem (properties of the bracket).** The bracket is bilinear and skew-symmetric, satisfies the Leibniz rule $\{f,gh\}=\{f,g\}h+g\{f,h\}$, and satisfies the Jacobi identity

$$
\{f,\{g,h\}\}+\{g,\{h,f\}\}+\{h,\{f,g\}\}=0 ;
$$

consequently $C^\infty(M)$ is a Lie algebra under the bracket and the map $f\mapsto X_f$ is a Lie algebra homomorphism, $[X_f,X_g]=X_{\{f,g\}}$. The bracket is nondegenerate in the sense that $\{f,g\}=0$ for all $g$ implies that $f$ is locally constant.

*Proof.* The bilinearity, skew-symmetry and Leibniz rule follow from the corresponding properties of $\omega$ and of the differential; the Jacobi identity is the identity $d\omega=0$ written in terms of the bracket, and the homomorphism property is the computation $[X_f,X_g]=\omega$-dual of $d\{f,g\}$. The details are those of *Symplectic Forms and Poisson Brackets* and of the symplectic geometry of Part II. $\square$

**Theorem (Darboux).** Every symplectic manifold is locally symplectomorphic to $(\mathbb{R}^{2n},\sum_{i=1}^n dq^i\wedge dp_i)$: around every point there are coordinates $(q^1,\dots,q^n,p_1,\dots,p_n)$, the **canonical coordinates**, in which the form is the displayed one.

*Proof.* Quoted as standard and belonging to the symplectic geometry of Part II, written in parallel; the proof is a Moser-type argument using the closedness and nondegeneracy of $\omega$ and a homotopy of forms. $\square$

**Corollary (Hamilton's equations in canonical coordinates).** In canonical coordinates, $X_H$ has components

$$
\dot q^i = \frac{\partial H}{\partial p_i}, \qquad \dot p_i = -\frac{\partial H}{\partial q^i} ,
$$

and the Poisson bracket is

$$
\{f,g\} = \sum_{i=1}^n\left(\frac{\partial f}{\partial q^i}\frac{\partial g}{\partial p_i} - \frac{\partial f}{\partial p_i}\frac{\partial g}{\partial q^i}\right) .
$$

Moreover $\frac{d}{dt}f = \{f,H\}$ along the flow of $X_H$, so that $f$ is conserved exactly when $\{f,H\}=0$.

*Proof.* The form $\omega = \sum dq^i\wedge dp_i$ gives $\omega(X_H,Y)=dq(X_H)\,dp(Y)-dp(X_H)\,dq(Y) = \dot q\,dp(Y)+\dot p\,dq(Y)$ for $X_H=(\dot q,\dot p)$; requiring this to equal $dH(Y)=H_qdq(Y)+H_pdp(Y)$ for all $Y$ gives the equations. The bracket formula is the same computation applied to $f$ and $g$, and the last statement is $\frac{d}{dt}f = df(X_H)=X_H(f)=\{f,H\}$. $\square$

**Definition.** A **Poisson manifold** is a manifold with a bracket on its functions that is bilinear, skew-symmetric, satisfies the Leibniz rule and the Jacobi identity; the bracket need not come from a symplectic form, and its rank may drop on a subvariety. A **Poisson structure** is the corresponding section of $\Lambda^2TM$; when it is nondegenerate it is the inverse of a symplectic form.

**Remark (the two formulations).** A symplectic structure is a nondegenerate Poisson structure, and the classical mechanics of a system without constraints is symplectic; a Poisson structure that degenerates occurs for a constrained system, after symmetry reduction, and for the Lie–Poisson structure on the dual of a Lie algebra. The relation between the two is the content of the symplectic geometry of Part II, where the reduction of a symplectic manifold by a group action is treated; here the nondegenerate case is used, and the degenerate case is named only where it occurs, as in the Euler top below.

### Conservation Laws and Phase Volume

**Theorem (conservation of energy).** For an autonomous Hamiltonian $H$, the function $H$ is conserved by its own flow, $\{H,H\}=0$, and the flow preserves the symplectic form, $\mathcal{L}_{X_H}\omega=0$, and hence the volume form $\omega^n/n!$.

*Proof.* The bracket is skew, so $\{H,H\}=0$; the preservation of $\omega$ is Cartan's formula $\mathcal{L}_{X_H}\omega = d\iota_{X_H}\omega+\iota_{X_H}d\omega = d\,dH + 0 = 0$, using closedness. The volume form is a power of $\omega$, so it is preserved as well. $\square$

**Theorem (Liouville).** The flow of a Hamiltonian vector field on a symplectic manifold of dimension $2n$ preserves the measure induced by $\omega^n/n!$; consequently, on a bounded invariant set of finite measure, almost every orbit returns arbitrarily close to its starting point infinitely often (Poincaré recurrence).

*Proof.* The invariance of the volume form is the preceding theorem. For the recurrence, let $A$ be the invariant set of finite positive measure and let $U\subseteq A$ be open; the images $\phi_t(U)$ all have the same measure as $U$, so if they were pairwise disjoint their union would have infinite measure; hence $\phi_{t_1}(U)\cap\phi_{t_2}(U)\neq\emptyset$ for some $t_1<t_2$, and $\phi_{t_2-t_1}(U)\cap U\neq\emptyset$, which is recurrence. $\square$

**Theorem (Noether, Hamiltonian form).** Let a Lie group $G$ act on the symplectic manifold $(M,\omega)$ preserving $\omega$ and the Hamiltonian $H$, with infinitesimal generators $\xi_{\mathfrak{g}}$ and a momentum map $J : M\to\mathfrak{g}^*$ satisfying $d\langle J,\xi\rangle = \iota_{\xi_M}\omega$. Then $J$ is conserved along the flow of $H$: $\{J_\xi,H\}=0$ for every $\xi\in\mathfrak{g}$.

*Proof.* The invariance of $H$ under the group gives $\mathcal{L}_{\xi_M}H = 0$, i.e., $dH(\xi_M)=0$. On the other hand $dH(\xi_M)=\omega(X_H,\xi_M)$ by the definition of $X_H$, and $\omega(X_H,\xi_M)=-\omega(\xi_M,X_H)=-d\langle J,\xi\rangle(X_H)=-\{J_\xi,H\}$, because $X_{J_\xi}=\xi_M$ by the definition of the momentum map and the nondegeneracy of $\omega$. Hence the bracket vanishes. The one-parameter case is the Noether theorem of the calculus of variations, from which the statement descends. $\square$

## Complete Integrability and Action-Angle Variables

**Definition.** A Hamiltonian system $(M,\omega,H)$ with $\dim M=2n$ is **completely integrable** (in the sense of Liouville) if there exist $n$ functions $F_1=H,F_2,\dots,F_n$ on $M$ that are independent at generic points and pairwise in involution, $\{F_i,F_j\}=0$ for all $i,j$.

**Theorem (Liouville–Arnold).** Let $(M,\omega,H)$ be completely integrable and let $c$ be a regular value of $F=(F_1,\dots,F_n)$ such that the level set $M_c=F^{-1}(c)$ is compact and connected. Then:

1. $M_c$ is diffeomorphic to the $n$-torus $\mathbb{T}^n$;
2. the flow of $X_H$ is linear on $M_c$ in suitable coordinates, so the motion is **conditionally periodic** with $n$ frequencies;
3. there is a neighbourhood of $M_c$ with **action-angle coordinates** $(I,\theta)\in\mathbb{R}^n\times\mathbb{T}^n$ in which $\omega = \sum d\theta^i\wedge dI_i$ and $H = H(I)$ depends only on the actions.

*Proof.* Quoted as standard. The vector fields $X_{F_i}$ are tangent to $M_c$ because the $F_i$ are in involution; they commute, since $[X_{F_i},X_{F_j}]=X_{\{F_i,F_j\}}=0$, so they define an integrable distribution whose leaves are open subsets of $M_c$. Compactness and connectedness make each leaf a torus, giving the first assertion. The leaves are the orbits of an abelian group of translations, and the parameters along the commuting flows are the angles, giving the second. The actions are defined by integrating the $1$-forms $\iota_{X_{F_i}}\omega$ over a basis of cycles of the torus; that the integrals are locally constant in $c$ follows from the closedness of those forms, and the resulting coordinates are canonical because the cycles are Lagrangian, which gives the third assertion. $\square$

**Corollary (solution by quadrature).** In action-angle coordinates the equations of the flow are $\dot I=0$ and $\dot\theta = \omega(I) = \frac{\partial H}{\partial I}$, so $I$ is constant and $\theta(t)=\theta(0)+\omega(I)t$; the system is solved by a single integration of known functions.

**Remark (the relation to the integrable equations).** The Liouville–Arnold theorem is the finite-dimensional half of the theory of integrable systems. The travelling-wave reductions of the KdV, nonlinear Schrödinger and sine-Gordon equations — obtained by substituting a travelling-wave ansatz into the partial differential equation — are finite-dimensional Hamiltonian systems, and their integrability, where it holds, is the integrability of this theorem; the infinite-dimensional Lax pairs of the two preceding articles reduce to finite-dimensional ones on these invariant submanifolds. The theorem also delimits integrability: a generic perturbation of an integrable system destroys the invariant tori, and the Kolmogorov–Arnold–Moser theorem describes the tori of a small perturbation that survive, those whose frequency vectors are sufficiently nonresonant; the whole subject is a chapter of dynamical systems, and the articles on that subject in this Part, written in parallel, treat the stability and the destruction of the tori.

## Examples

**Example (the Kepler problem).** For a particle of unit mass in a central potential $-k/r$ in the plane, the configuration space is $\mathbb{R}^2\setminus\{0\}$ with polar coordinates, $H = \frac12(p_r^2+p_\theta^2/r^2)-k/r$, and the system is completely integrable with the commuting pair $F_1=H$ and $F_2=p_\theta$, the angular momentum. The level sets of $(H,p_\theta)$ are tori except for the separatrix of the parabolic orbit, the actions are the classical Delaunay variables, and the additional conserved vector (the Runge–Lenz vector) accounts for the further degeneracy of the frequency vector: the two frequencies of the bounded motion coincide, so the bounded orbits close and are ellipses rather than dense on a torus. The example shows that a system may have more integrals than the Liouville theorem requires, and that the extra integral is detected by a resonance of the frequency vector.

**Example (the Euler top).** The rigid body with a fixed point and no external torque has phase space the dual of the Lie algebra $\mathfrak{so}(3)$, with the Lie–Poisson structure and the Hamiltonian $H = \frac12\bigl(M_1^2/I_1+M_2^2/I_2+M_3^2/I_3\bigr)$; equivalently, in the body frame, the Euler equations $\dot M = M\times(I^{-1}M)$. The Casimir function of the Lie–Poisson structure, $\tfrac12(M_1^2+M_2^2+M_3^2)$, is conserved, and together with the energy and the component of the angular momentum along a fixed axis of space it gives three commuting integrals in the six-dimensional phase space $T^*SO(3)$, so the system is completely integrable, and the reduced level sets are the classical ellipsoids cut by the energy spheres; the free symmetric top has a further degeneracy and the motion is a regular precession. The example is the standard instance of a system whose integrability is read off a Poisson structure that is not symplectic, and whose reduction is the setting of the symplectic geometry of Part II.

**Example (the geodesic flow).** For the mechanical Lagrangian with zero potential, the Hamiltonian flow on $T^*Q$ is the geodesic flow of the metric $g$. It is the model of a Hamiltonian system whose dynamics is chaotic for a negatively curved metric — the flow on a compact quotient of the hyperbolic plane is Anosov and ergodic, as the articles of this Part on the geodesic flow and on hyperbolic dynamics record — and completely integrable for a metric with sufficiently many Killing fields. The comparison of the two cases is the classical instance of the dichotomy between integrable and chaotic Hamiltonian dynamics.

## Summary

A Lagrangian system is given by a function $L$ on the tangent bundle of a configuration space $Q$, and its motions are the critical points of the action $S[q]=\int L(q,\dot q,t)dt$, equivalently the solutions of the Euler–Lagrange equations; the momentum $p_i=\partial L/\partial\dot q^i$ defines the Legendre transform, and when the transform is invertible the system is equivalently a Hamiltonian system on the cotangent bundle with $H=\sum p_i\dot q^i-L$ and Hamilton's equations $\dot q=\partial H/\partial p$, $\dot p=-\partial H/\partial q$. The Hamiltonian formulation is the symplectic one: a symplectic manifold $(M,\omega)$, the Hamiltonian vector field defined by $\iota_{X_H}\omega=dH$, the Poisson bracket $\{f,g\}=\omega(X_f,X_g)$ with its Jacobi identity and Leibniz rule, and the local model of Darboux $\omega=\sum dq^i\wedge dp_i$; the flow preserves $\omega$ and the volume $\omega^n/n!$, which gives Liouville's theorem and Poincaré recurrence, and a symmetry of the Hamiltonian gives a conserved momentum map by Noether's theorem. A Hamiltonian system on a $2n$-dimensional manifold is completely integrable when it possesses $n$ independent integrals in involution; then, on a compact connected regular level set, the Liouville–Arnold theorem exhibits an invariant torus with linear (conditionally periodic) flow and action-angle coordinates in which $H$ depends only on the actions, so the system is solved by quadrature. The Euler top, the Kepler problem and the geodesic flow are the standard examples, and the theory is the finite-dimensional companion of the integrable systems of the preceding articles, whose travelling-wave reductions are systems of this kind.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $Q$, $TQ$, $T^*Q$ | Configuration space, tangent and cotangent bundles |
| $L(q,\dot q,t)$ | Lagrangian; $S[q]$ the action |
| Euler–Lagrange | $\frac{d}{dt}L_{\dot q^i}-L_{q^i}=0$ |
| $p_i$, $\mathbb{F}L$ | Momentum and Legendre transform |
| $H(q,p)$ | Hamiltonian, $\sum p_i\dot q^i-L$ |
| Hamilton's equations | $\dot q^i=H_{p_i}$, $\dot p_i=-H_{q^i}$ |
| $(M,\omega)$ | Symplectic manifold, closed nondegenerate $2$-form |
| $X_H$, $\iota_{X_H}\omega=dH$ | Hamiltonian vector field |
| $\{f,g\}$ | Poisson bracket, $\omega(X_f,X_g)$ |
| $g_{ij}$, $g^{ij}$ | Metric and inverse metric of $Q$ |
| momentum map $J$ | Conserved quantity associated with a symmetry |
| $F_1,\dots,F_n$ | Integrals in involution, $F_1=H$ |
| $(I,\theta)$ | Action-angle coordinates, $\omega=\sum d\theta^i\wedge dI_i$ |
| $\omega(I)$ | Frequency vector $\partial H/\partial I$ of the torus flow |
| KAM | Kolmogorov–Arnold–Moser survival of tori under perturbation |

## Further Reading

- Vladimir I. Arnold, *Mathematical Methods of Classical Mechanics* (Springer, 2nd ed. 1989), for the Lagrangian and Hamiltonian formalism, the Liouville–Arnold theorem and the examples.
- Ralph Abraham and Jerrold E. Marsden, *Foundations of Mechanics* (Benjamin/Cummings, 2nd ed. 1978), for the global symplectic formulation and the momentum map.
- Jerrold E. Marsden and Tudor S. Ratiu, *Introduction to Mechanics and Symmetry* (Springer, 2nd ed. 1999), for Poisson structures, reduction and the Lie–Poisson examples.
- Carl Gustav Jacob Jacobi, *Vorlesungen über Dynamik* (Reimer, 1866), for the Hamilton–Jacobi theory and the classical integration of Hamiltonian systems.
- Vladimir I. Arnold, Valery V. Kozlov and Anatoly I. Neishtadt, *Mathematical Aspects of Classical and Celestial Mechanics* (Springer, 3rd ed. 2006), for integrability, the KAM theorem and its consequences.
- Jürgen Moser, "On Invariant Curves of Area-Preserving Mappings of an Annulus", *Nachrichten der Akademie der Wissenschaften in Göttingen* (1962), and Vladimir I. Arnold, "Proof of a Theorem of A. N. Kolmogorov on the Preservation of Conditionally Periodic Motions", *Russian Mathematical Surveys* 18 (1963), for the KAM theorem.
- Vladimir I. Arnold, "Sur la Géométrie Différentielle des Groupes de Lie de Dimension Infinie et ses Applications à l'Hydrodynamique", *Annales de l'Institut Fourier* 16 (1966), for the Lie–Poisson framework and the Euler equations.
