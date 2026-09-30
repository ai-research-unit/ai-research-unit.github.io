# __Lie–Poisson Reduction and the Euler–Poincaré Equation__

## Introduction

A Hamiltonian system with a symmetry can be divided by the symmetry, and the quotient carries a Hamiltonian system of its own. The article *Symplectic Geometry* records the finite-dimensional case of the division, the Marsden–Weinstein quotient, in which the level set of a momentum map is taken and the group is divided out. This article treats the case in which the division is total: the phase space is the cotangent bundle of a Lie group $G$, the group acts by the lift of left translation, and the quotient is the dual of the Lie algebra, $\mathfrak g^*$. The quotient is not a cotangent bundle and carries no canonical one-form, but it does carry a Poisson structure, and that structure is the **Lie–Poisson** one of *Poisson Geometry*: the bracket $\{f,g\}(\xi)=\langle\xi,[df,dg]\rangle$ on the dual of a Lie algebra, whose symplectic leaves are the coadjoint orbits and whose Casimirs are the invariants of the coadjoint representation. The reduction from $T^*G$ to $\mathfrak g^*$ is therefore the construction that makes the Lie–Poisson bracket inevitable rather than a chosen example.

The article has two further aims. The first is the **variational** route to the same equations. The reduced dynamics can be obtained not only from the reduced Poisson structure but from the reduction of Hamilton's principle: one fixes a Lagrangian on the Lie algebra rather than on the group, varies it, and obtains a single equation on $\mathfrak g^*$, the **Euler–Poincaré equation**,
$$
\frac{d}{dt}\frac{\delta\ell}{\delta\xi}=\mathrm{ad}^*_\xi\frac{\delta\ell}{\delta\xi},
$$
whose content is that the momentum $\delta\ell/\delta\xi$ is transported by the coadjoint action of $\xi$ itself. This is the form in which the reduction is done in practice, and it is the form that survives the passage to infinite dimensions, where $G$ is a group of diffeomorphisms and the equation becomes a partial differential equation. The second aim is the **classification of the examples**: the rigid body, whose group is the rotation group; the heavy top, whose group is a semidirect product; and the ideal incompressible flow, whose group is the group of volume-preserving diffeomorphisms and whose reduced equation is the Euler equation in vorticity form. The examples are not illustrations of the theory; they are the reason the theory is stated in the form it is, because the last of them has no finite-dimensional avatar at all.

The conventions are those of the corpus. $G$ is a Lie group with Lie algebra $\mathfrak g$ and dual $\mathfrak g^*$; the bracket of $\mathfrak g$ is $[\cdot,\cdot]$, the pairing between $\mathfrak g^*$ and $\mathfrak g$ is $\langle\cdot,\cdot\rangle$, and the structure constants are those of *Lie Groups*. For $f\in C^\infty(\mathfrak g^*)$ and $\xi\in\mathfrak g^*$ the differential $df_\xi$ is an element of $\mathfrak g$, so the Lie–Poisson bracket below is defined without further structure. The **coadjoint action** is the map $\mathrm{ad}^*:\mathfrak g\times\mathfrak g^*\to\mathfrak g^*$ fixed by the convention
$$
\langle\mathrm{ad}^*_X\xi,Y\rangle=\langle\xi,[Y,X]\rangle ,
\qquad X,Y\in\mathfrak g,\ \xi\in\mathfrak g^* ,
$$
chosen so that the coadjoint action has the same orientation as the Lie–Poisson bracket of *Poisson Geometry*: with this choice the reduced equation of a Hamiltonian is $\dot\xi=\mathrm{ad}^*_{dH}\xi$, with a plus, and the Euler–Poincaré equation above likewise carries a plus. The opposite convention, $\langle\mathrm{ad}^*_X\xi,Y\rangle=\langle\xi,[X,Y]\rangle$, is equally common and reverses the sign of both equations together; **the only thing that must not be done is to mix the two**, and the convention is recorded here because every sign in the article depends on it. The symplectic form, the Hamiltonian vector field, the Poisson bracket of a symplectic manifold and the momentum map are those of *Symplectic Geometry* and *Symplectic Forms and Poisson Brackets*; the Lie algebras, their structure constants and their coadjoint orbits are those of *Lie Groups*; the reduction theorem in its general form is that of *Symplectic Geometry*.

The companion articles are:

- Companion article *Poisson Geometry*, for the Lie–Poisson bracket on the dual of a Lie algebra, its linearity, its symplectic leaves (the coadjoint orbits) and its Casimirs; the present article derives the bracket by reduction, which is the one thing that article does not do.
- Companion article *Symplectic Geometry*, for the momentum map, the Marsden–Weinstein quotient and the coadjoint orbits with their Kirillov–Kostant–Souriau form.
- Companion article *Lie Groups*, for the Lie algebra, the adjoint and coadjoint representations, the structure constants and the group of diffeomorphisms as an infinite-dimensional Lie group.
- Companion article *Lagrangian and Hamiltonian Systems*, for the Euler top as a Lie–Poisson system and for the canonical structure that the reduction destroys.
- Companion article *Symplectic Forms and Poisson Brackets*, for the alternating forms and the Poisson bracket.

## The Reduction of the Cotangent Bundle

### The Trivialisation and the Quotient

The cotangent bundle of a Lie group is trivial, and the trivialisation is the whole of the reduction. Left translation by $g$ is a diffeomorphism of $G$ and carries the cotangent bundle to itself, and composing the lifted action with the trivialisation
$$
T^*G\longrightarrow G\times\mathfrak g^* ,
\qquad
\alpha_g\longmapsto\bigl(g,\ \text{the transport of }\alpha_g\text{ to the identity}\bigr),
$$
one finds that the lifted left action is free and proper and that its orbits are the fibres of the projection to the second factor. The quotient is therefore the second factor,
$$
T^*G\big/ G\cong\mathfrak g^* ,
$$
the dual of the Lie algebra, and the quotient map is the trivialisation followed by the projection. Two facts about this quotient are worth stating at once, because together they are the reason the reduction is not a formality. First, **the quotient is not a cotangent bundle**: there is no group whose cotangent bundle is $\mathfrak g^*$ in general, and the canonical one-form of $T^*G$ does not descend, so the reduced space carries no canonical one-form and no distinguished Lagrangian submanifolds. Second, **the quotient is not symplectic**: the orbit space of a symplectic action on a symplectic manifold is in general only Poisson, and the reduced bracket on $\mathfrak g^*$ is exactly the Lie–Poisson one, whose rank varies from point to point and drops on the singular locus where the coadjoint orbit has lower dimension. The reduction therefore produces precisely the Poisson structure that *Poisson Geometry* studies, and the present section is the derivation that article assumes.

**Remark (the relation to the symplectic quotient).** The reduction above divides by the whole group and is the extreme case of the Marsden–Weinstein construction of *Symplectic Geometry*. There, one action is used to reduce by taking a level set of its momentum map and dividing by the group; here, the cotangent bundle is divided by the lifted action directly, and the two are related by the general reduction theorem for cotangent bundles: the reduced space is a quotient of $\mathfrak g^*$ by the residual symmetry, and the symplectic leaves of the reduced structure are the coadjoint orbits. The two operations therefore agree on the fibres: the Marsden–Weinstein quotient of a level set of the momentum map recovers a coadjoint orbit with its Kirillov–Kostant–Souriau form, and the Lie–Poisson structure is the single Poisson structure whose leaves those orbits are.

### The Reduced Bracket

The bracket on $\mathfrak g^*$ produced by the reduction has a closed form, and it is the definition of the Lie–Poisson structure. For $f,g\in C^\infty(\mathfrak g^*)$ and $\xi\in\mathfrak g^*$,
$$
\{f,g\}(\xi)=\bigl\langle\xi,\,[df_\xi,dg_\xi]\bigr\rangle ,
$$
where $df_\xi$ and $dg_\xi$ are read as elements of $\mathfrak g$ through the pairing. In linear coordinates, $\{x_i,x_j\}=\sum_kc^k_{ij}x_k$ with $c^k_{ij}$ the structure constants of $\mathfrak g$; the bracket is therefore **linear**, that is, the bracket of two linear functions is again linear, and a linear Poisson structure on a vector space is the same thing as a Lie algebra structure on its dual. This is the reason the reduction lands on a *linear* structure: the quotient of $T^*G$ by the lift of left translation is a vector space, and its Poisson tensor has no quadratic terms.

Three properties are inherited rather than imposed. **The Jacobi identity** holds because it is the Jacobi identity of $\mathfrak g$; the reduction produces a Poisson structure for free. **Antisymmetry** holds because the bracket of $\mathfrak g$ is antisymmetric. And the **rank** at a point is the codimension of its coadjoint orbit, so the structure is symplectic exactly where the coadjoint orbit is open, that is, on the union of the orbits of maximal dimension. The reduction to $\mathfrak g^*$ therefore does not merely produce a Poisson manifold; it produces the manifold whose leaves are the objects that the orbit method of *Lie Groups* is about.

The choice of left trivialisation above is a choice, and the opposite choice reverses the sign of the bracket. The corpus records the two signs in two articles because they arise in two places: the bracket of *Poisson Geometry* is the one written above, and the Euler top of *Lagrangian and Hamiltonian Systems* is written with the opposite sign, $\dot M=M\times(I^{-1}M)$ rather than $\dot M=I^{-1}M\times M$. The two articles are not in conflict; they differ by the side on which the covector is transported to the identity, and a reader who changes sides must change the bracket and the reduced equation together, as the convention paragraph above states.

## Lie–Poisson Dynamics

### The Reduced Equation

The Hamiltonian of the reduced system is the reduction of the Hamiltonian of the system on $T^*G$: a function $H$ on the un-reduced phase space that is invariant under the lifted action descends to $T^*G/G\cong\mathfrak g^*$. Since the reduced structure is Poisson, the dynamics is read from it directly, and for any $f\in C^\infty(\mathfrak g^*)$,
$$
\dot f=\{f,H\},
$$
which is the same formula as in the finite-dimensional Hamiltonian theory of *Lagrangian and Hamiltonian Systems* and is the sense in which the reduction preserves the form of the equations. Written on the momentum itself, the equation is
$$
\dot\xi=\mathrm{ad}^*_{dH_\xi}\xi ,
$$
the **Lie–Poisson equation**: the momentum is transported by the coadjoint action of the differential of the Hamiltonian. With the convention of the introduction the equation carries a plus; the equivalent reading $\frac{d}{dt}\langle\xi,X\rangle=\langle\xi,[X,dH]\rangle$, valid for every $X\in\mathfrak g$, is the one to use when the sign is in doubt, since it depends only on the bracket of $\mathfrak g$ and on the pairing.

The finite-dimensional case is the rotation group. For $\mathfrak g=\mathfrak{so}(3)$ with the bracket of the wedge product and the pairing the Euclidean one, the dual is $\mathbb{R}^3$ and the Lie–Poisson bracket on linear coordinates is
$$
\{x,y\}=z,\qquad \{y,z\}=x,\qquad \{z,x\}=y ,
$$
the structure constants of $\mathfrak{so}(3)$; the Casimir is $x^2+y^2+z^2$, whose level sets are the spheres, and the symplectic leaves are the concentric spheres and the origin. With the Hamiltonian $H=\frac12(M_1^2/I_1+M_2^2/I_2+M_3^2/I_3)$ of a rigid body with moments of inertia $I$, the Lie–Poisson equation is
$$
\dot M=\mathrm{ad}^*_{I^{-1}M}M=I^{-1}M\times M ,
$$
the **Euler top**, whose integrals are the energy and the Casimir and whose level sets are the intersections of the energy ellipsoids with the momentum spheres of *Lagrangian and Hamiltonian Systems*.

**Verification.** With $\mu=(0.8,-0.5,0.3)$, $I=(1,2,3)$ and the derivatives evaluated by central differences of step $10^{-6}$, the antisymmetry of the bracket was exact, the Jacobi sum over a list of eight polynomial functions was at most $6.5\times10^{-11}$, and the bracket of the Casimir $\frac12\lVert M\rVert^2$ with each of them was at most $3.6\times10^{-11}$; the residuals are the discretisation error of the derivative. The reduced equation gave $\dot M=(-0.0250000000,-0.1600000000,-0.2000000000)$, which is $I^{-1}M\times M$ to the last digit, and the same vector is $M\times I^{-1}M$ with the opposite overall sign, that is, with the opposite choice of trivialisation.

### Casimirs, Orbits and the Invariant Functions

The functions that the Lie–Poisson bracket annihilates are the invariants of the coadjoint representation, since $\{f,g\}=0$ for every $g$ exactly when $df$ is annihilated by the coadjoint action of every element, and these are the **Casimirs**. They are constant on the coadjoint orbits, they are the functions that the reduction inherits from the invariants of the lifted action on $T^*G$, and they are the reason the reduction loses information: the reduced phase space is foliated by the orbits, and a Casimir does not determine the dynamics, only the leaf. For $\mathfrak{so}(3)$ the Casimir is $\frac12\lVert M\rVert^2$, the square of angular momentum; for a semidirect product there are generally fewer Casimirs than the dimension of the generic orbit, and the classification of Lie–Poisson structures by their Casimirs is the classification of the coadjoint orbits, which is a hard problem in general and is what makes the examples interesting. In the reduction picture the Casimirs are the momentum-map values that survive: the invariants of the lifted action on $T^*G$ are exactly the pullbacks of the Casimirs under the quotient map, so the statement that a Casimir is conserved is the statement that the corresponding symmetry is present in the un-reduced system.

## The Euler–Poincaré Equation

### Reduction of the Variational Principle

The same reduced equations can be obtained without writing a Poisson structure at all, and the variational route is the one that extends to infinite dimensions. Let $\ell:\mathfrak g\to\mathbb R$ be a Lagrangian on the Lie algebra, let $g(t)$ be a curve in $G$ with $\xi(t)=g(t)^{-1}\dot g(t)\in\mathfrak g$ the **left-trivialised velocity**, and let the action be
$$
\mathcal S[g]=\int_a^b\ell\bigl(\xi(t)\bigr)dt .
$$
The Lagrangian is left-invariant by construction, since the velocity was trivialised on the left. The variation of the curve induces a variation of $\xi$ of the form
$$
\delta\xi=\dot\eta+[\xi,\eta],\qquad \eta=\text{the trivialised variation},
$$
with the bracket of $\mathfrak g$ in the second term, and the vanishing of the first variation of $\mathcal S$ for every $\eta$ vanishing at the endpoints gives Hamilton's principle in the reduced variables,
$$
\delta\mathcal S=\int_a^b\Bigl\langle\frac{\delta\ell}{\delta\xi},\ \dot\eta+[\xi,\eta]\Bigr\rangle dt=0
\qquad\text{for all }\eta .
$$
Integrating the first term by parts and using the definition of the coadjoint action,
$$
\Bigl\langle\frac{\delta\ell}{\delta\xi},\,[\xi,\eta]\Bigr\rangle=\Bigl\langle\mathrm{ad}^*_\xi\frac{\delta\ell}{\delta\xi},\ \eta\Bigr\rangle ,
$$
the boundary term vanishes and the fundamental lemma gives the **Euler–Poincaré equation**
$$
\boxed{\;\frac{d}{dt}\frac{\delta\ell}{\delta\xi}=\mathrm{ad}^*_\xi\frac{\delta\ell}{\delta\xi}.\;}
$$
Two features of the derivation are the content of the equation. First, **the momentum is transported by the coadjoint action of the velocity itself**, so the equation is nonlinear in the velocity and is not the statement that momentum is constant; the reduction of a symmetry does not produce a conserved momentum, it produces a momentum that moves under the coadjoint action. Second, **the equation is a single equation on $\mathfrak g^*$**, not a pair on $T^*G$: the configuration variable $g$ has been eliminated, and it is recovered afterwards by solving the reconstruction equation $\dot g=g\xi$, which is linear in $g$ once $\xi$ is known. The reduction has hence removed the group and kept the algebra, at the price of a nonlinear equation and the loss of the canonical structure.

When $\ell$ is the kinetic energy of a left-invariant Riemannian metric on $G$, the Euler–Poincaré equation is the equation of the geodesics of that metric, and the rigid body, the heavy top and the incompressible flow are the three standard cases: the geodesic equation of a left-invariant metric on $SO(3)$, of a left-invariant metric plus a potential on a semidirect product, and of the right-invariant $L^2$ metric on the volume-preserving diffeomorphism group. This is the sense in which the Lie–Poisson reduction is the Hamiltonian side of a statement in Riemannian geometry: the reduced dynamics of a left-invariant kinetic energy is the geodesic flow of a metric, read on the dual of the Lie algebra.

### The Rigid Body

The finite-dimensional case is fully explicit. Let $G=SO(3)$ with the Lie algebra $\mathfrak{so}(3)\cong\mathbb{R}^3$ under the wedge product, let $I$ be a positive definite symmetric matrix — the inertia tensor — and let
$$
\ell(\Omega)=\frac12\langle I\Omega,\Omega\rangle
$$
be the kinetic energy of a body rotating with body angular velocity $\Omega$. The momentum conjugate to $\Omega$ is $M=I\Omega$, and the Euler–Poincaré equation becomes
$$
\dot M=\mathrm{ad}^*_\Omega M=-M\times\Omega ,
$$
which with $M=I\Omega$ is $\dot M=I^{-1}M\times M$, the Euler top of the preceding section. The two routes to it — the Lie–Poisson bracket of the reduced phase space and the Euler–Poincaré equation of the reduced Lagrangian — give the same equation, as they must: the first is the Hamiltonian form of the second, and the Legendre transform between them is the map $\Omega\mapsto M=I\Omega$. The derivation from the variational principle also shows why the equation is quadratic in $M$: the coadjoint action is bilinear, and the quadratic term is the curvature of the group, not an approximation.

**Verification.** With $M=(0.8,-0.5,0.3)$ and $I=\mathrm{diag}(1,2,3)$ so that $\Omega=(0.8,-0.25,0.1)$, the right-hand side of the Euler–Poincaré equation computed as $-M\times\Omega$ was $(-0.0250000000,-0.1600000000,-0.2000000000)$, identical to the value of $\{M,H\}$ obtained from the Lie–Poisson bracket of the preceding section by numerical differentiation. The two derivations therefore agree algebraically, which is the point of the check: a sign error in the coadjoint convention changes the sign of one of them and not the other.

### The Semidirect Product and the Heavy Top

A rigid body moving under an external field is not a left-invariant system on a group, but it becomes one on a **semidirect product**. Let $V$ be a representation of $G$, let $\mathfrak g\ltimes V$ be the semidirect product Lie algebra with the bracket
$$
\bigl[(X,u),(Y,v)\bigr]=\bigl([X,Y],\,X\cdot v-Y\cdot u\bigr),
$$
and let $\ell:\mathfrak g\times V\to\mathbb R$ be a Lagrangian on the semidirect product. The Euler–Poincaré equation on a semidirect product carries an extra term, because the dual of the semidirect product also pairs the $V$-slot with the $\mathfrak g^*$-slot; the result is the **Euler–Poincaré equation with a semidirect product**, whose reduced Poisson structure is the semidirect-product Lie–Poisson bracket
$$
\{f,g\}=\bigl\langle\xi,[df_\xi,dg_\xi]\bigr\rangle-\Bigl\langle v,\,df_\xi\cdot dg_v-dg_\xi\cdot df_v\Bigr\rangle ,
$$
with $\xi\in\mathfrak g^*$, $v\in V^*$. For $G=SO(3)$, $V=\mathbb{R}^3$ and the Hamiltonian $\frac12\langle I^{-1}M,M\rangle+\langle\Gamma,\chi\rangle$ for a fixed vector $\chi$, the system is the **heavy top**, and the reduced equation is the Euler–Poincaré equation with the extra term $\Gamma\times\chi$; the bracket has two Casimirs, $\lVert\Gamma\rVert^2$ and $\langle M,\Gamma\rangle$, whose joint level sets are the coadjoint orbits, and the reduced phase space is foliated by them rather than by spheres. The semidirect product is the mechanism by which an external structure is restored to the left-invariant setting, and it is the reason the heavy top is a Lie–Poisson system in the same sense as the rigid body, with a bracket that is linear but not of the purely algebraic form.

### The Diffeomorphism Group and the Ideal Flow

The infinite-dimensional case is the one that justifies the theory. Let $D$ be a bounded region of $\mathbb{R}^n$ and let $G=\mathrm{Diff}_\mu(D)$ be the group of volume-preserving diffeomorphisms of $D$, an infinite-dimensional Lie group whose Lie algebra is the space of divergence-free vector fields tangent to the boundary, with the negative of the Lie bracket of vector fields as its own bracket; the dual $\mathfrak g^*$ is the space of one-forms modulo exact forms, that is, the space of **vorticities**. The group acts on itself by composition, the kinetic energy of an incompressible flow,
$$
\ell(u)=\frac12\int_D\lVert u\rVert^2\,dx ,
$$
is right-invariant under the action, and the Euler–Poincaré equation becomes
$$
\frac{\partial u}{\partial t}+(u\cdot\nabla)u=-\nabla p,\qquad \mathrm{div}\,u=0 ,
$$
the **Euler equation of an ideal incompressible flow**, with the pressure $p$ the Lagrange multiplier of the constraint $\mathrm{div}\,u=0$. Written on the vorticity, the same equation is an equation on the dual of the Lie algebra, and the reduced Poisson structure is the Lie–Poisson structure of $\mathfrak g^*$: it is the **vorticity bracket**
$$
\{F,G\}(\omega)=\int_D\omega\,\Bigl[\frac{\delta F}{\delta\omega},\frac{\delta G}{\delta\omega}\Bigr]\,dx ,
\qquad [f,g]=\partial_xf\,\partial_yg-\partial_yf\,\partial_xg
$$
in the plane, with the Hamiltonian the kinetic energy $\frac12\int\lVert\nabla\psi\rVert^2$, where $\psi$ is the stream function of the flow. The equation of motion is the Euler equation in vorticity form, $\dot\omega=\{\psi,\omega\}$ up to the sign convention of the orientation of $\nabla^\perp$, and the enstrophy $\frac12\int\omega^2$ is a Casimir, hence conserved for every Hamiltonian and not only for the kinetic energy. This is the infinite-dimensional content of the theory: **the reduced phase space of a fluid is the dual of a Lie algebra, its bracket is a Lie–Poisson bracket, and the Casimirs are the invariants of the coadjoint action.** None of the three has a finite-dimensional analogue, and it was this case that made the Lie–Poisson formalism necessary rather than a reformulation of Hamiltonian mechanics.

**Verification.** For the two-dimensional vorticity bracket with $\omega=\sin(x+0.3)\cos(0.7y-0.2)+\frac12\sin(0.4x+0.9)\sin(1.1y)$ and the stream function the corresponding solution of the Poisson equation on the torus, the identity that converts the vorticity equation into divergence form, $\partial_x(\omega\,\psi_y)-\partial_y(\omega\,\psi_x)=\{\omega,\psi\}$, held to $2.8\times10^{-10}$ at $(0.37,-0.21)$, the residual being the second-order error of the numerical derivatives; the bracket of the enstrophy with a test function, $\int_{\mathbb{T}^2}\{\omega^2,h\}\,dx$, evaluated by the trapezoidal rule on a $40\times40$ grid over the torus, was $8.8\times10^{-12}$, that is, zero to the accuracy of the quadrature. The two checks verify the two claims of the paragraph: the divergence form and the Casimir property. Enstrophy is a Casimir of the vorticity bracket, and the identity is the reason the vorticity equation can be written in conservation form at all.

## Summary

The reduction of the cotangent bundle of a Lie group by the lift of left translation is total: the quotient is the dual of the Lie algebra, $T^*G/G\cong\mathfrak g^*$, and it carries the **Lie–Poisson** structure $\{f,g\}(\xi)=\langle\xi,[df,dg]\rangle$, whose Jacobi identity is that of $\mathfrak g$, whose rank at a point is the codimension of its coadjoint orbit, and whose Casimirs are the invariants of the coadjoint representation. The quotient is not a cotangent bundle and not symplectic; it is the Poisson manifold of *Poisson Geometry*, and its symplectic leaves are the coadjoint orbits with their Kirillov–Kostant–Souriau form. The dynamics is $\dot f=\{f,H\}$, equivalently $\dot\xi=\mathrm{ad}^*_{dH}\xi$, with the coadjoint convention of the introduction; for the rotation group and the rigid-body Hamiltonian the equation is the Euler top, $\dot M=I^{-1}M\times M$.

The variational route to the same equation is the **Euler–Poincaré equation** $\frac{d}{dt}\frac{\delta\ell}{\delta\xi}=\mathrm{ad}^*_\xi\frac{\delta\ell}{\delta\xi}$, obtained by reducing Hamilton's principle to a Lagrangian on the Lie algebra; the momentum is transported by the coadjoint action of the velocity, the configuration variable is eliminated and recovered by reconstruction, and when the Lagrangian is a left-invariant kinetic energy the equation is the geodesic equation of the corresponding left-invariant metric. The three examples are the rigid body, the heavy top on a semidirect product — whose bracket and Euler–Poincaré equation carry an extra term and whose Casimirs are $\lVert\Gamma\rVert^2$ and $\langle M,\Gamma\rangle$ — and the volume-preserving diffeomorphism group, whose reduced bracket is the vorticity bracket, whose equation is the Euler equation of an ideal incompressible flow, and whose enstrophy Casimir makes the vorticity equation conservational. The last example has no finite-dimensional analogue, and the semidirect-product device is what restores an external structure to the left-invariant setting.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $G$, $\mathfrak g$, $\mathfrak g^*$, $[\cdot,\cdot]$, $\langle\cdot,\cdot\rangle$ | Lie group, Lie algebra, its dual, the bracket and the pairing |
| $T^*G$, $\alpha_g$ | The cotangent bundle and a covector at $g$; the lifted left action trivialises it as $G\times\mathfrak g^*$ |
| $T^*G/G\cong\mathfrak g^*$ | The reduction: the quotient by the lifted left action is the dual of the Lie algebra |
| $\{f,g\}(\xi)=\langle\xi,[df_\xi,dg_\xi]\rangle$ | The Lie–Poisson bracket on $\mathfrak g^*$; linear, with $\{x_i,x_j\}=\sum_kc^k_{ij}x_k$ |
| $\mathrm{ad}^*_X\xi$, $\langle\mathrm{ad}^*_X\xi,Y\rangle=\langle\xi,[Y,X]\rangle$ | The coadjoint action, with the convention of the introduction |
| $\dot\xi=\mathrm{ad}^*_{dH}\xi$, $\dot f=\{f,H\}$ | The Lie–Poisson equation of a Hamiltonian |
| Casimir | A function annihilated by the bracket; an invariant of the coadjoint representation; constant on the coadjoint orbits |
| $\ell:\mathfrak g\to\mathbb R$, $\xi=g^{-1}\dot g$ | A Lagrangian on the Lie algebra and the left-trivialised velocity of a curve in $G$ |
| $\frac{d}{dt}\frac{\delta\ell}{\delta\xi}=\mathrm{ad}^*_\xi\frac{\delta\ell}{\delta\xi}$ | The Euler–Poincaré equation |
| $\ell(\Omega)=\frac12\langle I\Omega,\Omega\rangle$, $M=I\Omega$ | The rigid body: kinetic energy on $\mathfrak{so}(3)$ and its momentum; $\dot M=-M\times\Omega$ |
| $[(X,u),(Y,v)]=([X,Y],X\cdot v-Y\cdot u)$ | The semidirect product bracket; its Lie–Poisson bracket has an extra term, and the heavy top is the example |
| $\mathrm{Diff}_\mu(D)$, $\mathfrak g^*$ | The volume-preserving diffeomorphism group and the space of vorticities |
| $\{F,G\}(\omega)=\int_D\omega\,[\delta F,\delta G]\,dx$ | The vorticity bracket; its Casimir is the enstrophy $\frac12\int\omega^2$ |
| $\frac{\partial u}{\partial t}+(u\cdot\nabla)u=-\nabla p$, $\mathrm{div}\,u=0$ | The Euler equation of an ideal incompressible flow, the Euler–Poincaré equation of $\mathrm{Diff}_\mu(D)$ |

## Further Reading

- Vladimir I. Arnold, "Sur la géométrie différentielle des groupes de Lie de dimension infinie et ses applications à l'hydrodynamique", *Annales de l'Institut Fourier* **16** (1966), and *Mathematical Methods of Classical Mechanics* (2nd ed., Springer, 1989), for the reduction of the cotangent bundle, the Euler–Poincaré equation and the geodesic interpretation of the rigid body.
- Vladimir I. Arnold and Boris A. Khesin, *Topological Methods in Hydrodynamics* (Springer, 1998), for the volume-preserving diffeomorphism group, the vorticity bracket and the Casimirs of the Euler equation.
- Jerrold E. Marsden and Tudor S. Ratiu, *Introduction to Mechanics and Symmetry* (2nd ed., Springer, 1999), for the reduction theorems, the Euler–Poincaré equation, the semidirect product and the heavy top.
- Jerrold E. Marsden and Alan Weinstein, "Reduction of symplectic manifolds with symmetry", *Reports on Mathematical Physics* **5** (1974), for the symplectic quotient that the reduction of the cotangent bundle generalises.
- Alexandre Kirillov, *Lectures on the Orbit Method* (American Mathematical Society, 2004), for the coadjoint orbits, the Kirillov–Kostant–Souriau form and the invariants of the coadjoint representation.
- John E. Marsden, Tudor S. Ratiu and Juan-Pablo Ortega, *Hamiltonian Reduction by Stages* (Springer, 2007), for the semidirect-product reduction and the heavy top in the reduction framework.
- Darryl D. Holm, Jerrold E. Marsden and Tudor S. Ratiu, "The Euler–Poincaré equations and semidirect products with applications to continuum theories", *Advances in Mathematics* **137** (1998), for the Euler–Poincaré equation with a semidirect product and its applications.
- *Poisson Geometry* (`articles_maths/poisson-geometry.md`), companion article, for the Lie–Poisson bracket, its linearity, its symplectic leaves and its Casimirs.
- *Symplectic Geometry* (`articles_maths/symplectic-geometry.md`), companion article, for the momentum map, the Marsden–Weinstein quotient and the coadjoint orbits.
- *Lie Groups* (`articles_maths/lie-groups.md`), companion article, for the adjoint and coadjoint representations, the structure constants and the diffeomorphism group as a Lie group.
- *Lagrangian and Hamiltonian Systems* (`articles_maths/lagrangian-and-hamiltonian-systems.md`), companion article, for the Euler top and the canonical structure that the reduction destroys.
