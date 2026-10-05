# __The Signed Sandwich on a Linear Space__

## Introduction

The endomorphism algebra $E = \operatorname{End}_F(V)$ has a multiplication, and with it the two-sided operators $X \mapsto aXb$ and their **signed** variants $X \mapsto a\alpha(X)b$, where $\alpha$ is the grade involution of $E$, the order-two algebra automorphism induced by a linear involution of $V$. The signed sandwich is the composite of the unsigned one with $\alpha$, so the two families are reparametrisations of one another, and the sign it carries is the parity of the element it acts on; the sandwich maps compose by the rule $(a,b)(r,s) = (ar,sb)$, the signed ones by the twisted rule, and the invertible ones form the group of two-sided operators with the inner automorphisms among them. This article develops the two sandwiches, their composition laws, their relation and the invertibility criterion; the reflections they realise are *Reflections as Signed Two-Sided Operators on a Linear Space*, the one-sided variant is *The Signed Left Multiplication on a Linear Space*, and the adjoint with respect to the trace pairing is *The Signed Adjoint Sandwich on a Linear Space*.

*Involutive Linear Spaces* treats the linear-space involution of $E$, which is exactly $\alpha$, with its type $(p^2+q^2,2pq)$ and its trace $(p-q)^2$; the present article uses the multiplication of $E$ as well, which the linear-space article does not. *Involutive Bilinear Algebras* treats the involutions and the sandwiches of an abstract algebra with an involution; the article here is the concrete case over a linear space, inside the operator group, and it cites that article for the abstract laws. *Left and Right Multiplication in a Group* is the group-level analogue of the one-sided operators, and *The Adjoint of the Left Multiplication on a Linear Space* treats the unsigned one-sided operators with respect to the trace pairing.

Throughout, $F$ is a field, $V$ is a finite-dimensional $F$-linear space, $E = \operatorname{End}_F(V)$, and $\alpha$ is the **grade involution**: an algebra automorphism of $E$ with $\alpha^2 = \mathrm{id}$, given concretely by $\alpha(X) = TXT$ for a linear involution $T \neq \mathrm{id}$ of $V$. An element is **homogeneous** when it lies in an eigenspace of $\alpha$, and its **sign** is $\varepsilon_X = +1$ on the fixed part and $-1$ on the negated part. No form and no topology is used.

## The Two Sandwiches

**Definition.** For $a,b \in E$ the **unsigned sandwich** and the **signed sandwich** are the operators on $E$

$$
\Phi_{a,b}(X) = aXb, \qquad \Theta^{\alpha}_{a,b}(X) = a\,\alpha(X)\,b .
$$

**Proposition (composition laws).** For all $a,b,r,s \in E$,

$$
\Phi_{a,b}\Phi_{r,s} = \Phi_{ar,sb}, \qquad \Theta^{\alpha}_{a,b}\Theta^{\alpha}_{r,s} = \Theta^{\alpha}_{a\alpha(r),\alpha(s)b} .
$$

**Proof.** $\Phi_{a,b}\Phi_{r,s}(X) = a(rXs)b = (ar)X(sb) = \Phi_{ar,sb}(X)$. For the signed case apply $\alpha$ in the middle: $\Theta^{\alpha}_{a,b}\Theta^{\alpha}_{r,s}(X) = a\alpha(r\alpha(X)s)b = a\alpha(s)\alpha(\alpha(X))\alpha(r)b = a\alpha(s)X\alpha(r)b$, so the composite is the signed sandwich with the pair $(a\alpha(r),\alpha(s)b)$. This is the twisted form of the unsigned rule $(a,b)(r,s)=(ar,sb)$, and it reduces to it when $\alpha=\mathrm{id}$.

**Proposition (the signed sandwich is the unsigned one composed with $\alpha$).** For all $a,b$,

$$
\Theta^{\alpha}_{a,b} = \Phi_{a,b}\circ\alpha = \alpha\circ\Phi_{\alpha(a),\alpha(b)} , \qquad
\Phi_{a,b} = \alpha\circ\Theta^{\alpha}_{\alpha(a),\alpha(b)} = \Theta^{\alpha}_{\alpha(a),\alpha(b)}\circ\alpha .
$$

**Proof.** $\Phi_{a,b}(\alpha(X)) = a\alpha(X)b = \Theta^{\alpha}_{a,b}(X)$, which is the first identity; $(\alpha\circ\Phi_{\alpha(a),\alpha(b)})(X) = \alpha(\alpha(a)X\alpha(b)) = a\alpha(X)b$ by the multiplicativity of $\alpha$, which is the second. Replacing $a,b$ by $\alpha(a),\alpha(b)$ in the first identity and composing with $\alpha$ gives the last, since $\alpha^2=\mathrm{id}$.

**Corollary (the sign on homogeneous elements).** If $X$ is homogeneous then

$$
\Theta^{\alpha}_{a,b}(X) = \varepsilon_X\,\Phi_{a,b}(X) ,
$$

so the signed sandwich differs from the unsigned one by the parity sign of the element acted on; in particular the two agree on the fixed part of $\alpha$ and are opposite on the negated part.

**Proof.** $\alpha(X)=\varepsilon_X X$ for homogeneous $X$, so $a\alpha(X)b=\varepsilon_X aXb$.

## Invertibility and the Inner Sandwiches

**Proposition.** $\Phi_{a,b}$ is invertible if and only if $a$ and $b$ are invertible, and then $\Phi_{a,b}^{-1}=\Phi_{b^{-1},a^{-1}}$; $\Theta^{\alpha}_{a,b}$ is invertible if and only if $a$ and $b$ are invertible.

**Proof.** If $a,b$ are invertible, $\Phi_{b^{-1},a^{-1}}\Phi_{a,b}=\Phi_{b^{-1}a,ba^{-1}}=\Phi_{\mathrm{id},\mathrm{id}}=\mathrm{id}$ and likewise on the other side; if $\Phi_{a,b}$ is invertible, then $X \mapsto aXb$ is injective, which forces $a$ and $b$ to be injective: if $aX=0$ for some $X\neq0$ then $\Phi_{a,b}$ kills $Xb'$ for suitable $b'$, and similarly for $b$. The signed case follows from $\Theta^{\alpha}_{a,b}=\Phi_{a,b}\alpha$ and the invertibility of $\alpha$.

**Definition.** The **inner sandwich** of an invertible $a$ is $\Phi_{a,a^{-1}}$, also written $\mathrm{Ad}_a$; the **signed inner sandwich** is $\Theta^{\alpha}_{a,a^{-1}} = \mathrm{Ad}_a\circ\alpha$.

**Proposition.** $\mathrm{Ad}_a$ is the inner automorphism of the algebra $E$ determined by $a$, and the signed inner sandwich is an automorphism of $E$; the group $\{\mathrm{Ad}_a : a \in E^{\times}\}$ is isomorphic to $E^{\times}/Z(E)^{\times}$, and its order-two automorphisms are the $\mathrm{Ad}_a$ with $a^2$ central.

**Proof.** $\mathrm{Ad}_a(XY) = aXYa^{-1} = (aXa^{-1})(aYa^{-1})$, so $\mathrm{Ad}_a$ is an automorphism with inverse $\mathrm{Ad}_{a^{-1}}$; the kernel of $a\mapsto\mathrm{Ad}_a$ is the centre $Z(E)$; $\mathrm{Ad}_a^2=\mathrm{Ad}_{a^2}$, which is the identity exactly when $a^2$ is central, and this is the criterion of *Algebras of Endomorphisms*.

## Summary

On $E = \operatorname{End}_F(V)$ the unsigned sandwich $\Phi_{a,b}(X)=aXb$ composes by $\Phi_{a,b}\Phi_{r,s}=\Phi_{ar,sb}$, and the signed sandwich $\Theta^{\alpha}_{a,b}(X)=a\alpha(X)b$, formed with the grade involution $\alpha$, composes by the twisted rule $\Theta^{\alpha}_{a,b}\Theta^{\alpha}_{r,s}=\Theta^{\alpha}_{a\alpha(r),\alpha(s)b}$; the two families are related by $\Theta^{\alpha}_{a,b}=\Phi_{a,b}\circ\alpha=\alpha\circ\Phi_{\alpha(a),\alpha(b)}$, and on a homogeneous element the signed sandwich is the unsigned one multiplied by the parity sign. Both are invertible exactly when $a$ and $b$ are, with $\Phi_{a,b}^{-1}=\Phi_{b^{-1},a^{-1}}$; the inner sandwiches $\Phi_{a,a^{-1}}$ are the inner automorphisms of $E$, and the signed inner sandwiches $\Theta^{\alpha}_{a,a^{-1}}=\mathrm{Ad}_a\circ\alpha$ are the composites of an inner automorphism with the grade involution. The reflections realised by the signed sandwiches, the one-sided signed action, and the adjoint with respect to the trace pairing are the subjects of the three companion articles.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F$, $V$, $n$ | the field, the space and its dimension |
| $E=\operatorname{End}_F(V)$ | the endomorphism algebra |
| $\alpha$ | the grade involution, $\alpha(X)=TXT$, $T^2=\mathrm{id}$ |
| $\varepsilon_X$ | the sign of a homogeneous $X$, $+1$ or $-1$ |
| $\Phi_{a,b}(X)=aXb$ | the unsigned sandwich |
| $\Theta^{\alpha}_{a,b}(X)=a\alpha(X)b$ | the signed sandwich |
| $\Phi_{a,b}\Phi_{r,s}=\Phi_{ar,sb}$ | the composition law |
| $\Theta^{\alpha}_{a,b}\Theta^{\alpha}_{r,s}=\Theta^{\alpha}_{a\alpha(r),\alpha(s)b}$ | the signed composition law |
| $\mathrm{Ad}_a=\Phi_{a,a^{-1}}$ | the inner sandwich |

## Further Reading

- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for the involutions of an algebra and the sandwich operators.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the general theory of involutions and their sandwiches.
- Tsit-Yuen Lam, *A First Course in Noncommutative Rings* (Springer, 2nd ed. 2001), for the inner automorphisms of an endomorphism algebra and the centraliser of the multiplications.
