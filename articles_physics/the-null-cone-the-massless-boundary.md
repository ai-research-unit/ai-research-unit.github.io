# __The Null Cone: The Massless Boundary__

## Introduction

The set of elements of zero norm is the null cone. In the algebra it is the determinant-zero set, in the real slice it is the light cone, and its rays are the points of the sky. Every massless statement of this block is a statement about this cone: the massless representations are the limit of the massive ones as the orbit approaches it, the celestial sphere is its projectivisation, and the conformal group is the group of its projective transformations.

This article describes the cone three times — complex, real, and projected — states the spinor factorisation that makes the projective description work, and explains why the massless limit is a boundary and not a special case.

The article assumes *The Isomorphisms and Their Dimensions* for the determinant, *The Four Kinds of Frame Transformation* for the parabolic class, which is the cone's own class, and *The 2×2 Matrix Model: What It Computes and What It Cannot Show* for the complex form. It hands the massive orbits to *Wigner's Classification: Two Casimirs, Three Orbits* and the little group of a null momentum to *The Little Group of a Null Momentum: $E(2)$*.

## The Null Cone

### The Quadratic Form

$$
N(\tilde X)=\langle\tilde X\rangle_{\natural}=X_t^{2}+X_x^{2}+X_y^{2}+X_z^{2}=\det\mathsf{M}_2(\tilde X).
$$

The form is complex-bilinear, symmetric, non-degenerate, and of rank four. Its zero set is the cone; its non-zero values are the norm.

### The Complex Cone

Complexifying the four-dimensional real space of the algebra gives $\mathbb{C}^{4}$, and $N$ extends to a complex-bilinear form on it. The zero set

$$
\{\tilde X\in\mathbb{C}^{4}:N(\tilde X)=0\}
$$

is a **complex cone of complex dimension three**: a quadric, smooth away from its vertex, and irreducible.

### The Real Slice

The slice of the block in which the norm is a Minkowski interval is the **Hermitian** slice, $Q_t=q_t$ real and $Q_j=i q_j$ real, where

$$
N=\det\mathsf{M}_2(\tilde Q)=q_t^{2}-(q_x^{2}+q_y^{2}+q_z^{2}),
$$

the interval of inertia $(1,3)$. This is the **informational** form of a four-vector: Hermitian, with a real time coefficient. Multiplying by $i$ gives the **material** form $\tilde P_\Phi=i\tilde P$, anti-Hermitian, and the multiplication flips the sign of the norm:

$$
N(i\tilde P)=-N(\tilde P)=-\frac{E^{2}}{c^{2}}+\lvert\vec p\rvert^{2},
$$

the same sum of four squares with the time coefficient imaginary, which is the corpus's four-momentum. The two forms have the same zero set, so the real light cone below is common to both: three-dimensional, and with the vertex removed it has two components, the future and the past cones.

### Why the Two Descriptions Differ

The complex cone is one connected quadric. The real cone splits into two halves because the real form is indefinite — the one minus is $i^{2}=-1$ on the time slot — and it is the *sign of the time component* that separates the halves. That sign is what "future" and "past" mean, and it is lost in the complexification.

## Null Directions

### A Direction Is a Sign

Two null vectors that differ by a positive real factor have the same direction. A direction is therefore an equivalence class, and the class is what the sky is made of. In the algebra the class of a null element is what a light signal's propagation direction is: the vector $\tilde X$ has no scale that any observation can fix, only a direction and an overall factor.

### The Spinor Factorisation

A null element has rank-one matrix, so it factors:

$$
\mathsf{M}_2(\tilde X)=\xi\,\eta^{\mathsf T},
\qquad \xi,\eta\in\mathbb{C}^{2},
$$

and for a **Hermitian** null element the two spinors are conjugate,

$$
\mathsf{M}_2(\tilde X)=\operatorname{tr}\mathsf{M}_2(\tilde X)\,\xi\,\xi^{\dagger},
$$

with $\xi$ determined up to the phase $e^{i\alpha}$ and the trace a real scale. Both statements are verified numerically: the factorisation is exact, and multiplying $\xi$ by a phase leaves the outer product unchanged.

### What the Phase Means

The phase is not observable in the null direction, which is why a direction is a point of the projective spinor space and not of the spinor space. But the phase is observable in interference, and it is the same phase that the two-to-one cover of the group acts on. So the null direction's "sign" and the group's two-fold cover are the same phenomenon in two costumes.

### The Sphere of Null Directions

For the real cone the directions form a two-sphere:

$$
\{\text{future null directions}\}\cong S^{2}\cong\mathbb{CP}^{1},
$$

and the isomorphism is the spinor factorisation: a point of $\mathbb{CP}^{1}$ is a spinor up to phase, and the map to the null direction is the outer product.

## The Projectivised Space

### The Complex Projectivisation

Projectivising the complex cone gives

$$
\{\tilde X\in\mathbb{CP}^{3}:N(\tilde X)=0\}\cong\mathbb{CP}^{1}\times\mathbb{CP}^{1},
$$

the Klein quadric. The two factors are the two spinor chiralities, and the isomorphism is the statement that a complex null direction is a pair of projective spinors, one of each chirality.

That is the same two-factor structure that *The Two Commuting Complex Triples* finds in the algebra and that *The Self-Dual and Anti-Self-Dual Split* finds in the field strength. It is worth naming once: the complex null cone's projectivisation is a product, and the product's two factors are the self-dual and anti-self-dual halves.

### The Real Boundary

For the real cone only one factor survives as a real sphere, and the sky is

$$
S^{2}\cong\mathbb{CP}^{1}\cong\text{the celestial sphere}.
$$

So the real sky sits inside the Klein quadric as the set of **conjugate pairs**: a null direction is real precisely when its two spinors are conjugate to one another, and the real points are the fixed set of the conjugation that exchanges the two factors.

### The Boundary of the Mass Shell

The mass shell of a particle of mass $m$ is the hyperboloid $N=m^{2}c^{2}$ in the Hermitian representative used in this section, and $N=-m^{2}c^{2}$ in the material representative; the sign is the representative's and the cone is common to both. Its boundary in the projectivised momentum space is the null cone: as $m\to0$ the hyperboloid approaches the cone, and the projectivised hyperboloid approaches the sky.

So the sky is the boundary of every mass shell, and the statement "the massless representations are limits of the massive ones" is the statement that the boundary is where the limits live.

## The Massless Limit

### The Limit of the Boost

A boost of rapidity $\theta_{\mathrm{rpd}}$ acting on a momentum of mass $m$ takes it to

$$
m\cosh\theta_{\mathrm{rpd}},\qquad m\sinh\theta_{\mathrm{rpd}},
$$

in the time and boost directions. As $\theta_{\mathrm{rpd}}\to\infty$ with $m$ fixed, both components grow without bound and the ratio tends to one: the momentum becomes null. So the null cone is reached at infinite rapidity, and it is a limit and not a value.

### The Contraction

The stabiliser of a momentum changes in that limit. For $m>0$ it is $SU(2)$, the rotations about the momentum. For $m=0$ it is $E(2)$, the Euclidean group of the plane: the rotations about the momentum *and* the two null rotations that shear it. So the little group grows in the limit, and the growth is the reason the massless labels are not a limit of the massive ones in the naive sense.

*The Little Group of a Massive Particle: $\mathrm{SU}(2)$* and *The Little Group of a Null Momentum: $E(2)$* treat the two groups; the point here is that the boundary's group is larger.

### What Survives

The compact part survives, and the two extra generators are the ones that leave the null momentum fixed without being rotations. So the massless limit is not a degeneration of the little group into a smaller one, as a reader might expect from "the mass shell shrinks"; it is a degeneration into a larger one, with the labels reorganised.

## The Massless Representations as Limits

### The Two Labels

The massive labels are two numbers: the mass, which is continuous, and the spin, which is a half-integer. The massless labels are the helicity, a half-integer, and a continuous parameter that the little group's non-compact part carries.

### Why the Limit Is Not Term by Term

The massive module of spin $j$ does not converge to a single massless module as $m\to0$. It splits: the $2j+1$ states fall into helicity multiplets, and the multiplicities diverge as the mass goes to zero because the little group has grown. The corpus's statement in *Wigner's Classification: Two Casimirs, Three Orbits* is the orbit statement; the module statement is that the limit exists only after a reorganisation.

### The Cusp

The mass shell's two Casimirs, $N=-m^{2}c^{2}$ and the Pauli–Lubanski scalar, are independent for $m>0$ and become dependent on the cone: $N=0$ makes the Pauli–Lubanski vector proportional to the momentum, with the helicity as the constant. So the label space folds along the cone, and the fold is why the massless label set is not the $m\to0$ limit of the massive one.

### The Two Halves Separate

The massless limit is where the two chiral halves of the fermion carrier stop talking to each other. On the cone the Pauli–Lubanski vector is proportional to the momentum, $W_\mu=hP_\mu$, so the helicity is Lorentz invariant; and because the two chiral projectors both reduce to the helicity projectors, chirality and helicity coincide. A mass term is the only term in the Dirac equation that couples the two halves, so at $m=0$ the pair $(\tfrac12,0)\oplus(0,\tfrac12)$ degenerates into two independent carriers, one per helicity.

That is the representation-theoretic content of "the two halves separate", and it is why the massless fermion's two helicities may be described by separate Weyl fields while the massive one may not: the coupling that would have to be removed is exactly the mass. *The Dirac Pair and the Mass Term* proves the corresponding statement for $m\neq0$.

## The Conformal Group

### The Sky and Its Möbius Action

The Lorentz group acts on the sky, and its action is by Möbius transformations:

$$
\xi\mapsto\frac{a\xi+b}{c\xi+d},
\qquad
\begin{pmatrix}a&b\\c&d\end{pmatrix}\in SL_2(\mathbb{C}).
$$

So the group of the sky is $SL_2(\mathbb{C})$ acting on $\mathbb{CP}^{1}$, and this is the same $SL_2(\mathbb{C})$ that the block has been studying as the group of unit-norm elements of the biquaternion algebra.

### What the Two–Two Splitting of the Covers

The Möbius action is two-to-one from $SL_2(\mathbb{C})$ to its projective version, and the sky's conformal group is the projective version. So the conformal group of the sky is *smaller* than the biquaternion group by the centre, and the biquaternion group's extra element is the sign.

That is the same statement as *The Two-Sheeted Cover and the Topology of the Group*: the double cover is invisible on the sky and visible in interference.

### The Conformal Group of Spacetime

The conformal group of four-dimensional Minkowski space is larger than the Lorentz group: it adds dilations and the special conformal transformations. It is not the biquaternion group and is not contained in it. What the biquaternion group supplies is the Lorentz part and the sky's Möbius action; the rest is an extension.

This is worth stating plainly because the conformal group is often claimed for Clifford algebras. The claim that is true is that $SL_2(\mathbb{C})$ acts conformally on the sky and that the sky is the boundary of the compactified Minkowski space; the claim that is false is that the biquaternion algebra's group *is* the four-dimensional conformal group.

### Where It Sits in the Block

The null cone is the boundary of the mass shell, the sky is its projectivisation, the sky's group is the projective biquaternion group, and the massless representations live on the cone. So the cone is where the block's group theory, its projective geometry, and its massless physics meet, and it is the natural end of the structural part of the block.

## Summary

The null cone is the determinant-zero quadric: complex dimension three over $\mathbb{C}$, a two-component light cone in the real slice. Its projectivisation is the Klein quadric $\mathbb{CP}^{1}\times\mathbb{CP}^{1}$, whose factors are the two chiralities; the real sky is the diagonal, a two-sphere. Null directions come from spinors up to phase, and that phase is the sign that the double cover acts on. The mass shell's boundary is the cone, reached at infinite rapidity, and the little group *grows* there from $SU(2)$ to $E(2)$, which is why the massless representations are not the term-by-term limit of the massive ones. The Lorentz group acts on the sky by Möbius transformations, so the sky's conformal group is the projective biquaternion group, and the four-dimensional conformal group is larger and not contained in the algebra's group.

## Summary of Notation

| symbol | meaning |
|---|---|
| $N(\tilde X)=\langle\tilde X\rangle_{\natural}$ | the norm, equal to $\det\mathsf{M}_2(\tilde X)$ |
| null cone | $\{\tilde X:N(\tilde X)=0\}$ |
| $\xi,\eta$ | spinors in the rank-one factorisation |
| $\mathbb{CP}^{1}$ | projective spinor space, the sky |
| Klein quadric | $\{\tilde X\in\mathbb{CP}^{3}:N(\tilde X)=0\}\cong\mathbb{CP}^{1}\times\mathbb{CP}^{1}$ |
| helicity | the massless label carried by the null little group |

## Further Reading

- R. Penrose and W. Rindler, *Spinors and Space-Time*, Vol. 1 and 2, Cambridge University Press, 1984 and 1986 — null directions as spinors, the celestial sphere, and the Klein quadric.
- E. P. Wigner, "On unitary representations of the inhomogeneous Lorentz group", *Annals of Mathematics* 40 (1939) 149 — the null orbit and its little group.
- S. Weinberg, *The Quantum Theory of Fields*, Vol. 1, Cambridge University Press, 1995, §2.5 — the massless limit and the helicity labels.
- R. Penrose and W. Rindler, *Spinors and Space-Time*, Vol. 2, chapter on the conformal treatment of infinity — the sky as the boundary of compactified Minkowski space.
- *The Two Commuting Complex Triples* — the two-factor structure that the Klein quadric exhibits.
- *The Little Group of a Null Momentum: $E(2)$* — the group that the boundary's momentum preserves.
