# __The Coefficients of a Two-Sided Operator: A Worked Computation__

## Introduction

**The subject.** Every operator on the algebra is a unique combination of the sixteen basis operators $T_{e_\mu,e_\nu}$, and the sixteen coefficients of an operator are its coordinates. The article computes them for a two-sided operator and finds that they are the pairwise products of the four coordinates of one parameter and the four of the other: a tensor of rank one. The computation is carried through on the pair $a=e_t+\vec e_x$, $b=e_t+\vec e_y$, whose operator has four nonzero coefficients, and it is checked against the product law. The trace and the determinant are then recovered from the coefficients, and the test for a general operator to be a single product is stated as the vanishing of the quadratic relations of the tensor.

**The order of the article.** The expansion is stated first, then the worked pair, then the check by the product law. The two invariants follow, and the general tensor closes the article.

**It assumes** *$\operatorname{End}(\mathbb{B})$ as an Algebra: the Regular Representation*, *Operators Acting on Two Sides* and *The Tensor Product of Two Biquaternion Algebras*. **The row of the elements is** where a product of two elements is four numbers; here the product is sixteen, and the sixteen are built from the two fours.

**The result in one line.** The coefficient tensor of $T_{a,b}$ is the outer product $c_{\mu\nu}=a_\mu b_\nu$, so that a two-sided operator is exactly an operator whose sixteen coefficients form a tensor of rank one.

**Boundaries.** The cone of the products and its two rulings are *The Two-Sided Operators and the Segre Cone*; the minimal number of products in a sum is *The Length and the Two Ranks*; the products of the one-sided families are *The One-Sided Operators*.

## The Expansion

**Theorem.** For a pair of parameters, written $a=\sum_\mu a_\mu e_\mu$ and $b=\sum_\nu b_\nu e_\nu$,
$$
T_{a,b}=\sum_{\mu,\nu}a_\mu b_\nu\,T_{e_\mu,e_\nu}.
$$

*Proof.* Expand the product $aXb$ in the two parameters and use the bilinearity of the composition: $aXb=\sum_{\mu,\nu}a_\mu b_\nu e_\mu Xe_\nu$, and the coefficient of each basis operator is the product displayed.

**Corollary.** The coefficient tensor of a product is the outer product of the two coordinate vectors, and it has rank one whenever both parameters are nonzero.

*Proof.* A tensor whose entries are the pairwise products of two vectors is the tensor product of those vectors, which is nonzero and is of rank one; a rank-one tensor is by definition one of that form.

**Corollary.** The coordinates of a product satisfy the quadratic relations
$$
c_{\mu\nu}c_{\rho\sigma}=c_{\mu\sigma}c_{\rho\nu}
$$
for all quadruples of indices, and the relations characterise the products among all the operators.

*Proof.* Substituting $a_\mu b_\nu$ for $c_{\mu\nu}$ both sides equal $a_\mu b_\nu a_\rho b_\sigma$; conversely, if the relations hold and some coefficient is nonzero, say $c_{tt}$, then $c_{\mu\nu}=c_{\mu t}c_{t\nu}/c_{tt}$ and the operator is the product of the parameters with coordinates $c_{\mu t}/c_{tt}$ and $c_{t\nu}$.

**The reading.** The sixteen coordinates of a two-sided operator are determined by eight numbers. The map from pairs of parameters to operators is injective up to the simultaneous scaling, and its image is cut out by the quadratic relations, which say that the coefficient tensor factors.

## The Worked Pair

**The computation.** Take $a=e_t+\vec e_x$ and $b=e_t+\vec e_y$, so that the coordinates are $a_t=a_x=1$, $a_y=a_z=0$ and $b_t=b_y=1$, $b_x=b_z=0$. The sixteen coefficients are the products:
$$
c_{tt}=1,\quad c_{ty}=1,\quad c_{xt}=1,\quad c_{xy}=1,
$$
and the other twelve vanish.

**The operator.** The expansion reads
$$
T_{a,b}=T_{e_t,e_t}+T_{e_t,\vec e_y}+T_{\vec e_x,e_t}+T_{\vec e_x,\vec e_y},
$$
so that
$$
T_{a,b}(X)=X+X\vec e_y+\vec e_xX+\vec e_xX\vec e_y .
$$

**Proposition.** The four displayed coefficients are correct, and the twelve others vanish.

*Proof.* Expand $(e_t+\vec e_x)X(e_t+\vec e_y)=X+X\vec e_y+\vec e_xX+\vec e_xX\vec e_y$ and compare with the definition of the four basis operators.

**Proposition.** The multiplication of the units reproduces the law, and both parameters of the product are the same element. With $c=e_t+\vec e_y$ and $d=e_t+\vec e_x$,
$$
T_{a,b}T_{c,d}=T_{ac,\,db}=T_{\,e_t+\vec e_x+\vec e_y+\vec e_x\vec e_y,\ e_t+\vec e_x+\vec e_y+\vec e_x\vec e_y}.
$$

*Proof.* Compute $ac=(e_t+\vec e_x)(e_t+\vec e_y)=e_t+\vec e_y+\vec e_x+\vec e_x\vec e_y$ and $db=(e_t+\vec e_x)(e_t+\vec e_y)$, the same element; the law gives the product of the two operators as the two-sided operator of that pair. Computing the product directly from the two expansions gives the same sixteen coefficients, which is the check.

**The reading.** The worked pair shows the mechanism: four nonzero coefficients out of sixteen, each a product, and the product law acts on the parameters rather than on the coefficients. A reader who wants to multiply two two-sided operators multiplies their parameters and never their coefficients.

## The Two Invariants

**Theorem.** The trace of a two-sided operator is read from its coefficients by
$$
\operatorname{tr}(T_{a,b})=4\,c_{tt},
$$
and the determinant is
$$
\det(T_{a,b})=N(a)^{2}N(b)^{2}.
$$

*Proof.* The trace of each basis operator is $4$ at the pair $(e_t,e_t)$ and $0$ at the other fifteen, because the trace of $T_{A,B}$ is $4\,\mathrm{Sc}(A)\mathrm{Sc}(B)$; so the trace of the expansion is $4c_{tt}$. For the determinant, the eigenvalues of the left and right multiplications are the two roots of the quadratic of the parameter, each twice, so the determinant of each one-sided factor is the square of the multiplicative norm, and the determinant of the product is the product of the two.

**Corollary.** In the worked pair the trace is four and the determinant is sixteen.

*Proof.* The coefficient $c_{tt}=1$ gives the trace $4$; the two multiplicative norms are $1+1=2$ each, and the determinant is $2^2\cdot2^2=16$.

**Corollary.** An operator of the form $T_{a,b}$ is invertible exactly when both multiplicative norms are nonzero, and the vanishing of the determinant detects exactly the degenerate parameters.

*Proof.* The determinant is a product of two squares, and a square vanishes exactly when the norm does; an element is invertible exactly when its norm does not vanish.

**The reading.** The two invariants of the operator are read from four numbers: the single coefficient $c_{tt}$ and the two norms. The trace sees only the scalar coordinates, the determinant sees the norms, and neither sees the rest of the tensor.

## The General Operator

**Definition.** The **tensor rank** of an operator is the least number of products $T_{a,b}$ whose sum it is; it is the rank of its coefficient tensor in the sense of the tensor square.

**Proposition.** The tensor rank of an operator lies between one and four, and the value four is attained.

*Proof.* The coefficient tensor is a four-by-four array of numbers, and the least number of rank-one tensors summing to it is the rank of that array as a map of a four-dimensional space into itself, which is at most four; an array with generic entries has that rank equal to four, and every rank-one array is a product.

**Corollary.** The operators of tensor rank one are exactly the products, and the operators of tensor rank greater than one are the sums of products that are not themselves products.

*Proof.* The first statement is the definition combined with the rank-one criterion of the expansion; the second is the negation.

**Corollary.** The two-sided operators are a proper subset of the operator space, of complex dimension seven, and the test for membership is the quadratic relations of the coefficients.

*Proof.* The parameter count $8-1=7$, and the relations of the expansion section.

**The reading.** The coefficients are a tensor and the computation never needs a square arrangement of them. The tensor carries the whole structure: the products are its rank-one points, the sums are its general points, and the two invariants are two of its contractions. A reader who writes the sixteen coefficients in a square finds that the square never enters any proof.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $c_{\mu\nu}=a_\mu b_\nu$ | the coefficient tensor of a product |
| $c_{\mu\nu}c_{\rho\sigma}=c_{\mu\sigma}c_{\rho\nu}$ | the quadratic relations |
| $\operatorname{tr}(T_{a,b})=4c_{tt}$ | the trace from the coefficients |
| $\det(T_{a,b})=N(a)^{2}N(b)^{2}$ | the determinant from the parameters |
| $a=e_t+\vec e_x$, $b=e_t+\vec e_y$ | the worked pair, four nonzero coefficients |
| tensor rank | the least number of products in a sum |

## Further Reading

- [$\operatorname{End}(\mathbb{B})$ as an Algebra: the Regular Representation](end-b-as-an-algebra-the-regular-representation.html), for the basis and the trace form.
- [Operators Acting on Two Sides](operators-acting-on-two-sides.html), for the family and its composition law.
- [The Two-Sided Operators and the Segre Cone](the-two-sided-operators-and-the-segre-cone.html), for the rank-one condition read as a cone.
- [The Length and the Two Ranks](the-length-and-the-two-ranks.html), for the tensor rank as the length.
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the multiplicative norm of the parameters.
