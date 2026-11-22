# __The Two-Sided Operators and the Segre Cone__

## Introduction

**The subject.** The operators $T_{a,b}(X)=aXb$ are the decomposable elements of the sixteen-dimensional operator space, and they form a cone: a set closed under multiplication by scalars and spanned by a bilinear image of two four-dimensional parameter spaces. The article computes the cone. Its dimension is seven, its vertex is the zero operator, and its projective image is the product of two projective three-spaces, the Segre variety of the decomposable tensors. What the degeneracy of the parameters changes is not the shape of the cone but the rank of its points: a point is of rank four when both parameters are invertible and of rank two when exactly one of them is degenerate, so the operators of rank at most two form a proper part of the cone and the vertex is their only point of rank zero.

**The order of the article.** The operators and their product law come first; the basis and the independence second. The cone and its dimension follow, then the rank of a product, and the two rulings close the description.

**It assumes** *Operators Acting on Two Sides*, *The Tensor Product of Two Biquaternion Algebras* and *Zero Divisors and Invertibles in the Biquaternion Algebra*. **The row of the elements is** where a product of two elements is read; here the product is read as an operator, and the pair of parameters is read as a tensor.

**The result in one line.** The products fill a proper cone of complex dimension seven whose points have rank four over the invertible pairs of parameters, two over the pairs with one degenerate factor, one over the pairs with two degenerate factors, and zero at the vertex, and whose projective image is the Segre variety of the tensor square.

**Boundaries.** The one-sided boundaries of the cone are *The Left Ideals and the Image of a Left Multiplication*; the sums of products and their length are *The Length and the Two Ranks*; the difference and the sum of the two sides at one pair are the subject of the companion article on the Sylvester operator.

## The Operators and Their Law

**Definition.** For a pair of elements the **two-sided operator** is $T_{a,b}=L_aR_b$, with $T_{a,b}(X)=aXb$.

**Proposition.** The assignment is bilinear, the operator is zero only when a parameter is zero, and
$$
T_{a,b}T_{c,d}=T_{ac,db}.
$$

*Proof.* Bilinearity is the bilinearity of the product; $T_{a,b}(e_t)=ab$ is nonzero for two nonzero parameters; and the composite sends $X$ to $a(cXd)b=(ac)X(db)$.

**Corollary.** For each invertible $b$ the path $a\mapsto T_{a,b}$ is an injective linear map of the algebra into the operator space, and for each invertible $a$ the path $b\mapsto T_{a,b}$ is injective as well.

*Proof.* Linearity is bilinearity. If $T_{a,b}=0$ with $b$ invertible then $a=0$, since $ab=0$ forces $a=0$; and $T_{a,b}=T_{a',b}$ gives $aXb=a'Xb$ for all $X$, hence $a=a'$ after multiplying by $b^{-1}$ on the right.

**The reading.** The two parameters enter asymmetrically. The map from the left parameter is an isomorphism onto a four-dimensional subspace of the sixteen, and the map from the right parameter is an isomorphism onto another; the cone is the image of the pair, and its shape is the shape of a bilinear image.

## The Basis

**Theorem.** The sixteen operators $T_{e_\mu,e_\nu}$ are a basis of the operator space.

*Proof.* They are independent for the Hilbert–Schmidt pairing, which gives $\langle T_{e_\alpha,e_\beta},T_{e_\mu,e_\nu}\rangle_{*}=4\delta_{\alpha\mu}\delta_{\beta\nu}$; sixteen independent operators in a space of dimension sixteen are a basis.

**Corollary.** Every operator is a unique sum $\sum c_{\mu\nu}T_{e_\mu,e_\nu}$, and the sixteen coefficients are its coordinates.

*Proof.* The expansion in a basis.

**Corollary.** A product $T_{a,b}$ has the coordinates $c_{\mu\nu}=a_\mu b_\nu$, the pairwise products of the coordinates of the two parameters.

*Proof.* Expand $aXb=\sum_{\mu,\nu}a_\mu b_\nu e_\mu Xe_\nu$ and read the coefficient of each basis operator.

**The reading.** The coordinates of a product form a rank-one tensor: sixteen numbers built from four and four. The cone is the image of the map that sends a pair of parameter vectors to that tensor, and its geometry is the geometry of the rank-one tensors in a sixteen-dimensional space.

## The Cone and Its Dimension

**Definition.** The **cone of the products** is
$$
\mathcal C=\{T_{a,b}:a,b\in\mathbb{B}\}\subseteq\operatorname{End}(\mathbb{B}).
$$

**Theorem.** The cone is closed under multiplication by scalars, its vertex is the zero operator, and its dimension is seven.

*Proof.* Closure: $\lambda T_{a,b}=T_{\lambda a,b}$. The vertex: $T_{0,b}=T_{a,0}=0$. The dimension: the parameter space has dimension eight, and the group of scalars acts by $(\lambda a,\lambda^{-1}b)$, with trivial stabiliser at every pair of nonzero parameters, so the orbits are lines and the image has dimension $8-1=7$.

**Corollary.** The projective image of the cone is the Segre variety, the product of the two projective three-spaces of the left and of the right parameter, and the two factors are the two one-sided families.

*Proof.* A pair is determined up to simultaneous scaling by the operator, so the projective classes of the products are pairs of projective classes of parameters; the two factors record which parameter is which.

**Corollary.** The cone is proper: it has dimension seven inside a space of dimension sixteen, and it is not a linear subspace.

*Proof.* The dimension count, and the fact that the sum of two products is generally not a product, since the coordinates of a sum of two rank-one tensors have tensor rank two.

**The reading.** The degeneracy of the parameters does not flatten the cone. What it changes is the stratification by rank: the cone remains a seven-dimensional variety, and the rank of its points is constant only on the two pieces cut out by the degeneracy of the parameters. The two facts are independent, one about the tensor and one about the operator.

## The Rank of a Product

**Theorem.** For every pair of parameters
$$
\operatorname{rank}T_{a,b}=\frac{\operatorname{rank}L_a\cdot\operatorname{rank}R_b}{4},
$$
so the rank is four when both parameters are invertible, two when exactly one of them is degenerate, one when both are degenerate, and zero when a parameter vanishes.

*Proof.* The image of $T_{a,b}$ consists of the composites $aXb$, which vanish on the kernel of $b$ and take their values in the image of $a$; the space of such composites has dimension $r(a)r(b)$, where $r$ is the rank of an element as a map of the two-dimensional spinor space. Multiplication by an invertible element on either side does not change the rank, and $r(a)$ is two, one or zero according as $a$ is invertible, a nonzero zero divisor or zero.

**Corollary.** The cone meets the determinantal variety of the operators of rank at most one in a closed subvariety of dimension five, and that variety has complex dimension seven.

*Proof.* A product has rank one exactly when both parameters are degenerate, so the intersection is the image of the pairs of degenerate parameters. The variety itself is the set of operators whose image is a line: projectively it is the Segre variety of the two projective three-spaces, of dimension $3+3=6$, and its cone over the origin has dimension seven. The intersection has dimension $3+3-1=5$, a proper subvariety of the rank-one variety, of dimension five against seven.

**Corollary.** The determinantal set of the operators of rank at most two has complex dimension twelve, and it meets the cone in a closed subvariety of dimension six, the products with at least one degenerate factor. The cone is not contained in it.

*Proof.* The dimension twelve is $8k-k^{2}$ at $k=2$. The intersection is the image of the pairs with at least one degenerate factor: one parameter runs over the surface of the degenerate elements, of dimension three, and the other over the whole algebra, of dimension four, so the image has dimension $3+4-1=6$ after the scaling. The identity $T_{e_t,e_t}$ lies on the cone and has rank four, so the cone escapes the determinantal set.

**The reading.** The rank of a two-sided operator says whether its parameters are degenerate, and nothing else. Two products with the same rank are indistinguishable by the rank, whatever their tensor coordinates; the rank separates the vertex from the rest and never looks inside the rest.

## The Two Rulings

**Definition.** For a fixed nonzero $a$, the **left ruling** is the set $\{T_{a,b}\}$; for a fixed nonzero $b$, the **right ruling** is the set $\{T_{a,b}\}$.

**Proposition.** Each ruling is a four-dimensional subspace of the operator space, and two rulings of the same kind meet only at the vertex.

*Proof.* The set $\{T_{a,b}\}$ is the image of the injective linear map $b\mapsto T_{a,b}$, hence a subspace of dimension four. Two left rulings $\{T_{a,b}\}$ and $\{T_{a',b}\}$ with $a'\neq\lambda a$ meet only at zero, since a common nonzero element would give $aXb=a'Xb'$ for all $X$ and hence proportional parameters by the independence of the tensor coordinates.

**Corollary.** The cone is the union of the rulings, and the rulings of the two kinds meet pairwise in the single line spanned by the product of their parameters.

*Proof.* Every point lies in one ruling of each kind; a left ruling and a right ruling meet in the multiples of $T_{a,b}$.

**Corollary.** The vertex lies in every ruling, so the cone is a cone over its vertex in the strict sense.

*Proof.* $T_{0,b}=T_{a,0}=0$.

**The reading.** The rulings are the two families of the tensor square. Their intersections are lines, and the whole cone is the union of the lines through the vertex. This is the Segre picture, and it survives the degeneracy of the parameters unchanged: the geometry of the cone is the geometry of the decomposable tensors, and the operator rank is an extra layer that the geometry does not see.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $T_{a,b}(X)=aXb$ | the two-sided operator |
| $\mathcal C=\{T_{a,b}\}$ | the cone of the products, dimension seven |
| $c_{\mu\nu}=a_\mu b_\nu$ | the coordinates of a product, a rank-one tensor |
| $\lambda T_{a,b}=T_{\lambda a,b}$ | the scaling and the orbit |
| $\operatorname{rank}T_{a,b}$ | four, two, or zero at the vertex |
| $\{T_{a,b}:b\}$, $\{T_{a,b}:a\}$ | the two rulings |

## Further Reading

- [Operators Acting on Two Sides](operators-acting-on-two-sides.html), for the family and its first properties.
- [The Tensor Product of Two Biquaternion Algebras](the-tensor-product-of-two-biquaternion-algebras.html), for the decomposable tensors behind the cone.
- [The Coefficients of a Two-Sided Operator: A Worked Computation](the-coefficients-of-a-two-sided-operator-a-worked-computation.html), for the coordinates of a product.
- [The Left Ideals and the Image of a Left Multiplication](the-left-ideals-and-the-image-of-a-left-multiplication.html), for the images of the one-sided factors.
- [The Four Ranks of the Two-Sided Operators](the-four-ranks-of-the-two-sided-operators.html), for the rank stratified over the whole space.
