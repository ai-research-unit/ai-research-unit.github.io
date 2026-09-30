# __Scattering for the Quaternionic Dirac Operator: The Lippmann–Schwinger Equation, the Radiation Condition and Faddeev's Green's Function__

## Introduction

The corpus's quaternionic function theory is a theory of the **direct** problem. *Biquaternion Regular Functions* states the shifted operator $D_\alpha = D + M_\alpha$, its three parameter branches and its four integral theorems; *Maxwell's Equations in Chiral Media — The Quaternionic Reformulation* uses them to solve the boundary-value problem of a bounded scatterer. In both, the data are given on a closed surface: a Hölder field on $\Gamma$ is the trace of a solution of $D_\alpha g = 0$ in the domain if and only if $P_\alpha f = f$. Nothing in the corpus answers the question optics actually asks, which is the other way round: **given a medium that scatters a wave, what does the field far from it say about the medium?**

This article states the three-dimensional scattering theory of the same operator. The source is a short research paper of the quaternionic-analysis school, Swanhild Bernstein, *Seeing the Invisible and Maxwell's Equations*, written for a volume on inverse problems and motivated by **optical coherence tomography**. Its subject is the operator $D_3 + M_k$ with a **quaternionic, compactly supported potential** $m(x)$, and its tools are of two kinds. The first kind the corpus already owns: the Helmholtz fundamental solution, the outgoing radiation condition, the factorisation of the Laplacian, the zero-divisor cone. The second kind it does not: the **Lippmann–Schwinger** integral equation and its equivalence with the differential problem, the **unique continuation principle** that closes the Fredholm argument, and **Faddeev's Green's function** with the plane-wave substitution that produces it. The second kind is the substance of this article.

The article is organised as follows. A first section fixes the three-dimensional setting and the two one-sided multiplications, which are the source's notational pivot. A second recalls how Maxwell's equations become a Dirac-type system in a medium and states the force-free case. A third gives the two factorisations of the Helmholtz equation, by a scalar shift and by a vector one. A fourth states the outgoing fundamental solution of the Helmholtz operator, the boundary representation it gives, and the radiation condition, including the zero-divisor caveat recorded beside that condition in *Maxwell's Equations in Chiral Media — The Quaternionic Reformulation*. A fifth states the scattering problem and the integral equation equivalent to it. A sixth assembles the two inputs of the uniqueness theorem. A seventh gives Faddeev's Green's function. A closing section separates what the source establishes from what it transcribes, and lists the open questions.

**Conventions.** We use those of *Conventions in the Biquaternion Universe*, *Introduction to the Biquaternion Universe* and *Biquaternion Regular Functions*. The algebra is $\mathbb{B} = \mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ with basis $e_0=1,e_1,e_2,e_3$, $e_j^2=-e_0$, $e_je_k+e_ke_j=-2\delta_{jk}e_0$ for $j,k\ge1$, and central scalar imaginary $i$. The spatial Moisil–Teodoresco operator of *Biquaternion Regular Functions* is $D_3 = \sum_{k=1}^{3}e_k\partial_k$, with $D_3^2=-\Delta$ and $\Delta$ the Laplacian of $\mathbb{R}^3$; the corpus's other square root is $D = iD_3$, with $D^2=\Delta$, and the source writes its operator $D$ and means $D_3$, so **every occurrence of the source's $D$ is read here as $D_3$**. The Helmholtz fundamental solution is $\Theta_\alpha = -e^{i\alpha\lvert x\rvert}/(4\pi\lvert x\rvert)$ of *Biquaternion Regular Functions* and *Electromagnetism in Media — The Local Complex Structure at Work*, and the shifted family is $D_{3\pm\alpha} = D_3\pm\alpha$ of *Maxwell's Equations in Chiral Media — The Quaternionic Reformulation*, with fundamental solutions $\mathcal K_{\pm\alpha} = -(D_3\mp\alpha)\Theta_\alpha$ there. The null quadric $N(\tilde Q)=0$, the zero divisors $\mathcal Z$ and the scalar/vector/paravector subspaces are those of *Biquaternion Zero Divisors*, *Zero Divisors as a Physical Locus in Biquaternionic Form* and *The Light Cone as the Biquaternion Zero-Divisor Cone*. The fields live on $\mathbb{R}^3$ unless a variable is named, $G$ is a domain there, and $\hat{\mathbf{x}} = \mathbf{x}/\lvert\mathbf{x}\rvert$. We write $S(q)$ for the scalar part of a biquaternion $q$ and $V(q)$ for its pure part, and the quaternion conjugation is $\bar q = S(q)-V(q)$; in the source the pure part is written $q$ again, and its display of $V(q)$ in the preliminaries omits the summands, an evident slip for $V(q)=\sum_{j=1}^3 q_je_j$.

The reading list for the parts the corpus already owns is short: *Biquaternion Regular Functions* for the shifted operator; *Maxwell's Equations in Chiral Media — The Quaternionic Reformulation* for the radiation condition and its reductions; *Electromagnetism in Media — The Local Complex Structure at Work* for the Helmholtz kernel; *The Biquaternion D'Alembertian and Its Green's Functions* and *Exercise: The Retarded Potentials and the Green's Function* for the four-dimensional Green's functions, which this article does not use; and *Quaternion Harmonic Analysis* for the Radon and Fourier-slice side of tomography, which is the measured side rather than the scattering side. The mathematics sources for the ingredients the article transcribes are *Clifford Analysis* for monogenic functions, *Integrable Systems* and *Soliton Theory* for the one-dimensional inverse scattering transform, and *Coulomb Scattering and Rutherford's Formula in Biquaternionic Form* for the Born approximation as the corpus already has it.

## The Three-Dimensional Setting and the Two Multiplications

The setting is three-dimensional and the operator is the spatial Moisil–Teodoresco operator of *Biquaternion Regular Functions*,

$$
D_3 = \sum_{j=1}^{3} e_j\partial_j, \qquad D_3^2 = -\Delta .
$$

Its action on a pure-vector field is the classical pair of operations. Writing $u = u_1e_1+u_2e_2+u_3e_3$ for a vector field identified with its biquaternion,

$$
D_3 u = -\operatorname{div}u + \operatorname{curl}u ,
$$

so that the scalar part of $D_3u$ is minus the divergence and its vector part is the curl. This one identity is what makes the algebra a language for Maxwell's equations rather than an ornament on them: an equation whose scalar part is a divergence and whose vector part is a curl is a first-order system, and the algebra writes it as a single equation.

### The two one-sided multiplications

Because $\mathbb{B}$ is not commutative, a shift by an element of the algebra must say which side it multiplies on. The source introduces both,

$$
M^k q = kq \quad(\text{left multiplication}), \qquad M_k q = qk \quad(\text{right multiplication}), \qquad q\in\mathbb{B},
$$

so the **upper index multiplies on the left and the lower index on the right**. The corpus's own shift is the right one: the $M_\alpha$ of *Biquaternion Regular Functions* is $q\mapsto q\alpha$. The distinction matters twice in what follows. It matters algebraically, because the two operators have different symbols and different kernels; and it matters in the factorisations below, where the *same* second-order operator is produced by either side, so that a source that switches between $M^k$ and $M_k$ without comment is not in error, only terse. The source does switch: its section on the factorisation writes the vector shift with $M^k$ and its scattering problem is posed on $D_3+M_k$, and both are correct because a constant parameter commutes with $D_3$. What the two sides genuinely do not share is the fate of a *variable* coefficient: right multiplication by a function of $x$ does not commute with $\partial_j$, and the force-free case below is of that kind.

### Notation for the function spaces

Two weighted spaces are used. For $s\in\mathbb{R}$, $L^{2,s}$ is the set of scalar functions $u$ with $\lVert u\rVert_s = \lVert(1+\lvert x\rvert^2)^{s/2}u\rVert_{L^2(\mathbb{R}^3)}$ finite; for $\alpha\ge0$, $H^\alpha$ is the Sobolev space of scalar $u$ with $\lVert(1+\lvert\xi\rvert^{\alpha/2})\hat u\rVert_{L^2}$ finite, and $H^{\alpha,s}$ the corresponding weighted space. A biquaternion-valued function belongs to $C(G)$, $L^p(G)$, $H^1(G)$ and so on when each complex component does. These are the spaces in which the compactness and the bounds below are stated, and they are the source's.

## Maxwell's Equations as a Dirac-Type System

The source's second and third sections are the corpus's electromagnetic material seen from the scattering side, and they are recalled here because the scattering problem is posed for Maxwell's equations and only then transported to the algebra.

In an isotropic medium obeying Ohm's law, para- or diamagnetic, Maxwell's equations with the constitutive relations $\mathbf{D}=\epsilon\mathbf{E}$ and $\mathbf{B}=\mu\mathbf{H}$ read, in the time-harmonic regime $\mathbf{E}(x,t)=\mathrm{Re}(\mathbf{E}(x)e^{-i\omega t})$ and likewise for $\mathbf{H}$,

$$
\operatorname{curl}\mathbf{E}=i\omega\mu\mathbf{H}, \qquad
\operatorname{curl}\mathbf{H}=-i\omega\epsilon\mathbf{E}, \qquad
\operatorname{div}(\epsilon\mathbf{E})=0, \qquad
\operatorname{div}(\mu\mathbf{H})=0 .
$$

The refractive index of the medium is the complex number $N$ with

$$
N^2 = \mu_r\epsilon_r, \qquad N = n + i\kappa ,
$$

where $n$ is the usual refractive index and $\kappa$ the **extinction coefficient** describing the attenuation of the field in the medium. This is the quantity the tomography of the Introduction reconstructs, and it is a scalar field of the medium rather than an ingredient of the algebra.

### The quaternionic reformulation

With the normalised fields $\mathbf{E}\mapsto\sqrt{\epsilon}\,\mathbf{E}$ and $\mathbf{H}\mapsto\sqrt{\mu}\,\mathbf{H}$, the time-harmonic system becomes the pair

$$
D_\epsilon \mathbf{E} = -ik\mathbf{H} - \frac{\rho}{\sqrt{\epsilon}}, \qquad
D_\mu \mathbf{H} = ik\mathbf{E} + \sqrt{\mu}\,\mathbf{j}, \qquad
D_\alpha = D_3 + \operatorname{grad}\log\sqrt{\alpha},
$$

with $k=\omega\sqrt{\epsilon\mu}=\omega/c$ the wavenumber of the medium. The operator $D_\alpha$ here carries the same symbol as the corpus's $D_\alpha = D_3+M_\alpha$ but is **not the same operator**: the coefficient is the gradient coefficient $\operatorname{grad}\log\sqrt{\alpha}$, which *Electromagnetism in Media — The Local Complex Structure at Work* writes $D\pm M^{\vec{\alpha}_f}$, a **fixed vector field** multiplying on the left, rather than a constant element of the algebra. The pair above is the Kravchenko reformulation of Maxwell's equations in inhomogeneous media that the corpus's electromagnetic articles already record; it enters this article only as the reason the scattering problem below is a Maxwell problem.

### The force-free case

The one place in the source where the operator appears with a variable coefficient and a physical name is the **force-free magnetic field** of magnetohydrodynamics, characterised by

$$
\operatorname{div}\mathbf{B}=0, \qquad \operatorname{curl}\mathbf{B}+\alpha(x)\mathbf{B}=0
$$

for a scalar-valued function $\alpha(x)$. Because the scalar part of $D_3\mathbf{B}$ is $-\operatorname{div}\mathbf{B}$ and its vector part is $\operatorname{curl}\mathbf{B}$, and because $\mathbf{B}\alpha(x)=\alpha(x)\mathbf{B}$ for scalar $\alpha$, the pair of equations is **equivalent to the single equation**

$$
D_\alpha \mathbf{B} = 0, \qquad D_\alpha = D_3 + M_{\alpha(x)} .
$$

This is the source's Remark 5.1, attributing the relation to a paper of Kravchenko's on force-free fields. It is worth separating from the corpus's constant-parameter shift by more than a footnote: *Maxwell's Equations in Chiral Media — The Quaternionic Reformulation* and *Subluminal and Superluminal Electromagnetic Waves and the Lepton Mass Spectrum* treat the **constant-coefficient** Beltrami case, where $\alpha$ commutes with $D_3$ and the second-order companion is the scalar $\Delta+\alpha^2$, whereas here $\alpha$ is a function and right multiplication by it does not commute with $\partial_j$, so the companion is not a scalar operator and the theory of *Biquaternion Regular Functions* does not apply to it unchanged. Three objects are written $D_\alpha$ in play — the constant-parameter shift of *Biquaternion Regular Functions*, the gradient-coefficient operator $D\pm M^{\vec\alpha_f}$ of the electromagnetic articles, and this variable scalar-coefficient one — and this article names the distinction once so that they are not read for one another.

## The Two Factorisations of the Helmholtz Equation

Maxwell's equations reduce to second-order equations, and the reduction is a factorisation by first-order Dirac operators. This is why a scattering theory for the Dirac-type operator is a scattering theory for waves.

The four-dimensional identity is

$$
\frac{1}{c^2}\frac{\partial^2}{\partial t^2} - \Delta
= \left(\frac{1}{c}\frac{\partial}{\partial t} + iD_3\right)\left(\frac{1}{c}\frac{\partial}{\partial t} - iD_3\right),
$$

the wave operator in the source's sign; the corpus's d'Alembertian is its **negative**, $\Box = \Delta - c^{-2}\partial_t^2$ in *Biquaternion Analysis*, and the two conventions are not to be mixed. **The source prints this identity with the same factor twice**, which is not correct as it stands — with both factors equal, the cross terms add instead of cancelling and the right-hand side is $c^{-2}\partial_t^2+\Delta+2ic^{-1}\partial_tD_3$ — so what is written here is the corrected form, the two factors carrying opposite signs, whose cross terms cancel because $D_3$ has constant coefficients. In the time-harmonic case, with the dependence $e^{i\omega t}$ so that $\partial_t$ acts as $i\omega$, the factorisation is

$$
-\Delta - \frac{\omega^2}{c^2} = (D_3+k)(D_3-k), \qquad k=\frac{\omega}{c},
$$

the scalar shift of *Biquaternion Regular Functions* with its two branches $D_{3\pm k}$ and their fundamental solutions $\mathcal K_{\pm k}$; the kernel of the whole lies in the union of the two half-kernels, which is the decomposition used in *Maxwell's Equations in Chiral Media — The Quaternionic Reformulation*. This second form is the source's and is correct as printed, with $k$ the scalar wavenumber.

### The vector factorisation and its two signs

There is a second factorisation, and it is the one the scattering theory needs. With the parameter a **vector** $k=k_1e_1+k_2e_2+k_3e_3$ and either multiplication,

$$
(D_3+M^k)(D_3-M^k) = (D_3-M^k)(D_3+M^k) = -\Delta - k^2 = -\Delta + \lvert k\rvert^2 ,
$$

$$
(D_3+M^{ik})(D_3-M^{ik}) = (D_3-M^{ik})(D_3+M^{ik}) = -\Delta - i^2k^2 = -\Delta - \lvert k\rvert^2 ,
$$

where $k^2 = -k\cdot k = -\lvert k\rvert^2$ is the quaternion square of the vector. The two lines are one computation, the second being the first with $k\mapsto ik$, and between them they are the reason for the two signs the rest of the article carries. A shift by a **real** vector has the Klein–Gordon-type companion $-\Delta+\lvert k\rvert^2$, the sign of the square *opposite* to the scalar branch above; a shift by an **imaginary** vector has the Helmholtz companion $-\Delta-\lvert k\rvert^2$, which is the scalar branch's companion with $\alpha=\lvert k\rvert$. Both orderings agree in each line, and not because the parameter is a vector: a *constant* parameter of any kind commutes with $D_3$. The dependence on the side appears one step later, in the plane-wave substitution, and it is treated where it is used.

## The Green's Function, Its Boundary Representation and the Radiation Condition

### The outgoing Helmholtz kernel

The fundamental solution of the Helmholtz equation used throughout is the corpus's $\Theta_\alpha$ at $\alpha=k$,

$$
F_k(x-y) := -\frac{e^{ik\lvert x-y\rvert}}{4\pi\lvert x-y\rvert}, \qquad x,y\in\mathbb{R}^3,\ x\ne y .
$$

It solves $\Delta u+k^2u=0$ away from $y$, and its far-field behaviour is

$$
F_k(x-y) = -\frac{e^{ik\lvert x\rvert}}{4\pi\lvert x\rvert}\,e^{-ik\hat{\mathbf{x}}\cdot y} + O(\lvert x\rvert^{-2}), \qquad
D_3 F_k(x-y) = \bigl(D_3F_k\bigr)(x)\,e^{-ik\hat{\mathbf{x}}\cdot y} + O(\lvert x\rvert^{-2}),
$$

uniformly in the direction $\hat{\mathbf{x}}$ and in $y$ in a bounded set. The source's Proposition 7.1 attributes this. The first two terms are what will make every integral of the theory an **outgoing** field, and the $O(\lvert x\rvert^{-2})$ is what will make it satisfy the radiation condition with room to spare.

### The Cauchy-type kernel of the shifted operator

Applying the shifted operator to the Helmholtz kernel gives the fundamental solution of the Dirac-type equation,

$$
-D_{-k}F_k = C_k, \qquad
C_k(x) = \left(k+\frac{\mathbf{x}}{\lvert\mathbf{x}\rvert^{2}}-ik\hat{\mathbf{x}}\right)\frac{e^{ik\lvert\mathbf{x}\rvert}}{4\pi}, \qquad k=\text{const},\ \operatorname{Im}(k)\ge0 ,
$$

obtained, the source says, in the Kravchenko–Shapiro paper on the generalised Cauchy–Riemann system with a quaternionic parameter. Its bracket is exactly the bracket of the corpus's kernel in *Electromagnetism in Media — The Local Complex Structure at Work*,

$$
\mathcal K_{\pm\alpha} = -(D_3\mp\alpha)\Theta_\alpha = \left(\alpha+\frac{\mathbf{x}}{\lvert\mathbf{x}\rvert^{2}}-i\alpha\hat{\mathbf{x}}\right)\Theta_\alpha ,
$$

read at $\alpha=k$: since $D_{-k}=D_3-k$ is the negative branch $D_{3,-k}$, the source's kernel is $C_k=-(D_3-k)\Theta_k=\mathcal K_{+k}$. The two branches share the second-order companion, for $(D_3+k)(D_3-k)=-\Delta-k^2$ either way, so the companion cannot tell them apart and each of $\mathcal K_{\pm k}$ is a fundamental solution of **either** branch up to the normalisation sign; the corpus's table pairs $\mathcal K_{+\alpha}$ with $D_{3+\alpha}$ and the source applies $C_k$ to $D_{-k}$, and the pairing is a matter of convention rather than of substance. What is not a matter of convention is the **sign** of the kernel: the source's section 2.1 writes the free-space Green's function of the Helmholtz operator as $+e^{ik\lvert r-r'\rvert}/(4\pi\lvert r-r'\rvert)$, whereas the proposition writes $F_k$ with the minus. The two are Green's functions of the two signs of the same operator, $-\Delta-k^2$ and $\Delta+k^2$, and the chapter uses them in its two halves without noting the switch. The corpus's convention, fixed by $\Theta_\alpha$, is the one with the minus, and it is the one used in this article.

### The boundary representation

The fundamental solution gives a representation of the solutions of the first-order equation by their boundary values, the source's Proposition 7.2. Let $G$ be a bounded Lipschitz domain with boundary $\partial G$ and outward unit normal $n$, and let $u\in H^1(G)$. If $u\in\ker(D_3+k)$ and $\operatorname{Im}(k)\ge0$, then

$$
u(x) = -\int_{\partial G} C_k(x-y)\,n(y)\,u(y)\,dy ,
$$

and if $u$ lies in the kernel of the shifted operator — the source writes the two kernels as equal for the scalar $k$ of the proposition, where the two sides of the multiplication coincide — then

$$
u(x) = -\int_{\partial G}\Bigl[(-D_3F_k)(x-y)\,n(y)u(y) + n(y)u(y)\,F_k(x-y)\,k\Bigr]dy ,
$$

with $k=\sqrt{k^2}$ chosen so that $\operatorname{Im}(k)\ge0$. The two statements are the same Cauchy-type formula the corpus states on $\mathbb{H}_{\mathbb{B}}$ in *Biquaternion Regular Functions* and quotes for the shifted family in *Maxwell's Equations in Chiral Media — The Quaternionic Reformulation*; what is new here is only that the kernel is the **outgoing** one and that the representation is used, below, to force a field to vanish at infinity.

### The radiation condition

The condition that selects the outgoing solution is the source's Proposition 7.3, attributed to Kravchenko–Castillo. If $f\in H^1_{\mathrm{loc}}(G^{c})$ lies in $\ker(D_3+k)(G^{c})$ and satisfies the radiation condition

$$
\Bigl(k-\frac{\mathbf{x}}{\lvert\mathbf{x}\rvert^{2}}+ik\hat{\mathbf{x}}\Bigr)f(x) = o(\lvert x\rvert^{-1}) \qquad (\lvert x\rvert\to\infty),
$$

then $f = -C_k[f]$ for every $x\in G^{c}$, the middle bracket being a two-line fraction in the printed text. If instead $f$ lies in the kernel of the shifted operator and satisfies

$$
k\,f(x) + \frac{ix}{\lvert x\rvert}\,f(x)\,k = o(\lvert x\rvert^{-1}) \qquad (\lvert x\rvert\to\infty),
$$

with $k=\sqrt{k^{2}}$ and $\operatorname{Im}(k)\ge0$, then again $f=-C_k[f]$ on $G^{c}$; and **if $k$ is a zero divisor the source assumes in addition $f(x)=o(\lvert x\rvert^{-1})$**. The second form is the quaternionic radiation condition of the corpus's chiral-media article, the one whose scalar part is the Sommerfeld condition and whose vector part is the condition of Colton and Kress, and the extra hypothesis for the zero-divisor case is the caveat recorded beside it there: the element $1+i\hat{\mathbf{x}}$ is a non-pure zero divisor, so the condition may not be divided by it and implies no decay rate on its own. The source records the same fact in a remark of its own — for a scalar $k$ the term $\hat{\mathbf{x}}/\lvert x\rvert^{2}$ "can be written" away, "which apparently gives a faster decay", and this is "not true because $1+i\hat{\mathbf{x}}$ is a zero divisor" — and the reduction of the second condition to the first is exactly where the two $O(\lvert x\rvert^{-2})$ and $o(\lvert x\rvert^{-1})$ estimates of the previous sections have to be used with care.

The source adds one restriction that the corpus should note, because it is easy to lose: its Proposition 7.5 says the representation behind the proposition is true for quaternion-valued functions, but that the paper restricts itself to **vector** fields, quaternion-valued functions with vanishing scalar part. A general quaternion-valued field, and in particular one with a non-zero scalar part, is only partly covered, and this is a real limitation of the chapter rather than a notational preference: the scalar part of the field is what the divergence condition constrains in the Maxwell reading.

## The Scattering Problem and the Lippmann–Schwinger Equation

The problem is now stated for the Dirac-type operator itself, with a potential of the most general kind. Let $m(x)$ be a **quaternion-valued potential with compact support** $G$, and let $k$ be a vector identified with $k_1e_1+k_2e_2+k_3e_3\in\mathbb{H}$, with $k=\sqrt{k^{2}}$ and $\operatorname{Im}(k)\ge0$. Let $u^i$ be an incident field solving the **homogeneous** equation

$$
D_3u^i + u^ik = 0 \qquad \text{in } \mathbb{R}^3 . \tag{8.1}
$$

The scattering problem is to find a scattered field $u^s$ such that the total field $u=u^i+u^s$ solves the **inhomogeneous** equation

$$
D_3u + uk = u\,m(x)\,k \qquad \text{in } \mathbb{R}^3 , \tag{8.2}
$$

with $u = u^i+u^s$ and $u^s$ satisfying the radiation condition

$$
k\,u^s(x) + \frac{ix}{\lvert x\rvert}\,u^s(x)\,k = o(\lvert x\rvert^{-1}) \qquad (\lvert x\rvert\to\infty), \tag{8.4}
$$

and if $k$ is a zero divisor, the additional hypothesis $u^s(x)=o(1)$. The multiplication is on the **right** throughout, as the displayed equations (8.2) and (8.4) show; the source's prose names the same operator once as $D+k$ and once as $D+M_k$, and its reduction of the next section prints the left multiplication $M^k$ instead, so the side has to be read from the equations rather than from the symbols. For a scalar $k$ the two sides agree and the point is moot; for the vector $k$ of the scattering problem they do not: a constant $k$ still commutes with $D_3$, so the two agree to second order, but the first-order operators differ by the bracket $q\mapsto kq-qk$, which need not vanish. The potential may be scalar, vector or quaternion-valued; the source writes $m$ for all three and says so, and this is what makes the problem a scattering problem for a **medium** rather than for a scalar obstacle. In the optical reading of the Introduction, $m$ is the contrast of the medium and the right-hand side $umk$ is the Born-type source of the scattered field.

### The integral equation and its equivalence with the problem

The source's Theorem 8.2 states that the differential problem and an integral equation of Lippmann–Schwinger type have the same solutions. If $u$ solves (8.1)–(8.4), then $u$ restricted to $G$ solves

$$
u(x) = u^{i}(x) - \int_G \Bigl[(-D_3F_k)(x-y)\,u(y)\,m(y)\,k + u(y)\,m(y)\,k\,F_k(x-y)\,k\Bigr] dy , \tag{8.5}
$$

and conversely every solution of (8.5) solves the scattering problem. The equivalence is not a formality, and its two halves are computed in the source. In the forward direction one forms the integral $v$ on the right of (8.5); since the kernel of the Helmholtz operator is a fundamental solution, $v$ solves the same inhomogeneous equation as $u$, so $w=u-v$ solves the **homogeneous** equation $D_3w+wk=0$; and because each kernel decays like $\lvert x\rvert^{-2}$ and $u,m$ have compact support, $w$ is an outgoing solution of the homogeneous equation, whence $w=0$ by the representation of the radiation-condition proposition. That is, the integral equation is the differential problem with the radiation condition solved out, and the forcing term is the potential. In the other direction the same computation is read backwards, and the source notes that the region of integration may be replaced by any domain containing the support of $m$, which is what makes the equation a Fredholm equation on a bounded domain.

### The two hypotheses on the potential

Two conditions on $m$ are used, and the corpus should state them with the theorem rather than after it. The source assumes the potentials satisfy

$$
\max_{x\in G}\lvert m_j(x)\rvert \le C_1, \qquad \max_{x\in G}\lvert \operatorname{grad}m_j(x)\rvert \le C_2
$$

for constants $C_1,C_2$ and each component $m_j$; they are the hypotheses under which the unique continuation principle of the next section applies to the reduced system. A potential that is merely bounded and compactly supported is not enough for the proof as written.

## Uniqueness: Compactness and the Unique Continuation Principle

The existence of a solution to (8.5) is obtained by the Fredholm alternative, and the Fredholm alternative needs two facts: that the integral operator is compact, and that its homogeneous equation has only the trivial solution. The source supplies them from two different sources.

**Compactness** comes from the weak singularity of the kernels. The source's Lemma 8.4 states

$$
\lvert F_k(x-y)\rvert \le \frac{c}{\lvert x-y\rvert}, \qquad
\lvert D_3F_k(x-y)\rvert \le \frac{c_1}{\lvert x-y\rvert^{2}} + \frac{c_2}{\lvert x-y\rvert} ,
$$

so the kernels of the Lippmann–Schwinger equation are weakly singular, hence the integral operators are **compact** as maps on spaces of continuous functions and on $L^p$, $1<p<\infty$, for bounded domains. This is the classical route, and the corpus's scattering articles use it in the same form; it is worth noting that it needs the *boundedness* of the domain, which is why the integration is over $G$ and not over $\mathbb{R}^3$.

**Uniqueness** of the homogeneous solution comes from the unique continuation principle, quoted as the source's Lemma 8.5 from Colton and Kress, with the proof going back to Müller. Let $G\subset\mathbb{R}^3$ be a domain and $u_1,\dots,u_P\in C^2(G)$ real-valued with

$$
\lvert\Delta u_p\rvert \le c\sum_{q=1}^{P}\bigl\{\lvert u_q\rvert+\lvert\operatorname{grad}u_q\rvert\bigr\} \qquad \text{in } G, \qquad p=1,\dots,P ,
$$

for some constant $c$. If every $u_p$ vanishes in a neighbourhood of some point $x_0\in G$, then every $u_p$ is identically zero in $G$. To reach this hypothesis from the equation, the source applies $D_3$ to the homogeneous form of (8.2), $(D_3+M_k)u-m(x)uk=0$ — the source prints $M^k$ in this one line, the left multiplication, which is a different operator from the $M_k$ of its scattering problem when $k$ is a vector — obtaining

$$
\Delta u = (D_3u)k - D_3\bigl(m(x)uk\bigr),
$$

which is then expanded in scalar and vector parts into a system of the required shape, with the derivatives of $u$ and of $m$ on the right. The two hypotheses on $m$ above are exactly what this expansion needs.

### The uniqueness theorem

The source's Theorem 8.6 gathers the two inputs. For $k\in\mathbb{C}^3\setminus\{0\}$ there is a **unique** solution of the scattering problem (8.1)–(8.4), and it depends continuously on the incident field $u^{i}$ in the maximum norm. The proof is the Fredholm argument: the homogeneous equation has only the trivial solution by the previous paragraph, so the integral operator is boundedly invertible on $C(\bar B_R)$, whence existence and continuous dependence.

Two remarks on the statement, both of which the corpus should keep distinct from the source's own framing. First, the theorem is a theorem about the **direct** problem: existence, uniqueness and stability for a *given* incident field and a *given* potential. The chapter's title and abstract say inverse scattering, and the Faddeev Green's function of the next section is indeed a tool of the inverse problem, but the inverse problem proper — recovering $m$ from the field at infinity — is not solved in the chapter. Second, the proof closes not by the compactness alone but by the **outgoing** representation: the field is written as an integral over a large sphere, the radiation condition makes that integral vanish as the radius grows, so $u=0$ outside a ball, and the unique continuation principle extends the vanishing inward. The radiation condition is therefore not an auxiliary convenience in this theory; it is the half of the argument that the differential problem alone does not supply.

## Faddeev's Green's Function

The last construction of the source is the one that points at the inverse problem. Its idea is to conjugate the differential operator by a **plane wave**, which converts a Green's function with oscillatory behaviour at infinity into one that grows exponentially and therefore has better analytic properties in a parameter — Faddeev's construction, later used by Nachman and Ablowitz, Beals and Coifman, Sylvester and Uhlmann, Päivärinta and Isozaki in multidimensional inverse scattering.

### The plane-wave substitution

Three substitution identities are computed. For the Laplacian,

$$
(\Delta+k^2)\bigl(e^{ik\cdot x}v\bigr) = e^{ik\cdot x}\bigl(\Delta+2ik\cdot\nabla\bigr)v ,
$$

so that the Helmholtz operator becomes the **conjugate** operator $-\Delta-2ik\cdot\nabla-\lambda^2$ below. For the unshifted Dirac operator,

$$
(D_3-M^{ik})\bigl(e^{ik\cdot x}v\bigr) = e^{ik\cdot x}D_3v ,
$$

the plane wave being annihilated exactly. And for the shifted operator,

$$
(D_3+M_{ik})\bigl(e^{ik\cdot x}v\bigr) = e^{ik\cdot x}\bigl(D_3v + ikv + v\,ik\bigr),
$$

which is where the side of the multiplication shows: the term $ikv$ comes from $D_3$'s action on the plane wave, and the term $v\,ik$ from the shift. For a **vector-valued** $v$ the two products $ikv$ and $v\,ik$ combine, for $i$ is central and

$$
kv + vk = -k\cdot v + k\times v - v\cdot k + v\times k = -2\,k\cdot v ,
$$

the cross terms cancelling and the sum being a pure scalar, so that the first and third terms collapse to $-2i(k\cdot v)$ and

$$
(D_3+M_{ik})\bigl(e^{ik\cdot x}v\bigr) = e^{ik\cdot x}\bigl(D_3v-2i\,k\cdot v\bigr) .
$$

For a general quaternion-valued $v$ the two products do not combine and the substitution is not the plain transport of the vector case. This is the asymmetry announced in the factorisation section, and it is the reason the source poses its scattering problem on the vector operator and restricts, as noted above, to vector fields.

### The Green's operator

Faddeev's decomposition is to write the wave vector as $k=\eta+t\gamma$ with $\gamma\in S^2$ a direction, $\eta\cdot\gamma=0$, and to conjugate by the plane wave along $\gamma$. Applied to $e^{it\gamma\cdot x}w(x)$ the Helmholtz operator gives

$$
(\Delta+k^2)\bigl(e^{it\gamma\cdot x}w\bigr) = e^{it\gamma\cdot x}\bigl(-t^2+k^2+2it\gamma\cdot\nabla+\Delta\bigr)w ,
$$

so the operator to invert is $-\Delta-2it\gamma\cdot\nabla-\lambda^2$ with

$$
\lambda^2 = k^2-t^2 .
$$

Its Fourier transform is multiplication by $\xi^2+2t\gamma\cdot\xi-\lambda^2$; replacing the real $t$ by a complex parameter $z$, the symbol is invertible away from $\operatorname{Im}(z)=0$, and the **Faddeev Green's operator** is defined by the inverse of that symbol,

$$
\bigl(g_\gamma(\lambda,z)f\bigr)(x) = \frac{1}{(2\pi)^3}\int \frac{e^{ix\cdot\xi}}{\xi^2+2z\gamma\cdot\xi-\lambda^2}\,\hat f(\xi)\,d\xi ,
\qquad \gamma\in S^2,\ \lambda\ge0,\ z\in\mathbb{C}_+ = \{z : \operatorname{Im}(z)>0\} ,
$$

with the boundary value $g_\gamma(\lambda,t+i0)$ for real $t$. The symbol is non-degenerate for $\operatorname{Im}(z)\ne0$, so the integral converges absolutely for Schwartz $f$: this is the gain of the construction, an invertible symbol where the Helmholtz symbol is not.

### The bounds, and the two Faddeev Green's functions

The properties of $g_\gamma$ are quoted from Isozaki: for $s>\tfrac12$ it is continuous in $(\lambda,\gamma,z)$ except at $(\lambda,z)=(0,0)$, it is analytic in $z\in\mathbb{C}_+$, and for every $\delta_0>0$ and $0\le\alpha\le2$ there is $C$ with

$$
\lVert g_\gamma(\lambda,z)\rVert_{(L^{2,s}\to H^{\alpha,s})} \le \frac{C}{(\lambda+\lvert z\rvert)^{1-\alpha}}, \qquad \lambda+\lvert z\rvert\ge\delta_0 .
$$

The two Green's functions of the shifted operators are then obtained by applying the first-order operator to $g_\gamma$: the source gives

$$
G_\gamma(\lambda,z) = (D_3+M^{iz\gamma}-k)\,g_\gamma(\lambda,z)
$$

for the left-multiplication case, obtained from $(D_3+M^{iz\gamma}-k)(D_3+M^{iz\gamma}+k) = -\Delta-2iz\gamma\cdot\nabla-\lambda^2$ with $\lambda^2=k^2-z^2$, and a **different** Faddeev Green's function

$$
G_\gamma(\lambda,z) = (D_3+M^{iz\gamma}-M_{ik})\,g_\gamma(\lambda,z)
$$

for the right-multiplication case, from the corresponding factorisation with the right multiplications. The two differ because the two sides of the multiplication differ, and the source's own remark is the blunt one: "the multiplication from the other side leads to a different Faddeev's Green's function". The properties are restated as a theorem: the same continuity and analyticity as $g_\gamma$, and for $s>\tfrac12$, $\lambda+\lvert z\rvert\ge\delta_0$ and $0\le\alpha\le1$ a constant $C$ with

$$
\lVert g_\gamma(\lambda,z)\rVert_{(L^{2,s}\to H^{\alpha,s})} \le C\,(\lambda+\lvert z\rvert)^{\alpha} .
$$

This last estimate is printed with the *opposite* dependence on $\lambda+\lvert z\rvert$ from the proposition above it — increasing where the earlier bound decreases — and the two ranges of $\alpha$ do not coincide. As printed, the second is not a smoothing estimate and the first is; the discrepancy is recorded here and in the companion `.context`, and the reciprocal is to be checked against Isozaki's paper before either bound is relied on. The theorem's preamble speaks of the two $G_\gamma$ while its three items are printed with $g_\gamma$, one more instance of the chapter's loose use of the two symbols; the bounds are meant for the Green's functions of the shifted operators, which is how they are read here. The chapter's closing sentence draws the conclusion of the whole construction: with Faddeev's Green's function the inverse problem can be attacked, and its solution $u$ may be assumed to have the structure $u=e^{ik\cdot x}v$, which is the appropriate setting for optical coherence tomography.

## What the Source Establishes, Transcribes, and Does Not

**Transcribed from the corpus's own materials.**

- The three-dimensional setting, the operator $D_3$ and the identification $D_3u=-\operatorname{div}u+\operatorname{curl}u$; the Helmholtz kernel $\Theta_k=F_k$ and the shifted kernels $\mathcal K_{\pm k}$; the zero-divisor structure of the radiation condition. All of these are in *Biquaternion Regular Functions*, *Maxwell's Equations in Chiral Media — The Quaternionic Reformulation* and *Electromagnetism in Media — The Local Complex Structure at Work*, and this article adds no formula to them.
- The Maxwell reduction and the quaternionic reformulation in inhomogeneous media, which the corpus's electromagnetic articles own.

**Transcribed from the source, not derived here.**

- The outgoing kernel $C_k=-D_{-k}F_k$, its far-field asymptotics and the boundary representation of Proposition 7.2.
- The radiation condition of Proposition 7.3 in both forms, and the additional decay hypothesis in the zero-divisor case.
- The Lippmann–Schwinger equation (8.5) and its equivalence with the differential problem.
- The weak-singularity bounds, the compactness they give, the unique continuation principle and the uniqueness theorem.
- Faddeev's decomposition, the Green's operator $g_\gamma$, Isozaki's bounds and the two Green's functions $G_\gamma$.

**Established, in the sense that it was recomputed here.**

- The vector factorisation and the plane-wave substitution identities of the third and seventh sections: $(D_3\pm M_k)(D_3\mp M_k)=-\Delta+\lvert k\rvert^2$ and the same with $ik$, both orderings; $(D_3-M^{ik})(e^{ik\cdot x}v)=e^{ik\cdot x}D_3v$; and $kv+vk=-2k\cdot v$ for vector $v$ with the collapse failing for a general quaternion. The two-sided vocabulary — which of $M^k$ and $M_k$ the source uses in each section, and why either answers for a constant parameter — was reconstructed here, because the source does not state it.
- The identification $C_k=\mathcal K_{+k}$ in the corpus's notation, and with it the decision that the corpus's kernel sign, not the source's section 2.1 sign, is the one to keep.

**Not established, and left visible.**

- **The inverse problem itself.** The chapter's title, abstract and motivation are inverse scattering, but what Theorem 8.6 decides is the direct problem. The nearest thing to an inversion is the closing remark that the Faddeev Green's function makes the inverse problem accessible; a reconstruction formula, a uniqueness theorem for the potential and a stability estimate for the recovery of $m$ are all absent.
- **A quaternion-valued scattering theory.** The restriction to vector fields of Proposition 7.5 is carried through the whole paper, and the scalar part of a general quaternion-valued field — the part that the Maxwell reading constrains by $\operatorname{div}$ — is not covered.
- **The zero-divisor case.** The isotropic $k$ is handled by adding a hypothesis, not by a theory: nothing is said about what the radiation condition alone implies there, and the corpus's own algebra of the cone is not used.
- **Compatibility with the corpus's $D_\alpha$.** The source's $D$ is $D_3$; its variable-coefficient $D_\alpha$ of the force-free section is a third operator, distinct from the corpus's constant-parameter shift and from the gradient-coefficient operator of the electromagnetic articles. The three are kept apart here and nowhere identified.

## Open Questions

1. **Is there a four-variable scattering theory for $\tilde\nabla$?** The corpus's *Biquaternion Regular Functions* works on $\mathbb{H}_{\mathbb{B}}$ in four variables and its integral theory is complete there. The source's scattering theory is three-dimensional and spatial, with the frequency entering through $k$; the four-dimensional analogue, in which the radiation condition would be a condition on the two cones of the null quadric, is not in the corpus and is not in this source. Is the spatial reduction a convenience of the optical setting, or is the four-variable problem genuinely different?

2. **Does the corpus's zero-divisor algebra improve the isotropic case?** The source adds $u^s=o(1)$ when $k$ is isotropic. The corpus knows the geometry of the null cone: an isotropic $k$ has vanishing norm, $N(k)=0$, the elements $\tfrac12(1\pm i\hat{\mathbf{x}})$ are idempotents and zero divisors on it, and the cone carries the light-cone structure and the sphere of idempotents (*Biquaternion Zero Divisors*, *Biquaternion Idempotents and Projections*, *The Light Cone as the Biquaternion Zero-Divisor Cone*). Is there a radiation condition adapted to the degenerate direction, rather than a hypothesis that avoids it?

3. **Can the one-dimensional transform and the three-dimensional equation be read in one language?** The corpus has the inverse scattering transform and the Lax pair in *Integrable Systems* and *Soliton Theory*, and the source mentions the AKNS method as a motivation for the Dirac-operator route. Both routes are built on a factorisation of a Dirac-type operator, in different dimensions; is the Faddeev Green's function the three-dimensional input of a Riemann–Hilbert problem whose one-dimensional shadow is the corpus's transform?

4. **What does the Born approximation give for the quaternionic potential?** The corpus's Born approximation is in *Coulomb Scattering and Rutherford's Formula in Biquaternionic Form*, and the source's optical motivation uses the first-order Born term with the scattering potential $k^2[m^2-1]$. Is the first iteration of (8.5) — the integral with $u$ replaced by $u^i$ — the same object as the corpus's Born term, and does the quaternionic potential add a polarisation structure the scalar optical formula lacks?

5. **Is the vector-field restriction removable by the material/informational split?** A general quaternion-valued field splits into a scalar part and a vector part, and the corpus reads those two parts as the informational and the material sectors (*The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*, *The Anti-Hermitian Subspace $\mathbb{M}_-$ as the Material Sector*). The source discards one half; the corpus's reading would keep both. Does the scattering theory of the full field split into two coupled problems along the same line?

## Summary

The corpus's theory of the shifted operator $D_\alpha$ is a direct theory: it decides boundary-value problems. This article states the scattering theory of the same operator, in the three-dimensional spatial setting, as it stands in a short paper of the quaternionic-analysis school. The subject is the operator $D_3+M_k$ with a compactly supported quaternionic potential $m(x)$, and the objects that make the theory work are three.

The **Lippmann–Schwinger equation** is equivalent to the differential problem with the outgoing radiation condition: the total field $u=u^i+u^s$ satisfies the integral equation exactly when it satisfies $D_3u+uk=umk$ and $u^s$ is outgoing. The equivalence is the radiation condition solved out, and the source's proof uses the $O(\lvert x\rvert^{-2})$ decay of the kernels to show that the integral is outgoing.

**Uniqueness and existence** follow from the Fredholm alternative with two inputs: the compactness of the integral operator, which is the weak singularity $\lvert x-y\rvert^{-2}, \lvert x-y\rvert^{-1}$ of the kernels, and the uniqueness of the homogeneous solution, which is the unique continuation principle applied to a system derived by applying $D_3$ a second time. The proof closes through the radiation condition: the field is represented by a sphere integral that the condition makes vanish, so the field vanishes outside a ball, and unique continuation carries the vanishing inward.

**Faddeev's Green's function** is obtained by conjugating the operator by a plane wave along a direction $\gamma$, which replaces the Helmholtz symbol by the non-degenerate $\xi^2+2z\gamma\cdot\xi-\lambda^2$; its bounds, quoted from Isozaki, are what the multidimensional inverse-scattering method uses. The construction is applied separately to the two sides of the multiplication, and — this is the source's own remark — the right-multiplication operator has a *different* Faddeev Green's function from the left-multiplication one. The whole chapter is written for vector fields, and the inverse problem proper is not solved in it; what it supplies is the apparatus of the direct problem in quaternionic form and the Green's function that an inversion would need.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $e_0=1,e_1,e_2,e_3$ | Basis of $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$; $e_j^2=-e_0$; central scalar imaginary $i$ |
| $D_3=\sum_{j=1}^3 e_j\partial_j$ | Spatial Moisil–Teodoresco operator of *Biquaternion Regular Functions*; $D_3^2=-\Delta$; the source's $D$ |
| $D=iD_3$ | The corpus's other square root of the Laplacian, $D^2=\Delta$; distinct from the source's $D$ |
| $D_3u=-\operatorname{div}u+\operatorname{curl}u$ | The action on a pure-vector field, the bridge to Maxwell's equations |
| $M^kq=kq$, $M_kq=qk$ | Left and right multiplication; the upper index is the left one |
| $D_\alpha=D_3+M_\alpha$ | The corpus's shift, constant parameter; a different object from the gradient-coefficient $D_\alpha=D_3+\operatorname{grad}\log\sqrt{\alpha}$ of the electromagnetic articles |
| $k$ | Wave vector, identified with $k_1e_1+k_2e_2+k_3e_3$; $k=\sqrt{k^2}$, $\operatorname{Im}(k)\ge0$; $k^2=-k\cdot k$ |
| $\Theta_\alpha=-e^{i\alpha\lvert x\rvert}/(4\pi\lvert x\rvert)$ | Helmholtz fundamental solution; the source's $F_k$ at $\alpha=k$ |
| $\mathcal K_{\pm\alpha}=-(D_3\mp\alpha)\Theta_\alpha$ | Fundamental solutions of the shifted family; the source's $C_k$ is $\mathcal K_{+k}$ |
| $C_k=-D_{-k}F_k$ | Cauchy-type kernel of the Dirac-type operator, $(k+\hat{\mathbf{x}}/\lvert x\rvert-ik\hat{\mathbf{x}})e^{ik\lvert x\rvert}/(4\pi)$ |
| $k f+\hat{\mathbf{x}}fk=o(\lvert x\rvert^{-1})$ | The quaternionic radiation condition; the factor $1+i\hat{\mathbf{x}}$ is a zero divisor |
| $m(x)$ | Quaternion-valued potential with compact support $G$ |
| $u^i,u^s,u=u^i+u^s$ | Incident, scattered and total field |
| (8.1)–(8.4) | The scattering problem: homogeneous incident field, inhomogeneous total field, outgoing scattered field |
| (8.5) | The Lippmann–Schwinger integral equation; equivalent to (8.1)–(8.4) |
| $L^{2,s}$, $H^{\alpha,s}$ | Weighted $L^2$ and weighted Sobolev spaces of the compactness and the bounds |
| $k=\eta+t\gamma$, $\lambda^2=k^2-t^2$ | Faddeev's decomposition of the wave vector along a unit direction $\gamma$ |
| $g_\gamma(\lambda,z)$ | Faddeev's Green's operator; symbol $(\xi^2+2z\gamma\cdot\xi-\lambda^2)^{-1}$, $z\in\mathbb{C}_+$ |
| $G_\gamma(\lambda,z)$ | The two Faddeev Green's functions of the shifted operators, one for each side of the multiplication |

## Further Reading

- Swanhild Bernstein, "Seeing the Invisible and Maxwell's Equations", chapter, DOI 10.1007/978-3-0348-0603-9_13 (2013), the source of this article: the factorisations of the Helmholtz equation, the Lippmann–Schwinger equation for a quaternionic potential, the radiation condition with its zero-divisor remark, the uniqueness theorem, and Faddeev's Green's function. The scattering half of the same author's work; her 1996 and 1999 papers on the Riccati form of the factorisation, cited by *Electromagnetism in Media — The Local Complex Structure at Work*, are different papers.
- D. Colton and R. Kress, *Inverse Acoustic and Electromagnetic Scattering Theory*, Applied Mathematical Sciences 93 (Springer, 1992), for the Lippmann–Schwinger equation, the weak singularity of its kernel and the unique continuation principle (their Lemma, used as the source's Lemma 8.5).
- V. V. Kravchenko and R. P. Castillo, "An analogue of the Sommerfeld radiation condition for the Dirac operator", *Mathematical Methods in the Applied Sciences* **25** (2002) 1383–1394, for the two forms of the radiation condition used here.
- V. V. Kravchenko and M. V. Shapiro, "On a generalized system of Cauchy–Riemann equations with a quaternionic parameter", *Russian Academy of Sciences, Doklady* **47** (1993) 315–319, for the kernel $C_k=-D_{-k}F_k$.
- L. D. Faddeev, "Increasing solutions of the Schrödinger equation", *Doklady Akademii Nauk SSSR* **165** (1965) 514–517, for the exponentially growing Green's function and the plane-wave substitution.
- S. Bernstein, "Lippmann–Schwinger's integral equation for quaternionic Dirac operators", online (2003), the earlier paper by the same author in which the Lippmann–Schwinger equation for the quaternionic Dirac operator is announced; the chapter of the Further Reading above carries it further and cites it as [4].
- H. Isozaki, "Inverse scattering theory for Dirac operators", *Annales de l'Institut Henri Poincaré, section A* **66** (1997) 237–270, for Faddeev's Green's operator $g_\gamma$, its bounds and their use in the inverse problem, quoted in the last section.
- A. I. Nachman and M. J. Ablowitz, "A multidimensional inverse scattering method", *Studies in Applied Mathematics* **71** (1984) 243–250; R. Beals and R. R. Coifman, "Multidimensional inverse scattering and nonlinear partial differential equations", *Proceedings of Symposia in Pure Mathematics* **43** (1985) 45–70; and J. Sylvester and G. Uhlmann, "A global uniqueness theorem for an inverse boundary value problem", *Annals of Mathematics* **125** (1987) 153–169, for the Faddeev method in multidimensions.
- A. McIntosh and M. Mitrea, "Clifford algebras and Maxwell's equations in Lipschitz domains", *Mathematical Methods in the Applied Sciences* **22** (1999) 1599–1629, for the Dirac-operator form of Maxwell's equations on Lipschitz domains.
- C. Müller, "On the behavior of solutions of the differential equation $\Delta u=F(x,u)$ in a neighborhood of a point", *Communications on Pure and Applied Mathematics* **7** (1954) 505–515, for the unique continuation principle.
- A. F. Fercher, "Optical coherence tomography", *Journal of Biomedical Optics* **1** (1996) 153–173; A. F. Fercher, W. Drexler, C. K. Hitzenberger and T. Lasser, "Optical coherence tomography — principles and applications", *Reports on Progress in Physics* **66** (2003) 239–303, for the tomographic motivation of the chapter.
- Companion articles: *Biquaternion Regular Functions* (the shift $D_\alpha$ and its integral theory); *Maxwell's Equations in Chiral Media — The Quaternionic Reformulation* (the radiation condition, the two reductions and the zero-divisor caveat); *Electromagnetism in Media — The Local Complex Structure at Work* (the Helmholtz and shifted kernels); *Biquaternion Zero Divisors*, *Zero Divisors as a Physical Locus in Biquaternionic Form*, *The Light Cone as the Biquaternion Zero-Divisor Cone* and *Biquaternion Idempotents and Projections* (the algebra of the cone, the non-pure zero divisor $1+i\hat{\mathbf{x}}$ and its idempotents); *The Biquaternion D'Alembertian and Its Green's Functions* and *Exercise: The Retarded Potentials and the Green's Function* (the four-dimensional Green's functions, not used here); *Quaternion Harmonic Analysis* (the Radon transform and the Fourier slice theorem, the measured side of tomography); *Coulomb Scattering and Rutherford's Formula in Biquaternionic Form* (the Born approximation as the corpus has it); *Integrable Systems* and *Soliton Theory* (the one-dimensional inverse scattering transform and the Lax–AKNS route); *Clifford Analysis* (monogenic functions and the shifted operator on the real Clifford side); *Conventions in the Biquaternion Universe*.
