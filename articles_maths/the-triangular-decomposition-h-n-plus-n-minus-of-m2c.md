# __The Triangular Decomposition $h\oplus n_+\oplus n_-$ of $M_2(\mathbb{C})$__

## Introduction

**The algebra splits into the diagonal algebra of dimension $2$ and the two strictly triangular lines, and the brackets of the three pieces form the root system $A_{1}$.**

The article proves the decomposition $M_2(\mathbb{C})=h\oplus n_+\oplus n_-$, identifies $h\oplus n_+$ with the algebra $UT_2$ of upper triangular matrices and with the stabiliser of a line, computes the brackets between the three pieces, reads the roots $\pm\alpha$ and the coroot, and shows that $n_+$ is the nilradical of $UT_2$. It assumes *The Fine Decomposition against the Diagonal at $n=2$* for the corner coordinates and *The Ideals, the Centre and the Simplicity of $M_2(\mathbb{C})$* for the ideals.

It defers the antisymmetric part inside $UT_2$ to *The Antisymmetric Part inside $UT_2$: the Radical as the Commutator* and the warning about the wrong product to *$UT_2$ as a Linear Model of $\operatorname{Sym}_2$: Same Space, Wrong Product*. The biquaternion version of the same split is *The Peirce Basis of the Biquaternion Algebra*, where the two triangular lines are the mixed corners.

## The Decomposition

**Definition.** In the standard frame the three pieces are

$$
h=\left\{\begin{pmatrix}a&0\\ 0&d\end{pmatrix}\right\},\qquad
n_+=\mathbb{C}E_{12}=\left\{\begin{pmatrix}0&b\\ 0&0\end{pmatrix}\right\},\qquad
n_-=\mathbb{C}E_{21}=\left\{\begin{pmatrix}0&0\\ c&0\end{pmatrix}\right\}.
$$

**Theorem.** The sum is direct and equal to the algebra:

$$
M_2(\mathbb{C})=h\oplus n_+\oplus n_-,\qquad \dim_{\mathbb{C}}=2+1+1=4 .
$$

**Proof.** Every matrix is $\begin{pmatrix}a&b\\ c&d\end{pmatrix}$, with $a,d$ in $h$ and $b,c$ in the two lines; independence follows by reading the four entries separately.

**Corollary.** $M_2(\mathbb{C})=(h\oplus n_+)\oplus n_-$ is also the sum of the upper triangular algebra and the strictly lower line, and that is the form used in *$UT_2$ as the Complement of the Antisymmetric Part*.

**The decomposition refines the split into the two halves.** The diagonal $h$ lies inside the symmetric half, and each of the two lines $n_\pm$ splits into a symmetric and an antisymmetric part.

## The Algebra $UT_2$

**Definition.** $UT_2=h\oplus n_+$ is the algebra of upper triangular matrices.

**Proposition.** $UT_2$ is a subalgebra of dimension $3$, the line $n_+$ is a two-sided ideal of it, and $UT_2/n_+\cong h\cong\mathbb{C}\times\mathbb{C}$.

**Proof.** The product of two upper triangular matrices is upper triangular, and the product of an upper triangular matrix with a strictly upper one is strictly upper. The quotient by $n_+$ is the image of the diagonal, and diagonal matrices multiply entrywise.

**Proposition.** $UT_2=\{A:A(\mathbb{C}e_{1})\subseteq\mathbb{C}e_{1}\}$ is the stabiliser of the line $\mathbb{C}e_{1}$, so it is the parabolic subalgebra attached to that line.

**Proof.** The first column of $A$ is the image of $e_{1}$, and the condition that it be a multiple of $e_{1}$ is $c=0$, that is $A\in h\oplus n_+$.

**Corollary.** The parabolic subalgebras of $M_2(\mathbb{C})$ are the stabilisers of the lines of $\mathbb{C}^{2}$; they are parametrised by $\mathbb{P}^{1}$ and they are all conjugate.

**Proof.** Each line gives one stabiliser, and $\mathrm{GL}_2(\mathbb{C})$ acts transitively on the lines.

**The nilradical.** The line $n_+$ is nilpotent, since $E_{12}^{2}=0$, and it is the largest nilpotent ideal of $UT_2$; so the nilpotent radical of $UT_2$ is $n_+$ and $UT_2$ is not reductive.

## The Brackets of the Three Pieces

**Theorem.** The three pieces satisfy

$$
[h,h]=0,\qquad [h,n_+]\subseteq n_+,\qquad [h,n_-]\subseteq n_-,\qquad [n_+,n_-]\subseteq h,\qquad [n_+,n_+]=[n_-,n_-]=0 .
$$

**Proof.** The diagonal matrices commute and act diagonally on the two matrix units: for $D=\operatorname{diag}(a,d)$ one has $[D,E_{12}]=(a-d)E_{12}$ and $[D,E_{21}]=(d-a)E_{21}$. The bracket $[E_{12},E_{21}]=E_{11}-E_{22}$ is diagonal, and a one-dimensional space brackets to zero with itself.

**Corollary.** The traceless diagonal $h_{0}=\mathbb{C}(E_{11}-E_{22})$ is a Cartan subalgebra of $\mathfrak{sl}_2(\mathbb{C})$, and $\mathfrak{sl}_2(\mathbb{C})=h_{0}\oplus n_+\oplus n_-$ is its root space decomposition.

**Proof.** The three spaces lie inside the traceless algebra, their dimensions are $1+1+1=3$, and the brackets above are the root space axioms.

**The roots are $\pm\alpha$.** Define $\alpha\in h_{0}^{*}$ by $\alpha(\operatorname{diag}(a,-a))=2a$. Then $[X,E_{12}]=\alpha(X)E_{12}$ and $[X,E_{21}]=-\alpha(X)E_{21}$ for $X\in h_{0}$, so the two lines are the root spaces of $\alpha$ and of $-\alpha$.

**The coroot.** With $H=E_{11}-E_{22}$ one has $\alpha(H)=2$ and $\operatorname{tr}(H^{2})=2$, so $\langle H,X\rangle=\alpha(X)$ for every $X\in h_{0}$; the element $H$ is the coroot of $\alpha$, and the normalisation by the trace form is what makes the pairing return the structural constant $2$.

**The root system is $A_{1}$.** There are two roots, opposite to one another, and the Weyl group is the group of order two that exchanges them. At order $n$ the root system is $A_{n-1}$ and the Weyl group is the symmetric group, which is *The Matrix Algebra $M_n(\mathbb{C})$*.

## The Triangular Decomposition and the Flag

**Proposition.** The decomposition records the flag $0\subset\mathbb{C}e_{1}\subset\mathbb{C}^{2}$: the line $n_+$ moves the line, the diagonal $h$ preserves it, and the line $n_-$ sends it to $0$.

**Proof.** $E_{12}$ sends $e_{1}$ to $e_{2}$, which leaves the line; a diagonal matrix keeps $e_{1}$ inside the line; $E_{21}$ kills $e_{1}$.

**Corollary.** $n_+\oplus n_-$ is the space of matrices with zero diagonal, of dimension $2$, that is the tangent space to the set of matrices killing the flag.

**Proof.** A matrix of $n_+\oplus n_-$ has both diagonal entries zero, and conversely a matrix with zero diagonal lies in the sum of the two lines.

**The split is orthogonal in one direction only.** The diagonal $h$ is orthogonal to the off-diagonal plane for the trace form, since $\operatorname{tr}(E_{ii}E_{12})=\operatorname{tr}(E_{ii}E_{21})=0$; but $n_+$ and $n_-$ are not orthogonal, since $\operatorname{tr}(E_{12}E_{21})=1$.

**Proof.** The two computations are immediate from $\operatorname{tr}(E_{ij}E_{kl})=\delta_{jk}\delta_{il}$.

## The Two Lines and the Two Halves

**Proposition.** The symmetric half meets $n_+$ in the real line spanned by $E_{12}+E_{21}$ and meets $n_-$ in the same real line; the antisymmetric half meets $n_+$ in the real line spanned by $E_{12}-E_{21}$.

**Proof.** A matrix $bE_{12}+cE_{21}$ is symmetric exactly when $b=c$, and antisymmetric exactly when $b=-c$.

**Corollary.** Inside the off-diagonal plane the two halves are two lines, orthogonal for the trace form and exchanged by a rotation of angle $\pi/4$ of that plane.

**Proof.** The pairing of $E_{12}+E_{21}$ with $E_{12}-E_{21}$ is $\operatorname{tr}(E_{12}E_{21}-E_{21}E_{12})=1-1=0$.

**Corollary.** $UT_2$ contains the two-dimensional part $h\oplus\mathbb{R}(E_{12}+E_{21})$ of the symmetric half, and its third direction $E_{12}-E_{21}$ is antisymmetric.

**Proof.** The diagonal is symmetric and $E_{12}+E_{21}$ is symmetric, while $E_{12}-E_{21}$ is antisymmetric and completes a basis with them.

**The antisymmetric direction is the radical.** In $UT_2$ the antisymmetric line is exactly the commutator subspace, which is the content of *The Antisymmetric Part inside $UT_2$: the Radical as the Commutator*.

## Summary

$M_2(\mathbb{C})$ splits as the diagonal algebra of dimension $2$ and the two strictly triangular lines $n_+=\mathbb{C}E_{12}$ and $n_-=\mathbb{C}E_{21}$. The sum $h\oplus n_+$ is the upper triangular algebra $UT_2$, of dimension $3$, the stabiliser of the line $\mathbb{C}e_{1}$ and the parabolic attached to it, with nilradical $n_+$.

The brackets are $[h,n_\pm]\subseteq n_\pm$ and $[n_+,n_-]\subseteq h$, and each of the two nilpotent lines brackets to zero with itself. The traceless diagonal is a Cartan subalgebra of $\mathfrak{sl}_2(\mathbb{C})$ with roots $\pm\alpha$, where $\alpha(\operatorname{diag}(a,-a))=2a$, coroot $E_{11}-E_{22}$, and root system $A_{1}$. The diagonal is orthogonal to the off-diagonal plane, but the two nilpotent lines pair to $1$ and are not orthogonal. Inside the off-diagonal plane the symmetric and the antisymmetric halves are two orthogonal lines.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $h$ | the diagonal algebra, dimension $2$ |
| $n_+$ | $\mathbb{C}E_{12}$, the strictly upper line |
| $n_-$ | $\mathbb{C}E_{21}$, the strictly lower line |
| $UT_2$ | $h\oplus n_+$, the upper triangular algebra |
| $h_{0}$ | the traceless diagonal, a Cartan subalgebra |
| $\alpha$ | the root, $\alpha(\operatorname{diag}(a,-a))=2a$ |
| $H$ | $E_{11}-E_{22}$, the coroot direction |
| $A_{1}$ | the root system of $\mathfrak{sl}_2$ |

## Further Reading

- James E. Humphreys, *Introduction to Lie Algebras and Representation Theory* (Springer, 1972), for root space decompositions and the system $A_{1}$.
- Armand Borel, *Linear Algebraic Groups* (Springer, 1991), for parabolics as stabilisers of flags.
- [The Fine Decomposition against the Diagonal at $n=2$](the-fine-decomposition-against-the-diagonal-at-n-2.html), for the corner coordinates used here.
- [The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric at $n=2$](the-two-halves-over-r-symmetric-and-antisymmetric-at-n-2.html), for the symmetric and antisymmetric lines inside the triangular pieces.
- [The Peirce Basis of the Biquaternion Algebra](the-peirce-basis-of-the-biquaternion-algebra.html), for the mixed corners in the biquaternion language.
