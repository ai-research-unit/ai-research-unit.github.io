
# __The Hamilton–Jacobi Equation and Separability__

## Introduction

The Hamilton–Jacobi equation is a single first-order partial differential equation for one scalar function $S$ of the configuration variables and the time, and it is the form the mechanical equations take when the momenta are eliminated in favour of the gradients of that scalar. Its importance is that a **complete integral** — a solution carrying one independent constant per degree of freedom — generates, through the elementary relations $p_i=\partial S/\partial q^i$, a canonical transformation that carries the Hamiltonian to zero. The new coordinates are then constants, and the motion is recovered by inverting a family of algebraic relations. The equation is therefore a device for integration rather than a new law of motion: to solve it is to solve the system, and a single complete integral supplies the whole family of trajectories, one constant of integration being traded for each quadrature.

Two functions of the equation are distinguished from the outset. The **principal function** $S(q,\alpha,t)$ depends on the time, and it is the action of the calculus of variations read as a function of the endpoint. When the Hamiltonian does not depend on the time the time variable separates first and the equation reduces to the **characteristic function** $W(q,\alpha)$, which carries the energy as one of its constants and is otherwise independent of the time. Both are complete integrals in the sense above, and both turn the problem into ordinary integrations.

The method is decisive when the equation **separates**, that is, when coordinates exist in which the characteristic function is a sum of functions of one coordinate each. Every term of the sum then satisfies an ordinary differential equation, and every such equation yields a constant of the motion. The classical content of the theory is the description of the separable cases: the **Stäckel conditions**, which say which potentials separate in a given orthogonal coordinate system, and the finite classical list of orthogonal coordinate systems of three-dimensional Euclidean space in which the equation of a free particle separates. The worked examples — the oscillator, the central force and the Kepler problem, and the spherical, parabolic and elliptic coordinates — are the classical solved problems of mechanics, and the parabolic and the elliptic cases are the two that separate the Coulomb problem in a uniform field and the two-centre problem.

The setting is that of the two Hamiltonian articles of this Part. The Hamilton–Jacobi equation and the variational provenance of the principal function belong to *The Calculus of Variations*, and its Hamiltonian reformulation — the four generating functions $F_1,\dots,F_4$, the time-dependent shift $K=H+\partial F/\partial t$, the Poisson bracket and the symplectic form — belongs to *Lagrangian and Hamiltonian Systems*; both are used here and not re-derived. The companion article also owns the Liouville–Arnold theorem and the action-angle variables, to which the separable case is tied, and *Partial Differential Equations* owns the general first-order equation and its characteristics. This article owns the **method**: the complete integral, the separation of variables, the Stäckel conditions, the separable coordinate systems and the classical examples. The quantum-mechanical and optical readings of the equation, and the Hamilton–Jacobi–Bellman equation of optimal control, are not developed here.

## The Hamilton–Jacobi Equation

### From the Generating Function to the Equation

**Definition.** Let $H(q,p,t)$ be a Hamiltonian on the cotangent bundle of a configuration space $Q$ of dimension $f$. The **Hamilton–Jacobi equation** for a function $S(q,t)$ is

$$
\frac{\partial S}{\partial t} + H\Bigl(q,\frac{\partial S}{\partial q},t\Bigr) = 0 .
$$

The equation is a single first-order scalar partial differential equation in the $f+1$ variables $q^1,\dots,q^f,t$, nonlinear in the gradient $\partial S/\partial q$ exactly as $H$ is nonlinear in $p$; its characteristic equations are Hamilton's equations, so the integration of the equation and the integration of the flow are the same problem seen from two sides.

**Theorem (the equation as a vanishing Hamiltonian).** Let $S(q,P,t)$ be a generating function of the second type, so that the transformation $(q,p)\mapsto(Q,P)$ is defined by

$$
p_i=\frac{\partial S}{\partial q^i}, \qquad Q^i=\frac{\partial S}{\partial P_i},
$$

and has new Hamiltonian $K=H+\partial S/\partial t$. Then $S$ satisfies the Hamilton–Jacobi equation with $\partial S/\partial q$ in the place of $p$ if and only if the new Hamiltonian vanishes, $K=0$.

*Proof.* Substituting $p_i=\partial S/\partial q^i$ in $K=H+\partial S/\partial t$ gives $K=H(q,\partial S/\partial q,t)+\partial S/\partial t$, which is zero exactly when $S$ satisfies the equation; and $K=0$ is the condition that the new coordinates $Q^i,P_i$ be constant along the flow, since Hamilton's equations in the new variables read $\dot Q^i=\partial K/\partial P_i=0$ and $\dot P_i=-\partial K/\partial Q^i=0$. ∎

The theorem is the whole reason for the equation: it turns the search for constants of the motion into the search for a generating function that makes the Hamiltonian vanish, and the four generating functions of the companion article give four equivalent formulations, of which the second type above is the one conventionally used. It also explains why the equation, whose solutions are generating functions, is the "partial differential equation of mechanics": the ordinary differential equations of the flow are its characteristics.

**Remark (the principal function).** The action of the calculus of variations, read as a function of the endpoint and of the initial data, satisfies the Hamilton–Jacobi equation, and its gradient is the momentum, $p_i=\partial S/\partial q^i$. This is Jacobi's reading of the equation: the principal function is the generating function of the transformation to the constants, so the equation is not a new object but the action regarded as a function of the endpoint. The proof is the envelope argument of *The Calculus of Variations*: differentiating the action with respect to the endpoint moves the boundary and, by the vanishing of the first variation, produces the momentum and the equation. The additive constant of $S$ is immaterial, because only its derivatives enter.

### The Characteristic Function

When $H$ does not depend on the time, one constant of the equation may be taken for the time.

**Theorem (separation of the time).** Let $H$ be autonomous. Then the Hamilton–Jacobi equation has a complete integral of the form

$$
S(q,\alpha,t) = W(q,\alpha) - \alpha_1 t ,
$$

where $\alpha_1$ is one of the constants of $S$, if and only if $W$ satisfies the **reduced Hamilton–Jacobi equation**

$$
H\Bigl(q,\frac{\partial W}{\partial q}\Bigr) = \alpha_1 .
$$

The constant $\alpha_1$ is the value of the Hamiltonian, so along a solution it is the energy, and $W$ is **Hamilton's characteristic function**, also called the abbreviated action.

*Proof.* Substituting $S=W-\alpha_1t$ gives $\partial S/\partial t=-\alpha_1$ and $\partial S/\partial q=\partial W/\partial q$, so the equation becomes $-\alpha_1+H(q,\partial W/\partial q)=0$. Conversely any solution with $\partial_t S$ a constant gives the form, and the constant is $\pm$ the value of $H$, which the equation forces to be the energy. ∎

The characteristic function is the quantity that separates: it is a function of the coordinates alone, one of its constants is the energy, and the remaining $f-1$ constants are the further constants of the complete integral — the separation constants, when the equation separates in the coordinates at hand. For a system with $f$ degrees of freedom the reduced equation is a first-order partial differential equation in $f$ variables, and a complete integral of it depends on $f$ constants $\alpha_1,\dots,\alpha_f$.

### The Complete Integral and the Solution by Quadrature

**Definition.** A $C^2$ solution $S(q,\alpha,t)$ of the Hamilton–Jacobi equation depending on $f$ independent constants $\alpha=(\alpha_1,\dots,\alpha_f)$ is a **complete integral** if the Hessian matrix of mixed derivatives is nonsingular,

$$
\det\Bigl(\frac{\partial^2 S}{\partial q^i\,\partial\alpha_j}\Bigr)\neq0
$$

on the domain considered.

**Theorem (Jacobi).** Let $S(q,\alpha,t)$ be a complete integral of the Hamilton–Jacobi equation. Then the general solution of Hamilton's equations is obtained as follows. Put

$$
\beta_i = \frac{\partial S}{\partial\alpha_i}(q,\alpha,t), \qquad i=1,\dots,f ,
$$

solve these $f$ relations for the $f$ coordinates $q=q(\alpha,\beta,t)$, and set $p_i=\partial S/\partial q^i$ at that point. Then $(q(t),p(t))$ is a solution of Hamilton's equations for every choice of the $2f$ constants $\alpha,\beta$, and every solution arises in this way.

*Proof.* The map $(q,p)\mapsto(\alpha,\beta)$ given by $p_i=\partial S/\partial q^i$ and $\beta_i=\partial S/\partial\alpha_i$ is the canonical transformation generated by $S$, with the constants $\alpha$ in the role of the new momenta; its new Hamiltonian is $K=H+\partial S/\partial t=0$ by the equation. In the new variables Hamilton's equations are $\dot\alpha_i=-\partial K/\partial\beta_i=0$ and $\dot\beta_i=\partial K/\partial\alpha_i=0$, so $\alpha$ and $\beta$ are constant along the flow. The nonsingularity of $\partial^2S/\partial q\,\partial\alpha$ is the inverse-function hypothesis that lets the relations $\beta=\partial S/\partial\alpha$ be solved for $q$; substituting in $p=\partial S/\partial q$ gives the momenta. ∎

The inverse-function condition is exactly the nondegeneracy of the generating function of the companion article, and it is why the constants must be **independent**: if the mixed Hessian vanished, the relations $\beta=\partial S/\partial\alpha$ would not determine the coordinates. The theorem is the precise sense in which the Hamilton–Jacobi method solves a system: the $2f$ arbitrary constants of the general solution of Hamilton's equations are the $\alpha_i$ and the $\beta_i$, and the coordinates are found by inverting $\beta=\partial S/\partial\alpha$ rather than by integrating further.

**Example (the oscillator by quadrature).** For $H=\frac{1}{2m}(p^2+m^2\omega^2q^2)$, the characteristic function is

$$
W(q,\alpha_1)=\int^{q}\sqrt{2m\alpha_1-m^2\omega^2s^2}\,ds ,
$$

so that $p=W_q=\sqrt{2m\alpha_1-m^2\omega^2q^2}$; the constant $\alpha_1$ is the energy, and the quadrature $\partial W/\partial\alpha_1=\beta_1$ is

$$
\frac{1}{\omega}\arcsin\frac{q\omega}{\sqrt{2\alpha_1/m}}=t+\beta_1 ,
$$

equivalently $q(t)=q_{\max}\sin\omega(t+\beta_1)$ with $q_{\max}=\sqrt{2\alpha_1}/(\omega\sqrt m)$, and $p(t)=\sqrt{2m\alpha_1}\cos\omega(t+\beta_1)$. The energy is $\alpha_1$ on every solution, and the two constants $\alpha_1,\beta_1$ are the amplitude and the phase. The computation is the model of the method: one quadrature of $W$, one inversion of $\partial W/\partial\alpha_1$.

## Separability

### Additive Separation and the Separation Constants

**Definition.** The Hamilton–Jacobi equation **separates additively** in the coordinates $q^1,\dots,q^f$ if it has a complete integral of the form

$$
W(q,\alpha) = \sum_{i=1}^f W_i(q^i,\alpha) ,
$$

a sum of terms each depending on a single coordinate, the constants $\alpha_i$ being the separation constants (one of which is the energy). The separated solution of the full equation is then $S=\sum_iW_i(q^i,\alpha)-\alpha_1 t$.

**Theorem (the criterion of separation).** Suppose that in the Hamiltonian one coordinate $q^k$ and its conjugate gradient $\partial W/\partial q^k$ occur only through a single function,

$$
H = H\Bigl(q^1,\dots,\widehat{q^k},\dots,q^f;\, \frac{\partial W}{\partial q^1},\dots,\widehat{\frac{\partial W}{\partial q^k}},\dots,\frac{\partial W}{\partial q^f};\, \psi\Bigl(q^k,\frac{\partial W}{\partial q^k}\Bigr)\Bigr),
$$

the hat marking a missing entry. Then the equation separates in $q^k$, and $\psi=\Gamma_k$ is a constant.

*Proof.* Write the reduced equation as $H(\dots,\psi,\dots)=\alpha_1$. Differentiate with respect to $q^k$ at fixed values of the other coordinates and of the other gradients. The left side becomes $\partial H/\partial\psi\cdot d\psi/dq^k$, because $q^k$ occurs only through $\psi$; the right side is zero because $\alpha_1$ is constant and the other arguments are held fixed. Hence $\partial H/\partial\psi\cdot d\psi/dq^k=0$. Where $\partial H/\partial\psi\neq0$, which is the nondegenerate case, this gives $d\psi/dq^k=0$: the function $\psi$ is a constant $\Gamma_k$. ∎

The criterion is local and mechanical: a coordinate that enters only through one combination of itself and its own gradient can be separated off, and the value of that combination is a constant of the motion. A **cyclic** coordinate is the extreme instance, since then $q^k$ does not occur at all, $\psi=\partial W/\partial q^k=p_k$, and the separation constant $\Gamma_k=p_k$ is the conserved conjugate momentum of the companion article. Separation and symmetry therefore meet at the cyclic coordinate: the conserved momentum of a symmetry is the simplest separation constant.

**Remark (the dependence on the coordinates).** Whether the equation separates is a property of the pair consisting of the Hamiltonian and the coordinate system, not of the Hamiltonian alone. The same potential may separate in one system and not in another: the free particle separates in the coordinate systems of the classical list below but not in a general orthogonal system, the Coulomb potential separates both in spherical and in parabolic coordinates while a general central potential separates only in the spherical ones, and the uniform field, which does not separate in spherical coordinates, separates in parabolic ones. The choice of coordinates is therefore part of the method, and the classification of the favourable choices is the content of the next two subsections.

### The Stäckel Conditions

The systematic criterion for a Hamiltonian quadratic in the momenta is due to Stäckel.

**Theorem (Stäckel conditions).** Let $q^1,\dots,q^f$ be orthogonal coordinates in Euclidean space with scale factors $h_i$, so that the Hamiltonian of a particle of mass $m$ in a potential $U$ is

$$
H = \frac{1}{2m}\sum_{i=1}^f\frac{p_i^2}{h_i^2} + U(q) ,
$$

and consider the reduced Hamilton–Jacobi equation

$$
\frac{1}{2m}\sum_{i=1}^f\frac{1}{h_i^2}\Bigl(\frac{\partial W}{\partial q^i}\Bigr)^2 + U = \alpha_1 .
$$

If the potential admits the representation

$$
U(q) = \sum_{i=1}^f \frac{1}{h_i^2}\,U_i(q^i)
$$

with $U_i$ a function of the single coordinate $q^i$, and if the factors $1/h_i^2$ are nested as in the classical orthogonal systems, then the equation separates additively: clearing the denominators from the innermost coordinate outwards produces, at each step, an equation in a single coordinate whose constant parametrises the next. Conversely, among the classical separable systems, the condition is also necessary.

*Proof (three-dimensional Euclidean case).* Write $A_i=\frac{1}{2m}(\partial W_i/\partial q^i)^2+U_i$ for the bracket of the coordinate $q^i$, so that the reduced equation in spherical coordinates reads $A_r+A_\theta/r^2+A_\phi/(r^2\sin^2\theta)=\alpha_1$. Multiplication by $r^2$ gives

$$
r^2(A_r-\alpha_1) + A_\theta + \frac{A_\phi}{\sin^2\theta} = 0 ,
$$

in which the first group depends on $r$ alone and the second on $\theta,\phi$ alone; being equal and opposite, both are constant, say $A_\theta+A_\phi/\sin^2\theta=\Gamma_\theta$, whence the radial equation $A_r+\Gamma_\theta/r^2=\alpha_1$. Multiplication of that constant equation by $\sin^2\theta$ gives

$$
\sin^2\theta\,(A_\theta-\Gamma_\theta) + A_\phi = 0 ,
$$

and the same argument separates $\phi$: the term $A_\phi$ is a function of $\phi$ alone and $\sin^2\theta(A_\theta-\Gamma_\theta)$ a function of $\theta$ alone, so both are constant, $A_\phi=\Gamma_\phi$ and $A_\theta+\Gamma_\phi/\sin^2\theta=\Gamma_\theta$. Three equations in one coordinate each have been obtained, with the separation constants $\Gamma_\phi,\Gamma_\theta$ and the energy $\alpha_1$. The general $f$-dimensional case is the same clearing of denominators, performed from the innermost factor outwards; the hypothesis on the potential is exactly what makes the one-coordinate groups appear at each step. ∎

The content of the theorem is that the **same** coordinate-dependent factor multiplies the potential term and the momentum term of each coordinate, so the factor can be cleared and the coordinate isolated. For the free Hamiltonian of three-dimensional Euclidean space in spherical coordinates,
$$
H = \frac{1}{2m}\Bigl(p_r^2+\frac{p_\theta^2}{r^2}+\frac{p_\phi^2}{r^2\sin^2\theta}\Bigr) + U ,
$$
the factors are $1$, $1/r^2$ and $1/(r^2\sin^2\theta)$, so the Stäckel form of the potential is
$$
U(r,\theta,\phi) = U_r(r) + \frac{U_\theta(\theta)}{r^2} + \frac{U_\phi(\phi)}{r^2\sin^2\theta} .
$$
This is the precise sense in which separation is a match between the potential and the metric: the potential must reproduce the nesting of the scale factors. A general potential, such as the uniform field $U=Fz=Fr\cos\theta$, does not have the form, and indeed does not separate in spherical coordinates — it separates in the parabolic coordinates of the examples below.

**Remark (the Stäckel matrix).** On a curved configuration space the metric factor $1/h_i^2$ is replaced by the contravariant metric coefficient $g^{ii}$ of the orthogonal coordinates, and the conditions above become the existence of an invertible matrix $\Phi$ whose $j$-th column depends on the coordinate $q^j$ alone — the **Stäckel matrix** — in terms of which the metric and the potential are expressed by one and the same linear system. The potentials satisfying it form the **Stäckel class**, and the separation constants are the coordinates of the potential in the basis of solutions of that system. The matrix formulation is quoted here as standard; the theorem above is its constant-curvature, orthogonal instance, which is the one used in the examples.

**Remark (the separable systems of Euclidean space).** The coordinate systems in which the free Hamilton–Jacobi equation separates are finite in number. In three-dimensional Euclidean space they are the classical list enumerated by Stäckel and Eisenhart — the Cartesian, cylindrical, spherical, parabolic-cylindrical, elliptic-cylindrical, rotational-parabolic, paraboloidal, prolate-spheroidal, oblate-spheroidal, confocal-ellipsoidal and conical systems — commonly quoted as eleven, with the degenerate limits of these systems counted separately by some authors; in the plane the list is shorter, the Cartesian, polar and elliptic-cylindrical systems being the standard ones. A potential separates in a given system exactly when it belongs to the Stäckel class of that system, so the enumeration of the coordinate systems is also the enumeration of the separable potentials up to the Stäckel construction. The list is quoted as standard; its derivation is the classification of the Stäckel matrices.

### Separation and Integrability

**Remark (separation implies integrability).** A separable system is completely integrable in the sense of the Liouville–Arnold theorem of the companion article. The $f$ separation constants $\alpha_1,\dots,\alpha_f$ are $f$ independent functions on phase space, the energy among them, and they are in involution: the existence of the separated complete integral $W=\sum_iW_i(q^i,\alpha)$ exhibits the transformation to the variables in which the motion is a translation on a torus. The actions of the companion article are the closed integrals of the separated momenta,

$$
I_i = \frac{1}{2\pi}\oint p_i\,dq^i = \frac{1}{2\pi}\oint \frac{\partial W_i}{\partial q^i}\,dq^i ,
$$

and each is a function of the separation constants alone, so the Hamilton–Jacobi transformation to the constants is, in the compact case, the transformation to the action-angle coordinates in which $H$ depends on the actions only. The oscillator is the simplest instance: its action is $\alpha_1/\omega$, the energy divided by the frequency.

**Remark (the converse fails).** Integrability does not imply separation in a given coordinate system, and a completely integrable system can fail to separate in the coordinates suggested by its definition. Separation is a sufficient condition for integrability, not a necessary one: it is a statement about a coordinate system and a Stäckel construction, while integrability is a statement about the existence of commuting first integrals, which may exist without the separated form. The elliptic coordinates of the examples below are the classical place where the two meet — a system whose integrability is invisible in the natural coordinates becomes separable in the elliptic ones.

## The Examples

### The Central Force

**Example (the central force in polar coordinates).** For a particle in a plane in a central potential $V(r)$ the Hamiltonian in polar coordinates $(r,\phi)$ is
$$
H = \frac{1}{2m}\Bigl(p_r^2+\frac{p_\phi^2}{r^2}\Bigr) + V(r) .
$$
The coordinate $\phi$ is cyclic, so $p_\phi=\alpha_\phi$ is a separation constant and the angular momentum; the characteristic function is $W=W_r(r)+\alpha_\phi\phi$ with
$$
\frac{dW_r}{dr} = \sqrt{2m\bigl(\alpha_1-V(r)\bigr) - \frac{\alpha_\phi^2}{r^2}} ,
$$
and the two quadratures $\partial W/\partial\alpha_1=\beta_1$ and $\partial W/\partial\alpha_\phi=\beta_\phi$ read
$$
\int^{r}\frac{m\,ds}{\sqrt{2m(\alpha_1-V(s))-\alpha_\phi^2/s^2}} = t+\beta_1 ,
\qquad
\phi - \int^{r}\frac{\alpha_\phi\,ds}{s^2\sqrt{2m(\alpha_1-V(s))-\alpha_\phi^2/s^2}} = \beta_\phi .
$$
The first is the time along the orbit and the second is the orbit itself. This is the classical reduction of the central-force problem to two quadratures, and the Stäckel form of the potential is $V=V_r(r)$ with the other terms absent.

**Example (the Kepler problem and the conic).** For $V(r)=-k/r$ the second quadrature integrates in closed form. With $u=1/r$ and the angular momentum $L=\alpha_\phi$, the orbit relation is
$$
u = \frac{mk}{L^2}\bigl(1+e\cos(\phi-\phi_0)\bigr), \qquad e = \sqrt{1+\frac{2\alpha_1L^2}{mk^2}} ,
$$
a conic with one focus at the centre and eccentricity $e$; the sign of the energy decides the type, $e<1$ an ellipse for $\alpha_1<0$, $e=1$ a parabola for $\alpha_1=0$ and $e>1$ a hyperbola for $\alpha_1>0$. The computation is the classical solution of the Kepler problem by the Hamilton–Jacobi method, and it shows the characteristic feature of the separable case: the orbit is obtained from the quadrature of $W_r$ without integrating the equations of motion. The same quadrature, read as a function of the time, is Kepler's equation.

### Spherical Coordinates

**Example (the spherical separation).** In spherical coordinates $(r,\theta,\phi)$ the Hamiltonian is as displayed above. For a central potential $U(r)$ the coordinate $\phi$ is cyclic, giving the constant $\alpha_\phi=p_\phi$, the component of the angular momentum along the polar axis; the coordinate $\theta$ gives the second separation constant
$$
\alpha_\theta^2 = p_\theta^2 + \frac{p_\phi^2}{\sin^2\theta} ,
$$
which is the squared magnitude of the angular momentum $|\mathbf L|^2$; and the radial equation is
$$
\frac{1}{2m}\Bigl(p_r^2+\frac{|\mathbf L|^2}{r^2}\Bigr)+U(r) = \alpha_1 ,
$$
with the energy as the third constant. The three constants $\alpha_1$, $|\mathbf L|^2$ and the axial component of $\mathbf L$ are the three commuting integrals of the spherical case, and they are read off directly from the separated equations. For the general Stäckel potential $U$ the $\phi$ equation is instead $(\partial W_\phi/\partial\phi)^2=2m\bigl(\Gamma_\phi-U_\phi(\phi)\bigr)$, whose constant $\Gamma_\phi$ is the bracket of the $\phi$ coordinate rather than the axial momentum; the central case is the one in which $U_\phi$ is constant and the bracket reduces to $\alpha_\phi^2/2m$. For the Kepler potential $U=-k/r$ the three constants reduce to the classical integrals of the Coulomb problem, and for the isotropic oscillator $U=\frac12m\omega^2r^2$ they exhibit the accidental degeneracy of that problem, whose extra integral is algebraic in the separated momenta.

### Parabolic Coordinates and the Stark Effect

**Example (the parabolic separation of the Coulomb problem).** Introduce the parabolic coordinates
$$
\xi = r+z , \qquad \eta = r-z , \qquad \phi ,
$$
so that $r=(\xi+\eta)/2$ and $z=(\xi-\eta)/2$. The Hamiltonian of a particle of mass $m$ in the Coulomb potential $-\kappa/r$ together with a uniform field $F$ along the polar axis is
$$
H = \frac{2}{m(\xi+\eta)}\bigl(\xi\,p_\xi^2+\eta\,p_\eta^2\bigr) + \frac{p_\phi^2}{2m\xi\eta} - \frac{2\kappa}{\xi+\eta} + \frac{F}{2}(\xi-\eta) .
$$
Multiplication by $\xi+\eta$ separates the equation into a $\xi$-part and an $\eta$-part,
$$
\frac{2}{m}\xi\Bigl(\frac{\partial W}{\partial\xi}\Bigr)^2 + \frac{p_\phi^2}{2m\xi} + \frac{F}{2}\xi^2 - \alpha_1\xi = B_1 ,
$$
$$
\frac{2}{m}\eta\Bigl(\frac{\partial W}{\partial\eta}\Bigr)^2 + \frac{p_\phi^2}{2m\eta} - \frac{F}{2}\eta^2 - \alpha_1\eta = B_2 ,
$$
with the two separation constants subject to $B_1+B_2=2\kappa$, the energy $\alpha_1$ and the axial momentum $p_\phi$ being the other two constants. The potential $-\kappa/r+Fz$ therefore separates in parabolic coordinates although it does not separate in spherical ones; this is the coordinate system of the Stark effect, in which the hydrogen atom in a uniform electric field is solved, and the two separation constants $B_1,B_2$ replace the angular momentum of the field-free spherical description, from which they differ because the field has broken the spherical symmetry.

### Elliptic Coordinates and the Two-Centre Problem

**Example (the two-centre problem).** The potential of a particle in the field of two fixed Coulomb centres at $\pm a$ on the polar axis is $U=-Z_1/r_1-Z_2/r_2$, where $r_1,r_2$ are the distances to the two centres. In the confocal elliptic coordinates of the plane, and in the prolate spheroidal coordinates of space, the two distances enter through the two combinations that the Stäckel construction requires, and the potential belongs to the Stäckel class of those coordinates; the equation separates, and the separation constant — a fourth integral besides the energy, the axial momentum and the magnitude of the angular momentum — is the classical distinguishing integral of the two-centre problem. This is the coordinate system of the hydrogen molecular ion in the Born–Oppenheimer approximation, and it is the classical instance of a problem whose integrability is exposed by the elliptic coordinates and hidden in the spherical ones. The statement is quoted as standard.

## The Limits of the Method

The Hamilton–Jacobi method is not an algorithm for all systems, and three limitations define its scope.

- **Separation is coordinate-dependent and not always available.** The method reduces a system to quadratures only when the equation separates; for a general potential no coordinate system separates it, and the only route is to integrate the characteristic system — that is, to return to Hamilton's equations. Separation is a condition on the pair of potential and coordinates, and neither can be chosen freely once the other is fixed.
- **Integrability without separation.** A completely integrable system may fail to separate in any of the classical coordinate systems, and even when it separates the coordinates may be unnatural: the two-centre and elliptic cases above are integrable in coordinates that the potential does not suggest. Conversely, a separable system is always integrable, so the separable systems form a proper subclass of the integrable ones.
- **The three-body problem.** For three or more mutually attracting bodies no complete integral is known, and the obstruction is not technical: the search for additional integrals is constrained by Poincaré's non-existence results, and the Hamilton–Jacobi equation of the problem does not separate. The method therefore solves the two-body problem and the classical separable systems, and stops where the general theory of dynamical systems takes over. The existence of a complete integral is the classical face of integrability, and its failure is the classical face of chaos.

## Summary

The Hamilton–Jacobi equation is the single scalar equation $\partial_tS+H(q,\partial_qS,t)=0$ obtained by asking the canonical transformation with generating function $S$ to make the Hamiltonian vanish; the momenta are the gradients of $S$, and the equation is the condition that the new coordinates be constant. A complete integral $S(q,\alpha,t)$, one carrying $f$ independent constants, solves the system by quadrature: the relations $\beta=\partial S/\partial\alpha$ and $p=\partial S/\partial q$ give the general solution in terms of the $2f$ constants $\alpha,\beta$. For an autonomous Hamiltonian the time separates first and the equation reduces to $H(q,\partial W/\partial q)=\alpha_1$ for the characteristic function $W$, whose constant is the energy.

The equation separates additively when the characteristic function is a sum of one-coordinate terms; each coordinate that enters the Hamiltonian only through one combination of itself and its own gradient can be separated off, and the value of that combination is a constant of the motion. The cyclic coordinate is the extreme case, its separation constant being the conserved momentum. For a Hamiltonian quadratic in the momenta in orthogonal coordinates the systematic criterion is the Stäckel condition: the potential separates if and only if it is a sum of one-coordinate terms, each multiplied by the same coordinate-dependent metric factor that multiplies the corresponding momentum term, which for spherical coordinates is the representation $U=U_r(r)+U_\theta(\theta)/r^2+U_\phi(\phi)/(r^2\sin^2\theta)$; the potentials satisfying it form the Stäckel class, and the coordinate systems in which the free equation separates are the finite classical list of Stäckel and Eisenhart, commonly quoted as eleven in three dimensions. The separation constants are the commuting integrals, the actions are the closed integrals of the separated momenta, and the transformation to the constants is the transformation to the action-angle coordinates.

The examples are the central force, whose separation constant is the angular momentum and whose two quadratures give the orbit and the time; the Kepler problem, whose orbit is the conic of eccentricity $e=\sqrt{1+2\alpha_1L^2/mk^2}$; the spherical coordinates, whose constants are the energy, the squared angular momentum and its axial component; the parabolic coordinates, in which the Coulomb problem in a uniform field separates although it does not in spherical coordinates; and the elliptic coordinates of the two-centre problem. The method's limits are the dependence of separation on the coordinates, the existence of integrable systems that do not separate, and the three-body problem, for which no complete integral and no separation is known.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $S(q,\alpha,t)$ | Principal function, a complete integral of the equation |
| $W(q,\alpha)$ | Characteristic function, the time-independent part of $S$ |
| $\partial_tS+H(q,\partial_qS,t)=0$ | Hamilton–Jacobi equation |
| $H(q,\partial W/\partial q)=\alpha_1$ | Reduced equation; $\alpha_1$ the energy |
| $\alpha_i$, $\beta_i$ | The $f$ constants of $S$ and their conjugate constants $\partial S/\partial\alpha_i$ |
| $\Gamma_k$, $\psi(q^k,\partial W/\partial q^k)$ | Separation constant and the separating combination |
| $h_i$, $1/h_i^2$ | Scale factors of orthogonal coordinates and the metric factors |
| $U_i(q^i)$ | One-coordinate pieces of the Stäckel potential |
| Stäckel class | Potentials of the form $U=\sum_i(1/h_i^2)U_i(q^i)$ |
| $I_i=\frac{1}{2\pi}\oint p_i\,dq^i$ | Action variables of a separable system |
| $(r,\theta,\phi)$, $(r,\phi)$ | Spherical and polar coordinates |
| $(\xi,\eta,\phi)$, $\xi=r+z$, $\eta=r-z$ | Parabolic coordinates |
| $\alpha_\phi$, $\alpha_\theta^2=|\mathbf L|^2$ | Spherical separation constants |
| $B_1$, $B_2$, $B_1+B_2=2\kappa$ | Parabolic separation constants of the Coulomb-plus-field problem |

## Further Reading

- Carl Gustav Jacob Jacobi, *Vorlesungen über Dynamik* (Reimer, 1866), for the equation, the principal function and the classical integration of Hamiltonian systems.
- Paul Stäckel, "Über die Integration der Hamilton–Jacobischen Differentialgleichung mittelst Separation der Variabeln", Habilitationsschrift, Halle (1891), and "Über die Bewegung eines Punktes in einer $n$-fachen Mannigfaltigkeit", *Mathematische Annalen* 42 (1893), for the Stäckel conditions and the separation of the equation.
- Luther Pfahler Eisenhart, "Separable Systems of Stäckel", *Annals of Mathematics* 35 (1934), for the enumeration of the separable orthogonal systems.
- Vladimir I. Arnold, *Mathematical Methods of Classical Mechanics* (Springer, 2nd ed. 1989), for the Hamilton–Jacobi method, the complete integral and the action-angle variables.
- Herbert Goldstein, Charles P. Poole and John L. Safko, *Classical Mechanics* (Addison-Wesley, 3rd ed. 2002), for the separation of variables, the Stäckel conditions and the worked examples.
- Lev D. Landau and Evgeny M. Lifshitz, *Mechanics* (Pergamon, 3rd ed. 1976), for the Hamilton–Jacobi equation and the separation in the classical coordinate systems.
- Edmund T. Whittaker, *A Treatise on the Analytical Dynamics of Particles and Rigid Bodies* (Cambridge University Press, 4th ed. 1937), for the classical quadratures and the separable problems.
- L. A. Pars, *A Treatise on Analytical Dynamics* (Heinemann, 1965), for the Stäckel theory and the two-centre problem.
- Max Born, *Mechanics of the Atom* (Bell, 1927), for the parabolic coordinates and the Stark effect.
- Richard Courant and David Hilbert, *Methods of Mathematical Physics*, vol. II (Interscience, 1962), for the first-order equation, its characteristics and the Hamilton–Jacobi theory.
