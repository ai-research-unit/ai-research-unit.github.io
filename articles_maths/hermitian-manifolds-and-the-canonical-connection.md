# __Hermitian Manifolds and the Canonical Connection__

## Introduction

A **Hermitian manifold** is a complex manifold with a Hermitian metric on its holomorphic tangent bundle. Its tangent bundle is a holomorphic Hermitian bundle, and it therefore carries the **canonical connection** — the Chern connection of the tangent bundle — the unique connection compatible with both the metric and the holomorphic structure. The connection has an explicit local form in a holomorphic frame, a torsion that vanishes exactly in the Kähler case, and a curvature whose trace is the Ricci form and whose class is the first Chern class of the manifold.

The article develops the canonical connection of a Hermitian manifold. It recalls the Hermitian manifold and its metric from *Hermitian Metrics and the Levi-Civita Connection*, the previous entries of this group, and the Chern connection of a holomorphic Hermitian bundle from *Hermitian Vector Bundles and the Chern Connection*; it then specialises the construction to the holomorphic tangent bundle, computes the connection coefficients $\Gamma^i_{jk} = \sum_l h^{i\bar l}\partial_j h_{k\bar l}$ in a holomorphic frame, and develops the torsion, the comparison with the Levi-Civita connection by the contorsion tensor, the curvature forms, the Ricci form $-\frac{i}{2\pi}\partial\bar\partial\log\det(h_{i\bar j})$ and the first Chern class of the manifold. It identifies the Kähler case as the case where the canonical connection is torsion-free and coincides with the Levi-Civita connection.

The article assumes the complex manifolds, the almost complex structures, the type decomposition, the Dolbeault complex and the Hermitian metrics as geometric objects of *Hermitian Geometry and Almost Complex Structures* in Part IV; the Hermitian metrics, the fundamental form and the Kähler conditions of *Hermitian Metrics and the Levi-Civita Connection*, the previous entry of this group; and the Chern connection of a holomorphic Hermitian bundle, its local form $\omega=H^{-1}\partial H$ and its curvature $\Theta=\bar\partial(H^{-1}\partial H)$ of *Hermitian Vector Bundles and the Chern Connection*. The Kähler geometry — the Kähler form, the Hodge theory, the Lefschetz theorems, the curvature and the holonomy of a Kähler manifold — is *Kähler Geometry* in Part IV. The Chern classes of the manifold and their topological meaning are *Characteristic Classes* and *Chern Classes of a Hermitian Bundle* in this category. No physics is invoked.

## The Hermitian Manifold

**Definition.** A **Hermitian manifold** is a triple $(M, J, g)$ where $M$ is a complex manifold of complex dimension $n$, $J$ is its complex structure and $g$ is a Riemannian metric that is Hermitian for $J$; equivalently, it is a complex manifold with a Hermitian metric on the holomorphic tangent bundle $T^{1,0}M$. In a **holomorphic frame** $\partial_1, \ldots, \partial_n$ of $T^{1,0}M$, over a holomorphic chart with coordinates $z^1, \ldots, z^n$, the metric is the positive-definite Hermitian matrix

$$
h_{i\bar j} = g(\partial_i, \partial_{\bar j}), \qquad h_{i\bar j} = \overline{h_{j\bar i}},
$$

and the fundamental form is $\omega = \frac{i}{2}\sum_{i,j}h_{i\bar j}\,dz^i\wedge d\bar z^j$, a real $(1,1)$-form; the Hermitian condition, the fundamental form and the Kähler conditions are those of *Hermitian Metrics and the Levi-Civita Connection* and *Hermitian Geometry and Almost Complex Structures*, and are used here without repetition.

## The Canonical Connection of the Tangent Bundle

### Existence and Uniqueness

**Theorem.** On a Hermitian manifold the holomorphic tangent bundle $T^{1,0}M$, with the Hermitian metric $h$, carries a unique connection $\nabla$ compatible with the metric and with the holomorphic structure,

$$
\nabla h = 0, \qquad \nabla^{0,1} = \bar\partial,
$$

the **canonical connection** of the Hermitian manifold; it is the Chern connection of the holomorphic Hermitian bundle $T^{1,0}M$.

*Proof.* The tangent bundle is a holomorphic Hermitian bundle, so the existence and uniqueness theorem of *Hermitian Vector Bundles and the Chern Connection* applies verbatim; the connection it produces is the canonical one. The two conditions are the bundle form of metric compatibility and of the vanishing of the $(0,1)$-part of the connection in a holomorphic frame.

### The Local Coefficients

**Theorem.** In a holomorphic frame the canonical connection has the connection form $\omega = (h^{-1}\partial h)$, that is,

$$
\nabla_{\partial_j}\partial_k = \sum_i \Gamma^i_{jk}\,\partial_i, \qquad \Gamma^i_{jk} = \sum_l h^{i\bar l}\,\partial_j h_{k\bar l},
$$

where $(h^{i\bar l})$ is the inverse matrix of $(h_{i\bar l})$; equivalently, $\omega^i_k = \sum_j \Gamma^i_{jk}\,dz^j$, and the connection is determined by the **Christoffel symbols** $\Gamma^i_{jk}$ of the Hermitian metric. The conjugate components satisfy the reality relation $\overline{\Gamma^i_{jk}} = \Gamma^{\bar i}_{\bar j\bar k}$ for the conjugate frame, and the $(0,1)$-part of the connection vanishes in the holomorphic frame.

*Proof.* This is the formula $\omega = H^{-1}\partial H$ of *Hermitian Vector Bundles and the Chern Connection*, read on the frame $\partial_1, \ldots, \partial_n$ with the matrix $H=(h_{i\bar j})$; the entries of $\omega$ are the displayed $\Gamma^i_{jk}dz^j$. The vanishing of the $(0,1)$-part in a holomorphic frame is the defining property $\nabla^{0,1}=\bar\partial$; the conjugate relation follows from the Hermitian symmetry $h_{i\bar j}=\overline{h_{j\bar i}}$ and the reality of the metric.

**Proposition.** The coefficients satisfy the analogue of the metric-compatibility equation,

$$
\partial_j h_{k\bar l} = \sum_i \Gamma^i_{jk}\,h_{i\bar l}, \qquad \partial_{\bar j}h_{k\bar l} = \sum_i \bar\Gamma^{\bar i}_{\bar j\bar l}\,h_{k\bar i},
$$

and they are the unique solution with the second relation, so the connection is determined by the first-order system.

*Proof.* Substituting $\omega = H^{-1}\partial H$ into the metric-compatibility equation $dH = \omega^*H+H\omega$ gives $\partial H = \omega H$ in the holomorphic frame, because $\omega$ is of type $(1,0)$ and the conjugate part vanishes; reading the entries gives the display. Uniqueness is the invertibility of $h$.

## Torsion and the Comparison with the Levi-Civita Connection

### The Torsion of the Canonical Connection

**Definition.** The **torsion** of the canonical connection is the tensor $T(X,Y) = \nabla_XY - \nabla_YX - [X,Y]$, a section of $\Lambda^2T^*_{\mathbb{C}}M\otimes T_{\mathbb{C}}M$ read through the type decomposition. In a holomorphic frame its holomorphic components are

$$
T^k_{ij} = \Gamma^k_{ij} - \Gamma^k_{ji},
$$

the remaining components being determined by these and the conjugate relation; and its purely antiholomorphic part vanishes, $T^{0,2} = 0$.

*Proof.* The bracket of two holomorphic coordinate fields vanishes, so $T(\partial_i,\partial_j) = \nabla_{\partial_i}\partial_j-\nabla_{\partial_j}\partial_i = \sum_k(\Gamma^k_{ij}-\Gamma^k_{ji})\partial_k$, which is the display; the conjugate components of the connection give the conjugate components of the torsion, and the vanishing of the $(0,2)$-part is the vanishing of the $(0,1)$-part of the connection in the holomorphic frame. The symmetric part of the coefficients vanishes exactly when the connection is torsion-free.

**Theorem.** The canonical connection of a Hermitian manifold is torsion-free if and only if the manifold is Kähler, and then it equals the Levi-Civita connection. In general the torsion is nonzero, consists of a $(2,0)$-part and a $(1,1)$-part, and vanishes exactly when the fundamental form is closed.

*Proof.* This is the Kähler-condition theorem of *Hermitian Metrics and the Levi-Civita Connection*, where the equivalence of the torsion-freeness of the Chern connection with the closedness of the fundamental form and with the equality $\nabla^{Ch}=\nabla^{LC}$ is proved; the present statement is the same theorem read on the tangent bundle. The components of the torsion displayed above are nonzero exactly when the coefficients are not symmetric, that is, when the metric is not Kähler.

### The Contorsion Tensor

**Proposition.** The canonical connection and the Levi-Civita connection are both metric-compatible, so their difference is a $1$-form with values in the $g$-skew endomorphisms of the tangent bundle,

$$
\nabla^{Ch}_XY = \nabla^{LC}_XY + A(X,Y), \qquad g(A(X,Y),Z) = -g(A(X,Z),Y),
$$

and the **contorsion tensor** $A$ is built from the covariant derivative $\nabla^{LC}J$ of the complex structure; it vanishes exactly in the Kähler case.

*Proof.* The difference of two metric-compatible connections is a section of $T^*M\otimes\mathfrak{so}(TM,g)$, since the metric-compatibility equations for the two connections subtract to $g(A(X,Y),Z)+g(Y,A(X,Z))=0$. The difference vanishes precisely when the Levi-Civita connection has $\nabla^{LC}J=0$, by the comparison theorem of *Hermitian Metrics and the Levi-Civita Connection*; since $A$ is the difference of two connections determined locally by the metric and $J$, it is a tensor expression in $\nabla^{LC}J$, and it vanishes with it.

## The Curvature of the Canonical Connection

### The Curvature Forms

**Theorem.** The curvature of the canonical connection is

$$
\Omega = d\omega + \omega\wedge\omega = \bar\partial\omega = \bar\partial\bigl(h^{-1}\partial h\bigr),
$$

a matrix of $(1,1)$-forms; in components,

$$
\Omega^i_j = \sum_{k,l} R^i_{j k\bar l}\,dz^k\wedge d\bar z^l, \qquad R^i_{j k\bar l} = -\partial_{\bar l}\Gamma^i_{jk},
$$

up to the ordering convention of the two terms; the curvature has no $(0,2)$-part, and it is $h$-skew-Hermitian, $\Omega^* = -\Omega$, so $\frac{i}{2\pi}\Omega$ is a matrix of Hermitian $(1,1)$-forms. The curvature satisfies the second Bianchi identity $d^\nabla\Omega = 0$.

*Proof.* The holomorphic part $\partial\omega+\omega\wedge\omega$ vanishes for the Chern connection, as computed in *Hermitian Vector Bundles and the Chern Connection*, so the curvature is the $(1,1)$-form $\bar\partial\omega$; the component form is the definition of $\bar\partial$ applied to the coefficient function $\Gamma^i_{jk}$; the skew-Hermitian property is the metric-compatibility equation differentiated, and the Bianchi identity is the general identity of *The Covariant Derivative*. The sign in the component formula is fixed by the ordering $dz^k\wedge d\bar z^l$ and the convention that $\bar\partial(dz^k)=0$.

### The Ricci Form and the First Chern Class

**Definition.** The **Ricci form** of the Hermitian metric is

$$
\rho = \frac{i}{2\pi}\operatorname{tr}\Omega = \frac{i}{2\pi}\sum_i \Omega^i_i .
$$

**Theorem.** The Ricci form is a real closed $(1,1)$-form, given in a holomorphic frame by

$$
\rho = \frac{i}{2\pi}\,\bar\partial\partial\log\det(h_{i\bar j}) = -\frac{i}{2\pi}\,\partial\bar\partial\log\det(h_{i\bar j}),
$$

and its de Rham class is the first Chern class of the manifold, $\rho = c_1(T^{1,0}M) = -c_1(K_M)$, the first Chern class of the holomorphic tangent bundle. The form is the curvature of the induced metric on the determinant line bundle $\det T^{1,0}M = K_M^*$, the anticanonical bundle.

*Proof.* The trace of the curvature of a connection on a bundle with induced connection on the determinant line bundle is the curvature of the determinant line bundle, by the identity $\operatorname{tr}\Omega = \Omega_{\det}$ of *Chern Classes of a Hermitian Bundle*; the determinant line bundle of $T^{1,0}M$ is the anticanonical bundle. The local formula is the line-bundle formula $\Theta = \bar\partial\partial\log h$ with $h = \det(h_{i\bar j})$, the metric induced on the determinant. Realness and closedness are those of the first Chern form of a Hermitian line bundle, and the class is the first Chern class of the tangent bundle by definition.

### The Kähler Case

**Corollary.** When the manifold is Kähler, the canonical connection equals the Levi-Civita connection, its curvature is the Riemann curvature tensor of the metric in the holomorphic frame, the Ricci form is $\rho = \frac{i}{2\pi}\partial\bar\partial\log\det(h_{i\bar j})$ with the Kähler symmetry $R^i_{jk\bar l} = R^k_{ji\bar l}$, and the Ricci form is the Chern representative of $c_1$. The Ricci form, the Ricci tensor and the scalar curvature of a Kähler manifold are the subject of *Kähler Geometry* in Part IV; the present article supplies the connection, its torsion and its curvature in the general Hermitian case, of which the Kähler case is the torsion-free specialisation.

**Example.** On $\mathbb{C}^n$ with the Euclidean metric, $h_{i\bar j}=\delta_{ij}$, the coefficients $\Gamma^i_{jk}$ vanish, and the canonical connection is the flat one; on the Fubini–Study metric of $\mathbb{CP}^n$ the coefficients are the standard ones and the Ricci form is $\rho = \frac{n+1}{2\pi}\,\omega_{FS}$, so the first Chern class of $\mathbb{CP}^n$ is positive and equals $(n+1)$ times the class of the hyperplane, in agreement with $c(T\mathbb{CP}^n)=(1+x)^{n+1}$ of *Characteristic Classes*.

## Summary

A Hermitian manifold is a complex manifold with a Hermitian metric on its holomorphic tangent bundle. That bundle is a holomorphic Hermitian bundle, and it carries the canonical (Chern) connection: the unique connection with $\nabla h=0$ and $\nabla^{0,1}=\bar\partial$. In a holomorphic frame the connection coefficients are $\Gamma^i_{jk}=\sum_lh^{i\bar l}\partial_jh_{k\bar l}$, determined by the metric. The torsion of the connection vanishes exactly in the Kähler case; in general it has a $(2,0)$-part and a $(1,1)$-part, its $(0,2)$-part vanishes, and the connection differs from the Levi-Civita connection by the contorsion tensor built from $\nabla^{LC}J$, which vanishes exactly when the manifold is Kähler.

The curvature of the canonical connection is $\Omega=\bar\partial(h^{-1}\partial h)$, a matrix of $(1,1)$-forms, $h$-skew-Hermitian, and its trace is the Ricci form $\rho=\frac{i}{2\pi}\operatorname{tr}\Omega=-\frac{i}{2\pi}\partial\bar\partial\log\det(h_{i\bar j})$, a real closed $(1,1)$-form whose class is the first Chern class of the manifold; it is the curvature of the induced metric on the anticanonical bundle. In the Kähler case the canonical connection is the Levi-Civita connection and the curvature is the Riemann tensor of the metric; the Kähler theory is Part IV's, and the present article is its Hermitian generalisation.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(M,J,g)$, $\dim_{\mathbb{C}}M=n$ | Hermitian manifold; complex structure and Hermitian metric |
| $T^{1,0}M$, $\partial_i,\partial_{\bar j}$ | Holomorphic tangent bundle and its frame |
| $h_{i\bar j}=g(\partial_i,\partial_{\bar j})$, $h_{i\bar j}=\overline{h_{j\bar i}}$ | Hermitian metric matrix |
| $\omega=\frac{i}{2}\sum h_{i\bar j}dz^i\wedge d\bar z^j$ | Fundamental form; $(1,1)$ |
| Canonical connection | The unique $\nabla$ with $\nabla h=0$ and $\nabla^{0,1}=\bar\partial$ |
| $\Gamma^i_{jk}=\sum_lh^{i\bar l}\partial_jh_{k\bar l}$ | Christoffel symbols of the Hermitian metric |
| $T(X,Y)=\nabla_XY-\nabla_YX-[X,Y]$ | Torsion; $T^{0,2}=0$; vanishes iff Kähler |
| $A(X,Y)$, contorsion | Difference $\nabla^{Ch}-\nabla^{LC}$, built from $\nabla^{LC}J$ |
| $\Omega=\bar\partial(h^{-1}\partial h)$ | Curvature forms; $(1,1)$ and skew-Hermitian |
| $\Omega^i_j=\sum R^i_{j k\bar l}dz^k\wedge d\bar z^l$ | Curvature components in a holomorphic frame |
| $\rho=\frac{i}{2\pi}\operatorname{tr}\Omega=-\frac{i}{2\pi}\partial\bar\partial\log\det(h_{i\bar j})$ | Ricci form; class $c_1(T^{1,0}M)$ |
| $\det T^{1,0}M=K_M^*$ | Anticanonical bundle; curvature of its metric is $\operatorname{tr}\Omega$ |

## Further Reading

- Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry*, vol. II (Interscience, 1969), for the Hermitian connection of a complex manifold, its coefficients and its torsion.
- Shiing-Shen Chern, *Complex Manifolds Without Potential Theory* (Springer, 2nd ed. 1979), for the canonical connection, the curvature and the Ricci form.
- Phillip Griffiths and Joseph Harris, *Principles of Algebraic Geometry* (Wiley, 1978), for the Hermitian metric, the Chern connection of the tangent bundle and the first Chern class.
- Fangyang Zheng, *Complex Differential Geometry* (American Mathematical Society, 2000), for the Hermitian Christoffel symbols, the torsion and the comparison with the Levi-Civita connection.
- Werner Ballmann, *Lectures on Kähler Manifolds* (European Mathematical Society, 2006), for the Kähler specialisation, the curvature identities and the Ricci form.
