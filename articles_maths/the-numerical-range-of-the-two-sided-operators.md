# __The Numerical Range of the Two-Sided Operators__

## Introduction

**The subject.** The numerical range of an operator is the set of the values of the form $\langle X,TX\rangle/\langle X,X\rangle$ over the nonzero elements of the algebra, and it is the one invariant of the operator space that is not polynomial in the coefficients. The article computes its elementary properties, identifies the operators whose range is a single point, and locates the range of a product relative to the spectra of its two parameters. For Hermitian parameters the range is a segment, for unitary ones it lies in the disc, and in general it contains the four products of the eigenvalues.

**The order of the article.** The definition and the compactness come first, then the convexity. The single-point case follows, then the range of a product, and the boundary closes the article.

**It assumes** *The Adjoints and the Polar Decomposition of an Operator*, *The Spectrum of a Biquaternion* and *Operators Acting on Two Sides*. **The row of the elements is** where the numerical range of an element is the convex hull of its spectrum; here the range of an operator is a two-dimensional region in general.

**The result in one line.** The range is compact and convex, it is a point exactly for the scalar operators, and for a product it contains the four products of the eigenvalues of the parameters.

**Boundaries.** The spectrum of the operator is *The Four Ranks of the Two-Sided Operators*; the form itself is *The Adjoints and the Polar Decomposition of an Operator*; the products are *The Two-Sided Operators and the Segre Cone*.

## The Definition and the Compactness

**Definition.** For an operator $T$ the **numerical range** is
$$
W(T)=\left\{\frac{\langle X,TX\rangle}{\langle X,X\rangle}:X\neq0\right\},
$$
with $\langle X,Y\rangle=\operatorname{tr}(X^{\star}Y)$.

**Proposition.** The range is the image of the unit sphere of the algebra under a continuous map, hence compact, and it is contained in the disc of radius the operator norm.

*Proof.* The map $X\mapsto\langle X,TX\rangle$ is continuous and the unit sphere is compact, so the image is compact after the division by the positive norm; and $|\langle X,TX\rangle|\le\|T\|\langle X,X\rangle$ by the Cauchy–Schwarz inequality.

**Corollary.** The range contains the spectrum of the operator.

*Proof.* An eigenvector gives a value equal to its eigenvalue.

**The reading.** The range is a compact piece of the plane, and it is read from the form and the action alone. Unlike the trace, the determinant or the coefficients, it is not a polynomial invariant, and this is why the two-sided family needs it: the algebraic invariants cannot see the shape of the region where the form takes its values.

## The Convexity

**Theorem.** The numerical range is convex.

*Proof.* Let $z_1$ and $z_2$ be the values at two unit elements $X$ and $Y$, and let $z$ be a convex combination. The element $X\cos\theta+Y\sin\theta$ over a suitable real parameter sweeps a two-dimensional family of values whose image contains the segment from $z_1$ to $z_2$: the value at that element is a quadratic function of the parameter, and the two ends of the curve plus its convexity give the result. The general statement is the Toeplitz–Hausdorff theorem, and in finite dimension it follows from the connectedness of the set of decompositions of a unit element into two orthogonal pieces.

**Corollary.** The range is the convex hull of the set of the values at the unit elements, and it therefore contains the convex hull of the spectrum.

*Proof.* The definition gives the set, and the theorem gives its convexity.

**Corollary.** The range is a segment exactly when the operator is normal, and it is a disc exactly when the operator is scalar.

*Proof.* The range of a normal operator is the convex hull of its spectrum; the range is a single point exactly when the spectrum is a single point and the operator is a multiple of the identity.

**The reading.** The convexity is the reason the range is a usable invariant: a compact convex set in the plane is described by its boundary and by its support function, and both are read from the operator by a minimisation over the unit sphere.

## The Single Point

**Theorem.** The range of $T$ is a single point exactly when $T$ is a scalar operator, and the point is then the scalar.

*Proof.* If the range is the single point $\lambda$ then $\langle X,TX\rangle=\lambda\langle X,X\rangle$ for every $X$, so $T-\lambda\mathrm{I}$ is self-adjoint with zero form, hence zero; the converse is immediate.

**Corollary.** For the two-sided family the range is a point exactly when both parameters are scalars, and it is then the product of the two scalars.

*Proof.* The range of $T_{a,b}$ is a point exactly when $T_{a,b}$ is a scalar operator, which by the independence of the two parameters forces both to be scalar.

**Corollary.** The operators of point range are a two-dimensional family in the sixteen, and they are the fixed points of the adjoint action of the unitary group up to scalars.

*Proof.* The scalars form a line, and the operators of point range are exactly that line.

**The reading.** The point ranges are the scalars, and they are the only degenerate case. Every other operator has a two-dimensional range, because a segment already requires a non-scalar normal operator and a region requires a non-normal one.

## The Range of a Product

**Theorem.** The range of $T_{a,b}$ contains the four products $\lambda_i\mu_j$ of the eigenvalues of $a$ and of $b$, and it is contained in the convex hull of the products of the values of the ranges of $L_a$ and of $R_b$ when the two one-sided operators are normal.

*Proof.* The eigenvalues of the product are the pairwise products, and each lies in the range. For the containment, the one-sided operators commute and are simultaneously diagonalisable in the normal case, so the value of the product at a joint eigenvector is the product of the two values.

**Corollary.** For Hermitian parameters the product is Hermitian and its range is the segment between the smallest and the largest of the four products.

*Proof.* $T_{a,b}$ is self-adjoint by the adjoint computation, its eigenvalues are real and equal to the four products, and the range of a self-adjoint operator is the segment spanned by its extreme eigenvalues.

**Corollary.** For unitary parameters the product is unitary and its range lies in the closed unit disc, containing the four unimodular products.

*Proof.* A unitary operator preserves the form, so the values have modulus at most one, and the four products of unimodular eigenvalues lie on the circle.

**The reading.** The range of a product is governed by the spectra of the two parameters through their pairwise products, and its shape is governed by the two one-sided operators. The four numbers of the spectrum are always inside, the disc or the segment contains the rest, and nothing else about the range is visible from the two parameters.

## The Boundary

**Proposition.** A point of the boundary of the range that is an extreme point of the region is an approximate eigenvalue of the operator.

*Proof.* At an extreme boundary point the supporting line touches the range at that point; the maximisation of the real part over the unit sphere is attained at some element, and the variation of the element at the maximum gives the approximate eigenvector equation.

**Corollary.** For a normal operator every extreme boundary point is an eigenvalue, and the range is the polygon spanned by the spectrum.

*Proof.* The approximate eigenvalue equation is exact for a normal operator, and the extreme points are the extreme eigenvalues.

**Corollary.** The boundary of the range of a product with two spectrally regular parameters passes through the four products, and the region is the convex hull of the curve traced by the products of the one-sided values.

*Proof.* The four eigenvalues are extreme points, and the values at the joint eigenvectors are the products.

**The reading.** The boundary is where the form is extremal, and it is read by a maximisation. For the two-sided family the four eigenvalues are always on the boundary, and the rest of the boundary is the image of the sphere under the quadratic map attached to the pair.

## Further Reading

- [The Adjoints and the Polar Decomposition of an Operator](the-adjoints-and-the-polar-decomposition-of-an-operator.html), for the form with respect to which the range is taken.
- [The Spectrum of a Biquaternion](the-spectrum-of-a-biquaternion.html), for the eigenvalues entering the four products.
- [Operators Acting on Two Sides](operators-acting-on-two-sides.html), for the family whose range is computed.
- [The Four Ranks of the Two-Sided Operators](the-four-ranks-of-the-two-sided-operators.html), for the algebraic invariants that the range refines.
