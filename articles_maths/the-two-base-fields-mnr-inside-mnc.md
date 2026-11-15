# __The Two Base Fields: $M_n(\mathbb{R})$ inside $M_n(\mathbb{C})$__

## Introduction

**One antilinear involution of the complex matrix algebra cuts out the real matrices, and every real count in the category is read from that one involution.** The inclusion $M_n(\mathbb{R})\subset M_n(\mathbb{C})$ is not a second algebra beside the complex one; it is the fixed set of conjugation, and the complex algebra is its complexification.

The article states the inclusion, proves that the complexification costs nothing (the real dimension doubles, while the degree, the rank and the determinant do not move), separates the two real structures that $M_n(\mathbb{C})$ carries, and records what transfers from the real field to the complex one and what fails to transfer. It assumes *The Matrix Algebra $M_n(\mathbb{C})$* for the algebra, the trace, the determinant and the centre. It defers the spectral questions to *The Spectrum of a Matrix*, the counting of the singular set to *The Topology of $M_n(\mathbb{C})$*, and the quaternionic reading of the second real structure to *Coda: $n=2$ and the Biquaternion Algebra*.

## The Inclusion

**The real matrices form a real subalgebra of the complex ones, and they are not a complex subalgebra.** The set $M_n(\mathbb{R})$ is closed under addition and under the product, and it contains $I$. Multiplication by $i$ carries a real matrix to a real matrix only when the matrix is zero. So $M_n(\mathbb{R})$ is a **real form**: a real subspace of dimension $n^{2}$ which spans $M_n(\mathbb{C})$ over $\mathbb{C}$ but is not a complex subspace.

**The complex algebra is the complexification of the real one.** The map $A\otimes z\mapsto zA$ is an isomorphism

$$
M_n(\mathbb{R})\otimes_{\mathbb{R}}\mathbb{C}\longrightarrow M_n(\mathbb{C}),
$$

surjective because $A=\mathrm{Re}\,A\otimes1+\mathrm{Im}\,A\otimes i$, and injective on dimensions: $2n^{2}$ on each side. The counts are

| $n$ | $\dim_{\mathbb{R}}M_n(\mathbb{R})$ | $\dim_{\mathbb{C}}M_n(\mathbb{C})$ | $\dim_{\mathbb{R}}M_n(\mathbb{C})$ |
|---|---|---|---|
| $2$ | $4$ | $4$ | $8$ |
| $3$ | $9$ | $9$ | $18$ |
| $4$ | $16$ | $16$ | $32$ |
| $5$ | $25$ | $25$ | $50$ |
| $6$ | $36$ | $36$ | $72$ |

The first two columns agree at every $n$: the complex algebra has as many complex parameters as the real algebra has real ones.

## Conjugation as an Antilinear Involution

**Conjugation is additive, involutive, multiplicative, and conjugate-linear.** For all $A,B$ and all $z\in\mathbb{C}$,

$$
\sigma(A+B)=\sigma(A)+\sigma(B),\qquad \sigma(\sigma(A))=A,\qquad \sigma(AB)=\sigma(A)\sigma(B),\qquad \sigma(zA)=\bar z\,\sigma(A),
$$

with $\sigma(A)=\bar A$. The multiplicative rule is the entry rule $(\overline{AB})_{ij}=\sum_{k}\bar A_{ik}\bar B_{kj}$. The last rule makes $\sigma$ **antilinear**: it is real-homogeneous but not complex-homogeneous, and $\sigma(iA)=-i\sigma(A)$.

**The fixed set is exactly the real matrices, and an antilinear involution of an algebra is called a real structure.** The name is warranted twice: the fixed set of a real structure is a real form, and every real form of $M_n(\mathbb{C})$ arises from exactly one real structure. The second statement is proved in §*The Two Real Structures*.

**Conjugation is not inner.** If $\sigma(A)=SAS^{-1}$ for a fixed $S$ and every $A$, then $\sigma$ would be complex-linear; but $\sigma(iI)=-iI$ while $S(iI)S^{-1}=iI$. So the real structure is semilinear and not a conjugation by a matrix. This is the sharp difference from the involutions of the following articles, which are complex-linear.

**Conjugation commutes with the trace, the determinant and the transpose.** Since $\operatorname{tr}\bar A=\overline{\operatorname{tr}A}$ and $\det\bar A=\overline{\det A}$, the two polynomial invariants of a real matrix are real.

## The Real and the Imaginary Parts

**Every matrix is a real matrix plus $i$ times a real matrix, uniquely.** Put

$$
\mathrm{Re}\,A=\tfrac12(A+\bar A),\qquad \mathrm{Im}\,A=\frac{A-\bar A}{2i}.
$$

Both are real and $A=\mathrm{Re}\,A+i\,\mathrm{Im}\,A$. This is the eigenspace decomposition of $\sigma$: the fixed set for $+1$ and the set $\{A:\sigma(A)=-A\}=iM_n(\mathbb{R})$ for $-1$. The sum is direct, since a matrix that is both real and purely imaginary is zero, and the dimensions add: $n^{2}+n^{2}=2n^{2}$.

**The summands are orthogonal for the real part of the trace form, and only for the real part.** With $\langle A,B\rangle=\operatorname{tr}(A^{*}B)$ and $X,Y$ real,

$$
\operatorname{tr}(X^{\mathsf T}Y)=\sum_{i,j}X_{ij}Y_{ij}\in\mathbb{R},\qquad \operatorname{Re}\operatorname{tr}\big(X^{\mathsf T}(iY)\big)=0 .
$$

The Hermitian form itself does not vanish there: $\langle X,iY\rangle=i\operatorname{tr}(X^{\mathsf T}Y)$ is purely imaginary and generally nonzero. So orthogonality of the two summands is a statement about the real part, and asserting it of the Hermitian form is an error.

## The Rank over the Two Fields

**The rank of a real matrix is the same number over $\mathbb{R}$ and over $\mathbb{C}$.** The rank is the largest $r$ with a nonzero $r\times r$ minor. The minors of a real matrix are real numbers computed from its entries, and a real number is nonzero over $\mathbb{R}$ exactly when it is nonzero over $\mathbb{C}$. Hence

$$
\operatorname{rank}_{\mathbb{R}}A=\operatorname{rank}_{\mathbb{C}}A\qquad\text{for }A\in M_n(\mathbb{R}).
$$

**Invertibility is the same condition over the two fields.** If $A$ is real and $\det A\ne0$, then $A^{-1}=(\operatorname{adj}A)/\det A$ and the adjugate of a real matrix is real. So $GL_n(\mathbb{R})=GL_n(\mathbb{C})\cap M_n(\mathbb{R})$, and Gaussian elimination on a real matrix runs with real pivots throughout, each pivot being a ratio of real minors.

**The singular set meets the real algebra in a real hypersurface.** The set $\Sigma=\{\det A=0\}$ is a complex hypersurface of dimension $n^{2}-1$. Its intersection with $M_n(\mathbb{R})$ is the zero set of the real polynomial $\det$, of real dimension $n^{2}-1$, and it separates the real algebra into the two components of $GL_n(\mathbb{R})$. The complex group has no such separation; see *The Topology of $M_n(\mathbb{C})$*.

## The Determinant and the Characteristic Polynomial

**Both are real, and the characteristic polynomial has real coefficients.** The determinant is a polynomial with integer coefficients in the entries, so it is real on real matrices. The characteristic polynomial

$$
\chi_A(t)=\det(tI-A)=t^{n}-(\operatorname{tr}A)t^{n-1}+\cdots+(-1)^{n}\det A
$$

therefore has real coefficients for real $A$, its coefficients being the elementary symmetric functions of the eigenvalues.

**The spectrum is stable under conjugation.** If $Av=\lambda v$ with $A$ real, then $A\bar v=\bar\lambda\bar v$. So the conjugates of the eigenvalues are eigenvalues with the same algebraic multiplicity. The non-real eigenvalues come in pairs $\lambda,\bar\lambda$, and the number of real eigenvalues, counted with multiplicity, has the parity of $n$: a real $2\times2$ matrix has two real eigenvalues or none, a real $3\times3$ matrix one or three.

**The sign of the determinant is the real invariant.** For real $A$,

$$
\operatorname{tr}A\in\mathbb{R},\qquad \det A\in\mathbb{R},\qquad \det A=\prod_{k}\lambda_k ,
$$

and each conjugate pair contributes the positive number $|\lambda|^{2}$. So the sign of the determinant is the sign of the product of the real eigenvalues, and it labels the two components of $GL_n(\mathbb{R})$. The count of the components is in *The Topology of $M_n(\mathbb{C})$*, the spectral statements in *The Spectrum of a Matrix*.

## The Two Real Structures

**A real structure is a $\mathbb{C}$-antilinear algebra automorphism of order two, and $M_n(\mathbb{C})$ carries exactly two up to conjugacy.** The first is conjugation $\sigma_1(A)=\bar A$, with fixed algebra $M_n(\mathbb{R})$. The second exists for even $n$: let $J$ be the block-diagonal matrix of $\tfrac{n}{2}$ copies of $\begin{pmatrix}0&1\\-1&0\end{pmatrix}$ and put

$$
\sigma_2(A)=J\bar A J^{-1}.
$$

Then $\sigma_2$ is antilinear, multiplicative and of order two, because $J$ is real. Its fixed algebra is the set of $A$ with $\bar A=J^{-1}AJ$, of real dimension $n^{2}$; at $n=2$ it is a copy of $\mathbb{H}$.

**Every real structure is of one of these two shapes.** Let $\sigma$ be a real structure. There is an invertible $S$ with $\sigma(A)=S\bar AS^{-1}$, and $\sigma^{2}=\mathrm{id}$ reads $S\bar S=cI$ with $c\in\mathbb{R}^{\times}$; rescaling $S$ normalises $c$ to $\pm1$. If $c=1$, then $S$ is symmetric after a real change of basis and the fixed algebra is conjugate to $M_n(\mathbb{R})$. If $c=-1$, then $n$ is even, $S$ is skew after a change of basis, and the fixed algebra is conjugate to $M_{n/2}(\mathbb{H})$.

**The fixed algebras have the same real dimension and are not isomorphic.** Both have dimension $n^{2}$, since $4\cdot(n/2)^{2}=n^{2}$. They differ in type. At $n=2$ the fixed algebra of $\sigma_2$ is $\mathbb{H}$, where every nonzero element is invertible, while $M_2(\mathbb{R})$ contains the nonzero zero divisors $E_{11}$ and $E_{22}$ with $E_{11}E_{22}=0$. So $\mathbb{H}\not\cong M_2(\mathbb{R})$ and the two structures are not conjugate.

**The two structures differ by an inner automorphism.** Since $J$ is real,

$$
\sigma_1\sigma_2(A)=\overline{J\bar AJ^{-1}}=JAJ^{-1},
$$

which is conjugation by $J$. The real structures therefore form two classes joined by the inner automorphisms, and the second class exists only for even $n$.

**A real structure is not an involution of the split.** The involutions studied in *The Involutions over $\mathbb{R}$ and over $\mathbb{C}$* are complex-linear with eigenvalues $\pm1$, and their fixed sets are complex subspaces. A real structure is antilinear and its fixed set is a real form. Both split the algebra in two, and the halves are of different kinds: one pair is complex, the other real.

## The Case $n=2$: the Split Quaternions

**At $n=2$ the real algebra is the split quaternion algebra.** Let

$$
i=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad j=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad k=ij=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
$$

Then $i^{2}=-I$, $j^{2}=I$, $k^{2}=I$ and $ij=-ji=k$. The four matrices $I,i,j,k$ are a real basis of $M_2(\mathbb{R})$, and the algebra they span is the split quaternion algebra $\mathbb{H}_s$.

**The two real structures at $n=2$ give the two quaternion algebras.** With $J=i$, the fixed set of $\sigma_2(A)=i\bar Ai^{-1}$ is spanned by $I$ and the three matrices $i\sigma_1,i\sigma_2,i\sigma_3$ of the Pauli list, which multiply with all three squares equal to $-I$. So the two real forms of $M_2(\mathbb{C})$ are

$$
\mathbb{H}_s\cong M_2(\mathbb{R}),\qquad \mathbb{H},
$$

of real dimension $4$ each. The first is split, the second is a division algebra, and the complex algebra $M_2(\mathbb{C})=\mathbb{B}$ contains both.

**The split form has idempotents and the division form does not.** In $\mathbb{H}_s$ the element $j$ satisfies $(j-I)(j+I)=j^{2}-I=0$ with both factors nonzero, so $\tfrac12(I\pm j)$ are the two Peirce idempotents of the split algebra. In $\mathbb{H}$ every nonzero element is invertible, so there is no idempotent other than $0$ and $I$. The biquaternion articles read the split case through those two idempotents; see *The Peirce Decomposition of the Biquaternion Algebra*.

## Summary

The real matrices are the fixed set of the antilinear involution $\sigma(A)=\bar A$, and $M_n(\mathbb{C})=M_n(\mathbb{R})\otimes_{\mathbb{R}}\mathbb{C}$ is its complexification. The real dimension is $n^{2}$ against $2n^{2}$, while the rank, the degree $n$, the determinant and the characteristic polynomial do not change: a real matrix has the same rank over both fields, its inverse is real when it exists, and its spectrum is stable under conjugation with the non-real eigenvalues in pairs. The summands $M_n(\mathbb{R})$ and $iM_n(\mathbb{R})$ are orthogonal for the real part of the trace form and not for the Hermitian form. Up to conjugacy there are two real structures, with fixed algebras $M_n(\mathbb{R})$ and $M_{n/2}(\mathbb{H})$, of the same real dimension and of different type. At $n=2$ they are the split quaternions and the quaternions inside the biquaternion algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M_n(\mathbb{R})$ | the real matrices, a real form of dimension $n^{2}$ |
| $\sigma(A)=\bar A$ | entrywise conjugation, the first real structure |
| $\mathrm{Re}\,A$, $\mathrm{Im}\,A$ | the real and the imaginary part of $A$ |
| $iM_n(\mathbb{R})$ | the set $\{A:\sigma(A)=-A\}$, of dimension $n^{2}$ |
| $J$ | the block-diagonal symplectic matrix, $\tfrac{n}{2}$ blocks |
| $\sigma_2(A)=J\bar AJ^{-1}$ | the second real structure, fixed algebra $M_{n/2}(\mathbb{H})$ |
| $\chi_A(t)=\det(tI-A)$ | the characteristic polynomial, real for real $A$ |
| $\mathbb{H}_s\cong M_2(\mathbb{R})$ | the split quaternions |
| $\mathbb{H}$ | the quaternions, the other real form at $n=2$ |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for real forms, real structures and the two classes of antilinear involutions.
- Tsit-Yuen Lam, *A First Course in Noncommutative Rings* (Springer, 2001), for the quaternion algebras, their zero divisors and the split case.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the rank over a subfield, the adjugate and the reality of the polynomial.
- [The Matrix Algebra $M_n(\mathbb{C})$](the-matrix-algebra-mnc.html), for the algebra, the trace form and the real dimension.
- [Roots of Unity and the Lagrange Idempotents of $M_n(\mathbb{C})$](roots-of-unity-and-the-lagrange-idempotents-of-mnc.html), for the complex construction that the real field does not support.
- [The Peirce Decomposition of the Biquaternion Algebra](the-peirce-decomposition-of-the-biquaternion-algebra.html), for the idempotents of the split case at $n=2$.
