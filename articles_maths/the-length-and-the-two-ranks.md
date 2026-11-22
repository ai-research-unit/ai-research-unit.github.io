# __The Length and the Two Ranks__

## Introduction

**The subject.** Two numbers are attached to an operator and they are not the same number. The **length** is the least number of two-sided products whose sum the operator is; the **rank** is the dimension of its image. The length is read from the coefficients and the rank from the action, and neither determines the other. The article computes both, gives a witness for each combination that occurs, and shows that the two-sided operators are exactly the operators of length one.

**The order of the article.** The length is defined and identified with the rank of the coefficient array; the two-sided operators are then identified as the length-one stratum. The rank follows, the independence is proved by witnesses, and the strata of each invariant close the article.

**It assumes** *The Coefficients of a Two-Sided Operator: A Worked Computation*, *The Four Ranks of the Two-Sided Operators* and *$\operatorname{End}(\mathbb{B})$ as an Algebra: the Regular Representation*. **The row of the elements is** where a sum of products has a length in the algebra; here the same question is asked of an operator.

**The result in one line.** The length takes the values one to four and equals the rank of the coefficient array; the map rank takes the values zero to four; the products are the operators of length one, and every length occurs with every rank that is compatible with the dimension count.

**Boundaries.** The cone of the length-one operators is *The Two-Sided Operators and the Segre Cone*; the map rank alone is *The Four Ranks of the Two-Sided Operators*; the sums of two products read as an operator on the one-sided families are *The Adjoints and the Polar Decomposition of an Operator*.

## The Length

**Definition.** The **length** of an operator $T$ is the least $k$ for which
$$
T=\sum_{i=1}^{k}T_{a_i,b_i},
$$
and the length of the zero operator is zero.

**Theorem.** The length of an operator is the rank of its coefficient array, hence a number between one and four, and the value four is attained.

*Proof.* An operator is a sum of products exactly when its coefficient array is a sum of rank-one arrays, because the coordinates of $T_{a,b}$ are the products $a_\mu b_\nu$. The least number of rank-one arrays summing to an array is the rank of the array as a map of a four-dimensional space into itself, whence the bound four and the attainment.

**Corollary.** The operators of length one are exactly the two-sided operators.

*Proof.* A length-one operator is a single product; a product has a rank-one array; and conversely a rank-one array is the outer product of two nonzero vectors and defines a product.

**Corollary.** The operators of length at most $k$ form the determinantal variety of the arrays of rank at most $k$, of complex dimension $8k-k^{2}$; the variety of length at most one has dimension seven.

*Proof.* The identification of the length with the array rank, and the dimension formula for the determinantal variety.

**The reading.** The length measures a decomposition, not an action. It counts how many products are needed, and the answer is the rank of the array of coefficients, a quantity that knows nothing about the algebra's product beyond the basis.

## The Rank

**Definition.** The **rank** of an operator is the dimension of its image, and the **nullity** is the dimension of its kernel.

**Theorem.** The rank of an operator takes each of the values $0,1,2,3,4$ and satisfies the rank-nullity identity $\operatorname{rank}T+\dim\ker T=4$.

*Proof.* The image is a subspace of a four-dimensional space; a linear map with an image of any prescribed dimension exists, since the sixteen basis operators span all the maps; the identity is the dimension theorem of linear algebra.

**Corollary.** The operators of rank four are the invertible ones; the operators of rank zero are the zero operator; the intermediate ranks are carried by proper determinantal varieties.

*Proof.* A bijection of a four-dimensional space has rank four, and conversely.

**Corollary.** A two-sided operator has rank four, two, one or zero, and never three.

*Proof.* The rank of a two-sided operator is $\operatorname{rank}L_a\operatorname{rank}R_b/4$, and each one-sided rank is four, two or zero, so the values are four, two, one and zero. The value one occurs exactly when both parameters are degenerate, since $\operatorname{rank}L_a=2r(a)$ with $r$ the rank of the element as a map of the two-dimensional spinor, and then the image of the composite has dimension $r(a)r(b)=1$.

**The reading.** The rank measures the action. It counts dimensions in the image, and the answer depends on the parameters only through the vanishing of their norms. The two invariants therefore look at different objects: one at the coefficient array, the other at the map.

## The Independence

**Theorem.** The length and the rank are independent. The witnesses are: length one with rank four, the identity; length one with rank two, a product with one degenerate parameter; length two with rank four, $T_{e_t,e_t}+2T_{\vec e_x,\vec e_x}$; length three with rank three, $T_{e_t,e_t}+2T_{\vec e_x,\vec e_x}+3T_{\vec e_y,\vec e_y}$; length four with rank four, $\sum_{\mu=0}^{3}(2^{\mu}+1)T_{e_\mu,e_\mu}$; length four with rank one, $X\mapsto\mathrm{Sc}(X)e_t$.

*Proof.* The arrays of the last four operators are diagonal with two, three, four and four distinct nonzero entries, so their ranks as arrays are two, three, four and four. The map ranks are computed directly from the four images of the basis: the identity is a bijection, a product with a degenerate parameter has rank two, the two-entry and the four-entry sums are bijections, the three-entry sum has a one-dimensional kernel spanned by the fourth basis element, and the scalar map has a three-dimensional kernel.

**Corollary.** No inequality between the two invariants holds beyond the trivial bounds $1\le\text{length}\le4$ and $0\le\text{rank}\le4$.

*Proof.* The witnesses give length four with rank four and length four with rank one, so the length does not bound the rank from above; the identity gives length one with rank four, so it does not bound it from below either.

**Corollary.** The operators of rank one and length one do not exist, and the shortest witness of a rank-one operator has length four.

*Proof.* A length-one operator is a product, and a product of two nonzero parameters has rank four, two or one. That the scalar map is not a product follows from its values: a product sending $e_t$ to a multiple of $e_t$ has its second parameter proportional to the inverse of the first, and its value at $\vec e_x$ is then a conjugate of $\vec e_x$, of zero scalar part, hence never a multiple of $e_t$.

**The reading.** The two invariants are orthogonal pieces of information. The length says how the operator is built from the two sides; the rank says what it does to the space. A reader who knows one knows nothing about the other beyond the crude bounds.

## The Strata

**Proposition.** The strata of the length are the determinantal varieties of the coefficient array, nested as $\{0\}\subset D_1\subset D_2\subset D_3\subset D_4$, with complex dimensions $0,7,12,15,16$.

*Proof.* The dimension formula at $k=1,2,3,4$, and the inclusion of the arrays of rank at most $k$ in those of rank at most $k+1$.

**Corollary.** The two-sided operators are the stratum $D_1$: the cone of the products together with the zero operator.

*Proof.* $D_1$ is the set of the operators of length at most one, and the operators of length one are the products.

**Proposition.** The strata of the rank are the determinantal varieties of the operator as a map, with the same dimensions, nested in the same way.

*Proof.* The same dimension formula applied to the map instead of the array.

**Corollary.** The two stratifications have the same dimensions and are different stratifications: the length-one stratum is the cone of the products and the rank-one stratum is the variety of the maps onto a line, and the two meet only at the origin.

*Proof.* The rank-one stratum consists of the maps whose image is a line; a nonzero product has rank four, two or one, and it has rank one exactly when both parameters are degenerate.

**The reading.** Two nested families of varieties, of the same dimensions, cut by different conditions. The coincidence of the dimensions is the coincidence of the four and four of the two sides; the difference of the conditions is the difference between building an operator and acting with it.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| length $T$ | the least number of products summing to $T$ |
| length $=$ array rank | the identification, values one to four |
| $D_k$, dimension $8k-k^{2}$ | the operators of length at most $k$ |
| $\operatorname{rank}T$ | the dimension of the image, values zero to four |
| $T_{e_t,e_t}$ | length one, rank four |
| $X\mapsto\mathrm{Sc}(X)e_t$ | rank one, length four |

## Further Reading

- [The Coefficients of a Two-Sided Operator: A Worked Computation](the-coefficients-of-a-two-sided-operator-a-worked-computation.html), for the array and its rank-one test.
- [The Four Ranks of the Two-Sided Operators](the-four-ranks-of-the-two-sided-operators.html), for the rank of a product.
- [The Two-Sided Operators and the Segre Cone](the-two-sided-operators-and-the-segre-cone.html), for the length-one stratum.
- [The Adjoints and the Polar Decomposition of an Operator](the-adjoints-and-the-polar-decomposition-of-an-operator.html), for a second reading of the same sixteen coefficients.
- [$\operatorname{End}(\mathbb{B})$ as an Algebra: the Regular Representation](end-b-as-an-algebra-the-regular-representation.html), for the basis against which the coefficients are read.
