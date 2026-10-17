# __The Dirichlet Principle and the Hermitian Functional__

## Introduction

The weak solution of an elliptic problem is the minimiser of an energy. For the Dirichlet problem of $L$ with data $f$ the functional is

$$
E_f(w) = \mathfrak{a}(w,w) - 2\operatorname{Re}\langle f,w\rangle ,
$$

the Hermitian quadratic part of the sesquilinear form minus the pairing with the data, and the **Dirichlet principle** is the statement that $E_f$ attains its minimum at exactly one point of the test space and that the minimiser is the weak solution. The principle is the energy reading of the weak formulation: the variational equation $\mathfrak{a}(w,v)=\langle f,v\rangle$ is the vanishing of the first variation of $E_f$, and the coercivity of the form is what makes the stationary point a minimum and makes it unique.

This article reads the elliptic problem with the conjugation of the unknown function and moves from the equation to the functional. It fixes the Hermitian functional — its quadratic part, its reality, its strict convexity and the completion of the square — and proves the Dirichlet principle in the elliptic setting: the minimiser over the Dirichlet test space exists, is unique, and is the weak solution; conversely the weak solution minimises. It then proves the regularity of the minimiser, the interior smoothness of a weak solution of an elliptic equation (Weyl's lemma) and the classical Dirichlet principle for the Laplacian, whose minimiser with given boundary values is the harmonic function.

The sesquilinear form, its boundedness, coercivity and Hermitian property, the weak formulation and the solution operator are those of *Sesquilinear Forms and the Weak Formulation of an Elliptic Problem*; the closed coercive Hermitian form, its generator and the general Dirichlet principle are those of *Dirichlet Forms and the Hermitian Dirichlet Principle*, cited for the abstract statement; the calculus of variations and the general Euler–Lagrange equation are those of *The Calculus of Variations* and *The Euler–Lagrange Equation*; the Sobolev spaces, the trace and the Poincaré inequality are those of *Sobolev Spaces and Weak Solutions*; the elliptic regularity and Weyl's lemma are those of *Distributions and Fundamental Solutions* and *Partial Differential Equations*; and the classical Dirichlet problem and the harmonic functions are *Harmonic Functions and the Dirichlet Problem*. The variational characterisation of the eigenvalues and the min–max principle are *Variational Methods and the Hermitian Form*, below.

## The Hermitian Functional

**Definition.** Let $\mathfrak{a}$ be the sesquilinear form of an elliptic operator, bounded on $H^1(\Omega)$ and coercive on $H^1_0(\Omega)$, with Hermitian part $a_{\mathrm H}(w,v)=\tfrac12\bigl(\mathfrak{a}(w,v)+\overline{\mathfrak{a}(v,w)}\bigr)$, and let $f\in L^2(\Omega)$. The **Hermitian functional** of the problem is

$$
E_f(w) = a_{\mathrm H}(w,w) - 2\operatorname{Re}\langle f,w\rangle ,
$$

and for the Dirichlet integral of the Laplacian $\mathfrak{a}(w,v)=\int_\Omega\nabla w\cdot\overline{\nabla v}$ it is the classical **Dirichlet functional**

$$
D(w) = \int_\Omega|\nabla w|^2\,dx - 2\operatorname{Re}\langle f,w\rangle .
$$

When the form is Hermitian, $a_{\mathrm H}=a$ and $E_f(w)=\mathfrak{a}(w,w)-2\operatorname{Re}\langle f,w\rangle$; this is the case of the formally self-adjoint problem, and it is the case in which the functional is the energy.

**Proposition (reality, convexity and coercivity).** Let $\mathfrak{a}$ be Hermitian with coercivity constant $c$, so that $\mathfrak{a}(w,w)\ge c\|w\|_{H^1}^2$. Then $E_f$ is real-valued, strictly convex on $H^1_0(\Omega)$, bounded below, and **coercive** on the test space:

$$
E_f(w)\ge \tfrac{c}{2}\|w\|_{H^1}^2 - \frac{2}{c}\|f\|_{L^2}^2 ,
$$

so that $E_f(w)\to+\infty$ as $\|w\|_{H^1}\to\infty$; the functional attains a minimum on the nonempty closed convex set $H^1_0(\Omega)$.

*Proof.* Reality is the Hermitian property, $\mathfrak{a}(w,w)=\overline{\mathfrak{a}(w,w)}$. Strict convexity is the strict positivity of the quadratic part: for $w\neq v$ and $0<t<1$, $\mathfrak{a}(tw+(1-t)v,\cdot)$ expands into $ta(w,\cdot)+(1-t)\mathfrak{a}(v,\cdot)$ and the quadratic part is strictly convex because $\mathfrak{a}$ is coercive and the form modulus is bounded. For the lower bound, $|2\operatorname{Re}\langle f,w\rangle|\le2\|f\|_{L^2}\|w\|_{L^2}\le\frac{c}{2}\|w\|_{H^1}^2+\frac{2}{c}\|f\|_{L^2}^2$ by the elementary inequality $2\|f\|\|w\|\le\frac{c}{2}\|w\|^2+\frac{2}{c}\|f\|^2$; subtracting from the coercive bound gives the display. Coercive convex continuous functionals on a closed convex set attain their minimum.

**Proposition (completion of the square).** Let $w_0$ be the minimiser of $E_f$. Then for every $w\in H^1_0(\Omega)$,

$$
E_f(w) = \mathfrak{a}(w-w_0,w-w_0) - \mathfrak{a}(w_0,w_0) ,
$$

so that the minimum value is $-\mathfrak{a}(w_0,w_0)=-\langle f,w_0\rangle$, and $E_f$ is the translate of the squared form norm.

*Proof.* Expanding the right side and using the Hermitian symmetry $\mathfrak{a}(w,w_0)=\overline{\mathfrak{a}(w_0,w)}$ together with the variational equation $\mathfrak{a}(w_0,w)=\langle f,w\rangle$,

$$
\mathfrak{a}(w-w_0,w-w_0)-\mathfrak{a}(w_0,w_0) = \mathfrak{a}(w,w)-2\operatorname{Re}\mathfrak{a}(w,w_0) = \mathfrak{a}(w,w)-2\operatorname{Re}\overline{\langle f,w\rangle} = E_f(w) ,
$$

which is the display; the minimum value follows on setting $w=w_0$, where the squared form norm vanishes.

## The Dirichlet Principle

**Theorem (the Dirichlet principle).** Let the Hermitian form $\mathfrak{a}$ be bounded and coercive on $H^1_0(\Omega)$. Then $E_f$ has a unique minimiser in $H^1_0(\Omega)$, and $w$ is that minimiser if and only if $w$ is the weak solution, $\mathfrak{a}(w,v)=\langle f,v\rangle$ for every $v\in H^1_0(\Omega)$.

*Proof.* If $w$ minimises then for every $v$ and every real $t$ the function $t\mapsto E_f(w+tv)$ has a minimum at $t=0$; expanding,

$$
E_f(w+tv)-E_f(w) = 2t\operatorname{Re}\bigl(\mathfrak{a}(w,v)-\langle f,v\rangle\bigr) + t^2 \mathfrak{a}(v,v) ,
$$

so the derivative at $0$ vanishes, which for all $v$ is the variational equation; taking $v$ and then $iv$ separates the real and the imaginary part of $\mathfrak{a}(w,v)-\langle f,v\rangle$. Conversely, if the equation holds then the expansion reads $E_f(w+tv)-E_f(w)=t^2\mathfrak{a}(v,v)\ge0$ for every $v$, so no admissible direction lowers the value and $w$ minimises. Uniqueness is the strict convexity, or the completion of the square: two minimisers are both $w_0$ in that identity.

**Corollary (the minimiser is the weak solution).** The unique minimiser of the Dirichlet functional $D$ with datum $f$ is the weak solution of $-\Delta w=f$ with $w=0$ on $\partial\Omega$, and the minimal value is $-\langle f,w_0\rangle$ with $w_0$ the minimiser.

*Proof.* The Dirichlet functional is the Hermitian functional of the Laplacian form; the theorem identifies its minimiser with the weak solution, and the value is $-\langle f,w_0\rangle$ by the completion of the square.

**Theorem (the classical Dirichlet principle).** Let $U\in H^1(\Omega)$ be harmonic on $\Omega$ and let $\mathcal{E}_U=\{w\in H^1(\Omega) : w-U\in H^1_0(\Omega)\}$ be the affine set of admissible functions with the boundary data of $U$. Then $U$ minimises the Dirichlet integral $\int_\Omega|\nabla w|^2$ over $\mathcal{E}_U$, and it is the unique minimiser.

*Proof.* For any $w=U+\phi$ with $\phi\in H^1_0(\Omega)$,

$$
\int|\nabla w|^2 = \int|\nabla U|^2 + 2\operatorname{Re}\int\nabla U\cdot\overline{\nabla\phi} + \int|\nabla\phi|^2 ,
$$

and the middle term vanishes because $\Delta U=0$ in the weak sense and $\phi$ has trace zero; hence $\int|\nabla w|^2\ge\int|\nabla U|^2$, with equality only for $\phi=0$ by the Poincaré inequality. The classical minimiser is therefore the harmonic function with the given boundary values.

## Regularity of the Minimiser

**Theorem (Weyl's lemma for the minimiser).** Let the coefficients of $L$ be smooth and the form uniformly elliptic, and let $w\in H^1_0(\Omega)$ satisfy the variational equation for every test function, with $f\in L^2(\Omega)$. Then $w\in H^1_{\mathrm{loc}}(\Omega)$ is in fact $C^\infty(\Omega)$, and $Lw=f$ in the classical sense on $\Omega$. In particular the minimiser of the Dirichlet functional is smooth in the interior whenever $f$ is smooth, and it is harmonic where $f=0$.

*Proof.* The elliptic regularity theorem of *Distributions and Fundamental Solutions* gives $w\in H^2_{\mathrm{loc}}(\Omega)$; a bootstrap with the same theorem gives $w\in H^k_{\mathrm{loc}}(\Omega)$ for every $k$ once the coefficients and $f$ are smooth, and the Sobolev embedding gives the classical differentiability. The reduction to test functions is the standard localisation of the variational equation with a cutoff. The consequence for the minimiser follows because the minimiser is the weak solution.

**Remark (regularity and the classical statement).** Weyl's lemma is what closes the circle between the minimiser and the classical solution: the variational functional has a minimiser with no differentiability assumed, and the elliptic equation forces the minimiser to be as smooth as the data. The classical Dirichlet principle was stated by Riemann for the harmonic function with given boundary values and criticised for assuming the existence of the minimiser; the weak formulation and the coercivity supply the existence, and Weyl's lemma supplies the smoothness. The boundary regularity of the minimiser, that it is smooth up to the boundary when the boundary and the data are smooth, is the boundary estimate of *Partial Differential Equations*, and the harmonic case with general boundary data is *Harmonic Functions and the Dirichlet Problem*.

## The Inhomogeneous Problem and Variational Inequalities

**Theorem (the inhomogeneous Dirichlet problem).** Let $U\in H^1(\Omega)$ carry the boundary data and let $\phi\in H^1_0(\Omega)$, so that $w=U+\phi$ is the general admissible function. Then the minimiser of $\int|\nabla w|^2-2\operatorname{Re}\langle f,w\rangle$ over the affine set $U+H^1_0(\Omega)$ is $w=U+\phi_0$, where $\phi_0$ is the weak solution of

$$
\mathfrak{a}(\phi,v) = \langle f,v\rangle - \mathfrak{a}(U,v) \qquad (v\in H^1_0(\Omega)) ,
$$

and the dependence of $\phi_0$ on $U$ is affine and bounded; the boundary data therefore enter the problem as an extra source term $-\mathfrak{a}(U,\cdot)$.

*Proof.* Substituting $w=U+\phi$ in the Dirichlet principle, the functional becomes $E_f(U+\phi)$, whose part depending on $\phi$ is $\mathfrak{a}(\phi,\phi)-2\operatorname{Re}\langle f,\phi\rangle+2\operatorname{Re}\mathfrak{a}(U,\phi)$ plus a constant; the minimiser satisfies the variational equation displayed, and Lax–Milgram gives existence, uniqueness and the affine bounded dependence on $U$.

**Theorem (variational inequalities).** Let $K\subseteq H^1_0(\Omega)$ be a nonempty closed convex set and let $\mathfrak{a}$ be a bounded coercive Hermitian form. Then $E_f$ has a unique minimiser $w$ over $K$, and $w$ is characterised by the variational inequality

$$
\operatorname{Re}\bigl(\mathfrak{a}(w,v-w)\bigr) \ge \operatorname{Re}\langle f,v-w\rangle \qquad \text{for every } v\in K .
$$

*Proof.* Existence is the standard argument for a coercive convex continuous functional on a closed convex set: a minimising sequence is bounded, so a subsequence converges weakly, and the weak lower semicontinuity of $E_f$, which is convex continuous, gives a minimiser. Uniqueness is strict convexity, using the parallelogram identity for the quadratic part. For the characterisation, the convexity of $K$ makes $w+t(v-w)\in K$ for $0\le t\le1$; the derivative of $t\mapsto E_f(w+t(v-w))$ at $t=0$ is $2\operatorname{Re}(\mathfrak{a}(w,v-w)-\langle f,v-w\rangle)$, and it must be nonnegative.

**Example (the obstacle problem).** For $K=\{w\in H^1_0(\Omega) : w\ge\psi \text{ a.e.}\}$ with an obstacle $\psi\le0$ on the boundary and datum $f=0$, the minimiser satisfies the variational inequality and is the smallest superharmonic majorant of $\psi$: $-\Delta w\ge0$ on $\Omega$, $-\Delta w=0$ on the coincidence set $\{w>\psi\}$, and $w\ge\psi$. The inequality replaces the equation on the contact set, and it is the prototype of the variational inequalities of *The Calculus of Variations* and, in the literature, of *An Introduction to Variational Inequalities and Their Applications* by Kinderlehrer and Stampacchia.

## Summary

The elliptic weak problem has a Hermitian functional $E_f(w)=\mathfrak{a}(w,w)-2\operatorname{Re}\langle f,w\rangle$, the Dirichlet functional $D(w)=\int|\nabla w|^2-2\operatorname{Re}\langle f,w\rangle$ for the Laplacian; it is real, strictly convex and coercive, $E_f(w)\ge\frac{c}{2}\|w\|_{H^1}^2-\frac{2}{c}\|f\|_{L^2}^2$, and it is a translate of the squared form norm, $E_f(w)=\mathfrak{a}(w-w_0,w-w_0)-\mathfrak{a}(w_0,w_0)$, with the minimum value $-\langle f,w_0\rangle$. The Dirichlet principle identifies its unique minimiser with the weak solution: the first variation vanishes at $w$ for every direction exactly when $\mathfrak{a}(w,v)=\langle f,v\rangle$ for every $v$, and the second variation is $\mathfrak{a}(v,v)\ge0$, so the stationary point is the minimum, unique by strict convexity. For the Laplacian with given boundary values the minimiser of the Dirichlet integral is the harmonic function, the difference of the energies of two admissible functions being the Dirichlet integral of their difference. Finally, the minimiser is smooth: Weyl's lemma makes a weak solution of an elliptic equation with smooth coefficients and data of class $C^\infty$ in the interior, so the existence given by coercivity and the smoothness given by ellipticity meet in the minimiser. Over an affine admissible set the boundary data enter as the source term $-\mathfrak{a}(U,\cdot)$, and over a closed convex set the minimiser is characterised by the variational inequality $\operatorname{Re}\mathfrak{a}(w,v-w)\ge\operatorname{Re}\langle f,v-w\rangle$, of which the obstacle problem is the prototype.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathfrak{a}(w,v)$ | Sesquilinear form of the elliptic operator |
| $a_{\mathrm H}(w,v)=\tfrac12(\mathfrak{a}(w,v)+\overline{\mathfrak{a}(v,w)})$ | Hermitian part of the form |
| $E_f(w)=a_{\mathrm H}(w,w)-2\operatorname{Re}\langle f,w\rangle$ | Hermitian functional (energy) |
| $D(w)=\int|\nabla w|^2-2\operatorname{Re}\langle f,w\rangle$ | Dirichlet functional |
| $w_0$ | The minimiser, equal to the weak solution |
| $H^1_0(\Omega)$ | Dirichlet test space |
| $\mathcal{E}_U=U+H^1_0(\Omega)$ | Affine admissible set with boundary data $U$ |
| $c$ | Coercivity constant of the form |
| $K$ | Nonempty closed convex constraint set |
| $\psi$ | Obstacle, the function defining $K=\{w\ge\psi\}$ |

## Further Reading

- David Hilbert, *Über das Dirichletsche Prinzip* (Jahresbericht der Deutschen Mathematiker-Vereinigung 8, 1900), for the historical statement of the principle and its role.
- Hermann Weyl, *The method of orthogonal projection in potential theory* (Duke Mathematical Journal 7, 1940), for Weyl's lemma and the smoothness of weak solutions.
- David Gilbarg and Neil S. Trudinger, *Elliptic Partial Differential Equations of Second Order* (Springer, 2nd ed. 1983), for the energy functional, the minimisation and the regularity of the minimiser.
- David Kinderlehrer and Guido Stampacchia, *An Introduction to Variational Inequalities and Their Applications* (Academic Press, 1980), for the minimisation of convex functionals and the variational inequalities.
- Haïm Brezis, *Functional Analysis, Sobolev Spaces and Partial Differential Equations* (Springer, 2011), for the Dirichlet principle and the convexity of the energy.
- Lawrence C. Evans, *Partial Differential Equations* (American Mathematical Society, 2nd ed. 2010), for the energy method, the Dirichlet principle and the regularity theory.
