# __The Involution and the Hermitian Structure of $M_3(\mathbb{C})$__

## Introduction

The conjugate transpose
$$
A^{*}=\bar A^{\mathsf T},\qquad (A^{*})_{ij}=\overline{a_{ji}},
$$
is a real-linear involution of $M_{3}(\mathbb{C})$. It is not complex-linear: $(iA)^{*}=-iA^{*}$. Its fixed points are the Hermitian matrices, its anti-fixed points are the skew-Hermitian matrices, and the elements that preserve the Hermitian form are the $*$-unitary matrices. The involution gives the algebra a **Hermitian structure**, and the trace form
$$
\langle A,B\rangle=\operatorname{tr}(A^{*}B)
$$
is a positive definite Hermitian inner product. This is the form that is used throughout the category; it is not the complex bilinear trace pairing $\operatorname{tr}(AB)$ of *The Element, the Coordinates and the Trace of $M_3(\mathbb{C})$*, which is indefinite.

The article defines the involution and its three distinguished sets, proves the decomposition into Hermitian and skew-Hermitian parts, establishes the positive definiteness of the trace form and the Frobenius norm, identifies the real forms $\mathfrak{u}(3)$ and $\mathfrak{su}(3)$, and compares the definite form with the null cone of the biquaternion algebra. The comparison is the reason for the article: the biquaternion algebra has a quadratic form with nonzero isotropic vectors, while $M_{3}(\mathbb{C})$ with the Hermitian trace form has none. The singular set $\det A=0$ is not a null cone; it is a complex hypersurface of real codimension two, treated in *The Forms, the Norms and the Singular Set of $M_3(\mathbb{C})$*.

The construction is root-first. The matrix units $E_{ij}$ are those of *The Matrix Algebra $M_{3}(\mathbb{C})$*; the involution acts on them by $E_{ij}^{*}=E_{ji}$, and the standard root $H_{0}=\operatorname{diag}(1,\omega,\omega^{2})$ is $*$-unitary, because its eigenvalues have modulus one. The Hermitian structure is compatible with the frame but does not depend on it.

## The Involution

**Definition.** The **conjugate transpose** of $A=(a_{ij})$ is $A^{*}=(\bar a_{ji})$.

**Proposition.** The map $A\mapsto A^{*}$ is an involution of the real algebra:
$$
(A^{*})^{*}=A,\qquad (A+B)^{*}=A^{*}+B^{*},\qquad (\alpha A)^{*}=\bar\alpha A^{*},\qquad (AB)^{*}=B^{*}A^{*}.
$$
It is conjugate-linear, not complex-linear, and it is an anti-automorphism of the algebra.

**Proof.** The first three identities are entrywise. For the product, the $(i,j)$-entry of $(AB)^{*}$ is $\overline{(AB)_{ji}}=\sum_{k}\overline{a_{jk}b_{ki}}=\sum_{k}\bar b_{ki}\bar a_{jk}$, which is the $(i,j)$-entry of $B^{*}A^{*}$. The conjugate-linearity is the appearance of $\bar\alpha$; taking $\alpha=i$ gives $(iA)^{*}=-iA^{*}\neq iA^{*}$, so the map is not complex-linear.

**The three distinguished sets.**

- $A$ is **Hermitian** when $A^{*}=A$, equivalently $a_{ij}=\bar a_{ji}$.
- $A$ is **skew-Hermitian** when $A^{*}=-A$, equivalently $a_{ij}=-\bar a_{ji}$.
- $A$ is **$*$-unitary** when $A^{*}A=AA^{*}=I$.

The diagonal entries of a Hermitian matrix are real; the diagonal entries of a skew-Hermitian matrix are purely imaginary. The identity $I$ is Hermitian, and $iI$ is skew-Hermitian.

**The Hermitian and skew-Hermitian decomposition.** Every $A$ splits uniquely as
$$
A=\tfrac12(A+A^{*})+\tfrac12(A-A^{*}),
$$
where the first term is Hermitian and the second is skew-Hermitian. Hence
$$
M_{3}(\mathbb{C})=\operatorname{Herm}_{3}\oplus\operatorname{Skew}_{3},\qquad 18=9+9,
$$
as real vector spaces. The two summands are the $+1$ and $-1$ eigenspaces of the real-linear involution $A\mapsto A^{*}$.

**Proof.** The first term is fixed by the star, the second is anti-fixed, and their sum is $A$; the decomposition is unique because the intersection of the two eigenspaces is zero. The real dimensions are $9$ each: a Hermitian matrix is determined by the three real diagonal entries and the three complex entries above the diagonal, $3+2\cdot3=9$; the skew-Hermitian matrices are $i$ times the Hermitian ones, also of dimension $9$.

**The real forms.** The skew-Hermitian matrices form the real Lie algebra
$$
\mathfrak{u}(3)=\{A:A^{*}=-A\},\qquad \dim_{\mathbb{R}}\mathfrak{u}(3)=9,
$$
and the traceless skew-Hermitian matrices form
$$
\mathfrak{su}(3)=\{A:A^{*}=-A,\ \operatorname{tr}A=0\},\qquad \dim_{\mathbb{R}}\mathfrak{su}(3)=8.
$$
Both are closed under the commutator: if $A^{*}=-A$ and $B^{*}=-B$, then $[A,B]^{*}=[B^{*},A^{*}]=[-B,-A]=-[A,B]$. The complexifications are $\mathfrak{u}(3)_{\mathbb{C}}=\mathfrak{gl}_{3}(\mathbb{C})$ and $\mathfrak{su}(3)_{\mathbb{C}}=\mathfrak{sl}_{3}(\mathbb{C})$.

**The $*$-unitary group.** The $*$-unitary matrices form the group
$$
U(3)=\{U:U^{*}U=I\},\qquad \dim_{\mathbb{R}}U(3)=9,
$$
and the special $*$-unitary matrices form
$$
SU(3)=\{U\in U(3):\det U=1\},\qquad \dim_{\mathbb{R}}SU(3)=8.
$$
The Lie algebra of $U(3)$ is $\mathfrak{u}(3)$ and the Lie algebra of $SU(3)$ is $\mathfrak{su}(3)$. The determinant of a $*$-unitary matrix has modulus one, because $|\det U|^{2}=\det(U^{*}U)=1$; the condition $\det U=1$ removes one real dimension, hence $9-1=8$.

**The Cartan involution.** The map
$$
\theta(A)=-A^{*}
$$
is a real-linear involution of $M_{3}(\mathbb{C})$. Its $+1$ eigenspace is $\mathfrak{u}(3)$ and its $-1$ eigenspace is $\operatorname{Herm}_{3}$; the decomposition
$$
M_{3}(\mathbb{C})=\mathfrak{u}(3)\oplus\operatorname{Herm}_{3}
$$
is the Cartan decomposition of the real algebra. The group $GL_{3}(\mathbb{C})$ with the involution $g\mapsto(g^{*})^{-1}$ has the fixed subgroup $U(3)$, and the symmetric space $GL_{3}(\mathbb{C})/U(3)$ is the space of positive definite Hermitian matrices; this is the polar decomposition of *The Polar Decomposition of $M_3(\mathbb{C})$* and *The Exponential Polar Decomposition of $M_3(\mathbb{C})$*.

## The Hermitian Trace Form

**Definition.** The **Hermitian trace form** on $M_{3}(\mathbb{C})$ is
$$
\langle A,B\rangle=\operatorname{tr}(A^{*}B).
$$

**Proposition.** The form is Hermitian, positive definite and nondegenerate:
$$
\langle A,B\rangle=\overline{\langle B,A\rangle},\qquad
\langle A,A\rangle=\sum_{i,j=1}^{3}|a_{ij}|^{2}>0\quad(A\neq0).
$$
The associated norm is the **Frobenius norm**
$$
\|A\|_{\mathrm{F}}=\sqrt{\operatorname{tr}(A^{*}A)}=\Bigl(\sum_{i,j}|a_{ij}|^{2}\Bigr)^{1/2}.
$$

**Proof.** The Hermitian symmetry is
$$
\overline{\langle B,A\rangle}=\overline{\operatorname{tr}(B^{*}A)}=\operatorname{tr}(A^{*}B),
$$
using $\operatorname{tr}(C^{*})=\overline{\operatorname{tr}C}$ and $(B^{*}A)^{*}=A^{*}B$. For positivity,
$$
\operatorname{tr}(A^{*}A)=\sum_{i}(A^{*}A)_{ii}=\sum_{i}\sum_{j}\overline{a_{ji}}a_{ji}=\sum_{i,j}|a_{ij}|^{2},
$$
which is a sum of nonnegative real numbers and vanishes only when every entry is zero. The norm is the square root of the form.

**The only isotropic vector.** The form is definite, so the set of isotropic vectors is
$$
\{A:\langle A,A\rangle=0\}=\{0\}.
$$
There is no nonzero null vector and no null cone. This is the decisive difference from the biquaternion algebra, whose quadratic form has nonzero isotropic vectors.

**The real and imaginary parts.** The real part of the Hermitian form is the Euclidean inner product of the $18$ real coordinates:
$$
\operatorname{Re}\langle A,B\rangle=\sum_{i,j}\bigl(x_{ij}^{A}x_{ij}^{B}+y_{ij}^{A}y_{ij}^{B}\bigr),
$$
and the imaginary part is the symplectic form
$$
\operatorname{Im}\langle A,B\rangle=\sum_{i,j}\bigl(x_{ij}^{A}y_{ij}^{B}-y_{ij}^{A}x_{ij}^{B}\bigr).
$$
The real part is positive definite; the imaginary part is alternating. The pair is the Hermitian structure of the real vector space $\mathbb{R}^{18}\cong\mathbb{C}^{9}$.

**The Cauchy–Schwarz inequality.** For all $A,B$,
$$
|\langle A,B\rangle|^{2}\leq\langle A,A\rangle\langle B,B\rangle,
$$
with equality exactly when $A$ and $B$ are linearly dependent. The inequality is the Cauchy–Schwarz inequality for the positive definite form; it is the source of the operator norm estimates of *The Forms, the Norms and the Singular Set of $M_3(\mathbb{C})$*.

**The trace form and the star.** The Hermitian form is related to the complex bilinear trace pairing by
$$
\langle A,B\rangle=\operatorname{tr}(A^{*}B)=\overline{\operatorname{tr}(A^{\mathsf T}\bar B)},
$$
and the two agree on real symmetric matrices, where $A^{*}=A^{\mathsf T}=A$; on general complex matrices they differ: $\operatorname{tr}(AB)$ is complex bilinear and indefinite, $\operatorname{tr}(A^{*}B)$ is Hermitian and definite. The first is the trace pairing of *The Element, the Coordinates and the Trace of $M_3(\mathbb{C})$*; the second is the form of this article.

## The Hermitian Spectral Theorem

**Theorem.** Let $H$ be Hermitian. Then:

1. The eigenvalues of $H$ are real.
2. There is a $*$-unitary $U$ and a real diagonal matrix $\Lambda$ with $H=U\Lambda U^{*}$.
3. The spectral projectors are Hermitian and orthogonal, and $H=\sum_{k}\lambda_{k}P_{k}$ with $P_{k}^{*}=P_{k}$, $P_{k}P_{l}=\delta_{kl}P_{k}$, $\sum_{k}P_{k}=I$.
4. $H$ is positive definite exactly when all its eigenvalues are positive.

**Proof.** For an eigenvector $v$ with eigenvalue $\lambda$, $Hv=\lambda v$. Taking the Hermitian form with $v$,
$$
\lambda\langle v,v\rangle=\langle v,Hv\rangle=\langle Hv,v\rangle=\bar\lambda\langle v,v\rangle,
$$
so $\lambda=\bar\lambda$ and $\lambda$ is real. The spectral theorem for a Hermitian matrix gives an orthonormal basis of eigenvectors, hence $H=U\Lambda U^{*}$ with $U$ $*$-unitary and $\Lambda$ real diagonal. The projectors onto the eigenspaces are Hermitian because the eigenspaces are orthogonal, and the spectral identity is the expansion in that basis. The positive definiteness is the positivity of $\langle v,Hv\rangle=\sum_{k}\lambda_{k}|\langle v,u_{k}\rangle|^{2}$ for every nonzero $v$, which holds exactly when every $\lambda_{k}>0$.

**The positive definite cone.** The set of positive definite Hermitian matrices is open in $\operatorname{Herm}_{3}$ and is a single orbit of $GL_{3}(\mathbb{C})$ under $H\mapsto gHg^{*}$; it is the symmetric space $GL_{3}(\mathbb{C})/U(3)$. Its boundary is the set of positive semidefinite matrices with a zero eigenvalue, contained in $\det H=0$. The determinant is real on Hermitian matrices, and positive on the positive definite cone.

**Worked example.** Let
$$
H=\begin{pmatrix}1&i&0\\-i&2&0\\0&0&3\end{pmatrix}.
$$
Then $H^{*}=H$, so $H$ is Hermitian. Its trace is $6$ and its determinant is $3(2-1)=3$. The eigenvalues are $3$ and the two roots of $\lambda^{2}-3\lambda+1=0$, namely
$$
\frac{3+\sqrt5}{2},\qquad \frac{3-\sqrt5}{2},
$$
both real and positive; the smallest is approximately $0.382$, so $H$ is positive definite. The Frobenius norm squared is
$$
\operatorname{tr}(H^{2})=1+1+1+4+9=16,
$$
and the Hermitian form of $H$ with itself is $16$. The matrix
$$
K=iH=\begin{pmatrix}i&-1&0\\1&2i&0\\0&0&3i\end{pmatrix}
$$
is skew-Hermitian, $K^{*}=-K$; its eigenvalues are $i$ times the eigenvalues of $H$, purely imaginary. The matrix $U=\exp(iH)$ is $*$-unitary, because $(e^{iH})^{*}=e^{-iH}=(e^{iH})^{-1}$.

## The Real Forms and the Comparison with the Biquaternion Cone

**The real forms.** The real algebra $M_{3}(\mathbb{C})$ has several real forms:

| Real form | Definition | Real dimension |
|---|---|---|
| $M_{3}(\mathbb{R})$ | real entries | $9$ |
| $\mathfrak{u}(3)$ | skew-Hermitian | $9$ |
| $\mathfrak{su}(3)$ | traceless skew-Hermitian | $8$ |
| $\operatorname{Herm}_{3}$ | Hermitian | $9$ |

The first is a real algebra; the second and third are real Lie algebras; the fourth is a real vector space, not closed under multiplication. The $*$-unitary group $U(3)$ is the compact real form of $GL_{3}(\mathbb{C})$, and $SU(3)$ is the compact real form of $SL_{3}(\mathbb{C})$.

**The biquaternion comparison.** The biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ carries a quadratic form with nonzero isotropic vectors. For example, in the basis $e_{t},e_{x},e_{y},e_{z}$,
$$
(e_{t}+ie_{x})(e_{t}-ie_{x})=e_{t}^{2}+e_{x}^{2}=1-1=0,
$$
so the vector $e_{t}+ie_{x}$ is nonzero and isotropic. The null cone of $\mathbb{B}$ is a genuine cone with a nonzero link, and the zero divisors of $\mathbb{B}$ are exactly the isotropic vectors for the form.

In $M_{3}(\mathbb{C})$ with the Hermitian trace form, no such vector exists: $\langle A,A\rangle=0$ implies $A=0$. The zero divisors of $M_{3}$ (the singular matrices) are not the isotropic vectors of the form; the determinant is not the norm. The singular set
$$
\{A:\det A=0\}
$$
is a complex hypersurface, of real codimension two in the real $18$-dimensional algebra, not a cone over a positive definite form. The difference is structural: the biquaternion quadratic form is indefinite and has isotropic vectors; the $M_{3}$ Hermitian form is positive definite by construction, and its isotropic set is a point.

**Why the trace form is definite.** The definiteness is the statement $\operatorname{tr}(A^{*}A)=\sum|a_{ij}|^{2}$. It is the sum of the squared moduli of the nine complex entries, hence a positive real number for every nonzero $A$. The form is the Euclidean form on $\mathbb{C}^{9}$ read in the matrix coordinates; it is the natural positive definite form of the algebra as a complex vector space. The determinant and the trace are different invariants; neither is the norm.

**The determinant is not a norm.** The determinant is homogeneous of degree three and complex-valued; it vanishes on the singular matrices. The Frobenius norm is homogeneous of degree one and positive; it vanishes only at zero. The two define different geometries: the unit ball of the norm is bounded, while the set $|\det A|\leq1$ is unbounded because $A$ can have large entries with a small determinant. The singular set is the boundary of $GL_{3}$ in the norm topology, but it is not the boundary of a cone.

## Summary

The conjugate transpose is the real-linear involution
$$
\boxed{\;A^{*}=\bar A^{\mathsf T},\qquad (AB)^{*}=B^{*}A^{*},\qquad (iA)^{*}=-iA^{*}.\;}
$$
It gives the decomposition
$$
M_{3}(\mathbb{C})=\operatorname{Herm}_{3}\oplus\operatorname{Skew}_{3},\qquad 18=9+9,
$$
and the real forms
$$
\mathfrak{u}(3)=\operatorname{Skew}_{3}\quad(\dim 9),\qquad
\mathfrak{su}(3)=\{A\in\mathfrak{u}(3):\operatorname{tr}A=0\}\quad(\dim 8).
$$
The $*$-unitary group has $\dim U(3)=9$ and $\dim SU(3)=8$.

The Hermitian trace form is
$$
\boxed{\;\langle A,B\rangle=\operatorname{tr}(A^{*}B),\qquad
\langle A,A\rangle=\sum_{i,j}|a_{ij}|^{2}>0\quad(A\neq0).\;}
$$
It is positive definite, with Frobenius norm $\|A\|_{\mathrm{F}}=\sqrt{\operatorname{tr}(A^{*}A)}$, and its only isotropic vector is $0$. There is no null cone.

The Hermitian spectral theorem gives $H=U\Lambda U^{*}$ with $\Lambda$ real diagonal and $U$ $*$-unitary; the eigenvalues of a Hermitian matrix are real, and the positive definite cone is the set of Hermitian matrices with positive eigenvalues.

| Quantity | Value for $M_{3}(\mathbb{C})$ |
|---|---|
| Real dimension | $18$ |
| Hermitian dimension | $9$ |
| Skew-Hermitian dimension | $9$ |
| $\mathfrak{u}(3)$ dimension | $9$ |
| $\mathfrak{su}(3)$ dimension | $8$ |
| $U(3)$ dimension | $9$ |
| $SU(3)$ dimension | $8$ |
| Isotropic vectors of $\operatorname{tr}(A^{*}B)$ | $0$ only |
| Null cone | none |
| Singular set $\det=0$ | real codimension $2$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A^{*}=\bar A^{\mathsf T}$ | the conjugate transpose |
| $\operatorname{Herm}_{3}$ | the Hermitian matrices, real dimension $9$ |
| $\operatorname{Skew}_{3}$ | the skew-Hermitian matrices, real dimension $9$ |
| $\mathfrak{u}(3)$ | the skew-Hermitian Lie algebra |
| $\mathfrak{su}(3)$ | the traceless skew-Hermitian Lie algebra |
| $U(3),SU(3)$ | the $*$-unitary and special $*$-unitary groups |
| $\langle A,B\rangle=\operatorname{tr}(A^{*}B)$ | the positive definite Hermitian trace form |
| $\|A\|_{\mathrm{F}}$ | the Frobenius norm |
| $\theta(A)=-A^{*}$ | the Cartan involution |

## Further Reading

- [The Matrix Algebra $M_3(\mathbb{C})$](the-matrix-algebra-m3c.html), for the matrix units and the trace.
- [The Element, the Coordinates and the Trace of $M_3(\mathbb{C})$](the-element-the-coordinates-and-the-trace-of-m3c.html), for the complex bilinear trace pairing.
- [The Forms, the Norms and the Singular Set of $M_3(\mathbb{C})$](the-forms-the-norms-and-the-singular-set-of-m3c.html), for the determinant, the norms and the singular set.
- [The Polar Decomposition of $M_3(\mathbb{C})$](the-polar-decomposition-of-m3c.html), for the symmetric space $GL_{3}/U(3)$.
- [The Exponential and the Lie Group of $M_3(\mathbb{C})$](the-exponential-and-the-lie-group-of-m3c.html), for $U(3)$ and $SU(3)$.
- [The Biquaternion Algebra](the-biquaternion-algebra.html), for the null cone of the biquaternion form.
- [The Peirce Decomposition of the Biquaternion Algebra](the-peirce-decomposition-of-the-biquaternion-algebra.html), for the comparison with the biquaternion zero divisors.
- [Hermitian Adjoints on a Hermitian Algebra](hermitian-adjoints-on-a-hermitian-algebra.html), for the general theory of the star and the adjoint.
