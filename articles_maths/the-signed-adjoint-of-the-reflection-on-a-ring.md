
# __The Signed Adjoint of the Reflection on a Ring__

## Introduction

A **reflection** on a ring with a grade involution $\alpha$ and an involution $\sigma$ is the signed two-sided operator

$$
r_u(x) = u\,\alpha(x)\,u^{-1},
$$

the conjugation by a unit composed with the grade involution; on a graded algebra it is the reflection in the hyperplane of the elements fixed by $u$ up to the sign rule, and algebraically it is the signed sandwich $S_{u,u^{-1}}$. Its signed adjoint with respect to the twisted pairing is the sandwich $S_{\delta(u),\delta(u)^{-1}}$ with $\delta = \sigma\alpha$, and the reflection is **self-adjoint** exactly when the two sandwiches coincide, which happens exactly when $\delta(u)u^{-1}$ is central. The nondegenerate case is $\delta(u) = u$, a $\delta$-symmetric unit; the failure of self-adjointness occurs as soon as $\delta(u)u^{-1}$ is not central, and the reflection is then a signed operator whose adjoint is a genuinely different reflection.

This article reads the reflection as a signed operator, computes its square and its fixed set, identifies the self-adjointness condition and exhibits the failure in the degenerate case. It assumes *Reflections as Signed Two-Sided Operators on a Ring* for the operator, *The Signed Adjoint Sandwich on a Ring* for the adjoint, and *Involutions of the Endomorphism Ring* for the pairings. Throughout, $A$ is a ring with $1 \neq 0$ and an involution $\sigma$, $\tau$ is a $\sigma$-invariant trace, $\alpha$ is a grade involution commuting with $\sigma$, $\delta = \sigma\alpha$, the twisted pairing is $\{x,y\} = \tau(x\sigma(y))$, $u$ is a unit, and $r_u = S_{u,u^{-1}}$.

## The Reflection and its Square

**Theorem.** The operator $r_u$ is additive and bijective, and its square is the conjugation by $u\alpha(u)$:

$$
r_u^2(x) = u\alpha(u)\,x\,\bigl(u\alpha(u)\bigr)^{-1} .
$$

Hence $r_u$ is an **involution**, $r_u^2 = \mathrm{id}$, exactly when $u\alpha(u)$ is central; in that case it is a reflection, and its fixed set is $\{x : u\alpha(x) = xu\}$.

**Proof.** $r_u(r_u(x)) = u\,\alpha(u\alpha(x)u^{-1})\,u^{-1} = u\alpha(u)\,\alpha(\alpha(x))\,\alpha(u)^{-1}u^{-1} = u\alpha(u)\,x\,(u\alpha(u))^{-1}$, using that $\alpha$ is an automorphism and $\alpha^2 = \mathrm{id}$. The square is the identity exactly when the conjugating element $u\alpha(u)$ is central, and the fixed set is the equation $u\alpha(x)u^{-1} = x$.

**Remark (the degenerate square).** When $u\alpha(u)$ is not central the operator $r_u$ has order two only after reduction modulo the centre, and its square is the inner automorphism $\operatorname{inn}_{u\alpha(u)}$; the reflection is then not an involution on the ring but an operation of order two on the centre. The article keeps the involution case and notes the degenerate one at the boundary.

## The Signed Adjoint

**Theorem.** With respect to the twisted pairing,

$$
r_u^{*_\sigma} = S_{\delta(u),\delta(u)^{-1}} = r'_{\delta(u)} ,
$$

where $r'_v$ denotes the signed sandwich $S_{v,v^{-1}}$; the signed adjoint of a reflection is the reflection in $\delta(u)$.

**Proof.** This is $S_{u,u^{-1}}^{*_\sigma} = S_{\delta(u),\delta(u^{-1})}$ of *The Signed Adjoint Sandwich on a Ring*, together with $\delta(u^{-1}) = \delta(u)^{-1}$ because $\delta$ is an involution.

**Theorem (self-adjointness).** The reflection is self-adjoint, $r_u^{*_\sigma} = r_u$, exactly when

$$
S_{\delta(u),\delta(u)^{-1}} = S_{u,u^{-1}} \iff \delta(u) = \lambda u \ \text{ for some central } \lambda \iff \delta(u)u^{-1} \in Z(A) .
$$

In particular a **$\delta$-symmetric** unit, $\delta(u) = u$, gives a self-adjoint reflection, and so does $\delta(u) = \lambda u$ with $\lambda$ central.

**Proof.** The equality $S_{c,d} = S_{a,b}$ of two sandwiches as maps holds exactly when the rank-one tensors $c\otimes d$ and $a\otimes b$ agree, that is $c = \lambda a$, $d = \lambda^{-1}b$ for a central $\lambda$; with $a = d = u$, $b = c = u^{-1}$ (since $\delta(u^{-1}) = \delta(u)^{-1}$) this is $\delta(u) = \lambda u$. Dividing by $u$ gives the centrality of $\delta(u)u^{-1}$.

**Corollary (failure in the degenerate case).** If $\delta(u)u^{-1}$ is not central, the reflection is not self-adjoint: its adjoint is the reflection $r'_{\delta(u)}$, which conjugates by the different unit $\delta(u)$, and the two operators agree only on the elements commuting with $\delta(u)u^{-1}$. The self-adjointness therefore holds for the nondegenerate reflections, the $\delta$-symmetric units and their central multiples, and fails as soon as the unitarity defect leaves the centre.

**Proof.** The adjoint is $S_{\delta(u),\delta(u)^{-1}}$ and the two sandwiches differ when $\delta(u)u^{-1}$ is not central, by the same rank-one argument read in the converse direction; the agreement on the centraliser is the comparison of the two conjugations.

## Examples

**(a) The orthogonal reflection.** $A = M_n(\mathbb{R})$, $\sigma$ the transpose, $\alpha = \mathrm{id}$, $u$ a unit vector reflection $u = I - 2vv^{\mathrm t}$ with $v^{\mathrm t}v = 1$: $r_u(x) = uxu^{-1} = uxu$ is the reflection in the hyperplane orthogonal to $v$, it is an involution because $u^2 = I$ is central, and it is self-adjoint for the transpose because $\delta = \sigma = $ transpose fixes $u$ (the matrix $u$ is symmetric), so $r_u$ is self-adjoint and orthogonal.

**(b) The graded reflection.** With a $\mathbb{Z}/2$-grading and $\alpha$ the grade involution, a homogeneous unit $u$ satisfies $u\alpha(u) = \pm u^2$; the reflection is an involution when $u^2$ is central with the appropriate sign, and it is self-adjoint when $\sigma\alpha(u) = u$ up to a central factor. The sign $\pm$ is the degree of $u$, the sign rule of *Superalgebras and Graded Structures*.

**(c) The twisted case.** $A = \mathbb{C}$, $\sigma$ the conjugation, $\alpha = \mathrm{id}$, $u$ a complex number: $\delta(u) = \bar u$ and the reflection $r_u(x) = uxu^{-1} = x$ is the identity, self-adjoint trivially; for $u = i$, $\delta(u)u^{-1} = (-i)/i = -1$ is central and the reflection is self-adjoint.

**(d) The degenerate case.** For the same $A = M_n$ a non-symmetric unit $u$ has $\delta(u)u^{-1} = u^{\mathrm t}u^{-1}$ non-central in general, and the reflection $r_u$ is not self-adjoint: its adjoint is $r'_{u^{\mathrm t}}$, the reflection by the transpose of $u$. The failure is exactly the non-centrality of the defect.

## Summary

The reflection $r_u(x) = u\alpha(x)u^{-1} = S_{u,u^{-1}}$ has square the conjugation by $u\alpha(u)$, so it is an involution $\iff$ $u\alpha(u)$ is central, with fixed set $\{x : u\alpha(x) = xu\}$. Its signed adjoint with respect to the twisted pairing is $r_u^{*_\sigma} = S_{\delta(u),\delta(u)^{-1}}$, the reflection in $\delta(u) = \sigma\alpha(u)$; the reflection is **self-adjoint** exactly when $\delta(u)u^{-1}$ is central, in particular for the $\delta$-symmetric units and their central multiples. When $\delta(u)u^{-1}$ is not central the self-adjointness **fails** — the degenerate case — and the adjoint is the reflection in the different unit $\delta(u)$, agreeing with $r_u$ only on the centraliser of the defect.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $r_u(x) = u\alpha(x)u^{-1}$ | Reflection as a signed operator |
| $r_u = S_{u,u^{-1}}$ | The reflection is a signed sandwich |
| $r_u^2 = \operatorname{inn}_{u\alpha(u)}$ | Square; involution iff $u\alpha(u)$ central |
| $\operatorname{Fix}(r_u) = \{x : u\alpha(x) = xu\}$ | Fixed set |
| $r_u^{*_\sigma} = S_{\delta(u),\delta(u)^{-1}}$ | Signed adjoint |
| $\delta(u)u^{-1}\in Z(A)$ | Self-adjointness condition |
| $\delta(u) = u$ | Nondegenerate ($\delta$-symmetric) self-adjoint reflection |
| $r'_{\delta(u)}$ | Adjoint reflection in the degenerate case |

## Further Reading

- Nathan Jacobson, *Structure of Rings*, American Mathematical Society Colloquium Publications 37 (1964), for the conjugations and the reflections of the regular representation and their adjoints.
- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the self-adjoint and the skew operators of a ring with involution.
- Nicolas Bourbaki, *Algebra I*, Chapters 1–3 (Springer, 1998), for the reflections, the hyperplane of fixed vectors and the adjoint under a form.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, American Mathematical Society Colloquium Publications 44 (1998), for the reflections of a unitary group and their relation to the involution.
