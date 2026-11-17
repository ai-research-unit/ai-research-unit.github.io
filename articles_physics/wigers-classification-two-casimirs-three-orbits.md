# __Wigner's Classification: Two Casimirs, Three Orbits__

## Introduction

A relativistic particle is an irreducible unitary representation of the Poincaré group, and Wigner's classification reduces the problem to two steps: classify the orbits of momentum space, then classify the representations of the stabiliser of a point on each orbit. Momentum space has three orbits with physical meaning — timelike, null, spacelike, in the order of the sign of $N$, from negative to positive — and their stabilisers are $SU(2)$, $E(2)$ and $SU(1,1)$.

This article sets out the orbit picture, states how the two Casimirs enter, and derives the labels. It states carefully what the Casimirs do and do not classify, because the standard sentence "the two Casimirs label the orbit" is only half true.

The article assumes *$P$, $T$ and the Representation Labels* for the Casimirs' definition, *The Little Group of a Massive Particle: $\mathrm{SU}(2)$* and *The Little Group of a Null Momentum: $E(2)$* for the stabilisers, *The Null Cone: The Massless Boundary* for the cone, and *The Principal Series and the Complementary Series* for the Lorentz modules that appear as fibres.

## The Orbits

### Momentum Space

Momentum space is the dual of the translation space: four real components $p_\mu$, with the invariant form $p^{2}=\sum_\mu\varepsilon_\mu p_\mu p_\mu$. The Poincaré group acts by

$$
p\longmapsto\Lambda p,
$$

the translations acting trivially on momentum. So the orbit structure is the orbit structure of the Lorentz group on $\mathbb{R}^{4}$, and the translation part is invisible.

### Why Orbits

A unitary representation of the Poincaré group is determined by how the translations act. Their joint spectrum is a set of characters $p\mapsto e^{ip\cdot x}$, and irreducibility forces that set to be a single orbit. So:

- the orbit is the momentum content;
- the fibre over a point is the little group's representation;
- the induced representation assembles the two.

This is Mackey's orbit method, and Wigner's 1939 paper is its first and most important application.

### The Invariant

The Lorentz group preserves $N$ and nothing else continuous: the orbit of a point is the connected component of the level set of $N$, together with the sign of $p_0$ when $N\le0$. So the orbit is labelled by

$$
(N,\ \operatorname{sign}p_0),
$$

which is one continuous and one discrete label.

## The Three Orbits

### Timelike

$N=-m^{2}c^{2}<0$ with $p_0>0$: the future hyperboloid, a three-dimensional sheet. This is the momentum space of a massive particle, and the label is the mass.

$$
\mathcal{O}_{m}=\{p:N=-m^{2}c^{2},\ p_0>0\}\cong\mathbb{H}^{3}.
$$

### Null

$N=0$ with $p_0>0$: the future cone minus its vertex. It is three-dimensional, and its rays are the sky; a point of the orbit is a ray plus a positive scale, so the orbit is a principal $\mathbb{R}_{>0}$-bundle over $S^{2}$.

$$
\mathcal{O}_{0}=\{p:N=0,\ p_0>0\}\cong\mathbb{R}_{>0}\times S^{2}.
$$

### Spacelike

$N=\mu^{2}>0$: the one-sheeted hyperboloid, again three-dimensional: with $p_0=\mu\sinh s$ and $\lvert\vec p\rvert=\mu\cosh s$ it is $S^{2}\times\mathbb{R}$. It is not the momentum space of a physical particle, but it is a perfectly good orbit and its representations are used for tachyons, for spacelike separations in Euclidean field theory, and as a mathematical object.

$$
\mathcal{O}_{\mu}=\{p:N=\mu^{2}\}\cong S^{2}\times\mathbb{R},
$$

### The Count

Three orbits per sign of the invariant, one for each sign possibility, plus the degenerate vertex treated below. So "three orbits" means "three kinds", and the kinds are the three signs.

## The Casimirs as Orbit Invariants

### The First Casimir Is Constant on an Orbit

$C_1=-N$ takes the same value everywhere on an orbit, and it takes different values on different orbits. So $C_1$ classifies the orbit up to the discrete sign of $p_0$ and up to the vertex.

### The Second Casimir Is Not an Orbit Invariant

$C_2=-\sum_\mu\varepsilon_\mu W_\mu W_\mu$ is also constant on an orbit, because it is a Casimir. But it does not distinguish orbits from one another: it is constant on the orbit *and* on the fibre, and its value depends on which little-group representation sits over the orbit. So the correct statement is:

$$
C_1\ \text{labels the orbit};\qquad C_2\ \text{labels the fibre};\qquad (C_1,C_2)\ \text{labels the representation}.
$$

The common shorthand "the two Casimirs label the orbit" is a compression of this, and it is misleading in exactly one case: the null orbit, where $C_2$ vanishes for every representation and cannot label the fibre.

### The Pair

| orbit | $C_1$ | $C_2$ |
|---|---|---|
| timelike | $m^{2}c^{2}$ | $\hbar^{2}m^{2}c^{2}j(j+1)$, with $j$ the spin |
| null | $0$ | $0$ for all physical representations |
| spacelike | $-\mu^{2}$ | takes both signs |

So on the massless orbit the two Casimirs are not independent, and the label that distinguishes helicities has to come from the little group directly. That is the content of the next two sections.

### Why $C_2$ Vanishes on the Null Orbit

$\tilde W\cdot\tilde P=0$ identically. On the cone $\tilde P$ is null and orthogonal to itself, so $\tilde W$ is orthogonal to a null vector and either proportional to it or spacelike. In the physical case it is proportional, $W=hP$, and then $C_2=h^{2}P^{2}=0$. So the vanishing is forced by the orbit's geometry, not by a choice of representation.

## The Stabiliser

### The Little Group

$$
G_{p}=\{\Lambda:\Lambda p=p\}.
$$

For each orbit the stabiliser is a different group, and it is the group that acts on the fibre.

### The Three Little Groups

| orbit | representative momentum | little group | dimension |
|---|---|---|---|
| timelike | $(m,\vec 0)$ | $SU(2)$ (rotations) | $3$ |
| null | $(\omega,0,0,\omega)$ | $E(2)$, double covered | $3$ |
| spacelike | $(0,0,0,\mu)$ | $SU(1,1)$ | $3$ |

All three are three-dimensional, as they must be: the orbit is three-dimensional and the group is six-dimensional.

### Why the Stabiliser Determines the Representation

Once the orbit and a fibre representation are fixed, the induced representation is determined. So two data classify a particle:

$$
(\text{orbit},\ \text{irreducible unitary representation of }G_{p}).
$$

The second datum is where spin, helicity and the continuous-spin parameter live. That is why the labels are $(m,j)$ and $(0,h)$: the first entry is the orbit, the second is the fibre.

### Why the Stabiliser Changes the Counting

For the timelike orbit the little group is compact, so its irreducible unitary representations are finite-dimensional and labelled by a half-integer $j$ with $2j+1$ states. For the null orbit the little group is not compact, so its irreducible unitary representations are either one-dimensional (the helicity) or infinite-dimensional (the continuous spin). That structural difference, and not any dynamical input, is why a massless particle has two helicity states rather than $2j+1$.

## The Induced Representation

### The Construction

Choose a measurable section $s:\mathcal{O}\to G$, $s(p)\,p_{0}=p$, and let $\sigma$ be a representation of $G_{p_0}$ on a Hilbert space $V$. The induced module is the space of functions

$$
\Psi:G\to V,\qquad \Psi(g\,b)=\sigma(b)^{-1}\Psi(g)\ \ (b\in G_{p_0}),
$$

with the inner product integrated over the orbit. The Poincaré group acts by left multiplication, and the result is irreducible when $\sigma$ is.

### The Measure

The orbit carries a Lorentz-invariant measure, the one induced by the invariant measure on the hyperboloid or the cone. Its existence is why the construction produces a unitary representation and not merely a representation, and it is the subject of *The Invariant Measure on the Mass Shell*.

### The Module

The module is a space of $V$-valued sections over the orbit. Its dimension is infinite for every orbit, because the orbit is a continuum; the finite-dimensional label $2j+1$ is the fibre's dimension, not the module's.

That is worth stating because a reader who has just met the finite-dimensional Lorentz representations will expect a finite-dimensional module. There is none: the Poincaré group has no nontrivial finite-dimensional unitary representation either, for the same reason as the Lorentz group.

### The Momentum Basis

In the momentum basis a state is written $|p,\sigma\rangle$ with $p$ on the orbit and $\sigma$ a fibre label. The Lorentz transformation acts as

$$
U(\Lambda)|p,\sigma\rangle=\sum_{\sigma'}D_{\sigma\sigma'}\bigl(W(\Lambda,p)\bigr)|\Lambda p,\sigma'\rangle,
$$

with $W(\Lambda,p)=s(\Lambda p)^{-1}\Lambda s(p)$ the Wigner rotation — the element of the little group that the transformation produces. That element is exactly the Thomas–Wigner rotation of *Why Boosts Are Not Additive: The Bracket Table*, and here it is the cocycle that makes the representation work.

## The Physical Labels

### Massive

$$
(m,j),\qquad m>0,\quad j\in\{0,\tfrac12,1,\dots\},
$$

with $2j+1$ states per momentum. The states are the spin projections in the rest frame.

### Massless

$$
(0,h),\qquad h\in\{0,\pm\tfrac12,\pm1,\dots\},
$$

with one state per momentum per helicity, and both signs present in a parity-invariant theory. The helicity is the eigenvalue of the $M$-part of the little group; the two null rotations of $E(2)$ act trivially in the physical representations.

### What Is Not Physical

- The spacelike orbits, whose representations describe tachyons or Euclidean continuations.
- The continuous-spin representations, whose fibre is infinite-dimensional and whose spectrum has a continuum of helicities.
- The vertex $p=0$, whose little group is the whole Lorentz group and whose representations are the Lorentz modules themselves.

## The Exceptional Cases

### The Vertex

$p=0$ is a fixed point of the whole Lorentz group. Its little group is $G$ itself, so the vertex's representations are the Lorentz group's, and they are the finite-dimensional ones of *The Finite-Dimensional Representations and Their Unitarity Defect* or the series of *The Principal Series and the Complementary Series*. Physically the vertex is the vacuum: a state of zero momentum and zero energy, on which the Lorentz group acts without a momentum to stabilise.

### The Boundary of the Null Orbit

The null orbit is not closed in momentum space: its closure contains the vertex. So the massless representations are the boundary of the massive ones in the orbit space, which is the geometric form of the statement that the massless labels are not the term-by-term limit of the massive ones.

### The Continuous Spin

With $W$ spacelike instead of proportional to $P$, the little group $E(2)$'s translations act nontrivially, and the fibre is infinite-dimensional. The representation is unitary and it is labelled by a continuous parameter. It is not realised in nature, and the reason is not known from the group theory: nothing in Wigner's classification forbids it.

### The Two Signs of $p_0$

The timelike and null orbits each come in a future and a past sheet, related by time reversal. A physical theory uses one sheet, and the other describes antiparticles in the crossed channel. The classification treats the sheets as separate orbits and the choice as an input.

## Summary

Wigner's classification reduces a particle to an orbit of the Lorentz group in momentum space and an irreducible unitary representation of the orbit's stabiliser. There are three orbits, distinguished by the sign of $N$: the timelike hyperboloid with little group $SU(2)$ and labels $(m,j)$; the null cone with little group $E(2)$ and labels $(0,h)$; the spacelike hyperboloid with little group $SU(1,1)$ and no physical particle. The first Casimir labels the orbit and the second labels the fibre, so the pair labels the representation; on the null orbit the second vanishes identically and the helicity has to come from the little group. The induced representation assembles the two data, the Wigner rotation is its cocycle and is the Thomas–Wigner rotation, and the exceptions are the vertex, the non-closed boundary of the cone, and the unphysical continuous-spin family.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathcal{O}_{m},\mathcal{O}_{0},\mathcal{O}_{\mu}$ | the three orbits |
| $G_{p}$ | the little group of $p$ |
| $s(p)$ | a section of the orbit |
| $W(\Lambda,p)$ | the Wigner rotation, the cocycle |
| $(m,j)$ | the massive labels |
| $(0,h)$ | the massless labels |
| $\lvert p,\sigma\rangle$ | the momentum basis |

## Further Reading

- E. P. Wigner, "On unitary representations of the inhomogeneous Lorentz group", *Annals of Mathematics* 40 (1939) 149 — the original classification.
- G. W. Mackey, *Induced Representations of Groups and Quantum Mechanics*, Benjamin, 1968 — the orbit method in the form used here.
- S. Weinberg, *The Quantum Theory of Fields*, Vol. 1, Cambridge University Press, 1995, §2.5 — the construction in the physicist's notation, with the Wigner rotation explicit.
- Y. Ohnuki, *Unitary Representations of the Poincaré Group and Relativistic Wave Equations*, World Scientific, 1988 — the three little groups and the induced modules written out.
- *$P$, $T$ and the Representation Labels* — the Casimirs whose values appear here.
- *Why Boosts Are Not Additive: The Bracket Table* — the Thomas–Wigner rotation that becomes the cocycle.
