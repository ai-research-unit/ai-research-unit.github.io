# __The Length and the Two Ranks at $n=2$__

## Introduction

**An operator on the matrix space has a length, its Hilbert–Schmidt norm, and two ranks, the rank of the operator and the rank of the matrix it represents; for a two-sided operator the length is the product of the two lengths and the rank is the product of the two ranks.**

The article defines the length of an operator, computes it for the one-sided and the two-sided families, relates the length to the ranks, and shows how the two ranks of a two-sided operator are read from its two parameters. It assumes *The Two-Sided Operators and the Segre Cone at $n=2$*, *The One-Sided Operators at $n=2$* and *The Hilbert–Schmidt Form at $n=2$*.

It follows the biquaternion article *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra* for the four lengths of an element.

## The Length of an Operator

**The endomorphism algebra carries the Hilbert–Schmidt form, and its norm is the length of an operator.**

**Definition.** The **length** of an operator $T$ is $\|T\|=\bigl(\operatorname{tr}(T^{*}T)\bigr)^{1/2}$, the Hilbert–Schmidt norm computed on the sixteen real coordinates.

**Proposition.** The length is a norm on the endomorphism algebra, it is invariant under unitary conjugation, and it satisfies $\|T^{*}\|=\|T\|$.

**Proof.** The trace of $T^{*}T$ is a sum of squares of the sixteen real coordinates, so the length is the Euclidean norm in the real vector space; unitary conjugation preserves the trace of a product, and the adjoint changes nothing in the sum of squares.

**Corollary.** The length of the identity operator is two, the square root of the dimension of the matrix space.

**Proof.** The identity operator has the trace of $T^{*}T$ equal to four, the dimension of the space.

**Corollary.** The length is unchanged by the conjugation $T\mapsto U TU^{*}$ with $U$ unitary, so the length is a unitary invariant of the operator.

**Proof.** $(UTU^{*})^{*}(UTU^{*})=UT^{*}U^{*}UTU^{*}=UT^{*}TU^{*}$, whose trace is the trace of $T^{*}T$.

**Corollary.** The operators of length one form a compact manifold of real dimension thirty-one, the unit sphere of the endomorphism algebra.

**Proof.** The endomorphism algebra has real dimension thirty-two, and the unit sphere in a Euclidean space of that dimension is compact of dimension one less.

## The Length of a One-Sided Operator

**Proposition.** The length of the left multiplication $L_{X}$ is $\sqrt2$ times the length of $X$, and the same holds for the right multiplication.

**Proof.** The squared length of $L_{X}$ is the sum of the squared lengths of the images of the four matrix units, and each column of $X$ is counted twice, which gives twice the squared length of $X$.

**Corollary.** The left multiplications by the matrices of length one form a sphere of real dimension seven inside the endomorphism algebra.

**Proof.** The map $X\mapsto L_{X}$ is an injective linear map, and it scales the length by the constant factor $\sqrt2$.

**Corollary.** The left multiplications have the same length as the corresponding right multiplications, because transposition preserves the length.

**Proof.** The right multiplication by $X$ is the transpose of the left multiplication by $X^{\mathsf T}$, and the lengths of $X$ and of $X^{\mathsf T}$ agree.

## The Length of a Two-Sided Operator

**Theorem.** The length of the two-sided operator $T_{X,Y}$ is the product of the lengths of $X$ and $Y$.

**Proof.** In the basis of matrix units the operator $T_{X,Y}$ is the tensor product of $X$ with $Y^{\mathsf T}$, and the Hilbert–Schmidt norm of a tensor product is the product of the norms.

**Corollary.** The length is multiplicative over the composition of two-sided operators.

**Proof.** The composition multiplies the two parameters on each side, and the lengths multiply.

**Corollary.** The two-sided operator of length one built from two unit vectors is a rank-one operator of length one, and it is the projection onto a decomposable element composed with a functional.

**Proof.** The length is one times one, and the rank is one times one.

## The Two Ranks

**Proposition.** A two-sided operator has two ranks, the rank of the left parameter and the rank of the right parameter, and the rank of the operator is their product.

**Proof.** This is the rank formula of *The Two-Sided Operators and the Segre Cone at $n=2$*.

**Corollary.** The rank of an operator is at most the product of the two maximal ranks, which is four, and this is attained exactly by the invertible two-sided operators.

**Proof.** The product of two ranks is at most four, with equality exactly when both are two.

**Corollary.** An operator of rank one has exactly one pair of ranks, namely $(1,1)$, so its two parameters are both of rank one.

**Proof.** The product of two positive integers is one only for the pair $(1,1)$.

## The Length against the Ranks

**Proposition.** The squared length of an operator is the sum of the squares of its four singular values.

**Proof.** The operator is a $4\times4$ complex matrix in the basis of matrix units, and the trace of $T^{*}T$ is the sum of the squares of its singular values.

**Corollary.** The squared length lies between the square of the largest singular value and four times that square.

**Proof.** The sum of four nonnegative numbers lies between the largest of them and four times the largest.

**Corollary.** If all the singular values of an operator are at least one, then its rank is at most its squared length.

**Proof.** Each of the $r$ nonzero singular values contributes at least one to the sum of their squares.

## The Operator Norm

**Proposition.** For the length as the norm on the matrix space, the operator norm of $T_{X,Y}$ is the product of the operator norms of $X$ and $Y$, and the operator norm of $L_{X}$ is the operator norm of $X$.

**Proof.** The inequality $\|XZY\|\le\|X\|_{\mathrm{op}}\|Z\|\|Y\|_{\mathrm{op}}$ gives the upper bound, and taking $Z$ to be the rank-one map on the leading singular direction of $X$ and $Y$ attains it.

**Corollary.** The length of an operator lies between its operator norm and twice its operator norm, because the space has four dimensions.

**Proof.** The squared length is the sum of four squares of singular values, each at most the square of the largest.

**Corollary.** A one-sided operator is an isometry of the matrix space exactly when its parameter is unitary.

**Proof.** The operator norm of $L_{X}$ equals that of $X$, and the operator is an isometry exactly when the norm is one.

## The Extreme Cases

**Proposition.** The unitary operators of the matrix space are exactly the operators whose four singular values equal one, and their length is two.

**Proof.** A unitary operator preserves the Hilbert–Schmidt form, so all its singular values are one; conversely an operator with all singular values one is unitary, and the squared length is the sum of four ones.

**Corollary.** The length and the rank together do not determine unitarity: an operator of length two and rank four is unitary exactly when its four singular values are equal, and there are such operators with unequal singular values.

**Proof.** Squared length four means the four squares sum to four, which forces all of them to be one only when they are equal; for instance the singular values $\tfrac12,\tfrac12,\tfrac12,\tfrac{\sqrt{13}}{2}$ also give the sum four.

**Corollary.** The rank-one two-sided operators of length one form the product of two unit spheres, a compact set of real dimension six.

**Proof.** Each parameter runs over the unit sphere of real dimension three, and the product has dimension six.

## Summary

The length of an operator is its Hilbert–Schmidt norm, computed as the square root of the trace of $T^{*}T$. The one-sided operator $L_{X}$ has length $\sqrt2$ times the length of $X$, and the two-sided operator $T_{X,Y}$ has length the product of the two lengths.

The two ranks of a two-sided operator are the ranks of its two parameters, and the rank of the operator is their product. The length bounds the rank, and the unitary operators are exactly the operators of length two and rank four.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\|T\|$ | the length of an operator |
| $T^{*}$ | the adjoint for the Hilbert–Schmidt form |
| $L_{X}$, $R_{Y}$ | the one-sided operators |
| $T_{X,Y}$ | the two-sided operator |
| $\operatorname{rank}$ | the rank of an operator or a matrix |

## Further Reading

- Rajendra Bhatia, *Matrix Analysis* (Springer, 1997), for norms of operators and tensor products.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 2013), for singular values and ranks.
- [The Two-Sided Operators and the Segre Cone at $n=2$](the-two-sided-operators-and-the-segre-cone-at-n-2.html), for the rank formula used here.
- [The One-Sided Operators at $n=2$](the-one-sided-operators-at-n-2.html), for the one-sided lengths.
- [The Hilbert–Schmidt Form at $n=2$](the-hilbert-schmidt-form-at-n-2.html), for the form that defines the length.
