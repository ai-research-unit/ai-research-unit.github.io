# __The Hausdorff Dimension of the Biquaternion Julia Sets__

## Introduction

The Hausdorff dimension of a biquaternion Julia set is a number attached to a subset of an eight-real-dimensional space, and the category can report three things about it: the exact values for the parameter zero and for the parameters whose spectral set is a variety, the reduction of the dimension of a slice to the dimension of the corresponding classical fractal, and an upper bound for a central parameter in terms of the dimension of the complex Julia set. What the category cannot report is a formula for a general non-central parameter, and the article says so. The singular part of the fractal — the part lying on the critical set — requires separate treatment, and it is not negligible: it contains a real four-dimensional surface at the parameter zero.

The fractal and the critical set are *The Biquaternion Quadratic Map and Its Julia Sets*; the slices and their dimensions are classical, and the slice identification is *The Slices of the Biquaternion Julia Sets*; the zero divisors and the idempotent surface are *The Zero Divisors and the Singular Julia Sets*; the idempotent plane and its product structure are *The Idempotent Decomposition and the Split Fractal*; the system and the similarity dimension are *The Biquaternion Iterated Function Systems*. The dimension itself is defined in *Fractal Geometry* of Part IV, and its measure-theoretic refinements are in *Fractal Analysis* of Part III.

The article owns the dimension of the slices, the exact values at the parameter zero, the upper bound for a central parameter, the lower bound from the singular surface, and the statement of the open problem. It does not attempt a general dimension formula.

**Standing convention.** $\dim_H$ is the Hausdorff dimension, $\mathcal K_{\tilde C}$ and $J_{\tilde C}$ are the filled Julia set and the Julia set, and a **slice** of a fractal is its intersection with a real or complex subspace in the sense of *The Slices of the Biquaternion Julia Sets*.

## The Dimension of a Slice

**Proposition (the classical slices).** Let $\tilde C=Ce_0$ be central. Then

$$
\dim_H\bigl(J_{Ce_0}\cap\mathbb{C}e_0\bigr)=\dim_H J_C,\qquad \dim_H\bigl(\mathcal K_{Ce_0}\cap\mathbb{C}e_0\bigr)=\dim_H K_C,
$$

and for a real central parameter the same with the real quaternion subspace and the quaternion Julia set in place of the complex one.

**Proof.** The central slice is the image of the classical sets under the isometry $A\mapsto Ae_0$ of the Euclidean plane onto the centre (*The Slices of the Biquaternion Julia Sets*), and the quaternion slice is the classical quaternion picture; Hausdorff dimension is invariant under isometries.

**Theorem (the dimension of a product slice).** Let $\tilde\Pi$ be a primitive idempotent and $\tilde C=C_1\tilde\Pi+C_2\tilde\Pi'$ a parameter in the idempotent plane $W_{\tilde\Pi}$. Then

$$
\dim_H\bigl(J_{\tilde C}\cap W_{\tilde\Pi}\bigr)=\max\bigl(\dim_H J_{C_1}+\dim_H K_{C_2},\ \dim_H K_{C_1}+\dim_H J_{C_2}\bigr),
$$

the maximum of the two products of a boundary and a filled Julia set; when a factor has empty interior its boundary and its filled set coincide and the corresponding terms agree.

**Proof.** The slice is the boundary of the product, $J_{\tilde C}\cap W_{\tilde\Pi}=\partial(K_{C_1}\times K_{C_2})=(J_{C_1}\times K_{C_2})\cup(K_{C_1}\times J_{C_2})$ (*The Idempotent Decomposition and the Split Fractal*). For a product of two sets in Euclidean spaces the Hausdorff dimension satisfies $\dim_H(A\times B)=\dim_H A+\dim_H B$ when one of the factors is sufficiently regular, in particular for the Julia sets and the filled Julia sets of the quadratic family (*Fractal Geometry*, §*Products and the Dimension Formula*); applying it to the two products of the displayed union and taking the maximum gives the value.

**Remark (the slice need not have the dimension of the complex fractal).** A slice lies in the four-real-dimensional plane $W_{\tilde\Pi}$, so its dimension is at most four, and it can exceed the dimension of a single complex Julia set by the dimension of the other filled factor: at $C_1=C_2=0$ the two complex filled Julia sets are discs of dimension two and the slice, the boundary of the bidisc, has real dimension three. **The dimension of the biquaternion fractal is a statement about the whole eight-dimensional set, and a slice exhibits only the part of it carried by the plane.**

## The Parameter Zero

**Theorem (the dimension at the parameter zero).** For $\tilde C=0$,

$$
\dim_H\mathcal K_0=8, \qquad \dim_H J_0=7 .
$$

Moreover $J_0$ contains the idempotent surface, a real four-dimensional smooth manifold, so $\dim_H\bigl(J_0\cap\mathscr{Z}\bigr)\ge4$.

**Proof.** $\mathcal K_0$ contains the open set $\{\rho(\Phi(\tilde Q))<1\}$, because the orbit of a matrix of spectral radius below one tends to zero (*The Biquaternion Quadratic Map and Its Julia Sets*, §*The Central Parameter and the Eigenvalue Reduction*), so $\dim_H\mathcal K_0=8$. The Julia set is $J_0=\{\rho(\Phi(\tilde Q))=1\}$: the filled set $\mathcal K_0$ has closure $\{\rho\le1\}$ and interior $\{\rho<1\}$ — the matrices of spectral radius one that are not diagonalisable lie outside $\mathcal K_0$ but are limits of diagonalisable ones — so its boundary is the level set $\{\rho=1\}$. That level set is a semialgebraic set of real dimension seven: on the open dense set where exactly one eigenvalue has modulus one (or the two are distinct), $\rho$ is real-analytic with non-vanishing differential and the level set is a real hypersurface, and a semialgebraic set has Hausdorff dimension equal to its real dimension. The idempotent surface is contained in $J_0$ and has real dimension four (*The Zero Divisors and the Singular Julia Sets*).

**Remark (why the dimension drops from eight to seven).** The filled Julia set is full-dimensional because it contains a neighbourhood of the origin in the model, and the Julia set is the boundary of the region it fills, of one real dimension less. **The whole-dimensional non-escaping set and the codimension-one fractal of its boundary are the two objects of the parameter zero, and the singular surface is a distinguished part of the boundary.** The same picture holds at every central parameter for which the complex filled Julia set has interior.

## The Central Parameter

**Theorem (the central parameter bound).** Let $\tilde C=Ce_0$ be central and let $\mathcal K_c$ be the complex filled Julia set of $\zeta\mapsto\zeta^2+C$.

1. If $C$ lies in the interior of the Mandelbrot set, then $\dim_H\mathcal K_{Ce_0}=8$.
2. If the complex filled Julia set has dimension $\alpha$, then

$$
\dim_H\mathcal K_{Ce_0}\le4+2\alpha .
$$

**Proof.** (1) For $C$ in the interior of the Mandelbrot set the origin is in the interior of the complex filled Julia set, and the set of matrices whose eigenvalues lie in a disc about the origin contained in $K_C$ is an open neighbourhood of $0$ in $\mathcal K_{Ce_0}$; hence the set is full-dimensional. (2) A matrix in $\mathcal K_{Ce_0}$ with distinct eigenvalues $\lambda_1\neq\lambda_2$ is $S\operatorname{diag}(\lambda_1,\lambda_2)S^{-1}$. Fix the unordered pair of eigenvalues in $K_C$: the conjugates of the diagonal matrix form the conjugacy class, the quotient of $GL_2(\mathbb{C})$, of real dimension eight, by the centraliser of a diagonal matrix with distinct eigenvalues, which is the torus of diagonal matrices, of real dimension four; the class therefore has real dimension four, and near a matrix with distinct eigenvalues the conjugacy class and the eigenvalue pair are local coordinates on $\mathcal K_{Ce_0}$, four real dimensions from the class and at most $2\dim_HK_C$ from the pair, since the pair ranges over $K_C\times K_C$ and the product formula holds for these sets. The matrices with repeated eigenvalues form a set of lower dimension and do not affect the bound. Hence $\dim_H\mathcal K_{Ce_0}\le4+2\dim_HK_C$.

**Remark (the expectation and the evidence).** The bound is expected to be an equality, the four dimensions coming from the conjugacy class of a matrix and the $2\alpha$ from the pair of eigenvalues; the equality holds at $C=0$, where $\alpha=2$ and $4+2\alpha=8$. **The exact dimension of the biquaternion Julia set at a central parameter is the dimension of the complex Julia set, doubled and shifted by four, and this is the only clean formula the category has.** No such formula exists for a non-central parameter, because the orbit is not a polynomial in one element and the spectrum does not separate.

## The Non-Central Parameter and the Open Problem

**Remark (what is open).** For a non-central parameter the fractal is the Julia set of a polynomial map of $\mathbb{C}^4$ whose leading part is not proper, the pluripotential theory of the general case is not available (*The Pluripotential Theory of the Biquaternion Dynamics*), the singular set is a hypersurface with two components (*The Zero Divisors and the Singular Julia Sets*), and no dimension formula is known. **The dimension of the biquaternion Julia set for a general parameter is an open problem of the category**, and the honest report is that only the level sets of the Green's function on the regular part have controlled dimension.

**Remark (the singular part is not negligible).** At the parameter zero the singular part of the Julia set contains the real four-dimensional idempotent surface; for other parameters the intersection of the Julia set with the critical hypersurface is not known to be small, and no argument that it is of measure zero in the fractal is available. **Any dimension theory of the biquaternion fractals must handle the singular part separately, and the singular part can carry dimension**, which is the reason the article treats it before the general theory rather than after it.

## Summary

The Hausdorff dimension of a biquaternion Julia set is known in three situations. On a slice it is the dimension of the corresponding classical fractal: the complex dimension on the central slice, the quaternion dimension on the quaternion slice, and on an idempotent plane the maximum of the two products of one boundary and one filled complex Julia set, by the product formula. At the parameter zero the filled Julia set is full-dimensional, of dimension eight, the Julia set is the spectral hypersurface of dimension seven, and the idempotent surface gives the singular part dimension at least four. At a central parameter whose complex filled Julia set has interior the filled set is again full-dimensional, and in general the dimension is at most four plus twice the dimension of the complex Julia set, with equality expected and proved at the parameter zero. For a non-central parameter no formula is known and the singular part of the fractal is not known to be negligible; the general dimension problem is open.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\dim_H$ | Hausdorff dimension |
| $\mathcal K_{\tilde C}$, $J_{\tilde C}$ | the filled Julia set and the Julia set |
| $K_C$, $J_C$ | the complex filled Julia set and Julia set |
| $\rho(\Phi(\tilde Q))$ | the spectral radius of the matrix model |
| $W_{\tilde\Pi}$ | the idempotent plane $\mathbb{C}\tilde\Pi\oplus\mathbb{C}\tilde\Pi'$ |
| $\mathscr{Z}$ | the zero-divisor cone |
| $\alpha=\dim_HK_C$ | the dimension of the complex filled Julia set |

## Further Reading

- *Fractal Geometry* (`articles_maths/fractal-geometry.md`), for the definition of the dimension and the product formula.
- *The Slices of the Biquaternion Julia Sets* (`articles_maths/the-slices-of-the-biquaternion-julia-sets.md`), for the slices whose dimensions are computed here.
- *The Idempotent Decomposition and the Split Fractal* (`articles_maths/the-idempotent-decomposition-and-the-split-fractal.md`), for the product structure of the idempotent slice.
- *The Zero Divisors and the Singular Julia Sets* (`articles_maths/the-zero-divisors-and-the-singular-julia-sets.md`), for the idempotent surface and the singular part.
- *The Biquaternion Iterated Function Systems* (`articles_maths/the-biquaternion-iterated-function-systems.md`), for the similarity dimension of a system, which is the constructive counterpart.
