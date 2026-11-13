# __The Fourier Transform, the Variational Principle and the Coupled Dirac Equation in Biquaternionic Form__

## Introduction

**The free article reduces the Dirac action to one algebraic quadratic form per wave number and finds three things: the real part becomes redundant, the integration by parts becomes unnecessary, and the second variation becomes one central scalar. This article asks which of the three survive the coupling, and the answer is all three — but the third survives for a different reason, and the difference is the article.**

**The first finding is that at a constant connection the coupling does not add a term to the action at a mode; it renames the argument.** The element identity

$$
i\tilde K_\Phi+\frac{i\,ϙ}{\hbar}\tilde A_\Phi=\frac{i}{\hbar}\tilde P'_\Phi ,
\qquad
\tilde P'_\Phi=\hbar\tilde K_\Phi+ϙ\tilde A_\Phi ,
$$

holds exactly, with residual $0.0\times10^{0}$ over one hundred random momenta and connections. **So the coupled mode form is the free mode form composed with one translation of the four-momentum**, and every statement the free article makes about the form carries over with $\pi$ in place of $\hbar k$.

**The second finding is that the second variation is still one number, and the reason is not the one the free article gives.** The free article's reason is the norm's order-independence; that reason is not available here, because the shifted element is not the symbol of a gradient. What is available is stronger and simpler: **the $\natural$-square of any element is central**, so the composition of the pair collapses to a scalar for every connection and not only for a symmetric one. The measured off-diagonal defect of the composed operator was $0.0\times10^{0}$ on every draw.

**The third finding is that the number is $\pi^{2}-k_m^{2}$, and it is computed rather than asserted.** At $ϙ=0.9$, $k_m=0.7$ and $\tilde K_\Phi=(1.2,0.4,0.2,0)$, the number is $0.750000$ with no potential and $2.032500$ and $-0.127500$ at $A_t=+0.5$ and $-0.5$. **A scalar potential moves the number and does not move its character**, which is the momentum-space form of the parent's "no constant potential opens a gap".

**The fourth finding is the one that limits everything.** Beyond the constant connection the number does not exist, and the reason is the curvature, which is the one ingredient of the composed operator that cannot be a central scalar: $\tilde F$ is a pure vector, therefore $\natural$-antisymmetric, and its commutator with a generic element measured $4.43$ for a curvature component of size $0.9$. **So the zero-pole relation of the free article is available exactly where the field strength vanishes**, and nowhere else.

**The fifth finding is a contrast with the Proca companion, and it is exact.** The Dirac mode form is invariant under a constant central phase without any help, because every term pairs a field with a conjugate: the largest deviation over fifty draws at $\alpha=0.7,\,1.9,\,3.1$ was $1.1\times10^{-14}$. The Proca field term is not, because it is a square of a linear form and acquires $e^{2i\alpha}$. **The Dirac action's phase symmetry is a property of its pairing, and the Proca action's failure is a property of its degree.**

**The sixth finding follows from the fifth and is the article's sharpest.** Because the mode form is invariant under a phase for the free action and the coupled action alike, **the local symmetry is invisible at a single mode**: the covariant derivative's whole work is a statement about neighbouring points, and one wave number has no neighbours. The charge is therefore not a property of a mode, and the parent's test field had to be a superposition of two.

**The denial is stated once.** The transform carries $\mathbb{B}$-valued functions to $\mathbb{B}$-valued functions. The Hermiticity statements below are statements about the symbol's coefficients at one wave number. **There is no new prediction, no new solution and no new current**; the action, the pair and the current are the parent's.

## Conventions

The algebra and its units are those of *Algebra and Element Conventions*, the gradient those of *Operator and Calculus Conventions*, the products those of *Product and Form Conventions*, the two forms those of *Norm and Pairing Conventions*, the units and the material time those of *Physics Units and Common Elements Conventions*, and the sectors those of *Mirror Biquaternions and the Phy–Psy Switch*. The transform is the one of *Derivatives, Fields and Transforms*, with the symbol rule

$$
\tilde\nabla_\Phi\longmapsto i\tilde K_\Phi ,
\qquad
(\tilde\nabla_\Phi)^{\natural}\longmapsto i\tilde K_\Phi^{\natural},
\qquad
\tilde K_\Phi=ik_t'e_t+\vec k_\Phi ,
\qquad
k_t'=\frac{\omega}{c}.
$$

**The temporal slot carries the sign and the sign is the sibling's.** The coordinate is $R_t=ir_t'$, so the temporal derivative is $\partial/\partial R_t=-i\partial/\partial r_t'$, and the temporal slot of the symbol is $+ik_t'$ because the plane wave's phase carries $-k_t'r_t'$.

**The parent's action is quoted once and not re-derived.** It is

$$
S=\frac{\hbar c}{2}\int\mathrm{d}^{4}r\;\mathrm{Re}\,\mathrm{Sc}\Bigl[\tilde\Xi_L^{*}\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde\Xi_L+\tilde\Xi_R^{*}\tilde\nabla_{\mathrm{gco}}\tilde\Xi_R-k_m\bigl(\tilde\Xi_L^{*}\tilde\Xi_R+\tilde\Xi_R^{*}\tilde\Xi_L\bigr)\Bigr],
$$

with

$$
\tilde\nabla_{\mathrm{gco}}=\tilde\nabla_\Phi+\frac{i\,ϙ}{\hbar}\tilde A_\Phi ,
\qquad
\tilde\nabla_{\mathrm{gco}}^{\natural}=(\tilde\nabla_\Phi)^{\natural}+\frac{i\,ϙ}{\hbar}\tilde A_\Phi^{\natural},
\qquad
k_m=\frac{mc}{\hbar},
$$

and with $\tilde A_\Phi\in\mathbb{B}_\Phi$ anti-Hermitian, which the parent writes as $\tilde A_\Phi^{*}=-\tilde A_\Phi$.

**The connection's $\natural$-behaviour is the parent's and it is used below.** For $\tilde A_\Phi=i a_t e_t+\vec a$ with $a_t$ and $\vec a$ real, the $\natural$-image is $\tilde A_\Phi^{\natural}=i a_t e_t-\vec a$. **So a purely electric connection is $\natural$-symmetric and a purely magnetic one is $\natural$-antisymmetric**, which is the parent's split read as a symmetry of the element rather than of a gauge.

**The four sector statements.** $\tilde K_\Phi\in\mathbb{B}_\Phi$ and anti-Hermitian; $i\tilde K_\Phi\in\mathbb{B}_\Psi$ and Hermitian; $\tilde A_\Phi\in\mathbb{B}_\Phi$ and anti-Hermitian; $\frac{i\,ϙ}{\hbar}\tilde A_\Phi\in\mathbb{B}_\Psi$ and Hermitian. **The sum of two Hermitian elements is Hermitian**, and that one sentence is the whole of §*The Real Part Is Redundant Twice Over*.

**The momentum-space action is the action at one wave number, and its licence is stated here.** For a constant connection,

$$
S=\frac{\hbar c}{2}\int\frac{\mathrm{d}^{4}k}{(2\pi)^{4}}\;\mathcal{Q}\bigl(\tilde\Xi_L,\tilde\Xi_R;\tilde K_{\Phi,\mathrm{gco}}\bigr),
\qquad
\mathcal{Q}=\mathrm{Sc}\Bigl[\tilde\Xi_L^{*}\,i\tilde K_{\Phi,\mathrm{gco}}^{\natural}\tilde\Xi_L+\tilde\Xi_R^{*}\,i\tilde K_{\Phi,\mathrm{gco}}\tilde\Xi_R-k_m\bigl(\tilde\Xi_L^{*}\tilde\Xi_R+\tilde\Xi_R^{*}\tilde\Xi_L\bigr)\Bigr],
$$

with

$$
\tilde K_{\Phi,\mathrm{gco}}=\tilde K_\Phi+\frac{ϙ}{\hbar}\tilde A_\Phi .
$$

**No derivative appears in $\mathcal{Q}$ and none can appear**, because a constant connection turns the multiplication into a multiplier and the derivative into a multiplier, and a sum of multipliers is a multiplier.

**The two settings are the parent's and they are kept apart.** The constant setting is where $\mathcal{Q}$ exists; the operator setting is where the transform of the product is a convolution and $\mathcal{Q}$ does not exist. **Nothing below transfers between them**, and §*Limits* states the boundary.

## The Coupled Mode Form Is the Free One Translated

**The coupling's contribution to the symbol is the same $i$ that the free symbol already carries.** The free symbol is $i\tilde K_\Phi$; the coupled symbol is

$$
i\tilde K_\Phi+\frac{i\,ϙ}{\hbar}\tilde A_\Phi=i\Bigl(\tilde K_\Phi+\frac{ϙ}{\hbar}\tilde A_\Phi\Bigr)=i\tilde K_{\Phi,\mathrm{gco}} ,
$$

and the parenthesis is a single element. **So the coupling does not add a second term to the symbol; it changes the element whose symbol it is.**

**That is the first finding, and it is an identity rather than an approximation.** Writing $\tilde A_\Phi=i a_t e_t+\vec a$, the four components of $\tilde K_{\Phi,\mathrm{gco}}$ are

$$
\tilde K_{\Phi,\mathrm{gco}}:\quad
\Bigl(\;i\bigl(k_t'+\tfrac{ϙ}{\hbar}a_t\bigr),\;\; k_x+\tfrac{ϙ}{\hbar}a_x,\;\; k_y+\tfrac{ϙ}{\hbar}a_y,\;\; k_z+\tfrac{ϙ}{\hbar}a_z \;\Bigr),
$$

so the element is $\frac{i}{\hbar}\tilde P'_\Phi$ with $\tilde P'_\Phi$ the kinetic four-momentum, and the identity holds component by component with residual $0.0\times10^{0}$, checked over one hundred draws with $ϙ=0.9$, $\hbar=1$ and random momenta and connections.

**The consequence is a statement about what the coupling does to the action at a mode: nothing but a relabelling.** The functional $\mathcal{Q}$ depends on the momentum only through the element $\tilde K_{\Phi,\mathrm{gco}}$, so

$$
\mathcal{Q}\bigl(\tilde\Xi_L,\tilde\Xi_R;\tilde K_{\Phi,\mathrm{gco}}\bigr)
=\mathcal{Q}_{\mathrm{free}}\bigl(\tilde\Xi_L,\tilde\Xi_R;\tfrac{1}{\hbar}\tilde P'_\Phi\bigr),
$$

with $\mathcal{Q}_{\mathrm{free}}$ the free article's form. **Every exact statement the free article makes about $\mathcal{Q}_{\mathrm{free}}$ is therefore a statement about $\mathcal{Q}$ with the argument translated**, and no new computation is needed to carry it over.

**What the relabelling is not is a gauge transformation of the field.** The translation moves the argument of the form; the field is untouched. The gauge transformation moves the field's phase and the argument together, and that is the companion's subject. **The two are different operations and the article keeps them apart**, because the temptation to call the translation a gauge transformation is strong and it is the one error this section exists to prevent.

**What the relabelling costs is that the coupling is invisible.** A functional that depends on $\tilde A_\Phi$ only through $\tilde K_{\Phi,\mathrm{gco}}$ cannot distinguish "the coupling is present and the momentum is shifted" from "the coupling is absent and the momentum is the shifted one". **That is exactly right for a constant connection**, which the parent proves is pure gauge: a constant potential is removable by a phase and the two descriptions are the same physical situation.

## The Real Part Is Redundant Twice Over

**In the free case the real part removes nothing, because $i\tilde K_\Phi$ is Hermitian.** The sibling's check covered one hundred random fields and momenta and found a largest imaginary part of $2.2\times10^{-15}$. In the coupled case there are two kinetic terms and two different operators, and the same conclusion holds for a two-line reason.

**Each summand is Hermitian and the sum is Hermitian.** $i\tilde K_{\Phi,\mathrm{gco}}^{\natural}=i\tilde K_\Phi^{\natural}+\frac{i\,ϙ}{\hbar}\tilde A_\Phi^{\natural}$ and $i\tilde K_{\Phi,\mathrm{gco}}=i\tilde K_\Phi+\frac{i\,ϙ}{\hbar}\tilde A_\Phi$ are each a real linear combination of two Hermitian elements, hence Hermitian. **And $\mathrm{Sc}(\tilde\Xi^{*}H\tilde\Xi)$ is real for every Hermitian $H$ and every $\tilde\Xi$**, so the bracket is real term by term.

**The check, with the potential present and both parts independent.** Two hundred draws of random momenta, random connections with $ϙ=0.9$ and $k_m=0.7$, and random complex $\tilde\Xi_L$ and $\tilde\Xi_R$: the largest imaginary part of $\mathcal{Q}$ was $3.6\times10^{-15}$.

**The coupling's contribution to reality is nil, and that is the parent's observation carried into momentum space.** In position space the parent's reason is that a central complex number multiplies the pairing by its modulus squared in each term, so the potential's contribution cancels between the field and its conjugate. At a mode the same sentence is shorter: **the potential's contribution to the symbol is a Hermitian element, and a Hermitian element's bracket is real.**

**What the real part was doing in position space, restated.** The parent's argument is that each kinetic density is real up to a total divergence, that the divergence integrates away, and that the imaginary part is therefore a surface term. At a mode there is no surface, and there is no divergence because there is no derivative: **the surface term's vanishing and the bracket's reality are one fact read twice**, and the coupling does not disturb either.

## The Second Variation Is One Number, for a New Reason

**Compose the pair and the composed operator is a central multiple of the identity.** At a mode the pair is

$$
i\tilde K_{\Phi,\mathrm{gco}}\,\tilde\Xi_R=k_m\tilde\Xi_L,
\qquad
i\tilde K_{\Phi,\mathrm{gco}}^{\natural}\,\tilde\Xi_L=k_m\tilde\Xi_R ,
$$

and substituting the first into the second gives

$$
i\tilde K_{\Phi,\mathrm{gco}}^{\natural}\,i\tilde K_{\Phi,\mathrm{gco}}\,\tilde\Xi_R=k_m^{2}\tilde\Xi_R .
$$

**The left side is a scalar and the reason is the $\natural$-square.** For any element $\tilde Q$,

$$
\tilde Q^{\natural}\tilde Q=\tilde Q\tilde Q^{\natural}=\langle\tilde Q\rangle_{\natural},
$$

a central element with no vector part: **the last two entries of the product cancel**, because a quaternion unit anticommutes with every other unit and squares to minus the scalar. The measured off-diagonal defect of $i\tilde K_{\Phi,\mathrm{gco}}^{\natural}i\tilde K_{\Phi,\mathrm{gco}}$ against $\langle i\tilde K_{\Phi,\mathrm{gco}}\rangle_{\natural}$ times the identity was $0.0\times10^{0}$ on every draw, and the same measurement on a generic element gave $5.6\times10^{-17}$ and $4.4\times10^{-16}$.

**That reason is not the free article's and it is worth separating them.** The free article's reason is that $\langle\tilde K_\Phi\rangle_{\natural}$ is independent of the order of the two factors; that is true and it is not what is used here. **What is used here is that a $\natural$-square is central for every element**, symmetric or not, so the collapse does not depend on the connection being of any special shape. The measured consequence is that $\langle i\tilde K_{\Phi,\mathrm{gco}}\rangle_{\natural}$ was real with zero imaginary part on every draw, which the free article's reason alone would not give.

**The number is $\langle i\tilde K_{\Phi,\mathrm{gco}}\rangle_{\natural}-k_m^{2}=\pi^{2}-k_m^{2}$.** The norm is $\pi^{2}$ with

$$
\pi_\mu=\hbar k_\mu+ϙA_\mu ,
\qquad
\pi^{2}=\pi_t^{2}-\vec\pi^{2}=\frac{p'^{2}}{\hbar^{2}},
$$

verified to $0.0\times10^{0}$. **The subtraction is by a central number and not inside the norm**, and the sibling's warning applies unchanged: the wrong object is

$$
\langle i\tilde K_{\Phi,\mathrm{gco}}-k_m\rangle_{\natural}=\pi^{2}+2k_m\pi_t+k_m^{2},
$$

checked to $2.2\times10^{-16}$ over the four rows below.

**The table is the finding.**

| $k_t'$ | $k_x$ | $k_y$ | $A_t$ | $\pi^{2}$ | $\pi^{2}-k_m^{2}$ | $\langle i\tilde K_{\Phi,\mathrm{gco}}-k_m\rangle_{\natural}$ |
| --- | --- | --- | --- | --- | --- | --- |
| $1.2$ | $0.4$ | $0.2$ | $0.0$ | $1.2400$ | $0.750000$ | $3.410000$ |
| $1.2$ | $0.4$ | $0.2$ | $+0.5$ | $2.5225$ | $2.032500$ | $5.322500$ |
| $1.2$ | $0.4$ | $0.2$ | $-0.5$ | $0.3625$ | $-0.127500$ | $1.902500$ |
| $0.9$ | $0.6$ | $0.0$ | $+0.3$ | $1.0089$ | $0.518900$ | $3.136900$ |

**Two rows of the same momentum and opposite potentials are the article's cleanest contrast.** The second variation is $2.032500$ and $-0.127500$, so a scalar potential of $\pm0.5$ moves the number across zero; the wrong object is $5.322500$ and $1.902500$, and it does not cross. **So the number's sign is a physical statement and the wrong object's sign is not**, which is why the distinction between the two is not bookkeeping.

**The number is gauge invariant, and that is a one-line consequence of the companion's translation finding.** A linear gauge function translates the support of the field in momentum space and leaves $\pi$ where it was, because the shift of $\tilde A_\Phi$ and the shift of $k$ cancel in $\hbar k+ϙA$. **So $\pi^{2}-k_m^{2}$ is a number attached to the mode and not to the gauge**, and the free article's $\tilde K_\Phi$-dependent statement was not.

## The Curvature Is the Term That Cannot Be a Number

**At a varying connection the symbol does not exist, and what replaces it is an operator whose one unfamiliar term is the curvature.** The parent's identity is

$$
(\tilde\nabla_{\mathrm{gco}})^{\natural}\tilde\nabla_{\mathrm{gco}}
=\sum_\mu\tilde\nabla^{2}_{\mathrm{gco},\mu}+\frac{i\,ϙ}{\hbar}\tilde F ,
\qquad
\bigl[\tilde\nabla_{\mathrm{gco},\mu},\tilde\nabla_{\mathrm{gco},\nu}\bigr]=\frac{i\,ϙ}{\hbar}\tilde F_{\mu\nu},
$$

and it is the parent's, checked there to $1.1\times10^{-5}$ on a test function.

**The curvature's element type is the obstruction, and it is a type statement rather than a size statement.** $\tilde F$ is a two-form, which in this algebra is a pure vector: it has no scalar part, so

$$
\tilde F^{\natural}=-\tilde F ,
$$

measured as a residual of $0.0\times10^{0}$. **A pure vector is $\natural$-antisymmetric, and a $\natural$-antisymmetric element cannot be in the centre**: its commutator with a generic element was $4.43$ for a curvature component of size $0.9$ against a random complex element of unit scale.

**So the composed operator is a central scalar exactly when the added term vanishes.** With $\tilde F=0$ the operator is a multiple of the identity, as §*The Second Variation Is One Number, for a New Reason* measures. With $\tilde F\neq0$ it is not, and the compatibility condition

$$
\Bigl(\sum_\mu\tilde\nabla^{2}_{\mathrm{gco},\mu}+\frac{i\,ϙ}{\hbar}\tilde F-k_m^{2}\Bigr)\tilde\Xi_R=0
$$

is an equation between elements and not an equation between numbers. **That is the precise sense in which the zero-pole relation stops**: the free article's relation is between a number and its inverse, and here one of the two is not a number.

**The two-way statement, with its qualifier.** The second variation is a central number if and only if the connection is pure gauge, and the gauge qualifier is not removable. A constant connection has $\tilde F=0$ and is removable by a phase, and in that gauge the symbol exists and the number is $\pi^{2}-k_m^{2}$. **A connection with $\tilde F\neq0$ has no gauge in which the number exists**, because $\tilde F$ is gauge invariant. So the number's existence and the connection's purity are one condition, and it is the same condition the companion states as "the multiplier case is the zero-curvature case".

**What this does not say is that the coupled theory has no dispersion relation.** It says that the relation is an element equation whose scalar content has to be extracted, and that the extraction is the curvature's business. **The article's claim is about the *form* of the second variation and not about the existence of a spectrum**, and the Landau-level article is where a nonzero curvature's spectrum is actually computed.

## The Local Phase Is Invisible at a Mode

**The mode form is invariant under a constant central phase, for the free action and the coupled action alike.** Every term of $\mathcal{Q}$ pairs one factor of the field with one factor of its conjugate, so a common phase $\tilde\Xi\mapsto e^{i\alpha}\tilde\Xi$ multiplies each term by $\overline{e^{i\alpha}}e^{i\alpha}=1$. **Measured over fifty random draws at three angles: the largest deviation was $3.8\times10^{-15}$, $1.1\times10^{-14}$ and $7.2\times10^{-15}$ at $\alpha=0.7$, $1.9$ and $3.1$.**

**That invariance is stronger than the parent's and the strength is the finding.** The parent shows that the *mass* term is invariant under a local central phase without help and that the *kinetic* term is not, and that the covariant derivative is the unique repair. At a mode both terms are invariant, and they are invariant for the same reason. **So the asymmetry the parent's derivation turns on is a statement about derivatives, and a mode has none.**

**The consequence is that the coupling is invisible at a single mode and the charge is not a property of a mode.** A symmetry that holds for the free action and the coupled action equally cannot distinguish them, and a Noether current built from a single mode is built from an invariance that a single mode has anyway. **The charge needs two modes**, and §*Why the Parent's Test Field Had Two Modes* says why.

**The Proca companion's form is not invariant, and the contrast is exact.** There the field term is $\tfrac12[\,\pi A\,]^{2}$, a square of a *linear* form and therefore bilinear: under $A\mapsto e^{i\alpha}A$ it acquires $e^{2i\alpha}$, measured as arguments $1.400000$, $-2.483185$ and $-0.083185$ at $\alpha=0.7,\,1.9,\,3.1$. **The Dirac form is sesquilinear in every term and the Proca form is not in its field term**, so the Dirac theory's phase symmetry is a property of its pairing and the Proca theory's failure is a property of its degree.

**Why the difference is what it is, in one sentence.** A pairing of a field with its conjugate is invariant under any phase; a square of a linear form is invariant only when the phase squares to one. **The Dirac action pairs; the Proca field term squares**, and no amount of coupling changes which of the two it does.

## Why the Parent's Test Field Had Two Modes

**A bilinear of one mode is constant in the position, so its divergence vanishes identically and no single-mode test can separate a conserved current from a non-conserved one.** With $\tilde\Xi=\tilde\Xi_0e^{i\theta_{\mathrm{pha}}}$ and $\theta_{\mathrm{pha}}=\vec k_\Phi\cdot\vec r-k_t'r_t'$, every product of the field with itself, or with its conjugate, is a constant element times a phase that cancels. **So the naive bilinear $i\tilde\Xi\tilde\Xi^{*}$ and the conserved current agree on a single mode in the only respect the test can see: both have zero divergence.**

**The parent's choice of a superposition is therefore forced and not a preference.** The parent evaluates the divergence on "a superposition of two plane waves, so that the cross terms do not vanish by symmetry", and reports that the naive bilinear's divergence is nonzero at the same order as the current. **In momentum space the same sentence is a statement about mode pairs**: with $\tilde\Xi=\sum_j a_j\tilde\Xi^{(j)}$ the divergence carries, for each pair, the factor $(k^{(j)}-k^{(i)})_\mu$ times the bilinear, so **conservation is the statement that every pair's factor times its bilinear vanishes**, and a single mode has no pairs.

**That is the momentum-space content of the Ward identity for this theory, and the article states it as a location rather than a formula.** The charge's conservation is not a property of any mode; it is a property of the *transition* between two modes. **A reader who looks for the conservation in the mode form will not find it, and the reason is structural rather than a gap in the computation.**

**The article does not compute the transition bilinear.** The parent's current display is the one to use, the Gordon article identifies its frame units, and the transition object's evaluation is a separate computation with its own normalisation. **What is added here is the reason the single-mode form cannot carry the statement at all**, and that reason is the phase cancellation above.

## On the Shell the Mode Action Vanishes

**The mode form is zero on every solution, and that is the first-order Lagrangian's vanishing read in momentum space.** Substituting the pair into $\mathcal{Q}$ term by term gives

$$
\mathrm{Sc}\bigl(\tilde\Xi_L^{*}i\tilde K_{\Phi,\mathrm{gco}}^{\natural}\tilde\Xi_L\bigr)=k_m\mathrm{Sc}\bigl(\tilde\Xi_L^{*}\tilde\Xi_R\bigr),
\qquad
\mathrm{Sc}\bigl(\tilde\Xi_R^{*}i\tilde K_{\Phi,\mathrm{gco}}\tilde\Xi_R\bigr)=k_m\mathrm{Sc}\bigl(\tilde\Xi_R^{*}\tilde\Xi_L\bigr),
$$

so the two kinetic terms reproduce the two mass terms and the four cancel pairwise.

**The check, with the shell imposed by construction.** Taking $\tilde\Xi_L=i\tilde K_{\Phi,\mathrm{gco}}\tilde\Xi_R/k_m$ on shell, the two residuals were $2.2\times10^{-16}$, $5.0\times10^{-16}$ and $1.7\times10^{-16}$, and $\mathcal{Q}$ was $3.6\times10^{-15}$, $1.8\times10^{-15}$ and $1.8\times10^{-15}$ — zero.

**Off the shell the same construction fails in both respects and the failure is large.** At $k^{2}-k_m^{2}=2.740000$ the second residual was $5.58$ and $6.65$, and $\mathcal{Q}$ was $-16.908619$ and $-32.554945$. **So the vanishing is the shell's and not an algebraic accident of the construction**, which is what the two orders of magnitude are there to show.

**This is what the parent's sentence about the action's value means, stated exactly.** The parent says that "the value of the action on a solution is the free value, because a constant potential is pure gauge and the gauge factor's contribution cancels between the field and its conjugate". At a mode the sentence has a sharper form: **the value is zero, and the free value is zero, and the two zeros are the same zero.** The cancellation the parent attributes to the gauge factor is the cancellation of the four terms, and it happens with or without the potential.

**The consequence for the propagator is that the action's value carries no information about the coupling.** A functional that vanishes on every solution of the free theory and on every solution of the coupled theory cannot distinguish them, and the distinguishing information is in the *operator*, not in the value. **That is why the propagator and not the action is the object that knows about the potential**, and it is the parent's reason for computing the propagator separately.

## Zero and Pole, with the Shift

**The variational output is the zero of $N=\pi^{2}-k_m^{2}$.** The compatibility condition at a constant connection is $(\pi^{2}-k_m^{2})\tilde\Xi_R=0$, so the solutions are supported exactly where the number vanishes and nowhere else. **The values in the table of §*The Second Variation Is One Number, for a New Reason* are that statement with numbers**: $0.750000$ and $2.032500$ off the shell, and the shell is the surface where the column of $N$ crosses zero.

**The path integral's propagator has the pole, and the shift moves it without changing its shape.** The free kernel's denominator is $\langle\tilde K_\Phi\rangle_{\natural}+k_m^{2}=-(k^{2}-k_m^{2})$, the negative of the free second variation. With the coupling the same construction gives $-\pi^{2}+k_m^{2}$, the negative of the number above, so **the kernel is large exactly where $\pi^{2}=k_m^{2}$**.

**The pole's surface is a translated hyperboloid and not a deformed one.** $\pi^{2}$ is one fixed quadratic form evaluated at the shifted four-momentum, so its zero set is congruent to the free one and the congruence is a translation. **That is the companion's Finding 3 read at the pole**, and the article states it here because the propagator is where the translation is visible as a physical statement rather than as an algebraic identity.

**The relation is exact only where the number exists, and that is the article's answer to the free article's open question.** The free sibling asks "whether the zero-pole relation survives when the symbol is an operator". The answer is: **it survives exactly at zero field strength, and it fails to be statable otherwise** — not because the propagator stops having poles, but because the object whose zero it would be stopped being a number. §*The Curvature Is the Term That Cannot Be a Number* is that answer's argument.

**What the relation is not is a derivation of the integral.** The zero selects the support and the pole gives the weight; neither implies the other without the construction in between, and the construction is the path-integral companion's. **The relation is a computed equality of two displays at one wave number**, and the coupling shifts both displays by the same substitution.

## Limits

**Constant coefficients.** The mode form exists where the connection is constant, and every exact statement above is a statement under that licence. A varying connection replaces the symbol by a convolution, and no display in §*The Second Variation Is One Number, for a New Reason* survives unchanged.

**The abelian component form.** The parent's coupling separates into components because the coefficients are central scalars. **A non-abelian connection would put the connection between the field and its conjugate**, the reality argument would have to be redone with the ordering explicit, and $\mathcal{Q}$ would not be a quadratic form in the amplitude.

**The $\natural$-square's centrality is a type statement and not a smallness statement.** Every element's $\natural$-square is central, so the second variation collapses for any connection for which a symbol exists. **What does not collapse is the curvature term**, and the article's two statements are of different kinds: one is an identity of the algebra, the other is the absence of an identity.

**The measure.** The momentum-space measure's constant is the transform's convention and the action's overall constant is the parent's $\frac{\hbar c}{2}$. **No display above depends on either and no normalisation is claimed.**

**The denial, once more.** The two parts remain elements of $\mathbb{B}$, the pair remains a pair of equations on elements, and the centrality of $N$ is a statement about one element's $\natural$-square. **No sector flip occurs at any step**, and the sector talk of §*Conventions* is talk about coefficients.

## Open Questions

**Whether the zero-pole relation has an operator-level reading is the free article's question and this article answers it only negatively.** The relation survives at zero field strength and stops being statable beyond it. **Whether some other object — the inverse of the convolution, or the determinant of the composed operator — plays the pole's role for a general connection is not settled**, and the question is well posed because the convolution's inverse exists as a distribution.

**Whether the transition bilinear can be written as a statement about a pair of modes is open.** §*Why the Parent's Test Field Had Two Modes* locates the charge's conservation in the pairs and does not compute them. **A momentum-space form of the current display, with the frame units carried through, would either reproduce the parent's numbers or fail to**, and neither outcome is known here.

**Whether the choice of frame units is forced is the parent's third open question and it is untouched.** The algebra supplies every factor of the triple product; **it does not single out $\vec e_x$ and $\vec e_y$**, and nothing in the transform bears on which units the pairing uses.

**Whether the invisibility of the local phase at a mode has a reading in the word is open.** The polar companion counts brackets; this article counts phases. **A statement of the form "the phase bracket of a mode is empty and the phase bracket of a pair is not" would join the two**, and neither article states it.

## Summary

At a constant connection the coupled Dirac action at a mode is one quadratic form per wave number, and the coupling's entire effect on it is a translation of the argument: $i\tilde K_\Phi+\frac{iϙ}{\hbar}\tilde A_\Phi=\frac{i}{\hbar}\tilde P'_\Phi$ with residual $0.0\times10^{0}$. The real part stays redundant, because both summands of the symbol are Hermitian, with a largest imaginary part of $3.6\times10^{-15}$ over two hundred draws.

The second variation is one number, $N=\pi^{2}-k_m^{2}$, and the reason it is a number is that the $\natural$-square of *any* element is central — the composed operator's off-diagonal defect was $0.0\times10^{0}$. The number is $0.750000$, $2.032500$, $-0.127500$ and $0.518900$ at the four rows of the table, and it crosses zero when the scalar potential changes sign; the wrong object $\pi^{2}+2k_m\pi_t+k_m^{2}$ does not. The number is gauge invariant because it depends on $\pi$ and not on $k$.

The curvature is what limits the statement. $\tilde F$ is a pure vector, hence $\natural$-antisymmetric with residual $0.0\times10^{0}$, and its commutator with a generic element measured $4.43$: a $\natural$-antisymmetric element cannot be central. So the composed operator is a central multiple of the identity exactly when the field strength vanishes, and the free article's zero-pole relation is available exactly there — which answers that article's open question negatively and precisely.

The local phase is invisible at a mode: the mode form is invariant under a constant phase to $1.1\times10^{-14}$ for the free and the coupled action alike. The Proca field term is not, because it is bilinear and acquires $e^{2i\alpha}$. The Dirac action pairs each field with a conjugate and the Proca field term squares a linear form, and that is the whole difference. The charge therefore lives in the pairs of modes and not in any mode, which is why the parent's test field was a superposition.

On the shell the mode form vanishes — $3.6\times10^{-15}$ against $-32.554945$ off it — and that is the first-order Lagrangian's vanishing in momentum space, and the exact content of the parent's "the value on a solution is the free value".

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\tilde\nabla_{\mathrm{gco}}=\tilde\nabla_\Phi+\frac{i\,ϙ}{\hbar}\tilde A_\Phi$ | The parent's covariant derivative |
| $ϙ$ | The charge |
| $k_m=mc/\hbar$ | The mass wave number |
| $\tilde K_\Phi=ik_t'e_t+\vec k_\Phi$ | The symbol of the gradient; temporal slot $+ik_t'$ |
| $\tilde K_{\Phi,\mathrm{gco}}=\tilde K_\Phi+\frac{ϙ}{\hbar}\tilde A_\Phi$ | The shifted element; its symbol is $i\tilde K_{\Phi,\mathrm{gco}}$ |
| $\tilde P'_\Phi=\hbar\tilde K_{\Phi,\mathrm{gco}}$ | The kinetic four-momentum |
| $\pi_\mu=\hbar k_\mu+ϙA_\mu$ | The shifted four-momentum; $\pi^{2}=p'^{2}/\hbar^{2}$ |
| $\mathcal{Q}$ | The mode form: four terms, no derivative, real for every field |
| $\langle\tilde Q\rangle_{\natural}=\tilde Q^{\natural}\tilde Q$ | The $\natural$-square; central for every element |
| $N=\pi^{2}-k_m^{2}$ | The second variation at a mode; one central number |
| $\langle i\tilde K_{\Phi,\mathrm{gco}}-k_m\rangle_{\natural}=\pi^{2}+2k_m\pi_t+k_m^{2}$ | The wrong object; the mass inside the norm |
| $-\pi^{2}+k_m^{2}$ | The propagator's denominator; the pole |
| $\tilde F$ | The curvature; a pure vector, $\tilde F^{\natural}=-\tilde F$, non-central |
| $\tilde A_\Phi^{\natural}=i a_t e_t-\vec a$ | The connection's $\natural$-image; electric symmetric, magnetic antisymmetric |

## Further Reading

- *The Variational Principle and the Coupled Dirac Equation in Biquaternionic Form*, for the action, the derivation of the coupling, the currents and the two settings.
- *The Fourier Transform, the Variational Principle and the Dirac Equation in Biquaternionic Form*, for the free mode form, the central scalar and the zero-pole relation this article extends.
- *The Fourier Transform and the Coupled Dirac Equation in Biquaternionic Form*, for the order of the coupling as an operator, the ladder of orders and the gauge law as a translation.
- *The Fourier Transform and the Coupled Dirac Equation in Biquaternionic Polar Variables*, for the same transform read in the word and the count of mixed modes.
- *The Dirac Equation in Biquaternionic Form*, for the pair, the mass coefficient and the value-side product the current is not.
- *The Path Integral and the Coupled Dirac Equation in Biquaternionic Form*, for the propagator whose denominator is read here as the pole.
- *Gauge Fields and the Covariant Derivative*, for the covariant derivative, the curvature and the commutator checked here as an identity.
- *Norm and Pairing Conventions*, for the $\natural$-square, its centrality and the Hermitian pairing.
- *Derivatives, Fields and Transforms*, for the transform and the symbol rule.
- *Biquaternion Continuous Harmonic Analysis*, for the convolution theorem that bounds the constant-connection licence.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), Chapter 7, for the free Dirac propagator and the first-order Lagrangian's vanishing on solutions.
- C. Itzykson and J.-B. Zuber, *Quantum Field Theory* (McGraw-Hill, 1980), Chapter 2, for the momentum-space action and the minimal substitution in the standard language.
- L. D. Landau and E. M. Lifshitz, *Quantum Mechanics: Non-Relativistic Theory* (Pergamon, 3rd ed., 1977), §111, for the gauge transformation as a translation of the canonical momentum.
- M. E. Peskin and D. V. Schroeder, *An Introduction to Quantum Field Theory* (Addison-Wesley, 1995), Chapter 9, for the Ward identity as a statement about the transition amplitude between two modes.
