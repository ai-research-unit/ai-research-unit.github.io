
# __Geometric Measure Theory__

## Introduction

Geometric measure theory measures the subsets of $\mathbb{R}^n$ that are not open, not closed and not smooth — a surface, a curve, a Cantor set, the boundary of a set of finite perimeter — and it does so with a measure that is built to see dimension. The Lebesgue measure of a two-dimensional surface in $\mathbb{R}^3$ is zero and says nothing about it; the $m$-dimensional **Hausdorff measure** $\mathcal{H}^m$ assigns to a set the sum of the diameters of a covering, raised to the power $m$ and minimised, and thereby recovers the area of a surface, the length of a curve and a genuine number for a fractal. The **Hausdorff dimension** is the exponent at which this measure jumps from $+\infty$ to $0$, and it is the first coarse invariant of a set; the covering argument that computes it is also the proof of the **Frostman lemma**, that a set of positive $\mathcal{H}^m$ measure carries a measure with a controlled growth of mass, which is the same as saying that its capacity at the exponent $m$ is positive, in the sense of the potential theory of the previous article.

On a rectifiable set, that is a set that is the Lipschitz image of a piece of $\mathbb{R}^m$ up to a set of measure zero, the abstract measure becomes a calculus. The **area formula** states that the integral of the $m$-dimensional Jacobian of a Lipschitz map over the domain equals the integral over the target of the multiplicity of the map against $\mathcal{H}^m$ — the change of variables theorem for maps that are only Lipschitz, which is what one has, since by Rademacher's theorem the Jacobian exists almost everywhere; the **coarea formula** is its dual, expressing the integral of the Jacobian as the integral over the level sets of the $(n-m)$-dimensional measure — the Fubini theorem for nonlinear maps, and the tool by which the distribution function of a function is turned into the measure of its level sets, hence into the isoperimetric inequality. A set of finite $\mathcal{H}^m$ measure that has an approximate tangent $m$-plane at almost every point is rectifiable, and **Federer's structure theorem** states that a set of finite $\mathcal{H}^m$ measure splits into a rectifiable part and a purely unrectifiable part, the latter invisible to almost every orthogonal projection; the classical example of the second kind is the Besicovitch set.

The last part of the article is the existence theory for surfaces of least area. A **current** is the integration of differential forms over an oriented rectifiable set; its mass is the $\mathcal{H}^m$ measure of the set, weighted by the multiplicity, and its boundary is defined by Stokes' theorem, so that the boundary of a current is the current of the boundary when the set has one. The **compactness theorem** of Federer and Fleming, that a sequence of currents with uniformly bounded mass and boundary mass has a convergent subsequence in the flat norm, together with a polyhedral approximation, gives the solution of the **Plateau problem**: a current of least mass among those with prescribed boundary. The regularity of the minimiser — the interior smoothness away from a singular set of small dimension — is the content of the theorems of Allard and Almgren and of De Giorgi for the sets of finite perimeter, and it belongs to the minimal surface theory of the later categories of this Part, to which the last section points.

The prerequisites are *Measure Theory and Integration* for the measure, the integral, the Riesz representation theorem and the differentiation theory; *Modes of Convergence* for the lower semicontinuity and convergence statements on which the existence theorems rest; *Descriptive Set Theory* for the Borel and analytic structure of the sets considered, the analyticity of the projections and the measurability of the sets of finite measure; *Convex Analysis* for the convexity of the mass and the separation arguments; and *Nonsmooth and Variational Analysis* for Rademacher's theorem, the metric differentiability and the direct method in the form used here. The functional-analytic setting of the currents — the topological dual of the smooth forms, the weak topologies, the compactness in Sobolev spaces — belongs to later categories of this Part, and so does the minimal surface theory; the statements here are the geometric ones, with the analytic framework cited as standard.

## Hausdorff Measure and Dimension

### The Carathéodory Construction

**Definition.** For $s\geq0$ let $\omega_s = \pi^{s/2}/\Gamma(s/2+1)$, the volume of the unit ball of $\mathbb{R}^s$ when $s$ is an integer, and let $\beta_s = \omega_s/2^s$. For $\delta>0$ and $E\subseteq\mathbb{R}^n$ let
$$
\mathcal{H}^s_\delta(E) = \inf\Bigl\{\sum_j\beta_s(\operatorname{diam}C_j)^s : E\subseteq\bigcup_jC_j,\ \operatorname{diam}C_j\leq\delta\Bigr\}, \qquad \mathcal{H}^s(E) = \sup_{\delta>0}\mathcal{H}^s_\delta(E),
$$
the **Hausdorff $s$-measure** of $E$; it is an outer measure, it is Borel regular, and $\mathcal{H}^0$ is the counting measure. The normalising constant $\beta_s$ is chosen so that $\mathcal{H}^m$ agrees with the $m$-dimensional Lebesgue measure on the $m$-planes of $\mathbb{R}^n$; the unnormalised content $\sum_j(\operatorname{diam}C_j)^s$ of *Fractal Geometry* differs from the measure by the factor $\beta_s$, which is immaterial for the dimension, that dimension being a ratio of logarithms.

**Theorem.** $\mathcal{H}^n = \mathcal{L}^n$ on $\mathbb{R}^n$; the measure scales as $\mathcal{H}^s(\lambda E) = \lambda^s\mathcal{H}^s(E)$ for $\lambda>0$; and for an integer $m$ and an $m$-dimensional plane $V$ one has $\mathcal{H}^m(V\cap B(x,r)) = \omega_mr^m$, so that the scaling exponent of a measure detecting an $m$-dimensional object is $m$. Moreover $\mathcal{H}^m$ of a smooth $m$-dimensional submanifold is its $m$-dimensional surface measure, so that in particular $\mathcal{H}^{n-1}$ of the sphere of radius $r$ in $\mathbb{R}^n$ is $\sigma_{n-1}r^{n-1}$, the surface area of *Potential Theory*.

**Proof sketch.** The comparison with the Lebesgue measure rests on the **isodiametric inequality**, that among the sets of a given diameter the ball has the largest volume, which is proved by symmetrisation: the volume of a set is at most $\omega_n(\operatorname{diam}E/2)^n = \beta_n(\operatorname{diam}E)^n$. Given that, every admissible cover of $E$ satisfies $\sum_j\beta_n(\operatorname{diam}C_j)^n\geq\sum_j\mathcal{L}^n(C_j)\geq\mathcal{L}^n(E)$, whence $\mathcal{H}^n(E)\geq\mathcal{L}^n(E)$; conversely a cover of $E$ by small balls of radii $\rho_j$ with $\sum_j\mathcal{L}^n(B_j)$ close to $\mathcal{L}^n(E)$ has $\sum_j\beta_n(2\rho_j)^n = \sum_j\omega_n\rho_j^n = \sum_j\mathcal{L}^n(B_j)$, whence $\mathcal{H}^n(E)\leq\mathcal{L}^n(E)$. The two inequalities give the identity. $\square$

**Definition.** The **Hausdorff dimension** of $E$ is $\dim_{\mathcal H}E = \inf\{s : \mathcal{H}^s(E) = 0\} = \sup\{s : \mathcal{H}^s(E) = +\infty\}$; it satisfies $\dim_{\mathcal H}\bigcup_jE_j = \sup_j\dim_{\mathcal H}E_j$, is monotone, is invariant under Lipschitz maps in the sense that $\dim_{\mathcal H}f(E)\leq\dim_{\mathcal H}E$ for Lipschitz $f$, and for a countable set is $0$.

**Example.** The middle-thirds Cantor set is covered, at the stage $k$ of its construction, by $2^k$ intervals of length $3^{-k}$, so $\mathcal{H}^s$ is finite and positive exactly at $s = \log2/\log3 = 0.6309\ldots$ and the dimension equals that value; the computation of the covering numbers $\log(2^k)/\log(3^k)$ gives $0.6309$ for $k = 1,\dots,4$. The Sierpiński gasket is covered by exactly $3^k$ of its constituent triangles at scale $2^{-k}$, giving dimension $\log3/\log2 = 1.5849\ldots$; the numerical count of the squares of a dyadic grid of side $2^{-k}$ that meet the gasket gives $355$ at $k = 5$ and $29391$ at $k = 9$, with $\log(\text{count})/\log2^k$ equal to $1.6943$ and $1.6492$ — approaching the exact value from above as the grid refines, since the covering number overestimates the triangle count by a bounded factor where a square grid is not adapted to the triangular self-similarity.

### The Frostman Lemma, Projections and Slices

**Theorem (Frostman).** For $E\subseteq\mathbb{R}^n$ Borel and $s>0$ the following are equivalent up to constants: $\mathcal{H}^s(E)>0$; there is a positive Borel measure $\mu$ on $E$ with $\mu(E)>0$ and $\mu(B(x,r))\leq r^s$ for all $x$ and all $r>0$; and $\dim_{\mathcal H}E\geq s$.

**Proof sketch.** A measure with the growth condition distributes the mass of a set of dimension less than $s$ in a way that contradicts the countable additivity, whence the dimension bound. Conversely, from $\mathcal{H}^s(E)>0$ one defines a pre-measure by the restriction of the covering measure to a bounded part of $E$ and averages it over the scales, producing a measure with the growth bound. $\square$

**Theorem (Marstrand; Mattila).** Let $E\subseteq\mathbb{R}^n$ be Borel with $\dim_{\mathcal H}E = s$. Then for almost every $(n-m)$-dimensional subspace $V$, $\dim_{\mathcal H}\pi_V(E) = \min(s,m)$ where $\pi_V$ is the orthogonal projection; and for almost every $x\in\mathbb{R}^n$, $\dim_{\mathcal H}(E\cap(E+x))\geq2s-n$. Equivalently, a set of dimension $s$ with $s>n-m$ meets almost every translate of an $m$-plane in a set of dimension at least $s-(n-m)$ — the **slicing** statement.

**Proof sketch.** The projection is Lipschitz, so it cannot increase the dimension; the lower bound is proved by the energy method: a measure with finite $s$-energy pushes to a measure on the projection with finite $t$-energy for $t<\min(s,m)$, and the finiteness of the energy bounds the dimension from below. The intersection statement is proved by integrating the growth condition of the Frostman measure over the translates, using the Fubini theorem of *Measure Theory and Integration*. $\square$

## The Area and Coarea Formulae

### Lipschitz Maps and the $m$-Jacobian

**Definition.** For a Lipschitz $f:\mathbb{R}^m\to\mathbb{R}^n$ with $m\leq n$, differentiable at $x$, the **$m$-Jacobian** is
$$
J_mf(x) = \sqrt{\det\bigl(\nabla f(x)^{\mathsf T}\nabla f(x)\bigr)},
$$
the $m$-dimensional volume of the image of the unit $m$-cube under the differential.

**Theorem (area formula).** Let $f:\mathbb{R}^m\to\mathbb{R}^n$ be Lipschitz and let $A\subseteq\mathbb{R}^m$ be $\mathcal{L}^m$-measurable. Then
$$
\int_AJ_mf\,dx = \int_{\mathbb{R}^n}\mathcal{H}^0\bigl(A\cap f^{-1}(y)\bigr)\,d\mathcal{H}^m(y),
$$
and more generally $\int_A\varphi(f(x))J_mf(x)dx = \int\varphi(y)N(f,A,y)d\mathcal{H}^m(y)$ for Borel $\varphi\geq0$, where $N(f,A,y)$ is the number of preimages in $A$.

**Proof sketch.** For an injective $C^1$ map the formula is the change of variables theorem, with the Jacobian given by the Gram determinant; for a Lipschitz map, Rademacher's theorem gives the differential almost everywhere, and the formula is obtained by decomposing the domain into countably many pieces on each of which $f$ is a small perturbation of its affine approximation with an error controlled by the integrability of the Lipschitz constant and the Vitali–Besicovitch covering theorem; the multiplicity is what accounts for the failure of injectivity, and the countability of the preimages almost everywhere follows from the area formula applied to a small ball around each point. $\square$

**Example.** For the linear map $f(x,y) = (x+y,x-y)$ on the unit square, $\nabla f$ is the matrix with rows $(1,1)$ and $(1,-1)$, so $\nabla f^{\mathsf T}\nabla f = 2I$ and $J_2f = 2$; the image is the parallelogram with vertices $(0,0),(1,1),(2,0),(1,-1)$ of area $2$, in agreement with the area formula. For the parametrisation of the sphere the Jacobian is the surface element and its integral is $4\pi$, the area of the sphere.

### The Coarea Formula

**Theorem (coarea formula).** Let $f:\mathbb{R}^n\to\mathbb{R}^m$ be Lipschitz with $m\leq n$ and let $A$ be $\mathcal{L}^n$-measurable. Then
$$
\int_AJ_mf\,dx = \int_{\mathbb{R}^m}\mathcal{H}^{n-m}\bigl(A\cap f^{-1}(y)\bigr)\,dy .
$$
**Proof sketch.** The formula is the area formula applied to the map $F(x) = (f(x),x)$ from $\mathbb{R}^n$ to $\mathbb{R}^m\times\mathbb{R}^{n-m}$, whose Jacobian equals $J_mf$; the level sets of $f$ are the images of the fibres of the projection in the product, and the area formula for $F$ expresses the integral over the domain as the integral over the target, in which the slices appear. $\square$

**Example (polar coordinates and the isoperimetric inequality).** For $f(x) = \lvert x\rvert$ on $\mathbb{R}^n$ one has $J_1f = 1$ and the level set is the sphere of radius $r$, so the formula gives the polar coordinate identity $\int_{\mathbb{R}^n}g(\lvert x\rvert)dx = \sigma_{n-1}\int_0^\infty g(r)r^{n-1}dr$. For a set $E$ of finite perimeter — a set whose characteristic function has distributional derivative a finite measure — the coarea formula applied to the distance function from $E$ relates the perimeter to the $\mathcal{H}^{n-1}$ measures of the level sets, and the **isoperimetric inequality** $\mathcal{H}^{n-1}(\partial E)\geq n\omega_n^{1/n}\mathcal{L}^n(E)^{(n-1)/n}$ is obtained by combining the coarea formula with the Brunn–Minkowski inequality or with the Sobolev inequality; the equality case is the ball.

**Theorem (the fibres of a Lipschitz map; the Eilenberg inequality).** For a Lipschitz $f:\mathbb{R}^n\to\mathbb{R}^m$ and a Borel set $E$ the level sets $E\cap f^{-1}(y)$ are countably $\mathcal{H}^{n-m}$-rectifiable for almost every $y$, and more generally for a Lipschitz map between metric spaces the **Eilenberg inequality** bounds the average size of the fibres by the Hausdorff measure of the domain; this is the sense in which the coarea formula is the Fubini theorem for nonlinear level sets.

**Proof sketch.** The rectifiability of the level sets is the Whitney extension and implicit function theorem applied on the pieces where the differential of $f$ has full rank, the complement of those pieces contributing a set of measure zero by the area formula. $\square$

## Rectifiable Sets

### Approximate Tangents and Densities

**Definition.** A set $E\subseteq\mathbb{R}^n$ is **countably $\mathcal{H}^m$-rectifiable** if there are Lipschitz maps $f_j:\mathbb{R}^m\to\mathbb{R}^n$ with $\mathcal{H}^m\bigl(E\setminus\bigcup_jf_j(\mathbb{R}^m)\bigr) = 0$; it is **$\mathcal{H}^m$-rectifiable** if in addition $\mathcal{H}^m(E)<\infty$. A **rectifiable set** is a countably rectifiable set, together with the convention that all the statements below hold up to a set of $\mathcal{H}^m$ measure zero.

**Definition.** The $m$-dimensional **approximate tangent plane** of $E$ at $x$ is the subspace $T$ such that the blow-ups $(E-x)/r$ converge to $T$ in the sense of the weak* convergence of the measures $\mathcal{H}^m\llcorner E$: precisely, $\mathcal{H}^m\llcorner E$ scaled to the unit ball converges to $\mathcal{H}^m\llcorner T$ locally; the **density** is $\Theta^m(E,x) = \lim_{r\downarrow0}\mathcal{H}^m(E\cap B(x,r))/(\omega_mr^m)$ when the limit exists.

**Theorem.** A countably $\mathcal{H}^m$-rectifiable set has an approximate tangent $m$-plane at $\mathcal{H}^m$-almost every point of $E$, unique, and the density exists and equals $1$ at $\mathcal{H}^m$-almost every point; conversely, if $\mathcal{H}^m(E)<\infty$ and the density $\Theta^m(E,x)$ exists and is finite and positive at $\mathcal{H}^m$-almost every point, then $E$ is rectifiable, by the theorem of Preiss.

**Proof sketch.** For the forward direction one uses that a Lipschitz image has the tangent plane of the image of the differential wherever the differential has rank $m$, which holds almost everywhere by Rademacher, and that the multiplicity is countable almost everywhere by the area formula; the density statement is the behaviour of the $\mathcal{H}^m$ measure of a Lipschitz image near a point of full rank. The converse uses the growth bound of the measure obtained from the density and the projection theorem to produce a Lipschitz graph over a positive measure set of directions. $\square$

**Theorem (the differentiation theory, and Lebesgue points on a rectifiable set).** Let $\mu$ be a Radon measure on $\mathbb{R}^n$ and $f\in L^1_{\mathrm{loc}}(\mu)$. Then
$$
\lim_{r\downarrow0}\frac{1}{\mu(B(x,r))}\int_{B(x,r)}f\,d\mu = f(x)
$$
for $\mu$-almost every $x$ — the **Lebesgue–Besicovitch differentiation theorem**, obtained by replacing the Vitali covering theorem of the Euclidean theory by the **Besicovitch covering theorem**, which applies to arbitrary Radon measures. Moreover, if $E$ is countably $\mathcal{H}^m$-rectifiable then $\Theta^m(\mathcal{H}^m\llcorner E,x) = 1$ at $\mathcal{H}^m$-almost every point of $E$, so that $\mathcal{H}^m$-almost every point of $E$ is a Lebesgue point of $\mathcal{H}^m\llcorner E$.

**Proof sketch.** The Besicovitch covering theorem gives a covering of a set by balls with a bounded number of families, each consisting of pairwise disjoint balls, which is what the proof of the differentiation theorem needs in place of the doubling hypothesis; the density statements follow from the differentiation theorem applied to the indicator of the set. $\square$

### The Structure of Sets of Finite Measure

**Theorem (Federer's structure theorem).** Let $E\subseteq\mathbb{R}^n$ have $\mathcal{H}^m(E)<\infty$. Then $E$ decomposes as $E = R\cup P$ with $R$ rectifiable and $P$ **purely unrectifiable**, meaning that $\mathcal{H}^m(P\cap f(\mathbb{R}^m)) = 0$ for every Lipschitz $f:\mathbb{R}^m\to\mathbb{R}^n$; the decomposition is unique up to $\mathcal{H}^m$-null sets.

**Proof sketch.** The set of points at which the density does not exist, or is not $1$, or where the approximate tangent plane fails to exist, carries a set that can be covered by Lipschitz graphs only in a null part: the density-differentiation theorem produces the rectifiable part, and the failure of the tangent plane is what forces pure unrectifiability. $\square$

**Theorem (the projection criterion of Besicovitch and Marstrand).** A set $E$ with $0<\mathcal{H}^m(E)<\infty$ is purely unrectifiable if and only if $\mathcal{H}^m(\pi_V(E)) = 0$ for almost every $(n-m)$-dimensional subspace $V$; consequently the projection behaviour detects rectifiability.

**Proof sketch.** A rectifiable set has a tangent plane almost everywhere, so its projection onto $V$ has positive measure for almost every $V$; the converse is the hard direction, proved by the theory of the tangent planes and the integral-geometric inequalities: if the projections are null in almost every direction, the measure cannot be concentrated on a set with an approximate tangent plane, so the set is purely unrectifiable. $\square$

**Example (the four-corner Cantor set and the Kakeya set).** The four-corner Cantor set — the self-similar set obtained from the unit square by replacing it by the four corner squares of side $\frac14$ and iterating — has $0<\mathcal{H}^1(E)<\infty$, and by the theorem of Kenyon its projection on a line making angle $\theta$ with the horizontal has positive length exactly when $\tan\theta$ is rational and is null otherwise; the exceptional directions forming a countable set, the criterion applies and the set is purely unrectifiable. This is Besicovitch's example of a purely unrectifiable set of finite linear measure. A set of zero area, on the other hand, need not be small: the **Kakeya set** of Besicovitch has Lebesgue measure zero and contains a unit segment in *every* direction, so its projections have positive length in every direction and its $\mathcal{H}^1$ measure is infinite; the projection criterion, which is a statement about the sets of finite $\mathcal{H}^m$ measure, therefore does not apply to it.

**Theorem (the rectifiability of the boundary of a set of finite perimeter; De Giorgi).** If $E\subseteq\mathbb{R}^n$ is a set of finite perimeter, then the reduced boundary $\partial^*E$ — the set of points where the density of $E$ in the ball is $\frac12$ in the limiting sense and the normal of the perimeter measure exists — is countably $\mathcal{H}^{n-1}$-rectifiable, and the perimeter equals $\mathcal{H}^{n-1}\llcorner\partial^*E$; moreover the **Gauss–Green theorem** holds for the sets of finite perimeter, with the integration by parts against the measure-theoretic boundary. This is the geometric content of the theory of functions of bounded variation, developed in the parallel articles on the function spaces of this Part.

**Proof sketch.** The coarea formula applied to the distance function from $E$ and the isoperimetric inequality for the slices give the existence of the tangent planes and the finite measure of the boundary; the rectifiability then follows from the structure theorem applied to $\partial^*E$. $\square$

## Currents and the Plateau Problem

### Currents, Mass and Boundary

**Definition.** For an open set $\Omega\subseteq\mathbb{R}^n$ the space of **$m$-dimensional currents** is the dual of the space $\mathcal{D}^m(\Omega)$ of smooth $m$-forms with compact support, with the topology of the test functions. A current of the form
$$
T(\omega) = \int_M\langle\omega(x),\xi(x)\rangle\,d\mathcal{H}^m(x)
$$
with $M$ countably rectifiable and $\xi$ an $L^1(M;\Lambda_m)$ field of $m$-vectors is written $[M,\xi]$ and called **rectifiable**; the **mass** is
$$
\mathbf{M}(T) = \sup_{\lvert\omega\rvert\leq1}T(\omega) = \int_M\lvert\xi\rvert\,d\mathcal{H}^m ,
$$
and the **boundary** is defined by Stokes' theorem, $(\partial T)(\omega) = T(d\omega)$. A current is **integral** if it and its boundary are rectifiable of finite mass; the **flat norm** is $\mathcal{F}(T) = \inf\{\mathbf{M}(A)+\mathbf{M}(B) : T = A+\partial B\}$.

**Theorem.** The boundary operator satisfies $\partial\partial = 0$; the mass is lower semicontinuous with respect to the flat convergence; a rectifiable current of finite mass has rectifiable boundary of finite mass when $\mathcal{H}^{m-1}(\partial M)$ is finite and the orientation matches, in which case $\partial[M,\xi] = [\partial M,\xi']$ with the induced orientation; and the mass is a convex functional of the current, so that the direct method of *Convex Analysis* applies to it.

**Proof sketch.** $\partial\partial = 0$ is $d^2 = 0$ for forms. The lower semicontinuity is the Banach–Steinhaus argument applied to the defining supremum. The identification of the boundary with the boundary of the set is the Stokes theorem for rectifiable currents, proved by smoothing the forms and applying the classical theorem on the pieces of the Lipschitz graphs. $\square$

**Definition.** The **first variation** of the mass at $T$ in the direction of a smooth vector field $X$ is $\delta\mathbf{M}(T)(X) = \frac{d}{dt}\bigl[\mathbf{M}((\chi_t)_\#T)\bigr]\big|_{t=0}$, where $\chi_t$ is the flow of $X$; a current is **stationary** if the first variation vanishes for every $X$, and a set of finite perimeter is **minimal** if it is stationary.

**Theorem (the monotonicity formula; the tangent cone).** A stationary integral current satisfies the monotonicity of the density ratios $\mathbf{M}(T\cap B(x,r))/(\omega_mr^m)\ \uparrow$; hence the density $\Theta^m(T,x)$ exists at every point, and the blow-ups of a stationary current at a point have a limit that is a stationary cone — the **tangent cone** of $T$ at $x$. A stationary current that is a cone and is smooth away from the origin is a minimal cone, and the possible singular tangent cones are the subject of the regularity theory.

**Proof sketch.** The first variation of the mass of a cone is computed explicitly and is nonnegative exactly when the cone is stationary; the monotonicity is the differential inequality obtained from the first variation formula for the radial vector field. $\square$

### The Compactness and Existence Theorems

**Theorem (Federer–Fleming compactness).** Let $\{T_j\}$ be integral currents in an open set with $\mathbf{M}(T_j)\leq M$ and $\mathbf{M}(\partial T_j)\leq M$ for a constant $M$, all supported in a common compact set. Then a subsequence converges in the flat norm to an integral current $T$ with $\mathbf{M}(T)\leq\liminf_j\mathbf{M}(T_j)$ and $\partial T = \lim\partial T_j$, and the convergence is also in the sense of the weak* convergence of the currents.

**Proof sketch.** The **deformation theorem** approximates a current by a polyhedral one with controlled loss of mass, so that the bound on the mass and the boundary controls the complexity of the approximation; the compactness is then the compactness of the space of polyhedral chains with bounded mass at each scale, together with a diagonal subsequence. The lower semicontinuity of the mass and the continuity of the boundary are the general properties of the flat convergence. $\square$

**Theorem (the solution of the Plateau problem).** Let $S$ be an integral $(m-1)$-current in $\mathbb{R}^n$ with compact support and $\partial S = 0$. Then there is an integral $m$-current $T$ with $\partial T = S$ and
$$
\mathbf{M}(T) = \inf\{\mathbf{M}(U) : U\ \text{integral},\ \partial U = S\} ,
$$
so that $T$ is a surface of least mass with the prescribed boundary; and $T$ is stationary, hence smooth outside a closed singular set of Hausdorff dimension at most $m-2$ in the interior by the regularity theorem of Almgren, whose boundary regularity is the theorem of Hardt and Simon. The class of fillings is nonempty because the cone over $S$ is an integral current with boundary $S$. The solution is the weak form of the classical minimal surface spanned by a curve, and in the case $m = 2$, $n = 3$ the mass-minimiser for a smooth Jordan curve is the classical minimal disc, whose existence is the theorem of Douglas and Radó.

**Proof sketch.** The class of currents with the prescribed boundary is nonempty — it contains the cone over the boundary, whose mass is bounded by a constant times that of $S$ — and the mass is lower semicontinuous on it; the compactness theorem gives a convergent minimising sequence, and the limit is an integral current with the same boundary by the continuity of the boundary operator, and with the mass not larger than the infimum by the lower semicontinuity. The stationarity follows because a displacement of the minimiser that decreases the mass would contradict minimality. $\square$

**Theorem (the isoperimetric inequality and the filling bound).** Let $S$ be an integral $(m-1)$-current in $\mathbb{R}^n$ with compact support and $\partial S = 0$. Then $S$ bounds an integral $m$-current $T$ with
$$
\mathbf{M}(T)\leq C\bigl(\mathbf{M}(S)\bigr)^{\frac{m}{m-1}} ,
$$
where $C = C(m,n)$, so that the minimiser of the Plateau problem has mass controlled by the mass of the boundary; and the singular set of the minimiser has Hausdorff dimension at most $m-2$ by the general regularity theory.

**Proof sketch.** The inequality is the Federer–Fleming isoperimetric inequality, proved from the compactness theorem by a scaling and contradiction argument; the filling bound is the consequence for the minimiser, and the dimension of the singular set is the theorem of Almgren, proved by the study of the tangent cones of the previous subsection and a stratification by the symmetry of the cone. $\square$

**Remark (the relation to minimal surfaces and varifolds).** The currents of this article are oriented, and the orientability is a real hypothesis: it excludes the surfaces that carry no orientation, and with them the classes of surfaces for which the mass alone does not control the topology. The **varifolds** of Almgren remove the orientation and give the existence theorem for stationary surfaces in the unoriented setting, with the first variation and the monotonicity formula as above and the **Allard regularity theorem** asserting that a stationary varifold with density close to $1$ is a smooth graph; and the **calibration method** of Federer exhibits the minimality of a surface by producing a closed form of comass one whose restriction to the surface attains the mass. The minimal surface theory of the later category of this Part — the classical theory of the second variation, the Bernstein theorem and its failure in high dimensions, the parametric and the non-parametric regularity, and the relation to the partial differential equations of the mean curvature — is developed .

## Summary

The Hausdorff $s$-measure of a set is the infimum over coverings by sets of diameter at most $\delta$ of the sum of the $s$-th powers of the diameters, normalised so that the measure of the unit ball is its volume, and the limit in $\delta$ is Borel regular; $\mathcal{H}^n = \mathcal{L}^n$ on $\mathbb{R}^n$ by the isodiametric inequality and the normalisation, $\mathcal{H}^{n-1}$ of the sphere of radius $r$ is its surface area $\sigma_{n-1}r^{n-1}$, and the Hausdorff dimension is the exponent at which the measure jumps from $+\infty$ to $0$ and is computed on self-similar sets by counting: the Cantor set has dimension $\log2/\log3$ and the Sierpiński gasket $\log3/\log2$. A set of positive $s$-measure carries a measure with the growth bound $\mu(B(x,r))\leq r^s$, by the Frostman lemma, and the projection and slice theorems of Marstrand and Mattila state that the projections of a set of dimension $s$ have dimension $\min(s,m)$ for almost every $m$-plane and that the slices of a set of dimension $s$ with an $m$-plane have dimension at least $s-(n-m)$ for almost every translate. For a Lipschitz map the $m$-Jacobian $J_mf = \sqrt{\det(\nabla f^{\mathsf T}\nabla f)}$ satisfies the area formula, expressing the integral over the domain as the integral of the multiplicity against $\mathcal{H}^m$, and the coarea formula, expressing it as the integral of $\mathcal{H}^{n-m}$ of the level sets; the polar coordinate formula, the isoperimetric inequality and the rectifiability of the level sets of a Lipschitz function are its consequences. A countably $\mathcal{H}^m$-rectifiable set has an approximate tangent plane and density $1$ almost everywhere, conversely a set of finite measure with positive finite density is rectifiable, by the theorem of Preiss, and Federer's structure theorem splits a set of finite $\mathcal{H}^m$ measure into a rectifiable part and a purely unrectifiable part, the latter characterised by the vanishing of almost every projection and exemplified by the four-corner Cantor set; the reduced boundary of a set of finite perimeter is rectifiable and carries the perimeter as its $\mathcal{H}^{n-1}$ measure, by De Giorgi's theorem. Currents are the integration of forms over oriented rectifiable sets, with the mass the weighted measure and the boundary defined by Stokes' theorem; the compactness theorem of Federer and Fleming and the polyhedral deformation theorem give the solution of the Plateau problem, the existence of an integral current of least mass with prescribed boundary, which is stationary, satisfies the isoperimetric bound, and is smooth outside a singular set of dimension at most $m-2$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{H}^s$, $\mathcal{H}^s_\delta$ | Hausdorff $s$-measure and its $\delta$-approximation |
| $\dim_{\mathcal H}E$ | Hausdorff dimension |
| $\omega_s = \pi^{s/2}/\Gamma(s/2+1)$, $\beta_s = \omega_s/2^s$ | Volume of the unit ball of $\mathbb{R}^s$, normalising constant |
| $\mathcal{L}^n$, $\omega_n$ | Lebesgue measure, volume of the unit ball |
| $\pi_V$ | Orthogonal projection onto the subspace $V$ |
| $J_mf$ | $m$-Jacobian of the Lipschitz map $f$ |
| $N(f,A,y)$ | Multiplicity of $f$ over $y$ on $A$ |
| $\Theta^m(E,x)$ | $m$-dimensional density of $E$ at $x$ |
| $\partial^*E$ | Reduced boundary of a set of finite perimeter |
| $\mathcal{D}^m(\Omega)$ | Smooth $m$-forms with compact support |
| $T$, $[M,\xi]$ | Current, rectifiable current |
| $\mathbf{M}(T)$, $\partial T$ | Mass and boundary of a current |
| $\mathcal{F}(T)$ | Flat norm |
| $\delta\mathbf{M}(T)$ | First variation of the mass |
| $(\chi_t)_\#$ | Push-forward of a current by a flow |





## Further Reading

- Herbert Federer, *Geometric Measure Theory* (Springer, 1969), for the definitive account of Hausdorff measure, the area and coarea formulae, rectifiability, currents and the structure theory.
- Herbert Federer and Wendell H. Fleming, *Normal and integral currents* (Annals of Mathematics 72, 1960), for the compactness theorem and the solution of the Plateau problem.
- Frank Morgan, *Geometric Measure Theory: A Beginner's Guide* (5th ed., Academic Press, 2016), for the introductory account of the currents, the deformation theorem and the Plateau problem.
- Pertti Mattila, *Geometry of Sets and Measures in Euclidean Spaces* (Cambridge University Press, 1995), for the Frostman lemma, the projection and slice theorems, and the rectifiability criteria.
- Kenneth J. Falconer, *The Geometry of Fractal Sets* (Cambridge University Press, 1986), for the Hausdorff dimension, the self-similar sets and the Besicovitch set.
- Lawrence C. Evans and Ronald F. Gariepy, *Measure Theory and Fine Properties of Functions* (rev. ed., CRC Press, 2015), for the area and coarea formulae, the differentiation theory and the sets of finite perimeter.
- Enrico Bombieri, *Regularity theory for almost minimal currents* (Archive for Rational Mechanics and Analysis 78, 1982), for the regularity of the minimisers of the Plateau problem.
- William K. Allard, *On the first variation of a varifold* (Annals of Mathematics 95, 1972), for the varifolds, the monotonicity formula and the regularity theorem.
- Frederick J. Almgren, *Almgren's Big Regularity Paper* (World Scientific, 2000), for the dimension bound on the singular set of a mass-minimising current.
- David Preiss, *Geometry of measures in $\mathbb{R}^n$: distribution, rectifiability, and densities* (Annals of Mathematics 125, 1987), for the criterion that a set of finite measure with positive finite density everywhere is rectifiable.
- Richard Kenyon, *Projecting the one-dimensional Sierpiński gasket* (Israel Journal of Mathematics 97, 1997), for the directions in which the four-corner Cantor set has null projection.
