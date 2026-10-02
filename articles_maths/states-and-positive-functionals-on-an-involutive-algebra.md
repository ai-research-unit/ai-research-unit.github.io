
# __States and Positive Functionals on an Involutive Algebra__

## Introduction

A linear functional on an involutive algebra is **positive** when it is non-negatively valued on the elements of the form $a^*a$, and a **state** is a positive functional of norm one. Positivity is the linear functional's way of respecting the order that the involution defines on the algebra, and it is the datum that produces representations: from a positive functional $f$ the formula $\langle a,b\rangle_f = f(b^*a)$ is a pre-inner product, its null space is a left ideal, and the operators of left multiplication by the elements of the algebra pass to the completion and become a $*$-representation with a cyclic vector whose expectation is $f$. This is the **GNS construction**, and it is the bridge from the algebraic positivity to the operator algebras: the states of a $\mathrm{C}^*$-algebra separate its points, and the Gelfand–Naimark representation is the direct sum of their GNS representations.

This article treats the positive functionals and the states of an involutive Banach algebra: the elementary positivity and the Cauchy–Schwarz inequality, the boundedness of a positive functional, the GNS construction and the cyclic representation it produces, the convexity and the extreme points of the state space, and the relation between positivity of elements and positivity of functionals. It assumes the involutive Banach algebra, the $\mathrm{C}^*$-identity and the Gelfand–Naimark theorem from *Involutive Banach Algebras and the Gelfand–Naimark Theorem*, the article immediately preceding; the self-adjoint elements, the positive cone and the order from *Self-Adjoint Elements and the Positive Cone* and *Involutive Linear Algebras*; the bounded operators on a Hilbert space, the adjoint and the cyclic vectors from *Operator Algebras*; and the positivity and the GNS construction of the operator setting from *Operators on a C*-Algebra*. The grade involution $\alpha$ of the signed block is not used.

Throughout, $A$ is a unital involutive Banach algebra over $\mathbb{C}$ with involution $a \mapsto a^*$; a **positive functional** is a linear $f : A \to \mathbb{C}$ with $f(a^*a) \geq 0$ for all $a$; a **state** is a positive functional with $\lVert f\rVert = 1$, equivalently with $f(1) = 1$; $\mathcal{S}(A)$ is the set of states; for a positive $f$ the **GNS data** are the pre-inner product $\langle a,b\rangle_f = f(b^*a)$, the null space $N_f = \{a : f(a^*a) = 0\}$, the Hilbert space $H_f$ the completion of $A/N_f$, the representation $\pi_f$, and the class $\xi_f = 1 + N_f$; and $\omega_f(a) = f(a)$ is the expectation of $a$ in the state.

## Positive Functionals

**Definition.** A linear functional $f$ on $A$ is **positive** when $f(a^*a) \geq 0$ for every $a \in A$, **self-adjoint** when $f(a^*) = \overline{f(a)}$ for every $a$, and **Hermitian** if it is self-adjoint. A positive functional with $f(1) = 1$ is a **state**.

**Proposition (positivity gives self-adjointness and reality on the symmetric part).** If $f$ is positive then $f$ is self-adjoint and $f(h) \in \mathbb{R}$ for every self-adjoint $h$; moreover $f(a^*) = \overline{f(a)}$ for every $a$, and $f(b^*ab) \geq 0$ when $a$ is positive.

**Proof.** Write $a = h + ik$ with $h,k$ self-adjoint; positivity gives $f((h+\lambda k)^*(h+\lambda k)) = f(h^2) + \lambda f(hk + kh) + \lambda^2 f(k^2) \geq 0$ as a real quadratic in the real $\lambda$, so its discriminant is non-positive and $f(hk+kh)^2 \leq 4f(h^2)f(k^2)$, forcing the bilinear form to be real-valued on the self-adjoint part; applying this to $a$ and the shared real linearity gives $f(a^*)=\overline{f(a)}$. The last statement is positivity applied to $a b$. $\square$

**Theorem (Cauchy–Schwarz).** Let $f$ be positive. Then for all $a,b \in A$,

$$
\lvert f(b^*a)\rvert^2 \leq f(a^*a)\,f(b^*b) ,
$$

with equality if and only if $a$ and $b$ are linearly dependent modulo the null space of the form.

**Proof.** For complex $\lambda$ the quantity $\langle a - \lambda b, a - \lambda b\rangle_f = f((a-\lambda b)^*(a-\lambda b)) \geq 0$, and expanding gives $f(a^*a) - \lambda f(a^*b) - \bar\lambda f(b^*a) + \lvert\lambda\rvert^2 f(b^*b) \geq 0$; choosing $\lambda = f(b^*a)/f(b^*b)$ when $f(b^*b) \neq 0$ gives the inequality, and the equality case is the degenerate Cauchy–Schwarz statement for a positive semidefinite form. $\square$

**Theorem (boundedness of a positive functional).** Let $f$ be positive on a unital involutive Banach algebra. Then $f$ is bounded, with

$$
\lVert f\rVert = f(1) ,
$$

so a state is exactly a positive functional with $f(1) = 1$. In a $\mathrm{C}^*$-algebra every positive functional is bounded.

**Proof.** For $a$ with $\lVert a\rVert \leq 1$, Cauchy–Schwarz gives $\lvert f(a)\rvert^2 = \lvert f(1^*a)\rvert^2 \leq f(1^*1) f(a^*a) = f(1) f(a^*a)$; and $f(a^*a) \leq \lVert a^*a\rVert f(1) \leq \lVert a\rVert^2 f(1)$, since $f(1) - \lVert a^*a\rVert\cdot 1$ is positive and $f$ is positive on the positive cone, giving $\lvert f(a)\rvert \leq f(1)$; the reverse inequality is $f(1) = f(1\cdot1^*) \leq \lVert f\rVert$, so $\lVert f\rVert = f(1)$. $\square$

## The GNS Construction

**Theorem (the construction).** Let $f$ be a positive functional on $A$. Then $N_f = \{a : f(a^*a) = 0\}$ is a left ideal, the formula $\langle a + N_f, b + N_f\rangle_f = f(b^*a)$ is a well-defined inner product on $A/N_f$, and there is a unique $*$-representation $\pi_f : A \to B(H_f)$ on the completion with

$$
\pi_f(a)\,(b + N_f) = ab + N_f , \qquad \pi_f(a)\xi_f = a + N_f , \qquad f(a) = \langle \pi_f(a)\xi_f, \xi_f\rangle_f ,
$$

so that $f$ is the vector state of the cyclic vector $\xi_f = 1 + N_f$. The representation is **cyclic**, $\pi_f(A)\xi_f$ is dense in $H_f$, and the pair $(\pi_f, H_f)$ is the **GNS representation** of $f$.

**Proof.** Cauchy–Schwarz shows that $N_f$ is the radical of the positive semidefinite form $\langle a,b\rangle_f = f(b^*a)$; it is a left ideal because $f((xa)^*(xa)) = f(a^*x^*xa) \leq \lVert x\rVert^2 f(a^*a)$ for $a \in N_f$, by positivity of the functional $a \mapsto f(a^*x^*xa)$ or by the Cauchy–Schwarz applied to the modified functional. The form descends to the quotient and is positive definite there; left multiplication by $a$ passes to the quotient because $N_f$ is a left ideal, is bounded by the same estimate, and extends to the completion. The involution compatibility $\langle \pi_f(a)x, y\rangle = \langle x, \pi_f(a^*)y\rangle$ is the computation $f(y^*(ax)) = f((a^*y)^*x)$. $\square$

**Theorem (positivity of an element is detected by the states).** Let $A$ be a $\mathrm{C}^*$-algebra. An element $a$ is positive, $a = b^*b$ for some $b$, if and only if it is self-adjoint and $f(a) \geq 0$ for every state $f$. The states separate the points of $A$.

**Proof.** If $a$ is positive then $f(a) = f(b^*b) \geq 0$ for every positive $f$. Conversely a self-adjoint $a$ with $f(a) \geq 0$ for all states has non-negative spectrum, because for $\lambda < 0$ the element $a - \lambda$ is invertible with positive inverse and a state evaluating non-negatively on it gives a contradiction; such an element is a square. For separation, if $a \neq 0$ then $a^*a \neq 0$ and some state has $f(a^*a) = \lVert a^*a\rVert > 0$, by the Gelfand–Naimark representation of *Involutive Banach Algebras and the Gelfand–Naimark Theorem*. $\square$

## The State Space

**Proposition (convexity and compactness).** The set $\mathcal{S}(A)$ of states is a convex subset of the unit ball of the dual, closed in the weak-$*$ topology, and weak-$*$ compact; a convex combination $\lambda f + (1-\lambda) g$ of states is a state.

**Proof.** Positivity is preserved by convex combinations and by weak-$*$ limits, and the condition $f(1) = 1$ is weak-$*$ continuous, so $\mathcal{S}(A)$ is a weak-$*$ closed subset of the weak-$*$ compact unit ball of the dual; the convexity is linearity. $\square$

**Definition.** A **pure state** is an extreme point of $\mathcal{S}(A)$; a **mixed state** is one that is not pure. The **state space** is $\mathcal{S}(A)$ and its extreme boundary is the set of pure states.

**Proposition (GNS and extremality).** A state $f$ is pure if and only if its GNS representation $\pi_f$ is irreducible, that is $\pi_f(A)' = \mathbb{C}\cdot 1$; for a pure state the GNS representation is the only cyclic representation up to unitary equivalence.

**Proof.** The commutant $\pi_f(A)'$ acts on $H_f$ and commutes with $\pi_f(A)$; a projection $P \in \pi_f(A)'$ with $0 \neq P \neq 1$ decomposes $f$ as a sum of two positive functionals, so $f$ is not extreme; conversely if $f = \lambda f_1 + (1-\lambda) f_2$ then the GNS space of $f$ is the direct integral of those of the summands, and a nontrivial decomposition produces a projection, so purity is irreducibility. $\square$

## Examples

**Example (the vector states).** Let $H$ be a Hilbert space and $\xi \in H$ a unit vector; then $f(T) = \langle T\xi,\xi\rangle$ is a state of $B(H)$, and its GNS representation is the identity representation on the cyclic subspace $\overline{B(H)\xi}$; if $\xi$ is cyclic for $B(H)$, that is for the whole $H$, the state is faithful.

**Example (the evaluation functionals).** For $A = C(X,\mathbb{C})$ with the sup norm, every state is a probability measure $\mu$ on $X$, $f \mapsto \int f\,d\mu$, and the pure states are the evaluations at the points of $X$; the GNS representation of the evaluation at $x$ is the one-dimensional representation $f \mapsto f(x)$, and the state is multiplicative.

**Example (the tracial state).** For $A = M_n(\mathbb{C})$ the normalised trace $f(X) = \tfrac1n\operatorname{tr}(X)$ is a faithful state, and its GNS representation is the defining representation on $\mathbb{C}^n$; the state is faithful but not pure, corresponding to the fact that the defining representation is irreducible yet the trace decomposes over the pure vector states.

## Faithful States and the Separating Vector

**Definition.** A positive functional $f$ is **faithful** when $f(a^*a) = 0$ implies $a = 0$, equivalently when its null space $N_f$ is $\{0\}$; a **normal state** of a von Neumann algebra $M \subseteq B(H)$ is a state of the form $\omega_\xi(T) = \langle T\xi,\xi\rangle$ for a unit vector $\xi$, a **vector state**.

**Proposition (faithfulness and the separating vector).** A positive functional $f$ is faithful if and only if its GNS representation $\pi_f$ is injective, equivalently the cyclic vector $\xi_f$ is **separating** for $\pi_f(A)$, that is $\pi_f(a)\xi_f = 0$ implies $a = 0$. A state is faithful exactly when $a \geq 0$ and $f(a) = 0$ force $a = 0$.

**Proof.** $f(a^*a) = \langle\pi_f(a)\xi_f, \pi_f(a)\xi_f\rangle = \lVert\pi_f(a)\xi_f\rVert^2$, so $N_f = \{a : \pi_f(a)\xi_f = 0\}$; faithfulness is the injectivity of $\pi_f$, that is the separating property of the cyclic vector. The last statement uses the positivity of $a = b^*b$: if $f(a) = 0$ then $f(b^*b) = 0$ and $b = 0$. $\square$

**Remark (the normal states and the predual).** For a von Neumann algebra $M$ the normal states are the vector states, they determine the strong topology and the predual $M_*$ with $M = (M_*)^*$, and the GNS representation of a normal state is normal; the cyclic vector is both cyclic and separating exactly when the state is faithful and the algebra is in standard form. The theory is *Operator Algebras*. The connection with this article is that the faithfulness of a state is a property of its GNS representation, and it is the property that makes the representation an isomorphism onto an algebra of operators.

## Summary

A positive functional on an involutive Banach algebra is self-adjoint, obeys the Cauchy–Schwarz inequality $\lvert f(b^*a)\rvert^2 \leq f(a^*a)f(b^*b)$, and is bounded with $\lVert f\rVert = f(1)$, so a state is exactly a positive functional of norm one. From a positive functional $f$ the GNS construction produces a Hilbert space $H_f$, a cyclic vector $\xi_f$ and a $*$-representation $\pi_f$ with $f(a) = \langle\pi_f(a)\xi_f,\xi_f\rangle$; the null space $N_f = \{a : f(a^*a) = 0\}$ is a left ideal and the form $\langle a,b\rangle_f = f(b^*a)$ descends to an inner product on $A/N_f$. In a $\mathrm{C}^*$-algebra an element is positive exactly when every state evaluates non-negatively on it, and the states separate the points; the state space is convex and weak-$*$ compact, and its extreme points are the pure states, whose GNS representations are the irreducible ones. The positivity and the order on the elements are *Self-Adjoint Elements and the Positive Cone* and *Hermitian and Self-Adjoint Elements of a Banach Algebra*; the representation theory in full is *Operator Algebras*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $f$, positive functional | Linear with $f(a^*a)\geq 0$ for all $a$ |
| $f(a^*a)\geq0$, $\lvert f(b^*a)\rvert^2\leq f(a^*a)f(b^*b)$ | Positivity and Cauchy–Schwarz |
| $\lVert f\rVert = f(1)$ | Boundedness of a positive functional |
| $\mathcal{S}(A)$ | The state space, convex weak-$*$ compact |
| $N_f = \{a : f(a^*a) = 0\}$ | Null left ideal of the form |
| $H_f$, $\pi_f$, $\xi_f$ | GNS Hilbert space, representation, cyclic vector |
| $f(a) = \langle\pi_f(a)\xi_f,\xi_f\rangle$ | The state as a vector state |
| Pure state, irreducible | Extreme point; $\pi_f(A)' = \mathbb{C}$ |
| Faithful $f$ | $f(a^*a)=0 \Rightarrow a=0$; $\pi_f$ injective |
| Normal state $\omega_\xi$ | $\omega_\xi(T) = \langle T\xi,\xi\rangle$, a vector state |

## Further Reading

- Jacques Dixmier, *$\mathrm{C}^*$-Algebras* (North-Holland, 1977), for the positive functionals, the states and the GNS construction.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras, Volume I* (Academic Press, 1983), for the state space, the pure states and the irreducibility criterion.
- Gérard J. Murphy, *$\mathrm{C}^*$-Algebras and Operator Theory* (Academic Press, 1990), for the positivity and the order detected by the states.
- Theodore W. Palmer, *Banach Algebras and the General Theory of ${}^*$-Algebras, Volume II* (Cambridge University Press, 2001), for the positive functionals on an involutive Banach algebra.
- Masamichi Takesaki, *Theory of Operator Algebras I* (Springer, 1979), for the cyclic representations and the GNS construction.
