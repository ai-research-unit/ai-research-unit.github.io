# __Biquaternion Regular Functions__

## Introduction

This article studies **regular** (equivalently **monogenic**) biquaternion-valued functions. It follows the articles on biquaternion analysis, biquaternion integration, and biquaternion analysis on subspaces, and assumes the biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, its four conjugations, its biquaternion norm $N(\tilde{Q}) = \tilde{Q}\tilde{Q}^{\natural} = \sum_\mu Q_\mu^2$, its Euclidean norm, and its zero divisors.

The decisive fact is that $\mathbb{B}$ is **not a division algebra**: it has nonzero elements with no inverse, the zero divisors, forming the null quadric $N(\tilde{Q}) = 0$. Every failure of the complex analogy on the full algebra and on the indefinite subspaces is traceable to this fact; on $\mathbb{H}_{\mathbb{B}}$ the remaining failures are those of dimension and non-commutativity, so a statement of regularity must specify both the operator with respect to which the function is regular and the domain on which it is defined. The treatment is purely mathematical and no physical interpretation is used. Throughout, $\tilde{Q} = \sum_\mu Q_\mu e_\mu$ with $Q_\mu \in \mathbb{C}$, the units are anti-commuting with

$$
e_0 = 1, \qquad e_1^2 = e_2^2 = e_3^2 = -e_0, \qquad e_1 e_2 = e_3, \quad e_2 e_3 = e_1, \quad e_3 e_1 = e_2,
$$

and $i$ is a central scalar imaginary. We write $\tilde{Q} = Q_0 e_0 + \mathbf{Q}$, $\mathbf{Q} = Q_1 e_1 + Q_2 e_2 + Q_3 e_3$.

## The Biquaternion Variable and Its Two Complex Structures

A **complex structure** on a real vector space is a real-linear map $J$ with $J^2 = -\mathrm{id}$. The biquaternion algebra carries a pair of commuting complex structures,

$$
J_i(\tilde{Q}) = i\tilde{Q}, \qquad J_1(\tilde{Q}) = e_1\tilde{Q}.
$$

Both square to $-\mathrm{id}$ and commute because $i$ is central; the same construction with $e_2$ or $e_3$ gives further ones, and every root of $-1$ in $\mathbb{B}$ defines one. The two named structures are the **coefficient complex structure** $J_i$, which complexifies the coefficients $Q_\mu$, and the **quaternionic complex structure** $J_1$, which complexifies the plane spanned by $e_0, e_1$.

The quaternionic structure turns that plane into a complex line with coordinate $A = q_0 + e_1 q_1$, and the complex combinations of $e_0, e_1$ form the commutative subalgebra

$$
\mathbb{C}[e_1] = \{a e_0 + b e_1 : a, b \in \mathbb{C}\} = \mathrm{span}_{\mathbb{R}}\{e_0, e_1, i e_0, i e_1\} \cong \mathbb{C} \times \mathbb{C},
$$

the largest commutative subalgebra in which $e_1$ is the imaginary unit; the coefficient structure similarly singles out $\mathbb{C}_{\mathbb{B}} = \mathbb{C} e_0$. These two structures give two inequivalent notions of holomorphy, distinguished in §*Regular Functions: Single-Plane versus Hypercomplex*: no single complex structure reduces the four real variables to one. Finally, $\mathbb{B}$ is a simple algebra whose centre is $\mathbb{C}_{\mathbb{B}}$, and its biquaternion norm vanishes exactly on the zero divisors and the origin.

## The Cauchy–Riemann Operator and Its Conjugate

On a four-dimensional real subspace $V \subset \mathbb{B}$ with complex coefficients $Q_0, \dots, Q_3$, the **biquaternionic gradient**, called here the **biquaternionic Cauchy–Riemann operator**, and its **quaternion conjugate** are

$$
\tilde{\nabla} = \sum_{\mu=0}^{3} e_\mu \frac{\partial}{\partial Q_\mu}, \qquad \tilde{\nabla}^{\natural} = e_0 \frac{\partial}{\partial Q_0} - \sum_{k=1}^{3} e_k \frac{\partial}{\partial Q_k}.
$$

This is the **Cauchy–Riemann operator** of the biquaternion theory, classically the Dirac operator. The pair $(\tilde{\nabla}, \tilde{\nabla}^{\natural})$ plays the role of $(\partial_{\bar{A}}, \partial_A)$ in one complex variable. On the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, where all coefficients are real and the partials are ordinary real derivatives, $\tilde{\nabla}$ is the **Cauchy–Riemann operator** on $\mathbb{R}^4$. The units satisfy the Clifford relation $e_\mu e_\nu^{\natural} + e_\nu e_\mu^{\natural} = 2\delta_{\mu\nu} e_0$, so the cross terms cancel and

$$
\tilde{\nabla}\tilde{\nabla}^{\natural} = \tilde{\nabla}^{\natural}\tilde{\nabla} = \Box := \left(\partial^2_{Q_0} + \partial^2_{Q_1} + \partial^2_{Q_2} + \partial^2_{Q_3}\right) e_0.
$$

The **d'Alembertian** $\Box$ is scalar and acts component-wise. On $\mathbb{H}_{\mathbb{B}}$ it is the Euclidean Laplacian of signature $(4,0)$; on $\mathbb{M}_-$ it is $-\partial^2_{q'_0} + \Delta_{\mathbb{M}_-}$ of signature $(3,1)$; on $\mathbb{M}_+$ it is $\partial^2_{q_0} - \Delta_{\mathbb{M}_+}$ of signature $(1,3)$; these are coordinate expressions of one abstract operator, the factors of $-i$ being a change of coordinates. The second-order operator $\tilde{\nabla}^2 = \tilde{\nabla}\tilde{\nabla} = (\partial^2_{Q_0} - \Delta_Q)e_0 + 2\sum_k e_k \partial^2_{Q_0 Q_k}$ also appears, with $\tilde{\nabla}^2 = 2\partial_{Q_0}\tilde{\nabla} - \Box \neq \Box$; it must not be confused with $\Box$, the natural second-order operator. For a function depending only on $q_0, q_1$,

$$
\tilde{\nabla}\tilde{F} = 2\partial_{\bar{A}}\tilde{F}, \qquad \tilde{\nabla}^{\natural}\tilde{F} = 2\partial_{A}\tilde{F}, \qquad \partial_{\bar{A}} = \tfrac{1}{2}(\partial_{q_0} + e_1\partial_{q_1}), \qquad \partial_{A} = \tfrac{1}{2}(\partial_{q_0} - e_1\partial_{q_1}).
$$

## Regular Functions: Single-Plane versus Hypercomplex

**Definition (left-regular).** Let $\Omega$ be open in a four-dimensional real subspace $V \subset \mathbb{B}$, and let $\tilde{F} : \Omega \to \mathbb{B}$ be continuously differentiable. Then $\tilde{F}$ is **left-regular**, or **left-monogenic**, if $\tilde{\nabla}\tilde{F} = 0$ on $\Omega$. It is **right-regular** if $\tilde{F}\tilde{\nabla} := \sum_\mu \partial_\mu\tilde{F}\, e_\mu = 0$ on $\Omega$. The two differ by non-commutativity — the units act on the left in the first and on the right in the second — and are exchanged by quaternion conjugation together with the interchange of $\tilde{\nabla}$ and $\tilde{\nabla}^{\natural}$ ($\tilde{\nabla}\tilde{F} = 0 \iff \tilde{F}^{\natural}\,\tilde{\nabla}^{\natural} = 0$); a function regular with respect to $\tilde{\nabla}^{\natural}$ is **anti-regular**, the analogue of an anti-holomorphic function.

**Convention.** In this series **regular** without qualification means **left-regular**, $\tilde{\nabla}\tilde{F} = 0$. This is fixed by the analysis and integration articles and determines which operator is inverted: the operator being inverted is the **first-order** operator $\tilde{\nabla}$, whose fundamental solution is the Cauchy kernel. It is not $\Box$, and it is not $\tilde{\nabla}^2$; several second-order operators can be built from $\tilde{\nabla}$, and only one has the Cauchy kernel as its fundamental solution. The opposite convention, $\tilde{\nabla}^{\natural}\tilde{F} = 0$, is also common in the literature and merely interchanges regular and anti-regular.

**Single-plane holomorphy.** Fix $A = q_0 + e_1 q_1$. A function independent of $q_2, q_3$ is holomorphic in $A$ in the classical sense precisely when $\tilde{\nabla}\tilde{F} = 2\partial_{\bar{A}}\tilde{F} = 0$. Hence every classical holomorphic function of $A$, extended by constancy in the orthogonal directions, is regular: the powers $A^n$, the inverse $(A - w)^{-1}$, and so on. Such functions use one complex structure and carry no information about $q_2, q_3$.

**Hypercomplex regularity.** The hypercomplex notion uses the full dependence on all four variables and the full Clifford structure. It is strictly larger than the single-plane class: the Cauchy kernel $\tilde{G} = \tilde{Q}^{\natural}/\|\tilde{Q}\|_E^4$ is regular on $\mathbb{H}_{\mathbb{B}} \setminus \{0\}$ and is not holomorphic in any single-plane variable. The two notions coincide only in two real dimensions, where the biquaternionic operator reduces to the classical Cauchy–Riemann operator in one complex variable.

## The System of Regularity Equations

Writing $\tilde{F} = F_0 + \mathbf{F}$ with $\mathbf{F} = F_1 e_1 + F_2 e_2 + F_3 e_3$, the analysis article gives

$$
\tilde{\nabla}\tilde{F} = \left(\partial_{Q_0}F_0 - \mathrm{div}\,\mathbf{F}\right) + \left(\partial_{Q_0}\mathbf{F} + \mathrm{grad}\,F_0 + \mathrm{rot}\,\mathbf{F}\right),
$$

with $\mathrm{div}\,\mathbf{F} = \sum_k \partial_{Q_k}F_k$, $\mathrm{grad}\,F_0 = \sum_k (\partial_{Q_k}F_0)e_k$, and $\mathrm{rot}\,\mathbf{F} = \sum_{j,k,l}\epsilon_{jkl}(\partial_{Q_j}F_k)e_l$. Therefore $\tilde{F}$ is regular if and only if

$$
\partial_{Q_0}F_0 = \mathrm{div}\,\mathbf{F}, \qquad \partial_{Q_0}\mathbf{F} + \mathrm{grad}\,F_0 + \mathrm{rot}\,\mathbf{F} = 0.
$$

This is a **system of four equations** for the four coefficients, the biquaternionic **Cauchy–Riemann–Fueter system**. It is the precise sense in which regularity is expressed by a system of equations rather than by one complex equation, and it is the local expression of the regularity notion inherited from the Clifford algebra, coupling $F_0$ to $\mathbf{F}$ through $\mathrm{div}$, $\mathrm{grad}$, and $\mathrm{rot}$.

On $\mathbb{H}_{\mathbb{B}}$ the principal symbol $s(\xi) = \sum_\mu \xi_\mu e_\mu$ satisfies $s(\xi)s^{\natural}(\xi) = |\xi|^2 e_0$, so the system is **elliptic** and its solutions are smooth (indeed real-analytic). On $\mathbb{M}_-$, with $s(\xi) = -i\xi_0 e_0 + \sum_k \xi_k e_k$, one finds

$$
s(\xi)s^{\natural}(\xi) = \left(-\xi_0^2 + \xi_1^2 + \xi_2^2 + \xi_3^2\right)e_0,
$$

which vanishes when $\xi_0^2 = \xi_1^2 + \xi_2^2 + \xi_3^2$. Thus on the indefinite subspaces $\tilde{\nabla}$ is not elliptic; it is a Cauchy–Riemann-type operator factoring the wave operator, and the null cone is its characteristic set. The elliptic tools of the complex theory — the maximum principle, the mean value property, and Liouville's theorem — are therefore not available on $\mathbb{M}_\pm$.

## Examples of Regular Functions

**Constants.** If $\tilde{F}(\tilde{Q}) = \tilde{C}$ is constant, then $\tilde{\nabla}\tilde{F} = 0$ on any subspace; the constants form an eight-real-dimensional space of regular functions.

**Powers of a single-plane variable.** On $\mathbb{H}_{\mathbb{B}}$, with $A = q_0 + e_1 q_1$, every $A^n$, $n \geq 0$, is regular, being holomorphic in $A$ and independent of $q_2, q_3$; for $n = 1$ directly, $\tilde{\nabla} A = e_0 \cdot e_0 + e_1 \cdot e_1 = e_0 - e_0 = 0$. The negative power $(A - w)^{-1}$ is regular away from $A = w$, and more generally every classical holomorphic function of $A$, extended by constancy in the orthogonal directions, is regular. These are the regular **linear** and power functions.

**The coordinate function is not regular.** On $\mathbb{H}_{\mathbb{B}}$, $\tilde{\nabla}\tilde{Q} = \sum_{\mu} e_\mu e_\mu = e_0 - 3e_0 = -2e_0 \neq 0$. So the identity function is not regular, in sharp contrast with the complex case, where $A$ is holomorphic; the regular object that replaces it is the Cauchy kernel of §*The Cauchy Integral Formula Where It Holds*.

**The Cauchy kernel.** On $\mathbb{H}_{\mathbb{B}}$, $\tilde{G}(\tilde{Q}) = \tilde{Q}^{\natural}/\|\tilde{Q}\|_E^4$ satisfies $\tilde{\nabla}\tilde{G} = 0$ for $\tilde{Q} \neq 0$; it is the fundamental solution of $\tilde{\nabla}$ and is singular only at the origin, since $\mathbb{H}_{\mathbb{B}}$ has no zero divisors.

**Closure properties.** Regular functions are closed under addition, under right multiplication by constants, $\tilde{\nabla}(\tilde{F}\tilde{C}) = (\tilde{\nabla}\tilde{F})\tilde{C} = 0$, and under left multiplication by complex scalars, since $\lambda$ is central. Left multiplication by a **general** constant does not preserve regularity: on $\mathbb{H}_{\mathbb{B}}$, $\tilde{\nabla}(e_2 A) = e_0 e_2 + e_1 e_2 e_1 = e_2 + e_3 e_1 = 2e_2 \neq 0$. Thus the regular functions form a right $\mathbb{B}$-module under pointwise right multiplication by constants, but not a left module. Similarly $\tilde{\nabla}(cA) = c + e_1 c e_1 = 2(c_2 e_2 + c_3 e_3)$, so $cA$ is regular exactly when $c \in \mathbb{C}[e_1]$.

## Harmonicity and the Factorization of the Laplacian

Since $\Box = \tilde{\nabla}^{\natural}\tilde{\nabla}$, every left-regular function is harmonic: $\Box\tilde{F} = \tilde{\nabla}^{\natural}(\tilde{\nabla}\tilde{F}) = 0$, that is, $(\sum_\mu \partial^2_{Q_\mu})\tilde{F} = 0$. On $\mathbb{H}_{\mathbb{B}}$ this is the ordinary Laplace equation for each coefficient $F_\nu$; on $\mathbb{M}_\pm$ it is the wave equation. The converse fails: $q_0$ on $\mathbb{H}_{\mathbb{B}}$ is harmonic but $\tilde{\nabla} q_0 = e_0 \neq 0$. The factorization is the analogue of $\partial_A \partial_{\bar{A}} = \tfrac{1}{4}\Delta$ in one complex variable, and it explains why the harmonic functions form a strictly larger class. Right-regular functions are likewise harmonic: if $\tilde{F}\tilde{\nabla} = 0$, then

$$
0 = \left(\tilde{F}\tilde{\nabla}\right)\tilde{\nabla}^{\natural} = \sum_{\mu,\nu} \partial^2_{Q_\mu Q_\nu}\tilde{F}\, e_\mu e_\nu^{\natural} = \sum_{\mu=0}^{3} \partial^2_{Q_\mu}\tilde{F} = \Box\tilde{F},
$$

the mixed terms cancelling by the Clifford relation. Every regular function also satisfies $\tilde{\nabla}^2\tilde{F} = 0$, but $\tilde{\nabla}^2$ is not the natural second-order operator.

## The Cauchy Integral Formula Where It Holds

The integral theory is developed on $\mathbb{H}_{\mathbb{B}}$, where it is the standard Clifford analysis of $\mathbb{R}^4$ and is complete because $\mathbb{H}_{\mathbb{B}}$ is a division algebra. The following results are established in the integration article.

**Theorem (fundamental solution).** On $\mathbb{H}_{\mathbb{B}}$, the function $\tilde{G}(\tilde{Q}) = \tilde{Q}^{\natural}/\|\tilde{Q}\|_E^4$ satisfies $\tilde{\nabla}\tilde{G} = 0$ for $\tilde{Q} \neq 0$ and, in the sense of distributions, $\tilde{\nabla}\tilde{G} = -2\pi^2 \delta_0\, e_0$.

**Theorem (Cauchy integral formula).** Let $\tilde{F}$ be continuously differentiable on a domain $\Omega \subset \mathbb{H}_{\mathbb{B}}$ with piecewise smooth boundary $\partial\Omega$, and let $\tilde{Q}_0$ be an interior point. Then

$$
\tilde{F}(\tilde{Q}_0) = \frac{1}{2\pi^2}\int_{\partial\Omega}\tilde{G}(\tilde{Q} - \tilde{Q}_0)\tilde{n}\tilde{F}(\tilde{Q})\,dS - \frac{1}{2\pi^2}\int_{\Omega}\tilde{G}(\tilde{Q} - \tilde{Q}_0)(\tilde{\nabla}\tilde{F})(\tilde{Q})\,dV,
$$

where $\tilde{n}$ is the biquaternion-valued outward unit normal. If $\tilde{F}$ is regular, the volume term vanishes and

$$
\tilde{F}(\tilde{Q}_0) = \frac{1}{2\pi^2}\int_{\partial\Omega}\tilde{G}(\tilde{Q} - \tilde{Q}_0)\tilde{n}\tilde{F}(\tilde{Q})\,dS.
$$

Three hypotheses must be emphasized: the formula holds on the **quaternion subspace** $\mathbb{H}_{\mathbb{B}}$, where all four coefficients of $\tilde{Q}$ are real, and is **not** asserted on $\mathbb{M}_+$ or $\mathbb{M}_-$ or on the full algebra $\mathbb{B}$ (§*Where the Complex Analogy Fails: Zero Divisors and the Null Cone*); regularity is required on all of $\Omega$, not merely on the boundary; and the operator inverted is the first-order operator $\tilde{\nabla}$, normalized by $\tilde{\nabla}\tilde{G} = -2\pi^2\delta_0 e_0$. The mean value property, the maximum principle, Liouville's theorem, the identity theorem, the Cauchy estimates, and the residue theory for isolated singularities then follow, as in the integration article, on $\mathbb{H}_{\mathbb{B}}$ only.

## The Shifted Operator

The theory above is the theory of $\tilde{\nabla}$. Its **shift** is a larger theory, and it is the one that boundary-value problems use. With $D = i\sum_{k=1}^{3}e_k\partial_k$, so that $D^2 = \Delta$, and $M_\alpha$ right multiplication by $\alpha\in\mathbb{B}$,

$$
D_\alpha = D + M_\alpha ,
$$

the equation $D_\alpha f = 0$ defines the **$\alpha$-hyperholomorphic** functions. The parameter is an arbitrary element of the algebra: it may be a zero divisor, its square need not be scalar, and it need not commute with the units. The class therefore contains the Helmholtz-type shifts ($\alpha$ scalar) and, for a non-scalar $\alpha$, cases the Helmholtz theory does not have. The integral operators of the shifted theory are the Teodorescu transform $T_\alpha$, the Cauchy-type operator $K_\alpha$ and the operator of singular integration $S_\alpha$, built from the fundamental solution of $D_\alpha$; their formulas branch in three cases — $\alpha$ not a zero divisor; $\alpha$ a zero divisor with $\alpha_0\neq0$; $\alpha$ a zero divisor with $\alpha_0 = 0$ — because the kernel is built by inverting the symbol.

**Theorem.** With $T_\alpha$, $K_\alpha$ and $S_\alpha$ so defined, the Borel–Pompeiu formula, the Cauchy integral formula, the Plemelj–Sokhotski formulas, the involution $S_\alpha^2 = I$, the Cauchy integral theorem and the Morera theorem hold for $D_\alpha$ in the same shape as for $D$, on a domain with Liapunov boundary and Hölder data.

**Theorem (boundary-value criterion).** A Hölder function $f$ on $\Gamma = \partial\Omega$ is the boundary value of a solution of $D_\alpha g = 0$ in $\Omega$ if and only if

$$
P_\alpha f = f \ \text{ on } \Gamma, \qquad P_\alpha = \tfrac12(I + S_\alpha),
$$

and then $g = K_\alpha f$.

The criterion answers the question the Cauchy formula of the previous section leaves open. The formula reconstructs a regular function from boundary values already known to be admissible; the criterion decides which Hölder data are admissible at all, which is what a boundary condition alone supplies. It is the case $B=1$ of the Riemann boundary value problem $f^+ = f^-B+h$ of *Riemann Boundary Value Problems and Singular Integral Equations*: the criterion says that the datum lies in the $+1$ eigenspace of $S_\alpha$, and the general problem replaces the coefficient $1$ by an invertible $B$ and the single condition by the reduction of that article. The parameter itself can therefore be singular, not only the variable: for the pure element $\alpha = -(i\omega e_1+me_2)$ the norm is $N(\alpha) = m^2-\omega^2$, so $\alpha$ is a zero divisor — and, being pure, a nilpotent with $\alpha^2 = 0$ — exactly when $\omega^2 = m^2$. That is the third branch above, $\alpha$ a zero divisor with $\alpha_0 = 0$, and it is the criterion of *Zero Divisors of the General Plain Algebra* applied to the parameter rather than to the variable. The physical reading of the same identity, and the boundary-value problem that uses the criterion, are in the physics register of this article.

### The Helmholtz Null-Set Splits

For a **scalar** parameter the shifted theory has one further algebraic fact, and it is the fact on which the numerical theory of the operator rests. Let $\alpha\in\mathbb{C}$, $\alpha\neq0$, and let $D_\alpha = D+\alpha$ be regarded on the null-set of the shifted Laplacian, $(\Delta-\alpha^2)u=0$, which is the same as $D_\alpha D_{-\alpha}u=0$ because $D_\alpha D_{-\alpha}=D^2-\alpha^2=\Delta-\alpha^2$ for scalar $\alpha$. Define the two **shifted projectors**

$$
\Pi_{\pm\alpha}=\mp\frac{1}{2\alpha}D_{\mp\alpha}.
$$

**Proposition.** On $\ker(\Delta-\alpha^2)$ the operators $\Pi_{\pm\alpha}$ are complementary idempotents with ranges $\ker D_{\pm\alpha}$:

$$
\Pi_{\pm\alpha}^2=\Pi_{\pm\alpha},\qquad
\Pi_\alpha\Pi_{-\alpha}=\Pi_{-\alpha}\Pi_\alpha=0,\qquad
\Pi_\alpha+\Pi_{-\alpha}=I,\qquad
\operatorname{im}\Pi_{\pm\alpha}=\ker D_{\pm\alpha},
$$

and consequently

$$
\ker(\Delta-\alpha^2)=\ker D_\alpha\oplus\ker D_{-\alpha}.
$$

*Proof.* The shifts commute, both being $D$ plus a scalar. The sum is $\Pi_\alpha+\Pi_{-\alpha}=-\frac{1}{2\alpha}D_{-\alpha}+\frac{1}{2\alpha}D_{\alpha}=\frac{1}{2\alpha}\bigl((D+\alpha)-(D-\alpha)\bigr)=I$; the products are $\Pi_\alpha\Pi_{-\alpha}=-\frac{1}{4\alpha^2}D_{-\alpha}D_\alpha=-\frac{1}{4\alpha^2}(\Delta-\alpha^2)=0$ on the null-set, and likewise in the other order; and the idempotence is $\Pi_\alpha^2=\frac{1}{4\alpha^2}\bigl(\Delta-2\alpha D+\alpha^2\bigr)=\frac{1}{4\alpha^2}\bigl(2\alpha^2-2\alpha D\bigr)=-\frac{1}{2\alpha}(D-\alpha)=\Pi_\alpha$, the third equality using $\Delta=\alpha^2$ on the null-set. For the range, $D_\alpha f=0$ gives $Df=-\alpha f$, whence $(D-\alpha)f=-2\alpha f$ and $\Pi_\alpha f=f$: so $\Pi_\alpha$ fixes $\ker D_\alpha$ pointwise, and conversely $\Pi_\alpha f=f$ gives $D_{-\alpha}f=-2\alpha f$, hence $D_\alpha f=-\frac{1}{2\alpha}D_\alpha D_{-\alpha}f=0$ on the null-set. The same with $\alpha$ replaced by $-\alpha$. $\square$

The idempotence is a statement on the null-set only, and this is not a technicality: off it the two operators fail to be projections, the computation using $\Delta=\alpha^2$. The shift carries the opposite sign in the physics register, where the argument is written with $D_3=\sum_k e_k\partial_k$ so that $\Delta+\alpha^2=-(D_3+\alpha)(D_3-\alpha)$; the algebra is the same, only the naming of $\alpha$ differs, and the statement there is that the ambient space of the boundary-value problems is assembled from the two shifted kernels. The decomposition is also the single-quaternion form of the statement in *The Time-Harmonic Maxwell Operator and the Quaternionic Cauchy Integral* that the Helmholtz null-set is the direct sum of the two rotated copies of $\ker N$: the rotated copies are the matrix version of $\Pi_{\pm\alpha}$.

**Remark (the shifted projectors are not the boundary projectors).** The pair $\Pi_{\pm\alpha}$ is not the pair $P_\alpha,Q_\alpha=\tfrac12(I\mp S_\alpha)$ of the boundary-value theory. Both pairs are complementary idempotents cutting the same ambient space into the same two pieces, but $\Pi_{\pm\alpha}$ are **differential** operators acting inside the domain, while $P_\alpha,Q_\alpha$ are **singular-integral** operators acting on boundary data. The passage from the interior splitting to the boundary splitting is the composition $Q_\alpha\gamma\Pi_\alpha\Lambda$, with $\Lambda$ the extension operator of the Dirichlet problem and $\gamma$ the trace; that composition is what carries the completeness of the systems of fundamental solutions on $\Gamma$ from the completeness of the scalar Helmholtz system in the domain.

### The Split of the Parameter

A parameter that is not a zero divisor can be reduced to two that are. The reduction is a statement about the algebra, and it is the reason the degenerate branch of the three is not a side case.

**Theorem (the split of the parameter).** Let $\alpha\in\mathbb{B}$ be **pure** and let $\gamma\in\mathbb{C}$ satisfy $\gamma^2 = \alpha^2$, the square being the algebra's own, so that $\alpha = \gamma u$ with

$$
u = \frac{\alpha}{\gamma}, \qquad u^2 = 1, \qquad u^{\natural} = -u .
$$

Then $u$ is a **non-Hermitian root of $+1$**, in the classification of *Biquaternion Square Roots of Minus One, Zero and Plus One*, and the elements

$$
\beta_\pm = \tfrac12(1\pm u), \qquad \alpha_\pm = \tfrac12(\alpha\pm\gamma) = \pm\gamma\beta_\pm
$$

satisfy

$$
\beta_\pm^2 = \beta_\pm, \quad \beta_++\beta_- = 1, \quad \beta_+\beta_- = 0, \quad N(\beta_\pm) = 0,
$$

$$
\alpha_++\alpha_- = \alpha, \qquad \alpha_+\alpha_- = 0, \qquad N(\alpha_\pm) = 0 .
$$

Both halves of the parameter therefore lie on the zero-divisor cone, and the two projectors — right multiplication by $\beta_\pm$, which is the source's form $P_\pm = (2\gamma)^{-1}M(\gamma\pm\alpha)$ — are complementary, null and **not orthogonal**. With those $P_\pm$ the shifted operators satisfy

$$
D_{\alpha_+}P_+ + D_{\alpha_-}P_- = D_\alpha .
$$

*Proof.* Since $\alpha$ is pure, $u^{\natural} = -u$, and $\gamma$ is central and scalar, so $u^2 = \alpha^2/\gamma^2 = 1$ and $N(u) = -\alpha^2/\gamma^2 = -1$: over $\mathbb{C}$ the element $u$ is a unit vector, so it is a root of $+1$ that is not Hermitian, and the projectors it defines are not orthogonal. Idempotence is $\beta_\pm^2 = \tfrac14(1\pm 2u+u^2) = \tfrac12(1\pm u)$; complementarity is $1$; orthogonality is $\beta_+\beta_- = \tfrac14(1-u^2) = 0$; and nullity is $N(\beta_\pm) = \tfrac14(1\pm u)(1\mp u) = \tfrac14(1-u^2) = 0$, the second factor being $\overline{1\pm u}$ because $u^{\natural} = -u$. The parameter statements follow from $\alpha_\pm = \pm\gamma\beta_\pm$ and $\beta_\pm^2 = \beta_\pm$: $\alpha_++\alpha_- = \gamma(\beta_+-\beta_-) = \gamma u = \alpha$, and $\alpha_+\alpha_- = -\gamma^2\beta_+\beta_- = 0$ with $N(\alpha_\pm) = \gamma^2N(\beta_\pm) = 0$. For the operator identity, $D_{\alpha_\pm}P_\pm = D M_{\beta_\pm} + M_{\alpha_\pm\beta_\pm}$ and $\alpha_\pm\beta_\pm = \pm\gamma\beta_\pm^2 = \pm\gamma\beta_\pm$, so the two terms sum to $D(M_{\beta_+}+M_{\beta_-}) + M_{\gamma(\beta_+-\beta_-)} = D + M_\alpha$. $\square$

**Remark (the factor of two, and the source's writing).** The source prints the halves as $\alpha\pm\gamma$ rather than as $\tfrac12(\alpha\pm\gamma)$, and with those it is the same computation one step further: $\alpha_+\beta_+ + \alpha_-\beta_- = \gamma(\beta_++\beta_-) = \gamma$, so the two projected operators sum to $D + M_\gamma$ and, since $\gamma = \alpha - (\alpha-\gamma)$, the identity reads $D_{\alpha+\gamma}P_+ + D_{\alpha-\gamma}P_- = 2D_\alpha - D$. The two writings differ only by the overall factor two on the shift, and both agree on what matters: the halves are zero divisors, $(\alpha+\gamma)(\alpha-\gamma) = \alpha^2-\gamma^2 = 0$, whatever the factor. The factor is worth a line because the source's Cauchy-operator identity $K_\alpha = P_+K_{\alpha_+}+P_-K_{\alpha_-}$ is stated with its own halves, and only one of the two readings can be the one the kernel satisfies.

**Remark (why the reduction matters).** The equation with a unit parameter is thus assembled from two equations whose parameters are on the zero-divisor cone, and the boundary-value theory of those two is the degenerate branch above. The reduction is the algebraic fact behind a pattern that recurs wherever the corpus splits a field into two circular or two chiral components: two first-order equations whose shifts are the halves of one parameter, the two kernels carrying the two signs of the exponential, and the whole assembled by the complementary projectors. It is the same construction as the pair of idempotents of *The Biquaternion Vacuum as a Minimal Idempotent* read with the parameter's direction in place of the vacuum's, and it is why the *helicity* components of a time-harmonic field are a pair of projected shifted equations rather than a single one. The reading of the pair as helicity is in the physics register, with the field.

**The variable coefficient, and the Vekua equation.** The parameter above is constant, and the shifted theory is the theory of one constant shift. A variable coefficient of the special form $\vec{\alpha}=\mathrm{grad}\,\phi/\phi$ is removable, and this is worth recording here because it is the exact point at which the theory of regular functions meets the theory of generalized analytic functions. For a scalar carrier function $\phi\neq0$ and biquaternion-valued $g$,

$$
\left(D+\frac{\mathrm{grad}\,\phi}{\phi}\right)g=\frac{1}{\phi}\,D(\phi g),
\qquad
\left(D-\frac{\mathrm{grad}\,\phi}{\phi}\right)f=\phi\,D\!\left(\frac{f}{\phi}\right),
$$

the **carrier identity**, which follows from $D[\phi g]=(D\phi)g+\phi Dg$ because a scalar commutes with the units, and which holds for $D=i\sum_k e_k\partial_k$ as much as for its un-multiplied form. It says that $D$ shifted by a gradient coefficient is $D$ conjugated by multiplication by $\phi$: a gradient coefficient is not a new operator but a conjugate presentation of the same one. Equivalently, write $L_{\vec{\alpha}}:g\mapsto Dg-\vec{\alpha}g$ and $R^{\vec{\alpha}}:g\mapsto Dg+g\vec{\alpha}$ for the two ways of shifting by a coefficient on the left and on the right. The carrier identity disposes of $L_{\vec{\alpha}}$ at once, since $L_{\vec{\alpha}}$ is conjugate to $D$ and therefore exactly as hard as the un-shifted operator of the section above; it says nothing about $R^{\vec{\alpha}}$, which is genuinely new. What $R^{\vec{\alpha}}$ is, is a Schrödinger operator in disguise: in the normalisation of $D$ used by the sibling article *Electromagnetism in Media — The Local Complex Structure at Work* — there $D=e_1\partial_1+e_2\partial_2+e_3\partial_3$, so that $D^2=-\Delta$ rather than $+\Delta$ — the mixed product $R^{\vec{\alpha}}L_{\vec{\alpha}}u$ is $(-\Delta+v)u$ for scalar $u$, with $v=\Delta\phi/\phi$, and the quadratic relation $D\vec{\alpha}+\vec{\alpha}^2=-v$ that makes it so is the quaternionic Riccati equation and is satisfied identically by $\vec{\alpha}=\mathrm{grad}\,\phi/\phi$. That relation is what makes $R^{\vec{\alpha}}$ solvable by reduction to a scalar problem: every solution $\psi$ of $-\Delta\psi+v\psi=0$ yields a solution $(D-\vec{\alpha})\psi$ of $R^{\vec{\alpha}}F=0$, and a fundamental solution of $-\Delta+v$ yields a fundamental solution of $R^{\vec{\alpha}}$. The whole reduction is normalisation-dependent — adjoining the factor $i$ to $D$ changes the sign of the linear term in the relation $D\vec{\alpha}+\vec{\alpha}^2=-v$ and hence which potential pairs with which operator — so the factorisation stated here is tied to the convention just named, and it is re-derived for the electromagnetic problem in the sibling article. A first-order equation whose coefficients act on both $f$ and its conjugate $f^{*}$ is a **Vekua equation**, the governing equation of the pseudoanalytic functions, and the electromagnetic instance — the Maxwell system of an arbitrary inhomogeneous medium reduced to exactly such an equation, with $\sqrt{\epsilon}$ and $\sqrt{\mu}$ as carriers — is developed there. The constant-shift section above is the constant-carrier case of that development, and the asymmetry between $L_{\vec\alpha}$ and $R^{\vec\alpha}$ is the same asymmetry that decides which of the two carries the Schrödinger connection.

## Where the Complex Analogy Fails: Zero Divisors and the Null Cone

The complex theory rests on $\mathbb{C}$ being a field. In the biquaternion algebra this fails, and every consequence below is traceable to the zero divisors.

The zero divisors are exactly the nonzero elements with $N(\tilde{Q}) = Q_0^2 + Q_1^2 + Q_2^2 + Q_3^2 = 0$. The zero divisor set $\mathcal{Z}$ is a complex cone of complex dimension $3$ (real dimension $6$); on the indefinite subspaces it cuts out the double cones $q_0^2 = (q'_1)^2 + (q'_2)^2 + (q'_3)^2$ in $\mathbb{M}_+$ and $(q'_0)^2 = q_1^2 + q_2^2 + q_3^2$ in $\mathbb{M}_-$, each three-dimensional with apex at the origin; in $\mathrm{Vect}(\mathbb{B})$ the biquaternion norm is complex and vanishes on the nilpotent cone, of real dimension $4$; while on $\mathbb{C}_{\mathbb{B}}$, $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$ the biquaternion norm is definite and there are none. On the null cone there is no inverse, so no quotient $\tilde{A}/\tilde{Q}$ is defined, and the naive difference quotient of the analysis article requires $\tilde{H}^{-1}$, which may not exist.

The proof that $\tilde{\nabla}\tilde{G} = 0$ uses $\tilde{Q}^{\natural}\tilde{Q} = \|\tilde{Q}\|_E^2 e_0$, which requires real coefficients; on $\mathbb{M}_\pm$ this identity fails, so $\tilde{G}$ is not a fundamental solution and no Cauchy formula of the stated form holds, and whether a modified kernel exists is open (integration article). By §*The System of Regularity Equations* the principal symbol degenerates on the null cone on $\mathbb{M}_\pm$, so the system is not elliptic and the maximum principle, the mean value property, and Liouville's theorem do not generalize; a regular function there, if defined, solves a hyperbolic rather than an elliptic system. The natural singular set is the six-real-dimensional null quadric, not a point, so there is no punctured-disk model and the residue theory of the integration article is correspondingly delicate.

On the indefinite subspaces the null cone is thus simultaneously the zero divisor set, the characteristic set of $\tilde{\nabla}$, and the set where the Cauchy kernel ceases to be a fundamental solution. A theorem about regular functions must therefore either restrict to a domain avoiding the cone — or, better, to a subspace such as $\mathbb{H}_{\mathbb{B}}$ — or state explicitly which weakened conclusion replaces the classical one. No Cauchy formula may be asserted beyond the quaternion subspace.

## The Naive Inverse Function and the Role of the Null Cone

The naive transcription of $1/(A - w)$ is $\tilde{F}(\tilde{Q}) = \tilde{Q}^{-1} = \tilde{Q}^{\natural}/N(\tilde{Q})$, defined exactly on the group of units, that is, off the null quadric with the origin removed; it does not exist on the null cone. Its singular set is six-dimensional, not isolated, so there is no Laurent expansion about an isolated pole.

On $\mathbb{H}_{\mathbb{B}}$, where $N(\tilde{Q}) = \|\tilde{Q}\|_E^2$ is real and positive definite, the inverse exists for all $\tilde{Q} \neq 0$, but it is **not regular**: a direct computation gives

$$
\tilde{\nabla}\left(\frac{\tilde{Q}^{\natural}}{\|\tilde{Q}\|_E^2}\right) = \frac{4e_0}{\|\tilde{Q}\|_E^2} - \frac{2e_0}{\|\tilde{Q}\|_E^2} = \frac{2e_0}{\|\tilde{Q}\|_E^2} \neq 0.
$$

The genuine regular radial function is the Cauchy kernel $\tilde{G} = \tilde{Q}^{\natural}/\|\tilde{Q}\|_E^4$. In four variables the fundamental solution of $\tilde{\nabla}$ has homogeneity $1 - 4 = -3$, and the exponent $4$ is exactly this homogeneity; the naive inverse carries the two-dimensional exponent and is the fundamental solution of the Cauchy–Riemann operator only in the complex plane. The single-plane inverse $(A - w)^{-1}$ is regular, so this failure is a genuinely hypercomplex phenomenon — the change of dimension from two to four — not merely a consequence of non-commutativity. The null cone thus enters in two ways: on the full algebra it makes the inverse undefined on a positive-dimensional set, and on $\mathbb{H}_{\mathbb{B}}$, where the cone is absent, the naive inverse is still the wrong function, the correct kernel being selected by the homogeneity required in four variables.

## Relation to Fueter and Quaternionic Theories

Restricting to real quaternion-valued functions on $\mathbb{H}_{\mathbb{B}}$ recovers Fueter's quaternionic analysis: $\tilde{\nabla}$ is the Cauchy–Riemann operator $D$, the equation $DF = 0$ is the Cauchy–Riemann–Fueter equation, and the Cauchy formula, mean value property, maximum principle, Liouville theorem, identity theorem, Taylor and Laurent expansions, and residue theorem all hold (quaternion analysis article). Since $\mathbb{H}$ is a division algebra, this case has no zero divisors and is a complete analogue of the complex theory in the sense appropriate to four real variables; the biquaternion theory is its complexification, the variable remaining quaternionic in structure while the coefficients become complex.

The general framework is Clifford analysis. Since $\mathbb{B} \cong \mathrm{Cl}_{1,3}^{+}$, the regular functions of this article are the monogenic functions of the even Clifford algebra in four dimensions; relative to the quaternionic case, the additional structure is the complex coefficients, the four conjugations, the two complex structures, and the zero divisors. The bridge between the single-plane and hypercomplex notions is the **Fueter–Sce construction**: a slice-regular function is generally not monogenic, but applying the appropriate power of the Laplacian to a slice-regular function produces a monogenic one. Due to Fueter and completed by Sce, this is the precise mechanism converting holomorphic data of a single complex variable into regular functions of four real variables; it is treated in the companion article on Fueter theory for biquaternions.

## Summary

Regularity for biquaternion-valued functions must specify both the operator and the domain. A function is **left-regular** (left-monogenic) if $\tilde{\nabla}\tilde{F} = 0$ and right-regular if $\tilde{F}\tilde{\nabla} = 0$, where $\tilde{\nabla} = \sum_\mu e_\mu \partial_{Q_\mu}$ is the biquaternionic Cauchy–Riemann operator; the two notions are exchanged by quaternion conjugation, and a function regular for $\tilde{\nabla}^{\natural}$ is anti-regular, the analogue of an anti-holomorphic function. In this series regular unqualified means left-regular for the first-order operator $\tilde{\nabla}$, the operator whose fundamental solution is the Cauchy kernel; it is not $\Box$ and not $\tilde{\nabla}^2$.

Two notions of regularity must be kept apart. **Single-plane holomorphy** takes one complex variable $A = q_0 + e_1 q_1$, with $q_2, q_3$ entering only as parameters; every classical holomorphic function, extended by constancy in the orthogonal directions, is regular. **Hypercomplex regularity** uses the full dependence on all four variables and the full Clifford structure, is strictly larger, and contains the Cauchy kernel $\tilde{G} = \tilde{Q}^{\natural}/\|\tilde{Q}\|_E^4$, which is regular on $\mathbb{H}_{\mathbb{B}}\setminus\{0\}$ and holomorphic in no single-plane variable. Since $\Box = \tilde{\nabla}^{\natural}\tilde{\nabla}$ is scalar, every regular function is harmonic, but the converse fails, and $\tilde{\nabla}^2$ annihilates regular functions without being the natural second-order operator.

The integral theory is complete on the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, where the algebra is a division ring: the Cauchy integral formula holds there with fundamental solution $\tilde{\nabla}\tilde{G} = -2\pi^2\delta_0 e_0$, and the mean value property, maximum principle, Liouville theorem, identity theorem, Cauchy estimates and residue theory follow. Everything that fails elsewhere fails through the zero divisors: on $\mathbb{M}_\pm$ and on the full algebra the identity $\tilde{Q}^{\natural}\tilde{Q} = \|\tilde{Q}\|_E^2 e_0$ fails, the principal symbol degenerates on the null cone, the system is hyperbolic rather than elliptic, and no Cauchy formula may be asserted. The naive inverse $\tilde{Q}^{-1} = \tilde{Q}^{\natural}/N(\tilde{Q})$ fails in two ways: on the full algebra it is undefined on the positive-dimensional null cone, and even on $\mathbb{H}_{\mathbb{B}}$, where it exists, it is not regular, the correct kernel in four variables being fixed by the homogeneity $1 - 4 = -3$ rather than the two-dimensional exponent.

The **shifted operator** $D_\alpha = D + M_\alpha$, with $D = i\sum_k e_k\partial_k$ ($D^2 = \Delta$) and $M_\alpha$ right multiplication by an arbitrary $\alpha\in\mathbb{B}$, is the theory that boundary-value problems use. Its integral operators $T_\alpha$, $K_\alpha$ and $S_\alpha$ obey the same four theorems as the unshifted theory — Borel–Pompeiu, Cauchy, Plemelj–Sokhotski, involutiveness — with formulas that branch according to whether $\alpha$ is a unit, a zero divisor with nonzero scalar part, or a zero divisor with vanishing scalar part, since the kernel inverts the symbol. Its sharpest statement is the boundary-value criterion: $f$ is the trace on $\Gamma$ of a solution of $D_\alpha g = 0$ if and only if $P_\alpha f = f$ on $\Gamma$, with $P_\alpha = \tfrac12(I+S_\alpha)$, and then $g = K_\alpha f$. The parameter may itself be singular, not only the variable: $\alpha = -(i\omega e_1+me_2)$ has $N(\alpha) = m^2-\omega^2$ and hence lies in the zero divisor set — as a nilpotent, $\alpha^2 = 0$ — exactly when $\omega^2 = m^2$. A **pure** parameter that is not a zero divisor splits into two that are: with $\gamma\in\mathbb{C}$ satisfying $\gamma^2 = \alpha^2$, the non-Hermitian root $u = \alpha/\gamma$ of $+1$ gives the complementary null idempotents $\beta_\pm = \tfrac12(1\pm u)$, and the halves $\alpha_\pm = \tfrac12(\alpha\pm\gamma) = \pm\gamma\beta_\pm$ satisfy $\alpha_++\alpha_- = \alpha$, $\alpha_+\alpha_- = 0$ and $N(\alpha_\pm) = 0$; the split is assembled by the identity $D_{\alpha_+}P_+ + D_{\alpha_-}P_- = D_\alpha$, with $P_\pm$ right multiplication by $\beta_\pm$, and it is the reason the degenerate branch of the three carries the applications.

Restricting to real quaternion-valued functions recovers Fueter's quaternionic analysis, where the analogous theory is complete because $\mathbb{H}$ is a division algebra, and the general framework is Clifford analysis on $\mathrm{Cl}_{1,3}^{+}$; the Fueter–Sce construction converts slice-regular data of one complex variable into monogenic functions of four real variables.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C} \otimes_{\mathbb{R}} \mathbb{H}$ | Biquaternion algebra, $\cong \mathrm{Cl}_{1,3}^{+}$ |
| $\tilde{Q} = Q_0 e_0 + \mathbf{Q}$ | Biquaternion variable; $\mathbf{Q} = Q_1 e_1 + Q_2 e_2 + Q_3 e_3$ |
| $\tilde{\nabla} = \sum_\mu e_\mu \partial_{Q_\mu}$ | Biquaternionic Cauchy–Riemann operator |
| $\tilde{\nabla}^{\natural} = e_0\partial_{Q_0} - \sum_k e_k\partial_{Q_k}$ | Quaternion conjugate operator; $(\tilde{\nabla}, \tilde{\nabla}^{\natural})$ mirrors $(\partial_{\bar A}, \partial_A)$ |
| $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural} = \tilde{\nabla}^{\natural}\tilde{\nabla}$ | Scalar d'Alembertian, the sum of the four second derivatives |
| $\tilde{F}$ left-regular (left-monogenic) | $\tilde{\nabla}\tilde{F} = 0$ on a domain $\Omega$ |
| $\tilde{F}$ anti-regular | $\tilde{\nabla}^{\natural}\tilde{F} = 0$ |
| $\tilde{G} = \tilde{Q}^{\natural}/\|\tilde{Q}\|_E^4$ | Cauchy kernel, fundamental solution of $\tilde{\nabla}$ |
| $N(\tilde{Q}) = \tilde{Q}\tilde{Q}^{\natural}$ | Biquaternion norm; the zero divisors are the nonzero elements with $N = 0$ |
| $\|\tilde{Q}\|_E$ | Euclidean norm on $\mathbb{B} \cong \mathbb{R}^8$ |
| $\mathcal{Z}$ | Zero divisor set, a complex cone of real dimension $6$ |
| $\mathbb{H}_{\mathbb{B}}$ | Real-quaternion subspace, a division ring; the domain of the integral theory |
| $D = i\sum_k e_k\partial_k$ | Spatial Moisil–Teodoresco operator; $D^2 = \Delta$ |
| $M_\alpha$ | Right multiplication by $\alpha\in\mathbb{B}$ |
| $D_\alpha = D + M_\alpha$ | Shifted operator; its solutions are the $\alpha$-hyperholomorphic functions |
| $T_\alpha$, $K_\alpha$, $S_\alpha$ | Teodorescu transform, Cauchy-type operator and operator of singular integration for $D_\alpha$ |
| $P_\alpha = \tfrac12(I + S_\alpha)$ | Boundary projector; the boundary-value criterion is $P_\alpha f = f$ on $\Gamma$ |
| $\gamma$, $u = \alpha/\gamma$ | Scalar with $\gamma^2 = \alpha^2$ for a pure $\alpha$, and the non-Hermitian root $u^2 = 1$, $u^{\natural} = -u$ |
| $\beta_\pm = \tfrac12(1\pm u)$ | Complementary null idempotents; $P_\pm = M_{\beta_\pm}$ are the projectors of the split |
| $\alpha_\pm = \tfrac12(\alpha\pm\gamma) = \pm\gamma\beta_\pm$ | The two zero-divisor halves of the parameter; $\alpha_++\alpha_- = \alpha$, $\alpha_+\alpha_- = 0$ |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853).
- William Kingdon Clifford, "Preliminary Sketch of Biquaternions", *Proceedings of the London Mathematical Society* (1873).
- R. Fueter, "Die Funktionentheorie der Differentialgleichungen $\Delta u = 0$ und $\Delta\Delta u = 0$ mit vier reellen Variablen", *Commentarii Mathematici Helvetici* **7** (1934–35) 307–330.
- A. Sudbery, "Quaternionic analysis", *Mathematical Proceedings of the Cambridge Philosophical Society* **85** (1979) 199–225.
- F. Brackx, R. Delanghe, and F. Sommen, *Clifford Analysis* (Pitman, London, 1982).
- R. Delanghe, F. Sommen, and V. Souček, *Clifford Algebra and Spinor-Valued Functions* (Kluwer, Dordrecht, 1992).
- G. Gentili, C. Stoppato, and D. C. Struppa, *Regular Functions of a Quaternionic Variable* (Springer, 2013).
- V. V. Kravchenko and M. V. Shapiro, *Integral Representations for Spatial Models of Mathematical Physics*, Pitman Research Notes in Mathematics 351 (Addison-Wesley Longman, 1996), for the Teodorescu transform, the Cauchy-type operator and the singular integral operator with a biquaternionic parameter, for the Borel–Pompeiu and Plemelj–Sokhotski formulas there, and for the boundary-value criterion $P_\alpha f = f$.
- V. V. Kravchenko, "Quaternion-Valued Integral Representations of the Harmonic Electromagnetic and Spinor Fields", *Doklady Mathematics* **51** (1995), no. 2, 287–289 (translated from *Doklady Akademii Nauk* **341** (1995), no. 5, 603–605), for the parametric class $D_\alpha = D + M_\alpha$ and its Cauchy-type theory, and for the split of a pure parameter into the two zero-divisor halves $\alpha_\pm = \tfrac12(\alpha\pm\gamma)$ assembled by the projectors $P_\pm$ — the algebra of the section *The Split of the Parameter*. The paper's own application, the harmonic electromagnetic and spinor fields, is in the physics register.
- V. V. Kravchenko and M. V. Shapiro, *Doklady Akademii Nauk* **329** (1993), no. 5, 547–549, the origin of the general parametric system and of its Borel–Pompeiu, Cauchy and Sokhotski theorems; the 1995 note of the preceding entry cites it as its reference $[1]$ and restates that system, and the shifted-operator theory above is its development.
- V. V. Kravchenko, "On a Biquaternionic Bag Model", *Zeitschrift für Analysis und ihre Anwendungen* **14** (1995), no. 1, 3–14, DOI 10.4171/ZAA/658, for an application of the shifted operator: the linear bag model reduced to the boundary equation $P_\alpha\tilde{p} = S^+\tilde{p}$, whose parameter $\alpha = -(i\omega e_1+me_2)$ is a pure zero divisor exactly on the mass shell.
