# __The Length and the Two Ranks at $n=4$__

## Introduction

**The length of an operator on the matrix space is the rank of its coefficient matrix, it takes the five values $0,1,2,3,4$, four products always suffice, and the generic matrix has length four; the matrix rank of a single product takes only $0,1,2,4$ and never $3$, while the matrix rank of a sum of products takes all five values, and length and matrix rank are independent.**

Three facts are kept apart in this article, and the keeping apart is the point. The rank of a single product is restricted by the zero divisors of the biquaternion algebra. The rank of a general sum is not restricted, and an explicit operator of rank three is exhibited. And the length of an operator has no relation to its matrix rank: $E_{11}$ has length four and rank one, the identity has length one and rank four, and $\operatorname{diag}(1,2,3,4)$ has length three and rank four.

It assumes *The Two-Sided Operators and the Segre Cone at $n=4$* and *The One-Sided Operators at $n=4$*. The model at order two is *The Length and the Two Ranks at $n=2$*; the operator algebra is *$\operatorname{End}(M_4(\mathbb{C}))$ as an Algebra: the Regular Representation*.

## The Length

**Definition.** For $M\in M_4(\mathbb{C})$ the **length** $\ell(M)$ is the smallest number of two-sided products $T_{a,b}$ whose sum is $M$.

**Proposition.** $\ell(M)=\operatorname{rank}c(M)$, where $c(M)$ is the $4\times4$ coefficient matrix of $M$ in the basis $T_{\mu\nu}$, and $\ell$ takes the values $0,1,2,3,4$.

**Proof.** A sum of $k$ products has coefficient matrix a sum of $k$ rank-one matrices, of rank at most $k$; conversely a coefficient matrix of rank $r$ is a sum of $r$ rank-one matrices and each rank-one matrix is $c(T_{a,b})$ for suitable $a,b$. The rank of a $4\times4$ matrix is at most four.

**Corollary.** $\ell(M)=0$ exactly for $M=0$, and $\ell(M)=1$ exactly for the points of the Segre cone.

**Proof.** Rank zero is the zero matrix and rank one is the cone.

**Corollary.** $\ell(M)\le4$ for every operator, and the operators of length one are exactly those whose coefficient matrix is an outer product.

**Proof.** The rank bound and the criterion of the rank-one coefficient matrix.

## Four Products Suffice

**Theorem.** Every operator on the sixteen-dimensional matrix space is a sum of at most four two-sided products.

**Proof.** The coefficient matrix has rank at most four, and rank $r$ means a sum of $r$ rank-one matrices, each of which is a single product.

**Corollary.** The Segre cone generates the whole algebra in at most four steps, and the fourth step is necessary.

**Proof.** The length four is attained, for instance by $E_{11}$, as the next section shows.

**Corollary.** The algebra satisfies no polynomial identity of the form "every element is a sum of at most three products", in contrast with the products of three elements.

**Proof.** The counterexample of length four.

**The dimension count.** The set of operators of length at most $k$ is the image of the sum map from $k$ copies of the cone, of dimension at most $7k$; for $k=2$ this is $14<16$, so the operators of length two do not fill the space.

**Proof.** The cone has dimension seven, and the image of a map from a $14$-dimensional variety has dimension at most $14$.

**Corollary.** The operators of length three form a set of dimension at most $21$, which is the whole space, so the bound is not improved by the dimension count.

**Proof.** $21\ge16$.

## The Generic Length

**Proposition.** The operators of length less than four form a proper algebraic subset, so the generic operator has length four.

**Proof.** Length less than four is the vanishing of all the $4\times4$ minors of the coefficient matrix, which is a proper algebraic condition, since $\mathrm I_4$ has length one and $E_{11}$ has length four.

**Corollary.** A random operator has length four with probability one, and the length drops exactly on the determinantal varieties of the coefficient matrix.

**Proof.** The minors vanish on a set of measure zero.

**The strata.** The operators of length at most $k$ form the determinantal variety of the $4\times4$ coefficient matrices of rank at most $k$, of dimension $16-(4-k)^{2}$.

**Proof.** The classical formula for the dimension of the determinantal variety, in the sixteen-dimensional coefficient space.

**Corollary.** The strata have dimensions $7$, $12$ and $15$ for $k=1,2,3$: the set of length one is the Segre cone of dimension seven, and the set of length at most three is a hypersurface in the sixteen-dimensional space.

**Proof.** The formula at $k=1,2,3$ gives $16-9=7$, $16-4=12$ and $16-1=15$.

## The Rank of a Single Product

**Theorem.** For a single product $T_{a,b}$ the matrix rank is $\operatorname{rank}(a)\operatorname{rank}(b)$, where the rank of an element is its rank as a $2\times2$ matrix; hence the rank of a single product lies in $\{0,1,2,4\}$ and is never $3$.

**Proof.** $T_{a,b}$ is the linear map $X\mapsto aXb$; in the identification $\mathbb{B}\cong M_2(\mathbb{C})$ this is $X\mapsto aXb$, whose rank is $\operatorname{rank}(a)\operatorname{rank}(b)$ because the image is $a\,\mathbb{B}\,b$ and the two factors contribute independently. Each rank is $0,1$ or $2$, so the product is $0,1,2$ or $4$.

**Corollary.** A single product is invertible exactly when both factors are invertible, and then its rank is four.

**Proof.** The product of the ranks is four exactly when both are two.

**Corollary.** A single product of rank two exists: take $a$ a zero divisor of matrix rank one and $b$ invertible.

**Proof.** The rank formula, with $\operatorname{rank}(a)=1$ and $\operatorname{rank}(b)=2$.

**Corollary.** The value three is excluded for a single product but not for a sum, which is the content of the next section.

**Proof.** The rank formula and the example below.

## The Rank of a Sum

**Theorem.** The matrix rank of a sum of two-sided products takes all five values $0,1,2,3,4$.

**Proof.** The values $0,1,2,4$ occur for single products; the value three occurs for the explicit sum
$$
-T_{tt}-T_{tx}-T_{xt}-T_{yy}
=\begin{pmatrix}0&2&0&0\\-2&-2&0&0\\0&0&0&0\\0&0&0&-2\end{pmatrix},
$$
whose rows are $(0,2,0,0)$, $(-2,-2,0,0)$, $(0,0,0,0)$ and $(0,0,0,-2)$; the third row is zero and the other three are independent, so the rank is three.

**Corollary.** The rank three is not an obstruction of the algebra but a phenomenon of the sum: the four terms are single products of rank four, and their sum loses exactly one dimension.

**Proof.** Each $T_{\mu\nu}$ is a signed permutation of rank four; the sum has the displayed form.

**Corollary.** The operator of the theorem has length three, since its coefficient matrix is the displayed pattern of four nonzero entries of rank three.

**Proof.** The coefficient matrix of the sum is $-E_{11}-E_{12}-E_{21}-E_{33}$, whose rank is three.

**The warning.** A statement that a general sum of products has rank different from three is false. The restriction to the set $\{0,1,2,4\}$ is a statement about single products and about products of two zero divisors, not about sums.

**Proof.** The counterexample.

**The two zero divisors.** A product of two zero divisors of matrix rank one has matrix rank one, and the rank formula shows that no product of rank three can arise however the factors are chosen.

**Proof.** The product of the ranks.

## The Two Invariants Are Independent

**Proposition.** The length and the matrix rank are independent: all four combinations occur among the following three operators and their transposes.

| operator | matrix rank | length |
|---|---|---|
| $E_{11}$ | $1$ | $4$ |
| $\mathrm I_4$ | $4$ | $1$ |
| $\operatorname{diag}(1,2,3,4)$ | $4$ | $3$ |

**Proof.** $E_{11}$ has nonzero coefficients on all four values of the second index, so its coefficient matrix has rank four; the identity is $T_{tt}$, of length one; $\operatorname{diag}(1,2,3,4)$ has coefficient matrix of rank three, computed directly in the axis-free basis.

**Corollary.** No inequality relates the two invariants in either direction, and each is a complete invariant of a different structure: the matrix rank of the operator as an element, the length of the operator as a sum of products.

**Proof.** The table gives a counterexample to every monotone relation.

**Corollary.** $\ell(M)=1$ with matrix rank four for the identity, so the shortest operator is the one of largest rank; the length measures the complexity of the coefficient matrix, not the size of the image.

**Proof.** The table.

**The meaning.** The matrix rank is the dimension of the image of the operator acting on the matrix space; the length is the rank of its coefficient matrix in the two-sided basis. The first is a property of the map, the second a property of the coordinates.

**Proof.** The two definitions.

## Summary

The length of an operator is the rank of its coefficient matrix in the basis of two-sided products; it lies between zero and four, four products always suffice, and the generic operator has length four. The operators of length at most $k$ form the determinantal variety of the coefficient matrices of rank at most $k$.

The matrix rank of a single product is the product of the ranks of its two factors, so it lies in $\{0,1,2,4\}$ and is never three. The matrix rank of a sum is unrestricted, with the explicit sum $-T_{tt}-T_{tx}-T_{xt}-T_{yy}$ of rank three and length three.

The two invariants are independent: $E_{11}$ has rank one and length four, the identity has rank four and length one, and $\operatorname{diag}(1,2,3,4)$ has rank four and length three.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\ell(M)=\operatorname{rank}c(M)$ | the length |
| $c(M)$ | the coefficient matrix in the basis $T_{\mu\nu}$ |
| $\operatorname{rank}(a)$ | the rank of $a$ as a $2\times2$ matrix |
| $\{0,1,2,4\}$ | the ranks of a single product |
| $-T_{tt}-T_{tx}-T_{xt}-T_{yy}$ | the operator of rank three |

## Further Reading

- [The Two-Sided Operators and the Segre Cone at $n=4$](the-two-sided-operators-and-the-segre-cone-at-n-4.html), for the coefficient matrix and the cone.
- [The One-Sided Operators at $n=4$](the-one-sided-operators-at-n-4.html), for the two families and their products.
- [The Adjoints and the Polar Decomposition of an Operator at $n=4$](the-adjoints-and-the-polar-decomposition-of-an-operator-at-n-4.html), for the operator viewpoint.
- [The Length and the Two Ranks at $n=2$](the-length-and-the-two-ranks-at-n-2.html), for the case at order two.
- [The Two-Sided Operators and the Segre Cone at $n=2$](the-two-sided-operators-and-the-segre-cone-at-n-2.html), for the cone at order two.
