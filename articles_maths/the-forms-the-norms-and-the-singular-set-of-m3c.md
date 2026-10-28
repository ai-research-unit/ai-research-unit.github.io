# __The Forms, the Norms and the Singular Set of $M_3(\mathbb{C})$__

## Introduction

The algebra $M_{3}(\mathbb{C})$ carries three natural norms and one determinant. The **Frobenius norm** is the Euclidean norm of the nine complex entries, the **operator norm** is the norm of the linear map $\mathbb{C}^{3}\to\mathbb{C}^{3}$, and the **nuclear norm** is the sum of the singular values. The three are unitarily invariant and satisfy
$$
\|A\|_{\mathrm{op}}\leq\|A\|_{\mathrm{F}}\leq\|A\|_{*}\leq\sqrt3\,\|A\|_{\mathrm{F}}.
$$
The determinant is not a norm: it is homogeneous of degree three, complex-valued, and vanishes on the singular matrices. The **singular set**
$$
\Sigma=\{A:\det A=0\}
$$
is a complex hypersurface of real codimension two. It is stratified by the rank, with the dimensions
$$
\dim_{\mathbb{C}}(\operatorname{rank}3)=9,\quad
\dim_{\mathbb{C}}(\operatorname{rank}2)=8,\quad
\dim_{\mathbb{C}}(\operatorname{rank}1)=5,\quad
\dim_{\mathbb{C}}(\operatorname{rank}0)=0.
$$
The article defines the three norms, proves the inequalities and the singular-value description, describes the singular set and its rank strata, and compares the definite trace form with the null cone of the biquaternion algebra.

The comparison is the point of the article. The trace form $\operatorname{tr}(A^{*}B)$ of *The Involution and the Hermitian Structure* is positive definite, so its only isotropic vector is $0$ and it has no null cone. The biquaternion algebra has a quadratic form with nonzero isotropic vectors, a genuine null cone, and a link. The determinant zero set of $M_{3}$ is a cone, because the determinant is homogeneous, but it is not the null cone of the trace form: it is a cubic hypersurface, not a quadratic cone, and the form that defines it is not the positive definite one.

The article assumes the trace form and the Frobenius norm of *The Involution and the Hermitian Structure*, the determinant of *The Matrix Algebra $M_{3}(\mathbb{C})$*, and the rank of *The Element, the Coordinates and the Trace*.

## The Trace Form and the Frobenius Norm

**Definition.** The **Frobenius norm** is
$$
\|A\|_{\mathrm{F}}=\sqrt{\operatorname{tr}(A^{*}A)}=\Bigl(\sum_{i,j=1}^{3}|a_{ij}|^{2}\Bigr)^{1/2}.
$$

**Proposition.** The Frobenius norm is a norm on the complex vector space $M_{3}(\mathbb{C})$, and it is the Euclidean norm of the nine complex coordinates. It is unitarily invariant:
$$
\|UAV\|_{\mathrm{F}}=\|A\|_{\mathrm{F}}\qquad(U,V\in U(3)).
$$
Its square is the trace form $\langle A,A\rangle=\operatorname{tr}(A^{*}A)$, and the polarisation
$$
\langle A,B\rangle=\tfrac14\bigl(\|A+B\|_{\mathrm{F}}^{2}-\|A-B\|_{\mathrm{F}}^{2}\bigr)
+\tfrac{i}{4}\bigl(\|A+iB\|_{\mathrm{F}}^{2}-\|A-iB\|_{\mathrm{F}}^{2}\bigr)
$$
recovers the Hermitian form.

**Proof.** The norm is the square root of a positive definite Hermitian form, hence a norm. The invariance is
$$
\operatorname{tr}((UAV)^{*}(UAV))=\operatorname{tr}(V^{*}A^{*}U^{*}UAV)=\operatorname{tr}(V^{*}A^{*}AV)=\operatorname{tr}(A^{*}A),
$$
using $U^{*}U=I$ and the cyclic property of the trace. The polarisation is the standard one for a Hermitian form.

**The trace form.** The form $\langle A,B\rangle=\operatorname{tr}(A^{*}B)$ is positive definite, with only isotropic vector $0$. The Frobenius norm is the norm it defines. The complex bilinear trace pairing $\operatorname{tr}(AB)$ is a different form: it is indefinite, and its isotropic vectors are the nonzero matrices with $\operatorname{tr}(A^{2})=0$, such as $E_{12}$. The two forms agree on real symmetric matrices but not in general.

**The unit sphere.** The set $\{A:\|A\|_{\mathrm{F}}=1\}$ is the unit sphere $S^{17}\subset\mathbb{R}^{18}$, compact and smooth. The Frobenius distance between two matrices is the Euclidean distance of their coordinate vectors; the algebra is a Euclidean space of real dimension $18$ with this norm.

**The Frobenius distance to the singular set.** The distance from $A$ to $\Sigma$ in the Frobenius norm is the smallest singular value,
$$
\operatorname{dist}_{\mathrm{F}}(A,\Sigma)=\sigma_{\min}(A),
$$
with the convention $\sigma_{\min}=0$ for a singular matrix. The nearest singular matrix is obtained by truncating the smallest singular value to zero in the singular value decomposition.

**Proof.** By the Eckart–Young theorem, the nearest matrix of rank at most two is the truncation of the singular value decomposition that keeps the two largest singular values; the distance is the third singular value $\sigma_{3}=\sigma_{\min}$. The singular set is the union of the rank-at-most-two matrices, so the distance to it is the distance to that union, which is $\sigma_{3}$.

## The Operator and Nuclear Norms

**Definition.** The **operator norm** is
$$
\|A\|_{\mathrm{op}}=\sup_{\|v\|=1}\|Av\|,
$$
where the norm on $\mathbb{C}^{3}$ is the Euclidean norm. The **nuclear norm** is
$$
\|A\|_{*}=\sum_{i=1}^{3}\sigma_{i}(A),
$$
where $\sigma_{1}\geq\sigma_{2}\geq\sigma_{3}\geq0$ are the singular values of $A$, the square roots of the eigenvalues of $A^{*}A$.

**The singular value decomposition.** There are unitaries $U,V\in U(3)$ and a real diagonal $\Sigma=\operatorname{diag}(\sigma_{1},\sigma_{2},\sigma_{3})$ with
$$
A=U\Sigma V^{*}.
$$
The columns of $V$ are an orthonormal basis of eigenvectors of $A^{*}A$; the columns of $U$ are the corresponding directions of $Av$; the singular values are the lengths of the images. The decomposition is the Hermitian spectral theorem applied to $A^{*}A$.

**Proposition.** The three norms are
$$
\|A\|_{\mathrm{op}}=\sigma_{1},\qquad
\|A\|_{\mathrm{F}}=\Bigl(\sum_{i}\sigma_{i}^{2}\Bigr)^{1/2},\qquad
\|A\|_{*}=\sum_{i}\sigma_{i}.
$$
They are unitarily invariant, and they satisfy
$$
\|A\|_{\mathrm{op}}\leq\|A\|_{\mathrm{F}}\leq\|A\|_{*}\leq\sqrt3\,\|A\|_{\mathrm{F}},\qquad
\|A\|_{*}\leq3\|A\|_{\mathrm{op}}.
$$

**Proof.** The operator norm is the largest singular value: $\|Av\|^{2}=\sum_{i}\sigma_{i}^{2}|\langle v,v_{i}\rangle|^{2}\leq\sigma_{1}^{2}\|v\|^{2}$, with equality on the first right singular vector. The Frobenius norm is $\operatorname{tr}(A^{*}A)=\sum_{i}\sigma_{i}^{2}$. The nuclear norm is the sum of the singular values by definition. The inequalities are the comparisons of the $\ell^{1}$, $\ell^{2}$ and $\ell^{\infty}$ norms on the three singular values: $\max\sigma_{i}\leq(\sum\sigma_{i}^{2})^{1/2}\leq\sum\sigma_{i}\leq\sqrt3(\sum\sigma_{i}^{2})^{1/2}$, and $\sum\sigma_{i}\leq3\max\sigma_{i}$.

**The Schatten norms.** For $1\leq p<\infty$ the Schatten $p$-norm is
$$
\|A\|_{p}=\Bigl(\sum_{i}\sigma_{i}^{p}\Bigr)^{1/p}.
$$
The operator norm is the limit $p\to\infty$, the Frobenius norm is $p=2$, and the nuclear norm is $p=1$. The three norms of the article are the extremes and the middle of the family.

**The determinant and the singular values.** The determinant is the product of the singular values up to a phase:
$$
|\det A|=\prod_{i=1}^{3}\sigma_{i}.
$$
The singular set is exactly the set where $\sigma_{3}=0$. The **condition number** of an invertible matrix is
$$
\kappa(A)=\frac{\sigma_{1}}{\sigma_{3}}=\|A\|_{\mathrm{op}}\|A^{-1}\|_{\mathrm{op}},
$$
and it blows up as $A$ approaches the singular set.

**Proof.** $|\det A|^{2}=\det(A^{*}A)=\prod_{i}\sigma_{i}^{2}$, so $|\det A|=\prod_{i}\sigma_{i}$. The determinant vanishes exactly when one singular value vanishes, which is exactly when the rank is less than three. The condition number identity is $\|A^{-1}\|_{\mathrm{op}}=1/\sigma_{3}$.

**Hadamard and the determinant.** For every $A$,
$$
|\det A|\leq\prod_{j=1}^{3}\Bigl(\sum_{i=1}^{3}|a_{ij}|^{2}\Bigr)^{1/2}\leq\|A\|_{\mathrm{F}}^{3},
$$
and by the arithmetic–geometric mean inequality,
$$
|\det A|=\prod_{i}\sigma_{i}\leq\Bigl(\frac{\sum_{i}\sigma_{i}^{2}}{3}\Bigr)^{3/2}
=\frac{\|A\|_{\mathrm{F}}^{3}}{3\sqrt3}.
$$
The determinant is bounded by the norms but is not a norm: it is homogeneous of degree three and changes sign under a transposition of two columns.

**Worked example.** For $A=\operatorname{diag}(1,2,3)$, the singular values are $1,2,3$, so
$$
\|A\|_{\mathrm{op}}=3,\qquad \|A\|_{\mathrm{F}}=\sqrt{14},\qquad \|A\|_{*}=6,\qquad \det A=6.
$$
The condition number is $3/1=3$. For $B=\operatorname{diag}(2,1,0)$, the singular values are $2,1,0$, so
$$
\|B\|_{\mathrm{op}}=2,\qquad \|B\|_{\mathrm{F}}=\sqrt5,\qquad \|B\|_{*}=3,\qquad \det B=0.
$$
The matrix $B$ is singular of rank two; its distance to the rank-at-most-one matrices is $\sigma_{2}=1$ in the operator and Frobenius norms, and its distance to zero is $\sigma_{1}=2$.

## The Determinant and the Singular Set

**Definition.** The **singular set** is
$$
\Sigma=\{A\in M_{3}(\mathbb{C}):\det A=0\}.
$$
Its complement is the general linear group $GL_{3}(\mathbb{C})$.

**Proposition.** $\Sigma$ is a complex algebraic hypersurface of complex dimension $8$ and real dimension $16$. It is the zero set of the complex polynomial $\det$, equivalently of the two real polynomials $\operatorname{Re}\det$ and $\operatorname{Im}\det$; the two equations are independent at a matrix of rank two, so $\Sigma$ has real codimension two at its smooth points.

**Proof.** The determinant is a nonzero polynomial of degree three, so its zero set is a hypersurface of complex dimension $9-1=8$, real dimension $16$. At a matrix of rank two, the derivative of the determinant is nonzero: the cofactor matrix is nonzero, and the differential is $H\mapsto\operatorname{tr}(\operatorname{adj}(A)H)$, which is a nonzero linear functional. The real and imaginary parts of this complex linear functional are independent real linear functionals, so the two real equations have independent differentials and the real codimension is two.

**The singular locus.** The hypersurface $\Sigma$ is not smooth everywhere: its singular locus is the set of matrices of rank at most one,
$$
\Sigma_{\mathrm{sing}}=\{A:\operatorname{rank}A\leq1\},
$$
of complex dimension $5$. At a rank-one matrix all $2\times2$ minors vanish, and the cofactor matrix is zero, so the derivative of the determinant vanishes. The rank-two matrices form the smooth part of $\Sigma$.

**Proof.** The cofactor matrix of $A$ is nonzero exactly when the rank is at least two; at rank one all cofactors vanish. The rank-one locus is the image of $\mathbb{C}^{3}\times\mathbb{C}^{3}\to M_{3}$, $(u,v)\mapsto uv^{\mathsf T}$; the fibre over a nonzero rank-one matrix is the one-parameter family $(tu,t^{-1}v)$, so the dimension is $3+3-1=5$. The rank-two matrices are the complement of this locus in $\Sigma$, and they are smooth because the derivative is nonzero.

**The determinant is not a norm.** The determinant is homogeneous of degree three, $\det(\lambda A)=\lambda^{3}\det A$, and it is complex-valued; it vanishes on the singular set and is negative on some invertible matrices (for example, a permutation matrix with an odd permutation). The Frobenius norm is homogeneous of degree one, nonnegative, and vanishes only at zero. The two functions have different geometries: the unit ball of the norm is bounded, while the set $|\det A|\leq1$ is unbounded.

**The determinant cone.** The singular set is a cone: if $\det A=0$, then $\det(\lambda A)=\lambda^{3}\det A=0$ for every $\lambda\in\mathbb{C}$. It is the affine cone over the projective hypersurface of singular matrices in $\mathbb{P}^{8}$. The cone is cubic, not quadratic; it is not the null cone of a quadratic form. The trace form is positive definite and has no nonzero isotropic vectors, so the isotropic set of the form is the single point $0$, not the hypersurface $\Sigma$.

## The Rank Stratification

**The rank strata.** The algebra is the disjoint union
$$
M_{3}(\mathbb{C})=\bigsqcup_{r=0}^{3}\{A:\operatorname{rank}A=r\}.
$$
The ranks and their dimensions are:

| Rank | Description | Complex dimension | Real dimension |
|---|---|---|---|
| $3$ | invertible matrices, $GL_{3}(\mathbb{C})$ | $9$ | $18$ |
| $2$ | singular but not rank one | $8$ | $16$ |
| $1$ | $uv^{\mathsf T}$ with $u,v\neq0$ | $5$ | $10$ |
| $0$ | the zero matrix | $0$ | $0$ |

The rank-three stratum is open and dense; the rank-two stratum is the smooth part of the determinant hypersurface; the rank-one stratum is the singular locus of the hypersurface; the rank-zero stratum is a point.

**Proof of the dimensions.** The rank-three stratum is the complement of the determinant hypersurface, of dimension $9$. The rank-at-most-two stratum is the determinant hypersurface, of dimension $8$; removing the rank-at-most-one stratum, of dimension $5$, does not change the dimension, so the rank-two stratum has dimension $8$. The rank-one stratum is the image of the map $(u,v)\mapsto uv^{\mathsf T}$ from $\mathbb{C}^{3}\times\mathbb{C}^{3}$ minus the axes; the fibre over a nonzero rank-one matrix is $(tu,t^{-1}v)$ for $t\in\mathbb{C}^{\times}$, of dimension one, so the image has dimension $3+3-1=5$. The rank-zero stratum is the single zero matrix.

**The determinantal varieties.** The closure of the rank-at-most-$r$ stratum is the determinantal variety
$$
M_{\leq r}=\{A:\operatorname{rank}A\leq r\},
$$
defined by the vanishing of all $(r+1)\times(r+1)$ minors. For $r=2$ it is $\Sigma$, of dimension $8$; for $r=1$ it is the rank-one determinantal variety, of dimension $5$; for $r=0$ it is $\{0\}$. For $r=1,2$, the singular locus of $M_{\leq r}$ is $M_{\leq r-1}$; in particular, the singular locus of $\Sigma=M_{\leq2}$ is the rank-one variety.

**The distance to the rank strata.** By the Eckart–Young theorem, the distance from $A$ to $M_{\leq r}$ in the operator norm (and in the Frobenius norm) is $\sigma_{r+1}$, with the convention $\sigma_{4}=0$:
$$
\operatorname{dist}_{\mathrm{op}}(A,M_{\leq r})=\sigma_{r+1}(A),\qquad
\operatorname{dist}_{\mathrm{F}}(A,M_{\leq r})=\Bigl(\sum_{i>r}\sigma_{i}^{2}\Bigr)^{1/2}.
$$
So the distance to the singular set is $\sigma_{3}$, the distance to the rank-one variety is $\sigma_{2}$, and the distance to zero is $\sigma_{1}$. The singular values are the coordinates that measure the distance to each rank stratum.

**Proof.** The truncated singular value decomposition $A_{r}=U\operatorname{diag}(\sigma_{1},\ldots,\sigma_{r},0,\ldots,0)V^{*}$ has rank at most $r$ and satisfies
$$
\|A-A_{r}\|_{\mathrm{op}}=\sigma_{r+1},\qquad
\|A-A_{r}\|_{\mathrm{F}}=\Bigl(\sum_{i>r}\sigma_{i}^{2}\Bigr)^{1/2}.
$$
The Eckart–Young theorem states that no matrix of rank at most $r$ is closer in either norm. The distance formula follows.

**Worked example of the strata.** The matrix $\operatorname{diag}(2,1,0)$ has rank two, is singular, and lies in the smooth part of $\Sigma$; its distance to the rank-one variety is $1$ and to zero is $2$. The matrix
$$
uv^{\mathsf T}=\begin{pmatrix}1\\0\\0\end{pmatrix}(1,2,3)
=\begin{pmatrix}1&2&3\\0&0&0\\0&0&0\end{pmatrix}
$$
has rank one, lies in the singular locus of $\Sigma$, and has singular values $\sqrt{14},0,0$. Its Frobenius, operator and nuclear norms are all $\sqrt{14}$, because it has only one nonzero singular value.

## The Absence of a Null Cone

**The definite form.** The trace form $\langle A,A\rangle=\operatorname{tr}(A^{*}A)$ is positive definite. Its isotropic set is
$$
\{A:\langle A,A\rangle=0\}=\{0\}.
$$
There is no nonzero null vector and no null cone of this form; the link of its isotropic set is empty.

**The determinant cone is not the null cone.** The determinant zero set $\Sigma$ is a cone, because the determinant is homogeneous, but it is the zero set of a cubic polynomial, not of the quadratic form $\operatorname{tr}(A^{*}A)$. The two cones are different:
$$
\Sigma=\{A:\det A=0\},\qquad
\{A:\operatorname{tr}(A^{*}A)=0\}=\{0\}.
$$
The determinant vanishes on a hypersurface of real codimension two; the trace form vanishes only at the origin. The singular set is not the set of isotropic vectors of the form.

**The biquaternion null cone.** The biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ has a quadratic form with nonzero isotropic vectors. In the basis $e_{t},e_{x},e_{y},e_{z}$,
$$
Q(z)=z_{t}^{2}+z_{x}^{2}+z_{y}^{2}+z_{z}^{2},
\qquad
Q(e_{t}+ie_{x})=1-1=0.
$$
The null cone
$$
\mathcal{N}=\{z\in\mathbb{B}:Q(z)=0\}
$$
is a genuine cone of complex dimension three, with a link: its intersection with a sphere is a real five-dimensional manifold. The zero divisors of $\mathbb{B}$ are exactly the nonzero points of $\mathcal{N}$, because the quadratic form is the determinant in the matrix model $\mathbb{B}\cong M_{2}(\mathbb{C})$.

**The comparison.** The two algebras have different geometries:

| Object | $M_{3}(\mathbb{C})$ | $\mathbb{B}$ |
|---|---|---|
| Defining form | $\operatorname{tr}(A^{*}B)$, positive definite | $Q$, indefinite |
| Isotropic vectors | $0$ only | nonzero null vectors |
| Null cone | none ($\{0\}$ only) | genuine cone |
| Link | empty | real dimension five |
| Singular set | $\det=0$, real codimension two | $Q=0$, the null cone |
| Zero divisors | singular matrices | nonzero null vectors |

The singular set of $M_{3}$ is a cubic hypersurface; the null cone of $\mathbb{B}$ is a quadratic cone. The trace form of $M_{3}$ is definite, so the only isotropic vector is zero; the biquaternion form is indefinite, so its null cone has a link. The determinant zero set is not the null cone of the trace form; it is a different cone, of a different degree and a different dimension.

**Why the difference is structural.** The biquaternion algebra is not a division algebra: it is isomorphic to $M_{2}(\mathbb{C})$, and its quadratic form is the determinant, which is indefinite on the complexification and has nonzero zero divisors. The algebra $M_{3}(\mathbb{C})$ is simple, and the trace form $\operatorname{tr}(A^{*}B)$ is the positive definite form of the complex vector space; the determinant is a separate invariant of degree three. The definite form is the Euclidean geometry of the nine coordinates; the determinant is the algebraic condition of invertibility. The two are not the same, and the category keeps them separate.

## Summary

The three norms are
$$
\boxed{\;\|A\|_{\mathrm{F}}^{2}=\operatorname{tr}(A^{*}A),\qquad
\|A\|_{\mathrm{op}}=\sigma_{1},\qquad
\|A\|_{*}=\sum_{i}\sigma_{i},\;}
$$
with
$$
\|A\|_{\mathrm{op}}\leq\|A\|_{\mathrm{F}}\leq\|A\|_{*}\leq\sqrt3\,\|A\|_{\mathrm{F}}.
$$
The singular values are the square roots of the eigenvalues of $A^{*}A$, and $|\det A|=\prod_{i}\sigma_{i}$.

The singular set is
$$
\boxed{\;\Sigma=\{A:\det A=0\},\qquad \dim_{\mathbb{C}}\Sigma=8,\quad \dim_{\mathbb{R}}\Sigma=16,\;}
$$
a complex hypersurface of real codimension two, smooth at the rank-two matrices and singular at the rank-one matrices. The rank strata have dimensions
$$
9,\ 8,\ 5,\ 0
$$
in the complex reading, and $18,16,10,0$ in the real reading.

The trace form is positive definite, with isotropic set $\{0\}$; there is no null cone. The determinant zero set is a cubic cone, not the null cone of the trace form. The biquaternion algebra has an indefinite quadratic form, a genuine null cone and a nonzero link; the comparison is the structural difference between the definite Euclidean geometry of $M_{3}$ and the indefinite geometry of $\mathbb{B}$.

| Quantity | Value for $M_{3}(\mathbb{C})$ |
|---|---|
| Frobenius norm | $\sqrt{\operatorname{tr}(A^{*}A)}$ |
| Operator norm | largest singular value |
| Nuclear norm | sum of singular values |
| Determinant | product of singular values up to phase |
| Singular set | $\det=0$, complex dimension $8$, real codimension $2$ |
| Rank strata | $9,8,5,0$ complex |
| Isotropic vectors | $0$ only |
| Null cone | none |
| Biquaternion null cone | genuine, with a link |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\|A\|_{\mathrm{F}}$ | the Frobenius norm $\sqrt{\operatorname{tr}(A^{*}A)}$ |
| $\|A\|_{\mathrm{op}}$ | the operator norm, the largest singular value |
| $\|A\|_{*}$ | the nuclear norm, the sum of the singular values |
| $\sigma_{i}$ | the singular values, $\sigma_{1}\geq\sigma_{2}\geq\sigma_{3}\geq0$ |
| $\Sigma$ | the singular set $\{\det A=0\}$ |
| $M_{\leq r}$ | the determinantal variety of rank at most $r$ |
| $\kappa(A)$ | the condition number $\sigma_{1}/\sigma_{3}$ |
| $\mathcal{N}$ | the biquaternion null cone |

## Further Reading

- [The Involution and the Hermitian Structure](the-involution-and-the-hermitian-structure-of-m3c.html), for the positive definite trace form and the Frobenius norm.
- [The Matrix Algebra $M_{3}(\mathbb{C})$](the-matrix-algebra-m3c.html), for the determinant and the rank.
- [The Element, the Coordinates and the Trace](the-element-the-coordinates-and-the-trace-of-m3c.html), for the trace pairing and the rank.
- [The Cubic, the Discriminant and the Spectral Strata](the-cubic-the-discriminant-and-the-spectral-strata-of-m3c.html), for the determinant and the spectral strata.
- [The Biquaternion Algebra and Its Vector Spaces](the-biquaternion-algebra-and-its-vector-spaces.html), for the null cone of $\mathbb{B}$.
- [Ideals, Peirce Decompositions and Spinors in the Biquaternion Algebra](ideals-peirce-decompositions-and-spinors-in-the-biquaternion-algebra.html), for the zero divisors of $\mathbb{B}$.
- [The Polar Decomposition of $M_3(\mathbb{C})$](the-polar-decomposition-of-m3c.html), for the singular values as the eigenvalues of the positive factor.
- [The Determinant and Alternating Forms](the-determinant-and-alternating-forms.html), for the determinant and its geometry.
