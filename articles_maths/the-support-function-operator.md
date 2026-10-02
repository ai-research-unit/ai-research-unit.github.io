
# __The Support Function Operator__

## Introduction

The **support function** of a convex set $K$ is

$$
\sigma_K(u) = \sup_{x\in K}\langle u,x\rangle ,
$$

the greatest value the linear functional $u$ takes on $K$. It is a convex function of $u$, and it is positively homogeneous, so it is **sublinear**; and the assignment $K\mapsto\sigma_K$ is the **support function operator**, an order isomorphism from the convex sets to the sublinear functions under which the Minkowski sum of the sets becomes the pointwise sum of the functions and the convex hull of a union becomes the pointwise maximum. The operator is therefore the exact analogue, on the side of the convex sets, of the map that sends a set of vectors to the supremum of the linear functionals it supports, and it is the same map that the Legendre transform applies to the indicator of $K$: $\sigma_K = \delta_K^*$ in the notation of *Convex Functions and the Legendre Transform*.

The second half of the article is the **polar duality**. The polar $K^{\circ}$ collects the functionals bounded by one on $K$, the support function of the polar is the **gauge** of the closed convex set, and the **bipolar theorem** reconstructs a closed convex set from its polar. The support function is the bijection that makes the duality explicit: it is an order isomorphism, it is an isometry for the Hausdorff metric and the uniform metric, and it converts the operations of the convex sets into the operations of the sublinear functions.

The convex sets and their operations are *Convex Sets and the Convex Hull* and *Helly's Theorem and the Approximation of Convex Sets*, which uses the support function and its isometry property and defers the operator statement here; the cones, the polar cones and the extreme rays are *Cones, Extremal Rays and the Choquet Theory*; the duality pairing, the polar and the bipolar theorem are *Duality Theory*; the conjugacy and the subdifferential are *Convex Functions and the Legendre Transform*; and the positive operators and the operator order are *Positive Operators on an Ordered Space*. The support function of a finite-dimensional polytope and the facial structure of a polyhedron are *Convex Analysis*, and they are cited.

## The Support Function

### Definition and Sublinearity

**Definition.** Let $E$ and $E'$ be a dual pair and let $K\subseteq E$ be a nonempty convex set. The **support function** of $K$ is the function on $E'$

$$
\sigma_K(u) = \sup_{x\in K}\langle u,x\rangle ,
$$

with the value $+\infty$ when the supremum is unbounded, and the **domain** of finiteness is the **barrier cone** of $K$.

**Proposition.** The support function is **sublinear**: it is positively homogeneous,

$$
\sigma_K(\lambda u) = \lambda\,\sigma_K(u) \quad (\lambda\geq0),
$$

and subadditive,

$$
\sigma_K(u+v)\leq\sigma_K(u)+\sigma_K(v),
$$

and it is lower semicontinuous and convex as a function of $u$; it is the supremum of the linear functionals $\langle\cdot,x\rangle$ over $x\in K$.

*Proof.* Homogeneity is the linearity of the pairing in $\lambda\geq0$; subadditivity is $\langle u+v,x\rangle = \langle u,x\rangle+\langle v,x\rangle$ and the subadditivity of the supremum. The remaining assertions are that a supremum of linear functionals is convex, lower semicontinuous and sublinear, which is the second proposition of *Convex Functions and the Legendre Transform* applied to the family $\{\langle\cdot,x\rangle\}_{x\in K}$.

**Proposition (elementary properties).** The support function satisfies

$$
\sigma_{K+L} = \sigma_K+\sigma_L, \qquad \sigma_{\lambda K} = \lambda\sigma_K\ (\lambda\geq0), \qquad \sigma_{\operatorname{conv}(A)} = \sup_{a\in A}\langle\cdot,a\rangle ,
$$

and $K\subseteq L$ implies $\sigma_K\leq\sigma_L$.

*Proof.* The support function of the Minkowski sum is the supremum of $\langle u,x\rangle+\langle u,y\rangle$ over $x\in K$, $y\in L$, which is the sum of the two suprema; a positive multiple is scaled; the convex hull adds the points already dominated by the supremum of the linear functionals, so it does not change it; and the inclusion is monotonicity of the supremum.

### The Reconstruction Theorem

**Theorem (the support function determines the closed convex set).** For a nonempty closed convex $K$,

$$
K = \{x\in E : \langle u,x\rangle\leq\sigma_K(u) \ \text{for every } u\in E'\} ,
$$

and consequently $\sigma_K = \sigma_L$ for closed convex $K,L$ implies $K = L$.

*Proof.* The inclusion $\subseteq$ is the definition of $\sigma_K$. For the reverse, a point $x$ outside the closed convex set $K$ is separated from it by a continuous linear functional, which is a dual-pair version of the separation theorem of *Duality Theory*: there are $u$ and $\alpha$ with $\langle u,x\rangle > \alpha > \sup_K\langle u,\cdot\rangle = \sigma_K(u)$, so $x$ violates the inequality for that $u$.

The theorem is the statement that a closed convex set is the intersection of the closed half-spaces $\{\langle u,\cdot\rangle\leq\sigma_K(u)\}$ that contain it, and it shows that the support function is a complete invariant of a closed convex set.

## The Support Function as an Operator

### The Order Isomorphism

**Theorem.** The support function operator

$$
\Sigma : K\mapsto\sigma_K , \qquad \Sigma(K+L) = \Sigma(K)+\Sigma(L), \quad \Sigma(\lambda K) = \lambda\,\Sigma(K) ,
$$

is an order isomorphism from the nonempty closed convex subsets of $E$ onto the closed sublinear functions of the dual, the order being the inclusion on the sets and the pointwise order on the functions. It converts the Minkowski sum into the pointwise sum, its inverse is the reconstruction

$$
\Sigma^{-1}(\sigma) = \{x : \langle u,x\rangle\leq\sigma(u)\ \text{for all } u\} ,
$$

and it is **additive and positively homogeneous** in the sense displayed.

*Proof.* The map is order preserving and injective by the reconstruction theorem, and surjective because a closed sublinear function $\sigma$ has the set $K_\sigma$ on the right of the reconstruction formula as a nonempty closed convex set with $\sigma_{K_\sigma} = \sigma$, by the bipolar theorem of *Duality Theory*. Additivity and positive homogeneity are the elementary properties above, and the inverse is the reconstruction.

**Proposition (the operator is a lattice homomorphism for the join).** For nonempty closed convex $K$ and $L$,

$$
\sigma_{\operatorname{conv}(K\cup L)} = \max(\sigma_K,\sigma_L), \qquad \sigma_{K\cap L}\leq\min(\sigma_K,\sigma_L),
$$

with equality in the second only when $K\cap L$ already determines the smaller of the two supports; the first identity is exact.

*Proof.* The convex hull of the union has support function the supremum of the linear functionals over the union, which is the maximum of the two suprema; the intersection is contained in both sets, so its support is at most the minimum, and the reverse inequality fails in general because the intersection may be a proper subset with strictly smaller support.

**Proposition (the isometry with the Hausdorff metric).** For nonempty compact convex $K,L$,

$$
d_H(K,L) = \sup_{\lVert u\rVert\leq1}\bigl\lvert\sigma_K(u)-\sigma_L(u)\bigr\rvert ,
$$

so the support function operator is an isometry from the compact convex sets with the Hausdorff distance onto the sublinear functions with the uniform distance on the dual unit ball.

*Proof.* The Hausdorff distance is the smallest $\epsilon$ with $K\subseteq L+\epsilon B$ and $L\subseteq K+\epsilon B$ for the unit ball $B$, which by the additivity and positive homogeneity of $\Sigma$ is the smallest $\epsilon$ with $\sigma_K\leq\sigma_L+\epsilon\sigma_B$ and conversely; the support function of $B$ is the dual norm, so the condition is the uniform estimate $\lvert\sigma_K-\sigma_L\rvert\leq\epsilon$ on the unit ball. This is the isometry used in *Helly's Theorem and the Approximation of Convex Sets*.

### The Conjugacy with the Indicator

**Proposition.** Let $\delta_K$ be the indicator of a nonempty closed convex $K$, finite and zero on $K$ and $+\infty$ outside. Then the support function is the Legendre transform of the indicator,

$$
\sigma_K = \delta_K^{*} = \sup_{x}\bigl(\langle u,x\rangle-\delta_K(x)\bigr),
$$

and the biconjugacy theorem gives $\delta_K = \sigma_K^{*}$, which is the reconstruction theorem of the previous section in the language of *Convex Functions and the Legendre Transform*.

*Proof.* The two formulas are the definitions; the equality $\delta_K = \sigma_K^*$ is the Fenchel–Moreau theorem applied to the closed convex indicator.

## The Polar and the Gauge

### The Polar Set and the Bipolar Theorem

**Definition.** For a subset $A\subseteq E$ the **polar** is

$$
A^{\circ} = \{u\in E' : \langle u,x\rangle\leq1 \ \text{for every } x\in A\} ,
$$

a closed convex set containing the origin and, if $A$ contains the origin, a closed convex set with the origin in its interior whenever $A$ is bounded.

**Theorem (the bipolar theorem).** For every $A\subseteq E$,

$$
A^{\circ\circ} = \overline{\operatorname{conv}}(A\cup\{0\}) ,
$$

so that for a closed convex set containing the origin the polar is an involution, $K^{\circ\circ} = K$.

*Proof.* The polar is defined by the closed half-space conditions $\langle u,\cdot\rangle\leq1$ on $A$, so $A^{\circ}$ is the intersection of the closed half-spaces, and its polar is the smallest closed convex set containing $A$ and the origin, which is the stated set; this is the bipolar theorem of *Duality Theory*, and the involution is the case in which $A$ is closed convex and contains the origin.

### The Gauge and the Support of the Polar

**Definition.** The **gauge** of a convex set $K$ containing the origin in its interior is

$$
\rho_K(x) = \inf\{\lambda>0 : x\in\lambda K\} ,
$$

a sublinear function, and the **polar** $K^{\circ}$ is the set on which the functionals are at most one.

**Proposition (the support function of the polar is the gauge).** For a closed convex $K$ containing the origin in its interior,

$$
\sigma_{K^{\circ}} = \rho_K \quad\text{on } E, \qquad \rho_K(x) = \sup\{\langle u,x\rangle : u\in K^{\circ}\} ,
$$

and, symmetrically, the polar of the gauge ball recovers the polar set.

*Proof.* By the definition of the polar, $\sigma_{K^{\circ}}(x) = \sup\{\langle u,x\rangle : u\in K^{\circ}\}$, and the functional $u$ ranges over the polar, so the supremum is the gauge of $K$ by the bipolar theorem: $\rho_K$ is the smallest sublinear function whose unit ball is $K$, and its conjugate is the indicator of $K^{\circ}$.

## Worked Cases

### The Unit Ball and its Polar

For $K = B$ the closed unit ball of a normed space, the support function is the dual norm, $\sigma_B = \lVert\cdot\rVert_{E'}$, because the supremum of the pairing over the unit ball is the norm of the functional; and the polar of the unit ball is the unit ball of the dual, $B^{\circ} = B_{E'}$, so the polarity exchanges the unit balls and the gauge is the given norm. For $E = E' = \mathbb{R}^n$ with the Euclidean pairing the polar of the Euclidean ball is itself, and the polarity is an inversion in the sphere.

### A Polytope and its Faces

For a finite-dimensional polytope $K = \operatorname{conv}(p_1,\dots,p_N)$ the support function is the maximum of finitely many linear functions,

$$
\sigma_K(u) = \max_{i}\langle u,p_i\rangle ,
$$

a **piecewise linear convex** positively homogeneous function; its domains of linearity are the normal cones of the faces of $K$, and the exposed faces are the maximising sets of the linear functionals, which is the facial structure of *Convex Analysis*. The polar $K^{\circ}$ is the intersection of the half-spaces $\langle u,p_i\rangle\leq1$, the polyhedron dual to $K$, and the bipolar theorem is the self-duality of the polyhedral cones of the dimensions in which the polarisation is defined.

### A Cone and the Dual Cone

For a closed convex cone $C$ the support function is the indicator of the **dual cone**,

$$
\sigma_C(u) = \begin{cases} 0, & u\in C^{*},\\ +\infty, & u\notin C^{*}, \end{cases}
$$

because the pairing is unbounded above on $C$ unless $u$ is nonpositive on it; the polar of the cone is $C^{\circ} = -C^{*}$, and the bipolar theorem for cones is the double dual statement of *Cones, Extremal Rays and the Choquet Theory* and *Duality Theory*. The support operator therefore sends the cones to the indicators of the dual cones, and the polar exchanges a cone with the negative of its dual.

## Summary

The **support function** $\sigma_K(u) = \sup_{x\in K}\langle u,x\rangle$ is sublinear, convex and lower semicontinuous, it is the supremum of the linear functionals over the set, it is additive under the Minkowski sum, positively homogeneous, monotone under inclusion, and the **reconstruction theorem** recovers a closed convex set from it as the intersection of the half-spaces it defines. The **support function operator** $\Sigma : K\mapsto\sigma_K$ is an order isomorphism from the closed convex sets onto the closed sublinear functions, additive and positively homogeneous, a lattice homomorphism for the convex hull of a union, and an isometry from the Hausdorff metric to the uniform metric; it is the **Legendre transform of the indicator**, $\sigma_K = \delta_K^*$. The **polar** $A^{\circ} = \{u : \langle u,x\rangle\leq1 \text{ on } A\}$ satisfies the **bipolar theorem** $A^{\circ\circ} = \overline{\operatorname{conv}}(A\cup\{0\})$, so it is an involution on the closed convex sets containing the origin; the support function of the polar is the **gauge** of the set, and the polarity exchanges the unit balls of a normed space with those of its dual. The convex geometry is *Convex Sets and the Convex Hull* and *Helly's Theorem and the Approximation of Convex Sets*; the duality and the polar are *Duality Theory*; the conjugacy is *Convex Functions and the Legendre Transform*; the cones are *Cones, Extremal Rays and the Choquet Theory*; and the polyhedral case is *Convex Analysis*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\sigma_K(u) = \sup_{x\in K}\langle u,x\rangle$ | Support function of the convex set $K$ |
| $\Sigma : K\mapsto\sigma_K$ | Support function operator |
| $\sigma_{K+L} = \sigma_K+\sigma_L$ | Additivity under the Minkowski sum |
| $\sigma_{\operatorname{conv}(K\cup L)} = \max(\sigma_K,\sigma_L)$ | The operator is a join homomorphism |
| $\sigma_K = \delta_K^{*}$ | The support function is the conjugate of the indicator |
| $A^{\circ} = \{u : \langle u,x\rangle\leq1 \text{ on } A\}$ | Polar set |
| $A^{\circ\circ} = \overline{\operatorname{conv}}(A\cup\{0\})$ | Bipolar theorem |
| $\rho_K(x) = \inf\{\lambda>0 : x\in\lambda K\}$ | Gauge, the support function of the polar |
| $d_H(K,L) = \lVert\sigma_K-\sigma_L\rVert_\infty$ | The operator is an isometry |

## Further Reading

- Hermann Minkowski, *Geometrie der Zahlen* (Teubner, 1896), for the support function and the polar of a convex body.
- Wilhelm Fenchel, "On conjugate convex functions", *Canadian Journal of Mathematics* **1** (1949), 73–77, for the conjugacy with the indicator and the bipolar theorem.
- R. Tyrrell Rockafellar, *Convex Analysis* (Princeton University Press, 1970), for the support functions, the gauges and the polyhedral case.
- Gustave Choquet, *Lectures on Analysis, vol. II: Representation Theory* (Benjamin, 1969), for the support function and the extreme structure of the convex sets.
- Branko Grünbaum, *Convex Polytopes* (Interscience, 1967), for the polar polyhedra and the faces of a polytope.
- Peter M. Gruber, *Convex and Discrete Geometry*, Grundlehren der mathematischen Wissenschaften 336 (Springer, 2007), for the support function as an isometry and the approximation of the convex sets.
