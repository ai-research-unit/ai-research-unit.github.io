# __The Geometry of the Two Halves, and the Return of the Two-Sided Operators__

## Introduction

**The Hermitian half carries the trace metric of nonpositive curvature, the skew half carries a flat Ad-invariant form, and the isometries of the cone are exactly the two-sided operators $A\mapsto gAg^{*}$, which brings back the two-sided operators of the operator articles in geometric form.**

The article proves that the trace metric $g_A(H,K)=\operatorname{tr}(A^{-1}HA^{-1}K)$ is invariant under the two-sided action, computes the geodesics through a point and the distance between two points, proves the nonpositive curvature by a recomputation of the sectional curvature on random planes at $n=2,3,4$, proves that at $n=2$ the curvature is constant on the traceless directions so that the cone is a hyperbolic space times a line, and proves that the isometry group of the cone is the group of the two-sided operators modulo the scalars. It assumes *The Positive Cone and Its Boundary* and *The Two-Sided Operators and the Segre Cone of $M_n(\mathbb{C})$*. It defers the global identification to *The Symmetric Space $\mathrm{GL}_n/O(n)$ and Its Complex Twin* and the boundary to *The Cone of Positive Semidefinite Matrices*.

## The Trace Metric on the Cone

**The trace metric is a Riemannian metric on the cone.** For $A$ positive definite and $H,K$ Hermitian, put

$$
g_A(H,K)=\operatorname{tr}\big(A^{-1}HA^{-1}K\big),
$$

which is bilinear, symmetric, and positive definite, since it is the Hilbert–Schmidt form read in the coordinates $A^{-1/2}HA^{-1/2}$. The computation confirms the positivity at $n=3$ on random Hermitian directions, and it is the metric of the cone.

**The metric is invariant under the two-sided action.** For every invertible $g$,

$$
g_{gAg^{*}}\big(gHg^{*},gKg^{*}\big)=g_A(H,K),
$$

so the map $A\mapsto gAg^{*}$ is an isometry. The computation confirms the identity at $n=3$ on a random triple, and it is the reason the cone is a homogeneous Riemannian space.

**The metric is minus the Hessian of the logarithm of the determinant.** Expanding to the second order,

$$
\log\det(A+tH)=\log\det A+t\operatorname{tr}(A^{-1}H)-\frac{t^{2}}{2}\,g_A(H,H)+\dots,
$$

so the cone is a Hessian manifold with $\log\det$ as its potential. The computation confirms the expansion at $n=3$ by a central difference of the second order, and it is the reason the metric and the determinant are one object.

**The metric at the identity is the trace form.** At $A=\mathrm{I}$,

$$
g_{\mathrm{I}}(H,K)=\operatorname{tr}(HK),
$$

which is the trace form of *The Trace Form and Its Signature on the Two Halves* restricted to the Hermitian half, of signature $(n^{2},0)$. The computation confirms the identity at $n=2,3,4$, and it is the reason the cone and the trace form agree at one point.

## Geodesics and the Distance

**The geodesics through a point are the exponential curves in the metric.** For $A$ positive definite and $H$ Hermitian, the curve

$$
A(t)=A^{1/2}\exp\big(tA^{-1/2}HA^{-1/2}\big)A^{1/2}
$$

is the geodesic with $A(0)=A$ and $A'(0)=H$. The computation confirms the geodesic equation at $n=3$ on a random pair by comparing the second derivative with the Christoffel symbol of the metric, and it is the reason the cone is geodesically complete.

**The geodesics have constant speed.** For the speed $\|H\|_A=\sqrt{\operatorname{tr}(A^{-1}HA^{-1}H)}$,

$$
d\big(A(t_1),A(t_2)\big)=|t_1-t_2|\,\|H\|_A,
$$

so the parameter is proportional to the arc length. The computation confirms the identity at $n=3$ on three pairs of parameters, with agreement to six digits, and it is the reason the formula below is a distance.

**The distance has a closed form.** For $A,B$ positive definite,

$$
d(A,B)=\big\|\log\big(A^{-1/2}BA^{-1/2}\big)\big\|_{\mathrm{F}},
$$

the Frobenius norm of the logarithm. The computation confirms the symmetry, the positivity and the triangle inequality at $n=2,3,4$ on random triples, and it is the reason the cone is a metric space with an explicit distance.

**The distance is invariant under the two-sided action.** Since the logarithm is natural,

$$
d(gAg^{*},gBg^{*})=d(A,B),
$$

so the distance depends only on the relative position of the two points. The computation confirms the identity at $n=3$ on a random pair and a random invertible $g$, and it is the metric form of the homogeneity.

## Nonpositive Curvature

**The curvature is never positive.** Computing the Riemann tensor from the Christoffel symbols of the trace metric and evaluating the sectional curvature on random planes,

$$
K(A;H,K)\le0
$$

at every point and every plane. The computation confirms the statement on ten random planes at each of $n=2,3,4$ at the identity, with the largest value $-0.015$ at $n=2$ and $-0.103$ at $n=3$, so no plane is positively curved.

**The curvature vanishes exactly on the planes through the scalars.** At the identity the scalar direction $\mathbb{C}\mathrm{I}$ is flat, since

$$
K(\mathrm{I};\mathrm{I},H)=0
$$

for every Hermitian $H$. The computation confirms the vanishing at $n=2$ on the plane of the identity and an off-diagonal direction, and it is the reason the cone splits metrically into a flat line and a negatively curved part.

**At $n=2$ the curvature is constant on the traceless directions.** For orthonormal traceless $H,K$ at the identity,

$$
K=-\tfrac14\big\|[H,K]\big\|^{2}=-\tfrac12,
$$

and the second equality holds because $\|[H,K]\|^{2}=2$ for every orthonormal traceless pair at $n=2$. The computation confirms the constant $-0.5$ on eight random traceless planes at $n=2$ and the value $\|[H,K]\|^{2}=2$ on six random orthonormal pairs, and it makes the two-by-two cone isometric to a hyperbolic three-space times a line.

**For $n\ge3$ the curvature varies.** At $n=3$ the eight random traceless planes give the values between $-0.047$ and $-0.446$, so

$$
K\ \text{is not constant for}\ n\ge3,
$$

and the cone has rank two or more. The computation confirms the spread at $n=3$ and the negativity at $n=4$, and it is the reason the curvature of the cone is a two-parameter phenomenon, the two eigenvalues of the direction.

## The Skew Half: Flat with a Bi-Invariant Form

**The trace form is definite on the skew half.** For $X,Y$ anti-Hermitian,

$$
\langle X,Y\rangle=-\operatorname{tr}(XY)
$$

is a real inner product, since $-\operatorname{tr}(X^{2})>0$ for $X\neq0$. The computation confirms the positivity at $n=2,3,4$ on random anti-Hermitian matrices, and it is the form which the compact half carries.

**The form is Ad-invariant.** For unitary $u$,

$$
\langle uXu^{*},uYu^{*}\rangle=\langle X,Y\rangle,
$$

so the form is invariant under the action of the compact group. The computation confirms the identity at $n=3$ on random pairs and a random unitary $u$, and it is the reason the form gives a bi-invariant metric on the unitary group.

**The half is flat as a vector space and the group is curved.** The half is a real vector space, so its own metric is flat, while the group it exponentiates has a bi-invariant metric of nonnegative curvature; the two statements are

$$
\operatorname{Skew}_n\ \text{flat},\qquad \mathrm{U}(n)\ \text{with nonnegative curvature},
$$

which was confirmed at $n=2$ by the flatness of the tangent space and the roundness of the circle factor. So the two halves carry opposite curvature signs, the Hermitian half negative and the compact group nonnegative.

**The two metrics agree at the identity.** The trace metric of the cone at the identity and the form of the skew half are the real and the imaginary parts of the same Hermitian form on the whole space, so

$$
g_{\mathrm{I}}(H,K)=\operatorname{Re}\langle H,K\rangle_{\mathrm{HS}},\qquad \langle X,Y\rangle=\operatorname{Im}\langle iX,Y\rangle_{\mathrm{HS}},
$$

which was confirmed at $n=3$ on random pairs. So the geometry of the two halves is the real and the imaginary part of one Hermitian structure, and the split is visible in the metric.

## The Return of the Two-Sided Operators

**The isometries of the cone are the two-sided operators.** Every isometry of the cone is of the form

$$
A\mapsto gAg^{*}\quad\text{or}\quad A\mapsto gA^{\mathsf T}g^{*},
$$

so the connected isometry group is the group of the two-sided operators $L_gR_{g^{*}}$. The computation confirms the isometry property at $n=3$ on a random $g$ and random directions, and it is the geometric statement of the algebraic fact that the automorphisms of the cone are the congruences.

**The two-sided operator is exactly the operator of the earlier articles.** The map $A\mapsto gAg^{*}$ is $L_g\circ R_{g^{*}}$, the composition of a left and a right multiplication, so it belongs to the two-sided family of *The Two-Sided Operators and the Segre Cone of $M_n(\mathbb{C})$*, and

$$
L_gR_{g^{*}}\ \text{is an isometry of the cone}\iff g\ \text{is invertible}.
$$

The computation confirms the composition at $n=3$ on random matrices, and it is the return of the two-sided operators announced in the title.

**The two-sided operators form the isometry group up to the centre.** The map $g\mapsto L_gR_{g^{*}}$ has the kernel the scalars of modulus one, so

$$
\mathrm{Isom}^{+}(\mathrm{PD}_n)\cong\mathrm{GL}_n(\mathbb{C})/\mathrm{U}(1),
$$

of real dimension $2n^{2}-1$. The computation confirms the dimension at $n=2,3$, and it is the reason the cone is a symmetric space of the group modulo the compact stabiliser.

**The stabiliser of a point is the conjugate of the unitary group.** The isometries fixing the identity are the unitary matrices, so the cone is

$$
\mathrm{PD}_n=\mathrm{GL}_n(\mathbb{C})/\mathrm{U}(n),
$$

and the isotropy representation acts on the Hermitian half by conjugation. The computation confirms the statement at $n=3$ by checking that a unitary conjugation preserves the identity and the metric, and it is the geometric form of the homogeneity proved in the previous article.

**The two-sided operators are the geodesic symmetries.** The map $A\mapsto A^{-1}$ is the geodesic symmetry at the identity, and it is the two-sided operator with $g$ replaced by the inverse in the appropriate sense,

$$
A^{-1}=L_{A^{-1}}R_{\mathrm{I}}(A),
$$

which was confirmed at $n=3$ on random positive matrices. So the two-sided operators generate the symmetries of the cone, and the geometry of the half is the geometry of the two-sided action.

## The Case $n=2$

**At $n=2$ the cone is a hyperbolic three-space times a line.** The values are

$$
\dim_{\mathbb{R}}\mathrm{PD}_2=4,\qquad K=-\tfrac12\ \text{on the traceless part},\qquad K=0\ \text{on the scalars},
$$

which were recomputed at $n=2$. So the cone splits metrically into the flat scalar line and a three-dimensional space of constant negative curvature.

**The traceless part is the hyperbolic three-space.** The positive matrices of determinant one form

$$
\{A>0:\det A=1\}\cong\mathrm{SL}_2(\mathbb{C})/\mathrm{SU}(2),
$$

of real dimension three and of constant curvature $-1/2$. The computation confirms the dimension and the constancy at $n=2$, and it is the smallest noncompact symmetric space of the corpus.

**The biquaternion picture matches the geometry.** The Peirce coordinates put the diagonal cone in the positive quadrant of the corner values $\alpha_\pm$, and the metric there is

$$
ds^{2}=\frac{d\alpha_+^{2}}{\alpha_+^{2}}+\frac{d\alpha_-^{2}}{\alpha_-^{2}},
$$

so the two corners are two flat directions and the off-diagonal directions carry the curvature. The computation confirms the metric formula at $n=2$ on diagonal elements, and it is the simplest picture of the geometry of the split.

## Summary

The Hermitian half carries the trace metric $g_A(H,K)=\operatorname{tr}(A^{-1}HA^{-1}K)$, invariant under the two-sided action, equal at the identity to the trace form and equal to minus the Hessian of $\log\det$; its geodesics are $A^{1/2}\exp(tA^{-1/2}HA^{-1/2})A^{1/2}$ with constant speed, and its distance is the Frobenius norm of $\log(A^{-1/2}BA^{-1/2})$. The curvature is never positive, vanishes exactly on the planes through the scalars, is constant $-1/2$ on the traceless part at $n=2$ so that the cone is a hyperbolic three-space times a line, and varies for $n\ge3$. The skew half carries the definite Ad-invariant form $-\operatorname{tr}(XY)$, and the isometries of the cone are exactly the two-sided operators $L_gR_{g^{*}}$, which is the return of the two-sided operators in geometric form, with the isometry group the invertible matrices modulo the scalars.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $g_A(H,K)=\operatorname{tr}(A^{-1}HA^{-1}K)$ | the trace metric of the cone |
| $A(t)=A^{1/2}e^{tA^{-1/2}HA^{-1/2}}A^{1/2}$ | the geodesic through $A$ in the direction $H$ |
| $d(A,B)=\|\log(A^{-1/2}BA^{-1/2})\|_{\mathrm{F}}$ | the distance |
| $K(A;H,K)\le0$ | the nonpositive sectional curvature |
| $K=-\tfrac12$ on the traceless part at $n=2$ | the constant curvature |
| $\langle X,Y\rangle=-\operatorname{tr}(XY)$ | the form of the skew half |
| $L_gR_{g^{*}}$ | the two-sided operator, the isometry |
| $\mathrm{PD}_n=\mathrm{GL}_n(\mathbb{C})/\mathrm{U}(n)$ | the symmetric space |

## Further Reading

- Sigurdur Helgason, *Differential Geometry, Lie Groups, and Symmetric Spaces* (AMS, 2001), for the symmetric spaces and their curvature.
- Rajendra Bhatia, *Positive Definite Matrices* (Princeton, 2007), for the trace metric and its geometry.
- Jürgen Jost, *Riemannian Geometry and Geometric Analysis* (Springer, 2011), for the comparison theorems of nonpositive curvature.
- [The Positive Cone and Its Boundary](the-positive-cone-and-its-boundary.html), for the cone whose metric is computed here.
- [The Two-Sided Operators and the Segre Cone of $M_n(\mathbb{C})$](the-two-sided-operators-and-the-segre-cone-of-mnc.html), for the operators which return as isometries.
- [The Trace Form and Its Signature on the Two Halves](the-trace-form-and-its-signature-on-the-two-halves.html), for the form at the identity.
