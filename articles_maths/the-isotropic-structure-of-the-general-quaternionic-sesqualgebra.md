# __The Isotropic Structure of the General Quaternionic Sesqualgebra__

## Introduction

An indefinite general plain sesquilinear form has a **null set** beyond the origin, and the totally isotropic subspaces it carries are the isotropic structure of the form. For the general quaternionic sesquilinear form $\langle\tilde{Q}_2,\tilde{Q}_1\rangle_{\natural*}=\sum_{\mu}\varepsilon_{\mu}\bar Q_{1\mu}Q_{2\mu}$ the null set is the real quadric $\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=0$ of dimension $7$, and its maximal totally isotropic subspaces have dimension the **Witt index** $\min(n,m)$, that is $1$ over $\mathbb{C}$ and $2$ over $\mathbb{R}$. This article treats that structure: the isotropic elements, the totally isotropic subspaces, and the isotropic lines. The comparison with the *other* null set of the algebra, the zero-divisor cone of the norm $\langle\cdot\rangle_{\natural}$, is *The Four Forms and the Four Algebraic Norms*, §*What the Four Forms Separate*. The orthogonality and the subspaces are in *Krein Orthogonality and the Fundamental Decomposition*; the value-one sets of positive and negative sign are in *The Krein Level Sets and the Hyperbolic Structure*; and the projective geometry of the norm's cone is in *The Null Quadric and Its Projective Geometry*.

## Isotropic Elements

**Definition.** An element $\tilde{Q}$ is **Krein-isotropic**, or **Krein-null**, when $\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=0$; the **Krein null set** is

$$
\mathcal{K}=\{\tilde{Q}:\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=0\}=\Bigl\{\tilde{Q}:\sum_{\mu}\varepsilon_{\mu}|Q_{\mu}|^{2}=0\Bigr\}.
$$

**Theorem (the shape of the null set).** In the splitting $\tilde{Q}=c+v$ of the algebra into its centre and vector parts, with $c\in\mathbb{C}_{\mathbb{B}}$ the scalar part and $v\in\mathbb{V}_{\mathbb{B}}$ the vector part,

$$
\boxed{\; \mathcal{K}=\{\tilde{Q}:\|c\|_E=\|v\|_E\} \;};
$$

it is a real algebraic cone with apex the origin, homogeneous of degree two; its dimension and its singular point are *The Krein Level Sets and the Hyperbolic Structure*.

**Proof.** $\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=\|c\|_E^{2}-\|v\|_E^{2}$ by the sign vector of the coefficient basis, so the equation is $\|c\|_E=\|v\|_E$. The dimension of the cone, its singular point and its description at each radius are *The Krein Level Sets and the Hyperbolic Structure*.

**Example.** $e_t+\vec e_x$ has $\langle e_t+\vec e_x,e_t+\vec e_x\rangle_{\natural*}=1-1=0$ and $\langle\cdot\rangle_{\natural}=2$, so it is isotropic for the general quaternionic sesquilinear form and not for the norm. The element $\vec e_x+i\vec e_y$ has $\langle\cdot\rangle_{\natural}=1+i^{2}=0$ and $\langle \vec e_x+i\vec e_y,\vec e_x+i\vec e_y\rangle_{\natural*}=-2$, the reverse situation.

## Totally Isotropic Subspaces

**Definition.** A subspace $\mathbb{W}$ is **totally isotropic** when $\langle\tilde{Q}_2,\tilde{Q}_1\rangle_{\natural*}=0$ for all $\tilde{Q}_1,\tilde{Q}_2\in\mathbb{W}$, equivalently when $\mathbb{W}\subseteq\mathbb{W}^{\perp_{K}}$; it is **maximal** when it is contained in no larger one. The **Witt index** of the general quaternionic sesquilinear form is the common dimension of the maximal totally isotropic subspaces.

**Theorem (the Witt index and the maximal isotropic subspaces).** The Witt index is $\min(n,m)$: it is $1$ over $\mathbb{C}$ and $2$ over $\mathbb{R}$. A maximal totally isotropic complex subspace is $\mathbb{C}(e_t+\vec e_x)$, and a maximal totally isotropic real subspace is the plane

$$
\boxed{\; \mathbb{W}_{\mathrm{iso}}=\mathrm{span}_{\mathbb{R}}\{e_t+\vec e_x,\ i(e_t+\vec e_x)\},
\qquad
e_t+\vec e_x\ \text{and}\ i(e_t+\vec e_x)\ \text{isotropic, mutually orthogonal} \;}.
$$

Every totally isotropic subspace is contained in a maximal one, and the automorphism group $\mathrm{U}(1,3)$ acts transitively on the maximal ones.

**Proof.** If $\mathbb{W}$ is totally isotropic then it is orthogonal to itself, so $\mathbb{W}\subseteq\mathbb{W}^{\perp_{K}}$, and the restriction of the form to $\mathbb{W}+\mathbb{W}^{\perp_{K}}/\mathbb{W}^{\perp_{K}}$ makes the dimension of $\mathbb{W}$ at most $\min(n,m)$: an isotropic subspace meets the maximal positive definite subspaces and the maximal negative definite subspaces only at $0$. The two displayed spaces attain $\min(n,m)=1$ over $\mathbb{C}$ and $\min(n,m)=2$ over $\mathbb{R}$, since $\langle e_t+\vec e_x,e_t+\vec e_x\rangle_{\natural*}=0$, $\langle i(e_t+\vec e_x),e_t+\vec e_x\rangle_{\natural*}=i-i=0$ and the plane is $2$-dimensional over $\mathbb{R}$. The extension and transitivity are Witt's extension theorem for general plain sesquilinear forms (*Witt's Theorems*).

**Remark (the isotropic and the null elements).** An element $\tilde{Q}$ is isotropic exactly when the line $\mathbb{C}\tilde{Q}$ is totally isotropic (over $\mathbb{R}$, the real plane $\mathrm{span}_{\mathbb{R}}\{\tilde{Q},i\tilde{Q}\}$ is); the null set of the first section is the union of the totally isotropic complex lines, and the totally isotropic subspaces are the subspaces all of whose elements are isotropic.

## The Index in Two Ways

The index is $1$ over $\mathbb{C}$ and $2$ over $\mathbb{R}$, and it can be computed twice: bounded by the two definite parts, and exhibited by the isotropic lines that are also norm-null.

**Theorem (the index by a maximal definite subspace).** A definite subspace meets a totally isotropic subspace only at the origin. Hence a totally isotropic subspace $\mathbb{W}$ maps injectively into the two quotients $\mathbb{B}/\mathbb{W}_{-}$ and $\mathbb{B}/\mathbb{W}_{+}$, for every maximal negative definite subspace $\mathbb{W}_{-}$ and every maximal positive definite subspace $\mathbb{W}_{+}$, and

$$
\boxed{\; \dim_{\mathbb{C}}\mathbb{W}\leq\dim_{\mathbb{C}}\bigl(\mathbb{B}/\mathbb{W}_{-}\bigr)=n,\qquad
\dim_{\mathbb{C}}\mathbb{W}\leq\dim_{\mathbb{C}}\bigl(\mathbb{B}/\mathbb{W}_{+}\bigr)=m \;}.
$$

Therefore the Witt index is at most $\min(n,m)$, and the bound is attained.

**Proof.** A nonzero element of a definite subspace has a nonzero square, so it is not isotropic and cannot lie in the totally isotropic $\mathbb{W}$; the projection is therefore injective. The dimensions are $\dim\mathbb{B}-\dim\mathbb{W}_{-}=4-3=1=n$ and $\dim\mathbb{B}-\dim\mathbb{W}_{+}=4-1=3=m$. The bound $\min(n,m)=1$ over $\mathbb{C}$ is attained by the line $\mathbb{C}(e_t+\vec e_x)$, and over $\mathbb{R}$, where the bound is $2$, by the plane $\mathrm{span}_{\mathbb{R}}\{e_t+\vec e_x,i(e_t+\vec e_x)\}$.

**Definition.** A **doubly null line** is an isotropic line that lies in the norm cone as well: a complex line $\mathbb{C}\tilde{Q}$ with $\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=0$ and $\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=0$.

**Theorem (the Peirce lines).** For every real unit vector $\vec u\in\mathbb{V}_{\mathbb{B}}$, with $\tilde\Xi=i\vec u$, the element

$$
\tilde\Pi_\pm(\tilde\Xi)=\tfrac12\bigl(e_t\pm \tilde\Xi\bigr)
$$

is a rank-one Hermitian idempotent, $\tilde\Pi_\pm^2=\tilde\Pi_\pm$, $\tilde\Pi_\pm^{*}=\tilde\Pi_\pm$, with $\langle\tilde\Pi_\pm\rangle_{\natural}=0$ and $\langle\tilde\Pi_\pm,\tilde\Pi_\pm\rangle_{\natural*}=0$. The line $\mathbb{C}\tilde\Pi_\pm(\tilde\Xi)$ is therefore a maximal totally isotropic complex subspace and a doubly null line; it is a **Peirce line** of the algebra, generating the minimal left ideal $\mathbb{B}\tilde\Pi_\pm(\tilde\Xi)$ and the minimal right ideal $\tilde\Pi_\pm(\tilde\Xi)\mathbb{B}$, of complex dimension two, every element of which is a zero divisor. The two diagonal members $\vec u=\vec e_x$ give the lines $\mathbb{C}(e_t\pm i\vec e_x)$, the two distinguished doubly null lines.

**Proof.** A real unit vector has $\vec u^2=-e_t$, so $(\tilde\Xi)^2=e_t$ and $(e_t\pm \tilde\Xi)^2=1\pm2\tilde\Xi+(\tilde\Xi)^2=2(e_t\pm \tilde\Xi)$, whence $\tilde\Pi_\pm^2=\tilde\Pi_\pm$; $\tilde\Pi_\pm$ is Hermitian because $(\tilde\Xi)^{*}=\tilde\Xi$. For the two squares, $\langle e_t\pm \tilde\Xi\rangle_{\natural}=1+\langle\tilde\Xi\rangle_{\natural}=1-\|\vec u\|_E^2=0$ and $\langle e_t\pm \tilde\Xi,e_t\pm \tilde\Xi\rangle_{\natural*}=1-\|\tilde\Xi\|_E^2=0$. The minimal ideals are the standard ones of the algebra, of complex dimension two, and their elements $X\tilde\Pi_\pm$ satisfy $\langle X\tilde\Pi_\pm\rangle_{\natural}=\langle X\rangle_{\natural}\langle\tilde\Pi_\pm\rangle_{\natural}=0$.

**Corollary (the two descriptions agree on the norm cone).** The Peirce lines are exactly the doubly null lines. Writing $\tilde Q_3=\tilde S+i\tilde W$ with $\tilde S,\tilde W\in\mathbb{V}_{\mathbb{B}}$ real, the conditions $\|\tilde Q_3\|_E=1$ and $\langle\tilde Q_3\rangle_{\natural}=-1$ read

$$
\|\tilde S\|_E^{2}+\|\tilde W\|_E^{2}=1,\qquad
\|\tilde S\|_E^{2}-\|\tilde W\|_E^{2}=-1,\qquad
\langle\tilde S,\tilde W\rangle=0,
$$

which force $\tilde S=0$ and $\|\tilde W\|_E=1$: the doubly null lines are exactly the lines $\mathbb{C}(e_t\pm \tilde\Xi)$, parametrised by the real unit directions with the two signs, and the Peirce description is complete on the norm cone. The maximal totally isotropic *real* subspace is, by contrast, the plane $\mathrm{span}_{\mathbb{R}}\{e_t+\vec e_x,i(e_t+\vec e_x)\}$, whose generator has $\langle\cdot\rangle_{\natural}=2$ and is not a zero divisor, so it is not a Peirce line; within the real form $\mathbb{H}_{\mathbb{B}}$, whose form is the interval form in the basis $e_t,\vec e_x,\vec e_y,\vec e_z$, the maximal totally isotropic subspace is the diagonal light line $\mathrm{span}_{\mathbb{R}}\{e_t+\vec e_x\}$, and the Peirce lines are the complementary, norm-null part of the isotropic lines.

**Proof.** The three equations are the real and imaginary parts of $\langle\tilde Q_3\rangle_{\natural}=-1$ together with $\|\tilde Q_3\|_E=1$, using $\langle\tilde S+i\tilde W\rangle_{\natural}=\|\tilde S\|_E^{2}-\|\tilde W\|_E^{2}+2i\langle\tilde S,\tilde W\rangle$ and $\|\tilde S+i\tilde W\|_E^{2}=\|\tilde S\|_E^{2}+\|\tilde W\|_E^{2}$; adding and subtracting the first two give $\|\tilde S\|_E^{2}=0$ and $\|\tilde W\|_E^{2}=1$. The remaining statements are the previous definition and corollary.

## The Isotropic Lines

**Definition.** The **isotropic lines** of $\mathbb{C}^{4}$ for the general quaternionic sesquilinear form are the complex lines $\mathbb{C}\tilde{Q}$ spanned by nonzero isotropic elements.

The isotropic lines are exactly the lines $\mathbb{C}(e_t+\tilde Q_3)$ with $\|\tilde Q_3\|_E=1$, the boundary case of the parametrisation of the maximal positive definite subspaces in *Krein Orthogonality and the Fundamental Decomposition*, which uses the set $\|\tilde Q_3\|_E<1$. Their identification with the norm-one set of $\mathbb{V}_{\mathbb{B}}$ is *The Krein Level Sets and the Hyperbolic Structure*.

## Worked Examples

**An isotropic element of the centre–vector type.** $\tilde{Q}=e_t+\vec e_x$: isotropic, norm $2$, in the null cone of the real quaternion slice at the boundary.

**A zero divisor that is isotropic.** $\tilde{Q}=e_t+i\vec e_x$: both $\langle\cdot\rangle_{\natural}=0$ and $\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=0$; the line it spans is a doubly null line.

**A zero divisor that is not isotropic.** $\tilde{Q}=\vec e_x+i\vec e_y$: $\langle\cdot\rangle_{\natural}=0$, $\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=-2$, a strictly negative element.

**A timelike element.** $\tilde{Q}=e_t+\tfrac12\vec e_x$: $\langle\tilde{Q},\,\tilde{Q}\rangle_{\natural*}=\tfrac34>0$, so it lies inside the positive region and spans a maximal positive definite line.

**A maximal isotropic plane.** $\mathbb{W}_{\mathrm{iso}}=\mathrm{span}_{\mathbb{R}}\{e_t+\vec e_x,\ i(e_t+\vec e_x)\}$: real dimension $2$, over $\mathbb{C}$ it is the single line $\mathbb{C}(e_t+\vec e_x)$, and it is maximal because the Witt index over $\mathbb{R}$ is $2$.

**A Peirce line.** $\vec u=\vec e_y$: $\tilde\Pi_+=\tfrac12(e_t+i\vec e_y)$ is a rank-one Hermitian idempotent with $\langle\cdot\rangle_{\natural}=0$ and $\langle\tilde\Pi_+,\tilde\Pi_+\rangle_{\natural*}=0$, so the line $\mathbb{C}(e_t+i\vec e_y)=\mathbb{C}\tilde\Pi_+$ is a doubly null maximal isotropic line, a Peirce line.

**A maximal isotropic line that is not Peirce.** $\mathbb{C}(e_t+\vec e_x)$: the generator has $\langle\cdot\rangle_{\natural}=2$, so the line is isotropic and not doubly null; it is the complexification of the diagonal light line of the real form $\mathbb{H}_{\mathbb{B}}$, and it exhausts the index over $\mathbb{C}$ without lying in the norm cone.

## Summary

The Krein null set is $\mathcal{K}=\{\|c\|_E=\|v\|_E\}$, a real algebraic cone of dimension $7$, whose only singular point is the apex. It meets the complex norm cone of the zero divisors in the union of the doubly null lines, a cone of real dimension $4$ that contains $\mathbb{C}(e_t\pm i\vec e_x)$; the comparison of the two cones is *The Four Forms and the Four Algebraic Norms*, §*What the Four Forms Separate*. A totally isotropic subspace is one contained in its own Krein-orthogonal complement; the Witt index is $\min(n,m)$, that is $1$ over $\mathbb{C}$ and $2$ over $\mathbb{R}$; a maximal isotropic complex subspace is the line $\mathbb{C}(e_t+\vec e_x)$, a maximal isotropic real subspace is the plane it spans with $i(e_t+\vec e_x)$; every isotropic subspace extends to a maximal one and the automorphism group acts transitively on the maximal ones. The isotropic complex lines are parametrised by the norm-one set $\{\|\tilde Q_3\|_E=1\}$ of the vector subspace, on which each line is met exactly once; the topology of this set is *The Euclidean Topology of the Biquaternion Algebra*. The index is computed twice: bounded by the two definite parts, a totally isotropic subspace injecting into the quotient by either, and exhibited by the **Peirce lines** generated by the rank-one Hermitian idempotents $\tilde\Pi_\pm(\tilde\Xi)=\tfrac12(e_t\pm \tilde\Xi)$; these are exactly the doubly null lines, the isotropic lines that lie in the norm cone, while the maximal isotropic real plane is not a Peirce line, its generator being a non-zero-divisor.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{K}=\{\tilde{Q}:\langle\tilde{Q},\tilde{Q}\rangle_{\natural*}=0\}=\{\lVert c\rVert_E=\lVert v\rVert_E\}$ | The Krein null set |
| $\mathcal{N}=\{\langle\tilde{Q},\tilde{Q}\rangle_{\natural}=0\}$ | The norm cone of the zero divisors |
| $\mathbb{C}(e_t\pm i\vec e_x)$ | Doubly null isotropic lines |
| $\min(n,m)=1$ over $\mathbb{C}$, $2$ over $\mathbb{R}$ | The Witt index |
| $\mathbb{W}_{\mathrm{iso}}=\mathrm{span}_{\mathbb{R}}\{e_t+\vec e_x,i(e_t+\vec e_x)\}$ | The maximal isotropic real plane |
| $\mathbb{W}\subseteq\mathbb{W}^{\perp_{K}}$ | Totally isotropic subspace |
| $\dim_{\mathbb{C}}\mathbb{W}\le\min(n,m)$ | The index bound by the two definite parts |
| $\tilde\Pi_\pm(\tilde\Xi)=\tfrac12(e_t\pm \tilde\Xi)$ | The rank-one Hermitian idempotents spanning the Peirce lines |
| $\mathbb{C}(e_t\pm \tilde\Xi)$ | The doubly null lines, exactly the Peirce lines |
| $\{\lVert\tilde Q_3\rVert_E=1\}$ | the norm-one set parametrising the isotropic complex lines |

## Further Reading

- [Norm Regularity and Degeneracy in the Biquaternion Algebra](norm-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the norm cone of the zero divisors, whose intersection with the Krein null set is the doubly null lines
- [The Four Forms and the Four Algebraic Norms](the-four-forms-and-the-four-algebraic-norms.html), for the four forms and their four null sets, and for the null quadric of the general plain bilinear form with its hyperbolic planes
- [Square Roots of One and the Idempotents of the Biquaternion Algebra](square-roots-of-one-and-the-idempotents-of-the-biquaternion-algebra.html), for the idempotents $\tilde\Pi_\pm(\tilde\Xi)$ and the minimal left and right ideals they generate
- [Remarkable Subspaces and the Four General Products](remarkable-subspaces-and-the-four-general-products.html), for the same description for the general quaternionic bilinear form
- [Krein Orthogonality and the Fundamental Decomposition](krein-orthogonality-and-the-fundamental-decomposition.html), for the complements used here
- [The Krein Level Sets and the Hyperbolic Structure](the-krein-level-sets-and-the-hyperbolic-structure.html), for the ball whose boundary is the isotropic sphere
- [The Null Quadric and Its Projective Geometry](the-null-quadric-and-its-projective-geometry.html), for the projective geometry of the form's null cone
- [Witt's Theorems](witts-theorems.html), for the extension and transitivity theorems for forms
- János Bognár, *Indefinite Inner Product Spaces* (Springer, 1974), for isotropic subspaces, the Witt index and neutrality in a Krein space
