
# __Split-Quaternion Roots of Minus One__

## Introduction

This article determines the solutions of the equation $\xi^2 = -1$ in the split-quaternion algebra. It proves that the solutions are exactly the elements of the vector subspace of unit norm, identifies them with the complex structures of the plane, proves that they form a single conjugacy class and describes them as a homogeneous space, relates them to the idempotents and to the zero divisors, and compares the result with the quaternion case.

The split-quaternion algebra, its basis, its vector subspace $V$, its norm form $N$, its matrix model $\Phi$, its idempotents $u_\pm$ and its conjugation are assumed from *Split-Quaternion Algebra*. The criterion that the units are the elements with $N \neq 0$ and the description of the zero divisors are assumed from *Split-Quaternion Norm and Invertibility* and *Split-Quaternion Zero Divisors*; the zero divisor set is not re-described here. The hyperbolic plane that the solution set carries is treated in *Split-Quaternions and Hyperbolic Geometry*, and the double cover of the Lorentz group that acts on it in *Split-Quaternion Rotations and the Lorentz Group*. Nothing physical is invoked.

## The Equation and the Reduction to the Vector Subspace

**Theorem (The Solutions).** Let $\xi = a + \mathbf{u}$ with $a \in \mathbb{R}$ and $\mathbf{u} \in V$. Then $\xi^2 = -1$ if and only if

$$
a = 0 \quad \text{and} \quad N(\mathbf{u}) = 1 .
$$

Hence the solution set is

$$
\mathcal{R}_{-1} = \{\xi \in V : N(\xi) = 1\} = \{b e_1 + c e_2 + d e_3 : b^2 - c^2 - d^2 = 1\},
$$

a subset of the vector subspace. No solution has a nonzero scalar part.

**Proof.** For an element of $V$ the square is $-\!N$ times the identity, by (*Split-Quaternion Algebra*, §*The Restricted Form on the Vector Subspace*); so for $\xi = a + \mathbf{u}$,

$$
\xi^2 = a^2 + 2a\mathbf{u} + \mathbf{u}^2 = \big(a^2 - N(\mathbf{u})\big) + 2a\mathbf{u},
$$

where the first parenthesis is scalar and the second term is a vector. The equation $\xi^2 = -1$ splits into the two equations

$$
a^2 - N(\mathbf{u}) = -1, \qquad 2a\mathbf{u} = 0 .
$$

If $a \neq 0$ the second equation gives $\mathbf{u} = 0$, and the first then gives $a^2 = -1$, which has no real solution. Hence $a = 0$, and the first equation becomes $-N(\mathbf{u}) = -1$, that is $N(\mathbf{u}) = 1$. Conversely these two conditions give $\xi^2 = -N(\xi) = -1$. $\square$

**Corollary (The Root Set Is a Two-Sheeted Hyperboloid).** The solution set is a surface in the three-dimensional vector space $V$, namely the level set $N = 1$ of the signature-$(2,1)$ form, a hyperboloid of two sheets

$$
\mathcal{R}_{-1} = \{b^2 - c^2 - d^2 = 1\} = \{b \geq 1\} \cup \{b \leq -1\},
$$

the two sheets being distinguished by the sign of the coefficient $b$ of $e_1$. The set is not connected, and each sheet is diffeomorphic to a plane.

**Proof.** The two sheets are the intersections of the level set with the closed half-spaces $b \geq 1$ and $b \leq -1$; on the first, $b = \sqrt{1 + c^2 + d^2}$, and the map $(\xi_2, \xi_3) \mapsto \big(\sqrt{1 + \xi_2^2 + \xi_3^2}, \xi_2, \xi_3\big)$ is a diffeomorphism from $\mathbb{R}^2$ onto it, and similarly for the second. $\square$

The solutions therefore have norm one, $N(\xi) = 1$, so by the invertibility criterion every solution is a **unit** and none is a zero divisor. This is the first point of contact with *Split-Quaternion Zero Divisors* and it is taken up again in *The Relation to the Idempotents and to the Zero Divisors* below.

## Identification with the Complex Structures of the Plane

The matrix model turns the equation into a familiar one.

**Definition.** A **complex structure** on $\mathbb{R}^2$ is a real-linear map $J : \mathbb{R}^2 \to \mathbb{R}^2$ with $J^2 = -\mathrm{id}$. It makes $\mathbb{R}^2$ a one-dimensional complex vector space with multiplication $(p + iq)\cdot v = pv + qJv$.

**Theorem (The Root Set Is the Set of Complex Structures).** Under the isomorphism $\Phi : \mathbb{H}_{\mathrm{s}} \to M_2(\mathbb{R})$, the solutions of $\xi^2 = -1$ correspond exactly to the complex structures of $\mathbb{R}^2$:

$$
\Phi(\mathcal{R}_{-1}) = \{X \in M_2(\mathbb{R}) : X^2 = -I\} .
$$

A solution $\xi$ and its image $X = \Phi(\xi)$ satisfy $\operatorname{tr} X = 0$ and $\det X = 1$, and conversely every matrix with trace $0$ and determinant $1$ is an image of a solution.

**Proof.** The model is an algebra isomorphism carrying $-1$ to $-I$, so $\xi^2 = -1$ is equivalent to $X^2 = -I$. For the trace and determinant, the Cayley–Hamilton identity for a $2 \times 2$ matrix reads $X^2 - (\operatorname{tr}X) X + (\det X) I = 0$. If $X^2 = -I$, then $(\det X - 1) I = (\operatorname{tr} X) X$. If $\operatorname{tr} X \neq 0$, the identity exhibits $X$ as a scalar matrix, $X = \lambda I$, and then $X^2 = \lambda^2 I = -I$ has no real solution; so $\operatorname{tr} X = 0$, and then the identity gives $\det X = 1$. Conversely, if $\operatorname{tr} X = 0$ and $\det X = 1$, Cayley–Hamilton reads $X^2 + I = 0$. $\square$

**Corollary (The Root Set as Complex Lines).** For each solution $\xi$, the subalgebra generated by $\xi$ is

$$
\mathbb{R}[\xi] = \{p + q\xi : p, q \in \mathbb{R}\} \cong \mathbb{C},
$$

a copy of the complex numbers inside $\mathbb{H}_{\mathrm{s}}$, and every subalgebra of $\mathbb{H}_{\mathrm{s}}$ isomorphic to $\mathbb{C}$ arises in this way. The correspondence is two-to-one: $-\xi$ is again a solution and $\mathbb{R}[-\xi] = \mathbb{R}[\xi]$, so the map $\xi \mapsto \mathbb{R}[\xi]$ induces a bijection between the antipodal pairs $\{\pm\xi\}$ and the copies of $\mathbb{C}$, the two members of a pair lying on the two different sheets.

**Proof.** $\xi^2 = -1$ gives the isomorphism $p + q\xi \mapsto p + \mathrm{i}q$; conversely a subalgebra isomorphic to $\mathbb{C}$ is generated over $\mathbb{R}$ by an element with square $-1$, which is a solution, so the map is onto. For the fibres: the elements of $\mathbb{R}[\xi]$ with square $-1$ are the $p + q\xi$ with $pq = 0$ and $p^2 - q^2 = -1$, that is $p = 0$, $q = \pm1$, namely $\pm\xi$; and $\xi$ and $-\xi$ lie on the two sheets, their coefficients of $e_1$ being opposite. $\square$

The identification is the reason the matrix model is decisive here: the condition $\xi^2 = -1$ is a condition on a linear map, and the statement that the solutions are the complex structures of the plane is invisible in the generator description $b^2 - c^2 - d^2 = 1$ but immediate in the matrix description.

## The Root Set as a Conjugacy Class

**Theorem (A Single Conjugacy Class).** All solutions of $\xi^2 = -1$ are conjugate to one another under the group of units:

$$
\mathcal{R}_{-1} = \{g e_1 g^{-1} : g \in \mathbb{H}_{\mathrm{s}}^{\times}\} .
$$

The set is a single conjugacy class of the group $\mathbb{H}_{\mathrm{s}}^{\times}$, and it contains $e_1$, so it is the conjugacy class of $e_1$.

**Proof.** Transport the statement to matrices. Let $X^2 = -I$ and let $v \neq 0$. The vectors $v$ and $Xv$ are linearly independent: if $Xv = \lambda v$ for a real $\lambda$, then applying $X$ gives $-v = \lambda Xv = \lambda^2 v$, so $\lambda^2 = -1$, impossible. In the basis $(v, Xv)$ the map $X$ has the matrix

$$
\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix} = \Phi(e_1),
$$

since $Xv$ has coordinates $(0,1)$ and $X(Xv) = -v$ has coordinates $(-1,0)$. Hence $X$ is the conjugate of $\Phi(e_1)$ by the change-of-basis matrix, and $X$ is conjugate to $\Phi(e_1)$ within $GL_2(\mathbb{R})$. Transporting through $\Phi$ gives the statement. $\square$

**Corollary (The Two Orbits of the Norm-One Group).** The norm-one group $U = \{N = 1\} \cong \mathrm{SL}_2(\mathbb{R})$ is connected, so its orbits under conjugation are connected; the root set has two connected components, and $U$ acts on it with exactly two orbits, the two sheets of the hyperboloid. The full unit group $\mathbb{H}_{\mathrm{s}}^{\times}$ acts transitively, and the element that exchanges the two sheets is any unit of norm $-1$, for instance $e_2$, since $e_2 e_1 e_2^{-1} = -e_1$.

**Proof.** The first statement is the connectedness of $\mathrm{SL}_2(\mathbb{R})$ and the connectedness of the two sheets. The action of $e_2$ is the computation $e_2 e_1 = -e_3 = -e_1 e_2$, so $e_2 e_1 e_2^{-1} = -e_1$; here $e_2^{-1} = e_2$ and $N(e_2) = -1$. $\square$

## The Root Set as a Homogeneous Space

**Theorem (The Homogeneous Space).** Let $\operatorname{Cent}(e_1) = \{g \in \mathbb{H}_{\mathrm{s}}^{\times} : g e_1 = e_1 g\}$ be the centraliser of $e_1$ in the group of units. Then $\operatorname{Cent}(e_1)$ is the group of nonzero elements of the copy $\mathbb{R}[e_1] \cong \mathbb{C}$ of the complex numbers, so that

$$
\operatorname{Cent}(e_1) \cong \mathbb{C}^{\times},
$$

and the map $g \mapsto g e_1 g^{-1}$ induces a bijection of homogeneous spaces

$$
\mathcal{R}_{-1} \cong \mathbb{H}_{\mathrm{s}}^{\times} / \operatorname{Cent}(e_1) \cong GL_2(\mathbb{R}) / GL_1(\mathbb{C}).
$$

The two sides are real surfaces: $\dim_{\mathbb{R}} GL_2(\mathbb{R}) = 4$ and $\dim_{\mathbb{R}} \mathbb{C}^{\times} = 2$, so the quotient has real dimension $2$, matching the dimension of the hyperboloid.

**Proof.** In the matrix model $e_1$ corresponds to the rotation matrix $J$. A matrix $M$ commutes with $J$ exactly when $M$ has the form $\begin{pmatrix} p & q \\ -q & p \end{pmatrix} = p I + q J$ with $(p,q) \neq (0,0)$, since the equations $MJ = JM$ are $r = -q$ and $s = p$; such matrices are precisely the nonzero complex numbers acting on $\mathbb{R}^2 \cong \mathbb{C}$, and they are invertible with determinant $p^2 + q^2$. Hence the centraliser is $GL_1(\mathbb{C}) \cong \mathbb{C}^{\times}$. The orbit of $e_1$ under conjugation is the whole root set by the theorem that the root set is a single conjugacy class, and the stabiliser of $e_1$ is the centraliser, so the orbit–stabiliser correspondence gives the displayed bijection. $\square$

**Corollary (Each Sheet Is a Hyperbolic Plane).** The quotient $\mathrm{SL}_2(\mathbb{R}) / SO(2)$ is a model of the hyperbolic plane, and each sheet of $\mathcal{R}_{-1}$ is a copy of it, the copy carried by the sheet being acted on transitively by $\mathrm{SL}_2(\mathbb{R})$ with stabiliser $SO(2)$.

**Proof.** The stabiliser of $e_1$ in the norm-one group is $\operatorname{Cent}(e_1) \cap U = GL_1(\mathbb{C}) \cap \{N=1\}$, which is the group of unit complex numbers, isomorphic to $SO(2)$; the orbit of $e_1$ under $U$ is one sheet by the preceding corollary, and the orbit–stabiliser correspondence gives it as $SO(2)$-cosets. The identification of $\mathrm{SL}_2(\mathbb{R})/SO(2)$ with the hyperbolic plane is that of *Hyperbolic Geometry*. $\square$

The name for the object is therefore: **the root set is the conjugacy class of $e_1$, a homogeneous space $\mathbb{H}_{\mathrm{s}}^{\times} / \mathbb{C}^{\times}$, whose two connected components are two copies of the hyperbolic plane.**

## The Relation to the Idempotents and to the Zero Divisors

### The Roots of $+1$

The companion equation clarifies the role of the two signs.

**Proposition (The Roots of $+1$).** Let $\eta = a + \mathbf{u}$. Then $\eta^2 = +1$ if and only if either $a = \pm 1$ and $\mathbf{u} = 0$, or $a = 0$ and $N(\mathbf{u}) = -1$. The non-central solutions are the vectors of the **spacelike unit hyperboloid** $N = -1$ in $V$, a one-sheeted hyperboloid; the central solutions are $\pm 1$.

**Proof.** The same splitting as in the proof of the main theorem gives $a^2 - N(\mathbf{u}) = 1$ and $2a\mathbf{u} = 0$. If $\mathbf{u} = 0$ then $a = \pm 1$; if $\mathbf{u} \neq 0$ then $a = 0$ and $N(\mathbf{u}) = -1$. $\square$

**Theorem (The Idempotents Come from the Roots of $+1$).** Let $\eta \in V$ be a solution of $\eta^2 = 1$. Then

$$
p_+ = \tfrac{1}{2}(1 + \eta), \qquad p_- = \tfrac{1}{2}(1 - \eta)
$$

are idempotents with $p_+ + p_- = 1$ and $p_+ p_- = 0$, and they are zero divisors. The idempotents $u_\pm$ of (*Split-Quaternion Algebra*, §*The Idempotents*) are the case $\eta = e_2$. Conversely every non-scalar idempotent of $\mathbb{H}_{\mathrm{s}}$ is of this form for a unique root $\eta$ of $+1$ in $V$, and the correspondence between non-scalar idempotents and the roots of $+1$ in $V$ is a bijection.

**Proof.** The identities are the same computation as for $u_\pm$: $\big(\tfrac12(1\pm\eta)\big)^2 = \tfrac14(1 \pm 2\eta + \eta^2) = \tfrac12(1\pm\eta)$, and the products and the sum follow from $\eta^2=1$. The norm is

$$
N\big(\tfrac12(1+\eta)\big) = \tfrac14\big(N(1) + 2B(1,\eta) + N(\eta)\big) = \tfrac14(1 + 0 - 1) = 0,
$$

so the idempotent is a zero divisor, and the same holds for $p_-$.

For the converse, let $p$ be a non-scalar idempotent. A non-scalar idempotent of $M_2(\mathbb{R})$ has minimal polynomial dividing $x^2 - x$ but not equal to $x$ or to $x - 1$, so its eigenvalues are $0$ and $1$ and its trace is $1$; equivalently $\operatorname{rank} \Phi(p) = 1$ and $\operatorname{tr}\Phi(p) = 1$. For every $2 \times 2$ matrix the adjugate is $\operatorname{adj} M = (\operatorname{tr} M) I - M$, by direct computation, so for $p$ the identity $\Phi(\bar{p}) = \operatorname{adj}\Phi(p)$ of (*Split-Quaternion Algebra*, §*The Conjugation*) gives $\bar{p} = \operatorname{tr}(p) - p = 1 - p$. Put $\eta = 2p - 1$. Then

$$
\bar{\eta} = 2\bar{p} - 1 = 2(1 - p) - 1 = 1 - 2p = -\eta,
$$

so $\eta$ lies in the $-1$ eigenspace of the conjugation, which is $V$; and $\eta^2 = 4p^2 - 4p + 1 = 1$. The element $p$ is recovered from $\eta$ as $\tfrac12(1+\eta)$, so the correspondence is bijective. $\square$

### The Roots Are Not Zero Divisors

**Theorem (Disjointness and Generation).** No solution of $\xi^2 = -1$ is a zero divisor. However, every solution generates a zero divisor by multiplication by an idempotent: for each solution $\xi$ and each idempotent $p$ of a root of $+1$, the product $\xi p$ is a nonzero zero divisor, since

$$
N(\xi p) = N(\xi) N(p) = 1 \cdot 0 = 0 .
$$

**Proof.** $N(\xi) = 1 \neq 0$, so $\xi$ is a unit and not a zero divisor, by *Split-Quaternion Norm and Invertibility*, §*The Invertibility Criterion*. The product $\xi p$ is nonzero because $\xi$ is invertible and $p \neq 0$, and its norm is zero by multiplicativity and the vanishing of $N(p)$. $\square$

The picture is therefore the following. The roots of $+1$ in $V$ form a one-sheeted hyperboloid and produce the idempotents, which are zero divisors and split the algebra; the roots of $-1$ form a two-sheeted hyperboloid, produce the copies of $\mathbb{C}$, and are units. The two loci are disjoint hyperboloids in the same three-dimensional space $V$, one of signature $+1$ in its defining equation and one of norm $-1$.

## Comparison with the Quaternion and Biquaternion Cases

### The Quaternion Case

For the quaternion algebra the equation has a different solution set.

| | $\mathbb{H}$ | $\mathbb{H}_{\mathrm{s}}$ |
|---|---|---|
| equation | $\xi^2 = -1$ | $\xi^2 = -1$ |
| solution set | the unit sphere of $\operatorname{Im}\mathbb{H} \cong \mathbb{R}^3$ | the two-sheeted hyperboloid $\{N=1\} \subset V$ |
| topology | $S^2$, compact and connected | two planes, non-compact and disconnected |
| conjugacy class | single class under $Sp(1)$ | single class under $\mathbb{H}_{\mathrm{s}}^{\times}$ |
| homogeneous space | $Sp(1)/U(1) \cong S^2$ | $\mathbb{H}_{\mathrm{s}}^{\times}/\mathbb{C}^{\times}$, two hyperbolic planes |
| generated algebra | a copy of $\mathbb{C}$ | a copy of $\mathbb{C}$ |

The quaternion column is the standard description of the pure imaginary units of norm one, recorded in *Quaternion Algebra*, §*The Norm Form*: for a pure quaternion $\mathbf{u}$ one has $\mathbf{u}^2 = -N(\mathbf{u})$, so the solutions are the elements of the unit sphere of the imaginary part. The compactness is lost in the split case, and the connectedness of the root set is lost with it; what survives is the statement that the solutions are the complex structures of a plane, which in the quaternion case are the complex structures of the imaginary three-space and in the split case are those of a real two-space.

### The Biquaternion Case

The algebra $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ of the notation table is a later system of Part V, treated under Biquaternions, and nothing of it is used here. One structural remark is available from the conventions alone: $\mathbb{B}$ is an algebra over the field $\mathbb{C}$, and the equation $\xi^2 = -1$ over a complex algebra has the two central solutions $\xi = \pm i$ in addition to whatever further solutions the embedded real structure supplies; the root set is therefore strictly larger there, and its classification belongs to the later category. The present article is complete for the algebra over $\mathbb{R}$.

## Summary

The solutions of $\xi^2 = -1$ in the split-quaternion algebra are exactly the elements of the vector subspace $V$ with $N(\xi) = 1$, that is, the points of the two-sheeted hyperboloid $b^2 - c^2 - d^2 = 1$; no solution has a nonzero scalar part, and every solution has norm one, so every solution is a unit and none is a zero divisor.

Under the matrix model the solutions correspond to the complex structures of $\mathbb{R}^2$, the matrices $X$ with $X^2 = -I$, equivalently the matrices with trace $0$ and determinant $1$; each solution generates a copy of $\mathbb{C}$ inside the algebra, and the map from the solutions to the copies of $\mathbb{C}$ is two-to-one, $\xi$ and $-\xi$ generating the same copy, so that the antipodal pairs correspond bijectively to the copies of $\mathbb{C}$, one point of each pair on each sheet.

The solutions form a single conjugacy class, the class of $e_1$; the stabiliser of $e_1$ is its centraliser $\mathbb{C}^{\times}$, so the root set is the homogeneous space $\mathbb{H}_{\mathrm{s}}^{\times}/\mathbb{C}^{\times} \cong GL_2(\mathbb{R})/GL_1(\mathbb{C})$, of real dimension two. The norm-one group $U \cong \mathrm{SL}_2(\mathbb{R})$ acts with two orbits, the two sheets, and each sheet is a copy of the hyperbolic plane $\mathrm{SL}_2(\mathbb{R})/SO(2)$.

The roots of $+1$ play the companion role: they are $\pm 1$ together with the one-sheeted hyperboloid $N = -1$ in $V$, and each non-central root of $+1$ produces the idempotents $\tfrac12(1 \pm \eta)$, which are zero divisors; the idempotents $u_\pm$ are the case $\eta = e_2$. Every solution of $\xi^2 = -1$ generates a zero divisor by multiplication with an idempotent, although it is not itself one. In the quaternion case the solution set is the compact connected sphere $S^2$ and the homogeneous space is $Sp(1)/U(1)$; the biquaternion case is a later system of Part V, named and pointed forward.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $\xi^2 = -1$ | the equation of the article | this article |
| $\mathcal{R}_{-1} = \{\xi \in V : N(\xi) = 1\}$ | the solution set | this article |
| $b^2 - c^2 - d^2 = 1$ | the two-sheeted hyperboloid in the basis $e_1,e_2,e_3$ | this article |
| $X^2 = -I$ | the corresponding equation for matrices | this article |
| $GL_1(\mathbb{C})$ | the centraliser of a complex structure, $\cong \mathbb{C}^{\times}$ | this article |
| $\operatorname{Cent}(e_1)$ | the centraliser of $e_1$, $\cong \mathbb{C}^{\times}$ | this article |
| $\mathcal{R}_{-1} \cong \mathbb{H}_{\mathrm{s}}^{\times}/\mathbb{C}^{\times}$ | the root set as a homogeneous space | this article |
| $\eta^2 = +1$, $N(\eta) = -1$ | the root set of $+1$ in $V$ | this article |
| $\tfrac12(1 \pm \eta)$ | the idempotents attached to a root of $+1$ | this article |
| $U = \{N=1\} \cong \mathrm{SL}_2(\mathbb{R})$ | the norm-one group | *Split-Quaternion Norm and Invertibility* |
| $V$ | the vector subspace | *Split-Quaternion Algebra* |
| $\mathbb{H}_{\mathbb{D}}$, $\mathbb{B}$ | later Part V systems, named only | *The Number Systems as Clifford Algebras* |

## Further Reading

- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for the square roots of $-1$ in low-dimensional Clifford algebras and their role as complex structures.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the conjugacy classes of the pseudo-orthogonal groups and the orbit–stabiliser description.
- Igor R. Shafarevich, *Basic Algebraic Geometry 1* (Springer, 2013), for the hyperboloids and the quadrics of a pseudo-Euclidean space.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the comparison between the definite and indefinite cases of the roots of $-1$.
