
# __Operators on a Convex Set__

## Introduction

A convex set carries a structure of its own: the affine maps, those that preserve the segments, are its endomorphisms, and the affine automorphisms are its group. Read dually, the affine maps of a convex set are the positive unital maps of a space of functions, and this makes the affine maps the **operators** of the convex-set theory in exactly the sense in which the linear maps are the operators of the vector-space theory: they are the maps that the two dual descriptions describe from opposite sides. On a compact convex set $K$ the two sides are the affine continuous functions $A(K)$, an **order-unit space** whose order unit is the constant function $1$ and whose state space is $K$ itself, and the affine maps $L\to K$, in bijection with the positive unital maps $A(K)\to A(L)$.

The article uses these operators to reach the **Choquet boundary**, the object that plays the role of the extreme points for a compact convex set that is not metrizable. A point lies in the Choquet boundary exactly when its evaluation is a **pure state** of $A(K)$, that is, an extreme point of the state space; the boundary contains the extreme points, coincides with them when $K$ is metrizable, and is the support of the representing measures of Choquet's theorem. The boundary is thus an operator-theoretic object: it is the set of points whose evaluations are the extreme rays of the dual cone of $A(K)$.

The convex sets and their extreme points are *Convex Sets and the Convex Hull*; the cones and the extreme rays are *Cones, Extremal Rays and the Choquet Theory*, which also owns the integral representation and the maximal measures; the order-unit space, its state space and the evaluation are *Ordered Vector Spaces and the Order Unit* and *The Order Unit as an Operator*; the positive operators and the positivity of the function systems are *Positive Operators on an Ordered Space*. The finite-dimensional theory of affine maps is *Convex Analysis* in the *Foundations of Analysis* category of this Part, and it is cited. The affine maps of a convex set that arise from an algebra action are *The Left and Right Multiplication Operators on an Ordered Algebra* later in this category.

## Affine Maps and Function Systems

### Affine Maps

**Definition.** Let $C,D$ be convex sets. A map $f : C\to D$ is **affine** when

$$
f\bigl((1-t)x+ty\bigr) = (1-t)f(x)+tf(y) \qquad \text{for all } x,y\in C,\ t\in[0,1].
$$

An affine bijection with affine inverse is an **affine isomorphism**, and an affine isomorphism of $C$ with itself is an **affine automorphism**.

**Proposition.** An affine map is determined by its values on the extreme points of its domain when those span the domain affinely; the composite of affine maps is affine; and the affine automorphisms of a convex set form a group under composition.

*Proof.* An affine combination of the values of $f$ at the points of a set is determined by the affine combination of the points, which is the content of affinity; the linearity of composition in the affine relations is direct; and the automorphisms are closed under composition and inversion by definition.

**Example.** An affine map of a convex cone is a linear map; an affine map $f:C\to\mathbb{R}$ is an **affine function** on $C$; the affine functions form a linear space, the affine maps into a convex set $D$ form a convex set under the pointwise convex combinations, and the affine endomorphisms form only a semigroup.

### The Function System of a Compact Convex Set

**Definition.** For a compact convex set $K$ in a real locally convex space let

$$
A(K) = \{a : K\to\mathbb{R} \ \text{affine and continuous}\} ,
$$

with the supremum norm and the pointwise order, and with the constant function $1$ as order unit.

**Proposition (the function system).** $A(K)$ is an **order-unit space**: it is an Archimedean ordered vector space whose order is the pointwise one, whose order-unit norm is the supremum norm, and whose order unit is the constant function $1$. The restriction to $K$ of every continuous affine function on the ambient space belongs to $A(K)$, and these restrictions separate the points of $K$ by the separation theorem of *Duality Theory*.

*Proof.* Pointwise order and norms are computed pointwise; the supremum norm is the order-unit norm of $1$ because $-\lambda1\leq a\leq\lambda1$ pointwise is $\lvert a\rvert\leq\lambda$ uniformly. The separation statement is the Hahn–Banach theorem applied to two distinct points of the convex set.

**Theorem (the state space of the function system is the convex set).** For a compact convex set $K$ the map

$$
\mathrm{ev} : K\to S(A(K)), \qquad \mathrm{ev}(x)(a) = a(x),
$$

is an affine homeomorphism onto the state space of $A(K)$.

*Proof.* The evaluation is affine in $x$ and positive unital in $a$, so it lands in the state space. Injectivity is the separation of points by $A(K)$; surjectivity is the fact that a positive unital functional on $A(K)$ extends to a positive functional on $C(K)$ and is therefore integration against a probability measure $\mu$, whose barycentre $x$ satisfies $\int a\,d\mu = a(x)$ for every affine $a$ by the affine character of $a$, so the functional is $\mathrm{ev}(x)$. Continuity of $\mathrm{ev}$ and of its inverse is the weak-* topology against the sup norm, and the map is a homeomorphism by the compactness of the two spaces.

## Affine Maps as Operators

### The Duality with Positive Unital Maps

**Theorem.** For compact convex sets $K$ and $L$ the assignment

$$
g\mapsto \Phi_g, \qquad \Phi_g(a) = a\circ g \quad (a\in A(K)),
$$

is an affine bijection from the continuous affine maps $g : L\to K$ onto the positive unital linear maps $\Phi : A(K)\to A(L)$, with inverse sending $\Phi$ to the map whose evaluation at $y\in L$ is $\Phi(\cdot)(y)$.

*Proof.* If $g$ is affine and continuous then $\Phi_g$ is linear, and it is positive and unital because $a\geq0$ implies $a\circ g\geq0$ and $a = 1$ gives $1$. Conversely if $\Phi$ is positive and unital, the functional $\Phi(\cdot)(y)$ is a state of $A(K)$ for every $y\in L$, so by the previous theorem it is the evaluation at a unique $g(y)\in K$, and $y\mapsto g(y)$ is affine and continuous because each $a\circ g = \Phi(a)$ is; the two assignments are inverse by construction.

**Proposition (affine maps preserve barycentres).** Let $g : L\to K$ be continuous affine and let $\mu$ be a probability measure on $L$ with barycentre $y$. Then $g(y)$ is the barycentre of the pushed-forward measure $g_*\mu$ on $K$,

$$
g\bigl(r(\mu)\bigr) = r(g_*\mu).
$$

*Proof.* For $a\in A(K)$ one has $\int a\,d(g_*\mu) = \int (a\circ g)\,d\mu = (a\circ g)(y) = a(g(y))$, using the affinity of $a$ and $g$ through the barycentre of $\mu$; the two sides therefore have the same values against every $a$, and they are equal by the separation of points of $K$.

**Corollary (the group of affine automorphisms acts on the function system).** The affine automorphisms of $K$ correspond to the **order automorphisms** of $A(K)$, that is, the linear bijections preserving the cone and the order unit, by $g\mapsto \Phi_g$; the correspondence is an isomorphism of groups.

*Proof.* An affine automorphism has an affine inverse, so $\Phi_g$ is a unital bijection preserving positivity in both directions, hence an order automorphism; conversely an order automorphism $\Phi$ of $A(K)$ comes from an affine map $g$ by the theorem, and its inverse comes from an affine map that is the inverse of $g$ by the bijection.

### The Extreme Structure of the Set of Operators

**Proposition (the extreme affine maps).** The extreme points of the convex set of positive unital maps $A(K)\to A(L)$ are the maps $\Phi$ that are **multiplicative** on the extreme structure of $A(K)$: for a function system $A(K)$ that is a lattice, the extreme positive unital maps are the **lattice homomorphisms**. In particular, when $A(K) = C(K)$, the extreme positive unital maps $C(K)\to C(L)$ are the maps $a\mapsto a\circ g$ for a continuous $g : L\to K$, and no other.

*Proof.* A positive unital map $C(K)\to C(L)$ is extreme exactly when it is a lattice homomorphism, by the characterisation of the extreme positive operators of a function space in *The Cone of Positive Operators*; a unital lattice homomorphism $C(K)\to C(L)$ is the pullback along a continuous map, by the Gelfand–Kolmogorov theorem, giving the second statement. The general function system reduces to its lattice envelope.

## The Choquet Boundary

**Definition.** The **Choquet boundary** of a compact convex set $K$ is the set $\partial K$ of points $x$ whose evaluation $\mathrm{ev}(x)$ is an extreme point of the state space $A(K)^*_+\cap\{\cdot(1) = 1\}$; equivalently, the points such that the point mass $\delta_x$ is the only **maximal** representing measure.

**Proposition (the boundary is the extreme points, generally with inclusion).** The extreme points of $K$ lie in the Choquet boundary,

$$
\operatorname{ext} K \subseteq \partial K ,
$$

and the inclusion is an equality when $K$ is metrizable. The Choquet boundary is a $G_\delta$ subset when $K$ is metrizable, and it is a boundary in the sense that every continuous affine function attains its maximum on it.

*Proof.* If $x$ is extreme and $x = \int y\,d\mu(y)$ with $\mu$ a maximal measure, then $\mu$ is the point mass at $x$, by the extremality; hence $\mathrm{ev}(x)$ is extreme. Equality in the metrizable case is the Choquet–Bishop–de Leeuw theorem of *Cones, Extremal Rays and the Choquet Theory*, which identifies the Choquet boundary with the extreme points there. The maximum principle is Bauer's theorem of the same article, applied to the upper semicontinuous convex function $a$.

**Theorem (the boundary is where the representing measure is unique).** For $x\in K$ the following are equivalent: $x\in\partial K$; the evaluation $\mathrm{ev}(x)$ generates an extreme ray of the dual cone $A(K)^*_+$; the only maximal measure representing $x$ is $\delta_x$; and every continuous convex function $f$ on $K$ satisfies $f(x)\geq\int f\,d\mu$ for every representing measure $\mu$ of $x$.

*Proof.* The first two are equivalent by the correspondence between extreme points of a base and extreme rays of the cone, in *Cones, Extremal Rays and the Choquet Theory*. The equivalence of the first and the third is the definition of the boundary through maximal measures; the equivalence with the last is the integral inequality characterising the maximality of a representing measure, since a convex continuous $f$ is the supremum of affine continuous functions below it.

**Corollary (the boundary of a simplex and of a polytope).** For a finite-dimensional polytope the Choquet boundary is the set of its vertices; for the simplex of probability measures on a compact Hausdorff space it is the set of the point masses; and for the disk it is the circle. In each case the boundary is the set on which the representing maximal measure is unique, which is the property the operators of the convex set are built to detect.

*Proof.* A polytope is metrizable, so its Choquet boundary is its extreme-point set, which is its vertices; the probability simplex has the point masses as its extreme points; and the disk has the circle as its extreme set.

## Worked Cases

### The Interval

Let $K = [0,1]$. The affine continuous functions are the affine functions $a(t) = \alpha+\beta t$, the function system is two-dimensional, the state space is $[0,1]$ under the evaluation, and the affine maps of $[0,1]$ into itself are the maps $t\mapsto\alpha+\beta t$ with the image condition $0\leq\alpha,\alpha+\beta\leq1$, a convex set. The Choquet boundary is $\{0,1\}$, and the positive unital maps $A(K)\to A(K)$ are the affine reparametrisations.

### The Disk

Let $K = \overline{\mathbb{D}}$ be the closed unit disk. The affine continuous functions are the restrictions of the affine functions $z\mapsto \alpha + \operatorname{Re}(\lambda z)$, the state space is the disk, and the affine automorphisms are the rotations about the centre together with the reflection $z\mapsto\bar z$, a group isomorphic to the orthogonal group of the plane restricted to the disk. The Choquet boundary is the unit circle. For an interior point $z$ the maximal representing measures are exactly the probability measures on the unit circle with barycentre $z$, and there are many of them: the disk is not a simplex, and the harmonic measure is only one point of a large convex set. This is the standard example of a compact convex set that is not a simplex, in which the maximal representing measure of a point is far from unique.

### The State Space of a Function System

For an order-unit space $E$ with state space $K = S(E)$ the affine continuous functions on $K$ contain $E$ as a subspace by the evaluation embedding of *The Order Unit as an Operator*, and $A(K) = E$ exactly in the case of the Kadison representation theorem. The affine maps of $K$ into itself are the transposes of the positive unital maps of $E$, and the Choquet boundary of $K$ is the set of points where the state is pure; this is the general form of the statement that the pure states are the boundary of the state space.

## Summary

The **affine maps** of a convex set are its endomorphisms: they preserve the segments, they compose, and the automorphisms form a group. For a compact convex set $K$ the affine continuous functions $A(K)$ form the **function system**, an order-unit space with the constant $1$ as unit and the supremum norm, whose **state space is $K$ itself** under the evaluation. The affine maps $L\to K$ correspond bijectively and contravariantly to the **positive unital maps** $A(K)\to A(L)$ by $g\mapsto(a\mapsto a\circ g)$; affine maps preserve **barycentres**, $g(r(\mu)) = r(g_*\mu)$; and the affine automorphisms correspond to the order automorphisms of $A(K)$. The extreme positive unital maps of a function system are the lattice homomorphisms, and for $C(K)$ they are exactly the pullbacks along continuous maps. The **Choquet boundary** $\partial K$ is the set of points whose evaluation is an **extreme point of the state space**, equivalently the points whose only maximal representing measure is the point mass; it contains the extreme points, equals them in the metrizable case, and supports the integral representation of Choquet's theorem. The convex sets and the extreme points are *Convex Sets and the Convex Hull*; the integral representation, the maximal measures and the boundary are *Cones, Extremal Rays and the Choquet Theory*; the order-unit space and the evaluation are *Ordered Vector Spaces and the Order Unit* and *The Order Unit as an Operator*; and the algebraic affine maps are *The Left and Right Multiplication Operators on an Ordered Algebra* later in this category.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| Affine map | Map preserving the convex combinations |
| $A(K)$ | Continuous affine functions on the compact convex set $K$ |
| Function system | $A(K)$ as an order-unit space with unit $1$ |
| $\mathrm{ev}(x)(a) = a(x)$ | Evaluation, an affine homeomorphism $K\to S(A(K))$ |
| $\Phi_g(a) = a\circ g$ | Positive unital map associated to the affine map $g$ |
| $g(r(\mu)) = r(g_*\mu)$ | Preservation of the barycentre |
| $\partial K$ | Choquet boundary |
| $\operatorname{ext}K\subseteq\partial K$ | Inclusion, equality in the metrizable case |

## Further Reading

- Erik M. Alfsen, *Compact Convex Sets and Boundary Integrals* (Springer, 1971), for the function system, the state space and the Choquet boundary.
- Errett Bishop and Karl de Leeuw, "The representations of linear functionals by measures on sets of extreme points", *Annales de l'Institut Fourier* **9** (1959), 305–331, for the boundary and the extreme points.
- Heinz Bauer, "Minimalstellen von Funktionen und Extremalpunkte", *Archiv der Mathematik* **9** (1958), 389–393, for the maximum principle and the boundary.
- Gustave Choquet, *Lectures on Analysis, vol. II: Representation Theory* (Benjamin, 1969), for the affine maps and the integral representation.
- Israel Gelfand and Georgi Kolmogorov, "Über verschiedene Definitionen der Wahrscheinlichkeitsrechnung", *Recueil Mathématique* **1** (1936), 45–55, for the representation of the lattice homomorphisms of $C(K)$.
