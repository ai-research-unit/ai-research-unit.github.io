
# __Impulsive Differential Equations__

## Introduction

An impulsive differential equation combines two kinds of evolution. Between certain instants the unknown changes continuously, according to an ordinary differential equation; at those instants it changes discontinuously, by a prescribed jump that may depend on the state reached. The instants themselves are either fixed in advance — the equation has a list of impulse times — or determined by the state, as when the trajectory meets a prescribed surface and is then reset. The combination is the natural language for systems in which a continuous process is interrupted by abrupt events, and its mathematics is the mathematics of a piecewise continuous solution produced by gluing ordinary solutions across jumps.

The new features are all caused by the jumps. A solution is no longer continuous, only piecewise continuous with one-sided limits at the impulse times, so the very notion of a solution has to be stated with care. Uniqueness of an initial-value problem must be checked on each interval separately, and it can fail through the interaction of the jumps with the differential equation, through the coincidence of two impulses or of an impulse with a zero of the solution, or through an accumulation of impulse times at a finite limit. The theory therefore consists of the ordinary theory applied interval by interval together with a vocabulary for the pathologies that the gluing creates.

The setting is a Banach space $X$ over $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, an interval $I \subseteq \mathbb{R}$, and a right-hand side $f : I \times X \to X$, exactly as in *Ordinary Differential Equations*, whose results are used throughout; the impulsive perturbations are the new ingredient. The article treats first the impulsive initial-value problem with fixed impulse times, its existence and uniqueness by the interval method, and the pathologies of accumulation and beating; then the linear theory, with the fundamental matrix as a product of ordinary fundamental matrices and exponentials of the jumps, and the variation-of-constants formula; then stability, where the jumps enter through a discrete Lyapunov condition; and finally the measure-driven formulation, in which the impulses are a measure and the equation is a differential equation driven by that measure, the Stieltjes integral being the one supplied by *Measure Theory and Integration*.

## The Impulsive Initial-Value Problem

### Definition and Solution Concept

**Definition.** Let $(\tau_k)_{k \in \mathbb{Z}}$ be a strictly increasing sequence of real numbers, the **impulse times** or **jump times**, and let $f : I \times X \to X$ and $I_k : X \to X$ be functions for each $k$, the **jump maps**. The **impulsive differential equation** determined by $f$ and $(I_k,\tau_k)$ is

$$
y'(t) = f(t,y(t)), \quad t \neq \tau_k; \qquad \Delta y\bigr|_{t=\tau_k} = I_k\bigl(y(\tau_k^-)\bigr),
$$

where $\Delta y|_{t=\tau_k} = y(\tau_k^+) - y(\tau_k^-)$ and $y(\tau_k^\pm)$ are the one-sided limits. A **solution** on an interval $J$ is a function $y$ that is continuous on $J$ except at the impulse times in $J$, differentiable with $y'(t) = f(t,y(t))$ at every $t \in J$ that is not an impulse time, satisfies the jump condition at each impulse time interior to $J$, and is left-continuous at the endpoints, $y(t)=y(t^-)$; if the impulse time is an endpoint of the domain, only the appropriate one-sided value is prescribed. The solution is **piecewise continuously differentiable**.

**Definition.** An impulsive equation **has an impulse at the initial time** if the initial datum is specified at a jump time; then the correct initial condition is the right-hand limit $y(\tau_0^+) = y_0$, and the left-hand value is immaterial. Otherwise the initial condition is $y(\tau_0) = y_0$ in the ordinary sense. The **pre-jump value** of a solution at $\tau_k$ is $y(\tau_k^-)$ and the **post-jump value** is $y(\tau_k^+)$.

The convention on one-sided values is the only point of care in the definition, and it matters for the composition of jumps: the jump map acts on the value *before* the jump, which is the limit from the left, so the value immediately after is $I_k(y(\tau_k^-)) + y(\tau_k^-)$.

**Example (a scalar impulsive logistic equation).** With $f(t,y) = y(1-y)$, impulse times $\tau_k = k$ and jumps $I_k(y) = -\tfrac12 y$, the solution grows logistically between integers and is halved at each integer; the piecewise continuous solution is computed by the interval method below, and its asymptotic size is smaller than the carrying capacity $1$ by a factor determined by the halving.

### Existence and Uniqueness by the Interval Method

**Theorem (interval method).** Suppose $f$ is continuous and locally Lipschitz in its second variable, each $I_k$ is continuous, and the impulse times are locally finite, that is, every compact subinterval of $I$ contains only finitely many $\tau_k$. Then for every initial datum there is a unique maximal solution.

*Proof.* On the interval $[\tau_0, \tau_1]$, before the first impulse, the equation is the ordinary problem $y' = f(t,y)$ with the given initial value, and the Picard–Lindelöf theorem of *Ordinary Differential Equations* gives a unique maximal solution there. If the solution reaches $\tau_1$ with a left limit $y(\tau_1^-)$, the jump condition defines $y(\tau_1^+) = y(\tau_1^-) + I_1(y(\tau_1^-))$, which is continuous in $y(\tau_1^-)$ because $I_1$ is; the ordinary argument then restarts at $(\tau_1, y(\tau_1^+))$ on $[\tau_1,\tau_2]$. Because the impulse times are locally finite, finitely many steps cover any compact subinterval, and the solution is obtained by gluing. Uniqueness is the uniqueness of each ordinary subproblem together with the determinism of the jump maps. $\square$

**Corollary (maximal interval and blow-up).** The maximal solution has an interval $(\alpha,\beta)$; if $\beta < \infty$ and $\beta$ is not an accumulation point of impulse times, then the solution is unbounded on $[\tau_0,\beta)$, and if $\beta$ is an accumulation point the solution may have a finite limit or no limit at all.

*Proof.* If the solution were bounded on $[\tau_0,\beta)$ and there were a final impulse time $\tau_N < \beta$ before $\beta$, the boundedness and the local Lipschitz condition would extend the solution beyond $\beta$, as in the ordinary maximal-interval theorem. When the impulse times accumulate at $\beta$ the limit need not exist, and the standard examples below show both possibilities. $\square$

### Accumulation of Impulses and Beating

**Definition.** The impulse times **accumulate** at $\tau^*$ if $\tau_k \to \tau^*$ from below with $\tau_k < \tau^*$; a solution exhibits the **Zeno phenomenon** if the number of impulses performed before a finite time $\tau^*$ is infinite. Two solutions **beat** at $\tau_k$ if the trajectory meets the same impulse surface of a state-dependent impulse problem more than once.

Accumulation of impulse times destroys the local finiteness on which the interval method rests, and the solution may fail to exist beyond $\tau^*$ in the ordinary sense. The two behaviours that occur are these.

**Example (a solution terminating).** Let $\tau_k = 1 - 2^{-k}$ and let the jump map at every $\tau_k$ be $I_k(y) = -1$ on the state $y$, with $f \equiv 0$. Starting from $y(0)=1$, the solution is $y(t) = 1$ for $t<\tau_1=\tfrac12$, then $0$, then $-1$, and after $k$ impulses $y = 1-k$; the trajectory is defined up to $t=1$ and takes the value $-k\to-\infty$ along the sequence, so it has no finite limit as $t \to 1^-$ and is unbounded on every neighbourhood of $1$. The maximal interval is $(-\infty,1)$ and the solution blows up at the accumulation point.

**Example (a solution with a finite limit).** With the same impulse times and jumps $I_k(y) = -2^{-k}$, the partial sums $\sum_{j\le k}2^{-j}$ converge to $1$, so $y(t) \to 1-1=0$ as $t\to1^-$; the solution has a finite limit and can be extended through the accumulation point by continuity, after which the equation is again ordinary. Thus accumulation does not always terminate the solution: it depends on the summability of the jumps.

**Remark.** The two examples show that the local finiteness of the impulse times is a genuine hypothesis of the existence theorem and not a technical convenience. In applications one imposes it, or one replaces the impulsive problem by the measure-driven formulation below, in which the accumulated impulses are carried by a measure and the solution is defined by a Stieltjes integral that can converge even when the individual impulses are infinitely many.

## Linear Impulsive Systems

### The Fundamental Matrix

**Definition.** A **linear impulsive system** is

$$
y'(t) = A(t)\,y(t), \quad t \neq \tau_k; \qquad y(\tau_k^+) = (I + B_k)\,y(\tau_k^-),
$$

with $A : I \to B(X)$ continuous and $B_k \in B(X)$. Its **fundamental matrix** at $t_0$ is the solution of the matrix problem with $W(t_0) = I$, written $W(t,t_0)$ when both arguments are needed; it is **causal**, $W(t,s)W(s,r) = W(t,r)$ for $r \le s \le t$, and invertible, $W(t,s)^{-1} = W(s,t)$.

**Theorem (product formula).** On the interval $(\tau_k,\tau_{k+1}]$ the fundamental matrix is obtained by multiplying the ordinary fundamental matrices and the jump factors:

$$
W(t,\tau_k^+) = \Phi_k(t)\,\bigl(I + B_k\bigr), \qquad
W(t,t_0) = \Phi_k(t)\,(I+B_k)\,\Phi_{k-1}(\tau_k)\cdots(I+B_1)\,\Phi_0(\tau_1)\,(I+B_0)\,\Phi_{t_0}(\tau_0),
$$

where $\Phi_j$ denotes the ordinary fundamental matrix of $y'=A(t)y$ on the relevant interval. When $A$ is constant and the jumps occur at equally spaced times $\tau_k = kT$, the one-period product is

$$
M = e^{A(T-\tau)}\,\bigl(I+B\bigr),
$$

the **monodromy matrix**, and the fundamental matrix satisfies $W(t+T) = W(t)M$ for $t$ in the first period.

*Proof.* The formula is the interval method applied to the matrix equation: between impulses the matrix solves the linear equation $W' = AW$, so it equals the ordinary fundamental matrix; across an impulse left multiplication by $I+B_k$ performs the jump. The causality and invertibility are immediate from the formula and from the invertibility of each factor. $\square$

**Theorem (Floquet).** If $A$ is $T$-periodic and the jump pattern is $T$-periodic with finitely many jumps per period, then $W(t,t_0) = P(t)e^{(t-t_0)C}$ where $P$ is $T$-periodic and invertible in $t$ and $C$ is constant, $e^{TC}=M$.

*Proof.* Since $W(t+T) = W(t)M$ by periodicity, and $M$ is invertible as a product of invertible factors, choose a logarithm $C$ with $e^{TC}=M$ and put $P(t) = W(t)e^{-tC}$; then $P(t+T) = W(t+T)e^{-(t+T)C} = W(t)Me^{-TC}e^{-tC} = W(t)e^{-tC} = P(t)$. $\square$

**Corollary (stability).** The linear impulsive periodic system is asymptotically stable if and only if every eigenvalue of the monodromy matrix $M$ has modulus strictly less than $1$; it is stable if and only if the eigenvalues have modulus at most $1$ and those of modulus $1$ are semisimple. The eigenvalues of $M$ are the **Floquet multipliers** and the eigenvalues of $C$ the **Floquet exponents**.

*Proof.* By Floquet's theorem $W(t) = P(t)e^{tC}$ with $P$ bounded and invertible, so the growth of $W(t)$ as $t\to\infty$ is governed by $e^{tC}$, hence by the eigenvalues of $C$; these are $\log\mu/T$ for the eigenvalues $\mu$ of $M$, so $|\mu|<1$ is equivalent to strictly negative real part for the exponents. $\square$

**Example (an oscillator with a periodic kick).** With $A = \begin{pmatrix}0&1\\-1&0\end{pmatrix}$, a period $T = 2\pi$ and one impulse per period with $B = \alpha I$ at $t = \pi$, the monodromy over one period is the product of two rotation-half matrices and the factor $1+\alpha$:

$$
M = (1+\alpha)e^{A\pi}e^{A\pi} = (1+\alpha)e^{2\pi A} = (1+\alpha)I,
$$

since $e^{2\pi A} = I$ for the rotation generator $A$. The multipliers are $1+\alpha$ twice, so the system is asymptotically stable exactly for $-2 < \alpha < 0$. The computation is exact and shows that a kick can stabilise an oscillator that is otherwise neutrally stable, and destabilise it when too strong.

### Variation of Constants

**Theorem (variation of constants).** The solution of the inhomogeneous linear impulsive system $y' = A(t)y + b(t)$, $y(\tau_k^+) = (I+B_k)y(\tau_k^-) + c_k$, with $y(t_0)=y_0$, is

$$
y(t) = W(t,t_0)y_0 + \int_{t_0}^{t}W(t,s)\,b(s)\,ds + \sum_{\tau_k \in (t_0,t]} W(t,\tau_k^+)\,c_k ,
$$

the sum being finite on every compact interval when the impulse times are locally finite.

*Proof.* By linearity it suffices to verify each term. The first is the homogeneous solution; the integral term is the ordinary variation-of-constants formula between impulses, its value jumping correctly because $W$ does; and each $c_k$ contributes the response of an impulse to the state at $\tau_k$, propagated forward by $W(t,\tau_k^+)$, which is the definition of $c_k$. Uniqueness of the solution of the impulsive initial-value problem completes the proof. $\square$

## Stability

### Lyapunov Functions with Jumps

**Definition.** For the impulsive system with impulse times $(\tau_k)$ the **jump operator** at time $t$ associated with the impulsive equation $y' = f(t,y)$ is the map sending the pre-jump value to the post-jump value; a **Lyapunov function** is a continuous positive definite $V : \mathbb{R}\times X \to \mathbb{R}$ that is continuously differentiable off the impulse times, whose derivative $\dot V(t,y) = \partial_tV + \partial_yV\cdot f(t,y)$ along the continuous flow is nonpositive, and whose jumps satisfy

$$
V\bigl(\tau_k^+, y(\tau_k^+)\bigr) \le V\bigl(\tau_k^-, y(\tau_k^-)\bigr)
$$

along solutions.

**Theorem (stability).** If such a Lyapunov function exists with $\dot V \le 0$ and nonincreasing jumps, the zero solution is stable; if in addition $\dot V \le -w(\|y\|)$ for a positive definite $w$ and the jumps satisfy $V(\tau_k^+,y^+) \le (1 - d_k)V(\tau_k^-,y^-)$ with $d_k \ge 0$ and $\sum_k d_k = \infty$, the zero solution is asymptotically stable.

*Proof.* Between impulses $V(\tau_k^+,y(t))$ is nonincreasing by $\dot V \le 0$, and the jump hypothesis makes it nonincreasing across the impulses as well; so $V$ is a nonincreasing function of time along the solution, and positive definiteness gives stability exactly as in the direct method of Lyapunov for ordinary equations. Under the stronger hypotheses the total decrement is infinite, so $V \to 0$ and, by positive definiteness, $y \to 0$. $\square$

**Corollary (linear systems).** For the linear impulsive system with constant $A$ and jumps $B_k$, the quadratic $V(y) = y^*y$ gives

$$
V(y(\tau_k^+)) = \|(I+B_k)y(\tau_k^-)\|^2 \le \|I+B_k\|^2\,V(y(\tau_k^-)),
$$

and the derivative along the flow is $\dot V = y^*(A^*+A)y$. Hence if $A^*+A \le -2\alpha I$ and $\|I+B_k\|^2 \le e^{-2\beta_k}$ with $\alpha$ and the $\beta_k$ giving an infinite total decrement, the zero solution is asymptotically stable.

*Proof.* Immediate from the theorem applied to the quadratic; the infinite decrement condition is $\sum_k(\beta_k) = \infty$ when the impulses are separated in a bounded way, more precisely when the inter-impulse times are bounded above, so that the continuous decrement $\alpha \cdot$ (time) is not lost. $\square$

**Example (a stable discrete map).** For the pure impulse problem with $A=0$, $B_k = B$ constant and impulses at every integer, the theorem gives the sufficient discrete-time condition $\|(I+B)\|<1$; the sharp condition for the stability of the iteration $x \mapsto (I+B)x$ is the spectral one $\rho(I+B)<1$, which is strictly weaker — the norm of a matrix can exceed its spectral radius, as it does for a nilpotent $I+B$ of large norm — and which is equivalent to $\|(I+B)^n\|<1$ for some $n$ by the spectral radius formula $\rho(M)=\lim_n\|M^n\|^{1/n}$. The two conditions agree when $I+B$ is normal, since then $\|I+B\|=\rho(I+B)$ in the operator norm induced by the Euclidean norm. The example shows that the impulsive theory contains the theory of the iterated linear map $x \mapsto (I+B)x$ as the special case $A=0$.

### Comparison and an Explicit Estimate

**Theorem (impulsive Gronwall inequality).** Let $u : [t_0,\beta) \to [0,\infty)$ be piecewise continuous, continuous at all non-impulse times, and suppose

$$
u(t) \le a + \int_{t_0}^{t}\beta(s)u(s)\,ds + \sum_{\tau_k \in (t_0,t]}\gamma_k\,u(\tau_k^-)
$$

with $a \ge 0$, $\beta \ge 0$ continuous, $\gamma_k \ge 0$. Then

$$
u(t) \le a\,\exp\Bigl(\int_{t_0}^t\beta(s)\,ds\Bigr)\prod_{\tau_k \in (t_0,t]}(1+\gamma_k) .
$$

*Proof.* Apply the ordinary Gronwall inequality of *Ordinary Differential Equations* on each interval between consecutive impulse times, accumulating the factor $1+\gamma_k$ at each impulse. $\square$

The inequality is the working tool for continuous dependence and for existence proofs with non-Lipschitz impulses; it shows that the jumps multiply the ordinary estimate by the product of the jump factors, so that stability is a question about the convergence of that product.

## Measure-Driven Impulsive Equations

### The Stieltjes Formulation

**Definition.** Let $\mu$ be a locally finite positive measure on $I$, the **impulse measure**, and let $F : I\times X \to X$ be continuous. The **measure-driven differential equation** is

$$
dy = F(t,y)\,d\mu ,
$$

understood as the integral equation

$$
y(t) = y(t_0) + \int_{[t_0,t]}F(s, y(s))\,d\mu(s),
$$

the integral being the Lebesgue–Stieltjes (or Kurzweil–Stieltjes) integral of *Measure Theory and Integration*. When $\mu = \lambda + \sum_k m_k\delta_{\tau_k}$ with $\lambda$ Lebesgue measure, $m_k$ masses and $\delta_{\tau_k}$ Dirac measures, and $F = f\cdot(d\lambda/d\mu) + \sum_k I_k(\cdot)\cdot(dm_k\delta/d\mu)$, the measure-driven equation is the impulsive equation of the preceding sections with $I_k$ scaled by $m_k$.

**Theorem (existence and uniqueness).** If $F$ is continuous, $\mu$ is locally finite, and $F$ satisfies a global Lipschitz condition in the second variable with $\mu$-integrable constant, then for every $t_0$ and $y_0$ there is a unique solution on the whole interval.

*Proof.* The integral operator is a contraction on the space of $\mu$-a.e. continuous functions with the sup norm when the Lipschitz constant times $\mu([t_0,t])$ is less than $1$, which holds on a sufficiently short interval and can be iterated; this is the Picard argument with the Stieltjes integral replacing the Lebesgue integral, and the completeness of the space is that of $C([t_0,t],X)$ under the supremum norm. $\square$

**Remark (why the measure language is the right one).** The measure formulation removes the need for local finiteness of the impulse times: an accumulated sequence of impulses is carried by a measure $\sum_k m_k\delta_{\tau_k}$ that is finite on compact sets whenever $\sum_{k:\tau_k\le t}m_k < \infty$, and the Stieltjes integral converges under this summability even though the intervals between impulses shrink to zero length. The Zeno phenomenon is then a statement about the mass of the measure on a small interval, not about the count of the impulse times, and the solution continues to exist when the total mass is finite. The general interaction of this formulation with the ordinary equation in the absolutely continuous part of $\mu$ is the theory of measure differential equations, and its study for finite-dimensional $X$ and a general $\mu$ is a standard chapter of the field.

## Summary

An impulsive differential equation is an ordinary differential equation punctuated by state-dependent or time-dependent jumps; a solution is piecewise continuously differentiable, with left and right limits at each impulse time and a jump prescribed in terms of the left limit. If the impulse times are locally finite, the right-hand side is continuous and locally Lipschitz, and the jump maps are continuous, then the interval method — solving the ordinary equation between impulses and applying the jump at each impulse time — gives a unique maximal solution, exactly as the ordinary theory would on each piece. Accumulation of impulse times destroys local finiteness; a solution then may blow up at the accumulation point, as a divergent sum of jumps does, or may have a finite limit and extend through it, as a convergent sum does, so the phenomenon is governed by the summability of the jumps.

For linear impulsive systems the fundamental matrix is a product of ordinary fundamental matrices and jump factors, and the variation-of-constants formula adds a finite sum of responses at the impulse times to the ordinary integral. When the coefficients and the impulse pattern are periodic, Floquet's theorem writes the fundamental matrix as a periodic factor times an exponential of the logarithm of the monodromy matrix, and asymptotic stability is exactly the condition that every Floquet multiplier have modulus less than one. Stability in the nonlinear case is decided by a Lyapunov function whose derivative is nonpositive along the flow and whose value does not increase across the jumps, the strong form giving asymptotic stability, and the impulsive Gronwall inequality multiplies the ordinary estimate by the product of the jump factors.

The measure-driven formulation $dy = F(t,y)\,d\mu$ replaces the discrete list of impulses by a locally finite measure and the Stieltjes integral by the Lebesgue or Kurzweil–Stieltjes integral of *Measure Theory and Integration*; it subsumes the impulsive equation, removes the hypothesis of local finiteness when the total mass is finite, and is the natural setting in which the Zeno phenomenon becomes a statement about the mass of the measure on a short interval.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $X$ | Banach state space over $\mathbb{K}$ |
| $f(t,y)$ | Continuous part of the impulsive equation |
| $(\tau_k)$ | Impulse times, strictly increasing |
| $I_k$, $B_k$ | Jump map and linear jump matrix at $\tau_k$ |
| $y(\tau_k^-)$, $y(\tau_k^+)$ | Pre-jump and post-jump values |
| $\Delta y|_{\tau_k}$ | Jump $y(\tau_k^+)-y(\tau_k^-)$ |
| $W(t,s)$ | Fundamental matrix of a linear impulsive system |
| $\Phi_j$ | Ordinary fundamental matrix $y'=A(t)y$ between impulses |
| $M$ | Monodromy matrix over one period |
| Floquet multipliers, exponents | Eigenvalues of $M$ and of its logarithm $C$ |
| $\rho(M)$ | Spectral radius of the jump matrix, $\rho(M)=\lim_n\|M^n\|^{1/n}$ |
| $V(t,y)$ | Lyapunov function; $\dot V$ its derivative along the flow |
| $d_k$ | Fractional decrement $V(\tau_k^+,y^+)\le(1-d_k)V(\tau_k^-,y^-)$ |
| $\mu$, $\delta_{\tau}$ | Impulse measure and Dirac measure at $\tau$ |
| $dy = F(t,y)\,d\mu$ | Measure-driven (Stieltjes) formulation |
| Zeno phenomenon | Infinitely many impulses before a finite time |

## Further Reading

- Marat Akhmet, *Principles of Discontinuous Dynamical Systems* (Springer, 2010), for the interval method, the beating phenomenon and B-equivalence.
- Marat Akhmet and Mehmet O. Fen, *Impulsive Differential Equations and Applications* (Hindawi, 2007), for the modern formulation and stability.
- Vangipuram Lakshmikantham, Drumi D. Bainov and Pavel S. Simeonov, *Theory of Impulsive Differential Equations* (World Scientific, 1989), for the classical existence, linear and stability theory.
- Drumi D. Bainov and Pavel S. Simeonov, *Impulsive Differential Equations: Periodic Solutions and Applications* (Longman, 1993), for periodic solutions and the monodromy matrix.
- Štefan Schwabik and Guoju Ye, *Topics in Banach Space Integration* (World Scientific, 2005), for the Kurzweil–Stieltjes integral used in the measure-driven formulation.
- Jaroslav Kurzweil, "Generalized Ordinary Differential Equations", *Czechoslovak Mathematical Journal* 8 (1958), for the integral of the measure-driven equation.
- Anatoly D. Myshkis and Anatoly M. Samoilenko, "Systems with Impulses at Fixed Times", *Differential Equations* 9 (1973), for the accumulation of impulses and the Zeno phenomenon.
- Peter E. Kloeden and Eckhard Platen, *Numerical Solution of Stochastic Differential Equations* (Springer, 1992), for the interval-gluing technique that the impulsive and stochastic theories share.
- Alexander Halanay and Demetrios Wexler, *Qualitative Theory of Impulsive Systems* (Editura Academiei, 1968), for the early systematic treatment.
