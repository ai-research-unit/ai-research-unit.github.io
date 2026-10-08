# __The Euclidean Form, the Norm and the Completion on a Clifford Algebra__

## Introduction

A Clifford algebra over a definite real form can be made a Euclidean space by declaring the blades orthonormal, and this article is the Part II half of that construction: it owns the Euclidean form on the completion, the boundedness of the multiplication operators, and the Cauchy–Schwarz inequality with the compactness of the unit ball.

The algebraic half is in Part I. The three invariant scalar forms — the blade form, the Hermitian–Schmidt form and the trace form — their diagonalisation by the blades, their definiteness and the adjoints of left and right multiplication with respect to them are in *The Blade Form and the Hermitian Structure with Hermitian Adjoint*. What is added here is the metric layer: the form as a scalar product on a Hilbert space, the norm and its failure to be submultiplicative, and the completion.

The conventions are those of *The Blade Form and the Hermitian Structure with Hermitian Adjoint*: $\mathrm{Cl}(V,q)$ is the Clifford algebra of a quadratic form $q$, the $e_I$ are the blades of an orthogonal basis, and $\mathrm{Sc}$ is the scalar part.

## The Euclidean Form and the Completion

**Definition.** The **Euclidean form** of the algebra is

$$
(x,y) = \sum_I a_I\,b_I ,
$$

the form in which the blades of an orthonormal basis are an orthonormal basis. Over a real base with $q$ positive definite it is the blade form of *The Blade Form and the Hermitian Structure with Hermitian Adjoint*, and $\langle x,x\rangle = \sum_I a_I^{2} > 0$; over a complex base the same positive structure is the conjugate-reversion form $\sum_I \bar a_I b_I = \mathrm{Sc}(x^{r,\sigma}y)$, $\sigma$-sesquilinear and positive definite.

**Proposition.** Over a real base with $q$ positive definite the Euclidean form makes $\mathrm{Cl}(V,q)$ a finite-dimensional Hilbert space; its completion in infinite dimension is the Hilbert space on which the canonical anticommutation relations are represented, in *Infinite-Dimensional Clifford Algebras and CAR with Inner Conjugation*. The blade form and the form of the dagger are the Euclidean form twisted by the signature signs, so all three are unitarily equivalent after a diagonal change of basis; the distinction between them is the distinction between the geometries and not between the topological spaces.

## Boundedness of the Multiplication Operators

**Proposition.** With the Euclidean norm $\|x\| = (x,x)^{1/2}$, every $L_x$ and $R_x$ is bounded, and

$$
\|xy\| \le 2^{n/2}\,\|x\|\,\|y\| .
$$

For $x$ a blade the inequality holds with constant $1$: $\|e_Iy\| = \|y\|$, since left multiplication by a blade permutes the blade basis up to signs.

**Proof.** Each $e_I$ acts by a signed permutation of the blade basis, so $\|L_{e_I}\|_{\mathrm{op}} = 1$. For general $x = \sum_I a_Ie_I$, subadditivity of the operator norm gives

$$
\|L_x\|_{\mathrm{op}} \le \sum_I |a_I| \le \Bigl(2^{n}\sum_I|a_I|^{2}\Bigr)^{1/2} = 2^{n/2}\|x\| ,
$$

by Cauchy–Schwarz on the $2^{n}$ coefficients. Then $\|xy\| = \|L_xy\| \le \|L_x\|_{\mathrm{op}}\|y\|$.

**Remark (the norm is not submultiplicative).** The constant $2^{n/2}$ is not an accident of the proof: the Euclidean norm of a Clifford algebra is not submultiplicative. The bound $2^{n/2}$ is a Cauchy–Schwarz estimate: the ratio $\|xy\|/(\|x\|\|y\|)$ is at least $2^{1/2}$ in every dimension, the element $\tfrac12(1 + e_1)$, which is not a blade, satisfying $x^{2}=x$ with $\|x\|=2^{-1/2}$; in $\mathrm{Cl}_{1,0}$, where the bound equals $2^{1/2}$, this value is the bound itself, while in the higher dimensions the bound is not known to be attained. This is the reason the algebra is completed as a Hilbert space with a von Neumann or a Clifford algebra structure rather than as a Banach algebra in this norm.

## Cauchy–Schwarz, Positivity and the Cone

**Proposition (Cauchy–Schwarz).** For the Euclidean form, $|(x,y)|^{2} \le (x,x)(y,y)$ with equality exactly when $x$ and $y$ are proportional.

**Proof.** The form is positive definite, so the standard proof applies; equality is the case of linear dependence.

**Corollary.** The set $\{x : (x,x) \le 1\}$ is the closed unit ball of the algebra and is compact, and the set $\{x : x = y^{\dagger}y\}$ is the positive cone of *Positivity and the Hermitian Cone of a Hermitian Algebra with Hermitian Adjoint*; in dimension three with the definite form the latter is the cone over the sphere of radius $1/2$ that appears in *Spin Factors and the Clifford Envelope with Inner Conjugation*.

## Summary

Over a real base with $q$ positive definite the **Euclidean form** $(x,y)=\sum_I a_I b_I$, in which the blades are orthonormal, makes $\mathrm{Cl}(V,q)$ a finite-dimensional Hilbert space, and its completion in infinite dimension is the Hilbert space on which the canonical anticommutation relations are represented. With the Euclidean norm every left and right multiplication is bounded, with $\|xy\|\le 2^{n/2}\|x\|\|y\|$ — a constant that is the price of the failure of the norm to be submultiplicative, and the reason the algebra is completed as a Hilbert space rather than as a Banach algebra in this norm. **Cauchy–Schwarz** holds for the Euclidean form, the set $\{x:(x,x)\le1\}$ is the compact closed unit ball, and $\{x:x=y^{\dagger}y\}$ is the positive cone. The algebraic forms, their definiteness and the adjoints of the multiplications are in *The Blade Form and the Hermitian Structure with Hermitian Adjoint*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm{Cl}(V,q)$ | Clifford algebra of a quadratic form $q$ |
| $e_I$, $i_1 < \dots < i_k$ | Blade of an orthogonal basis |
| $\mathrm{Sc}(x)$ | Scalar part, the coefficient of $1$ |
| $(x,y) = \sum_I a_Ib_I$ | Euclidean form, blades orthonormal |
| $\|x\| = (x,x)^{1/2}$ | Euclidean norm |
| $L_x$, $R_x$ | Left and right multiplication by $x$ |
| $2^{n/2}$ | Bound constant in $\|xy\| \le 2^{n/2}\|x\|\|y\|$ |

## Further Reading

- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the Hermitian structure of the spinor bundle and the positive definite spinor form.
- Ola Bratteli and Derek W. Robinson, *Operator Algebras and Quantum Statistical Mechanics II*, Texts and Monographs in Physics (Springer, 2nd ed. 1997), for the Clifford algebra of a Hilbert space, the completion and the canonical anticommutation relations.
- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for the trace form and the separability criterion.
