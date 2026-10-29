# __Jordan Algebras__

## Introduction

This article introduces **Jordan algebras**: commutative algebras over a commutative ring whose product satisfies a single identity in place of associativity, the **Jordan identity**. The subject is developed here as pure algebra, and no physical interpretation is used anywhere. The treatment is introductory.

The base structure is a **commutative ring** $R$ with identity $1 \neq 0$. The corpus's broad sense of "algebra" — a module with a bilinear product, not assumed associative, commutative or unital — is the setting, as in *Algebras*, and the Jordan product fails associativity for the same structural reason that the Lie bracket does, so is the nearest general precedent. Here the product is commutative; the compensating identity is the Jordan identity rather than the Jacobi identity.

The product itself has a **symmetric** origin. If $A$ is an associative algebra with product $(x, y) \mapsto xy$, then the symmetrised product

$$
x \bullet y = \tfrac{1}{2}(xy + yx)
$$

is commutative, and when $2$ is invertible in $R$ it is the unique commutative bilinear product with the same squaring map, $x \bullet x = x^2$, because the polarisation identity

$$
2\,(x \bullet y) = (x+y)^2 - x^2 - y^2
$$

reconstructs $x \bullet y$ from squares. The square $x \mapsto x^2$ is the degree-two part of the product, and the symmetrisation is exactly the passage from an ordered product to the unordered one, in the sense of *Symmetric Powers*. The Jordan identity is what survives of associativity after the order of the factors is forgotten.

The article defines Jordan algebras and their symmetrised examples, proves the Jordan identity for $A^+$, establishes power associativity, describes the Peirce decomposition attached to an idempotent, and states the classification of the formally real finite-dimensional algebras. The multiplication operators, the trace form and the derivations are the operator layer and are cited, not developed. The companion article treats the matrix algebras $H_n(D)$, the exceptional Albert algebra, and the special/exceptional dichotomy, treats the degree-two case.

## The Jordan Product

### Definition

Let $J$ be an $R$-module with a bilinear map $\bullet : J \times J \to J$. For $x \in J$ write $x^2 = x \bullet x$. The pair $(J, \bullet)$ is a **Jordan algebra** if $\bullet$ is commutative,

$$
x \bullet y = y \bullet x ,
$$

and the **Jordan identity**

$$
x^2 \bullet (y \bullet x) = (x^2 \bullet y) \bullet x
$$

holds for all $x, y \in J$. The identity says that the two ways of bracketing $x^2$, $y$ and $x$ agree; its operator form $[L_x,L_{x^2}]=0$ is *The Jordan Multiplication Operators*, §*The Jordan Identity in Operator Form*, and is not used here. The algebra is **unital** if there is an element $1 \in J$ with $1 \bullet x = x$ for all $x$; it is then automatically the two-sided unit because $\bullet$ is commutative. A **homomorphism** of Jordan algebras is an $R$-linear map preserving the product, $f(x \bullet y) = f(x) \bullet f(y)$; it is **unital** if it preserves $1$.

**Remark.** No coefficient such as $\tfrac{1}{2}$ appears in the axioms, so the definition makes sense over an arbitrary commutative ring. The symmetrised product of an associative algebra, by contrast, is usually written with $\tfrac{1}{2}$ and then requires $2$ invertible; when $2$ is not invertible the product $x \bullet y = xy + yx$ serves, and the two differ only by the unit $2$.

### The Jordan Identity and Its Equivalent Forms

The identity as stated involves only one element $x$ and one further element $y$. It can be restated in several equivalent ways, of which the following are the most useful.

**Proposition.** Let $(J, \bullet)$ be a commutative $R$-algebra. The Jordan identity implies, by polarisation, the **linearised identity**

$$
\boxed{\;2\,(x \bullet w) \bullet (y \bullet x) + x^2 \bullet (y \bullet w) = 2\,\bigl((x \bullet w) \bullet y\bigr) \bullet x + (x^2 \bullet y) \bullet w\;}
$$

for all $x, w, y \in J$. Conversely, the linearised identity at $w = x$ gives $3\,x^2 \bullet (y \bullet x) = 3\,(x^2 \bullet y) \bullet x$, so the two are equivalent when $3$ is invertible in $R$.

*Proof.* Work in $J \otimes_R R[t]$, which is a Jordan algebra by base change of the axioms. Since $(x + tw)^2 = x^2 + 2t\,(x \bullet w) + t^2 w^2$, the Jordan identity for the element $x + tw$ reads

$$
(x^2 + 2t\,x \bullet w + t^2 w^2) \bullet \bigl(y \bullet (x + tw)\bigr) = \bigl((x^2 + 2t\,x \bullet w + t^2 w^2) \bullet y\bigr) \bullet (x + tw),
$$

and the coefficient of $t$ is the displayed identity. A polynomial identity over $R[t]$ has vanishing coefficients. At $w = x$ the identity reads $3\,x^2 \bullet (y \bullet x) = 3\,(x^2 \bullet y) \bullet x$, so it returns the Jordan identity when $3$ is invertible.

The content of the axiom is therefore: the two ways of bracketing $x^2$, $y$ and $x$ agree, and this continues to hold after linearisation. The operator reading, in which the identity is the commutativity of the multiplication operators $L_x$ and $L_{x^2}$, is *The Jordan Multiplication Operators*, §*The Jordan Identity in Operator Form*.

### Power Associativity

A commutative algebra is **power associative** if the subalgebra generated by any single element is associative; equivalently, if the powers $x^n$ defined recursively by

$$
x^1 = x, \qquad x^{n+1} = x \bullet x^n
$$

satisfy $x^m \bullet x^n = x^{m+n}$ for all $m, n \geq 1$.

**Theorem.** Every Jordan algebra is power associative.

*Proof (sketch).* The Jordan identity is the elementwise identity

$$
x^2 \bullet (x \bullet y) = x \bullet (x^2 \bullet y) \qquad \text{for all } y,
$$

which says that the powers $x^2$ and $x$ may be moved past one another. The powers $x^n$ are obtained by iterating the map $y \mapsto x \bullet y$, so the submodule spanned by them is stable under that map. The assertion $x^m \bullet x^n = x^{m+n}$ is proved by induction on $m+n$. For $m+n \leq 2$ it is immediate from the definitions. For the step one writes $x^{m+1}\bullet x^n = x\bullet(x^m\bullet x^n)$ and uses the induction hypothesis, together with the displayed identity, to commute the powers of $x$; this gives $x^{m+n+1}$. The induction is standard and is carried out in any of the references below.

**Corollary.** In a Jordan algebra every element generates a commutative associative subalgebra, spanned by its powers. In particular, for each $x$ in a unital Jordan algebra the substitution $t \mapsto x$ is a surjective algebra homomorphism $R[t] \to J$ onto that subalgebra.

## Examples

### The Symmetrisation of an Associative Algebra

Let $A$ be an associative $R$-algebra. Define $A^+$ to be the same $R$-module with the **symmetrised product**

$$
x \bullet y = xy + yx
$$

when no division by $2$ is used, or $x \bullet y = \tfrac{1}{2}(xy + yx)$ when $2$ is invertible; the two products differ by the invertible scalar $2$, so they define isomorphic Jordan algebras whenever $2$ is a unit. This product is commutative, and the example below shows it satisfies the Jordan identity.

**Theorem.** For every associative algebra $A$, the symmetrised algebra $A^+$ is a Jordan algebra.

*Proof.* Commutativity is immediate. For the identity, compute both sides of $x^2 \bullet (y \bullet x) = (x^2 \bullet y) \bullet x$ in $A$, using the product $x \bullet y = xy + yx$ and the associativity of $A$, so that the Jordan square is $x^2 = x \bullet x = 2\,x\cdot x$. On the left,

$$
x^2 \bullet (y \bullet x) = 2x^2(yx + xy) + (yx + xy)\,2x^2 = 2\bigl(x^2yx + x^3y + yx^3 + xyx^2\bigr),
$$

and on the right,

$$
(x^2 \bullet y) \bullet x = (2x^2y + 2yx^2)x + x(2x^2y + 2yx^2) = 2\bigl(x^2yx + yx^3 + x^3y + xyx^2\bigr).
$$

The two expressions are the same four monomials in a different order, so the identity holds over every commutative ring. With the halved product $x \bullet y = \tfrac12(xy + yx)$ every coefficient is divided by $2$ and the same cancellation occurs, so the identity holds there too.

The construction $A \mapsto A^+$ is functorial: an algebra homomorphism $f: A \to B$ is a Jordan homomorphism $A^+ \to B^+$, because $f(xy + yx) = f(x)f(y) + f(y)f(x)$. A Jordan algebra isomorphic to a subalgebra of some $A^+$ is called **special**; one that is not is **exceptional**. The dichotomy is not covered here.

**Example.** $R^+$ for $R$ commutative is just $R$ with its multiplication, since the product is already commutative; this shows that every commutative associative algebra is a special Jordan algebra.

**Example.** For $A = M_n(R)$ the symmetrised algebra $M_n(R)^+$ is a Jordan algebra in which the product of matrices is the anticommutator. Its symmetric subalgebra $H_n(R)$, defined, is a Jordan subalgebra for the same reason.

### Hermitian Matrices

Let $D$ be a composition algebra over $R$ with a conjugation, for instance $\mathbb{R}$, $\mathbb{C}$ or $\mathbb{H}$, and let $H_n(D)$ denote the $n \times n$ matrices that are equal to their conjugate transpose, with the symmetrised product. Then $H_n(D)$ is a Jordan algebra, a subalgebra of $M_n(D)^+$ for associative $D$. For $n = 1$ this is the base field with its multiplication. For $n = 2$ and $D = \mathbb{R}$ it is the three-dimensional algebra spanned by orthogonal idempotents $u_+, u_-$ with $u_+ + u_- = 1$ together with an element $w$ satisfying $w \bullet w = 1$ and $u_\pm \bullet w = \tfrac12 w$; this is the smallest spin factor. These algebras, and the non-associative case $D = \mathbb{O}$, are treated; here they serve as the main source of examples.

### Spin Factors

A **spin factor** is a Jordan algebra of degree two built from a quadratic form on a free $R$-module; for $V = R^n$ with the standard form it is written $JSpin_n$. Its construction, its idempotents and the Clifford algebra that envelops it use the form and its standard form, and are *Spin Factors and the Clifford Envelope with Inner Conjugation*, in Part II, where the form is available; they are named only here.

### The Albert Algebra

If $\mathbb{O}$ denotes the octonions, the algebra $H_3(\mathbb{O})$ of Hermitian $3 \times 3$ matrices over $\mathbb{O}$ with the symmetrised product is a Jordan algebra of dimension $27$. It is the **Albert algebra**, and it is exceptional: it does not embed into any $A^+$ with $A$ associative. It is the smallest exceptional Jordan algebra and the only one among the finite-dimensional formally real algebras; the details, including the verification that the symmetrised product satisfies the Jordan identity, are in *Non-Associative Algebras and the Property Ladder*. The naive symmetrisation of matrix multiplication works only because the diagonal entries are required to be real, that is, fixed by the octonion conjugation; without that restriction the symmetrised product fails the Jordan identity.

## The Operator Layer

The trace form, its symmetry and its invariance under derivations, and the Lie algebra $\operatorname{Der}(J)$ of derivations of a Jordan algebra are operator theory: they are *The Jordan Multiplication Operators*, §*The Trace Form* and §*Inner Derivations*. They are cited where the corpus needs them and are not used here; the structure of this article is read with the product alone.

## The Peirce Decomposition

### The Cubic Identity for an Idempotent

An element $e \in J$ is an **idempotent** if $e^2 = e$. Idempotents in a Jordan algebra play the role that spectral projections play in an associative algebra.

**Theorem.** Let $e$ be an idempotent of a Jordan algebra $J$ over a ring in which $2$ is invertible. Then every $x \in J$ satisfies the **cubic identity**

$$
\boxed{\;2\,e \bullet \bigl(e \bullet (e \bullet x)\bigr) - 3\,e \bullet (e \bullet x) + e \bullet x = 0\;} .
$$

*Proof.* Apply the linearised identity above with $x = e$ and $y = e$:

$$
2\,(e \bullet w) \bullet e + e \bullet (e \bullet w) = 2\,\bigl((e \bullet w) \bullet e\bigr) \bullet e + (e \bullet e) \bullet w .
$$

Since $\bullet$ is commutative and $e \bullet e = e$, the left side is $3\,e \bullet (e \bullet w)$ and the right side is $2\,e \bullet \bigl(e \bullet (e \bullet w)\bigr) + e \bullet w$; rearranging gives the identity with $x = w$.

Because $t(t-1)(2t-1)$ has simple roots, the cubic identity splits every element into three components:

$$
x_1 = 2\,e \bullet (e \bullet x) - e \bullet x, \qquad x_{1/2} = 4\,e \bullet x - 4\,e \bullet (e \bullet x), \qquad x_0 = x - 3\,e \bullet x + 2\,e \bullet (e \bullet x),
$$

with $x = x_1 + x_{1/2} + x_0$ and $e \bullet x_\lambda = \lambda x_\lambda$ for $\lambda = 0, \tfrac12, 1$.

### The Peirce Spaces

The components give a direct sum decomposition of $J$ for each idempotent $e$:

$$
\boxed{\;J = J_1(e) \oplus J_{1/2}(e) \oplus J_0(e), \qquad J_\lambda(e) = \{x \in J : e \bullet x = \lambda x\}\;}.
$$

The summands are the **Peirce spaces** of $e$. The extreme spaces are subalgebras with units $e$ and $1 - e$ respectively when $J$ is unital, the middle space is a bimodule for them, and the products obey

$$
J_1 \bullet J_1 \subseteq J_1, \quad J_0 \bullet J_0 \subseteq J_0, \quad J_1 \bullet J_0 = 0, \quad J_1 \bullet J_{1/2} \subseteq J_{1/2}, \quad J_0 \bullet J_{1/2} \subseteq J_{1/2}, \quad J_{1/2} \bullet J_{1/2} \subseteq J_1 \oplus J_0 .
$$

For a Jordan algebra of degree two, such as a spin factor, the Peirce decomposition with respect to a rank-one idempotent $e$ splits the algebra into the two lines $Re$ and $R(1-e)$ together with the middle space $J_{1/2}(e)$; this is the shape in which the spin factors and the Clifford envelope are analysed, in *Spin Factors and the Clifford Envelope with Inner Conjugation* of Part II.

**Example.** In $A^+$ for $A = M_n(R)$ and $e = \operatorname{diag}(1, \ldots, 1, 0, \ldots, 0)$ with $r$ ones, the Peirce spaces are the block-diagonal parts $J_1 = A_{11}$, $J_0 = A_{22}$ and the two off-diagonal blocks, which together make up $J_{1/2}$.

## Formally Real Jordan Algebras and the Classification

### Formal Reality

A Jordan algebra $J$ over $\mathbb{R}$ is **formally real** if

$$
x_1^2 + x_2^2 + \cdots + x_k^2 = 0 \quad \Longrightarrow \quad x_1 = x_2 = \cdots = x_k = 0 .
$$

In a formally real Jordan algebra a sum of squares vanishes only if every term does, so the squares behave like nonnegative real numbers and $x^2 = 0$ forces $x = 0$. Formal reality rules out nilpotent elements, since $x^n = 0$ with $n \geq 2$ and $x^{n-1} \neq 0$ would give $(x^{n-1})^2 = 0$. The associated *order*, the **positive cone** it defines, and the equivalent criterion that the trace form be positive definite — the trace form is *The Jordan Multiplication Operators*, §*The Trace Form* — are not covered here; they are *Jordan Algebras and the Positive Cone*, in Part III, where the order is available, and are named only.

### The Classification

**Theorem (Jordan–von Neumann–Wigner).** Every finite-dimensional formally real Jordan algebra is a direct sum of simple ideals, and every simple finite-dimensional formally real Jordan algebra is isomorphic to one of the following:

1. the one-dimensional algebra $\mathbb{R} = JSpin_0 = H_1(\mathbb{R})$;
2. the spin factors $JSpin_n$, $n \geq 2$;
3. the matrix algebras $H_n(\mathbb{R})$, $n \geq 3$;
4. the complex Hermitian matrix algebras $H_n(\mathbb{C})$, $n \geq 3$;
5. the quaternionic Hermitian matrix algebras $H_n(\mathbb{H})$, $n \geq 3$;
6. the exceptional Albert algebra $H_3(\mathbb{O})$.

The list separates the spin factors from the matrix family because the overlap is genuine: $H_2(D) \cong JSpin_{1+\dim_{\mathbb{R}}D}$ for $D = \mathbb{R}, \mathbb{C}, \mathbb{H}$, so the rank-two matrix algebras are spin factors , while $H_n(\mathbb{R})$ for $n \geq 3$ is a genuinely different algebra that embeds in no spin factor. The classification is quoted here as standard; the individual families, the verification that they are Jordan algebras, and the proof that the Albert algebra is exceptional are the content of *Special and Exceptional Jordan Algebras*.

**Remark.** Over a general field the classification is much more delicate and was completed only with Zel'manov's theorem on the nilpotency of the radical; the present article and the two that follow its theme restrict to the classical and formally real setting, where the classification is the one above.

## Summary

A **Jordan algebra** is a commutative $R$-algebra $(J, \bullet)$ satisfying the Jordan identity $x^2 \bullet (y \bullet x) = (x^2 \bullet y) \bullet x$, which implies the linearised identity displayed in §*The Jordan Identity and Its Equivalent Forms*. The symmetrised product $x \bullet y = xy + yx$ of an associative algebra $A$ makes $A^+$ a Jordan algebra, and the proof reduces to the equality of the two expansions $2(x^2yx + x^3y + yx^3 + xyx^2)$ and $2(x^2yx + yx^3 + x^3y + xyx^2)$. Every Jordan algebra is power associative, so each element generates a commutative associative subalgebra. An idempotent $e$ produces the Peirce decomposition $J = J_1(e)\oplus J_{1/2}(e)\oplus J_0(e)$: the cubic identity $2\,e\bullet(e\bullet(e\bullet x))-3\,e\bullet(e\bullet x)+e\bullet x=0$ splits every element into three components with $e\bullet x_\lambda=\lambda x_\lambda$, $\lambda\in\{0,\tfrac12,1\}$. Over $\mathbb{R}$, the formally real finite-dimensional Jordan algebras are the direct sums of $\mathbb{R} = JSpin_0$, the spin factors $JSpin_n$ with $n \geq 2$, the Hermitian matrix algebras $H_n$ over $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$ with $n \geq 3$, and the exceptional Albert algebra $H_3(\mathbb{O})$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$ | Commutative ring with identity $1 \neq 0$ |
| $(J, \bullet)$ | Jordan algebra: commutative product with the Jordan identity |
| $x^2 = x \bullet x$ | Square in a Jordan algebra |
| $x^n$ | Jordan powers, defined by $x^{n+1} = x \bullet x^n$ |
| $A^+$ | Symmetrisation of an associative algebra, $x \bullet y = xy + yx$ |
| $D$ | A composition algebra: $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$ or $\mathbb{O}$; distinct from $\mathbb{D}$, the split complex numbers |
| $H_n(D)$ | Hermitian $n \times n$ matrices over $D$ |
| $JSpin_n$, $JSpin(V)$ | Spin factor of a quadratic form; constructed in *Spin Factors and the Clifford Envelope with Inner Conjugation* (Part II) |
| $H_3(\mathbb{O})$ | Albert algebra, the exceptional $27$-dimensional Jordan algebra |
| $e$ | Idempotent, $e^2 = e$ |
| $J_\lambda(e)$ | Peirce spaces for $\lambda \in \{0, \tfrac12, 1\}$ |
| Formally real | $\sum x_i^2 = 0 \Rightarrow x_i = 0$ |







## Further Reading

- Pascual Jordan, John von Neumann and Eugene Wigner, "On an algebraic generalization of the quantum mechanical formalism", *Annals of Mathematics* 35 (1934), 29–64, for the classification of formally real Jordan algebras.
- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, 1968), for the general structure theory.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for a modern exposition of the identities, the Peirce decomposition and the classification.
- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for the place of Jordan algebras among non-associative algebras.
- Efim Zel'manov, "On prime Jordan algebras", *Algebra i Logika* 18 (1979), for the structure theory over general fields.
- The eigenvalue decomposition of an element is [The Eigenvalue Decomposition in a Jordan Algebra](the-eigenvalue-decomposition-in-a-jordan-algebra.html).
