
# __Nonlinear Functional Analysis__

## Introduction

A nonlinear equation between Banach spaces, $f(u)=v$, has no linear structure to be inverted, and the two ways of solving it that the theory provides are the local one, in which the derivative $f'(u)$ is inverted and the equation is solved by iteration in a neighbourhood of a known solution, and the global one, in which $f$ is the derivative of a functional and the equation is read as the critical-point equation $F'(u)=0$. The first way is the reduction of the nonlinear problem to a linear one by the inverse and implicit function theorems; the second is the calculus of variations in its modern form, with convexity replacing the invertibility of the derivative in the cases where the functional is convex, and with compactness replacing it in the cases where the functional has a minimax geometry.

The article develops both. It begins with nonlinear maps between Banach spaces, their continuity, compactness and differentiability, and the two basic local theorems: the **inverse function theorem**, that a $C^k$ map with invertible derivative at a point is a local $C^k$ diffeomorphism, and the **implicit function theorem**, that a level set with surjective derivative is locally a graph; with them come the constant-rank theorem and Lyusternik's theorem on local surjectivity. It then develops **convex analysis**: the subdifferential of a convex function, its maximal monotonicity, the Legendre–Fenchel conjugate, the sum rule and the minimisation criterion $0 \in\partial f(x)$, together with Ekeland's variational principle, which converts the existence of approximate minimisers into the existence of a point that minimises a perturbed functional. It treats **monotone operators** on a Banach space, for which the maximality and the coercivity give surjectivity, and it treats the **variational methods**: the direct method of the calculus of variations, the Palais–Smale condition, the deformation lemma, the minimax principle and the mountain pass theorem, with the Ljusternik–Schnirelmann theory of the multiplicity of critical points.

The analytic fixed-point theorems — the contraction principle, the Schauder and Leray–Schauder theorems, and the degree theory of which they are consequences — are not covered here; only the contraction principle is quoted here, as a standard tool for the inverse function theorem, and the topological degree is not used. The differential calculus on normed spaces, the Fréchet and Gâteaux derivatives, the mean value inequality and Taylor's theorem are those of *Differential Calculus on Normed Spaces*; the Hahn–Banach theorem, weak topologies, reflexivity and the duality of Banach spaces are those of *Duality Theory*, and the compact operators and Fredholm theory are those of *Fredholm Theory*. The measure theory and integration used in the examples are those of *Measure Theory and Integration*. The applications of the theory to elliptic boundary problems, evolution equations and the calculus of variations belong to *Differential Equations* in the calculus of variations proper; they are cited, not developed.

No physics is invoked.

## Nonlinear Maps and Their Differentiability

### Continuity, Boundedness and Compactness

**Definition.** Let $X,Y$ be Banach spaces over $\mathbb{K}=\mathbb{R}$ or $\mathbb{C}$ and let $D \subseteq X$ be open. A map $f:D\to Y$ is **continuous** if it is continuous for the norm topologies; **locally bounded** if every point of $D$ has a neighbourhood on which $f$ is bounded; **Lipschitz** if $\|f(x)-f(y)\|\le L\|x-y\|$ for some $L$; and **compact** if it maps bounded subsets of $D$ to relatively compact subsets of $Y$. It is **proper** if the preimage of every compact set is compact, and **weakly continuous** if it is continuous for the weak topologies.

For linear maps the notions of continuity and local boundedness coincide, and a continuous linear map is bounded; for nonlinear maps they do not, and a continuous nonlinear map need not be bounded on bounded sets: on the open set $D=(0,\infty)$ the continuous function $f(t)=1/t$ is unbounded on the bounded set $(0,1)$. A map that is continuous and maps bounded sets to bounded sets is called **bounded**; a completely continuous map is one that is continuous and compact.

**Proposition.** (i) A continuous map on an open set is locally bounded if $Y=\mathbb{K}$ and $f$ is convex. (ii) A compact map is bounded on bounded sets and is completely continuous. (iii) On an infinite-dimensional reflexive Banach space a bounded continuous map need not be weakly continuous, and a compact map need not be continuous from the weak topology to the norm topology either: the norm of a Hilbert space is weakly lower semicontinuous but not weakly continuous, and as a map into $\mathbb{R}$ it is compact on bounded sets; for a compact *linear* operator weak convergence of $x_n$ does imply norm convergence of $Tx_n$.

*Proof.* (i) is the standard local boundedness of a convex function, proved by choosing a simplex around the point and bounding on it. (ii) is immediate from the definitions. (iii) is the standard statement that a compact map sends weakly convergent sequences to norm-convergent ones; the proof uses the uniform boundedness of the weakly convergent sequence and the compactness. $\square$

**Definition.** A **functional** is a map $F:D\to\mathbb{R}$; it is **coercive** if $F(x)\to+\infty$ as $\|x\|\to\infty$, **lower semicontinuous** if $x_n\to x$ implies $F(x)\le\liminf F(x_n)$, and **weakly lower semicontinuous** if the same holds for weakly convergent sequences.

### Differentiation

**Definition.** Let $f:D\to Y$ with $D$ open. The map is **Fréchet differentiable** at $x \in D$ if there is $A \in B(X,Y)$ with

$$
f(x+h)=f(x)+Ah+o(\|h\|) \qquad (\|h\|\to0),
$$

and then $A=f'(x)=Df(x)$ is the **Fréchet derivative**. It is **Gâteaux differentiable** at $x$ if the directional derivative $\delta f(x;h)=\lim_{t\to0}\frac{f(x+th)-f(x)}{t}$ exists for every $h$ and defines a bounded linear map $h\mapsto\delta f(x;h)$. The map is of class $C^k$ if it is $k$ times Fréchet differentiable with continuous derivatives, and of class $C^{k,\alpha}$ if the $k$-th derivative is Hölder continuous of exponent $\alpha$.

The Fréchet derivative is unique when it exists, the chain rule and the product rule hold, and the mean value inequality of *Differential Calculus on Normed Spaces*, $\|f(x+h)-f(x)\|\le\sup_{t\in[0,1]}\|f'(x+th)\|\,\|h\|$, governs all estimates. The Gâteaux derivative exists whenever the Fréchet derivative does, and the two coincide; the converse fails, and the classical example is the map $f(x,y)=\frac{x^3}{x^2+y^2}$ (with $f(0,0)=0$), which is continuous and has a directional derivative at the origin in every direction, $\delta f(0;h)=\frac{h_1^3}{h_1^2+h_2^2}$ for $h \neq0$, yet is not Fréchet differentiable there, since $f(h)/\|h\|$ along the line $y=x$ tends to $\frac{1}{2\sqrt2}$ and not to $0$; the directional derivative is not linear in $h$, so this map is not Gâteaux differentiable at the origin in the strict sense either, and the requirement that $h\mapsto\delta f(x;h)$ be bounded and linear is exactly what separates the two notions.

**Theorem (Taylor).** Let $f:D\to Y$ be of class $C^k$ near $x$ and let $x+h \in D$. Then

$$
f(x+h)=\sum_{j=0}^{k-1}\frac{1}{j!}f^{(j)}(x)(h)^j+\int_0^1\frac{(1-t)^{k-1}}{(k-1)!}\,f^{(k)}(x+th)(h)^k\,dt ,
$$

the integral being the Bochner integral of a continuous $Y$-valued function; the remainder is $o(\|h\|^{k-1})$ and, for $f \in C^k$, of order $\|h\|^k$ near $x$.

**Example.** (i) The map $f:\mathbb{R}^n\to\mathbb{R}$, $f(x)=\langle Ax,x\rangle$ for a symmetric matrix $A$, has $f'(x)h=2\langle Ax,h\rangle$.

(ii) The map $F:L^2(\Omega)\to\mathbb{R}$, $F(u)=\int_\Omega\bigl(\frac12|\nabla u|^2+g(u)\bigr)dx$ with $g \in C^1$, the model functional of a quasilinear problem, has $F'(u)h=\int_\Omega(\nabla u\cdot\nabla h+g'(u)h)\,dx$, and the critical-point equation $F'(u)=0$ is the weak form of $-\Delta u+g'(u)=0$, whose theory belongs.

(iii) The **Nemytskii operator** $u\mapsto g(\cdot,u(\cdot))$ is continuous and bounded from $L^p(\Omega)$ to $L^q(\Omega)$ when $g$ is continuous and satisfies the growth condition $|g(x,s)|\le C(1+|s|^{p/q})$, and its composition with the compact embedding is compact; it is the archetype of the nonlinear operators that couple the calculus with the function spaces.

## The Inverse and Implicit Function Theorems

### Local Invertibility

**Theorem (inverse function theorem).** Let $X,Y$ be Banach spaces, $D \subseteq X$ open, $f:D\to Y$ of class $C^k$ for some $k \ge1$, and let $x_0 \in D$ be such that $f'(x_0)$ is invertible in $B(X,Y)$. Then there are open neighbourhoods $U$ of $x_0$ and $V$ of $f(x_0)$ such that $f:U\to V$ is a bijection with a $C^k$ inverse; moreover $g=f^{-1}$ satisfies $g'(y)=f'(g(y))^{-1}$, and if $f$ is real analytic the same is true of $g$.

*Proof (sketch).* Compose with the inverse of $f'(x_0)$ to assume $f'(x_0)=I$, and consider the map $T(x)=x-f(x)+y$ for a fixed $y$ near $f(x_0)$; a solution of $f(x)=y$ is a fixed point of $T$. Near $x_0$ the derivative $T'(x)=I-f'(x)$ has norm at most $\frac12$, so $T$ is a contraction on a suitable closed ball, and the contraction mapping principle below gives a unique fixed point. The bounds are uniform for $y$ in a neighbourhood of $f(x_0)$, which gives the bijection $U\to V$. For the differentiability of the inverse, write $g=f^{-1}$ and $x=g(y)$; applying $f'(x)^{-1}$ to the expansion $k=f(x+h)-f(x)=f'(x)h+o(\|h\|)$ with $h=g(y+k)-g(y)$ gives $g(y+k)-g(y)=f'(g(y))^{-1}k+o(\|k\|)$, whence $g'(y)=f'(g(y))^{-1}$; its continuity, together with the higher derivatives and the analytic statement, follows by induction. $\square$

**Lemma (contraction mapping principle).** Let $(M,d)$ be a complete metric space and $T:M\to M$ a contraction, $d(Tx,Ty)\le\kappa\,d(x,y)$ with $\kappa<1$. Then $T$ has a unique fixed point $x^*$, and for every $x$ the iterates $T^nx$ converge to $x^*$ with $d(T^nx,x^*)\le\frac{\kappa^n}{1-\kappa}d(x,Tx)$.

The principle is the fixed-point theorem of the metric setting and is proved by showing that the iterates form a Cauchy sequence, summing the geometric series; the uniqueness is immediate. The analytic fixed-point theorems, which extract fixed points from compactness rather than contractivity, are not covered here.

**Theorem (Newton's method; Kantorovich).** Let $f:D\to Y$ be $C^1$ with $f'$ Lipschitz of constant $L$ on a ball, let $f'(x_0)^{-1}$ exist with $\|f'(x_0)^{-1}\|\le\beta$, and let $\eta=\|f'(x_0)^{-1}f(x_0)\|$. If $\beta L\eta\le\frac12$ and the ball $B(x_0,r)$ with $r=\frac{1-\sqrt{1-2\beta L\eta}}{\beta L}$ lies in $D$, then $f$ has a zero in $B(x_0,r)$, the Newton iterates $x_{n+1}=x_n-f'(x_n)^{-1}f(x_n)$ are defined and converge to it, and the convergence is quadratic.

*Proof (sketch).* One shows by induction that the Newton iterates are defined, that the quadratic estimates $\|x_{n+1}-x_n\|\le\frac{\beta L}{2}\|x_n-x_{n-1}\|^2$ hold, and that the majorising scalar sequence converges; the details are the standard Kantorovich argument, cited below. $\square$

### Implicit Functions and Level Sets

**Theorem (implicit function theorem).** Let $X,Y,Z$ be Banach spaces, let $\Omega \subseteq X\times Y$ be open, and let $F:\Omega\to Z$ be of class $C^k$ with $F(x_0,y_0)=0$. If the partial derivative $\partial_yF(x_0,y_0) \in B(Y,Z)$ is invertible, then there are neighbourhoods $U$ of $x_0$ and $W$ of $y_0$ and a $C^k$ map $\varphi:U\to W$ with $\varphi(x_0)=y_0$ and

$$
F(x,y)=0 \text{ in } U\times W \iff y=\varphi(x); \qquad \varphi'(x)=-\bigl(\partial_yF(x,\varphi(x))\bigr)^{-1}\partial_xF(x,\varphi(x)).
$$

*Proof.* Apply the inverse function theorem to $(x,y)\mapsto(x,F(x,y))$, whose derivative at $(x_0,y_0)$ is the invertible operator with matrix $\begin{pmatrix}I&0\\\partial_xF&\partial_yF\end{pmatrix}$. $\square$

**Theorem (constant rank and local surjectivity).** Let $f:D\to Y$ be $C^1$, $x_0 \in D$, and suppose $f'(x_0)$ is surjective with a complemented kernel (always the case when $X,Y$ are Hilbert spaces, or when $f'(x_0)$ is Fredholm). Then there are neighbourhoods of $x_0$ and of $f(x_0)$ and a diffeomorphism under which $f$ becomes a linear projection; in particular $f$ is locally surjective at $x_0$ and there is a constant $C$ with, for $y$ near $f(x_0)$, a solution $x$ of $f(x)=y$ satisfying

$$
\|x-x_0\| \le C\|y-f(x_0)\| .
$$

*Proof (sketch).* Decompose $X=\ker f'(x_0)\oplus X_1$ and $Y=f'(x_0)(X)\oplus Y_1$; the map $x_1\mapsto f(x_0+x_1)$ is a local diffeomorphism from $X_1$ onto a neighbourhood of $f(x_0)$ by the inverse function theorem, and the variations in the kernel direction are absorbed by the diffeomorphism; the estimate is the quantitative form of the local surjectivity. This is Lyusternik's theorem, and it is the form in which the inverse function theorem is applied when the derivative is onto but not injective. $\square$

**Corollary (local structure of a level set).** If $F:\Omega\to Z$ is $C^k$ and $F'(x_0)$ is surjective, then the level set $F^{-1}(F(x_0))$ is near $x_0$ a $C^k$ submanifold of $X$ of dimension $\dim\ker F'(x_0)$; in particular a regular value of a $C^k$ map between finite-dimensional manifolds has a $C^k$ preimage. This is the local form of the theorem on regular values, whose global consequences for the topology of manifolds belong to *Differential Topology*.

## Convex Analysis

### Convex Functions and Their Subdifferentials

**Definition.** A function $f:X\to\mathbb{R}\cup\{+\infty\}$ is **convex** if $f(tx+(1-t)y)\le tf(x)+(1-t)f(y)$ for $t \in[0,1]$ and all $x,y$; **proper** if it is not identically $+\infty$; **lower semicontinuous** if its epigraph $\{(x,\lambda):\lambda\ge f(x)\}$ is closed. The **effective domain** is $\operatorname{dom}f=\{x:f(x)<+\infty\}$.

**Proposition.** (i) A proper convex function that is bounded above on a neighbourhood of a point is continuous at that point and locally Lipschitz there. (ii) A lower semicontinuous convex function is weakly lower semicontinuous. (iii) A convex function that is coercive and lower semicontinuous attains its minimum.

*Proof.* (i) is the standard argument that bounds the function above on a ball and uses the convexity to bound the oscillation on a smaller ball; (ii) uses that a convex l.s.c. function is the supremum of its affine minorants; (iii) uses the coercivity to restrict to a bounded set, the weak lower semicontinuity and the reflexivity to extract a weakly convergent minimising sequence with a limit in the set and the l.s.c. to pass to the limit. $\square$

**Definition.** The **subdifferential** of $f$ at $x$ with $f(x)<+\infty$ is

$$
\partial f(x)=\{x^* \in X^*:f(y)\ge f(x)+\langle x^*,y-x\rangle \text{ for all } y \in X\},
$$

the set of slopes of affine minorants of $f$ that are tangent at $x$; the elements are **subgradients**. The function is **subdifferentiable** at $x$ if $\partial f(x)\neq\varnothing$, and it is Gâteaux differentiable at $x$ exactly when $\partial f(x)$ is a singleton, in which case $\partial f(x)=\{f'(x)\}$.

**Theorem (Rockafellar).** Let $f$ be proper, convex and lower semicontinuous. Then $\partial f(x)$ is convex and weak-$*$ closed; it is nonempty and bounded when $x$ lies in the interior of $\operatorname{dom}f$, and at a boundary point of the effective domain it may be empty or unbounded, the normal cone of a convex set being the model of the second case; the operator $\partial f:X\rightrightarrows X^*$ is **monotone**, $\langle x^*-y^*,x-y\rangle\ge0$, and **maximal monotone** in the sense below; and

$$
x \text{ minimises } f \iff 0 \in\partial f(x).
$$

*Proof (sketch).* The convexity of $\partial f(x)$ and its weak-$*$ closedness are immediate from the definition; the nonemptiness at interior points is the Hahn–Banach separation of the epigraph from $(x,f(x)-1)$; the maximal monotonicity is Rockafellar's theorem and is standard; and the minimisation criterion is the definition of the subgradient when $x$ is a minimiser, and follows by taking $y=x+th$ and letting $t\downarrow0$ in the other direction. $\square$

### The Legendre–Fenchel Conjugate

**Definition.** The **conjugate** (or Legendre–Fenchel transform) of $f:X\to\mathbb{R}\cup\{+\infty\}$ is

$$
f^*(x^*)=\sup_{x \in X}\bigl(\langle x^*,x\rangle-f(x)\bigr) \in(-\infty,+\infty] ,
$$

a convex lower semicontinuous function on $X^*$; the **biconjugate** is $f^{**}$, and **Fenchel's inequality** $f(x)+f^*(x^*)\ge\langle x^*,x\rangle$ holds always.

**Theorem (Fenchel–Moreau).** For a proper function $f$, one has $f^{**}=f$ if and only if $f$ is convex and lower semicontinuous. Moreover

$$
x^* \in\partial f(x) \iff f(x)+f^*(x^*)=\langle x^*,x\rangle \iff x \in\partial f^*(x^*),
$$

so the subdifferential of the conjugate is the inverse relation of the subdifferential of $f$.

**Example.** (i) For $f(x)=\frac12\|x\|^2$ on a Hilbert space identified with its dual, $f^*=f$, and $\partial f(x)=\{x\}$; the pair is the model of a strictly convex functional and its conjugate.

(ii) For the indicator $\delta_C$ of a closed convex set $C$ (equal to $0$ on $C$ and $+\infty$ off it), $\delta_C^*=\sigma_C$ is the support function, and $\partial\delta_C(x)=N_C(x)$ is the normal cone; the minimisation criterion becomes the variational inequality $\langle x^*,y-x\rangle\ge0$ for all $y \in C$.

(iii) For $f(x)=\|x\|$, $\partial f(0)$ is the unit ball of $X^*$ and $\partial f(x)=\{x^*:\|x^*\|=1,\ \langle x^*,x\rangle=\|x\|\}$ for $x \neq0$; the subdifferential need not be a singleton, and the nondifferentiability of $f$ at $0$ is exactly the multivaluedness of $\partial f(0)$.

### Ekeland's Variational Principle

**Theorem (Ekeland).** Let $(X,d)$ be a complete metric space and let $f:X\to\mathbb{R}\cup\{+\infty\}$ be proper, lower semicontinuous and bounded below. For every $\epsilon>0$ there is $x_\epsilon \in X$ with

$$
f(x_\epsilon)\le\inf_Xf+\epsilon, \qquad f(x_\epsilon)\le f(x)+\epsilon\,d(x,x_\epsilon) \quad \text{for all } x \in X .
$$

Equivalently, $x_\epsilon$ is a strict minimiser of the perturbed functional $x\mapsto f(x)+\epsilon\,d(x,x_\epsilon)$.

*Proof (sketch).* Choose $x_0$ with $f(x_0)\le\inf f+\epsilon$ and order the space by $x\preceq y \iff f(x)+\epsilon\,d(x,y)\le f(y)$. Having chosen $x_n$, put $S_n=\{x:x\preceq x_n\}$ and choose $x_{n+1} \in S_n$ with $f(x_{n+1})\le\inf_{S_n}f+2^{-(n+1)}\epsilon$. Then $\epsilon\,d(x_n,x_{n+1})\le f(x_n)-f(x_{n+1})$, so

$$
\sum_{n}d(x_n,x_{n+1})\le\frac{f(x_0)-\inf f}{\epsilon}<\infty ,
$$

and the sequence is Cauchy; let $x_\epsilon$ be its limit. The order is closed under limits (by lower semicontinuity of $f$ and continuity of $d$), so $x_\epsilon\preceq x_n$ for every $n$. If some $x \neq x_\epsilon$ had $f(x)<f(x_\epsilon)-\epsilon\,d(x,x_\epsilon)$, then $x\preceq x_\epsilon\preceq x_n$ for all $n$, whence $f(x)\ge\inf_{S_n}f\ge f(x_{n+1})-2^{-(n+1)}\epsilon\to f(x_\epsilon)$, a contradiction; hence $f(x_\epsilon)\le f(x)+\epsilon\,d(x,x_\epsilon)$ for all $x$, and $f(x_\epsilon)\le f(x_0)\le\inf f+\epsilon$. $\square$

**Corollary.** If $f$ is bounded below, l.s.c. and not identically $+\infty$, then for every $\epsilon>0$ there is $x_\epsilon$ with $f(x_\epsilon)\le\inf f+\epsilon$ and $\operatorname{dist}(0,\partial f(x_\epsilon))\le\epsilon$ when $f$ is convex and $X$ is a Banach space; hence approximate minimisers of a convex functional are approximate critical points, and an exact minimiser satisfies $0 \in\partial f(x)$.

## Monotone Operators

### Definitions and Maximality

**Definition.** An operator $A:X\rightrightarrows X^*$ (a multivalued map) is **monotone** if

$$
\langle x^*-y^*,x-y\rangle\ge0 \quad \text{for all } x,y \in X,\ x^* \in Ax,\ y^* \in Ay ,
$$

and **strictly monotone** if the inequality is strict for $x \neq y$. It is **maximal monotone** if it is monotone and its graph is maximal in $X\times X^*$ with respect to inclusion among monotone graphs. It is **coercive** if $\inf_{x^*\in Ax}\langle x^*,x\rangle/\|x\|\to+\infty$ as $\|x\|\to\infty$, and a single-valued operator is **hemicontinuous** if $t\mapsto\langle A(x+ty),z\rangle$ is continuous at $t=0$ for all $x,y,z \in X$. The **duality map** $J:X\rightrightarrows X^*$ is

$$
J(x)=\{x^* \in X^*:\langle x^*,x\rangle=\|x\|^2=\|x^*\|^2\},
$$

which is single-valued when $X$ is strictly convex, and $J$ is maximal monotone and coercive.

**Theorem (Minty–Browder).** A monotone operator $A:X\rightrightarrows X^*$ is maximal if and only if $R(A+J)=X^*$, that is, if and only if the equation $x^* \in Ax+Jx$ is solvable for every $x^* \in X^*$. A maximal monotone and coercive operator is surjective, $R(A)=X^*$.

*Proof (sketch).* The necessity is the surjectivity of a maximal monotone perturbation of $J$, proved by a Galerkin approximation in finite-dimensional subspaces and a monotonicity argument passing to the limit; the sufficiency follows because a monotone operator whose sum with $J$ is surjective cannot have a proper monotone extension. The coercivity gives the boundedness of the solutions of $x^*\in Ax+Jx$ and the surjectivity of $A$ itself. The argument is the standard one of Minty and Browder, cited below. $\square$

**Theorem (Rockafellar).** The subdifferential $\partial f$ of a proper convex lower semicontinuous function is maximal monotone; conversely a maximal monotone operator is the subdifferential of a proper convex lower semicontinuous function exactly when it is cyclically monotone, that is, when

$$
\sum_{j=1}^{m}\langle x_j^*,x_j-x_{j+1}\rangle\ge0 \qquad (x_{m+1}=x_1)
$$

for every finite cycle, and then the function is recovered from $A$ by the formula $f(x)=\sup\bigl(\langle a_0,x\rangle+\sum_{j}\langle x_j^*,x_{j+1}-x_j\rangle\bigr)$ over the finite chains in the graph of $A$. The inclusion $0 \in Ax$ is the abstract form of a variational inequality, whose solvability theory follows from the surjectivity theorem above.

**Example (the p-Laplacian).** On $W^{1,p}_0(\Omega)$ the operator $Au=-\operatorname{div}(|\nabla u|^{p-2}\nabla u)$ is monotone, coercive and hemicontinuous, hence maximal monotone and surjective onto $W^{-1,q}(\Omega)$ with $\frac1p+\frac1q=1$; the equation $Au=f$ has a unique solution for every $f$, and the monotonicity is the replacement for the ellipticity that is unavailable in the nonlinear setting. The example and its boundary-value theory belong.

## Variational Methods

### The Direct Method

**Theorem (direct method).** Let $X$ be a reflexive Banach space and $F:X\to\mathbb{R}\cup\{+\infty\}$ proper, coercive and weakly lower semicontinuous. Then $F$ attains its minimum on $X$, and the set of minimisers is weakly closed and convex when $F$ is convex.

*Proof.* Choose a minimising sequence $(x_n)$ with $F(x_n)\to\inf F$; coercivity bounds it, reflexivity gives a weakly convergent subsequence $x_{n_k}\rightharpoonup x$, weak lower semicontinuity gives $F(x)\le\liminf F(x_{n_k})=\inf F$, and hence $F(x)=\inf F$. $\square$

This is the fundamental existence theorem of the calculus of variations; the technical work in its applications is the verification of the weak lower semicontinuity and the coercivity in the function space of the problem, which is the content .

### The Palais–Smale Condition and the Deformation Lemma

**Definition.** Let $F \in C^1(X,\mathbb{R})$. A sequence $(u_n)$ is a **Palais–Smale sequence at level $c$** if $F(u_n)\to c$ and $F'(u_n)\to0$; the functional satisfies the **Palais–Smale condition** $(PS)_c$ if every such sequence has a convergent subsequence. A point $u$ is **critical** if $F'(u)=0$, and $c$ is a **critical value** if some critical point has $F(u)=c$.

**Lemma (deformation).** Let $F \in C^1(X,\mathbb{R})$ satisfy $(PS)_c$ and suppose $c$ is not a critical value. Then there exist $\delta>0$, $\epsilon>0$ and a homeomorphism $\eta:X\to X$ isotopic to the identity with

$$
\eta\bigl(\{F\le c+\epsilon\}\bigr)\subseteq\{F\le c-\epsilon\}, \qquad \eta(u)=u \text{ whenever } |F(u)-c|>\delta .
$$

*Proof (sketch).* One constructs a pseudogradient vector field $v(u)$ with $\langle F'(u),v(u)\rangle\ge\frac12\|F'(u)\|^2$ and $\|v(u)\|\le\|F'(u)\|$, and lets $\eta$ be the time-one map of the flow $-\dot u=v(u)$ on the region where $F'\neq0$; the Palais–Smale condition ensures that the flow exists for the required time and that the region $\{c-\epsilon\le F\le c+\epsilon,\ F'=0\}$ is empty for small $\epsilon$. $\square$

### The Minimax Principle and the Mountain Pass

**Theorem (minimax).** Let $F \in C^1(X,\mathbb{R})$, let $\mathcal F$ be a family of subsets of $X$ that is invariant under the homeomorphisms isotopic to the identity, and put

$$
c=\inf_{S \in\mathcal F}\sup_{u \in S}F(u) .
$$

If $c$ is finite and $F$ satisfies $(PS)_c$, then $c$ is a critical value of $F$.

*Proof (sketch).* If $c$ were not critical, the deformation lemma applied with $\eta$ would carry every $S$ with $\sup_SF\le c+\epsilon$ into $\{F\le c-\epsilon\}$, contradicting the definition of $c$ as the infimum of the maxima. $\square$

**Theorem (mountain pass).** Let $X$ be a Banach space, $F \in C^1(X,\mathbb{R})$ with $F(0)=0$, and suppose there are $r>0$ and $\rho>0$ with

$$
F(u)\ge\rho \text{ for } \|u\|=r, \qquad \text{and there is } v \text{ with } \|v\|>r \text{ and } F(v)<\rho .
$$

Let $\Gamma=\{\gamma \in C([0,1],X):\gamma(0)=0,\ \gamma(1)=v\}$ and

$$
c=\inf_{\gamma \in\Gamma}\max_{t \in[0,1]}F(\gamma(t)) \ge\rho .
$$

If $F$ satisfies $(PS)_c$, then $c$ is a critical value of $F$, and the corresponding critical point is not the origin.

*Proof (sketch).* The family $\Gamma$ is invariant under the homeomorphisms of $X$ isotopic to the identity fixing $0$ and $v$, so the minimax principle applies. $\square$

**Example (a semilinear problem).** On $H_0^1(\Omega)$ let $F(u)=\frac12\int_\Omega|\nabla u|^2dx-\int_\Omega G(u)\,dx$ with $G'=g$ of subcritical growth and $g(u)=o(u)$ at $0$; the origin is a local minimum, the energy is unbounded below along rays when $G$ is superquadratic, and the mountain pass geometry holds; the Palais–Smale condition follows from the compactness of the embedding $H_0^1\hookrightarrow L^2$ and the growth hypothesis, so the theorem produces a nontrivial solution of $-\Delta u=g(u)$ with $u=0$ on the boundary. The functional-analytic scheme is the content of the present section; the elliptic existence theory, the regularity of the solution and the maximum principle belong .

### Ljusternik–Schnirelmann Theory

**Definition.** The **Ljusternik–Schnirelmann category** $\operatorname{cat}_X(S)$ of a closed subset $S \subseteq X$ is the least number of closed sets contractible in $X$ whose union covers $S$. The **genus** $\gamma(S)$ is the least $n$ for which there exists an odd continuous map $S\to S^{n-1}$, the unit sphere of $\mathbb{R}^n$, with the conventions $\gamma(\varnothing)=0$ and $\gamma(S)=+\infty$ if no such $n$ exists; it is the $Z_2$ measure of size adapted to functionals invariant under $u\mapsto-u$.

**Theorem (Ljusternik–Schnirelmann).** Let $F \in C^1(X,\mathbb{R})$ satisfy $(PS)_c$ for every $c$ and be bounded below. Then the minimax values

$$
c_k=\inf_{S:\ \operatorname{cat}_X(S)\ge k}\ \sup_{u \in S}F(u), \qquad k=1,2,\dots
$$

are critical values, and if the sequence is finite it terminates in a value below which there are no critical values; consequently a functional bounded below with infinitely many distinct minimax values has infinitely many critical points. For a functional that is even, $F(-u)=F(u)$, and bounded below, the genus replaces the category,

$$
c_k=\inf_{\gamma(S)\ge k}\ \sup_{u \in S}F(u), \qquad k=1,2,\dots,
$$

and the critical points so produced occur in pairs $\pm u$.

The theory gives multiplicity results — several solutions where the direct method gives one — and it is the functional-analytic input to the existence of multiple solutions of symmetric variational problems, developed and applied to boundary problems.

## Summary

Nonlinear functional analysis replaces the linear algebra of a single operator by the study of a nonlinear map and of its derivative, and by the study of a functional and of its critical points. A map $f:D\to Y$ that is $C^k$ with $f'(x_0)$ invertible is a local $C^k$ diffeomorphism, by the inverse function theorem, and a level set with invertible partial derivative is locally a graph, by the implicit function theorem; the surjective case is Lyusternik's theorem, $f$ being locally surjective with the estimate $\|x-x_0\|\le C\|f(x)-f(x_0)\|$, and the level set is then a $C^k$ submanifold of dimension $\dim\ker f'(x_0)$. Newton's method converges quadratically under the Kantorovich hypotheses.

For a convex functional the derivative is replaced by the **subdifferential** $\partial f(x)=\{x^*:f(y)\ge f(x)+\langle x^*,y-x\rangle\}$, which is a convex weak-$*$ closed set, nonempty at interior points of the effective domain, a singleton exactly at the points of Gâteaux differentiability, and the minimiser criterion is $0 \in\partial f(x)$. The Legendre–Fenchel conjugate $f^*(x^*)=\sup_x(\langle x^*,x\rangle-f(x))$ satisfies $f^{**}=f$ exactly for convex l.s.c. proper $f$ and inverts the subdifferential, and Ekeland's variational principle produces, for every $\epsilon>0$, a point that minimises $f(\cdot)+\epsilon\,d(\cdot,x_\epsilon)$ and is therefore an approximate minimiser of $f$; for a convex functional such a point is an approximate critical point. A monotone operator $A:X\rightrightarrows X^*$ with $\langle x^*-y^*,x-y\rangle\ge0$ is maximal exactly when $A+J$ is surjective, by the Minty–Browder theorem, and maximal monotone and coercive operators are surjective; the subdifferential of a convex l.s.c. proper function is maximal monotone, so convex minimisation is a special case of the solvability of variational inequalities.

For a functional that is not convex the global theory is variational. The direct method gives a minimiser for a coercive weakly lower semicontinuous functional on a reflexive space; the Palais–Smale condition and the deformation lemma yield the minimax principle, that $c=\inf_{S\in\mathcal F}\sup_SF$ is a critical value when $\mathcal F$ is invariant under isotopies and $(PS)_c$ holds; the mountain pass theorem is the case of the family of paths joining a point to a point of lower energy, and produces a nontrivial solution of the semilinear problem $-\Delta u=g(u)$ under subcritical growth; and the Ljusternik–Schnirelmann category and genus count the minimax levels and give the multiplicity of critical points for symmetric functionals. The topological fixed-point theorems and the degree are not covered here.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $X,Y,Z$ | Banach spaces over $\mathbb{K}=\mathbb{R}$ or $\mathbb{C}$ |
| $B(X,Y)$, $X^*$ | bounded operators, dual space |
| $f'(x)=Df(x)$ | Fréchet derivative |
| $C^k$, $C^{k,\alpha}$ | differentiability classes |
| $F$ | a functional $X\to\mathbb{R}\cup\{+\infty\}$ |
| $\operatorname{dom}f$ | effective domain of a convex function |
| $\partial f(x)$ | subdifferential of a convex function |
| $f^*$, $f^{**}$ | Legendre–Fenchel conjugate and biconjugate |
| $\delta_C$, $\sigma_C$, $N_C$ | indicator, support function, normal cone of a convex set |
| $(PS)_c$ | Palais–Smale condition at level $c$ |
| $c$, $c_k$ | minimax values |
| $A:X\rightrightarrows X^*$ | multivalued monotone operator |
| $J$ | duality map |
| $\operatorname{cat}_X(S)$, $\gamma(S)$ | Ljusternik–Schnirelmann category and genus |
| $T$ | contraction with constant $\kappa$ |
| $\eta$ | deformation homeomorphism |







## Further Reading

- Stefan Banach, "Sur les opérations dans les ensembles abstraits et leur application aux équations intégrales", *Fundamenta Mathematicae* 3 (1922), 133–181, for the contraction principle and the beginnings of nonlinear analysis in Banach spaces.
- Leonid A. Lyusternik, "On conditional extrema of functionals", *Matematicheskii Sbornik* 41 (1934), 390–401, for the theorem on local surjectivity and the beginnings of Ljusternik–Schnirelmann theory.
- Leonid V. Kantorovich, "On Newton's method for functional equations", *Doklady Akademii Nauk SSSR* 59 (1948), 1237–1240, for the convergence theorem for Newton's method.
- Ralph T. Rockafellar, *Convex Analysis* (Princeton University Press, 1970), for convex functions, subdifferentials, conjugates and the maximal monotonicity theorem.
- Ivar Ekeland, "On the variational principle", *Journal of Mathematical Analysis and Applications* 47 (1974), 324–353, for the variational principle and its applications.
- George J. Minty, "Monotone (nonlinear) operators in Hilbert space", *Duke Mathematical Journal* 29 (1962), 341–346, and Felix E. Browder, "Nonlinear monotone and accretive operators in Banach spaces", *Proceedings of the National Academy of Sciences* 61 (1968), 388–393, for the maximality and surjectivity theory of monotone operators.
- Richard S. Palais and Stephen Smale, "A generalized Morse theory", *Bulletin of the American Mathematical Society* 70 (1964), 165–172, for the Palais–Smale condition and the deformation lemma.
- Antonio Ambrosetti and Paul H. Rabinowitz, "Dual variational methods in critical point theory and applications", *Journal of Functional Analysis* 14 (1973), 349–381, for the mountain pass theorem and its applications.
- Lamberto Cesari, *Optimization—Theory and Applications* (Springer, 1983), for the direct method, lower semicontinuity and the calculus of variations.
