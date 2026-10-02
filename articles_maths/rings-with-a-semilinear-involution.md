
# __Rings with a Semilinear Involution__

## Introduction

An involution of a ring is **linear** over the ring, and its twisting of the elements is only the reversal of products. When the ring carries an automorphism $\varsigma$, one may ask for a map that reverses products *and* intertwines $\varsigma$ with its inverse, a **$\varsigma$-semilinear involution**; the linear case is the case $\varsigma = \mathrm{id}$. The name is borrowed from the semilinear maps of a module, where a coefficient $\lambda$ is carried to $\varsigma(\lambda)$, and the point of the notion is that the naive identities then fail: the composite $\sigma\varsigma$ is an ordinary involution rather than the product of two, the map $\sigma$ commutes with $\varsigma$ only when $\varsigma^2 = \mathrm{id}$, and the fixed set of $\sigma$ need not be stable under $\varsigma$.

This article defines the semilinear involution of a ring, derives the identities that do hold, and records the failure of the ones a reader would expect; the map $\sigma\varsigma$ it produces is the ordinary involution to which the whole corpus applies. It assumes *Involutive Rings* for the involution, the fixed set and the symmetric and skew elements, and *Ring and Field Automorphisms* for the automorphism group; the semilinear involutions of a linear space and of an algebra over a field are treated with the linear structures of a later category and are named here only at the boundary. Throughout, $A$ is a ring with $1 \neq 0$, $\varsigma$ is an automorphism of $A$, and $\sigma$ is a $\varsigma$-semilinear involution; the ordinary involution attached to the pair is $\tau = \sigma\varsigma$. Nothing is measured, and no form or scalar product occurs.

## The Definition

**Definition.** Let $\varsigma$ be an automorphism of the ring $A$. A **$\varsigma$-semilinear involution** of $A$ is a map $\sigma : A \to A$ such that for all $a, b \in A$

$$
\sigma(a+b) = \sigma(a)+\sigma(b), \quad \sigma(ab) = \sigma(b)\sigma(a), \quad \sigma(1) = 1, \quad \sigma^2 = \mathrm{id}, \quad \sigma\varsigma = \varsigma^{-1}\sigma .
$$

The last condition is the **semilinearity**: $\sigma$ carries the automorphism $\varsigma$ to its inverse. When $\varsigma = \mathrm{id}$ the definition reduces to that of an ordinary involution, so the linear case is the case of a trivial twisting automorphism.

**Proposition (elementary).** Let $\sigma$ be $\varsigma$-semilinear. Then $\sigma$ is a bijection with $\sigma^{-1} = \sigma$, it is $\mathbb{Z}$-linear, it satisfies $\sigma(a^n) = \sigma(a)^n$, and it carries units to units. Moreover

$$
\sigma\varsigma = \varsigma^{-1}\sigma, \qquad \varsigma\sigma = \sigma\varsigma^{-1}, \qquad \sigma\varsigma^2 = \varsigma^{-2}\sigma, \qquad \sigma\varsigma^{k} = \varsigma^{-k}\sigma
$$

for every integer $k$.

**Proof.** Bijectivity and the power law are as for an involution. The second display follows from the first by composing with $\varsigma$ on the left and using $\varsigma^{-1}\varsigma = \mathrm{id}$: $\varsigma\sigma\varsigma = \sigma$, so $\varsigma\sigma = \sigma\varsigma^{-1}$. The third and fourth are obtained by iterating the second, $\sigma\varsigma^k = \varsigma^{-k}\sigma$ for all $k$.

## The Attached Ordinary Involution

**Theorem.** Let $\sigma$ be a $\varsigma$-semilinear involution and put $\tau = \sigma\varsigma$. Then $\tau$ is an **ordinary involution** of $A$, $\sigma = \tau\varsigma^{-1}$, and the automorphisms $\varsigma$ and $\sigma$ generate the dihedral group

$$
\langle \varsigma, \sigma \rangle = \{\varsigma^k, \sigma\varsigma^k : k \in \mathbb{Z}\}, \qquad \sigma^2 = \mathrm{id}, \qquad \sigma\varsigma\sigma^{-1} = \varsigma^{-1}.
$$

**Proof.** $\tau$ is additive and carries $1$ to $1$; it is anti-multiplicative, $\tau(ab) = \sigma(\varsigma(ab)) = \sigma(\varsigma(a)\varsigma(b)) = \sigma(\varsigma(b))\sigma(\varsigma(a)) = \tau(b)\tau(a)$; and $\tau^2 = \sigma\varsigma\sigma\varsigma = \sigma(\varsigma\sigma)\varsigma = \sigma(\sigma\varsigma^{-1})\varsigma = \varsigma^{-1}\varsigma = \mathrm{id}$, using the second identity of the previous proposition. The formula $\sigma = \tau\varsigma^{-1}$ is then immediate. The relation $\sigma\varsigma\sigma^{-1} = \varsigma^{-1}$ is the semilinearity with $\sigma^{-1} = \sigma$, and together with $\sigma^2 = \mathrm{id}$ it presents $\langle \varsigma, \sigma \rangle$ as the semidirect product $\langle \varsigma \rangle \rtimes \langle \sigma \rangle$, the dihedral group of order $2m$ when $\varsigma$ has finite order $m$ and an infinite dihedral group otherwise.

**Corollary (the ordinary case recovered).** The map $\sigma$ satisfies $\sigma\varsigma = \varsigma\sigma$ exactly when $\varsigma^2 = \mathrm{id}$, and then $\tau = \sigma\varsigma$ is the composite of the two commuting involutions $\sigma$ and $\varsigma$ of $A$. The $\varsigma$-semilinear involutions of $A$ are exactly the maps $\tau\varsigma^{-1}$ with $\tau$ an ordinary involution of $A$ satisfying $\tau\varsigma = \varsigma^{-1}\tau$.

**Proof.** $\sigma\varsigma = \varsigma\sigma$ is exactly $\varsigma^{-1} = \varsigma$, that is $\varsigma^2 = \mathrm{id}$; then $\tau = \sigma\varsigma$ is the composite of the two commuting order-two maps $\sigma$ and $\varsigma$. For the parametrisation, an ordinary involution $\tau$ gives $\sigma = \tau\varsigma^{-1}$, and $\sigma^2 = \tau\varsigma^{-1}\tau\varsigma^{-1}$ is $\mathrm{id}$ exactly when $\tau\varsigma^{-1}\tau = \varsigma$, that is, composing on the left by $\tau$, when $\varsigma^{-1}\tau = \tau\varsigma$; the remaining axioms are immediate.

## The Failure of the Naive Identities

The semilinear case is not the linear one with a decoration: four identities that hold when $\varsigma = \mathrm{id}$ fail as soon as the twisting is nontrivial.

**Proposition.** Let $\sigma$ be $\varsigma$-semilinear.

**(a)** $\sigma$ is $\varsigma$-**linear** ($\sigma\varsigma = \varsigma\sigma$) exactly when $\varsigma^2 = \mathrm{id}$; otherwise $\sigma$ intertwines $\varsigma$ with $\varsigma^{-1}$ and is not a semilinear map for $\varsigma$ in the usual sense of a module.

**(b)** The naive composite rule fails: whereas $\sigma^2\varsigma^2 = \varsigma^2$, the true composite is $(\sigma\varsigma)^2 = \mathrm{id}$ for every $\varsigma$.

**(c)** $\sigma$ commutes with $\varsigma^2$ exactly when $\varsigma^4 = \mathrm{id}$, because $\sigma\varsigma^2 = \varsigma^{-2}\sigma$.

**(d)** The fixed set $A^\sigma = \{a : \sigma(a) = a\}$ is an additive subgroup containing $1$, but it is stable under $\varsigma$ exactly when $\varsigma^2 = \mathrm{id}$ on $A^\sigma$; for $a \in A^\sigma$ one has $\sigma(\varsigma(a)) = \varsigma^{-1}(a)$, so $\varsigma(a)$ is again fixed exactly when $\varsigma^2(a) = a$.

**Proof.** (a) is the first identity of the previous proposition. (b) is the computation of the theorem. (c) is $\sigma\varsigma^2 = \varsigma^{-2}\sigma$, which is $\varsigma^2\sigma$ exactly when $\varsigma^{-2} = \varsigma^2$. (d) $A^\sigma$ is additive because $\sigma$ is, and contains $1$; for the stability, compute $\sigma(\varsigma(a)) = \varsigma^{-1}\sigma(a) = \varsigma^{-1}(a)$, which is $\varsigma(a)$ exactly when $\varsigma^2(a) = a$.

**Proposition (the fixed set is not a subring in general).** For $a, b \in A^\sigma$ one has $\sigma(ab) = \sigma(b)\sigma(a) = ba$, so $ab$ is fixed exactly when $a$ and $b$ commute. This is the same failure as for an ordinary involution of a noncommutative ring, and it is inherited from $\tau = \sigma\varsigma$: $A^\sigma$ is the fixed set of the ordinary involution $\tau$ composed with $\varsigma$.

**Proof.** The computation is the anti-multiplicativity of $\sigma$ on fixed elements; the fixed set of $\sigma$ is the image of the fixed set of $\tau$, $A^\sigma = \varsigma(A^\tau)$, because $\sigma(a) = a$ is equivalent to $\tau(\varsigma^{-1}(a)) = a$, that is to $\varsigma^{-1}(a) \in A^\tau$.

**Remark.** If $A$ is an $S$-algebra and the automorphism $\varsigma$ extends an automorphism $\varsigma_0$ of $S$ acting on the scalars, and if in addition $\sigma$ is $S$-semilinear in the module sense, $\sigma(sa) = \varsigma_0(s)\sigma(a)$, then $\sigma$ restricts to $\varsigma_0$ on the scalars and its fixed set is only an $S^{\varsigma_0}$-module; this is the semilinear involution of the linear structures of a later category, whose treatment is not repeated here.

## Examples

**(a) The trivial twist.** $\varsigma = \mathrm{id}$ gives the ordinary involutions of *Involutive Rings*: the transpose, the conjugate transpose, the group-ring inversion. Every statement above specialises to the known one.

**(b) The transpose twisted by a symmetric unit.** On $A = M_n(R)$ let $\varsigma(X) = GXG^{-1}$ be the inner automorphism of a unit $G$ with $G^{\mathrm t} = G$. The transpose $T(X) = X^{\mathrm t}$ satisfies

$$
T\varsigma(X) = G^{-\mathrm t}X^{\mathrm t}G^{\mathrm t} = G^{-1}X^{\mathrm t}G = \varsigma^{-1}T(X),
$$

since $G^{\mathrm t} = G$; so $T$ is a $\varsigma$-semilinear involution and $\tau = T\varsigma$ is the ordinary involution $X \mapsto G^{-1}X^{\mathrm t}G$. For $G$ with $G^{\mathrm t} = -G$, $G^2 = -1$ this $\tau$ is the symplectic involution of *Matrix Rings with an Involution*.

**(c) A group ring.** Let $A = K[G]$ and let $\varsigma$ be induced by an automorphism $\phi$ of $G$; the inversion map $\sigma(g) = g^{-1}$ extended linearly satisfies $\sigma\varsigma\sigma^{-1}(g) = \sigma\varsigma(g^{-1}) = \sigma(\phi(g)^{-1}) = \phi(g)$, so $\sigma\varsigma\sigma^{-1} = \varsigma$ and not $\varsigma^{-1}$ unless $\phi$ is the identity; thus inversion is $\varsigma$-semilinear only for the trivial twist, and the semilinear involutions of a group ring come from $\tau\varsigma^{-1}$ with $\tau$ the inverse composed with an anti-automorphism of $G$, as in *Involutions of a Group Ring*.

**(d) A quadratic twist.** On $A = K \times K$ with $\varsigma(a,b) = (b,a)$ of order two, set $\sigma(a,b) = (b,a)$; then $\sigma\varsigma = \mathrm{id}$-componentwise, $\sigma^2 = \mathrm{id}$ and $\sigma\varsigma = \varsigma\sigma = \varsigma$, so $\sigma$ is a $\varsigma$-semilinear involution with $\tau = \sigma\varsigma = \mathrm{id}$, the trivial ordinary involution.

**Example (the dihedral reading).** The relations $\sigma^2 = \mathrm{id}$, $\sigma\varsigma\sigma^{-1} = \varsigma^{-1}$ are the presentation of the dihedral group, so a ring with a $\varsigma$-semilinear involution is a ring with an action of a dihedral group, and the semilinear involution is the reflection of that action. This is the same reflection that *Reflections as Signed Two-Sided Operators on a Ring* reads as an operator, and the two are the element-level and the operator-level faces of one structure.

## Summary

A **$\varsigma$-semilinear involution** of a ring $A$ is an additive anti-multiplicative map $\sigma$ with $\sigma(1) = 1$, $\sigma^2 = \mathrm{id}$ and $\sigma\varsigma = \varsigma^{-1}\sigma$, where $\varsigma$ is an automorphism; the ordinary involution is the case $\varsigma = \mathrm{id}$. The composite $\tau = \sigma\varsigma$ is an **ordinary involution**, $\sigma = \tau\varsigma^{-1}$, and $\varsigma, \sigma$ generate the dihedral group $\langle \varsigma, \sigma\rangle$ with $\sigma^2 = \mathrm{id}$ and $\sigma\varsigma\sigma^{-1} = \varsigma^{-1}$; the semilinear involutions are parametrised by the ordinary involutions $\tau$ with $\tau\varsigma\tau = \varsigma^{-1}$, a condition that is automatic when $\varsigma^2 = \mathrm{id}$.

The naive identities fail for a nontrivial twist: $\sigma$ commutes with $\varsigma$ exactly when $\varsigma^2 = \mathrm{id}$, the composite $\sigma\varsigma$ has order two although $\sigma^2\varsigma^2 = \varsigma^2$, the map $\sigma$ commutes with $\varsigma^2$ exactly when $\varsigma^4 = \mathrm{id}$, and the fixed set $A^\sigma$ is an additive subgroup containing $1$ that fails to be a subring as for any involution and fails to be $\varsigma$-stable unless $\varsigma^2 = \mathrm{id}$ on it. Over a coefficient ring the semilinearity is genuine: $\sigma$ restricts to $\varsigma$ on the scalars and its fixed set is only linear over the fixed ring of $\varsigma$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A$ | Ring with $1 \neq 0$, not assumed commutative |
| $\varsigma$ | Automorphism of $A$; the twisting automorphism |
| $\sigma$ | $\varsigma$-semilinear involution |
| $\sigma\varsigma = \varsigma^{-1}\sigma$ | Semilinearity |
| $\tau = \sigma\varsigma$ | Attached ordinary involution; $\sigma = \tau\varsigma^{-1}$ |
| $\sigma^2 = \mathrm{id}$, $\sigma\varsigma\sigma^{-1} = \varsigma^{-1}$ | Dihedral relations; $\langle\varsigma,\sigma\rangle$ dihedral |
| $A^\sigma$ | Fixed set of $\sigma$; additive subgroup, not stable under $\varsigma$ in general |
| $\sigma\varsigma^2 = \varsigma^{-2}\sigma$ | $\sigma$ centralises $\varsigma^2$ iff $\varsigma^4 = \mathrm{id}$ |
| $G^{\mathrm t} = G$ | Condition on a unit making the transpose semilinear for the inner twist |

## Further Reading

- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for involutions of rings and the generalities that the semilinear case specialises.
- Nathan Jacobson, *Structure of Rings*, American Mathematical Society Colloquium Publications 37 (1964), for automorphisms and anti-automorphisms of a ring and their commutation relations.
- Serge Lang, *Algebra* (Springer, 3rd ed. 2002), for semilinear maps, twisted forms and the descent along an automorphism.
- Nicolas Bourbaki, *Algebra I*, Chapters 1–3 (Springer, 1998), for order-two automorphisms, their fixed rings and the dihedral actions they generate.
