# __The Four Multiplication Tables: $SS$, $SK$, $KS$, $KK$__

## Introduction

**Every product of two real matrices splits into two pieces, a symmetric one and an antisymmetric one, and each of the four pairings $SS$, $SK$, $KS$, $KK$ contributes to both pieces by different formulas; the table is the multiplication table of the two halves read in the two projections.**

The article computes the four tables, states which piece of each product is a commutator and which an anticommutator, and identifies the two products that stay where they start: the square of an antisymmetric matrix is symmetric and negative semidefinite, and the square of a symmetric matrix keeps a symmetric part and an antisymmetric part. It assumes *The Symmetric and Antisymmetric Parts of a Product* for the two projection formulas, and it defers the algebra structure of the symmetric half to *The Jordan Algebra $\operatorname{Sym}_n(\mathbb{R})$* and the Lie structure of the antisymmetric half to *The Lie Algebra $\operatorname{Skew}_n\cong\mathfrak{so}(n)$*.

Throughout $n\ge2$, and $M_n=M_n(\mathbb{R})$. The projections are

$$
\pi_+(X)=\tfrac12(X+X^{\mathsf T}),\qquad \pi_-(X)=\tfrac12(X-X^{\mathsf T}),
$$

so that $X=\pi_+(X)+\pi_-(X)$, and the halves are $S=\operatorname{Sym}_n$ and $K=\operatorname{Skew}_n$.

## The Four Products

**The four tables are the four choices of two factors from the two halves.** Write an element of $S$ as $S$ and an element of $K$ as $K$, and read the product as the matrix product. The four products are

$$
SS',\qquad SK,\qquad KS,\qquad KK',
$$

where $S,S'\in\operatorname{Sym}_n$ and $K,K'\in\operatorname{Skew}_n$. Each is a general element of $M_n$, so each splits into its two projections, and the content of the section is the four pairs of formulas.

**The transposes of the four products are known.** Since $S^{\mathsf T}=S$ and $K^{\mathsf T}=-K$,

$$
(SS')^{\mathsf T}=S'S,\qquad (SK)^{\mathsf T}=-KS,\qquad (KS)^{\mathsf T}=-SK,\qquad (KK')^{\mathsf T}=K'K.
$$

So the product $SS'$ is symmetric exactly when the factors commute; the product $SK$ is symmetric exactly when $SK=-KS$; and $KK'$ is symmetric exactly when $K,K'$ anticommute.

**Consequence: the four tables are not four independent objects.** The third is the transpose of the second with a sign, so $KS$ contributes exactly what $SK$ contributes, read on the other factor. This is why the two halves over $\mathbb{R}$ carry three tables and not four, and why the two-sided operator of *The Symmetric and Antisymmetric Parts of a Product* is the natural way to write them.

## The Tables $SS$ and $KK$

**The product of two symmetric matrices splits as an anticommutator and a commutator.** With $S,S'\in\operatorname{Sym}_n$,

$$
SS'=\underbrace{\tfrac12(SS'+S'S)}_{\in\operatorname{Sym}_n}+\underbrace{\tfrac12(SS'-S'S)}_{\in\operatorname{Skew}_n}.
$$

*Proof.* The first summand equals its transpose, since $(SS'+S'S)^{\mathsf T}=S'S+SS'$. The second changes sign, since $(SS'-S'S)^{\mathsf T}=S'S-SS'$. Both are nonzero in general, so $SS\subseteq S\oplus K$ and the two projections are the anticommutator and the commutator.

**The product of two antisymmetric matrices splits the other way around.** With $K,K'\in\operatorname{Skew}_n$,

$$
KK'=\underbrace{\tfrac12(KK'+K'K)}_{\in\operatorname{Sym}_n}+\underbrace{\tfrac12(KK'-K'K)}_{\in\operatorname{Skew}_n},
$$

by the same computation with a sign: $(KK'+K'K)^{\mathsf T}=K'^{\mathsf T}K^{\mathsf T}+K^{\mathsf T}K'^{\mathsf T}=K'K+KK'$, and the difference is antisymmetric. Measured on $100$ random pairs at $n=2,3,4$, the symmetric part is symmetric in every case and the antisymmetric part antisymmetric in every case.

**The structure of the two formulas is identical and the meaning is different.** In $SS'$ the symmetric part is the anticommutator of two symmetric matrices and the antisymmetric part is their commutator; in $KK'$ the same two words appear with the same roles. What changes is the sign of the square: $S^{2}$ is symmetric and positive semidefinite, while $K^{2}$ is symmetric and negative semidefinite.

**The square of an antisymmetric matrix is symmetric and negative semidefinite.** For $K\in\operatorname{Skew}_n$,

$$
(K^{2})^{\mathsf T}=(K^{\mathsf T})^{2}=(-K)^{2}=K^{2},\qquad K^{2}=-KK^{\mathsf T},
$$

and $-KK^{\mathsf T}$ is negative semidefinite with kernel $\ker K$. So the map $K\mapsto K^{2}$ leaves the antisymmetric half and lands in the closed cone of the symmetric half. Measured on $100$ random antisymmetric matrices at each of $n=2,3,4$, all $300$ squares were symmetric and negative semidefinite.

**Consequence: $KK$ is not closed in $K$ but its square is closed in $S$.** The product $KK'$ has an antisymmetric part in general, and that part is the commutator $\tfrac12[K,K']$; the square has no antisymmetric part at all. So the antisymmetric half is closed under the square only up to the bracket, and the bracket of two antisymmetric matrices is again antisymmetric, as *The Lie Algebra $\operatorname{Skew}_n\cong\mathfrak{so}(n)$* records.

## The Tables $SK$ and $KS$

**The mixed product splits by an anticommutator and a commutator of the two different halves.** With $S\in\operatorname{Sym}_n$ and $K\in\operatorname{Skew}_n$,

$$
SK=\underbrace{\tfrac12(SK-KS)}_{\in\operatorname{Sym}_n}+\underbrace{\tfrac12(SK+KS)}_{\in\operatorname{Skew}_n},
$$

and the same formula for $KS$ with the two factors exchanged.

*Proof.* $(SK)^{\mathsf T}=-KS$, so the symmetric projection is $\tfrac12(SK-KS)$ and the antisymmetric projection is $\tfrac12(SK+KS)$. Each is checked by transposing: $(SK-KS)^{\mathsf T}=-KS+SK$, and $(SK+KS)^{\mathsf T}=-KS-SK$.

**The mixed table is the reason the two halves are not ideals of each other.** Neither $SK\subseteq S$ nor $SK\subseteq K$ holds, and the failure is measured by the two parts: $SK\in S$ exactly when $SK=KS$, that is when the factors commute, and $SK\in K$ exactly when $SK=-KS$, that is when they anticommute. Measured on $100$ random pairs at $n=2,3,4$, neither condition held in any case.

**The mixed product has no distinguished vanishing.** For $SS'$ the square is special; for $SK$ nothing is: both parts are nonzero for a generic pair, and their dimensions in the two halves are $1$ each per matrix-unit pair, in the sense that a single entry $S_{ij}K_{kl}$ contributes to both projections. So the table $SK$ is the one that mixes the two halves most completely.

## The Traces of the Four Tables

**The trace of a product sees only the like pairings.** For $S,S'\in\operatorname{Sym}_n$ and $K,K'\in\operatorname{Skew}_n$,

$$
\operatorname{tr}(SS')=\sum_{i,j}S_{ij}S'_{ij},\qquad \operatorname{tr}(KK')=-\sum_{i,j}K_{ij}K'_{ij},
$$

and $\operatorname{tr}(SK)=0$.

*Proof.* The first two are the identity $\operatorname{tr}(AB)=\sum_{i,j}A_{ij}B_{ji}$ with $B$ symmetric and $B$ antisymmetric. For the third, $\operatorname{tr}(SK)=\operatorname{tr}((SK)^{\mathsf T})=\operatorname{tr}(-KS)=-\operatorname{tr}(SK)$, so the number is zero.

**Consequence: the two halves are orthogonal for the trace form, and each is definite on itself.** The trace form is positive definite on $S$ and negative definite on $K$; the mixed pairings vanish. So the four tables have a diagonal trace form:

$$
\begin{pmatrix}\operatorname{tr}(SS')&\operatorname{tr}(SK)\\\operatorname{tr}(KS)&\operatorname{tr}(KK')\end{pmatrix}=\begin{pmatrix}\langle S,S'\rangle_{\mathrm{HS}}&0\\0&-\langle K,K'\rangle_{\mathrm{HS}}\end{pmatrix}.
$$

The block structure is the content of *The Two Halves as Orthogonal Complements for the Trace Form*, and it says that the four tables decouple completely as far as the invariant bilinear form is concerned.

## Which Products Stay Inside a Half

**Only two of the four products stay inside a half for all choices of factors, and both are squares.** $S^{2}\in S$ holds always, because $S^{2}=(S^{2})^{\mathsf T}$; $K^{2}\in S$ holds always, by the previous section; and $SS'\in S$, $KK'\in K$, $SK\in S\cup K$ fail for generic factors. So

$$
S\cdot S\subseteq S\oplus K,\qquad S\cdot K\subseteq S\oplus K,\qquad K\cdot K\subseteq S\oplus K,
$$

and the first two are equalities for $n\ge2$ while the third is an equality only for $n\ge3$: at $n=2$ the anti-Hermitian half is one-dimensional and abelian, so $[K,K']=0$ and $KK'$ stays in $S$.

**Consequence: the two halves are not subalgebras of $M_n$.** Neither is closed under the product of the algebra, so neither inherits an associative structure. Each inherits a different one: $S$ is closed under the anticommutator and $K$ under the commutator, which is the content of *The Two Halves: Symmetric and Antisymmetric*.

**The commutator and the anticommutator are exchanged by the two tables.** In $SS'$ the commutator is the antisymmetric part; in $KK'$ the commutator is the antisymmetric part as well; in $SK$ the commutator is the symmetric part. So the answer to the question "which product is the bracket" depends on the pair of halves, and the mixed table is the one that reverses the answer.

## The Case $n=2$

**At $n=2$ the four tables are explicit.** Write $S=\begin{pmatrix}a&b\\ b&c\end{pmatrix}$ and $K=\begin{pmatrix}0&d\\ -d&0\end{pmatrix}$. Then

$$
SK=\begin{pmatrix}-bd&ad\\ -cd&bd\end{pmatrix},\qquad \pi_+(SK)=\begin{pmatrix}-bd&\tfrac12(ad-cd)\\ \tfrac12(ad-cd)&bd\end{pmatrix},\qquad \pi_-(SK)=\begin{pmatrix}0&\tfrac12(ad+cd)\\ -\tfrac12(ad+cd)&0\end{pmatrix},
$$

and $K^{2}=-d^{2}\mathrm{I}$, which is symmetric and negative semidefinite for every $d$.

**The two-dimensional case shows the failure of closure in one line.** $SK\in S$ would need $ad=cd$, that is $d(a-c)=0$, which fails for $d\ne0$ and $a\ne c$; $SK\in K$ would need $ad=-cd$, that is $d(a+c)=0$, which fails for $d\ne0$ and $a\ne-c$. So both inclusions fail on an open set, and the two failures are independent.

**The trace identity is visible in the entries.** $\operatorname{tr}(SS')=aa'+2bb'+cc'$ and $\operatorname{tr}(KK')=-2dd'$, so the two traces are the Hilbert–Schmidt squares with the sign of the half, and $\operatorname{tr}(SK)=-bd+bd=0$.

## Summary

The four tables of the two halves of $M_n(\mathbb{R})$ are the products $SS'$, $SK$, $KS$ and $KK'$, and each splits into a symmetric part and an antisymmetric part. In $SS'$ the symmetric part is the anticommutator and the antisymmetric part the commutator; in $KK'$ the same two formulas hold, with $K^{2}=-KK^{\mathsf T}$ symmetric and negative semidefinite, so the square of an antisymmetric matrix leaves the antisymmetric half and lands in the closed cone of the symmetric half; in the mixed product $SK$ the symmetric part is $\tfrac12(SK-KS)$ and the antisymmetric part $\tfrac12(SK+KS)$, so the bracket appears in the symmetric half. The trace form sees only the like pairings, is positive definite on $S$, negative definite on $K$ and vanishes on the mixed pairings, so the four tables decouple. None of the three tables stays inside a half, so neither half is a subalgebra of $M_n$; each carries its own product, the anticommutator on the symmetric half and the commutator on the antisymmetric half.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S,S'$ | elements of $\operatorname{Sym}_n$ |
| $K,K'$ | elements of $\operatorname{Skew}_n$ |
| $\pi_+,\pi_-$ | the symmetric and antisymmetric projections |
| $SS',SK,KS,KK'$ | the four table products |
| $\tfrac12(AB+BA)$ | the anticommutator, closed on $\operatorname{Sym}_n$ |
| $\tfrac12(AB-BA)$ | the commutator, closed on $\operatorname{Skew}_n$ |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the two-sided Peirce decomposition and the products between the corners.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge, 2013), for the symmetric and antisymmetric decompositions and the trace identities.
- [The Symmetric and Antisymmetric Parts of a Product](the-symmetric-and-antisymmetric-parts-of-a-product.html), for the projection formulas used here.
- [The Two Halves: Symmetric and Antisymmetric](the-two-halves-symmetric-and-antisymmetric-over-r.html), for the two halves and their products.
- [The Two Halves as Orthogonal Complements for the Trace Form](the-two-halves-as-orthogonal-complements-for-the-trace-form.html), for the block structure of the trace form.
