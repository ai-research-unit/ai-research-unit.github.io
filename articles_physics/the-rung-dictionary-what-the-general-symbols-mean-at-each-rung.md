# __The Rung Dictionary: What the General Symbols Mean at Each Rung__

## Introduction

**The category's articles are general, and the worked case is usually the scalar.** That is not a defect — a general statement needs a first column — but it leaves a reader unable to tell, from a general article alone, what its symbols denote at the other four rungs. This page is the one table that answers the question. It is the companion of the five-by-five matrix in [Five Steps from a Lagrangian to Fluid Equations](five-steps-from-a-lagrangian-to-fluid-equations.html): **that matrix is the fluid side, read across as five steps; this table is the object side, read across as five columns of one symbol.**

**What the table is for, in three uses.**

1. **A general article says which column it works.** *"The scalar column is worked here; the other columns are in the dictionary"* is a complete scope sentence, and it is the sentence the one-carrier articles of this category were missing.
2. **A reader substitutes a rung.** Take any general display, replace each symbol by its row entry at the rung of interest, and the display either parses or fails. The failure is the information: it names the object the rung does not have.
3. **A new Lagrangian is placed.** A sixth column is filled by answering the same ten rows, and a row that cannot be filled is the rung's obstruction — the way the Proca rung cannot fill the "unconstrained momentum" row and the matrix rung cannot fill the "base-valued flow" row.

**What the table is not.** It is not a derivation and it does not replace the band articles. **The entries state the *kind* of object each symbol denotes, not its formula**; the formulas live in the articles the last row names. A reader who wants the Klein–Gordon conjugate momentum in closed form goes to *Hamiltonian Field Theory in Biquaternionic Form*; a reader who wants to know what "the conjugate momentum" means at the Dirac rung reads the fourth column below.

## The Table

| symbol | Schrödinger | Klein–Gordon | Dirac | Proca | $\mathrm{SU}(4)$ |
|---|---|---|---|---|---|
| **the field (S2's word)** | $\varrho e^{i\theta}\varepsilon e_t$ | $\varrho e^{i\theta}\varepsilon e_t$ | $\varrho e^{i\theta}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ | $\varepsilon i\varrho\tilde U_{\Psi,\mathrm b}$ | $U_{\mathrm{frm}}PU_{\mathrm{frm}}^{\dagger}$ |
| **the invariant density** | $\lVert\tilde\Xi\rVert^{2}$; in the word, $2r^{2}\cosh\theta_{\mathrm{rpd}}$ | $\lVert\tilde\Xi\rVert^{2}$ | $\tilde\Xi^{\dagger}\tilde\Xi$: scalar part the number density, the rest the spin density | $\sum_{\imath}\varepsilon_{\imath}A^{*}_{\imath}A_{\imath}$ | the four eigenvalues $\rho_{1},\dots,\rho_{4}$ of $P$ |
| **the flow** | $\vec\nabla_\Phi S/m$, a gradient | $\partial_{\imath}S/m$, a four-gradient | the frame's direction, transported by the rotor | the direction $u_{\imath}=A_{\imath}/\varrho$ | the internal $\Omega_{\imath}=U_{\mathrm{frm}}^{\dagger}D_{\imath}U_{\mathrm{frm}}$ |
| **the conjugate momentum** | $i\tilde\Xi^{*}$: no independent momentum | $\pi=\left(\partial\xi/\partial r'_t\right)^{*}$, an independent field | the first-order bilinear; $\pi-i\tilde\Xi^{\dagger}\approx0$ is a constraint | $\pi^{0}=0$; $\pi^{\imath}=-F^{0\imath*}$, three independent components | $\Pi=\left(D_{t}\Xi\right)^{\dagger}$ in the matter directions; the connection's momenta constrained |
| **the Legendre transform** | vanishing Hessian; the kinetic matrix replaces it | regular on the pair $(\xi,\pi)$ | vanishing Hessian; first order throughout | rank three of four: one primary constraint | regular in the matter directions, singular in the fifteen connection directions |
| **the constraint count** | none; the four momenta $p_{r},p_{\theta_{\mathrm{rpd}}}$ vanish | none | eight second-class: four degrees of freedom | two second-class: three degrees of freedom | fifteen first-class: fifteen degrees of freedom |
| **the bracket** | the canonical bracket on $(\tilde\Xi,i\tilde\Xi^{*})$ | the field Poisson bracket, integrated over space | the Dirac bracket, then the anticommutator | the Dirac bracket on the constrained surface | the bracket with the trace pairing, projected by the Gauss laws |
| **the pressure** | $p(\rho_{\mathrm{num}},\beta)$ | $p(\rho_{\mathrm{num}},\beta)$ | the trace of the stress; the spin part is separate | the trace of the stress; the polarization part is separate | $\mathrm{Tr}$ of the matrix stress |
| **the chemical potential** | $\mu_{\mathrm{chm}}=-\partial_{t'}S$ | $\mu_{\mathrm{chm}}=-\partial_{t'}S$ | $\mu_{\mathrm{chm}}$ plus the spin potential | $\mu_{\mathrm{chm}}$ plus the polarization potential | four, one per diagonal phase of $\mathrm{U}(1)^{4}$ |
| **the independent thermal data** | $(\rho_{\mathrm{num}},\beta)$ | $(\rho_{\mathrm{num}},\beta)$ | density, spin polarization, $\beta$ | density, polarization, $\beta$ | four densities, the frame, $\beta$ |
| **the force slot** | Euler, with the quantum force | Euler, with $\gamma^{-1}$ | the spin fluid's acceleration | Euler, projected onto two components | a momentum balance; the commutator, not a contraction |
| **the pairing** | $\mathrm{Sc}(\tilde Q^{*}\tilde Q)$ | $\mathrm{Sc}(\tilde Q^{*}\tilde Q)$ | the spinor form $\tilde\Xi^{\dagger}\tilde\Xi$ | the vector form $\sum_{\imath}\varepsilon_{\imath}A^{*}_{\imath}A_{\imath}$ | $\mathrm{Tr}$ |
| **where it is computed** | *Schrödinger fluid equations* | *Klein–Gordon fluid equations* | *Spin-half fluid equations* | *Charged spin-one fluid equations* | *The $\mathrm{SU}(4)$ Fluid Equations from the Primordial Action* |

**Read a row and the rungs differ; read a column and it is one rung's data.** The two hardest rows are the two ends. **The flow row fails at the matrix rung for the reason S5 records**: the flow is internal, so it is a connection and not a velocity, and what the row's substitution produces is a balance. **The conjugate-momentum row fails at the Dirac and Proca rungs for the reason the Dirac–Bergmann algorithm records**: there is no unconstrained momentum to write, and what replaces it is a constraint plus a Dirac bracket.

## How a General Article Uses the Table

**A universal article** — one whose stated result contains no carrier — uses the rows as definitions and needs no column. The invariant-density article is the model: the three requirements it states are requirements on the *pairing*, and the pairing row is filled differently at each rung without the requirements changing.

**A one-carrier article** states its column and points here. *"The scalar column is worked here"* is accurate for the Hamiltonian, the Wigner function and the thermal state, and it is the sentence that turns an honest limitation into a usable general article.

**An article that is a column by design** says so in its own title or first paragraph, and the table's last row points the reader to it. The two-fluid model, the spin fluid and the Frenkel condition are in this class; they are not failures of generality, they are columns.

**An article whose condition is a declared class** — a gauge connection, a spin-carrying fluid, a one-mode truncation, two dimensions — is general over that class, and the table does not apply to it row by row. The condition is the article's, and the dictionary does not override it.

## What the Table Does Not Decide

**It does not supply the matrix rung's thermodynamics.** The row entries name four densities, a frame and four potentials, and naming them is not an equation of state. **The matrix state's dynamics — how the four densities and the frame respond to a temperature — is a research problem and this table does not solve it.** It makes the problem visible, which is the reason the thermal section needs the table: the one-component articles can now say *which* column they are, and the matrix column is seen to be open rather than covered.

**It does not unify the Proca and Dirac spin.** The two rows carry a polarization, and the two polarizations are not the same representation: the Dirac one is the rotor's, the Proca one is the vector's. A reader who copies the spin-half potential into the vector column gets an object of the wrong type, and the row's wording is what prevents the copy.

**It does not decide which groups the algebra contains.** The density row is available for any compact group whose generators can be traced; whether $\mathbb{B}$ *contains* the group is the ceiling question, stated in [The Invariant Density](the-invariant-density-which-pairing-the-action-can-integrate.html) and not answered here.

**It does not fix the coefficients.** The entries are kinds; the normalisations, the signs and the factors of $2\pi$ are the band articles' and are cited in the last row.

## Summary

The category's general statements are read at five rungs, and the dictionary is the one table that says what each symbol denotes at each. **Its three uses are the scope sentence, the substitution test and the placement of a new column; its three limits are the matrix thermodynamics, the two spin representations and the group-content question.** The table makes the category's scalar default a visible column rather than an unstated one, and it gives every band slot a common target.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\varrho$, $\theta$ | the word's amplitude and phase, S2's parameters |
| $\tilde U_{\Psi,\mathrm b}$, $\tilde u_{\mathrm r}$ | the rotor and the direction of the spinor word |
| $U_{\mathrm{frm}}$, $P$ | the frame of the matrix word and its diagonal density |
| $\rho_{\mathrm{num}}$ | the proper density, $\lVert\tilde\Xi\rVert^{2}$ at the central rungs |
| $\Omega_{\imath}$ | the matrix rung's internal flow, $U_{\mathrm{frm}}^{\dagger}D_{\imath}U_{\mathrm{frm}}$ |
| $p(\rho_{\mathrm{num}},\beta)$ | the thermal pressure of the one-component column |
| $\mu_{\mathrm{chm}}$ | the chemical potential, $-\partial_{t'}S$ |
| $\mathrm{Tr}$ | the trace pairing of the matrix rung |

## Further Reading

- [Five Steps from a Lagrangian to Fluid Equations](five-steps-from-a-lagrangian-to-fluid-equations.html), companion article, for the same five columns read as five steps.
- [The Invariant Density: Which Pairing the Action Can Integrate](the-invariant-density-which-pairing-the-action-can-integrate.html), companion article, for the pairing row's derivation and the group-content question.
- [Hamiltonian Field Theory in Biquaternionic Form](hamiltonian-field-theory-in-biquaternionic-form.html), companion article, for the conjugate-momentum and Legendre rows, with the scalar column worked.
- [The Dirac–Bergmann Algorithm: First- and Second-Class Constraints](the-dirac-bergmann-algorithm-first-and-second-class-constraints.html), companion article, for the constraint-count row at the five rungs.
- [The Chemical Potential Is the Phase's Frequency](the-chemical-potential-is-the-phases-frequency.html), companion article, for the chemical-potential row and the four matrix potentials.
- [The Local Thermal State of a Fluid](the-local-thermal-state-of-a-fluid.html), companion article, for the thermal-data row's scalar column.
