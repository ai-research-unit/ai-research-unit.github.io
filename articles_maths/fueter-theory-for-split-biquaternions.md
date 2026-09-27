
# __Fueter Theory for Split-Biquaternions__

## Introduction

This article develops Fueter theory in the split biquaternion setting: the Fueter operator, the functions it defines, the construction that produces them from holomorphic functions of one complex variable, and the relation to the biquaternion and split quaternion theories. It follows *Split-Biquaternion Analysis* and *Split-Biquaternion Regular Functions*, where the Cauchy–Riemann operator $\tilde{\nabla}$ and its conjugate $\bar{\tilde{\nabla}}$ were constructed, and it uses the algebra and the zero divisors of *Split-Biquaternion Algebra* and *Split-Biquaternion Zero Divisors*.

The treatment is purely mathematical, and no theorem is asserted beyond its hypotheses. Throughout the quaternion basis is $e_0 = 1, e_1, e_2, e_3$ with $e_1^2 = e_2^2 = e_3^2 = -e_0$, the central split complex unit is $j$ with $j^2 = +e_0$, and a split biquaternion is $\tilde{Q} = \sum_{\mu=0}^{3} Q_\mu e_\mu$ with $Q_\mu = q_\mu + jq'_\mu \in \mathbb{D}$. On the quaternion subspace $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ the coordinates are real, $\tilde{Q} = \sum_\mu q_\mu e_\mu$, with $\mathbf{q} = q_1e_1+q_2e_2+q_3e_3$, $\rho = \|\mathbf{q}\|_E$, $\hat{\mathbf{q}} = \mathbf{q}/\rho$, and $\partial_\mu = \partial/\partial q_\mu$.

## The Fueter Operator

### Definition and Conjugate

On the quaternion subspace the **Fueter operator**, also called the **Cauchy–Riemann–Fueter operator**, is the split-biquaternion-valued first-order operator

$$
\tilde{\nabla} = \sum_{\mu=0}^{3} e_\mu \partial_\mu = \partial_0 + \mathbf{D} , \qquad \mathbf{D} = e_1\partial_1 + e_2\partial_2 + e_3\partial_3 ,
$$

acting on the left. Its **conjugate** is obtained by negating the vector part, $\bar{\tilde{\nabla}} = \partial_0 - \mathbf{D}$. This is the split biquaternion case of the Cauchy–Riemann operator; the older name for it in the physics literature is not used here.

### Factorization of the Laplacian

**Proposition.** On the quaternion subspace, $\tilde{\nabla}\bar{\tilde{\nabla}} = \bar{\tilde{\nabla}}\tilde{\nabla} = \Delta_4 e_0$, where $\Delta_4 = \sum_{\mu=0}^{3}\partial_\mu^2$.

**Proof.** Expand $\tilde{\nabla}\bar{\tilde{\nabla}} = \sum_{\mu,\nu} e_\mu\bar{e}_\nu\partial_\mu\partial_\nu$ with $\bar{e}_0 = e_0$ and $\bar{e}_k = -e_k$. The diagonal term is $\sum_\mu e_\mu\bar{e}_\mu\partial_\mu^2 = \Delta_4 e_0$, since $e_k\bar{e}_k = -e_k^2 = e_0$; the off-diagonal coefficient $e_\mu\bar{e}_\nu + e_\nu\bar{e}_\mu$ vanishes by anticommutativity of the units. The same argument gives $\bar{\tilde{\nabla}}\tilde{\nabla}$. $\square$

### Relation to the Cauchy–Riemann Operator

The factorization makes $\tilde{\nabla}$ a square root of the Laplacian: with $\mathbf{D}^2 = -\Delta_3 e_0$ one has $(\partial_0+\mathbf{D})(\partial_0-\mathbf{D}) = \partial_0^2+\Delta_3 = \Delta_4$. On a slice $\mathbb{C}_I$ (below), the part of $\tilde{\nabla}$ differentiating along the slice is the complex Cauchy–Riemann operator $\partial_{q_0} + I\partial_\rho$, so $\tilde{\nabla}\tilde{F} = 0$ is the quaternionic Cauchy–Riemann equation. In Clifford language $\mathbb{H}$ is the even subalgebra of $\mathrm{Cl}_{0,3}$, and Fueter-regular functions are its **monogenic** functions.

## Fueter-Regular Functions

### Left and Right Regularity

**Definition.** Let $\tilde{F} : \Omega \to \mathbb{H}_{\mathbb{D}}$ be differentiable on an open set $\Omega \subseteq \mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$. Then $\tilde{F}$ is **left-regular** if $\tilde{\nabla}\tilde{F} = 0$, and **right-regular** if $\tilde{F}\tilde{\nabla} = \sum_\mu \partial_\mu\tilde{F}\,e_\mu = 0$.

The two conditions differ because the algebra is noncommutative; left-regular functions are stable under right multiplication by quaternion constants and right-regular functions under left multiplication, neither being stable on the other side in general. On the full algebra the operator is the idempotent-split pair of quaternion operators, so a function is regular if and only if both of its idempotent components are regular:

$$
\tilde{\nabla}\tilde{F} = \left(\tilde{\nabla}\tilde{F}_+\right)\tilde\Pi_+ + \left(\tilde{\nabla}\tilde{F}_-\right)\tilde\Pi_- = 0 \iff \tilde{\nabla}\tilde{F}_+ = \tilde{\nabla}\tilde{F}_- = 0 .
$$

### The Componentwise System

Writing $\tilde{F} = \sum_\mu F_\mu e_\mu$ and $\mathbf{F} = F_1e_1+F_2e_2+F_3e_3$, the scalar-vector decomposition gives

$$
\tilde{\nabla}\tilde{F} = \left(\partial_0F_0 - \mathrm{div}\,\mathbf{F}\right) + \left(\partial_0\mathbf{F} + \mathrm{grad}\,F_0 + \mathrm{rot}\,\mathbf{F}\right) ,
$$

with $\mathrm{div}\,\mathbf{F} = \sum_k\partial_kF_k$, $\mathrm{grad}\,F_0 = \sum_k(\partial_kF_0)e_k$ and $\mathrm{rot}\,\mathbf{F} = \sum_{j,k,l}\epsilon_{jkl}(\partial_jF_k)e_l$. Hence left-regularity is

$$
\partial_0F_0 = \mathrm{div}\,\mathbf{F} , \qquad \partial_0\mathbf{F} = -\mathrm{grad}\,F_0 - \mathrm{rot}\,\mathbf{F} ,
$$

the quaternionic Cauchy–Riemann–Fueter system, one algebra equation equivalent to the corresponding system for each component. This is the **same system** as in the quaternion and biquaternion cases, because it rests only on the Clifford relation among $e_0,e_1,e_2,e_3$.

## Harmonicity and the Mean Value Property

**Proposition.** Every left- or right-regular function is harmonic for the four-dimensional Laplacian: $\Delta_4\tilde{F} = 0$ componentwise.

**Proof.** If $\tilde{\nabla}\tilde{F} = 0$, then $\Delta_4\tilde{F} = \bar{\tilde{\nabla}}(\tilde{\nabla}\tilde{F}) = 0$; if $\tilde{F}\tilde{\nabla} = 0$, then $\Delta_4\tilde{F} = (\tilde{F}\tilde{\nabla})\bar{\tilde{\nabla}} = 0$ with the operators acting on the right. $\square$

Consequently every regular function is real-analytic and satisfies the maximum principle, Liouville's theorem, the identity theorem and the Cauchy estimates on the quaternion subspace, where the system is elliptic. Since each component is harmonic, the **mean value property** holds: for $\tilde{F}$ regular near the closed ball $\bar{B}(\tilde{Q}_0,r)$,

$$
\tilde{F}(\tilde{Q}_0) = \frac{1}{|B(\tilde{Q}_0,r)|}\int_{B(\tilde{Q}_0,r)}\tilde{F}\,dV = \frac{1}{|\partial B(\tilde{Q}_0,r)|}\int_{\partial B(\tilde{Q}_0,r)}\tilde{F}\,dS ,
$$

with the ordinary measures on $\mathbb{R}^4$, the property following from the factorization. On the indefinite subspaces the same operator factors a wave operator, and the elliptic consequences are lost.

## The Fueter Construction

### The Axial Extension of a Holomorphic Function

Let $f_0$ be holomorphic on the disc $D(0,R) \subseteq \mathbb{C}$, written $f_0(z) = u(x,y) + iv(x,y)$ with $z = x+iy$ and $u,v$ real-valued, so that $u,v$ are harmonic and satisfy $u_x = v_y$, $u_y = -v_x$. The **axial extension** of $f_0$ is

$$
\tilde{f}_0(\tilde{Q}) = u(q_0,\rho) + \hat{\mathbf{q}}\,v(q_0,\rho) ,
$$

defined for $\rho > 0$ by replacing $x$ by $q_0$, $y$ by $\rho$, and the complex imaginary unit $i$ by $\hat{\mathbf{q}}$; the replacement is legitimate because $\hat{\mathbf{q}}^2 = -1$. When $f_0$ has real Taylor coefficients, $v(q_0,0) = 0$, the extension is continuous at $\rho = 0$ with value $f_0(q_0)$, and $\tilde{f}_0(\tilde{Q}) = \sum_{n\ge0}a_n\tilde{Q}^n$ on $B(0,R)$. Complex coefficients are handled by $\mathbb{C}$-linearity.

### Fueter's Theorem

**Theorem (Fueter's construction).** Let $f_0$ be holomorphic on $D(0,R)$ with axial extension $\tilde{f}_0$. Then

$$
\tilde{F}(\tilde{Q}) = \Delta_4\tilde{f}_0(\tilde{Q}) = \frac{2\partial_\rho u(q_0,\rho)}{\rho} + \hat{\mathbf{q}}\left(\frac{2\partial_\rho v(q_0,\rho)}{\rho} - \frac{2v(q_0,\rho)}{\rho^2}\right)
$$

is defined and real-analytic on $B(0,R)$, by continuity at $\rho = 0$, and is both left- and right-Fueter-regular there.

**Proof.** For $g = A(q_0,\rho) + \hat{\mathbf{q}}B(q_0,\rho)$ one has $\tilde{\nabla}g = g\tilde{\nabla} = (\partial_0A - \partial_\rho B - 2B/\rho) + \hat{\mathbf{q}}(\partial_0B + \partial_\rho A)$, using $\hat{\mathbf{q}}^2 = -1$ and $\sum_{j,k}(\partial_{q_k}\hat{q}_j)e_ke_j = (-3-\hat{\mathbf{q}}^2)/\rho = -2/\rho$; so $g$ is left-regular exactly when it is right-regular, and this holds when $\partial_0A = \partial_\rho B + 2B/\rho$ and $\partial_0B = -\partial_\rho A$. Applying $\Delta_4$ to the axial extension and using the radial Laplacian identity gives the two scalar coefficients $2u_\rho/\rho$ and $2(\rho v_\rho - v)/\rho^2$, whose Cauchy–Riemann relations are exactly the two conditions. $\square$

### The Kernel and Injectivity

**Proposition.** The map $\tau(f_0) = \Delta_4\tilde{f}_0$ vanishes if and only if $f_0$ is affine, $f_0(z) = az+b$ with $a,b \in \mathbb{C}$.

**Proof.** $\tau(f_0) = 0$ forces $u_\rho = 0$ and $\rho v_\rho = v$, so $u = u(q_0)$ and $v = c(q_0)\rho$; then $c' = 0$ and $u = cq_0+d$ with $c,d \in \mathbb{R}$, and complex linearity gives all affine functions; conversely $\Delta_4$ annihilates affine functions. $\square$

So $\tau$ is injective exactly on the holomorphic functions whose Taylor coefficients vanish to order two.

## The Axial and Slice Approach

### Imaginary Units and Slices

An imaginary unit is an element $I$ with $I^2 = -1$. On the quaternion subspace the imaginary units form the two-sphere $S^2$ of unit pure imaginary quaternions, and every $\tilde{Q}$ with $\mathbf{q} \neq 0$ is uniquely $\tilde{Q} = q_0 + I\rho$ with $I \in S^2$ and $\rho > 0$; the **slice** $\mathbb{C}_I = \mathbb{R} + I\mathbb{R}$ is a copy of the complex plane, and two slices meet only in $\mathbb{R}$ unless $I = \pm J$.

On the full algebra the roots of $-1$ are, by *Split-Biquaternion Roots of Minus One*, the family of pairs $(\hat{u}_+,\hat{u}_-)$ of imaginary units in the two idempotent components, a manifold $S^2 \times S^2$ of dimension four. The quaternion subspace carries the diagonal two-sphere of those roots, the Hermitian subspace $\mathbb{M}_+$ carries the anti-diagonal two-sphere, and the remaining roots lie on neither. The set of roots is therefore no longer a sphere, and there is no single imaginary sphere on which to base the theory: the axial construction must select one root, hence one slice, at a time, and this is the same obstruction as in the biquaternion case, only with a different root manifold.

### Axially Symmetric Functions and the Axial Coefficients

A function is **axially symmetric** if $\tilde{F}(q_0 + \hat{\mathbf{q}}\rho)$ depends on the direction $\hat{\mathbf{q}}$ only through $\hat{\mathbf{q}}$. Such a function has the axial representation $\tilde{F}(\tilde{Q}) = A(q_0,\rho) + \hat{\mathbf{q}}B(q_0,\rho)$ over the basis $\{1,\hat{\mathbf{q}}\}$ of the slice, with **axial coefficients** $A, B$. For such a function the left- and right-regularity conditions coincide and reduce to

$$
\partial_0A = \partial_\rho B + \frac{2B}{\rho} , \qquad \partial_0B = -\partial_\rho A ;
$$

eliminating $B$ gives $\Delta_4A = 0$, so the scalar axial coefficient is harmonic, while $\Delta_4B = 2B/\rho^2$. On the full algebra, where regularity is the pair of quaternionic regularities, an axially symmetric function is regular if and only if each idempotent component is, so the axial coefficients carry a pair of systems, one per half.

### The Fueter–Sce Theorem and Its Hypotheses

**Theorem (Fueter–Sce).** Let $n \geq 1$ be odd, let $\mathrm{Cl}_{0,n}$ have generators $e_1,\dots,e_n$, and let $f_0$ be holomorphic on a disc, with axial extension $\tilde{f}_0$ to $\mathbb{R}^{n+1}$. Then $\tilde{F} = \Delta^{(n-1)/2}\tilde{f}_0$ is monogenic, annihilated on the left and on the right by the Cauchy–Riemann operator on the ball where the extension is defined. For $n = 3$ the exponent is $1$, recovering Fueter's construction.

Three hypotheses are needed and none can be dropped: $f_0$ must be **holomorphic** on the disc, so its Taylor series converges there; the construction has the **affine kernel** $az+b$, so injectivity requires the Taylor coefficients to vanish to order two; and the **parity** $(n-1)/2$ must be a non-negative integer, so $n$ must be odd.

## Power Series Representations

A series with split biquaternion coefficients placed on the right, $f(\tilde{Q}) = \sum_{n\ge0}\tilde{Q}^na_n$, converges absolutely on the set where $\limsup_n\left(\|\tilde{Q}^n\|_E\,\|a_n\|_E\right)^{1/n} < 1$; in particular it converges for $\tilde{Q}$ in the quaternion subspace with $\|\tilde{Q}\|_E < R$, where $R^{-1} = \limsup_n\|a_n\|_E^{1/n}$, because on the quaternion subspace the Euclidean norm is multiplicative and $\|\tilde{Q}^n\|_E = \|\tilde{Q}\|_E^n$. Its sum is **slice-regular**, holomorphic on each slice; slice-regular functions form a different class from the Fueter-regular ones. For example $\tilde{Q}\mapsto\tilde{Q}$ is slice-regular, but

$$
\tilde{\nabla}\tilde{Q} = \sum_{\mu=0}^{3}e_\mu e_\mu = e_0 - e_1^2 - e_2^2 - e_3^2 = -2e_0 \neq 0 .
$$

The Fueter construction is precisely the operation converting slice-regular, or holomorphic, data into Fueter-regular functions.

For real Taylor coefficients, term-by-term application of $\Delta_4$ gives the induced series $\tau(f_0) = \sum_{n\ge0}a_n\Delta_4(\tilde{Q}^n)$, beginning at $n = 2$ and converging normally on $B(0,R)$ because $\Delta_4(\tilde{Q}^n)$ is homogeneous of degree $n-2$ with at most polynomial growth in $n$. In general, with $\mathcal{P}_k$ the algebra-valued homogeneous polynomials of degree $k$ and $\mathcal{M}_k = \{P\in\mathcal{P}_k : \tilde{\nabla}P = 0\}$ the monogenic ones, the Fischer decomposition $\mathcal{P}_k = \bigoplus_{j=0}^{k}\tilde{Q}^j\mathcal{M}_{k-j}$ gives every Fueter-regular function on the ball a normally convergent expansion into monogenic homogeneous pieces, the analogue of the Taylor series of complex analysis.

## The Split Biquaternionic Case

On the quaternion subspace the theory is the classical one with split biquaternion coefficients, because the subspace is a division algebra: $N(\tilde{Q}) = \sum_\mu q_\mu^2$ is positive definite, so every nonzero element is invertible and the fundamental solution $\tilde{G} = \bar{\tilde{Q}}/\|\tilde{Q}\|_E^4$ is regular off the origin. This is the definite case of the firmest kind: the Cauchy theory there has a single singularity, the origin.

On the full algebra the coefficient ring is the split complex algebra $\mathbb{D}$ rather than the complex field, and this changes the geometry of the singular set without changing the equations. The zero divisors are the union $Z = \mathbb{H}\tilde\Pi_+ \cup \mathbb{H}\tilde\Pi_-$ of the two four-dimensional ideals, so the singular set of the naive inverse is a union of two linear subspaces rather than the quadric hypersurface of the biquaternion case. In particular the Fueter operator is elliptic over the real coordinates of a four-dimensional subspace, but the pointwise inversion of $\tilde{Q}$ fails on $Z$, and a domain for the Cauchy theory of the full algebra must avoid $Z$, not merely the origin. On the indefinite subspaces the second-order operator is the wave operator of signature $(3,1)$ or $(1,3)$, so the axial coefficients satisfy a wave-type system rather than a Laplace system; the null cone of the relevant real form is the characteristic set.

## The Relation to the Biquaternion and Split Quaternion Theories

The biquaternion Fueter theory is obtained by replacing $\mathbb{D}$ with $\mathbb{C}$: there the coefficient algebra is a field, the singular set of the full algebra is the null quadric of the complex norm form, of real dimension six, and the Fueter operator fails ellipticity over $\mathbb{C}$. In the split biquaternion case the coefficient algebra is the split complex algebra, the singular set is the union of two linear four-spaces, and the Fueter operator remains elliptic over the real coordinates of each four-dimensional subspace; the split biquaternion theory is thus the "indefinite coefficient" companion of the biquaternion theory, with the quadric hypersurface of singularities replaced by a union of subspaces.

The split quaternion theory, by contrast, is the four-dimensional algebra $\mathbb{H}_{\mathrm{s}} \cong \mathrm{Cl}_{1,1} \cong M_2(\mathbb{R})$, whose Fueter theory has its own zero divisors and its own three-sphere structure; it is a *different system* and must not be identified with $\mathbb{H}_{\mathbb{D}}$. The two are related by the tensor factorisation: the split biquaternion algebra is the split complex extension of the quaternions, not the complexification of the split quaternions, and the Fueter theory of the present article is that of the quaternion algebra with split complex coefficients. On the quaternion subspace the three theories agree in their equations, differing only in the coefficient ring that decorates the solution space.

## Summary

The Fueter operator $\tilde{\nabla} = \sum_\mu e_\mu\partial_\mu$ and its conjugate factor the four-dimensional Laplacian on the quaternion subspace, $\tilde{\nabla}\bar{\tilde{\nabla}} = \bar{\tilde{\nabla}}\tilde{\nabla} = \Delta_4e_0$, and left-regularity $\tilde{\nabla}\tilde{F} = 0$ and right-regularity $\tilde{F}\tilde{\nabla} = 0$ differ only in the sign of the curl term of the componentwise system, coinciding for axially symmetric functions; every regular function is harmonic, hence real-analytic on the quaternion subspace, and satisfies the mean value property. On the full algebra regularity is the pair of quaternionic regularities of the two idempotent components, a splitting with no counterpart in the simple biquaternion algebra. The Fueter construction sends a holomorphic $f_0$ to the induced function $\Delta_4\tilde{f}_0 = 2u_\rho/\rho + \hat{\mathbf{q}}(2v_\rho/\rho - 2v/\rho^2)$, which is both left- and right-regular; it is $\mathbb{C}$-linear with the affine functions as kernel, hence injective exactly for holomorphic functions whose Taylor coefficients vanish to order two, and the Fueter–Sce theorem extends it to odd-dimensional Clifford algebras with the power $(n-1)/2$ under the hypotheses of holomorphic convergence, order-two vanishing and odd dimension. The imaginary units of the full algebra form the four-dimensional manifold $S^2\times S^2$ rather than a sphere, so the slice approach must select one root at a time. On the quaternion subspace the origin is the only singularity; on the full algebra the coefficient ring is the split complex algebra and the singular set is the union of the two ideals, a union of two linear four-spaces rather than a quadric, this being the exact difference from the biquaternion theory, whose singular set is the six-dimensional null quadric and whose operator loses ellipticity over $\mathbb{C}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}_{\mathbb{D}} = \mathbb{D}\otimes_{\mathbb{R}}\mathbb{H}$ | Split biquaternion algebra |
| $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ | Quaternion subspace, the domain of Fueter theory |
| $\tilde{Q} = \sum_\mu Q_\mu e_\mu$, $Q_\mu \in \mathbb{D}$ | Split biquaternion; real coefficients on the quaternion subspace |
| $\mathbf{q} = \sum_k q_ke_k$, $\rho = \|\mathbf{q}\|_E$, $\hat{\mathbf{q}} = \mathbf{q}/\rho$ | Vector part, its modulus, its direction |
| $\tilde{\nabla} = \partial_0 + \mathbf{D}$, $\mathbf{D} = \sum_k e_k\partial_k$ | Fueter operator, acting on the left |
| $\bar{\tilde{\nabla}} = \partial_0 - \mathbf{D}$ | Conjugate Fueter operator |
| $\Delta_4 = \sum_\mu\partial_\mu^2$ | Four-dimensional Laplacian, $\tilde{\nabla}\bar{\tilde{\nabla}} = \bar{\tilde{\nabla}}\tilde{\nabla} = \Delta_4e_0$ |
| $\tilde{F}$ left-regular / right-regular | $\tilde{\nabla}\tilde{F} = 0$ / $\tilde{F}\tilde{\nabla} = 0$ |
| $I$, $\mathbb{C}_I = \mathbb{R}+I\mathbb{R}$ | Imaginary unit, $I^2 = -1$; slice |
| $A, B$ | Axial coefficients, $\tilde{F} = A(q_0,\rho) + \hat{\mathbf{q}}B(q_0,\rho)$ |
| $\tilde{f}_0$, $\Delta_4\tilde{f}_0$ | Axial extension of $f_0$ and its Fueter-induced function |
| $Z = \mathbb{H}\tilde\Pi_+\cup\mathbb{H}\tilde\Pi_-$ | Zero divisor locus of the full algebra |
| $\mathrm{Cl}_{0,n}$, $\mathrm{Cl}_{0,3}^{+}$ | Clifford algebras; $\mathbb{H}$ is $\mathrm{Cl}_{0,3}^{+}$ |

## Further Reading

- F. Brackx, R. Delanghe and F. Sommen, *Clifford Analysis*, Research Notes in Mathematics 76 (Pitman, 1982), for monogenic functions and the Cauchy–Riemann operator.
- R. Delanghe, F. Sommen and V. Souček, *Clifford Algebra and Spinor-Valued Functions* (Kluwer, 1992), for the analytic theory of the Cauchy–Riemann operator and the Fueter–Sce construction.
- Klaus Gürlebeck and Wolfgang Sprößig, *Quaternionic and Clifford Calculus for Physicists and Engineers* (Wiley, 1997), for the componentwise regularity system and the axial approach.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd edition (Cambridge University Press, 2001), for the Clifford relation among the units and the identification $\mathbb{H}\cong\mathrm{Cl}_{0,3}^{+}$.
