
# __The Positive Cone of an Involutive Algebra__

## Introduction

An **involution** of an algebra $A$ over $\mathbb{C}$ is a map $a\mapsto a^{*}$ that is conjugate-linear, is an anti-automorphism,

$$
(ab)^{*} = b^{*}a^{*}, \qquad (a^{*})^{*} = a ,
$$

and fixes the scalars. It produces a cone without any further datum: the **positive cone** of the involutive algebra is the set of sums of the elements of the form $a^{*}a$,

$$
A_+ = \Bigl\{\sum_{i} a_i^{*}a_i\Bigr\} ,
$$

which is convex, closed under addition and nonnegative scaling, closed under the involution, and closed under the **congruences** $x\mapsto c^{*}xc$. Its elements are the **positive elements** of the algebra, and they order the **Hermitian** part $H(A) = \{a : a^{*} = a\}$ by $a\leq b$ when $b - a\in A_+$. The cone is pointed exactly when the algebra is **reduced**, that is, when $\sum a_i^{*}a_i = 0$ forces every $a_i = 0$; this is the faithful-representation condition, and it is assumed throughout, because without it the cone contains a line and no order survives.

The article constructs the cone, proves that it is a cone, and describes the order it defines. The involution is **positive**, so it is an order isomorphism of the Hermitian part; the identity is positive, $1 = 1^{*}1$, so the unital algebra is an ordered algebra with order unit; and the crucial difference from the commutative case is that the cone of a noncommutative involutive algebra is closed under the **symmetrised** product but not under the associative one, which is the reason the order of an involutive algebra is a **Jordan** order and not an associative one. The **Hilbert cone** — the same cone for an algebra that also carries an inner product compatible with the involution — is *The Hilbert Cone of an Involutive Algebra* later in this category, where the positivity and the $JBW$ structure are developed; the **ordered involutive algebra**, the structure carrying the order and the involution together, is *Ordered Involutive Algebras*; the **Hermitian elements and the order unit** are *Hermitian Elements and the Order Unit*; and the **positive functionals**, the states and the extreme points are *The Cone of Positive Functionals*.

The algebra, the involution and the Hilbert algebra are *Hilbert Algebras* and *The Hermitian Sandwich on a Hermitian Algebra with Hermitian Adjoint* of Part II; the order and the order unit are *Ordered Vector Spaces and the Order Unit*; the positive operators are *Positive Operators on an Ordered Space*; the Jordan structure of the symmetrised product is *Jordan Algebras and the Positive Cone* and *The Jordan Algebra of Self-Adjoint Elements* later in this category; and the $C^{*}$-axioms are *Operator Algebras* and *JB\*-Algebras and the Gelfand–Naimark Theorem* later in this category.

## The Involution and its Cone

### The Involution

**Definition.** An **involutive algebra** is an associative algebra $A$ over $\mathbb{C}$ with a map $a\mapsto a^{*}$ that is conjugate-linear, is an anti-automorphism of order two, and fixes the scalars; the elements with $a^{*} = a$ are **Hermitian**, those with $a^{*} = -a$ are **skew**, and every element decomposes as

$$
a = \operatorname{Re}a + i\operatorname{Im}a, \qquad \operatorname{Re}a = \tfrac12(a+a^{*}), \quad \operatorname{Im}a = \tfrac1{2i}(a - a^{*}) ,
$$

into the sum of a Hermitian and a skew element in the complex sense, so that $H(A)$ is a real vector subspace.

*Proof.* The conjugate-linearity and the order-two property make the real and imaginary parts Hermitian and skew-adjoint as stated; the decomposition is unique because a Hermitian and a skew element can only add to the real part of $a$.

**Definition.** The **positive cone** of the involutive algebra is

$$
A_+ = \Bigl\{\sum_{i} a_i^{*}a_i : a_i\in A\Bigr\} .
$$

**Example.** For $A = M_n(\mathbb{C})$ with $a^{*} = \bar a^{\mathsf{T}}$ the cone $A_+$ is the cone of positive semidefinite matrices; for $A = C(X,\mathbb{C})$ with pointwise conjugation it is the cone of nonnegative continuous functions; for the group algebra $\mathbb{C}[G]$ with $g^{*} = g^{-1}$ it is the cone of the positive-definite elements, which is the origin of the Hilbert-algebra theory of Part II.

### The Cone is a Cone

**Proposition (closure properties).** The set $A_+$ is closed under addition and nonnegative scaling, contains $0$ and $1$, is closed under the involution,

$$
A_+^{*} = A_+ ,
$$

and is closed under the **congruences**: for $c\in A$ and $x\in A_+$, $c^{*}xc\in A_+$.

*Proof.* The sum of two sums of the form $a^{*}a$ is again one; a nonnegative multiple likewise; $0$ is the empty sum and $1 = 1^{*}1$; the involution sends $a^{*}a$ to $a^{*}a$ because $(a^{*}a)^{*} = a^{*}a$, and it is additive and conjugate-linear, so it preserves the set. For the congruence, $c^{*}\bigl(\sum a_i^{*}a_i\bigr)c = \sum (a_ic)^{*}(a_ic)\in A_+$.

**Definition.** The involutive algebra is **reduced** when $\sum_i a_i^{*}a_i = 0$ implies every $a_i = 0$; equivalently, when $a^{*}a = 0$ implies $a = 0$, which holds exactly when the algebra admits a faithful $\ast$-representation on a Hilbert space.

**Proposition (pointedness).** When $A$ is reduced the cone $A_+$ is pointed, $A_+\cap(-A_+) = \{0\}$, and hence is a proper convex cone.

*Proof.* If $x\in A_+\cap(-A_+)$ then $x = \sum a_i^{*}a_i = -\sum b_j^{*}b_j$, so $x + \sum b_j^{*}b_j = \sum a_i^{*}a_i + \sum b_j^{*}b_j = 0$; by reducedness every $a_i$ and every $b_j$ vanishes, hence $x = 0$.

**Proposition (the cone is closed under the symmetrised product).** The symmetrised product

$$
\{a,b\} = \tfrac12(ab + ba)
$$

of two elements of $A_+$ lies in $A_+$ when $A$ is a reduced involutive algebra of the $\ast$-normed kind, so that the cone is a **Jordan cone**; the associative product of two positive elements need not be positive.

*Proof.* The statement is the theorem that the positive cone of a C*-algebra is closed under the Jordan product, proved by the functional calculus: writing $a = u^{*}u$ and reducing to a square, the positivity of $\{a,b\}$ follows from the identity $\{x^{*}x,y\} = \frac12\bigl((xy^{*})^{*}(xy^{*}) + (x^{*}y^{*})^{*}(x^{*}y^{*})\bigr)$ after the standard symmetrisation over the spectral resolution of $x$. The failure for the associative product is the example of the matrix algebra, in which the product of two positive semidefinite matrices need not be Hermitian, and the symmetrised product is the correct product of the order.

## The Order

### Definition and Basic Properties

**Definition.** On the Hermitian part $H(A)$ the **order** is

$$
a\leq b \iff b - a\in A_+ .
$$

**Proposition (ordered vector space).** When $A$ is reduced, $H(A)$ with this order is an ordered vector space over $\mathbb{R}$ whose positive cone is $A_+\cap H(A)$, and $1$ is an order unit: for every Hermitian $a$ there is $\lambda>0$ with $-\lambda1\leq a\leq\lambda1$, in the bounded case in which such a $\lambda$ exists.

*Proof.* The order is defined by a cone by the pointedness and the closure under addition and scaling; the order-unit statement is the existence of $\lambda$ dominating $a$ in the cone, which holds for $\lambda$ larger than the norm of $a$ in a $\ast$-normed algebra.

**Proposition (the involution is positive and is an order isomorphism).** For $a,b\in H(A)$,

$$
a\leq b \implies a^{*}\leq b^{*} ,
$$

and since the Hermitian part is fixed by the involution the implication is trivial on $H(A)$. On the whole algebra the involution is **positive** in either order convention, $x\in A_+ \Rightarrow x^{*}\in A_+$ and $x\in A_+ \Rightarrow x^{*}x\in A_+$; consequently it is an order isomorphism of the positive cone, and it exchanges the left and right orders,

$$
x\leq_{r} y \iff x^{*}\leq_{l} y^{*} .
$$

*Proof.* $x^{*}\in A_+$ for $x\in A_+$ is the closedness of the cone under the involution; $x^{*}x\in A_+$ is the definition. The exchange of the one-sided orders is the anti-multiplicativity $(xy)^{*} = y^{*}x^{*}$.

**Proposition (the order is Archimedean under a $\ast$-norm).** If $A$ is a $\ast$-normed algebra with $\lVert a^{*}a\rVert = \lVert a\rVert^{2}$, then the order is Archimedean: $0\leq a$ and $a\leq\lambda1$ for every $\lambda>0$ implies $a = 0$.

*Proof.* Under the $\ast$-norm condition the positive cone lies in the closed ball of the norm, and the intersection of the intervals $[0,\lambda1]$ over all $\lambda>0$ is $\{0\}$ by the norm estimate $\lVert a\rVert\leq\lambda$ for every $\lambda>0$.

### The Cone in the Examples

**Example (the matrices).** For $A = M_n(\mathbb{C})$ the cone is the positive semidefinite cone, the order is the Loewner order, the order unit is the identity, and the order is Archimedean for the operator norm. The cone is **not** closed under the associative product, but it is closed under the symmetrised product, and it is the self-dual cone of *Jordan Algebras and the Positive Cone*.

**Example (the continuous functions).** For $A = C(X,\mathbb{C})$ the cone is the pointwise nonnegative cone, the order is the pointwise order, the involution is positive, the algebra is **commutative**, and here the cone **is** closed under the associative product; the difference from the matrix case is exactly commutativity, and this is the reason the corpus separates the ordered involutive algebras into the commutative and the noncommutative families.

## The Section of the Positive Functionals

**Definition.** A **positive functional** on the involutive algebra is a linear functional $\varphi$ that is Hermitian, $\varphi(a^{*}) = \overline{\varphi(a)}$, and positive on the cone, $\varphi(a^{*}a)\geq0$ for every $a$; it is a **state** when further $\varphi(1) = 1$.

**Proposition.** A Hermitian linear functional is positive if and only if it is positive on $A_+$; the positive functionals form the **dual cone** of $A_+$ in the space of Hermitian functionals, and the states form its base at the order unit. For every positive $\varphi$ the **Cauchy–Schwarz inequality**

$$
\lvert\varphi(b^{*}a)\rvert^{2}\leq\varphi(a^{*}a)\,\varphi(b^{*}b)
$$

holds.

*Proof.* Positivity on the cone is equivalent to positivity on the generators $a^{*}a$ by linearity and the definition of the cone; the base statement is the order-unit normalisation of *Ordered Vector Spaces and the Order Unit*; the inequality is the Cauchy–Schwarz inequality of the positive semidefinite form $(a,b)\mapsto\varphi(b^{*}a)$, which is positive semidefinite because $\varphi((a+\lambda b)^{*}(a+\lambda b))\geq0$ for every $\lambda$.

## Summary

An **involution** of an algebra is a conjugate-linear anti-automorphism of order two; it produces the **positive cone** $A_+ = \{\sum a_i^{*}a_i\}$ of the sums of the elements of the form $a^{*}a$, which is closed under addition and nonnegative scaling, is closed under the involution, and is closed under the **congruences** $x\mapsto c^{*}xc$. It is **pointed** exactly when the algebra is **reduced** (equivalently, admits a faithful $\ast$-representation), and then it orders the **Hermitian** part by $a\leq b\iff b-a\in A_+$, with $1$ an order unit in the bounded case. The involution is **positive** and is an order isomorphism, exchanging the left and the right orders; the order is Archimedean under a $\ast$-norm with $\lVert a^{*}a\rVert = \lVert a\rVert^{2}$. The cone is closed under the **symmetrised** product, so the order of a noncommutative involutive algebra is a **Jordan** order; in the commutative case it is also closed under the associative product. The **positive functionals** are the dual cone, the **states** its base at the order unit, and they satisfy the **Cauchy–Schwarz** inequality. The Hilbert algebra is *Hilbert Algebras* and the Hermitian sandwich is *The Hermitian Sandwich on a Hermitian Algebra with Hermitian Adjoint*; the order and the order unit are *Ordered Vector Spaces and the Order Unit*; the Jordan order is *Jordan Algebras and the Positive Cone* and *The Jordan Algebra of Self-Adjoint Elements*; the states and the extreme points are *The Cone of Positive Functionals*; the Hilbert cone is *The Hilbert Cone of an Involutive Algebra*; the ordered involutive algebra is *Ordered Involutive Algebras*; and the $C^{*}$-theory is *Operator Algebras* and *JB\*-Algebras and the Gelfand–Naimark Theorem*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $a^{*}$ | Involution, a conjugate-linear anti-automorphism of order two |
| $H(A) = \{a : a^{*} = a\}$ | Hermitian elements |
| $A_+ = \{\sum a_i^{*}a_i\}$ | Positive cone of the involutive algebra |
| $c^{*}xc$ | Congruence, preserving the cone |
| Reduced | $\sum a_i^{*}a_i = 0$ implies every $a_i = 0$ |
| $a\leq b \iff b-a\in A_+$ | The order on the Hermitian part |
| $\{a,b\} = \tfrac12(ab+ba)$ | Symmetrised product, preserving $A_+$ |
| $\varphi(a^{*}a)\geq0$ | Positive functional; state when $\varphi(1) = 1$ |
| $\lvert\varphi(b^{*}a)\rvert^{2}\leq\varphi(a^{*}a)\varphi(b^{*}b)$ | Cauchy–Schwarz for the positive functionals |

## Further Reading

- Jacques Dixmier, *Les algèbres d'opérateurs dans l'espace hilbertien* (Gauthier-Villars, 1969), for the positive cone of an operator algebra and the Cauchy–Schwarz inequality for the states.
- Richard Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. 1 (Academic Press, 1983), for the involution, the Hermitian elements and the order of a C*-algebra.
- Shoichiro Sakai, *C\*-Algebras and W\*-Algebras* (Springer, 1971), for the positive functionals, the states and the extreme points.
- Max Koecher, *The Minnesota Notes on Jordan Algebras and their Applications* (Springer, 1999), for the symmetrised product and the Jordan order of a noncommutative algebra.
- Pascual Jordan, John von Neumann and Eugene Wigner, "On an algebraic generalization of the quantum mechanical formalism", *Annals of Mathematics* **35** (1934), 29–64, for the order of the symmetrised product and the Jordan structure.
