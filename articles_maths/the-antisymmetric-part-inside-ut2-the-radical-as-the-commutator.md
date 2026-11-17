# __The Antisymmetric Part inside $UT_2$: the Radical as the Commutator__

## Introduction

**Inside the upper triangular matrices the antisymmetric part of an element is never available, and the three subspaces that the algebra produces — the derived algebra, the nilradical and the radical of the trace form — coincide with the single nilpotent line $n_+$.**

The article computes the antisymmetric part of an upper triangular matrix, shows that the intersection $UT_2\cap\Lambda^{2}$ is zero and that the antisymmetric part of an element lies outside the algebra, proves the commutator formula, proves that the derived algebra is the nilpotent line, proves that the radical of the trace form is the same line, and states the coincidence of the three subspaces. It assumes *The Triangular Decomposition $h\oplus n_+\oplus n_-$ of $M_2(\mathbb{C})$*, *$UT_2$ as the Complement of the Antisymmetric Part* and *The Two Halves as Orthogonal Complements at $n=2$*.

It defers the comparison of the two models of the symmetric half to *$UT_2$ as a Linear Model of $\operatorname{Sym}_2$: Same Space, Wrong Product* and the geometric reading to *The Geometry of the Two Halves at $n=2$, and the Return of the Two-Sided Operators*.

## The Elements and Their Antisymmetric Parts

**Proposition.** An element $U=\begin{pmatrix}a&b\\ 0&d\end{pmatrix}$ of $UT_2$ has symmetric part $\tfrac12\begin{pmatrix}2a&b\\ b&2d\end{pmatrix}$ and antisymmetric part $\tfrac b2 J$.

**Proof.** The transpose is $\begin{pmatrix}a&0\\ b&d\end{pmatrix}$, so the difference of the matrix and its transpose is $\begin{pmatrix}0&b\\ -b&0\end{pmatrix}=bJ$.

**Corollary.** The intersection $UT_2\cap\Lambda^{2}\mathbb{R}^{2}$ is zero, and the antisymmetric part of an element of $UT_2$ belongs to $UT_2$ only when $b=0$.

**Proof.** An antisymmetric matrix has a nonzero lower left entry as soon as it is nonzero, and an upper triangular matrix has a zero there.

**The off-diagonal entry is the whole obstruction.** The number $b$ measures how far the element is from being symmetric, and the antisymmetric part that measures it is $\tfrac b2J$, a matrix outside the algebra.

**Proof.** The symmetric part is symmetric and the sum of the two parts is $U$; the antisymmetric part is $\tfrac b2J$, which is not upper triangular.

## The Commutator Formula

**Theorem.** For $U=\begin{pmatrix}a&b\\ 0&d\end{pmatrix}$ and $V=\begin{pmatrix}a'&b'\\ 0&d'\end{pmatrix}$,

$$
[U,V]=\begin{pmatrix}0&b'(a-d)-b(a'-d')\\ 0&0\end{pmatrix}.
$$

**Proof.** $UV=\begin{pmatrix}aa'&ab'+bd'\\ 0&dd'\end{pmatrix}$ and $VU=\begin{pmatrix}aa'&a'b+b'd\\ 0&dd'\end{pmatrix}$; the diagonal entries agree and the difference of the off-diagonal entries is $b'(a-d)-b(a'-d')$.

**Corollary.** Every commutator lies in $n_+$, so the derived algebra of $UT_2$ is contained in the nilpotent line.

**Proof.** The display has only one possibly nonzero entry, in the upper right corner.

**Corollary.** With $U=D=\operatorname{diag}(a,d)$ one has $[D,E_{12}]=(a-d)E_{12}$, so the line $n_+$ is reached as soon as the diagonal entries differ.

**Proof.** Put $b=0$, $a'=0$, $b'=1$, $d'=0$ in the formula; the value is $a-d$.

**Corollary.** The derived algebra is exactly $n_+$, and $UT_2$ is solvable of derived length two.

**Proof.** The derived algebra contains $(a-d)E_{12}$ for suitable $D$, hence contains the whole line, and $[n_+,n_+]=0$ because $E_{12}^{2}=0$.

## The Radical of the Trace Form

**Proposition.** The trace form on $UT_2$ has Gram matrix $\operatorname{diag}(1,0,1)$ in the basis $E_{11},E_{12},E_{22}$, of rank $2$ and inertia $(2,0)$ with a one-dimensional radical.

**Proof.** $\operatorname{tr}(E_{11}^{2})=\operatorname{tr}(E_{22}^{2})=1$, $\operatorname{tr}(E_{12}^{2})=\operatorname{tr}(E_{11}E_{12})=\operatorname{tr}(E_{12}E_{22})=0$.

**Corollary.** The radical of the trace form on $UT_2$ is the nilpotent line $n_+$.

**Proof.** The radical is the null space of the Gram matrix, which is spanned by $E_{12}$ in these coordinates; and $\operatorname{tr}(UE_{12})=0$ for every upper triangular $U$ because the product has zero diagonal.

**The form is semidefinite and not definite.** On $UT_2$ the form is positive semidefinite with a one-dimensional kernel, whereas on the symmetric half it is positive definite with eigenvalues $1,1,2$.

**Proof.** $\operatorname{tr}(U^{2})=a^{2}+d^{2}$ for upper triangular $U$, which is a sum of squares and vanishes exactly on the nilpotent line.

## The Three Subspaces Coincide

**Theorem.** In $UT_2$ the derived algebra, the nilradical and the radical of the trace form are all the line $n_+$.

**Proof.** The derived algebra is $n_+$ by the commutator formula. A nilpotent ideal must lie in the nilpotent line, since $E_{11}$ and $E_{22}$ are not nilpotent and every element with a nonzero diagonal entry has a nonzero eigenvalue; and $n_+$ itself is a nilpotent ideal. The radical of the form is $n_+$ by the Gram computation.

**Corollary.** The algebra is the semidirect product of the diagonal algebra with the line $n_+$, and the line is simultaneously the commutator subspace, the nilpotent ideal and the orthogonal degenerate direction.

**Proof.** The vector space splits as $h\oplus n_+$, the line is an ideal, and the three descriptions of the line are the three theorems above.

**The equality of the three spaces is not special to order two, but the collapse into one line is.** At every order the radical of the trace form on $UT_n$ is the strictly upper triangular algebra, which is also the derived algebra and the nilradical; what is special to order two is that this algebra is a single line, so the three descriptions name the same one-dimensional space with no filtration above it.

**Proof.** Pairing a matrix with $E_{ii}$ reads its diagonal entry and pairing it with $E_{ji}$ reads the entry $m_{ij}$ with $j>i$, so a matrix in the radical has zero diagonal and zero entries below it, hence is strictly upper triangular; and the commutator of two upper triangular matrices is strictly upper triangular.

## Solvability and the Filtration

**Proposition.** The lower central series of $UT_2$ is $UT_2$, then $n_+$, then $0$, so the algebra is nilpotent of class two.

**Proof.** The commutator of two elements lies in $n_+$ and the commutator with $n_+$ vanishes because $n_+$ is one-dimensional and abelian.

**Corollary.** The algebra is solvable and nilpotent, and its Killing form vanishes identically.

**Proof.** A nilpotent Lie algebra has a vanishing Killing form, since every adjoint operator is nilpotent and the trace of a product of nilpotent operators is zero.

**Corollary.** The trace form and the Killing form differ completely on $UT_2$: the trace form has rank $2$ and the Killing form is zero.

**Proof.** The trace form is computed above; the Killing form vanishes by nilpotency.

## Why the Antisymmetric Part Cannot Live Inside

**Proposition.** The map $U\mapsto\operatorname{antisym}U$ sends $UT_2$ onto the line $\mathbb{R}J$, and the image meets $UT_2$ only at zero.

**Proof.** The antisymmetric part is $\tfrac b2J$, which runs over the whole line as $b$ runs over the reals, and $J$ is not upper triangular.

**Corollary.** The algebra $UT_2$ is a graph over the symmetric half for the projection $\operatorname{sym}$, and the antisymmetric line is the complementary direction that the algebra does not contain.

**Proof.** The map $\operatorname{sym}$ is the identity on $UT_2\cap\operatorname{Sym}_2$ and has kernel $UT_2\cap\Lambda^{2}=0$, so it is injective, and both spaces have dimension $3$.

**Corollary.** The commutator measures the antisymmetric part of the product, and it is blind to the symmetric part: $\operatorname{antisymmetric}(UV)$ depends only on the diagonal differences and the off-diagonal entries.

**Proof.** The commutator formula is linear in the off-diagonal entries and in the differences of the diagonal entries, and it vanishes when the two diagonal entries agree.

## Summary

For $U=\begin{pmatrix}a&b\\ 0&d\end{pmatrix}$ the antisymmetric part is $\tfrac b2J$, which lies outside $UT_2$ unless $b=0$, so the intersection of the algebra with the antisymmetric line is zero and the off-diagonal entry $b$ is the only obstruction to symmetry.

The commutator is $[U,V]=\bigl(b'(a-d)-b(a'-d')\bigr)E_{12}$, so the derived algebra is the nilpotent line $n_+$, the algebra is nilpotent of class two and solvable of derived length two, and the trace form has Gram matrix $\operatorname{diag}(1,0,1)$ with radical $n_+$. The derived algebra, the nilradical and the radical of the trace form are the same line, and the Killing form vanishes identically while the trace form has rank $2$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $UT_2$ | the upper triangular matrices |
| $n_+$ | the strictly upper triangular line $\mathbb{R}E_{12}$ |
| $h$ | the diagonal algebra |
| $J$ | the antisymmetric unit |
| $\operatorname{antisymmetric}U$ | $\tfrac12(U-U^{\mathsf T})$, equal to $\tfrac b2J$ on $UT_2$ |
| $[U,V]$ | the commutator, always in $n_+$ |

## Further Reading

- Anthony W. Knapp, *Lie Groups Beyond an Introduction* (Birkhäuser, 2002), for solvable and nilpotent Lie algebras, radicals and their Killing forms.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 2013), for the trace form on the triangular algebra and its degeneracy.
- [The Triangular Decomposition $h\oplus n_+\oplus n_-$ of $M_2(\mathbb{C})$](the-triangular-decomposition-h-n-plus-n-minus-of-m2c.html), for the three subspaces and the product rule.
- [$UT_2$ as the Complement of the Antisymmetric Part](ut2-as-the-complement-of-the-antisymmetric-part.html), for the trace form on the triangular algebra.
- [The Lie Algebra $\operatorname{Skew}_2$: One Dimension, Hence Abelian](the-lie-algebra-skew-2-one-dimension-hence-abelian.html), for the antisymmetric line that the algebra does not contain.
