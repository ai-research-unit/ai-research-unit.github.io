# __Spin-1 Condensates and the Spinor Order Parameter in Biquaternionic Form__

## Introduction

A spin-one Bose–Einstein condensate is the physical system in which the three-level structure of the preceding articles is realised as matter. Atoms whose ground state carries hyperfine angular momentum one — sodium-23 and rubidium-87 are the standard examples — condense into a single macroscopic wave function that has three internal components, one for each value of the spin projection. The order parameter is therefore a three-component complex spinor, and its symmetry, its ground states, its defects and its response to fields are all consequences of the spin-one algebra acting on that spinor.

The purpose of this article is to describe that order parameter in the framework. Three things are established. First, the spinor is not an alien object: it is a vector in the symmetric square of the defining module, so the framework's own construction of the qutrit, through the two-factor algebra $\mathbb{B}\otimes_\mathbb{C}\mathbb{B}$, is exactly the construction of a spin-1 condensate's internal state space, and the spinor's three components are the three independent components of a symmetric two-fundamental amplitude. Second, the two order parameters that the standard theory distinguishes — the magnetic (vector) order $\langle\mathbf F\rangle$ and the nematic order — are the expectations of the framework's linear and quadratic operators, that is, of the adjoint action and of the rank-two tensor operator; their being the only two invariants is the statement that for spin one the first two moments exhaust the algebraically independent information. Third, the two standard ground-state families have a transparent algebraic form: the ferromagnetic states are the symmetrised products of two *identical* fundamental idempotents, and the polar (nematic) states are the symmetrised products of two *antipodal* ones. The magnetic phase is the phase in which the two constituent fundamental spins point the same way; the nematic phase is the phase in which they point opposite ways.

The article is organised as follows. The standard mean-field theory of the spin-one condensate is recapitulated: the order parameter, the symmetry group, the interaction energy, the phase diagram and the order-parameter manifolds. The spinor is then embedded in the framework, and the two order parameters are expressed in its terms, with the invariants written in Bloch coordinates. The ferromagnetic and polar families are built from idempotents of the two-factor algebra. The energy functional is then rewritten in the framework's coordinates, the symmetries and the topological defects are classified in the framework's terms, and a closing section separates what the algebra determines from what is imported from the standard theory.

## The Spin-One Condensate: Mean-Field Theory

### The spinor order parameter

The condensate is described by a macroscopic wave function with three internal components,

$$
\Psi(\mathbf r)=\sqrt{n(\mathbf r)}\,e^{i\theta(\mathbf r)}\,
\boldsymbol\zeta(\mathbf r),\qquad
\boldsymbol\zeta=\begin{pmatrix}\zeta_+\\ \zeta_0\\ \zeta_-\end{pmatrix},\qquad
\boldsymbol\zeta^{\dagger}\boldsymbol\zeta=1 ,
$$

where $n$ is the density, $\theta$ the global phase, and $\boldsymbol\zeta$ the *spinor order parameter*, a unit vector in $\mathbb{C}^3$ whose components multiply the states of spin projection $m=+1,0,-1$ along the quantisation axis. The spin operators are the dimensionless three-dimensional matrices

$$
F_x=\frac{1}{\sqrt2}\begin{pmatrix}0&1&0\\1&0&1\\0&1&0\end{pmatrix},\quad
F_y=\frac{i}{\sqrt2}\begin{pmatrix}0&-1&0\\1&0&-1\\0&1&0\end{pmatrix},\quad
F_z=\begin{pmatrix}1&0&0\\0&0&0\\0&0&-1\end{pmatrix},
$$

satisfying $[F_i,F_j]=i\epsilon_{ijk}F_k$ and $\mathbf F^2=2I_3$, the spin-one commutation relations and Casimir. In these units the eigenvalues of $F_z$ are $+1,0,-1$, and the vector expectation

$$
\langle\mathbf F\rangle=\boldsymbol\zeta^{\dagger}\mathbf F\,\boldsymbol\zeta
$$

is the magnetic order parameter, a real three-vector with $|\langle\mathbf F\rangle|\le1$. The atomic Hamiltonian is invariant under the three-parameter family of transformations

$$
\boldsymbol\zeta\;\longmapsto\;e^{i\alpha}\,e^{-i\beta\,\hat{\mathbf n}\cdot\mathbf F}\,\boldsymbol\zeta ,
\qquad \alpha\in\mathbb{R},\quad \beta\in\mathbb{R},\quad \hat{\mathbf n}\in S^2 ,
$$

that is, under $G=U(1)_{\mathrm{phase}}\times SU(2)_{\mathrm{spin}}$; the two factors commute, because the first is a phase on all three components and the second rotates them among themselves. This symmetry, and its breaking in the ground state, organises everything that follows.

### The interaction energy and the phase diagram

For a dilute gas in a uniform field the mean-field energy density of the condensate is, in the standard treatment,

$$
\mathcal{E}=\frac{\hbar^2}{2m}\lvert\nabla\Psi\rvert^2+Vn+\frac{c_0}{2}n^2+\frac{c_2}{2}n^2\,\lvert\langle\mathbf F\rangle\rvert^2
+p\,\langle F_z\rangle+q\,\langle F_z^2\rangle ,
$$

with the spin-independent and spin-dependent contact couplings

$$
c_0=\frac{4\pi\hbar^2}{3m}\left(2a_2+a_0\right),
\qquad
c_2=\frac{4\pi\hbar^2}{3m}\left(a_2-a_0\right),
$$

built from the two-body scattering lengths $a_0$ and $a_2$ in the total-spin-zero and total-spin-two channels, and with the linear and quadratic Zeeman terms $p\propto B$ and $q\propto B^2$. This energy is the standard mean-field functional of the spin-one condensate, and the following consequences of it are likewise standard.

The fourth term is the only place where the direction of the spinor enters the interaction energy, and it depends on the spinor *only* through the single invariant $\lvert\langle\mathbf F\rangle\rvert^2$. A spinor that minimises it at fixed density will therefore maximise or minimise the magnetic order according to the sign of $c_2$, and a simple calculation of $\lvert\langle\mathbf F\rangle\rvert^2$ over the unit spinors shows that its range is $[0,1]$, with the extreme values attained on the following families:

$$
\lvert\langle\mathbf F\rangle\rvert=1:\quad
\boldsymbol\zeta\propto e^{-i\beta\,\hat{\mathbf n}\cdot\mathbf F}\begin{pmatrix}1\\0\\0\end{pmatrix},
\qquad
\lvert\langle\mathbf F\rangle\rvert=0:\quad
\boldsymbol\zeta\propto e^{-i\beta\,\hat{\mathbf n}\cdot\mathbf F}\begin{pmatrix}0\\1\\0\end{pmatrix}.
$$

The first family is a rotation of the fully stretched state: it is the family of **spin-one coherent states**, and each member has a definite spin direction, $\langle\mathbf F\rangle=\hat{\mathbf n}$ (up to the sign conventions of the rotation). The second is a rotation of the $m=0$ state: each member has vanishing magnetic moment in every direction, $\langle\mathbf F\rangle=0$. A state of the second family carries nematic order — it distinguishes an axis, but not a direction along it.

The phase diagram at $p=0$ follows. For $c_2<0$ the interaction favours a large $\lvert\langle\mathbf F\rangle\rvert$ and the ground state is **ferromagnetic**: at $q=0$ the spinor locks onto a common direction, and a positive $q$ tilts the magnetisation into the plane perpendicular to the field and reduces its magnitude, the order surviving up to $q=2\lvert c_2\rvert n^2$, above which the polar state takes over. For $c_2>0$ the interaction favours $\langle\mathbf F\rangle=0$, and the ground state is **polar** (also called nematic) for $q>0$ and **broken-axisymmetric** for $q<0$: the quadratic Zeeman term orients the director, along the field axis for $q>0$, where the state is the $\hat z$-directed nematic spinor, and in the plane perpendicular to the field for $q<0$, where the spinor is a superposition of $m=\pm1$. The two are the extreme values $\langle F_z^2\rangle=0$ and $\langle F_z^2\rangle=1$ of the alignment invariant, and the broken-axisymmetric state has the additional freedom of the relative phase of its two $m=\pm1$ amplitudes, which the $q>0$ state does not have; that free relative phase is the sense in which the axisymmetry about the field is broken.

Two invariants therefore suffice for the uniform ground-state problem: $\lvert\langle\mathbf F\rangle\rvert^2$, which measures the magnetic order and is the expectation of a quadratic expression in the spin operators, and $\langle F_z^2\rangle$, which measures the alignment of the state with the field axis and is also quadratic in the spin operators. This is the fact that the framework's operator content explains, and the next sections make it explicit.

## The Spinor as a Vector in the Symmetric Sector

### The spinor components in the two-factor basis

The three-component spinor is a vector in the symmetric square of the two-dimensional fundamental module $V=\mathbb{C}^2$. With the coupled basis of the two-factor problem,

$$
|1,+1\rangle=|\!\uparrow\uparrow\rangle,\qquad
|1,0\rangle=\tfrac{1}{\sqrt2}\left(|\!\uparrow\downarrow\rangle+|\!\downarrow\uparrow\rangle\right),\qquad
|1,-1\rangle=|\!\downarrow\downarrow\rangle ,
$$

a symmetric two-fundamental amplitude with components $(c_{\uparrow\uparrow},c_{\uparrow\downarrow},c_{\downarrow\uparrow},c_{\downarrow\downarrow})$ with $c_{\uparrow\downarrow}=c_{\downarrow\uparrow}$ corresponds to the spinor

$$
\boldsymbol\zeta=\begin{pmatrix}\zeta_+\\ \zeta_0\\ \zeta_-\end{pmatrix}
=\begin{pmatrix}c_{\uparrow\uparrow}\\ \sqrt2\,c_{\uparrow\downarrow}\\ c_{\downarrow\downarrow}\end{pmatrix},
$$

and the normalisation $\boldsymbol\zeta^\dagger\boldsymbol\zeta=1$ is the normalisation of the two-fundamental amplitude. The identification is the standard one, and it is exact: the spin-one internal space of the condensate *is* the triplet sector of two fundamental degrees of freedom.

In the framework the triplet sector is the image of the symmetriser

$$
P_{\mathrm{sym}}=\tfrac{1}{4}\left(3\,e_0\otimes e_0-\sum_{k=1}^{3}e_k\otimes e_k\right),
$$

acting on the four-dimensional module $V\otimes V$ of $\mathbb{B}\otimes_\mathbb{C}\mathbb{B}\cong M_4(\mathbb{C})$. The spin-one operators are the symmetric combinations

$$
\tilde F_k=\tilde S_k^{(1)}+\tilde S_k^{(2)},
$$

which act irreducibly on the triplet and annihilate the singlet, and whose restrictions reproduce the matrices $F_k$ above with matrix elements $\sqrt2\hbar$ in the standard normalisation. A condensate state is thus an element of $\mathbb{B}\otimes_\mathbb{C}\mathbb{B}$ of the form

$$
\rho=P_{\mathrm{sym}}\,\rho\,P_{\mathrm{sym}},\qquad \rho\ge0,\qquad \mathrm{Tr}\,\rho=1 ,
$$

that is, a state of the two-factor algebra living in the exchange-symmetric sector. The spinor is its pure representative,

$$
\rho=|\boldsymbol\zeta\rangle\langle\boldsymbol\zeta| ,
$$

and the two order parameters of the standard theory are its first and second moments.

Counting parameters confirms the identification and locates the framework's contribution. A unit spinor has five real parameters; the global phase is unobservable, leaving four, the dimension of $\mathbb{CP}^2$. A Hermitian element of $\mathbb{B}\otimes_\mathbb{C}\mathbb{B}$ in the symmetric sector has the same four invariant parameters for a pure state, together with the four that describe departure from purity. The framework thus describes the condensate's internal state by the full eight-parameter state space of the symmetric sector, of which the condensate order parameter is the pure part.

### The two order parameters

The framework's operator content on the triplet is generated by the linear operators $\tilde F_k$ and the quadratic operators built from them. The two expectations that the standard energy contains are precisely of these two kinds. The magnetic order is the linear one,

$$
\langle F_k\rangle=\mathrm{Tr}\!\left(\rho\,\tilde F_k\right),
$$

and the alignment is the quadratic one,

$$
\langle F_z^2\rangle=\mathrm{Tr}\!\left(\rho\,\tilde F_z^{\,2}\right)
=\tfrac{2}{3}+\frac{n_3}{\sqrt3}-\frac{n_8}{3} ,
$$

where the second equality gives the alignment in terms of the eighth and third Bloch coordinates of the density matrix, a relation verified on random pure states. The quadratic operators have one further independent expectation, the traceless symmetric tensor

$$
Q_{ij}=\langle F_iF_j\rangle-\tfrac{2}{3}\delta_{ij} ,
\qquad \mathrm{Tr}\,Q=0 ,
$$

which is the *nematic* (quadrupolar) order parameter. For the polar state aligned with the director $\hat{\mathbf n}$ it takes the value $Q_{ij}=\tfrac{1}{3}\delta_{ij}-\hat n_i\hat n_j$, a form that is invariant under $\hat{\mathbf n}\to-\hat{\mathbf n}$ — which is why the polar order parameter is a director and not a vector. The explicit computation for the state $\boldsymbol\zeta=(0,1,0)^T$ gives $\langle\mathbf F\rangle=0$ and $Q=\tfrac{1}{3}\,\mathrm{diag}(1,1,-2)$.

The two order parameters are therefore the framework's rank-one and rank-two tensor expectations, and the statement that the standard uniform mean-field energy depends on the state only through $\lvert\langle\mathbf F\rangle\rvert^2$ and $\langle F_z^2\rangle$ is a statement about which invariants the algebra supplies at the two lowest ranks. The linear invariant detects the adjoint (magnetic) order, the quadratic one detects the nematic order, and for spin one there is no independent invariant at rank three.

## Ferromagnetic and Polar States from the Algebra

### Coherent states from identical idempotents

The spin-one coherent states are the rotations of the stretched state. In the two-factor realisation the stretched state is the product of two identical fundamental states, $|\!\uparrow\uparrow\rangle$, and the framework's version of it is the symmetrised product of two identical fundamental idempotents,

$$
P_{\mathrm{sym}}\left(P_+(\hat{\mathbf n})\otimes P_+(\hat{\mathbf n})\right)P_{\mathrm{sym}}
=\lvert\boldsymbol\zeta_{\hat{\mathbf n}}\rangle\langle\boldsymbol\zeta_{\hat{\mathbf n}}\rvert ,
$$

where $P_+(\hat{\mathbf n})$ is the fundamental idempotent of the informational sector along $\hat{\mathbf n}$ and $\boldsymbol\zeta_{\hat{\mathbf n}}$ is the spin-one coherent state whose magnetic order points along $\hat{\mathbf n}$. The magnetic order parameter of the condensate is thus read off from the axis along which the two fundamental idempotents coincide, and the ferromagnetic phase is the phase in which the two constituent fundamental spins are *parallel*.

This gives the algebraic form of the ferromagnetic order: the order parameter is the axis of a single fundamental idempotent, doubled. The spin-one coherent state has $\lvert\langle\mathbf F\rangle\rvert=1$ — verified explicitly on rotated coherent states — and the two-parameter family of directions, together with the phase, makes the ferromagnetic order-parameter manifold.

### Polar states from antipodal idempotents

The polar states have a different and equally transparent realisation: they are the symmetrised products of two *antipodal* fundamental idempotents,

$$
P_{\mathrm{sym}}\left(P_+(\hat{\mathbf n})\otimes P_-(\hat{\mathbf n})\right)P_{\mathrm{sym}}
=\tfrac{1}{2}\,\lvert\boldsymbol\zeta_{\hat{\mathbf n}}^{\mathrm{pol}}\rangle\langle\boldsymbol\zeta_{\hat{\mathbf n}}^{\mathrm{pol}}\rvert ,
$$

with $P_-(\hat{\mathbf n})$ the orthogonal idempotent along the same axis. That the result is a projector, and that it is the polar state with director $\hat{\mathbf n}$, was verified directly: for $\hat{\mathbf n}=\hat z$ the left-hand side is $\tfrac12\lvert 1,0\rangle\langle 1,0\rvert$ and the state has $\langle\mathbf F\rangle=0$, $Q=\tfrac13\mathrm{diag}(1,1,-2)$. The nematic phase is thus the phase in which the two constituent fundamental spins are *antiparallel*: the magnetic order cancels, and what survives is the common axis, in the form of the traceless symmetric tensor.

The two families exhaust the two extreme values of the magnetic invariant, and they are distinguished by a single algebraic choice — whether the two fundamental idempotents that are symmetrised are the same or orthogonal. The broken-axisymmetric family, which interpolates between them when $q<0$, corresponds to symmetrising two fundamental idempotents that are neither identical nor orthogonal; the angle between the two fundamental spin directions parameterises the departure from the two extremes.

### The order-parameter manifolds

The symmetry group of the problem acts on the symmetric sector as $G=U(1)_{\mathrm{phase}}\times SU(2)_{\mathrm{spin}}$, and the order-parameter manifolds are the orbits. In the framework both factors have an algebraic description: the phase $e^{i\alpha}$ is multiplication by the central element $e^{i\alpha}e_0$ of $\mathbb{B}$, and the spin rotation $e^{-i\beta\hat{\mathbf n}\cdot\mathbf F}$ is the adjoint action on the triplet.

For the ferromagnetic state $\boldsymbol\zeta=(1,0,0)^T$ the stabiliser in $G$ is the diagonal $U(1)$: the rotation about the ferromagnetic axis multiplies the state by a phase, since $e^{-i\beta F_z}(1,0,0)^T=e^{-i\beta}(1,0,0)^T$, which the phase factor can absorb. Hence

$$
M_{\mathrm{FM}}=G/U(1)_{\mathrm{diag}}\;\cong\;S^2\times S^1 ,
$$

three real dimensions: a direction on the sphere and a phase on the circle.

For the polar state $\boldsymbol\zeta=(0,1,0)^T$ the stabiliser is larger. The rotations about the director fix the state exactly, $e^{-i\beta F_z}(0,1,0)^T=(0,1,0)^T$, since $F_z$ annihilates it; and the $\pi$-rotations about the perpendicular axes change it by the sign $-1$, since $e^{-i\pi F_x}(0,1,0)^T=-(0,1,0)^T$, which the phase absorbs. The stabiliser is therefore the group generated by the rotations about the director and those $\pi$-rotations, and the orbit is

$$
M_{\mathrm{polar}}=G/\left(U(1)\rtimes\mathbb{Z}_2\right)\;\cong\;\left(S^2/\mathbb{Z}_2\right)\times S^1 ,
$$

again three real dimensions, but with the director unoriented: $\hat{\mathbf n}$ and $-\hat{\mathbf n}$ give the same state. This is the geometric content of the nematic order parameter, and it is why the polar manifold is not a sphere times a circle but the *quotient* of one.

These manifolds are the standard order-parameter manifolds of the spin-one condensate, and their topology governs the defects: the phase circle contributes mass vortices in both phases, the sphere contributes spin vortices in the ferromagnetic phase, and the $\mathbb{Z}_2$ identification in the polar phase permits half-quantum vortices, in which a winding of the phase by $\pi$ is compensated by a rotation of the director. The framework supplies the algebra of the order parameter and therefore its symmetry breaking pattern; the topological classification then follows by the standard rules.

## The Energy Functional in the Framework

The uniform part of the mean-field energy can be written entirely in the framework's coordinates. Since the spin-dependent interaction depends on the state only through $\lvert\langle\mathbf F\rangle\rvert^2$, and the quadratic Zeeman term only through $\langle F_z^2\rangle$, the energy is a function of the Bloch vector of the symmetric sector,

$$
\mathcal{E}_{\mathrm{uniform}}
=\frac{c_0}{2}n^2+\frac{c_2}{2}n^2\,\lvert\mathbf s(n)\rvert^2
+q\left(\frac{2}{3}+\frac{n_3}{\sqrt3}-\frac{n_8}{3}\right)
+p\,s_3(n) ,
$$

where the components $s_a$ of the magnetic order are the Bloch-coordinate expressions

$$
s_1=\sqrt{\tfrac{2}{3}}\left(n_1+n_6\right),\qquad
s_2=\sqrt{\tfrac{2}{3}}\left(n_2+n_7\right),\qquad
s_3=\tfrac{1}{\sqrt3}n_3+n_8 ,
$$

obtained from $\langle F_k\rangle=\mathrm{Tr}(\rho\tilde F_k)$ with the Gell-Mann expansion of the density matrix. Two observations follow immediately.

First, the ground-state problem is a minimisation of a *quadratic* function of the Bloch vector over the spin-one state space, and the competition between $\lvert\mathbf s\rvert^2$ and $\langle F_z^2\rangle$ is the competition between two quadratic forms. For $c_2<0$ at $q=0$ the minimiser is at $\lvert\mathbf s\rvert=1$, the coherent family; for $c_2>0$ at $q>0$ the interaction wins at $\mathbf s=0$ and $\langle F_z^2\rangle=0$, the polar family; for $c_2>0$ at $q<0$ the quadratic Zeeman term prefers $\langle F_z^2\rangle=1$, which is delivered by the nematic state whose director lies in the plane perpendicular to the field, and the minimiser is that broken-axisymmetric state. The polar state has $\lvert\mathbf s\rvert=0$ and $\langle F_z^2\rangle=0$; the states $(\lvert 1,1\rangle\pm\lvert 1,-1\rangle)/\sqrt2$, which are the extremes of the quadratic Zeeman term, have $\lvert\mathbf s\rvert=0$ and $\langle F_z^2\rangle=1$. These values were verified on the three families.

Second, the framework determines the *form* of the energy functional, not its coefficients. The invariants $\lvert\mathbf s\rvert^2$ and $\langle F_z^2\rangle$ are the two quadratic forms that the algebra supplies on its symmetric sector, and the phases are their competition; the couplings $c_0$, $c_2$, $p$ and $q$ come from the two-body physics and the external field, and are not algebraically determined. The mean-field functional is thus a statement of the framework's kinematics with physical coefficients attached; which is what one expects of a kinematic framework, and it is worth stating plainly because the phase diagram is often presented as though the algebra of the order parameter were an input rather than a consequence.

Minimising the two quadratic forms over the state space reproduces the phase diagram directly, without reference to the spinor parametrisation. A numerical minimisation of $\mathcal{E}$ over all spin-one states, carried out on superpositions rather than on a restricted family, gives the following minimisers.

| $c_2n$ | $q$ | Ground state | $\lvert\langle\mathbf F\rangle\rvert$ | $\langle F_z^2\rangle$ |
|---|---|---|---|---|
| $<0$ | $0$ | ferromagnetic | $1$ | $1$ |
| $>0$ | $>0$ | polar | $0$ | $0$ |
| $>0$ | $<0$ | broken axisymmetric | $0$ | $1$ |
| $<0$ | $>0$ | tilted, partially magnetised | $<1$ | intermediate |

The three named phases sit at the corners of the $(c_2,q)$ plane and are the states that the two invariants take to their extreme values; the fourth row is the intermediate region in which the quadratic Zeeman term reduces the magnetic order without destroying it. In the ferromagnetic row at $q=0$ the direction is degenerate — every coherent direction is a minimiser, with $\langle F_z^2\rangle$ ranging over $[\tfrac12,1]$ — and the value listed is that of the field-aligned representative. In every case the minimiser was a pure state, as it must be, since the energy is linear in the density matrix and the state space is convex: a mixed state can never beat both of its components.

## What the Algebra Determines and What Is Imported

The division of labour in the preceding sections can be tabulated.

| Ingredient of the spin-one condensate | Status in the framework |
|---|---|
| Three-component spinor, unit normalisation | vector in $\mathrm{Sym}^2V$; the triplet of $\mathbb{B}\otimes_\mathbb{C}\mathbb{B}$ |
| Spin-one operators, $\mathbf F^2=2I$ | restrictions of $\tilde S_k^{(1)}+\tilde S_k^{(2)}$ |
| Phase symmetry $U(1)$ | multiplication by the centre $e^{i\alpha}e_0$ of $\mathbb{B}$ |
| Spin symmetry $SU(2)$ | the adjoint action on the triplet |
| Magnetic order $\langle\mathbf F\rangle$ | linear (rank-one) tensor expectation |
| Nematic order $Q_{ij}$ | rank-two tensor expectation, traceless part |
| Coherent (ferromagnetic) states | symmetrised products of identical fundamental idempotents |
| Polar/nematic states | symmetrised products of antipodal fundamental idempotents |
| Alignment invariant $\langle F_z^2\rangle$ | $\tfrac23+n_3/\sqrt3-n_8/3$, a quadratic form in the Bloch vector |
| Order-parameter manifolds | orbits of the centre and the adjoint action |
| Defect classification | inherited from the manifold topology; not algebraic |
| Couplings $c_0$, $c_2$, $p$, $q$, scattering lengths | imported from the standard two-body theory |

The pattern is the one the subcategory has established throughout: the algebra supplies the state space, the operators and the invariants, and therefore the symmetry-breaking pattern and the shape of the energy as a function of the state; the dynamics — which coefficients multiply which invariant, and hence which phase is selected for which atom — is physics imported from outside the algebra. The value of the framework's description is that the spin-one order parameter is not posited but *built*: it is what two fundamental systems look like when they are symmetrised, and the two phases are what the two ways of symmetrising a pair — in parallel and in antiparallel alignment — produce.

## Summary

- The order parameter of a spin-one condensate is a unit spinor $\boldsymbol\zeta\in\mathbb{C}^3$ carrying the three spin projections, invariant under $G=U(1)_{\mathrm{phase}}\times SU(2)_{\mathrm{spin}}$; in the framework it is a vector in the symmetric square $\mathrm{Sym}^2V$ of the defining module, realised as the triplet sector of $\mathbb{B}\otimes_\mathbb{C}\mathbb{B}\cong M_4(\mathbb{C})$ selected by $P_{\mathrm{sym}}$, with components $(c_{\uparrow\uparrow},\sqrt2c_{\uparrow\downarrow},c_{\downarrow\downarrow})$.
- The two factors of the symmetry group have algebraic interpretations: the phase is multiplication by the central element $e^{i\alpha}e_0$, and the spin rotation is the adjoint action on the triplet.
- The standard mean-field energy is a function of the spinor only through the three invariants $\lvert\langle\mathbf F\rangle\rvert^2$, $\langle F_z\rangle$ and $\langle F_z^2\rangle$. In the framework these are the rank-one tensor expectation, the quadratic $F_z^2$ expectation, and the $z$-component of the magnetic order; the alignment was verified to be $\langle F_z^2\rangle=\tfrac23+n_3/\sqrt3-n_8/3$ on random pure states, and the magnetic order components are $s_1=\sqrt{2/3}(n_1+n_6)$, $s_2=\sqrt{2/3}(n_2+n_7)$, $s_3=n_3/\sqrt3+n_8$.
- The nematic (quadrupolar) order parameter is the traceless symmetric tensor $Q_{ij}=\langle F_iF_j\rangle-\tfrac23\delta_{ij}$; for the polar state along $\hat{\mathbf n}$ it is $\tfrac13\delta_{ij}-\hat n_i\hat n_j$, invariant under $\hat{\mathbf n}\to-\hat{\mathbf n}$. The polar state $\boldsymbol\zeta=(0,1,0)^T$ has $\langle\mathbf F\rangle=0$ and $Q=\tfrac13\mathrm{diag}(1,1,-2)$, both verified.
- Ferromagnetic and polar ground states have a common algebraic origin: the ferromagnetic states are $P_{\mathrm{sym}}\left(P_+(\hat{\mathbf n})\otimes P_+(\hat{\mathbf n})\right)P_{\mathrm{sym}}$, symmetrised products of *identical* fundamental idempotents, with $\lvert\langle\mathbf F\rangle\rvert=1$; the polar states are $P_{\mathrm{sym}}\left(P_+(\hat{\mathbf n})\otimes P_-(\hat{\mathbf n})\right)P_{\mathrm{sym}}=\tfrac12\lvert\boldsymbol\zeta^{\mathrm{pol}}_{\hat{\mathbf n}}\rangle\langle\boldsymbol\zeta^{\mathrm{pol}}_{\hat{\mathbf n}}\rvert$, symmetrised products of *antipodal* idempotents, with $\langle\mathbf F\rangle=0$. Parallel constituents give magnetic order, antiparallel constituents give nematic order.
- The order-parameter manifolds follow from the orbit-stabiliser computation with the stabilisers $U(1)_{\mathrm{diag}}$ and $U(1)\rtimes\mathbb{Z}_2$: $M_{\mathrm{FM}}\cong S^2\times S^1$ and $M_{\mathrm{polar}}\cong(S^2/\mathbb{Z}_2)\times S^1$, both of three real dimensions, the second encoding the unoriented director.
- The uniform energy is a quadratic function of the Bloch vector of the symmetric sector; the phase diagram is the competition of two quadratic forms, and the couplings that decide the winner are imported from the two-body theory, not derived from the algebra. A numerical minimisation over superpositions reproduces the standard corners: ferromagnetic ($\lvert\langle\mathbf F\rangle\rvert=1$, $\langle F_z^2\rangle=1$ for the field-aligned member of the degenerate direction family) for $c_2<0$ at $q=0$, polar ($0$, $0$) for $c_2>0$ at $q>0$, and broken axisymmetric ($0$, $1$) for $c_2>0$ at $q<0$; the minimiser is always a pure state, as convexity requires.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Psi=\sqrt n\,e^{i\theta}\boldsymbol\zeta$ | Condensate wave function; $n$ density, $\theta$ phase |
| $\boldsymbol\zeta=(\zeta_+,\zeta_0,\zeta_-)^T$ | Spinor order parameter, $\boldsymbol\zeta^\dagger\boldsymbol\zeta=1$ |
| $F_k$ | Dimensionless spin-one operators, eigenvalues $\pm1,0$; $\mathbf F^2=2I_3$ |
| $\langle\mathbf F\rangle$ | Magnetic (vector) order parameter |
| $Q_{ij}=\langle F_iF_j\rangle-\tfrac23\delta_{ij}$ | Nematic (quadrupolar) order parameter, traceless |
| $G=U(1)_{\mathrm{phase}}\times SU(2)_{\mathrm{spin}}$ | Symmetry group of the order parameter |
| $c_0,c_2$ | Spin-independent and spin-dependent contact couplings |
| $p,q$ | Linear and quadratic Zeeman coefficients |
| $P_{\mathrm{sym}}$ | Symmetriser onto the triplet of $\mathbb{B}\otimes_\mathbb{C}\mathbb{B}$ |
| $\tilde F_k=\tilde S_k^{(1)}+\tilde S_k^{(2)}$ | Triplet spin operators of the two-factor algebra |
| $P_\pm(\hat{\mathbf n})$ | Fundamental idempotents of the informational sector |
| $n_1,\dots,n_8$ | Bloch coordinates of the symmetric-sector state |
| $M_{\mathrm{FM}},M_{\mathrm{polar}}$ | Order-parameter manifolds $S^2\times S^1$, $(S^2/\mathbb{Z}_2)\times S^1$ |

## Further Reading

- Tin-Lun Ho, "Spinor Bose Condensates in Optical Traps", *Physical Review Letters* **81** (1998) 742, for the spin-one condensate, its order parameter and its ground-state phases.
- T. Ohmi and K. Machida, "Bose–Einstein Condensation with Internal Degrees of Freedom in Alkali Atom Gases", *Journal of the Physical Society of Japan* **67** (1998) 1822, for the mean-field functional and the magnetic phase.
- Dan M. Stamper-Kurn and Masahito Ueda, "Spinor Bose gases: Symmetries, magnetism, and quantum dynamics", *Reviews of Modern Physics* **85** (2013) 1191, for the symmetry classification, the phase diagram, the order-parameter manifolds and the topological defects.
- Yuki Kawaguchi and Masahito Ueda, "Spinor Bose–Einstein condensates", *Physics Reports* **520** (2012) 253, for the order-parameter manifolds, their homotopy groups, and the defect classification.
- Lev Pitaevskii and Sandro Stringari, *Bose–Einstein Condensation and Superfluidity* (Oxford University Press, 2016), for the mean-field theory of condensates and the contact-interaction couplings.
- Chaoyang Zhang, *Spinor Bose–Einstein Condensates* (World Scientific, 2011), for the spin-one and spin-two order parameters and their symmetry properties.
- J. J. Sakurai and Jim Napolitano, *Modern Quantum Mechanics* (Pearson, 2017), for the spin-one algebra, coherent states and rotation matrices used here.
- Ingemar Bengtsson and Karol Życzkowski, *Geometry of Quantum States* (Cambridge University Press, 2006), for the geometry of three-level state spaces and the Bloch-vector parameterisation of the Gell-Mann basis.
