
# __Split-Quaternion Rotations and the Lorentz Group__

## Introduction

This article studies the action of the unit split-quaternions on the vector subspace. It identifies the unit groups, computes the adjoint action, proves the double cover $\mathrm{SL}_2(\mathbb{R}) \to \mathrm{SO}^{+}(2,1)$ of the Lorentz group of signature $(2,1)$, describes the elliptic and hyperbolic one-parameter subgroups, and classifies the elements of the vector subspace as timelike, lightlike or spacelike according to their orbits.

The split-quaternion algebra, its vector subspace $V$, its norm form $N$, its conjugation and its idempotents are assumed from *Split-Quaternion Algebra*; the group of units, the norm-one group and the signature of the restricted form are assumed from *Split-Quaternion Norm and Invertibility*. The defining module and the matrix model are assumed from *Split-Quaternion Matrix Representations*, and the representations of the algebra from *Split-Quaternion Representations*. The Lorentz groups and the orthogonal groups are those of *The Orthogonal Lie Algebra* and *Isometries and Orthogonal Transformations*; the hyperbolic plane that the sheets carry is the subject of *Split-Quaternions and Hyperbolic Geometry*, to which the last step of this article points. Nothing physical is invoked.

## The Unit Split-Quaternions

**Definition.** The **norm-one group** of the algebra is

$$
U = \{x \in \mathbb{H}_{\mathrm{s}} : N(x) = 1\},
$$

and the set of elements of norm $\pm 1$ is

$$
U^{\pm} = \{x \in \mathbb{H}_{\mathrm{s}} : N(x) = \pm 1\} = \mathrm{SL}_2^{\pm}(\mathbb{R}).
$$

Both are groups under multiplication, and $U$ is a subgroup of $U^{\pm}$.

**Theorem (The Two Components).** The group $U$ is isomorphic to $\mathrm{SL}_2(\mathbb{R})$ and is connected; the group $U^{\pm}$ has exactly two connected components,

$$
U = \mathrm{SL}_2(\mathbb{R}) \quad \text{and} \quad \{x : N(x) = -1\} = \mathrm{SL}_2^{-}(\mathbb{R}),
$$

and the two components are interchanged by multiplication by $e_2$. The full group of units is

$$
\mathbb{H}_{\mathrm{s}}^{\times} = \{N \neq 0\} \cong GL_2(\mathbb{R}),
$$

its centre is $\mathbb{R}^{\times}$, and it has the two components $\{N > 0\} = GL_2^{+}(\mathbb{R})$ and $\{N < 0\} = GL_2^{-}(\mathbb{R})$.

**Proof.** The identification $U \cong \mathrm{SL}_2(\mathbb{R})$ and the isomorphism $\mathbb{H}_{\mathrm{s}}^{\times} \cong GL_2(\mathbb{R})$ are (*Split-Quaternion Norm and Invertibility*, §*The Group of Units*), where the connectedness of $\mathrm{SL}_2(\mathbb{R})$ and the splitting of the units into the two components $\{N>0\}$, $\{N<0\}$ are recorded. The element $e_2$ has $N(e_2) = -1$ and $e_2^{-1} = e_2$, so multiplication by $e_2$ exchanges the two norm levels; it therefore identifies the two components of $U^{\pm}$, and since $U$ is connected, $U^{\pm}$ has exactly two components. The centre is $\mathbb{R}$ by (*Split-Quaternion Algebra*, §*The Centre and Simplicity*), so the central units are the nonzero scalars. $\square$

**Remark (Two readings of "the unit split-quaternions").** The norm-one group $U$ is connected and has no two-component structure; the two components appear for the group $U^{\pm}$ of units of norm $\pm 1$. Both readings occur in the literature, and this article keeps them apart: the double cover below is a statement about $U = \mathrm{SL}_2(\mathbb{R})$, and the second component of $U^{\pm}$ is reached by $e_2$ and acts by isometries reversing the time direction.

## The Adjoint Action on the Vector Subspace

For a unit $u$ define the conjugation map

$$
\Theta(u) : V \to V, \qquad \Theta(u)v = u v u^{-1}.
$$

**Theorem (The Adjoint Representation).** For every unit $u$, the map $\Theta(u)$ is a real-linear automorphism of $V$ preserving the form $N$; the assignment $u \mapsto \Theta(u)$ is a group homomorphism

$$
\Theta : \mathbb{H}_{\mathrm{s}}^{\times} \longrightarrow O(V, N) \cong O(2,1),
$$

whose kernel is the centre $\mathbb{R}^{\times}$ and whose image lies in $SO(2,1)$. On the norm-one group the restriction

$$
\Theta : U \cong \mathrm{SL}_2(\mathbb{R}) \longrightarrow \mathrm{SO}^{+}(2,1)
$$

has kernel $\{\pm 1\}$.

**Proof.** *The maps land in $V$.* Conjugation by $u$ is an algebra automorphism, and it commutes with the conjugation, since $\overline{uvu^{-1}} = \bar{u}\,\bar{v}\,\bar{u}^{-1}$ and $\overline{u^{-1}} = \bar{u}^{-1}$. The vector subspace is the $-1$ eigenspace of the conjugation by (*Split-Quaternion Algebra*, §*The Two Eigenspaces*), so it is mapped to itself. *The form is preserved.* $N(uvu^{-1}) = N(u)N(v)N(u)^{-1} = N(v)$ by multiplicativity, since $N$ is real and nonzero on a unit. Hence $\Theta(u) \in O(V,N)$. *Kernel.* If $\Theta(u) = \mathrm{id}$ then $u$ commutes with every element of $V$; since $1$ and $V$ generate the algebra, $u$ is central, so $u \in \mathbb{R}^{\times}$. Conversely every nonzero scalar is in the kernel. *Determinant.* The map $\det\circ\,\Theta : \mathbb{H}_{\mathrm{s}}^{\times} \to \{\pm 1\}$ is a continuous homomorphism. Its domain has the two components $\{N>0\}$ and $\{N<0\}$; the first is $GL_2^{+}(\mathbb{R})$, which is connected, so $\det\Theta \equiv 1$ there. On the second component, $\Phi(e_2) = K$ is a reflection, and the computation of (*Split-Quaternion Algebra*, §*The Multiplication Table*) gives $e_2e_1e_2 = -e_1$, $e_2e_2e_2 = e_2$, $e_2e_3e_2 = -e_3$, so $\Theta(e_2) = \operatorname{diag}(-1,1,-1)$ in the basis $e_1,e_2,e_3$ and $\det\Theta(e_2) = +1$. Hence $\det\Theta \equiv 1$ and the image lies in $SO(2,1)$. *The restricted kernel.* The kernel on $U$ is the centre intersected with $\{N=1\}$, that is $\{\pm 1\}$. $\square$

**Corollary (The Image of the Unit Group).** The image of the full unit group is

$$
\Theta(\mathbb{H}_{\mathrm{s}}^{\times}) = SO(2,1) \cong PGL_2(\mathbb{R}),
$$

and the image of the norm-one group is $\Theta(U) = SO^{+}(2,1)$, the identity component.

**Proof.** The image of $\mathbb{H}_{\mathrm{s}}^{\times}$ is a subgroup of $SO(2,1)$ containing the image of the connected group $U$, which is connected and contains the identity, so the image contains the identity component; the domain has exactly two components and the image lies in $SO(2,1)$, which has two components, so the image is all of $SO(2,1)$. The second statement is proved below, where $\Theta(U)$ is identified with $\mathrm{SO}^{+}(2,1)$ through the double cover. $\square$

## The Double Cover of $\mathrm{SO}^{+}(2,1)$

**Theorem (The Double Cover).** The adjoint action restricted to the norm-one group is a surjective group homomorphism

$$
\Theta : \mathrm{SL}_2(\mathbb{R}) \longrightarrow \mathrm{SO}^{+}(2,1)
$$

with kernel $\{\pm 1\}$. It is therefore a double cover, and it induces an isomorphism

$$
\mathrm{SL}_2(\mathbb{R})/\{\pm 1\} = \mathrm{PSL}_2(\mathbb{R}) \cong \mathrm{SO}^{+}(2,1).
$$

**Proof.** By the preceding theorem the homomorphism is well defined and has kernel $\{\pm 1\}$. Its differential at the identity is the representation of the Lie algebra $\mathfrak{sl}_2(\mathbb{R}) = V$ with the commutator bracket (by *Split-Quaternion Algebra*, §*The Lie Algebra Structure*) on the Lie algebra $\mathfrak{so}(2,1)$ of the isometry algebra of the signature-$(2,1)$ form; it is injective because the kernel of $\Theta$ is discrete, and both Lie algebras have dimension $3$, so the differential is an isomorphism, by *The Orthogonal Lie Algebra*, §*The Lie Algebra of Skew Transformations*. The image of a Lie group homomorphism with injective differential is an open Lie subgroup of the target; since the target $\mathrm{SO}^{+}(2,1)$ is connected, an open subgroup containing the identity is the whole group, by *The Lie Correspondence and the Adjoint Representation*. Hence $\Theta$ is surjective, and the first isomorphism theorem for groups gives $\mathrm{SL}_2(\mathbb{R})/\{\pm 1\} \cong \mathrm{SO}^{+}(2,1)$. $\square$

**Corollary (A Double Cover That Is Not the Universal Cover).** The group $\mathrm{SL}_2(\mathbb{R})$ is connected but not simply connected: its fundamental group is infinite cyclic. The double cover of the theorem is therefore not the universal cover of $\mathrm{SO}^{+}(2,1)$; the universal cover is the infinite cyclic cover of $\mathrm{SL}_2(\mathbb{R})$, and the intermediate cover of degree two is the object of the theorem.

**Proof.** The fundamental group of $\mathrm{SL}_2(\mathbb{R})$ is computed in *Matrix Groups and Classical Groups*, where the maximal compact subgroup $SO(2)$ is seen to generate the fundamental group; the covering theory gives the rest. $\square$

This is a structural difference from the quaternion case and it is worth naming: the quaternion unit sphere is the three-sphere, which is simply connected, so there the double cover of $SO(3)$ is the universal cover, whereas here the double cover of $\mathrm{SO}^{+}(2,1)$ sits under an infinite tower.

**Corollary (Fixed Directions).** A non-identity elliptic isometry $\Theta(g(\theta))$ fixes the positive-norm direction $\mathbb{R}\xi$ and no other direction of $V$; a non-identity hyperbolic isometry $\Theta(h(t))$ fixes the negative-norm direction $\mathbb{R}\eta$ and the two isotropic directions of the plane $\eta^{\perp}$. Neither fixes any other direction.

**Proof.** The fixed directions of the first two kinds are computed in the two theorems below. An isometry of $V$ with three fixed directions in general position is the identity, because the form is nondegenerate and such directions span $V$; a nontrivial elliptic isometry acts on the definite plane $\xi^{\perp}$ as a rotation by the nonzero angle $2\theta$, so it fixes no direction there, and a nontrivial hyperbolic isometry acts on the indefinite plane $\eta^{\perp}$ as a hyperbolic rotation, which is the identity only for $t = 0$. $\square$

## The Lorentz Group of Signature $(2,1)$

**Definition.** The **Lorentz group of signature $(2,1)$** is the isometry group $O(V,N) \cong O(2,1)$ of the form $N = b^2 - c^2 - d^2$ on the three-dimensional vector subspace; its **identity component** is $\mathrm{SO}^{+}(2,1)$, the group of isometries of determinant $+1$ preserving the time orientation.

**Theorem (The Structure of the Group).** The group $O(2,1)$ has four connected components, distinguished by the signs of $\det$ and of the coordinate $b$ of a timelike vector; the subgroup $SO(2,1)$ of determinant $+1$ has two components, and its identity component is $\mathrm{SO}^{+}(2,1)$, a three-dimensional group isomorphic to $\mathrm{PSL}_2(\mathbb{R})$. The full group of units of the algebra maps onto $SO(2,1)$ with kernel $\mathbb{R}^{\times}$, and the norm-one group maps onto $\mathrm{SO}^{+}(2,1)$ with kernel $\{\pm 1\}$.

**Proof.** The components of $O(2,1)$ are described in *Isometries and Orthogonal Transformations*; the isomorphism $\mathrm{PSL}_2(\mathbb{R}) \cong \mathrm{SO}^{+}(2,1)$ is the double cover of the preceding section, and the statement about the images and kernels is the theorem on the adjoint representation and its corollary. $\square$

**Remark (Signature $(2,1)$, not $(3,1)$).** The form restricted to the vector subspace has signature $(2,1)$ by (*Split-Quaternion Algebra*, §*The Restricted Form on the Vector Subspace*), and the group acting on the vector subspace is therefore the three-dimensional Lorentz group $\mathrm{SO}^{+}(2,1)$. The group $\mathrm{SO}^{+}(3,1)$ is the Lorentz group of four-dimensional Minkowski space and does not occur here; the split-quaternion system carries three-dimensional Lorentzian geometry and the hyperbolic plane, not four-dimensional geometry and hyperbolic three-space.

## Elliptic and Hyperbolic One-Parameter Subgroups

The solutions of $\xi^2 = -1$ and of $\eta^2 = +1$ generate the two kinds of one-parameter subgroup of $U$.

**Theorem (Elliptic Subgroups).** Let $\xi \in V$ with $\xi^2 = -1$. Then the elements

$$
g(\theta) = \cos\theta + \xi \sin\theta, \qquad \theta \in \mathbb{R},
$$

form a subgroup of $U$ isomorphic to $SO(2)$, and

$$
\Theta(g(\theta)) \xi = \xi, \qquad \Theta(g(\theta)) : \xi^{\perp} \to \xi^{\perp} \text{ is a rotation by } 2\theta .
$$

The subgroups obtained from the solutions of $\xi^2 = -1$ are the compact subgroups of $U$, and they exhaust the conjugacy classes of maximal compact subgroups.

**Proof.** The norm is $N(g(\theta)) = \cos^2\theta \cdot 1 + \sin^2\theta \cdot N(\xi) = \cos^2\theta + \sin^2\theta = 1$, using $\xi^2 = -N(\xi) = -1$; the addition formula for $g$ follows from $\xi^2 = -1$. The element $g$ commutes with $\xi$, so $\xi$ is fixed; and $\xi^{\perp}$ is the orthogonal plane of dimension two, which is definite because $\xi$ has positive norm, so that conjugation by $g$ acts on it as a rotation; the explicit computation with $\xi = e_1$ in the basis $e_2,e_3$ gives $\Theta(g(\theta))e_2 = \cos 2\theta\, e_2 + \sin 2\theta\, e_3$ and $\Theta(g(\theta))e_3 = -\sin 2\theta\, e_2 + \cos 2\theta\, e_3$, a rotation by $2\theta$, as in the quaternion case of *Quaternion Algebra*, §*The Rotation Group*. $\square$

**Theorem (Hyperbolic Subgroups).** Let $\eta \in V$ with $\eta^2 = +1$, that is $N(\eta) = -1$. Then the elements

$$
h(t) = \cosh t + \eta \sinh t, \qquad t \in \mathbb{R},
$$

form a subgroup of $U$ isomorphic to $\mathbb{R}$, and

$$
\Theta(h(t)) \eta = \eta, \qquad \Theta(h(t)) : \eta^{\perp} \to \eta^{\perp}
$$

acts on the plane $\eta^{\perp}$ of signature $(1,1)$ as a hyperbolic rotation with parameter $2t$: it fixes the two isotropic lines of that plane setwise and translates along the hyperbolas $N = \text{constant}$.

**Proof.** The norm is $N(h(t)) = \cosh^2 t + \sinh^2 t \cdot 1 = \cosh^2 t - \sinh^2 t = 1$, using $N(\eta) = -1$; the addition formula follows from $\eta^2 = 1$. The element $h(t)$ commutes with $\eta$, so $\eta$ is fixed; the orthogonal plane $\eta^{\perp}$ has signature $(1,1)$ because $\eta$ is spacelike, and an isometry of a $(1,1)$ plane with a fixed nonzero vector acts as a hyperbolic rotation, fixing the two isotropic directions setwise. $\square$

**Corollary (The Trichotomy of Subgroups).** The subgroup generated by a solution of $\xi^2 = -1$ is compact and consists of elements without real eigenvalues; the subgroup generated by a solution of $\eta^2 = +1$ is non-compact and its non-identity elements have the two real eigenvalues $e^{\pm t}$ of the isometry. The three families correspond to the three conjugacy classes of one-parameter subgroups of $U$: the elliptic class, the hyperbolic class, and the parabolic class, the last consisting of the subgroups generated by the nilpotents of $V$ and acting by parabolic isometries fixing a single isotropic line.

**Proof.** The first two statements are the computations of the two theorems; the parabolic case uses the nilpotents of (*Split-Quaternion Zero Divisors*, §*Nonzero Nilpotents*), whose exponentials are the elements $1 + t\xi$ with $\xi^2 = 0$ and $N(\xi) = 0$. $\square$

## The Trichotomy of Timelike, Lightlike and Spacelike Elements

The form $N$ is isotropic, so the trichotomy is real: all three classes are nonempty, unlike in the quaternion case, where the form is definite and only the analogue of the timelike class occurs.

**Definition.** A nonzero element $v \in V$ is **timelike** when $N(v) > 0$, **lightlike** when $N(v) = 0$, and **spacelike** when $N(v) < 0$. The lightlike elements are the nilpotents of (*Split-Quaternion Zero Divisors*, §*Nonzero Nilpotents*).

**Theorem (The Orbits).** The action of $\mathrm{SO}^{+}(2,1)$ on $V$ has the following orbits.

| Orbit | Criterion | Structure |
|---|---|---|
| $\{0\}$ | $v = 0$ | one point |
| two timelike orbits | $N(v) = 1$, the two sheets $b \geq 1$ and $b \leq -1$ | each a copy of the hyperbolic plane |
| two lightlike orbits | $v \neq 0$, $N(v) = 0$ | the two nappes of the cone, each a homogeneous space of dimension $2$ |
| one spacelike orbit | $N(v) = -1$ | the one-sheeted hyperboloid, a homogeneous space of dimension $2$ |

Each nontrivial orbit is a level set of $N$ scaled to $\pm 1$ or $0$, and the stabiliser of a timelike point is a copy of $SO(2)$, the stabiliser of a spacelike point is a copy of $SO(1,1) \cong \mathbb{R}$, and the stabiliser of a lightlike point is the one-parameter unipotent group of null transvections, isomorphic to $\mathbb{R}$.

**Proof.** The form and its action are those of the preceding sections; the level sets are invariant because $\Theta$ preserves $N$, and transitivity on each level set is the standard transitivity of the Lorentz group on each hyperboloid, proved in *Isometries and Orthogonal Transformations*, together with the orbit–stabiliser theorem. The stabiliser of a timelike vector is the group of isometries of the positive-definite orthogonal complement, namely $SO(2)$; that of a spacelike vector is the group of isometries of the signature-$(1,1)$ complement, namely $SO(1,1)$; and that of a lightlike vector preserves the radical $\mathbb{R}v$ of the orthogonal complement and acts trivially on the one-dimensional quotient $v^{\perp}/\mathbb{R}v$, so that its Lie algebra is the line $\{X \in \mathfrak{so}(2,1) : Xv = 0\}$, of dimension one: every orbit in the table is two-dimensional and the group is three-dimensional, so every stabiliser is one-dimensional, the three of them being $SO(2)$, $SO(1,1)$ and the unipotent group. (The stabiliser of a lightlike *direction*, which is a point of the boundary of the hyperbolic plane rather than a vector of the cone, is the larger two-dimensional solvable group, the affine group of the line.) $\square$

**Corollary (The Two Sheets and the Hyperbolic Plane).** Each sheet of $N = 1$ is a copy of the hyperbolic plane, and the identity component of its isometry group is $\mathrm{SO}^{+}(2,1) \cong \mathrm{PSL}_2(\mathbb{R})$. The model is built on the split-quaternions in *Split-Quaternions and Hyperbolic Geometry*, which carries the geometry; the present article supplies the group action, not the model.

**Proof.** The orbit of a timelike unit vector is $\mathrm{SO}^{+}(2,1)/SO(2)$, and this quotient is a model of the hyperbolic plane by *Hyperbolic Geometry*; the identification of the sheets with the hyperboloid model is (*Split-Quaternion Norm and Invertibility*, §*Isotropy*) combined with the transitivity above. $\square$

**Corollary (The Sign of the Norm and the Fixed Vectors).** An isometry $\Theta(g)$ with a nonzero fixed vector of $V$ has that vector timelike, lightlike or spacelike according to its type: elliptic isometries fix a timelike vector if they are non-trivial, hyperbolic isometries fix a spacelike vector and the two lightlike directions of its orthogonal plane, and parabolic isometries fix a unique lightlike line and no other direction.

**Proof.** The fixed vectors of $g$ are the eigenvectors of $g$ in $V$, and the stated eigenvectors are those computed in the three cases of the one-parameter subgroups. $\square$

## Comparison with the Quaternion and Split-Biquaternion Cases

### The Quaternion Case

| | $\mathbb{H}$ | $\mathbb{H}_{\mathrm{s}}$ |
|---|---|---|
| unit group | $Sp(1) \cong S^3$, compact, simply connected | $\mathrm{SL}_2(\mathbb{R})$, non-compact, not simply connected |
| norm levels | $N = 1$ only | $N = \pm 1$, two components |
| isometry group produced | $SO(3)$, by the adjoint action on $\operatorname{Im}\mathbb{H}$ | $\mathrm{SO}^{+}(2,1)$, by the adjoint action on $V$ |
| cover | universal double cover | double cover, not universal |
| form on the vector part | definite, signature $(3,0)$ | isotropic, signature $(2,1)$ |
| trichotomy | only one class, all nonzero vectors equivalent | timelike, lightlike, spacelike, all nonempty |

The quaternion column is the classical description of the unit quaternions as the double cover of the rotation group, recorded in *Quaternion Algebra*, §*The Rotation Group*, and in *Quaternion Rotations and Reflections*. The single structural cause of every difference is the sign pattern: a definite form gives a compact sphere and one class of vectors, an isotropic form gives a non-compact hyperboloid and the full trichotomy.

### The Split-Biquaternion Case

The eight-dimensional algebra $\mathbb{H}_{\mathbb{D}}$ of the notation table is a later system of Part V, treated under Split-Biquaternions, and nothing of it is used here. The one thing worth stating from the conventions is a warning about size: the present article's isometry group is the three-dimensional $\mathrm{SO}^{+}(2,1)$ acting on the three-dimensional vector subspace of a four-dimensional algebra, and the eight-dimensional relative is a different system with its own, larger, geometry, treated later. The name *split quaternions* belongs to the four-dimensional algebra of this category and not to $\mathbb{H}_{\mathbb{D}}$.

## Summary

The norm-one group of the split-quaternion algebra is $U \cong \mathrm{SL}_2(\mathbb{R})$, connected; the group of units of norm $\pm 1$ is $\mathrm{SL}_2^{\pm}(\mathbb{R})$, with the two components $U$ and the norm $-1$ component interchanged by $e_2$; and the full group of units is $GL_2(\mathbb{R})$ with centre $\mathbb{R}^{\times}$.

Conjugation by a unit preserves the vector subspace and the form, giving a homomorphism from the group of units onto $SO(2,1) \cong PGL_2(\mathbb{R})$ with kernel $\mathbb{R}^{\times}$, and a homomorphism $\mathrm{SL}_2(\mathbb{R}) \to \mathrm{SO}^{+}(2,1)$ with kernel $\{\pm 1\}$, hence a double cover and an isomorphism $\mathrm{PSL}_2(\mathbb{R}) \cong \mathrm{SO}^{+}(2,1)$. The double cover is not the universal cover, because $\mathrm{SL}_2(\mathbb{R})$ has infinite cyclic fundamental group. The Lorentz group of the system is the three-dimensional $\mathrm{SO}^{+}(2,1)$, the group of the signature-$(2,1)$ form, and not $\mathrm{SO}^{+}(3,1)$.

The roots of $\xi^2 = -1$ generate the compact (elliptic) one-parameter subgroups, isomorphic to $SO(2)$ and fixing a timelike direction and rotating its orthogonal plane; the roots of $\eta^2 = +1$ generate the non-compact (hyperbolic) subgroups, fixing a spacelike direction and acting as hyperbolic rotations on its orthogonal plane of signature $(1,1)$; the nilpotents generate the parabolic subgroups. The nonzero vectors of the vector subspace fall into two timelike orbits (the sheets of the hyperboloid $N=1$, each a hyperbolic plane), two lightlike orbits (the nappes of the cone) and one spacelike orbit, with the trichotomy nonempty because the form is isotropic. The quaternion case has a compact simply connected unit sphere, a universal double cover of $SO(3)$, a definite vector form and a single class of vectors; the eight-dimensional relative is a later system of Part V, named here only.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $U = \{N=1\}$ | the norm-one group, $\cong \mathrm{SL}_2(\mathbb{R})$ | *Split-Quaternion Norm and Invertibility* |
| $U^{\pm} = \{N = \pm 1\}$ | $\mathrm{SL}_2^{\pm}(\mathbb{R})$, two components | this article |
| $\mathbb{H}_{\mathrm{s}}^{\times} \cong GL_2(\mathbb{R})$ | the group of units | *Split-Quaternion Norm and Invertibility* |
| $\Theta(u)v = uvu^{-1}$ | the adjoint action on $V$ | this article |
| $(V,N) \cong \mathbb{R}^{2,1}$ | the vector subspace with its signature-$(2,1)$ form | *Split-Quaternion Algebra* |
| $O(2,1)$, $SO(2,1)$, $\mathrm{SO}^{+}(2,1)$ | the Lorentz group, its determinant-one part, its identity component | this article |
| $\mathrm{SL}_2(\mathbb{R}) \to \mathrm{SO}^{+}(2,1)$ | the double cover | this article |
| $\mathrm{PSL}_2(\mathbb{R}) \cong \mathrm{SO}^{+}(2,1)$ | the isomorphism induced by the cover | this article |
| $g(\theta) = \cos\theta + \xi\sin\theta$ | the elliptic one-parameter subgroup | this article |
| $h(t) = \cosh t + \eta\sinh t$ | the hyperbolic one-parameter subgroup | this article |
| timelike, lightlike, spacelike | $N>0$, $N=0$, $N<0$ on $V$ | this article |
| nilpotents of $V$ | the lightlike elements and the parabolic generators | *Split-Quaternion Zero Divisors* |

## Further Reading

- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the adjoint action of a Clifford group on the vector space and the classical identifications of the low-dimensional orthogonal groups.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd ed. (Cambridge University Press, 2001), for the split quaternions as the even Clifford algebra $\mathrm{Cl}_{1,1}^{0}$ and their rotation and boost interpretation.
- John Stillwell, *Naive Lie Theory* (Springer, 2008), for the one-parameter subgroups, the exponential map and the relation between $\mathrm{SL}_2(\mathbb{R})$ and $\mathrm{SO}^{+}(2,1)$.
- Serge Lang, *$\mathrm{SL}_2(\mathbb{R})$* (Addison-Wesley, 1975), for the covering groups of $\mathrm{SL}_2(\mathbb{R})$ and the elliptic, hyperbolic and parabolic classifications.
