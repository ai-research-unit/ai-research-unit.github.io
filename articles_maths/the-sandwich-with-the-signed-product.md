# __The Sandwich with the Signed Product__

## Introduction

The signed two-sided operators of *Two-Sided Operators with the Signed Product* become a family of conjugations when the two parameters are a unit and its inverse. The **signed sandwich** is

$$
\Sigma_x(y) = T^{\alpha}_{x,\,x^{-1}}(y) = x\,\alpha(y)\,x^{-1},
$$

the ordinary inner conjugation of the argument twisted by the grading. It is the map that carries the reflections on the nose: for a vector $u$ of nonzero norm the signed sandwich $\Sigma_u$ is the reflection $\rho_u$, where the ordinary inner conjugation returned $-\rho_u$ and the twisted conjugation $\chi_u$ also returned $\rho_u$ but by a different route. What the signed sandwich adds is that it does this with the ordinary inverse $x^{-1}$, so that the whole discussion stays inside the one-parameter family of conjugations.

The article has three parts. It fixes the signed sandwich, its relation to the inner conjugation and to the twisted conjugation, and the value at the unit, which is the grade involution. It computes the composition, and finds that the product of **two** signed sandwiches is not signed but is an ordinary inner conjugation, the two grade involutions cancelling – the sandwich form of the coset structure of the parent family. And it reads the versor action: a versor acts on the quadratic space by an isometry, the odd versors give the reflections, the even ones give minus a rotation, and the products generate the orthogonal group.

The ordinary sandwich and the twisted conjugation are *The Sandwich on a Clifford Algebra*; the signed family and its composition laws are *Two-Sided Operators with the Signed Product*; the signed inner conjugation $\alpha(x)yx^{-1}$, whose left factor carries the sign, is *Two-Sided Operators on a Clifford Algebra with Signed Inner Conjugation*; the versors, the reflections and the groups are *The Clifford, Pin and Spin Groups with Signed Inner Conjugation* and *The Two-Sided Operators and the Spin Group*. Those are cited. The base is a field $F$ of characteristic not $2$, $q$ is non-degenerate and $\alpha$ is the grade involution.

## The Signed Sandwich

**Definition.** For a unit $x \in \mathrm{Cl}(V,q)^{\times}$ the **signed sandwich** by $x$ is

$$
\Sigma_x(y) = x\,\alpha(y)\,x^{-1}, \qquad y \in \mathrm{Cl}(V,q).
$$

**Proposition (the three conjugations).** Let $x$ be homogeneous of degree $k$ with $\varepsilon_x = (-1)^{k}$. Then

$$
\Sigma_x = \mathrm{Ad}_x\circ\alpha = \alpha\circ\mathrm{Ad}_x, \qquad \Sigma_x(v) = -\varepsilon_x\,\chi_x(v) \quad (v \in V),
$$

where $\mathrm{Ad}_x(y) = xyx^{-1}$ is the inner conjugation and $\chi_x(y) = xy\alpha(x)^{-1}$ is the twisted conjugation. So the signed sandwich is the inner conjugation with the argument twisted, it is also the inner conjugation conjugated by $\alpha$, and on the vectors it differs from the twisted conjugation by the sign $-\varepsilon_x$.

**Proof.** $\Sigma_x(y) = x\alpha(y)x^{-1} = \alpha\bigl(\alpha(x)y\alpha(x)^{-1}\bigr) = \alpha\,\mathrm{Ad}_{\alpha(x)}(y) = \alpha\,\mathrm{Ad}_x\,\alpha(y)$ because $\mathrm{Ad}_{\alpha(x)} = \alpha\mathrm{Ad}_x\alpha$; hence $\Sigma_x = \mathrm{Ad}_x\alpha = \alpha\mathrm{Ad}_x$. The vector statement is $\chi_x = \varepsilon_x\mathrm{Ad}_x$, so $x\alpha(v)x^{-1} = -xvx^{-1} = -\varepsilon_x\chi_x(v)$.

**Proposition (elementary properties).** $\Sigma_x$ is $F$-linear and bijective with inverse $\Sigma_{x^{-1}}$; $\Sigma_x(1) = 1$; $\Sigma_1 = \alpha$; and $\Sigma_x$ preserves the grading of the algebra modulo two, since it is a composition of the automorphism $\alpha$ with the automorphism $\mathrm{Ad}_x$.

**Proof.** $\Sigma_x$ is a composite of bijections; $\alpha(1) = 1$ and $x1x^{-1} = 1$; $\Sigma_1 = \alpha$; both $\alpha$ and $\mathrm{Ad}_x$ preserve the parity grading.

**Proposition (the composition law and the cancellation).** For units $x, z$,

$$
\Sigma_x \circ \Sigma_z = T_{x\alpha(z),\ \alpha(z)^{-1}x^{-1}} = \mathrm{Ad}_{x\,\alpha(z)} .
$$

So the composite of two signed sandwiches is an **ordinary inner conjugation**, with parameter $x\alpha(z)$; the two grade involutions cancel, exactly as for the general signed product.

**Proof.** By the composition law of *Two-Sided Operators with the Signed Product*, $T^{\alpha}_{x,x^{-1}}\circ T^{\alpha}_{z,z^{-1}} = T_{x\alpha(z),\ \alpha(z^{-1})x^{-1}}$; and $\alpha(z^{-1}) = \alpha(z)^{-1}$, while $\bigl(x\alpha(z)\bigr)^{-1} = \alpha(z)^{-1}x^{-1}$, so the parameters are a unit and its inverse and the result is the inner conjugation $\mathrm{Ad}_{x\alpha(z)}$.

**Corollary (the group generated).** The signed sandwiches generate together with their products the group

$$
\{\, \mathrm{Ad}_y : y \in \mathrm{Cl}(V,q)^{\times} \,\} \cup \{\, \Sigma_x : x \in \mathrm{Cl}(V,q)^{\times} \,\},
$$

in which the signed sandwiches form the nontrivial coset of the inner conjugations, since $\Sigma_x = \mathrm{Ad}_x\alpha$ and $\alpha$ is not an inner conjugation. No signed sandwich is the identity, and the square of one is the inner conjugation $\Sigma_x^{2} = \mathrm{Ad}_{x\alpha(x)}$.

**Proof.** $\Sigma_x\Sigma_z = \mathrm{Ad}_{x\alpha(z)}$ is the composition law; $\Sigma_x = \mathrm{Ad}_x\alpha$ is the first proposition, and $\alpha$ is an automorphism but not of the form $\mathrm{Ad}_y$, because it does not fix the odd part; the square is the law with $z = x$, giving $x\alpha(x)$.

**Remark (the value at the unit and the odd part).** $\Sigma_x(1) = 1$ for every unit, so unlike the general signed two-sided operator the signed sandwich is not detected by the unit; what distinguishes it from the ordinary inner conjugation is the odd part. Precisely, $\Sigma_x = \mathrm{Ad}_x\circ\alpha$ agrees with the inner conjugation on the even part, $\Sigma_x = \mathrm{Ad}_x$ on $\mathrm{Cl}^{0}$, and equals its negative on the odd part, $\Sigma_x = -\mathrm{Ad}_x$ on $\mathrm{Cl}^{1}$; this holds for every unit $x$, whatever its parity, and it is the sharp statement of the cancellation in the composition law.

## The Reflections and the Versor Action

**Theorem (the reflections).** Let $u \in V$ with $q(u) \neq 0$. Then $\Sigma_u$ restricted to $V$ is the reflection in $u^{\perp}$:

$$
\Sigma_u(v) = u\,\alpha(v)\,u^{-1} = -u\,v\,u^{-1} = \rho_u(v), \qquad v \in V .
$$

**Proof.** This is the reflection theorem of *Two-Sided Operators with the Signed Product*, in the sandwich form $b = u^{-1}$.

**Theorem (the versor action).** Let $x$ be a versor, so that $\chi_x(V) \subseteq V$. Then $\Sigma_x$ preserves $V$ and its restriction is an isometry,

$$
q\bigl(\Sigma_x(v)\bigr) = q(v), \qquad B\bigl(\Sigma_x(v),\Sigma_x(w)\bigr) = B(v,w), \qquad v, w \in V,
$$

and the map $x \mapsto \Sigma_x\big|_V$ is a homomorphism from the Clifford group into $O(V,q)$ whose restriction to the even versors carries a rotation $R$ to $-\mathrm{Ad}_R = -\chi_R$, the rotation composed with the central element $-1$, and whose value on an odd versor $u$ is the reflection $\rho_u$.

**Proof.** $\Sigma_x$ is a bijection preserving $V$ because $\chi_x$ is and the two differ on $V$ by the nonzero scalar $-\varepsilon_x$; an isometry scaled by a nonzero scalar is an isometry. The value on the even and the odd part is the sign computation of the first proposition, together with $\chi_u = \rho_u$ and $\chi_R = \mathrm{Ad}_R$ for the twisted conjugation.

**Corollary (Cartan–Dieudonné).** Every orthogonal transformation of the quadratic space is a composite of signed sandwiches: in even dimension it is $\Sigma_{u_1}\cdots\Sigma_{u_{2k}} = \mathrm{Ad}_{u_1\cdots u_{2k}}$ for vectors of nonzero norm, an even product, and a reflection is a single $\Sigma_u$.

**Proof.** The reflections generate $O(V,q)$ and each is a $\Sigma_u$; their products are composites of signed sandwiches, which by the cancellation are inner conjugations of products of vectors.

**Remark (the three sandwiches distinguished).** The ordinary sandwich $T_{x,x^{-1}} = \mathrm{Ad}_x$ is multiplicative and has value $1$ at the unit but gives $-\rho_u$ on a vector; the twisted conjugation $\chi_x$ gives $\rho_u$ but uses $\alpha(x)^{-1}$, not $x^{-1}$; the signed sandwich $\Sigma_u$ gives $\rho_u$ and uses $x^{-1}$, at the price of a family that is a coset and not a group. The three are related by $\chi_x = \varepsilon_x\mathrm{Ad}_x$ and $\Sigma_x = -\varepsilon_x\chi_x$ on $V$.

## Worked Cases

### A Reflection in $\mathrm{Cl}_{0,3}(\mathbb{R})$

With $e_j^{2} = -1$ let $x = e_1$, so $x^{-1} = -e_1$ and $\alpha(e_j) = -e_j$. Then $\Sigma_{e_1}(v) = e_1\alpha(v)(-e_1) = e_1ve_1$, and on the basis $(-e_1, e_2, e_3)$: the reflection $\rho_{e_1}$. The square is $\Sigma_{e_1}^{2} = \mathrm{Ad}_{e_1\alpha(e_1)} = \mathrm{Ad}_{-e_1^{2}} = \mathrm{Ad}_1 = \mathrm{id}$, which is the reflection squared.

### An Even Versor

In the same algebra let $R = e_1e_2$. Then $\Sigma_R$ acts on the basis of $V$ by $(e_1, e_2, -e_3)$, which is $-\mathrm{Ad}_R$, the half-turn composed with the central element $-1$; on the even part it agrees with $\mathrm{Ad}_R$, as the previous remark states. The product $\Sigma_R\Sigma_{e_1} = \mathrm{Ad}_{R\alpha(e_1)} = \mathrm{Ad}_{-e_1e_2e_1} = \mathrm{Ad}_{e_2}$ is an inner conjugation, as the composition law requires.

### Two Reflections

With $u = e_1$ and $w = e_2$, $\Sigma_u\Sigma_w = \mathrm{Ad}_{u\alpha(w)} = \mathrm{Ad}_{e_1(-e_2)} = \mathrm{Ad}_{-e_1e_2} = \mathrm{Ad}_{e_1e_2}$, which acts on the basis by $(-e_1,-e_2,e_3)$: the rotation through the full angle in the $e_1,e_2$ plane, the product of the two reflections. The cancellation of the two involutions is visible in the sign of the parameter.

## Summary

The **signed sandwich** $\Sigma_x(y) = x\alpha(y)x^{-1}$ is the inner conjugation with the argument twisted by the grading; it equals $\mathrm{Ad}_x\circ\alpha = \alpha\circ\mathrm{Ad}_x$, it is bijective with inverse $\Sigma_{x^{-1}}$, and $\Sigma_1 = \alpha$. On the vectors it equals $-\varepsilon_x\chi_x$, so it agrees with the twisted conjugation on the odd part up to sign and with the inner conjugation on the even part. Its composition law is the cancellation statement: **two signed sandwiches give an ordinary inner conjugation**, $\Sigma_x\Sigma_z = \mathrm{Ad}_{x\alpha(z)}$, with square $\Sigma_x^{2} = \mathrm{Ad}_{x\alpha(x)}$; the family is the nontrivial coset of the inner conjugations, a torsor and not a group. A vector $u$ gives the reflection $\Sigma_u = \rho_u$; therefore the signed sandwiches carry the reflections, their products carry the rotations, and through Cartan–Dieudonné they generate the orthogonal group. The ordinary sandwich, the twisted conjugation and the versor action are *The Sandwich on a Clifford Algebra*; the signed family is *Two-Sided Operators with the Signed Product*; the groups are *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Sigma_x(y) = x\,\alpha(y)\,x^{-1}$ | Signed sandwich |
| $\Sigma_x = \mathrm{Ad}_x\circ\alpha = \alpha\circ\mathrm{Ad}_x$ | Relation to the inner conjugation |
| $\Sigma_x = -\varepsilon_x\chi_x$ on $V$ | Relation to the twisted conjugation |
| $\Sigma_x\circ\Sigma_z = \mathrm{Ad}_{x\alpha(z)}$ | Two signed sandwiches give an inner conjugation |
| $\Sigma_x^{2} = \mathrm{Ad}_{x\alpha(x)}$ | Square of a signed sandwich |
| $\Sigma_1 = \alpha$ | Value at the unit |
| $\Sigma_u = \rho_u$ | Reflection by a vector of nonzero norm |
| $\mathrm{Ad}_x$, $\chi_x$, $T_{x,x^{-1}}$ | Inner conjugation; twisted conjugation; ordinary sandwich |

## Further Reading

- Claude Chevalley, *The Algebraic Theory of Spinors and Clifford Algebras*, Collected Works vol. 2 (Springer, 1997), for the two conjugation actions and the reflections.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the reflection formula and the versor action on the vectors.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups*, Cambridge Studies in Advanced Mathematics 50 (Cambridge University Press, 1995), for the signed conjugations and the orthogonal group.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for the reflection formula in the low-dimensional algebras.
- Winfried Scharlau, *Quadratic and Hermitian Forms*, Grundlehren der mathematischen Wissenschaften 270 (Springer, 1985), for the orthogonal group generated by reflections.
