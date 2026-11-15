# __The Two Base Fields: $M_n(\mathbb{R})$ inside $M_n(\mathbb{C})$__

## Introduction

**One antilinear involution of the complex matrix algebra cuts out the real matrices, and every real count in the category is read from that one involution.** The inclusion $M_n(\mathbb{R})\subset M_n(\mathbb{C})$ is not a second algebra beside the complex one; it is the fixed set of conjugation, and the complex algebra is its complexification.

The article states the inclusion, proves that the complexification costs nothing (the real dimension doubles, while the degree, the rank and the determinant do not move), separates the two real structures that $M_n(\mathbb{C})$ carries, and records what transfers from the real field to the complex one and what fails to transfer. It assumes *The Matrix Algebra $M_n(\mathbb{C})$* for the algebra, the trace, the determinant and the centre. It defers the spectral questions to *The Spectrum of a Matrix*, the counting of the singular set to *The Topology of $M_n(\mathbb{C})$*, and the quaternionic reading of the second real structure to *Coda: $n=2$ and the Biquaternion Algebra*.

## The Inclusion

**The real matrices form a real subalgebra of the complex ones, and they are not a complex subalgebra.** The set $M_n(\mathbb{R})$ is closed under addition, under the matrix product, and it contains $I$. Multiplication by $i$ carries a real matrix to a real matrix only when the matrix is zero. So $M_n(\mathbb{R})$ is a **real form**: a real subspace of real dimension $n^{2}$ which spans $M_n(\mathbb{C})$ over $\mathbb{C}$ but is not itself a complex subspace.

**The complex algebra is the complexification of the real one.** The map

$$
M_n(\mathbb{R})\otimes_{\mathbb{R}}\mathbb{C}\longrightarrow M_n(\mathbb{C}),\qquad A\otimes z\longmapsto zA
$$

is an isomorphism of complex algebras. It is surjective because $A=\mathrm{Re}\,A\otimes1+\mathrm{Im}\,A\otimes i$, and it is injective on dimensions: the left side has real dimension $2n^{2}$ and so has the right side. The two dimensions are

| $n$ | $\dim_{\mathbb{R}}M_n(\mathbb{R})$ | $\dim_{\mathbb{C}}M_n(\mathbb{C})$ | $\dim_{\mathbb{R}}M_n(\mathbb{C})$ |
|---|---|---|---|
| $2$ | $4$ | $4$ | $8$ |
| $3$ | $9$ | $9$ | $18$ |
| $4$ | $16$ | $16$ | $32$ |
| $5$ | $25$ | $25$ | $50$ |
| $6$ | $36$ | $36$ | $72$ |

The middle and the left column agree at every $n$, and the right column is twice them. The equality of the first two columns is the statement that the complex algebra has the same number of complex parameters as the real algebra has real ones.

**The real matrices are the fixed set of conjugation, and that is the definition used below.** Write $\sigma(A)=\bar A$ for entrywise conjugation. Then $M_n(\mathbb{R})=\{A:\sigma(A)=A\}$, and the inclusion is a statement about $\sigma$, not about the entries.

## Conjugation as an Antilinear Involution

**Conjugation is additive, involutive, multiplicative, and conjugate-linear.** For all $A,B$ and all $z\in\mathbb{C}$,

$$
\sigma(A+B)=\sigma(A)+\sigma(B),\qquad \sigma(\sigma(A))=A,\qquad \sigma(AB)=\sigma(A)\sigma(B),\qquad \sigma(zA)=\bar z\,\sigma(A).
$$

The multiplicative rule is the rule for the entries of a product, $(\overline{AB})_{ij}=\sum_{k}\bar A_{ik}\bar B_{kj}$. The last rule is what makes $\sigma$ **antilinear**: it is additive and real-homogeneous but not complex-homogeneous, and $\sigma(iA)=-i\sigma(A)$.

**An antilinear involution of an algebra is called a real structure.** The name is warranted: the fixed set of a real structure is a real form, and every real form of $M_n(\mathbb{C})$ arises from exactly one real structure. Both statements are proved in §*The Two Real Structures*.

**Conjugation is not an inner automorphism.** If $\sigma(A)=SAS^{-1}$ for some fixed $S$ and every $A$, then $\sigma$ would be complex-linear, and it is not: $\sigma(iI)=-iI$ while $S(iI)S^{-1}=iI$. So the real structure is genuinely semilinear, not a conjugation by a matrix. This is the sharp difference between the real structure $\sigma$ and the involutions of the following articles, which are complex-linear.

**Conjugation commutes with the trace, the determinant and the transpose.** Since $\operatorname{tr}\bar A=\overline{\operatorname{tr}A}$ and $\det\bar A=\overline{\det A}$, the two polynomial invariants of a real matrix are real. The transpose and conjugation commute, $\sigma(A^{\mathsf T})=\sigma(A)^{\mathsf T}$, and so do conjugation and the conjugate transpose in the form $\sigma(A^{*})=\sigma(A)^{*}$.

## The Real and the Imaginary Parts

**Every matrix is a real matrix plus $i$ times a real matrix, and the two summands are unique.** Put

$$
\mathrm{Re}\,A=\tfrac12(A+\bar A),\qquad \mathrm{Im}\,A=\tfrac12(A-\bar A)\cdot(-i)=\frac{A-\bar A}{2i}.
$$

Both are real matrices, and $A=\mathrm{Re}\,A+i\,\mathrm{Im}\,A$. The decomposition is the eigenspace decomposition of $\sigma$: the fixed set for the eigenvalue $+1$ and the set $\{A:\sigma(A)=-A\}=iM_n(\mathbb{R})$ for the eigenvalue $-1$. The sum is direct because a matrix that is both real and purely imaginary is zero,

$$
M_n(\mathbb{R})\cap iM_n(\mathbb{R})=\{0\},
$$

and the dimensions add, $n^{2}+n^{2}=2n^{2}$.

**The two summands are orthogonal for the real part of the trace form, and only for the real part.** With $\langle A,B\rangle=\operatorname{tr}(A^{*}B)$ and $X,Y$ real,

$$
\operatorname{tr}(X^{\mathsf T}Y)=\sum_{i,j}X_{ij}Y_{ij}\in\mathbb{R},\qquad \operatorname{Re}\operatorname{tr}\big(X^{\mathsf T}(iY)\big)=0 ,
$$

so the real part of the form has the two summands orthogonal. The Hermitian form itself does not: $\langle X,iY\rangle=i\operatorname{tr}(X^{\mathsf T}Y)$ is purely imaginary and usually nonzero. A statement that the real and the imaginary parts are *orthogonal* is therefore a statement about the real part, and asserting it of the Hermitian form is an error.

**The projections are not algebra homomorphisms.** The map $A\mapsto\mathrm{Re}\,A$ is real-linear and idempotent, but $\mathrm{Re}(AB)\ne(\mathrm{Re}\,A)(\mathrm{Re}\,B)$ in general: the product of two Hermitian matrices need not be Hermitian. The decomposition is a decomposition of the vector space and of the real structure, not of the algebra.

## The Rank over the Two Fields

**The rank of a real matrix is the same number over $\mathbb{R}$ and over $\mathbb{C}$.** The rank is the largest $r$ such that some $r\times r$ minor is nonzero. The minors of a real matrix are real numbers computed from its entries, and a real number is nonzero in $\mathbb{R}$ exactly when it is nonzero in $\mathbb{C}$. Hence

$$
\operatorname{rank}_{\mathbb{R}}A=\operatorname{rank}_{\mathbb{C}}A\qquad\text{for }A\in M_n(\mathbb{R}).
$$

**Invertibility is the same condition over the two fields.** If $A$ is real and $\det A\ne0$, the inverse is $A^{-1}=(\operatorname{adj}A)/\det A$, and the adjugate of a real matrix is real. So

$$
GL_n(\mathbb{R})=GL_n(\mathbb{C})\cap M_n(\mathbb{R}),
$$

and Gaussian elimination on a real matrix can be run with real pivots throughout. Every pivot is a ratio of real minors, so the elimination never leaves $M_n(\mathbb{R})$.

**The degree of the algebra does not change.** The degree of $M_n(\mathbb{C})$ over $\mathbb{C}$ is $n$, the size of its matrix units. Complexification preserves the degree, since $M_n(\mathbb{R})\otimes_{\mathbb{R}}\mathbb{C}=M_n(\mathbb{C})$ and the matrix units of the real algebra complexify to matrix units of the complex one. So the real form has degree $n$ as well. The number of complex parameters of the algebra is $n^{2}$ over either field.

**The singular set meets the real algebra in a real hypersurface.** The set $\Sigma=\{A:\det A=0\}$ is a complex hypersurface of complex dimension $n^{2}-1$. Its intersection with $M_n(\mathbb{R})$ is the zero set of the real polynomial $\det$, of real dimension $n^{2}-1$, and it separates $M_n(\mathbb{R})$ into the two components of $GL_n(\mathbb{R})$. The complex group has no such separation; the point is taken up in *The Topology of $M_n(\mathbb{C})$*.

## The Determinant and the Characteristic Polynomial

**Both are real, and the characteristic polynomial has real coefficients.** The determinant is a polynomial with integer coefficients in the entries, so it takes real values on real matrices. The characteristic polynomial

$$
\chi_A(t)=\det(tI-A)=t^{n}-(\operatorname{tr}A)t^{n-1}+\cdots+(-1)^{n}\det A
$$

therefore has real coefficients whenever $A$ is real. Its coefficients are the elementary symmetric functions of the eigenvalues, and each of them is real.

**The spectrum is stable under conjugation.** If $Av=\lambda v$ with $A$ real, then $A\bar v=\bar\lambda\bar v$, so the conjugate of an eigenvalue is an eigenvalue, with the conjugated eigenvector. The non-real eigenvalues therefore come in pairs $\lambda,\bar\lambda$ of equal algebraic multiplicity, and the number of real eigenvalues, counted with multiplicity, has the same parity as $n$. A real $2\times2$ matrix has either two real eigenvalues or none; a real $3\times3$ matrix has one or three; and so on.

**The trace and the determinant are the two real numbers that survive.** For a real matrix,

$$
\operatorname{tr}A\in\mathbb{R},\qquad \det A\in\mathbb{R},\qquad |\det A|=\prod_{k}|\lambda_k| ,
$$

and the product of a conjugate pair is the positive number $|\lambda|^{2}$. So the sign of the determinant is the sign of the product of the real eigenvalues, and it is the invariant that labels the two components of $GL_n(\mathbb{R})$. The proof of that labelling is in *The Topology of $M_n(\mathbb{C})$*; the counting of the eigenvalues is in *The Spectrum of a Matrix*.

## The Two Real Structures

**A real structure is a $\mathbb{C}$-antilinear algebra automorphism of order two, and $M_n(\mathbb{C})$ carries exactly two of them up to conjugacy.** The first is conjugation $\sigma_1(A)=\bar A$, with fixed algebra $M_n(\mathbb{R})$. The second exists for even $n$: let $J$ be the block-diagonal matrix of $\tfrac{n}{2}$ copies of $\begin{pmatrix}0&1\\-1&0\end{pmatrix}$ and put

$$
\sigma_2(A)=J\bar A J^{-1}.
$$

Then $\sigma_2$ is antilinear, multiplicative, and of order two, since $J$ is real. Its fixed algebra is the set of matrices commuting with $J$ and satisfying $\bar A=J^{-1}AJ$; for $n=2$ that set is a copy of the quaternion algebra $\mathbb{H}$, of real dimension $4$.

**Every real structure is of one of these two shapes.** Let $\sigma$ be a real structure. The map $A\mapsto\sigma(A)$ is antilinear and of order two, so there is an invertible $S$ with $\sigma(A)=S\bar AS^{-1}$; the condition $\sigma^{2}=\mathrm{id}$ reads $S\bar S=cI$ with $c\in\mathbb{R}^{\times}$, and rescaling $S$ normalises $c$ to $\pm1$. If $c=1$ then $S$ is symmetric after a real change of basis and the fixed algebra is conjugate to $M_n(\mathbb{R})$. If $c=-1$ then $n$ is even, $S$ is skew after a change of basis, and the fixed algebra is conjugate to $M_{n/2}(\mathbb{H})$.

**The two fixed algebras have the same real dimension and are not isomorphic.** Both have real dimension $n^{2}$, since $M_{n/2}(\mathbb{H})$ has dimension $4\cdot(n/2)^{2}=n^{2}$. They differ in type. At $n=2$ the fixed algebra of $\sigma_2$ is $\mathbb{H}$, in which every nonzero element is invertible, while $M_2(\mathbb{R})$ contains the nonzero zero divisors $E_{11}$ and $E_{22}$ with $E_{11}E_{22}=0$. So $\mathbb{H}\not\cong M_2(\mathbb{R})$, and the two real structures are not conjugate.

**The two structures differ by an inner automorphism.** Since $J$ is real,

$$
\sigma_1\sigma_2(A)=\overline{J\bar AJ^{-1}}=JAJ^{-1},
$$

which is conjugation by $J$, an automorphism of the complex algebra. The real structures of $M_n(\mathbb{C})$ therefore form two conjugacy classes which meet in the inner automorphism group, and the class of $\sigma_2$ is defined only for even $n$.

**A real structure is not one of the involutions of the split.** The involutions studied in *The Involutions over $\mathbb{R}$ and over $\mathbb{C}$* are complex-linear maps with eigenvalues $\pm1$ on a complex vector space, and their fixed sets are complex subspaces. A real structure is antilinear, and its fixed set is a real form, of real dimension equal to the complex dimension of the ambient space. The two notions both split the algebra into two halves, and the halves are of different kinds.

## What Transfers and What Does Not

**Every identity with rational coefficients transfers from the real algebra to the complex one, and back.** The rank, the trace, the determinant, the characteristic polynomial, the adjugate and the identities among them are polynomial identities in the entries with integer coefficients. They hold over $\mathbb{C}$ and they restrict to $M_n(\mathbb{R})$, and a polynomial identity that holds on all real matrices holds on all complex ones by linearity in the real and imaginary parts separately.

**Diagonalisability does not transfer from the complex field to the real one.** The rotation

$$
R=\begin{pmatrix}0&-1\\1&0\end{pmatrix}
$$

is diagonalisable over $\mathbb{C}$, with eigenvalues $\pm i$, and it satisfies $R^{2}=-I$; over $\mathbb{R}$ it has no eigenvector at all. A real matrix is diagonalisable over $\mathbb{R}$ exactly when its complex diagonalisation can be chosen real, which happens when the eigenvectors of each real eigenvalue can be chosen real and the conjugate pairs are left in $2\times2$ real blocks. The general statement is in *Normal Matrices and the Common Spectral Theorem*.

**Connectedness does not transfer.** The group $GL_n(\mathbb{R})$ has two connected components, labelled by the sign of the determinant, while $GL_n(\mathbb{C})$ is connected. The reason is that $\det$ maps the complex group onto $\mathbb{C}^{\times}$, which is connected, and the real group onto $\mathbb{R}^{\times}$, which is not. The count of the components is the first topological difference between the two base fields; the second is the fundamental group.

**The trace form restricted to the real algebra is the Euclidean form.** For real $X,Y$,

$$
\operatorname{tr}(X^{*}Y)=\operatorname{tr}(X^{\mathsf T}Y)=\sum_{i,j}X_{ij}Y_{ij}
$$

is the standard inner product of $\mathbb{R}^{n^{2}}$. The restriction is real-valued and positive definite, and it is the form used in *The Trace Form and Its Signature on the Two Halves* on the real side.

## The Case $n=2$: the Split Quaternions

**At $n=2$ the real algebra is the split quaternion algebra.** Let

$$
i=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad j=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad k=ij=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
$$

Then $i^{2}=-I$, $j^{2}=I$, $k^{2}=I$, and $ij=-ji=k$. The four matrices $I,i,j,k$ are a real basis of $M_2(\mathbb{R})$. The algebra they span is the **split quaternion algebra** $\mathbb{H}_s$, and it is isomorphic to $M_2(\mathbb{R})$.

**The two real structures at $n=2$ give the two quaternion algebras.** With $J=i$,

$$
\sigma_2(A)=i\bar Ai^{-1},
$$

and the fixed set of $\sigma_2$ is spanned by $I$ and the three matrices $i\sigma_1$, $i\sigma_2$, $i\sigma_3$ of the Pauli list, which multiply by the quaternion rules with all three squares equal to $-I$. So the two real forms of $M_2(\mathbb{C})$ are

$$
\mathbb{H}_s\cong M_2(\mathbb{R}),\qquad \mathbb{H},
$$

of real dimension $4$ each. The first is split, the second is a division algebra. The complex algebra $M_2(\mathbb{C})$ is $\mathbb{B}$, the biquaternion algebra, and the two real forms are its two real quaternion subalgebras.

**The split algebra has a null cone and the division algebra does not.** In $\mathbb{H}_s$ the element $j$ satisfies $j^{2}=I$, so $j-I$ and $j+I$ are nonzero with product $j^{2}-I=0$. In $\mathbb{H}$ every nonzero element is invertible. This is the $n=2$ instance of the general fact that a fixed algebra of a real structure depends on the structure and not only on its dimension. The biquaternion articles read the split case through the idempotents $\tfrac12(I\pm j)$, which are the two Peirce idempotents of $\mathbb{H}_s$; see *The Peirce Decomposition of the Biquaternion Algebra*.

## Summary

The real matrices form the fixed set of the antilinear involution $\sigma(A)=\bar A$ of $M_n(\mathbb{C})$, and $M_n(\mathbb{C})=M_n(\mathbb{R})\otimes_{\mathbb{R}}\mathbb{C}$ is its complexification. The real dimension is $n^{2}$ against $2n^{2}$, while the rank, the degree $n$, the determinant and the characteristic polynomial do not change: a real matrix has the same rank over both fields, its inverse is real when it exists, and its spectrum is stable under conjugation. The two summands $M_n(\mathbb{R})$ and $iM_n(\mathbb{R})$ are orthogonal for the real part of the trace form and not for the Hermitian form. Up to conjugacy $M_n(\mathbb{C})$ carries two real structures, $\bar A$ with fixed algebra $M_n(\mathbb{R})$ and $J\bar AJ^{-1}$ with fixed algebra $M_{n/2}(\mathbb{H})$, of the same real dimension $n^{2}$ and of different isomorphism type. At $n=2$ the two forms are the split quaternions and the quaternions inside the biquaternion algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $M_n(\mathbb{R})$ | the real matrices, a real form of real dimension $n^{2}$ |
| $\sigma(A)=\bar A$ | entrywise conjugation, the first real structure |
| $\mathrm{Re}\,A$, $\mathrm{Im}\,A$ | the real and the imaginary part of $A$ |
| $iM_n(\mathbb{R})$ | the set $\{A:\sigma(A)=-A\}$, of real dimension $n^{2}$ |
| $J$ | the block-diagonal symplectic matrix of $\tfrac{n}{2}$ blocks |
| $\sigma_2(A)=J\bar AJ^{-1}$ | the second real structure, fixed algebra $M_{n/2}(\mathbb{H})$ |
| $\chi_A(t)=\det(tI-A)$ | the characteristic polynomial, with real coefficients for real $A$ |
| $\mathbb{H}_s\cong M_2(\mathbb{R})$ | the split quaternions, the real form at $n=2$ |
| $\mathbb{H}$ | the quaternions, the other real form at $n=2$ |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for real forms, real structures and the two classes of antilinear involutions of a matrix algebra.
- Tsit-Yuen Lam, *A First Course in Noncommutative Rings* (Springer, 2001), for the quaternion algebras, their zero divisors and the split case.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the rank over a subfield, the adjugate and the reality of the characteristic polynomial.
- [The Matrix Algebra $M_n(\mathbb{C})$](the-matrix-algebra-mnc.html), for the algebra, the trace form and the real dimension.
- [Roots of Unity and the Lagrange Idempotents of $M_n(\mathbb{C})$](roots-of-unity-and-the-lagrange-idempotents-of-mnc.html), for the complex construction that the real field does not support.
- [The Peirce Decomposition of the Biquaternion Algebra](the-peirce-decomposition-of-the-biquaternion-algebra.html), for the idempotents of the split case at $n=2$.
