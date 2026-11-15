# __The Two-Sided Operators and the Segre Cone at $n=4$__

## Introduction

**The operators $T_{a,b}(X)=aXb$ form a sixteen-dimensional algebra with the product rule $T_{a,b}T_{c,d}=T_{ac,db}$; in the axis-free basis the sixteen $T_{\mu\nu}$ are signed permutations of determinant one and form a basis, the coefficient matrix of $T_{a,b}$ is the outer product $c_{\mu\nu}=a_\mu b_\nu$ of rank one, so the set of two-sided operators is the Segre cone over $\mathbb{P}^{3}\times\mathbb{P}^{3}$, of dimension seven.**

The article proves the product rule, proves that the sixteen basis operators are independent signed permutations, computes the coefficient matrix and its rank, identifies the set of operators with the cone over the Segre variety, gives the criterion of rank at most one, records the orthogonality $\operatorname{tr}(T^{\dagger}T)=4\delta$ and the coordinate formula $c_{\mu\nu}=\tfrac14\operatorname{tr}(T_{\mu\nu}^{\dagger}M)$, and describes the real slice and the two one-sided boundaries.

It assumes *The One-Sided Operators at $n=4$* and *$M_4(\mathbb{C})$ Axis-Free Representation: Operators*. The model at order two is *The Two-Sided Operators and the Segre Cone at $n=2$*; the length built on the coefficient matrix is *The Length and the Two Ranks at $n=4$*.

## The Two-Sided Operators

**Definition.** For $a,b\in\mathbb{B}$ let $T_{a,b}$ be the operator $X\mapsto aXb$.

**Proposition.** $T_{a,b}=L_aR_b$, the map $(a,b)\mapsto T_{a,b}$ is bilinear, and $T_{a,b}=0$ only when $a=0$ or $b=0$.

**Proof.** The two-sided operator is the composition of a left and a right multiplication; bilinearity is bilinearity of the product; and $a\,e_t\,b=ab$ is nonzero when both factors are.

**Corollary.** The sixteen operators $T_{\mu\nu}=T_{e_\mu,e_\nu}$ on the units form a basis of the sixteen-dimensional algebra.

**Proof.** They are independent as matrices, since each is a signed permutation and distinct signed permutations are distinct matrices, and there are sixteen of them in a space of dimension sixteen.

**Corollary.** Every element of $M_4(\mathbb{C})$ acts on the algebra as a finite sum of two-sided operators, and the sum is unique in the basis.

**Proof.** The basis property and the dimension.

**The interpretation.** $\mathbb{B}\otimes\mathbb{B}^{\mathrm{opp}}\cong\operatorname{End}(\mathbb{B})$ through $a\otimes b^{\mathrm{op}}\mapsto T_{a,b}$, of dimension $16$.

**Proof.** The tensor map of the regular representation article.

## The Product Rule

**Theorem.** For elements $a,b,c,d$,
$$
T_{a,b}\,T_{c,d}=T_{ac,db}.
$$

**Proof.** Apply the left side to $X$: $a(cXd)b=(ac)X(db)$.

**Corollary.** The product is closed, the operators form an algebra, and the unit is $T_{e_t,e_t}=\mathrm I_4$.

**Proof.** The rule with $a=c=e_t$, and $T_{e_t,e_t}(X)=X$.

**Corollary.** The rule is not the product rule of the tensor algebra: the second index is reversed, which is the content of the "opposite" in $\mathbb{B}^{\mathrm{opp}}$.

**Proof.** The tensor product multiplies the two factors in the same order.

**The trace of a product.** $\operatorname{tr}(T_{a,b}T_{c,d})=\operatorname{tr}(ac)\operatorname{tr}(db)$, by the trace formula of the regular representation.

**Proof.** $T_{a,b}T_{c,d}=T_{ac,db}$ and the trace of $T_{A,B}$ is $\operatorname{tr}A\operatorname{tr}B$.

**Corollary.** The trace pairing on the operator algebra is the product of the two trace pairings of the algebra, so it is nondegenerate and indefinite.

**Proof.** $\operatorname{tr}(T_{a,b}T_{c,d})=\operatorname{tr}(ac)\operatorname{tr}(db)$ is the tensor product of the two trace pairings, each of which is nondegenerate and takes both signs.

## The Coefficient Matrix

**Definition.** For $M\in M_4(\mathbb{C})$ the **coefficient matrix** $c(M)$ is the $4\times4$ matrix of coefficients in the expansion $M=\sum c_{\mu\nu}T_{\mu\nu}$.

**Proposition.** $c_{\mu\nu}=\tfrac14\operatorname{tr}(T_{\mu\nu}^{\dagger}M)$, and the formula is exact.

**Proof.** The operators $T_{\mu\nu}$ satisfy $\operatorname{tr}(T_{\mu\nu}^{\dagger}T_{\rho\sigma})=4\delta_{\mu\rho}\delta_{\nu\sigma}$, so expanding $M$ and taking the pairing with $T_{\mu\nu}^{\dagger}$ isolates $4c_{\mu\nu}$.

**Corollary.** $c(T_{a,b})$ is the matrix $\tilde a\tilde b^{\mathsf T}$, where $\tilde a$ and $\tilde b$ are the coefficient vectors of $a$ and $b$; hence $\operatorname{rank}c(T_{a,b})=1$ for nonzero $a,b$.

**Proof.** Expand $aXb=\sum_{\mu}\tilde a_\mu e_\mu X\sum_\nu\tilde b_\nu e_\nu$ and read the coefficient of $T_{\mu\nu}$, which is $\tilde a_\mu\tilde b_\nu$.

**Corollary.** $\operatorname{tr}M=4c_{tt}$, since $T_{tt}=\mathrm I_4$ is the only basis element of nonzero trace.

**Proof.** The diagonal entries of $T_{\mu\nu}$ for $(\mu,\nu)\neq(t,t)$ cancel in pairs on the four basis elements, so each of the fifteen has trace zero, while $T_{tt}=\mathrm I_4$ has trace four.

## The Segre Cone

**Definition.** The **Segre variety** is the image of $\mathbb{P}^{3}\times\mathbb{P}^{3}$ in $\mathbb{P}^{15}$ under the map sending a pair of lines to the rank-one matrix, and the **Segre cone** is the affine cone over it.

**Theorem.** The set of two-sided operators $\{T_{a,b}:a,b\in\mathbb{B}\}$ is exactly the Segre cone: the set of matrices of rank at most one, of complex dimension $7$.

**Proof.** Every $T_{a,b}$ has coefficient matrix of rank one by the outer-product form; conversely a matrix of rank one is $uv^{\mathsf T}$, which is $c(T_{a,b})$ for the elements with coefficient vectors $u$ and $v$; the cone over a variety of dimension $3+3=6$ has dimension $7$.

**Corollary.** The projective image of the cone is $\mathbb{P}^{3}\times\mathbb{P}^{3}$, and the two factors are the two one-sided families.

**Proof.** The pair $(a,b)$ is determined up to simultaneous scaling by the operator, so the projective classes are pairs of points of the two projective spaces.

**Corollary.** The cone is not convex at the origin and is not a linear subspace: the sum of two rank-one matrices has rank one or two.

**Proof.** The rank of a sum of two rank-one matrices is one when the factors are proportional and two otherwise.

**The two rulings.** Through every point of the cone pass two projective three-spaces, the set of operators with fixed left factor and the set with fixed right factor.

**Proof.** Fix $a$ and vary $b$, or fix $b$ and vary $a$.

## The Criterion of the Rank One

**Theorem.** An operator $M$ is a single two-sided product exactly when $\operatorname{rank}c(M)\le1$.

**Proof.** If $M=T_{a,b}$ the coefficient matrix is an outer product; conversely, if $\operatorname{rank}c(M)\le1$ then $c_{\mu\nu}=u_\mu v_\nu$ for some vectors, and $M=\sum u_\mu v_\nu T_{\mu\nu}=T_{a,b}$ with $a=\sum u_\mu e_\mu$ and $b=\sum v_\nu e_\nu$.

**Corollary.** The operators of rank-one coefficient matrix are exactly the points of the Segre cone, and they are the products of one left and one right multiplication.

**Proof.** The theorem and the description of the cone.

**Corollary.** A sum of two such operators has coefficient matrix of rank at most two, and the rank counts the minimal number of products in the decomposition.

**Proof.** The coefficient matrix of a sum is the sum of the coefficient matrices, and the rank of a sum of $k$ rank-one matrices is at most $k$.

**The length.** The minimal number of products in a decomposition of $M$ is $\operatorname{rank}c(M)$, the length of the operator article.

**Proof.** The corollary and the existence of a decomposition with $\operatorname{rank}$ terms.

## The Pairing and the Coordinates

**Theorem.** $\operatorname{tr}(T_{\mu\nu}^{\dagger}T_{\rho\sigma})=4\delta_{\mu\rho}\delta_{\nu\sigma}$, so the sixteen operators are orthogonal for the Hilbert–Schmidt form and the formula $c_{\mu\nu}=\tfrac14\operatorname{tr}(T_{\mu\nu}^{\dagger}M)$ is exact.

**Proof.** $T_{\mu\nu}^{\dagger}$ is the transpose of the matrix, which is again a signed permutation; the product of two distinct signed permutations has zero trace, and the product of one with itself is the identity.

**Corollary.** The map $M\mapsto 4c(M)$ is the Hilbert–Schmidt expansion, and $\lVert M\rVert_F^{2}=4\sum_{\mu\nu}|c_{\mu\nu}|^{2}$.

**Proof.** Expand $M$ in the orthogonal basis and use the norm of each basis vector, which is $4$.

**Corollary.** The trace pairing and the Hilbert–Schmidt pairing have the same diagonal in this basis and differ only in the signs: $+4$ on the ten symmetric operators and $-4$ on the six antisymmetric ones.

**Proof.** The transpose of $T_{\mu\nu}$ is $\pm T_{\mu\nu}$, and the sign is the symmetry of the pair.

## The Real Slice and the Two Boundaries

**Proposition.** Over $\mathbb{R}$ the operators $T_{a,b}$ with real coefficients form a real subspace of dimension $16$ inside the real $32$-dimensional endomorphism algebra, and the Segre cone of the real slice is the cone over $\mathbb{P}^{3}(\mathbb{R})\times\mathbb{P}^{3}(\mathbb{R})$.

**Proof.** The restriction of scalars and the same rank-one argument over the reals.

**Corollary.** The real cone has dimension $7$ and its projective image is a product of two real projective three-spaces, each of dimension three.

**Proof.** $3+3=6$ projective dimensions and one more for the cone.

**The two rulings.** For a fixed nonzero $a$ the operators $T_{a,b}$ form a four-dimensional subspace, and for a fixed nonzero $b$ the operators $T_{a,b}$ form another; these are the two rulings of the cone, and their intersection is the line of scalars times $T_{a,b}$ itself.

**Proof.** The linearity in each variable and the rank-one form of the coefficient matrix, whose kernel and image lines are fixed by the ruling.

**Corollary.** The vertex of the cone is the zero operator, and it lies in both rulings.

**Proof.** $T_{0,b}=T_{a,0}=0$.

**The degenerate case.** An operator of coefficient rank zero is the zero operator; the operators of coefficient rank one are the points of the cone away from the vertex; the operators of larger rank are outside the cone and are the sums of several products.

**Proof.** The rank criterion and the closure of the set of rank-at-most-one matrices.

## Summary

The two-sided operators $T_{a,b}(X)=aXb$ form a sixteen-dimensional algebra with the product rule $T_{a,b}T_{c,d}=T_{ac,db}$, and the sixteen operators on the units are signed permutations of determinant one forming a basis. The coefficient matrix of $T_{a,b}$ is the outer product of the two coefficient vectors, hence of rank one.

The set of single products is therefore the Segre cone over $\mathbb{P}^{3}\times\mathbb{P}^{3}$, of complex dimension seven, and the criterion for being a single product is that the coefficient matrix have rank at most one. The Hilbert–Schmidt pairing makes the sixteen operators orthogonal with squared norm four, and the coordinate formula is exact.

Over the reals the same cone is the cone over the product of two real projective three-spaces, and its two boundaries are the two one-sided degenerations.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $T_{a,b}(X)=aXb$ | the two-sided operator |
| $T_{\mu\nu}$ | the sixteen basis operators |
| $c(M)$ | the coefficient matrix, with $c_{\mu\nu}=\tfrac14\operatorname{tr}(T_{\mu\nu}^{\dagger}M)$ |
| $\mathbb{P}^{3}\times\mathbb{P}^{3}$ | the Segre variety over which the cone is built |
| $\operatorname{rank}c(M)$ | the length of the operator |
| $\operatorname{tr}(T^{\dagger}T)=4\delta$ | the Hilbert–Schmidt orthogonality |

## Further Reading

- Joe Harris, *Algebraic Geometry: A First Course* (Springer, 1992), for the Segre varieties and their cones.
- [The One-Sided Operators at $n=4$](the-one-sided-operators-at-n-4.html), for the two families whose products these are.
- [The Length and the Two Ranks at $n=4$](the-length-and-the-two-ranks-at-n-4.html), for the rank of the coefficient matrix as the length.
- [$M_4(\mathbb{C})$ Axis-Free Representation: Operators](m4c-axis-free-representation-operators.html), for the sixteen matrices and the trace pairing.
- [The Two-Sided Operators and the Segre Cone at $n=2$](the-two-sided-operators-and-the-segre-cone-at-n-2.html), for the case at order two.
