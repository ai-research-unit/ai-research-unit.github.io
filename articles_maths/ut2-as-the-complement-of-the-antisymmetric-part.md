# __$UT_2$ as the Complement of the Antisymmetric Part__

## Introduction

**The upper triangular matrices form a three-dimensional complement to the antisymmetric line, and that complement is not the orthogonal one: the trace form on it is degenerate, with the nilpotent line as radical.**

The article proves the vector space decomposition $M_2(\mathbb{R})=UT_2\oplus\Lambda^{2}\mathbb{R}^{2}$, writes the projection onto $UT_2$ along the antisymmetric line, compares it with the orthogonal complement that is the symmetric half, computes the radical of the restricted trace form, and shows that the radical is exactly the nilradical of $UT_2$. It assumes *The Triangular Decomposition $h\oplus n_+\oplus n_-$ of $M_2(\mathbb{C})$*, *The Two Halves as Orthogonal Complements at $n=2$* and *The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric at $n=2$*.

It defers the question of the product carried by a complement of the same dimension to *$UT_2$ as a Linear Model of $\operatorname{Sym}_2$: Same Space, Wrong Product*, and the bracket of the triangular algebra to *The Antisymmetric Part inside $UT_2$: the Radical as the Commutator*.

## The Two Subspaces

**The dimensions match.** $\dim_{\mathbb{R}}UT_2=3$ and $\dim_{\mathbb{R}}\Lambda^{2}\mathbb{R}^{2}=1$, so the two dimensions add to $4$, the dimension of $M_2(\mathbb{R})$.

**Theorem.** The intersection is zero and the sum is the whole space:

$$
M_2(\mathbb{R})=UT_2\oplus\Lambda^{2}\mathbb{R}^{2},\qquad \dim=3+1=4 .
$$

**Proof.** An upper triangular matrix has a zero lower-left entry, and the antisymmetric matrices are the multiples of $J=\begin{pmatrix}0&1\\ -1&0\end{pmatrix}$, whose lower-left entry is $-1$; an antisymmetric matrix that is also upper triangular is therefore zero. The dimensions then give the sum.

**Corollary.** $UT_2$ is a complement of the antisymmetric line, so every matrix splits as an upper triangular part plus a multiple of $J$ in exactly one way.

**Proof.** A direct sum decomposition gives existence and uniqueness of the two components.

## The Projection onto $UT_2$

**Proposition.** The projection onto $UT_2$ along the antisymmetric line is

$$
P\begin{pmatrix}a&b\\ c&d\end{pmatrix}=\begin{pmatrix}a&b+c\\ 0&d\end{pmatrix},
$$

and the antisymmetric part of a matrix is $-cJ$.

**Proof.** $A-P(A)=\begin{pmatrix}0&-c\\ c&0\end{pmatrix}=-cJ$, which is antisymmetric; and $P(A)$ is upper triangular. The map $P$ is linear, its image is $UT_2$, and its kernel is the antisymmetric line.

**Corollary.** $P$ is a projection: $P^{2}=P$, its rank is $3$ and its kernel is one-dimensional.

**Proof.** For $U$ upper triangular one has $P(U)=U$, since the lower-left entry is zero and adds nothing to the upper-right one.

**The projection changes an entry that the reader does not expect.** The corner $(1,2)$ is modified: its new value is $b+c$, not $b$. The correction is exactly the antisymmetric part, which has to be moved into the symmetric direction of the off-diagonal plane.

**In complex form.** Over $\mathbb{C}$ the same formulas hold, with $UT_2$ of complex dimension $3$ and the complex line $\mathbb{C}J$ of dimension $1$; the real statement is the restriction to real matrices.

## The Other Complement

**Proposition.** The orthogonal complement of the antisymmetric line for the trace form is the symmetric half, not $UT_2$.

**Proof.** That complement is the symmetric half by *The Two Halves as Orthogonal Complements at $n=2$*; the two spaces $\operatorname{Sym}_2(\mathbb{R})$ and $UT_2$ are both three-dimensional complements of the same line, so they are different complements of the same subspace.

**They cut the off-diagonal plane in different lines.** Inside the two-dimensional plane of off-diagonal matrices the symmetric half is the line spanned by $E_{12}+E_{21}$ and the triangular algebra is the line spanned by $E_{12}$; the two complements differ only in that plane.

**Proposition.** The two complements meet in the diagonal, so they share a two-dimensional piece and differ in the off-diagonal plane.

**Proof.** A matrix that is both upper triangular and symmetric has $b=c$ and $c=0$, hence is diagonal.

**Corollary.** The pair of complements shows that a subspace of codimension one has many complements but only one orthogonal complement, and the two are related by a shear in the two-dimensional off-diagonal plane.

## The Restricted Trace Form

**Theorem.** In the basis $E_{11},E_{22},E_{12}$ of $UT_2$ the Gram matrix of the trace form is

$$
\begin{pmatrix}1&0&0\\ 0&1&0\\ 0&0&0\end{pmatrix},
$$

so the restriction is degenerate and its radical is the line $n_+=\mathbb{R}E_{12}$.

**Proof.** $\operatorname{tr}(E_{11}^{2})=\operatorname{tr}(E_{22}^{2})=1$, $\operatorname{tr}(E_{11}E_{22})=0$, and $E_{12}^{2}=0$ with $\operatorname{tr}(E_{11}E_{12})=\operatorname{tr}(E_{22}E_{12})=0$; so the last row and the last column vanish and the radical is spanned by $E_{12}$.

**Corollary.** $\operatorname{rad}(UT_2)=n_+$ and $UT_2^{\perp}=\mathbb{R}E_{12}$ for the trace form on $M_2(\mathbb{R})$.

**Proof.** The radical of the restriction is $UT_2\cap UT_2^{\perp}$; the orthogonal complement is computed from $\operatorname{tr}(E_{11}X)=\operatorname{tr}(E_{22}X)=\operatorname{tr}(E_{12}X)=0$, which force $x_{11}=x_{22}=x_{21}=0$.

**Corollary.** $UT_2$ is not isotropic, and it is not a maximal isotropic subspace either.

**The radical is the nilradical.** The two notions agree at this order: the radical of the trace form on $UT_2$ is the nilpotent radical $n_+$, the largest nilpotent ideal, which is the content of *The Antisymmetric Part inside $UT_2$: the Radical as the Commutator*.

## The Dimension Count and What It Does Not Give

**$UT_2$ and $\operatorname{Sym}_2$ have the same dimension.** Both are three-dimensional real spaces, so there are linear isomorphisms between them, for example

$$
\begin{pmatrix}a&b\\ 0&d\end{pmatrix}\longmapsto\begin{pmatrix}a&b/2\\ b/2&d\end{pmatrix}.
$$

**Proof.** The map is linear, injective, and its image is the symmetric half; the inverse is $\begin{pmatrix}a&s\\ s&d\end{pmatrix}\mapsto\begin{pmatrix}a&2s\\ 0&d\end{pmatrix}$.

**The isomorphism is not multiplicative.** It carries the identity to the identity, but it does not carry products to products, so it is only a linear identification.

**Proof.** Take the upper triangular matrix $U=E_{12}$ and its image $S=\tfrac12(E_{12}+E_{21})$. In $UT_2$ one has $U^{2}=0$, while $S^{2}=\tfrac14 I$; the two products do not correspond.

**Corollary.** A common dimension is not a common algebra, and the comparison of the products is the subject of *$UT_2$ as a Linear Model of $\operatorname{Sym}_2$: Same Space, Wrong Product*.

## Why the Complement Is Useful

**The complement gives the flag coordinates.** $UT_2$ is the stabiliser of the line $\mathbb{C}e_{1}$, so its elements are the matrices that preserve the first step of the flag; the antisymmetric line is the direction that moves the line most, in the sense that $J$ sends $e_{1}$ to $-e_{2}$.

**Proof.** The first column of an upper triangular matrix is a multiple of $e_{1}$, and the first column of $J$ is $-e_{2}$.

**The complement is the tangent space of the parabolic.** The matrices preserving the line form the closed subgroup of the upper triangular matrices, of complex dimension $3$, and its tangent space at the identity is $UT_2$; the antisymmetric line lies outside that tangent space, since $J$ does not preserve the line.

**The two complements answer two different questions.** The symmetric complement answers the question of the orthogonal projection for the trace form; the triangular complement answers the question of the flag and of the parabolic subalgebra.

## Summary

$M_2(\mathbb{R})$ is the direct sum of the three-dimensional upper triangular algebra and the antisymmetric line, and the projection onto $UT_2$ along that line sends $\begin{pmatrix}a&b\\ c&d\end{pmatrix}$ to $\begin{pmatrix}a&b+c\\ 0&d\end{pmatrix}$.

The symmetric half is the orthogonal complement of the antisymmetric line, so the triangular complement is a non-orthogonal one; the two complements differ by a shear of the off-diagonal plane and meet in the diagonal. The trace form on $UT_2$ has Gram matrix $\operatorname{diag}(1,1,0)$, so its radical is the nilpotent line $n_+$, which is also the nilradical of the algebra, and $UT_2^{\perp}=\mathbb{R}E_{12}$. The linear isomorphism $UT_2\cong\operatorname{Sym}_2$ is not multiplicative.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $UT_2$ | the upper triangular algebra |
| $J$ | $\begin{pmatrix}0&1\\ -1&0\end{pmatrix}$, spanning the antisymmetric line |
| $P$ | the projection onto $UT_2$ along $\mathbb{R}J$ |
| $n_+$ | $\mathbb{R}E_{12}$, the nilpotent line |
| $\operatorname{rad}(UT_2)$ | the radical of the restricted trace form, equal to $n_+$ |
| $UT_2^{\perp}$ | the orthogonal complement, also $\mathbb{R}E_{12}$ |

## Further Reading

- Armand Borel, *Linear Algebraic Groups* (Springer, 1991), for parabolics, flags and their tangent spaces.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 2013), for degenerate restrictions of the trace pairing.
- [The Two Halves as Orthogonal Complements at $n=2$](the-two-halves-as-orthogonal-complements-at-n-2.html), for the orthogonal complement of the antisymmetric line.
- [The Triangular Decomposition $h\oplus n_+\oplus n_-$ of $M_2(\mathbb{C})$](the-triangular-decomposition-h-n-plus-n-minus-of-m2c.html), for the triangular algebra and its nilradical.
- [The Ideals, the Centre and the Simplicity of $M_2(\mathbb{C})$](the-ideals-the-centre-and-the-simplicity-of-m2c.html), for the ideals of the triangular algebra.
