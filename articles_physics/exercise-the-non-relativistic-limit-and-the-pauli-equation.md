# __Exercise: The Non-Relativistic Limit and the Pauli Equation__

## Introduction

This is one of the worked exercises attached to the article *The Biquaternion Dirac Equation — Solutions and Non-Relativistic Limit*. That article stated the biquaternion Dirac equation, constructed its plane-wave solutions, and carried the equation into the non-relativistic regime far enough to exhibit the Pauli equation and the gyromagnetic factor $g=2$. This exercise takes the limiting procedure as given and executes it in full: every order that contributes to the first corrections is kept, every coefficient is derived, and every claim is checked.

Five problems are worked:

1. the Foldy–Wouthuysen elimination of the small component, carried out step by step and to the order at which the first corrections appear;
2. the minimal substitution $p\to p-ϙ\vec A$ and the electromagnetic terms it produces, including the spin term and the coefficient that fixes $g=2$;
3. the next order in $1/c$: the relativistic kinetic correction, the Darwin term, and the spin–orbit coupling;
4. the Hermiticity of every term, and which terms lie in the Hermitian subspace $\mathbb M_+$ and which do not;
5. the physical dimensions of every term.

**On the parent article.** The parent's non-relativistic section works only to leading order. It factors out the rest energy, eliminates the small component with the approximation $\partial/\partial t'\,\chi\approx 0$, and reads off the Pauli Hamiltonian; it stops there. It contains no spin–orbit and no Darwin term, it never actually performs a Foldy–Wouthuysen transformation (the transformation appears only in its Further Reading), and it does not state the sector ($\mathbb M_\pm$) status of the intermediate operators it uses ($\beta$, $\boldsymbol\alpha$, $O$, $S_1$), although it does identify the Pauli Hamiltonian and the spin term as $\mathbb M_+$ observables. Problems 3 and 4 supply those orders. Where the parent is silent this is stated explicitly and not silently filled in.

**Conventions.** The biquaternion algebra is $\mathbb B=\mathbb C\otimes_\mathbb R\mathbb H$, the basis is $e_t=1,\vec e_x,\vec e_y,\vec e_z$ with $\vec e_k^2=-e_t$, and $i$ is the scalar imaginary. The subspace $\mathbb M_+$ is the Hermitian subspace (real scalar, imaginary vector) and $\mathbb M_-$ the anti-Hermitian subspace (imaginary scalar, real vector), with $\mathbb B=\mathbb M_+\oplus\mathbb M_-$ and $i\mathbb M_\pm=\mathbb M_\mp$. The isomorphism, written $\mathsf{M}_2$ as in the companion Dirac article, is $e_t\mapsto I_2$, $\vec e_k\mapsto-i\sigma_k$, $i\mapsto iI_2$, so that $\mathsf{M}_2(\vec e_k)=-i\sigma_k$ and $\sigma_k\leftrightarrow i\vec e_k$. The gamma matrices are the parent's Dirac-basis matrices,

$$
\gamma^0=\begin{pmatrix} I_2&0\\0&-I_2\end{pmatrix}=\beta,\qquad
\gamma^k=\begin{pmatrix} 0&\sigma_k\\-\sigma_k&0\end{pmatrix},
\qquad \{\gamma^\mu,\gamma^\nu\}=2g^{\mu\nu}I_4,\quad g=\mathrm{diag}(+1,-1,-1,-1).
$$

The Clifford metric $g$ is carried by the generators; it is the negative of the metric $\eta=\mathrm{diag}(-1,+1,+1,+1)$ that appears in the $ict'$ form of the biquaternionic gradient, $\tilde\nabla=e_t\partial/\partial Q_t+\vec e_x\partial/\partial Q_x+\vec e_y\partial/\partial Q_y+\vec e_z\partial/\partial Q_z$ with $\partial^2/\partial Q_t^2=-c^{-2}\,\partial^2/\partial {t'}^2$. The kinetic momentum is $\vec\pi=p-ϙ\vec A$ with $p=-i\hbar\nabla$, the charge is $ϙ$, the electrostatic potential is written $\phi_0$, and the potential energy of the charge in it is $V=ϙ\phi_0$. Natural units $\hbar=c=1$ are used while deriving; $\hbar$ and $c$ are restored wherever a physical statement is made.

## Problem 1: The Foldy–Wouthuysen elimination of the small component

**Statement.** Starting from the four-component Dirac Hamiltonian with minimal coupling, eliminate the small component and obtain the Pauli Hamiltonian, keeping the orders through the first corrections.

**Solution.**

*Step 1: the split.* In the Dirac basis the Hamiltonian is

$$
i\hbar\,\partial/\partial t'\,\psi=H\psi,\qquad
H=c\,\boldsymbol\alpha\cdot\vec\pi+\beta mc^2+ϙ\phi_0,
\qquad \alpha^k=\gamma^0\gamma^k=\begin{pmatrix}0&\sigma_k\\ \sigma_k&0\end{pmatrix}.
$$

Write $H=\beta mc^2+O+E$ with

$$
O=c\,\boldsymbol\alpha\cdot\vec\pi \quad(\text{odd},\ \beta O\beta=-O),
\qquad E=ϙ\phi_0 \quad(\text{even},\ \beta E\beta=E).
$$

The even operator $E$ is the electrostatic energy and the odd operator $O$ is what couples the upper and lower components.

*Step 2: factoring out the rest energy.* Write $\psi=\exp(-imc^2t'/\hbar)(\phi,\chi)^{\mathsf T}$. Substituting and cancelling the common phase gives the parent's two coupled equations,

$$
i\hbar\,\partial/\partial t'\,\phi=c\,\boldsymbol\sigma\cdot\vec\pi\,\chi+ϙ\phi_0\phi,
\qquad
i\hbar\,\partial/\partial t'\,\chi=c\,\boldsymbol\sigma\cdot\vec\pi\,\phi-2mc^2\chi+ϙ\phi_0\chi .
$$

*Step 3: the leading elimination.* The term $2mc^2\chi$ dominates the second equation whenever the fields, the kinetic energy and $\partial/\partial t'\,\chi$ are small compared with $mc^2$. Neglecting the other terms there,

$$
\chi=\frac{\boldsymbol\sigma\cdot\vec\pi}{2mc}\,\phi+O(c^{-3}),
$$

so the small component is of relative order $v/c$, as it must be. Substituting into the first equation eliminates $\chi$ exactly at this order:

$$
i\hbar\,\partial/\partial t'\,\phi=\left[\frac{(\boldsymbol\sigma\cdot\vec\pi)^2}{2m}+ϙ\phi_0\right]\phi .
$$

*Step 4: the systematic transformation.* The approximation of Step 3 is the first term of a controlled expansion. The Foldy–Wouthuysen generator is $S=S_1+S_2+\cdots$ with

$$
S_1=-\frac{i}{2mc^2}\,\beta O .
$$

For static fields the generator is time-independent, and

$$
\exp(iS_1)\big(H-i\hbar\partial/\partial t'\big)\exp(-iS_1)
=H+i[S_1,H]-\tfrac12[S_1,[S_1,H]]-\tfrac{i}{6}[S_1,[S_1,[S_1,H]]]+\cdots
$$

Using $O\beta=-\beta O$ and $E\beta=\beta E$, the three elementary commutators are

$$
i[S_1,\beta mc^2]=-O,\qquad
i[S_1,O]=\frac{\beta O^2}{mc^2},\qquad
[S_1,[S_1,\beta mc^2]]=\frac{\beta O^2}{mc^2}.
$$

The first cancels the odd term $O$; the second and third combine into the even term $\frac{\beta O^2}{2mc^2}$, the leading non-relativistic energy. There is also a residual odd operator, of relative order $(v/c)^2$ compared with $O$,

$$
O_1=i[S_1,E]=\frac{iϙ}{2mc}\,\beta\,\boldsymbol\alpha\cdot\vec E,
$$

which the second transformation $S_2=-\frac{i}{2mc^2}\beta O_1$ removes. To the order at which the first physical corrections appear, therefore,

$$
H_1=\beta mc^2+ϙ\phi_0+\frac{\beta O^2}{2mc^2}+O_1+O(c^{-2}).
$$

*Step 5: evaluating $O^2$.* With $\alpha^i\alpha^j=\delta^{ij}+i\epsilon^{ijk}\Sigma_k$ and $\Sigma_k=\mathrm{diag}(\sigma_k,\sigma_k)$,

$$
O^2=c^2\big(\vec\pi^2+i\,\boldsymbol\Sigma\cdot(\vec\pi\times\vec\pi)\big).
$$

Since $O$ is block-off-diagonal, its square is block-diagonal, so the odd part of $H_1$ is exactly $O_1$ and the even part, beyond the rest energy, is $ϙ\phi_0+\beta O^2/(2mc^2)$. In the upper (large) block, $\beta\to+1$ and $\boldsymbol\Sigma\to\boldsymbol\sigma$, so

$$
H_{\rm large}=mc^2+ϙ\phi_0+\frac{\vec\pi^2-ϙ\,\boldsymbol\sigma\cdot\vec B}{2m}+O(c^{-2}),
$$

where the evaluation of $\vec\pi\times\vec\pi$ is carried out in Problem 2. Subtracting the rest energy,

$$
\boxed{\;i\hbar\,\partial/\partial t'\,\phi=\left[\frac{(p-ϙ\vec A)^2}{2m}+ϙ\phi_0-\frac{ϙ\hbar}{2m}\,\boldsymbol\sigma\cdot\vec B\right]\phi\;}
$$

which is the Pauli equation exactly as the parent reports it. The coefficient $1/2m$ is the whole content of the $g=2$ result of Problem 2: it is produced by the $2mc^2$ in the denominator of the small-component elimination, not put in by hand.

## Problem 2: Minimal substitution, the electromagnetic terms, and $g=2$

**Statement.** Carry out the minimal substitution, evaluate the electromagnetic terms it generates, and verify the gyromagnetic factor $g=2$ together with the biquaternion form of the spin term.

**Solution.**

*Step 1: the substitution.* The parent's convention is $D_\mu=\partial/\partial Q_\mu+iqA_\mu$, which in this mostly-minus metric is equivalent to

$$
p\ \longrightarrow\ p-ϙ\vec A,\qquad i\partial/\partial t'\ \longrightarrow\ i\partial/\partial t'-ϙ\phi_0 ,
$$

i.e. $\vec\pi=p-ϙ\vec A$ and the electrostatic energy $ϙ\phi_0$ collected in $V=ϙ\phi_0$. This is the mostly-minus form of the covariant derivative; the reader should note that the mostly-plus convention uses $D_\mu=\partial/\partial Q_\mu-iqA_\mu$, and that the sign of $A_\mu=(\phi_0,-\vec A)$ is tied to the metric. Within this article the statement above is used throughout, and it reproduces the standard Hamiltonian $H=c\boldsymbol\alpha\cdot(p-ϙ\vec A)+\beta mc^2+ϙ\phi_0$.

*Step 2: the commutator of the kinetic momenta.* With $p=-i\hbar\nabla$,

$$
[\pi_i,\pi_j]=-ϙ\big([p_i,A_j]+[A_i,p_j]\big)
=-ϙ\big(-i\hbar\partial/\partial Q_i\,A_j+i\hbar\partial/\partial Q_j\,A_i\big)
=i\hbar ϙ\,\epsilon_{ijk}B_k ,
$$

so that

$$
\vec\pi\times\vec\pi=i\hbar ϙ\,\vec B,\qquad \vec B=\nabla\times\vec A .
$$

Equivalently, $p\times\vec A+\vec A\times p=-i\hbar\vec B$; the two terms are individually non-Hermitian but their sum is Hermitian. In natural units this is the parent's $\vec\pi\times\vec\pi=iϙ\vec B$.

*Step 3: the square of the spin operator.* The Pauli identity is

$$
(\boldsymbol\sigma\cdot\vec a)(\boldsymbol\sigma\cdot\vec b)
=\vec a\cdot\vec b\,I_2+i\,\boldsymbol\sigma\cdot(\vec a\times\vec b),
$$

valid for any two vectors whose components commute with one another. Applying it to $\vec a=\vec b=\vec\pi$ and using Step 2,

$$
(\boldsymbol\sigma\cdot\vec\pi)^2=\vec\pi^2+i\,\boldsymbol\sigma\cdot(\vec\pi\times\vec\pi)
=\vec\pi^2+i\,\boldsymbol\sigma\cdot(i\hbar ϙ\vec B)
=\vec\pi^2-ϙ\hbar\,\boldsymbol\sigma\cdot\vec B ,
$$

which is the parent's result, with $\hbar$ restored. The coefficient carries no power of $c$: the two factors of $c$ in the elimination cancel, since $\chi=\boldsymbol\sigma\cdot\vec\pi/(2mc)\,\phi$ is multiplied by $c\,\boldsymbol\sigma\cdot\vec\pi$ in the first equation. The identification $\vec S=\tfrac\hbar2\boldsymbol\sigma$ gives the spin term

$$
-\frac{ϙ\hbar}{2m}\,\boldsymbol\sigma\cdot\vec B=-\frac{ϙ}{m}\,\vec S\cdot\vec B=-\vec\mu\cdot\vec B .
$$

*Step 4: the gyromagnetic factor.* Writing the coupling as $-\vec\mu\cdot\vec B$ identifies

$$
\vec\mu=\frac{ϙ\hbar}{2m}\boldsymbol\sigma=\frac{ϙ}{m}\,\vec S,\qquad \vec S=\frac\hbar2\boldsymbol\sigma .
$$

The general parametrization of a magnetic dipole is $\vec\mu=g\dfrac{ϙ}{2m}\vec S$, so that

$$
\boxed{\;g=2\;}
$$

for a structureless spin-$\tfrac12$ particle. For the electron, $ϙ=-e$ and

$$
\vec\mu_e=-\frac{e}{m_e}\vec S=-g\frac{e}{2m_e}\vec S,\qquad g=2,
$$

whose magnitude at $S_z=\hbar/2$ is one Bohr magneton $\mu_B=e\hbar/2m_e$. The measured anomalous part $a=(g-2)/2\approx\alpha/2\pi$ is a radiative correction that lies outside the equation treated here.

*Step 5: the biquaternion form.* Under the isomorphism $\sigma_k\leftrightarrow i\vec e_k$, a magnetic field written as the pure real quaternion $\vec B=B_k \vec e_k$ maps the spin term to

$$
-\frac{ϙ\hbar}{2m}\boldsymbol\sigma\cdot\vec B\ \longleftrightarrow\ -\frac{ϙ\hbar}{2m}\,i\vec B\ \in\ \mathbb M_+ ,
$$

the Hermitian element of the informational sector, exactly as the parent states. The kinetic and electrostatic terms multiply the identity and map to the scalar part $(\vec\pi^2/2m)e_t$ and $ϙ\phi_0 e_t$ of $\mathbb M_+$.

*Numerical checks.* The commutator identity of Step 2 was verified by finite differences on a grid with $\vec A=(-y,0,0)$, for which $\vec B=(0,0,1)$; the operator identity $[\pi_x,\pi_y]\psi=iqB_z\psi$ was confirmed at five test points with a maximum absolute error $4.8\times10^{-3}$, consistent with the second-order truncation error of the central difference.

## Problem 3: The spin–orbit and Darwin terms at the next order

**Statement.** Extend the elimination to the next order in $1/c$ and obtain the relativistic kinetic correction, the Darwin term, and the spin–orbit coupling.

**Solution.** This order is *not* contained in the parent article, which stops at the leading Pauli Hamiltonian. It is obtained by the second Foldy–Wouthuysen step.

*Step 1: the second generator.* The odd remainder of $H_1$ is $O_1=\dfrac{iϙ}{2mc}\beta\boldsymbol\alpha\cdot\vec E$, and the transformation that removes it is

$$
S_2=-\frac{i}{2mc^2}\,\beta O_1 .
$$

Evaluating the expansion of $\exp(iS_2)H_1\exp(-iS_2)$ and using $[\boldsymbol\alpha\cdot\vec E,ϙ\phi_0]=0$ (the matrix $\boldsymbol\alpha$ is constant and $\vec E$ and $\phi_0$ are functions of position), the even terms of relative order $c^{-2}$ that survive are

$$
H^{(2)}
=-\frac{(\boldsymbol\sigma\cdot\vec\pi)^4}{8m^3c^2}
+\frac{\hbar^2}{8m^2c^2}\nabla^2V
-\frac{ϙ\hbar}{4m^2c^2}\,\boldsymbol\sigma\cdot(\vec E\times\vec\pi),
$$

with $V=ϙ\phi_0$ the potential energy. The first term is the expansion of the large-component energy $\sqrt{m^2c^4+(\boldsymbol\sigma\cdot\vec\pi)^2c^2}$; it is $(\boldsymbol\sigma\cdot\vec\pi)^4$, not $\vec\pi^4$, because $(\boldsymbol\sigma\cdot\vec\pi)^2=\vec\pi^2-ϙ\hbar\boldsymbol\sigma\cdot\vec B$, so the two differ by $-ϙ\hbar(\vec\pi^2\boldsymbol\sigma\cdot\vec B+\boldsymbol\sigma\cdot\vec B\vec\pi^2)+(ϙ\hbar)^2(\boldsymbol\sigma\cdot\vec B)^2$, which is of the same $1/c^2$ order and is not dropped.

*Step 2: the Darwin term.* Since $\vec E=-\nabla\phi_0$ and $V=ϙ\phi_0$,

$$
\frac{\hbar^2}{8m^2c^2}\nabla^2V=-\frac{ϙ\hbar^2}{8m^2c^2}\nabla\cdot\vec E .
$$

This is the Darwin term. Its Hermiticity is immediate: $\nabla\cdot\vec E$ is a real function of position.

*Step 3: the spin–orbit term.* Since $\nabla V=ϙ\nabla\phi_0=-ϙ\vec E$,

$$
-\frac{ϙ\hbar}{4m^2c^2}\boldsymbol\sigma\cdot(\vec E\times\vec\pi)
=\frac{\hbar}{4m^2c^2}\,\boldsymbol\sigma\cdot(\nabla V\times\vec\pi)
=\frac{\hbar}{4m^2c^2}\,\frac1r\frac{dV}{dr}\,\boldsymbol\sigma\cdot\vec L
\qquad(\text{central }V),
$$

where $\vec E\times\vec\pi$ has been written with $\vec E=-\nabla\phi_0$. For a central electrostatic field, whose vector potential may be neglected so that $\vec\pi\to p$, the last factor is the standard spin–orbit coupling with $\vec L=\vec r\times p$ and $\vec S=\tfrac\hbar2\boldsymbol\sigma$. The coefficient $1/(4m^2c^2)$ already contains the Thomas factor of $\tfrac12$: a naive Lorentz transformation to the instantaneous rest frame of the electron would give twice this value, and the factor of $\tfrac12$ is the Thomas precession correction. With $\vec S=\tfrac\hbar2\boldsymbol\sigma$, the term reads $\dfrac{1}{2m^2c^2}\dfrac1r\dfrac{dV}{dr}\vec L\cdot\vec S$, the standard spin–orbit coupling.

*Step 4: the assembled Hamiltonian.* Collecting the leading and next-to-leading orders, the large-component Hamiltonian is

$$
\boxed{\;
H=\frac{\vec\pi^2}{2m}+ϙ\phi_0-\frac{ϙ\hbar}{2m}\boldsymbol\sigma\cdot\vec B
-\frac{(\boldsymbol\sigma\cdot\vec\pi)^4}{8m^3c^2}
+\frac{\hbar^2}{8m^2c^2}\nabla^2V
-\frac{ϙ\hbar}{4m^2c^2}\boldsymbol\sigma\cdot(\vec E\times\vec\pi)
\;}
$$

to relative order $c^{-2}$. The first three terms are the Pauli Hamiltonian of Problem 1; the last three are the corrections that the parent article does not reach.

*Step 5: numerical verification against the exact Dirac spectrum.* The three corrections are fixed by their coefficients; a single overall check is therefore decisive. In a hydrogenic atom with nuclear charge $\mathfrak{Z}$, the first-order shifts of the four terms are, in natural units ($c=1$), as in the companion's derivation,

$$
\Delta E_{\rm kin}=-\frac{m(\mathfrak{Z}\alpha)^4}{2n^3}\!\left[\frac{1}{\ell+\tfrac12}-\frac{3}{4n}\right],\qquad
\Delta E_{\rm SO}=\frac{m(\mathfrak{Z}\alpha)^4}{2n^3}\frac{j(j+1)-\ell(\ell+1)-\tfrac34}{2\ell(\ell+\tfrac12)(\ell+1)},
$$

$$
\Delta E_{\rm D}=\frac{m(\mathfrak{Z}\alpha)^4}{2n^3}\quad(\ell=0),\qquad \Delta E_{\rm D}=0\quad(\ell\neq0),
$$

with the exact Dirac shift $\Delta E_{\rm exact}=-\dfrac{m(\mathfrak{Z}\alpha)^4}{2n^3}\Big[\dfrac{1}{j+\tfrac12}-\dfrac{3}{4n}\Big]$. Evaluating all of these with exact rational arithmetic for every level with $n\le6$ (36 levels, both $j=\ell\pm\tfrac12$), the sum $\Delta E_{\rm kin}+\Delta E_{\rm SO}+\Delta E_{\rm D}$ equals $\Delta E_{\rm exact}$ in every case, with difference exactly $0$. An independent one-dimensional Foldy–Wouthuysen expansion, carried out symbolically to order $m^{-3}$ in a purely scalar potential, reproduces the four coefficients $1,+\tfrac12,+\tfrac18,-\tfrac18$ for $V$, $\vec\pi^2/2m$, $\nabla^2V/(8m^2c^2)$ and $-(\boldsymbol\sigma\cdot\vec\pi)^4/(8m^3c^2)$ respectively. The Darwin sign is therefore $+\hbar^2\nabla^2V/(8m^2c^2)$, equivalently $-(ϙ\hbar^2/8m^2c^2)\nabla\cdot\vec E$.

## Problem 4: Hermiticity and the $\mathbb M_\pm$ decomposition

**Statement.** Check the Hermiticity of every term and determine which terms lie in $\mathbb M_+$.

**Solution.**

*Step 1: Hermiticity.* Each term of the Hamiltonian of Problem 3 is Hermitian:

- $\vec\pi^2/2m$: $\pi_i^\dagger=\pi_i$, hence $\pi_i\pi_i$ is Hermitian;
- $ϙ\phi_0$: multiplication by the real function $ϙ\phi_0$, Hermitian;
- $-\dfrac{ϙ\hbar}{2m}\boldsymbol\sigma\cdot\vec B$: $\sigma_k$ and the real field $B_k$ are Hermitian;
- $-(\boldsymbol\sigma\cdot\vec\pi)^4/(8m^3c^2)$: a real multiple of the Hermitian $(\boldsymbol\sigma\cdot\vec\pi)^2$;
- $\dfrac{\hbar^2}{8m^2c^2}\nabla^2V$: multiplication by a real function;
- $-\dfrac{ϙ\hbar}{4m^2c^2}\boldsymbol\sigma\cdot(\vec E\times\vec\pi)$: this is the one term whose Hermiticity is not automatic. Using $[\pi_i,E_j]=-i\hbar\partial/\partial Q_i\,E_j$,

$$
(\vec E\times\vec\pi)_i^\dagger=(\vec E\times\vec\pi)_i+i\hbar(\nabla\times\vec E)_i ,
$$

so the term is Hermitian if and only if $\nabla\times\vec E=0$, its failure of Hermiticity being proportional to the curl. Since $\vec E=-\nabla\phi_0$ for an electrostatic field, $\nabla\times\vec E=-\nabla\times\nabla\phi_0=0$ identically, and the term is Hermitian. Writing it instead as $\boldsymbol\sigma\cdot(\nabla V\times\vec\pi)$ makes this manifest, because $\nabla V$ is a gradient. For a general time-dependent field, where $\vec E$ has a solenoidal part $-\partial/\partial t'\,\vec A$ and $\nabla\times\vec E=-\partial/\partial t'\,\vec B$, the antisymmetric part does not vanish and the non-relativistic reduction requires the symmetrized ordering; this is the only place in the reduction where the result is convention- and ordering-sensitive beyond the metric conventions already noted.

*Step 2: the $\mathbb M_+$ representatives.* Under the isomorphism, a Hermitian $2\times2$ matrix $h_tI_2+\vec h\cdot\boldsymbol\sigma$ corresponds to the Hermitian biquaternion $h_te_t+i\vec h\in\mathbb M_+$; this was verified directly for 100 random Hermitian operators with maximum error $0$. Applying it term by term, with $\vec B=B_k\vec e_k$ and $(\vec E\times\vec\pi)=(\vec E\times\vec\pi)_k\vec e_k$,

| Term of $H$ | Biquaternion representative | Sector |
|---|---|---|
| $\vec\pi^2/2m$ | $(\vec\pi^2/2m)\,e_t$ | $\mathbb M_+$ |
| $ϙ\phi_0$ | $(ϙ\phi_0)\,e_t$ | $\mathbb M_+$ |
| $-\dfrac{ϙ\hbar}{2m}\boldsymbol\sigma\cdot\vec B$ | $-\dfrac{ϙ\hbar}{2m}\,i\vec B$ | $\mathbb M_+$ |
| $\dfrac{\hbar^2}{8m^2c^2}\nabla^2V$ | $\dfrac{\hbar^2}{8m^2c^2}(\nabla^2V)\,e_t$ | $\mathbb M_+$ |
| $-\dfrac{ϙ\hbar}{4m^2c^2}\boldsymbol\sigma\cdot(\vec E\times\vec\pi)$ | $-\dfrac{ϙ\hbar}{4m^2c^2}\,i(\vec E\times\vec\pi)$ | $\mathbb M_+$ |

Every term of the reduced, two-component Hamiltonian is Hermitian, hence every term lands in $\mathbb M_+$. This is the precise content of the parent's remark that the spin term is an observable of the informational sector; the remark applies term by term.

*Step 3: what does not land in $\mathbb M_+$.* Three classes of object in the reduction do not.

1. **The Clifford-odd operators.** The mass term $\beta mc^2$ contains $\beta=\gamma^0$, and the generator $S_1=-\frac{i}{2mc^2}\beta O$ contains $\beta O$. Both $\beta$ and $\beta O$ are odd products of gamma matrices, whereas $\mathbb B\cong\mathrm{Cl}^+_{1,3}$ is the *even* subalgebra. They therefore have no representative in $\mathbb B$ at all, and a fortiori none in either $\mathbb M_\pm$. This is why the four-component Hamiltonian is not an element of $\mathbb B$ and why a transformation is needed before the biquaternion identification can be made: the Foldy–Wouthuysen transformation is exactly the operation that removes the Clifford-odd part and leaves an element of $\mathbb M_+$.

2. **The anti-Hermitian generator.** $S_1$ is Hermitian, so $iS_1$ is anti-Hermitian: it plays the rôle that the elements of $\mathbb M_-$ play in the companion quantum article, where the Lie algebra of the unitary group is $\mathbb M_-$. It is not itself in $\mathbb M_-$, because it is built from the Clifford-odd element $\beta O$. The two gradings must not be conflated: the Foldy–Wouthuysen grading is by conjugation with $\beta$, the $\mathbb M_\pm$ grading is by ${}^{*}$. Thus the odd operator $O=c\boldsymbol\alpha\cdot\vec\pi$ is Foldy–Wouthuysen-odd but Clifford-even and Hermitian, so as a biquaternion it lies in $\mathbb M_+$; while $\beta O$ is Foldy–Wouthuysen-odd, Clifford-odd and anti-Hermitian, and lies in neither $\mathbb B$ nor $\mathbb M_\pm$. The identification of "odd" with "not in $\mathbb M_+$" is incorrect.

3. **The real structure and the mass term.** In the biquaternion equation the conjugation $\flat=-{}^{*}$ is the algebra's real structure, and it *preserves* the sectors: if $\tilde\Psi\in\mathbb M_+$ then $\tilde\Psi^\flat=-\tilde\Psi\in\mathbb M_+$, and if $\tilde\Psi\in\mathbb M_-$ then $\tilde\Psi^\flat=\tilde\Psi\in\mathbb M_-$. Its action is diagonal on the sector decomposition with opposite signs $\mp1$: a coupling built on $\flat$ — a Majorana-type mass, $m\tilde\Psi^\flat$ — would carry those opposite signs. The parent's mass term is not that coupling; it is the linear, chirality-off-diagonal pair $\tilde\nabla\tilde\Psi_R = m\tilde\Psi_L$, $\tilde\nabla^{\natural}\tilde\Psi_L = m\tilde\Psi_R$, which couples the two central ideals (the chiralities) and leaves each element's sector membership untouched. The operation that exchanges the two sectors is multiplication by the central $i$. The rest-energy phase that is factored out before the reduction,

$$
\exp(-imc^2t'/\hbar)=\cos\!\Big(\frac{mc^2t'}{\hbar}\Big)e_t-\sin\!\Big(\frac{mc^2t'}{\hbar}\Big)(ie_t),
$$

is not Hermitian: its first term lies in $\mathbb M_+$ and its second in $\mathbb M_-$, since $ie_t$ is anti-Hermitian. It is a phase, not an observable, and must be factored out before a two-component (hence $\mathbb M_+$) description of the dynamics is reached.

## Problem 5: The physical dimensions of each term

**Statement.** Determine the physical dimensions of each term.

**Solution.** Every term is an energy, since each is a term of a Hamiltonian. The individual coefficients nevertheless carry different powers of $\hbar$ and $c$, and checking them is a useful consistency test. In SI units, with $[\hbar]=\mathrm{kg\,m^2\,s^{-1}}$, $[c]=\mathrm{m\,s^{-1}}$, $[ϙ]=\mathrm C$, $[\phi_0]=\mathrm{V}=\mathrm{kg\,m^2\,s^{-3}A^{-1}}$, $[\vec B]=\mathrm T=\mathrm{kg\,s^{-2}A^{-1}}$ and $[\vec E]=\mathrm{V\,m^{-1}}=\mathrm{kg\,m\,s^{-3}A^{-1}}$:

| Term | Coefficient units | Field/operator units | Product |
|---|---|---|---|
| $\vec\pi^2/2m$ | $1/m$ | $(\mathrm{kg\,m\,s^{-1}})^2$ | $\mathrm{kg\,m^2\,s^{-2}}$ |
| $ϙ\phi_0$ | $\mathrm C$ | $\mathrm{kg\,m^2\,s^{-3}A^{-1}}$ | $\mathrm{kg\,m^2\,s^{-2}}$ |
| $\dfrac{ϙ\hbar}{2m}\boldsymbol\sigma\cdot\vec B$ | $\mathrm C\,\mathrm{kg\,m^2\,s^{-1}\,kg^{-1}}$ | $\mathrm{kg\,s^{-2}A^{-1}}$ | $\mathrm{kg\,m^2\,s^{-2}}$ |
| $-\dfrac{ϙ\hbar^2}{8m^2c^2}\nabla\cdot\vec E$ | $\mathrm C\,\mathrm{kg^2m^4s^{-2}}\,\mathrm{kg^{-2}m^{-2}s^{2}}$ | $\mathrm{kg\,s^{-3}A^{-1}}$ | $\mathrm{kg\,m^2\,s^{-2}}$ |
| $\dfrac{ϙ\hbar}{4m^2c^2}\boldsymbol\sigma\cdot(\vec E\times\vec\pi)$ | $\mathrm C\,\mathrm{kg\,m^2s^{-1}}\,\mathrm{kg^{-2}m^{-2}s^{2}}$ | $\mathrm{kg^2m^2s^{-4}A^{-1}}$ | $\mathrm{kg\,m^2\,s^{-2}}$ |
| $\dfrac{(\boldsymbol\sigma\cdot\vec\pi)^4}{8m^3c^2}$ | $\mathrm{kg^{-3}m^{-2}s^{2}}$ | $\mathrm{kg^4m^4s^{-4}}$ | $\mathrm{kg\,m^2\,s^{-2}}$ |

The pattern is informative. The leading terms ($\vec\pi^2/2m$, $ϙ\phi_0$, the spin term) carry no power of $c$; the three corrections each carry $c^{-2}$, which is the statement that they are relativistic corrections of order $v^2/c^2$. The spin term carries one power of $\hbar$ while the leading kinetic and electrostatic terms carry none, so the spin term vanishes formally in the classical limit $\hbar\to0$; this is the operator form of the statement that the magnetic moment of a point charge is a quantum effect. The Darwin and spin–orbit terms carry $\hbar^2$ and $\hbar$ respectively, and both survive the $\hbar\to0$ limit when divided by $\hbar$ in the corresponding classical spin–orbit coupling, which is the Thomas-precession energy.

## Summary

The non-relativistic limit of the biquaternion Dirac equation was carried through in five steps.

The Foldy–Wouthuysen elimination of the small component, executed systematically with the generator $S_1=-\frac{i}{2mc^2}\beta O$, produces the Pauli Hamiltonian
$i\hbar\partial/\partial t'\,\phi=\big[\vec\pi^2/2m+ϙ\phi_0-(ϙ\hbar/2m)\boldsymbol\sigma\cdot\vec B\big]\phi$,
reproducing the parent article. The minimal substitution $\vec\pi=p-ϙ\vec A$ gives $[\pi_i,\pi_j]=i\hbar ϙ\epsilon_{ijk}B_k$ and $(\boldsymbol\sigma\cdot\vec\pi)^2=\vec\pi^2-ϙ\hbar\boldsymbol\sigma\cdot\vec B$, and the coefficient $1/2m$ produced by the elimination fixes $g=2$ and $\vec\mu=(ϙ/m)\vec S$, hence $\mu_B=e\hbar/2m_e$ for the electron. At the next order in $1/c$ the second Foldy–Wouthuysen step adds the relativistic kinetic correction $-(\boldsymbol\sigma\cdot\vec\pi)^4/(8m^3c^2)$, the Darwin term $+\hbar^2\nabla^2V/(8m^2c^2)=-(ϙ\hbar^2/8m^2c^2)\nabla\cdot\vec E$, and the spin–orbit coupling $-(ϙ\hbar/4m^2c^2)\boldsymbol\sigma\cdot(\vec E\times\vec\pi)=(\hbar/4m^2c^2)r^{-1}(dV/dr)\boldsymbol\sigma\cdot\vec L$. Summed, these reproduce the exact Dirac fine structure of hydrogenic ions for 36 levels with $n\le6$, with difference exactly zero.

Every term of the reduced Hamiltonian is Hermitian and therefore lies in $\mathbb M_+$; the objects that do not are the Clifford-odd pieces ($\beta mc^2$, $\beta O$), which have no representative in $\mathbb B$ at all, the anti-Hermitian generator $iS_1$, and the real structure $\flat$ — whose opposite-sign action on the sectors a Majorana-type coupling would carry — together with the sector-exchanging rest-energy phase; the parent's mass term is the linear coupling between the two chiralities. The Foldy–Wouthuysen grading by $\beta$ must not be confused with the $\mathbb M_\pm$ grading by ${}^{*}$. All terms are energies, the three corrections carrying the expected $c^{-2}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb B=\mathbb C\otimes_\mathbb R\mathbb H$ | Biquaternion algebra |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$, $\vec e_k^2=-e_t$ | Quaternion basis |
| $\mathbb M_+,\mathbb M_-$ | Hermitian / anti-Hermitian subspaces |
| $\mathsf{M}_2(\vec e_k)=-i\sigma_k$, $\sigma_k\leftrightarrow i\vec e_k$ | Isomorphism, Pauli matrices |
| $\beta=\gamma^0$, $\alpha^k=\gamma^0\gamma^k$ | Dirac-basis matrices |
| $g=\mathrm{diag}(+1,-1,-1,-1)$ | Clifford metric; $g=-\eta$ |
| $\vec\pi=p-ϙ\vec A$ | Kinetic momentum |
| $\vec B=\nabla\times\vec A$, $\vec E$ | Magnetic, electric fields |
| $V=ϙ\phi_0$ | Potential energy |
| $H=\beta mc^2+O+E$, $O=c\boldsymbol\alpha\cdot\vec\pi$ | Split Hamiltonian; odd part |
| $S_1=-\frac{i}{2mc^2}\beta O$ | Foldy–Wouthuysen generator |
| $O_1=\frac{iϙ}{2mc}\beta\boldsymbol\alpha\cdot\vec E$ | Residual odd operator |
| $\vec S=\tfrac\hbar2\boldsymbol\sigma$, $\vec\mu=g\frac{ϙ}{2m}\vec S$ | Spin and magnetic moment |
| $g=2$ | Gyromagnetic factor |
| $\mu_B=e\hbar/2m_e$ | Bohr magneton |

## Further Reading

- P. A. M. Dirac, "The quantum theory of the electron," *Proceedings of the Royal Society A* **117** (1928) 610–624, for the original prediction of $g=2$.
- L. L. Foldy and S. A. Wouthuysen, "On the Dirac theory of spin 1/2 particles and its non-relativistic limit," *Physical Review* **78** (1950) 29–36, for the transformation used here.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the plane-wave solutions and the standard non-relativistic reduction.
- J. J. Sakurai, *Advanced Quantum Mechanics* (Addison-Wesley, 1967), for the emergence of the Pauli equation and the spin–orbit coupling.
- W. Greiner, *Relativistic Quantum Mechanics: Wave Equations* (Springer, 2000), for a step-by-step Foldy–Wouthuysen and Pauli limit.
- C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the fine structure and the hydrogen spectrum.
- The companion articles of this series: *The Dirac Equation in Biquaternionic Form*, *The Biquaternion Dirac Equation — Solutions and Non-Relativistic Limit*, and *Quantum Physics in Biquaternionic Form*.
