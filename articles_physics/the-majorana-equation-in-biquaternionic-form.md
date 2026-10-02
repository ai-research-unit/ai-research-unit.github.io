# __The Majorana Equation in Biquaternionic Form__

## Introduction

The **Majorana equation** is the relativistic wave equation of a fermion that is its own antiparticle, $\psi^{c}=\psi$. Ettore Majorana wrote it in 1937 as a real form of the Dirac equation, and it is the equation of the spin-$\tfrac12$ field whose charge conjugation is a symmetry rather than an exchange. It differs from the Dirac equation in one term and in one consequence: the mass term pairs the field with its conjugate instead of with the other chiral half, and the field therefore carries half the independent components of a Dirac field, no fermion number, and no electromagnetic coupling.

The corpus already owns the pieces around this equation. *The Neutrino and Majorana Fermions in Biquaternionic Form* fixes the three notions — Dirac, Weyl, Majorana — constructs charge conjugation as a conjugate-linear real structure $\mathcal{C}$ on the Dirac module $\Delta=S\oplus\bar S$, verifies that the constraint $\psi^{c}=\psi$ is consistent with the massive equation, computes the bilinears, identifies the coefficient conjugation $\bar{\cdot}$ as the algebra's charge conjugation, and shows that the material/informational split does not supply the reality condition. *Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form* separates the algebra's $\flat$ from the module's $\mathcal{C}$, places the neutral spinors in the $\mathrm{Spin}^c$ structure, and diagnoses the retired equation on its dispersion. *Real Spinors and Reality Conditions on the Biquaternion Algebra with Hermitian Adjoint* settles which spinor types each signature admits and why the normalisation must be stated. *Klein–Gordon from the Dirac Square in Biquaternionic Form* supplies the second-order consequence of a first-order pair.

What no companion article yet does is treat the **equation itself**: the three standard forms under which it is written and the proof that they agree, the two-component Majorana operator and the pair of Weyl operators whose product is the d'Alembertian, the eigenstructure of the charge-conjugation operator with its Majorana and ELKO sectors, and the counting of independent solutions. The present article supplies those, in the conventions of the series, and it defers the module-level reality discussion to the companion articles rather than repeating it.

The presentation is split three ways, as in the companions.

- **Established, and recomputed below.** In the block (chiral) basis with $g=\mathrm{diag}(+,-,-,-)$, the matrix $C=i\gamma^{2}\gamma^{0}$ is real, antisymmetric, $C^{T}=-C$ and $C^{2}=-I_4$, and $C\gamma^{\mu T}C^{-1}=-\gamma^{\mu}$ for all four $\mu$. The antilinear map $\mathcal{C}\psi=K\psi^{*}$ with $K=C\gamma^{0T}$ is a real structure, $\mathcal{C}^{2}=1$, whose matrix $K$ is real with $K^{2}=I_4$, and it satisfies $K\gamma^{\mu*}K^{-1}=-\gamma^{\mu}$ for all four $\mu$. It commutes with the kinetic operator $i\gamma^{\mu}\partial_\mu$. Its eigenspaces for the eigenvalues $\pm1$ are each of **real dimension four** and span the module. Both eigenspaces are on the mass shell, $(\Box-m^{2})\psi=0$; on the $+1$ eigenspace the Majorana equation is the Dirac equation, and on the $-1$ eigenspace it is the Dirac equation with the opposite sign of the mass term. The two-component Weyl operators satisfy $W_{R}W_{L}=\Box$, so the left- and right-handed Weyl operators are the two square roots of the d'Alembertian. In the opposite signature the Clifford algebra $\mathrm{Cl}_{3,1}$ is the real matrix algebra $M_4(\mathbb{R})$, and a representation with **all generators real** exists; that is the real form of the equation.
- **Transcribed, and cited.** The module-level construction of $\mathcal{C}$, the exchange of the chiral halves, the identification of $\bar{\cdot}$ as the charge conjugation, the fixed space of real dimension four, and the vanishing of the vector current are the content of the neutrino article and are used here, not rebuilt.
- **Not supplied.** The functional-analytic content of the two-component square root identity in the continuum, the observability of the neutrino's Majorana nature, the Majorana phases and the lepton-number-violating rates, and any selection principle that would make one fermion Majorana rather than Dirac, are outside the algebra.

The article is organised as follows. The next section states the equation and its three forms and proves the equivalence. A section then treats the charge-conjugation eigenstates and the ELKO companion. A section counts the independent solutions against the Dirac count. A closing section separates what the framework supplies, transcribes, and does not supply.

**Conventions.** We use those of the companion articles. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$, $e_k^{2}=-e_0$, $e_1e_2=e_3$, and $i$ the scalar imaginary. The matrix realisation is $\Phi(e_0)=I_2$, $\Phi(e_k)=-i\sigma_k$, $\Phi(i)=iI_2$. The Clifford generators are taken in the **block (chiral) basis** of the series,

$$
\gamma^{0}=\begin{pmatrix}0&I_2\\ I_2&0\end{pmatrix},\qquad
\gamma^{k}=\begin{pmatrix}0&\sigma^{k}\\ -\sigma^{k}&0\end{pmatrix},\qquad k=1,2,3,
$$

with $g=\mathrm{diag}(+,-,-,-)$ so that $\{\gamma^{\mu},\gamma^{\nu}\}=2g^{\mu\nu}I_4$, and $\gamma_5=i\gamma^{0}\gamma^{1}\gamma^{2}\gamma^{3}=\mathrm{diag}(-I_2,I_2)$. The Dirac module is $\Delta=S\oplus\bar S$, a Dirac spinor is $\Psi=(\psi_L,\psi_R)^{T}$, and the charge conjugation is $\psi^{c}=C\bar\psi^{T}=C\gamma^{0T}\psi^{*}$. The d'Alembertian is the series convention

$$
\Box=\partial_{ict}^{2}+\Delta=\Delta-\frac{1}{c^{2}}\partial_t^{2},
$$

so that the relativistic second-order equation reads $(\Box-m^{2})\psi=0$ in natural units, and the mass is measured in inverse-length units where a distinction is needed. The symbols $\sigma^{\mu}=(I_2,\boldsymbol{\sigma})$ and $\bar\sigma^{\mu}=(I_2,-\boldsymbol{\sigma})$ are the two-component Weyl vectors, and $\epsilon=i\sigma_2$ is the real antisymmetric $2\times2$ matrix, $\epsilon^{T}=-\epsilon$, $\epsilon^{2}=-I_2$, the symplectic form of the spinor module.

## The Equation and Its Three Forms

The Majorana equation is written in three ways, and the reason the three matter is that each displays a different property: the real form displays the reality of the solutions, the charge-conjugate form displays the role of charge conjugation, and the two-component form displays the contact with the Lorentz group. We state all three and prove that they agree.

### The Charge-Conjugate Form

The equation is

$$
i\gamma^{\mu}\partial_\mu\,\psi \;=\; m\,\psi^{c},
\qquad
\psi^{c} \;=\; C\,\bar\psi^{T} \;=\; C\gamma^{0T}\psi^{*},
$$

with $\bar\psi=\psi^{\dagger}\gamma^{0}$. The charge-conjugation matrix, in the block basis and the mostly-minus signature, is

$$
C\;=\;i\gamma^{2}\gamma^{0}
\;=\;\begin{pmatrix}\epsilon&0\\ 0&-\epsilon\end{pmatrix},
\qquad
\epsilon=i\sigma_2=\begin{pmatrix}0&1\\ -1&0\end{pmatrix},
$$

and it is **real**. The definition is fixed by the requirement that the kinetic term be preserved,

$$
C\,\gamma^{\mu T}\,C^{-1}\;=\;-\,\gamma^{\mu},
$$

and the matrix has the properties that make it a charge conjugation: $C^{T}=-C$, $C^{2}=-I_4$, $C^{\dagger}=C^{-1}$. All of these were checked in the block basis, on all four values of $\mu$ where a $\mu$ appears.

**The antilinear map is the reality condition, not the matrix.** Passing the conjugation into the spinor,

$$
\psi^{c} \;=\; K\,\psi^{*},
\qquad
K\;=\;C\,\gamma^{0T}\;=\;\begin{pmatrix}0&\epsilon\\ -\epsilon&0\end{pmatrix},
$$

and the matrix $K$ is **real** with

$$
K^{2}\;=\;I_4,
\qquad
K\,\gamma^{\mu*}\,K^{-1}\;=\;-\,\gamma^{\mu}\quad(\mu=0,1,2,3).
$$

The first relation is the statement that $\mathcal{C}:\psi\mapsto K\psi^{*}$ is an **involution**, $\mathcal{C}^{2}=1$, and the second is what makes it commute with the kinetic operator. Because $\mathcal{C}$ is conjugate-linear, commuting with $i\gamma^{\mu}\partial_\mu$ is exactly the displayed condition:

$$
\mathcal{C}\!\left(i\gamma^{\mu}\partial_\mu\psi\right)
=\;K\,(i\gamma^{\mu})^{*}\,\partial_\mu\psi^{*}
=\;i\gamma^{\mu}\partial_\mu\!\left(K\psi^{*}\right)
=\;i\gamma^{\mu}\partial_\mu\,\mathcal{C}\psi ,
$$

using $K(i\gamma^{\mu})^{*}K^{-1}=i\gamma^{\mu}$, which is the second relation. This is the same verified identity the neutrino article records, and it is the whole reason the constraint is consistent with the equation: applying $\mathcal{C}$ to $i\gamma^{\mu}\partial_\mu\psi=m\psi^{c}$ returns the same equation with $\psi$ and $\psi^{c}$ interchanged, so the deviation $\psi-\psi^{c}$ is preserved by the evolution and a field self-conjugate at one time stays self-conjugate.

**On the fixed space it is the Dirac equation.** If $\psi$ satisfies the Majorana equation and the constraint $\psi^{c}=\psi$, then $i\gamma^{\mu}\partial_\mu\psi=m\psi$, which is the massive Dirac equation. Conversely the massive Dirac equation restricted to the fixed space implies the Majorana equation. The two equations are therefore the same equation on the Majorana sector and different equations off it; the content is the consistency of the constraint, which is a computation and was performed above.

### The Real Form

A spinor is **real** when it equals its own conjugate, and the reason the equation can be written in a form in which that reality is visible is the reality type of the Clifford algebra.

**The real representation exists in the opposite signature.** The two real Clifford algebras of four dimensions are not isomorphic over $\mathbb{R}$: the corpus's mostly-minus algebra is the quaternionic matrix algebra $\mathrm{Cl}_{1,3}\cong M_2(\mathbb{H})$, and the mostly-plus algebra is the real matrix algebra $\mathrm{Cl}_{3,1}\cong M_4(\mathbb{R})$. In the mostly-plus signature the generators can be taken **purely real**, and the following set does it, with $\eta=\mathrm{diag}(-1,+1,+1,+1)$:

$$
r^{0}=\begin{pmatrix}0&1&0&0\\ -1&0&0&0\\ 0&0&0&1\\ 0&0&-1&0\end{pmatrix},\quad
r^{1}=\begin{pmatrix}0&1&0&0\\ 1&0&0&0\\ 0&0&0&1\\ 0&0&1&0\end{pmatrix},
$$

$$
r^{2}=\begin{pmatrix}0&0&1&0\\ 0&0&0&-1\\ 1&0&0&0\\ 0&-1&0&0\end{pmatrix},\quad
r^{3}=\begin{pmatrix}1&0&0&0\\ 0&-1&0&0\\ 0&0&-1&0\\ 0&0&0&1\end{pmatrix}.
$$

Each matrix is real; $r^{0}$ is antisymmetric with $(r^{0})^{2}=-I_4$ and $r^{1},r^{2},r^{3}$ are symmetric with $(r^{k})^{2}=+I_4$; and the four anticommute in pairs, so that $\{r^{\mu},r^{\nu}\}=2\eta^{\mu\nu}I_4$. This was checked entry by entry. In this representation the Dirac operator $i r^{\mu}\partial_\mu$ has real matrix coefficients, its massless part preserves the real subspace of real four-component spinors, and a solution of the massless equation can be chosen **purely real**; with a real mass term through the charge conjugation the massive solutions are the Majorana spinors. This is the sense in which the Majorana equation is "the Dirac equation written so that it has purely real solutions", the first of the three standard forms.

**Why the corpus's signature does not have it, and what replaces it.** In the mostly-minus signature the algebra is quaternionic and no representation with all generators real exists; that is the algebraic reason the corpus works with a complex Dirac module and an antilinear real structure $\mathcal{C}$ rather than with real spinors. The two pictures are the two normalisations of one structure, exchanged by the volume element, and the companion *Real Spinors and Reality Conditions* records that the roles of the two signs are exchanged in the two conventions. A reader comparing a "real" Majorana spinor in one signature with a "self-conjugate" Majorana spinor in the other is comparing the two normalisations, and the comparison must state which is in force. The framework's own carrier of the reality is the antilinear $\mathcal{C}$ of the previous subsection.

### The Two-Component Form

The third form acts on a complex two-component spinor and is the form in contact with the Lorentz group. With the Weyl vectors $\sigma^{\mu}=(I_2,\boldsymbol{\sigma})$ and $\bar\sigma^{\mu}=(I_2,-\boldsymbol{\sigma})$, the **Majorana operator** is the Weyl operator together with an antilinear mass term,

$$
D_L \;=\; i\,\bar\sigma^{\mu}\partial_\mu \;-\; m\,\epsilon\,(\,\cdot\,)^{*},
$$

acting on a left-handed Weyl spinor $\psi_L\in S$, so that the two-component Majorana equation is

$$
i\,\bar\sigma^{\mu}\partial_\mu\,\psi_L \;=\; m\,\epsilon\,\psi_L^{*}.
$$

The mass term is exactly the conjugation $\mathcal{C}$ written in two-component language: $\epsilon\,\psi_L^{*}$ is the right-handed conjugate that the four-component $\psi^{c}$ produces in its upper half, and the equation pairs the field with that conjugate rather than with an independent right-handed field. The matrix $\epsilon$ is the antisymmetric form that defines the symplectic pairing of *The Spinor Module in Biquaternionic Form and Its Lorentz Action*, and it is the same object as the off-diagonal block of $K$; the two-component form is therefore not a different equation but the same equation in the defining representation.

**The two Weyl operators are the two square roots of the d'Alembertian.** Set

$$
W_L=i\,\bar\sigma^{\mu}\partial_\mu,
\qquad
W_R=i\,\sigma^{\mu}\partial_\mu .
$$

Then

$$
\sigma^{\mu}\bar\sigma^{\nu}+\sigma^{\nu}\bar\sigma^{\mu}=2\eta^{\mu\nu}I_2
\qquad\Longrightarrow\qquad
W_RW_L \;=\; -\,\sigma^{\mu}\bar\sigma^{\nu}\partial_\mu\partial_\nu \;=\; -\,\eta^{\mu\nu}\partial_\mu\partial_\nu\,I_2 \;=\;\Box\,I_2 .
$$

The anticommutator identity was checked for all sixteen pairs $(\mu,\nu)$, and it is the two-component statement of the Clifford relation: the d'Alembertian is the **product** of the two Weyl operators, not the square of either alone. This is why the first-order two-component operators are called square roots of the Klein–Gordon operator, and it is the two-component counterpart of the matrix identity $(\not\partial)^{2}=-\not\partial^{2}=\Box$ used in *Klein–Gordon from the Dirac Square in Biquaternionic Form* for the four-component case. The mass term supplies the $-m^{2}$, so that the second-order equation of the self-conjugate field is the massive Klein–Gordon equation $(\Box-m^{2})\psi=0$, exactly as in the four-component case verified below.

## The Charge-Conjugation Eigenstates and the ELKO Companion

The charge-conjugation operator is an involution on an eight-real-dimensional space, so it has two eigenvalues and the module splits into two real forms. The split is worth computing, because one half is the Majorana sector and the other half is a different and often-missed object.

**The spectrum is $\{+1,-1\}$.** Since $\mathcal{C}^{2}=1$, the eigenvalues of $\mathcal{C}$ satisfy $\lambda^{2}=1$; since $\mathcal{C}$ is conjugate-linear and $K$ is real with $K^{2}=I_4$, both eigenvalues occur and the eigenspaces are the kernels of $K\psi^{*}=\pm\psi$. Solving the two linear systems in the eight real variables $(\mathrm{Re}\,\psi,\mathrm{Im}\,\psi)$ gives

$$
\dim_{\mathbb{R}}\{\psi:\psi^{c}=+\psi\}=4,
\qquad
\dim_{\mathbb{R}}\{\psi:\psi^{c}=-\psi\}=4,
$$

and the two eigenspaces together span $\Delta$. Both were obtained by elimination and both are four-real-dimensional, as the reality of $K$ requires: an involution on a real vector space of even dimension has eigenspaces of equal dimension.

**The $+1$ eigenspace is the Majorana sector.** In blocks the condition $K\psi^{*}=+\psi$ reads $\psi_R=-\epsilon\psi_L^{*}$ and $\psi_L=\epsilon\psi_R^{*}$, which are consistent, so the fixed space is parametrised by $\psi_L$ alone and has real dimension four. This is the Majorana condition of the neutrino article, and on this space the Majorana equation is the Dirac equation, as shown above. The bilinears of this sector — no vector current, a permitted scalar mass, a permitted axial current — are the Grassmann-level statements the neutrino article computes, and they are not re-derived here.

**The $-1$ eigenspace is the ELKO companion.** The condition $K\psi^{*}=-\psi$ reads $\psi_R=+\epsilon\psi_L^{*}$, which is the same equation with the opposite sign, and it too is consistent and four-real-dimensional. A spinor of this sector satisfies the **sign-flipped** equation

$$
i\gamma^{\mu}\partial_\mu\,\psi \;=\; -\,m\,\psi ,
$$

which is the Dirac equation with the wrong sign on the mass term. It is therefore **not** a solution of the Dirac equation for $m\neq0$, and it is the spinor called ELKO in the literature — the "eigenspinor of the charge-conjugation operator" of Lounesto's class 5. Its defining feature is exactly that charge conjugation returns minus the spinor, so the coupling to the central phase is obstructed even more strongly than for the Majorana sector: the antilinear article records that Majorana and ELKO spinors are both **neutral** for this reason, while the Dirac spinor carries the phase.

**Both sectors are on the same mass shell.** This follows from the involution alone and needs no knowledge of which sector a field lies in. Let $\psi$ solve $i\gamma^{\mu}\partial_\mu\psi=m\psi^{c}$. Apply the kinetic operator again and use that $\mathcal{C}$ commutes with it and is an involution:

$$
(i\gamma^{\mu}\partial_\mu)^{2}\psi
=\;m\,i\gamma^{\mu}\partial_\mu\,\psi^{c}
=\;m\,\mathcal{C}\!\left(i\gamma^{\mu}\partial_\mu\psi\right)
=\;m\,\mathcal{C}\!\left(m\psi^{c}\right)
=\;m^{2}\psi .
$$

Since $(\not\partial)^{2}=g^{\mu\nu}\partial_\mu\partial_\nu=-\Box$ and $i^{2}=-1$, the left side is $\Box\psi$, so

$$
(\Box-m^{2})\psi \;=\;0 .
$$

Every solution of the Majorana equation, in either eigenspace, obeys the massive Klein–Gordon equation; the ELKO companion is on the mass shell even though it is not a Dirac solution. The two sectors differ in the first-order equation, not in the dispersion, and this is the precise sense in which ELKO "solves Klein–Gordon but not Dirac".

**What the split does and does not say.** The two eigenspaces are the two real forms of the Dirac module under the same involution, and the four-component Majorana spinor is the $+1$ one. What the split does **not** provide is a mass term for the ELKO sector: the sign-flipped equation has the mass with the opposite sign, and no rewriting of the algebra turns the $+1$ Majorana equation into the $-1$ one without changing the sign of $m$. Whether the ELKO sector is realised in nature is an open empirical question, and no claim is made here.

## Solutions and the Counting of States

The counting is the sharpest difference between the Majorana and Dirac equations, and it is a statement about the field rather than about a single plane wave.

**A single plane wave is not self-conjugate.** For a plane wave $\psi=u\,e^{-ip\cdot x}$ one has $\psi^{c}=u^{c}e^{+ip\cdot x}$, so the condition $\psi^{c}=\psi$ for all $x$ forces $p=0$ and, at rest in the block basis, the only solution of the combined system is $u=0$. The self-conjugate object is not a single mode but the **field**

$$
\psi(x)\;=\;u\,e^{-ip\cdot x}\;+\;u^{c}\,e^{+ip\cdot x},
\qquad
(p\!\!\!/\,-m)u=0 ,
$$

which satisfies $\psi^{c}=\psi$ and the Dirac equation when $u$ does. This is the standard construction, and it is the resolution of the apparent conflict between "the Majorana spinor is its own conjugate" and "a plane wave is not its own conjugate": the condition is on the field, and the field pairs each positive-frequency mode with the negative-frequency conjugate of the same mode.

**Two independent components, against the Dirac four.** Because the fixed space is parametrised by $\psi_L$ alone, a Majorana field has the two complex components of one Weyl spinor, that is four real components, against the eight real components of a Dirac field. The doubling of the Dirac degrees of freedom is exactly the carrying of a conserved fermion number: the Dirac field has independent particle and antiparticle halves, the Majorana field has one. The companion article on the seesaw uses this counting, and the statement that two Majorana fields of equal mass reassemble into one Dirac field is the same count in reverse.

**Bilinears, at the level of the field.** The count and the neutrality are reflected in the bilinears: for the anticommuting Majorana field the vector current vanishes and the scalar and axial bilinears survive, so the field can carry a mass but no fermion number. The neutrino article computes this table and records the trap that a commuting c-number spinor obeying the same algebraic condition gives the **opposite** pattern, because the antisymmetry of the Grassmann components is what makes the scalar bilinear add rather than cancel. Nothing in the present article changes that; the eigenstructure above is classical and the bilinear physics is quantum, and they must not be mixed.

## What the Algebra Supplies, Transcribes, and Does Not Supply

| Item | Status |
|---|---|
| The charge-conjugation matrix $C=i\gamma^{2}\gamma^{0}$: real, $C^{T}=-C$, $C^{2}=-I_4$, $C\gamma^{\mu T}C^{-1}=-\gamma^{\mu}$ | **Supplied**, recomputed in the block basis on all $\mu$ |
| The antilinear real structure $\mathcal{C}\psi=K\psi^{*}$: $K$ real, $K^{2}=I_4$, $\mathcal{C}^{2}=1$, $K\gamma^{\mu*}K^{-1}=-\gamma^{\mu}$ | **Supplied**, recomputed on all $\mu$ |
| $\mathcal{C}$ commutes with the kinetic operator, so the constraint is consistent with the massive equation | **Supplied** (through $K\gamma^{\mu*}K^{-1}=-\gamma^{\mu}$) |
| The spectral split into two real four-dimensional eigenspaces, Majorana and ELKO | **Supplied**, recomputed by elimination |
| Both eigenspaces on the mass shell, $(\Box-m^{2})\psi=0$ | **Supplied** (from the involution and the Clifford square) |
| The two-component Weyl operators with $W_RW_L=\Box$ | **Supplied**, recomputed on all sixteen pairs |
| A real representation of $\mathrm{Cl}_{3,1}$, and hence purely real solutions in the opposite signature | **Supplied**, recomputed entry by entry |
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

The Majorana equation is the relativistic wave equation of a spin-$\tfrac12$ field equal to its own charge conjugate, and it is the Dirac equation with the mass term pairing the field with its conjugate instead of with the other chiral half. In the block (chiral) basis with $g=\mathrm{diag}(+,-,-,-)$ its three standard forms were written and shown to agree. The charge-conjugate form uses the real matrix $C=i\gamma^{2}\gamma^{0}$, for which $C^{T}=-C$, $C^{2}=-I_4$, $C\gamma^{\mu T}C^{-1}=-\gamma^{\mu}$ on all $\mu$, and the antilinear map $\mathcal{C}\psi=K\psi^{*}$ with the real matrix $K=C\gamma^{0T}$ satisfies $K^{2}=I_4$ and $K\gamma^{\mu*}K^{-1}=-\gamma^{\mu}$; this is the real structure, and it commutes with the kinetic operator, which is what makes the constraint $\psi^{c}=\psi$ consistent with the massive equation and reduces it to the Dirac equation on the fixed space. The real form uses the real representation of $\mathrm{Cl}_{3,1}\cong M_4(\mathbb{R})$, which was exhibited entry by entry with all generators real and purely real solutions; the corpus's mostly-minus algebra is quaternionic, and the antilinear $\mathcal{C}$ is what replaces the real form there. The two-component form is the Weyl operator with the antilinear mass term $m\epsilon(\,\cdot\,)^{*}$, and the two Weyl operators satisfy $W_RW_L=\Box$, which is the precise sense in which they are square roots of the Klein–Gordon operator. The charge-conjugation operator is an involution whose two eigenspaces are each of real dimension four: the $+1$ space is the Majorana sector, on which the equation is Dirac, and the $-1$ space is the ELKO companion, on which the equation has the opposite sign of the mass and is not Dirac. Both are on the mass shell, $(\Box-m^{2})\psi=0$, and both were obtained by elimination. A self-conjugate field carries one Weyl spinor rather than two, no vector current, and no fermion number; whether a given fermion is Majorana, and the neutrino mass and phases, are outside the algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $i\gamma^{\mu}\partial_\mu\psi=m\psi^{c}$ | The Majorana equation |
| $\psi^{c}=C\bar\psi^{T}=C\gamma^{0T}\psi^{*}$ | Charge-conjugate spinor |
| $C=i\gamma^{2}\gamma^{0}$ | Charge-conjugation matrix; real, $C^{T}=-C$, $C^{2}=-I_4$ |
| $C\gamma^{\mu T}C^{-1}=-\gamma^{\mu}$ | Preservation of the kinetic term |
| $\mathcal{C}\psi=K\psi^{*}$ | The antilinear real structure |
| $K=C\gamma^{0T}=\bigl(\begin{smallmatrix}0&\epsilon\\ -\epsilon&0\end{smallmatrix}\bigr)$ | Real involution matrix; $K^{2}=I_4$ |
| $K\gamma^{\mu*}K^{-1}=-\gamma^{\mu}$ | $\mathcal{C}$ commutes with $i\gamma^{\mu}\partial_\mu$ |
| $\psi^{c}=+\psi$ | Majorana condition; the $+1$ eigenspace, real dimension four |
| $\psi^{c}=-\psi$ | ELKO condition; the $-1$ eigenspace, real dimension four |
| $i\gamma^{\mu}\partial_\mu\psi=-m\psi$ | Sign-flipped equation of the ELKO sector |
| $(\Box-m^{2})\psi=0$ | Common mass shell of both sectors |
| $\mathrm{Cl}_{3,1}\cong M_4(\mathbb{R})$ | Real form: generators real, purely real solutions |
| $r^{0},r^{1},r^{2},r^{3}$ | The exhibited real generators, $\{r^{\mu},r^{\nu}\}=2\eta^{\mu\nu}I_4$ |
| $\sigma^{\mu}=(I_2,\boldsymbol{\sigma})$, $\bar\sigma^{\mu}=(I_2,-\boldsymbol{\sigma})$ | Weyl vectors |
| $\epsilon=i\sigma_2$ | Symplectic form; $\epsilon^{T}=-\epsilon$, $\epsilon^{2}=-I_2$ |
| $D_L=i\bar\sigma^{\mu}\partial_\mu-m\epsilon(\,\cdot\,)^{*}$ | Two-component Majorana operator |
| $W_L=i\bar\sigma^{\mu}\partial_\mu$, $W_R=i\sigma^{\mu}\partial_\mu$ | Weyl operators; $W_RW_L=\Box$ |
| $\Box=\Delta-\partial_t^{2}$ | d'Alembertian, series convention |

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
