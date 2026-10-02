# __The Signed Adjoint Sandwich on a Linear Space__

## Introduction

The trace pairing of $E = \operatorname{End}_F(V)$ is invariant under the grade involution, $\operatorname{tr}(\alpha(X)Z) = \operatorname{tr}(X\alpha(Z))$, and that invariance computes the adjoint of every signed sandwich: the adjoint of $\Theta^{\alpha}_{a,b}$ is the signed sandwich $\Theta^{\alpha}_{\alpha(b),\alpha(a)}$, obtained by applying the grade involution to both parameters and exchanging them. The adjoint of the signed left multiplication, which is the case $b=1$, is therefore the signed right multiplication $\Theta^{\alpha}_{1,\alpha(a)}$, the unsigned case being the familiar adjointness of the left and right multiplications. The list includes a unitarity criterion: a signed sandwich is unitary exactly when the product $\alpha(b)\alpha(a)$ of the two parameters is a central involution, which is the signed form of the element condition $u^{*}u = uu^{*} = 1$.

*The Signed Sandwich on a Linear Space* and *The Signed Left Multiplication on a Linear Space* supply the operators, *The Adjoint of the Left Multiplication on a Linear Space* supplies the trace pairing and its compatibility with the element involution, and *The Adjoint of an Endomorphism* supplies the adjoint of a single endomorphism. The reflection case is *The Signed Adjoint of the Reflection on a Linear Space*, the one-sided case is *The Signed Adjoint of the Left Multiplication on a Linear Space*, and the module-level variant is *The Graded Adjoint Action on a Module over a Linear Space*. The forms are Part II.

Throughout, $F$ is a field with $2 \neq 0$, $V$ is a finite-dimensional $F$-linear space, $E = \operatorname{End}_F(V)$, $\alpha$ is the grade involution of $E$, an algebra automorphism of order two with $\alpha(X)=TXT$, $T^2=\mathrm{id}$, and $\Phi_{a,b}(X)=aXb$, $\Theta^{\alpha}_{a,b}(X)=a\alpha(X)b$ are the sandwiches, $\Lambda^{\alpha}_{a}(X)=a\alpha(X)$ the signed left multiplication. The trace pairing is $\langle X,Y\rangle=\operatorname{tr}(XY)$ and ${}^{\dagger}$ is its adjoint.

## The Adjoint of a Signed Sandwich

**Lemma (the trace pairing is $\alpha$-invariant).** For all $X,Z \in E$, $\langle\alpha(X),Z\rangle = \langle X,\alpha(Z)\rangle$, that is, $\operatorname{tr}(\alpha(X)Z) = \operatorname{tr}(X\alpha(Z))$.

**Proof.** Write $\alpha(X) = TXT$ with $T^2=\mathrm{id}$. Then $\operatorname{tr}(TXTZ) = \operatorname{tr}(XTZT)$ by the cyclic invariance, and $TZT = \alpha(Z)$.

**Proposition (the adjoint of the signed sandwich).** For all $a,b \in E$,

$$
\bigl(\Theta^{\alpha}_{a,b}\bigr)^{\dagger} = \Theta^{\alpha}_{\alpha(b),\alpha(a)} , \qquad
\bigl(\Theta^{\alpha}_{a,b}\bigr)^{\dagger}(Y) = \alpha(b)\,\alpha(Y)\,\alpha(a) .
$$

**Proof.** $\langle\Theta^{\alpha}_{a,b}(X),Y\rangle = \operatorname{tr}(a\alpha(X)bY) = \operatorname{tr}(\alpha(X)\,bYa) = \langle\alpha(X),\,bYa\rangle = \langle X,\,\alpha(bYa)\rangle = \langle X,\,\alpha(b)\alpha(Y)\alpha(a)\rangle$, using the $\alpha$-invariance of the trace pairing in the middle and the multiplicativity $\alpha(bYa)=\alpha(b)\alpha(Y)\alpha(a)$; the adjoint is unique because the trace pairing is non-degenerate.

**Corollary (the adjoint of the unsigned sandwich).** For $\alpha=\mathrm{id}$ the statement is $(\Phi_{a,b})^{\dagger}=\Phi_{b,a}$, the adjoint of an unsigned sandwich being the sandwich with the two factors exchanged; in particular the inner automorphism $\mathrm{Ad}_a=\Phi_{a,a^{-1}}$ has adjoint $\Phi_{a^{-1},a}=\mathrm{Ad}_{a^{-1}}$.

**Proof.** Setting $\alpha=\mathrm{id}$ gives $\Theta^{\mathrm{id}}_{b,a}=\Phi_{b,a}$; the inner case is $b=a^{-1}$.

**Corollary (self-adjointness).** $\Theta^{\alpha}_{a,b}$ is self-adjoint, $(\Theta^{\alpha}_{a,b})^{\dagger}=\Theta^{\alpha}_{a,b}$, exactly when $b=\alpha(a)$; the self-adjoint signed sandwiches are those of the form $\Theta^{\alpha}_{a,\alpha(a)}$.

**Proof.** $\Theta^{\alpha}_{\alpha(b),\alpha(a)}=\Theta^{\alpha}_{a,b}$ is equivalent to the two equations $\alpha(b)=a$ and $\alpha(a)=b$, which together say $b=\alpha(a)$.

## The Adjoint of the Signed Left Multiplication

**Proposition.** For every $a \in E$,

$$
\bigl(\Lambda^{\alpha}_{a}\bigr)^{\dagger} = \Theta^{\alpha}_{1,\alpha(a)} = R_{\alpha(a)}\circ\alpha , \qquad
\bigl(\Lambda^{\alpha}_{a}\bigr)^{\dagger}(Y) = \alpha(Y)\,\alpha(a) .
$$

**Proof.** The signed left multiplication is $\Theta^{\alpha}_{a,1}$, so the previous proposition gives the adjoint $\Theta^{\alpha}_{\alpha(1),\alpha(a)}=\Theta^{\alpha}_{1,\alpha(a)}$, whose value at $Y$ is $\alpha(Y)\alpha(a)$; this is the right multiplication by $\alpha(a)$ after the grade involution. For $\alpha=\mathrm{id}$ it is $R_a$, in agreement with $(L_a)^{\dagger}=R_a$ of *The Adjoint of the Left Multiplication on a Linear Space*.

**Corollary (the unsigned case).** For $\alpha=\mathrm{id}$ the signed left multiplication is the left multiplication and the adjoint is the right multiplication, $(\Phi_{a,1})^{\dagger}=\Phi_{1,a}=R_a$; the signed case is the image of the unsigned one under the grade involution, $(\Lambda^{\alpha}_{a})^{\dagger}=\Theta^{\alpha}_{1,\alpha(a)}$.

**Proof.** Immediate from the proposition and $\Theta^{\mathrm{id}}_{a,1}=L_a$.

**Corollary (self-adjointness of the one-sided operators).** $\Lambda^{\alpha}_{a}$ is self-adjoint if and only if $a$ is central and even, $a\in Z(E)$ and $\alpha(a)=a$.

**Proof.** $\Theta^{\alpha}_{1,\alpha(a)}=\Theta^{\alpha}_{a,1}$ says $\alpha(Y)\alpha(a)=a\alpha(Y)$ for all $Y$, that is $a$ commutes with $\alpha(E)=E$, whence $a$ is central, and setting $Y=1$ gives $\alpha(a)=a$.

## Unitarity

**Theorem (the unitarity criterion of a signed sandwich).** For all $a,b \in E$,

$$
\bigl(\Theta^{\alpha}_{a,b}\bigr)^{\dagger}\Theta^{\alpha}_{a,b} = \Phi_{u,u}, \qquad u = \alpha(b)\alpha(a) ,
$$

so $\Theta^{\alpha}_{a,b}$ is unitary for the trace pairing — $(\Theta^{\alpha}_{a,b})^{\dagger}\Theta^{\alpha}_{a,b}=\mathrm{id}$ and the same on the other side — if and only if $u=\alpha(b)\alpha(a)$ is a central involution of $E$.

**Proof.** $\Theta^{\alpha}_{\alpha(b),\alpha(a)}\Theta^{\alpha}_{a,b}(X) = \alpha(b)\alpha(a)\,\alpha(\alpha(X))\,\alpha(b)\alpha(a)$ by applying the composition law of *The Signed Sandwich on a Linear Space* twice; the two inner images cancel and the result is the unsigned sandwich $uXu$ with $u=\alpha(b)\alpha(a)$. The sandwich $X\mapsto uXu$ is the identity exactly when $u^2=1$ and $u$ is central.

**Corollary (the unitarity of the signed left multiplication).** $\Lambda^{\alpha}_{a}=\Theta^{\alpha}_{a,1}$ is unitary exactly when $\alpha(a)$ is a central involution; in particular, writing $u=\alpha(a)$ and assuming $a$ even, so that $u$ is self-adjoint, the condition is $u^{*}u = uu^{*} = 1$ with $u$ an involution of $E$.

**Proof.** The theorem with $b=1$ gives $u=\alpha(1)\alpha(a)=\alpha(a)$.

**Corollary (the signed inner sandwich).** $\Theta^{\alpha}_{a,a^{-1}}$ is unitary exactly when $\alpha(a^{-1})\alpha(a)$ is a central involution; this product is $\alpha(a)^{-1}\alpha(a)=1$, so the signed inner sandwich is always unitary, and its adjoint is $\Theta^{\alpha}_{\alpha(a)^{-1},\alpha(a)}$, which is the identity exactly when $a$ is central.

**Proof.** For $(a,b)=(a,a^{-1})$ the parameter $u$ of the theorem is $\alpha(a^{-1})\alpha(a)=1$; the adjoint is the corollary on self-adjointness and the adjoint formula.

## Summary

The trace pairing of $E$ is invariant under the grade involution, $\operatorname{tr}(\alpha(X)Z)=\operatorname{tr}(X\alpha(Z))$, and computes the adjoints of the signed family: $(\Theta^{\alpha}_{a,b})^{\dagger}=\Theta^{\alpha}_{\alpha(b),\alpha(a)}$, so the adjoint of a signed sandwich is a signed sandwich with the parameters exchanged and imaged under $\alpha$, and the unsigned case is $(\Phi_{a,b})^{\dagger}=\Phi_{b,a}$. The adjoint of the signed left multiplication is $(\Lambda^{\alpha}_{a})^{\dagger}=\Theta^{\alpha}_{1,\alpha(a)}=R_{\alpha(a)}\alpha$, whose unsigned case is $(L_a)^{\dagger}=R_a$. The self-adjoint signed sandwiches are those with $b=\alpha(a)$, and a signed left multiplication is self-adjoint exactly for central even $a$. A signed sandwich is unitary exactly when $\alpha(b)\alpha(a)$ is a central involution, so a signed left multiplication is unitary exactly when $\alpha(a)$ is a central involution, and the signed inner sandwich is always unitary with adjoint the signed sandwich by the inverse of $\alpha(a)$. In the self-adjoint case the criterion is the element condition $u^{*}u=uu^{*}=1$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F$, $V$, $E$ | the field, the space, the endomorphism algebra |
| $\alpha$ | the grade involution, $\alpha(X)=TXT$ |
| $\langle X,Y\rangle=\operatorname{tr}(XY)$ | the trace pairing |
| ${}^{\dagger}$ | the adjoint with respect to the trace pairing |
| $\Theta^{\alpha}_{a,b}(X)=a\alpha(X)b$ | the signed sandwich |
| $\Lambda^{\alpha}_{a}(X)=a\alpha(X)$ | the signed left multiplication |
| $(\Theta^{\alpha}_{a,b})^{\dagger}=\Theta^{\alpha}_{\alpha(b),\alpha(a)}$ | the adjoint of a signed sandwich |
| $(\Lambda^{\alpha}_{a})^{\dagger}=\Theta^{\alpha}_{1,\alpha(a)}$ | the adjoint of a signed left multiplication |
| $(\Theta^{\alpha}_{a,b})^{\dagger}\Theta^{\alpha}_{a,b}=\Phi_{u,u}$, $u=\alpha(b)\alpha(a)$ | the unitarity criterion |
| $(\Phi_{a,b})^{\dagger}=\Phi_{b,a}$ | the unsigned case |

## Further Reading

- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for the trace form, the adjoint and the involutions of an algebra.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for adjoints and unitarity with respect to an involution.
- Tsit-Yuen Lam, *A First Course in Noncommutative Rings* (Springer, 2nd ed. 2001), for the trace pairing and the left and right multiplications.
