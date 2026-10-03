# __The Isotropic Structure of the Krein Form__

## Introduction

An indefinite Hermitian form has a **null set** beyond the origin, and the shape of that set and of the totally isotropic subspaces it carries is the geometry of the form. For the Krein form $[\tilde{Q},\tilde{Q}']=\sum_{\mu}\varepsilon_{\mu}\bar Q_{\mu}Q'_{\mu}$ the null set is the real quadric $[\tilde{Q},\tilde{Q}]=0$ of dimension $7$, it is smooth away from the origin, its link is the product $S^{1}\times S^{5}$, and its maximal totally isotropic subspaces have dimension the **Witt index** $\min(p,q)$, that is $1$ over $\mathbb{C}$ and $2$ over $\mathbb{R}$. This article treats that structure: the isotropic elements, the totally isotropic subspaces, the isotropic lines and their boundary sphere, and the comparison with the *other* null set of the algebra, the zero-divisor cone of the norm $N$. The orthogonality and the subspaces are in *Krein Orthogonality and the Fundamental Decomposition*; the level sets of positive and negative sign are in *The Krein Level Sets and the Hyperbolic Structure*; and the projective geometry of the norm's cone is in *Biquaternion Topology*.

**Conventions.** $e_0=1$, $e_k^{2}=-e_0$, central scalar imaginary $i$, $\mathrm{Sc}$ the scalar part; the Krein form is $[\tilde{Q},\tilde{Q}']=\sum_{\mu}\varepsilon_{\mu}\bar Q_{\mu}Q'_{\mu}$ with $\varepsilon=(1,-1,-1,-1)$, the Hermitian form is $\langle\tilde{Q},\tilde{Q}'\rangle=\sum_{\mu}\bar Q_{\mu}Q'_{\mu}$ with $\|\tilde{Q}\|_E^{2}=\langle\tilde{Q},\tilde{Q}\rangle$, and the norm is $N(\tilde{Q})=\sum_{\mu}Q_{\mu}^{2}$.

## Isotropic Elements

**Definition.** An element $\tilde{Q}$ is **Krein-isotropic**, or **Krein-null**, when $[\tilde{Q},\tilde{Q}]=0$; the **Krein null set** is

$$
\mathcal{K}=\{\tilde{Q}:[\tilde{Q},\tilde{Q}]=0\}=\Bigl\{\tilde{Q}:\sum_{\mu}\varepsilon_{\mu}|Q_{\mu}|^{2}=0\Bigr\}.
$$

**Theorem (the shape of the null set).** In the splitting $\tilde{Q}=c+v$ of the algebra into its centre and vector parts, with $c\in\mathbb{C}_{\mathbb{B}}$ the scalar part and $v\in\mathbb{V}_{\mathbb{B}}$ the vector part,

$$
\mathcal{K}=\{\tilde{Q}:\|c\|_E=\|v\|_E\};
$$

it is a closed real algebraic cone of apex the origin, homogeneous of degree two, of real dimension $7$, irregular only at the apex, and it is connected.

**Proof.** $[\tilde{Q},\tilde{Q}]=\|c\|_E^{2}-\|v\|_E^{2}$ by the sign vector of the coefficient basis, so the equation is $\|c\|_E=\|v\|_E$. The set is the zero set of a single non-constant real polynomial, hence of dimension $7$ at its smooth points; its gradient with respect to the four real coordinates of $c$ and the six of $v$ is $2(c,-v)\neq0$ off the origin, so the apex is the only singular point and the cone is a real $7$-manifold away from it. Connectivity follows because the map $\tilde{Q}\mapsto(\|c\|_E,\|v\|_E)$ makes the cone for each $t>0$ the product of the spheres of radius $t$ in the two factors, glued along $t$, that is $S^{1}\times S^{5}$.

**Theorem (the link).** The intersection of the null set with the Euclidean unit sphere $\|\tilde{Q}\|_E=1$ is diffeomorphic to $S^{1}\times S^{5}$; the punctured cone $\mathcal{K}\setminus\{0\}$ retracts onto it and is homotopy equivalent to $S^{1}\times S^{5}$.

**Proof.** On the unit sphere $\|c\|_E^{2}+\|v\|_E^{2}=1$ together with $\|c\|_E=\|v\|_E$ forces $\|c\|_E=\|v\|_E=1/\sqrt2$, so the link is $S^{1}\times S^{5}$ with the radii $1/\sqrt2$; the retraction is $\tilde{Q}\mapsto\tilde{Q}/\|\tilde{Q}\|_E$.

**Example.** $e_0+e_1$ has $[e_0+e_1,e_0+e_1]=1-1=0$ and $N=2$, so it is isotropic for the Krein form and not for the norm. The element $e_1+ie_2$ has $N=1+i^{2}=0$ and $[e_1+ie_2,e_1+ie_2]=-2$, the reverse situation.

## The Comparison with the Norm Cone

**Definition.** The **norm cone** of the algebra is the zero set $\mathcal{N}=\{\tilde{Q}:N(\tilde{Q})=0\}$ of the norm, the union of the origin and the zero-divisor set of *Biquaternion Zero Divisors*; it is a complex cone of real dimension $6$.

**Theorem (the two cones are different).** The Krein null set and the norm cone are distinct: neither is contained in the other. Their intersection $\mathcal{K}\cap\mathcal{N}$ is a real algebraic cone of dimension $5$, and it contains the two complex lines $\mathbb{C}(e_0+ie_1)$ and $\mathbb{C}(e_0-ie_1)$.

**Proof.** $e_0+e_1$ is in the Krein null set and not in the norm cone, $e_1+ie_2$ in the norm cone and not in the Krein null set, so neither inclusion holds. For the dimension, in the affine chart $Q_0=1$ the equations $N=0$ and $[\tilde{Q},\tilde{Q}]=0$ are one complex and one real equation on the six real coordinates $Q_1,Q_2,Q_3$, that is three real equations in six unknowns, so the projective intersection has real dimension $3$ and the cone over it has real dimension $5$. The two displayed lines are isotropic for both forms: $N(e_0\pm ie_1)=1+(i)^{2}=0$ and $[e_0\pm ie_1,e_0\pm ie_1]=1-1=0$.

**Remark (the two cones agree on a real slice).** On the real quaternion subspace $\mathbb{H}_{\mathbb{B}}$ the Krein form is the interval form and the norm is the Euclidean form, $[\tilde{Q},\tilde{Q}]=q_0^{2}-\sum_kq_k^{2}$ and $N(\tilde{Q})=\sum_{\mu}q_{\mu}^{2}$; the Krein null set is the light cone of the slice, the norm cone meets the real slice only at the origin, and the two agree nowhere except at $0$.

## Totally Isotropic Subspaces

**Definition.** A subspace $\mathbb{W}$ is **totally isotropic** when $[\tilde{Q},\tilde{Q}']=0$ for all $\tilde{Q},\tilde{Q}'\in\mathbb{W}$, equivalently when $\mathbb{W}\subseteq\mathbb{W}^{\perp_{K}}$; it is **maximal** when it is contained in no larger one. The **Witt index** of the Krein form is the common dimension of the maximal totally isotropic subspaces.

**Theorem (the Witt index and the maximal isotropic subspaces).** The Witt index is $\min(p,q)$: it is $1$ over $\mathbb{C}$ and $2$ over $\mathbb{R}$. A maximal totally isotropic complex subspace is $\mathbb{C}(e_0+e_1)$, and a maximal totally isotropic real subspace is the plane

$$
\mathbb{W}_{\mathrm{iso}}=\mathrm{span}_{\mathbb{R}}\{e_0+e_1,\ i(e_0+e_1)\},
\qquad
e_0+e_1\ \text{and}\ i(e_0+e_1)\ \text{isotropic, mutually orthogonal}.
$$

Every totally isotropic subspace is contained in a maximal one, and the isometry group $U(1,3)$ acts transitively on the maximal ones.

**Proof.** If $\mathbb{W}$ is totally isotropic then it is orthogonal to itself, so $\mathbb{W}\subseteq\mathbb{W}^{\perp_{K}}$, and the restriction of the form to $\mathbb{W}+\mathbb{W}^{\perp_{K}}/\mathbb{W}^{\perp_{K}}$ makes the dimension of $\mathbb{W}$ at most $\min(p,q)$: an isotropic subspace meets the maximal positive definite subspaces and the maximal negative definite subspaces only at $0$. The two displayed spaces attain $\min(p,q)=1$ over $\mathbb{C}$ and $\min(p,q)=2$ over $\mathbb{R}$, since $[e_0+e_1,e_0+e_1]=0$, $[e_0+e_1,i(e_0+e_1)]=i-i=0$ and the plane is $2$-dimensional over $\mathbb{R}$. The extension and transitivity are Witt's extension theorem for Hermitian forms (*Witt's Theorems*).

**Remark (the isotropic and the null elements).** An element $\tilde{Q}$ is isotropic exactly when the line $\mathbb{C}\tilde{Q}$ is totally isotropic (over $\mathbb{R}$, the real plane $\mathrm{span}_{\mathbb{R}}\{\tilde{Q},i\tilde{Q}\}$ is); the null set of the first section is the union of the totally isotropic complex lines, and the totally isotropic subspaces are the subspaces all of whose elements are isotropic.

## The Isotropic Lines and the Boundary Sphere

**Definition.** The **isotropic lines** of $\mathbb{C}^{4}$ for the Krein form are the complex lines $\mathbb{C}\tilde{Q}$ spanned by nonzero isotropic elements.

**Theorem (the isotropic lines form $S^{5}$).** The isotropic complex lines are exactly the lines $\mathbb{C}(e_0+\tilde{V})$ with $\|\tilde{V}\|_E=1$, so the assignment $\tilde{V}\mapsto\mathbb{C}(e_0+\tilde{V})$ is a bijection from the unit sphere of $\mathbb{V}_{\mathbb{B}}\cong\mathbb{C}^{3}$ — a copy of $S^{5}$ — onto the set of isotropic lines.

**Proof.** An isotropic line $\mathbb{C}\tilde{Q}$ has $[\tilde{Q},\tilde{Q}]=0$, hence $\|c\|_E=\|v\|_E$, so it is not contained in $\mathbb{V}_{\mathbb{B}}$ and admits a representative with nonzero scalar part; scaling it gives exactly one representative of the form $e_0+\tilde{V}$. For that representative $[e_0+\tilde{V},e_0+\tilde{V}]=1-\|\tilde{V}\|_E^{2}$, so the line is isotropic exactly for $\|\tilde{V}\|_E=1$; and distinct points $\tilde{V}$ of the unit sphere give distinct lines, since $e_0+\tilde{V}$ and $e_0+\tilde{V}'$ span the same line only if $\tilde{V}=\tilde{V}'$. This is the boundary case of the parametrisation of the maximal positive definite subspaces in *Krein Orthogonality and the Fundamental Decomposition*, which uses the open ball $\|\tilde{V}\|_E<1$.

**Corollary (the two links).** The punctured real cone $\mathcal{K}\setminus\{0\}$ is homotopy equivalent to $S^{1}\times S^{5}$, and the space of isotropic complex lines is $S^{5}$: passing from one to the other is dividing by the action of the circle of complex phases, which acts freely on the isotropic elements.

## Worked Examples

**An isotropic element of the centre–vector type.** $\tilde{Q}=e_0+e_1$: isotropic, norm $2$, in the light cone of the real quaternion slice at the boundary.

**A zero divisor that is isotropic.** $\tilde{Q}=e_0+ie_1$: both $N=0$ and $[\tilde{Q},\tilde{Q}]=0$; the line it spans is a doubly null line.

**A zero divisor that is not isotropic.** $\tilde{Q}=e_1+ie_2$: $N=0$, $[\tilde{Q},\tilde{Q}]=-2$, a strictly negative element.

**A timelike element.** $\tilde{Q}=e_0+0.5e_1$: $[\,\tilde{Q},\tilde{Q}]=0.75>0$, so it lies inside the positive region and spans a maximal positive definite line.

**A maximal isotropic plane.** $\mathbb{W}_{\mathrm{iso}}=\mathrm{span}_{\mathbb{R}}\{e_0+e_1,\ i(e_0+e_1)\}$: real dimension $2$, over $\mathbb{C}$ it is the single line $\mathbb{C}(e_0+e_1)$, and it is maximal because the Witt index over $\mathbb{R}$ is $2$.

**The link at a point.** For $\tilde{Q}=(e_0+e_1)/\sqrt2$ one has $\|\tilde{Q}\|_E=1$ and $[\,\tilde{Q},\tilde{Q}]=0$: the point $S^{1}\times S^{5}$ of the link is reached by normalising, and the circle is the phase of the complex coefficient.

## Summary

The Krein null set is $\mathcal{K}=\{\|c\|_E=\|v\|_E\}$, a real algebraic cone of dimension $7$, smooth away from its apex, connected, with link and punctured homotopy type $S^{1}\times S^{5}$. It is distinct from the complex norm cone of the zero divisors: neither contains the other, the two meet in a cone of real dimension $5$, and the lines $\mathbb{C}(e_0\pm ie_1)$ are null for both forms. A totally isotropic subspace is one contained in its own Krein-orthogonal complement; the Witt index is $\min(p,q)$, that is $1$ over $\mathbb{C}$ and $2$ over $\mathbb{R}$; a maximal isotropic complex subspace is the line $\mathbb{C}(e_0+e_1)$, a maximal isotropic real subspace is the plane it spans with $i(e_0+e_1)$; every isotropic subspace extends to a maximal one and the isometry group acts transitively on the maximal ones. The isotropic complex lines are the points of $S^{5}$, the boundary sphere of the positive half of the ball; the centre $S^{1}$ is the difference between the punctured cone and the space of isotropic lines.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{K}=\{\tilde{Q}:[\tilde{Q},\tilde{Q}]=0\}=\{\lVert c\rVert_E=\lVert v\rVert_E\}$ | The Krein null set |
| $S^{1}\times S^{5}$ | The link of the null cone and the homotopy type of $\mathcal{K}\setminus\{0\}$ |
| $\mathcal{N}=\{N(\tilde{Q})=0\}$ | The norm cone of the zero divisors |
| $\mathbb{C}(e_0\pm ie_1)$ | Doubly null isotropic lines |
| $\min(p,q)=1$ over $\mathbb{C}$, $2$ over $\mathbb{R}$ | The Witt index |
| $\mathbb{W}_{\mathrm{iso}}=\mathrm{span}_{\mathbb{R}}\{e_0+e_1,i(e_0+e_1)\}$ | The maximal isotropic real plane |
| $\mathbb{W}\subseteq\mathbb{W}^{\perp_{K}}$ | Totally isotropic subspace |
| $S^{5}$ | The space of isotropic complex lines |

## Further Reading

- *Biquaternion Zero Divisors* (`articles_maths/biquaternion-zero-divisors.md`), for the norm cone that the Krein null set is compared with
- *Krein Orthogonality and the Fundamental Decomposition* (`articles_maths/krein-orthogonality-and-the-fundamental-decomposition.md`), for the complements used here
- *The Krein Level Sets and the Hyperbolic Structure* (`articles_maths/the-krein-level-sets-and-the-hyperbolic-structure.md`), for the ball whose boundary is the isotropic sphere
- *Biquaternion Topology* (`articles_maths/biquaternion-topology.md`), for the projective geometry of the norm's null cone
- *Witt's Theorems* (`articles_maths/witts-theorems.md`), for the extension and transitivity theorems for forms
- János Bognár, *Indefinite Inner Product Spaces* (Springer, 1974), for isotropic subspaces, the Witt index and neutrality in a Krein space
