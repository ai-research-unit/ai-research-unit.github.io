
# __Dual-Numbers Analysis on Subspaces__

## Introduction

The article *Dual-Numbers Analysis* defined limits, continuity, the dual derivative, the Cauchy–Riemann equations and the Wirtinger derivatives on the dual plane, and *Dual-Numbers Integration* defined the contour integral and the Cauchy–Goursat theorem there. This article specialises the differential operators to the two distinguished submodules of the dual algebra, the **real submodule** $R_{\mathbb{D}'}$ and the **infinitesimal submodule** $\varepsilon R_{\mathbb{D}'}$, and reduces the analysis to the real line and its first-order neighbourhood. The structural model is *Biquaternion Analysis on Subspaces*, where six subspaces of $\mathbb{B}$ carry specialisations of one abstract Cauchy–Riemann operator; here only two submodules exist and both are one-dimensional, so the specialisation is correspondingly sharper.

The treatment is mathematically honest: every claim is either proved or stated as a definition. No physics is invoked. Throughout the algebra is $\mathbb{D}'$ over $\mathbb{R}$, the independent variable is written

$$
Z = x + y\varepsilon, \qquad x, y \in \mathbb{R},
$$

so that $x$ is the coordinate on the real submodule and $y$ the coordinate on the infinitesimal submodule, and a function is written

$$
f(Z) = u(x, y) + v(x, y)\varepsilon, \qquad u, v : U \to \mathbb{R},
$$

with $U$ an open subset of the dual plane. The real coordinates identify $\mathbb{D}'$ with $\mathbb{R}^2$. The norm form is $N(Z) = x^2$, the maximal ideal is $\mathfrak{m} = (\varepsilon) = \varepsilon\mathbb{R}$, dual conjugation is $\bar{Z} = x - y\varepsilon$, and the Euclidean structure is $\|Z\|_E^2 = x^2 + y^2$.

## The Differential Operators on the Two Submodules

### The Coordinate Operators

**Definition.** The **coordinate operators** are the ordinary partial derivatives

$$
\partial_x = \frac{\partial}{\partial x}, \qquad \partial_y = \frac{\partial}{\partial y},
$$

acting on $\mathbb{R}$-valued and $\mathbb{D}'$-valued functions on $U$, together with the operator $M_\varepsilon$ of multiplication by $\varepsilon$.

The three operators generate the algebra of constant-coefficient differential operators on the dual plane, and their composite relations are governed by $\varepsilon^2 = 0$:

$$
M_\varepsilon \circ \partial_x = \partial_x \circ M_\varepsilon, \qquad M_\varepsilon \circ \partial_y = \partial_y \circ M_\varepsilon, \qquad M_\varepsilon^2 = 0.
$$

**Proposition.** The two partial derivatives commute, $\partial_x\partial_y = \partial_y\partial_x$, and $M_\varepsilon$ commutes with both, so the algebra they generate is commutative.

**Proof.** Partial derivatives commute by the symmetry of second derivatives; $M_\varepsilon$ commutes with $\partial_x, \partial_y$ because $\varepsilon$ is a constant. $\square$

### The Operators Restricted to the Submodules

The two submodules are the eigenspaces of dual conjugation and they carry different data.

**Definition.** The **real operator** is the derivative along the real submodule,

$$
D_{\mathbb{R}} = \partial_x,
$$

acting on functions of $x$ alone; the **infinitesimal operator** is the derivative along the infinitesimal submodule,

$$
D_{\mathfrak{m}} = \partial_y,
$$

acting on the coefficient of $\varepsilon$.

**Proposition.** On a function written $f = u + v\varepsilon$,

$$
\partial_x f = u_x + v_x\varepsilon, \qquad \partial_y f = u_y + v_y\varepsilon, \qquad M_\varepsilon f = u\varepsilon.
$$

So $\partial_x, \partial_y$ differentiate both components, while $M_\varepsilon$ projects onto the infinitesimal submodule by discarding the real part. In particular $M_\varepsilon$ annihilates the real submodule $R_{\mathbb{D}'}$ and maps the whole algebra onto $\mathfrak{m}$.

**Proof.** The two first formulas are the componentwise partial derivatives; the third uses $\varepsilon^2 = 0$, which kills the term $v\varepsilon^2$. The final statement is $M_\varepsilon(u + v\varepsilon) = u\varepsilon$, which vanishes iff $u = 0$. $\square$

### The Real and Infinitesimal Components

The submodules also define the component maps

$$
\operatorname{Re} f = u, \qquad \operatorname{Inf} f = v, \qquad \text{so that } f = \operatorname{Re} f + (\operatorname{Inf} f)\varepsilon.
$$

The operator $\operatorname{Re}$ is the augmentation $\mathbb{D}' \to \mathbb{R}$ of *Dual-Numbers Analysis*, and it is a ring homomorphism with kernel $\mathfrak m$; the operator $\operatorname{Inf}$ is a linear map $\mathbb{D}' \to \mathbb{R}$ vanishing on the real submodule.

## The Cauchy–Riemann Operator in Dual Coordinates

### The Cauchy–Riemann Equations

**Definition.** A function $f = u + v\varepsilon$ is **dual differentiable** (dual holomorphic) at $Z_0$ if the limit

$$
f'(Z_0) = \lim_{h \to 0} \frac{f(Z_0 + h) - f(Z_0)}{h},
$$

taken along invertible increments $h$, exists as a dual number.

**Theorem (dual Cauchy–Riemann equations).** $f = u + v\varepsilon$ is dual differentiable at $Z_0 = x_0 + y_0\varepsilon$ if and only if $u, v$ are real differentiable near $(x_0, y_0)$ and

$$
u_y = 0, \qquad v_y = u_x.
$$

In that case

$$
f'(Z) = u_x + v_x\varepsilon.
$$

**Proof.** For $h = h_1 + h_2\varepsilon$ with $h_1 \neq 0$, write $\rho = h_2/h_1$ for the direction of the increment. Since $h^{-1} = h_1^{-1}(1 - \rho\varepsilon)$ and $\varepsilon^2 = 0$, the difference quotient is, to zeroth order in $h$,

$$
\frac{f(Z_0 + h) - f(Z_0)}{h} = u_x + u_y\rho + \left(v_x + (v_y - u_x)\rho - u_y\rho^2\right)\varepsilon + O(h).
$$

For the limit to be independent of the direction $\rho$, the coefficients of the powers of $\rho$ in each component must vanish, giving $u_y = 0$ and then $v_y = u_x$; the remaining part is $u_x + v_x\varepsilon$. $\square$

### The Cauchy–Riemann and Holomorphic Operators

**Definition.** The **Cauchy–Riemann operator** and the **holomorphic operator** are

$$
\bar\partial = \partial_y - \varepsilon\partial_x, \qquad \partial_Z = \partial_x.
$$

**Theorem.** $f$ is dual differentiable if and only if $\bar\partial f = 0$, and then $f' = \partial_Z f$.

**Proof.** $\bar\partial f = (\partial_y - \varepsilon\partial_x)(u + v\varepsilon) = u_y + (v_y - u_x)\varepsilon$, using $\varepsilon^2 = 0$. This vanishes exactly when $u_y = 0$ and $v_y = u_x$, which is the Cauchy–Riemann system; and $\partial_Z f = u_x + v_x\varepsilon = f'$. $\square$

**Remark.** The Cauchy–Riemann operator here has the asymmetric shape $\bar\partial = \partial_y - \varepsilon\partial_x$, with the algebra element $\varepsilon$ multiplying the *real* derivative rather than the infinitesimal one. This is forced by nilpotence: the naive analogue of the complex operator $\partial_x + i\partial_y$, namely $\partial_x + \varepsilon\partial_y$, does **not** annihilate the dual-holomorphic functions, since $(\partial_x + \varepsilon\partial_y)(x + y\varepsilon) = 1 \neq 0$. The complex operator owes its shape to $i^2 = -1$; with $\varepsilon^2 = 0$ the operator must be rearranged into $\partial_y - \varepsilon\partial_x$.

### The Solution Class

**Corollary.** A function on a connected domain $U$ is dual differentiable if and only if it has the form

$$
f(x + y\varepsilon) = u(x) + \bigl(y\,u'(x) + c(x)\bigr)\varepsilon,
$$

for ordinary differentiable functions $u$ and $c$ of the single variable $x$. In particular

$$
f'(Z) = u'(x) + \bigl(y\,u''(x) + c'(x)\bigr)\varepsilon.
$$

**Proof.** $u_y = 0$ gives $u = u(x)$; then $v_y = u'(x)$ integrates to $v = y\,u'(x) + c(x)$. The derivative is $u_x + v_x\varepsilon$ by the theorem. $\square$

So the dual-holomorphic functions are parametrised by two arbitrary differentiable functions of one variable, $u$ and $c$, in contrast with the complex case, where a holomorphic function is parametrised by one analytic function of one variable and its real and imaginary parts are harmonic. The real part $u(x)$ is in general not harmonic: $\Delta u = u''(x) \neq 0$ unless $u$ is affine.

## The Nilpotent Component and the Maximal Ideal

### The Two Components of the Cauchy–Riemann Operator

**Definition.** Write the Cauchy–Riemann operator as

$$
\bar\partial = \underbrace{\partial_y}_{\text{scalar part}} \; \underbrace{-\, \varepsilon\,\partial_x}_{\text{nilpotent part}},
$$

its **scalar part** $\partial_y$ and its **nilpotent part** $-\varepsilon\partial_x$, the latter carrying the factor $\varepsilon$.

**Proposition.** Multiplication by $\varepsilon$ kills the nilpotent part:

$$
M_\varepsilon \circ \bar\partial = \varepsilon\,\partial_y = \bar\partial \circ M_\varepsilon.
$$

So composing with $\varepsilon$ discards the nilpotent part and retains only the scalar part, and the two agree as operators.

**Proof.** $\varepsilon(\partial_y - \varepsilon\partial_x) = \varepsilon\partial_y - \varepsilon^2\partial_x = \varepsilon\partial_y$, and $\varepsilon\partial_y = (\partial_y - \varepsilon\partial_x)\varepsilon$ since $\varepsilon$ is constant. $\square$

**Corollary.** On the nilpotent direction the operator $\bar\partial$ becomes $\varepsilon\partial_y$, an operator of rank one in the algebra: it maps a function to an element of $\mathfrak m$ whose real part is zero. The nilpotent part $-\varepsilon\partial_x$ of $\bar\partial$ is annihilated by multiplication by $\varepsilon$, so it never contributes to the infinitesimal part of $\bar\partial f$.

### The Maximal Ideal as the Nilpotent Direction

**Theorem.** The maximal ideal $\mathfrak{m} = \varepsilon\mathbb{R}$ is exactly the image of $M_\varepsilon$ and exactly the kernel of the augmentation $\operatorname{Re}$. The Cauchy–Riemann operator annihilates the constants and, restricted to the real submodule, is $-\partial_x$ times $\varepsilon$, while every dual-holomorphic function is determined by its restriction to $R_{\mathbb{D}'}$ together with the derivative $u'$.

**Proof.** $M_\varepsilon(\mathbb{D}') = \varepsilon\mathbb{D}' = \mathfrak{m}$ since $\varepsilon^2 = 0$; $\ker\operatorname{Re} = \mathfrak{m}$ by definition; $\bar\partial(\text{const}) = 0$; and the solution class $u(x) + (yu'(x) + c(x))\varepsilon$ is fixed by $u$ and $c$, both functions on $R_{\mathbb{D}'}$. $\square$

### The Second-Order Operators and the Failure of Factorisation

**Definition.** The **algebra-valued gradient** and its **conjugate** are

$$
\nabla = \partial_x + \varepsilon\partial_y, \qquad \bar\nabla = \partial_x - \varepsilon\partial_y.
$$

They are the specialisations of the model's abstract operator $\tilde\nabla = \sum_\mu e_\mu \partial_\mu$ to the dual basis $(e_0, e_1) = (1, \varepsilon)$.

**Theorem.** $\nabla\bar\nabla = \bar\nabla\nabla = \partial_x^2$. Hence the **algebra-valued d'Alembertian** is

$$
\Box = \nabla\bar\nabla = \partial_x^2,
$$

the flat second derivative along the real direction.

**Proof.** $\nabla\bar\nabla = (\partial_x + \varepsilon\partial_y)(\partial_x - \varepsilon\partial_y) = \partial_x^2 - \varepsilon\partial_x\partial_y + \varepsilon\partial_y\partial_x - \varepsilon^2\partial_y^2 = \partial_x^2$, the cross terms cancelling by the commutation of partial derivatives and the last term vanishing because $\varepsilon^2 = 0$; the reverse order is identical. $\square$

**Theorem.** The square of the gradient satisfies the model identity

$$
\nabla^2 = 2\,\partial_x\nabla - \Box.
$$

**Proof.** $\nabla^2 = (\partial_x + \varepsilon\partial_y)^2 = \partial_x^2 + 2\varepsilon\partial_x\partial_y$, and $2\partial_x\nabla - \Box = 2\partial_x(\partial_x + \varepsilon\partial_y) - \partial_x^2 = \partial_x^2 + 2\varepsilon\partial_x\partial_y$. $\square$

**Corollary (failure of factorisation).** The Euclidean Laplacian

$$
\Delta = \partial_x^2 + \partial_y^2
$$

does **not** factor as a product $\nabla\bar\nabla$ of algebra-valued first-order operators; indeed $\nabla\bar\nabla = \partial_x^2$ is missing the term $\partial_y^2$, which is annihilated by $\varepsilon^2 = 0$ in the product. In the complex case the corresponding factorisation $\partial_x^2 + \partial_y^2 = (\partial_x + i\partial_y)(\partial_x - i\partial_y)$ holds because $i^2 = -1$; the dual algebra has no element squaring to $-1$, so no such factorisation exists.

This is the analytic face of the degeneracy of the norm form: just as $N(Z) = x^2$ fails to register the infinitesimal direction, the algebra-valued d'Alembertian $\Box = \partial_x^2$ fails to register it, and only the unaugmented Euclidean Laplacian $\Delta$ sees both directions. The second-order theory is richer than the product of the first-order operators, and this is the exact obstruction to a dual analogue of the factorised wave operator.

## Reduction to the Real Line and Its First-Order Neighbourhood

### The Real Line

**Theorem.** Every dual-holomorphic function $f$ on a connected domain is determined by the pair of ordinary differentiable functions

$$
u = \operatorname{Re} f \big|_{\{y = 0\}}, \qquad c = \operatorname{Inf} f \big|_{\{y = 0\}},
$$

the real part and the infinitesimal part of the restriction of $f$ to the real line. Explicitly,

$$
f(x + y\varepsilon) = u(x) + c(x)\varepsilon + y\,u'(x)\,\varepsilon.
$$

**Proof.** By the solution class, $f = u(x) + (yu'(x) + c(x))\varepsilon$, so the restriction to the axis $y = 0$ is $u(x) + c(x)\varepsilon$ and the coefficient of $y$ in the infinitesimal part is $u'(x)$. $\square$

So the analysis on the two-dimensional dual plane reduces completely to analysis on the one-dimensional real line: the data are two functions $u, c$ of $x$, and the whole $y$-dependence of a holomorphic function is the first-order term $y\,u'(x)$. The infinitesimal submodule is the **first-order neighbourhood** of the real line inside the dual plane, and a holomorphic function is affine along it.

### Integration on the Submodules

**Theorem.** A dual-holomorphic $f = u(x) + (yu'(x) + c(x))\varepsilon$ has the primitive

$$
F(x + y\varepsilon) = U(x) + \bigl(y\,u(x) + C(x)\bigr)\varepsilon, \qquad U' = u, \quad C' = c,
$$

so that $F' = f$. Consequently the contour integral of $f$ along a contour $\gamma$ reduces to the two real contour integrals

$$
\oint_\gamma f(Z)\,dZ = \oint_\gamma u\,dx + \left(\oint_\gamma \bigl(u\,dy + v\,dx\bigr)\right)\varepsilon, \qquad v = y\,u'(x) + c(x),
$$

and it vanishes for a closed contour in a simply connected domain, the dual Cauchy–Goursat theorem: the real part vanishes because $u_y = 0$, and the infinitesimal part vanishes because $v_y = u_x$, both by Green's theorem.

**Proof.** The primitive is verified componentwise: $\partial_x F = U'(x) + (yu'(x) + C'(x))\varepsilon = u(x) + (yu'(x) + c(x))\varepsilon = f(x + y\varepsilon)$, and $F$ is dual holomorphic because its real part $U$ depends only on $x$ and its infinitesimal part is $yU'(x) + C(x)$. For the contour formula, $dZ = dx + dy\,\varepsilon$ and $\varepsilon^2 = 0$ give $f\,dZ = u\,dx + (u\,dy + v\,dx)\varepsilon$; the real integral $\oint_\gamma u\,dx$ equals $-\iint u_y\,dA = 0$, and the infinitesimal integral $\oint_\gamma(u\,dy + v\,dx)$ equals $\iint(u_x - v_y)\,dA = 0$. $\square$

So integration too reduces to the real line: the primitive of a dual-holomorphic function is obtained by integrating its two real data functions.

### The Role of the Maximal Ideal

**Theorem.** The maximal ideal is the first-order neighbourhood of the real line: for every $h \in \mathfrak{m}$, translation $T_h(Z) = Z + h$ changes the infinitesimal coordinate by $h$ and every dual-holomorphic function is affine along the translates $Z + \mathfrak{m} = \{x + t\varepsilon : t \in \mathbb{R}\}$. The quotient $\mathbb{D}'/\mathfrak{m} \cong R_{\mathbb{D}'}$ is the real line, and the analysis of holomorphic functions is the analysis of their behaviour transverse to the maximal ideal.

**Proof.** $Z + t\varepsilon = x + (y + t)\varepsilon$, and a holomorphic function on that line is $u(x) + ((y+t)u'(x) + c(x))\varepsilon$, affine in $t$ with slope $u'(x)$; the quotient identification is the augmentation. $\square$

## Comparison with the Split Complex Case

### The Split Complex Operators

For the split complex algebra $\mathbb{D} = \mathbb{R}[j]$, $j^2 = +1$, write $z = x + yj$ and $f = u + vj$. The Cauchy–Riemann system is

$$
u_x = v_y, \qquad u_y = v_x,
$$

which factors through the idempotents $\Pi_\pm = \tfrac{1}{2}(1 \pm j)$: on setting $f = \phi \Pi_1 + \psi \Pi_2$, the system is equivalent to the two independent transport equations

$$
\partial_x\phi = \partial_y\phi, \qquad \partial_x\psi = -\partial_y\psi,
$$

with the general solutions $\phi = \phi(x + y)$ and $\psi = \psi(x - y)$.

**Proposition.** A split-complex holomorphic function is $\phi(x + y)\Pi_1 + \psi(x - y)\Pi_2$ for arbitrary differentiable $\phi, \psi$ of one variable; hence it too is determined by two functions of one variable, but along the characteristics $x + y$ and $x - y$.

**Proof.** Substituting $f = \phi(x+y)\Pi_1 + \psi(x-y)\Pi_2$ into the system gives $u_x = v_y$ and $u_y = v_x$ directly, using $j \Pi_1 = \Pi_1$ and $j \Pi_2 = -\Pi_2$. $\square$

### The Degeneration

The dual case is the contraction of the split-complex case in which the two characteristics $x \pm y$ coalesce to the single characteristic $x$ and the transported functions become polynomial of degree one in the transverse coordinate:

| | $\mathbb{D} = \mathbb{R}[j]$, $j^2 = +1$ | $\mathbb{D}'$, $\varepsilon^2 = 0$ |
|---|---|---|
| Cauchy–Riemann system | $u_x = v_y$, $u_y = v_x$ | $u_y = 0$, $v_y = u_x$ |
| Idempotents / characteristics | $\Pi_\pm$ along $x \pm y$ | none; single characteristic $x$ |
| Solution class | $\phi(x+y)\Pi_1 + \psi(x-y)\Pi_2$ | $u(x) + (yu'(x) + c(x))\varepsilon$ |
| Data on the real line | two functions, transported | two functions, one differentiated |
| Algebra-valued Laplacian | $\Box = \partial_x^2 - \partial_y^2$, factors | $\Box = \partial_x^2$, does not factor |
| Euclidean Laplacian | $\partial_x^2 + \partial_y^2$ factors | $\partial_x^2 + \partial_y^2$ does not factor |

Two features of the comparison stand out. First, the split-complex analysis reduces to the two characteristics $x + y$ and $x - y$, while the dual analysis reduces to the single characteristic $x$ with the transverse dependence polynomial of degree one; the parabolic direction is the coincidence limit of the two hyperbolic characteristics. Second, the split-complex algebra-valued Laplacian $\partial_x^2 - \partial_y^2$ factors as $(\partial_x + j\partial_y)(\partial_x - j\partial_y)$, because $j^2 = +1$ cancels the sign in the product; the dual operator $\partial_x^2$ does not factor, because $\varepsilon^2 = 0$ leaves no trace of the transverse second derivative. In both cases the Euclidean Laplacian $\partial_x^2 + \partial_y^2$ is the unaugmented second-order operator that sees the whole plane.

## Summary

The two distinguished submodules of the dual numbers, the real submodule $R_{\mathbb{D}'}$ with coordinate operator $\partial_x$ and the infinitesimal submodule $\varepsilon R_{\mathbb{D}'} = \mathfrak{m}$ with coordinate operator $\partial_y$, carry the analysis of the dual plane. The algebra is identified with $\mathbb{R}^2$ by $Z = x + y\varepsilon$, and the three coordinate operators $\partial_x, \partial_y$ and multiplication $M_\varepsilon$ commute, with $M_\varepsilon^2 = 0$; multiplication by $\varepsilon$ projects onto the maximal ideal and kills the real part. The Cauchy–Riemann operator is $\bar\partial = \partial_y - \varepsilon\partial_x$, with holomorphic operator $\partial_Z = \partial_x$; a function $f = u + v\varepsilon$ is dual holomorphic exactly when $u_y = 0$ and $v_y = u_x$, and the holomorphic functions are $f = u(x) + (yu'(x) + c(x))\varepsilon$ with derivative $f' = u' + (yu'' + c')\varepsilon$. The operator $\bar\partial$ splits into a scalar part $\partial_y$ and a nilpotent part $-\varepsilon\partial_x$, and multiplication by $\varepsilon$ annihilates the nilpotent part, leaving $\varepsilon\bar\partial = \varepsilon\partial_y$; the maximal ideal is the first-order neighbourhood of the real line, along which holomorphic functions are affine. The algebra-valued d'Alembertian is $\Box = \nabla\bar\nabla = \partial_x^2$ for $\nabla = \partial_x + \varepsilon\partial_y$, and it satisfies $\nabla^2 = 2\partial_x\nabla - \Box$; it does **not** factorise the Euclidean Laplacian $\partial_x^2 + \partial_y^2$, because $\varepsilon^2 = 0$ annihilates the transverse second derivative. The whole theory reduces to the real line and its first-order neighbourhood: a holomorphic function is two functions $u, c$ of $x$, its primitive is obtained by integrating them, and integration and differentiation commute with the reduction. The comparison with the split complex case shows the dual case as the contraction in which the characteristics $x \pm y$ coalesce to $x$ and the transported data become affine in the transverse coordinate, while the split-complex Laplacian $\partial_x^2 - \partial_y^2$ factorises and the dual $\partial_x^2$ does not.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}' = \mathbb{R}[\varepsilon]/(\varepsilon^2)$ | Dual-number algebra; $\varepsilon^2 = 0$ |
| $Z = x + y\varepsilon$ | General dual number in analysis coordinates |
| $x$ | Coordinate on the real submodule $R_{\mathbb{D}'}$ |
| $y$ | Coordinate on the infinitesimal submodule $\varepsilon R_{\mathbb{D}'}$ |
| $f = u + v\varepsilon$ | Dual-valued function, $u, v : U \to \mathbb{R}$ |
| $\partial_x, \partial_y$ | Coordinate partial derivatives |
| $M_\varepsilon$ | Multiplication by $\varepsilon$; $M_\varepsilon^2 = 0$ |
| $D_{\mathbb{R}} = \partial_x$, $D_{\mathfrak{m}} = \partial_y$ | Real and infinitesimal coordinate operators |
| $\operatorname{Re}, \operatorname{Inf}$ | Real-part and infinitesimal-part maps |
| $\mathfrak{m} = (\varepsilon)$ | Maximal ideal, first-order neighbourhood |
| $\bar\partial = \partial_y - \varepsilon\partial_x$ | Cauchy–Riemann operator |
| $\partial_Z = \partial_x$ | Holomorphic operator; $f' = \partial_Z f$ |
| $u_y = 0$, $v_y = u_x$ | Dual Cauchy–Riemann equations |
| $\nabla = \partial_x + \varepsilon\partial_y$, $\bar\nabla = \partial_x - \varepsilon\partial_y$ | Algebra-valued gradient and its conjugate |
| $\Box = \nabla\bar\nabla = \partial_x^2$ | Algebra-valued d'Alembertian |
| $\Delta = \partial_x^2 + \partial_y^2$ | Euclidean Laplacian, unfactorisable here |
| $\Pi_\pm = \tfrac{1}{2}(1 \pm j)$ | Split-complex idempotents, in the comparison |

## Further Reading

- Walter Rudin, *Real and Complex Analysis* (McGraw–Hill, New York, 3rd ed. 1987), for the Cauchy–Riemann equations and the Wirtinger operators in the complex case.
- Lars Hörmander, *An Introduction to Complex Analysis in Several Variables* (North-Holland, Amsterdam, 3rd ed. 1990), for the Cauchy–Riemann operator as a first-order elliptic operator and its factorisation of the Laplacian.
- Richard Delanghe, Frank Sommen and Vladimir Souček, *Clifford Algebra and Spinor-Valued Functions* (Kluwer, Dordrecht, 1992), for the Cauchy–Riemann operator of a Clifford algebra, its square, and the factorisation of the Laplacian, as the comparison theory.
- Garret Sobczyk, "The generalized Cauchy–Riemann operator and the factorization of the Laplacian", in *Clifford Algebras and Their Applications in Mathematical Physics* (Kluwer, Dordrecht, 1993), for the factorisation problem and its failure for degenerate forms.
- Andreas Griewank and Andrea Walther, *Evaluating Derivatives: Principles and Techniques of Algorithmic Differentiation* (SIAM, Philadelphia, 2008), for the dual-number computation of first derivatives and the first-order neighbourhood of a point.
- Vladimir V. Kisil, *Geometry of Möbius Transformations: Elliptic, Parabolic and Hyperbolic Actions of $SL(2,\mathbb{R})$* (Imperial College Press, London, 2012), for the elliptic–parabolic–hyperbolic trichotomy and the contraction of characteristics.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, Natick, 2003), for the norm forms and the degenerate limits of the number systems of the family.
