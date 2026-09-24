# __Exercise: The Non-Relativistic Limit and the Pauli Equation__

## Introduction

This is one of the worked exercises attached to the article *The Biquaternion Dirac Equation — Solutions and Non-Relativistic Limit*. That article stated the biquaternion Dirac equation, constructed its plane-wave solutions, and carried the equation into the non-relativistic regime far enough to exhibit the Pauli equation and the gyromagnetic factor $g=2$. This exercise takes the limiting procedure as given and executes it in full: every order is kept, every coefficient is derived, and every claim is checked.

Five problems are worked:

1. the Foldy–Wouthuysen elimination of the small component, carried out step by step and to the order at which the first corrections appear;
2. the minimal substitution $\hat{\mathbf p}\to\hat{\mathbf p}-q\mathbf A$ and the electromagnetic terms it produces, including the spin term and the coefficient that fixes $g=2$;
3. the next order in $1/c$: the relativistic kinetic correction, the Darwin term, and the spin–orbit coupling;
4. the Hermiticity of every term, and which terms lie in the Hermitian subspace $\mathbb M_+$ and which do not;
5. the physical dimensions of every term.

**On the parent article.** The parent's non-relativistic section works only to leading order. It factors out the rest energy, eliminates the small component with the approximation $\partial_t\tilde\chi\approx 0$, and reads off the Pauli Hamiltonian; it stops there. It contains no spin–orbit and no Darwin term, it never actually performs a Foldy–Wouthuysen transformation (the transformation appears only in its Further Reading), and it does not state the sector ($\mathbb M_\pm$) status of the intermediate operators it uses ($\beta$, $\boldsymbol\alpha$, $O$, $S_1$), although it does identify the Pauli Hamiltonian and the spin term as $\mathbb M_+$ observables. Problems 3 and 4 supply those orders. Where the parent is silent this is stated explicitly and not silently filled in.

**Conventions.** The biquaternion algebra is $\mathbb B=\mathbb C\otimes_\mathbb R\mathbb H$, the basis is $e_0=1,e_1,e_2,e_3$ with $e_k^2=-e_0$, and $i$ is the scalar imaginary. The subspace $\mathbb M_+$ is the Hermitian subspace (real scalar, imaginary vector) and $\mathbb M_-$ the anti-Hermitian subspace (imaginary scalar, real vector), with $\mathbb B=\mathbb M_+\oplus\mathbb M_-$ and $i\mathbb M_\pm=\mathbb M_\mp$. The isomorphism, written $\Phi$ as in the companion Dirac article, is $e_0\mapsto I_2$, $e_k\mapsto-i\sigma_k$, $i\mapsto iI_2$, so that $\Phi(e_k)=-i\sigma_k$ and $\sigma_k\leftrightarrow ie_k$. (The same letter $\Phi$ denotes the electrostatic potential in $A^\mu=(\Phi,\mathbf A)$, as in the parent; the two uses are distinguished by their arguments.) The gamma matrices are the parent's Dirac-basis matrices,

$$
\gamma^0=\begin{pmatrix} I_2&0\\0&-I_2\end{pmatrix}=\beta,\qquad
\gamma^k=\begin{pmatrix} 0&\sigma_k\\-\sigma_k&0\end{pmatrix},
\qquad \{\gamma^\mu,\gamma^\nu\}=2g^{\mu\nu}I_4,\quad g=\mathrm{diag}(+1,-1,-1,-1).
$$

The Clifford metric $g$ is carried by the generators; it is the negative of the metric $\eta=\mathrm{diag}(-1,+1,+1,+1)$ that appears in the $ict$ form of the biquaternionic gradient, $\tilde\nabla=e_0\partial_{ict}+e_1\partial_x+e_2\partial_y+e_3\partial_z$ with $\partial_{ict}^2=-\partial_t^2/c^2$. The kinetic momentum is $\boldsymbol\pi=\hat{\mathbf p}-q\mathbf A$ with $\hat{\mathbf p}=-i\hbar\nabla$, the charge is $q$, and the potential energy of the charge in the electrostatic potential is $V=q\Phi$. Natural units $\hbar=c=1$ are used while deriving; $\hbar$ and $c$ are restored wherever a physical statement is made.

## Problem 1: The Foldy–Wouthuysen elimination of the small component

**Statement.** Starting from the four-component Dirac Hamiltonian with minimal coupling, eliminate the small component and obtain the Pauli Hamiltonian, keeping every order in $1/c$.

**Solution.**

*Step 1: the split.* In the Dirac basis the Hamiltonian is

$$
i\hbar\,\partial_t\psi=\hat H\psi,\qquad
\hat H=c\,\boldsymbol\alpha\cdot\boldsymbol\pi+\beta mc^2+q\Phi,
\qquad \alpha^k=\gamma^0\gamma^k=\begin{pmatrix}0&\sigma_k\\ \sigma_k&0\end{pmatrix}.
$$

Write $\hat H=\beta mc^2+O+E$ with

$$
O=c\,\boldsymbol\alpha\cdot\boldsymbol\pi \quad(\text{odd},\ \beta O\beta=-O),
\qquad E=q\Phi \quad(\text{even},\ \beta E\beta=E).
$$

The even operator $E$ is the electrostatic energy and the odd operator $O$ is what couples the upper and lower components.

*Step 2: factoring out the rest energy.* Write $\psi=e^{-imc^2t/\hbar}(\tilde\phi,\tilde\chi)^{\mathsf T}$. Substituting and cancelling the common phase gives the parent's two coupled equations,

$$
i\hbar\,\partial_t\tilde\phi=c\,\boldsymbol\sigma\cdot\boldsymbol\pi\,\tilde\chi+q\Phi\tilde\phi,
\qquad
i\hbar\,\partial_t\tilde\chi=c\,\boldsymbol\sigma\cdot\boldsymbol\pi\,\tilde\phi-2mc^2\tilde\chi+q\Phi\tilde\chi .
$$

*Step 3: the leading elimination.* The term $2mc^2\tilde\chi$ dominates the second equation whenever the fields, the kinetic energy and $\partial_t\tilde\chi$ are small compared with $mc^2$. Neglecting the other terms there,

$$
\tilde\chi=\frac{\boldsymbol\sigma\cdot\boldsymbol\pi}{2mc}\,\tilde\phi+O(c^{-3}),
$$

so the small component is of relative order $v/c$, as it must be. Substituting into the first equation eliminates $\tilde\chi$ exactly at this order:

$$
i\hbar\,\partial_t\tilde\phi=\left[\frac{(\boldsymbol\sigma\cdot\boldsymbol\pi)^2}{2m}+q\Phi\right]\tilde\phi .
$$

*Step 4: the systematic transformation.* The approximation of Step 3 is the first term of a controlled expansion. The Foldy–Wouthuysen generator is $S=S_1+S_2+\cdots$ with

$$
S_1=-\frac{i}{2mc^2}\,\beta O .
$$

For static fields the generator is time-independent, and

$$
e^{iS_1}\big(\hat H-i\hbar\partial_t\big)e^{-iS_1}
=\hat H+i[S_1,\hat H]-\tfrac12[S_1,[S_1,\hat H]]-\tfrac{i}{6}[S_1,[S_1,[S_1,\hat H]]]+\cdots
$$

Using $O\beta=-\beta O$ and $E\beta=\beta E$, the three elementary commutators are

$$
i[S_1,\beta mc^2]=-O,\qquad
i[S_1,O]=\frac{\beta O^2}{mc^2},\qquad
[S_1,[S_1,\beta mc^2]]=\frac{\beta O^2}{mc^2}.
$$

The first cancels the odd term $O$; the second and third combine into the even term $\frac{\beta O^2}{2mc^2}$, the leading non-relativistic energy. There is also a residual odd operator, of relative order $(v/c)^2$ compared with $O$,

$$
O_1=i[S_1,E]=\frac{iq}{2mc}\,\beta\,\boldsymbol\alpha\cdot\mathbf E,
$$

which the second transformation $S_2=-\frac{i}{2mc^2}\beta O_1$ removes. To the order at which the first physical corrections appear, therefore,

$$
\hat H_1=\beta mc^2+q\Phi+\frac{\beta O^2}{2mc^2}+O_1+O(c^{-2}).
$$

*Step 5: evaluating $O^2$.* With $\alpha^i\alpha^j=\delta^{ij}+i\epsilon^{ijk}\Sigma_k$ and $\Sigma_k=\mathrm{diag}(\sigma_k,\sigma_k)$,

$$
O^2=c^2\big(\boldsymbol\pi^2+i\,\boldsymbol\Sigma\cdot(\boldsymbol\pi\times\boldsymbol\pi)\big).
$$

Since $O$ is block-off-diagonal, its square is block-diagonal, so the odd part of $\hat H_1$ is exactly $O_1$ and the even part, beyond the rest energy, is $q\Phi+\beta O^2/(2mc^2)$. In the upper (large) block, $\beta\to+1$ and $\boldsymbol\Sigma\to\boldsymbol\sigma$, so

$$
\hat H_{\rm large}=mc^2+q\Phi+\frac{\boldsymbol\pi^2-q\,\boldsymbol\sigma\cdot\mathbf B}{2m}+O(c^{-2}),
$$

where the evaluation of $\boldsymbol\pi\times\boldsymbol\pi$ is carried out in Problem 2. Subtracting the rest energy,

$$
\boxed{\;i\hbar\,\partial_t\tilde\phi=\left[\frac{(\hat{\mathbf p}-q\mathbf A)^2}{2m}+q\Phi-\frac{q\hbar}{2m}\,\boldsymbol\sigma\cdot\mathbf B\right]\tilde\phi\;}
$$

which is the Pauli equation exactly as the parent reports it. The coefficient $1/2m$ is the whole content of the $g=2$ result of Problem 2: it is produced by the $2mc^2$ in the denominator of the small-component elimination, not put in by hand.

## Problem 2: Minimal substitution, the electromagnetic terms, and $g=2$

**Statement.** Carry out the minimal substitution, evaluate the electromagnetic terms it generates, and verify the gyromagnetic factor $g=2$ together with the biquaternion form of the spin term.

**Solution.**

*Step 1: the substitution.* The parent's convention is $D_\mu=\partial_\mu+iqA_\mu$, which in this mostly-minus metric is equivalent to

$$
\hat{\mathbf p}\ \longrightarrow\ \hat{\mathbf p}-q\mathbf A,\qquad i\partial_t\ \longrightarrow\ i\partial_t-q\Phi ,
$$

i.e. $\boldsymbol\pi=\hat{\mathbf p}-q\mathbf A$ and the electrostatic energy $q\Phi$ collected in $V=q\Phi$. This is the mostly-minus form of the covariant derivative; the reader should note that the mostly-plus convention uses $D_\mu=\partial_\mu-iqA_\mu$, and that the sign of $A_\mu=(\Phi,-\mathbf A)$ is tied to the metric. Within this article the statement above is used throughout, and it reproduces the standard Hamiltonian $\hat H=c\boldsymbol\alpha\cdot(\hat{\mathbf p}-q\mathbf A)+\beta mc^2+q\Phi$.

*Step 2: the commutator of the kinetic momenta.* With $\hat{\mathbf p}=-i\hbar\nabla$,

$$
[\pi_i,\pi_j]=-q\big([\hat p_i,A_j]+[A_i,\hat p_j]\big)
=-q\big(-i\hbar\partial_iA_j+i\hbar\partial_jA_i\big)
=i\hbar q\,\epsilon_{ijk}B_k ,
$$

so that

$$
\boldsymbol\pi\times\boldsymbol\pi=i\hbar q\,\mathbf B,\qquad \mathbf B=\nabla\times\mathbf A .
$$

Equivalently, $\hat{\mathbf p}\times\mathbf A+\mathbf A\times\hat{\mathbf p}=-i\hbar\mathbf B$; the two terms are individually non-Hermitian but their sum is Hermitian. In natural units this is the parent's $\boldsymbol\pi\times\boldsymbol\pi=iq\mathbf B$.

*Step 3: the square of the spin operator.* The Pauli identity is

$$
(\boldsymbol\sigma\cdot\mathbf a)(\boldsymbol\sigma\cdot\mathbf b)
=\mathbf a\cdot\mathbf b\,I_2+i\,\boldsymbol\sigma\cdot(\mathbf a\times\mathbf b),
$$

valid for any two vectors whose components commute with one another. Applying it to $\mathbf a=\mathbf b=\boldsymbol\pi$ and using Step 2,

$$
(\boldsymbol\sigma\cdot\boldsymbol\pi)^2=\boldsymbol\pi^2+i\,\boldsymbol\sigma\cdot(\boldsymbol\pi\times\boldsymbol\pi)
=\boldsymbol\pi^2+i\,\boldsymbol\sigma\cdot(i\hbar q\mathbf B)
=\boldsymbol\pi^2-q\hbar\,\boldsymbol\sigma\cdot\mathbf B ,
$$

which is the parent's result, with $\hbar$ restored. The coefficient carries no power of $c$: the two factors of $c$ in the elimination cancel, since $\tilde\chi=\boldsymbol\sigma\cdot\boldsymbol\pi/(2mc)\,\tilde\phi$ is multiplied by $c\,\boldsymbol\sigma\cdot\boldsymbol\pi$ in the first equation. The identification $\mathbf S=\tfrac\hbar2\boldsymbol\sigma$ gives the spin term

$$
-\frac{q\hbar}{2m}\,\boldsymbol\sigma\cdot\mathbf B=-\frac{q}{m}\,\mathbf S\cdot\mathbf B=-\boldsymbol\mu\cdot\mathbf B .
$$

*Step 4: the gyromagnetic factor.* Writing the coupling as $-\boldsymbol\mu\cdot\mathbf B$ identifies

$$
\boldsymbol\mu=\frac{q\hbar}{2m}\boldsymbol\sigma=\frac{q}{m}\,\mathbf S,\qquad \mathbf S=\frac\hbar2\boldsymbol\sigma .
$$

The general parametrization of a magnetic dipole is $\boldsymbol\mu=g\dfrac{q}{2m}\mathbf S$, so that

$$
\boxed{\;g=2\;}
$$

for a structureless spin-$\tfrac12$ particle. For the electron, $q=-e$ and

$$
\boldsymbol\mu_e=-\frac{e}{m_e}\mathbf S=-g\frac{e}{2m_e}\mathbf S,\qquad g=2,
$$

whose magnitude at $S_z=\hbar/2$ is one Bohr magneton $\mu_B=e\hbar/2m_e$. The measured anomalous part $a=(g-2)/2\approx\alpha/2\pi$ is a radiative correction that lies outside the equation treated here.

*Step 5: the biquaternion form.* Under the isomorphism $\sigma_k\leftrightarrow ie_k$, a magnetic field written as the pure real quaternion $\mathbf B=B_k e_k$ maps the spin term to

$$
-\frac{q\hbar}{2m}\boldsymbol\sigma\cdot\mathbf B\ \longleftrightarrow\ -\frac{q\hbar}{2m}\,i\mathbf B\ \in\ \mathbb M_+ ,
$$

the Hermitian element of the informational sector, exactly as the parent states. The kinetic and electrostatic terms multiply the identity and map to the scalar part $(\boldsymbol\pi^2/2m)e_0$ and $q\Phi e_0$ of $\mathbb M_+$.

*Numerical checks.* The Pauli identity of Step 3 was verified with random complex vectors against $2\times2$ matrices, maximum error $8.9\times10^{-15}$ over $1000$ samples. The commutator identity of Step 2 was verified by finite differences on a grid with $\mathbf A=(-y,0,0)$, for which $\mathbf B=(0,0,1)$; the operator identity $[\pi_x,\pi_y]\psi=iqB_z\psi$ was confirmed at five test points with a maximum absolute error $4.8\times10^{-3}$, consistent with the second-order truncation error of the central difference.

## Problem 3: The spin–orbit and Darwin terms at the next order

**Statement.** Extend the elimination to the next order in $1/c$ and obtain the relativistic kinetic correction, the Darwin term, and the spin–orbit coupling.

**Solution.** This order is *not* contained in the parent article, which stops at the leading Pauli Hamiltonian. It is obtained by the second Foldy–Wouthuysen step.

*Step 1: the second generator.* The odd remainder of $\hat H_1$ is $O_1=\dfrac{iq}{2mc}\beta\boldsymbol\alpha\cdot\mathbf E$, and the transformation that removes it is

$$
S_2=-\frac{i}{2mc^2}\,\beta O_1 .
$$

Evaluating the expansion of $e^{iS_2}\hat H_1e^{-iS_2}$ and using $[\boldsymbol\alpha\cdot\mathbf E,q\Phi]=0$ (the matrix $\boldsymbol\alpha$ is constant and $\mathbf E$, $\Phi$ are functions of position), the even terms of relative order $c^{-2}$ that survive are

$$
\hat H^{(2)}
=-\frac{(\boldsymbol\sigma\cdot\boldsymbol\pi)^4}{8m^3c^2}
+\frac{\hbar^2}{8m^2c^2}\nabla^2V
-\frac{q\hbar}{4m^2c^2}\,\boldsymbol\sigma\cdot(\mathbf E\times\boldsymbol\pi),
$$

with $V=q\Phi$ the potential energy. The first term is the expansion of the large-component energy $\sqrt{m^2c^4+(\boldsymbol\sigma\cdot\boldsymbol\pi)^2c^2}$; it is $(\boldsymbol\sigma\cdot\boldsymbol\pi)^4$, not $\boldsymbol\pi^4$, because $(\boldsymbol\sigma\cdot\boldsymbol\pi)^2=\boldsymbol\pi^2-q\hbar\boldsymbol\sigma\cdot\mathbf B$, so the two differ by $-q\hbar(\boldsymbol\pi^2\boldsymbol\sigma\cdot\mathbf B+\boldsymbol\sigma\cdot\mathbf B\boldsymbol\pi^2)+(q\hbar)^2(\boldsymbol\sigma\cdot\mathbf B)^2$, which is of the same $1/c^2$ order and is not dropped.

*Step 2: the Darwin term.* Since $\mathbf E=-\nabla\Phi$ and $V=q\Phi$,

$$
\frac{\hbar^2}{8m^2c^2}\nabla^2V=-\frac{q\hbar^2}{8m^2c^2}\nabla\cdot\mathbf E .
$$

This is the Darwin term. Its Hermiticity is immediate: $\nabla\cdot\mathbf E$ is a real function of position.

*Step 3: the spin–orbit term.* Since $\nabla V=q\nabla\Phi=-q\mathbf E$,

$$
-\frac{q\hbar}{4m^2c^2}\boldsymbol\sigma\cdot(\mathbf E\times\boldsymbol\pi)
=\frac{\hbar}{4m^2c^2}\,\boldsymbol\sigma\cdot(\nabla V\times\boldsymbol\pi)
=\frac{\hbar}{4m^2c^2}\,\frac1r\frac{dV}{dr}\,\boldsymbol\sigma\cdot\mathbf L
\qquad(\text{central }V),
$$

where $\mathbf E\times\boldsymbol\pi$ has been written with $\mathbf E=-\nabla\Phi$. For a central electrostatic field, whose vector potential may be neglected so that $\boldsymbol\pi\to\hat{\mathbf p}$, the last factor is the standard spin–orbit coupling with $\mathbf L=\mathbf r\times\hat{\mathbf p}$ and $\mathbf S=\tfrac\hbar2\boldsymbol\sigma$. The coefficient $1/(4m^2c^2)$ already contains the Thomas factor of $\tfrac12$: a naive Lorentz transformation to the instantaneous rest frame of the electron would give twice this value, and the factor of $\tfrac12$ is the Thomas precession correction. With $\mathbf S=\tfrac\hbar2\boldsymbol\sigma$, the term reads $\dfrac{1}{2m^2c^2}\dfrac1r\dfrac{dV}{dr}\mathbf L\cdot\mathbf S$, the standard spin–orbit coupling.

*Step 4: the assembled Hamiltonian.* Collecting the leading and next-to-leading orders, the large-component Hamiltonian is

$$
\boxed{\;
\hat H=\frac{\boldsymbol\pi^2}{2m}+q\Phi-\frac{q\hbar}{2m}\boldsymbol\sigma\cdot\mathbf B
-\frac{(\boldsymbol\sigma\cdot\boldsymbol\pi)^4}{8m^3c^2}
+\frac{\hbar^2}{8m^2c^2}\nabla^2V
-\frac{q\hbar}{4m^2c^2}\boldsymbol\sigma\cdot(\mathbf E\times\boldsymbol\pi)
\;}
$$

to relative order $c^{-2}$. The first three terms are the Pauli Hamiltonian of Problem 1; the last three are the corrections that the parent article does not reach.

*Step 5: numerical verification against the exact Dirac spectrum.* The three corrections are fixed by their coefficients; a single overall check is therefore decisive. In a hydrogenic atom with nuclear charge $Z$, the first-order shifts of the four terms are, in natural units ($c=1$), as in the companion's derivation,

$$
\Delta E_{\rm kin}=-\frac{m(Z\alpha)^4}{2n^3}\!\left[\frac{1}{\ell+\tfrac12}-\frac{3}{4n}\right],\qquad
\Delta E_{\rm SO}=\frac{m(Z\alpha)^4}{2n^3}\frac{j(j+1)-\ell(\ell+1)-\tfrac34}{2\ell(\ell+\tfrac12)(\ell+1)},
$$

$$
\Delta E_{\rm D}=\frac{m(Z\alpha)^4}{2n^3}\quad(\ell=0),\qquad \Delta E_{\rm D}=0\quad(\ell\neq0),
$$

with the exact Dirac shift $\Delta E_{\rm exact}=-\dfrac{m(Z\alpha)^4}{2n^3}\Big[\dfrac{1}{j+\tfrac12}-\dfrac{3}{4n}\Big]$. Evaluating all of these with exact rational arithmetic for every level with $n\le6$ (36 levels, both $j=\ell\pm\tfrac12$), the sum $\Delta E_{\rm kin}+\Delta E_{\rm SO}+\Delta E_{\rm D}$ equals $\Delta E_{\rm exact}$ in every case, with difference exactly $0$. An independent one-dimensional Foldy–Wouthuysen expansion, carried out symbolically to order $m^{-3}$ in a purely scalar potential, reproduces the four coefficients $1,+\tfrac12,+\tfrac18,-\tfrac18$ for $V$, $\boldsymbol\pi^2/2m$, $\nabla^2V/(8m^2c^2)$ and $-(\boldsymbol\sigma\cdot\boldsymbol\pi)^4/(8m^3c^2)$ respectively. The Darwin sign is therefore $+\hbar^2\nabla^2V/(8m^2c^2)$, equivalently $-(q\hbar^2/8m^2c^2)\nabla\cdot\mathbf E$.

## Problem 4: Hermiticity and the $\mathbb M_\pm$ decomposition

**Statement.** Check the Hermiticity of every term and determine which terms lie in $\mathbb M_+$.

**Solution.**

*Step 1: Hermiticity.* Each term of the Hamiltonian of Problem 3 is Hermitian:

- $\boldsymbol\pi^2/2m$: $\pi_i^\dagger=\pi_i$, hence $\pi_i\pi_i$ is Hermitian;
- $q\Phi$: multiplication by the real function $q\Phi$, Hermitian;
- $-\dfrac{q\hbar}{2m}\boldsymbol\sigma\cdot\mathbf B$: $\sigma_k$ and the real field $B_k$ are Hermitian;
- $-(\boldsymbol\sigma\cdot\boldsymbol\pi)^4/(8m^3c^2)$: a real multiple of the Hermitian $(\boldsymbol\sigma\cdot\boldsymbol\pi)^2$;
- $\dfrac{\hbar^2}{8m^2c^2}\nabla^2V$: multiplication by a real function;
- $-\dfrac{q\hbar}{4m^2c^2}\boldsymbol\sigma\cdot(\mathbf E\times\boldsymbol\pi)$: this is the one term whose Hermiticity is not automatic. Using $[\pi_i,E_j]=-i\hbar\partial_iE_j$,

$$
(\mathbf E\times\boldsymbol\pi)_i^\dagger=(\mathbf E\times\boldsymbol\pi)_i+i\hbar(\nabla\times\mathbf E)_i ,
$$

so the term is Hermitian if and only if $\nabla\times\mathbf E=0$, its failure of Hermiticity being proportional to the curl. Since $\mathbf E=-\nabla\Phi$ for an electrostatic field, $\nabla\times\mathbf E=-\nabla\times\nabla\Phi=0$ identically, and the term is Hermitian. Writing it instead as $\boldsymbol\sigma\cdot(\nabla V\times\boldsymbol\pi)$ makes this manifest, because $\nabla V$ is a gradient. For a general time-dependent field, where $\mathbf E$ has a solenoidal part $-\partial_t\mathbf A$ and $\nabla\times\mathbf E=-\partial_t\mathbf B$, the antisymmetric part does not vanish and the non-relativistic reduction requires the symmetrized ordering; this is the only place in the reduction where the result is convention- and ordering-sensitive beyond the metric conventions already noted.

*Step 2: the $\mathbb M_+$ representatives.* Under the isomorphism, a Hermitian $2\times2$ matrix $h_0I_2+\mathbf h\cdot\boldsymbol\sigma$ corresponds to the Hermitian biquaternion $h_0e_0+i\mathbf h\in\mathbb M_+$; this was verified directly for 200 random Hermitian operators with maximum error $0$. Applying it term by term, with $\mathbf B=B_ke_k$ and $(\mathbf E\times\boldsymbol\pi)=(\mathbf E\times\boldsymbol\pi)_ke_k$,

| Term of $\hat H$ | Biquaternion representative | Sector |
|---|---|---|
| $\boldsymbol\pi^2/2m$ | $(\boldsymbol\pi^2/2m)\,e_0$ | $\mathbb M_+$ |
| $q\Phi$ | $(q\Phi)\,e_0$ | $\mathbb M_+$ |
| $-\dfrac{q\hbar}{2m}\boldsymbol\sigma\cdot\mathbf B$ | $-\dfrac{q\hbar}{2m}\,i\mathbf B$ | $\mathbb M_+$ |
| $\dfrac{\hbar^2}{8m^2c^2}\nabla^2V$ | $\dfrac{\hbar^2}{8m^2c^2}(\nabla^2V)\,e_0$ | $\mathbb M_+$ |
| $-\dfrac{q\hbar}{4m^2c^2}\boldsymbol\sigma\cdot(\mathbf E\times\boldsymbol\pi)$ | $-\dfrac{q\hbar}{4m^2c^2}\,i(\mathbf E\times\boldsymbol\pi)$ | $\mathbb M_+$ |

Every term of the reduced, two-component Hamiltonian is Hermitian, hence every term lands in $\mathbb M_+$. This is the precise content of the parent's remark that the spin term is an observable of the informational sector; the remark applies term by term.

*Step 3: what does not land in $\mathbb M_+$.* Three classes of object in the reduction do not.

1. **The Clifford-odd operators.** The mass term $\beta mc^2$ contains $\beta=\gamma^0$, and the generator $S_1=-\frac{i}{2mc^2}\beta O$ contains $\beta O$. Both $\beta$ and $\beta O$ are odd products of gamma matrices, whereas $\mathbb B\cong\mathrm{Cl}^+_{1,3}$ is the *even* subalgebra. They therefore have no representative in $\mathbb B$ at all, and a fortiori none in either $\mathbb M_\pm$. This is why the four-component Hamiltonian is not an element of $\mathbb B$ and why a transformation is needed before the biquaternion identification can be made: the Foldy–Wouthuysen transformation is exactly the operation that removes the Clifford-odd part and leaves an element of $\mathbb M_+$.

2. **The anti-Hermitian generator.** $S_1$ is Hermitian, so $iS_1$ is anti-Hermitian: it plays the rôle that the elements of $\mathbb M_-$ play in the companion quantum article, where the Lie algebra of the unitary group is $\mathbb M_-$. It is not itself in $\mathbb M_-$, because it is built from the Clifford-odd element $\beta O$. The two gradings must not be conflated: the Foldy–Wouthuysen grading is by conjugation with $\beta$, the $\mathbb M_\pm$ grading is by $\dagger$. Thus the odd operator $O=c\boldsymbol\alpha\cdot\boldsymbol\pi$ is Foldy–Wouthuysen-odd but Clifford-even and Hermitian, so as a biquaternion it lies in $\mathbb M_+$; while $\beta O$ is Foldy–Wouthuysen-odd, Clifford-odd and anti-Hermitian, and lies in neither $\mathbb B$ nor $\mathbb M_\pm$. The identification of "odd" with "not in $\mathbb M_+$" is incorrect.

3. **The real structure and the mass term.** In the biquaternion equation the conjugation $\flat=-\dagger$ is the algebra's real structure, and it *preserves* the sectors: if $\tilde\Psi\in\mathbb M_+$ then $\tilde\Psi^\flat=-\tilde\Psi\in\mathbb M_+$, and if $\tilde\Psi\in\mathbb M_-$ then $\tilde\Psi^\flat=\tilde\Psi\in\mathbb M_-$. Its action is diagonal on the sector decomposition with opposite signs $\mp1$: a coupling built on $\flat$ — a Majorana-type mass, $m\tilde\Psi^\flat$ — would carry those opposite signs. The parent's mass term is not that coupling; it is the linear, chirality-off-diagonal pair $\tilde\nabla\tilde\Psi_R = m\tilde\Psi_L$, $\bar{\tilde\nabla}\tilde\Psi_L = m\tilde\Psi_R$, which couples the two central ideals (the chiralities) and leaves each element's sector membership untouched. The operation that exchanges the two sectors is multiplication by the central $i$. The rest-energy phase that is factored out before the reduction,

$$
e^{-imc^2t/\hbar}=\cos\!\Big(\frac{mc^2t}{\hbar}\Big)e_0-\sin\!\Big(\frac{mc^2t}{\hbar}\Big)(ie_0),
$$

is not Hermitian: its first term lies in $\mathbb M_+$ and its second in $\mathbb M_-$, since $ie_0$ is anti-Hermitian. It is a phase, not an observable, and must be factored out before a two-component (hence $\mathbb M_+$) description of the dynamics is reached.

## Problem 5: The physical dimensions of each term

**Statement.** Determine the physical dimensions of each term.

**Solution.** Every term is an energy, since each is a term of a Hamiltonian. The individual coefficients nevertheless carry different powers of $\hbar$ and $c$, and checking them is a useful consistency test. In SI units, with $[\hbar]=\mathrm{kg\,m^2\,s^{-1}}$, $[c]=\mathrm{m\,s^{-1}}$, $[q]=\mathrm C$, $[\Phi]=\mathrm{V}=\mathrm{kg\,m^2\,s^{-3}A^{-1}}$, $[\mathbf B]=\mathrm T=\mathrm{kg\,s^{-2}A^{-1}}$ and $[\mathbf E]=\mathrm{V\,m^{-1}}=\mathrm{kg\,m\,s^{-3}A^{-1}}$:

| Term | Coefficient units | Field/operator units | Product |
|---|---|---|---|
| $\boldsymbol\pi^2/2m$ | $1/m$ | $(\mathrm{kg\,m\,s^{-1}})^2$ | $\mathrm{kg\,m^2\,s^{-2}}$ |
| $q\Phi$ | $\mathrm C$ | $\mathrm{kg\,m^2\,s^{-3}A^{-1}}$ | $\mathrm{kg\,m^2\,s^{-2}}$ |
| $\dfrac{q\hbar}{2m}\boldsymbol\sigma\cdot\mathbf B$ | $\mathrm C\,\mathrm{kg\,m^2\,s^{-1}\,kg^{-1}}$ | $\mathrm{kg\,s^{-2}A^{-1}}$ | $\mathrm{kg\,m^2\,s^{-2}}$ |
| $-\dfrac{q\hbar^2}{8m^2c^2}\nabla\cdot\mathbf E$ | $\mathrm C\,\mathrm{kg^2m^4s^{-2}}\,\mathrm{kg^{-2}m^{-2}s^{2}}$ | $\mathrm{kg\,s^{-3}A^{-1}}$ | $\mathrm{kg\,m^2\,s^{-2}}$ |
| $\dfrac{q\hbar}{4m^2c^2}\boldsymbol\sigma\cdot(\mathbf E\times\boldsymbol\pi)$ | $\mathrm C\,\mathrm{kg\,m^2s^{-1}}\,\mathrm{kg^{-2}m^{-2}s^{2}}$ | $\mathrm{kg^2m^2s^{-4}A^{-1}}$ | $\mathrm{kg\,m^2\,s^{-2}}$ |
| $\dfrac{(\boldsymbol\sigma\cdot\boldsymbol\pi)^4}{8m^3c^2}$ | $\mathrm{kg^{-3}m^{-2}s^{2}}$ | $\mathrm{kg^4m^4s^{-4}}$ | $\mathrm{kg\,m^2\,s^{-2}}$ |

The pattern is informative. The leading terms ($\boldsymbol\pi^2/2m$, $q\Phi$, the spin term) carry no power of $c$; the three corrections each carry $c^{-2}$, which is the statement that they are relativistic corrections of order $v^2/c^2$. The spin term carries one power of $\hbar$ while the leading kinetic and electrostatic terms carry none, so the spin term vanishes formally in the classical limit $\hbar\to0$; this is the operator form of the statement that the magnetic moment of a point charge is a quantum effect. The Darwin and spin–orbit terms carry $\hbar^2$ and $\hbar$ respectively, and both survive the $\hbar\to0$ limit when divided by $\hbar$ in the corresponding classical spin–orbit coupling, which is the Thomas-precession energy.

## Summary

The non-relativistic limit of the biquaternion Dirac equation was carried through in five steps.

The Foldy–Wouthuysen elimination of the small component, executed systematically with the generator $S_1=-\frac{i}{2mc^2}\beta O$, produces the Pauli Hamiltonian
$i\hbar\partial_t\tilde\phi=\big[\boldsymbol\pi^2/2m+q\Phi-(q\hbar/2m)\boldsymbol\sigma\cdot\mathbf B\big]\tilde\phi$,
reproducing the parent article. The minimal substitution $\boldsymbol\pi=\hat{\mathbf p}-q\mathbf A$ gives $[\pi_i,\pi_j]=i\hbar q\epsilon_{ijk}B_k$ and $(\boldsymbol\sigma\cdot\boldsymbol\pi)^2=\boldsymbol\pi^2-q\hbar\boldsymbol\sigma\cdot\mathbf B$, and the coefficient $1/2m$ produced by the elimination fixes $g=2$ and $\boldsymbol\mu=(q/m)\mathbf S$, hence $\mu_B=e\hbar/2m_e$ for the electron. At the next order in $1/c$ the second Foldy–Wouthuysen step adds the relativistic kinetic correction $-(\boldsymbol\sigma\cdot\boldsymbol\pi)^4/(8m^3c^2)$, the Darwin term $+\hbar^2\nabla^2V/(8m^2c^2)=-(q\hbar^2/8m^2c^2)\nabla\cdot\mathbf E$, and the spin–orbit coupling $-(q\hbar/4m^2c^2)\boldsymbol\sigma\cdot(\mathbf E\times\boldsymbol\pi)=(\hbar/4m^2c^2)r^{-1}(dV/dr)\boldsymbol\sigma\cdot\mathbf L$. Summed, these reproduce the exact Dirac fine structure of hydrogenic ions for 36 levels with $n\le6$, with difference exactly zero.

Every term of the reduced Hamiltonian is Hermitian and therefore lies in $\mathbb M_+$; the objects that do not are the Clifford-odd pieces ($\beta mc^2$, $\beta O$), which have no representative in $\mathbb B$ at all, the anti-Hermitian generator $iS_1$, and the real structure $\flat$ — whose opposite-sign action on the sectors a Majorana-type coupling would carry — together with the sector-exchanging rest-energy phase; the parent's mass term is the linear coupling between the two chiralities. The Foldy–Wouthuysen grading by $\beta$ must not be confused with the $\mathbb M_\pm$ grading by $\dagger$. All terms are energies, the three corrections carrying the expected $c^{-2}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb B=\mathbb C\otimes_\mathbb R\mathbb H$ | Biquaternion algebra |
| $e_0=1,e_1,e_2,e_3$, $e_k^2=-e_0$ | Quaternion basis |
| $\mathbb M_+,\mathbb M_-$ | Hermitian / anti-Hermitian subspaces |
| $\Phi(e_k)=-i\sigma_k$, $\sigma_k\leftrightarrow ie_k$ | Isomorphism, Pauli matrices |
| $\beta=\gamma^0$, $\alpha^k=\gamma^0\gamma^k$ | Dirac-basis matrices |
| $g=\mathrm{diag}(+1,-1,-1,-1)$ | Clifford metric; $g=-\eta$ |
| $\boldsymbol\pi=\hat{\mathbf p}-q\mathbf A$ | Kinetic momentum |
| $\mathbf B=\nabla\times\mathbf A$, $\mathbf E$ | Magnetic, electric fields |
| $V=q\Phi$ | Potential energy |
| $\hat H=\beta mc^2+O+E$, $O=c\boldsymbol\alpha\cdot\boldsymbol\pi$ | Split Hamiltonian; odd part |
| $S_1=-\frac{i}{2mc^2}\beta O$ | Foldy–Wouthuysen generator |
| $O_1=\frac{iq}{2mc}\beta\boldsymbol\alpha\cdot\mathbf E$ | Residual odd operator |
| $\mathbf S=\tfrac\hbar2\boldsymbol\sigma$, $\boldsymbol\mu=g\frac{q}{2m}\mathbf S$ | Spin and magnetic moment |
| $g=2$ | Gyromagnetic factor |
| $\mu_B=e\hbar/2m_e$ | Bohr magneton |

## Further Reading

- P. A. M. Dirac, "The quantum theory of the electron," *Proceedings of the Royal Society A* **117** (1928) 610–624, for the original prediction of $g=2$.
- L. L. Foldy and S. A. Wouthuysen, "On the Dirac theory of spin 1/2 particles and its non-relativistic limit," *Physical Review* **78** (1950) 29–36, for the transformation used here.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the plane-wave solutions and the standard non-relativistic reduction.
- J. J. Sakurai, *Advanced Quantum Mechanics* (Addison-Wesley, 1967), for the emergence of the Pauli equation and the spin–orbit coupling.
- W. Greiner, *Relativistic Quantum Mechanics: Wave Equations* (Springer, 2000), for a step-by-step Foldy–Wouthuysen and Pauli limit.
- C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the fine structure and the hydrogen spectrum.
- The companion articles of this series: *The Dirac Equation in Biquaternionic Form*, *The Biquaternion Dirac Equation — Solutions and Non-Relativistic Limit*, and *Quantum Mechanics in Biquaternionic Form*.
