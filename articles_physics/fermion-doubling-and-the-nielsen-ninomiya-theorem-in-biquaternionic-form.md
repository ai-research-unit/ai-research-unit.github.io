# __Fermion Doubling and the Nielsen–Ninomiya Theorem in Biquaternionic Form__

## Introduction

Putting a single Dirac fermion on a lattice produces more than one fermion. The naive discretization of the Dirac action in $d$ Euclidean dimensions yields $2^d$ identical species — sixteen in four dimensions — called **tastes** of the fermion. The extra states are **doublers**, and they are not an artefact of one careless choice of difference operator: the **Nielsen–Ninomiya theorem** states that under very general assumptions no lattice regularization of chiral fermions can avoid an equal number of left- and right-handed species, so a chiral gauge theory cannot be discretized on a lattice without violating one of the assumptions. The obstruction is one of the sharpest in lattice field theory, and it is the reason lattice QCD uses modified fermions — Wilson, staggered, Ginsparg–Wilson, domain-wall, overlap, twisted-mass — each of which pays a price to the theorem rather than escaping it.

This article treats fermion doubling in the biquaternion framework. The framework's honest contribution here is again a **negative** one, and it should be stated first: the biquaternion Dirac equation does **not** evade Nielsen–Ninomiya. If a lattice is imposed on the biquaternion gradient, the doubling argument applies unchanged, because the argument uses only locality, hermiticity, translation invariance and the oddness of the massless symbol about the origin — properties that the discretized biquaternion gradient shares with the standard one. The algebra is not a lattice, and it does not supply one. What the framework can do is state the obstruction in its own variables, and — this is the one positive structural point — its multivector, Clifford-algebraic form of the Dirac field places it naturally close to the **Dirac–Kähler** equation, whose simplicial discretization is exactly the staggered fermion, a lattice formulation whose doublers are reduced but not removed.

The next section sets up the naive discretization, its propagator and its doublers, and the taste-exchange symmetry. The section after states the Nielsen–Ninomiya theorem and the index-theoretic idea of its proof, then surveys the resolutions and what each one sacrifices. The biquaternion reading follows: the discretization of the biquaternion gradient, the independence of the doubling from the algebra, the relation to Dirac–Kähler and staggered fermions, and the framework's index-theorem connection. The closing sections are the open questions, the gamma formulation, the summary, the notation table and the literature.

## Naive Discretization

### The classical action and the lattice

The biquaternion field lives on the Lorentzian section. In the coordinates $x_0=ct'$, $x_k$, the frame is carried by the cells $L_{a}R_{b}$, with $L_a\psi=a\psi$ and $R_b\psi=\psi b$, so that $L_{a}R_{b}\psi=a\psi b$ and $L_{a}R_{b}L_{c}R_{d}=L_{ac}R_{db}$; the identity is $L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$. Here $i$ is the scalar imaginary, $i^2=-1$. The four Minkowski frame cells $iR_{\vec e_x}^{\mathrm{pau}}$ and $iL_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}$ ($k=1,2,3$) satisfy

$$
(iR_{\vec e_x}^{\mathrm{pau}})^2=L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}},\qquad
(iL_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}})^2=-L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}},\qquad
\{iR_{\vec e_x}^{\mathrm{pau}},iL_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}\}=0,\qquad
\{iL_{\vec e_j}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},iL_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}\}=-2\delta_{jk}L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}},
$$

which are the Clifford relations of $g=\mathrm{diag}(+1,-1,-1,-1)$; the chirality cell is $\chi=-iR_{\vec e_z}^{\mathrm{pau}}$. The biquaternion Dirac equation is the chiral pair

$$
\tilde{\nabla}\tilde{\Psi}_R=m\tilde{\Psi}_L,
\qquad
\tilde{\nabla}^{\natural}\tilde{\Psi}_L=m\tilde{\Psi}_R,
$$

and its spinor-module representative is the single cell equation

$$
(\mathbb{D}-m)\psi=0,\qquad
\mathbb{D}=-R_{\vec e_x}^{\mathrm{pau}}\frac{\partial}{\partial x_0}+\sum_{k=1}^3 L_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}\frac{\partial}{\partial x_k}.
$$

The two lines are the two chiral halves of the field: the gradient $\tilde{\nabla}$ acts on the right-chiral field and its conjugate $\tilde{\nabla}^{\natural}$ on the left-chiral one, and the mass couples them. The transcription of the pair on the spinor module is the single cell equation. At $m=0$ the pair decouples into $\tilde{\nabla}\tilde{\Psi}_R=0$ and $\tilde{\nabla}^{\natural}\tilde{\Psi}_L=0$. The free continuum Dirac action is

$$
S_F[\psi,\bar\psi] = \int d^4x\;\bar\psi(x)\left(\mathbb{D}-m\right)\psi(x)
= \int d^4x\;\bar\psi(x)\left(-R_{\vec e_x}^{\mathrm{pau}}\frac{\partial}{\partial x_0}+\sum_{k=1}^3 L_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}\frac{\partial}{\partial x_k}-m\right)\psi(x).
$$

On the Euclidean section the frame cells are

$$
E_4=iR_{\vec e_x}^{\mathrm{pau}},\qquad E_k=-L_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}\quad(k=1,2,3),
$$

which satisfy $E_\mu^2=L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$ and $\{E_\mu,E_\nu\}=2\delta_{\mu\nu}L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$. These are the Wick-rotated frame cells, a change of frame and not a change of algebra. With $x_4=ix_0$, so that $\partial/\partial x_0=i\partial/\partial x_4$, the cell operator becomes

$$
\mathbb{D}=-R_{\vec e_x}^{\mathrm{pau}}\frac{\partial}{\partial x_0}+\sum_{k=1}^3L_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}\frac{\partial}{\partial x_k}
=-\sum_{\mu=1}^4E_\mu\frac{\partial}{\partial x_\mu},
$$

so $(\mathbb{D}-m)\psi=0$ and $(\sum_\mu E_\mu\partial/\partial x_\mu+m)\psi=0$ are the same equation; the flip of the mass sign is the Wick rotation, not a new convention. The Euclidean chirality is $iR_{\vec e_z}^{\mathrm{pau}}=E_4E_1E_2E_3$, which is minus the Minkowski chirality cell $-iR_{\vec e_z}^{\mathrm{pau}}$: the four cells anticommute, so reversing their order flips the sign. The Euclidean action is

$$
S^E_F[\psi,\bar\psi] = \int d^4x_E\;\bar\psi(x)\left(\sum_{\mu=1}^4 E_\mu\frac{\partial}{\partial x_\mu} + m\right)\psi(x).
$$

The lattice below discretizes $S^E_F$. In the lattice sections the index $\mu=1,\dots,4$ labels the four Euclidean directions, the fourth temporal; the doubling theorem is a statement about the symbol and does not depend on the signature.

Introduce a lattice of spacing $a$ whose sites are indexed by integer vectors $n = (n_1,n_2,n_3,n_4)$; the fields become Grassmann variables $\psi_n$, $\bar\psi_n$ at each site, and the derivative is replaced by the **symmetric difference**

$$
\partial^E/\partial x_\mu\psi \;\longrightarrow\; \frac{\psi_{n+\vec u_\mu} - \psi_{n-\vec u_\mu}}{2a}.
$$

The naive action is then

$$
S_F^L[\psi,\bar\psi] = a^4\sum_n \bar\psi_n\left(\sum_{\mu=1}^{4}\,E_\mu\frac{\psi_{n+\vec u_\mu}-\psi_{n-\vec u_\mu}}{2a} + m\psi_n\right),
$$

which reduces to $S^E_F$ as $a\to0$. It therefore looks like a theory of a single fermion. It is not.

### The propagator and the doubler poles

The lattice propagator following from this action is

$$
\boxed{\;S(p) = \frac{m - i\,a^{-1}\sum_{\mu=1}^4 E_\mu\sin(p_\mu a)}{m^2 + a^{-2}\sum_{\mu=1}^4\sin^2(p_\mu a)}\;}.
$$

The kinetic denominator vanishes at $m=0$ when $\sin(p_\mu a) = 0$ for every $\mu$, that is, at the points

$$
\boxed{\;a p_\mu = \pi_{A\mu}\;},
$$

where the sixteen vectors $\pi_A$ have entries $0$ or $\pi$. Taking the zone as $[0,2\pi/a)^4$, these sixteen points are its corners: one is the origin, the other **fifteen are the doublers**, and each is a distinct fermion species. For $m\ne0$ the denominator is bounded below by $m^2$ on the real zone, so no pole lies there at all; all sixteen species reappear as $m\to0$. The mechanism is the symbol: over one period of length $2\pi/a$, $\sin(p_\mu a)$ has two zeros, at $p_\mu=0$ and $p_\mu=\pi/a$, whereas the bosonic symbol built from $\sin(p_\mu a/2)$ has one.

The doubling also shows in the dispersion relation. In lattice units $a=1$, the pole condition with $p_4=i\omega$ gives

$$
\sinh^2\omega(\vec p) = m^2 + \sum_{k=1}^3\sin^2 p_k .
$$

Its minima sit at the zeros of the spatial sines, eight in all. The temporal direction doubles each of them: $\sin^2(p_4a)$ has period $\pi/a$, so $p_4=0$ and $p_4=\pi/a$ give the same branch, and the sixteen poles are the eight spatial corners times the two temporal choices.

The same count follows from the symbol alone. At $m=0$ the inverse propagator is

$$
S(p)^{-1}=i\sum_{\mu=1}^4 E_\mu\frac{\sin(p_\mu a)}{a},
$$

an **odd** periodic function of $p$. Each of the sixteen points $\pi_A/a$ equals its own negative modulo $2\pi/a$, so oddness forces the symbol to vanish at all sixteen: a lone zero at the origin is impossible. A scalar boson escapes, because its symbol $\sin(p_\mu a/2)$ is even about the origin.

### The taste-exchange symmetry

The naive action carries a symmetry absent from the continuum: for each of the sixteen sign patterns $\pi_A$ there is a transformation

$$
\boxed{\;\psi_n \;\to\; \exp(-i\,n\cdot\pi_A)\,S_A\,\psi_n,
\qquad
\bar\psi_n \;\to\; \bar\psi_n\,S_A^\dagger\,\exp(i\,n\cdot\pi_A),
\qquad
S_0 = L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}},\quad S_\nu = iR_{\vec e_z}^{\mathrm{pau}}E_\nu\;},
$$

with $S_A$ the product of the $S_\nu$ over the indices in $A$; the lattice must be of even extent in each direction, so that the phase is single-valued. Conjugating a frame cell by $S_A$ flips its sign exactly for $\mu\in A$,

$$
S_A^\dagger E_\mu S_A=(-1)^{\delta_{\mu\in A}}E_\mu ,
$$

which is still a representation of the Clifford algebra. Fourier transforming shows that the transformation shifts the momentum by $\pi_A$ and leaves the action unchanged. The sixteen tastes are therefore exactly degenerate in the free theory. They cannot be discarded in an interacting theory: the lattice conserves momentum only modulo $2\pi/a$, so a hard virtual gauge boson can transfer $\pi/a$ and connect the tastes.

## The Nielsen–Ninomiya Theorem

### Statement and assumptions

The **Nielsen–Ninomiya theorem** (1981) is the no-go theorem behind the doubling. In its Hamiltonian form, consider a theory with Hamiltonian $H = \sum_{x,y}\psi^\dagger(x)F(x,y)\psi(y)$ and a charge $Q$. Then there are equal numbers of left-handed and right-handed fermions for every set of charges, provided:

- **translational invariance**, so that $F(x,y) = F(x-y)$;
- **locality**, meaning $F(x-y)$ decays fast enough that its Fourier transform has continuous derivatives;
- **hermiticity**, $F(x)^\dagger = F(-x)$;
- a **local, quantized, exactly conserved charge**.

The theorem also has a Euclidean form for an action

$$
S=\sum_{x,y,\mu}\bar\psi(x)\,E_\mu F_\mu(x,y)P_R\psi(y),
$$

under translation invariance, hermiticity ($F_\mu(-x)=F_\mu(x)^\dagger$) and locality; here $P_R=\tfrac12(L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}-iR_{\vec e_z}^{\mathrm{pau}})$ is the right-chiral projector, the projector on the $+1$ eigenvalue of the chirality cell $-iR_{\vec e_z}^{\mathrm{pau}}$, and $P_L=\tfrac12(L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}+iR_{\vec e_z}^{\mathrm{pau}})$ is the left-chiral one. A general version extends the statement to *all* regularization schemes: no regularized chiral fermion theory can simultaneously have the correct global symmetry, unequal numbers of left- and right-handed Weyl species, the correct chiral anomaly, and an action bilinear in the Weyl fields. One consequence is that the Standard Model cannot be put on a lattice without violating one of these conditions; another is that a chirally invariant regularization makes the chiral anomaly vanish, which is wrong. The theorem does not say *how many* doublers appear — only that at least one partner is forced. When chiral fermions do not exist — odd dimensions — the theorem is vacuous, since there is no chirality operator anticommuting with all the frame generators.

### The proof idea

The Euclidean proof uses the **Poincaré–Hopf theorem**. Locality makes the Fourier transform of the kernel, $F_\mu(k)$, a continuous vector field on the Brillouin zone; it is the inverse propagator. Its isolated zeros are the particle species, and around each zero the field is either a source/sink or a saddle, with the **index** of the vector field equal to $\pm 1$; the two signs correspond to left- and right-handedness. Poincaré–Hopf says the sum of the indices equals the Euler characteristic of the manifold the field lives on. The Brillouin zone is topologically a four-torus, whose Euler characteristic is **zero**. Hence the numbers of left- and right-handed species are equal, and the doublers are unavoidable.

## Resolutions and What Each One Sacrifices

Every lattice fermion formulation must give up at least one hypothesis of the theorem, or the bilinear form of the action that carries them. The main routes are:

- **Wilson fermions** add a term proportional to the second difference, which gives the doublers a mass of order $1/a$ and removes them from the low-energy theory, at the cost of explicitly breaking chiral symmetry.
- **Ginsparg–Wilson fermions** satisfy a remnant of chiral symmetry on the lattice, $\{D,\chi\}=a\,D\chi D$ with $D$ the lattice Dirac operator and $\chi=-iR_{\vec e_z}^{\mathrm{pau}}$, in place of the continuum anticommutator $\{D,\chi\}=0$; the **overlap** fermions realize this with an exactly massless, index-carrying operator. Chiral symmetry is not broken explicitly; it is realized in this modified form.
- **Domain-wall fermions** place chiral fermions on the boundaries of an extra dimension; the bulk mass term breaks chiral symmetry explicitly, but the boundary mode's chiral symmetry is restored as the extra dimension grows, and the price is the extra dimension.
- **Staggered (Kogut–Susskind) fermions** reduce the sixteen tastes to four by distributing the four spinor components over the sites of a hypercube, which leaves only a discrete remnant of the translation symmetry.
- **Twisted-mass Wilson fermions** add a chirally twisted mass term; the Wilson term removes the doublers, and the twist protects a remnant of chiral symmetry.
- **Symmetric mass generation** is a non-perturbative interacting route that gaps the mirror fermions without breaking the symmetries, evading the bilinear assumption.
- **Non-local formulations** (perfect, SLAC, Stacey fermions) use a discontinuous propagator and are non-local.
- **One-sided difference operators** (forward or backward) avoid doubling because they are non-hermitian and so violate the theorem's hermiticity assumption; the resulting interacting theory is non-covariant and hard to renormalize, and is not used in practice.

What survives all of this is the part with experimental consequences: the correct anomaly structure in lattice QCD, and the impossibility of a chirally invariant lattice discretization of a chiral gauge theory.

## The Biquaternion Reading

### Discretizing the biquaternion gradient

The framework's gradient is $\tilde{\nabla} = e_t\partial/\partial Q_t + \vec e_x\partial/\partial Q_x + \vec e_y\partial/\partial Q_y + \vec e_z\partial/\partial Q_z$. A lattice discretization replaces each partial derivative by a difference operator. If the symmetric difference is used, the Fourier symbol of $\partial/\partial Q_\mu$ is $i\sin(p_\mu a)/a$ in each direction, and on plane waves the biquaternion gradient acquires the symbol

$$
\boxed{\;\tilde{\nabla} \;\longrightarrow\; e_t\,\frac{i\sin(p_ta)}{a}+\sum_{k=x,y,z}\vec e_k\,\frac{i\sin(p_ka)}{a}\;}.
$$

The denominator of the lattice propagator is then built from $\sum_\mu\sin^2(p_\mu a)$, which has the sixteen zeros identified above.

### The doubling is a property of the difference operator, not of the algebra

This is the article's central negative statement. Nothing in the derivation of the doublers uses the biquaternion structure: it uses (a) locality, (b) hermiticity of the difference operator, (c) translation invariance, and (d) the oddness about $p=0$ of the massless symbol. The discretized biquaternion gradient satisfies all four exactly as the standard one does. **Therefore the biquaternion Dirac equation suffers fermion doubling on any lattice satisfying the theorem's hypotheses, and the framework offers no evasion of Nielsen–Ninomiya.** A claim to the contrary would be false: the algebra is a continuum algebra; it is not a lattice, and it does not supply a non-local or non-hermitian difference operator either. The companion article on Dirac matter faces the mirror-image fact, that the algebra is indifferent to the lattice that sits on top of it.

### Dirac–Kähler and staggered fermions

The one positive structural point is a proximity, not a solution. The biquaternion algebra is the even part of the real Clifford algebra $\mathrm{Cl}_{1,3}(\mathbb{R})$, $\mathrm{Cl}^{+}_{1,3}(\mathbb{R})\cong M_2(\mathbb{C})\cong\mathbb{H}\otimes\mathbb{C}$, and the biquaternion field sits in the even part of a **Dirac–Kähler** multivector, the field of the companion mathematical article. The Dirac–Kähler equation is the multivector equation; its operator is odd and couples the even and odd parts, so it does not restrict to the biquaternion field. The relation is therefore containment, not identity. What the containment gives is the natural discretization: on a simplicial complex the Dirac–Kähler equation becomes the **staggered fermion** formulation, and the even part is the framework's field. Staggered fermions do not remove doubling; they reduce the sixteen tastes to four and preserve a remnant symmetry. So the framework's multivector form places it naturally in the family of lattice formulations that *mitigate* doubling, and not in the family that evades it. This is a structural statement about the natural discretization, not a derivation of a lattice for the biquaternion equation.

### Index-theoretic connections

Two index-theoretic facts touch the framework through its companion articles. First, the anomalous half-integer quantum Hall effect of graphene — the $\tfrac12$ offset of the companion Dirac-matter article — is a consequence of the Atiyah–Singer index theorem applied to the massless Dirac operator in a magnetic field: a Landau level sits exactly at the Dirac point, half-filled in neutral graphene. Second, the Dirac–Kähler operator's zero modes on a compact manifold are the harmonic forms, guaranteed to exist whenever the relevant Betti numbers do not vanish, unlike the Dirac operator, which has none when the scalar curvature is positive (Lichnerowicz). Both are statements about the analytic index of a Dirac-type operator. The framework's equation is one more Dirac-type operator in this family, and its index is expected to behave accordingly; the corpus has not computed it.

### What the framework supplies and what it does not

The framework supplies a continuum equation and a multivector structure whose natural discretization is the staggered one. It does **not** supply a lattice, a chirally invariant lattice formulation, a resolution of the doubling, or any modification of the Nielsen–Ninomiya theorem. The theorem is a statement about local, hermitian, translation-invariant lattice bilinears, and the biquaternion algebra says nothing about any of those properties; imposing a lattice on it puts it under the theorem, not beside it.

## Open Questions

1. **The index of the biquaternion Dirac operator.** The companion Dirac–Kähler article gives the zero modes of the multivector Dirac operator as harmonic forms. What is the corresponding statement for the biquaternion gradient $\tilde{\nabla}$, and does the $\mathbb{M}_\pm$ split organize the index?

2. **The lattice imposition.** Is there a lattice that the framework's structure selects among the many possible ones, in the way that the multivector form selects simplicial/staggered? This article argues only for the *proximity* to staggered; a derivation is not attempted.

3. **Anomaly matching.** The general Nielsen–Ninomiya statement involves the correct chiral anomaly. The framework's anomaly treatment — does it have one, and is it the standard bilinear one? — is not in the corpus and is the sharpest open point.

4. **Odd dimensions.** The theorem is vacuous in odd dimensions. Does the framework's dimension-independence (the algebra is defined for any $d$) have anything to say about the chirality-free odd-dimensional case, or is that a pure lattice statement?

5. **Symmetric mass generation.** This resolution evades the bilinear assumption by interactions. Whether the framework's sector structure can express the gapping of mirror fermions is open.

6. **Empirical contact.** As everywhere, the doubling is a lattice artefact without continuum signature; any framework-level claim must respect that.

## The Gamma Formulation

The gammas are the frame cells of the body, written as single letters; they form a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra.

Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\psi=a\psi$ and $R_b\psi=\psi b$.

$$
\gamma_0=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\quad \gamma_1=iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_2=iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_3=iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_5=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}} .
$$

The Euclidean frame of the lattice sections is built from these cells, with a factor of $i$ on the three spatial legs:

$$
\gamma^E_4=\gamma_0=iR_{\vec e_x}^{\mathrm{pau}},\qquad
\gamma^E_k=i\gamma_k=-L_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}\quad(k=1,2,3),\qquad
\gamma^E_5=\gamma^E_4\gamma^E_1\gamma^E_2\gamma^E_3=iR_{\vec e_z}^{\mathrm{pau}}.
$$

The four cells anticommute, so moving $\gamma^E_4$ to the right past the other three flips the sign:
$$
\gamma^E_1\gamma^E_2\gamma^E_3\gamma^E_4=-\gamma^E_5=\gamma_5 .
$$
In particular $\gamma^E_5=-\gamma_5$, and a right-chiral projector written with the Euclidean chirality reads $P_R=\tfrac12(I_4-\gamma^E_5)=\tfrac12(I_4+\gamma_5)$.

The sixteen graded products of the five cells — the unit, the four cells, the six products of two, the four products of three and $\gamma_5$ — form a basis of $M_4(\mathbb{C})$, so every two-sided operator is a complex combination of them.

$\gamma_5$ is the reference-frame representative of the chirality operator. The abstract central grading $\chi_{\mathrm{ad}}=i\tilde\Xi_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, with $\chi_{\mathrm{ad}}^2=e_t$ — is a different object; on the Dirac module it is represented by the cell $\chi=-iR_{\vec e_z}^{\mathrm{pau}}=\gamma_5$.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The two Dirac equations.** The chiral pair of the body is a two-sided system:

$$
\tilde{\nabla}\tilde\Psi_R=m\tilde\Psi_L,\qquad
\tilde{\nabla}^{\natural}\tilde\Psi_L=m\tilde\Psi_R .
$$

On the spinor module the pair reduces to the single cell equation $(\mathbb{D}-m)\psi=0$, with $\mathbb{D}=i\gamma\cdot\partial$, the dot product being the metric contraction $\gamma\cdot\partial=\sum_\mu\varepsilon_\mu\gamma_\mu\partial/\partial x_\mu$ and $\varepsilon_\mu=g_{\mu\mu}$; in the letter this is $(i\gamma\cdot\partial-m)\psi=0$. The letter and the cells are the same operator: expanding the metric sum gives back $-R_{\vec e_x}^{\mathrm{pau}}\partial/\partial x_0+\sum_k L_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}\partial/\partial x_k$.

The pair and the cell equation are the same statement in two readings. The two lines of the pair are the two chiral halves of $\psi$: with

$$
P_R=\tfrac12(I_4+\gamma_5),\qquad P_L=\tfrac12(I_4-\gamma_5),\qquad \psi_R=P_R\psi,\qquad \psi_L=P_L\psi,
$$

the projections of the cell equation are

$$
i\gamma\cdot\partial\,\psi_R=m\psi_L,\qquad
i\gamma\cdot\partial\,\psi_L=m\psi_R .
$$

The gradient anticommutes with $\gamma_5$, so it carries each chirality into the other, and the mass couples the two lines. At $m=0$ each line stands alone, $\tilde{\nabla}\tilde\Psi_R=0$ and $\tilde{\nabla}^{\natural}\tilde\Psi_L=0$, and the two chiralities decouple.

**The identities of the frame.** In the $\gamma$ reading the indices run over $\mu=0,1,2,3$, so the lattice direction $\mu=4$ of the previous sections is $\mu=0$ here. With $\epsilon_{0123}=+1$,
$$
\{\gamma_\mu,\gamma_\nu\}=2g_{\mu\nu}I_4,\qquad
(\gamma_k)^2=-I_4,\qquad
\gamma_5^2=I_4,\qquad
\{\gamma_\mu,\gamma_5\}=0,
$$
$$
[\gamma_\mu,\gamma_\nu]=2\gamma_\mu\gamma_\nu\quad(\mu\ne\nu),\qquad
[\gamma_a,\Sigma_{cd}]=g_{ac}\gamma_d-g_{ad}\gamma_c,\qquad
\Sigma_{cd}=\tfrac14[\gamma_c,\gamma_d],
$$
$$
\mathrm{tr}(\gamma_\mu\gamma_\nu)=4g_{\mu\nu},\qquad
\mathrm{tr}(\gamma_5\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)=-4i\,\epsilon_{\mu\nu\rho\sigma},
$$
$$
\mathrm{tr}(\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)
=4\bigl(g_{\mu\nu}g_{\rho\sigma}-g_{\mu\rho}g_{\nu\sigma}+g_{\mu\sigma}g_{\nu\rho}\bigr).
$$
The spin generators are the $S_{cd}$ of *The Gamma Frame and the Complexified Dirac Algebra of $M_4(\mathbb{C})$*, renamed $\Sigma_{cd}$ here because $S_\nu$ and $S_A$ are the taste generators.

The four contraction sums follow from the Clifford relations. In the Euclidean frame, where every cell squares to $+I_4$, every $\gamma$ in these sums is read as its Euclidean cell $\gamma^E$,
$$
\sum_\mu\gamma_\mu\gamma_\mu=4I_4,\qquad
\sum_\mu\gamma_\mu\gamma_\alpha\gamma_\mu=-2\gamma_\alpha,\qquad
\sum_\mu\gamma_\mu\gamma_\alpha\gamma_\beta\gamma_\mu=4\delta_{\alpha\beta}I_4,
$$
and, for distinct $\alpha,\beta,\gamma$,
$$
\sum_\mu\gamma_\mu\gamma_\alpha\gamma_\beta\gamma_\gamma\gamma_\mu=2\gamma_\alpha\gamma_\beta\gamma_\gamma .
$$
In the $\mathbb{M}_-$ frame the metric enters and $\sum_\mu\gamma_\mu\gamma_\mu=-2I_4$.

## Summary

Naive discretization of the Dirac action on a $d$-dimensional lattice gives $2^d$ tastes — sixteen in four dimensions — because the difference operator's symbol $\sin(p_\mu a)$ has two zeros per period. The doublers appear as extra poles of the propagator at the Brillouin-zone corners, are related by the taste-exchange symmetry $S_\nu=iR_{\vec e_z}^{\mathrm{pau}}E_\nu$, and are exactly degenerate in the free theory, so an interacting lattice theory cannot simply drop them. The Nielsen–Ninomiya theorem states the obstruction: a local, hermitian, translation-invariant lattice bilinear has equal numbers of left- and right-handed species; the Euclidean proof is a Poincaré–Hopf index count on the Brillouin-zone torus, whose Euler characteristic vanishes. Every resolution — Wilson, staggered, Ginsparg–Wilson, overlap, domain-wall, twisted-mass, symmetric mass generation, non-local, one-sided — gives up one of the theorem's hypotheses, and symmetric mass generation gives up the bilinear form of the action rather than a hypothesis.

The biquaternion framework does not evade the obstruction. The doubling argument uses only locality, hermiticity, translation invariance and the oddness of the massless symbol, all of which the discretized biquaternion gradient shares; the algebra is not a lattice and supplies no alternative difference operator. The one positive structural point is that the framework's multivector field is contained in the **Dirac–Kähler** multivector, whose simplicial discretization is the **staggered fermion** formulation — a mitigation, not a solution. Two index-theoretic facts reach the framework as companions: the anomalous half-integer quantum Hall effect of graphene and the harmonic-form zero modes of the Dirac–Kähler operator.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $a$, $n$, $\vec u_\mu$ | Lattice spacing, site index, unit lattice vector in the direction $\mu$ |
| $S_F^L$ | Naive lattice fermion action |
| $L_{a}R_{b}$ | Frame cells, $L_a\psi=a\psi$, $R_b\psi=\psi b$, $L_{a}R_{b}\psi=a\psi b$; identity $L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$ |
| $iR_{\vec e_x}^{\mathrm{pau}}$, $iL_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}$ | Minkowski frame cells; $(iR_{\vec e_x}^{\mathrm{pau}})^2=+L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$, $(iL_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}})^2=-L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$ |
| $\chi=-iR_{\vec e_z}^{\mathrm{pau}}$ | Minkowski chirality cell; $\chi^2=L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$ and $\chi$ anticommutes with the four frame cells |
| $\mathbb{D}$ | Cell Dirac operator, $\mathbb{D}=-R_{\vec e_x}^{\mathrm{pau}}\partial/\partial x_0+\sum_k L_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}\partial/\partial x_k$ |
| $E_4=iR_{\vec e_x}^{\mathrm{pau}}$, $E_k=-L_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}$ | Euclidean frame cells; $E_\mu^2=L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$, $\{E_\mu,E_\nu\}=2\delta_{\mu\nu}L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$ |
| $iR_{\vec e_z}^{\mathrm{pau}}$ | Euclidean chirality, $iR_{\vec e_z}^{\mathrm{pau}}=E_4E_1E_2E_3$, the negative of the Minkowski chirality cell |
| $P_R$, $P_L$ | Chiral projectors, $P_{R,L}=\tfrac12(L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}\mp iR_{\vec e_z}^{\mathrm{pau}})$ |
| $\pi_A$ | The sixteen sign patterns with entries $0$ or $\pi$ |
| $S_\nu=iR_{\vec e_z}^{\mathrm{pau}}E_\nu$ | Taste-exchange generators, $S_A$ the corresponding products |
| $I_4$ | Unit matrix of the four-dimensional Dirac module |
| $D$ | Lattice Dirac operator of the Ginsparg–Wilson relation |
| $S(p)$ | Naive lattice propagator |
| $\omega(\vec p)$ | Lattice dispersion relation |
| $F(x,y)$, $F_\mu(k)$ | Lattice kernel and its Fourier transform (vector field on the zone) |
| $\tilde{\nabla}$ | Biquaternionic gradient |
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
- The companion articles of this series: [The Dirac–Kähler Equation](../articles_maths/the-dirac-kahler-equation.html), [Dirac Matter: Graphene, Dirac Cones and Topological Insulators in Biquaternionic Form](dirac-matter-graphene-dirac-cones-and-topological-insulators-in-biquaternionic-form.html), and [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html).
