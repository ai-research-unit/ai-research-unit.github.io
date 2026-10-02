
# __The Signed Adjoint of the Reflection on a Complex Vector Space__

## Introduction

A reflection of a Hermitian space $V$ is the unitary self-adjoint involution
$$
\rho_u(v) = v - 2\,\frac{h(v,u)}{h(u,u)}\,u ,
$$
the reflection in the hyperplane orthogonal to the non-isotropic vector $u$; it satisfies $\rho_u^2 = \mathrm{id}$ and $\rho_u^{\dagger} = \rho_u$, so it is a **self-adjoint involution**, and it defines the grade involution $\alpha_r(X) = rXr$ of the endomorphism algebra. The reflection is the simplest signed operator: read as an operator on $E = \operatorname{End}_{\mathbb C}(V)$, its left and right multiplications and its inner signed sandwich are all self-adjoint for the Hermitian trace form $\langle X,Y\rangle = \operatorname{tr}(X^{\dagger}Y)$,
$$
L_r^{*} = L_r, \qquad R_r^{*} = R_r, \qquad \mathrm{Ad}_r^{*} = \mathrm{Ad}_r,
$$
because $r^{\dagger} = r$; the signed inner sandwich of the reflection is the identity, $\Theta^{\alpha_r}_{r,r^{-1}} = \mathrm{id}$, and the conjugation $\mathrm{Ad}_r$ is a self-adjoint involutive automorphism of $E$. The self-adjointness of all these operators is exactly the statement that the reflection is **real**, $r^{\dagger} = r$, in the sense of the Hermitian geometry; and the whole picture fails in the degenerate case, where the vector $u$ is isotropic, the reflection formula has no meaning, and the operators built from it lose their self-adjointness — the failure that the signed adjoint theory records as the failure of the criterion $a = \alpha(a^{\dagger})$.

The article has three sections: the reflection and its adjoint on $V$; the signed adjoints of the operators the reflection defines on the endomorphism algebra; and the failure in the degenerate case. The reflections and their geometric theory are *Isometries and Orthogonal Transformations* and *Reflections as Signed Two-Sided Operators on a Complex Vector Space*, the latter of this Part; the signed sandwich and its adjoint are *The Signed Sandwich on a Complex Vector Space* and *The Signed Adjoint Sandwich on a Complex Vector Space*, the latter the preceding article of this group; the adjoint of a Hermitian operator is *The Adjoint of a Hermitian Operator*; the Hermitian forms, the unitary group and the signatures are *Hermitian Geometry and the Unitary Group*; the degeneracy of a form and the radical are *Bilinear Forms*. None of that is re-derived.

Throughout, $V$ is a finite-dimensional complex vector space with a Hermitian form $h$, $r = \rho_u$ is a reflection of $V$, $T = r$ is the unitary self-adjoint involution of the grade involution, $\alpha_r(X) = rXr$, $\Lambda^{\alpha_r}_a$ and $\rho^{\alpha_r}_b$ and $\Theta^{\alpha_r}_{a,b}$ are the signed operators of the preceding articles, and $\langle X,Y\rangle = \operatorname{tr}(X^{\dagger}Y)$ is the Hermitian trace form of $E = \operatorname{End}_{\mathbb C}(V)$.

## The Reflection and Its Adjoint on $V$

**Proposition (the reflection is self-adjoint and unitary).** For $h(u,u) \neq 0$ the formula $\rho_u(v) = v - 2h(v,u)h(u,u)^{-1}u$ defines a complex-linear map with
$$
\rho_u^{2} = \mathrm{id}, \qquad \rho_u^{\dagger} = \rho_u, \qquad h(\rho_uv, \rho_uw) = h(v,w),
$$
so the reflection is a unitary self-adjoint involution; it fixes the hyperplane $u^{\perp}$ and acts as $-\mathrm{id}$ on the line $\mathbb{C}u$.

**Proof.** The map is complex-linear because $h(\cdot,u)$ is conjugate-linear and $u$ is a complex multiple of a conjugate-linear functional; $\rho_u(u) = -u$ and $\rho_u(v) = v$ for $h(v,u) = 0$; the involutivity, the self-adjointness and the unitarity are the computations $\rho_u^2 = \mathrm{id}$, $h(\rho_uv,w) = h(v,\rho_uw)$ and $h(\rho_uv,\rho_uw) = h(v,w)$, all by the definition and the sesquilinearity. The reflections and their classification are *Isometries and Orthogonal Transformations*.

**Corollary (the adjoint is the reflection itself).** The adjoint of the reflection on $V$ is the reflection, $\rho_u^{*} = \rho_u$, so the reflection is the Hermitian case of the self-adjoint operators of *The Adjoint of a Hermitian Operator*; its eigenvalues are $1$ on the hyperplane and $-1$ on the line, and its determinant is $-1$.

**Proof.** The self-adjointness $h(\rho_uv,w) = h(v,\rho_uw)$ is the proposition; the eigenvalues are read on the direct sum $u^{\perp}\oplus\mathbb{C}u$, and the determinant is the product $1^{m-1}\cdot(-1)$. This is *The Adjoint of a Hermitian Operator* and *Self-Adjoint Operators and the Spectral Theorem*.

## The Signed Adjoints of the Operators of the Reflection

**Proposition (the one-sided multiplications of the reflection).** The left and right multiplications of the reflection are self-adjoint, $L_r^{*} = L_r$ and $R_r^{*} = R_r$, and the conjugation is self-adjoint and involutive, $\mathrm{Ad}_r^{*} = \mathrm{Ad}_r$, $\mathrm{Ad}_r^{2} = \mathrm{id}$.

**Proof.** $L_r^{*} = L_{r^{\dagger}} = L_r$ and $R_r^{*} = R_{r^{\dagger}} = R_r$ by the unsigned adjoint law and $r^{\dagger}=r$; $\mathrm{Ad}_r^{*} = \mathrm{Ad}_{r^{\dagger}} = \mathrm{Ad}_r$, and $\mathrm{Ad}_r^{2} = \mathrm{Ad}_{r^2} = \mathrm{id}$. This is *The Adjoint of the Left Multiplication on a Complex Vector Space*.

**Proposition (the signed inner sandwich of the reflection).** With $\alpha_r(X) = rXr$ one has
$$
\Theta^{\alpha_r}_{r,r^{-1}} = \mathrm{id}, \qquad \bigl(\Theta^{\alpha_r}_{r,r^{-1}}\bigr)^{*} = \mathrm{id}, \qquad \Theta^{\alpha_r}_{r,r} = \mathrm{Ad}_r, \qquad \bigl(\Theta^{\alpha_r}_{r,r}\bigr)^{*} = \mathrm{Ad}_r ,
$$
so every signed operator of the reflection is self-adjoint, and the reflection is the fixed case of the signed adjoint criterion $a = \alpha_r(a^{\dagger})$.

**Proof.** $\Theta^{\alpha_r}_{r,r^{-1}}(X) = r\alpha_r(X)r^{-1} = r(rXr)r = r^{2}Xr^{2} = X$, using $r^{-1}=r$ and $r^{2}=\mathrm{id}$; the same computation gives $\Theta^{\alpha_r}_{r,r}(X) = X$, so the two coincide for an involution, and the adjoint of the identity is the identity. The conjugation is $\mathrm{Ad}_r(X) = rXr$, which is $\Theta^{\alpha_r}_{r,r^{-1}}\circ\alpha_r(X) = r\alpha_r(\alpha_r(X))r = rXr$; its adjoint is itself because $r^{\dagger}=r$. The criterion $a = \alpha_r(a^{\dagger})$ with $a=r$ is $r = r r^{\dagger} r = r^{3} = r$, which holds. This is *The Signed Adjoint Sandwich on a Complex Vector Space* and *Reflections as Signed Two-Sided Operators on a Complex Vector Space*.

**Remark (the reflection as the geometric realisation of the involution).** The reflection is the geometric source of the grade involutions of the endomorphism algebra: every unitary self-adjoint involution $T$ is a product of reflections by the Cartan–Dieudonné theorem, so the grade involutions that the signed theory uses are the conjugations of products of reflections, and the self-adjointness of the operators of $T$ is assembled from the self-adjointness of the operators of the reflections. This is *Isometries and Orthogonal Transformations*.

## The Failure in the Degenerate Case

**Proposition (the failure for isotropic vectors).** If $h(u,u) = 0$ with $u\neq0$, then the vector $u$ is isotropic, the reflection formula $v\mapsto v - 2h(v,u)h(u,u)^{-1}u$ is undefined, and no unitary self-adjoint involution acting as $-\mathrm{id}$ on $\mathbb{C}u$ and as $\mathrm{id}$ on a complement exists in general; when an operator $r$ with $r^2 = \mathrm{id}$ exists but fails to satisfy $r^{\dagger} = r$, the signed operators of $r$ are not self-adjoint, and the criterion $a = \alpha_r(a^{\dagger})$ fails.

**Proof.** The coefficient $h(u,u)^{-1}$ is undefined when $h(u,u)=0$; the hyperplane $u^{\perp}$ then contains $u$, so it is not a complement of the line and the reflection cannot be defined by the orthogonal splitting; and if $r^{\dagger}\neq r$ then $L_r^{*} = L_{r^{\dagger}}\neq L_r$, and the signed adjoint formula gives a signed sandwich different from the original. This is *Bilinear Forms* and *The Signed Sandwich on a Complex Vector Space*.

**Corollary (the role of the signature).** The reflections exist for the non-isotropic vectors, and their signed operators are self-adjoint exactly in the non-degenerate case; the degeneration of the form is the degeneration of the self-adjointness of the reflections, which is the operator face of the failure of the signature to be defined and of the radical to be trivial.

**Proof.** The existence and self-adjointness are the two propositions; the radical and the signature are *Bilinear Forms* and *Hermitian Geometry and the Unitary Group*.

**Example (the definite case and the Lorentzian case).** For the positive-definite form every nonzero vector is non-isotropic, so every vector defines a reflection, all the signed operators of the reflections are self-adjoint, and the Cartan–Dieudonné theorem generates $U(m)$ by reflections; for an indefinite form of signature $(p,q)$ with $p,q>0$ the isotropic vectors form the isotropic cone, the reflections are defined exactly off the cone, and the reflections generate the unitary group $U(p,q)$ but the isotropic directions have no reflection and the signed adjoint criterion fails along them. This is *Hermitian Geometry and the Unitary Group* and *Isometries and Orthogonal Transformations*.

## Summary

A reflection $\rho_u$ of a Hermitian space is a unitary self-adjoint involution, $\rho_u^2 = \mathrm{id}$, $\rho_u^{\dagger} = \rho_u$, fixing the hyperplane $u^{\perp}$ and negating the line $\mathbb{C}u$; on the endomorphism algebra with the trace form its left and right multiplications and its inner conjugation are self-adjoint, $L_r^{*} = L_r$, $R_r^{*} = R_r$, $\mathrm{Ad}_r^{*} = \mathrm{Ad}_r$, and the signed inner sandwich of the reflection is the identity with the identity adjoint, every signed operator of the reflection being self-adjoint. The criterion $a = \alpha_r(a^{\dagger})$ is satisfied by $a=r$, so the reflection is the model case of the signed self-adjointness; the reflections generate the unitary group by Cartan–Dieudonné, and so the self-adjointness of the signed theory is assembled from them. When the form is degenerate and $u$ isotropic the reflection is undefined and the self-adjointness fails, the operator face of the radical. The reflections are *Isometries and Orthogonal Transformations* and *Reflections as Signed Two-Sided Operators on a Complex Vector Space*; the signed adjoints are *The Signed Adjoint Sandwich on a Complex Vector Space*; the adjoint is *The Adjoint of a Hermitian Operator*; the degeneracy is *Bilinear Forms*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\rho_u(v)=v-2h(v,u)h(u,u)^{-1}u$ | the reflection in $u^{\perp}$ |
| $\rho_u^2=\mathrm{id}$, $\rho_u^{\dagger}=\rho_u$ | unitary self-adjoint involution |
| $\alpha_r(X)=rXr$ | the grade involution of the reflection |
| $L_r^{*}=L_r$, $R_r^{*}=R_r$, $\mathrm{Ad}_r^{*}=\mathrm{Ad}_r$ | self-adjointness of the operators of $r$ |
| $\Theta^{\alpha_r}_{r,r^{-1}}=\mathrm{id}$ | the signed inner sandwich of the reflection |
| $h(u,u)=0$ | the isotropic failure |

## Further Reading

- Jean Dieudonné, *La géométrie des groupes classiques* (Springer, third edition, 1971), for the reflections, the Cartan–Dieudonné theorem and the unitary groups.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the involutions, the reflections and the adjoints.
- Paul R. Halmos, *Finite-Dimensional Vector Spaces* (Springer, 1974), for the self-adjoint involutions, the reflections and the trace form.
- Sigurdur Helgason, *Differential Geometry, Lie Groups and Symmetric Spaces* (American Mathematical Society, 2001), for the reflections, the geodesic symmetries and the unitary groups of the indefinite forms.
