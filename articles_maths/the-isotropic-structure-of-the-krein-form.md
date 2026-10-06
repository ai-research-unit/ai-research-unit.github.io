# __The Isotropic Structure of the Krein Form__

## Introduction

An indefinite complex sesquilinear form has a **null set** beyond the origin, and the shape of that set and of the totally isotropic subspaces it carries is the geometry of the form. For the quaternion sesquilinear form $\langle\tilde{Q}',\tilde{Q}\rangle_{\natural*}=\sum_{\mu}\varepsilon_{\mu}\bar Q_{\mu}Q'_{\mu}$ the null set is the real quadric $\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=0$ of dimension $7$, it is smooth away from the origin, its link is the product $S^{1}\times S^{5}$, and its maximal totally isotropic subspaces have dimension the **Witt index** $\min(p,q)$, that is $1$ over $\mathbb{C}$ and $2$ over $\mathbb{R}$. This article treats that structure: the isotropic elements, the totally isotropic subspaces, and the isotropic lines and their boundary sphere. The comparison with the *other* null set of the algebra, the zero-divisor cone of the norm $N$, is *The Four Pairings of the Biquaternion Algebra*, §*The Null Sets Compared*. The orthogonality and the subspaces are in *Krein Orthogonality and the Fundamental Decomposition*; the level sets of positive and negative sign are in *The Krein Level Sets and the Hyperbolic Structure*; and the projective geometry of the norm's cone is in *Biquaternion Topology*.

**Conventions.** $e_0=1$, $e_k^{2}=-e_0$, central scalar imaginary $i$, $\mathrm{Sc}$ the scalar part; the quaternion sesquilinear form is $\langle\tilde{Q}',\tilde{Q}\rangle_{\natural*}=\sum_{\mu}\varepsilon_{\mu}\bar Q_{\mu}Q'_{\mu}$ with $\varepsilon=(1,-1,-1,-1)$, the complex sesquilinear form is $\langle\tilde{Q}',\tilde{Q}\rangle_{*}=\sum_{\mu}\bar Q_{\mu}Q'_{\mu}$ with $\|\tilde{Q}\|_E^{2}=\langle\tilde{Q},\tilde{Q}\rangle_{*}$, and the norm is $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=\sum_{\mu}Q_{\mu}^{2}$.

## Isotropic Elements

**Definition.** An element $\tilde{Q}$ is **Krein-isotropic**, or **Krein-null**, when $\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=0$; the **Krein null set** is

$$
\mathcal{K}=\{\tilde{Q}:\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=0\}=\Bigl\{\tilde{Q}:\sum_{\mu}\varepsilon_{\mu}|Q_{\mu}|^{2}=0\Bigr\}.
$$

**Theorem (the shape of the null set).** In the splitting $\tilde{Q}=c+v$ of the algebra into its centre and vector parts, with $c\in\mathbb{C}_{\mathbb{B}}$ the scalar part and $v\in\mathbb{V}_{\mathbb{B}}$ the vector part,

$$
\mathcal{K}=\{\tilde{Q}:\|c\|_E=\|v\|_E\};
$$

it is a closed real algebraic cone of apex the origin, homogeneous of degree two, of real dimension $7$, irregular only at the apex, and it is connected.

**Proof.** $\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=\|c\|_E^{2}-\|v\|_E^{2}$ by the sign vector of the coefficient basis, so the equation is $\|c\|_E=\|v\|_E$. The set is the zero set of a single non-constant real polynomial, hence of dimension $7$ at its smooth points; its gradient with respect to the four real coordinates of $c$ and the six of $v$ is $2(c,-v)\neq0$ off the origin, so the apex is the only singular point and the cone is a real $7$-manifold away from it. Connectivity follows because the map $\tilde{Q}\mapsto(\|c\|_E,\|v\|_E)$ makes the cone for each $t>0$ the product of the spheres of radius $t$ in the two factors, glued along $t$, that is $S^{1}\times S^{5}$.

**Theorem (the link).** The intersection of the null set with the Euclidean unit sphere $\|\tilde{Q}\|_E=1$ is diffeomorphic to $S^{1}\times S^{5}$; the punctured cone $\mathcal{K}\setminus\{0\}$ retracts onto it and is homotopy equivalent to $S^{1}\times S^{5}$.

**Proof.** On the unit sphere $\|c\|_E^{2}+\|v\|_E^{2}=1$ together with $\|c\|_E=\|v\|_E$ forces $\|c\|_E=\|v\|_E=1/\sqrt2$, so the link is $S^{1}\times S^{5}$ with the radii $1/\sqrt2$; the retraction is $\tilde{Q}\mapsto\tilde{Q}/\|\tilde{Q}\|_E$.

**Example.** $e_0+e_1$ has $\langle e_0+e_1,e_0+e_1\rangle_{\natural*}=1-1=0$ and $N=2$, so it is isotropic for the quaternion sesquilinear form and not for the norm. The element $e_1+ie_2$ has $N=1+i^{2}=0$ and $\langle e_1+ie_2,e_1+ie_2\rangle_{\natural*}=-2$, the reverse situation.

## Totally Isotropic Subspaces

**Definition.** A subspace $\mathbb{W}$ is **totally isotropic** when $\langle\tilde{Q}',\tilde{Q}\rangle_{\natural*}=0$ for all $\tilde{Q},\tilde{Q}'\in\mathbb{W}$, equivalently when $\mathbb{W}\subseteq\mathbb{W}^{\perp_{K}}$; it is **maximal** when it is contained in no larger one. The **Witt index** of the quaternion sesquilinear form is the common dimension of the maximal totally isotropic subspaces.

**Theorem (the Witt index and the maximal isotropic subspaces).** The Witt index is $\min(p,q)$: it is $1$ over $\mathbb{C}$ and $2$ over $\mathbb{R}$. A maximal totally isotropic complex subspace is $\mathbb{C}(e_0+e_1)$, and a maximal totally isotropic real subspace is the plane

$$
\mathbb{W}_{\mathrm{iso}}=\mathrm{span}_{\mathbb{R}}\{e_0+e_1,\ i(e_0+e_1)\},
\qquad
e_0+e_1\ \text{and}\ i(e_0+e_1)\ \text{isotropic, mutually orthogonal}.
$$

Every totally isotropic subspace is contained in a maximal one, and the isometry group $U(1,3)$ acts transitively on the maximal ones.

**Proof.** If $\mathbb{W}$ is totally isotropic then it is orthogonal to itself, so $\mathbb{W}\subseteq\mathbb{W}^{\perp_{K}}$, and the restriction of the form to $\mathbb{W}+\mathbb{W}^{\perp_{K}}/\mathbb{W}^{\perp_{K}}$ makes the dimension of $\mathbb{W}$ at most $\min(p,q)$: an isotropic subspace meets the maximal positive definite subspaces and the maximal negative definite subspaces only at $0$. The two displayed spaces attain $\min(p,q)=1$ over $\mathbb{C}$ and $\min(p,q)=2$ over $\mathbb{R}$, since $\langle e_0+e_1,e_0+e_1\rangle_{\natural*}=0$, $\langle i(e_0+e_1),e_0+e_1\rangle_{\natural*}=i-i=0$ and the plane is $2$-dimensional over $\mathbb{R}$. The extension and transitivity are Witt's extension theorem for complex sesquilinear forms (*Witt's Theorems*).

**Remark (the isotropic and the null elements).** An element $\tilde{Q}$ is isotropic exactly when the line $\mathbb{C}\tilde{Q}$ is totally isotropic (over $\mathbb{R}$, the real plane $\mathrm{span}_{\mathbb{R}}\{\tilde{Q},i\tilde{Q}\}$ is); the null set of the first section is the union of the totally isotropic complex lines, and the totally isotropic subspaces are the subspaces all of whose elements are isotropic.

## The Index in Two Ways

The index is $1$ over $\mathbb{C}$ and $2$ over $\mathbb{R}$, and it can be computed twice: bounded by the two definite parts, and exhibited by the isotropic lines that are also norm-null.

**Theorem (the index by a maximal definite subspace).** A definite subspace meets a totally isotropic subspace only at the origin. Hence a totally isotropic subspace $\mathbb{W}$ maps injectively into the two quotients $\mathbb{B}/\mathbb{W}_{-}$ and $\mathbb{B}/\mathbb{W}_{+}$, for every maximal negative definite subspace $\mathbb{W}_{-}$ and every maximal positive definite subspace $\mathbb{W}_{+}$, and

$$
\dim_{\mathbb{C}}\mathbb{W}\leq\dim_{\mathbb{C}}\bigl(\mathbb{B}/\mathbb{W}_{-}\bigr)=p,\qquad
\dim_{\mathbb{C}}\mathbb{W}\leq\dim_{\mathbb{C}}\bigl(\mathbb{B}/\mathbb{W}_{+}\bigr)=q .
$$

Therefore the Witt index is at most $\min(p,q)$, and the bound is attained.

**Proof.** A nonzero element of a definite subspace has a nonzero square, so it is not isotropic and cannot lie in the totally isotropic $\mathbb{W}$; the projection is therefore injective. The dimensions are $\dim\mathbb{B}-\dim\mathbb{W}_{-}=4-3=1=p$ and $\dim\mathbb{B}-\dim\mathbb{W}_{+}=4-1=3=q$. The bound $\min(p,q)=1$ over $\mathbb{C}$ is attained by the line $\mathbb{C}(e_0+e_1)$, and over $\mathbb{R}$, where the bound is $2$, by the plane $\mathrm{span}_{\mathbb{R}}\{e_0+e_1,i(e_0+e_1)\}$.

**Definition.** A **doubly null line** is an isotropic line that lies in the norm cone as well: a complex line $\mathbb{C}\tilde{Q}$ with $\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=0$ and $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=0$.

**Theorem (the Peirce lines).** For every real unit vector $\hat\mu\in\mathbb{V}_{\mathbb{B}}$ the element

$$
\tilde\Pi_{\pm}(\hat\mu)=\tfrac12\bigl(e_0\pm i\hat\mu\bigr)
$$

is a rank-one Hermitian idempotent, $\tilde\Pi_\pm^2=\tilde\Pi_\pm$, $\tilde\Pi_\pm^{*}=\tilde\Pi_\pm$, with $N(\tilde\Pi_\pm)=0$ and $\langle\tilde\Pi_\pm,\tilde\Pi_\pm\rangle_{\natural*}=0$. The line $\mathbb{C}\tilde\Pi_\pm(\hat\mu)$ is therefore a maximal totally isotropic complex subspace and a doubly null line; it is a **Peirce line** of the algebra, generating the minimal left ideal $\mathbb{B}\tilde\Pi_\pm(\hat\mu)$ and the minimal right ideal $\tilde\Pi_\pm(\hat\mu)\mathbb{B}$, of complex dimension two, every element of which is a zero divisor. The two diagonal members $\hat\mu=e_1$ give the lines $\mathbb{C}(e_0\pm ie_1)$, the two distinguished doubly null lines.

**Proof.** A real unit vector has $\hat\mu^2=-e_0$, so $(i\hat\mu)^2=e_0$ and $(e_0\pm i\hat\mu)^2=1\pm2i\hat\mu+(i\hat\mu)^2=2(e_0\pm i\hat\mu)$, whence $\tilde\Pi_\pm^2=\tilde\Pi_\pm$; $\tilde\Pi_\pm$ is Hermitian because $(i\hat\mu)^{*}=i\hat\mu$. For the two squares, $N(e_0\pm i\hat\mu)=1+N(i\hat\mu)=1-\|\hat\mu\|_E^2=0$ and $\langle e_0\pm i\hat\mu,e_0\pm i\hat\mu\rangle_{\natural*}=1-\|i\hat\mu\|_E^2=0$. The minimal ideals are the standard ones of the algebra, of complex dimension two, and their elements $X\tilde\Pi_\pm$ satisfy $N(X\tilde\Pi_\pm)=N(X)N(\tilde\Pi_\pm)=0$.

**Corollary (the two descriptions agree on the norm cone).** The Peirce lines are exactly the doubly null lines. Writing $\tilde V=\tilde U+i\tilde W$ with $\tilde U,\tilde W\in\mathbb{V}_{\mathbb{B}}$ real, the conditions $\|\tilde V\|_E=1$ and $N(\tilde V)=-1$ read

$$
\|\tilde U\|_E^{2}+\|\tilde W\|_E^{2}=1,\qquad
\|\tilde U\|_E^{2}-\|\tilde W\|_E^{2}=-1,\qquad
\langle\tilde U,\tilde W\rangle=0,
$$

which force $\tilde U=0$ and $\|\tilde W\|_E=1$: the doubly null lines are exactly the lines $\mathbb{C}(e_0\pm i\hat\mu)$, parametrised by the unit sphere $S^2$ of directions with the two signs, and the Peirce description is complete on the norm cone. The maximal totally isotropic *real* subspace is, by contrast, the plane $\mathrm{span}_{\mathbb{R}}\{e_0+e_1,i(e_0+e_1)\}$, whose generator has $N=2$ and is not a zero divisor, so it is not a Peirce line; within the real form $\mathbb{H}_{\mathbb{B}}$, whose form is the interval form in the basis $e_0,e_1,e_2,e_3$, the maximal totally isotropic subspace is the diagonal light line $\mathrm{span}_{\mathbb{R}}\{e_0+e_1\}$, and the Peirce lines are the complementary, norm-null part of the isotropic lines.

**Proof.** The three equations are the real and imaginary parts of $N(\tilde V)=-1$ together with $\|\tilde V\|_E=1$, using $N(\tilde U+i\tilde W)=\|\tilde U\|_E^{2}-\|\tilde W\|_E^{2}+2i\langle\tilde U,\tilde W\rangle$ and $\|\tilde U+i\tilde W\|_E^{2}=\|\tilde U\|_E^{2}+\|\tilde W\|_E^{2}$; adding and subtracting the first two give $\|\tilde U\|_E^{2}=0$ and $\|\tilde W\|_E^{2}=1$. The remaining statements are the previous definition and corollary.

## The Isotropic Lines and the Boundary Sphere

**Definition.** The **isotropic lines** of $\mathbb{C}^{4}$ for the quaternion sesquilinear form are the complex lines $\mathbb{C}\tilde{Q}$ spanned by nonzero isotropic elements.

**Theorem (the isotropic lines form $S^{5}$).** The isotropic complex lines are exactly the lines $\mathbb{C}(e_0+\tilde{V})$ with $\|\tilde{V}\|_E=1$, so the assignment $\tilde{V}\mapsto\mathbb{C}(e_0+\tilde{V})$ is a bijection from the unit sphere of $\mathbb{V}_{\mathbb{B}}\cong\mathbb{C}^{3}$ — a copy of $S^{5}$ — onto the set of isotropic lines.

**Proof.** An isotropic line $\mathbb{C}\tilde{Q}$ has $\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=0$, hence $\|c\|_E=\|v\|_E$, so it is not contained in $\mathbb{V}_{\mathbb{B}}$ and admits a representative with nonzero scalar part; scaling it gives exactly one representative of the form $e_0+\tilde{V}$. For that representative $\langle e_0+\tilde{V},e_0+\tilde{V}\rangle_{\natural*}=1-\|\tilde{V}\|_E^{2}$, so the line is isotropic exactly for $\|\tilde{V}\|_E=1$; and distinct points $\tilde{V}$ of the unit sphere give distinct lines, since $e_0+\tilde{V}$ and $e_0+\tilde{V}'$ span the same line only if $\tilde{V}=\tilde{V}'$. This is the boundary case of the parametrisation of the maximal positive definite subspaces in *Krein Orthogonality and the Fundamental Decomposition*, which uses the open ball $\|\tilde{V}\|_E<1$.

**Corollary (the two links).** The punctured real cone $\mathcal{K}\setminus\{0\}$ is homotopy equivalent to $S^{1}\times S^{5}$, and the space of isotropic complex lines is $S^{5}$: passing from one to the other is dividing by the action of the circle of complex phases, which acts freely on the isotropic elements.

## Worked Examples

**An isotropic element of the centre–vector type.** $\tilde{Q}=e_0+e_1$: isotropic, norm $2$, in the light cone of the real quaternion slice at the boundary.

**A zero divisor that is isotropic.** $\tilde{Q}=e_0+ie_1$: both $N=0$ and $\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=0$; the line it spans is a doubly null line.

**A zero divisor that is not isotropic.** $\tilde{Q}=e_1+ie_2$: $N=0$, $\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=-2$, a strictly negative element.

**A timelike element.** $\tilde{Q}=e_0+\tfrac12e_1$: $\langle\tilde{Q},\,\tilde{Q}\rangle_{\natural*}=\tfrac34>0$, so it lies inside the positive region and spans a maximal positive definite line.

**A maximal isotropic plane.** $\mathbb{W}_{\mathrm{iso}}=\mathrm{span}_{\mathbb{R}}\{e_0+e_1,\ i(e_0+e_1)\}$: real dimension $2$, over $\mathbb{C}$ it is the single line $\mathbb{C}(e_0+e_1)$, and it is maximal because the Witt index over $\mathbb{R}$ is $2$.

**The link at a point.** For $\tilde{Q}=(e_0+e_1)/\sqrt2$ one has $\|\tilde{Q}\|_E=1$ and $\langle\tilde{Q},\,\tilde{Q}\rangle_{\natural*}=0$: the point $S^{1}\times S^{5}$ of the link is reached by normalising, and the circle is the phase of the complex coefficient.

**A Peirce line.** $\hat\mu=e_2$: $\tilde\Pi_+=\tfrac12(e_0+ie_2)$ is a rank-one Hermitian idempotent with $N=0$ and $\langle\tilde\Pi_+,\tilde\Pi_+\rangle_{\natural*}=0$, so the line $\mathbb{C}(e_0+ie_2)=\mathbb{C}\tilde\Pi_+$ is a doubly null maximal isotropic line, a Peirce line.

**A maximal isotropic line that is not Peirce.** $\mathbb{C}(e_0+e_1)$: the generator has $N=2$, so the line is isotropic and not doubly null; it is the complexification of the diagonal light line of the real form $\mathbb{H}_{\mathbb{B}}$, and it exhausts the index over $\mathbb{C}$ without lying in the norm cone.

## Summary

The Krein null set is $\mathcal{K}=\{\|c\|_E=\|v\|_E\}$, a real algebraic cone of dimension $7$, smooth away from its apex, connected, with link and punctured homotopy type $S^{1}\times S^{5}$. It meets the complex norm cone of the zero divisors in the union of the doubly null lines, a cone of real dimension $4$ that contains $\mathbb{C}(e_0\pm ie_1)$; the comparison of the two cones is *The Four Pairings of the Biquaternion Algebra*, §*The Null Sets Compared*. A totally isotropic subspace is one contained in its own Krein-orthogonal complement; the Witt index is $\min(p,q)$, that is $1$ over $\mathbb{C}$ and $2$ over $\mathbb{R}$; a maximal isotropic complex subspace is the line $\mathbb{C}(e_0+e_1)$, a maximal isotropic real subspace is the plane it spans with $i(e_0+e_1)$; every isotropic subspace extends to a maximal one and the isometry group acts transitively on the maximal ones. The isotropic complex lines are the points of $S^{5}$, the boundary sphere of the positive half of the ball; the centre $S^{1}$ is the difference between the punctured cone and the space of isotropic lines. The index is computed twice: bounded by the two definite parts, a totally isotropic subspace injecting into the quotient by either, and exhibited by the **Peirce lines** generated by the rank-one Hermitian idempotents $\tilde\Pi_\pm(\hat\mu)=\tfrac12(e_0\pm i\hat\mu)$; these are exactly the doubly null lines, the isotropic lines that lie in the norm cone, while the maximal isotropic real plane is not a Peirce line, its generator being a non-zero-divisor.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{K}=\{\tilde{Q}:\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=0\}=\{\lVert c\rVert_E=\lVert v\rVert_E\}$ | The Krein null set |
| $S^{1}\times S^{5}$ | The link of the null cone and the homotopy type of $\mathcal{K}\setminus\{0\}$ |
| $\mathcal{N}=\{\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=0\}$ | The norm cone of the zero divisors |
| $\mathbb{C}(e_0\pm ie_1)$ | Doubly null isotropic lines |
| $\min(p,q)=1$ over $\mathbb{C}$, $2$ over $\mathbb{R}$ | The Witt index |
| $\mathbb{W}_{\mathrm{iso}}=\mathrm{span}_{\mathbb{R}}\{e_0+e_1,i(e_0+e_1)\}$ | The maximal isotropic real plane |
| $\mathbb{W}\subseteq\mathbb{W}^{\perp_{K}}$ | Totally isotropic subspace |
| $\dim_{\mathbb{C}}\mathbb{W}\le\min(p,q)$ | The index bound by the two definite parts |
| $\tilde\Pi_\pm(\hat\mu)=\tfrac12(e_0\pm i\hat\mu)$ | The rank-one Hermitian idempotents spanning the Peirce lines |
| $\mathbb{C}(e_0\pm i\hat\mu)$ | The doubly null lines, exactly the Peirce lines |
| $S^{5}$ | The space of isotropic complex lines |

## Further Reading

- *Biquaternion Zero Divisors* (`articles_maths/biquaternion-zero-divisors.md`), for the norm cone of the zero divisors, whose intersection with the Krein null set is the doubly null lines
- *The Four Pairings of the Biquaternion Algebra* (`articles_maths/the-four-pairings-of-the-biquaternion-algebra.md`), for the comparison of the null sets and of the level sets of the four forms
- *Biquaternion Idempotents and Projections* (`articles_maths/biquaternion-idempotents-and-projections.md`), for the idempotents $\tilde\Pi_\pm(\hat\mu)$ and the minimal left and right ideals they generate
- *The Complex Bilinear Form on the Biquaternion Algebra* (`articles_maths/the-complex-bilinear-form-on-the-biquaternion-algebra.md`), for the null quadric of the complex bilinear form and its isotropic planes
- *The Six Subspaces and the Four Complex Products* (`articles_maths/the-six-subspaces-and-the-four-complex-products.md`), for the same description for the quaternion bilinear form
- *Krein Orthogonality and the Fundamental Decomposition* (`articles_maths/krein-orthogonality-and-the-fundamental-decomposition.md`), for the complements used here
- *The Krein Level Sets and the Hyperbolic Structure* (`articles_maths/the-krein-level-sets-and-the-hyperbolic-structure.md`), for the ball whose boundary is the isotropic sphere
- *Biquaternion Topology* (`articles_maths/biquaternion-topology.md`), for the projective geometry of the norm's null cone
- *Witt's Theorems* (`articles_maths/witts-theorems.md`), for the extension and transitivity theorems for forms
- János Bognár, *Indefinite Inner Product Spaces* (Springer, 1974), for isotropic subspaces, the Witt index and neutrality in a Krein space
