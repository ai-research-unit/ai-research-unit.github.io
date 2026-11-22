# __The Four Ranks of the Two-Sided Operators__

## Introduction

**The subject.** A two-sided operator is a linear map of the algebra, and it has a rank in the sense of linear maps, distinct from the tensor rank of its coefficients. The article computes the map rank. On the sector where both parameters are invertible the rank is four, and at the vertex it is zero; the intermediate values appear only on the products of degenerate parameters, and they never appear on the cone of invertible pairs. The map rank therefore takes exactly four values, four, two, one and zero, and never the value three. It stratifies the operator space in the coarsest possible way, and the article explains the coarseness by the scarcity of the degenerate parameters: they fill only a hypersurface of the algebra.

**The order of the article.** The rank of a product comes first, then the strata on the cone, then the same count for the one-sided families. The general order follows, and the failure of the rank to separate points closes the article.

**It assumes** *The Two-Sided Operators and the Segre Cone*, *The Left Ideals and the Image of a Left Multiplication* and *N-Regularity and N-Degeneracy in the Biquaternion Algebra*. **The row of the elements is** where invertibility is decided by the norm; here the same decision is read as the rank of an operator.

**The result in one line.** The rank of a two-sided operator takes the value four on the invertible pairs, two on the products with exactly one degenerate factor, one on the products of two degenerate factors, and zero at the vertex; the value three never occurs.

**Boundaries.** The rank of the coefficient tensor is *The Length and the Two Ranks*; the images of a one-sided operator are *The Left Ideals and the Image of a Left Multiplication*; the strata read by the spectrum are *The Spin-Zero Carrier and the Rank Strata*.

## The Rank of a Product

**Definition.** The **rank** of an operator is the dimension of its image.

**Theorem.** For every pair of parameters
$$
\operatorname{rank}T_{a,b}=\frac{\operatorname{rank}L_a\cdot\operatorname{rank}R_b}{4},
$$
so the rank of a two-sided operator takes the four values of the table.

| case | rank |
|---|---|
| both parameters invertible | $4$ |
| exactly one parameter degenerate | $2$ |
| both parameters degenerate | $1$ |
| a parameter zero | $0$ |

*Proof.* Write $\mathbb{B}=\operatorname{End}(S)$ with $S$ of dimension two, and let $r(a)$ be the rank of $a$ as a map of $S$, so that $r(a)\in\{0,1,2\}$ and $\operatorname{rank}L_a=2r(a)$, since the image of $L_a$ consists of the maps into the image of $a$. The image of $T_{a,b}$ consists of the composites $aXb$, which vanish on the kernel of $b$ and take their values in the image of $a$; the space of such maps has dimension $r(a)r(b)$. Hence $\operatorname{rank}T_{a,b}=r(a)r(b)=\operatorname{rank}L_a\operatorname{rank}R_b/4$, and $r(a)$ is two, one or zero according as $a$ is invertible, a nonzero zero divisor or zero.

**Corollary.** The rank of $T_{a,b}$ is zero exactly at the vertex of the cone.

*Proof.* The operator is zero exactly when a parameter is zero.

**Corollary.** The rank of a product is a function of the pair of parameters through the two norms alone.

*Proof.* The four cases of the theorem are distinguished by the vanishing of the two norms, and nothing else enters.

**The reading.** The rank of a two-sided operator carries one bit of information about each parameter: whether it is invertible. All the continuous data of the parameters, their spectra and their coordinates, are invisible to the rank. This is the sharpest contrast with the general row, where a product can carry every rank from zero to four and the rank moves with the geometry of the two factors.

## The Four Strata

**Definition.** The **rank strata** are the level sets of the rank on the operator space.

**Theorem.** On the cone of the products the rank strata are four, of complex dimensions seven, six, five and zero: the products of two invertible parameters, of rank four and opening the cone; the products with exactly one degenerate factor, of rank two; the products of two degenerate factors, of rank one; and the vertex.

*Proof.* The map from the pairs of parameters to the cone has one-dimensional fibres, the simultaneous scaling, so the image of a set of dimension $d$ has dimension $d-1$. The pairs of two invertible parameters form an open set of dimension $4+4=8$, of image dimension seven; the pairs with exactly one degenerate factor form a set of dimension $4+3=7$, of image dimension six; the pairs of two degenerate parameters form a set of dimension $3+3=6$, of image dimension five; and the pair of two zeros is a point, of image dimension zero. The ranks are read from the table.

**Corollary.** A product of two nonzero parameters never has rank three, and its rank is four when both are invertible, two when exactly one is degenerate and one when both are.

*Proof.* The theorem, whose table has four rows, giving the ranks four, two, one and zero.

**Corollary.** On the whole operator space the rank takes all five values, the determinantal variety of rank at most $k$ having complex dimension $8k-k^{2}$; the cone meets the variety of rank at most two in a proper subvariety of dimension six, one at most three. The cone is not contained in either, since it carries the identity of rank four.

*Proof.* Put $n=4$ in the dimension formula: seven, twelve, fifteen, sixteen. The cone has dimension seven, and a product has rank one exactly when both parameters are degenerate by the theorem, so the rank-one part of the cone is the image of the pairs of degenerate parameters, of dimension $3+3-1=5$, and the rank-two part adds the image of a degenerate with an arbitrary parameter, of dimension $3+4-1=6$.

**The reading.** Four strata on the cone and five on the space, and the one value the cone misses is three. The difference between the two counts is exactly the degenerate parameters, and the briefness of the list is the scarcity of the degenerate elements: an algebra in which the degenerate elements fill only a hypersurface of the parameters has only one value of the rank that the products cannot reach.

## The One-Sided Families

**Proposition.** The rank of a left multiplication is four at an invertible parameter, two at a degenerate one, and zero at the origin.

*Proof.* The image of $L_a$ is the left ideal generated by $a$, and the left ideals have dimensions four, two and zero.

**Corollary.** The rank stratifies each one-sided family by the same rule as the cone, and the two families have the same three strata.

*Proof.* The computation for the left family, and the same computation for the right family, whose images are the right ideals.

**Corollary.** The rank of a one-sided operator and the rank of the two-sided operator it generates agree at every pair with an invertible partner.

*Proof.* Multiplying by an invertible operator preserves the rank.

**The reading.** The one-sided and the two-sided rows give the same stratification, because the rank is insensitive to composition with invertible factors. The one-sided families are four-dimensional and the cone is seven-dimensional, and the strata are the same three shapes cut in spaces of different sizes.

## The General Order

**Proposition.** For the algebra of all linear maps of an $n$-dimensional complex space, the rank of an operator takes the $n+1$ values $0,1,\dots,n$, and the determinantal variety of the operators of rank at most $k$ has dimension $2nk-k^{2}$.

*Proof.* The rank is the dimension of the image; the variety of operators whose image lies in a fixed $k$-dimensional subspace and whose kernel contains a fixed complementary subspace has the stated dimension, and it is the closure of the set of operators of rank exactly $k$.

**Corollary.** At the order of this row the general count gives five values and the sector where both parameters are invertible gives two, the collapse being from $n+1$ to $2$.

*Proof.* Put $n=4$ in the proposition for the five values; the collapse is the theorem on the cone.

**Corollary.** The determinantal variety of rank at most one has dimension seven, and the cone meets it in a subvariety of dimension five.

*Proof.* The formula with $k=1$ gives $2n-1=7$; the products of two degenerate parameters have rank one by the theorem, and the pairs of degenerate parameters form a set of dimension $3+3=6$ on which the scalars act, so the image has dimension five.

**The reading.** An algebra whose degenerate elements fill a hypersurface has the fewest possible rank strata above the middle and the most structure inside each. The five determinantal varieties of the general row collapse to three, and the information that they carried is carried here by the tensor rank of the coefficients, which is the subject of the companion article on the length.

## The Failure to Separate

**Proposition.** The rank does not separate the operators: two products with different spectra and different tensor coordinates have the same rank.

*Proof.* Every product of two invertible parameters has rank four, whatever the parameters, so the rank is constant on a seven-dimensional family.

**Corollary.** A second invariant is needed, and the tensor rank of the coefficients is the natural one.

*Proof.* The tensor rank varies between one and sixteen on the space while the map rank varies over three values, so the two invariants are independent.

**Corollary.** The pair of invariants determines neither the spectrum nor the orbit of the operator under the unit group.

*Proof.* The spectrum is invariant under conjugation by units and is not a function of the two ranks, and the orbit of a product under conjugation is the set of products with conjugated parameters, which the ranks do not distinguish.

**The reading.** The rank is coarse by construction. It answers one question, whether an operator is invertible or how badly not, and it answers it in three words. Every finer question about a two-sided operator is a question about its coefficients or its spectrum, and the article on the length takes the first of those routes.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{rank}T$ | the dimension of the image |
| $\operatorname{rank}T_{a,b}=4$ | both parameters invertible |
| $\operatorname{rank}T_{a,b}=2$ | exactly one parameter degenerate |
| $\operatorname{rank}T_{a,b}=0$ | the vertex of the cone |
| $0$ and $15$ real dimensions | the strata on the cone and on the space |
| $2nk-k^{2}$ | the dimension of the general determinantal variety |

## Further Reading

- [The Two-Sided Operators and the Segre Cone](the-two-sided-operators-and-the-segre-cone.html), for the cone on which the strata are cut.
- [N-Regularity and N-Degeneracy in the Biquaternion Algebra](n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html), for the criterion of invertibility.
- [The Length and the Two Ranks](the-length-and-the-two-ranks.html), for the second invariant.
- [The Spin-Zero Carrier and the Rank Strata](the-spin-zero-carrier-and-the-rank-strata.html), for the rank restricted to the scalar line.
- [The Left Ideals and the Image of a Left Multiplication](the-left-ideals-and-the-image-of-a-left-multiplication.html), for the images of the one-sided families.
