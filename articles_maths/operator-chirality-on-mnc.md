# __Operator Chirality on $M_n(\mathbb{C})$__

## Introduction

**The question.** The transpose of a matrix splits the carrier $M_n$ into two halves. What are the halves, how does the product behave across them, and which operator moves one half to the other?

**The answer in one line.** The transpose is an involutive anti-automorphism, the halves are the symmetric and the antisymmetric matrices of dimensions $n(n+1)/2$ and $n(n-1)/2$, and the operator that reverses the chirality is the transpose itself, read as an operator on the carrier.

**Why the article is needed.** The word chirality is used twice in this corpus, for two different objects. In the biquaternion series it names the split between the left and the right multiplications. Here it names the split between the two eigenspaces of the transpose. The two splits are different, and at $n=2$ they are easily confused because both are two-fold and both are realised by $4\times4$ matrices.

**Boundaries.** The two-sided action is *The Two-Sided Operators and the Segre Cone of $M_n(\mathbb{C})$*; the adjoints are *The Two-Sided Operator, the Difference Family and the Adjoints of $M_n(\mathbb{C})$*; the two halves as real spaces are *The Symmetric and Antisymmetric Parts of the Operator Space*. The biquaternion original is *Operator Chirality on the Biquaternion Algebra*.

**Conventions.** $\tau(X)=X^{\mathsf T}$; $\operatorname{Sym}_n=\{X:\tau X=X\}$ and $\operatorname{Anti}_n=\{X:\tau X=-X\}$; $F$ is the operator $X\mapsto X^{\mathsf T}$ on the carrier; $E_{ij}$ are the matrix units.

## The Transpose Involution

**Proposition.** $\tau$ is complex-linear, involutive, and an anti-automorphism: $\tau(XY)=\tau(Y)\tau(X)$.

*Proof.* Linearity and $\tau^2=\mathrm I$ are immediate from the entries, and $(XY)^{\mathsf T}=Y^{\mathsf T}X^{\mathsf T}$ is the entry identity $(XY)_{ij}=\sum_kX_{ik}Y_{kj}$. $\square$

**Proposition (the two halves).** $\operatorname{Sym}_n$ and $\operatorname{Anti}_n$ are complex subspaces of dimensions
$$
\dim\operatorname{Sym}_n=\frac{n(n+1)}{2},\qquad \dim\operatorname{Anti}_n=\frac{n(n-1)}{2},
$$
and $M_n=\operatorname{Sym}_n\oplus\operatorname{Anti}_n$.

*Proof.* The projections $X\mapsto\tfrac12(X\pm X^{\mathsf T})$ are linear and complementary. A symmetric matrix is free on and above the diagonal, $n(n+1)/2$ entries; an antisymmetric one is free strictly above the diagonal, $n(n-1)/2$ entries, with the diagonal zero. $\square$

**The dimensions add up.** $\tfrac12n(n+1)+\tfrac12n(n-1)=n^2$. At $n=2$ the two numbers are $3$ and $1$.

## The Product Is Not Graded

**The four products.** Because $\tau$ reverses the order, the halves are not a grading of the algebra:
$$
(XY)^{\mathsf T}=Y^{\mathsf T}X^{\mathsf T}.
$$
The table of the four products, with the entries the transpose of the product:

| $X$ | $Y$ | $(XY)^{\mathsf T}$ |
|---|---|---|
| $\operatorname{Sym}$ | $\operatorname{Sym}$ | $YX$, not $XY$ in general |
| $\operatorname{Sym}$ | $\operatorname{Anti}$ | $-YX$ |
| $\operatorname{Anti}$ | $\operatorname{Sym}$ | $-YX$ |
| $\operatorname{Anti}$ | $\operatorname{Anti}$ | $-YX$ |

**Consequence.** $\operatorname{Sym}_n$ is not a subalgebra for $n\ge2$, and neither is $\operatorname{Anti}_n$. The sum $XY+(XY)^{\mathsf T}=[X,Y]$ and the difference $XY-(XY)^{\mathsf T}=\{X,Y\}$ are both nonzero for a generic mixed pair, so a mixed product is neither symmetric nor antisymmetric.

**What does hold.** The two sets $\operatorname{Sym}_n\cdot\operatorname{Sym}_n$ and $\operatorname{Anti}_n\cdot\operatorname{Anti}_n$ are each stable under $\tau$ as sets, and so are the two mixed products. The split is a splitting of the carrier, not of the algebra.

**The biquaternion contrast.** At $n=2$ the antisymmetric half is one-dimensional and spanned by the symplectic unit, and the symmetric half is three-dimensional. The quaternion conjugation of the coefficient frame is the transpose, so the biquaternion two-sided theory reads this split as the split into the scalar-plus-vector part and the axial part.

## The Peirce Corners

**Proposition (the corners).** Let $E$ be an idempotent with $E^{\mathsf T}=E$, of rank $k$, and $F=\mathrm I-E$. Then
$$
\tau(E M_nF)=F M_nE,\qquad \tau(F M_nE)=E M_nF,
$$
so the transpose exchanges the two off-diagonal Peirce corners, each of complex dimension $k(n-k)$.

*Proof.* If $X=EYF$ then $X^{\mathsf T}=F^{\mathsf T}Y^{\mathsf T}E^{\mathsf T}=FY^{\mathsf T}E$, which lies in $F M_nE$. Applying $\tau$ again returns $X$. $\square$

**The diagonal corners.** $\tau$ preserves $E M_nE$ and $F M_nF$, and inside each of them it exchanges the symmetric and antisymmetric parts, of dimensions $k(k+1)/2$ and $k(k-1)/2$.

**The two corners of the biquaternion frame.** At $n=2$ with $k=1$ the two off-diagonal corners are one-dimensional each, and the transpose exchanges them. They are the two chiral corners of *The Spin Content of $M_4(\mathbb{C})$*, and the half-integer labels attached to them there come from the block reading, not from the transpose.

## The Reversing Operator

**Proposition.** The transpose of the carrier, $F(X)=X^{\mathsf T}$, is an involution with eigenvalues $+1$ on $\operatorname{Sym}_n$ and $-1$ on $\operatorname{Anti}_n$, and
$$
\operatorname{tr}F=n,\qquad \operatorname{tr}F^2=n^2 .
$$

*Proof.* $F^2=\mathrm I$, so the eigenvalues are $\pm1$; the multiplicities are the dimensions of the two halves, whose difference is $n$. The trace of $F^2$ is the dimension of the carrier. $\square$

**Proposition (which commutators reverse the chirality).** For $S\in\operatorname{Sym}_n$ the operator $\operatorname{ad}_S=L_S-R_S$ is odd for the split, and for $K\in\operatorname{Anti}_n$ it is even:
$$
\operatorname{ad}_S(\operatorname{Sym}_n)\subseteq\operatorname{Anti}_n,\quad
\operatorname{ad}_S(\operatorname{Anti}_n)\subseteq\operatorname{Sym}_n,\quad
\operatorname{ad}_K(\operatorname{Sym}_n)\subseteq\operatorname{Sym}_n .
$$

*Proof.* For $S$ symmetric, $(SX-XS)^{\mathsf T}=X^{\mathsf T}S^{\mathsf T}-S^{\mathsf T}X^{\mathsf T}=XS-SX$ when $X$ is symmetric, which is $-\operatorname{ad}_SX$. The other three cases are the same computation. $\square$

**The operator is a two-sided one.** $\operatorname{ad}_S=L_S-R_S$ is the difference family of *The Two-Sided Operator, the Difference Family and the Adjoints of $M_n(\mathbb{C})$*, and it is the only member of the three families that reverses the chirality. Neither $L_S$ nor $R_S$ does.

## Chirality and the Metric

**Proposition.** $F$ is self-adjoint and unitary for the Hilbert–Schmidt form, and the two halves are orthogonal.

*Proof.* $\langle FX,Y\rangle=\operatorname{tr}(X^{\mathsf T*}Y)=\operatorname{tr}(\overline{X}Y)=\sum_{ij}\overline{X}_{ij}Y_{ji}$, and $\langle X,FY\rangle=\operatorname{tr}(X^{*}Y^{\mathsf T})=\sum_{ij}\overline{X}_{ji}Y_{ij}$; the two sums agree after exchanging the names of the indices. Orthogonality: for $S$ symmetric and $K$ antisymmetric,
$$
\operatorname{tr}(SK)=\sum_{i<j}S_{ij}K_{ji}+\sum_{i<j}S_{ji}K_{ij}=\sum_{i<j}S_{ij}K_{ij}-\sum_{i<j}S_{ij}K_{ij}=0 .
$$
$\square$

**The consequence.** The projections $\tfrac12(\mathrm I\pm F)$ are orthogonal projections, and the Hilbert–Schmidt norm obeys the Pythagorean identity
$$
\lVert X\rVert_{\mathrm{HS}}^2=\lVert\tfrac12(X+X^{\mathsf T})\rVert_{\mathrm{HS}}^2+\lVert\tfrac12(X-X^{\mathsf T})\rVert_{\mathrm{HS}}^2 .
$$

**The reading.** $F$ is an orthogonal involution of the operator space: complex-linear, self-adjoint and unitary, with eigenvalues $\pm1$. It is not a real structure, which would be conjugate-linear. It is the orthogonal reflection of the carrier across the symmetric half.

**At $n=2$.** The symmetric half has dimension $3$ and the antisymmetric half $1$, and the metric split is the $3+1$ of the biquaternion frame. The biquaternion series reads the $3$ as the vector part and the $1$ as the axial part; that reading needs the real form, because over $\mathbb{C}$ the antisymmetric $1$ is the line of the symplectic unit and the symmetric $3$ is everything else.

## The Two Chiralities Are Different

**The witness.** At $n=4$ take $J_z=\operatorname{diag}(\tfrac32,\tfrac12,-\tfrac12,-\tfrac32)$ and $X=E_{01}+E_{10}$, which is symmetric. Then $J_z$ is symmetric, so
$$
[J_z,X]=E_{01}-E_{10},
$$
which is antisymmetric. The principal copy therefore moves a symmetric matrix to an antisymmetric one, and $\operatorname{Sym}_n$ is not invariant under it.

**The moral.** The chirality of this article is a property of the algebra and its transpose. The splitting of $M_n$ into carriers $V_k$ is a property of the conjugation action of the principal copy. They are different decompositions of the same $n^2$ dimensions, and a statement about one is not a statement about the other.

**The same operator, two names.** The operator $F$ that reverses the chirality is exactly the flip of the two tensor slots, so it is also the operator that exchanges the left and the right multiplications. The coincidence is exact and is proved in *The Transposition of the Two Sides*: $FL_AF=R_{A^{\mathsf T}}$.

## The Finite Check

Computed with numpy for $n=2,3,4,5$: the dimension of the symmetric subspace, as the rank of the map $X\mapsto X+X^{\mathsf T}$, is $3,6,10,15$, matching $n(n+1)/2$; the antisymmetric dimension is $1,3,6,10$, matching $n(n-1)/2$. The trace of $F$ is $n$ and the trace of $F^2$ is $n^2$ in each case.

The parity of the commutators was checked on random symmetric and antisymmetric matrices: the residual $\lVert\operatorname{ad}_SX+(\operatorname{ad}_SX)^{\mathsf T}\rVert$ is of the order of $10^{-15}$ in all four cases, and similarly for the other three entries of the table. The witness identity at $n=4$ was computed exactly:
$$
[J_z,E_{01}+E_{10}]=E_{01}-E_{10}.
$$

## The Dimensions

| $n$ | $\dim\operatorname{Sym}$ | $\dim\Lambda^2$ | total |
|---|---|---|---|
| $2$ | $3$ | $1$ | $4$ |
| $3$ | $6$ | $3$ | $9$ |
| $4$ | $10$ | $6$ | $16$ |
| $5$ | $15$ | $10$ | $25$ |

**The two corners.** For the block $(p,q)=(1,n-1)$ the corner $S_{11}$ is one-dimensional, the corner $S_{22}$ has dimension $(n-1)^2$, and the two off-diagonal corners have dimension $n-1$ each. The symmetric part contains the two diagonal corners; the antisymmetric part is spanned by the differences of the off-diagonal corners, paired with their transposes.

**The reading at $n=2$.** The symmetric part has dimension three and the antisymmetric part one, so the split is the split of a four-dimensional space into $3+1$, the same numbers as the carrier decomposition $V_1\oplus V_0$. The equality of the numbers is a coincidence of dimensions: the two invariant structures are different, and the difference is the one drawn in the introduction.

**The degeneracy at $n=2$.** For $n\ge3$ the two Peirce corners $S_{12}$ and $S_{21}$ are distinct subspaces of dimension $n-1$. At $n=2$ they are two distinct lines, and the flip exchanges them.

## Summary

The transpose splits $M_n$ into halves of dimensions $n(n+1)/2$ and $n(n-1)/2$. It is an anti-automorphism, so the split is not a grading and neither half is a subalgebra. It exchanges the two off-diagonal Peirce corners. The transpose operator $F$ has eigenvalues $\pm1$ on the two halves, and the commutator $\operatorname{ad}_S$ with a symmetric $S$ is the operator that reverses the chirality. This chirality is not the principal-copy spin splitting; the principal copy itself moves one half to the other.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tau(X)=X^{\mathsf T}$ | the transpose involution of the algebra |
| $\operatorname{Sym}_n,\operatorname{Anti}_n$ | the two halves, of dimensions $n(n+1)/2$ and $n(n-1)/2$ |
| $F$ | the transpose as an operator on the carrier, $F(X)=X^{\mathsf T}$ |
| $E,F$ | an idempotent and its complement, in the Peirce section |
| $\operatorname{ad}_S$ | $L_S-R_S$, the difference-family operator |

## Further Reading
- [The Two-Sided Operator, the Difference Family and the Adjoints of $M_n(\mathbb{C})$](the-two-sided-operator-the-difference-family-and-the-adjoints-of-mnc.html), for the difference family.
- [The Symmetric and Antisymmetric Parts of the Operator Space](the-symmetric-and-antisymmetric-parts-of-the-operator-space.html), for the same split one level up.
- [The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric](the-two-halves-over-r-symmetric-and-antisymmetric.html), for the real reading.
- [The Peirce Decomposition and the Corner Recursion of $M_n(\mathbb{C})$](the-peirce-decomposition-and-the-corner-recursion-of-mnc.html), for the corners.
- [Operator Chirality on the Biquaternion Algebra](operator-chirality-on-the-biquaternion-algebra.html), for the case $n=2$.
- [The Spin Decomposition of $M_n(\mathbb{C})$](the-spin-decomposition-of-mnc.html), for the splitting that is not this one.
