
# __Optimal Control and the Pontryagin Maximum Principle__

## Introduction

Optimal control is the problem of steering a dynamical system with a control of one's own choosing so as to minimise a cost. The **state** $x(t)$ obeys a differential equation $\dot x = f(x,u,t)$ whose right-hand side contains a **control** $u(t)$ drawn from a set $U$, and the cost is a **running cost**, integrated along the trajectory, together with a **terminal cost** paid at the final time,

$$
J(u) = \varphi\bigl(x(T)\bigr) + \int_{t_0}^{T}L\bigl(x(t),u(t),t\bigr)\,dt .
$$

The problem is the calculus of variations read with a differential equation as its constraint, and it has two faces. The **Pontryagin maximum principle** removes the constraint by the multiplier rule: the multiplier is a function of time, the **costate** $p(t)$, and the state, the control and the costate together satisfy a first-order system of twice the dimension of the state, whose solutions are the candidates for optimality. **Dynamic programming** instead studies the **value function**, the least cost attainable from a given state at a given time, and shows that it solves a first-order partial differential equation, the **Hamilton–Jacobi–Bellman equation**, which is the Hamilton–Jacobi equation of the calculus of variations with the control eliminated by a minimisation.

The two routes are complementary rather than rival. The maximum principle is a system of ordinary differential equations with split boundary conditions, and it is the route that produces explicit solutions and the classical necessary conditions — the bang-bang form of a time-optimal control, the feedback and the Riccati equation of a linear-quadratic problem. Dynamic programming is a partial differential equation, and it is the route that proves **sufficiency**: a differentiable solution of the Bellman equation from which the minimising control can be read off solves the problem. Where the value function is smooth the two are related by the identity $p = V_x$: the costate of the maximum principle is the gradient of the value function. Where it is not smooth, the maximum principle survives and the classical Bellman equation does not, which is one reason both are kept.

The article develops the following. The problem is fixed first, with its data, its admissible controls and its two elementary instances; then the maximum principle is stated and derived from the multiplier rule of the calculus of variations, and its Hamiltonian is shown to be the conservation law of the autonomous problem. The linear-quadratic problem is then solved in full, first in matrix form and then in a scalar instance whose closed form is elementary; the time-optimal problem of the double integrator is solved as the classical instance of a **bang-bang** control; and the article closes with dynamic programming, the Bellman equation, the verification theorem and the passage between the two routes.

The setting is that of the calculus of variations: the Lagrange multiplier rule for a constrained functional, the first variation and the Legendre transform are used here rather than re-derived, and the multiplier of the state equation is the costate. The convex formulation of the control condition, the subdifferential and the Fenchel conjugate are those of convex analysis, and they are the vocabulary of the sufficiency statements; the linear systems, the matrix exponential, the variation of constants and the two-point boundary-value problem are those of the ordinary differential equations of this Part; and the possible failure of the value function to be differentiable places its general theory in the nonsmooth analysis of this Part. The **control Hamiltonian** introduced below is not the Hamiltonian of classical mechanics: it is $\langle p,f\rangle+L$, whereas the Hamiltonian of the calculus of variations is $p\cdot\dot q-L$, and the two differ by the sign of the cost. The symplectic reading of the state–costate system belongs to the article of this Part on Lagrangian and Hamiltonian systems, written in parallel, and the name is used here in the control sense throughout.

## The Optimal Control Problem

### Data, Admissible Controls and Minimisers

**Definition.** A **control system** on an interval $[t_0,T]$ consists of a **state space** $X\subseteq\mathbb{R}^n$, a **control set** $U\subseteq\mathbb{R}^m$, a **dynamics** $f : X\times U\times[t_0,T]\to\mathbb{R}^n$, a **running cost** $L : X\times U\times[t_0,T]\to\mathbb{R}$ and a **terminal cost** $\varphi : X\to\mathbb{R}$. An **admissible control** is a bounded measurable $u : [t_0,T]\to U$; the corresponding **trajectory** is the solution $x$ of

$$
\dot x(t) = f\bigl(x(t),u(t),t\bigr), \qquad x(t_0)=x_0 ,
$$

which is assumed to exist and to be unique and to extend to the whole interval; and the **cost** of $u$ is $J(u)$ above. A pair $(x^*,u^*)$ is **optimal** if $J(u^*)\le J(u)$ for every admissible $u$.

The hypotheses that make the trajectory well posed are the standard ones: $f$ continuous in $(u,t)$ and Lipschitz in $x$ uniformly in $(u,t)$, and $U$ bounded. Under them the Picard–Lindelöf theorem gives existence and uniqueness for each $u$, and the boundedness of $U$ and the Lipschitz bound keep the trajectory on a common interval. The dependence of the trajectory on the control is continuous in the supremum norm, but not differentiable in a useful way, and this is the technical reason the proof of the maximum principle uses variations concentrated on a set of small measure — the **needle variations** — rather than the smooth variations of the calculus of variations.

**Definition.** The problem is **autonomous** if $f$ and $L$ do not depend explicitly on $t$; it has **fixed final time** if $T$ is prescribed and **free final time** if $T$ is part of the unknown. The final state is **free** when no condition is imposed on $x(T)$, and **fixed** when $x(T)=x_1$ is prescribed.

### Two Elementary Problems

**Example (the scalar integrator).** Let $n=m=1$, $f(x,u)=u$, $U=\mathbb{R}$, $L=\tfrac12(x^2+u^2)$, $\varphi=0$, $x(0)=x_0$, with $T$ fixed and $x(T)$ free. The task is to hold the state near the origin at least cost, and the solution below is $x(t)=x_0\cosh(T-t)/\cosh T$, $u(t)=-\tanh(T-t)x(t)$.

**Example (the double integrator).** Let $x=(x_1,x_2)$ with $\dot x_1=x_2$, $\dot x_2=u$, $U=[-1,1]$, $L=1$ and $\varphi=0$. The cost is the time itself, so the problem is to bring the state to the origin, at rest, in the least time with a bounded acceleration; its solution is the bang-bang law of the section below, and it is the standard instance in which the optimal control takes only the extreme values of $U$.

### The Relation to the Calculus of Variations

The calculus of variations also minimises $\int L$, but its admissible class is a space of curves and its constraint, when there is one, is algebraic or integral: a multiplier rule produces the Lagrange multipliers, and a holonomic constraint produces a multiplier function. In optimal control the constraint is the state equation itself, which is a differential constraint on the pair $(x,u)$ rather than a restriction of the curve $x$ alone; the control cannot be eliminated before varying, and the multiplier attached to the equation is a function of time. This is what distinguishes the problem from an ordinary variational one, and it is the shape the non-holonomic constraint of mechanics has: there, too, the constraint is not integrable, and the Lagrange–d'Alembert principle multiplies it by an unknown function instead of eliminating it, as the article of this Part on Lagrangian and Hamiltonian systems records. The multiplier rule used here is the one established for constrained functionals in the calculus of variations, with the multiplier paired against $f-\dot x$ so that the costate equation comes out with the classical sign.

Two familiar statements reappear as special cases. If $f(x,u)=u$ with $U$ open and $L$ independent of $x$, the minimisation of the Hamiltonian gives $p=-L_u$, and the costate equation $\dot p=-L_x$ then reads $\frac{d}{dt}L_u=L_x$, which is the Euler–Lagrange equation of the calculus of variations; and if $L$ is strictly convex in $u$ and $f$ is affine in $u$, the elimination of the control by minimising the control Hamiltonian is the Legendre transform, with the momentum of the calculus of variations equal to the negative of the costate.

## The Pontryagin Maximum Principle

### The Control Hamiltonian and the Costate

**Definition.** The **control Hamiltonian** of the problem is

$$
H(x,u,p,t) = \langle p,f(x,u,t)\rangle + L(x,u,t),
$$

in which $p\in\mathbb{R}^n$ is a new variable, the **costate**. The Hamiltonian is defined for all $p$ and has the state and the control as its first two arguments; the costate is the multiplier of the state equation, and the choice of sign fixing $H$ is recorded because every equation below depends on it.

The definition is the one that gives the maximum principle its classical shape. The theorem is named for the formulation in which the integral is to be **maximised**: for the problem of maximising $\int L$ the control **maximises** $H=\langle p,f\rangle+L$ at each time, and for the minimisation problem solved here it **minimises** the same $H$. The name is the name of the theorem and not an instruction about the control, and the minimisation form is used throughout this article.

### Statement of the Principle

**Theorem (Pontryagin maximum principle, normal form).** Suppose that $U$ is compact, that $f$ is continuous in $(u,t)$ and of class $C^1$ in $x$ with a bound on $f_x$, and that $L$ and $\varphi$ are of class $C^1$ in $x$. Let $(x^*,u^*)$ be optimal for the problem with $x(t_0)=x_0$ fixed, $T$ fixed and $x(T)$ free. Then there is an absolutely continuous $p : [t_0,T]\to\mathbb{R}^n$ such that, for almost every $t$,

$$
\dot x^* = \frac{\partial H}{\partial p}, \qquad \dot p = -\frac{\partial H}{\partial x},
$$

the second equation being read along $(x^*,u^*,p)$, and such that $u^*(t)$ minimises the function $u\mapsto H(x^*(t),u,p(t),t)$ over $U$ at almost every $t$. At the terminal time,

$$
p(T) = \frac{\partial\varphi}{\partial x}\bigl(x^*(T)\bigr),
$$

and if the final time is free as well then in addition

$$
H\bigl(x^*(T),u^*(T),p(T),T\bigr) = 0 .
$$

Three of the four conditions are the rewriting of the three stations of the multiplier rule: the variation in $p$ returns the state equation, the variation in $x$ returns the costate equation, and the boundary term returns the terminal condition. The fourth, the pointwise minimisation, is the one that requires the needle variation, because a control need not vary in a direction inside a Banach space; where $u^*(t)$ lies in the interior of $U$ and $H$ is differentiable in $u$, the condition reduces to $H_u=0$, the classical form.

**Corollary (the control is the minimiser of the Hamiltonian).** If $U=\mathbb{R}^m$, $f$ is affine in $u$ and $L$ is strictly convex in $u$ with a positive-definite Hessian $L_{uu}$, then the minimisation is attained at the unique $u$ solving $H_u=0$, and the implicit function theorem makes it a function $\kappa$ of $(x,p,t)$,

$$
u = \kappa(x,p,t), \qquad \langle p,f_u(x,u,t)\rangle + L_u(x,u,t) = 0 .
$$

The state and costate equations with the control so eliminated form a closed first-order system in $2n$ variables, the **Hamiltonian system of the maximum principle**. When $f$ is affine in $u$ and $L$ is quadratic in $u$, this elimination is exactly the Legendre transform of the calculus of variations, and the system is that of the calculus of variations with a control-dependence in the data.

### Derivation by the Lagrange Multiplier Rule

The derivation itself makes the role of the costate plain.

*Proof (sketch).* Adjoin the state equation to the cost with a multiplier $p$, pairing the multiplier against $f-\dot x$ so that the sign below comes out right:

$$
\widehat J(u) = \varphi\bigl(x(T)\bigr) + \int_{t_0}^{T}\Bigl[L(x,u,t) + \langle p, f(x,u,t)-\dot x\rangle\Bigr]dt .
$$

The functional $\widehat J$ is stationary in $p$ exactly when the state equation holds. Stationarity in $x$ is the Euler–Lagrange equation of the integrand $G = L+\langle p,f\rangle-\langle p,\dot x\rangle$ in the state variable: $G_{\dot x}=-p$, $G_x = L_x+f_x^{\mathsf T}p$, and $\frac{d}{dt}G_{\dot x}=G_x$ gives

$$
\dot p = -L_x - f_x^{\mathsf T}p = -\frac{\partial H}{\partial x},
$$

the costate equation. The integration by parts that produces it leaves the boundary term $-\langle p(T),\delta x(T)\rangle$, which together with $d\varphi(x(T))$ gives $p(T)=\varphi_x(x^*(T))$ when the final state is free. Stationarity in $u$ gives $\langle L_u+f_u^{\mathsf T}p,\delta u\rangle = 0$ on directions in which the control may vary, which is $\langle H_u,\delta u\rangle = 0$ and hence the pointwise minimisation where the control is free to move in all directions. The free-time condition is the remaining boundary term: differentiating the value in $T$ gives $\varphi_x\cdot\dot x^* + L = \langle p,\dot x^*\rangle + L = H = 0$ at $T$. ∎

The proof is a sketch in one respect, and the respect matters: the variation in $u$ is legitimate only when $\delta u$ ranges over a space containing the admissible directions at $u^*$, that is, in the interior of $U$. The full theorem replaces it by a needle variation, a perturbation of the control on a set of small measure, and the passage to the limit produces the pointwise minimisation without any differentiability in $u$. Nothing else in the statement changes, and the interior case is the one used in every computation below.

### Properties of the Hamiltonian

**Proposition (the Hamiltonian is conserved for an autonomous problem).** If $f$ and $L$ do not depend explicitly on $t$, then $H$ is constant along every trajectory satisfying the maximum principle.

*Proof.* Along such a trajectory,

$$
\frac{d}{dt}H = H_x\cdot\dot x + H_p\cdot\dot p + H_u\cdot\dot u = H_x\cdot H_p + H_p\cdot(-H_x) + \langle H_u,\dot u\rangle = \langle H_u,\dot u\rangle ,
$$

and $H_u$ vanishes in the interior case; in the general case $H(x^*,u,p,t)$ is minimised in $u$ at $u^*$ and the minimiser has derivative zero in the direction of the curve. Hence $H$ is constant. ∎

For a free final time the constant is zero, by the transversality condition: an autonomous time-optimal problem has $H\equiv0$ along the optimal trajectory. This is the conservation law of the optimal control problem, the analogue of the conservation of energy of a mechanical system, and it is the first check to apply to a candidate solution.

**Remark (the costate as a sensitivity, and the convex case).** The costate has a second reading, independent of the multiplier rule: for a perturbation of the initial state $x_0$ the least cost $V(x_0)$ satisfies $dV = \langle p(t_0),dx_0\rangle$ to first order, so that $p$ measures the marginal cost of the state — the **shadow price** of the state in the language of the convex analysis of this Part. When the problem is **convex** — $L$ convex in $(x,u)$, $f$ affine, $\varphi$ convex, $U$ convex — the maximum principle is also sufficient: a pair satisfying the four conditions is optimal. The convexity hypothesis is the one that rules out the saddle points a non-convex problem may have, and the sufficiency is proved by the convexity inequality along a comparison trajectory, exactly as the Karush–Kuhn–Tucker conditions of the convex analysis are shown to be sufficient.

## The Linear-Quadratic Regulator

The linear-quadratic problem is the one case with a complete, explicit and finite-dimensional answer, and the answer is the matrix Riccati equation. It is also the case in which the elimination of the control is exactly the Legendre transform of a convex quadratic, so that the maximum principle and the classical Legendre transform coincide.

### The Matrix Riccati Equation

**Theorem (the linear-quadratic regulator).** Let

$$
\dot x = Ax + Bu, \qquad J(u) = \tfrac12x(T)^{\mathsf T}Ex(T) + \tfrac12\int_{t_0}^{T}\bigl(x^{\mathsf T}Cx + u^{\mathsf T}Du\bigr)dt ,
$$

with $C$ symmetric positive semidefinite, $D$ symmetric positive definite, $E$ symmetric, and $x(t_0)=x_0$ fixed, $T$ fixed and $x(T)$ free. Then the optimal control is the linear feedback

$$
u^*(t) = -D^{-1}B^{\mathsf T}p(t) = -D^{-1}B^{\mathsf T}S(t)\,x^*(t),
$$

where $S$ is the symmetric solution on $[t_0,T]$ of the **matrix Riccati equation**

$$
\dot S = -C - A^{\mathsf T}S - SA + SBD^{-1}B^{\mathsf T}S , \qquad S(T) = E ,
$$

which the hypotheses of the theorem ensure to exist on the whole interval, while the scalar instance below shows how a solution can fail to. The costate system is $\dot x = Ax - BD^{-1}B^{\mathsf T}Sx$, $\dot p = -Cx - A^{\mathsf T}p$.

*Proof.* The control Hamiltonian is $H = \tfrac12x^{\mathsf T}Cx+\tfrac12u^{\mathsf T}Du+\langle p,Ax+Bu\rangle$, and $H_u = Du + B^{\mathsf T}p$ vanishes at $u=-D^{-1}B^{\mathsf T}p$; the Hessian $H_{uu}=D$ is positive definite, so the stationary point is the minimiser and the corollary above applies. The state equation becomes $\dot x = Ax - BD^{-1}B^{\mathsf T}p$ and the costate equation is $\dot p = -H_x = -Cx - A^{\mathsf T}p$. Put $p=Sx$ with $S$ symmetric; differentiating gives

$$
\dot p = \dot Sx + S\dot x = \dot Sx + SAx - SBD^{-1}B^{\mathsf T}Sx ,
$$

and equating this with $-Cx-A^{\mathsf T}Sx$, whose terms all carry $x$, gives the Riccati equation. The terminal condition is $S(T)=E$, from $p(T)=Ex(T)$. ∎

The Riccati equation in this sense is the matrix generalisation of the classical scalar Riccati equation treated in the integrable systems of this Part: the scalar instance below, $\dot S=S^2-1$, is exactly that equation with constant coefficients, and its constant solutions $S=\pm1$ are the two equilibria of the classical equation. What differs is where the equation comes from and what it describes. There the equation is the logarithmic derivative $y=\phi'/\phi$ of a second-order linear equation and is integrated by that substitution; here it is the flow of the optimal feedback, and the matrix equation is equivalent to the linear system of the maximum principle, so the linearisation is present in both but is exploited differently. The constant solution $S=1$ of the infinite-horizon problem with $C=D=B=1$, $A=0$ is the stabilising feedback, the equilibrium towards which the finite-horizon solution flows as the interval lengthens.

### The Scalar Regulator

Take $n=m=1$, $A=0$, $B=C=D=1$, $E=0$ and $t_0=0$, so that $\dot x=u$ and $J=\tfrac12\int_0^T(x^2+u^2)dt$, the first example of the article. The Riccati equation and its terminal condition are

$$
\dot S = S^2-1, \qquad S(T)=0 ,
$$

whose solution is $S(t)=\tanh(T-t)$: indeed $S(T)=0$, and $\dot S = -\operatorname{sech}^2(T-t) = \tanh^2(T-t)-1 = S^2-1$. The optimal control is therefore

$$
u^*(t) = -\tanh(T-t)\,x^*(t) ,
$$

a feedback that vanishes at the final time, since no time then remains in which to act, and approaches $u=-x$ as $T-t$ grows, the infinite-horizon feedback. The closed loop $\dot x = -\tanh(T-t)x$ integrates to

$$
x^*(t) = x_0\,\frac{\cosh(T-t)}{\cosh T} ,
$$

which decreases from $x_0$ to $x_0/\cosh T$; for $T=2.3$ and $x_0=1.7$ the value at $t=1.1$ is $0.611$, and a numerical integration of the closed loop reproduces it. The costate is $p(t)=S(t)x^*(t)=\tanh(T-t)\,x^*(t)$ and it satisfies $\dot p=-x^*$, so the pair is the solution of $\dot x=-p$, $\dot p=-x$ with $x(0)=x_0$, $p(T)=0$, as the maximum principle requires. The Hamiltonian $H=\tfrac12(x^2+u^2)+pu=\tfrac12(x^2-p^2)$ is constant along the solution, in agreement with the autonomous conservation law.

Two features of the scalar instance carry over. The Riccati solution is governed by the terminal weight. With $S(T)=E$ and $\lvert E\rvert<1$ it is $S(t)=\tanh\bigl(T-t+\operatorname{artanh}E\bigr)$, bounded on the whole interval; with $\lvert E\rvert>1$ it is $S(t)=\coth\bigl(T-t+\operatorname{arcoth}E\bigr)$, which has a pole at $t_*=T+\operatorname{arcoth}E$. For $E>1$ the pole lies beyond $T$, so the solution is finite on $[t_0,T]$; for $E<-1$ it lies at $t_*<T$, and the solution escapes to $\pm\infty$ before the interval ends whenever $t_0<t_*$: for $T=1$ and $E=-3$ the escape is at $t_*=0.653$. A negative terminal weight of sufficient size therefore leaves the finite-horizon problem without a feedback solution on a long enough interval, while a terminal weight that is positive semidefinite always gives one; this is the **finite escape** of the Riccati equation, and it is the reason the infinite-horizon problem is treated as the limit of finite-horizon problems rather than directly. Second, the value function is

$$
V(x,t) = \tfrac12S(t)x^2 = \tfrac12\tanh(T-t)\,x^2 ,
$$

which depends on the state only through the quadratic form and on the time only through $S$; the general linear-quadratic value function is $\tfrac12x^{\mathsf T}S(t)x$ for the same reason.

## Time-Optimal Control and the Bang-Bang Principle

When the running cost is $L=1$ the cost is the time itself, and the control Hamiltonian is linear in the control, so its minimisation over a compact interval is attained at an endpoint. The resulting control is called **bang-bang**: it takes only the extreme values of $U$, and it switches between them finitely often, the count being governed by the costate equations.

### The Double Integrator

Take the double integrator of the first section: $x=(x_1,x_2)$, $\dot x_1=x_2$, $\dot x_2=u$, $U=[-1,1]$, $L=1$, $\varphi=0$, $x(T)=0$ with $T$ free and minimal, the target being the origin at rest. The control Hamiltonian is

$$
H = p_1x_2 + p_2u + 1 ,
$$

and the costate equations are $\dot p_1 = -H_{x_1} = 0$ and $\dot p_2 = -H_{x_2} = -p_1$, so $p_1$ is constant and $p_2$ is affine in $t$. Since $H$ is linear in $u$, its minimisation over $[-1,1]$ gives

$$
u^*(t) = -\operatorname{sgn}\bigl(p_2(t)\bigr)
$$

wherever $p_2\neq0$, and the affine function $p_2$ vanishes at most once; hence an optimal control has **at most one switch**. This is the **bang-bang principle** in its simplest instance. The free-time condition is $H(T)=0$, which at $x_2(T)=0$ reads $p_2(T)u^*(T)+1=0$, so that $|p_2(T)|=1$.

The switching set is computable because the trajectories are explicit. For $u=+1$ the quantity $x_1-\tfrac12x_2^2$ is constant, since its derivative is $\dot x_1-x_2\dot x_2=x_2(1-u)$ and $u=1$; for $u=-1$ it is $x_1+\tfrac12x_2^2$ that is constant, the same computation with $u=-1$. The trajectories that terminate at the origin at rest therefore lie on the two parabolas $x_1=\tfrac12x_2^2$ with $x_2<0$, approached with $u=+1$, and $x_1=-\tfrac12x_2^2$ with $x_2>0$, approached with $u=-1$, and the two together are the level set of

$$
\sigma(x) = x_1 + \tfrac12x_2\lvert x_2\rvert .
$$

The optimal control is $u^*=-\operatorname{sgn}\sigma$ before the switching curve is met and the complementary extreme value after. Three instances, obtained by integrating the closed loop, are worth recording, because each is exact and each is a check on the sign convention: from $(1,0)$ the optimal time is $2$, with one switch at $\bigl(\tfrac12,-1\bigr)$; from $(2,0)$ it is $2\sqrt2$, again with one switch, at $\bigl(1,-\sqrt2\bigr)$; and from $(0,1)$ it is $1+\sqrt2$, the switch being at $\bigl(\tfrac14,-1/\sqrt2\bigr)$, after which the braking arc with $u=+1$ carries the state to the origin. At each of the three switch points $\sigma=0$: for the first, $\tfrac12+\tfrac12(-1)(1)=0$; for the second, $1+\tfrac12(-\sqrt2)(\sqrt2)=0$; for the third, $\tfrac14+\tfrac12(-1/\sqrt2)(1/\sqrt2)=\tfrac14-\tfrac14=0$.

**Remark (the singular case).** The control is undetermined by the minimisation where $p_2\equiv0$ on an interval; such an **singular arc** is not decided by the maximum principle alone, and it requires the differentiated conditions $H_u=0$, $\frac{d}{dt}H_u=0,\dots$ to be analysed separately. The double integrator has no singular arc, because $p_2$ affine can vanish on an interval only if $p_1=p_2=0$, which the free-time condition forbids; a problem with an integrator of higher order can have one, and the maximum principle then only brackets the arc without determining the control on it.

## Dynamic Programming and the Hamilton–Jacobi–Bellman Equation

### The Value Function and Bellman's Principle

**Definition.** For $(\xi,\tau)\in X\times[t_0,T]$ let $\mathcal{U}(\xi,\tau)$ be the admissible controls on $[\tau,T]$ whose trajectory from $\xi$ at time $\tau$ exists; the **value function** is

$$
V(\xi,\tau) = \inf_{u\in\mathcal{U}(\xi,\tau)}\Bigl[\varphi\bigl(x(T)\bigr) + \int_{\tau}^{T}L\bigl(x,u,t\bigr)dt\Bigr] ,
$$

with $x(\tau)=\xi$; the infimum is over the controls, and $V(\xi,T)=\varphi(\xi)$.

**Theorem (Bellman's principle of optimality).** For $t_0\le\tau\le\tau'\le T$,

$$
V(\xi,\tau) = \inf_{u}\Bigl[\int_{\tau}^{\tau'}L\bigl(x,u,t\bigr)dt + V\bigl(x(\tau'),\tau'\bigr)\Bigr] ,
$$

the infimum being over the controls on $[\tau,\tau']$ and $x$ the trajectory they generate.

*Proof.* The right-hand side is the infimum of the cost of the controls split into their restriction to $[\tau,\tau']$ and their restriction to $[\tau',T]$, and the second part of the cost is at least $V(x(\tau'),\tau')$, with equality attained in the limit by controls that are near-optimal after $\tau'$; the infimum over the first part then reproduces the left-hand side. ∎

### The Equation and the Verification Theorem

**Theorem (Hamilton–Jacobi–Bellman).** Suppose $V$ is of class $C^1$ on $X\times(t_0,T)$. Then $V$ satisfies

$$
\frac{\partial V}{\partial t} + \min_{u\in U}\Bigl[L(\xi,u,t) + \Bigl\langle \frac{\partial V}{\partial\xi}, f(\xi,u,t)\Bigr\rangle\Bigr] = 0 , \qquad V(\xi,T)=\varphi(\xi).
$$

*Proof.* Take $\tau'=\tau+\varepsilon$ in Bellman's principle, let the control be constant on the short interval, and expand to first order in $\varepsilon$; dividing by $\varepsilon$ and using that an optimal control achieves the minimum gives the equation. ∎

The minimisation in the statement is over the control at the single point $(\xi,t)$, exactly as in the maximum principle, and the two are related by the identity

$$
p(t) = \frac{\partial V}{\partial\xi}\bigl(x^*(t),t\bigr)
$$

along an optimal trajectory: substituting $p=V_\xi$ into the minimised Hamiltonian identifies the Bellman minimiser with the maximum-principle minimiser. In the scalar regulator above the identity reads $p=\tanh(T-t)x=Sx$, the costate obtained from the Riccati equation, and $V=\tfrac12Sx^2$ satisfies $V_t+\tfrac12x^2-\tfrac12V_x^2=0$, which is the Bellman equation with the control eliminated: $\min_u[\tfrac12(x^2+u^2)+V_xu] = \tfrac12x^2-\tfrac12V_x^2$ at $u=-V_x$.

**Theorem (verification).** Suppose $W\in C^1$ satisfies the Hamilton–Jacobi–Bellman equation with $W(\xi,T)=\varphi(\xi)$, and suppose that for each $(\xi,t)$ the minimum in the equation is attained at $u=\kappa(\xi,t)$ with $\kappa$ measurable. Then $W=V$ on $X\times[t_0,T]$, the closed-loop equation $\dot x=f(x,\kappa(x,t),t)$ has trajectories that are admissible, and the corresponding control is optimal.

*Proof.* For any admissible control and its trajectory, the Bellman equation gives $\frac{d}{dt}W(x(t),t) = W_t+W_x\cdot f \le -L(x,u,t)$ with equality exactly at $u=\kappa(x,t)$; integrating from $t$ to $T$ and using $W(\cdot,T)=\varphi$ gives $W(x(t),t)\le J$ for every $u$, with equality for the closed-loop control. ∎

The verification theorem is why dynamic programming proves **sufficiency**, whereas the maximum principle gives candidates. Its restriction is regularity: the value function of a control problem need not be differentiable, and the classical equation is then replaced by the equation read in the sense of **viscosity solutions**, the device that makes the comparison argument of the verification theorem work for a merely continuous value function. This is the point of contact with the nonsmooth analysis of this Part, and the classical statement above is the differentiable case.

### The Passage between the Two Routes

The two routes are related by the **characteristic system** of the Bellman equation. The equation $V_t + H(\xi,\kappa(\xi,V_\xi,t),V_\xi,t)=0$ is a first-order partial differential equation whose characteristic equations, along the curves of steepest descent, are the state and costate equations of the maximum principle, with $p=V_\xi$; the initial condition $V(\xi,T)=\varphi(\xi)$ produces the terminal condition $p(T)=\varphi_x(x(T))$ on the characteristics that arrive at $T$. The maximum principle is thus the characteristic method for the Bellman equation, and it is available precisely when the value function is not: its equations are ordinary, along a single trajectory, and they do not require the value function to exist as a differentiable function of the state. The Bellman equation, conversely, decides the global question the maximum principle leaves open, for a convex problem its solution certifying the optimum where the costate system supplies only candidates.

## Summary

An optimal control problem fixes a control system: a state $x$ obeying $\dot x=f(x,u,t)$, a control $u$ in a set $U$, a running cost $L$ and a terminal cost $\varphi$, the cost being $J(u)=\varphi(x(T))+\int_{t_0}^{T}L\,dt$. It is the calculus of variations with the state equation as its constraint, and the multiplier of that constraint is the **costate** $p$. The **Pontryagin maximum principle** states that an optimal pair together with a costate satisfies the state equation $\dot x=H_p$ and the costate equation $\dot p=-H_x$ of the control Hamiltonian $H=\langle p,f\rangle+L$, that $u(t)$ minimises $u\mapsto H(x(t),u,p(t),t)$ over $U$ at almost every time, and that the split boundary conditions are $x(t_0)=x_0$ together with $p(T)=\varphi_x(x(T))$ when the final state is free, with $H(T)=0$ added when the final time is free. The principle is the multiplier rule of the calculus of variations, the control condition requiring the needle variation rather than a smooth one; its Hamiltonian is constant along optimal trajectories of an autonomous problem, and zero when the final time is free.

The **linear-quadratic regulator** is the case of a linear system and a quadratic cost, and it is solved by a linear feedback $u=-D^{-1}B^{\mathsf T}Sx$ whose matrix $S$ solves the matrix Riccati equation $\dot S=-C-A^{\mathsf T}S-SA+SBD^{-1}B^{\mathsf T}S$ with $S(T)=E$; in the scalar instance $\dot x=u$, $J=\tfrac12\int_0^T(x^2+u^2)dt$, the solution is $S=\tanh(T-t)$, the feedback is $u=-\tanh(T-t)x$, the closed loop is $x=x_0\cosh(T-t)/\cosh T$, and the Riccati solution exhibits the finite escape that separates the finite- from the infinite-horizon problem. The **time-optimal** problem with a bounded control has a Hamiltonian linear in the control, so the optimal control is **bang-bang**: for the double integrator it takes the values $\pm1$ with at most one switch, on the two parabolic arcs $\sigma=x_1+\tfrac12x_2\lvert x_2\rvert=0$, and the optimal times from $(1,0)$, $(2,0)$ and $(0,1)$ are $2$, $2\sqrt2$ and $1+\sqrt2$.

**Dynamic programming** introduces the value function $V$, the least cost from a state at a time, and derives from Bellman's principle the **Hamilton–Jacobi–Bellman equation** $V_t+\min_u[L+\langle V_x,f\rangle]=0$ with $V(\cdot,T)=\varphi$. A classical solution of that equation, together with a measurable minimiser, is optimal, so the method certifies **sufficiency** where the maximum principle produces candidates; the costate and the value function are related by $p=V_x$ along an optimal trajectory, and the maximum principle is the characteristic system of the Bellman equation. Convexity of the problem makes the maximum principle sufficient as well, and the value function's possible failure to be differentiable is the point of contact with the nonsmooth analysis of this Part.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $x$, $u$, $U$ | State, control, control set |
| $f(x,u,t)$ | Dynamics, $\dot x=f$ |
| $L$, $\varphi$, $J$ | Running cost, terminal cost, cost functional |
| $t_0$, $T$ | Initial and final times |
| $H=\langle p,f\rangle+L$ | Control Hamiltonian |
| $p$ | Costate, the multiplier of the state equation |
| $\dot x=H_p$, $\dot p=-H_x$ | State and costate equations |
| $u$ minimises $H$ | Pointwise condition of the maximum principle |
| $p(T)=\varphi_x(x(T))$ | Transversality for a free final state |
| $H(T)=0$ | Additional condition for a free final time |
| $A$, $B$, $C$, $D$, $E$ | System and cost matrices of the linear-quadratic problem |
| $S$ | Riccati matrix, $p=Sx$ |
| $\dot S=-C-A^{\mathsf T}S-SA+SBD^{-1}B^{\mathsf T}S$ | Matrix Riccati equation, $S(T)=E$ |
| $\sigma=x_1+\tfrac12x_2\lvert x_2\rvert$ | Switching function of the double integrator |
| $V(\xi,\tau)$ | Value function, the least cost from $(\xi,\tau)$ |
| $V_t+\min_u[L+\langle V_x,f\rangle]=0$ | Hamilton–Jacobi–Bellman equation |
| $p=V_x$ | Costate of the maximum principle as a value gradient |

## Further Reading

- Lev S. Pontryagin, Vladimir G. Boltyanskii, Revaz V. Gamkrelidze and Evgenii F. Mishchenko, *The Mathematical Theory of Optimal Processes* (Interscience, 1962), for the maximum principle, its proof by needle variations and its applications.
- Wendell H. Fleming and Raymond W. Rishel, *Deterministic and Stochastic Optimal Control* (Springer, 1975), for the maximum principle and dynamic programming side by side.
- Daniel Liberzon, *Calculus of Variations and Optimal Control Theory: A Concise Introduction* (Princeton University Press, 2012), for the maximum principle derived from the calculus of variations, with the Hamiltonian conventions used here.
- Eduardo D. Sontag, *Mathematical Control Theory: Deterministic Finite Dimensional Systems* (Springer, 2nd ed. 1998), for controllability, the bang-bang principle and the linear-quadratic theory.
- Michael Athans and Peter L. Falb, *Optimal Control: An Introduction to the Theory and Its Applications* (McGraw-Hill, 1966), for the classical engineering treatment of the Riccati equation and the time-optimal problem.
- Michael G. Crandall and Pierre-Louis Lions, "Viscosity Solutions of Hamilton–Jacobi Equations", *Transactions of the American Mathematical Society* 277 (1983), for the weak solutions of the Bellman equation.
- Hector J. Sussmann and Jan C. Willems, "300 Years of Optimal Control: From the Brachystochrone to the Maximum Principle", *IEEE Control Systems Magazine* 17 (1997), for the history of the subject.
