# __States and Positive Functionals on a Topological Sesqualgebra__

## Introduction

A positive functional on an involutive algebra is one that is non-negatively valued on the elements of the form $x^{*}x$, and a state is a positive functional of norm one. The positivity is the functional's way of respecting the involution, and on a sesqualgebra it does one thing more: the formula $h_{f}(x,y) = f(x^{*}y)$ is a **sesquilinear pairing**, and it is the reduction of the canonical $A$-valued Hermitian form $h(x,y) = x^{*}y$ by the functional. The pairing is positive semi-definite, it satisfies the Cauchy–Schwarz inequality, and its null space is a left ideal; on the quotient the construction of Gelfand, Naimark and Segal produces a Hilbert space and a representation in which the pairing becomes an honest inner product and the involution of the sesqualgebra becomes the Hilbert adjoint.

Three facts organise the article. The pairing $h_{f}$ attached to a positive functional is a **sesquilinear form**, conjugate-linear in the first slot and linear in the second, Hermitian, positive semi-definite, and it is the scalar reduction $h_{\varphi}$ of the form layer at the conjugate functional $\varphi = \varsigma\circ f$, so the scalar theory of the sesqualgebra is contained in the functional theory. The **Cauchy–Schwarz inequality** $|h_{f}(x,y)|^{2} \leq h_{f}(x,x)h_{f}(y,y)$ holds, its null space $N_{f} = \{x : f(x^{*}x) = 0\}$ is the radical of the pairing and a left ideal, and on the quotient the pairing is an inner product. And the **GNS construction** produces a Hilbert space $H_{f}$, a cyclic vector $\xi_{f}$ and a representation $\pi_{f}$ with $\pi_{f}(x^{*}) = \pi_{f}(x)^{*}$ and

$$
\pi_{f}(x \star y) = \pi_{f}(x)\pi_{f}(y)^{*} , \qquad f(x) = \langle \xi_{f}, \pi_{f}(x)\xi_{f}\rangle ,
$$

so the representation turns the sesquilinear structure into operators: the derived product of the sesqualgebra becomes the product-with-adjoint, and the pairing $h_{f}(x,y) = f(x^{*}y)$ becomes the inner product of the vectors $\pi_{f}(x)\xi_{f}$ and $\pi_{f}(y)\xi_{f}$.

The article defines the positive functionals and the pairing they induce, proves the Cauchy–Schwarz inequality and the continuity, runs the GNS construction and reads the sesquilinear structure through it, and names the passage to the GNS construction of the degree-two form category, which it defers. The general theory of the positive functionals, the states and the GNS construction is *States and Positive Functionals on an Involutive Algebra*; the sesquilinear form and its reduction are *The Sesquilinear Form and the Conjugation* and *Hermitian Forms on a Sesqualgebra*; the canonical $A$-valued form and its reductions are *Adjoints of Bounded Sesquilinear Operators*; the positivity and the order are *Self-Adjoint Elements and the Positive Cone* and *Positivity and the Positive Cone of a Hermitian Form*; and the representation theory in full is *Operator Algebras*. Throughout, $A$ is a unital $\mathrm{C}^{*}$-algebra over $(\mathbb{C},\varsigma)$ with $\varsigma$ the conjugation, read as a sesqualgebra through the derived product $x \star y = xy^{*}$; a **positive functional** is a linear $f : A \to \mathbb{C}$ with $f(x^{*}x) \geq 0$ for all $x$, a **state** is a positive functional with $\lVert f\rVert = 1$, equivalently $f(1) = 1$, and $h_{f}(x,y) = f(x^{*}y)$ is its pairing.

## Positive Functionals and the Pairing

### The Definition

**Definition.** A linear functional $f : A \to \mathbb{C}$ is **positive** when $f(x^{*}x) \geq 0$ for every $x \in A$; it is **self-adjoint** when $f(x^{*}) = \overline{f(x)}$ for every $x$, and a positive functional with $f(1) = 1$ is a **state**. The **null space** of $f$ is $N_{f} = \{x : f(x^{*}x) = 0\}$.

**Proposition (positivity gives self-adjointness).** If $f$ is positive then $f$ is self-adjoint and $f(h) \in \mathbb{R}$ for every Hermitian $h \in A$.

*Proof.* Write $x = h + ik$ with $h, k$ Hermitian; positivity gives $f((h + \lambda k)^{*}(h + \lambda k)) = f(h^{2}) + \lambda f(hk + kh) + \lambda^{2}f(k^{2}) \geq 0$ as a real quadratic in the real $\lambda$, so its discriminant is non-positive and the bilinear form is real valued on the Hermitian part; applying this to the element $x$ and using the real linearity of $f$ on the Hermitian part gives $f(x^{*}) = \overline{f(x)}$. $\square$

**Remark.** The proposition is the reason the positivity of a functional is a condition of the *sesquilinear* layer: a positive functional is Hermitian, and a Hermitian functional is exactly a real-valued functional on the Hermitian part, which is the scalar datum that a sesquilinear form of the layer reduces to.

### The Sesquilinear Pairing

**Definition.** The **pairing** of a functional $f : A \to \mathbb{C}$ is

$$
h_{f} : A \times A \longrightarrow \mathbb{C} , \qquad h_{f}(x,y) = f(x^{*}y) .
$$

**Proposition (the pairing of a positive functional).** Let $f$ be positive. Then $h_{f}$ is additive in each variable, conjugate-linear in the first and linear in the second, Hermitian, $h_{f}(y,x) = \overline{h_{f}(x,y)}$, and positive semi-definite, $h_{f}(x,x) = f(x^{*}x) \geq 0$. It is the reduction $h_{\varphi}$ of *The Sesquilinear Form and the Conjugation*, §*The Correspondence*, at the functional $\varphi = \varsigma\circ f$, since $h_{\varsigma\circ f}(x,y) = \varsigma(f(y^{*}x)) = f((y^{*}x)^{*}) = f(x^{*}y)$ by the self-adjointness of $f$; equivalently it is the conjugate of the reduction $h_{f}$, and it is the form $h(x,y) = x^{*}y$ of *Hermitian Forms on a Sesqualgebra*, §*The Reduction to the Scalars*, at that functional.

*Proof.* Additivity is linearity of $f$; conjugate-linearity in the first slot is $h_{f}(\lambda x, y) = f(\bar\lambda x^{*}y) = \bar\lambda h_{f}(x,y)$, and linearity in the second is $h_{f}(x,\lambda y) = f(x^{*}\lambda y) = \lambda h_{f}(x,y)$, the scalar $\lambda$ being central. The Hermitian property is $h_{f}(y,x) = f(y^{*}x) = \overline{f(x^{*}y)} = \overline{h_{f}(x,y)}$, which is the self-adjointness of the proposition above; the positive semi-definiteness is the definition of positivity. The identifications are the definitions of the two cited sections read at $\varphi = \varsigma\circ f$, the conjugate functional of $f$. $\square$

**Remark (the convention of the corpus and the Hilbert convention).** The form $\Psi(x,y) = y^{*}x$ of *Hermitian Forms on a Sesqualgebra* is linear in the first slot and $\varsigma$-semilinear in the second, and $h_{f}(x,y) = f(x^{*}y) = \overline{f(y^{*}x)}$ is its conjugate, the same form in the Hilbert convention, semilinear in the first slot. The two are exchanged by the exchange of the two arguments, and they carry the same information because $f$ is self-adjoint; the article uses the Hilbert convention, which is the one in which $h_{f}$ is a genuine inner product on the quotient.

### The Cauchy–Schwarz Inequality and the Null Space

**Theorem (Cauchy–Schwarz).** Let $f$ be positive. Then for all $x,y \in A$,

$$
\lvert h_{f}(x,y)\rvert^{2} \leq h_{f}(x,x)\,h_{f}(y,y) = f(x^{*}x)f(y^{*}y) ,
$$

with equality if and only if $x$ and $y$ are linearly dependent modulo $N_{f}$.

*Proof.* For complex $\lambda$ the element $x - \lambda y$ satisfies $h_{f}(x - \lambda y, x - \lambda y) = f((x - \lambda y)^{*}(x - \lambda y)) \geq 0$; expanding with the two parities gives $h_{f}(x,x) - \lambda h_{f}(x,y) - \bar\lambda h_{f}(y,x) + \lvert\lambda\rvert^{2}h_{f}(y,y) \geq 0$. When $h_{f}(y,y) \neq 0$ the choice $\lambda = h_{f}(y,x)/h_{f}(y,y)$ and the Hermitian property reduce it to $h_{f}(x,x) - \lvert h_{f}(x,y)\rvert^{2}/h_{f}(y,y) \geq 0$, which is the inequality; when $h_{f}(y,y) = 0$ the same quadratic in real $\lambda$ forces $h_{f}(x,y) = 0$. The equality case is the degenerate case of a positive semi-definite form, by *The Norm Defined by a Form*, §*The Cauchy–Schwarz Inequality*. $\square$

**Corollary (the radical is the null space).** For a positive $f$ the null space is the radical of the pairing,

$$
N_{f} = \{x : h_{f}(x,x) = 0\} = \{x : h_{f}(x,y) = 0 \ \text{for all } y\} = \{x : h_{f}(y,x) = 0 \ \text{for all } y\} ,
$$

and it is a left ideal of $A$.

*Proof.* The equality of the first two sets is Cauchy–Schwarz: $h_{f}(x,x) = 0$ forces $h_{f}(x,y) = 0$ for every $y$, and the converse is the case $y = x$; the third set agrees with the second by the Hermitian property. For the ideal property let $x \in N_{f}$ and $a \in A$; then for every $y$,

$$
h_{f}(ax, y) = f((ax)^{*}y) = f(x^{*}a^{*}y) = h_{f}(x, a^{*}y) = 0 ,
$$

so $ax \in N_{f}$, and $N_{f}$ is a left ideal. $\square$

### Continuity

**Theorem (a positive functional is continuous).** Let $f$ be positive on the unital $\mathrm{C}^{*}$-algebra $A$. Then $f$ is bounded and

$$
\lVert f\rVert = f(1) ,
$$

so a state is exactly a positive functional with $f(1) = 1$, and the pairing of a state is controlled by $h_{f}(x,y) \leq \lVert x\rVert\lVert y\rVert$ in absolute value.

*Proof.* For $\lVert a\rVert \leq 1$ the Cauchy–Schwarz inequality gives $\lvert f(a)\rvert^{2} = \lvert f(1^{*}a)\rvert^{2} \leq f(1)f(a^{*}a)$, and $a^{*}a \leq \lVert a\rVert^{2}1$ in the $\mathrm{C}^{*}$-order with $f$ positive on the positive cone, so $f(a^{*}a) \leq \lVert a\rVert^{2}f(1)$; hence $\lvert f(a)\rvert \leq f(1)$ and $\lVert f\rVert \leq f(1)$, while $f(1) \leq \lVert f\rVert$ is the definition of the norm. The bound on the pairing is Cauchy–Schwarz applied to $x/\lVert x\rVert$ and $y/\lVert y\rVert$. $\square$

**Remark (the general Banach case).** On an arbitrary unital Banach sesqualgebra the boundedness of a positive functional is not automatic, and the article accordingly restricts to the continuous ones; in the $\mathrm{C}^{*}$-case the hypothesis is free. The bound $\lVert f\rVert = f(1)$ is the reason the states are the positive functionals of the unit ball, and it is the entry to the general theory of *States and Positive Functionals on an Involutive Algebra*, §*The State Space*, which is cited.

## The GNS Construction

### The Inner Product Space

**Theorem (the quotient is a pre-Hilbert space).** Let $f$ be positive. Then the formula

$$
\langle x + N_{f}, y + N_{f}\rangle_{f} = h_{f}(x,y) = f(x^{*}y)
$$

is a well-defined inner product on $A/N_{f}$, and the completion $H_{f}$ is a Hilbert space in which $A/N_{f}$ is dense.

*Proof.* The form is well defined on the quotient because $N_{f}$ is the radical, by the corollary of §*The Cauchy–Schwarz Inequality and the Null Space*; it is positive semi-definite by the definition of positivity, and it is positive definite on the quotient because its radical has been divided out; it is sesquilinear by the proposition of §*The Sesquilinear Pairing*. The completion of an inner product space is a Hilbert space, by *Hilbert Spaces*, §*Completeness and the Projection Theorem*. $\square$

### The Representation

**Theorem (the GNS representation).** Let $f$ be positive. Then the left multiplication by an element of $A$ passes to the quotient as a bounded operator,

$$
\pi_{f}(a) : H_{f} \to H_{f} , \qquad \pi_{f}(a)(x + N_{f}) = ax + N_{f} ,
$$

and $\pi_{f}$ is a $*$-representation, $\pi_{f}(a)^{*} = \pi_{f}(a^{*})$, so $\pi_{f}(a^{*}) = \pi_{f}(a)^{*}$ makes the involution of the sesqualgebra into the adjoint.

*Proof.* Left multiplication preserves $N_{f}$ because the null space is a left ideal, by the corollary above, so the formula is well defined on classes. Boundedness follows from the inequality $h_{f}(ax,ax) = f(x^{*}a^{*}ax) \leq \lVert a\rVert^{2}f(x^{*}x) = \lVert a\rVert^{2}h_{f}(x,x)$, which is the positivity of the functional $z \mapsto f(x^{*}zx)$ on the positive cone of the $\mathrm{C}^{*}$-algebra, with $a^{*}a \leq \lVert a\rVert^{2}1$; the operator is thus bounded with $\lVert\pi_{f}(a)\rVert \leq \lVert a\rVert$ and extends to the completion. The adjoint computation is

$$
\langle \pi_{f}(a)x, y\rangle_{f} = f(x^{*}a^{*}y) = f(x^{*}(a^{*}y)) = \langle x, \pi_{f}(a^{*})y\rangle_{f} ,
$$

which exhibits $\pi_{f}(a^{*}) = \pi_{f}(a)^{*}$ and, in particular, that $\pi_{f}$ is a $*$-representation. $\square$

### The Cyclic Vector and the State

**Proposition (the state is a vector state).** Let $f$ be positive and put $\xi_{f} = 1 + N_{f}$. Then $\xi_{f}$ is **cyclic**, $\overline{\pi_{f}(A)\xi_{f}} = H_{f}$, and

$$
f(a) = \langle \xi_{f}, \pi_{f}(a)\xi_{f}\rangle_{f} , \qquad \lVert\xi_{f}\rVert^{2} = f(1) .
$$

In particular $f$ is a state exactly when $f(1) = 1$, that is exactly when $\xi_{f}$ is a unit vector.

*Proof.* The computation is $\langle\xi_{f}, \pi_{f}(a)\xi_{f}\rangle = \langle 1 + N_{f}, a + N_{f}\rangle = f(1^{*}a) = f(a)$, and $\lVert\xi_{f}\rVert^{2} = \langle 1 + N_{f}, 1 + N_{f}\rangle = f(1)$; the inner product is conjugate-linear in the first slot, so the state is $\langle\xi_{f}, \pi_{f}(a)\xi_{f}\rangle$ and the reverse order gives $\overline{f(a)}$. The cyclic property is the definition of $H_{f}$ as the completion of the image of $A/N_{f}$. $\square$

## The Representation of the Sesquilinear Structure

### The Involution Becomes the Adjoint

**Theorem (the derived product and the triple product under $\pi_{f}$).** Let $f$ be a positive functional. Then for all $x,y,z \in A$,

$$
\pi_{f}(x \star y) = \pi_{f}(x)\pi_{f}(y)^{*} , \qquad \pi_{f}(\{x,y,z\}) = \pi_{f}(x)\pi_{f}(y)^{*}\pi_{f}(z) ,
$$

and the unit is represented by the identity, $\pi_{f}(1) = 1$.

*Proof.* The derived product is $x \star y = xy^{*}$, and $\pi_{f}$ is multiplicative with $\pi_{f}(y^{*}) = \pi_{f}(y)^{*}$; the triple product is $(x \star y) \star z^{*} = xy^{*}z$ of *The Bounded Ternary Product*, §*The Definition and the Parity*, and $\pi_{f}$ is multiplicative. The unit is represented by the identity because $\pi_{f}(1)(x + N_{f}) = x + N_{f}$ for every $x$, on a dense subspace, whence $\pi_{f}(1) = 1$ by continuity. $\square$

**Remark.** The theorem is the sense in which the GNS construction is the passage of the sesqualgebra to the operators: an element of the sesqualgebra acts on the GNS space by its left multiplication, the derived product acts as the product followed by the adjoint, and the two products of the layer — the binary and the ternary — become the two operations of the operator algebra. The representation is the scalar realisation of the operator theory of *Adjoints of Bounded Sesquilinear Operators*, §*The Canonical Pairing*.

### The Form $h_{f}$ Realised

**Theorem (the pairing is the inner product of the images).** Let $f$ be a positive functional. Then for all $x,y \in A$,

$$
h_{f}(x,y) = f(x^{*}y) = \langle \pi_{f}(x)\xi_{f}, \pi_{f}(y)\xi_{f}\rangle_{f} ,
$$

so the pairing $h_{f}$ is the pullback of the inner product of $H_{f}$ by the map $x \mapsto \pi_{f}(x)\xi_{f}$, and it is positive definite exactly when $f$ is faithful.

*Proof.* The multiplicativity and the adjoint property give $\langle\pi_{f}(x)\xi_{f}, \pi_{f}(y)\xi_{f}\rangle = \langle\xi_{f}, \pi_{f}(x)^{*}\pi_{f}(y)\xi_{f}\rangle = \langle\xi_{f}, \pi_{f}(x^{*}y)\xi_{f}\rangle = f(x^{*}y)$, the last step by the vector-state formula. The map $x \mapsto \pi_{f}(x)\xi_{f}$ has kernel $N_{f}$, by $\lVert\pi_{f}(x)\xi_{f}\rVert^{2} = f(x^{*}x)$; so $h_{f}$ is positive definite exactly when $N_{f} = \{0\}$, which is faithfulness. $\square$

**Remark.** The theorem is the reason the pairing is called positive semi-definite and not positive definite in general: it is the inner product of the images, so its radical is exactly the set of the elements whose image is annihilated by the cyclic vector, and the representation $\pi_{f}$ is injective exactly when the pairing is definite.

## The Passage to the Form Category

### The Reduction of the Canonical Form

**Remark (the pairing as a reduction).** The $A$-valued form of the sesqualgebra is $h(x,y) = x^{*}y$ of *Adjoints of Bounded Sesquilinear Operators*, §*The Canonical Pairing*, and the pairing of a functional is its scalar reduction, $h_{f}(x,y) = f(h(x,y))$. The functional $f$ is positive exactly when the reduction $h_{f}$ is positive semi-definite, by the definition of positivity; the reduction is therefore the passage from the operator-valued form of the layer to the scalar forms, and the GNS construction is the completion of that reduction to an inner product.

### The Deferred GNS of the Degree-Two Form

**Remark (named and deferred).** The GNS construction of the degree-two form category reads the same construction from a positive definite Hermitian form $h$ on a sesqualgebra, with the inner product $h$ itself and the representation by the operators that leave $h$ invariant; the passage is *The GNS Construction*, §*The Construction*, and it is deferred. The article records only that the form $h_{f}$ of a positive functional is a positive semi-definite form of that category and that the present construction is the specialisation in which the form is the reduction of the canonical $A$-valued one; the general theory and the indefinite case of *The Indefinite GNS Construction* are not needed here.

### The Collapse at the Trivial Involution

**Proposition (the collapse).** Let $\varsigma = \mathrm{id}$. Then the sesqualgebra has collapsed to the algebra: the involution $*$ is $\mathbb{C}$-linear, the two scalar rules of the product coincide, the pairing $h_{f}(x,y) = f(x^{*}y)$ is $\mathbb{C}$-bilinear rather than sesquilinear, and the GNS construction is that of *States and Positive Functionals on an Involutive Algebra* applied to the $\mathbb{C}$-linear involution $*$ of $A$; the positive functionals are the positive linear functionals of the bilinear layer, and the pairing reads $h_{f}(x,y) = f(xy)$ when in addition $* = \mathrm{id}$.

*Proof.* At $\varsigma = \mathrm{id}$ the scalar rule $(\lambda x)^{*} = \varsigma(\lambda)x^{*}$ becomes $(\lambda x)^{*} = \lambda x^{*}$, so $*$ is $\mathbb{C}$-linear and $h_{f}(\lambda x, y) = f(\lambda x^{*}y) = \lambda h_{f}(x,y)$: the pairing is linear, not merely conjugate-linear, in the first slot. The product is $\mathbb{K}$-bilinear, by the collapse theorem of *Topological Sesqualgebras*, §*The Collapse*, and the positivity is the classical condition on the cone $\{\sum x_{i}^{*}x_{i}\}$. The reduction $f(x^{*}y)$ equals $f(xy)$ for all $x,y$ exactly when $x^{*} = x$ for every $x$, that is when $* = \mathrm{id}$. $\square$

## Examples

### The Field and the Matrices

**Example (the field, verdict: the pairing of the modulus).** Let $A = \mathbb{C}$ with the conjugation and the derived product $z \star w = z\bar w$. A positive functional is $f(z) = \lambda z$ with $\lambda \geq 0$, the pairing is $h_{f}(z,w) = \lambda\bar z w$, the null space is $\{0\}$ for $\lambda > 0$, and the GNS space is $\mathbb{C}$ with the representation $\pi_{f}(z) = z$ and the cyclic vector $\xi_{f} = 1$. The state $\lambda = 1$ is the model state of all the examples, and the pairing is the Hermitian inner product of the plane.

**Example (the matrices, verdict: the Hilbert–Schmidt pairing).** Let $A = M_{n}(\mathbb{C})$ with the conjugation, the conjugate transpose and $X \star Y = XY^{*}$. The normalised trace $f(X) = \tfrac1n\operatorname{tr}(X)$ is a faithful state, the pairing is $h_{f}(X,Y) = \tfrac1n\operatorname{tr}(X^{*}Y)$, the Hilbert–Schmidt inner product scaled by $n$, and the GNS space is $M_{n}(\mathbb{C})$ with the Hilbert–Schmidt norm; the representation is $\pi_{f}(X)(Y) = XY$, that is the left regular representation, acting on the matrices as a Hilbert space. The pairing is definite because the trace is faithful, and the example is the finite-dimensional model in which every statement of the article is visible in linear algebra.

### The Functions

**Example (the functions, verdict: the measure states).** Let $A = C(X,\mathbb{C})$ for compact Hausdorff $X$, with the supremum norm, the involution $\sigma(g) = \bar g$ and $f \star g = f\bar g$. A state is a probability measure $\mu$ on $X$, $f(g) = \int g\,\mathrm{d}\mu$, by the Riesz representation theorem of *States and Positive Functionals on an Involutive Algebra*, §*Examples*; the pairing is $h_{f}(g,h) = \int\bar g h\,\mathrm{d}\mu$, the $L^{2}(\mu)$ inner product, and the GNS space is $L^{2}(X,\mu)$ with the representation by multiplication and the cyclic vector the constant function one. The example is the infinite-dimensional model; the pairing is the reduction by the measure of the canonical form, and its density is the Radon–Nikodým derivative in the non-atomic case.

## Summary

A **positive functional** on a unital sesqualgebra is a linear $f$ with $f(x^{*}x) \geq 0$; it is self-adjoint, and it induces the **sesquilinear pairing** $h_{f}(x,y) = f(x^{*}y)$, conjugate-linear in the first slot and linear in the second, Hermitian and positive semi-definite, which is the scalar reduction $h_{\varphi}$ of *The Sesquilinear Form and the Conjugation* at the conjugate functional $\varphi = \varsigma\circ f$ and the reduction of the canonical $A$-valued form $h(x,y) = x^{*}y$ by the functional. The **Cauchy–Schwarz inequality** $\lvert h_{f}(x,y)\rvert^{2} \leq h_{f}(x,x)h_{f}(y,y)$ holds, the **null space** $N_{f} = \{x : f(x^{*}x) = 0\}$ is the radical of the pairing and a left ideal, and on $A/N_{f}$ the pairing is an inner product whose completion $H_{f}$ carries the **GNS representation** $\pi_{f}$, a $*$-representation with $\pi_{f}(x^{*}) = \pi_{f}(x)^{*}$ and a cyclic vector $\xi_{f} = 1 + N_{f}$ such that $f(a) = \langle\xi_{f}, \pi_{f}(a)\xi_{f}\rangle$. The representation turns the **sesquilinear structure into operators**, $\pi_{f}(x \star y) = \pi_{f}(x)\pi_{f}(y)^{*}$ and $\pi_{f}(\{x,y,z\}) = \pi_{f}(x)\pi_{f}(y)^{*}\pi_{f}(z)$, and realises the pairing as the inner product of the images, $h_{f}(x,y) = \langle\pi_{f}(x)\xi_{f}, \pi_{f}(y)\xi_{f}\rangle$, so that $h_{f}$ is definite exactly when $f$ is faithful. The construction is the specialisation of the GNS construction of the degree-two form category to the forms that are reductions of the canonical one, and it is the scalar reading of the operator theory of the layer.

## Summary of Notation

| symbol | meaning |
|---|---|
| $f$, positive functional | Linear with $f(x^{*}x) \geq 0$; self-adjoint |
| $f(1) = 1$ | the normalisation that makes $f$ a state |
| $h_{f}(x,y) = f(x^{*}y)$ | the sesquilinear pairing, semilinear in the first slot |
| $h_{f}(y,x) = \overline{h_{f}(x,y)}$, $h_{f}(x,x) \geq 0$ | Hermitian and positive semi-definite |
| $\lvert h_{f}(x,y)\rvert^{2} \leq h_{f}(x,x)h_{f}(y,y)$ | the Cauchy–Schwarz inequality |
| $N_{f} = \{x : f(x^{*}x) = 0\}$ | the null space, the radical of the pairing and a left ideal |
| $H_{f}$, $\pi_{f}$, $\xi_{f} = 1 + N_{f}$ | the GNS space, representation and cyclic vector |
| $\pi_{f}(x^{*}) = \pi_{f}(x)^{*}$ | the involution becomes the adjoint |
| $\pi_{f}(x \star y) = \pi_{f}(x)\pi_{f}(y)^{*}$ | the derived product becomes product-with-adjoint |
| $h_{f}(x,y) = \langle\pi_{f}(x)\xi_{f}, \pi_{f}(y)\xi_{f}\rangle$ | the pairing as the inner product of the images |
| $\lVert f\rVert = f(1)$ | the continuity, automatic in the $\mathrm{C}^{*}$-case |

## Further Reading

- Jacques Dixmier, *$\mathrm{C}^{*}$-Algebras* (North-Holland, 1977), for the positive functionals, the states and the GNS construction.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume I* (Academic Press, 1983), for the state space, the cyclic representations and the irreducibility criterion.
- Gérard J. Murphy, *$\mathrm{C}^{*}$-Algebras and Operator Theory* (Academic Press, 1990), for the positivity, the Cauchy–Schwarz inequality and the GNS representation.
- Theodore W. Palmer, *Banach Algebras and the General Theory of ${}^*$-Algebras, Volume II* (Cambridge University Press, 2001), for the positive functionals on an involutive Banach algebra and the continuity question.
- Israel M. Gelfand and Mark A. Naimark, *On the imbedding of normed rings into the ring of operators in Hilbert space* (Mat. Sbornik 12, 1943), for the original construction and the representation theorem.
- Konrad Schmüdgen, *Unbounded Self-Adjoint Operators on Hilbert Space* (Springer, 2012), for the positive forms, the Hilbert-space completion and the indefinite generalisations that the form category carries.
