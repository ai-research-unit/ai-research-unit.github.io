# __Introduction to the $2\times2$ Matrix Element Representation of Reduced Biquaternions__

## Introduction

The **$2\times2$ matrix element representation** writes the reduced biquaternion as the matrix of its own multiplication. The regular representation sends $T$ to the operator $L_{T}:W\mapsto TW$ on the complex two-dimensional space of the algebra, and that operator is a $2\times2$ matrix with **complex** entries; on the real four-dimensional space the same operator is a $4\times4$ matrix with **real** entries. This article writes the two models, explains why the signs of the entries are forced by $j^{2}=+1$, records the trace, the determinant and the norm, and shows how the change to the idempotent basis diagonalises the matrix. The multiplication is **commutative**, so the matrix is symmetric, and it **has zero divisors**, so the matrix may be singular at a non-zero element. The diagonal model of the algebra itself — the isomorphism onto the diagonal matrices and the structure read there — is *The General Plain Algebra in the $2\times2$ Matrix Element Representation of the Reduced Biquaternions*; this article is about the element as a matrix, not about the structure.

**Conventions.** The basis is $1,i,j,ij$ with $i^{2}=-1$, $j^{2}=+1$, $ji=ij$; the element is $T=A+Bj$ with $A=a+ia'$, $B=b+ib'$; the idempotents are $\Pi_{1,2}=\tfrac12(1\pm j)$ and the idempotent coordinates are $q_1=A+B$, $q_2=A-B$, with $T=q_1\Pi_{1}+q_2\Pi_{2}$. The four products and the forms $B,N,H,K$ are *The Four Products, Their Forms and Their Algebraic Norms*, and the multiplication operators in general are *Operators on the Reduced Biquaternions*. The element glyph is $T$, without a tilde.

**Boundaries.** The regular representation is defined in *Introduction to Reduced Biquaternion Element Representations*; the four-vector reading of the same element is *The Four-Vector Element Representation of the Reduced Biquaternions*; the diagonal model of the algebra is *The General Plain Algebra in the $2\times2$ Matrix Element Representation of the Reduced Biquaternions*; the other presentations are *Reduced Biquaternion Other Algebraic Element Representations*; and the operators of the four products are collected in *Operators on the Reduced Biquaternions*. The biquaternion counterpart is *Introduction to the $2\times2$ Matrix Element Representation $M_{2}(\mathbb{C})$ of Biquaternions*, where the image is the whole of $M_{2}(\mathbb{C})$.

## The Regular Representation as a Matrix

**The regular representation sends the element to the matrix with the two columns $A,B$ and $B,A$.**

### The Map on the Basis

**Definition.** The **matrix element representation** is
$$
\varphi(T)=\begin{pmatrix}A&B\\ B&A\end{pmatrix},
$$
the matrix of the left multiplication $W\mapsto TW$ on the complex basis $1,j$ of $\mathbb{B}_{\mathrm{r}}$.

**Proposition (the images of the basis).** On the real basis,
$$
\varphi(1)=\begin{pmatrix}1&0\\ 0&1\end{pmatrix}=\mathrm I_{2},\qquad
\varphi(i)=\begin{pmatrix}i&0\\ 0&i\end{pmatrix}=i\,\mathrm I_{2},\qquad
\varphi(j)=\begin{pmatrix}0&1\\ 1&0\end{pmatrix}=\sigma_{1},\qquad
\varphi(ij)=i\,\sigma_{1}.
$$

*Proof.* $L_{1}=\operatorname{id}$ and $L_{i}$ is multiplication by the central complex unit $i$ on both coordinates, hence $i\mathrm I_{2}$; $L_{j}(1)=j$ and $L_{j}(j)=j^{2}=1$, giving the columns $\binom{0}{1}$ and $\binom{1}{0}$, that is $\sigma_{1}$; and $L_{ij}=L_{i}L_{j}=i\sigma_{1}$.

### The Matrix of an Element

**Theorem (the matrix).** The map $\varphi$ is an injective homomorphism of $\mathbb{C}$-algebras, $\varphi(TW)=\varphi(T)\varphi(W)$ and $\varphi(1)=\mathrm I_{2}$, with the block form
$$
\varphi(T)=\begin{pmatrix}A&B\\ B&A\end{pmatrix}=\begin{pmatrix}a&-a'\\ a'&a\end{pmatrix}+j\begin{pmatrix}b&-b'\\ b'&b\end{pmatrix}
$$
over the real basis, using $i=\begin{smallmatrix}0&-1\\ 1&0\end{smallmatrix}$.

*Proof.* The product rule is read from $TW=(AC+BD)+(AD+BC)j$: the matrix product $\begin{smallmatrix}A&B\\ B&A\end{smallmatrix}\begin{smallmatrix}C&D\\ D&C\end{smallmatrix}=\begin{smallmatrix}AC+BD&AD+BC\\ BC+AD&BD+AC\end{smallmatrix}$ has the two diagonal entries $AC+BD$ and the two off-diagonal entries $AD+BC$, which is $\varphi(TW)$. The injectivity is $\varphi(T)=0\Rightarrow A=B=0\Rightarrow T=0$. The real display is $\varphi(i)=i\mathrm I_{2}$ and $\varphi(j)=\sigma_{1}$ written in the real $2\times2$ basis.

**Corollary (the image is not the whole matrix algebra).** The image $\varphi(\mathbb{B}_{\mathrm{r}})$ is a commutative two-dimensional subalgebra of $M_{2}(\mathbb{C})$ — the matrices of the form $\begin{smallmatrix}A&B\\ B&A\end{smallmatrix}$ — and not the whole of $M_{2}(\mathbb{C})$, which has complex dimension four. The biquaternion companion is realised as the whole of $M_{2}(\mathbb{C})$; here the commutativity forces the two diagonal entries to be equal and the two off-diagonal entries to be equal, halving the linear dimension.

*Proof.* The displayed form shows that the image is spanned over $\mathbb{C}$ by $\mathrm I_{2}$ and $\sigma_{1}$, of complex dimension two; the matrix $\operatorname{diag}(1,0)$ is not of the form and so is not in the image.

## Why the Signs Are Forced

**The images must satisfy $\varphi(i)^{2}=-\mathrm I_{2}$, $\varphi(j)^{2}=+\mathrm I_{2}$ and $\varphi(i)\varphi(j)=\varphi(j)\varphi(i)$, and these force the shape.**

**Theorem (the shape is forced).** Let $\varphi$ be an injective homomorphism of $\mathbb{C}$-algebras with $\varphi(i)=i\mathrm I_{2}$. Then $\varphi(j)^{2}=\mathrm I_{2}$, so $\varphi(j)$ is an involution; if in addition $\varphi(j)$ has trace $0$ and is symmetric, then $\varphi(j)=\varepsilon\,\sigma_{1}$ with $\varepsilon=\pm1$ in the basis $1,j$, and the image of $T$ is $\begin{smallmatrix}A&\varepsilon B\\ \varepsilon B&A\end{smallmatrix}$, which the normalisation $\varepsilon=+1$ reduces to the matrix of §*The Regular Representation*.

*Proof.* From $\varphi(i)^{2}=\varphi(i^{2})=\varphi(-1)=-\mathrm I_{2}$ the image of $i$ is $i\mathrm I_{2}$ up to conjugation in the centre, which is scalar; from $\varphi(j)^{2}=\varphi(j^{2})=\varphi(1)=\mathrm I_{2}$ the image of $j$ is an involution. A traceless symmetric involution of $\mathbb{C}^{2}$ has $\sigma_{1}$ as its normal form, because its eigenvalues are $+1,-1$ with orthogonal eigendirections; and $ij=ji$ forces $\varphi(j)$ to commute with $\varphi(i)=i\mathrm I_{2}$, which is automatic. Reading $T=A+Bj$ through $\varphi$ with $\varphi(j)=\sigma_{1}$ gives $\begin{smallmatrix}A&B\\ B&A\end{smallmatrix}$.

**Remark (the other normal form).** The same element is sent to the **diagonal** matrix $\operatorname{diag}(q_1,q_2)$ in the idempotent basis, where the image of $j$ is $\sigma_{3}=\operatorname{diag}(1,-1)$ instead of $\sigma_{1}$; the two normal forms are conjugate by the change of basis of §*The Diagonal Model*. The choice between $\sigma_{1}$ and $\sigma_{3}$ is the choice between writing the element and writing the algebra, and the algebra is the diagonal picture of *The General Plain Algebra in the $2\times2$ Matrix Element Representation of the Reduced Biquaternions*.

## The Real-Entry Model

**On the real four-dimensional space the same operator is a real $4\times4$ matrix with the repeated-block form.**

**Theorem (the real matrix).** For $T=a+ia'+bj+ib'j$, the left multiplication on the real basis $1,i,j,ij$ is
$$
L_{T}=\begin{pmatrix}
a&-a'&b&-b'\\
a'&a&b'&b\\
b&-b'&a&-a'\\
b'&b&a'&a
\end{pmatrix}
=\begin{pmatrix}\tilde A&\tilde B\\ \tilde B&\tilde A\end{pmatrix},
\qquad
\tilde A=\begin{pmatrix}a&-a'\\ a'&a\end{pmatrix},\quad
\tilde B=\begin{pmatrix}b&-b'\\ b'&b\end{pmatrix}.
$$

*Proof.* This is the real form of the complex matrix of §*The Matrix of an Element*, read by *The Four-Vector Element Representation of the Reduced Biquaternions*, §*Multiplication in Four-Vector Form*: each complex entry $A$ becomes the real $2\times2$ block $\tilde A$ and each entry $B$ the block $\tilde B$, and the two $2\times2$ blocks of the complex matrix become the four blocks of the real one.

**Corollary (the two models agree).** The real matrix is the realification of the complex one: the complex $2\times2$ model and the real $4\times4$ model are the same operator on the same space read over the two base fields, and the real one carries the four real coordinates of *The Four-Vector Element Representation of the Reduced Biquaternions*.

*Proof.* The realification of a complex matrix replaces each entry by its real $2\times2$ block, which is exactly the passage from $\begin{smallmatrix}A&B\\ B&A\end{smallmatrix}$ to the displayed matrix.

## Trace, Determinant and the Norm

**The trace is twice the scalar complex coordinate, the determinant is the reduced norm, and the element is invertible exactly when the determinant does not vanish.**

**Theorem (the invariants).** For $T=A+Bj$,
$$
\operatorname{tr}\varphi(T)=2A,\qquad \det\varphi(T)=\langle T\rangle_{\natural}=A^{2}-B^{2}=q_1q_2,
$$
and for the real matrix
$$
\operatorname{tr}L_{T}=4a,\qquad \det L_{T}=\lvert \langle T\rangle_{\natural}\rvert^{2}=\lvert q_1\rvert^{2}\lvert q_2\rvert^{2}.
$$

*Proof.* The trace of $\begin{smallmatrix}A&B\\ B&A\end{smallmatrix}$ is $A+A=2A$ and its determinant is $A^{2}-B^{2}=q_1q_2$; the real matrix has trace $a+a+a+a=4a$, which is $\operatorname{tr}\varphi(T)+\overline{\operatorname{tr}\varphi(T)}$ read in real coordinates, and determinant $\det(\tilde A-\tilde B)\det(\tilde A+\tilde B)=\lvert A-B\rvert^{2}\lvert A+B\rvert^{2}=\lvert q_2\rvert^{2}\lvert q_1\rvert^{2}$, by *The Four-Vector Element Representation of the Reduced Biquaternions*, §*Multiplication in Four-Vector Form*.

**Corollary (the criterion in the model).** $T$ is a **unit** exactly when $\varphi(T)$ is invertible, that is $q_1\neq0$ and $q_2\neq0$; $T$ is a **zero divisor** exactly when $\varphi(T)\neq0$ is singular, that is exactly one of $q_1,q_2$ is $0$; and $T$ is **nilpotent** exactly when $\varphi(T)$ is nilpotent, that is $q_1=q_2=0$, hence $T=0$. The multiplication is **not a division algebra**, and the singular non-zero matrices are the images of the zero divisors.

*Proof.* Invertibility of $\varphi(T)$ is $\langle T\rangle_{\natural}=q_1q_2\neq0$, the criterion of *Norm and Invertibility in the General Plain Algebra of the Reduced Biquaternions*; a diagonal model makes the three cases immediate, and the image of a diagonal matrix is nilpotent only if both entries vanish. The absence of division is the corollary of *The Four Products, Their Forms and Their Algebraic Norms*.

## The Diagonal Model and the Change of Basis

**The change to the idempotent basis diagonalises every matrix of the image, and the change of basis is the matrix of the two idempotents.**

**Theorem (the diagonalisation).** With the change-of-basis matrix
$$
P=\begin{pmatrix}1&1\\ 1&-1\end{pmatrix},\qquad \det P=-2,
$$
which sends the basis $1,j$ to the basis $1+j,\,1-j$, one has
$$
P^{-1}\varphi(T)P=\operatorname{diag}(q_1,q_2),
$$
the diagonal matrix of the two idempotent coordinates.

*Proof.* $\varphi(T)P=\begin{smallmatrix}A&B\\ B&A\end{smallmatrix}\begin{smallmatrix}1&1\\ 1&-1\end{smallmatrix}=\begin{smallmatrix}A+B&A-B\\ B+A&B-A\end{smallmatrix}=\begin{smallmatrix}q_1&q_2\\ q_1&-q_2\end{smallmatrix}$, and $P^{-1}=\tfrac12\begin{smallmatrix}1&1\\ 1&-1\end{smallmatrix}$ multiplies this to $\operatorname{diag}(q_1,q_2)$, the two columns $1+j$ and $1-j$ being the unnormalised idempotents $2\Pi_{1}$ and $2\Pi_{2}$.

**Corollary (the two changes of basis).** The complex change has determinant $-2$ and the induced real change of the quadruple has determinant $4=\lvert-2\rvert^{2}$, which is the inverse of the $\tfrac14$ of *Decompositions Along the Remarkable Subspaces*; the two are the same change read over $\mathbb{C}$ and over $\mathbb{R}$.

*Proof.* The determinant of the realification of $P$ is $\lvert\det P\rvert^{2}$, by the multiplicativity of the determinant under realification; and *Decompositions Along the Remarkable Subspaces* writes the passage the other way, from the idempotent coordinates to the real quadruple, with determinant $\tfrac14$, the inverse.

**Corollary (the diagonal model).** In the image of $\varphi$ every element is diagonalisable, and the image is the algebra of diagonal matrices in the idempotent basis; the diagonal model and the structure read there are *The General Plain Algebra in the $2\times2$ Matrix Element Representation of the Reduced Biquaternions*.

*Proof.* Every matrix of the image is conjugate to a diagonal one by the same matrix $P$, which is the simultaneous diagonalisation of the commutative algebra.

## The Singular Elements and the Ideals

**The singular matrices are the zero divisors, and the ideals are the coordinate lines of the diagonal model.**

**Theorem (the singular elements).** A matrix of the image is singular exactly when one of the two entries $q_1,q_2$ of its diagonal form vanishes; the singular non-zero matrices are the images of the two idempotent lines, and their rank is one.

*Proof.* The determinant is $q_1q_2$; the rank of $\operatorname{diag}(q_1,q_2)$ is the number of non-zero entries; a singular non-zero diagonal matrix has rank one, and its preimage is an element with exactly one of $q_1,q_2$ zero, which is a zero divisor of *Zero Divisors of the General Plain Algebra of the Reduced Biquaternions*.

**Corollary (the ideals as lines).** The minimal ideals $\mathbb{C}\Pi_{1}$ and $\mathbb{C}\Pi_{2}$ are the two coordinate lines of the diagonal model, the matrices with a single non-zero entry $q_1$ or $q_2$; every element of the first line annihilates every element of the second, the product of the two coordinate lines being the zero matrix.

*Proof.* The images of $\Pi_{1}$ and $\Pi_{2}$ are $\operatorname{diag}(1,0)$ and $\operatorname{diag}(0,1)$, and their product is $\operatorname{diag}(0,0)$, which is the annihilation of *Ideals and Peirce Decomposition of the General Plain Algebra of the Reduced Biquaternions*.

## The Groups in the Model

**The unit group is the group of invertible matrices of the image, and it is not the whole general linear group.**

**Theorem (the group of units).** The image of the unit group is
$$
\varphi(\mathbb{B}_{\mathrm{r}}^{\times})=\left\{\begin{pmatrix}A&B\\ B&A\end{pmatrix}:A\neq\pm B\right\},
$$
the invertible matrices of the image, conjugate to the invertible diagonal matrices $\operatorname{diag}(q_1,q_2)$ with $q_1,q_2\neq0$; it is not the whole of $GL_{2}(\mathbb{C})$, which is larger.

*Proof.* The invertibility is $A\neq\pm B$, that is $q_1\neq0$ and $q_2\neq0$; conjugation by $P$ identifies the set with the invertible diagonal matrices; and $GL_{2}(\mathbb{C})$ contains matrices that are not of the form, so the inclusion is proper.

## What the Matrix Form Makes Visible

**The matrix form makes the determinant and the trace visible as the norm and the scalar coordinate, and the commutativity visible as symmetry.**

The determinant of the matrix is the reduced norm $\langle\cdot\rangle_{\natural}$, and the multiplicativity of $\langle\cdot\rangle_{\natural}$ is the multiplicativity of the determinant; the trace is twice the scalar complex coordinate $A$; the symmetry of the matrix is the commutativity of the algebra; the simultaneous diagonalisability is the semisimplicity; the rank-one singular matrices are the zero divisors; and the image being the commutant of $\sigma_{1}$ — the matrices commuting with $\begin{smallmatrix}0&1\\ 1&0\end{smallmatrix}$ — is the statement that the algebra is the centraliser of its own generator $j$. None of these readings requires a metric, and the metrical reading of the determinant and of the norm is *Topology and Metric for Each of the Operations*.

## Summary

The reduced biquaternion $T=A+Bj$ is the matrix $\begin{smallmatrix}A&B\\ B&A\end{smallmatrix}$ of its own multiplication on the complex basis $1,j$, and the real $4\times4$ matrix $\begin{smallmatrix}\tilde A&\tilde B\\ \tilde B&\tilde A\end{smallmatrix}$ on the real basis $1,i,j,ij$. The images of the basis are $\mathrm I_{2}$, $i\mathrm I_{2}$, $\sigma_{1}$, $i\sigma_{1}$, and the shape is forced by $\varphi(j)^{2}=\mathrm I_{2}$ and the centrality of $i$. The trace is $2A$ and the determinant $\langle T\rangle_{\natural}=q_1q_2$ in the complex model, $4a$ and $\lvert \langle T\rangle_{\natural}\rvert^{2}$ in the real one. The change of basis $P=\begin{smallmatrix}1&1\\ 1&-1\end{smallmatrix}$ of determinant $-2$ diagonalises every matrix of the image to $\operatorname{diag}(q_1,q_2)$; the induced real change has determinant $4$, the inverse of the $\tfrac14$ of *Decompositions Along the Remarkable Subspaces*. The element is a **unit** exactly when $q_1\neq0$ and $q_2\neq0$, a **zero divisor** exactly when exactly one of them vanishes, and the multiplication is **not a division algebra**. The image is a commutative two-dimensional subalgebra of $M_{2}(\mathbb{C})$ and not the whole matrix algebra, which is the difference from the biquaternion companion.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\varphi(T)$ | the $2\times2$ complex matrix $\begin{smallmatrix}A&B\\ B&A\end{smallmatrix}$ of the multiplication by $T$ |
| $L_{T}$ | the real $4\times4$ matrix $\begin{smallmatrix}\tilde A&\tilde B\\ \tilde B&\tilde A\end{smallmatrix}$ of the multiplication |
| $\sigma_{1}$ | $\begin{smallmatrix}0&1\\ 1&0\end{smallmatrix}$, the image of $j$ in the basis $1,j$ |
| $P=\begin{smallmatrix}1&1\\ 1&-1\end{smallmatrix}$ | the change of basis to the idempotent basis, of determinant $-2$ |
| $\langle T\rangle_{\natural}=q_1q_2$ | the determinant of $\varphi(T)$, the reduced norm |

## Further Reading

- *Introduction to Reduced Biquaternion Element Representations* (`articles_maths/introduction-to-reduced-biquaternion-element-representations.md`), for the regular representation.
- *The Four-Vector Element Representation of the Reduced Biquaternions* (`articles_maths/the-four-vector-element-representation-of-the-reduced-biquaternions.md`), for the real quadruple and the real matrix.
- *The General Plain Algebra in the $2\times2$ Matrix Element Representation of the Reduced Biquaternions* (`articles_maths/the-general-plain-algebra-in-the-2x2-matrix-element-representation-of-the-reduced-biquaternions.md`), for the diagonal model of the algebra.
- *Norm and Invertibility in the General Plain Algebra of the Reduced Biquaternions* (`articles_maths/norm-and-invertibility-in-the-general-plain-algebra-of-the-reduced-biquaternions.md`), for the invertibility criterion.
- *Decompositions Along the Remarkable Subspaces* (`articles_maths/decompositions-along-the-remarkable-subspaces-of-the-reduced-biquaternions.md`), for the real change of basis of determinant $\tfrac14$.
- *Introduction to the $2\times2$ Matrix Element Representation $M_{2}(\mathbb{C})$ of Biquaternions* (`articles_maths/introduction-to-the-2x2-matrix-element-representation-of-biquaternions.md`), for the companion whose image is the whole matrix algebra.
