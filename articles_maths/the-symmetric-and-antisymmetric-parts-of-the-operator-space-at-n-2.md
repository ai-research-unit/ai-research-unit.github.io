# __The Symmetric and Antisymmetric Parts of the Operator Space at $n=2$__

## Introduction

**Transposition is an involution of the matrix space, conjugation by it is an involution of the operator algebra, and the operator algebra splits into the sixteen-dimensional symmetric part and the sixteen-dimensional antisymmetric part, with the two-sided operator $T_{X,Y}$ symmetric exactly when $Y=X^{\mathsf T}$.**

The article defines the transposition operator, transports it to an involution of the endomorphism algebra, computes the two eigenspaces and their dimensions, determines which one-sided and two-sided operators lie in each part, compares the transposition involution with the adjoint, and reads the decomposition on the unitary and the self-adjoint operators. It assumes *The Adjoints and the Polar Decomposition of an Operator at $n=2$*, *The Two-Sided Operators and the Segre Cone at $n=2$* and *The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric at $n=2$*.

It follows the biquaternion article *The Endomorphisms of the Biquaternion Algebra* for the same involution on the eight real coordinates.

## The Transposition Operator

**Transposition is a conjugate-linear involution of the matrix space, and it is an isometry of the Hilbert–Schmidt form.**

**Definition.** Let $\tau(Z)=Z^{\mathsf T}$ be the transposition operator on the matrix space.

**Proposition.** The operator $\tau$ is conjugate-linear, involutive and an isometry: $\langle\tau Z,\tau W\rangle=\langle Z,W\rangle$.

**Proof.** Transposition reverses the order of a product and conjugates a scalar product, and applying it twice returns the matrix; the form of a product of transposes is the conjugate of the reversed form.

**Corollary.** The fixed points of $\tau$ are the symmetric matrices, and the anti-fixed points are the antisymmetric matrices.

**Proof.** A matrix equal to its transpose is symmetric, and one equal to minus its transpose is antisymmetric.

**Corollary.** The transposition operator is not complex-linear, so it is not an element of the endomorphism algebra.

**Proof.** The complex scalar $i$ is carried to $-i$ under transposition of a scalar product, which is conjugate-linearity.

## The Involution on the Operator Algebra

**Theorem.** The map $\theta(T)=\tau T\tau$ is an involutive automorphism of the endomorphism algebra, and it is complex-linear.

**Proof.** The two factors of the conjugation are conjugate-linear, so the composite is linear; and $\theta(TS)=\tau TS\tau=\tau T\tau\,\tau S\tau=\theta(T)\theta(S)$ because $\tau^{2}$ is the identity, so the map is an automorphism, and it is involutive for the same reason.

**Corollary.** The operator algebra splits as the direct sum of the two eigenspaces of $\theta$, of dimensions sixteen each.

**Proof.** An involution has the eigenvalues $+1$ and $-1$, and each eigenspace has half the dimension because the two projectors $\tfrac12(1\pm\theta)$ are complementary.

**Corollary.** The identity operator is symmetric, and the transposition operator composed with the identity is symmetric as an operator on the algebra.

**Proof.** The identity operator commutes with $\tau$, and $\tau$ is itself fixed by the conjugation when it is regarded as an operator.

## The Two Families

**Proposition.** The conjugate of a two-sided operator is $\theta(T_{X,Y})=T_{Y^{\mathsf T},X^{\mathsf T}}$.

**Proof.** Applying $\tau$ on both sides sends $Z$ to $(XZ^{\mathsf T}Y)^{\mathsf T}=Y^{\mathsf T}ZX^{\mathsf T}$.

**Corollary.** The two-sided operator $T_{X,Y}$ is symmetric exactly when $Y=X^{\mathsf T}$, and antisymmetric exactly when $Y=-X^{\mathsf T}$.

**Proof.** The conjugate is $T_{Y^{\mathsf T},X^{\mathsf T}}$, which equals $T_{X,Y}$ exactly when the two parameters agree as stated, and equals its negative in the other case.

**Corollary.** The left multiplication by $X$ is symmetric exactly when $X$ is symmetric, and the right multiplication by $Y$ is symmetric exactly when $Y$ is symmetric.

**Proof.** The left multiplication is the two-sided operator with the second parameter the identity, so the condition is $I=X^{\mathsf T}$; the right multiplication is the case of the first parameter the identity.

## The Relation with the Adjoint

**Proposition.** The transposition involution and the adjoint commute: $\theta(T^{*})=\theta(T)^{*}$.

**Proof.** Both are computed by conjugating and transposing the four-by-four matrix of the operator, and conjugation and transposition of a matrix commute with its conjugate transpose.

**Corollary.** The adjoint of a symmetric operator is symmetric, and the adjoint of an antisymmetric operator is antisymmetric.

**Proof.** The involution preserves the eigenspaces, and the adjoint is compatible with it.

**Corollary.** The symmetric self-adjoint operators are exactly the operators $T_{H,H}$ with $H$ Hermitian, a real space of dimension four.

**Proof.** A symmetric operator has $Y=X^{\mathsf T}$, and self-adjointness forces both parameters to be Hermitian; the Hermitian half has real dimension four.

## The Antisymmetric Part

**Proposition.** The antisymmetric operators are exactly those of the form $T_{X,-X^{\mathsf T}}$ together with the sums of such operators, and they form a Lie subalgebra.

**Proof.** The bracket of two antisymmetric operators is the difference of two products, each of which is symmetric, so the bracket is antisymmetric; the space is closed under the bracket.

**Corollary.** The commutator with the transposition operator is $[\tau,T]=(\theta(T)-T)\tau=-2T_{-}\tau$, so it measures the antisymmetric part.

**Proof.** Since $\tau T=\theta(T)\tau$, the commutator is $(\theta(T)-T)\tau$, and $\theta(T)-T$ is minus twice the antisymmetric part.

**Corollary.** The bracket of the antisymmetric part with the whole algebra preserves the antisymmetric part, so the antisymmetric part is an ideal for the bracket action.

**Proof.** The involution is an automorphism, so it acts on the bracket by the bracket of its actions, which preserves the two eigenspaces.

## The Two Halves inside the Operator Space

**Proposition.** The symmetric operators form a subalgebra of the endomorphism algebra, and the antisymmetric part is a module over it.

**Proof.** The product of two symmetric operators is symmetric because the involution is an automorphism, and the product of a symmetric with an antisymmetric operator is antisymmetric for the same reason.

**Corollary.** The symmetric part is the fixed algebra of the involution, and its unitary group is the group of operators that commute with transposition up to the involution.

**Proof.** The fixed algebra is by definition the symmetric part, and its unitary group consists of the unitaries fixed by the involution.

**Corollary.** The antisymmetric part is an ideal of the Lie algebra, since the bracket of an antisymmetric operator with any operator is antisymmetric.

**Proof.** The involution is an automorphism of the algebra and hence of the bracket, so it acts on a bracket by the brackets of its actions; the sign product of the two eigenspaces shows that a bracket with an antisymmetric factor stays antisymmetric.

**Corollary.** The dimension count is sixteen plus sixteen, matching the thirty-two real dimensions of the operator algebra.

**Proof.** The two eigenspaces are complex subspaces of dimension sixteen each, and their real dimensions add to thirty-two.

## Summary

Transposition is a conjugate-linear involution of the matrix space, and conjugation by it is an involution of the operator algebra splitting it into two parts of dimension sixteen each. The two-sided operator $T_{X,Y}$ is symmetric exactly when $Y=X^{\mathsf T}$ and antisymmetric exactly when $Y=-X^{\mathsf T}$, so the left and right multiplications are symmetric exactly when their parameters are symmetric.

The transposition involution commutes with the adjoint, the symmetric part is a subalgebra, and the antisymmetric part is a Lie subalgebra and a module over the symmetric one.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tau(Z)=Z^{\mathsf T}$ | the transposition operator |
| $\theta(T)=\tau T\tau$ | the involution of the operator algebra |
| $T_{X,Y}$ | the two-sided operator |
| $+1,-1$ | the two eigenspaces of the involution |
| $T^{*}$ | the adjoint for the Hilbert–Schmidt form |

## Further Reading

- Paul R. Halmos, *A Hilbert Space Problem Book* (Springer, 1982), for transposition and its operator consequences.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 2013), for symmetric and antisymmetric matrices.
- [The Adjoints and the Polar Decomposition of an Operator at $n=2$](the-adjoints-and-the-polar-decomposition-of-an-operator-at-n-2.html), for the adjoint compared here with transposition.
- [The Two-Sided Operators and the Segre Cone at $n=2$](the-two-sided-operators-and-the-segre-cone-at-n-2.html), for the two-sided operators classified here.
- [The Two Halves over $\mathbb{R}$: Symmetric and Antisymmetric at $n=2$](the-two-halves-over-r-symmetric-and-antisymmetric-at-n-2.html), for the same split on the matrices themselves.
