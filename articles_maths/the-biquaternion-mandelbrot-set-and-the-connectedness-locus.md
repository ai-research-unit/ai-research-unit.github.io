# __The Biquaternion Mandelbrot Set and the Connectedness Locus__

## Introduction

The Mandelbrot set is the set of complex parameters $C$ for which the orbit of the critical point $0$ under $\zeta\mapsto\zeta^2+C$ is bounded, and it is also the set for which the Julia set is connected. In the biquaternion algebra $\mathbb{B}$ the parameter is an element $\tilde Q_2$ and not a complex number, the critical set is not a point but the union of the zero-divisor cone with the vector subspace $\mathrm{Vect}(\mathbb{B})$, and the two classical descriptions of the locus — the boundedness of the critical orbit and the connectedness of the Julia set — are no longer obviously the same. This article defines the connectedness locus and the critical-orbit locus, computes both on the subalgebras where the algebra is commutative and the reduction to the complex plane is exact, and records where the biquaternion answer is open.

The quadratic family, its filled Julia set, its Julia set and its critical set are *The Biquaternion Quadratic Map and Its Julia Sets*, and its derivative and holomorphy are *The Biquaternion Holomorphic Dynamics and the Jacobian*. The classical theory is *The Mandelbrot Set and the Quadratic Family*, *The Real Quadratic Family and Its Bifurcations* and *The Julia Sets of a Complex Polynomial*; the quaternion case is *The Quaternion Mandelbrot Set*; the two-variable complex theory is *Several Complex Variables* and the holomorphic dynamics of Part III. All are used here and none is restated.

The article owns the definition of the connectedness locus and of the critical-orbit locus, the escape-time algorithm and the obstruction to a single escape radius, the exact reduction on the central and commutative slices, and the placement of the real, the complex and the quaternion parameter sweeps. It does not prove any connectedness criterion in the full algebra; that is stated as the open problem it is.

**Standing convention.** The parameter is $\tilde Q_2\in\mathbb{B}$, the map is $F_{\tilde Q_2}(\tilde Q)=\tilde Q^2+\tilde Q_2$ in the general plain bilinear product, the filled Julia set is $\mathcal K_{\tilde Q_2}$ and the Julia set is $J_{\tilde Q_2}=\partial\mathcal K_{\tilde Q_2}$. A central parameter is written $\tilde Q_2=Ce_t$ with $C\in\mathbb{C}$; the connectedness locus is written $\mathcal B$ and the critical-orbit locus $\mathcal C$.

## The Two Loci

**Definition.** The **connectedness locus** is

$$
\mathcal B=\{\tilde Q_2\in\mathbb{B} : J_{\tilde Q_2} \text{ is connected}\},
$$

and the **critical-orbit locus** is

$$
\mathcal C=\{\tilde Q_2\in\mathbb{B} : \text{the orbit of } 0 \text{ under } F_{\tilde Q_2} \text{ is bounded}\}.
$$

**Remark (why the orbit of $0$ and not of every critical point).** In one variable the critical set is the single point $0$, so the two readings of the definition coincide. In $\mathbb{B}$ the critical set is the union of the zero-divisor cone with the vector subspace, it is unbounded, and it contains points with escaping orbits for every parameter, so the condition that *every* critical orbit be bounded is empty and cannot be the definition. The definition used here is the boundedness of the orbit of $0$, the point that is critical for every invariant complex plane, which is the condition tested by the escape-time algorithm and the one that reduces to the classical Mandelbrot set on the central slice.

**Remark (the two agree in $\mathbb{C}$ and are not asserted to agree here).** In the complex plane the theorem of Douady and Hubbard identifies the two loci with the Mandelbrot set; the identification rests on a normal-family construction in one variable and does not transport to $\mathbb{C}^4$ by itself. **The relation between $\mathcal B$ and $\mathcal C$ in $\mathbb{B}$ is the central open question of this article and of the category.** What can be proved here is the shape of the two loci on the subalgebras where the algebra is commutative.

**Definition.** The **biquaternion Mandelbrot set** is the critical-orbit locus $\mathcal C$; where the two loci are known to agree the two names are used interchangeably, the context naming the reading.

## The Escape-Time Algorithm and the Obstruction

The escape-time algorithm decides membership in the complement of the critical-orbit locus by iterating and testing a numerical bound. The test rests on a lower bound for the size of a product, and that is where the biquaternion case departs from the classical one.

**Proposition (the classical bound).** Let $q$ be a real quaternion, $c$ a real quaternion, and $|\cdot|$ the quaternion norm. If $|q|>1+|c|$ then $|q^2+c|\ge|q|^2-|c|>|q|$, so the orbit of $q$ under $q\mapsto q^2+c$ escapes and $|q_n|\to\infty$.

**Proof.** $|q^2|=|q|^2$ by multiplicativity of the quaternion norm, and the triangle inequality gives the lower bound. From $|q|>1+|c|$, $|q|^2-|c|>|q|(1+|c|)-|c|=|q|+|c|(|q|-1)>|q|$; the size strictly increases at every step and the increment grows.

In $\mathbb{B}$ no such bound exists in the Euclidean norm, because the biquaternion square can vanish.

**Proposition (the collapse).** There are non-zero $\tilde Q\in\mathbb{B}$ with $\tilde Q^2=0$ and $\|\tilde Q\|_E$ arbitrarily large, so $\|\tilde Q^2\|_E$ admits no lower bound in terms of $\|\tilde Q\|_E$ and the classical escape-time test cannot be applied to the Euclidean norm.

**Proof.** A pure vector $\vec Q=\sum_{k=1}^3Q_k\vec e_k$ has $\vec Q^2=-(\sum_kQ_k^2)e_t$, so $\vec Q^2=0$ exactly when $\sum_kQ_k^2=0$; the element $\tilde Q=\vec e_x+i\vec e_y$ satisfies this, and $\lambda\tilde Q$ does too for every $\lambda\in\mathbb{C}$. The norm of $\lambda\tilde Q$ is $|\lambda|\sqrt2$, unbounded, while its square is zero.

The failure is not a defect of the Euclidean norm alone. The biquaternion norm $\langle\cdot\rangle_{\natural}$ is multiplicative but complex-valued and vanishes on the zero divisors, and its modulus $r=\sqrt{|N|}$ vanishes on the same set; neither can serve as a size. The unique real multiplicative semi-norm of the algebra is $r$ itself, and a semi-norm that vanishes off the origin cannot decide escape (*N-Regularity and Degeneracy in the Biquaternion Algebra*). **The escape-time algorithm exists in $\mathbb{B}$ only off the zero-divisor cone.**

What survives is a conditional bound, phrased through the singular values of the matrix model.

**Proposition (conditional escape).** Let $\tilde Q\in\mathbb{B}$, $M=\mathsf{M}_2(\tilde Q)$, let $\sigma_1\ge\sigma_2\ge0$ be the two singular values of $M$, and suppose $\sigma_2\ge\delta\sigma_1$ for some $\delta>0$. Then

$$
\|\tilde Q^2\|_E\ge\delta^2\|\tilde Q\|_E^2 .
$$

Consequently, if $\delta^2\|\tilde Q\|_E^2-\|\tilde Q_2\|_E>\|\tilde Q\|_E$, in particular for

$$
\boxed{\;\|\tilde Q\|_E>R_\delta:=\frac{1+\sqrt{1+4\delta^2\|\tilde Q_2\|_E}}{2\delta^2}\;},
$$

then $\|F_{\tilde Q_2}(\tilde Q)\|_E>\|\tilde Q\|_E$ and the orbit of $\tilde Q$ escapes.

**Proof.** For a $2\times2$ matrix $A$, $\|A\|_F^2=\sigma_1(A)^2+\sigma_2(A)^2\ge2\sigma_2(A)^2$, so $\|A\|_F\ge\sqrt2\,\sigma_2(A)$; and $\sigma_2(M^2)\ge\sigma_2(M)^2$, because $\sigma_1\sigma_2=|\det|$, $\sigma_1$ is submultiplicative, and
$$
\sigma_2(M^2)=\frac{|\det M|^2}{\sigma_1(M^2)}\ge\frac{|\det M|^2}{\sigma_1(M)^2}=\sigma_2(M)^2 .
$$
Also $\|M\|_F^2\le2\sigma_1(M)^2$ gives $\sigma_1(M)\ge\|M\|_F/\sqrt2=\|\tilde Q\|_E$, using $\|\mathsf{M}_2(\tilde Q)\|_F=\sqrt2\|\tilde Q\|_E$. Hence

$$
\|M^2\|_F\ge\sqrt2\,\sigma_2(M^2)\ge\sqrt2\,\sigma_2(M)^2\ge\sqrt2\,\delta^2\sigma_1(M)^2\ge\sqrt2\,\delta^2\|\tilde Q\|_E^2 ,
$$

and dividing by $\sqrt2$ gives $\|\tilde Q^2\|_E=\|M^2\|_F/\sqrt2\ge\delta^2\|\tilde Q\|_E^2$. The triangle inequality finishes.

**Remark (what $\delta$ measures).** The quantity $\delta=\sigma_2/\sigma_1$ is the reciprocal condition number of the iterate; $\delta=0$ exactly on the zero divisors. **The conditional escape radius is a family $R_\delta$ indexed by the distance to the zero-divisor cone, and there is no finite radius uniform in $\delta$.** The radius $R_\delta$ is the honest replacement of the single escape radius of the field, and it is developed in *The Escape Radius and the Green's Function for the Biquaternions*.

## The Central Slice

**Proposition (the critical orbit of a central parameter is classical).** Let $\tilde Q_2=Ce_t$. Then $F_{\tilde Q_2}^n(0)=q_n(0)e_t$, where $q_n(0)$ is the $n$-th iterate of $0$ under $\zeta\mapsto\zeta^2+C$. In particular

$$
\boxed{\;0\in\mathcal C_{\text{central}}:=\{\tilde Q_2=Ce_t : F_{\tilde Q_2}^n(0) \text{ bounded}\} \iff C\in\mathcal M\;},
$$

the complex Mandelbrot set.

**Proof.** $F_{\tilde Q_2}(0)=\tilde Q_2=Ce_t$, and $F_{\tilde Q_2}(Ae_t)=A^2e_t+Ce_t=(A^2+C)e_t$ because $e_t$ is the identity and the parameter is central; induction gives the claim. Boundedness in $\mathbb{B}$ is the boundedness of the complex sequence, which is the definition of the Mandelbrot set.

**Remark (the whole central slice is classical).** The proposition is the orbit of the single point $0$; more is true for the filled Julia set, by the eigenvalue reduction of *The Biquaternion Quadratic Map and Its Julia Sets*: for a central parameter $\tilde Q_2=Ce_t$ and a diagonalisable $\mathsf{M}_2(\tilde Q)$ with spectrum $\{\lambda_1,\lambda_2\}$, the point $\tilde Q$ lies in $\mathcal K_{\tilde Q_2}$ exactly when both $\lambda_j$ lie in the complex filled Julia set $K_C$. **The central slice of the biquaternion theory is the complex theory, read on the two eigenvalues.**

**Corollary (the centre is a slice of $\mathcal C$).** The intersection of $\mathcal C$ with the centre $\mathbb{C}_{\mathbb{B}}$ is the embedded copy of the Mandelbrot set $\mathcal M\subset\mathbb{C}$, under $C\mapsto Ce_t$.

## The Commutative Plane and the Product Locus

The reduction is not special to the centre: every two-dimensional commutative subalgebra cut out by an idempotent gives the same phenomenon, with two independent complex parameters.

**Theorem (the idempotent plane).** Let $\tilde\Pi$ be a primitive idempotent of $\mathbb{B}$ and let $\tilde\Pi'=e_t-\tilde\Pi$ be its complement, so that $\tilde\Pi\tilde\Pi'=\tilde\Pi'\tilde\Pi=0$ and $\tilde\Pi+\tilde\Pi'=e_t$. The plane

$$
W_{\tilde\Pi}=\mathbb{C}\tilde\Pi\oplus\mathbb{C}\tilde\Pi'
$$

is a commutative subalgebra isomorphic to $\mathbb{C}\oplus\mathbb{C}$ by $A\tilde\Pi+B\tilde\Pi'\mapsto(A,B)$; the product there is coordinatewise, and for a parameter $\tilde Q_2=C_1\tilde\Pi+C_2\tilde\Pi'$ the restriction of $F_{\tilde Q_2}$ to $W_{\tilde\Pi}$ is the pair of commuting complex quadratic maps

$$
(A,B)\longmapsto(A^2+C_1,\;B^2+C_2).
$$

Hence

$$
\boxed{\;W_{\tilde\Pi}\cap\mathcal K_{\tilde Q_2}=K_{C_1}\times K_{C_2}, \qquad W_{\tilde\Pi}\cap\mathcal C=\{C_1\in\mathcal M\}\times\{C_2\in\mathcal M\}\;},
$$

and the critical-orbit locus of the plane is the product $\mathcal M\times\mathcal M$. The general plain bilinear product therefore gives the **intersection** of the two conditions, not their union.

**Proof.** $\tilde\Pi^2=\tilde\Pi$, $\tilde\Pi'^2=\tilde\Pi'$ and $\tilde\Pi\tilde\Pi'=0$ give $(A\tilde\Pi+B\tilde\Pi')^2=A^2\tilde\Pi+B^2\tilde\Pi'$, and the parameter splits the same way; the two coordinates do not interact, so the orbit is the pair of complex orbits and both must be bounded.

**Remark (the choice of product and the shape of the locus).** On the diagonal subalgebra the complex bilinear product has no cross term, so the locus is a product; a product that mixes the two coordinates would couple the two iterations, and the locus would be neither a product nor a union but a genuinely two-variable object. **The phrase "intersection or union of two lower-dimensional loci" is exact only where the algebra splits; where it does not, no such description holds.** The comparison of the four general products is *The Four General Products and Their Relations over the Biquaternion Algebra*.

## The Computable Slices

The parameter space is eight-real-dimensional, and the article records the three slices on which the sweep can actually be computed, one to a subsection.

### The Real Slice

For $\tilde Q_2=ce_t$ with $c\in\mathbb{R}$ the central parameter is real, the complex map has real coefficients, and the critical orbit is the real critical orbit of *The Real Quadratic Family and Its Bifurcations*. The slice is therefore the real interval $[-2,\tfrac14]$ of the classical theory, at the real axis of the embedded copy of $\mathcal M$, and on it the bifurcation structure is the one of the real quadratic family. The whole-picture symmetry is the full group of involutions $G$, since a real central parameter is fixed by every element of $G$ (*The Biquaternion Quadratic Map and Its Julia Sets*, §*The Conjugations and the Equivariance*).

### The Complex Slice

For $\tilde Q_2=Ce_t$ with $C\in\mathbb{C}$ the slice is the whole classical Mandelbrot set, by the corollary of §*The Central Slice*, and its symmetry is the subgroup $\{\mathrm{id},{}^{\natural}\}$ together with the single reflection $C\mapsto\bar C$ of the complex plane, which is not one of the four biquaternion conjugations but the bar restricted to the centre. It is the slice on which the biquaternion escape-time picture coincides with the classical one, and is the picture usually shown as "the biquaternion Mandelbrot set".

### The Quaternion Slice

For $\tilde Q_2\in\mathbb{H}_{\mathbb{B}}$, the real quaternion subspace, the algebra is not commutative and the reduction to the centre does not apply; but the parameter lies in a division subalgebra, the norm is real and positive definite there, and the slice reproduces the quaternion Mandelbrot set of *The Quaternion Mandelbrot Set*. The slice is the computable three-dimensional picture, and it is the one on which the classical escape radius is available, since the quaternion subspace is a division algebra.

**Remark (the warning).** The three slices are different sets, and a picture of "the biquaternion Mandelbrot set" is a picture of a slice. **Every visualisation must state its slice, and no slice is canonical.** The warning is made in full in *The Slices of the Biquaternion Julia Sets*, where it belongs.

## Summary

The connectedness locus $\mathcal B$ and the critical-orbit locus $\mathcal C$ agree in the complex plane and are not proved to agree in $\mathbb{B}$; their relation is the central open question of the category, and the article states them separately. The escape-time algorithm fails in the Euclidean norm because the square of a non-zero element can vanish, so no single escape radius exists; what survives is a conditional radius $R_\delta$ indexed by the reciprocal condition number $\delta=\sigma_2/\sigma_1$ of the iterate, finite off the zero-divisor cone and unbounded as $\delta\to0$. On the central slice the critical orbit of $0$ is the classical one, so the slice of the critical-orbit locus is the embedded Mandelbrot set, and on every idempotent plane the map splits into two commuting complex quadratic maps with the locus $\mathcal M\times\mathcal M$, an intersection and not a union. The computable slices are the real interval $[-2,\tfrac14]$, the embedded Mandelbrot set, and the quaternion Mandelbrot set; each is a slice, and the warning that no slice is canonical closes the article.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde Q_2$ | the biquaternion parameter |
| $F_{\tilde Q_2}(\tilde Q)=\tilde Q^2+\tilde Q_2$ | the quadratic family |
| $\mathcal K_{\tilde Q_2}$, $J_{\tilde Q_2}$ | the filled Julia set and the Julia set |
| $\mathcal B$ | the connectedness locus |
| $\mathcal C$ | the critical-orbit locus, the biquaternion Mandelbrot set |
| $\mathcal M$, $K_C$ | the complex Mandelbrot set and filled Julia set |
| $\mathsf{M}_2$ | the matrix realization |
| $\sigma_1\ge\sigma_2$ | the singular values of $\mathsf{M}_2(\tilde Q)$; $\delta=\sigma_2/\sigma_1$ |
| $R_\delta$ | the conditional escape radius at condition $\delta$ |
| $\|\cdot\|_E$, $\|\cdot\|_F$ | the Euclidean norm on $\mathbb{B}$ and the Frobenius norm on $M_2(\mathbb{C})$ |
| $\tilde\Pi$, $\tilde\Pi'=e_t-\tilde\Pi$ | a primitive idempotent and its complement |
| $W_{\tilde\Pi}=\mathbb{C}\tilde\Pi\oplus\mathbb{C}\tilde\Pi'$ | the commutative idempotent plane |
| $G$ | the group of involutions |

## Further Reading

- [The Biquaternion Quadratic Map and Its Julia Sets](the-biquaternion-quadratic-map-and-its-julia-sets.html), for the family, the critical set and the central-parameter reduction used here.
- [The Escape Radius and the Green's Function for the Biquaternions](the-escape-radius-and-the-greens-function-for-the-biquaternions.html), for the conditional radius in full.
- [The Mandelbrot Set and the Quadratic Family](the-mandelbrot-set-and-the-quadratic-family.html) and [The Real Quadratic Family and Its Bifurcations](the-real-quadratic-family-and-its-bifurcations.html), for the classical loci the slices reproduce.
- [The Quaternion Mandelbrot Set](the-quaternion-mandelbrot-set.html), for the quaternion slice.
- [The Zero Divisors and the Singular Julia Sets](the-zero-divisors-and-the-singular-julia-sets.html), for the set on which the escape test collapses.
