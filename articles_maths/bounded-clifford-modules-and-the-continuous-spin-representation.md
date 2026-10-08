# __Bounded Clifford Modules and the Continuous Spin Representation__

## Introduction

A Clifford module is a module on which the algebra acts, and the layer asks when the action is continuous and when it is **bounded**: the representation $\pi:\mathrm{Cl}(V,q)\to\operatorname{End}(M)$ is bounded when the operator norms of the images are uniformly bounded over the unit ball of the algebra, and the best constant is the **modulus** $\lvert\!\lvert\!\lvert\pi\rvert\!\rvert\!\rvert$ of the representation. The two questions — joint continuity of the action $A\times M\to M$ and boundedness of the modulus — are the same question in the normed case, and the uniform boundedness principle makes them the same also in the complete case when the action is defined on the whole product: a separately continuous action of a complete normed algebra on a complete normed module is automatically jointly continuous and bounded. This is the module version of the theorem of *The Bounded Left and Right Multiplication on a Clifford Algebra*, and it is the article where the spin representation is placed in the topological layer.

The examples are the content. The **spinor module** of a finite-dimensional Clifford algebra is a minimal left ideal, of dimension $2^{\lfloor n/2\rfloor}$, and the spin representation is the action of the algebra on it; in finite dimension every action is continuous and bounded, so the layer is silent. In infinite dimension the two natural modules separate: the **Fock module**, on which the canonical anticommutation relations act boundedly with modulus one, and the **regular module**, in which the algebra acts on itself by left multiplication. The Fock module is realised on the exterior algebra: with $V=W\oplus W^{*}$ paired by the polarisation and $\pi(w)(\lambda)=w\wedge\lambda$, $\pi(w^{*})(\lambda)=\iota_{w}(\lambda)$ on $\Lambda W$, the creators and the annihilators are of operator norm one and the modulus is one, and the representation is irreducible. The regular module is the contrasting example: its modulus is the multiplication constant of the norm, which exceeds one for the Euclidean norm of the definite case and is unbounded in infinite dimension, so the algebra is not a bounded representation of itself in that norm.

The article treats the modules and the continuity of the action, the modulus of a bounded representation, the spin representation and its topological properties, the Fock and exterior modules, and the extension of the action to a completion of the module. The abstract theory of the Clifford modules, the minimal left ideals and the spin representation as algebra is *Spin Representations and Clifford Modules with Inner Conjugation* and *Spinors as Minimal Left Ideals with Inner Conjugation*; the Fock representation and the canonical anticommutation relations are *Infinite-Dimensional Clifford Algebras and CAR with Inner Conjugation*; the continuity of the algebra itself is *Operators on a Topological Clifford Algebra*; the sandwich action of the versors on a module of spinors is *The Bounded Sandwich and the Continuous Inner Conjugation*; the Hermitian structure on a module is the layer of `Sesqualgebras with a degree-2 form`, whose *Hermitian Modules over a Hermitian Algebra with Hermitian Adjoint* and *Dirac Operators with Hermitian Adjoint* own the adjoint and the Dirac operator.

## Modules and the Continuity of the Action

**Definition.** A **topological Clifford module** is a topological $F$-module $M$ with a continuous left action $\mathrm{Cl}(V,q)\times M\to M$, $(\theta,m)\mapsto\theta m$, which is $F$-bilinear and associative, so that the associated representation $\pi:\mathrm{Cl}(V,q)\to\operatorname{End}(M)$, $\pi(\theta)m=\theta m$, is a homomorphism of algebras. A **normed** module carries a norm inducing its topology, and a normed module over a normed algebra is **bounded**, of **modulus** $\lvert\!\lvert\!\lvert\pi\rvert\!\rvert\!\rvert=\sup\{\lVert\pi(\theta)\rVert : \lVert\theta\rVert\le1\}$, when that supremum is finite.

**Proposition (the modulus and separate continuity).** Let $M$ be normed and let the action be continuous in each variable separately. Then each $\pi(\theta)$ is a bounded operator, $\lVert\pi(\theta)\rVert\le\lvert\!\lvert\!\lvert\pi\rvert\!\rvert\!\rvert\lVert\theta\rVert$ when the modulus is finite, and the modulus is finite exactly when the action has a uniform bound over the products of the unit balls.

*Proof.* Separately continuous linear maps of a normed space are bounded, so each $\pi(\theta)$ has finite norm; the bound $\lVert\pi(\theta)m\rVert\le C\lVert\theta\rVert\lVert m\rVert$ with $C$ the uniform bound is the definition of the modulus, and conversely a finite modulus gives the uniform bound. $\square$

**Theorem (the action on a complete module is bounded).** Let the algebra and the module be complete normed spaces over a complete valued field, and let the action be defined on the whole product $A\times M$ and be continuous in each variable separately. Then the action is **jointly continuous** and the representation is bounded.

*Proof.* Apply the uniform boundedness principle to the family $\{\pi(\theta) : \lVert\theta\rVert\le1\}$ of bounded operators on the complete space $M$: for each $m$ the set $\{\lVert\pi(\theta)m\rVert : \lVert\theta\rVert\le1\}$ is bounded, because the map $\theta\mapsto\theta m$ is continuous at the origin and hence bounded on the unit ball. The principle gives the uniform bound, that is the finiteness of the modulus; and a bilinear map with a uniform bound $C$ on the product of the unit balls is jointly continuous, since the bound on the unit balls extends to all elements by homogeneity and $\lVert\theta m-\theta_{0}m_{0}\rVert\le C(\lVert\theta\rVert\lVert m-m_{0}\rVert+\lVert\theta-\theta_{0}\rVert\lVert m_{0}\rVert)$, which tends to zero with the increments. $\square$

**Remark (the hypothesis, as for the product).** The theorem needs the action to be **defined** on the whole product of the two complete spaces. An action defined only on the algebraic algebra inside a completion — the situation of the Euclidean norm — is not addressed by the principle, and the failure of the uniform bound there is the same failure as in *The Bounded Left and Right Multiplication on a Clifford Algebra*. The module statement is therefore not an extra theorem but the same theorem in one more variable.

## The Spin Representation

**Definition.** Let $V$ be of finite dimension $n$ over $F$ with a non-degenerate form and let $\Delta$ be a minimal left ideal of $\mathrm{Cl}(V,q)$, of dimension $2^{\lfloor n/2\rfloor}$. The action of the algebra on $\Delta$ by left multiplication is the **spin representation**, $\pi_{\Delta}:\mathrm{Cl}(V,q)\to\operatorname{End}(\Delta)$, and the elements of $\Delta$ are the **spinors**.

**Proposition (topological properties of the finite-dimensional spin representation).** In finite dimension $\pi_{\Delta}$ is continuous and bounded; it is irreducible when the algebra is simple, and then it is faithful, the kernel being a two-sided ideal; and the even and the odd parts $\Delta^{\pm}$ are the two half-spinor spaces, exchanged by the odd part of the algebra, as in *Spin Representations and Clifford Modules with Inner Conjugation*.

*Proof.* All linear maps of a finite-dimensional space are continuous and the modulus is finite, the unit ball being compact; the irreducibility, the faithfulness under simplicity and the splitting are the algebraic statements of the cited Part I article. $\square$

**Theorem (the Fock module and the exterior module).** Let $W$ be a Hilbert space and let $V=W\oplus W^{*}$ carry the form that pairs the two summands by $B(w,w'^{*})=\tfrac12\langle w,w'\rangle$ and vanishes on each summand with itself. Then the exterior algebra $\Lambda W$ carries a continuous action of $\mathrm{Cl}(V,q)$ by

$$
\pi(w)(\lambda)=w\wedge\lambda,\qquad \pi(w^{*})(\lambda)=\iota_{w}(\lambda),
$$

the creators and the annihilators are of operator norm one, the modulus is one for the operator norm on the algebra — the norm of the norm closure that defines the CAR algebra — the representation is irreducible, and the module with this action is the **Fock module** of the canonical anticommutation relations of *Infinite-Dimensional Clifford Algebras and CAR with Inner Conjugation*. The completion of the algebraic exterior algebra in the norm of the inner product is a Hilbert space on which the action extends continuously, with the same modulus.

*Proof.* The classes $w\in W$ and $w^{*}\in W^{*}$ generate $V$, and on the exterior algebra the operators satisfy the Clifford relations: the creation operators $w\wedge\cdot$ commute with each other, the contractions anticommute with each other, and on a decomposable element $\lambda=w_{1}\wedge\dots\wedge w_{k}$ one computes $w\wedge\iota_{w'}(\lambda)+\iota_{w'}(w\wedge\lambda)=\langle w,w'\rangle\lambda=2B(w,w')\lambda$, which is the relation $\pi(w)\pi(w'^{*})+\pi(w'^{*})\pi(w)=2B(w,w')$ of the Clifford algebra of $V$; each creation operator is a partial isometry of norm $\lVert w\rVert$, since $\lVert w\wedge\lambda\rVert\le\lVert w\rVert\lVert\lambda\rVert$ with equality for $\lambda$ orthogonal to the span of $w$, and each contraction is its adjoint in the pairing, so the operators attached to unit vectors of $W$ have operator norm one, and the modulus is one for the operator norm of the algebra, that norm being the norm of the representation by definition of the CAR algebra. The vacuum generates the module under the creators, which is the irreducibility; the extension to the completion is by the uniform bound, as in the theorem on the extension of the action. $\square$

**Remark (the two infinite-dimensional modules are not the same module).** The Fock module is a **bounded** module of the algebraic Clifford algebra with modulus one, and the algebra acts on it by a faithful irreducible representation; the algebra itself, with the Euclidean norm, is a module over itself which is **not** bounded, its modulus being the multiplication constant, greater than one and infinite in infinite dimension. The two statements are compatible because the modules differ: in the first the action is defined on the whole of the module and the operators are uniformly bounded, in the second the algebra acts on itself by left multiplication and the multiplications have no uniform bound. The distinction is the module form of the distinction between a subalgebra of the bounded operators and a dense subalgebra on which the product does not extend.

## The Extension to a Completion

**Theorem (the extension of the action).** Let $M$ be a normed module on which the algebra acts with finite modulus and let $\widehat{M}$ be the completion of $M$ (or of the image of the algebra in the bounded operators when the module is the algebra itself). Then the action extends uniquely to a continuous action on $\widehat{M}$, with the same modulus, and the extended action makes $\widehat{M}$ a module over the completed algebra when the completion of the algebra is taken in a submultiplicative norm.

*Proof.* Each $\pi(\theta)$ is a bounded operator on $M$ of norm at most $\lvert\!\lvert\!\lvert\pi\rvert\!\rvert\!\rvert\lVert\theta\rVert$ for a submultiplicative norm, hence extends uniquely to the completion with the same norm; the extension is multiplicative on a dense subspace and hence everywhere, and the uniform bound is preserved by continuity. $\square$

**Corollary (the two completions of the spinor module).** The completion of the spinor module in the Euclidean norm is the Fock space, and the completed action is the Fock representation; the completion of the algebra in the projective norm acts on it by the extension of the same representation, and the two completions coincide as topological modules when the coefficient series converge absolutely.

*Proof.* The Fock space is the completion of the algebraic exterior algebra in the norm of the inner product, and the action of the theorem is the extension of the representation of the theorem above, with modulus one; the identification of the two completions is the comparison of *The Completion of a Clifford Algebra*. $\square$

## Worked Cases

### The Finite-Dimensional Case

For a finite-dimensional algebra over a complete valued field every module is a finite-dimensional space, every action is continuous and bounded, and the modulus is finite; the spin representation is the classical one and the article adds nothing beyond the notation. The case is the one to which the algebraic Part I articles apply without modification, and the layer begins with infinite dimension.

### The Fock Module and the Exterior Module

For $W$ of infinite dimension the Fock module of the theorem is a bounded irreducible module of modulus one, the completion in the norm of the inner product is the Fock space, and the creator and the annihilator have operator norm one. This is the module on which the C*-norm of *The Completion of a Clifford Algebra* is defined, by the formula $\lVert a\rVert=\lVert\pi_{\Delta}(a)\rVert$ for the representation, and the trustworthiness of the norm rests on the fact that the representation is faithful.

### The Module of the Algebra over Itself

The algebra acts on itself by left multiplication, and this is the regular module; its modulus is the multiplication constant of the norm, which is at most one for a submultiplicative norm and greater than one for the Euclidean norm, unbounded in infinite dimension. The regular module is the extreme case of a module that is not bounded, and it is the module whose failure is treated in *The Bounded Left and Right Multiplication on a Clifford Algebra*.

### The Extension to a Module of Spinors

For the **signed** layer the module of spinors carries the action $\chi_{x}$ of the versors of *The Bounded Sandwich and the Continuous Inner Conjugation*, and the refined statement that the Pin and Spin groups act through the Clifford module is *Pin Representations and Hermitian Modules with Signed Hermitian Adjoint* and *Spinors as Minimal Left Ideals with Signed Hermitian Adjoint* of `Sesqualgebras with a degree-2 form`, where the Hermitian structure is available; the present article owns only the continuity and the modulus of the action.

## Summary

A **topological Clifford module** is a topological module with a continuous bilinear action; when the module is normed the action has a **modulus** $\lvert\!\lvert\!\lvert\pi\rvert\!\rvert\!\rvert$, finite exactly when the action is uniformly bounded over the products of the unit balls, and a separately continuous action of a **complete** normed algebra on a complete normed module, defined on the whole product, is automatically jointly continuous and bounded, by the **uniform boundedness principle** — the module form of the theorem for the product of the algebra.

The **spin representation** is the action of the algebra on a minimal left ideal of dimension $2^{\lfloor n/2\rfloor}$; it is continuous and bounded in finite dimension, where the layer is silent, and the infinite-dimensional example that matters is the **Fock module** of the exterior algebra, where $\pi(w)=w\wedge\cdot$ and $\pi(w^{*})=\iota_{w}$ have operator norm one, the modulus is one, the representation is irreducible and faithful, and the action extends to the completion, which is the Fock space of *Infinite-Dimensional Clifford Algebras and CAR with Inner Conjugation*. The regular module, in which the algebra acts on itself, has modulus equal to the multiplication constant of the norm — greater than one and infinite for the Euclidean norm of the definite case — and that contrast is the module form of the difference between a subalgebra of the bounded operators and a dense subalgebra whose product does not extend.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\pi:\mathrm{Cl}\to\operatorname{End}(M)$ | the representation of the algebra on the module |
| $\lvert\!\lvert\!\lvert\pi\rvert\!\rvert\!\rvert$ | the modulus, $\sup\{\lVert\pi(\theta)\rVert : \lVert\theta\rVert\le1\}$ |
| $\Delta$, $\dim\Delta=2^{\lfloor n/2\rfloor}$ | the spinor module, a minimal left ideal |
| $\pi(w)=w\wedge\cdot$, $\pi(w^{*})=\iota_{w}$ | the creators and the annihilators of the Fock module |
| $\lvert\!\lvert\!\lvert\pi\rvert\!\rvert\!\rvert=1$ | the modulus of the Fock representation |
| $>1$, $\infty$ | the modulus of the regular module, Euclidean norm |
| $\Lambda W$ and its completion | the algebraic and the completed Fock module |

## Further Reading

- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, Vol. I (Academic Press, 1983), for the uniform boundedness principle and the boundedness of a representation.
- Ola Bratteli and Derek W. Robinson, *Operator Algebras and Quantum Statistical Mechanics*, Vol. 2 (Springer, 1997), for the canonical anticommutation relations and the Fock representation.
- Frank F. Bonsall and John Duncan, *Complete Normed Algebras* (Springer, 1973), for the modulus of a representation and the module theory of a normed algebra.
- Claude Chevalley, *The Algebraic Theory of Spinors and Clifford Algebras* (Springer, 1997), for the spinor module and the minimal left ideals.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd edition (Cambridge University Press, 2001), for the spin representation in the classical notation.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the half-spinor spaces and the action of the versors.
