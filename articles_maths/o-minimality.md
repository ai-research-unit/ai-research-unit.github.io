
# __O-Minimality__

## Introduction

This is the fifth article of the Real Numbers system in Part V, and it occupies the **geometry slot** of that system, read for the definable rather than the metric structure of the line. The system is the ordered field $\mathbb{R}$ of *The Real Numbers*, and the object of study is the *tameness* of its definable sets: the property that every subset of the line definable by a first-order formula with parameters is a finite union of intervals and points, and the structure theory of definable sets in all dimensions that this property forces.

This article is the one article of the load that is model-theoretic rather than synthetic, and its position is deliberate: o-minimality is not a construction on $\mathbb{R}$ but a property of the line's definable sets, and it is a property of the real line in the same way that the intermediate value property or the cell decomposition of a semialgebraic set is. It is placed here because it is the geometric form of the completeness and order of $\mathbb{R}$: the definable sets of the line are the sets that the geometry of the line can describe, and o-minimality says that they cannot be wild. The general model theory — languages, structures, satisfaction, quantifier elimination, compactness, types and elementary extensions — is the subject of Part I's *Model Theory*, which is being written in parallel and is used here rather than developed; the model theory of the natural numbers, with its wild definability and its undecidability, is the subject of *Peano Arithmetic and Model Theory* and forms the contrast to everything below. The real algebraic geometry of the semialgebraic sets is from *Real Algebraic Geometry*, and the ordered field theory of $\mathbb{R}$ from *Real-Closed and Complete Ordered Fields*.

Throughout, $\mathcal{L}$ is a first-order language containing a binary relation symbol $<$, an $\mathcal{L}$-**structure** $\mathcal{M}$ is o-minimal if $<$ is interpreted as a dense linear order without endpoints on its domain $M$ and every subset of $M$ definable with parameters is a finite union of intervals and points; $\mathbb{R}$ denotes the real line as an $\mathcal{L}$-structure, $\mathrm{RCF}$ the theory of real closed fields in the language of ordered rings, $\mathbb{R}_{\exp}$ the real exponential field $(\mathbb{R}, +, \cdot, <, \exp)$ and $\mathbb{R}_{\mathrm{an}}$ the real field with restricted analytic functions. Definable sets are written as $\varphi(M, \bar a) = \{x \in M^n : \mathcal{M} \models \varphi(x, \bar a)\}$, and a **cell** is a definable set of a particular recursive form introduced below.

## Definable Sets

### Languages and Structures

**Definition.** Let $\mathcal{L}$ be a first-order language and $\mathcal{M}$ an $\mathcal{L}$-structure with domain $M$. A set $A \subseteq M^n$ is **definable** (in $\mathcal{M}$, with parameters) if there is a formula $\varphi(x_1, \dots, x_n, \bar y)$ of $\mathcal{L}$ and a tuple $\bar a \in M^m$ with

$$
A = \{\bar x \in M^n : \mathcal{M} \models \varphi(\bar x, \bar a)\}.
$$

A set definable without parameters is **0-definable**. A function is definable if its graph is.

**Theorem.** The definable sets are closed under finite unions, finite intersections, complements in $M^n$, Cartesian products, coordinate permutations, and images and preimages under definable functions. In particular the projection $\pi : M^{n+1} \to M^n$ of a definable set is definable.

**Proof.** The Boolean combinations are the logical connectives, the products and permutations are the renamings of variables, and the projection is the existential quantifier; the closure under images follows from the closure under projections and graphs. $\square$

**Definition.** A theory $T$ has **quantifier elimination** if every formula is equivalent, modulo $T$, to a quantifier-free formula; equivalently, every definable set is a finite Boolean combination of sets defined by atomic formulas.

**Theorem (Tarski–Seidenberg).** The theory $\mathrm{RCF}$ of real closed fields has quantifier elimination in the language of ordered rings. Consequently a subset of $\mathbb{R}^n$ is definable in $(\mathbb{R}, +, \cdot, <)$ if and only if it is **semialgebraic**, that is, a finite Boolean combination of sets $\{x : f(x) \geq 0\}$ with $f \in \mathbb{R}[x_1,\dots,x_n]$.

**Proof.** Quantifier elimination for real closed fields is Tarski's theorem, and the identification of the quantifier-free definable sets with the semialgebraic sets is immediate from the form of the atomic formulas. The elimination is proved by an algebraic argument reducing the one-variable case to the sign of a polynomial on a finite set of roots; it is given in *Model Theory* and *Real Algebraic Geometry*. $\square$

**Corollary.** The theory $\mathrm{RCF}$ is complete and decidable: there is an algorithm deciding, for a sentence in the language of ordered rings, whether it holds in $\mathbb{R}$.

### Definable Subsets of the Line

**Theorem (dense linear orders).** Let $\mathcal{M} = (M, <)$ be a dense linear order without endpoints. Then every definable subset of $M$ is a finite union of intervals and points.

**Proof.** The theory of dense linear orders without endpoints has quantifier elimination: a quantifier-free formula in one free variable is a Boolean combination of atoms $x = a$ and $a < x < b$, hence defines a finite union of points and intervals. $\square$

**Theorem.** Let $\mathcal{M} = (M, +, <)$ be a nontrivial **divisible** ordered abelian group, that is, an ordered $\mathbb{Q}$-vector space. Then every definable subset of $M$ is a finite union of intervals and points.

**Proof.** The theory of divisible ordered abelian groups admits quantifier elimination in the language of ordered groups. A quantifier-free formula in one free variable with parameters is therefore a Boolean combination of atoms $x < a$ and $a < x$, and such a Boolean combination defines a finite union of points and intervals. The argument is in *Model Theory*. $\square$

**Theorem (sharpness).** Divisibility cannot be dropped for ordered abelian groups. An ordered abelian group with a dense order is o-minimal if and only if it is divisible.

**Proof.** Divisibility means that $M$ is an ordered $\mathbb{Q}$-vector space, and the preceding theorem gives o-minimality. For the converse, let $M$ be a dense ordered abelian group that is not divisible and put

$$
2M = \{x \in M : \text{there is } y \in M \text{ with } y + y = x\}.
$$

The set $2M$ is a proper definable subgroup, proper because divisibility is exactly the condition $2M = M$. It cannot be a finite union of intervals and points: it is infinite, so such a decomposition would contain a nondegenerate interval $(a,b)$, and then $2M$, being a subgroup, would contain the difference interval $(a - b, b - a)$, the negatives of its elements, and all finite sums of these, hence an interval symmetric about $0$ and all of its finite sums. In the lexicographic group $M = \mathbb{Z} \times \mathbb{Q}$ this is explicit and immediately contradictory, as the example below records. The general statement is standard and is in the references. $\square$

**Example.** In the lexicographic group $M = \mathbb{Z} \times \mathbb{Q}$ the subgroup $2M$ is $2\mathbb{Z} \times \mathbb{Q}$, which contains $(1,0)$'s predecessor block but not $(1,0)$ itself. Explicitly, $2M$ contains the interval $[0,(1,0)) = \{(0,q) : q \geq 0\}$; being a subgroup it also contains $(-(1,0), 0]$ and therefore, by taking sums of the two, the interval $(-(2,0), (2,0))$, and that interval contains $(1,0)$, which is not in $2M$. So $2M$ is not a finite union of intervals and points and $M$ is not o-minimal.

**Remark.** The theorem is the reason the divisible case is the one that carries the theory: the ordered $\mathbb{Q}$-vector space is the divisible case, and a divisible ordered abelian group is o-minimal while a non-divisible one already fails on the single definable set $2M$.

**Remark.** In each of these examples the definable subsets of the line are determined by quantifier elimination in one variable, and that is the simplest route to o-minimality. The theorem below, that the real field is o-minimal, cannot be obtained that way in general, because quantifier elimination in the language of ordered rings does not by itself bound the number of intervals uniformly; what is needed is a theorem about the *number* of connected components, and that is supplied by the cell decomposition.

## O-Minimal Structures

### The Definition

**Definition.** An $\mathcal{L}$-structure $\mathcal{M}$ is **o-minimal** if the language contains a binary relation symbol $<$ whose interpretation is a dense linear order without endpoints on $M$, and every subset of $M$ definable with parameters is a finite union of intervals and points.

The definition is a condition on the definable subsets of the domain only; the content of the theory is that this one-dimensional condition forces a strong structure on the definable subsets of all $M^n$.

**Theorem (equivalent formulations).** For an expansion $\mathcal{M}$ of a dense linear order, the following are equivalent:

**(i)** $\mathcal{M}$ is o-minimal;

**(ii)** every definable subset of $M$ has finitely many definable connected components;

**(iii)** there is no definable subset of $M$ that is infinite and discrete;

**(iv)** every definable function $f : M \to M$ is piecewise constant or strictly monotone.

**Proof.** The equivalence of (i), (ii) and (iii) is immediate from the fact that a finite union of intervals and points has finitely many components and no infinite discrete definable subset, while an infinite definable set with a least element above each of its points contains a discrete definable subset. The equivalence with (iv) is the one-dimensional case of the monotonicity theorem below. $\square$

**Theorem (elementary equivalence).** If $\mathcal{M}$ is o-minimal then every structure elementarily equivalent to $\mathcal{M}$ is o-minimal; o-minimality is therefore a property of the complete theory, not of a single structure. It passes to reducts, and to expansions that do not change the definable subsets of the line.

**Proof.** The condition that every definable subset of the line is a finite union of intervals and points is a schema of first-order sentences, one for each formula, and is thus preserved under elementary equivalence. $\square$

### Examples and Non-Examples

**Theorem.** The following structures are o-minimal:

**(a)** $(\mathbb{R}, <)$, and more generally any dense linear order without endpoints;

**(b)** $(\mathbb{R}, +, <)$ and the ordered vector spaces over an ordered field;

**(c)** $(\mathbb{R}, +, \cdot, <)$, the real field, and every real closed field;

**(d)** $\mathbb{R}_{\exp} = (\mathbb{R}, +, \cdot, <, \exp)$, the real exponential field (Wilkie);

**(e)** $\mathbb{R}_{\mathrm{an}} = (\mathbb{R}, +, \cdot, <, f)$ with the restricted analytic functions $f$ (Denef–van den Dries, after Gabrielov).

**Proof.** Case (a) is the quantifier elimination for dense linear orders; (b) is the quantifier elimination for ordered abelian groups in the divisible case; (c) is Tarski–Seidenberg together with the cell decomposition below; (d) is Wilkie's theorem of 1996, proved by a model-theoretic analysis of the real exponential field; (e) is the analytic cell decomposition obtained by Gabrielov's theorem on the complements of subanalytic sets. The statements (c)–(e) are quoted from the literature. $\square$

**Theorem.** The following structures are **not** o-minimal:

**(a)** $(\mathbb{Z}, +, \cdot, <)$, and $(\mathbb{N}, +, \cdot, <)$, since the order is not dense and the definable sets include the infinite discrete subsets;

**(b)** $(\mathbb{R}, +, \cdot, <, \sin)$, since $\mathbb{Z} = \{x : \sin(\pi x) = 0\}$ is definable and infinite discrete;

**(c)** any expansion of the real field in which an infinite discrete set is 0-definable, such as $(\mathbb{R}, +, \cdot, <, \mathbb{Z})$ with a predicate for the integers, since $\mathbb{Z}$ itself is then definable, infinite and discrete.

**Proof.** In each case an infinite discrete subset of the line is definable with parameters, and o-minimality forbids this by condition (iii) above. In (b), $\pi$ is a parameter and $\sin(\pi x) = 0$ defines exactly $\mathbb{Z}$; in (c) the offending set is part of the language. $\square$

**Remark.** The contrast between (b) and (c) on the one hand and the o-minimality of $\mathbb{R}_{\exp}$ on the other is the central phenomenon: the exponential function is tame because it is a function from the line to the line with no zeroes and no oscillations, while the sine function and the integers are wild because they produce an infinite discrete definable set. The same contrast is the model-theoretic form of the difference between the algebraic and the analytic functions in the theory of the real line.

## Cell Decomposition

### Cells

**Definition.** The **cells** of $M^n$ are defined by recursion on $n$. A cell of $M^1$ is a point or an interval. A cell of $M^{n+1}$ is a set of one of the forms

$$
\{(\bar x, y) : \bar x \in C,\ f(\bar x) < y < g(\bar x)\}, \qquad \{(\bar x, y) : \bar x \in C,\ y = f(\bar x)\},
$$

where $C \subseteq M^n$ is a cell and $f, g : C \to M$ are definable continuous functions with $f < g$ pointwise, allowing either endpoint to be omitted so that the condition is one-sided or two-sided. The **dimension** of a cell is $n$ minus the number of coordinates that are constrained to equal a definable function of the others, so a cell of $M^n$ has dimension $k \leq n$.

**Theorem (cell decomposition).** Let $\mathcal{M}$ be o-minimal and let $A_1, \dots, A_k \subseteq M^n$ be definable. Then there is a decomposition of $M^n$ into finitely many cells, each contained in one of the $A_i$ or in its complement, and refining any given finite decomposition. Moreover, if $f : A \to M$ is definable with $A \subseteq M^n$ definable, the decomposition can be chosen so that $f$ is continuous on each cell contained in $A$.

**Proof.** The proof is an induction on $n$ using the one-dimensional definition: in $M^1$ the definable sets are finite unions of intervals and points, which is already a cell decomposition. For the induction step one uses the **uniform finiteness** of the fibres, itself a consequence of o-minimality, to ensure that the number of intervals in a fibre is bounded by an integer depending only on the formula, and then one applies the one-dimensional case to the finitely many boundary functions. The full induction is the standard proof. $\square$

**Corollary.** Every definable subset of $M^n$ has finitely many definably connected components, each of them definable, and every definable subset of $M^n$ is a finite disjoint union of cells. A definable set is finite if and only if it has dimension $0$.

**Proof.** The first statement is the cell decomposition applied to the set and its boundary, using that a cell is definably connected and that the cells of a decomposition are disjoint; the second is immediate from the definition of dimension. $\square$

**Theorem (definable choice).** If $A \subseteq M^{n+1}$ is definable, then there is a definable function $f : \pi(A) \to M$ with $(\bar x, f(\bar x)) \in A$ for all $\bar x \in \pi(A)$, where $\pi$ is the projection to the first $n$ coordinates.

**Proof.** The cell decomposition of $A$ exhibits $A$ as a finite union of cells over the cells of a decomposition of $\pi(A)$, and on each part one chooses the least (or the first) element of the fibre; the resulting function is definable because the choice is made by a definable formula. $\square$

## Definable Functions and Dimension

### The Monotonicity Theorem

**Theorem (monotonicity).** Let $\mathcal{M}$ be o-minimal and let $f : (a,b) \to M$ be definable. Then there are $a = a_0 < a_1 < \cdots < a_k = b$ such that on each open interval $(a_i, a_{i+1})$ the function $f$ is continuous and either constant or strictly monotone.

**Proof.** The set of points at which $f$ fails to be locally constant or locally strictly monotone is definable, and by o-minimality it is a finite union of points and intervals; one shows that it cannot contain an interval, for otherwise a definable order-isomorphism argument would produce an infinite discrete definable set. Removing the finitely many offending points gives the required partition. This is the monotonicity theorem of the theory; the details are in the references. $\square$

**Corollary.** Let $\mathcal{M}$ be an o-minimal expansion of an ordered field and let $f : (a,b) \to M$ be definable. Then $f$ is piecewise continuous and on each piece either constant or strictly monotone, and its one-sided limits exist at every point of $(a,b)$. The set of points at which $f$ is differentiable is definable, and the derivative is a definable function wherever it exists.

**Proof.** The partition, the monotonicity and the one-sided limits are the monotonicity theorem. For a definable $f$ the difference quotients are definable functions of two variables, and the set of pairs $(x,y)$ for which the quotient tends to $y$ as the increment tends to $0$ is definable and meets each vertical line in at most one point; by definable choice it is the graph of a definable function, which is the derivative of $f$. $\square$

**Example.** For the real field $\mathcal{M} = (\mathbb{R}, +, \cdot, <)$ the definable functions are the semialgebraic ones, and these are piecewise Nash: the pieces of the monotonicity partition can be refined to semialgebraic cells on which the function is analytic, so that in this structure the conclusion strengthens to piecewise $C^k$ for every $k$. The same strengthening holds for the restricted analytic structure $\mathbb{R}_{\mathrm{an}}$, whose definable functions are piecewise analytic by construction, and for the exponential field $\mathbb{R}_{\exp}$. Such strengthenings are proved structure by structure; the regularity that o-minimality supplies on its own is the monotonicity and definability statement above.

### Dimension

**Definition.** For a definable set $A \subseteq M^n$ the **dimension** $\dim A$ is the largest $d$ such that $A$ contains a cell of dimension $d$, or $-\infty$ for the empty set; equivalently, the largest $d$ such that some projection of $A$ onto $d$ coordinates has nonempty interior.

**Theorem.** The dimension is the unique function from definable sets to $\{-\infty, 0, 1, 2, \dots\}$ satisfying

$$
\dim A = 0 \iff A \text{ finite}, \qquad \dim(A \cup B) = \max(\dim A, \dim B), \qquad \dim(A \times B) = \dim A + \dim B,
$$

and for every definable function $f : A \to M^n$, $\dim f(A) \leq \dim A$, with equality holding if $f$ is injective.

**Proof.** The first three properties follow from the cell decomposition, using that the dimension of a cell is additive under products and maximal under unions. The behaviour under definable functions is checked on cells: a definable continuous function on a cell cannot increase the number of free coordinates, and an injective function cannot decrease it. $\square$

**Theorem (exchange and the matroid axioms).** Let $\mathrm{dcl}$ be the definable closure in an o-minimal structure. Then $\mathrm{dcl}$ satisfies the **exchange property**: if $b \in \mathrm{dcl}(A \cup \{a\}) \setminus \mathrm{dcl}(A)$, then $a \in \mathrm{dcl}(A \cup \{b\})$. Consequently the dimension is the rank function of a matroid, and for a definable set $A \subseteq M^n$ the dimension equals the maximum, over the tuples $\bar a \in A$, of the dcl-rank of the set of coordinates of $\bar a$ in the matroid induced by $\mathrm{dcl}$.

**Proof.** The exchange property is proved from the monotonicity theorem and the cell decomposition: a definable function establishing $b \in \mathrm{dcl}(A \cup \{a\})$ can be inverted off a finite set. The matroid axioms and the identification of the dimension with the rank then follow from the general theory of matroids and the dimension properties above. The argument is in the references. $\square$

**Corollary (uniform finiteness).** For a definable family $\{A_{\bar x} : \bar x \in B\}$ of subsets of $M$, there is an integer $N$ such that every set in the family has at most $N$ definably connected components; more generally, the dimension of the fibres is uniformly bounded and attained on a definable subset of the parameter space.

**Proof.** If the number of components of the fibres were unbounded, the cell decomposition applied to the family would produce a formula defining an infinite discrete subset of $M$, contradicting o-minimality; so the number is uniformly bounded. The same argument bounds the fibre dimensions, which by the cell decomposition take finitely many values. $\square$

**Theorem (Pillay).** Every group definable in an o-minimal structure is, definably, a Lie group: there is a definable manifold structure on the group making the group operations definable and the group locally Euclidean, and the group is definably isomorphic to a definable subgroup of a linear group.

**Proof.** The definable manifold structure is obtained from a cell decomposition adapted to the group operation, using definable choice to build the charts; the linear representation is obtained from the adjoint action on the Lie algebra of the definable group. The theorem is Pillay's and is quoted from the literature. $\square$

## O-Minimality and Real Algebraic Geometry

### Tarski–Seidenberg and the Real Field

**Theorem.** The real field $(\mathbb{R}, +, \cdot, <)$ is o-minimal, and a subset of $\mathbb{R}^n$ is definable in it if and only if it is semialgebraic. The definable sets are exactly the finite unions of cells of the semialgebraic cell decomposition.

**Proof.** By Tarski–Seidenberg the definable sets are the semialgebraic sets, and the one-variable statement follows because a semialgebraic subset of $\mathbb{R}$ is a finite union of points and intervals. The cell decomposition then follows from the algebraic arguments of *Real Algebraic Geometry*. $\square$

**Corollary (projection).** If $A \subseteq \mathbb{R}^{n+1}$ is semialgebraic then its projection to $\mathbb{R}^n$ is semialgebraic; this is the Tarski–Seidenberg projection theorem, and it is the algebraic form of the statement that the real field has quantifier elimination.

**Theorem (o-minimality of the exponential field; Wilkie).** $\mathbb{R}_{\exp} = (\mathbb{R}, +, \cdot, <, \exp)$ is o-minimal. Consequently every set definable with the exponential function is a finite union of cells, every definable function is piecewise monotone and piecewise $C^k$, and the definable sets are tame.

**Proof.** Wilkie's theorem, proved by a model-theoretic analysis of the real exponential field and the theory of the exponential function near the origin; it is quoted. $\square$

**Theorem (analytic case).** $\mathbb{R}_{\mathrm{an}} = (\mathbb{R}, +, \cdot, <, f_1, \dots, f_m)$ with the restricted analytic functions is o-minimal, and the subanalytic sets are the definable sets.

**Proof.** The result is Denef–van den Dries, using Gabrielov's theorem that the complement of a subanalytic set is subanalytic; it is quoted. $\square$

### Counting Rational Points: The Pila–Wilkie Theorem

**Theorem (Pila–Wilkie).** Let $A \subseteq \mathbb{R}^n$ be definable in an o-minimal structure and suppose that $A$ contains no infinite semialgebraic subset. Then for every $\varepsilon > 0$ there is $c$ such that the number of rational points of height at most $H$ in $A$ is at most $c H^{\varepsilon}$, where the height of $p/q$ is $\max(\lvert p\rvert, q)$.

**Proof.** The theorem is Pila and Wilkie's, proved by a counting of the intersections of $A$ with the algebraic curves of bounded degree and a reduction to the o-minimal dimension theory; it is quoted from the literature. $\square$

**Remark.** The Pila–Wilkie theorem is the o-minimal counterpart of the Diophantine approximation of *Diophantine Approximation and Continued Fractions*: the tame geometry of the real line bounds the rational points on a definable set in the same way that the continued fractions bound the rational approximations to a real number. The theorem has become the engine of the Pila–Zannier proof of the Manin–Mumford conjecture and of the Pila proofs of the André–Oort conjecture for the modular curves, and it shows that o-minimality is not a technical curiosity but the geometric structure underlying a range of arithmetic results.

### The Contrast with the Natural Numbers

**Remark.** The model theory of the real line is the exact counterpart of the model theory of the naturals. In $(\mathbb{N}, +, \cdot, <)$ the definable sets are the arithmetical sets, stratified by the arithmetical hierarchy; the theory is undecidable, non-standard models abound, and the definable subsets of $\mathbb{N}$ are as wild as the arithmetic permits; this is the content of *Peano Arithmetic and Model Theory*. In $(\mathbb{R}, +, \cdot, <)$, by contrast, the definable sets are the semialgebraic sets, the theory is complete and decidable, and the definable sets have finite cell decompositions and a dimension theory; and even after the addition of the exponential and of the restricted analytic functions the tame behaviour persists. O-minimality is the name for this tameness, and it is the form in which the completeness and order of $\mathbb{R}$ appear in logic: the line is so rigid that its definable sets cannot realise the combinatorial complexity that the discrete structures support.

## Summary

A set is definable in a structure if it is the set of solutions of a first-order formula with parameters, and a structure expanding a dense linear order is o-minimal if every definable subset of its domain is a finite union of intervals and points; equivalently, every definable subset of the line has finitely many connected components, there is no infinite discrete definable subset, and every definable unary function is piecewise constant or strictly monotone. O-minimality is preserved under elementary equivalence, so it is a property of a complete theory, and the real field, the real exponential field, the real field with restricted analytic functions and the ordered vector spaces are o-minimal, whereas the integers, the field of reals with the sine function, and any expansion by an infinite discrete set are not.

The structure theory of o-minimal structures rests on the cell decomposition: every definable subset of $M^n$ is a finite disjoint union of cells, the decomposition can be made compatible with any finite family of definable sets and any definable function, and it yields definable choice, the finiteness of the connected components and a dimension function on definable sets. The dimension is additive under products, maximal under unions, non-increasing under definable images, and the definable closure satisfies the exchange property, so that the dimension is the rank of a matroid and the fibre dimensions in a definable family are uniformly bounded. Definable unary functions are piecewise monotone, and in o-minimal expansions of fields they are piecewise $C^k$; definable groups are definably Lie groups by Pillay's theorem. In the real field the definable sets are exactly the semialgebraic sets, by Tarski–Seidenberg, and the cell decomposition is the semialgebraic one of *Real Algebraic Geometry*; Wilkie's theorem extends o-minimality to the exponential field and the Denef–van den Dries theorem to the restricted analytic functions, and the Pila–Wilkie theorem converts o-minimality into a bound on the number of rational points on a definable set. The geometry slot of the system $\mathbb{R}$ is thus completed by the statement that the definable sets of the line are tame, and o-minimality is the precise sense in which the completeness and order of $\mathbb{R}$ prevent its geometry from realising the wildness of the discrete systems.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{L}$ | A first-order language, containing $<$ |
| $\mathcal{M}$, $M$ | A structure and its domain |
| $\varphi(M, \bar a)$ | Definable set of a formula with parameters |
| $\mathrm{dcl}$ | Definable closure |
| $\mathrm{RCF}$ | Theory of real closed fields |
| $\mathbb{R}$ | The real field $(\mathbb{R}, +, \cdot, <)$ |
| $\mathbb{R}_{\exp}$ | Real exponential field $(\mathbb{R}, +, \cdot, <, \exp)$ |
| $\mathbb{R}_{\mathrm{an}}$ | Real field with restricted analytic functions |
| Cell | Definable set of the recursive interval or graph form |
| $\dim A$ | Dimension of a definable set, cell dimension |
| $\pi$ | Coordinate projection |
| $H$ | Height of a rational point, $\max(\lvert p\rvert, q)$ |

## Further Reading

- Lou van den Dries, *Tame Topology and O-Minimal Structures* (Cambridge University Press, 1998), for the definition of o-minimality, the cell decomposition and the dimension theory.
- David Marker, *Model Theory: An Introduction* (Springer, 2002), for the general model theory, quantifier elimination and the model theory of real closed fields used here.
- Alfred Tarski, *A Decision Method for Elementary Algebra and Geometry* (University of California Press, 2nd ed. 1951), for the quantifier elimination and decidability of the real field.
- Alex Wilkie, "Model completeness results for expansions of the ordered field of real numbers by restricted Pfaffian functions and the exponential function", *Journal of the American Mathematical Society* 9 (1996), for the o-minimality of the real exponential field.
- Lou van den Dries and Chris Miller, "Geometric categories and o-minimal structures", *Duke Mathematical Journal* 84 (1996), for the geometric consequences of o-minimality and the cell decomposition.
- Jonathan Pila and Alex Wilkie, "The rational points of a definable set", *Duke Mathematical Journal* 133 (2006), for the counting theorem and its arithmetic applications.
- Anand Pillay, "On groups and fields definable in o-minimal structures", *Journal of Pure and Applied Algebra* 53 (1988), for the definable group theorem.
