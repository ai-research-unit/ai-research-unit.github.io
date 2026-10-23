# __Introduction to the $2\times2$ Matrix Element Representation of Reduced Biquaternions__

## Introduction

The **$2\times2$ matrix element representation** writes the reduced biquaternion as the matrix of its own multiplication. The regular representation sends $\breve Q$ to the operator $L_{\breve Q}:\breve Q_{2}\mapsto \breve Q \breve Q_{2}$ on the complex two-dimensional space of the algebra, and that operator is a $2\times2$ matrix with **complex** entries; on the real four-dimensional space the same operator is a $4\times4$ matrix with **real** entries. This article writes the two models, explains why the signs of the entries are forced by $j^{2}=+1$, records the trace, the determinant and the norm, and shows how the change to the idempotent basis diagonalises the matrix. The multiplication is **commutative**, so the matrix is symmetric, and it **has zero divisors**, so the matrix may be singular at a non-zero element. The diagonal model of the algebra itself — the isomorphism onto the diagonal matrices and the structure read there — is *The Algebra in the $2\times2$ Matrix Element Representation of the Reduced Biquaternions*; this article is about the element as a matrix, not about the structure.

## The Regular Representation as a Matrix

**The regular representation sends the element to the matrix with the two columns $Q_{\blacktriangle},Q_{\blacktriangledown}$ and $Q_{\blacktriangledown},Q_{\blacktriangle}$.**

### The Map on the Basis

**Definition.** The **matrix element representation** is
$$
\varphi(\breve Q)=\begin{pmatrix}Q_{\blacktriangle}&Q_{\blacktriangledown}\\ Q_{\blacktriangledown}&Q_{\blacktriangle}\end{pmatrix},
$$
the matrix of the left multiplication $\breve Q_{2}\mapsto \breve Q \breve Q_{2}$ on the complex basis $1,j$ of $\mathbb{B}_{\mathrm{r}}$.

**Proposition (the images of the basis).** On the real basis,
$$
\varphi(1)=\begin{pmatrix}1&0\\ 0&1\end{pmatrix}=\mathrm I_{2},\qquad
\varphi(i)=\begin{pmatrix}i&0\\ 0&i\end{pmatrix}=i\,\mathrm I_{2},\qquad
\varphi(j)=\begin{pmatrix}0&1\\ 1&0\end{pmatrix}=\sigma_{1},\qquad
\varphi(ij)=i\,\sigma_{1}.
$$

*Proof.* $L_{1}=\operatorname{id}$ and $L_{i}$ is multiplication by the central complex unit $i$ on both coordinates, hence $i\mathrm I_{2}$; $L_{j}(1)=j$ and $L_{j}(j)=j^{2}=1$, giving the columns $\binom{0}{1}$ and $\binom{1}{0}$, that is $\sigma_{1}$; and $L_{ij}=L_{i}L_{j}=i\sigma_{1}$.

### The Matrix of an Element

**Theorem (the matrix).** The map $\varphi$ is an injective homomorphism of $\mathbb{C}$-algebras, $\varphi(\breve Q_{1}\breve Q_{2})=\varphi(\breve Q_{1})\varphi(\breve Q_{2})$ and $\varphi(1)=\mathrm I_{2}$, with the block form
$$
\boxed{\;
\varphi(\breve Q)=\begin{pmatrix}Q_{\blacktriangle}&Q_{\blacktriangledown}\\ Q_{\blacktriangledown}&Q_{\blacktriangle}\end{pmatrix}=\begin{pmatrix}q_{\blacktriangle}&-q'_{\blacktriangle}\\ q'_{\blacktriangle}&q_{\blacktriangle}\end{pmatrix}+j\begin{pmatrix}q_{\blacktriangledown}&-q'_{\blacktriangledown}\\ q'_{\blacktriangledown}&q_{\blacktriangledown}\end{pmatrix}
\;}
$$
over the real basis, using $i=\begin{smallmatrix}0&-1\\ 1&0\end{smallmatrix}$.

*Proof.* The product rule is read from $\breve Q_{1}\breve Q_{2}=(Q_{1\blacktriangle}Q_{2\blacktriangle}+Q_{1\blacktriangledown}Q_{2\blacktriangledown})+(Q_{1\blacktriangle}Q_{2\blacktriangledown}+Q_{1\blacktriangledown}Q_{2\blacktriangle})j$: the matrix product $\begin{smallmatrix}Q_{1\blacktriangle}&Q_{1\blacktriangledown}\\ Q_{1\blacktriangledown}&Q_{1\blacktriangle}\end{smallmatrix}\begin{smallmatrix}Q_{2\blacktriangle}&Q_{2\blacktriangledown}\\ Q_{2\blacktriangledown}&Q_{2\blacktriangle}\end{smallmatrix}=\begin{smallmatrix}Q_{1\blacktriangle}Q_{2\blacktriangle}+Q_{1\blacktriangledown}Q_{2\blacktriangledown}&Q_{1\blacktriangle}Q_{2\blacktriangledown}+Q_{1\blacktriangledown}Q_{2\blacktriangle}\\ Q_{1\blacktriangledown}Q_{2\blacktriangle}+Q_{1\blacktriangle}Q_{2\blacktriangledown}&Q_{1\blacktriangledown}Q_{2\blacktriangledown}+Q_{1\blacktriangle}Q_{2\blacktriangle}\end{smallmatrix}$ has the two diagonal entries $Q_{1\blacktriangle}Q_{2\blacktriangle}+Q_{1\blacktriangledown}Q_{2\blacktriangledown}$ and the two off-diagonal entries $Q_{1\blacktriangle}Q_{2\blacktriangledown}+Q_{1\blacktriangledown}Q_{2\blacktriangle}$, which is $\varphi(\breve Q_{1}\breve Q_{2})$. The injectivity is $\varphi(\breve Q)=0\Rightarrow Q_{\blacktriangle}=Q_{\blacktriangledown}=0\Rightarrow \breve Q=0$. The real display is $\varphi(i)=i\mathrm I_{2}$ and $\varphi(j)=\sigma_{1}$ written in the real $2\times2$ basis.

**Corollary (the image is not the whole matrix algebra).** The image $\varphi(\mathbb{B}_{\mathrm{r}})$ is a commutative two-dimensional subalgebra of $M_{2}(\mathbb{C})$ — the matrices of the form $\begin{smallmatrix}Q_{\blacktriangle}&Q_{\blacktriangledown}\\ Q_{\blacktriangledown}&Q_{\blacktriangle}\end{smallmatrix}$ — and not the whole of $M_{2}(\mathbb{C})$, which has complex dimension four. The biquaternion companion is realised as the whole of $M_{2}(\mathbb{C})$; here the commutativity forces the two diagonal entries to be equal and the two off-diagonal entries to be equal, halving the linear dimension.

*Proof.* The displayed form shows that the image is spanned over $\mathbb{C}$ by $\mathrm I_{2}$ and $\sigma_{1}$, of complex dimension two; the matrix $\operatorname{diag}(1,0)$ is not of the form and so is not in the image.

## Why the Signs Are Forced

**The images must satisfy $\varphi(i)^{2}=-\mathrm I_{2}$, $\varphi(j)^{2}=+\mathrm I_{2}$ and $\varphi(i)\varphi(j)=\varphi(j)\varphi(i)$, and these force the shape.**

**Theorem (the shape is forced).** Let $\varphi$ be an injective homomorphism of $\mathbb{C}$-algebras with $\varphi(i)=i\mathrm I_{2}$. Then $\varphi(j)^{2}=\mathrm I_{2}$, so $\varphi(j)$ is an involution; if in addition $\varphi(j)$ has trace $0$ and is symmetric, then $\varphi(j)=\varepsilon\,\sigma_{1}$ with $\varepsilon=\pm1$ in the basis $1,j$, and the image of $\breve Q$ is $\begin{smallmatrix}Q_{\blacktriangle}&\varepsilon Q_{\blacktriangledown}\\ \varepsilon Q_{\blacktriangledown}&Q_{\blacktriangle}\end{smallmatrix}$, which the normalisation $\varepsilon=+1$ reduces to the matrix of §*The Regular Representation*.

*Proof.* From $\varphi(i)^{2}=\varphi(i^{2})=\varphi(-1)=-\mathrm I_{2}$ the image of $i$ is $i\mathrm I_{2}$ up to conjugation in the centre, which is scalar; from $\varphi(j)^{2}=\varphi(j^{2})=\varphi(1)=\mathrm I_{2}$ the image of $j$ is an involution. A traceless symmetric involution of $\mathbb{C}^{2}$ has $\sigma_{1}$ as its normal form, because its eigenvalues are $+1,-1$ with orthogonal eigendirections; and $ij=ji$ forces $\varphi(j)$ to commute with $\varphi(i)=i\mathrm I_{2}$, which is automatic. Reading $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ through $\varphi$ with $\varphi(j)=\sigma_{1}$ gives $\begin{smallmatrix}Q_{\blacktriangle}&Q_{\blacktriangledown}\\ Q_{\blacktriangledown}&Q_{\blacktriangle}\end{smallmatrix}$.

**Remark (the other normal form).** The same element is sent to the **diagonal** matrix $\operatorname{diag}(Q_{+},Q_{-})$ in the idempotent basis, where the image of $j$ is $\sigma_{3}=\operatorname{diag}(1,-1)$ instead of $\sigma_{1}$; the two normal forms are conjugate by the change of basis of §*The Diagonal Model*. The choice between $\sigma_{1}$ and $\sigma_{3}$ is the choice between writing the element and writing the algebra, and the algebra is the diagonal picture of *The Algebra in the $2\times2$ Matrix Element Representation of the Reduced Biquaternions*.

## The Real-Entry Model

**On the real four-dimensional space the same operator is a real $4\times4$ matrix with the repeated-block form.**

**Theorem (the real matrix).** For $\breve Q=q_{\blacktriangle}+iq'_{\blacktriangle}+q_{\blacktriangledown}j+iq'_{\blacktriangledown}j$, the left multiplication on the real basis $1,i,j,ij$ is
$$
L_{\breve Q}=\begin{pmatrix}
q_{\blacktriangle}&-q'_{\blacktriangle}&q_{\blacktriangledown}&-q'_{\blacktriangledown}\\
q'_{\blacktriangle}&q_{\blacktriangle}&q'_{\blacktriangledown}&q_{\blacktriangledown}\\
q_{\blacktriangledown}&-q'_{\blacktriangledown}&q_{\blacktriangle}&-q'_{\blacktriangle}\\
q'_{\blacktriangledown}&q_{\blacktriangledown}&q'_{\blacktriangle}&q_{\blacktriangle}
\end{pmatrix}
=\begin{pmatrix}A_+&A_-\\ A_-&A_+\end{pmatrix},
\qquad
A_+=\begin{pmatrix}q_{\blacktriangle}&-q'_{\blacktriangle}\\ q'_{\blacktriangle}&q_{\blacktriangle}\end{pmatrix},\quad
A_-=\begin{pmatrix}q_{\blacktriangledown}&-q'_{\blacktriangledown}\\ q'_{\blacktriangledown}&q_{\blacktriangledown}\end{pmatrix}.
$$

*Proof.* This is the real form of the complex matrix of §*The Matrix of an Element*, read by *The Four-Vector Element Representation of the Reduced Biquaternions*, §*Multiplication in Four-Vector Form*: each complex entry $Q_{\blacktriangle}$ becomes the real $2\times2$ block $A_+$ and each entry $Q_{\blacktriangledown}$ the block $A_-$, and the two $2\times2$ blocks of the complex matrix become the four blocks of the real one.

**Corollary (the two models agree).** The real matrix is the realification of the complex one: the complex $2\times2$ model and the real $4\times4$ model are the same operator on the same space read over the two base fields, and the real one carries the four real coordinates of *The Four-Vector Element Representation of the Reduced Biquaternions*.

*Proof.* The realification of a complex matrix replaces each entry by its real $2\times2$ block, which is exactly the passage from $\begin{smallmatrix}Q_{\blacktriangle}&Q_{\blacktriangledown}\\ Q_{\blacktriangledown}&Q_{\blacktriangle}\end{smallmatrix}$ to the displayed matrix.

## Trace, Determinant and the Norm

**The trace is twice the scalar complex coordinate, the determinant is the reduced norm, and the element is invertible exactly when the determinant does not vanish.**

**Theorem (the invariants).** For $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$,
$$
\boxed{\;
\operatorname{tr}\varphi(\breve Q)=2Q_{\blacktriangle},\qquad \det\varphi(\breve Q)=\langle \breve Q\rangle_{\mathrm{ts}}=Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}=Q_{+}Q_{-}
\;},
$$
and for the real matrix
$$
\operatorname{tr}L_{\breve Q}=4q_{\blacktriangle},\qquad \det L_{\breve Q}=\lvert \langle \breve Q\rangle_{\mathrm{ts}}\rvert^{2}=\lvert Q_{+}\rvert^{2}\lvert Q_{-}\rvert^{2}.
$$

*Proof.* The trace of $\begin{smallmatrix}Q_{\blacktriangle}&Q_{\blacktriangledown}\\ Q_{\blacktriangledown}&Q_{\blacktriangle}\end{smallmatrix}$ is $Q_{\blacktriangle}+Q_{\blacktriangle}=2Q_{\blacktriangle}$ and its determinant is $Q_{\blacktriangle}^{2}-Q_{\blacktriangledown}^{2}=Q_{+}Q_{-}$; the real matrix has trace $q_{\blacktriangle}+q_{\blacktriangle}+q_{\blacktriangle}+q_{\blacktriangle}=4q_{\blacktriangle}$, which is $\operatorname{tr}\varphi(\breve Q)+\overline{\operatorname{tr}\varphi(\breve Q)}$ read in real coordinates, and determinant $\det(A_+-A_-)\det(A_++A_-)=\lvert Q_{\blacktriangle}-Q_{\blacktriangledown}\rvert^{2}\lvert Q_{\blacktriangle}+Q_{\blacktriangledown}\rvert^{2}=\lvert Q_{-}\rvert^{2}\lvert Q_{+}\rvert^{2}$, by *The Four-Vector Element Representation of the Reduced Biquaternions*, §*Multiplication in Four-Vector Form*.

**Corollary (the criterion in the model).** $\breve Q$ is a **unit** exactly when $\varphi(\breve Q)$ is invertible, that is $Q_{+}\neq0$ and $Q_{-}\neq0$; $\breve Q$ is a **zero divisor** exactly when $\varphi(\breve Q)\neq0$ is singular, that is exactly one of $Q_{+},Q_{-}$ is $0$; and $\breve Q$ is **nilpotent** exactly when $\varphi(\breve Q)$ is nilpotent, that is $Q_{+}=Q_{-}=0$, hence $\breve Q=0$. The multiplication is **not a division algebra**, and the singular non-zero matrices are the images of the zero divisors.

*Proof.* Invertibility of $\varphi(\breve Q)$ is $\langle \breve Q\rangle_{\mathrm{ts}}=Q_{+}Q_{-}\neq0$, the criterion of *Norm and Invertibility in the Algebra of the Reduced Biquaternions*; a diagonal model makes the three cases immediate, and the image of a diagonal matrix is nilpotent only if both entries vanish. The absence of division is the corollary of *The Four Products, Their Forms and Their Algebraic Norms*.

## The Diagonal Model and the Change of Basis

**The change to the idempotent basis diagonalises every matrix of the image, and the change of basis is the matrix of the two idempotents.**

**Theorem (the diagonalisation).** With the change-of-basis matrix
$$
P=\begin{pmatrix}1&1\\ 1&-1\end{pmatrix},\qquad \det P=-2,
$$
which sends the basis $1,j$ to the basis $1+j,\,1-j$, one has
$$
\boxed{\;
P^{-1}\varphi(\breve Q)P=\operatorname{diag}(Q_{+},Q_{-})
\;},
$$
the diagonal matrix of the two idempotent coordinates.

*Proof.* $\varphi(\breve Q)P=\begin{smallmatrix}Q_{\blacktriangle}&Q_{\blacktriangledown}\\ Q_{\blacktriangledown}&Q_{\blacktriangle}\end{smallmatrix}\begin{smallmatrix}1&1\\ 1&-1\end{smallmatrix}=\begin{smallmatrix}Q_{\blacktriangle}+Q_{\blacktriangledown}&Q_{\blacktriangle}-Q_{\blacktriangledown}\\ Q_{\blacktriangledown}+Q_{\blacktriangle}&Q_{\blacktriangledown}-Q_{\blacktriangle}\end{smallmatrix}=\begin{smallmatrix}Q_{+}&Q_{-}\\ Q_{+}&-Q_{-}\end{smallmatrix}$, and $P^{-1}=\tfrac12\begin{smallmatrix}1&1\\ 1&-1\end{smallmatrix}$ multiplies this to $\operatorname{diag}(Q_{+},Q_{-})$, the two columns $1+j$ and $1-j$ being the unnormalised idempotents $2\Pi_+$ and $2\Pi_-$.

**Corollary (the two changes of basis).** The complex change has determinant $-2$ and the induced real change of the quadruple has determinant $4=\lvert-2\rvert^{2}$, which is the inverse of the $\tfrac14$ of *Decompositions Along the Remarkable Subspaces*; the two are the same change read over $\mathbb{C}$ and over $\mathbb{R}$.

*Proof.* The determinant of the realification of $P$ is $\lvert\det P\rvert^{2}$, by the multiplicativity of the determinant under realification; and *Decompositions Along the Remarkable Subspaces* writes the passage the other way, from the idempotent coordinates to the real quadruple, with determinant $\tfrac14$, the inverse.

**Corollary (the diagonal model).** In the image of $\varphi$ every element is diagonalisable, and the image is the algebra of diagonal matrices in the idempotent basis; the diagonal model and the structure read there are *The Algebra in the $2\times2$ Matrix Element Representation of the Reduced Biquaternions*.

*Proof.* Every matrix of the image is conjugate to a diagonal one by the same matrix $P$, which is the simultaneous diagonalisation of the commutative algebra.

## The Singular Elements and the Ideals

**The singular matrices are the zero divisors, and the ideals are the coordinate lines of the diagonal model.**

**Theorem (the singular elements).** A matrix of the image is singular exactly when one of the two entries $Q_{+},Q_{-}$ of its diagonal form vanishes; the singular non-zero matrices are the images of the two idempotent lines, and their rank is one.

*Proof.* The determinant is $Q_{+}Q_{-}$; the rank of $\operatorname{diag}(Q_{+},Q_{-})$ is the number of non-zero entries; a singular non-zero diagonal matrix has rank one, and its preimage is an element with exactly one of $Q_{+},Q_{-}$ zero, which is a zero divisor of *Zero Divisors of the Algebra of the Reduced Biquaternions*.

**Corollary (the ideals as lines).** The minimal ideals $\mathbb{C}\Pi_+$ and $\mathbb{C}\Pi_-$ are the two coordinate lines of the diagonal model, the matrices with a single non-zero entry $Q_{+}$ or $Q_{-}$; every element of the first line annihilates every element of the second, the product of the two coordinate lines being the zero matrix.

*Proof.* The images of $\Pi_+$ and $\Pi_-$ are $\operatorname{diag}(1,0)$ and $\operatorname{diag}(0,1)$, and their product is $\operatorname{diag}(0,0)$, which is the annihilation of *Ideals and Peirce Decomposition of the Algebra of the Reduced Biquaternions*.

## The Groups in the Model

**The unit group is the group of invertible matrices of the image, and it is not the whole general linear group.**

**Theorem (the group of units).** The image of the unit group is
$$
\varphi(\mathbb{B}_{\mathrm{r}}^{\times})=\left\{\begin{pmatrix}Q_{\blacktriangle}&Q_{\blacktriangledown}\\ Q_{\blacktriangledown}&Q_{\blacktriangle}\end{pmatrix}:Q_{\blacktriangle}\neq\pm Q_{\blacktriangledown}\right\},
$$
the invertible matrices of the image, conjugate to the invertible diagonal matrices $\operatorname{diag}(Q_{+},Q_{-})$ with $Q_{+},Q_{-}\neq0$; it is not the whole of $GL_{2}(\mathbb{C})$, which is larger.

*Proof.* The invertibility is $Q_{\blacktriangle}\neq\pm Q_{\blacktriangledown}$, that is $Q_{+}\neq0$ and $Q_{-}\neq0$; conjugation by $P$ identifies the set with the invertible diagonal matrices; and $GL_{2}(\mathbb{C})$ contains matrices that are not of the form, so the inclusion is proper.

## What the Matrix Form Makes Visible

**The matrix form makes the determinant and the trace visible as the norm and the scalar coordinate, and the commutativity visible as symmetry.**

The determinant of the matrix is the reduced norm $\langle\cdot\rangle_{\mathrm{ts}}$, and the multiplicativity of $\langle\cdot\rangle_{\mathrm{ts}}$ is the multiplicativity of the determinant; the trace is twice the scalar complex coordinate $Q_{\blacktriangle}$; the symmetry of the matrix is the commutativity of the algebra; the simultaneous diagonalisability is the semisimplicity; the rank-one singular matrices are the zero divisors; and the image being the commutant of $\sigma_{1}$ — the matrices commuting with $\begin{smallmatrix}0&1\\ 1&0\end{smallmatrix}$ — is the statement that the algebra is the centraliser of its own generator $j$. None of these readings requires a metric, and the metrical reading of the determinant and of the norm is *Topology and Metric for Each of the Operations*.

## Summary

The reduced biquaternion $\breve Q=Q_{\blacktriangle}+jQ_{\blacktriangledown}$ is the matrix $\begin{smallmatrix}Q_{\blacktriangle}&Q_{\blacktriangledown}\\ Q_{\blacktriangledown}&Q_{\blacktriangle}\end{smallmatrix}$ of its own multiplication on the complex basis $1,j$, and the real $4\times4$ matrix $\begin{smallmatrix}A_+&A_-\\ A_-&A_+\end{smallmatrix}$ on the real basis $1,i,j,ij$. The images of the basis are $\mathrm I_{2}$, $i\mathrm I_{2}$, $\sigma_{1}$, $i\sigma_{1}$, and the shape is forced by $\varphi(j)^{2}=\mathrm I_{2}$ and the centrality of $i$. The trace is $2Q_{\blacktriangle}$ and the determinant $\langle \breve Q\rangle_{\mathrm{ts}}=Q_{+}Q_{-}$ in the complex model, $4q_{\blacktriangle}$ and $\lvert \langle \breve Q\rangle_{\mathrm{ts}}\rvert^{2}$ in the real one. The change of basis $P=\begin{smallmatrix}1&1\\ 1&-1\end{smallmatrix}$ of determinant $-2$ diagonalises every matrix of the image to $\operatorname{diag}(Q_{+},Q_{-})$; the induced real change has determinant $4$, the inverse of the $\tfrac14$ of *Decompositions Along the Remarkable Subspaces*. The element is a **unit** exactly when $Q_{+}\neq0$ and $Q_{-}\neq0$, a **zero divisor** exactly when exactly one of them vanishes, and the multiplication is **not a division algebra**. The image is a commutative two-dimensional subalgebra of $M_{2}(\mathbb{C})$ and not the whole matrix algebra, which is the difference from the biquaternion companion.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\varphi(\breve Q)$ | the $2\times2$ complex matrix $\begin{smallmatrix}Q_{\blacktriangle}&Q_{\blacktriangledown}\\ Q_{\blacktriangledown}&Q_{\blacktriangle}\end{smallmatrix}$ of the multiplication by $\breve Q$ |
| $L_{\breve Q}$ | the real $4\times4$ matrix $\begin{smallmatrix}A_+&A_-\\ A_-&A_+\end{smallmatrix}$ of the multiplication |
| $\sigma_{1}$ | $\begin{smallmatrix}0&1\\ 1&0\end{smallmatrix}$, the image of $j$ in the basis $1,j$ |
| $P=\begin{smallmatrix}1&1\\ 1&-1\end{smallmatrix}$ | the change of basis to the idempotent basis, of determinant $-2$ |
| $\langle \breve Q\rangle_{\mathrm{ts}}=Q_{+}Q_{-}$ | the determinant of $\varphi(\breve Q)$, the reduced norm |

## Further Reading

- [Introduction to Reduced Biquaternion Element Representations](introduction-to-reduced-biquaternion-element-representations.html), for the regular representation.
- [The Four-Vector Element Representation of the Reduced Biquaternions](the-four-vector-element-representation-of-the-reduced-biquaternions.html), for the real quadruple and the real matrix.
- [The Algebra in the $2\times2$ Matrix Element Representation of the Reduced Biquaternions](the-general-plain-algebra-in-the-2x2-matrix-element-representation-of-the-reduced-biquaternions.html), for the diagonal model of the algebra.
- [Norm and Invertibility in the Algebra of the Reduced Biquaternions](norm-and-invertibility-in-the-general-plain-algebra-of-the-reduced-biquaternions.html), for the invertibility criterion.
- [Decompositions Along the Remarkable Subspaces](decompositions-along-the-remarkable-subspaces-of-the-reduced-biquaternions.html), for the real change of basis of determinant $\tfrac14$.
- [Introduction to the $2\times2$ Matrix Element Representation $M_{2}(\mathbb{C})$ of Biquaternions](introduction-to-the-2x2-matrix-element-representation-of-biquaternions.html), for the companion whose image is the whole matrix algebra.
