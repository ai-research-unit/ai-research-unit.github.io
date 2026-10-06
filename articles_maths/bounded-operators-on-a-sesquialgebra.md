# __Bounded Operators on a Sesquialgebra__

## Introduction

The operators of a sesquialgebra are of two kinds, because the product is linear in the first slot and $\varsigma$-semilinear in the second: the $\mathbb{K}$-linear operators and the conjugate-linear ones, and the left multiplication belongs to the second class while the right multiplication belongs to the first. When the module carries a norm the bounded operators of each class form a Banach space. This article lays down that operator layer, which is the topological counterpart of the endomorphism algebras of *The Left and Right Multiplication Operators of a Sesquialgebra*.

Three facts organise the article. The two classes are each complete for the operator norm, and composition with the involution is an isometric isomorphism from the bounded linear operators onto the bounded conjugate-linear ones, so the two spaces are one Banach space read through two scalar rules. The union of the two classes is not closed under composition, since the composite of two conjugate-linear operators is linear, so no algebra structure has that union as its underlying set; the smallest algebra containing both is the direct sum, and it carries a $\mathbb{Z}/2$-grading whose graded pieces are the two classes, the parity of a composite being the product of the parities. And the norm topology is not the only natural one: the topology of pointwise convergence is coarser, it agrees with the norm topology exactly in finite dimension, while the uniform boundedness principle keeps the two in contact on a complete module.

The article defines the two classes and their norm, proves the completeness and reads the involution as the operator that exchanges them, treats the composition and the grading, compares the norm topology with the topology of pointwise convergence, and works the examples. The two parities are *The Left and Right Multiplication Operators of a Sesquialgebra*, §*The Two Parities*; the norm, the bounded maps and the completeness of the operator space are *Normed and Banach Spaces*, §*Bounded Linear Maps* and §*Completeness*, and *The Operator Algebra of a Banach Space*, §*The Bounded Operators of a Banach Space*; the pointwise convergence and the equicontinuous families are *Bounded Operators on a Topological Vector Space*, §*The Space of Continuous Operators*; the uniform boundedness principle is *Normed and Banach Spaces*, §*Uniform Boundedness*. Throughout $(\mathbb{K},\varsigma)$ is $\mathbb{R}$ or $\mathbb{C}$ with its continuous involution, $A$ is a normed sesquialgebra over $(\mathbb{K},\varsigma)$ in the sense of *Banach Sesquialgebras* when the norm is submultiplicative and in the sense of *Topological Sesquialgebras* otherwise, and the topology is the norm topology unless another one is named.

## The Two Classes of Operators

### The Definition and the Operator Norm

**Definition.** Let $T : A \to A$ be additive. Then $T$ is **$\mathbb{K}$-linear** if $T(\lambda x) = \lambda T(x)$ for all $\lambda \in \mathbb{K}$ and $x \in A$, and **conjugate-linear**, or **$\varsigma$-semilinear**, if $T(\lambda x) = \varsigma(\lambda)T(x)$. It is **bounded** if

$$
\lVert T\rVert = \sup\{\lVert Tx\rVert : x \in A,\ \lVert x\rVert \leq 1\} < +\infty .
$$

The bounded $\mathbb{K}$-linear operators form the space $B(A)$, the bounded conjugate-linear operators the space $B^{\varsigma}(A)$, and $\lVert T\rVert$ is the **operator norm** of $T$ in either class.

The two classes are the two endomorphism classes of the algebraic layer, read with the continuity that the norm imposes. For a sesquialgebra of full type with a nontrivial involution both are nonempty and different: the left multiplications lie in the second class, and the right multiplications in the first, by *The Left and Right Multiplication Operators of a Sesquialgebra*, §*The Two Parities*.

**Proposition (boundedness is continuity, in both classes).** For an additive $T : A \to A$ of either class the following are equivalent: $T$ is bounded; $T$ is continuous; $T$ is continuous at $0$; there is $C \geq 0$ with $\lVert Tx\rVert \leq C\lVert x\rVert$ for all $x$.

*Proof.* An additive map of either class satisfies $T(x) - T(y) = T(x-y)$ and $T(\lambda(x-y)) = \varsigma(\lambda)(Tx-Ty)$ for suitable $\lambda$, so it commutes with the translations in the appropriate sense and is continuous exactly when it is continuous at $0$. If $\lVert Tx\rVert \leq C\lVert x\rVert$ then $\lVert Tx - Ty\rVert \leq C\lVert x - y\rVert$ and $T$ is Lipschitz. Conversely a continuous $T$ is continuous at $0$, so there is $r > 0$ with $\lVert Tx\rVert \leq 1$ whenever $\lVert x\rVert \leq r$; then for $x \neq 0$ one has $\lVert T(rx/\lVert x\rVert)\rVert = \lvert \varsigma(r/\lVert x\rVert)\rvert \lVert Tx\rVert = (r/\lVert x\rVert)\lVert Tx\rVert \leq 1$, because the modulus of a scalar is fixed by $\varsigma$, and $\lVert Tx\rVert \leq r^{-1}\lVert x\rVert$. The last two conditions are recastings of the first, and the least constant is the supremum of the definition. $\square$

**Proposition (the three expressions of the norm).** For $T$ of either class,

$$
\lVert T\rVert = \sup_{\lVert x\rVert = 1}\lVert Tx\rVert = \sup_{x \neq 0}\frac{\lVert Tx\rVert}{\lVert x\rVert} , \qquad \lVert Tx\rVert \leq \lVert T\rVert\lVert x\rVert .
$$

*Proof.* The twist does not affect the scaling: for conjugate-linear $T$ one has $\lVert T(\mu x)\rVert = \lvert \varsigma(\mu)\rvert\lVert Tx\rVert = \lvert \mu\rvert\lVert Tx\rVert$, because an involution of $\mathbb{R}$ or $\mathbb{C}$ fixes the modulus, and for linear $T$ the same computation holds without $\varsigma$. The three suprema therefore range over the same values, and the inequality is the definition of the last one. $\square$

### The Completeness of the Two Classes

**Theorem ($B(A)$ is a Banach algebra and $B^{\varsigma}(A)$ a Banach space).** $B(A)$ is a unital algebra under the pointwise linear structure and the composition, the operator norm is submultiplicative on it, $\lVert ST\rVert \leq \lVert S\rVert\lVert T\rVert$ and $\lVert \mathrm{id}\rVert = 1$, and $B(A)$ is complete for it when $A$ is complete, hence a unital Banach algebra. The space $B^{\varsigma}(A)$ is a Banach space with the same norm when $A$ is complete.

*Proof.* For $B(A)$ this is the theorem of *Operators on a Banach Algebra*, §*The Bounded Operators*, whose proof uses only the completeness of $A$ and the submultiplicativity of the operator norm. For $B^{\varsigma}(A)$, let $(T_n)$ be Cauchy; for each $x$ the sequence $(T_nx)$ is Cauchy in $A$, with limit $Tx$, and $T$ is additive because the limits are and conjugate-linear because $\varsigma$ is continuous: $T(\lambda x) = \lim_n T_n(\lambda x) = \lim_n \varsigma(\lambda)T_nx = \varsigma(\lambda)Tx$. The uniformly bounded norms $\lVert T_n\rVert \leq M$ give $\lVert Tx\rVert \leq M\lVert x\rVert$, so $T$ is bounded, and $\lVert T - T_n\rVert \leq \sup_{m \geq n}\lVert T_m - T_n\rVert \to 0$, so the space is complete. $\square$

### The Involution as an Operator

**Proposition (composition with the involution).** Let $*$ be an isometric involution of $A$ and $* : A \to A$ the map $x \mapsto x^{*}$, read as an operator. Then $* \in B^{\varsigma}(A)$, $\lVert *\rVert = 1$, $*^{2} = \mathrm{id}$, and

$$
B(A) \longrightarrow B^{\varsigma}(A), \qquad T \longmapsto T \circ * ,
$$

is an isometric vector-space isomorphism, with inverse $S \mapsto S \circ *$.

*Proof.* The involution is additive, conjugate-linear, $*(\lambda x) = \varsigma(\lambda)x^{*}$, and isometric by hypothesis, so $* \in B^{\varsigma}(A)$ with norm one, and $*^{2} = \mathrm{id}$ because an involution has order two. The composite of a $\mathbb{K}$-linear $T$ with $*$ is conjugate-linear, and $\lVert T \circ *\rVert = \sup_{\lVert x\rVert\leq1}\lVert T(x^{*})\rVert = \lVert T\rVert$ because $*$ is a surjective isometry and its image of the unit ball is the unit ball. The assignment is additive and $\mathbb{K}$-linear, and $(T \circ *) \circ * = T$ and $(S \circ *) \circ * = S$, so it is bijective with the stated inverse. $\square$

**Remark.** The proposition is the reason the two classes are not two unrelated spaces: the bounded conjugate-linear operators are exactly the bounded linear operators followed or preceded by the involution, $B^{\varsigma}(A) = B(A) \circ * = * \circ B(A)$. The same statement at the level of the whole endomorphism algebra is *The Left and Right Multiplication Operators of a Sesquialgebra*, §*The Two Parities*, and the topology adds the isometry and the completeness.

## The Composition and the Grading

### The Parity of a Composite

**Proposition (the parity multiplication).** For operators of the two classes the composite is of the class given by

$$
B(A) \circ B(A) \subseteq B(A), \quad B(A) \circ B^{\varsigma}(A) \subseteq B^{\varsigma}(A), \quad B^{\varsigma}(A) \circ B(A) \subseteq B^{\varsigma}(A), \quad B^{\varsigma}(A) \circ B^{\varsigma}(A) \subseteq B(A),
$$

and in each case $\lVert ST\rVert \leq \lVert S\rVert\lVert T\rVert$.

*Proof.* Write the parities as a two-element group. The scalar rule of a composite of two additive maps is the product of the rules: if $T(\lambda x) = \sigma_T(\lambda)T(x)$ and $S(\lambda y) = \sigma_S(\lambda)S(y)$ with $\sigma_T, \sigma_S \in \{\mathrm{id}, \varsigma\}$, then $S(T(\lambda x)) = \sigma_S(\lambda)\sigma_T(\lambda)S(T(x))$ and $\sigma_S\sigma_T = \mathrm{id}$ exactly when the two rules agree. The norm inequality is the estimate of the preceding section read on $ST$. $\square$

**Corollary (the union is not an algebra).** Suppose $\varsigma \neq \mathrm{id}$. Then the union $B(A) \cup B^{\varsigma}(A)$ is not closed under composition, since the composite of two conjugate-linear operators is linear and is not conjugate-linear unless it vanishes; consequently the union is not the underlying set of an algebra under the composition, and in particular $B^{\varsigma}(A)$ is not a subalgebra of anything under it.

*Proof.* For conjugate-linear $S$ and $T$ the composite is linear by the proposition. It is conjugate-linear only if it is both linear and conjugate-linear, that is if $(\lambda - \varsigma(\lambda))STx = 0$ for all $\lambda$ and $x$; with $\varsigma \neq \mathrm{id}$ this forces $ST = 0$. So $ST$ lies outside the union as soon as $ST \neq 0$. $\square$

### The Graded Algebra

**Theorem (the direct sum is a graded Banach algebra).** Let

$$
\mathcal{B}(A) = B(A) \oplus B^{\varsigma}(A)
$$

with the componentwise vector structure, the norm $\lVert (T_0,T_1)\rVert = \lVert T_0\rVert + \lVert T_1\rVert$, and the product

$$
(T_0,T_1)(S_0,S_1) = (T_0S_0 + T_1S_1,\ T_0S_1 + T_1S_0) .
$$

Then $\mathcal{B}(A)$ is an associative unital algebra with unit $(\mathrm{id},0)$, the norm is submultiplicative, $\lVert (T_0,T_1)(S_0,S_1)\rVert \leq \lVert (T_0,T_1)\rVert\lVert (S_0,S_1)\rVert$, and $\mathcal{B}(A)$ is a Banach algebra when $A$ is complete. The direct sum is $\mathbb{Z}/2$-graded, with even part $B(A)$ and odd part $B^{\varsigma}(A)$, the two classes are its graded pieces, and the product of two homogeneous elements is homogeneous of the product of the parities.

*Proof.* The product formula is the parity rule written out, and it is associative because the four cases reduce to the associativity of the composition in the two classes: the even part of a product of three factors collects the terms with an even number of odd factors, and the two ways of bracketing give the same because the composition is associative and the mixed products distribute. The unit is $(\mathrm{id},0)$. For submultiplicativity,

$$
\lVert (T_0S_0 + T_1S_1,\ T_0S_1 + T_1S_0)\rVert \leq (\lVert T_0\rVert\lVert S_0\rVert + \lVert T_1\rVert\lVert S_1\rVert) + (\lVert T_0\rVert\lVert S_1\rVert + \lVert T_1\rVert\lVert S_0\rVert) = \lVert (T_0,T_1)\rVert\lVert (S_0,S_1)\rVert ,
$$

by the triangle inequality and the submultiplicativity in each class. Completeness is that of a finite direct sum of complete spaces. $\square$

**Remark (the sum map is injective).** For $\varsigma \neq \mathrm{id}$ the evaluation $(T_0,T_1) \mapsto T_0 + T_1$ is an injective map $\mathcal{B}(A) \to \operatorname{End}(A)$: if $T_0 + T_1 = 0$ then $T_0 = -T_1$ is at once $\mathbb{K}$-linear and conjugate-linear, so $(\lambda - \varsigma(\lambda))T_0 = 0$ for every $\lambda$, and $\varsigma \neq \mathrm{id}$ forces $T_0 = T_1 = 0$. The grading of $\mathcal{B}(A)$ is therefore visible on its image, and an additive operator has at most one decomposition into an even and an odd part.

**Remark (the failure of a single algebra and its repair).** The theorem is the precise sense in which a single algebra contains both classes: the classes are not subalgebras of $\mathcal{B}(A)$ as ungraded pieces, since the odd part is not closed under the product, but they are its homogeneous components, and the grading records which class an operator comes from. The involution is the odd element $(0,*)$, and $(0,*)(0,*) = (*^{2},0) = (\mathrm{id},0)$, which is the reason the graded algebra is not the plain direct sum of two algebras; the operator thus exhibits the same order-two obstruction as the datum involution itself.

## The Topology of Pointwise Convergence

### The Strong Operator Topology

**Definition.** The **topology of pointwise convergence**, or the **strong operator topology**, on the operators is the locally convex topology of the seminorms $T \mapsto \lVert Tx\rVert$ for $x \in A$; a net converges, $T_\alpha \to T$, exactly when $T_\alpha x \to Tx$ in $A$ for every $x$. It is the topology induced from the product topology of $A^{A}$.

**Proposition (elementary properties).** The topology of pointwise convergence is Hausdorff, locally convex and coarser than the norm topology, and the operator norm is lower semicontinuous for it.

*Proof.* It is a locally convex topology by definition, Hausdorff because a nonzero operator differs from $0$ at some $x$; it is coarser than the norm topology because $\lVert T_\alpha x - Tx\rVert \leq \lVert T_\alpha - T\rVert\lVert x\rVert$, so norm convergence gives pointwise convergence. For the lower semicontinuity, $\{T : \lVert T\rVert > c\}$ is the union over $x$ of $\{T : \lVert Tx\rVert > c\lVert x\rVert\}$, which is open. $\square$

**Theorem (coincidence with the norm topology).** On $B(A)$, or on $B^{\varsigma}(A)$, the topology of pointwise convergence agrees with the norm topology if and only if $A$ is finite-dimensional.

*Proof.* If $A$ is finite-dimensional then $B(A)$ and $B^{\varsigma}(A)$ are finite-dimensional and all Hausdorff locally convex topologies on them agree. Conversely suppose the two topologies agree on $B(A)$; then the norm-open unit ball $\{T : \lVert T\rVert < 1\}$ is open for the pointwise topology, so it contains a basic neighbourhood $\{T : \lVert Tx_i\rVert < \epsilon,\ i = 1,\dots,n\}$ for some $x_1,\dots,x_n$. If $A$ is infinite-dimensional there is $x$ of norm one outside the span of the $x_i$; choose by Hahn–Banach a functional $f$ with $f(x) = 1$ and $f(x_i) = 0$ for all $i$, and for $y \in A$ let $T_y = f(\cdot)y$. Then $T_y$ lies in the basic neighbourhood because $T_yx_i = f(x_i)y = 0$, while $\lVert T_y\rVert = \lVert f\rVert\lVert y\rVert$ is unbounded in $y$, contradicting the containment in the unit ball. So $A$ is finite-dimensional, and the same argument with $B(A)$ replaced by $B^{\varsigma}(A)$ is carried by the isometric isomorphism of §*The Involution as an Operator*. $\square$

### The Uniform Boundedness Principle

**Theorem (pointwise boundedness implies norm boundedness).** Let $A$ be a Banach space and $\mathcal{F} \subseteq B(A)$ with $\sup_{T \in \mathcal{F}}\lVert Tx\rVert < +\infty$ for every $x$. Then $\sup_{T \in \mathcal{F}}\lVert T\rVert < +\infty$.

*Proof.* This is the uniform boundedness principle of *Normed and Banach Spaces*, §*Uniform Boundedness*; the completeness of $A$ is its hypothesis, and the conclusion is that a pointwise bounded family of bounded operators is norm bounded. $\square$

**Corollary (sequences of the strong topology).** Let $A$ be a Banach sesquialgebra and let $(T_n)$ converge pointwise to $T$. Then $(T_n)$ is norm bounded, $T$ is bounded, and $\lVert T\rVert \leq \liminf_n\lVert T_n\rVert$; in particular the pointwise limit of a sequence of bounded operators is bounded. On an infinite-dimensional $A$ the pointwise topology is not normable.

*Proof.* Pointwise convergence makes $(T_n)$ pointwise bounded, so it is norm bounded by the theorem, and $T$ is additive; the bound $\lVert Tx\rVert = \lim_n\lVert T_nx\rVert \leq (\sup_n\lVert T_n\rVert)\lVert x\rVert$ makes $T$ bounded, with the stated estimate on the norms. For the last statement, a normable topology has a bounded neighbourhood, namely a ball of a norm defining it; but a basic neighbourhood of the pointwise topology, $\{T : \lVert Tx_i\rVert < \epsilon,\ i = 1,\dots,n\}$, is not a bounded set, since it contains the operators $T_y = f(\cdot)y$ of §*The Strong Operator Topology*, whose norms $\lVert T_y\rVert = \lVert f\rVert\lVert y\rVert$ are arbitrarily large. Hence the pointwise topology has no bounded neighbourhood and is not normable. $\square$

The corollary is the exact point at which the sesquilinear layer needs the completeness of the bilinear layer: separate continuity of the product gives the continuity of the one-sided multiplications without any completeness, but the passage from pointwise convergence to norm bounds and the normability question are properties of the complete norm and are used where a limit of operators is taken.

## The Relation to the Endomorphism Algebras of the Layer

**Proposition (the bounded operators inside the endomorphism algebras).** Let $\operatorname{End}_{\mathbb{K}}(A)$ be the algebra of all $\mathbb{K}$-linear maps and $\operatorname{End}^{\varsigma}_{\mathbb{K}}(A)$ the vector space of all conjugate-linear maps. Then

$$
B(A) = \{T \in \operatorname{End}_{\mathbb{K}}(A) : T \text{ continuous}\} , \qquad B^{\varsigma}(A) = \{T \in \operatorname{End}^{\varsigma}_{\mathbb{K}}(A) : T \text{ continuous}\} ,
$$

and the spaces of the algebraic layer are recovered by forgetting the norm, with $\mathcal{B}(A)$ reducing to the graded algebra $\operatorname{End}_{\mathbb{K}}(A) \oplus \operatorname{End}^{\varsigma}_{\mathbb{K}}(A)$.

*Proof.* Boundedness is continuity in each class, by §*The Two Classes of Operators*; the algebraic statements are the definitions of the two endomorphism spaces of *The Left and Right Multiplication Operators of a Sesquialgebra*, §*The Two Parities*. $\square$

**Remark.** The proposition is the sense in which the present article adds a norm and nothing algebraically: the operator layer of the sesquialgebra is the algebraic layer of Part I restricted to the continuous maps and completed. On a finite-dimensional $A$ there is nothing to restrict, since every map is continuous, and $\mathcal{B}(A)$ is the graded algebra of all operators; on an infinite-dimensional $A$ the restriction is proper, and the left multiplication of an unbounded element would be the first thing to leave it. In a normed sesquialgebra every element has bounded one-sided multiplications, so no such element occurs, and that is the subject of *The Bounded Left and Right Multiplication Operators of a Sesquialgebra*.

## Examples

### The Field

**Example (the field, verdict: two copies of $\mathbb{C}$).** Let $A = \mathbb{C}$ with the modulus and $\varsigma$ the conjugation. The bounded linear operators are the multiplications $z \mapsto cz$, so $B(A) \cong \mathbb{C}$; the bounded conjugate-linear operators are the maps $z \mapsto c\bar z$, so $B^{\varsigma}(A) \cong \mathbb{C}$ as a real vector space, via the involution $z \mapsto \bar z$. The graded algebra $\mathcal{B}(A)$ is $\mathbb{R}$-dimensional of dimension four, with even part the two-dimensional $B(A)$ and odd part the two-dimensional $B^{\varsigma}(A)$; the involution is the odd element $z \mapsto \bar z$.

### The Matrices

**Example (the matrices, verdict: the sandwiches span the conjugate-linear operators).** Let $A = M_n(\mathbb{C})$ with the operator norm, the conjugation and the product $S \star T = ST^{*}$. The bounded linear operators are all the linear maps, of complex dimension $n^{2}$; and every bounded conjugate-linear map is a finite sum of sandwich operators $X \mapsto AX^{*}B$, since the matrix units give $X \mapsto E_{ij}X^{*}E_{kl}$ and these span. The involution $X \mapsto X^{*}$ is the sandwich $S_{1,1}$ of *The Sesquilinear Sandwich Operator*, §*The Definition*, and it is the odd element of the graded algebra that generates the whole odd part by composition with the linear operators, as §*The Involution as an Operator* states.

### The Sequences

**Example (the sequences, verdict: the shift has no conjugate-linear partner).** Let $A = \ell^{1}$ with the norm, the termwise conjugation and the termwise product, which is submultiplicative. The left shift $T(x_0,x_1,\dots) = (x_1,x_2,\dots)$ is bounded and linear; the map $x \mapsto \bar x$ followed by the left shift is the bounded conjugate-linear operator $T \circ *$, and $T \circ *$ has the same norm as $T$ by §*The Involution as an Operator*. The operator norm of a sandwich is estimated in *The Bounded Sesquilinear Sandwich*.

## Summary

The operators of a sesquialgebra fall into two classes, the $\mathbb{K}$-linear and the conjugate-linear, and a norm makes each of them a Banach space: $B(A)$ is a unital Banach algebra for the composition and the operator norm, with $\lVert ST\rVert \leq \lVert S\rVert\lVert T\rVert$, and $B^{\varsigma}(A)$ is a Banach space for the same norm in which boundedness, continuity and a finite Lipschitz constant agree. Composition with the isometric involution is an isometry $B(A) \to B^{\varsigma}(A)$, so the two spaces are one space read through two scalar rules, and the left multiplications lie in the second while the right multiplications lie in the first.

The union of the two classes is not closed under composition, the composite of two conjugate-linear operators being linear, so it is not the underlying set of an algebra; the smallest algebra containing the classes is the graded direct sum $\mathcal{B}(A) = B(A) \oplus B^{\varsigma}(A)$ with the parity product and the norm $\lVert T_0\rVert + \lVert T_1\rVert$, a graded Banach algebra whose homogeneous components are exactly the two classes and whose unit is even and whose involution is odd. The norm topology on the operators is not the only natural one: the topology of pointwise convergence is coarser and locally convex, it agrees with the norm topology exactly when $A$ is finite-dimensional, and on a complete $A$ the uniform boundedness principle converts pointwise boundedness into norm boundedness, so a pointwise convergent sequence of bounded operators has a bounded limit and converges in no finer a sense than the strong one. The bounded operators are the continuous ones inside the endomorphism algebras of the algebraic layer, and the layer of the next articles is their use in reading the product.

## Summary of Notation

| symbol | meaning |
|---|---|
| $B(A)$ | the bounded $\mathbb{K}$-linear operators, $A \to A$ |
| $B^{\varsigma}(A)$ | the bounded conjugate-linear operators, $A \to A$ |
| $\lVert T\rVert = \sup_{\lVert x\rVert\leq1}\lVert Tx\rVert$ | the operator norm, on both classes |
| $T(\lambda x) = \varsigma(\lambda)T(x)$ | the defining rule of the conjugate-linear class |
| $* \in B^{\varsigma}(A)$, $\lVert *\rVert = 1$ | the isometric involution as the odd operator |
| $T \mapsto T \circ *$ | the isometric isomorphism $B(A) \to B^{\varsigma}(A)$ |
| $B^{\varsigma}(A) \circ B^{\varsigma}(A) \subseteq B(A)$ | the parity of a composite of two odd operators |
| $\mathcal{B}(A) = B(A) \oplus B^{\varsigma}(A)$ | the graded Banach algebra of the two classes |
| $\lVert T_0\rVert + \lVert T_1\rVert$ | the norm on the graded sum, submultiplicative |
| topology of pointwise convergence | $T_\alpha \to T$ iff $T_\alpha x \to Tx$ for all $x$ |
| norm topology $=$ pointwise topology | exactly when $A$ is finite-dimensional |
| $\sup_T\lVert Tx\rVert < \infty \Rightarrow \sup_T\lVert T\rVert < \infty$ | uniform boundedness on a complete $A$ |

## Further Reading

- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume I* (Academic Press, 1983), for the strong operator topology, the norm topology and the uniform boundedness principle in the operator setting.
- Theodore W. Palmer, *Banach Algebras and the General Theory of ${}^*$-Algebras, Volume I* (Cambridge University Press, 1994), for the operator spaces attached to an algebra with an involution and the grading of the compositions.
- Nicolas Bourbaki, *Topological Vector Spaces, Chapters 1–5* (Springer, 1987), for the pointwise convergence, the equicontinuous families and the topologies of the operator spaces.
- John B. Conway, *A Course in Functional Analysis* (Springer, second edition, 1990), for the bounded operators of a normed space and the topologies on their space.
- The companion articles of this series: *Topological Sesquialgebras*, *Banach Sesquialgebras*, *The Left and Right Multiplication Operators of a Sesquialgebra*, *The Bounded Left and Right Multiplication Operators of a Sesquialgebra* and *The Sesquilinear Adjoint Operator*.
