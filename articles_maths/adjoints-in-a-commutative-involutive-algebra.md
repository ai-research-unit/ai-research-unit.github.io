# __Adjoints in a Commutative Involutive Algebra__

## Introduction

A non-degenerate reflexive pairing $B$ on a commutative involutive algebra $(A,\sigma)$ turns each $R$-linear operator $F : A\to A$ into a second operator $F^{\dagger}$, the **adjoint**, defined by moving $F$ from one side of the pairing to the other, $B(Fx,y) = B(x,F^{\dagger}y)$; the assignment $F\mapsto F^{\dagger}$ is an involution of the endomorphism algebra $\operatorname{End}_R(A)$, and it is the operator-level companion of the involution $\sigma$ of the elements. This article develops the adjoint for the commutative involutive algebras of *Commutative Algebras with an Involution*: it proves the existence and uniqueness of $F^{\dagger}$, establishes that ${}^{\dagger}$ is an anti-automorphism of order two, describes the **self-adjoint part** and the **unitary operators**, and computes the adjoint of a multiplication, $L_a^{\dagger} = L_{\sigma(a)}$. The last computation identifies the abstract involution of the multiplication operators of *Involutions of the Multiplication Operators* with the adjoint involution restricted to $\operatorname{Mult}(A)$, and it shows that every multiplication operator is **normal**, $L_aL_a^{\dagger} = L_a^{\dagger}L_a$, because of the commutativity of the algebra.

The article assumes *Commutative Algebras with an Involution* for $\sigma$, *Involutions of the Multiplication Operators* for $L_a$ and the induced involution, *The Operators on an Algebra* and *The Adjoint of an Endomorphism* for the adjoint of an endomorphism and the pairing, *Modules over a Ring* for the modules, and *Involutive Algebras* for the involution of the endomorphism algebra. The forms, the Hilbert structure and the operator spectrum belong to Part II; the signed variants are *The Signed Adjoint Sandwich*, *The Signed Adjoint of the Reflection* and *The Signed Adjoint of the Left Multiplication*, later in this group. Throughout, $R$ is a commutative ring with identity in which $2$ is invertible, $(A,\sigma)$ is a commutative involutive $R$-algebra, $B$ is a non-degenerate reflexive $\sigma$-sesquilinear pairing on $A$ with $B(ax,y) = B(x,\sigma(a)y)$, and ${}^{\dagger}$ is the adjoint involution of $\operatorname{End}_R(A)$; no norm, distance, positivity or operator spectrum occurs.

## The Pairing and the Adjoint

### The Adjacent Structure

**Definition.** A **$\sigma$-sesquilinear pairing** on $A$ is an $R$-bilinear map $B : A\times A\to R$ with $B(ax,y) = B(x,\sigma(a)y)$ for all $a, x, y$; it is **reflexive** when $B(x,y) = 0 \iff B(y,x) = 0$, and **non-degenerate** when $B(x,y) = 0$ for all $y$ forces $x = 0$ and dually. The pairing is the algebra-level analogue of the pairing of *The Adjoint of an Endomorphism*, and it is not a form in the sense of Part II: no symmetry and no sign is assumed, only the reflexivity needed for the adjoint.

**Theorem (existence and uniqueness).** For every $F \in \operatorname{End}_R(A)$ there is a unique $F^{\dagger}\in\operatorname{End}_R(A)$ with

$$
B(Fx,y) = B(x,F^{\dagger}y) \qquad \text{for all } x, y \in A .
$$

*Proof.* The map $y\mapsto B(F\,\cdot\,,y)$ is $R$-linear, so it is an element of the dual of $A$; non-degeneracy identifies the dual with $A$ through $z\mapsto B(\,\cdot\,,z)$, so there is a unique $z$ with $B(Fx,y) = B(x,z)$ for all $x$; put $F^{\dagger}y = z$. The assignment is additive and $R$-linear in $F$ and in $y$ because $B$ is bilinear. $\square$

### The Adjoint Involution

**Theorem.** The map ${}^{\dagger} : \operatorname{End}_R(A)\to\operatorname{End}_R(A)$ is additive, $R$-linear, of order two, and anti-multiplicative:

$$
(F+G)^{\dagger} = F^{\dagger}+G^{\dagger}, \qquad (\lambda F)^{\dagger} = \lambda F^{\dagger}, \qquad (FG)^{\dagger} = G^{\dagger}F^{\dagger}, \qquad (F^\dagger)^\dagger = F .
$$

Hence ${}^{\dagger}$ is an involution of the associative algebra $\operatorname{End}_R(A)$, in the sense of *Involutive Algebras*.

*Proof.* Additivity and $R$-linearity are the bilinearity of $B$; the order two is the reflexivity: $B(Fx,y) = B(x,F^{\dagger}y) = B((F^\dagger)^\dagger x,y)$ gives $(F^\dagger)^\dagger = F$ by non-degeneracy; the anti-multiplicativity is $B(FGx,y) = B(Gx,F^{\dagger}y) = B(x,G^{\dagger}F^{\dagger}y)$. $\square$

## The Adjoint Involution and the Self-Adjoint Part

### Self-Adjoint and Skew-Adjoint Operators

**Definition.** An operator $F$ is **self-adjoint** when $F^{\dagger} = F$, **skew-adjoint** when $F^{\dagger} = -F$, and **unitary** when $F^{\dagger}F = FF^{\dagger} = 1$; the set of the self-adjoint operators is $E^+$ and the set of the skew-adjoint operators is $E^-$, with $E = \operatorname{End}_R(A)$.

**Proposition.** The self-adjoint operators form a Jordan algebra under $F\bullet G = \tfrac12(FG+GF)$ and the skew-adjoint operators form a Lie algebra under the commutator; $E = E^+\oplus E^-$ when $2$ is invertible, and the unitary operators form a group.

*Proof.* This is *Involutive Algebras* applied to the involution ${}^{\dagger}$ of $E$: the fixed set is closed under the symmetrised product, the anti-fixed under the commutator, and the units fixed up to the inverse form the unitary group. $\square$

### The Adjoint of a Multiplication

**Theorem.** For every $a \in A$ the adjoint of the multiplication $L_a$ is the multiplication by the image of $a$ under the involution:
$$
L_a^{\dagger} = L_{\sigma(a)} .
$$

*Proof.* $B(L_ax,y) = B(ax,y) = B(x,\sigma(a)y) = B(x,L_{\sigma(a)}y)$ for all $x,y$, so $L_{\sigma(a)}$ satisfies the defining relation of the adjoint, and the adjoint is unique. $\square$

**Corollary (consistency with the induced involution).** The restriction of the adjoint involution ${}^{\dagger}$ to the multiplication operators is the induced involution of *Involutions of the Multiplication Operators*: $L_a^{\dagger} = L_a^{*}$. Hence the fixed part of the multiplication algebra is the multiplication algebra of the fixed subalgebra, and the two constructions of the involution of $\operatorname{Mult}(A)$ coincide.

**Corollary (normality).** Every multiplication operator is normal with respect to ${}^{\dagger}$,
$$
L_aL_a^{\dagger} = L_{a\sigma(a)} = L_a^{\dagger}L_a ,
$$
because the algebra is commutative; the multiplication operators therefore lie in the **normal** part of $\operatorname{End}_R(A)$, and $L_a$ is self-adjoint exactly when $\sigma(a) = a$ and skew-adjoint exactly when $\sigma(a) = -a$.

*Proof.* $L_aL_a^{\dagger} = L_aL_{\sigma(a)} = L_{a\sigma(a)}$ and $L_a^{\dagger}L_a = L_{\sigma(a)}L_a = L_{\sigma(a)a}$, and $a\sigma(a) = \sigma(a)a$. $\square$

## Examples

**Example (the coordinate algebra).** Let $A = R^n$ with the standard pairing $B(x,y) = \sum_ix_iy_i$ and let $\sigma$ be an involution of $A$ permuting or negating the coordinates. Then the adjoint of an operator $F$, represented by a matrix, is $F^{\dagger} = \sigma F^{\mathsf{T}}\sigma^{-1}$, that is, the transpose composed with the coordinate involution on both sides. The multiplications $L_a$ for $a$ a diagonal matrix are diagonal, and $L_a^{\dagger} = L_{\sigma(a)}$ is the diagonal matrix with the permuted or negated diagonal, confirming the theorem.

**Example (the polynomial ring).** Let $A = R[x]$ with $\sigma(x) = -x$ and let $B$ be the $R$-bilinear pairing with $B(x^i,x^j) = \delta_{ij}$, reflexive and non-degenerate on the polynomials of bounded degree; then $L_x^{\dagger} = L_{-x} = -L_x$, so the multiplication by $x$ is skew-adjoint, and the multiplication by $x^2$ is self-adjoint. The fixed subalgebra of the multiplication operators is the multiplication by the even polynomials.

## Summary

A non-degenerate reflexive $\sigma$-sesquilinear pairing on a commutative involutive algebra $(A,\sigma)$ defines the **adjoint** $F^{\dagger}$ of every operator by $B(Fx,y) = B(x,F^{\dagger}y)$; the adjoint exists, is unique, and the assignment ${}^{\dagger}$ is an **involution** of $\operatorname{End}_R(A)$, additive, $R$-linear, of order two and anti-multiplicative. The **self-adjoint** operators form a Jordan algebra under the symmetrised product and the **skew-adjoint** operators a Lie algebra under the commutator, with the decomposition into the two when $2$ is invertible; the **unitary** operators form a group. The adjoint of a multiplication is $L_a^{\dagger} = L_{\sigma(a)}$, so the adjoint involution restricted to the multiplication operators is the induced involution of *Involutions of the Multiplication Operators* and every multiplication operator is **normal**. The coordinate algebra and the polynomial ring are the worked examples. No norm, distance, positivity or operator spectrum occurs.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(A,\sigma)$ | Commutative involutive $R$-algebra |
| $B(ax,y) = B(x,\sigma(a)y)$ | $\sigma$-sesquilinear pairing |
| $B(Fx,y) = B(x,F^{\dagger}y)$ | Definition of the adjoint |
| $(FG)^{\dagger} = G^{\dagger}F^{\dagger}$, $(F^\dagger)^\dagger = F$ | The adjoint involution |
| $E^+, E^-$ | Self-adjoint and skew-adjoint operators |
| $F^{\dagger}F = FF^{\dagger} = 1$ | Unitary operator |
| $L_a^{\dagger} = L_{\sigma(a)} = L_a^{*}$ | Adjoint of a multiplication |
| $L_aL_a^{\dagger} = L_a^{\dagger}L_a$ | Normality of the multiplications |

## Further Reading

- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society Colloquium Publications 44, 1998), for the adjoint involution and the self-adjoint part.
- Nicolas Bourbaki, *Algebra II* (Springer, 2003), for the sesquilinear pairings, the adjoints and the reflexive forms.
- Richard D. Schafer, *An Introduction to Nonassociative Algebras* (Academic Press, 1966), for the endomorphism algebra, the adjoint and the normal elements.
- Werner Greub, *Multilinear Algebra* (Springer, second edition, 1978), for the pairings, the dualities and the transpose.
- Nathan Jacobson, *Structure and Representations of Jordan Algebras* (American Mathematical Society, 1968), for the self-adjoint operators as a Jordan algebra.
