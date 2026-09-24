
# __Differential-Algebraic Equations__

## Introduction

A differential-algebraic equation is a system of relations among the unknown and its derivatives in which some relations are differential and some are purely algebraic. The unknown is therefore split, implicitly or explicitly, into a part that is governed by a differential equation and a part that at every instant is determined by the others through a constraint. The equations are the general implicit form of an ordinary differential equation, written $F(t,y,y')=0$ rather than $y' = f(t,y)$, and the difficulty is exactly that in general $F$ cannot be solved for $y'$: the derivative occurs in some equations only in combination with an algebraic relation, and the constraint may have to be differentiated before the system becomes an equation for the derivatives of all components.

The subject is the theory of that solvability. Its central invariant is the **index**, a nonnegative integer measuring how many differentiations of the constraints are needed before the system determines every derivative, equivalently how far the system is from being an ordinary equation, and equivalently how many derivatives of the inhomogeneity enter the solution. The index governs everything: whether an initial value is admissible, whether the solution depends continuously on the data, whether the problem is well posed for a numerical method, and how the solution responds to a perturbation of the constraint. A system of index one behaves like an ordinary equation with a parameter determined by an implicit equation; a system of index two or more is genuinely different, its solution containing derivatives of the data and its initial conditions overdetermined.

The setting is the finite-dimensional one, a state space $\mathbb{K}^n$ with $\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$, because the index theory is a theory of matrices and of the implicit function theorem, and the Jordan and Kronecker forms of Part I are the algebraic input. Where a result extends to a Banach space it is said so. The ordinary theory of *Ordinary Differential Equations* and the implicit function theorem of the differential calculus on normed spaces are assumed, and the constrained mechanical system that is the standard source of the subject is treated as an example of the general theory. The Lagrangian and Hamiltonian formulation of that example, and the variational reading of the constraints, belong to the article of this Part on Lagrangian and Hamiltonian systems, which is written in parallel and continues the example there.

## Implicit Equations and the Notion of Index

### The Implicit and Semi-Explicit Forms

**Definition.** Let $F : \mathbb{R}\times\mathbb{K}^n\times\mathbb{K}^n \to \mathbb{K}^n$ be a function. The **implicit differential equation** determined by $F$ is

$$
F(t, y, y') = 0 .
$$

It is a **differential-algebraic equation** if the partial derivative $F_{y'}$ is everywhere singular on the solution set, so that the equation cannot be solved for $y'$ by the implicit function theorem. The system is **semi-explicit** if it can be written

$$
y_1'(t) = f\bigl(t, y_1(t), y_2(t)\bigr), \qquad 0 = g\bigl(t, y_1(t), y_2(t)\bigr),
$$

with $y_1 \in \mathbb{K}^{n_1}$ the **differential variables** and $y_2 \in \mathbb{K}^{n_2}$ the **algebraic variables**; it is **linear with constant coefficients** if it has the form

$$
E\,y'(t) + A\,y(t) = q(t),
$$

with $E, A \in M_n(\mathbb{K})$ and $E$ singular.

The semi-explicit form is the general local form of a differential-algebraic equation, by the implicit function theorem applied to the equations in which $y'$ does occur: those equations are solved for the derivatives of $n_1$ components, and the remaining equations are the constraints.

**Example (the constrained motion of a particle).** A particle of unit mass constrained to a smooth surface $\{q : g(q)=0\}$ subject to a force $f(q,v)$ obeys

$$
q' = v, \qquad v' = f(q,v) - G(q)^{\mathrm{T}}\lambda, \qquad 0 = g(q),
$$

where $G = \partial g/\partial q$ and $\lambda$ is the vector of multipliers. The first two equations are differential, the third is the constraint; the unknown $(\lambda, q)$ is determined only through the constraint, and the system is the standard example of a differential-algebraic equation in mechanics, written here purely as a system of equations. The general Lagrangian and Hamiltonian account of constrained systems is the subject of the article of this Part on Lagrangian and Hamiltonian systems.

### Differentiation Index

**Definition.** The **differentiation index** of a semi-explicit system at a point is the least number $\nu$ of times the constraint $0 = g(t,y_1,y_2)$ must be differentiated with respect to $t$, using the differential equations to eliminate $y_1'$, until the resulting equations determine $y_2'$ as a continuous function of $(t,y_1,y_2)$. For a linear constant-coefficient system $Ey' + Ay = q$ with regular pencil the differentiation index is the size of the largest nilpotent block in the Kronecker form, and it is written $\nu(E,A)$.

The definition is local and can vary from point to point; a system has **index $\nu$** on a set if the index is $\nu$ at every point of it. Index zero is the case of an ordinary equation in implicit form. The index is the invariant of the theory, and the sections below compute it in the two cases that matter most.

**Definition.** Two further indices are used when the differentiation index is unsuitable. The **perturbation index** is the least $\nu$ such that, for every sufficiently small perturbation $\delta(t)$ of the equation, the solution satisfies an estimate

$$
\|y(t) - y_\delta(t)\| \le C\Bigl(\|\delta\|_\infty + \|\delta'\|_\infty + \cdots + \|\delta^{(\nu-1)}\|_\infty + \int_{t_0}^{t}\|\delta(s)\|\,ds\Bigr),
$$

uniformly on compact intervals, and the **tractability index** is a variant computed by a finite sequence of matrix operations on the coefficients. For the linear systems considered here the three generally agree, and the difference between the differentiation index and the perturbation index measures the amplification of a perturbation of the constraint.

**Theorem (the differentiation index counts derivatives of the data).** For a linear system $Ey' + Ay = q(t)$ with regular pencil and index $\nu$, every solution is of the form

$$
y = \sum_{k=0}^{\nu-1} c_k\,q^{(k)} + y_{\mathrm{hom}},
$$

where the $c_k$ are matrices and $y_{\mathrm{hom}}$ solves the homogeneous system; consequently the solution depends on the first $\nu-1$ derivatives of $q$, and the initial value $y(t_0)$ must satisfy $\nu-1$ consistency conditions for a solution to exist.

*Proof.* Quoted as standard, and proved in the next section by the Kronecker form. The statement follows from the explicit representation $v = \sum_{k=0}^{\nu-1}(-N)^kq_2^{(k)}$ for the algebraic part; each differentiation of $q_2$ raises the order of the derivative appearing, and there are exactly $\nu-1$ terms because $N^\nu = 0$. $\square$

## The Linear Theory and the Kronecker Form

### The Weierstrass–Kronecker Canonical Form

**Definition.** The **matrix pencil** determined by $E, A$ is the family $\lambda E + A$, and it is **regular** if $\det(\lambda E + A)$ is not identically zero as a polynomial in $\lambda$. For a regular pencil there are invertible matrices $P, Q \in GL_n(\mathbb{K})$ and a decomposition $n = r + s$ with

$$
PEQ = \begin{pmatrix} I_r & 0\\ 0 & N\end{pmatrix}, \qquad PAQ = \begin{pmatrix} J & 0\\ 0 & I_s\end{pmatrix},
$$

where $J$ is in Jordan form and $N$ is nilpotent with index $\nu$. This is the **Weierstrass–Kronecker form** of the pencil, and $\nu$ is the **index** of the pencil.

*Proof.* Quoted as standard (the Weierstrass canonical form for regular matrix pencils). The proof is the classification of the modules over $\mathbb{K}[\lambda]$ given by the pencil, using the structure theorem of finitely generated modules over a principal ideal domain, in the form developed for the Jordan form in Part I; the nilpotent part $N$ is the obstruction to solving for $y'$. $\square$

**Theorem (solution of the linear system).** In the coordinates of the Weierstrass–Kronecker form, write $y = Q(u, v)$ and $q = P^{-1}(q_1, q_2)$. Then the system $Ey' + Ay = q$ is equivalent to the uncoupled system

$$
u' + Ju = q_1, \qquad N v' + v = q_2 .
$$

The first is an ordinary linear system with the solution of *Ordinary Differential Equations*. The second is solved by

$$
v = \sum_{k=0}^{\nu-1}(-N)^k q_2^{(k)},
$$

a finite sum because $N$ is nilpotent of index $\nu$; it involves no free constant, so the value of $v$ is completely determined by $q_2$ and its derivatives, and in particular the initial value $v(t_0)$ must equal $\sum_{k}(-N)^kq_2^{(k)}(t_0)$.

*Proof.* Multiply the equation $Ey' + Ay = q$ by $P$ and change variable $y = Qw$ to obtain $PEQ w' + PAQ w = Pq$; with $w = (u,v)$ this is the displayed uncoupled system. For the second equation, the identity $v + Nv' = q_2$ gives $v = q_2 - Nv'$ and, differentiating and iterating, the induction

$$
v = \sum_{j=0}^{k-1}(-N)^jq_2^{(j)} + (-1)^kN^kv^{(k)} ,
$$

which is verified by substituting the case $k$ into $v = q_2 - Nv'$ to obtain the case $k+1$. At $k=\nu$ the last term vanishes because $N^\nu = 0$, giving the stated finite sum. $\square$

**Corollary (index of the constrained particle).** For the constrained particle with constraint $g(q)=0$ of rank $m$ and $G$ of full row rank, the differentiation index is $3$.

*Proof.* Differentiating $g(q)=0$ once gives $Gv = 0$; differentiating again gives $Gv' + \dot Gv = 0$, and substituting $v' = f - G^{\mathrm{T}}\lambda$ gives $Gf - GG^{\mathrm{T}}\lambda + \dot Gv = 0$, which determines $\lambda$ because $GG^{\mathrm{T}}$ is invertible when $G$ has full row rank; differentiating a third time and eliminating $v''$ and $\dot v$ determines $\lambda'$ as a continuous function of $(q,v)$. Hence the constraint must be differentiated three times before the multiplier derivative is obtained, and the index is $3$. $\square$

### Consistency and the Hidden Constraints

**Definition.** The **constraints** of a semi-explicit system are the equations $0 = g(t,y_1,y_2)$; the **hidden constraints** are the equations obtained by differentiating the constraints along solutions and eliminating the derivatives by the differential equations. An initial value is **consistent** if it satisfies the constraints and all the hidden constraints.

**Theorem (index one).** For the semi-explicit system $y_1' = f(t,y_1,y_2)$, $0=g(t,y_1,y_2)$ with $g_{y_2}$ invertible in a neighbourhood of a point $(t_0,y_1^0,y_2^0)$ satisfying $g(t_0,y_1^0,y_2^0)=0$, the constraint can be solved locally for $y_2 = G(t,y_1)$, $y_2^0 = G(t_0,y_1^0)$, and the system becomes the ordinary equation

$$
y_1' = f\bigl(t, y_1, G(t,y_1)\bigr) .
$$

Hence through every consistent point with $y_2^0 = G(t_0,y_1^0)$ there passes a unique solution; the only consistency condition is the constraint itself.

*Proof.* The implicit function theorem applied to $g$ in $y_2$ gives $G$ of class $C^1$ with $g(t,y_1,G(t,y_1))=0$; substituting into the differential equation gives an ordinary equation with a locally Lipschitz right-hand side, to which Picard–Lindelöf applies. Every solution of the original system satisfies this equation, and conversely a solution of the reduced equation with $y_2 = G(t,y_1)$ satisfies both the differential equation and the constraint. $\square$

**Example (index one with a hidden constraint of a different kind).** The system $y_1' = y_2$, $0 = y_1 - t^2$ has the constraint $y_1 = t^2$ and the differential equation gives $y_2 = y_1' = 2t$, so the constraint itself already determines $y_2$ and there is no hidden constraint; the index is one. The initial value must satisfy $y_1(t_0) = t_0^2$ and $y_2(t_0) = 2t_0$, and then the solution $(y_1,y_2) = (t^2, 2t)$ is unique.

## Higher Index and Its Consequences

The cases of index two and three are the ones in which the differential-algebraic theory differs from the ordinary theory in kind, and the difference is visible in three places: the number of consistency conditions, the dependence of the solution on derivatives of the data, and the response to perturbations.

**Example (an index-two linear system).** The system

$$
y_1' = y_1 + y_2 + q_1(t), \qquad 0 = y_1 + q_2(t)
$$

has $n_1 = n_2 = 1$ and constraint $g = y_1 + q_2 = 0$. Differentiating once, $y_1' + q_2' = 0$, and substituting the differential equation gives $y_1 + y_2 + q_1 + q_2' = 0$, which determines $y_2 = -y_1 - q_1 - q_2'$; the second differentiation is needed to get $y_2'$, so the index is two. The solution involves $q_2'$, and the initial value must satisfy the two conditions $y_1(t_0) = -q_2(t_0)$ and $y_2(t_0) = q_2(t_0) - q_1(t_0) - q_2'(t_0)$ rather than one. The matrix form has $E = \begin{pmatrix}1&0\\0&0\end{pmatrix}$, $A = \begin{pmatrix}-1&-1\\1&0\end{pmatrix}$; the determinant of the pencil is the constant $1$, so the pencil is regular with no finite eigenvalue, its Kronecker form consists entirely of a nilpotent block of size two, and the index is two.

**Proposition (sensitivity of an index-two system).** Perturb the index-two system above in the constraint to $0 = y_1 + q_2(t) + \delta(t)$. Then the solution of the perturbed system has $y_{1,\delta} = -q_2 - \delta$, and, when $\delta$ is differentiable,

$$
y_{2,\delta} = -q_1 - q_2' - \delta' - y_{1,\delta},
$$

so that

$$
\|y_2 - y_{2,\delta}\| \le \|\delta\|_\infty + \|\delta'\|_\infty .
$$

Thus a bound on the perturbation in the supremum norm alone does not bound the solution: the estimate requires control of the derivative of the perturbation.

*Proof.* Substituting the perturbed constraint into the differentiated constraint $y_1' = -q_2' - \delta'$ and integrating gives $y_1$, and substituting into the original differential equation gives $y_2 = -y_1 - q_1 - q_2' - \delta'$. The estimate is the triangle inequality. $\square$

**Remark (why higher index is different from the ordinary theory).** For an ordinary equation a continuous right-hand side that is Lipschitz gives a solution as smooth as the equation permits, and a perturbation of size $\varepsilon$ in the equation gives an error of order $\varepsilon$ in the solution. For a differential-algebraic equation of index $\nu$, a solution requires the inhomogeneity to be $\nu-1$ times differentiable, and a perturbation of the constraint of size $\varepsilon$ can produce an error of order $\varepsilon$ in the solution only if the differentiated perturbations are also controlled. This is the sense in which the index measures the distance from the ordinary theory, and it is the reason the index rather than the dimension is the invariant that governs the qualitative behaviour.

### Index Reduction and the Drift Phenomenon

**Definition.** **Index reduction** is the replacement of a differential-algebraic equation of index $\nu$ by an equivalent lower-index equation, classically by differentiating the constraints. The differentiated constraints are **invariants** of the original system: every solution of it satisfies them. Replacing a constraint by its derivative enlarges the solution set, because the differentiated equation is a consequence of the original but does not imply it; the original constraint must therefore be retained as well, and the reduced system consists of the original equations together with the differentiated constraints.

**Theorem (index reduction via constraint differentiation).** For the constrained particle the differentiated system

$$
q' = v, \qquad v' = f(q,v) - G(q)^{\mathrm{T}}\lambda, \qquad 0 = g(q), \qquad 0 = G(q)v
$$

has index two instead of three, and its solutions with $g(q(t_0))=0$ are exactly the solutions of the original system. Differentiating once more gives an index-one system.

*Proof.* The differentiated constraint $Gv=0$ determines one relation among the variables; substituting it into the constraint $g=0$ and differentiating once more produces the multiplier equation, which determines $\lambda$; the index drops by one at each differentiation by definition. Solutions of the original system satisfy the differentiated constraints, and conversely a solution of the reduced system that begins on $g=0$ keeps $g=0$ because $\frac{d}{dt}g(q) = Gv = 0$. $\square$

**Remark (the drift phenomenon).** A numerical method applied to the reduced system solves the differentiated constraint but not the original one, and the discrepancy, the **drift**, generally grows with time: the integration controls the equation that was imposed and leaves the discarded one to wander. This is why a differential-algebraic equation is not solved by a naive integration of a reduced ordinary system, and why the theory keeps the index as a property of the equation rather than of a reformulation.

## Constrained Systems and the Variational Seam

The constrained particle has a variational description that is the source of the index-three structure, and it is useful to record the seam without developing it.

**Proposition (the constrained variational problem).** The equations

$$
q' = v, \qquad v' = -V'(q) - G(q)^{\mathrm{T}}\lambda, \qquad 0 = g(q)
$$

are the stationarity equations of the action $\int \bigl(\tfrac12\|v\|^2 - V(q)\bigr)dt$ over the curves satisfying $g(q)=0$, the multiplier $\lambda$ being the Lagrange multiplier of the constraint. The stationarity conditions are a differential-algebraic system of index three.

*Proof.* The Lagrange multiplier rule for the constrained variational problem gives $q'' = -V'(q) - G^{\mathrm{T}}\lambda$ together with $g(q)=0$; writing $v = q'$ gives the first-order form, and the computation of the index is the corollary above. $\square$

The full variational account — the Euler–Lagrange equations, the Legendre transform, the Hamiltonian form and the role of the multiplier — belongs to the articles of this Part on the calculus of variations and on Lagrangian and Hamiltonian systems, written in parallel. What matters here is that the differential-algebraic structure is not an artefact of a bad formulation: it is intrinsic to a variational problem with a holonomic constraint, and the index is the number of differentiations of the constraint needed to express the multiplier.

To close the article, the ordinary differential equation $y'=f(t,y)$ is the index-zero case, the semi-explicit system with $g_{y_2}$ invertible is the index-one case, the constrained particle is the index-three case, and between them lies a hierarchy indexed by the differentiation index. Each level is a genuine extension of the one above: an index-one system is an ordinary equation on a manifold determined by the constraint, an index-two system has a hidden constraint and a solution containing one derivative of the data, and an index-three system is the stationary condition of a variational problem with a constraint.

## Summary

A differential-algebraic equation is an implicit equation $F(t,y,y')=0$ whose derivative $\partial F/\partial y'$ is singular on the solution set; the semi-explicit form $y_1' = f(t,y_1,y_2)$, $0=g(t,y_1,y_2)$ separates the differential from the algebraic variables, and the linear constant-coefficient case $Ey'+Ay=q$ with singular $E$ is the model problem. The invariant of the theory is the differentiation index, the number of differentiations of the constraint needed to determine the algebraic variables, and for a regular pencil it is the size of the largest nilpotent block of the Weierstrass–Kronecker form. In that form the system uncouples into an ordinary linear system and the nilpotent equation $Nv' + v = q_2$, whose solution $v = \sum_{k=0}^{\nu-1}(-N)^kq_2^{(k)}$ is a finite sum and shows that the solution depends on derivatives of the data up to order $\nu-1$.

Consequently an initial value must satisfy the constraints and the hidden constraints obtained by differentiation, so a higher-index problem has a positive number of consistency conditions rather than none. Index-one systems with invertible $g_{y_2}$ reduce to ordinary equations on a manifold and have unique solutions through consistent points; index-two and higher systems require differentiability of the data, have solutions containing derivatives of the data, and respond to perturbations of the constraint through the derivatives of the perturbation rather than through its size. Index reduction differentiates the constraints to lower the index, at the price of solving the differentiated constraint and drifting off the original one; the constrained mechanical system is the standard index-three example and is the stationary condition of a constrained variational problem. The index is thus the measure of how far an implicit equation is from an ordinary equation, and the theory is the ordinary theory plus the consistency, smoothness and sensitivity conditions that the index prescribes.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $F(t,y,y')=0$ | Implicit differential equation |
| $y_1 \in \mathbb{K}^{n_1}$, $y_2 \in \mathbb{K}^{n_2}$ | Differential and algebraic variables |
| $g(t,y_1,y_2)=0$ | Constraint of a semi-explicit system |
| $E$, $A$ | Coefficient matrices, $E$ singular, of $Ey'+Ay=q$ |
| $\lambda E + A$ | Matrix pencil; regular if $\det(\lambda E+A)\not\equiv0$ |
| $P$, $Q$, $r$, $s$ | Equivalences to Kronecker form and the sizes of its two blocks |
| $J$, $N$ | Jordan block and nilpotent block, $N^\nu=0$ |
| $\nu$ | Index: differentiation index, Kronecker index, perturbation index |
| hidden constraints | Differentiated constraints, $Gv=0$ etc. |
| $q$, $v$, $\lambda$, $G=g_q$ | Position, velocity, Lagrange multiplier and constraint gradient |
| $V(q)$ | Potential in the constrained variational problem |
| consistent initial value | One satisfying the constraints and the hidden constraints |
| drift | Violation of the original constraint by a reduced system |

## Further Reading

- Kathryn E. Brenan, Stephen L. Campbell and Linda R. Petzold, *Numerical Solution of Initial-Value Problems in Differential-Algebraic Equations* (SIAM, 1996), for the index, consistency and the numerical theory.
- Stephen L. Campbell and Carl D. Meyer, *Generalized Inverses of Linear Transformations* (Pitman, 1979; reprinted SIAM, 2009), for the Kronecker form and linear descriptor systems.
- Ernst Hairer and Gerhard Wanner, *Solving Ordinary Differential Equations II: Stiff and Differential-Algebraic Problems* (Springer, 2nd ed. 1996), for the index and its numerical consequences.
- Peter Kunkel and Volker Mehrmann, *Differential-Algebraic Equations: Analysis and Numerical Solution* (EMS, 2006), for the tractability index and a unified treatment.
- Ernst Hairer, Christian Lubich and Michel Roche, *The Numerical Solution of Differential-Algebraic Systems by Runge–Kutta Methods* (Springer, 1989), for index reduction and the drift phenomenon.
- Peter C. Müller, *Theory of Holonomic and Non-Holonomic Systems* (Bibliographisches Institut, 1977), for the mechanical origin of the constrained equations.
- Ronald A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 2nd ed. 2013), for the linear algebra of pencils and nilpotent blocks.
- Linda R. Petzold, "Differential/Algebraic Equations are not ODEs", *SIAM Journal on Scientific and Statistical Computing* 3 (1982), for the distinction between the two theories.
