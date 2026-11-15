# __The Split Real Form: $M_n(\mathbb{R})$ inside $M_n(\mathbb{C})$__

## Introduction

**The real matrices are exactly the complex matrices fixed by entrywise conjugation, and this identifies $M_n(\mathbb{R})$ as a real form of $M_n(\mathbb{C})$.** A real form is a real subalgebra whose complexification is the whole algebra. There are two of them, and the real matrices are the split one.

The article proves that the fixed set of conjugation is $M_n(\mathbb{R})$, that $\mathbb{C}\otimes_{\mathbb{R}}M_n(\mathbb{R})=M_n(\mathbb{C})$, that the rank does not change while the spectrum does, that the real and imaginary parts are orthogonal for the real part of the trace form and not for the Hermitian form, and that there are exactly two real forms. It assumes *The Matrix Algebra $M_n(\mathbb{R})$* and *The Matrix Algebra $M_n(\mathbb{C})$*. It defers the spectral consequences to *The Real Spectrum: Real Roots and Conjugate Pairs* and the even case to *The Involutions of the First Kind: Transpose and Symplectic*.

## The Fixed Set of Conjugation

**Entrywise conjugation is a conjugate-linear involution of $M_n(\mathbb{C})$.** Write $c(A)=\bar A$. Then $c^{2}=\mathrm{id}$, $c(A+B)=c(A)+c(B)$, $c(AB)=c(A)c(B)$ and $c(\lambda A)=\bar\lambda c(A)$ for $\lambda\in\mathbb{C}$. It is an anti-linear automorphism, not an anti-automorphism: the order of a product is preserved.

**Its fixed set is $M_n(\mathbb{R})$.** If $\bar A=A$ then every entry is a real number, so $A\in M_n(\mathbb{R})$; conversely a real matrix is fixed. So

$$
M_n(\mathbb{R})=\{A\in M_n(\mathbb{C}):\bar A=A\},
$$

and the inclusion is an inclusion of real algebras, not of complex ones: $M_n(\mathbb{R})$ is not a complex subspace, since $i\mathrm{I}$ is not real.

**The fixed set is not an ideal and not a complex subalgebra.** $M_n(\mathbb{R})$ is closed under sums and products and under real scalars, and it is not closed under multiplication by $i$. It is therefore a real form: a real subspace $V$ with $V\oplus iV=M_n(\mathbb{C})$ as real spaces and $V\cdot V\subseteq V$.

**The direct sum is a decomposition into real and imaginary parts.** Every $A$ is

$$
A=\underbrace{\tfrac12(A+\bar A)}_{\operatorname{Re}A\in M_n(\mathbb{R})}+i\underbrace{\tfrac1{2i}(A-\bar A)}_{\operatorname{Im}A\in M_n(\mathbb{R})},
$$

and the two summands are unique. So $\dim_{\mathbb{R}}M_n(\mathbb{C})=2\dim_{\mathbb{R}}M_n(\mathbb{R})$, that is $2n^{2}=2n^{2}$.

## The Complexification and the Dimension

**The complexification of the real algebra is the complex algebra.** The map

$$
\mathbb{C}\otimes_{\mathbb{R}}M_n(\mathbb{R})\longrightarrow M_n(\mathbb{C}),\qquad \lambda\otimes A\longmapsto\lambda A,
$$

is an isomorphism of complex algebras: it is $\mathbb{C}$-bilinear, multiplicative on the generators, and both sides have complex dimension $n^{2}$. Equivalently, a real basis of $M_n(\mathbb{R})$ is a complex basis of $M_n(\mathbb{C})$, since the $n^{2}$ matrix units are real and complex-linearly independent.

**The dimension doubles and the matrix units do not.** The unit $E_{ij}$ is real, so the complex algebra has the same matrix units and the same product rule. The real dimension is $n^{2}$ for $M_n(\mathbb{R})$ and $2n^{2}$ for $M_n(\mathbb{C})$; the complex dimension of $M_n(\mathbb{C})$ is $n^{2}$. So the two algebras are the same size over their own fields and differ by the factor two in real terms.

**A real basis is half of a complex basis.** The real dimension of the complex algebra, read as a real space, is $2n^{2}$, and the real matrices span an $n^{2}$-dimensional subspace. The complementary subspace is $iM_n(\mathbb{R})$, the imaginary matrices, which is not a subalgebra: the product of two imaginary matrices is real.

## The Rank and the Spectrum

**The rank does not change under the passage to $\mathbb{C}$.** The rank is the largest order of a nonvanishing minor, and the minors of a real matrix are real polynomials in its entries. A complex matrix has rank at least $r$ exactly when some $r\times r$ minor is nonzero, and for real matrices this condition is the same whether tested in $\mathbb{R}$ or in $\mathbb{C}$. Hence

$$
\operatorname{rk}_{\mathbb{C}}A=\operatorname{rk}_{\mathbb{R}}A,\qquad A\in M_n(\mathbb{R}).
$$

So a real matrix is invertible over $\mathbb{C}$ exactly when it is invertible over $\mathbb{R}$, and $\mathrm{GL}_n(\mathbb{R})=\mathrm{GL}_n(\mathbb{C})\cap M_n(\mathbb{R})$.

**The spectrum is conjugation stable but not real.** The characteristic polynomial has real coefficients, so its nonreal roots occur in conjugate pairs. The multiset of eigenvalues satisfies

$$
\operatorname{spec}(A)=\overline{\operatorname{spec}(A)},
$$

and the eigenvalues fall into real points and pairs $\mu,\bar\mu$ with $\mu\notin\mathbb{R}$. This is the single largest difference between the two categories: over $\mathbb{C}$ every root is available, while here the spectrum leaves the base field.

**A real matrix need not be diagonalisable over $\mathbb{R}$ even when it is over $\mathbb{C}$.** The rotation $J=\begin{pmatrix}0&-1\\ 1&0\end{pmatrix}$ has eigenvalues $\pm i$ and is diagonalisable over $\mathbb{C}$ with complex eigenvectors; over $\mathbb{R}$ it has no eigenvector at all. The invariant statement is the real Jordan form with $2\times2$ blocks $\begin{pmatrix}a&-b\\ b&a\end{pmatrix}$, which is *The Real Jordan Form and the Rotation Blocks*.

**The determinant and the trace are the two coefficients that stay real.** The determinant is the product of the eigenvalues, hence real and equal to the product over the conjugate pairs, $\det A=\prod_{\text{real}}\lambda\prod_{\text{pairs}}|\mu|^{2}$. The trace is the sum, hence real and equal to the sum over the real roots plus twice the real parts of the nonreal ones. Both computations agree with the real Leibniz expansion.

## The Two Real Structures

**A real structure on $M_n(\mathbb{C})$ is a conjugate-linear automorphism of order two, and its fixed set is a real form.** The conjugate-linear automorphism $c(A)=\bar A$ gives $M_n(\mathbb{R})$. A second one is available when $n$ is even: with $J$ the standard symplectic matrix,

$$
c_J(A)=J\bar A J^{-1},
$$

which is conjugate linear, multiplicative, and of order two because $J\bar J=J^{2}=-\mathrm{I}$ cancels twice.

**The fixed set of $c_J$ is $M_{n/2}(\mathbb{H})$, the matrices over the quaternions.** Writing $n=2m$ and cutting $A$ into $2\times2$ blocks, the condition $J\bar AJ^{-1}=A$ says that each block has the form $\begin{pmatrix}u&v\\ -\bar v&\bar u\end{pmatrix}$, which is the regular representation of a quaternion $u+vj$. So the fixed algebra is $M_m(\mathbb{H})$, of real dimension $4m^{2}=n^{2}$.

**There are exactly two real forms.** Let $c'$ be any conjugate-linear automorphism of order two. Then $c'c$ is a complex-linear automorphism, hence inner by Skolem–Noether: $c'c=\operatorname{Ad}_S$ for some $S$, and $c'=\operatorname{Ad}_S\circ c$. The condition $c'^{2}=\mathrm{id}$ becomes $S\bar S$ central, and a rescaling absorbs the scalar. So $c'$ is conjugate to $c$, giving $M_n(\mathbb{R})$, or, when $n$ is even and $S\bar S=-\mathrm{I}$ up to a square, to $c_J$, giving $M_{n/2}(\mathbb{H})$. No third case occurs, and for odd $n$ the quaternionic form does not exist.

**The real matrices are the split form, and the test is the idempotents.** $M_n(\mathbb{R})$ contains the $n$ orthogonal idempotents $E_{11},\dots,E_{nn}$, of rank one, summing to $\mathrm{I}$. The algebra $M_m(\mathbb{H})$ contains no idempotent other than $0$ and $\mathrm{I}$: if $P^{2}=P$ then $P$ is a projection onto a quaternionic subspace, and such a subspace has a complement, so $P=0$ or $P=\mathrm{I}$ when the module is a single copy. A real form with a full family of $n$ idempotents is **split**; one without is not. So $M_n(\mathbb{R})$ is split and $M_{n/2}(\mathbb{H})$ is not.

## The Trace Form and the Real Part

**The real part of the Hermitian form is the Hilbert–Schmidt form of the real algebra.** On $M_n(\mathbb{C})$ the form $\langle A,B\rangle_{\mathbb{C}}=\operatorname{tr}(A^{*}B)$ is positive definite Hermitian. For real $A$ and $B$ its real part is

$$
\operatorname{Re}\operatorname{tr}(A^{*}B)=\operatorname{tr}(A^{\mathsf T}B)=\sum_{i,j}A_{ij}B_{ij},
$$

which is the positive definite form of $M_n(\mathbb{R})$, and its imaginary part is zero. So the real algebra sits inside the complex one isometrically for the real part of the Hermitian form.

**The real and imaginary subspaces are orthogonal for $\operatorname{Re}\operatorname{tr}(A^{*}B)$ and not for the Hermitian form.** If $A$ is real and $B=iC$ with $C$ real, then $\operatorname{tr}(A^{*}B)=\operatorname{tr}(A^{\mathsf T}iC)=i\operatorname{tr}(A^{\mathsf T}C)$ is purely imaginary, so its real part is zero; hence the two subspaces are perpendicular. For the Hermitian form they are not: that same number is imaginary and nonzero, so the Hermitian pairing of a real with an imaginary matrix is neither zero nor real.

**The trace form is the complexification of the real trace form.** The bilinear form $\operatorname{tr}(AB)$ on $M_n(\mathbb{R})$ has signature $(n(n+1)/2,n(n-1)/2)$; on $M_n(\mathbb{C})$ the same expression is complex bilinear and nondegenerate, with no real signature of its own. Since it is the complexification of the real form, its Witt index is the larger of the two numbers, $n(n+1)/2$. Over $\mathbb{R}$ no form is both definite and invariant; over $\mathbb{C}$ the Hermitian form is.

## The Split Quaternion Instance at $n=2$

**At $n=2$ the split form is the split-quaternion algebra, and the compact form is the quaternions.** The algebra $M_2(\mathbb{R})$ is $\mathbb{H}_{\mathrm{spl}}$, whose complexification is $M_2(\mathbb{C})=\mathbb{B}$, the biquaternion algebra. The other real form of $M_2(\mathbb{C})$ is $M_1(\mathbb{H})=\mathbb{H}$.

**The two forms are distinguished by their idempotents and by their norms.** $\mathbb{H}_{\mathrm{spl}}$ has the two idempotents $\tfrac12(1\pm\vec e_y)$ and the indefinite norm of signature $(2,2)$; $\mathbb{H}$ has no idempotent besides $0$ and $1$ and its norm is positive definite, of signature $(4,0)$. The biquaternion algebra carries both structures, the quaternion conjugation ${}^{\natural}$ with its N-norm of signature $(4,4)$, and the complex conjugation with the definite Hermitian form.

**The passage is by extension of scalars only.** $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}_{\mathrm{spl}}=M_2(\mathbb{C})$ and $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}=M_2(\mathbb{C})$, so the two real algebras become the same complex algebra. Everything that distinguishes them is lost under the tensor product with $\mathbb{C}$; this is why the real category needs its own articles.

## Summary

$M_n(\mathbb{R})$ is the fixed set of the entrywise conjugation of $M_n(\mathbb{C})$, a real form of real dimension $n^{2}$ whose complexification is the whole algebra. The rank is unchanged by the passage to $\mathbb{C}$, the spectrum is conjugation stable and may leave $\mathbb{R}$, and the real Jordan form carries rotation blocks. The real and imaginary parts are orthogonal for the real part of the Hermitian form and not for the Hermitian form itself. There are exactly two real forms, the split $M_n(\mathbb{R})$ and the quaternionic $M_{n/2}(\mathbb{H})$ for even $n$, and they are told apart by their idempotents: the split form has a full family of $n$ rank-one idempotents, the quaternionic form has none. At $n=2$ the pair is $\mathbb{H}_{\mathrm{spl}}$ and $\mathbb{H}$, and both complexify to the biquaternion algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $c(A)=\bar A$ | entrywise conjugation, a conjugate-linear involution |
| $c_J(A)=J\bar AJ^{-1}$ | the quaternionic real structure, for even $n$ |
| $\operatorname{Re}A$, $\operatorname{Im}A$ | the real and imaginary parts, both real matrices |
| $\mathbb{C}\otimes_{\mathbb{R}}M_n(\mathbb{R})$ | the complexification, isomorphic to $M_n(\mathbb{C})$ |
| $M_{n/2}(\mathbb{H})$ | the quaternionic real form, for even $n$ |
| $\operatorname{tr}(A^{*}B)$ | the Hermitian form whose real part is the Hilbert–Schmidt form |

## Further Reading

- Tsit-Yuen Lam, *A First Course in Noncommutative Rings* (Springer, 2001), for central simple algebras and their forms.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for real forms and involutions of the first and second kind.
- [The Matrix Algebra $M_n(\mathbb{R})$](the-matrix-algebra-mnr.html), for the real algebra itself.
- [The Matrix Algebra $M_n(\mathbb{C})$](the-matrix-algebra-mnc.html), for the complex algebra and its Hermitian form.
- [The Biquaternion Algebra](the-biquaternion-algebra.html), for the algebra that both real forms complexify to.
- [Quaternion Algebra](quaternion-algebra.html), for the compact real form $M_{n/2}(\mathbb{H})$ at $n=2$.
