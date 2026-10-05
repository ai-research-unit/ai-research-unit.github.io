# __Reflections as Signed Two-Sided Operators on a Linear Space__

## Introduction

A reflection of a linear space is a linear involution of type $(n-1,1)$, and as an element of $E = \operatorname{End}_F(V)$ it satisfies $r^2 = 1$; it carries its own grade involution $\alpha_r(X) = rXr$, and the question of this article is which elements of $E$ act by an involution through the signed two-sided operator, and how the reflections of $V$ correspond to them. The answer is a criterion: the signed inner sandwich $\Theta^{\alpha}_{a,a^{-1}} = \mathrm{Ad}_a\circ\alpha$ has square $\mathrm{Ad}_{a\alpha(a)}$ and is an involution exactly when $a\alpha(a)$ is central; the reflection $r$ itself acts trivially by its own signed sandwich, and the elements acting by an involution through a fixed grade involution are precisely those with $a\alpha(a)$ central. The correspondence fails in the degenerate cases, of characteristic two and of the trivial grade involution.

*The Signed Sandwich on a Linear Space* supplies the two sandwiches, their composition laws and the inner ones; *Involutive Subspaces and the Decomposition* supplies the form-free notion of a reflection and its fixed hyperplane; *Involutive Bilinear Algebras* treats the abstract correspondence between involutions of an algebra and elements acting by sandwiched involutions, and the present article is the concrete case on $E$ inside the operator group. The adjoint of the reflection is *The Signed Adjoint of the Reflection on a Linear Space*.

Throughout, $F$ is a field with $2 \neq 0$, $V$ is a finite-dimensional $F$-linear space, $E = \operatorname{End}_F(V)$, and $\alpha$ is a grade involution of $E$: an automorphism of order two, given concretely by $\alpha(X) = TXT$ for a linear involution $T$ of $V$. A **reflection** is a linear involution $r$ of $V$ of type $(n-1,1)$, equivalently an element $r \in E$ with $r^2 = \mathrm{id}$ and $\operatorname{rk}(r-\mathrm{id}) = n-1$.

## The Signed Operator of an Element

**Definition.** For an invertible $a \in E$ the **signed inner sandwich** of $a$ is

$$
\Theta^{\alpha}_{a,a^{-1}} = \mathrm{Ad}_a\circ\alpha, \qquad
\Theta^{\alpha}_{a,a^{-1}}(X) = a\,\alpha(X)\,a^{-1} .
$$

**Proposition.** $\Theta^{\alpha}_{a,a^{-1}}$ is an automorphism of $E$, and

$$
\bigl(\Theta^{\alpha}_{a,a^{-1}}\bigr)^{2} = \mathrm{Ad}_{a\alpha(a)} ,
$$

so it is an involution of $E$ exactly when $a\alpha(a)$ is central in $E$.

**Proof.** It is an automorphism as the composite of the automorphisms $\mathrm{Ad}_a$ and $\alpha$. For the square, $\mathrm{Ad}_a\alpha\mathrm{Ad}_a\alpha = \mathrm{Ad}_a\,\alpha\mathrm{Ad}_a\alpha = \mathrm{Ad}_a\mathrm{Ad}_{\alpha(a)}\alpha^2 = \mathrm{Ad}_{a\alpha(a)}$, using $\alpha\mathrm{Ad}_b\alpha = \mathrm{Ad}_{\alpha(b)}$ and $\alpha^2=\mathrm{id}$. An inner automorphism is the identity exactly when its parameter is central, by *Algebras of Endomorphisms*.

**Corollary.** If $a$ commutes with $\alpha$, that is $\alpha(a)=a$, then $\Theta^{\alpha}_{a,a^{-1}}$ is an involution exactly when $a^2$ is central; in particular a scalar $\lambda$ gives $\Theta^{\alpha}_{\lambda,\lambda^{-1}}=\alpha$, of order two.

## Reflections and the Correspondence

**Proposition (the reflection acts trivially by its own signed sandwich).** Let $r$ be a reflection of $V$ and let $\alpha = \alpha_r$, $\alpha_r(X) = rXr$. Then

$$
\Theta^{\alpha_r}_{r,r^{-1}}(X) = r\,(rXr)\,r = X ,
$$

so $\Theta^{\alpha_r}_{r,r^{-1}} = \mathrm{id}$; the reflection is fixed by the signed inner sandwich of itself.

**Proof.** $r^2=\mathrm{id}$ gives $r\alpha_r(X)r = r(rXr)r = X$.

**Proposition (the correspondence).** An automorphism of $E$ of the form $\Theta^{\alpha}_{a,a^{-1}}$ is an involution if and only if $a\alpha(a)$ is central; writing $a = r\lambda$ with $r$ a reflection commuting with $\alpha$ and $\lambda$ a scalar, this condition becomes $\lambda^2 r\alpha(r)$ central, and the automorphisms of $E$ obtained are the inner automorphisms composed with $\alpha$ and parametrised by the classes of $E^{\times}$ modulo the centre in which $a\alpha(a)$ is central. Every reflection of $V$ supplies a grade involution $\alpha_r$, and the assignment is injective on the reflections modulo the centre.

**Proof.** The criterion is the proposition of the previous section. The factorisation $a = r\lambda$ with $r$ a reflection holds for every invertible $a$ up to a scalar when the scalar is chosen to make $r=a/\lambda$ an involution: $r^2 = a^2/\lambda^2$, so $\lambda$ is chosen with $\lambda^2$ equal to the central part of $a^2$. The injectivity statement is the computation of the centre of the automorphism group, *Algebras of Endomorphisms*.

**Remark (the failure in the degenerate cases).** Two degenerations break the correspondence. In characteristic two a reflection is unipotent, the decomposition $V = V_+\oplus V_-$ with a sign does not exist, and the grade involution collapses to the identity, so the signed sandwich is the unsigned inner automorphism and realises no sign; this is the collapse of *Involutive Linear Spaces*. When $\alpha = \mathrm{id}$, that is when the linear involution defining it is the identity, the signed and unsigned sandwiches coincide and the family carries no sign at all.

## Summary

A reflection of $V$ is a linear involution of type $(n-1,1)$, an element $r \in E$ with $r^2=\mathrm{id}$ and $\operatorname{rk}(r-\mathrm{id})=n-1$. For an invertible $a$ the signed inner sandwich $\Theta^{\alpha}_{a,a^{-1}}(X)=a\alpha(X)a^{-1}$ is an automorphism of $E$ whose square is $\mathrm{Ad}_{a\alpha(a)}$, so it is an involution exactly when $a\alpha(a)$ is central; the reflection $r$ acts trivially by its own signed sandwich $\Theta^{\alpha_r}_{r,r^{-1}}$, and the elements acting by an involution through a fixed grade involution $\alpha$ are those with $a\alpha(a)$ central, parametrised by the invertible classes modulo the centre. The correspondence between reflections and elements acting by an involution breaks in characteristic two, where the sign collapses, and when the defining involution is the identity, where the signed and unsigned families coincide.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F$, $V$, $n$ | the field, the space and its dimension |
| $E=\operatorname{End}_F(V)$ | the endomorphism algebra |
| $r$ | a reflection, $r^2=\mathrm{id}$, $\operatorname{rk}(r-\mathrm{id})=n-1$ |
| $\alpha_r(X)=rXr$ | the grade involution of a reflection |
| $\Theta^{\alpha}_{a,a^{-1}}=\mathrm{Ad}_a\circ\alpha$ | the signed inner sandwich |
| $(\Theta^{\alpha}_{a,a^{-1}})^2=\mathrm{Ad}_{a\alpha(a)}$ | the square, an involution iff $a\alpha(a)$ central |
| $\mathrm{Ad}_a=\Phi_{a,a^{-1}}$ | the inner automorphism |

## Further Reading

- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for involutions, reflections and the sandwich operators.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the correspondence between involutions and sandwiched elements.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for reflections and their fixed hyperplanes.
