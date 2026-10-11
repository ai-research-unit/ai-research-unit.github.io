# __Idempotents of the Symmetric Plain Algebra__

## Introduction

The symmetric plain algebra $\mathbb{B}^{\bullet}$ is the complex space $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ under the Jordan product $\tilde P\bullet\tilde Q=\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$ of *Introduction to the Symmetric Plain Algebra of Biquaternions*. This article determines the **idempotents** of the block, classifies them, and reads the decomposition each one produces.

The idempotents of the block are the idempotents of the algebra: the two squares agree, $\tilde Q\bullet\tilde Q=\tilde Q\tilde Q$, so the equation $\tilde Q\bullet\tilde Q=\tilde Q$ is the equation $\tilde Q^2=\tilde Q$. The classification is therefore the one of *Idempotents of the General Plain Algebra*, and this article states it in the block's reading and draws the one conclusion that the algebra cannot draw, the **Jordan Peirce decomposition**.

The block is not left-alternative, and this is the decisive difference from the algebra in the operator theory. In the algebra an idempotent gives a **projector**, $L_{\tilde\Pi}^{2}=L_{\tilde\Pi}$, and the projector produces a Peirce decomposition, corner subalgebras and a lattice of ideals. In the block the operator of an idempotent is **not** a projector, and only the unit gives the identity operator; what the Jordan theory provides instead is the **cubic Peirce identity** $L_{\tilde\Pi}(2L_{\tilde\Pi}-\mathrm{id})(L_{\tilde\Pi}-\mathrm{id})=0$ and the decomposition of the space into the three Jordan Peirce spaces. The article states the absence of the associative calculus and gives the form the Jordan theory allows.

An idempotent is defined relative to a product, and the definition is stated once for a general product in *Definitions for the Study of the 12 Algebraic Structures*, §*The Idempotent*; throughout this article the product is $\bullet$ and, unqualified, **idempotent** means idempotent of $\bullet$. The idempotents of the algebra are *Idempotents of the General Plain Algebra*; the associated zero divisors are *Zero Divisors of the Symmetric Plain Algebra*; the operator theory is *The Multiplication Operators of the Symmetric Plain Algebra*; and the criterion that separates the block from the algebra is *The Specificities of the Symmetric Plain Algebra*.

**Conventions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, $e_1e_2=e_3$, central scalar imaginary $i$ and $Q_\mu\in\mathbb{C}$. An element is $\tilde Q=Q_0e_0+\mathbf{Q}$ with $\mathbf{Q}=\sum_{k=1}^{3}Q_ke_k$, and $(\mathbf{P},\mathbf{Q})=\sum_kP_kQ_k$. The product with the mark is $\tilde P\bullet\tilde Q=\tfrac12(\tilde P\tilde Q+\tilde Q\tilde P)$; the central square is $c(\tilde Q)=\sum_\mu Q_\mu^2=\tilde Q\tilde Q^{\natural}$. The left multiplication is $L^{\bullet}_{\tilde X}:\tilde Y\mapsto\tilde X\bullet\tilde Y$.

## The Definition and the Equation

**Definition (idempotent of a product).** Let $\star$ be a product on $\mathbb{B}$; then $\tilde\Pi$ is an **idempotent of $\star$** when

$$
\tilde\Pi\star\tilde\Pi=\tilde\Pi .
$$

The origin is an idempotent of every product, and a product with a unit has the unit as an idempotent.

Throughout this article the product is the symmetric plain product $\bullet$, and the equation is $\tilde\Pi\bullet\tilde\Pi=\tilde\Pi$. Because the square of the block is the plain square, the equation is the equation of the algebra,

$$
\tilde\Pi^{2}=\tilde\Pi\qquad\Longleftrightarrow\qquad \tilde\Pi\bullet\tilde\Pi=\tilde\Pi ,
$$

and the idempotents of the block are exactly the idempotents of the general plain product. The classification of the algebra applies verbatim; it is restated here in the block's coordinates and with the block's reading.

## The Classification

**Theorem (the idempotents).** The idempotents of the block are exactly the following.

**The two trivial idempotents.**

$$
\tilde\Pi=0,\qquad \tilde\Pi=e_0 .
$$

**The non-trivial idempotents.** The elements

$$
\tilde\Pi=\tfrac12\bigl(e_0+\mathbf{u}\bigr),\qquad \mathbf{u}\in\mathrm{Vect}(\mathbb{B}),\quad \mathbf{u}\neq0,\quad \mathbf{u}^2=e_0 ,
$$

a four-real-parameter family, equivalently written $\tilde\Pi=\tfrac12(e_0+\boldsymbol{\tilde\Xi} i)$ with $\boldsymbol{\tilde\Xi}$ pure and $\boldsymbol{\tilde\Xi}^2=-e_0$.

*Proof.* Write $\tilde\Pi=\Pi_0e_0+\boldsymbol{\Pi}$ and use the plain square $\tilde\Pi^2=\bigl[\Pi_0^2-(\boldsymbol{\Pi},\boldsymbol{\Pi})\bigr]e_0+2\Pi_0\boldsymbol{\Pi}$. The equation $\tilde\Pi^2=\tilde\Pi$ is the pair

$$
2\Pi_0\boldsymbol{\Pi}=\boldsymbol{\Pi},\qquad \Pi_0^2-(\boldsymbol{\Pi},\boldsymbol{\Pi})=\Pi_0 .
$$

The first forces $(2\Pi_0-1)\boldsymbol{\Pi}=0$: either $\boldsymbol{\Pi}=0$, and the second gives $\Pi_0^2=\Pi_0$, that is $\tilde\Pi=0$ or $\tilde\Pi=e_0$; or $\Pi_0=\tfrac12$, and then $(\boldsymbol{\Pi},\boldsymbol{\Pi})=-\tfrac14$, that is $\boldsymbol{\Pi}=\tfrac12\mathbf{u}$ with $\mathbf{u}$ pure and $(\mathbf{u},\mathbf{u})=-1$, which is $\mathbf{u}^2=e_0$. The two cases are exhaustive.

The parametrisation $\mathbf{u}=\boldsymbol{\tilde\Xi} i$ is the corpus's form: with $\boldsymbol{\tilde\Xi}$ pure and $\boldsymbol{\tilde\Xi}^2=-e_0$ one has $\mathbf{u}^2=\boldsymbol{\tilde\Xi}^2i^2=(-e_0)(-e_0)=e_0$, and conversely every pure $\mathbf{u}$ with $\mathbf{u}^2=e_0$ is $\boldsymbol{\tilde\Xi}=\mathbf{u}i^{-1}$ with $\boldsymbol{\tilde\Xi}^2=-e_0$.

**Corollary (the bijection).** The map $\mathbf{u}\mapsto\tfrac12(e_0+\mathbf{u})$ is a bijection from the pure roots of $+1$ onto the non-trivial idempotents, and the non-trivial idempotents are exactly the pure roots of $+1$ divided by two and translated by $\tfrac12e_0$.

## The Idempotents and the Roots

The pure roots of $+1$ are the pure elements $\mathbf{u}$ with $(\mathbf{u},\mathbf{u})=-1$ (*Square Roots of Minus One, Zero and Plus One in the Symmetric Plain Algebra*, where the family is described in real coordinates as $\mathbf{u}=\mathbf{p}i-\mathbf{p}'$ with $\mathbf{p}^2-\mathbf{p}'^2=1$ and $\mathbf{p}\cdot\mathbf{p}'=0$). The bijection turns the complex quadric $(\mathbf{u},\mathbf{u})=-1$ of the three-dimensional vector subspace into the idempotent family, and it separates the two trivial idempotents, which are not of the form $\tfrac12(e_0+\mathbf{u})$ with $\mathbf{u}$ pure.

**Proposition (the idempotents are isotropic).** Every non-trivial idempotent has vanishing central square,

$$
c\bigl(\tfrac12(e_0+\mathbf{u})\bigr)=\tfrac14\bigl(1+(\mathbf{u},\mathbf{u})\bigr)=0 ,
$$

while the unit has $c(e_0)=1\neq0$ and the origin is the trivial idempotent excluded by the definition of a zero divisor.

The non-trivial idempotents are therefore **isotropic** and, by the criterion of *Zero Divisors of the Symmetric Plain Algebra*, they are zero divisors: the annihilator of $\tfrac12(e_0+\mathbf{u})$ is the complex line $\mathbb{C}\,(e_0-\mathbf{u})$. The trivial idempotents $0$ and $e_0$ are not zero divisors, the origin being excluded by the definition and the unit being invertible.

## The Orthogonality and the Peirce Decomposition

### The Complementary Idempotent

**Proposition.** If $\tilde\Pi$ is an idempotent, then so is $e_0-\tilde\Pi$, and the two are orthogonal:

$$
(e_0-\tilde\Pi)^{\bullet2}=e_0-\tilde\Pi,\qquad \tilde\Pi\bullet(e_0-\tilde\Pi)=0 .
$$

*Proof.* $(e_0-\tilde\Pi)\bullet(e_0-\tilde\Pi)=e_0-2\tilde\Pi+\tilde\Pi^{\bullet2}=e_0-\tilde\Pi$, using $\tilde\Pi^{\bullet2}=\tilde\Pi$; and $\tilde\Pi\bullet(e_0-\tilde\Pi)=\tilde\Pi-\tilde\Pi^{\bullet2}=0$.

### The Absence of the Associative Peirce Calculus

**Proposition (no non-trivial idempotent gives a projector).** For a non-trivial idempotent $\tilde\Pi$ the left multiplication is not a projector, $L^{\bullet}_{\tilde\Pi}\circ L^{\bullet}_{\tilde\Pi}\neq L^{\bullet}_{\tilde\Pi}$; only the unit $e_0$ gives the identity operator.

*Proof.* On the witness $\tilde\Pi=\tfrac12(e_0+ie_1)$ the operator $L^{\bullet}_{\tilde\Pi}$ has the three distinct eigenvalues $0,\tfrac12,1$ (below), so $L^{\bullet}_{\tilde\Pi}(L^{\bullet}_{\tilde\Pi}-\mathrm{id})\neq0$. The reason is structural: the identity $L^{\bullet}_{\tilde X}{}^{2}=L^{\bullet}_{\tilde X^{\bullet2}}$ at every $\tilde X$ is left alternativity, the block is not left-alternative, and the chain $L^{\bullet}_{\tilde\Pi}{}^{2}=L^{\bullet}_{\tilde\Pi^{\bullet2}}=L^{\bullet}_{\tilde\Pi}$ that makes an idempotent a projector therefore breaks at its second step (*The Specificities of the Symmetric Plain Algebra*).

**The absence is stated and not filled.** The block has no projector calculus of the non-trivial idempotents, no corner subalgebras of the associative kind, and no ideal lattice generated by an idempotent: those are theorems of a left-alternative structure and the block is not one. What it has is the decomposition the Jordan theory allows, which is the next subsection.

### The Jordan Peirce Decomposition

**Theorem (the cubic Peirce identity).** For every idempotent $\tilde\Pi$ of the block the left multiplication satisfies

$$
2L^{\bullet}_{\tilde\Pi}{}^{3}-3L^{\bullet}_{\tilde\Pi}{}^{2}+L^{\bullet}_{\tilde\Pi}=0,
\qquad\text{that is}\qquad L^{\bullet}_{\tilde\Pi}\bigl(2L^{\bullet}_{\tilde\Pi}-\mathrm{id}\bigr)\bigl(L^{\bullet}_{\tilde\Pi}-\mathrm{id}\bigr)=0 .
$$

*Proof.* The identity is the polynomial identity of an idempotent in a Jordan algebra; in the block it is the statement that the eigenvalues of $L^{\bullet}_{\tilde\Pi}$ lie in $\{0,\tfrac12,1\}$, which is recomputed below on the witness and follows in general from the multiplication by $\tilde\Pi$ being a degree-two derivation of the quadric.

**Theorem (the decomposition).** Let $\tilde\Pi$ be a non-trivial idempotent and let

$$
\mathbb{B}_{\lambda}=\{\tilde Y\in\mathbb{B}:\ \tilde\Pi\bullet\tilde Y=\lambda\tilde Y\},\qquad \lambda\in\{0,\tfrac12,1\}.
$$

Then $\mathbb{B}=\mathbb{B}_{1}\oplus\mathbb{B}_{1/2}\oplus\mathbb{B}_{0}$ and the three spaces are:

$$
\mathbb{B}_{1}=\mathbb{C}\tilde\Pi,\qquad \mathbb{B}_{0}=\mathbb{C}(e_0-\tilde\Pi),\qquad \dim_{\mathbb{C}}\mathbb{B}_{1/2}=2 .
$$

*Proof.* By the cubic identity the operator $L^{\bullet}_{\tilde\Pi}$ has the minimal polynomial $t(t-\tfrac12)(t-1)$ with distinct roots, so it is diagonalisable and the three eigenspaces add to the whole space. The eigenvalue $1$ is realised by $\tilde\Pi$ and the eigenvalue $0$ by $e_0-\tilde\Pi$; the trace $\operatorname{Tr}L^{\bullet}_{\tilde\Pi}=4\Pi_0=2$ is the sum of the eigenvalues counted with multiplicity, so $1+0+\tfrac12\dim\mathbb{B}_{1/2}=2$ and the middle space has dimension two.

The middle space is the Jordan analogue of the two mixed Peirce spaces of an associative algebra; it is a single space and not a pair, because the product is commutative, and it is a bimodule and not a subalgebra. The decomposition is the **Jordan Peirce decomposition** of the block relative to $\tilde\Pi$, and it is the form the Jordan theory allows; the deeper theory of the Peirce spaces is *The Multiplication Operators of the Symmetric Plain Algebra*.

## Summary

The idempotents of the block are the idempotents of the plain product, the two squares being equal. They are the origin, the unit, and the four-real-parameter family $\tfrac12(e_0+\mathbf{u})$ with $\mathbf{u}$ pure and $\mathbf{u}^2=e_0$, equivalently $\tfrac12(e_0+\boldsymbol{\tilde\Xi} i)$ with $\boldsymbol{\tilde\Xi}$ a pure root of $-1$; the non-trivial idempotents are in bijection with the pure roots of $+1$. Every non-trivial idempotent is isotropic, $c=0$, and is a zero divisor whose annihilator is the line spanned by its natural conjugate, while the two trivial idempotents are not zero divisors. An idempotent and its complement $e_0-\tilde\Pi$ are orthogonal idempotents. The block is not left-alternative, so a non-trivial idempotent does **not** give a projector and there is no associative Peirce calculus, no corner subalgebra and no ideal lattice; only the unit gives the identity operator. What survives is the Jordan theory: the cubic Peirce identity $L^{\bullet}_{\tilde\Pi}(2L^{\bullet}_{\tilde\Pi}-\mathrm{id})(L^{\bullet}_{\tilde\Pi}-\mathrm{id})=0$ and the decomposition $\mathbb{B}=\mathbb{C}\tilde\Pi\oplus\mathbb{B}_{1/2}\oplus\mathbb{C}(e_0-\tilde\Pi)$ with a two-dimensional middle space.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tilde P\bullet\tilde Q$ | the symmetric plain product, the multiplication of the block |
| $\tilde\Pi$ | an idempotent of the block, $\tilde\Pi^{\bullet2}=\tilde\Pi$ |
| $\tfrac12(e_0+\mathbf{u})$, $\mathbf{u}^2=e_0$ | the non-trivial idempotents |
| $e_0-\tilde\Pi$ | the complementary idempotent, orthogonal to $\tilde\Pi$ |
| $2L^{\bullet}_{\tilde\Pi}{}^{3}-3L^{\bullet}_{\tilde\Pi}{}^{2}+L^{\bullet}_{\tilde\Pi}=0$ | the cubic Peirce identity |
| $\mathbb{B}_{1}\oplus\mathbb{B}_{1/2}\oplus\mathbb{B}_{0}$ | the Jordan Peirce decomposition, of dimensions $1,2,1$ |

## Further Reading

- *Definitions for the Study of the 12 Algebraic Structures*, §*The Idempotent*, for the product-relative definition.
- *Idempotents of the General Plain Algebra*, for the classification the block restates and the projector calculus the block does not have.
- *Square Roots of Minus One, Zero and Plus One in the Symmetric Plain Algebra*, for the pure roots of $+1$ that index the non-trivial idempotents.
- *Zero Divisors of the Symmetric Plain Algebra*, for the isotropic idempotents as the scalar family of the zero divisors.
- *The Specificities of the Symmetric Plain Algebra*, for the left alternativity the block fails and the Jordan law it satisfies.
- *The Multiplication Operators of the Symmetric Plain Algebra*, for the Peirce spaces and the structure algebra.
- Kevin McCrimmon, *A Taste of Jordan Algebras* (Springer, 2004), for the cubic Peirce identity and the Peirce decomposition of a Jordan algebra.
