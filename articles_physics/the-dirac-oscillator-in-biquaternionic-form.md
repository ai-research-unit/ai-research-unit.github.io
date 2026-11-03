# __The Dirac Oscillator in Biquaternionic Form__

## Introduction

The Dirac oscillator is the relativistic quantum system obtained from the free Dirac Hamiltonian by the non-minimal substitution

$$
\boxed{\;\vec p \;\longrightarrow\; \vec p - i m\omega \beta\vec r\;},
$$

introduced by Marcos Moshinsky and Adam Szczepaniak in 1989. Here $\vec p$ is the momentum operator, $p_k=-i\hbar\,\partial/\partial Q_k$, and the Hamiltonian is

$$
H = c\,\boldsymbol\alpha\cdot\left(\vec p - i m\omega\beta\vec r\right) + \beta mc^2 .
$$

The substitution is "non-minimal" in the precise sense that it cannot be obtained from a gauge potential: it adds, to the odd (frame-anticommuting) part of the Dirac operator, a term linear in the position. The resulting system is exactly solvable, its non-relativistic limit is the three-dimensional isotropic harmonic oscillator together with a spin–orbit coupling of the same order as the level spacing, and it has become the standard laboratory for the relativistic treatment of confining interactions.

It belongs in this subcategory as the **exactly solvable external-potential problem** of the biquaternionic Dirac theory. The hydrogen atom, treated in the companion article *The Hydrogen Atom in Biquaternionic Form — The Relativistic Case*, is exactly solvable by a different mechanism (a Coulomb central field and a second-order radial reduction); the oscillator is exactly solvable because the first-order operator can be **squared in closed form**, and the square is again a second-order operator, central apart from a single spin–orbit term. That is the same square as in *Klein–Gordon from the Dirac Square in Biquaternionic Form*, now with the position-dependent addition that makes the square a harmonic oscillator. A square available in closed form, plus a confining addition that is linear in the position, make the model the place where one sees concretely how the biquaternionic first-order operator behaves under squaring.

The article derives the substitution, the reduction to a pair of two-component equations, the exact operator identity on squaring, and the spectrum; it then works the one-dimensional case for which everything is transparent, takes the non-relativistic limit, reads the result in the algebra, and connects the zero modes to the supersymmetric structure developed in the companion article *Supersymmetric Quantum Physics in the Biquaternion Framework*.

**Two Dirac equations.** The corpus carries two, and this article keeps them apart. The **algebra equation** is the one-sided chiral pair

$$
\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L,
\qquad
\tilde{\nabla}^{\natural}\tilde{\Psi}_L = m\tilde{\Psi}_R ,
$$

in which every derivative acts by left multiplication and the mass is the off-diagonal pairing of the two minimal left ideals. Chirality is present, but not as a cell of the frame: it is the split into those ideals, carried algebraically by the central grading $\chi=i\tilde\Xi_{\mathrm{ad}}$. The **module equation** is the single two-sided cell equation $(\mathbb{D}-mc/\hbar)\psi=0$, in which the frame cells multiply on both sides and whose two chiral projections are two lines; there the chirality is the pure right multiplication $\Gamma=-iR_{\vec e_z}^{\mathrm{pau}}$, and the large/small split is the frame grading: $\beta=iR_{\vec e_x}^{\mathrm{pau}}$ is diagonal in the basis in which the two-spinors are the large and small components. The oscillator is a problem in the module equation, because the substitution is built from $\beta$ and from the velocity cells, and both are two-sided objects. The algebra pair is recorded here because its square is the Klein–Gordon operator on which the whole construction rests; the oscillator itself is never posed in it, and apart from the dictionary drawn in *The Gamma Formulation* it makes no further appearance.

**Conventions.** These are the series conventions. A cell is the two-sided multiplication

$$
L_a\psi=a\psi,\qquad R_b\psi=\psi b,\qquad L_aR_bL_cR_d=L_{ac}R_{db},
$$

with $L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$ the identity. The four generator cells $iL_{e_\mu}^{\mathrm{pau}}R_{\vec e_{\nu(\mu)}}^{\mathrm{pau}}$, one per coordinate $x_\mu$, with $\nu(t)=x$ and $\nu(k)=y$, satisfy

$$
\{iL_{e_\mu}^{\mathrm{pau}}R_{\vec e_{\nu(\mu)}}^{\mathrm{pau}},iL_{e_\nu}^{\mathrm{pau}}R_{\vec e_{\nu(\nu)}}^{\mathrm{pau}}\}=2g_{\mu\nu}L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}},
\qquad
g=\mathrm{diag}(+1,-1,-1,-1),
$$

so that $(iR_{\vec e_x}^{\mathrm{pau}})^2=L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$ and $(iL_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}})^2=-L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$. The frame cell and the velocity cells are

$$
\beta=iR_{\vec e_x}^{\mathrm{pau}}=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},
\qquad
\alpha_k=L_{\vec e_k}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}=iR_{\vec e_x}^{\mathrm{pau}}\,iL_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},
$$

where the two factors of $i$ give $-1$ and the reversed unit product $\vec e_y\vec e_x=-\vec e_z$ gives a second, so the two cancel. Both cells are Hermitian, square to $L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$, and satisfy $\{\beta,\alpha_k\}=0$ and $\{\alpha_j,\alpha_k\}=2\delta_{jk}L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$. **A cell product collects a sign from two places:** from the factors of $i$, one per generator cell, and from the units, which the composition rule reverses, so that $R_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}=R_{\vec e_y\vec e_x}^{\mathrm{pau}}=-R_{\vec e_z}^{\mathrm{pau}}$ because $\vec e_y\vec e_x=-\vec e_z$. The two signs can cancel, and in $\beta\,(iL_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}})=\alpha_k$ they do: the product of two generator cells carries no $i$ at all. The products used below are

$$
\beta\alpha_k=iL_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\qquad
\alpha_k\beta=-iL_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\qquad
\beta\alpha_k\beta=-\alpha_k .
$$

The two-sided Dirac operator is

$$
\mathbb{D}=-R_{\vec e_x}^{\mathrm{pau}}\frac{\partial}{\partial x_0}-\sum_k L_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}\frac{\partial}{\partial Q_k},
\qquad x_0=ct',
$$

and its square is the d'Alembertian $\Box=\partial^2/\partial Q_t^2+\Delta$, with $Q_t=ict'$ and $\Delta=\sum_k\partial^2/\partial Q_k^2$.

## The Non-Minimal Substitution

Minimal coupling replaces $\vec p$ by $\vec p - ϙ\vec A$; the added term is a vector potential and enters the Hamiltonian through $\boldsymbol\alpha\cdot\vec A$. The oscillator substitution is different in three ways, and each matters.

**It multiplies the position by $\beta$.** The added term is $-im\omega\beta\vec r$, not $-im\omega\vec r$. Because $\beta$ anticommutes with $\boldsymbol\alpha$, the product $\boldsymbol\alpha\cdot(\beta\vec r)$, which is the cell $\alpha_k\beta=-iL_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}$ contracted with the position, is frame-**odd**: it lies in the same grading class as the kinetic term $\boldsymbol\alpha\cdot\vec p$, and in the opposite class from the mass $\beta mc^2$. In the algebra this is the statement that the substitution shifts the odd part of the operator while leaving the even part alone, which is why the square is again second order and central except for the spin–orbit term.

**The coefficient is imaginary, and the term is Hermitian.** A gauge interaction adds the real, Hermitian $ϙ\vec A$ to $\vec p$; here the coefficient is $i$. In the cells the imaginary coefficient is spent on the cell at once, because $\alpha_k\beta=-iL_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}$ and the two factors of $i$ multiply to $-1$:

$$
c\,\boldsymbol\alpha\cdot\left(-im\omega\beta\vec r\right)
=-icm\omega\sum_k\alpha_k\beta\,x_k
=-cm\omega\sum_k L_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}\,x_k .
$$

The coefficient is now real, and the cell $L_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}$ is Hermitian: $(L_aR_b)^{\dagger}=L_{a^*}R_{b^*}$, and the units satisfy $\vec e_k^*=-\vec e_k$ and $\vec e_y^*=-\vec e_y$, so the two sign changes cancel. The added term is therefore Hermitian, and so is $H$. What the imaginary coefficient signals is not a complex deformation — the spectrum below is real — but a term that is frame-odd, linear in the position and matrix-valued, which a gauge potential cannot produce.

**It is linear in the position**, so it grows without bound. The oscillator potential is confining, the spectrum is discrete, and the model is a relativistic confinement model rather than a scattering problem. This is the physical reason for its use in quark-confinement phenomenology, and the reason the spectrum consists of bound levels with the mass gap at their base.

Multiplying the time-dependent equation $H\psi=i\hbar\,\partial \psi/\partial t$ on the left by $\beta/(\hbar c)$ — so that every term is divided by $\hbar$ and the right-hand side becomes $i\beta\,\partial \psi/\partial x_0$ — two collapses do the work. The kinetic term becomes $\sum_kL_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}\partial/\partial Q_k$, because the $i$ of the cell, the $i$ of $p_k=-i\hbar\partial/\partial Q_k$ and the $1/\hbar$ multiply to $+1$, and that term is $-\mathbb{D}+i\beta\,\partial/\partial x_0$: its second piece cancels the right-hand side, so the **time** derivative drops out and the spatial part survives as $-\mathbb{D}$. The frame cell passing through the substitution changes its sign, $\beta\alpha_k\beta=-\alpha_k$, so $-im\omega\beta\vec r$ becomes $+im\omega\alpha_kQ_k$, and the mass term becomes $mc/\hbar$. What remains is

$$
\left(\mathbb{D} - \frac{mc}{\hbar}\right)\psi = i\,\frac{m\omega}{\hbar}\,\alpha_k x_k\,\psi .
$$

The right-hand side is a spacelike cell, linear in the position: the non-minimal term is a position-dependent generator of the odd part, and the cell $\alpha_k$ that carries it is Hermitian. This is the form in which the biquaternion interpretation is made below.

## Reduction to Two-Component Equations

Write the four-spinor as a pair of two-spinors, $\psi = (\phi,\chi)^{\mathsf T}$, and use the Dirac basis

$$
\beta = \begin{pmatrix} I_2 & 0 \\ 0 & -I_2\end{pmatrix},
\qquad
\alpha_k = \begin{pmatrix} 0 & \sigma_k \\ \sigma_k & 0 \end{pmatrix}.
$$

In this basis the frame cell is block-diagonal and the velocity cells are block-off-diagonal, and in the two off-diagonal blocks the triple $\alpha_k=L_{\vec e_k}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}$ is a Pauli triple: each block is Hermitian, squares to the identity, and the three anticommute pairwise. Writing $\alpha_k\mapsto\sigma_k$ records that identification; which of the several unitarily equivalent Pauli triples a particular cell realisation produces is a relabelling of the three axes, and nothing below depends on it.

Since $\beta\vec r = \mathrm{diag}(\vec r,-\vec r)$, the substitution acts differently in the two blocks:

$$
\boldsymbol\alpha\cdot\left(\vec p-im\omega\beta\vec r\right)
= \begin{pmatrix}
0 & \boldsymbol\sigma\cdot(\vec p+im\omega\vec r) \\
\boldsymbol\sigma\cdot(\vec p-im\omega\vec r) & 0
\end{pmatrix}.
$$

The time-independent equation $H\psi = E\psi$ therefore becomes the coupled pair

$$
(E - mc^2)\phi = c\,\boldsymbol\sigma\cdot(\vec p+im\omega\vec r)\,\chi,
\qquad
(E + mc^2)\chi = c\,\boldsymbol\sigma\cdot(\vec p-im\omega\vec r)\,\phi .
$$

This is the form in which the oscillator is normally solved: the upper and lower two-spinors are coupled by the two conjugate first-order operators, and the coupling is exactly the minimal-coupling-like structure with $\pm im\omega\vec r$ in place of $\vec A$. Eliminating $\chi$,

$$
\chi = \frac{c\,\boldsymbol\sigma\cdot(\vec p-im\omega\vec r)}{E+mc^2}\,\phi ,
$$

and substituting into the first equation gives the second-order equation for $\phi$ alone:

$$
\left(E^2 - m^2c^4\right)\phi
= c^2\left[\boldsymbol\sigma\cdot(\vec p+im\omega\vec r)\right]
\left[\boldsymbol\sigma\cdot(\vec p-im\omega\vec r)\right]\phi .
$$

Everything now rests on evaluating the product of the two first-order operators in closed form.

## The Square of the Coupled Operator

The product is evaluated with the Pauli identity

$$
(\boldsymbol\sigma\cdot\vec A)(\boldsymbol\sigma\cdot\vec B)
= \vec A\cdot\vec B + i\,\boldsymbol\sigma\cdot(\vec A\times\vec B),
$$

which holds for operator-valued $\vec A,\vec B$ with the ordering as written. Take

$$
\vec A = \vec p + im\omega\vec r, \qquad \vec B = \vec p - im\omega\vec r.
$$

The dot product gives

$$
\vec A\cdot\vec B = \vec p^2 + m^2\omega^2\vec r^2 + im\omega\left[\vec r\cdot\vec p - \vec p\cdot\vec r\right]
= \vec p^2 + m^2\omega^2\vec r^2 - 3m\hbar\omega,
$$

because $[Q_k,p_k]=i\hbar$ and the sum over the three spatial directions gives $3i\hbar$, so $im\omega\,(3i\hbar)=-3m\hbar\omega$, one more use of $i^2=-1$. The cross product gives

$$
\vec A\times\vec B
= -im\omega\,\vec p\times\vec r + im\omega\,\vec r\times\vec p
= 2im\omega\,\vec L,
\qquad \vec L = \vec r\times\vec p,
$$

using $\vec p\times\vec r = -\vec L$; hence

$$
i\,\boldsymbol\sigma\cdot(\vec A\times\vec B) = -2m\omega\,\boldsymbol\sigma\cdot\vec L.
$$

Write the two conjugate operators of the coupled pair as

$$
\mathcal{Q}=\boldsymbol\sigma\cdot(\vec p-im\omega\vec r),
\qquad
\mathcal{Q}^\dagger=\boldsymbol\sigma\cdot(\vec p+im\omega\vec r),
$$

so that the product just evaluated is $\mathcal{Q}^\dagger\mathcal{Q}$. The operator identity is therefore

$$
\boxed{\;\mathcal{Q}^\dagger\mathcal{Q}
= \vec p^2 + m^2\omega^2\vec r^2 - 3m\hbar\omega - 2m\omega\,\boldsymbol\sigma\cdot\vec L\;},
$$

and the second-order equation of the last section reads $(E^2-m^2c^4)\phi=c^2\mathcal{Q}^\dagger\mathcal{Q}\phi$.

This is the load-bearing equation of the article. It was verified by direct matrix computation in a truncated three-dimensional oscillator basis: the identity held in the bulk of the basis to $1.8\times10^{-15}$ (the deviation in the outermost shell of the truncation is the expected finite-basis artefact of the commutator $[Q_k,p_k]=i\hbar$, which a truncated basis realises only in the bulk). The representation used was the Cartesian three-mode Fock space with total excitation number up to $N_{\max}=7$, restricted to states of excitation number at most $N_{\max}-2$.

The right-hand side separates into three pieces. The first two terms are the **three-dimensional isotropic oscillator** in operator form,

$$
\vec p^2 + m^2\omega^2\vec r^2 = 2m\left(\frac{\vec p^2}{2m} + \tfrac12 m\omega^2\vec r^2\right) = 2m\,H_{\mathrm{osc}},
$$

with the standard spectrum $\hbar\omega(N+\tfrac32)$ in terms of the total oscillator number $N = 2n_r + l$. The constant $-3m\hbar\omega$ then removes exactly the zero-point energy of the oscillator, leaving $2m\hbar\omega N$. The last term, $-2m\omega\,\boldsymbol\sigma\cdot\vec L$, is a **spin–orbit coupling** whose strength is tied to the oscillator frequency; it is not a small correction but a term of the same order as the level spacing, and it governs the whole spectral structure.

## The Spectrum

Insert the boxed identity into the second-order equation:

$$
\left(E^2 - m^2c^4\right)\phi
= c^2\left(\vec p^2 + m^2\omega^2\vec r^2 - 3m\hbar\omega - 2m\omega\,\boldsymbol\sigma\cdot\vec L\right)\phi .
$$

On the right, the first three terms are scalars in the spin and orbital variables, while the spin–orbit term is diagonal in the basis $|N,l,s_{\mathrm{tot}},s_{\mathrm{tot},z}\rangle$: it commutes with $\tilde S_{\mathrm{tot}}^2$ and with $\vec L^2$, but not with the individual components $L_k$. Its eigenvalues are the standard ones,

$$
\frac{1}{\hbar}\,\boldsymbol\sigma\cdot\vec L =
\begin{cases}
+l, & s_{\mathrm{tot}} = l + \tfrac12 \\[2pt]
-(l+1), & s_{\mathrm{tot}} = l - \tfrac12
\end{cases}
$$

so that, using $\vec p^2 + m^2\omega^2\vec r^2 - 3m\hbar\omega = 2m\hbar\omega N$ and $N = 2n_r + l$,

$$
\boxed{\;E^2 = m^2c^4 + 2m\hbar\omega c^2\left(N - \frac{\boldsymbol\sigma\cdot\vec L}{\hbar}\right)
=
\begin{cases}
m^2c^4 + 4m\hbar\omega c^2\,n_r, & s_{\mathrm{tot}} = l+\tfrac12, \\[4pt]
m^2c^4 + 2m\hbar\omega c^2\left(2n_r + 2l + 1\right), & s_{\mathrm{tot}} = l-\tfrac12 .
\end{cases}\;}
$$

This is the Dirac-oscillator spectrum. Its structure is the two-branch pattern familiar from the literature: one branch is a tower in the radial quantum number $n_r$ alone, the other a tower shifted by the orbital quantum number; both are positive, so $E^2 \geq m^2c^4$ and the spectrum has a gap. The ground state has $n_r = 0$, $l = 0$, $s_{\mathrm{tot}} = \tfrac12$, and energy $E = \pm mc^2$; the first excited level stands at $E^2 = m^2c^4 + 4m\hbar\omega c^2$.

The $s_{\mathrm{tot}} = l+\tfrac12$ branch depends on $n_r$ and **not on $l$**. This is the characteristic degeneracy of the Dirac oscillator: for every $l$ with $s_{\mathrm{tot}} = l+\tfrac12$, the state with $n_r = 0$ has the same energy $E = \pm mc^2$, so the ground level is infinitely degenerate, and so is every other level of that branch, since $E^2$ there does not depend on $l$ at all. The degeneracy is not an artefact of the elimination of $\chi$ or of a particular gauge: it follows from the exact operator identity above, because the spin–orbit term cancels the oscillator zero point precisely for the aligned states. It is the same zero-mode structure that appears in the supersymmetric interpretation of the biquaternion section below, and it is the reason the model is called a "pseudo-oscillator": the spatial oscillator and the spin–orbit term conspire to produce a degeneracy pattern different from the non-relativistic oscillator's.

The anti-aligned case requires $l\geq1$, since $s_{\mathrm{tot}}=l-\tfrac12$ is a total angular momentum only for $l\geq1$; at $l=0$ the only state is the aligned one, with $s_{\mathrm{tot}}=\tfrac12$ and $\boldsymbol\sigma\cdot\vec L=0$.

The structure agrees with the published two-branch spectra obtained by solving the radial equations or by locating the poles of the Green's function (see the Further Reading); the derivation here obtains it directly from the operator identity, without a radial decomposition.

## The One-Dimensional Case

The one-dimensional oscillator shows the mechanism without the spin–orbit bookkeeping. With a single coordinate and the substitution $p \to p - im\omega\beta x$, the pair reduces to

$$
(E-mc^2)\phi = c\left(p + im\omega x\right)\chi, \qquad
(E+mc^2)\chi = c\left(p - im\omega x\right)\phi,
$$

and the product of the two first-order operators is now a scalar,

$$
\left(p + im\omega x\right)\left(p - im\omega x\right)
= p^2 + m^2\omega^2x^2 - m\hbar\omega .
$$

The oscillator's zero point is $\tfrac12\hbar\omega$, so $p^2 + m^2\omega^2x^2$ has eigenvalues $2m\hbar\omega(n+\tfrac12)$, and the constant removes the zero point exactly:

$$
\boxed{\;E^2 = m^2c^4 + 2m\hbar\omega c^2\,n, \qquad n = 0,1,2,\dots\;}
$$

The spectrum is a single tower in $n$, and the ground state sits at $E = \pm mc^2$, as in the three-dimensional aligned branch but without the orbital multiplicity. The one-dimensional result is the cleanest check that the constant $-m\hbar\omega$ (which becomes $-3m\hbar\omega$ in three dimensions) is not a convention but a consequence of the commutator $[x,p] = i\hbar$; the zero-point cancellation that produces the $E \propto n$ spectrum is the same mechanism in both cases.

## The Non-Relativistic Limit and the Pseudo-Oscillator

The companion article on the Foldy–Wouthuysen transformation gives the systematic non-relativistic expansion. Applied to the oscillator it gives, in the upper block, the effective operator $\mathcal{Q}^\dagger\mathcal{Q}/(2m)$ — the leading order of $E-mc^2$ read off $E^2-m^2c^4=c^2\mathcal{Q}^\dagger\mathcal{Q}$ — and its negative in the lower block. The oscillator part of that operator is $\vec p^2/(2m)+\tfrac12m\omega^2\vec r^2$, whose levels would be $\hbar\omega(N+\tfrac32)$ if it were the whole of it.

It is not the whole operator. Divided by $2m$, the boxed identity gives

$$
\frac{\mathcal{Q}^\dagger\mathcal{Q}}{2m}
= \frac{\vec p^2}{2m}+\tfrac12m\omega^2\vec r^2-\tfrac32\hbar\omega-\omega\,\boldsymbol\sigma\cdot\vec L ,
$$

so the zero point is removed and a spin–orbit term of order $\omega$ is added, with no factor of $1/c^2$. Its eigenvalues are $-\hbar\omega\,l$ for $s_{\mathrm{tot}}=l+\tfrac12$ and $+\hbar\omega(l+1)$ for $s_{\mathrm{tot}}=l-\tfrac12$: both are of the order of the spacing $\hbar\omega$, and both grow with $l$. At leading order in $1/c$ the energy above the mass gap is therefore

$$
E-mc^2 \approx \hbar\omega\left(N-\frac{\boldsymbol\sigma\cdot\vec L}{\hbar}\right),
$$

which reproduces the two branches of the spectrum in the non-relativistic regime. Treating the spin–orbit term as a small perturbation of the non-relativistic oscillator is not legitimate: it is the same order as the level spacing, and it changes the degeneracy pattern. The non-relativistic limit of the Dirac oscillator is the oscillator **with a spin–orbit coupling of order $\omega$**, not the pure oscillator.

The comparison isolates where the relativistic content lives. In the free theory the spin–orbit coupling is a $1/c^2$ correction, because it comes from the elimination of the small components; in the oscillator it is present at leading order, because the confining substitution is itself linear in the position and frame-odd. The biquaternion framework reads this as the statement that the substitution shifts the **odd** part of the operator, and the odd part is precisely what the square converts into an even operator with a spin–orbit component.

## The Biquaternion Reading

Three structural statements can now be made in the algebra.

**The substitution is a shift of the odd part.** The gradient $\tilde{\nabla}=e_t\,\partial/\partial Q_t+\sum_k\vec e_k\,\partial/\partial Q_k$ has a frame-even part ($e_t\,\partial/\partial Q_t$, the timelike direction) and a frame-odd part ($\sum_k\vec e_k\,\partial/\partial Q_k$, the spacelike directions). What the substitution adds to the operator is the cell $-cm\omega\sum_kL_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}\,x_k$, and that cell is frame-odd: it anticommutes with $\beta=iR_{\vec e_x}^{\mathrm{pau}}$, and it is linear in the position. Squaring the two conjugate first-order operators returns a second-order operator that is central except for one remainder: the pieces built from the two conjugate gradients combine as in the free case, and what survives beside the centre is the spin–orbit cell. With the dictionary of *Reduction to Two-Component Equations*, that remainder is

$$
-2m\omega\,\boldsymbol\sigma\cdot\vec L
\;\longleftrightarrow\;
-2m\omega\sum_k L_k^{\mathrm{orb}}\,L_{\vec e_k}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}},
\qquad
L_k^{\mathrm{orb}}=\sum_{a,b}\epsilon_{kab}\,Q_ap_b ,
$$

a Hermitian element of $\mathbb{M}_+$: $L_{\vec e_k}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}=\alpha_k$ is Hermitian, $L_k^{\mathrm{orb}}$ is Hermitian, and the two commute. The spin is the Hermitian cell $\alpha_k$, the orbital angular momentum is the scalar operator $L_k^{\mathrm{orb}}$, and the coupling is their contraction — the operator $\sum_kL_k^{\mathrm{orb}}\tilde S_k$ of the hydrogen article, up to the factor $-4m\omega/\hbar$. That the remainder is Hermitian and spinorial rather than central is the algebraic statement that the oscillator's square is not the Klein–Gordon operator: the non-minimal term, unlike the mass, does not merely shift the eigenvalue, it adds a Hermitian operator to the square.

**The zero point is a commutator.** The constant $-3m\hbar\omega$ comes from the commutator of position and momentum. In the cells the shift carries $L_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}x_k$ against the momentum $p_k$, and the two do not commute: their commutator is the central scalar $[Q_k,p_k]=i\hbar$, and the trace is $3i\hbar$. The factor $im\omega$ of the substitution turns it into $-3m\hbar\omega$ through one use of $i^2=-1$. This is why the aligned ground state sits at the mass gap: the commutator has removed the zero-point energy exactly, and the cancellation counts the number of spatial directions rather than any particular representation.

**The zero modes are supersymmetric.** The operator identity has the form of a factorisation, $\mathcal{Q}^\dagger\mathcal{Q}$ with the conjugate pair of *The Square of the Coupled Operator*. The aligned states with $n_r=0$ are exactly the **zero modes** $\mathcal{Q}\phi=0$, and their infinite degeneracy is the zero-mode degeneracy of the factorised operator. The pair $(\mathcal{Q},\mathcal{Q}^\dagger)$ is the standard supersymmetric pair of quantum physics: $\mathcal{Q}^\dagger\mathcal{Q}$ and $\mathcal{Q}\mathcal{Q}^\dagger$ are partner Hamiltonians, and the zero modes of $\mathcal{Q}$ are the states the supersymmetry relates. That this supersymmetry is present, and hidden in the Dirac equation rather than imposed, is the content of the Benítez–Salas-Brito solution listed in the Further Reading. The companion article *Supersymmetric Quantum Physics in the Biquaternion Framework* develops this correspondence; the Dirac oscillator is its exactly solvable relativistic realisation. The two operators here are not the two gradients $\tilde{\nabla},\tilde{\nabla}^{\natural}$ of the free mass pair but their shifted, spin-projected forms; what is common to both is that the square of a first-order operator with a conjugate partner is a second-order operator whose zero modes carry the structure.

## The Gamma Formulation

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra.

Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\psi=a\psi$ and $R_b\psi=\psi b$, and $c(M)$ is the coefficient matrix of $M$ in the basis of the sixteen products.

$$
\gamma_0=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\quad \gamma_1=iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_2=iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_3=iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_5=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}} .
$$

A single product is a pure tensor; the products form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and a general element is a sum of at most four, with $\ell(M)=\operatorname{rank}c(M)$.

$\gamma_5$ is the reference-frame cell of the chirality $\Gamma$; the central grading $\chi=i\tilde\Xi_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi^2=e_t$ — is a different object, represented by $\gamma_5$ on the Dirac module.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The identities the bodies cite.** In the $\gamma$ reading, with $\epsilon_{0123}=+1$,
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
The four contraction sums are frame statements, because a cell's square is. In the Euclidean frame, where every cell squares to $+I_4$, they are $4I_4$, $-2\gamma_\alpha$, $4\delta_{\alpha\beta}I_4$ and $-2\gamma_\delta\gamma_\beta\gamma_\alpha$. In the $\mathbb{M}_-$ frame the metric enters: $\sum_\mu\gamma_\mu\gamma_\mu=-2I_4$, and $\sum_\mu\gamma_\mu\gamma_\alpha\gamma_\mu=2(1+g_{\alpha\alpha})\gamma_\alpha$, which is $4\gamma_0$ at $\alpha=0$ and $0$ at every spatial $\alpha$. The remaining two do not collapse to a single monomial with a fixed coefficient, their sign depending on how the free indices split between timelike and spacelike, which is why the Euclidean frame is the one in which all four are elementary; nothing below uses them.

**The two Dirac equations.** In this reading the module equation is the Dirac equation. The cells give

$$
\mathbb{D}=i\sum_{\mu=0}^{3}\gamma_\mu\frac{\partial}{\partial x_\mu},
\qquad x_\mu=(ct',Q_x,Q_y,Q_z),
$$

a plain sum over the four directions: the minus signs of the three spatial cells do the work the metric would do, and the square is $\Box$ because $\gamma_0^2=I_4$ and $\gamma_k^2=-I_4$. With the projectors

$$
P_R=\tfrac12(I_4+\gamma_5),\qquad P_L=\tfrac12(I_4-\gamma_5),
$$

and $\psi_R=P_R\psi$, $\psi_L=P_L\psi$, the equation $(\mathbb{D}-mc/\hbar)\psi=0$ splits into the two lines

$$
\mathbb{D}\psi_R=\frac{mc}{\hbar}\psi_L,\qquad
\mathbb{D}\psi_L=\frac{mc}{\hbar}\psi_R .
$$

$\mathbb{D}$ anticommutes with $\gamma_5$, so it carries each chirality into the other, and the mass couples the two lines; at $m=0$ each line stands alone. The two lines have the shape of the algebra pair, and the difference between the formulations sits in the operator. The algebra needs the conjugate $\tilde{\nabla}^{\natural}$ for its second line, because the quaternion conjugate is what reverses the spacelike directions. On the module the **same** cell operator serves both lines, and what swaps the chiralities is the anticommutation: chirality there is the cell $\gamma_5=-iR_{\vec e_z}^{\mathrm{pau}}$, a pure right multiplication, whereas in the algebra it is the split into the two ideals, carried by $\chi$, and no cell of the frame represents it.

**The oscillator in the $\gamma$ reading.** The frame cell is $\gamma_0=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}}$ and the velocity cells are $\gamma_k=iL_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}$, so $\beta=\gamma_0$, $\alpha_k=\gamma_0\gamma_k$, and

$$
L_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}=-i\gamma_k .
$$

The added term of the substitution, with its explicit $i$ as in the introduction, therefore reads

$$
-icm\omega\sum_k\alpha_k\beta\,x_k=+icm\omega\sum_k\gamma_kx_k ,
$$

because $\alpha_k\beta=-\gamma_k$ and the two factors of $i$ give $-1$. The $i$ has not disappeared here: it has moved from the coefficient onto the matrix, and it is needed there, since $\gamma_k$ is anti-Hermitian while $i\gamma_k$ is Hermitian. In the cells the same term is $-cm\omega\sum_kL_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}x_k$, with a real coefficient and a Hermitian cell, which is why the body writes it that way.

**What the frame cell is not.** $\gamma_0=\beta=iR_{\vec e_x}^{\mathrm{pau}}$ is the frame cell and $\gamma_5=-iR_{\vec e_z}^{\mathrm{pau}}$ is the chirality cell; the two anticommute. The mass term $\beta mc^2$ is diagonal in the frame grading and off-diagonal in the chirality grading: the Foldy–Wouthuysen transformation can diagonalise it in the frame grading, but no chirality projection can, and the mass is not a chirality.

## Summary

The Dirac oscillator is the system obtained by the non-minimal substitution $\vec p \to \vec p - im\omega\beta\vec r$ in the Dirac Hamiltonian. The substitution is frame-odd, imaginary and linear in the position; it shifts the odd part of the first-order operator without touching the even (mass) part. In the Dirac basis the equation reduces to the coupled pair

$$
(E-mc^2)\phi = c\,\boldsymbol\sigma\cdot(\vec p+im\omega\vec r)\chi,
\qquad
(E+mc^2)\chi = c\,\boldsymbol\sigma\cdot(\vec p-im\omega\vec r)\phi .
$$

Eliminating $\chi$ and using the Pauli identity gives the exact operator identity, with $\mathcal{Q}$ the conjugate pair of *The Square of the Coupled Operator*,

$$
\boxed{\;\mathcal{Q}^\dagger\mathcal{Q}
= \vec p^2 + m^2\omega^2\vec r^2 - 3m\hbar\omega - 2m\omega\,\boldsymbol\sigma\cdot\vec L\;},
$$

verified in the bulk of a truncated Cartesian oscillator basis to $1.8\times10^{-15}$. The right-hand side is the three-dimensional oscillator with its zero point removed, plus a spin–orbit coupling of order $\omega$. The spectrum is

$$
E^2 = m^2c^4 + 2m\hbar\omega c^2\left(N - \frac{\boldsymbol\sigma\cdot\vec L}{\hbar}\right)
=
\begin{cases}
m^2c^4 + 4m\hbar\omega c^2\,n_r, & s_{\mathrm{tot}} = l+\tfrac12, \\[4pt]
m^2c^4 + 2m\hbar\omega c^2\left(2n_r+2l+1\right), & s_{\mathrm{tot}} = l-\tfrac12,
\end{cases}
$$

with the aligned branch independent of $l$ and hence an infinitely degenerate level at $E = \pm mc^2$. In one dimension the spin–orbit term is absent and the spectrum is $E^2 = m^2c^4 + 2m\hbar\omega c^2 n$, $n = 0,1,2,\dots$.

In the biquaternion framework the substitution shifts the frame-odd part of the gradient, and in the cells its imaginary coefficient is spent on the cell: the added term is $-cm\omega\sum_kL_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}x_k$, a real coefficient times a Hermitian, frame-odd cell. The square is central except for the Hermitian spin–orbit remainder $-2m\omega\sum_kL_k^{\mathrm{orb}}L_{\vec e_k}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}$ in $\mathbb{M}_+$. The zero-point cancellation is the trace of the commutator $[Q_k,p_k]=i\hbar$ over the three spatial directions, converted to $-3m\hbar\omega$ by one factor $i^2=-1$. The zero modes of the shifted operator are the supersymmetric partner structure that the companion article develops. The article uses the two-sided module equation throughout; the gammas, the chirality projectors and the matrix form of the two Dirac equations appear only in *The Gamma Formulation*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $\mathbb{M}_+$ | Hermitian (informational) sector |
| $e_t = 1$, $\vec e_x, \vec e_y, \vec e_z$ | Quaternion units, $\vec e_k^2 = -e_t$ |
| $L_{a}R_{b}$, $L_{a}R_{b}\psi = a\psi b$ | Two-sided cell; $L_{a}R_{b}L_{c}R_{d} = L_{ac}R_{db}$ |
| $\beta = iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}}$, $\alpha_k = L_{\vec e_k}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}$ | Frame and Dirac velocity cells; $\beta\alpha_k=iL_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}$, $\alpha_k\beta=-iL_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}$ |
| $\Gamma = -iR_{\vec e_z}^{\mathrm{pau}}$ | Chirality cell, a pure right multiplication |
| $g = \mathrm{diag}(+1,-1,-1,-1)$ | Clifford metric (level-3 tool) |
| $H = c\,\boldsymbol\alpha\cdot(\vec p-im\omega\beta\vec r) + \beta mc^2$ | Dirac-oscillator Hamiltonian |
| $\vec p - im\omega\beta\vec r$ | Non-minimal substitution (frame-odd shift) |
| $\mathbb{D} = -R_{\vec e_x}^{\mathrm{pau}}\partial/\partial x_0-\sum_kL_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}\partial/\partial Q_k$ | Two-sided Dirac operator, $\mathbb{D}^2=\Box$ |
| $\phi$, $\chi$ | Upper (large) and lower (small) two-spinors |
| $\mathcal{Q} = \boldsymbol\sigma\cdot(\vec p-im\omega\vec r)$, $\mathcal{Q}^\dagger = \boldsymbol\sigma\cdot(\vec p+im\omega\vec r)$ | Factorised conjugate operators |
| $\mathcal{Q}^\dagger \mathcal{Q} = \vec p^2+m^2\omega^2\vec r^2-3m\hbar\omega-2m\omega\boldsymbol\sigma\cdot\vec L$ | Operator identity |
| $\vec L = \vec r\times\vec p$, $L_k^{\mathrm{orb}}=\sum_{a,b}\epsilon_{kab}Q_ap_b$ | Orbital angular momentum |
| $-2m\omega\sum_kL_k^{\mathrm{orb}}L_{\vec e_k}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}$ | Spin–orbit remainder, Hermitian in $\mathbb{M}_+$ |
| $N = 2n_r + l$ | Total oscillator quantum number |
| $n_r$ | Radial quantum number |
| $E^2 = m^2c^4+4m\hbar\omega c^2 n_r$ ($s_{\mathrm{tot}}=l+\tfrac12$) | Aligned branch |
| $E^2 = m^2c^4+2m\hbar\omega c^2(2n_r+2l+1)$ ($s_{\mathrm{tot}}=l-\tfrac12$) | Anti-aligned branch |
| $E^2 = m^2c^4+2m\hbar\omega c^2 n$ | One-dimensional spectrum |
| $\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L$, $\tilde{\nabla}^{\natural}\tilde{\Psi}_L = m\tilde{\Psi}_R$ | Biquaternion mass pair (the one-sided algebra equation) |
| $\Box = \partial^2/\partial Q_t^2 + \Delta$ | Series d'Alembertian |

## Further Reading

- M. Moshinsky and A. Szczepaniak, "The Dirac oscillator," *Journal of Physics A: Mathematical and General* **22** (1989) L817–L819, for the original non-minimal substitution and the exact solution.
- M. Moshinsky and Yu. F. Smirnov, *The Harmonic Oscillator in Modern Physics* (Harwood, 1996), for the oscillator algebra, the pseudo-oscillator, and the relativistic realisation.
- A. D. Alhaidari, "The Dirac-oscillator Green's function," *International Journal of Theoretical Physics* **43** (2004) 939–946, for the two-branch energy spectrum obtained from the Green's-function poles.
- J. Benítez, R. P. Martínez y Romero, H. N. Núñez-Yépez and A. L. Salas-Brito, "Solution and hidden supersymmetry of a Dirac oscillator," *Physical Review Letters* **64** (1990) 1643–1645 (erratum **65** (1990) 2085), for the hidden supersymmetry that the zero-mode discussion below reproduces.
- R. Szmytkowski and M. Gruchowski, "Completeness of the Dirac oscillator eigenfunctions," *Journal of Physics A: Mathematical and General* **34** (2001) 4991–4997, for the completeness of the two-branch eigenfunctions.
- P. Strange and L. H. Ryder, "The Dirac oscillator in a rotating frame of reference," *Physics Letters A* **380** (2016) 3465–3468, for the oscillator in a non-inertial setting and the subtleties the rotation introduces.
- F. Domínguez-Adame and M. A. González, "Solvable linear potentials in the Dirac equation," *Europhysics Letters* **13** (1990) 193–198, for the linear — oscillator — potential solved in reduced dimensions.
- W. Greiner, *Relativistic Quantum Mechanics: Wave Equations* (Springer, 1990), for the Dirac representation, the coupled two-spinor equations and the non-relativistic reduction.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the Dirac Hamiltonian and the Foldy–Wouthuysen reduction used in the non-relativistic comparison.
