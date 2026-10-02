
# __Ordered Vector Spaces and the Order Unit__

## Introduction

An **ordered vector space** is a real vector space with a distinguished cone of *positive* elements; the order compares two vectors by the membership of their difference in that cone. The order is not a distance and not a topology: it is an **algebraic** structure placed on the linear space, defined by linear operations alone, and it is the structure that the whole of this category develops. Two extra inputs make an ordered vector space into an instrument of analysis. An **order unit** is a positive element so large that the order intervals it defines absorb the space; it turns the order into a norm, the **order-unit norm**, and its unit ball is the order interval $[-u,u]$. The norm in turn defines the **order topology**, the topology in which the cone is closed and the order is continuous.

This article fixes the vocabulary of the category: the positive cone and the order it generates, the generating and pointed cases, the Archimedean condition, the order intervals and the order-bounded sets, the order unit and the order-unit norm, and the order topology together with the convex **state space** that the dual carries. It is the space on which the operator articles of this category act: the positive operators, the cone of positive operators, the order unit as an operator, the order projections, and the affine maps of a convex set.

The linear and topological background is *Topological Modules and Vector Spaces*, *Locally Convex Spaces* and *Duality Theory*, and the correspondence between a closed convex cone and a duality is *Duality Theory*; the order-theoretic vocabulary is *Order Theory and Lattices*. The order-unit norm is already used in *Jordan Algebras and the Positive Cone*, whose notation it is, and this article adopts it verbatim. The integral representation of a point of the state space is deferred to *Cones, Extremal Rays and the Choquet Theory* later in this category; the Riesz-space structure and the bands are deferred to *The Order Projection*.

## Ordered Vector Spaces

### The Positive Cone and the Order

**Definition.** Let $E$ be a real vector space. A **positive cone** is a subset $E_+\subseteq E$ such that

$$
E_+ + E_+ \subseteq E_+, \qquad \lambda E_+ \subseteq E_+ \ \text{for every } \lambda\geq0, \qquad E_+ \cap (-E_+) = \{0\}.
$$

An **ordered vector space** is a pair $(E,E_+)$; the cone is **generating** when $E = E_+ - E_+$, and the order is defined by

$$
x \leq y \iff y - x \in E_+ .
$$

**Proposition.** The relation $\leq$ is a partial order; it is compatible with the linear operations,

$$
x \leq y \implies x + z \leq y + z, \qquad x \leq y \implies \lambda x \leq \lambda y \ \text{for } \lambda \geq 0,
$$

and its positive part is $E_+$: $x\geq0$ exactly when $x\in E_+$. Conversely every partial order compatible with the linear operations and such that the order is determined by its positive part arises from the cone $E_+ = \{x : x\geq0\}$.

*Proof.* Reflexivity is $0\in E_+$; transitivity is closure under addition; antisymmetry is pointedness: $x\leq y$ and $y\leq x$ give $y-x\in E_+\cap(-E_+)$ and hence $y = x$. The two compatibility rules are closure under addition and under nonnegative scaling. Conversely a compatible order has $\{x : x\geq0\}$ closed under addition and under nonnegative scaling, and pointed because $\geq$ is antisymmetric.

The order is **total** when $E_+ \cup (-E_+) = E$, **directed** when every pair has an upper bound, and the cone is **generating** exactly when the order is directed in the sense that $E = E_+ - E_+$. In finite dimension a cone is generating exactly when it has nonempty interior, and then its interior is the set of **strictly positive** elements. A linear subspace $M$ is **order dense** when every element of $E$ lies between two elements of $M$.

### Order Boundedness and the Archimedean Property

**Definition.** The **order interval** with endpoints $x\leq y$ is

$$
[x,y] = \{z : x \leq z \leq y\} = (x + E_+) \cap (y - E_+) .
$$

A set is **order bounded** when it is contained in an order interval, and a subset $A\subseteq E$ is **bounded above** when some $y$ satisfies $a\leq y$ for all $a\in A$.

**Definition.** The ordered vector space is **Archimedean** when, for every $x,y$,

$$
n\,x \leq y \ \text{for every } n\in\mathbb{N} \implies x \leq 0 .
$$

The real line, every ordered subspace of a space of real functions under the pointwise order, and every ordered vector space whose cone is closed for a linear topology are Archimedean. The standard non-Archimedean example is the lexicographic order on $\mathbb{R}^2$, in which $(0,1)$ is an infinitesimal against $(1,0)$.

**Proposition.** If $x\leq\epsilon u$ for every real $\epsilon>0$, then $x\leq0$, in an Archimedean space; and conversely an ordered vector space with an order unit is Archimedean exactly when this implication holds.

*Proof.* With $\epsilon = 1/n$ and $y = u$ the Archimedean condition gives the first claim. For the converse, $nx\leq u$ for all $n$ gives $x\leq u/n$ for all $n$, hence $x\leq0$.

### Order Units

**Definition.** An **order unit** of an ordered vector space $E$ is an element $u\in E_+$ such that for every $x\in E$ there is $\lambda>0$ with

$$
-\lambda u \leq x \leq \lambda u .
$$

Equivalently, the order intervals $[-\lambda u,\lambda u]$ absorb $E$, so that $u$ is an **interior point of the cone** for the order topology defined below; and an order unit exists exactly when the cone is generating and has an element whose order interval is absorbing.

**Proposition (the order-unit norm).** Let $E$ be Archimedean with order unit $u$. The formula

$$
\|x\|_u = \inf\{\lambda > 0 : -\lambda u \leq x \leq \lambda u\}
$$

defines a norm on $E$, the **order-unit norm**, whose closed unit ball is the order interval $[-u,u]$, and for which $u$ has norm one.

*Proof.* The set in the infimum is nonempty by the order-unit property, and it is upward closed, so the infimum is a nonnegative real. Homogeneity and the triangle inequality come from the closure of $E_+$ under addition and nonnegative scaling: $[-\lambda u,\lambda u]+[-\mu u,\mu u]\subseteq[-(\lambda+\mu)u,(\lambda+\mu)u]$, and $[-\lambda u,\lambda u]$ is scaled by $\lambda$. For definiteness, $\|x\|_u = 0$ says $x\leq\epsilon u$ and $-x\leq\epsilon u$ for every $\epsilon>0$, whence $x\leq0$ and $x\geq0$ by the Archimedean property, so $x = 0$. The unit ball is $[-u,u]$ by definition, and $\|u\|_u = 1$.

**Proposition (uniqueness up to equivalence).** Any two order units $u,v$ give equivalent order-unit norms: there are constants $0 < c\leq C$ with

$$
c\,\|x\|_u \leq \|x\|_v \leq C\,\|x\|_u
$$

for all $x$, so the order topology does not depend on the order unit.

*Proof.* Since $u$ is an order unit there is $\alpha>0$ with $u\leq\alpha v$, and since $v$ is an order unit there is $\beta>0$ with $v\leq\beta u$. Then $[-\lambda u,\lambda u]\subseteq[-\lambda\alpha v,\lambda\alpha v]$ and $[-\lambda v,\lambda v]\subseteq[-\lambda\beta u,\lambda\beta u]$, which is the two inequalities with $C = \alpha$ and $c = 1/\beta$.

### The Order Topology

**Definition.** The **order topology** of an Archimedean ordered vector space with order unit is the topology of the order-unit norm. Its basic open sets are the translates of the order intervals $\epsilon[-u,u]$.

**Proposition.** In the order topology the cone $E_+$ is closed, the order intervals are closed convex bounded subsets, addition and nonnegative scaling are continuous, and the order unit lies in the interior of the cone.

*Proof.* The sets $[-\epsilon u,\epsilon u]$ are the closed balls of the norm, so intervals are closed; the cone is the intersection of the closed half-spaces $f\geq0$ over the functionals $f$ that are positive on the cone, and each such functional is continuous for the order-unit norm by the next proposition; addition is continuous because the norm is, and the unit ball is convex because the interval is. The order unit is interior to the cone because $u - \epsilon u$ has norm $1-\epsilon<1$ around it.

**Proposition (order-bounded functionals and the dual).** For a linear functional $f$ on $E$ the following are equivalent: $f$ is continuous for the order topology; $f$ is bounded on the order interval $[-u,u]$; $f$ is **order bounded**, meaning that it maps order-bounded sets to bounded sets of reals. The set of such functionals is the **order dual** $E'$, and $f\geq0$ in it exactly when $f(x)\geq0$ for every $x\in E_+$.

*Proof.* Continuity is boundedness on the unit ball $[-u,u]$, which is order boundedness; and a functional positive on the cone is monotone, hence bounded on an interval by its values at the endpoints, so order bounded. The positivity criterion is the definition of the dual order.

### The State Space

**Definition.** The **state space** of $E$ with order unit $u$ is the set of **states**,

$$
S = \{f\in E' : f\geq0,\ f(u) = 1\},
$$

a convex subset of the dual, and a **pure state** is an extreme point of $S$.

**Proposition.** $S$ is nonempty, convex, and a base of the cone $(E')_+$ of positive functionals: every positive functional is a nonnegative multiple of a state. When $E$ is a Banach space in its order-unit norm and $u$ is its own unit, $S$ is weak-* compact, by the Banach–Alaoglu theorem of *Duality Theory*, so it has extreme points by the Krein–Milman theorem of *Convex Sets and the Convex Hull*.

*Proof.* The order-unit property and the Hahn–Banach theorem produce a functional with $f(u)=1$ and $\lvert f\rvert\leq1$ on $[-u,u]$, which is a state. Convexity is linearity in $f$; the base property is that every $g\geq0$ with $g(u)=\alpha>0$ is $g = \alpha(g/\alpha)$ with $g/\alpha$ a state. The compactness is the weak-* compactness of the polar of the unit ball, and the extreme points follow.

The cone of positive functionals, the states and their extreme points are developed in *The Cone of Positive Functionals* later in this category; the integral representation of a state and the Choquet boundary in *Cones, Extremal Rays and the Choquet Theory*.

## Worked Cases

### The Space of Continuous Functions

Let $E = C(X)$ be the continuous real functions on a compact Hausdorff space, with the pointwise order, so that $E_+$ is the cone of nonnegative functions, and let $u = 1$ be the constant function. The space is Archimedean, $1$ is an order unit, the order-unit norm is the supremum norm, and the order topology is the topology of uniform convergence. The states are the probability measures on $X$ by the Riesz representation theorem; the pure states are the point evaluations, which is the Krein–Milman theorem for the simplex of probability measures, and the finite-dimensional case is the simplex of *Convex Analysis*.

### A Matrix Algebra

Let $E = H_n(\mathbb{R})$ be the real symmetric matrices under the Loewner order, whose cone is the positive semidefinite matrices. The identity matrix is an order unit, the order-unit norm is the operator norm, since $-\lambda 1\leq x\leq\lambda1$ for a Hermitian $x$ exactly when every eigenvalue of $x$ lies in $[-\lambda,\lambda]$, and the order topology is the norm topology. The states are the positive linear functionals normalised at the identity; the extreme ones are the vector states, and this is the finite-dimensional instance of the theory of *Jordan Algebras and the Positive Cone*.

## Summary

An **ordered vector space** is a real vector space with a positive cone $E_+$ that is closed under addition and nonnegative scaling and is pointed, and the order $x\leq y \iff y-x\in E_+$ is a partial order compatible with the linear operations, with positive part $E_+$; it is total or directed according to the cone, and generating when the cone has nonempty interior in finite dimension. The space is **Archimedean** when $nx\leq y$ for all $n$ forces $x\leq0$. An **order unit** $u$ is a positive element whose order intervals absorb the space; it defines the **order-unit norm** $\|x\|_u = \inf\{\lambda>0 : -\lambda u\leq x\leq\lambda u\}$, whose closed unit ball is $[-u,u]$, and two order units give equivalent norms, so the **order topology** is independent of the unit. In the order topology the cone is closed, the intervals are closed convex bounded, the operations are continuous, and the order-bounded functionals are exactly the continuous ones, so the order dual is the dual. The **state space** $S = \{f\geq0 : f(u)=1\}$ is a convex base of the positive cone of the dual, weak-* compact in the Banach case and hence with extreme points. The order-unit norm is the notation of *Jordan Algebras and the Positive Cone*; the duality is *Duality Theory*; the extreme-point theory is *Convex Sets and the Convex Hull*; the Riesz-space structure is deferred to *The Order Projection*, and the integral representation to *Cones, Extremal Rays and the Choquet Theory*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $E$, $E_+$ | Ordered vector space, positive cone |
| $x\leq y$ | $y - x\in E_+$ |
| $[x,y]$ | Order interval between $x$ and $y$ |
| Order bounded, directed, generating | Contained in an interval; every pair bounded above; $E = E_+ - E_+$ |
| Archimedean | $nx\leq y$ for all $n$ implies $x\leq0$ |
| $u$ | Order unit |
| $\|x\|_u = \inf\{\lambda > 0 : -\lambda u \leq x \leq \lambda u\}$ | Order-unit norm |
| $S = \{f\in E' : f\geq0,\ f(u)=1\}$ | State space, a convex base of $(E')_+$ |
| Pure state | Extreme point of $S$ |

## Further Reading

- Nicolas Bourbaki, *Topological Vector Spaces*, Chapters 1–5 (Springer, 1987), for ordered vector spaces, cones and the order topology.
- Graham Jameson, *Ordered Linear Spaces*, Lecture Notes in Mathematics 141 (Springer, 1970), for the positive cone, the order unit and the order-unit norm in their general form.
- Charalambos D. Aliprantis and Owen Burkinshaw, *Positive Operators* (Academic Press, 1985), for the cone, the order topology and the order dual.
- Karl R. Stromberg, *An Introduction to Classical Real Analysis* (Wadsworth, 1981), for the order-unit norm and the state space in the function-space case.
- Erik M. Alfsen, *Compact Convex Sets and Boundary Integrals* (Springer, 1971), for the state space as a convex set and its extreme points.
