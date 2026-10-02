
# __The Functional Calculus of a Self-Adjoint Element__

## Introduction

The spectral theorem for a self-adjoint element $a$ identifies the commutative $\mathrm{C}^*$-algebra $C^*(a,1)$ it generates with the algebra $C(\sigma(a))$ of continuous functions on its compact real spectrum, and under that identification the element $a$ is the identity function. Reading the identification backwards gives the **continuous functional calculus**: every continuous complex function $f$ on $\sigma(a)$ produces an element $f(a)$ of $A$, the assignment $f \mapsto f(a)$ is an isometric $*$-isomorphism of $C(\sigma(a))$ onto $C^*(a,1)$, and it intertwines the algebra of functions with the algebra of elements. The calculus is the analytic instrument of the whole theory: it produces the square roots, the absolute values and the positive elements, it proves the spectral mapping theorem $\sigma(f(a)) = f(\sigma(a))$ in one line, and it turns every property of a continuous function into a property of the element.

This article assumes the spectral theorem and the reality of the spectrum from *The Spectrum of a Self-Adjoint Element*; the commutative Gelfand–Naimark theorem from *Involutive Banach Algebras and the Gelfand–Naimark Theorem*; the positivity, the order, the square roots and the polar decomposition from *Hermitian and Self-Adjoint Elements of a Banach Algebra* and *Self-Adjoint Elements and the Positive Cone*; the spectrum and the holomorphic functional calculus from *Topological Algebras and Banach Algebras* and *Holomorphic Functional Calculus*; and the continuous calculus of the operator setting from *Operator Algebras* and *Operators on a C*-Algebra*. The grade involution $\alpha$ is not used.

Throughout, $A$ is a unital $\mathrm{C}^*$-algebra over $\mathbb{C}$ with involution $a \mapsto a^*$; $a$ is self-adjoint (or normal) with spectrum $\sigma(a)$ and $C^*(a,1)$ the closed unital $*$-subalgebra it generates; $C(\sigma(a))$ is the algebra of continuous complex functions on the compact set $\sigma(a)$ with the sup norm; and the **functional calculus** is the map $\Phi_a : C(\sigma(a)) \to A$, $f \mapsto f(a)$.

## The Continuous Calculus

**Theorem (the continuous functional calculus).** Let $a$ be self-adjoint. There is a unique unital $*$-homomorphism

$$
\Phi_a : C(\sigma(a)) \to A , \qquad f \mapsto f(a) ,
$$

and it is an isometric $*$-isomorphism onto $C^*(a,1)$; it sends the identity function to $a$, the constant $1$ to the unit, and conjugation to the involution, $\overline{f}(a) = f(a)^*$. For a polynomial $p$, $p(a)$ is the element computed by the algebra, so the calculus extends the polynomial calculus.

**Proof.** By *The Spectrum of a Self-Adjoint Element* the Gelfand transform is an isometric $*$-isomorphism $C^*(a,1) \to C(\sigma(a))$ sending $a$ to the identity function; its inverse is $\Phi_a$, it is an isometric $*$-isomorphism, and on polynomials it agrees with evaluation because the Gelfand transform is multiplicative and unital. Uniqueness: two unital $*$-homomorphisms agreeing on the identity function agree on its continuous functions by continuity and the Stone–Weierstrass density of the polynomials. $\square$

**Theorem (the spectral mapping theorem).** For self-adjoint $a$ and continuous $f : \sigma(a) \to \mathbb{C}$,

$$
\sigma\bigl(f(a)\bigr) = f\bigl(\sigma(a)\bigr) .
$$

**Proof.** Under the identification of $C^*(a,1)$ with $C(\sigma(a))$, the element $f(a)$ is the function $f$, whose spectrum as an element of the algebra $C(\sigma(a))$ is its range $f(\sigma(a))$; the spectrum is an invariant of the algebra $C^*(a,1)$ because invertibility in a unital $\mathrm{C}^*$-subalgebra with the same unit is the same as invertibility in $A$. $\square$

**Corollary (positivity and the calculus).** For self-adjoint $a$, $f(a) \geq 0$ exactly when $f \geq 0$ on $\sigma(a)$; the calculus is **positive**, and it produces the square root and the absolute value:

$$
f \geq 0 \Rightarrow \Phi_a(f) \geq 0 , \qquad a^{1/2} = \Phi_a(\lambda \mapsto \lambda^{1/2}) , \qquad \lvert a\rvert = \Phi_a(\lvert\lambda\rvert) ,
$$

with unique $a^{1/2} \geq 0$ and $(a^{1/2})^2 = a$.

**Proof.** If $f \geq 0$ then $f = g\bar g$ for the continuous $g = f^{1/2}$, so $\Phi_a(f) = \Phi_a(g)\Phi_a(g)^* \in P$; conversely $f(a) \geq 0$ implies $f \geq 0$ because $f$ is the Gelfand transform of $f(a)$ and the characters are positive on positive elements. The square root and the absolute value are the functions displayed; the uniqueness of the positive square root is *Self-Adjoint Elements and the Positive Cone*. $\square$

## The Normal Case and the Comparison

**Theorem (the calculus for a normal element).** The continuous functional calculus holds for a normal element $a$ ($a^*a = aa^*$): $\Phi_a$ is an isometric $*$-isomorphism $C(\sigma(a)) \to C^*(a,1)$, and for two continuous functions $f,g$, $f(a)g(a) = (fg)(a)$. The spectrum $\sigma(a)$ is a compact subset of $\mathbb{C}$, and $\lVert f(a)\rVert = \lVert f\rVert_\infty$.

**Proof.** For normal $a$ the $\mathrm{C}^*$-algebra $C^*(a,1)$ is commutative, so the Gelfand transform identifies it with $C(\sigma(a))$ and the same argument applies; multiplicativity and isometry are inherited. $\square$

**Remark (the two calculi).** The continuous calculus works for self-adjoint and, more generally, normal elements, because the algebra generated is commutative; for a general element the polynomial calculus does not extend continuously, and one uses the **holomorphic functional calculus**, which for a function holomorphic on a neighbourhood of $\sigma(a)$ produces $f(a)$ by a contour integral. The holomorphic calculus is *Holomorphic Functional Calculus*; the continuous calculus is its boundary case for normal elements, and it is this calculus that is used in the spectral theory of a self-adjoint element. The operator-valued version, with the projection-valued measure, is *Operator Algebras*.

**Example (the Hermitian matrix).** For a Hermitian matrix $X = U\operatorname{diag}(\lambda_i)U^*$ the calculus is $f(X) = U\operatorname{diag}(f(\lambda_i))U^*$, the spectral mapping theorem reads that the eigenvalues of $f(X)$ are the values of $f$ on the eigenvalues of $X$, and the positive square root is the matrix with the square roots of the eigenvalues on the diagonal.

**Example (the function algebra).** For $A = C(X,\mathbb{C})$ and a real-valued $f$ self-adjoint, the calculus is $g(f) = g \circ f$; the spectral mapping theorem reads $\sigma(g\circ f) = (g\circ f)(X)$, and the square root is the pointwise square root.

**Example (the multiplication operator).** On $A = L^\infty(X,\mu)$ a real self-adjoint function acts on $L^2(X,\mu)$ as a multiplication operator; the calculus is $g(a) = g\circ a$, and the projection-valued measure of the spectral theorem is the family of indicator functions of the sublevel sets, the operator form of the spectral decomposition.

## The Analytic and the Borel Calculi

**Theorem (the analytic calculus).** For a self-adjoint $a$ and a function $f$ holomorphic on an open neighbourhood of $\sigma(a)$,

$$
f(a) = \frac{1}{2\pi i}\oint_\Gamma f(\lambda)(\lambda - a)^{-1}\,d\lambda ,
$$

where $\Gamma$ is a finite cycle in the domain of $f$ surrounding $\sigma(a)$; the element is independent of $\Gamma$, and the assignment $f \mapsto f(a)$ is a unital algebra homomorphism extending the polynomial calculus, the **holomorphic functional calculus**. The contour integral and the general theory are *Holomorphic Functional Calculus*.

**Theorem (the Borel calculus, named).** For a self-adjoint operator $a \in B(H)$ the calculus extends to the bounded Borel functions on $\sigma(a)$ and the spectral theorem delivers a **projection-valued measure** $E$ on the Borel sets of $\sigma(a)$ with

$$
a = \int_{\sigma(a)} \lambda\,dE(\lambda) , \qquad f(a) = \int_{\sigma(a)} f\,dE .
$$

The measure $E$, the measurable calculus and the spectral decomposition are *Operator Algebras*; here they are named and deferred.

**Proposition (the polynomial core).** The continuous calculus is the unique continuous extension of the polynomial calculus, and by the Stone–Weierstrass theorem the polynomials are dense in $C(\sigma(a))$; the spectral mapping theorem for a polynomial is the algebraic statement that the algebra homomorphism sends the identity function to $a$.

## Summary

For a self-adjoint element $a$ of a unital $\mathrm{C}^*$-algebra the continuous functional calculus is the unique unital $*$-homomorphism $\Phi_a : C(\sigma(a)) \to A$, $f \mapsto f(a)$, and it is an isometric $*$-isomorphism onto the commutative $\mathrm{C}^*$-algebra $C^*(a,1)$; it sends the identity function to $a$ and conjugation to the involution, and it extends the polynomial calculus. The spectral mapping theorem reads $\sigma(f(a)) = f(\sigma(a))$, the calculus is positive, $f \geq 0$ implying $f(a) \geq 0$, and it produces the square root $a^{1/2}$ and the absolute value $\lvert a\rvert$. The calculus holds for a normal element, whose generated algebra is commutative, and its boundary case for general elements is the holomorphic functional calculus, which produces $f(a)$ by a contour integral; the operator-valued spectral theorem with the projection-valued measure is the form the calculus takes in *Operator Algebras*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $a = a^*$ | Self-adjoint element, $\sigma(a) \subseteq \mathbb{R}$ |
| $\Phi_a : C(\sigma(a)) \to A$, $f \mapsto f(a)$ | The continuous functional calculus |
| $C^*(a,1)$ | The commutative unital $\mathrm{C}^*$-algebra generated by $a$ |
| $\sigma(f(a)) = f(\sigma(a))$ | Spectral mapping theorem |
| $f \geq 0 \Rightarrow f(a) \geq 0$ | Positivity of the calculus |
| $a^{1/2} = \Phi_a(\lambda^{1/2})$, $\lvert a\rvert = \Phi_a(\lvert\cdot\rvert)$ | Square root and absolute value |
| Normal $a$ | The calculus extends, $C^*(a,1)$ commutative |
| Holomorphic calculus | Contour-integral calculus for a general element |
| Borel calculus, PV measure $E$ | $a=\int\lambda\,dE$; deferred to *Operator Algebras* |

## Further Reading

- Gérard J. Murphy, *$\mathrm{C}^*$-Algebras and Operator Theory* (Academic Press, 1990), for the continuous functional calculus, the spectral mapping theorem and the positive square roots.
- Jacques Dixmier, *$\mathrm{C}^*$-Algebras* (North-Holland, 1977), for the calculus and its place in the spectral theory.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume I* (Academic Press, 1983), for the continuous and Borel functional calculi and the spectral theorem.
- Nelson Dunford and Jacob T. Schwartz, *Linear Operators, Part I* (Interscience, 1958), for the holomorphic functional calculus and the contour-integral construction.
- John B. Conway, *A Course in Functional Analysis* (Springer, second edition, 1990), for the functional calculus in the operator form.
