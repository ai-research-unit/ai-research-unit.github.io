# __Exercise: The Non-Relativistic Limit and the Pauli Equation__

## Introduction

This is one of the worked exercises attached to the article *The Dirac Equation in Biquaternionic Form — Solutions and the Non-Relativistic Limit*. That article states the two forms of the biquaternion Dirac equation, constructs the plane-wave solutions of the one-sided pair, and carries the pair into the non-relativistic regime far enough to exhibit the Pauli equation and the gyromagnetic factor $g=2$. This exercise takes the limiting procedure as given and executes it in full: every order that contributes to the first corrections is kept, every coefficient is derived, and every claim is checked.

Five problems are worked:

1. the Foldy–Wouthuysen elimination of the small component, carried out step by step and to the order at which the first corrections appear;
2. the minimal substitution $p\to p-ϙ\vec A$ and the electromagnetic terms it produces, including the spin term and the coefficient that fixes $g=2$;
3. the next order in $1/c$: the relativistic kinetic correction, the Darwin term, and the spin–orbit coupling;
4. the Hermiticity of every term, and which terms lie in the Hermitian subspace $\mathbb M_+$ and which do not;
5. the physical dimensions of every term.

**On the parent article.** The parent's non-relativistic section works only to leading order. It factors out the rest energy, eliminates the small component with the approximation $\partial/\partial t'\,\chi\approx 0$, and reads off the Pauli Hamiltonian; it stops there. It contains no spin–orbit and no Darwin term, and it does not perform a systematic Foldy–Wouthuysen transformation. It also does not state the sector ($\mathbb M_\pm$) status of the intermediate operators it uses. Problems 3 and 4 supply those orders and that status. Where the parent is silent this is stated explicitly and not silently filled in.

**The cells.** The article is written in the cells of the frame, and the gamma symbols appear only in *The Gamma Formulation*. Write $L_a\psi=a\psi$ and $R_b\psi=\psi b$, so that $L_aR_b\psi=a\psi b$, with $L_aR_bL_cR_d=L_{ac}R_{db}$. The four coordinate cells are

$$
c_0=iR_{\vec e_x}^{\mathrm{pau}},\qquad c_k=iL_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}\quad(k=x,y,z),
$$

and the chirality cell is $-iR_{\vec e_z}^{\mathrm{pau}}=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}$, the parent's cell for chirality. The squares and the anticommutators follow from $i^2=-1$ and $\vec e_k^2=-e_t$:

$$
c_0^2=R_{(i\vec e_x)^2}^{\mathrm{pau}}=R_{i^2\vec e_x^2}=R_{e_t}^{\mathrm{pau}}=1,\qquad
c_k^2=L_{(i\vec e_k)^2}^{\mathrm{pau}}R_{\vec e_y^2}^{\mathrm{pau}}=L_{e_t}^{\mathrm{pau}}R_{-e_t}^{\mathrm{pau}}=-1,
$$

$$
\{c_0,c_k\}=0,\qquad \{c_j,c_k\}=-2\delta_{jk}.
$$

Repeated spatial indices $j,k,l$ are summed over $x,y,z$, and the sums are written out only where a chain of equalities would otherwise be ambiguous.

The velocity cell is one product of two coordinate cells, and one use of $i^2=-1$ removes both factors of $i$:

$$
\alpha_k=c_0c_k=iR_{\vec e_x}^{\mathrm{pau}}\,iL_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}
=i^2L_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y\vec e_x}^{\mathrm{pau}}
=-L_{\vec e_k}^{\mathrm{pau}}R_{-\vec e_z}^{\mathrm{pau}}
=L_{\vec e_k}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}.
$$

In the Dirac basis, where $c_0=\operatorname{diag}(I_2,-I_2)$, the velocity cell is $\alpha_k=\begin{pmatrix}0&\sigma_k\\\sigma_k&0\end{pmatrix}$. The spin cell is $S_k=iL_{\vec e_k}^{\mathrm{pau}}$; it is block diagonal in that basis, with upper block $\sigma_k$ and lower block $-\sigma_k$, and it satisfies

$$
\alpha_j\alpha_k=\delta_{jk}+i\epsilon_{jkl}S_l .
$$

The Clifford metric is $g=\operatorname{diag}(+1,-1,-1,-1)$, the negative of the metric $\eta=\operatorname{diag}(-1,+1,+1,+1)$ that appears in the $ict'$ form of the biquaternionic gradient. The kinetic momentum is $\vec\pi=p-ϙ\vec A$ with $p=-i\hbar\nabla$, the charge is $ϙ$, the electrostatic potential is written $\Phi$, and the potential energy of the charge in it is $V=ϙ\Phi$. Natural units $\hbar=c=1$ are used while deriving; $\hbar$ and $c$ are restored wherever a physical statement is made.

### The two Dirac equations

The parent carries two equations, and they must not be read as one.

**The one-sided pair.** The corpus's own equation is the chiral pair. It acts on the two chiral halves $\tilde\Psi_R$ and $\tilde\Psi_L$ of the field by left multiplication, and the mass is the off-diagonal pairing of the two halves:

$$
\tilde\nabla\tilde\Psi_R=m\tilde\Psi_L,
$$

$$
\tilde\nabla^{\natural}\tilde\Psi_L=m\tilde\Psi_R .
$$

Both gradients act on the left, and no right multiplication and no conjugation enters. On the Dirac module the pair is a four-component equation, and it is the equation reduced below.

**The two-sided form.** Kravchenko's dictionary writes the same physics as a single equation on the whole algebra. The derivative acts on the left, the mass acts on the right through the chirality cell, and a componentwise conjugation supplies the antilinear part. Here $D_3=\sum_k\vec e_k\,\partial/\partial Q_k$ is the three-dimensional Cauchy–Riemann operator and $\mathcal N$ names the left-hand side. In natural units:

$$
\mathcal N F=\Bigl(i\frac{\partial}{\partial t'}+D_3\Bigr)F-mi\,\overline F\,\vec e_z=0 .
$$

Equivalently,

$$
-\tilde\nabla^{\natural}F-mi\,\overline F\,\vec e_z=0
$$

for a field $F\in\mathbb B$. The two forms are related by a change of representation, but they are different operators: the pair is linear in the field, while the mass term of the two-sided form is antilinear because it carries $\overline F$.

| | One-sided pair | Two-sided form |
|---|---|---|
| Equation | $\tilde\nabla\tilde\Psi_R=m\tilde\Psi_L$, $\tilde\nabla^{\natural}\tilde\Psi_L=m\tilde\Psi_R$ | $\mathcal NF=0$, with $\mathcal NF=(i\partial/\partial t'+D_3)F-mi\overline F\vec e_z$ |
| Multiplication | left by $\tilde\nabla$ and $\tilde\nabla^{\natural}$ | left by $i\partial/\partial t'$ and $D_3$; right by $\vec e_z$; antilinear bar |
| Field | $\tilde\Psi=\tilde\Psi_L+\tilde\Psi_R\in\Delta$ | $F\in\mathbb B$ |
| Mass | off-diagonal pairing of the chiral halves | $-mi\overline F\vec e_z$: a conjugation and a direction |
| Chirality | the central sign $\chi=i\tilde\Xi_{\mathrm{ad}}$ | the chirality cell $-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}$ |
| Use | the formulation and its kinematics | the dictionary, the Cauchy theory, the integral representation |

The reduction below is of the one-sided pair, read on the Dirac module. The Foldy–Wouthuysen transformation is applied to the four-component Hamiltonian of that pair. The two-sided form is a different operator, antilinear in its mass term; its non-relativistic reduction is not attempted here.

## Problem 1: The Foldy–Wouthuysen elimination of the small component

**Statement.** Starting from the four-component Dirac Hamiltonian with minimal coupling, eliminate the small component and obtain the Pauli Hamiltonian, keeping the orders through the first corrections.

**Solution.**

*Step 1: the split.* In the Dirac basis the Hamiltonian is

$$
i\hbar\,\partial/\partial t'\,\psi=H\psi,\qquad
H=c\sum_k\alpha_k\pi_k+c_0mc^2+ϙ\Phi,
\qquad
\alpha_k=c_0c_k=L_{\vec e_k}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}.
$$

Write $H=c_0mc^2+O+E$ with

$$
O=c\sum_k\alpha_k\pi_k\quad(\text{odd},\ c_0Oc_0=-O),
\qquad E=ϙ\Phi\quad(\text{even},\ c_0Ec_0=E).
$$

The even operator $E$ is the electrostatic energy and the odd operator $O$ is what couples the upper and lower components. One product with $c_0$ removes one velocity cell, since $c_0\alpha_k=c_0^2c_k=c_k$:

$$
c_0O=c\sum_k c_k\pi_k .
$$

*Step 2: factoring out the rest energy.* Write $\psi=\exp(-imc^2t'/\hbar)(\phi,\chi)^{\mathsf T}$. Substituting and cancelling the common phase gives the parent's two coupled equations,

$$
i\hbar\,\partial/\partial t'\,\phi=c\,\boldsymbol\sigma\cdot\vec\pi\,\chi+ϙ\Phi\phi,
$$

$$
i\hbar\,\partial/\partial t'\,\chi=c\,\boldsymbol\sigma\cdot\vec\pi\,\phi-2mc^2\chi+ϙ\Phi\chi .
$$

*Step 3: the leading elimination.* The term $2mc^2\chi$ dominates the second equation whenever the fields, the kinetic energy and $\partial/\partial t'\,\chi$ are small compared with $mc^2$. Neglecting the other terms there,

$$
\chi=\frac{\boldsymbol\sigma\cdot\vec\pi}{2mc}\,\phi+O(c^{-3}),
$$

so the small component is of relative order $v/c$, as it must be. Substituting into the first equation eliminates $\chi$ exactly at this order:

$$
i\hbar\,\partial/\partial t'\,\phi=\left[\frac{(\boldsymbol\sigma\cdot\vec\pi)^2}{2m}+ϙ\Phi\right]\phi .
$$

*Step 4: the systematic transformation.* The approximation of Step 3 is the first term of a controlled expansion. The Foldy–Wouthuysen generator is $S=S_1+S_2+\cdots$ with

$$
S_1=-\frac{i}{2mc^2}\,c_0O
=-\frac{i}{2mc^2}\,c_0\cdot c\sum_k c_0c_k\pi_k
=-\frac{i}{2mc}\sum_k c_k\pi_k
=\frac{1}{2mc}\sum_k L_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}\pi_k .
$$

The last equality is again $i^2=-1$, since $c_k=iL_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}$. For static fields the generator is time-independent, and the transformed Hamiltonian is

$$
e^{iS_1}He^{-iS_1}
=H+i[S_1,H]-\tfrac12[S_1,[S_1,H]]-\tfrac{i}{6}[S_1,[S_1,[S_1,H]]]+\cdots
$$

the full transformed operator being this expression minus $i\hbar\partial/\partial t'$. Using $c_0O=-Oc_0$ and $c_0E=Ec_0$, the three elementary commutators are

$$
i[S_1,c_0mc^2]=-O,\qquad
i[S_1,O]=\frac{c_0O^2}{mc^2},\qquad
[S_1,[S_1,c_0mc^2]]=\frac{c_0O^2}{mc^2}.
$$

The first cancels the odd term $O$. The second contributes $+\frac{c_0O^2}{mc^2}$ to the expansion and the third contributes $-\frac12$ of the same, so together they give $+\frac{c_0O^2}{2mc^2}$, the leading non-relativistic energy. There is also a residual odd operator, of relative order $(v/c)^2$ compared with $O$ for a Coulomb field,

$$
O_1=i[S_1,E]
=\frac{i}{2mc}\sum_k L_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}[\pi_k,E]
=\frac{i}{2mc}\sum_k L_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}(i\hbarϙE_k)
=-\frac{\hbarϙ}{2mc}\sum_k L_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}E_k,
$$

which the second transformation $S_2=-\frac{i}{2mc^2}c_0O_1$ removes. To the order at which the first physical corrections appear, therefore,

$$
H_1=c_0mc^2+ϙ\Phi+\frac{c_0O^2}{2mc^2}+O_1+O(c^{-2}).
$$

The omitted even term of order $c^{-2}$ is the second-order term $-\tfrac12[S_1,[S_1,E]]$; it is evaluated in Problem 3.

*Step 5: evaluating $O^2$.* With $\alpha_k=L_{\vec e_k}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}$ and $L_aR_bL_cR_d=L_{ac}R_{db}$,

$$
\alpha_j\alpha_k=L_{\vec e_j}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}L_{\vec e_k}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}
=L_{\vec e_j\vec e_k}^{\mathrm{pau}}R_{-e_t}^{\mathrm{pau}}
=-L_{\vec e_j\vec e_k}^{\mathrm{pau}}
=\delta_{jk}-\epsilon_{jkl}L_{\vec e_l}^{\mathrm{pau}},
$$

since $\vec e_j\vec e_k=-\delta_{jk}+\epsilon_{jkl}\vec e_l$. Therefore

$$
O^2=c^2\alpha_j\alpha_k\pi_j\pi_k
=c^2\left(\vec\pi^2-\epsilon_{jkl}L_{\vec e_l}^{\mathrm{pau}}\pi_j\pi_k\right).
$$

The commutator of the kinetic momenta is evaluated in Problem 2; here its consequence is $\epsilon_{jkl}\pi_j\pi_k=i\hbarϙB_l$, so

$$
O^2=c^2\left(\vec\pi^2-i\hbarϙL_{\vec e_l}^{\mathrm{pau}}B_l\right)
=c^2\left(\vec\pi^2-\hbarϙ\,iL_{\vec e_l}^{\mathrm{pau}}B_l\right).
$$

Since $O$ is block off-diagonal, its square is block diagonal; $O^2$ is even and commutes with $c_0$. In the upper (large) block, $c_0\to+1$ and the spin cell $iL_{\vec e_l}^{\mathrm{pau}}\to\sigma_l$, so

$$
O^2_{\rm large}=c^2\left(\vec\pi^2-\hbarϙ\,\boldsymbol\sigma\cdot\vec B\right),
\qquad
H_{\rm large}=mc^2+ϙ\Phi+\frac{\vec\pi^2-ϙ\hbar\,\boldsymbol\sigma\cdot\vec B}{2m}+O(c^{-2}).
$$

Subtracting the rest energy,

$$
\boxed{\;i\hbar\,\partial/\partial t'\,\phi=\left[\frac{(p-ϙ\vec A)^2}{2m}+ϙ\Phi-\frac{ϙ\hbar}{2m}\,\boldsymbol\sigma\cdot\vec B\right]\phi\;}
$$

which is the Pauli equation exactly as the parent reports it. The coefficient $1/2m$ is the whole content of the $g=2$ result of Problem 2: it is produced by the $2mc^2$ in the denominator of the small-component elimination, not put in by hand.

## Problem 2: Minimal substitution, the electromagnetic terms, and $g=2$

**Statement.** Carry out the minimal substitution, evaluate the electromagnetic terms it generates, and verify the gyromagnetic factor $g=2$ together with the biquaternion form of the spin term.

**Solution.**

*Step 1: the substitution.* The parent's minimal coupling replaces the four-momentum by $p_\mu-ϙA_\mu$, with the four-potential $A_\mu=(\Phi,-\vec A)$ in this mostly-minus metric. The spatial components give $p\to p-ϙ\vec A$, and the time component gives

$$
i\partial/\partial t'\ \longrightarrow\ i\partial/\partial t'-ϙ\Phi ,
$$

that is $\vec\pi=p-ϙ\vec A$ and the electrostatic energy $ϙ\Phi$ collected in $V=ϙ\Phi$. The sign of the coupling is tied to the metric and to the convention for $A_\mu$; the mostly-plus convention often writes the opposite sign. Within this article the statement above is used throughout, and it reproduces the standard Hamiltonian $H=c\sum_k\alpha_k(p_k-ϙA_k)+c_0mc^2+ϙ\Phi$, with $\alpha_k=c_0c_k$.

*Step 2: the commutator of the kinetic momenta.* With $p=-i\hbar\nabla$,

$$
[\pi_i,\pi_j]=-ϙ\bigl([p_i,A_j]+[A_i,p_j]\bigr)
=-ϙ\bigl(-i\hbar\partial/\partial Q_i\,A_j+i\hbar\partial/\partial Q_j\,A_i\bigr)
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

valid whenever the matrices $\sigma_k$ commute with every component $a_i$ and $b_j$. The components $a_i$ and $b_j$ need not commute among themselves, provided the cross product is read with the operator ordering kept. Applying it to $\vec a=\vec b=\vec\pi$ and using Step 2,

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

*Step 5: the biquaternion form.* Under the isomorphism $\sigma_k\leftrightarrow i\vec e_k$, the spin cell $iL_{\vec e_k}^{\mathrm{pau}}$ is the biquaternion representative of $\sigma_k$ on the upper block, and a magnetic field written as the pure real quaternion $\vec B=\sum_k B_k \vec e_k$ maps the spin term to

$$
-\frac{ϙ\hbar}{2m}\boldsymbol\sigma\cdot\vec B\ \longleftrightarrow\ -\frac{ϙ\hbar}{2m}\,i\vec B\ \in\ \mathbb M_+ ,
$$

the Hermitian element of the informational sector, exactly as the parent states. The kinetic and electrostatic terms multiply the identity and map to the scalar part $(\vec\pi^2/2m)e_t$ and $ϙ\Phi e_t$ of $\mathbb M_+$.

*Numerical check.* The commutator identity of Step 2 was verified by finite differences on a $41\times41$ grid with spacing $h=0.1$ on $[-2,2]^2$, with $\vec A=(-y,0,0)$, for which $\vec B=(0,0,1)$, and with the smooth test function $\psi=\exp(-(x^2+y^2))\cos(2x)\sin(3y)$. With $ϙ=\hbar=1$, the identity $[\pi_x,\pi_y]\psi=iB_z\psi$ was confirmed at the interior points with a maximum absolute error $4.8\times10^{-2}$; halving the spacing to $h=0.05$ gave $1.2\times10^{-2}$, the factor four of the second-order central difference.

## Problem 3: The spin–orbit and Darwin terms at the next order

**Statement.** Extend the elimination to the next order in $1/c$ and obtain the relativistic kinetic correction, the Darwin term, and the spin–orbit coupling.

**Solution.** This order is *not* contained in the parent article, which stops at the leading Pauli Hamiltonian. The even terms of order $c^{-2}$ have two sources. The second-order term $-\tfrac12[S_1,[S_1,E]]$ of the first transformation gives the Darwin and spin–orbit couplings; the expansion of the free large-block energy gives the relativistic kinetic correction. The second transformation removes the residual odd term $O_1$ and adds no even term at this order.

*Step 1: the even term of the first transformation.* From Step 4 of Problem 1,

$$
[S_1,E]=\frac{i\hbarϙ}{2mc}\sum_k L_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}E_k .
$$

A direct use of the cell algebra, with $[S_1,E]$ above and $S_1=\frac{1}{2mc}\sum_j L_{\vec e_j}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}\pi_j$, gives

$$
-\tfrac12[S_1,[S_1,E]]
=-\frac{\hbarϙ}{4m^2c^2}\,iL_{\vec e_l}^{\mathrm{pau}}(E\times\vec\pi)_l
-\frac{\hbar^2ϙ}{8m^2c^2}\,\nabla\cdot\vec E .
$$

The first term comes from the antisymmetric part of $\alpha_j\alpha_k=\delta_{jk}+i\epsilon_{jkl}S_l$; the second comes from the symmetric part. Since $\nabla\cdot\vec E=-\nabla^2V/ϙ$, the second term is the Darwin term $+\hbar^2\nabla^2V/(8m^2c^2)$. In the upper block, $iL_{\vec e_l}^{\mathrm{pau}}\to\sigma_l$, so the two terms read

$$
-\frac{\hbarϙ}{4m^2c^2}\,\boldsymbol\sigma\cdot(\vec E\times\vec\pi)
-\frac{\hbar^2ϙ}{8m^2c^2}\,\nabla\cdot\vec E .
$$

*Step 2: the Darwin term.* Since $\vec E=-\nabla\Phi$ and $V=ϙ\Phi$,

$$
\frac{\hbar^2}{8m^2c^2}\nabla^2V=-\frac{ϙ\hbar^2}{8m^2c^2}\nabla\cdot\vec E .
$$

This is the Darwin term. Its Hermiticity is immediate: $\nabla\cdot\vec E$ is a real function of position.

*Step 3: the spin–orbit term.* Since $\nabla V=ϙ\nabla\Phi=-ϙ\vec E$,

$$
-\frac{ϙ\hbar}{4m^2c^2}\boldsymbol\sigma\cdot(\vec E\times\vec\pi)
=\frac{\hbar}{4m^2c^2}\,\boldsymbol\sigma\cdot(\nabla V\times\vec\pi)
=\frac{\hbar}{4m^2c^2}\,\frac1r\frac{dV}{dr}\,\boldsymbol\sigma\cdot\vec L
\qquad(\text{central }V),
$$

where $\vec E\times\vec\pi$ has been written with $\vec E=-\nabla\Phi$. For a central electrostatic field, whose vector potential may be neglected so that $\vec\pi\to p$, the last factor is the standard spin–orbit coupling with $\vec L=\vec r\times p$ and $\vec S=\tfrac\hbar2\boldsymbol\sigma$. The coefficient $1/(4m^2c^2)$ already contains the Thomas factor of $\tfrac12$: a naive Lorentz transformation to the instantaneous rest frame of the electron would give twice this value, and the factor of $\tfrac12$ is the Thomas precession correction. With $\vec S=\tfrac\hbar2\boldsymbol\sigma$, the term reads $\dfrac{1}{2m^2c^2}\dfrac1r\dfrac{dV}{dr}\vec L\cdot\vec S$, the standard spin–orbit coupling.

*Step 4: the relativistic kinetic correction.* The free large-block energy is the expansion of $\sqrt{m^2c^4+O^2}$, and the next term is fixed by the same $O^2$:

$$
\sqrt{m^2c^4+O^2}
=mc^2+\frac{O^2}{2mc^2}-\frac{O^4}{8m^3c^6}+\cdots .
$$

In the upper block $O^4=c^4(\boldsymbol\sigma\cdot\vec\pi)^4$, so the correction is

$$
-\frac{(\boldsymbol\sigma\cdot\vec\pi)^4}{8m^3c^2}.
$$

It is $(\boldsymbol\sigma\cdot\vec\pi)^4$, not $\vec\pi^4$, because $(\boldsymbol\sigma\cdot\vec\pi)^2=\vec\pi^2-ϙ\hbar\boldsymbol\sigma\cdot\vec B$; the difference is of the same $c^{-2}$ order and is not dropped.

*Step 5: the second generator and the assembled Hamiltonian.* The odd remainder is $O_1$, and the transformation that removes it is $S_2=-\frac{i}{2mc^2}c_0O_1$. With $O_1$ from Problem 1 and $c_0L_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}=-i\alpha_k$,

$$
c_0O_1=\frac{i\hbarϙ}{2mc}\sum_k\alpha_kE_k,
\qquad
S_2=-\frac{i}{2mc^2}c_0O_1=\frac{\hbarϙ}{4m^2c^3}\sum_k\alpha_kE_k .
$$

The transformation cancels $O_1$; its even terms are of higher order and are dropped. Collecting the leading and next-to-leading orders, the large-component Hamiltonian is

$$
\boxed{\;
H=\frac{\vec\pi^2}{2m}+ϙ\Phi-\frac{ϙ\hbar}{2m}\boldsymbol\sigma\cdot\vec B
-\frac{(\boldsymbol\sigma\cdot\vec\pi)^4}{8m^3c^2}
+\frac{\hbar^2}{8m^2c^2}\nabla^2V
-\frac{ϙ\hbar}{4m^2c^2}\boldsymbol\sigma\cdot(\vec E\times\vec\pi)
\;}
$$

to relative order $c^{-2}$. The first three terms are the Pauli Hamiltonian of Problem 1; the last three are the corrections that the parent article does not reach.

*Step 6: numerical verification against the exact Dirac spectrum.* The three corrections are fixed by their coefficients; a single overall check is therefore decisive. In a hydrogenic atom with nuclear charge $\mathfrak{Z}$, the first-order shifts of the three corrections are, in natural units ($c=1$), the standard ones,

$$
\Delta E_{\rm kin}=-\frac{m(\mathfrak{Z}\alpha)^4}{2n^3}\!\left[\frac{1}{\ell+\tfrac12}-\frac{3}{4n}\right],\qquad
\Delta E_{\rm SO}=\frac{m(\mathfrak{Z}\alpha)^4}{2n^3}\frac{s_{\mathrm{tot}}(s_{\mathrm{tot}}+1)-\ell(\ell+1)-\tfrac34}{2\ell(\ell+\tfrac12)(\ell+1)}\quad(\ell\neq0),
$$

$$
\Delta E_{\rm D}=\frac{m(\mathfrak{Z}\alpha)^4}{2n^3}\quad(\ell=0),\qquad \Delta E_{\rm D}=0\quad(\ell\neq0),
$$

with the exact Dirac shift $\Delta E_{\rm exact}=-\dfrac{m(\mathfrak{Z}\alpha)^4}{2n^3}\Bigl[\dfrac{1}{s_{\mathrm{tot}}+\tfrac12}-\dfrac{3}{4n}\Bigr]$. Evaluating all of these with exact rational arithmetic for every level with $n\le6$ (36 levels, with the allowed $s_{\mathrm{tot}}=\ell\pm\tfrac12$, one value at $\ell=0$), the sum $\Delta E_{\rm kin}+\Delta E_{\rm SO}+\Delta E_{\rm D}$ equals $\Delta E_{\rm exact}$ in every case, with difference exactly $0$. The coefficients are also those of the two sources named at the head of this problem: the binomial coefficients $1,\tfrac12,-\tfrac18$ of $\sqrt{m^2c^4+O^2}$ and the Darwin coefficient $+\tfrac18$ of the second-order term.

## Problem 4: Hermiticity and the $\mathbb M_\pm$ decomposition

**Statement.** Check the Hermiticity of every term and determine which terms lie in $\mathbb M_+$.

**Solution.**

*Step 1: Hermiticity.* Each term of the Hamiltonian of Problem 3 is Hermitian:

- $\vec\pi^2/2m$: $\pi_i^\dagger=\pi_i$, hence $\sum_i\pi_i^2$ is Hermitian;
- $ϙ\Phi$: multiplication by the real function $ϙ\Phi$, Hermitian;
- $-\dfrac{ϙ\hbar}{2m}\boldsymbol\sigma\cdot\vec B$: $\sigma_k$ and the real field $B_k$ are Hermitian;
- $-\dfrac{(\boldsymbol\sigma\cdot\vec\pi)^4}{8m^3c^2}$: minus a real multiple of the square of the Hermitian $(\boldsymbol\sigma\cdot\vec\pi)^2$;
- $\dfrac{\hbar^2}{8m^2c^2}\nabla^2V$: multiplication by a real function;
- $-\dfrac{ϙ\hbar}{4m^2c^2}\boldsymbol\sigma\cdot(\vec E\times\vec\pi)$: this is the one term whose Hermiticity is not automatic. Using $[\pi_i,E_j]=-i\hbar\partial/\partial Q_i\,E_j$,

$$
(\vec E\times\vec\pi)_i^\dagger=(\vec E\times\vec\pi)_i+i\hbar(\nabla\times\vec E)_i ,
$$

so the term is Hermitian if and only if $\nabla\times\vec E=0$, its failure of Hermiticity being proportional to the curl. Since $\vec E=-\nabla\Phi$ for an electrostatic field, $\nabla\times\vec E=-\nabla\times\nabla\Phi=0$ identically, and the term is Hermitian. Writing it instead as $\boldsymbol\sigma\cdot(\nabla V\times\vec\pi)$ makes this manifest, because $\nabla V$ is a gradient. For a general time-dependent field, where $\vec E$ has a solenoidal part $-\partial/\partial t'\,\vec A$ and $\nabla\times\vec E=-\partial/\partial t'\,\vec B$, the antisymmetric part does not vanish and the non-relativistic reduction requires the symmetrized ordering; this is the only place in the reduction where the result is convention- and ordering-sensitive beyond the metric conventions already noted.

*Step 2: the $\mathbb M_+$ representatives.* Under the isomorphism, a Hermitian $2\times2$ matrix $h_tI_2+\vec h\cdot\boldsymbol\sigma$ corresponds to the Hermitian biquaternion $h_te_t+i\vec h\in\mathbb M_+$. Applying it term by term, with $\vec B=\sum_k B_k\vec e_k$ and $(\vec E\times\vec\pi)=(\vec E\times\vec\pi)_k\vec e_k$,

| Term of $H$ | Biquaternion representative | Sector |
|---|---|---|
| $\vec\pi^2/2m$ | $(\vec\pi^2/2m)\,e_t$ | $\mathbb M_+$ |
| $ϙ\Phi$ | $(ϙ\Phi)\,e_t$ | $\mathbb M_+$ |
| $-\dfrac{ϙ\hbar}{2m}\boldsymbol\sigma\cdot\vec B$ | $-\dfrac{ϙ\hbar}{2m}\,i\vec B$ | $\mathbb M_+$ |
| $-\dfrac{(\boldsymbol\sigma\cdot\vec\pi)^4}{8m^3c^2}$ | $-\dfrac{1}{8m^3c^2}\bigl(\vec\pi^2-\hbarϙ\,i\vec B\bigr)^2$ | $\mathbb M_+$ |
| $\dfrac{\hbar^2}{8m^2c^2}\nabla^2V$ | $\dfrac{\hbar^2}{8m^2c^2}(\nabla^2V)\,e_t$ | $\mathbb M_+$ |
| $-\dfrac{ϙ\hbar}{4m^2c^2}\boldsymbol\sigma\cdot(\vec E\times\vec\pi)$ | $-\dfrac{ϙ\hbar}{4m^2c^2}\,i(\vec E\times\vec\pi)$ | $\mathbb M_+$ |

Every term of the reduced, two-component Hamiltonian is Hermitian, hence every term lands in $\mathbb M_+$. This is the precise content of the parent's remark that the spin term is an observable of the informational sector; the remark applies term by term.

*Step 3: what does not land in $\mathbb M_+$.* Three classes of object in the reduction do not.

1. **The Clifford-odd operators.** The mass term $c_0mc^2$ contains the cell $c_0=iR_{\vec e_x}^{\mathrm{pau}}$, and the generator $S_1=-\frac{i}{2mc^2}c_0O$ contains $c_0O$. Their coefficient matrices are odd elements of the Clifford algebra, whereas $\mathbb B\cong\mathrm{Cl}^+_{1,3}$ is the *even* subalgebra and a left multiplication by a biquaternion has an even coefficient matrix. They therefore have no representative in $\mathbb B$ at all, and a fortiori none in either $\mathbb M_\pm$. This is why the four-component Hamiltonian is not an element of $\mathbb B$ and why a transformation is needed before the biquaternion identification can be made: the Foldy–Wouthuysen transformation is exactly the operation that removes the Clifford-odd part and leaves an element of $\mathbb M_+$.

2. **The anti-Hermitian generator.** $S_1$ is Hermitian, so $iS_1$ is anti-Hermitian: it plays the rôle that the elements of $\mathbb M_-$ play in the companion quantum article, where the Lie algebra of the $*$-unitary group is $\mathbb M_-$. It is not itself in $\mathbb M_-$, because it is built from the Clifford-odd element $c_0O$. The two gradings must not be conflated: the Foldy–Wouthuysen grading is by conjugation with $c_0$, the $\mathbb M_\pm$ grading is by ${}^{*}$. Thus the odd operator $O=c\sum_k\alpha_k\pi_k$ is Foldy–Wouthuysen-odd but Clifford-even and Hermitian, so as a biquaternion it lies in $\mathbb M_+$; while $c_0O$ is Foldy–Wouthuysen-odd, Clifford-odd and anti-Hermitian, and lies in neither $\mathbb B$ nor $\mathbb M_\pm$. The identification of "odd" with "not in $\mathbb M_+$" is incorrect.

3. **The real structure and the mass term.** In the biquaternion equation the conjugation $\flat=-{}^{*}$ is the algebra's real structure. It maps $\mathbb M_+$ to $\mathbb M_-$ and fixes $\mathbb M_-$: if $\tilde\Psi\in\mathbb M_+$ then $\tilde\Psi^\flat=-\tilde\Psi\in\mathbb M_-$, and if $\tilde\Psi\in\mathbb M_-$ then $\tilde\Psi^\flat=\tilde\Psi$. Its action is diagonal on the sector decomposition with opposite signs $\mp1$: a coupling built on $\flat$ — a Majorana-type mass, $m\tilde\Psi^\flat$ — would carry those opposite signs. The parent's mass term is not that coupling; it is the linear, chirality-off-diagonal pair $\tilde\nabla\tilde\Psi_R=m\tilde\Psi_L$, $\tilde\nabla^{\natural}\tilde\Psi_L=m\tilde\Psi_R$, which couples the two central ideals (the chiralities) and leaves each element's sector membership untouched. The operation that exchanges the two sectors is multiplication by the central $i$. The rest-energy phase that is factored out before the reduction,

$$
\exp(-imc^2t'/\hbar)=\cos\!\Bigl(\frac{mc^2t'}{\hbar}\Bigr)e_t-\sin\!\Bigl(\frac{mc^2t'}{\hbar}\Bigr)(ie_t),
$$

is not Hermitian: its first term lies in $\mathbb M_+$ and its second in $\mathbb M_-$, since $ie_t$ is anti-Hermitian. It is a phase, not an observable, and must be factored out before a two-component (hence $\mathbb M_+$) description of the dynamics is reached.

## Problem 5: The physical dimensions of each term

**Statement.** Determine the physical dimensions of each term.

**Solution.** Every term is an energy, since each is a term of a Hamiltonian. The individual coefficients nevertheless carry different powers of $\hbar$ and $c$, and checking them is a useful consistency test. In SI units, with $[\hbar]=\mathrm{kg\,m^2\,s^{-1}}$, $[c]=\mathrm{m\,s^{-1}}$, $[ϙ]=\mathrm C$, $[\Phi]=\mathrm V=\mathrm{kg\,m^2\,s^{-3}A^{-1}}$, $[\vec B]=\mathrm T=\mathrm{kg\,s^{-2}A^{-1}}$ and $[\vec E]=\mathrm{V\,m^{-1}}=\mathrm{kg\,m\,s^{-3}A^{-1}}$:

| Term | Coefficient units | Field/operator units | Product |
|---|---|---|---|
| $\vec\pi^2/2m$ | $1/m$ | $(\mathrm{kg\,m\,s^{-1}})^2$ | $\mathrm{kg\,m^2\,s^{-2}}$ |
| $ϙ\Phi$ | $\mathrm C$ | $\mathrm{kg\,m^2\,s^{-3}A^{-1}}$ | $\mathrm{kg\,m^2\,s^{-2}}$ |
| $-\dfrac{ϙ\hbar}{2m}\boldsymbol\sigma\cdot\vec B$ | $\mathrm C\,\mathrm{kg\,m^2\,s^{-1}\,kg^{-1}}$ | $\mathrm{kg\,s^{-2}A^{-1}}$ | $\mathrm{kg\,m^2\,s^{-2}}$ |
| $-\dfrac{ϙ\hbar^2}{8m^2c^2}\nabla\cdot\vec E$ | $\mathrm C\,\mathrm{kg^2m^4s^{-2}}\,\mathrm{kg^{-2}m^{-2}s^{2}}$ | $\mathrm{kg\,s^{-3}A^{-1}}$ | $\mathrm{kg\,m^2\,s^{-2}}$ |
| $-\dfrac{ϙ\hbar}{4m^2c^2}\boldsymbol\sigma\cdot(\vec E\times\vec\pi)$ | $\mathrm C\,\mathrm{kg\,m^2s^{-1}}\,\mathrm{kg^{-2}m^{-2}s^{2}}$ | $\mathrm{kg^2m^2s^{-4}A^{-1}}$ | $\mathrm{kg\,m^2\,s^{-2}}$ |
| $-\dfrac{(\boldsymbol\sigma\cdot\vec\pi)^4}{8m^3c^2}$ | $\mathrm{kg^{-3}m^{-2}s^{2}}$ | $\mathrm{kg^4m^4s^{-4}}$ | $\mathrm{kg\,m^2\,s^{-2}}$ |

The pattern is informative. The leading terms ($\vec\pi^2/2m$, $ϙ\Phi$, the spin term) carry no power of $c$; the three corrections each carry $c^{-2}$, which is the statement that they are relativistic corrections of order $v^2/c^2$. The spin term carries one power of $\hbar$ in its coefficient, while the leading kinetic and electrostatic terms carry none. Written with $\vec S=\tfrac\hbar2\boldsymbol\sigma$, it is $-(ϙ/m)\vec S\cdot\vec B$, the classical coupling of a magnetic moment; the power of $\hbar$ is the conversion between the dimensionless $\boldsymbol\sigma$ and the spin. The Darwin term carries $\hbar^2$ and has no classical counterpart. The spin–orbit term carries one power of $\hbar$ in its coefficient, but it is quadratic in the angular momenta once $\vec S$ and $\vec L=\vec r\times\vec p$ are used, so it becomes the classical Thomas-precession coupling when $\vec S$ and $\vec L$ are classical.

## The Gamma Formulation

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb C)=M_4(\mathbb C)$, not a different algebra. This is the only section of the article that names them.

Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\psi=a\psi$ and $R_b\psi=\psi b$.

$$
\gamma_0=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\quad \gamma_1=iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_2=iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_3=iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_5=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}} .
$$

A single product $L_aR_b$ is a pure tensor; the pure products form the seven-dimensional cone of coefficient matrices of rank at most one, and a general element of the cell algebra is a sum of at most four of them.

$\gamma_5$ is the reference-frame cell of the chirality, the cell $-iR_{\vec e_z}^{\mathrm{pau}}$; the central grading $\chi=i\tilde\Xi_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi^2=e_t$ — is a different object, represented by $\gamma_5$ on the Dirac module.

The dictionary is complex-linear; over $\mathbb R$ the products $L_aR_b$ span $\mathrm{Cl}_{3,1}(\mathbb R)\cong M_4(\mathbb R)$, and the four coordinate cells span $\mathrm{Cl}_{1,3}(\mathbb R)\cong M_2(\mathbb H)$.

**The identities of the frame.** In the $\gamma$ reading, with $\epsilon_{0123}=+1$,

$$
\{\gamma_\mu,\gamma_\nu\}=2g_{\mu\nu}I_4,\qquad
(\gamma_k)^2=-I_4,\qquad
\gamma_5^2=I_4,\qquad
\{\gamma_\mu,\gamma_5\}=0,
$$

$$
[\gamma_\mu,\gamma_\nu]=2\gamma_\mu\gamma_\nu\quad(\mu\ne\nu),\qquad
[\gamma_a,S_{cd}]=g_{ac}\gamma_d-g_{ad}\gamma_c,\qquad
S_{cd}=\tfrac14[\gamma_c,\gamma_d],
$$

$$
\mathrm{tr}(\gamma_\mu\gamma_\nu)=4g_{\mu\nu},\qquad
\mathrm{tr}(\gamma_5\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)=-4i\,\epsilon_{\mu\nu\rho\sigma},
$$

$$
\mathrm{tr}(\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)
=4\bigl(g_{\mu\nu}g_{\rho\sigma}-g_{\mu\rho}g_{\nu\sigma}+g_{\mu\sigma}g_{\nu\rho}\bigr).
$$

The four contraction sums are frame statements, because they follow from the cell squares alone. In the Euclidean frame, where every cell squares to $+I_4$, they are

$$
\sum_\mu\gamma_\mu\gamma_\mu=4I_4,\qquad
\sum_\mu\gamma_\mu\gamma_\alpha\gamma_\mu=-2\gamma_\alpha,
$$

$$
\sum_\mu\gamma_\mu\gamma_\alpha\gamma_\beta\gamma_\mu=4\delta_{\alpha\beta}I_4,\qquad
\sum_\mu\gamma_\mu\gamma_\alpha\gamma_\beta\gamma_\gamma\gamma_\mu=-2\gamma_\gamma\gamma_\beta\gamma_\alpha .
$$

In the mostly-minus frame of this article the metric signs enter and only the two-index sum stays a multiple of the identity, $\sum_\mu\gamma_\mu\gamma_\mu=-2I_4$; the three higher sums are not rescaled versions of the Euclidean ones, which is why they are stated in the frame where the squares are all $+1$.

With $\nu(t)=x$ and $\nu(k)=y$, the coordinate cell of $x_\mu$ is $iL_{e_\mu}^{\mathrm{pau}}R_{\vec e_{\nu(\mu)}}^{\mathrm{pau}}$; these are the cells $c_0=iR_{\vec e_x}^{\mathrm{pau}}$ and $c_k=iL_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}$ used throughout the body, and the gamma frame above is exactly this set, renamed.

## Summary

The non-relativistic limit of the biquaternion Dirac equation was carried through in five steps, for the one-sided chiral pair read on the Dirac module. The two-sided form of the parent is a different operator, antilinear in its mass term, and is not reduced here.

The Foldy–Wouthuysen elimination of the small component, executed systematically with the generator $S_1=-\frac{i}{2mc^2}c_0O=\frac{1}{2mc}\sum_k L_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}\pi_k$, produces the Pauli Hamiltonian
$i\hbar\partial/\partial t'\,\phi=\big[\vec\pi^2/2m+ϙ\Phi-(ϙ\hbar/2m)\boldsymbol\sigma\cdot\vec B\big]\phi$,
reproducing the parent article. The minimal substitution $\vec\pi=p-ϙ\vec A$ gives $[\pi_i,\pi_j]=i\hbar ϙ\epsilon_{ijk}B_k$ and $(\boldsymbol\sigma\cdot\vec\pi)^2=\vec\pi^2-ϙ\hbar\boldsymbol\sigma\cdot\vec B$, and the coefficient $1/2m$ produced by the elimination fixes $g=2$ and $\vec\mu=(ϙ/m)\vec S$, hence $\mu_B=e\hbar/2m_e$ for the electron. At the next order in $1/c$, the second-order term $-\tfrac12[S_1,[S_1,E]]$ of the first transformation gives the Darwin term $+\hbar^2\nabla^2V/(8m^2c^2)=-(ϙ\hbar^2/8m^2c^2)\nabla\cdot\vec E$ and the spin–orbit coupling $-(ϙ\hbar/4m^2c^2)\boldsymbol\sigma\cdot(\vec E\times\vec\pi)=(\hbar/4m^2c^2)r^{-1}(dV/dr)\boldsymbol\sigma\cdot\vec L$, while the expansion of the free large-block energy gives the relativistic kinetic correction $-(\boldsymbol\sigma\cdot\vec\pi)^4/(8m^3c^2)$. The second transformation removes the residual odd term $O_1$ and adds no even term at this order. Summed, these reproduce the exact Dirac fine structure of hydrogenic ions for 36 levels with $n\le6$, with difference exactly zero.

Every term of the reduced Hamiltonian is Hermitian and therefore lies in $\mathbb M_+$; the objects that do not are the Clifford-odd pieces ($c_0mc^2$, $c_0O$), which have no representative in $\mathbb B$ at all, the anti-Hermitian generator $iS_1$, and the real structure $\flat$ — whose opposite-sign action on the sectors a Majorana-type coupling would carry — together with the sector-exchanging rest-energy phase; the parent's mass term is the linear coupling between the two chiralities. The Foldy–Wouthuysen grading by $c_0$ must not be confused with the $\mathbb M_\pm$ grading by ${}^{*}$. All terms are energies, the three corrections carrying the expected $c^{-2}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb B=\mathbb C\otimes_\mathbb R\mathbb H$ | Biquaternion algebra |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$, $\vec e_k^2=-e_t$ | Quaternion basis |
| $\mathbb M_+,\mathbb M_-$ | Hermitian / anti-Hermitian subspaces |
| $\mathsf{M}_2(\vec e_k)=-i\sigma_k$, $\sigma_k\leftrightarrow i\vec e_k$ | Isomorphism, Pauli matrices |
| $L_a\psi=a\psi$, $R_b\psi=\psi b$, $L_aR_bL_cR_d=L_{ac}R_{db}$ | Left, right and two-sided multiplication |
| $c_0=iR_{\vec e_x}^{\mathrm{pau}}$, $c_k=iL_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}$ | Coordinate cells; $c_0^2=1$, $c_k^2=-1$, $\{c_0,c_k\}=0$ |
| $\alpha_k=c_0c_k=L_{\vec e_k}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}$ | Velocity cell, after one use of $i^2=-1$ |
| $S_k=iL_{\vec e_k}^{\mathrm{pau}}$ | Spin cell; upper block $\sigma_k$, lower block $-\sigma_k$ |
| $g=\operatorname{diag}(+1,-1,-1,-1)$ | Clifford metric; $g=-\eta$ |
| $\vec\pi=p-ϙ\vec A$ | Kinetic momentum |
| $\vec B=\nabla\times\vec A$, $\vec E$ | Magnetic, electric fields |
| $V=ϙ\Phi$ | Potential energy |
| $H=c_0mc^2+O+E$, $O=c\sum_k\alpha_k\pi_k$ | Split Hamiltonian; odd part |
| $S_1=-\frac{i}{2mc^2}c_0O=\frac{1}{2mc}\sum_k L_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}\pi_k$ | Foldy–Wouthuysen generator |
| $O_1=i[S_1,E]=-\frac{\hbarϙ}{2mc}\sum_k L_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}E_k$ | Residual odd operator |
| $S_2=-\frac{i}{2mc^2}c_0O_1=\frac{\hbarϙ}{4m^2c^3}\sum_k\alpha_kE_k$ | Second generator |
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
- [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html), for the two forms and the mass.
- [The Dirac Equation in Biquaternionic Form — Solutions and the Non-Relativistic Limit](the-dirac-equation-in-biquaternionic-form-solutions-and-the-non-relativistic-limit.html), the parent of this exercise.
- [The Foldy–Wouthuysen Transformation in Biquaternionic Form](the-foldy-wouthuysen-transformation-in-biquaternionic-form.html), for the transformation in the algebra.
- [Quantum Physics in Biquaternionic Form](quantum-physics-in-biquaternionic-form.html), for the sector structure.
- [Operator and Calculus Conventions](operator-and-calculus-conventions.html), for the cell calculus.
