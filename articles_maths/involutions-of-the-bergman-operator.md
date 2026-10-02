
# __Involutions of the Bergman Operator__

## Introduction

Let $\Omega \subseteq \mathbb{C}^n$ be a bounded domain, $A^2(\Omega)$ the **Bergman space** of the holomorphic functions that are square-integrable, and
$$
B : L^2(\Omega) \longrightarrow A^2(\Omega), \qquad Bg(z) = \int_{\Omega} K(z,w)\,g(w)\,dV(w),
$$
the **Bergman operator**, the orthogonal projection onto the Bergman space; its kernel $K(z,w)$ is the **Bergman kernel**. The operator carries an involution of its own, the **conjugate symmetry** of the kernel,
$$
K(z, w) = \overline{K(w, z)},
$$
which is the exchange of the two variables followed by conjugation; the symmetry is exactly the statement that $B$ is self-adjoint, and together with $B^2 = B$ it says that $B$ is an orthogonal projection, the model of the Hermitian projections of *The Adjoint of a Hermitian Operator*. On a domain stable under the conjugation of the coordinates, $z\mapsto\bar z$, there is a second involution, the conjugate-linear map
$$
\sigma f(z) = \overline{f(\bar z)},
$$
an antiunitary involution of the Bergman space that commutes with $B$ and whose fixed space is the **real Bergman space** of the functions with real Taylor coefficients; it is the Bergman-space form of the real structure of *The Involution on a Complex Vector Space*, and the two involutions — the conjugate symmetry of the kernel and the conjugation of the space — are the operator and the pointwise faces of the same Hermitian geometry.

The article has three sections: the Bergman operator, its idempotence and its self-adjointness; the conjugate symmetry of the kernel; and the conjugate-linear involution of the Bergman space. The Bergman kernel, the projection and the transformation law are *The Bergman Operator* and *Reproducing Kernel Hilbert Spaces*, earlier in this Part; the adjoint, the Hermitian operators and the positivity are *The Adjoint of a Hermitian Operator*, the preceding article of this group; the Hermitian forms and the unitary group are *Hermitian Geometry and the Unitary Group*; the real structure and the conjugation are *The Involution on a Complex Vector Space* and *Real Structures on a Complex Manifold*; the bounded symmetric domain and its Bergman metric are *Hermitian Symmetric Spaces and the Bergman Metric*. None of that is re-derived.

Throughout, $\Omega$ is a bounded domain in $\mathbb{C}^n$, $A^2(\Omega)$ is its Bergman space with the $L^2$ inner product $\langle f,g\rangle = \int_\Omega f\bar g\,dV$, $K(z,w)$ is the Bergman kernel, $B$ is the Bergman projection, and $z\mapsto\bar z$ is the coordinate conjugation whenever $\Omega$ is stable under it.

## The Bergman Operator, Its Idempotence and Its Self-Adjointness

**Proposition (the Bergman operator is an orthogonal projection).** The Bergman operator $B$ is idempotent and self-adjoint for the $L^2$ inner product,
$$
B^2 = B, \qquad B^{*} = B,
$$
so it is the orthogonal projection of $L^2(\Omega)$ onto $A^2(\Omega)$; equivalently $\operatorname{im}B = A^2(\Omega)$ and $\ker B$ is the orthogonal complement of the Bergman space.

**Proof.** The reproducing property $f(z) = \langle f, K(z,\cdot)\rangle$ for $f \in A^2$ gives $\operatorname{im}B = A^2$ and $Bf = f$ on $A^2$, hence $B^2 = B$; the self-adjointness is the equivalence of the conjugate symmetry of the kernel with $B^{*} = B$, proved in the next proposition. An idempotent self-adjoint operator is the orthogonal projection onto its range, by the spectral theorem. The reproducing property and the projection are *The Bergman Operator* and *Reproducing Kernel Hilbert Spaces*.

**Proposition (conjugate symmetry is self-adjointness).** The kernel satisfies $K(z,w) = \overline{K(w,z)}$, and this identity is equivalent to the self-adjointness of $B$: for $f, g \in L^2$,
$$
\langle Bf, g\rangle = \int\!\!\int K(z,w)f(w)\overline{g(z)}\,dV(w)\,dV(z) = \overline{\langle Bg, f\rangle} = \langle f, Bg\rangle .
$$

**Proof.** Substituting the definition of $B$, exchanging the order of integration by Fubini, and using the conjugate symmetry $K(z,w) = \overline{K(w,z)}$ gives $\langle Bf,g\rangle = \int\!\!\int \overline{K(w,z)}f(w)\overline{g(z)} = \overline{\int\!\!\int K(w,z)g(z)\overline{f(w)}} = \overline{\langle Bg,f\rangle} = \langle f,Bg\rangle$; conversely, if $B$ is self-adjoint the two iterated integrals differ by conjugation for all $f,g$ and the kernel is conjugate-symmetric. The kernel and the Fubini exchange are *The Bergman Operator* and *Reproducing Kernel Hilbert Spaces*.

**Corollary (the growth of the kernel and the diagonal).** The diagonal $K(z,z) > 0$ and is the square of the norm of the evaluation functional at $z$; on the diagonal the conjugate symmetry is the reality $K(z,z) = \overline{K(z,z)}$, and the Bergman metric $g^{\mathrm B}_{i\bar j} = \partial_i\bar\partial_j\log K(z,z)$ is built from the diagonal, *Hermitian Symmetric Spaces and the Bergman Metric*.

**Proof.** For $f\in A^2$ with $f(z)\neq0$ one has $|f(z)|^2 = |\langle f,K(z,\cdot)\rangle|^2 \le \|f\|^2K(z,z)$ by Cauchy–Schwarz, and choosing $f = K(z,\cdot)$ gives equality; hence $K(z,z) = \|K(z,\cdot)\|^2>0$ except at a point supporting no holomorphic function. The diagonal value of a conjugate-symmetric kernel is real. The Bergman metric is the $\partial\bar\partial\log$ of the diagonal, *Hermitian Symmetric Spaces and the Bergman Metric*.

## The Conjugate-Linear Involution of the Bergman Space

**Definition.** Suppose $\Omega$ is stable under the conjugation $z\mapsto\bar z$. The **conjugation** of the Bergman space is the map
$$
\sigma f(z) = \overline{f(\bar z)} .
$$

**Proposition (the conjugation is an antiunitary involution).** $\sigma$ is a conjugate-linear involution of $A^2(\Omega)$ and an isometry,
$$
\sigma^2 = \mathrm{id}, \qquad \sigma(\lambda f) = \bar\lambda\,\sigma f, \qquad \langle \sigma f, \sigma g\rangle = \langle g, f\rangle ,
$$
and it commutes with the Bergman operator, $\sigma B = B\sigma$; its fixed space is the **real Bergman space** of the functions with real Taylor coefficients at the origin.

**Proof.** The map is conjugate-linear by the conjugation of the scalar; $\sigma^2 f(z) = \overline{\overline{f(\bar{\bar z})}} = f(z)$; the isometry is the change of variables $z\mapsto\bar z$, which preserves $dV$; and $\sigma(f\bar g) = (\sigma f)\overline{(\sigma g)}$, so the inner product is conjugated. The commutation with $B$ follows from $K(\bar z,\bar w) = \overline{K(z,w)}$ for a domain stable under conjugation, which is the conjugate symmetry read under the involution of the variables. A function with real Taylor coefficients satisfies $\overline{f(\bar z)} = f(z)$, and conversely. This is *Real Structures on a Complex Manifold* and *The Involution on a Complex Vector Space*.

**Proposition (the two involutions are one).** The conjugate symmetry of the kernel, the self-adjointness of $B$, and the commutation of the Bergman projection with the conjugation $\sigma$ are the three expressions of the same Hermitian geometry of the domain; on the disc and the bounded symmetric domains they are the reflection of the domain in its real locus, and the real Bergman space is the descending of the Bergman theory to the real form.

**Proof.** The self-adjointness is the conjugate symmetry; the commutation of $B$ with $\sigma$ is the invariance $K(\bar z,\bar w) = \overline{K(z,w)}$ of the kernel under conjugation, which follows from the characterisation of the kernel as the extremal function of the evaluation; the real Bergman space is the fixed space, and on the disc $\sigma$ is $f(z)\mapsto\overline{f(\bar z)}$, whose fixed functions are exactly the real-analytic ones. This is the descent of *Real Structures on a Complex Manifold*.

**Example (the disc and the polydisc).** On the unit disc the Bergman kernel is $K(z,w) = \pi^{-1}(1-z\bar w)^{-2}$ (with the normalisation fixed by *The Bergman Operator*), which is conjugate-symmetric, $K(z,w) = \overline{K(w,z)}$; the conjugation $\sigma f(z) = \overline{f(\bar z)}$ has the real Bergman space of the functions with real Taylor coefficients, and the Bergman projection is self-adjoint and commutes with $\sigma$. On the polydisc the kernel is the product of the one-variable kernels and every statement is componentwise; on a bounded symmetric domain the conjugation is the geodesic symmetry in the origin. This is *Hermitian Symmetric Spaces and the Bergman Metric*.

## Summary

For a bounded domain $\Omega$ the Bergman operator $B$, the orthogonal projection of $L^2$ onto the Bergman space with the reproducing kernel $K(z,w)$, is idempotent and self-adjoint, $B^2 = B = B^{*}$, and its self-adjointness is exactly the conjugate symmetry $K(z,w) = \overline{K(w,z)}$ of the kernel; on the diagonal $K(z,z) = \|K(z,\cdot)\|^2 > 0$ is real and generates the Bergman metric. When the domain is stable under the coordinate conjugation there is the conjugate-linear involution $\sigma f(z) = \overline{f(\bar z)}$, an antiunitary involution commuting with $B$, whose fixed space is the real Bergman space; the conjugate symmetry of the kernel, the self-adjointness of the projection and the commutation with $\sigma$ are the three faces of the same Hermitian geometry, and on the disc and the bounded symmetric domains the conjugation is the real structure of the domain. The kernel and the projection are *The Bergman Operator* and *Reproducing Kernel Hilbert Spaces*; the adjoint and the positivity are *The Adjoint of a Hermitian Operator*; the real structure is *Real Structures on a Complex Manifold*; the symmetric domain is *Hermitian Symmetric Spaces and the Bergman Metric*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A^2(\Omega)$ | the Bergman space |
| $K(z,w)$ | the Bergman kernel, conjugate-symmetric |
| $B$, $B^2=B=B^{*}$ | the Bergman projection |
| $K(z,w)=\overline{K(w,z)}$ | conjugate symmetry, equivalent to $B^{*}=B$ |
| $\sigma f(z)=\overline{f(\bar z)}$ | the conjugation of the Bergman space |
| $A^2(\Omega)^{\sigma}$ | the real Bergman space |

## Further Reading

- Steven R. Bell, *The Cauchy Transform, Potential Theory and Conformal Mapping* (CRC Press, second edition, 2016), for the Bergman projection, its self-adjointness and its kernel.
- Steven G. Krantz, *Function Theory of Several Complex Variables* (American Mathematical Society, second edition, 2001), for the Bergman kernel, the conjugate symmetry and the real Bergman space.
- Robert C. Gunning and Hugo Rossi, *Analytic Functions of Several Complex Variables* (Prentice-Hall, 1965), for the Bergman projection and its behaviour under conjugation.
- Elias M. Stein and Rami Shakarchi, *Fourier Analysis* (Princeton University Press, 2003), for the orthogonal projections, the self-adjointness and the change of variables.
