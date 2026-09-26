
# __Integrable Systems__

## Introduction

An integrable system is a differential equation that can be solved by linear means despite being nonlinear, and the instrument of the solution is a pair of linear operators whose commutator reproduces the equation. The discovery of Lax was that the Korteweg–de Vries equation, written $u_t - 6uu_x + u_{xxx} = 0$, is equivalent to the operator equation

$$
L_t = [A, L], \qquad L = -\partial_x^2 + u ,
$$

for a suitable third-order operator $A$. The operator $L$ is the Schrödinger operator with potential $u$, and the Lax equation says that $u$ evolves in such a way that the spectrum of $L$ is constant: the evolution is an **isospectral deformation**. The eigenvalues of $L$ are therefore integrals of the motion, and there are infinitely many of them, so the equation possesses infinitely many conserved quantities and is, in the appropriate infinite-dimensional sense, completely integrable.

The consequence is a solution method. Because the spectrum of $L$ is constant, the **scattering data** of $L$ evolve in time by a simple linear law — in the reflectionless case by a pure exponential — and the solution $u$ is recovered from the evolved data by solving a linear integral equation, the Gelfand–Levitan–Marchenko equation. This is the **inverse scattering transform**, and it is for these equations what the Fourier transform is for a linear constant-coefficient equation: a change of variables that linearises the flow. Its most conspicuous output is the soliton, a localised travelling wave that survives collision with other solitons unchanged in shape and speed, not covered here.

The article treats the theory in the following order: Lax pairs and isospectral deformation, with the KdV computation carried out and the zero-curvature form stated; the conservation laws of KdV and the recursion that generates them, together with the bi-Hamiltonian structure that organises them; the inverse scattering transform, in its direct and inverse halves and with the evolution of the scattering data; the soliton solutions obtained from reflectionless data; the finite-gap or algebro-geometric solutions, which are the periodic analogue and are built from Riemann surfaces and theta functions; and the integrability tests, the Painlevé test and the Hirota bilinear method. The boundary with the theory of dynamical systems is fixed as follows: the finite-dimensional reading of integrability — the Liouville–Arnold theorem, invariant tori, action-angle variables and the stability of the flow — belongs to the articles of this Part on smooth dynamical systems and on the geodesic flow, which are written in parallel, and the Hamiltonian and symplectic formulation in finite dimensions belongs to the article of this Part on Lagrangian and Hamiltonian systems. What is treated here is the partial-differential side: the operator pairs, the conservation laws and the transform.

## Lax Pairs and Isospectral Deformation

### The Lax Equation

**Definition.** Let $L$ and $A$ be linear operators on a function space, with $L$ formally self-adjoint and $A$ formally skew-adjoint. The **Lax pair** $(L,A)$ **represents** the evolution equation $u_t = F(u)$ if

$$
L_t = [A,L] := AL - LA ,
$$

where $L_t$ is the operator obtained by differentiating the coefficients of $L$ in time.

**Theorem (isospectrality).** Suppose $L(t) = -\partial_x^2 + u(\cdot,t)$ on $\mathbb{R}$ with $u$ decaying at infinity, suppose $A$ is skew-adjoint, and suppose $L_t = [A,L]$. Then the spectrum of $L(t)$ is independent of $t$. Moreover, if $\psi$ solves the eigenvalue equation $L\psi = \lambda\psi$ and evolves by $\psi_t = A\psi$, then $L\psi = \lambda\psi$ holds for all $t$ with $\lambda$ constant.

*Proof.* Differentiate the eigenvalue equation: $L_t\psi + L\psi_t = \lambda_t\psi + \lambda\psi_t$. Substituting $\psi_t=A\psi$ and $L_t = AL-LA$ gives $(AL-LA)\psi + LA\psi = \lambda_t\psi + \lambda A\psi$, and the left-hand side is $A(L\psi) = \lambda A\psi$ by the eigenvalue equation, so $\lambda_t\psi = 0$ and $\lambda$ is constant whenever $\psi\neq0$. The spectrum, being the set of such $\lambda$, is time-independent. $\square$

The theorem explains the name: the evolution moves $u$ along a trajectory in the space of potentials on which the spectrum is constant, and the eigenvalues are the integrals of motion. That the eigenvalues are infinitely many is what makes the equation solvable.

**Theorem (the KdV Lax pair).** For $L = -\partial_x^2+u$ and

$$
A = -4\partial_x^3 + 6u\,\partial_x + 3u_x ,
$$

the Lax equation $L_t = [A,L]$ is equivalent to the Korteweg–de Vries equation

$$
u_t - 6uu_x + u_{xxx} = 0 .
$$

*Proof.* By the direct computation of the commutator, treated as an operator on a test function $\psi$:

$$
[A,L]\psi = \bigl(6uu_x - u_{xxx}\bigr)\psi .
$$

Indeed, the third-order part contributes $-4[D^3,L]\psi = -4u_{xxx}\psi + \dots$ and the remaining terms contribute $6uu_x\psi$; all terms involving derivatives of $\psi$ cancel identically, so the commutator is multiplication by $6uu_x-u_{xxx}$. Since $L_t$ is multiplication by $u_t$, the Lax equation is exactly KdV in the stated convention. $\square$

The computation is the model of every Lax-pair verification, and the operator $A$ is skew-adjoint, as required by the general theorem. The notation $u_t - 6uu_x + u_{xxx}=0$ is fixed once and for all in this article; the equation written with the other sign of the nonlinearity is the same equation after the substitution $u\mapsto-u$.

### Zero Curvature and the AKNS Scheme

**Definition.** A **zero-curvature representation** of an evolution equation for a field $q(x,t)$ is a pair of matrix-valued functions $U(x,t;\lambda)$ and $V(x,t;\lambda)$, depending on a spectral parameter $\lambda$, such that

$$
U_t - V_x + [U,V] = 0
$$

is equivalent to the equation; the equation is the compatibility condition for the linear system $\psi_x = U\psi$, $\psi_t = V\psi$.

**Theorem (equivalence with a Lax pair).** A zero-curvature representation with $U$ depending on the field and $\lambda$ is equivalent, on the level of the linear problem, to a Lax pair; the operator $L$ is the spatial part of the system and $A$ is the time part, and the isospectrality of the Lax pair becomes the statement that the monodromy of $\psi_x = U\psi$ is conserved.

*Proof.* If the linear system is compatible, its solutions satisfy $\psi_{xt}=\psi_{tx}$, which is the zero-curvature equation, and the spectral parameter is a constant of the motion for the same reason that the eigenvalue is in the Lax formulation; conversely, a Lax pair can be rewritten as a zero-curvature pair by choosing a matrix realisation of the operator $L$ and taking $U$ and $V$ to be the matrices of the spatial and temporal parts. $\square$

**Example (the AKNS system).** With the matrices

$$
U = \begin{pmatrix}-ik & q\\ r & ik\end{pmatrix}, \qquad
V = \begin{pmatrix} C & D\\ E & -C\end{pmatrix},
$$

the entries of $V$ being polynomials in $k$ determined by the requirement that the zero-curvature equation hold identically in $k$, one obtains, for different choices of the polynomial degree and the reduction of $(q,r)$, the nonlinear Schrödinger equation $iq_t+q_{xx}\pm2|q|^2q=0$, the modified KdV equation, the sine-Gordon equation $u_{xt}=\sin u$ and KdV itself. This is the **AKNS scheme**, and it exhibits the integrable equations as the reductions of a single linear problem rather than as a list.

## Conservation Laws and the Hamiltonian Hierarchy

### The Conserved Densities of KdV

**Definition.** A **conservation law** for an evolution equation $u_t=F(u)$ is an identity $\rho_t = J_x$ valid on all solutions, with $\rho$ the **conserved density** and $J$ the **flux**; if $\rho$ and $J$ decay at infinity, then $\int\rho\,dx$ is a constant of the motion, and it is **nontrivial** if it is not a constant and not implied by a lower-order law.

**Theorem (the first conserved densities of KdV).** For $u_t - 6uu_x + u_{xxx}=0$, the following are conservation laws:

$$
\rho_1 = u, \qquad \rho_2 = u^2, \qquad \rho_3 = u^3 + \tfrac12u_x^2 ,
$$

with fluxes

$$
J_1 = 3u^2-u_{xx}, \qquad J_2 = 4u^3-2uu_{xx}+u_x^2 ,
$$

and correspondingly for the third; the constants $I_k = \int\rho_k\,dx$ are independent.

*Proof.* For the first, $\rho_{1,t} = u_t = 6uu_x-u_{xxx} = (3u^2-u_{xx})_x$, so $J_1 = 3u^2-u_{xx}$. For the second, $\rho_{2,t} = 2uu_t = 12u^2u_x-2uu_{xxx}$, while $J_{2,x} = 12u^2u_x-2u_xu_{xx}-2uu_{xxx}+2u_xu_{xx} = 12u^2u_x-2uu_{xxx}$ for the displayed $J_2$, so $\rho_{2,t}=J_{2,x}$. For the third, the functional $H = \int(u^3+\tfrac12u_x^2)dx$ is the Hamiltonian of the equation: its variational derivative is $\frac{\delta H}{\delta u} = 3u^2 - u_{xx}$, and KdV reads $u_t = \partial_x\frac{\delta H}{\delta u}$. Hence $\frac{dH}{dt} = \int\frac{\delta H}{\delta u}u_t\,dx = \int\frac{\delta H}{\delta u}\,\partial_x\frac{\delta H}{\delta u}\,dx = \frac12\int\partial_x\Bigl(\frac{\delta H}{\delta u}\Bigr)^2dx = 0$ on a solution decaying at infinity, and the identity $\rho_{3,t}=J_{3,x}$ holds with $J_3$ computed from the variational derivative. $\square$

**Theorem (the Lenard recursion and the infinite hierarchy).** Normalise the conserved functionals so that $I_1 = \tfrac12\int u^2$ and $I_2 = \int(u^3+\tfrac12u_x^2)$; then the sequence $I_1,I_2,\dots$ is generated by the **recursion operator**

$$
R = -\partial_x^2 + 4u + 2u_x\partial_x^{-1} ,
$$

in the sense that

$$
\partial_x\frac{\delta I_{k+1}}{\delta u} = R\,\partial_x\frac{\delta I_k}{\delta u} ;
$$

the densities $\rho_1,\rho_2,\rho_3$ of the preceding theorem are those of the sequence up to the constant normalisation, the invariant $\int u$ being the additional member outside the recursion; consequently KdV has infinitely many independent conserved quantities in involution.

*Proof.* Quoted as standard (the Lenard–Kruskal recursion). Each density is obtained from the previous one by solving the condition that a certain combination be a total derivative, and the recursion operator performs that solution at the level of the differential algebra generated by $u$ and its derivatives; in the normalisation fixed in the statement the recursion starts from the density $\frac12u^2$ and reproduces $u^3+\frac12u_x^2$ and its successors as the next members. $\square$

**Theorem (bi-Hamiltonian structure).** KdV is Hamiltonian with respect to two compatible Poisson structures,

$$
\mathcal{P}_1 = \partial_x, \qquad \mathcal{P}_2 = -\partial_x^3 + 4u\partial_x + 2u_x ,
$$

in the sense that $u_t = \mathcal{P}_1\frac{\delta H_2}{\delta u} = \mathcal{P}_2\frac{\delta H_1}{\delta u}$ for suitable functionals $H_1,H_2$, and the recursion operator is $R = \mathcal{P}_2\mathcal{P}_1^{-1}$. A vector field that is Hamiltonian for two compatible structures is **bi-Hamiltonian**, and the Magri theorem then produces an infinite sequence of conserved quantities in involution.

*Proof.* Quoted as standard (the Magri–Gel'fand–Dorfman theory). For KdV one checks that $\mathcal{P}_1\delta H_2/\delta u$ and $\mathcal{P}_2\delta H_1/\delta u$ both equal $6uu_x-u_{xxx}$, with $H_2 = \int(\frac12u_x^2+u^3)$ and $H_1 = \frac12\int u^2$; the compatibility of the two structures gives the recursion and the involution. $\square$

The bi-Hamiltonian structure is the reason the recursion works, and it is the infinite-dimensional counterpart of the finite-dimensional integrability that is treated with the dynamical systems of this Part: there the integrals in involution are produced by a symplectic structure plus a flow, here by a pair of compatible Poisson structures. The finite-dimensional theory — the Liouville–Arnold theorem, action-angle variables and the invariant tori — is the subject of the articles of this Part on smooth dynamical systems and on the geodesic flow, written in parallel, and is not repeated here.

## The Inverse Scattering Transform

### The Direct Problem

**Definition.** For the Schrödinger operator $L = -\partial_x^2+u$ with $u$ real and decaying at infinity, the **scattering problem** is the eigenvalue problem $L\psi = k^2\psi$. Its spectrum consists of the continuous part $[0,\infty)$ together with finitely many negative eigenvalues $-a_1^2 > -\kappa_1^2 > \dots > -\kappa_N^2$. The **Jost solutions** $\psi_\pm(x,k) = e^{\mp ikx} + o(1)$ as $x\to\pm\infty$ satisfy

$$
\psi_+(x,k) = a(k)\,\psi_-(x,k)^* + b(k)\,\psi_-(x,-k) ,
$$

and the **scattering data** are the reflection coefficient $r(k) = b(k)/a(k)$, the transmission coefficient $1/a(k)$, the bound-state eigenvalues $\lambda_n = -\kappa_n^2$ and the norming constants $c_n$.

**Theorem (properties of the scattering data).** For real $u \in L^1(\mathbb{R},(1+|x|)dx)$, the scattering data have the following properties: $a$ extends analytically to the upper half-plane with simple zeros at the bound states $i\kappa_n$; $|a(k)|^2 - |b(k)|^2 = 1$ for real $k$, so $|r|\le1$; $r(k) = \overline{r(-k)}$; and the bound-state data are real and positive.

*Proof.* Quoted as standard (the direct scattering theory). The analyticity comes from the Volterra integral equations for the Jost solutions and the exponential decay of the kernel; the identity $|a|^2-|b|^2=1$ is the Wronskian relation of the two Jost solutions, computed at $x=\pm\infty$; the symmetry is the reality of $u$. $\square$

### The Evolution of the Data and the Inverse Problem

**Theorem (the evolution of the scattering data).** If $u(\cdot,t)$ solves KdV in the convention fixed above, then the transmission coefficient $1/a$ is time-independent, the bound-state eigenvalues are constant, and

$$
b(k,t) = b(k,0)\,e^{8ik^3t}, \qquad c_n(t) = c_n(0)\,e^{4\kappa_n^3t};
$$

the evolution of the scattering data is linear and decoupled, which is the sense in which the transform linearises the equation.

*Proof.* Quoted as standard. The time evolution of the Jost solution is governed by the operator $A$ of the Lax pair, $\psi_t = A\psi$, and evaluating the asymptotics of $A\psi = -4\psi_{xxx}+6u\psi_x+3u_x\psi$ as $x\to\pm\infty$, where $u\to0$, gives $\psi_t \sim -4\psi_{xxx}$, that is, in terms of the asymptotic exponentials $\psi_\pm\sim e^{\mp ikx}$, the factor $\mp4(-ik)^3 = \pm4ik^3$; comparing the two asymptotic representations of the solution then gives the stated factors, since $a$ multiplies the outgoing term and $b$ the incoming one. $\square$

**Theorem (the inverse problem).** The potential $u$ is recovered from the scattering data by the **Gelfand–Levitan–Marchenko** integral equation

$$
K(x,y) + B(x+y) + \int_x^\infty K(x,z)\,B(z+y)\,dz = 0 \qquad (y > x),
$$

where the kernel is $B(\xi) = \sum_{n=1}^N c_n^2e^{-\kappa_n\xi} + \frac{1}{2\pi}\int_{\mathbb{R}}r(k)e^{ik\xi}dk$, and then

$$
u(x) = -2\,\frac{d}{dx}K(x,x).
$$

The map $u \mapsto (\text{scattering data}) \mapsto u$ is a bijection between the class of decaying real potentials and the class of admissible data, and it intertwines the KdV flow with the linear evolution of the theorem above.

*Proof.* Quoted as standard (the inverse scattering transform). The kernel $K$ is the transformation kernel relating the Jost solutions of $L=-\partial_x^2+u$ to those of the free operator $-\partial_x^2$; the equation for $K$ is obtained by requiring the transformed solutions to have the correct asymptotics, and the formula for $u$ is the statement that the transformation of $-\partial_x^2$ differs from $-\partial_x^2$ by multiplication by $-2K(x,x)'$. $\square$

**Corollary (solution of the Cauchy problem).** For $u_0$ real and rapidly decaying, the solution of KdV with $u(\cdot,0)=u_0$ is obtained by computing the scattering data of $u_0$, evolving them by the exponential factors above, solving the Gelfand–Levitan–Marchenko equation for the evolved data, and reading off $u(x,t) = -2\partial_xK(x,x;t)$.

The scheme is the exact analogue for KdV of the Fourier solution of a constant-coefficient linear equation: the direct transform computes the data, the data evolve linearly, the inverse transform returns the solution. The difference is that the transform is nonlinear, and the superposition of two solutions is not a solution; the solitons instead pass through one another with a phase shift, which the nonlinearity of the inverse problem records.

## Solitons and Reflectionless Potentials

**Definition.** A potential $u$ is **reflectionless** if $r(k)\equiv0$; its scattering data consist only of the bound states and the norming constants, and the Gelfand–Levitan–Marchenko kernel is then a finite exponential sum, so the equation is solved by linear algebra.

**Theorem (the one-soliton solution).** For the reflectionless potential with a single bound state $\lambda = -\kappa^2$, the evolution of the data gives

$$
u(x,t) = -2\kappa^2\operatorname{sech}^2\bigl(\kappa(x-4\kappa^2t-x_0)\bigr),
$$

a negative localised travelling wave moving to the right with speed $4\kappa^2$; it is the unique reflectionless solution with one bound state.

*Proof.* With $N=1$, the kernel is $B(\xi) = c_1^2e^{-\kappa\xi}$ with $c_1^2 = 2\kappa e^{2\kappa x_0}$ at $t=0$, and the Marchenko equation is solved by an exponential; the formula for $u$ is then a direct differentiation. The time dependence comes from the factor $c_1(t)^2e^{-\kappa\xi}$, and the resulting wave depends on $x,t$ only through the combination $x-4\kappa^2t$, which is the travelling-wave ansatz. $\square$

**Theorem (N-soliton solutions and elastic collision).** For reflectionless data with $N$ bound states the solution is an $N$-soliton

$$
u(x,t) = -2\partial_x^2\log\det\bigl(I + C(x,t)\bigr),
$$

where $C$ is the $N\times N$ matrix with entries $C_{mn} = \frac{c_m(t)^2}{\kappa_m+\kappa_n}e^{-(\kappa_m+\kappa_n)x}$; as $t\to\pm\infty$ it is asymptotic to $N$ well-separated one-solitons with the same speeds and amplitudes, the only effect of the collision being a phase shift in each. The collision is therefore **elastic**, and this is what distinguishes the solitons of an integrable equation from the dissipative pulses of a general one.

*Proof.* Quoted as standard. The $N$-soliton formula is the determinant solution of the Marchenko equation with a degenerate kernel, obtained by Cramer's rule; the asymptotic analysis of the determinant as $t\to\pm\infty$ shows that the off-diagonal factors become negligible in the two limits and identifies the phase shifts from the diagonal entries. $\square$

**Example (the two-soliton).** For $N=2$ with $\kappa_1>\kappa_2>0$ the taller and faster soliton overtakes the shorter and slower one; after the passage the two waves are unchanged in shape and speed, and each has acquired a positive phase shift proportional to $\log\frac{(\kappa_1+\kappa_2)^2}{(\kappa_1-\kappa_2)^2}$, which diverges as $\kappa_1\to\kappa_2$ and is finite otherwise. The example is the cleanest illustration of the elastic collision and of the nonlinear superposition that replaces linear addition.

## Finite-Gap Solutions and Integrability Tests

**Definition.** A **finite-gap** or **algebro-geometric** solution of KdV is a solution whose associated Schrödinger operator has spectrum equal to a finite union of intervals, $[0,\infty)$ together with finitely many bands; the solution is then periodic or quasi-periodic and is expressed by theta functions on a hyperelliptic Riemann surface.

**Theorem (Its–Matveev, Dubrovin–Novikov).** The finite-gap solutions of KdV are exactly the solutions for which the spectrum of $L=-\partial_x^2+u$ is a finite union of bands; they are given by the **Its–Matveev formula**

$$
u(x,t) = -2\sum_{j=1}^{g}\lambda_j + 2\partial_x^2\log\Theta\bigl(\mathbf{U}x + \mathbf{V}t + \mathbf{d}\bigr) ,
$$

where $\Theta$ is the Riemann theta function of the hyperelliptic curve $\mu^2 = \prod_{j=1}^{2g+1}(\lambda-\lambda_j)$, the vectors $\mathbf{U},\mathbf{V}$ are the periods of two Abelian differentials and $\mathbf{d}$ is a constant; the solution is quasi-periodic in $x$ and $t$ with $g$ independent frequencies.

*Proof.* Quoted as standard. The Baker–Akhiezer function on the curve satisfies a linear problem whose compatibility is the KdV equation, exactly as in the zero-curvature formulation, and Riemann's theta-function solution of the inversion problem expresses the divisor of the Baker–Akhiezer function in terms of theta functions; the formula for $u$ follows from the pole behaviour of the Baker–Akhiezer function at infinity. $\square$

**Remark (the role of the Riemann surface).** The finite-gap construction turns the integrable equation into a problem in the geometry of a compact Riemann surface: the flow of KdV is the straight-line motion of the divisor of the Baker–Akhiezer function on the Jacobian of the curve, and the quasi-periodicity is the projection of a linear flow on a torus. The soliton is the degenerate case $g=1$ in which the curve is singular and the theta function degenerates to a hyperbolic function; the reflectionless $N$-soliton is the limit in which all the bands but finitely many collapse to points.

**Definition.** The **Painlevé test** for an evolution equation requires that every solution of the equation, continued around a movable singularity in the complex time plane, be single-valued: the solution must have the form $(t-t_0)^{\alpha}$ times an analytic function of $(t-t_0)$, with $\alpha$ rational and the expansion free of movable branch points. An equation passing the test is **of Painlevé type**, and for integrable equations the test is expected to succeed.

**Theorem (Weiss–Tabor–Carnevale).** The KdV equation passes the Painlevé test; the expansion of a solution about a movable singular manifold $\phi(x,t)=x-x_0(t)$ takes the form $u = -2\partial_x^2\log\phi + u_0 + u_1\phi + \dots$, with the recursion for the coefficients obstructed only at the resonances, and the obstruction conditions are satisfied identically.

*Proof.* Quoted as standard. The leading behaviour is computed from the dominant balance $u_t\sim uu_x\sim u_{xxx}$, which gives $u\sim -2/\phi_x^2\cdot\phi_{xx}$ up to the transformation to a singular manifold; the resonances of the recursion are at $-1, 4, 6$ for KdV, and the two nontrivial resonance conditions are verified by using the KdV equation itself. $\square$

**Remark (the Hirota form).** The substitution $u = -2\partial_x^2\log\tau$ with $\tau$ a **tau function** converts KdV into the bilinear equation $D_x(D_t + D_x^3)\tau\cdot\tau = 0$, where $D$ denotes the Hirota bilinear derivative

$$
D_x^mD_t^n\,f\cdot g = \partial_{x'}^m\partial_{t'}^nf(x+x',t+t')g(x-x',t-t')\bigr|_{x'=t'=0} .
$$

The $N$-soliton and the finite-gap solutions are then obtained from a tau function that is a finite determinant or a theta function, and the bilinear method gives the cleanest route to the explicit formulas and to the Lax pair itself.

## Summary

An integrable system is a nonlinear evolution equation that is equivalent to the compatibility condition of a pair of linear operators. For KdV, $L_t=[A,L]$ with $L=-\partial_x^2+u$ and $A=-4\partial_x^3+6u\partial_x+3u_x$ is equivalent to $u_t-6uu_x+u_{xxx}=0$, and the Lax equation expresses the isospectrality of the Schrödinger operator: the eigenvalues of $L$ are constants of the motion, and the eigenfunctions evolve by $\psi_t=A\psi$. The zero-curvature formulation $U_t-V_x+[U,V]=0$ is the matrix form of the same idea, and the AKNS scheme obtains KdV, the nonlinear Schrödinger equation, modified KdV and the sine-Gordon equation as reductions of one linear problem.

KdV has infinitely many conservation laws, generated by the Lenard recursion with recursion operator $R=-\partial_x^2+4u+2u_x\partial_x^{-1}$, whose first members are $u$, $u^2$ and $u^3+\frac12u_x^2$; the density $u^3+\frac12u_x^2$ is the energy, and the equation is bi-Hamiltonian with respect to the compatible structures $\partial_x$ and $-\partial_x^3+4u\partial_x+2u_x$, which is what produces the infinite family by the Magri theorem. The inverse scattering transform computes the scattering data of $L$ — reflection and transmission coefficients, bound states and norming constants — of which the transmission coefficient and the eigenvalues are time-independent while the reflection data evolve by $e^{8ik^3t}$; the potential is recovered by the Gelfand–Levitan–Marchenko equation and the formula $u=-2\partial_xK(x,x)$. Reflectionless data give the reflectionless potentials, among them the one-soliton $u=-2\kappa^2\operatorname{sech}^2(\kappa(x-4\kappa^2t-x_0))$ and the $N$-soliton determinant formula; the collision of solitons is elastic with a phase shift. The periodic analogue is the finite-gap solution, built from a hyperelliptic Riemann surface and a Riemann theta function by the Its–Matveev formula, and the integrability tests are the Painlevé test and the Hirota bilinear form, in which KdV becomes $D_x(D_t+D_x^3)\tau\cdot\tau=0$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $u(x,t)$ | Field of the integrable equation |
| $L$, $A$ | Lax pair; $L$ self-adjoint, $A$ skew-adjoint |
| $L_t = [A,L]$ | Lax equation, the isospectral deformation |
| $U$, $V$, $\lambda$ | Zero-curvature pair and spectral parameter |
| KdV | $u_t - 6uu_x + u_{xxx} = 0$ |
| $\rho$, $J$ | Conserved density and flux; $I_k = \int\rho_k$ |
| $R$ | Recursion (Lenard) operator $-\partial_x^2+4u+2u_x\partial_x^{-1}$ |
| $\mathcal{P}_1$, $\mathcal{P}_2$ | Compatible Hamiltonian (Poisson) structures |
| $H$, $H_1$, $H_2$ | Hamiltonian functionals, $\delta H/\delta u$ the variational derivative |
| $\psi_\pm$, $a$, $b$, $r$ | Jost solutions, transmission and reflection data |
| $\kappa_n$, $c_n$ | Bound-state wavenumbers and norming constants |
| $K(x,y)$, $B$ | Gelfand–Levitan–Marchenko kernel and its data |
| $\kappa$, $x_0$ | Soliton parameter and centre |
| $\Theta$, $\lambda_j$ | Riemann theta function and band edges; $g$ the genus |
| $D_x,D_t$, $\tau$ | Hirota bilinear derivatives and the tau function |
| AKNS | The matrix scheme generating the integrable hierarchy |



## Further Reading

- Peter D. Lax, "Integrals of Nonlinear Equations of Evolution and Solitary Waves", *Communications on Pure and Applied Mathematics* 21 (1968), for the Lax pair and isospectral deformation.
- Mark J. Ablowitz and Harvey Segur, *Solitons and the Inverse Scattering Transform* (SIAM, 1981), for the inverse scattering method and the AKNS scheme.
- Philip G. Drazin and Robin S. Johnson, *Solitons: An Introduction* (Cambridge University Press, 1989), for the KdV computations, the conservation laws and the soliton solutions.
- Clifford S. Gardner, John M. Greene, Martin D. Kruskal and Robert M. Miura, "Method for Solving the Korteweg–de Vries Equation", *Physical Review Letters* 19 (1967), for the original inverse scattering solution.
- Israel M. Gel'fand and Boris M. Levitan, "On the Determination of a Differential Equation from Its Spectral Function", *American Mathematical Society Translations* 1 (1955), for the inverse problem.
- Franco Magri, "A Simple Model of the Integrable Hamiltonian Equation", *Journal of Mathematical Physics* 19 (1978), for the bi-Hamiltonian structure and the recursion operator.
- Boris A. Dubrovin, "Theta Functions and Non-Linear Equations", *Russian Mathematical Surveys* 36 (1981), for the finite-gap solutions and the theta-function construction.
- Alexander R. Its and Victor B. Matveev, "Schrödinger Operators with Finite-Gap Spectrum and N-Soliton Solutions of the Korteweg–de Vries Equation", *Theoretical and Mathematical Physics* 23 (1975), for the Its–Matveev formula.
- John Weiss, Morris Tabor and George Carnevale, "The Painlevé Property for Partial Differential Equations", *Journal of Mathematical Physics* 24 (1983), for the Painlevé test.
- Ryogo Hirota, *The Direct Method in Soliton Theory* (Cambridge University Press, 2004), for the bilinear method and the tau function.
