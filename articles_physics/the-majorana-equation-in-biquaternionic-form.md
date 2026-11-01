# __The Majorana Equation in Biquaternionic Form__

## Introduction

The **Majorana equation** is the relativistic wave equation of a fermion that is its own antiparticle, $\psi^{c}=\psi$. Ettore Majorana wrote it in 1937 as a real form of the Dirac equation, and it is the equation of the spin-$\tfrac12$ field whose charge conjugation is a symmetry rather than an exchange. It differs from the Dirac equation in one term and in one consequence: the mass term pairs the field with its conjugate instead of with the other chiral half, and the field therefore carries half the independent components of a Dirac field, no fermion number, and no electromagnetic coupling.

The corpus already owns the pieces around this equation. *The Neutrino and Majorana Fermions in Biquaternionic Form* fixes the three notions — Dirac, Weyl, Majorana — constructs charge conjugation as a conjugate-linear real structure $\mathcal{C}$ on the Dirac module $\Delta=S\oplus\bar S$, verifies that the constraint $\psi^{c}=\psi$ is consistent with the massive equation, computes the bilinears, identifies the coefficient conjugation $\bar{\cdot}$ as the algebra's charge conjugation, and shows that the material/informational split does not supply the reality condition. *Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form* separates the algebra's $\flat$ from the module's $\mathcal{C}$, places the neutral spinors in the $\mathrm{Spin}^c$ structure, and diagnoses the retired equation on its dispersion. *Real Spinors and Reality Conditions on the Biquaternion Algebra with Hermitian Adjoint* settles which spinor types each signature admits and why the normalisation must be stated. *Klein–Gordon from the Dirac Square in Biquaternionic Form* supplies the second-order consequence of a first-order pair.

What no companion article yet does is treat the **equation itself**: the three standard forms under which it is written and the proof that they agree, the two-component Majorana operator and the pair of Weyl operators whose product is the d'Alembertian, the eigenstructure of the charge-conjugation operator with its Majorana and ELKO sectors, and the counting of independent solutions. The present article supplies those, in the conventions of the series, and it defers the module-level reality discussion to the companion articles rather than repeating it.

The presentation is split three ways, as in the companions.

- **Established, and recomputed below.** In the cell frame with $g=\mathrm{diag}(+,-,-,-)$, the charge-conjugation cell $C=T_{e_t,e_x}$ is real, antisymmetric, $C^{T}=-C$ and $C^{2}=-T_{e_t,e_t}$, and $C\,\mathsf C_{\mu}^{T}C^{-1}=-\mathsf C_{\mu}$ for all four $\mu$. The antilinear map $\mathcal{C}\psi=C\bar\psi^{T}=i\psi^{*}$ is a real structure, $\mathcal{C}^{2}=1$, whose central scalar is $K=i$ with $K K^{*}=T_{e_t,e_t}$, and it anticommutes with each generator, $\mathcal{C}(\mathsf C_{\mu}\psi)=-\mathsf C_{\mu}\mathcal{C}\psi$, for all four $\mu$. It commutes with the kinetic operator $\mathbb{D}$. Its eigenspaces for the eigenvalues $\pm1$ are each of **real dimension four** and span the module. Both eigenspaces are on the mass shell, $(\Box-m^{2})\psi=0$; on the $+1$ eigenspace the Majorana equation is the Dirac equation, and on the $-1$ eigenspace it is the Dirac equation with the opposite sign of the mass term. The two-component Weyl operators satisfy $W_{R}W_{L}=\Box$, so the left- and right-handed Weyl operators are the two square roots of the d'Alembertian. In the opposite signature the Clifford algebra $\mathrm{Cl}_{3,1}$ is the real matrix algebra $M_4(\mathbb{R})$, and a representation with **all generators real** exists; that is the real form of the equation.
- **Transcribed, and cited.** The module-level construction of $\mathcal{C}$, the exchange of the chiral halves, the identification of $\bar{\cdot}$ as the charge conjugation, the fixed space of real dimension four, and the vanishing of the vector current are the content of the neutrino article and are used here, not rebuilt.
- **Not supplied.** The functional-analytic content of the two-component square root identity in the continuum, the observability of the neutrino's Majorana nature, the Majorana phases and the lepton-number-violating rates, and any selection principle that would make one fermion Majorana rather than Dirac, are outside the algebra.

The article is organised as follows. The next section states the equation and its three forms and proves the equivalence. A section then treats the charge-conjugation eigenstates and the ELKO companion. A section counts the independent solutions against the Dirac count. A closing section separates what the framework supplies, transcribes, and does not supply.

**Frame.** The coordinate displays are read in the $\mathbb{B}$ frame, with $Q_t=ict'$; the cell displays carry the generator metric $g=\mathrm{diag}(+,-,-,-)$ and are read in the $\mathbb{M}_-$ frame.

$$
\mathsf C_{0}=iT_{e_t,e_x},\qquad
\mathsf C_{k}=iT_{e_k,e_y},\qquad k=1,2,3,
$$

with $L_a\psi=a\psi$, $R_b\psi=\psi b$ and $T_{a,b}=L_aR_b$; with $g=\mathrm{diag}(+,-,-,-)$ the generators satisfy $\{\mathsf C_{\mu},\mathsf C_{\nu}\}=2g_{\mu\nu}T_{e_t,e_t}$. The chirality operator is $\Gamma=\mathsf C_5=-iT_{e_t,e_z}$, which is $-1$ on the left-handed half $S$ and $+1$ on the right-handed half $\bar S$. The Dirac module is $\Delta=S\oplus\bar S$, a Dirac spinor is $\Psi=(\psi_L,\psi_R)^{T}$, and the charge conjugation is $\psi^{c}=C\bar\psi^{T}=i\psi^{*}$. The d'Alembertian is the series convention

$$
\Box=\partial^2/\partial Q_t^2+\Delta=\Delta+ \partial^2/\partial Q_t^2,
$$

so that the relativistic second-order equation reads $(\Box-m^{2})\psi=0$ in natural units, and the mass is measured in inverse-length units where a distinction is needed. The symbols $\sigma_{\mu}=(I_2,-\boldsymbol{\sigma})$ and $\bar\sigma_{\mu}=(I_2,+\boldsymbol{\sigma})$ are the two-component Weyl vectors, lowered with $g=\mathrm{diag}(+,-,-,-)$, and $\epsilon=i\sigma_2$ is the real antisymmetric $2\times2$ matrix, $\epsilon^{T}=-\epsilon$, $\epsilon^{2}=-I_2$, the symplectic form of the spinor module.

## The Equation and Its Three Forms

The Majorana equation is written in three ways, and the reason the three matter is that each displays a different property: the real form displays the reality of the solutions, the charge-conjugate form displays the role of charge conjugation, and the two-component form displays the contact with the Lorentz group. We state all three and prove that they agree.

### The Charge-Conjugate Form

Here and below $\mathbb{D}$ is the pair operator of *Operator and Calculus Conventions*, acting on the module in the chiral basis, with $\mathbb{D}^2=\Box$. The equation is

$$
\boxed{\;\mathbb{D}\,\psi \;=\; m\,\psi^{c},
\qquad
\psi^{c} \;=\; C\,\bar\psi^{T} \;=\; i\psi^{*}\;},
$$

with $\bar\psi=\psi^{\dagger}\mathsf C_{0}$. The charge-conjugation cell, in the cell frame and the mostly-minus signature, is

$$
C\;=\;T_{e_t,e_x}
\;=\;-i\mathsf C_{0},
$$

and it is **real**. The definition is fixed by the requirement that the kinetic term be preserved,

$$
C\,\mathsf C_{\mu}^{T}\,C^{-1}\;=\;-\,\mathsf C_{\mu},
$$

and the cell has the properties that make it a charge conjugation: $C^{T}=-C$, $C^{2}=-T_{e_t,e_t}$, $C^{\dagger}=C^{-1}$. All of these were checked in the cell frame, on all four values of $\mu$ where a $\mu$ appears.

**The antilinear map is the reality condition, not the cell.** Passing the conjugation into the spinor,

$$
\psi^{c} \;=\; K\,\psi^{*},
\qquad
K\;=\;C\,\mathsf C_{0}^{T}\;=\;i\,T_{e_t,e_t},
$$

and the central scalar $K$ satisfies

$$
K\,K^{*}\;=\;T_{e_t,e_t},
\qquad
K\,\mathsf C_{\mu}^{*}\,K^{-1}\;=\;-\,\mathsf C_{\mu}\quad(\mu=0,1,2,3).
$$

The first relation is the statement that $\mathcal{C}:\psi\mapsto K\psi^{*}$ is an **involution**, $\mathcal{C}^{2}=1$, and the second is what makes it commute with the kinetic operator: a generator is one factor of $i$ times a cell with real entries, so its coefficient conjugate is its negative. Because $\mathcal{C}$ is conjugate-linear, commuting with $\mathbb{D}$ is exactly the displayed condition:

$$
\mathcal{C}\!\left(\mathbb{D}\psi\right)
=\;K\,(i\mathsf C_{\mu})^{*}\,\partial/\partial Q_\mu\psi^{*}
=\;\mathbb{D}\!\left(K\psi^{*}\right)
=\;\mathbb{D}\,\mathcal{C}\psi ,
$$

using $K(i\mathsf C_{\mu})^{*}K^{-1}=i\mathsf C_{\mu}$, which is the second relation. This is the same verified identity the neutrino article records, and it is the whole reason the constraint is consistent with the equation: applying $\mathcal{C}$ to $\mathbb{D}\psi=m\psi^{c}$ returns the same equation with $\psi$ and $\psi^{c}$ interchanged, so the deviation $\psi-\psi^{c}$ is preserved by the evolution and a field self-conjugate at one time stays self-conjugate.

**On the fixed space it is the Dirac equation.** If $\psi$ satisfies the Majorana equation and the constraint $\psi^{c}=\psi$, then $\mathbb{D}\psi=m\psi$, which is the massive Dirac equation. Conversely the massive Dirac equation restricted to the fixed space implies the Majorana equation. The two equations are therefore the same equation on the Majorana sector and different equations off it; the content is the consistency of the constraint, which is a computation and was performed above.

### The Real Form

A spinor is **real** when it equals its own conjugate, and the reason the equation can be written in a form in which that reality is visible is the reality type of the Clifford algebra.

**The real representation exists in the opposite signature.** The two real Clifford algebras of four dimensions are not isomorphic over $\mathbb{R}$: the corpus's mostly-minus algebra is the quaternionic matrix algebra $\mathrm{Cl}_{1,3}\cong M_2(\mathbb{H})$, and the mostly-plus algebra is the real matrix algebra $\mathrm{Cl}_{3,1}\cong M_4(\mathbb{R})$. In the mostly-plus signature the generators can be taken **purely real**: every cell has real entries in the cell frame, and four of them carry the opposite metric, with $\mathring\eta=\mathrm{diag}(-1,+1,+1,+1)$:

$$
r_{0}=-T_{e_x,e_t},\qquad
r_{1}=-T_{e_z,e_y},\qquad
r_{2}=T_{e_z,e_x},\qquad
r_{3}=-T_{e_z,e_z}.
$$

Each cell is real; $r_{0}$ is antisymmetric with $(r_{0})^{2}=-T_{e_t,e_t}$ and $r_{1},r_{2},r_{3}$ are symmetric with $(r_{k})^{2}=+T_{e_t,e_t}$; and the four anticommute in pairs, so that $\{r_{\mu},r_{\nu}\}=2\mathring\eta_{\mu\nu}T_{e_t,e_t}$. In this representation the Dirac operator $i\sum_\mu r_\mu\partial/\partial Q_\mu$ has real matrix coefficients, its massless part preserves the real subspace of real four-component spinors, and a solution of the massless equation can be chosen **purely real**; with a real mass term through the charge conjugation the massive solutions are the Majorana spinors. This is the sense in which the Majorana equation is "the Dirac equation written so that it has purely real solutions", the first of the three standard forms.

**Why the corpus's signature does not have it, and what replaces it.** In the mostly-minus signature the algebra is quaternionic and no representation with all generators real exists; that is the algebraic reason the corpus works with a complex Dirac module and an antilinear real structure $\mathcal{C}$ rather than with real spinors. The two pictures are the two normalisations of one structure, exchanged by the volume element, and the companion *Real Spinors and Reality Conditions* records that the roles of the two signs are exchanged in the two conventions. A reader comparing a "real" Majorana spinor in one signature with a "self-conjugate" Majorana spinor in the other is comparing the two normalisations, and the comparison must state which is in force. The framework's own carrier of the reality is the antilinear $\mathcal{C}$ of the previous subsection.

### The Two-Component Form

The third form acts on a complex two-component spinor and is the form in contact with the Lorentz group. With the Weyl vectors $\sigma_{\mu}=(I_2,-\boldsymbol{\sigma})$ and $\bar\sigma_{\mu}=(I_2,+\boldsymbol{\sigma})$, the **Majorana operator** is the Weyl operator together with an antilinear mass term,

$$
D_L \;=\; i\sum_\mu\bar\sigma_{\mu}\partial/\partial Q_\mu \;-\; m\,\epsilon\,(\,\cdot\,)^{*},
$$

acting on a left-handed Weyl spinor $\psi_L\in S$, so that the two-component Majorana equation is

$$
i\sum_\mu\bar\sigma_{\mu}\partial/\partial Q_\mu\,\psi_L \;=\; m\,\epsilon\,\psi_L^{*}.
$$

The mass term is exactly the conjugation $\mathcal{C}$ written in two-component language: $\epsilon\,\psi_L^{*}$ is the right-handed conjugate that the four-component $\psi^{c}$ produces in its lower half, and the equation pairs the field with that conjugate rather than with an independent right-handed field. The matrix $\epsilon$ is the antisymmetric form that defines the symplectic pairing of *The Spinor Module in Biquaternionic Form and Its Lorentz Action*; the two-component form is therefore not a different equation but the same equation in the defining representation.

**The two Weyl operators are the two square roots of the d'Alembertian.** Set

$$
W_L=i\sum_\mu\bar\sigma_{\mu}\partial/\partial Q_\mu,
\qquad
W_R=i\sum_\mu\sigma_{\mu}\partial/\partial Q_\mu .
$$

Then

$$
\boxed{\;\sigma_{\mu}\bar\sigma_{\nu}+\sigma_{\nu}\bar\sigma_{\mu}=2\eta_{\mu\nu}I_2
\qquad\Longrightarrow\qquad
W_RW_L \;=\; -\,\sum_{\mu,\nu}\sigma_{\mu}\bar\sigma_{\nu}\partial^2/\partial Q_\mu\partial Q_\nu \;=\; -\,\sum_{\mu,\nu}\eta_{\mu\nu}\partial^2/\partial Q_\mu\partial Q_\nu\,I_2 \;=\;\Box\,I_2\;}.
$$

The anticommutator identity was checked for all sixteen pairs $(\mu,\nu)$, and it is the two-component statement of the Clifford relation: the d'Alembertian is the **product** of the two Weyl operators, not the square of either alone. This is why the first-order two-component operators are called square roots of the Klein–Gordon operator, and it is the two-component counterpart of the matrix square used in *Klein–Gordon from the Dirac Square in Biquaternionic Form* for the four-component case. The mass term supplies the $-m^{2}$, so that the second-order equation of the self-conjugate field is the massive Klein–Gordon equation $(\Box-m^{2})\psi=0$, exactly as in the four-component case verified below.

## The Charge-Conjugation Eigenstates and the ELKO Companion

The charge-conjugation operator is an involution on an eight-real-dimensional space, so it has two eigenvalues and the module splits into two real forms. The split is worth computing, because one half is the Majorana sector and the other half is a different and often-missed object.

**The spectrum is $\{+1,-1\}$.** Since $\mathcal{C}^{2}=1$ and $\mathcal{C}$ is conjugate-linear with the central scalar $K=i$, both eigenvalues occur and the eigenspaces are the kernels of $K\psi^{*}=\pm\psi$. Solving the two linear systems in the eight real variables $(\mathrm{Re}\,\psi,\mathrm{Im}\,\psi)$ gives

$$
\boxed{\;\dim_{\mathbb{R}}\{\psi:\psi^{c}=+\psi\}=4,
\qquad
\dim_{\mathbb{R}}\{\psi:\psi^{c}=-\psi\}=4\;},
$$

and the two eigenspaces together span $\Delta$. Both are four-real-dimensional, and the count is immediate from the condition: writing $\psi=a+ib$ with $a,b\in\mathbb{R}^{4}$, the equation $\psi=\pm i\psi^{*}$ forces $a=\pm b$, so each eigenspace is $\{(1\pm i)a\}$ and carries four real parameters. Multiplication by $i$ carries one eigenspace onto the other.

**The $+1$ eigenspace is the Majorana sector.** The condition $K\psi^{*}=+\psi$ is $\psi=i\psi^{*}$, a single relation between the two halves rather than two independent real conditions. Since $\mathcal{C}$ anticommutes with $\Gamma$, it carries $S$ to $\bar S$ and back, so the projection of the fixed space onto either half is an isomorphism; the fixed space is therefore parametrised by $\psi_L$ alone and has real dimension four. This is the Majorana condition of the neutrino article, and on this space the Majorana equation is the Dirac equation, as shown above. The bilinears of this sector — no vector current, a permitted scalar mass, a permitted axial current — are the Grassmann-level statements the neutrino article computes, and they are not re-derived here.

**The $-1$ eigenspace is the ELKO companion.** The condition $K\psi^{*}=-\psi$ is $\psi=-i\psi^{*}$, the same relation with the opposite sign, and it too is consistent and four-real-dimensional. A spinor of this sector satisfies the **sign-flipped** equation

$$
\mathbb{D}\,\psi \;=\; -\,m\,\psi ,
$$

which is the Dirac equation with the wrong sign on the mass term. It is therefore **not** a solution of the Dirac equation for $m\neq0$, and it is the spinor called ELKO in the literature — the "eigenspinor of the charge-conjugation operator" of Lounesto's class 5. Its defining feature is exactly that charge conjugation returns minus the spinor, so the coupling to the central phase is obstructed even more strongly than for the Majorana sector: the antilinear article records that Majorana and ELKO spinors are both **neutral** for this reason, while the Dirac spinor carries the phase.

**Both sectors are on the same mass shell.** This follows from the algebra alone and needs no matrix square. The dynamics is the chiral pair $\tilde{\nabla}\tilde{\Psi}_R=m\tilde{\Psi}_L$, $\tilde{\nabla}^{\natural}\tilde{\Psi}_L=m\tilde{\Psi}_R$; applying $\tilde{\nabla}^{\natural}$ to the first member and using the second gives $\Box\tilde{\Psi}_R=m^2\tilde{\Psi}_R$, and symmetrically for the left half. In the spinor-module language, let $\psi$ solve $\mathbb{D}\psi=m\psi^{c}$; applying the kinetic operator again and using that $\mathcal{C}$ commutes with it and is an involution gives

$$
(\mathbb{D})^{2}\psi
=\;m\,\mathbb{D}\,\psi^{c}
=\;m\,\mathcal{C}\!\left(\mathbb{D}\psi\right)
=\;m\,\mathcal{C}\!\left(m\psi^{c}\right)
=\;m^{2}\psi .
$$

The chain returns the eigenvalue $m^{2}$. The mass-shell equation itself is the algebra's: applying $\tilde{\nabla}^{\natural}$ to the first member of the pair and using the second gives $\Box\tilde{\Psi}_R=m^{2}\tilde{\Psi}_R$, and likewise for $\tilde{\Psi}_L$. The module chain above is the component check of that eigenvalue.

Every solution of the Majorana equation, in either eigenspace, obeys the massive Klein–Gordon equation in this sense; the ELKO companion is on the mass shell even though it is not a Dirac solution. The two sectors differ in the first-order equation, not in the dispersion, and this is the precise sense in which ELKO "solves Klein–Gordon but not Dirac".

**What the split does and does not say.** The two eigenspaces are the two real forms of the Dirac module under the same involution, and the four-component Majorana spinor is the $+1$ one. What the split does **not** provide is a mass term for the ELKO sector: the sign-flipped equation has the mass with the opposite sign, and no rewriting of the algebra turns the $+1$ Majorana equation into the $-1$ one without changing the sign of $m$. Whether the ELKO sector is realised in nature is an open empirical question, and no claim is made here.

## Solutions and the Counting of States

The counting is the sharpest difference between the Majorana and Dirac equations, and it is a statement about the field rather than about a single plane wave.

**A single plane wave is not self-conjugate.** For a plane wave $\psi=u\,\exp(-ip\cdot x)$ one has $\psi^{c}=u^{c}\exp(+ip\cdot x)$, so the condition $\psi^{c}=\psi$ for all $x$ forces $p=0$ and, at rest in the block basis, the only solution of the combined system is $u=0$. The self-conjugate object is not a single mode but the **field**

$$
\psi(x)\;=\;u\,\exp(-ip\cdot x)\;+\;u^{c}\,\exp(+ip\cdot x),
\qquad
(\mathsf C_{\mu}p_{\mu}-m)u=0 ,
$$

which satisfies $\psi^{c}=\psi$ and the Dirac equation when $u$ does. This is the standard construction, and it is the resolution of the apparent conflict between "the Majorana spinor is its own conjugate" and "a plane wave is not its own conjugate": the condition is on the field, and the field pairs each positive-frequency mode with the negative-frequency conjugate of the same mode.

**Two independent components, against the Dirac four.** Because the fixed space is parametrised by $\psi_L$ alone, a Majorana field has the two complex components of one Weyl spinor, that is four real components, against the eight real components of a Dirac field. The doubling of the Dirac degrees of freedom is exactly the carrying of a conserved fermion number: the Dirac field has independent particle and antiparticle halves, the Majorana field has one. The companion article on the seesaw uses this counting, and the statement that two Majorana fields of equal mass reassemble into one Dirac field is the same count in reverse.

**Bilinears, at the level of the field.** The count and the neutrality are reflected in the bilinears: for the anticommuting Majorana field the vector current vanishes and the scalar and axial bilinears survive, so the field can carry a mass but no fermion number. The neutrino article computes this table and records the trap that a commuting c-number spinor obeying the same algebraic condition gives the **opposite** pattern, because the antisymmetry of the Grassmann components is what makes the scalar bilinear add rather than cancel. Nothing in the present article changes that; the eigenstructure above is classical and the bilinear physics is quantum, and they must not be mixed.

## What the Algebra Supplies, Transcribes, and Does Not Supply

| Item | Status |
|---|---|
| The charge-conjugation cell $C=T_{e_t,e_x}$: real, $C^{T}=-C$, $C^{2}=-T_{e_t,e_t}$, $C\mathsf C_{\mu}^{T}C^{-1}=-\mathsf C_{\mu}$ | **Supplied**, recomputed in the cell frame on all $\mu$ |
| The antilinear real structure $\mathcal{C}\psi=K\psi^{*}$: $K=i$, $KK^{*}=T_{e_t,e_t}$, $\mathcal{C}^{2}=1$, $K\mathsf C_{\mu}^{*}K^{-1}=-\mathsf C_{\mu}$ | **Supplied**, recomputed on all $\mu$ |
| $\mathcal{C}$ commutes with the kinetic operator, so the constraint is consistent with the massive equation | **Supplied** (through $K\mathsf C_{\mu}^{*}K^{-1}=-\mathsf C_{\mu}$) |
| The spectral split into two real four-dimensional eigenspaces, Majorana and ELKO | **Supplied**, recomputed by elimination |
| Both eigenspaces on the mass shell, $(\Box-m^{2})\psi=0$ | **Supplied** (from the involution and the Clifford square) |
| The two-component Weyl operators with $W_RW_L=\Box$ | **Supplied**, recomputed on all sixteen pairs |
| A real representation of $\mathrm{Cl}_{3,1}$, and hence purely real solutions in the opposite signature | **Supplied**, recomputed cell by cell |
| The module-level construction of $\mathcal{C}$, the exchange of chiral halves, the identification of $\bar{\cdot}$, the fixed space, the bilinears | **Transcribed** from *The Neutrino and Majorana Fermions in Biquaternionic Form* |
| The two normalisations and the reality types by signature | **Transcribed** from *Real Spinors and Reality Conditions* |
| The neutral spinors and the $\mathrm{Spin}^c$ structure | **Transcribed** from *Antilinear Structure and the Two Kinds of Mass* |
| A selection principle making a fermion Majorana rather than Dirac | **Not supplied**; the choice is empirical |
| The neutrino mass, the Majorana phases, lepton-number-violating rates | **Outside** the algebra |
| Whether the ELKO sector is realised | **Not decided** |

## Open Questions

1. **The algebra-level form of the two-component mass term.** The four-component equation is transcribeable into the algebra through the coefficient conjugation $\bar{\cdot}$, as the neutrino article shows. Whether the two-component mass term $m\epsilon(\,\cdot\,)^{*}$ has a representation as a biquaternion-valued operation on the module, in the way the Dirac mass is the linear chiral pair, is not settled here.

2. **The status of the ELKO sector.** The $-1$ eigenspace is a genuine real form of the module and is on the mass shell, but it is not a Dirac solution and its mass term has the opposite sign. Whether it is a physical sector, a spurion, or an artefact of writing the involution in a basis with both signs, is open.

3. **The normalisation of the real form.** The real representation of $\mathrm{Cl}_{3,1}$ given above is one of several; whether the framework should fix a canonical representative, in the way it fixes the block basis for the complex case, is an authorial decision that belongs with the conventions.

4. **The continuum square root.** The identity $W_RW_L=\Box$ is an operator identity on differentiable fields. Whether the two-component Majorana operator, as an unbounded operator on a Hilbert space, admits the corresponding self-adjoint square-root theory in the sense of the companion articles on semigroups and evolution equations, is not treated here.

5. **Empirical contact.** The decisive experiment is neutrinoless double beta decay, and the framework offers no rate and no prediction. Whether the eigenstructure above can be brought into contact with a rate is open, and is recorded in the neutrino article as an open question of the corpus.

## Summary

The Majorana equation is the relativistic wave equation of a spin-$\tfrac12$ field equal to its own charge conjugate, and it is the Dirac equation with the mass term pairing the field with its conjugate instead of with the other chiral half. In the cell frame with $g=\mathrm{diag}(+,-,-,-)$ its three standard forms were written and shown to agree. The charge-conjugate form uses the real cell $C=T_{e_t,e_x}$, for which $C^{T}=-C$, $C^{2}=-T_{e_t,e_t}$, $C\mathsf C_{\mu}^{T}C^{-1}=-\mathsf C_{\mu}$ on all $\mu$, and the antilinear map $\mathcal{C}\psi=K\psi^{*}$ with the central scalar $K=C\mathsf C_{0}^{T}=i$ satisfies $KK^{*}=1$ and $K\mathsf C_{\mu}^{*}K^{-1}=-\mathsf C_{\mu}$; this is the real structure, and it commutes with the kinetic operator, which is what makes the constraint $\psi^{c}=\psi$ consistent with the massive equation and reduces it to the Dirac equation on the fixed space. The real form uses the real representation of $\mathrm{Cl}_{3,1}\cong M_4(\mathbb{R})$, which was exhibited as four real cells with all generators real and purely real solutions; the corpus's mostly-minus algebra is quaternionic, and the antilinear $\mathcal{C}$ is what replaces the real form there. The two-component form is the Weyl operator with the antilinear mass term $m\epsilon(\,\cdot\,)^{*}$, and the two Weyl operators satisfy $W_RW_L=\Box$, which is the precise sense in which they are square roots of the Klein–Gordon operator. The charge-conjugation operator is an involution whose two eigenspaces are each of real dimension four: the $+1$ space is the Majorana sector, on which the equation is Dirac, and the $-1$ space is the ELKO companion, on which the equation has the opposite sign of the mass and is not Dirac. Both are on the mass shell, $(\Box-m^{2})\psi=0$, and both were obtained by elimination. A self-conjugate field carries one Weyl spinor rather than two, no vector current, and no fermion number; whether a given fermion is Majorana, and the neutrino mass and phases, are outside the algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathsf C_0=iT_{e_t,e_x}$, $\mathsf C_k=iT_{e_k,e_y}$, $\Gamma=\mathsf C_5=-iT_{e_t,e_z}$ | Generator cells and chirality operator; $\{\mathsf C_\mu,\mathsf C_\nu\}=2g_{\mu\nu}T_{e_t,e_t}$ |
| $L_a,R_b$, $T_{a,b}=L_aR_b$ | $L_a\psi=a\psi$, $R_b\psi=\psi b$; $T_{a,b}\psi=a\psi b$ |
| $\mathbb{D}\psi=m\psi^{c}$ | The Majorana equation |
| $\psi^{c}=C\bar\psi^{T}=i\psi^{*}$ | Charge-conjugate spinor |
| $C=T_{e_t,e_x}=-i\mathsf C_0$ | Charge-conjugation cell; real, $C^{T}=-C$, $C^{2}=-T_{e_t,e_t}$ |
| $C\mathsf C_{\mu}^{T}C^{-1}=-\mathsf C_{\mu}$ | Preservation of the kinetic term |
| $\mathcal{C}\psi=K\psi^{*}$ | The antilinear real structure |
| $K=C\mathsf C_{0}^{T}=i\,T_{e_t,e_t}$ | Central scalar of the real structure; $KK^{*}=T_{e_t,e_t}$ |
| $K\mathsf C_{\mu}^{*}K^{-1}=-\mathsf C_{\mu}$ | $\mathcal{C}$ commutes with $\mathbb{D}$ |
| $\psi^{c}=+\psi$ | Majorana condition; the $+1$ eigenspace, real dimension four |
| $\psi^{c}=-\psi$ | ELKO condition; the $-1$ eigenspace, real dimension four |
| $\mathbb{D}\psi=-m\psi$ | Sign-flipped equation of the ELKO sector |
| $(\Box-m^{2})\psi=0$ | Common mass shell of both sectors |
| $\mathrm{Cl}_{3,1}\cong M_4(\mathbb{R})$ | Real form: generators real, purely real solutions |
| $r_{0},r_{1},r_{2},r_{3}$ | The exhibited real generators, four cells with $\{r_{\mu},r_{\nu}\}=2\mathring\eta_{\mu\nu}T_{e_t,e_t}$ |
| $\sigma_{\mu}=(I_2,-\boldsymbol{\sigma})$, $\bar\sigma_{\mu}=(I_2,+\boldsymbol{\sigma})$ | Weyl vectors (lowered, mostly-minus frame) |
| $\epsilon=i\sigma_2$ | Symplectic form; $\epsilon^{T}=-\epsilon$, $\epsilon^{2}=-I_2$ |
| $D_L=i\sum_\mu\bar\sigma_{\mu}\partial/\partial Q_\mu-m\epsilon(\,\cdot\,)^{*}$ | Two-component Majorana operator |
| $W_L=i\sum_\mu\bar\sigma_{\mu}\partial/\partial Q_\mu$, $W_R=i\sum_\mu\sigma_{\mu}\partial/\partial Q_\mu$ | Weyl operators; $W_RW_L=\Box$ |
| $\Box=\Delta-\partial^2/\partial {t'}^2$ | d'Alembertian, series convention |

## Further Reading

- E. Majorana, "Teoria simmetrica dell'elettrone e del positrone," *Nuovo Cimento* **14** (1937) 171–184, for the original equation and the real form of the Dirac theory.
- C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), Chapter 2 and Appendix A, for the charge-conjugation matrix, the Majorana condition and the conventions used here.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), Chapter 5, for the charge-conjugation operator and its two eigenstates.
- P. B. Pal, "Dirac, Majorana, and Weyl fermions," *American Journal of Physics* **79** (2011) 485–498, for the counting of components and the neutrality of the Majorana field.
- A. Aste, "A direct road to Majorana fields," *Symmetry* **2** (2010) 1776–1809, for the two-component construction and the symplectic group $\mathrm{Sp}(2,\mathbb{C})$ as the double cover of the Lorentz group.
- E. Marsch, "On the Majorana equation: relations between its complex two-component and real four-component eigenfunctions," *ISRN Mathematical Physics* **2012** (2012) 760239, for the two-component and four-component eigenfunctions and their relation.
- P. Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the Lounesto classification and the class-5 (ELKO-type) spinor with the charge-conjugation eigenvalue $-1$.
- D. V. Ahluwalia and D. Grumiller, "Spin-half fermions with mass dimension one: theory, phenomenology, and dark matter," *Journal of Cosmology and Astroparticle Physics* **0507** (2005) 012, for the ELKO spinor and its properties.
- H. B. Lawson and M.-L. Michelsohn, *Spin Geometry* (Princeton, 1989), and P. Budinich and A. Trautman, *The Spinorial Chessboard* (Springer, 1988), for the real, complex and quaternionic types of Clifford modules and the reality of the generators by signature.

## Appendix — The Gamma Formulation

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra.

$$
\gamma_0=iL_tR_x,\quad \gamma_1=iL_xR_y,\quad \gamma_2=iL_yR_y,\quad \gamma_3=iL_zR_y,\quad \gamma_5=-iL_tR_z .
$$

A single product is a pure tensor; the products form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and a general element is a sum of at most four, with $\ell(M)=\operatorname{rank}c(M)$.

$\gamma_5$ is the reference-frame cell of the chirality $\Gamma$; the central grading $\chi=i\tilde\Xi_{\mathrm{ad}}$ ($\chi^2=e_t$, not an element of $\mathbb{B}$) is a different object, represented by $\gamma_5$ on the Dirac module.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.
