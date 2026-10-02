
# __Convex Functions and the Legendre Transform__

## Introduction

A real-valued function is **convex** when its epigraph is a convex set, equivalently when it lies below the chords of its graph, and the convex functions are exactly the functions that a family of affine functions can bound from below. This is what makes them the analytic objects of a **dual** description: a convex function is its own set of supporting affine minorants, and the transform that records those minorants is the **Legendre transform**, or **conjugate**,

$$
f^*(y) = \sup_{x}\bigl(\langle x,y\rangle - f(x)\bigr).
$$

The transform is order-reversing and, on the closed convex functions, an involution; it is therefore an anti-automorphism of a lattice, and the Fenchel–Young inequality that defines it is an **adjunction** in the sense of *Order Theory and Lattices*. Its local form is the **subdifferential**, the set of slopes of the supporting affine functions at a point, and the transform and the subdifferential are inverse to each other as set-valued maps.

The article is written on a real vector space $E$ paired with a space $E'$ of linear functionals, most often a locally convex space with its dual, in the sense of *Duality Theory* and *Locally Convex Spaces*. The calculus of convex functions in $\mathbb{R}^n$ — the directional derivative, the continuity and Lipschitz behaviour on the domain, the Fenchel duality theorem, the Moreau envelope and the proximal map, the Karush–Kuhn–Tucker conditions — is developed in *Convex Analysis*, in the *Foundations of Analysis* category of this Part, and it is cited here rather than restated. What this article adds is the general setting, the reading of the transform as an order-reversing involution and as an adjunction, its relation to the subdifferential, and the classical Legendre form for a differentiable strictly convex function, whose local computation uses the derivative of this Part.

## Convex Functions and their Epigraphs

### Definition and Elementary Properties

**Definition.** Let $f : E\to(-\infty,+\infty]$. The **epigraph** is

$$
\operatorname{epi} f = \{(x,t)\in E\times\mathbb{R} : f(x)\leq t\},
$$

and $f$ is **convex** when $\operatorname{epi} f$ is a convex subset of $E\times\mathbb{R}$. It is **proper** when it is not identically $+\infty$ and never takes the value $-\infty$, **closed** when $\operatorname{epi} f$ is closed, and **lower semicontinuous** when $f(x)\leq\liminf f(x_i)$ along every convergent net $x_i\to x$; for a proper function the last two conditions are the same.

**Proposition.** A proper function $f$ is convex if and only if

$$
f\bigl((1-t)x + t y\bigr) \leq (1-t)\,f(x) + t\,f(y)
$$

for all $x,y$ and all $t\in[0,1]$, with the convention that the right side is $+\infty$ when a value is infinite. It is convex if and only if it is the pointwise supremum of the affine functions that it dominates.

*Proof.* The first equivalence is the definition of convexity of the epigraph written out in the two coordinates. For the second, an affine minorant has a convex epigraph containing $\operatorname{epi} f$, so it is a convex function below $f$, and the supremum of convex functions is convex; conversely, if $f$ is convex and closed then a point $(x,t)$ outside $\operatorname{epi} f$ is separated from it by a continuous functional, which produces an affine minorant excluding $(x,t)$, so the supremum recovers $f$.

**Proposition (the lattice).** The pointwise supremum of any family of convex functions is convex; the sum of two proper convex functions is convex; and the composition $f\circ A$ of a convex $f$ with a linear map $A$ is convex. The proper closed convex functions form a complete lattice under the pointwise order, in which the supremum is the pointwise supremum and the infimum is its closed convex hull.

*Proof.* The epigraph of a supremum is the intersection of the epigraphs, and the intersection of convex sets is convex; the sum has epigraph the Minkowski sum of the epigraphs, convex as a sum of convex sets; composition pulls the epigraph back along $A\times\mathrm{id}$. The lattice statement is the completeness of the intersection of closed convex sets.

### The Convex Hull of a Function

The **convex hull** $\operatorname{conv} f$ of a function is the greatest convex function below $f$, and $\operatorname{cl}\operatorname{conv} f$ is the greatest closed convex function below it; the two are the closed convex hull of the epigraph read back as a function. The operator $f\mapsto\operatorname{cl}\operatorname{conv} f$ is a closure operator on the lattice of functions, monotone, increasing and idempotent, and its fixed points are the closed convex functions. This is the function-level form of the closure operator of *Convex Sets and the Convex Hull*.

## The Legendre Transform

### Definition and the Fenchel–Young Inequality

**Definition.** The **Legendre transform**, or **conjugate**, of $f : E\to(-\infty,+\infty]$ is the function $f^* : E'\to(-\infty,+\infty]$ given by

$$
f^*(y) = \sup_{x\in E}\bigl(\langle x,y\rangle - f(x)\bigr),
$$

where $\langle x,y\rangle = y(x)$ is the duality pairing. It is a supremum of affine functions of $y$, so it is convex and lower semicontinuous, and it is proper exactly when $f$ has an affine minorant.

**Proposition (Fenchel–Young).** For all $x$ and $y$,

$$
\langle x,y\rangle \leq f(x) + f^*(y),
$$

with equality if and only if $y$ is a supporting slope of $f$ at $x$, that is, if and only if $f(x') \geq f(x) + \langle x'-x,y\rangle$ for every $x'$.

*Proof.* The inequality is the definition of the supremum: $f^*(y)\geq\langle x,y\rangle - f(x)$ for every $x$. Equality says the supremum is attained at $x$, which is exactly the inequality $f(x')\geq\langle x',y\rangle - f^*(y) = f(x)+\langle x'-x,y\rangle$ for every $x'$.

**Proposition (the adjunction, and the transform is order-reversing).** For functions $f$ and $g$,

$$
f \leq g \implies f^* \geq g^*,
$$

and more sharply, for every $g$ on $E'$ and every $f$ on $E$,

$$
f(x) + g(y) \geq \langle x,y\rangle \ \text{ for all } x,y \iff f \geq (-g)^* \iff g \geq (-f)^* .
$$

*Proof.* The first assertion is that the supremum defining $f^*$ is over a larger family when $f$ is smaller. The second is Fenchel–Young written as an adjunction: the condition on the left is that $-f(y) \leq \langle x,y\rangle - \dots$; unwinding the two suprema gives $g(y)\geq -f^*(y)$ and $f(x)\geq -g^*(x)$.

The pair of inequalities is a **Galois connection** between the lattice of functions on $E$ and the lattice of functions on $E'$ with the order reversed, in the sense of *Order Theory and Lattices*: the transform is the left adjoint of the transform with $f$ replaced by $-f$.

### The Biconjugate and the Involution

**Theorem (Fenchel–Moreau).** For every function $f$,

$$
f^{* *} = \operatorname{cl}\operatorname{conv} f .
$$

Consequently $f^{**} = f$ if and only if $f$ is closed and convex, and the Legendre transform is an order-reversing involution of the set of closed convex functions, an anti-automorphism of its lattice.

*Proof.* By definition $f^{**}(x) = \sup_y(\langle x,y\rangle - f^*(y))$, which is the supremum of the affine minorants $x\mapsto\langle x,y\rangle - f^*(y)$ of $f$ — the value $f^*(y)$ finite ensures the minorant — so it is the greatest closed convex function below $f$, namely $\operatorname{cl}\operatorname{conv} f$. Applying the identity twice to a closed convex $f$ returns $f$; and the transform reverses order, so it reverses the lattice operations.

**Corollary (the transform exchanges the lattice operations).** On closed convex functions the transform turns the pointwise supremum into the **infimal convolution**

$$
(f^* \oplus g^*)(y) = \inf_{y_1+y_2=y}\bigl(f^*(y_1) + g^*(y_2)\bigr),
$$

and the infimal convolution into the pointwise sum: $(f+g)^* = f^* \oplus g^*$ and $(f\oplus g)^* = f^* + g^*$, where the closure is taken as needed.

*Proof.* A functional $y$ supports $f+g$ at $x$ exactly when it splits as $y_1+y_2$ with $f(x_1)+g(x_2)$ minimal; reading the equality case of Fenchel–Young gives the two identities.

### The Subdifferential

**Definition.** The **subdifferential** of $f$ at $x$ is the set of supporting slopes,

$$
\partial f(x) = \{y\in E' : f(x')\geq f(x) + \langle x'-x,y\rangle \ \text{for all } x'\},
$$

empty when $f(x) = +\infty$, and it is a closed convex subset of $E'$. A point $x$ **minimises** $f$ when $0\in\partial f(x)$.

**Proposition (the transform and the subdifferential are inverse).** For all $x$ and $y$,

$$
y\in\partial f(x) \iff x\in\partial f^*(y) \iff f(x) + f^*(y) = \langle x,y\rangle .
$$

Hence $\partial f^* = (\partial f)^{-1}$ as set-valued maps, and the subdifferential of a closed convex function is a **maximal monotone** operator: $(y_2 - y_1)(x_2 - x_1)\geq0$ for $y_i\in\partial f(x_i)$, and no proper enlargement of its graph is monotone.

*Proof.* The three conditions are the equality case of Fenchel–Young read at $(x,y)$, at $(y,x)$ for the conjugate, and again at $(x,y)$; the equality of the two extreme forms identifies the two descriptions. Monotonicity is the sum of the two inequalities for $(x_1,y_1)$ and $(x_2,y_2)$; maximality is the standard argument of *Convex Analysis*, where the finite-dimensional case is proved.

### The Classical Legendre Form

Suppose $f$ is proper, strictly convex, differentiable and **superlinear**, $f(x)/\lVert x\rVert\to+\infty$. Then the gradient $\nabla f : E\to E'$ is injective, its image is the domain of $f^*$, and

$$
f^*(y) = \langle (\nabla f)^{-1}(y),\, y\rangle - f\bigl((\nabla f)^{-1}(y)\bigr),
$$

the classical formula of Legendre, in which the transform is computed by solving $y = \nabla f(x)$ for $x$ and substituting. At a corresponding pair $y = \nabla f(x)$ the Hessian of the transform is the inverse of the Hessian of $f$,

$$
D^2 f^*(y) = \bigl(D^2 f(x)\bigr)^{-1},
$$

when the second derivative exists and is invertible, by differentiating the identity $\nabla f^*\circ\nabla f = \mathrm{id}$. The transform is then an involution on the smooth strictly convex functions, and the subdifferential is the inverse of a bijection, so the set-valued theory reduces to the differentiable one.

## Worked Cases

### The Norm

For $f(x) = \tfrac12\lVert x\rVert^2$ on a real Hilbert space, identified with its dual by the Riesz representation theorem of *Normed and Banach Spaces*, the transform is $f^*(y) = \tfrac12\lVert y\rVert^2$: the function is its own conjugate, and the subdifferential is $\partial f(x) = \{x\}$, so the transform is the identity. For $f = \lVert\cdot\rVert$ the conjugate is the indicator of the dual unit ball, $\delta_{\{\lVert y\rVert\leq1\}}$, and the subdifferential of the norm at $x$ is the set of unit functionals attaining their norm at $x$.

### The Indicator and the Support Function

For the indicator $f = \delta_C$ of a nonempty convex set $C$, finite and zero on $C$ and $+\infty$ outside, the conjugate is the **support function** $f^* = \sigma_C$, $y\mapsto\sup_{x\in C}\langle x,y\rangle$, which is convex, closed, positively homogeneous and sublinear. The transform of $\sigma_C$ is $\delta_{\overline{\operatorname{conv}} C}$, so the biconjugacy theorem reconstructs a closed convex set from its support function; this duality of a convex set and its support function is the subject of *The Support Function Operator* in this category.

### The Entropy

On $\mathbb{R}$ let $f(x) = e^x$. It is strictly convex and superlinear, $\nabla f = e^x$, and the classical formula gives $f^*(y) = y\log y - y$ for $y>0$, with $f^*(0) = 0$ by continuity and $f^*(y) = +\infty$ for $y<0$. The domain of the conjugate is the positive half-line, the image of the exponential, and the pair exhibits the general fact that the conjugate is determined on the image of the gradient and is $+\infty$ outside it.

## Summary

A function is convex exactly when its epigraph is convex, equivalently when it lies below its chords, equivalently when it is the supremum of the affine functions below it; the greatest closed convex function below $f$ is a closure operator on the lattice of functions. The **Legendre transform** $f^*(y) = \sup_x(\langle x,y\rangle - f(x))$ is convex and closed, it reverses order, and the Fenchel–Young inequality $f(x)+f^*(y)\geq\langle x,y\rangle$ is an adjunction between the lattice of functions on $E$ and the lattice on $E'$ with the order reversed. The **Fenchel–Moreau theorem** states $f^{**} = \operatorname{cl}\operatorname{conv} f$, so the transform is an order-reversing involution of the closed convex functions and exchanges the pointwise sum with the infimal convolution. The **subdifferential** $\partial f(x)$, the set of supporting slopes, is characterised by equality in Fenchel–Young, it is the inverse of $\partial f^*$ as a set-valued map, it contains the origin exactly at the minimisers, and it is a maximal monotone operator. In the smooth strictly convex superlinear case the transform is Legendre's classical one, computed by inverting the gradient, and the Hessian of the transform is the inverse of the Hessian of the function. The finite-dimensional calculus — the directional derivative, the continuity on the domain, the duality theorem, the Moreau envelope, the Karush–Kuhn–Tucker conditions — is *Convex Analysis*; the adjunction language is *Order Theory and Lattices*; the pairing is *Duality Theory*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $f : E\to(-\infty,+\infty]$ | A proper extended-real function |
| $\operatorname{epi} f$ | Epigraph, convex exactly when $f$ is convex |
| $\operatorname{conv} f$, $\operatorname{cl}\operatorname{conv} f$ | Greatest convex, and greatest closed convex, minorant |
| $f^*(y) = \sup_x(\langle x,y\rangle - f(x))$ | Legendre transform, or conjugate |
| $\langle x,y\rangle$ | Duality pairing between $E$ and $E'$ |
| $f(x)+f^*(y)\geq\langle x,y\rangle$ | Fenchel–Young inequality |
| $f^{**} = \operatorname{cl}\operatorname{conv} f$ | Biconjugacy (Fenchel–Moreau) |
| $f^* \oplus g^*$ | Infimal convolution, the dual of the pointwise sum |
| $\partial f(x)$ | Subdifferential, the set of supporting slopes |
| $\partial f^* = (\partial f)^{-1}$ | The transform inverts the subdifferential |
| $\nabla f$, $D^2 f$ | Gradient and Hessian in the smooth case |
| $\delta_C$, $\sigma_C$ | Indicator and support function of a convex set $C$ |

## Further Reading

- Werner Fenchel, *Convex Cones, Sets and Functions*, Lecture Notes (Princeton University Press, 1953), for the conjugate and the biconjugacy theorem in their general form.
- Jean-Jacques Moreau, "Fonctions convexes duales et points proximaux dans un espace hilbertien", *Comptes Rendus de l'Académie des Sciences* **255** (1962), 2897–2899, for the biconjugacy and the proximal theory.
- R. Tyrrell Rockafellar, *Convex Analysis* (Princeton University Press, 1970), for the finite-dimensional calculus, subdifferentials, conjugates and duality.
- R. Tyrrell Rockafellar, "Monotone operators and the proximal point algorithm", *SIAM Journal on Control and Optimization* **14** (1976), 877–898, for the monotonicity of the subdifferential.
- Ivar Ekeland and Roger Temam, *Convex Analysis and Variational Problems* (North-Holland, 1976), for the transform on a locally convex space and the duality theory.
- Adrien-Marie Legendre, *Mémoires de l'Académie des Sciences* (1787), for the classical transform of the smooth strictly convex case.
