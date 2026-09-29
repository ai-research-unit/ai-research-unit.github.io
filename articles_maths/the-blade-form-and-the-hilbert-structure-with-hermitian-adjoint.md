
# __The Blade Form and the Hilbert Structure with Hermitian Adjoint__

## Introduction

A Clifford algebra is a finite-dimensional algebra, and like every finite-dimensional algebra it can be turned into a Euclidean space by declaring a basis orthonormal. The basis that the algebra itself provides is the basis of **blades**: the products of the vectors of an orthogonal basis, one for each subset of the basis. The scalar forms that this choice gives rise to are the ones that are invariant, in the sense that they are computed from the multiplication and the anti-involutions and do not depend on a further choice of basis inside the algebra.

Two scalar forms arise this way, and they are the two halves of the involutive structure. The **blade form** $\langle x,y\rangle = \mathrm{Sc}(x^{r}y)$ is built from reversion; the **Hermitian–Schmidt form** $\langle x,y\rangle_{\dagger} = \mathrm{Sc}(x^{\dagger}y)$ is built from the dagger, and specializes to the Clifford conjugation when $\sigma = \mathrm{id}$. Both have the blades orthogonal, so both are diagonal in the blade basis, and their diagonal entries differ only by the parity sign: this is how one and the same algebra carries the Euclidean structure of *Clifford Algebras in Finite Dimensions* and the indefinite structure that the geometric product requires. The **trace form** $T(x,y) = \operatorname{Tr}(m_{xy})$ is the third, the one that is intrinsic to the algebra as a Frobenius algebra and underlies the duality of *The Volume Element, Duality and the Hodge Star*.

This article treats the three forms as scalar forms on the algebra, their diagonalization by the blades, their definiteness in the two definite cases, the trace form and the Frobenius structure, the adjoints of left and right multiplication with respect to them, and the Hilbert structure that the Euclidean form induces, including the boundedness of the multiplication operators. The algebra-valued forms are *Hermitian Forms on a Clifford Algebra with Hermitian Adjoint*; the operator on the algebra is *The Hermitian Sandwich on a Clifford Algebra with Hermitian Adjoint*; the operator on a Clifford module, where the same form appears on the spinor side, is *Hermitian Clifford Modules with Hermitian Adjoint* and *The Adjoint of the One-Sided Action with Hermitian Adjoint*; and the completion in infinite dimension, together with the canonical anticommutation relations, is *Infinite-Dimensional Clifford Algebras and CAR with Inner Conjugation*.

## The Blade Form

### Definition

**Definition.** Let $(e_1,\dots,e_n)$ be an orthogonal basis of the quadratic space $(V,q)$, with $e_i^{2} = q(e_i) \in A$, and let $e_I = e_{i_1}\cdots e_{i_k}$ for $I = \{i_1 < \dots < i_k\}$ be the corresponding blades. The **blade form** of the algebra is

$$
\langle x,y\rangle = \mathrm{Sc}\bigl(x^{r}y\bigr),
$$

the scalar part of reversion in the first argument times the second. It is symmetric, $\langle x,y\rangle = \langle y,x\rangle$, and bilinear over the base.

**Remark (why reversion, and not the dagger).** The scalar part is the coefficient of the unit and is invariant under reversion, so with $x = \sum_I a_I e_I$ and $y = \sum_I b_I e_I$,

$$
\langle x,y\rangle = \sum_I a_I\,\bigl(e_{i_1}^{2}\cdots e_{i_k}^{2}\bigr)\, b_I ,
$$

the diagonal form of the blade basis twisted by the signature of the quadratic form. Reversion fixes the individual vectors, which is what makes the twist the plain product of the $e_i^{2}$; the dagger would insert the parity sign, as the next section shows.

### The Blades are Orthogonal

**Proposition.** The blades are orthogonal for the blade form and

$$
\langle e_I,e_J\rangle = \Bigl(\prod_{i\in I} e_i^{2}\Bigr)\,\delta_{IJ} .
$$

**Proof.** For a blade of degree $k$, reversion acts by $e_I^{r} = (-1)^{k(k-1)/2}e_I$. Then

$$
e_I^{r}e_I = (-1)^{k(k-1)/2}\,e_I^{2} = (-1)^{k(k-1)/2}\cdot(-1)^{k(k-1)/2}\prod_{i\in I}e_i^{2} = \prod_{i\in I}e_i^{2},
$$

a scalar, so $\langle e_I,e_I\rangle = \prod_{i\in I}e_i^{2}$; and for $I \neq J$ the product $e_Ie_J$ is a blade of positive degree, whose scalar part vanishes.

**Corollary (non-degeneracy).** The blade form is non-degenerate exactly when every $\prod_{i\in I}e_i^{2}$ is invertible, which for a form on a free module over a field means exactly that $q$ is non-degenerate. For a degenerate form the radical of the blade form is the even part of the radical of $q$ in the sense of *Degenerate Clifford Algebras and the Radical*.

### Positive Definiteness and the Euclidean Structure

**Proposition.** Let $A = \mathbb{R}$. The blade form is positive definite exactly when the quadratic form is positive definite. Then the blades form an orthonormal basis of $\mathrm{Cl}(V,q)$, the grade projections are orthogonal, and

$$
\langle x,x\rangle = \sum_I a_I^{2} > 0 \quad \text{for } x \neq 0 .
$$

**Proof.** In an orthonormal basis of a positive definite form every $e_i^{2} = 1$, so $\prod_{i\in I}e_i^{2} = 1$ and the diagonal of the preceding proposition is the identity.

**Remark (the Euclidean structure).** This is the form in which the Clifford algebra is the Euclidean space of *Clifford Algebras in Finite Dimensions*, and the blades of an orthonormal basis are its orthonormal frame. Over $\mathbb{C}$ the corresponding positive structure uses the conjugate reversion, $\langle x,y\rangle = \mathrm{Sc}(x^{r,\sigma}y) = \sum_I \bar a_I b_I$, which is positive definite Hermitian; the two are related by the coefficient involution and are the two real forms of the same complex form.

### The Trace Form and the Frobenius Structure

**Proposition.** Let $m_x$ denote left multiplication by $x$ and $\operatorname{Tr}$ its trace on the algebra. Then

$$
\operatorname{Tr}(m_z) = \dim_A \mathrm{Cl}(V,q)\cdot \mathrm{Sc}(z) = 2^{n}\,\mathrm{Sc}(z),
$$

and consequently the **trace form** satisfies

$$
T(x,y) = \operatorname{Tr}(m_{xy}) = 2^{n}\,\mathrm{Sc}(xy) = 2^{n}\,\langle x^{r},y\rangle .
$$

**Proof.** In the blade basis, left multiplication by $e_I$ sends $e_J$ to $\pm e_{I\triangle J}$, a blade of degree $|I|+|J|-2|I\cap J|$; this is $e_J$ again only when $I = \emptyset$. Hence $\operatorname{Tr}(m_{e_I}) = 0$ for $I \neq \emptyset$ and $\operatorname{Tr}(m_1) = 2^{n}$, and the statement follows by linearity.

**Corollary.** $T$ is symmetric, $T(x,y) = T(y,x)$, because $\operatorname{Tr}(m_{xy}) = \operatorname{Tr}(m_y m_x) = \operatorname{Tr}(m_{yx})$, and it is associative in the sense $T(xy,z) = T(x,yz)$, because $m_{(xy)z} = m_x m_y m_z$ has the same trace as $m_{x(yz)}$. So $(\mathrm{Cl}(V,q), T)$ is a **symmetric Frobenius algebra**, and $T$ is non-degenerate exactly when the algebra is semisimple, which holds for a non-degenerate form over a field of characteristic not two.

**Remark (the dual basis).** The blade form identifies the algebra with its dual, and the dual basis of the blades is $\check e_I = \bigl(\prod_{i\in I}e_i^{2}\bigr)^{-1}e_I$; this is the duality used in *The Volume Element, Duality and the Hodge Star*, and it is the reason the trace form is the pairing that pairs the algebra with its dual.

## The Two Signatures

### Reversion against Clifford Conjugation

**Proposition.** The scalar form built from a general anti-involution $c$ is $\langle x,y\rangle_c = \mathrm{Sc}(c(x)y)$, and on the blades

$$
\mathrm{Sc}\bigl(x^{r}y\bigr) = \sum_I \Bigl(\prod_{i\in I}e_i^{2}\Bigr)a_Ib_I,
\qquad
\mathrm{Sc}\bigl(x^{\dagger}y\bigr) = \sum_I (-1)^{|I|}\Bigl(\prod_{i\in I}e_i^{2}\Bigr)a_Ib_I .
$$

So the form of the dagger is the blade form with the parity sign inserted; its Gram matrix is diagonal with entries $\pm 1$; and it is positive definite exactly when the quadratic form is **negative** definite, which is the statement, on the scalar level, that the choice between reversion and the dagger is a choice of signature.

**Proof.** $x^{\dagger} = \sigma(\alpha(x^{r}))$ and $\sigma$ acts only on the coefficients, while $\alpha(e_I) = (-1)^{|I|}e_I$; then $x^{\dagger}e_I$ matches the computation of the blade form up to the sign $(-1)^{|I|}$.

### The Adjoint of Left Multiplication

**Theorem.** Let $L_x$ and $R_x$ denote left and right multiplication by $x$. With respect to the blade form,

$$
\langle L_xy,z\rangle = \langle y, L_{x^{r}}z\rangle, \qquad \langle R_xy,z\rangle = \langle y, R_{x^{r}}z\rangle,
$$

so the adjoint of left or right multiplication by $x$ is multiplication by $x^{r}$; and with respect to the form of the dagger,

$$
\bigl(L_xy,z\bigr)_{\dagger} = \bigl(y, L_{x^{\dagger}}z\bigr)_{\dagger}, \qquad \bigl(R_xy,z\bigr)_{\dagger} = \bigl(y, R_{x^{\dagger}}z\bigr)_{\dagger},
$$

so the adjoint there is multiplication by the dagger.

**Proof.** Let $\langle x,y\rangle = \mathrm{Sc}(x^{r}y)$. Then $\langle L_xy,z\rangle = \mathrm{Sc}((xy)^{r}z) = \mathrm{Sc}(y^{r}x^{r}z) = \langle y, x^{r}z\rangle$; the right-handed statement is the same with the order reversed. The dagger case is identical with $x^{\dagger}$ in place of $x^{r}$, using that the dagger is an anti-involution.

**Corollary (the operator version of the sandwich).** Substituting $y = 1$ in the dagger case, the adjoint of left multiplication is computed by $\Theta_x(1) = \mathrm{Sc}(x\,x^{\dagger})$, which is the diagonal of the dagger form at $x^{\dagger}$, the identity of *Hermitian Forms on a Clifford Algebra with Hermitian Adjoint*. On a Clifford module the same computation gives the adjoint of the one-sided action, and that is *The Adjoint of the One-Sided Action with Hermitian Adjoint*.

## The Hilbert Structure

### The Euclidean Form and the Completion

**Definition.** The **Euclidean form** of the algebra is

$$
(x,y) = \sum_I a_I\,b_I ,
$$

the form in which the blades of an orthonormal basis are an orthonormal basis; it is positive definite over $\mathbb{R}$ in the sense of the Euclidean structure above, and sesquilinear, $(x,ay) = a(x,y)$, $(\sigma(a)x,y) = \sigma(a)(x,y)$, over a complex base.

**Proposition.** Over a definite real form the Euclidean form makes $\mathrm{Cl}(V,q)$ a finite-dimensional Hilbert space; its completion in infinite dimension is the Hilbert space on which the canonical anticommutation relations are represented, in *Infinite-Dimensional Clifford Algebras and CAR with Inner Conjugation*. The blade form and the form of the dagger are the Euclidean form twisted by the signature signs, so all three are unitarily equivalent after a diagonal change of basis; the distinction between them is the distinction between the geometries and not between the topological spaces.

### Boundedness of the Multiplication Operators

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

**Remark (the norm is not submultiplicative).** The constant $2^{n/2}$ is not an accident of the proof: the Euclidean norm of a Clifford algebra is not submultiplicative. In $\mathrm{Cl}_{2,0}$ the maximum of $\|xy\|/(\|x\|\|y\|)$ over the algebra is between $1$ and $\sqrt 2$, attained inside the algebra and not on the blades. This is the reason the algebra is completed as a Hilbert space with a von Neumann or a Clifford algebra structure rather than as a Banach algebra in this norm.

### Cauchy–Schwarz, Positivity and the Cone

**Proposition (Cauchy–Schwarz).** For the Euclidean form, $|(x,y)|^{2} \le (x,x)(y,y)$ with equality exactly when $x$ and $y$ are proportional.

**Proof.** The form is positive definite, so the standard proof applies; equality is the case of linear dependence.

**Corollary.** The set $\{x : (x,x) \le 1\}$ is the closed unit ball of the algebra and is compact, and the set $\{x : x = y^{\dagger}y\}$ is the positive cone of *Positivity and the Hermitian Cone of a Clifford Algebra with Hermitian Adjoint*; in dimension three with the definite form the latter is the cone over the sphere of radius $1/2$ that appears in *Spin Factors and the Clifford Envelope with Inner Conjugation*.

## Summary

A Clifford algebra carries three invariant scalar forms. The **blade form** $\langle x,y\rangle = \mathrm{Sc}(x^{r}y)$ has the blades of an orthonormal basis orthogonal, with $\langle e_I,e_I\rangle = \prod_{i\in I}e_i^{2}$, is non-degenerate exactly when $q$ is, and is positive definite exactly when $q$ is positive definite; it is the Euclidean structure of the algebra. The **Hermitian–Schmidt form** $\mathrm{Sc}(x^{\dagger}y)$ is the same computation with the parity sign inserted, so its Gram matrix is diagonal with entries $\pm1$ and it is positive definite exactly when $q$ is negative definite: the choice between reversion and the dagger is a choice of signature on the scalar level. The **trace form** $T(x,y) = \operatorname{Tr}(m_{xy}) = 2^{n}\mathrm{Sc}(xy)$ makes the algebra a symmetric **Frobenius algebra**, non-degenerate exactly when the algebra is semisimple, and it is the pairing used for duality.

The adjoint of left or right multiplication is multiplication by the corresponding anti-involution: with respect to the blade form it is $x^{r}$, with respect to the dagger form it is $x^{\dagger}$. The latter is the scalar form of the identity $\Theta_x(1) = \mathrm{Sc}(xx^{\dagger})$, and its module version is the adjoint of the one-sided action. Over a definite real form the Euclidean form makes the algebra a Hilbert space, and multiplication is bounded with $\|xy\| \le 2^{n/2}\|x\|\|y\|$, the constant being the price of the non-submultiplicativity of the norm; the completion in infinite dimension carries the canonical anticommutation relations.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $e_I$, $i_1 < \dots < i_k$ | Blade of the orthonormal basis |
| $\mathrm{Sc}(x)$ | Scalar part, the coefficient of $1$ |
| $\langle x,y\rangle = \mathrm{Sc}(x^{r}y)$ | Blade form |
| $\mathrm{Sc}(x^{\dagger}y)$ | Form of the dagger, the parity twist of the blade form |
| $(x,y) = \sum_I a_Ib_I$ | Euclidean form, blades orthonormal |
| $T(x,y) = \operatorname{Tr}(m_{xy})$ | Trace form |
| $m_x$, $L_x$, $R_x$ | Multiplication by $x$, on the left and on the right |
| $\check e_I = (\prod_{i\in I}e_i^{2})^{-1}e_I$ | Dual blade for the blade form |
| $\|x\| = (x,x)^{1/2}$ | Euclidean norm |

## Further Reading

- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced Mathematics 50 (Cambridge University Press, 1995), for the scalar and trace forms of a Clifford algebra.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the Hermitian structure of the spinor bundle and the positive definite spinor form.
- Frank W. Warner, *Foundations of Differentiable Manifolds and Lie Groups*, Graduate Texts in Mathematics 94 (Springer, 1983), for the Frobenius algebra and the trace form of a finite-dimensional algebra.
- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for the trace form, the discriminant and the separability criterion.
- Ola Bratteli and Derek W. Robinson, *Operator Algebras and Quantum Statistical Mechanics II*, Texts and Monographs in Physics (Springer, 2nd ed. 1997), for the Clifford algebra of a Hilbert space, the completion and the canonical anticommutation relations.
