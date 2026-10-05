
# __Reflections as Signed Two-Sided Operators on a Complex Vector Space__

## Introduction

A reflection of a complex vector space with a Hermitian form is a unitary involution of type $(n-1,1)$, that is a unitary endomorphism $r$ of $V$ with $r^2 = \mathrm{id}$ whose fixed space has dimension $n-1$; by the classification of such involutions every reflection is a $\rho_u$. As an element of the endomorphism algebra $E = \operatorname{End}_{\mathbb C}(V)$ the reflection satisfies $r^2 = \mathrm{id}$, so it defines a **grade involution** $\alpha_r(X) = rXr$, and the question of this article is which elements of $E$ act by an involution through the signed two-sided operator, and how the reflections of $V$ correspond to them. The answer is the criterion of the linear case sharpened by the form: the signed inner sandwich $\Theta^{\alpha}_{a,a^{-1}} = \mathrm{Ad}_a\circ\alpha$ has square $\mathrm{Ad}_{a\alpha(a)}$ and is an involution exactly when $a\alpha(a)$ is central; the reflection $r$ itself acts trivially by its own signed sandwich, $\Theta^{\alpha_r}_{r,r^{-1}} = \mathrm{id}$; and the realised involutions that are isometries of the Hermitian trace form are exactly the conjugations by the unitary reflections of $V$, so that the correspondence singles out the reflections from the general involutions of type $(n-1,1)$. The correspondence fails when the grade involution collapses and when the chosen form is degenerate.

The article has three sections: the signed operator of an element and its square; the reflections and the correspondence; and the failure in the degenerate cases. The unsigned and signed sandwiches and their laws are *The Signed Sandwich on a Complex Vector Space*, the previous article of this group; the abstract correspondence between the involutions of an algebra and the elements acting by sandwiched involutions is *Involutive Algebras*; the form-free notion of a reflection and its fixed hyperplane is *Involutive Subspaces and the Decomposition*; the endomorphism algebra, its centre and its trace are *Algebras of Endomorphisms*. The adjoint of the reflection is *The Signed Adjoint of the Reflection on a Complex Vector Space*, of this group.

Throughout, $V$ is a finite-dimensional complex vector space of dimension $n$ with a positive-definite Hermitian form $h$, $E = \operatorname{End}_{\mathbb C}(V)$, $A^{\dagger}$ is the adjoint for $h$, $\alpha$ is a grade involution of $E$ of the form $\alpha(X) = TXT$ with $T$ a unitary self-adjoint involution of $V$, and $\langle X, Y\rangle = \operatorname{tr}(X^{\dagger}Y)$ is the Hermitian trace form of $E$. A **reflection** is a unitary involution $r$ of $V$ of type $(n-1,1)$, equivalently an element $r \in E$ with $r^2 = \mathrm{id}$, $r^{\dagger} = r$ and $\operatorname{rk}(r-\mathrm{id}) = n-1$.

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
so it is an involution of $E$ exactly when $a\alpha(a)$ is central in $E$. When $a$ is unitary the automorphism is an isometry of the Hermitian trace form.

**Proof.** It is an automorphism as the composite of the automorphisms $\mathrm{Ad}_a$ and $\alpha$; the square is computed from $\alpha\mathrm{Ad}_b\alpha = \mathrm{Ad}_{\alpha(b)}$ and $\alpha^2 = \mathrm{id}$, and an inner automorphism is trivial exactly when its parameter is central, by *Algebras of Endomorphisms*. The isometry for unitary $a$ is the computation of *The Signed Sandwich on a Complex Vector Space*.

**Corollary.** If $a$ commutes with $\alpha$, that is $\alpha(a) = a$, then $\Theta^{\alpha}_{a,a^{-1}}$ is an involution exactly when $a^2$ is central; in particular a scalar $\lambda$ gives $\Theta^{\alpha}_{\lambda,\lambda^{-1}} = \alpha$, of order two.

## Reflections and the Correspondence

**Proposition (the reflection acts trivially by its own signed sandwich).** Let $r$ be a reflection of $V$ and let $\alpha = \alpha_r$, $\alpha_r(X) = rXr$. Then
$$
\Theta^{\alpha_r}_{r,r^{-1}}(X) = r\,(rXr)\,r = X ,
$$
so $\Theta^{\alpha_r}_{r,r^{-1}} = \mathrm{id}$; the reflection is fixed by the signed inner sandwich of itself.

**Proof.** $r^2 = \mathrm{id}$ gives $r\alpha_r(X)r = r(rXr)r = X$.

**Proposition (the correspondence).** An automorphism of $E$ of the form $\Theta^{\alpha}_{a,a^{-1}}$ is an involution if and only if $a\alpha(a)$ is central; writing $a = r\lambda$ with $r$ a reflection commuting with $\alpha$ and $\lambda$ a scalar, this condition becomes $\lambda^2 r\alpha(r)$ central, and the involutions of $E$ obtained are the inner automorphisms composed with $\alpha$ and parametrised by the classes of $E^{\times}$ modulo the centre in which $a\alpha(a)$ is central. Every reflection of $V$ supplies a grade involution $\alpha_r$, and the assignment is injective on the reflections modulo the centre.

**Proof.** The criterion is the proposition of the previous section. The factorisation $a = r\lambda$ holds for every invertible $a$ up to a scalar when the scalar is chosen to make $r = a/\lambda$ an involution: $r^2 = a^2/\lambda^2$, and $\lambda$ is chosen with $\lambda^2$ the central part of $a^2$. The injectivity statement is the computation of the centre of the automorphism group, *Algebras of Endomorphisms*.

**Proposition (the reflections are exactly the isometric involutions).** Among the involutions of $V$ of type $(n-1,1)$, the reflections are exactly those that are self-adjoint for $h$, and equivalently exactly those whose conjugation $\mathrm{Ad}_r$ preserves the Hermitian trace form; a self-adjoint involution of type $(n-1,1)$ is automatically unitary, and its two eigenspaces are orthogonal.

**Proof.** A unitary involution of type $(n-1,1)$ is self-adjoint, so the reflections are among the self-adjoint involutions of that type. Conversely let $r$ be self-adjoint, $r = r^{\dagger}$, with $r^2 = \mathrm{id}$ and $\operatorname{rk}(r-\mathrm{id}) = n-1$. The eigenspaces $V_{\pm} = \ker(r\mp\mathrm{id})$ are the $+1$ and $-1$ eigenspaces, and for $v \in V_+$, $w \in V_-$ one has $h(v,w) = h(rv,w) = h(v,rw) = -h(v,w)$, so $h(v,w) = 0$ and the two eigenspaces are orthogonal; with $\dim V_+ = n-1$, $\dim V_- = 1$ and $V = V_+\oplus V_-$ an orthogonal sum, $r$ fixes $V_+$ pointwise and negates the line $V_-$, so $r = \rho_u$ for a generator $u$ of $V_-$ and is unitary. That $\mathrm{Ad}_r$ preserves the trace form is the isometry statement for unitary $r$.

**Remark (the realised involutions).** The conjugations $\mathrm{Ad}_r$ by the reflections $r$ are the involutions of $E$ that preserve both the trace form and the complex structure, and they are the involutions that arise from the geometry of $V$; the inner signed sandwiches $\Theta^{\alpha}_{a,a^{-1}}$ that are involutions form the larger family of all inner automorphisms composed with a grade involution, and the unitary condition on $T$ and on $a$ is what restricts the family to the isometric ones. The reflection is the case in which the element and the grade involution are the same, and then the sandwich is the identity.

## The Failure in the Degenerate Cases

**Remark (the failure when the involution collapses).** When $\alpha = \mathrm{id}$, that is when the defining involution $T$ is the identity, the signed sandwich is the ordinary inner automorphism $\mathrm{Ad}_a$ and realises no sign; the two-sided family carries no grading, and the correspondence between the reflections and the elements acting by an involution degenerates to the statement that every involution of $E$ of the form $\mathrm{Ad}_a$ is an involution exactly when $a^2$ is central. The characteristic cannot degenerate here, the characteristic being zero, so this is the only collapse of the involution.

**Remark (the failure for a degenerate form, and for the non-self-adjoint involutions).** When the Hermitian form $h$ is **degenerate**, the orthogonal complement of a hyperplane need not be a line, a self-adjoint involution of type $(n-1,1)$ need not have orthogonal eigenspaces, and the classification $r = \rho_u$ fails; when in addition a vector $u$ with $h(u,u) = 0$ is present, the formula for $\rho_u$ is undefined and the reflection in the isotropic direction does not exist. The failure has a second face even in the non-degenerate case: an involution of $V$ of type $(n-1,1)$ that is not self-adjoint is not a reflection, its two eigenspaces are not orthogonal, its conjugation does not preserve the trace form, and it is not realised by a signed sandwich that is an isometry. The correspondence between the reflections of the Hermitian space and the isometric signed-sandwich involutions is therefore valid exactly in the non-degenerate, self-adjoint case.

**Corollary (the operator form of the correspondence).** The reflections of $V$ correspond to the grade involutions $\alpha_r$ modulo the centre, and the isometric signed-sandwich involutions are exactly the conjugations by these involutions; the element acting by the involution is the reflection itself, and the signed inner sandwich of a reflection is the identity. This is the operator form of the statement that a reflection is its own inverse and fixes its hyperplane pointwise.

## Summary

A reflection of a Hermitian space $V$ is a unitary involution of type $(n-1,1)$, equivalently an element $r \in E = \operatorname{End}_{\mathbb C}(V)$ with $r^2 = \mathrm{id}$, $r^{\dagger} = r$ and $\operatorname{rk}(r-\mathrm{id}) = n-1$; as an element it defines the grade involution $\alpha_r(X) = rXr$. For an invertible $a$ the signed inner sandwich $\Theta^{\alpha}_{a,a^{-1}}(X) = a\alpha(X)a^{-1}$ is an automorphism of $E$ whose square is $\mathrm{Ad}_{a\alpha(a)}$, so it is an involution exactly when $a\alpha(a)$ is central; the reflection acts trivially by its own signed sandwich, $\Theta^{\alpha_r}_{r,r^{-1}} = \mathrm{id}$, and the elements acting by an involution through a fixed $\alpha$ are those with $a\alpha(a)$ central, parametrised by the invertible classes modulo the centre. Among the involutions of type $(n-1,1)$ the reflections are exactly the self-adjoint ones, and equivalently exactly those whose conjugation preserves the Hermitian trace form; a self-adjoint such involution has orthogonal eigenspaces and is unitary. The correspondence fails when the grade involution collapses to the identity, when the Hermitian form is degenerate or the reflection direction isotropic, and for non-self-adjoint involutions, which are not realised as isometries. The laws of the sandwich are *The Signed Sandwich on a Complex Vector Space*; the abstract correspondence is *Involutive Algebras*; the adjoint is *The Signed Adjoint of the Reflection on a Complex Vector Space*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $E=\operatorname{End}_{\mathbb C}(V)$, $r$ | the endomorphism algebra and a reflection |
| $r^2=\mathrm{id}$, $\operatorname{rk}(r-\mathrm{id})=n-1$ | the reflection as an involution of type $(n-1,1)$ |
| $\alpha_r(X)=rXr$ | the grade involution of a reflection |
| $\Theta^{\alpha}_{a,a^{-1}}=\mathrm{Ad}_a\circ\alpha$ | the signed inner sandwich |
| $(\Theta^{\alpha}_{a,a^{-1}})^2=\mathrm{Ad}_{a\alpha(a)}$ | the square, an involution iff $a\alpha(a)$ central |
| $\langle X,Y\rangle=\operatorname{tr}(X^\dagger Y)$ | the Hermitian trace form |
| $\rho_u$ | the unitary reflection, a generator of the $-1$ eigenspace |

## Further Reading

- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for involutions, reflections and the sandwich operators.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the correspondence between involutions and sandwiched elements.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for reflections, their fixed hyperplanes and the unitary groups.
- Sigurdur Helgason, *Differential Geometry, Lie Groups and Symmetric Spaces* (American Mathematical Society, 2001), for reflections and the symmetric spaces they generate.
