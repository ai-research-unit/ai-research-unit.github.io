# __The Two Halves and the Analysis over $\mathbb{R}$: Smooth Structures and the Exponential__

## Introduction

**The two halves are the eigenspaces of a smooth involution, so they are embedded submanifolds that split the tangent bundle, and the exponential behaves completely differently on them: a diffeomorphism on the symmetric half and a covering on the antisymmetric one.**

The article proves that $\operatorname{Sym}_n$ and $\operatorname{Skew}_n$ are embedded submanifolds of dimensions $n(n+1)/2$ and $n(n-1)/2$, that the symmetrisation and antisymmetrisation maps are smooth projections splitting the tangent bundle, that the exponential is a diffeomorphism on one half and a surjective local diffeomorphism on the other, and that the two exponentials do not multiply to the exponential of the sum. It assumes *The Analysis on $M_n(\mathbb{R})$*, *The Exponential of the Symmetric Part: Stretches and the Positive Cone* and *The Exponential of the Antisymmetric Part: One-Parameter Rotations*. It defers the metric to *The Geometry of the Two Halves and the Riemannian Reading*.

## The Two Halves as Submanifolds

**Theorem.** $\operatorname{Sym}_n$ and $\operatorname{Skew}_n$ are linear subspaces of $M_n(\mathbb{R})$, hence embedded smooth submanifolds of dimensions $n(n+1)/2$ and $n(n-1)/2$ with a single chart each.

*Proof.* Each is the fixed set of a linear map, the transpose or its negative, so each is a vector subspace. A vector subspace of $\mathbb{R}^{N}$ is an embedded submanifold with the inclusion as a chart.

**The sum map is a linear isomorphism.**

$$
\Phi:\operatorname{Sym}_n\oplus\operatorname{Skew}_n\to M_n(\mathbb{R}),\qquad \Phi(S,K)=S+K,
$$

with inverse $X\mapsto\bigl(\tfrac12(X+X^{\mathsf T}),\tfrac12(X-X^{\mathsf T})\bigr)$. So $\Phi$ is a diffeomorphism, and the two halves give a smooth product decomposition of the algebra.

**The inverse formula is the projection onto each factor.** Write $\pi_{+}(X)=\tfrac12(X+X^{\mathsf T})$ and $\pi_{-}(X)=\tfrac12(X-X^{\mathsf T})$. Then $\pi_{+}$ and $\pi_{-}$ are linear, hence smooth, and they satisfy

$$
\pi_{+}^{2}=\pi_{+},\qquad \pi_{-}^{2}=\pi_{-},\qquad \pi_{+}\pi_{-}=\pi_{-}\pi_{+}=0,\qquad \pi_{+}+\pi_{-}=\mathrm{id}.
$$

So they are complementary idempotent endomorphisms of the vector space, and $\operatorname{Sym}_n$ and $\operatorname{Skew}_n$ are their images.

**Consequence: the tangent bundle splits.** At every point $X$ the tangent space is $M_n(\mathbb{R})$, and the two projections cut it into a symmetric and an antisymmetric part. The splitting is constant in $X$, so it is a direct sum of two trivial vector bundles, and every smooth curve decomposes into a symmetric and an antisymmetric curve.

**The splitting is not a Lie algebra splitting.** The symmetric half is not a subalgebra for the commutator, so the splitting of the tangent bundle is not a splitting of the algebra into subalgebras; it is only a splitting of the vector bundle. *The Two Halves: Symmetric and Antisymmetric* is the article that makes this precise.

## The Derivative of the Exponential on Each Half

**On the symmetric half the derivative is the dexp acting on a symmetric direction.**

$$
d(\exp)_{S}(H)=e^{S}\sum_{k\ge0}\frac{(-1)^{k}}{(k+1)!}\operatorname{ad}_S^{k}(H),\qquad H\in\operatorname{Sym}_n,
$$

and the result is symmetric: for $S$ and $H$ both symmetric the commutator $[S,H]$ is antisymmetric, so $\operatorname{ad}_S$ exchanges the two halves, and the $k$-th term is symmetric for $k$ even and anti-self-adjoint for $k$ odd, which is exactly the pairing with the alternating coefficients.

**On the antisymmetric half the derivative is the same formula with an antisymmetric direction, and the result is antisymmetric.** The two halves are therefore preserved by the derivative, as they must be, since $\exp$ maps each half into a subset of the corresponding symmetric or orthogonal set.

**The derivative is invertible on each half at every point.** For the symmetric half this follows from the global bijectivity of $\exp$; for the antisymmetric half it follows from the covering property, since a local diffeomorphism has invertible derivative.

**The exponential of the sum is not the product of the exponentials.** For

$$
S=\begin{pmatrix}1&0.5\\0.5&-0.2\end{pmatrix},\qquad K=\begin{pmatrix}0&0.7\\-0.7&0\end{pmatrix},
$$

the two products differ substantially:

$$
e^{S}e^{K}=\begin{pmatrix}1.7325&2.5368\\ -0.0020&1.2816\end{pmatrix},\qquad e^{S+K}=\begin{pmatrix}2.4953&1.8262\\ -0.3044&0.6691\end{pmatrix},
$$

with a largest entry difference of $0.7628$. The reason is that $SK-KS=\begin{pmatrix}-0.7&0.84\\0.84&0.7\end{pmatrix}\ne0$, so the Baker–Campbell–Hausdorff correction does not vanish.

## The Exponential on the Symmetric Half

**Theorem.** $\exp:\operatorname{Sym}_n\to\operatorname{Sym}_n^{>0}$ is an analytic diffeomorphism, with inverse $\log$.

*Proof.* Surjective: the spectral theorem writes $P=Q\Lambda Q^{\mathsf T}$ with $\Lambda$ positive diagonal, and then $P=e^{S}$ with $S=Q(\log\Lambda)Q^{\mathsf T}$ symmetric. Injective: if $e^{S}=e^{S'}$ with both symmetric then $S$ and $S'$ commute with $e^{S}$, hence are polynomials in it, hence are simultaneously diagonalisable and agree on the eigenvalues. Analytic with analytic inverse: the logarithm of a positive definite matrix is given by the convergent series in $P-\mathrm{I}$ when $\|P-\mathrm{I}\|<1$ and by the spectral formula in general.

**So the symmetric half is a global chart for the cone.** The cone is an open convex subset of a vector space of dimension $n(n+1)/2$, and the exponential is a diffeomorphism onto it, which is the strongest possible statement about the exponential on this half.

**The derivative is everywhere invertible and the map is proper.** Properness follows from the spectral formula: if $e^{S}$ stays in a compact set then the eigenvalues of $S$ stay bounded, so $S$ stays in a compact set. A proper local diffeomorphism that is injective is a diffeomorphism, which gives a second proof.

## The Exponential on the Antisymmetric Half

**Theorem.** $\exp:\operatorname{Skew}_n\to\mathrm{SO}(n)$ is surjective, a local diffeomorphism everywhere, and not injective.

*Proof.* Surjective: by the spectral theorem for antisymmetric matrices, every rotation is a direct sum of rotations in orthogonal planes, and each planar rotation is $e^{\theta J_2}$; assembling the blocks gives $K\in\operatorname{Skew}_n$ with $e^{K}=Q$. Local diffeomorphism: the derivative is invertible at every point, and the map is equivariant under conjugation so it suffices to check at $0$. Not injective: at $n=2$ the matrix $2\pi J$ satisfies $e^{2\pi J}=\mathrm{I}$, and more generally $\exp$ is $2\pi$-periodic in each angle.

**The failure of injectivity is exactly the periodicity of the angles.** The eigenvalues of an antisymmetric matrix are $i\theta_1,-i\theta_1,\dots$ and the exponential depends on the angles modulo $2\pi$. So $\exp$ is a covering map onto its image in a neighbourhood of each point, and globally it is a fibration with fibres consisting of the angle shifts by $2\pi\mathbb{Z}$.

**The image is exactly $\mathrm{SO}(n)$ and not a proper subset.** This is where the antisymmetric half differs from a general subspace: the exponential of an antisymmetric matrix is always orthogonal with determinant one, and conversely every such matrix has an antisymmetric logarithm. So the two halves both have the exponential as a surjection onto their natural targets, and the difference is injectivity.

**Consequence: the half is a covering space of the group, and the two are not diffeomorphic.** $\operatorname{Skew}_n$ is contractible and $\mathrm{SO}(n)$ is not, so no diffeomorphism can exist; the exponential is a surjective local diffeomorphism between spaces of different homotopy type.

## The Smooth Structure of the Involution

**The transpose is a smooth involution of the algebra whose fixed and anti-fixed sets are the two halves.** It is linear, hence smooth, and it satisfies $\sigma^{2}=\mathrm{id}$, so its differential is itself and the eigenvalues of the differential are $\pm1$ everywhere.

**A smooth involution splits the tangent bundle into the $\pm1$ eigenbundles.** This is the general fact behind the splitting: for a smooth map $\sigma$ with $\sigma^{2}=\mathrm{id}$ on a manifold, the derivative at a fixed point has eigenvalues $\pm1$ and the fixed set is a submanifold whose tangent space is the $+1$ eigenbundle. Here the manifold is a vector space and the involution is linear, so the statement is the elementary one of the projections $\pi_{\pm}$.

**The same pattern appears at the group level.** The map $\Theta(A)=(A^{\mathsf T})^{-1}$ is a smooth involution of $\mathrm{GL}_n(\mathbb{R})$ whose fixed set is $\mathrm{O}(n)$; its derivative at the identity is $X\mapsto-X^{\mathsf T}$, whose fixed set is $\operatorname{Skew}_n$. So the Cartan involution of the group and the transpose involution of the algebra have the same fixed space at the identity, and this is the beginning of the Cartan decomposition.

**The two involutions differ by a sign and that sign is the whole content of the Cartan decomposition.** The algebra involution fixes $\operatorname{Sym}_n$; the group involution, differentiated, fixes $\operatorname{Skew}_n$. The two halves are exchanged by the sign, and the two decompositions differ by which half is the subalgebra.

## Analytic Consequences of the Splitting

**Every analytic function of a matrix splits along the halves in the sense of its Taylor coefficients.** For $f$ analytic near $0$ and $X=S+K$,

$$
f(X)=f(0)+f'(0)(S+K)+\tfrac12f''(0)(S+K)^{2}+\cdots,
$$

and the powers mix $S$ and $K$ through their commutator. So the Taylor expansion of $f$ is not a sum of a function of $S$ and a function of $K$; the mixing is exactly the noncommutativity.

**The trace kills the cross terms at first order.** $\operatorname{tr}(SK)=0$ for $S$ symmetric and $K$ antisymmetric, so the first-order term of $\operatorname{tr}f(X)$ is $f'(0)\operatorname{tr}S$, and the antisymmetric part enters only at second order and through $\operatorname{tr}(K^{2})$, which is negative.

**The determinant is blind to the antisymmetric part's sign and sees only its square.** $\det e^{S+K}=e^{\operatorname{tr}S}$, since the trace of $K$ vanishes; so the determinant of the exponential depends only on the symmetric part. This is the cleanest analytic statement of the split: the volume change is the symmetric part, and the rotation is the antisymmetric part.

**The splitting is the infinitesimal form of the polar decomposition.** Every invertible matrix is a rotation times a stretch, and the differential of that statement at the identity is the splitting of the algebra into the two halves.

## Summary

$\operatorname{Sym}_n$ and $\operatorname{Skew}_n$ are embedded submanifolds of dimensions $n(n+1)/2$ and $n(n-1)/2$, the images of the smooth complementary projections $\pi_{\pm}$, and they split the tangent bundle of the algebra. The exponential is an analytic diffeomorphism from $\operatorname{Sym}_n$ onto the positive definite cone and a surjective local diffeomorphism from $\operatorname{Skew}_n$ onto $\mathrm{SO}(n)$ that is not injective. The two exponentials do not multiply to the exponential of the sum, with a largest entry difference of $0.7628$ in the explicit example at $n=2$. The involution $\Theta(A)=(A^{\mathsf T})^{-1}$ on the group has derivative $X\mapsto-X^{\mathsf T}$ at the identity, which is why the group fixed set is the anti-Hermitian half while the algebra fixed set is the symmetric half.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\pi_{+},\pi_{-}$ | the symmetrisation and antisymmetrisation projections |
| $\Phi$ | the linear isomorphism $\operatorname{Sym}_n\oplus\operatorname{Skew}_n\to M_n(\mathbb{R})$ |
| $e^{S}$, $e^{K}$ | the stretch and the rotation parts of the exponential |
| $\Theta(A)=(A^{\mathsf T})^{-1}$ | the Cartan involution of the group |
| $\operatorname{ad}_S$ | the commutator operator used in dexp |

## Further Reading

- Sigurdur Helgason, *Differential Geometry, Lie Groups and Symmetric Spaces* (American Mathematical Society, 2001), for the Cartan involution and the exponential on each half.
- John Lee, *Introduction to Smooth Manifolds* (Springer, 2012), for embedded submanifolds, involutions and the splitting of the tangent bundle.
- [The Exponential of the Symmetric Part: Stretches and the Positive Cone](the-exponential-of-the-symmetric-part-stretches-and-the-positive-cone.html), for the diffeomorphism on the symmetric half.
- [The Exponential of the Antisymmetric Part: One-Parameter Rotations](the-exponential-of-the-antisymmetric-part-one-parameter-rotations.html), for the covering on the antisymmetric half.
- [The Analysis on $M_n(\mathbb{R})$](the-analysis-on-mnr.html), for the norms, the dexp series and the functional calculus.
