
# __Non-Archimedean Functional Analysis__

## Introduction

A norm on a vector space over a non-Archimedean field is required to satisfy the strong triangle inequality $\lVert x + y \rVert \leq \max(\lVert x \rVert, \lVert y \rVert)$, and the resulting theory of normed and Banach spaces differs from the classical one in ways that are not merely technical. Some of the cornerstones survive: completeness makes a non-Archimedean Banach space a Baire space, so the open mapping theorem, the closed graph theorem and the uniform boundedness principle hold with the same proofs. Others fail badly: the Hahn–Banach theorem holds for all normed spaces over $K$ exactly when $K$ is spherically complete, so over $\mathbb{C}_p$ there exist normed spaces with no nonzero continuous linear functional at all; there are no inner products with a positivity property, so Hilbert space theory has no analogue and orthogonal projection must be replaced by the theory of orthogonal bases and complementation; and the unit ball of an infinite-dimensional Banach space is never compact, so compactness is replaced by the weaker notion of a compactoid set.

This article develops the theory from the definitions. It sets out the geometric consequences of the strong triangle inequality for normed spaces, treats the spaces $c_0(I)$ and $\ell^\infty(I)$ and computes the dual of the former, defines orthogonal and orthonormal families and proves that the normed spaces with an orthogonal basis are exactly the spaces isometric to some $c_0(I)$, states and proves the elementary part of the open mapping and closed graph theorems and of the uniform boundedness principle, states Ingleton's theorem characterising the fields for which Hahn–Banach holds, treats spherically complete fields, defines compactoid sets and proves the basic facts about them, and closes with the polar and duality theory and with the connections to the Tate algebra of *Rigid Analytic Functions* and the measures of *p-adic Integration*.

The prerequisites are *Absolute Values, Valuations and Completions* and *Local Fields* for the valued fields, *Normed and Banach Spaces* for the classical theory that is being adapted, *Topological Algebras and Banach Algebras* for the Banach-algebra language, *p-adic Analysis* and *Rigid Analytic Functions* for the examples, and *Modules* for bases and direct sums. The Archimedean theory in its full modern form is in this Part; the comparison with it is made where it is illuminating, and the reader is referred there for the theorems that have no non-Archimedean analogue. Throughout, $K$ is a complete non-Archimedean field with a nontrivial absolute value $\lvert \cdot \rvert$, valuation ring $K^\circ$ and residue field $k$; all vector spaces are over $K$ and all norms take values in the value group of $K$ extended by $0$.

## Normed Spaces over a Non-Archimedean Field

### Definitions and Elementary Geometry

**Definition.** A **seminorm** on a $K$-vector space $E$ is a map $\lVert \cdot \rVert : E \to [0,\infty)$ with $\lVert 0 \rVert = 0$, $\lVert \lambda x \rVert = \lvert \lambda \rvert \lVert x \rVert$ and $\lVert x + y \rVert \leq \max(\lVert x \rVert, \lVert y \rVert)$; it is a **norm** if $\lVert x \rVert = 0$ implies $x = 0$. A **normed space** is a pair $(E,\lVert\cdot\rVert)$; it is a **Banach space** if it is complete for the metric $d(x,y) = \lVert x - y \rVert$. The **unit ball** is $B_E = \{x : \lVert x \rVert \leq 1\}$ and the **unit sphere** is $S_E = \{x : \lVert x \rVert = 1\}$.

**Proposition (geometry).** In a normed space over $K$ the following hold.

**(a)** Every triangle is isosceles: if $\lVert x \rVert > \lVert y \rVert$ then $\lVert x + y \rVert = \lVert x \rVert$.

**(b)** The closed balls $B(a,r) = \{x : \lVert x - a \rVert \leq r\}$ and the open balls $B^-(a,r) = \{x : \lVert x - a \rVert < r\}$ are clopen, and any two balls are either disjoint or one contains the other.

**(c)** Every point of a ball is a centre of it: if $\lVert b - a \rVert < r$ then $B(a,r) = B(b,r)$.

**(d)** A series $\sum_n x_n$ converges if and only if $x_n \to 0$; and if it converges, then $\lVert\sum_n x_n\rVert \leq \sup_n \lVert x_n \rVert$, with equality whenever the maximum is attained and the terms attaining it do not cancel.

**(e)** If $K$ is locally compact then $E$ is locally compact exactly when it is finite-dimensional, and in that case the closed unit ball of $E$ is compact; if $K$ is not locally compact then no nonzero normed space over $K$ is locally compact, not even a one-dimensional one.

**Proof.** Part (a) is the strong triangle inequality: $\lVert x \rVert = \lVert (x+y) - y \rVert \leq \max(\lVert x+y \rVert, \lVert y \rVert) = \lVert x + y \rVert$ when $\lVert x+y \rVert \geq \lVert y \rVert$, and the reverse inequality is the strong triangle inequality; the case $\lVert x+y\rVert < \lVert y \rVert$ is excluded because it would give $\lVert x \rVert < \lVert y \rVert$. For (b), if $\lVert x - a \rVert > r$ then $B(x,r) \cap B(a,r) = \emptyset$, by (a) applied to $(y-x) + (x-a)$; hence the closed ball is open, and the open ball is closed by the same argument, so the balls are clopen; nesting is the isosceles property applied to the centres. Part (c) is (a) applied to the difference. Part (d) is the non-Archimedean convergence criterion together with (a). Part (e): a finite-dimensional space over a locally compact $K$ is homeomorphic to $K^n$ with the sup norm, hence locally compact with compact unit ball; the converse for infinite dimension, and the statement that no nonzero normed space over a non-locally-compact $K$ is locally compact, are Monna's theorem: a locally compact normed space over $K$ has a locally compact one-dimensional subspace, hence forces $K$ locally compact, and over such a $K$ an infinite-dimensional space has non-compact unit ball. The standard reference is *Non-Archimedean Functional Analysis* of van Rooij. $\square$

### The Standard Spaces

**Definition.** For a set $I$ let
$$
c_0(I) = \Bigl\{ (a_i)_{i \in I} \in K^I : \text{for every } \epsilon > 0 \text{ the set } \{i : \lvert a_i \rvert \geq \epsilon\} \text{ is finite} \Bigr\},
$$
and let $\ell^\infty(I)$ be the space of all bounded families $(a_i)_{i\in I}$, both with the supremum norm $\lVert a \rVert_\infty = \sup_i \lvert a_i \rvert$. For $I = \mathbb{N}$ these are written $c_0$ and $\ell^\infty$.

**Theorem.** $c_0(I)$ and $\ell^\infty(I)$ are Banach spaces over $K$, with $c_0(I) \subseteq \ell^\infty(I)$ a closed subspace, and the dual of $c_0(I)$ is isometrically $\ell^\infty(I)$:
$$
c_0(I)' \cong \ell^\infty(I), \qquad \lVert f \rVert = \sup_{\lVert a \rVert_\infty \leq 1} \lvert f(a) \rvert = \sup_i \lvert f(e_i) \rvert,
$$
where $e_i$ is the family that is $1$ at $i$ and $0$ elsewhere.

**Proof.** Completeness of $\ell^\infty$ is the completeness of a product of complete spaces restricted by a closed condition, and $c_0$ is closed in $\ell^\infty$ because a uniform limit of null families is null. For the duality, let $f \in c_0(I)'$ and put $b_i = f(e_i)$; every $a \in c_0(I)$ is the norm-convergent sum $\sum_i a_i e_i$, so $f(a) = \sum_i a_i b_i$ by continuity, and $\lvert f(a) \rvert \leq \lVert a \rVert_\infty \sup_i \lvert b_i \rvert$. The family $(b_i)$ is bounded because $\lvert b_i \rvert \leq \lVert f \rVert$; conversely a bounded family $(b_i)$ defines a functional of norm $\sup_i \lvert b_i \rvert$, the bound being attained on the unit vectors. $\square$

**Example (the Tate algebra is a $c_0$).** The Tate algebra $T_n = K\langle \xi_1,\dots,\xi_n\rangle$ of *Rigid Analytic Functions*, with its Gauss norm, is isometric as a Banach space to $c_0(\mathbb{N}^n)$: the monomials $\xi^\nu$ satisfy $\lVert\sum_\nu a_\nu \xi^\nu\rVert = \max_\nu \lvert a_\nu \rvert$ by the Gauss lemma, so they form an orthonormal family, and the coefficient families are exactly the null families on $\mathbb{N}^n$. The multiplicative structure is additional to the Banach space structure.

**Example (spaces of continuous functions).** For a compact topological space $X$ the space $C(X,K)$ of continuous functions with the supremum norm is a Banach space, and for $X = \mathbb{Z}_p$ its dual is the space of $p$-adic measures of *p-adic Integration*, with the Amice transform giving the coefficients of the dual element in the variable $\binom{x}{n}$.

## Orthogonal Bases and the Structure of Normed Spaces

### Orthogonal Families

**Definition.** A family $(e_i)_{i \in I}$ of nonzero vectors of a normed space $E$ is **orthogonal** if
$$
\Bigl\lVert \sum_{i \in F} a_i e_i \Bigr\rVert = \max_{i \in F} \lvert a_i \rvert \lVert e_i \rVert
$$
for every finite $F \subseteq I$ and all $a_i \in K$; it is **orthonormal** if in addition $\lVert e_i \rVert = 1$ for all $i$. A family is an **orthogonal basis** of $E$ if it is orthogonal and every vector of $E$ is the limit of the net of its finite partial sums $\sum_{i\in F} a_i e_i$.

**Proposition.** A family $(e_i)_{i \in I}$ of nonzero vectors is orthogonal if and only if each of its finite subfamilies is. If $(e_i)$ is orthogonal and $x$ lies in the closed span of the family, then $x = \sum_i a_ie_i$ for a unique family $(a_i)$ with $a_i\|e_i\|\to0$, and
$$
\lVert x \rVert = \sup_{i \in I} \lvert a_i \rvert \lVert e_i \rVert .
$$
In particular an orthogonal family is topologically free.

**Proof.** The first statement is the definition restricted to finite index sets. For the expansion, the norm is continuous and on finite sums it is given by the orthogonality condition, so $\lVert x\rVert = \lim_F \max_{i\in F}\lvert a_i\rvert\lVert e_i\rVert = \sup_i \lvert a_i\rvert\lVert e_i\rVert$ along the net of finite subsets. For uniqueness, if $\sum_i a_ie_i = \sum_i b_ie_i$ then for every finite $F$ one has $\max_{i\in F}\lvert a_i - b_i\rvert\lVert e_i\rVert = \lVert \sum_{i\in F}(a_i-b_i)e_i\rVert$, and the right-hand side tends to $0$ as $F$ grows, so $a_j = b_j$ for each fixed $j$. $\square$

### The Structure Theorem

**Theorem.** A normed space $E$ over $K$ admits an orthogonal basis if and only if $E$ is isometrically isomorphic to $c_0(I)$ for some set $I$. In that case the images of the canonical unit vectors form an orthonormal basis.

**Proof.** In $c_0(I)$ the unit vectors $e_i$ form an orthonormal basis: for a finite sum $\lVert\sum a_ie_i\rVert_\infty = \max_i\lvert a_i\rvert$, and the span of the $e_i$ is dense because a null family is approximated by its finite partial sums. Conversely, if $(e_i)$ is an orthogonal basis of $E$, the map $(a_i) \mapsto \sum_i a_i e_i$ is a linear isometry of $c_0(I)$ onto $E$: it is norm-preserving on finite sums by orthogonality, it is well defined and continuous for null families, and it is surjective by the definition of a basis. $\square$

**Remark (which spaces have orthogonal bases).** Not every Banach space over $K$ has one. Over a discretely valued field the question is governed by the structure of the unit ball, and there are Banach spaces with no orthogonal basis; over a spherically complete field the theory of the next section still does not produce bases, which are an extra hypothesis rather than a theorem. The spaces with orthogonal bases are precisely the isometric copies of the $c_0(I)$, and they are the non-Archimedean analogues of the classical spaces with an unconditional basis.

**Corollary (orthogonalisation lemma).** Let $K$ be spherically complete and let $x_1,\dots,x_n$ be linearly independent vectors of norm $1$ in a normed space $E$ over $K$. Then there is an orthonormal family $y_1,\dots,y_n$ spanning the same subspace, each $y_j$ obtained from $x_j$ by subtracting a $K^\circ$-linear combination of $y_1,\dots,y_{j-1}$; consequently $\lVert \sum_j a_jx_j \rVert \leq \max_j \lvert a_j \rvert$ for all $a_j \in K$, and every finite-dimensional subspace of $E$ has an orthogonal basis and admits a projection of $E$ onto it of norm $1$.

**Proof sketch.** Over a spherically complete field every one-dimensional subspace has a linear projection of norm $1$ onto it, by the Hahn–Banach theorem applied to a norm-attaining functional; the induction is then the classical orthogonalisation, subtracting from $x_j$ the component in the span of $y_1,\dots,y_{j-1}$ furnished by such a projection, and the induction hypothesis maintains $\lVert y_j\rVert = 1$. The norm-1 projection onto the whole finite-dimensional subspace follows by composing. $\square$

## Duality and the Hahn–Banach Theorem

### Spherical Completeness

**Definition.** A non-Archimedean valued field $K$ is **spherically complete** if every decreasing chain $B_1 \supseteq B_2 \supseteq \cdots$ of closed balls has nonempty intersection.

**Proposition.** Every spherically complete field is complete, and every complete field with discrete value group is spherically complete. The field $\mathbb{Q}_p$ is spherically complete; the field $\mathbb{C}_p$ is complete and its value group is divisible, and it is **not** spherically complete.

**Proof.** Spherical completeness implies completeness: the terms of a Cauchy sequence eventually lie in a chain of balls of arbitrarily small radius, and a point of the intersection is a limit. Suppose the value group of $K$ is discrete and let $B_1 \supseteq B_2 \supseteq \cdots$ be a decreasing chain of closed balls with radii $r_n$ in the value group. If the radii are bounded below by a positive number, then they lie in the set $\{q^{-m} : m \geq 0\}$ intersected with $[r_1,\infty)$, which is finite, so the radii are eventually constant and the chain of sets stabilises, giving a nonempty intersection; if the radii tend to $0$, the centres form a Cauchy sequence, whose limit lies in every ball because the balls are closed and nested. For $\mathbb{C}_p$ the value group is $p^{\mathbb{Q}}$, which is divisible and dense, and the field is not spherically complete: the standard example, due to Krasner, is a nested family of closed balls whose radii decrease to a positive limit that is not the absolute value of any element of $\mathbb{C}_p$, chosen so that no point lies in all of them; the construction is reproduced in the standard references. $\square$

### Ingleton's Theorem

**Theorem (Ingleton).** The Hahn–Banach extension theorem, in the form that a bounded linear functional on a subspace of a normed space extends to the whole space with the same norm, holds for all normed spaces over $K$ if and only if $K$ is spherically complete.

**Proof sketch (the direction that Hahn–Banach fails).** Suppose $K$ is not spherically complete, so there is a decreasing chain of closed balls $B_n$ with empty intersection. One builds a normed space $E$ with a subspace $D$ and a functional on $D$ of norm $1$ that cannot be extended with norm $1$, or even at all, using the chain as an obstruction: the canonical embedding of the union of the subspaces generated by the balls into a suitable quotient is such that every continuous functional must vanish on a ball of positive radius, and the chain forces the functional to vanish identically. The construction is due to Ingleton and is reproduced in the standard references. $\square$

**Proof sketch (the direction that Hahn–Banach holds).** Let $K$ be spherically complete, $D \subseteq E$ a subspace, and $f$ a bounded functional on $D$ of norm $c$. Consider the family of all extensions of $f$ to subspaces of $E$ with the same norm, ordered by extension; by Zorn's lemma it has a maximal element. If the maximal extension $g$ were defined on a proper subspace $M \neq E$, one takes $y \notin M$ and shows that one of the values $g(m) + \lambda$ can be chosen with $\lvert g(m) + \lambda \rvert \leq c\lVert m + y\rVert$ for all $m \in M$: the sets $\{g(m) + \mu : \lvert\mu\rvert \leq c\lVert m+y\rVert \}$ are balls in $K$, and the spherical completeness of $K$ gives a common $\lambda$ in their intersection, extending $g$ to $M + Ky$ and contradicting maximality. $\square$

**Corollary (the bidual).** Let $K$ be spherically complete. Then for every normed space $E$ the canonical map $E \to E''$ is an isometry, and the dual separates points of $E$: $\lVert x \rVert = \sup\{ \lvert f(x) \rvert : f \in E', \lVert f \rVert \leq 1\}$.

**Proof.** The Hahn–Banach theorem applies to the functional on the line $Kx$ given by $\lambda x \mapsto \lambda \lVert x \rVert$ when $x\ne0$, extending it to $E$ with norm $1$, which gives a functional of norm $1$ with $\lvert f(x) \rvert = \lVert x \rVert$. The identification of $E$ with a subspace of $E''$ is the standard one, and it is isometric because the functional above realises the norm. $\square$

**Remark (spaces with trivial dual).** If $K$ is not spherically complete, there exist normed spaces $E \neq 0$ over $K$ with $E' = 0$; the construction uses a nested family of balls with empty intersection, and the example shows that the failure of Hahn–Banach is not confined to pathological subspaces but can destroy the duality of a whole space. Over $\mathbb{C}_p$ such spaces exist, which is the reason that the theory over $\mathbb{C}_p$ is developed with the extra structure of a "polar" or of a Banach space over a spherically complete subfield.

## Linear Operators

### The Open Mapping and Closed Graph Theorems

**Theorem (open mapping).** Let $E,F$ be Banach spaces over $K$ and let $T : E \to F$ be a continuous linear surjection. Then $T$ is open: the image of the unit ball of $E$ contains a ball of positive radius about $0$ in $F$. Consequently $T$ induces a topological isomorphism $E/\ker T \cong F$ of normed spaces; in general that isomorphism is not isometric.

**Proof.** Since $F = \bigcup_n T(nB_E)$ and $F$ is a Baire space, some closure $\overline{T(nB_E)}$ has nonempty interior, and the standard scaling argument gives the existence of $r > 0$ with $B(0,r) \subseteq \overline{T(B_E)}$; by scaling again, $B(0,rt) \subseteq \overline{T(tB_E)}$ for every $t>0$. Let $\lVert y \rVert < r$. Choose $x_1$ with $\lVert x_1 \rVert \leq 1$ and $\lVert y - T(x_1)\rVert < r/2$; the residual lies in $B(0,r/2) \subseteq \overline{T(2^{-1}B_E)}$, so choose $x_2$ with $\lVert x_2\rVert \leq 2^{-1}$ and $\lVert y - T(x_1) - T(x_2)\rVert < r/4$; continuing, one obtains $x_k$ with $\lVert x_k\rVert \leq 2^{-(k-1)}$ and $\lVert y - T(x_1 + \cdots + x_k)\rVert < r/2^k$. The series $\sum_k x_k$ converges because its terms tend to $0$, its sum $x$ satisfies $\lVert x \rVert \leq 1$ by the strong triangle inequality, and $T(x) = y$ by continuity, so $B(0,r) \subseteq T(B_E)$ and $T$ is open. $\square$

**Theorem (closed graph).** Let $E, F$ be Banach spaces and let $T : E \to F$ be linear with closed graph. Then $T$ is continuous.

**Proof.** The graph $G = \{(x,Tx)\} \subseteq E \times F$ is a Banach space and the projection $G \to E$ is a continuous linear bijection; it is open by the open mapping theorem, so its inverse $x \mapsto (x,Tx)$ is continuous, and $T$ is the composition with the continuous second projection. $\square$

**Theorem (uniform boundedness).** Let $E$ be a Banach space, $F$ a normed space and $(T_i)_{i\in I}$ a family of continuous linear maps with $\sup_i \lVert T_i x \rVert < \infty$ for every $x \in E$. Then $\sup_i \lVert T_i \rVert < \infty$.

**Proof sketch.** The sets $A_n = \{x : \sup_i \lVert T_i x \rVert \leq n\}$ are closed with union $E$, and $E$ is a Baire space, so some $A_n$ has nonempty interior; scaling gives the bound on the operator norms. If $E$ is finite-dimensional then the unit sphere is compact and each $\lVert T_i\rVert$ is attained on it, which gives the same conclusion directly. $\square$

**Remark (the failure of local compactness).** The classical criterion has to be adjusted, because compactness of the unit ball requires compactness of the field: the closed unit ball of a normed space over $K$ is compact exactly when the space is finite-dimensional and $K$ is locally compact, and over $\mathbb{C}_p$ even the one-dimensional space $\mathbb{C}_p$ has non-compact unit ball. What fails in infinite dimension is the existence of sufficiently many functionals and of topological complements: over $\mathbb{C}_p$ there is a continuous linear surjection of Banach spaces whose kernel is not complemented, and properties defined by duality, such as reflexivity, need not hold. The Banach space $c_0$ is not reflexive over a spherically complete field: the limit functional on the subspace of convergent families of $c_0' = \ell^\infty$ extends by Hahn–Banach to a functional that is not evaluation at any element of $c_0$, so the canonical map $c_0 \to c_0''$ is not surjective.

## Compactoid Sets and Duality

### Compactoidness

**Definition.** A subset $X$ of a normed space $E$ is **compactoid** if for every neighbourhood $U$ of $0$ in $E$ there is a finite set $F \subseteq E$ with $X \subseteq U + \mathrm{ac}(F)$, where $\mathrm{ac}(F)$ is the set of finite linear combinations $\sum \lambda_i x_i$ with $\lvert \lambda_i \rvert \leq 1$. Equivalently, $X$ is compactoid when it can be approximated in every neighbourhood of $0$ by sets lying in a finite-dimensional subspace of controlled norm.

**Proposition.** Every compactoid set is bounded; every subset of a compactoid set is compactoid; the closure and the absolutely convex hull of a compactoid set are compactoid; a compact set is compactoid; and the union of two compactoid sets is compactoid.

**Proof.** The kernel of the definition is the finite-dimensional approximation: a set contained in $\mathrm{ac}(F)$ is bounded by $\max_{x\in F}\lVert x\rVert$ and the same bound holds after adding a small perturbation. Closure under subsets and under closure follow from the definition applied to a basic sequence of neighbourhoods. A compact set is compactoid because it is covered by finitely many translates of any neighbourhood. $\square$

**Theorem.** Let $K$ be spherically complete and let $E$ be a normed space over $K$. Then a bounded set $X \subseteq E$ is compactoid if and only if it is contained in the closed absolutely convex hull of a null sequence; in particular

**(a)** the closed unit ball of $c_0(I)$ is compactoid, and for $I$ infinite it is not compact;

**(b)** a linear map $T : E \to F$ between normed spaces is compact, in the sense that it maps bounded sets to compactoid sets, if and only if it is the norm limit of a sequence of finite-rank operators.

**Proof sketch.** (a) For the unit ball of $c_0(I)$ and $\epsilon > 0$, the family $\{i : \lvert a_i \rvert \geq \epsilon\}$ is finite for each $a$ in the ball, so the ball is covered by the sets of elements that are $\epsilon$-small outside a finite set depending on the element; a compactness argument with the finite sets turns this into a cover of the ball by finitely many translates of the $\epsilon$-ball inside a coordinate subspace. Compactness fails because the unit vectors are pairwise at distance $1$. (b) A finite-rank operator maps bounded sets into finite-dimensional sets, which are compactoid, and a norm limit of compactoid-valued operators stays compactoid-valued because the approximation is uniform; conversely the compactoidness gives the approximating finite-dimensional subspaces, and choosing a bounded net in each gives finite-rank operators converging in norm. $\square$

### The Polar and the Bipolar Theorem

**Definition.** For a subset $A$ of a normed space $E$ the **polar** is
$$
A^\circ = \{ f \in E' : \lvert f(x) \rvert \leq 1 \text{ for all } x \in A \},
$$
and for a subset $B \subseteq E'$ the polar in $E$ is $B_\circ = \{x \in E : \lvert f(x) \rvert \leq 1 \text{ for all } f \in B\}$. The **absolutely convex hull** of $A$ is the set of finite sums $\sum \lambda_i x_i$ with $x_i \in A$, $\lvert \lambda_i \rvert \leq 1$.

**Theorem (bipolar theorem; Schikhof).** Let $K$ be spherically complete, let $E$ be a normed space over $K$ and let $A \subseteq E$. Then the bipolar $(A^\circ)_\circ$ is the closure in $E$ of the absolutely convex hull of $A$, and the correspondence $A \mapsto A^\circ$ reverses inclusions and exchanges compactoid sets with neighbourhoods of $0$ in $E'$ equipped with the topology of uniform convergence on compactoid sets.

**Proof sketch.** Over a spherically complete field the Hahn–Banach theorem is available and separates a point from a closed absolutely convex set not containing it, which is the content of the theorem; the identification of compactoidness with the property of being "polar of a neighbourhood" is then a formal consequence of the definitions and of the density of the finite-dimensional approximations. The details are in the standard reference. $\square$

**Corollary (the duality of the Tate algebra).** Let $K$ be a complete non-Archimedean field and let $T_n = K\langle\xi_1,\dots,\xi_n\rangle$ be the Tate algebra of *Rigid Analytic Functions* with its Gauss norm, so that $T_n$ is isometric to $c_0(\mathbb{N}^n)$. Then the dual of $T_n$ is isometrically $\ell^\infty(\mathbb{N}^n)$, the space of bounded families of coefficients; the pairing is $(f, \lambda) \mapsto \sum_\nu a_\nu \lambda_\nu$ for $f = \sum_\nu a_\nu\xi^\nu$, and the unit ball of the dual is the space of $p$-adic distributions of *p-adic Integration*, with the Amice transform identifying a distribution with the power series $\sum_\nu \lambda_\nu T^\nu$ of bounded coefficients and a measure with an element of $\mathbb{Z}_p[[T]]$ in the case $K = \mathbb{Q}_p$.

**Proof.** This is the duality $c_0(I)' = \ell^\infty(I)$ of the previous section applied to the orthonormal basis of monomials, together with the identification of the distributions and the Amice transform established in *p-adic Integration*. $\square$

## Summary

A normed space over a non-Archimedean field is a vector space with a norm satisfying the strong triangle inequality; its balls are clopen and nested or disjoint, every point of a ball is a centre, a series converges if and only if its terms tend to $0$, and the space is locally compact exactly when it is finite-dimensional over a locally compact field; over a field that is not locally compact no nonzero normed space is locally compact, and the unit ball is compact only when the space is finite-dimensional and the field is locally compact. The standard Banach spaces are $c_0(I)$ and $\ell^\infty(I)$, and the dual of the former is the latter, isometrically; the Tate algebra with its Gauss norm is an example, isometric as a Banach space to $c_0(\mathbb{N}^n)$. A family is orthogonal when the norm of every finite linear combination $\sum a_ie_i$ is $\max_i \lvert a_i\rvert \lVert e_i\rVert$, and the normed spaces with an orthogonal basis are exactly the isometric copies of the spaces $c_0(I)$; over a spherically complete field every finite-dimensional subspace has an orthogonal basis and a projection of norm $1$ onto it.

Duality is governed by spherical completeness. The Hahn–Banach theorem holds for all normed spaces over $K$ exactly when every decreasing chain of closed balls has nonempty intersection, by Ingleton's theorem; $\mathbb{Q}_p$ is spherically complete and $\mathbb{C}_p$ is not, and over a field that is not spherically complete there are nonzero normed spaces with trivial dual. Over a spherically complete field the canonical map to the bidual is an isometry and the dual separates points. The open mapping theorem, the closed graph theorem and the uniform boundedness principle hold for Banach spaces over any complete non-Archimedean field, with the classical proofs, because completeness still makes the space a Baire space; what fails is everything that depends on an inner product or on the compactness of the unit ball. Compactness is replaced by compactoidness, the property of being approximable in every neighbourhood of $0$ by a finite-dimensional set; the unit ball of $c_0$ is compactoid but not compact, a compact operator is a norm limit of finite-rank operators, and over a spherically complete field the bipolar theorem identifies the bipolar of a set with the closure of its absolutely convex hull, giving the duality between the Tate algebra and the space of power series as the analytic Amice transform.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $K$ | Complete non-Archimedean field, absolute value $\lvert\cdot\rvert$ |
| $K^\circ$, $k$ | Valuation ring, residue field |
| $E$, $F$ | Normed spaces over $K$ |
| $\lVert x \rVert$ | Norm, with $\lVert x+y\rVert \leq \max$ |
| $B_E$, $S_E$ | Unit ball and unit sphere of $E$ |
| $B(a,r)$ | Closed ball of centre $a$ and radius $r$ |
| $c_0(I)$, $\ell^\infty(I)$ | Null families, bounded families, with the sup norm |
| $e_i$ | Canonical unit vector of $c_0(I)$ |
| $E'$ | Continuous dual, with the operator norm |
| Orthogonal, orthonormal | $\lVert\sum a_ie_i\rVert = \max\lvert a_i\rvert\lVert e_i\rVert$; and $\lVert e_i\rVert=1$ |
| Orthogonal basis | Orthogonal family with dense span |
| Spherically complete | Every decreasing chain of closed balls has nonempty intersection |
| $E''$ | Bidual, with the canonical isometry $E \to E''$ |
| $\mathrm{ac}(F)$ | Absolutely convex hull of $F$ |
| Compactoid | Approximable by $\mathrm{ac}(F)$ in every neighbourhood of $0$ |
| $A^\circ$, $B_\circ$ | Polar of $A \subseteq E$ in $E'$, polar of $B \subseteq E'$ in $E$ |
| $T_n = K\langle\xi_1,\dots,\xi_n\rangle$ | Tate algebra, isometric to $c_0(\mathbb{N}^n)$ |
| $\mathbb{Q}_p$, $\mathbb{C}_p$ | Spherically complete; complete but not spherically complete |



## Further Reading

- A. C. M. van Rooij, *Non-Archimedean Functional Analysis* (Marcel Dekker, 1978), for the systematic theory of normed spaces, orthogonal bases and spherical completeness.
- Wim H. Schikhof, *Locally convex spaces over non-Archimedean valued fields* (in: $p$-adic Functional Analysis, Lecture Notes in Mathematics 1454, Springer, 1990), for compactoidness, the polar theory and the bipolar theorem.
- A. W. Ingleton, *The Hahn–Banach theorem for non-Archimedean valued fields* (Proceedings of the Cambridge Philosophical Society 48, 1952), for the theorem that Hahn–Banach holds exactly over spherically complete fields.
- Lawrence Narici and Edward Beckenstein, *Topological Vector Spaces* (2nd ed., CRC Press, 2011), for the general theory of non-Archimedean topological vector spaces.
- N. De Grande-De Kimpe and others, *$p$-adic Functional Analysis* (Lecture Notes in Pure and Applied Mathematics, Marcel Dekker, 1992), for the conferences and surveys of the compactoid theory.
- Christine Perez-Garcia and Wilhelmus H. Schikhof, *Locally Convex Spaces over Non-Archimedean Valued Fields* (Cambridge University Press, 2010), for the modern account of duality and compactoidness.
- Peter Schneider, *Nonarchimedean Functional Analysis* (Springer, 2002), for the Banach spaces arising in rigid analytic geometry and the duality with power series.
- Kiran S. Kedlaya, *$p$-adic Differential Equations* (Cambridge University Press, 2010), for the function-space examples used in the analytic theory.
