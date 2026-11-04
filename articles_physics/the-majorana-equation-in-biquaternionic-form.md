# __The Majorana Equation in Biquaternionic Form__

## Introduction

The **Majorana equation** is the relativistic wave equation of a fermion that is its own antiparticle, $\psi^{c}=\psi$. Ettore Majorana wrote it in 1937 as a real form of the Dirac equation, and it is the equation of the spin-$\tfrac12$ field whose charge conjugation is a symmetry rather than an exchange. It differs from the Dirac equation in one term and in one consequence: the mass term pairs the field with its conjugate instead of with the other chiral half, and the field therefore carries half the independent components of a Dirac field, no fermion number, and hence no charge to couple minimally to a photon.

The corpus already owns the pieces around this equation. *The Neutrino and Majorana Fermions in Biquaternionic Form* fixes the three notions — Dirac, Weyl, Majorana — constructs charge conjugation as a conjugate-linear real structure $\mathcal{C}$ on the Dirac module $\Delta=S\oplus\bar S$, verifies that the constraint $\psi^{c}=\psi$ is consistent with the massive equation, computes the bilinears, identifies the coefficient conjugation $\bar{\cdot}$ as the algebra's charge conjugation, and shows that the material/informational split does not supply the reality condition. *Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form* separates the algebra's $\flat$ from the module's $\mathcal{C}$, places the neutral spinors in the $\mathrm{Spin}^c$ structure, and diagnoses the retired equation on its dispersion. *Real Spinors and Reality Conditions on the Biquaternion Algebra with Hermitian Adjoint* settles which spinor types each signature admits and why the normalisation must be stated. *Klein–Gordon from the Dirac Square in Biquaternionic Form* supplies the second-order consequence of a first-order pair.

What no companion article yet does is treat the **equation itself**: the three standard ways in which it is written, and what each of them does and does not assert, the two-component Majorana operator and the pair of Weyl operators whose product is the d'Alembertian, the eigenstructure of the charge-conjugation operator with its two real four-dimensional sectors, and the counting of independent solutions. The present article supplies those, in the conventions of the series, and it defers the module-level reality discussion to the companion articles rather than repeating it.

The presentation is split three ways, as in the companions.

- **Established, and recomputed below.** In the cell frame with $g=\mathrm{diag}(-,+,+,+)$ the charge-conjugation cell $C=R_{\vec e_x}^{\mathrm{axf}}$ is real and antisymmetric, $C^{T}=-C$, and $C^{2}=-L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$; it satisfies $C\,(iR_{\vec e_x}^{\mathrm{axf}})^{T}C^{-1}=-\,iR_{\vec e_x}^{\mathrm{axf}}$ and $C\,(iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}})^{T}C^{-1}=-\,iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ for all four $\mu$. The antilinear map $\mathcal{C}\psi=C(\psi^{\dagger}\,iR_{\vec e_x}^{\mathrm{axf}})^{T}=i\psi^{*}$ is a real structure, $\mathcal{C}^{2}=1$, with the central scalar $K=C\,(iR_{\vec e_x}^{\mathrm{axf}})^{T}=i$ and $K K^{*}=L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$. It anticommutes with each of the four **generator cells** $i c_\mu$ and commutes with the kinetic operator $\mathbb{D}$, because $\mathbb{D}$ is a sum of the **real cells** $c_\mu$ and the two signs are one factor of $i$ apart. Its eigenspaces for the eigenvalues $\pm1$ are each of **real dimension four** and span the module. Both are on the mass shell, $(\Box-m^{2})\psi=0$; on the $+1$ eigenspace the Majorana equation is the Dirac equation, and on the $-1$ eigenspace it is the Dirac equation with the opposite sign of the mass term, which a chirality flip removes. The two-component Weyl operators satisfy $W_{R}W_{L}=\Box$, so the left- and right-handed Weyl operators are the two square roots of the d'Alembertian. The four cells are themselves real and generate $\mathrm{Cl}_{3,1}\cong M_4(\mathbb{R})$, so $\mathbb{D}$ preserves a real subspace: that is the real form, and it is a property of the operator already written, not a fourth equation. The corpus's generators $i c_\mu$ are $\mathrm{Cl}_{1,3}\cong M_2(\mathbb{H})$ and admit no real representation, which is why the reality is carried by the antilinear $\mathcal{C}$.
- **Transcribed, and cited.** The module-level construction of $\mathcal{C}$, the exchange of the chiral halves, the identification of $\bar{\cdot}$ as the charge conjugation, the fixed space of real dimension four, and the vanishing of the vector current are the content of the neutrino article and are used here, not rebuilt.
- **Not supplied.** The functional-analytic content of the two-component square root identity in the continuum, the observability of the neutrino's Majorana nature, the Majorana phases and the lepton-number-violating rates, and any selection principle that would make one fermion Majorana rather than Dirac, are outside the algebra.

The article is organised as follows. The next section states the equation in its three forms and checks that they are one equation. A section then treats the charge-conjugation eigenstates, and the limit of the ELKO reading of them. A section counts the independent solutions against the Dirac count. A section then separates what the framework supplies, transcribes, and does not supply, and a short section at the end records how the same cells read as matrices, which is the only place in the article where matrix notation appears.

## Frame and Notation

The coordinate displays are read in the $\mathbb{B}$ frame, with $Q_t=ict'$; the cell displays carry the generator metric $g=\mathrm{diag}(-,+,+,+)$ and are read in the $\mathbb{M}_-$ frame. A **cell** is a product $L_aR_b$ read as one two-sided operator,

$$
L_a\psi=a\psi,\qquad R_b\psi=\psi b,\qquad L_aR_b\psi=a\psi b .
$$

The four cells that carry the metric are

$$
c_0=R_{\vec e_x}^{\mathrm{axf}},\qquad c_k=L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\qquad k=1,2,3,
$$

and each is **real** in the cell frame. The left factor of $c_0$ is absent because it is the identity and not because it is understood: $L_{e_t}^{\mathrm{axf}}$ and $R_{e_t}^{\mathrm{axf}}$ both act as the identity, because $e_t=1$, so a factor $L_{e_t}^{\mathrm{axf}}$ in a cell may be inserted or deleted without effect. This is why the same cell is written $iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}$ in one display and $iR_{\vec e_x}^{\mathrm{axf}}$ in another; the two are identical, and the article uses the short form after saying so once.

The **generator cells** are $i$ times the real cells. With $g=\mathrm{diag}(-,+,+,+)$ they carry the anticommutation relations,

$$
\{i c_\mu,\,i c_\nu\}\;=\;i^{2}\{c_\mu,c_\nu\}\;=\;-\{c_\mu,c_\nu\}\;=\;2g_{\mu\nu}L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}},
$$

because $i$ is central and $i^{2}=-1$, so that

$$
\{c_\mu,c_\nu\}=-2g_{\mu\nu}L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}.
$$

That minus is the whole difference between the two displays, and it is the reason the kinetic operator below has real coefficients. The chirality cell is

$$
\Gamma=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}=-iR_{\vec e_z}^{\mathrm{axf}},\qquad \Gamma^{2}=L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}},
$$

which is $-1$ on the left-handed half $S$ and $+1$ on the right-handed half $\bar S$. The Dirac module is $\Delta=S\oplus\bar S$, a Dirac spinor is $\Psi=(\psi_L,\psi_R)^{T}$, and charge conjugation is $\psi^{c}=C(\psi^{\dagger}\,iR_{\vec e_x}^{\mathrm{axf}})^{T}$, with the cell $C$ determined in the next section.

**The d'Alembertian.** The series convention is

$$
\Box=\frac{\partial^2}{\partial Q_t^2}+\Delta,
$$

and because the complex coordinate carries $Q_t=ict'$, the same object is $\Box=\Delta-(1/c^{2})\partial^{2}/\partial {t'}^{2}$ in SI units. The letter $c$ here is the speed of light and $c_\mu$ is a cell; the subscript separates the two symbols, and no equation below uses both in the same slot. In natural units $c=1$ the relativistic second-order equation reads $(\Box-m^{2})\psi=0$, and the mass is measured in inverse-length units where a distinction is needed.

**Where the derivative is taken.** The complex coordinate carries one factor of $i$ on its own, $\partial/\partial Q_t=-\frac{i}{c}\partial/\partial t'$. A cell contracted with a derivative must therefore be contracted with $\partial/\partial t'$, not with $\partial/\partial Q_t$: the complex coordinate would supply the $i$ a second time and reverse the sign of the time term. Every contraction below is written in the **real coordinates**

$$
x_0=t',\qquad x_k=Q_k,\qquad k=1,2,3,
$$

and it is in those coordinates that $g$ is the metric, that $g_{\mu\nu}[\mathbb{M}_-]$ are its components with $\sum_{\mu,\nu}g_{\mu\nu}[\mathbb{M}_-]\partial^2/\partial x_\mu\partial x_\nu=\partial^2/\partial {t'}^2-\Delta$, and that a real cell times a derivative is a real operator.

**The two-component vectors.** The symbols $\sigma_{\mu}=(I_2,-\boldsymbol{\sigma})$ and $\bar\sigma_{\mu}=(I_2,+\boldsymbol{\sigma})$ are the two-component Weyl vectors, lowered with $g$, and $\epsilon=i\sigma_2$ is the real antisymmetric $2\times2$ matrix, $\epsilon^{T}=-\epsilon$, $\epsilon^{2}=-I_2$, the symplectic form of the spinor module.

## The Equation and Its Three Forms

The Majorana equation is written in three ways. Two of them are operators and one is a reading, and separating them is what keeps the signs straight: the charge-conjugate form displays the role of charge conjugation, the real form displays the reality of the coefficients, and the two-component form displays the contact with the Lorentz group.

| Form | Operator | Carrier | What it displays |
|---|---|---|---|
| Charge-conjugate | a sum of real cells, two-sided | $\Delta=S\oplus\bar S$, four complex components | the role of the charge conjugation |
| Real | the same cells, read on a real subspace | the real four-dimensional subspace of the module | the reality of the coefficients |
| Two-component | a $2\times2$ matrix | $S$, two complex components | the Lorentz group in its defining representation |

**Two first-order equations, not one.** The word *Dirac* names two different displays in this subject, and they must not be conflated. The **cell equation** is

$$
\mathbb{D}\,\psi \;=\; m\,\psi ,
\qquad
\mathbb{D}=\sum_\mu c_\mu\frac{\partial}{\partial x_\mu},
$$

where every coefficient is one of the four real cells of the frame, and only the squares enter below. The operator is a sum of two-sided multiplications and acts on the four-component module; its square is $\Box$, with $c_0^{2}=-L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ supplying the minus of the time term and $c_k^{2}=+L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ the plus of the Laplacian. The **Weyl equation** is

$$
W_L\,\psi_L \;=\; 0,
$$

where $W_L$ is a $2\times2$ matrix acting on one chiral half. It is the massless limit of the cell equation in the defining representation of $SL(2,\mathbb{C})$, and it is the image of the cell operator under that representation. The two displays are related through the product of the two Weyl operators, $W_RW_L=\Box=\mathbb{D}^{2}$, computed in the third subsection. A reader who carries only one of them will mis-count the components; a reader who identifies them will mis-state the mass term.

### The Charge-Conjugate Form

Here and below $\mathbb{D}$ is the pair operator of *Operator and Calculus Conventions*, acting on the module in the chiral basis, with $\mathbb{D}^{2}=\Box$ and the real cell coefficients displayed above. The equation is

$$
\boxed{\;\mathbb{D}\,\psi \;=\; m\,\psi^{c},
\qquad
\psi^{c} \;=\; C\,(\psi^{\dagger}\,iR_{\vec e_x}^{\mathrm{axf}})^{T} \;=\; i\psi^{*}\;},
$$

with $\psi^{\dagger}\,iR_{\vec e_x}^{\mathrm{axf}}$. The charge-conjugation cell, in the cell frame and the mostly-minus signature, is

$$
C\;=\;L_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}\;=\;R_{\vec e_x}^{\mathrm{axf}}\;=\;-\,i\,(iR_{\vec e_x}^{\mathrm{axf}}),
$$

and it is **real**: the factor $-i$ multiplies the generator cell $iR_{\vec e_x}^{\mathrm{axf}}$, and the two factors of $i$ multiply to $1$, since $i^{2}=-1$. It is the time generator read with the opposite phase. The definition is fixed by the requirement that the kinetic term be preserved,

$$
C\,(iR_{\vec e_x}^{\mathrm{axf}})^{T}C^{-1}=-\,iR_{\vec e_x}^{\mathrm{axf}},
\qquad
C\,(iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}})^{T}C^{-1}=-\,iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},
$$

and the cell has the three properties that make it a charge conjugation:

$$
C^{T}=-C,\qquad C^{2}=-L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}},\qquad C^{\dagger}=C^{-1}.
$$

All of these were checked in the cell frame, on all four values of $\mu$ where a $\mu$ appears.

**The antilinear map is the reality condition, not the cell.** Passing the conjugation into the spinor,

$$
\psi^{c} \;=\; K\,\psi^{*},
\qquad
K\;=\;C\,(iR_{\vec e_x}^{\mathrm{axf}})^{T}\;=\;i\,L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}},
$$

the central scalar $K$ is the plain $i$, and it satisfies

$$
K\,K^{*}\;=\;L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}},
$$

which is the statement that $\mathcal{C}:\psi\mapsto K\psi^{*}$ is an **involution**, $\mathcal{C}^{2}=1$. The compatibility with the generators is one display per family, and the two families are one factor of $i$ apart:

$$
K\,(i c_\mu)^{*}\,K^{-1}\;=\;-\,i c_\mu,
\qquad
K\,c_\mu^{*}\,K^{-1}\;=\;c_\mu,
\qquad \mu=0,1,2,3 .
$$

The left identity is the **anticommutation with the generators**, and the right one is the **commutation with the kinetic operator**. Neither is a separate hypothesis: a generator is one factor of $i$ times a cell with real entries, so the coefficient conjugate of $i c_\mu$ is $-i c_\mu$, and since $K$ is a central scalar both identities reduce to the reality of $c_\mu$. The single factor of $i$ between the two lines is the whole content of the apparently opposite signs.

Because $\mathcal{C}$ is conjugate-linear and the kinetic operator has real coefficients,

$$
\mathcal{C}\!\left(\mathbb{D}\psi\right)
=\;K\sum_\mu c_\mu^{*}\frac{\partial}{\partial x_\mu}\psi^{*}
=\;\sum_\mu c_\mu\frac{\partial}{\partial x_\mu}\!\left(K\psi^{*}\right)
=\;\mathbb{D}\,\mathcal{C}\psi ,
$$

and no sign is produced. This is the same verified identity the neutrino article records, and it is the whole reason the constraint is consistent with the equation: applying $\mathcal{C}$ to $\mathbb{D}\psi=m\psi^{c}$ returns the same equation with $\psi$ and $\psi^{c}$ interchanged, so the deviation $\psi-\psi^{c}$ is preserved by the evolution and a field self-conjugate at one time stays self-conjugate.

**On the fixed space it is the Dirac equation.** If $\psi$ satisfies the Majorana equation and the constraint $\psi^{c}=\psi$, then $\mathbb{D}\psi=m\psi$, which is the massive Dirac equation. Conversely the massive Dirac equation restricted to the fixed space implies the Majorana equation. The two equations are therefore the same equation on the Majorana sector; on the complementary eigenspace the same equation appears with the reversed sign of the mass, which the chirality cell removes. The content is the consistency of the constraint, which is a computation and was performed above.

### The Real Form

A spinor is **real** when it equals its own conjugate, and whether the equation can be written so that this reality is visible depends on the reality type of the Clifford algebra. The point is easy to get wrong, so it is stated before it is used.

**The coefficient is already real; the generator is not.** The four cells $c_\mu$ have real entries, but they carry $\{c_\mu,c_\nu\}=-2g_{\mu\nu}L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$, that is the metric $-\varepsilon=(1,-1,-1,-1)$. Read as generators, they therefore generate $\mathrm{Cl}_{3,1}\cong M_4(\mathbb{R})$ and not the corpus's $\mathrm{Cl}_{1,3}$. The corpus's generators are $i c_\mu$, and those carry $+g$, hence $\mathrm{Cl}_{1,3}\cong M_2(\mathbb{H})$, which has **no** representation by real $4\times4$ matrices. That is the whole reason the $i$ sits in the generator and not in the kinetic operator, and the two statements are not in conflict: $\mathbb{D}=\sum c_\mu\partial/\partial x_\mu$ is a real operator because the cells are read with the opposite overall sign of the metric.

**What that buys.** Because every $c_\mu$ is real, $\mathbb{D}$ preserves the real subspace $\mathbb{R}^{4}\subset\Delta$, and a solution whose initial data lie there stays there: the real form of the equation is a statement about the operator, not about a second operator. The real subspace it preserves is the one on which the charge conjugation is $\psi\mapsto\psi^{*}$ rather than $\psi\mapsto i\psi^{*}$; the two differ by the normalisation of the reality, which is the point of *Real Spinors and Reality Conditions*, and in the corpus's mostly-minus normalisation the same four-real-dimensional family appears as $\psi=i\psi^{*}$, the Majorana sector computed below, not as the strictly real-valued spinors. A real-valued spinor in the corpus's normalisation has $\psi^{c}=i\psi$ and is therefore **not** its own conjugate; this is the trap of the word "real", and the two normalisations must not be mixed.

**The conventional Majorana frame.** For comparison with the literature, the same algebra has a frame in which the temporal cell is antisymmetric and the three spatial cells are symmetric, with $\mathringg_{\mu\nu}[\mathbb{M}_-]$:

$$
r_{0}=-L_{\vec e_x}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}},\qquad
r_{1}=-L_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\qquad
r_{2}=L_{\vec e_z}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}},\qquad
r_{3}=-L_{\vec e_z}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}},
$$

$$
(r_{0})^{2}=-L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}},\quad (r_{k})^{2}=+L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}},\quad
\{r_{\mu},r_{\nu}\}=2\mathringg_{\mu\nu}[\mathbb{M}_-]L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}.
$$

This is a **frame of the same real algebra**, not an existence proof: the four cells $c_\mu$ above already have exactly this pattern, with $c_0=R_{\vec e_x}^{\mathrm{axf}}$ antisymmetric and $c_k=L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ symmetric, and they carry the same anticommutator with $-g$. What the display exhibits is the standard shape in which the real Majorana representation is quoted. In this frame the massless equation

$$
\sum_\mu r_\mu\frac{\partial}{\partial x_\mu}\,\psi \;=\; 0
$$

has real coefficients and squares to

$$
\sum_\mu (r_\mu)^{2}\frac{\partial^2}{\partial x_\mu^2}
\;=\;-\,\frac{\partial^2}{\partial {t'}^2}+\Delta
\;=\;\Box .
$$

The massless field therefore propagates real initial data, and this is the sense in which the Majorana equation is "the Dirac equation written so that it has purely real solutions": a reality statement about the coefficients, with the charge conjugation then supplying the mass. It is **not** a third operator; it is the reality reading of the first form, and a reader who expects a new equation here will look for one that does not exist.

### The Two-Component Form

The third form acts on a complex two-component spinor and is the form in contact with the Lorentz group. It is not a different equation: it is the same dynamics in the defining representation, and its operator is the image of the cell operator $\mathbb{D}$ under that representation.

**The two Weyl operators.** The Weyl vectors are lowered and the derivatives are lowered, so the invariant contractions carry the metric weight explicitly:

$$
W_L=i\sum_\mu g_{\mu\mu}\,\bar\sigma_{\mu}\frac{\partial}{\partial x_\mu}
=i\Bigl(\frac{\partial}{\partial t'}-\boldsymbol\sigma\cdot\nabla\Bigr),
\qquad
W_R=i\sum_\mu g_{\mu\mu}\,\sigma_{\mu}\frac{\partial}{\partial x_\mu}
=i\Bigl(\frac{\partial}{\partial t'}+\boldsymbol\sigma\cdot\nabla\Bigr).
$$

The metric factor is not decoration: without it the spatial part changes sign and the two chiralities are exchanged. That is the trap of the two-component form, and it is the same trap as in the four-component count — a sign of a weight, not a sign of a physics. With $g=\mathrm{diag}(-,+,+,+)$ the two orders of the pair give

$$
\sigma_{\mu}\bar\sigma_{\nu}+\sigma_{\nu}\bar\sigma_{\mu}=2\varepsilon_\mu\delta_{\mu\nu}I_2,
\qquad
\bar\sigma_{\mu}\sigma_{\nu}+\bar\sigma_{\nu}\sigma_{\mu}=2\varepsilon_\mu\delta_{\mu\nu}I_2,\qquad \varepsilon=(1,-1,-1,-1),
$$

both verified for all sixteen pairs $(\mu,\nu)$; the symmetric part of a product is the metric, and the antisymmetric part spans the six Lorentz generators.

**Where the two-component equation comes from.** It is a block of the four-component equation, not an independent postulate, and the derivation is short enough to give in full. In the chiral basis the equation $\mathbb{D}\psi=m\psi$ reads as a pair,

$$
W_L\,\psi_L \;=\; \mu\,\psi_R,
\qquad
W_R\,\psi_R \;=\; \mu\,\psi_L,
$$

with $\mu=\pm m$. The sign of $\mu$ is fixed by the frame and moved to $+m$ by $\psi_R\mapsto-\psi_R$; nothing below depends on it, and the displays take $\mu=+m$.

**The Majorana condition is what closes the pair.** The two blocks are two equations for two unknowns, and a Majorana field is the case in which they are not independent. With $\epsilon=i\sigma_2$ the condition is

$$
\psi_R \;=\; \epsilon\,\psi_L^{*},
$$

fixed up to one phase, which is the same convention that fixes $\mu$. Substituting into the first block leaves a single equation for a single two-component spinor, and that is the **two-component Majorana equation**:

$$
i\Bigl(\frac{\partial}{\partial t'}-\boldsymbol\sigma\cdot\nabla\Bigr)\psi_L
\;=\; m\,\epsilon\,\psi_L^{*}.
$$

The operator $D_L=W_L-m\,\epsilon\,(\,\cdot\,)^{*}$ is therefore **antilinear**, and it must not be squared the way a matrix operator is: $W_L$ is one block and $W_R$ the other, so the second-order equation of the two-component form comes from eliminating $\psi_R$ between the two blocks, not from $D_L^{2}$. A reader who squares $D_L$ as if it were a matrix obtains the wrong sign, and this is the one place in the article where the difference bites.

On a plane wave $e^{-iEt'+i\boldsymbol p\cdot\boldsymbol x}$ the massless equation reads $(E+\boldsymbol\sigma\cdot\boldsymbol p)\psi_L=0$, that is $\boldsymbol\sigma\cdot\hat{\boldsymbol p}\,\psi_L=-\psi_L$: helicity $-\tfrac12$, the left-handed branch. The mass term is the conjugation $\mathcal{C}$ written in two-component language — $\epsilon\psi_L^{*}$ is exactly the lower half that $\psi^{c}$ supplies for a self-conjugate field — so the equation pairs the field with its own conjugate rather than with an independent right-handed field. The matrix $\epsilon$ is the antisymmetric form that defines the symplectic pairing of *The Spinor Module in Biquaternionic Form and Its Lorentz Action*.

**The two Weyl operators are the two square roots of the d'Alembertian.** The cross terms in $W_RW_L$ cancel because the derivatives commute and the Pauli matrices anticommute,

$$
W_RW_L
=-\Bigl(\frac{\partial}{\partial t'}+\boldsymbol\sigma\cdot\nabla\Bigr)
\Bigl(\frac{\partial}{\partial t'}-\boldsymbol\sigma\cdot\nabla\Bigr)
=-\frac{\partial^2}{\partial {t'}^2}
+\sum_{j,k}\sigma_j\sigma_k\frac{\partial^2}{\partial Q_j\partial Q_k},
$$

and $\sum_{j,k}\sigma_j\sigma_k\partial^2/\partial Q_j\partial Q_k=\sum_{j,k}\delta_{jk}\partial^2/\partial Q_j\partial Q_k=\Delta$, because only the symmetric part of $\sigma_j\sigma_k$ survives the commuting derivatives. Hence, in natural units,

$$
\boxed{\;W_RW_L \;=\; \Bigl(\Delta-\frac{\partial^2}{\partial {t'}^2}\Bigr)I_2 \;=\;\Box\,I_2\;}.
$$

In the index notation the same computation is the symmetrisation of the double sum,

$$
W_RW_L
=-\sum_{\mu,\nu}g_{\mu\mu}g_{\nu\nu}\,\sigma_{\mu}\bar\sigma_{\nu}\frac{\partial^2}{\partial x_\mu\partial x_\nu}
=-\sum_{\mu,\nu}g_{\mu\nu}[\mathbb{M}_-]\frac{\partial^2}{\partial x_\mu\partial x_\nu}\,I_2
=\Box\,I_2,
$$

since $\sum_\mug_{\mu\mu}[\mathbb{M}_-]\partial^2/\partial x_\mu^2=\partial^2/\partial {t'}^2-\Delta$. The d'Alembertian is the **product** of the two Weyl operators and not the square of either alone; that is the precise sense in which the first-order two-component operators are square roots of the Klein–Gordon operator, and it is the two-component counterpart of the matrix square of *Klein–Gordon from the Dirac Square in Biquaternionic Form*. Applied to the Majorana pair it gives the elimination in one line: substituting $\psi_R=\epsilon\psi_L^{*}$ into the first block and then the second block into the result yields

$$
W_RW_L\,\psi_L
=\mu\,W_R\bigl(\epsilon\psi_L^{*}\bigr)
=\mu^{2}\psi_L
=m^{2}\psi_L ,
$$

so that $(\Box-m^{2})\psi_L=0$ — the same second-order equation as in the four-component form, and with no sign left over, because $\mu^{2}=m^{2}$ regardless of the frame convention.

## The Charge-Conjugation Eigenstates and the ELKO Reading

The charge-conjugation operator is an involution on a space of real dimension eight, so it has two eigenvalues and the module splits into two real forms. The split is worth computing, because it is routinely misread as two theories: one half is the Majorana sector, and the other half turns out to be the same sector seen through the chirality.

**The spectrum is $\{+1,-1\}$.** Since $\mathcal{C}^{2}=1$ and $\mathcal{C}$ is conjugate-linear with the central scalar $K=i$, both eigenvalues occur and the eigenspaces are the kernels of $K\psi^{*}=\pm\psi$. Solving the two linear systems in the eight real variables $(\mathrm{Re}\,\psi,\mathrm{Im}\,\psi)$ gives

$$
\dim_{\mathbb{R}}\{\psi:\psi^{c}=+\psi\}=4,
\qquad
\dim_{\mathbb{R}}\{\psi:\psi^{c}=-\psi\}=4,
$$

and the two eigenspaces together span $\Delta$. The count is immediate from the condition: writing $\psi=a+ib$ with $a,b\in\mathbb{R}^{4}$, the equation $\psi=\pm i\psi^{*}$ gives $a=\pm b$, so each eigenspace is $\{(1\pm i)a\}$ and carries four real parameters. Multiplication by $i$ carries one eigenspace onto the other.

**The $+1$ eigenspace is the Majorana sector.** The condition $K\psi^{*}=+\psi$ is $\psi=i\psi^{*}$, a single relation between the two halves rather than two independent real conditions. Since $\mathcal{C}$ anticommutes with $\Gamma$, it carries $S$ to $\bar S$ and back, so the projection of the fixed space onto either half is an isomorphism; the fixed space is therefore parametrised by $\psi_L$ alone and has real dimension four. This is the Majorana condition of the neutrino article, and on this space the Majorana equation is the Dirac equation, as shown above. The bilinears of this sector — no vector current, a permitted scalar mass, a permitted axial current — are the Grassmann-level statements the neutrino article computes, and they are not re-derived here.

**The $-1$ eigenspace, and why it is not a second theory.** The condition $K\psi^{*}=-\psi$ is $\psi=-i\psi^{*}$, the same relation with the opposite sign, and it too has real dimension four. A spinor of this sector, pushed through $\mathbb{D}\psi=m\psi^{c}$, obeys

$$
\mathbb{D}\,\psi \;=\; -\,m\,\psi .
$$

That reads like a new equation, and it is not. The chirality cell anticommutes with every $c_\mu$ and therefore with $\mathbb{D}$, and it exchanges the two eigenspaces: if $\mathcal{C}\psi=-\psi$ then $\mathcal{C}(\Gamma\psi)=-\Gamma\mathcal{C}\psi=+\Gamma\psi$, so $\Gamma\psi$ lies in the $+1$ space. Since $\mathbb{D}(\Gamma\psi)=-\Gamma\mathbb{D}\psi$, a solution of $\mathbb{D}\psi=-m\psi$ is carried to

$$
\mathbb{D}\,(\Gamma\psi) \;=\; +\,m\,(\Gamma\psi),
$$

which is the massive Dirac equation. The $-1$ sector is therefore the $+1$ sector seen through the chirality flip, with the sign of the mass absorbed: no spectrum separates the two sectors.

**Why the carrier is $\Gamma$ and not the multiplication by $i$.** Both $\psi\mapsto\Gamma\psi$ and $\psi\mapsto i\psi$ exchange the two eigenspaces, since $\Gamma$ and $i$ are both odd under the conjugation:

$$
(\Gamma\psi)^{c}=-\Gamma\psi^{c},
\qquad
(i\psi)^{c}=-i\,\psi^{c}.
$$

They differ in what they do to the equation, and the difference is a count of sign changes. The chirality cell changes sign **twice**, once against the kinetic operator, $\Gamma\mathbb{D}=-\mathbb{D}\Gamma$, and once against the conjugation, and the two cancel:

$$
\mathbb{D}(\Gamma\psi)
=-\Gamma\,\mathbb{D}\psi
=-\Gamma\,m\psi^{c}
=-m\,\Gamma\psi^{c}
=m\,(\Gamma\psi)^{c}.
$$

Multiplication by $i$ changes sign **once**, against the conjugation only, so it carries a solution of the equation with mass $m$ to a solution of the same display with mass $-m$:

$$
\mathbb{D}(i\psi)
=i\,\mathbb{D}\psi
=i\,m\psi^{c}
=-m\,i\psi^{c}
=-m\,(i\psi)^{c}.
$$

So $\Gamma$ is a symmetry of the Majorana equation and $i$ is not: $i$ permutes the eigenvalues and reverses the mass, $\Gamma$ permutes them and preserves everything else. That is the precise sense in which the two sectors are one theory — the passage between them is made by a symmetry of the equation, not by a relabelling that changes it. It is also the same arithmetic as in the frame section, where the two factors of $i$ in a generator cell multiply to $-1$. What the eigenvalue does distinguish is the neutrality, which is the next point.

**The neutrality.** What both sectors do share, and what the eigenvalue does fix, is the obstruction to a phase: if $\mathcal{C}\psi=\pm\psi$ then $\psi$ cannot be multiplied by $e^{i\alpha}$ without leaving the sector, so neither a Majorana nor an anti-self-conjugate spinor can carry a conserved $U(1)$ charge. The antilinear article records this for both signs, and it is the algebraic content of "the Majorana field has no fermion number".

**The ELKO reading, and its limit.** The spinors of mass dimension one in the literature are built as the eigenspinors of exactly this $C$ operator, and **both** eigenvalues are used: the self-conjugate and the anti-self-conjugate members are taken together as the full set. What distinguishes them there is not the eigenvalue but the bilinears — the degenerate "dipole" class 5 of Lounesto's classification, where the scalar and axial densities vanish while the vector density does not — together with the mass dimension one and the resulting non-standard spin sums. None of that follows from the eigenstructure computed here. An article that reported the $-1$ eigenspace as "the ELKO sector" would be claiming a dynamical distinction where the algebra supplies a bookkeeping one.

**Both sectors are on the same mass shell.** The second-order equation is common to the whole module and needs no matrix square. Let $\psi$ solve $\mathbb{D}\psi=m\psi^{c}$. Applying the kinetic operator again, and using that $\mathcal{C}$ commutes with it and is an involution,

$$
(\mathbb{D})^{2}\psi
\;=\;m\,\mathbb{D}\,\psi^{c}
\;=\;m\,\mathcal{C}\!\left(\mathbb{D}\psi\right)
\;=\;m\,\mathcal{C}\!\left(m\psi^{c}\right)
\;=\;m^{2}\,\mathcal{C}^{2}\psi
\;=\;m^{2}\psi ,
$$

so $(\Box-m^{2})\psi=0$ in either eigenspace. The same chain in the algebra is the chiral pair $\tilde{\nabla}\tilde{\Psi}_R=m\tilde{\Psi}_L$, $\tilde{\nabla}^{\natural}\tilde{\Psi}_L=m\tilde{\Psi}_R$: applying $\tilde{\nabla}^{\natural}$ to the first member and using the second gives $\Box\tilde{\Psi}_R=m^{2}\tilde{\Psi}_R$, and symmetrically for the left half. The two routes are the module and the algebra faces of one statement.

**What the split does and does not say.** The two eigenspaces are the two real forms of the Dirac module under one involution, each of real dimension four, and $\Gamma$ is an isomorphism between them. What the split does **not** give is a second mass, a second dispersion, or a second particle: it gives one field with a definite charge-conjugation eigenvalue. Whether the mass-dimension-one programme built on the same operator describes nature is an empirical question, and it is not settled by anything computed here.

## Solutions and the Counting of States

The counting is the sharpest difference between the Majorana and Dirac equations, and it is a statement about the field rather than about a single plane wave.

**A single plane wave is never a solution.** For $\psi=u\,\exp(-ip\cdot x)$ the kinetic term is proportional to $\exp(-ip\cdot x)$ while $\psi^{c}=u^{c}\exp(+ip\cdot x)$ is proportional to the opposite exponential, so the equation splits into two conditions that must hold at once: the coefficient of $\exp(-ip\cdot x)$ requires $i(p_{0}c_{0}-\sum_k p_{k}c_{k})u=0$, and the coefficient of the conjugate exponential requires $m\,u^{c}=0$, hence $u=0$ for every $p$. Nothing is wrong with the equation; a mode and its conjugate are two different modes.

**The self-conjugate object is the field, not the mode.** The solution pairs the mode with the conjugate of the same momentum,

$$
\psi(x)\;=\;u\,\exp(-ip\cdot x)\;+\;u^{c}\,\exp(+ip\cdot x),
\qquad
\Bigl(iR_{\vec e_x}^{\mathrm{axf}}p_{0}-\sum_k iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}p_{k}+m\Bigr)u=0 ,
$$

which is self-conjugate by construction, $(\psi^{c})^{c}=\psi$, and which solves the Majorana equation whenever $u$ solves the bracket displayed beside it. The two frequencies give one condition each, and they are not the same condition: the coefficient of $\exp(-ip\cdot x)$ requires $(iP+m)u=0$ with $P=p_{0}c_{0}-\sum_k p_{k}c_{k}$, which is the bracket as displayed, while the coefficient of $\exp(+ip\cdot x)$ requires $(iP-m)u^{c}=0$. The second is the conjugate of the first: conjugating $(iP+m)u=0$ reverses the sign of $i$ and leaves the real matrix $P$ alone, and a central scalar carries $u^{*}$ to $u^{c}$, so a single antilinear condition on $u$ produces both halves, and the amplitude and its conjugate obey the bracket with opposite signs of $m$. That is the momentum-space picture of "one field, two signs of the frequency", and it is why the sign of $m$ in the display tracks the frequency and not a choice of physics. It is also the resolution of the apparent conflict between "the Majorana spinor is its own conjugate" and "a plane wave is not self-conjugate": the condition is on the field, and the field carries two modes of opposite frequency.

**The bracket is the mass shell.** The kinetic part of the bracket is $iP$, and

$$
(iP)^{2}=-P^{2}=p_{0}^{2}-|\boldsymbol p|^{2},
$$

because $c_{0}^{2}=-L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$, $c_{k}^{2}=+L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ and the cross terms vanish by the anticommutation. The bracket therefore forces $p_{0}^{2}-|\boldsymbol p|^{2}=m^{2}$: the field is on the mass shell, and the metric enters only through the relative minus of the spatial term. Written the other way round, $P^{2}=-m^{2}L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$, which is the same statement with the sign of the square absorbed by $i^{2}=-1$.

**Four real components, against the Dirac eight.** Because the fixed space is parametrised by $\psi_L$ alone, a Majorana field has the two complex components of one Weyl spinor, that is four real components, against the eight real components of a Dirac field. The doubling of the Dirac degrees of freedom is exactly the carrying of a conserved fermion number: the Dirac field has independent particle and antiparticle halves, the Majorana field has one. The companion article on the seesaw uses this counting, and the statement that two Majorana fields of equal mass reassemble into one Dirac field is the same count in reverse.

**Bilinears, at the level of the field.** The count and the neutrality are reflected in the bilinears: for the anticommuting Majorana field the vector current vanishes and the scalar and axial bilinears survive, so the field can carry a mass but no fermion number. The neutrino article computes this table and records the trap that a commuting c-number spinor obeying the same algebraic condition gives the **opposite** pattern, because the antisymmetry of the Grassmann components is what makes the scalar bilinear add rather than cancel. Nothing in the present article changes that; the eigenstructure above is classical and the bilinear physics is quantum, and they must not be mixed.

## What the Algebra Supplies, Transcribes, and Does Not Supply

| Item | Status |
|---|---|
| The charge-conjugation cell $C=R_{\vec e_x}^{\mathrm{axf}}$: real, $C^{T}=-C$, $C^{2}=-L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$, $C\,(iR_{\vec e_x}^{\mathrm{axf}})^{T}C^{-1}=-\,iR_{\vec e_x}^{\mathrm{axf}}$ and $C\,(iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}})^{T}C^{-1}=-\,iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ | **Supplied**, recomputed in the cell frame on all $\mu$ |
| The antilinear real structure $\mathcal{C}\psi=K\psi^{*}$: $K=i$, $KK^{*}=L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$, $\mathcal{C}^{2}=1$, $K\,(ic_\mu)^{*}K^{-1}=-\,ic_\mu$ for all $\mu$ | **Supplied**, recomputed on all $\mu$ |
| $\mathcal{C}$ commutes with the kinetic operator, so the constraint is consistent with the massive equation | **Supplied**, through the reality of the cells $c_\mu$ |
| The spectral split into two real four-dimensional eigenspaces, exchanged by $\Gamma$ | **Supplied**, recomputed by elimination |
| Both eigenspaces on the mass shell, $(\Box-m^{2})\psi=0$ | **Supplied**, from the involution and the Clifford square |
| The two-component Weyl operators with $W_RW_L=\Box$ | **Supplied**, recomputed on all sixteen pairs |
| $\Gamma$ as a symmetry of the equation, $\mathbb{D}(\Gamma\psi)=m(\Gamma\psi)^{c}$, and the multiplication by $i$ as carrying $m$ to $-m$ | **Supplied**, from $\Gamma\mathbb{D}=-\mathbb{D}\Gamma$ and $(\Gamma\psi)^{c}=-\Gamma\psi^{c}$ |
| Real cells generating $\mathrm{Cl}_{3,1}\cong M_4(\mathbb{R})$, so that $\mathbb{D}$ is a real operator; the quaternionic type of $\mathrm{Cl}_{1,3}$, hence no real representation of the generators $i c_\mu$ | **Supplied**, recomputed cell by cell |
| The module-level construction of $\mathcal{C}$, the exchange of chiral halves, the identification of $\bar{\cdot}$, the fixed space, the bilinears | **Transcribed** from *The Neutrino and Majorana Fermions in Biquaternionic Form* |
| The two normalisations and the reality types by signature | **Transcribed** from *Real Spinors and Reality Conditions* |
| The neutral spinors and the $\mathrm{Spin}^c$ structure | **Transcribed** from *Antilinear Structure and the Two Kinds of Mass* |
| A selection principle making a fermion Majorana rather than Dirac | **Not supplied**; the choice is empirical |
| The neutrino mass, the Majorana phases, lepton-number-violating rates | **Outside** the algebra |
| The bilinear structure and the mass dimension that distinguish the ELKO spinors | **Outside** the algebra; the eigenstructure alone does not supply them |

## Open Questions

1. **The algebra-level form of the two-component mass term.** The four-component equation is transcribeable into the algebra through the coefficient conjugation $\bar{\cdot}$, as the neutrino article shows. Whether the two-component mass term $m\epsilon(\,\cdot\,)^{*}$ has a representation as a biquaternion-valued operation on the module, in the way the Dirac mass is the linear chiral pair, is not settled here.

2. **Whether the $\pm1$ split has any dynamical content.** The two eigenspaces are isomorphic through $\Gamma$, and the sign of $m$ that separates them is removable, so the split carries no second mass and no second dispersion. Whether a physical selection rule could ever distinguish the two eigenvalues — for instance through a coupling that is odd under the chirality flip — is open, and the eigenstructure alone does not decide it.

3. **The normalisation of the real form.** The irreducible real representation of $\mathrm{Cl}_{3,1}\cong M_4(\mathbb{R})$ is unique up to equivalence, but the frame that realises it is not: $c_\mu$ and $r_\mu$ are two, and the two differ in which cell is antisymmetric. Whether the framework should fix one canonically, in the way it fixes the chiral block decomposition for the complex case, is an authorial decision that belongs with the conventions.

4. **The continuum square root.** The identity $W_RW_L=\Box$ is an operator identity on differentiable fields, and the second-order equation of the two-component form follows from eliminating $\psi_R$ between the two blocks. Whether the pair $(W_L,W_R)$ admits the corresponding functional-analytic treatment — domains, closed extensions, and the sense in which each block is a square root of the d'Alembertian on a Hilbert space — is not treated here; the antilinear $D_L$ is not the object to which a self-adjointness theorem would apply.

5. **Empirical contact.** The decisive experiment is neutrinoless double beta decay, and the framework offers no rate and no prediction. Whether the eigenstructure above can be brought into contact with a rate is open, and is recorded in the neutrino article as an open question of the corpus.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The bracket is the frame, on the generators as on the metric, $\gamma_\mu[\mathbb{M}_-]$ or $\gamma_\mu[\mathbb{B}]$, so that a glyph names a display and not an object of the algebra.

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra.

Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\psi=a\psi$ and $R_b\psi=\psi b$, and $c(M)$ is the coefficient matrix of $M$ in the basis of the sixteen products.

$$
\gamma_0[\mathbb{M}_-]=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\quad \gamma_1[\mathbb{M}_-]=iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_2[\mathbb{M}_-]=iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_3[\mathbb{M}_-]=iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\quad \gamma_5[\mathbb{M}_-]=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}} .
$$

The same in the axis-free display:

$$
\gamma_0[\mathbb{M}_-]=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}},\quad \gamma_1[\mathbb{M}_-]=iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_2[\mathbb{M}_-]=iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_3[\mathbb{M}_-]=iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\quad \gamma_5[\mathbb{M}_-]=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}} .
$$

In the notation of the body the dictionary is one line: $\gamma_\mu[\mathbb{M}_-]=i c_\mu$ and $\gamma_5[\mathbb{M}_-]=\Gamma$. A single product is a pure tensor; the products form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and a general element is a sum of at most four, with $\ell(M)=\operatorname{rank}c(M)$.

$\gamma_5[\mathbb{M}_-]$ is the reference-frame cell of the chirality $\Gamma$; the central grading $\chi=i\tilde\Xi_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi^2=e_t$ — is a different object, represented by $\gamma_5[\mathbb{M}_-]$ on the Dirac module.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The identities the bodies cite.** In the $\gamma$ reading, with $\varepsilon=(1,-1,-1,-1)$ the sign vector of the cells,
$$
\{\gamma_\mu[\mathbb{M}_-],\gamma_\nu[\mathbb{M}_-]\}=2\varepsilon_\mu\delta_{\mu\nu}I_4,\qquad
(\gamma_k[\mathbb{M}_-])^2=-I_4,\qquad
\gamma_5[\mathbb{M}_-]^2=I_4,\qquad
\{\gamma_\mu[\mathbb{M}_-],\gamma_5[\mathbb{M}_-]\}=0,
$$
$$
[\gamma_\mu[\mathbb{M}_-],\gamma_\nu[\mathbb{M}_-]]=2\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-]\quad(\mu\ne\nu),\qquad
[\gamma_a[\mathbb{M}_-],S_{cd}]=\varepsilon_a\delta_{ac}\gamma_d[\mathbb{M}_-]-\varepsilon_a\delta_{ad}\gamma_c[\mathbb{M}_-],\qquad
S_{cd}=\tfrac14[\gamma_c[\mathbb{M}_-],\gamma_d[\mathbb{M}_-]],
$$
$$
\mathrm{tr}(\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-])=4\varepsilon_\mu\delta_{\mu\nu},\qquad
\mathrm{tr}(\gamma_5[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-]\gamma_\rho[\mathbb{M}_-]\gamma_\sigma[\mathbb{M}_-])=-4i\,\epsilon_{\mu\nu\rho\sigma},
$$
$$
\mathrm{tr}(\gamma_\mu[\mathbb{M}_-]\gamma_\nu[\mathbb{M}_-]\gamma_\rho[\mathbb{M}_-]\gamma_\sigma[\mathbb{M}_-])
=4\bigl(\varepsilon_\mu\delta_{\mu\nu}\varepsilon_\rho\delta_{\rho\sigma}
-\varepsilon_\mu\delta_{\mu\rho}\varepsilon_\nu\delta_{\nu\sigma}
+\varepsilon_\mu\delta_{\mu\sigma}\varepsilon_\nu\delta_{\nu\rho}\bigr).
$$
The contraction sums follow from the squares. With one index raised, $\gamma^\mu[\mathbb{M}_-]=-\varepsilon_\mu\gamma_\mu[\mathbb{M}_-]$, so that $\sum_\mu\gamma^\mu[\mathbb{B}]\gamma_\mu[\mathbb{B}]=-4I_4$, $\sum_\mu\gamma^\mu[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-]=2\gamma_\alpha[\mathbb{M}_-]$, $\sum_\mu\gamma^\mu[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]\gamma_\beta[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-]=-4\varepsilon_\alpha\delta_{\alpha\beta}I_4$ and $\sum_\mu\gamma^\mu[\mathbb{M}_-]\gamma_\gamma[\mathbb{M}_-]\gamma_\beta[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]\gamma_\mu[\mathbb{M}_-]=2\gamma_\gamma[\mathbb{M}_-]\gamma_\beta[\mathbb{M}_-]\gamma_\alpha[\mathbb{M}_-]$.
## Summary

The Majorana equation is the relativistic wave equation of a spin-$\tfrac12$ field equal to its own charge conjugate, and it is the Dirac equation with the mass term pairing the field with its conjugate instead of with the other chiral half. In the cell frame with $g=\mathrm{diag}(-,+,+,+)$ its three standard forms were written, and each was identified as one operator, or one reading of it, rather than as a separate equation. The cell operator is $\mathbb{D}=\sum_\mu c_\mu\partial/\partial x_\mu$, built from the four real cells $c_0=R_{\vec e_x}^{\mathrm{axf}}$ and $c_k=L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$, so that $\mathbb{D}^{2}=\Box$ with no sign left over: the two factors of $i$ of each generator are already multiplied to $-1$. The charge-conjugate form uses the real cell $C=R_{\vec e_x}^{\mathrm{axf}}$, for which $C^{T}=-C$, $C^{2}=-L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$, $C\,(iR_{\vec e_x}^{\mathrm{axf}})^{T}C^{-1}=-\,iR_{\vec e_x}^{\mathrm{axf}}$ and $C\,(iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}})^{T}C^{-1}=-\,iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ on all $\mu$, and the antilinear map $\mathcal{C}\psi=K\psi^{*}$ with the central scalar $K=C\,(iR_{\vec e_x}^{\mathrm{axf}})^{T}=i$ satisfies $KK^{*}=L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$, so that $\mathcal{C}^{2}=1$; it anticommutes with each generator cell, $K\,(ic_\mu)^{*}K^{-1}=-\,ic_\mu$, and commutes with $\mathbb{D}$, which is what makes the constraint $\psi^{c}=\psi$ consistent with the massive equation and reduces it to the Dirac equation on the fixed space. The real form needs no new operator: the four cells $c_\mu$ are real and generate $\mathrm{Cl}_{3,1}\cong M_4(\mathbb{R})$, so $\mathbb{D}$ preserves the real subspace on which the charge conjugation is the plain complex conjugation, and the frame $r_\mu$ is the conventional way of writing that same algebra. The corpus's generators $i c_\mu$ are $\mathrm{Cl}_{1,3}\cong M_2(\mathbb{H})$ and admit no real representation, which is why the reality is carried by the antilinear $\mathcal{C}$. The two-component form is the Weyl operator with the antilinear mass term, $i(\partial/\partial t'-\boldsymbol\sigma\cdot\nabla)\psi_L=m\epsilon\psi_L^{*}$ with $\epsilon=i\sigma_2$, and the two Weyl operators satisfy $W_RW_L=\Box$, which is the precise sense in which they are square roots of the Klein–Gordon operator. The charge-conjugation operator is an involution whose two eigenspaces are each of real dimension four: the $+1$ space is the Majorana sector, on which the equation is Dirac, and the $-1$ space carries the opposite sign of the mass, which the chirality cell removes — $\Gamma$ changes sign against the kinetic operator and again against the conjugation, so the two cancel, while the multiplication by $i$ changes it once and reverses the mass — so that $\Gamma$ is an isomorphism between the two and $i$ is not. Both are on the mass shell, $(\Box-m^{2})\psi=0$, which follows from the involution and needs no matrix square. A self-conjugate field carries one Weyl spinor rather than two, no vector current, and no fermion number; whether a given fermion is Majorana, and the neutrino mass and phases, are outside the algebra.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L_a$, $R_b$, $L_aR_b$ | $L_a\psi=a\psi$, $R_b\psi=\psi b$, $L_aR_b\psi=a\psi b$; $L_{e_t}^{\mathrm{axf}}=R_{e_t}^{\mathrm{axf}}=\mathrm{id}$ |
| $c_0=R_{\vec e_x}^{\mathrm{axf}}$, $c_k=L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ | The four real cells, the coefficients of $\mathbb{D}$ |
| $i c_\mu$, $\{ic_\mu,ic_\nu\}=2\varepsilon_\mu\delta_{\mu\nu}L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ | Generator cells and their anticommutation relations |
| $\Gamma=-iR_{\vec e_z}^{\mathrm{axf}}$ | Chirality cell; $-1$ on $S$, $+1$ on $\bar S$, $\Gamma^{2}=L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ |
| $S$, $\bar S$, $\Delta=S\oplus\bar S$ | Chiral halves, $\Gamma=-1$ and $\Gamma=+1$, and the Dirac module |
| $x_0=t'$, $x_k=Q_k$ | The real coordinates in which contractions with derivatives are written |
| $p_\mu=(p_0,p_k)$, $P=p_{0}c_{0}-\sum_k p_{k}c_{k}$ | Momentum, lowered, and the kinetic bracket of the momentum-space equation |
| $u$, $u^{c}=Ku^{*}$ | The two amplitudes of the self-conjugate field $u\,e^{-ip\cdot x}+u^{c}\,e^{+ip\cdot x}$ |
| $\Box=\partial^2/\partial Q_t^2+\Delta=\Delta-(1/c^{2})\partial^{2}/\partial {t'}^{2}$ | d'Alembertian, series convention; $c=1$ in natural units |
| $\mathbb{D}=\sum_\mu c_\mu\partial/\partial x_\mu$ | Kinetic operator of the module, real coefficients, $\mathbb{D}^{2}=\Box$ |
| $\mathbb{D}\psi=m\psi^{c}$ | The Majorana equation |
| $\psi^{c}=C(\psi^{\dagger}\,iR_{\vec e_x}^{\mathrm{axf}})^{T}=i\psi^{*}$ | Charge-conjugate spinor |
| $C=L_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}=R_{\vec e_x}^{\mathrm{axf}}=-\,i(iR_{\vec e_x}^{\mathrm{axf}})$ | Charge-conjugation cell; real, $C^{T}=-C$, $C^{2}=-L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ |
| $C\,(iR_{\vec e_x}^{\mathrm{axf}})^{T}C^{-1}=-\,iR_{\vec e_x}^{\mathrm{axf}}$ and $C\,(iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}})^{T}C^{-1}=-\,iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$ | Preservation of the kinetic term |
| $\mathcal{C}\psi=K\psi^{*}$ | The antilinear real structure |
| $K=C\,(iR_{\vec e_x}^{\mathrm{axf}})^{T}=i\,L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ | Central scalar of the real structure; $KK^{*}=L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ |
| $K\,(i c_\mu)^{*}K^{-1}=-\,i c_\mu$ | $\mathcal{C}$ anticommutes with the generators |
| $K\,c_\mu^{*}K^{-1}=c_\mu$ | $\mathcal{C}$ commutes with $\mathbb{D}$ |
| $\psi^{c}=+\psi$ | Majorana condition; the $+1$ eigenspace, real dimension four |
| $\psi^{c}=-\psi$ | Anti-self-conjugate condition; the $-1$ eigenspace, real dimension four |
| $\mathbb{D}\psi=-m\psi$ | Its equation; $\Gamma$ carries it to $\mathbb{D}(\Gamma\psi)=+m(\Gamma\psi)$ |
| $(\Box-m^{2})\psi=0$ | Common mass shell of both sectors |
| $\mathrm{Cl}_{3,1}\cong M_4(\mathbb{R})$ | Carried by the cells $c_\mu$; real entries, real operator |
| $r_{0},r_{1},r_{2},r_{3}$ | The exhibited real generators, $\{r_{\mu},r_{\nu}\}=2\mathringg_{\mu\nu}[\mathbb{M}_-]L_{e_t}^{\mathrm{axf}}R_{e_t}^{\mathrm{axf}}$ |
| $\sigma_{\mu}=(I_2,-\boldsymbol{\sigma})$, $\bar\sigma_{\mu}=(I_2,+\boldsymbol{\sigma})$ | Weyl vectors, lowered, mostly-minus frame |
| $\epsilon=i\sigma_2$ | Symplectic form; $\epsilon^{T}=-\epsilon$, $\epsilon^{2}=-I_2$ |
| $D_L=W_L-m\epsilon(\,\cdot\,)^{*}$ | Two-component Majorana operator; antilinear, one block of the pair, not a matrix to be squared |
| $W_L=i(\partial/\partial t'-\boldsymbol\sigma\cdot\nabla)$, $W_R=i(\partial/\partial t'+\boldsymbol\sigma\cdot\nabla)$ | Weyl operators; $W_RW_L=\Box$ |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- E. Majorana, "Teoria simmetrica dell'elettrone e del positrone," *Nuovo Cimento* **14** (1937) 171–184, for the original equation and the real form of the Dirac theory.
- C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), Chapter 2 and Appendix A, for the charge-conjugation matrix, the Majorana condition and the conventions used here.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), Chapter 5, for the charge-conjugation operator and its two eigenstates.
- P. B. Pal, "Dirac, Majorana, and Weyl fermions," *American Journal of Physics* **79** (2011) 485–498, for the counting of components and the neutrality of the Majorana field.
- A. Aste, "A direct road to Majorana fields," *Symmetry* **2** (2010) 1776–1809, for the two-component construction and the symplectic group $\mathrm{Sp}(2,\mathbb{C})$ as the double cover of the Lorentz group.
- E. Marsch, "On the Majorana equation: relations between its complex two-component and real four-component eigenfunctions," *ISRN Mathematical Physics* **2012** (2012) 760239, for the two-component and four-component eigenfunctions and their relation.
- P. Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the Lounesto classification and the class-5 (ELKO-type) spinor with the charge-conjugation eigenvalue $-1$.
- D. V. Ahluwalia and D. Grumiller, "Spin-half fermions with mass dimension one: theory, phenomenology, and dark matter," *Journal of Cosmology and Astroparticle Physics* **0507** (2005) 012, for the ELKO spinor and its properties.
- H. B. Lawson and M.-L. Michelsohn, *Spin Geometry* (Princeton, 1989), and P. Budinich and A. Trautman, *The Spinorial Chessboard* (Springer, 1988), for the real, complex and quaternionic types of Clifford modules and the reality of the generators by signature.
