# __The Four Multiplication Tables: $SS$, $SK$, $KS$, $KK$__

## Introduction

**The four products of the halves are governed by one identity, $(XY)^{\mathsf T}=\epsilon\delta\,YX$ for $X$ in the $\epsilon$-half and $Y$ in the $\delta$-half, and every entry of every table is a consequence of it.**

The article proves the identity, derives from it the four tables: the table of the product, the table of the commutator, the table of the anticommutator and the table of the twisted products, each a $2\times2$ array of halves. It shows that the commutator lands in the half $-\epsilon\delta$ and the anticommutator in the half $+\epsilon\delta$, so the two operations exchange the tables, and it verifies all four tables by direct computation at $n=2,3,4,6$. It assumes *The Symmetric and Antisymmetric Parts of a Product* for the expansion of a single product and *The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric* for the closure rules. It defers the Jordan structure to *The Jordan Algebra $\operatorname{Sym}_n$*, the Lie structure to *The Lie Algebra $\operatorname{Skew}_n\cong\mathfrak{so}(n)$*, and the operator version to *The Symmetric and Antisymmetric Parts of the Operator Space*.

## The Master Identity

**The transpose of a product of two homogeneous elements is the product in the other order times the product of the signs.** For $X^{\mathsf T}=\epsilon X$ and $Y^{\mathsf T}=\delta Y$ with $\epsilon,\delta=\pm1$,

$$
(XY)^{\mathsf T}=Y^{\mathsf T}X^{\mathsf T}=\delta\epsilon\,YX .
$$

Write $\epsilon\delta$ for the product of the two signs. The identity was verified for all four combinations at $n=2,3,4,6$ with random elements of the two halves, and it holds for every $n$ because it is the multiplicativity of the transpose.

**The identity splits a product into a fixed and an anti-fixed part at once.** Adding and subtracting the identity from $XY$ itself,

$$
XY+\epsilon\delta\,YX\in\operatorname{Sym}_n,\qquad XY-\epsilon\delta\,YX\in\operatorname{Skew}_n ,
$$

since the first is fixed by the transpose and the second is negated by it. Both statements were checked for all four combinations at $n=2,3,4,6$. So the parity of a product is not a property of $XY$ alone: it is a property of the two combinations $XY\pm\epsilon\delta\,YX$, and the ordinary product is the average of the two.

**When the signs agree the two combinations are the anticommutator and the commutator; when they differ they are exchanged.** For $\epsilon\delta=+1$ the fixed combination is $XY+YX$ and the anti-fixed one is $XY-YX$; for $\epsilon\delta=-1$ the fixed combination is $XY-YX$ and the anti-fixed one is $XY+YX$. Hence

$$
\epsilon\delta=+1:\ \{X,Y\}\in\operatorname{Sym}_n,\ [X,Y]\in\operatorname{Skew}_n;\qquad
\epsilon\delta=-1:\ [X,Y]\in\operatorname{Sym}_n,\ \{X,Y\}\in\operatorname{Skew}_n .
$$

## The Table of the Product

**Each product of two halves gives one entry in each half.** Combining the identity with the expansion of *The Symmetric and Antisymmetric Parts of a Product*,

$$
SS':\quad \pi_{+}=S\circ S',\ \pi_{-}=\tfrac12[S,S'],\qquad
SK':\quad \pi_{+}=\tfrac12[S,K'],\ \pi_{-}=\tfrac12\{S,K'\},
$$

$$
KS':\quad \pi_{+}=\tfrac12[K,S'],\ \pi_{-}=\tfrac12\{K,S'\},\qquad
KK':\quad \pi_{+}=K\circ K',\ \pi_{-}=\tfrac12[K,K'] .
$$

So the table of the product, read as four entries each carrying two halves, is

| product | symmetric part | antisymmetric part |
|---|---|---|
| $SS'$ | $S\circ S'$ | $\tfrac12[S,S']$ |
| $SK'$ | $\tfrac12[S,K']$ | $\tfrac12\{S,K'\}$ |
| $KS'$ | $\tfrac12[K,S']$ | $\tfrac12\{K,S'\}$ |
| $KK'$ | $K\circ K'$ | $\tfrac12[K,K']$ |

**The rule of the table is the sign product.** A product whose two factors have the same sign contributes its symmetric part through the Jordan product and its antisymmetric part through the bracket; a product whose factors have opposite signs contributes the other way round. The sign product of the two factors is the same for $SS'$ and $KK'$ and the same for $SK'$ and $KS'$, which is why the table has two rows of one kind and two of the other.

**The table is symmetric under exchanging the two factors up to the transposition of the entry.** Since $(XY)^{\mathsf T}=\epsilon\delta\,YX$, exchanging $X$ and $Y$ multiplies the antisymmetric part by $\epsilon\delta$ and leaves the symmetric part alone. So the $SK$ and $KS$ entries differ by the sign and the $SS$, $KK$ entries are symmetric in their arguments up to a transpose.

## The Table of the Commutator

**The commutator lands in the half $-\epsilon\delta$.** From the master identity,

$$
(XY-YX)^{\mathsf T}=\epsilon\delta\,YX-XY=-\epsilon\delta\,(XY-YX),
$$

so $[X,Y]\in\operatorname{Anti}\sigma$ when $\epsilon\delta=+1$ and $[X,Y]\in\operatorname{Fix}\sigma$ when $\epsilon\delta=-1$. The table is therefore

| commutator | $\operatorname{Sym}$ | $\operatorname{Skew}$ |
|---|---|---|
| $\operatorname{Sym}$ | $\operatorname{Skew}$ | $\operatorname{Sym}$ |
| $\operatorname{Skew}$ | $\operatorname{Sym}$ | $\operatorname{Skew}$ |

with the entries

$$
[S,S']\in\operatorname{Skew}_n,\qquad [S,K']\in\operatorname{Sym}_n,\qquad [K,S']\in\operatorname{Sym}_n,\qquad [K,K']\in\operatorname{Skew}_n .
$$

All four inclusions were verified at $n=2,3,4,6$ on random elements.

**The commutator table is the statement that the antisymmetric half is a Lie algebra and the symmetric half is a module over it.** The two diagonal entries put $[S,S']$ and $[K,K']$ in the antisymmetric half, so $\operatorname{Skew}_n$ is closed and $\operatorname{Sym}_n$ is not. The two off-diagonal entries put the mixed brackets in the symmetric half, which is the closure rule $[\operatorname{Skew}_n,\operatorname{Sym}_n]\subseteq\operatorname{Sym}_n$ that makes the pair reductive.

**The commutator of two elements of the algebra is a sum of four brackets, two in each half.** For $A=S+K$ and $B=S'+K'$,

$$
[A,B]=[S,S']+[K,K']+[S,K']+[K,S'],
$$

with the first two in $\operatorname{Skew}_n$ and the last two in $\operatorname{Sym}_n$. So the commutator is graded by the same parity, and the two halves of the commutator are read from the two diagonals and the two off-diagonals of the table.

## The Table of the Anticommutator

**The anticommutator lands in the half $+\epsilon\delta$, so its table is the other one.** From the master identity,

$$
(XY+YX)^{\mathsf T}=\epsilon\delta\,YX+XY=+\epsilon\delta\,(XY+YX),
$$

hence the anticommutator is fixed when $\epsilon\delta=+1$ and anti-fixed when $\epsilon\delta=-1$:

| anticommutator | $\operatorname{Sym}$ | $\operatorname{Skew}$ |
|---|---|---|
| $\operatorname{Sym}$ | $\operatorname{Sym}$ | $\operatorname{Skew}$ |
| $\operatorname{Skew}$ | $\operatorname{Skew}$ | $\operatorname{Sym}$ |

with

$$
\{S,S'\}\in\operatorname{Sym}_n,\qquad \{S,K'\}\in\operatorname{Skew}_n,\qquad \{K,S'\}\in\operatorname{Skew}_n,\qquad \{K,K'\}\in\operatorname{Sym}_n .
$$

Again all four were verified on random elements at $n=2,3,4,6$.

**The two tables are exchanged by the sign and coincide at $n=1$.** The commutator table sends $(\epsilon,\delta)$ to $-\epsilon\delta$ and the anticommutator table to $+\epsilon\delta$; the two agree only when $-\epsilon\delta=+\epsilon\delta$, which never happens. The tables are therefore genuinely different, and the difference is the sign that separates a Lie algebra from a Jordan algebra.

**The product is the average of the two tables, and the transpose is the difference.** For any two elements,

$$
XY=\tfrac12\{X,Y\}+\tfrac12[X,Y],\qquad (XY)^{\mathsf T}=\tfrac12\{X,Y\}-\tfrac12[X,Y],
$$

so the four entries of the product table are the averages of the entries of the other two, and the transpose is their difference. The three tables are one table read three times.

## The Twisted Products and the Two Structures

**The twisted products are the maps that land in a definite half.** For $X$ in the $\epsilon$-half and $Y$ in the $\delta$-half put

$$
X\star Y=\tfrac12\big(XY+\epsilon\delta\,YX\big)\in\operatorname{Fix}\sigma,\qquad
X\wedge Y=\tfrac12\big(XY-\epsilon\delta\,YX\big)\in\operatorname{Anti}\sigma .
$$

Then $\star$ is commutative on pairs of the same half and $\wedge$ is the bracket there, while on pairs of opposite halves $\star$ is the bracket and $\wedge$ is the anticommutator. So the two maps $\star$ and $\wedge$ are the entries of the tables with the signs absorbed.

**The Jordan structure lives in $\star$ and the Lie structure in $\wedge$.** On the symmetric half, $\star$ is the Jordan product $S\circ S'$ and $\wedge$ is $\tfrac12[S,S']$; on the antisymmetric half, $\star$ is $K\circ K'$ and $\wedge$ is $\tfrac12[K,K']$. So each half carries both products, one of which is a Jordan product and the other a Lie bracket, and the two halves differ by which of them is closed.

**The mixed entries make the symmetric half a module and the antisymmetric half an operator space.** On pairs of opposite halves, $\star$ gives $\tfrac12[S,K']\in\operatorname{Sym}_n$, which is the action of $\mathfrak{so}(n)$ on $\operatorname{Sym}_n$, and $\wedge$ gives $\tfrac12\{S,K'\}\in\operatorname{Skew}_n$, which is the corresponding infinitesimal strain. The two mixed entries of the four tables are therefore the two sides of the same operator.

## The Case $n=2$

**At $n=2$ the four tables have one-dimensional entries of the second kind.** With $\operatorname{Sym}_2$ three-dimensional and $\operatorname{Skew}_2$ one-dimensional, the $SS$ entry is a three-dimensional symmetric output plus a one-dimensional skew output, and the $KK$ entry is the reverse:

$$
K\circ K'=-\theta\theta'\,\mathrm{I},\qquad [K,K']=0 ,
$$

the second because $\operatorname{Skew}_2$ is abelian. So the $KK$ row of the product table has a scalar symmetric part and no antisymmetric part at all.

**The mixed rows are computed by the Pauli brackets.** For $S=a\mathrm{I}+b\sigma_1+c\sigma_3$ and $K'=\theta'J$,

$$
[S,K']=2\theta'(b\sigma_3-c\sigma_1)\in\operatorname{Sym}_2,\qquad \{S,K'\}=2\theta'a\,J\in\operatorname{Skew}_2 ,
$$

with $a$ the coefficient of $\mathrm{I}$, so the mixed entry of the product table is $\theta'(b\sigma_3-c\sigma_1)+\theta'aJ$, a sum of one vector in each half. Both identities were verified numerically, and the second shows that the anticommutator of a symmetric matrix with $J$ sees only the scalar part of the symmetric matrix.

**The biquaternion reading names the four entries.** The idempotents $\tilde\Pi_\pm$ are symmetric and the corners $\mathbb{B}_{+-}$, $\mathbb{B}_{-+}$ are mixed, so a product of two corner elements uses the $KS$ and $SK$ rows, and a product of two idempotents uses the $SS$ row. The companion nilpotents $\vec\Upsilon_{+-}$ and $\vec\Upsilon_{-+}$ satisfy $\vec\Upsilon_{-+}=\vec\Upsilon_{+-}^{*}$ and $\vec\Upsilon_{+-}\vec\Upsilon_{-+}=\tilde\Pi_+$, which is a $KS$ product whose two halves are the idempotent and the bracket; the normalisation is the statement that one of the two halves is fixed by the gauge.

## Summary

The master identity $(XY)^{\mathsf T}=\epsilon\delta\,YX$ for homogeneous $X$ and $Y$ produces every entry of the four tables. The product table has $SS'=S\circ S'+\tfrac12[S,S']$, $SK'=\tfrac12[S,K']+\tfrac12\{S,K'\}$, $KS'=\tfrac12[K,S']+\tfrac12\{K,S'\}$ and $KK'=K\circ K'+\tfrac12[K,K']$. The commutator lands in the half $-\epsilon\delta$, so $[S,S']$ and $[K,K']$ are antisymmetric and $[S,K']$, $[K,S']$ symmetric; the anticommutator lands in the half $+\epsilon\delta$, with the signs reversed. The twisted products $X\star Y$ and $X\wedge Y$ absorb the signs and carry the Jordan structure and the Lie structure on each half and the module structure on the mixed pairs.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\epsilon,\delta$ | the signs of the two homogeneous factors, $+1$ for $\operatorname{Sym}$, $-1$ for $\operatorname{Skew}$ |
| $(XY)^{\mathsf T}=\epsilon\delta\,YX$ | the master identity of the four tables |
| $X\star Y=\tfrac12(XY+\epsilon\delta\,YX)$ | the twisted product, landing in $\operatorname{Fix}\sigma$ |
| $X\wedge Y=\tfrac12(XY-\epsilon\delta\,YX)$ | the twisted bracket, landing in $\operatorname{Anti}\sigma$ |
| $S\circ S'$, $K\circ K'$ | the Jordan products of the two halves |
| $[S,K']\in\operatorname{Sym}_n$, $\{S,K'\}\in\operatorname{Skew}_n$ | the two mixed entries |
| $\operatorname{Fix}\sigma,\operatorname{Anti}\sigma$ | the two halves of the involution |

## Further Reading

- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the graded products of a Peirce decomposition and the sign rules.
- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (AMS, 1968), for the Jordan product as the symmetric combination of a product.
- James E. Humphreys, *Introduction to Lie Algebras and Representation Theory* (Springer, 1972), for the bracket as the antisymmetric combination and the module structure.
- [The Symmetric and Antisymmetric Parts of a Product](the-symmetric-and-antisymmetric-parts-of-a-product.html), for the expansion that the tables refine.
- [The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric](the-two-halves-over-r-symmetric-and-antisymmetric.html), for the closure rules that the tables record.
- [Symmetric Pairs and Cartan Pairs: the Reductivity Criterion](symmetric-pairs-and-cartan-pairs-the-reductivity-criterion.html), for the module property of the mixed entries.
