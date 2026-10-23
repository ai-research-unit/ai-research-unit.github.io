
# __Split-Quaternion Roots of Minus One__

## Introduction

This article determines the solutions of the equation $\tilde\xi^2 = -1$ in the split-quaternion algebra. It proves that the solutions are exactly the elements of the vector subspace of unit norm, identifies them with the complex structures of the plane, proves that they form a single conjugacy class and describes them as a homogeneous space, relates them to the idempotents and to the zero divisors, and compares the result with the quaternion case.

The split-quaternion algebra, its basis, its vector subspace $V$, its central product $\langle\tilde q\rangle_{\natural} = \tilde q\tilde{q}^{\natural}$, its idempotents $\tilde\pi_{1,2}$ and its conjugation are assumed from *Split-Quaternion Algebra*; the metrical reading of $\langle\cdot\rangle_{\natural}$ is in *Split-Quaternion Norm and Invertibility*. The criterion that the units are the elements with $N \neq 0$ and the description of the zero divisors are assumed from *Split-Quaternion Norm and Invertibility* and *Split-Quaternion Zero Divisors*; the zero divisor set is not re-described here. The hyperbolic plane that the solution set carries is treated in *Split-Quaternions and Hyperbolic Geometry*, and the double cover of the Lorentz group that acts on it in *Split-Quaternion Rotations and the Lorentz Group*. Nothing physical is invoked.

## The Equation and the Reduction to the Vector Subspace

**Theorem (The Solutions).** Let $\tilde\xi = q_t + \vec q$ with $q_t \in \mathbb{R}$ and $\vec q \in V$. Then $\tilde\xi^2 = -1$ if and only if

$$
\boxed{\;q_t = 0 \quad \text{and} \quad \langle \vec q\rangle_{\natural} = 1\;}.
$$

Hence the solution set is

$$
\boxed{\;\mathcal{R}_{-1} = \{\tilde\xi \in V : \langle\tilde\xi\rangle_{\natural} = 1\} = \{q_x \vec e_x + q_y \vec e_y + q_z \vec e_z : q_x^2 - q_y^2 - q_z^2 = 1\}\;},
$$

a subset of the vector subspace. No solution has a nonzero scalar part.

**Proof.** For an element of $V$ the square is $-\!N$ times the identity, by (*Split-Quaternion Norm and Invertibility*, §*The Split-Quaternion Norm*); so for $\tilde\xi = q_t + \vec q$,

$$
\tilde\xi^2 = q_t^2 + 2q_t\vec q + \vec q^2 = \big(q_t^2 - \langle \vec q\rangle_{\natural}\big) + 2q_t\vec q,
$$

where the first parenthesis is scalar and the second term is a vector. The equation $\tilde\xi^2 = -1$ splits into the two equations

$$
q_t^2 - \langle \vec q\rangle_{\natural} = -1, \qquad 2q_t\vec q = 0 .
$$

If $q_t \neq 0$ the second equation gives $\vec q = 0$, and the first then gives $q_t^2 = -1$, which has no real solution. Hence $q_t = 0$, and the first equation becomes $-\langle \vec q\rangle_{\natural} = -1$, that is $\langle \vec q\rangle_{\natural} = 1$. Conversely these two conditions give $\tilde\xi^2 = -\langle\tilde\xi\rangle_{\natural} = -1$.

**Corollary (The Root Set Is the Level Set $N = 1$).** The solution set is a two-dimensional subset of the three-dimensional vector space $V$, namely the level set $N = 1$ in $V$, with two components

$$
\mathcal{R}_{-1} = \{q_x^2 - q_y^2 - q_z^2 = 1\} = \{q_x \geq 1\} \cup \{q_x \leq -1\},
$$

the two components being distinguished by the sign of the coefficient $q_x$ of $\vec e_x$. The set is not connected, and each component is diffeomorphic to a plane.

**Proof.** The two components are the intersections of the level set with the closed half-spaces $q_x \geq 1$ and $q_x \leq -1$; on the first, $q_x = \sqrt{1 + q_y^2 + q_z^2}$, and the map $(\xi_y, \xi_z) \mapsto \big(\sqrt{1 + \xi_y^2 + \xi_z^2}, \xi_y, \xi_z\big)$ is a diffeomorphism from $\mathbb{R}^2$ onto it, and similarly for the second.

The solutions therefore have $\langle\tilde\xi\rangle_{\natural} = 1$, so by the invertibility criterion every solution is a **unit** and none is a zero divisor. This is the first point of contact with *Split-Quaternion Zero Divisors* and it is taken up again in *The Relation to the Idempotents and to the Zero Divisors* below.

## Identification with the Complex Structures of the Plane

**Theorem (The Root Set Is the Level Set $N = 1$).** The solutions of $\tilde\xi^2 = -1$ are exactly the vectors of the vector subspace with $N = 1$:

$$
\mathcal{R}_{-1} = \{\tilde\xi \in V : \langle\tilde\xi\rangle_{\natural} = 1\},
$$

the level set $q_x^2 - q_y^2 - q_z^2 = 1$; every solution has $\operatorname{Sc}\tilde\xi = 0$ and $\langle\tilde\xi\rangle_{\natural} = 1$, and conversely.

**Proof.** Write $\tilde\xi = \xi_t + \vec v$ with $\xi_t \in S$ and $\vec v \in V$. Then $\tilde\xi^2 = \xi_t^2 + 2\xi_t\vec v + \vec v^2 = \xi_t^2 + 2\xi_t\vec v - \langle \vec v\rangle_{\natural}$; this equals $-1$ exactly when the $V$-component $2\xi_t\vec v$ vanishes, so $\xi_t = 0$ or $\vec v = 0$. If $\vec v = 0$ then $\xi_t^2 = -1$, impossible over $\mathbb{R}$; hence $\xi_t = 0$ and the $S$-component gives $-\langle \vec v\rangle_{\natural} = -1$, that is $\langle\tilde\xi\rangle_{\natural} = 1$. Conversely $\tilde\xi \in V$ with $\langle\tilde\xi\rangle_{\natural} = 1$ has $\tilde\xi^2 = -\langle\tilde\xi\rangle_{\natural} = -1$.

**Corollary (The Root Set as Complex Lines).** For each solution $\tilde\xi$, the subalgebra generated by $\tilde\xi$ is

$$
\boxed{\;\mathbb{R}[\tilde\xi] = \{p + q\tilde\xi : p, q \in \mathbb{R}\} \cong \mathbb{C}\;},
$$

a copy of the complex numbers inside $\mathbb{H}_{\mathrm{s}}$, and every subalgebra of $\mathbb{H}_{\mathrm{s}}$ isomorphic to $\mathbb{C}$ arises in this way. The correspondence is two-to-one: $-\tilde\xi$ is again a solution and $\mathbb{R}[-\tilde\xi] = \mathbb{R}[\tilde\xi]$, so the map $\tilde\xi \mapsto \mathbb{R}[\tilde\xi]$ induces a bijection between the antipodal pairs $\{\pm\tilde\xi\}$ and the copies of $\mathbb{C}$, the two members of a pair lying on the two different components.

**Proof.** $\tilde\xi^2 = -1$ gives the isomorphism $p + q\tilde\xi \mapsto p + \mathrm{i}q$; conversely a subalgebra isomorphic to $\mathbb{C}$ is generated over $\mathbb{R}$ by an element with square $-1$, which is a solution, so the map is onto. For the fibres: the elements of $\mathbb{R}[\tilde\xi]$ with square $-1$ are the $p + q\tilde\xi$ with $pq = 0$ and $p^2 - q^2 = -1$, that is $p = 0$, $q = \pm1$, namely $\pm\tilde\xi$; and $\tilde\xi$ and $-\tilde\xi$ lie on the two sheets, their coefficients of $\vec e_x$ being opposite.

## The Root Set as a Conjugacy Class

**Theorem (A Single Conjugacy Class).** All solutions of $\tilde\xi^2 = -1$ are conjugate to one another under the group of units:

$$
\boxed{\;\mathcal{R}_{-1} = \{g \vec e_x g^{-1} : g \in \mathbb{H}_{\mathrm{s}}^{\times}\}\;}.
$$

The set is a single conjugacy class of the group $\mathbb{H}_{\mathrm{s}}^{\times}$, and it contains $\vec e_x$, so it is the conjugacy class of $\vec e_x$.

**Proof.** The adjoint action of the unit group on $V$ has image the Lorentz group $\mathrm{SO}(2,1)$ by *Split-Quaternion Rotations and the Lorentz Group*, §*The Adjoint Action on the Vector Subspace*, and $\mathrm{SO}(2,1)$ acts transitively on each component of the level set $N = 1$; the unit $\vec e_y$ with $N = -1$ exchanges the components. Hence every solution is conjugate to $\vec e_x$ under the unit group.

**Corollary (The Two Orbits of the Group $\{N = 1\}$).** The group $U = \{N = 1\} \cong \mathrm{SL}_2(\mathbb{R})$ is connected, so its orbits under conjugation are connected; the root set has two connected components, and $U$ acts on it with exactly two orbits, the two components of the level set. The full unit group $\mathbb{H}_{\mathrm{s}}^{\times}$ acts transitively, and the element that exchanges the two sheets is any unit of norm $-1$, for instance $\vec e_y$, since $\vec e_y \vec e_x \vec e_y^{-1} = -\vec e_x$.

**Proof.** The first statement is the connectedness of $\mathrm{SL}_2(\mathbb{R})$ and the connectedness of the two components. The action of $\vec e_y$ is the computation $\vec e_y \vec e_x = -\vec e_z = -\vec e_x \vec e_y$, so $\vec e_y \vec e_x \vec e_y^{-1} = -\vec e_x$; here $\vec e_y^{-1} = \vec e_y$ and $\langle \vec e_y\rangle_{\natural} = -1$.

## The Root Set as a Homogeneous Space

**Theorem (The Homogeneous Space).** Let $\operatorname{Cent}(\vec e_x) = \{g \in \mathbb{H}_{\mathrm{s}}^{\times} : g \vec e_x = \vec e_x g\}$ be the centraliser of $\vec e_x$ in the group of units. Then $\operatorname{Cent}(\vec e_x)$ is the group of nonzero elements of the copy $\mathbb{R}[\vec e_x] \cong \mathbb{C}$ of the complex numbers, so that

$$
\operatorname{Cent}(\vec e_x) \cong \mathbb{C}^{\times},
$$

and the map $g \mapsto g \vec e_x g^{-1}$ induces a bijection of homogeneous spaces

$$
\boxed{\;\mathcal{R}_{-1} \cong \mathbb{H}_{\mathrm{s}}^{\times} / \operatorname{Cent}(\vec e_x), \qquad \operatorname{Cent}(\vec e_x) \cong \mathbb{C}^{\times}\;}.
$$

The two sides are real surfaces: the unit group has real dimension $4$ and $\mathbb{C}^{\times}$ has real dimension $2$, so the quotient has real dimension $2$, matching the dimension of the level set.

**Proof.** An element commutes with $\vec e_x$ exactly when it lies in the subalgebra $\operatorname{span}\{1,\vec e_x\} \cong \mathbb{C}$: the elements $1$ and $\vec e_x$ commute with $\vec e_x$, while $\vec e_y$ and $\vec e_z = \vec e_x\vec e_y$ anticommute with it, since $\vec e_x\vec e_y = -\vec e_y\vec e_x$ and $\vec e_z\vec e_x = -\vec e_x\vec e_z$. The units of this subalgebra are the nonzero complex numbers, so $\operatorname{Cent}(\vec e_x) \cong \mathbb{C}^{\times}$. The orbit of $\vec e_x$ under conjugation is the whole root set by the theorem that the root set is a single conjugacy class, and the stabiliser of $\vec e_x$ is the centraliser, so the orbit–stabiliser correspondence gives the displayed bijection.

**Corollary (Each Component Is a Hyperbolic Plane).** The quotient $\mathrm{SL}_2(\mathbb{R}) / SO(2)$ is a model of the hyperbolic plane, and each component of $\mathcal{R}_{-1}$ is a copy of it, the copy carried by the component being acted on transitively by $\mathrm{SL}_2(\mathbb{R})$ with stabiliser $SO(2)$.

**Proof.** The stabiliser of $\vec e_x$ in the group $\{N = 1\}$ is $\operatorname{Cent}(\vec e_x) \cap U = GL_1(\mathbb{C}) \cap \{N=1\}$, which is the group of unit complex numbers, isomorphic to $SO(2)$; the orbit of $\vec e_x$ under $U$ is one sheet by the preceding corollary, and the orbit–stabiliser correspondence gives it as $SO(2)$-cosets. The identification of $\mathrm{SL}_2(\mathbb{R})/SO(2)$ with the hyperbolic plane is that of *Hyperbolic Geometry*.

The name for the object is therefore: **the root set is the conjugacy class of $\vec e_x$, a homogeneous space $\mathbb{H}_{\mathrm{s}}^{\times} / \mathbb{C}^{\times}$, whose two connected components are two copies of the hyperbolic plane.**

## The Relation to the Idempotents and to the Zero Divisors

### The Roots of $+1$

The companion equation clarifies the role of the two signs.

**Proposition (The Roots of $+1$).** Let $\eta = q_t + \vec q$. Then $\eta^2 = +1$ if and only if either $q_t = \pm 1$ and $\vec q = 0$, or $q_t = 0$ and $\langle \vec q\rangle_{\natural} = -1$. The non-central solutions are the vectors of the level set $N = -1$ in $V$, which has one component; the central solutions are $\pm 1$.

**Proof.** The same splitting as in the proof of the main theorem gives $q_t^2 - \langle \vec q\rangle_{\natural} = 1$ and $2q_t\vec q = 0$. If $\vec q = 0$ then $q_t = \pm 1$; if $\vec q \neq 0$ then $q_t = 0$ and $\langle \vec q\rangle_{\natural} = -1$.

**Theorem (The Idempotents Come from the Roots of $+1$).** Let $\eta \in V$ be a solution of $\eta^2 = 1$. Then

$$
\tilde\pi_+ = \tfrac{1}{2}(1 + \eta), \qquad \tilde\pi_- = \tfrac{1}{2}(1 - \eta)
$$

are idempotents with $\tilde\pi_+ + \tilde\pi_- = 1$ and $\tilde\pi_+ \tilde\pi_- = 0$, and they are zero divisors. The idempotents $\tilde\pi_{1,2}$ of (*Split-Quaternion Algebra*, §*The Idempotents*) are the case $\eta = \vec e_y$. Conversely every non-scalar idempotent of $\mathbb{H}_{\mathrm{s}}$ is of this form for a unique root $\eta$ of $+1$ in $V$, and the correspondence between non-scalar idempotents and the roots of $+1$ in $V$ is a bijection.

**Proof.** The identities are the same computation as for $\tilde\pi_{1,2}$: $\big(\tfrac12(1\pm\eta)\big)^2 = \tfrac14(1 \pm 2\eta + \eta^2) = \tfrac12(1\pm\eta)$, and the products and the sum follow from $\eta^2=1$. The product that decides the zero divisor is

$$
\Big(\tfrac12(1+\eta)\Big)\overline{\Big(\tfrac12(1+\eta)\Big)} = \tfrac14(1+\eta)(1-\eta) = \tfrac14(1-\eta^2) = 0,
$$

so the idempotent is a zero divisor, and the same holds for $\tilde\pi_-$.

For the converse, let $\tilde\pi$ be a non-scalar idempotent, and write $\tilde\pi = \tfrac12 + u$ with $u \in V$. From $\tilde\pi^2 = \tilde\pi$ one gets $u^2 = \tfrac14$, so $\langle u\rangle_{\natural} = -\tfrac14$ and $u \neq 0$; putting $\eta = 2u$ gives $\eta \in V$, $\eta^2 = 1$ and $\langle \eta\rangle_{\natural} = -1$, so $\eta$ is a root of $+1$ in $V$ and $\tilde\pi = \tfrac12(1 + \eta)$, with $\eta = 2\tilde\pi - 1$ determined by $\tilde\pi$. Also $\tilde\pi^{\natural} = \tfrac12 - u = 1 - \tilde\pi$. Put $\eta = 2\tilde\pi - 1$. Then

$$
\bar{\eta} = 2\tilde\pi^{\natural} - 1 = 2(1 - \tilde\pi) - 1 = 1 - 2\tilde\pi = -\eta,
$$

so $\eta$ lies in the $-1$ eigenspace of the conjugation, which is $V$; and $\eta^2 = 4\tilde\pi^2 - 4\tilde\pi + 1 = 1$. The element $\tilde\pi$ is recovered from $\eta$ as $\tfrac12(1+\eta)$, so the correspondence is bijective.

### The Roots Are Not Zero Divisors

**Theorem (Disjointness and Generation).** No solution of $\tilde\xi^2 = -1$ is a zero divisor. However, every solution generates a zero divisor by multiplication by an idempotent: for each solution $\tilde\xi$ and each idempotent $\tilde\pi$ of a root of $+1$, the product $\tilde\xi\tilde\pi$ is a nonzero zero divisor, since

$$
\langle\tilde\xi\tilde\pi\rangle_{\natural} = \langle\tilde\xi\rangle_{\natural} \langle\tilde\pi\rangle_{\natural} = 1 \cdot 0 = 0 .
$$

**Proof.** $\langle\tilde\xi\rangle_{\natural} = 1 \neq 0$, so $\tilde\xi$ is a unit and not a zero divisor, by *Split-Quaternion Norm and Invertibility*, §*The Invertibility Criterion*. The product $\tilde\xi\tilde\pi$ is nonzero because $\tilde\xi$ is invertible and $\tilde\pi \neq 0$, and its split-quaternion norm is zero by multiplicativity and the vanishing of $\langle\tilde\pi\rangle_{\natural}$.

The picture is therefore the following. The roots of $+1$ in $V$ form the level set $N = -1$ and produce the idempotents, which are zero divisors and split the algebra; the roots of $-1$ form the level set $N = 1$, produce the copies of $\mathbb{C}$, and are units. The two loci are disjoint level sets in the same three-dimensional space $V$, one cut out by $N = -1$ and one by $N = 1$.

## Comparison with the Quaternion and Biquaternion Cases

### The Quaternion Case

For the quaternion algebra the equation has a different solution set.

| | $\mathbb{H}$ | $\mathbb{H}_{\mathrm{s}}$ |
|---|---|---|
| equation | $\tilde\xi^2 = -1$ | $\tilde\xi^2 = -1$ |
| solution set | the level set $\{N = 1\}$ in $\operatorname{Im}\mathbb{H} \cong \mathbb{R}^3$ | the level set $\{N = 1\}$ in $V$ |
| real dimension | $2$ | $2$ |
| conjugacy class | single class under $Sp(1)$ | single class under $\mathbb{H}_{\mathrm{s}}^{\times}$ |
| homogeneous space | $Sp(1)/\mathrm{U}(1)$ | $\mathbb{H}_{\mathrm{s}}^{\times}/\mathbb{C}^{\times}$, two hyperbolic planes |
| generated algebra | a copy of $\mathbb{C}$ | a copy of $\mathbb{C}$ |

The quaternion column is the standard description of the pure imaginary units with $N = 1$, recorded in *Quaternion Algebra*, §*Basic Properties*: for a pure quaternion $\vec q$ one has $\vec q^2 = -\langle \vec q\rangle_{\natural}$, so the solutions are the elements of the level set $\{N = 1\}$ of the imaginary part. The compactness of the quaternion case and the connectivity of the two components in the split case are topological statements and belong to *Split-Quaternion Topology*; what is used here is the algebraic statement that the solutions are the complex structures of a plane, which in the quaternion case are the complex structures of the imaginary three-space and in the split case are those of a real two-space.

### The Biquaternion Case

The algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ of the notation table is a later system of Part V, treated under Biquaternions, and nothing of it is used here. One structural remark is available from the conventions alone: $\mathbb{B}$ is an algebra over the field $\mathbb{C}$, and the equation $\tilde\Xi^2 = -1$ over a complex algebra has the two central solutions $\tilde\Xi = \pm i$ in addition to whatever further solutions the embedded real structure supplies; the root set is therefore strictly larger there, and its classification belongs to the later category. The present article is complete for the algebra over $\mathbb{R}$.

## Summary

The solutions of $\tilde\xi^2 = -1$ in the split-quaternion algebra are exactly the elements of the vector subspace $V$ with $\langle\tilde\xi\rangle_{\natural} = 1$, that is, the points of the level set $q_x^2 - q_y^2 - q_z^2 = 1$; no solution has a nonzero scalar part, and every solution has $N = 1$, so every solution is a unit and none is a zero divisor.

Each solution is a vector of the vector subspace with $\operatorname{Sc} = 0$ and $N = 1$; each solution generates a copy of $\mathbb{C}$ inside the algebra, and the map from the solutions to the copies of $\mathbb{C}$ is two-to-one, $\tilde\xi$ and $-\tilde\xi$ generating the same copy, so that the antipodal pairs correspond bijectively to the copies of $\mathbb{C}$, one point of each pair on each sheet.

The solutions form a single conjugacy class, the class of $\vec e_x$; the stabiliser of $\vec e_x$ is its centraliser $\mathbb{C}^{\times}$, so the root set is the homogeneous space $\mathbb{H}_{\mathrm{s}}^{\times}/\mathbb{C}^{\times}$, of real dimension two. The group $U \cong \mathrm{SL}_2(\mathbb{R})$ acts with two orbits, the two components, and each component is a copy of the hyperbolic plane $\mathrm{SL}_2(\mathbb{R})/SO(2)$.

The roots of $+1$ play the companion role: they are $\pm 1$ together with the level set $N = -1$ in $V$, and each non-central root of $+1$ produces the idempotents $\tfrac12(1 \pm \eta)$, which are zero divisors; the idempotents $\tilde\pi_{1,2}$ are the case $\eta = \vec e_y$. Every solution of $\tilde\xi^2 = -1$ generates a zero divisor by multiplication with an idempotent, although it is not itself one. In the quaternion case the solution set is the compact connected two-dimensional set and the homogeneous space is $Sp(1)/\mathrm{U}(1)$; the biquaternion case is a later system of Part V, named and pointed forward.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $\tilde\xi^2 = -1$ | the equation of the article | this article |
| $\mathcal{R}_{-1} = \{\tilde\xi \in V : \langle\tilde\xi\rangle_{\natural} = 1\}$ | the solution set | this article |
| $q_x^2 - q_y^2 - q_z^2 = 1$ | the level set $N = 1$ in the basis $\vec e_x,\vec e_y,\vec e_z$ | this article |
| $X^2 = -I$ | the corresponding equation for matrices | this article |
| $GL_1(\mathbb{C})$ | the centraliser of a complex structure, $\cong \mathbb{C}^{\times}$ | this article |
| $\operatorname{Cent}(\vec e_x)$ | the centraliser of $\vec e_x$, $\cong \mathbb{C}^{\times}$ | this article |
| $\mathcal{R}_{-1} \cong \mathbb{H}_{\mathrm{s}}^{\times}/\mathbb{C}^{\times}$ | the root set as a homogeneous space | this article |
| $\eta^2 = +1$, $\langle \eta\rangle_{\natural} = -1$ | the root set of $+1$ in $V$ | this article |
| $\tfrac12(1 \pm \eta)$ | the idempotents attached to a root of $+1$ | this article |
| $U = \{N=1\} \cong \mathrm{SL}_2(\mathbb{R})$ | the group of units with $N = 1$ | *Split-Quaternion Norm and Invertibility* |
| $V$ | the vector subspace | *Split-Quaternion Algebra* |
| $\mathbb{H}_{\mathbb{D}}$, $\mathbb{B}$ | later Part V systems, named only | *The Number Systems as Clifford Algebras* |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for the square roots of $-1$ in low-dimensional Clifford algebras and their role as complex structures.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the conjugacy classes of the pseudo-orthogonal groups and the orbit–stabiliser description.
- Igor R. Shafarevich, *Basic Algebraic Geometry 1* (Springer, 2013), for the hyperboloids and the quadrics of a pseudo-Euclidean space.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the comparison between the definite and indefinite cases of the roots of $-1$.
