# __The Flat Kähler Structure of $\mathbb{C}^2$__

## Introduction

The space $\mathbb{C}^2$ carries a canonical Hermitian metric, the Euclidean metric read in complex coordinates, and its associated Kähler form. The metric is flat: its curvature tensor vanishes identically, its geodesics are the real lines, and its exponential map is the identity. **The flat Kähler structure is the model of a Kähler manifold of zero curvature**, in the same way that the ball is the model of a negatively curved one and the projective plane of a positively curved one.

This article treats the Hermitian metric and the Kähler form, the complex structure $J$ and the relation among the Hermitian, bilinear and Kähler forms, the flatness and the vanishing of the curvature, the group of holomorphic isometries, and the Kähler potential. The canonical forms themselves are *The Three Canonical Forms on $\mathbb{C}^2$*; the realification is *The Realification of $\mathbb{C}^2$*; the moduli of domains and the negatively curved model are *The Ball and the Bicylinder in $\mathbb{C}^2$*; the Hénon maps of the last article of the category are polynomial automorphisms that do not preserve the metric.

**The flat Kähler structure is the Euclidean structure of $\mathbb{R}^4$ together with the complex structure $J$.** The metric is the real part of the Hermitian form, the Kähler form is minus its imaginary part, and $J$ is parallel. The holomorphic isometries are the translations and the unitary group, $\mathbb{C}^2\rtimes\mathrm{U}(2)$, and not the unitary group alone.

## The Hermitian Metric and the Kähler Form

**The Hermitian metric is $h=dQ_{\blacktriangle}\otimes d\overline{Q}_{\blacktriangle}+dQ_{\blacktriangledown}\otimes d\overline{Q}_{\blacktriangledown}$; its real part is the Euclidean metric and its imaginary part is minus the Kähler form, a closed and nondegenerate $2$-form.**

**Definition.** The **Hermitian metric** on $\mathbb{C}^2$ is
$$
h=dQ_{\blacktriangle}\otimes d\overline{Q}_{\blacktriangle}+dQ_{\blacktriangledown}\otimes d\overline{Q}_{\blacktriangledown},
$$
and its real and imaginary parts are
$$
g=\operatorname{Re}h=dq_{\blacktriangle}^2+dq'^2_{\blacktriangle}+dq_{\blacktriangledown}^2+dq'^2_{\blacktriangledown},\qquad
\Omega=-\operatorname{Im}h=\frac{i}{2}\left(dQ_{\blacktriangle}\wedge d\overline{Q}_{\blacktriangle}+dQ_{\blacktriangledown}\wedge d\overline{Q}_{\blacktriangledown}\right).
$$
The form $\Omega$ is the **Kähler form** of the flat metric.

**Proposition (the three readings).** The form $g$ is a Riemannian metric of signature $(4,0)$; the form $\Omega$ is a symplectic form; and
$$
\Omega=dq_{\blacktriangle}\wedge dq'_{\blacktriangle}+dq_{\blacktriangledown}\wedge dq'_{\blacktriangledown},
\qquad
\Omega(X,Y)=g(JX,Y)
$$
for real vector fields $X,Y$. In particular $\Omega$ is nondegenerate and $J$ is an isometry of $g$.

*Proof.* In real coordinates, $\frac{i}{2}dQ_{\blacktriangle}\wedge d\overline{Q}_{\blacktriangle}=dq_{\blacktriangle}\wedge dq'_{\blacktriangle}$, and the same with the descending triangle, so $\Omega$ is the standard symplectic form of $\mathbb{R}^4$. The identity $\Omega(X,Y)=g(JX,Y)$ is checked on the basis: $J\partial_{q_{\blacktriangle}}=\partial_{q'_{\blacktriangle}}$, $J\partial_{q'_{\blacktriangle}}=-\partial_{q_{\blacktriangle}}$, and $g(\partial_{q_{\blacktriangle}},\partial_{q'_{\blacktriangle}})=0$, $g(J\partial_{q_{\blacktriangle}},\partial_{q'_{\blacktriangle}})=1$. The metric is positive definite and $g(JX,JY)=g(X,Y)$.

**Theorem (the Kähler condition).** The form $\Omega$ is closed, $d\Omega=0$, and the metric is Kähler. The complex structure $J$ is parallel, $\nabla J=0$, for the Levi-Civita connection of $g$.

*Proof.* The form $\Omega$ has constant coefficients, so $d\Omega=0$. The connection of a flat metric has zero Christoffel symbols in the linear coordinates, so $\nabla J=0$ because $J$ is a constant matrix.

**Remark (the orientation).** The volume form is
$$
\frac{\Omega^2}{2!}=dq_{\blacktriangle}\wedge dq'_{\blacktriangle}\wedge dq_{\blacktriangledown}\wedge dq'_{\blacktriangledown},
$$
the Lebesgue volume of $\mathbb{R}^4$. **The Kähler form is the area form of the complex lines**: its restriction to a complex line is the Euclidean area form of that plane, with the orientation given by $J$.

## The Complex Structure and the Forms

**The Hermitian form $H$, the bilinear form $B$ and the Kähler form $\Omega$ are three readings of the same metric data; $H=g-i\Omega$ on real vectors, and $B$ is $H$ composed with the conjugation of the second variable. The holomorphic symplectic form $\omega=dQ_{\blacktriangle}\wedge dQ_{\blacktriangledown}$ is a fourth form, treated in *The Three Canonical Forms on $\mathbb{C}^2$*.**

**Definition.** On $\mathbb{C}^2$,
$$
H(Q_1,Q_2)=Q_{1\blacktriangle}\overline{Q_{2\blacktriangle}}+Q_{1\blacktriangledown}\overline{Q_{2\blacktriangledown}},\qquad
B(Q_1,Q_2)=Q_{1\blacktriangle}Q_{2\blacktriangle}+Q_{1\blacktriangledown}Q_{2\blacktriangledown},\qquad
\Omega(X,Y)=g(JX,Y).
$$

**Proposition (the relation among the forms).** For real vectors $Q_1,Q_2\in\mathbb{C}^2\cong\mathbb{R}^4$,
$$
H(Q_1,Q_2)=g(Q_1,Q_2)+i\operatorname{Im}H(Q_1,Q_2)=g(Q_1,Q_2)-i\,\Omega(Q_1,Q_2),
$$
and
$$
B(Q_1,Q_2)=H(Q_1,\overline{Q_2}).
$$
The form $B$ is complex bilinear and symmetric; the form $H$ is Hermitian; the form $\Omega$ is real and alternating.

*Proof.* The real part of $H$ is $g$ by definition, and the imaginary part is $-\Omega$ by the computation of the previous section. The identity $B(Q_1,Q_2)=H(Q_1,\overline{Q_2})$ is the definition of $B$ and the fact that $\overline{\bar w_k}=w_k$.

**Remark (the signatures).** The real part of $B$ is the symmetric form
$$
\operatorname{Re}B(Q_1,Q_2)=q_{\blacktriangle}u_{\blacktriangle}-q'_{\blacktriangle}v_{\blacktriangle}+q_{\blacktriangledown}u_{\blacktriangledown}-q'_{\blacktriangledown}v_{\blacktriangledown},
$$
of signature $(2,2)$; the imaginary part is the symmetric form
$$
\operatorname{Im}B(Q_1,Q_2)=q_{\blacktriangle}v_{\blacktriangle}+q'_{\blacktriangle}u_{\blacktriangle}+q_{\blacktriangledown}v_{\blacktriangledown}+q'_{\blacktriangledown}u_{\blacktriangledown},
$$
also of signature $(2,2)$. **The form $B$ is the complexification of the split-complex norm**, and its isotropic cone is treated in *The Isotropic Cone of the Bilinear Form on $\mathbb{C}^2$*. The Kähler form $\Omega$ is nondegenerate on every complex line, and its sign is the orientation of the line.

**Remark (the two almost-complex structures).** The complex structure $J$ is compatible with $g$ and with $\Omega$; the form $B$ is $\mathbb{C}$-bilinear and satisfies
$$
B(JQ_1,JQ_2)=-B(Q_1,Q_2),
$$
so it is $J$-anti-invariant. **The three forms $H$, $B$ and $\Omega$ are not independent data**: $g$ and $\Omega$ determine each other through $J$, and $B$ is the holomorphic reading of $H$; the holomorphic symplectic form is $\omega=dQ_{\blacktriangle}\wedge dQ_{\blacktriangledown}$.

## Flatness and Curvature

**The metric is flat: the curvature tensor vanishes, the geodesics are the real lines, the exponential map is the identity, and every curvature invariant is zero.**

**Theorem (zero curvature).** The Riemann curvature tensor of $g$ vanishes identically, and so do the Ricci tensor, the scalar curvature and the holomorphic sectional curvature. The geodesics are the affine real lines $t\mapsto a+tv$, and the exponential map at every point is the identity in the linear coordinates.

*Proof.* In the linear coordinates $(q_{\blacktriangle},q'_{\blacktriangle},q_{\blacktriangledown},q'_{\blacktriangledown})$ the metric has constant coefficients, so the Christoffel symbols vanish, the curvature tensor is zero, and the geodesic equation is $\ddot x=0$. The exponential map is the identity because the geodesics are straight lines.

**Corollary (the model).** Every complete simply connected flat Kähler manifold of complex dimension $2$ is isometric to $\mathbb{C}^2$ with the flat metric.

*Proof.* A complete simply connected flat Riemannian manifold is isometric to $\mathbb{R}^4$ with the Euclidean metric; a Kähler structure is an orthogonal complex structure, and the orthogonal complex structures on $\mathbb{R}^4$ are all conjugate to the standard one by an orthogonal map.

**Remark (the contrast with the ball).** The ball of *The Ball and the Bicylinder in $\mathbb{C}^2$* has constant negative holomorphic sectional curvature and a nontrivial curvature tensor; the flat space has zero curvature and a trivial holonomy group. **The two are the extreme cases of the sign of the curvature**, and the compact quotients of the flat space are the complex tori, while the compact quotients of the ball are the compact complex hyperbolic manifolds.

**Remark (the holonomy).** The holonomy group of the flat metric is trivial, because the connection is the trivial connection in the linear frame. **A nontrivial flat Kähler manifold has a holonomy representation of its fundamental group in $\mathrm{U}(2)$**, and the compact quotients of the flat space are the complex tori; a flat Kähler metric on a torus is a constant Hermitian form.

## The Holomorphic Isometries

**The holomorphic isometries of the flat metric are the affine maps $Q\mapsto AQ+Q_0$ with $A\in\mathrm{U}(2)$; they form the group $\mathbb{C}^2\rtimes\mathrm{U}(2)$ of real dimension $8$.**

**Theorem (the isometry group).** Every holomorphic isometry of $\mathbb{C}^2$ with the flat metric is of the form
$$
Q\longmapsto AQ+Q_0,\qquad A\in\mathrm{U}(2),\ Q_0\in\mathbb{C}^2.
$$
The group is the semidirect product $\mathbb{C}^2\rtimes\mathrm{U}(2)$, of real dimension $4+4=8$.

*Proof.* An isometry of $\mathbb{R}^4$ is affine, $Q\mapsto AQ+Q_0$ with $A\in\mathrm{O}(4)$; it is holomorphic exactly when $A$ commutes with $J$, that is, when $A\in\mathrm{O}(4)\cap\mathrm{GL}_2(\mathbb{C})=\mathrm{U}(2)$. The translations form the normal subgroup $\mathbb{C}^2$, and the linear parts form $\mathrm{U}(2)$.

**Corollary (the full isometry group).** The isometry group of the flat metric, without the holomorphic condition, is $\mathbb{C}^2\rtimes\mathrm{O}(4)$, of real dimension $4+6=10$; the holomorphic isometries form the subgroup $\mathbb{C}^2\rtimes\mathrm{U}(2)$, of codimension two.

*Proof.* The linear part of an isometry of $\mathbb{R}^4$ is any orthogonal matrix; the holomorphic condition is the commutation with $J$, which cuts $\mathrm{O}(4)$ down to $\mathrm{U}(2)$.

**Remark (the translations are not optional).** The group $\mathrm{U}(2)$ alone does not act transitively on $\mathbb{C}^2$; the translations are needed to reach every point. **The full group of biholomorphisms of $\mathbb{C}^2$ is much larger than the isometry group**: the affine group $\mathbb{C}^2\rtimes\mathrm{GL}_2(\mathbb{C})$ acts by biholomorphisms but not by isometries unless the linear part is unitary, and the polynomial and non-polynomial automorphisms of *The Affine and Polynomial Automorphisms of $\mathbb{C}^2$* are larger still.

**Remark (the stabiliser).** The stabiliser of the origin in the holomorphic isometry group is $\mathrm{U}(2)$, of dimension $4$; the stabiliser of a point in the full isometry group is $\mathrm{O}(4)$, of dimension $6$. **The homogeneous space is $\mathbb{C}^2\cong(\mathbb{C}^2\rtimes\mathrm{U}(2))/\mathrm{U}(2)$**, and the isotropy representation is the standard representation of $\mathrm{U}(2)$.

## The Kähler Potential and the Canonical Form

**The flat Kähler form has the global potential $\varphi=\frac12\lVert Q\rVert^2$, and the metric is the Hessian of $\varphi$; the canonical bundle is trivial and the space is Calabi–Yau.**

**Proposition (the potential).** The function
$$
\varphi(Q)=\frac12\lVert Q\rVert^2=\frac12\left(\lvert Q_{\blacktriangle}\rvert^2+\lvert Q_{\blacktriangledown}\rvert^2\right)
$$
satisfies
$$
\Omega=i\,\partial\bar\partial\varphi.
$$
Conversely, every Kähler potential of the flat form differs from $\varphi$ by a pluriharmonic function.

*Proof.* The mixed second derivatives of $\varphi$ are $\partial^2\varphi/\partial Q_{\blacktriangle}\partial\overline{Q}_{\blacktriangle}=\partial^2\varphi/\partial Q_{\blacktriangledown}\partial\overline{Q}_{\blacktriangledown}=\frac12$ and the mixed ones vanish, so $i\partial\bar\partial\varphi=\frac{i}{2}(dQ_{\blacktriangle}\wedge d\overline{Q}_{\blacktriangle}+dQ_{\blacktriangledown}\wedge d\overline{Q}_{\blacktriangledown})=\Omega$. If $\varphi'$ is another potential, then $\partial\bar\partial(\varphi'-\varphi)=0$, so $\varphi'-\varphi$ is pluriharmonic.

**Proposition (the metric as a Hessian).** In the real coordinates, the metric is the Hessian of $\frac12\lVert Q\rVert^2$, and the Kähler form is the associated $(1,1)$-form. The form $\Omega$ is parallel for the Levi-Civita connection, and the pair $(g,\Omega)$ is a Kähler structure.

*Proof.* The Hessian of a quadratic form is the constant form itself; the association is the one of the previous proposition.

**Remark (the canonical bundle).** The holomorphic volume form
$$
\omega=dQ_{\blacktriangle}\wedge dQ_{\blacktriangledown}
$$
is parallel and nowhere vanishing, so the canonical bundle of $\mathbb{C}^2$ is trivial. **The flat Kähler metric is Ricci-flat and the space is a (noncompact) Calabi–Yau manifold of complex dimension $2$**; the form $\omega$ is the holomorphic symplectic form of *The Three Canonical Forms on $\mathbb{C}^2$*, and it is preserved by every holomorphic map with Jacobian determinant $1$.

**Remark (the Fubini–Study comparison).** The projective compactification of *The Compactifications of $\mathbb{C}^2$* carries the Fubini–Study metric, whose restriction to the affine chart is not the flat metric: the Fubini–Study metric has positive curvature and the flat metric has zero curvature. **The flat metric is the limit of the rescalings of the Fubini–Study metric near a point**, and the two agree to first order at the origin.

## Summary

The flat Kähler structure of $\mathbb{C}^2$ is the Euclidean metric $g=dq_{\blacktriangle}^2+dq'^2_{\blacktriangle}+dq_{\blacktriangledown}^2+dq'^2_{\blacktriangledown}$ together with the complex structure $J$ and the Kähler form $\Omega=\frac{i}{2}(dQ_{\blacktriangle}\wedge d\overline{Q}_{\blacktriangle}+dQ_{\blacktriangledown}\wedge d\overline{Q}_{\blacktriangledown})=dq_{\blacktriangle}\wedge dq'_{\blacktriangle}+dq_{\blacktriangledown}\wedge dq'_{\blacktriangledown}$. The Hermitian form is $H=g-i\Omega$ on real vectors, the bilinear form is $B(Q_1,Q_2)=H(Q_1,\overline{Q_2})$, and $\Omega(X,Y)=g(JX,Y)$. The metric is flat: the curvature tensor, the Ricci tensor, the scalar curvature and the holomorphic sectional curvature vanish, the geodesics are the real lines and the exponential map is the identity.

The holomorphic isometries are the affine maps $Q\mapsto AQ+Q_0$ with $A\in\mathrm{U}(2)$, forming $\mathbb{C}^2\rtimes\mathrm{U}(2)$ of real dimension $8$; the full isometry group is $\mathbb{C}^2\rtimes\mathrm{O}(4)$ of dimension $10$. The Kähler form has the global potential $\frac12\lVert Q\rVert^2$, the canonical bundle is trivial, and the space is a noncompact Calabi–Yau manifold. The flat structure is the zero-curvature model of a Kähler surface, and its compact quotients are the complex tori.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $h=dQ_{\blacktriangle}\otimes d\overline{Q}_{\blacktriangle}+dQ_{\blacktriangledown}\otimes d\overline{Q}_{\blacktriangledown}$ | the Hermitian metric |
| $g=\operatorname{Re}h$ | the Euclidean metric of $\mathbb{R}^4$ |
| $\Omega=-\operatorname{Im}h=\frac{i}{2}(dQ_{\blacktriangle}\wedge d\overline{Q}_{\blacktriangle}+dQ_{\blacktriangledown}\wedge d\overline{Q}_{\blacktriangledown})$ | the Kähler form |
| $J$ | the complex structure, $J^2=-I$ |
| $H(Q_1,Q_2)=Q_{1\blacktriangle}\overline{Q_{2\blacktriangle}}+Q_{1\blacktriangledown}\overline{Q_{2\blacktriangledown}}$ | the Hermitian form |
| $B(Q_1,Q_2)=Q_{1\blacktriangle}Q_{2\blacktriangle}+Q_{1\blacktriangledown}Q_{2\blacktriangledown}$ | the complex bilinear form |
| $\varphi=\frac12\lVert Q\rVert^2$ | the Kähler potential, $\Omega=i\partial\bar\partial\varphi$ |
| $\omega=dQ_{\blacktriangle}\wedge dQ_{\blacktriangledown}$ | the holomorphic symplectic form and volume form |
| $\mathbb{C}^2\rtimes\mathrm{U}(2)$ | the group of holomorphic isometries |
| $\mathbb{C}^2\rtimes\mathrm{O}(4)$ | the full isometry group |

## Further Reading

- [Complex Two-Space](the-complex-two-space.html), for the space and the Hermitian form.
- [The Realification of $\mathbb{C}^2$](the-realification-of-the-complex-two-space.html), for the identification with $\mathbb{R}^4$ and the complex structure $J$.
- [The Three Canonical Forms on $\mathbb{C}^2$](the-three-canonical-forms-on-the-complex-two-space.html), for $H$, $B$ and the holomorphic symplectic form $\omega$, and their signatures.
- [The Subspaces of $\mathbb{C}^2$](the-subspaces-of-the-complex-two-space.html), for the complex lines, the Lagrangian planes and the isotropic lines.
- [The Ball and the Bicylinder in $\mathbb{C}^2$](the-ball-and-the-bicylinder.html), for the negatively curved model and its Bergman metric.
- [The Isotropic Cone of the Bilinear Form on $\mathbb{C}^2$](the-isotropic-cone-of-the-bilinear-form.html), the next article, for the null cone of $B$.
- [The Classical Groups of $\mathbb{C}^2$](the-classical-groups-of-the-complex-two-space.html), for $\mathrm{U}(2)$, $\mathrm{SU}(2)$ and the other groups of the space.
- [The Compactifications of $\mathbb{C}^2$](the-compactifications-of-the-complex-two-space.html), for the Fubini–Study comparison.
- [Conventions in Mathematics](conventions-in-mathematics.html), for the glyphs and the typographic conventions of the corpus.
