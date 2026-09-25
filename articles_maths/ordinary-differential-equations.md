
# __Ordinary Differential Equations__

## Introduction

An ordinary differential equation relates a function of one real variable to its derivatives. It is the first subject in which the calculus of Part III becomes an object of study rather than a tool: the local existence theorem is the contraction mapping principle in action, the linear theory is a theorem about the matrix exponential, and the qualitative theory is a statement about the eigenvalues of a linearisation. This article develops that theory once, in the general setting of a Banach space, because the arguments do not become harder there and the finite-dimensional case is then the case in which the linear map is a matrix.

The scalar field is $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, and the ambient space is a Banach space $X$ over $\mathbb{K}$ in the sense of *Banach and Hilbert Spaces*; in the linear theory $X$ is finite-dimensional and the operator is a matrix. The calculus used is the differential calculus on normed spaces and its completeness-based cornerstones. Where a result needs completeness of $X$ rather than merely a norm, this is said. Nothing below needs the ground ring to be a field other than through the scalar field $\mathbb{K}$; the analysis of an ordinary differential equation is a real or complex construction.

The article proceeds from the local to the global and from the nonlinear to the linear. It establishes the Picard–Lindelöf theorem and the maximal interval of existence, the Gronwall inequality and continuous dependence on the data, the reduction of a higher-order equation to a first-order system, the matrix exponential with the variation of constants formula, linear equations with constant coefficients and the characteristic equation, boundary-value problems with their Green's functions, the Sturm–Liouville eigenvalue problem and its eigenfunction expansion, and finally the phase portrait of an autonomous planar system with the classification of equilibria by the eigenvalues of the linearisation. The special equations of mathematical physics — Bessel's equation and Legendre's equation among them — are introduced here as linear equations with regular singular points, and their solutions are the special functions treated per system in Part V.

## The First-Order Equation

### The Initial-Value Problem

**Definition.** Let $I \subseteq \mathbb{R}$ be an interval, $X$ a Banach space over $\mathbb{K}$, and $f : I \times X \to X$ a function. The **ordinary differential equation** determined by $f$ is

$$
y'(t) = f(t, y(t)),
$$

and the **initial-value problem** with initial datum $(t_0, y_0) \in I \times X$ is the pair

$$
y'(t) = f(t,y(t)), \qquad y(t_0) = y_0 .
$$

A **solution** on an interval $J \subseteq I$ containing $t_0$ is a differentiable map $y : J \to X$ satisfying both conditions; when $t_0$ is not named, a **solution** is any such map on any interval on which the equation is meaningful.

The equation is **autonomous** if $f$ does not depend on $t$, **linear** if $f(t,y) = A(t)y + b(t)$ for a family $A(t)$ of bounded operators and a map $b$, and **homogeneous** in that case if $b = 0$. An equation of **order $n$** relates $y$ to its first $n$ derivatives, and is written $y^{(n)} = g(t, y, y', \dots, y^{(n-1)})$.

**Proposition (the integral equation).** Let $f : I \times X \to X$ be continuous. Then a continuous map $y : J \to X$ is a solution of the initial-value problem with datum $(t_0,y_0)$ if and only if it satisfies the **integral equation**

$$
y(t) = y_0 + \int_{t_0}^{t} f(s, y(s))\, ds \qquad (t \in J).
$$

*Proof.* If $y$ solves the initial-value problem, the fundamental theorem of calculus applied to each side gives the integral equation, the integral of a continuous $X$-valued map being defined by the Bochner integral of *Measure Theory and Integration*, or componentwise in the finite-dimensional case. Conversely, if the integral equation holds, the right side is differentiable with derivative $f(t,y(t))$ by continuity of $f$ and of $y$, and the value at $t_0$ is $y_0$. $\square$

The proposition is the reason the existence theorem is a fixed-point theorem: it replaces differentiation, which loses information on a merely continuous map, by integration, which improves it.

### The Lipschitz Condition and Picard–Lindelöf

**Definition.** A map $f : I \times X \to X$ is **Lipschitz in its second variable**, or simply **Lipschitz**, with constant $L$ if

$$
\|f(t,y) - f(t,z)\| \le L\|y - z\| \qquad \text{for all } t \in I,\ y, z \in X ,
$$

and **locally Lipschitz in the second variable** if every point of $I \times X$ has a neighbourhood on which this holds with some constant. It is **uniformly Lipschitz on a strip** $J \times X$ if a single $L$ works for all $t \in J$.

**Theorem (Picard–Lindelöf).** Let $f : I \times X \to X$ be continuous and locally Lipschitz in its second variable, and let $(t_0,y_0) \in I \times X$. Then there is $\delta > 0$ such that the initial-value problem has a unique solution on $(t_0-\delta, t_0+\delta)$.

*Proof.* Choose $a, b > 0$ with $[t_0-a, t_0+a] \times \overline{B}(y_0,b) \subseteq I \times X$; on this set $f$ is bounded, say $\|f\| \le M$, and Lipschitz with constant $L$. Put $\delta = \min(a, b/M, 1/(2L))$ and let $\mathcal{C}$ be the set of continuous maps $y : [t_0-\delta, t_0+\delta] \to X$ with $y(t_0) = y_0$ and $\|y(t)-y_0\| \le b$; with the supremum metric, $\mathcal{C}$ is a complete metric space, being a closed subset of the Banach space $C([t_0-\delta,t_0+\delta],X)$. Define

$$
T(y)(t) = y_0 + \int_{t_0}^{t} f(s,y(s))\, ds .
$$

The integrand is continuous and bounded by $M$, so $\|T(y)(t) - y_0\| \le M|t-t_0| \le M\delta \le b$, and $T(y)$ is continuous: $T$ maps $\mathcal{C}$ to itself. For $y, z \in \mathcal{C}$,

$$
\|T(y)(t) - T(z)(t)\| \le \Bigl|\int_{t_0}^{t}\|f(s,y(s)) - f(s,z(s))\|\,ds\Bigr| \le L|t-t_0|\,\|y-z\|_\infty \le \tfrac12\|y-z\|_\infty ,
$$

so $T$ is a contraction of constant $\tfrac12$. By the contraction mapping principle $T$ has a unique fixed point in $\mathcal{C}$, and by the integral equation this fixed point is exactly the solution. $\square$

The contraction mapping principle is quoted here as the standard completeness argument of the theory of metric and complete spaces; it is the same statement as the one used for the inverse function theorem in the differential calculus on normed spaces.

**Example.** For the scalar equation $y' = y$, $y(0) = 1$, the iteration of $T$ from $y_{(0)} \equiv 1$ gives $y_{(n)}(t) = \sum_{k=0}^{n} t^k/k!$, so the fixed point is $\exp$, and the theorem reproduces the exponential series. The constant $\delta$ obtained in the proof is far from optimal; the solution exists on all of $\mathbb{R}$.

**Theorem (Peano).** If $f$ is continuous on a neighbourhood of $(t_0,y_0)$ and bounded there, the initial-value problem has at least one solution on some interval about $t_0$. The Lipschitz hypothesis is not needed for existence, only for uniqueness.

*Proof.* Quoted as standard (Peano's theorem). The proof uses the Arzelà–Ascoli theorem: the Euler polygons are an equicontinuous family taking values in a compact set, so a subsequence converges uniformly, and the limit solves the integral equation. $\square$

**Example (non-uniqueness).** For $y' = \sqrt{|y|}$ with $y(0) = 0$ the map $f(y) = \sqrt{|y|}$ is continuous and not Lipschitz at $0$. Besides $y \equiv 0$, the family

$$
y_c(t) = \begin{cases} 0, & t \le c, \\ \tfrac14(t-c)^2, & t > c \end{cases}
$$

solves the problem for every $c \ge 0$, so the solution is not unique; this is precisely what the Lipschitz condition rules out.

### The Maximal Interval of Existence

**Definition.** A solution $y : J \to X$ of the initial-value problem is **maximal** if no solution on a strictly larger interval extends it; $J$ is then the **maximal interval of existence**. A maximal solution is **complete** if $J = I$.

**Theorem (maximal interval).** Let $f : I \times X \to X$ be continuous and locally Lipschitz in its second variable. Then every initial-value problem has a maximal solution, its maximal interval $J$ is open, and if $J = (\alpha, \beta)$ is a proper subinterval of $I$ then $y(t)$ leaves every compact subset of $X$ as $t \to \alpha^+$ or $t \to \beta^-$.

*Proof.* The solutions form a directed family under extension and their union over a chain is a solution, so Zorn's lemma produces a maximal one; alternatively the union of the local solutions constructed at successive points of the interval is a solution, and the maximal interval is open because local existence holds at every interior point. If a compact $K \subseteq X$ contained $y(t_n)$ for a sequence $t_n \to \beta^-$, then by compactness a subsequence would converge to some $y^*$; the local solution through $(\beta, y^*)$ would extend the solution past $\beta$, contradicting maximality. $\square$

**Corollary.** If the maximal interval is bounded above by $\beta < \infty$ and yet $y$ is bounded on $[t_0,\beta)$, then $f$ cannot be bounded and uniformly Lipschitz on the strip $[t_0,\beta)\times X$, and the solution has no limit in $X$ at $\beta$: it **blows up** in finite time.

*Proof.* If $\|y\|\le R$ on $[t_0,\beta)$ and $f$ is bounded by $M$ and Lipschitz with constant $L$ on the strip, the argument of Picard–Lindelöf with a uniform step size extends the solution beyond $\beta$, a contradiction. Blow-up rather than escape to the boundary of $X$ is therefore the only possibility when $X$ is finite-dimensional. $\square$

**Example.** For $y' = y^2$ with $y(0) = 1$ the solution is $y(t) = 1/(1-t)$ on $(-\infty,1)$, whose maximal interval is bounded above by $1$, and $|y(t)| \to \infty$ as $t \to 1^-$.

### Gronwall and Continuous Dependence

**Lemma (Bellman–Grönwall).** Let $u, \beta : [t_0,t_1] \to \mathbb{R}$ be continuous with $\beta \ge 0$ and let $a \ge 0$. If

$$
u(t) \le a + \int_{t_0}^{t}\beta(s)\,u(s)\,ds \qquad (t \in [t_0,t_1]),
$$

then

$$
u(t) \le a\,\exp\Bigl(\int_{t_0}^{t}\beta(s)\,ds\Bigr) .
$$

*Proof.* Put $v(t) = a + \int_{t_0}^t \beta u$; then $v \ge u \ge 0$ and $v'(t) = \beta(t)u(t) \le \beta(t)v(t)$, so $(v(t)e^{-\int_{t_0}^{t}\beta})' \le 0$, and integrating gives $v(t) \le v(t_0)e^{\int_{t_0}^{t}\beta} = a\,e^{\int_{t_0}^{t}\beta}$. $\square$

**Theorem (continuous dependence).** Let $f : I \times X \to X$ be continuous and Lipschitz with constant $L$ in its second variable, and let $y, z$ be solutions of $y' = f(t,y)$ with $y(t_0) = y_0$, $z(t_0) = z_0$ on a common interval $[t_0,t_1]$. Then

$$
\|y(t) - z(t)\| \le \|y_0 - z_0\|\,e^{L(t-t_0)} \qquad (t \in [t_0,t_1]).
$$

*Proof.* Subtracting the integral equations and applying the Lipschitz condition gives $u(t) \le \|y_0-z_0\| + L\int_{t_0}^t u(s)\,ds$ for $u = \|y-z\|$; Gronwall gives the estimate. $\square$

**Corollary (uniqueness).** Two solutions with the same initial datum agree on the intersection of their intervals, so the maximal solution is unique. In particular the **flow** $\varphi_t(y_0) = y(t)$ of an autonomous equation is well defined wherever it exists, and $\varphi_{t+s} = \varphi_t \circ \varphi_s$ on the common domain of definition.

The estimate says that the solution depends on the initial datum Lipschitz-continuously with a constant growing exponentially in $t$, and that this exponential growth is the worst case; for a linear equation $y' = Ay$ the sharp constant is $\|e^{tA}\|$, which need not equal $e^{\|A\|t}$.

## Systems and Higher-Order Equations

**Proposition (reduction to a first-order system).** The order-$n$ equation $y^{(n)} = g(t, y, y', \dots, y^{(n-1)})$ on $X$ is equivalent to the first-order system

$$
Y' = F(t, Y), \qquad F(t, Y) = \bigl(Y_1, \dots, Y_{n-1}, g(t, Y_0, \dots, Y_{n-1})\bigr),
$$

on the Banach space $X^n$, under the correspondence $Y = (y, y', \dots, y^{(n-1)})$.

*Proof.* If $y$ is $n$ times differentiable then $Y$ is differentiable with the displayed derivative; conversely a solution $Y$ of the system has $Y_k = Y_{k-1}'$ for $k \ge 1$, so $Y_0$ is $n$ times differentiable and satisfies the equation. $\square$

Consequently the existence, uniqueness, maximal-interval and continuous-dependence theorems proved for the first-order equation apply to the order-$n$ equation with no change; only the norm on $X^n$ has to be chosen, and any of the usual equivalent product norms serves.

**Example (the pendulum).** The equation $\theta'' + \sin\theta = 0$ reduces to the planar system $(\theta', \omega') = (\omega, -\sin\theta)$ on $\mathbb{R}^2$, which is autonomous with $f$ smooth, hence locally Lipschitz, so every initial datum has a unique maximal solution; the energy $\tfrac12\omega^2 - \cos\theta$ is constant along solutions, and boundedness of the energy together with the corollary on maximal intervals shows that solutions are defined for all real $t$.

**Remark.** The reduction converts a scalar equation of order $n$ into a system whose dimension is $n$ times the dimension of $X$, and it is the reason the linear theory below is stated for systems: the scalar linear equation of order $n$ is recovered as a special case.

## Linear Systems

### The Matrix Exponential

**Definition.** For a bounded linear operator $A \in B(X)$ the **exponential** is

$$
e^{A} = \sum_{n\ge 0}\frac{A^n}{n!} ,
$$

the series converging in the operator norm because the normed algebra $B(X)$ is complete and $\|A^n\| \le \|A\|^n$. The map $t \mapsto e^{tA}$ is the **one-parameter group** generated by $A$.

The convergence and the algebraic properties used below are those of the exponential in a Banach algebra, given in *Topological Algebras and Banach Algebras*: $B(X)$ is a unital Banach algebra and $\exp$ converges everywhere there. The following collects what the linear theory needs.

**Theorem (properties of the exponential).** For $A, B \in B(X)$:

**(a)** $e^{0} = I$ and $e^{A}$ is invertible with inverse $e^{-A}$;

**(b)** if $AB = BA$ then $e^{A+B} = e^{A}e^{B}$, and in particular $e^{(s+t)A} = e^{sA}e^{tA}$ for all $s, t \in \mathbb{R}$;

**(c)** $t \mapsto e^{tA}$ is differentiable with $\dfrac{d}{dt}e^{tA} = A e^{tA} = e^{tA}A$;

**(d)** $\|e^{tA}\| \le e^{|t|\,\|A\|}$, and $\|e^{tA} - I\| \le |t|\|A\|e^{|t|\|A\|}$.

*Proof.* (a) and (b) are the elementary properties of the exponential series in a Banach algebra. For (c), the difference quotient for the series term by term gives $\frac{1}{h}(e^{(t+h)A} - e^{tA}) = e^{tA}\frac{1}{h}(e^{hA}-I)$, and $\frac{1}{h}(e^{hA}-I) \to A$ as $h \to 0$ by the estimate in (d). (d) is the triangle inequality applied to the series. $\square$

### The Fundamental Matrix and Variation of Constants

**Definition.** For a linear system $y' = A(t)y$ with $A : I \to B(X)$ continuous, a **fundamental matrix** at $t_0 \in I$ is the map $t \mapsto \Phi(t)$ of bounded operators solving

$$
\Phi'(t) = A(t)\Phi(t), \qquad \Phi(t_0) = I .
$$

**Theorem.** For every $t_0 \in I$ the fundamental matrix exists on all of $I$, is unique, and is invertible for every $t$; when $A$ is constant, $\Phi(t) = e^{(t-t_0)A}$ and $\Phi$ is a one-parameter group.

*Proof.* The columns of $\Phi$ are the solutions of the initial-value problems with initial data a basis of $X$, and the Picard–Lindelöf theorem gives them locally; the operator $\Phi(t)$ is invertible because $\Phi(t)\Phi(t)^{-1}$ solves the same linear equation as the identity, so if a solution of $y'=A(t)y$ vanished at one point it would vanish identically, and $\det\Phi \neq 0$ follows in finite dimension; equivalently $\Psi(t) = \Phi(t)^{-1}$ solves $\Psi' = -\Psi A(t)$ and a solution with $\Psi(t_0)=I$ exists on all of $I$ by the same theorem. The invertibility in general follows from the identity $\det \Phi(t) = \exp(\int_{t_0}^t \operatorname{tr}A(s)\,ds)$ in finite dimension, and from the group property when $A$ is constant. $\square$

**Theorem (variation of constants).** The solution of the inhomogeneous linear system $y' = A(t)y + b(t)$ with $y(t_0) = y_0$ is

$$
y(t) = \Phi(t)y_0 + \int_{t_0}^{t}\Phi(t)\Phi(s)^{-1}b(s)\,ds .
$$

*Proof.* Write $y(t) = \Phi(t)u(t)$; the product rule and $\Phi' = A\Phi$ give $\Phi u' = b$, so $u' = \Phi^{-1}b$ and $u(t) = y_0 + \int_{t_0}^t \Phi(s)^{-1}b(s)\,ds$. $\square$

When $A$ is constant the formula reads $y(t) = e^{(t-t_0)A}y_0 + \int_{t_0}^{t}e^{(t-s)A}b(s)\,ds$, the second term being the superposition of the responses to impulses at times $s$, which is the interpretation of the exponential as the kernel of the solution operator.

### Constant Coefficients and the Characteristic Equation

Now $X$ is finite-dimensional of dimension $n$ over $\mathbb{K}$ and $A$ is a fixed $n \times n$ matrix. The Jordan form of $A$, treated in *Modules over $k[x]$ and the Jordan Form*, describes the exponential completely.

**Definition.** The **characteristic polynomial** of $A$ is $p_A(\lambda) = \det(\lambda I - A)$, a monic polynomial of degree $n$; its roots are the **eigenvalues** of $A$, and the **characteristic equation** of the equation $y'=Ay$ is $p_A(\lambda) = 0$.

**Theorem (constant coefficients).** With $A$ in Jordan form, $e^{tA}$ is block diagonal with blocks $e^{tJ}$. For a Jordan block $J = \lambda I + N$ with $N$ nilpotent of index $m$,

$$
e^{tJ} = e^{\lambda t}\sum_{k=0}^{m-1}\frac{t^k}{k!}N^{k} ,
$$

so every entry of $e^{tA}$ is a finite sum of terms $t^k e^{\lambda t}$ with $\lambda$ an eigenvalue and $0 \le k < n$.

*Proof.* Since $\lambda I$ and $N$ commute, $e^{tJ} = e^{\lambda t I}e^{tN}$, and the second factor is the finite sum because $N^m=0$. $\square$

**Corollary (scalar equation).** For the scalar equation $y^{(n)} + a_{n-1}y^{(n-1)} + \cdots + a_0 y = 0$ with characteristic polynomial $p(\lambda) = \lambda^n + a_{n-1}\lambda^{n-1} + \cdots + a_0$, the solution space is $n$-dimensional and spanned by the functions $t^k e^{\lambda t}$ over the roots $\lambda$ of $p$ and the powers $0 \le k < $ multiplicity of $\lambda$. The solution is stable — bounded for all $t \ge 0$ — exactly when every root has $\operatorname{Re}\lambda \le 0$ and every root with $\operatorname{Re}\lambda = 0$ is simple.

*Proof.* The reduction to a first-order system has companion matrix whose characteristic polynomial is $p$, and the previous theorem describes $e^{tA}$; boundedness follows from the display, and the converse from the occurrence of $t^k$ with $k \ge 1$ at a repeated eigenvalue on the imaginary axis. $\square$

**Example.** For $y'' + y = 0$ the roots of $\lambda^2+1$ are $\pm i$, and the solutions are $c_1\cos t + c_2\sin t$. For $y'' - y = 0$ the roots are $\pm1$ and the solutions are $c_1e^{t}+c_2e^{-t}$; the first is stable and the second is not, which the eigenvalues already show.

**Example (the rotation matrix).** For $A = \begin{pmatrix}0&-1\\1&0\end{pmatrix}$ the eigenvalues are $\pm i$ and

$$
e^{tA} = \begin{pmatrix}\cos t & -\sin t\\ \sin t & \cos t\end{pmatrix},
$$

as one checks by splitting $A$ into the series of even and odd powers, using $A^2 = -I$.

### Periodic Coefficients

**Theorem (Floquet).** Let $A : \mathbb{R} \to B(\mathbb{C}^n)$ be continuous and $T$-periodic. Then the fundamental matrix has the form

$$
\Phi(t) = P(t)e^{tB},
$$

with $P$ $T$-periodic and invertible and $B$ a constant matrix, the **monodromy logarithm**; $B$ is determined by $\Phi(T) = e^{TB}$ up to the choice of a branch of the logarithm, and the solutions are bounded for all $t$ exactly when the eigenvalues of $\Phi(T)$ have modulus at most $1$, those of modulus $1$ being simple.

*Proof.* Quoted as standard. The matrix $C = \Phi(T)$ is invertible, so it has a logarithm $B$ with $e^{TB}=C$; the product $P(t) = \Phi(t)e^{-tB}$ satisfies $P(t+T) = \Phi(t)\Phi(T)e^{-(t+T)B} = \Phi(t)e^{-tB} = P(t)$, since $\Phi(t+T) = \Phi(t)\Phi(T)$. $\square$

## Boundary-Value Problems and Green's Functions

**Definition.** A **boundary-value problem** consists of a linear differential equation $Ly = f$ on an interval $(a,b)$ together with $n$ linear conditions on the values of $y$ and its derivatives at $a$ and $b$, written $By = 0$. It is **homogeneous** when $f = 0$ and $B$ is unchanged; its **resolvent set** is the set of parameters for which $Ly = f$, $By=0$ has a unique solution for every $f$.

**Theorem (Green's function).** Let $L$ be an order-$n$ linear differential operator with continuous coefficients on $[a,b]$ and let $B$ impose $n$ linearly independent boundary conditions. If the homogeneous problem $Ly=0$, $By=0$ has only the trivial solution, then there is a unique function $G : [a,b]^2 \to \mathbb{K}$, the **Green's function**, such that the solution of $Ly = f$, $By=0$ is

$$
y(x) = \int_a^b G(x,s)\,f(s)\,ds .
$$

The function $G$ is continuous, $G(x,s)$ solves $L_xG = 0$ for $x \neq s$ and satisfies the boundary conditions in $x$, and at $x = s$ its derivatives up to order $n-2$ are continuous while

$$
\partial_x^{n-1}G(s^+,s) - \partial_x^{n-1}G(s^-,s) = \frac{1}{a_n(s)} ,
$$

where $a_n$ is the leading coefficient of $L$.

*Proof.* Construct $G$ from a basis of solutions of $Ly=0$ adjusted to the boundary conditions, as the standard variation-of-parameters construction; the jump condition makes $L_x$ of the integral return $f$, and the boundary conditions are satisfied because each factor does, since the integral in $s$ commutes with the boundary conditions in $x$. Uniqueness follows from the uniqueness of the solution of the boundary-value problem. $\square$

**Example.** For $-y'' = f$ on $(0,1)$ with $y(0)=y(1)=0$ the Green's function is

$$
G(x,s) = \begin{cases} x(1-s), & x \le s,\\ s(1-x), & x > s,\end{cases}
$$

which is symmetric, continuous, piecewise linear and vanishes at both endpoints; the jump in $\partial_xG$ at $x=s$ is $-1$, matching the leading coefficient $-1$.

The Green's function is the kernel of the inverse of the differential operator, and its symmetry $G(x,s) = G(s,x)$ for a self-adjoint problem is the symmetry of the inverse operator. The theory of the inverse as a bounded operator, and of the problem as a Fredholm equation when the homogeneous problem is nontrivial, is the Fredholm theory of operators.

## Sturm–Liouville Problems

### The Self-Adjoint Form

**Definition.** A **Sturm–Liouville problem** on $(a,b)$ is an eigenvalue problem

$$
-(p\,y')' + q\,y = \lambda\, w\, y ,
$$

with $p > 0$, $w > 0$ and $q$ real and continuous on $[a,b]$, together with separated boundary conditions

$$
\alpha_1 y(a) + \alpha_2 y'(a) = 0, \qquad \beta_1 y(b) + \beta_2 y'(b) = 0 ,
$$

at least one of $(\alpha_1,\alpha_2)$ and one of $(\beta_1,\beta_2)$ being nonzero. The function $w$ is the **weight**.

In the **regular** case $p$ is positive and continuous on the closed interval and $w$ is positive and continuous there; a **singular** endpoint is one at which $p$ vanishes or the interval is unbounded, and it is **limit-circle** or **limit-point** according to the behaviour of the solutions of the equation at it. Bessel's equation and Legendre's equation are singular Sturm–Liouville problems, and they are the origin of the special functions of Part V.

**Theorem (self-adjointness).** On the Hilbert space $L^2((a,b), w\,dx)$ of *Measure Theory and Integration* the operator $Ly = \frac{1}{w}(-(py')' + qy)$ with domain the smooth functions satisfying the boundary conditions is symmetric,

$$
\langle Ly, z\rangle_w = \langle y, Lz\rangle_w ,
$$

and its closure is self-adjoint when the problem is regular or limit-point at each singular endpoint.

*Proof.* Integrating by parts twice,

$$
\int_a^b \bigl(-(py')' + qy\bigr)\bar z\,dx = \bigl[-py'\bar z + py\bar z'\bigr]_a^b + \int_a^b y\,\overline{-(pz')' + qz}\,dx ,
$$

and the boundary term vanishes because both $y$ and $z$ satisfy the separated conditions; the self-adjointness of the closure is the standard Weyl–Stone result for limit-point endpoints. $\square$

### The Eigenvalue Expansion

**Theorem (Sturm–Liouville).** For a regular Sturm–Liouville problem the eigenvalues are real, form an increasing sequence $\lambda_1 < \lambda_2 < \cdots$ with $\lambda_n \to \infty$, and to each eigenvalue corresponds a one-dimensional eigenspace. The eigenfunctions $y_n$, normalised in $L^2((a,b),w\,dx)$, are orthonormal and complete: every $f \in L^2((a,b),w\,dx)$ has an expansion

$$
f = \sum_{n\ge1} c_n y_n, \qquad c_n = \int_a^b f(x)\,y_n(x)\,w(x)\,dx ,
$$

convergent in $L^2$ and uniformly absolutely convergent when $f$ is continuous with $f'$ of bounded variation satisfying the boundary conditions. The eigenvalues obey the **asymptotic law**

$$
\lambda_n \sim \Bigl(\frac{n\pi}{\int_a^b\sqrt{w/p}\,dx}\Bigr)^2 \qquad (n \to \infty),
$$

which in the case $p \equiv w \equiv 1$ reduces to $\lambda_n \sim n^2\pi^2/(b-a)^2$.

*Proof.* Symmetry of the operator makes the eigenvalues real, and the Rayleigh quotient

$$
R(y) = \frac{\int_a^b\bigl(p|y'|^2 + q|y|^2\bigr)dx}{\int_a^b|y|^2 w\,dx}
$$

stationarises exactly at the eigenfunctions; the minimum of $R$ over the functions orthogonal to the first $n-1$ eigenfunctions is $\lambda_n$, which is the variational characterisation and shows that the $\lambda_n$ increase and tend to infinity. The simplicity and the asymptotic law are the classical Sturm–Liouville theorems, proved by Sturm's oscillation comparison. $\square$

The expansion is the one-dimensional case of the spectral theorem for self-adjoint operators: the differential operator has compact resolvent and discrete spectrum, exactly as for a compact self-adjoint operator on a Hilbert space, and the orthonormal eigenbasis is the one supplied by the spectral theorem of *Banach and Hilbert Spaces*.

**Example.** For $-y'' = \lambda y$ on $(0,\pi)$ with $y(0)=y(\pi)=0$ the eigenvalues are $\lambda_n = n^2$ with eigenfunctions $y_n(x) = \sqrt{2/\pi}\sin(nx)$, and the expansion is the Fourier sine series. For the Legendre problem $((1-x^2)y')' + \lambda y = 0$ on $(-1,1)$ the eigenvalues are $\lambda_n = n(n+1)$ and the eigenfunctions are the Legendre polynomials, defined by the singular case of the theory.

**Remark.** The eigenfunction expansion is the reason a boundary-value problem for a partial differential equation can be solved by separation of variables: one coordinate is expanded in the eigenfunctions of the corresponding Sturm–Liouville problem, and the remaining equation is an ordinary differential equation for the coefficients.

## Autonomous Systems and the Phase Plane

### Equilibria and Linearisation

**Definition.** For an autonomous equation $y' = f(y)$ a point $y_*$ is an **equilibrium** if $f(y_*) = 0$, and the equilibrium is **stable** if for every neighbourhood $U$ of $y_*$ there is a neighbourhood $V$ with $\varphi_t(V) \subseteq U$ for all $t \ge 0$; it is **asymptotically stable** if in addition $\varphi_t(y) \to y_*$ as $t \to \infty$ for $y$ in some neighbourhood, and **unstable** if it is not stable.

**Theorem (linearisation).** Let $f$ be of class $C^1$ near an equilibrium $y_*$, with derivative $A = Df(y_*)$. Then:

**(a)** if every eigenvalue of $A$ has strictly negative real part, $y_*$ is asymptotically stable;

**(b)** if some eigenvalue of $A$ has strictly positive real part, $y_*$ is unstable;

**(c)** if the eigenvalues of $A$ all have nonpositive real part and some have real part $0$, the linearisation does not decide stability, and the nonlinear terms decide.

*Proof.* The solution is $y(t) = y_* + z(t)$ with $z' = Az + r(z)$, $\|r(z)\| = o(\|z\|)$. If the spectrum of $A$ lies in $\{\operatorname{Re} < 0\}$ then $\|e^{tA}\| \le Ce^{-\gamma t}$ for some $C, \gamma > 0$, and the variation-of-constants formula and Gronwall give decay of $z$ for small $z(0)$; if some eigenvalue has positive real part, the unstable manifold theorem produces solutions leaving every neighbourhood. Statement (c) is the content of the examples below. $\square$

### The Planar Case

For a planar autonomous system $x' = P(x,y)$, $y' = Q(x,y)$ with equilibrium at the origin and linearisation matrix $A = \begin{pmatrix}P_x & P_y\\ Q_x & Q_y\end{pmatrix}$, the eigenvalues $\lambda_1, \lambda_2$ of $A$ classify the phase portrait at the origin in the nondegenerate case $\det A \neq 0$.

**Theorem (classification of planar equilibria).** With $\tau = \operatorname{tr}A$, $\delta = \det A$ and discriminant $\tau^2 - 4\delta$:

| Condition | Eigenvalues | Type | Stability |
|---|---|---|---|
| $\delta < 0$ | real, opposite signs | saddle | unstable |
| $\delta > 0$, $\tau^2 - 4\delta \ge 0$, $\tau < 0$ | real, both negative | stable node | asymptotically stable |
| $\delta > 0$, $\tau^2 - 4\delta \ge 0$, $\tau > 0$ | real, both positive | unstable node | unstable |
| $\delta > 0$, $\tau^2 - 4\delta < 0$, $\tau < 0$ | complex, $\operatorname{Re} < 0$ | stable spiral | asymptotically stable |
| $\delta > 0$, $\tau^2 - 4\delta < 0$, $\tau > 0$ | complex, $\operatorname{Re} > 0$ | unstable spiral | unstable |
| $\delta > 0$, $\tau = 0$ | purely imaginary, $\pm i\omega$ | centre | depends on nonlinear terms |

*Proof.* The classification follows from the form of the real solution $e^{tA}$: real distinct eigenvalues give motion along the eigenvectors, a saddle when the signs differ; a repeated eigenvalue gives a node with possibly a Jordan factor contributing a factor $t$; complex eigenvalues $\alpha \pm i\beta$ give a spiral whose stability is the sign of $\alpha$, the direction of winding being that of the imaginary part. The centre case has eigenvalues purely imaginary and the linear solutions are periodic; a nonlinear perturbation can turn them into a stable or unstable spiral, and the centre is genuinely undecided by the linearisation. $\square$

**Example (a stable spiral).** For $x' = -x - y$, $y' = x - y$ the matrix is $\begin{pmatrix}-1&-1\\1&-1\end{pmatrix}$ with trace $-2$, determinant $2$ and eigenvalues $-1\pm i$; the origin is an asymptotically stable spiral, and solutions spiral inward with rotation period $2\pi$ and radial decay $e^{-t}$.

**Example (a Hamiltonian centre).** For the pendulum $x' = y$, $y' = -\sin x$ the equilibrium at the origin has $\tau = 0$, $\delta = 1$ and eigenvalues $\pm i$, so the linearisation is a centre; the conserved energy $\tfrac12y^2 + 1-\cos x$ has a strict minimum at the origin, and the level sets are closed curves, so the origin is stable but not asymptotically stable — the nonlinear terms here confirm the centre.

**Example (a nonlinear centre becoming a spiral).** For $x' = -y + x(x^2+y^2)$, $y' = x + y(x^2+y^2)$ the linearisation at the origin has eigenvalues $\pm i$; in polar coordinates the equations read $r' = r^3$, $\theta' = 1$, so the origin is an unstable spiral. Changing the sign of the cubic terms makes it asymptotically stable. This is the failure in statement (c) of the linearisation theorem.

## Summary

An ordinary differential equation $y' = f(t,y)$ is equivalent to the integral equation $y(t) = y_0 + \int_{t_0}^t f(s,y(s))\,ds$, and if $f$ is continuous and locally Lipschitz in its second variable the Picard–Lindelöf theorem gives a unique local solution as the fixed point of the contraction $T$. Without the Lipschitz condition Peano's theorem still gives existence and uniqueness can fail. Every solution extends to a maximal open interval, at whose ends the solution either leaves every compact set or blows up in finite time, and the Gronwall inequality gives continuous dependence on the initial datum with an exponential estimate, hence uniqueness.

A higher-order equation reduces to a first-order system, so the same theorems apply. For a linear system $y' = A(t)y$ the fundamental matrix exists on all of the interval and is invertible, the inhomogeneous equation is solved by the variation-of-constants formula $y = \Phi y_0 + \int \Phi(t)\Phi(s)^{-1}b(s)\,ds$, and for constant coefficients the exponential $e^{tA}$ is computed from the Jordan form: every entry is a sum of terms $t^ke^{\lambda t}$ over the eigenvalues $\lambda$, so the characteristic polynomial determines the solution completely and controls its stability. With periodic coefficients Floquet's theorem writes the fundamental matrix as a periodic factor times an exponential.

A linear boundary-value problem with only the trivial solution of its homogeneous part has a Green's function and is solved by $y(x) = \int G(x,s)f(s)\,ds$. A regular Sturm–Liouville problem is a self-adjoint operator with compact resolvent: its eigenvalues are real and simple, tend to infinity, and its eigenfunctions form a complete orthonormal basis of the weighted $L^2$ space, the one-dimensional instance of the spectral theorem. The eigenfunction expansion is the bridge to boundary-value problems for partial differential equations.

For an autonomous system the equilibria are classified by the derivative at the point: eigenvalues with strictly negative real part give asymptotic stability, eigenvalues with strictly positive real part give instability, and a purely imaginary spectrum leaves the question open, as the planar centre examples show. In the plane the trace and determinant of the linearisation tabulate the node, saddle, spiral and centre cases. The reduction of the qualitative theory of these systems to their invariant sets, and the study of the flow when the linearisation is degenerate, is the subject of the dynamical-systems articles of this Part, which are written in parallel and continue the phase-plane analysis begun here.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{K}$ | $\mathbb{R}$ or $\mathbb{C}$ |
| $X$ | Banach space of state variables over $\mathbb{K}$ |
| $I$, $J$ | Interval of the independent variable; maximal interval $J$ |
| $y' = f(t,y)$ | First-order equation; $f$ the vector field or right-hand side |
| $y(t_0) = y_0$ | Initial datum |
| $L$ | Lipschitz constant in the second variable |
| $T$ | Picard operator $T(y)(t) = y_0 + \int_{t_0}^t f(s,y(s))\,ds$ |
| $\varphi_t$ | Flow of an autonomous equation, $\varphi_t(y_0) = y(t)$ |
| $A$, $A(t)$ | Bounded operator of a linear system $y' = Ay + b$ |
| $e^{tA}$ | Matrix (operator) exponential, the solution operator |
| $\Phi(t)$ | Fundamental matrix, $\Phi' = A\Phi$, $\Phi(t_0) = I$ |
| $p_A(\lambda) = \det(\lambda I - A)$ | Characteristic polynomial; $p_A(\lambda)=0$ the characteristic equation |
| $B$ | Monodromy logarithm of a periodic system, $\Phi(t) = P(t)e^{tB}$ |
| $G(x,s)$ | Green's function of a linear boundary-value problem |
| $p$, $q$, $w$ | Sturm–Liouville coefficient, potential and weight |
| $\lambda_n$, $y_n$ | Sturm–Liouville eigenvalues and eigenfunctions |
| $R(y)$ | Rayleigh quotient |
| $y_*$ | Equilibrium of an autonomous system |
| $A = Df(y_*)$, $\tau$, $\delta$ | Linearisation matrix, its trace and determinant |
| node, saddle, spiral, centre | Classification of a planar equilibrium |

## Further Reading

- Earl A. Coddington and Norman Levinson, *Theory of Ordinary Differential Equations* (McGraw–Hill, 1955), for the classical existence theory, linear systems and Sturm–Liouville problems.
- Jack K. Hale, *Ordinary Differential Equations* (Krieger, 2nd ed. 1980), for the Banach-space formulation and the qualitative theory.
- Philip Hartman, *Ordinary Differential Equations* (Birkhäuser, 2nd ed. 1982), for the phase-plane analysis and the linearisation theorems.
- Morris W. Hirsch, Stephen Smale and Robert L. Devaney, *Differential Equations, Dynamical Systems, and an Introduction to Chaos* (Academic Press, 3rd ed. 2013), for the planar classification and stability.
- Einar Hille, *Lectures on Ordinary Differential Equations* (Addison-Wesley, 1969), for the exponential of operators and periodic systems.
- Witold Hurewicz, *Lectures on Ordinary Differential Equations* (MIT Press, 1958; reprinted Dover, 1990), for a concise treatment of the maximal interval and continuous dependence.
- Serge Lang, *Differential and Riemannian Manifolds* (Springer, 3rd ed. 1995), for the flow of a vector field and its relation to differential geometry.
- Vladimir I. Arnold, *Ordinary Differential Equations* (Springer, 3rd ed. 1992), for the geometric reading of the phase portrait.
