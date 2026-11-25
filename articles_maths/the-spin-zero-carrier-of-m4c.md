# __The Spin-Zero Carrier of $M_4(\mathbb{C})$: the Scalars__

## Introduction

**The subject.** The carrier of label zero is the line of scalars. It is the smallest carrier, the only one contained in a half, the only one closed under multiplication, and the one that appears in all four readings of the algebra.

**The order of the article.** The first section identifies the carrier and its dimensions. The second proves its invariance and its characterization as the fixed space. The third computes its occurrence in the four readings. The fourth treats its relations with the other carriers, orthogonality and multiplication. The fifth draws the boundary.

**It assumes** *The Clebsch–Gordan Decomposition of $M_4(\mathbb{C})$* for the carriers and *The Parity Rule* for the squares. The row at order two is *The Spin-Zero Carrier of the Biquaternion Algebra*.

**The result in one line.** $V_0=\mathbb{C}\mathrm I$, of complex dimension one and real dimension two, fixed pointwise by the conjugation action, and occurring in every reading of the algebra.

**Boundaries.** The article does not treat the determinant or the spectrum of the scalar matrices in detail; those are the subjects of the two following articles.

## The Carrier

**Proposition.** $V_0=\mathbb{C}\mathrm I$ is a carrier of label $0$, of complex dimension one and real dimension two.

*Proof.* The scalars are invariant under conjugation and the Casimir acts on them by zero; the space of scalars is one complex dimensional, hence two real dimensional.

**Corollary.** The carrier is the fixed space of the conjugation action: $\Phi_q(X)=X$ for all $q$ exactly when $X$ is a scalar.

*Proof.* A matrix commuting with all of $SU(2)$ commutes with all matrices and is a scalar.

**Corollary.** The carrier is the only one of dimension one, and the only one whose label is zero.

*Proof.* The dimensions are $1,3,5,7$ and the labels $0,1,2,3$.

**The reading.** The carrier of label zero is the trivial representation, and its vectors are the fixed points.

## Invariance and Orthogonality

**Proposition.** $V_0$ is orthogonal to the other three carriers for the trace form, and the trace form on it is $\operatorname{tr}(\lambda\mathrm I\,\mu\mathrm I)=4\lambda\mu$.

*Proof.* The carriers are inequivalent irreducible modules, so the invariant bilinear form pairs them trivially; the trace of a scalar matrix is four times the scalar.

**Corollary.** The trace of an element of $V_k$ for $k\ge1$ is zero, and the trace of a scalar is four times the scalar.

*Proof.* The trace is an invariant linear form, trivial on the nontrivial carriers.

**Corollary.** The projection onto $V_0$ is $X\mapsto(\operatorname{tr}X/4)\mathrm I$.

*Proof.* The projection is the identity on the scalars and zero on the traceless part.

**The reading.** The carrier is separated from the others by the trace, which is the only invariant linear form.

## The Occurrences

**Proposition.** $V_0$ occurs in each of the four readings: as the carrier $V_0$ in the principal reading, as the scalars in the $U(4)$ reading, as the piece $(0,0)$ in the factorised reading, and as the scalars of each diagonal block in the block reading.

*Proof.* The four lists: $7+5+3+1$ contains $1$; $1+15$ begins with $1$; $1+3+3+9$ begins with $1$; $8+3+3+2$ contains the scalars of the two blocks.

**Corollary.** The label zero is the only label that occurs in all four readings.

*Proof.* The table of *Which Spin Lives in Which Reading*.

**Corollary.** The scalars are the only piece of the four readings that is one-dimensional, and the only one contained in the symmetric half.

*Proof.* The identity is symmetric and the other pieces have dimension at least two.

**The reading.** The carrier of label zero is the common part of the four readings, which is why the centre is the same object in all of them.

## Multiplication

**Proposition.** $V_0$ is closed under multiplication, and $V_0V_k=V_k$ for every carrier.

*Proof.* The scalars commute with everything and multiplication by a nonzero scalar is an isomorphism of $V_k$.

**Corollary.** $V_0$ is the only carrier that is a subalgebra, and the only one whose product with another carrier is a carrier.

*Proof.* The products of the other carriers are sums of at least two carriers.

**Corollary.** $V_0$ is an ideal, and in fact a two-sided ideal, of the algebra.

*Proof.* $\lambda\mathrm I$ multiplied by any matrix on either side is a scalar multiple of that matrix, but for the ideal property one needs $X\lambda\mathrm I=\lambda X\in M_4$, which holds; the scalars form the centre.

**The reading.** The carrier is simultaneously a subalgebra, an ideal and the centre; it is the only carrier with these three properties.

## The Boundary

**Against the determinant article.** The determinant is a function on the algebra, computed on the carrier as the fourth power; that is the next article.

**Against the spectral article.** The spectrum of a scalar is the single eigenvalue repeated four times; the discriminant vanishes identically on the carrier.

**Against the rank article.** A scalar is invertible or zero: the rank is four or zero, and the two strata meet the carrier in one point each.

## The Scalars and the Centre

**Proposition.** The carrier of label zero is the centre of the algebra, it is the commutant of the copy, and it is the only carrier on which the conjugation action is trivial.

*Proof.* The scalars commute with every matrix, so they are fixed by the conjugation action; the fixed points of an action are the label-zero isotypic component, which is one-dimensional because the multiplicity of the label zero in the tensor square is one; a carrier on which the action is trivial is the fixed space, hence the centre.

**Corollary.** The scalars are the kernel of the traceless projection, and every element of the algebra is the sum of a unique scalar and a unique traceless element.

*Proof.* The projection $X\mapsto X-(\operatorname{tr}X/4)\mathrm I$ has the scalars as kernel and the traceless part as image.

**Corollary.** The determinant of a scalar is the fourth power of the scalar, and the trace form on the centre is four times the product of the two scalars.

*Proof.* $\det(t\mathrm I)=t^{4}$ and $\operatorname{tr}(s\mathrm I\cdot t\mathrm I)=4st$.

**The reading.** The scalar carrier is the part of the algebra that the copy does not see, and it is the unit of the four readings: every list of carriers contains the term one.

## The Unit and the Invariants

**The unit.** The identity matrix is the highest weight vector of the scalar carrier, of weight zero, and it is the unique element of the algebra fixed by the copy and of trace four; the other scalars are its multiples.

**The forms on the line.** Both forms take the value four on the unit, since $\operatorname{tr}(\mathrm I\,\mathrm I)=4$ and $\operatorname{tr}(\mathrm I\,\mathrm I^{\dagger})=4$; on the scalars the two forms therefore coincide, and they differ only on the elements of the carriers on which the conjugation is not real.

**The determinant.** The determinant of the unit is one, and the determinant of a general scalar is the fourth power of the scalar; the fourth power is the degree of the determinant on a space of dimension four, so the scalar carrier sees the dimension of the module through the degree of its determinant.

**The reading.** The scalars are the carrier of the unit, and the unit records the dimension of the module in the degree of its determinant and in the value of its forms.

## Summary

The carrier of label zero is the line of scalars, of complex dimension one and real dimension two, fixed pointwise by the conjugation action and separated from the other carriers by the trace. The projection onto it is $X\mapsto(\operatorname{tr}X/4)\mathrm I$.

It occurs in all four readings of the algebra, it is the only one-dimensional piece, it is closed under multiplication, it multiplies every carrier to itself, and it is a two-sided ideal: it is the centre.

**The place in the corpus.** The scalar carrier is the unit of the four readings and the only summand that is also a two-sided ideal; it is the piece the copy does not see, and its simplicity is the reason the trace form and the determinant are the only invariants that distinguish it from the traceless part.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $V_0=\mathbb{C}\mathrm I$ | the carrier of label zero |
| $\operatorname{tr}/4$ | the projection onto it |
| $4\lambda\mu$ | the trace form on it |
| $1+15$, $1+3+3+9$, $8+3+3+2$ | the readings containing the scalars |

## Further Reading

- [The Spin-Zero Carrier and the Determinant at $n=4$](the-spin-zero-carrier-and-the-determinant-at-n-4.html), for the determinant.
- [The Spin-Zero Carrier and the Spectral Strata at $n=4$](the-spin-zero-carrier-and-the-spectral-strata-at-n-4.html), for the spectrum.
- [The Spin-Zero Carrier and the Rank Strata at $n=4$](the-spin-zero-carrier-and-the-rank-strata-at-n-4.html), for the rank.
- [The Spin-Zero Carrier of the Biquaternion Algebra](the-spin-zero-carrier-of-m4c.html), for the row at order two.
- [Which Spin Lives in Which Reading at $n=4$](which-spin-lives-in-which-reading-at-n-4.html), for the four readings.
