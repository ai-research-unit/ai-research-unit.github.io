# __The Exponential and the Lie Group Structure at $n=4$__

## Introduction

**The matrix space $M_4(\mathbb{C})$ is the Lie algebra of $\mathrm{GL}_4(\mathbb{C})$ under the commutator, the exponential series converges everywhere and gives a smooth map whose image is the whole group, because $\mathbb{C}$ is algebraically closed and every matrix has a logarithm; the exponential is a local diffeomorphism at the origin, with differential the identity, and it is a global diffeomorphism from $\operatorname{Herm}_4$ onto the open cone and a surjection from $\mathfrak{u}(4)$ onto $U(4)$.**

The article proves the convergence and the elementary identities, shows that the exponential is always invertible, proves the surjectivity by reducing to the Jordan form and taking a logarithm of the eigenvalues, identifies the differential and truncates the Baker–Campbell–Hausdorff formula to the second order, identifies the one-parameter subgroups with the solutions of the linear equation $\dot X=AX$, reads the eigenvalues in the axis-free frame, and restricts to the two real forms.

It assumes *The Jordan Form of a $4\times4$ Matrix* family of results, *The Exponential of the Symmetric Part: Stretches and the Positive Cone at $n=4$* and *The Homotopy of $\mathrm{GL}_4(\mathbb{C})$ and of the Two Halves*. The model at order two is *The Exponential and the Lie Group Structure of $\mathrm{GL}_2(\mathbb{C})$*.

## The Series and Its Convergence

**Proposition.** For every complex $4\times4$ matrix $A$ the series
$$
e^{A}=\sum_{k\ge0}\frac{A^{k}}{k!}
$$
converges absolutely in every matrix norm, hence defines an analytic function of $A$.

**Proof.** $\lVert A^{k}\rVert\le\lVert A\rVert^{k}$ and the scalar series $\sum\lVert A\rVert^{k}/k!$ converges; absolute convergence in a complete space gives convergence, and the terms are polynomials in the entries, so the limit is analytic.

**Corollary.** The exponential is continuous, and $e^{0}=\mathrm I_4$.

**Proof.** The series at the zero matrix.

**Corollary.** $e^{tA}$ is analytic in the real parameter $t$ and depends analytically on $A$ jointly.

**Proof.** Substitution into the absolutely convergent series, which is locally uniform in $(t,A)$.

**The eigenvalues.** The eigenvalues of $e^{A}$ are $e^{\lambda}$ for $\lambda$ an eigenvalue of $A$, with the same algebraic multiplicities, and the Jordan structure of $e^{A}$ is the image of that of $A$.

**Proof.** Triangularise $A$ and apply the series to the triangular matrix; the diagonal of the exponential is the exponential of the diagonal, and the off-diagonal entries are determined recursively by divided differences of the exponential.

**Corollary.** $e^{A}$ is never singular, and $\det e^{A}=e^{\operatorname{tr}A}$.

**Proof.** The determinant is the product of the eigenvalues, hence $\prod e^{\lambda}=e^{\sum\lambda}=e^{\operatorname{tr}A}$, which is never zero.

## The Homomorphism Property and the Determinant

**Theorem.** If $AB=BA$ then $e^{A+B}=e^{A}e^{B}$; in particular $e^{A}e^{-A}=\mathrm I_4$, so $e^{A}$ is invertible with inverse $e^{-A}$.

**Proof.** The binomial expansion of $(A+B)^{k}$ is valid when the two commute, and the two double series regroup into the product of the two exponential series.

**Corollary.** The map $t\mapsto e^{tA}$ is a homomorphism from $(\mathbb{R},+)$ into $\mathrm{GL}_4(\mathbb{C})$.

**Proof.** $e^{(s+t)A}=e^{sA}e^{tA}$ by the theorem with $sA$ and $tA$, which commute.

**Corollary.** $\det e^{A}=e^{\operatorname{tr}A}$ gives the determinant of every element of the image, and the image lies in the connected component of the identity.

**Proof.** The path $t\mapsto e^{tA}$ joins the identity to $e^{A}$.

**The failure without commutation.** For noncommuting $A$ and $B$ the identity fails, and the first correction is the commutator: $e^{A}e^{B}=e^{A+B+\frac12[A,B]+\cdots}$.

**Proof.** The Baker–Campbell–Hausdorff formula.

## Surjectivity of the Exponential

**Theorem.** Every invertible $4\times4$ complex matrix is the exponential of a complex matrix.

**Proof.** Put $A$ in Jordan form $A=J$ and write $J=D+N$ with $D$ diagonal and $N$ nilpotent, $DN=ND$. Each nonzero diagonal entry $\lambda$ has a logarithm $\mu$ with $e^{\mu}=\lambda$; the logarithm of a Jordan block with eigenvalue $\lambda\neq0$ is $\mu\mathrm I+\sum_{k\ge1}(-1)^{k+1}(\lambda^{-1}N)^{k}/k$, which terminates because $N^{4}=0$, and its exponential is the block. The sum of the logarithms over the blocks, transported back by the change of basis, exponentiates to $A$.

**Corollary.** The exponential is surjective onto $\mathrm{GL}_4(\mathbb{C})$, and it is not injective: the matrices $A$ and $A+2\pi i\,\mathrm I_4$ have the same exponential.

**Proof.** The eigenvalues of the sum are shifted by $2\pi i$, which the exponential does not see.

**Corollary.** The surjectivity uses the algebraic closedness of $\mathbb{C}$; over $\mathbb{R}$ the exponential of a real matrix has positive determinant, so it misses the whole component of negative determinant.

**Proof.** $\det e^{A}=e^{\operatorname{tr}A}>0$ for real $A$, while $\mathrm{GL}_4(\mathbb{R})$ has elements of negative determinant.

**Corollary.** Over $\mathbb{R}$ the exponential is onto the identity component, which is the set of matrices with positive determinant.

**Proof.** The real Jordan form and a real logarithm on each block with positive eigenvalues or with complex conjugate pairs.

## The Differential and the BCH Formula

**Theorem.** The differential of the exponential at the origin is the identity, so the exponential is a local diffeomorphism there and provides exponential coordinates on a neighbourhood of the identity.

**Proof.** $\left.\frac{d}{dt}\right|_{t=0}e^{tB}=B$, since the series is $tB$ plus terms of order $t^{2}$.

**Corollary.** Every element of $\mathrm{GL}_4(\mathbb{C})$ near the identity is $e^{B}$ for a unique small $B$.

**Proof.** The inverse function theorem.

**Theorem.** For small $A,B$,
$$
\log\bigl(e^{A}e^{B}\bigr)=A+B+\tfrac12[A,B]+\tfrac1{12}[A,[A,B]]+\tfrac1{12}[B,[B,A]]+\cdots,
$$
so the group law in exponential coordinates is the addition corrected by the commutator.

**Proof.** The Baker–Campbell–Hausdorff formula, truncated at the displayed order.

**Corollary.** The commutator is the infinitesimal measure of the failure of the group to be abelian, and the algebra determines the group law near the identity.

**Proof.** The second-order term in the formula.

**Corollary.** The group is abelian exactly when the algebra is abelian, which fails for $M_4$.

**Proof.** The bracket of two matrices is nonzero in general.

## One-Parameter Subgroups

**Theorem.** The one-parameter subgroups of $\mathrm{GL}_4(\mathbb{C})$ are exactly the maps $t\mapsto e^{tA}$, and they are the solutions of the linear equation $\dot X=AX$ with $X(0)=\mathrm I_4$.

**Proof.** Differentiate the series term by term to get $\frac{d}{dt}e^{tA}=Ae^{tA}=e^{tA}A$; conversely a smooth curve with $\dot X=AX$ satisfies $\frac{d}{dt}(e^{-tA}X)=0$, so $X=e^{tA}$.

**Corollary.** The flow of the constant vector field $A$ on the group is the right translation by the one-parameter subgroup, so the Lie algebra acts by left-invariant vector fields.

**Proof.** The solution formula and the invariance of the equation under left translation.

**Corollary.** The solutions are defined for all time because the matrix $A$ is bounded, so the group is complete.

**Proof.** The exponential is defined for every $t$.

## The Axis-Free Reading

**Proposition.** In the axis-free frame the eigenvalues of an element are $Q_t\pm iB$ with multiplicities two and two, where $Q_t$ is the scalar part and $B$ is the length of the vector part; hence the eigenvalues of its exponential are $e^{Q_t}e^{\pm iB}$, two of each.

**Proof.** The quaternion eigenvalues of the biquaternion are $Q_t\pm i\lVert\vec Q\rVert$, each twice in the four-dimensional representation.

**Corollary.** The determinant is $e^{4Q_t}$ and the trace of the exponential is $2e^{Q_t}(e^{iB}+e^{-iB})=4e^{Q_t}\cos B$.

**Proof.** The product and the sum of the four eigenvalues.

**Corollary.** For a purely vector element, with $Q_t=0$, the exponential has eigenvalues $e^{\pm iB}$ twice each, so it is a scalar of unit modulus times a rotor and the rotor is the exponential of a bivector.

**Proof.** The eigenvalues $e^{\pm iB}$ and the two-sided action of the rotor.

## The Two Subgroups

**Theorem.** The exponential maps $\operatorname{Herm}_4$ diffeomorphically onto $\operatorname{Herm}_4^{++}$ and maps $\mathfrak{u}(4)$ onto $U(4)$.

**Proof.** A Hermitian $H$ has real eigenvalues, so $e^{H}$ is positive definite Hermitian; the inverse is the logarithm of the eigenvalues, which is smooth on the positive axis. A anti-Hermitian $K$ satisfies $(e^{K})^{\ast}=e^{K^{\ast}}=e^{-K}=(e^{K})^{-1}$, so the image is unitary; and every unitary is $e^{K}$ for some anti-Hermitian $K$ by the spectral theorem.

**Corollary.** $\exp$ is a diffeomorphism from the Hermitian half onto the open cone, and a surjection with non-discrete fibres from the skew half onto the unitary group.

**Proof.** The first is a diffeomorphism by the two smooth inverse constructions; the second is onto with the ambiguity of the angles by $2\pi$.

**Corollary.** The composition gives the polar decomposition: every invertible matrix is $e^{H}e^{K}$ with $H$ Hermitian and $K$ anti-Hermitian.

**Proof.** The polar decomposition and the two surjectivities.

**The Lie algebra of the unitary group.** $\mathfrak{u}(4)$ is the Lie algebra of $U(4)$ because it is the fixed set of the involution $X\mapsto-X^{\ast}$ on the real Lie algebra, and it is closed under the commutator.

**Proof.** The tangent space at the identity of the level set $A^{\ast}A=\mathrm I$.

## Summary

The exponential series converges everywhere, gives an invertible matrix with determinant $e^{\operatorname{tr}A}$, and is a homomorphism on commuting arguments. It is surjective onto $\mathrm{GL}_4(\mathbb{C})$ because every nonzero complex number has a logarithm and the logarithm of a Jordan block terminates; over $\mathbb{R}$ it reaches only the component of positive determinant.

The differential at the origin is the identity, so the exponential gives coordinates near the identity, and the Baker–Campbell–Hausdorff formula corrects the addition by the commutator. The one-parameter subgroups are the solutions of $\dot X=AX$.

In the axis-free frame the eigenvalues are $Q_t\pm iB$ twice each, so the determinant of the exponential is $e^{4Q_t}$ and the rotor is the exponential of a bivector. The exponential is a diffeomorphism from the Hermitian half onto the open cone and a surjection from the skew half onto $U(4)$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $e^{A}=\sum A^{k}/k!$ | the exponential |
| $\det e^{A}=e^{\operatorname{tr}A}$ | the determinant identity |
| $\mathrm I+2\pi i\mathrm I$ shift | the non-injectivity |
| $A+B+\tfrac12[A,B]$ | the BCH truncation |
| $\dot X=AX$ | the one-parameter subgroup equation |
| $Q_t\pm iB$ | the axis-free eigenvalues |

## Further Reading

- Brian C. Hall, *Lie Groups, Lie Algebras and Representations* (Springer, 2015), for the exponential map and the BCH formula.
- [The Exponential of the Symmetric Part: Stretches and the Positive Cone at $n=4$](the-exponential-of-sym-4-stretches-and-the-positive-cone.html), for the Hermitian restriction.
- [The Homotopy of $\mathrm{GL}_4(\mathbb{C})$ and of the Two Halves](the-homotopy-of-gl4c-and-of-the-two-halves.html), for the contraction built from the exponential.
- [The Minimal Polynomial and the Jordan Form of a $4\times4$ Matrix](the-minimal-polynomial-and-the-jordan-form-of-a-4x4-matrix.html), for the Jordan form used in the surjectivity proof.
- [The Exponential and the Lie Group Structure of $\mathrm{GL}_2(\mathbb{C})$](the-exponential-and-the-lie-group-structure-of-gl2c.html), for the case at order two.
