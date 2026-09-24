# __Jordan Algebras__

## Introduction

This article introduces **Jordan algebras**: commutative algebras over a commutative ring whose product satisfies a single identity in place of associativity, the **Jordan identity**. The subject is developed here as pure algebra, and no physical interpretation is used anywhere. The treatment is introductory.

The base structure is a **commutative ring** $R$ with identity $1 \neq 0$. The corpus's broad sense of "algebra" — a module with a bilinear product, not assumed associative, commutative or unital — is the setting, as in *Algebras*, and the Jordan product fails associativity for the same structural reason that the Lie bracket does, sois the nearest general precedent. Here the product is commutative; the compensating identity is the Jordan identity rather than the Jacobi identity.

The product itself has a **symmetric** origin. If $A$ is an associative algebra with product $(x, y) \mapsto xy$, then the symmetrised product

$$
x \circ y = \tfrac{1}{2}(xy + yx)
$$

is commutative, and when $2$ is invertible in $R$ it is the unique commutative bilinear product with the same squaring map, $x \circ x = x^2$, because the polarisation identity

$$
2\,(x \circ y) = (x+y)^2 - x^2 - y^2
$$

reconstructs $x \circ y$ from squares. The square $x \mapsto x^2$ is the degree-two part of the product, and the symmetrisation is exactly the passage from an ordered product to the unordered one, in the sense of *Symmetric Powers*. The Jordan identity is what survives of associativity after the order of the factors is forgotten.

The article defines Jordan algebras and their symmetrised examples, proves the Jordan identity for $A^+$, establishes power associativity, constructs the trace form and proves its invariance under derivations, describes the Peirce decomposition attached to an idempotent, and states the classification of the formally real finite-dimensional algebras. The companion articletreats the matrix algebras $H_n(D)$, the exceptional Albert algebra, and the special/exceptional dichotomy, treats the degree-two case.

## The Jordan Product

### Definition

Let $J$ be an $R$-module with a bilinear map $\circ : J \times J \to J$. For $x \in J$ write $x^2 = x \circ x$, and for a fixed $x$ let $L_x \in \operatorname{End}_R(J)$ be the **multiplication operator**

$$
L_x(y) = x \circ y .
$$

The pair $(J, \circ)$ is a **Jordan algebra** if $\circ$ is commutative,

$$
x \circ y = y \circ x ,
$$

and the **Jordan identity**

$$
x^2 \circ (y \circ x) = (x^2 \circ y) \circ x
$$

holds for all $x, y \in J$. In operator form the identity is

$$
[L_x, L_{x^2}] = 0 ,
$$

where $[S, T] = ST - TS$ is the commutator of endomorphisms. The algebra is **unital** if there is an element $1 \in J$ with $1 \circ x = x$ for all $x$; it is then automatically the two-sided unit because $\circ$ is commutative. A **homomorphism** of Jordan algebras is an $R$-linear map preserving the product, $f(x \circ y) = f(x) \circ f(y)$; it is **unital** if it preserves $1$.

**Remark.** No coefficient such as $\tfrac{1}{2}$ appears in the axioms, so the definition makes sense over an arbitrary commutative ring. The symmetrised product of an associative algebra, by contrast, is usually written with $\tfrac{1}{2}$ and then requires $2$ invertible; when $2$ is not invertible the product $x \circ y = xy + yx$ serves, and the two differ only by the unit $2$.

### The Jordan Identity and Its Equivalent Forms

The identity as stated involves only one element $x$ and one further element $y$. It can be restated in several equivalent ways, of which the following are the most useful.

**Proposition.** Let $(J, \circ)$ be a commutative $R$-algebra. The Jordan identity $x^2 \circ (y \circ x) = (x^2 \circ y) \circ x$ for all $x, y \in J$ is equivalent to the operator identity

$$
[L_x, L_{x^2}] = 0 \qquad \text{for all } x \in J .
$$

It implies, by polarisation, the **linearised identity**

$$
[L_w, L_{x^2}] + 2\,[L_x, L_{x \circ w}] = 0 \qquad \text{for all } x, w \in J ,
$$

and, when $2$ is invertible in $R$, the **cyclic** form

$$
[L_x, L_{y \circ z}] + [L_y, L_{z \circ x}] + [L_z, L_{x \circ y}] = 0 \qquad \text{for all } x, y, z \in J .
$$

The cyclic form at $z = x$ is the linearised identity, so it implies it over any commutative ring. Conversely, the linearised identity at $w = x$ reads $3\,[L_x, L_{x^2}] = 0$, so the three forms are equivalent whenever $2$ and $3$ are invertible in $R$.

*Proof.* Commutativity identifies $L_x(y) = x \circ y$ and $L_{x^2}(y) = x^2 \circ y$, so the identity $x^2 \circ (y \circ x) = (x^2 \circ y) \circ x$ for all $y$ is exactly $[L_x, L_{x^2}] = 0$; this needs no hypothesis on $2$. For the polarised forms, work in $J \otimes_R R[t]$, which is a Jordan algebra by base change of the axioms. Since $(x + tw)^2 = x^2 + 2t\,(x \circ w) + t^2 w^2$ and $L_{x + tw} = L_x + tL_w$, the expansion of $[L_{x + tw}, L_{(x+tw)^2}] = 0$ has $t$-coefficient $[L_w, L_{x^2}] + 2\,[L_x, L_{x \circ w}]$, and a polynomial identity over $R[t]$ has vanishing coefficients. Similarly, expanding $[L_{x + sy + tz}, L_{(x+sy+tz)^2}] = 0$ shows that the coefficient of $st$ is twice the cyclic sum, so the cyclic form follows when $2$ is invertible. The specialisations $z = x$ and $w = x$ are immediate. $\square$

The content of the axiom is therefore: multiplication by $x$ and multiplication by $x^2$ commute, and this continues to hold after linearisation. Despite the absence of associativity, the operators $L_x$ and $L_{x^2}$ generate a commutative algebra of endomorphisms, which is what makes the powers of a single element manageable.

### Power Associativity

A commutative algebra is **power associative** if the subalgebra generated by any single element is associative; equivalently, if the powers $x^n$ defined recursively by

$$
x^1 = x, \qquad x^{n+1} = x \circ x^n
$$

satisfy $x^m \circ x^n = x^{m+n}$ for all $m, n \geq 1$.

**Theorem.** Every Jordan algebra is power associative.

*Proof (sketch).* The Jordan identity states $[L_x, L_{x^2}] = 0$, so $L_x$ commutes with $L_{x^2}$. All powers $x^n$ are obtained from $x$ by iterating $L_x$, since $x^{n+1} = L_x(x^n)$; hence the submodule spanned by the powers is stable under $L_x$. The assertion $x^m \circ x^n = x^{m+n}$ is proved by induction on $m + n$. For $m + n \leq 2$ it is immediate from the definitions. For the induction step one uses the identity $L_{x^2}L_x = L_x L_{x^2}$, rewritten as

$$
x^2 \circ (x \circ y) = x \circ (x^2 \circ y) \qquad \text{for all } y,
$$

to move two of the factors past one another: writing $x^{m+1} \circ x^n = x \circ (x^m \circ x^n)$ and using the induction hypothesis, together with the displayed identity to commute the powers of $x$, gives $x^{m+n+1}$. The induction is standard and is carried out in any of the references below. $\square$

**Corollary.** In a Jordan algebra every element generates a commutative associative subalgebra, spanned by its powers. In particular, for each $x$ in a unital Jordan algebra the substitution $t \mapsto x$ is a surjective algebra homomorphism $R[t] \to J$ onto that subalgebra.

## Examples

### The Symmetrisation of an Associative Algebra

Let $A$ be an associative $R$-algebra. Define $A^+$ to be the same $R$-module with the **symmetrised product**

$$
x \circ y = xy + yx
$$

when no division by $2$ is used, or $x \circ y = \tfrac{1}{2}(xy + yx)$ when $2$ is invertible; the two products differ by the invertible scalar $2$, so they define isomorphic Jordan algebras whenever $2$ is a unit. This product is commutative, and the example below shows it satisfies the Jordan identity.

**Theorem.** For every associative algebra $A$, the symmetrised algebra $A^+$ is a Jordan algebra.

*Proof.* Commutativity is immediate. For the identity, compute both sides of $x^2 \circ (y \circ x) = (x^2 \circ y) \circ x$ in $A$, using the product $x \circ y = xy + yx$ and the associativity of $A$, so that the Jordan square is $x^2 = x \circ x = 2\,x\cdot x$. On the left,

$$
x^2 \circ (y \circ x) = 2x^2(yx + xy) + (yx + xy)\,2x^2 = 2\bigl(x^2yx + x^3y + yx^3 + xyx^2\bigr),
$$

and on the right,

$$
(x^2 \circ y) \circ x = (2x^2y + 2yx^2)x + x(2x^2y + 2yx^2) = 2\bigl(x^2yx + yx^3 + x^3y + xyx^2\bigr).
$$

The two expressions are the same four monomials in a different order, so the identity holds over every commutative ring. With the halved product $x \circ y = \tfrac12(xy + yx)$ every coefficient is divided by $2$ and the same cancellation occurs, so the identity holds there too. $\square$

The construction $A \mapsto A^+$ is functorial: an algebra homomorphism $f: A \to B$ is a Jordan homomorphism $A^+ \to B^+$, because $f(xy + yx) = f(x)f(y) + f(y)f(x)$. A Jordan algebra isomorphic to a subalgebra of some $A^+$ is called **special**; one that is not is **exceptional**. The dichotomy is not covered here.

**Example.** $R^+$ for $R$ commutative is just $R$ with its multiplication, since the product is already commutative; this shows that every commutative associative algebra is a special Jordan algebra.

**Example.** For $A = M_n(R)$ the symmetrised algebra $M_n(R)^+$ is a Jordan algebra in which the product of matrices is the anticommutator. Its symmetric subalgebra $H_n(R)$, defined, is a Jordan subalgebra for the same reason.

### Hermitian Matrices

Let $D$ be a composition algebra over $R$ with a conjugation, for instance $\mathbb{R}$, $\mathbb{C}$ or $\mathbb{H}$, and let $H_n(D)$ denote the $n \times n$ matrices that are equal to their conjugate transpose, with the symmetrised product. Then $H_n(D)$ is a Jordan algebra, a subalgebra of $M_n(D)^+$ for associative $D$. For $n = 1$ this is the base field with its multiplication. For $n = 2$ and $D = \mathbb{R}$ it is the three-dimensional algebra spanned by orthogonal idempotents $u_+, u_-$ with $u_+ + u_- = 1$ together with an element $w$ satisfying $w \circ w = 1$ and $u_\pm \circ w = \tfrac12 w$; this is the smallest spin factor. These algebras, and the non-associative case $D = \mathbb{O}$, are treated; here they serve as the main source of examples.

### Spin Factors

Let $V$ be a free $R$-module with a quadratic form $q$ and polar form $B$, normalised so that $B(v, v) = q(v)$, and put $JSpin(V) = R \cdot 1 \oplus V$ with product

$$
(\alpha, v) \circ (\beta, w) = \bigl(\alpha\beta + B(v, w),\ \alpha w + \beta v\bigr).
$$

Then $JSpin(V)$ is a unital Jordan algebra of **degree two**: every element satisfies the quadratic equation $x^2 - 2\alpha x + (\alpha^2 - q(v))1 = 0$ over its powers, and the idempotents other than $0$ and $1$ are exactly the elements $\tfrac12(1 \pm u)$ with $q(u) = 1$. For $V = R^n$ with the standard form write $JSpin_n$. The Clifford algebra of the form supplies an associative algebra in which $JSpin(V)$ embeds, and the construction of that enveloping algebra is not covered here.

### The Albert Algebra

If $\mathbb{O}$ denotes the octonions, the algebra $H_3(\mathbb{O})$ of Hermitian $3 \times 3$ matrices over $\mathbb{O}$ with the symmetrised product is a Jordan algebra of dimension $27$. It is the **Albert algebra**, and it is exceptional: it does not embed into any $A^+$ with $A$ associative. It is the smallest exceptional Jordan algebra and the only one among the finite-dimensional formally real algebras; the details, including the verification that the symmetrised product satisfies the Jordan identity, are. The naive symmetrisation of matrix multiplication works only because the diagonal entries are required to be real, that is, fixed by the octonion conjugation; without that restriction the symmetrised product fails the Jordan identity.

## The Trace Form and Derivations

### The Trace Form

Let $J$ be a Jordan algebra that is free of finite rank as an $R$-module. The **trace form** is

$$
T : J \times J \longrightarrow R, \qquad T(x, y) = \operatorname{tr}(L_{x \circ y}).
$$

It is symmetric and $R$-bilinear, because $\circ$ is commutative and $L$ is linear in its subscript. Its name records the special case: if $2$ is invertible and $J = A^+$ for an associative algebra $A$ that is free of finite rank, then $L_x = \tfrac{1}{2}(\lambda_x + \rho_x)$, where $\lambda_x$ and $\rho_x$ are the operators of left and right multiplication by $x$ on $A$; for $A = M_n(R)$ each of them has trace $n\operatorname{tr}(x)$, obtained by writing the operator in the basis of matrix units, so

$$
T(x, y) = \tfrac{1}{2}\bigl(\operatorname{tr}(\lambda_{x\circ y}) + \operatorname{tr}(\rho_{x\circ y})\bigr) = n\operatorname{tr}(x\circ y) = n\operatorname{tr}(xy)
$$

with the halved product $x \circ y = \tfrac12(xy + yx)$, and the trace form is the associative trace form $\operatorname{tr}(xy)$ up to the scalar $n$.

**Proposition.** Let $J$ be a Jordan algebra and let $\delta \in \operatorname{End}_R(J)$ be a **derivation**, that is, an $R$-linear map with

$$
\delta(x \circ y) = \delta(x) \circ y + x \circ \delta(y)
$$

for all $x, y$. Then $T(\delta x, y) + T(x, \delta y) = 0$; derivations are skew with respect to the trace form.

*Proof.* The derivation identity is equivalent to the operator identity

$$
\delta L_x = L_{\delta x} + L_x \delta, \qquad \text{equivalently} \qquad [\delta, L_x] = L_{\delta x},
$$

because both sides applied to $y$ give $\delta(x \circ y) = \delta x \circ y + x \circ \delta y$. Hence

$$
\operatorname{tr}\bigl([\delta, L_{x \circ y}]\bigr) = \operatorname{tr}\bigl(L_{\delta(x \circ y)}\bigr) = \operatorname{tr}\bigl(L_{\delta x \circ y} + L_{x \circ \delta y}\bigr) = T(\delta x, y) + T(x, \delta y),
$$

where the last equality is the definition of $T$ and the linearity of $L$ in its subscript. The left-hand side is the trace of a commutator and therefore vanishes. $\square$

**Corollary.** The trace form is invariant under every one-parameter group of automorphisms generated by a derivation: for a derivation $\delta$, the bilinear form $T$ is annihilated by the infinitesimal action $\delta$, so any automorphism of the form $\exp(\delta)$ (when defined) preserves $T$.

### Derivations

The set of derivations of a Jordan algebra $J$ is written $\operatorname{Der}(J)$. It is a submodule of $\operatorname{End}_R(J)$, closed under the commutator: if $\delta, \eta$ are derivations then so is $[\delta, \eta]$. Indeed,

$$
\delta\eta(x\circ y) = \delta(\eta x\circ y + x\circ \eta y) = \delta\eta x\circ y + \eta x\circ \delta y + \delta x\circ \eta y + x\circ \delta\eta y
$$

and

$$
\eta\delta(x\circ y) = \eta\delta x\circ y + \delta x\circ \eta y + \eta x\circ \delta y + x\circ \eta\delta y ,
$$

so subtracting, the two cross terms cancel and

$$
[\delta,\eta](x\circ y) = [\delta,\eta]x \circ y + x \circ [\delta,\eta]y .
$$

Thus $\operatorname{Der}(J)$ is a **Lie algebra** under the commutator, in the sense. It is the infinitesimal automorphism algebra of $J$. The **inner derivations** are the elements of the span of the operators $[L_x, L_y]$; that these are derivations is a consequence of the linearised identity of the proposition above, and they form an ideal of $\operatorname{Der}(J)$.

## The Peirce Decomposition

### The Cubic Identity for an Idempotent

An element $e \in J$ is an **idempotent** if $e^2 = e$. Idempotents in a Jordan algebra play the role that spectral projections play in an associative algebra.

**Theorem.** Let $e$ be an idempotent of a Jordan algebra $J$ over a ring in which $2$ is invertible. Then

$$
2 L_e^3 - 3 L_e^2 + L_e = 0 ,
$$

as an identity of endomorphisms of $J$. Equivalently, $L_e(L_e - 1)(2L_e - 1) = 0$, so over a field the only possible eigenvalues of $L_e$ are $0$, $1$ and $\tfrac{1}{2}$.

*Proof.* Use the linearised identity $[L_w, L_{x^2}] + 2\,[L_x, L_{x \circ w}] = 0$ with $x = e$ and $w$ arbitrary; since $e^2 = e$ it reads

$$
[L_w, L_e] + 2\,[L_e, L_{e \circ w}] = 0 .
$$

Evaluate both sides on the element $e$ and put $Z = e \circ (w \circ e) = (e \circ w) \circ e$, the two expressions being equal by the Jordan identity with $x = e$, $y = w$. Now $L_wL_e e = L_e w$, $L_eL_w e = Z$, $L_eL_{e\circ w}e = L_eZ$ and $L_{e\circ w}L_e e = Z$, so the identity becomes $L_e w - 3Z + 2L_eZ = 0$, that is,

$$
L_e w - 3L_e^2 w + 2L_e^3 w = 0
$$

for every $w \in J$. Hence $2L_e^3 - 3L_e^2 + L_e = 0$, which factors as $L_e(L_e - 1)(2L_e - 1) = 0$. $\square$

### The Peirce Spaces

The theorem gives a direct sum decomposition of $J$ for each idempotent $e$:

$$
J = J_1(e) \oplus J_{1/2}(e) \oplus J_0(e), \qquad J_\lambda(e) = \{x \in J : e \circ x = \lambda x\}.
$$

The summands are the **Peirce spaces** of $e$. The extreme spaces are subalgebras with units $e$ and $1 - e$ respectively when $J$ is unital, the middle space is a bimodule for them, and the products obey

$$
J_1 \circ J_1 \subseteq J_1, \quad J_0 \circ J_0 \subseteq J_0, \quad J_1 \circ J_0 = 0, \quad J_1 \circ J_{1/2} \subseteq J_{1/2}, \quad J_0 \circ J_{1/2} \subseteq J_{1/2}, \quad J_{1/2} \circ J_{1/2} \subseteq J_1 \oplus J_0 .
$$

For a Jordan algebra of degree two, such as a spin factor, the Peirce decomposition with respect to a rank-one idempotent $e$ splits the algebra into the two lines $Re$ and $R(1-e)$ together with the hyperplane of $V$ orthogonal to the vector part of $e$; this is the form in which the spin factors and the Clifford envelope are analysed.

**Example.** In $A^+$ for $A = M_n(R)$ and $e = \operatorname{diag}(1, \ldots, 1, 0, \ldots, 0)$ with $r$ ones, the Peirce spaces are the block-diagonal parts $J_1 = A_{11}$, $J_0 = A_{22}$ and the two off-diagonal blocks, which together make up $J_{1/2}$.

## Formally Real Jordan Algebras and the Classification

### Formal Reality

A Jordan algebra $J$ over $\mathbb{R}$ is **formally real** if

$$
x_1^2 + x_2^2 + \cdots + x_k^2 = 0 \quad \Longrightarrow \quad x_1 = x_2 = \cdots = x_k = 0 .
$$

This is the algebraic condition that makes the set of sums of squares a pointed convex cone, free of lines through the orig. In a formally real Jordan algebra a sum of squares vanishes only if every term does, so the squares behave like nonnegative real numbers: $x^2 = 0$ forces $x = 0$, and the set of sums of squares is a pointed cone. The associated **positive cone** and its properties are not covered here. Formal reality rules out nilpotent elements, since $x^n = 0$ with $n \geq 2$ and $x^{n-1} \neq 0$ would give $(x^{n-1})^2 = 0$, and it forces the trace form to be positive definite when the algebra is finite-dimensional and unital.

### The Classification

**Theorem (Jordan–von Neumann–Wigner).** Every finite-dimensional formally real Jordan algebra is a direct sum of simple ideals, and every simple finite-dimensional formally real Jordan algebra is isomorphic to one of the following:

1. the one-dimensional algebra $\mathbb{R} = JSpin_0 = H_1(\mathbb{R})$;
2. the spin factors $JSpin_n$, $n \geq 2$;
3. the matrix algebras $H_n(\mathbb{R})$, $n \geq 3$;
4. the complex Hermitian matrix algebras $H_n(\mathbb{C})$, $n \geq 3$;
5. the quaternionic Hermitian matrix algebras $H_n(\mathbb{H})$, $n \geq 3$;
6. the exceptional Albert algebra $H_3(\mathbb{O})$.

The list separates the spin factors from the matrix family because the overlap is genuine: $H_2(D) \cong JSpin_{1+\dim_{\mathbb{R}}D}$ for $D = \mathbb{R}, \mathbb{C}, \mathbb{H}$, so the rank-two matrix algebras are spin factors , while $H_n(\mathbb{R})$ for $n \geq 3$ is a genuinely different algebra that embeds in no spin factor. The classification is quoted here as standard; the individual families, the verification that they are Jordan algebras, and the proof that the Albert algebra is exceptional are the content .

**Remark.** Over a general field the classification is much more delicate and was completed only with Zel'manov's theorem on the nilpotency of the radical; the present article and the two that follow its theme restrict to the classical and formally real setting, where the classification is the one above.

## Summary

A **Jordan algebra** is a commutative $R$-algebra $(J, \circ)$ satisfying the Jordan identity $x^2 \circ (y \circ x) = (x^2 \circ y) \circ x$, equivalently $[L_x, L_{x^2}] = 0$. The symmetrised product $x \circ y = xy + yx$ of an associative algebra $A$ makes $A^+$ a Jordan algebra, and the proof reduces to the equality of the two expansions $2(x^2yx + x^3y + yx^3 + xyx^2)$ and $2(x^2yx + yx^3 + x^3y + xyx^2)$. Every Jordan algebra is power associative, so each element generates a commutative associative subalgebra. The trace form $T(x,y) = \operatorname{tr}(L_{x\circ y})$ is symmetric, and every derivation is skew for it. An idempotent $e$ produces the Peirce decomposition $J = J_1(e)\oplus J_{1/2}(e)\oplus J_0(e)$, because $L_e$ satisfies $2L_e^3 - 3L_e^2 + L_e = 0$ and has spectrum in $\{0, 1, \tfrac12\}$. Over $\mathbb{R}$, the formally real finite-dimensional Jordan algebras are the direct sums of $\mathbb{R} = JSpin_0$, the spin factors $JSpin_n$ with $n \geq 2$, the Hermitian matrix algebras $H_n$ over $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$ with $n \geq 3$, and the exceptional Albert algebra $H_3(\mathbb{O})$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $R$ | Commutative ring with identity $1 \neq 0$ |
| $(J, \circ)$ | Jordan algebra: commutative product with the Jordan identity |
| $x^2 = x \circ x$ | Square in a Jordan algebra |
| $L_x$ | Multiplication operator $y \mapsto x \circ y$ |
| $\lambda_x$, $\rho_x$ | Left and right multiplication by $x$ in an associative algebra |
| $[S, T] = ST - TS$ | Commutator of endomorphisms |
| $x^n$ | Jordan powers, defined by $x^{n+1} = x \circ x^n$ |
| $A^+$ | Symmetrisation of an associative algebra, $x \circ y = xy + yx$ |
| $D$ | A composition algebra: $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$ or $\mathbb{O}$; distinct from $\mathbb{D}$, the split complex numbers |
| $H_n(D)$ | Hermitian $n \times n$ matrices over $D$ |
| $JSpin(V)$, $JSpin_n$ | Spin factor $R \oplus V$ with $(\alpha,v)\circ(\beta,w) = (\alpha\beta + B(v,w), \alpha w + \beta v)$ |
| $q$, $B$ | Quadratic form and its polar form, $B(v,v) = q(v)$ |
| $H_3(\mathbb{O})$ | Albert algebra, the exceptional $27$-dimensional Jordan algebra |
| $T(x,y) = \operatorname{tr}(L_{x\circ y})$ | Trace form |
| $\operatorname{Der}(J)$ | Lie algebra of derivations of $J$ |
| $\delta$ | A derivation, $\delta(x\circ y) = \delta x \circ y + x \circ \delta y$ |
| $e$ | Idempotent, $e^2 = e$ |
| $J_\lambda(e)$ | Peirce spaces for $\lambda \in \{0, \tfrac12, 1\}$ |
| Formally real | $\sum x_i^2 = 0 \Rightarrow x_i = 0$ |







## Further Reading

- Pascual Jordan, John von Neumann and Eugene Wigner, "On an algebraic generalization of the quantum mechanical formalism", *Annals of Mathematics* 35 (1934), 29–64, for the classification of formally real Jordan algebras.
- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, 1968), for the general structure theory.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for a modern exposition of the identities, the Peirce decomposition and the classification.
- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for the place of Jordan algebras among non-associative algebras.
- Efim Zel'manov, "On prime Jordan algebras", *Algebra i Logika* 18 (1979), for the structure theory over general fields.
