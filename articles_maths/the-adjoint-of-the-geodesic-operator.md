# __The Adjoint of the Geodesic Operator__

## Introduction

The geodesics of a Riemannian manifold are the integral curves of the geodesic flow, and the linearisation of the flow along a geodesic is the **geodesic operator**: it is the second-order differential operator on the fields along the geodesic that sends a field to its second covariant derivative plus the curvature term, and its kernel is the space of the **Jacobi fields**. The equation it defines is the **Jacobi equation**, $L_\gamma V = 0$, and the operator is its **adjoint**: the covariant derivative along a geodesic is skew-adjoint for the $L^2$ pairing of the fields vanishing at the ends of the geodesic, the square of a skew-adjoint operator is self-adjoint, the curvature term is self-adjoint because the curvature operator is symmetric in the metric, and the sum is therefore self-adjoint. The self-adjointness is what makes the geodesic operator a Sturm–Liouville operator, with a discrete real spectrum and an index that counts the conjugate points.

The article develops the operator and its adjoint. It defines the geodesic operator along a geodesic as the linearisation of the geodesic flow, identifies it with the Jacobi operator $\frac{D^2}{dt^2}+\mathcal{R}_{\dot\gamma}$, and shows that the Jacobi equation is its kernel equation; it defines the $L^2$ pairing on the fields vanishing at the endpoints and proves that the covariant derivative is skew-adjoint and the curvature term self-adjoint, so that the geodesic operator is self-adjoint; it identifies the quadratic form of the operator with the **index form** of the second variation of the energy, and shows that the index form is symmetric and hence defines the self-adjoint operator; and it reads off the consequences for the conjugate points, the Morse index and the nullity.

The article assumes the geodesics, the exponential map, the curvature and the Jacobi fields of *Curvature and Geodesics* and *Riemannian Geometry*, the geodesic flow and the second variation from *The Geodesic Flow Operator*, and the curvature operator, its symmetry and its self-adjointness from *The Curvature Operator*, all in this category. The comparison theorems and the injectivity radius are the subject of *The Conjugate Locus and the Injectivity Radius* in a later category of this Part; the operator-theoretic reading of the self-adjointness is the subject of *Isometric Involutions on the Operator Layer* and *Hermitian Manifolds and the Adjoint*, the following articles of this category. No physics is invoked.

## The Geodesic Operator

### The Linearisation of the Geodesic Flow

**Definition.** Let $\gamma : [a, b] \to M$ be a geodesic with velocity $\dot\gamma$, a parallel field, and let $\mathcal{R}_{\dot\gamma} : T_{\gamma(t)}M \to T_{\gamma(t)}M$ be the **curvature operator in the direction $\dot\gamma$**,

$$
\mathcal{R}_{\dot\gamma}(V) = R(V, \dot\gamma)\dot\gamma ,
$$

the curvature operator of *The Curvature Operator* contracted with the velocity. The **geodesic operator** along $\gamma$ is the second-order operator on the fields along $\gamma$

$$
L_\gamma = \frac{D^2}{dt^2} + \mathcal{R}_{\dot\gamma}, \qquad
L_\gamma(V) = \frac{D^2V}{dt^2} + R(V, \dot\gamma)\dot\gamma ,
$$

where $\frac{D}{dt}$ is the covariant derivative along $\gamma$. A **Jacobi field** is a field with $L_\gamma V = 0$:

$$
\frac{D^2V}{dt^2} + R(V, \dot\gamma)\dot\gamma = 0,
$$

which is the **Jacobi equation**. The geodesic operator is the linearisation of the geodesic flow of *The Geodesic Flow Operator* along the orbit $\gamma$, and the Jacobi fields are the derivatives of the variations of $\gamma$ by geodesics.

**Theorem.** The Jacobi fields along a geodesic form a $2n$-dimensional vector space, $n = \dim M$, and are exactly the fields $V(t) = d(\exp_{\gamma(0)})_{t\dot\gamma(0)}(t\,\xi)$ for $\xi \in T_{\dot\gamma(0)}(T_{\gamma(0)}M)$, that is the images of the linearisation of the exponential map. Along a geodesic the field $t\dot\gamma(t)$ is a Jacobi field, and it is the derivative of the variations of $\gamma$ by the homothetic reparametrisations; the Jacobi fields tangent to the geodesic are the fields $t\dot\gamma(t) + w$ with $w$ parallel.

**Proof.** The Jacobi equation is a linear second-order ordinary differential equation, so its solution space has dimension $2n$. The variation of the geodesic flow by a family of geodesics has derivatives satisfying the Jacobi equation, since the linearisation of $\nabla_{\dot\gamma}\dot\gamma = 0$ gives the equation, and the identification with the differential of the exponential map is the definition of the exponential map along the geodesic; the fields $t\dot\gamma$ and the parallel fields are the explicit solutions in the directions tangent to the geodesic. The details are in *Curvature and Geodesics*.

### The Jacobi Equation

**Proposition.** The geodesic operator is a second-order linear operator with the same principal part as $\frac{D^2}{dt^2}$; the parallel fields are its kernel exactly when the curvature vanishes along $\gamma$, its kernel is the Jacobi fields, and its image consists of the fields that are $L^2$-orthogonal to the kernel of the formal adjoint, which is the operator itself.

**Proof.** The statement about the kernel is the definition of the Jacobi field, and the parallel fields satisfy $L_\gamma V = \mathcal{R}_{\dot\gamma}V$, which vanishes exactly when $\mathcal R_{\dot\gamma} = 0$. The statement about the image is the Fredholm alternative for the self-adjoint operator, which is the theorem of the next section.

## The Adjoint

### The L² Pairing and Integration by Parts

**Definition.** Fix a geodesic $\gamma:[a,b]\to M$ and consider the smooth fields along $\gamma$ with prescribed boundary conditions. The **$L^2$ pairing** of two fields is

$$
\langle V, W\rangle_{L^2} = \int_a^b \langle V(t), W(t)\rangle_{\gamma(t)}\,dt ,
$$

the metric at the running point being the fibre metric, and the space of the fields is completed to a Hilbert space; the **formal adjoint** $L_\gamma^{*}$ of the geodesic operator is the operator with

$$
\langle L_\gamma V, W\rangle_{L^2} = \langle V, L_\gamma^{*}W\rangle_{L^2}
$$

for all smooth fields $V$ and $W$ vanishing at the endpoints $a$ and $b$.

**Theorem.** The covariant derivative along a geodesic is **skew-adjoint** for the $L^2$ pairing with the vanishing boundary conditions,

$$
\left(\frac{D}{dt}\right)^{*} = -\frac{D}{dt},
$$

because $\langle\frac{DV}{dt},W\rangle + \langle V,\frac{DW}{dt}\rangle = \frac{d}{dt}\langle V,W\rangle$ and the boundary term vanishes; the curvature operator in the direction of the geodesic is **self-adjoint**,

$$
\langle \mathcal{R}_{\dot\gamma}(V), W\rangle = \langle V, \mathcal{R}_{\dot\gamma}(W)\rangle,
$$

because the curvature tensor is symmetric in the pairs $(V, \dot\gamma)$ and $(W, \dot\gamma)$; and the geodesic operator is **self-adjoint**,

$$
L_\gamma^{*} = L_\gamma ,
$$

the square of the skew-adjoint derivative being self-adjoint and the sum of two self-adjoint operators being self-adjoint.

**Proof.** Along $\gamma$ the derivative of the function $t\mapsto\langle V(t),W(t)\rangle$ is $\langle\frac{DV}{dt},W\rangle+\langle V,\frac{DW}{dt}\rangle$ by the metricity of the connection, so integrating over $[a,b]$ gives

$$
\langle\tfrac{DV}{dt},W\rangle_{L^2}+\langle V,\tfrac{DW}{dt}\rangle_{L^2} = \langle V,W\rangle\bigr|_a^b = 0
$$

for the fields vanishing at the endpoints, which is the skew-adjointness. The self-adjointness of $\mathcal R_{\dot\gamma}$ is the symmetry $\langle R(X,Y)Z,W\rangle = \langle R(W,Z)Y,X\rangle$ of *The Curvature Operator* evaluated with $Y = Z = \dot\gamma$, which gives $\langle R(V,\dot\gamma)\dot\gamma, W\rangle = \langle V, R(W,\dot\gamma)\dot\gamma\rangle$. The operator $(\frac{D}{dt})^2$ is the composition of two skew-adjoint operators, and $(\frac{D}{dt})^2 = \frac{D}{dt}\circ\frac{D}{dt}$ has the adjoint $(-\frac{D}{dt})\circ(-\frac{D}{dt}) = (\frac{D}{dt})^2$, so it is self-adjoint; hence $L_\gamma = (\frac{D}{dt})^2 + \mathcal R_{\dot\gamma}$ is the sum of two self-adjoint operators and is self-adjoint.

**Corollary.** The eigenfields of the geodesic operator have real eigenvalues and orthogonal eigenspaces, and the operator is diagonalisable in an orthonormal basis of the Hilbert space; the operator is a symmetric Sturm–Liouville operator on the interval, with the same qualitative theory as the scalar Sturm–Liouville problem.

**Proof.** A self-adjoint operator has real eigenvalues, and the eigenspaces of distinct eigenvalues are orthogonal; the compactness of the resolvent on a bounded interval gives the orthonormal basis. The Sturm–Liouville statement is the observation that the equation $L_\gamma V = \lambda V$ has the form of a system of Sturm–Liouville equations with the curvature as the potential.

### The Adjoint on the Operator Layer

**Proposition.** The geodesic operator acts on the operator layer of the fields along the geodesic, and the adjoint operation is the formal adjoint for the $L^2$ pairing; the operator commutes with the reversal of the geodesic, $L_{\gamma^{-1}} = L_\gamma$ read on the fields pulled back by the reversal, so the self-adjointness is compatible with the geodesic involution of *Hermitian Manifolds and the Geodesic Involution*. The self-adjointness of $L_\gamma$ is the operator-layer form of the fact that the curvature operator is symmetric.

**Proof.** The formal adjoint is the operator-layer operation of *Real Structures on the Operator Layer* and of the involutions of the operator layer, and the computation above identifies it with the operator; the reversal of the geodesic carries the covariant derivative to its negative and the curvature term to itself, so the operator is invariant up to the pullback. The last statement is the identification of the curvature term with the symmetric curvature operator.

## The Index Form

### The Second Variation

**Definition.** The **index form** of the geodesic $\gamma$ on the fields vanishing at the endpoints is the symmetric bilinear form

$$
I(V, W) = \int_a^b \Bigl(\bigl\langle \tfrac{DV}{dt}, \tfrac{DW}{dt}\bigr\rangle - \bigl\langle R(V, \dot\gamma)\dot\gamma, W\bigr\rangle\Bigr)\,dt ,
$$

the second variation of the energy of the family of curves with the fields $V$ and $W$ as the variation fields, evaluated at the geodesic.

**Theorem.** The index form is symmetric and is the quadratic form of the geodesic operator: for the fields vanishing at the endpoints,

$$
I(V, W) = \bigl\langle -\tfrac{D^2V}{dt^2} - \mathcal{R}_{\dot\gamma}V,\, W\bigr\rangle_{L^2} = -\langle L_\gamma V, W\rangle_{L^2},
$$

so that the self-adjointness of the geodesic operator and the symmetry of the index form are the same statement, and the Jacobi fields are the kernel of the index form.

**Proof.** Integrating by parts the first term,

$$
\int_a^b\bigl\langle \tfrac{DV}{dt}, \tfrac{DW}{dt}\bigr\rangle = -\int_a^b\bigl\langle \tfrac{D^2V}{dt^2}, W\bigr\rangle ,
$$

the boundary term being zero because the fields vanish at the endpoints; the curvature term is the metric pairing with $\mathcal R_{\dot\gamma}$, and the symmetry of the index form follows from the symmetry of the curvature. Setting $I(V,W)=0$ for all $W$ gives $L_\gamma V = 0$, so the kernel is the Jacobi fields.

### Morse Index and Nullity

**Theorem.** The **index** of the index form, the maximal dimension of a subspace on which $I$ is negative definite, equals the number of conjugate points of $\gamma(0)$ along $\gamma$ in the interior of the interval, counted with multiplicity; the **nullity**, the dimension of the kernel, equals the dimension of the space of the Jacobi fields vanishing at both endpoints, which is the multiplicity of the endpoint $\gamma(b)$ if it is conjugate. This is the **Morse index theorem**, and the self-adjointness of the geodesic operator is what makes the index finite and the counting meaningful.

**Proof sketch.** The Jacobi fields vanishing at $a$ form an $n$-dimensional space, and the conjugate points are the zeros of the nonvanishing ones; the index is computed by counting the sign changes of the solutions of the Jacobi equation, which is the Sturm oscillation argument applied to the self-adjoint operator; the nullity is the kernel dimension by the previous theorem. The details, including the finiteness of the index and the comparison theorems, are in *The Conjugate Locus and the Injectivity Radius* and in the references.

## Examples

**Example (the flat space).** In $\mathbb R^n$ the curvature vanishes, the geodesic operator is $L_\gamma = \frac{D^2}{dt^2}$ with the ordinary derivative, the Jacobi fields are the affine fields $t\mapsto v + tw$, and there are no conjugate points; the index form is $\int\langle V',W'\rangle \geq 0$, positive definite on the fields vanishing at the ends, of index zero. The self-adjointness is the integration by parts for the second derivative.

**Example (the sphere and the hyperbolic space).** On the round sphere of curvature $+1$ the geodesic operator is $L_\gamma V = V'' + V$ in a parallel frame along a great circle, with the scalar potential $+1$; the Jacobi fields are $\cos t$ and $\sin t$, the first conjugate point is at $t=\pi$, and the index is the number of the conjugate points in the interval. On the hyperbolic space of curvature $-1$ the operator is $V'' - V$, the solutions are $\cosh t$ and $\sinh t$, there is no conjugate point and the index is zero everywhere; the sign of the curvature term is the sign of the potential, and the Sturm comparison between the two cases is the comparison of the Jacobi equation.

**Example (the curvature as the potential).** For a general geodesic the curvature operator in the direction of the geodesic, $\mathcal R_{\dot\gamma}$, is the matrix potential of the vector Sturm–Liouville problem $V''+\mathcal R_{\dot\gamma}V = \lambda V$; it is self-adjoint, so the problem has a real spectrum, and the oscillation of the solutions is governed by the eigenvalues of $\mathcal R_{\dot\gamma}$. This is the sense in which the geodesic operator is the adjoint (that is, the self-adjoint operator) of the geodesic flow.

## Summary

The **geodesic operator** along a geodesic $\gamma$ is the second-order operator $L_\gamma = \frac{D^2}{dt^2} + \mathcal{R}_{\dot\gamma}$, the linearisation of the geodesic flow, with $\mathcal R_{\dot\gamma}(V) = R(V,\dot\gamma)\dot\gamma$ the curvature operator in the direction of the geodesic; its kernel is the space of the **Jacobi fields**, of dimension $2n$, which are the derivatives of the variations of the geodesic by geodesics and the images of the differential of the exponential map. The **Jacobi equation** $L_\gamma V = 0$ is the kernel equation, and the fields $t\dot\gamma$ and the parallel fields are its tangent solutions.

For the $L^2$ pairing with the fields vanishing at the ends of the geodesic, the covariant derivative is **skew-adjoint**, $(\frac{D}{dt})^*=-\frac{D}{dt}$, and the curvature term is **self-adjoint** because the curvature tensor is symmetric; hence the geodesic operator is **self-adjoint**, $L_\gamma^{*}=L_\gamma$, with a real spectrum and orthogonal eigenfields, and it is a symmetric Sturm–Liouville operator whose potential is the curvature. Its quadratic form is the **index form** $I(V,W) = \int(\langle V',W'\rangle-\langle R(V,\dot\gamma)\dot\gamma,W\rangle)$, symmetric and with the Jacobi fields as its kernel; the index of the index form counts the conjugate points with multiplicity and the nullity is the dimension of the Jacobi fields vanishing at the ends, which is the Morse index theorem. The geodesic operator is invariant under the reversal of the geodesic, and its self-adjointness is the operator-layer form of the symmetry of the curvature operator. The flat space, the sphere and the hyperbolic space are the constant-potential examples, with index zero, with conjugate points at the multiples of $\pi$, and with no conjugate point respectively.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_\gamma = \frac{D^2}{dt^2}+\mathcal{R}_{\dot\gamma}$ | Geodesic operator (Jacobi operator) along $\gamma$ |
| $\mathcal{R}_{\dot\gamma}(V) = R(V,\dot\gamma)\dot\gamma$ | Curvature operator in the direction of the geodesic |
| $L_\gamma V = 0$ | Jacobi equation; the kernel is the Jacobi fields |
| $\langle V,W\rangle_{L^2} = \int_a^b\langle V,W\rangle dt$ | $L^2$ pairing of the fields along the geodesic |
| $(\frac{D}{dt})^*=-\frac{D}{dt}$ | The covariant derivative is skew-adjoint |
| $\mathcal R_{\dot\gamma}^{*}=\mathcal R_{\dot\gamma}$ | The curvature term is self-adjoint (symmetric curvature) |
| $L_\gamma^{*}=L_\gamma$ | The geodesic operator is self-adjoint |
| $I(V,W)$ | Index form; the quadratic form of the geodesic operator |
| Index, nullity | Number of conjugate points; dimension of the Jacobi fields vanishing at the ends |

## Further Reading

- Manfredo P. do Carmo, *Riemannian Geometry* (Birkhäuser, 1992), for the Jacobi fields, the index form, the self-adjointness and the Morse index theorem.
- Jürgen Jost, *Riemannian Geometry and Geometric Analysis*, 7th ed. (Springer, 2017), for the Jacobi equation, the Sturm–Liouville theory and the index theorems.
- Shoshichi Kobayashi and Katsumi Nomizu, *Foundations of Differential Geometry, Volume II* (Interscience, 1969), for the Jacobi operator, the curvature and the conjugate points in the variational setting.
- John Milnor, *Morse Theory* (Princeton University Press, 1963), for the index theorem, the conjugate points and the self-adjointness of the second variation.
- Wilhelm Klingenberg, *Riemannian Geometry*, 2nd ed. (de Gruyter, 1995), for the geodesic operator, the conjugate locus and the injectivity radius.
