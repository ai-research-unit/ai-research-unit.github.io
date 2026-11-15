# __The Geometry of the Two Halves and the Riemannian Reading__

## Introduction

**The algebra is a pseudo-Euclidean vector space of signature $(n(n+1)/2,\,n(n-1)/2)$, the two halves are its orthogonally complementary definite subspaces, and the group carries a bi-invariant pseudo-Riemannian metric whose curvature is the commutator; so the entire geometry of the two halves is read from one indefinite scalar product.**

The article fixes the scalar product $\langle X,Y\rangle=\operatorname{tr}(XY)$, proves the signature, shows that the two halves are flat totally geodesic subspaces of opposite definiteness, distinguishes the flat exponential from the matrix exponential, defines the bi-invariant metric on $\mathrm{GL}_n(\mathbb{R})$ and identifies its geodesics, and computes the curvature as a bilinear expression in the bracket. It assumes *The Trace Form and Its Indefinite Signature* and *The Exponential of the Symmetric Part: Stretches and the Positive Cone*. It defers the symmetric space to *The Symmetric Space $\mathrm{GL}_n(\mathbb{R})/\mathrm{O}(n)$ and Its Complex Twin*.

## The Indefinite Scalar Product

**Definition.** On $M_n(\mathbb{R})$ put $\langle X,Y\rangle=\operatorname{tr}(XY)$. It is symmetric and nondegenerate, being the trace of the product, and it is invariant under the transpose and under conjugation: $\langle AX,XB\rangle=\langle X,B\!AX\rangle$.

**Theorem.** The signature is $\bigl(n(n+1)/2,\ n(n-1)/2\bigr)$, that is $p=n(n+1)/2$ positive and $q=n(n-1)/2$ negative directions.

*Proof.* The two halves are orthogonal, since $\operatorname{tr}(SK)=0$ for $S$ symmetric and $K$ skew, because $SK$ and $KS=(SK)^{\mathsf T}$ have the same trace. On $\operatorname{Sym}_n$ the form is positive definite, $\operatorname{tr}(S^{2})=\|S\|_{2}^{2}>0$ for $S\ne0$. On $\operatorname{Skew}_n$ it is negative definite, $\operatorname{tr}(K^{2})=-\|K\|_{2}^{2}<0$. So the signature is the pair of dimensions, measured as $(3,1),(6,3),(10,6),(15,10)$ at $n=2,3,4,5$.

**So the algebra is a pseudo-Euclidean space with a preferred orthogonal splitting into a definite positive and a definite negative part.** The splitting is exactly the splitting into the two halves, and it is the only natural one.

**The cone of isotropic vectors is worth naming.** $X$ is isotropic when $\operatorname{tr}(X^{2})=0$. For a symmetric $X$ that happens only at $X=0$, since the form is definite there; for a skew $X$ likewise. So every isotropic vector has both halves nonzero, and the isotropic cone is the union of the lines on which the two quadratic forms cancel.

**The form is not the Hilbert–Schmidt form.** $\operatorname{tr}(X^{\mathsf T}X)$ is definite and equal to the Euclidean norm; $\operatorname{tr}(X^{2})$ is indefinite and equal to the difference of the norms of the two halves:

$$
\langle X,X\rangle=\|S\|_{2}^{2}-\|K\|_{2}^{2}\quad\text{for }X=S+K .
$$

## The Two Halves as Flat Subspaces

**Each half is a linear subspace, hence flat and totally geodesic.** In a pseudo-Euclidean vector space the geodesics are the straight lines, so a linear subspace is totally geodesic, and the induced metric on it is flat.

**The two halves realise the two halves of the signature.** On $\operatorname{Sym}_n$ the form is positive definite of dimension $n(n+1)/2$, on $\operatorname{Skew}_n$ negative definite of dimension $n(n-1)/2$, exactly the two indices. They are not the only definite subspaces of those dimensions: a graph of a symmetric map over the skew half can be positive definite too. What is special about the halves is that they are the unique *orthogonal* pair of definite subspaces covering the whole space.

**The intrinsic geometry of $\operatorname{Sym}_n$ is Euclidean.** Its distance is $\|S-S'\|_{2}$, its geodesics are the affine lines $S+tH$, and its isometry group is the semidirect product of the translations and $\mathrm{O}(\operatorname{Sym}_n)$.

**The intrinsic geometry of $\operatorname{Skew}_n$ is Euclidean with the opposite sign.** Distances are the same numbers, $\|K-K'\|_{2}$, computed from $-\operatorname{tr}((K-K')^{2})$, but the squared length of a vector is negative, so the half is a negative definite pseudo-Riemannian manifold and not a Riemannian one. Its geodesics are still the affine lines.

**Consequence: the algebra is the orthogonal direct sum of a Euclidean and an anti-Euclidean space.** Every vector has a positive length, a negative length, or zero, and the sign is the sign of $\|S\|_{2}^{2}-\|K\|_{2}^{2}$. The three regions are the two parts of the isotropic cone and the cone itself.

## The Two Exponentials

**The flat exponential and the matrix exponential are different maps with the same source.** The flat exponential at the origin of the vector space is the identity: $\operatorname{Exp}_0(V)=V$. The matrix exponential is the series, $\operatorname{Exp}(V)=e^{V}$. Both start at $\mathrm{I}$ when read as maps into the group, and their derivatives at $0$ agree, but their global behaviour is different.

**The distance in the group metric is the length of the tangent vector, not the length of the image.** For $S=\begin{pmatrix}1&0.5\\0.5&-0.2\end{pmatrix}$ the length of $S$ is $\sqrt{\operatorname{tr}S^{2}}=\sqrt{1.54}\approx1.241$, while the Euclidean distance from $\mathrm{I}$ to $e^{S}$ is $\|e^{S}-\mathrm{I}\|_{2}\approx2.2798$. So the exponential is far from an isometry.

**The matrix exponential is a chart for the cone, and the chart is not the Euclidean one.** The map $S\mapsto e^{S}$ is a diffeomorphism of the half onto the cone, and pulling back the flat metric of the half gives the cone a flat metric in which the exponential is an isometry by construction. That metric is not the restriction of the algebra metric to the cone.

**The flat metric and the cone metric differ by the derivative of the exponential.** The pullback is $\langle d\exp_S(H),d\exp_S(H')\rangle$, and it equals the flat one only where the dexp is orthogonal, that is on the centre.

## The Bi-Invariant Metric on the Group

**Definition.** On the group put $g_A(H,H')=\operatorname{tr}(A^{-1}HA^{-1}H')$ for tangent vectors $H,H'\in T_A\mathrm{GL}_n(\mathbb{R})=M_n(\mathbb{R})$.

**Theorem.** $g$ is a pseudo-Riemannian metric of constant signature $(p,q)$, invariant under both left and right translations, and its geodesics through $\mathrm{I}$ are exactly the one-parameter subgroups $t\mapsto e^{tX}$.

*Proof.* The formula is left-invariant by construction: translating $H$ by $A$ turns $A^{-1}H$ into $X$ and leaves the expression $\langle X,X'\rangle$ unchanged. Right translation by $B$ sends $A^{-1}H$ to $B^{-1}A^{-1}HB$, and cyclicity of the trace gives $\operatorname{tr}(B^{-1}MB\,B^{-1}NB)=\operatorname{tr}(MN)$, so the metric is bi-invariant. Signature: at $A=\mathrm{I}$ the metric is the trace form, of signature $(p,q)$. Geodesics: for a bi-invariant metric the Levi-Civita connection is $\nabla_XY=\tfrac12[X,Y]$ on left-invariant fields, and the curve $t\mapsto e^{tX}$ has velocity field right-invariant along itself, so $\nabla_{\dot\gamma}\dot\gamma=\tfrac12[\dot\gamma,\dot\gamma]=0$.

**So the matrix exponential is the Riemannian exponential at the identity.** This is the one place where the algebra exponential and the geometry agree, and it is the reason the exponential is the natural map in the Lie theory.

**The exponential is not the Riemannian exponential at other points.** At a point $A\ne\mathrm{I}$ the geodesics are the curves $Ae^{tX}$, not the curves $e^{A+tX}$; the metric is left-invariant, so it sees only the left-translated structure.

**The signature is indefinite, so the metric has null directions.** The left-invariant vector fields with $X$ isotropic are null, and the light cone at each point is the left translate of the isotropic cone of the algebra.

## Curvature

**For a bi-invariant metric the curvature tensor is a bracket.**

$$
R(X,Y)Z=-\tfrac14\bigl[[X,Y],Z\bigr],\qquad K(X,Y)=\tfrac14\langle[X,Y],[X,Y]\rangle .
$$

The first formula is the standard one for a bi-invariant metric on a Lie group, and the second is the sectional curvature of the plane spanned by two vectors that are orthonormal and non-null.

*Proof.* For the bi-invariant metric the connection is $\nabla_XY=\tfrac12[X,Y]$, so $R(X,Y)Z=\nabla_X\nabla_YZ-\nabla_Y\nabla_XZ-\nabla_{[X,Y]}Z$ becomes $\tfrac14[Y,[X,Z]]-\tfrac14[X,[Y,Z]]-\tfrac12[[X,Y],Z]$, and the Jacobi identity turns this into $-\tfrac14[[X,Y],Z]$.

**Consequence: the metric is flat exactly where the bracket vanishes.** A bi-invariant metric on a connected Lie group is flat only when the group is abelian, so $\mathrm{GL}_n(\mathbb{R})$ with this metric is never flat for $n\ge2$. The directions that stay flat are the ones whose brackets vanish, that is the directions in a commutative subalgebra.

**Consequence: the curvature on $\mathfrak{so}(3)$ is negative with the trace form.** Take $X=E_{12}/\sqrt{2}$ and $Y=E_{23}/\sqrt{2}$, orthonormal for $-\operatorname{tr}$ on $\mathfrak{so}(3)$. Then $[X,Y]=E_{13}/2$ and $\operatorname{tr}([X,Y]^{2})=-1/2$, so

$$
K(X,Y)=\tfrac14(-0.5)=-0.125 .
$$

So the sectional curvature is negative on the compact part, which is the opposite sign from the usual normalisation of a compact group and is the effect of the indefinite trace form.

**Consequence: the symmetric half is flat while the group is not.** The half is a vector space with the flat metric; the group is curved by the bracket. The passage from the half to the group is the exponential, and the curvature is the obstruction to the exponential's being a local isometry.

**The two readings are related by the Cartan decomposition.** $\mathfrak{gl}_n=\mathfrak{p}\oplus\mathfrak{k}$ with $\mathfrak{p}=\operatorname{Sym}_n$ and $\mathfrak{k}=\operatorname{Skew}_n$, and $[\mathfrak{p},\mathfrak{p}]\subseteq\mathfrak{k}$, $[\mathfrak{p},\mathfrak{k}]\subseteq\mathfrak{p}$, $[\mathfrak{k},\mathfrak{k}]\subseteq\mathfrak{k}$. So the curvature of the symmetric space is computed from $[\mathfrak{p},\mathfrak{p}]$, and the flat directions inside $\mathfrak{p}$ are the commuting ones.

## Summary

The trace form gives $M_n(\mathbb{R})$ the structure of a pseudo-Euclidean space of signature $(n(n+1)/2,\,n(n-1)/2)$, with the two halves as orthogonally complementary definite subspaces: $\operatorname{Sym}_n$ positive definite, $\operatorname{Skew}_n$ negative definite, each flat and totally geodesic. The flat exponential is the identity and the matrix exponential is a chart with a different metric; the length $\sqrt{1.54}\approx1.241$ of a symmetric matrix differs from the distance $\approx2.2798$ between $\mathrm{I}$ and its exponential. On the group the metric $g_A(H,H')=\operatorname{tr}(A^{-1}HA^{-1}H')$ is bi-invariant of the same signature and its geodesics through $\mathrm{I}$ are the one-parameter subgroups, so the matrix exponential is the Riemannian exponential at $\mathrm{I}$. The curvature is $R(X,Y)Z=-\tfrac14[[X,Y],Z]$, negative on the compact part, with $K=-0.125$ for an orthonormal plane in $\mathfrak{so}(3)$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle X,Y\rangle=\operatorname{tr}(XY)$ | the indefinite scalar product of signature $(p,q)$ |
| $g_A(H,H')$ | the bi-invariant metric on the group |
| $R(X,Y)Z$ | the curvature tensor, $-\tfrac14[[X,Y],Z]$ |
| $K(X,Y)$ | the sectional curvature, $\tfrac14\langle[X,Y],[X,Y]\rangle$ |
| $\mathfrak{p},\mathfrak{k}$ | the symmetric and skew halves in the Cartan decomposition |

## Further Reading

- Sigurdur Helgason, *Differential Geometry, Lie Groups and Symmetric Spaces* (American Mathematical Society, 2001), for bi-invariant metrics, geodesics and curvature on Lie groups.
- Barrett O'Neill, *Semi-Riemannian Geometry* (Academic Press, 1983), for indefinite metrics, their signature and their geodesics.
- [The Trace Form and Its Indefinite Signature](the-trace-form-and-its-indefinite-signature.html), for the signature and the orthogonal splitting.
- [The Two Halves and the Analysis: Smooth Structures and the Exponential](the-two-halves-and-the-analysis-smooth-structures-and-the-exponential-over-r.html), for the analytic side of the same splitting.
- [The Cartan Decomposition of $\mathrm{GL}_n(\mathbb{R})$](the-cartan-decomposition-of-glnr.html), for the decomposition used in the last section.
