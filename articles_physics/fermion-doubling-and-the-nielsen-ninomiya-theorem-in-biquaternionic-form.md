# __Fermion Doubling and the Nielsen–Ninomiya Theorem in Biquaternionic Form__

## Introduction

Putting a single Dirac fermion on a lattice produces more than one fermion. The naive discretization of the Dirac action in $d$ Euclidean dimensions yields $2^d$ identical species — sixteen in four dimensions — called **tastes** of the fermion. The extra states are **doublers**, and they are not an artefact of one careless choice of difference operator: the **Nielsen–Ninomiya theorem** states that under very general assumptions no lattice regularization of chiral fermions can avoid an equal number of left- and right-handed species, so a chiral gauge theory cannot be discretized on a lattice without violating one of the assumptions. The obstruction is one of the sharpest in lattice field theory, and it is the reason lattice QCD uses modified fermions — Wilson, staggered, Ginsparg–Wilson, domain-wall, overlap, twisted-mass — each of which evades the theorem by giving up one of its hypotheses.

This article treats fermion doubling in the biquaternion framework. The framework's honest contribution here is again a **negative** one, and it should be stated first: the biquaternion Dirac equation does **not** evade Nielsen–Ninomiya. If a lattice is imposed on the biquaternion gradient, the doubling argument applies unchanged, because the argument uses only locality, hermiticity, translation invariance and the oddness of the massless symbol about the origin — properties that the discretized biquaternion gradient shares with the standard one. The algebra is not a lattice, and it does not supply one. What the framework can do is state the obstruction in its own variables, and — this is the one positive structural point — its multivector, Clifford-algebraic form of the Dirac field puts it naturally close to the **Dirac–Kähler** equation, whose simplicial discretization is exactly the staggered fermion, a lattice formulation whose doublers are reduced but not removed.

The article is organised as follows. The next section sets up the naive discretization, its propagator and its doublers. The third presents the taste-exchange symmetry. The fourth states the Nielsen–Ninomiya theorem and the index-theoretic idea of its proof. The fifth surveys the resolutions and what each one sacrifices. The sixth gives the biquaternion reading: discretization of the biquaternion gradient, the density of states on the Brillouin zone, the relation to Dirac–Kähler and staggered fermions, and the framework's index-theorem connection. The closing sections are the open questions, the summary, the notation table and the literature.

## Naive Discretization

### The classical action and the lattice

In Euclidean spacetime the free continuum Dirac action is

$$
S_F[\psi,\bar\psi] = \int d^4x\;\bar\psi(x)\left(\gamma^\mu\partial_\mu + m\right)\psi(x).
$$

Introduce a lattice of spacing $a$ whose sites are indexed by integer vectors $n = (n_1,n_2,n_3,n_4)$; the fields become Grassmann variables $\psi_n$, $\bar\psi_n$ at each site, and the derivative is replaced by the **symmetric difference**

$$
\partial_\mu\psi \;\longrightarrow\; \frac{\psi_{n+\hat\mu} - \psi_{n-\hat\mu}}{2a}.
$$

The naive action is then

$$
S_F^L[\psi,\bar\psi] = a^4\sum_n \bar\psi_n\left(\sum_{\mu=1}^{4}\gamma_\mu\frac{\psi_{n+\hat\mu}-\psi_{n-\hat\mu}}{2a} + m\psi_n\right),
$$

which reduces to the continuum action as $a\to0$. It therefore looks like a theory of a single fermion. It is not.

### The propagator and the doubler poles

The lattice propagator following from this action is

$$
S(p) = \frac{m - i\,a^{-1}\sum_\mu\gamma_\mu\sin(p^\mu a)}{m^2 + a^{-2}\sum_\mu\sin^2(p^\mu a)}.
$$

The denominator vanishes when $\sin(p^\mu a) = 0$ for every $\mu$ and $\sum_\mu\sin^2(p^\mu a) = -m^2a^2$, that is, at the points

$$
ap^\mu = (am,0,0,0) + \pi_A^\mu,
$$

where the sixteen vectors $\pi_A$ have entries $0$ or $\pi$. There is the expected pole near the origin, and there are **fifteen additional poles** at the corners of the Brillouin zone. Each is a distinct fermion species. The mechanism is the $\sin(p^\mu a)$ symbol: unlike the bosonic case, where the symbol is built from $\sin(p^\mu a/2)$ and has a single zero per period, $\sin(p^\mu a)$ has two zeros over $p^\mu\in[-\pi/a,\pi/a]$.

The doubling also shows in the dispersion relation: inverting the Wick rotation at the pole gives

$$
\sinh\omega(\mathbf p) = \sqrt{m^2 + \sum_{j=1}^3\sin^2 p_j},
$$

whose zeros are the local minima about which the species live — eight from the three spatial directions, and the remaining eight from the Euclidean temporal direction, which is recovered not by a naive $p_4 = \pm i\omega$ but by the full contour integration. The free continuum massless propagator is proportional to $\gamma_\mu p^\mu$, an **odd** function of $p$; a propagator that is local, continuous and periodic must therefore cross zero again, which is the corner pole. Scalar bosons escape because their symbol is even about the origin.

### The taste-exchange symmetry

The naive action carries a symmetry absent from the continuum: for each of the sixteen sign patterns $\pi_A$ there is a transformation

$$
\psi_n \;\to\; e^{-in\cdot\pi_A}\,S_A\,\psi_n,
\qquad
\bar\psi_n \;\to\; \bar\psi_n\,S_A^\dagger\,e^{in\cdot\pi_A},
\qquad
S_0 = I,\quad S_\nu = i\gamma_5\gamma_\nu ,
$$

with $S_A$ the product of the $S_\nu$ over the indices in $A$. Fourier transforming shows that this shifts the momentum by $\pi_A$ and flips the signs of a subset of the gamma matrices, $(\gamma_1,\gamma_2,\gamma_3,\gamma_4)\to(\pm\gamma_1,\pm\gamma_2,\pm\gamma_3,\pm\gamma_4)$, which is still a representation of the Dirac algebra. The transformation therefore exchanges the tastes; since it is a symmetry of the action, the tastes are physically indistinguishable. In an interacting theory they cannot even be ignored, because momentum is conserved only modulo $2\pi/a$: two $\pi_0$-taste fermions can scatter through a highly virtual gauge boson into two $\pi_1$-taste fermions.

## The Nielsen–Ninomiya Theorem

### Statement and assumptions

The **Nielsen–Ninomiya theorem** (1981) is the no-go theorem behind the doubling. In its Hamiltonian form, consider a theory with Hamiltonian $H = \sum_{x,y}\psi^\dagger(x)F(x,y)\psi(y)$ and a charge $Q$. Then there are equal numbers of left-handed and right-handed fermions for every set of charges, provided:

- **translational invariance**, so that $F(x,y) = F(x-y)$;
- **locality**, meaning $F(x-y)$ decays fast enough that its Fourier transform has continuous derivatives;
- **hermiticity**, $F(x) = F(x)^\dagger$;
- a **local, quantized, exactly conserved charge**.

The theorem also has a Euclidean form for an action $S=\sum_{x,y,\mu}\bar\psi(x)i\gamma_\mu F_\mu(x,y)P_R\psi(y)$ under translation invariance, hermiticity ($F_\mu(-x)=F_\mu(x)^*$) and locality. A general version extends the statement to *all* regularization schemes: no regularized chiral fermion theory can simultaneously have the correct global symmetry, unequal numbers of left- and right-handed Weyl species, the correct chiral anomaly, and an action bilinear in the Weyl fields. One consequence is that the Standard Model cannot be put on a lattice without violating one of these conditions; another is that a chirally invariant regularization makes the chiral anomaly vanish, which is wrong. The theorem does not say *how many* doublers appear — only that at least one partner is forced. When chiral fermions do not exist — odd dimensions — the theorem is vacuous, since there is no chirality operator anticommuting with all gamma matrices.

### The proof idea

The Euclidean proof uses the **Poincaré–Hopf theorem**. Locality makes the Fourier transform of the inverse propagator, $F_\mu(k)$, a continuous vector field on the Brillouin zone. Its isolated zeros are the particle species, and around each zero the field is either a source/sink or a saddle, with the **index** of the vector field equal to $\pm 1$; the two signs correspond to left- and right-handedness. Poincaré–Hopf says the sum of the indices equals the Euler characteristic of the manifold the field lives on. The Brillouin zone is topologically a four-torus, whose Euler characteristic is **zero**. Hence the numbers of left- and right-handed species are equal, and the doublers are unavoidable.

## Resolutions and What Each One Sacrifices

Every lattice fermion formulation must violate at least one hypothesis of the theorem. The main routes are:

- **Wilson fermions** add a term proportional to the second difference, which gives the doublers a mass of order $1/a$ and removes them from the low-energy theory, at the cost of explicitly breaking chiral symmetry.
- **Ginsparg–Wilson fermions** satisfy a remnant of chiral symmetry on the lattice, in which $\{\gamma_5,D\}$ is replaced by $aD\gamma_5 D$; the **overlap** fermions realize this with an exactly massless, index-carrying operator. Chiral symmetry is again explicitly broken, but a modified version survives.
- **Domain-wall fermions** place chiral fermions on the boundaries of an extra dimension; chiral symmetry is broken explicitly and the dimensionality increased.
- **Staggered (Kogut–Susskind) fermions** reduce the number of doublers from sixteen to four by spreading the spinor components over the lattice and breaking translation invariance at the lattice-spacing level.
- **Twisted-mass fermions** add a chirally twisted mass term, again explicitly breaking chiral symmetry.
- **Symmetric mass generation** is a non-perturbative interacting route that gaps the mirror fermions without breaking the symmetries, evading the bilinear assumption.
- **Non-local formulations** (perfect, SLAC, Stacey fermions) use a discontinuous propagator and are non-local.
- **One-sided difference operators** (forward or backward) avoid doubling because they are non-hermitian and so violate the theorem's hermiticity assumption; the resulting interacting theory is non-covariant and hard to renormalize, and is not used in practice.

The theorems that survive all of this are the ones with experimental consequences: the correct anomaly structure in lattice QCD, and the impossibility of a chirally invariant lattice discretization of a chiral gauge theory.

## The Biquaternion Reading

### Discretizing the biquaternion gradient

The framework's gradient is $\tilde\nabla = e_0\partial_{ict} + e_1\partial_x + e_2\partial_y + e_3\partial_z$. A lattice discretization replaces each partial derivative by a difference operator. If the symmetric difference is used, the Fourier symbol of $\partial_\mu$ is $i\sin(p^\mu a)/a$ in each direction, and the biquaternion gradient acquires the symbol

$$
\tilde\nabla \;\longrightarrow\; e_\mu\,\frac{i\sin(p^\mu a)}{a},
$$

acting on plane waves on the lattice. The denominator of the lattice propagator is then built from $\sum_\mu\sin^2(p^\mu a)$, which has the sixteen zeros identified above.

### The doubling is a property of the difference operator, not of the algebra

This is the article's central negative statement. Nothing in the derivation of the doublers uses the biquaternion structure: it uses (i) locality, (ii) hermiticity of the difference operator, (iii) translation invariance, and (iv) the oddness about $p=0$ of the massless symbol. The discretized biquaternion gradient satisfies all four exactly as the standard one does. **Therefore the biquaternion Dirac equation suffers fermion doubling on any lattice satisfying the theorem's hypotheses, and the framework offers no evasion of Nielsen–Ninomiya.** A claim to the contrary would be false: the algebra is a continuum algebra; it is not a lattice, and it does not supply a non-local or non-hermitian difference operator either. The companion article on Dirac matter faces the mirror-image fact, that the algebra is indifferent to the lattice that sits on top of it.

### Dirac–Kähler and staggered fermions

The one positive structural point is a proximity, not a solution. The biquaternion field, viewed as a Clifford-algebra element, is a **multivector**, and the multivector Dirac equation is the **Dirac–Kähler equation** of the companion mathematical article. The Dirac–Kähler equation has a natural discretization on a simplicial complex, replacing the exterior derivative and codifferential by the boundary and coboundary operators, and that discretization is equivalent to the **staggered fermion** formulation — a change of basis maps one to the other. Staggered fermions do not remove doubling; they reduce the sixteen tastes to four and preserve a remnant symmetry. So the framework's multivector form places it naturally in the family of lattice formulations that *mitigate* doubling, and not in the family that evades it. This is a genuine structural statement: it says which mitigation is the framework-natural one, not that the framework solves the problem.

### Index-theoretic connections

Two index-theoretic facts touch the framework through its companion articles. First, the anomalous half-integer quantum Hall effect of graphene — the $\tfrac12$ offset of the companion Dirac-matter article — is a consequence of the Atiyah–Singer index theorem applied to the massless Dirac operator in a magnetic field: a Landau level sits exactly at the Dirac point, half-filled in neutral graphene. Second, the Dirac–Kähler operator's zero modes on a compact manifold are the harmonic forms, guaranteed to exist whenever the relevant Betti numbers do not vanish, unlike the Dirac operator, which has no zero modes on a positively curved manifold. Both are statements about the analytic index of a Dirac-type operator. The framework's equation is one more Dirac-type operator in this family, and its index is expected to behave accordingly; the corpus has not computed it.

### What the framework supplies and what it does not

The framework supplies a continuum equation and a multivector structure whose natural discretization is the staggered one. It does **not** supply a lattice, a chirally invariant lattice formulation, a resolution of the doubling, or any modification of the Nielsen–Ninomiya theorem. The theorem is a statement about local, hermitian, translation-invariant lattice bilinears; the biquaternion algebra is none of those things and does not alter the conclusion when one is imposed.

## Open Questions

1. **The index of the biquaternion Dirac operator.** The companion Dirac–Kähler article gives the zero modes of the multivector Dirac operator as harmonic forms. What is the corresponding statement for the biquaternion gradient $\tilde\nabla$, and does the $\mathbb M_\pm$ split organize the index?

2. **The lattice imposition.** Is there a lattice that the framework's structure selects among the many possible ones, in the way that the multivector form selects simplicial/staggered? This article argues only for the *proximity* to staggered; a derivation is not attempted.

3. **Anomaly matching.** The general Nielsen–Ninomiya statement involves the correct chiral anomaly. The framework's anomaly treatment — does it have one, and is it the standard bilinear one? — is not in the corpus and is the sharpest open point.

4. **Odd dimensions.** The theorem is vacuous in odd dimensions. Does the framework's dimension-independence (the algebra is defined for any $d$) have anything to say about the chirality-free odd-dimensional case, or is that a pure lattice statement?

5. **Symmetric mass generation.** This resolution evades the bilinear assumption by interactions. Whether the framework's sector structure can express the gapping of mirror fermions is open.

6. **Empirical contact.** As everywhere, the doubling is a lattice artefact without continuum signature; any framework-level claim must respect that.

## Summary

Naive discretization of the Dirac action on a $d$-dimensional lattice gives $2^d$ tastes — sixteen in four dimensions — because the difference operator's symbol $\sin(p^\mu a)$ has two zeros per period. The doublers appear as extra poles of the propagator at the Brillouin-zone corners, are related by the taste-exchange symmetry $S_\nu = i\gamma_5\gamma_\nu$, and are physically indistinguishable, so an interacting lattice theory cannot ignore them. The Nielsen–Ninomiya theorem states the obstruction: a local, hermitian, translation-invariant lattice bilinear has equal numbers of left- and right-handed species; the Euclidean proof is a Poincaré–Hopf index count on the Brillouin-zone torus, whose Euler characteristic vanishes. Every resolution — Wilson, staggered, Ginsparg–Wilson, overlap, domain-wall, twisted-mass, symmetric mass generation, non-local, one-sided — violates one hypothesis of the theorem.

The biquaternion framework does not evade the obstruction. The doubling argument uses only locality, hermiticity, translation invariance and the oddness of the massless symbol, all of which the discretized biquaternion gradient shares; the algebra is not a lattice and supplies no alternative difference operator. The one positive structural point is that the framework's multivector field places its natural discretization with the **Dirac–Kähler** equation, whose simplicial form is the **staggered fermion** formulation — a mitigation, not a solution. Two index-theoretic facts reach the framework as companions: the anomalous half-integer quantum Hall effect of graphene and the harmonic-form zero modes of the Dirac–Kähler operator.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $a$, $n$, $\hat\mu$ | Lattice spacing, site index, unit lattice vector |
| $S_F^L$ | Naive lattice fermion action |
| $\pi_A$ | The sixteen sign patterns with entries $0$ or $\pi$ |
| $S_\nu = i\gamma_5\gamma_\nu$ | Taste-exchange generators, $S_A$ the corresponding products |
| $S(p)$ | Naive lattice propagator |
| $\omega(\mathbf p)$ | Lattice dispersion relation |
| $F(x,y)$, $F_\mu(k)$ | Lattice kernel and its Fourier transform (vector field on the zone) |
| $\tilde\nabla$ | Biquaternionic gradient |
| $\mathbb{M}_\pm$ | Framework sectors |

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
- The companion articles of this series: *The Dirac–Kähler Equation*, *Dirac Matter: Graphene, Dirac Cones and Topological Insulators in Biquaternionic Form*, and *The Dirac Equation in Biquaternionic Form*.
