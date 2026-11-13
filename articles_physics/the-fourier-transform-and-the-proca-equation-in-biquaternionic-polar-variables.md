# __The Fourier Transform and the Proca Equation in Biquaternionic Polar Variables__

## Introduction

**The Proca word has four parameters and two brackets, and one of its four bracket slots is empty.** *The Proca Equation in Biquaternionic Polar Variables* decomposes the potential as $\tilde A_\Phi=\varepsilon i\,r\,\tilde U$ on the timelike branch and as $\tilde A_\Phi=r\,\tilde U\,\hat u$ on the spacelike one, computes the logarithmic derivative, and tabulates four bracket slots: the scale, which is real central; the phase, which **vanishes identically on both branches**; the frame's rapidity, which is a Hermitian vector; and the frame's axis, which is a real vector. It then says the sentence that organises everything: in the material sector there is no central bracket, so there is no phase gradient, no guidance equation, and no Madelung pair.

**In frequency space that empty slot has a name, and the name is parity.** The Proca symbol is even in the four-wave-number; the Dirac symbol is odd; the Klein–Gordon scalar is even; the Schrödinger symbol is neither. **An odd symbol is what a phase bracket can live in and an even one has no room for it**, and that is the article's first finding. The parent's bracket table and the symbol's parity table are one table read in two registers.

**The second finding is that the branch is not a spectral property at all.** The sign of $\langle\tilde A_\Phi\rangle_\natural$ is an indefinite quadratic form on the amplitudes, not a linear functional of the mode coefficients. Two lightlike modes can sum to a timelike one; the invariant of a sum is not the sum of the invariants. **So no function of the spectrum determines which branch a field is on**, and the chart's piecewiseness cannot be read off the transform's support.

**What the transform does with the piecewiseness is relocate it.** The parent shows that the word is piecewise in spacetime, because the sign of the invariant varies from event to event. Mode by mode it is not: a Fourier mode is a constant frame, so every mode sits strictly inside one branch. **The transform does not remove the branch structure; it moves it from spacetime to the space of amplitudes**, where its boundary is the cone $\langle A\rangle_\natural=0$.

**That cone is the corpus's own object.** *Degenerate Solutions of the Biquaternionic Proca Equation* proves that $\langle\tilde A_\Phi\rangle_\natural=0$ is **one real equation on four real parameters** on the material sector, and that its solution set is a cone with a sector label $\Sigma_{01}$. The same equation on the amplitudes gives the same cone. **The chart's failure set on the field and the branch's boundary on the amplitudes are one variety**, and §*The Chart's Failure Set Is the Amplitude Cone* states the identity.

**The denial is stated plainly.** The transform acts on $\mathbb{B}$-valued functions and returns $\mathbb{B}$-valued functions. No sector is exchanged, no field changes its type, and the word is not reconstructed from its transform. **There is no new solution and no new equation**; the word, the brackets and the two branches are the parent's.

## Conventions

The algebra, the products, the two forms, the units and the sectors are those of *Algebra and Element Conventions*, *Product and Form Conventions*, *Norm and Pairing Conventions*, *Physics Units and Common Elements Conventions* and *Mirror Biquaternions and the Phy–Psy Switch*. The gradient and the d'Alembertian are those of *Operator and Calculus Conventions*, and the transform is the one of *Derivatives, Fields and Transforms*, with the symbol rule

$$
\tilde\nabla_\Phi\longmapsto i\tilde K_\Phi ,
\qquad
\tilde K_\Phi=ik_t'e_t+\vec k_\Phi ,
\qquad
k_t'=\frac{\omega}{c},
\qquad
k^{2}=k_t'^{2}-\vec k_\Phi^{2}.
$$

The word and its parameters are the parent's:

$$
\text{timelike:}\quad \tilde A_\Phi=\varepsilon\,i\,r\,\tilde U ,
\qquad
\text{spacelike:}\quad \tilde A_\Phi=r\,\tilde U\,\hat u ,
\qquad
\tilde U=\exp\Bigl(i\frac{\theta_{\mathrm{rpd}}}{2}\hat u_{\mathrm b}\Bigr) ,
$$

with $r\ge0$ the scale, $\varepsilon=\pm1$ the branch label, $\theta_{\mathrm{rpd}}\ge0$ the rapidity, $\hat u_{\mathrm b}$ the boost axis and $\hat u$ a real unit vector. The parent's bracket table is quoted and not re-derived:

| bracket | type | timelike branch | spacelike branch |
| --- | --- | --- | --- |
| scale | real central scalar | $\partial_\mu\ln r$ | $\partial_\mu\ln r$ |
| phase | central imaginary | $0$ identically | $0$ identically |
| frame, rapidity part | Hermitian vector | $\tfrac12\partial_\mu\theta_{\mathrm{rpd}}\,i\hat u_{\mathrm b}$ | $-\tfrac12\partial_\mu\theta_{\mathrm{rpd}}\,i\hat u$ |
| frame, axis part | real vector | $\sinh^{2}\frac{\theta_{\mathrm{rpd}}}{2}\,\hat u_{\mathrm b}\partial_\mu\hat u_{\mathrm b}$ | $-\hat u\,\partial_\mu\hat u$ and the conjugated rapidity term |

**The invariant is the only one the field carries.** $\langle\tilde A_\Phi\rangle_\natural=-(a_t')^{2}+\vec A^{2}$, real and indefinite, and the two branches are its two signs. On a mode the same number is $\langle A\rangle_\natural=-\lvert a_t'\rvert^{2}+\lvert\vec a\rvert^{2}$, an indefinite quadratic form on the amplitude. **Everything the article says about the branch is a statement about that form.**

**The symbol, quoted from the form companion.** The Proca operator's symbol in the four-component reading is $\sigma^\mu{}_\nu=(k^{2}-k_m^{2})\delta^\mu{}_\nu-k^\mu k_\nu$, acting on the amplitude by $(\sigma A)_\mu=(k^{2}-k_m^{2})A_\mu-k_\mu[kA]$ with $[kA]=k_t'a_t'-\vec k_\Phi\cdot\vec a$. Its eigenvalues are $\{k^{2}-k_m^{2},k^{2}-k_m^{2},k^{2}-k_m^{2},-k_m^{2}\}$. **The chart reading is a decomposition of this matrix into the four types, and the decomposition is the section that follows.**

**The denial of the Legendre reading, once.** The parent's chart is a chart of the field, and the transform's variable is not one of its parameters. The corpus has a second conjugacy — the polar variational parent's canonical momenta, four of which vanish — and it is a Legendre conjugacy, not a Fourier one. **§*Limits* records the distinction and the article uses it nowhere else.**

## The Brackets Are the Types of the Symbol

**The chart's bracket slots and the symbol's parts are the same slots, and the symbol fills two of the four.** A general element of $\mathbb{B}$ splits into a real central part, an imaginary central part, a Hermitian vector part and an anti-Hermitian vector part, and the polar word's four brackets are the gradients of the four parameters that generate those parts. The Proca symbol splits the same way, and only two of the four parts are non-zero:

$$
\sigma=\underbrace{\bigl(k^{2}-k_m^{2}\bigr)\delta^\mu{}_\nu}_{\text{scalar part: the scale slot}}
\;-\;\underbrace{k^\mu k_\nu}_{\text{rank-one part: the frame slot}} ,
\qquad
\text{imaginary central part}=0 ,
\qquad
\text{anti-Hermitian vector part}=0 .
$$

**The first part is the scale and the second is the frame.** The scalar part multiplies every amplitude direction by the same number, which is what the parent's scale bracket does when it is differentiated; the rank-one part carries every amplitude onto a multiple of the wave number, which is what the frame bracket does when it transports the boost axis. The correspondence is a correspondence of decompositions and not an analogy.

**On the material sector the imaginary central slot is empty, and that is the parent's whole point.** The material potential is $\tilde A_\Phi=i\,a_t'e_t+\vec A$ with real coefficients, and the polar word's parameter count is four: the scale, the rapidity, the boost axis and the spacelike direction. **Four parameters, four components, and no angle among them** — which is the parent's "the same eight parameters would be four redundant", read as a statement about which slots the carrier can fill.

**In frequency space the empty slot is not an absence of a coefficient but a symmetry of the matrix.** The symbol has no imaginary central part for a free Proca field, because $k^{2}-k_m^{2}$ and $k^\mu k_\nu$ are both real. **The matrix is real, so it commutes with complex conjugation, and a real matrix cannot generate a phase** — which is the algebraic form of the parent's sentence that the material sector "loses the phase".

**What replaces the phase is the frame, and the symbol carries it in its vector part.** The parent's third and fourth rows — the rapidity's Hermitian vector and the axis's real vector — are the two vector types of the symbol. **So the chart's positive content is the symbol's vector part and its negative content is the symbol's missing central slot**, and the next section makes the negative content a measurement.

## The Absent Phase Is the Even Symbol

**A symbol that generates a phase must be odd in the wave number, and the Proca symbol is even.** Take the four theories and measure $\sigma(-\tilde K_\Phi)$ against $\sigma(\tilde K_\Phi)$ on the same wave number, $k_t'=1.2$ with $\vec k_\Phi=(0.3,0.2,0.1)$:

| theory | object | parity | measured |
| --- | --- | --- | --- |
| Proca | $\sigma^\mu{}_\nu$ | even | $\lvert\sigma(-K)-\sigma(K)\rvert=0.00\times10^{0}$ |
| Klein–Gordon | $k^{2}-k_m^{2}$ | even | $\lvert\sigma(-K)-\sigma(K)\rvert=0.00\times10^{0}$ |
| Dirac | $i\tilde K_\Phi-k_m$ | odd | $\lvert\sigma(-K)+\sigma(K)\rvert=2k_m=1.400000$ |
| Schrödinger | $-\hbar\omega-h_t$ | neither | $\lvert\sigma(-\omega)+\sigma(\omega)\rvert=2h_t=1.000000$ |

**The odd entries are twice the constant term, and that is the table's arithmetic.** The measure of an odd part is $\lvert\sigma(-K)-\sigma(K)\rvert$, which for the Dirac symbol is $2k_m$ and for the Schrödinger symbol $2h_t$: hence $1.400000$ and $1.000000$ at $k_m=0.7$ and $h_t=0.5$. **So the table's second and third rows differ from the first two by a factor and not by a principle**: an odd symbol's reflection doubles its constant term, and an even symbol's reflection cancels its whole value.

**The table is the article's first finding and it is one line of algebra behind each entry.** The Proca and Klein–Gordon symbols are quadratic in $k$; the Dirac symbol is linear; the Schrödinger symbol is affine. **An even symbol is invariant under the reflection $k\mapsto-k$, and a phase bracket is precisely a quantity that changes sign under that reflection**, so the material sector cannot carry one.

**The correspondence with the parent's table is exact and it is slot by slot.** The parent's phase row is zero on both branches; the symbol's imaginary central slot is zero for every wave number. The parent's frame rows are the vector parts; the symbol's vector part is the rank-one piece. **The chart reads the matrix's types; the parity reads the matrix's order; and the two readings agree because a real second-order symbol has no odd slot to fill.**

**This is why the Dirac chart carries a phase and the Proca chart does not, and the reason is not the spin.** The Dirac operator is first order and its symbol is odd, so a central imaginary coefficient is available and the guidance equation follows from it. The Proca operator is second order and its symbol is even, so no such coefficient exists and no guidance equation can be written. **The difference between the two charts is the order of the operator and not the representation that carries it**, and the article says so because the parent's contrast is sometimes read as a statement about spin.

## The Branch Is Not a Spectral Property

**The branch label is an indefinite quadratic form on the amplitudes, and a quadratic form is not a linear functional.** The invariant $\langle A\rangle_\natural=-\lvert a_t'\rvert^{2}+\lvert\vec a\rvert^{2}$ is homogeneous of degree two in the amplitude, so it does not distribute over a superposition:

$$
\langle A+B\rangle_\natural=\langle A\rangle_\natural+\langle B\rangle_\natural+2\,\mathrm{Re}\,[A,B]_\natural ,
\qquad
[A,B]_\natural:=-a_t'(A)a_t'(B)+\vec a(A)\cdot\vec a(B) ,
$$

and the cross term is not zero in general. **Measured on two timelike amplitudes $c=(2,0.1,0,0)$ and $d=(2,-0.1,0,0)$: $\langle c\rangle_\natural=\langle d\rangle_\natural=+3.99$ but $\langle c+d\rangle_\natural=+16.00$ against $\langle c\rangle_\natural+\langle d\rangle_\natural=+7.98$.**

**The boundary of the branch is a cone and not a subspace.** Two lightlike amplitudes can sum to a timelike one and differ to a spacelike one: for $a=(1,1,0,0)$ and $b=(1,-1,0,0)$ both invariants vanish, while $\langle a+b\rangle_\natural=+4.0$ and $\langle a-b\rangle_\natural=-4.0$. **So the lightlike set is closed under scaling and not under addition**, and no linear functional can vanish on it without vanishing on everything.

**The consequence for the transform is immediate and negative.** A field is a superposition of modes, and each mode has its own amplitude. The branch of the field at an event is the sign of the invariant of the *sum*, which is not determined by the branches of the summands. **So the chart's piecewiseness is not a property of the spectrum**, and an article that read a branch label off the support of the transform would be reading a quantity the support does not carry.

**What the transform does carry is the bracket structure.** The scale and the frame are first-order objects, and their gradients are the symbols; the branch is a second-order object, and its gradient is nothing. **The parent's bracket table is therefore a table of first-order data, and the branch label sits outside it** — which is why the parent tabs it separately, as a sign of an invariant, and not as a fifth bracket.

## The Chart's Failure Set Is the Amplitude Cone

**The parent's failure set and the branch's boundary are one equation.** The chart fails where the local four-vector is lightlike, and on the material sector that is

$$
\langle\tilde A_\Phi\rangle_\natural=-(a_t')^{2}+\vec A^{2}=0 ,
$$

which *Degenerate Solutions of the Biquaternionic Proca Equation* proves is **one real equation on four real parameters**, cutting the four-dimensional material sector to a three-dimensional cone. On a mode the same display reads $-\lvert a_t'\rvert^{2}+\lvert\vec a\rvert^{2}=0$, which is the same cone in the amplitude space.

**The codimension is one in both readings and for the same reason.** In the algebra $\langle\tilde Q\rangle_\natural=0$ is complex and costs two real conditions; on the material sector the coefficients are real and it costs one. **On the amplitudes the coefficients are also real for a material field, so the same halving applies**, and the cone has codimension one in the amplitude space as well.

**The parent's sector label transfers with the cone.** *Degenerate Solutions* shows that a lightlike material potential satisfies $\tilde A_\Phi^{2}=\lambda\tilde A_\Phi$ with $\lambda=2i a_t'$, so it lies in $\Sigma_{01}$ and not in $\Sigma_{00}$, and that the trace $2i a_t'$ is what decides. **The amplitude cone carries the same label**, and it does so for the same reason: the trace of a pure vector vanishes identically, so the field strength's cone is $\Sigma_{00}$ and the potential's is $\Sigma_{01}$.

**What the transform adds here is only the location.** The parent's cone is a set of field values in spacetime; on a mode it is a set of amplitudes at one wave number. **The equation is unchanged and the variety is unchanged; what changes is that the cone is now a condition on the coefficients of a superposition rather than on the value of a field at an event**, and that is why §*The Branch Is Not a Spectral Property* can be stated as a fact about quadratic forms.

**The failure set is larger than the scalar chart's and the transform does not shrink it.** The parent records that in the scalar case the chart fails where $r=0$, a codimension-two set in spacetime, while here it fails on the whole light cone of field values, a family of three-dimensional surfaces. **In amplitude space the two are a point and a cone**, and the transform preserves the distinction: a point is a point and a cone is a cone.

## What the Transform Does to Piecewiseness

**A Fourier mode is a constant frame, so every mode sits strictly inside one branch.** The parent's plane-wave section makes this explicit: for $\tilde A_\Phi=\tilde A_0\cos\theta_{\mathrm{pwp}}$ with a constant timelike $\tilde A_0$, the word is $r=\lvert\cos\theta_{\mathrm{pwp}}\rvert\sqrt{-\langle\tilde A_0\rangle_\natural}$, a constant $\tilde U_{\mathrm b}$, and $\varepsilon=\mathrm{sign}\cos\theta_{\mathrm{pwp}}$. **The boost is fixed by the amplitude, the whole spacetime dependence sits in the scale, and the branch label flips only at the nodes.**

**The transform's support sees the scale and not the flip.** A plane wave's transform is supported at one wave number with an amplitude, and the amplitude's invariant sign is the branch. The node where $\varepsilon$ flips is a zero of the scale and a feature of the *superposition*, not of the mode. **So the chart's failure on the nodal surfaces is invisible to each mode and visible only in their sum**, which is the precise sense in which the transform relocates the piecewiseness.

**The relocation is a gain and it is bounded.** The gain: the branch becomes a property of an amplitude, so it can be discussed without reference to a spacetime point, and the amplitude cone is a fixed algebraic object. The bound: the branch of a *field* is the branch of the sum, which §*The Branch Is Not a Spectral Property* shows is not determined by the summands. **Both statements are needed and neither is the whole story.**

**What would be needed to recover the piecewiseness is a statement about the phase of the superposition.** Two modes of different wave numbers superpose with a relative phase, and the invariant of the sum depends on it. **The transform keeps both amplitudes and both phases, so the data are present; what is absent is a linear functional that reads the branch from them**, and the article states the absence rather than constructing a nonlinear one.

## The Lorenz Condition in the Chart on a Mode

**The parent's divergence display becomes one algebraic equation on a mode.** The parent writes

$$
S=\varepsilon\Bigl[c\,\frac{\partial r}{\partial r'_t}-s\,\hat u_{\mathrm b}\cdot\nabla r
+\tfrac12 rs\,\frac{\partial\theta_{\mathrm{rpd}}}{\partial r'_t}-\tfrac12 rc\,\hat u_{\mathrm b}\cdot\nabla\theta_{\mathrm{rpd}}-rs\,\nabla\cdot\hat u_{\mathrm b}\Bigr]=0 ,
$$

with $c=\cosh\frac{\theta_{\mathrm{rpd}}}{2}$ and $s=\sinh\frac{\theta_{\mathrm{rpd}}}{2}$, and observes that the first two terms are $\partial_{r'_t}(\varepsilon rc)$ and the last three are $-\nabla\cdot(\varepsilon rs\hat u_{\mathrm b})$. **On a mode every derivative becomes a multiplication**, so the display collapses to

$$
[kA]=k_t'a_t'-\vec k_\Phi\cdot\vec a=0 ,
$$

which is one linear condition on the four amplitudes and it is the Lorenz plane.

**It is the same plane as the symbol's kernel, named in the chart's letters.** The form companion computes the kernel of $\sigma$ on the shell and finds it three-dimensional and annihilated to $3\times10^{-17}$; here the same plane is written as the vanishing of the divergence. **Two computations, one plane**: the kernel is what the operator does not see, and the Lorenz condition is what the field must satisfy. That they coincide is the content of "the constraint is implied and not imposed", read in the chart.

**The chart's letters and the amplitude's components are related by a change of basis and not by a transform.** The word's four parameters are a polar decomposition of the same four numbers, so the Lorenz condition is one equation in either set. **The transform does not enter this section at all**, and the section is included only to record that the chart's own constraint and the form companion's kernel are one object.

**What the chart adds is the reading of the condition as a transport equation.** The parent identifies $S$ with $\partial_\mu(ru^\mu)$ on the timelike branch — the field's own current's conservation, in the flow's own density — and that is *The Spin-One Fluid of the Biquaternion Proca Field*'s reading. **In frequency space the same conservation is the vanishing of $[kA]$, which is algebraic**, and the fluid's continuity equation becomes a single linear condition on a mode. The two readings are one equation, and the frequency-space one is the weaker statement: it holds for a mode and says nothing about a general field.

## Limits

**The constant-coefficient licence bounds every statement here.** The symbol is a matrix of numbers only where the coefficients are constant, which the free equation satisfies. With a connection the symbol is a matrix of operators and the coupled polar companion treats that case.

**The branch is a property of the carrier and not of the transform.** The two branches exist because the material sector's invariant is indefinite, and the transform neither creates nor removes them. An article that reported a branch from the sign of a frequency would be reporting a different quantity.

**The parity table's Schrödinger entry is a comparison and not a claim about that family.** The Schrödinger symbol is affine in the frequency and therefore neither even nor odd; the entry is included to make the table a census of the corpus's operators, and the article claims nothing about the Schrödinger chart.

**The denial, once more.** No sector is exchanged. The word is a decomposition of an element of $\mathbb{B}_\Phi$, the amplitudes are its four real components, and the parity is a property of a matrix of complex numbers. **None of the three is a statement about $\mathbb{B}_\Phi$ and $\mathbb{B}_\Psi$.**

## Open Questions

**Whether a branch label can be assigned to a superposition at all is open.** §*The Branch Is Not a Spectral Property* shows that the label is not a linear functional of the mode coefficients, which is not the same as showing that no assignment exists. A nonlinear assignment — the sign of the invariant of the sum — always exists, and whether it has a reading in the chart's own terms is not settled here.

**Whether the absent phase bracket and the even symbol are the same statement or two statements is open.** The article exhibits both and shows that they agree; whether the agreement is an identity of the algebra or a coincidence of the corpus's two conventions is a question about the operator's order and not about the Proca field, and it is not answered here.

**The amplitude cone's sector label is inherited and not proved here.** *Degenerate Solutions* proves the label for the field values, and §*The Chart's Failure Set Is the Amplitude Cone* transfers it by the sameness of the equation. Whether the transfer needs an additional argument — the amplitude being a coefficient and not a value — is a question the article raises and does not answer.

## Summary

The Proca polar chart has four parameters and two brackets, and one of its four bracket slots is empty: the phase vanishes identically on both branches. In frequency space that emptiness has a name. The Proca symbol is even in the four-wave-number to machine precision ($0.00\times10^{0}$ in the largest entry difference at $k_t'=1.2$), as is the Klein–Gordon scalar; the Dirac symbol is odd ($\lvert\sigma(-K)+\sigma(K)\rvert=2k_m=1.400000$) and the Schrödinger symbol is neither. **A phase bracket needs an odd slot, and a real second-order symbol has none**, which is why the Proca chart carries no guidance equation and the Dirac chart does.

The branch is not a spectral property. The invariant $\langle A\rangle_\natural$ is indefinite quadratic in the amplitudes, so it does not distribute: two timelike amplitudes with invariants $+3.99$ each sum to $+16.00$ while their invariants sum to $+7.98$. The lightlike set is a cone and not a subspace: two lightlike amplitudes sum to a timelike one and differ to a spacelike one. **No linear functional of the spectrum determines a branch label.**

The chart's failure set and the branch's boundary are one variety. The parent's condition "the local four-vector is lightlike" is the same equation as the amplitude cone, and it is one real equation on four real parameters — the parent's codimension-one count and *Degenerate Solutions*'s sector label $\Sigma_{01}$ both transfer unchanged.

What the transform does with the piecewiseness is relocate it. A Fourier mode is a constant frame and sits strictly inside one branch, so the nodal flip is a feature of the superposition and not of the mode. **The branch moves from spacetime to the amplitude space**, and the article states the move as a gain — the branch becomes algebraic — and as a bound — the branch of a sum is not determined by the summands. In the chart's own letters the Lorenz condition on a mode is $[kA]=0$, which is the same plane as the symbol's three-dimensional kernel.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\tilde K_\Phi=ik_t'e_t+\vec k_\Phi$ | The four-wave number; $k_t'=\omega/c$ |
| $k^{2}=k_t'^{2}-\vec k_\Phi^{2}$ | The interval in wave numbers |
| $k_m=mc/\hbar$ | The mass wave number |
| $\tilde A_\Phi=\varepsilon i r\tilde U$, $r\tilde U\hat u$ | The word on the timelike and spacelike branches |
| $r,\ \varepsilon,\ \theta_{\mathrm{rpd}},\ \hat u_{\mathrm b},\ \hat u$ | Scale, branch label, rapidity, boost axis, spacelike direction |
| $\langle A\rangle_\natural=-\lvert a_t'\rvert^{2}+\lvert\vec a\rvert^{2}$ | The invariant; an indefinite quadratic form on the amplitudes |
| $[kA]=k_t'a_t'-\vec k_\Phi\cdot\vec a$ | The Lorenz form of a mode; the parent's $S$ up to $-i$ |
| $\sigma^\mu{}_\nu=(k^{2}-k_m^{2})\delta^\mu{}_\nu-k^\mu k_\nu$ | The Proca symbol, quoted from the form companion |
| $0.00\times10^{0}$ / $1.400000$ | The measured parity residuals for the even and the odd symbol |

## Further Reading

- *The Proca Equation in Biquaternionic Polar Variables*, for the word, the two branches, the bracket table and the absent phase.
- *Degenerate Solutions of the Biquaternionic Proca Equation*, for the lightlike set, the two cones and the sector labels.
- *The Proca Equation: Massive Spin 1 in Biquaternionic Form*, for the plane waves, the Lorenz condition and the polarisation count.
- *The Fourier Transform and the Proca Equation in Biquaternionic Form*, for the symbol's determinant, rank and kernel.
- *The Fourier Transform and the Dirac Equation in Biquaternionic Polar Variables*, for the chart that does carry a phase, and for the phase gradient as the Fourier variable.
- *The Spin-One Fluid of the Biquaternion Proca Field*, for the Lorenz condition as the field's own continuity equation.
- *Mirror Biquaternions and the Phy–Psy Switch*, for the sector bookkeeping that the material sector's reality presupposes.
- *Derivatives, Fields and Transforms*, for the symbol rule.
- *Norm and Pairing Conventions*, for the norm's indefiniteness and the two forms.
- H. Weyl, *The Theory of Groups and Quantum Mechanics* (Dover, 1950), for the polar decomposition of a real four-vector and its two branches.
- C. Møller, *The Theory of Relativity* (Oxford University Press, 1972), for the causal character of a four-vector and the cone of field values.
