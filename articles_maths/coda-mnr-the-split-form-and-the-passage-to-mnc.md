# __Coda: $M_n(\mathbb{R})$, the Split Form, and the Passage to $M_n(\mathbb{C})$__

## Introduction

**Three things exist over $\mathbb{R}$ and nowhere over $\mathbb{C}$: two classes of involutions of the first kind with the same fixed-space dimension, a spectrum that leaves the base field, and a trace form that is indefinite while the invariant forms are all indefinite too; these three facts are the whole difference between the two categories.**

The coda collects the three phenomena, states the sense in which $M_n(\mathbb{R})$ is the split real form of $M_n(\mathbb{C})$, gives a dictionary of what happens to each structure under complexification and under the real form, and states what the real case teaches that the complex case cannot. It assumes the whole of the real series and cites it by title. It defers nothing; it is the last article.

## The Three Phenomena

**The first is the pair of involution classes.** Transpose $\sigma(X)=X^{\mathsf T}$ and the symplectic involution $\sigma(X)=-JX^{\mathsf T}J^{-1}$ are both involutions of the first kind, both anti-automorphisms of the algebra, and both conjugate to their own transpose. Their fixed spaces have the same dimension,

$$
\dim\operatorname{Sym}_n=\frac{n(n+1)}{2}=\dim\{X:-JX^{\mathsf T}J^{-1}=X\},
$$

but one fixed space is a Jordan algebra and the other a Lie algebra. The fixed space of the transpose is closed under the anticommutator and not under the commutator; the fixed space of the symplectic involution is closed under the commutator and not under the anticommutator. Measured on $100$ random pairs, the symplectic fixed space is closed under the bracket on all $100$ and the symmetric space on none.

**Over $\mathbb{C}$ the dichotomy survives and the signature does not.** The sign in the product rule separates the two classes over every field, so the symplectic type is not conjugate to the transpose over $\mathbb{C}$ either. What complexification removes is the refinement inside the orthogonal class: over $\mathbb{C}$ every nondegenerate symmetric form is congruent to the identity, so all orthogonal involutions are conjugate, while over $\mathbb{R}$ Sylvester's law leaves one class per signature.

**The second is the spectrum.** The characteristic polynomial of a real matrix has real coefficients, so its roots are real or in complex conjugate pairs; the eigenvalues of an antisymmetric matrix are purely imaginary; the eigenvalues of a rotation come in planes with angles. None of this is visible over $\mathbb{C}$, where the fundamental theorem of algebra makes every polynomial split and every matrix triangularisable.

**The third is the trace form.** On $M_n(\mathbb{R})$ the form $\operatorname{tr}(XY)$ has signature $(n(n+1)/2,\,n(n-1)/2)$, so it is indefinite for $n\ge2$. The Hilbert–Schmidt form $\operatorname{tr}(X^{\mathsf T}Y)$ is definite but is not invariant and does not see the algebra structure. No form on $M_n(\mathbb{R})$ is both definite and invariant.

**Over $\mathbb{C}$ there is such a form.** $\operatorname{tr}(A^{*}B)$ is positive definite and invariant under unitary conjugation, so the two properties that are incompatible over $\mathbb{R}$ are compatible over $\mathbb{C}$. This is the sharpest single statement of the difference between the categories.

## The Split Real Form

**Definition.** $M_n(\mathbb{R})$ is a real form of $M_n(\mathbb{C})$: a real subalgebra whose complexification is the complex algebra, $M_n(\mathbb{R})\otimes_{\mathbb{R}}\mathbb{C}\cong M_n(\mathbb{C})$.

**Theorem.** The form is split: the real algebra contains a subalgebra isomorphic to $\mathbb{R}^{n}$, namely the diagonal matrices, of the maximal possible dimension for a commutative subalgebra of $M_n(\mathbb{R})$.

*Proof.* The diagonal matrices form an $n$-dimensional commutative subalgebra, and a commutative subalgebra of $M_n$ has dimension at most $n$ because a commuting family is simultaneously triangularisable and a triangular commutative algebra has dimension at most $n$. So $n$ is the maximal dimension, and a real form is split exactly when its Cartan subalgebra has the maximal dimension, which is the rank $n$ of the complex algebra.

**The other real form is different, and it exists only for even $n$.** For $n=2m$ the quaternion algebra $M_m(\mathbb{H})$, read as a real algebra of dimension $4m^{2}=n^{2}$, is a second real form: its complexification is $M_n(\mathbb{C})$, and its maximal commutative subalgebra has dimension $m=n/2$. For odd $n$ there is no second form. So $M_n(\mathbb{R})$ is the unique real form for odd $n$ and the split one for even $n$, and it is the form with the largest flats.

**Consequence: the two real forms give different geometry.** For the split form the symmetric space $\mathrm{GL}_n(\mathbb{R})/\mathrm{O}(n)$ has rank $n$; for $M_m(\mathbb{H})$ the analogous quotient $\mathrm{GL}_m(\mathbb{H})/\mathrm{Sp}(m)$ has rank $m=n/2$. The rank is a real invariant, invisible to the complex algebra.

**Consequence: the real dimension of the algebra is fixed but the real dimension of the group is not.** Both real forms of $M_n(\mathbb{C})$ have real dimension $n^{2}$; their groups of invertible elements have different topology, and one is homotopy equivalent to a compact group of the same rank while the other is not.

## The Dictionary

**The same construction, read over each field.**

| Structure | over $\mathbb{R}$ | over $\mathbb{C}$ |
|---|---|---|
| the algebra | $M_n(\mathbb{R})$, dimension $n^{2}$ | $M_n(\mathbb{C})$, real dimension $2n^{2}$ |
| the involution | two types, and one orthogonal class per signature | the same two types, one orthogonal class |
| symmetric part | $\operatorname{Sym}_n$, dimension $n(n+1)/2$ | $\operatorname{Sym}_n(\mathbb{C})$, complex dimension $n(n+1)/2$ |
| antisymmetric part | $\operatorname{Skew}_n=\mathfrak{so}(n)$ | $\operatorname{Skew}_n(\mathbb{C})=\mathfrak{so}(n,\mathbb{C})$ |
| the trace form | signature $(n(n+1)/2,\,n(n-1)/2)$ | the complex bilinear form, no signature |
| the invariant definite form | none | $\operatorname{tr}(A^{*}B)$ |
| the group of invertibles | two components | one component |
| the spectrum | real roots and conjugate pairs | all roots, no pairs |
| the Jordan form | rotation blocks $2\times2$ | no rotation blocks |

**Every entry of the real column is a restriction of the complex column, and the restriction loses information in a controlled way.** The loss is the passage from a complex vector space to its real points, and the three phenomena of the first section are exactly the three places where the loss is visible.

**The dictionary is not symmetric.** Complexification is canonical; coming back is a choice of real form. So the real theory is not a special case of the complex theory but a family of choices inside it.

## What Complexification Does to the Two Halves

**Complexification preserves the two halves but not their definiteness.** $\operatorname{Sym}_n\otimes\mathbb{C}=\operatorname{Sym}_n(\mathbb{C})$ and $\operatorname{Skew}_n\otimes\mathbb{C}=\operatorname{Skew}_n(\mathbb{C})$, so the splitting survives. What does not survive is the positivity: over $\mathbb{C}$ the form $\operatorname{tr}(X^{2})$ is complex-valued, so there is no positive and no negative half, only two isotropic halves.

**Consequence: the cone disappears.** The positive definite cone is defined by $v^{\mathsf T}Xv>0$ for real $v$, and over $\mathbb{C}$ the same condition with $v\ne0$ defines the set of Hermitian matrices, which is a real vector space, not a complex one. So the cone is a real object attached to a complex algebra, and it is the cone of a real form.

**Consequence: the exponential keeps its local properties and loses its global ones.** Over both fields the exponential is a local diffeomorphism at $0$ with derivative the identity. Over $\mathbb{R}$ its image misses part of the identity component; over $\mathbb{C}$ the image of $\exp$ on $M_n(\mathbb{C})$ is all of $\mathrm{GL}_n(\mathbb{C})$, because every invertible complex matrix has a logarithm, by the Jordan form without rotation blocks. So the failure of surjectivity is a real phenomenon.

**Consequence: the two components are real.** $\mathrm{GL}_n(\mathbb{C})$ is connected, so the sign of the determinant does not split it; over $\mathbb{R}$ the sign is the only continuous invariant available, and it cuts the group exactly in two.

## The Spectrum

**Real eigenvalues and conjugate pairs.** For $A\in M_n(\mathbb{R})$ the characteristic polynomial has real coefficients, so the nonreal roots occur in conjugate pairs with the same multiplicity, and the real Jordan form pairs each conjugate pair into a $2\times2$ rotation block tensor a nilpotent Jordan block. The number of real roots and the number of pairs are the two integers that classify the spectral type.

**The discriminant cuts the strata.** The discriminant of the characteristic polynomial is a polynomial in the entries, and its zero set is the set of matrices with a repeated eigenvalue. The complement has components indexed by the number of real roots, and crossing the discriminant changes that number by two or by one at a real collision.

**The symmetric and antisymmetric cases are the two extremes.** For symmetric matrices the spectrum is real and the discriminant strata are the collisions; for antisymmetric matrices the spectrum is purely imaginary, so the eigenvalues are $i\theta$ and the collision is $\theta=0$. Both are the spectra of the two halves, and both are invisible over $\mathbb{C}$ where the eigenvalue type carries no information.

**Consequence: the spectral theorem is richer over $\mathbb{R}$.** Over $\mathbb{R}$ there are two spectral theorems, one for symmetric and one for antisymmetric matrices, with two different canonical forms: diagonal and block diagonal by rotations. Over $\mathbb{C}$ there is one, and the antisymmetric case becomes the diagonalisable case with imaginary eigenvalues.

## What the Real Case Teaches

**The real theory carries the extra structure, not less.** Every real statement has a complex shadow, and the shadow loses the three phenomena.

**The real theory is the one that connects to the cone, the order and the group.** The positive cone, the Löwner order, the polar decomposition with its sign, the two components and the covering $\mathrm{Spin}(n)\to\mathrm{SO}(n)$ all require real scalars. Over $\mathbb{C}$ the first becomes a Hermitian cone, the second survives, the third loses its sign, the fourth disappears and the fifth becomes a complex covering.

**The split form is the one with the largest flats.** Its symmetric space has maximal rank $n$, equal to the rank of the complex algebra, so its geometry sees the complex combinatorics most directly.

**Consequence: the passage to $\mathbb{C}$ is a passage to the algebra of the combinatorics, and the passage back is a choice of positivity.** That is the shape of the whole subject: the complex algebra carries the incidence, the real forms carry the metrics, and the three phenomena of the first section are the three places where a metric is chosen.

## The Shape of the Series

**The series added one structure at a time to the same space, and the three phenomena recurred at every stage.** The two involution classes gave the two fixed spaces and the two decompositions; the spectrum gave the discriminant, the Jordan form and the two spectral theorems; the indefinite trace form gave the signature, the curvature and the absence of a definite invariant form.

**The last statement of the series is the first.** $M_n(\mathbb{R})$ is a simple real algebra of dimension $n^{2}$ with centre $\mathbb{R}\mathrm{I}$, its trace form has signature $(n(n+1)/2,\,n(n-1)/2)$, its group of invertibles has two components cut by the sign of the determinant, and the whole structure is the split real form of the complex algebra. Everything else is a consequence.

## Summary

The real category differs from the complex one in exactly three ways: two conjugacy classes of involutions of the first kind with fixed spaces $\operatorname{Sym}_n$ and $\mathfrak{sp}_n$ of the same dimension $n(n+1)/2$, one a Jordan algebra and the other a Lie algebra; a spectrum that leaves the base field, giving conjugate pairs, a discriminant and rotation blocks in the Jordan form; and a trace form of signature $(n(n+1)/2,\,n(n-1)/2)$, indefinite, with no definite invariant form anywhere. $M_n(\mathbb{R})$ is the split real form of $M_n(\mathbb{C})$, with the diagonal matrices as a maximal commutative subalgebra of dimension $n$. The dictionary between the two fields loses the definiteness of the halves, the cone, the two components and the failure of the exponential, and keeps the algebra, the corners, the bracket and the combinatorics.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\sigma(X)=X^{\mathsf T}$ | the transpose involution, fixed space $\operatorname{Sym}_n$ |
| $\sigma(X)=-JX^{\mathsf T}J^{-1}$ | the symplectic involution, fixed space $\mathfrak{sp}_n$ |
| $M_n(\mathbb{R})\otimes\mathbb{C}$ | the complexification, isomorphic to $M_n(\mathbb{C})$ |
| $(p,q)$ | the signature $(n(n+1)/2,\,n(n-1)/2)$ of the trace form |
| the split form | the real form whose maximal commutative subalgebra has dimension $n$ |

## Further Reading

- Nathan Jacobson, *Lie Algebras* (Dover, 1979), for real forms, split forms and the classification of involutions.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the real Jordan form, the discriminant and the spectral theorems.
- [The Split Real Form: $M_n(\mathbb{R})$ inside $M_n(\mathbb{C})$](the-split-real-form-mnr-inside-mnc.html), for the complexification.
- [The Involutions of the First Kind: Transpose and Symplectic](the-involutions-of-the-first-kind-transpose-and-symplectic.html), for the first phenomenon.
- [The Trace Form and Its Indefinite Signature](the-trace-form-and-its-indefinite-signature.html), for the third phenomenon.
