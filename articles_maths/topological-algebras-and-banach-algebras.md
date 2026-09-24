
# __Topological Algebras and Banach Algebras__

## Introduction

The algebra theory so far has been algebraic: an $R$-algebra is a module with a bilinear product, and nothing is assumed about a topology. The hypercomplex analysis needs more. Differentiation, integration and limits require a topology in which the algebra operations are continuous, and the completeness needed for the exponential and for the solution of differential equations requires that topology to come from a norm that is compatible with the product. This article supplies that layer: topological algebras, normed algebras, Banach algebras, the openness of the unit group, the exponential map, the Gelfand–Mazur theorem, and the precise sense in which a norm controls divisibility.

The base ring of this article is no longer an arbitrary commutative ring. Topology enters through a complete valued ground field, and we take

$$
\mathbb{K} = \mathbb{R} \quad \text{or} \quad \mathbb{K} = \mathbb{C},
$$

with the usual absolute value and its topology. Every algebra below is over $\mathbb{K}$, so that linear combinations with coefficients in $\mathbb{K}$ can be limited. This is the one point in the category where the field hypothesis cannot be avoided, and it is flagged here once and for all: the algebraic constructions of the preceding entries hold over a commutative ring, whereas the four hypercomplex-analysis articles require a complete valued ground field of the kind fixed here.

The four analysis articles —and— take place over general hypercomplex systems. This article stays general too: it develops the topological and Banach-algebra machinery once, without reference to a particular number system.

## Topological Algebras

**Definition.** A **topological algebra** over $\mathbb{K}$ is a $\mathbb{K}$-algebra $A$ equipped with a topology such that:

1. the addition $A \times A \to A$, $(x,y) \mapsto x + y$, is continuous;
2. the scalar multiplication $\mathbb{K} \times A \to A$, $(\lambda, x) \mapsto \lambda x$, is continuous;
3. the product $A \times A \to A$, $(x,y) \mapsto xy$, is continuous.

Here $A \times A$ carries the product topology and $\mathbb{K}$ its usual topology. A topological algebra is **Hausdorff** if its topology is, and in this article all topological algebras are Hausdorff, as they are for the purposes of analysis.

The continuity of a bilinear map is not automatic from separate continuity in infinite dimensions; the two are equivalent in the normed case below, which is the case used throughout the analysis.

**Proposition (the topology is determined at $0$).** Let $A$ be a topological algebra. The additive group of $A$ is a topological group, so its topology is translation invariant and is determined by the neighbourhoods of $0$: the translates $x + V$, as $V$ runs through a basis of neighbourhoods of $0$, form a basis of neighbourhoods of $x$, and a subset $U \subseteq A$ is open if and only if for every $x \in U$ there is a neighbourhood $V$ of $0$ with $x + V \subseteq U$. The closure of $\{0\}$ is

$$
\overline{\{0\}} = \bigcap \{V : V \text{ a neighbourhood of } 0\},
$$

a two-sided ideal of $A$ contained in every neighbourhood of $0$. Consequently $A$ is Hausdorff if and only if $\{0\}$ is closed, that is, if and only if this ideal is zero.

*Proof.* Translation $y \mapsto x + y$ is continuous because addition is, and it is a homeomorphism because it has the continuous inverse $y \mapsto -x + y$ (scalar multiplication by $-1$ is continuous). Hence $x + V$ is a neighbourhood of $x$ and every neighbourhood of $x$ is of that form, which gives the characterisation of open sets. For the closure, $x \in \overline{\{0\}}$ means that every neighbourhood of $x$ contains $0$, which by translation invariance says exactly that $x$ lies in every neighbourhood of $0$; that is the displayed identity. That set is an ideal: if $a, b \in \overline{\{0\}}$ then $a + b \in \overline{\{0\} + \{0\}} = \overline{\{0\}}$ and $-a \in \overline{\{0\}}$ by continuity of addition and of negation, while for any $x \in A$ the element $ax$ lies in $\overline{\{0\}\cdot x} \subseteq \overline{\{0\}}$ because right multiplication by $x$ is continuous; the left case is the same. Finally, in a topological group the Hausdorff property is equivalent to the closedness of the identity: if $\{0\}$ is closed and $x \neq y$ then $x - y \neq 0$, so some neighbourhood $W$ of $0$ misses $x - y$, and continuity of subtraction produces neighbourhoods $U, V$ of $0$ with $U - V \subseteq W$, whence $x + U$ and $y + V$ are disjoint. $\square$

**Remark.** The proposition is the reason a topological algebra can be specified by a neighbourhood basis of $0$ alone, and it is what makes the normed case below a special case: when the topology comes from a norm, the balls about $0$ are such a basis. If $A$ is not Hausdorff, the ideal $\overline{\{0\}}$ is the obstruction, and the quotient $A/\overline{\{0\}}$ is Hausdorff; every topological algebra below is Hausdorff, so this ideal is zero.

**Example.** $\mathbb{K}$ itself, with its usual topology, is a topological algebra; the product and sum are continuous by the elementary properties of limits. Any $\mathbb{K}$-subalgebra of a topological algebra, with the subspace topology, is a topological algebra.

**Example.** Let $X$ be a compact Hausdorff space. The algebra $C(X, \mathbb{K})$ of continuous $\mathbb{K}$-valued functions on $X$, with pointwise operations and the topology of uniform convergence, is a commutative unital topological algebra: addition, scalar multiplication and multiplication of functions are continuous with respect to the supremum norm $\|f\|_\infty = \sup_{x \in X} |f(x)|$.

**Example.** The matrix algebra $M_n(\mathbb{K})$ with the topology of entrywise convergence is a topological algebra; the product entries are polynomials in the entries of the factors, hence continuous.

**Example.** The real number-system algebras are topological algebras over $\mathbb{R}$: with the Euclidean topology on $\mathbb{R}^n$, the sum and the product are the polynomial maps given by the multiplication tables, hence continuous.

### The Unit Group

**Proposition.** Let $A$ be a unital topological algebra whose topology is induced by a norm. Then the group $A^\times$ of units is an open subset of $A$, and the inversion map $A^\times \to A^\times$, $x \mapsto x^{-1}$, is continuous.

*Proof.* Let $a \in A^\times$ and set $c = \|a^{-1}\|$. If $\|x - a\| < c^{-1}$ then $\|a^{-1}(x - a)\| \leq c\|x-a\| < 1$, so by the Neumann series below the element $1 + a^{-1}(x-a) = a^{-1}x$ is a unit, hence $x = a(a^{-1}x)$ is a unit. Thus the ball of radius $c^{-1}$ around $a$ lies in $A^\times$, so $A^\times$ is open. For continuity, write

$$
x^{-1} - a^{-1} = x^{-1}(a - x)a^{-1},
$$

so that $\|x^{-1} - a^{-1}\| \leq \|x^{-1}\|\,\|a^{-1}\|\,\|a - x\|$; since $\|x^{-1}\|$ is bounded on a small neighbourhood of $a$ by the previous estimate, the right side tends to $0$ as $x \to a$. $\square$

**Corollary.** In a unital normed algebra, an element $x$ with $\|1 - x\| < 1$ is a unit, and

$$
x^{-1} = \sum_{n \geq 0} (1 - x)^n, \qquad \|x^{-1}\| \leq \frac{1}{1 - \|1 - x\|}.
$$

*Proof.* This is the Neumann series, valid because the geometric series converges absolutely when $\|1 - x\| < 1$; the estimate follows from the submultiplicative inequality $\|(1-x)^n\| \leq \|1-x\|^n$. $\square$

The openness of $A^\times$ is the algebraic expression of the fact that invertibility is a stable condition, and it is used repeatedly in the hypercomplex analysis entries, where the set of units is open and the set of zero divisors is its closed complement together with $0$: in a finite-dimensional algebra the left zero divisors are exactly the elements $x$ with $\det\lambda_x = 0$, a closed condition on $x$.

## Normed Algebras

**Definition.** A **normed algebra** over $\mathbb{K}$ is a $\mathbb{K}$-algebra $A$ equipped with a norm $\|\cdot\| : A \to \mathbb{R}_{\geq 0}$ such that

$$
\|xy\| \leq \|x\|\,\|y\| \qquad \text{for all } x, y \in A,
$$

the norm being **submultiplicative**. If $A$ is unital one may and does assume $\|1\| = 1$, replacing $\|\cdot\|$ by the equivalent norm $\sup\{\|xy\| : \|y\| \leq 1\}$ when necessary.

The inequality $\|xy\| \leq \|x\|\|y\|$ is the compatibility between the metric and the algebraic structure. It implies the joint continuity of the product.

**Theorem.** Let $A$ be a normed algebra. Then the product is jointly continuous: for $(x_n) \to x_0$ and $(y_n) \to y_0$,

$$
\|x_n y_n - x_0 y_0\| \leq \|x_n - x_0\|\,\|y_n\| + \|x_0\|\,\|y_n - y_0\| \longrightarrow 0.
$$

Hence $A$, with its norm topology, is a topological algebra, and if $A$ is unital then $\|x^{-1}\| \geq \|x\|^{-1}$ for every unit.

*Proof.* The displayed estimate is the triangle inequality and submultiplicativity. The norm topology makes addition and scalar multiplication continuous by the definition of a normed vector space. For the last statement, $1 = \|xx^{-1}\| \leq \|x\|\|x^{-1}\|$. $\square$

**Definition.** A normed algebra is a **normed division algebra** if it is unital and every nonzero element is a unit; the norm is **multiplicative** if $\|xy\| = \|x\|\|y\|$ for all $x,y$. An algebra with a multiplicative norm is a **composition algebra**.

**Proposition.** Let $A$ be a normed algebra with multiplicative norm. Then $A$ has no zero divisors, and if $A$ is finite-dimensional and unital it is a normed division algebra.

*Proof.* If $xy = 0$ then $\|x\|\|y\| = \|xy\| = 0$, so $x = 0$ or $y = 0$. If $A$ is finite-dimensional, no zero divisors implies every nonzero element is a unit by *Centre, Units, Zero Divisors and Division Algebras*. $\square$

**Completion.** Let $A$ be a normed algebra and let $\bar{A}$ be the completion of the underlying normed space. The product extends uniquely to a continuous bilinear map $\bar{A} \times \bar{A} \to \bar{A}$, because it is uniformly continuous on bounded sets; the extension is associative when $A$ is, and unital with the same unit. Hence

$$
\text{the completion of a normed algebra is a Banach algebra.}
$$

## Banach Algebras

**Definition.** A **Banach algebra** is a normed algebra that is complete in its norm. A **Banach algebra over $\mathbb{K}$** means a Banach algebra over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$ in the sense above.

**Example.** $C(X,\mathbb{K})$ with the supremum norm is a commutative unital Banach algebra: uniform limits of continuous functions are continuous, and $\|fg\|_\infty \leq \|f\|_\infty\|g\|_\infty$.

**Example.** $M_n(\mathbb{K})$ with the operator norm $\|M\| = \sup\{\|Mv\| : \|v\| \leq 1\}$ is a unital Banach algebra; the operator norm is submultiplicative by submultiplicativity of the composition of operators.

**Example.** For a locally compact group $G$, the convolution algebra $L^1(G)$ with the $L^1$-norm is a Banach algebra, commutative when $G$ is abelian; it need not have a unit. Group algebras over a field are the subject of *Group Algebras*; the analytic version is quoted here only as an example.

**Example.** The finite-dimensional algebras $\mathbb{H}$ and $\mathbb{B}$ are Banach algebras: $\mathbb{H}$ with the norm $\|q\| = N(q)^{1/2}$, which is multiplicative because $N$ is; $\mathbb{B}$ with the operator norm transported across the isomorphism $\mathbb{B} \cong M_2(\mathbb{C})$ of *Biquaternion Algebra ($\mathbb{B}$)*.

### Finite-Dimensional Algebras

**Theorem.** Let $A$ be a finite-dimensional unital algebra over $\mathbb{K}$. Then $A$ carries a norm making it a normed algebra, and it is complete for it; consequently $A$ is a Banach algebra. Moreover all norms on $A$ are equivalent, so the topology is unique.

*Proof.* Choose a basis $e_1, \dots, e_m$ and let $\|\cdot\|_1$ be the $\ell^1$-norm in that basis; submultiplicativity may fail, so define

$$
\|x\| = \sup\{\|xy\|_1 : \|y\|_1 \leq 1\}.
$$

This is a norm: it is subadditive and absolutely homogeneous because the product is bilinear, and $\|x\| = 0$ gives $xe_j = 0$ for every $j$, hence $x = x \cdot \sum_j c_j e_j = 0$ where $1 = \sum_j c_j e_j$. It is equivalent to $\|\cdot\|_1$: expanding $x = \sum_i x_i e_i$ and $y = \sum_j y_j e_j$ with $\sum_j |y_j| \leq 1$ gives

$$
\|xy\|_1 \leq \sum_{i,j} |x_i|\,|y_j|\,\|e_ie_j\|_1 \leq C\,\|x\|_1, \qquad C = \max_{i,j}\|e_ie_j\|_1 ,
$$

so $\|x\| \leq C\|x\|_1$, and conversely if the two norms were not equivalent there would be a sequence with $\|x_n\|_1 = 1$ and $\|x_n\| \to 0$; a subsequence converges in $\|\cdot\|_1$ to some $x \ne 0$, and $\|x\| = \lim_n\|x_n\| = 0$, since $\|\cdot\|$ is continuous for $\|\cdot\|_1$ by the bound just proved — impossible for a norm. Hence the two norms are equivalent. Finally it is submultiplicative, by the definition of $\|\cdot\|$ and the bilinearity of the product: for $\|w\|_1 \leq 1$,

$$
\|xyw\|_1 = \|x(yw)\|_1 \leq \|x\|\,\|yw\|_1 \leq \|x\|\,\|y\|\,\|w\|_1 .
$$

Completeness follows from finite dimension and equivalence of the norm with $\|\cdot\|_1$. The last statement is the standard equivalence of all norms on a finite-dimensional $\mathbb{K}$-vector space. $\square$

**Corollary.** Every finite-dimensional unital $\mathbb{K}$-algebra — in particular $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$, $\mathbb{B}$, $\mathbb{D}$, $\mathbb{D}'$, every matrix algebra $M_n(\mathbb{K})$ and every Clifford algebra $\mathrm{Cl}_{p,q}$ — is a Banach algebra in its unique vector-space topology, and every $\mathbb{K}$-linear map between finite-dimensional algebras is continuous.

The uniqueness of the topology means that for finite-dimensional algebras the topological notions of convergence, continuity and differentiability do not depend on the norm chosen. This is what permits the hypercomplex-analysis entries to speak of the Euclidean topology on $\mathbb{H}$ or $\mathbb{B}$ without further qualification.

## The Unit Group and the Exponential

**Theorem.** Let $A$ be a unital Banach algebra. Then $A^\times$ is an open subset of $A$, inversion is continuous, and $A^\times$ is a topological group under multiplication. Moreover $A^\times$ is a **Banach Lie group**, and its Lie algebra is $A$ itself with the commutator bracket

$$
[x,y] = xy - yx.
$$

*Proof.* The first two statements are the proposition above specialised to a complete normed algebra. For the Lie structure, the exponential below gives local coordinates near $1$, and the Lie algebra of the group of units is the tangent space at $1$, identified with $A$; the bracket is the commutator because the group law is multiplication. $\square$

**Definition.** For $x \in A$, the **exponential** is

$$
\exp(x) = \sum_{n \geq 0} \frac{x^n}{n!}.
$$

**Theorem.** Let $A$ be a unital Banach algebra over $\mathbb{K}$. Then the series defining $\exp(x)$ converges absolutely for every $x$, with $\|\exp(x)\| \leq e^{\|x\|}$; the map $\exp : A \to A^\times$ is continuous; and

$$
\exp(x + y) = \exp(x)\exp(y) \quad \text{whenever } xy = yx.
$$

The derivative of $\exp$ at $0$ is the identity, so $\exp$ maps a neighbourhood of $0$ diffeomorphically onto a neighbourhood of $1$ in $A^\times$.

*Proof.* Absolute convergence follows from $\sum \|x\|^n/n! = e^{\|x\|} < \infty$ and completeness. The functional equation is the binomial theorem, valid because $x$ and $y$ commute. For the last statement, expand

$$
\exp(h) = 1 + h + O(\|h\|^2),
$$

so the Fréchet derivative of $\exp$ at $0$ is $\mathrm{id}_A$; the inverse function theorem in Banach spaces gives a local diffeomorphism, and the image lies in $A^\times$ because $\exp(x)\exp(-x) = 1$. $\square$

**Corollary (the exponential and inner automorphisms).** For $a, x \in A$,

$$
\exp(\mathrm{ad}_a)(x) = \exp(a)\,x\,\exp(-a),
$$

where $\mathrm{ad}_a(x) = [a,x]$. The inner automorphisms of $A$ therefore arise from exponentials of inner derivations, and the correspondence between derivations and automorphisms of *Automorphisms and Derivations of Algebras* is exact in the Banach setting.

**Example (units of the number systems).** The group of units of a finite-dimensional algebra is an open subset, as above. For the number systems:

| Algebra | $A^\times$ | Components |
|---|---|---|
| $\mathbb{R}$ | $\mathbb{R}\setminus\{0\}$ | $2$ |
| $\mathbb{C}$ | $\mathbb{C}\setminus\{0\}$ | $1$ |
| $\mathbb{H}$ | $\mathbb{H}\setminus\{0\} \cong \mathbb{R}_{>0} \times SU(2)$ | $1$ |
| $\mathbb{B}$ | $\mathbb{B}^\times \cong GL_2(\mathbb{C})$ | $1$ |
| $\mathbb{D}$ | $a^2 \neq b^2$ | $4$ |
| $\mathbb{D}'$ | $a \neq 0$ | $2$ |

The unit group of $\mathbb{B}$ is $GL_2(\mathbb{C})$ under the algebra isomorphism $\mathbb{B} \cong M_2(\mathbb{C})$, which is connected; that of $\mathbb{H}$ retracts onto the unit sphere $S^3 = SU(2)$, which is connected and simply connected.

## The Gelfand–Mazur Theorem

The norm constrains the division algebras that can exist over $\mathbb{C}$.

**Theorem (Gelfand–Mazur).** Let $A$ be a unital Banach algebra over $\mathbb{C}$ in which every nonzero element is invertible. Then $A$ is isometrically isomorphic to $\mathbb{C}$.

*Proof (sketch).* For $x \in A$ the spectrum $\sigma(x) = \{\lambda \in \mathbb{C} : x - \lambda 1 \notin A^\times\}$ is nonempty, compact and contained in the closed disc of radius $\|x\|$; nonemptiness is the deepest step and uses the analyticity of the resolvent $\lambda \mapsto (x - \lambda 1)^{-1}$ together with Liouville's theorem. If every nonzero element of $A$ is invertible then $\sigma(x)$ consists of a single point $\lambda(x)$ for each $x$, and $\lambda : A \to \mathbb{C}$ is a unital algebra homomorphism; it is an isometry by the spectral radius formula, and it is injective because $\lambda(x) = 0$ gives $x = 0$. $\square$

**Corollary.** There is no normed division algebra over $\mathbb{C}$ other than $\mathbb{C}$ itself, and every complex Banach algebra that is a division algebra is one-dimensional.

**Corollary (Hurwitz and Frobenius in the normed setting).** The finite-dimensional normed division algebras with multiplicative norm over $\mathbb{R}$ are exactly $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$ and the octonions $\mathbb{O}$ (Hurwitz); the associative ones among them are exactly $\mathbb{R}$, $\mathbb{C}$ and $\mathbb{H}$ (Frobenius). The octonions are non-associative, so they fall outside the associative range of this category; the three division algebras of the Frobenius list are treated in *Division Algebras*.

The Gelfand–Mazur theorem is the reason the hypercomplex analysis over $\mathbb{C}$ has no nontrivial finite-dimensional theory of division-algebra type: any complex Banach algebra whose elements are all divisible is $\mathbb{C}$. The interesting hypercomplex systems are either over $\mathbb{R}$ or have zero divisors, and the following section makes the distinction precise.

## Characters, the Gelfand Transform and Duality

Commutative Banach algebras over $\mathbb{C}$ are governed by their one-dimensional representations, and the theory of them is the analytical counterpart of the reconstruction of an algebra from its quotient fields.

**Definition.** Let $A$ be a commutative unital Banach algebra over $\mathbb{C}$. A **character** of $A$ is a nonzero algebra homomorphism $\chi : A \to \mathbb{C}$. The **maximal ideal space** (also called the **character space** or **Gelfand spectrum**) of $A$ is

$$
\operatorname{Max}(A) = \{\chi : \chi \text{ a character of } A\},
$$

topologised as a subset of the unit ball of the dual space $A'$ in the weak-$*$ topology. For a commutative ring the characters correspond to the maximal ideals, and for a Banach algebra the correspondence is a bijection.

**Theorem (characters and maximal ideals, standard).** Let $A$ be a commutative unital $\mathbb{C}$-Banach algebra. Every character is continuous of norm one, the map $\chi \mapsto \ker\chi$ is a bijection from $\operatorname{Max}(A)$ onto the set of maximal ideals of $A$, and $\operatorname{Max}(A)$ is a nonempty compact Hausdorff space in the weak-$*$ topology.

*Proof (sketch).* The kernel of a character is a proper ideal, and if $I \supseteq \ker\chi$ then $A/I$ is a quotient of $\mathbb{C}$, hence $\mathbb{C}$; so $\ker\chi$ is maximal. Conversely, if $M$ is maximal then $A/M$ is a unital complex Banach algebra whose only ideals are trivial, hence a division algebra, and Gelfand–Mazur gives $A/M \cong \mathbb{C}$; the quotient map is therefore a character. A maximal ideal of a unital Banach algebra is closed, because its closure is again a proper ideal — the open unit ball about $1$ consists of units, so no sequence from $M$ can converge to $1$ — hence $\ker\chi$ is closed and $\chi$, whose kernel has codimension one, is continuous. Compactness of $\operatorname{Max}(A)$ in the weak-$*$ topology follows from the Banach–Alaoglu theorem together with the closedness of the character conditions, and nonemptiness from the existence of maximal ideals. $\square$

**Theorem (Gelfand transform).** Let $A$ be a commutative unital $\mathbb{C}$-Banach algebra. The **Gelfand transform**

$$
a \longmapsto \hat a, \qquad \hat a(\chi) = \chi(a),
$$

is a continuous unital algebra homomorphism $A \to C(\operatorname{Max}(A))$ with $\|\hat a\|_\infty \leq \|a\|$ and

$$
\hat a\bigl(\operatorname{Max}(A)\bigr) = \sigma(a), \qquad \|\hat a\|_\infty = r(a) = \lim_{n\to\infty}\|a^n\|^{1/n},
$$

the **spectral radius formula**. The kernel of the Gelfand transform is the intersection of the maximal ideals, the **Jacobson radical** of $A$, so the transform is injective exactly when $A$ is semisimple.

*Proof (sketch).* Each $\hat a$ is continuous by definition of the weak-$*$ topology on $\operatorname{Max}(A)$, and multiplicativity and unitality are immediate from the definitions. The identification of the range of $\hat a$ with $\sigma(a)$ is the statement that $a - \lambda 1$ is non-invertible exactly when it lies in some maximal ideal, that is, when some character annihilates it. The spectral radius formula is the standard theorem on the convergence of the power series for the resolvent on the complement of $\sigma(a)$. $\square$

**Example (the Fourier transform).** For the convolution algebra $L^1(\mathbb{R})$ the characters are

$$
\chi_\xi(f) = \int_\mathbb{R}f(x)\,e^{-i\xi x}\,dx, \qquad \xi \in \mathbb{R},
$$

so $\operatorname{Max}\bigl(L^1(\mathbb{R})\bigr) = \mathbb{R}$ and the Gelfand transform is the Fourier transform, with $\|\hat f\|_\infty = r(f) \leq \|f\|_1$ for the spectral radius formula. For a finite abelian group $G$ the group algebra $\mathbb{C}[G]$ is semisimple with $\operatorname{Max}(\mathbb{C}[G])$ the character group $\hat G$, and the Gelfand transform is the discrete Fourier transform, $\mathbb{C}[G] \cong \prod_{\chi \in \hat G}\mathbb{C}$; the same computation over a general base ring is the content of *Group Algebras*.

**Definition.** A **$\mathrm{C}^*$-algebra** is a complex Banach algebra $A$ with an involution $a \mapsto a^*$ satisfying

$$
(ab)^* = b^*a^*, \qquad (a^*)^* = a, \qquad \|a^*a\| = \|a\|^2
$$

for all $a, b \in A$.

**Theorem (Gelfand duality; commutative Gelfand–Naimark).** Let $A$ be a commutative unital $\mathrm{C}^*$-algebra. Then the Gelfand transform is an isometric $*$-isomorphism $A \to C(\operatorname{Max}(A))$, so $A$ is recovered from the compact Hausdorff space $\operatorname{Max}(A)$; the assignment $A \mapsto \operatorname{Max}(A)$ is a contravariant equivalence between commutative unital $\mathrm{C}^*$-algebras with unital $*$-homomorphisms and compact Hausdorff spaces with continuous maps.

*Proof (sketch).* For a character of a $\mathrm{C}^*$-algebra one has $\chi(a^*) = \overline{\chi(a)}$, because $a = u + iv$ with $u,v$ self-adjoint and $\chi(u)$ is real; hence the Gelfand transform is a $*$-homomorphism. The $\mathrm{C}^*$-identity gives

$$
\|\hat a\|_\infty^2 = \|\widehat{a^*a}\|_\infty = r(a^*a) = \|a^*a\| = \|a\|^2,
$$

using the spectral radius formula and the fact that $a^*a$ is self-adjoint, so the transform is isometric; its image is a closed $*$-subalgebra of $C(\operatorname{Max}(A))$ separating points and containing the constants, hence all of $C(\operatorname{Max}(A))$ by the Stone–Weierstrass theorem. The equivalence statement is the functoriality of the constructions, a unital $*$-homomorphism $A \to B$ inducing a continuous map $\operatorname{Max}(B) \to \operatorname{Max}(A)$ by composition, and the inverse functor sending a compact space $X$ to $C(X)$. $\square$

**Corollary (the continuous functional calculus).** Let $a$ be a normal element of a unital $\mathrm{C}^*$-algebra $A$, so that $a^*a = aa^*$. Then there is a unique isometric $*$-isomorphism

$$
C(\sigma(a)) \longrightarrow C^*(a,1), \qquad f \longmapsto f(a),
$$

onto the $\mathrm{C}^*$-subalgebra generated by $a$ and $1$, and $f(g(a)) = (f \circ g)(a)$.

*Proof.* The subalgebra $C^*(a,1)$ is commutative, since $a$ and $a^*$ commute, so Gelfand duality identifies it with $C(\operatorname{Max}(C^*(a,1)))$; the map $a \mapsto \hat a$ is a homeomorphism of $\operatorname{Max}(C^*(a,1))$ onto $\sigma(a)$, and the inverse of the Gelfand transform is the required calculus. $\square$

The corollary supplies square roots of positive elements, moduli and the polar decomposition, and it is the technical heart of the spectral theorem. The non-commutative theory — the realisation of an abstract $\mathrm{C}^*$-algebra as operators on a Hilbert space, the Gelfand–Naimark–Segal construction, von Neumann algebras and the modular theory — is developed, which continues the present section with the involution present.

## The Norm and Divisibility

A norm and a norm form are different objects, and the difference governs what the analysis can detect.

**Definition.** Let $A$ be a $\mathbb{K}$-algebra. A **norm** on $A$ is a subadditive, positive-definite, absolutely homogeneous function $\|\cdot\| : A \to \mathbb{R}_{\geq 0}$; it vanishes only at $0$. A **norm form** on $A$ is a quadratic form $N : A \to \mathbb{K}$, possibly indefinite and possibly vanishing on nonzero elements.

**Proposition.** Let $A$ be a unital normed algebra. Then:

1. $\|x^{-1}\| \geq \|x\|^{-1}$ for every unit $x$;
2. if $\|1 - x\| < 1$ then $x$ is a unit, and $\|x^{-1}\| \leq (1 - \|1-x\|)^{-1}$;
3. if the norm is multiplicative, then $A$ has no zero divisors and $\|x^{-1}\| = \|x\|^{-1}$ for every unit $x$;
4. no norm can vanish on a nonzero element, so a norm never detects a zero divisor.

*Proof.* Statement 1 is $\|1\| \leq \|x\|\|x^{-1}\|$ with $\|1\| = 1$. Statement 2 is the Neumann series. Statement 3: multiplicativity gives $\|x\|\|y\| = \|xy\| = 0$ if $xy = 0$, and $\|x\|\|x^{-1}\| = \|1\| = 1$. Statement 4 is the positive definiteness of a norm. $\square$

**Example (the quaternions).** For $\mathbb{H}$ the Euclidean norm $\|q\| = N(q)^{1/2}$ is multiplicative, because the norm form $N(q) = \sum_\mu q_\mu^2$ is; so $\mathbb{H}$ is a normed division algebra, and $\|q^{-1}\| = \|q\|^{-1}$.

**Example (the biquaternions).** For $\mathbb{B}$ the quadratic form $N(\tilde{Q}) = \sum_\mu Q_\mu^2$ is complex-valued and vanishes on the nonzero zero divisors, so it is a norm form and not a norm. The Euclidean norm

$$
\|\tilde{Q}\|_E = \Bigl(\sum_{\mu} |Q_\mu|^2\Bigr)^{1/2} = \Bigl(\mathrm{Sc}(\tilde{Q}\tilde{Q}^\dagger)\Bigr)^{1/2}
$$

is a genuine norm, positive definite and vanishing only at $\tilde{Q} = 0$; it is not multiplicative, and it carries no information about divisibility: an element can be a zero divisor while having large Euclidean norm. This is the reason $\mathbb{B}$ is a Banach algebra but not a normed division algebra, and it is why the analysis over $\mathbb{B}$ must work with the norm form and the quadratic structure rather than with a multiplicative absolute value.

**Example (the split complex and dual numbers).** For $\mathbb{D}$ the form $N(a+bj) = a^2 - b^2$ is indefinite, so it is not a norm; for $\mathbb{D}'$ the form $N(a + b\varepsilon) = a^2$ vanishes on the maximal ideal $(\varepsilon)$. In both cases the Euclidean norm of the underlying $\mathbb{R}^2$ is a genuine norm, submultiplicative after a rescaling, but not multiplicative; the zero divisors are detected by the vanishing of the norm form, not by the norm.

## Summary

A **topological algebra** is a $\mathbb{K}$-algebra whose addition, scalar multiplication and product are continuous, and a **normed algebra** is one whose norm is submultiplicative, which makes the product jointly continuous. A **Banach algebra** is a complete normed algebra; the completion of a normed algebra is a Banach algebra. Every finite-dimensional $\mathbb{K}$-algebra is a Banach algebra in a unique topology, all norms on it being equivalent, so the number systems, the matrix algebras and the Clifford algebras are all Banach algebras.

In a unital normed algebra the **unit group** $A^\times$ is open and inversion is continuous, by the Neumann series; in a unital Banach algebra $A^\times$ is a Banach Lie group with Lie algebra $A$ under the commutator bracket, and the **exponential** $\exp(x) = \sum x^n/n!$ converges everywhere, satisfies $\exp(x+y) = \exp(x)\exp(y)$ for commuting $x,y$, and is a local diffeomorphism at $0$; inner derivations exponentiate to inner automorphisms, as in *Automorphisms and Derivations of Algebras*. The **Gelfand–Mazur theorem** states that a unital complex Banach algebra in which every nonzero element is invertible is $\mathbb{C}$; with Hurwitz and Frobenius this pins the normed real division algebras to $\mathbb{R}, \mathbb{C}, \mathbb{H}$ (associative) and to $\mathbb{O}$ as well without associativity.

A **norm** is positive definite and never vanishes on a nonzero element, whereas a **norm form** is a quadratic form that may vanish on the zero divisors; the norm form $N(\tilde{Q})$ of $\mathbb{B}$, being complex-valued and vanishing on the null set, is not a norm, and the Euclidean norm of $\mathbb{B}$ detects only the zero element. Divisibility is read from the norm form, not from the norm, and this distinction is what the hypercomplex analysis has to respect.

A **character** of a commutative unital complex Banach algebra is a nonzero homomorphism into $\mathbb{C}$, and the characters, equivalently the maximal ideals, form the compact Hausdorff **maximal ideal space** $\operatorname{Max}(A)$. The **Gelfand transform** $\hat a(\chi) = \chi(a)$ is a contractive unital homomorphism $A \to C(\operatorname{Max}(A))$ whose range on $a$ is $\sigma(a)$, with $\|\hat a\|_\infty = r(a) = \lim\|a^n\|^{1/n}$, and whose kernel is the Jacobson radical; it is the Fourier transform when $A = L^1(\mathbb{R})$ and the discrete Fourier transform when $A = \mathbb{C}[G]$. For a commutative unital **$\mathrm{C}^*$-algebra** the Gelfand transform is an isometric $*$-isomorphism onto $C(\operatorname{Max}(A))$, which is **Gelfand duality**, a contravariant equivalence with compact Hausdorff spaces; the **continuous functional calculus** for a normal element $a$ is the same theorem applied to the commutative $\mathrm{C}^*$-algebra $C^*(a,1)$, and identifies it with $C(\sigma(a))$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{K}$ | $\mathbb{R}$ or $\mathbb{C}$, the complete valued ground field here |
| $A$ | Topological / normed / Banach algebra over $\mathbb{K}$ |
| $\|\cdot\|$ | Submultiplicative norm; $\|xy\| \leq \|x\|\|y\|$ |
| $\|\cdot\|_\infty$ | Supremum norm on $C(X,\mathbb{K})$ |
| $A^\times$ | Group of units, open in a normed algebra |
| $(1-x)^{-1} = \sum_{n} x^n$ | Neumann series, valid for $\|x\| < 1$ |
| $\exp(x) = \sum_n x^n/n!$ | Exponential map, defined on a Banach algebra |
| $[x,y] = xy - yx$ | Commutator, the bracket of $A$ as Lie algebra of $A^\times$ |
| $\sigma(x)$ | Spectrum of $x$ |
| $N$ | Norm form; may be indefinite and may vanish |
| $\|\tilde{Q}\|_E$ | Euclidean norm of a biquaternion, $(\sum_\mu |Q_\mu|^2)^{1/2}$ |
| $C(X,\mathbb{K})$ | Continuous functions on compact $X$, a Banach algebra |
| $M_n(\mathbb{K})$ | Matrix algebra with operator norm |
| $SU(2)$ | Unit quaternions; $\mathbb{H}^\times \cong \mathbb{R}_{>0} \times SU(2)$ |
| $\mathbb{O}$ | Octonions, the non-associative normed real division algebra |
| $\chi$ | Character of a commutative unital complex Banach algebra |
| $\operatorname{Max}(A)$ | Maximal ideal space (character space) of $A$ |
| $\hat a(\chi) = \chi(a)$ | Gelfand transform of $a$ |
| $r(a) = \lim_n\|a^n\|^{1/n}$ | Spectral radius, $= \|\hat a\|_\infty$ |
| $C^*(a,1)$ | $\mathrm{C}^*$-subalgebra generated by a normal element $a$ and $1$ |





## Further Reading

- Walter Rudin, *Functional Analysis* (McGraw–Hill, 2nd ed. 1991), for normed algebras, the Neumann series and the spectrum.
- I. M. Gelfand, D. A. Raikov and G. E. Shilov, *Commutative Normed Rings* (Chelsea, 1964), for characters, the Gelfand transform and Gelfand duality.
- Charles E. Rickart, *General Theory of Banach Algebras* (Van Nostrand, 1960), for the maximal ideal space, the spectral radius formula, the functional calculus and the Gelfand–Mazur theorem.
- Garth Warner, *Topological Fields* (North-Holland, 1989), for topological algebras over valued fields.
- John B. Conway, *A Course in Functional Analysis* (Springer, 2nd ed. 1990), for Banach algebras, the exponential and spectral theory.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for finite-dimensional algebras and their unique topology.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for composition algebras and the Hurwitz theorem.
