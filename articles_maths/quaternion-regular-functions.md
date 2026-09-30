
# __Quaternion Regular Functions__

## Introduction

Quaternion analysis, in the sense of one complex variable generalised to four real variables, is built on a first-order operator and the class of functions it annihilates. This article defines that operator and its conjugate, states the system of equations that regularity imposes, proves the harmonicity of regular functions through the factorization of the Laplacian, records the examples that generated the classical theory, and gives the Cauchy integral formula that holds on the quaternion algebra. It is the quaternion member of the family's regularity pair; its counterpart is the biquaternion case, where the algebra is no longer a division algebra and the null cone obstructs the complex analogy. Here the algebra is a division algebra, there is no null cone, and the analogy holds without restriction.

The article uses *Quaternion Algebra* and *Quaternion Norm and Invertibility* for the algebra, the quaternion norm and the inverse, *The Scalar and Vector Subspaces of $\mathbb{H}$* for the vector-calculus decomposition of the operator, *Quaternion Integration* for the Cauchy integral formula and its consequences, and *Quaternion Special Functions* for the exponential that generates the examples. It is adjacent to *Fueter Theory for Quaternions*, which owns the Fueter construction and the axial and slice approach; this article owns the operator and the system it defines. The classical one-variable model is compared throughout; no physical vocabulary is used, and the first-order operator is the **Cauchy–Riemann operator** of the menu (some older literature calls it the Dirac operator, a name not used in this corpus).

The corpus's default base is a commutative ring with identity; the analysis requires the real numbers, so the operator is defined over $\mathbb{R}$ and the results are stated for domains in $\mathbb{R}^4$. A separate section treats the three-dimensional theory of the **reduced quaternions** $\mathcal{A} = \operatorname{span}_\mathbb{R}\{e_0,e_1,e_2\}$, a real vector space that is not a subalgebra, whose operator is the reduced Cauchy–Riemann operator of the Riesz system; because that module is a subspace of codimension one, its left and right regularity coincide and the theory is two-sided.

Throughout, $\mathbb{H}$ is the quaternion algebra over $\mathbb{R}$ with basis $e_0 = 1, e_1, e_2, e_3$, $e_k^2 = -e_0$; the variable is $x = x_0+x_1e_1+x_2e_2+x_3e_3$ with $x_\mu\in\mathbb{R}$; the conjugate is $\bar x = x_0-\mathbf{x}$ and the modulus is $|x| = \sqrt{N(x)}$. The partial derivatives are $\partial_\mu = \partial/\partial x_\mu$, and the Euclidean Laplacian is $\Delta = \sum_\mu \partial_\mu^2$. The vector operations on $\mathbf{f} = f_1e_1+f_2e_2+f_3e_3$ are $\mathrm{div}\,\mathbf{f} = \sum_k\partial_kf_k$, $\mathrm{grad}\,f_0 = \sum_k(\partial_kf_0)e_k$, and $\mathrm{rot}\,\mathbf{f} = \sum_{j,k,l}\epsilon_{jkl}(\partial_jf_k)e_l$.

## The Cauchy–Riemann Operator and Its Conjugate

**Definition.** The **Cauchy–Riemann operator** on $\mathbb{H}$ and its **quaternion conjugate** are

$$
D = \sum_{\mu=0}^{3}e_\mu\partial_\mu = \partial_0+e_1\partial_1+e_2\partial_2+e_3\partial_3, \qquad
\bar D = \sum_{\mu=0}^{3}\bar e_\mu\partial_\mu = \partial_0-e_1\partial_1-e_2\partial_2-e_3\partial_3,
$$

with $\bar e_0 = e_0$ and $\bar e_k = -e_k$; the bar conjugates the basis elements, not the derivatives.

**Proposition.** The units satisfy the Clifford relation $e_\mu\bar e_\nu+e_\nu\bar e_\mu = 2\delta_{\mu\nu}e_0$, and consequently

$$
D\bar D = \bar D D = \Delta,
$$

so the Cauchy–Riemann operator factors the Laplacian, exactly as $\partial_z\partial_{\bar z} = \tfrac14\Delta$ in one complex variable.

*Proof.* For $\mu = \nu$ one has $e_\mu\bar e_\mu = e_0$, since $e_0\bar e_0 = e_0$ and $e_k\bar e_k = -e_k^2 = e_0$; for $\mu\neq\nu$, $e_\mu\bar e_\nu = -e_\mu e_\nu = e_\nu e_\mu = -e_\nu\bar e_\mu$. Hence all mixed second derivatives cancel in the product, leaving $\sum_\mu\partial_\mu^2 = \Delta$.

**Remark.** The pair $(D,\bar D)$ plays the role of $(\partial_z,\partial_{\bar z})$, but the two operators are not merely the two first-order factors of the Laplacian: because the algebra is non-commutative, the products $D\bar D$ and $\bar D D$ agree as differential operators on the algebra but the operators themselves act on functions by left multiplication and are not interchangeable with right multiplication by a quaternion.

## Regular Functions

**Definition.** Let $\Omega\subseteq\mathbb{H}$ be a domain and $f : \Omega\to\mathbb{H}$ continuously differentiable. Then $f$ is **left-regular**, or **left-monogenic**, if

$$
Df = \sum_{\mu=0}^{3}e_\mu\partial_\mu f = 0
$$

on $\Omega$. It is **right-regular** if $fD := \sum_\mu\partial_\mu f\,e_\mu = 0$, and it is **anti-regular** if $\bar D f = 0$.

**Convention.** In this article and its companions, **regular** without qualification means **left-regular**, $Df = 0$. The opposite convention $\bar Df = 0$ also occurs in the literature and merely interchanges the regular and anti-regular classes.

**Proposition.** Quaternion conjugation exchanges the two regularity conventions: $f$ is left-regular if and only if $\bar f$ is right-regular with respect to the conjugate operator,

$$
Df = 0\iff\bar f\,\bar D = 0,
$$

and $f$ is right-regular if and only if $\bar f$ is anti-regular, $fD = 0\iff\bar D\bar f = 0$.

*Proof.* Conjugation is an anti-automorphism, so it reverses the order of the factors in each term: $\overline{Df} = \sum_\mu(\partial_\mu\bar f)\bar e_\mu = \bar f\bar D$ and $\overline{fD} = \sum_\mu\bar e_\mu\partial_\mu\bar f = \bar D\bar f$. A quaternion vanishes exactly when its conjugate does.

## The System of Regularity Equations

**Theorem.** Writing $f = f_0+\mathbf{f}$ with $\mathbf{f} = f_1e_1+f_2e_2+f_3e_3$, the operator decomposes as

$$
Df = \bigl(\partial_0f_0-\mathrm{div}\,\mathbf{f}\bigr) + \bigl(\partial_0\mathbf{f}+\mathrm{grad}\,f_0+\mathrm{rot}\,\mathbf{f}\bigr),
$$

so $f$ is left-regular if and only if it solves the **Cauchy–Riemann–Fueter system**

$$
\partial_0f_0 = \mathrm{div}\,\mathbf{f}, \qquad \partial_0\mathbf{f}+\mathrm{grad}\,f_0+\mathrm{rot}\,\mathbf{f} = 0 .
$$

*Proof.* Multiply out $e_\mu\partial_\mu(f_0+\mathbf{f})$ term by term, using $\mathbf{a}\mathbf{b} = -\langle\mathbf{a},\mathbf{b}\rangle+\mathbf{a}\times\mathbf{b}$ for pure quaternions: the scalar part collects $\partial_0f_0-\mathrm{div}\,\mathbf{f}$, and the vector part collects $\partial_0\mathbf{f}+\mathrm{grad}\,f_0+\mathrm{rot}\,\mathbf{f}$. Both parts must vanish.

**Corollary.** The system is a first-order elliptic system of four equations for the four coefficients. Its principal symbol is $s(\xi) = \sum_\mu\xi_\mu e_\mu$, which satisfies $s(\xi)\bar s(\xi) = |\xi|^2e_0$ for every real covector $\xi\neq0$, so the system is elliptic and its solutions are real-analytic.

*Proof.* The principal symbol is invertible with inverse $\bar s(\xi)/|\xi|^2$, which is the ellipticity condition; elliptic systems with smooth coefficients have real-analytic solutions.

**Remark.** The ellipticity is exact, and it is the point at which the quaternion algebra differs from the biquaternion algebra: for the quaternion algebra the quaternion norm is definite, so $|\xi|^2$ never vanishes, and the operator has no characteristic set. There is therefore no analogue of the null cone of $\mathbb{B}$.

## Examples and Closure Properties

**Theorem.** Every constant function is regular; the coordinate function $x$ is not regular, since $Dx = \sum_\mu e_\mu e_\mu = -2e_0$; the Cauchy kernel

$$
G(x) = \frac{\bar x}{|x|^4}
$$

is regular on $\mathbb{H}\setminus\{0\}$; and every classical holomorphic function of the single complex variable $z = x_0+e_1x_1$, extended by constancy in $x_2,x_3$, is regular.

*Proof.* The constants have vanishing derivatives; the identity gives $Dx = e_0-3e_0 = -2e_0$; the kernel is checked by differentiation, the homogeneity of $G$ in four real variables being $1-4 = -3$, so that $G$ is the fundamental solution; and the single-plane statement follows because on functions independent of $x_2,x_3$ the operator reduces to $Df = 2\partial_{\bar z}f$ with $\partial_{\bar z} = \tfrac12(\partial_0+e_1\partial_1)$.

**Proposition (closure).** Regular functions are closed under addition, under right multiplication by constant quaternions, and under left multiplication by real scalars; they are **not** closed under left multiplication by a general quaternion constant. Hence they form a right $\mathbb{H}$-module but not a left one.

*Proof.* Additivity is clear; for a constant $c$, $D(fc) = (Df)c = 0$ while $D(cf) = \sum_\mu e_\mu c\,\partial_\mu f$ need not vanish, as $D(e_2z) = e_2+e_1e_2e_1 = 2e_2\neq0$ shows.

**Remark.** The failure of left multiplication exhibits the non-commutativity directly: the coordinate $z = x_0+e_1x_1$ is regular and $z^2$ is regular, but the reversed products are not, and the single-plane holomorphic functions are the largest class of regular functions obtained from one complex direction. The Cauchy kernel is regular but is not holomorphic in any single-plane variable, so the hypercomplex class is strictly larger than the single-plane class; the two coincide only in two real dimensions.

## Harmonicity and the Factorization of the Laplacian

**Theorem.** Every left-regular function is harmonic,

$$
Df = 0 \implies \Delta f = \bar D(Df) = 0,
$$

and every right-regular function is harmonic as well; the harmonic functions form a strictly larger class, since the coordinate $x_0$ is harmonic but $Dx_0 = e_0\neq0$.

*Proof.* By the factorization $\bar DD = \Delta$, a left-regular $f$ satisfies $\Delta f = \bar D(Df) = 0$; for right-regularity one uses $D\bar D = \Delta$ on the left factor. The coordinate $x_0$ is annihilated by the Laplacian and not by $D$.

**Corollary.** Each coefficient $f_\nu$ of a regular function solves the four-dimensional Laplace equation $\sum_\mu\partial_\mu^2f_\nu = 0$, so regular functions are real-analytic and satisfy the mean value property; the converse fails, so regularity is strictly stronger than harmonicity.

*Proof.* The Laplacian acts componentwise, and the factorization shows the coefficients are harmonic; strictness is the coordinate example. The mean value property and real-analyticity of harmonic functions are standard.

## The Three-Dimensional Operator and the Logarithmic Derivative

The operator $D$ of this article is four-dimensional, and its square is not the Laplacian: with $D_3 = e_1\partial_1+e_2\partial_2+e_3\partial_3$ the spatial part and $D = \partial_0+D_3$, one has $D^2 = \partial_0^2+2\partial_0D_3-\Delta_3$, which is not scalar because of the mixed term $2\partial_0D_3$. It is the *conjugate* that removes that term, $D\bar D = \Delta$. The spatial part alone is a classical operator with a function theory of its own, and it is the operator on which the three-dimensional Riccati theory is built.

**Definition.** The **Moisil–Theodoresco operator**, or three-dimensional Cauchy–Riemann operator, is

$$
D_3 = e_1\partial_1+e_2\partial_2+e_3\partial_3 .
$$

It agrees with $D$ on functions independent of $x_0$, but its kernel is larger: $D_3f = 0$ does not imply $Df = 0$, since $D = \partial_0+D_3$.

**Proposition (the split and the square).** For a differentiable $g$ on a domain of $\mathbb{R}^3$,

$$
D_3g = -\mathrm{div}\mathbf{g}+\mathrm{grad}g_0+\mathrm{rot}\mathbf{g},
$$

so that $D_3\phi = \mathrm{grad}\phi$ on a scalar; and $D_3^2 = -\Delta_3$, the cross terms cancelling because $\partial_j\partial_k$ is symmetric while $e_je_k$ is antisymmetric for $j\neq k$.

*Proof.* The split is the three-dimensional case of the computation of the section above, with the $\partial_0$ terms removed. For the square, the $j=k$ terms give $\sum_ke_k^2\partial_k^2 = -\Delta_3$ and the $j\neq k$ terms pair as $(e_je_k+e_ke_j)\partial_j\partial_k = 0$.

**Remark (why the dimension matters).** The four-dimensional operator needs its conjugate to factor the Laplacian, and the square shows why: the mixed terms $2\partial_0D_3$ that the conjugate cancels are exactly those the fourth coordinate contributes. In three dimensions there is no such term, $D_3$ factorises the Laplacian alone, and the operator is elliptic with symbol $s(\xi) = \xi_1e_1+\xi_2e_2+\xi_3e_3$, whose square is $-|\xi|^2$.

**Definition (the logarithmic derivative).** For a scalar $\phi$ that does not vanish, the **logarithmic derivative** of Marchenko is

$$
\check\partial\phi = \phi^{-1}D_3\phi,
$$

a vector-valued function, and it is logarithmic: $\check\partial(\phi_1\phi_2) = \check\partial\phi_1+\check\partial\phi_2$. That identity is the Leibniz rule $D_3(\phi g) = D_3(\phi)g+\phi D_3g$ for a scalar left factor, and the same scalar hypothesis governs the factorisation below.

**Proposition (the Riccati PDE).** A non-vanishing scalar $\phi$ solves the three-dimensional Schrödinger equation $\Delta_3\phi+v\phi = 0$ if and only if $\mathbf{f} = \check\partial\phi$ solves

$$
D_3\mathbf{f}+\mathbf{f}^2 = v .
$$

*Proof.* With $\mathbf{f} = \phi^{-1}\nabla\phi$, the curl vanishes, $\mathrm{rot}\mathbf{f} = \nabla(\phi^{-1})\times\nabla\phi = 0$, so $D_3\mathbf{f} = -\mathrm{div}\mathbf{f}$, and the quadratic term $\mathbf{f}^2 = -\lvert\mathbf{f}\rvert^2$ cancels the second term of the divergence, leaving $D_3\mathbf{f}+\mathbf{f}^2 = -\phi^{-1}\Delta\phi$.

**Remark (the factorisation).** The Schrödinger operator factorises through $D_3$: with $M_{\mathbf{f}}$ the operator of right multiplication by $\mathbf{f}$, one has $-\Delta_3-vI = (D_3+M_{\mathbf{f}})(D_3-M_{\mathbf{f}})$ if and only if $\mathbf{f}$ solves the Riccati PDE, and the identity holds on a scalar right factor. On a general quaternion-valued argument the product differs from $-\Delta_3-v$ by $\sum_ke_k[\psi,\partial_k\mathbf{f}]$: the non-commutativity that separates this theory from the classical one appears here as an explicit defect term.

**Remark.** The equation itself, its one-dimensional reduction and the generalised Euler theorems belong to *Integrable Systems*; the operator, its square and the logarithmic derivative that make the lift possible belong here.

## The Vectorial Coefficient and the Componentwise Reduction

The coefficient of the previous section is a gradient, $\mathbf{f} = \check\partial\phi$, and that is what makes the Riccati PDE and a single *scalar* Schrödinger equation available. The other case is the first-order equation

$$
D_3f+f\vec\alpha = 0,
\qquad
\vec\alpha = \alpha_1e_1+\alpha_2e_2+\alpha_3e_3 ,
$$

with an arbitrary vector-valued coefficient on the **right**. The side is not a convention: the identity below is a right-multiplication statement, and the left-hand equation $D_3f+\vec\alpha f = 0$ is the regular equation conjugated by division by a scalar, by the carrier identity of *Electromagnetism in Media*, so only the right-hand form carries the Schrödinger connection. The equation is not artificial — several first-order systems of the physics corpus reduce to it, and that reading, with the dictionary of coefficients, is in the physics articles. Only the static Maxwell member forces $\vec\alpha$ to be a gradient, so the Riccati theory of the previous section covers that member and not the others.

**The scalar-carrier identity, without the gradient hypothesis.** The identity behind the Riccati section needs only the right factor to be **scalar**, not the coefficient to be a gradient: for any vector-valued $\vec\beta$ and any scalar $u$,

$$
(D_3+M_{\vec\beta})(D_3-M_{\vec\beta})u = -\Delta_3u-(D_3\vec\beta)u-\vec\beta^2u .
$$

*Proof.* Since $u$ is scalar, $D_3(u\vec\beta) = (D_3u)\vec\beta+u\,D_3\vec\beta$; therefore $(D_3+M_{\vec\beta})(D_3-M_{\vec\beta})u = D_3(D_3u-u\vec\beta)+(D_3u-u\vec\beta)\vec\beta = -\Delta_3u-u\,D_3\vec\beta-u\vec\beta^2$, the mixed terms cancelling. The Riccati PDE $D_3\mathbf{f}+\mathbf{f}^2 = v$ is thus the statement that the bracket $-D_3\vec\beta-\vec\beta^2$ is a *prescribed* scalar, which is what $\vec\beta = \check\partial\phi$ achieves and a general $\vec\beta$ does not.

**Proposition (componentwise reduction to four scalar Schrödinger operators).** Let the coefficient be **separated**, $\vec\alpha = \alpha_1(x_1)e_1+\alpha_2(x_2)e_2+\alpha_3(x_3)e_3$, each $\alpha_k$ a function of its own variable alone, and let $u = \sum_ku_ke_k$. Put $\vec\alpha^{(0)} = \vec\alpha$ and, for $k = 1,2,3$,

$$
\vec\alpha^{(k)} = \alpha_ke_k-\sum_{j\neq k}\alpha_je_j = -e_k\vec\alpha e_k ,
$$

the coefficient with the two components other than $k$ **reversed**. Then

$$
(D_3+M_{\vec\alpha})(D_3-M_{\vec\alpha})u = \sum_{k=0}^{3}e_k\left(-\Delta_3u_k-\vec\alpha^2u_k-(D_3\vec\alpha^{(k)})u_k\right),
$$

and each $D_3\vec\alpha^{(k)}$ is a **scalar**.

*Proof.* Expanding, $(D_3+M_{\vec\alpha})(D_3-M_{\vec\alpha})u = -\Delta_3u-\sum_je_ju\,\partial_j\vec\alpha-u\vec\alpha^2$. Separatedness gives $\partial_j\vec\alpha = e_j\partial_j\alpha_j$, so $\sum_je_je_k\partial_j\vec\alpha = \sum_je_je_ke_j\partial_j\alpha_j$; since $e_je_ke_j = -e_k$ when $j = k$ and $e_je_ke_j = e_k$ otherwise, this is $e_kD_3\vec\alpha^{(k)}$ for $k\ge1$, and for $k = 0$ it is $-e_0\sum_j\partial_j\alpha_j = e_0D_3\vec\alpha$, which is the same display because $\vec\alpha^{(0)} = \vec\alpha$. Scalarity: separatedness gives $D_3\vec\alpha^{(k)} = -\partial_k\alpha_k+\sum_{j\ne k}\partial_j\alpha_j$ for $k\ge1$ and $D_3\vec\alpha = -\sum_j\partial_j\alpha_j$, all scalar.

**The case $k = 0$ is the identity, not the reversal.** With $\vec\alpha^{(0)} = -\vec\alpha$ in place of $\vec\alpha^{(0)} = \vec\alpha$ the display fails by the residual $2(D_3\vec\alpha)u_0$. The same care is needed with the source's involution, which is printed for the components $e_1,e_2,e_3$ of the projected equations; the $e_0$-component carries the coefficient itself.

**Two consequences.** If $f$ solves $D_3f+f\vec\alpha = 0$, then applying $D_3-M_{\vec\alpha}$ and reading the display with $\vec\alpha$ replaced by $-\vec\alpha$ gives

$$
(-\Delta_3+w_k)f_k = 0,
\qquad
w_k = D_3\vec\alpha^{(k)}-\vec\alpha^2 ,
$$

so the four components of any solution solve four *scalar* Schrödinger equations. Conversely, if scalar functions $g_k$ solve $(-\Delta_3+v_k)g_k = 0$ with

$$
v_k = -D_3\vec\alpha^{(k)}-\vec\alpha^2 ,
$$

then $f = (D_3-M_{\vec\alpha})g$ with $g = \sum_kg_ke_k$ solves $D_3f+f\vec\alpha = 0$. The first-order equation therefore inherits the theory of the four scalar operators — fundamental solutions, solvability, boundary values — and the map $g\mapsto(D_3-M_{\vec\alpha})g$ is the way back. It is the exact analogue of the previous section's construction $\mathbf{f} = \check\partial\phi$, with four potentials and four carriers in place of the single one.

**The worked example.** The simplest separated coefficient is $\vec\alpha = \sum_k(x_k-b_k)^{-1}e_k$, a shifted coordinate reciprocal in each direction, with the $b_k$ constants. Then $\partial_k\alpha_k = -\alpha_k^2$ gives $D_3\vec\alpha = -\sum_j\partial_j\alpha_j = \sum_j\alpha_j^2 = -\vec\alpha^2$, so the four potentials are

$$
v_0 = 0,
\qquad
v_k = 2\sum_{j\neq k}\alpha_j^2 = 2\sum_{j\neq k}\frac{1}{(x_j-b_j)^2}\quad(k\ge1),
$$

and the corresponding solutions of the four scalar equations are $\phi_0 = \prod_j(x_j-b_j)$ for the harmonic case $v_0 = 0$ and $\phi_k = (x_k-b_k)\prod_{j\ne k}(x_j-b_j)^{-1}$; the negatives of the reciprocals, $f_k = 1/\phi_k$, assemble into $f = \sum_kc_kf_ke_k$, which solves $D_3f+f\vec\alpha = 0$ for any constants $c_k$. The example is the smallest one that exercises all four of the potentials, and it shows the case $v_0 = 0$: the $e_0$-component of the reduction is the Laplace equation, as it must be, since $\phi_0$ is a product of one linear factor in each variable and is harmonic.

**Separation is sufficient, not necessary, and the exact condition is a Jacobian condition.** The proof used $\partial_j\vec\alpha = e_j\partial_j\alpha_j$, which *is* separation, and the display holds for a general vector-valued coefficient exactly when the symmetric part of its Jacobian vanishes,

$$
\partial_j\alpha_k+\partial_k\alpha_j = 0 \qquad (j\neq k),
$$

separated coefficients being the case of a diagonal Jacobian. The class is strictly larger: the rigid-rotation-like $\vec\alpha = x_2e_1-x_1e_2$ satisfies the condition without being separated, and the display is still exact for it. What separation alone supplies is the **scalarity** of the four brackets, and with it the reading as four scalar equations; for a coefficient in the larger class whose $D_3\vec\alpha^{(k)}$ is not scalar the display holds but no longer separates into four scalar problems. Both statements were checked symbolically on a generic vector-valued coefficient: the difference vanishes identically exactly under the three conditions above.

**The projection device.** The idempotents

$$
P^\pm_k = \tfrac12M_{(1\pm ie_k)},
\qquad
(P^\pm_k)^2 = P^\pm_k,
\qquad
P^+_k+P^-_k = I,
\qquad
P^+_kP^-_k = 0,
$$

act on the right and diagonalise a *scalar* shift: for any function $\nu$,

$$
P^\pm_k\,(D_3+M_{\nu}) = \bigl(D_3 \pm M_{i\nu e_k}\bigr)P^\pm_k .
$$

So an equation whose coefficient is a scalar multiple of one basis vector splits into two equations whose coefficients differ in sign, and a coefficient that is a sum of two independent shifts splits into four. The device is algebraic, not analytic: it is the idempotent pair $\tfrac12(1\pm ie_k)$ that the mass-shell section of *The Dirac Equation in Biquaternionic Form* uses with a biquaternionic parameter, and the same pair, written without normalisation, that the stratified case of *Maxwell's Equations in Chiral Media* uses. The identity above is the statement that the projection commutes with the shifted operator up to the reversal of the shift, and it was checked symbolically for both signs and all three $k$.

## The Reduced-Quaternion Module and the Riesz System

The operator of the previous section acts on the three imaginary directions of $\mathbb{H}$. A second three-dimensional theory is obtained from the opposite choice of coordinates, one real direction and two imaginary ones, and it is the theory on which the constructive approximation of the ball in $\mathbb{R}^3$ is built. Its coefficients lie in the **reduced quaternions**

$$
\mathcal{A} = \operatorname{span}_\mathbb{R}\{e_0,e_1,e_2\} = \{f_0+f_1e_1+f_2e_2 : f_0,f_1,f_2\in\mathbb{R}\},
$$

and the decisive feature is that $\mathcal{A}$ is a three-dimensional real vector space but **not** a subalgebra of $\mathbb{H}$: the product $e_1e_2 = e_3$ leaves it. The subspace is closed under conjugation and under inversion in $\mathbb{H}$, since $\bar f = f_0-f_1e_1-f_2e_2\in\mathcal{A}$ and $f^{-1} = \bar f/(f_0^2+f_1^2+f_2^2)\in\mathcal{A}$ for $f\neq 0$, and the product of two of its elements falls back into it exactly when their vector parts are parallel. The failure of closure is the source of what is distinctive in the theory.

**Definition (reduced Cauchy–Riemann operator).** On $\mathcal{A}$-valued functions of $x = x_0+x_1e_1+x_2e_2$ in a domain of $\mathbb{R}^3$, the **reduced Cauchy–Riemann operator** and its conjugate are

$$
D = \partial_0+e_1\partial_1+e_2\partial_2, \qquad \bar D = \partial_0-e_1\partial_1-e_2\partial_2 .
$$

**Proposition.** $D\bar D = \bar DD = \Delta_3 = \partial_0^2+\partial_1^2+\partial_2^2$, so the two operators factor the Laplacian of $\mathbb{R}^3$ and every monogenic function is harmonic in each component.

*Proof.* As in four variables, $e_\mu\bar e_\mu = e_0$ for $\mu = 0,1,2$ and $e_\mu\bar e_\nu = -e_\mu e_\nu = e_\nu e_\mu = -e_\nu\bar e_\mu$ for $\mu\neq\nu$; the mixed second derivatives cancel in the product.

**Remark (the contrast with $D_3$).** The two three-dimensional operators are different objects. The Moisil–Theodoresco operator $D_3 = e_1\partial_1+e_2\partial_2+e_3\partial_3$ uses the three imaginary directions and squares by itself, $D_3^2 = -\Delta_3$; the reduced operator $D$ uses one real and two imaginary directions and needs its conjugate, $D\bar D = \Delta_3$. They are exchanged by the rotation that trades the coordinate $x_0$ for $x_3$ and the basis element $e_0$ for $e_3$, and they agree on the functions independent of the traded coordinate.

**Definition (monogenic).** An $\mathcal{A}$-valued continuously differentiable function $f$ is **monogenic** in $\Omega$ if $Df = 0$, and **anti-monogenic** if $\bar Df = 0$.

**Proposition (component form).** For $f = f_0+f_1e_1+f_2e_2$,

$$
Df = (\partial_0f_0-\partial_1f_1-\partial_2f_2)+(\partial_0f_1+\partial_1f_0)e_1+(\partial_0f_2+\partial_2f_0)e_2+(\partial_1f_2-\partial_2f_1)e_3,
$$

so the equation $Df = 0$ is the first-order system

$$
\partial_0f_0 = \partial_1f_1+\partial_2f_2, \qquad \partial_0f_1 = -\partial_1f_0, \qquad \partial_0f_2 = -\partial_2f_0, \qquad \partial_1f_2 = \partial_2f_1 .
$$

*Proof.* Direct expansion with $e_1^2 = e_2^2 = -e_0$ and $e_1e_2 = e_3 = -e_2e_1$; the $e_3$-component collects the two cross products $\partial_1f_2\,e_1e_2$ and $\partial_2f_1\,e_2e_1$, whose difference is $(\partial_1f_2-\partial_2f_1)e_3$.

The value of $Df$ is a full quaternion: the $e_3$-component is present although the values of $f$ lie in the three-dimensional subspace. Monogenicity therefore imposes one equation more than the dimension of the values suggests, and that fourth equation is what couples the two imaginary components.

**Proposition (two-sidedness; the Riesz system).** For an $\mathcal{A}$-valued function the left and right equations are equivalent,

$$
Df = 0 \iff fD = 0,
$$

and both are equivalent to the **Riesz system** for the field $F = (f_0,-f_1,-f_2)$,

$$
\operatorname{div}F = 0, \qquad \operatorname{curl}F = 0 .
$$

*Proof.* Expanding $fD = \sum_\mu(\partial_\mu f)e_\mu$ gives the same scalar, $e_1$ and $e_2$ components as $Df$ above, and the opposite $e_3$ component $-(\partial_1f_2-\partial_2f_1)$; the two systems of four equations therefore have the same solutions. For the second statement, $\operatorname{div}F = \partial_0f_0-\partial_1f_1-\partial_2f_2$ is the scalar equation, the three components of $\operatorname{curl}F$ are $\partial_1F_2-\partial_2F_1 = -(\partial_1f_2-\partial_2f_1)$, $\partial_2F_0-\partial_0F_2 = \partial_2f_0+\partial_0f_2$ and $\partial_0F_1-\partial_1F_0 = -(\partial_0f_1+\partial_1f_0)$, and the four equations written above are exactly these four.

**Remark (why two-sidedness is special).** In the four-variable theory the left and right equations are genuinely different and the two classes of regular functions do not coincide. Here they do, and for a structural reason: the mismatch between the two products is confined to the single component $e_3$ and to a single sign, so the two four-equation systems have the same solution set. It is this coincidence that lets the classical one-variable arguments, which use the product rule on both sides, run in three variables without modification.

**Definition (hypercomplex derivative, constants, primitive).** For a monogenic function $f$ the **hypercomplex derivative** is $\tfrac12\bar Df$. A monogenic function whose hypercomplex derivative vanishes identically is a **hyperholomorphic constant**; equivalently it is a function monogenic with respect to both $D$ and $\bar D$. A **monogenic primitive** of a monogenic $f$ is a monogenic $\mathcal{P}f$ with $\tfrac12\bar D(\mathcal{P}f) = f$; the primitive is made unique by requiring it to be orthogonal to the hyperholomorphic constants.

**Proposition (the ladder).** Relative to the orthogonal basis of the paragraph below,

$$
\tfrac12\bar D\,X_n^{l,\dagger} = (n+l+1)X_{n-1}^{l,\dagger}\ (0\leq l\leq n), \qquad
\tfrac12\bar D\,Y_n^{m,\dagger} = (n+m+1)Y_{n-1}^{m,\dagger}\ (1\leq m\leq n),
$$

so differentiation lowers the degree by one and multiplies by a positive integer, and

$$
\mathcal{P}X_n^{l,\dagger} = \frac{X_{n+1}^{l,\dagger}}{n+l+2}\ (0\leq l\leq n+1), \qquad
\mathcal{P}Y_n^{m,\dagger} = \frac{Y_{n+1}^{m,\dagger}}{n+m+2}\ (1\leq m\leq n+1).
$$

The elements $X_n^{n+1,\dagger}$ and $Y_n^{n+1,\dagger}$ are the hyperholomorphic constants of degree $n$: they are monogenic and annihilated by $\tfrac12\bar D$.

**Spherical monogenics.** The **solid spherical monogenics** are the homogeneous monogenic $\mathcal{A}$-valued polynomials, and their space in degree $n$ is written $\mathcal{R}^+(B_r;\mathcal{A};n)$. A complete orthogonal system is obtained by applying $\tfrac12\bar D$ to the solid harmonics $r^{n+1}U^0_{n+1}$, $r^{n+1}U^m_{n+1}$, $r^{n+1}V^m_{n+1}$ built from the Legendre polynomial of degree $n+1$ and its associated functions $P^m_{n+1}$, $m = 1,\dots,n+1$, and the resulting basis of traces on the sphere is

$$
\{X_n^0, X_n^m, Y_n^m : m = 1,\dots,n+1\}_{n\in\mathbb{N}_0},
$$

a system that can be read as a refinement of the spherical harmonics and that carries recurrence relations and preserves the properties of the holomorphic powers $z^n$. Its $L^2(B_r;\mathcal{A})$ norms and its pointwise bounds are

$$
\|X_n^{0,\dagger}\| = \sqrt{\frac{r^{2n+3}}{2n+3}}\sqrt{\pi(n+1)}, \qquad
\|X_n^{m,\dagger}\| = \|Y_n^{m,\dagger}\| = \sqrt{\frac{r^{2n+3}}{2n+3}}\sqrt{\frac{\pi}{2}(n+1)\frac{(n+1+m)!}{(n+1-m)!}},
$$

$$
|X_n^{l,\dagger}(x)| \leq \frac{1}{2}(n+1)\sqrt{\frac{(n+1+l)!}{(n+1-l)!}}\,|x|^n, \qquad
|Y_n^{m,\dagger}(x)| \leq \frac{1}{2}(n+1)\sqrt{\frac{(n+1+m)!}{(n+1-m)!}}\,|x|^n .
$$

**Theorem (dimension of the monogenic polynomials).** $\dim\mathcal{R}^+(B_r;\mathcal{A};n) = 2n+3$.

The count is fixed by the ladder: the space of $\mathcal{A}$-valued homogeneous polynomials of degree $n$ has dimension $3(n+1)$, the derivative $\tfrac12\bar D$ maps the monogenic subspace of degree $n$ onto that of degree $n-1$ with kernel of dimension two, and the rank and the kernel dimensions are $2n+1$ and $2$, so the dimension is $2n+3$. Verified in exact arithmetic for $n = 0,\dots,5$: $3,5,7,9,11,13$.

**Remark (dimension counts).** In one complex variable the monogenic polynomials of degree $n$ form a two-dimensional space, spanned by the trace of the holomorphic power and its companion, for every $n$. Here the count grows linearly, $2n+3$, because the two hyperholomorphic constants of each degree account for two dimensions and the remaining $2n+1$ carry the sphere's worth of harmonics that must be paired in each degree. The generic Clifford dimension formula belongs to the Clifford-type systems of *Harmonic Analysis over Hypercomplex Systems* and does not apply here, because $\mathcal{A}$ is not an algebra.

**Theorem (Fourier expansion; the main part and the constants).** Let $f\in\mathcal{R}^+(B_r;\mathcal{A})$. Then $f$ decomposes as an orthogonal sum

$$
f(x) = g(x)+h(x), \qquad
g(x) = \sum_{n=0}^{\infty}\Bigl[X_n^{0,\dagger}(x)a_n^0+\sum_{m=1}^{n}\bigl(X_n^{m,\dagger}(x)a_n^m+Y_n^{m,\dagger}(x)b_n^m\bigr)\Bigr],
$$

$$
h(x) = \sum_{n=0}^{\infty}\bigl[X_n^{n+1,\dagger}(x)a_n^{n+1}+Y_n^{n+1,\dagger}(x)b_n^{n+1}\bigr],
$$

with real coefficients, where $g$ is the **main part** of $f$ and $h$ is the hyperholomorphic constant: the first sum runs over the basis elements up to index $n$, and the second over the two basis elements of index $n+1$, which are the constants of the degree.

*Proof.* The basis is complete and orthogonal in $L^2(B_r;\mathcal{A})$, so the expansion follows from the usual $L^2$ projection; the two index ranges separate the elements that survive the hypercomplex derivation from those it annihilates.

**Remark.** The orthogonal splitting $f = g+h$ is the exact analogue of the classical fact that $f(z)-f'(0)z$ is orthogonal to the constants, and it is the structural reason the one-variable estimates carry over to this setting. The estimate of the hypercomplex derivative by the growth of its maximum modulus, and the Bloch radius that it gives, are worked out in *Bloch's Theorem and the Bloch Constant for Monogenic Functions*.

## The Cauchy Integral Formula

**Theorem (fundamental solution).** The Cauchy kernel $G(x) = \bar x/|x|^4$ satisfies $DG = 0$ for $x\neq0$ and, in the sense of distributions,

$$
DG = 2\pi^2\delta_0 e_0 .
$$

**Theorem (Cauchy integral formula).** Let $f$ be continuously differentiable on a bounded domain $\Omega\subseteq\mathbb{H}$ with piecewise smooth boundary $\partial\Omega$, and let $x_0$ be an interior point. Then

$$
f(x_0) = \frac{1}{2\pi^2}\int_{\partial\Omega}G(x-x_0)\,n(x)f(x)\,dS - \frac{1}{2\pi^2}\int_{\Omega}G(x-x_0)\,(Df)(x)\,dV,
$$

where $n$ is the $\mathbb{H}$-valued outward unit normal. If $f$ is regular, the volume term vanishes and

$$
f(x_0) = \frac{1}{2\pi^2}\int_{\partial\Omega}G(x-x_0)\,n(x)f(x)\,dS .
$$

*Proof.* These are the standard results of Clifford analysis in dimension four; the kernel and the constant are computed from the distributional identity $DG = 2\pi^2\delta_0e_0$, which is verified by integrating over a ball of radius $\varepsilon$ and using the homogeneity of $G$. The formula is derived by applying Stokes' theorem to the form $G(x-x_0)n(x)f(x)\,dS$ and subtracting the singular contribution at $x_0$, all products being quaternion products with $G$ on the left and $f$ on the right.

**Corollary.** On $\mathbb{H}$ the Cauchy integral formula holds on every domain, with no restriction to a subspace and no exceptional set; the mean value property, the maximum principle, Liouville's theorem, the identity theorem, and the residue theory for isolated singularities then follow as for holomorphic functions of one variable, since $\mathbb{H}$ has no zero divisors.

*Proof.* The kernel is defined and smooth off the origin throughout $\mathbb{H}$; the absence of zero divisors makes the inverse $x^{-1}$ defined for every $x\neq0$ and the singular set a single point. The consequences are standard in Clifford analysis.

## Comparison with the Biquaternion Case

The biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ carries the same operator with complex coefficients, so the Cauchy–Riemann operator on $\mathbb{H}$ is exactly the operator on the quaternion subspace $\mathbb{H}_{\mathbb{B}}$ of $\mathbb{B}$, where all coefficients are real.

| Feature | $\mathbb{H}$ | $\mathbb{B}$ |
|---|---|---|
| Coefficients of the variable | real | complex |
| Norm | definite | indefinite |
| Zero divisors | none | the null cone $\mathcal{N} = \{N = 0\}$ |
| Ellipticity of $D$ | everywhere, $s(\xi)\bar s(\xi) = \lvert\xi\rvert^2$ | on indefinite subspaces $s(\xi)\bar s(\xi)$ degenerates on $\mathcal{N}$ |
| Cauchy kernel | $G = \bar x/\lvert x\rvert^4$, regular off the origin | regular only where $N\neq0$; not a fundamental solution on indefinite subspaces |
| Cauchy integral formula | global on every domain | asserted only on the quaternion subspace $\mathbb{H}_{\mathbb{B}}$ |
| Maximum principle, Liouville, residue theory | available | available on $\mathbb{H}_{\mathbb{B}}$, fail on $\mathbb{M}_\pm$ |

The obstruction in the biquaternion case is entirely the null cone: because $N$ is indefinite, the principal symbol $s(\xi)$ is singular on the characteristic set, the Cauchy kernel ceases to be a fundamental solution off the quaternion subspace, and the identity $\bar x x = |x|^2$ used to compute $DG = 0$ fails once the coefficients are complex and null. On the quaternion algebra the quaternion norm is definite, so all of these properties hold globally and the four-variable Cauchy theory is complete. The biquaternion account is in *Biquaternion Regular Functions*.

## Summary

The Cauchy–Riemann operator $D = \sum_\mu e_\mu\partial_\mu$ and its conjugate $\bar D = \sum_\mu\bar e_\mu\partial_\mu$ factor the Euclidean Laplacian, $D\bar D = \bar DD = \Delta$, through the Clifford relation $e_\mu\bar e_\nu+e_\nu\bar e_\mu = 2\delta_{\mu\nu}e_0$. A function is left-regular if $Df = 0$; regularity is equivalent to the Cauchy–Riemann–Fueter system $\partial_0f_0 = \mathrm{div}\,\mathbf{f}$, $\partial_0\mathbf{f}+\mathrm{grad}\,f_0+\mathrm{rot}\,\mathbf{f} = 0$, a first-order elliptic system of four equations whose principal symbol is invertible everywhere because the quaternion norm is definite.

Regular functions are closed under addition, right multiplication by constants, and real scaling, but not under left multiplication by general quaternions, so they form a right module; constants and classical holomorphic functions of a single-plane variable are regular, the coordinate function is not, and the genuine radial regular function is the Cauchy kernel $G = \bar x/|x|^4$, of homogeneity $-3$ in four variables. Every regular function is harmonic, but not conversely. The Cauchy integral formula holds on every domain in $\mathbb{H}$, with the kernel $G$ and the constant $1/(2\pi^2)$, and it yields the mean value property, the maximum principle, Liouville's theorem and the residue theory without exception.

The spatial part $D_3 = e_1\partial_1+e_2\partial_2+e_3\partial_3$ is the **Moisil–Theodoresco operator** of the three-dimensional theory: it splits as $-\mathrm{div}+\mathrm{grad}+\mathrm{rot}$, it squares alone to the negative Laplacian, $D_3^2 = -\Delta_3$, and it carries the logarithmic derivative $\check\partial\phi = \phi^{-1}D_3\phi$ and the Riccati PDE $D_3\mathbf{f}+\mathbf{f}^2 = v$, which is equivalent to the three-dimensional Schrödinger equation $\Delta_3\phi+v\phi = 0$ and factorises its operator, $-\Delta_3-vI = (D_3+M_{\mathbf{f}})(D_3-M_{\mathbf{f}})$, on a scalar right factor. The four-dimensional operator needs its conjugate for the same factorisation because only the conjugate removes the mixed term $2\partial_0D_3$ of its square. The same operator carries the equation $D_3f+f\vec\alpha = 0$ with a general vectorial coefficient: for a coefficient with one function of one variable per direction, the product $(D_3+M_{\vec\alpha})(D_3-M_{\vec\alpha})$ acts componentwise as four *scalar* Schrödinger operators with the four potentials $\vec\alpha^2\pm D_3\vec\alpha^{(k)}$, the reduction is exact precisely for coefficients of skew-symmetric Jacobian, and the idempotents $\tfrac12(1\pm ie_k)$ split a scalar shift into two shifts of opposite sign.

A second three-dimensional theory uses the **reduced quaternions** $\mathcal{A} = \operatorname{span}_\mathbb{R}\{e_0,e_1,e_2\}$, a three-dimensional real subspace that is closed under conjugation and inversion but is not a subalgebra, since $e_1e_2 = e_3$ leaves it. The reduced Cauchy–Riemann operator $D = \partial_0+e_1\partial_1+e_2\partial_2$ and its conjugate factor the three-dimensional Laplacian, $D\bar D = \bar DD = \Delta_3$, and they are the rotation images of $D_3$ under the exchange of $x_0$ with $x_3$; unlike $D_3$ they act on one real and two imaginary coordinates. In components, $Df = 0$ is the four-equation system $\partial_0f_0 = \partial_1f_1+\partial_2f_2$, $\partial_0f_1 = -\partial_1f_0$, $\partial_0f_2 = -\partial_2f_0$, $\partial_1f_2 = \partial_2f_1$, and it is equivalent both to the right equation $fD = 0$ and to the **Riesz system** $\operatorname{div}F = \operatorname{curl}F = 0$ for $F = (f_0,-f_1,-f_2)$: every monogenic function of this theory is two-sided, a coincidence that fails in four variables. The hypercomplex derivative is $\tfrac12\bar Df$, its vanishing defines the hyperholomorphic constants, and the monogenic primitive is the inverse of that derivative modulo the constants. The solid spherical monogenics form a complete orthogonal system indexed by polynomials $X_n^{l,\dagger}$ and $Y_n^{m,\dagger}$ built from the Legendre functions, with ladder relations under differentiation and primitivation, and the homogeneous monogenic polynomials of degree $n$ form a space of dimension $2n+3$. Every monogenic function decomposes orthogonally into a main part and a hyperholomorphic constant, the analogue of the classical fact that $f(z)-f'(0)z$ is orthogonal to the constants; that decomposition is the basis of the Bloch theorem for monogenic functions.

The comparison with the biquaternions isolates the role of the quaternion norm: on $\mathbb{H}$ the definiteness of $N$ makes the operator elliptic everywhere and the Cauchy theory global, while on $\mathbb{B}$ the indefinite form produces the null cone, on which the symbol degenerates and the Cauchy kernel ceases to be fundamental, so the analogy is available only on the quaternion subspace. The Fueter construction and the slice description of regular functions are in *Fueter Theory for Quaternions*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | The quaternion algebra, a division algebra |
| $x = x_0+\mathbf{x}$ | Variable quaternion, $x_\mu\in\mathbb{R}$, $\mathbf{x} = x_1e_1+x_2e_2+x_3e_3$ |
| $\partial_\mu, \Delta = \sum_\mu\partial_\mu^2$ | Partial derivatives and Euclidean Laplacian |
| $D = \sum_\mu e_\mu\partial_\mu$ | Cauchy–Riemann operator |
| $\bar D = \sum_\mu\bar e_\mu\partial_\mu$ | Conjugate operator, $\bar e_0 = e_0$, $\bar e_k = -e_k$ |
| $e_\mu\bar e_\nu+e_\nu\bar e_\mu = 2\delta_{\mu\nu}e_0$ | Clifford relation; gives $D\bar D = \bar DD = \Delta$ |
| $Df = 0$ | Left-regularity; regular means left-regular here |
| $fD = 0$, $\bar Df = 0$ | Right-regular and anti-regular functions |
| $\mathrm{div}, \mathrm{grad}, \mathrm{rot}$ | Vector-calculus operators in the decomposition of $Df$ |
| $\partial_0f_0 = \mathrm{div}\,\mathbf{f}$, $\partial_0\mathbf{f}+\mathrm{grad}\,f_0+\mathrm{rot}\,\mathbf{f} = 0$ | Cauchy–Riemann–Fueter system |
| $s(\xi) = \sum_\mu\xi_\mu e_\mu$ | Principal symbol, $s\bar s = \lvert\xi\rvert^2$ |
| $z = x_0+e_1x_1$ | Single-plane complex variable, $\partial_{\bar z} = \tfrac12(\partial_0+e_1\partial_1)$ |
| $G(x) = \bar x/\lvert x\rvert^4$ | Cauchy kernel; $DG = 2\pi^2\delta_0e_0$ |
| $\mathbb{B}, \mathbb{H}_{\mathbb{B}}$ | Biquaternion algebra and its quaternion subspace |
| $D_3 = e_1\partial_1+e_2\partial_2+e_3\partial_3$ | Moisil–Theodoresco operator; $D_3^2 = -\Delta_3$ |
| $\check\partial\phi = \phi^{-1}D_3\phi$ | Logarithmic derivative; $\mathbf{f} = \check\partial\phi$ solves the Riccati PDE |
| $M_{\vec\alpha}$ | Operator of right multiplication by $\vec\alpha$, $M_{\vec\alpha}u = u\vec\alpha$ |
| $\vec\alpha^{(k)}$ | $\vec\alpha^{(0)} = \vec\alpha$, $\vec\alpha^{(k)} = -e_k\vec\alpha e_k$ ($k\ge1$): the two components other than $k$ reversed |
| $v_k = -D_3\vec\alpha^{(k)}-\vec\alpha^2$, $w_k = D_3\vec\alpha^{(k)}-\vec\alpha^2$ | The four potentials of the componentwise reduction |
| $P^\pm_k = \tfrac12M_{(1\pm ie_k)}$ | Complementary idempotents; $P^\pm_k(D_3+M_\nu) = (D_3\pm M_{i\nu e_k})P^\pm_k$ |
| $\mathcal{A} = \operatorname{span}_\mathbb{R}\{e_0,e_1,e_2\}$ | Reduced quaternions; a real subspace, not a subalgebra |
| $D = \partial_0+e_1\partial_1+e_2\partial_2$ | Reduced Cauchy–Riemann operator on $\mathbb{R}^3$ |
| $\bar D = \partial_0-e_1\partial_1-e_2\partial_2$ | Its conjugate; $D\bar D = \bar DD = \Delta_3$ |
| $Df = 0 \iff fD = 0 \iff \mathrm{div}F = \mathrm{curl}F = 0$ | Two-sidedness and the Riesz system, $F = (f_0,-f_1,-f_2)$ |
| $\tfrac12\bar Df$ | Hypercomplex derivative |
| $\mathcal{R}^+(B_r;\mathcal{A};n)$ | Homogeneous monogenic polynomials of degree $n$; $\dim = 2n+3$ |
| $X_n^{l,\dagger}, Y_n^{m,\dagger}$ | Orthogonal basis of solid spherical monogenics |
| $X_n^{n+1,\dagger}, Y_n^{n+1,\dagger}$ | Hyperholomorphic constants of degree $n$ |
| $\mathcal{P}$ | Monogenic primitive; inverse to $\tfrac12\bar D$ modulo the constants |

## Further Reading

- Rudolf Fueter, "Die Funktionentheorie der Differentialgleichungen $\Delta u = 0$ und $\Delta\Delta u = 0$ mit vier reellen Variablen", *Commentarii Mathematici Helvetici* **7** (1934) 307–330, for the origin of the four-variable regularity theory.
- F. Brackx, Richard Delanghe and F. Sommen, *Clifford Analysis* (Pitman, 1982), for the Cauchy–Riemann operator, monogenic functions and the Cauchy integral formula.
- Richard Delanghe, F. Sommen and V. Souček, *Clifford Algebra and Spinor-Valued Functions* (Kluwer, 1992), for the function theory of the Cauchy–Riemann operator in several variables.
- John E. Gilbert and Margaret A. M. Murray, *Clifford Algebras and Dirac Operators in Harmonic Analysis* (Cambridge University Press, 1991), for the analytic properties of the operator and its consequences.
- Klaus Gürlebeck and Wolfgang Sprößig, *Quaternionic and Clifford Calculus for Physicists and Engineers* (Wiley, 1997), for the quaternion Cauchy formula and its applications.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd ed. 2001), for the algebraic identities underlying the factorization of the Laplacian.
- Viktor Kravchenko, Vladislav V. Kravchenko and Benjamin Williams, "A quaternionic generalisation of the Riccati differential equation" (arXiv:math-ph/0101010, 2001), for the Moisil–Theodoresco operator, the logarithmic derivative and the Riccati PDE.
- Viktor G. Kravchenko and Vladislav V. Kravchenko, "Quaternionic factorization of the Schrödinger operator and its applications to some first order systems of mathematical physics" (arXiv:math-ph/0305046, 2003), for the equation $D_3f+f\vec\alpha = 0$ with a vectorial coefficient, the componentwise reduction to four scalar Schrödinger operators with the potentials $\pm D_3\vec\alpha^{(k)}-\vec\alpha^2$, and the projections $P^\pm_k$; the separability hypothesis there is sufficient but the exact condition for the reduction is the vanishing of the symmetric part of the Jacobian of $\vec\alpha$.
- Marcel Riesz, *Clifford Numbers and Spinors* (Institute for Physical Science and Technology, Lecture Series 38, Maryland, 1958), for the original Riesz system in $\mathbb{R}^3$ and its relation to the $n$-dimensional Cauchy–Riemann system.
- Klaus Gürlebeck and Helmuth Malonek, "A hypercomplex derivative of monogenic functions in $\mathbb{R}^{n+1}$ and its applications", *Complex Variables and Elliptic Equations* **39** (1999) 199–228, for the hypercomplex derivative, the hyperholomorphic constants and the monogenic primitive.
- Helmuth Leutwiler, "Quaternionic analysis in $\mathbb{R}^3$ versus its hyperbolic modification", in *Clifford Analysis and Its Applications*, NATO Science Series II **25** (Kluwer, 2001) 193–211, for the reduced-quaternion function theory and the dimension $2n+3$ of the homogeneous monogenic polynomials.
- Richard Delanghe, "On homogeneous polynomial solutions of the Riesz system and their harmonic potentials", *Complex Variables and Elliptic Equations* **52** (2007) 1047–1062, for the polynomial solutions of the Riesz system and their harmonic potentials.
- Isabel Caçao, Klaus Gürlebeck and Sören Bock, "On derivatives of spherical monogenics", *Complex Variables and Elliptic Equations* **51** (2006) 847–869, for the complete orthonormal systems of spherical monogenics and the ladder relations.
- Klaus Gürlebeck and João Morais, "On orthonormal polynomial solutions of the Riesz system in $\mathbb{R}^3$", in *Recent Advances in Computational and Applied Mathematics* (Springer, 2011) 143–158, for the orthogonal basis, the norm formulas and the pointwise estimates used above.
