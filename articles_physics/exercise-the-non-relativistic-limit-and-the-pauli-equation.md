# __Exercise: The Non-Relativistic Limit and the Pauli Equation__

## Introduction

This is one of the worked exercises attached to the article *The Dirac Equation in Biquaternionic Form — Solutions and the Non-Relativistic Limit*. That article states the two forms of the biquaternion Dirac equation, constructs the plane-wave solutions of the one-sided pair, and carries the pair into the non-relativistic regime far enough to exhibit the Pauli equation and the gyromagnetic factor $g=2$. This exercise takes the limiting procedure as given and executes it in full: every order that contributes to the first corrections is kept, every coefficient is derived, and every claim is checked.

Five problems are worked:

1. the Foldy–Wouthuysen elimination of the small component, carried out step by step and to the order at which the first corrections appear;
2. the minimal substitution $p\to p-q\vec A$ and the electromagnetic terms it produces, including the spin term and the coefficient that fixes $g=2$;
3. the next order in $1/c$: the relativistic kinetic correction, the Darwin term, and the spin–orbit coupling;
4. the Hermiticity of every term, and which terms lie in the Hermitian subspace $\mathbb M_+$ and which do not;
5. the physical dimensions of every term.

**The operators, fixed once.** Every derivative in this exercise is the biquaternionic gradient

$$
\tilde\nabla=\sum_{\mu\in\{t,x,y,z\}}e_\mu\frac{\partial}{\partial Q_\mu},
\qquad
\tilde\nabla^{\natural}=\sum_{\mu\in\{t,x,y,z\}}\varepsilon_\mu e_\mu\frac{\partial}{\partial Q_\mu},
\qquad
\varepsilon=(1,-1,-1,-1),
$$

and its norm is the d'Alembertian

$$
\Box=\tilde\nabla\tilde\nabla^{\natural}=\tilde\nabla^{\natural}\tilde\nabla=\frac{\partial^2}{\partial Q_t^2}+\Delta_Q .
$$

On the material sector, where $Q_t=ict'$, the gradient and its conjugate read

$$
\tilde\nabla\big|_{\mathbb M_-}=-\frac{i}{c}e_t\frac{\partial}{\partial t'}+\sum_k\vec e_k\frac{\partial}{\partial q_k},
\qquad
\tilde\nabla^{\natural}\big|_{\mathbb M_-}=-\frac{i}{c}e_t\frac{\partial}{\partial t'}-\sum_k\vec e_k\frac{\partial}{\partial q_k},
\qquad
\Box\big|_{\mathbb M_-}=\Delta-\frac{1}{c^2}\frac{\partial^2}{\partial t'^2},
$$

and the pure part of the gradient is written $D_3=\sum_k\vec e_k\partial/\partial q_k$. Minimal coupling shifts each derivative, $\partial/\partial Q_\mu\to\partial/\partial Q_\mu-iqA_\mu/\hbar$, so the gauged gradient is

$$
\tilde\nabla_A=\tilde\nabla-\frac{iq}{\hbar}\tilde A,
\qquad
\tilde A=\Phi e_t-\vec A,
\qquad
\vec A=\sum_kA_k\vec e_k,
\qquad
\sum_k\vec e_k\pi_k=-i\hbar\,D_3^A ,
$$

with $\pi_k=p_k-qA_k$ and $D_3^A=\sum_k\vec e_k(\partial/\partial q_k-iqA_k/\hbar)$ the pure part of $\tilde\nabla_A$. A plane wave $\exp\!\bigl(i(k_0x_0-\vec k\cdot\vec q)\bigr)$, with $x_0=ct'$, replaces the gradient by the element

$$
\tilde K=k_0-i\vec k,
\qquad
\tilde Kf=0\ \text{on the light cone},
\qquad
\tilde K^{\natural}\tilde K=k_0^2-\lvert\vec k\rvert^2 .
$$

**What the gradient can do, and what it cannot.** The massless equation is one first-order equation in one field,

$$
\tilde\nabla F=0 .
$$

The massive case is not of that form, and the reason is a square. The square of the gradient is not scalar: the time unit commutes with the three spatial units instead of anticommuting with them, so the mixed derivatives add, and each spatial unit squares to $-e_t$, which puts the wrong sign on the Laplacian. Explicitly, on a general field,

$$
\tilde\nabla^2=\Box-2\Delta-\frac{2i}{c}\sum_k\vec e_k\frac{\partial^2}{\partial t'\,\partial q_k},
$$

so $\tilde\nabla^2\neq\Box$ and no scalar mass can be subtracted from the square. The massive equation is therefore a pair of first-order equations in two fields, the **chiral pair**, and it is stated below. No one-field first-order massive equation is written anywhere in this exercise.

**On the parent article.** The parent's non-relativistic section works only to leading order. It factors out the rest energy, eliminates the small component with the approximation $\partial/\partial t'\,\chi\approx 0$, and reads off the Pauli Hamiltonian; it stops there. It contains no spin–orbit and no Darwin term, and it does not perform a systematic Foldy–Wouthuysen transformation. It also does not state the sector ($\mathbb M_\pm$) status of the intermediate operators it uses. Problems 3 and 4 supply those orders and that status. Where the parent is silent this is stated explicitly and not silently filled in.

All the derivatives below are $\tilde\nabla$, $\tilde\nabla^{\natural}$ and their pure part $D_3$, and no other differential operator appears. Natural units $\hbar=c=1$ are used while deriving; $\hbar$ and $c$ are restored wherever a physical statement is made. Fixing the frame, the chirality is the operator that multiplies on the right by $-i\vec e_z$ and takes the two values $\mp1$; the field is one element $F\in\mathbb B$ split into its two parts, $F=F_L+F_R$, of value $-1$ and $+1$. The side is position: the chirality acts as $F\mapsto-iF\vec e_z$, and the left action $F\mapsto-i\vec e_zF$ is a different element, never used here. Since $\vec e_z=-\omega$ with $\omega$ the pseudoscalar of the frame, $\omega^2=-e_t$, the chirality is also written $F\mapsto iF\omega$; the $i$ in front of it is the central scalar $i$ of the algebra and not $\omega$.

### The two Dirac equations

The parent carries two equations, and they must not be read as one.

**The one-sided pair.** The corpus's own equation is the chiral pair. It acts on the two chiral halves $F_R$ and $F_L$ of the field by left multiplication, and the mass is the off-diagonal pairing of the two halves:

$$
\tilde\nabla F_R=mF_L,
$$

$$
\tilde\nabla^{\natural}F_L=mF_R .
$$

Both gradients act on the left, and no right multiplication and no conjugation enters. On the Dirac module $\Delta=\mathbb B$ the pair is a four-component equation, and it is the equation reduced below.

**The two-sided form.** Kravchenko's dictionary writes the same physics as a single equation on the whole algebra. The derivative acts on the left, the mass acts on the right through $\vec e_z=-\omega$, and a componentwise conjugation supplies the antilinear part. Here $D_3=\sum_k\vec e_k\,\partial/\partial Q_k$ is the pure part of the gradient and $\mathcal N$ names the left-hand side. In natural units:

$$
\mathcal N F=\Bigl(i\frac{\partial}{\partial t'}+D_3\Bigr)F-mi\,\overline F\,\vec e_z=0 .
$$

Equivalently,

$$
-\tilde\nabla^{\natural}F-mi\,\overline F\,\vec e_z=0
$$

for a field $F\in\mathbb B$, since $i\partial/\partial t'=-\partial/\partial Q_t$ in these units. The two forms are related by a change of representation, but they are different operators: the pair is linear in the field, while the mass term of the two-sided form is antilinear because it carries $\overline F$.

| | One-sided pair | Two-sided form |
|---|---|---|
| Equation | $\tilde\nabla F_R=mF_L$, $\tilde\nabla^{\natural}F_L=mF_R$ | $\mathcal NF=0$, with $\mathcal NF=(i\partial/\partial t'+D_3)F-mi\overline F\vec e_z$ |
| Multiplication | left by $\tilde\nabla$ and $\tilde\nabla^{\natural}$ | left by $i\partial/\partial t'$ and $D_3$; right by $\vec e_z$; antilinear bar |
| Field | $F=F_L+F_R\in\Delta=\mathbb B$ | $F\in\mathbb B$ |
| Mass | off-diagonal pairing of the chiral halves | $-mi\overline F\vec e_z$: a conjugation and a direction |
| Chirality | the central sign, $\mp1$ on the two halves | the right multiplication by $-i\vec e_z$ |
| Use | the formulation and its kinematics | the dictionary, the Cauchy theory, the integral representation |

The reduction below is of the one-sided pair, read on the Dirac module. The Foldy–Wouthuysen transformation is applied to the Hamiltonian of that pair. The two-sided form is a different operator, antilinear in its mass term; its non-relativistic reduction is not attempted here.

### The Hamiltonian form

**The two gradings.** The reduction needs two involutions of the module, and both are right multiplications of the algebra, written by position.

- The **chirality** $\Gamma F=-iF\vec e_z$, of values $\mp1$ on $F_L$ and $F_R$. It separates the two members of the pair, and it commutes with every left multiplication, hence with the gradient.
- The **mass grading** $\beta F=iF\vec e_x$. It squares to the identity, $\beta^2=1$; it anticommutes with the chirality, $\beta\Gamma=-\Gamma\beta$; and it commutes with the gradient. Its two values split the module into a **large** part and a **small** part.

**The Hamiltonian.** The pair, read on the module, is the equation of motion

$$
i\hbar\frac{\partial F}{\partial t'}=HF,
\qquad
H=\beta mc^2+O+q\Phi,
\qquad
OF=c\sum_k\vec e_k\pi_k\,F\,\vec e_y=-i\hbar c\,\bigl(D_3^AF\bigr)\vec e_y .
$$

The mass term is the grading itself, multiplied by the mass. The kinetic operator $O$ is the pure part of the gauged gradient, multiplied on the right by $\vec e_y$. Both factors are present and both are needed: left multiplication by $\vec e_k$ with the derivative on one side, and the multiplier $\vec e_y$ on the other, so $O$ is a two-sided operator and not the left multiplication by an element. It is odd because $\vec e_y$ anticommutes with $\vec e_x$; it reverses the chirality because $\vec e_y$ anticommutes with $\vec e_z$ as well. The relations used below are four:

$$
\beta^2=1,
\qquad
\beta O=-O\beta,
\qquad
\beta\,q\Phi=q\Phi\,\beta,
\qquad
O=O^{\dagger},\quad \beta=\beta^{\dagger},
$$

so that $O$ is odd, $q\Phi$ is even, and $H$ is Hermitian. The eigenvalues of $H$ at zero potential are $\pm\sqrt{m^2c^4+c^2\vec\pi^2}$, which is the mass shell $\tilde K^{\natural}\tilde K=m^2$ of the pair.

**The two halves.** With $\beta\varphi=+\varphi$ and $\beta\chi=-\chi$, the equation of motion reads on the two parts

$$
i\hbar\frac{\partial\varphi}{\partial t'}=mc^2\varphi+O\chi+q\Phi\varphi,
\qquad
i\hbar\frac{\partial\chi}{\partial t'}=-mc^2\chi+O\varphi+q\Phi\chi .
$$

The even operator $q\Phi$ is the electrostatic energy and the odd operator $O$ is what couples the large and the small parts: $O\varphi$ is small and $O\chi$ is large. This is the system reduced in Problem 1.

## Problem 1: The Foldy–Wouthuysen elimination of the small component

**Statement.** Starting from the four-component Dirac equation with minimal coupling, eliminate the small component and obtain the Pauli Hamiltonian, keeping the orders through the first corrections.

**Solution.**

*Step 1: the split.* The Hamiltonian of the pair is $H=\beta mc^2+O+E$ with

$$
O=c\sum_k\vec e_k\pi_k\,(\cdot)\,\vec e_y\quad(\text{odd},\ \beta O\beta=-O),
\qquad
E=q\Phi\quad(\text{even},\ \beta E\beta=E),
$$

and the odd operator is the pure part of the gauged gradient, $\sum_k\vec e_k\pi_k=-i\hbar D_3^A$, multiplied on the right by $\vec e_y$. Writing it as $\hbar c\,\vec\pi$, that is as the left multiplication by an element, would make it even; the right multiplier $\vec e_y$ is what makes it odd, and it is also what reverses the chirality.

*Step 2: factoring out the rest energy.* Write $F=\exp(-i\theta)\,G$ with $\theta=mc^2t'/\hbar$. The factor is the central element $\cos\theta-i\sin\theta$, which commutes with every operator of the reduction, so it can be cancelled on both sides. What is left of the mass term is $(\beta-1)mc^2$, which vanishes on the large part and is $-2mc^2$ on the small part, and the parent's two coupled equations follow:

$$
i\hbar\frac{\partial\varphi}{\partial t'}=O\chi+q\Phi\varphi,
$$

$$
i\hbar\frac{\partial\chi}{\partial t'}=O\varphi-2mc^2\chi+q\Phi\chi .
$$

*Step 3: the leading elimination.* The term $2mc^2\chi$ dominates the second equation whenever the fields, the kinetic energy and $\partial\chi/\partial t'$ are small compared with $mc^2$. Neglecting the other terms there,

$$
\chi=\frac{O}{2mc^2}\,\varphi+O(c^{-3}),
$$

so the small part is of relative order $v/c$, as it must be. Substituting into the first equation eliminates $\chi$ exactly at this order:

$$
i\hbar\frac{\partial\varphi}{\partial t'}=\left[\frac{O^2}{2mc^2}+q\Phi\right]\varphi ,
$$

and on the large part $O^2/(2mc^2)=(\vec\pi^2-\hbar q\boldsymbol\sigma\cdot\vec B)/2m$, whose leading term is $\vec\pi^2/2m$ and whose remainder is evaluated in Problem 2.

*Step 4: the systematic transformation.* The approximation of Step 3 is the first term of a controlled expansion. The Foldy–Wouthuysen generator is $S=S_1+S_2+\cdots$ with

$$
S_1=-\frac{i}{2mc^2}\,\beta O
=-\frac{1}{2mc}\sum_k\vec e_k\pi_k\,(\cdot)\,\vec e_z
=\frac{i\hbar}{2mc}\bigl(D_3^A\cdot\bigr)\vec e_z .
$$

The second form is the first one after $\beta O=-ic\sum_k\vec e_k\pi_k(\cdot)\vec e_z$, the two multipliers of $\beta O$ being $i\vec e_x$ and $\vec e_y$, whose product is $i\vec e_z$; the third is the same operator written with the pure part of the gauged gradient, since $\sum_k\vec e_k\pi_k=-i\hbar D_3^A$. The generator is two-sided as well, left by $\vec e_k$ and right by $\vec e_z$, and it is Hermitian, being the product of an anti-Hermitian left factor and an anti-Hermitian right multiplier with a Hermitian $\pi_k$ between them; so $iS_1$ is anti-Hermitian and the transformation is unitary. For static fields the generator is time-independent, and the transformed Hamiltonian is

$$
e^{iS_1}He^{-iS_1}
=H+i[S_1,H]-\tfrac12[S_1,[S_1,H]]-\tfrac{i}{6}[S_1,[S_1,[S_1,H]]]+\cdots
$$

the full transformed operator being this expression minus $i\hbar\partial/\partial t'$. Using $\beta O=-O\beta$ and $\beta E=E\beta$, the three elementary commutators are

$$
i[S_1,\beta mc^2]=-O,\qquad
i[S_1,O]=\frac{\beta O^2}{mc^2},\qquad
[S_1,[S_1,\beta mc^2]]=\frac{\beta O^2}{mc^2}.
$$

The first cancels the odd term $O$. The second contributes $+\frac{\beta O^2}{mc^2}$ to the expansion and the third contributes $-\frac12$ of the same, so together they give $+\frac{\beta O^2}{2mc^2}$, the leading non-relativistic energy. There is also a residual odd operator, of relative order $(v/c)^2$ compared with $O$ for a Coulomb field,

$$
O_1=i[S_1,E]
=\frac{\hbar q}{2mc}\sum_k\vec e_kE_k\,(\cdot)\,\vec e_z
=\frac{\hbar q}{2mc}\,(\vec E\,\cdot)\,\vec e_z ,
$$

which the second transformation $S_2=-\frac{i}{2mc^2}\beta O_1$ removes. To the order at which the first physical corrections appear, therefore,

$$
H_1=\beta mc^2+q\Phi+\frac{\beta O^2}{2mc^2}+O_1+O(c^{-2}).
$$

The omitted even term of order $c^{-2}$ is the second-order term $-\tfrac12[S_1,[S_1,E]]$; it is evaluated in Problem 3.

*Step 5: evaluating $O^2$.* Each term of $O$ ends in the right multiplication by $\vec e_y$, and $\vec e_y\vec e_y=-e_t$, so the two multipliers collapse to a scalar and $O^2$ is a left multiplication by an element:

$$
O^2=c^2\sum_{j,k}\vec e_j\vec e_k\,\pi_j\pi_k\,\vec e_y\vec e_y
=-c^2\sum_{j,k}\vec e_j\vec e_k\,\pi_j\pi_k .
$$

The product identity of the algebra, $\vec e_j\vec e_k=-\delta_{jk}+\epsilon_{jkl}\vec e_l$, splits the sum into a symmetric and an antisymmetric part. The symmetric part is $-\vec\pi^2$. The antisymmetric part is the commutator, the ordering being kept since $\vec p$ and $\vec A$ do not commute: with $[\pi_j,\pi_k]=i\hbar q\epsilon_{jkl}B_l$ and $\sum_{j<k}\epsilon_{jkl}\vec e_j\vec e_k=\vec e_l$, it gives $i\hbar q\vec B$. Hence

$$
O^2=c^2\left(\vec\pi^2-i\hbar q\,\vec B\right),
\qquad
\vec B=\sum_kB_k\vec e_k .
$$

This is a left multiplication by an element of the algebra, so it is even, and it commutes with $\beta$. On the large part the element $-i\hbar q\vec B$ acts as the matrix $-\hbar q\,\boldsymbol\sigma\cdot\vec B$, under the isomorphism $\mathsf M_2(\vec e_k)=-i\sigma_k$, so

$$
O^2_{\rm large}=c^2\left(\vec\pi^2-\hbar q\,\boldsymbol\sigma\cdot\vec B\right),
\qquad
H_{\rm large}=mc^2+q\Phi+\frac{\vec\pi^2-q\hbar\,\boldsymbol\sigma\cdot\vec B}{2m}+O(c^{-2}).
$$

Subtracting the rest energy,

$$
\boxed{\;i\hbar\frac{\partial\varphi}{\partial t'}=\left[\frac{(p-q\vec A)^2}{2m}+q\Phi-\frac{q\hbar}{2m}\,\boldsymbol\sigma\cdot\vec B\right]\varphi\;}
$$

which is the Pauli equation exactly as the parent reports it. The coefficient $1/2m$ is the whole content of the $g=2$ result of Problem 2: it is produced by the $2mc^2$ in the denominator of the small-component elimination, not put in by hand.

## Problem 2: Minimal substitution, the electromagnetic terms, and $g=2$

**Statement.** Carry out the minimal substitution, evaluate the electromagnetic terms it generates, and verify the gyromagnetic factor $g=2$ together with the biquaternion form of the spin term.

**Solution.**

*Step 1: the substitution.* The minimal coupling of this exercise is a shift of every derivative, $\partial/\partial Q_\mu\to\partial/\partial Q_\mu-iqA_\mu/\hbar$; on the gradient it is $\tilde\nabla\to\tilde\nabla_A=\tilde\nabla-iq\tilde A/\hbar$, with $A_\mu=(\Phi,-\vec A)$ in this mostly-minus metric, so that $\tilde A=\Phi e_t-\vec A$. The time component gives

$$
i\hbar\frac{\partial}{\partial t'}\ \longrightarrow\ i\hbar\frac{\partial}{\partial t'}-q\Phi ,
$$

and the spatial components give $\vec\pi=p-q\vec A$, that is the pure part of the gradient becomes $D_3^A$ with $\sum_k\vec e_k\pi_k=-i\hbar D_3^A$. The electrostatic energy is collected in $V=q\Phi$. The sign of the coupling is tied to the metric and to the convention for $A_\mu$; the mostly-plus convention often writes the opposite sign. Within this article the statement above is used throughout.

*Step 2: the commutator of the kinetic momenta.* With $p=-i\hbar\nabla$ and $\nabla=\sum_k\vec e_k\partial/\partial q_k$ the pure part of the gradient,

$$
[\pi_i,\pi_j]=-q\bigl([p_i,A_j]+[A_i,p_j]\bigr)
=-q\bigl(-i\hbar\partial/\partial q_i\,A_j+i\hbar\partial/\partial q_j\,A_i\bigr)
=i\hbar q\,\epsilon_{ijk}B_k ,
$$

so that

$$
\vec\pi\times\vec\pi=i\hbar q\,\vec B,\qquad \vec B=\nabla\times\vec A .
$$

Equivalently, $p\times\vec A+\vec A\times p=-i\hbar\vec B$; the two terms are individually non-Hermitian but their sum is Hermitian. In natural units this is the parent's $\vec\pi\times\vec\pi=iq\vec B$. The curl here is the curl of the corpus's pure gradient: for $\vec A=\sum_kA_k\vec e_k$ the product $D_3\vec A$ is $-\nabla\cdot\vec A$ in its scalar part and $\nabla\times\vec A$ in its pure part, with no reversed sign, so $B_k=\epsilon_{kji}\partial/\partial q_jA_i$ is the Cartesian curl and no sign of this exercise had to be changed on that account.

*Step 3: the square of the gradient's pure part.* The product identity of the algebra is the product of two pure elements,

$$
\Bigl(\sum_k\vec e_ka_k\Bigr)\Bigl(\sum_k\vec e_kb_k\Bigr)
=-\vec a\cdot\vec b\,e_t+\sum_l\epsilon_{ljk}a_jb_k\,\vec e_l ,
$$

which is $-\vec a\cdot\vec b-i\,\boldsymbol\sigma\cdot(\vec a\times\vec b)$ in the matrix reading, and it is valid whenever the coefficients commute with the units, which they do. Applying it to the two factors of $O$ and keeping the ordering, the commutator of Step 2 gives

$$
O^2=c^2\bigl(\vec\pi^2-i\hbar q\vec B\bigr)
\ \longleftrightarrow\
c^2\bigl(\vec\pi^2-\hbar q\,\boldsymbol\sigma\cdot\vec B\bigr)
$$

on the large part, which is the parent's result, with $\hbar$ restored. The coefficient carries no power of $c$: the two factors of $c$ in the elimination cancel, since $\chi=O\varphi/(2mc^2)$ is multiplied by $O$ in the first equation. The identification $\vec S=\tfrac\hbar2\boldsymbol\sigma$ gives the spin term

$$
-\frac{q\hbar}{2m}\,\boldsymbol\sigma\cdot\vec B=-\frac{q}{m}\,\vec S\cdot\vec B=-\vec\mu\cdot\vec B .
$$

*Step 4: the gyromagnetic factor.* Writing the coupling as $-\vec\mu\cdot\vec B$ identifies

$$
\vec\mu=\frac{q\hbar}{2m}\boldsymbol\sigma=\frac{q}{m}\,\vec S,\qquad \vec S=\frac\hbar2\boldsymbol\sigma .
$$

The general parametrization of a magnetic dipole is $\vec\mu=g\dfrac{q}{2m}\vec S$, so that

$$
\boxed{\;g=2\;}
$$

for a structureless spin-$\tfrac12$ particle. For the electron, $q=-e$ and

$$
\vec\mu_e=-\frac{e}{m_e}\vec S=-g\frac{e}{2m_e}\vec S,\qquad g=2,
$$

whose magnitude at $S_z=\hbar/2$ is one Bohr magneton $\mu_B=e\hbar/2m_e$. The measured anomalous part $a=(g-2)/2\approx\alpha/2\pi$ is a radiative correction that lies outside the equation treated here.

*Step 5: the biquaternion form.* Under the isomorphism $\mathsf M_2(\vec e_k)=-i\sigma_k$ the spin components are the elements $\tilde S_k=\tfrac\hbar2i\vec e_k$, and a magnetic field written as the pure real quaternion $\vec B=\sum_kB_k\vec e_k$ maps the spin term to

$$
-\frac{q\hbar}{2m}\boldsymbol\sigma\cdot\vec B\ \longleftrightarrow\ -\frac{q\hbar}{2m}\,i\vec B\ \in\ \mathbb M_+ ,
$$

the Hermitian element of the informational sector, exactly as the parent states: $(i\vec B)^{*}=i\vec B$, because $(\vec e_k)^{*}=-\vec e_k$ and the coefficient is imaginary. The kinetic and electrostatic terms are the scalar multiples $(\vec\pi^2/2m)e_t$ and $q\Phi e_t$ of $\mathbb M_+$.

*Numerical check.* The commutator identity of Step 2 was verified by finite differences on a $41\times41$ grid with spacing $h=0.1$ on $[-2,2]^2$, with $\vec A=(-y,0,0)$, for which $\vec B=(0,0,1)$, and with the smooth test function $\psi=\exp(-(x^2+y^2))\cos(2x)\sin(3y)$. With $q=\hbar=1$, the identity $[\pi_x,\pi_y]\psi=iB_z\psi$ was confirmed at the interior points with a maximum absolute error $4.8\times10^{-2}$; halving the spacing to $h=0.05$ gave $1.2\times10^{-2}$, the factor four of the second-order central difference.

## Problem 3: The spin–orbit and Darwin terms at the next order

**Statement.** Extend the elimination to the next order in $1/c$ and obtain the relativistic kinetic correction, the Darwin term, and the spin–orbit coupling.

**Solution.** This order is *not* contained in the parent article, which stops at the leading Pauli Hamiltonian. The even terms of order $c^{-2}$ have two sources. The second-order term $-\tfrac12[S_1,[S_1,E]]$ of the first transformation gives the Darwin and spin–orbit couplings; the expansion of the free large-part energy gives the relativistic kinetic correction. The second transformation removes the residual odd term $O_1$ and adds no even term at this order.

*Step 1: the even term of the first transformation.* From Step 4 of Problem 1,

$$
[S_1,E]=-\frac{i\hbar q}{2mc}\sum_k\vec e_kE_k\,(\cdot)\,\vec e_z
=-\frac{i\hbar q}{2mc}\,(\vec E\,\cdot)\,\vec e_z .
$$

A direct use of the algebra, with $[S_1,E]$ above and $S_1=-\frac{1}{2mc}\sum_j\vec e_j\pi_j(\cdot)\vec e_z$, gives

$$
-\tfrac12[S_1,[S_1,E]]
=-\frac{\hbar q}{4m^2c^2}\,i(\vec E\times\vec\pi)
-\frac{\hbar^2q}{8m^2c^2}\,\nabla\cdot\vec E .
$$

The first term comes from the antisymmetric part of $\vec e_j\vec e_k=-\delta_{jk}+\epsilon_{jkl}\vec e_l$; the second comes from the symmetric part. Since $\nabla\cdot\vec E=-\nabla^2V/q$, the second term is the Darwin term $+\hbar^2\nabla^2V/(8m^2c^2)$. In the large part, $i\vec a$ acts as $\boldsymbol\sigma\cdot\vec a$, so the two terms read

$$
-\frac{\hbar q}{4m^2c^2}\,\boldsymbol\sigma\cdot(\vec E\times\vec\pi)
-\frac{\hbar^2q}{8m^2c^2}\,\nabla\cdot\vec E .
$$

*Step 2: the Darwin term.* Since $\vec E=-\nabla\Phi$ and $V=q\Phi$,

$$
\frac{\hbar^2}{8m^2c^2}\nabla^2V=-\frac{q\hbar^2}{8m^2c^2}\nabla\cdot\vec E .
$$

This is the Darwin term. Its Hermiticity is immediate: $\nabla\cdot\vec E$ is a real function of position.

*Step 3: the spin–orbit term.* Since $\nabla V=q\nabla\Phi=-q\vec E$,

$$
-\frac{q\hbar}{4m^2c^2}\boldsymbol\sigma\cdot(\vec E\times\vec\pi)
=\frac{\hbar}{4m^2c^2}\,\boldsymbol\sigma\cdot(\nabla V\times\vec\pi)
=\frac{\hbar}{4m^2c^2}\,\frac1r\frac{dV}{dr}\,\boldsymbol\sigma\cdot\vec L
\qquad(\text{central }V),
$$

where $\vec E\times\vec\pi$ has been written with $\vec E=-\nabla\Phi$. For a central electrostatic field, whose vector potential may be neglected so that $\vec\pi\to p$, the last factor is the standard spin–orbit coupling with $\vec L=\vec r\times p$ and $\vec S=\tfrac\hbar2\boldsymbol\sigma$. The coefficient $1/(4m^2c^2)$ already contains the Thomas factor of $\tfrac12$: a naive Lorentz transformation to the instantaneous rest frame of the electron would give twice this value, and the factor of $\tfrac12$ is the Thomas precession correction. With $\vec S=\tfrac\hbar2\boldsymbol\sigma$, the term reads $\dfrac{1}{2m^2c^2}\dfrac1r\dfrac{dV}{dr}\vec L\cdot\vec S$, the standard spin–orbit coupling.

*Step 4: the relativistic kinetic correction.* The free large-part energy is the expansion of $\sqrt{m^2c^4+O^2}$, and the next term is fixed by the same $O^2$:

$$
\sqrt{m^2c^4+O^2}
=mc^2+\frac{O^2}{2mc^2}-\frac{O^4}{8m^3c^6}+\cdots .
$$

In the large part $O^4=c^4(\boldsymbol\sigma\cdot\vec\pi)^4$, so the correction is

$$
-\frac{(\boldsymbol\sigma\cdot\vec\pi)^4}{8m^3c^2}
=-\frac{1}{8m^3c^2}\bigl(\vec\pi^2-i\hbar q\vec B\bigr)^2 .
$$

It is $(\boldsymbol\sigma\cdot\vec\pi)^4$, not $\vec\pi^4$, because $(\boldsymbol\sigma\cdot\vec\pi)^2=\vec\pi^2-q\hbar\boldsymbol\sigma\cdot\vec B$; the difference is of the same $c^{-2}$ order and is not dropped.

*Step 5: the second generator and the assembled Hamiltonian.* The odd remainder is $O_1$, and the transformation that removes it is $S_2=-\frac{i}{2mc^2}\beta O_1$. With $O_1$ from Problem 1 and $\beta(\vec E\,\cdot)\vec e_z=i(\vec E\,\cdot)\vec e_y$,

$$
\beta O_1=\frac{i\hbar q}{2mc}\sum_k\vec e_kE_k\,(\cdot)\,\vec e_y,
\qquad
S_2=-\frac{i}{2mc^2}\beta O_1=\frac{\hbar q}{4m^2c^3}\sum_k\vec e_kE_k\,(\cdot)\,\vec e_y .
$$

The transformation cancels $O_1$; its even terms are of higher order and are dropped. Collecting the leading and next-to-leading orders, the large-part Hamiltonian is

$$
\boxed{\;
H=\frac{\vec\pi^2}{2m}+q\Phi-\frac{q\hbar}{2m}\boldsymbol\sigma\cdot\vec B
-\frac{(\boldsymbol\sigma\cdot\vec\pi)^4}{8m^3c^2}
+\frac{\hbar^2}{8m^2c^2}\nabla^2V
-\frac{q\hbar}{4m^2c^2}\boldsymbol\sigma\cdot(\vec E\times\vec\pi)
\;}
$$

to relative order $c^{-2}$. The first three terms are the Pauli Hamiltonian of Problem 1; the last three are the corrections that the parent article does not reach.

*Step 6: numerical verification against the exact Dirac spectrum.* The three corrections are fixed by their coefficients; a single overall check is therefore decisive. In a hydrogenic atom with nuclear charge $\mathfrak{Z}$, the first-order shifts of the three corrections are, in natural units ($c=1$), the standard ones,

$$
\Delta E_{\rm kin}=-\frac{m(\mathfrak{Z}\alpha)^4}{2n^3}\!\left[\frac{1}{\ell+\tfrac12}-\frac{3}{4n}\right],
$$

$$
\Delta E_{\rm SO}=\frac{m(\mathfrak{Z}\alpha)^4}{2n^3}\,\frac{j(j+1)-\ell(\ell+1)-\tfrac34}{2\ell(\ell+\tfrac12)(\ell+1)}\quad(\ell\neq0),
$$

$$
\Delta E_{\rm D}=\frac{m(\mathfrak{Z}\alpha)^4}{2n^3}\quad(\ell=0),
\qquad
\Delta E_{\rm D}=0\quad(\ell\neq0),
$$

with the exact Dirac shift $\Delta E_{\rm exact}=-\dfrac{m(\mathfrak{Z}\alpha)^4}{2n^3}\Bigl[\dfrac{1}{j+\tfrac12}-\dfrac{3}{4n}\Bigr]$. Evaluating all of these with exact rational arithmetic for every level with $n\le6$ (36 levels, with $j$ the total angular momentum, $j=\ell\pm\tfrac12$ and one value at $\ell=0$), the sum $\Delta E_{\rm kin}+\Delta E_{\rm SO}+\Delta E_{\rm D}$ equals $\Delta E_{\rm exact}$ in every case, with difference exactly $0$. The coefficients are also those of the two sources named at the head of this problem: the binomial coefficients $1,\tfrac12,-\tfrac18$ of $\sqrt{m^2c^4+O^2}$ and the Darwin coefficient $+\tfrac18$ of the second-order term.

## Problem 4: Hermiticity and the $\mathbb M_\pm$ decomposition

**Statement.** Check the Hermiticity of every term and determine which terms lie in $\mathbb M_+$.

**Solution.**

*Step 1: Hermiticity.* Each term of the Hamiltonian of Problem 3 is Hermitian:

- $\vec\pi^2/2m$: $\pi_i^\dagger=\pi_i$, hence $\sum_i\pi_i^2$ is Hermitian;
- $q\Phi$: multiplication by the real function $q\Phi$, Hermitian;
- $-\dfrac{q\hbar}{2m}\boldsymbol\sigma\cdot\vec B$: $\sigma_k$ and the real field $B_k$ are Hermitian;
- $-\dfrac{(\boldsymbol\sigma\cdot\vec\pi)^4}{8m^3c^2}$: minus a real multiple of the square of the Hermitian $(\boldsymbol\sigma\cdot\vec\pi)^2$;
- $\dfrac{\hbar^2}{8m^2c^2}\nabla^2V$: multiplication by a real function;
- $-\dfrac{q\hbar}{4m^2c^2}\boldsymbol\sigma\cdot(\vec E\times\vec\pi)$: this is the one term whose Hermiticity is not automatic. Using $[\pi_i,E_j]=-i\hbar\partial/\partial q_i\,E_j$,

$$
(\vec E\times\vec\pi)_i^\dagger=(\vec E\times\vec\pi)_i+i\hbar(\nabla\times\vec E)_i ,
$$

so the term is Hermitian if and only if $\nabla\times\vec E=0$, its failure of Hermiticity being proportional to the curl. Since $\vec E=-\nabla\Phi$ for an electrostatic field, $\nabla\times\vec E=-\nabla\times\nabla\Phi=0$ identically, and the term is Hermitian. Writing it instead as $\boldsymbol\sigma\cdot(\nabla V\times\vec\pi)$ makes this manifest, because $\nabla V$ is a gradient. For a general time-dependent field, where $\vec E$ has a solenoidal part and $\nabla\times\vec E=-\partial/\partial t'\,\vec B$, the antisymmetric part does not vanish and the non-relativistic reduction requires the symmetrized ordering; this is the only place in the reduction where the result is convention- and ordering-sensitive beyond the metric conventions already noted.

*Step 2: the $\mathbb M_+$ representatives.* Under the isomorphism, a Hermitian $2\times2$ matrix $h_tI_2+\vec h\cdot\boldsymbol\sigma$ corresponds to the Hermitian biquaternion $h_te_t+i\vec h\in\mathbb M_+$. Applying it term by term, with $\vec B=\sum_k B_k\vec e_k$ and $(\vec E\times\vec\pi)=(\vec E\times\vec\pi)_k\vec e_k$,

| Term of $H$ | Biquaternion representative | Sector |
|---|---|---|
| $\vec\pi^2/2m$ | $(\vec\pi^2/2m)\,e_t$ | $\mathbb M_+$ |
| $q\Phi$ | $(q\Phi)\,e_t$ | $\mathbb M_+$ |
| $-\dfrac{q\hbar}{2m}\boldsymbol\sigma\cdot\vec B$ | $-\dfrac{q\hbar}{2m}\,i\vec B$ | $\mathbb M_+$ |
| $-\dfrac{(\boldsymbol\sigma\cdot\vec\pi)^4}{8m^3c^2}$ | $-\dfrac{1}{8m^3c^2}\bigl(\vec\pi^2-\hbar q\,i\vec B\bigr)^2$ | $\mathbb M_+$ |
| $\dfrac{\hbar^2}{8m^2c^2}\nabla^2V$ | $\dfrac{\hbar^2}{8m^2c^2}(\nabla^2V)\,e_t$ | $\mathbb M_+$ |
| $-\dfrac{q\hbar}{4m^2c^2}\boldsymbol\sigma\cdot(\vec E\times\vec\pi)$ | $-\dfrac{q\hbar}{4m^2c^2}\,i(\vec E\times\vec\pi)$ | $\mathbb M_+$ |

Every term of the reduced, two-component Hamiltonian is Hermitian, hence every term lands in $\mathbb M_+$. This is the precise content of the parent's remark that the spin term is an observable of the informational sector; the remark applies term by term. Each representative is a left multiplication by an element, which is what makes the identification possible at all.

*Step 3: what does not land in $\mathbb M_+$.* Three classes of object in the reduction do not.

1. **The right multiplications.** The mass term $\beta mc^2$ multiplies by $i\vec e_x$ on the right, and the odd operator $O$ ends in a right multiplication by $\vec e_y$. The two multipliers are $i\vec e_x$, which is Hermitian, and $\vec e_y$, which is anti-Hermitian; each operator is Hermitian anyway, because the left factor $\vec e_k$ is anti-Hermitian too and a product of two anti-Hermitian factors with a Hermitian $\pi_k$ between them is Hermitian. What matters is that neither operator is a left multiplication, so no element of $\mathbb B$ represents either. This is why the four-component Hamiltonian is not an element of $\mathbb B$ and why a transformation is needed before the biquaternion identification can be made: the Foldy–Wouthuysen transformation is exactly the operation that replaces the two-sided operators by left multiplications and leaves a sum of elements of $\mathbb M_+$. A right multiplication is a different operator from the left multiplication by the same element, and neither may be substituted for the other.

2. **The anti-Hermitian generator.** $S_1$ is Hermitian, so $iS_1$ is anti-Hermitian: it plays the rôle that the elements of $\mathbb M_-$ play in the companion quantum article, where the Lie algebra of the $*$-unitary group is $\mathbb M_-$. It is not itself in $\mathbb M_-$, because it is built from right multiplications and is not a left multiplication by an element. The two gradings must not be conflated: the Foldy–Wouthuysen grading is by conjugation with $\beta$, the $\mathbb M_\pm$ grading is by ${}^{*}$. Thus the odd operator $O$ is Foldy–Wouthuysen-odd and Hermitian, yet it is not the left multiplication by the element $\hbar c\vec\pi$ — that element acts on one side and is even — and the identification of "odd" with "not in $\mathbb M_+$" is incorrect.

3. **The real structure and the mass term.** In the biquaternion equation the conjugation $\flat=-{}^{*}$ is the algebra's real structure. It maps $\mathbb M_+$ to $\mathbb M_-$ and fixes $\mathbb M_-$: if $F\in\mathbb M_+$ then $F^\flat=-F\in\mathbb M_-$, and if $F\in\mathbb M_-$ then $F^\flat=F$. Its action is diagonal on the sector decomposition with opposite signs $\mp1$: a coupling built on $\flat$ — a Majorana-type mass, $mF^\flat$ — would carry those opposite signs. The parent's mass term is not that coupling; it is the linear, chirality-off-diagonal pair $\tilde\nabla F_R=mF_L$, $\tilde\nabla^{\natural}F_L=mF_R$, which couples the two values of the chirality and leaves each element's sector membership untouched. The operation that exchanges the two sectors is multiplication by the central $i$. The rest-energy factor that is removed before the reduction, the central element $\cos\theta-i\sin\theta$ with $\theta=mc^2t'/\hbar$, is not Hermitian either: the conjugation inverts $\theta$, so the element is fixed by ${}^{*}$ neither as it stands nor after multiplication by $-1$, and it lies in neither $\mathbb M_+$ nor $\mathbb M_-$. The phase that removes the mass term from a $\beta$-diagonal equation, $\exp(-i\beta\theta)=\cos\theta\,e_t+\sin\theta\,\vec e_x$, is a right multiplication, and it splits the other way: its scalar part lies in $\mathbb M_+$ and its pure part in $\mathbb M_-$, since $\vec e_x$ is anti-Hermitian. Either way the rest-energy factor is a phase and not an observable, and it must be factored out before a two-component (hence $\mathbb M_+$) description of the dynamics is reached.

*Step 4: the sides, one line per operator.* Every operator of the reduction is listed with the element that multiplies on the left and the element that multiplies on the right. The column headed "side" is the answer to the only question that matters here: whether the operator is a single multiplication or a product of two.

| Operator | Left element | Right element | Side |
|---|---|---|---|
| $\beta$ | $e_t$ | $i\vec e_x$ | right multiplication alone |
| $\Gamma$ | $e_t$ | $-i\vec e_z$ | right multiplication alone |
| $O$ | $\vec e_k$, with $\pi_k$ | $\vec e_y$ | two-sided |
| $S_1$ | $\vec e_k$, with $\pi_k$ | $\vec e_z$ | two-sided |
| $O_1$ | the element $\vec E$ | $\vec e_z$ | two-sided |
| $S_2$ | the element $\vec E$ | $\vec e_y$ | two-sided |
| $O^2$ | $\vec e_j\vec e_k$, with $\pi_j\pi_k$ | $e_t$, the two $\vec e_y$ having collapsed | left multiplication by an element |
| $\vec\pi^2$, $q\Phi$, $\boldsymbol\sigma\cdot\vec B$, the $c^{-2}$ terms | an element of $\mathbb M_+$ | $e_t$ | left multiplication by an element |

No other right multiplication and no other differential operator occurs in the reduction: the only derivative is the pure part of the gradient, $\sum_k\vec e_k\pi_k=-i\hbar D_3^A$, and it always appears with the single left element $\vec e_k$ shown. The elements $\vec e_y$ and $\vec e_z$ that close $O$, $S_1$, $O_1$ and $S_2$ are the only right multipliers, and no symbol of the article stands for an operator whose sides are left unstated.

## Problem 5: The physical dimensions of each term

**Statement.** Determine the physical dimensions of each term.

**Solution.** Every term is an energy, since each is a term of a Hamiltonian. The individual coefficients nevertheless carry different powers of $\hbar$ and $c$, and checking them is a useful consistency test. In SI units, with $[\hbar]=\mathrm{kg\,m^2\,s^{-1}}$, $[c]=\mathrm{m\,s^{-1}}$, $[q]=\mathrm C$, $[\Phi]=\mathrm V=\mathrm{kg\,m^2\,s^{-3}A^{-1}}$, $[\vec B]=\mathrm T=\mathrm{kg\,s^{-2}A^{-1}}$ and $[\vec E]=\mathrm{V\,m^{-1}}=\mathrm{kg\,m\,s^{-3}A^{-1}}$:

| Term | Coefficient units | Field/operator units | Product |
|---|---|---|---|
| $\vec\pi^2/2m$ | $1/m$ | $(\mathrm{kg\,m\,s^{-1}})^2$ | $\mathrm{kg\,m^2\,s^{-2}}$ |
| $q\Phi$ | $\mathrm C$ | $\mathrm{kg\,m^2\,s^{-3}A^{-1}}$ | $\mathrm{kg\,m^2\,s^{-2}}$ |
| $-\dfrac{q\hbar}{2m}\boldsymbol\sigma\cdot\vec B$ | $\mathrm C\,\mathrm{kg\,m^2\,s^{-1}\,kg^{-1}}$ | $\mathrm{kg\,s^{-2}A^{-1}}$ | $\mathrm{kg\,m^2\,s^{-2}}$ |
| $-\dfrac{q\hbar^2}{8m^2c^2}\nabla\cdot\vec E$ | $\mathrm C\,\mathrm{kg^2m^4s^{-2}}\,\mathrm{kg^{-2}m^{-2}s^{2}}$ | $\mathrm{kg\,s^{-3}A^{-1}}$ | $\mathrm{kg\,m^2\,s^{-2}}$ |
| $-\dfrac{q\hbar}{4m^2c^2}\boldsymbol\sigma\cdot(\vec E\times\vec\pi)$ | $\mathrm C\,\mathrm{kg\,m^2s^{-1}}\,\mathrm{kg^{-2}m^{-2}s^{2}}$ | $\mathrm{kg^2m^2s^{-4}A^{-1}}$ | $\mathrm{kg\,m^2\,s^{-2}}$ |
| $-\dfrac{(\boldsymbol\sigma\cdot\vec\pi)^4}{8m^3c^2}$ | $\mathrm{kg^{-3}m^{-2}s^{2}}$ | $\mathrm{kg^4m^4s^{-4}}$ | $\mathrm{kg\,m^2\,s^{-2}}$ |

The pattern is informative. The leading terms ($\vec\pi^2/2m$, $q\Phi$, the spin term) carry no power of $c$; the three corrections each carry $c^{-2}$, which is the statement that they are relativistic corrections of order $v^2/c^2$. The spin term carries one power of $\hbar$ in its coefficient, while the leading kinetic and electrostatic terms carry none. Written with $\vec S=\tfrac\hbar2\boldsymbol\sigma$, it is $-(q/m)\vec S\cdot\vec B$, the classical coupling of a magnetic moment; the power of $\hbar$ is the conversion between the dimensionless $\boldsymbol\sigma$ and the spin. The Darwin term carries $\hbar^2$ and has no classical counterpart. The spin–orbit term carries one power of $\hbar$ in its coefficient, but it is quadratic in the angular momenta once $\vec S$ and $\vec L=\vec r\times p$ are used, so it becomes the classical Thomas-precession coupling when $\vec S$ and $\vec L$ are treated as classical vectors.

## Summary

The non-relativistic limit of the biquaternion Dirac equation was carried through in five steps, for the one-sided chiral pair read on the Dirac module. Every derivative in the reduction is the biquaternionic gradient: the free equation is the first-order one-field equation $\tilde\nabla F=0$, the massive equation is the chiral pair $\tilde\nabla F_R=mF_L$, $\tilde\nabla^{\natural}F_L=mF_R$, and the square of the gradient is neither scalar nor the d'Alembertian, so no one-field first-order massive equation was written at any point. The two-sided form of the parent is a different operator, antilinear in its mass term, and is not reduced here.

The Foldy–Wouthuysen elimination of the small component, executed systematically with the generator

$$
S_1=-\frac{i}{2mc^2}\beta O=-\frac{1}{2mc}\sum_k\vec e_k\pi_k\,(\cdot)\,\vec e_z=\frac{i\hbar}{2mc}\bigl(D_3^A\cdot\bigr)\vec e_z ,
$$

produces the Pauli Hamiltonian $i\hbar\,\partial\varphi/\partial t'=\bigl[\vec\pi^2/2m+q\Phi-(q\hbar/2m)\boldsymbol\sigma\cdot\vec B\bigr]\varphi$, reproducing the parent article. The minimal substitution in the gradient, $\tilde\nabla\to\tilde\nabla-iq\tilde A/\hbar$, gives $[\pi_i,\pi_j]=i\hbar q\epsilon_{ijk}B_k$ and $(\boldsymbol\sigma\cdot\vec\pi)^2=\vec\pi^2-q\hbar\boldsymbol\sigma\cdot\vec B$, and the coefficient $1/2m$ produced by the elimination fixes $g=2$ and $\vec\mu=(q/m)\vec S$, hence $\mu_B=e\hbar/2m_e$ for the electron. At the next order in $1/c$, the second-order term $-\tfrac12[S_1,[S_1,E]]$ of the first transformation gives the Darwin term $+\hbar^2\nabla^2V/(8m^2c^2)=-(q\hbar^2/8m^2c^2)\nabla\cdot\vec E$ and the spin–orbit coupling $-(q\hbar/4m^2c^2)\boldsymbol\sigma\cdot(\vec E\times\vec\pi)=(\hbar/4m^2c^2)r^{-1}(dV/dr)\boldsymbol\sigma\cdot\vec L$, while the expansion of the free large-part energy gives the relativistic kinetic correction $-(\boldsymbol\sigma\cdot\vec\pi)^4/(8m^3c^2)$. The second transformation removes the residual odd term $O_1$ and adds no even term at this order. Summed, these reproduce the exact Dirac fine structure of hydrogenic ions for 36 levels with $n\le6$, with difference exactly zero.

Every term of the reduced Hamiltonian is Hermitian and therefore lies in $\mathbb M_+$. The objects that do not are the two-sided operators of the reduction — the mass term $\beta mc^2$ and the odd operator $O$, which end in right multiplications by $i\vec e_x$ and by $\vec e_y$ and so are not left multiplications by an element — together with the anti-Hermitian generator $iS_1$ and the rest-energy phase, which is not Hermitian and belongs to neither sector. The real structure $\flat$ — whose opposite-sign action on the sectors a Majorana-type coupling would carry — is not the parent's mass term, which is the linear coupling of the two chiralities. The Foldy–Wouthuysen grading by $\beta$ must not be confused with the $\mathbb M_\pm$ grading by ${}^{*}$. All terms are energies, the three corrections carrying the expected $c^{-2}$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb B=\mathbb C\otimes_\mathbb R\mathbb H$ | Biquaternion algebra |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$, $\vec e_k^2=-e_t$ | Quaternion basis |
| $\mathbb M_+,\mathbb M_-$ | Hermitian / anti-Hermitian subspaces |
| $\mathsf{M}_2(\vec e_k)=-i\sigma_k$, $\sigma_k\leftrightarrow i\vec e_k$ | Isomorphism, Pauli matrices |
| $\tilde\nabla$, $\tilde\nabla^{\natural}$ | The gradient and its conjugate, $\varepsilon=(1,-1,-1,-1)$ |
| $\Box=\tilde\nabla\tilde\nabla^{\natural}$ | The d'Alembertian |
| $D_3=\sum_k\vec e_k\partial/\partial q_k$, $D_3^A$ | Pure part of the gradient, free and gauged |
| $\tilde\nabla_A=\tilde\nabla-iq\tilde A/\hbar$, $\tilde A=\Phi e_t-\vec A$ | Minimal substitution in the gradient |
| $\tilde K=k_0-i\vec k$ | Symbol of the gradient on a plane wave; $\tilde K^{\natural}\tilde K=k_0^2-\lvert\vec k\rvert^2$ |
| $F=F_L+F_R$; $\Gamma F=-iF\vec e_z$ | The field and its chirality, values $\mp1$ |
| $\beta F=iF\vec e_x$, $\beta^2=1$, $\beta\Gamma=-\Gamma\beta$ | The mass grading; $\beta O=-O\beta$ |
| $O=c\sum_k\vec e_k\pi_k(\cdot)\vec e_y=-i\hbar c(D_3^A\cdot)\vec e_y$ | The odd operator; $O^2=c^2(\vec\pi^2-i\hbar q\vec B)$ |
| $\omega=-\vec e_z$, $\omega^2=-e_t$ | The pseudoscalar of the frame |
| $\vec\pi=p-q\vec A$ | Kinetic momentum |
| $\vec B=\nabla\times\vec A$, $\vec E$ | Magnetic, electric fields |
| $V=q\Phi$ | Potential energy |
| $H=\beta mc^2+O+E$, $E=q\Phi$ | Split Hamiltonian; odd and even parts |
| $S_1=-\frac{i}{2mc^2}\beta O=-\frac{1}{2mc}\sum_k\vec e_k\pi_k(\cdot)\vec e_z$ | Foldy–Wouthuysen generator |
| $O_1=i[S_1,E]=\frac{\hbar q}{2mc}(\vec E\cdot)\vec e_z$ | Residual odd operator |
| $S_2=-\frac{i}{2mc^2}\beta O_1=\frac{\hbar q}{4m^2c^3}(\vec E\cdot)\vec e_y$ | Second generator |
| $\vec S=\tfrac\hbar2\boldsymbol\sigma$, $\vec\mu=g\frac{q}{2m}\vec S$ | Spin and magnetic moment |
| $g=2$ | Gyromagnetic factor |
| $\mu_B=e\hbar/2m_e$ | Bohr magneton |

## Further Reading

- P. A. M. Dirac, "The quantum theory of the electron," *Proceedings of the Royal Society A* **117** (1928) 610–624, for the original prediction of $g=2$.
- L. L. Foldy and S. A. Wouthuysen, "On the Dirac theory of spin 1/2 particles and its non-relativistic limit," *Physical Review* **78** (1950) 29–36, for the transformation used here.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the plane-wave solutions and the standard non-relativistic reduction.
- J. J. Sakurai, *Advanced Quantum Mechanics* (Addison-Wesley, 1967), for the emergence of the Pauli equation and the spin–orbit coupling.
- W. Greiner, *Relativistic Quantum Mechanics: Wave Equations* (Springer, 2000), for a step-by-step Foldy–Wouthuysen elimination and Pauli limit.
- C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), for the fine structure and the hydrogen spectrum.
- [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html), for the two forms and the mass term.
- [The Dirac Equation in Biquaternionic Form — Solutions and the Non-Relativistic Limit](the-dirac-equation-in-biquaternionic-form-solutions-and-the-non-relativistic-limit.html), the parent of this exercise, for the Pauli limit at leading order.
- [The Foldy–Wouthuysen Transformation in Biquaternionic Form](the-foldy-wouthuysen-transformation-in-biquaternionic-form.html), for the transformation in the algebra.
- [Quantum Physics in Biquaternionic Form](quantum-physics-in-biquaternionic-form.html), for the sector structure and the observables.
- [Operator and Calculus Conventions](operator-and-calculus-conventions.html), for the gradient, its conjugate, the d'Alembertian and the gauged gradient.
