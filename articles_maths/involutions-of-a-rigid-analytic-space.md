
# __Involutions of a Rigid Analytic Space__

## Introduction

Rigid analytic geometry is the geometry of the zero sets of systems of convergent power series over a complete non-Archimedean field; its affine objects are the affinoid spaces, spectra of the quotients of the Tate algebra $K\langle x_1,\dots,x_n\rangle$. An involution of a rigid analytic space is an automorphism of order two, and the natural questions are: what is its fixed locus, does the quotient exist as a rigid analytic space, and how does the quotient map look at the fixed points. For a finite group over a field in which the order of the group is invertible the quotient always exists, and for the group of order two this is the whole theory; this article states the quotient theorem, computes the basic examples of the affine line, the projective line and the polydisc, and records the failure of the theory when the residue characteristic divides the order. It is the non-Archimedean member of the Hermitian-forms part of the category; the classical analogue is the quotient of a complex analytic space by an antiholomorphic involution. Nothing here reads a distance as an object.

## Rigid Analytic Spaces and Involutions

### The objects

**Definition.** A **rigid analytic space** over $K$ is a locally ringed space over the category of the affinoid spaces, locally isomorphic to $\mathrm{Sp}(A)$ for a $K$-affinoid algebra $A$; the **Tate algebra** is
$$
T_n=K\langle x_1,\dots,x_n\rangle=\Bigl\{\sum_{\alpha}a_\alpha x^\alpha:\ |a_\alpha|\rho^{|\alpha|}\to0\ \text{ for all }\rho<1\ \text{ on the unit polydisc}\Bigr\}.
$$
An **involution** of a rigid analytic space $X$ is an automorphism $\sigma:X\to X$ with $\sigma^2=\mathrm{id}$.

**Definition.** The **fixed locus** is the subspace
$$
X^\sigma=\{x\in X:\sigma(x)=x\},
$$
with the structure sheaf obtained by the ideal generated locally by the elements $f-\sigma(f)$.

**Proposition.** The fixed locus is a closed analytic subspace of $X$; it is the support of the quotient sheaf $\mathcal{O}_X/(1-\sigma)\mathcal{O}_X$, and it can have any dimension from $0$ to $\dim X$. The complement $X\setminus X^\sigma$ is the region on which $\sigma$ acts freely.

**Proof.** The elements $f-\sigma(f)$ generate a coherent ideal sheaf because $\sigma$ is an automorphism of the structure sheaf; the zero locus of that ideal is the fixed set. This is the standard construction of invariant theory, in *Rigid Analytic Geometry*.

### The quotient

**Theorem (finite quotient).** Let the finite group $G$ act on the rigid analytic space $X$ over $K$, and suppose either that $\operatorname{char}K=0$ or that $\#G$ is invertible in the residue field. Then the quotient $X/G$ exists as a rigid analytic space, the quotient map $\pi:X\to X/G$ is finite and surjective, the structure sheaf of the quotient is $\pi_*\mathcal{O}_X^G$, and $\pi$ is an isomorphism over the locus where the action is free. For $G=\{\mathrm{id},\sigma\}$ the quotient is written $X/\sigma$.

**Proof.** The statement is local, and in the affinoid case $X=\mathrm{Sp}(A)$ the invariants $A^G$ are a $K$-affinoid algebra when $\#G$ is invertible, by the averaging operator $f\mapsto\frac1{\#G}\sum_{g\in G}g(f)$ composed with the reduction of the affinoid algebra; the quotient is $\mathrm{Sp}(A^G)$ and the map $\mathrm{Sp}(A)\to\mathrm{Sp}(A^G)$ is finite. The geometric statement follows by gluing. This is the theorem of the finite group quotients in *Rigid Analytic Geometry*.

**Corollary.** For an involution, $\pi$ has degree two over the free locus, and the ramification locus is exactly the fixed locus $X^\sigma$; the different of the quotient map is supported on $X^\sigma$.

## The Basic Examples

### The Tate algebra

**Theorem.** Let $A=T_n=K\langle x_1,\dots,x_n\rangle$ with the involution $\sigma(x_i)=-x_i$. Then
$$
A^\sigma=K\langle\text{monomials of even total degree}\rangle,
$$
which is a $K$-affinoid algebra of the indicated generators; for $n=1$ it is $K\langle x^2\rangle\cong K\langle y\rangle$. The quotient map
$$
\mathrm{Sp}(A)\to\mathrm{Sp}(A^\sigma)
$$
is finite of degree two and is ramified exactly at the origin $\{x_1=\dots=x_n=0\}$.

**Proof.** A convergent series is fixed by $\sigma$ exactly when its odd-degree coefficients vanish; the ring of even series is affinoid because it is the image of $A$ under the averaging operator $\frac12(f+\sigma f)$, which is a continuous linear projection, so it is a closed $K$-affinoid subalgebra. The ramification is the vanishing of the derivative of the invariants at the origin.

### The affine and projective lines

**Example (the affine line).** For $\mathbb{A}^1=\mathrm{Sp}(K\langle z\rangle)$ with $\sigma(z)=-z$ the quotient is $\mathbb{A}^1$ with coordinate $w=z^2$, the map is $\pi(z)=z^2$, of degree two, ramified at $z=0$.

**Example (the projective line).** For $\mathbb{P}^1$ with the involution $z\mapsto-z$ the quotient is $\mathbb{P}^1$ with coordinate $w=z^2$; the map is degree two and ramified at the two fixed points $0$ and $\infty$, which are the fibre of $w=0$ and $w=\infty$.

**Example (a disc automorphism).** An involution of the open unit disc is either free or conjugate to a rotation-like map; when it has a fixed point the quotient is an affinoid or a disc with a coordinate $w$ of even valuation, and the fixed points of the reduction may be more numerous than those of the rigid space.

## The Berkovich Reading

**Theorem.** The involution extends to the Berkovich space $X^{\mathrm{an}}$, the quotient $X^{\mathrm{an}}/\sigma$ exists and equals $(X/\sigma)^{\mathrm{an}}$ for the good spaces, and the fixed locus $X^{\mathrm{an},\sigma}$ contains the fixed locus $X^\sigma$ strictly in general, because the non-classical points can be fixed; the additional fixed points are the points in the closure of the fixed locus of the reduction.

**Proof.** The Berkovich space is the set of multiplicative seminorms bounded by the spectral norm, and $\sigma$ acts on it by precomposition; the quotient of the spectral norm under the invariant seminorm $|\cdot|^G$ gives the identification $(X/G)^{\mathrm{an}}=X^{\mathrm{an}}/G$. The extra fixed points are those seminorms invariant under $\sigma$ without being the kernel of a maximal ideal. This is the theory of *Berkovich Spaces*.

## Failure of the Degenerate Cases

The theory fails in four degenerate configurations. First, when the residue characteristic is $2$ the order of the group is not invertible, the averaging operator does not exist, and the invariants of a $K$-affinoid algebra under an involution need not be affinoid; the quotient can fail to be a rigid analytic space in the naive sense, and a tameness hypothesis or a different category is required. Second, the fixed locus can be empty, in which case the quotient map is étale of degree two and the different is zero; the interesting cases are the ramified ones, and the ramification must be computed by the different even when the fixed locus is a positive-dimensional subspace. Third, the action on the reduction is not faithful in general, and the fixed points of the reduction do not lift to fixed points of the rigid space; the reduction is a coarser invariant and can suggest a fixed locus where there is none. Fourth, the quotient in the category of the rigid analytic spaces and in the category of the Berkovich spaces coincide for the good spaces but not for the general ones, because the Berkovich quotient has more points; the rigid quotient is the "classical" part of the Berkovich quotient. These are the boundary cases of the construction.

## Summary

An involution of a rigid analytic space over a complete non-Archimedean field is an automorphism of order two; its fixed locus is the closed subspace cut out by the elements $f-\sigma(f)$, and when the residue characteristic is not $2$ the quotient $X/\sigma$ exists as a rigid analytic space with structure sheaf the invariants $\pi_*\mathcal{O}_X^\sigma$, the quotient map being finite of degree two and ramified exactly on the fixed locus. The basic examples are the Tate algebra with $x_i\mapsto-x_i$, whose invariants are the even series, the affine line and the projective line with $z\mapsto-z$, whose quotients have the coordinate $z^2$, and the disc automorphisms. The Berkovich quotient contains additional fixed points, the failure of the theory is the residue characteristic $2$, and the fixed locus may be empty, positive-dimensional, or larger for the reduction than for the rigid space.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K$ | Complete non-Archimedean field |
| $T_n=K\langle x_1,\dots,x_n\rangle$ | Tate algebra |
| $\mathrm{Sp}(A)$ | Affinoid space |
| $\sigma$, $\sigma^2=\mathrm{id}$ | Involution |
| $X^\sigma$ | Fixed locus |
| $X/\sigma$, $A^\sigma$ | Quotient space and invariant ring |
| $\pi:X\to X/\sigma$ | Quotient map |
| $f-\sigma(f)$ | Generators of the fixed ideal |
| $(X/G)^{\mathrm{an}}=X^{\mathrm{an}}/G$ | Berkovich quotient |

## Further Reading

- John Tate, *Rigid Analytic Spaces* (Inventiones Mathematicae, 1971), for the affinoid spaces and the invariants.
- Jean-Pierre Serre, *Rigid Analytic Spaces* (seminar notes, 1963), for the finite group quotients.
- Siegfried Bosch, Ulrich Güntzer and Reinhold Remmert, *Non-Archimedean Analysis* (Springer, 1984), for the affinoid algebras and the reduction.
- Vladimir Berkovich, *Spectral Theory and Analytic Geometry over Non-Archimedean Fields* (American Mathematical Society, 1990), for the analytic spaces and the quotients.
- Brian Conrad, *Several Approaches to Non-Archimedean Geometry* (American Mathematical Society, 2008), for the comparison of the rigid and the Berkovich categories.
