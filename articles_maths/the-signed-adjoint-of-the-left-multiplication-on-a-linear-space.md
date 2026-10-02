# __The Signed Adjoint of the Left Multiplication on a Linear Space__

## Introduction

The signed left multiplication $\Lambda^{\alpha}_{a} = L_a\circ\alpha$ is the signed sandwich with right factor one, and its adjoint with respect to the trace pairing is the signed right multiplication $R_{\alpha(a)}\circ\alpha$, the operator $Y \mapsto \alpha(Y)\alpha(a)$: the adjoint of the one-sided signed operator is again one-sided, with the parameter imaged by the grade involution and the side exchanged. The article records the computation, its relation to the adjoint of the general signed sandwich, the unsigned case, and the self-adjointness and unitarity criteria of the one-sided operators.

*The Signed Left Multiplication on a Linear Space* supplies $\Lambda^{\alpha}_{a}$ and its laws, *The Signed Adjoint Sandwich on a Linear Space* supplies the adjoint computation of the signed family, of which this is the case $b=1$, and *The Adjoint of the Left Multiplication on a Linear Space* supplies the unsigned trace-adjoint $(L_a)^{\dagger}=R_a$ and the compatibility with an element involution. The forms are Part II.

Throughout, $F$ is a field with $2 \neq 0$, $V$ is a finite-dimensional $F$-linear space, $E = \operatorname{End}_F(V)$, $\alpha$ is the grade involution of $E$, an algebra automorphism of order two with $\alpha(X)=TXT$, and $\Lambda^{\alpha}_{a}(X)=a\alpha(X)$. The trace pairing is $\langle X,Y\rangle=\operatorname{tr}(XY)$ and ${}^{\dagger}$ is its adjoint.

## The Adjoint

**Proposition.** For every $a \in E$,

$$
\bigl(\Lambda^{\alpha}_{a}\bigr)^{\dagger} = \Theta^{\alpha}_{1,\alpha(a)} = R_{\alpha(a)}\circ\alpha , \qquad
\bigl(\Lambda^{\alpha}_{a}\bigr)^{\dagger}(Y) = \alpha(Y)\,\alpha(a) .
$$

**Proof.** $\langle\Lambda^{\alpha}_{a}X,Y\rangle = \operatorname{tr}(a\alpha(X)Y) = \operatorname{tr}(\alpha(X)Ya) = \langle\alpha(X),Ya\rangle = \langle X,\alpha(Ya)\rangle = \langle X,\alpha(Y)\alpha(a)\rangle$, using the $\alpha$-invariance of the trace pairing and the multiplicativity $\alpha(Ya)=\alpha(Y)\alpha(a)$; the adjoint is unique because the trace pairing is non-degenerate. This is the case $b=1$ of the adjoint formula $(\Theta^{\alpha}_{a,b})^{\dagger}=\Theta^{\alpha}_{\alpha(b),\alpha(a)}$.

**Corollary (relation to the signed sandwich).** Since $\Lambda^{\alpha}_{a}=\Theta^{\alpha}_{a,1}$, its adjoint is $\Theta^{\alpha}_{\alpha(1),\alpha(a)}=\Theta^{\alpha}_{1,\alpha(a)}$; taking adjoints twice returns $\Lambda^{\alpha}_{a}$ because $\Theta^{\alpha}_{\alpha(a),\alpha(1)}=\Theta^{\alpha}_{\alpha(a),1}$ and $\alpha^2=\mathrm{id}$, in agreement with the order-two property.

**Corollary (the unsigned case).** For $\alpha=\mathrm{id}$ the signed left multiplication is the left multiplication and the statement reads $(L_a)^{\dagger}=R_a$, the trace-adjointness of *The Adjoint of the Left Multiplication on a Linear Space*; the signed statement is the image of the unsigned one under the grade involution.

**Proof.** $\Theta^{\mathrm{id}}_{1,a}=R_a$ and $\Lambda^{\mathrm{id}}_{a}=L_a$.

**Corollary (self-adjointness).** $\Lambda^{\alpha}_{a}$ is self-adjoint, $(\Lambda^{\alpha}_{a})^{\dagger}=\Lambda^{\alpha}_{a}$, if and only if $a$ is central and even, $a \in Z(E)$ and $\alpha(a)=a$.

**Proof.** $\Theta^{\alpha}_{1,\alpha(a)}=\Theta^{\alpha}_{a,1}$ says $\alpha(Y)\alpha(a)=a\alpha(Y)$ for all $Y$, so $a$ commutes with $\alpha(E)=E$ and $a$ is central; setting $Y=1$ gives $\alpha(a)=a$.

## Unitarity and the Element Involution

**Corollary (unitarity).** $\Lambda^{\alpha}_{a}$ is unitary for the trace pairing if and only if $\alpha(a)$ is a central involution of $E$; the condition is $u^{*}u=uu^{*}=1$ with $u=\alpha(a)$ in the self-adjoint case, when $a$ is even.

**Proof.** This is the unitarity criterion of *The Signed Adjoint Sandwich on a Linear Space* with $b=1$: the parameter of the criterion is $\alpha(1)\alpha(a)=\alpha(a)$.

**Remark (the compatibility with an element involution).** If $E$ carries a pairing-based involution ${}^{*}$ and the induced operator involution $S^{*}(X)=S(X^{*})^{*}$ of *The Adjoint of the Left Multiplication on a Linear Space*, the unsigned left multiplications satisfy $L_a^{*}=R_{a^{*}}$; the signed ones satisfy $\bigl(\Lambda^{\alpha}_{a}\bigr)^{*}(X)=\alpha(X^{*})\,a^{*}$, which is the signed counterpart, and the two computations differ by the grade involution. When the element involution is the identity the signed statement reduces to the unsigned one.

## Summary

The adjoint of the signed left multiplication $\Lambda^{\alpha}_{a}$ with respect to the trace pairing is $\Theta^{\alpha}_{1,\alpha(a)}=R_{\alpha(a)}\alpha$, the signed right multiplication by $\alpha(a)$; this is the case $b=1$ of the adjoint of the signed sandwich, $(\Theta^{\alpha}_{a,b})^{\dagger}=\Theta^{\alpha}_{\alpha(b),\alpha(a)}$, and taking adjoints twice returns the operator because $\alpha$ has order two. For $\alpha=\mathrm{id}$ the statement reduces to the trace-adjointness $(L_a)^{\dagger}=R_a$ of the unsigned theory. The one-sided operator is self-adjoint exactly for central even $a$, and unitary exactly when $\alpha(a)$ is a central involution, the self-adjoint case being the element condition $u^{*}u=uu^{*}=1$ with $u=\alpha(a)$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F$, $V$, $E$ | the field, the space, the endomorphism algebra |
| $\alpha$ | the grade involution, $\alpha(X)=TXT$ |
| $\Lambda^{\alpha}_{a}(X)=a\alpha(X)$ | the signed left multiplication |
| $\langle X,Y\rangle=\operatorname{tr}(XY)$ | the trace pairing |
| ${}^{\dagger}$ | the trace-adjoint |
| $(\Lambda^{\alpha}_{a})^{\dagger}=\Theta^{\alpha}_{1,\alpha(a)}=R_{\alpha(a)}\alpha$ | the adjoint computation |
| $(\Theta^{\alpha}_{a,b})^{\dagger}=\Theta^{\alpha}_{\alpha(b),\alpha(a)}$ | the signed sandwich case |
| $Z(E)$ | the centre of $E$ |

## Further Reading

- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for the trace form and the adjoint of a one-sided operator.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for one-sided operators and their adjoints.
- Tsit-Yuen Lam, *A First Course in Noncommutative Rings* (Springer, 2nd ed. 2001), for the left and right multiplications and the trace pairing.
