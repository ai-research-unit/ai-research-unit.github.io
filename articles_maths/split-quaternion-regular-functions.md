
# __Split-Quaternion Regular Functions__

## Introduction

This article studies **regular** (equivalently **monogenic**) split-quaternion-valued functions, that is, functions annihilated by the split-quaternion **Cauchy–Riemann operator**. The split-quaternion algebra $\mathbb{H}_{\mathrm{s}}$ carries an **indefinite** norm of signature $(2,2)$, and this is decisive: the first-order operator has an indefinite principal symbol, the associated second-order operator is an ultrahyperbolic (wave-type) operator rather than a Laplacian, and the algebra has zero divisors whose null cone is the characteristic set on which the Cauchy kernel is singular.

The article owns the regularity theory of the category: the operator and its conjugate, the system of regularity equations, the failure of ellipticity, the examples, the harmonicity that survives as a wave equation, and the failure of the complex analogy where the zero divisors intervene. It relies on *Split-Quaternion Analysis* for the differential operators and the Peirce coordinates, on *Split-Quaternion Analysis* for the subalgebra operators, and on the biquaternion counterpart *Biquaternion Regular Functions* for the structural comparison. No physics is invoked; the object called a "Dirac operator" in older literature is here the **Cauchy–Riemann operator**, and that name is used throughout.

**Conventions.** Coordinates are $\tilde q = q_0 e_0 + q_1 e_1 + q_2 e_2 + q_3 e_3$, with $N(\tilde q) = q_0^2+q_1^2-q_2^2-q_3^2$. For a function $F : \Omega \to \mathbb{H}_{\mathrm{s}}$ on an open set $\Omega$ in a four-dimensional subspace, the partial derivatives are written $\partial_{q_0}, \partial_{q_1}, \partial_{q_2}, \partial_{q_3}$.

## The Cauchy–Riemann Operator and Its Conjugate

**Definition.** The **Cauchy–Riemann operator** (the split-quaternion gradient) and its **conjugate** are

$$
\nabla = e_0 \partial_{q_0} + e_1 \partial_{q_1} + e_2 \partial_{q_2} + e_3 \partial_{q_3}, \qquad
\bar{\nabla} = e_0 \partial_{q_0} - e_1 \partial_{q_1} - e_2 \partial_{q_2} - e_3 \partial_{q_3} .
$$

The pair $(\nabla, \bar{\nabla})$ plays the role of $(\partial_{\bar z}, \partial_z)$ in one complex variable. The units satisfy the Clifford relations $e_\mu e_\nu^{\natural} + e_\nu e_\mu^{\natural} = 2g_{\mu\nu} e_0$ with $g = \operatorname{diag}(1,1,-1,-1)$, so the cross terms cancel and

$$
\nabla \bar{\nabla} = \bar{\nabla} \nabla = \Box := \bigl(\partial_{q_0}^2 + \partial_{q_1}^2 - \partial_{q_2}^2 - \partial_{q_3}^2\bigr) e_0 .
$$

The second-order operator $\Box$ is the **ultrahyperbolic operator** of signature $(2,2)$: a wave operator, not a Laplacian. This single sign difference from the quaternion and biquaternion cases governs the whole of the regularity theory below.

**Proof.** Expand $\nabla\bar{\nabla} = \sum_{\mu,\nu} e_\mu e_\nu^{\natural} \partial_\mu\partial_\nu$. The diagonal coefficients are $e_0e_0^{\natural} = e_0$, $e_1e_1^{\natural} = -e_1^2 = e_0$, $e_2e_2^{\natural} = -e_2^2 = -e_0$, $e_3e_3^{\natural} = -e_3^2 = -e_0$, giving the displayed signs; the off-diagonal coefficients come in symmetric pairs $e_\mu e_\nu^{\natural} + e_\nu e_\mu^{\natural}$, which vanish by the Clifford relations. The same computation with the factors reversed gives $\bar{\nabla}\nabla = \Box$.

## Regularity and the System of Equations

**Definition.** Let $\Omega$ be open in a four-dimensional real subspace, and let $F : \Omega \to \mathbb{H}_{\mathrm{s}}$ be continuously differentiable. Then $F$ is **left-regular**, or **left-monogenic**, if $\nabla F = 0$ on $\Omega$; it is **right-regular** if $F\nabla := \sum_\mu \partial_\mu F\, e_\mu = 0$; and **anti-regular** if $\bar{\nabla}F = 0$. In this category **regular** without qualification means left-regular, and the operator inverted is the first-order operator $\nabla$, not $\Box$.

**Theorem (the regularity system).** Write $F = F_0 + \mathbf{F}$, $\mathbf{F} = F_1 e_1 + F_2 e_2 + F_3 e_3$. Then

$$
\nabla F = \bigl(\partial_{q_0} F_0 - \mathrm{div}_{\mathrm{s}}\,\mathbf{F}\bigr) + \bigl(\partial_{q_0} \mathbf{F} + \operatorname{grad}_{\mathrm{s}} F_0 + \operatorname{rot}_{\mathrm{s}} \mathbf{F}\bigr),
$$

where the **split** divergence, gradient and curl are taken with respect to the indefinite form $N|_V = q_1^2-q_2^2-q_3^2$, using the sign matrix $\operatorname{diag}(1,-1,-1)$; hence $F$ is regular if and only if the four equations

$$
\partial_{q_0} F_0 = \mathrm{div}_{\mathrm{s}}\,\mathbf{F}, \qquad \partial_{q_0} \mathbf{F} + \operatorname{grad}_{\mathrm{s}} F_0 + \operatorname{rot}_{\mathrm{s}} \mathbf{F} = 0
$$

hold. This is the **split-quaternion Cauchy–Riemann system**, four scalar equations for the four coefficients, inheriting the signs of the indefinite form.

**Proof.** Multiply out $\nabla F = \sum_\mu e_\mu \partial_\mu F$ using the multiplication table; the scalar part collects $\partial_{q_0} F_0$ against the signed sum $\partial_{q_1} F_1 - \partial_{q_2} F_2 - \partial_{q_3} F_3$, and the vector part collects the signed gradient and curl.

## The Regularity System Is Not Elliptic

**Theorem.** The principal symbol of $\nabla$ is $s(\xi) = \xi_0 + \xi_1 e_1 + \xi_2 e_2 + \xi_3 e_3$, and

$$
s(\xi)\,s^{\natural}(\xi) = \xi_0^2 + \xi_1^2 - \xi_2^2 - \xi_3^2 = N(\xi) e_0,
$$

which vanishes on the null cone $\mathcal{N}$ and only there. Hence the Cauchy–Riemann system is **not elliptic**: it is of ultrahyperbolic (wave) type, and its characteristic variety is exactly the null cone $\mathcal{N}$, the same set that carries the zero divisors.

**Proof.** The identity $s(\xi)s^{\natural}(\xi) = N(\xi)e_0$ is the Fourier symbol of $\nabla\bar\nabla = \Box$. The symbol vanishes precisely when the quadratic form $N(\xi)$ vanishes, i.e. on the null cone. A first-order system is elliptic exactly when its symbol is invertible off the zero section, which fails here on a three-dimensional cone.

**Corollary.** The elliptic tools of the complex theory are unavailable. There is no maximum principle, no mean value property, and no Liouville theorem for regular functions of the full algebra: the equation $\Box F = 0$ admits the plane-wave solutions $F(\tilde q) = f(\tilde q\cdot \xi)$ for every null vector $\xi$, which are bounded and nonconstant on strips and grow without bound in other directions but obey no elliptic constraint.

## Examples of Regular Functions

**Constants.** Every constant is regular, since $\nabla C = 0$; the constants form a four-real-dimensional space.

**The elliptic subalgebra.** On the plane $\mathbb{C} = \mathbb{R}[e_1]$ with $z = q_0 + q_1 e_1$ ($e_1^2 = -1$), a function independent of $q_2,q_3$ satisfies $\nabla F = 2\partial_{\bar z}F$, so $F$ is regular exactly when it is holomorphic in $z$ in the classical sense. Thus every classical holomorphic function of $z = q_0+q_1 e_1$, extended by constancy in $e_2,e_3$, is regular, and $\mathbb{R}[e_1]$ is the elliptic island of the theory.

**The split-complex planes.** On $\mathbb{D}_2 = \mathbb{R}[e_2]$ with $w = q_0 + q_2 e_2$ ($e_2^2 = +1$), a function independent of $q_1,q_3$ satisfies $\nabla F = (\partial_{q_0} + e_2\partial_{q_2})F$, the **hyperbolic Cauchy–Riemann operator**. Its solutions include the split-complex *conjugates*: the linear function $q_0 - q_2 e_2$ is regular, because $\nabla(q_0 - q_2 e_2) = 1 - e_2^2 = 0$, whereas the linear function $q_0 + q_2 e_2 = w$ is not, since $\nabla w = 1 + e_2^2 = 2$. On the split-complex planes the roles of the variable and its conjugate are exchanged relative to the complex case. The same holds on $\mathbb{D}_3 = \mathbb{R}[e_3]$.

**The identity function is not regular.** On the full algebra, $\nabla \tilde q = \sum_\mu e_\mu e_\mu = e_0^2 + e_1^2 + e_2^2 + e_3^2 = 1 - 1 + 1 + 1 = 2 e_0 \neq 0$. So the identity is not regular, as in the quaternion case.

**The Cauchy kernel and its singularity.** The candidate fundamental solution is

$$
G(\tilde q) = \frac{\tilde{q}^{\natural}}{N(\tilde q)^2},
$$

which satisfies $\nabla G = 0$ away from the null set. But because $\mathbb{H}_{\mathrm{s}}$ has zero divisors, $N(\tilde q) = 0$ on the whole cone $\mathcal{N}$, so $G$ is singular on a **three-dimensional cone**, not merely at the origin. This is the first and deepest failure of the complex analogy.

## Harmonicity and the Factorization of the Ultrahyperbolic Operator

**Theorem.** Every regular function is **harmonic** for the ultrahyperbolic operator: if $\nabla F = 0$ then $\Box F = \bar{\nabla}(\nabla F) = 0$, i.e.

$$
\bigl(\partial_{q_0}^2 + \partial_{q_1}^2 - \partial_{q_2}^2 - \partial_{q_3}^2\bigr) F = 0 .
$$

Right-regular functions are likewise harmonic, and the factorization $\Box = \nabla\bar{\nabla} = \bar{\nabla}\nabla$ is the analogue of $\partial_z\partial_{\bar z} = \tfrac14 \Delta$ in one complex variable.

**Proof.** The vanishing $\Box F = 0$ is immediate from $\Box = \bar{\nabla}\nabla$ applied to $\nabla F = 0$; the right-regular case is the same identity with the factors on the other side.

**Corollary.** The converse fails: $F(\tilde q) = q_0$ is harmonic, since $\Box q_0 = 0$, but $\nabla q_0 = e_0 \neq 0$, so $q_0$ is not regular. Thus the regular functions form a proper subclass of the $\Box$-harmonic functions, exactly as holomorphic functions are a proper subclass of harmonic functions in one complex variable.

## The Role of the Zero Divisors and the Failure of the Analogy

The complex analogy fails precisely where the zero divisors intervene, and this is the content of the present article.

**Theorem.** On a domain meeting the null cone, no regular function that is a genuine inverse of the coordinate behaves as the complex $1/z$ does. The Cauchy kernel $G(\tilde q) = \tilde{q}^{\natural}/N(\tilde q)^2$ is singular on all of $\mathcal{N}$, and the singularity is a three-dimensional cone; there is no way to isolate a punctured neighbourhood by a sphere, because the null cone passes through every neighbourhood.

**Proof.** The singular set of $G$ is $\{N(\tilde q) = 0\}$, which is $\mathcal{N}$, of dimension $3$; a frame around a point of $\mathcal{N}$ is not a compact separating surface but is pierced by the cone.

**The Cauchy integral formula fails.** Even when a boundary integral can be written down, the kernel is singular on the part of the null cone inside the domain, so the classical Cauchy integral formula has no direct analogue: there is no simply connected domain whose boundary avoids the characteristic set while containing the singularities of the kernel.

**What survives.** On the elliptic subalgebra $\mathbb{C} = \mathbb{R}[e_1]$ the theory is the classical theory of one complex variable and the Cauchy formula holds verbatim; on each split-complex plane and on each definite bidimensional subspace the theory is a two-dimensional hyperbolic (or elliptic) Cauchy–Riemann theory with its own integral formula along characteristics. Thus regularity is a *local-in-direction* phenomenon whose global integral theory exists only on the subspaces that avoid the indefinite directions. This is developed in *Split-Quaternion Analysis*.

## Relation to the Biquaternion Regular Functions and Clifford Analysis

The biquaternion article *Biquaternion Regular Functions* develops regularity on $\mathbb{B}$ with the **elliptic** operator whose symbol satisfies $s(\xi)s^{\natural}(\xi) = |\xi|^2 e_0$, giving the Clifford analysis of $\mathbb{R}^4$: a maximum principle, a mean value property, a Cauchy integral formula and a fundamental solution $G = \bar{Q}/\|Q\|_E^4$ singular only at the origin. On the biquaternion indefinite subspaces $\mathbb{M}_\pm$ the operator becomes a wave operator and the elliptic tools disappear there.

The split-quaternion case is the **fully indefinite** one: the form is indefinite, so no subspace through the origin of dimension greater than two is definite and the elliptic theory lives only on definite planes; the symbol vanishes on the whole null cone, the second-order operator is ultrahyperbolic, and the Cauchy kernel is singular on a cone of dimension three. The definiteness that the biquaternion theory retains on its quaternion half is precisely what the split-quaternion algebra lacks. In the language of Clifford analysis, the pair $(\nabla, \bar{\nabla})$ here are the Cauchy–Riemann operators of $\mathrm{Cl}_{2,2}$, and the regularity theory is an indefinite-signature-$(2,2)$ Clifford analysis with a null characteristic variety. Nothing biquaternion-specific — the central imaginary unit $i$, the definite quaternion half, the Euclidean kernel — is imported; the two theories are placed side by side only for comparison.

## Summary

The split-quaternion Cauchy–Riemann operator $\nabla = \sum_\mu e_\mu\partial_\mu$ and its conjugate $\bar{\nabla}$ satisfy $\nabla\bar{\nabla} = \bar{\nabla}\nabla = \Box$, the ultrahyperbolic operator $\partial_{q_0}^2+\partial_{q_1}^2-\partial_{q_2}^2-\partial_{q_3}^2$ of signature $(2,2)$. A function is regular when $\nabla F = 0$, equivalently when it satisfies the split-quaternion Cauchy–Riemann system of four scalar equations with the signs of the indefinite form. The system is **not elliptic**: its symbol $s(\xi)$ obeys $s(\xi)s^{\natural}(\xi) = N(\xi)e_0$ and vanishes exactly on the null cone, which is the characteristic variety and the zero-divisor set. Every regular function is $\Box$-harmonic, but not conversely. The examples are the constants; the classical holomorphic functions of the elliptic variable $z = q_0+q_1 e_1$; the split-complex conjugates on the hyperbolic planes $\mathbb{D}_2, \mathbb{D}_3$; and the Cauchy kernel $\tilde{q}^{\natural}/N(\tilde q)^2$, singular on the whole null cone. The complex analogy holds on the elliptic subalgebra and fails wherever the null cone intervenes: no maximum principle, no mean value property, no Liouville theorem, and no global Cauchy integral formula on the full algebra. The biquaternion theory, by contrast, retains an elliptic half, and the failure here is exactly the absence of an elliptic subspace of dimension greater than two: the form is indefinite, and the only definite subspaces are the planes.

## Summary of Notation

| Symbol | Meaning | Article |
|---|---|---|
| $\mathbb{H}_{\mathrm{s}}$ | the split-quaternion algebra | *Split-Quaternion Algebra* |
| $\nabla = \sum_\mu e_\mu\partial_\mu$ | the Cauchy–Riemann operator | this article |
| $\bar{\nabla} = e_0\partial_{q_0} - e_1\partial_{q_1} - e_2\partial_{q_2} - e_3\partial_{q_3}$ | its conjugate | this article |
| $\Box = \nabla\bar{\nabla} = \bar{\nabla}\nabla$ | the ultrahyperbolic operator, signature $(2,2)$ | this article |
| $\nabla F = 0$ | left-regular (monogenic); $F\nabla=0$ right-regular | this article |
| $g = \operatorname{diag}(1,1,-1,-1)$ | the Clifford sign matrix | this article |
| $\mathbb{C} = \mathbb{R}[e_1]$ | the elliptic subalgebra, $z = q_0+q_1 e_1$ | *Split-Quaternion Elementary Functions* |
| $\mathbb{D}_2, \mathbb{D}_3$ | the split-complex planes, hyperbolic Cauchy–Riemann operators | *Split-Quaternion Split-Complex Subspaces* |
| $G(\tilde q) = \tilde{q}^{\natural}/N(\tilde q)^2$ | the Cauchy kernel, singular on $\mathcal{N}$ | this article |
| $\mathcal{N} = \{N=0\}$ | the null cone / characteristic set | *Split-Quaternion Zero Divisors* |
| $N(\tilde q) = q_0^2+q_1^2-q_2^2-q_3^2$ | the split-quaternion norm, signature $(2,2)$ | *Split-Quaternion Norm and Invertibility* |

## Further Reading

- F. Brackx, R. Delanghe and F. Sommen, *Clifford Analysis*, Research Notes in Mathematics 76 (Pitman, 1982), for monogenic functions, the Cauchy–Riemann operator of a Clifford algebra and the Cauchy kernel.
- R. Delanghe, F. Sommen and V. Souček, *Clifford Algebra and Spinor-Valued Functions* (Kluwer, 1992), for regularity over Clifford algebras of general signature.
- John E. Gilbert and Margaret A. M. Murray, *Clifford Algebras and Dirac Operators in Harmonic Analysis* (Cambridge University Press, 1991), for the factorization of Laplacians and wave operators by first-order operators.
- R. S. Ward and Raymond O. Wells, *Twistor Geometry and Field Theory* (Cambridge University Press, 1990), for the Cauchy–Riemann operators of signature $(2,2)$ and the ultrahyperbolic equation.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I*, 2nd ed. (Springer, 1990), for ellipticity, the principal symbol and the characteristic variety of a first-order system.
