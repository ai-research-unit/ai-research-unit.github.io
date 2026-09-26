
# __Fractional Differential Equations__

## Introduction

The theory of differential equations becomes richer when the order of differentiation is allowed to be a real number. Fractional calculus defines an operator $D^\alpha$ for every $\alpha>0$ that coincides with the ordinary derivative of order $n$ when $\alpha=n$ and interpolates between the orders for non-integer $\alpha$, and the equations $D^\alpha y = f(t,y)$ — **fractional differential equations** — have a well-posed theory whose solutions exhibit behaviour with no counterpart in the integer-order theory. The interpolation is not merely formal: the operator $D^\alpha$ is nonlocal, its action on a function depending on the whole past of the function rather than on an arbitrarily small neighbourhood, and it is this nonlocality that changes the character of the equations.

The building blocks are three. First, the **fractional integral** $I^\alpha$ of order $\alpha>0$, a convolution of the function with the power kernel $t^{\alpha-1}/\Gamma(\alpha)$, which is defined whenever the function is locally integrable and which satisfies the semigroup law $I^\alpha I^\beta = I^{\alpha+\beta}$. Second, the **fractional derivatives**, of which two are in use: the Riemann–Liouville derivative $D^\alpha$, defined by differentiating the fractional integral, and the Caputo derivative ${}^C D^\alpha$, defined by fractionally integrating the ordinary derivative. The two differ by the contribution of the initial values and are suited to different problems; the Caputo derivative is the one for which the initial conditions of a fractional differential equation are the ordinary ones. Third, the **Mittag-Leffler function** $E_\alpha$, which is to the fractional equations what the exponential is to the ordinary ones: $y(t) = y_0E_\alpha(\lambda t^\alpha)$ solves $D^\alpha y = \lambda y$.

The article proceeds from the fractional integral and the two derivatives, through their composition laws and their Laplace transforms, to the Mittag-Leffler function and its asymptotic behaviour, and then to the three levels of the theory. For the fractional ordinary equation $D^\alpha y = f(t,y)$ the Cauchy problem is equivalent to a weakly singular Volterra integral equation, and the Picard iteration of *Ordinary Differential Equations* applies with the contraction factor $LT^\alpha/\Gamma(\alpha+1)$ on a short interval, giving existence and uniqueness; the linear equation is solved by the Mittag-Leffler function, whose algebraic large-time decay is the characteristic feature of the sub-exponential regime $0<\alpha<1$. For the fractional partial equation ${}^C D_t^\alpha u = \Delta u$ the solution is a fractional diffusion, given in Fourier variables by $E_\alpha(-|\xi|^2t^\alpha)$, whose mean square displacement grows as $t^\alpha$ rather than as $t$ and whose transition density is not Gaussian. For the operator theory, the fractional powers of an operator are defined by a Bochner integral against the resolution of the identity or against a semigroup, and this connects the subject to the semigroups and evolution equations of this Part, where the generation theory of the operators $e^{-tA}$ is developed. The whole theory is developed over $\mathbb{R}$ or $\mathbb{R}^n$; the target space is a Banach space $X$ over $\mathbb{K}$, and the integrals are those of *Measure Theory and Integration*.

## Fractional Integrals and Derivatives

### The Fractional Integral

**Definition.** Let $\alpha>0$ and let $f$ be locally integrable on $[a,\infty)$. The **Riemann–Liouville fractional integral** of order $\alpha$ is

$$
I_a^\alpha f(t) = \frac{1}{\Gamma(\alpha)}\int_a^t(t-s)^{\alpha-1}f(s)\,ds , \qquad t>a ,
$$

and for $\alpha=0$ one sets $I_a^0f=f$. When $a=0$ or when the base point is clear the subscript and the base are omitted.

**Theorem (semigroup law).** For $\alpha,\beta>0$ and $f$ locally integrable, $I_a^\alpha I_a^\beta f = I_a^{\alpha+\beta}f = I_a^\beta I_a^\alpha f$; the family $(I_a^\alpha)_{\alpha>0}$ is thus a commutative one-parameter family of operators.

*Proof.* Interchanging the order of integration in the iterated integral and evaluating the inner integral by the beta function gives

$$
\int_a^t(t-s)^{\alpha-1}\int_a^s(s-\tau)^{\beta-1}f(\tau)\,d\tau\,ds = B(\alpha,\beta)\int_a^t(t-\tau)^{\alpha+\beta-1}f(\tau)\,d\tau ,
$$

with $B(\alpha,\beta) = \Gamma(\alpha)\Gamma(\beta)/\Gamma(\alpha+\beta)$; dividing by $\Gamma(\alpha)\Gamma(\beta)$ gives the law, and the symmetry in $\alpha,\beta$ the commutativity. $\square$

**Example.** $I_a^\alpha(t-a)^\beta = \frac{\Gamma(\beta+1)}{\Gamma(\beta+\alpha+1)}(t-a)^{\beta+\alpha}$ for $\beta>-1$, which is the fundamental computation from which most others follow; in particular $I_a^\alpha 1 = (t-a)^\alpha/\Gamma(\alpha+1)$, which vanishes at $t=a$ precisely when $\alpha>0$.

### The Riemann–Liouville and Caputo Derivatives

**Definition.** Let $\alpha>0$ and let $n = \lceil\alpha\rceil$ be the least integer with $n\ge\alpha$, so that $n-1 < \alpha \le n$. The **Riemann–Liouville derivative** of order $\alpha$ is

$$
D_a^\alpha f(t) = \frac{d^n}{dt^n}I_a^{n-\alpha}f(t) = \frac{1}{\Gamma(n-\alpha)}\frac{d^n}{dt^n}\int_a^t(t-s)^{n-\alpha-1}f(s)\,ds ,
$$

and the **Caputo derivative** of order $\alpha$ is

$$
{}^C D_a^\alpha f(t) = I_a^{n-\alpha}\frac{d^n}{dt^n}f(t) = \frac{1}{\Gamma(n-\alpha)}\int_a^t(t-s)^{n-\alpha-1}f^{(n)}(s)\,ds .
$$

The two agree when the first $n$ derivatives of $f$ vanish at $a$; in general they differ by a polynomial in $(t-a)$.

**Theorem (consistency and difference).** If $\alpha = n$ is an integer, then $D_a^n f = {}^C D_a^n f = f^{(n)}$. For non-integer $\alpha$ with $n = \lceil\alpha\rceil$,

$$
D_a^\alpha f(t) = {}^C D_a^\alpha f(t) + \sum_{k=0}^{n-1}\frac{(t-a)^{k-\alpha}}{\Gamma(k-\alpha+1)}\,f^{(k)}(a) .
$$

In particular $D_a^\alpha$ of a constant is $\frac{(t-a)^{-\alpha}}{\Gamma(1-\alpha)}$ for $0<\alpha<1$, whereas the Caputo derivative of a constant is zero.

*Proof.* For integer $\alpha$ the operator $I^{0}$ is the identity and the definitions reduce to $f^{(n)}$. For the difference, write $f$ as its Taylor polynomial of order $n-1$ at $a$ plus a remainder whose first $n$ derivatives vanish at $a$; the Caputo derivative kills the polynomial and acts on the remainder, while the Riemann–Liouville derivative picks up the contribution of the polynomial, computed term by term from $D_a^\alpha(t-a)^k = \frac{\Gamma(k+1)}{\Gamma(k+1-\alpha)}(t-a)^{k-\alpha}$. $\square$

The difference is not a technicality. The Caputo derivative is the one for which the initial conditions of a fractional differential equation are the ordinary values $f^{(k)}(a)$, $k<n$, and for which the derivative of a constant vanishes; the Riemann–Liouville derivative is the one that composes cleanly with the fractional integral. The two operators are the two natural completions of the integer-order derivative to non-integer order, and the theory uses both.

**Theorem (composition laws).** For $\alpha>0$ and $n=\lceil\alpha\rceil$:

$$
D_a^\alpha I_a^\alpha f = f, \qquad I_a^\alpha D_a^\alpha f(t) = f(t) - \sum_{k=0}^{n-1}\frac{(t-a)^{k-\alpha}}{\Gamma(k-\alpha+1)}\,\Bigl[I_a^{n-\alpha}f\Bigr]^{(k)}(a^+),
$$

(the latter for $f$ with the required regularity), and for the Caputo derivative

$$
I_a^\alpha\,{}^C D_a^\alpha f(t) = f(t) - \sum_{k=0}^{n-1}\frac{(t-a)^k}{k!}f^{(k)}(a).
$$

*Proof.* The first identity is the fundamental theorem of calculus applied to $I^{n-\alpha}f$. For the second, apply the operator identity $I^\alpha D^n I^{n-\alpha}$ and peel off the boundary terms of the repeated integration; the Caputo identity follows from $I^\alpha I^{n-\alpha}f^{(n)} = I^nf^{(n)}$ and the $n$-fold integration formula. $\square$

**Definition.** The **Grünwald–Letnikov derivative** of order $\alpha$ is the limit of the finite-difference quotient

$$
D_{\mathrm{GL}}^\alpha f(t) = \lim_{h\to0^+}h^{-\alpha}\sum_{k=0}^{\lfloor t/h\rfloor}(-1)^k\binom{\alpha}{k}f(t-kh),
$$

with $\binom{\alpha}{k} = \frac{\Gamma(\alpha+1)}{\Gamma(k+1)\Gamma(\alpha-k+1)}$.

**Proposition.** For $f$ of class $C^n$ with $n=\lceil\alpha\rceil$ the Grünwald–Letnikov derivative agrees with the Riemann–Liouville derivative; for $\alpha = n$ the generating function $(1-z)^n$ has finitely many nonzero coefficients and the definition reduces to the $n$-th finite difference.

*Proof.* The coefficients of $(1-z)^\alpha$ are $(-1)^k\binom{\alpha}{k}$, so the sum is the $\alpha$-th finite difference of $f$; expanding $f(t-kh)$ in a Taylor polynomial and summing against the binomial coefficients, whose partial sums have the known asymptotics, gives the Riemann–Liouville derivative in the limit. For $\alpha=n$ the generating function is a polynomial of degree $n$, so only $k\le n$ contribute and the quotient is the $n$-th difference quotient. $\square$

The Grünwald–Letnikov form is the definition best suited to computation, and it is the definition that shows the nonlocality most plainly: the value of $D^\alpha f$ at $t$ depends on the values of $f$ at all earlier points $t-kh$ down to $0$, with weights decaying like $k^{-\alpha-1}$.

## The Mittag-Leffler Function

**Definition.** For $\alpha>0$ and $\beta \in \mathbb{C}$ the **Mittag-Leffler function** is the entire function

$$
E_{\alpha,\beta}(z) = \sum_{k=0}^{\infty}\frac{z^k}{\Gamma(\alpha k+\beta)} ,
$$

and $E_\alpha = E_{\alpha,1}$. Thus $E_1(z) = e^z$, $E_2(z) = \cosh\sqrt z$ for the even variable, and $E_{1,2}(z) = (e^z-1)/z$.

**Theorem (Laplace transform).** For $\alpha>0$, $\beta>0$, $\lambda \in \mathbb{C}$ and $t>0$,

$$
\int_0^\infty e^{-st}\,t^{\beta-1}E_{\alpha,\beta}(\lambda t^\alpha)\,dt = \frac{s^{-\beta}}{1-\lambda s^{-\alpha}}, \qquad \operatorname{Re}s > |\lambda|^{1/\alpha} .
$$

*Proof.* Integrating term by term and using $\int_0^\infty e^{-st}t^{\gamma-1}dt = \Gamma(\gamma)s^{-\gamma}$,

$$
\int_0^\infty e^{-st}t^{\beta-1}E_{\alpha,\beta}(\lambda t^\alpha)dt = \sum_{k\ge0}\frac{\lambda^k}{\Gamma(\alpha k+\beta)}\cdot\frac{\Gamma(\alpha k+\beta)}{s^{\alpha k+\beta}} = \sum_{k\ge0}\lambda^ks^{-\alpha k-\beta} ,
$$

which is the displayed geometric series, absolutely convergent for $|s|>|\lambda|^{1/\alpha}$. $\square$

**Theorem (asymptotics).** For $0<\alpha<1$ and $\lambda>0$,

$$
E_\alpha(-\lambda t^\alpha) = \frac{1}{\lambda\,\Gamma(1-\alpha)}\,t^{-\alpha} + O(t^{-2\alpha}) \qquad (t\to\infty),
$$

so the function decays algebraically and not exponentially; for $1<\alpha<2$ the decay is algebraic with an oscillation. Near $t=0$, $E_\alpha(-\lambda t^\alpha) = 1 - \frac{\lambda t^\alpha}{\Gamma(\alpha+1)} + O(t^{2\alpha})$.

*Proof.* Quoted as standard. The expansion follows from the integral representation $E_\alpha(-z) = \int_\gamma \frac{e^{\zeta}\zeta^{\alpha-1}}{\zeta^\alpha+z}d\zeta$ and the residue at the pole $\zeta$ with $\zeta^\alpha = -z$; the pole contributes $t^{-\alpha}$. $\square$

The algebraic decay is the quantitative content of anomalous relaxation: a fractional relaxation equation relaxes to equilibrium as a power of the time rather than exponentially, and the fractional order $\alpha$ is the exponent.

## Fractional Ordinary Differential Equations

### The Cauchy Problem

**Definition.** Let $\alpha>0$, let $X$ be a Banach space, and let $f : [0,T]\times X \to X$. The **fractional differential equation** of order $\alpha$ is

$$
{}^C D_0^\alpha y(t) = f\bigl(t, y(t)\bigr), \qquad y^{(k)}(0) = y_k, \quad k = 0,\dots,n-1,
$$

the derivative being the Caputo derivative, so that the initial data are the ordinary values of $y$ and its derivatives at $0$. With $n=1$ and $\alpha \in (0,1)$ there is one initial condition, $y(0)=y_0$, and the equation is the **fractional relaxation equation** when $f$ does not depend on $t$.

**Theorem (equivalence to a Volterra equation).** For $\alpha \in (0,1)$ and $y$ continuous, the Cauchy problem ${}^C D_0^\alpha y = f(t,y)$, $y(0)=y_0$, is equivalent to the integral equation

$$
y(t) = y_0 + \frac{1}{\Gamma(\alpha)}\int_0^t(t-s)^{\alpha-1}f\bigl(s,y(s)\bigr)\,ds = y_0 + I_0^\alpha f(\cdot,y)(t).
$$

For general $\alpha$ with $n=\lceil\alpha\rceil$, the equivalent equation is $y(t) = \sum_{k<n}\frac{t^k}{k!}y_k + I_0^\alpha f(\cdot,y)(t)$.

*Proof.* Apply $I_0^\alpha$ to both sides of the equation and use the composition identity $I_0^\alpha\,{}^C D_0^\alpha y = y - \sum_{k<n}\frac{t^k}{k!}y^{(k)}(0)$; conversely, applying ${}^C D_0^\alpha$ to the integral equation returns the equation, by the same identity read backwards. $\square$

**Theorem (existence and uniqueness).** Let $\alpha\in(0,1)$, let $f:[0,T]\times X\to X$ be continuous and Lipschitz in the second variable with constant $L$, and let $y_0 \in X$. Then on the interval $[0,T_*]$ with

$$
T_* = \min\Bigl(T,\ \bigl(\Gamma(\alpha+1)/L\bigr)^{1/\alpha}\Bigr)
$$

there is a unique continuous solution of the Cauchy problem; on a shorter interval it is the limit of the Picard iterates $y_{m+1} = y_0 + I_0^\alpha f(\cdot,y_m)$.

*Proof.* Let $T' \le T_*$ and consider the map $\Lambda y = y_0 + I_0^\alpha f(\cdot,y)$ on $C([0,T'],X)$ with the supremum norm. Then

$$
\|\Lambda y - \Lambda z\|_\infty \le L\,\|I_0^\alpha\| \cdot \|y-z\|_\infty, \qquad \|I_0^\alpha\|\le \frac{(T')^\alpha}{\Gamma(\alpha+1)},
$$

as follows from $I_0^\alpha 1 = t^\alpha/\Gamma(\alpha+1)$ and the positivity of the kernel; choosing $T'$ with $L(T')^\alpha/\Gamma(\alpha+1)<1$ makes $\Lambda$ a contraction, the contraction mapping principle gives a unique fixed point, and the fixed point is exactly the solution by the equivalence theorem. Iterating over successive intervals gives the maximal interval. $\square$

The proof is the Picard argument verbatim, with the single change that the kernel is weakly singular: the factor $T^\alpha/\Gamma(\alpha+1)$ replaces the factor $T$ of the ordinary theory, and the singularity is integrable, so no separate treatment is needed.

**Theorem (the linear equation).** The solution of ${}^C D_0^\alpha y = \lambda y$ with $y(0)=y_0$, $\alpha\in(0,1)$, is

$$
y(t) = y_0\,E_\alpha(\lambda t^\alpha),
$$

and more generally the solution with $y(0)=y_0$ of ${}^C D_0^\alpha y - \lambda y = t^{\beta-1}g(t)$ is given by the convolution of the Mittag-Leffler kernel with the forcing term.

*Proof.* The Laplace transform of the equation, using $\mathcal L\{{}^C D_0^\alpha y\}(s) = s^\alpha\hat y(s) - s^{\alpha-1}y_0$, gives $\hat y(s) = \frac{s^{\alpha-1}y_0}{s^\alpha-\lambda} = \frac{y_0s^{-1}}{1-\lambda s^{-\alpha}}$; the inverse transform by the previous theorem with $\beta=1$ is $y_0E_\alpha(\lambda t^\alpha)$. $\square$

**Example (stretched and algebraic relaxation).** For $0<\alpha<1$ and $\lambda>0$ the solution of ${}^C D_0^\alpha y = -\lambda y$ is $y = y_0E_\alpha(-\lambda t^\alpha)$, which begins at $1$, decays initially like $1 - \lambda t^\alpha/\Gamma(\alpha+1)$, and at large time decays like $y_0/(\lambda\Gamma(1-\alpha))\,t^{-\alpha}$; for $\alpha=1$ it is the exponential $e^{-\lambda t}$. The limiting cases are exact: as $\alpha\to1$ the Mittag-Leffler function tends to the exponential, and the algebraic tail disappears.

## Fractional Partial Differential Equations

**Definition.** Let $\alpha\in(0,1]$. The **time-fractional diffusion equation** is

$$
{}^C D_{0}^\alpha u(x,t) = \Delta u(x,t), \qquad u(x,0)=f(x),
$$

on $\mathbb{R}^n\times(0,\infty)$; for $\alpha=1$ it is the heat equation of the classical theory, and for $\alpha<1$ it is a **subdiffusion**.

**Theorem (solution by the Fourier transform).** For $f$ bounded and continuous, the solution is

$$
\hat u(\xi,t) = E_\alpha\bigl(-|\xi|^2t^\alpha\bigr)\hat f(\xi),
$$

so that $u(\cdot,t) = f * K_t^{(\alpha)}$ with the **fractional heat kernel**

$$
K_t^{(\alpha)}(x) = \frac{1}{(2\pi)^n}\int_{\mathbb{R}^n}e^{ix\cdot\xi}E_\alpha\bigl(-|\xi|^2t^\alpha\bigr)d\xi .
$$

*Proof.* Taking the Fourier transform in $x$ turns the equation into the fractional ordinary equation ${}^C D_0^\alpha\hat u = -|\xi|^2\hat u$ with $\hat u(\xi,0)=\hat f(\xi)$, whose solution is the Mittag-Leffler function by the preceding theorem. $\square$

**Theorem (subdiffusive scaling).** The kernel $K_t^{(\alpha)}$ is a probability density for each $t>0$, it is self-similar,

$$
K_t^{(\alpha)}(x) = t^{-\alpha n/2}K_1^{(\alpha)}\bigl(x\,t^{-\alpha/2}\bigr),
$$

and for $0<\alpha<1$ it has the heavy tail

$$
K_t^{(\alpha)}(x) \sim c\,t^{\alpha}\,|x|^{-n-2} \qquad (|x|\to\infty),
$$

with a constant $c$ depending on $\alpha$ and $n$. Consequently the second moment $\int|x|^2K_t^{(\alpha)}$ is infinite for $0<\alpha<1$, while the truncated second moment over the ball $|x|\le R$ with $R$ large compared with $t^{\alpha/2}$ grows as $C\,t^{\alpha}$. For $\alpha=1$ the kernel is the Gaussian heat kernel of the classical theory and the second moment is $2nt$.

*Proof.* The scaling is the substitution $\xi\mapsto t^{-\alpha/2}\xi$ in the Fourier integral. The tail follows from the behaviour of $E_\alpha(-|\xi|^2t^\alpha)$ near $\xi=0$, namely $1 - c_1|\xi|^2t^\alpha + o(|\xi|^2)$; a density whose Fourier transform has this expansion has the tail $|x|^{-n-2}$ with coefficient proportional to $t^\alpha$, and its second moment diverges because $\int R^2\cdot R^{-n-2}R^{n-1}dR = \int R^{-1}dR$ diverges at infinity. Truncating at $R$ recovers the growth $t^\alpha$. $\square$

**Remark (anomalous diffusion as mathematics).** The exponent of the mean square displacement, $\alpha$ instead of $1$, is the defining feature of subdiffusion, and it is a statement about the scaling of the kernel. The equation is mathematically distinct from the heat equation not only in its solutions but in its operator theory: the operator ${}^C D_t^\alpha$ does not generate a semigroup in the ordinary sense, and the solution operator is not a one-parameter group but a family obeying an integro-differential evolution equation. The general theory of such evolution families belongs with the semigroups and evolution equations of this Part, where the generation theorem for the classical case is proved; the fractional case is the boundary of that theory, and the Mittag-Leffler function replaces the exponential throughout.

## Fractional Powers of Operators

**Definition.** Let $A$ be a closed linear operator on a Banach space $X$ whose resolvent contains a sector $|\arg\lambda|<\phi$ and satisfies $\|(\lambda I - A)^{-1}\|\le M|\lambda|^{-1}$ there, and suppose $0$ lies in the resolvent set. For $0<\alpha<1$ the **negative fractional power** $A^{-\alpha}$ is

$$
A^{-\alpha} = \frac{\sin(\pi\alpha)}{\pi}\int_0^\infty \lambda^{-\alpha}(\lambda I + A)^{-1}\,d\lambda ,
$$

the integral converging in the operator norm, and the positive fractional power $A^\alpha$ is the inverse of $A^{-\alpha}$ on its domain.

**Theorem (properties).** The family $A^{-\alpha}$ is a strongly continuous semigroup-like family, $A^{-\alpha}A^{-\beta} = A^{-(\alpha+\beta)}$ for $\alpha,\beta>0$, and $A^{-\alpha}$ is injective with dense range; if $A$ generates a bounded strongly continuous semigroup $e^{-tA}$, then

$$
A^{-\alpha} = \frac{1}{\Gamma(\alpha)}\int_0^\infty t^{\alpha-1}e^{-tA}\,dt ,
$$

the Bochner integral converging in the operator norm.

*Proof.* The semigroup law for the first formula follows from the resolvent identity and the fact that the Laplace transform of the product of two power kernels is the power kernel of the sum, evaluated at the resolvent; the second formula follows from the first by the standard representation of the resolvent as the Laplace transform of the semigroup, $\int_0^\infty e^{-\lambda t}e^{-tA}dt = (\lambda I+A)^{-1}$, and the beta integral. $\square$

The two formulas coincide on their common domain and give the fractional power in terms of a semigroup that is assumed to exist; the generation theory that decides when it does — the Hille–Yosida and Lumer–Phillips theorems, and the analytic semigroup setting in which $A^\alpha$ is defined for complex $\alpha$ — is the content of the article of this Part on semigroups and evolution equations. What belongs to this article is the scalar theory of the fractional integral and derivative and the way it is used to write the fractional equations as Volterra equations; the operator-valued theory is the functional-analytic continuation of the same formulas.

**Remark (the fractional calculus of variations).** A variational problem with a fractional derivative in the Lagrangian, $\int_a^bL(t,y,{}^C D_a^\alpha y)\,dt$, has stationarity equations obtained by a fractional integration by parts, in which the adjoint of ${}^C D_a^\alpha$ on the appropriate space is a Riemann–Liouville derivative acting on the test function. The resulting Euler–Lagrange equation is a fractional boundary-value problem with boundary terms at both ends; the full development belongs to the calculus of variations and its fractional extension, and is noted here only to fix the seam.

## Summary

The fractional integral $I_a^\alpha f(t) = \frac{1}{\Gamma(\alpha)}\int_a^t(t-s)^{\alpha-1}f(s)ds$ is defined for every $\alpha>0$ and obeys the semigroup law $I^\alpha I^\beta = I^{\alpha+\beta}$. Differentiating it gives the Riemann–Liouville derivative $D_a^\alpha = D^nI^{n-\alpha}$, and fractionally integrating the ordinary derivative gives the Caputo derivative ${}^C D_a^\alpha = I^{n-\alpha}D^n$ with $n=\lceil\alpha\rceil$; the two agree on functions whose first $n$ derivatives vanish at $a$ and differ in general by a polynomial, and both reduce to $f^{(n)}$ when $\alpha=n$ is an integer. The Caputo derivative is the one whose initial conditions are ordinary values, and $D_a^\alpha$ annihilates constants while the Riemann–Liouville derivative does not. The Grünwald–Letnikov finite-difference formula gives an equivalent, manifestly nonlocal definition.

The Mittag-Leffler function $E_{\alpha,\beta}(z) = \sum_kz^k/\Gamma(\alpha k+\beta)$ is the special function of the subject; its Laplace transform is $s^{-\beta}/(1-\lambda s^{-\alpha})$, and for $0<\alpha<1$ it decays algebraically, $E_\alpha(-\lambda t^\alpha)\sim t^{-\alpha}/(\lambda\Gamma(1-\alpha))$, rather than exponentially. The Cauchy problem ${}^C D_0^\alpha y = f(t,y)$ with $n$ initial values is equivalent to a weakly singular Volterra integral equation, and Picard iteration gives existence and uniqueness on an interval whose length is governed by the factor $LT^\alpha/\Gamma(\alpha+1)$; the linear equation ${}^C D_0^\alpha y = \lambda y$ has the solution $y_0E_\alpha(\lambda t^\alpha)$. The time-fractional diffusion equation ${}^C D_t^\alpha u = \Delta u$ is solved in Fourier variables by $E_\alpha(-|\xi|^2t^\alpha)$, its kernel is self-similar with the scaling $t^{\alpha/2}$ and heavy tails, and its mean square displacement grows as $t^\alpha$, which is subdiffusion. Fractional powers of a closed sectorial operator are defined by a Bochner integral against the resolvent, or equivalently against a bounded semigroup, $A^{-\alpha} = \frac{1}{\Gamma(\alpha)}\int_0^\infty t^{\alpha-1}e^{-tA}dt$; the generation theory behind that formula belongs to the semigroups and evolution equations of this Part.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\alpha$, $\beta$ | Orders and parameters; $\alpha>0$, $\beta\in\mathbb{C}$ |
| $\Gamma$ | Gamma function |
| $I_a^\alpha$ | Riemann–Liouville fractional integral of order $\alpha$ from $a$ |
| $D_a^\alpha$ | Riemann–Liouville fractional derivative |
| ${}^C D_a^\alpha$ | Caputo fractional derivative |
| $D_{\mathrm{GL}}^\alpha$ | Grünwald–Letnikov derivative |
| $n = \lceil\alpha\rceil$ | Least integer $\ge\alpha$ |
| $E_{\alpha,\beta}$ | Mittag-Leffler function, $E_\alpha = E_{\alpha,1}$ |
| $\lambda$ | Coefficient of the linear fractional equation |
| $K_t^{(\alpha)}$ | Fractional heat kernel of order $\alpha$ |
| ${}^C D_t^\alpha u = \Delta u$ | Time-fractional diffusion equation |
| $A^{-\alpha}$, $A^\alpha$ | Fractional powers of a sectorial operator $A$ |
| $X$ | Banach target space |
| subdiffusion | Mean square displacement growing as $t^\alpha$, $\alpha<1$ |

## Further Reading

- Kai Diethelm, *The Analysis of Fractional Differential Equations* (Springer, 2010), for the Riemann–Liouville and Caputo theory and the Mittag-Leffler function.
- Anatoly A. Kilbas, Hari M. Srivastava and Juan J. Trujillo, *Theory and Applications of Fractional Differential Equations* (Elsevier, 2006), for the systematic theory and the composition laws.
- Igor Podlubny, *Fractional Differential Equations* (Academic Press, 1999), for the Grünwald–Letnikov definition and the Mittag-Leffler asymptotics.
- Rudolf Gorenflo, Anatoly A. Kilbas, Francesco Mainardi and Sergei V. Rogosin, *Mittag-Leffler Functions, Related Topics and Applications* (Springer, 2nd ed. 2020), for the special function and its asymptotics.
- Francesco Mainardi, *Fractional Calculus and Waves in Linear Viscoelasticity* (Imperial College Press, 2010), for the relaxation and diffusion models.
- Mark M. Meerschaert and Alla Sikorskii, *Stochastic Models for Fractional Calculus* (De Gruyter, 2012), for subdiffusion and the scaling of the transition kernels.
- Boris Baeumer and Mark M. Meerschaert, "Stochastic Solutions for Fractional Cauchy Problems", *Journal of Applied Probability* 38 (2001), for the probabilistic representation.
- Alessandra N. Kochubei, "Fractional Order Diffusion", *Differential Equations* 26 (1990), for the fundamental solution of the time-fractional diffusion equation.
- Ravi P. Agarwal, Dumitru Baleanu, Vangipuram Lakshmikantham and others, "Fractional Calculus of Variations", in *Advances in Fractional Calculus* (Springer, 2007), for the variational extension noted at the end.
