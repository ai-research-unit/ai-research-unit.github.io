
# __Reflections as Signed Two-Sided Operators on a Symmetry Group__

## Introduction

A **reflection** of a quadratic space is an involutive isometry fixing a hyperplane pointwise and negating a line transverse to it, and the theorem of Cartan–Dieudonné says that the reflections generate the whole orthogonal group. The reflection is an operator of a special shape, and the shape is two-sided: in the pin group of the form the reflection in the hyperplane $u^{\perp}$ is the **signed inner conjugation** by the vector $u$,

$$
\rho_u(v) = u\,\alpha(v)\,u^{-1}, \qquad v \in V,
$$

while the unsigned inner conjugation $uvu^{-1}$ gives its negative. This article treats a single reflection as a signed two-sided operator: the involution property, the fixed hyperplane, the eigenvalues, the determinant, the generation of the rotation group by products of two reflections, and the failure of the whole correspondence for isotropic vectors and for a degenerate form. It is the single-reflection case of *The Signed Sandwich on a Symmetry Group*, the previous article of this group, and it isolates what the reflection adds to the general signed sandwich: the involution and the hyperplane.

Reflections, their generation theorem and the orthogonal group are *Isometries and Orthogonal Transformations*; the sign of a reflection and its place in the orientation are *The Rotation Group and Orientation*; the realisation in the Clifford algebra, the pin group and the signed inner conjugation are *The Clifford, Pin and Spin Groups with Signed Inner Conjugation* and *Two-Sided Operators on a Clifford Algebra with Signed Inner Conjugation*, and the reflection formula there is quoted, not re-derived. The signed sandwich and the grade involution are the previous article of this group. No adjoint is taken; the adjoint of the reflection is *The Signed Adjoint of the Reflection on a Symmetry Group*, in the group `- * Operator Theory` of this category.

The article has four sections: the reflections of a form; the reflection as a signed two-sided operator; its properties and the generation of the rotations; and the failure in the degenerate case. Throughout, $V$ is a finite-dimensional space over a field $F$ of characteristic not $2$ with a non-degenerate quadratic form $q$ and polar form $B$, $u \in V$ a vector of nonzero norm, and $\rho_u$ the reflection in $u^{\perp}$.

## The Reflections of a Form

### Definition and Elementary Form

**Definition.** For $u \in V$ with $q(u) \neq 0$ the **reflection** in the hyperplane $u^{\perp} = \{v : B(v,u) = 0\}$ is the linear map

$$
\rho_u : V \longrightarrow V, \qquad \rho_u(v) = v - 2\,\frac{B(v,u)}{q(u)}\,u .
$$

**Proposition.** The map $\rho_u$ is linear, fixes $u^{\perp}$ pointwise, sends $u$ to $-u$, and is an involution: $\rho_u^2 = \mathrm{id}$. It is an isometry of $q$, $q(\rho_u v) = q(v)$ for all $v$, and it has determinant $-1$ and the two eigenvalues $+1$ (on $u^{\perp}$, of multiplicity $\dim V - 1$) and $-1$ (on the line $Fu$).

**Proof.** Linearity and the fixed hyperplane are immediate from the formula; the value at $u$ is $u - 2q(u)^{-1}q(u)u = -u$. For the involution, $B(\rho_u v,u) = B(v,u) - 2q(u)^{-1}B(v,u)q(u) = -B(v,u)$, so applying $\rho_u$ twice returns $v$. The isometry property follows from $q(\rho_uv) = q(v) - 2\frac{B(v,u)}{q(u)}B(v,u) + \frac{B(v,u)^2}{q(u)^2}q(u) = q(v)$ after two applications of the polar relation; the determinant and the spectrum are read off the decomposition $V = u^{\perp}\oplus Fu$.

### The Generation of the Orthogonal Group

**Theorem (Cartan–Dieudonné).** Every element of the orthogonal group $\operatorname{O}(V,q)$ is a product of at most $\dim V$ reflections, and every element of the rotation group $\operatorname{O}^+(V,q)$ is a product of an even number of reflections. The reflections generate $\operatorname{O}(V,q)$, and the determinant is the parity of the number of factors.

**Proof sketch.** The proof is by induction on the dimension: given $g \in \operatorname{O}(V,q)$ and a vector $u$ with $g(u) \neq u$, the composite $\rho_{g(u)-u}\circ g$ fixes $u$ and reduces to a reflection on $u^{\perp}$, where the induction applies; the parity statement follows from $\det\rho_u = -1$. This is *Isometries and Orthogonal Transformations*.

## The Reflection as a Signed Two-Sided Operator

### The Two-Sided Form of the Reflection

**Definition.** On the Clifford algebra $\mathrm{Cl}(V,q)$ the **signed full reflection** by $u$ is the signed inner conjugation

$$
\mathrm{Ad}^{\alpha}_u(x) = u\,\alpha(x)\,u^{-1}, \qquad x \in \mathrm{Cl}(V,q),
$$

where $\alpha$ is the grade involution, *The Signed Sandwich on a Symmetry Group*.

**Theorem.** The restriction of the signed inner conjugation to the vectors is the reflection:

$$
\mathrm{Ad}^{\alpha}_u(v) = \rho_u(v) \quad \text{for every } v \in V,
\qquad \text{whereas} \qquad \mathrm{Ad}_u(v) = u v u^{-1} = -\rho_u(v) .
$$

Hence the reflection of the form is a signed two-sided operator and the unsigned two-sided operator is its negative.

**Proof.** For a vector $u$ one has $\alpha(u) = -u$, so $\mathrm{Ad}^{\alpha}_u(v) = -uvu^{-1}$; the fundamental relation $uvu = 2B(u,v)u - q(u)v$ of the Clifford algebra gives $uvu^{-1} = 2B(u,v)q(u)^{-1}u - v = -\rho_u(v)$, and the two displayed identities follow. This is *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*, quoted.

### The Sandwich with a Vector on One Side

**Proposition (why the one-sided form is not a reflection).** The signed sandwich with one vector parameter,

$$
S^{\alpha}_{u,e}(x) = u\,\alpha(x), \qquad S^{\alpha}_{e,u}(x) = \alpha(x)\,u,
$$

is a bijection of the Clifford algebra, with inverses $y \mapsto \alpha(u^{-1}y)$ and $y \mapsto \alpha(yu^{-1})$, but it does **not** preserve the subspace $V$ of vectors, so it restricts to no operator of the quadratic space and is not a reflection. The two-sided operator $x \mapsto u\,\alpha(x)\,u^{-1}$ does preserve $V$, and it is the reflection.

**Proof.** The inverse computation is $u\,\alpha\bigl(\alpha(u^{-1}y)\bigr) = u\,u^{-1}y = y$. For the failure, a vector $v$ has $\alpha(v) = -v$, so $u\,\alpha(v) = -uv$, and the product of the two vectors $u, v$ is the scalar $B(u,v)$ plus the bivector $u\wedge v$; hence $-uv$ is a vector exactly when $u\wedge v = 0$, that is when $v$ is a multiple of $u$. The two-sided statement is the reflection theorem above.

**Remark.** The contrast is the point. The one-sided signed operator shifts the space; the two-sided signed operator with the inverse on the right fixes the hyperplane. This is why the geometry of reflections lives in the two-sided layer, and why the signed left multiplication of the next article is an operator of a different kind.

## Properties and the Rotation

### Involution, Hyperplane and Spectrum

**Proposition.** The signed inner conjugation $\mathrm{Ad}^{\alpha}_u$ is an involution of the group layer exactly when $u^{2} = q(u)$ is central and $\alpha$ acts as required, namely

$$
\mathrm{Ad}^{\alpha}_u \circ \mathrm{Ad}^{\alpha}_u = \mathrm{id} \quad \text{on } V,
$$

while on the whole Clifford algebra it is an involution composed with the grading: $\mathrm{Ad}^{\alpha}_u$ is an algebra automorphism on the even part and a twisted automorphism on the odd part, and its restriction to $V$ is the involution $\rho_u$ with the fixed hyperplane $u^{\perp}$ and the negated line $Fu$.

**Proof.** On $V$ the composition is $\rho_u^2 = \mathrm{id}$ by the previous section; on the whole algebra the multiplicativity of $\mathrm{Ad}^{\alpha}_u$ holds up to the parity sign, which is the parity sign proposition of *The Signed Sandwich on a Symmetry Group*.

### Products of Two Reflections

**Theorem (rotations as even signed sandwiches).** Let $u, w \in V$ have nonzero norm. The product of the two reflections is the signed sandwich by the even element $uw$,

$$
\rho_u \circ \rho_w = \mathrm{Ad}^{\alpha}_{uw} \quad \text{on } V,
$$

and it is a rotation: it lies in $\operatorname{O}^+(V,q)$ and preserves the orientation. Conversely every rotation of $V$ is such a product, by Cartan–Dieudonné with an even number of factors.

**Proof.** The product $\rho_u\rho_w$ acts on a vector $v$ by $u\,\alpha(w\alpha(v)w^{-1})\,u^{-1} = uw\,\alpha(v)\,(uw)^{-1} = \mathrm{Ad}^{\alpha}_{uw}(v)$, using that $\alpha$ is an automorphism and $\alpha(w) = -w$ gives the same element up to the sign that the two reflections absorb; the determinant parity is even, so the rotation group is reached.

**Corollary (the half-turn).** The product of a reflection with itself is the identity, the product of two reflections in perpendicular vectors is the half-turn $\rho_u\rho_w = -\mathrm{id}$ on the plane they span, and the angle of a rotation is twice the angle between the reflecting hyperplanes. In the plane the rotations are exactly the even elements $uw$ with $u, w$ unit vectors, and the parameter is unique up to the sign $uw = (-u)(-w)$.

**Remark (the covering).** The map $x \mapsto \mathrm{Ad}^{\alpha}_x$ from the pin group to the orthogonal group is surjective with kernel the scalars, and on the even part it restricts to the double cover $\mathrm{Spin}(V,q) \to \operatorname{SO}(V,q)$; the reflection is the image of a vector, the rotation the image of a product of two vectors, and the sign ambiguity $x \mapsto -x$ is the kernel. This is *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*, and it is the reason the two-sided operator and not its parameter is the geometric object.

## The Failure in the Degenerate Case

### Isotropic Vectors

**Proposition.** Let $u \in V$ be **isotropic**, $q(u) = 0$ with $u \neq 0$. Then $u$ is not invertible in the Clifford algebra, $\mathrm{Ad}^{\alpha}_u$ is not defined, and $\rho_u$ is not defined, because the reflection formula has $q(u)$ in the denominator and $u^{\perp} = \{v : B(v,u) = 0\}$ contains $u$ itself: the hyperplane is tangent to the isotropic cone and the involution fails to be a reflection in a line transverse to it.

**Proof.** An isotropic vector has $u^{2} = q(u)\cdot 1 = 0$, so it is a zero divisor in $\mathrm{Cl}(V,q)$ and lies in no unit group; the reflection formula requires $q(u) \neq 0$, and $B(u,u) = q(u) = 0$ puts $u$ in its own "hyperplane", so $u^{\perp}$ is not transverse to $Fu$.

**Remark.** The signed inner conjugation therefore defines a reflection exactly for the **anisotropic** vectors, and the reflections available to the form are the anisotropic ones. In the Euclidean case every nonzero vector is anisotropic and the correspondence is complete; in the Lorentzian case the isotropic (null) vectors are exactly the ones outside the correspondence, and this is the geometric origin of the light cone's special role.

### Degenerate Forms

**Proposition.** Let $q$ be **degenerate**, with radical $V^{\perp} = \{u : B(u,v) = 0\ \text{for all } v\}$ of positive dimension. Then the reflection in a vector of the radical is not defined at all — the formula divides by $q(u)$ and the hyperplane is the whole space when $u \in V^{\perp}$ with $q(u) = 0$ — and the orthogonal group is not generated by reflections of $V$ alone; the group $\operatorname{O}(V,q)$ contains the transvections along the radical, which are not reflections.

**Proof.** For $u \in V^{\perp}$ one has $B(v,u) = 0$ for all $v$, so $u^{\perp} = V$ and the formula $\rho_u(v) = v$ gives the identity rather than a reflection whenever $q(u) \neq 0$; when $q(u) = 0$ the map $u$ is not invertible. The transvections $v \mapsto v + \lambda(v)u$ with $u$ in the radical and $\lambda$ a linear form are isometries of $q$ that are unipotent and not reflections, so the generation theorem fails.

**Remark.** The degenerate case is the reason the corpus treats the non-degenerate form as the standing hypothesis of the reflection theory: the correspondence reflection-to-signed-two-sided-operator is a theorem precisely for the anisotropic vectors of a non-degenerate form, and outside that range it degrades in the two ways above.

## Worked Cases

**Example (the Euclidean plane).** Let $V = \mathbb{R}^2$ with $q(x) = x_1^2 + x_2^2$ and $u = (\cos\theta, \sin\theta)$ a unit vector, $q(u) = 1$. The reflection $\rho_u$ has matrix $\begin{pmatrix}\cos 2\theta & \sin 2\theta \\ \sin 2\theta & -\cos 2\theta\end{pmatrix}$, determinant $-1$, and is $\mathrm{Ad}^{\alpha}_u$ restricted to $V$; the unsigned $\mathrm{Ad}_u$ is its negative. The product of the reflections in $u$ and in $w$ with angle $\varphi$ between them is the rotation through $2\varphi$, and the even element $uw$ is the rotor of *The Three Two-Dimensional Algebras and the Three Kinds of Rotation*.

**Example (Minkowski space).** Let $V = \mathbb{R}^{1,1}$ with $q(x) = x_0^2 - x_1^2$ and $u = (1,0)$, $q(u) = 1$. The reflection $\rho_u$ fixes the line $u^{\perp} = \mathbb{R}(0,1)$, which is isotropic, and negates $u$; it is the Lorentz boost of infinite velocity, and it is $\mathrm{Ad}^{\alpha}_u$. The isotropic vectors $(\pm1, 1)$ have $q = 0$, are not units, and index no reflection; they are the light rays, and the correspondence of the previous section excludes exactly them.

**Example (the degenerate form).** Let $V = \mathbb{R}^2$ with $q(x) = x_1^2$, degenerate with radical $\mathbb{R}(0,1)$. The vector $u = (1,0)$ has $q(u) = 1$ and gives the reflection $\rho_u(x) = (x_1, x_2) - 2x_1(1,0) = (-x_1, x_2)$, a genuine reflection; the radical vector $w = (0,1)$ has $q(w) = 0$ and is not a unit, and the transvection $(x_1, x_2) \mapsto (x_1, x_2 + \lambda x_1)$ is an isometry of $q$ that is not a reflection and is not in the group generated by $\rho_u$. The generation theorem fails, and the signed two-sided operator does not reach the whole isometry group.

## Summary

A reflection of a quadratic space is the involutive isometry $\rho_u(v) = v - 2B(v,u)q(u)^{-1}u$ fixing the hyperplane $u^{\perp}$ and negating the line $Fu$; it has determinant $-1$ and the eigenvalues $+1$ and $-1$, and by the theorem of Cartan–Dieudonné the reflections generate the orthogonal group and the even products generate the rotations. In the pin group the reflection is the signed inner conjugation by the vector $u$, $\rho_u(v) = u\alpha(v)u^{-1} = \mathrm{Ad}^{\alpha}_u(v)$, while the unsigned inner conjugation gives $-\rho_u(v)$; the correspondence is two-sided in an essential way, the one-sided signed operators not preserving $V$. The product of two reflections is the even signed sandwich $\mathrm{Ad}^{\alpha}_{uw} = \rho_u\rho_w$, a rotation, and the map $x \mapsto \mathrm{Ad}^{\alpha}_x$ is the double cover of the orthogonal group by the pin group with kernel the scalars. The correspondence holds exactly for the anisotropic vectors of a non-degenerate form: an isotropic vector is not a unit and indexes no reflection, and for a degenerate form the radical carries transvections that are isometries but not reflections, so the generation by reflections fails.

No adjoint is taken here; the adjoint of the reflection as a signed operator is the article *The Signed Adjoint of the Reflection on a Symmetry Group* of the group `- * Operator Theory`.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $u$, $q(u) \neq 0$ | a vector of nonzero norm in the quadratic space $V$ |
| $\rho_u$ | the reflection in $u^{\perp}$, $\rho_u(v) = v - 2B(v,u)q(u)^{-1}u$ |
| $u^{\perp}$ | the fixed hyperplane of $\rho_u$ |
| $\mathrm{Ad}^{\alpha}_u$ | the signed inner conjugation by $u$; restricts to $\rho_u$ on $V$ |
| $\mathrm{Ad}_u$ | the unsigned inner conjugation; restricts to $-\rho_u$ on $V$ |
| $S^{\alpha}_{a,b}$ | the signed sandwich; the reflection is the diagonal with a vector |
| $\operatorname{O}(V,q)$, $\operatorname{O}^+(V,q)$ | orthogonal and rotation groups |
| $\operatorname{Pin}(V,q)$, $\operatorname{Spin}(V,q)$ | pin and spin groups; the double covers of the orthogonal and rotation groups |
| $V^{\perp}$ | the radical of a degenerate form |

## Further Reading

- Jean Dieudonné, *La géométrie des groupes classiques* (Springer, 1971), for the reflections, the generation theorems and the degenerate case.
- Claude Chevalley, *The Algebraic Theory of Spinors and Clifford Algebras* (Springer, 1997), for the Clifford group, the reflections and the pin group.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, second edition, 2001), for the reflection formula and the isotropic and degenerate cases.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the orthogonal group inside the Clifford group and the reflection principle.
- Larry C. Grove, *Classical Groups and Geometric Algebra* (American Mathematical Society, 2002), for the generation of the classical groups by reflections and transvections.
