
# __The Signed Adjoint of the Geodesic Reflection__

## Introduction

The **geodesic reflection** is the isometry of a geometry fixing a geodesic, or a totally geodesic hypersurface, pointwise and reversing the normal, and read as a signed operator it is the **signed conjugation** $x \mapsto -axa^{-1}$ by the reflection element $a$; the adjoint of that signed operator is the **signed adjoint**, and the geodesic reflection is **self-adjoint** for the form it preserves because it is an involution and an isometry. The article develops the geodesic reflection together with its adjoint in the operator layer built from the involution: the reflection is the one-sided read of the signed conjugation, the adjoint is computed with respect to the form of the geometry and with respect to a grade involution, and the self-adjointness holds exactly up to the sign, failing in the degenerate case where the normal is isotropic or the characteristic is two.

The article develops the self-adjointness of the geodesic reflection for the form, the signed inner sandwich of the reflection and its identity for the grade involution the reflection defines, the signed adjoint for a general grade involution with the self-adjointness criterion, the geodesic instances in the Euclidean, the spherical and the hyperbolic geometries, and the degenerate case of the isotropic normal and the characteristic two. The geodesic reflection itself is *Geodesic Reflection as an Operator*, the signed sandwich and its adjoint are *The Signed Sandwich on an Ordered Algebra* and *The Signed Adjoint of the Reflection on a Linear Space*, and the article owns the geometric instance of the signed adjoint.

The article assumes *Geodesic Reflection as an Operator* for the reflection, the reflection element, the inversion and the symmetry; *The Adjoint under a Hermitian Pairing* for the adjoint and the self-adjoint elements; *Reflections as Signed Two-Sided Operators on a Linear Space* and *The Signed Adjoint of the Reflection on a Linear Space* of Part I for the signed inner sandwich and its adjoint; *The Signed Sandwich on an Ordered Algebra* of Part III for the signed sandwich; and *Clifford Algebras* of Part II and *Hyperbolic Geometry*, *Spherical Geometry* and *Euclidean Geometry* of this Part for the reflection elements and the geometries. No physics is invoked.

## The Geodesic Reflection and Its Self-Adjointness

### The Reflection and the Form

**Definition.** Let $(V,q)$ be a quadratic space over a field of characteristic not two with the polar form $B$, and let $a \in V$ with $q(a) \neq 0$; the **reflection** in the hyperplane $a^\perp$ is

$$
\rho_a(x) = x - 2\,\frac{B(x,a)}{q(a)}\,a ,
$$

the geodesic reflection of *Geodesic Reflection as an Operator*; in the Clifford algebra it is the signed conjugation $\rho_a(x) = -a\,x\,a^{-1}$, and it is the reflection element $a$ that carries the geometry.

**Theorem.** The geodesic reflection preserves the quadratic form, $q(\rho_a x) = q(x)$, so it is an isometry of the form; it is an involution, $\rho_a^2 = \mathrm{id}$; consequently it is **self-adjoint** and **unitary** with respect to the pairing of the form,

$$
\rho_a^{\dagger} = \rho_a^{-1} = \rho_a , \qquad \rho_a^{\dagger}\rho_a = \mathrm{id} ,
$$

and the self-adjointness is the statement that a reflection is its own adjoint, which holds for every reflection of a nondegenerate form.

**Proof.** The preservation is the computation $q(\rho_a x) = q(x)$ of the reflection; the square is the identity because the reflection formula applied twice returns $x$, and the two facts give the adjoint: $h(\rho_a x, y) = h(\rho_a x, \rho_a \rho_a y) = h(x, \rho_a y)$ using the preservation with the substitution $y = \rho_a \rho_a y$, so $\rho_a^{\dagger} = \rho_a$; the unitarity is the combination of the self-adjointness and the involution. The statement is in *Geodesic Reflection as an Operator* and *The Adjoint under a Hermitian Pairing*.

**Corollary.** The self-adjointness of the geodesic reflection is exactly the self-adjointness of the reflection as an element: the reflection element $a$ satisfies $a^{*} = a$ for the adjoint induced by the form (the reflection preserves the pairing), and the reflection operator is self-adjoint for the trace pairing of the endomorphism algebra in the sense of the next sections. The two statements — the geometric and the algebraic — are the same fact read on the space and on the algebra.

### The Element and the Operator

**Proposition.** The reflection element $a$ is self-adjoint for the form, and the geodesic reflection is the signed sandwich $\Theta^{\alpha_a}_{a,a^{-1}}$ with the grade involution $\alpha_a(X) = aXa$ defined by the reflection; the reflection preserves the form and its polar, and it is the case of the signed sandwich in which the two parameters are inverse to each other.

**Proof.** The element $a$ is a vector and its adjoint with respect to the symmetric form is itself, $a^{*} = a$; the conjugation $x \mapsto axa^{-1}$ is the signed sandwich by $a$ and $a^{-1}$, and its negative on the vectors is the reflection formula. The statement is in *Reflections as Signed Two-Sided Operators on a Linear Space* and *Clifford Algebras*.

## The Signed Inner Sandwich of the Reflection

**Definition.** Let $E = \operatorname{End}_F(V)$ be the endomorphism algebra with the trace pairing $\langle X,Y\rangle = \operatorname{tr}(XY)$, let $\dagger$ be its adjoint, let $r$ be a reflection of $V$ and let $\alpha$ be a grade involution of $E$; the **signed inner sandwich** of the reflection is

$$
\Theta^{\alpha}_{r,r^{-1}}(X) = r\,\alpha(X)\,r^{-1} .
$$

**Theorem.** With the grade involution $\alpha_r(X) = rXr$ defined by the reflection, the signed inner sandwich is the identity,

$$
\Theta^{\alpha_r}_{r,r^{-1}} = \mathrm{id} ,
$$

so the reflection is **self-adjoint and unitary** for its own signed sandwich,

$$
\bigl(\Theta^{\alpha_r}_{r,r^{-1}}\bigr)^{\dagger} = \mathrm{id} = \Theta^{\alpha_r}_{r,r^{-1}} ;
$$

the geodesic reflection is therefore self-adjoint for the signed structure it defines, and its signed adjoint is itself.

**Proof.** The sandwich is $r(rXr)r^{-1} = X$ using $r^2 = \mathrm{id}$ and $r^{-1} = r$, which is the identity; the adjoint of the identity is the identity, and the identity is unitary. The statement is *The Signed Adjoint of the Reflection on a Linear Space*, applied to the geodesic reflection.

**Remark (the trivial sandwich and the geodesic meaning).** The identity of the signed inner sandwich is the algebraic form of the statement that the reflection is its own inverse: the sandwich of the reflection with itself is the identity, and the reflection reverses the normal and fixes the hypersurface, which is the geometric content of the involution. The geodesic reflection of the geometry is thus the model of a signed two-sided operator that is self-adjoint for its own sign.

## The Signed Adjoint for a General Grade Involution

**Theorem.** For an arbitrary grade involution $\alpha$ the adjoint of the signed inner sandwich of the reflection is

$$
\bigl(\Theta^{\alpha}_{r,r^{-1}}\bigr)^{\dagger} = \Theta^{\alpha}_{\alpha(r)^{-1},\,\alpha(r)} ,
$$

the signed sandwich by the inverse image of the parameter; the sandwich is always **unitary**, and it is **self-adjoint** if and only if $\alpha(r)$ is an involution,

$$
\alpha(r)^2 = \mathrm{id} .
$$

**Proof.** The adjoint formula of the signed adjoint sandwich with the parameters $r$ and $r^{-1}$ gives $\Theta^{\alpha}_{\alpha(r^{-1}),\alpha(r)} = \Theta^{\alpha}_{\alpha(r)^{-1},\alpha(r)}$; the unitarity parameter is $\alpha(r^{-1})\alpha(r) = \alpha(r)^{-1}\alpha(r) = 1$, a central element, so the sandwich is unitary; the self-adjointness requires $\alpha(r^{-1}) = \alpha(r)$, that is, $\alpha(r)^{-1} = \alpha(r)$, which is $\alpha(r)^2 = \mathrm{id}$. The statement is in *The Signed Adjoint of the Reflection on a Linear Space*.

**Corollary.** When the reflection commutes with the grade involution, in particular when $\alpha = \alpha_r$, the signed inner sandwich of the reflection is self-adjoint; the general reflection is self-adjoint for the sign it defines and unitary for every sign. The geodesic reflection is therefore self-adjoint for the grade involution of the reflection and unitary for every grade involution, and the self-adjointness fails only when the sign is carried by an element that does not commute with the reflection.

**Proof.** If $r$ commutes with $\alpha$ then $\alpha(r) = r$ and $\alpha(r)^2 = r^2 = \mathrm{id}$, so the criterion of the theorem holds; for $\alpha = \alpha_r$ the sandwich is the identity. The statement is the corollary of the model article.

## The Geodesic Instances

**Example (the Euclidean and the spherical reflection).** In the Euclidean space the reflection in the hyperplane $a^\perp$ has the reflection element $a$ of positive square, $q(a) > 0$; the reflection is self-adjoint for the Euclidean form, the signed inner sandwich of the reflection is the identity for the sign it defines, and the general sign gives the unitary sandwich of the theorem. On the sphere the reflection in a great sphere is the restriction of the Euclidean reflection, and the same statements hold with the ambient form.

**Example (the hyperbolic reflection).** In the hyperboloid model the reflection in the geodesic hyperplane with the spacelike normal $a$ has $B(a,a) > 0$ and the reflection element $a$ of positive square for the spacelike form; the reflection is self-adjoint for the form of signature $(n,1)$, the signed adjoint is the self-adjoint signed sandwich, and the reflection in a geodesic of the hyperbolic plane is the inversion of the Möbius model, whose sign is the orientation reversal of *Geodesic Reflection as an Operator*. The self-adjointness for the ambient form is the statement that the hyperbolic reflection preserves the form, and the signed adjoint records the sign of the orientation.

**Remark (the sign and the geometry).** The sign of the signed adjoint of the geodesic reflection is the sign of the orientation reversal of the reflection: the reflection reverses the normal and the orientation in the ambient space, and the signed adjoint carries the same sign. The two structures — the form and the orientation — are the two ingredients of the article, and the geodesic reflection is self-adjoint for the form and sign-reversing for the orientation.

## The Degenerate Case

**Definition.** The **degenerate case** of the geodesic reflection is the case in which the normal is **isotropic**, $q(a) = 0$, or the characteristic is two; in the first case the reflection element $a$ has no inverse in the Clifford algebra, the formula $\rho_a(x) = -axa^{-1}$ loses its meaning, and the reflection is not defined as a signed conjugation; in the second case the reflection is unipotent, the decomposition $V = V_+ \oplus V_-$ with a sign does not exist, and the grade involution collapses to the identity.

**Theorem.** When the normal is isotropic the geodesic reflection of the form fails to exist, the signed adjoint of the reflection is undefined, and the self-adjointness cannot be asserted; when the characteristic is two the reflection is unipotent with $(\rho_a - \mathrm{id})^2 = 0$, the sign of the decomposition disappears, and the signed adjoint of the reflection is the ordinary adjoint, so the distinction between the signed and the unsigned statements vanishes.

**Proof.** For $q(a) = 0$ the inverse $a^{-1} = a/q(a)$ does not exist and the Clifford sandwich is undefined; in characteristic two the reflection formula is $\rho_a(x) = x - B(x,a)a$ with $B(a,a) = q(a) \neq 0$ but the two eigenspaces $\pm1$ coalesce into the unipotent form, and the grade involution of the associated structure is the identity. The statement is the degenerate-case analysis of *The Signed Adjoint of the Reflection on a Linear Space*, *Clifford Algebras* and *Degenerate Clifford Algebras and the Radical*.

**Remark (the boundary of the article).** The self-adjointness of the geodesic reflection is a statement of the nondegenerate case, and its failure in the degenerate case is the exact boundary of the signed structure: the reflection needs the inverse of its element and the form needs the nondegeneracy for the adjoint to exist. The article marks the two failures and leaves the degenerate theory to *Degenerate Clifford Algebras and the Radical* and to the indefinite geometry of the quadratic forms.

## Summary

The geodesic reflection $\rho_a(x) = x - 2B(x,a)a/q(a)$ preserves the form, is an involution, and is therefore **self-adjoint and unitary** for the form, $\rho_a^{\dagger} = \rho_a^{-1} = \rho_a$; the reflection is the signed sandwich $\Theta^{\alpha_a}_{a,a^{-1}}$ with the grade involution it defines, and that signed inner sandwich is the identity, so the reflection is self-adjoint for its own sign. For a general grade involution $\alpha$ the signed adjoint of the reflection is $\bigl(\Theta^{\alpha}_{r,r^{-1}}\bigr)^{\dagger} = \Theta^{\alpha}_{\alpha(r)^{-1},\alpha(r)}$, always unitary and self-adjoint exactly when $\alpha(r)^2 = \mathrm{id}$, which holds in particular when the reflection commutes with the sign. The Euclidean, the spherical and the hyperbolic reflections are the geodesic instances, self-adjoint for their ambient forms and carrying the sign of the orientation reversal. In the degenerate case the isotropic normal $q(a) = 0$ makes the reflection element non-invertible and the signed adjoint undefined, and in characteristic two the reflection is unipotent and the sign collapses; these are the two boundaries of the self-adjointness of the geodesic reflection.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\rho_a(x) = x - 2B(x,a)a/q(a)$ | Geodesic reflection with the reflection element $a$ |
| $\rho_a = -a(\cdot)a^{-1}$ | Signed conjugation form of the reflection |
| $\rho_a^{\dagger} = \rho_a^{-1} = \rho_a$ | Self-adjointness and unitarity for the form |
| $r$, $r^2 = \mathrm{id}$ | Reflection of the space |
| $\alpha_r(X) = rXr$ | Grade involution defined by the reflection |
| $\Theta^{\alpha}_{r,r^{-1}}(X) = r\alpha(X)r^{-1}$ | Signed inner sandwich |
| $\Theta^{\alpha_r}_{r,r^{-1}} = \mathrm{id}$ | Self-adjointness of the reflection |
| $(\Theta^{\alpha}_{r,r^{-1}})^{\dagger} = \Theta^{\alpha}_{\alpha(r)^{-1},\alpha(r)}$ | Signed adjoint for a general sign |
| $\alpha(r)^2 = \mathrm{id}$ | Self-adjointness criterion |
| $q(a) = 0$ | Isotropic normal, the degenerate case |

## Further Reading

- Nicolas Bourbaki, *Algebra I: Chapters 1–3* (Springer, 1998), for the reflections, the involutions and the adjoints.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions* (American Mathematical Society, 1998), for the self-adjointness of the sandwiched involutions.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the reflections, the spin groups and the forms they preserve.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2001), for the reflection formula and the Cartan–Dieudonné theorem.
- John G. Ratcliffe, *Foundations of Hyperbolic Manifolds*, 2nd ed. (Springer, 2006), for the geodesic reflections and the hyperbolic isometries.
