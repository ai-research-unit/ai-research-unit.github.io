# __Reduced Biquaternion Analysis__

## Introduction

Reduced biquaternion analysis is the study of functions of a reduced biquaternion variable through the operations of the algebra, on the Euclidean space of *The Euclidean Topology of the Reduced Biquaternion Algebra*. The article fixes the metric setting, defines limits and continuity, states the **problem of differentiability** — the difference quotient needs a division by the increment, and the increment may be a zero divisor — and shows how the algebra resolves it: because the algebra is the direct product of two copies of $\mathbb{C}$, a function that is differentiable in the reduced sense decouples into **two complex analyses**, one in each idempotent coordinate. The class of functions so obtained, the pairs of holomorphic functions of the two coordinates, is the reduced analogue of the holomorphic functions, and it is the smallest possible: the algebra is **commutative**, it **has zero divisors**, the Euclidean norm is not multiplicative, and it is **not a division algebra**, so no richer theory of a single complex variable over the whole four-dimensional space is available. The functions themselves are the subject of *Reduced Biquaternion Regular Functions*.

**Conventions.** The basis is $1,i,j,ij$ with $i^{2}=-1$, $j^{2}=+1$, $ji=ij$; the element is $T=A+Bj$ with $A=a+ia'$, $B=b+ib'$; the idempotent coordinates are $q_1=A+B$, $q_2=A-B$, and $T=q_1\Pi_{1}+q_2\Pi_{2}$ with $\Pi_{1,2}=\tfrac12(1\pm j)$. The Euclidean metric is $d(T,W)=\sqrt{K(T-W)}$, $K=\lvert A\rvert^{2}+\lvert B\rvert^{2}$. The element glyph is $T$, without a tilde; a general function is written $\Phi$ or $f$.

**Boundaries.** The metric and the topology are *Topology in the Space of Reduced Biquaternions*, *The Euclidean Topology of the Reduced Biquaternion Algebra* and *Topology and Metric for Each of the Operations*; the two coordinate projections are *Ideals and Peirce Decomposition of the General Plain Algebra of the Reduced Biquaternions*; the differentiable functions are *Reduced Biquaternion Regular Functions*; the integral theory is *Reduced Biquaternion Integration*; the operator theory is *Fueter Theory for Reduced Biquaternions*. The biquaternion counterpart is *Biquaternion Analysis*.

## The Metric Structure

**The analysis is done in the metric space of the Euclidean norm, on an open set of the space.**

**Definition.** An **open set** $\Omega$ is a union of open balls of the Euclidean metric; a **domain** is a non-empty connected open set. A function is studied on a domain $\Omega\subset\mathbb{B}_{\mathrm{r}}$, with the induced metric $d$ and the induced topology.

**Theorem (the setting).** On a domain the metric is complete on the closed balls, the balls are convex, and every element of the domain has a ball neighbourhood contained in the domain; the four products are continuous, so all the algebra operations are defined and continuous on the domain and its functions.

*Proof.* The space is $\mathbb{R}^{4}$ under the coordinate isometry, so the balls are the standard Euclidean balls, which are convex and complete; the open-set property is the definition; the continuity of the products is *Topology in the Space of Reduced Biquaternions*.

## Limits and Continuity

**Definition.** For a function $f:\Omega\to\mathbb{B}_{\mathrm{r}}$, a point $Z_{0}\in\Omega$ and an element $L$, the **limit** is $f(Z)\to L$ as $Z\to Z_{0}$ when for every $\varepsilon>0$ there is $\delta>0$ with $\lVert f(Z)-L\rVert<\varepsilon$ whenever $0<\lVert Z-Z_{0}\rVert<\delta$; the function is **continuous** at $Z_{0}$ when $f(Z)\to f(Z_{0})$.

**Theorem (continuity is coordinatewise).** A function $f$ is continuous at $Z_{0}$ if and only if its two idempotent-coordinate functions
$$
f_{1}=\lambda_{1}\circ f,\qquad f_{2}=\lambda_{2}\circ f
$$
are continuous at $Z_{0}$ as complex-valued functions of $Z$. The two coordinate projections $\lambda_{1},\lambda_{2}$ are continuous algebra homomorphisms.

*Proof.* The homeomorphism $Z\mapsto(q_1,q_2)$ of *The Euclidean Topology of the Reduced Biquaternion Algebra* identifies the metric space with $\mathbb{C}\times\mathbb{C}$ with the product of the Euclidean metrics up to a constant; convergence in the product is convergence of the two coordinates; and the coordinate projections are the characters, which are ring homomorphisms continuous for the topology.

**Corollary (the algebra of continuous functions).** The continuous functions form a commutative algebra over $\mathbb{R}$ under the pointwise operations, closed under the three conjugations; the subalgebra of functions depending only on $q_1$, or only on $q_2$, is a copy of the continuous complex functions of one complex variable.

*Proof.* Pointwise sums and products of continuous functions are continuous, and the conjugations are continuous isometries; a function of $q_1$ alone is the composition of the continuous $Z\mapsto q_1$ with a continuous complex function.

## The Problem of Differentiability

**The difference quotient needs a division by the increment, and the increment may be a zero divisor.**

**Definition.** The **difference quotient** of $f$ at $Z$ with increment $H$ is
$$
\frac{f(Z+H)-f(Z)}{H},
$$
defined when $H$ is invertible. The function is **differentiable** at $Z$ when the quotient tends to a limit $f'(Z)\in\mathbb{B}_{\mathrm{r}}$ as $H\to0$ through the invertible increments.

**Theorem (the obstacle).** The increments range over the unit group, which is open and dense but not all of the space; the increments that are excluded are the zero divisors, and the division by them is impossible. The quotient is therefore defined on a dense subset of the increments and not on all of them.

*Proof.* The invertible increments are the units of *The Group of Units of the General Plain Algebra of the Reduced Biquaternions*, whose complement is the zero-divisor set of *Zero Divisors of the General Plain Algebra of the Reduced Biquaternions*, closed with empty interior; an increment in the complement, being without inverse, cannot divide.

**Theorem (the polynomials are differentiable).** Every polynomial in $T$ with reduced biquaternion coefficients is differentiable at every point, with derivative the formal derivative: if $P(X)=\sum_{n}c_{n}X^{n}$ then
$$
\frac{P(Z+H)-P(Z)}{H}=\sum_{n}c_{n}\sum_{k=0}^{n-1}(Z+H)^{n-1-k}Z^{k}\longrightarrow P'(Z)
$$
as $H\to0$, the inner sum being a polynomial in $H$.

*Proof.* Because the algebra is associative, $(Z+H)^{n}-Z^{n}=H\sum_{k=0}^{n-1}(Z+H)^{n-1-k}Z^{k}$, so the difference factors on the left or on the right by $H$; the algebra is commutative, so the two factorisations coincide; when $H$ is invertible the quotient is the inner sum, a polynomial in $H$, whose limit as $H\to0$ is $\sum_{n}nc_{n}Z^{n-1}=P'(Z)$, independent of the direction of approach.

**Corollary (a non-differentiable function).** The conjugation $T\mapsto\bar T$ is continuous but not differentiable at the origin: the quotient $\bar H/H$ equals $+1$ for real increments $H$ and $-1$ for increments $H=ijs$ on the fourth axis, so the limit depends on the direction and does not exist.

*Proof.* $\bar H=H$ for real $H$, giving quotient $1$; $\overline{ijs}=-ijs$ for the element $ijs$ on the fourth axis, giving quotient $-1$; the two directions give different limits, so no derivative exists.

## The Reduction to Two Complex Analyses

**A differentiable function of the reduced variable decouples into two holomorphic functions, one in each idempotent coordinate.**

**Theorem (the reduction).** Let $\Omega$ be a domain and $f:\Omega\to\mathbb{B}_{\mathrm{r}}$ differentiable in the sense above at every point, with the derivative continuous. Then, writing
$$
f(Z)=g_{1}(Z)\,\Pi_{1}+g_{2}(Z)\,\Pi_{2},
$$
the function $g_{1}$ depends only on $q_1$ and the function $g_{2}$ only on $q_2$, and each is holomorphic: there are holomorphic functions $G_{1}$ and $G_{2}$ of one complex variable with
$$
f(Z)=G_{1}(q_1)\,\Pi_{1}+G_{2}(q_2)\,\Pi_{2},\qquad f'(Z)=G_{1}'(q_1)\,\Pi_{1}+G_{2}'(q_2)\,\Pi_{2}.
$$

*Proof.* In the idempotent basis the algebra is the direct product and the multiplication is componentwise, so differentiating is componentwise: $f'(Z)=g_{1}'(Z)\Pi_{1}+g_{2}'(Z)\Pi_{2}$, and the componentwise derivative of $g_{1}$ at $Z$ along increments $H=m\Pi_{1}+n\Pi_{2}$ is the derivative in the coordinate $q_1$ alone, since the product $Z^{n}$ depends on $q_1$ and $q_2$ separately; the limit defining $g_{1}'$ uses only $m$, so $g_{1}$ has no dependence on $q_2$, and likewise $g_{2}$ has none on $q_1$. Each is then a complex function with a complex derivative, that is holomorphic, and the derivative rule is the chain rule in each coordinate.

**Corollary (the system decouples).** The reduced Cauchy–Riemann system is the pair of complex equations
$$
\frac{\partial g_{1}}{\partial\bar q_1}=0,\qquad \frac{\partial g_{2}}{\partial\bar q_2}=0,
$$
so the theory of differentiable reduced biquaternion functions is the product of two copies of the theory of holomorphic functions of one complex variable. There is no single complex analysis over the four-dimensional algebra, because the algebra is **not a division algebra**.

*Proof.* A complex function of one variable is holomorphic exactly when it satisfies the complex Cauchy–Riemann equation, that is when it is annihilated by the Wirtinger derivative in the conjugate coordinate; the system is the pair of the two coordinates, and the two have no coupling, the algebra being a direct product.

## The Differential Operators

**The Wirtinger derivatives of the two coordinates give the differential operators of the theory.**

**Definition.** On the four real coordinates, or on the complex coordinates $A,B$, define the **Wirtinger derivatives**
$$
\partial_{q_1}=\tfrac12\bigl(\partial_{A}+\partial_{B}\bigr),\quad
\partial_{\bar q_1}=\tfrac12\bigl(\partial_{\bar A}+\partial_{\bar B}\bigr),\quad
\partial_{q_2}=\tfrac12\bigl(\partial_{A}-\partial_{B}\bigr),\quad
\partial_{\bar q_2}=\tfrac12\bigl(\partial_{\bar A}-\partial_{\bar B}\bigr).
$$

**Theorem (the Laplacian).** The Euclidean Laplacian in the four real coordinates is
$$
\Delta=\partial_{a}^{2}+\partial_{a'}^{2}+\partial_{b}^{2}+\partial_{b'}^{2}
=4\bigl(\partial_{A}\partial_{\bar A}+\partial_{B}\partial_{\bar B}\bigr)
=8\bigl(\partial_{q_1}\partial_{\bar q_1}+\partial_{q_2}\partial_{\bar q_2}\bigr).
$$
As a check, $\Delta K=8$ and $\Delta q_1=\Delta q_2=0$.

*Proof.* For a complex variable $A=a+ia'$ one has $\partial_{a}=\partial_{A}+\partial_{\bar A}$ and $\partial_{a'}=i(\partial_{A}-\partial_{\bar A})$, so $\partial_{a}^{2}+\partial_{a'}^{2}=4\partial_{A}\partial_{\bar A}$, and likewise for $B$; this gives the middle expression. The change of variables $q_1=A+B$, $q_2=A-B$ gives $\partial_{A}=\partial_{q_1}+\partial_{q_2}$ and $\partial_{B}=\partial_{q_1}-\partial_{q_2}$, whence $\partial_{A}\partial_{\bar A}+\partial_{B}\partial_{\bar B}=2(\partial_{q_1}\partial_{\bar q_1}+\partial_{q_2}\partial_{\bar q_2})$, the last expression. For the check: $K=\tfrac12(\lvert q_1\rvert^{2}+\lvert q_2\rvert^{2})$ and $\partial_{q_1}\partial_{\bar q_1}\lvert q_1\rvert^{2}=1$, so $8(\tfrac12+\tfrac12)=8$; and the holomorphic coordinates are annihilated by the conjugate derivations.

**Corollary (the differentiable functions are harmonic).** A differentiable reduced biquaternion function $f(Z)=G_{1}(q_1)\Pi_{1}+G_{2}(q_2)\Pi_{2}$ satisfies
$$
\Delta f=0,
$$
each component being annihilated by the conjugate derivative of its own coordinate, $\partial_{\bar q_1}G_{1}=0$ and $\partial_{\bar q_2}G_{2}=0$.

*Proof.* A holomorphic function of one complex variable has harmonic real and imaginary parts, the Cauchy–Riemann equations giving $\partial_{a}^{2}+\partial_{a'}^{2}$ applied to each part equal to zero; the components are decoupled and the total Laplacian is the sum of the two-dimensional Laplacians of the two components, up to the factor of the change of variables.

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

The quaternion variable admits the Fueter class of regular functions, driven by the non-commutative structure and the single complex analysis of the operator $\partial_{\bar z}$; the reduced biquaternion variable, being commutative with zero divisors, does not reproduce that class: its differentiable functions are the pairs of holomorphic functions of §*The Reduction to Two Complex Analyses*, and the Cauchy–Riemann system decouples. The operator theory that replaces the Fueter construction, with the reduced Dirac-type operator and its solutions, is *Fueter Theory for Reduced Biquaternions*, and the integral theory based on the decoupled system is *Reduced Biquaternion Integration*.

## Summary

Reduced biquaternion analysis works on a domain of the Euclidean space with metric $d(T,W)=\sqrt{K(T-W)}$. Limits and continuity are coordinatewise for the two idempotent coordinates, and the continuous functions form a commutative algebra closed under the three conjugations. The difference quotient requires a division by the increment, and the increments that are zero divisors cannot divide; the quotient is defined on the dense set of invertible increments, the polynomials in $T$ are differentiable with the formal derivative, and the conjugation $\bar T$ is not differentiable, the quotient depending on the direction. Differentiable functions decouple into the two idempotent coordinates, $f(Z)=G_{1}(q_1)\Pi_{1}+G_{2}(q_2)\Pi_{2}$ with $G_{1}$ and $G_{2}$ holomorphic, and the reduced Cauchy–Riemann system is the pair of complex equations $\partial_{\bar q_1}g_{1}=0$ and $\partial_{\bar q_2}g_{2}=0$. The differential operators are the Wirtinger derivatives of the two coordinates, with Laplacian $\Delta=8(\partial_{q_1}\partial_{\bar q_1}+\partial_{q_2}\partial_{\bar q_2})$ and components harmonic. On a two-dimensional subspace the analysis is the complex or the split-complex analysis of one variable, and the Fueter theory of the quaternions is replaced by the operator theory of *Fueter Theory for Reduced Biquaternions*. The multiplication is **commutative**, **has zero divisors** and is **not a division algebra**, which is why the analysis is a pair of complex analyses and not a single four-dimensional one.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Omega$ | a domain, an open connected set |
| $f_{1}=\lambda_{1}\circ f$, $f_{2}=\lambda_{2}\circ f$ | the two idempotent-coordinate functions |
| $\frac{f(Z+H)-f(Z)}{H}$ | the difference quotient, for $H$ invertible |
| $f(Z)=G_{1}(q_1)\Pi_{1}+G_{2}(q_2)\Pi_{2}$ | a differentiable function, with $G_{1},G_{2}$ holomorphic |
| $\partial_{q_1},\partial_{\bar q_1},\partial_{q_2},\partial_{\bar q_2}$ | the Wirtinger derivatives of the two coordinates |
| $\Delta=8(\partial_{q_1}\partial_{\bar q_1}+\partial_{q_2}\partial_{\bar q_2})$ | the Euclidean Laplacian |

## Further Reading

- *The Euclidean Topology of the Reduced Biquaternion Algebra* (`articles_maths/the-euclidean-topology-of-the-reduced-biquaternion-algebra.md`), for the metric and the unit group.
- *Ideals and Peirce Decomposition of the General Plain Algebra of the Reduced Biquaternions* (`articles_maths/ideals-and-peirce-decomposition-of-the-general-plain-algebra-of-the-reduced-biquaternions.md`), for the two coordinate projections.
- *Topology and Metric for Each of the Operations* (`articles_maths/topology-and-metric-for-each-of-the-operations-of-the-reduced-biquaternions.md`), for the metric of each product.
- *The Four Products, Their Forms and Their Algebraic Norms* (`articles_maths/the-four-products-their-forms-and-their-algebraic-norms-of-the-reduced-biquaternions.md`), for the products and the norms used throughout.
- *Introduction to the General Plain Algebra of the Reduced Biquaternions* (`articles_maths/introduction-to-the-general-plain-algebra-of-the-reduced-biquaternions.md`), for the algebra and the idempotent splitting.
- *Biquaternion Analysis* (`articles_maths/biquaternion-analysis.md`), for the non-commutative companion.
