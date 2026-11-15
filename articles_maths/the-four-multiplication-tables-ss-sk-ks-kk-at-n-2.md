# __The Four Multiplication Tables: $SS$, $SK$, $KS$, $KK$ at $n=2$__

## Introduction

**With the basis $I,\sigma_{3},\sigma_{1},J$ of the real matrix algebra, the sixteen products fall into four tables of sizes $3\times3$, $3\times1$, $1\times3$ and $1\times1$, and the two mixed tables differ by a sign in every entry.**

The article writes the four multiplication tables, reads the symmetric block, shows that the symmetric half is not closed under the plain product because two entries of the $SS$ table leave it, computes the tables for the anticommutator and the commutator, and checks associativity on the structure constants. It assumes *The Symmetric and Antisymmetric Parts of a Product at $n=2$* and *The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric at $n=2$*.

It defers the algebra axioms of the symmetric half to *The Jordan Algebra $\operatorname{Sym}_2$* and the bracket to *The Lie Algebra $\operatorname{Skew}_2$: One Dimension, Hence Abelian*.

## The Basis

**Definition.** The basis of $M_2(\mathbb{R})$ used throughout is

$$
I=\begin{pmatrix}1&0\\ 0&1\end{pmatrix},\qquad
\sigma_{3}=\begin{pmatrix}1&0\\ 0&-1\end{pmatrix},\qquad
\sigma_{1}=\begin{pmatrix}0&1\\ 1&0\end{pmatrix},\qquad
J=\begin{pmatrix}0&1\\ -1&0\end{pmatrix}.
$$

**Proposition.** The first three are symmetric, form a basis of $\operatorname{Sym}_2(\mathbb{R})$, and the last is antisymmetric and spans $\Lambda^{2}\mathbb{R}^{2}$.

**Proof.** Reading the entries, the first three are symmetric and independent, and $J$ is antisymmetric; the dimensions are $3$ and $1$.

**The basis is orthogonal for the trace form.** The pairings are $\operatorname{tr}(I^{2})=\operatorname{tr}(\sigma_{3}^{2})=\operatorname{tr}(\sigma_{1}^{2})=2$ and $\operatorname{tr}(J^{2})=-2$, and every mixed pairing vanishes.

**Proof.** $\operatorname{tr}(I\sigma_{3})=\operatorname{tr}(\sigma_{3}\sigma_{1})=\operatorname{tr}(\sigma_{1}J)=\operatorname{tr}(IJ)=0$ is a direct computation of the two-by-two products.

**The scaling by a half makes the basis orthonormal.** The matrices $I/\sqrt2$, $\sigma_{3}/\sqrt2$, $\sigma_{1}/\sqrt2$ are orthonormal for the trace form on the symmetric half and $J/\sqrt2$ has squared length $-1$.

**Proof.** Divide the four squared lengths by $2$; three are $+1$ and one is $-1$, which is the signature $(3,1)$.

## The Table $SS$

**Theorem.** The products of two symmetric basis elements are

| $\cdot$ | $I$ | $\sigma_{3}$ | $\sigma_{1}$ |
|---|---|---|---|
| $I$ | $I$ | $\sigma_{3}$ | $\sigma_{1}$ |
| $\sigma_{3}$ | $\sigma_{3}$ | $I$ | $J$ |
| $\sigma_{1}$ | $\sigma_{1}$ | $-J$ | $I$ |

**Proof.** Each entry is a two-by-two product: $I$ is the identity, $\sigma_{3}^{2}=\sigma_{1}^{2}=I$, and $\sigma_{3}\sigma_{1}=-\sigma_{1}\sigma_{3}=J$. The last identity is the computation $\sigma_{3}\sigma_{1}=\begin{pmatrix}0&1\\ -1&0\end{pmatrix}=J$ and $\sigma_{1}\sigma_{3}=\begin{pmatrix}0&-1\\ 1&0\end{pmatrix}=-J$.

**Corollary.** The symmetric half is not closed under the plain product: two of the nine entries, $\sigma_{3}\sigma_{1}$ and $\sigma_{1}\sigma_{3}$, lie in the antisymmetric line.

**Proof.** The two entries are $\pm J$, and $J$ is not symmetric.

**Corollary.** The table is symmetric apart from those two entries, and the antisymmetric entries are antisymmetric in the two factors: swapping $\sigma_{3}$ and $\sigma_{1}$ changes the sign of the out-of-half entry.

**Proof.** $I$ commutes with everything and the two other basis elements commute up to sign, with the sign carried by the $J$ entry.

**The symmetrised table is closed.** Replacing each entry by the average of the two orders gives the anticommutators, and all of them stay in the symmetric half: $\{I,X\}=2X$, $\{\sigma_{3},\sigma_{1}\}=0$, $\{\sigma_{3},\sigma_{3}\}=\{I,I\}=2I$.

**Proof.** The average of the $(3,1)$ and $(1,3)$ entries of the table is $\tfrac12(J-J)=0$, and the other averages are the diagonal entries.

## The Table $SK$

**Theorem.** The products of a symmetric basis element with $J$ are

| $\cdot$ | $J$ |
|---|---|
| $I$ | $J$ |
| $\sigma_{3}$ | $\sigma_{1}$ |
| $\sigma_{1}$ | $-\sigma_{3}$ |

**Proof.** $J$ commutes with the scalars; $\sigma_{3}J=\sigma_{3}(i\sigma_{2})=\sigma_{1}$ and $\sigma_{1}J=-\sigma_{3}$ are the two-by-two products $\begin{pmatrix}0&1\\ -1&0\end{pmatrix}$ times the respective factor.

**Corollary.** Two of the three mixed products are symmetric and one is antisymmetric, so the mixed table does not stay in either half.

**Proof.** $\sigma_{3}J=\sigma_{1}$ and $\sigma_{1}J=-\sigma_{3}$ are symmetric, while $IJ=J$ is antisymmetric.

## The Table $KS$

**Theorem.** The products of $J$ with a symmetric basis element are

| $\cdot$ | $I$ | $\sigma_{3}$ | $\sigma_{1}$ |
|---|---|---|---|
| $J$ | $J$ | $-\sigma_{1}$ | $\sigma_{3}$ |

**Proof.** $J$ commutes with the scalars, and $J\sigma_{3}=-\sigma_{3}J=-\sigma_{1}$ with $J\sigma_{1}=-\sigma_{1}J=\sigma_{3}$.

**Corollary.** The two mixed tables differ by a sign in every entry: $J\sigma_{3}=-\sigma_{3}J$ and $J\sigma_{1}=-\sigma_{1}J$, while both equal $J$ at the identity.

**Proof.** Compare the two displays entry by entry.

**Corollary.** The mixed tables are related by the transpose, since $(SK)^{\mathsf T}=-KS$ for $S$ symmetric and $K$ antisymmetric.

**Proof.** $(SK)^{\mathsf T}=K^{\mathsf T}S^{\mathsf T}=-KS$, and the transpose of each basis element is itself.

## The Table $KK$

**Theorem.** The single product is

$$
J^{2}=-I .
$$

**Proof.** $\begin{pmatrix}0&1\\ -1&0\end{pmatrix}^{2}=\begin{pmatrix}-1&0\\ 0&-1\end{pmatrix}$.

**Corollary.** The one-dimensional antisymmetric half contains the scalar $-1$ in its square, so the algebra generated by $J$ alone is the complex numbers $\mathbb{R}\oplus\mathbb{R}J$ with $J^{2}=-1$.

**Proof.** The span of $I$ and $J$ is closed under products and is a two-dimensional real algebra with an element whose square is $-1$, hence isomorphic to $\mathbb{C}$.

**That subalgebra is the standard complex structure of the real plane.** Multiplication by $J$ is the rotation of angle $\pi/2$, so the complex numbers inside $M_2(\mathbb{R})$ are exactly the matrices of the form $aI+bJ$.

## The Four Tables Together

**The full table.** Reading the four blocks as one array of size $4\times4$ gives

| $\cdot$ | $I$ | $\sigma_{3}$ | $\sigma_{1}$ | $J$ |
|---|---|---|---|---|
| $I$ | $I$ | $\sigma_{3}$ | $\sigma_{1}$ | $J$ |
| $\sigma_{3}$ | $\sigma_{3}$ | $I$ | $J$ | $\sigma_{1}$ |
| $\sigma_{1}$ | $\sigma_{1}$ | $-J$ | $I$ | $-\sigma_{3}$ |
| $J$ | $J$ | $-\sigma_{1}$ | $\sigma_{3}$ | $-I$ |

**Proposition.** Of the sixteen entries, twelve lie in the symmetric half and four lie in the antisymmetric line; the four antisymmetric entries are $(\sigma_{3},\sigma_{1})$, $(\sigma_{1},\sigma_{3})$, $(I,J)$ and $(J,I)$.

**Proof.** Read the array; the antisymmetric entries are exactly the products of two elements one of which is $J$ with the identity, and the two off-diagonal products of $\sigma_{3}$ and $\sigma_{1}$.

**Corollary.** The antisymmetric entries of the table are exactly the products whose two factors have different symmetry or whose factors are the identity and $J$; the count of four matches $\dim\Lambda^{2}=1$ times four pairings.

**Proof.** The antisymmetric part of each product is computed by the rules of *The Symmetric and Antisymmetric Parts of a Product at $n=2$*, and the four listed entries are the only ones where the rule gives a nonzero result.

**Associativity on the table.** The four tables satisfy $(XY)Z=X(YZ)$ for all triples of basis elements, which is the check that the structure constants are those of an associative algebra and not only of a nonassociative one.

**Proof.** Each side is the product of three of the four matrices and the products of two-by-two matrices are associative; the tables are consistent with threefold products, for example $(JJ)J=-J=J(JJ)$ and $(\sigma_{3}J)\sigma_{1}=\sigma_{1}\sigma_{1}=I=\sigma_{3}(J\sigma_{1})=\sigma_{3}\sigma_{3}$.

## The Anticommutator and the Commutator Tables

**The anticommutator table on the symmetric half.** For the three symmetric basis elements,

$$
\{I,I\}=2I,\quad \{\sigma_{3},\sigma_{3}\}=\{\sigma_{1},\sigma_{1}\}=2I,\quad \{I,\sigma_{3}\}=2\sigma_{3},\quad \{I,\sigma_{1}\}=2\sigma_{1},\quad \{\sigma_{3},\sigma_{1}\}=0 .
$$

**Proof.** The products in both orders are read from the $SS$ table, where the only entries that change sign are those in the antisymmetric line, and those are the entries whose symmetrised value vanishes.

**The commutator table on the symmetric half.** The only nonzero commutator of two symmetric basis elements is $[\sigma_{3},\sigma_{1}]=2J$.

**Proof.** $[I,X]=0$ and $[\sigma_{3},\sigma_{1}]=\sigma_{3}\sigma_{1}-\sigma_{1}\sigma_{3}=J-(-J)=2J$.

**Corollary.** The bracket of two traceless symmetric basis elements is twice the antisymmetric unit, so on the traceless plane the bracket is a cross product followed by the identification of $\Lambda^{2}\mathbb{R}^{2}$ with $\mathbb{R}$.

**Proof.** The traceless plane has basis $\sigma_{3},\sigma_{1}$, the bracket of the two is $2J$, and $J$ spans the one-dimensional second exterior power; the constant $2$ is the scale of the identification.

## The Tables in the Biquaternion Language

**The corpus organises the same sixteen products differently.** In the biquaternion algebra the four general products are the products of two elements taken with or without the conjugation, and the two halves are the corners $\mathbb{B}_{st}$ rather than the symmetric and antisymmetric parts.

**The translation.** Under the identification of the biquaternion algebra with $M_2(\mathbb{C})$, the biquaternion conjugation corresponds to the conjugate transpose, so the four general products of *The Four General Products and Their Relations over the Biquaternion Algebra* correspond to the four tables of this article with the Hermitian and anti-Hermitian halves in place of the symmetric and antisymmetric ones.

**Proof.** Conjugation in the biquaternion algebra reverses the order of a product, and the conjugate transpose does the same, $(XY)^{*}=Y^{*}X^{*}$; the correspondence of the halves follows.

**Corollary.** The four tables of this article and the four tables of the biquaternion article are the same table seen in two bases, and the sign difference between the mixed tables is the statement that the conjugation is antilinear.

## Summary

In the basis $I,\sigma_{3},\sigma_{1},J$ the sixteen products fall into the $3\times3$ block $SS$, the column $SK$, the row $KS$ and the scalar $KK$. The $SS$ block has two entries, $\sigma_{3}\sigma_{1}=J$ and $\sigma_{1}\sigma_{3}=-J$, in the antisymmetric line, so the symmetric half is not closed under the plain product; the mixed tables differ by a sign in every entry and are exchanged by the transpose; and $J^{2}=-I$ makes the span of $I$ and $J$ a copy of the complex numbers inside the real matrices.

The symmetrised $SS$ table is closed and gives the anticommutator table $\{u,v\}=2\operatorname{tr}(uv)I$ on the traceless plane, while the commutator table has the single nonzero entry $[\sigma_{3},\sigma_{1}]=2J$. The four tables are the matrix form of the four general products of the biquaternion algebra under the correspondence that sends the conjugation to the conjugate transpose.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $I,\sigma_{3},\sigma_{1}$ | the symmetric basis of $\operatorname{Sym}_2(\mathbb{R})$ |
| $J$ | $i\sigma_{2}$, the antisymmetric unit |
| $SS$, $SK$, $KS$, $KK$ | the four blocks of the multiplication table |
| $\{X,Y\}$ | the anticommutator |
| $[X,Y]$ | the commutator |
| $\mathbb{B}$ | the biquaternion algebra |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for multiplication tables and structure constants of finite dimensional algebras.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2001), for the multiplication table of the Pauli matrices and the quaternion units.
- [The Symmetric and Antisymmetric Parts of a Product at $n=2$](the-symmetric-and-antisymmetric-parts-of-a-product-at-n-2.html), for the rules that produce these tables.
- [The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric at $n=2$](the-two-halves-over-r-symmetric-and-antisymmetric-at-n-2.html), for the two halves and their closure properties.
- [The Four General Products and Their Relations over the Biquaternion Algebra](the-four-general-products-and-their-relations-over-the-biquaternion-algebra.html), for the same four tables on the biquaternion side.
