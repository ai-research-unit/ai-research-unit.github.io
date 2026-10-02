# __The Shape Operator__

## Introduction

A hypersurface in a Riemannian manifold carries one piece of data beyond its own induced metric, and it is the way it bends. The bending is measured by the **shape operator**, the operator on the tangent bundle of the hypersurface that is the derivative of the unit normal field: to each tangent direction it assigns the tangential part of the change of the normal in that direction. The same data is read as a symmetric tensor, the **second fundamental form**; the operator and the tensor are related by the metric, and the article takes the operator as the object, because the principal curvatures are its eigenvalues and because the two fundamental equations of the theory, of Gauss and of Codazzi, are statements about it.

The article develops the shape operator of a hypersurface. It defines the operator, proves that it is self-adjoint for the induced metric, and reads the Gauss and the Weingarten formulas that decompose the ambient covariant derivative into the intrinsic part and the normal part; it proves the **Gauss equation**, which computes the curvature of the hypersurface from the ambient curvature and the operator, and the **Codazzi equation**, which computes the normal component of the ambient curvature from the derivative of the operator; it identifies the principal curvatures, the mean curvature and the Gauss–Kronecker curvature as the eigenvalues, the trace and the determinant of the operator; and it works the examples of the sphere, the hyperplane and the cylinder. The operator is the hypersurface case of the second fundamental form of a submanifold, and it is the operator whose self-adjointness is the geometric source of the adjoint structure developed elsewhere in this category.

The article assumes the metric, the Levi-Civita connection and the curvature of *Curvature and Geodesics* and *Riemannian Geometry*, and the immersion and the submanifold of *Smooth Manifolds and Differential Geometry*. The curvature operator and the Gauss equation in operator form are *The Curvature Operator* of this group; the mean curvature flow and the minimal surfaces are the synthesis of this Part, and the form-defined side of the operator is *The Adjoint of the Geodesic Operator* later in this category. No physics is invoked.

## The Shape Operator of a Hypersurface

### The Setting

Let $f : N^n \to \bar M^{n+1}$ be an immersion of an $n$-dimensional manifold into a Riemannian manifold $(\bar M, \bar g)$; the induced metric is $g = f^*\bar g$, and $N$ is a **hypersurface** when the immersion is of codimension one. Suppose in addition that $N$ is **two-sided**, so that there is a globally defined unit normal field $\nu$ along $f$:

$$
\bar g(\nu, \nu) = 1, \qquad \bar g\bigl(df(X), \nu\bigr) = 0
$$

for every tangent vector $X$, and the tangent space of $\bar M$ at a point of $N$ splits as $T\bar M = df(TN)\oplus\mathbb{R}\nu$. The immersion is identified with its image and a tangent vector $X$ of $N$ with $df(X)$; a bar marks an object of $\bar M$, and no bar marks an object of $N$. The two-sidedness is automatic when $N$ and $\bar M$ are orientable, and it is the standing assumption of the article.

**Definition.** The **shape operator** of the hypersurface is the endomorphism of the tangent bundle

$$
A : TN \longrightarrow TN, \qquad A(X) = -\bigl(\bar\nabla_X\nu\bigr)^{\top},
$$

the tangential part of the negative of the ambient covariant derivative of the normal in the direction $X$; the **second fundamental form** is the symmetric $(0, 2)$-tensor

$$
\mathrm{II}(X, Y) = g(A(X), Y),
$$

and the shape operator is the $g$-adjoint of the second fundamental form, $g(A(X), Y) = \mathrm{II}(X, Y)$.

**Proposition.** The shape operator is well defined, it is smooth, and it is characterised by the two **fundamental formulas**

$$
\bar\nabla_XY = \nabla_XY + \mathrm{II}(X, Y)\,\nu \qquad \text{(Gauss)}, \qquad
\bar\nabla_X\nu = -A(X) \qquad \text{(Weingarten)},
$$

where $\nabla$ is the Levi-Civita connection of the induced metric $g$. In particular the normal part of $\bar\nabla_XY$ is $\mathrm{II}(X,Y)\nu$, the tangential part is $\nabla_XY$, and $\bar\nabla_X\nu$ is tangent, since $\bar g(\bar\nabla_X\nu, \nu) = \frac12X\bar g(\nu,\nu) = 0$.

**Proof.** Decompose $\bar\nabla_XY$ into its tangential and normal parts; the tangential part defines a connection $\nabla$ on $TN$, and the normal part is some multiple of $\nu$, written $\mathrm{II}(X,Y)$. The same decomposition applied with $Y$ replaced by the normal gives $\bar\nabla_X\nu$, which is tangent by the computation above, and the definition of $A$ names its tangential part. The connection $\nabla$ is the Levi-Civita connection of $g$: it is metric because $\bar\nabla$ is and $\mathrm{II}$ is normal, and it is torsion-free because $\bar\nabla$ is and the normal components agree, $\mathrm{II}(X,Y)=\mathrm{II}(Y,X)$, both being the $\nu$-component of the symmetric quantity $\bar\nabla_XY-\bar\nabla_YX = [X,Y]$. Smoothness is the smoothness of $\nu$ and of $\bar\nabla$.

### Self-Adjointness

**Theorem.** The shape operator is self-adjoint for the induced metric:

$$
g\bigl(A(X), Y\bigr) = g\bigl(Y, A(X)\bigr) = g\bigl(X, A(Y)\bigr) \qquad \text{equivalently} \qquad \mathrm{II}(X, Y) = \mathrm{II}(Y, X) .
$$

**Proof.** The torsion-free property of $\bar\nabla$ gives $\bar\nabla_XY - \bar\nabla_YX = [X, Y]$, which is tangent; taking normal parts and using the Gauss formula, the left side has normal part $\mathrm{II}(X,Y)\nu - \mathrm{II}(Y,X)\nu$, and the right side has no normal part, so $\mathrm{II}(X,Y)=\mathrm{II}(Y,X)$. Passing from the tensor to the operator by the metric gives $g(A(X),Y)=g(X,A(Y))$, since $g(A(X),Y)=\mathrm{II}(X,Y)=\mathrm{II}(Y,X)=g(A(Y),X)=g(X,A(Y))$.

**Corollary.** The shape operator is diagonalisable in an orthonormal basis at each point, and its eigenvalues are real. They are the **principal curvatures** $\kappa_1, \ldots, \kappa_n$ of the hypersurface; the **mean curvature** is their mean, $H = \frac{1}{n}\operatorname{tr}A$, and the **Gauss–Kronecker curvature** is their product, $K = \det A$. The hypersurface is **totally geodesic** when $A = 0$, **totally umbilic** when $A = \lambda\,\mathrm{id}$ for a function $\lambda$, and **minimal** when $H = 0$.

## The Gauss and Codazzi Equations

### The Gauss Equation

**Theorem (Gauss).** For tangent vectors $X, Y, Z, W$ of $N$, the curvature tensors of $N$ and of $\bar M$ are related by

$$
\bar R(X, Y, Z, W) = R(X, Y, Z, W) + \mathrm{II}(X, Z)\,\mathrm{II}(Y, W) - \mathrm{II}(X, W)\,\mathrm{II}(Y, Z),
$$

equivalently, in operator form,

$$
\bar R(X, Y, Z, W) = R(X, Y, Z, W) + g\bigl((A\wedge A)(X\wedge Y), Z\wedge W\bigr),
$$

where $A\wedge A$ denotes the self-adjoint operator on $\Lambda^2TN$ induced by $A$ and the metric, $(A\wedge A)(X\wedge Y) = A(X)\wedge A(Y)$.

**Proof.** Compute $\bar\nabla_X\bar\nabla_YZ$ with the Gauss formula and the Weingarten formula:

$$
\bar\nabla_X\bar\nabla_YZ = \bar\nabla_X\bigl(\nabla_YZ + \mathrm{II}(Y,Z)\nu\bigr)
= \nabla_X\nabla_YZ + \mathrm{II}(X,\nabla_YZ)\,\nu + X\bigl(\mathrm{II}(Y,Z)\bigr)\nu - \mathrm{II}(Y,Z)\,A(X).
$$

The tangential part is $\nabla_X\nabla_YZ - \mathrm{II}(Y,Z)A(X)$ and the normal part is $\mathrm{II}(X,\nabla_YZ)\nu + X(\mathrm{II}(Y,Z))\nu$. Subtracting the same expression with $X$ and $Y$ exchanged and subtracting $\bar\nabla_{[X,Y]}Z$, the normal parts cancel by the torsion-freeness of $\nabla$, and the tangential part is $\bar R(X,Y)Z + \mathrm{II}(Y,Z)A(X) - \mathrm{II}(X,Z)A(Y)$. Pairing with $W$ and using $g(A(X),W) = \mathrm{II}(X,W)$ gives the first display, and the second is its reading through the inner product on bivectors with $(A\wedge A)$.

**Corollary (the hypersurface case of the Gauss theorem of surfaces).** When $\bar M$ is flat and $n = 2$, the curvature of the surface is the determinant of the operator, $K = \det A = \kappa_1\kappa_2$, the **Theorema Egregium**, and the Gauss–Kronecker curvature of the definition coincides with the Gaussian curvature of the induced metric.

**Proof.** With $\bar R = 0$ the Gauss equation gives $R(X,Y,Z,W) = \mathrm{II}(X,W)\mathrm{II}(Y,Z)-\mathrm{II}(X,Z)\mathrm{II}(Y,W)$. For an orthonormal basis $X,Y$ of the tangent plane, $K = R(X,Y,Y,X) = \mathrm{II}(X,X)\mathrm{II}(Y,Y)-\mathrm{II}(X,Y)^2 = \det(\mathrm{II}) = \det A$ in the basis that diagonalises $A$, which is the product of the principal curvatures.

### The Codazzi Equation

**Definition.** The **covariant derivative of the shape operator** is

$$
(\nabla_XA)(Y) = \nabla_X\bigl(A(Y)\bigr) - A(\nabla_XY),
$$

and the covariant derivative of the second fundamental form is $(\nabla_X\mathrm{II})(Y,Z) = g\bigl((\nabla_XA)(Y), Z\bigr)$.

**Theorem (Codazzi).** For tangent vectors $X, Y, Z$,

$$
\bar R(X, Y, Z, \nu) = (\nabla_X\mathrm{II})(Y, Z) - (\nabla_Y\mathrm{II})(X, Z) = g\bigl((\nabla_XA)(Y) - (\nabla_YA)(X),\, Z\bigr),
$$

where $\bar R(X,Y,Z,\nu) = \bar g(\bar R(X,Y)Z, \nu)$ is the normal component of the ambient curvature.

**Proof.** From the computation of $\bar\nabla_X\bar\nabla_YZ$ in the proof of the Gauss equation, the normal part of $\bar R(X,Y)Z$ is

$$
\mathrm{II}(X,\nabla_YZ) + X\bigl(\mathrm{II}(Y,Z)\bigr) - \mathrm{II}(Y,\nabla_XZ) - Y\bigl(\mathrm{II}(X,Z)\bigr) - \mathrm{II}([X,Y],Z).
$$

Substituting $X(\mathrm{II}(Y,Z)) = (\nabla_X\mathrm{II})(Y,Z) + \mathrm{II}(\nabla_XY,Z) + \mathrm{II}(Y,\nabla_XZ)$ and the analogous expression for $Y(\mathrm{II}(X,Z))$, the eight extra terms and the term $\mathrm{II}([X,Y],Z)$ cancel in pairs by the symmetry $\mathrm{II}(X,Y)=\mathrm{II}(Y,X)$ and the identity $[X,Y]=\nabla_XY-\nabla_YX$, leaving the displayed difference.

**Corollary.** When the ambient space is flat the shape operator is **Codazzi**, $(\nabla_XA)(Y)=(\nabla_YA)(X)$; the Gauss and the Codazzi equations are the integrability conditions of the immersion, and a simply connected hypersurface is determined up to an ambient isometry by its metric and its shape operator satisfying both, the fundamental theorem of the hypersurface theory.

## Examples and the Constant-Curvature Ambient

**Example (the sphere).** For the sphere of radius $r$ in Euclidean space, $N = S^n_r$, the outward unit normal is $\nu(x) = x/r$ and the ambient derivative is the Euclidean one, so $A(X) = -\bar\nabla_X(x/r) = -X/r$, that is $A = -\frac{1}{r}\mathrm{id}$ with the outward normal and $A = \frac1r\mathrm{id}$ with the inward one. All principal curvatures are equal, the hypersurface is totally umbilic, the mean curvature is $\pm1/r$, and the Gauss equation gives $K = 1/r^2$ for the Gaussian curvature of the two-sphere, and the sectional curvature $1/r^2$ in every dimension.

**Example (the hyperplane and the cylinder).** For a hyperplane in Euclidean space the normal is constant, so $A = 0$ and the hypersurface is totally geodesic; its geodesics are the straight lines of the ambient, and the Gauss equation gives the flat intrinsic curvature. For the cylinder $S^1_r\times\mathbb{R}$ in $\mathbb{R}^3$ with the outward normal in the plane, the operator is $\mathrm{diag}(1/r, 0)$ in the orthonormal frame of the circle direction and the axis direction: one principal curvature is $1/r$ and the other is $0$, the mean curvature is $1/(2r)$, and the Gauss curvature is $\det A = 0$.

**Theorem (curvature of a hypersurface of a space form).** If the ambient has constant curvature $\bar\lambda$, then for an orthonormal tangent frame that diagonalises $A$ with principal curvatures $\kappa_i$, the sectional curvature of $N$ on the plane spanned by the $i$-th and $j$-th directions is

$$
K_{ij} = \bar\lambda + \kappa_i\kappa_j .
$$

**Proof.** Apply the Gauss equation with $X = e_i$, $Y = e_j$, $Z = e_j$ and $W = e_i$ and use $\bar R(e_i,e_j,e_j,e_i) = \bar\lambda$:

$$
R(e_i, e_j, e_j, e_i) = \bar\lambda - \mathrm{II}(e_i, e_j)\mathrm{II}(e_j, e_i) + \mathrm{II}(e_i, e_i)\mathrm{II}(e_j, e_j) = \bar\lambda - \mathrm{II}(e_i, e_j)^2 + \kappa_i\kappa_j .
$$

In a frame that diagonalises $A$ the off-diagonal entry $\mathrm{II}(e_i,e_j)$ vanishes for $i \neq j$, so $K_{ij} = R(e_i,e_j,e_j,e_i) = \bar\lambda + \kappa_i\kappa_j$, which agrees with the sphere, where $\bar\lambda = 0$ and $\kappa_i\kappa_j = 1/r^2$, and with the cylinder, where one curvature is $0$.

## Summary

For a two-sided hypersurface $N$ of a Riemannian manifold $\bar M$ with unit normal $\nu$, the **shape operator** $A(X) = -(\bar\nabla_X\nu)^{\top}$ is the derivative of the normal, an endomorphism of $TN$, and the **second fundamental form** $\mathrm{II}(X,Y) = g(A(X),Y)$ is the symmetric tensor $g$-dual to it. The Gauss formula $\bar\nabla_XY = \nabla_XY + \mathrm{II}(X,Y)\nu$ and the Weingarten formula $\bar\nabla_X\nu = -A(X)$ decompose the ambient derivative, and the connection $\nabla$ they induce on $N$ is the Levi-Civita connection of the induced metric.

The shape operator is self-adjoint, equivalently $\mathrm{II}$ is symmetric; its eigenvalues are the **principal curvatures** $\kappa_1,\ldots,\kappa_n$, its trace is $n$ times the mean curvature, and its determinant is the Gauss–Kronecker curvature. The **Gauss equation** writes the ambient curvature as the intrinsic curvature plus the quadratic expression in $\mathrm{II}$, the operator form being the addition of $A\wedge A$; when the ambient is flat and $n=2$ it reduces to $K=\det A$, the Theorema Egregium. The **Codazzi equation** identifies the normal component of the ambient curvature with the antisymmetrised covariant derivative of $\mathrm{II}$, so a flat ambient has a Codazzi shape operator; Gauss and Codazzi together are the integrability conditions that determine the hypersurface up to an ambient isometry from its metric and its shape operator. On a space form of curvature $\bar\lambda$ the sectional curvature on the $i,j$ plane is $\bar\lambda + \kappa_i\kappa_j$; the sphere is totally umbilic with $A = \pm\frac1r\mathrm{id}$, the hyperplane is totally geodesic, and the cylinder has the principal curvatures $1/r$ and $0$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(\bar M, \bar g)$, $N$, $f$ | Ambient manifold, hypersurface and immersion; bars for ambient objects |
| $\nu$ | Unit normal field, $\bar g(\nu,\nu)=1$ |
| $g = f^*\bar g$ | Induced metric on the hypersurface |
| $A(X) = -(\bar\nabla_X\nu)^{\top}$ | Shape operator (Weingarten map) |
| $\mathrm{II}(X,Y) = g(A(X),Y)$ | Second fundamental form; symmetric |
| $\bar\nabla_XY = \nabla_XY + \mathrm{II}(X,Y)\nu$ | Gauss formula |
| $\bar\nabla_X\nu = -A(X)$ | Weingarten formula |
| $\kappa_1,\ldots,\kappa_n$ | Principal curvatures; eigenvalues of $A$ |
| $H = \frac1n\operatorname{tr}A$, $K = \det A$ | Mean curvature; Gauss–Kronecker curvature |
| $A=0$, $A=\lambda\mathrm{id}$, $H=0$ | Totally geodesic; totally umbilic; minimal |
| Gauss equation | $\bar R = R + \mathrm{II}\wedge\mathrm{II}$; operator form with $A\wedge A$ |
| Codazzi equation | $\bar R(X,Y,Z,\nu) = (\nabla_X\mathrm{II})(Y,Z)-(\nabla_Y\mathrm{II})(X,Z)$ |
| $K_{ij} = \bar\lambda+\kappa_i\kappa_j$ | Sectional curvature of a hypersurface of a space form |

## Further Reading

- Manfredo P. do Carmo, *Riemannian Geometry* (Birkhäuser, 1992), for the second fundamental form, the Gauss map and the fundamental equations of the hypersurface theory.
- Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry, Volume II* (Interscience, 1969), for the submanifold theory, the Gauss and Codazzi equations and the fundamental theorem.
- Michael Spivak, *A Comprehensive Introduction to Differential Geometry, Volume IV* (Publish or Perish, 1979), for the classical theory of surfaces, the shape operator and the Theorema Egregium.
- Barrett O'Neill, *Semi-Riemannian Geometry with Applications to Relativity* (Academic Press, 1983), for the shape operator in the general signature and the hypersurface examples.
- Wolfgang Kühnel, *Differential Geometry: Curves—Surfaces—Manifolds*, 3rd ed. (American Mathematical Society, 2015), for the principal curvatures, the mean and Gauss curvatures and the examples.
