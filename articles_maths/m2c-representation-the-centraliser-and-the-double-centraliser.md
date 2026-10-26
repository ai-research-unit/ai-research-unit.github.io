# __$M_2(\mathbb{C})$ Model : The Centraliser and the Double Centraliser__

## Introduction

For a non-scalar matrix the elements commuting with it form a commutative algebra, the plane of polynomials in the matrix, of complex dimension two; for a scalar matrix the commutant is the whole matrix algebra, of complex dimension four, which is not commutative. The double centraliser returns the same algebra in every case.

This article develops the commutant, the double commutant, the three spectral types, the eigenbasis ambiguity and the dimension count. It is the matrix form of *$M_2(\mathbb{C})$ Representation : The Centraliser and the Double Centraliser*, §*The Commutant*.

**Conventions.** The algebra and the model are those of *$M_2(\mathbb{C})$ Representation : The Matrix Product and the Algebra Structure*. The matrix of $\tilde Q$ is $X=\mathsf M_2(\tilde Q)$, and $\mathbb{C}[X]$ is the algebra of polynomials in $X$.

**Boundaries.** The module-theoretic commutant of an element and its double centraliser are *The Centraliser* and *The Category of Modules*, §*Endomorphisms and the Standard Bimodule*; the eigenbasis and its construction are *$M_2(\mathbb{C})$ Representation : The Eigenbasis and the Diagonalising Matrix*; the spectral projectors are *$M_2(\mathbb{C})$ Representation : The Spectral Projectors and the Nilpotents*.

## The Commutant

For $X\in M_2(\mathbb{C})$ the **commutant** or **centraliser** is

$$
C(X)=\{Y\in M_2(\mathbb{C}):XY=YX\},
$$

a unital subalgebra of $M_2(\mathbb{C})$ containing $\mathbb{C}[X]$. The **double commutant** is $C(C(X))$.

**Theorem.** For every $X$,

$$
C(X)=
\begin{cases}
M_2(\mathbb{C}), & X=\lambda\mathrm I_2,\\[2pt]
\mathbb{C}[X]=\operatorname{span}_{\mathbb{C}}\{\mathrm I_2,X\}, & X\neq\lambda\mathrm I_2,
\end{cases}
\qquad\text{and}\qquad
C\bigl(C(X)\bigr)=\mathbb{C}[X].
$$

In particular $C(X)$ has complex dimension $4$ for a scalar and complex dimension $2$ for a non-scalar.

*Proof.* The scalar case is clear. For the non-scalar case, put $X$ in Jordan form. If the eigenvalues are distinct, $X$ is conjugate to $\operatorname{diag}(\lambda_+,\lambda_-)$ with $\lambda_+\neq\lambda_-$; a commuting matrix is diagonal, and every diagonal matrix is a polynomial in $X$ by interpolation at the two eigenvalues. If the eigenvalue is repeated, $X$ is conjugate to $\lambda\mathrm I_2+N$ with $N\neq0$ and $N^2=0$; taking $N=E_{12}$, a matrix commuting with $N$ has the form $\begin{pmatrix}a&b\\0&a\end{pmatrix}=a\mathrm I_2+bN$. In both cases $\mathbb{C}[X]$ has complex dimension two and is maximal commutative, so $C(C(X))=C(X)=\mathbb{C}[X]$. $\square$

**The minimal polynomial.** The same computation reads

$$
\mathbb{C}[X]\cong\mathbb{C}[t]\big/\bigl(m_X(t)\bigr),
$$

where $m_X$ is the minimal polynomial. The three spectral types are the three factorisations of $m_X$.

| Type of $X$ | $m_X(t)$ | $\mathbb{C}[X]$ | Dimension over $\mathbb{C}$ |
|---|---|---|---|
| scalar | $t-\lambda$ | $\mathbb{C}$ | $1$ |
| non-scalar, distinct eigenvalues | $(t-\lambda_+)(t-\lambda_-)$ | $\mathbb{C}\times\mathbb{C}$ | $2$ |
| non-scalar, repeated eigenvalue | $(t-\lambda)^2$ | $\mathbb{C}[\varepsilon]/(\varepsilon^2)$ | $2$ |

The third row is the algebra of dual numbers: the nilpotent $\varepsilon=N$ squares to zero.

## The Three Types in the Eigenbasis

**Distinct eigenvalues.** Let $X=C\operatorname{diag}(\lambda_+,\lambda_-)C^{-1}$ with $\lambda_+\neq\lambda_-$. Conjugating by $C$,

$$
C^{-1}C(X)C=\left\{\begin{pmatrix}a&0\\0&b\end{pmatrix}:a,b\in\mathbb{C}\right\}.
$$

The commutant is spanned by the two spectral projectors

$$
\Pi_+=\frac{X-\lambda_-\mathrm I_2}{\lambda_+-\lambda_-},\qquad
\Pi_-=\frac{X-\lambda_+\mathrm I_2}{\lambda_--\lambda_+},
$$

which satisfy $\Pi_++\Pi_-=\mathrm I_2$ and $\Pi_+\Pi_-=0$. The isomorphism $\mathbb{C}[X]\to\mathbb{C}\times\mathbb{C}$ is evaluation at the two eigenvalues, $Y\mapsto(\mu_+,\mu_-)$ when $Y=\mu_+\Pi_++\mu_-\Pi_-$.

**Repeated eigenvalue.** Let $X=\lambda\mathrm I_2+N$ with $N\neq0$ and $N^2=0$. The commutant is

$$
C(X)=\{a\mathrm I_2+bN\},
$$

the dual numbers, with $N$ the nilpotent direction. In the Jordan basis it is the algebra of upper triangular matrices with equal diagonal entries.

**Scalar.** For $X=\lambda\mathrm I_2$ every matrix commutes, $C(X)=M_2(\mathbb{C})$, and $\mathbb{C}[X]=\mathbb{C}\mathrm I_2$.

## The Adjugate and the Dagger in the Commutant

**The adjugate.** By Cayley–Hamilton,

$$
\operatorname{adj}X=(\operatorname{Tr}X)\mathrm I_2-X,
$$

so the adjugate lies in $\mathbb{C}[X]\subseteq C(X)$ for every $X$. In particular a matrix commutes with its adjugate, and for an invertible $X$ the inverse $X^{-1}=\operatorname{adj}X/\det X$ lies in the commutant as well.

**The dagger.** The Hermitian conjugate lies in the commutant exactly when $X$ is normal:

$$
X^{\dagger}\in C(X)\iff XX^{\dagger}=X^{\dagger}X .
$$

For a normal matrix the spectral theorem writes $X=U\operatorname{diag}(\lambda_1,\lambda_2)U^{\dagger}$, and $X^{\dagger}=U\operatorname{diag}(\bar\lambda_1,\bar\lambda_2)U^{\dagger}$ is the Lagrange interpolation of the conjugate eigenvalues, hence a polynomial in $X$. For a non-normal matrix the two matrices $X$ and $X^{\dagger}$ do not commute, and the dagger lies outside the commutant.

**The reading.** The commutant is the polynomial algebra for every non-scalar matrix; the adjugate is the degree-one element that is always inside it, and the dagger is the degree-one element that is inside it exactly on the normal locus.

## The Eigenbasis and Its Ambiguity

**Proposition.** Let $X$ have distinct eigenvalues. The matrices $C$ with $C^{-1}XC$ diagonal are exactly

$$
C=C_0D,\qquad D=\operatorname{diag}(d_+,d_-),\quad d_+d_-\neq0,
$$

where $C_0$ is one such matrix.

*Proof.* The columns of $C$ are eigenvectors, each determined up to a nonzero scalar; the two eigenspaces are one-dimensional and distinct. $\square$

**Corollary.** The eigenbasis is unique up to the independent rescaling of its two columns, and the ambiguity is the group of invertible diagonal matrices, which is the group of units of the commutant in the eigenbasis.

**The degenerate analogue.** For a non-scalar Jordan block there is no eigenbasis, but the commutant still acts: the matrices commuting with $X$ are $\{a\mathrm I_2+bN\}$, and the only unit is $a\neq0$ with $b$ arbitrary, the group $\mathbb{C}^\times\ltimes\mathbb{C}$.

## The Double Centraliser

**Theorem.** For every $X$,

$$
C\bigl(C(X)\bigr)=\mathbb{C}[X].
$$

*Proof.* The inclusion $\mathbb{C}[X]\subseteq C(C(X))$ is clear. Conversely, if $X$ is non-scalar, $C(X)=\mathbb{C}[X]$ is maximal commutative, so an element commuting with all of $\mathbb{C}[X]$ commutes with $X$ and lies in $C(X)=\mathbb{C}[X]$. If $X$ is scalar, $C(X)=M_2(\mathbb{C})$ and $C(M_2(\mathbb{C}))=\mathbb{C}\mathrm I_2=\mathbb{C}[X]$. $\square$

**The module reading.** The statement is the double centraliser theorem for the algebra $\mathbb{C}[X]$ acting on $\mathbb{C}^2$: the commutant in $M_2(\mathbb{C})$ of the commutant of $\mathbb{C}[X]$ is $\mathbb{C}[X]$ itself. In the algebra it is the same statement for $\mathbb{C}[\tilde X]$ acting on the defining module (*The Category of Modules*, §*Endomorphisms and the Standard Bimodule*).

**The dimension count.** The double centraliser does not enlarge the algebra: the chain

$$
\mathbb{C}[X]\subseteq C(C(X))=C(X)
$$

is an equality for non-scalar $X$, and for scalar $X$ it reads $\mathbb{C}\mathrm I_2=C(M_2(\mathbb{C}))\subsetneq M_2(\mathbb{C})=C(X)$.

## Summary

The commutant of a non-scalar $2\times2$ matrix is the plane $\mathbb{C}[X]=\operatorname{span}\{\mathrm I_2,X\}$, of complex dimension two, and the commutant of a scalar is the whole algebra. The plane is $\mathbb{C}\times\mathbb{C}$ for distinct eigenvalues, with the two spectral projectors as a basis of idempotents, and the dual numbers $\mathbb{C}[\varepsilon]/(\varepsilon^2)$ for a non-scalar Jordan block. The double commutant returns $\mathbb{C}[X]$ in every case. The eigenbasis of a matrix with distinct eigenvalues is unique up to the independent rescaling of its two columns, and that ambiguity is the group of units of the commutant.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $C(X)=\{Y:XY=YX\}$ | the commutant |
| $C(C(X))$ | the double commutant |
| $\mathbb{C}[X]$ | the algebra of polynomials in $X$ |
| $m_X$ | the minimal polynomial of $X$ |
| $\Pi_\pm$ | the spectral projectors of a matrix with distinct eigenvalues |
| $N$ | the nilpotent part of a Jordan block, $N^2=0$ |
| $\mathbb{C}[\varepsilon]/(\varepsilon^2)$ | the dual numbers, the commutant of a non-scalar Jordan block |

## Further Reading

- [Modules over the Biquaternion Algebra](modules-over-the-biquaternion-algebra.html), for the commutant of an element and the double centraliser theorem
- [$M_2(\mathbb{C})$ Representation : The Eigenbasis and the Diagonalising Matrix](m2c-representation-the-eigenbasis-and-the-diagonalising-matrix.html), for the eigenbasis and its construction
- [$M_2(\mathbb{C})$ Representation : The Spectral Projectors and the Nilpotents](m2c-representation-the-spectral-projectors-and-the-nilpotents.html), for the projectors and the Jordan types
- [$M_2(\mathbb{C})$ Representation : The Functional Calculus](m2c-representation-the-functional-calculus.html), for the use of the commutant in both reductions
- [Square Roots of One and the Idempotents of the Biquaternion Algebra](square-roots-of-one-and-the-idempotents-of-the-biquaternion-algebra.html), for the spectral projectors in the algebra
