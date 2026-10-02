
# __The Signed Sandwich on a Complex Vector Space__

## Introduction

Let $V$ be a complex vector space, $E = \operatorname{End}_{\mathbb C}(V)$ its endomorphism algebra, and $\alpha$ a **grade involution** of $E$: an automorphism of order two, given concretely by $\alpha(X) = TXT$ for a linear involution $T$ of $V$. The **unsigned sandwich** is the two-sided multiplication
$$
\Phi_{a,b}(X) = aXb,
$$
and the **signed sandwich** is its twist by the grade involution,
$$
\Theta^{\alpha}_{a,b}(X) = a\,\alpha(X)\,b .
$$
The signed sandwich is the most general operator built from two one-sided multiplications and the involution, and it is the object that realises the symmetries of the space: when the involution $T$ is **unitary and self-adjoint** for a Hermitian form $h$ on $V$ — so that $\alpha$ preserves the adjoint, $\alpha(X^{\dagger}) = \alpha(X)^{\dagger}$ — the inner signed sandwich $\Theta^{\alpha}_{u,u^{-1}} = \mathrm{Ad}_u\circ\alpha$ by a unitary $u$ is an isometry of the Hermitian trace form of $E$, and the **unitary reflections** of $V$ are the involutions it realises. Its composition laws reduce every composite of signed sandwiches to a signed sandwich, its square is $\mathrm{Ad}_{a\alpha(a)}$ so that it is an involution exactly when $a\alpha(a)$ is central, and its relation to the unsigned sandwich is the relation of the two involutive layers: the unsigned sandwich is the case of the trivial $\alpha$, and the signed family is the unsigned family composed with the involution.

The article has three sections: the sandwich and its composition laws; the reflections and the isometries it realises; and the relation to the unsigned sandwich and the degenerate cases. The unsigned and signed sandwiches, their laws and the associated involutive-subspace theory are *The Signed Sandwich on a Linear Space*, *Involutive Linear Spaces* and *Involutive Linear Algebras*; the endomorphism algebra, the double centraliser and the trace are *Algebras of Endomorphisms*; the Hermitian form, the unitary group and the involution are *The Unitary and Symplectic Groups*, *Hermitian Geometry and the Unitary Group* and *The Left and Right Multiplication Operators on a Complex Vector Space*, the previous article of this group. The correspondence between reflections and the elements acting by an involution is *Reflections as Signed Two-Sided Operators on a Complex Vector Space*, and the adjoint of the signed sandwich is *The Signed Adjoint Sandwich on a Complex Vector Space*, both of this group.

Throughout, $V$ is a finite-dimensional complex vector space of dimension $n$ with a positive-definite Hermitian form $h$, $E = \operatorname{End}_{\mathbb C}(V)$, $A^{\dagger}$ is the adjoint for $h$, $T$ is a unitary self-adjoint involution of $V$, $\alpha(X) = TXT$ is the grade involution it defines, $\Phi_{a,b}$ and $\Theta^{\alpha}_{a,b}$ are the unsigned and signed sandwiches on $E$, and $\langle X, Y\rangle = \operatorname{tr}(X^{\dagger}Y)$ is the Hermitian trace form of $E$. The characteristic is zero throughout, so $2 \neq 0$ and no collapse of the sign occurs.

## The Sandwich and Its Composition Laws

**Definition.** For $a, b \in E$ the **unsigned sandwich** and the **signed sandwich** are
$$
\Phi_{a,b}(X) = aXb, \qquad \Theta^{\alpha}_{a,b}(X) = a\,\alpha(X)\,b .
$$
The signed sandwich is the composite $\Theta^{\alpha}_{a,b} = \Phi_{a,\alpha(b)}\circ\alpha = \alpha\circ\Phi_{\alpha(a),b}$, and the inversion $\alpha$ is the only difference between the two families.

**Proposition (composition).** For all $a,b,c,d \in E$,
$$
\Theta^{\alpha}_{a,b}\,\Theta^{\alpha}_{c,d} = \Theta^{\alpha}_{a\alpha(d),\,\alpha(c)b}, \qquad
\Phi_{a,b}\,\Theta^{\alpha}_{c,d} = \Theta^{\alpha}_{ac,\,db}, \qquad
\Theta^{\alpha}_{a,b}\,\Phi_{c,d} = \Theta^{\alpha}_{a\alpha(d),\,\alpha(c)b}.
$$
Thus the set of signed sandwiches is closed under composition, and each product of a signed and an unsigned sandwich is again a signed sandwich; the unsigned sandwiches are closed among themselves, $\Phi_{a,b}\Phi_{c,d} = \Phi_{ac,db}$.

**Proof.** Direct computation: $\Theta^{\alpha}_{a,b}(\Theta^{\alpha}_{c,d}(X)) = a\alpha(c\alpha(X)d)b = a\alpha(d)\,\alpha(\alpha(X))\,\alpha(c)b = a\alpha(d)X\alpha(c)b = \Theta^{\alpha}_{a\alpha(d),\alpha(c)b}(X)$, using $\alpha^2 = \mathrm{id}$; the other two are the same computation with one factor unsigned, and the unsigned law is associativity.

**Corollary (invertibility and inverse).** $\Theta^{\alpha}_{a,b}$ is invertible if and only if $a$ and $b$ are invertible, and then
$$
\bigl(\Theta^{\alpha}_{a,b}\bigr)^{-1} = \Theta^{\alpha}_{\alpha(b^{-1}),\,\alpha(a^{-1})} .
$$

**Proof.** Invertibility follows from the factorisation $\Theta^{\alpha}_{a,b} = \Phi_{a,\alpha(b)}\circ\alpha$ and the invertibility of $\alpha$. The inverse is checked by the composition law: with $c = \alpha(b^{-1})$ and $d = \alpha(a^{-1})$ one has $a\alpha(d) = a\alpha(\alpha(a^{-1})) = aa^{-1} = \mathrm{id}$ and $\alpha(c)b = \alpha(\alpha(b^{-1}))b = b^{-1}b = \mathrm{id}$, so the composite is $\Theta^{\alpha}_{\mathrm{id},\mathrm{id}} = \mathrm{id}$, and likewise on the other side.

**Definition.** The **inner signed sandwich** of an invertible $a$ is
$$
\Theta^{\alpha}_{a,a^{-1}} = \mathrm{Ad}_a\circ\alpha, \qquad \Theta^{\alpha}_{a,a^{-1}}(X) = a\,\alpha(X)\,a^{-1} .
$$

**Proposition (the square).** $\Theta^{\alpha}_{a,a^{-1}}$ is an automorphism of $E$ and
$$
\bigl(\Theta^{\alpha}_{a,a^{-1}}\bigr)^{2} = \mathrm{Ad}_{a\alpha(a)} ,
$$
so it is an involution exactly when $a\alpha(a)$ is central in $E$; in particular, when $a$ commutes with $\alpha$ it is an involution exactly when $a^2$ is central.

**Proof.** It is an automorphism as the composite of the automorphisms $\mathrm{Ad}_a$ and $\alpha$. For the square, $\mathrm{Ad}_a\alpha\mathrm{Ad}_a\alpha = \mathrm{Ad}_a\,\alpha\mathrm{Ad}_a\alpha = \mathrm{Ad}_a\mathrm{Ad}_{\alpha(a)}\alpha^2 = \mathrm{Ad}_{a\alpha(a)}$, using $\alpha\mathrm{Ad}_b\alpha = \mathrm{Ad}_{\alpha(b)}$ and $\alpha^2 = \mathrm{id}$; an inner automorphism is the identity exactly when its parameter is central, *Algebras of Endomorphisms*.

## The Reflections and the Isometries Realised

**Definition.** For $u \in V$ with $h(u,u) \neq 0$ the **unitary reflection** in $u$ is
$$
\rho_u(v) = v - 2\,\frac{h(v,u)}{h(u,u)}\,u ;
$$
it is a $\mathbb{C}$-linear involution of $V$ of type $(n-1,1)$, fixing the hyperplane $u^{\perp}$ and negating the line $\mathbb{C}u$; it is unitary, $\rho_u^{\dagger} = \rho_u^{-1}$, and self-adjoint, $\rho_u^{\dagger} = \rho_u$, for $h$.

**Proposition (the reflection is unitary and self-adjoint).** $\rho_u^2 = \mathrm{id}$, $\rho_u^{\dagger} = \rho_u$, and $\rho_u$ is unitary; it is therefore an element $r \in E$ with $r^2 = \mathrm{id}$, $r^{\dagger} = r$, and the grade involution $\alpha_r(X) = rXr$ it defines is an isometry of the trace form of $E$.

**Proof.** $\rho_u$ fixes $u^{\perp}$ and sends $u$ to $-u$, so $\rho_u^2 = \mathrm{id}$; the self-adjointness is $h(\rho_uv,w) = h(v,\rho_uw)$ from the Hermitian symmetry of $h$ and the reality of the factor $h(v,u)/h(u,u)$ in the appropriate pairing; unitarity is self-adjointness together with the involution, $\rho_u^{\dagger}\rho_u = \rho_u^2 = \mathrm{id}$. Since $r$ is unitary, conjugation by $r$ preserves $\operatorname{tr}(A^\dagger B)$ because it preserves the adjoint and the trace, as in the proposition below.

**Proposition (the inner signed sandwich by a unitary is an isometry).** Let $u \in E$ be unitary, $u^{\dagger}u = uu^{\dagger} = \mathrm{id}$. Then $\Theta^{\alpha}_{u,u^{-1}}$ preserves the Hermitian trace form,
$$
\bigl\langle \Theta^{\alpha}_{u,u^{-1}}(X),\, \Theta^{\alpha}_{u,u^{-1}}(Y)\bigr\rangle = \langle X, Y\rangle ,
$$
and it is an involution exactly when $u\alpha(u)$ is central. If moreover $\alpha$ comes from a unitary reflection $r$ and $u = r$, then $\Theta^{\alpha_r}_{r,r^{-1}} = \mathrm{id}$: a reflection is fixed by the signed inner sandwich of itself.

**Proof.** For the isometry, $\Theta(X)^{\dagger} = (u\alpha(X)u^{-1})^{\dagger} = u\,\alpha(X)^{\dagger}\,u^{-1} = u\,\alpha(X^{\dagger})\,u^{-1} = \Theta(X^{\dagger})$, using $u^{\dagger} = u^{-1}$ and $\alpha(X^{\dagger}) = T X^{\dagger} T = (TXT)^{\dagger} = \alpha(X)^{\dagger}$, which is the unitarity and self-adjointness of $T$; since $\Theta$ is an algebra automorphism, $\Theta(X^{\dagger})\Theta(Y) = \Theta(X^{\dagger}Y)$, and $\operatorname{tr}(\Theta(Z)) = \operatorname{tr}(u\alpha(Z)u^{-1}) = \operatorname{tr}(\alpha(Z)) = \operatorname{tr}(TZT) = \operatorname{tr}(Z)$, so the inner product is preserved. The involutivity criterion is the square proposition. For the last assertion, $\Theta^{\alpha_r}_{r,r^{-1}}(X) = r(rXr)r = X$ by $r^2 = \mathrm{id}$.

**Remark (the reflections realised).** The conjugations $\mathrm{Ad}_r$ by the unitary reflections $r$ are the involutions of $E$ that preserve the trace form and the complex structure; the signed inner sandwich $\Theta^{\alpha}_{u,u^{-1}}$ is an automorphism of $E$ that is the composite of such a conjugation with a grade involution, and it is an involution precisely when $u\alpha(u)$ is central. In this way the reflections of the Hermitian space are the involutions the signed sandwiches realise, and the unitary condition on $T$ is what makes the realised involutions isometries.

## The Relation to the Unsigned Sandwich and the Degenerate Cases

**Proposition (the unsigned sandwich as the trivial involution).** The signed sandwich with $\alpha = \mathrm{id}$ is the unsigned sandwich, $\Theta^{\mathrm{id}}_{a,b} = \Phi_{a,b}$; for the general grade involution,
$$
\Theta^{\alpha}_{a,b} = \Phi_{a,\alpha(b)}\circ\alpha = \alpha\circ\Phi_{\alpha(a),b},
$$
so the signed family is the unsigned family composed with the involution $\alpha$, and the diagonal case $b = a^{-1}$ is the inner signed sandwich $\Theta^{\alpha}_{a,a^{-1}} = \mathrm{Ad}_a\circ\alpha$, an inner automorphism followed by the involution.

**Proof.** The identity $\Theta^{\alpha}_{a,b} = \Phi_{a,\alpha(b)}\circ\alpha$ is the definition, and $\alpha\circ\Phi_{\alpha(a),b}(X) = \alpha(\alpha(a)Xb) = a\alpha(X)\alpha(b)$, which is $\Theta^{\alpha}_{a,\alpha(b)}(X)$... reading it as a two-sided multiplication by $a$ on the left and $\alpha(b)$ on the right after the involution. The diagonal case follows on setting $b = a^{-1}$.

**Remark (the failure in the degenerate cases).** Two degenerations break the correspondence between the signed sandwich and the geometry. When $\alpha = \mathrm{id}$ the signed and unsigned sandwiches coincide and the family carries no sign at all; this is the collapse of the $\mathbb Z/2$-grading, and the reflections are then ordinary conjugations. When the Hermitian form $h$ is degenerate, or when the vector $u$ is **isotropic**, $h(u,u) = 0$, the formula for $\rho_u$ is undefined and there is no unitary reflection in $u$; the signed sandwich by such an element still exists as an operator on $E$ but realises no reflection of $V$, so the correspondence between the elements acting by an involution and the reflections of the space fails exactly where the chosen form degenerates.

**Corollary (the sandwich and the operator layer).** The signed sandwich $\Theta^{\alpha}_{a,b}$ is the composite $L_a\circ\alpha\circ R_b$ of a left multiplication, the involution and a right multiplication, and every operator on $E$ built from the one-sided multiplications and one grade involution is of this form; with it the one-sided operators, the inner automorphisms and the reflections of the Hermitian space lie in a single family. This is the sense in which the signed sandwich is the central object of the operator layer of the category.

## Summary

On the endomorphism algebra $E = \operatorname{End}_{\mathbb C}(V)$ of a complex vector space the signed sandwich $\Theta^{\alpha}_{a,b}(X) = a\alpha(X)b$ is the twist of the two-sided multiplication by the grade involution $\alpha(X) = TXT$, with the composition laws $\Theta^{\alpha}_{a,b}\Theta^{\alpha}_{c,d} = \Theta^{\alpha}_{a\alpha(d),\alpha(c)b}$, $\Phi_{a,b}\Theta^{\alpha}_{c,d} = \Theta^{\alpha}_{ac,db}$ and $\Phi_{a,b}\Phi_{c,d} = \Phi_{ac,db}$, and with inverse $(\Theta^{\alpha}_{a,b})^{-1} = \Theta^{\alpha}_{\alpha(b^{-1}),\alpha(a^{-1})}$. The inner signed sandwich $\Theta^{\alpha}_{a,a^{-1}} = \mathrm{Ad}_a\circ\alpha$ has square $\mathrm{Ad}_{a\alpha(a)}$, so it is an involution exactly when $a\alpha(a)$ is central, and when $T$ is unitary and self-adjoint and $u$ is unitary it preserves the Hermitian trace form $\langle X,Y\rangle = \operatorname{tr}(X^\dagger Y)$; the unitary reflections $\rho_u(v) = v - 2h(v,u)h(u,u)^{-1}u$ of the Hermitian space are the elements whose conjugations are the realised involutions, and each reflection is fixed by its own signed inner sandwich. The signed family is the unsigned family $\Phi_{a,b}(X) = aXb$ composed with $\alpha$, the case $\alpha = \mathrm{id}$ being the unsigned one; the correspondence with the reflections fails when $\alpha = \mathrm{id}$ and when the form is degenerate or the vector isotropic. The laws, the involutive-subspace theory and the reflections are *The Signed Sandwich on a Linear Space*, *Involutive Linear Spaces* and *Reflections as Signed Two-Sided Operators on a Complex Vector Space*; the adjoint is *The Signed Adjoint Sandwich on a Complex Vector Space*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Phi_{a,b}(X) = aXb$ | the unsigned sandwich |
| $\Theta^{\alpha}_{a,b}(X) = a\alpha(X)b$ | the signed sandwich |
| $\alpha(X) = TXT$ | the grade involution, $T$ a unitary self-adjoint involution |
| $\Theta^{\alpha}_{a,a^{-1}} = \mathrm{Ad}_a\circ\alpha$ | the inner signed sandwich |
| $(\Theta^{\alpha}_{a,a^{-1}})^2 = \mathrm{Ad}_{a\alpha(a)}$ | the square, an involution iff $a\alpha(a)$ central |
| $\rho_u(v) = v - 2h(v,u)h(u,u)^{-1}u$ | the unitary reflection in $u$ |
| $\langle X,Y\rangle = \operatorname{tr}(X^\dagger Y)$ | the Hermitian trace form of $E$ |

## Further Reading

- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for involution, sandwiches and the automorphism groups of an algebra.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the correspondence between involutions and sandwiched elements.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for reflections, the sandwich and the orthogonal and unitary groups.
- Sigurdur Helgason, *Differential Geometry, Lie Groups and Symmetric Spaces* (American Mathematical Society, 2001), for reflections, the unitary group and the symmetric spaces they generate.
