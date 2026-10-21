# __Reduced Biquaternion Analysis__

## Introduction

Reduced biquaternion analysis is the study of functions of a reduced biquaternion variable through the operations of the algebra, on the Euclidean space of *The Euclidean Topology of the Reduced Biquaternion Algebra*. The article fixes the metric setting, defines limits and continuity, states the **problem of differentiability** — the difference quotient needs a division by the increment, and the increment may be a zero divisor — and shows how the algebra resolves it: because the algebra is the direct product of two copies of $\mathbb{C}$, a function that is differentiable in the reduced sense decouples into **two complex analyses**, one in each idempotent coordinate. The class of functions so obtained, the pairs of holomorphic functions of the two coordinates, is the reduced analogue of the holomorphic functions, and it is the smallest possible: the algebra is **commutative**, it **has zero divisors**, the Euclidean norm is not multiplicative, and it is **not a division algebra**, so no richer theory of a single complex variable over the whole four-dimensional space is available. The functions themselves are the subject of *Reduced Biquaternion Regular Functions*.

**Conventions.** The basis is $1,i,j,ij$ with $i^{2}=-1$, $j^{2}=+1$, $ji=ij$; the element is $\breve Q=Q_++jQ_-$ with $Q_+=q_++iq'_+$, $Q_-=q_-+iq'_-$; the idempotent coordinates are $Q_{++}=Q_++Q_-$, $Q_{--}=Q_+-Q_-$, and $\breve Q=Q_{++}\Pi_++Q_{--}\Pi_-$ with $\Pi_{\pm}=\tfrac12(1\pm j)$. The Euclidean metric is $d(\breve Q_{1},\breve Q_{2})=\sqrt{K(\breve Q_{1}-\breve Q_{2})}$, $K=\lvert Q_+\rvert^{2}+\lvert Q_-\rvert^{2}$. The element glyph is $\breve Q$, with the breve and without a tilde; a general function is written $\Phi$ or $f$.

**Boundaries.** The metric and the topology are *Topology in the Space of Reduced Biquaternions*, *The Euclidean Topology of the Reduced Biquaternion Algebra* and *Topology and Metric for Each of the Operations*; the two coordinate projections are *Ideals and Peirce Decomposition of the Algebra of the Reduced Biquaternions*; the differentiable functions are *Reduced Biquaternion Regular Functions*; the integral theory is *Reduced Biquaternion Integration*; the operator theory is *Fueter Theory for Reduced Biquaternions*. The biquaternion counterpart is *Biquaternion Analysis*.

## The Metric Structure

**The analysis is done in the metric space of the Euclidean norm, on an open set of the space.**

**Definition.** An **open set** $\Omega$ is a union of open balls of the Euclidean metric; a **domain** is a non-empty connected open set. A function is studied on a domain $\Omega\subset\mathbb{B}_{\mathrm{r}}$, with the induced metric $d$ and the induced topology.

**Theorem (the setting).** On a domain the metric is complete on the closed balls, the balls are convex, and every element of the domain has a ball neighbourhood contained in the domain; the four products are continuous, so all the algebra operations are defined and continuous on the domain and its functions.

*Proof.* The space is $\mathbb{R}^{4}$ under the coordinate isometry, so the balls are the standard Euclidean balls, which are convex and complete; the open-set property is the definition; the continuity of the products is *Topology in the Space of Reduced Biquaternions*.

## Limits and Continuity

**Definition.** For a function $f:\Omega\to\mathbb{B}_{\mathrm{r}}$, a point $\breve Q_{0}\in\Omega$ and an element $L$, the **limit** is $f(\breve Q)\to L$ as $\breve Q\to \breve Q_{0}$ when for every $\varepsilon>0$ there is $\delta>0$ with $\lVert f(\breve Q)-L\rVert<\varepsilon$ whenever $0<\lVert \breve Q-\breve Q_{0}\rVert<\delta$; the function is **continuous** at $\breve Q_{0}$ when $f(\breve Q)\to f(\breve Q_{0})$.

**Theorem (continuity is coordinatewise).** A function $f$ is continuous at $\breve Q_{0}$ if and only if its two idempotent-coordinate functions
$$
f_{1}=\lambda_+\circ f,\qquad f_{2}=\lambda_-\circ f
$$
are continuous at $\breve Q_{0}$ as complex-valued functions of $\breve Q$. The two coordinate projections $\lambda_+,\lambda_-$ are continuous algebra homomorphisms.

*Proof.* The homeomorphism $\breve Q\mapsto(Q_{++},Q_{--})$ of *The Euclidean Topology of the Reduced Biquaternion Algebra* identifies the metric space with $\mathbb{C}\times\mathbb{C}$ with the product of the Euclidean metrics up to a constant; convergence in the product is convergence of the two coordinates; and the coordinate projections are the characters, which are ring homomorphisms continuous for the topology.

**Corollary (the algebra of continuous functions).** The continuous functions form a commutative algebra over $\mathbb{R}$ under the pointwise operations, closed under the three conjugations; the subalgebra of functions depending only on $Q_{++}$, or only on $Q_{--}$, is a copy of the continuous complex functions of one complex variable.

*Proof.* Pointwise sums and products of continuous functions are continuous, and the conjugations are continuous isometries; a function of $Q_{++}$ alone is the composition of the continuous $\breve Q\mapsto Q_{++}$ with a continuous complex function.

## The Problem of Differentiability

**The difference quotient needs a division by the increment, and the increment may be a zero divisor.**

**Definition.** The **difference quotient** of $f$ at $\breve Q$ with increment $\breve Q_{H}$ is
$$
\frac{f(\breve Q+\breve Q_{H})-f(\breve Q)}{\breve Q_{H}},
$$
defined when $\breve Q_{H}$ is invertible. The function is **differentiable** at $\breve Q$ when the quotient tends to a limit $f'(\breve Q)\in\mathbb{B}_{\mathrm{r}}$ as $\breve Q_{H}\to0$ through the invertible increments.

**Theorem (the obstacle).** The increments range over the unit group, which is open and dense but not all of the space; the increments that are excluded are the zero divisors, and the division by them is impossible. The quotient is therefore defined on a dense subset of the increments and not on all of them.

*Proof.* The invertible increments are the units of *The Group of Units of the Algebra of the Reduced Biquaternions*, whose complement is the zero-divisor set of *Zero Divisors of the Algebra of the Reduced Biquaternions*, closed with empty interior; an increment in the complement, being without inverse, cannot divide.

**Theorem (the polynomials are differentiable).** Every polynomial in $\breve Q$ with reduced biquaternion coefficients is differentiable at every point, with derivative the formal derivative: if $P(X)=\sum_{n}c_{n}X^{n}$ then
$$
\frac{P(\breve Q+\breve Q_{H})-P(\breve Q)}{\breve Q_{H}}=\sum_{n}c_{n}\sum_{k=0}^{n-1}(\breve Q+\breve Q_{H})^{n-1-k}\breve Q^{k}\longrightarrow P'(\breve Q)
$$
as $\breve Q_{H}\to0$, the inner sum being a polynomial in $\breve Q_{H}$.

*Proof.* Because the algebra is associative, $(\breve Q+\breve Q_{H})^{n}-\breve Q^{n}=\breve Q_{H}\sum_{k=0}^{n-1}(\breve Q+\breve Q_{H})^{n-1-k}\breve Q^{k}$, so the difference factors on the left or on the right by $\breve Q_{H}$; the algebra is commutative, so the two factorisations coincide; when $\breve Q_{H}$ is invertible the quotient is the inner sum, a polynomial in $\breve Q_{H}$, whose limit as $\breve Q_{H}\to0$ is $\sum_{n}nc_{n}\breve Q^{n-1}=P'(\breve Q)$, independent of the direction of approach.

**Corollary (a non-differentiable function).** The conjugation $\breve Q\mapsto\bar{\breve Q}$ is continuous but not differentiable at the origin: the quotient $\bar{\breve Q_{H}}/\breve Q_{H}$ equals $+1$ for real increments $\breve Q_{H}$ and $-1$ for increments $\breve Q_{H}=ijs$ on the fourth axis, so the limit depends on the direction and does not exist.

*Proof.* $\bar{\breve Q_{H}}=\breve Q_{H}$ for real $\breve Q_{H}$, giving quotient $1$; $\overline{ijs}=-ijs$ for the element $ijs$ on the fourth axis, giving quotient $-1$; the two directions give different limits, so no derivative exists.

## The Reduction to Two Complex Analyses

**A differentiable function of the reduced variable decouples into two holomorphic functions, one in each idempotent coordinate.**

**Theorem (the reduction).** Let $\Omega$ be a domain and $f:\Omega\to\mathbb{B}_{\mathrm{r}}$ differentiable in the sense above at every point, with the derivative continuous. Then, writing
$$
f(\breve Q)=g_{1}(\breve Q)\,\Pi_++g_{2}(\breve Q)\,\Pi_-,
$$
the function $g_{1}$ depends only on $Q_{++}$ and the function $g_{2}$ only on $Q_{--}$, and each is holomorphic: there are holomorphic functions $G_{1}$ and $G_{2}$ of one complex variable with
$$
f(\breve Q)=G_{1}(Q_{++})\,\Pi_++G_{2}(Q_{--})\,\Pi_-,\qquad f'(\breve Q)=G_{1}'(Q_{++})\,\Pi_++G_{2}'(Q_{--})\,\Pi_-.
$$

*Proof.* In the idempotent basis the algebra is the direct product and the multiplication is componentwise, so differentiating is componentwise: $f'(\breve Q)=g_{1}'(\breve Q)\Pi_++g_{2}'(\breve Q)\Pi_-$, and the componentwise derivative of $g_{1}$ at $\breve Q$ along increments $\breve Q_{H}=m\Pi_++n\Pi_-$ is the derivative in the coordinate $Q_{++}$ alone, since the product $\breve Q^{n}$ depends on $Q_{++}$ and $Q_{--}$ separately; the limit defining $g_{1}'$ uses only $m$, so $g_{1}$ has no dependence on $Q_{--}$, and likewise $g_{2}$ has none on $Q_{++}$. Each is then a complex function with a complex derivative, that is holomorphic, and the derivative rule is the chain rule in each coordinate.

**Corollary (the system decouples).** The reduced Cauchy–Riemann system is the pair of complex equations
$$
\frac{\partial g_{1}}{\partial\bar Q_{++}}=0,\qquad \frac{\partial g_{2}}{\partial\bar Q_{--}}=0,
$$
so the theory of differentiable reduced biquaternion functions is the product of two copies of the theory of holomorphic functions of one complex variable. There is no single complex analysis over the four-dimensional algebra, because the algebra is **not a division algebra**.

*Proof.* A complex function of one variable is holomorphic exactly when it satisfies the complex Cauchy–Riemann equation, that is when it is annihilated by the Wirtinger derivative in the conjugate coordinate; the system is the pair of the two coordinates, and the two have no coupling, the algebra being a direct product.

## The Differential Operators

**The Wirtinger derivatives of the two coordinates give the differential operators of the theory.**

**Definition.** On the four real coordinates, or on the complex coordinates $Q_+,Q_-$, define the **Wirtinger derivatives**
$$
\partial/\partial Q_{++}=\tfrac12\bigl(\partial/\partial Q_++\partial/\partial Q_-\bigr),\quad
\partial/\partial\bar Q_{++}=\tfrac12\bigl(\partial/\partial\bar Q_++\partial/\partial\bar Q_-\bigr),\quad
\partial/\partial Q_{--}=\tfrac12\bigl(\partial/\partial Q_+-\partial/\partial Q_-\bigr),\quad
\partial/\partial\bar Q_{--}=\tfrac12\bigl(\partial/\partial\bar Q_+-\partial/\partial\bar Q_-\bigr).
$$

**Theorem (the Laplacian).** The Euclidean Laplacian in the four real coordinates is
$$
\Delta=\partial^2/\partial q_+^2+\partial^2/\partial q'^2_++\partial^2/\partial q_-^2+\partial^2/\partial q'^2_-
=4\bigl(\partial^2/\partial Q_+\partial\bar Q_++\partial^2/\partial Q_-\partial\bar Q_-\bigr)
=8\bigl(\partial^2/\partial Q_{++}\partial\bar Q_{++}+\partial^2/\partial Q_{--}\partial\bar Q_{--}\bigr).
$$
As a check, $\Delta K=8$ and $\Delta Q_{++}=\Delta Q_{--}=0$.

*Proof.* For a complex variable $Q_+=q_++iq'_+$ one has $\partial/\partial q_+=\partial/\partial Q_++\partial/\partial\bar Q_+$ and $\partial/\partial q'_+=i(\partial/\partial Q_+-\partial/\partial\bar Q_+)$, so $\partial^2/\partial q_+^2+\partial^2/\partial q'^2_+=4\partial^2/\partial Q_+\partial\bar Q_+$, and likewise for $Q_-$; this gives the middle expression. The change of variables $Q_{++}=Q_++Q_-$, $Q_{--}=Q_+-Q_-$ gives $\partial/\partial Q_+=\partial/\partial Q_{++}+\partial/\partial Q_{--}$ and $\partial/\partial Q_-=\partial/\partial Q_{++}-\partial/\partial Q_{--}$, whence $\partial^2/\partial Q_+\partial\bar Q_++\partial^2/\partial Q_-\partial\bar Q_-=2(\partial^2/\partial Q_{++}\partial\bar Q_{++}+\partial^2/\partial Q_{--}\partial\bar Q_{--})$, the last expression. For the check: $K=\tfrac12(\lvert Q_{++}\rvert^{2}+\lvert Q_{--}\rvert^{2})$ and $\partial^2/\partial Q_{++}\partial\bar Q_{++}\lvert Q_{++}\rvert^{2}=1$, so $8(\tfrac12+\tfrac12)=8$; and the holomorphic coordinates are annihilated by the conjugate derivations.

**Corollary (the differentiable functions are harmonic).** A differentiable reduced biquaternion function $f(\breve Q)=G_{1}(Q_{++})\Pi_++G_{2}(Q_{--})\Pi_-$ satisfies
$$
\Delta f=0,
$$
each component being annihilated by the conjugate derivative of its own coordinate, $\partial/\partial\bar Q_{++}G_{1}=0$ and $\partial/\partial\bar Q_{--}G_{2}=0$.

*Proof.* A holomorphic function of one complex variable has harmonic real and imaginary parts, the Cauchy–Riemann equations giving $\partial^2/\partial q_+^2+\partial^2/\partial q'^2_+$ applied to each part equal to zero; the components are decoupled and the total Laplacian is the sum of the two-dimensional Laplacians of the two components, up to the factor of the change of variables.

## Functions on a Subspace

**On a subalgebra or a subspace the analysis reduces to a known one.**

**Theorem (the reductions).** The restrictions of the reduced biquaternion analysis to the four remarkable subspaces are the analyses of the corresponding algebras:

- on the complex line $\mathbb{R}\{1,i\}$ the analysis is the complex analysis of one variable;
- on the split line $\mathbb{R}\{1,j\}$ the analysis is the split-complex analysis of one variable;
- on the plane $\mathbb{R}\{1,ij\}$ the analysis is again the complex analysis, the element $ij$ squaring to $-1$;
- on a subspace containing the two idempotent lines the analysis is the product of the two complex analyses.

*Proof.* Each subspace is a subalgebra or a linear subspace closed under the relevant product, carrying the restriction of the norm; the two-dimensional subalgebras are the complex numbers and the split-complex numbers of the corpus, and the fourth case is the idempotent splitting of §*The Reduction to Two Complex Analyses*.

## The Relation to Fueter and Clifford Analysis

**The reduced theory is not the Fueter theory of the quaternions; it is a pair of complex analyses, and the Fueter-type operators appear in the operator theory.**

The quaternion variable admits the Fueter class of regular functions, driven by the non-commutative structure and the single complex analysis of the operator $\partial/\partial\bar z$; the reduced biquaternion variable, being commutative with zero divisors, does not reproduce that class: its differentiable functions are the pairs of holomorphic functions of §*The Reduction to Two Complex Analyses*, and the Cauchy–Riemann system decouples. The operator theory that replaces the Fueter construction, with the reduced Dirac-type operator and its solutions, is *Fueter Theory for Reduced Biquaternions*, and the integral theory based on the decoupled system is *Reduced Biquaternion Integration*.

## Summary

Reduced biquaternion analysis works on a domain of the Euclidean space with metric $d(\breve Q_{1},\breve Q_{2})=\sqrt{K(\breve Q_{1}-\breve Q_{2})}$. Limits and continuity are coordinatewise for the two idempotent coordinates, and the continuous functions form a commutative algebra closed under the three conjugations. The difference quotient requires a division by the increment, and the increments that are zero divisors cannot divide; the quotient is defined on the dense set of invertible increments, the polynomials in $\breve Q$ are differentiable with the formal derivative, and the conjugation $\bar{\breve Q}$ is not differentiable, the quotient depending on the direction. Differentiable functions decouple into the two idempotent coordinates, $f(\breve Q)=G_{1}(Q_{++})\Pi_++G_{2}(Q_{--})\Pi_-$ with $G_{1}$ and $G_{2}$ holomorphic, and the reduced Cauchy–Riemann system is the pair of complex equations $\partial/\partial\bar Q_{++}g_{1}=0$ and $\partial/\partial\bar Q_{--}g_{2}=0$. The differential operators are the Wirtinger derivatives of the two coordinates, with Laplacian $\Delta=8(\partial^2/\partial Q_{++}\partial\bar Q_{++}+\partial^2/\partial Q_{--}\partial\bar Q_{--})$ and components harmonic. On a two-dimensional subspace the analysis is the complex or the split-complex analysis of one variable, and the Fueter theory of the quaternions is replaced by the operator theory of *Fueter Theory for Reduced Biquaternions*. The multiplication is **commutative**, **has zero divisors** and is **not a division algebra**, which is why the analysis is a pair of complex analyses and not a single four-dimensional one.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Omega$ | a domain, an open connected set |
| $f_{1}=\lambda_+\circ f$, $f_{2}=\lambda_-\circ f$ | the two idempotent-coordinate functions |
| $\frac{f(\breve Q+\breve Q_{H})-f(\breve Q)}{\breve Q_{H}}$ | the difference quotient, for $\breve Q_{H}$ invertible |
| $f(\breve Q)=G_{1}(Q_{++})\Pi_++G_{2}(Q_{--})\Pi_-$ | a differentiable function, with $G_{1},G_{2}$ holomorphic |
| $\partial/\partial Q_{++},\partial/\partial\bar Q_{++},\partial/\partial Q_{--},\partial/\partial\bar Q_{--}$ | the Wirtinger derivatives of the two coordinates |
| $\Delta=8(\partial^2/\partial Q_{++}\partial\bar Q_{++}+\partial^2/\partial Q_{--}\partial\bar Q_{--})$ | the Euclidean Laplacian |

## Further Reading

- [The Euclidean Topology of the Reduced Biquaternion Algebra](the-euclidean-topology-of-the-reduced-biquaternion-algebra.html), for the metric and the unit group.
- [Ideals and Peirce Decomposition of the Algebra of the Reduced Biquaternions](ideals-and-peirce-decomposition-of-the-general-plain-algebra-of-the-reduced-biquaternions.html), for the two coordinate projections.
- [Topology and Metric for Each of the Operations](topology-and-metric-for-each-of-the-operations-of-the-reduced-biquaternions.html), for the metric of each product.
- [The Four Products, Their Forms and Their Algebraic Norms](the-four-products-their-forms-and-their-algebraic-norms-of-the-reduced-biquaternions.html), for the products and the norms used throughout.
- [Introduction to the Algebra of the Reduced Biquaternions](introduction-to-the-general-plain-algebra-of-the-reduced-biquaternions.html), for the algebra and the idempotent splitting.
- [Biquaternion Analysis](biquaternion-analysis.html), for the non-commutative companion.
