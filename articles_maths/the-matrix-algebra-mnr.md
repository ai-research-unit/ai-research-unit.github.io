# __The Matrix Algebra $M_n(\mathbb{R})$__

## Introduction

**The matrix algebra $M_n(\mathbb{R})$ is the algebra of $n\times n$ real matrices, and it is the split real form of $M_n(\mathbb{C})$: same matrix units, same trace, same determinant, and a different geometry.** Every construction of the complex category reads here, and three things change. The transpose is one of two inequivalent involutions. The spectrum need not lie in the base field. The trace form is indefinite.

The article fixes the algebra, its matrix units, its trace and determinant, its centre, its transpose, its trace form and its unit group, and closes with the case $n=2$. It assumes only linear algebra over $\mathbb{R}$, and defers the embedding in $M_n(\mathbb{C})$ to *The Split Real Form: $M_n(\mathbb{R})$ inside $M_n(\mathbb{C})$* and the spectral theory to *The Real Spectrum: Real Roots and Conjugate Pairs*.

Throughout $n\ge2$; the transpose is written ${}^{\mathsf T}$ and the identity is $\mathrm{I}$.

## The Algebra and the Matrix Units

**The algebra is the real vector space of $n\times n$ arrays with the matrix product.** Write $E_{ij}$ for the array with $1$ in the entry $(i,j)$ and $0$ elsewhere. The $n^{2}$ arrays $E_{ij}$ are a basis over $\mathbb{R}$, and the product is

$$
E_{ij}E_{kl}=\delta_{jk}E_{il}.
$$

The product is associative and $\mathbb{R}$-bilinear, and $\mathrm{I}=\sum_{k}E_{kk}$ is the unit. The algebra is not commutative for $n\ge2$: $E_{12}E_{21}=E_{11}$ while $E_{21}E_{12}=E_{22}$.

**The dimension over $\mathbb{R}$ is $n^{2}$.** Each entry is one real number, so the basis has $n^{2}$ members. This is half the real dimension $2n^{2}$ of $M_n(\mathbb{C})$, and the factor two is the passage from $\mathbb{R}$ to $\mathbb{C}$, not a change of the algebra.

## Trace, Determinant and Rank

**The trace is the unique linear functional that vanishes on commutators.** Define

$$
\operatorname{tr}A=\sum_{k=1}^{n}A_{kk},\qquad \operatorname{tr}(AB)=\operatorname{tr}(BA).
$$

The identity on the right is a computation with the entries. If $f$ is linear and $f(AB)=f(BA)$ for all $A,B$, then testing on matrix units gives $f(E_{ij})=0$ for $i\ne j$ and $f(E_{ii})=f(E_{jj})$, so $f=c\operatorname{tr}$.

**The determinant is the multiplicative polynomial of degree $n$ normalised at $\mathrm{I}$.** It is the Leibniz sum

$$
\det A=\sum_{\sigma\in S_n}\operatorname{sgn}(\sigma)\prod_{k=1}^{n}A_{k,\sigma(k)},
$$

so it is a polynomial in the entries with integer coefficients, and $\det(AB)=\det A\det B$. Both are invariant under conjugation: $\operatorname{tr}(SAS^{-1})=\operatorname{tr}A$ and $\det(SAS^{-1})=\det A$.

**The rank is the dimension of the image.** For $A\in M_n(\mathbb{R})$ the rank $\operatorname{rk}A$ is $\dim\operatorname{im}A$, equal to the largest order of a nonvanishing minor, and $\operatorname{rk}_{\mathbb{C}}A=\operatorname{rk}_{\mathbb{R}}A$ because the minors are the same real polynomials. The eigenvalues do not survive in the same way; *The Element: Rank, Trace, Determinant, Characteristic Polynomial over $\mathbb{R}$* treats that.

**The determinant cuts the algebra into two open halves.** The zero set $\Sigma=\{A:\det A=0\}$ is a hypersurface of dimension $n^{2}-1$ and its complement is the unit group. Since $\mathbb{R}^{\times}$ has two components, so does the complement; over $\mathbb{C}$ it is connected.

## The Centre and the Simplicity

**The centre is $\mathbb{R}\mathrm{I}$.** If $A$ commutes with every matrix unit then $AE_{ij}=E_{ij}A$ for all $i,j$. Comparing the entry $(i,j)$ on both sides gives $A_{ii}=A_{jj}$ and $A_{ij}=0$ for $i\ne j$; hence $A=\lambda\mathrm{I}$ with $\lambda\in\mathbb{R}$.

**The algebra is simple, and the proof is the same line as over $\mathbb{C}$.** Let $J$ be a nonzero two-sided ideal and let $A\in J$ be nonzero, with $A_{kl}\ne0$. Then for all $i,j$,

$$
E_{ik}AE_{lj}=A_{kl}E_{ij}\in J,
$$

so $J$ contains every matrix unit, hence contains $\mathrm{I}$. Therefore $J=M_n(\mathbb{R})$.

**Central simplicity is a real statement.** $M_n(\mathbb{R})$ is the split central simple real algebra of degree $n$; the other one is $M_{n/2}(\mathbb{H})$ for even $n$, and the two are distinguished by their involutions, not by their ideals. Both complexify to $M_n(\mathbb{C})$; see *The Split Real Form: $M_n(\mathbb{R})$ inside $M_n(\mathbb{C})$*.

**The algebra is not a division algebra.** $E_{11}E_{22}=0$ with both factors nonzero, and $AB=0$ with $A,B\ne0$ exactly when $\operatorname{im}B\subseteq\ker A$. So $M_n(\mathbb{R})$ has zero divisors, in contrast with $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$.

## The Transpose and the Two Halves

**The transpose is an involution of the first kind: it is $\mathbb{R}$-linear and it fixes the base field.** Write $\sigma(A)=A^{\mathsf T}$. Then $\sigma^{2}=\mathrm{id}$, $\sigma(AB)=\sigma(B)\sigma(A)$, and $\sigma(\lambda A)=\lambda\sigma(A)$ for every $\lambda\in\mathbb{R}$. The last property is what fails over $\mathbb{C}$ for the conjugate transpose, which is conjugate linear and fixes only the real scalars.

**The two eigenspaces are the symmetric and the antisymmetric matrices.** Every $A$ splits uniquely as

$$
A=\underbrace{\tfrac12(A+A^{\mathsf T})}_{\in\operatorname{Sym}_n}+\underbrace{\tfrac12(A-A^{\mathsf T})}_{\in\operatorname{Skew}_n},
$$

with

$$
\operatorname{Sym}_n=\{S:S^{\mathsf T}=S\},\qquad \operatorname{Skew}_n=\{K:K^{\mathsf T}=-K\},
$$

and

$$
\dim\operatorname{Sym}_n=\frac{n(n+1)}{2},\qquad \dim\operatorname{Skew}_n=\frac{n(n-1)}{2},\qquad \frac{n(n+1)}{2}+\frac{n(n-1)}{2}=n^{2}.
$$

**The two halves are not closed under the same operation.** The product of two symmetric matrices is symmetric only when they commute, and the product of two antisymmetric matrices is symmetric, since $(KK')^{\mathsf T}=K'K$. The commutator of two antisymmetric matrices is antisymmetric, so $\operatorname{Skew}_n$ is a Lie algebra and $\operatorname{Sym}_n$ is not; this is *The Two Halves: Symmetric and Antisymmetric*.

**The transpose is not the only involution of the first kind when $n$ is even.** Fix an antisymmetric invertible $J$ and put

$$
\sigma_J(A)=-JA^{\mathsf T}J^{-1}.
$$

Then $\sigma_J^{2}=\mathrm{id}$, and $\sigma_J$ is $\mathbb{R}$-linear and of the first kind. Its fixed space is $\mathfrak{sp}_n$, of dimension $n(n+1)/2$, the same dimension as $\operatorname{Sym}_n$. Over $\mathbb{C}$ the same two types exist, but the signature that separates the orthogonal ones over $\mathbb{R}$ collapses, so each type is a single class. Over $\mathbb{R}$ the two are distinct, and one fixed space is a Jordan algebra while the other is a Lie algebra. The comparison is *The Two Classes Compared*; the definition and the classification are *The Involutions of the First Kind: Transpose and Symplectic*.

## The Trace Form and Its Signature

**The bilinear form $\langle A,B\rangle=\operatorname{tr}(AB)$ is symmetric, nondegenerate and indefinite.** Symmetry is the identity $\operatorname{tr}(AB)=\operatorname{tr}(BA)$, and nondegeneracy follows from $\langle E_{ij},E_{kl}\rangle=\delta_{il}\delta_{jk}$: a matrix unit pairs only with its transpose. The form is invariant,

$$
\langle AB,C\rangle=\operatorname{tr}(ABC)=\langle A,BC\rangle,
$$

so it is an associative form, the trace form of the algebra.

**Its signature is $(n(n+1)/2,\,n(n-1)/2)$.** The symmetric matrices are positive definite for the form and the antisymmetric ones negative definite:

$$
\langle S,S\rangle=\operatorname{tr}(S^{2})=\sum_{i,j}S_{ij}S_{ji}=\sum_{i,j}S_{ij}^{2}>0,\qquad
\langle K,K\rangle=\operatorname{tr}(K^{2})=-\sum_{i,j}K_{ij}^{2}<0.
$$

The two halves are orthogonal, because $\operatorname{tr}(SK)=\operatorname{tr}((SK)^{\mathsf T})=\operatorname{tr}(K^{\mathsf T}S^{\mathsf T})=-\operatorname{tr}(KS)=-\operatorname{tr}(SK)$ forces $\operatorname{tr}(SK)=0$. So the form is positive definite on $\operatorname{Sym}_n$ and negative definite on $\operatorname{Skew}_n$, and the signature is the pair of their dimensions. Measured on the basis of matrix units it is $(3,1)$, $(6,3)$, $(10,6)$, $(15,10)$ at $n=2,3,4,5$.

**The form is indefinite for every $n\ge2$, and the null cone is nontrivial.** The antisymmetric half is nonempty as soon as $n\ge2$, so there are elements of negative square. Isotropic elements exist too: every nonzero nilpotent has $\operatorname{tr}(N^{2})=0$, and $E_{12}$ is one.

**No form on $M_n(\mathbb{R})$ is both definite and invariant.** The trace form is invariant and indefinite. The Hilbert–Schmidt form $\operatorname{tr}(A^{\mathsf T}B)=\sum_{i,j}A_{ij}B_{ij}$ is positive definite and not invariant. This dichotomy is the third difference from $\mathbb{C}$, where $\operatorname{tr}(A^{*}B)$ is both. *The Trace Form and Its Indefinite Signature* and *The Hilbert–Schmidt Form: Definite but Not Invariant* prove the two halves of the statement.

## The Unit Group and the Two Components

**The unit group is $\mathrm{GL}_n(\mathbb{R})$, of dimension $n^{2}$.** It is the complement of $\Sigma$, open and dense, and a group under the product. The determinant is a surjective homomorphism

$$
\det:\mathrm{GL}_n(\mathbb{R})\longrightarrow\mathbb{R}^{\times},
$$

whose kernel is $\mathrm{SL}_n(\mathbb{R})$, of dimension $n^{2}-1$.

**The group has exactly two connected components, cut by the sign of the determinant.** The map $\det$ is continuous, so it is constant on each component, and it is onto $\mathbb{R}^{\times}$, which has two components; hence there are at least two. Each preimage is connected: by Gram–Schmidt $A=QR$ with $Q\in\mathrm{SO}(n)$ and $R$ upper triangular with positive diagonal, $Q$ is joined to $\mathrm{I}$ through rotations and $R$ through triangular matrices with positive diagonal, a convex set. The negative part is the translate $D\{\det>0\}$ with $D=\operatorname{diag}(-1,1,\dots,1)$.

**The two components are not the two halves.** $\operatorname{Sym}_n$ meets both, since $\mathrm{I}$ and $-\mathrm{I}$ are symmetric, so the cut by the sign of the determinant is topological and not linear.

## The Case $n=2$: $M_2(\mathbb{R})$ and $\mathbb{C}$

**As a real algebra $M_2(\mathbb{R})$ is not $\mathbb{C}$, and the two differ in dimension.** $M_2(\mathbb{R})$ has real dimension $4$ and $\mathbb{C}$ has real dimension $2$. The relation between them is that $\mathbb{C}$ sits inside $M_2(\mathbb{R})$ as a subalgebra, and the whole algebra is the split-quaternion algebra.

**The embedding.** The map $a+bi\mapsto\begin{pmatrix}a&-b\\ b&a\end{pmatrix}$ is an injective homomorphism of real algebras $\mathbb{C}\to M_2(\mathbb{R})$, whose image is the set of matrices commuting with $J=\begin{pmatrix}0&-1\\ 1&0\end{pmatrix}$, the image of $i$. So $\mathbb{C}$ sits in $M_2(\mathbb{R})$ as a subalgebra of dimension $2$, not as the whole algebra.

**The whole algebra is the split quaternions.** The matrices $\mathrm{I}$, $J$, $H=\operatorname{diag}(1,-1)$ and $P=\begin{pmatrix}0&1\\ 1&0\end{pmatrix}$ are a basis of $M_2(\mathbb{R})$, with $J^{2}=-\mathrm{I}$, $H^{2}=P^{2}=\mathrm{I}$ and $HP=-JH$. The multiplication table is that of $\mathbb{H}_{\mathrm{spl}}$ in *Split-Quaternion Algebra*, so $M_2(\mathbb{R})\cong\mathbb{H}_{\mathrm{spl}}$. The division algebra $\mathbb{H}$ is not a real matrix algebra: $M_2(\mathbb{R})$ has zero divisors.

**The trace form at $n=2$ has signature $(3,1)$.** The symmetric part is three-dimensional and positive definite; the antisymmetric part is one-dimensional, spanned by $J$, with $\operatorname{tr}(J^{2})=-2$. This is the form of signature $(3,1)$ of *Split-Quaternion Algebra*.

## Summary

$M_n(\mathbb{R})$ is the split central simple real algebra of dimension $n^{2}$, with centre $\mathbb{R}\mathrm{I}$ and matrix units $E_{ij}E_{kl}=\delta_{jk}E_{il}$. The trace is the only invariant linear functional, the determinant the multiplicative polynomial of degree $n$. The transpose is an involution of the first kind, with eigenspaces $\operatorname{Sym}_n$ and $\operatorname{Skew}_n$ of dimensions $n(n+1)/2$ and $n(n-1)/2$; for even $n$ a second class exists, with fixed space $\mathfrak{sp}_n$ of the same dimension. The trace form $\operatorname{tr}(AB)$ has signature $(n(n+1)/2,n(n-1)/2)$, so no form on the algebra is both definite and invariant. The unit group has two components, cut by the sign of the determinant. At $n=2$ the algebra is the split quaternions and contains $\mathbb{C}$ as the centraliser of $J$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M_n(\mathbb{R})$ | the algebra of $n\times n$ real matrices, of real dimension $n^{2}$ |
| $E_{ij}$ | the matrix unit, $1$ in the entry $(i,j)$ |
| $\mathrm{I}$ | the unit, $\sum_k E_{kk}$ |
| $\operatorname{tr}$, $\det$, $\operatorname{rk}$ | the trace, the determinant and the rank |
| ${}^{\mathsf T}$ | the transpose |
| $\operatorname{Sym}_n$, $\operatorname{Skew}_n$ | the symmetric and antisymmetric halves, of dimensions $n(n+1)/2$ and $n(n-1)/2$ |
| $\sigma_J(A)=-JA^{\mathsf T}J^{-1}$ | the symplectic involution, for even $n$ |
| $\langle A,B\rangle=\operatorname{tr}(AB)$ | the trace form, of signature $(n(n+1)/2,n(n-1)/2)$ |
| $\mathrm{GL}_n(\mathbb{R})$, $\mathrm{SL}_n(\mathbb{R})$ | the unit group and its determinant-one subgroup |
| $\Sigma=\{\det=0\}$ | the singular set, of codimension one |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the matrix algebra, its matrix units and its two-sided ideals.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the trace, the determinant, the rank and the transpose.
- [Split-Quaternion Algebra](split-quaternion-algebra.html), for the algebra $M_2(\mathbb{R})$ and its forms.
- [The Matrix Algebra $M_n(\mathbb{C})$](the-matrix-algebra-mnc.html), for the complex algebra that this one specializes.
- [The Matrix Algebra $M_3(\mathbb{C})$](the-matrix-algebra-m3c.html), for the same construction at a fixed dimension.
