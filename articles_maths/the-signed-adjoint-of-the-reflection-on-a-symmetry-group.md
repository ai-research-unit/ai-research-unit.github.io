
# __The Signed Adjoint of the Reflection on a Symmetry Group__

## Introduction

A reflection is an involutive isometry, and an operator that is both an isometry and an involution is its own adjoint: $\rho_u^{*} = \rho_u^{-1} = \rho_u$. The adjoint of the reflection is therefore the reflection itself, and the reflections are exactly the elements of the orthogonal group that the adjoint does not move — the self-adjoint unitaries of the group, among the involutions it contains. The property is what distinguishes a reflection from a rotation: a rotation is unitary but not self-adjoint, its adjoint being its inverse, and the two together generate the adjoint action on the whole orthogonal group. The property **fails** in the degenerate case: for an isotropic vector $u$, with $q(u) = 0$, the reflection formula has no meaning, the signed inner conjugation that realises it is not defined, and the substitute operator — the transvection — is not self-adjoint.

The article treats the reflection as an operator, its adjoint and self-adjointness, the failure of the property in the degenerate case, and the generation of the orthogonal group with its adjoint. The reflection and the Cartan–Dieudonné generation theorem are *Isometries and Orthogonal Transformations*, *The Rotation Group and Orientation* and *Reflections as Signed Two-Sided Operators on a Symmetry Group*; the adjoint of a symmetry operator, the unitarity theorem and the operator involution are *The Adjoint of a Symmetry Operator*, the first article of this group; the adjoint of the general signed sandwich is *The Signed Adjoint Sandwich on a Symmetry Group*, the previous article, of which this is the single-reflection case; the Clifford realisation of the reflection is *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*. The two-structures question, whether an involution of the elements agrees with the adjoint of the operators, is *The Adjoint of a Symmetry Operator* and is not reopened.

The article has four sections: the reflection as an operator; its adjoint and self-adjointness; the degenerate case and the failure; and the worked cases. Throughout, $V$ is a finite-dimensional space over a field $F$ of characteristic not $2$ with a non-degenerate quadratic form $q$ and polar form $B$, $G = \operatorname{O}(V,q)$ the orthogonal group, $u \in V$ a vector with $q(u) \neq 0$ except in the degenerate section, and $\rho_u$ the reflection in $u^{\perp}$; the adjoint is taken with respect to $q$ as in *The Adjoint of a Symmetry Operator*.

## The Reflection as an Operator

### The Formula

**Definition.** For $q(u) \neq 0$ the **reflection** in the hyperplane $u^{\perp}$ is the linear operator

$$
\rho_u : V \longrightarrow V, \qquad \rho_u(v) = v - 2\,\frac{B(v,u)}{q(u)}\,u .
$$

**Proposition.** The reflection is linear, fixes $u^{\perp}$ pointwise, sends $u$ to $-u$, is an involution $\rho_u^2 = \mathrm{id}$, is an isometry $q(\rho_u v) = q(v)$, is an element of $G$ of determinant $-1$, and is the negative of the **transvection** $v \mapsto v - \frac{B(v,u)}{q(u)}u$ composed appropriately; it is the operator whose signed two-sided form is the signed inner conjugation $\mathrm{Ad}^{\alpha}_u = \rho_u$ of *Reflections as Signed Two-Sided Operators on a Symmetry Group*.

**Proof.** These are the elementary properties of the reflection, *Reflections as Signed Two-Sided Operators on a Symmetry Group*, quoted.

### The Reflection in the Clifford Algebra

**Proposition.** In the Clifford algebra $\mathrm{Cl}(V,q)$ the reflection is the restriction to the vectors of the signed inner conjugation by $u$,

$$
\rho_u(v) = u\,\alpha(v)\,u^{-1}, \qquad v \in V,
$$

while the unsigned inner conjugation is its negative, $uvu^{-1} = -\rho_u(v)$; the vector $u$ satisfies $u^2 = q(u)$ and $u^{-1} = q(u)^{-1}u$, and the conjugation by $u$ is the reflection up to the sign of the grade involution.

**Proof.** The identity is the Clifford reflection formula, *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*; it is quoted, not re-derived.

**Remark.** The reflection is at once an operator of the geometry, an element of the orthogonal group, and an inner conjugation of the Clifford algebra; the three descriptions coincide and the adjoint is the same in each.

## The Adjoint of the Reflection

### Self-Adjointness

**Theorem (the reflection is self-adjoint).** The adjoint of the reflection with respect to the form is the reflection itself,

$$
\rho_u^{*} = \rho_u^{-1} = \rho_u, \qquad \langle \rho_u v, w\rangle = \langle v, \rho_u w\rangle \ \text{for all } v, w,
$$

so the reflection is both unitary and **Hermitian** (self-adjoint); in the notation of the operator involution it is a unitary element fixed by the adjoint.

**Proof.** An isometry of the form has adjoint its inverse, $g^{*} = g^{-1}$, by the unitarity theorem of *The Adjoint of a Symmetry Operator*; an involution has $g^{-1} = g$; combining, $\rho_u^{*} = \rho_u^{-1} = \rho_u$. Directly, $B(\rho_u v, w) = B(v,w) - 2q(u)^{-1}B(v,u)B(u,w)$ and $B(v, \rho_u w) = B(v,w) - 2q(u)^{-1}B(v,u)B(u,w)$ are equal by the symmetry of $B$.

### The Involutions and the Reflections

**Proposition.** The self-adjoint unitary elements of $G$ are exactly the **involutions** of $G$,

$$
\{g \in G : g^{*} = g^{-1} = g\} = \{g \in G : g^2 = \mathrm{id}\},
$$

and a reflection is the involutive isometry whose fixed space is a hyperplane; an involution that fixes a subspace of codimension greater than one is a product of commuting reflections and is self-adjoint without being a single reflection.

**Proof.** $g^{*} = g$ and $g^{*} = g^{-1}$ together give $g^{-1} = g$, i.e., $g^2 = \mathrm{id}$; conversely an involutive isometry satisfies $g^{*} = g^{-1} = g$. The fixed-space statement is the classification of the involutions of an orthogonal group, *Isometries and Orthogonal Transformations*: a self-adjoint involution is orthogonally diagonalisable with eigenvalues $\pm1$, hence a product of reflections in the $(-1)$-eigenspaces.

### The Rotations

**Proposition.** A rotation, an element of $\operatorname{O}^{+}(V,q)$ that is not an involution, is unitary but not self-adjoint: its adjoint is its inverse, $g^{*} = g^{-1} \neq g$. The adjoint therefore separates the reflections from the rotations inside the orthogonal group, and the Cartan–Dieudonné theorem reads $\rho_{u_1}\cdots\rho_{u_{2k}}$ for a rotation, whose adjoint is $\rho_{u_{2k}}\cdots\rho_{u_1} = g^{-1}$.

**Proof.** The adjoint of an isometry is its inverse; a rotation is not an involution, so it is not self-adjoint. The adjoint of a product reverses the order, $(g_1g_2)^{*} = g_2^{*}g_1^{*}$, and the reflections are self-adjoint, so the adjoint of a product of reflections is the product in reverse order, which for a rotation is its inverse. The generation theorem is *Isometries and Orthogonal Transformations*.

## The Degenerate Case and the Failure

### The Isotropic Vector

**Proposition (the isotropic case).** For $u$ with $q(u) = 0$ the reflection formula is undefined — the normalisation by $q(u)$ is lost — no operator of the reflection's shape exists in the orthogonal group, and the signed inner conjugation $\mathrm{Ad}^{\alpha}_u(x) = u\alpha(x)u^{-1}$ is likewise undefined, because an isotropic vector is a zero divisor in $\mathrm{Cl}(V,q)$ and does not lie in the Clifford group.

**Proof.** The reflection sends $u$ to $-u$ and fixes $u^{\perp}$; an isotropic $u$ lies in $u^{\perp}$, so the two requirements are contradictory and no such involution exists. For the Clifford statement, $u^2 = q(u) = 0$ makes $u$ a zero divisor with no inverse, *The Clifford, Pin and Spin Groups with Signed Inner Conjugation*.

### The Failure of Self-Adjointness

**Proposition.** The operator that generalises the reflection to an isotropic vector is a **transvection**, a unipotent operator of the shape $\tau(v) = v + B(v,u)w$ with $w$ chosen so that $B(u,w) = 1$, or more generally $\mathrm{id} + N$ with $N$ of square zero; it fixes the isotropic line $Fu$, it is not an involution, $\tau^2 \neq \mathrm{id}$, and it is not self-adjoint, a unitary self-adjoint operator being an involution.

**Proof.** $\tau^2(v) = v + 2B(v,u)w \neq v$ for any $v$ with $B(v,u) \neq 0$, so $\tau$ is not an involution; a unitary self-adjoint operator satisfies $g^2 = \mathrm{id}$, so a non-involutive operator is not self-adjoint. In the degenerate case $\tau$ is not even an isometry, $q(\tau v) = q(v) + 2B(v,u)B(v,w) + B(v,u)^2q(w) \neq q(v)$ in general, so the self-adjointness fails on both counts. The degenerate-form theory is *Quadratic Forms and Polarisation* and *Bilinear Forms*.

**Remark.** The failure is the boundary of the theorem: the self-adjointness of the reflection is proved from two properties — isometry and involution — and the degenerate substitute has neither. The **signed** reflection $\mathrm{Ad}^{\alpha}_u$ is self-adjoint in the Clifford setting exactly when the vector satisfies $u^{*} = u$, by *The Signed Adjoint Sandwich on a Symmetry Group*; the two conditions, the non-degeneracy of the form and the reality of the vector, are the standing hypotheses of the self-adjointness.

## Worked Cases

**Example (the Euclidean reflection).** Let $q$ be positive definite and $u \neq 0$; the reflection $\rho_u$ is an involution and an isometry, hence self-adjoint, $\rho_u^{*} = \rho_u$. In an orthonormal basis $\rho_u$ is a symmetric orthogonal matrix, and self-adjointness is the symmetry of the matrix; the example is the original case.

**Example (the hyperbolic reflection).** Let $q$ be of signature $(p,q)$ and $u$ a vector with $q(u) \neq 0$; the reflection is again self-adjoint, and it is an element of $O(p,q)$ with determinant $-1$. In the rank-one case $O(p,1)$ the reflection in $u^{\perp}$ is the geodesic symmetry of hyperbolic space when $u$ is the base vector, *The Orthogonal Group and the Involutive Automorphism*.

**Example (the rotations are not self-adjoint).** On the Euclidean plane with the rotation $r_{\theta}$ through an angle $\theta$ not $0$ or $\pi$, the adjoint is $r_{\theta}^{*} = r_{-\theta} \neq r_{\theta}$, so the rotation is unitary and not self-adjoint; on $\theta = \pi$ the rotation is an involution and is self-adjoint, which is the case where it is a product of two reflections in perpendicular lines. The example shows the separation of the reflections from the rotations by the adjoint.

**Example (the transvection).** Let $q$ be of signature $(1,1)$ with isotropic vectors $u = e_1+e_2$ in a basis with $q(e_1) = 1$, $q(e_2) = -1$; the transvection $\tau(v) = v + B(v,u)w$ with $B(u,w) = 1$ is unipotent, it fixes the isotropic line $Fu$, it is not an involution and it is not self-adjoint, and it generates the parabolic one-parameter subgroup of $O(1,1)$. The example is the degenerate substitute in the smallest indefinite case, and it is the boundary the self-adjointness theorem does not reach.

## Summary

A reflection $\rho_u$ with $q(u) \neq 0$ is an involutive isometry, and its adjoint with respect to the form is itself: $\rho_u^{*} = \rho_u^{-1} = \rho_u$, so the reflection is both unitary and self-adjoint; the self-adjoint unitary elements of the orthogonal group are exactly its involutions, and a reflection is the involutive isometry with a hyperplane of fixed vectors, while a general involution is a product of commuting reflections. A rotation is unitary and not self-adjoint, its adjoint being its inverse, so the adjoint separates the reflections from the rotations and the Cartan–Dieudonné theorem gives the adjoint of a product of reflections as the reverse product. The property fails in the degenerate case: for an isotropic vector the reflection is undefined, the signed inner conjugation does not exist, and the substitute transvection is neither an isometry nor self-adjoint, so the self-adjointness is a theorem about the non-degenerate reflection alone. In the Clifford setting the signed reflection $\mathrm{Ad}^{\alpha}_u$ is self-adjoint exactly when $u^{*} = u$, by *The Signed Adjoint Sandwich on a Symmetry Group*. The adjoint of the one-sided signed operator is the subject of the next article.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\rho_u$ | the reflection in $u^{\perp}$, $q(u) \neq 0$ |
| $\rho_u(v) = v - 2q(u)^{-1}B(v,u)u$ | the reflection formula |
| $\rho_u^{*} = \rho_u^{-1} = \rho_u$ | the reflection is self-adjoint |
| $\{g : g^{*} = g^{-1} = g\}$ | the self-adjoint unitaries; the involutions |
| $g^{*} = g^{-1}$ | a rotation is unitary, not self-adjoint |
| $\rho_{u_1}\cdots\rho_{u_{2k}}$ | a rotation as a product of reflections (Cartan–Dieudonné) |
| $\mathrm{Ad}^{\alpha}_u(v) = \rho_u(v)$ | the reflection as a signed inner conjugation |
| $\tau_u = \mathrm{id} - B(\cdot,u)w$ | the transvection; the degenerate substitute |
| $u^{*} = u$ | the reality condition for the signed self-adjointness |

## Further Reading

- Jean Dieudonné, *La géométrie des groupes classiques* (Springer, 1971), for the reflections, the transvections and the generation of the orthogonal group.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the reflection as a signed inner conjugation and its self-adjointness.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, second edition, 2001), for the reflection, the isotropic case and the failure of the conjugation.
- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (Academic Press, 1978), for the reflection as the geodesic symmetry in the rank-one symmetric spaces.
- O. Timothy O'Meara, *Introduction to Quadratic Forms* (Springer, 1973), for the degenerate case, the transvections and the isotropic vectors.
