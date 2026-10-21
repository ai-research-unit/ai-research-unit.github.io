# __The Krein Form and the Indefinite Structure__

## Introduction

The fourth form of the biquaternion algebra is Hermitian and indefinite. On two elements it is

$$
\langle\tilde P,\tilde Q\rangle_{\natural*}=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu P_\mu\overline{Q_\mu},
\qquad \varepsilon=(1,-1,-1,-1),
$$

and at two equal arguments it is real. It has signature $(1,3)$ over $\mathbb{C}$ and $(2,6)$ over $\mathbb{R}$, it fixes no overall sign, and it cannot normalise a state. Those are not defects of the form; they are the structure it carries. Its level sets are hyperboloids rather than spheres, its positive lines form a complex hyperbolic space, and its isometry group is $\mathrm{U}(1,3)$, not the Lorentz group.

The physical reading of the form itself — the gauge calibration, the sign relation to the interval on the material sector — is the subject of this article. The article gives the Gram matrix, the fundamental symmetry, the isometry group, the level sets, the hyperbolic geometry and the $J$-contractions. It states the geometry and the readings, and it states where the readings stop.

The article is a reader. The mathematics is owned by *The Krein Form as a Product on the Symmetric Quaternionic Sesqualgebra*, *The Krein Gram Matrix and the Restrictions of the Form*, *The Krein Isometry Group and Its $J$-Contractions*, *The Krein Level Sets and the Hyperbolic Structure*, *Indefinite Positivity and the Krein Cone* and *The Isotropic Structure of the General Quaternionic Sesqualgebra*.

## The Results It Uses

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| The form as a product, its Hermitian character and its signatures | [The Krein Form as a Product on the Symmetric Quaternionic Sesqualgebra](../articles_maths/the-krein-form-as-a-product-on-the-symmetric-quaternionic-sesqualgebra.html) |
| The Gram matrix and the restrictions to the subspaces | [The Krein Gram Matrix and the Restrictions of the Form](../articles_maths/the-krein-gram-matrix-and-the-restrictions-of-the-form.html) |
| The isometry group, the boosts and the $J$-contractions | [The Krein Isometry Group and Its $J$-Contractions](../articles_maths/the-krein-isometry-group-and-its-j-contractions.html) |
| The level sets and the two hyperbolic models | [The Krein Level Sets and the Hyperbolic Structure](../articles_maths/the-krein-level-sets-and-the-hyperbolic-structure.html) |
| The Krein cone, the operator cone and the indefinite positivity | [Indefinite Positivity and the Krein Cone of the Biquaternion Algebra](../articles_maths/indefinite-positivity-and-the-krein-cone-of-the-biquaternion-algebra.html) |
| The null set, the doubly-null lines and the totally isotropic subspaces | [The Isotropic Structure of the General Quaternionic Sesqualgebra](../articles_maths/the-isotropic-structure-of-the-general-quaternionic-sesqualgebra.html) |
| The fundamental decomposition and the Krein-orthogonal projections | [Krein Orthogonality and the Fundamental Decomposition](../articles_maths/krein-orthogonality-and-the-fundamental-decomposition.html) |
| The Cartan decomposition and the symmetric space | [The Krein Cartan Decomposition of the Operator Algebra](../articles_maths/the-krein-cartan-decomposition-of-the-operator-algebra.html) |
| The fundamental symmetry $J={}^{\natural}$ | [The Fundamental Symmetry of the Biquaternion Algebra](../articles_maths/the-fundamental-symmetry-of-the-biquaternion-algebra.html) |

## The Form and Its Gram Matrix

In the coefficient basis the form is written with the matrix

$$
E=\operatorname{diag}(1,-1,-1,-1),
$$

so that $\langle\tilde P,\tilde Q\rangle_{\natural*}=P^{\mathsf T}E\bar Q$ in the convention linear in the first argument. The matrix is Hermitian and invertible, with one positive and three negative eigenvalues. The form is therefore indefinite, and its **inertia** is $(1,3)$ over $\mathbb{C}$; after realification, the real form has signature $(2,6)$.

| Subspace | The restricted form | Signature |
| --- | --- | --- |
| Centre $\mathbb{C}_{\mathbb{B}}$ | $\lvert c\rvert^2$ | $(1,0)$ over $\mathbb{C}$ |
| Vector space $\mathrm{Vect}(\mathbb{B})$ | $-\lVert v\rVert^2$ | $(0,3)$ over $\mathbb{C}$ |
| Informational sector $\mathbb{M}_+$ | the interval $\langle\tilde Q\rangle_{\natural}$ | $(1,3)$ over $\mathbb{R}$ |
| Material sector $\mathbb{M}_-$ | minus the interval $-\langle\tilde Q\rangle_{\natural}$ | $(1,3)$ over $\mathbb{R}$ |
| Real quaternion space $\mathbb{H}_{\mathbb{B}}$ | the interval | $(1,3)$ over $\mathbb{R}$ |
| Imaginary quaternion space $i\mathbb{H}_{\mathbb{B}}$ | minus the interval | $(1,3)$ over $\mathbb{R}$ |

The table is the whole of the sign story. The centre is positive, the vector space is negative, and on each of the two sectors the form is the interval read with a sign. On the material sector the sign is minus; on the informational sector it is plus. The four real forms carry the same signature $(1,3)$; the minus signs record the relation to the quaternionic norm, not a different inertia. The form is real at equal arguments because the diagonal entries are real, and it is indefinite because the two contributions have opposite signs.

The indefiniteness is what makes the form unable to normalise. A definite Hermitian form has a compact unit sphere and a trace-one slice; the Krein form has neither. Its "unit" level set is a hyperboloid, non-compact and of real dimension seven. A state that needs a normalised representative must use the definite Born form, not this one.

## The Fundamental Symmetry

The indefinite form is a definite form in disguise. Let $J={}^{\natural}$ be the natural conjugation, fixing the central $i$ and negating the three vector units. Then

$$
\langle\tilde P,\tilde Q\rangle_{\natural*}=\langle\tilde P,J\tilde Q\rangle_{*},
\qquad
\langle\tilde P,\tilde Q\rangle_{*}=\sum_\mu P_\mu\overline{Q_\mu},
$$

and $J^2=\mathrm{id}$. The operator $J$ is the **fundamental symmetry** of the form: it is a real linear involution with eigenvalue $+1$ on the centre and $-1$ on the vector space, and it is an isometry of the Krein form.

The decomposition into the two eigenspaces,

$$
\mathbb{B}=\mathbb{C}_{\mathbb{B}}\oplus\mathrm{Vect}(\mathbb{B}),
$$

is the **fundamental decomposition**. The form is positive definite on the first summand and negative definite on the second, and the two summands are Krein-orthogonal. Every statement about the indefinite form can be read as a statement about the definite form together with the involution $J$; the indefinite structure is the twist.

Physically, $J$ is the parity of the frame: it fixes the clock direction and reverses every spatial direction. That the algebra carries this involution on its own is the statement that the gauge's parity is not an extra choice. The sign vector $\varepsilon$ inside the product is the same object in coordinates.

## The Isometry Group

A **Krein isometry** is a $\mathbb{C}$-linear operator preserving the form:

$$
U_J(\mathbb{B})=\{T:T^{\mathsf T}E\bar T=E\}.
$$

In the coefficient basis the group is $\mathrm{U}(1,3)$. It has real dimension $16$, it is non-compact, its centre is the circle $\mathrm{U}(1)$ of scalar matrices of modulus one, and its maximal compact subgroup is $\mathrm{U}(1)\times\mathrm{U}(3)$, the group preserving the canonical fundamental decomposition.

The group is not the Lorentz group. It is larger: it rotates the centre into the centre and the vector space into itself only in its compact part, and its general element mixes the two. The proper orthochronous Lorentz group of the material sector is the subgroup that preserves the real form $\mathbb{M}_-$ and its time orientation; it has dimension $6$ inside the $16$ of $\mathrm{U}(1,3)$. The extra dimensions are the gauge directions that the Lorentz group does not see.

The boosts are the simplest non-compact elements. On the Krein-orthogonal sum of a positive and a negative line,

$$
T_t e_t=\cosh t\,e_t+\sinh t\,\vec e_x, \qquad
T_t\vec e_x=\sinh t\,e_t+\cosh t\,\vec e_x,
$$

with $T_t=\mathrm{id}$ on the two remaining directions. Each $T_t$ is a Krein isometry, the family is a one-parameter subgroup, and

$$
\operatorname{spec}(T_t)=\{e^{t},e^{-t},1,1\}.
$$

The restriction of $T_t$ to the Minkowski slice $\mathbb{H}_{\mathbb{B}}$ is the Lorentz boost of rapidity $t$ along $\vec e_x$.

The spectrum of a general Krein isometry obeys the inversion symmetry

$$
\lambda\in\operatorname{spec}(T)\iff\frac{1}{\bar\lambda}\in\operatorname{spec}(T),
$$

with multiplicities. The eigenvalues on the unit circle are paired by conjugation and the eigenvalues off it occur in inverted pairs. A Krein isometry is therefore not confined to the unit circle: the boosts leave it, and that is the group-level form of the non-compactness.

The compact algebraic isometries form a small subgroup. The central phases and the sandwiches by the unitary elements generate

$$
\mathrm{U}(1)\times PU(2)\cong\mathrm{U}(1)\times SO(3),
$$

of real dimension $4$. The phases are the scalar isometries; the unitary sandwiches are the inner automorphisms of the algebra; the two families commute and meet only at the identity. The compact subgroup is far from the whole group, whose dimension is $16$. The norm-one sandwiches are isometries too, but they are not inner automorphisms and they form the non-compact proper orthochronous Lorentz group $\mathrm{PSL}(2,\mathbb{C})\cong SO^{+}(1,3)$.

## The Level Sets

The three sign level sets are hyperboloids, not spheres. In the splitting $\tilde Q=c+v$ into the centre and the vector part,

$$
\{\tilde Q:\langle\tilde Q,\tilde Q\rangle_{\natural*}=1\}
=\{(c,v):\lVert c\rVert_E^2=1+\lVert v\rVert_E^2\}\cong S^1\times\mathbb{R}^6,
$$

$$
\{\tilde Q:\langle\tilde Q,\tilde Q\rangle_{\natural*}=-1\}
=\{(c,v):\lVert v\rVert_E^2=1+\lVert c\rVert_E^2\}\cong S^5\times\mathbb{R}^2,
$$

$$
\{\tilde Q:\langle\tilde Q,\tilde Q\rangle_{\natural*}=0\}
=\{(c,v):\lVert c\rVert_E=\lVert v\rVert_E\}\cong S^1\times S^5\times\mathbb{R}_{>0}.
$$

All three have real dimension $7$. The positive set is homotopy equivalent to $S^1$, the negative set to $S^5$, and the null set to $S^1\times S^5$. The positive region $\{\lVert c\rVert_E>\lVert v\rVert_E\}$ retracts onto the circle $c/\lVert c\rVert_E$, and the negative region $\{\lVert v\rVert_E>\lVert c\rVert_E\}$ retracts onto the sphere $v/\lVert v\rVert_E$.

The comparison with the other two families of level sets is sharp.

| Family | Level sets | Real dimension | Compact? |
| --- | --- | --- | --- |
| Biquaternion norm $\langle\tilde Q\rangle_{\natural}=\lambda$ | complex hypersurfaces | $6$ | no |
| Krein form $\langle\tilde Q,\tilde Q\rangle_{\natural*}=t$ | real hyperboloids | $7$ | no |
| Born form $\langle\tilde Q,\tilde Q\rangle_{*}=r^2$ | Euclidean spheres | $7$ | yes |

The norm's levels are complex hypersurfaces, the Krein levels are real hypersurfaces, and only the definite Born levels are compact. The three families are the three geometries of the algebra: the projective geometry of the zero-divisor cone, the hyperbolic geometry of the indefinite form, and the elliptic geometry of the state space.

The phase circle acts freely on the positive level set, and the quotient is the complex hyperbolic space of the next section. The positive level set is a principal $S^1$-bundle over that space, and it is diffeomorphic to $S^1\times\mathbb{R}^6$.

## The Hyperbolic Structure

The positive lines are the lines $\mathbb{C}(e_t+\tilde Q_1)$ with $\lVert\tilde Q_1\rVert_E<1$. The assignment

$$
\tilde Q_1\longmapsto\mathbb{C}(e_t+\tilde Q_1)
$$

is a bijection from the open unit ball of the vector space onto the set of positive lines. That set is the **complex hyperbolic space** $\mathbb{CH}^3$, of real dimension $6$, and it is the homogeneous space

$$
\mathbb{CH}^3\cong\mathrm{U}(1,3)/(\mathrm{U}(1)\times\mathrm{U}(3)).
$$

The boundary is the set of isotropic lines, $\lVert\tilde Q_1\rVert_E=1$, a copy of $S^5$. The ball carries the Bergman metric, which is Kähler, complete, of constant negative holomorphic sectional curvature, and invariant under the isometries of the form; the boundary is at infinite distance. The intersection of the ball with a complex line is a copy of the unit disc, totally geodesic and isometric to $\mathbb{CH}^1$; the real geodesics are the images of the real diameters of these discs under the group.

The Minkowski slice gives the real picture inside the complex one. On the real quaternion space the form is the interval, the ball meets the slice in the real unit ball of $\mathbb{R}^3$, and the Bergman metric restricts to the Poincaré metric of the real hyperbolic space $H^3$. The slice is totally geodesic and totally real. The positive level set on the slice is the two-sheeted hyperboloid, and its sheet $q_t=\sqrt{1+\lVert\vec q\rVert^2}$ is the hyperboloid model of $H^3$.

The geometry is the geometry of the gauge form. A positive line is a time axis; the ball is the space of time axes; the boundary is the set of null directions; a boost is a hyperbolic translation inside the ball; and the Lorentz group of a real slice is the subgroup that preserves that slice. The group $\mathrm{U}(1,3)$ is the full isometry group of the ball, and the Lorentz group is a real section of it.

## The $J$-Contractions

A **$J$-contraction** is a $\mathbb{C}$-linear operator $T$ whose defect $\mathrm{id}-T^{\dagger}T$ lies in the $J$-positive operator cone

$$
\mathcal{P}_J=J\cdot\{S:S\ge0\},
$$

with $\dagger$ the Krein adjoint, $T^{\dagger}=JT^{*}J$.

The contraction is **strict** when the defect is invertible. The model is the Krein-orthogonal projection onto the vector subspace,

$$
\pi_y=\tfrac12(\mathrm{id}-J),
$$

whose defect is the projection onto the centre,

$$
\pi_x=\tfrac12(\mathrm{id}+J).
$$

The projection $\pi_y$ is a $J$-contraction; its defect $\pi_x$ is $J$-positive; and the set of $J$-contractions is invariant under conjugation by Krein isometries. The scalar multiplications are contractions only when they are isometries.

The geometric reading is the ball. The strict $J$-contractions correspond to the interior of the complex hyperbolic ball, and the isometry group acts on its boundary. A contraction inside the ball shrinks the positive part; a gauge transformation on the boundary preserves it. The defect operator measures the shrinking. The reading is geometric and not a dynamics: the algebra supplies the inclusion of the contraction set in the ball and the group that acts on its boundary, and it does not supply a time parameter for the contraction.

The operator cone itself is larger than the set of contractions. It is closed and convex, stable under sums and $J$-adjoints, and it contains $J$ but not the identity. The identity is not $J$-positive, which is the sharp statement that the gauge's positivity is transported by the fundamental symmetry and not by the algebra's unit.

## The Two Cones

The **Krein cone** is the set of non-negative square,

$$
P_K=\{\tilde Q:\langle\tilde Q,\tilde Q\rangle_{\natural*}\ge0\}
=\{\tilde Q:\lVert c\rVert_E\ge\lVert v\rVert_E\}.
$$

It is closed, star-shaped and contractible, but it is neither convex nor pointed: it has two opposite nappes, and the segment between a point and its negative leaves it. Its interior is the positive region, its boundary is the Krein null set, and it contains the whole positive axis and no negative element. On the Hermitian subspace its intersection is the full light cone of the interval form, whose future nappe is the Hermitian cone $P$ of the dagger; on a Minkowski slice the intersection is the full light cone, with no nappe selected by the algebra.

The Krein null set is not the zero-divisor cone. The Krein null set has real dimension $7$; the zero-divisor cone $\{N=0\}$ has real dimension $6$. Neither contains the other. The element $e_t+\vec e_x$ is Krein-null with interval $2$; the element $\vec e_x+i\vec e_y$ has interval $0$ and Krein square $-2$. The two cones meet exactly on the doubly-null lines

$$
\mathbb{C}(e_t\pm i\hat\mu),
$$

with $\hat\mu$ a real unit direction; these are the Peirce lines of the rank-one Hermitian idempotents. On the material sector, where the Krein form is minus the interval, the two null sets coincide with the light cone. The distinction is therefore a property of the complex algebra and not of a sector.

The Krein cone is a cone of indefinite positivity and not a state space. It is not convex, it is not pointed, and it carries no trace. A state space needs the positive definite Born form and the trace-one slice; the Krein cone supplies the sign condition in which the gauge form is read.

## Physical Readings

**The gauge calibration.** The Krein form pairs two frames and returns a real number with a sign. It is positive on the clock direction and negative on the spatial directions, so it ranks nothing and normalises nothing: its value at equal arguments carries a signature, not a weight. The "unit" gauge is a hyperboloid, and a gauge slice is non-compact. The definite companion that carries a weight is the Born form; the two are the invariant pair of the frame.

**The sign is the sector.** On the material sector the form is minus the interval; on the informational sector it is the interval. The metric of matter and the gauge form of the frame are therefore one object read with a sign, and the sign is the whole of their difference. This is the reading that the companion article develops; the geometry here is the same statement in the language of level sets.

**The parity is the fundamental symmetry.** $J={}^{\natural}$ fixes the centre and reverses the vector subspace. It is the frame's own parity, and it is the algebra's own involution, not an extra choice. The indefinite form is the definite form transported by this parity.

**The time axes are the positive lines.** A positive line is a time axis of an observer. The space of time axes is the complex hyperbolic ball; the boundary is the set of null directions; a boost is a hyperbolic translation; the Lorentz group of a real slice is the subgroup that preserves that slice. The reading is kinematic: it identifies the points of the ball with the frames, and it does not give a law of motion inside the ball.

**The level sets are gauge calibrations, not mass shells, in the full algebra.** On the material sector, where the form is minus the interval, the Krein levels are the mass shells up to sign. In the full algebra they are not: the mass shell is a statement about a sector, and the Krein level set is a statement about the frame. Reading a full-algebra level set as a mass shell is the error the distinction prevents.

**The isometry group is the gauge group of the form, not the Lorentz group.** $\mathrm{U}(1,3)$ is the group that preserves the indefinite pairing of frames. The Lorentz group is the subgroup that preserves the material real slice. The gauge reading is a name for the invariance of the form; it is not a derivation of a gauge field.

## Limits

The article states the indefinite structure and no dynamics. It does not derive a gauge field, a connection, a curvature or a field strength; it does not claim that the physical gauge group is $\mathrm{U}(1,3)$; and it does not claim that the hyperbolic geometry is a model of physical space.

The form is a reading. Its sign, its signature and its level sets are properties of the algebra and of the two sectors; the identification of the form with a gauge calibration is the physical hypothesis, stated with the companion article and not proved here.

The Krein cone is not a state space. It is not convex, not pointed and not traced; it carries a sign condition and not a probability. The state space is the positive definite Born form with its trace-one slice.

The level sets are not probability normalisations. They are hyperboloids, non-compact and of real dimension seven; a normalised state needs a compact level set, and only the Born form supplies one.

The isometry group is not the Lorentz group. The Lorentz group is the subgroup that preserves the material real form; the extra dimensions of $\mathrm{U}(1,3)$ are the gauge directions of the form, and their physical status is not settled by the algebra.

## Summary

- The Krein form is the fourth form of the algebra, Hermitian and indefinite, of signature $(1,3)$ over $\mathbb{C}$ and $(2,6)$ over $\mathbb{R}$.
- Its Gram matrix is $E=\operatorname{diag}(1,-1,-1,-1)$; it is positive on the centre, negative on the vector space, and equal to $\pm$ the interval on the two sectors.
- It is real at equal arguments and cannot normalise a state; its unit level set is a non-compact hyperboloid, not a sphere.
- The fundamental symmetry $J={}^{\natural}$ relates it to the definite Born form by $\langle P,Q\rangle_{\natural*}=\langle P,JQ\rangle_{*}$; the indefinite structure is the definite one twisted by $J$.
- The isometry group is $\mathrm{U}(1,3)$, of real dimension $16$, with centre $\mathrm{U}(1)$ and maximal compact $\mathrm{U}(1)\times\mathrm{U}(3)$.
- The boosts are one-parameter subgroups with spectrum $\{e^{t},e^{-t},1,1\}$; the spectrum of a general Krein isometry is invariant under $\lambda\mapsto1/\bar\lambda$.
- The compact algebraic isometries form $\mathrm{U}(1)\times PU(2)\cong\mathrm{U}(1)\times SO(3)$, of dimension $4$; the norm-one sandwiches form the non-compact proper orthochronous Lorentz group.
- The level sets are $S^1\times\mathbb{R}^6$, $S^5\times\mathbb{R}^2$ and $S^1\times S^5\times\mathbb{R}_{>0}$, all of real dimension $7$.
- The positive lines form the complex hyperbolic ball $\mathbb{CH}^3=\mathrm{U}(1,3)/(\mathrm{U}(1)\times\mathrm{U}(3))$, with boundary $S^5$; the Minkowski slice gives the real hyperbolic space $H^3$.
- The $J$-contractions are the interior of the ball, and the isometry group acts on its boundary; the model contraction is $\pi_y=\tfrac12(\mathrm{id}-J)$ with defect $\pi_x$.
- The Krein cone is closed and star-shaped but neither convex nor pointed; it is an indefinite positivity cone, not a state space.
- The Krein null set (dimension $7$) and the zero-divisor cone (dimension $6$) are different; they meet on the doubly-null lines $\mathbb{C}(e_t\pm i\hat\mu)$.
- The Lorentz group is the subgroup of $\mathrm{U}(1,3)$ that preserves the material real slice; the gauge group of the form is the whole $\mathrm{U}(1,3)$.
- The form is a reading and no gauge field is derived; the hyperbolic geometry is kinematic and no dynamics is supplied.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\langle\tilde P,\tilde Q\rangle_{\natural*}=\sum_\mu\varepsilon_\mu P_\mu\overline{Q_\mu}$ | the Krein form, the gauge form |
| $E=\operatorname{diag}(1,-1,-1,-1)$ | its Gram matrix in the coefficient basis |
| $\lVert\cdot\rVert_E$ | the Euclidean norm of the coefficient vector |
| $\varepsilon=(1,-1,-1,-1)$ | the sign vector, the gauge inside the product |
| $J={}^{\natural}$ | the fundamental symmetry, $J^2=\mathrm{id}$ |
| $T^{\dagger}=JT^{*}J$ | the Krein adjoint |
| $\langle\tilde P,\tilde Q\rangle_{\natural*}=\langle\tilde P,J\tilde Q\rangle_{*}$ | the bridge to the definite Born form |
| $\mathrm{U}(1,3)$ | the Krein isometry group |
| $T_t$ | the boost of parameter $t$ |
| $\mathbb{CH}^3$ | the complex hyperbolic space of positive lines |
| $H^3$ | the real hyperbolic space of the Minkowski slice |
| $P_K=\{\lVert c\rVert_E\ge\lVert v\rVert_E\}$ | the Krein cone |
| $\mathcal{K}=\{\lVert c\rVert_E=\lVert v\rVert_E\}$ | the Krein null set |
| $\mathbb{C}(e_t\pm i\hat\mu)$ | the doubly-null lines |
| $\mathcal{P}_J=J\cdot\{S\ge0\}$ | the $J$-positive operator cone |
| $\pi_x=\tfrac12(\mathrm{id}+J)$, $\pi_y=\tfrac12(\mathrm{id}-J)$ | the projections onto the centre and the vector space |
| $\mathbb{M}_\pm$ | the informational and material sectors |

## Further Reading

- [The Krein Form as a Product on the Symmetric Quaternionic Sesqualgebra](../articles_maths/the-krein-form-as-a-product-on-the-symmetric-quaternionic-sesqualgebra.html), for the form as a product and its Hermitian character.
- [The Krein Gram Matrix and the Restrictions of the Form](../articles_maths/the-krein-gram-matrix-and-the-restrictions-of-the-form.html), for the Gram matrix and the six restrictions.
- [The Krein Isometry Group and Its $J$-Contractions](../articles_maths/the-krein-isometry-group-and-its-j-contractions.html), for the group, the boosts and the contractions.
- [The Krein Level Sets and the Hyperbolic Structure](../articles_maths/the-krein-level-sets-and-the-hyperbolic-structure.html), for the level sets, the ball and the two hyperbolic models.
- [Indefinite Positivity and the Krein Cone of the Biquaternion Algebra](../articles_maths/indefinite-positivity-and-the-krein-cone-of-the-biquaternion-algebra.html), for the cone and the operator cone.
- [The Isotropic Structure of the General Quaternionic Sesqualgebra](../articles_maths/the-isotropic-structure-of-the-general-quaternionic-sesqualgebra.html), for the null set and the doubly-null lines.
- *The Four Forms and the Four Algebraic Norms*, for the place of the Krein form among the four forms.
- *The Operators: One-Sided, Two-Sided, Sandwich*, for the one-sided and two-sided operators of the form.
- *The Polar Representation and Its Three Pairings*, for the factors that the isometries act on.
