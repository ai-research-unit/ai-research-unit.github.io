
# __Fueter Theory__

## Introduction

Fueter theory is the function theory of a quaternionic variable built from a first-order operator. Its subject is a function $f:\Omega\to\mathbb{H}$ of a quaternion $q=q_t+q_x\vec e_x+q_y\vec e_y+q_z\vec e_z$, and its basic notion is that of a **regular** function: one annihilated by the **Fueter operator**

$$
\bar\partial = \partial/\partial Q_t+\vec e_x\partial/\partial Q_x+\vec e_y\partial/\partial Q_y+\vec e_z\partial/\partial Q_z ,
$$

the conjugate of which, $\partial=\partial/\partial Q_t-\vec e_x\partial/\partial Q_x-\vec e_y\partial/\partial Q_y-\vec e_z\partial/\partial Q_z$, satisfies $\bar\partial\partial=\partial\bar\partial=\Delta$, the Laplacian of $\mathbb{R}^4$. The theory was introduced by Fueter in 1935 as the quaternionic analogue of complex analysis: the aim was a class of functions with a Cauchy integral formula, a power-series expansion and a Cauchy–Riemann system. The class is the quaternionic instance of the monogenic functions of *Clifford Analysis*, so the general operator theory is not repeated here; what this article develops is what is specific to the quaternionic case, and the article states at each point which of its results is an instance of the general theory and which is peculiar to four dimensions.

Three features organise the article. The first is the **Cauchy–Fueter integral formula**, $f(q)=\frac{1}{2\pi^2}\int_{\partial\Omega}\frac{(p-q)^{\natural}}{|p-q|^4}\,\nu_B(p)f(p)\,dS(p)$, the quaternionic form of the general Cauchy formula, whose kernel is the fundamental solution of the Fueter operator. The second is **Fueter's theorem**, the construction that produces regular functions from holomorphic functions of one complex variable: the radial extension of a holomorphic function is not regular, but its Laplacian is, and the construction shifts the homogeneity by two. This theorem is the reason the quaternionic theory is a genuine generalisation of complex analysis rather than a formal analogue, and it is the result that the per-system theories generalise. The third is the **axial** description of the functions that the construction produces: a regular function constant on the spheres about the real axis is determined by two real functions of two variables satisfying a pair of equations, and Fueter's theorem is the statement that these are the equations of a holomorphic function in disguise.

The boundaries are these. The general hypercomplex theory — left and right regularity, the symbol, ellipticity, the Cauchy transform, the per-system value spaces — is in *Hypercomplex Analysis* and *Regularity and the Cauchy–Riemann Operator*, and is cited; the integration theory of that general setting is not covered here. The Clifford-algebra formulation, the Fischer decomposition and the polymonogenic functions are in *Clifford Analysis*, the immediately preceding article, and are used there. The quaternionic analyses of the other systems — the biquaternionic case, the split-biquaternionic case, the slice theory with its own power series — belong to Part V and are cited as the places where the system-specific statements are proved. The article is mathematics: no physical reading of $\mathbb{R}^4$ is used.

## The Fueter Operator and Regularity

### The Algebra and the Operator

Let $\mathbb{H}$ be the real quaternion algebra, with basis $e_t,\vec e_x,\vec e_y,\vec e_z$ and relations $\vec e_\mu^2=-e_t$, $\vec e_\mu\vec e_\nu=-\vec e_\nu\vec e_\mu$ for $\mu\neq\nu$, and $\vec e_x\vec e_y=\vec e_z$. A quaternion is written $q=q_t+\vec q$, $q_t\in\mathbb{R}$, $\vec q=q_x\vec e_x+q_y\vec e_y+q_z\vec e_z$; its conjugate is $q^{\natural}=q_t-\vec q$, its norm is $N(q)=q q^{\natural}=|q|^2=q_t^2+q_x^2+q_y^2+q_z^2$, and every nonzero quaternion is invertible with $q^{-1}=q^{\natural}/|q|^2$. The algebra is identified with $\mathbb{R}^4$ through the basis, and open sets of $\mathbb{H}$ with open sets of $\mathbb{R}^4$.

**Definition.** The **Fueter operator** and its conjugate are

$$
\bar\partial = \partial/\partial Q_t+\sum_{\mu\in\{x,y,z\}}\vec e_\mu\,\partial/\partial Q_\mu , \qquad \partial = \partial/\partial Q_t-\sum_{\mu\in\{x,y,z\}}\vec e_\mu\,\partial/\partial Q_\mu .
$$

They act on a $C^1$ function $f:\Omega\to\mathbb{H}$ on the left, $\bar\partial f = \partial/\partial Q_tf+\sum_{\mu\in\{x,y,z\}}\vec e_\mu\,\partial/\partial Q_\mu\,f$. The function $f$ is **left regular** (Fueter regular) if $\bar\partial f=0$ and **right regular** if $f\bar\partial=0$, the operator acting on the right.

**Proposition (factorisation and ellipticity).** $\bar\partial\partial=\partial\bar\partial=\Delta$ and the symbol $\sigma(\xi)=\xi_t+\sum_{\mu\in\{x,y,z\}}\vec e_\mu\xi_\mu$ is invertible for every $\xi\neq0$, with $\sigma(\xi)^{-1}=\bar\sigma(\xi)/|\xi|^2$ and $\bar\sigma(\xi)=\xi_t-\sum_{\mu\in\{x,y,z\}}\vec e_\mu\xi_\mu$.

*Proof.* The computation is the one of *Regularity and the Cauchy–Riemann Operator* with $B_\mu=\vec e_\mu$; the diagonal terms of $\bar\partial\partial$ give $\partial^2/\partial Q_t^2+\sum_{\mu\in\{x,y,z\}}\partial^2/\partial Q_\mu^2$ and the off-diagonal terms cancel by $\vec e_\mu\vec e_\nu=-\vec e_\nu\vec e_\mu$. For the symbol, $\sigma(\xi)\bar\sigma(\xi)=\xi_t^2+\sum_i\xi_\mu^2=|\xi|^2$, a positive real number and hence a unit, and the two factors commute with the product because $\xi_t$ is real and central.

**Remark (the place of the Fueter operator).** The pair $(\mathbb{H},\bar\partial)$ is the hypercomplex system of *Hypercomplex Analysis* whose value algebra is $\mathbb{H}$ and whose frame is $(e_t,\vec e_x,\vec e_y,\vec e_z)$; the operator is the Cauchy–Riemann operator with coefficients the imaginary units. In the notation of *Clifford Analysis* this is the case $m=3$ with $\mathcal{S}=\mathbb{H}$; the classical quaternionic analysis differs from that article only in the sign convention for the operator, the two operators $\bar\partial$ and $\partial$ exchanging roles. The general results on ellipticity, real-analyticity, the Cauchy transform and residues apply without change.

### Elementary Properties and Examples

**Proposition (structure of the regular functions).** The left regular functions on a domain $\Omega$ form a real vector space and a right $\mathbb{H}$-module: if $f$ is left regular and $a\in\mathbb{H}$ then $af$ need not be regular, while $fa$ and $f+a$ are. The right regular functions form a left $\mathbb{H}$-module. Conjugation exchanges the two classes: $f$ is left regular if and only if $f^{\natural}$ is right regular for $\bar\partial$.

*Proof.* The vector-space and module statements follow from the linearity of $\bar\partial$ over the constants on the right and from $\bar\partial(fa)=(\bar\partial f)a$, which holds because $a$ is constant. For the exchange of sides, apply the involution: $(\bar\partial f)^{\natural}=\sum_{\mu\in\{t,x,y,z\}}\partial/\partial Q_\mu\,f^{\natural}\,e_\mu^{\natural}$, with $e_t^{\natural}=e_t$ and $\vec e_\mu^{\natural}=-\vec e_\mu$; this is the right-action statement of *Regularity and the Cauchy–Riemann Operator*.

**Example (constants and the Fueter variables).** Constants are regular, and the functions

$$
z_\mu = q_t\vec e_\mu - q_\mu , \qquad \mu \in \{x,y,z\} ,
$$

are regular: for such a function $\partial/\partial Q_t z_\mu=\vec e_\mu$ and $\partial/\partial Q_\mu z_\mu=-1$, all other derivatives vanishing, so $\bar\partial z_\mu=\vec e_\mu+\vec e_\mu(-1)=0$. These are the **Fueter variables**. They are linear in $q$ and independent, and together with their left multiples $az_\mu$ they span the space $\mathcal{M}_1$ of linear regular functions, of real dimension $12$; the dimension is read off from the Fischer decomposition of *Clifford Analysis*, $\dim\mathcal{M}_1=\dim\mathcal{P}_1-\dim\mathcal{P}_0=4\cdot 4-4=12$, and the three families $az_\mu$ also give $12$ real parameters.

**Example (the coordinate functions).** No coordinate function and no constant multiple of $q=q_t+\vec q$ is regular: $\bar\partial q=\partial/\partial Q_tq+\sum_{\mu\in\{x,y,z\}}\vec e_\mu\,\partial/\partial Q_\mu\,q=1-\sum_{\mu\in\{x,y,z\}}\vec e_\mu^2=1-3=-2$. The contrast with the complex case, where $z$ is regular, is the first sign that the quaternionic theory is not a naive copy of the complex one; the regular linear functions are the Fueter variables $z_\mu$ and not the coordinates.

**Example (regular functions from the complex subalgebra).** Let $u\in\mathbb{R}^3$ be a unit vector, write $q_u=\langle\vec q,u\rangle$ for the real coordinate along $u$, and put $\zeta=q_t+uq_u$. Then $u$ and $\zeta$ commute, $\partial/\partial Q_t\zeta=1$, and $\partial/\partial Q_\mu\zeta=uu_\mu$, so

$$
\bar\partial\zeta = 1+\sum_{\mu\in\{x,y,z\}}\vec e_\mu\,uu_\mu = 1+u\sum_{\mu\in\{x,y,z\}}u_\mu\vec e_\mu = 1+u^2 = 0 ,
$$

using $\sum_{\mu\in\{x,y,z\}}u_\mu\vec e_\mu=u$ and $u^2=-1$. Hence $\zeta$ is regular, and so is $\zeta^k$ for every $k$, since $\bar\partial\zeta^k=k\zeta^{k-1}\bar\partial\zeta=0$. The plane spanned by $1$ and $u$ therefore carries a copy of $\mathbb{C}$ whose holomorphic functions are regular. These are the **reduced** or **plane** regular functions, and they are the functions from which Fueter's theorem constructs all regular functions.

**Theorem (regularity consequences).** Every left regular function is real-analytic and its four components are harmonic. Hence a regular function satisfies the mean value property

$$
f(q) = \frac{1}{|S^3|r^3}\int_{S(q,r)}f(p)\,dS(p) , \qquad S(q,r)\subseteq\Omega ,
$$

the maximum principle on a connected domain, Liouville's theorem on $\mathbb{R}^4$, and the identity theorem.

*Proof.* If $\bar\partial f=0$ then $\Delta f=\partial\bar\partial f=0$, so each component is harmonic; harmonic functions are real-analytic, satisfy the spherical mean value property and the maximum principle, and a bounded harmonic function on $\mathbb{R}^4$ is constant.

**Remark (the Cauchy–Riemann–Fueter system).** Written in components, the single equation $\bar\partial f=0$ is the system of four real first-order equations

$$
\partial/\partial Q_t f_t-\sum_{\mu\in\{x,y,z\}}\partial/\partial Q_\mu f_\mu = 0, \qquad \partial/\partial Q_t f_\mu+\partial/\partial Q_\mu f_t+\sum_{\text{cyclic }(\mu,\nu,\lambda)}\bigl(\partial/\partial Q_\mu f_\nu-\partial/\partial Q_\nu f_\mu\bigr)=0 , \quad \mu\in\{x,y,z\} .
$$

obtained by expanding $f=\sum_{\mu\in\{t,x,y,z\}}f_\mu\,e_\mu$ and $\vec e_\mu\vec e_\nu=\vec e_\lambda$ for cyclic $(\mu,\nu,\lambda)$. The system is elliptic and overdetermined in the sense that its solutions depend on two real functions of two variables in the axial case below; it is the quaternionic form of the Cauchy–Riemann equations, and the form in which Fueter's original construction is stated.

## The Cauchy–Fueter Integral Formula

**Theorem (the Cauchy–Fueter kernel).** The function

$$
E(q) = \frac{1}{2\pi^2}\frac{q^{\natural}}{|q|^4} , \qquad q\neq0 ,
$$

is a fundamental solution of the Fueter operator, $\bar\partial E=\delta_0$, and it is the Cauchy kernel of the theory.

*Proof.* The kernel is the case $m=3$ of the general kernel of *Clifford Analysis*: with $\Phi$ a fundamental solution of the Laplacian one has $\bar\partial(\partial\Phi)=\Delta\Phi=\delta_0$, so $\partial\Phi$ is a fundamental solution of $\bar\partial$, and the constant is fixed by $\omega_3=|S^3|=2\pi^2$ and by the homogeneity $-4$ of the kernel. Equivalently, one verifies directly that $\bar\partial E=0$ away from the origin and that the flux of $E$ through a small sphere about the origin is $1$.

**Theorem (Cauchy–Fueter integral formula).** Let $\Omega\subseteq\mathbb{H}$ be a bounded domain with smooth boundary, let $\nu_B=\sum_{\mu\in\{t,x,y,z\}}\nu_\mu e_\mu$ where $(\nu_t,\dots,\nu_z)$ is the outward unit normal, and let $f$ be left regular on a neighbourhood of $\bar\Omega$. Then for $q\in\Omega$,

$$
f(q) = \frac{1}{2\pi^2}\int_{\partial\Omega}\frac{(p-q)^{\natural}}{|p-q|^4}\,\nu_B(p)\,f(p)\,dS(p) .
$$

Moreover, for $f$ of class $C^1$ on $\bar\Omega$ the **Cauchy–Fueter–Pompeiu formula**

$$
f(q) = \frac{1}{2\pi^2}\int_{\partial\Omega}\frac{(p-q)^{\natural}}{|p-q|^4}\,\nu_B(p)\,f(p)\,dS(p) - \frac{1}{2\pi^2}\int_\Omega\frac{(p-q)^{\natural}}{|p-q|^4}\,(\bar\partial f)(p)\,dp
$$

holds, and it reduces to the preceding statement when $f$ is regular.

*Proof.* The formula is the quaternionic case of the general Cauchy–Pompeiu formula of *Hypercomplex Analysis*, with the kernel of the preceding theorem. It is proved by excising a small ball about $q$, applying the quaternionic form of the divergence theorem to the punctured domain, and letting the radius tend to zero, the boundary term over the small sphere contributing $f(q)$ by the mean value property of the harmonic components.

**Corollary (Cauchy estimates).** For $B(q,r)\subseteq\Omega$ and $f$ left regular,

$$
\|f(q)\|\le\frac{1}{2\pi^2r^3}\int_{\partial B(q,r)}\|f(p)\|\,dS(p)\le\sup_{\partial B(q,r)}\|f\| ,
$$

using $\int_{\partial B(q,r)}dS=2\pi^2r^3$.

**Remark (the other formulæ).** The Cauchy transform $\mathcal{C}h(q)=\frac{1}{2\pi^2}\int_{\partial\Omega}\frac{(p-q)^{\natural}}{|p-q|^4}\nu_B(p)h(p)dS(p)$ maps a boundary datum to a regular function inside, and the jump formula $\mathcal{C}^+h-\mathcal{C}^-h=h$ recovers the density; both are the quaternionic instances of the general statements of the hypercomplex theory, whose integration theory is the subject , with the kernel here specialised to the quaternionic case. The Hardy space of boundary values of regular functions and the projection onto it are likewise the general theory's, and the explicit kernel makes the small-sphere residues of the quaternionic theory computable: the residue of $E$ at the origin is $1$ in the normalisation of the kernel.

## Fueter's Theorem

The construction that connects complex analysis to the quaternionic theory is not the substitution of a quaternion for the complex variable; it is the radial extension of a holomorphic function followed by the Laplacian. Write a point of $\mathbb{H}$ as $q=q_t+\vec q$ with $r=|\vec q|$, and for a function $g(x,y)$ of two real variables define its **axial extension**

$$
g^{\mathrm{ax}}(q) = g(q_t,r) .
$$

This extension is constant on every sphere $\{q_t\}\times S^2_{r}$ about the real axis, and it is well defined away from the axis $\vec q=0$ together with the derivatives that occur below.

**Theorem (Fueter).** Let $f=u+iv$ be holomorphic on a domain $\Omega\subseteq\mathbb{C}$, and define

$$
f^{\mathrm{ax}}(q) = u(q_t,r) + \frac{\vec q}{r}\,v(q_t,r) , \qquad |\vec q| = r .
$$

Then the function

$$
F(q) = \Delta f^{\mathrm{ax}}(q)
$$

is left and right regular at every point where $f^{\mathrm{ax}}$ is defined and $r\neq0$. For $f(z)=z^n$ the resulting function is regular and homogeneous of degree $n-2$; in particular $f(z)=1$ and $f(z)=z$ give $F=0$, and the construction is an isomorphism from the holomorphic functions onto the axial regular functions modulo the two lowest degrees.

*Proof.* Quoted as standard (Fueter 1935; see also the treatments of Sudbery and of Colombo–Sabadini–Struppa). The verification is a computation in the axial coordinates of the next section: writing a regular function in the form $A(q_t,r)+\vec qB(q_t,r)$ leads to the pair of equations $\partial A/\partial q_t=3B+r\,\partial B/\partial r$, $\partial B/\partial q_t=-(\partial A/\partial r)/r$, and the Cauchy–Riemann equations for $f=u+iv$ together with the radial form of the Laplacian show that $A,B$ built from $u,v$ by $\Delta$ satisfy this pair.

**Example (the verification in low degree).** For $f(z)=z^2$ one has $u=q_t^2-r^2$, $v=2q_tr$, so $f^{\mathrm{ax}}=q_t^2-r^2+2q_t\vec q$ and, using $\Delta(q_t^2-r^2)=2-6=-4$ in $\mathbb{R}^4$ and $\Delta(2q_tq_\mu)=0$ for each $i$, the function $F=-4$ is a nonzero constant, hence regular. For $f(z)=z^3$ one has $u=q_t^3-3q_tr^2$, $v=3q_t^2r-r^3$, hence $f^{\mathrm{ax}}=q_t^3-3q_tr^2+\vec q(3q_t^2-r^2)$; now $\Delta(q_t^3-3q_tr^2)=6q_t-18q_t=-12q_t$ and, componentwise, $\Delta(q_\mu(3q_t^2-r^2))=-4q_\mu$, so

$$
F = -12q_t-4\vec q ,
$$

which is regular of degree $1$: indeed $F=A+\vec qB$ with $A=-12q_t$, $B=-4$, and the axial equations give $-12=-12$ and $0=0$. The two examples exhibit the degree shift by two and the vanishing on the constants and the identity.

**Remark (why the Laplacian is necessary).** The axial extension $f^{\mathrm{ax}}$ itself is not regular in general: for $f(z)=z^3$, $\bar\partial f^{\mathrm{ax}}=(\partial A/\partial q_t-3B-r\partial B/\partial r)+(\partial B/\partial q_t+(\partial A/\partial r)/r)\vec q$ with $A=q_t^3-3q_tr^2$, $B=3q_t^2-r^2$, and neither bracket vanishes. The theorem says that the obstruction is exactly the one removed by the Laplacian. This is the structural difference between the complex and the quaternionic theory: holomorphic functions of one variable correspond not to regular functions but to regular functions after a second-order operator has been applied, and the correspondence loses the two lowest homogeneities.

**Remark (the symmetry behind the construction).** The orthogonal group $SO(3)$ acts on the imaginary part of $q$ and fixes the real part; it acts on the regular functions by $f\mapsto f\circ T^{-1}$, $T\in SO(3)$, and the axial functions are exactly the fixed points of this action. Fueter's theorem is therefore the statement that the invariant part of the quaternionic theory is a copy of complex analysis, while the full theory is the orbit of that invariant part under the rotation group. The rotation group itself, the spin cover and the quaternionic description of rotations are Part II's, and the symmetry statement above is the analytic form of the same structure.

## Axial Functions and the Reduced Equations

The construction of the last section is best understood through the class of functions it produces.

**Definition.** A function $f$ on a domain of $\mathbb{H}$ not meeting the real axis is **axial** if it has the form

$$
f(q) = A(q_t,r)+\vec q\,B(q_t,r) , \qquad r=|\vec q| ,
$$

with $A,B$ real-valued functions of two variables.

**Proposition (the axial regularity equations).** The axial function $f=A+\vec qB$ is left regular if and only if the pair

$$
\partial A/\partial q_t = 3B+r\partial B/\partial r , \qquad \partial B/\partial q_t = -\frac{\partial A/\partial r}{r}
$$

holds on the domain.

*Proof.* Compute $\bar\partial f$ term by term. The scalar derivatives give $\partial/\partial Q_tf=\partial A/\partial q_t+\vec q\partial B/\partial q_t$, and the vector derivatives give $\sum_{\mu\in\{x,y,z\}}\vec e_\mu\,\partial/\partial Q_\mu\,A = r^{-1}\partial A/\partial r\vec q$ and

$$
\sum_{\mu\in\{x,y,z\}}\vec e_\mu\,\partial/\partial Q_\mu(\vec qB) = -3B-r\partial B/\partial r ,
$$

the second identity following from $\vec e_\mu\vec q\,q_\mu$ summed over $i$, which equals $-r^2$, together with $\vec e_\mu\cdot\vec e_\mu=-1$. Collecting the scalar and the vector parts gives

$$
\bar\partial f = \bigl(\partial A/\partial q_t-3B-r\partial B/\partial r\bigr)+\Bigl(\partial B/\partial q_t+\frac{\partial A/\partial r}{r}\Bigr)\vec q ,
$$

and this vanishes exactly when both brackets do.

**Corollary (the reduced Cauchy–Riemann system).** Writing $A=\phi$ and $B=\psi/r$ for real-valued $\phi,\psi$ of $(q_t,r)$ turns the pair into

$$
\phi_0 = \psi_r+\frac{2\psi}{r} , \qquad \psi_0 = -\phi_r ,
$$

the reduced Cauchy–Riemann system of the axial theory. The solutions are exactly the axial regular functions, and Fueter's theorem says that every holomorphic function of the reduced variable $\zeta=q_t+ir$ produces one through $F=\Delta f^{\mathrm{ax}}$; this is the precise sense in which complex analysis sits inside the quaternionic theory as its rotation-invariant part.

*Proof.* Substituting $A=\phi$, $B=\psi/r$ into $\partial A/\partial q_t=3B+r\partial B/\partial r$ gives $\phi_0=3\psi/r+r(\psi_r/r-\psi/r^2)=\psi_r+2\psi/r$, and substituting into $\partial B/\partial q_t=-(\partial A/\partial r)/r$ gives $\psi_0/r-\psi/r^2\cdot0=-\phi_r/r$, that is $\psi_0=-\phi_r$. For the worked example $F=-12q_t-4\vec q$ one has $\phi=-12q_t$, $\psi=-4r$, and the pair reads $-12=-4-8$ and $0=0$.

**Example (the radial regular functions).** Taking $A=0$, the pair requires $3B+r\partial B/\partial r=0$, so $B=cr^{-3}$; the function $f(q)=\vec q\,r^{-3}$ is regular away from the axis and is, up to the constant, the vector part of the Cauchy–Fueter kernel. Taking $B=0$ requires $\partial A/\partial r=0$, so $A=A(q_t)$, an arbitrary function of the real variable; the function $f=A(q_t)$ is regular, the "plane" regular functions of the real axis. These two families are the extreme axial cases and the building blocks of the general axial solution.

## Series Expansions and the Fueter Polynomials

**Theorem (Taylor-type expansion).** Every function left regular on a neighbourhood of the origin has a unique expansion

$$
f(q) = \sum_{k\ge0}\;\sum_{\lambda} a_\lambda\,V_\lambda(q) , \qquad a_\lambda\in\mathbb{H} ,
$$

convergent on the ball of regularity, where $V_\lambda$ runs over the **Fueter polynomials**: the symmetrised products

$$
V_{\lambda_1\dots\lambda_k}(q) = \frac{1}{k!}\sum_{\sigma\in S_k}z_{\lambda_{\sigma(1)}}\cdots z_{\lambda_{\sigma(k)}} ,
$$

of the Fueter variables $z_t=q_t$, $z_\mu=q_t\vec e_\mu-q_\mu$ $(\mu\in\{x,y,z\})$, taken over the proper multi-indices of the theory; these polynomials form a basis of the space of homogeneous regular polynomials of degree $k$.

*Pro.* Quoted as standard (Fueter; Sudbery). The expansion is the quaternionic instance of the general power-series expansion of the hypercomplex theory, whose integration theory is not treated here, and the explicit basis is the classical Fueter basis; the homogeneity and the regularity of the symmetrised products follow from the Leibniz rule for $\bar\partial$ and the regularity of the $z_\mu$.

**Remark (what the expansion does and does not give).** The expansion makes the regular functions a class as rigid as the holomorphic ones — a regular function on a ball is determined by its coefficients, and the Cauchy–Fueter formula computes them by small-sphere integrals — but the class is not closed under multiplication, since the product of two of the linear regular functions $z_\mu$ need not be regular; this is the failure recorded in *Hypercomplex Analysis* and *Clifford Analysis*, and it is the reason the theory has a basis but no algebra of regular functions. The dimension of the homogeneous piece is read from the Fischer decomposition of *Clifford Analysis*; for the quaternionic case it is $\dim\mathcal{M}_k=4[\binom{3+k}{k}-\binom{2+k}{k-1}]$, and the Fueter polynomials enumerate it.

**Example (the low pieces).** For $k=0$ the expansion is the constant term. For $k=1$ it is $\sum_{\mu\in\{x,y,z\}}a_\mu z_\mu$, the span of the Fueter variables, of real dimension $12$; the polynomials $z_\mu$ are the linear regular functions, while $q$ itself is not regular. For $k=2$ the Fischer decomposition gives $\dim\mathcal{M}_2=24$, and the piece contains the powers $z_\mu^2$ of the Fueter variables, which are the plane-regular functions of the subalgebra generated by $e_t$ and $\vec e_\mu$; a product $z_\mu z_\nu$ with $\mu\neq\nu$ is not regular, so the class fails to be an algebra already at degree two.

## The Axial and Slice Points of View

**Remark (the two descriptions).** The axial description of the preceding section describes the functions that are invariant under the rotations of the imaginary part of $q$; it is the description in which complex analysis appears inside the quaternionic theory. The **slice** description starts instead from the observation that $\mathbb{H}=\bigcup_{i\in S^2}\mathbb{C}_i$ is the union of the complex planes $\mathbb{C}_i=\mathbb{R}+i\mathbb{R}$, one for each imaginary unit $i$, and calls a function regular if it is holomorphic on each slice $\mathbb{C}_i$ and the slices fit together with a compatibility condition. The two descriptions agree on their common domain: a slice-regular function that is also axial is an axial regular function, and Fueter's theorem is then the correspondence with the holomorphic functions of the reduced variable. The slice theory has its own power series, its own Cauchy formula and its own class of "slice" regular functions that need not be Fueter-regular; it is a theory of Part V, where it is developed for the quaternions and for the biquaternions, and carries the biquaternionic case and the explicit power series. Here the axial formulation is the one used, and the slice formulation is mentioned only to delimit it.

**Remark (the biquaternionic and other systems).** Replacing the real coefficients of the quaternion algebra by complex ones gives the biquaternions $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$; the Fueter operator is defined by the same formula, the Cauchy kernel acquires a different normalisation because the algebra has zero divisors, and the class of regular functions is larger in some directions and smaller in others. The biquaternionic function theory, its Fueter operator and its regular functions are treated in Part V; the split quaternionic case is treated there too. What carries over from this article is the operator, the factorisation, the Cauchy kernel and Fueter's theorem; what changes is the value algebra and the structure of its zero-divisor set.

## Summary

The Fueter operator $\bar\partial=\partial/\partial Q_t+\vec e_x\partial/\partial Q_x+\vec e_y\partial/\partial Q_y+\vec e_z\partial/\partial Q_z$ and its conjugate $\partial$ factor the Laplacian of $\mathbb{R}^4$, $\bar\partial\partial=\partial\bar\partial=\Delta$, and are elliptic, with symbol $\sigma(\xi)=\xi_t+\sum_{\mu\in\{x,y,z\}}\vec e_\mu\xi_\mu$ and inverse $\bar\sigma(\xi)/|\xi|^2$. A function is left regular when $\bar\partial f=0$; the left regular functions form a real vector space and a right $\mathbb{H}$-module, conjugation exchanges left and right regularity, and every regular function is real-analytic with harmonic components, so the mean value property, the maximum principle, Liouville's theorem and the identity theorem hold. The linear regular functions are the Fueter variables $z_\mu=q_t\vec e_\mu-q_\mu$, spanning a space of real dimension $12$. The fundamental solution is the Cauchy–Fueter kernel $E(q)=\frac{1}{2\pi^2}q^{\natural}|q|^{-4}$, and it yields the Cauchy–Fueter formula $f(q)=\frac{1}{2\pi^2}\int_{\partial\Omega}(p-q)^{\natural}|p-q|^{-4}\nu_B(p)f(p)dS(p)$, the Cauchy–Fueter–Pompeiu formula for non-regular functions, the Cauchy estimates on balls and the jump and projection statements of the general theory. **Fueter's theorem** constructs regular functions from holomorphic ones: the axial extension $f^{\mathrm{ax}}=u(q_t,r)+\frac{\vec q}{r}v(q_t,r)$ of a holomorphic $f=u+iv$ is not regular, but its Laplacian $F=\Delta f^{\mathrm{ax}}$ is, the construction shifting homogeneity by two and killing the constants and the identity. The axial regular functions $A(q_t,r)+\vec qB(q_t,r)$ are exactly those solving the pair $\partial A/\partial q_t=3B+r\,\partial B/\partial r$, $\partial B/\partial q_t=-(\partial A/\partial r)/r$, which is a Cauchy–Riemann system in the reduced variables $(q_t,r)$, and every regular function on a ball has a Taylor expansion in the homogeneous monogenic pieces $\mathcal{M}_k$, whose standard bases are the Fueter polynomials $V_\lambda$ and whose coefficients are computed by the Cauchy–Fueter formula. The class is rigid but not an algebra: products of regular functions need not be regular. The general operator theory is *Clifford Analysis* and *Regularity and the Cauchy–Riemann Operator*; the slice description and the biquaternionic, split-biquaternionic and other value algebras are Part V.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | Real quaternions, basis $e_t,\vec e_x,\vec e_y,\vec e_z$ |
| $q=q_t+\vec q$ | Quaternionic variable; $\vec q=q_x\vec e_x+q_y\vec e_y+q_z\vec e_z$ |
| $q^{\natural}$, $\langle q\rangle_{\natural}=|q|^2$ | Quaternionic conjugation and norm |
| $\bar\partial=\partial/\partial Q_t+\sum_{\mu\in\{x,y,z\}}\vec e_\mu\,\partial/\partial Q_\mu$ | Fueter operator |
| $\partial=\partial/\partial Q_t-\sum_{\mu\in\{x,y,z\}}\vec e_\mu\,\partial/\partial Q_\mu$ | Conjugate; $\bar\partial\partial=\partial\bar\partial=\Delta$ |
| $\sigma(\xi)$, $\bar\sigma(\xi)$ | Symbol and conjugate symbol of $\bar\partial$ |
| $\bar\partial f=0$, $f\bar\partial=0$ | Left and right Fueter regularity |
| $z_\mu=q_t\vec e_\mu-q_\mu$ | Fueter variables |
| $E(q)=\frac{1}{2\pi^2}q^{\natural}|q|^{-4}$ | Cauchy–Fueter kernel; $\bar\partial E=\delta_0$ |
| $\nu_B=\sum_\alpha\nu_\alpha e_\alpha$ | Conormal element |
| $f^{\mathrm{ax}}$ | Axial (radial) extension of $f$ |
| $F=\Delta f^{\mathrm{ax}}$ | Fueter construction |
| $A(q_t,r)+\vec qB(q_t,r)$ | Axial form of a regular function |
| $r=|\vec q|$, $\zeta=q_t+ir$ | Radial coordinate and reduced complex variable |
| $V_\lambda$ | Fueter polynomials; $\mathcal{M}_k$ homogeneous regular polynomials |
| $\mathcal{C}$ | Cauchy transform |





## Further Reading

- R. Fueter, "Die Funktionentheorie der Differentialgleichungen $\Delta u=0$ und $\Delta\Delta u=0$ mit vier reellen Variablen", *Commentarii Mathematici Helvetici* 7 (1935), 307–330, for the original definition of regularity and the construction from holomorphic functions.
- A. Sudbery, "Quaternionic Analysis", *Mathematical Proceedings of the Cambridge Philosophical Society* 85 (1979), 199–225, for Fueter's theorem, the Fueter variables and the Taylor expansion.
- F. Brackx, R. Delanghe and F. Sommen, *Clifford Analysis* (Pitman, 1982), for the four-dimensional case inside the general Clifford theory.
- R. Delanghe, F. Sommen and V. Souček, *Clifford Algebra and Spinor-Valued Functions* (Kluwer, 1992), for the Cauchy kernel, the spherical monogenics and the integral representation.
- Fabrizio Colombo, Irene Sabadini and Daniele C. Struppa, *Noncommutative Functional Calculus* (Birkhäuser, 2011), for the modern treatment of regular functions and the axial and slice descriptions.
- Graziano Gentili, Caterina Stoppato and Daniele C. Struppa, *Regular Functions of a Quaternionic Variable* (Springer, 2013), for the slice point of view and its power series.
- Klaus Gürlebeck and Wolfgang Sprößig, *Quaternionic and Clifford Calculus for Physicists and Engineers* (Wiley, 1997), for the Cauchy–Fueter formula and its boundary-value applications.
- Anthony K. G. Rose, "Quaternionic Functions and the Fueter Construction" (unpublished notes and papers), for detailed computations of the Fueter construction in low degree.
