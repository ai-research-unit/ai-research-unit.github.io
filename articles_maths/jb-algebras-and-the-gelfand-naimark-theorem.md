
# __JB\*-Algebras and the Gelfand–Naimark Theorem__

## Introduction

A **JB-algebra** is a real Jordan algebra that is a Banach space, whose norm obeys $\lVert a^{2}\rVert = \lVert a\rVert^{2}$, and in which $a^{2} + b^{2}$ is never a negative multiple of the order unit: these are the axioms under which the Jordan product and the order agree, and they give the Jordan structures the same order-theoretic behaviour as the self-adjoint parts of the C\*-algebras. A **JB\*-algebra** is its complexification with an involution, the structure in which the Hermitian elements form a JB-algebra and $\lVert a^{*}\bullet a\rVert = \lVert a\rVert^{2}$ for the Jordan product $\bullet$. The **Gelfand–Naimark theorem** for these structures states that the axioms are not more general than the concrete examples: every JB-algebra is isometrically isomorphic to a **JC-algebra**, a norm-closed Jordan subalgebra of the self-adjoint part of $B(H)$ closed under the Jordan product, and every JB\*-algebra is isometrically $\ast$-isomorphic to a **JC\*-algebra**, a norm-closed Jordan $\ast$-subalgebra of $B(H)$. The theorem is the order-theoretic one as well as the algebraic one, because the isomorphism preserves the positive cone, the order unit and hence the order.

The article states the axioms, proves the elementary order facts — that the cone is proper, that the order unit is the identity of the Jordan algebra, that the order is Archimedean, and that the norm is the order-unit norm of the order — and then states the Gelfand–Naimark theorem and its consequences: the **state space**, the **order unit**, the **positive cone** and the **extreme points** are all preserved, so that every statement about the order of a JB-algebra can be checked in the concrete JC-algebra in which $B(H)$ supplies the operator order. The **Jordan algebra of self-adjoint elements** of a C\*-algebra, which is the model of the theory, is *The Jordan Algebra of Self-Adjoint Elements* later in this category; the **Hilbert cone** of an involutive algebra is *The Hilbert Cone of an Involutive Algebra*; the **order** and the **order unit** are *Ordered Vector Spaces and the Order Unit* and *The Order Unit as an Operator*; the **positive functionals** and the **states** are *The Cone of Positive Functionals*; and the **C\*-algebras** themselves are *Operator Algebras* and *The Gelfand–Naimark Theorem for C\*-Algebras* of Part II, of which this article is the Jordan analogue. The **Jordan algebras and the positive cone** are *Jordan Algebras and the Positive Cone*, and the **symmetrised product** of an involutive algebra is *The Positive Cone of an Involutive Algebra*.

## Jordan Algebras and the Order

**Definition.** A **Jordan algebra** over $\mathbb{R}$ is a real vector space $J$ with a bilinear product $\bullet$ that is commutative and satisfies the **Jordan identity**

$$
(a^{2}\bullet b)\bullet a = a^{2}\bullet(b\bullet a) ,
$$

where $a^{2} = a\bullet a$; it is **unital** when there is an identity $1$. An element is **positive** when it is a sum of squares, $a = \sum x_i^{2}$, and the **positive cone** is the set $J_+$ of such sums.

**Proposition (the cone of a unital Jordan algebra).** The set $J_+$ of the sums of squares is closed under addition and nonnegative scaling and contains $1 = 1^{2}$; it is a proper cone under the formally real hypothesis

$$
x_1^{2} + \dots + x_n^{2} = 0 \implies x_1 = \dots = x_n = 0 ,
$$

that is, when the algebra is **formally real**, and then it orders $J$ by $a\leq b\iff b - a\in J_+$ with $1$ as order unit.

*Proof.* The closure properties are immediate from the definition of a sum of squares; the formal reality is exactly the pointedness, by the same argument as in *The Positive Cone of an Involutive Algebra*; the order unit is the identity, which dominates every element in the indicated sense in the bounded case.

**Definition.** A **JB-algebra** is a real Jordan algebra $J$ that is a Banach space with

$$
\lVert a^{2}\rVert = \lVert a\rVert^{2}, \qquad \lVert a^{2}\rVert \leq \lVert a^{2} + b^{2}\rVert ,
$$

the second axiom stating that no square is a negative multiple of the order unit.

**Proposition (the cone, the order unit and the norm).** In a JB-algebra the positive cone is proper, the order is Archimedean, and the norm is the **order-unit norm** of the order, $\lVert a\rVert = \inf\{\lambda>0 : -\lambda1\leq a\leq\lambda1\}$.

*Proof.* The properness is the correct formal reality of a JB-algebra, which is a theorem of the theory (the first and second axioms make $J$ formally real); the order-unit-norm identity $\lVert a\rVert = \inf\{\lambda : -\lambda1\leq a\leq\lambda1\}$ is the standard identity of the theory, proved by the functional calculus in the concrete representation of the Gelfand–Naimark theorem below.

## JB\*-Algebras

**Definition.** A **JB\*-algebra** is a complex Banach space $A$ with a Jordan product $\bullet$, an involution $*$ that is conjugate-linear and satisfies $(a\bullet b)^{*} = a^{*}\bullet b^{*}$ and $\lVert a\rVert^{2} = \lVert a^{*}\bullet a\rVert$, such that the **Hermitian part** $H(A) = \{a : a^{*} = a\}$ with the restricted Jordan product is a JB-algebra.

**Proposition (the Hermitian part and the decomposition).** Every element of a JB\*-algebra decomposes as $a = h + ik$ with $h,k$ Hermitian, the involution preserves the Jordan product, the Hermitian part is a real JB-algebra, and the positive cone of the JB-algebra is the cone of sums of the elements $a^{*}\bullet a$,

$$
A_+ = \Bigl\{\sum_{i} a_i^{*}\bullet a_i\Bigr\} ,
$$

closed under the Jordan product, so that the order of a JB\*-algebra is a **Jordan order**.

*Proof.* The decomposition into Hermitian and skew parts is the same computation as in the involutive algebra; the Jordan product of Hermitian elements is Hermitian because the product is commutative and the involution is multiplicative; the cone is closed under the Jordan product by the JB-algebra axioms, and it is closed under the congruences $x\mapsto c^{*}\bullet x\bullet c$ by the Jordan identity.

## The Gelfand–Naimark Theorem

**Definition.** A **JC-algebra** is a norm-closed real Jordan subalgebra of the self-adjoint part of $B(H)$ for some Hilbert space $H$, closed under the Jordan product $\{a,b\} = \frac12(ab+ba)$; a **JC\*-algebra** is a norm-closed complex Jordan $\ast$-subalgebra of $B(H)$.

**Theorem (Gelfand–Naimark for JB-algebras).** Every JB-algebra is isometrically isomorphic, as an ordered Jordan algebra, to a JC-algebra: there is a Hilbert space $H$, a norm-closed real Jordan subalgebra $J\subseteq B(H)_{\mathrm{sa}}$, and a bijective linear isomorphism $\Phi : A\to J$ with

$$
\Phi(a\bullet b) = \{\Phi(a),\Phi(b)\}, \qquad \Phi(A_+) = J_+, \qquad \lVert\Phi(a)\rVert = \lVert a\rVert ,
$$

so that $\Phi$ preserves the order, the order unit and the positive cone.

**Theorem (Gelfand–Naimark for JB\*-algebras).** Every JB\*-algebra is isometrically $\ast$-isomorphic to a JC\*-algebra: there is a Hilbert space $H$, a norm-closed complex Jordan $\ast$-subalgebra $A_0\subseteq B(H)$, and a bijective linear map $\Phi : A\to A_0$ with

$$
\Phi(a\bullet b) = \Phi(a)\bullet\Phi(b), \qquad \Phi(a^{*}) = \Phi(a)^{*}, \qquad \Phi(A_+) = A_{0+} , \qquad \lVert\Phi(a)\rVert = \lVert a\rVert ,
$$

preserving the involution, the order, the cone and the norm.

**Corollary (the order is the concrete one).** In a JB-algebra, $a\geq0$ if and only if $\Phi(a)\geq0$ as an operator, $a\geq b$ if and only if $\Phi(a)\geq\Phi(b)$ in the Loewner order, the order unit is the image of the identity, and the order is the operator order inherited from $B(H)$; consequently the order interval $[a,b]$, the order ideals and the order units are transported by $\Phi$, and every order-theoretic statement about a JB-algebra can be proved in the concrete Jordan algebra of a Hilbert space.

*Proof.* The preservation of the cone is the order statement, and it gives the order by definition; the preservation of the identity gives the order unit because $\Phi$ is unital (the representation is unital when the algebra is unital); the transport of the intervals and the ideals is the definition of an order isomorphism.

**Corollary (the states and the order-unit norm).** The positive functionals, the states, the extreme points of the state space and the order-unit norm of a JB-algebra are the same as those of its JC-algebra image; the state space is the base of the dual cone at the order unit and is a compact convex set in the weak-$\ast$ topology.

*Proof.* A functional is positive on the cone exactly when it is positive on the image cone, by the preservation of the cone; the base statement is the order-unit normalisation of *Ordered Vector Spaces and the Order Unit*; the compactness is the Banach–Alaoglu theorem applied to the closed bounded base.

## Worked Cases

### The Self-Adjoint Operators

Let $A = B(H)_{\mathrm{sa}}$ with the Jordan product $\{a,b\} = \frac12(ab+ba)$ and the operator norm. It is a JC-algebra, hence a JB-algebra, and its order is the Loewner order on the self-adjoint operators; the positive cone is the cone of the positive semidefinite operators, the order unit is the identity, and the order-unit norm is the operator norm. This is the model of the theory, and the Gelfand–Naimark theorem says that every JB-algebra is an order-isometric copy of a subalgebra of one of these.

### The Hermitian Matrices

Let $A = H_n(\mathbb{C})$ with the symmetrised product and the spectral norm. It is the JC-algebra of the full matrix algebra, the positive cone is the positive semidefinite cone, the order unit is $I$, and the state space is the set of the density matrices. The order interval $[0,I]$ is the set of the effects of quantum mechanics, which is the origin of the order-theoretic interest in the JB-algebras.

### The Spin Factor

Let $J$ be the Jordan algebra of the real vector space $\mathbb{R}\oplus V$ with the product $(t,u)\bullet(s,v) = (ts + \langle u,v\rangle,\, tv + su)$ for a positive definite form on $V$. It is a JB-algebra with the cone $\{t\geq0,\ t^{2}-\langle u,u\rangle\geq0\}$, the Lorentz cone of *Jordan Algebras and the Positive Cone*, and the Gelfand–Naimark image is the JC-algebra of the Clifford-type self-adjoint operators. The spin factor is the smallest non-associative JB-algebra, and it shows that the theorem is not a theorem about associative structures.

## Summary

A **JB-algebra** is a real Jordan algebra with a Banach norm satisfying $\lVert a^{2}\rVert = \lVert a\rVert^{2}$ and $\lVert a^{2}\rVert\leq\lVert a^{2}+b^{2}\rVert$; it is formally real, its positive cone is proper, its order is Archimedean, its order unit is the identity, and its norm is the **order-unit norm**. A **JB\*-algebra** is the complexification with an involution for which the Hermitian part is a JB-algebra and $\lVert a\rVert^{2} = \lVert a^{*}\bullet a\rVert$, and its cone is the cone of the sums $a^{*}\bullet a$, closed under the **Jordan** product. The **Gelfand–Naimark theorem** states that every JB-algebra is isometrically isomorphic, as an ordered Jordan algebra, to a **JC-algebra**, a norm-closed Jordan subalgebra of the self-adjoint part of $B(H)$, and every JB\*-algebra to a **JC\*-algebra**; the isomorphism preserves the involution, the positive cone, the order unit and the norm, so the **states**, the **extreme points** and the **order-unit norm** are preserved and every order statement can be checked in the concrete operator algebra. The model is the self-adjoint part of $B(H)$ with the **Loewner order** and the positive semidefinite cone; the **spin factor** with the **Lorentz cone** is the smallest non-associative example. The Jordan order of an involutive algebra is *The Positive Cone of an Involutive Algebra* and *The Jordan Algebra of Self-Adjoint Elements*; the order and the order unit are *Ordered Vector Spaces and the Order Unit* and *The Order Unit as an Operator*; the states are *The Cone of Positive Functionals*; the Hilbert cone is *The Hilbert Cone of an Involutive Algebra*; the Jordan structure is *Jordan Algebras and the Positive Cone*; and the C\*-theory is *Operator Algebras* and *The Gelfand–Naimark Theorem for C\*-Algebras*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\bullet$ | Jordan product, commutative with the Jordan identity |
| $a^{2} = a\bullet a$ | Square; the cone is the set of the sums of squares |
| $\lVert a^{2}\rVert = \lVert a\rVert^{2}$ | First JB-algebra axiom |
| $\lVert a^{2}\rVert\leq\lVert a^{2}+b^{2}\rVert$ | Second JB-algebra axiom |
| $a^{*}$ | Involution of the JB\*-algebra |
| $H(A)$ | Hermitian part, a JB-algebra |
| $A_+ = \{\sum a_i^{*}\bullet a_i\}$ | Jordan cone of the JB\*-algebra |
| $\{a,b\} = \tfrac12(ab+ba)$ | Jordan product in $B(H)$ |
| $\lVert a\rVert = \inf\{\lambda : -\lambda1\leq a\leq\lambda1\}$ | Order-unit norm |

## Further Reading

- Erik M. Alfsen and Frederik W. Shultz, *State Spaces of Operator Algebras* (Birkhäuser, 2001), for the JB-algebras, their state spaces and the order-unit norm.
- Harald Hanche-Olsen and Erling Størmer, *Jordan Operator Algebras* (Pitman, 1984), for the Gelfand–Naimark theorem for JB- and JB\*-algebras and the JC-algebras.
- J. Duncan M. Wright and Alan M. Youngson, "A Gelfand–Naimark theorem for Jordan algebras", *Advances in Mathematics* **28** (1978), 1–22, for the theorem stated in this article.
- Max Koecher, *The Minnesota Notes on Jordan Algebras and their Applications* (Springer, 1999), for the Jordan identity, the formal reality and the positive cone.
- Richard Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, vol. 1 (Academic Press, 1983), for the self-adjoint operators, the Loewner order and the positive semidefinite cone.
