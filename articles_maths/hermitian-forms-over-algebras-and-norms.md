# __Hermitian Forms over Algebras and Norms__

## Introduction

The degree-2 structure of an algebra with an involution is carried by its **norm**: the quadratic map $N(x) = xx^{*}$, whose polarisation is the trace form of the involution. The norm turns the algebra into a space with a quadratic form, and the two operations interact: the norm is multiplicative precisely for the algebras that the quadratic form makes into composition algebras, and the polarisation of the norm is the trace form of *Polarisation and the Hermitian Square*.

This article computes the norm and its polarisation for the four algebras of the corpus — the field, the quaternion algebra, the matrix algebra and the Clifford algebra — and draws the boundary that the word **norm** needs in this layer. Three facts are the substance. On a quaternion algebra the norm $N(x) = x\bar{x}$ is a multiplicative quadratic form whose polarisation is the trace form: the quaternion algebra is a composition algebra, and the norm form is the classical four-dimensional form of the norm-one group. On a central simple algebra the **reduced norm** plays the same role with the reduced trace; on $M_n$ it is the determinant, and its polarisation is the trace form $\tau(X\operatorname{adj}(Y))$ — a form distinct from the Hermitian form $\tau(XY^{*})$, which is not the polarisation of any multiplicative norm. And on a Clifford algebra the norm $x^{*}x$ is a quadratic form which is multiplicative on the versors of the spin group and fails on the general element from dimension three on, which is the algebraic reason the Clifford norm form is not a composition form.

The algebraic norm is valued in the base; it becomes the topological norm, a distance and a completion, only when it is **selected** so that its values are positive reals, and that selection is the passage to *The Norm Defined by a Form* and to Part II. The bilinear original of the whole article is *Quadratic Forms over Algebras and Norms*. Throughout, $A$ is a finite-dimensional $R$-algebra with a $\varsigma$-semilinear involution $*$, $N(x) = xx^{*}$ is the norm map, and the polarisation of a quadratic form $Q$ is $B(x,y) = \tfrac{1}{2}\bigl(Q(x+y) - Q(x) - Q(y)\bigr)$ with $2$ invertible in the fixed ring.

## The Norm Map and Its Polarisation

**Definition.** The **norm map** of the algebra is $N(x) = xx^{*}$, valued in the fixed ring when $x^{*}x = xx^{*}$, and the **trace form** of the involution is

$$
\langle x, y \rangle = \tfrac{1}{2}\bigl(N(x+y) - N(x) - N(y)\bigr) = \tfrac{1}{2}\bigl(xy^{*} + yx^{*}\bigr) .
$$

**Proposition.** The polarisation of the norm map is the bilinear map $\langle x,y\rangle = \tfrac{1}{2}(xy^{*}+yx^{*})$, and the **trace form** of the involution is its functional image $\varphi(\langle x,y\rangle)$, which is symmetric and $R^{\varsigma}$-bilinear.

**Proof.** Expand $N(x+y) = (x+y)(x^{*}+y^{*}) = xx^{*} + xy^{*} + yx^{*} + yy^{*}$ and subtract $N(x) + N(y)$; the result is $xy^{*} + yx^{*}$, whose $R$-linearity is clear. The functional image $\varphi(xy^{*}+yx^{*})$ is symmetric because the two products are exchanged by the involution and $\varphi$ is $\varsigma$-linear.

**Corollary.** The diagonal of the *form* and the norm map are related by $q(x) = \varphi(x^{*}x)$; for a cyclic functional, in particular for the trace form $\varphi = \tau$, the two products $x^{*}x$ and $xx^{*}$ have the same functional and the diagonal is the functional of the norm, $q(x) = \varphi(N(x))$. A non-cyclic functional sees only $x^{*}x$, and then the trace form $\varphi(xy^{*}+yx^{*})$ of the involution and the trace form $h_{\mathrm{tr}}(x,y) = h(x,y)+h(y,x)$ of *Polarisation and the Hermitian Square* differ.

## The Quaternion Norm

Let $A = (\alpha,\beta)_{R}$ be the quaternion algebra with basis $1, i, j, k = ij$, $i^{2} = \alpha$, $j^{2} = \beta$, and the conjugation $\bar{x} = a - bi - cj - dk$ for $x = a + bi + cj + dk$.

**Proposition.** The norm $N(x) = x\bar{x}$ is the quadratic form

$$
N(x) = a^{2} - \alpha b^{2} - \beta c^{2} + \alpha\beta d^{2},
$$

and it is **multiplicative**: $N(xy) = N(x)N(y)$ for all $x, y$.

**Proof.** $x\bar{x} = a^{2} - b^{2}i^{2} - c^{2}j^{2} - d^{2}k^{2}$ because the cross terms cancel pairwise by the anticommutation of $i, j, k$; with $i^{2} = \alpha$, $j^{2} = \beta$ and $k^{2} = -\alpha\beta$ this is the displayed form. For multiplicativity, $N(xy) = xy\,\overline{xy} = xy\bar{y}\bar{x} = xN(y)\bar{x}$ because the conjugation is an anti-automorphism; $N(y)$ is central, so $xN(y)\bar{x} = N(y)x\bar{x} = N(x)N(y)$.

**Corollary.** The polarisation of the quaternion norm is the **trace form** $\langle x,y\rangle = \tfrac{1}{2}(x\bar{y} + y\bar{x})$, and over $\mathbb{R}$ with $\alpha = \beta = -1$ the norm is the positive definite form $a^{2}+b^{2}+c^{2}+d^{2}$ of $\mathbb{H}$, whose norm-one group is $\{x : N(x) = 1\}$, the compact group $\mathrm{SU}(2)$.

The quaternion algebra is a composition algebra because its norm is multiplicative, and the same is true of the octonion algebra, with the norm of the split and the definite quaternion algebras differing by the signs of the form; the bilinear counterparts over a general field are *Quadratic Forms over Algebras and Norms*.

## The Reduced Norm of a Central Simple Algebra

**Definition.** For a central simple $R$-algebra $A$ the **reduced norm** $N = \operatorname{Nrd}$ is the multiplicative polynomial map defined by the determinant of the regular representation, and the **reduced trace** $T = \operatorname{Trd}$ is its polarisation.

**Proposition.** The reduced norm is multiplicative, $N(xy) = N(x)N(y)$. For an algebra of **degree two** — a quaternion algebra, $\mathsf{M}_2$, or the biquaternion algebra — the reduced norm is a quadratic form and its polarisation is the bilinear form

$$
B(x,y) = \tfrac{1}{2}\bigl(N(x+y) - N(x) - N(y)\bigr) = T\bigl(x\,\operatorname{adj}(y)\bigr),
$$

the reduced trace against the adjugate. It is **not** the Hermitian form $h(x,y) = T(xy^{*})$. For degree $n \geq 3$ the reduced norm is a form of degree $n$ and its full polarisation is $n$-linear, of which $T(x\operatorname{adj}(y))$ is only the quadratic part.

**Proof.** Multiplicativity is the multiplicativity of the determinant. For the polarisation on $\mathsf{M}_2$, $\det(X+Y) = \det X + \det Y + \tau(X\operatorname{adj}Y)$ directly; for $n \geq 3$ the expansion $\det(X+Y) = \det X + \sum_{ij}X_{ij}\operatorname{adj}(Y)_{ji} + \dots$ has the higher-degree terms that the dots conceal. The last clause is the identity of the two quadratic forms on $\mathsf{M}_2$ checked below.

**Remark.** The two forms are genuinely different in the layer, and the difference is the whole point of the degree-2 structure. On $\mathsf{M}_2$ with $X = E_{11}$ and $Y = E_{22}$ the Hermitian form gives $h(X,Y) = \tau(XY^{*}) = 0$ while the polarisation of the determinant gives $B(X,Y) = 1$: the Hermitian form sees the two matrices as orthogonal, the norm form does not. A Hermitian form is a degree-2 structure *chosen* on the algebra; the reduced norm is a degree-2 structure *given* by the algebra. The two coincide only in the algebras in which the adjugate is the dagger, that is, in the dimensions where the inverse is the conjugate transpose.

**Proposition.** For an involution of the first kind the reduced norm is invariant, $N(x^{*}) = N(x)$, and the norm form is quadratic; for an involution of the second kind it is twisted, $N(x^{*}) = \varsigma(N(x))$, and the norm form is Hermitian in the sense of *The Sesquilinear Form and the Conjugation*.

**Proof.** Read the determinant of the adjoint: $N(x^{*}) = \det(x^{*}) = \det(x)$ for a first-kind involution acting on the matrix algebra, and $\det(x^{*}) = \varsigma(\det x)$ when the involution twists the scalars.

## The Norm of a Clifford Algebra

Let $\mathrm{Cl}(V,q)$ carry the dagger of *Hermitian Algebras*, $x^{\dagger} = \sigma(\alpha(x^{r}))$.

**Definition.** The **norm** of $x$ is $x^{\dagger}x$ and the **norm form** is its scalar part,

$$
N(x) = \operatorname{Sc}(x^{\dagger}x) = \sum_{I} (-1)^{|I|}\Bigl(\prod_{i\in I}e_{i}^{2}\Bigr)a_{I}^{2},
$$

the parity twist of the **blade form** $\operatorname{Sc}(x^{r}y)$ of *The Blade Form and the Hermitian Structure with Hermitian Adjoint*, whose blades are orthogonal.

**Proposition.** The norm form is definite exactly in the extreme cases, positive definite when $q$ is **negative** definite, because the dagger inserts the parity sign; and it is **not** multiplicative from dimension three on: $N(x) = N(y) = 1$ but $N(xy) = -3$ for the elements $x = y = 1 + e_{1} + e_{23}$ of $\mathrm{Cl}_{3,0}$.

**Proof.** The diagonal is the computation of *The Blade Form and the Hermitian Structure with Hermitian Adjoint*, $\operatorname{Sc}(x^{\dagger}y) = \sum_{I}(-1)^{|I|}(\prod_{i\in I}e_{i}^{2})a_{I}b_{I}$; the coefficients $(-1)^{|I|}\prod_{i\in I}e_{i}^{2}$ are $\pm1$, and they are all $+1$ exactly when every $e_{i}^{2} = -1$, that is when $q$ is negative definite. For the failure, in $\mathrm{Cl}_{3,0}$ the element $x = 1 + e_{1} + e_{23}$ has $x^{\dagger}x = 1 - 2e_{123}$, so $N(x) = 1$; squaring, $x^{2} = 1 + 2e_{1} + 2e_{23} + 2e_{123}$, and $N(x^{2}) = 1 - 4 - 4 + 4 = -3$ while $N(x)^{2} = 1$. The multiplicativity holds in dimension two, where the algebra is the quaternion algebra or $\mathsf{M}_2$, and on the versors below.

**Corollary.** The Clifford algebra is not a composition algebra in the norm of the dagger; the norm is multiplicative on the **versors**, $N(xy) = N(x)N(y)$ for $x, y$ in the Clifford group, which is the multiplicative structure of *Versors, Rotors and the Sandwich Action with Signed Inner Conjugation*, and the failure on the general element is the algebraic reason the norm form of a Clifford algebra is a quadratic form *with* a group rather than a composition form.

## The Algebraic Norm and the Topological Norm

The word norm carries two meanings in the corpus, and the boundary is a rule, not a convention. The **algebraic norm** of this article is a map into the base ring, $N : A \to R$, and it is algebra: forms, quadratic maps, polarisations and their groups. The **topological norm** is the selection of a form's values as positive real numbers, and only the selection makes a distance, a unit ball, a boundedness and a completion. The selection is *The Norm Defined by a Form* and *The Completion of a Sesqualgebra with a Form* in Part II, and the criterion is that a norm becomes topological when it is chosen so that its values bound a metric — never because its formula contains a square.

## Examples

### The Field

For $A = \mathbb{C}$ with the conjugation the norm is $N(z) = |z|^{2}$, multiplicative by the multiplicativity of the modulus, with trace form $\langle z,w\rangle = \operatorname{Re}(z\bar{w})$, the Euclidean plane form of the field.

### The Matrices

On $M_2(\mathbb{C})$ the reduced norm is the determinant, its polarisation is $B(X,Y) = \tau(X\operatorname{adj}(Y))$, and the Hermitian form of the dagger is the Frobenius form $\tau(XY^{\dagger})$; the two differ, as the remark above shows. At $n=2$ the difference is visible already on the identity:

$$
X=\begin{pmatrix}1&2\\3&4\end{pmatrix},\qquad Y=\begin{pmatrix}1&0\\0&0\end{pmatrix},\qquad \operatorname{adj}Y=\begin{pmatrix}0&0\\0&1\end{pmatrix},\qquad \tau(X\operatorname{adj}Y)=4\neq1=\tau(XY^{\dagger}) .
$$

### The Biquaternion Algebra

On $\mathbb{B} = M_2(\mathbb{C})$ the reduced norm is the determinant and the norm form of the dagger is the quadratic form of the tensor product of the two conjugate structures; the two readings, the general plain and the general quaternionic, are *The Form on the Biquaternion Algebra as a General Plain Sesquilinear Form*.

## What Belongs Elsewhere

- The **composition algebras** — the quaternion and octonion algebras, the Hurwitz theorem and the norm form over a general field — are *Quadratic Forms over Algebras and Norms*.
- The **reduced norm, the reduced trace and the class of a central simple algebra** are *Involutions of a Central Simple Algebra* and *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint*.
- The **blade form and the trace form of a Clifford algebra** are *The Blade Form and the Hermitian Structure with Hermitian Adjoint*, and the Euclidean form with its completion is *The Euclidean Form, the Norm and the Completion on a Clifford Algebra* in Part II.
- The **selection of a form's values as a norm** with a distance, a unit ball and a completion is *The Norm Defined by a Form*, *The Completion of a Sesqualgebra with a Form* and the category *Topology on Sesqualgebras with a degree-2 form*.

## Summary

- The **norm map** of the algebra is $N(x) = xx^{*}$ and its polarisation is the trace form $\tfrac{1}{2}(xy^{*}+yx^{*})$; the diagonal of the form is $q(x) = \varphi(x^{*}x)$, which is the functional of the norm, $q(x) = \varphi(N(x))$, for a cyclic functional such as the trace.
- The quaternion norm $N(x) = a^{2}-\alpha b^{2}-\beta c^{2}+\alpha\beta d^{2}$ is multiplicative, so the quaternion algebra is a composition algebra; its polarisation is the trace form, and the norm-one group is the compact group of the definite case.
- The reduced norm of a central simple algebra is multiplicative and its polarisation is the reduced trace against the adjugate; it is in general **not** the Hermitian form of the dagger, as $\mathsf{M}_2$ shows.
- For an involution of the first kind the reduced norm is invariant, for one of the second kind it is twisted by $\varsigma$.
- The norm of a Clifford algebra is the blade form, positive definite over a real base with $q$ positive definite, but it is not multiplicative: the multiplications hold on the versors of the Clifford group.
- The **algebraic norm** is a map into the base ring and is Algebra; the **topological norm** is the selection of positive real values and is Part II.

## Summary of Notation

| symbol | meaning |
|---|---|
| $N(x) = xx^{*}$ | the norm map of the algebra |
| $\langle x,y\rangle$ | the trace form $\tfrac{1}{2}(xy^{*}+yx^{*})$ |
| $q(x) = \varphi(N(x))$ | the diagonal of the form as the functional of the norm |
| $\operatorname{Nrd}$, $\operatorname{Trd}$ | the reduced norm and the reduced trace |
| $\operatorname{adj}$ | the adjugate of a matrix |
| $\mathrm{Cl}(V,q)$ | the Clifford algebra with the dagger of *Hermitian Algebras* |
| $a_{I}$ | the coefficients of $x$ in the blade basis |

## Further Reading

- T. Y. Lam, *Introduction to Quadratic Forms over Fields*, Graduate Studies in Mathematics 67 (American Mathematical Society, 2005), for the norm forms of quaternion algebras and the composition algebras.
- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings*, Grundlehren der mathematischen Wissenschaften 294 (Springer, 1991), for the reduced norm and the reduced trace of a central simple algebra with an involution.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the norm and the trace of a Clifford algebra and the multiplicativity on the Clifford group.
