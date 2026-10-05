# __The Signed Adjoint Sandwich on an Algebra__

## Introduction

The signed sandwich is the two-sided operator $S_{a,b}(x)=a\,\alpha(x)\,b$ built from a left multiplication, a right multiplication and a grade involution $\alpha$; it is the algebraic home of the reflections and of the conjugation by a unit, and the two-sided companion of the signed left multiplication. Its **signed adjoint** with respect to the twisted pairing $\{x,y\}=\tau(x\sigma(y))$ is again a signed sandwich, $S_{a,b}^{*_\sigma}=S_{\delta(a),\delta(b)}$ with $\delta=\sigma\alpha$, and the parameters are **not** reversed: the twisted adjoint of the signed sandwich is the signed sandwich of the $\delta$-images, in the same order. The sandwich is unitary, $S^{*_\sigma}S=SS^{*_\sigma}=\mathrm{id}$, exactly when the two products $\delta(a)\alpha(a)$ and $\alpha(b)\delta(b)$ are central and mutually inverse; for the reflection $b=\alpha(a)^{-1}$ this is the single condition that $\sigma(a)a$ be central and fixed by $\alpha$, and for the one-sided operator $b=1$ it is $\delta(a)\alpha(a)=1$.

This article computes the signed adjoint, the inverse and the composition of the sandwiched operators, derives the unitarity condition $u^{*}u=uu^{*}=1$ it defines, and prepares the reflection of *The Signed Adjoint of the Reflection on an Algebra*. It assumes *The Signed Sandwich on an Algebra* for the operator $S_{a,b}$, the signed conjugation $\rho_u=S_{u,u^{-1}}$ and the composition and inverse rules, *The Adjoint of the Left Multiplication on an Algebra* for the one-sided case, *Involutions of the Operator Algebra* and *The Adjoint in an Involutive Algebra* for the adjoint operation and the twisted pairing, *Frobenius Algebras* for the trace and the pairing, *Involutive Bilinear Algebras* for the involution and the grade involution, and *Unitary Elements of an Involutive Algebra* for the unitary elements and the group they form. The graded version of the same computation is *The Graded Adjoint Action on a Module over an Algebra*; the analytic reading of the unitary operators is Part II. This article stays inside Part I: no distance, norm, form with a norm, topology or limit.

Throughout, $k$ is a field of characteristic not two, $A$ is a finite-dimensional unital associative $k$-algebra, $\tau$ is a trace whose pairing $\langle x,y\rangle=\tau(xy)$ is nondegenerate, $\sigma$ is an involution of $A$ with $\tau(\sigma(x))=\tau(x)$, and $\alpha$ is an involutive automorphism of $A$ with $\alpha^{2}=\mathrm{id}$ commuting with $\sigma$ and preserving the trace, $\tau(\alpha(x))=\tau(x)$. The twist is $\delta=\sigma\alpha$, an anti-automorphism of order two; the twisted pairing is $\{x,y\}=\tau(x\sigma(y))$, the unsigned sandwich is $T_{a,b}(x)=axb$, the signed sandwich is $S_{a,b}(x)=a\alpha(x)b$, and the adjoints for the two pairings are $T^{*_\sigma}$ and $T^{*}$.

## The Signed Adjoint

**Theorem.** With respect to the twisted pairing,

$$
\{S_{a,b}x,y\}=\{x,\,S_{\delta(a),\delta(b)}y\}, \qquad \text{that is} \qquad S_{a,b}^{*_\sigma}=S_{\delta(a),\delta(b)} .
$$

The signed adjoint of a sandwich is the sandwich of the two $\delta$-images, with the order of the parameters **not** reversed, and the assignment $S_{a,b}\mapsto S_{\delta(a),\delta(b)}$ is an involution of the signed sandwich space.

*Proof.* Compute the left side, $\{S_{a,b}x,y\}=\tau(a\alpha(x)b\,\sigma(y))=\tau(\sigma(y)a\alpha(x)b)$ by cyclicity, and use the $\alpha$-invariance of the trace to write it as $\tau(\alpha(\sigma(y)a\alpha(x)b))=\tau(\alpha\sigma(y)\alpha(a)x\alpha(b))$; by the commutation $\alpha\sigma=\sigma\alpha$ this is $\tau(\sigma(\alpha(y))\alpha(a)x\alpha(b))=\tau(x\alpha(b)\sigma(\alpha(y))\alpha(a))$, again by cyclicity. On the other side, $\{x,S_{\delta(a),\delta(b)}y\}=\tau(x\,\sigma(\delta(a)\alpha(y)\delta(b)))=\tau(x\,\sigma(\delta(b))\sigma(\alpha(y))\sigma(\delta(a)))$, and $\sigma\delta=\sigma\sigma\alpha=\alpha$ gives $\sigma(\delta(a))=\alpha(a)$ and $\sigma(\delta(b))=\alpha(b)$, so this is the same expression. Hence the identity; the order-two property is $\delta^{2}=\mathrm{id}$, and the image is again a signed sandwich, so the signed sandwich space is stable.

**Proposition (the plain pairing).** With respect to the plain pairing,

$$
S_{a,b}^{*}=S_{\alpha(b),\alpha(a)},
$$

so the plain adjoint of a signed sandwich is the signed sandwich of the two $\alpha$-images with the order **reversed**; and the two adjoints are related by the conjugation of the operator algebra,

$$
S_{a,b}^{*_\sigma}=c_{\sigma}\bigl(S_{a,b}^{*}\bigr), \qquad c_{\sigma}(T)=\sigma T\sigma .
$$

*Proof.* For the plain pairing, $\langle S_{a,b}x,y\rangle=\tau(a\alpha(x)by)=\tau(bya\alpha(x))=\tau(\alpha(bya)x)$ by the $\alpha$-invariance and cyclicity, which is $\langle x,S_{\alpha(b),\alpha(a)}y\rangle$, since $\alpha(bya)=\alpha(b)\alpha(y)\alpha(a)$. The relation is the dictionary $T^{*_\sigma}=\sigma T^{*}\sigma$ of *The Adjoint in an Involutive Algebra*, applied to $T=S_{a,b}$: $\sigma S_{\alpha(b),\alpha(a)}\sigma(x)=\sigma(\alpha(b)\alpha(\sigma(x))\alpha(a))=\sigma(\alpha(a))\,\sigma(\alpha(\sigma(x)))\,\sigma(\alpha(b))=\delta(a)\alpha(x)\delta(b)$, using $\alpha\sigma=\sigma\alpha$ and $\sigma^{2}=\mathrm{id}$.

**Corollary (the grade involution is self-adjoint).** The grade involution itself is the sandwich $S_{1,1}=\alpha$, and it is self-adjoint for both pairings, $\alpha^{*}=\alpha$ and $\alpha^{*_\sigma}=\alpha$.

*Proof.* For the twisted pairing the theorem gives $S_{1,1}^{*_\sigma}=S_{\delta(1),\delta(1)}=S_{1,1}$, because $\delta(1)=1$; for the plain pairing the proposition gives $S_{1,1}^{*}=S_{\alpha(1),\alpha(1)}=S_{1,1}$, because $\alpha(1)=1$.

## The Inverse and the Composition

**Theorem.** The signed sandwich satisfies the composition rules of *The Signed Sandwich on an Algebra*,

$$
S_{a,b}S_{c,d}=T_{a\alpha(c),\,\alpha(d)b}, \qquad S_{a,b}^{-1}=S_{\alpha(a)^{-1},\,\alpha(b)^{-1}},
$$

and the unsigned sandwich $T_{c,d}$ is the identity exactly when $c$ is a central unit and $d=c^{-1}$.

*Proof.* The composition and the inverse are read from *The Signed Sandwich on an Algebra*: the product of two signed sandwiches is an unsigned sandwich, and the sandwich $S_{a,b}=T_{a,b}\alpha$ is invertible exactly when $a$ and $b$ are units. For the identity criterion, $T_{c,d}(x)=cxd=x$ for all $x$ gives $cd=1$ at $x=1$ and then $cx=xc$ for all $x$, that is $c$ central with $d=c^{-1}$; conversely a central $c$ with $d=c^{-1}$ gives $cxc^{-1}=x$.

The identity criterion is the reason a unitarity condition on a sandwich carries a central factor and not only $1$: the parameters $(a,b)$ and $(\lambda a,\lambda^{-1}b)$ with $\lambda$ central determine the same sandwich, so the unitarity is a condition modulo this scaling.

## The Unitarity Condition

**Theorem.** The signed sandwich is **unitary** for the twisted pairing, $S_{a,b}^{*_\sigma}S_{a,b}=S_{a,b}S_{a,b}^{*_\sigma}=\mathrm{id}$, exactly when

$$
c=\delta(a)\alpha(a) \text{ is central}, \qquad \text{and} \qquad d=\alpha(b)\delta(b)=c^{-1} .
$$

Equivalently, $S_{a,b}^{*_\sigma}=S_{a,b}^{-1}$, and the two products agree because the operators are square matrices over $k$.

*Proof.* By the theorem and the composition rule, $S_{a,b}^{*_\sigma}S_{a,b}=S_{\delta(a),\delta(b)}S_{a,b}=T_{c,d}$ with $c=\delta(a)\alpha(a)$ and $d=\alpha(b)\delta(b)$. The identity criterion of the preceding section says that $T_{c,d}=\mathrm{id}$ exactly when $c$ is central and $d=c^{-1}$, which is the displayed condition; the equivalence with $S^{*_\sigma}=S^{-1}$ is the inverse rule, and one of the two products being the identity suffices for the other because a one-sided inverse of a square matrix is two-sided.

**Corollary (the reflection).** For the signed conjugation $\rho_u=S_{u,u^{-1}}$ the unitarity condition is the single condition

$$
\rho_u \text{ is unitary} \iff \sigma(u)u \text{ is central and } \alpha\bigl(\sigma(u)u\bigr)=\sigma(u)u .
$$

so the reflection is a unitary operator exactly when $\sigma(u)u$ is an element of the even centre of the graded algebra.

*Proof.* With $b=\alpha(a)^{-1}$ and $a=u$ one computes $\alpha(b)\delta(b)=\alpha(\alpha(u)^{-1})\delta(\alpha(u)^{-1})=u^{-1}\delta(\alpha(u))^{-1}$ and $\delta(\alpha(u))=\sigma(u)$, so $d=(\sigma(u)u)^{-1}$; and $c=\delta(u)\alpha(u)=\alpha(\sigma(u)u)$ because $\alpha\sigma=\sigma\alpha$. The general condition $d=c^{-1}$ is then $\sigma(u)u=\alpha(\sigma(u)u)$, and the centrality of $c=\alpha(\sigma(u)u)$ is the centrality of $\sigma(u)u$.

**Corollary (the one-sided case).** For the signed left multiplication $S_{a,1}=\Lambda(a)$ the unitarity condition is

$$
S_{a,1} \text{ is unitary} \iff \delta(a)\alpha(a)=1 \iff \alpha(a) \text{ is a unitary element of } A ,
$$

since $\delta(a)=\sigma(\alpha(a))$ and the equation $\sigma(\alpha(a))\alpha(a)=1$ is the unitarity of $\alpha(a)$ for $\sigma$.

*Proof.* In the general condition $d=\alpha(1)\delta(1)=1$, so $c^{-1}=1$ and $c=1$, that is $\delta(a)\alpha(a)=1$; with $\delta=\sigma\alpha$ and $v=\alpha(a)$ this is $\sigma(v)v=1$, the unitarity of $v$. The full development of the one-sided operator is *The Signed Adjoint of the Left Multiplication on an Algebra*.

**Corollary (the unitary elements).** The **unitary elements** of the algebra for the anti-automorphism $\delta$ are the units $u$ with

$$
u^{*_\sigma}u=uu^{*_\sigma}=1, \qquad u^{*_\sigma}=\delta(u),
$$

and they form a subgroup of $A^{\times}$; the one-sided signed operators $\Lambda(u)$ with $u$ of this form are unitary, and the signed sandwiches with $a$ and $b$ satisfying the two conditions above are the unitary sandwiches.

*Proof.* The group statement is *Unitary Elements of an Involutive Algebra* applied to the involutive algebra $(A,\delta)$; the identification of the unitary one-sided operators is the corollary above with $\delta(u)=u^{-1}$, and the two-sided statement is the theorem.

## Examples

**(a) The matrix sandwich.** $A=M_n(k)$ with the transpose $\sigma$ and the grade involution $\alpha$ of a $\mathbb{Z}/2$-grading; the signed adjoint of $S_{a,b}(X)=a\alpha(X)b$ is $S_{\delta(a),\delta(b)}$ with $\delta=\sigma\alpha$, and for $\alpha=\mathrm{id}$ the adjoint of $X\mapsto aXb$ is $X\mapsto a^{\mathsf{T}}Xb^{\mathsf{T}}$, the transpose of the matrix parameters applied to $X$. The centrality condition is the scalarity of the parameter products.

**(b) The signed conjugation.** For $b=a^{-1}$ and $\alpha=\mathrm{id}$ the sandwich is the inner automorphism $x\mapsto axa^{-1}$, and its twisted adjoint is $x\mapsto\sigma(a)x\sigma(a)^{-1}$; it is self-adjoint only when $\sigma(a)$ is a central multiple of $a$, and unitary only when $\sigma(a)a$ is central, which for $\alpha=\mathrm{id}$ is the condition $\sigma(a)a\in Z(A)$.

**(c) The reflection and the odd element.** For a graded algebra and an odd element $u$ with $u^{2}$ central, the signed conjugation $\rho_u$ is a reflection with $\rho_u^{2}=\iota_{-u^{2}}$; it is unitary exactly when $\sigma(u)u$ is central and even. The Clifford algebra supplies the standard instance, and its metric reading is Part II and *Quadratic Forms and Clifford Algebras*.

**(d) The unit case.** $a=b=1$ gives the grade involution $S_{1,1}=\alpha$, whose signed adjoint is itself; it is unitary because $\alpha^{2}=\mathrm{id}$ and $\alpha$ is self-adjoint, which is the case $c=d=1$ of the general condition.

**(e) The central scaling.** The parameters $(a,b)$ and $(\lambda a,\lambda^{-1}b)$ with $\lambda$ central give the same signed sandwich when $\lambda$ is fixed by $\alpha$; the unitarity condition is invariant under the scaling, since $\delta(\lambda a)\alpha(\lambda a)=\lambda^{2}\delta(a)\alpha(a)$ and $\alpha(\lambda^{-1}b)\delta(\lambda^{-1}b)=\lambda^{-2}\alpha(b)\delta(b)$, the two products squaring back into inverse positions.

## Summary

For the twisted pairing the signed sandwich $S_{a,b}(x)=a\alpha(x)b$ has signed adjoint $S_{a,b}^{*_\sigma}=S_{\delta(a),\delta(b)}$ with $\delta=\sigma\alpha$, the parameters not reversed, while for the plain pairing the adjoint is $S_{\alpha(b),\alpha(a)}$, the parameters reversed and twisted by $\alpha$; the two are related by the conjugation $c_{\sigma}(T)=\sigma T\sigma$, and the grade involution $\alpha=S_{1,1}$ is self-adjoint for both. The sandwich is unitary, $S^{*_\sigma}S=SS^{*_\sigma}=\mathrm{id}$, exactly when the central elements $c=\delta(a)\alpha(a)$ and $d=\alpha(b)\delta(b)$ are inverse to one another; for the reflection $b=\alpha(a)^{-1}$ this reduces to the centrality and the $\alpha$-fixedness of $\sigma(a)a$, and for the one-sided operator $b=1$ to $\delta(a)\alpha(a)=1$, which is the unitarity of $\alpha(a)$. The unitary elements for $\delta$ satisfy $u^{*_\sigma}u=uu^{*_\sigma}=1$ with $u^{*_\sigma}=\delta(u)$ and form a subgroup of the units; the signed sandwich space is stable under the signed adjoint, and the identity is reached only up to the central scaling $(a,b)\sim(\lambda a,\lambda^{-1}b)$ of the parameters.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S_{a,b}(x)=a\alpha(x)b$ | the signed sandwich |
| $T_{a,b}(x)=axb$ | the unsigned sandwich |
| $\alpha$, $\sigma$, $\delta=\sigma\alpha$ | the grade involution, the involution, and their twist |
| $\{x,y\}=\tau(x\sigma(y))$ | the twisted pairing |
| $S_{a,b}^{*_\sigma}=S_{\delta(a),\delta(b)}$ | the signed adjoint; no reversal |
| $S_{a,b}^{*}=S_{\alpha(b),\alpha(a)}$ | the plain adjoint; reversal |
| $S_{a,b}S_{c,d}=T_{a\alpha(c),\alpha(d)b}$ | the composition rule |
| $S_{a,b}^{-1}=S_{\alpha(a)^{-1},\alpha(b)^{-1}}$ | the inverse |
| $T_{c,d}=\mathrm{id}\iff c\in Z(A),\ d=c^{-1}$ | the identity criterion |
| $c=\delta(a)\alpha(a)$, $d=\alpha(b)\delta(b)$ | the unitarity parameters |
| unitary $\iff c\in Z(A),\ d=c^{-1}$ | the unitarity condition |
| $\sigma(u)u\in Z(A)$, $\alpha$-fixed | the unitary reflections $\rho_u$ |
| $u^{*_\sigma}u=uu^{*_\sigma}=1$, $u^{*_\sigma}=\delta(u)$ | the unitary elements for $\delta$ |

## Further Reading

- Nathan Jacobson, *Structure of Rings*, American Mathematical Society Colloquium Publications 37 (1964), for the two-sided operators of the regular representation and their adjoints.
- I. N. Herstein, *Rings with Involution* (University of Chicago Press, 1976), for the adjoint of a sandwich, the unitary elements and the trace conditions.
- Nicolas Bourbaki, *Algebra I*, Chapters 1–3 (Springer, 1998), for adjoints under a sesquilinear pairing and the unitarity condition.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, American Mathematical Society Colloquium Publications 44 (1998), for the unitary groups of an algebra with involution.
