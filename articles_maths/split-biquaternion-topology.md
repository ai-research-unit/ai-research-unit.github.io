
# __Split-Biquaternion Topology__

## Introduction

The split biquaternion algebra is, as a topological space, a copy of $\mathbb{R}^8$, and the interesting topological objects attached to it are the unit sphere, the null cone of the Hermitian form together with its link, the group of units, and the failure surface of the polar decomposition. This article records the topology of these spaces and compares it with the biquaternion case. The algebra and its forms are used from *Split-Biquaternion Algebra* and *Split-Biquaternion Norm and Invertibility*; the Hermitian form and the Lorentzian structure are treated in *Split-Biquaternion Rotations and the Lorentz Group*; the group of units is described in *Split-Biquaternion Exponential and Lie Group Structure*.

The treatment is purely mathematical. No physics is invoked; "null cone" names the zero set of a quadratic form, and "link" names the intersection with a sphere.

## The Underlying Space and Its Contractibility

**Proposition.** As a real vector space $\mathbb{H}_{\mathbb{D}} \cong \mathbb{R}^8$, the algebra is contractible, and the punctured algebra $\mathbb{H}_{\mathbb{D}} \setminus \{0\}$ is homotopy equivalent to the seven-sphere $S^7$.

**Proof.** The algebra is a real vector space of dimension $8$; a vector space is contractible, and removing a point from $\mathbb{R}^n$ gives a space homotopy equivalent to $S^{n-1}$, here $S^7$.

The **Euclidean norm** of an element is the positive square root of the real part of its split-biquaternion norm,

$$
\|\tilde{Q}\| = \left(\sum_\mu (q_\mu^2 + q'^2_\mu)\right)^{1/2} = \left(\mathrm{Re}\,N(\tilde{Q})\right)^{1/2} ,
$$

and it is a genuine norm: it is positive definite because the real part of $N$ is a sum of squares. The algebra is thus a Euclidean space of dimension $8$, and all the polar and homotopy statements below use this norm.

## The Euclidean Unit Sphere

**Definition.** The **unit sphere** of the algebra is $S_{\mathbb{E}} = \{\tilde{Q} : \|\tilde{Q}\| = 1\} \cong S^7$.

**Proposition.** The unit sphere of the algebra is a seven-sphere, and the map $\tilde{Q} \mapsto \tilde{Q}/\|\tilde{Q}\|$ is a deformation retraction of $\mathbb{H}_{\mathbb{D}}\setminus\{0\}$ onto it.

**Proof.** The equation $\mathrm{Re}\,N(\tilde{Q}) = 1$ is the equation of the unit sphere in $\mathbb{R}^8$, and radial normalisation is the standard retraction.

The unit sphere of the Euclidean norm is **not** the norm-one group: the norm-one group is cut out by the split complex norm $N = e_0$, not by its real part, and it has dimension $6$ rather than $7$. The two agree only on the quaternion subspace, where the split complex part of $N$ vanishes; this is the first topological distinction between the split biquaternion and the biquaternion case, where the norm-one slice is the complex quadric in $\mathbb{C}^4$.

## The Null Cone

**Definition.** The **null cone** of the algebra is the zero set of the Hermitian form of scalar part $g(\tilde{Q}) = \sum_\mu (q_\mu^2 - q'^2_\mu)$:

$$
C = \left\{ \tilde{Q} \in \mathbb{H}_{\mathbb{D}} : g(\tilde{Q}) = 0 \right\} , \qquad g(\tilde{Q}) = 0 \iff \sum_\mu q_\mu^2 = \sum_\mu q'^2_\mu .
$$

**Proposition.** The null cone $C$ is a closed cone of dimension $7$ through the origin, connected when the origin is removed, and the split-biquaternion norm $N$ vanishes on no point of $C$ except the origin.

**Proof.** The equation is homogeneous of degree two, so $C$ is a cone; its real dimension is $7$ because the gradient of $g$ is nonzero away from the origin. Removing the origin leaves the connected surface $\|q\| = \|q'\| > 0$, the product of the two spheres with their common radius; the two equal-norm conditions do not separate it into components. The split-biquaternion norm has $\mathrm{Re}\,N(\tilde{Q}) = \|q\|^2 + \|q'\|^2 > 0$ off the origin, so $N$ never vanishes there.

**Remark.** The null cone of the Hermitian form is strictly larger than the zero divisor set. Every zero divisor is isotropic for $g$ (this is a statement of *Split-Biquaternion Rotations and the Lorentz Group*), but the converse fails: the element $e_1 + je_0$ is null for $g$ and is not a zero divisor, since its split-biquaternion norm is a unit of $\mathbb{D}$. The zero divisors form the union of the two four-dimensional ideals, a proper subset of the cone.

## The Link of the Null Cone

**Definition.** The **link** of the null cone is its intersection with the Euclidean unit sphere, $L = C \cap S_{\mathbb{E}}$.

**Theorem.** The link of the null cone is homeomorphic to $S^3 \times S^3$.

**Proof.** On the unit sphere $\|q\|^2 + \|q'\|^2 = 1$ the extra equation $\|q\|^2 = \|q'\|^2$ gives $\|q\| = \|q'\| = 1/\sqrt{2}$. So $L$ is the set of pairs of four-vectors of fixed length $1/\sqrt2$, that is $S^3 \times S^3$.

The link of the null cone is thus the same manifold as the norm-one group $S^3 \times S^3 = \mathrm{Spin}(4)$, and the coincidence is structural: both are the twofold product of a three-sphere by itself, one cut out by the Hermitian form on the unit sphere and the other by the split complex norm on the whole algebra. The link is connected, simply connected, and has the homology of $S^3\times S^3$, with nonzero Betti numbers in degrees $0,3,3,6$.

## The Group of Units and Its Homotopy

**Theorem.** The group of units is $\mathbb{H}_{\mathbb{D}}^{\times} \cong \mathbb{H}^{\times}\times\mathbb{H}^{\times} \cong \mathbb{R}_{>0}^2 \times S^3 \times S^3$. It is connected and simply connected, and it is homotopy equivalent to $S^3\times S^3$.

**Proof.** Units are pairs of nonzero quaternions, and $\mathbb{H}^\times \cong \mathbb{R}_{>0}\times S^3$; the positive rays are contractible, so the unit group deformation retracts onto $S^3\times S^3$. A product of spheres of dimension $3$ is simply connected.

**Corollary.** The homotopy groups of the unit group are

$$
\pi_0 = 0, \quad \pi_1 = 0, \quad \pi_2 = 0, \quad \pi_3(\mathbb{H}_{\mathbb{D}}^{\times}) = \mathbb{Z}\oplus\mathbb{Z} ,
$$

the last being $\pi_3(S^3)\oplus\pi_3(S^3)$ by the Künneth and Hurewicz theorems for a product of simply connected spaces.

## The Boundary of the Polar Decomposition

The componentwise polar form $\tilde{Q} = r_+\hat{q}_+ \tilde\Pi_1 + r_-\hat{q}_- \tilde\Pi_2$ of *Split-Biquaternion Exponential and Lie Group Structure* is defined for every element whose two components are nonzero, that is on the complement of the zero divisor set $Z = Z_+\cup Z_-$, and it fails exactly where a component vanishes. The two sets $Z_+ = \{\tilde{Q}_+ = 0\}$ and $Z_- = \{\tilde{Q}_- = 0\}$ are four-dimensional subspaces of the algebra, each homotopy equivalent to $S^3$, and their union is the **failure surface** of the polar decomposition:

$$
Z = \left\{ \tilde{Q} : \tilde{Q}_+ = 0 \ \text{or}\ \tilde{Q}_- = 0 \right\} , \qquad Z_\pm \simeq S^3 .
$$

**Proposition.** The failure surface $Z$ is a closed algebraic subset of dimension $4$, isotropic for the Hermitian form $g$, and its link in the Euclidean sphere is homeomorphic to $S^3$; the two pieces $Z_+$ and $Z_-$ meet only at the origin.

**Proof.** Each $Z_\pm$ is a four-dimensional real subspace, hence is $\simeq S^3$ after removing the origin; the two meet only in the zero element because $\tilde{Q}_+ = 0$ and $\tilde{Q}_- = 0$ together give $\tilde{Q} = 0$. Each element of $Z_\pm \setminus\{0\}$ is a zero divisor, hence isotropic for $g$. The link of a four-dimensional subspace in the seven-sphere is a three-sphere.

The polar decomposition is therefore a homeomorphism from the complement of $Z$ onto $(\mathbb{R}_{>0}\times S^3)\times(\mathbb{R}_{>0}\times S^3)$, and the topological boundary of its domain is exactly the zero divisor set.

## Comparison with the Biquaternion Case

The two algebras share the ambient topology: both are $\mathbb{R}^8$, both are contractible, and both have a seven-sphere of unit vectors. They differ in every structure attached to the forms. The biquaternion norm one slice is the complex quadric $\{N = 1\} \subset \mathbb{C}^4$, a six-dimensional manifold related to $SL(2,\mathbb{C})$ and non-compact; the split biquaternion norm-one group is the compact $S^3\times S^3 \cong \mathrm{Spin}(4)$. The biquaternion unit group $GL(2,\mathbb{C})$ deformation retracts onto the compact $U(2) \cong (S^1\times S^3)/\{\pm1\}$, with fundamental group $\mathbb{Z}$ and third homotopy group $\mathbb{Z}$; the split biquaternion unit group is $\mathbb{R}_{>0}^2\times S^3\times S^3$, simply connected, with third homotopy group $\mathbb{Z}^2$. The biquaternion null cone of the complex norm is the null cone of the complexified quadratic form with link $S^1\times S^1$; the split biquaternion null cone of the Hermitian form has link $S^3\times S^3$. The link of the null cone and the norm-one group, the same manifold here, are different objects in the biquaternion case, where the norm-one slice is non-compact and the null cone link is a torus.

## Summary

The algebra is $\mathbb{R}^8$, hence contractible, and its punctured form is homotopy equivalent to $S^7$. The Euclidean norm, the square root of the real part of the split-biquaternion norm, is positive definite; the Euclidean unit sphere is $S^7$, distinct from the six-dimensional norm-one group. The null cone of the Hermitian form $g$ of signature $(4,4)$ is the seven-dimensional cone $\|q\| = \|q'\|$, on which the split-biquaternion norm never vanishes off the origin, and it strictly contains the zero divisor set, whose members are isotropic but which does not exhaust the cone. The link of the null cone is $S^3\times S^3$, the same manifold as the norm-one group $\mathrm{Spin}(4)$. The group of units is $\mathbb{R}_{>0}^2\times S^3\times S^3$, connected, simply connected, homotopy equivalent to $S^3\times S^3$, with $\pi_3 = \mathbb{Z}^2$. The polar decomposition of an element is defined off the zero divisor set, whose two four-dimensional pieces $Z_\pm$ are each $\simeq S^3$ and meet only at the origin; that set is the failure surface and the topological boundary of the polar domain. Compared with the biquaternion case, the ambient topology is the same but every form-attached object differs: the compact $\mathrm{Spin}(4)$ norm-one group replaces the non-compact $SL(2,\mathbb{C})$ slice, the simply connected unit group replaces $GL(2,\mathbb{C})$, and the link $S^3\times S^3$ replaces the torus.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}_{\mathbb{D}} \cong \mathbb{R}^8$ | The algebra as a topological space |
| $\|\tilde{Q}\| = (\mathrm{Re}\,N(\tilde{Q}))^{1/2}$ | Euclidean norm |
| $S_{\mathbb{E}} = \{\|\tilde{Q}\| = 1\} \cong S^7$ | Euclidean unit sphere |
| $g(\tilde{Q}) = \sum_\mu(q_\mu^2 - q'^2_\mu)$ | Hermitian form of signature $(4,4)$ |
| $C = \{g = 0\}$ | Null cone, dimension $7$ |
| $L = C\cap S_{\mathbb{E}} \cong S^3\times S^3$ | Link of the null cone |
| $Z_\pm = \{\tilde{Q}_\pm = 0\}$ | The two four-dimensional zero divisor subspaces |
| $Z = Z_+\cup Z_-$ | Zero divisor set, the failure surface of the polar form |
| $\mathbb{H}_{\mathbb{D}}^{\times} \cong \mathbb{R}_{>0}^2\times S^3\times S^3$ | Group of units |
| $G_1 = S^3\times S^3 \cong \mathrm{Spin}(4)$ | Norm-one group |
| $\pi_3(\mathbb{H}_{\mathbb{D}}^{\times}) = \mathbb{Z}^2$ | Third homotopy group of the unit group |

## Further Reading

- Allen Hatcher, *Algebraic Topology* (Cambridge University Press, 2002), for homotopy equivalence, the homotopy groups of spheres and the Künneth theorem.
- John Milnor and James D. Stasheff, *Characteristic Classes* (Princeton University Press, 1974), for the homotopy and cohomology of $S^3\times S^3$ and of the compact classical groups.
- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (Academic Press, 1978), for the topology of non-compact groups and their maximal compact subgroups.
- F. Reese Harvey, *Spinors and Calibrations* (Academic Press, 1990), for the links of the null cones of the classical forms and their relation to the sphere products.
