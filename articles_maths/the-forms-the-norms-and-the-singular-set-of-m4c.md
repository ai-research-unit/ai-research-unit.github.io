# __The Forms, the Norms and the Singular Set of $M_4(\mathbb{C})$__

## Introduction

**The full matrix algebra carries a positive definite trace form, three unitarily invariant norms, and the determinantal singular set $\{\det=0\}$ of real codimension two; it has no null cone.** The trace form is $\langle A,B\rangle=\operatorname{tr}(A^*B)$; the norms are the Frobenius, operator and nuclear norms, read from the singular values; the singular set is a complex hypersurface of complex dimension $15$ and real dimension $30$. The zero divisors are the singular matrices, not the isotropic vectors of a form.

The article defines the trace form and the three norms, proves the norm inequalities, describes the determinant and the singular set, stratifies the singular set by rank with the dimension of each stratum, and compares the definite case with the null cone of the biquaternion algebra and its link.

The involution and the positive definite form are *The Involution and the Hermitian Structure of $M_4(\mathbb{C})$*; the polar decomposition is *The Polar Decomposition of $M_4(\mathbb{C})$*; the rank-one determinantal variety is *Rank-One Matrices and the Determinantal Variety*; the biquaternion null cone is *$M_4(\mathbb{C})_L$ Representation : Rank-One Matrices and the Determinantal Variety*.

## The Forms

**The trace form.** The **Hermitian trace form** is

$$
\langle A,B\rangle=\operatorname{tr}(A^*B).
$$

It is positive definite:

$$
\langle A,A\rangle=\sum_{i,j=1}^{4}\lvert A_{ij}\rvert^2,
$$

with equality only for $A=0$. It is the form of *The Involution and the Hermitian Structure of $M_4(\mathbb{C})$*, and it is the only positive definite form used in this article.

**The trace pairing.** The **bilinear trace pairing** is

$$
\beta(A,B)=\operatorname{tr}(AB).
$$

It is symmetric, complex-bilinear and indefinite. It is not the Hermitian form; it agrees with it on the real symmetric matrices but not elsewhere. It is the pairing of *The Element, the Coordinates and the Trace of $M_4(\mathbb{C})$*.

**The Killing form.** On the traceless subalgebra,

$$
K(X,Y)=8\operatorname{tr}(XY)=8\beta(X,Y),
$$

which is the Killing form of $\mathfrak{sl}_4(\mathbb{C})$. It is invariant and non-degenerate on $\mathfrak{sl}_4$, and it is negative definite on the compact real form $\mathfrak{su}(4)$.

**The determinant.** The determinant is not a form and not a norm. It is a multiplicative polynomial of degree four:

$$
\det(AB)=\det A\det B,\qquad
\det(\lambda A)=\lambda^4\det A.
$$

Its modulus is the product of the singular values, and it vanishes exactly on the singular set.

## The Three Norms

**The singular values.** For $A\in M_4(\mathbb{C})$, let

$$
\sigma_1\ge\sigma_2\ge\sigma_3\ge\sigma_4\ge0
$$

be the singular values, the non-negative square roots of the eigenvalues of $A^*A$.

**The Frobenius norm.**

$$
\lVert A\rVert_F=\sqrt{\operatorname{tr}(A^*A)}
=\Bigl(\sum_{k=1}^{4}\sigma_k^2\Bigr)^{1/2}
=\Bigl(\sum_{i,j=1}^{4}\lvert A_{ij}\rvert^2\Bigr)^{1/2}.
$$

It is the Euclidean norm of the sixteen coordinates.

**The operator norm.**

$$
\lVert A\rVert_{\mathrm{op}}
=\sup_{\lVert x\rVert=1}\lVert Ax\rVert
=\sigma_1.
$$

It is the largest singular value, the operator norm of the linear map for the Euclidean norm on $\mathbb{C}^4$.

**The nuclear norm.**

$$
\lVert A\rVert_{*}=\operatorname{tr}\lvert A\rvert
=\sum_{k=1}^{4}\sigma_k,
\qquad
\lvert A\rvert=\sqrt{A^*A}.
$$

It is the sum of the singular values, also called the trace norm or the Schatten $1$-norm.

**Proposition (the norm inequalities).** For every $A\in M_4(\mathbb{C})$,

$$
\lVert A\rVert_{\mathrm{op}}\le\lVert A\rVert_F\le\lVert A\rVert_{*}
\le\sqrt{4}\,\lVert A\rVert_F
\le4\,\lVert A\rVert_{\mathrm{op}}.
$$

**Proof.** The first inequality is $\sigma_1\le(\sum\sigma_k^2)^{1/2}$. The second is $\sum\sigma_k^2\le(\sum\sigma_k)^2$ for non-negative numbers with cross terms. The third is the Cauchy–Schwarz inequality

$$
\sum_{k=1}^{4}\sigma_k\le\sqrt{4}\Bigl(\sum_{k=1}^{4}\sigma_k^2\Bigr)^{1/2}.
$$

The last is $\lVert A\rVert_F\le\sqrt{4}\sigma_1$, because there are four singular values each at most $\sigma_1$.

**$*$-Unitary invariance.** All three norms are invariant under left and right multiplication by unitaries:

$$
\lVert UAV\rVert=\lVert A\rVert,\qquad U,V\in U(4),
$$

for each of the three norms. The invariance follows from the fact that the singular values are unchanged by $*$-unitary multiplication.

**Duality.** The operator and nuclear norms are dual:

$$
\lVert A\rVert_{\mathrm{op}}=\sup_{\lVert B\rVert_{*}\le1}\lvert\operatorname{tr}(A^*B)\rvert,
\qquad
\lVert A\rVert_{*}=\sup_{\lVert B\rVert_{\mathrm{op}}\le1}\lvert\operatorname{tr}(A^*B)\rvert.
$$

The Frobenius norm is self-dual:

$$
\lVert A\rVert_F=\sup_{\lVert B\rVert_F\le1}\lvert\operatorname{tr}(A^*B)\rvert.
$$

**The determinant bound.** The modulus of the determinant is the product of the singular values:

$$
\lvert\det A\rvert=\prod_{k=1}^{4}\sigma_k.
$$

The arithmetic–geometric mean inequality gives

$$
\lvert\det A\rvert\le\Bigl(\frac{\lVert A\rVert_{*}}{4}\Bigr)^4,
\qquad
\lvert\det A\rvert\le\lVert A\rVert_{\mathrm{op}}^4,
\qquad
\lvert\det A\rvert\le\frac{\lVert A\rVert_F^4}{16}.
$$

The determinant is not a norm: it vanishes on nonzero singular matrices, and it is not subadditive.

**The spectral radius.** The **spectral radius** is

$$
\rho(A)=\max_{k}\lvert\lambda_k(A)\rvert,
$$

the maximum modulus of the eigenvalues. It is not a norm: it can vanish for a nonzero nilpotent. It satisfies

$$
\rho(A)\le\lVert A\rVert_{\mathrm{op}},
$$

with equality for normal matrices. The spectral radius is the subject of *Spectral Theory and the Spectral Projectors of $M_4(\mathbb{C})$*.

## The Determinant and the Singular Set

**Definition.** The **singular set** is

$$
\Sigma=\{A\in M_4(\mathbb{C}):\det A=0\}.
$$

Its complement is the general linear group $GL_4(\mathbb{C})$.

**Theorem.** The singular set is a complex hypersurface of complex dimension $15$ and real dimension $30$, hence of real codimension $2$ in $M_4(\mathbb{C})\cong\mathbb{R}^{32}$. It is irreducible, and it is the zero locus of the irreducible polynomial $\det$.

**Proof.** The determinant is a nonzero polynomial of degree four in the sixteen entries; its zero locus is a hypersurface of complex dimension $16-1=15$. The polynomial is irreducible: it is linear in the first row and irreducible by induction, or it is the determinant of the generic matrix, which is irreducible over $\mathbb{C}$ (the determinant of a generic matrix is irreducible). The real dimension is twice the complex dimension, $30$, and the real codimension is $32-30=2$.

**The differential.** The derivative of the determinant is

$$
d(\det)_A(B)=\operatorname{tr}(\operatorname{adj}(A)B),
$$

where $\operatorname{adj}(A)$ is the adjugate matrix. The gradient of the determinant at $A$ is the adjugate, and the adjugate vanishes exactly when $\operatorname{rank}A\le2$. Hence the singular locus of the hypersurface $\Sigma$ is the set of matrices of rank at most $2$.

**The singular locus.** The determinant hypersurface is smooth at the matrices of rank $3$: there the adjugate has rank $1$ and is nonzero, so the gradient does not vanish. At rank $4$ the determinant is nonzero and the hypersurface is not present. The singular locus of $\Sigma$ is

$$
\Sigma_{\mathrm{sing}}=\{A:\operatorname{rank}A\le2\},
$$

of complex dimension $12$ and real dimension $24$.

**The rank stratification.** The rank strata are

$$
M_4^{(r)}=\{A:\operatorname{rank}A=r\},\qquad r=0,1,2,3,4.
$$

The variety of matrices of rank at most $r$ has complex dimension

$$
\dim\{A:\operatorname{rank}A\le r\}=r(2\cdot4-r)=r(8-r),
$$

and the rank-exactly-$r$ stratum has the same dimension, because the lower-rank locus has smaller dimension for $r\ge1$.

| Rank $r$ | Complex dimension $r(8-r)$ | Real dimension | Position in $\Sigma$ |
|---|---|---|---|
| $0$ | $0$ | $0$ | the zero matrix |
| $1$ | $7$ | $14$ | singular locus |
| $2$ | $12$ | $24$ | singular locus |
| $3$ | $15$ | $30$ | smooth part of $\Sigma$ |
| $4$ | $16$ | $32$ | complement $GL_4$ |

**Proof of the dimension formula.** A rank-$r$ matrix is the product $UV$ with $U$ a $4\times r$ matrix of rank $r$ and $V$ an $r\times4$ matrix of rank $r$. The pair $(U,V)$ has $4r+r4=8r$ parameters, and the ambiguity is the action of $GL_r$ by $U\mapsto UG$, $V\mapsto G^{-1}V$, of dimension $r^2$. Hence the dimension is $8r-r^2=r(8-r)$. The rank-exactly-$r$ stratum is open in the rank-at-most-$r$ variety, so it has the same dimension.

**The closure order.** The closure of $M_4^{(r)}$ is the union of the strata of rank at most $r$:

$$
\overline{M_4^{(r)}}=\bigcup_{s\le r}M_4^{(s)}.
$$

The stratification is the rank stratification; it is the algebraic stratification behind the singular set and the determinantal varieties.

**The cone structure.** The singular set is a cone: if $A\in\Sigma$, then $\lambda A\in\Sigma$ for every $\lambda\in\mathbb{C}$. It is not the isotropic cone of the positive definite form; every nonzero matrix has positive Frobenius norm. The cone is the determinantal cone, not a null cone.

## The Absence of a Null Cone

**The isotropic set.** The trace form is positive definite, so

$$
\{A:\langle A,A\rangle=0\}=\{0\}.
$$

There is no nonzero isotropic vector and no null cone. The singular set $\Sigma$ is a cone in the algebraic sense, but it is not the zero set of the form: it is the zero set of the determinant.

**The zero divisors.** The zero divisors of $M_4$ are exactly the singular matrices:

$$
AB=0\quad\text{with }A,B\ne0
\iff
\operatorname{im}B\subseteq\ker A,
$$

which requires $\operatorname{rank}A+\operatorname{rank}B\le4$. The zero divisors form the singular set, a hypersurface, not the isotropic cone of a form.

**The contrast with $\mathbb{B}$.** The biquaternion algebra $\mathbb{B}=M_2(\mathbb{C})$ carries the quaternionic norm

$$
N(\tilde Q)=Q_t^2+B^2,
$$

which is complex-valued and has a nonzero zero set. Its zero set is the **null cone** of the zero divisors: the cone of nonzero elements whose norm vanishes. The regular model $M_4(\mathbb{C})_L$ has determinant equal to the square of the norm, and its singular set is that null cone. The full algebra $M_4(\mathbb{C})$ has the positive definite trace form and no null cone; its singular set is the determinantal hypersurface, which is a different object.

**The comparison of the links.** The null cone of $\mathbb{B}$ is a complex cone of complex dimension $3$ and real dimension $6$; its link in the unit sphere $S^7$ is a real algebraic variety of dimension $5$, a circle bundle over the quadric surface $\mathbb{P}^1\times\mathbb{P}^1$. The singular set $\Sigma$ of $M_4$ is a complex cone of complex dimension $15$ and real dimension $30$; its link in the unit sphere $S^{31}$ is a real algebraic hypersurface of dimension $29$, singular along the rank-at-most-two locus. The projectivised first link is the quadric surface; the link itself is a circle bundle over it. The second link is the link of the determinantal hypersurface, stratified by rank. The two cones are not homeomorphic, and the definite form of $M_4$ does not produce a null cone.

**The regular model is not the full algebra.** The regular model's determinant is the square of the biquaternion norm, and its singular set is the null cone. The full algebra's determinant is the usual $4\times4$ determinant, and its singular set is the determinantal hypersurface. The positive definite form of the full algebra is not the quaternionic norm. The two singular sets have different dimensions and different links.

## Summary

The full matrix algebra carries the positive definite trace form $\langle A,B\rangle=\operatorname{tr}(A^*B)$, the bilinear trace pairing $\beta(A,B)=\operatorname{tr}(AB)$ and the Killing form $8\beta$ on $\mathfrak{sl}_4$. The three unitarily invariant norms are the Frobenius norm $\lVert A\rVert_F=(\sum\sigma_k^2)^{1/2}$, the operator norm $\lVert A\rVert_{\mathrm{op}}=\sigma_1$ and the nuclear norm $\lVert A\rVert_*=\sum\sigma_k$, with

$$
\lVert A\rVert_{\mathrm{op}}\le\lVert A\rVert_F\le\lVert A\rVert_*\le2\lVert A\rVert_F\le4\lVert A\rVert_{\mathrm{op}}.
$$

The singular set $\Sigma=\{\det=0\}$ is an irreducible complex hypersurface of complex dimension $15$ and real dimension $30$, of real codimension $2$; its smooth part is the rank-$3$ stratum, and its singular locus is the rank-at-most-$2$ variety of complex dimension $12$. The rank strata have complex dimensions $0,7,12,15,16$ for ranks $0,1,2,3,4$. The singular set is a cone in the algebraic sense, but it is not the isotropic cone of the definite form; the only isotropic vector is $0$. The biquaternion algebra, by contrast, has a complex-valued norm and a genuine null cone; its projectivised null cone is a quadric surface and its link is a circle bundle over it, while the link of the $M_4$ singular set is the link of the determinantal hypersurface.

$$
\boxed{\ \lVert A\rVert_{\mathrm{op}}\le\lVert A\rVert_F\le\lVert A\rVert_*\le2\lVert A\rVert_F,\quad \dim_\mathbb{C}\Sigma=15,\quad \dim_\mathbb{R}\Sigma=30,\quad \operatorname{codim}_\mathbb{R}\Sigma=2. }
$$

| Stratum | Complex dimension | Real dimension |
|---|---|---|
| Rank $0$ | $0$ | $0$ |
| Rank $1$ | $7$ | $14$ |
| Rank $2$ | $12$ | $24$ |
| Rank $3$ | $15$ | $30$ |
| Rank $4$ | $16$ | $32$ |
| Singular locus of $\Sigma$ | $12$ | $24$ |
| Smooth part of $\Sigma$ | $15$ | $30$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle A,B\rangle=\operatorname{tr}(A^*B)$ | the positive definite trace form |
| $\beta(A,B)=\operatorname{tr}(AB)$ | the bilinear trace pairing |
| $\sigma_1\ge\cdots\ge\sigma_4$ | the singular values |
| $\lVert A\rVert_F$ | the Frobenius norm |
| $\lVert A\rVert_{\mathrm{op}}$ | the operator norm |
| $\lVert A\rVert_*$ | the nuclear norm |
| $\Sigma=\{\det=0\}$ | the singular set |
| $M_4^{(r)}$ | the rank-$r$ stratum |
| $\rho(A)$ | the spectral radius |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the singular values, the unitarily invariant norms, the determinant and the rank stratification.
- Rajendra Bhatia, *Matrix Analysis* (Springer, 1997), for the Schatten norms, the duality of the operator and nuclear norms and the spectral radius.
- Joe Harris, *Algebraic Geometry: A First Course* (Springer, 1992), for determinantal varieties and their dimensions.
- [The Involution and the Hermitian Structure of $M_4(\mathbb{C})$](the-involution-and-the-hermitian-structure-of-m4c.html), for the positive definite trace form.
- [The Element, the Coordinates and the Trace of $M_4(\mathbb{C})$](the-element-the-coordinates-and-the-trace-of-m4c.html), for the trace pairing.
- [The Polar Decomposition of $M_4(\mathbb{C})$](the-polar-decomposition-of-m4c.html), for the singular value decomposition.
- [Spectral Theory and the Spectral Projectors of $M_4(\mathbb{C})$](spectral-theory-and-the-spectral-projectors-of-m4c.html), for the spectral radius and the eigenvalues.
- [$M_4(\mathbb{C})_L$ Representation : Rank-One Matrices and the Determinantal Variety](m4c-representation-rank-one-matrices-and-the-determinantal-variety.html), for the null cone of the regular model.
