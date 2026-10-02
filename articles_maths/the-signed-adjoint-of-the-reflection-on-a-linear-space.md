# __The Signed Adjoint of the Reflection on a Linear Space__

## Introduction

A reflection of a linear space is a linear involution of type $(n-1,1)$, and read as a signed two-sided operator it carries the grade involution $\alpha_r(X) = rXr$ that it defines. Its signed inner sandwich acts trivially, $\Theta^{\alpha_r}_{r,r^{-1}} = \mathrm{id}$, so the reflection is self-adjoint and unitary for its own signed sandwich; for an arbitrary grade involution the adjoint of the signed inner sandwich of $r$ is $\Theta^{\alpha}_{\alpha(r)^{-1},\alpha(r)}$, the sandwich by the inverse image of the parameter, and the sandwich is always unitary while being self-adjoint exactly when $\alpha(r)$ is an involution. This article records those facts and marks the degenerate cases in which they collapse.

*Involutive Subspaces and the Decomposition* supplies the form-free reflection and its fixed hyperplane; *Reflections as Signed Two-Sided Operators on a Linear Space* supplies the signed inner sandwich and the correspondence between reflections and sandwiched involutions; *The Signed Adjoint Sandwich on a Linear Space* supplies the adjoint computations. The pairing-based self-adjointness of a reflection — the orthogonal reflection — belongs to the symmetric and antisymmetric categories of this Part and to *Hilbert Algebras*, Part II.

Throughout, $F$ is a field with $2 \neq 0$, $V$ is a finite-dimensional $F$-linear space, $E = \operatorname{End}_F(V)$, $r$ is a reflection of $V$, and $\alpha$ is a grade involution of $E$ with $\alpha_r(X) = rXr$ the one defined by $r$. The trace pairing is $\langle X,Y\rangle = \operatorname{tr}(XY)$ and ${}^{\dagger}$ is its adjoint.

## The Adjoint of the Reflection

**Proposition (the reflection is self-adjoint for its own signed sandwich).** With $\alpha = \alpha_r$ one has $\Theta^{\alpha}_{r,r^{-1}} = \mathrm{id}$, and therefore

$$
\bigl(\Theta^{\alpha_r}_{r,r^{-1}}\bigr)^{\dagger} = \mathrm{id} = \Theta^{\alpha_r}_{r,r^{-1}} ,
$$

so the reflection is self-adjoint and unitary for the signed sandwich it defines.

**Proof.** $\Theta^{\alpha_r}_{r,r^{-1}}(X) = r(rXr)r = X$ by $r^2=\mathrm{id}$, which is *Reflections as Signed Two-Sided Operators on a Linear Space*; the adjoint of the identity is the identity, and the identity is unitary.

**Proposition (the adjoint for a general grade involution).** For an arbitrary grade involution $\alpha$,

$$
\bigl(\Theta^{\alpha}_{r,r^{-1}}\bigr)^{\dagger} = \Theta^{\alpha}_{\alpha(r)^{-1},\alpha(r)} ,
$$

and this sandwich is always unitary; it is self-adjoint if and only if $\alpha(r)$ is an involution, $\alpha(r)^2=1$.

**Proof.** The adjoint formula of *The Signed Adjoint Sandwich on a Linear Space* with $a=r$ and $b=r^{-1}$ gives $\Theta^{\alpha}_{\alpha(r^{-1}),\alpha(r)}=\Theta^{\alpha}_{\alpha(r)^{-1},\alpha(r)}$. The unitarity parameter of the adjoint sandwich is $\alpha(r^{-1})\alpha(r)=\alpha(r)^{-1}\alpha(r)=1$, a central involution, so the sandwich is unitary by the criterion; self-adjointness requires $\alpha(r^{-1})=\alpha(r)$, that is $\alpha(r)^{-1}=\alpha(r)$, which is $\alpha(r)^2=1$.

**Corollary.** When $r$ commutes with $\alpha$, in particular when $\alpha=\alpha_r$, the signed inner sandwich of $r$ is self-adjoint; when $\alpha=\alpha_r$ it is the identity.

**Proof.** If $r$ commutes with $\alpha$ then $\alpha(r)=r$ and $\alpha(r)^2=r^2=1$, so the self-adjointness criterion holds; for $\alpha=\alpha_r$ the sandwich is $r\alpha_r(X)r^{-1}=r(rXr)r^{-1}=X$, the identity.

## Self-Adjointness of the Reflection as an Element

**Proposition.** A reflection $r$ is a self-adjoint **element** of $E$ with respect to a pairing-based involution $A \mapsto A^{*}$ — a different question from the self-adjointness of the sandwich operator — exactly when $r^{*}=r$, that is, when the reflection preserves the pairing; with respect to the trace pairing and the grade involution, the element $r$ is self-adjoint under the induced operator involution exactly when $r$ is central and even, $r=\alpha(r)$.

**Proof.** The first statement is the definition of the element adjoint $(r^{*}=r)$; the second is the computation $L_r^{*}=R_{r^{*}}$ of *The Adjoint of the Left Multiplication on a Linear Space* together with the criterion for a one-sided operator to be self-adjoint, which requires the parameter central and even.

**Remark (the failure in the degenerate cases).** In characteristic two a reflection is unipotent, the decomposition $V = V_+\oplus V_-$ with a sign does not exist, and the grade involution collapses to the identity, so the signed adjoint of the reflection is the ordinary adjoint and the sign disappears; this is the collapse of *Involutive Linear Spaces*. When the grade involution is the identity, the signed inner sandwich is the ordinary inner automorphism, its adjoint is the inverse inner automorphism, and the distinction between the signed and unsigned statements vanishes.

## Summary

For a reflection $r$ of $V$ the signed inner sandwich $\Theta^{\alpha_r}_{r,r^{-1}}$ is the identity, so the reflection is self-adjoint and unitary for the grade involution it defines; for a general grade involution $\alpha$ the adjoint of $\Theta^{\alpha}_{r,r^{-1}}$ is the signed sandwich $\Theta^{\alpha}_{\alpha(r)^{-1},\alpha(r)}$, always unitary and self-adjoint exactly when $\alpha(r)$ is an involution, which holds in particular when $r$ commutes with $\alpha$. As an element with respect to a pairing-based involution the reflection is self-adjoint exactly when it preserves the pairing; with respect to the trace pairing and the induced operator involution it is self-adjoint exactly when it is central and even. The statements collapse in characteristic two and when the grade involution is the identity.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F$, $V$, $E$ | the field, the space, the endomorphism algebra |
| $r$ | a reflection, $r^2=\mathrm{id}$, $\operatorname{rk}(r-\mathrm{id})=n-1$ |
| $\alpha_r(X)=rXr$ | the grade involution of $r$ |
| $\Theta^{\alpha}_{r,r^{-1}}(X)=r\alpha(X)r^{-1}$ | the signed inner sandwich of $r$ |
| $(\Theta^{\alpha}_{r,r^{-1}})^{\dagger}=\Theta^{\alpha}_{\alpha(r)^{-1},\alpha(r)}$ | its adjoint |
| $\langle X,Y\rangle=\operatorname{tr}(XY)$ | the trace pairing |

## Further Reading

- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for reflections, involutions and adjoints.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the self-adjointness of sandwiched involutions.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for reflections and the pairing they preserve.
