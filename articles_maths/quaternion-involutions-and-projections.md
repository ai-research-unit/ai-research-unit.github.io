# __Quaternion Involutions and Projections__

## Introduction

The quaternion algebra carries a family of order-two maps that the corpus has met in several places and never collected: the three coordinate maps of *Quaternion Augmented Statistics*, the half-turn example of *Quaternion Automorphisms and Derivations*, and the three conjugations that *Worked Examples in the Quaternion Algebra* and *The Scalar and Vector Subspaces of $\mathbb{H}$* call the involutions of the algebra. This article collects them. A real-linear map of $\mathbb{H}$ that is its own inverse and is multiplicative is an **involution**, and it is shown below that the involutions are the identity and the maps $\tilde q\mapsto-\nu\tilde q\nu$, one for each axis line $\mathbb{R}\nu$. The family is therefore infinite, parametrised by the axis lines, that is by the projective plane. The conjugations, which reverse the order of a product, are **anti-involutions** and form a separate family of the same size, glued to the involutions by the conjugate.

The article turns on one computation, the multiplicativity of $-\nu\tilde q\nu$, which uses $\nu^2=-1$. From it follow the geometry of an involution — it fixes the scalar part and the axis line and reflects the vector part in the axis, so that it is the reflection in the line and not in the plane — the composition rules of a mutually perpendicular triple, and the two formulas that name the article: the component of a vector parallel to an axis is half the vector plus its involution, and the perpendicular component is half the difference. The article closes with the resolution of a quaternion in an orthonormal frame, where the involutions supply the coefficients and no coordinate system need be chosen.

The treatment is mathematical throughout. No physical object is introduced, no state of a physical system is named, and no physical interpretation is invoked. A unit vector is an element of the imaginary subspace with unit quaternion norm; it is a direction in $\mathbb{R}^3$ and nothing else.

The quaternion algebra and its basis $e_0 = 1, e_1, e_2, e_3$ with $e_k^2 = -e_0$, the conjugate, the quaternion norm and the absence of zero divisors are from *Quaternion Algebra* and *Quaternion Norm and Invertibility*; the inner automorphism $\iota_u(\tilde x) = u\tilde xu^{-1}$ and the theorem that every automorphism of $\mathbb{H}$ is inner are from *Quaternion Automorphisms and Derivations*; the adjoint action, the plane reflection $\rho_v$, the half-angle formula and the composition $\rho_{v_1}\rho_{v_2} = \operatorname{Ad}_{v_1v_2}$ are from *Quaternion Rotations and Reflections*; the three coordinate involutions, the sign matrix, the Klein group and the recovery of the conjugate from the three coordinate involutions are from *Quaternion Augmented Statistics*; the sphere of unit vectors, identified with $Sp(1)/U(1)$, is from *Quaternion Roots of Minus One*.

Throughout, a quaternion is $\tilde q = q_0e_0+q_1e_1+q_2e_2+q_3e_3$ with scalar part $q_0 = \mathrm{Sc}\,\tilde q$ and vector part $\mathbf q = \mathrm{Vect}\,\tilde q = q_1e_1+q_2e_2+q_3e_3\in\operatorname{Im}\mathbb{H}$, the conjugate is $\bar{\tilde q} = q_0e_0-q_1e_1-q_2e_2-q_3e_3$, the quaternion norm is $N(\tilde q) = \tilde q\bar{\tilde q} = |\tilde q|^2$, the real inner product on $\operatorname{Im}\mathbb{H}$ is $\langle x,y\rangle = \mathrm{Sc}(x\bar y) = \sum_{k=1}^{3}x_ky_k$ with $|x|^2 = \langle x,x\rangle$, and a **unit vector** is an element $\nu\in\operatorname{Im}\mathbb{H}$ with $N(\nu) = 1$. For a unit vector $\nu$ one has $\nu^2 = -e_0$ and $\nu^{-1} = \bar\nu = -\nu$. The units of $\mathbb{H}$ are the non-zero elements, and $Sp(1)$ is the unit sphere.

The source of the arrangement is the paper of Ell and Sangwine, *Quaternion Involutions* (arXiv:math/0506034): the axioms, the infinitude of the family, the reflection reading, the composition theorems, the recovery of the conjugate and the projection formulas are theirs. The notation is the corpus's. Where the source writes $\tilde q^{\nu}$ for the value $-\nu\tilde q\nu$, this article writes $\iota_\nu(\tilde q)$, the inner-automorphism notation of *Quaternion Automorphisms and Derivations*, to which the involution is a specialisation.

## Involutions and Anti-Involutions

### The Axioms

**Definition.** An **involution** of $\mathbb{H}$ is a map $f : \mathbb{H}\to\mathbb{H}$ with

1. $f(f(\tilde q)) = \tilde q$ for every $\tilde q$;
2. $f$ is $\mathbb{R}$-linear, $f(\tilde p+\tilde q) = f(\tilde p)+f(\tilde q)$ and $f(\lambda\tilde q) = \lambda f(\tilde q)$ for real $\lambda$;
3. $f$ is multiplicative, $f(\tilde p\tilde q) = f(\tilde p)f(\tilde q)$.

A map satisfying 1 and 2 together with the reversed product rule $f(\tilde p\tilde q) = f(\tilde q)f(\tilde p)$ is an **anti-involution**.

**Remark (why all three axioms).** Axiom 1 alone admits too much. The real-linear map that fixes $e_0$ and $e_1$ and exchanges $e_2$ and $e_3$ is its own inverse, so it satisfies Axioms 1 and 2, and it fails Axiom 3: it sends the product $e_2e_3 = e_1$, which it fixes, to $e_3e_2 = -e_1$. It is Axiom 3 that forces the shape found in the next section, and the failure is not removable by a change of sign.

**Proposition.** An involution fixes $e_0$, and is a unital algebra automorphism of order dividing two; conversely every unital algebra automorphism $\sigma$ with $\sigma^2 = \mathrm{id}$ is an involution.

*Proof.* For an involution $f$, put $\tilde e = f(e_0)$. Then $\tilde e = f(e_0) = f(e_0e_0) = f(e_0)f(e_0) = \tilde e^2$, so $\tilde e$ is idempotent. It is not zero: were $\tilde e = 0$, then $e_0 = f(f(e_0)) = f(\tilde e) = f(0) = 0$, which is false. An idempotent $\tilde e$ in $\mathbb{H}$ satisfies $\tilde e(\tilde e-e_0) = 0$, and $\mathbb{H}$ has no zero divisors, so $\tilde e = 0$ or $\tilde e = e_0$; hence $f(e_0) = e_0$. Axioms 2 and 3 then say exactly that $f$ is a unital $\mathbb{R}$-algebra endomorphism, and Axiom 1 makes it bijective with inverse $f$. The converse is immediate from the definition of a unital automorphism.

### The Conjugate Is an Anti-Involution

**Theorem.** Quaternion conjugation is an anti-involution, and is not an involution.

*Proof.* Conjugation is $\mathbb{R}$-linear and satisfies $\overline{\tilde p\tilde q} = \bar{\tilde q}\bar{\tilde p}$, the reversed product rule, and it is its own inverse; so it satisfies Axioms 1 and 2 and the reversed form of Axiom 3. It fails Axiom 3: $\overline{e_1e_2} = \overline{e_3} = -e_3$, while $\bar e_1\bar e_2 = (-e_1)(-e_2) = e_1e_2 = e_3$.

**Corollary.** The anti-involutions of $\mathbb{H}$ are the conjugate $\tilde q\mapsto\bar{\tilde q}$ and the maps $\tilde q\mapsto-\nu\bar{\tilde q}\nu$ for unit vectors $\nu$, that is the composite $\iota_\nu\circ\bar{\cdot}$ of an involution with the conjugate.

*Proof.* Let $f$ be an anti-involution. From the reversed product rule at $\tilde p = \tilde q = e_0$ one gets $f(e_0) = f(e_0)^2$, and $f(e_0)\neq0$ because $f$ is its own inverse; as above $f(e_0) = e_0$, so $f$ fixes $e_0$. Then $g = f\circ\bar{\cdot}$ is multiplicative, since both $f$ and conjugation reverse products, and it fixes $e_0$ and is bijective, so it is a unital automorphism; by *Quaternion Automorphisms and Derivations* it is $\iota_u$ for a unit $u$, and $f = \iota_u\circ\bar{\cdot}$. Computing, $f(f(\tilde q)) = u^2\tilde q u^{-2} = \iota_{u^2}(\tilde q)$, so $f$ is an anti-involution exactly when $u^2$ is real, that is when $u$ is real or pure imaginary; a real $u$ gives the conjugate, and a pure $u$ is $u = t\nu$ with $t\neq0$ real and $\nu$ a unit vector, giving $f(\tilde q) = t\nu\bar{\tilde q}(t\nu)^{-1} = \nu\bar{\tilde q}\nu^{-1} = -\nu\bar{\tilde q}\nu$.

**Remark (the terminology of the corpus).** The corpus calls $\bar{\cdot}$, $-\bar{\cdot}$ and $-\mathrm{id}$ *the three involutions* of the algebra in *Worked Examples in the Quaternion Algebra* and in *The Scalar and Vector Subspaces of $\mathbb{H}$*, and *Quaternion Augmented Statistics* defines an involution by $\iota^2 = \mathrm{id}$ alone. In the sense of this article only the conjugate is an anti-involution, and the maps $-\bar{\cdot}$ and $-\mathrm{id}$ are neither involutions nor anti-involutions. For $-\mathrm{id}$ the product $(-\tilde p)(-\tilde q)$ equals $\tilde p\tilde q$, while multiplicativity would need it to equal $-\tilde p\tilde q$ and the reversed rule would need it to equal $-\tilde q\tilde p$; for $-\bar{\cdot}$ the product $(-\bar{\tilde p})(-\bar{\tilde q})$ equals $\bar{\tilde p}\bar{\tilde q}$, which is neither $-\overline{\tilde p\tilde q} = -\bar{\tilde q}\bar{\tilde p}$ nor its reverse $-\bar{\tilde p}\bar{\tilde q}$. The maps $\iota_k$ of *Quaternion Augmented Statistics* are involutions in the sense of this article as well, and are the coordinate instances of the family classified next; it is the multiplicative sense that carries the classification.

## The Involutions of the Algebra

### The Family Defined by a Unit Vector

**Theorem (the involutions).** For every unit vector $\nu$ the map

$$
\iota_\nu(\tilde q) = \nu\tilde q\nu^{-1} = -\nu\tilde q\nu
$$

is an involution of $\mathbb{H}$, and conversely the involutions of $\mathbb{H}$ are $\mathrm{id}$ and the maps $\iota_\nu$ with $\nu$ a unit vector. Hence $\mathbb{H}$ has infinitely many involutions. Moreover $\iota_\nu = \iota_\omega$ exactly when $\omega = \pm\nu$, so the non-trivial involutions are parametrised by the axis lines $\mathbb{R}\nu$, that is by the projective plane of directions of $\mathbb{R}^3$.

*Proof.* (a) The map is the inner automorphism of *Quaternion Automorphisms and Derivations*, hence multiplicative, and it is $\mathbb{R}$-linear; it is its own inverse because $\iota_\nu(\iota_\nu(\tilde q)) = \nu^2\tilde q\nu^{-2} = (-e_0)\tilde q(-e_0) = \tilde q$. The second form follows from $\nu^{-1} = -\nu$. (b) Conversely, let $f$ be an involution; by the proposition of the previous section it is a unital automorphism of order dividing two; by Skolem–Noether it is inner, $f = \iota_u$ for a unit $u$; and $\iota_u^2 = \iota_{u^2} = \mathrm{id}$ exactly when $u^2$ is central, that is real. Writing $u = u_0+\mathbf u$ with vector part $\mathbf u$, one has $u^2 = u_0^2-N(\mathbf u)+2u_0\mathbf u$, real precisely when $u_0 = 0$ or $\mathbf u = 0$. The second case is $u$ real, giving the identity; the first is $u$ pure imaginary, $u = t\nu$ with $t$ real and $\nu$ a unit vector, and $\iota_u = \iota_\nu$. (c) For the parametrisation, $\iota_\nu$ fixes the plane $\operatorname{span}(e_0,\nu)$ pointwise and no more, so $\iota_\nu = \iota_\omega$ forces $\operatorname{span}(e_0,\nu) = \operatorname{span}(e_0,\omega)$, hence $\omega = \pm\nu$; the converse is the identity $\nu\tilde q\nu^{-1} = (-\nu)\tilde q(-\nu)^{-1}$.

**Corollary.** The involutions $\iota_\nu$ of the coordinate axes are the three maps $\iota_k$ of *Quaternion Augmented Statistics*, and the involution about the axis $e_1$ is the half-turn of the example of *Quaternion Automorphisms and Derivations*.

### Not Every Self-Inverse Sandwich Is an Involution

**Proposition.** For unit vectors $\nu_1,\nu_2$ the map $g(\tilde q) = \nu_1\tilde q\nu_2$ is its own inverse, $g^2 = \mathrm{id}$. It is multiplicative, hence an involution, exactly when $\nu_2 = -\nu_1$, and then it is $\iota_{\nu_1}$. In particular a map $\nu_1\tilde q\nu_2$ with $\nu_2\neq-\nu_1$ is self-inverse and is not an involution.

*Proof.* The square is $g(g(\tilde q)) = \nu_1^2\tilde q\nu_2^2 = \tilde q$, since $\nu_1^2 = \nu_2^2 = -e_0$. For multiplicativity, $g(\tilde p)g(\tilde q) = \nu_1\tilde p\nu_2\nu_1\tilde q\nu_2$ and $g(\tilde p\tilde q) = \nu_1\tilde p\tilde q\nu_2$; the two agree for all $\tilde p,\tilde q$ exactly when $\nu_2\nu_1 = e_0$ — set $\tilde p = \tilde q = e_0$ and cancel — that is exactly when $\nu_2 = \nu_1^{-1} = -\nu_1$, and then $g(\tilde q) = -\nu_1\tilde q\nu_1 = \iota_{\nu_1}(\tilde q)$.

The proposition is the reason Axiom 3 is not redundant: the self-inverse sandwiches of that shape form a four-dimensional family, the involutions a two-dimensional one, the projective plane.

## The Geometry of an Involution

### The Line Reflection

**Theorem.** Let $\nu$ be a unit vector and $\tilde q = q_0+\mathbf q$ its scalar and vector decomposition. Then

$$
\iota_\nu(\tilde q) = q_0-\nu\mathbf q\nu = q_0+2\langle\mathbf q,\nu\rangle\nu-\mathbf q .
$$

Consequently $\iota_\nu$ fixes the scalar part, fixes the vector part parallel to $\nu$ and negates the vector part perpendicular to $\nu$: on the vector subspace $\operatorname{Im}\mathbb{H}$ it is the reflection in the line $\mathbb{R}\nu$, equivalently the rotation by $\pi$ about $\nu$. On $\mathbb{H}$ it fixes the plane $\operatorname{span}(e_0,\nu)$ pointwise and negates its orthogonal complement $\nu^{\perp}$ pointwise.

*Proof.* Since $\nu e_0\nu^{-1} = e_0$, the map fixes the scalar part. For pure $\mathbf q$ one has $\nu\mathbf q = \nu\times\mathbf q-\langle\nu,\mathbf q\rangle$ and $\mathbf q\nu = -\nu\times\mathbf q-\langle\nu,\mathbf q\rangle$ from the product formula of *Quaternion Algebra*, so $\nu\mathbf q\nu = (\nu\times\mathbf q)\nu-\langle\nu,\mathbf q\rangle\nu = \mathbf q-2\langle\nu,\mathbf q\rangle\nu$, using $(\nu\times\mathbf q)\nu = (\nu\times\mathbf q)\times\nu = \mathbf q-\langle\nu,\mathbf q\rangle\nu$; hence $-\nu\mathbf q\nu = 2\langle\mathbf q,\nu\rangle\nu-\mathbf q$. The right-hand side fixes $\mathbf q$ when $\mathbf q$ is parallel to $\nu$ and negates it when $\langle\mathbf q,\nu\rangle = 0$, so on $\operatorname{Im}\mathbb{H}$ the map is the reflection in the line $\mathbb{R}\nu$, equivalently the rotation by $\pi$ about $\nu$. Adding the fixed scalar line gives the fixed plane $\operatorname{span}(e_0,\nu)$ and the anti-fixed plane $\nu^{\perp}$.

**Corollary (parallel and perpendicular elements).** For a unit vector $\nu$, $\iota_\nu(\tilde q) = \tilde q$ when $\mathbf q$ is parallel to $\nu$, and $\iota_\nu(\tilde q) = \bar{\tilde q}$ when $\mathbf q$ is perpendicular to $\nu$.

*Proof.* The involution fixes the scalar part and replaces $\mathbf q$ by its reflection in the line $\mathbb{R}\nu$, which is $\mathbf q$ in the parallel case and $-\mathbf q$ in the perpendicular case.

### The Line Reflection and the Plane Reflection

**Remark.** The reflection of *Quaternion Rotations and Reflections* is the plane reflection

$$
\rho_\nu(\tilde x) = -\nu\tilde x\nu^{-1},
$$

which on $\operatorname{Im}\mathbb{H}$ equals $\tilde x-2\langle\tilde x,\nu\rangle\nu$ and is the reflection in the **plane** $\nu^{\perp}$; on $\mathbb{H}$ it also negates the scalar line, $\rho_\nu(e_0) = -e_0$. Since $\nu^{-1} = -\nu$, one has $\rho_\nu = -\iota_\nu$: the involution and the plane reflection are the two reflections attached to the axis $\nu$, and the sign between them is exactly the difference between reflecting in the line and reflecting in the plane. The plane reflection is orientation-reversing on $\operatorname{Im}\mathbb{H}$ and the involution is orientation-preserving there, the determinants being $-1$ and $+1$.

## Composition of Involutions

### The Composite Is an Inner Automorphism

**Theorem.** For unit vectors $\nu_1,\nu_2$,

$$
\iota_{\nu_1}\circ\iota_{\nu_2} = \operatorname{Ad}_{\nu_1\nu_2} ,
$$

the inner automorphism determined by the product $\nu_1\nu_2$.

*Proof.* $\iota_{\nu_1}(\iota_{\nu_2}(\tilde q)) = \nu_1(\nu_2\tilde q\nu_2^{-1})\nu_1^{-1} = (\nu_1\nu_2)\tilde q(\nu_2^{-1}\nu_1^{-1}) = (\nu_1\nu_2)\tilde q(\nu_1\nu_2)^{-1}$, since $(\nu_1\nu_2)^{-1} = \nu_2^{-1}\nu_1^{-1}$.

The composite is therefore the same map as the product $\rho_{\nu_1}\rho_{\nu_2}$ of two plane reflections of *Quaternion Rotations and Reflections*. It is the identity exactly when $\nu_1$ and $\nu_2$ are parallel; it is the involution $\iota_{\nu_1\times\nu_2}$ when they are perpendicular; and for a general pair of axes it is a rotation through an angle that is neither $0$ nor $\pi$.

### Mutually Perpendicular Involutions

**Theorem.** Let $\nu_1,\nu_2$ be perpendicular unit vectors. Then $\nu_1\nu_2 = \nu_1\times\nu_2$ is a unit vector, the two involutions commute, and their composite is the involution about the common perpendicular:

$$
\iota_{\nu_1}\circ\iota_{\nu_2} = \iota_{\nu_2}\circ\iota_{\nu_1} = \iota_{\nu_1\times\nu_2} .
$$

*Proof.* For perpendicular pure quaternions $\nu_1\nu_2 = -\langle\nu_1,\nu_2\rangle+\nu_1\times\nu_2 = \nu_1\times\nu_2$, of norm one because the two are unit and perpendicular; so the composite is $\operatorname{Ad}_{\nu_1\times\nu_2}$, the inner automorphism of the unit vector $\nu_1\times\nu_2$, which is $\iota_{\nu_1\times\nu_2}$. For the commutation, $\nu_2\nu_1 = -\nu_1\nu_2$ and $\operatorname{Ad}$ is unchanged by the sign of its argument, so $\operatorname{Ad}_{\nu_2\nu_1} = \operatorname{Ad}_{\nu_1\nu_2}$, and by the previous theorem the two composites agree.

**Theorem (the Klein group of a perpendicular triple).** Let $\nu_1,\nu_2,\nu_3$ be mutually perpendicular unit vectors. Then

$$
\{\mathrm{id},\iota_{\nu_1},\iota_{\nu_2},\iota_{\nu_3}\}
$$

is a group under composition, isomorphic to $\mathbb{Z}/2\times\mathbb{Z}/2$. The product of two distinct members is the third — up to the sign of the axis, which the involution does not see — and the composition of all three is the identity.

*Proof.* Each member is its own inverse by the first theorem of the section. For the products, $\iota_{\nu_1}\iota_{\nu_2} = \iota_{\nu_1\times\nu_2}$ and $\nu_1\times\nu_2$ is one of $\pm\nu_3$, so the product is $\iota_{\nu_3}$; the other pairs are the same up to the order of the factors, which the commutation makes immaterial, and the sign of the axis is immaterial by the parametrisation theorem. For the triple, $(\iota_{\nu_1}\iota_{\nu_2})\iota_{\nu_3} = \iota_{\nu_3}\iota_{\nu_3} = \mathrm{id}$.

**Remark.** This is the general form of the sign matrix and of the Klein group of *Quaternion Augmented Statistics*, where the perpendicular triple is the coordinate one $e_1,e_2,e_3$ and the four maps are $\mathrm{id},\iota_1,\iota_2,\iota_3$; the four maps there are the four characters of the group, and the group is the same group.

### The Composite Is a Rotation

**Theorem.** For unit vectors $\nu_1,\nu_2$ the composite $\iota_{\nu_1}\iota_{\nu_2} = \operatorname{Ad}_{\nu_1\nu_2}$ fixes the scalar part, preserves the quaternion norm, and rotates the vector part about the axis $\mathrm{Vect}(\nu_1\nu_2) = \nu_1\times\nu_2$ through twice the angle from $\nu_1$ to $\nu_2$.

*Proof.* The composite is $\operatorname{Ad}_p$ with $p = \nu_1\nu_2$, the product of two unit vectors, hence a unit quaternion; $\operatorname{Ad}_p$ is the inner automorphism, which fixes the centre and preserves the norm, and on $\operatorname{Im}\mathbb{H}$ it is the rotation of axis $\mathrm{Vect} p$ through twice the argument of $p$, by the half-angle formula and the rotation reading of *Quaternion Rotations and Reflections*. The product $\nu_1\nu_2$ has argument the angle from $\nu_1$ to $\nu_2$ and vector part $\nu_1\times\nu_2$, so the rotation is about $\nu_1\times\nu_2$ through twice that angle. The involution case is the perpendicular one, where $\nu_1\nu_2$ is already a unit vector and the angle is $\pi$.

## The Conjugate from Three Involutions

### The Sum of the Three Involutions

**Lemma.** Let $\nu_1,\nu_2,\nu_3$ be mutually perpendicular unit vectors and let $\mathbf q$ be a vector. Then

$$
\iota_{\nu_1}(\mathbf q)+\iota_{\nu_2}(\mathbf q)+\iota_{\nu_3}(\mathbf q) = -\mathbf q .
$$

*Proof.* Resolve $\mathbf q = \eta_1+\eta_2+\eta_3$ with $\eta_i$ parallel to $\nu_i$. The involution about $\nu_i$ fixes $\eta_i$ and negates the other two components, by the corollary on parallel and perpendicular elements; the sum is therefore $(\eta_1-\eta_2-\eta_3)+(-\eta_1+\eta_2-\eta_3)+(-\eta_1-\eta_2+\eta_3) = -\eta_1-\eta_2-\eta_3 = -\mathbf q$.

### The Conjugate Identity

**Theorem.** Let $\nu_1,\nu_2,\nu_3$ be mutually perpendicular unit vectors. For every quaternion $\tilde q$,

$$
\bar{\tilde q} = \tfrac12\bigl(\iota_{\nu_1}(\tilde q)+\iota_{\nu_2}(\tilde q)+\iota_{\nu_3}(\tilde q)-\tilde q\bigr),
\qquad
q_0 = \tfrac14\bigl(\tilde q+\iota_{\nu_1}(\tilde q)+\iota_{\nu_2}(\tilde q)+\iota_{\nu_3}(\tilde q)\bigr).
$$

*Proof.* Write $\tilde q = q_0+\mathbf q$. Each involution fixes $q_0$ and, by the lemma, the three together send $\mathbf q$ to $-\mathbf q$, so $\iota_{\nu_1}(\tilde q)+\iota_{\nu_2}(\tilde q)+\iota_{\nu_3}(\tilde q) = 3q_0-\mathbf q$. The first identity becomes $\tfrac12(3q_0-\mathbf q-q_0-\mathbf q) = q_0-\mathbf q = \bar{\tilde q}$, and the second becomes $\tfrac14(q_0+\mathbf q+3q_0-\mathbf q) = q_0$.

**Remark.** The conjugate, which is the only anti-involution among the four maps, is a fixed integer combination of the three involutions: the anti-involution is generated by the involutions even though it is not one of them. For the coordinate triple this is the recovery formula of *Quaternion Augmented Statistics*, $\bar{\tilde q} = \tfrac12(\iota_1\tilde q+\iota_2\tilde q+\iota_3\tilde q-\tilde q)$; the general form holds for every mutually perpendicular triple.

## Projections

### Projection of a Vector

**Theorem.** Let $\nu$ be a unit vector and $\mathbf q$ a vector. Then

$$
\mathbf q_{\parallel\nu} = \tfrac12\bigl(\mathbf q+\iota_\nu(\mathbf q)\bigr) = \langle\mathbf q,\nu\rangle\nu ,
\qquad
\mathbf q_{\perp\nu} = \tfrac12\bigl(\mathbf q-\iota_\nu(\mathbf q)\bigr) = \mathbf q-\langle\mathbf q,\nu\rangle\nu ,
$$

and $\mathbf q = \mathbf q_{\parallel\nu}+\mathbf q_{\perp\nu}$, the first component parallel to $\nu$ and the second perpendicular to it.

*Proof.* By the line-reflection theorem $\iota_\nu(\mathbf q) = 2\langle\mathbf q,\nu\rangle\nu-\mathbf q$. Adding gives $2\langle\mathbf q,\nu\rangle\nu$ and subtracting gives $2\mathbf q-2\langle\mathbf q,\nu\rangle\nu$. The two components are the classical parallel and perpendicular projections, so the involution computes them without naming coordinates.

### Projection of a Quaternion

**Theorem.** With $\tilde q = q_0+\mathbf q$ and $\nu$ a unit vector,

$$
\tfrac12\bigl(\tilde q+\iota_\nu(\tilde q)\bigr) = q_0+\langle\mathbf q,\nu\rangle\nu ,
\qquad
\tfrac12\bigl(\tilde q-\iota_\nu(\tilde q)\bigr) = \mathbf q-\langle\mathbf q,\nu\rangle\nu .
$$

The first component lies in the plane $\operatorname{span}(e_0,\nu)$, the Argand plane of the axis, and carries the scalar part; the second is a vector perpendicular to $\nu$.

*Proof.* The involution fixes $q_0$; applying the vector theorem to $\mathbf q$ gives the two expressions.

### The Resolution in an Orthonormal Frame

**Theorem.** Let $\nu_1,\nu_2,\nu_3$ be mutually perpendicular unit vectors. Every quaternion has a unique resolution

$$
\tilde q = a+\nu_1\alpha+\nu_2\beta+\nu_3\gamma , \qquad a,\alpha,\beta,\gamma\in\mathbb{R} ,
$$

whose coefficients are computed by the involutions from $\tilde q$ alone:

$$
a = \tfrac14\bigl(\tilde q+\iota_{\nu_1}(\tilde q)+\iota_{\nu_2}(\tilde q)+\iota_{\nu_3}(\tilde q)\bigr),
\qquad
\alpha\nu_1+\beta\nu_2+\gamma\nu_3 = \tfrac12\bigl(\tilde q-\bar{\tilde q}\bigr),
$$

and, coefficient by coefficient, with $\mathbf q = \mathrm{Vect}\tilde q$ and $b_i = \tfrac12\bigl(\mathbf q+\iota_{\nu_i}(\mathbf q)\bigr)$,

$$
\alpha\nu_1 = b_1 , \qquad \beta\nu_2 = b_2 , \qquad \gamma\nu_3 = b_3 , \qquad \alpha = \langle\mathbf q,\nu_1\rangle,\ \ \beta = \langle\mathbf q,\nu_2\rangle,\ \ \gamma = \langle\mathbf q,\nu_3\rangle .
$$

*Proof.* The scalar part is fixed by all four maps, so each of the four values has the same scalar part $a$, and their sum has scalar part $4a$; no involution contributes a further scalar, which gives the first formula. The vector part is $\mathbf q = \tfrac12(\tilde q-\bar{\tilde q})$, resolved along the three axes by the parallel projection of the vector theorem, $b_i = \langle\mathbf q,\nu_i\rangle\nu_i$, so $\alpha = \langle\mathbf q,\nu_1\rangle$ and similarly for $\beta$ and $\gamma$. Uniqueness is the uniqueness of the decomposition of the vector part in the orthonormal basis.

The resolution is the computation the involutions were introduced for: the four maps produce the four coefficients in a frame the algebra chooses, and no numerical coordinates are fixed.

## Summary

An involution of $\mathbb{H}$ is a real-linear self-inverse multiplicative map; multiplicativity is not implied by the other two axioms, and the map that exchanges $e_2$ and $e_3$ while fixing $e_0$ and $e_1$ shows it. Quaternion conjugation is an anti-involution and not an involution, and the anti-involutions are exactly the conjugate and its twists $\tilde q\mapsto-\nu\bar{\tilde q}\nu$ by the involutions.

The involutions of $\mathbb{H}$ are the identity together with the maps $\iota_\nu(\tilde q) = \nu\tilde q\nu^{-1} = -\nu\tilde q\nu$, one for each unit vector $\nu$; since $\iota_\nu = \iota_{-\nu}$, the non-trivial involutions are parametrised by the axis lines, that is by the projective plane, and the family is infinite. The class contains the three coordinate involutions $\iota_k$ of *Quaternion Augmented Statistics* and the half-turn example of *Quaternion Automorphisms and Derivations*.

An involution fixes the scalar part and the axis line and negates the perpendicular plane; on the imaginary subspace it is the reflection in the axis line, equivalently the rotation by $\pi$ about the axis, and it is the negative of the plane reflection $\rho_\nu$ of *Quaternion Rotations and Reflections*. Two involutions compose to the inner automorphism $\operatorname{Ad}_{\nu_1\nu_2}$, which is a rotation about $\nu_1\times\nu_2$ through twice the angle between the axes; perpendicular involutions commute, the involutions of a mutually perpendicular triple form a Klein four-group, and the product of two perpendicular ones is the involution about the third axis.

Three mutually perpendicular involutions recover the conjugate and the scalar part, $\bar{\tilde q} = \tfrac12(\iota_{\nu_1}\tilde q+\iota_{\nu_2}\tilde q+\iota_{\nu_3}\tilde q-\tilde q)$ and $q_0 = \tfrac14(\tilde q+\iota_{\nu_1}\tilde q+\iota_{\nu_2}\tilde q+\iota_{\nu_3}\tilde q)$; for the coordinate triple this is the recovery formula of *Quaternion Augmented Statistics*. The projection of a vector or a quaternion on an axis is $\tfrac12$ of the element plus or minus its involution, with the parallel component lying in the Argand plane of the axis, and the two formulas resolve any quaternion in any mutually perpendicular triple of axes, which is the constructive content of the family.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | Quaternion algebra |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $\tilde q = q_0e_0+q_1e_1+q_2e_2+q_3e_3$ | General quaternion, scalar part $q_0$, vector part $\mathbf q$ |
| $\mathrm{Sc}, \mathrm{Vect}$ | Scalar and vector part functionals |
| $\bar{\tilde q}$ | Quaternion conjugate, an anti-involution |
| $N(\tilde q) = \tilde q\bar{\tilde q} = \lvert\tilde q\rvert^2$ | Quaternion norm and modulus |
| $\operatorname{Im}\mathbb{H}$ | Imaginary subspace, the space of vectors |
| $\langle x,y\rangle = \mathrm{Sc}(x\bar y)$ | Real inner product on $\operatorname{Im}\mathbb{H}$ |
| $\nu$ | Unit vector, $\nu\in\operatorname{Im}\mathbb{H}$, $N(\nu) = 1$ |
| $Sp(1)$ | Unit sphere and unit group of $\mathbb{H}$ |
| $\iota_u(\tilde x) = u\tilde xu^{-1}$ | Inner automorphism (from *Quaternion Automorphisms and Derivations*) |
| $\iota_\nu(\tilde q) = \nu\tilde q\nu^{-1} = -\nu\tilde q\nu$ | Involution about the axis $\nu$, a unit vector |
| $\tilde q^{\nu} = -\nu\tilde q\nu$ | The source's notation for the value of $\iota_\nu$ |
| $\operatorname{Ad}_q(\tilde x) = q\tilde xq^{-1}$ | Adjoint action and inner automorphism |
| $\rho_\nu(\tilde x) = -\nu\tilde x\nu^{-1} = -\iota_\nu(\tilde x)$ | Plane reflection of the axis $\nu$ |
| $\operatorname{span}(e_0,\nu)$ | Argand plane of the axis $\nu$ |
| $\nu_1,\nu_2,\nu_3$ mutually perpendicular | Orthonormal frame of axes |
| $\mathbb{R}\nu$ | Axis line; the involutions are parametrised by the axis lines |

## Further Reading

- William Rowan Hamilton, *Elements of Quaternions* (Longmans, Green and Co., London, 1866), for the product of two vectors as minus the inner product plus the cross product, and the origin of the conjugate.
- H. S. M. Coxeter, "Quaternions and reflections", *American Mathematical Monthly* **53** (1946) 136–146, for the reflection of a vector in a line and in a plane and for the rotation realised by a product of two reflections.
- Todd A. Ell and Stephen J. Sangwine, "Quaternion involutions", arXiv:math/0506034 (2005), for the axioms, the infinitude of the family, the reflection reading, the composition theorems, the recovery of the conjugate and the projection formulas.
- V. M. Chernov, "Discrete orthogonal transforms with data representation in composition algebras", *Proceedings of the Scandinavian Conference on Image Analysis* (Uppsala, 1995) 357–364, for the three coordinate involutions and the recovery of the conjugate from them.
- Thomas Bülow and Gerald Sommer, "Hypercomplex signals — a novel extension of the analytic signal to the multidimensional case", *IEEE Transactions on Signal Processing* **49** (2001) 2844–2852, for the use of the involutions in signal analysis.
- Emil Artin, *Geometric Algebra* (Interscience, 1957), for the reflection groups and the structure of the orthogonal group.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the Skolem–Noether theorem and the automorphisms of central simple algebras.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the quaternion readings of reflections, rotations and the Clifford identification.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the reflection and rotation groups in quaternion terms.
