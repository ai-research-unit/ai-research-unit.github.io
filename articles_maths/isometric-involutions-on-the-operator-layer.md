# __Isometric Involutions on the Operator Layer__

## Introduction

The **operator layer** of a Riemannian manifold is the algebra of the differential operators built from the metric and the Levi-Civita connection: the covariant derivatives, the Laplacian, the curvature endomorphisms, and the operators assembled from them. An isometric involution acts on this layer by **conjugation**, $T\mapsto\sigma T\sigma^{-1}$, an order-two automorphism that preserves the order filtration, the metric, the connection and the curvature; its **fixed operators** commute with the involution and descend to the quotient, and its **skew operators** anticommute with it and live on the twisted layer. The involution also interacts with the **adjoint**: because it is an isometry, the conjugation commutes with the formal adjoint, $(\sigma T\sigma^{-1})^{*} = \sigma T^{*}\sigma^{-1}$, so the involutions preserve the self-adjoint operators and the skew-adjoint operators, and the symmetry of the curvature and the self-adjointness of the geodesic operator of the preceding article are instances.

The article develops the operator layer with an isometric involution. It defines the layer as the algebra of the metric operators, exhibits the action of the involution by conjugation, and proves that it is an order-two automorphism preserving the order filtration; it splits the layer into the fixed and the skew operators, proves the $\mathbb{Z}/2$-graded multiplication, and identifies the fixed subalgebra with the operator layer of the quotient; it defines the adjoint for the $L^2$ pairing of the Riemannian density and proves that the conjugation commutes with the adjoint, so that the involution preserves the self-adjoint and the skew-adjoint operators; and it reads the Laplacian, the geodesic operator and the curvature operator as examples of fixed operators, and the signed operators as the skew ones.

The article assumes the isometries, the Killing fields and the fixed sets of *Isometries as Operators*, the geodesic operator and the adjoint from *The Adjoint of the Geodesic Operator* and the curvature operator from *The Curvature Operator* of this category; the isometric involutions, the quotient and the descent from the two involution articles of this category; the smooth operator layer, the conjugation and the descent from *Real Structures on a Smooth Manifold* of Part III and *Real Structures on the Operator Layer* of Part I, whose notation $\mathrm{ad}_\sigma$, $T^{*}$ and the eigenspaces $\mathcal{D}_\pm$ are used. The Hermitian case is *Hermitian Manifolds and the Adjoint*, the following article of this category, and it is named as a forward reference. No physics is invoked.

## The Operator Layer of a Riemannian Manifold

### The Algebra of the Metric Operators

**Definition.** The **operator layer** of a Riemannian manifold $(M, g)$ is the algebra $\mathcal{D}(M, g)$ of the differential operators on the tensor fields of $M$ that are assembled from the metric and the Levi-Civita connection: the multiplication by functions and tensors, the covariant derivative $\nabla_X$, the Lie derivative $\mathcal{L}_X$, the curvature endomorphisms $R(X,Y)$, the Laplace–Beltrami operator $\Delta = \operatorname{tr}_g\nabla^2$, and their compositions and linear combinations with the coefficients depending on the geometry. It is an algebra under composition, filtered by the order, and its zeroth order is the algebra of the functions and the tensors, its first order the derivations and the covariant derivatives. The smooth operator layer of *Real Structures on a Smooth Manifold* of Part III is the specialisation in which no metric is present, and the present layer is the metric-refined sheaf whose structure group is the orthogonal group.

**Proposition.** The layer is generated over the functions by the covariant derivatives, and it is the sheaf of the differential operators of the category; it is acted on by the isometry group by conjugation, $F\cdot T = F\,T\,F^{-1}$, this action preserving the order filtration, the metric, the volume density and the curvature.

**Proof.** The generation by the covariant derivatives is the generation of the smooth operator layer together with the algebraic operations involving the metric; an isometry preserves the metric, hence the Levi-Civita connection, the curvature, the density and the order of an operator, so conjugation is an algebra automorphism preserving the filtration. The details are those of *Real Structures on a Smooth Manifold* and *The Sheaf of Differential Operators*.

### The Action of the Isometric Involution

**Definition.** Let $\sigma$ be an isometric involution of $(M, g)$, as in the preceding articles of this category. Its action on the operator layer is the **conjugation**

$$
\mathrm{ad}_\sigma : \mathcal{D}(M, g) \longrightarrow \mathcal{D}(M, g), \qquad
\mathrm{ad}_\sigma(T) = \sigma\,T\,\sigma^{-1},
$$

where $\sigma$ acts on the functions and the tensors by the pullback $\sigma^{*}$ and on the operators by conjugation; on the functions, $\mathrm{ad}_\sigma(f) = \sigma^{*}f = f\circ\sigma$.

**Theorem.** The conjugation is an order-two algebra automorphism of the operator layer,

$$
\mathrm{ad}_\sigma(ST) = \mathrm{ad}_\sigma(S)\,\mathrm{ad}_\sigma(T), \qquad
\mathrm{ad}_\sigma(\mathrm{id}) = \mathrm{id}, \qquad
\mathrm{ad}_\sigma^2 = \mathrm{id},
$$

it is an isometry of the layer for the pairing below, it preserves the order filtration and the associated graded, and it fixes the metric, the Levi-Civita connection, the curvature operator and the Riemannian density. Consequently it acts on the covariant derivative by $\mathrm{ad}_\sigma(\nabla_X) = \nabla_{d\sigma(X)}$ and on the curvature endomorphism by $\mathrm{ad}_\sigma(R(X,Y)) = R(d\sigma X, d\sigma Y)$.

**Proof.** Conjugation by an invertible map is an algebra automorphism, of order two when the map is an involution; the conjugation by an isometry preserves the metric, the connection and the curvature because these are built from the metric functorially, so $\sigma\nabla_X\sigma^{-1} = \nabla_{d\sigma X}$ and the same for the curvature; it preserves the order filtration because an isometry carries a differential operator of order $m$ to one of order $m$. This is the Riemannian case of the conjugation of *Real Structures on the Operator Layer* of Part I.

## The Fixed Operators and the Skew Operators

### The Eigenspaces

**Definition.** The **fixed operators** and the **skew operators** of the involution are the two eigenspaces of the conjugation,

$$
\mathcal{D}_+ = \{T : \mathrm{ad}_\sigma(T) = T\}, \qquad
\mathcal{D}_- = \{T : \mathrm{ad}_\sigma(T) = -T\},
$$

and, when $2$ is invertible, the layer decomposes as $\mathcal{D}(M,g) = \mathcal{D}_+\oplus\mathcal{D}_-$, with every operator split as $T = T_+ + T_-$, $T_+ = \tfrac12(T+\mathrm{ad}_\sigma T)$ and $T_- = \tfrac12(T-\mathrm{ad}_\sigma T)$.

**Theorem.** The decomposition is direct and the multiplication is $\mathbb{Z}/2$-graded:

$$
\mathcal{D}_+\mathcal{D}_+ \subseteq \mathcal{D}_+, \qquad
\mathcal{D}_+\mathcal{D}_- \subseteq \mathcal{D}_-, \qquad
\mathcal{D}_-\mathcal{D}_- \subseteq \mathcal{D}_+,
$$

the fixed operators form a subalgebra, and the skew operators form a module over it. The metric, the Levi-Civita connection, the curvature, the curvature operator, the Laplacian and the geodesic operator are fixed operators; the operators that change sign under the involution are the skew ones, and the sign is the sign of the transformation of the operator by the reflection $y\mapsto-y$ of the normal coordinates.

**Proof.** The eigenspace statements follow from $\mathrm{ad}_\sigma^2=\mathrm{id}$ and the identity $\mathrm{ad}_\sigma(ST)=\mathrm{ad}_\sigma(S)\mathrm{ad}_\sigma(T)$, which multiplies the eigenvalue signs; this is the graded algebra of *Real Structures on the Operator Layer*. The named operators are fixed because the conjugation fixes each of the functorial constructions from which they are built, by the previous theorem; the operator of the reversal of a geodesic is fixed by *The Adjoint of the Geodesic Operator*.

### The Fixed Subalgebra and the Skew Module

**Proposition.** The fixed subalgebra $\mathcal{D}_+$ is the operator layer of the quotient $M/\sigma$: a fixed operator preserves the $\sigma$-invariant tensors and the $\sigma$-anti-invariant tensors separately, so it descends to an operator on the quotient, and the descent is an algebra isomorphism from $\mathcal{D}_+$ onto the operator layer of $M/\sigma$ when the involution is free. The skew module $\mathcal{D}_-$ carries the $\sigma$-anti-invariant tensors to themselves, and it is the module of the operators on the twisted layer.

**Proof.** A fixed operator commutes with the involution, hence preserves the eigenspaces of the action on the sections, so it carries the invariant sections to the invariant sections and the anti-invariant sections to the anti-invariant sections; the invariant sections are the functions and the tensors of the quotient, and the descent is bijective in the free case because the invariant sections and the quotient sections are the same. The anti-invariant sections are the sections of the twisted bundle, which is the bundle associated to the sign representation of $\langle\sigma\rangle$, and the skew operators act on them; this is the descent of *Real Structures on a Smooth Manifold*.

## The Adjoint

### The Adjoint Commutes with the Involution

**Definition.** The **adjoint** of an operator $T$ on the sections is the operator $T^{*}$ with

$$
\langle Tx, y\rangle = \langle x, T^{*}y\rangle
$$

for the **$L^2$ pairing** of the sections,

$$
\langle x, y\rangle = \int_M \langle x, y\rangle_g\,d\mu, \qquad d\mu \text{ the Riemannian density},
$$

when it exists; the operator is **self-adjoint** when $T^{*}=T$ and **skew-adjoint** when $T^{*}=-T$. The pairing uses the density rather than the signed volume form, so that it is defined without an orientation.

**Theorem.** The pullback $\sigma^{*}$ of an isometric involution is self-adjoint and unitary for the $L^2$ pairing, and it is an involution,

$$
(\sigma^{*})^{*} = \sigma^{*}, \qquad (\sigma^{*})^{-1} = \sigma^{*}, \qquad \langle \sigma^{*}x, \sigma^{*}y\rangle = \langle x, y\rangle,
$$

so that the conjugation commutes with the adjoint:

$$
\bigl(\mathrm{ad}_\sigma(T)\bigr)^{*} = (\sigma\,T\,\sigma^{-1})^{*} = \sigma\,T^{*}\,\sigma^{-1} = \mathrm{ad}_\sigma(T^{*}).
$$

Consequently the involution preserves the self-adjoint operators and the skew-adjoint operators: a fixed self-adjoint operator has a fixed adjoint, and the eigenspaces $\mathcal{D}_{\pm}$ are stable under the adjoint operation when the operator is self-adjoint or skew-adjoint respectively.

**Proof.** Since the involution is an isometry, the change of variables $x\mapsto\sigma(x)$ has the Jacobian equal to $1$ for the Riemannian density, so

$$
\langle \sigma^{*}f, g\rangle = \int (f\circ\sigma)\bar g\,d\mu = \int f\,(\bar g\circ\sigma)\,d\mu = \langle f, \sigma^{*}g\rangle ,
$$

which is the self-adjointness, and $\langle\sigma^{*}f,\sigma^{*}g\rangle = \langle f,g\rangle$, which is the unitarity; the involution follows from $\sigma^2=\mathrm{id}$. Then

$$
\langle \sigma T\sigma^{-1}x, y\rangle = \langle T\sigma^{-1}x, \sigma^{-1}y\rangle = \langle \sigma^{-1}x, T^{*}\sigma^{-1}y\rangle = \langle x, \sigma T^{*}\sigma^{-1}y\rangle ,
$$

using $\sigma^{*}=\sigma^{-1}$ and the self-adjointness; hence the adjoint of the conjugate is the conjugate of the adjoint. The last statement follows because the conjugation is an algebra isomorphism preserving the involution $\sigma$, so it carries the solutions of $T^{*}=T$ to the solutions of $T^{*}=T$ in the fixed part.

**Corollary.** The Laplace–Beltrami operator is self-adjoint and fixed; the geodesic operator is self-adjoint and fixed by the reversal of the geodesic; the curvature operator is self-adjoint and fixed; the covariant derivative is skew-adjoint for the fields with vanishing boundary conditions and is fixed by the involution. The self-adjointness of the geodesic operator and the symmetry of the curvature of the preceding articles are the instances of the commutation of the conjugation with the adjoint.

### Self-Adjoint Operators and the Eigenspaces

**Proposition.** A self-adjoint fixed operator descends to a self-adjoint operator on the quotient; a self-adjoint skew operator is a bounded operator of the twisted layer whose square is a fixed positive operator. The spectrum of a fixed self-adjoint operator is invariant under the involution in the sense that the eigenfunctions can be chosen invariant or anti-invariant, and the trace of the involution on the finite-dimensional eigenspaces, where it exists, is the **equivariant index** of the operator.

**Proof.** The descent of the fixed self-adjoint operator is the previous proposition, and the adjoint is preserved by the previous theorem, so the descended operator is self-adjoint. A skew self-adjoint operator $T$ satisfies $\mathrm{ad}_\sigma T=-T$ and $T^{*}=T$, so $T^2$ satisfies $\mathrm{ad}_\sigma T^2=+T^2$ and $(T^2)^{*}=(T^*)^2=T^2$, which is the statement. The spectrum statement is that the finite-dimensional eigenspaces of a fixed self-adjoint operator are representations of $\mathbb{Z}/2$ and split into the invariant and the anti-invariant parts; the trace of the involution on them is the equivariant index, whose theory is the Lefschetz index of the involution.

## Examples

**Example (the flat reflection).** On $\mathbb{R}^n$ with the reflection $\sigma(x_1, x') = (-x_1, x')$ the operator layer splits into the operators preserving the parity of the first variable and those reversing it; the Laplacian is fixed, the operator $\partial/\partial x_1$ is skew, and the fixed operators descend to the half-space; the derivative $\partial/\partial x_1$ anticommutes with the reflection because the coordinate changes sign, which is the skew case at the level of the first-order operators.

**Example (the antipodal quotient).** On the sphere $S^n$ with the antipodal map the Laplacian is fixed and descends to the Laplacian of $\mathbb{RP}^n$; the eigenfunctions of the Laplacian split into the even ones, which are the functions of the quotient, and the odd ones, which are the sections of the twisted bundle; the trace of the involution on an eigenspace is the difference of the even and the odd dimensions, and it appears in the spectrum of the projective space through the selection rule. The geodesic operator is fixed by the reversal, and the curvature operator is fixed.

**Example (the geodesic operator and its adjoint).** The geodesic operator $L_\gamma = \frac{D^2}{dt^2}+\mathcal R_{\dot\gamma}$ is fixed by the reversal of the geodesic and is self-adjoint; the covariant derivative $\frac{D}{dt}$ is skew-adjoint and skew with respect to the reversal in the appropriate sense; the index form is the fixed part of the quadratic form. This is the example from which the whole operator-layer picture is abstracted, and it is the content of *The Adjoint of the Geodesic Operator*.

## Summary

The **operator layer** of a Riemannian manifold is the algebra of the differential operators built from the metric and the Levi-Civita connection; an isometric involution acts on it by the **conjugation** $\mathrm{ad}_\sigma(T)=\sigma T\sigma^{-1}$, an order-two algebra automorphism preserving the order filtration and fixing the metric, the connection, the curvature and the density. The layer splits into the **fixed operators** $\mathcal{D}_+$ and the **skew operators** $\mathcal{D}_-$, with the $\mathbb{Z}/2$-graded multiplication $\mathcal{D}_+\mathcal{D}_+\subseteq\mathcal{D}_+$, $\mathcal{D}_+\mathcal{D}_-\subseteq\mathcal{D}_-$, $\mathcal{D}_-\mathcal{D}_-\subseteq\mathcal{D}_+$; the fixed operators form a subalgebra and are the operator layer of the quotient $M/\sigma$, and the skew operators form the module of the operators on the twisted layer.

For the $L^2$ pairing with the Riemannian density, the pullback of an isometric involution is self-adjoint, unitary and involutive, so the conjugation commutes with the adjoint, $(\mathrm{ad}_\sigma T)^{*}=\mathrm{ad}_\sigma(T^{*})$; the involution therefore preserves the self-adjoint operators and the skew-adjoint operators. The Laplacian, the curvature operator and the geodesic operator are self-adjoint and fixed; the covariant derivative is skew-adjoint and fixed; a fixed self-adjoint operator descends to a self-adjoint operator on the quotient; and the trace of the involution on the eigenspaces is the equivariant index. The flat reflection, the antipodal quotient of the sphere and the geodesic operator with its adjoint are the examples, and the Hermitian case, where the adjoint is compared with the complex structure, is *Hermitian Manifolds and the Adjoint*, the following article.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{D}(M,g)$ | Operator layer: the metric differential operators |
| $\mathrm{ad}_\sigma(T)=\sigma T\sigma^{-1}$ | Conjugation by the isometric involution |
| $\mathcal{D}_+$, $\mathcal{D}_-$ | Fixed and skew operators |
| $\mathcal{D}_+\mathcal{D}_-\subseteq\mathcal{D}_-$ etc. | $\mathbb{Z}/2$-graded multiplication |
| $\mathcal{D}_+\cong\mathcal{D}(M/\sigma)$ | Fixed operators are the operator layer of the quotient |
| $\langle x,y\rangle=\int\langle x,y\rangle_g d\mu$ | $L^2$ pairing with the Riemannian density |
| $T^{*}$, $\langle Tx,y\rangle=\langle x,T^{*}y\rangle$ | Adjoint, self-adjoint, skew-adjoint |
| $(\mathrm{ad}_\sigma T)^{*}=\mathrm{ad}_\sigma(T^{*})$ | Conjugation commutes with the adjoint |
| $\sigma^{*}$ self-adjoint, unitary, involutive | The pullback of an isometric involution |
| Equivariant index | Trace of the involution on the eigenspaces |

## Further Reading

- Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry, Volume I* (Interscience, 1963), for the operators on a Riemannian manifold, the Laplacian and the invariant operators.
- Marcel Berger, Paul Gauduchon and Edmond Mazet, *Le spectre d'une variété riemannienne* (Springer, 1971), for the spectral theory of the invariant operators and the quotients.
- Michael Atiyah and Isadore Singer, "The index of elliptic operators III: elliptic operators on homogeneous spaces", *Annals of Mathematics* 87 (1968), 546–604, for the equivariant index and the invariant operators.
- Nicole Berline, Ezra Getzler and Michèle Vergne, *Heat Kernels and Dirac Operators* (Springer, 1992), for the equivariant operators, the index and the supertrace.
- Shoshichi Kobayashi, *Transformation Groups in Differential Geometry* (Springer, 1972), for the invariant operators and the quotients by the transformation groups.
