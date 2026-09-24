
# __Nonsmooth and Variational Analysis__

## Introduction

A variational problem is the problem of minimising a functional, and the classical theory of the calculus of variations solves it by making the first variation vanish: a minimiser of a differentiable functional is a critical point, and the Euler–Lagrange equation is the resulting differential equation. The hypothesis that fails first, in the problems that arise in practice, is differentiability. The obstacle problem minimises the Dirichlet energy over the functions above a given obstacle, and the functional is smooth but the constraint set is not; the total variation functional $\int\lvert\nabla u\rvert$ is convex but not differentiable at the points where $\nabla u$ vanishes; a maximum of finitely many smooth functions is differentiable except on a set where the active functions change; and a cost function that is only Lipschitz has no derivative at all at the points where the minimisation takes place. The replacement for the derivative in all these cases is a set-valued generalisation of it, and the theory of that replacement is nonsmooth analysis.

Two constructions of the derivative set are in use, and the relation between them is the first thing to fix. The **Clarke subdifferential** of a locally Lipschitz function is the convex hull of the limits of the gradients at the points of differentiability, which exist almost everywhere by Rademacher's theorem; it is always a nonempty compact convex set, it satisfies a mean value theorem and a chain rule, and it is the correct object for the necessary conditions of Lipschitz programming. The **Fréchet subdifferential** is the set of vectors $v$ for which $f(u)\geq f(x)+\langle v,u-x\rangle+o(\lvert u-x\rvert)$; it may be empty even where the function is Lipschitz, it is generally not convex, and its limits at nearby points — the **limiting** or **Mordukhovich** subdifferential — is the object with the exact calculus: the sum rule and the chain rule hold under minimal hypotheses, and the necessary optimality conditions hold without a constraint qualification. The Clarke object is the convexification of the limiting one in the Lipschitz case, and each is the right tool for a different purpose: Clarke's for convex-valued necessary conditions and for the convex analysis of Lipschitz functions, the limiting one for exact calculus and for the coderivative.

The existence theory is the second half of the subject. **Ekeland's variational principle** states that a lower semicontinuous functional bounded below on a complete metric space has, for every $\epsilon>0$, a point that is within $\epsilon$ of the infimum and that minimises the perturbed functional $f(\cdot)+\epsilon d(x,\cdot)$; it is the substitute for compactness in problems where no minimiser need exist, it gives the approximate optimality conditions in the smooth and nonsmooth settings, and it implies the fixed point theorem of Caristi. The **metric regularity** of a set-valued map and its infinitesimal form, the coderivative condition of Mordukhovich, give the exact statements of the inverse and implicit function theorems for maps that are not single-valued or not differentiable, and the **extremal principle** is the separation theorem of the nonsmooth setting. The article closes with the direct method in the nonsmooth setting, the relaxation of a non-convex variational problem by its convex envelope and its lower semicontinuous envelope, the optimality conditions of nonsmooth programming in both the Clarke and the limiting forms, and the two model problems: the obstacle problem and the total variation functional.

The prerequisites are *Convex Analysis* in this category, which supplies the subdifferential of a convex function, the normal cone, the Fenchel conjugate and the Moreau envelope; *Measure Theory and Integration* for the almost everywhere statements, in particular Rademacher's theorem, which is the analytic input of the Clarke construction; and *Modes of Convergence* for the convergence of the gradients in the definition of the limiting objects and for the lower semicontinuity vocabulary. The general theory of set-valued maps on infinite-dimensional spaces, the metric regularity of maps between Banach spaces, the Ekel; the statements here are the finite-dimensional ones that the neighbouring articles use, with the general versions cited as standard.

## Nonsmooth Functions and their Subdifferentials

### Lipschitz Functions and Rademacher's Theorem

**Definition.** A function $f:\mathbb{R}^n\to\mathbb{R}$ is **locally Lipschitz** at $x$ if there are a neighbourhood $U$ of $x$ and $L\geq0$ with $\lvert f(u)-f(v)\rvert\leq L\lvert u-v\rvert$ for all $u,v\in U$. The **one-sided directional derivative** is $f'(x;d) = \lim_{t\downarrow0}t^{-1}(f(x+td)-f(x))$ when the limit exists.

**Theorem (Rademacher).** A function that is locally Lipschitz on an open set $U\subseteq\mathbb{R}^n$ is differentiable at almost every point of $U$, and its gradient there is locally bounded; for every $x\in U$ and every direction $d$ the difference quotients $t^{-1}(f(x+td)-f(x))$, $0<t<t_0$, are bounded by the Lipschitz constant, so the upper one-sided derivative $\limsup_{t\downarrow0}t^{-1}(f(x+td)-f(x))$ is finite, and the one-sided derivative $f'(x;d)$ exists exactly when that upper derivative equals the corresponding lower one.

**Proof sketch.** The one-dimensional case is the theorem that a monotone function is differentiable almost everywhere, applied to the restriction of $f$ to each line; the $n$-dimensional case follows from the one-dimensional one by averaging over the directions of a finite set spanning $\mathbb{R}^n$ and using the Lipschitz bound to control the difference between the directional quotients of the various directions. $\square$

**Remark (why the theorem matters here).** Rademacher's theorem is what makes the definition of the Clarke subdifferential below possible: the set of differentiability points is of full measure and dense, so the limits of the gradients there carry information about the behaviour of the function at every point. Without it, the convexified derivative set would not be definable at all.

### The Fréchet and Limiting Subdifferentials

**Definition.** For $f:\mathbb{R}^n\to(-\infty,+\infty]$ finite at $x$, the **Fréchet subdifferential** is
$$
\hat\partial f(x) = \bigl\{\,v : f(u)\geq f(x)+\langle v,u-x\rangle+o(\lvert u-x\rvert)\ \text{as } u\to x\,\bigr\},
$$
and the **limiting (Mordukhovich) subdifferential** is
$$
\partial f(x) = \{\,v : v = \lim_kv_k\ \text{with } v_k\in\hat\partial f(u_k),\ f(u_k)\to f(x),\ u_k\to x\,\}.
$$
For a set $\Omega$ and $x\in\Omega$ the **Fréchet normal cone** is $\hat N(x;\Omega) = \hat\partial\delta_\Omega(x)$ and the **limiting normal cone** is $N(x;\Omega) = \partial\delta_\Omega(x)$; the **tangent (contingent) cone** is $T(x;\Omega) = \{d : \exists t_k\downarrow0, d_k\to d,\ x+t_kd_k\in\Omega\}$.

**Theorem.** The Fréchet subdifferential is a closed convex set, possibly empty, and for convex $f$ it coincides with the subdifferential of convex analysis; the limiting subdifferential is closed but generally not convex and may be empty; for locally Lipschitz $f$ the limiting subdifferential is nonempty compact at every point, and the **Clarke subdifferential** is its closed convex hull, $\partial^\circ f(x) = \overline{\operatorname{conv}}\partial f(x)$. One has $\hat\partial f(x)\subseteq\partial f(x)\subseteq\partial^\circ f(x)$; for $v\in\hat\partial f(x)$ the one-sided difference quotients satisfy
$$
\liminf_{t\downarrow0}\frac{f(x+td)-f(x)}{t}\geq\langle v,d\rangle\qquad(d\in\mathbb{R}^n),
$$
so that $f'(x;d)\geq\langle v,d\rangle$ whenever the one-sided derivative exists; for the Clarke set the dual inequality
$$
f'(x;d)\leq\max_{v\in\partial^\circ f(x)}\langle v,d\rangle
$$
always holds for locally Lipschitz $f$; and for a limiting subgradient neither inequality need hold, as the example below shows.

**Proof sketch.** The Fréchet set is the intersection of the closed half-spaces of the first-order affine minorants, hence closed and convex; the convex case is the definition of the convex subdifferential. The first inequality is the defining inequality divided by $t$; the second is Clarke's theorem, proved by the mean value theorem applied along the direction $d$ together with the upper semicontinuity of the generalised gradient. $\square$

**Example.** For $f(x) = \lvert x\rvert$ one has $\hat\partial f(0) = \partial f(0) = \partial^\circ f(0) = [-1,1]$, all three objects agreeing because the function is convex; for $f(x) = -\lvert x\rvert$ one has $\hat\partial f(0) = \emptyset$, $\partial f(0) = \{-1,1\}$ and $\partial^\circ f(0) = [-1,1]$, so the three objects are pairwise distinct. The emptiness of the Fréchet subdifferential is the two-sided computation: the defining ratio $(f(u)-f(0)-vu)/\lvert u\rvert$ equals $-1-v\operatorname{sgn}u$ for $u\neq0$, whose infimum over $u\neq0$ is $-1-\lvert v\rvert<0$, so no $v$ satisfies the defining inequality; computing the ratio over a grid of $u$ for $v = -2,\dots,2$ reproduces this infimum at each $v$. The two limits $\pm1$ of the derivative on the two sides are the elements of the limiting subdifferential. The value $v = 1$, a limit of gradients at the points $x<0$, is *not* a Fréchet subgradient at the origin, since the inequality above with $d = +1$ would give the false $-1 = f'(0;1)\geq\langle1,1\rangle = 1$; this is the sense in which the limiting subdifferential is larger than the Fréchet one and its elements carry no first-order inequality.

**Definition.** A locally Lipschitz $f$ is **regular** (Clarke-regular) at $x$ if the one-sided directional derivative $f'(x;d)$ exists for every $d$ and equals Clarke's generalised directional derivative
$$
f^\circ(x;d) = \max_{v\in\partial^\circ f(x)}\langle v,d\rangle
$$
for every $d$. Convex functions and continuously differentiable functions are regular at every point; the function $-\lvert x\rvert$ is not, since $f'(0;1) = -1$ while $f^\circ(0;1) = 1$.

### The Clarke Subdifferential and its Calculus

**Definition.** For a locally Lipschitz $f$ and a point $x$, the **Clarke subdifferential** (also **generalised gradient**) is
$$
\partial^\circ f(x) = \operatorname{conv}\{\,v : v = \lim_k\nabla f(x_k),\ x_k\to x,\ f\ \text{differentiable at } x_k\,\}.
$$
**Theorem.** $\partial^\circ f(x)$ is a nonempty compact convex set, the map $x\mapsto\partial^\circ f(x)$ is upper semicontinuous with compact images, and $\partial^\circ f$ is the smallest set-valued map with these properties containing all the limits of the gradients; for the pointwise maximum $f = \max_{i\leq m}g_i$ of $C^1$ functions,
$$
\partial^\circ f(x) = \operatorname{conv}\{\nabla g_i(x) : g_i(x) = f(x)\},
$$
and for the composition $f\circ G$ with $G$ continuously differentiable the chain rule $\partial^\circ(f\circ G)(x)\subseteq \nabla G(x)^{\mathsf T}\partial^\circ f(G(x))$ holds, with equality when $G$ is a local diffeomorphism.

**Proof sketch.** For the maximum, the differentiability points of $f$ off the set where two of the $g_i$ agree have gradients among the active ones, and on the coincidence set the limits add nothing, so the convex hull of the active gradients is the whole of $\partial^\circ f$; the chain rule follows from the mean value theorem below and the upper semicontinuity; the minimality is a consequence of the definition and the fact that the limits of gradients against a sequence are contained in any upper semicontinuous convex-valued extension. $\square$

**Theorem (the mean value theorem; Clarke).** Let $f$ be locally Lipschitz on an open set containing the segment $[x,y]$. Then there is $z$ in the segment with
$$
f(y)-f(x)\in\langle\partial^\circ f(z),\,y-x\rangle ;
$$
and consequently $\lvert f(y)-f(x)\rvert\leq\max_{v\in\partial^\circ f(z)}\lvert v\rvert\,\lvert y-x\rvert$ for some $z$ in the segment, so that a bound on the generalised gradient gives a Lipschitz bound.

**Proof sketch.** The function $t\mapsto f(x+t(y-x))$ is locally Lipschitz on $[0,1]$; its derivative exists almost everywhere by Rademacher and is a limit of directional derivatives, and the fundamental theorem of calculus for the absolutely continuous function so obtained expresses the difference as the integral of the derivative, which is an element of the required convex set by the definition of the subdifferential and the mean value inequality. $\square$

**Theorem (the sum rule).** For locally Lipschitz $f,g$, $\partial^\circ(f+g)(x)\subseteq\partial^\circ f(x)+\partial^\circ g(x)$, and equality holds when one of them is strictly differentiable at $x$; the inclusion may be strict otherwise, the finite-dimensional case being the one in which no further hypothesis is needed for the inclusion itself.

**Proof sketch.** The inclusion follows from the mean value theorem applied to $f+g$ and the separate mean value theorems for $f$ and $g$; the equality under strict differentiability is obtained by subtracting a smooth function and applying the minimality property. $\square$

**Remark (the relations).** For a locally Lipschitz function one always has $\hat\partial f(x)\subseteq\partial f(x)\subseteq\partial^\circ f(x)$; the first inclusion is the definition, and the second holds because the limits of gradients at nearby points belong to the upper semicontinuous convex-valued map and the convex hull of the limits is the whole of $\partial^\circ f$. For convex $f$ all three sets are the convex subdifferential of *Convex Analysis*; for $C^1$ functions all three are the singleton $\{\nabla f(x)\}$; and for the pointwise maximum of smooth functions the Clarke set is the convex hull of the active gradients, while the limiting set is the set of gradients of the active functions themselves, without convexification. The choice among them is dictated by the calculus one needs: the Clarke set gives convex-valued necessary conditions and the global Lipschitz estimate, the limiting set gives the exact sum and chain rules and the necessary conditions without constraint qualifications.

## Variational Principles and Metric Regularity

### Ekeland's Variational Principle

**Theorem (Ekeland).** Let $(X,d)$ be a complete metric space and $f:X\to\mathbb{R}\cup\{+\infty\}$ lower semicontinuous and bounded below, with $f\not\equiv+\infty$. For every $\epsilon>0$ and every $x_0$ with $f(x_0)\leq\inf_Xf+\epsilon$ there is $x_\epsilon$ with
$$
f(x_\epsilon)\leq f(x_0), \qquad d(x_\epsilon,x_0)\leq1, \qquad f(x_\epsilon)\leq f(x)+\epsilon\, d(x,x_\epsilon)\quad\text{for all } x\in X .
$$
In particular every lower semicontinuous functional bounded below on a complete metric space has, for every $\epsilon>0$, a point that is $\epsilon$-optimal and $\epsilon$-optimal for the perturbed functional.

**Proof.** Order the points by $x\preceq y$ iff $f(x)\leq f(y)-\epsilon d(x,y)$, a partial order by the triangle inequality; the set of points below $x_0$ is closed by lower semicontinuity and its diameter is at most $1$, so the intersection of the chain of set-valued iterations is a point $x_\epsilon$ by completeness, and it is maximal in the order, which is the displayed inequality. $\square$

**Theorem (consequences).** (a) If $f$ is continuously differentiable on a Banach space, the principle gives for every $\epsilon$ a point $x_\epsilon$ with $\lVert\nabla f(x_\epsilon)\rVert\leq\epsilon$ — the **approximate critical point** statement — so that a functional bounded below and without critical points cannot exist. (b) The **Caristi fixed point theorem**: if $T:X\to X$ satisfies $d(x,Tx)\leq f(x)-f(Tx)$ for a lower semicontinuous $f$ bounded below on a complete metric space, then $T$ has a fixed point. (c) The principle implies the **Borwein–Preiss** smooth variational principle in the form in which it is applied to non-smooth minimisation: a lower semicontinuous bounded-below function on a Banach space with an equivalent smooth norm attains its minimum after perturbation by a small smooth function.

**Proof sketch.** (a) is the inequality of the principle evaluated at $x+\delta h$ for unit $h$ and letting $\delta\downarrow0$. (b) is proved by applying the principle to $f$ to obtain a maximal point, at which the Caristi inequality forces $Tx = x$; the converse holds as well, so the two statements are equivalent. (c) is proved by iterating the principle and summing the perturbations to obtain a smooth one. $\square$

### Metric Regularity and the Lyusternik–Graves Theorem

**Definition.** A set-valued map $F:\mathbb{R}^n\rightrightarrows\mathbb{R}^m$ is **metrically regular** around $(\bar x,\bar y)\in\operatorname{gph}F$ if there is $\kappa>0$ and a neighbourhood $U$ of $(\bar x,\bar y)$ with
$$
\operatorname{dist}\bigl(x,F^{-1}(y)\bigr)\leq\kappa\,\operatorname{dist}\bigl(y,F(x)\bigr)\qquad\text{for all } (x,y)\in U .
$$
**Theorem (Lyusternik–Graves; the inverse function theorem).** If $F$ is single-valued and strictly differentiable at $\bar x$ with surjective derivative $\nabla F(\bar x)$, then $F$ is metrically regular around $(\bar x,F(\bar x))$; consequently the inverse map is locally single-valued, Lipschitz and defined on a neighbourhood of $F(\bar x)$. More generally, for a set-valued $F$ with closed graph the metric regularity is equivalent to the kernel condition $D^*F(\bar x,\bar y)(0) = \{0\}$, where the **coderivative** is
$$
D^*F(\bar x,\bar y)(v) = \{\,u : (u,-v)\in N\bigl((\bar x,\bar y);\operatorname{gph}F\bigr)\,\}.
$$
**Proof sketch.** The implication from surjectivity to regularity is proved by the Newton iteration: the linearised equation $\nabla F(\bar x)(x-x_k)+\ldots$ is solved at each step, the error is controlled by the quantitative open mapping theorem for linear maps, and the iteration converges geometrically, using completeness. The converse and the coderivative criterion are proved by differentiating the metric inequality: a nonzero element of the coderivative kernel at the origin produces a pair of sequences in the graph whose distance to the graph violates the inequality. $\square$

**Theorem (the extremal principle).** Let $\Omega_1,\Omega_2\subseteq\mathbb{R}^n$ be closed and let $\bar x\in\Omega_1\cap\Omega_2$. If no two sequences $x_i^k\in\Omega_i$ with $x_i^k\to\bar x$ satisfy $\lvert x_1^k-x_2^k\rvert = o(\lvert x_1^k-\bar x\rvert+\lvert x_2^k-\bar x\rvert)$, then there is a nonzero $v\in N(\bar x;\Omega_1)\cap(-N(\bar x;\Omega_2))$ — the sets are **extremal** at $\bar x$ and are separated by a common normal.

**Proof sketch.** The extremal condition means that the difference set $\Omega_1-\Omega_2$ has the origin as an isolated point in a suitable asymptotic sense; one perturbs the two sets by small quadratic penalties relative to their affine spans, applies Ekeland's principle to the distance between the perturbed sets, and lets the perturbations vanish; the resulting pairs of nearest points produce the two normals, whose sum tends to zero in the limit. $\square$

**Remark (the calculus).** The extremal principle is the source of the **fuzzy sum rule** for the Fréchet subdifferential, $\hat\partial(f+g)(x)\subseteq\hat\partial f(x_1)+\hat\partial g(x_2)$ with $x_i$ near $x$ and $f,g$ close in value, whence the exact sum rule $\partial(f+g)(x)\subseteq\partial f(x)+\partial g(x)$ for the limiting subdifferential under a qualification on the domain; and it gives the **limiting necessary conditions**, in which the normal cone of the constraint set replaces the gradient of the constraint function and no constraint qualification is required.

## Variational Problems and the Direct Method

### Existence, Relaxation and the Convex Envelope

**Theorem (the direct method, nonsmooth form).** Let $f:\mathbb{R}^n\to(-\infty,+\infty]$ be lower semicontinuous and coercive on a nonempty closed set $C$. Then $f$ attains its minimum on $C$; if $f$ is strictly convex the minimiser is unique; and the set of minimisers is closed, and convex when $f$ is convex.

**Proof.** A minimising sequence is bounded by coercivity, has a convergent subsequence, and the limit lies in $C$ by closedness and is a minimiser by lower semicontinuity. Convexity gives convexity of the minimiser set, strict convexity uniqueness. $\square$

**Definition.** For $f:\mathbb{R}^n\to\mathbb{R}\cup\{+\infty\}$ the **lower semicontinuous envelope** is $\overline f(x) = \sup\{g(x) : g\leq f,\ g\ \text{lower semicontinuous}\}$ and the **convex envelope** (relaxation) is $\operatorname{conv}f(x) = \sup\{g(x) : g\leq f,\ g\ \text{convex}\}$; a variational problem is **relaxable without a duality gap** if the infimum of $f$ over $C$ equals the minimum of $\overline f$ over $C$.

**Theorem.** If $f$ is bounded below and coercive, then the infimum of $f$ over $\mathbb{R}^n$ equals the minimum of $\operatorname{conv}f$, and the minimisers of the relaxation are the limits of minimising sequences of $f$; the relaxation is the closed convex hull of $f$, computed as $\operatorname{conv}f = (\operatorname{cl}f)^{**}$ in the sense of the Fenchel duality of *Convex Analysis*.

**Proof sketch.** The relaxed function is the greatest closed convex minorant and is therefore below the original; the reverse inequality at a point is the separation theorem applied to the epigraph, exactly as in the biconjugacy theorem; the statement about minimising sequences follows because a coercive bounded-below function attains its infimum after relaxation by the direct method, and the value is the limit of values along any minimising sequence. $\square$

**Example (the total variation and the obstacle).** The **obstacle problem** minimises $J(u) = \int_\Omega\lvert\nabla u\rvert^2$ over the admissible functions $u\geq\psi$ of the Sobolev space $H^1_0(\Omega)$ of functions with one square-integrable derivative vanishing on the boundary, whose theory is standard and developed in the parallel articles on the function spaces of this Part; the constraint set is convex and closed, the functional is strictly convex, and the direct method gives a unique minimiser, characterised by the variational inequality $\int\nabla u\cdot\nabla(v-u)\geq0$ for all admissible $v$, which — taking the two signs of the perturbation where the constraint is inactive and only nonnegative perturbations where it is active — splits into the equation $\Delta u = 0$ on the set where $u>\psi$ and the inequality $\Delta u\leq0$ where $u = \psi$. The **total variation** functional $TV(u) = \int_\Omega\lvert\nabla u\rvert$ is convex, lower semicontinuous in $L^1$ and not differentiable where $\nabla u = 0$, so that its minimisers, when they exist, are characterised by $0\in\partial TV(u)+\ldots$ and the optimality condition is a subdifferential inclusion rather than an equation; the **Rudin–Osher–Fatemi** model minimises $\frac12\lVert u-f\rVert_2^2+\lambda TV(u)$ and is solved by the proximal algorithms of *Convex Analysis*, the proximal map of the total variation being the denoising operator. The rigorous existence theory for these functionals requires the Sobolev space $H^1$ and its compactness, which belong ; the nonsmooth content here — the subdifferential of the non-differentiable term and the convexity of the constraint — is in the finite-dimensional calculus, applied pointwise to the integrands.

### Optimality Conditions in Nonsmooth Programming

**Theorem (Clarke; Lipschitz programming).** Consider the problem of minimising $f_0$ subject to $f_i\leq0$, $i = 1,\dots,m$, and $x\in C$, where the functions are locally Lipschitz and $C$ is closed. If $\bar x$ is a local minimiser and the **Clarke constraint qualification** holds — $0\notin\partial^\circ f_i(\bar x)$ for the active $i$, or more generally a positive-linear-independence condition on the active generalised gradients — then there are $\lambda_i\geq0$ with $\lambda_if_i(\bar x) = 0$ and
$$
0\in\partial^\circ f_0(\bar x)+\sum_i\lambda_i\partial^\circ f_i(\bar x)+N_C(\bar x).
$$
**Proof sketch.** The problem is written as the minimisation of the locally Lipschitz function $f_0+\delta$, where $\delta$ is the indicator of the intersection of the active constraint sets; the mean value theorem and the common-normal form of the extremal principle applied to the epigraph and the constraint set give the multipliers, and the constraint qualification is exactly the condition under which the normal cone of the intersection is the sum of the normal cones. $\square$

**Theorem (the limiting form; Mordukhovich).** If $\bar x$ is a local minimiser of the problem above and a certain **basic constraint qualification** holds — the intersection of the limiting normal cones of the active constraint sets contains no nonzero positive combination adding to an element of $-N(\bar x;C)$ — then there are $\lambda_i\geq0$ with complementary slackness and
$$
0\in\partial f_0(\bar x)+\sum_i\lambda_i\partial f_i(\bar x)+N(\bar x;C),
$$
with the limiting subdifferential and the limiting normal cone. The advantage of this form is that the multiplier rule holds under a qualification that is automatically verified when the constraints are described by a system with a surjective derivative; the disadvantage is that the objects are not convex, so the conditions are necessary and not sufficient.

**Proof sketch.** The limiting necessary conditions are the exact form of the extremal principle applied to the graph of the problem, with the fuzzy sum rule replacing the Clarke convexification; the constraint qualification is what makes the fuzzy sum rule exact. $\square$

**Remark (the difference in use).** The Clarke conditions are the correct tool when sufficiency is wanted, since the convexity of $\partial^\circ$ makes the conditions sufficient for local optimality in the convex case and for the Lipschitz estimate in general; the limiting conditions are the correct tool when only necessity is at stake and no constraint qualification is available, as in problems with infinitely many constraints, with equality constraints without surjectivity, or with the solution at a singular point of the feasible set.

## Summary

A locally Lipschitz function on $\mathbb{R}^n$ is differentiable almost everywhere, by Rademacher's theorem, and this almost everywhere regularity is what allows the derivative at a point to be replaced by a set of derivative-like vectors. Three such sets are in use: the Fréchet subdifferential $\hat\partial f(x)$ of vectors satisfying a first-order inequality, which is closed and convex and may be empty; the limiting subdifferential $\partial f(x)$ of limits of Fréchet subgradients at nearby points, which is closed but generally non-convex and carries the exact calculus, with the sum rule $\partial(f+g)\subseteq\partial f+\partial g$ under a qualification; and the Clarke subdifferential $\partial^\circ f(x) = \overline{\operatorname{conv}}\partial f(x)$, which is always nonempty compact and convex for locally Lipschitz functions, contains the other two, satisfies the mean value theorem $f(y)-f(x)\in\langle\partial^\circ f(z),y-x\rangle$ and the chain rule, and equals the convex hull of the active gradients for a maximum of smooth functions. For convex functions all three agree with the subdifferential of convex analysis; the three differ already for $f(x) = -\lvert x\rvert$ at the origin, where $\hat\partial f(0) = \emptyset$, $\partial f(0) = \{-1,1\}$ and $\partial^\circ f(0) = [-1,1]$. Ekeland's variational principle gives approximate minimisers of a lower semicontinuous functional bounded below on a complete metric space; it yields the approximate critical point statement, the Caristi fixed point theorem and the smooth variational principle, and it is the tool by which the exact calculus and the metric regularity theory are proved. A set-valued map with closed graph is metrically regular exactly when the kernel of its coderivative at the reference point is trivial, which is the nonsmooth form of the inverse function theorem of Lyusternik and Graves, and the extremal principle is the separation theorem from which the fuzzy and the exact sum rules are derived. The direct method in finite dimensions gives the existence of minimisers for a coercive lower semicontinuous functional on a closed set; the relaxation of a non-convex problem by its closed convex envelope removes the duality gap for coercive problems; the optimality conditions of nonsmooth programming hold in the Clarke form under a constraint qualification and in the limiting form without one; and the obstacle problem and the total variation functional are the model problems in which the subdifferential enters as the replacement for the Euler–Lagrange equation.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $f'(x;d)$ | One-sided directional derivative |
| $\hat\partial f(x)$ | Fréchet subdifferential |
| $\partial f(x)$ | Limiting (Mordukhovich) subdifferential |
| $\partial^\circ f(x)$ | Clarke subdifferential (generalised gradient) |
| $\hat N(x;\Omega)$, $N(x;\Omega)$ | Fréchet and limiting normal cones |
| $T(x;\Omega)$ | Tangent (contingent) cone |
| $\operatorname{gph}F$ | Graph of the set-valued map $F$ |
| $D^*F$ | Coderivative |
| $d(x,A)$, $\operatorname{dist}$ | Distance to a set |
| $\overline f$, $\operatorname{conv}f$ | Lower semicontinuous and convex envelopes |
| $TV(u)$ | Total variation functional |
| $\lambda_i$ | Lagrange multipliers |
| $X$, $d$ | Complete metric space and its distance |



## Further Reading

- Frank H. Clarke, *Optimization and Nonsmooth Analysis* (Wiley, 1983), for the generalised gradient, the mean value theorem, the chain rule and the Lipschitz programming conditions.
- Frank H. Clarke, Yu. S. Ledyaev, R. J. Stern and P. R. Wolenski, *Nonsmooth Analysis and Control Theory* (Springer, 1998), for the refined calculus and the applications to control.
- Boris S. Mordukhovich, *Variational Analysis and Generalized Differentiation I: Basic Theory* (Springer, 2006), for the limiting subdifferential, the coderivative, the extremal principle and the necessary conditions without constraint qualifications.
- Boris S. Mordukhovich, *Variational Analysis and Generalized Differentiation II: Applications* (Springer, 2006), for the applications to optimisation, control and the calculus of variations.
- Ivar Ekeland, *On the variational principle* (Journal of Mathematical Analysis and Applications 47, 1974), for the variational principle and its consequences.
- Ivar Ekeland and Roger Temam, *Convex Analysis and Variational Problems* (North-Holland, 1976), for the convex case, the relaxation and the existence theory of variational problems.
- Ralph Tyrell Rockafellar and Roger J.-B. Wets, *Variational Analysis* (3rd ed., Springer, 2009), for the systematic treatment of the set-valued calculus, metric regularity and the coderivative.
- Alexey D. Ioffe, *Metric regularity and subdifferential calculus* (Russian Mathematical Surveys 55, 2000), for the relation between the coderivative criteria, the Lyusternik–Graves theorem and the subdifferential calculus.
- Jonathan M. Borwein and Qiji J. Zhu, *Techniques of Variational Analysis* (Springer, 2005), for the smooth variational principles, the fuzzy calculus and the worked examples.
