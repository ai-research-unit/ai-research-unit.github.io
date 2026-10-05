# __The Involution on the Multiplication Operators__

## Introduction

The multiplication operators of a commutative involutive algebra carry the involution $L_a^{*} = L_{\sigma(a)}$ of *Involutions of the Multiplication Operators*, and *Adjoints in a Commutative Involutive Algebra* shows that this involution is the restriction of the adjoint involution ${}^{\dagger}$ of $\operatorname{End}_R(A)$ to the multiplication algebra: $L_a^{*} = L_a^{\dagger}$. The present article reads the restricted involution as a structure in its own right. Its **fixed algebra** is the set of the self-adjoint multiplications, $\{F\in\operatorname{Mult}(A) : F^{\dagger} = F\}$, which is the multiplication algebra of the fixed subalgebra, $L_{A^\sigma}$, and which carries the symmetrised product $F\bullet G = \tfrac12(FG+GF)$ as a Jordan algebra; its skew part is $L_{A^-}$, and the whole multiplication algebra is the direct sum of the two when $2$ is invertible. The involution descends to the quotients of the algebra, to the module endomorphisms, and to the multiplication operators of the fixed subalgebra, and it is the operator-level shadow of the involution of the elements.

The article collects the properties of the restricted involution: it is the unique algebra involution of $\operatorname{Mult}(A)$ that corresponds to $\sigma$ under the isomorphism $a\mapsto L_a$; it is compatible with the inclusion $\operatorname{Mult}(A)\hookrightarrow\operatorname{End}_R(A)$, so the multiplication algebra is an involutive subalgebra of the endomorphism algebra; the fixed algebra $L_{A^\sigma}$ is the multiplication algebra of the fixed subalgebra and is a Jordan subalgebra of the self-adjoint operators; and the involution is compatible with the descent and with the quotients. The closed forms are the multiplication algebra of the polynomial ring with the negation, where the fixed algebra is the multiplication by the even polynomials, and of the coordinate algebra, where it is the multiplication by the fixed coordinates.

The article assumes *Involutions of the Multiplication Operators* for $L_a$ and the induced involution, *Adjoints in a Commutative Involutive Algebra* for the pairing, the adjoint ${}^{\dagger}$ and the identity $L_a^{\dagger} = L_{\sigma(a)}$, *Commutative Algebras with an Involution* for the fixed subalgebra and the descent, *Involutive Bilinear Algebras* for the involution of the endomorphism algebra and the fixed algebra of an involution, and *Jordan Algebras* for the symmetrised product. No form, norm, distance or order occurs.

## The Restricted Involution

### Definition and Identification

**Definition.** The **involution on the multiplication operators** is the map

$$
{}^{*} : \operatorname{Mult}(A)\to\operatorname{Mult}(A), \qquad F^{*} = F^{\dagger}|_{\operatorname{Mult}(A)},
$$

the restriction of the adjoint involution of $\operatorname{End}_R(A)$. On the generators it is $L_a^{*} = L_{\sigma(a)}$.

**Theorem.** The restriction ${}^{*}$ is well defined, coincides with the induced involution of *Involutions of the Multiplication Operators*, and makes $\operatorname{Mult}(A)$ an involutive subalgebra of $\operatorname{End}_R(A)$: the inclusion $\iota : \operatorname{Mult}(A)\hookrightarrow\operatorname{End}_R(A)$ satisfies $\iota(F^{*}) = \iota(F)^{\dagger}$.

*Proof.* $L_a^{\dagger} = L_{\sigma(a)}$ by *Adjoints in a Commutative Involutive Algebra*, so the restriction agrees with the displayed definition on the generators and hence on the whole algebra; the compatibility with the inclusion is the definition of the restriction. $\square$

**Corollary (uniqueness).** The involution ${}^{*}$ is the unique algebra involution of $\operatorname{Mult}(A)$ with $L_a^{*} = L_{\sigma(a)}$ for all $a$, because the $L_a$ generate the multiplication algebra and $a\mapsto L_a$ is injective; equivalently, it is the unique involution making the isomorphism $A\cong\operatorname{Mult}(A)$ equivariant.

### Compatibility with the Structure

**Proposition.** The restricted involution is compatible with the composition, $(FG)^{*} = G^{*}F^{*} = F^{*}G^{*}$, with the linearity, with the unit, $\mathrm{id}^{*} = \mathrm{id}$, and with the commutator in the sense $[F,G]^{*} = [G^{*},F^{*}]$.

*Proof.* The first two are the anti-multiplicativity of ${}^{\dagger}$ and the commutativity of the algebra; the unit is $L_1^{*} = L_{\sigma(1)} = L_1$; the commutator identity is the graded derivation of the anti-automorphism. $\square$

## The Fixed Algebra

### The Self-Adjoint Multiplications

**Theorem.** The fixed algebra and the skew part of the multiplication operators are

$$
\operatorname{Mult}(A)^{*} = \{F : F^{\dagger} = F\} = L_{A^\sigma}\cong A^\sigma, \qquad
\operatorname{Mult}(A)^{-} = \{F : F^{\dagger} = -F\} = L_{A^-}\cong A^- ,
$$

and $\operatorname{Mult}(A) = \operatorname{Mult}(A)^{*}\oplus\operatorname{Mult}(A)^{-}$ when $2$ is invertible.

*Proof.* $L_a^{\dagger} = L_a$ iff $\sigma(a) = a$; the injectivity of $a\mapsto L_a$ gives the isomorphisms; the direct sum is the involution decomposition of *Involutive Bilinear Algebras*. $\square$

**Corollary.** The fixed algebra of the involution on the multiplication operators is the multiplication algebra of the fixed subalgebra; it is $\operatorname{Mult}(A^\sigma)$, it is closed under the symmetrised product, and it is a Jordan subalgebra of the self-adjoint operators $E^+$ of $\operatorname{End}_R(A)$.

### The Jordan Structure

**Proposition.** With the symmetrised product $F\bullet G = \tfrac12(FG+GF)$ the fixed algebra $\operatorname{Mult}(A)^{*}$ is a Jordan algebra, isomorphic to $(A^\sigma)^+$; the skew part is a Lie algebra under the commutator, isomorphic to the Lie algebra of $A^-$ under the commutator.

*Proof.* The fixed algebra of an involution is closed under the symmetrised product and the anti-fixed part under the commutator, by *Involutive Bilinear Algebras*; the isomorphism with $A^\sigma$ and $A^-$ is $a\mapsto L_a$, which carries the products to the products. $\square$

## Descent and Quotients

**Proposition.** Let $I$ be a $\sigma$-stable ideal of $A$ and let $\bar\sigma$ be the induced involution of the quotient $A/I$. Then the multiplication operators of the quotient are the images of the multiplication operators of $A$ under the quotient map, and the induced involution of the quotient's multiplication operators is $\overline{L_a^{*}} = \overline{L_{\sigma(a)}}$; the fixed algebra is the multiplication algebra of $(A/I)^{\bar\sigma}\cong A^\sigma/(I\cap A^\sigma)$.

*Proof.* $L_{a+I} = \pi L_a$ where $\pi$ is the quotient map, and $\bar\sigma(a+I) = \sigma(a)+I$ gives $\overline{L_a^{*}} = L_{\bar\sigma(a+I)} = L_{\sigma(a)+I}$; the fixed subalgebra of the quotient is the quotient of the fixed subalgebra by $I\cap A^\sigma$ by *Involution-Invariant Ideals of the Symmetric Algebra*. $\square$

**Proposition (descent).** Under the descent of *Commutative Algebras with an Involution*, the multiplication operators of $A$ with a $\sigma$-semilinear involution are the scalar extensions of the multiplication operators of $A^\sigma$; the fixed algebra $L_{A^\sigma}$ is the algebra of the fixed points of the involution on $\operatorname{Mult}(A)$.

*Proof.* The descent identifies the $A$-modules with a $\sigma$-semilinear involution with the $A^\sigma$-modules, and the multiplication operators restrict to the multiplications of the fixed subalgebra. $\square$

## Examples

**Example (the negated variable).** For $A = R[x]$ with $\sigma(x) = -x$ the involution on the multiplication operators is $L_f^{*} = L_{f(-x)}$; the fixed algebra is $L_{R[x^2]}\cong R[x^2]$, the multiplications by the even polynomials, a Jordan algebra under the symmetrised product, and the skew part is $L_{xR[x^2]}$. On $R[x]/(x^k)$ the same formula holds modulo $x^k$.

**Example (the coordinate algebra).** For $A = R^n$ with the standard pairing and a coordinate involution $\sigma$, the multiplication operators are the diagonal matrices $L_a$; the involution on them is $L_a^{*} = L_{\sigma(a)}$, the fixed algebra is the diagonal matrices with the coordinates fixed by $\sigma$, and every such operator is self-adjoint.

## Summary

The **involution on the multiplication operators** of a commutative involutive algebra is $L_a^{*} = L_{\sigma(a)}$, the restriction of the adjoint involution ${}^{\dagger}$ of $\operatorname{End}_R(A)$; by *Adjoints in a Commutative Involutive Algebra* it is the induced involution of *Involutions of the Multiplication Operators*, and it is the unique algebra involution making the isomorphism $A\cong\operatorname{Mult}(A)$ equivariant. Its **fixed algebra** is $\operatorname{Mult}(A)^{*}\cong A^\sigma$, the multiplication algebra of the fixed subalgebra, a Jordan algebra under the symmetrised product; its skew part is $L_{A^-}$, a Lie algebra under the commutator; and $\operatorname{Mult}(A)$ is their direct sum when $2$ is invertible. The involution is compatible with the composition, descends to the stable quotients and to the fixed subalgebra under the descent, and makes the multiplication algebra an involutive subalgebra of the endomorphism algebra. The negated variable and the coordinate algebra are the worked examples. No form, norm, distance or order occurs.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{Mult}(A)$ | Multiplication algebra of the commutative algebra $A$ |
| $L_a^{*} = L_{\sigma(a)} = L_a^{\dagger}$ | The involution on the multiplication operators |
| $\iota(F^{*}) = \iota(F)^{\dagger}$ | Compatibility with the inclusion in $\operatorname{End}_R(A)$ |
| $\operatorname{Mult}(A)^{*}\cong A^\sigma$ | Fixed algebra |
| $\operatorname{Mult}(A)^{-}\cong A^-$ | Skew part |
| $F\bullet G = \tfrac12(FG+GF)$ | Jordan structure on the fixed algebra |
| $\overline{L_a^{*}}$ on $A/I$ | Descent to a stable quotient |

## Further Reading

- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society Colloquium Publications 44, 1998), for the involutions and their restrictions to subalgebras.
- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, 1968), for the multiplication algebra, its fixed part and the Jordan structure.
- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for the multiplication algebras and their involutions.
- Nicolas Bourbaki, *Algebra II* (Springer, 2003), for the commutative algebras, the ideals and the quotients.
- Atiyah and Macdonald, *Introduction to Commutative Algebra* (Addison-Wesley, 1969), for the quotients and the multiplication operators.
