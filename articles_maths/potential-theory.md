
# __Potential Theory__

## Introduction

Potential theory is the study of the Laplace equation through its solutions and through the measures that solve it. Its two classical problems are the representation of a harmonic function by the values it takes on the boundary of the region where it is defined, and the measurement of the size of a set by the total mass that can be spread on it with a potential everywhere bounded by one. The first problem is the **Dirichlet problem**: given a function on the boundary of a domain, find the harmonic function inside with those boundary values. The second is the theory of **capacity**: the sets that no nonzero measure can charge without making the potential infinite are the polar sets, they are exactly the sets of zero capacity, and the capacity of a set is the best constant in the estimate that a measure on it must satisfy, which is the analytic form of the statement that the set is small.

The two problems are the same problem. The Dirichlet problem for the ball is solved by an explicit integral, the **Poisson integral**, whose kernel is the normal derivative of the Green function of the ball; the solution is unique by the maximum principle, and on a general domain the solution is constructed by **Perron's method**, taking the supremum of all subharmonic functions below the boundary data, a construction that produces a harmonic function but may fail to attain the boundary data at a point where the complement of the domain is too thin — and the exact condition for attainment is **Wiener's criterion**, a divergence condition on the sum of the capacities of the parts of the complement in the dyadic annuli around the point. Capacity is thus not an auxiliary notion: it decides the solvability of the classical boundary value problem. The Newtonian and logarithmic potentials are the objects connecting the two: the potential of a measure is superharmonic exactly on the sets the measure charges, the polar sets are exactly the sets of vanishing capacity, and the equilibrium measure of a set of positive capacity is the one that minimises the energy, its existence being Frostman's theorem.

The article is organised as follows. Harmonic and subharmonic functions; the mean value property and its converse, the maximum principle, Harnack's inequality and the Harnack convergence principle; the Poisson kernel and the solution of the Dirichlet problem on a ball; the Green function and the representation of a harmonic function on a smoothly bounded domain by its boundary values. Then potentials, energies, capacity, polar sets, the theorems of Frostman and Riesz, and the Wiener criterion. Then Perron's method and the barrier characterisation of regular boundary points. The last section records the relation to the harmonic analysis of the previous article — the Poisson integral as a convolution, the spherical harmonics as the eigenfunctions of the spherical Laplacian, and the Fourier transform of the Poisson kernel as the diagonaliser of the Laplacian on the half-space — and the relation to the partial differential equations of the later categories, where the weak formulation, the maximum principle of the general elliptic operator and the existence theory of the Dirichlet problem are not covered here.

The prerequisites are *Measure Theory and Integration* for the measure, the integral, the Riesz representation theorem for the extension of the surface measure and the approximation arguments; *Modes of Convergence* for the convergence of the Poisson integrals and for the almost everywhere statements; *Fourier Analysis on Euclidean Spaces* for the transform of the Poisson kernel, the heat kernel and the fundamental solution of the Laplacian; and *Convex Analysis* for the separation theorems used in the capacity theory. The weak theory of the elliptic boundary problem, the Sobolev spaces and the variational formulation of the Dirichlet principle belong to later categories of this Part; the statements of this article are the classical pointwise ones, with the weak versions cited as standard.

## Harmonic Functions

### The Mean Value Property

**Definition.** Let $\Omega\subseteq\mathbb{R}^n$ be open. A function $u\in C^2(\Omega)$ is **harmonic** if $\Delta u = 0$ on $\Omega$, where $\Delta = \sum_j\partial_j^2$; the **Newtonian kernel** is
$$
N(x) = \begin{cases}\dfrac{1}{(2-n)\sigma_{n-1}}\lvert x\rvert^{2-n},&n\geq3,\\[2mm] \dfrac{1}{2\pi}\log\lvert x\rvert,&n = 2,\end{cases}
$$
with $\sigma_{n-1}$ the surface measure of the unit sphere, so that $\Delta N = 0$ off the origin and the potential of a probability measure is the corresponding average of translates of $N$.

**Theorem (the mean value property).** A continuous $u$ on $\Omega$ is harmonic if and only if for every ball $B(x,r)\subseteq\Omega$
$$
u(x) = \frac{1}{\sigma_{n-1}r^{n-1}}\int_{\partial B(x,r)}u\,d\sigma = \frac{1}{\omega_nr^n}\int_{B(x,r)}u\,dy ,
$$
where $\sigma_{n-1}$ is the surface measure of the unit sphere and $\omega_n$ the volume of the unit ball. Consequently a harmonic function is $C^\infty$, in fact analytic, and it satisfies the **strong maximum principle**: if $u$ attains its maximum at an interior point of a connected $\Omega$, then $u$ is constant; and the **Liouville theorem**: a harmonic function on $\mathbb{R}^n$ bounded above (or below) is constant.

**Proof sketch.** The spherical mean $M(r) = (1/\sigma_{n-1})\int_{S^{n-1}}u(x+r\zeta)d\sigma(\zeta)$ satisfies the ordinary differential equation $M''(r)+\frac{n-1}{r}M'(r) = (1/\sigma_{n-1})\int_{S^{n-1}}\Delta u(x+r\zeta)d\sigma$; if $u$ is harmonic the right side vanishes, so $r^{n-1}M'(r)$ is constant, and its value at $r = 0$ is $0$, giving $M$ constant and equal to $u(x)$. Conversely the mean value property implies the maximum principle, and the maximum principle applied to the harmonic minorant $u-\epsilon\lvert x\rvert^2$ gives $\Delta u = 0$. Smoothness follows by writing $u$ as the average over a small sphere and differentiating under the integral sign. $\square$

**Theorem (Harnack's inequality and principle).** If $u\geq0$ is harmonic on a connected $\Omega$ and $K\subseteq\Omega$ is compact, then $\sup_Ku\leq C_K\inf_Ku$ with $C_K$ depending only on $K$ and $\Omega$; consequently a locally uniformly convergent sequence of harmonic functions has a harmonic limit, and a monotone sequence of harmonic functions converges, locally uniformly, to a harmonic function or to $+\infty$ identically.

**Proof sketch.** For the inequality one uses the Poisson representation on a ball inscribed in $\Omega$ and compares the Poisson kernels at two points of the compact set, the ratio of the kernels being bounded there. For the convergence principle, the Harnack inequality applied to the differences of a locally uniformly convergent sequence gives equicontinuity and the limit satisfies the mean value property, hence is harmonic. $\square$

**Theorem (removable singularities).** If $u$ is harmonic on $\Omega\setminus\{x_0\}$ and $u(x) = o(\lvert x-x_0\rvert^{2-n})$ as $x\to x_0$ for $n\geq3$ (and $u = o(\log\lvert x-x_0\rvert)$ for $n=2$), then $u$ extends to a harmonic function on $\Omega$.

**Proof sketch.** The mean value over a small sphere about $x_0$ is controlled by the hypothesis on the growth; the difference of $u$ and its Poisson-type corrector $cN$ has vanishing mean value at every scale, so the maximum principle applied on the annulus between two small spheres gives the bound and the case $c = 0$ gives the extension. $\square$

### The Dirichlet Problem on the Ball

**Definition.** The **Poisson kernel** of the unit ball is
$$
P(x,\zeta) = \frac{1-\lvert x\rvert^2}{\lvert x-\zeta\rvert^n}\qquad(x\in B,\ \zeta\in\partial B),
$$
and the **Poisson integral** of a function $f\in C(\partial B)$ is $u(x) = \frac{1}{\sigma_{n-1}}\int_{\partial B}P(x,\zeta)f(\zeta)\,d\sigma(\zeta)$.

**Theorem.** $P$ is harmonic in $x$, positive, and normalised: $\frac{1}{\sigma_{n-1}}\int_{\partial B}P(x,\zeta)d\sigma(\zeta) = 1$ for every $x\in B$. In the plane the kernel is $P(re^{i\theta},\zeta) = \frac{1-r^2}{1-2r\cos(\theta-\varphi)+r^2}$ with $\zeta = e^{i\varphi}$, and its integral against $d\theta$ over a period equals $2\pi$. The Poisson integral of a continuous $f$ solves the Dirichlet problem: $u$ is harmonic on $B$, extends continuously to $\bar B$ with $u = f$ on $\partial B$, and is the unique such function; moreover $u$ is the real part of a holomorphic function in the plane case, and the family $\{P(x,\cdot)\}_{x\to\zeta_0}$ is an approximate identity on the sphere, so that $u(x)\to f(\zeta_0)$ as $x\to\zeta_0$ along every approach.

**Proof sketch.** The kernel is $\partial_\nu G$ for the Green function of the ball; positivity and normalisation are direct computations, and the approximate identity property is the concentration of $P(x,\cdot)$ near $\zeta$ as $x\to\zeta$, controlled by the positivity and the normalisation, with the continuity of $f$ giving the limit. Uniqueness is the maximum principle applied to the difference of two solutions. $\square$

**Example.** For $u(x,y) = x^2-y^2$, harmonic in the plane, the mean value over the circle of radius $R$ about $(a,b)$ equals $u(a,b)$; the numerical averages over $200000$ points of the circles centred at $(0.3,-0.2)$ with $R = 0.5$ and at $(1,1)$ with $R = 2$ give $0.050000$ and $0$, in agreement with $u$ at the centres. The Poisson kernel in the plane has been integrated numerically over the period for $r = 0,0.3,0.7,0.95$, giving $2\pi$ in each case, which is the normalisation $u\equiv1$ and the exact value of the integral of the kernel.

**Theorem (Green's function and the representation).** Let $\Omega$ be a bounded domain with smooth boundary. There is a unique function $G:\Omega\times\Omega\to(-\infty,+\infty]$ with $G(x,y) = N(x-y)-h_x(y)$, where $h_x$ is harmonic in $y$ and chosen so that $G(x,\cdot) = 0$ on $\partial\Omega$; it is symmetric, $G(x,y) = G(y,x)$, positive, and satisfies for every $u$ harmonic on a neighbourhood of $\bar\Omega$
$$
u(x) = \frac{1}{\sigma_{n-1}}\int_{\partial\Omega}\partial_\nu G(x,\zeta)\,u(\zeta)\,d\sigma(\zeta),
$$
the **Poisson formula** of the domain, whose kernel $\partial_\nu G$ is the Poisson kernel.

**Proof sketch.** The existence of $h_x$ is the Dirichlet problem for the harmonic function $N(x-\cdot)$ on the boundary, solved by the method of the next section; symmetry follows by applying Green's second identity to $G(x,\cdot)$ and $G(y,\cdot)$ on the domain with two small balls removed and letting the radii tend to zero, which produces the symmetry of the singular parts. $\square$

## Potentials and Capacity

### Potentials and Energies

**Definition.** For a finite Borel measure $\mu$ of compact support the **Newtonian potential** is $U^\mu(x) = \int N(x-y)d\mu(y)$, and the **energy** is $I(\mu) = \iint N(x-y)\,d\mu(x)\,d\mu(y)$, a quantity in $(-\infty,+\infty]$.

**Theorem.** Let $\mu$ be a finite measure of compact support. Then $U^\mu$ is lower semicontinuous, is superharmonic on the complement of $\operatorname{supp}\mu$ and is superharmonic on $\mathbb{R}^n$ in the distributional sense; it is finite almost everywhere with respect to Lebesgue measure, and $-\infty<U^\mu(x)<+\infty$ at every point that is not an atom; and if $U^\mu\leq M$ everywhere then the energy satisfies $I(\mu)\leq M\mu(\mathbb{R}^n)$.

**Proof sketch.** The lower semicontinuity is Fatou's lemma applied to an approximating sequence of continuous kernels; the superharmonicity is the mean value inequality, which follows by integrating the mean value equality for $N$ over the measure; finiteness almost everywhere is the summability of $\lvert x\rvert^{2-n}$ in the appropriate dimension. The energy bound is the double integral of $U^\mu$ against $\mu$ and the pointwise bound. $\square$

**Theorem (Frostman).** Let $K\subseteq\mathbb{R}^n$ be compact and of positive capacity in the sense defined below. Then there is a probability measure $\mu$ supported on $K$ whose potential is bounded, and among the admissible measures the one minimising the energy is characterised by the condition that $U^\mu$ is constant on $K$ outside a polar set, that constant being the energy $I(\mu)$; the **equilibrium measure** is unique up to polar sets.

**Proof sketch.** The energy is a lower semicontinuous strictly convex functional on the weakly compact set of probability measures on $K$; a minimiser exists by the direct method, and the first variation in the direction of a difference of two admissible measures gives the constancy of the potential on the support almost everywhere. $\square$

**Example (the shell theorem and the equilibrium measure of a sphere).** For the uniform measure of total mass $m$ on the sphere of radius $R$ and the kernel $1/\lvert x-y\rvert$ in $\mathbb{R}^3$, the potential equals $m/R$ inside the sphere and $m/\lvert x\rvert$ outside, by the theorem of the spherical shell: the numerical evaluation of the surface integral over the unit sphere by a Fibonacci lattice with $200000$ points gives $4\pi$ at the points $0,0.5,0.9$ of the radial coordinate and $4\pi/r$ at $r = 2,3$, in agreement with the theorem. The uniform measure on the sphere is therefore an equilibrium measure of the sphere: its potential is constant on the support, and the corresponding energy is the capacity.

### Capacity and Polar Sets

**Definition.** For a compact set $K\subseteq\mathbb{R}^n$ the **capacity** is
$$
\operatorname{cap}(K) = \inf\Bigl\{\int_{\mathbb{R}^n}\lvert\nabla f\rvert^2\,dx : f\in C_c^\infty(\mathbb{R}^n),\ f\geq1\ \text{on a neighbourhood of } K\Bigr\},
$$
and the **energy capacity** is $\operatorname{cap}_2(K) = 1/\inf\{I(\mu) : \mu\ \text{probability measure on } K\}$, the two being comparable by constants depending on the dimension. A set is **polar** if it is contained in the set $\{U^\mu = +\infty\}$ for some finite measure $\mu$; the **fine topology** of Cartan is the coarsest topology in which every superharmonic function is continuous, and a set $E$ is **thin** at $x$ if $x$ is not a limit point of $E$ in the fine topology, so that a set is polar exactly when it is thin at every one of its points.

**Theorem.** The capacity is countably subadditive, $\operatorname{cap}(B_r) = r^{n-2}\operatorname{cap}(B_1)$ for $n\geq3$ and the ball of radius $r$, and for $n\geq3$ a set is polar if and only if it has zero capacity; a set with $\dim_{\mathcal H}E<n-2$ is polar, a polar set has $\dim_{\mathcal H}E\leq n-2$ and is consequently of Lebesgue measure zero, and the countable union of polar sets is polar. Moreover a compact set is removable for the bounded harmonic functions of the region outside it — every function harmonic and bounded off the set extends across it — exactly when its capacity is zero, and no set of positive capacity has this property.

**Proof sketch.** The subadditivity follows from the definition of capacity as an infimum of energies; the scaling law is a change of variable in the defining integral; the characterisation of polar sets by zero capacity combines the Frostman theorem with the definition of polarity, and the dimension statements follow from the energy criterion for a measure with finite kernel integral, since a probability measure of finite energy requires the Hausdorff dimension of its support to be at least the exponent of the kernel. The removability statement is the removable singularity theorem applied with the potential of an equilibrium measure concentrated on the set. $\square$

**Theorem (Riesz decomposition).** Let $n\geq3$ and let $v\geq0$ be superharmonic and finite on $\mathbb{R}^n$. Then $v = U^\mu+h$, where $\mu$ is the Riesz measure of $v$, supported on the set where $v$ is not harmonic, and $h$ is the greatest harmonic minorant of $v$; the measure is recovered from $v$ by testing against $\Delta\varphi$ for $\varphi$ of class $C_c^\infty$.

**Proof sketch.** The functional $\varphi\mapsto\int v\Delta\varphi$ is positive, by the superharmonicity and the maximum principle, and therefore is represented by a positive measure $\mu$ by the Riesz representation theorem; the difference $v-U^\mu$ is then harmonic, and its maximality follows from the maximum principle. $\square$

### The Wiener Criterion

**Theorem (Wiener's criterion).** Let $\Omega$ be a domain and $\zeta_0\in\partial\Omega$. Then $\zeta_0$ is a **regular** boundary point for the Dirichlet problem — every solution constructed by Perron's method attains its boundary data continuously at $\zeta_0$ — if and only if
$$
\sum_{k\geq1}2^{k(n-2)}\operatorname{cap}\bigl(\Omega^{\mathsf c}\cap\{2^{-k}\leq\lvert x-\zeta_0\rvert\leq2^{-k+1}\}\bigr) = +\infty
$$
for $n\geq3$, with the logarithmic modification of the summands in the plane. Equivalently, $\zeta_0$ is regular exactly when the complement $\Omega^{\mathsf c}$ is not thin at $\zeta_0$ in the fine topology, which is the geometric form of the same divergence condition. In particular every point of a boundary that satisfies the exterior cone condition is regular, points of a smooth boundary are regular, and an isolated point of the boundary is never regular, in accordance with the removable singularity theorem.

**Proof sketch.** The test is proved by constructing a barrier at $\zeta_0$ from the equilibrium measures of the parts of the complement in the dyadic annuli; the divergence of the series is exactly the condition under which the potentials of those measures can be combined with weights summing to a finite barrier. The necessity is proved by the converse construction, in which the divergence of the series is used to bound the Perron function below by a positive amount. $\square$

**Remark (why the criterion is a capacity statement).** The exponent $k(n-2)$ compensates the scaling law of the capacity: the capacity of the part of the complement at distance $2^{-k}$ from the point is at most $2^{-k(n-2)}$ times a constant depending on the dimension, so the series compares the set with the critical scaling at which the potential of the equilibrium measure is exactly of the size that a barrier requires. This is the sense in which the solvability of the Dirichlet problem is measured by a capacity rather than by a dimension: a set of Hausdorff dimension greater than $n-2$ is thick and the series diverges, a set of dimension smaller than $n-2$ is thin and the series converges, and at the critical dimension $n-2$ the divergence test is the finer one, deciding the cases that dimension alone cannot.

## Perron's Method and Regular Boundary Points

### Subharmonic Functions and the Perron Family

**Definition.** An upper semicontinuous function $v:\Omega\to[-\infty,+\infty)$ is **subharmonic** if for every ball $B(x,r)\subseteq\Omega$
$$
v(x)\leq\frac{1}{\sigma_{n-1}r^{n-1}}\int_{\partial B(x,r)}v\,d\sigma ,
$$
and **superharmonic** if $-v$ is subharmonic; a function that fails to be finite at a single point or that fails to be upper semicontinuous is allowed, with the convention that an upper semicontinuous function with values in $[-\infty,+\infty)$ satisfies the inequality only where it is finite.

**Theorem.** A function $v\in C^2$ is subharmonic if and only if $\Delta v\geq0$; the sum of two subharmonic functions is subharmonic; the pointwise maximum of two is subharmonic; a subharmonic function satisfies the maximum principle; and a subharmonic function on a ball whose boundary values are bounded above by a harmonic function is bounded above by it on the whole ball — the **comparison principle**.

**Proof sketch.** For a $C^2$ function the mean value over a small sphere expands as $v(x)+\frac{r^2}{2n}\Delta v(x)+O(r^4)$, so the inequality for all small $r$ is equivalent to $\Delta v\geq0$. The comparison principle follows from the maximum principle applied to the difference, the difference being subharmonic and with nonpositive boundary values. $\square$

**Theorem (Perron).** Let $\Omega$ be a bounded domain and $f\in C(\partial\Omega)$. Let
$$
\mathcal{P}(f) = \{\,v : v\ \text{subharmonic on }\Omega,\ \limsup_{y\to\zeta}v(y)\leq f(\zeta)\ \text{for all }\zeta\in\partial\Omega\,\},
$$
and let $u(x) = \sup_{v\in\mathcal{P}(f)}v(x)$, the **Perron function**. Then $\mathcal{P}(f)$ is nonempty, $u$ is finite and harmonic on $\Omega$, and $u$ is the unique harmonic function on $\Omega$ whose boundary values do not exceed $f$ and which is largest with this property; and $u$ solves the Dirichlet problem with data $f$ if and only if $\lim_{y\to\zeta}u(y) = f(\zeta)$ at every $\zeta\in\partial\Omega$.

**Proof sketch.** The family is nonempty because a sufficiently negative constant belongs to it. A locally bounded above subharmonic function can be replaced by the harmonic function with the same boundary values on a small ball — the **harmonic correction** — which increases it without leaving the family, so the supremum can be taken over functions each of which is harmonic on a neighbourhood of the point at which the value is evaluated. A direct compactness and harmonicity argument with Harnack's principle then shows that $u$ satisfies the mean value property on an arbitrary ball inside $\Omega$, hence is harmonic; and a harmonic function has the required boundary inequalities, hence is the largest such. The last statement is the definition of the regularity of the boundary point. $\square$

**Theorem (the barrier criterion).** A boundary point $\zeta_0$ is regular if and only if there is a **barrier** at $\zeta_0$: a superharmonic function $w$ on $\Omega$, bounded below, with $\lim_{y\to\zeta_0}w(y) = 0$ and $\liminf_{y\to\zeta}w(y)>0$ for every $\zeta\in\partial\Omega\setminus\{\zeta_0\}$. Points satisfying the exterior cone condition, and points of a $C^1$ boundary, admit a barrier, hence are regular; an isolated boundary point never admits one, which is the removable singularity theorem stated in boundary form.

**Proof sketch.** The barrier is used to compare the Perron function with the data at $\zeta_0$: the function $f(\zeta_0)+\epsilon w$ is a supersolution whose values near $\zeta_0$ are arbitrarily close to those of the data, and the comparison principle applied inside a small ball gives the continuity at $\zeta_0$. Conversely, a regular point yields a barrier as the harmonic correction of a suitable function constructed from the Perron family. $\square$

### The Spherical Harmonics and the Relation to Fourier Analysis

**Theorem (the spherical harmonics).** The eigenvalues of the Laplace–Beltrami operator $\Delta_{S^{n-1}}$ on the unit sphere are $-k(k+n-2)$, $k = 0,1,2,\dots$, the eigenspace of the eigenvalue $-k(k+n-2)$ consisting of the restrictions to the sphere of the harmonic homogeneous polynomials of degree $k$, of dimension $\binom{n+k-1}{k}-\binom{n+k-3}{k-2}$; the eigenfunctions are the **spherical harmonics** $Y_{k,j}$, they are orthogonal in $L^2(S^{n-1})$, and they are complete.

**Proof sketch.** A homogeneous polynomial $p$ of degree $k$ that is harmonic satisfies, by the computation of the Laplacian in polar coordinates $\Delta = \partial_r^2+\frac{n-1}{r}\partial_r+\frac{1}{r^2}\Delta_{S^{n-1}}$ applied to $r^kp(\zeta)$, the eigenrelation $\Delta_{S^{n-1}}p = -k(k+n-2)p$ on the sphere; conversely an eigenfunction that is a polynomial restriction is harmonic because the radial part of the Laplacian annihilates $r^k$ times it. The dimension count is the difference of the dimensions of the spaces of homogeneous polynomials of degree $k$ and of degree $k-2$, and the completeness is the spectral theorem for the compact self-adjoint operator obtained from the inverse of $-\Delta_{S^{n-1}}$, together with the density of the restrictions of polynomials in $L^2(S^{n-1})$. $\square$

**Remark (the Poisson kernel and the transform).** The Poisson kernel of the ball is the generating function of the spherical harmonics: in the plane with $\zeta = e^{i\varphi}$ and $x = re^{i\theta}$,
$$
P(x,\zeta) = \sum_{k\in\mathbb{Z}}r^{\lvert k\rvert}e^{ik(\theta-\varphi)} ,
$$
so the Poisson integral is the Fourier series of the boundary data evaluated through the Abel means, and the Poisson kernel is the Abel kernel of the circle. On $\mathbb{R}^n_+$ the Poisson kernel of the half-space is the Fourier transform of the multiplier $e^{-2\pi\lvert\xi\rvert y}$, so the solution of the Dirichlet problem on the half-space is, by the theory of *Fourier Analysis on Euclidean Spaces*, the Fourier multiplier $e^{-2\pi y\lvert\xi\rvert}$ applied to the boundary data — the same statement as the fact that the heat semigroup diagonalises the Laplacian, with the exponential decay replaced by the exponentially decaying multiplier. The potential theory of the sphere as a homogeneous space, with the harmonics as the matrix coefficients of the rotation group, belongs to the harmonic analysis of the neighbouring category of this Part, written in parallel; the pointwise content is the theorem above.

## Summary

A harmonic function on an open set is a $C^2$ function annihilated by the Laplacian, equivalently a continuous function satisfying the mean value property over every ball or sphere; harmonic functions are smooth, satisfy the strong maximum principle and the Liouville theorem, obey Harnack's inequality $\sup_Ku\leq C_K\inf_Ku$ for nonnegative harmonic functions on compact subsets, and the Harnack convergence principle; singularities of sufficient weakness are removable. The Dirichlet problem for the unit ball is solved by the Poisson integral with kernel $(1-\lvert x\rvert^2)/\lvert x-\zeta\rvert^n$, which is harmonic, positive and normalised to $1$, so that the Poisson family is an approximate identity on the sphere and the integral of continuous boundary data is the unique harmonic function with those values; on a smoothly bounded domain the solution is written with the boundary derivative of the Green function, and the symmetry of the Green function follows from Green's identity. A finite measure has a lower semicontinuous Newtonian potential, superharmonic off its support, and an energy; the equilibrium measure of a compact set of positive capacity exists, by the direct method applied to the energy, and its potential is constant on the set, by the theorem of Frostman; the capacity $\inf\{\int\lvert\nabla f\rvert^2\}$ is countably subadditive, scales as the $(n-2)$-th power of the radius, and vanishes exactly on the polar sets, so that a set of Hausdorff dimension less than $n-2$ is polar and a polar set has dimension at most $n-2$; the removable sets for the bounded harmonic functions are exactly the sets of capacity zero; and the Wiener criterion states that a boundary point is regular exactly when the series of the capacities of the dyadic pieces of the complement diverges, equivalently exactly when the complement is not thin at the point in the fine topology of Cartan. The Dirichlet problem on a general domain is solved by Perron's method, whose Perron function is the supremum of the subharmonic functions below the boundary data and is harmonic; a boundary point is regular — the data are attained — exactly when a barrier exists there, equivalently exactly when the Wiener series diverges, a condition that compares the complement of the domain with the critical scaling at every dyadic length. The spherical harmonics are the restrictions of the harmonic homogeneous polynomials, the eigenfunctions of the Laplace–Beltrami operator with eigenvalues $-k(k+n-2)$, and the Poisson kernel is their generating function, so that the Dirichlet problem on the ball is the theory of the Abel means of the boundary data and the potential theory of the half-space is the theory of the Fourier multiplier $e^{-2\pi y\lvert\xi\rvert}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Delta$ | Laplacian on $\mathbb{R}^n$ |
| $N(x)$ | Newtonian kernel |
| $u$, $v$, $w$ | Harmonic, subharmonic, superharmonic functions |
| $B(x,r)$, $\omega_n$, $\sigma_{n-1}$ | Ball, volume of the unit ball, surface measure of the unit sphere |
| $P(x,\zeta)$ | Poisson kernel of the ball |
| $G(x,y)$ | Green function of the domain |
| $U^\mu$, $I(\mu)$ | Newtonian potential and energy of the measure $\mu$ |
| $\operatorname{cap}(K)$, $\operatorname{cap}_2(K)$ | Capacity and energy capacity of the set $K$ |
| $\dim_{\mathcal H}E$ | Hausdorff dimension of a set |
| $\mathcal{P}(f)$, $u$ | Perron family and Perron function |
| $Y_{k,j}$, $\Delta_{S^{n-1}}$ | Spherical harmonics and the Laplace–Beltrami operator |







## Further Reading

- Naum S. Landkof, *Foundations of Modern Potential Theory* (Springer, 1972), for the classical theory of potentials, energies, capacity and the Wiener criterion.
- Lester L. Helms, *Potential Theory* (Springer, 2009), for the systematic treatment of harmonic and superharmonic functions, the Dirichlet problem and capacity.
- Marcel Brelot, *Éléments de la théorie classique du potentiel* (4th ed., Centre de Documentation Universitaire, 1969), for the Perron method, the fine topology and the barrier criterion.
- Oliver Dimon Kellogg, *Foundations of Potential Theory* (Springer, 1929), for the classical Dirichlet problem and the Poisson integral.
- David Gilbarg and Neil S. Trudinger, *Elliptic Partial Differential Equations of Second Order* (2nd ed., Springer, 1983), for the maximum principles, the barriers and the regularity theory of the elliptic boundary problem.
- Norbert Wiener, *The Dirichlet problem* (Journal of Mathematics and Physics 3, 1924), for the original form of the criterion named after him.
- Elias M. Stein and Guido Weiss, *Introduction to Fourier Analysis on Euclidean Spaces* (Princeton University Press, 1971), for the Poisson kernel, the conjugate function and the spherical harmonics.
- Claus Müller, *Spherical Harmonics* (Springer, 1966), for the spherical harmonics, their dimensions and the addition theorem.
- Pertti Mattila, *Geometry of Sets and Measures in Euclidean Spaces* (Cambridge University Press, 1995), for the Hausdorff dimension and the energy criterion used in the description of the polar sets.
