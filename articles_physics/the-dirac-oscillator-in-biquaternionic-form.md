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

The article derives the substitution, the split of a state into its two frame parts and the coupled pair those parts satisfy, the exact operator identity on squaring, and the spectrum; it then works the one-dimensional case for which everything is transparent, takes the non-relativistic limit, reads the result in the algebra, and connects the zero modes to the supersymmetric structure developed in the companion article *Supersymmetric Quantum Physics in the Biquaternion Framework*. Nothing below is written with a matrix, a column or a decomposition of the algebra: a state is an element, an operator is an action on it, and every display of an array is confined to *The Legacy Gamma Formulation*.

**Two Dirac equations.** The corpus carries two, and this article keeps them apart. The **algebra equation** is the one-sided chiral pair

$$
\tilde{\nabla}\tilde{\Psi}_R = m\tilde{\Psi}_L,
\qquad
\tilde{\nabla}^{\natural}\tilde{\Psi}_L = m\tilde{\Psi}_R ,
$$

in which every derivative multiplies on the left and the mass couples the two values of the subscript. The **module equation** is the single two-sided equation $(\mathbb{D}-mc/\hbar)\psi=0$, in which the multipliers stand on both sides and whose two chiral parts are two lines. Chirality is the subscript in both forms of the equation, and it takes two values. In the module equation the large and small parts are not the chiral parts but the two values of the frame action $\beta$: $\beta$ is $+1$ on one part and $-1$ on the other, the mass is diagonal in that label and off-diagonal in the chiral one, and the two labels are different functions of the same state. The oscillator is a problem in the module equation, because the substitution is built from $\beta$ and from the velocity actions, and both are two-sided. The algebra pair is recorded here because its square is the Klein–Gordon operator on which the whole construction rests; the oscillator itself is never posed in it, and apart from the dictionary drawn in *The Legacy Gamma Formulation* it makes no further appearance.

**The subscript.** Chirality is the subscript: an element is $L$ or $R$, and those are the two values. The letters are the Dirac ones, $L$ for left-handed and $R$ for right-handed, in the sense the corpus already uses for $\psi_L$ and $\psi_R$. Every element is a sum of one of each, only the zero element is both, a product takes the letter of its right factor, and left multiplication keeps the letter. The subscript belongs to the element and not to the state: a unit, a product and a general element carry it as well.

**Conventions.** These are the series conventions. The unit is $e_t$, it satisfies $e_tQ=Qe_t=Q$ for every element $Q$, and it is never written as an operator of its own. An action on a state is the two-sided multiplication, written out,
$$
Q\longmapsto a\,Q\,b ,
$$
so that a state is an element of $\mathbb{B}$ and no column is introduced. Two actions compose by substitution, $c\,(aQb)\,d=ca\,Q\,bd$: the left elements compose in reverse and the right elements in order. The four generators of the frame, one per coordinate, are
$$
G_0:\ Q\longmapsto iQ\vec e_x,
\qquad
G_k:\ Q\longmapsto i\vec e_kQ\vec e_y ,
$$
they anticommute pairwise, $G_0^2=\mathrm I$ and $G_k^2=-\mathrm I$, and in one line $\{G_\mu,G_\nu\}=2g_{\mu\nu}$ with $g=\operatorname{diag}(+1,-1,-1,-1)$. The frame action and the velocity actions are
$$
\beta:\ Q\longmapsto iQ\vec e_x,
\qquad
\alpha_k:\ Q\longmapsto \vec e_kQ\vec e_z .
$$

Both $\beta$ and $\alpha_k$ are Hermitian, square to the identity, and satisfy $\{\beta,\alpha_k\}=0$ and $\{\alpha_j,\alpha_k\}=2\delta_{jk}$. **A product of two actions collects a sign from two places:** from the factors of $i$, one per generator, and from the units, which compose in reverse, so that $\vec e_y\vec e_x=-\vec e_z$. The two signs can cancel, and in $\beta$ applied after $G_k$ they do,
$$
G_k\text{ then }\beta:\ Q\longmapsto i\bigl(i\vec e_kQ\vec e_y\bigr)\vec e_x=-\vec e_kQ\,(\vec e_y\vec e_x)=\vec e_kQ\vec e_z=\alpha_k ,
$$
the two factors of $i$ giving $-1$ and the reversed pair of units a second, so that no $i$ survives. The products used below are
$$
\beta\alpha_k:\ Q\longmapsto i\vec e_kQ\vec e_y,\qquad
\alpha_k\beta:\ Q\longmapsto -i\vec e_kQ\vec e_y,\qquad
\beta\alpha_k\beta=-\alpha_k .
$$
The two-sided Dirac operator is the action
$$
\mathbb{D}:\ Q\longmapsto -(\partial_0Q)\vec e_x-\sum_k \vec e_k\,(\partial_kQ)\,\vec e_y,
\qquad x_0=ct',
$$
and its square is the d'Alembertian $\Box=\partial^2/\partial Q_t^2+\Delta$, with $Q_t=ict'$ and $\Delta=\sum_k\partial^2/\partial Q_k^2$: the generator $G_0$ squares to $+1$ and each $G_k$ to $-1$, and the cross terms vanish by the anticommutation.

## The Non-Minimal Substitution

Minimal coupling replaces $\vec p$ by $\vec p - q\vec A$; the added term is a vector potential and enters the Hamiltonian through $\boldsymbol\alpha\cdot\vec A$. The oscillator substitution is different in three ways, and each matters.

**It multiplies the position by $\beta$.** The added term is $-im\omega\beta\vec r$, not $-im\omega\vec r$. Because $\beta$ anticommutes with $\boldsymbol\alpha$, the product $\boldsymbol\alpha\cdot(\beta\vec r)$, which is the action $\alpha_k\beta:Q\mapsto-i\vec e_kQ\vec e_y$ contracted with the position, is frame-**odd**: it lies in the same grading class as the kinetic term $\boldsymbol\alpha\cdot\vec p$, and in the opposite class from the mass $\beta mc^2$. In the algebra this is the statement that the substitution shifts the odd part of the operator while leaving the even part alone, which is why the square is again second order and central except for the spin–orbit term.

**The coefficient is imaginary, and the term is Hermitian.** A gauge interaction adds the real, Hermitian $q\vec A$ to $\vec p$; here the coefficient is $i$. In the actions the imaginary coefficient is spent on the action at once, because $\alpha_k\beta$ is the action $Q\mapsto-i\vec e_kQ\vec e_y$ and the two factors of $i$ multiply to $-1$:

$$
c\,\boldsymbol\alpha\cdot\left(-im\omega\beta\vec r\right)\psi
=-icm\omega\sum_k\alpha_k\beta\,x_k\,\psi
=-cm\omega\sum_k \vec e_k\,(x_k\psi)\,\vec e_y .
$$

The coefficient is now real, and the action $Q\mapsto\vec e_kQ\vec e_y$ is Hermitian: the adjoint of $Q\mapsto aQb$ is $Q\mapsto a^{*}Qb^{*}$, and the units satisfy $\vec e_k^{*}=-\vec e_k$ and $\vec e_y^{*}=-\vec e_y$, so the two sign changes cancel. The added term is therefore Hermitian, and so is $H$. What the imaginary coefficient signals is not a complex deformation — the spectrum below is real — but a term that is frame-odd, linear in the position and biquaternion-valued, which a gauge potential cannot produce.

**It is linear in the position**, so it grows without bound. The oscillator potential is confining, the spectrum is discrete, and the model is a relativistic confinement model rather than a scattering problem. This is the physical reason for its use in quark-confinement phenomenology, and the reason the spectrum consists of bound levels with the mass gap at their base.

Applying $\beta/(\hbar c)$ to both sides of the time-dependent equation $H\psi=i\hbar\,\partial \psi/\partial t$ — so that every term is divided by $\hbar$ and the right-hand side becomes $i\beta\,\partial \psi/\partial x_0$ — two collapses do the work. The kinetic term becomes the action $Q\mapsto\sum_k\vec e_k(\partial_kQ)\vec e_y$, because the $i$ of the action, the $i$ of $p_k=-i\hbar\partial/\partial Q_k$ and the $1/\hbar$ multiply to $+1$, and that term is $-\mathbb{D}+i\beta\,\partial/\partial x_0$: its second piece cancels the right-hand side, so the **time** derivative drops out and the spatial part survives as $-\mathbb{D}$. The frame action passing through the substitution changes its sign, $\beta\alpha_k\beta=-\alpha_k$, so $-im\omega\beta\vec r$ becomes $+im\omega\alpha_kQ_k$, and the mass term becomes $mc/\hbar$. What remains is

$$
\left(\mathbb{D} - \frac{mc}{\hbar}\right)\psi = i\,\frac{m\omega}{\hbar}\left(\sum_k \vec e_k\,Q_k\,\psi\,\vec e_z\right) .
$$

The right-hand side is a spacelike action, linear in the position: the non-minimal term is a position-dependent generator of the odd part, and the action $\alpha_k$ that carries it is Hermitian. This is the form in which the biquaternion interpretation is made below.

## The Frame Split and the Coupled Pair

A state is an element $\psi$ of $\mathbb{B}$. The frame action $\beta$ takes the two values $+1$ and $-1$, so every state splits in exactly one way,

$$
\psi=\psi_+ + \psi_-,
\qquad
\psi_+=\tfrac12\bigl(\psi+i\psi\vec e_x\bigr),
\qquad
\psi_-=\tfrac12\bigl(\psi-i\psi\vec e_x\bigr),
\qquad
\beta\psi_+=\psi_+,\quad \beta\psi_-=-\psi_- .
$$

The split is read on the element and not chosen in a basis: $\psi_+$ is the part with $\beta=+1$ and $\psi_-$ the part with $\beta=-1$. Since $\beta$ anticommutes with every $\alpha_k$, each velocity action carries $\psi_+$ into the part with $\beta=-1$ and $\psi_-$ into the part with $\beta=+1$; that is why the pair below is coupled, and why no first-order equation survives for one part alone when $m\ne0$.

Writing $H\psi=E\psi$ with the Hamiltonian of the introduction and separating the two parts gives the coupled pair

$$
(E-mc^2)\psi_+ = c\sum_k\alpha_k\,\bigl(p_k+im\omega Q_k\bigr)\psi_- ,
\qquad
(E+mc^2)\psi_- = c\sum_k\alpha_k\,\bigl(p_k-im\omega Q_k\bigr)\psi_+ ,
$$

in which each $\alpha_k$ acts on the element written after it. The two signs are the two values of $\beta$: the added term $-im\omega\beta\vec r$ is $+im\omega\vec r$ on the part with $\beta=-1$ and $-im\omega\vec r$ on the part with $\beta=+1$. The pair is the shape in which the oscillator is normally solved: the two frame parts are coupled by the two conjugate first-order actions, and the coupling has the shape of a minimal coupling with $\pm im\omega\vec r$ in place of $\vec A$. Eliminating $\psi_-$,

$$
\psi_- = \frac{c}{E+mc^2}\sum_k\alpha_k\,\bigl(p_k-im\omega Q_k\bigr)\psi_+ ,
$$

and substituting into the first line gives the second-order equation for the large part alone:

$$
\left(E^2 - m^2c^4\right)\psi_+
= c^2\,\mathcal{Q}_+\mathcal{Q}_-\,\psi_+ ,
\qquad
\mathcal{Q}_\pm:\ Q\longmapsto\sum_k \vec e_k\,\bigl(p_k\pm im\omega Q_k\bigr)Q\,\vec e_z .
$$

The two first-order actions are conjugate to one another and are built from the same three velocity actions; their product is what the next section evaluates. Everything now rests on that product.

## The Square of the Coupled Operator

The product is computed from two facts and from no matrix identity: the three velocity actions anticommute, and $[Q_k,p_k]=i\hbar$.

**The diagonal part.** The terms with equal indices are scalar operators, and their sum is

$$
\sum_k\bigl(p_k+im\omega Q_k\bigr)\bigl(p_k-im\omega Q_k\bigr)
= \vec p^{\,2} + m^2\omega^2\vec r^{\,2} + im\omega\sum_k\bigl[Q_k,p_k\bigr]
= \vec p^{\,2} + m^2\omega^2\vec r^{\,2} - 3m\hbar\omega ,
$$

because $[Q_k,p_k]=i\hbar$ in each of the three spatial directions, the sum of the three gives $3i\hbar$, and $im\omega\,(3i\hbar)=-3m\hbar\omega$ through one more use of $i^2=-1$.

**The cross part.** A term with $j\ne k$ is $\alpha_j\alpha_k$ times a scalar operator. The two actions anticommute, so only the antisymmetric part of the coefficient survives, and it is

$$
\bigl(p_j+im\omega Q_j\bigr)\bigl(p_k-im\omega Q_k\bigr)-\bigl(p_k+im\omega Q_k\bigr)\bigl(p_j-im\omega Q_j\bigr)
= 2im\omega\bigl(Q_jp_k-Q_kp_j\bigr) = 2im\omega\,L_l^{\mathrm{orb}}
$$

on the cyclic index $l$. The composition of two velocity actions is a left multiplication by a unit,

$$
\alpha_x\alpha_y:\ Q\longmapsto-\vec e_zQ,
\qquad
\alpha_y\alpha_z:\ Q\longmapsto-\vec e_xQ,
\qquad
\alpha_z\alpha_x:\ Q\longmapsto-\vec e_yQ ,
$$

so the whole cross part is one action: the coefficient $2im\omega L_l^{\mathrm{orb}}$, the minus of the left multiplication and the unit give

$$
Q\longmapsto -2m\omega\sum_k L_k^{\mathrm{orb}}\,i\vec e_kQ .
$$

Adding the two parts, the operator identity is

$$
\boxed{\;\mathcal{Q}_+\mathcal{Q}_-
= \vec p^{\,2} + m^2\omega^2\vec r^{\,2} - 3m\hbar\omega - 2m\omega\sum_k L_k^{\mathrm{orb}}\,i\vec e_k\;}
$$

where the last term is the left multiplication by $i\vec e_k$ with the scalar $L_k^{\mathrm{orb}}$ in front of it, and the second-order equation of the last section reads $(E^2-m^2c^4)\psi_+=c^2\mathcal{Q}_+\mathcal{Q}_-\psi_+$.

This is the load-bearing equation of the article. It was checked by exact differentiation on generic polynomial states of total degree at most two, with random complex coefficients: both sides were evaluated on the same state and the residual was zero, not merely small, because the differentiation of a polynomial is exact and no truncation enters. The commutator $[Q_k,p_k]=i\hbar$, which a truncated basis realises only in its bulk, is here an identity at every order, and it is the only place where $\hbar$ enters the square.

The right-hand side separates into three pieces. The first two terms are the **three-dimensional isotropic oscillator** in operator form,

$$
\vec p^{\,2} + m^2\omega^2\vec r^{\,2} = 2m\left(\frac{\vec p^{\,2}}{2m} + \tfrac12 m\omega^2\vec r^{\,2}\right) = 2m\,H_{\mathrm{osc}},
$$

with the standard spectrum $\hbar\omega(N+\tfrac32)$ in terms of the total oscillator number $N = 2n_r + l$. The constant $-3m\hbar\omega$ then removes exactly the zero-point energy of the oscillator, leaving $2m\hbar\omega N$. The last term is a **spin–orbit coupling** whose strength is tied to the oscillator frequency; it is not a small correction but a term of the same order as the level spacing, and it governs the whole spectral structure.

**Two values, and two only.** Write $S=\sum_k L_k^{\mathrm{orb}}\,i\vec e_k$ for the last term without its coefficient. Since $(i\vec e_k)^2=e_t$ and $i\vec e_j$ anticommutes with $i\vec e_k$ for $j\ne k$, and since $(i\vec e_j)(i\vec e_k)=i\epsilon_{jkl}\,i\vec e_l$, the square of $S$ is

$$
S^2=\sum_k\bigl(L_k^{\mathrm{orb}}\bigr)^2+\sum_{j<k}\bigl[L_j^{\mathrm{orb}},L_k^{\mathrm{orb}}\bigr]\,(i\vec e_j)(i\vec e_k)
= \vec L^{\,2}-\hbar S ,
$$

where $[L_j^{\mathrm{orb}},L_k^{\mathrm{orb}}]=i\hbar\epsilon_{jkl}L_l^{\mathrm{orb}}$. On a state of orbital number $l$ the operator $S$ therefore takes the two values $\hbar l$ and $-\hbar(l+1)$, the two roots of $\lambda^2=\hbar^2l(l+1)-\hbar\lambda$, and nothing else. The spin–orbit coupling is a two-valued operator, and that is the whole of its spectrum.

## The Spectrum

Insert the boxed identity into the second-order equation:

$$
\left(E^2 - m^2c^4\right)\psi_+
= c^2\left(\vec p^{\,2} + m^2\omega^2\vec r^{\,2} - 3m\hbar\omega - 2m\omega\,S\right)\psi_+ .
$$

The first three terms are scalars in the position and in the orbital variables, while $S$ is diagonal in the basis of states of definite oscillator number $N$, definite $l$ and definite total angular momentum, and takes the two values above. The total angular momentum is the Hermitian element

$$
\tilde S_{\mathrm{tot},k}=L_k^{\mathrm{orb}}e_t+\tilde S_k,
\qquad
\tilde S_k=\tfrac{\hbar}{2}i\vec e_k ,
$$

acting by left multiplication, and the contraction obeys $\sum_k(L_k^{\mathrm{orb}}e_t)\tilde S_k=\tfrac12(\tilde S_{\mathrm{tot}}^2-\vec L^{\,2}-\tfrac34\hbar^2e_t)$, so the two values of $S$ are read from the Casimir alone: $+\hbar l$ for $s_{\mathrm{tot}}=l+\tfrac12$ and $-\hbar(l+1)$ for $s_{\mathrm{tot}}=l-\tfrac12$. With $\vec p^{\,2} + m^2\omega^2\vec r^{\,2} - 3m\hbar\omega = 2m\hbar\omega N$ and $N = 2n_r + l$, and writing $\mathcal{S}=S/\hbar$ for the dimensionless value,

$$
\boxed{\;E^2 = m^2c^4 + 2m\hbar\omega c^2\left(N - \mathcal{S}\right)
=
\begin{cases}
m^2c^4 + 4m\hbar\omega c^2\,n_r, & s_{\mathrm{tot}} = l+\tfrac12, \\[4pt]
m^2c^4 + 2m\hbar\omega c^2\left(2n_r + 2l + 1\right), & s_{\mathrm{tot}} = l-\tfrac12 .
\end{cases}\;}
$$

This is the Dirac-oscillator spectrum. Its structure is the two-branch pattern familiar from the literature: one branch is a tower in the radial quantum number $n_r$ alone, the other a tower shifted by the orbital quantum number; both are positive, so $E^2 \geq m^2c^4$ and the spectrum has a gap. The ground state has $n_r = 0$, $l = 0$, $s_{\mathrm{tot}} = \tfrac12$, and energy $E = \pm mc^2$; the first excited level stands at $E^2 = m^2c^4 + 4m\hbar\omega c^2$.

The formula was also checked by direct diagonalisation of $H$ in a truncated oscillator basis, with $m=\hbar=\omega=c=1$ and the truncation $n_x+n_y+n_z\leq8$: the distinct values of $E^2$ that come out are $1$, $5$, $7$, $9$, $11$, $13$, $15$, $17$, $19$, $23$, $27$, $31$, $35$, which is the aligned tower $1+4n_r$ together with the anti-aligned tower $1+2(2l+1)$, the values $21$ and $25$ being absent only because the states that carry them need more than eight oscillator quanta. The lowest level $E^2=1$ comes out with the large multiplicity that the aligned branch predicts.

The $s_{\mathrm{tot}} = l+\tfrac12$ branch depends on $n_r$ and **not on $l$**. This is the characteristic degeneracy of the Dirac oscillator: for every $l$ with $s_{\mathrm{tot}} = l+\tfrac12$, the state with $n_r = 0$ has the same energy $E = \pm mc^2$, so the ground level is infinitely degenerate, and so is every other level of that branch, since $E^2$ there does not depend on $l$ at all. The degeneracy is not an artefact of the elimination of $\psi_-$ or of a particular gauge: it follows from the exact operator identity above, because the value $+\hbar l$ of $S$ cancels the orbital content of $N$ precisely for the aligned states. It is the same zero-mode structure that appears in the supersymmetric interpretation of the biquaternion section below, and it is the reason the model is called a "pseudo-oscillator": the spatial oscillator and the spin–orbit term conspire to produce a degeneracy pattern different from the non-relativistic oscillator's.

The anti-aligned case requires $l\geq1$, since $s_{\mathrm{tot}}=l-\tfrac12$ is a total angular momentum only for $l\geq1$; at $l=0$ the only state is the aligned one, with $s_{\mathrm{tot}}=\tfrac12$ and $S=0$.

The structure agrees with the published two-branch spectra obtained by solving the radial equations or by locating the poles of the Green's function (see the Further Reading); the derivation here obtains it directly from the operator identity, without a radial decomposition.

## The One-Dimensional Case

The one-dimensional oscillator shows the mechanism without the spin–orbit bookkeeping. With a single coordinate $Q$, the single velocity action $\alpha:Q\mapsto\vec e_xQ\vec e_z$, and the substitution $p \to p - im\omega\beta Q$, the pair reduces to

$$
(E-mc^2)\psi_+ = c\,\alpha\,\bigl(p + im\omega Q\bigr)\psi_-,
\qquad
(E+mc^2)\psi_- = c\,\alpha\,\bigl(p - im\omega Q\bigr)\psi_+ ,
$$

and the product of the two first-order operators is now a scalar, because $\alpha^2$ is the identity:

$$
\bigl(p + im\omega Q\bigr)\bigl(p - im\omega Q\bigr)
= p^2 + m^2\omega^2Q^2 - m\hbar\omega .
$$

The oscillator's zero point is $\tfrac12\hbar\omega$, so $p^2 + m^2\omega^2Q^2$ has eigenvalues $2m\hbar\omega(n+\tfrac12)$, and the constant removes the zero point exactly:

$$
\boxed{\;E^2 = m^2c^4 + 2m\hbar\omega c^2\,n, \qquad n = 0,1,2,\dots\;}
$$

The spectrum is a single tower in $n$, and the ground state sits at $E = \pm mc^2$, as in the three-dimensional aligned branch but without the orbital multiplicity. The one-dimensional result is the cleanest check that the constant $-m\hbar\omega$ (which becomes $-3m\hbar\omega$ in three dimensions) is not a convention but a consequence of the commutator $[Q,p] = i\hbar$; the zero-point cancellation that produces the $E \propto n$ spectrum is the same mechanism in both cases.

## The Non-Relativistic Limit and the Pseudo-Oscillator

The companion article on the Foldy–Wouthuysen transformation gives the systematic non-relativistic expansion. Applied to the oscillator it gives, on the large part, the effective operator $\mathcal{Q}_+\mathcal{Q}_-/(2m)$ — the leading order of $E-mc^2$ read off $E^2-m^2c^4=c^2\mathcal{Q}_+\mathcal{Q}_-$ — and its negative on the small part. The oscillator part of that operator is $\vec p^{\,2}/(2m)+\tfrac12m\omega^2\vec r^{\,2}$, whose levels would be $\hbar\omega(N+\tfrac32)$ if it were the whole of it.

It is not the whole operator. Divided by $2m$, the boxed identity gives

$$
\frac{\mathcal{Q}_+\mathcal{Q}_-}{2m}
= \frac{\vec p^{\,2}}{2m}+\tfrac12m\omega^2\vec r^{\,2}-\tfrac32\hbar\omega-\omega\,S ,
$$

so the zero point is removed and a spin–orbit term of order $\omega$ is added, with no factor of $1/c^2$. Its two values are $-\hbar\omega\,l$ for $s_{\mathrm{tot}}=l+\tfrac12$ and $+\hbar\omega(l+1)$ for $s_{\mathrm{tot}}=l-\tfrac12$: both are of the order of the spacing $\hbar\omega$, and both grow with $l$. At leading order in $1/c$ the energy above the mass gap is therefore

$$
E-mc^2 \approx \hbar\omega\left(N-\mathcal{S}\right),
$$

which reproduces the two branches of the spectrum in the non-relativistic regime. Treating the spin–orbit term as a small perturbation of the non-relativistic oscillator is not legitimate: it is the same order as the level spacing, and it changes the degeneracy pattern. The non-relativistic limit of the Dirac oscillator is the oscillator **with a spin–orbit coupling of order $\omega$**, not the pure oscillator.

The comparison isolates where the relativistic content lives. In the free theory the spin–orbit coupling is a $1/c^2$ correction, because it comes from the elimination of the small part; in the oscillator it is present at leading order, because the confining substitution is itself linear in the position and frame-odd. The biquaternion framework reads this as the statement that the substitution shifts the **odd** part of the operator, and the odd part is precisely what the square converts into an even operator with a spin–orbit component.

## The Biquaternion Reading

Three structural statements can now be made in the algebra.

**The substitution is a shift of the odd part.** The gradient $\tilde{\nabla}=e_t\,\partial/\partial Q_t+\sum_k\vec e_k\,\partial/\partial Q_k$ has a frame-even part ($e_t\,\partial/\partial Q_t$, the timelike direction) and a frame-odd part ($\sum_k\vec e_k\,\partial/\partial Q_k$, the spacelike directions). What the substitution adds to the operator is the action $Q\mapsto-cm\omega\sum_k\vec e_k(x_kQ)\vec e_y$, and that action is frame-odd: it anticommutes with $\beta$, and it is linear in the position. Squaring the two conjugate first-order actions returns a second-order operator that is central except for one remainder: the pieces built from the two conjugate gradients combine as in the free case, and what survives beside the centre is the spin–orbit part. In the elements it is

$$
-2m\omega\,S=-2m\omega\sum_k L_k^{\mathrm{orb}}\,i\vec e_k
\;\longleftrightarrow\;
-\frac{4m\omega}{\hbar}\sum_k\bigl(L_k^{\mathrm{orb}}e_t\bigr)\tilde S_k ,
\qquad
\tilde S_k=\tfrac{\hbar}{2}i\vec e_k ,
$$

a Hermitian element of $\mathbb{M}_+$: $i\vec e_k$ is Hermitian, $L_k^{\mathrm{orb}}$ is Hermitian, and the two commute. The spin is the Hermitian element $i\vec e_k$, the orbital angular momentum is the scalar operator $L_k^{\mathrm{orb}}$, and the coupling is their contraction, which is the operator $\sum_kL_k^{\mathrm{orb}}\tilde S_k$ of the hydrogen article up to the factor $-4m\omega/\hbar$. That the remainder is Hermitian and not central is the algebraic statement that the oscillator's square is not the Klein–Gordon operator: the non-minimal term, unlike the mass, does not merely shift the eigenvalue, it adds a Hermitian element to the square.

**The zero point is a commutator.** The constant $-3m\hbar\omega$ comes from the commutator of position and momentum. The shift carries $\vec e_k(x_k\psi)\vec e_y$ against the momentum $p_k$, and the two do not commute: their commutator is the central scalar $[Q_k,p_k]=i\hbar$, and the sum over the three directions is $3i\hbar$. The factor $im\omega$ of the substitution turns it into $-3m\hbar\omega$ through one use of $i^2=-1$. This is why the aligned ground state sits at the mass gap: the commutator has removed the zero-point energy exactly, and the cancellation counts the number of spatial directions rather than any particular representation.

**The zero modes are supersymmetric.** The operator identity has the form of a factorisation, $\mathcal{Q}_+\mathcal{Q}_-$ with the conjugate pair of *The Square of the Coupled Operator*. The aligned states with $n_r=0$ are exactly the **zero modes** $\mathcal{Q}_-\psi_+=0$, and their infinite degeneracy is the zero-mode degeneracy of the factorised operator. The pair $(\mathcal{Q}_-,\mathcal{Q}_+)$ is the standard supersymmetric pair of quantum physics: $\mathcal{Q}_+\mathcal{Q}_-$ and $\mathcal{Q}_-\mathcal{Q}_+$ are partner Hamiltonians, and the zero modes of one are the states the supersymmetry relates. That this supersymmetry is present, and hidden in the Dirac equation rather than imposed, is the content of the Benítez–Salas-Brito solution listed in the Further Reading. The companion article *Supersymmetric Quantum Physics in the Biquaternion Framework* develops this correspondence; the Dirac oscillator is its exactly solvable relativistic realisation. The two operators here are not the two gradients $\tilde{\nabla},\tilde{\nabla}^{\natural}$ of the free mass pair but their shifted, spin-projected forms; what is common to both is that the square of a first-order operator with a conjugate partner is a second-order operator whose zero modes carry the structure.

## The Legacy Gamma Formulation

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra.

Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\psi=a\psi$ and $R_b\psi=\psi b$, and $c(M)$ is the coefficient matrix of $M$ in the basis of the sixteen products.

$$
\gamma_0=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\quad \gamma_1=iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_2=iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_3=iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_5=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}} .
$$

The same in the axis-free display:

$$
\gamma_0=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}},\quad \gamma_1=iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_2=iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_3=iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_5=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}} .
$$

A single product is a pure tensor; the products form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and a general element is a sum of at most four, with $\ell(M)=\operatorname{rank}c(M)$.

$\gamma_5$ is the reference-frame cell of the chirality, $-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}$, and $Q_L$ is its $-1$ part in every display; the central grading $\chi=i\tilde\Xi_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi^2=e_t$ — is a different object, represented by $\gamma_5$ on the Dirac module.

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

$\mathbb{D}$ anticommutes with $\gamma_5$, so it carries each chirality into the other, and the mass couples the two lines; at $m=0$ each line stands alone. The two lines have the shape of the algebra pair, and the difference between the formulations sits in the operator. The algebra needs the conjugate $\tilde{\nabla}^{\natural}$ for its second line, because the quaternion conjugate is what reverses the spacelike directions. On the module the **same** cell operator serves both lines, and what swaps the chiralities is the anticommutation: chirality there is the cell $\gamma_5=-iR_{\vec e_z}^{\mathrm{pau}}$, a pure right multiplication, and in the algebra the same chirality is written centrally as the sign $\chi$; the cell and the sign are one operator in two writings, while the split into the two Peirce copies is neither.

**The oscillator in the $\gamma$ reading.** The frame cell is $\gamma_0=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}}$ and the velocity cells are $\gamma_k=iL_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}$, so $\beta=\gamma_0$, $\alpha_k=\gamma_0\gamma_k$, and

$$
L_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}=-i\gamma_k .
$$

In the axis-free display:

$$
L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}=-i\gamma_k .
$$

The added term of the substitution, with its explicit $i$ as in the introduction, therefore reads

$$
-icm\omega\sum_k\alpha_k\beta\,x_k=+icm\omega\sum_k\gamma_kx_k ,
$$

because $\alpha_k\beta=-\gamma_k$ and the two factors of $i$ give $-1$. The $i$ has not disappeared here: it has moved from the coefficient onto the matrix, and it is needed there, since $\gamma_k$ is anti-Hermitian while $i\gamma_k$ is Hermitian. In the cells the same term is $-cm\omega\sum_kL_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}x_k$, with a real coefficient and a Hermitian cell, which is why the body writes it that way.

**What the frame cell is not.** $\gamma_0=\beta=iR_{\vec e_x}^{\mathrm{pau}}$ is the frame cell and $\gamma_5=-iR_{\vec e_z}^{\mathrm{pau}}$ is the chirality cell; the two anticommute. The mass term $\beta mc^2$ is diagonal in the frame grading and off-diagonal in the chirality grading: the Foldy–Wouthuysen transformation can diagonalise it in the frame grading, but no chirality projection can, and the mass is not a chirality.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{e_\mu}^{\mathrm{axf}}=C_{\Pi}L_{e_\mu}^{\mathrm{pau}}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

The Dirac oscillator is the system obtained by the non-minimal substitution $\vec p \to \vec p - im\omega\beta\vec r$ in the Dirac Hamiltonian. The substitution is frame-odd, imaginary and linear in the position; it shifts the odd part of the first-order operator without touching the even (mass) part. A state is an element $\psi$ of $\mathbb{B}$, the frame action $\beta$ splits it uniquely into $\psi_+$ and $\psi_-$, and the equation reduces to the coupled pair

$$
(E-mc^2)\psi_+ = c\sum_k\alpha_k\bigl(p_k+im\omega Q_k\bigr)\psi_-,
\qquad
(E+mc^2)\psi_- = c\sum_k\alpha_k\bigl(p_k-im\omega Q_k\bigr)\psi_+ .
$$

Eliminating $\psi_-$ and using the anticommutation of the velocity actions together with $[Q_k,p_k]=i\hbar$ gives the exact operator identity, with $\mathcal{Q}_\pm$ the conjugate pair of *The Square of the Coupled Operator*,

$$
\boxed{\;\mathcal{Q}_+\mathcal{Q}_-
= \vec p^{\,2} + m^2\omega^2\vec r^{\,2} - 3m\hbar\omega - 2m\omega\sum_k L_k^{\mathrm{orb}}\,i\vec e_k\;}
$$

checked by exact differentiation on generic polynomial states, with zero residual. The right-hand side is the three-dimensional oscillator with its zero point removed, plus a spin–orbit coupling of order $\omega$; the coupling is the element $S=\sum_k L_k^{\mathrm{orb}}i\vec e_k$, which takes the two values $\hbar l$ and $-\hbar(l+1)$ because $S^2=\vec L^{\,2}-\hbar S$. The spectrum is

$$
E^2 = m^2c^4 + 2m\hbar\omega c^2\left(N - \mathcal S\right)
=
\begin{cases}
m^2c^4 + 4m\hbar\omega c^2\,n_r, & s_{\mathrm{tot}} = l+\tfrac12, \\[4pt]
m^2c^4 + 2m\hbar\omega c^2\left(2n_r+2l+1\right), & s_{\mathrm{tot}} = l-\tfrac12,
\end{cases}
$$

with the aligned branch independent of $l$ and hence an infinitely degenerate level at $E = \pm mc^2$. In one dimension the spin–orbit term is absent and the spectrum is $E^2 = m^2c^4 + 2m\hbar\omega c^2 n$, $n = 0,1,2,\dots$.

In the biquaternion framework the substitution shifts the frame-odd part of the gradient, and in the actions its imaginary coefficient is spent on the action: the added term is $Q\mapsto-cm\omega\sum_k\vec e_k(x_kQ)\vec e_y$, a real coefficient times a Hermitian, frame-odd action. The square is central except for the Hermitian remainder $-2m\omega\sum_kL_k^{\mathrm{orb}}i\vec e_k$, which in the elements is $-\frac{4m\omega}{\hbar}\sum_k(L_k^{\mathrm{orb}}e_t)\tilde S_k$. The zero-point cancellation is the trace of the commutator $[Q_k,p_k]=i\hbar$ over the three spatial directions, converted to $-3m\hbar\omega$ by one factor $i^2=-1$. The zero modes of the shifted operator are the supersymmetric partner structure that the companion article develops. The article uses the two-sided module equation throughout; the gammas, the two chiral parts and the arrays of the two Dirac equations appear only in *The Legacy Gamma Formulation*, and no display of the body needs one.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $\mathbb{M}_+$ | Hermitian (informational) sector |
| $e_t = 1$, $\vec e_x, \vec e_y, \vec e_z$ | Quaternion units, $\vec e_k^2 = -e_t$, $\vec e_y\vec e_x = -\vec e_z$ |
| $Q\mapsto aQb$ | Action on a state; the two-sided multiplication, written out |
| $Q\mapsto caQbd$ | Composition: the action $Q\mapsto aQb$ followed by $Q\mapsto cQd$ |
| $G_0:\ Q\mapsto iQ\vec e_x$, $G_k:\ Q\mapsto i\vec e_kQ\vec e_y$ | The four generators of the frame; $\{G_\mu,G_\nu\}=2g_{\mu\nu}$ |
| $\beta:\ Q\mapsto iQ\vec e_x$ | Frame action; $\beta^2=\mathrm I$, the two values $+1$ and $-1$ |
| $\alpha_k:\ Q\mapsto \vec e_kQ\vec e_z$ | Velocity actions; $\alpha_k^2=\mathrm I$, $\{\alpha_j,\alpha_k\}=2\delta_{jk}$, $\{\beta,\alpha_k\}=0$ |
| $\beta\alpha_k:\ Q\mapsto i\vec e_kQ\vec e_y$, $\alpha_k\beta:\ Q\mapsto-i\vec e_kQ\vec e_y$ | The two mixed products; $\beta\alpha_k\beta=-\alpha_k$ |
| $Q_L$, $Q_R$ | Chirality: the two values of the subscript, left-handed and right-handed |
| $g = \mathrm{diag}(+1,-1,-1,-1)$ | Metric read off the squares of the generators |
| $H = c\,\boldsymbol\alpha\cdot(\vec p-im\omega\beta\vec r) + \beta mc^2$ | Dirac-oscillator Hamiltonian |
| $\vec p - im\omega\beta\vec r$ | Non-minimal substitution (frame-odd shift) |
| $\mathbb{D}:\ Q\mapsto-(\partial_0Q)\vec e_x-\sum_k\vec e_k(\partial_kQ)\vec e_y$ | Two-sided Dirac operator, $\mathbb{D}^2=\Box$ |
| $\psi_+$, $\psi_-$ | The two frame parts, $\beta\psi_\pm=\pm\psi_\pm$; large and small |
| $\mathcal{Q}_\pm:\ Q\mapsto\sum_k\vec e_k(p_k\pm im\omega Q_k)Q\vec e_z$ | Factorised conjugate actions |
| $\mathcal{Q}_+\mathcal{Q}_- = \vec p^{\,2}+m^2\omega^2\vec r^{\,2}-3m\hbar\omega-2m\omega S$ | Operator identity |
| $S = \sum_k L_k^{\mathrm{orb}}\,i\vec e_k$ | Spin–orbit element, Hermitian; $S^2=\vec L^{\,2}-\hbar S$ |
| $\tilde S_k = \tfrac{\hbar}{2}i\vec e_k$, $\tilde S_{\mathrm{tot},k}=L_k^{\mathrm{orb}}e_t+\tilde S_k$ | Spin and total angular momentum elements |
| $\mathcal S = S/\hbar$ | Dimensionless value of the spin–orbit element |
| $\vec L = \vec r\times\vec p$, $L_k^{\mathrm{orb}}=\sum_{a,b}\epsilon_{kab}Q_ap_b$ | Orbital angular momentum |
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
