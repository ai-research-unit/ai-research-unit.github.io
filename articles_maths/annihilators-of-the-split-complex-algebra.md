# __Annihilators of the Split-Complex Algebra__

## Introduction

Being a zero divisor of a product is a property of one element alone: it says that *some* nonzero partner exists that the element kills. The annihilator says *which* partners those are, and it is the finer object. It is the set of elements killed by a fixed element,

$$
A(Q_2)=\{Q_1:Q_2Q_1=0\},\qquad B(Q_2)=\{Q_1:Q_1Q_2=0\},
$$

the left and the right annihilator (*Definitions for the Study of the Algebraic Structures over the Biquaternion $\mathbb{C}$ Space*, §*The Zero Divisor and the Annihilator*). When the product is carried by a multiplication operator the annihilator is the kernel of that operator, so it is a linear subspace.

The block of this article is the **general plain multiplication**, the plain product of the split-complex algebra,

$$
Q_2Q_1=(q_2q_1+q'_2q'_1)+j(q_2q'_1+q'_2q_1).
$$

It is associative, commutative and unital, and the algebra is the product of two copies of $\mathbb{R}$, isomorphic to $\mathbb{R}\times\mathbb{R}$. Its zero divisors are the nonzero elements of the null cone $\mathcal{N}$, and such an element is a rank-one matrix in the regular matrix model (*Zero Divisors of the Split-Complex Algebra*, above this article in this category). The annihilator is the kernel of the corresponding multiplication: it is $\{0\}$ off the null cone, a real line on the nonzero part of the cone, and the whole algebra at the origin, and because the algebra is commutative the two sides carry the **same** subspace. The article owns that reading, the multiplication operators with their ranks, and the shape of the annihilator on the distinguished subspaces; the zero-divisor set is the cited article's.

**The results.** The annihilator of an element is the set of partners that it kills. For the general plain product the multiplication operator $L_Q$ has trace $2q$ and determinant $Q\bar Q=q^{2}-q'^{2}$; its rank is $2$ off the null cone, $1$ on the nonzero part of the cone, and $0$ at the origin. Both annihilators of an element coincide; they are trivial off the null cone, a real line on the nonzero part of the cone, and the whole algebra at the origin. The two null lines annihilate one another, $\operatorname{ann}(\mathbb{R}\Pi_{+})=\mathbb{R}\Pi_{-}$ and $\operatorname{ann}(\mathbb{R}\Pi_{-})=\mathbb{R}\Pi_{+}$; the annihilator of the origin is the whole algebra, and the annihilator of the whole algebra is the origin.

## The Annihilator of a Product

**The annihilator of an element is the set of partners that it kills; the left annihilator is the kernel of the left multiplication and the right annihilator is the kernel of the right multiplication, and for a nonzero element both are nonzero exactly when the element is a zero divisor of the corresponding side.**

**Definition (annihilator).** Let $\star$ be a product on $\mathbb{D}$ and let $Q_2\in\mathbb{D}$. The **left annihilator** and the **right annihilator** of $Q_2$ in $\star$ are

$$
A_\star(Q_2)=\{Q_1:Q_2\star Q_1=0\},\qquad
B_\star(Q_2)=\{Q_1:Q_1\star Q_2=0\}.
$$

They are the kernels of the left and the right multiplication. For $Q_2\neq0$ they are nonzero exactly when $Q_2$ is a zero divisor of the corresponding side; at $Q_2=0$ the annihilator is the whole algebra, although $0$ is not a zero divisor.

Throughout this article the product is the **general plain multiplication** $\star$, and unqualified, *annihilator* means the annihilator of $\star$. The two one-sided multiplications are the operators

$$
L_{Q_2}Q_1=Q_2Q_1,\qquad R_{Q_2}Q_1=Q_1Q_2,
$$

the left and the right multiplication of the plain algebra. The block is the parent of the other products of the space: it is associative and commutative, and its annihilators are the model for the two-sided reading. The block carries an involution, the conjugation, which is an automorphism; because the product is commutative, the involution does not separate the sides, and the two annihilators of an element are equal.

**Proposition (the two sides coincide).** For every $Q_2\in\mathbb{D}$,

$$
\boxed{\;A(Q_2)=B(Q_2)\;}.
$$

**Proof.** The plain product is commutative, so $Q_2Q_1=Q_1Q_2$ for every $Q_1$, and the two defining equations are the same.

**Proposition (the annihilator is an ideal).** For every $Q_2$, the annihilator $A(Q_2)$ is an ideal of the plain algebra.

**Proof.** If $Q_1,Q_1'\in A(Q_2)$ then $Q_2(Q_1+Q_1')=Q_2Q_1+Q_2Q_1'=0$, so the set is closed under addition. If $Q_1\in A(Q_2)$ and $R\in\mathbb{D}$ then $Q_2(RQ_1)=R(Q_2Q_1)=0$, so it is closed under multiplication by arbitrary elements. It is nonempty because it contains $0$.

## The Multiplication Operators and Their Ranks

**The left multiplication $L_Q$ is the real-linear operator of matrix $\begin{pmatrix}q&q'\\q'&q\end{pmatrix}$ in the basis $1,j$; its trace is $2q$, its determinant is $Q\bar Q=q^{2}-q'^{2}$, and its rank is $2$ off the null cone, $1$ on the nonzero part of the cone, and $0$ at the origin.**

**Definition.** For $Q\in\mathbb{D}$ the **left multiplication** by $Q$ is the map

$$
L_Q:\mathbb{D}\longrightarrow\mathbb{D},\qquad L_Q(B)=QB.
$$

Because the algebra is commutative, $L_Q=R_Q$, and the article writes $L_Q$ for both.

**Proposition (the matrix).** In the basis $1,j$ the operator $L_Q$ has the matrix

$$
\mathsf{L}(Q)=\begin{pmatrix}q&q'\\q'&q\end{pmatrix},
$$

with trace $2q$ and determinant $q^{2}-q'^{2}=Q\bar Q$.

**Proof.** $L_Q(1)=Q=q+jq'$ and $L_Q(j)=Qj=q'+jq$; the two columns are the coordinates of these images, $(q,q')$ and $(q',q)$. The trace and the determinant are read from the matrix.

**Proposition (the rank).** The rank of $L_Q$ is

$$
\boxed{\;\operatorname{rank}L_Q=
\begin{cases}
2, & Q\bar Q\neq0,\\
1, & Q\bar Q=0\text{ and }Q\neq0,\\
0, & Q=0.
\end{cases}\;}
$$

**Proof.** The determinant is $Q\bar Q$, so the rank is $2$ exactly when the determinant is nonzero. When $Q\neq0$ and $Q\bar Q=0$, the matrix is nonzero and singular, so its rank is $1$. At $Q=0$ the matrix is zero.

**Corollary (the kernel is the annihilator).** For every $Q$,

$$
\ker L_Q=A(Q)=\{B:QB=0\}.
$$

The rank-nullity theorem gives

$$
\dim A(Q)=2-\operatorname{rank}L_Q,
$$

so the annihilator has dimension $0$ off the null cone, dimension $1$ on the nonzero part of the cone, and dimension $2$ at the origin.

**Remark (the eigenvalues and the eigenlines).** The characteristic polynomial of $\mathsf{L}(Q)$ is

$$
\lambda^{2}-2q\lambda+(q^{2}-q'^{2})=(\lambda-Q_{+})(\lambda-Q_{-}),
$$

so the eigenvalues are the idempotent coordinates $Q_{+}=q+q'$ and $Q_{-}=q-q'$, with eigenvectors $\Pi_{+}$ and $\Pi_{-}$. The operator is diagonal in the idempotent basis, $L_Q\Pi_{\pm}=Q_{\pm}\Pi_{\pm}$; it is singular exactly when one eigenvalue vanishes, and then its kernel is the eigenline of the vanishing eigenvalue. The matrix is symmetric, so $L_Q$ is self-adjoint for the Euclidean form.

## The Annihilator of an Element

**The annihilator of a nonzero element is $\{0\}$ off the null cone and the opposite null line on the cone; the annihilator of the origin is the whole algebra.**

**Theorem (the annihilator).** For $Q\in\mathbb{D}$,

$$
A(Q)=
\begin{cases}
\{0\}, & Q\bar Q\neq0,\\
\mathbb{R}\Pi_{-}, & Q=\lambda\Pi_{+},\ \lambda\neq0,\\
\mathbb{R}\Pi_{+}, & Q=\lambda\Pi_{-},\ \lambda\neq0,\\
\mathbb{D}, & Q=0.
\end{cases}
$$

**Proof.** The first case is the invertibility criterion: if $Q$ is a unit then $QB=0$ implies $B=Q^{-1}0=0$. For the second, write $B=B_{+}\Pi_{+}+B_{-}\Pi_{-}$; then $QB=\lambda B_{+}\Pi_{+}$, which vanishes exactly when $B_{+}=0$, that is $B\in\mathbb{R}\Pi_{-}$. The third case is symmetric. The fourth is the definition: $0\cdot B=0$ for every $B$.

**Corollary (the dichotomy).** A nonzero element is a zero divisor exactly when its annihilator is nonzero, and then the annihilator is a line. The annihilator of a zero divisor is never the line that carries the element itself: the two null lines annihilate one another.

**Remark (the origin is not a zero divisor).** The origin has the largest annihilator, the whole algebra, and it is excluded from the zero-divisor set. The annihilator is therefore not a faithful witness of the zero-divisor property at the origin: it is maximal there, while the element is not a divisor. The convention is the one of *Zero Divisors of the Split-Complex Algebra*.

## The Annihilator of an Ideal

**The annihilator of an ideal is an ideal, and on the two minimal ideals it exchanges them: $\operatorname{ann}(\mathbb{R}\Pi_{+})=\mathbb{R}\Pi_{-}$, $\operatorname{ann}(\mathbb{R}\Pi_{-})=\mathbb{R}\Pi_{+}$; the annihilator of the whole algebra is the origin, and the annihilator of the origin is the whole algebra.**

**Definition.** For a subset $S\subseteq\mathbb{D}$ the **annihilator** of $S$ is

$$
\operatorname{ann}(S)=\{B:QB=0\text{ for every }Q\in S\}.
$$

For an ideal $I$ the annihilator is an ideal, and it is the intersection of the annihilators of the elements of $I$.

**Proposition (the minimal ideals).** The two minimal ideals are the two null lines, and

$$
\boxed{\;\operatorname{ann}(\mathbb{R}\Pi_{+})=\mathbb{R}\Pi_{-},\qquad
\operatorname{ann}(\mathbb{R}\Pi_{-})=\mathbb{R}\Pi_{+}\;}.
$$

**Proof.** The annihilator of $\mathbb{R}\Pi_{+}$ is the intersection over $\lambda\neq0$ of $\operatorname{ann}(\lambda\Pi_{+})$, each of which is $\mathbb{R}\Pi_{-}$; the intersection is $\mathbb{R}\Pi_{-}$. The other case is symmetric.

**Proposition (the two extremes).**

$$
\operatorname{ann}(\mathbb{D})=\{0\},\qquad \operatorname{ann}(\{0\})=\mathbb{D}.
$$

**Proof.** If $B$ annihilates every element, it annihilates $1$, so $B=0$. Every element annihilates $0$.

**Proposition (the null cone).** $\operatorname{ann}(\mathcal{N})=\{0\}$.

**Proof.** The null cone contains $\Pi_{+}$ and $\Pi_{-}$, so an annihilator of the cone lies in $\mathbb{R}\Pi_{-}\cap\mathbb{R}\Pi_{+}=\{0\}$.

**Corollary (the double annihilator).** On the ideals of $\mathbb{D}$ the annihilator is an involution:

$$
\operatorname{ann}(\operatorname{ann}(I))=I
$$

for $I=0$, $I=\mathbb{R}\Pi_{+}$, $I=\mathbb{R}\Pi_{-}$ and $I=\mathbb{D}$.

**Proof.** Direct from the two propositions: $\operatorname{ann}(\operatorname{ann}(0))=\operatorname{ann}(\mathbb{D})=0$; $\operatorname{ann}(\operatorname{ann}(\mathbb{R}\Pi_{+}))=\operatorname{ann}(\mathbb{R}\Pi_{-})=\mathbb{R}\Pi_{+}$; the other line is symmetric; $\operatorname{ann}(\operatorname{ann}(\mathbb{D}))=\operatorname{ann}(0)=\mathbb{D}$.

## The Annihilator on the Distinguished Subspaces

**On the two eigenspaces of the conjugation every nonzero element has zero annihilator; on the two idempotent lines every nonzero element has the opposite line as its annihilator; the origin has the whole algebra.**

The distinguished one-dimensional subspaces are the real line $\mathbb{R}_{\mathbb{D}}$, the split imaginary line $j\mathbb{R}_{\mathbb{D}}$, and the two idempotent lines $\mathbb{R}\Pi_{+}$ and $\mathbb{R}\Pi_{-}$.

### The Real Subspace $\mathbb{R}_{\mathbb{D}}$

For $Q=q\neq0$ the operator $L_Q$ is multiplication by the nonzero real number $q$, of rank $2$ and kernel $\{0\}$. Every nonzero real number is a unit, and its annihilator is trivial.

### The Split Imaginary Subspace $j\mathbb{R}_{\mathbb{D}}$

For $Q=jq'$ with $q'\neq0$ the operator $L_Q$ is multiplication by $jq'$, of matrix $\begin{pmatrix}0&q'\\q'&0\end{pmatrix}$, of determinant $-q'^{2}\neq0$ and rank $2$. The annihilator is $\{0\}$.

### The Idempotent Lines

For $Q=\lambda\Pi_{+}$ with $\lambda\neq0$ the matrix is $\lambda\begin{pmatrix}1&1\\1&1\end{pmatrix}$, of rank $1$ and kernel $\mathbb{R}(1,-1)=\mathbb{R}\Pi_{-}$. For $Q=\lambda\Pi_{-}$ the matrix is $\lambda\begin{pmatrix}1&-1\\-1&1\end{pmatrix}$, of rank $1$ and kernel $\mathbb{R}(1,1)=\mathbb{R}\Pi_{+}$.

### Summary of the Distribution

| subspace | $Q$ | rank $L_Q$ | annihilator |
|---|---|---|---|
| $\mathbb{R}_{\mathbb{D}}$ | $q\neq0$ | $2$ | $\{0\}$ |
| $j\mathbb{R}_{\mathbb{D}}$ | $jq'\neq0$ | $2$ | $\{0\}$ |
| $\mathbb{R}\Pi_{+}$ | $\lambda\Pi_{+}\neq0$ | $1$ | $\mathbb{R}\Pi_{-}$ |
| $\mathbb{R}\Pi_{-}$ | $\lambda\Pi_{-}\neq0$ | $1$ | $\mathbb{R}\Pi_{+}$ |
| $\{0\}$ | $0$ | $0$ | $\mathbb{D}$ |

## The Annihilator and the Matrix Model

**In the regular matrix model the annihilator is the kernel of the matrix $\begin{pmatrix}q&q'\\q'&q\end{pmatrix}$; the rank-one matrices of the null cone have a one-dimensional kernel, and the kernel is the opposite null line.**

The regular representation sends $Q$ to the matrix

$$
\mathsf{M}(Q)=\begin{pmatrix}q&q'\\q'&q\end{pmatrix},
$$

an injective homomorphism of the algebra into $M_2(\mathbb{R})$ (*The Matrix Element Representations of the Split-Complexoid*). The left multiplication $L_Q$ is the same matrix acting on column vectors, and its kernel is the annihilator:

$$
\ker\mathsf{M}(Q)=A(Q).
$$

Off the null cone the determinant is nonzero and the kernel is $\{0\}$; on the nonzero part of the cone the determinant is zero and the rank is one, so the kernel is a line. The eigenvectors of $\mathsf{M}(Q)$ are $\Pi_{+}$ and $\Pi_{-}$, with eigenvalues $Q_{+}$ and $Q_{-}$; the kernel is the eigenline of the vanishing eigenvalue, which is the opposite null line. The matrix model therefore reads the annihilator as the kernel of a singular $2\times2$ matrix of rank one.

## Summary

The annihilator of an element is the set of partners that it kills. For the plain product the two sides coincide, $A(Q)=B(Q)$, and the annihilator is an ideal and the kernel of the multiplication operator $L_Q$, of matrix $\begin{pmatrix}q&q'\\q'&q\end{pmatrix}$, trace $2q$ and determinant $Q\bar Q$. Its rank is $2$ off the null cone, $1$ on the nonzero part of the cone, and $0$ at the origin, so the annihilator is $\{0\}$ off the cone, the opposite null line on the cone, and the whole algebra at the origin:

$$
A(Q)=
\begin{cases}
\{0\}, & Q\bar Q\neq0,\\
\mathbb{R}\Pi_{-}, & Q=\lambda\Pi_{+},\ \lambda\neq0,\\
\mathbb{R}\Pi_{+}, & Q=\lambda\Pi_{-},\ \lambda\neq0,\\
\mathbb{D}, & Q=0.
\end{cases}
$$

The two null lines annihilate one another, the annihilator of the whole algebra is the origin, the annihilator of the origin is the whole algebra, and the double annihilator restores every ideal. On the two eigenspaces of the conjugation the annihilator is trivial away from the origin; on the two idempotent lines it is the opposite line; the origin has the whole algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}$ | Split complex algebra |
| $Q=q+jq'$ | General split complex number |
| $L_Q(B)=QB$ | Left multiplication by $Q$; equal to the right multiplication |
| $\mathsf{L}(Q)=\begin{pmatrix}q&q'\\q'&q\end{pmatrix}$ | Matrix of $L_Q$ in the basis $1,j$ |
| $A(Q)=\ker L_Q=\{B:QB=0\}$ | Annihilator of $Q$; equal to the right annihilator |
| $\operatorname{ann}(S)=\{B:QB=0\ \forall Q\in S\}$ | Annihilator of a set |
| $\operatorname{ann}(\mathbb{R}\Pi_{\pm})=\mathbb{R}\Pi_{\mp}$ | The two null lines annihilate one another |
| $\operatorname{ann}(\mathbb{D})=\{0\}$, $\operatorname{ann}(\{0\})=\mathbb{D}$ | The two extremes |
| $\operatorname{ann}(\operatorname{ann}(I))=I$ | The double annihilator on the ideals |
| $Q_{\pm}=q\pm q'$ | Eigenvalues of $L_Q$, with eigenvectors $\Pi_{\pm}$ |

## Further Reading

- [Zero Divisors of the Split-Complex Algebra](zero-divisors-of-the-split-complex-algebra.html), for the zero-divisor set, its two families and the criterion.
- [Norm and Invertibility in the General Split-Complex Algebra](norm-and-invertibility-in-the-general-split-complex-algebra.html), for the invertibility criterion and the group of units.
- [Ideals and Peirce Decomposition of the Split-Complex Algebra](ideals-and-peirce-decomposition-of-the-split-complex-algebra.html), for the two minimal ideals and the Peirce decomposition.
- [The Matrix Element Representations of the Split-Complexoid](the-matrix-element-representations-of-the-split-complexoid.html), for the regular matrix model and its kernel.
- [The Two Products of the Split-Complexoid Space](the-two-products-of-the-split-complexoid-space.html), for the two products and the multiplication operators.
