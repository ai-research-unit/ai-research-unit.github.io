
# __Split-Complex Analysis on Subspaces__

## Introduction

The differential calculus of the split-complex algebra $\mathbb{D}=\mathbb{R}[x]/(x^2-1)$ is governed by its two distinguished subspaces: the fixed line $\mathbb{R}_{\mathbb{D}}=\mathbb{R}\cdot1$ of the conjugation and its anti-fixed line $j\mathbb{R}_{\mathbb{D}}=\mathbb{R}\cdot j$, and, finer, the two idempotent lines $\mathbb{R}\Pi_\pm$ whose direct sum is the algebra. This article writes the Cauchy–Riemann operator of *Split Complex Analysis* on each of these subspaces, resolves it into its two components in the idempotent coordinates, and shows that the whole calculus reduces to ordinary calculus on the two copies of $\mathbb{R}$ that the idempotents exhibit. It is the two-dimensional analogue of the subspace calculus of *Biquaternion Analysis*, where the corresponding object is the biquaternionic Cauchy–Riemann operator restricted to a four-real-dimensional subspace; here the subspaces are one-dimensional and the reduction is complete.

The article owns the coordinate operators $\partial_x$ and $\partial_y$ together with their restrictions to the two subspaces, the split Cauchy–Riemann operator $\nabla=\partial_x+j\partial_y$ and its conjugate $\bar\nabla$, the Wirtinger derivatives $\partial/\partial Z$ and $\partial/\partial\bar Z$ written in idempotent coordinates, the resolution of the Cauchy–Riemann operator into its two idempotent components, the reduction of differentiability to differentiability in each idempotent coordinate, and the role of the zero-divisor directions in the theory. It assumes the calculus, the Cauchy–Riemann equations and the idempotent decomposition of *Split Complex Analysis*, the subspace list of *Split-Complex Subspaces*, the norm and its isotropy of *Split-Complex Norm and Invertibility*, and the classification of the null cone of *Split-Complex Zero Divisors*. No physics is invoked and no new result is claimed.

**Conventions.** The algebra is $\mathbb{D}=\mathbb{R}[x]/(x^2-1)$, with basis $1$, $j$, $j^2=+1$; a general element is $Z=x+jy$ with $x,y\in\mathbb{R}$, and in the idempotent basis $Z=Z_+\Pi_1+Z_-\Pi_2$ with $Z_\pm=x\pm y$ and $\Pi_\pm=\tfrac12(1\pm j)$. The real subspace is $\mathbb{R}_{\mathbb{D}}=\mathbb{R}\cdot1$, the split imaginary subspace is $j\mathbb{R}_{\mathbb{D}}=\mathbb{R}\cdot j$, and the idempotent lines are $\mathbb{R}\Pi_1$ and $\mathbb{R}\Pi_2$. The norm is $N(Z)=x^2-y^2$, vanishing exactly on the two null lines $\mathbb{R}\Pi_1$ and $\mathbb{R}\Pi_2$.

## The Two Subspaces and Their Coordinates

### The Eigenlines of the Conjugation

The conjugation $\bar Z=x-jy$ is the unique non-trivial involution of $\mathbb{D}$ (*Split-Complex Subspaces*), and it splits the algebra into its fixed line and its anti-fixed line,

$$
\mathbb{R}_{\mathbb{D}}=\{Z:\bar Z=Z\}=\mathbb{R}\cdot1, \qquad j\mathbb{R}_{\mathbb{D}}=\{Z:\bar Z=-Z\}=\mathbb{R}\cdot j, \qquad \mathbb{D}=\mathbb{R}_{\mathbb{D}}\oplus j\mathbb{R}_{\mathbb{D}} .
$$

Writing $Z_r=\tfrac12(Z+\bar Z)=x$ and $Z_i=\tfrac12 j^{-1}(Z-\bar Z)=y$ for the coordinates in this decomposition gives $Z=Z_r+jZ_i$. The two lines are the eigenspaces of the involution, for the eigenvalues $+1$ and $-1$; no other involution of the algebra is available, since the idempotent conjugation coincides with $\bar{\cdot}$.

### The Idempotent Coordinates

The idempotents $\Pi_\pm=\tfrac12(1\pm j)$ are orthogonal, $\Pi_1\Pi_2=0$, complete, $\Pi_1+\Pi_2=1$, and primitive (*Split-Complex Idempotents and Projections*); they give the finer decomposition into the two idempotent lines, with coordinates

$$
Z_+=x+y, \qquad Z_-=x-y, \qquad Z=Z_+\Pi_1+Z_-\Pi_2 .
$$

The two coordinate systems are related by the invertible $\mathbb{R}$-linear change of basis

$$
Z_+=Z_r+Z_i, \qquad Z_-=Z_r-Z_i, \qquad Z_r=\tfrac12\bigl(Z_++Z_-\bigr), \qquad Z_i=\tfrac12\bigl(Z_+-Z_-\bigr),
$$

which is the identity $\mathbb{D}=\mathbb{R}\Pi_1\oplus\mathbb{R}\Pi_2\cong\mathbb{R}\oplus\mathbb{R}$ read in the basis $\{1,j\}$.

**The two copies of $\mathbb{R}$.** In the idempotent basis the algebra is the direct product $\mathbb{D}=\mathbb{R}\Pi_1\oplus\mathbb{R}\Pi_2$ with $\mathbb{R}\Pi_\pm\cong\mathbb{R}$, and multiplication is componentwise, $(ZW)_\pm=Z_\pm W_\pm$. This is the algebraic fact behind every reduction below: the two idempotent coordinates are independent real variables, and a function of $Z$ is a pair of functions, one of each.

## Differential Operators on the Subspaces

### The Coordinate Operators

Let $f:U\to\mathbb{D}$ be a differentiable function on an open set $U\subseteq\mathbb{D}$, written $f(Z)=u(x,y)+jv(x,y)$ with real-valued $u$ and $v$. The two coordinate operators are

$$
\partial_x=\frac{\partial}{\partial x}, \qquad \partial_y=\frac{\partial}{\partial y},
$$

tangential to $\mathbb{R}_{\mathbb{D}}$ and to $j\mathbb{R}_{\mathbb{D}}$ respectively: $\partial_x$ differentiates along the fixed line, and $\partial_y$ along the anti-fixed line. On the real subspace $\mathbb{R}_{\mathbb{D}}$ the operator $\partial_y$ acts trivially, and on the split imaginary subspace $j\mathbb{R}_{\mathbb{D}}$ the operator $\partial_x$ does: each of the two one-dimensional subspaces carries a single first-order operator, the derivative along its own direction, and the calculus of the plane is the calculus of the pair.

**Partial derivatives act componentwise.** Since the basis elements $1$ and $j$ are constants,

$$
\partial_x f=u_x+jv_x, \qquad \partial_y f=u_y+jv_y, \qquad \partial_x\partial_y f=\partial_y\partial_x f,
$$

so the two operators commute and obey the ordinary rules of the differential calculus on each coefficient separately.

### The Split Cauchy–Riemann Operator

The split Cauchy–Riemann operator is

$$
\nabla=\partial_x+j\,\partial_y,
$$

with conjugate

$$
\bar\nabla=\partial_x-j\,\partial_y .
$$

For $f=u+jv$ the two operators read

$$
\nabla f=\bigl(u_x+v_y\bigr)+j\bigl(v_x+u_y\bigr), \qquad \bar\nabla f=\bigl(u_x-v_y\bigr)+j\bigl(v_x-u_y\bigr),
$$

so the equation $\bar\nabla f=0$ is the split Cauchy–Riemann system

$$
u_x=v_y, \qquad u_y=v_x,
$$

the $j^2=+1$ analogue of the complex system $u_x=v_y$, $u_y=-v_x$. The single sign that separates the two systems is the sign of the square of the imaginary unit, and it is the same sign that makes the norm of $\mathbb{D}$ indefinite.

### The D'Alembertian

The product of the two operators is the wave operator, the **d'Alembertian**:

$$
\nabla\bar\nabla=\bar\nabla\nabla=\partial_x^2-\partial_y^2=\Box .
$$

**Proof.** Expanding, $\nabla\bar\nabla=(\partial_x+j\partial_y)(\partial_x-j\partial_y)=\partial_x^2+j\partial_y\partial_x-j\partial_x\partial_y-j^2\partial_y^2$, the two mixed terms cancel because the coordinate operators commute, and $j^2=+1$ leaves $\partial_x^2-\partial_y^2$. The same computation gives $\bar\nabla\nabla$.

So every function in the kernel of either operator solves the two-variable wave equation, and the operator is not elliptic; this is the analytic face of the indefiniteness of the norm.

## The Cauchy–Riemann Operator in Idempotent Coordinates

### The Wirtinger Derivatives

The Wirtinger derivatives of *Split Complex Analysis* are

$$
\frac{\partial}{\partial Z}=\frac{1}{2}\Bigl(\partial_x+j\,\partial_y\Bigr)=\frac{1}{2}\nabla, \qquad \frac{\partial}{\partial\bar Z}=\frac{1}{2}\Bigl(\partial_x-j\,\partial_y\Bigr)=\frac{1}{2}\bar\nabla,
$$

and a differentiable function satisfies the split Cauchy–Riemann equations exactly when $\partial f/\partial\bar Z=0$, in which case $f'(Z)=\partial f/\partial Z$.

### The Operator in Idempotent Coordinates

**Theorem.** In the idempotent coordinates the Wirtinger derivatives are

$$
\frac{\partial}{\partial Z}=\Pi_1\frac{\partial}{\partial Z_+}+\Pi_2\frac{\partial}{\partial Z_-}, \qquad \frac{\partial}{\partial\bar Z}=\Pi_1\frac{\partial}{\partial Z_-}+\Pi_2\frac{\partial}{\partial Z_+}.
$$

**Proof.** With $\partial_{Z_+}=\tfrac12(\partial_x+\partial_y)$ and $\partial_{Z_-}=\tfrac12(\partial_x-\partial_y)$, substitute $\Pi_\pm=\tfrac12(1\pm j)$:

$$
\Pi_1\partial_{Z_+}+\Pi_2\partial_{Z_-}=\tfrac14\bigl[(1+j)(\partial_x+\partial_y)+(1-j)(\partial_x-\partial_y)\bigr]=\tfrac14\bigl[2\partial_x+2j\partial_y\bigr]=\tfrac12(\partial_x+j\partial_y)=\frac{\partial}{\partial Z},
$$

and the same computation with $j$ replaced by $-j$ gives the second identity.

### The Two Components

The Cauchy–Riemann operator is therefore the sum of two idempotent components,

$$
\frac{\partial}{\partial\bar Z}=\Pi_1\frac{\partial}{\partial Z_-}+\Pi_2\frac{\partial}{\partial Z_+},
$$

the $\Pi_1$-component $\Pi_1\,\partial_{Z_-}$ acting as the derivative in $Z_-$ and the $\Pi_2$-component $\Pi_2\,\partial_{Z_+}$ acting as the derivative in $Z_+$. The two components are mutually annihilating, $\Pi_1\Pi_2=0$, and they commute, since they act on distinct coordinates and the algebra is commutative; they are the images of the single operator $\bar\nabla$ under the two projections of $\mathbb{D}\cong\mathbb{R}\oplus\mathbb{R}$. The same splitting applied to $\partial/\partial Z$ gives the components $\Pi_1\partial_{Z_+}$ and $\Pi_2\partial_{Z_-}$.

### The Operators on the Idempotent Lines

Restricted to the idempotent line $\mathbb{R}\Pi_1=\{Z:Z_-=0\}$ the operator $\partial_{Z_+}$ is the derivative along the line; restricted to $\mathbb{R}\Pi_2=\{Z:Z_+=0\}$ the operator $\partial_{Z_-}$ is. Each idempotent line is a copy of $\mathbb{R}$, and one component of the Cauchy–Riemann operator differentiates along it: the component carried on $\mathbb{R}\Pi_2$ acts as $\partial_{Z_+}$ on $\mathbb{R}\Pi_1$, and the component carried on $\mathbb{R}\Pi_1$ acts as $\partial_{Z_-}$ on $\mathbb{R}\Pi_2$. The two components act on the two lines crosswise, which is the operator version of the mutual annihilation $\Pi_1\Pi_2=0$.

## The Kernel and the Reduction to the Two Copies of $\mathbb{R}$

**Theorem (fundamental theorem of the subspace calculus).** Write $f=f_+\Pi_1+f_-\Pi_2$ with $f_\pm$ real-valued. Then $f$ is split-complex differentiable, that is $\partial f/\partial\bar Z=0$, if and only if

$$
\frac{\partial f_+}{\partial Z_-}=0, \qquad \frac{\partial f_-}{\partial Z_+}=0,
$$

equivalently if and only if $f_+=f_+(Z_+)$ and $f_-=f_-(Z_-)$ are differentiable functions of the single real variables $Z_+$ and $Z_-$ respectively.

**Proof.** By the preceding theorem, applied to $f=f_+\Pi_1+f_-\Pi_2$ and using $\Pi_1^2=\Pi_1$, $\Pi_2^2=\Pi_2$, $\Pi_1\Pi_2=0$,

$$
\frac{\partial f}{\partial\bar Z}=\Pi_1\frac{\partial f}{\partial Z_-}+\Pi_2\frac{\partial f}{\partial Z_+}=\Bigl(\frac{\partial f_+}{\partial Z_-}\Bigr)\Pi_1+\Bigl(\frac{\partial f_-}{\partial Z_+}\Bigr)\Pi_2 .
$$

The two idempotents are linearly independent over $\mathbb{R}$, so the expression vanishes if and only if both coefficients do.

**Corollary (the derivative).** For such a function $f$,

$$
f'(Z)=\frac{\partial f}{\partial Z}=f_+'(Z_+)\,\Pi_1+f_-'(Z_-)\,\Pi_2,
$$

where $f_+'$ and $f_-'$ are the ordinary derivatives of the two one-variable functions.

**Proof.** With $\partial/\partial Z=\Pi_1\partial_{Z_+}+\Pi_2\partial_{Z_-}$, the same expansion gives $\partial f/\partial Z=(\partial_{Z_+}f_+)\Pi_1+(\partial_{Z_-}f_-)\Pi_2$, and by the theorem $f_+$ depends only on $Z_+$ and $f_-$ only on $Z_-$.

**Remark (the reduction).** The theorem is the exact statement that the analytic content of $\mathbb{D}$ is the analytic content of two independent copies of $\mathbb{R}$: the split-complex differentiable functions are the sum of two copies of the differentiable functions of one real variable, one attached to $Z_+$ and one to $Z_-$, with no interaction between them. In the complex case the two real components of a holomorphic function are tied together by the Cauchy–Riemann equations and form a single analytic object; here the two components are free, and this freedom is the same fact that removes the Cauchy integral formula and Liouville's theorem (*Split Complex Analysis*).

**Example.** For $f(Z)=Z=Z_+\Pi_1+Z_-\Pi_2$ one has $f_+=Z_+$ and $f_-=Z_-$, both conditions hold, and $f'=\Pi_1+\Pi_2=1$. For $g(Z)=\bar Z=Z_-\Pi_1+Z_+\Pi_2$ one has $g_+=Z_-$, so $\partial_{Z_-}g_+=1\neq0$ and $g$ is not split-complex differentiable. For $h(Z)=e^Z=e^{Z_+}\Pi_1+e^{Z_-}\Pi_2$ one has $h_+=e^{Z_+}$ and $h_-=e^{Z_-}$, so $h$ is differentiable with $h'=e^{Z_+}\Pi_1+e^{Z_-}\Pi_2=e^Z$.

## The Role of the Zero Divisors

The Cauchy–Riemann operator is not elliptic, and the failure is measured exactly by the zero divisors of the algebra.

**The principal symbol.** Replacing $\partial_x$ and $\partial_y$ by the frequency variables $\xi$ and $\eta$ gives the principal symbol of $\nabla$,

$$
\sigma(\xi,\eta)=\xi+j\,\eta, \qquad N\bigl(\sigma(\xi,\eta)\bigr)=\xi^2-\eta^2 .
$$

The operator is elliptic precisely when $\sigma(\xi,\eta)\neq0$ for every $(\xi,\eta)\neq(0,0)$, which would require the norm to be definite; it is not, and $N(\sigma)$ vanishes on the two directions $\xi=\pm\eta$. Those are spanned by $1+j$ and $1-j$, that is, by the zero-divisor lines $\mathbb{R}\Pi_1$ and $\mathbb{R}\Pi_2$ classified in *Split-Complex Zero Divisors*. So the characteristic variety of the Cauchy–Riemann operator is the null cone, and the zero divisors of the algebra are its characteristic directions.

**No smoothing.** Because the symbol vanishes on a cone, the operator is hyperbolic rather than elliptic and does not smooth: a solution of $\partial f/\partial\bar Z=0$ is an arbitrary pair of differentiable functions $f_+(Z_+)$ and $f_-(Z_-)$ and carries no more regularity than that. In the complex case the symbol $\xi+i\eta$ vanishes only at the origin, the operator is elliptic, and holomorphic functions are automatically real analytic; the loss of that automatic smoothing is the analytic cost of the indefinite norm.

**Constancy along the null directions.** By the fundamental theorem, $f$ is split-complex differentiable exactly when its idempotent components are constant along the null directions: the $\Pi_1$-component $f_+$ is constant along $\mathbb{R}\Pi_2$, and the $\Pi_2$-component $f_-$ is constant along $\mathbb{R}\Pi_1$. The two zero-divisor lines are therefore the directions of constancy of the differentiable functions, and motion of a point along the null direction of the complementary component does not change the analytic data. This is the operator-level counterpart of the two null lines being the boundary of the polar parametrisation (*Split-Complex Topology*) and of the failure of a single Cauchy integral formula (*Split Complex Analysis*).

**Contrast with the biquaternion case.** In the biquaternion algebra the same mechanism operates with a characteristic variety of real dimension $6$, the null cone of $\mathbb{B}$, instead of two lines; the principal symbol of the biquaternionic Cauchy–Riemann operator again fails to vanish on the isotropic directions, so the failure of ellipticity there is the higher-dimensional form of the failure here, and the reduction to copies of $\mathbb{R}$ has no biquaternion analogue.

## Comparison with the Complex and Biquaternion Cases

| feature | $\mathbb{C}$ | $\mathbb{D}$ | $\mathbb{B}$ |
|---|---|---|---|
| distinguished real subspaces | $2$: $\mathbb{R}_{\mathbb{C}}$, $i\mathbb{R}_{\mathbb{C}}$ | $2$: $\mathbb{R}_{\mathbb{D}}$, $j\mathbb{R}_{\mathbb{D}}$ | $4$: $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$, $\mathbb{M}_+$, $\mathbb{M}_-$ |
| Cauchy–Riemann operator | $\partial_x+i\partial_y$, elliptic | $\partial_x+j\partial_y$, hyperbolic | $\sum_\mu e_\mu\partial_\mu$, not elliptic |
| square of the operator | Laplacian, definite | d'Alembertian, indefinite | operator of real order $4$ |
| characteristic variety | $\{0\}$ | the two null lines | the null cone, real dimension $6$ |
| kernel of $\partial/\partial\bar Z$ | holomorphic functions | $f_+(Z_+)\Pi_1+f_-(Z_-)\Pi_2$ | biregular functions, obstructed |
| reduction to copies of $\mathbb{R}$ | none | two copies, one per idempotent | none |

The pattern is that in $\mathbb{D}$ the subspace calculus is not merely a restriction of the plane calculus but a complete resolution of it: the two real subspaces supply the two operators, the idempotent lines supply the two variables, and the Cauchy–Riemann operator is exactly the sum of the two one-variable derivatives. In $\mathbb{C}$ no such splitting exists, and in $\mathbb{B}$ the four subspaces do not resolve the operator, because the zeros of its symbol form a genuine cone rather than a pair of lines.

## Summary

The split-complex plane carries two distinguished one-dimensional real subspaces, the fixed line $\mathbb{R}_{\mathbb{D}}$ and the anti-fixed line $j\mathbb{R}_{\mathbb{D}}$ of the unique non-trivial involution, with coordinate operators $\partial_x$ and $\partial_y$; the first acts on the fixed line and the second on the anti-fixed line, and the split Cauchy–Riemann operator is $\nabla=\partial_x+j\partial_y$, whose square is the d'Alembertian $\Box=\partial_x^2-\partial_y^2$. In the idempotent basis $\Pi_\pm=\tfrac12(1\pm j)$ the Wirtinger derivatives become $\partial/\partial Z=\Pi_1\partial_{Z_+}+\Pi_2\partial_{Z_-}$ and $\partial/\partial\bar Z=\Pi_1\partial_{Z_-}+\Pi_2\partial_{Z_+}$, so the Cauchy–Riemann operator is the sum of two mutually annihilating idempotent components, one differentiating in each idempotent coordinate.

The kernel of the Cauchy–Riemann operator consists exactly of the functions $f=f_+(Z_+)\Pi_1+f_-(Z_-)\Pi_2$ with $f_\pm$ differentiable functions of the single real variable $Z_\pm$, and the derivative acts as $f'=f_+'(Z_+)\Pi_1+f_-'(Z_-)\Pi_2$. This is the complete reduction of the analysis to the two copies of $\mathbb{R}$ that the idempotents exhibit. The operator is not elliptic: the norm of its principal symbol is the norm $\xi^2-\eta^2$, which vanishes on the two null directions, so the characteristic variety is the zero-divisor set, the components of a differentiable function are constant along the null directions, and there is no automatic smoothing. Compared with $\mathbb{C}$, where the operator is elliptic and the two components are tied together, and with $\mathbb{B}$, where the characteristic variety is a six-dimensional cone, the split-complex case is the exact middle: a complete resolution into two one-variable calculi, with the zero divisors marking the directions that the operator does not see.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{D}=\mathbb{R}[x]/(x^2-1)$ | Split complex algebra; basis $1$, $j$, $j^2=+1$ |
| $Z=x+jy$ | General split complex number |
| $Z=Z_+\Pi_1+Z_-\Pi_2$ | Idempotent coordinates, $Z_\pm=x\pm y$ |
| $\Pi_\pm=\tfrac12(1\pm j)$ | Idempotents, orthogonal and complete |
| $\mathbb{R}_{\mathbb{D}}=\mathbb{R}\cdot1$ | Real subspace, fixed line of the conjugation |
| $j\mathbb{R}_{\mathbb{D}}=\mathbb{R}\cdot j$ | Split imaginary subspace, anti-fixed line |
| $\mathbb{R}\Pi_1$, $\mathbb{R}\Pi_2$ | The two idempotent lines, the null lines |
| $Z_r=x$, $Z_i=y$ | Eigenline coordinates |
| $\partial_x$, $\partial_y$ | Coordinate operators along the two subspaces |
| $\nabla=\partial_x+j\partial_y$ | Split Cauchy–Riemann operator |
| $\bar\nabla=\partial_x-j\partial_y$ | Conjugate Cauchy–Riemann operator |
| $\Box=\partial_x^2-\partial_y^2$ | D'Alembertian; $\nabla\bar\nabla=\bar\nabla\nabla=\Box$ |
| $\partial/\partial Z$, $\partial/\partial\bar Z$ | Wirtinger derivatives, $=\tfrac12\nabla$, $\tfrac12\bar\nabla$ |
| $\partial_{Z_\pm}$ | Derivative in the idempotent coordinate $Z_\pm$ |
| $\sigma(\xi,\eta)=\xi+j\eta$ | Principal symbol; $N(\sigma)=\xi^2-\eta^2$ |
| $f=f_+\Pi_1+f_-\Pi_2$ | Idempotent decomposition of a function |

## Further Reading

- F. Brackx, R. Delanghe and F. Sommen, *Clifford Analysis* (Pitman, Research Notes in Mathematics 76, 1982), for the Cauchy–Riemann operator of a hypercomplex algebra and its relation to harmonic and wave equations.
- R. Delanghe, F. Sommen and V. Souček, *Clifford Algebra and Spinor-Valued Functions* (Kluwer, Mathematics and its Applications 53, 1992), for the principal symbol, the characteristic variety and the failure of ellipticity of the hypercomplex Cauchy–Riemann operator.
- Lars Hörmander, *The Analysis of Linear Partial Differential Operators I* (Springer, Grundlehren der mathematischen Wissenschaften 256, 2nd ed. 1990), for the principal symbol, ellipticity, hyperbolicity and the characteristic variety.
- Gerald B. Folland, *Introduction to Partial Differential Equations* (Princeton University Press, 2nd ed. 1995), for the d'Alembertian, its characteristics and the general solution of the one-dimensional wave equation.
- Isaak Yaglom, *Complex Numbers in Geometry* (Academic Press, 1968), for the split complex plane, its idempotent coordinates and its two null directions.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the algebra $\mathrm{Cl}(1,1)$, its isotropic lines and the split complex structure.
- A. Sudbery, *Quaternionic Analysis* (Mathematical Proceedings of the Cambridge Philosophical Society 85, 1979), for the factorization of second-order operators by first-order hypercomplex operators.
