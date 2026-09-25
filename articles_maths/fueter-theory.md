
# __Fueter Theory__

## Introduction

Fueter theory is the function theory of a quaternionic variable built from a first-order operator. Its subject is a function $f:\Omega\to\mathbb{H}$ of a quaternion $q=q_0+q_1e_1+q_2e_2+q_3e_3$, and its basic notion is that of a **regular** function: one annihilated by the **Fueter operator**

$$
\bar\partial = \partial_0+e_1\partial_1+e_2\partial_2+e_3\partial_3 ,
$$

the conjugate of which, $\partial=\partial_0-e_1\partial_1-e_2\partial_2-e_3\partial_3$, satisfies $\bar\partial\partial=\partial\bar\partial=\Delta$, the Laplacian of $\mathbb{R}^4$. The theory was introduced by Fueter in 1935 as the quaternionic analogue of complex analysis: the aim was a class of functions with a Cauchy integral formula, a power-series expansion and a Cauchy–Riemann system. The class is the quaternionic instance of the monogenic functions of *Clifford Analysis*, so the general operator theory is not repeated here; what this article develops is what is specific to the quaternionic case, and the article states at each point which of its results is an instance of the general theory and which is peculiar to four dimensions.

Three features organise the article. The first is the **Cauchy–Fueter integral formula**, $f(q)=\frac{1}{2\pi^2}\int_{\partial\Omega}\frac{\overline{(p-q)}}{|p-q|^4}\,\nu_B(p)f(p)\,dS(p)$, the quaternionic form of the general Cauchy formula, whose kernel is the fundamental solution of the Fueter operator. The second is **Fueter's theorem**, the construction that produces regular functions from holomorphic functions of one complex variable: the radial extension of a holomorphic function is not regular, but its Laplacian is, and the construction shifts the homogeneity by two. This theorem is the reason the quaternionic theory is a genuine generalisation of complex analysis rather than a formal analogue, and it is the result that the per-system theories generalise. The third is the **axial** description of the functions that the construction produces: a regular function constant on the spheres about the real axis is determined by two real functions of two variables satisfying a pair of equations, and Fueter's theorem is the statement that these are the equations of a holomorphic function in disguise.

The boundaries are these. The general hypercomplex theory — left and right regularity, the symbol, ellipticity, the Cauchy transform, the per-system value spaces — is in *Hypercomplex Analysis* and *Regularity and the Cauchy–Riemann Operator*, and is cited; the integration theory of that general setting is not covered here. The Clifford-algebra formulation, the Fischer decomposition and the polymonogenic functions are in *Clifford Analysis*, the immediately preceding article, and are used there. The quaternionic analyses of the other systems — the biquaternionic case, the split-biquaternionic case, the slice theory with its own power series — belong to Part V and are cited as the places where the system-specific statements are proved. The article is mathematics: no physical reading of $\mathbb{R}^4$ is used.

## The Fueter Operator and Regularity

### The Algebra and the Operator

Let $\mathbb{H}$ be the real quaternion algebra, with basis $1,e_1,e_2,e_3$ and relations $e_i^2=-1$, $e_ie_j=-e_je_i$ for $i\neq j$, and $e_1e_2=e_3$. A quaternion is written $q=q_0+\vec q$, $q_0\in\mathbb{R}$, $\vec q=q_1e_1+q_2e_2+q_3e_3$; its conjugate is $\bar q=q_0-\vec q$, its norm is $N(q)=q\bar q=|q|^2=q_0^2+q_1^2+q_2^2+q_3^2$, and every nonzero quaternion is invertible with $q^{-1}=\bar q/|q|^2$. The algebra is identified with $\mathbb{R}^4$ through the basis, and open sets of $\mathbb{H}$ with open sets of $\mathbb{R}^4$.

**Definition.** The **Fueter operator** and its conjugate are

$$
\bar\partial = \partial_0+\sum_{i=1}^{3}e_i\partial_i , \qquad \partial = \partial_0-\sum_{i=1}^{3}e_i\partial_i .
$$

They act on a $C^1$ function $f:\Omega\to\mathbb{H}$ on the left, $\bar\partial f = \partial_0f+\sum_ie_i\partial_if$. The function $f$ is **left regular** (Fueter regular) if $\bar\partial f=0$ and **right regular** if $f\bar\partial=0$, the operator acting on the right.

**Proposition (factorisation and ellipticity).** $\bar\partial\partial=\partial\bar\partial=\Delta$ and the symbol $\sigma(\xi)=\xi_0+\sum_ie_i\xi_i$ is invertible for every $\xi\neq0$, with $\sigma(\xi)^{-1}=\bar\sigma(\xi)/|\xi|^2$ and $\bar\sigma(\xi)=\xi_0-\sum_ie_i\xi_i$.

*Proof.* The computation is the one of *Regularity and the Cauchy–Riemann Operator* with $B_i=e_i$; the diagonal terms of $\bar\partial\partial$ give $\partial_0^2+\sum_i\partial_i^2$ and the off-diagonal terms cancel by $e_ie_j=-e_je_i$. For the symbol, $\sigma(\xi)\bar\sigma(\xi)=\xi_0^2+\sum_i\xi_i^2=|\xi|^2$, a positive real number and hence a unit, and the two factors commute with the product because $\xi_0$ is real and central. $\square$

**Remark (the place of the Fueter operator).** The pair $(\mathbb{H},\bar\partial)$ is the hypercomplex system of *Hypercomplex Analysis* whose value algebra is $\mathbb{H}$ and whose frame is $(1,e_1,e_2,e_3)$; the operator is the Cauchy–Riemann operator with coefficients the imaginary units. In the notation of *Clifford Analysis* this is the case $m=3$ with $\mathcal{S}=\mathbb{H}$; the classical quaternionic analysis differs from that article only in the sign convention for the operator, the two operators $\bar\partial$ and $\partial$ exchanging roles. The general results on ellipticity, real-analyticity, the Cauchy transform and residues apply without change.

### Elementary Properties and Examples

**Proposition (structure of the regular functions).** The left regular functions on a domain $\Omega$ form a real vector space and a right $\mathbb{H}$-module: if $f$ is left regular and $a\in\mathbb{H}$ then $af$ need not be regular, while $fa$ and $f+a$ are. The right regular functions form a left $\mathbb{H}$-module. Conjugation exchanges the two classes: $f$ is left regular if and only if $\bar f$ is right regular for $\bar\partial$.

*Proof.* The vector-space and module statements follow from the linearity of $\bar\partial$ over the constants on the right and from $\bar\partial(fa)=(\bar\partial f)a$, which holds because $a$ is constant. For the exchange of sides, apply the involution: $\overline{\bar\partial f}=\sum_i\partial_i\bar f\,\bar e_i$ for $i=0,1,2,3$ with $e_0=1$, and $\bar e_0=1$, $\bar e_i=-e_i$; this is the right-action statement of *Regularity and the Cauchy–Riemann Operator*. $\square$

**Example (constants and the Fueter variables).** Constants are regular, and the functions

$$
z_i = q_0e_i - q_i , \qquad i = 1,2,3 ,
$$

are regular: for such a function $\partial_0z_i=e_i$ and $\partial_iz_i=-1$, all other derivatives vanishing, so $\bar\partial z_i=e_i+e_i(-1)=0$. These are the **Fueter variables**. They are linear in $q$ and independent, and together with their left multiples $az_i$ they span the space $\mathcal{M}_1$ of linear regular functions, of real dimension $12$; the dimension is read off from the Fischer decomposition of *Clifford Analysis*, $\dim\mathcal{M}_1=\dim\mathcal{P}_1-\dim\mathcal{P}_0=4\cdot 4-4=12$, and the three families $az_i$ also give $12$ real parameters.

**Example (the coordinate functions).** No coordinate function and no constant multiple of $q=q_0+\vec q$ is regular: $\bar\partial q=\partial_0q+\sum_ie_i\partial_iq=1-\sum_ie_i^2=1-3=-2$. The contrast with the complex case, where $z$ is regular, is the first sign that the quaternionic theory is not a naive copy of the complex one; the regular linear functions are the Fueter variables $z_i$ and not the coordinates.

**Example (regular functions from the complex subalgebra).** Let $u\in\mathbb{R}^3$ be a unit vector, write $q_u=\langle\vec q,u\rangle$ for the real coordinate along $u$, and put $\zeta=q_0+uq_u$. Then $u$ and $\zeta$ commute, $\partial_0\zeta=1$, and $\partial_i\zeta=uu_i$, so

$$
\bar\partial\zeta = 1+\sum_{i=1}^3e_i\,uu_i = 1+u\sum_{i=1}^3u_ie_i = 1+u^2 = 0 ,
$$

using $\sum_iu_ie_i=u$ and $u^2=-1$. Hence $\zeta$ is regular, and so is $\zeta^k$ for every $k$, since $\bar\partial\zeta^k=k\zeta^{k-1}\bar\partial\zeta=0$. The plane spanned by $1$ and $u$ therefore carries a copy of $\mathbb{C}$ whose holomorphic functions are regular. These are the **reduced** or **plane** regular functions, and they are the functions from which Fueter's theorem constructs all regular functions.

**Theorem (regularity consequences).** Every left regular function is real-analytic and its four components are harmonic. Hence a regular function satisfies the mean value property

$$
f(q) = \frac{1}{|S^3|r^3}\int_{S(q,r)}f(p)\,dS(p) , \qquad S(q,r)\subseteq\Omega ,
$$

the maximum principle on a connected domain, Liouville's theorem on $\mathbb{R}^4$, and the identity theorem.

*Proof.* If $\bar\partial f=0$ then $\Delta f=\partial\bar\partial f=0$, so each component is harmonic; harmonic functions are real-analytic, satisfy the spherical mean value property and the maximum principle, and a bounded harmonic function on $\mathbb{R}^4$ is constant. $\square$

**Remark (the Cauchy–Riemann–Fueter system).** Written in components, the single equation $\bar\partial f=0$ is the system of four real first-order equations

$$
\partial_0f_0-\sum_{i=1}^3\partial_if_i = 0, \qquad \partial_0f_k+\partial_kf_0+\sum_{\text{cyclic }(i,j,k)}\bigl(\partial_if_j-\partial_jf_i\bigr)=0 , \quad k=1,2,3 .
$$

obtained by expanding $f=\sum_\alpha f_\alpha e_\alpha$ and $e_ie_j=e_k$ for cyclic $(i,j,k)$. The system is elliptic and overdetermined in the sense that its solutions depend on two real functions of two variables in the axial case below; it is the quaternionic form of the Cauchy–Riemann equations, and the form in which Fueter's original construction is stated.

## The Cauchy–Fueter Integral Formula

**Theorem (the Cauchy–Fueter kernel).** The function

$$
E(q) = \frac{1}{2\pi^2}\frac{\bar q}{|q|^4} , \qquad q\neq0 ,
$$

is a fundamental solution of the Fueter operator, $\bar\partial E=\delta_0$, and it is the Cauchy kernel of the theory.

*Proof.* The kernel is the case $m=3$ of the general kernel of *Clifford Analysis*: with $\Phi$ a fundamental solution of the Laplacian one has $\bar\partial(\partial\Phi)=\Delta\Phi=\delta_0$, so $\partial\Phi$ is a fundamental solution of $\bar\partial$, and the constant is fixed by $\omega_3=|S^3|=2\pi^2$ and by the homogeneity $-4$ of the kernel. Equivalently, one verifies directly that $\bar\partial E=0$ away from the origin and that the flux of $E$ through a small sphere about the origin is $1$. $\square$

**Theorem (Cauchy–Fueter integral formula).** Let $\Omega\subseteq\mathbb{H}$ be a bounded domain with smooth boundary, let $\nu_B=\sum_{\alpha=0}^{3}\nu_\alpha e_\alpha$ where $(\nu_0,\dots,\nu_3)$ is the outward unit normal, and let $f$ be left regular on a neighbourhood of $\bar\Omega$. Then for $q\in\Omega$,

$$
f(q) = \frac{1}{2\pi^2}\int_{\partial\Omega}\frac{\overline{(p-q)}}{|p-q|^4}\,\nu_B(p)\,f(p)\,dS(p) .
$$

Moreover, for $f$ of class $C^1$ on $\bar\Omega$ the **Cauchy–Fueter–Pompeiu formula**

$$
f(q) = \frac{1}{2\pi^2}\int_{\partial\Omega}\frac{\overline{(p-q)}}{|p-q|^4}\,\nu_B(p)\,f(p)\,dS(p) - \frac{1}{2\pi^2}\int_\Omega\frac{\overline{(p-q)}}{|p-q|^4}\,(\bar\partial f)(p)\,dp
$$

holds, and it reduces to the preceding statement when $f$ is regular.

*Proof.* The formula is the quaternionic case of the general Cauchy–Pompeiu formula of *Hypercomplex Analysis*, with the kernel of the preceding theorem. It is proved by excising a small ball about $q$, applying the quaternionic form of the divergence theorem to the punctured domain, and letting the radius tend to zero, the boundary term over the small sphere contributing $f(q)$ by the mean value property of the harmonic components. $\square$

**Corollary (Cauchy estimates).** For $B(q,r)\subseteq\Omega$ and $f$ left regular,

$$
\|f(q)\|\le\frac{1}{2\pi^2r^3}\int_{\partial B(q,r)}\|f(p)\|\,dS(p)\le\sup_{\partial B(q,r)}\|f\| ,
$$

using $\int_{\partial B(q,r)}dS=2\pi^2r^3$.

**Remark (the other formulæ).** The Cauchy transform $\mathcal{C}h(q)=\frac{1}{2\pi^2}\int_{\partial\Omega}\frac{\overline{(p-q)}}{|p-q|^4}\nu_B(p)h(p)dS(p)$ maps a boundary datum to a regular function inside, and the jump formula $\mathcal{C}^+h-\mathcal{C}^-h=h$ recovers the density; both are the quaternionic instances of the general statements of the hypercomplex theory, whose integration theory is the subject , with the kernel here specialised to the quaternionic case. The Hardy space of boundary values of regular functions and the projection onto it are likewise the general theory's, and the explicit kernel makes the small-sphere residues of the quaternionic theory computable: the residue of $E$ at the origin is $1$ in the normalisation of the kernel.

## Fueter's Theorem

The construction that connects complex analysis to the quaternionic theory is not the substitution of a quaternion for the complex variable; it is the radial extension of a holomorphic function followed by the Laplacian. Write a point of $\mathbb{H}$ as $q=q_0+\vec q$ with $r=|\vec q|$, and for a function $g(x,y)$ of two real variables define its **axial extension**

$$
\tilde g(q) = g(q_0,r) .
$$

This extension is constant on every sphere $\{q_0\}\times S^2_{r}$ about the real axis, and it is well defined away from the axis $\vec q=0$ together with the derivatives that occur below.

**Theorem (Fueter).** Let $f=u+iv$ be holomorphic on a domain $\Omega\subseteq\mathbb{C}$, and define

$$
\tilde f(q) = u(q_0,r) + \frac{\vec q}{r}\,v(q_0,r) , \qquad |\vec q| = r .
$$

Then the function

$$
F(q) = \Delta\tilde f(q)
$$

is left and right regular at every point where $\tilde f$ is defined and $r\neq0$. For $f(z)=z^n$ the resulting function is regular and homogeneous of degree $n-2$; in particular $f(z)=1$ and $f(z)=z$ give $F=0$, and the construction is an isomorphism from the holomorphic functions onto the axial regular functions modulo the two lowest degrees.

*Proof.* Quoted as standard (Fueter 1935; see also the treatments of Sudbery and of Colombo–Sabadini–Struppa). The verification is a computation in the axial coordinates of the next section: writing a regular function in the form $A(q_0,r)+\vec qB(q_0,r)$ leads to the pair of equations $A_0=3B+rB_r$, $B_0=-A_r/r$, and the Cauchy–Riemann equations for $f=u+iv$ together with the radial form of the Laplacian show that $A,B$ built from $u,v$ by $\Delta$ satisfy this pair. $\square$

**Example (the verification in low degree).** For $f(z)=z^2$ one has $u=q_0^2-r^2$, $v=2q_0r$, so $\tilde f=q_0^2-r^2+2q_0\vec q$ and, using $\Delta(q_0^2-r^2)=2-6=-4$ in $\mathbb{R}^4$ and $\Delta(2q_0q_i)=0$ for each $i$, the function $F=-4$ is a nonzero constant, hence regular. For $f(z)=z^3$ one has $u=q_0^3-3q_0r^2$, $v=3q_0^2r-r^3$, hence $\tilde f=q_0^3-3q_0r^2+\vec q(3q_0^2-r^2)$; now $\Delta(q_0^3-3q_0r^2)=6q_0-18q_0=-12q_0$ and, componentwise, $\Delta(q_i(3q_0^2-r^2))=-4q_i$, so

$$
F = -12q_0-4\vec q ,
$$

which is regular of degree $1$: indeed $F=A+\vec qB$ with $A=-12q_0$, $B=-4$, and the axial equations give $-12=-12$ and $0=0$. The two examples exhibit the degree shift by two and the vanishing on the constants and the identity.

**Remark (why the Laplacian is necessary).** The axial extension $\tilde f$ itself is not regular in general: for $f(z)=z^3$, $\bar\partial\tilde f=(A_0-3B-rB_r)+(B_0+A_r/r)\vec q$ with $A=q_0^3-3q_0r^2$, $B=3q_0^2-r^2$, and neither bracket vanishes. The theorem says that the obstruction is exactly the one removed by the Laplacian. This is the structural difference between the complex and the quaternionic theory: holomorphic functions of one variable correspond not to regular functions but to regular functions after a second-order operator has been applied, and the correspondence loses the two lowest homogeneities.

**Remark (the symmetry behind the construction).** The orthogonal group $SO(3)$ acts on the imaginary part of $q$ and fixes the real part; it acts on the regular functions by $f\mapsto f\circ T^{-1}$, $T\in SO(3)$, and the axial functions are exactly the fixed points of this action. Fueter's theorem is therefore the statement that the invariant part of the quaternionic theory is a copy of complex analysis, while the full theory is the orbit of that invariant part under the rotation group. The rotation group itself, the spin cover and the quaternionic description of rotations are Part II's, and the symmetry statement above is the analytic form of the same structure.

## Axial Functions and the Reduced Equations

The construction of the last section is best understood through the class of functions it produces.

**Definition.** A function $f$ on a domain of $\mathbb{H}$ not meeting the real axis is **axial** if it has the form

$$
f(q) = A(q_0,r)+\vec q\,B(q_0,r) , \qquad r=|\vec q| ,
$$

with $A,B$ real-valued functions of two variables.

**Proposition (the axial regularity equations).** The axial function $f=A+\vec qB$ is left regular if and only if the pair

$$
A_0 = 3B+rB_r , \qquad B_0 = -\frac{A_r}{r}
$$

holds on the domain.

*Proof.* Compute $\bar\partial f$ term by term. The scalar derivatives give $\partial_0f=A_0+\vec qB_0$, and the vector derivatives give $\sum_ie_i\partial_iA = r^{-1}A_r\vec q$ and

$$
\sum_{i=1}^{3}e_i\partial_i(\vec qB) = -3B-rB_r ,
$$

the second identity following from $e_i\vec q\,q_i$ summed over $i$, which equals $-r^2$, together with $e_i\cdot e_i=-1$. Collecting the scalar and the vector parts gives

$$
\bar\partial f = \bigl(A_0-3B-rB_r\bigr)+\Bigl(B_0+\frac{A_r}{r}\Bigr)\vec q ,
$$

and this vanishes exactly when both brackets do. $\square$

**Corollary (the reduced Cauchy–Riemann system).** Writing $A=\phi$ and $B=\psi/r$ for real-valued $\phi,\psi$ of $(q_0,r)$ turns the pair into

$$
\phi_0 = \psi_r+\frac{2\psi}{r} , \qquad \psi_0 = -\phi_r ,
$$

the reduced Cauchy–Riemann system of the axial theory. The solutions are exactly the axial regular functions, and Fueter's theorem says that every holomorphic function of the reduced variable $\zeta=q_0+ir$ produces one through $F=\Delta\tilde f$; this is the precise sense in which complex analysis sits inside the quaternionic theory as its rotation-invariant part.

*Proof.* Substituting $A=\phi$, $B=\psi/r$ into $A_0=3B+rB_r$ gives $\phi_0=3\psi/r+r(\psi_r/r-\psi/r^2)=\psi_r+2\psi/r$, and substituting into $B_0=-A_r/r$ gives $\psi_0/r-\psi/r^2\cdot0=-\phi_r/r$, that is $\psi_0=-\phi_r$. For the worked example $F=-12q_0-4\vec q$ one has $\phi=-12q_0$, $\psi=-4r$, and the pair reads $-12=-4-8$ and $0=0$. $\square$

**Example (the radial regular functions).** Taking $A=0$, the pair requires $3B+rB_r=0$, so $B=cr^{-3}$; the function $f(q)=\vec q\,r^{-3}$ is regular away from the axis and is, up to the constant, the vector part of the Cauchy–Fueter kernel. Taking $B=0$ requires $A_r=0$, so $A=A(q_0)$, an arbitrary function of the real variable; the function $f=A(q_0)$ is regular, the "plane" regular functions of the real axis. These two families are the extreme axial cases and the building blocks of the general axial solution.

## Series Expansions and the Fueter Polynomials

**Theorem (Taylor-type expansion).** Every function left regular on a neighbourhood of the origin has a unique expansion

$$
f(q) = \sum_{k\ge0}\;\sum_{\lambda} a_\lambda\,V_\lambda(q) , \qquad a_\lambda\in\mathbb{H} ,
$$

convergent on the ball of regularity, where $V_\lambda$ runs over the **Fueter polynomials**: the symmetrised products

$$
V_{\lambda_1\dots\lambda_k}(q) = \frac{1}{k!}\sum_{\sigma\in S_k}z_{\lambda_{\sigma(1)}}\cdots z_{\lambda_{\sigma(k)}} ,
$$

of the Fueter variables $z_0=q_0$, $z_i=q_0e_i-q_i$ $(i=1,2,3)$, taken over the proper multi-indices of the theory; these polynomials form a basis of the space of homogeneous regular polynomials of degree $k$.

*Pro.* Quoted as standard (Fueter; Sudbery). The expansion is the quaternionic instance of the general power-series expansion of the hypercomplex theory, whose integration theory is not treated here, and the explicit basis is the classical Fueter basis; the homogeneity and the regularity of the symmetrised products follow from the Leibniz rule for $\bar\partial$ and the regularity of the $z_i$. $\square$

**Remark (what the expansion does and does not give).** The expansion makes the regular functions a class as rigid as the holomorphic ones — a regular function on a ball is determined by its coefficients, and the Cauchy–Fueter formula computes them by small-sphere integrals — but the class is not closed under multiplication, since the product of two of the linear regular functions $z_i$ need not be regular; this is the failure recorded in *Hypercomplex Analysis* and *Clifford Analysis*, and it is the reason the theory has a basis but no algebra of regular functions. The dimension of the homogeneous piece is read from the Fischer decomposition of *Clifford Analysis*; for the quaternionic case it is $\dim\mathcal{M}_k=4[\binom{3+k}{k}-\binom{2+k}{k-1}]$, and the Fueter polynomials enumerate it.

**Example (the low pieces).** For $k=0$ the expansion is the constant term. For $k=1$ it is $\sum_ia_iz_i$, the span of the Fueter variables, of real dimension $12$; the polynomials $z_i$ are the linear regular functions, while $q$ itself is not regular. For $k=2$ the Fischer decomposition gives $\dim\mathcal{M}_2=24$, and the piece contains the powers $z_i^2$ of the Fueter variables, which are the plane-regular functions of the subalgebra generated by $1$ and $e_i$; a product $z_iz_j$ with $i\neq j$ is not regular, so the class fails to be an algebra already at degree two.

## The Axial and Slice Points of View

**Remark (the two descriptions).** The axial description of the preceding section describes the functions that are invariant under the rotations of the imaginary part of $q$; it is the description in which complex analysis appears inside the quaternionic theory. The **slice** description starts instead from the observation that $\mathbb{H}=\bigcup_{i\in S^2}\mathbb{C}_i$ is the union of the complex planes $\mathbb{C}_i=\mathbb{R}+i\mathbb{R}$, one for each imaginary unit $i$, and calls a function regular if it is holomorphic on each slice $\mathbb{C}_i$ and the slices fit together with a compatibility condition. The two descriptions agree on their common domain: a slice-regular function that is also axial is an axial regular function, and Fueter's theorem is then the correspondence with the holomorphic functions of the reduced variable. The slice theory has its own power series, its own Cauchy formula and its own class of "slice" regular functions that need not be Fueter-regular; it is a theory of Part V, where it is developed for the quaternions and for the biquaternions, and carries the biquaternionic case and the explicit power series. Here the axial formulation is the one used, and the slice formulation is mentioned only to delimit it.

**Remark (the biquaternionic and other systems).** Replacing the real coefficients of the quaternion algebra by complex ones gives the biquaternions $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$; the Fueter operator is defined by the same formula, the Cauchy kernel acquires a different normalisation because the algebra has zero divisors, and the class of regular functions is larger in some directions and smaller in others. The biquaternionic function theory, its Fueter operator and its regular functions are treated in Part V; the split quaternionic case is treated there too. What carries over from this article is the operator, the factorisation, the Cauchy kernel and Fueter's theorem; what changes is the value algebra and the structure of its zero-divisor set.

## Summary

The Fueter operator $\bar\partial=\partial_0+e_1\partial_1+e_2\partial_2+e_3\partial_3$ and its conjugate $\partial$ factor the Laplacian of $\mathbb{R}^4$, $\bar\partial\partial=\partial\bar\partial=\Delta$, and are elliptic, with symbol $\sigma(\xi)=\xi_0+\sum_ie_i\xi_i$ and inverse $\bar\sigma(\xi)/|\xi|^2$. A function is left regular when $\bar\partial f=0$; the left regular functions form a real vector space and a right $\mathbb{H}$-module, conjugation exchanges left and right regularity, and every regular function is real-analytic with harmonic components, so the mean value property, the maximum principle, Liouville's theorem and the identity theorem hold. The linear regular functions are the Fueter variables $z_i=q_0e_i-q_i$, spanning a space of real dimension $12$. The fundamental solution is the Cauchy–Fueter kernel $E(q)=\frac{1}{2\pi^2}\bar q|q|^{-4}$, and it yields the Cauchy–Fueter formula $f(q)=\frac{1}{2\pi^2}\int_{\partial\Omega}\overline{(p-q)}|p-q|^{-4}\nu_B(p)f(p)dS(p)$, the Cauchy–Fueter–Pompeiu formula for non-regular functions, the Cauchy estimates on balls and the jump and projection statements of the general theory. **Fueter's theorem** constructs regular functions from holomorphic ones: the axial extension $\tilde f=u(q_0,r)+\frac{\vec q}{r}v(q_0,r)$ of a holomorphic $f=u+iv$ is not regular, but its Laplacian $F=\Delta\tilde f$ is, the construction shifting homogeneity by two and killing the constants and the identity. The axial regular functions $A(q_0,r)+\vec qB(q_0,r)$ are exactly those solving the pair $A_0=3B+rB_r$, $B_0=-A_r/r$, which is a Cauchy–Riemann system in the reduced variables $(q_0,r)$, and every regular function on a ball has a Taylor expansion in the homogeneous monogenic pieces $\mathcal{M}_k$, whose standard bases are the Fueter polynomials $V_\lambda$ and whose coefficients are computed by the Cauchy–Fueter formula. The class is rigid but not an algebra: products of regular functions need not be regular. The general operator theory is *Clifford Analysis* and *Regularity and the Cauchy–Riemann Operator*; the slice description and the biquaternionic, split-biquaternionic and other value algebras are Part V.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | Real quaternions, basis $1,e_1,e_2,e_3$ |
| $q=q_0+\vec q$ | Quaternionic variable; $\vec q=q_1e_1+q_2e_2+q_3e_3$ |
| $\bar q$, $N(q)=|q|^2$ | Quaternionic conjugation and norm form |
| $\bar\partial=\partial_0+\sum_{i=1}^3e_i\partial_i$ | Fueter operator |
| $\partial=\partial_0-\sum_{i=1}^3e_i\partial_i$ | Conjugate; $\bar\partial\partial=\partial\bar\partial=\Delta$ |
| $\sigma(\xi)$, $\bar\sigma(\xi)$ | Symbol and conjugate symbol of $\bar\partial$ |
| $\bar\partial f=0$, $f\bar\partial=0$ | Left and right Fueter regularity |
| $z_i=q_0e_i-q_i$ | Fueter variables |
| $E(q)=\frac{1}{2\pi^2}\bar q|q|^{-4}$ | Cauchy–Fueter kernel; $\bar\partial E=\delta_0$ |
| $\nu_B=\sum_\alpha\nu_\alpha e_\alpha$ | Conormal element |
| $\tilde f$ | Axial (radial) extension of $f$ |
| $F=\Delta\tilde f$ | Fueter construction |
| $A(q_0,r)+\vec qB(q_0,r)$ | Axial form of a regular function |
| $r=|\vec q|$, $\zeta=q_0+ir$ | Radial coordinate and reduced complex variable |
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
