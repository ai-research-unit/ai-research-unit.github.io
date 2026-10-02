
# __The Signed Adjoint Sandwich on a Group__

## Introduction

The signed sandwich $x\mapsto a\,\alpha(x)\,b$ is the two-sided operator built from the two-sided translation and the grade involution, and its adjoint under the natural pairing is again a signed sandwich, with the two parameters inverted and twisted by the involution. The computation is entirely explicit, and it has a sharp consequence: every signed sandwich is unitary, so the unitarity condition imposes no constraint on the parameters, while the self-adjointness condition is the nontrivial one and returns a centrality statement. This article gives the adjoint, the unitarity that follows from it, and the self-adjointness criterion. It is the fourth article of the `* Operator Theory` group; the signed sandwich and its composition law are from *The Signed Sandwich on a Group*, the pairing and the adjoint from *Involutions on the Operator Layer*, and the unsigned case from *The Group Inversion as an Adjoint*.

Throughout, $(G,\alpha)$ is a group with an involutive automorphism $\alpha$, $\Sigma^{\alpha}_{a,b}$ is the signed sandwich $\Sigma^{\alpha}_{a,b}(x)=a\,\alpha(x)\,b$, the pairing is $\langle g,h\rangle=\delta_{g,h}$, and the adjoint is defined by $\langle Tx,y\rangle=\langle x,T^{*}y\rangle$.

## The Adjoint of the Signed Sandwich

**Theorem (the adjoint is a signed sandwich).** For every $a,b\in G$,

$$
\bigl(\Sigma^{\alpha}_{a,b}\bigr)^{*}=\Sigma^{\alpha}_{\alpha(a)^{-1},\ \alpha(b)^{-1}}
=\Sigma^{\alpha}_{\alpha(a^{-1}),\ \alpha(b^{-1})}.
$$

**Proof.** In the basis $G$, $\Sigma^{\alpha}_{a,b}(g)=a\,\alpha(g)\,b$, so the matrix entry $\bigl(\Sigma^{\alpha}_{a,b}\bigr)_{h,g}$ equals $1$ exactly when $h=a\,\alpha(g)\,b$, that is when $g=\alpha(a)^{-1}\alpha(h)\alpha(b)^{-1}=\alpha\bigl(a^{-1}hb^{-1}\bigr)$, using that $\alpha$ is an automorphism with $\alpha^{2}=\mathrm{id}$. Hence the transpose sends $h$ to $\alpha(a)^{-1}\alpha(h)\alpha(b)^{-1}=\Sigma^{\alpha}_{\alpha(a)^{-1},\alpha(b)^{-1}}(h)$.

**Corollary (the adjoint inverts and twists the parameters).** The adjoint of a signed sandwich is a signed sandwich, and the assignment on the parameters is

$$
(a,b)\longmapsto\bigl(\alpha(a)^{-1},\ \alpha(b)^{-1}\bigr)=\bigl(\alpha(a^{-1}),\ \alpha(b^{-1})\bigr).
$$

In particular the adjoint of the unsigned sandwich is the unsigned sandwich with inverted parameters, in agreement with *The Group Inversion as an Adjoint*.

**Proof.** The formula is the theorem with $\alpha=\mathrm{id}$, and the two expressions for the parameter pair agree because $\alpha$ is an automorphism. The unsigned case $\bigl(\Sigma_{a,b}\bigr)^{*}=\Sigma_{a^{-1},b^{-1}}$ is the specialisation.

**Proposition (the adjoint of a product of two signed sandwiches).** $\bigl(\Sigma^{\alpha}_{a,b}\Sigma^{\alpha}_{c,d}\bigr)^{*}=\bigl(\Sigma^{\alpha}_{a\alpha(c),\,\alpha(d)b}\bigr)^{*}=\Sigma^{\alpha}_{\alpha(a)^{-1}\alpha(c)^{-1},\ \alpha(d)^{-1}\alpha(b)^{-1}}$, by the anti-multiplicativity of the adjoint and the composition law of *The Signed Sandwich on a Group*.

**Proof.** The composition law is $\Sigma^{\alpha}_{a,b}\Sigma^{\alpha}_{c,d}=\Sigma^{\alpha}_{a\alpha(c),\alpha(d)b}$; applying the theorem to the composite gives the displayed pair. The two routes — composing the adjoints in reverse and transposing the composite — agree.

## Unitarity

**Theorem (every signed sandwich is unitary).** For every $a,b\in G$,

$$
\bigl(\Sigma^{\alpha}_{a,b}\bigr)^{*}\Sigma^{\alpha}_{a,b}=\mathrm{id}=\Sigma^{\alpha}_{a,b}\bigl(\Sigma^{\alpha}_{a,b}\bigr)^{*}.
$$

**Proof.** By the adjoint formula and the composition law,

$$
\Sigma^{\alpha}_{a,b}\bigl(\Sigma^{\alpha}_{a,b}\bigr)^{*}
=\Sigma^{\alpha}_{a,b}\Sigma^{\alpha}_{\alpha(a)^{-1},\alpha(b)^{-1}}
=\Sigma^{\alpha}_{a\,\alpha(\alpha(a)^{-1}),\ \alpha(\alpha(b)^{-1})\,b}
=\Sigma^{\alpha}_{a\,a^{-1},\ b^{-1}\,b}=\Sigma^{\alpha}_{e,e}=\mathrm{id},
$$

and the other product is the same computation with the order exchanged.

**Corollary (the unitarity condition imposes nothing).** The condition $u^{*}u=uu^{*}=1$ of the menu is satisfied by every signed sandwich, whatever the pair $(a,b)$ and whatever the involutive automorphism $\alpha$; the signed sandwiches form a set of unitary operators and the unitarity condition does not cut it down.

**Proof.** The theorem is the condition for $u=\Sigma^{\alpha}_{a,b}$; it holds for all pairs, so the set of unitary operators contains all the signed sandwiches.

**Remark (the contrast with the unsigned case).** The unsigned sandwich is also unitary, with inverse $\Sigma_{a^{-1},b^{-1}}$, so unitarity is not the feature that distinguishes the signed family; the signed family is the coset of the unsigned family under the involution, by *The Signed Sandwich on a Group*, and the two have the same unitarity. The distinguishing feature is the sign carried by $\alpha$, which shows up in the self-adjointness rather than in the unitarity.

## Self-Adjointness

**Proposition (the equality of two signed sandwiches).** Two signed sandwiches agree, $\Sigma^{\alpha}_{a,b}=\Sigma^{\alpha}_{c,d}$, if and only if there is a central element $z\in Z(G)$ with

$$
c=a\,z^{-1}, \qquad d=z\,b .
$$

**Proof.** The equality $a\alpha(x)b=c\alpha(x)d$ for all $x$ is equivalent to $c^{-1}a\,\alpha(x)=\alpha(x)\,db^{-1}$ for all $x$; the element $u=c^{-1}a$ then commutes with every $\alpha(x)$, hence $u\in Z(G)$, and $db^{-1}=u$. Setting $z=u$ gives the two relations.

**Theorem (the self-adjointness criterion).** The signed sandwich $\Sigma^{\alpha}_{a,b}$ is self-adjoint if and only if

$$
\alpha(a)\,a\in Z(G) \quad\text{and}\quad b\,\alpha(b)=\bigl(\alpha(a)\,a\bigr)^{-1},
$$

equivalently if and only if there is a central element $z$ of order at most two with $\alpha(a)a=z$ and $b\alpha(b)=z$.

**Proof.** Self-adjointness is $\Sigma^{\alpha}_{a,b}=\Sigma^{\alpha}_{\alpha(a)^{-1},\alpha(b)^{-1}}$, which by the equality criterion is the existence of $z\in Z(G)$ with $\alpha(a)^{-1}=a z^{-1}$ and $\alpha(b)^{-1}=zb$. The first gives $z=\alpha(a)a$; substituting into the second gives $\alpha(b)^{-1}=\alpha(a)a\,b$, equivalently $b\alpha(b)=(\alpha(a)a)^{-1}$. Since $z=\alpha(a)a$ and $z^{-1}=b\alpha(b)$ are both displayed as the same central element and its inverse, $z^{2}=e$. In particular the self-adjoint signed sandwiches are the ones whose two parameters satisfy the reflection condition $\alpha(a)a\in Z(G)$ on the first and its inverse on the second.

**Corollary (the self-adjoint two-sided translations).** For $\alpha=\mathrm{id}$ the criterion is $a^{2}\in Z(G)$ and $b^{2}=(a^{2})^{-1}$, so the self-adjoint unsigned sandwiches are the two-sided translations with $a^{2}$ central of order at most two and $b=a^{-1}$ up to the centre; the sandwich is then the unsigned translation paired with the corresponding reflection of the cyclic subgroup generated by $a$.

**Proof.** The criterion specialises with $\alpha=\mathrm{id}$, and the last statement is the identification of the two-sided translation with the reflection data of the unsigned operator.

## The Relation to the One-Sided Operators

**Proposition (factorisation).** $\Sigma^{\alpha}_{a,b}=R_b\circ\ell^{\alpha}_a$, where $\ell^{\alpha}_a(x)=a\,\alpha(x)$ is the signed left multiplication of *The Signed Left Multiplication on a Group*.

**Proof.** $R_b(\ell^{\alpha}_a(x))=a\,\alpha(x)\,b=\Sigma^{\alpha}_{a,b}(x)$ for every $x$, and both maps are linear, so the composition is the signed sandwich.

**Corollary (the adjoint factors in reverse).** $\bigl(\Sigma^{\alpha}_{a,b}\bigr)^{*}=\bigl(\ell^{\alpha}_a\bigr)^{*}\circ(R_b)^{*}=\ell^{\alpha}_{\alpha(a)^{-1}}\circ R_{b^{-1}}$.

**Proof.** The adjoint of a product reverses the order, the adjoint of $R_b$ is $R_{b^{-1}}$, and the adjoint of the signed left multiplication is computed in *The Signed Adjoint of the Left Multiplication on a Group*; composing and comparing with the theorem gives the same expression.

**Remark.** The factorisation shows that the signed sandwich is read from a signed one-sided operator and a right translation; its adjoint is then read from the two adjoints in the reverse order, and the result is again a signed sandwich with the two parameters transformed. Nothing in the computation uses invertibility of $a$ or of $b$, and the adjoint formula holds for all parameters.

## Summary

The adjoint of the signed sandwich is the signed sandwich with the parameters transformed by inversion and the involution,

$$
\bigl(\Sigma^{\alpha}_{a,b}\bigr)^{*}=\Sigma^{\alpha}_{\alpha(a)^{-1},\alpha(b)^{-1}},
$$

which for $\alpha=\mathrm{id}$ is the unsigned rule $\Sigma_{a,b}^{*}=\Sigma_{a^{-1},b^{-1}}$, and which respects composition through the anti-multiplicativity of the adjoint. **Every signed sandwich is unitary**, because the adjoint is its inverse; the unitarity condition $u^{*}u=uu^{*}=1$ therefore holds for all parameters and imposes no restriction. The **self-adjointness** is the nontrivial condition: $\Sigma^{\alpha}_{a,b}$ is self-adjoint if and only if $\alpha(a)a$ is a central element of order at most two and $b\alpha(b)$ is its inverse, the reflection condition on the first parameter and its dual on the second. Two signed sandwiches agree exactly when their parameters differ by a central factor, $\Sigma^{\alpha}_{a,b}=\Sigma^{\alpha}_{az^{-1},zb}$ for $z\in Z(G)$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Sigma^{\alpha}_{a,b}(x)=a\,\alpha(x)\,b$ | the signed sandwich |
| $\bigl(\Sigma^{\alpha}_{a,b}\bigr)^{*}=\Sigma^{\alpha}_{\alpha(a)^{-1},\alpha(b)^{-1}}$ | the adjoint |
| $u^{*}u=uu^{*}=1$ | the unitarity condition, satisfied by every signed sandwich |
| $\alpha(a)a\in Z(G)$, $b\alpha(b)=(\alpha(a)a)^{-1}$ | the self-adjointness criterion |
| $\Sigma^{\alpha}_{a,b}=\Sigma^{\alpha}_{az^{-1},zb}$ | equality up to a central factor |
| $\Sigma^{\alpha}_{a,b}=R_b\circ\ell^{\alpha}_a$ | factorisation into one-sided operators |

## Further Reading

- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for adjoints, unitary operators and the self-adjoint elements of a group with involution.
- Serge Lang, *Algebra* (Springer, Graduate Texts in Mathematics 211, third edition, 2002), for bilinear forms, adjoints and the unitary group.
- Donald S. Passman, *The Algebraic Structure of Group Rings* (Wiley, 1977), for the group algebra, its translations and their inverses.
- I. Martin Isaacs, *Finite Group Theory* (American Mathematical Society, Graduate Studies in Mathematics 92, 2008), for centrality conditions and elements of order two.
