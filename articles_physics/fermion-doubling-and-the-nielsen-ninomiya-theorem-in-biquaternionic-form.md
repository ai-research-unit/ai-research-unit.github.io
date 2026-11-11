# __Fermion Doubling and the Nielsen–Ninomiya Theorem in Biquaternionic Form__

## Introduction

Putting a single Dirac fermion on a lattice produces more than one fermion. The naive discretization of the Dirac action in $d$ Euclidean dimensions yields $2^d$ identical species — sixteen in four dimensions — called **tastes** of the fermion. The extra states are **doublers**, and they are not an artefact of one careless choice of difference operator: the **Nielsen–Ninomiya theorem** states that under very general assumptions a lattice regularization of chiral fermions must carry equal numbers of $L$ and $R$ species — the two values of the chirality subscript of *Matrix Representations Conventions*. A chiral gauge theory therefore cannot be put on a lattice without giving up one of the assumptions. The obstruction is one of the sharpest in lattice field theory, and it is the reason lattice QCD uses modified fermions — Wilson, staggered, Ginsparg–Wilson, domain-wall, overlap, twisted-mass — each of which pays a price to the theorem rather than escaping it.

This article treats fermion doubling in the biquaternion framework. The framework's honest contribution here is again a **negative** one, and it should be stated first: the biquaternion Dirac equation does **not** evade Nielsen–Ninomiya. If a lattice is imposed on the biquaternion gradient, the doubling argument applies unchanged, because the argument uses only locality, hermiticity, translation invariance and the oddness of the massless symbol about the origin — properties that the discretized biquaternion gradient shares with the standard one. The algebra is not a lattice, and it does not supply one. What the framework can do is state the obstruction in its own variables, and — this is the one positive structural point — its multivector form of the Dirac field places it naturally close to the **Dirac–Kähler** equation, whose simplicial discretization is exactly the staggered fermion, a lattice formulation whose doublers are reduced but not removed.

**One operator, and it is the gradient.** Every derivative of the article is the biquaternionic gradient of *Operator and Calculus Conventions*, §*The Gradient*, with its quaternion conjugate and its d'Alembertian,

$$
\tilde\nabla=\sum_{\mu\in\{t,x,y,z\}}e_\mu\frac{\partial}{\partial R_\mu},
\qquad
\tilde\nabla^{\natural}=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu e_\mu\frac{\partial}{\partial R_\mu},
\qquad
\Box_\Phi=\tilde\nabla_\Phi(\tilde\nabla_\Phi)^{\natural}=\frac{\partial^2}{\partial R_t^2}+\Delta_Q ,
$$

with $\varepsilon=(1,-1,-1,-1)$. No second letter is introduced for it. No derivative of the article is two-sided: the lattice gradient of §*Naive Discretization* is this same operator with each coordinate derivative replaced by a symmetric difference.

The next section sets up the naive discretization, its propagator and its doublers, and the taste degeneracy. The section after states the Nielsen–Ninomiya theorem and the index-theoretic idea of its proof, then surveys the resolutions and what each one sacrifices. The biquaternion reading follows: the discretization of the biquaternion gradient, the independence of the doubling from the algebra, the relation to Dirac–Kähler and staggered fermions, and the framework's index-theorem connection. The closing sections are the open questions, the summary, the notation table and the literature.

## Naive Discretization

### The field, the chirality and the lattice

**The field.** The field is the biquaternion $\tilde{Ξ}_{\mathrm{sp}}$, an element of $\mathbb{B}$; $\tilde{Ξ}_{\mathrm{sp}}$ is its four-component coordinate column where a column is needed. Its coordinates are the four coordinates of the $\mathbb{B}$ frame, $Q_t,Q_x,Q_y,Q_z$, which on the material sector read $Q_t=i q'_t$ and $Q_\eta=q_\eta$ (*Frame and Metric Conventions*). Here $i$ is the scalar imaginary, $i^2=-1$.

**The dynamics is the chiral pair of the gradient**,

$$
\tilde\nabla_\Phi\tilde{Ξ}_{\mathrm{sp},R}=k_m\tilde{Ξ}_{\mathrm{sp},L},
\qquad
(\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=k_m\tilde{Ξ}_{\mathrm{sp},R},
$$

with massless limit $\tilde\nabla_\Phi\tilde{Ξ}_{\mathrm{sp}}=0$; the subscript is the chirality label. The free equation is first order and one field. The massive equation is not: $\tilde\nabla^2$ is not scalar, because the time unit commutes with the three space units, so the mixed terms survive the sum: $\tilde\nabla^2=\partial^2/\partial R_t^2-\Delta_Q+2\sum_\eta\vec e_\eta\,\partial^2/\partial R_t\partial R_\eta$, which is not scalar — verified on a polynomial element, where the vector part of $\tilde\nabla^2\tilde{Ξ}_{\mathrm{sp}}$ is nonzero. There is therefore no one-field, first-order massive equation in this algebra. The pair is the whole of the massive dynamics, and no letter is introduced to make it look like one equation. Here $k_m=mc/\hbar$ is the mass wave number, the inverse of the mass length.

**The chirality is a right action.** $\xi\tilde Q=-i\tilde Q\vec e_z$, of spectrum $+1,+1,-1,-1$ and of the two values $L$ and $R$ (*Special Element Conventions*, §*The Chirality Convention*). The side is part of the definition: the left action $\tilde Q\mapsto-i\vec e_z\tilde Q$ is a different operator — the two differ by conjugation by $\vec e_z$ — and it is not the chirality. Neither operator is two-sided; each is a single multiplication, written out.

**The lattice.** A lattice of spacing $a$ has sites indexed by integer vectors $n=(n_1,n_2,n_3,n_4)$, and $\vec u_\mu$ is the unit lattice vector in the direction $\mu$. The index $\mu=1,\dots,4$ labels the four coordinate directions. The field becomes a Grassmann-valued element $\tilde{Ξ}_{\mathrm{sp},n}$ at each site, with $\tilde{Ξ}_{\mathrm{sp},n}^*$ an independent Grassmann variable and not its conjugate, and each coordinate derivative is replaced by the **symmetric difference**

$$
D_\mu\tilde{Ξ}_{\mathrm{sp},n}=\frac{\tilde{Ξ}_{\mathrm{sp},n+\vec u_\mu}-\tilde{Ξ}_{\mathrm{sp},n-\vec u_\mu}}{2a},
\qquad
D_\mu\ \text{replaces}\ \frac{\partial}{\partial R_\mu}.
$$

The lattice gradient is the same gradient with these differences in place of the four derivatives,

$$
\tilde\nabla^{L}=\sum_{\mu}e_\mu D_\mu ,
$$

and the naive action is the scalar part of the field contracted with it,

$$
S_F^L[\tilde{Ξ}_{\mathrm{sp}}] = a^4\sum_n \mathrm{Sc}\bigl[\tilde{Ξ}_{\mathrm{sp},n}^*\,\tilde\nabla^{L}\tilde{Ξ}_{\mathrm{sp},n}\bigr],
$$

the action whose equation of motion is the massless limit of the pair. The mass is not a term of this one-field action: it is the second line of the pair, and its lattice form is the pair's. Each $D_\mu$ is anti-Hermitian up to the boundary term of summation by parts, exactly as $\partial/\partial R_\mu$ is, so the kinetic kernel meets the hermiticity hypothesis of §*The Nielsen–Ninomiya Theorem* in the same form as the standard discretization. The action reduces to $\int d^4r\,\mathrm{Sc}\bigl[\tilde{Ξ}_{\mathrm{sp}}^*\,\tilde\nabla_\Phi\tilde{Ξ}_{\mathrm{sp}}\bigr]$ as $a\to0$. It therefore looks like a theory of a single fermion. It is not.

**The coordinates are the frame's own.** The four $Q_\mu$ are the $\mathbb{B}$ frame's coordinates, and the frame's form is $\sum_\mu Q_\mu^2$ with all four coefficients equal: the lattice is imposed on a Euclidean coordinate, and nothing has to be rotated before discretizing. The fourth coordinate is $Q_t=i q'_t$ with $x_0=r'_{t}$, so a lattice momentum $p_t$ is read at $p_t=i\omega/c$ for a frequency $\omega$, and in lattice units $a=1$ at $p_t=i\omega$. The doubling count depends on $\sin(p_\mu a)$ alone and not on the signature.

### The propagator and the doubler poles

**The symbol.** On a plane wave $\tilde{Ξ}_{\mathrm{sp},n}\propto e^{i(p\cdot x)/\hbar}$ the symmetric difference carries $i\sin(p_\mu a)/a$, so the lattice gradient acquires the element symbol

$$
\tilde K_{\Phi}(p)=a^{-1}\sum_{\mu}\sin(p_\mu a)\,e_\mu ,
\qquad
\tilde\nabla^{L}\ \longrightarrow\ i\tilde K_{\Phi}(p),
$$

displayed again in §*Discretizing the biquaternion gradient*. Left multiplication by a nonzero element of $\mathbb{B}$ is invertible over $\mathbb{C}$ unless the element is a **zero divisor**, and the test is the quaternion norm,

$$
\tilde K_{\Phi}\tilde K_{\Phi}^{\natural}=a^{-2}\sum_{\mu}\sin^2(p_\mu a),
$$

a scalar. Verified: the identity at residual $5\times10^{-15}$ over $200$ random real momenta, and the rank four of left multiplication by $\tilde K_{\Phi}$ wherever the norm is nonzero.

**The massive propagator.** With the mass the equation is the pair, and its symbol is the block

$$
\mathcal P(p)=\begin{pmatrix}-m & i\tilde K_{\Phi}(p)\ i\tilde K_{\Phi}(p)^{\natural} & -m\end{pmatrix},
\qquad
\det\mathcal P(p)=\Bigl(m^2+a^{-2}\sum_{\mu}\sin^2(p_\mu a)\Bigr)^{4},
$$

so the propagator is the inverse block,

$$
\boxed{\;\mathcal S(p) = -\frac{1}{\,m^{2}+a^{-2}\sum_{\mu}\sin^{2}(p_\mu a)}\begin{pmatrix} m & i\tilde K_{\Phi}(p)\ i\tilde K_{\Phi}(p)^{\natural} & m\end{pmatrix}\;}.
$$

Both identities verified by direct inversion, at residual $0$ for the inverse and $1\times10^{-12}$ for the determinant; the massless inverse, the inverse of left multiplication by $i\tilde K_{\Phi}$, is $\mathcal S_0(p)=-i\tilde K_{\Phi}^{\natural}/(\tilde K_{\Phi}\tilde K_{\Phi}^{\natural})$ at the same residual. The scalar denominator is exactly the one the single-column form of the literature carries. The block is the price of the mass, and it is the block of the chiral pair, not a second dynamics.

**The poles.** The denominator vanishes at $m=0$ when $\sin(p_\mu a) = 0$ for every $\mu$, that is, at the points

$$
\boxed{\;a p_\mu = \pi_{A\mu}\;},
$$

where the sixteen vectors $\pi_A$ have entries $0$ or $\pi$. Taking the zone as $[0,2\pi/a)^4$, these sixteen points are its corners: one is the origin, the other **fifteen are the doublers**, and each is a distinct fermion species. Verified: a grid of $64^4$ momenta in the zone has exactly sixteen zeros, distinct. For $m\ne0$ the denominator is bounded below by $m^2$ on the real zone, so no pole lies there at all; all sixteen species reappear as $m\to0$. The mechanism is the symbol: over one period of length $2\pi/a$, $\sin(p_\mu a)$ has two zeros, at $p_\mu=0$ and $p_\mu=\pi/a$, whereas the bosonic symbol built from $\sin(p_\mu a/2)$ has one.

The doubling also shows in the dispersion relation. In lattice units $a=1$, the pole condition with $p_t=i\omega$ gives

$$
\sinh^2\omega(\vec p) = m^2 + \sum_{\eta=1}^3\sin^2 p_\eta .
$$

Its minima sit at the zeros of the spatial sines, eight in all. The temporal direction doubles each of them: $\sin^2(p_ta)$ has period $\pi/a$, so $p_t=0$ and $p_t=\pi/a$ give the same branch, and the sixteen poles are the eight spatial corners times the two temporal choices.

The same count follows from the symbol alone. At $m=0$ the inverse propagator is the element $i\tilde K_{\Phi}(p)$, an **odd** periodic function of $p$. Each of the sixteen points $\pi_A/a$ equals its own negative modulo $2\pi/a$, so oddness forces the symbol to vanish at all sixteen: a lone zero at the origin is impossible. A scalar boson escapes, because its symbol $\sin(p_\mu a/2)$ is even about the origin.

**What the doublers are in the algebra.** The sixteen are the momenta at which the symbol is the zero element. Off the real zone the symbol can instead be a nonzero zero divisor, and there left multiplication by $\tilde K_{\Phi}$ has rank two and a kernel of complex dimension two — verified at three null momenta, rank $2$ and kernel $2$ each. On the real zone the symbol vanishes outright and the propagator has a simple pole. The doubling is thus a property of the difference operator read through the quaternion norm; the algebra supplies the norm and nothing else.

### The taste degeneracy

**There are no sixteen species of the field to permute.** The field is one element and its symbol is one element, so no transformation of the field permutes sixteen spinor species, and none is claimed. What the naive action carries is a degeneracy of the pole set, and the degeneracy is exact in the free theory.

**The pole condition is one scalar equation**, $\tilde K_{\Phi}\tilde K_{\Phi}^{\natural}=0$, and it depends on $\sin^2(p_\mu a)$ alone. Hence the shift $p_\mu\mapsto p_\mu+\pi/a$ on any subset $A$ of the four directions leaves it unchanged, and the sixteen corners are one orbit under the sixteen shifts. The symbol itself is multiplied by the sign pattern $(-1)^{\delta_{\mu\in A}}$,

$$
\tilde K_{\Phi}(p+\pi_A/a)=a^{-1}\sum_{\mu}(-1)^{\delta_{\mu\in A}}\sin(p_\mu a)\,e_\mu ,
$$

so the shift reverses the sign of some of the four units and does nothing else.

**Which sign patterns the algebra supplies.** Conjugation by the unit $\vec e_\eta$, the map $x\mapsto\vec e_\eta x\vec e_\eta^{-1}$ — the only two-sided product in the article, and it acts on the units, never on the field or on a derivative — reverses the two spatial units perpendicular to it and fixes the other two: $\vec e_z x\vec e_z^{-1}$ sends $\vec e_x,\vec e_y$ to their negatives and fixes $\vec e_z$. So the four even sign patterns on the three spatial units are realized by inner automorphisms of $\mathbb{B}$. The quaternion conjugation $\natural$ reverses all three spatial units and supplies the four odd patterns. The temporal unit is central: no automorphism of $\mathbb{B}$ reverses it, and no element anticommutes with all four units — verified, the null space of the four equations $e_\mu a=-ae_\mu$ is zero. The temporal sign is reached by the shift alone.

**What follows.** The sixteen poles are exactly degenerate in the free theory, and the degeneracy is a property of the difference operator, not of the algebra. They cannot be discarded in an interacting theory: the lattice conserves momentum only modulo $2\pi/a$, so a hard virtual gauge boson can transfer $\pi/a$ and connect the tastes.

## The Nielsen–Ninomiya Theorem

### Statement and assumptions

The **Nielsen–Ninomiya theorem** (1981) is the no-go theorem behind the doubling, and its content is a statement about **one chiral species**: a lattice theory cannot carry a single Weyl field. Whatever the kernel, the $L$ and the $R$ species come in equal numbers, so a lone $L$ drags in an $R$ however the action is written.

**Hamiltonian form.** Take $H=\sum_{x,y}\tilde{Ξ}_{\mathrm{sp}}^{\dagger}(x)F(x,y)\tilde{Ξ}_{\mathrm{sp}}(y)$ with a conserved charge $Q$, where $\tilde{Ξ}_{\mathrm{sp}}$ is the spinor column, $\tilde{Ξ}_{\mathrm{sp}}^{\dagger}$ its column adjoint and $F(x,y)$ a matrix on that column: the theorem's own kernel is a matrix, and no element of $\mathbb{B}$ is meant here. The numbers of $L$ and $R$ fermions are equal for every set of charges, provided that

- **translation invariance** holds, $F(x,y)=F(x-y)$;
- **locality** holds, meaning $F(x-y)$ decays fast enough for its Fourier transform to have continuous derivatives;
- **hermiticity** holds, $F(x)^\dagger=F(-x)$;
- the charge is **local, quantized and exactly conserved**.

**Euclidean form.** The statement is then about the $R$ part alone, with a biquaternion-valued kernel, one component per coordinate direction,

$$
\tilde F(x,y)=\sum_{\mu}F_\mu(x,y)\,e_\mu ,
\qquad
S=\sum_{x,y}\mathrm{Sc}\bigl[\tilde{Ξ}_{\mathrm{sp},R}^*(x)\,\tilde F(x,y)\,\tilde{Ξ}_{\mathrm{sp},R}(y)\bigr],
$$

under the same three hypotheses, translation invariance, locality, and hermiticity of the operator the kernel generates; here $\tilde{Ξ}_{\mathrm{sp},R}$ is the $R$ part of the field, the chirality subscript of *Matrix Representations Conventions*, and no $L$ part is present. The kernel is an element of $\mathbb{B}$: the four $F_\mu$ are its coordinates, and the four coordinate directions are the units.

**General form, all regularizations.** No regularized chiral fermion theory can simultaneously have the correct global symmetry, unequal numbers of $L$ and $R$ Weyl species, the correct chiral anomaly, and an action bilinear in the Weyl fields. The Standard Model therefore cannot be put on a lattice without violating one of these conditions, and a chirally invariant regularization makes the chiral anomaly vanish, which is wrong.

**What the theorem does not say.** It does not say *how many* doublers appear, only that at least one partner is forced. It is vacuous when chiral fermions do not exist, that is in odd dimensions, because there is no chirality operator that anticommutes with all four unit directions.

### The proof idea

The Euclidean proof uses the **Poincaré–Hopf theorem**, and it has three steps. Locality makes the Fourier transform of the kernel, $\tilde F(k)=\sum_\mu F_\mu(k)e_\mu$, a continuous $\mathbb{B}$-valued field on the Brillouin zone, and that field is the inverse propagator. Its isolated zeros are the particle species; around each zero the field is a source, a sink or a saddle, and its **index** there is $\pm1$, the two signs being the two values $L$ and $R$. Poincaré–Hopf then says that the sum of the indices equals the Euler characteristic of the manifold the field lives on, and the Brillouin zone is a four-torus, whose Euler characteristic is **zero**.

Hence the numbers of $L$ and $R$ species are equal, and the doublers are unavoidable: the count is a topological identity, not a property of any one difference operator.

## Resolutions and What Each One Sacrifices

Every lattice fermion formulation must give up at least one hypothesis of the theorem, or the bilinear form of the action that carries them. The main routes are:

- **Wilson fermions** add a term proportional to the second difference, which gives the doublers a mass of order $1/a$ and removes them from the low-energy theory, at the cost of explicitly breaking chiral symmetry.
- **Ginsparg–Wilson fermions** satisfy a remnant of chiral symmetry on the lattice, $\{D,\xi\}=a\,D\xi D$ with $D$ the lattice Dirac operator and $\xi$ the chirality, $\xi\tilde Q=-i\tilde Q\vec e_z$, in place of the continuum anticommutator $\{D,\xi\}=0$; the **overlap** fermions realize this with an exactly massless, index-carrying operator. Chiral symmetry is not broken explicitly; it is realized in this modified form.
- **Domain-wall fermions** place chiral fermions on the boundaries of an extra dimension; the bulk mass term breaks chiral symmetry explicitly, but the boundary mode's chiral symmetry is restored as the extra dimension grows, and the price is the extra dimension.
- **Staggered (Kogut–Susskind) fermions** reduce the sixteen tastes to four by distributing the four components of the field over the sites of a hypercube, which leaves only a discrete remnant of the translation symmetry.
- **Twisted-mass Wilson fermions** add a chirally twisted mass term; the Wilson term removes the doublers, and the twist protects a remnant of chiral symmetry.
- **Symmetric mass generation** is a non-perturbative interacting route that gaps the mirror fermions without breaking the symmetries, evading the bilinear assumption.
- **Non-local formulations** (perfect, SLAC, Stacey fermions) use a discontinuous propagator and are non-local.
- **One-sided difference operators** (forward or backward) avoid doubling because they are non-hermitian and so violate the theorem's hermiticity assumption; the resulting interacting theory is non-covariant and hard to renormalize, and is not used in practice.

What survives all of this is the part with experimental consequences: the correct anomaly structure in lattice QCD, and the impossibility of a chirally invariant lattice discretization of a chiral gauge theory.

## The Biquaternion Reading

### Discretizing the biquaternion gradient

The framework's gradient is $\tilde\nabla_\Phi$, the one of *Operator and Calculus Conventions*, and it is the only derivative operator of the article. A lattice discretization replaces each of its four partial derivatives by a difference operator. If the symmetric difference is used, the Fourier symbol of $\partial/\partial R_\mu$ is $i\sin(p_\mu a)/a$ in each direction, and on plane waves the biquaternion gradient acquires the symbol

$$
\boxed{\;\tilde\nabla_\Phi \;\longrightarrow\; e_t\,\frac{i\sin(p_ta)}{a}+\sum_{\eta=x,y,z}\vec e_\eta\,\frac{i\sin(p_ka)}{a}\;},
$$

that is, $i\tilde K_{\Phi}(p)$ with $\tilde K_{\Phi}$ of §*The propagator and the doubler poles*. The denominator of the lattice propagator is then the scalar $\tilde K_{\Phi}\tilde K_{\Phi}^{\natural}=\sum_\mu\sin^2(p_\mu a)/a^2$, which has the sixteen zeros identified above.

### The doubling is a property of the difference operator, not of the algebra

This is the article's central negative statement. Nothing in the derivation of the doublers uses the biquaternion structure: it uses (a) locality, (b) hermiticity of the difference operator, (c) translation invariance, and (d) the oddness about $p=0$ of the massless symbol. The discretized biquaternion gradient satisfies all four exactly as the standard one does. **Therefore the biquaternion Dirac equation suffers fermion doubling on any lattice satisfying the theorem's hypotheses, and the framework offers no evasion of Nielsen–Ninomiya.** A claim to the contrary would be false: the algebra is a continuum algebra; it is not a lattice, and it does not supply a non-local or non-hermitian difference operator either. The companion article on Dirac matter faces the mirror-image fact, that the algebra is indifferent to the lattice that sits on top of it.

### Dirac–Kähler and staggered fermions

The one positive structural point is a proximity, not a solution. The biquaternion field sits in the even part of a **Dirac–Kähler** multivector, the field of the companion mathematical article. The Dirac–Kähler equation is the multivector equation; its operator is odd and couples the even and odd parts, so it does not restrict to the biquaternion field. The relation is therefore containment, not identity. What the containment gives is the natural discretization: on a simplicial complex the Dirac–Kähler equation becomes the **staggered fermion** formulation, and the even part is the framework's field. Staggered fermions do not remove doubling; they reduce the sixteen tastes to four and preserve a remnant symmetry. So the framework's multivector form places it naturally in the family of lattice formulations that *mitigate* doubling, and not in the family that evades it. This is a structural statement about the natural discretization, not a derivation of a lattice for the biquaternion equation.

### Index-theoretic connections

Two index-theoretic facts touch the framework through its companion articles. First, the anomalous half-integer quantum Hall effect of graphene — the $\tfrac12$ offset of the companion Dirac-matter article — is a consequence of the Atiyah–Singer index theorem applied to the massless Dirac operator in a magnetic field: a Landau level sits exactly at the Dirac point, half-filled in neutral graphene. Second, the Dirac–Kähler operator's zero modes on a compact manifold are the harmonic forms, guaranteed to exist whenever the relevant Betti numbers do not vanish, unlike the Dirac operator, which has none when the scalar curvature is positive (Lichnerowicz). Both are statements about the analytic index of a Dirac-type operator. The framework's equation is one more Dirac-type operator in this family, and its index is expected to behave accordingly; the corpus has not computed it.

### What the framework supplies and what it does not

The framework supplies a continuum equation and a multivector structure whose natural discretization is the staggered one. It does **not** supply a lattice, a chirally invariant lattice formulation, a resolution of the doubling, or any modification of the Nielsen–Ninomiya theorem. The theorem is a statement about local, hermitian, translation-invariant lattice bilinears, and the biquaternion algebra says nothing about any of those properties; imposing a lattice on it puts it under the theorem, not beside it.

## Open Questions

1. **The index of the biquaternion Dirac operator.** The companion Dirac–Kähler article gives the zero modes of the multivector Dirac operator as harmonic forms. What is the corresponding statement for the biquaternion gradient $\tilde\nabla_\Phi$, and does the $\mathbb{B}_{\Psi}/\mathbb{B}_{\Phi}$ split organize the index?

2. **The lattice imposition.** Is there a lattice that the framework's structure selects among the many possible ones, in the way that the multivector form selects simplicial/staggered? This article argues only for the *proximity* to staggered; a derivation is not attempted.

3. **Anomaly matching.** The general Nielsen–Ninomiya statement involves the correct chiral anomaly. The framework's anomaly treatment — does it have one, and is it the standard bilinear one? — is not in the corpus and is the sharpest open point.

4. **Odd dimensions.** The theorem is vacuous in odd dimensions. Does the framework's dimension-independence (the algebra is defined for any $d$) have anything to say about the chirality-free odd-dimensional case, or is that a pure lattice statement?

5. **Symmetric mass generation.** This resolution evades the bilinear assumption by interactions. Whether the framework's sector structure can express the gapping of mirror fermions is open.

6. **Empirical contact.** As everywhere, the doubling is a lattice artefact without continuum signature; any framework-level claim must respect that.

## Summary

Naive discretization of the Dirac action on a $d$-dimensional lattice gives $2^d$ tastes — sixteen in four dimensions — because the difference operator's symbol $\sin(p_\mu a)$ has two zeros per period. The doublers appear as extra poles of the propagator at the Brillouin-zone corners, all sixteen are poles of the one scalar denominator $\tilde K_{\Phi}\tilde K_{\Phi}^{\natural}$, and they are exactly degenerate in the free theory, so an interacting lattice theory cannot simply drop them. The Nielsen–Ninomiya theorem states the obstruction: a local, hermitian, translation-invariant lattice bilinear has equal numbers of $L$ and $R$ species; the Euclidean proof is a Poincaré–Hopf index count on the Brillouin-zone torus, whose Euler characteristic vanishes. Every resolution — Wilson, staggered, Ginsparg–Wilson, overlap, domain-wall, twisted-mass, symmetric mass generation, non-local, one-sided — gives up one of the theorem's hypotheses, and symmetric mass generation gives up the bilinear form of the action rather than a hypothesis.

The biquaternion framework does not evade the obstruction. The doubling argument uses only locality, hermiticity, translation invariance and the oddness of the massless symbol, all of which the discretized biquaternion gradient shares; the algebra is not a lattice and supplies no alternative difference operator. The one positive structural point is that the framework's multivector field is contained in the **Dirac–Kähler** multivector, whose simplicial discretization is the **staggered fermion** formulation — a mitigation, not a solution. Two index-theoretic facts reach the framework as companions: the anomalous half-integer quantum Hall effect of graphene and the harmonic-form zero modes of the Dirac–Kähler operator.

## Summary of Notation

| Symbol | Meaning |
|+-|+-|
| $a$, $n$, $\vec u_\mu$ | Lattice spacing, site index, unit lattice vector in the direction $\mu$ |
| $\tilde{Ξ}_{\mathrm{sp}}$ | The field, an element of $\mathbb{B}$; $\tilde{Ξ}_{\mathrm{sp}}$ its four-component coordinate column |
| $\tilde\nabla_\Phi$, $(\tilde\nabla_\Phi)^{\natural}$, $\Box$ | The biquaternionic gradient, its quaternion conjugate and the d'Alembertian, of *Operator and Calculus Conventions* |
| $\tilde\nabla^{L}$, $D_\mu$ | The lattice gradient $\sum_\mu e_\mu D_\mu$ and the symmetric difference replacing $\partial/\partial R_\mu$ |
| $\tilde K_{\Phi}(p)$ | The element symbol of the lattice gradient, $a^{-1}\sum_\mu\sin(p_\mu a)e_\mu$; the symbol of $\tilde\nabla^{L}$ is $i\tilde K_{\Phi}(p)$ |
| $\xi$ | The chirality, $\xi\tilde Q=-i\tilde Q\vec e_z$, of spectrum $+1,+1,-1,-1$ |
| $\tilde{Ξ}_{\mathrm{sp},L}$, $\tilde{Ξ}_{\mathrm{sp},R}$ | The two values of the chirality subscript; these letters label chirality, not the multiplications $L_b$ and $R_b$ |
| $S_F^L$ | Naive lattice fermion action |
| $\mathcal S(p)$ | Naive lattice propagator in the chiral-block form; its scalar denominator is the single-column propagator's |
| $\pi_A$ | The sixteen sign patterns with entries $0$ or $\pi$ |
| $D$ | Lattice Dirac operator of the Ginsparg–Wilson relation |
| $\omega(\vec p)$ | Lattice dispersion relation |
| $F(x,y)$, $F_\mu(k)$ | Lattice kernel and its Fourier transform (vector field on the zone) |
| $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{\Phi}$ | The Hermitian and anti-Hermitian sectors, $\mathbb{B}=\mathbb{B}_{\Psi}\oplus\mathbb{B}_{\Phi}$, with $i\,\mathbb{B}_{\Psi}=\mathbb{B}_{\Phi}$ |

## Further Reading

- H. B. Nielsen and M. Ninomiya, "Absence of neutrinos on a lattice (I): proof by homotopy theory," *Nuclear Physics B* **185** (1981) 20–40, and "(II): intuitive topological proof," *Nuclear Physics B* **193** (1981) 173–194, for the original theorem.
- H. B. Nielsen and M. Ninomiya, "A no-go theorem for regularizing chiral fermions," *Physics Letters B* **105** (1981) 219–223, for the general-regularization version.
- D. Friedan, "A proof of the Nielsen–Ninomiya theorem," *Communications in Mathematical Physics* **85** (1982) 481–490, for the differential-geometric proof.
- L. H. Karsten, "Lattice fermions in Euclidean space-time," *Physics Letters B* **104** (1981) 315–319, for the Euclidean statement.
- K. G. Wilson, "Confinement of quarks," *Physical Review D* **10** (1974) 2445–2459, and P. H. Ginsparg and K. G. Wilson, "A remnant of chiral symmetry on the lattice," *Physical Review D* **25** (1982) 2649–2657, for Wilson and Ginsparg–Wilson fermions.
- H. Neuberger, "Exactly massless quarks on the lattice," *Physics Letters B* **417** (1998) 141–144, for overlap fermions.
- D. B. Kaplan, "A method for simulating chiral fermions on the lattice," *Physics Letters B* **288** (1992) 342–347, and Y. Shamir, "Chiral fermions from lattice boundaries," *Nuclear Physics B* **406** (1993) 90–106, for domain-wall fermions.
- J. Kogut and L. Susskind, "Hamiltonian formulation of Wilson's lattice gauge theories," *Physical Review D* **11** (1975) 395–408, for staggered fermions.
- P. Becher and H. Joos, "The Dirac–Kähler equation and fermions on the lattice," *Zeitschrift für Physik C* **15** (1982) 343–365, for the simplicial discretization and its equivalence to staggered fermions.
- I. Montvay and G. Münster, *Quantum Fields on a Lattice* (Cambridge University Press, 1994), and C. Gattringer and C. B. Lang, *Quantum Chromodynamics on the Lattice* (Springer, 2010), for textbook treatments.
- The companion articles of this series: [The Dirac–Kähler Equation](../articles_maths/the-dirac-kahler-equation.html), [Dirac Matter: Graphene, Dirac Cones and Topological Insulators in Biquaternionic Form](dirac-matter-graphene-dirac-cones-and-topological-insulators-in-biquaternionic-form.html), and [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html).
