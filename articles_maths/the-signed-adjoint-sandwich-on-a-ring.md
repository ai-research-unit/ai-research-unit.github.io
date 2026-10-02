
# __The Signed Adjoint Sandwich on a Ring__

## Introduction

The **signed sandwich** is the two-sided operator $S_{a,b}(x) = a\,\alpha(x)\,b$ built from a left multiplication, a right multiplication and a grade involution $\alpha$ of a ring with an involution $\sigma$; it is the two-sided companion of the signed left multiplication and the algebraic home of the reflections and of the conjugation by a unit. Its **signed adjoint** with respect to the twisted pairing $\{x,y\} = \tau(x\sigma(y))$ is again a signed sandwich, $S_{a,b}^{*_\sigma} = S_{\delta(a),\delta(b)}$ with $\delta = \sigma\alpha$, and the sandwich is **unitary**, $S_{a,b}^{*_\sigma}S_{a,b} = S_{a,b}S_{a,b}^{*_\sigma} = \mathrm{id}$, exactly under the two conditions $\delta(a)\alpha(a) = 1$ and $\alpha(b)\delta(b) = 1$; in the case of a reflection, $b = \alpha(a)^{-1}$, these reduce to the unitarity of $a$ and of $\alpha(a)$.

This article computes the signed adjoint, the inverse and the composition of the sandwiched operators, derives the unitarity condition $u^{*}u = uu^{*} = 1$ it defines, and prepares the reflection of *The Signed Adjoint of the Reflection on a Ring*. It assumes *The Signed Sandwich on a Ring* for the operator, *Involutions of the Endomorphism Ring* for the pairings and the adjoint, and *The Adjoint of the Left Multiplication on a Ring* for the one-sided case. Throughout, $A$ is a ring with $1 \neq 0$ and an involution $\sigma$, $\tau$ is a $\sigma$-invariant trace, $\alpha$ is a grade involution commuting with $\sigma$, $\delta = \sigma\alpha$, the twisted pairing is $\{x,y\} = \tau(x\sigma(y))$, and $S_{a,b}(x) = a\alpha(x)b$.

## The Signed Adjoint

**Theorem.** With respect to the twisted pairing,

$$
\{S_{a,b}x, y\} = \{x, S_{\delta(a),\delta(b)}y\} , \qquad \text{that is } S_{a,b}^{*_\sigma} = S_{\delta(a),\delta(b)} .
$$

The signed adjoint of a sandwich is the sandwich of the two $\delta$-images, with the order of the parameters **not** reversed, and it is an involution of the algebra of sandwiched operators.

**Proof.** $\{S_{a,b}x,y\} = \tau(a\alpha(x)b\,\sigma(y)) = \tau(\sigma(y)a\alpha(x)b)$; cyclically $= \tau(\alpha(x)b\sigma(y)a)$, and using $\tau\circ\alpha = \tau$ with $\alpha^2 = \mathrm{id}$ this is $\tau(x\,\alpha(b\sigma(y)a)) = \tau(x\,\alpha(b)\alpha(\sigma(y))\alpha(a)) = \tau(x\,\alpha(b)\sigma(\alpha(y))\alpha(a))$, the last step by the commutation of $\alpha$ and $\sigma$. On the other side, $\{x,S_{\delta(a),\delta(b)}y\} = \tau(x\,\sigma(\delta(a)\alpha(y)\delta(b))) = \tau(x\,\sigma(\delta(b))\,\sigma(\alpha(y))\,\sigma(\delta(a)))$; since $\sigma\delta = \sigma\sigma\alpha = \alpha$, one has $\sigma(\delta(a)) = \alpha(a)$ and $\sigma(\delta(b)) = \alpha(b)$, so this is $\tau(x\,\alpha(b)\sigma(\alpha(y))\alpha(a))$, matching the first expression term by term. Hence $S_{a,b}^{*_\sigma} = S_{\delta(a),\delta(b)}$, and the order-two property is $\delta^2 = \mathrm{id}$.

**Proposition (inverse and composition).** The sandwich $S_{a,b}$ is invertible exactly when $a$ and $b$ are units, with

$$
S_{a,b}^{-1} = S_{\alpha(a)^{-1},\alpha(b)^{-1}} ,
$$

and the composition of two sandwiches is a two-sided operator but not a sandwich,

$$
S_{c,d}\circ S_{a,b} = L_{c\alpha(a)}\,R_{\alpha(b)d} .
$$

**Proof.** $S_{c,d}(S_{a,b}(x)) = c\,\alpha(a\alpha(x)b)\,d = c\alpha(a)\,\alpha(\alpha(x))\,\alpha(b)d = c\alpha(a)\,x\,\alpha(b)d$; the inverse is the case in which the two coefficients are $1$, and the composition formula is the same computation.

## The Unitarity Condition

**Theorem.** The sandwich is **unitary** for the twisted pairing,

$$
S_{a,b}^{*_\sigma}S_{a,b} = S_{a,b}S_{a,b}^{*_\sigma} = \mathrm{id} ,
$$

exactly when

$$
\delta(a)\alpha(a) = 1 \quad \text{and} \quad \alpha(b)\delta(b) = 1 .
$$

For the sandwich with $b = \alpha(a)^{-1}$ these are the two conditions $\sigma(\alpha(a))\alpha(a) = 1$ and $\sigma(a)a = 1$, that is the unitarity of $a$ and of $\alpha(a)$; the second is the condition $a^{*_\sigma}a = 1$ with $a^{*_\sigma} = \delta(a)$.

**Proof.** By the theorem and the composition formula, $S_{a,b}^{*_\sigma}S_{a,b} = S_{\delta(a),\delta(b)}\circ S_{a,b} = L_{\delta(a)\alpha(a)}R_{\alpha(b)\delta(b)}$, which is the identity exactly when both coefficients are $1$ and both are central, that is under the two conditions. For $b = \alpha(a)^{-1}$ one has $\alpha(b) = a^{-1}$ and $\delta(b) = \delta(\alpha(a)^{-1}) = \delta(\alpha(a))^{-1} = \sigma(\alpha(\alpha(a)))^{-1} = \sigma(a)^{-1}$, so $\alpha(b)\delta(b) = a^{-1}\sigma(a)^{-1} = (\sigma(a)a)^{-1}$, giving $\sigma(a)a = 1$; the first condition is the same statement for $\alpha(a)$.

**Corollary (the unitary elements).** The **unitary elements** of $A$ with respect to $\sigma$ are the units $u$ with

$$
u^{*_\sigma}u = uu^{*_\sigma} = 1, \qquad u^{*_\sigma} = \delta(u) = \sigma(\alpha(u)) ;
$$

they form a subgroup of $A^\times$, and the sandwiches $S_{a,\alpha(a)^{-1}}$ with $a$ and $\alpha(a)$ unitary are the unitary sandwiches. The one-sided case of *The Signed Adjoint of the Left Multiplication on a Ring* is $b = 1$, and the reflection of *The Signed Adjoint of the Reflection on a Ring* is $b = u^{-1}$.

**Proof.** The subgroup statement is *Involutive Rings*; the identification of the unitary sandwiches is the theorem, and the specialisations to $b = 1$ and to $b = u^{-1}$ are immediate.

## Examples

**(a) The matrix sandwich.** $A = M_n$ with the transpose $\sigma$ and the grade involution $\alpha$ from a $\mathbb{Z}/2$-grading; $S_{a,b}(X) = a\alpha(X)b$, and its signed adjoint is $S_{\delta(a),\delta(b)}$ with $\delta = \sigma\alpha$. For $\alpha = \mathrm{id}$ the sandwich is $X\mapsto aXb$ and its signed adjoint is $X\mapsto\sigma(a)X\sigma(b)$, which for the transpose is $X\mapsto a^{\mathrm t}Xb^{\mathrm t}$.

**(b) The conjugation.** For $b = a^{-1}$ and $\alpha = \mathrm{id}$, $S_{a,a^{-1}}(x) = axa^{-1}$ is the inner automorphism, and its signed adjoint is $S_{\sigma(a),\sigma(a)^{-1}}$; the inner automorphism is self-adjoint for the twisted pairing exactly when $\sigma(a) = \lambda a$ with $\lambda$ central.

**(c) The reflection.** For $b = u^{-1}$ and a general $\alpha$ the sandwich is the reflection $r_u$; it is unitary exactly when $u$ and $\alpha(u)$ are unitary, and it is self-adjoint under the weaker condition of *The Signed Adjoint of the Reflection on a Ring*.

**(d) The unit case.** $a = b = 1$ gives the grade involution $S_{1,1} = \alpha$, whose signed adjoint is $S_{\delta(1),\delta(1)} = \alpha$; $\alpha$ is self-adjoint for the twisted pairing, and its unitarity is the condition $\alpha(1)\delta(1) = 1$, automatic.

## Summary

The signed sandwich $S_{a,b}(x) = a\alpha(x)b$ has signed adjoint $S_{a,b}^{*_\sigma} = S_{\delta(a),\delta(b)}$ with respect to the twisted pairing $\{x,y\} = \tau(x\sigma(y))$, where $\delta = \sigma\alpha$; the parameters are **not** swapped. The inverse is $S_{\alpha(a)^{-1},\alpha(b)^{-1}}$, the composition is $S_{c,d}\circ S_{a,b} = L_{c\alpha(a)}R_{\alpha(b)d}$, and the sandwich is unitary, $S^{*}S = SS^{*} = \mathrm{id}$, exactly when $\delta(a)\alpha(a) = 1$ and $\alpha(b)\delta(b) = 1$; for $b = \alpha(a)^{-1}$ these are the unitarity of $a$ and of $\alpha(a)$, the latter being $a^{*_\sigma}a = 1$ with $a^{*_\sigma} = \delta(a)$. The unitary elements form a subgroup, and the one-sided and reflection cases of the following articles are the specialisations $b = 1$ and $b = u^{-1}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S_{a,b}(x) = a\alpha(x)b$ | Signed sandwich |
| $\alpha$, $\delta = \sigma\alpha$ | Grade involution and its twist by $\sigma$ |
| $\{x,y\} = \tau(x\sigma(y))$ | Twisted pairing |
| $S_{a,b}^{*_\sigma} = S_{\delta(a),\delta(b)}$ | Signed adjoint; no swap |
| $S_{a,b}^{-1} = S_{\alpha(a)^{-1},\alpha(b)^{-1}}$ | Inverse |
| $S_{c,d}\circ S_{a,b} = L_{c\alpha(a)}R_{\alpha(b)d}$ | Composition; not a sandwich |
| $\delta(a)\alpha(a) = 1$, $\alpha(b)\delta(b) = 1$ | Unitarity condition |
| $u^{*_\sigma}u = uu^{*_\sigma} = 1$ | Unitary elements, $u^{*_\sigma} = \delta(u)$ |
| $S_{a,\alpha(a)^{-1}}$ | Unitary sandwich form |

## Further Reading

- Nathan Jacobson, *Structure of Rings*, American Mathematical Society Colloquium Publications 37 (1964), for the one-sided and two-sided operators of the regular representation and their adjoints.
- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the adjoint of a sandwich, the unitary elements and the trace conditions.
- Nicolas Bourbaki, *Algebra I*, Chapters 1–3 (Springer, 1998), for adjoints under a sesquilinear pairing and the unitarity condition.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, American Mathematical Society Colloquium Publications 44 (1998), for the unitary groups and the unitarity condition of an involution.
