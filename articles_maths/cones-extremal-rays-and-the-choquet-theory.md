
# __Cones, Extremal Rays and the Choquet Theory__

## Introduction

A **cone** is a convex set closed under nonnegative scaling, and its one-dimensional convex subsets are its **rays**. A ray that cannot be the sum of two vectors outside it is an **extremal ray**, and the extremal rays are the primitive directions of a cone in exactly the sense in which the extreme points are the primitive points of a convex set: a **base** cuts the cone by a hyperplane, the extreme rays of the cone become the extreme points of the base, and the theory of one is the theory of the other. This is the structure that an **ordered vector space** carries its order in: the positive cone, its rays, and the order that the rays generate.

The second half of the article is the **Choquet theory**, the integral representation of the points of a compact convex set by measures carried by its extreme points. A compact convex set is the closed convex hull of its extreme points by Krein–Milman, but that is a statement about the closure; Choquet's theorem states that every point is the **barycentre** of a *measure* concentrated on the extreme set, and it is therefore a much finer statement, because the measure remembers the proportions in which the extreme points are mixed. The extreme points are the **Choquet boundary** for a metrizable compact convex set, by the Choquet–Bishop–de Leeuw theorem, and the representing measure is unique exactly when the set is a **simplex**, by the Choquet–Meyer theorem. These are the results that make a compact convex set an integral-representation device, and they are used by the order theory of the states and the weights later in this category.

The setting is the one of *Convex Sets and the Convex Hull*: a real locally convex space, with compactness used where Krein–Milman is used. The cones and the ordered vector spaces are those of *Ordered Vector Spaces and the Order Unit*, whose state space is the principal example; the duality of a cone with its polar, and the bipolar theorem, are *Duality Theory*; the measure and the integral are *Measure Theory and Integration*, in the *Foundations of Analysis* category of this Part. The finite-dimensional theory of cones, polyhedral cones and their extreme rays is *Convex Analysis* and is cited.

## Convex Cones and their Rays

### Cones, the Order and the Dual

**Definition.** A subset $C$ of a real vector space $E$ is a **convex cone** when it is convex and closed under nonnegative scaling,

$$
C + C \subseteq C, \qquad \lambda C \subseteq C \ \text{for } \lambda\geq0 .
$$

It is **pointed** when $C\cap(-C) = \{0\}$, **generating** when $C - C = E$, and **proper** when it is pointed. A pointed convex cone makes $E$ an ordered vector space by $x\leq y \iff y - x\in C$, and conversely the positive cone of an ordered vector space is a pointed convex cone.

**Definition.** A **ray** of $C$ is the set $\mathbb{R}_{\geq0}\,x = \{tx : t\geq0\}$ of nonnegative multiples of a nonzero $x\in C$. A ray $R$ is **extremal** when

$$
x, y\in C,\ x + y\in R \implies x, y\in R .
$$

A vector $x\in C$ is an **extremal generator** when its ray is extremal, and the set of extremal rays is written $\operatorname{ray}(C)$.

**Proposition.** For a convex cone $C$ the extremal rays are exactly the one-dimensional faces of $C$; the cone is the conical hull of its extremal rays when it is closed, polyhedral and pointed; and the sum of two vectors on distinct extremal rays lies on no extremal ray.

*Proof.* If $R$ is a face and one-dimensional then $x+y\in R$ with $x,y\in C$ puts $x$ and $y$ in the face $R$ by the face condition, so $R$ is extremal; conversely an extremal ray is a face because a segment with endpoints in $C$ meeting the ray has its endpoints in the ray. The generation by extremal rays is the finite-dimensional Minkowski statement of *Convex Analysis*; the last claim is the contrapositive of the defining property.

### Bases

**Definition.** A **base** of a convex cone $C$ is a convex subset $B\subseteq C$ such that every nonzero $x\in C$ is a unique positive multiple of a point of $B$; equivalently $B = C\cap f^{-1}(1)$ for a linear functional $f$ with $f>0$ on $C\setminus\{0\}$.

**Proposition (extreme points of a base are extremal rays).** Let $B$ be a base of a convex cone $C$. The map $x\mapsto\mathbb{R}_{\geq0}\,x$ sends the extreme points of $B$ onto the extremal rays of $C$, and it is a bijection between them.

*Proof.* If $b\in B$ is extreme and $x+y\in\mathbb{R}_{\geq0}b$ with $x,y\in C$, divide by $f(x+y)=1$ and write $x = f(x)\,b_1$, $y = f(y)\,b_2$ with $b_1,b_2\in B$ and $f(x),f(y)\geq0$; then $b$ is the convex combination $f(x)b_1 + f(y)b_2$, and extremality forces $x,y$ onto the ray of $b$. Conversely if the ray of $b$ is extremal and $b = tx_1+(1-t)x_2$ with $x_i\in B$, then $b$ is the sum of $tx_1$ and $(1-t)x_2$ in the cone, so both are on the ray of $b$, and being in $B$ and on that ray they equal $b$.

**Proposition (the dual cone and the base of the dual).** The **dual cone** of $C$ is

$$
C^* = \{f\in E' : f(x)\geq0 \ \text{for every } x\in C\},
$$

a closed convex cone in the dual for the weak-* topology; when $C$ is closed, proper and generating with a base, the states $S = \{f\in C^* : f(u) = 1\}$ of *Ordered Vector Spaces and the Order Unit* are a base of $C^*$, weak-* compact when the base of $C$ is compact.

*Proof.* $C^*$ is the intersection of the closed half-spaces $\{f : f(x)\geq0\}$, hence a closed convex cone. Every nonzero $f\in C^*$ has $f(u)>0$ when $u$ is an order unit in the interior of $C$, so $f/f(u)$ lies in $S$ and the representation is unique; the compactness is that of the polar of the order interval, which is the base.

## The Choquet Theory

### Measures and Barycentres

**Definition.** Let $K$ be a compact convex subset of a real locally convex space $E$. A probability measure $\mu$ on $K$ has a **barycentre** $r(\mu)\in K$, the unique point satisfying

$$
f\bigl(r(\mu)\bigr) = \int_K f\,d\mu \qquad \text{for every } f\in E' .
$$

The measure **represents** $x$ when $r(\mu) = x$, and the set of representing measures is a convex weak-* compact subset of the probability measures on $K$.

**Proposition.** The barycentre exists and lies in $K$; the assignment $\mu\mapsto r(\mu)$ is affine and weak-* to weak continuous; and the point mass $\delta_x$ represents $x$.

*Proof.* The functional $f\mapsto\int f\,d\mu$ is linear and continuous on $E'$ with respect to the topology of uniform convergence on $K$; it is a positive functional of norm one; the point it defines lies in $K$ because $K$ is the intersection of the half-spaces containing it and a point outside would be separated from $K$ by a functional whose integral would then violate $\lvert f\rvert\leq\sup_K\lvert f\rvert$. Affineness in $\mu$ is linearity of the integral; and $\delta_x$ gives $f(x)$.

**Definition.** The **order** on the representing measures is

$$
\mu\preceq\nu \iff \mu(f)\leq\nu(f) \ \text{for every continuous convex } f:K\to\mathbb{R},
$$

and a measure is **maximal** when it is maximal for $\preceq$. The **Choquet boundary** $\partial K$ is the set of points $x$ whose point mass $\delta_x$ is maximal, equivalently the points at which every upper semicontinuous convex function that is $\leq0$ on $\operatorname{ext} K$ is $\leq0$ at $x$.

### Choquet's Theorem

**Theorem (Choquet).** Let $K$ be a compact convex subset of a locally convex space. Every $x\in K$ is the barycentre of a maximal probability measure: there is $\mu$ on $K$ with $r(\mu) = x$ and $\mu\preceq\nu$ for every representing measure $\nu$ of $x$.

*Proof.* The set $M_x$ of representing measures of $x$ is nonempty (it contains $\delta_x$) and weak-* compact, and the order $\preceq$ is inductive on it, an upper bound of a chain being any weak-* cluster point; Zorn's lemma gives a maximal element. The delicate point is that the supremum of a chain of measures exists as a measure, which is the Riesz representation theorem of *Measure Theory and Integration* applied to the limit of the integrals of convex functions, and it is the step where compactness of $K$ is consumed.

**Theorem (Choquet–Bishop–de Leeuw).** Every maximal measure $\mu$ on $K$ is carried by the Choquet boundary, $\mu(K\setminus\partial K) = 0$. Consequently, for a metrizable $K$, where $\partial K = \operatorname{ext} K$, every $x\in K$ is the barycentre of a measure carried by the extreme points,

$$
x = \int_{\operatorname{ext} K} e\,d\mu(e) .
$$

*Proof.* If $x\notin\partial K$ there is an upper semicontinuous convex $f$ with $f(x)>0$ and $f\leq0$ on $\partial K$; the set where $f$ attains its positive maximum is a compact convex subset of $K$ disjoint from the boundary, and a maximal measure gives it no mass, by the maximality; iterating over the boundary and using the metrizability to run a countable exhaustion yields the result. The identification $\partial K = \operatorname{ext} K$ in the metrizable case is the Choquet–Bishop–de Leeuw theorem.

### The Bauer Maximum Principle and the Simplices

**Theorem (Bauer).** Let $K$ be compact convex and let $f : K\to\mathbb{R}$ be upper semicontinuous and convex. Then $f$ attains its maximum at an extreme point of $K$.

*Proof.* The set $F$ of maximisers is a nonempty compact face of $K$, and a compact convex set has an extreme point $x$; an extreme point of the face $F$ is extreme in $K$, and it maximises $f$.

**Definition.** A compact convex set $K$ is a **simplex** when every $x\in K$ has a unique maximal representing measure, equivalently when the cone of affine continuous functions together with the constants is generated by its positive part in the order of *Ordered Vector Spaces and the Order Unit*.

**Theorem (Choquet–Meyer).** For a compact convex set $K$ the following are equivalent: $K$ is a simplex; every $x\in K$ is represented by a unique maximal measure; the barycentric map from the probability measures on $\operatorname{ext} K$ to $K$ is a bijection. A simplex is affinely isomorphic to the set of probability measures on a compact Hausdorff space only in the finite-dimensional case, where it is the convex hull of affinely independent points.

*Proof.* Uniqueness of the maximal measure at every point is equivalent to the cone of affine functions being **lattice generated**, which is the statement that the dual order is a Riesz order in the sense of *The Order Projection*; the equivalence of the lattice condition with the uniqueness is the theorem of Choquet and Meyer. The affine isomorphism for a finite simplex is the one of *Convex Sets and the Convex Hull*.

## Worked Cases

### The Cone of Positive Semidefinite Matrices

Let $C = H_n(\mathbb{R})_+$ be the cone of positive semidefinite matrices, a pointed generating cone in the real symmetric matrices. Its extremal rays are the rays $\mathbb{R}_{\geq0}\,vv^{\mathsf{T}}$ of the rank-one positive matrices, indexed by the lines of $\mathbb{R}^n$ up to sign; the base cut out by the trace is the set of density matrices, whose extreme points are the rank-one projections, and the identification is the bijection of the base proposition. Every positive semidefinite matrix is the sum of at most $n$ rank-one positive matrices with positive coefficients, by the spectral theorem, which is the finite-dimensional instance of the conical hull of the extremal rays.

### The State Space of the Continuous Functions

Let $K = \{\mu : \mu\geq0,\ \mu(X) = 1\}$ be the probability measures on a compact Hausdorff space $X$, viewed as a weak-* compact convex subset of the dual of $C(X)$; it is a simplex, and the extreme points are the point masses $\delta_x$ by the Bauer maximum principle applied to the evaluation $f\mapsto f(x)$. The barycentric map from the probability measures on the extreme points to $K$ is the identity, and the uniqueness of the representing maximal measure is the statement that a probability measure on $X$ is determined by its integrals against the continuous functions.

### The Interval

Take $K = [0,1]$, a compact convex subset of $\mathbb{R}$, whose extreme points are $0$ and $1$. Every $x\in K$ is the barycentre of the unique measure $(1-x)\delta_0 + x\delta_1$, so $K$ is a simplex with one-dimensional maximal measures; this is the smallest instance of the theory and the model for the integral representation of a state of the order-unit space of *Ordered Vector Spaces and the Order Unit*.

## Summary

A **convex cone** is a convex set closed under nonnegative scaling; it is pointed, generating and proper in the usual senses, and it is exactly what an ordered vector space orders by. Its **rays** are its one-dimensional subsets, and the **extremal rays** are its one-dimensional faces, exactly those rays $R$ with $x+y\in R$, $x,y\in C$, forcing $x,y\in R$. A **base** cuts the cone by a hyperplane, the extreme points of the base correspond bijectively to the extremal rays of the cone, and the dual cone carries the weak-* compact **state space** as a base. On a compact convex set $K$ every probability measure has a **barycentre** $r(\mu)$ with $f(r(\mu)) = \int f\,d\mu$, and **Choquet's theorem** states that every point is the barycentre of a **maximal** measure; **Choquet–Bishop–de Leeuw** states that a maximal measure is carried by the **Choquet boundary**, which is the set of extreme points when $K$ is metrizable; and the **Choquet–Meyer theorem** states that the representing maximal measure is unique at every point exactly when $K$ is a **simplex**. **Bauer's maximum principle** states that an upper semicontinuous convex function attains its maximum at an extreme point. The cones and the order are *Ordered Vector Spaces and the Order Unit*, the extreme points and Krein–Milman are *Convex Sets and the Convex Hull*, the duality of cones is *Duality Theory*, the integral and the Riesz representation theorem are *Measure Theory and Integration*, and the polyhedral cones are *Convex Analysis*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $C$, $E_+$ | Convex cone; positive cone of an ordered vector space |
| $\mathbb{R}_{\geq0}\,x$ | The ray through $x$ |
| Extremal ray | A one-dimensional face of the cone |
| $B = C\cap f^{-1}(1)$ | A base of the cone, $f>0$ on $C\setminus\{0\}$ |
| $C^* = \{f : f\geq0 \text{ on } C\}$ | Dual cone |
| $r(\mu)$ | Barycentre of the probability measure $\mu$ |
| $\mu\preceq\nu$ | Order of measures, $\mu(f)\leq\nu(f)$ for convex continuous $f$ |
| $\partial K$ | Choquet boundary |
| Simplex | A compact convex set with a unique maximal representing measure at each point |

## Further Reading

- Gustave Choquet, "Remarques à propos de la démonstration d'unicité de P.-A. Meyer", *Séminaire Brelot–Choquet–Deny* **6** (1962), for the uniqueness theory of the simplices.
- Gustave Choquet and Paul-André Meyer, "Existence et unicité des représentations intégrales dans les convexes compacts quelconques", *Annales de l'Institut Fourier* **13** (1963), 139–154, for the Choquet–Meyer theorem.
- Errett Bishop and Karl de Leeuw, "The representations of linear functionals by measures on sets of extreme points", *Annales de l'Institut Fourier* **9** (1959), 305–331, for the Choquet–Bishop–de Leeuw theorem.
- Heinz Bauer, "Minimalstellen von Funktionen und Extremalpunkte", *Archiv der Mathematik* **9** (1958), 389–393, for the maximum principle.
- Erik M. Alfsen, *Compact Convex Sets and Boundary Integrals* (Springer, 1971), for the integral representation in full.
- Robert R. Phelps, *Lectures on Choquet's Theorem* (Van Nostrand, 2nd ed. 2001), for a concise modern treatment.
