# __The Electron in Biquaternionic Form__

## Introduction

The electron is the object on which the relativistic quantum theory of this series is calibrated. It is the particle of Dirac's 1928 equation, the spin-$\tfrac{1}{2}$ field whose magnetic moment is measured to twelve significant figures, and the fermion whose two values of the chirality the Standard Model treats differently. In the biquaternion framework of these articles the electron is the **biquaternion Dirac field** $\tilde{Ξ}_{\mathrm{sp}}\in\mathbb{B}$: an element of the algebra whose two chirality parts satisfy the pair

$$
\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp},R} = k_{m_e}\tilde{Ξ}_{\mathrm{sp},L}, \qquad \tilde{\nabla}^{\natural}\tilde{Ξ}_{\mathrm{sp},L} = k_{m_e}\tilde{Ξ}_{\mathrm{sp},R},
$$

with $m = m_e$ the electron mass. At $m=0$ the pair splits into the two one-sided equations

$$
\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp},R} = 0, \qquad \tilde{\nabla}^{\natural}\tilde{Ξ}_{\mathrm{sp},L} = 0,
$$

one equation per value of the chirality. Each part satisfies the Klein–Gordon equation $(\Box - k_{m_e}^{2})\tilde{Ξ}_{\mathrm{sp},L,R} = 0$, with $\frac{m\,c}{k_m}$ and $c$ restored. The algebra's real structure is the involution $\flat=-{}^{*}$ (*Algebra and Element Conventions*); it is a map of the algebra and not of a carrier, and it is not the mass term. Here $1/k_{m_e}=\hbar/(m_ec)$ is the mass length.

**The element every phase in this article is built from.** The electron's quantum numbers enter through one division and no other,

$$
\tilde K_{\Phi}=\frac{\tilde P_{\Phi}}{\hbar}=i\,k_{t}^{\prime}e_t+\vec k_{\Phi},
\qquad
k_{t}^{\prime}=\frac{E}{\hbar\,c}=\frac{\omega}{c},
\qquad
\vec k_{\Phi}=\frac{\vec p}{\hbar},
\qquad
\tilde P_{\Phi}=i\,p'_{t}e_t+\vec p_{\Phi},
$$

so that $k_m=m\,c/\hbar$ is the third wave number and the mass shell is one line on the coordinates, $\langle\tilde K_{\Phi}\rangle_{\natural}=-k_{t}^{\prime\,2}+k_{\Phi}^{2}=-k_{m_e}^{2}$. Here $\hbar=\frac{m_e\,c}{k_{m_e}}$, the unit that the rest of the article writes in that form; the letter appears wherever a division by it is made explicit, and $\tilde K_{\Phi}$ is what the letter builds. The division is legitimate term by term because $\hbar$ is real and central: it rescales every coefficient from its dimension to an inverse length and moves no element between the sectors, so $\tilde K_{\Phi}\in\mathbb{B}_{\Phi}$ whenever $\tilde P_{\Phi}$ is. Every plane wave below is $\exp(\pm i\,\mathrm{Sc}(\tilde K_{\Phi}\tilde R_\Phi^{\natural}))$, and no other wave number is introduced: the two coordinates of this element and the mass wave number $k_{m_e}$ exhaust the list.

A framework that reformulates known physics can be read in two very different ways. Read generously, every correct statement about the electron becomes a statement the framework "contains"; read carefully, most of those statements are properties of the Dirac equation that the framework merely transcribes, and the specific numbers attached to the electron must be inserted by hand. This article takes the second interpretation and asks a single question: **which properties of the electron are consequences of the biquaternion structure, which are consequences of the Dirac equation the framework contains, which are parameters inserted from outside, and which lie outside the framework altogether?**

The answer, stated plainly at the outset, is the following. The framework *forces* the electron's spin-$\tfrac{1}{2}$ representation content and its tree-level gyromagnetic factor $g=2$; it *contains* the decomposition by chirality, the mass term as the off-diagonal coupler of the two chirality parts, and the Zitterbewegung with its scale; it *inserts* the mass $m_e$, the charge $e$, and the unit $\frac{m\,c}{k_m}$; and it does *not* contain the anomalous magnetic moment, the weak chiral coupling, or a derivation of the mass or charge values. The electron's data are not contained in either subspace, $\mathbb{B}_{\Psi}$ or $\mathbb{B}_{\Phi}$: its spin state, its current, and its Coulomb field are distributed across both, the operation that exchanges the two subspaces is the central $i$ (the rest-energy phase), and the algebra's real structure $\flat = -{}^{*}$ acts on the two sectors with opposite signs, while the mass term couples the two values of the chirality.

A second, less comfortable point belongs in the introduction. Almost every statement the framework makes about "the electron" is a statement about a general structureless spin-$\tfrac{1}{2}$ field. The algebra does not single the electron out. Its mass, its charge, and the identity of its antiparticle are the inputs that make the general field into *this* field.

**The form of the writing.** Every equation below is an equation between elements of the algebra, and every operator is written as the act it performs. A one-sided action is written by position, $a\tilde Q$ and $\tilde Qb$; a two-sided action is written out, $\tilde Q\mapsto a\tilde Qb$; and an operator is named only where the operator itself is the subject of the sentence. The one display of the older formulation is kept in a closing section, for the reader who wants the standard notation.

## The Electron as a Biquaternion Field

**The objects are named here and fixed elsewhere.** The algebra, its four units and its coefficient basis are *Algebra and Element Conventions*; the star, the involution $\flat$ and the two sectors are fixed there; the gradient, its quaternion conjugate and the d'Alembertian are *Operator and Calculus Conventions*; the complex coordinate and the metric of the material sector are *Frame and Metric Conventions*; the two-sided operators and their cells are *Matrix Representations Conventions*, and the one display in this article is the axis-free one. No formula of those objects is repeated here, and every use below is a use of the file named.

**The electron's data are carried by these objects.**

| Electron datum | Biquaternion object |
|---|---|
| The field | the element $\tilde{Ξ}_{\mathrm{sp}}\in\mathbb{B}$ |
| Free equation | $\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp},R} = k_{m_e}\tilde{Ξ}_{\mathrm{sp},L}$, $\tilde{\nabla}^{\natural}\tilde{Ξ}_{\mathrm{sp},L} = k_{m_e}\tilde{Ξ}_{\mathrm{sp},R}$ |
| Mass | the coefficient $m_e$ of the chirality-off-diagonal pair |
| Charge | the coupling $ϙ=-e$ in the gauge-covariant derivative (see below) |
| Spin state | the state $\tilde{Ϛ}_{\Psi}(\vec u)\in\mathbb{B}_{\Psi}$ along a declared unit direction $\vec u$ |
| Spin observables | Hermitian elements $\tilde R_\Psi = i \sum_k h_k\vec e_k\in\mathbb{B}_{\Psi}$ |
| Conserved current | $\tilde{J}_{\Phi} = ic\,j_0 e_t + \vec j\in\mathbb{B}_{\Phi}$, with $j_0\ge0$ |
| Chirality parts | the parts $\tilde{Ξ}_{\mathrm{sp},L}$ and $\tilde{Ξ}_{\mathrm{sp},R}$, the two values of the subscript |

The placement of these objects already contains the article's main structural observation: the electron's state-like data (its spin) and its field-strength-like data (its Coulomb field) are $\mathbb{B}_{\Psi}$ objects, its current is an $\mathbb{B}_{\Phi}$ object, the algebra's real structure $\flat$ acts on the two sectors with opposite signs while the mass term couples the two values of the chirality, and it is the rest-energy phase that rotates one sector into the other. There is no single sector of the algebra in which "the electron" lives.

## Mass: A Term the Framework Needs but Cannot Supply

The electron mass appears in the free equation as the coefficient of the chirality-off-diagonal pair

$$
\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp},R} = k_{m_e}\tilde{Ξ}_{\mathrm{sp},L}, \qquad
\tilde{\nabla}^{\natural}\tilde{Ξ}_{\mathrm{sp},L} = k_{m_e}\tilde{Ξ}_{\mathrm{sp},R} .
$$

Three statements are worth separating — how the mass couples the two values of the chirality, how the algebra's real structure acts on the two sectors, and what phase the mass puts between the sectors — and a fourth, negative statement closes the section.

**It mixes the two values of the chirality.** The two parts of the field are the part of value $L$ and the part of value $R$, and the mass term couples them: without it, the electron would be two independent massless fields. The electron's mass is therefore represented, in the framework, as a chirality-mixing term, and this is the structural origin, in the biquaternion reading, of the fact that a field of one chirality value alone cannot carry a mass. The coupling is necessarily off-diagonal. Left multiplication keeps the value of its operand, and a product takes the value of its right factor, so a left multiplication by one element of $\mathbb{B}$ can never carry the part of one value onto the part of the other; only the off-diagonal pair above does it. The pair is complex-linear in the field but not left-$\mathbb{B}$-linear, which is the precise sense in which the mass sits outside the action the algebra supplies of itself.

**The real structure acts on the two sectors with opposite signs.** This is a derived form of the star's two sector signs. For an element $\tilde{Q} = \tilde{Q}_+ + \tilde{Q}_-$ with $\tilde{Q}_\pm\in\mathbb{B}_{\Psi}\cup\mathbb{B}_{\Phi}$ one has $\tilde{Q}_\pm^{*} = \pm\tilde{Q}_\pm$, hence

$$
\tilde{Q}^\flat = -\tilde{Q}^{*} = -\tilde{Q}_+ + \tilde{Q}_-,
$$

so $\flat$ acts as $-1$ on the $\mathbb{B}_{\Psi}$ part and $+1$ on the $\mathbb{B}_{\Phi}$ part. It **preserves** each sector and marks it with a sign: it is diagonal on the sector decomposition, not an exchange of the two sectors. This is a property of the algebra's real structure, not of the mass term.

**It is not the mass, though it has the shape of one.** An algebra-level coupling built on $\flat$ — the single-field equation $\tilde{\nabla}F = mF^\flat$ on $F\in\mathbb{B}$, the retired form recorded in *Algebra and Element Conventions* — is Majorana-shaped: because $\flat$ is antilinear, such a term pairs the field with its own conjugate and is not invariant under the continuous central phase, which is exactly how a Majorana pairing differs from an ordinary Dirac mass. But it is the wrong equation for the electron, not merely a differently written one: its central-phase plane waves sit on the spacelike locus rather than on the mass shell. The electron's mass must therefore break the central phase rather than being built from $\flat$, and in this article it does — it is the off-diagonal chirality pair, and $\flat$ is used only for conjugation. The operation that exchanges the two sectors is multiplication by the central $i$, $i\,\mathbb{B}_{\Psi} = \mathbb{B}_{\Phi}$.

**It sets the rate at which the two sectors rotate into one another.** Factoring the rest energy out of a free plane wave gives

$$
\exp\!\Big(-c\,k_m\,i\,r'_{t}\Big)
= \cos\!\Big(c\,k_m\,r'_{t}\Big)e_t - \sin\!\Big(c\,k_m\,r'_{t}\Big)(ie_t),
$$

where the right-hand side uses only $i^2=-1$ and $e_t=1$: expanding the exponential, $\exp(-i\theta)=e_t-i\theta e_t-\tfrac12\theta^2e_t+\cdots$ and collecting the real and imaginary parts gives the cosine and the sine. Here $e_t\in\mathbb{B}_{\Psi}$ and $ie_t\in\mathbb{B}_{\Phi}$ (an imaginary scalar is anti-Hermitian). The exponent is the one exponent of the article read at rest: $c\,k_m\,r'_t=k_{t}^{\prime}r'_t$ with $\vec k_{\Phi}=0$ and $k_{t}^{\prime}=k_m$, so the phase is $\mathrm{Sc}(\tilde K_{\Phi}\tilde R_\Phi^{\natural})$ restricted to the temporal coordinate. The rest-energy phase is central, and because $i\,\mathbb{B}_{\Psi} = \mathbb{B}_{\Phi}$ it is a rotation between the sectors at angular frequency $ck_{m_e}$: it takes the $\mathbb{B}_{\Psi}$ direction $e_t$ toward the $\mathbb{B}_{\Phi}$ direction $ie_t$ and back. The mass sets this scale — the frequency is $ck_{m_e}$ — through the mass shell. This is the sense in which the electron's mass, in the framework, *is* the rate of the rotation between the material and informational subspaces.

**What is not derived.** The value $m_e = 9.1093837015\times10^{-31}$ kg, or equivalently $m_ec^2 = 0.510998950$ MeV, is not a consequence of the algebra or of the equation; it is a parameter. The framework is scale-free until $m_e$ is supplied, and every electron scale below — the Compton length, the Zitterbewegung frequency — is set by the supplied value, not produced by the structure.

## Charge: A Coupling Constant in the Gradient

The free biquaternion Dirac equation contains no charge. Charge enters only through the coupling of the field to the four-potential $\tilde{A}_{\Phi} = i\,a'_t\,e_t + \vec A\in\mathbb{B}_{\Phi}$. In the intrinsic form this is the minimal substitution

$$
\tilde P_{\Phi} \to \tilde P_{\Phi} - ϙ\tilde A_{\Phi}, \qquad\text{equivalently}\qquad p_\mu \to p_\mu - ϙA_\mu,
$$

with $ϙ$ the particle's charge; for the electron $ϙ = -e$. The precise biquaternion form of this coupling is set out in the companion article *The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism*, which replaces $\tilde\nabla$ and $\tilde\nabla^{\natural}$ by the gauge-covariant derivative $\tilde\nabla_{\mathrm{gco}}$ of *Operator and Calculus Conventions* and its conjugate $\tilde\nabla_{\mathrm{gco}}^{\natural}$, both carrying $+\frac{k_m\,i\,ϙ}{m\,c}\tilde{A}_{\Phi}$, and derives the coupled equation

$$
\tilde\nabla_{\mathrm{gco}}\tilde{Ξ}_{\mathrm{sp},R} = k_{m_e}\tilde{Ξ}_{\mathrm{sp},L}, \qquad
\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde{Ξ}_{\mathrm{sp},L} = k_{m_e}\tilde{Ξ}_{\mathrm{sp},R},
$$

and shows that it is exactly gauge covariant in the massive case as well as the massless one, the central phase passing through the linear mass pair; the charge is therefore *represented* in the framework, not derived by it.

Four statements are worth separating.

**The conservation law is derived.** Given the equation, a four-current is conserved. The current is the material-sector element $\tilde{J}_{\Phi} = ic\,j_0 e_t + \vec j$, with $j_0\ge0$, and its conservation is the vanishing of the scalar part of $\tilde\nabla^{\natural}\tilde{J}_{\Phi}$, that is $\partial j_0/\partial r'_t + \nabla\cdot\vec j = 0$. That the electron's conserved current is a material-sector object is a structural consequence of the equation, not an added assumption. What is not derived is the bilinear itself: it is not a product of the field with its own conjugate inside the algebra, because it carries an adjoint read through a form, and a pairing of two elements is not an element. It is displayed, once and in the older formulation, in the closing section of the companion article on minimal coupling, where it is also shown that no bilinear of the field alone takes its place. No step of this article uses it: the conservation law just stated is all that the sections below need.

**The value and sign of the charge are inserted.** Nothing in the algebra fixes $e$, explains why charge is quantised, or explains why the electron and the proton have equal and opposite charge. The equation with $ϙ = -e$ and the equation with $ϙ = +e$ have the same form, related by $\tilde{A}_{\Phi}\to-\tilde{A}_{\Phi}$; the labelling of which branch is the electron is a convention. Charge conjugation makes this explicit: the equation admits a symmetry that exchanges the two frequency branches and reverses the sign of the current, and the operator that realises it is displayed in the closing section. The framework represents both signs of charge on the same footing.

**The electron's Coulomb field is an $\mathbb{B}_{\Psi}$ object.** For a point charge $ϙ$ at rest the field-strength biquaternion is, from the companion article on Maxwell's equations,

$$
\tilde{F}(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z) = \frac{i\,ϙ\,\vec u_x}{4\pi\sqrt{\epsilon}\,\|(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)\|^2},
$$

a purely imaginary vector, hence an element of the Hermitian subspace $\mathbb{B}_{\Psi}$, with $\vec u_x = (r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)/\|(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)\|$ the radial unit vector. The electron's charge shows itself, in the framework, through a field in the informational sector, while its current lies in the material sector. The two faces of the same charge sit in opposite halves of the algebra.

**What is derived once the coupling is inserted.** The minimal substitution yields the magnetic coupling with the coefficient $1/2m_e$, and hence the sign relation $\vec\mu_e = -(e/m_e)\vec S$: the electron's magnetic moment is anti-parallel to its spin because its charge is negative. The magnitude, however, is dimensional and carries $e$ and $\frac{m\,c}{k_m}$.

## Spin: Derived as a Representation, Normalised by Hand

The electron's spin is where the framework is strongest and where the distinction between derived and inserted is sharpest.

**Derived: the representation.** The algebra $\mathbb{B}\cong M_2(\mathbb{C})$ has a unique irreducible left action, on a complex space of dimension two, and the group of unit elements of the quaternionic norm is $SL(2,\mathbb{C})$, the double cover of the proper orthochronous Lorentz group (*Norm and Pairing Conventions*). A field in that space carries the representation $(\tfrac12,0)$; the field of this article splits by the chirality into two such parts and carries $(\tfrac12,0)\oplus(0,\tfrac12)$. In either case the spin is $\tfrac12$: a rotation by $2\pi$ acts as $-e_t$ on the two-dimensional space and as $+e_t$ on the four-vectors of $\mathbb{B}_{\Phi}$. The twofold, double-valued character of electron spin is therefore a consequence of where the field lives, not an independent postulate. The spin rotations are the real unit quaternions, forming $SU(2)$.

**Derived: the state and observable structure.** The electron's spin state along a declared unit direction $\vec u$ is the state $\tilde{Ϛ}_{\Psi}(\vec u)\in\mathbb{B}_{\Psi}$ of *Algebra and Element Conventions*, and its spin observables are the Hermitian elements $i \sum_k h_k\vec e_k\in\mathbb{B}_{\Psi}$. With the Born pairing of *Norm and Pairing Conventions* the state along $\vec u$ returns the weight $n_\nu h_\nu$ on $\tilde R_\Psi = i\sum_k h_k\vec e_k$; in particular the state along $\vec e_z$ returns $1$ on $i\vec e_z$ and $0$ on $i\vec e_x$, the values the spin along $z$ requires.

**Inserted: the magnitude.** The spin element is $\tilde S_{\Psi,k} =\frac{m\,c}{2\,k_m}(i\vec e_k)$. The element $i\vec e_k$ is Hermitian and squares to $+e_t$, so it is the algebra's spin component and has the two eigenvalues $\pm1$. The factor $\frac{m\,c}{2\,k_m}$ is a normalisation, not a prediction: the algebra fixes that spin is two-valued and that its observables close under $SU(2)$, but it does not fix the unit in which spin is measured. The number $\tfrac{1}{2}$ in "spin-$\tfrac{1}{2}$" is algebra; the number $\frac{m\,c}{k_m}$ is physics inserted from outside.

## The Dirac Description of the Electron

The electron's relativistic dynamics is the chirality pair $\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp},R}=k_{m_e}\tilde{Ξ}_{\mathrm{sp},L}$, $\tilde{\nabla}^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=k_{m_e}\tilde{Ξ}_{\mathrm{sp},R}$. The plane-wave solutions are computed in the companion solutions article, in the algebra's own objects. They come in two branches at each momentum,

$$
\tilde{Ξ}_{\mathrm{sp}}^{(+)}=w^{(r)}(\vec p)\exp\!\big(+i\,\mathrm{Sc}(\tilde K_{\Phi}\tilde R_\Phi^{\natural})\big),
\qquad
\tilde{Ξ}_{\mathrm{sp}}^{(-)}=v^{(r)}(\vec p)\exp\!\big(-i\,\mathrm{Sc}(\tilde K_{\Phi}\tilde R_\Phi^{\natural})\big),
$$

$$
\mathrm{Sc}(\tilde K_{\Phi}\tilde R_\Phi^{\natural})=\vec k_{\Phi}\cdot\vec r-k_{t}^{\prime}r'_t=\frac{\vec p\cdot\vec r-E\,r'_t/c}{\hbar},
$$

the first being the positive-frequency branch $w^{(r)}$ and the second the negative-frequency branch $v^{(r)}$, with $\vec r = r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z$, $E = +\sqrt{\vec p^2c^2 + m_e^2c^4}$ and $r$ the spin label. The two branches are the two signs of the one exponent, and the sign is the sign of the temporal coordinate $k_{t}^{\prime}$; the spatial coordinate $\vec k_{\Phi}$ is common to both, and only the temporal one changes sign, which is the algebraic statement that the two branches have equal momentum and opposite energy. Earlier versions printed the exponent as $\frac{k_m\,i\,(E\,r'_t/c-\vec p\cdot\vec r)}{m\,c^{2}}$, whose coefficient is $\frac{1}{\hbar\,c}$ and not $\frac{1}{\hbar}$: that form divides the action by one factor of $c$ too many, since $Et/\hbar$ with $t=r'_t/c$ is $E\,r'_t/(\hbar\,c)$. Written as $\mathrm{Sc}(\tilde K_{\Phi}\tilde R_\Phi^{\natural})$ the exponent is an inverse length against a length, dimensionless by construction, with nothing left to check. Together they span a complex space of dimension four, one pair for each value of the chirality; the dimension two of each pair is the dimension of the irreducible action, and the count is the count of the two values. The spin sums, normalisations, and bilinears are constructed in the companion solutions article and are not repeated here.

**A note on the wave-number biquaternion.** The mass-shell condition is written in the corpus convention, in which the four-wavevector has the imaginary time component of the $i r'_t$ convention. It is the element of the introduction, $\tilde K_{\Phi}=\tilde P_{\Phi}/\hbar=i k_{t}^{\prime}e_t+\vec k_{\Phi}$, whose coordinates are $k_{t}^{\prime}=\omega/c$ and $\vec k_{\Phi}=\vec p/\hbar$ with $\vec k_{\Phi}^{2}=k_x^2+k_y^2+k_z^2$ the Euclidean square, which is what the norm of a vector part produces. Then

$$
\tilde K_{\Phi}\tilde K_{\Phi}^{\natural}=\langle\tilde K_{\Phi}\rangle_{\natural}=-\frac{\omega^{2}}{c^{2}}+\vec k_{\Phi}^{2}=-k_{t}^{\prime\,2}+k_{\Phi}^{2},
$$

and this is $-k_{m_e}^{2}$ on the shell, which is $E^2 = \vec p^2c^2 + m_e^2c^4$ under $\tilde P_{\Phi}=\hbar\tilde K_{\Phi}$. It is the form used by the companion solutions article and by the parent Dirac article. With the electron's constants and $|\vec p|/(m_ec)=0.37417$ the coordinates are $k_{t}^{\prime}=2.764945\times10^{12}\ \mathrm{m^{-1}}$ and $k_{\Phi}=9.689525\times10^{11}\ \mathrm{m^{-1}}$, and $-k_{t}^{\prime\,2}+k_{\Phi}^{2}=-6.706054\times10^{24}\ \mathrm{m^{-2}}$ equals $-k_{m_e}^{2}$ to machine precision, with $k_{m_e}=2.589605\times10^{12}\ \mathrm{m^{-1}}$; the same three numbers give $2c\,k_{t}^{\prime}=2E/\hbar=1.657820\times10^{21}\ \mathrm{rad\,s^{-1}}$ off rest and $1.552688\times10^{21}\ \mathrm{rad\,s^{-1}}$ at rest.

**What the older display did.** It printed the same condition as $\tilde P_{\Phi}\,k_{\mathrm{mo}} = i\frac{\omega}{c}e_t+\vec k$ with $\langle\tilde P_{\Phi}k_{\mathrm{mo}}\rangle_{\natural}=-k_{m_e}^{2}$, and described $k_{\mathrm{mo}}=\frac{k_m\,p}{m\,c}$ as *the momentum length*. Three things are wrong with it, and each is the same thing seen from a different side. First, the dimensions: $\tilde P_{\Phi}$ carries a momentum and $k_{\mathrm{mo}}$ an inverse length, so the product carries a momentum over a length, $\mathrm{M}\,\mathrm{T}^{-1}$, while the right-hand side carries $\mathrm{L}^{-1}$; the two sides of the first display differ by one factor of a momentum. Second, the name: $\frac{k_m\,p}{m\,c}$ is $\frac{p}{\hbar}$, an inverse length and not a length, and it is not a third object at all — it is $\left|\vec k_{\Phi}\right|$, the modulus of the spatial coordinate already present. Third, the norm: with the product written as it was, $\tilde P_{\Phi}\tilde P_{\Phi}^{\natural}k_{\mathrm{mo}}^{2}$ carries $\mathrm{M}^{2}\mathrm{T}^{-2}$, a momentum squared, and cannot equal $-k_{m_e}^{2}$; the shell needs one division by $\hbar$, not a multiplication by $p/\hbar$. With $k_m=\frac{m_e c}{\hbar}$ and $|\vec p|/(m_e c)=0.37417$ the numbers are $k_{\mathrm{mo}}=9.689525\times10^{11}\ \mathrm{m^{-1}}$ and $k_{m_e}=2.589605\times10^{12}\ \mathrm{m^{-1}}$, so $k_{\mathrm{mo}}/k_{m_e}=0.37417$ — the momentum fraction recovered, which is what a length could not have given.

The division is the one line that fixes all three: $\tilde K_{\Phi}=\tilde P_{\Phi}/\hbar$ has the unit of the right-hand side, names its coordinates, and makes the shell a statement about one element.

**Antiparticle.** The two frequency branches are exchanged by charge conjugation, and in the quantized interpretation the negative-frequency branch describes the positron. The framework represents the electron and the positron on the same algebraic footing; which branch is called the electron is fixed by the charge convention of the previous section, not by the algebra.

### The One-Sided and the Two-Sided Forms of the Equation

The article carries two Dirac equations, and they must not be read as one. They use the same mass coefficient; they differ in which side of the field the derivative acts and in where the mass sits.

The **one-sided equation** is the corpus's definition: the chirality pair above. The gradient acts by left multiplication, the field is the algebra element $\tilde{Ξ}_{\mathrm{sp}} = \tilde{Ξ}_{\mathrm{sp},L}+\tilde{Ξ}_{\mathrm{sp},R}$, and the mass is the off-diagonal pairing of the two chirality parts,

$$
\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp},R} = k_{m_e}\,\tilde{Ξ}_{\mathrm{sp},L}, \qquad
\tilde{\nabla}^{\natural}\tilde{Ξ}_{\mathrm{sp},L} = k_{m_e}\,\tilde{Ξ}_{\mathrm{sp},R} .
$$

This is the form in which the chirality is visible, and it is the form the sections on mass and on the two chirality values use.

The **two-sided equation** is the dictionary form of V. V. Kravchenko: a single equation on the algebra-valued field $F\in\mathbb{B}$,

$$
\mathcal{N}F = \Big(i\frac{\partial}{\partial r'_t}+\vec\nabla\Big)F - m\,i\,\overline{F}\,\vec e_z = 0,
\qquad\text{that is}\qquad
-\tilde{\nabla}^{\natural}F - k_m\,i\,\overline{F}\,\vec e_z = 0
$$

with $\vec\nabla = \sum_k\vec e_k\,\partial/\partial R_k$ and the bar the coefficientwise complex conjugation. The time derivative and the spatial gradient act by left multiplication; the mass term acts by right multiplication through $\vec e_z$ and carries the antilinear conjugation. This is the form in which the quaternionic analysis acts — the shifted operator, the Cauchy kernel, and the integral representation of the harmonic field.

| | One-sided equation | Two-sided equation |
|---|---|---|
| Equation | $\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R}=k_{m_e}\tilde{Ξ}_{\mathrm{sp},L}$, $\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=k_{m_e}\tilde{Ξ}_{\mathrm{sp},R}$ | $\mathcal{N}F=0$, as displayed |
| Field | the element $\tilde{Ξ}_{\mathrm{sp}}\in\mathbb{B}$ | the element $F\in\mathbb{B}$ |
| Mass | the off-diagonal pairing of the two chirality values | $-k_{m_e}i\,\overline{F}\,\vec e_z$: a conjugation and a direction |
| Derivative | left, by $\tilde\nabla$ and $\tilde\nabla^{\natural}$ | left by $i\partial/\partial r'_t$ and $\vec\nabla$; right by $\vec e_z$ in the mass |
| Chirality | the subscript, the two values $L$ and $R$ | the same two values, carried by the right multiplication by $\vec e_z$ in the mass |
| Use | the definition, the kinematics, and the mass term | the analytic theory and the integral representation |

The two are related by an explicit real-linear dictionary, not by an identity of operators. The one-sided pair is the definition, and the two-sided single equation is the form in which the analytic machinery acts. The electron's mass is the same coefficient $m_e$ in both; what changes is the representation, not the physics.

## Gyromagnetic Ratio: The One Quantitative Number the Equation Predicts

The Dirac description yields one celebrated number. Carrying the biquaternion Dirac equation to the non-relativistic regime — the computation is performed in the companion solutions article and its exercise — eliminates the small part and leaves the Pauli equation with the spin term. That term is the Hermitian element

$$
-\frac{ϙ\,c}{2\,k_{m_e}}\,i\,\vec B = -\frac{ϙ\,\hbar}{2\,m_e}\,i\,\vec B\ \in \mathbb{B}_{\Psi} ,
$$

where $\frac{c}{k_{m_e}}=\frac{\hbar}{m_e}$, so the coefficient is the Bohr-magneton one and the two writings are the same number in two units.

Writing the coupling as $-\vec\mu\cdot\vec B$ identifies $\vec\mu = (ϙ/m_e)\vec S$, with the spin components $\tilde S_{\Psi,k} =\frac{m\,c}{2\,k_m}i\vec e_k$, which is $\vec\mu = g\,(ϙ/2m_e)\vec S$ with

$$
g = 2 .
$$

The coefficient $1/2m_e$ is produced by the elimination, not put in by hand: this is Dirac's tree-level prediction, here a property of the biquaternionic mass term. For the electron, $ϙ = -e$, so

$$
\boxed{\;\vec\mu_e = -\frac{e}{m_e}\vec S = -g\,\frac{e}{2m_e}\vec S, \qquad g = 2\;},
$$

of magnitude one Bohr magneton $\mu_B = \dfrac{e\,c}{2\,k_{m_e}} = \dfrac{e\,\hbar}{2\,m_e} = 9.274010\times10^{-24}$ J T$^{-1}$ when $\vec S$ is aligned with $\vec B$.

Two qualifications belong with the result. First, the derivation is the standard Dirac one, transcribed; the biquaternion form supplies the compact notation and the sector interpretation of the spin coupling as an $\mathbb{B}_{\Psi}$ observable, not an independent derivation. Second, $g=2$ is not an electron-specific number: it holds for any structureless spin-$\tfrac{1}{2}$ field, so it distinguishes the electron from a spin-1 particle but not from a muon.

**Outside the framework: the anomaly.** The measured value is $g/2 = 1.00115965218$, i.e. $a = (g-2)/2 = 1.159652\times10^{-3}$, close to the one-loop Schwinger value $a \approx \alpha/2\pi = 1.161410\times10^{-3}$. This is a radiative correction of quantum electrodynamics; it lies outside the classical equation treated here, and the framework does not contain it. The tree-level $g=2$ is the whole of what the equation supplies.

## Zitterbewegung: The Scale of the Mass, Not a Signature of a Sector

The electron is the particle on which the Zitterbewegung was found. In the framework's own terms, the trembling is the interference of the two frequency branches, so its angular frequency is twice the angular frequency of either branch: $2c\,k_{t}^{\prime}=2E/\hbar$, and $2c\,k_{m_e}=2m_ec^{2}/\hbar$ at rest. The display carries one frequency and one length, and the length is not $k_m$ but its reciprocal,

$$
\omega_Z = 2c\,k_{t}^{\prime} = 2c\,k_{m_e} = 1.55269\times10^{21}\ \text{rad s}^{-1},
\qquad
f_Z=\frac{\omega_Z}{2\pi}=2.47118\times10^{20}\ \text{Hz},
\qquad
\frac{1}{2\,k_{m_e}} = 193.1\ \text{fm}
$$

half the reduced Compton wavelength $1/k_{m_e}=386.2$ fm. These are the standard values, reconfirmed numerically in the companion article on the Zitterbewegung. Both frequencies come from one coordinate: $2c\,k_{t}^{\prime}$ is twice $c$ times the temporal entry of $\tilde K_{\Phi}$, and the second equality is the value of that entry at rest, where $\vec k_{\Phi}=0$ and the shell gives $k_{t}^{\prime}=k_{m_e}$.

The older version of this paragraph wrote the frequency as $2c\,k_E$ and called $k_E=E/(\frac{m\,c^{2}}{k_m})$ *the energy length*. The expression is $E/(\hbar\,c)$ — the same number as $k_{t}^{\prime}$, since $\frac{m\,c^{2}}{k_m}=\hbar\,c$ — but it is an inverse length and not a length, its reciprocal $E/(\hbar c)$ has none of the standing of a Compton length, and it was never a second object beside the mass wave number. It is retired here in favour of the coordinate it denotes.

The framework's temptation is to read the trembling as the observable face of the complexification — positive- and negative-energy branches being the two sectors. The companion article tests that identification and refutes it. The energy sign is the sign of the eigenvalue of a Hamiltonian whose terms multiply the field on the right, through the action $\tilde Q\mapsto i\tilde Q\vec e_x$, and no element of $\mathbb{B}$ does that by left multiplication, while the sectors are the two signs of the star. The two are also splits of different objects: a family of solutions and the values it takes. What survives is a relation of scale and phase: at rest the trembling frequency is exactly twice the rest-energy sector-rotation frequency $ck_{m_e}$, because the trembling phase is the square of the free-evolution phase. For the electron this means that its rest energy sets both the rate at which the sectors rotate into one another and the frequency of the trembling, without the trembling being an informational-sector effect.

## The Two Values of the Chirality

The chirality of the electron field is the subscript of the element, and it takes two values. The field is written

$$
\tilde{Ξ}_{\mathrm{sp}} = \tilde{Ξ}_{\mathrm{sp},L} + \tilde{Ξ}_{\mathrm{sp},R},
$$

where $\tilde{Ξ}_{\mathrm{sp},L}$ is the part of value $L$ and $\tilde{Ξ}_{\mathrm{sp},R}$ the part of value $R$; only the zero element carries both. Each part is carried by a complex space of dimension two, and the pair is what the Standard Model calls the left-handed and the right-handed halves of the field.

Two facts about products carry the whole structure, and they are stated in words because that is all they are. **Left multiplication keeps the value**: for every element $a$, the product $a\tilde{Ξ}_{\mathrm{sp},L}$ has value $L$ and $a\tilde{Ξ}_{\mathrm{sp},R}$ has value $R$. **A product takes the value of its right factor**: when the factor on the right carries a value, so does the product, and it is that value. Two consequences follow at once. The massless pair splits into one equation per value, because each of the two one-sided equations above carries a single value through. And the mass term, which is a left multiplication on the field and an off-diagonal coupling of the two values, is the only term that relates them — the same statement as the chirality-mixing of the mass section, read from the other side.

**Derived.** The two-value structure is a consequence of the representation: the field is the direct sum of the two inequivalent two-dimensional representations of $SL(2,\mathbb{C})$, and the mass term is the unique Lorentz-invariant coupling between them. For a massless electron the value of the chirality coincides with helicity, so the two branches become the two definite chiralities. This is a genuine structural consequence of the algebra and of the equation.

**Represented, not derived: the weak chiral coupling.** In the Standard Model the electron couples to the weak interaction through its left-handed part only. The framework contains the decomposition by chirality, so it has the vocabulary for this, but it does not select the coupling: nothing in $\mathbb{B}$ or in the Dirac equation says that one value couples and the other does not. The $V-A$ structure is an input.

**Caution: the values of the chirality are not the two sectors.** The decomposition by chirality is a decomposition of the element by a subscript; the sector decomposition is a decomposition of the algebra by the star. The Zitterbewegung article reaches the same distinction from the other side when it rejects the identification of the energy branches with $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{\Phi}$ and names the chirality as the candidate for the interference structure. The two decompositions share nothing: a statement about one is not a statement about the other.

## Derived, Represented, Outside: An Accounting

| Feature of the electron | Status in the framework | Where it comes from |
|---|---|---|
| Spin-$\tfrac{1}{2}$ representation content | Derived | $\mathbb{B}\cong M_2(\mathbb{C})$, unique irreducible action on a space of dimension two; $SL(2,\mathbb{C})$ double cover |
| Spin states, observables, expectation values | Derived | the state of $\mathbb{B}_{\Psi}$ and the Born pairing of *Norm and Pairing Conventions* |
| Spin magnitude $\frac{m\,c}{2\,k_m}$ | Represented | normalisation of $\tilde S_{\Psi,k} =\frac{m\,c}{2\,k_m}i\vec e_k$ |
| Tree-level $g=2$, $\vec\mu_e = -(e/m_e)\vec S$ | Derived (conditional) | $1/2m_e$ coefficient from the mass term plus minimal coupling |
| Conservation of the current, $\tilde{J}_{\Phi}\in\mathbb{B}_{\Phi}$ | Derived | the law $\mathrm{Sc}(\tilde\nabla^{\natural}\tilde{J}_{\Phi}) = 0$; the bilinear itself is the older display's, in the companion article's closing section |
| Coulomb field $\tilde{F}\in\mathbb{B}_{\Psi}$ | Derived (from Maxwell) | point-charge solution; purely imaginary vector |
| Mass term couples the two chirality values, off-diagonally | Derived | the two-value split; the off-diagonal pair |
| Two-sided single-equation form | Derived (dictionary) | the real-linear dictionary $F\in\mathbb{B}$; a change of representation, not of physics |
| Rest-energy phase rotates sectors at $ck_{m_e}$ | Derived | $\exp(-i\theta) = \cos\theta\,e_t - \sin\theta\,(ie_t)$ |
| Zitterbewegung frequency and amplitude | Derived | two-branch interference; $2c\,k_{t}^{\prime}=2E/\hbar$, $\dfrac{1}{2\,k_{m_e}}$ |
| Mass value $m_e$ | Represented | parameter of the equation |
| Charge value $e$, sign convention, quantisation | Represented | minimal coupling; no derivation in the framework |
| Electron/positron labelling | Represented | charge convention; charge conjugation is a symmetry |
| Anomalous moment $a=(g-2)/2$ | Outside | radiative QED correction |
| Weak $V-A$ chiral coupling | Outside | Standard Model input |
| Quantization of the field | Partly outside | a transcription to the algebra exists; the operator-valued field is open |
| Anything that would distinguish the electron from another spin-$\tfrac{1}{2}$ field | Outside | the algebra contains no such discriminator |

## The Gaps, Named

Two gaps are structural and cannot be closed by better notation: the mass value and the charge value are inputs, and the anomaly is outside the classical equation. Three further gaps belong to the programme rather than to this article. **Quantization** has been carried out at the level of the algebra, but the $\mathbb{B}$-intrinsic form — the operator-valued biquaternion field, its Lagrangian, its Fock space, and the embedding of the fermionic $\mathbb{Z}/2$ grading in $\mathbb{B}$ — remains open, so the electron as a quantum field is only partly inside the framework. **Empirical contact** is absent: nothing here distinguishes the framework from standard relativistic quantum physics for the electron. And the framework is **not electron-specific**: it represents the electron, the muon, and any other structureless spin-$\tfrac{1}{2}$ field by the same objects, with no reason in the algebra to prefer one mass or charge over another. These are labelled gaps, not a closed account.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The generators carry no frame label: $\gamma_\mu$ is one set of matrices, and the frame is named on the coordinate.

The sections above are written in cells; this section writes the same cells as gamma matrices, for readers who want the standard notation. The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra.

Each gamma is a single cell $T_{a,b}=L_aR_b$, a pure tensor, and a general element of $M_4(\mathbb{C})$ is a sum of at most four such cells.

$$
\gamma_0=iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_x},\quad \gamma_1=iL_{\mathrm{pau},\vec e_x}R_{\mathrm{pau},\vec e_y},\quad \gamma_2=iL_{\mathrm{pau},\vec e_y}R_{\mathrm{pau},\vec e_y},\quad \gamma_3=iL_{\mathrm{pau},\vec e_z}R_{\mathrm{pau},\vec e_y},\quad \gamma_5=-iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_z} .
$$

The same in the axis-free display:

$$
\gamma_0=iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_x},\quad \gamma_1=iL_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_y},\quad \gamma_2=iL_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_y},\quad \gamma_3=iL_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y},\quad \gamma_5=-iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_z} .
$$

$\gamma_5$ is the cell of the chirality operator $\Gamma:\tilde{Ξ}_{\mathrm{sp}}\mapsto -i\,e_t\,\tilde{Ξ}_{\mathrm{sp}}\,\vec e_z = -iR_{\mathrm{pau},\vec e_z}$, which acts on the Dirac module. The central grading $\chi=i\tilde{Ζ}_{\mathrm{ad}}$, where $\tilde{Ζ}_{\mathrm{ad}}$ is the central root of $-1$ that complexifies the real subalgebra $\mathbb{B}_{\mathbb{R}}=\mathbb{B}_{H}$ ($\tilde{Ζ}_{\mathrm{ad}}^2=-1$, $[\tilde{Ζ}_{\mathrm{ad}},i]=0$), is the difference of the two central idempotents of the complexified algebra, so $\xi^2=i^2\tilde{Ζ}_{\mathrm{ad}}^2=(-1)(-1)=e_t$. The grading $\xi$ is central and belongs to the algebra, $\Gamma$ is its representative on the module, and $\gamma_5$ is that representative written as a cell.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$. The four generator cells of the older display are these gammas, $\gamma_\mu$, and the charge-conjugation cell is $C = -iL_{\mathrm{pau},\vec e_y}R_{\mathrm{pau},\vec e_z} = i\gamma_2\gamma_0$, the antisymmetric matrix with $C^2=-I_4$ that reverses all four gammas under transposition.

**The identities the bodies cite.** In the $\gamma$ reading, with $\varepsilon=(1,-1,-1,-1)$ the sign vector of the cells,
$$
\{\gamma_\mu,\gamma_\nu\}=2\varepsilon_\mu\delta_{\mu\nu}I_4,\qquad
(\gamma_k)^2=-I_4,\qquad
\gamma_5^2=I_4,\qquad
\{\gamma_\mu,\gamma_5\}=0,
$$
$$
[\gamma_\mu,\gamma_\nu]=2\gamma_\mu\gamma_\nu\quad(\mu\ne\nu),\qquad
[\gamma_a,S_{cd}]=\varepsilon_a\delta_{ac}\gamma_d-\varepsilon_a\delta_{ad}\gamma_c,\qquad
S_{cd}=\tfrac14[\gamma_c,\gamma_d],
$$
$$
\mathrm{tr}(\gamma_\mu\gamma_\nu)=4\varepsilon_\mu\delta_{\mu\nu},\qquad
\mathrm{tr}(\gamma_5\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)=-4i\,\epsilon_{\mu\nu\rho\sigma},
$$
$$
\mathrm{tr}(\gamma_\mu\gamma_\nu\gamma_\rho\gamma_\sigma)
=4\bigl(\varepsilon_\mu\delta_{\mu\nu}\varepsilon_\rho\delta_{\rho\sigma}
-\varepsilon_\mu\delta_{\mu\rho}\varepsilon_\nu\delta_{\nu\sigma}
+\varepsilon_\mu\delta_{\mu\sigma}\varepsilon_\nu\delta_{\nu\rho}\bigr).
$$
The contraction sums follow from the squares. With one index raised, $\gamma^\mu=-\varepsilon_\mu\gamma_\mu$, so that $\sum_\mu\gamma^\mu\gamma_\mu=-4I_4$, $\sum_\mu\gamma^\mu\gamma_\alpha\gamma_\mu=2\gamma_\alpha$, $\sum_\mu\gamma^\mu\gamma_\alpha\gamma_\beta\gamma_\mu=-4\varepsilon_\alpha\delta_{\alpha\beta}I_4$ and $\sum_\mu\gamma^\mu\gamma_\gamma\gamma_\beta\gamma_\alpha\gamma_\mu=-2\gamma_\gamma\gamma_\beta\gamma_\alpha$.

## Summary

The electron is the biquaternion Dirac field $\tilde{Ξ}_{\mathrm{sp}}\in\mathbb{B}$: one element whose two chirality parts satisfy the pair $\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp},R} = k_{m_e}\tilde{Ξ}_{\mathrm{sp},L}$, $\tilde{\nabla}^{\natural}\tilde{Ξ}_{\mathrm{sp},L} = k_{m_e}\tilde{Ξ}_{\mathrm{sp},R}$. The mass is the coefficient of the off-diagonal coupling of the two values; the algebra's real structure $\flat={}-{}^{*}$ acts on the two sectors with opposite signs; and the rest-energy phase $\exp(-i\,k_{m_e}r'_t) = \cos(k_{m_e}r'_t)\,e_t - \sin(k_{m_e}r'_t)\,(ie_t)$, which is $\exp(-i k_{t}^{\prime}r'_t)$ with $k_{t}^{\prime}=k_{m_e}$ at rest, rotates the two sectors into one another at the angular frequency $c\,k_{m_e}=m_ec^{2}/\hbar$. The charge is inserted at the gradient by minimal coupling, which for the linear mass pair is exactly gauge covariant; the conserved current then lies in $\mathbb{B}_{\Phi}$, while the static Coulomb field of a point charge is a purely imaginary vector and lies in $\mathbb{B}_{\Psi}$.

The framework derives the electron's spin-$\tfrac{1}{2}$ representation content from the unique irreducible action of $\mathbb{B}\cong M_2(\mathbb{C})$ on a complex space of dimension two, and the spin state and observable structure from the state of $\mathbb{B}_{\Psi}$ with the Born pairing; the magnitude $\frac{m\,c}{2\,k_m}$ is a normalisation. It derives the tree-level gyromagnetic factor $g=2$ from the $1/2m_e$ coefficient produced by eliminating the small part, giving $\vec\mu_e = -(e/m_e)\vec S$ and one Bohr magneton $\mu_B = ec\dfrac{1}{2\,k_{m_e}} = 9.274010\times10^{-24}$ J T$^{-1}$; the anomalous part $a\approx\alpha/2\pi$ is outside the equation. It reproduces the Zitterbewegung at $\omega_Z = 2c\,k_{t}^{\prime} = 2c\,k_{m_e} = 1.55269\times10^{21}$ rad s$^{-1}$, twice the temporal coordinate of $\tilde K_{\Phi}$ times $c$, and at amplitude $\frac{1}{2\,k_{m_e}}= 193.1$ fm, and the companion article's test shows the trembling is the second harmonic of the sector rotation, not a signature of either sector. It contains the two values of the chirality and the mass term as the chirality-mixing coupling, but not the weak $V-A$ coupling of the left-handed electron.

The electron's data are not confined to either sector: state-like and field-strength-like data are $\mathbb{B}_{\Psi}$, current is $\mathbb{B}_{\Phi}$, the real structure $\flat$ acts on the two sectors with opposite signs while the mass term couples the two chirality values, and the rest-energy phase rotates the sectors into one another. What the framework cannot supply is the electron's mass, its charge, its anomalous moment, its empirical signature, and any reason to single it out among spin-$\tfrac{1}{2}$ fields. Those are the labelled gaps, and they are not closed by the notation.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $Q_t=i r'_t$, $Q_k=x,y,z$ | Coordinates; $r'_t$ the real time of the material sector |
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | The four units of the coefficient basis |
| $i$ | Scalar imaginary, $i^2 = -1$ |
| $\natural$, $\bar{\cdot}$, ${}^{*}$ | Quaternion, complex, Hermitian conjugations |
| $\mathbb{B}_{\Phi}$, $\mathbb{B}_{\Psi}$ | Anti-Hermitian (material) and Hermitian (informational) subspaces |
| $\mathbb{B}_{H}$ | Real quaternion subspace |
| $\tilde{\nabla}$ | Biquaternionic gradient, of *Operator and Calculus Conventions* |
| $\Box$ | Central d'Alembertian |
| $\tilde{Ξ}_{\mathrm{sp}}$ | Biquaternion Dirac field |
| $\tilde{Ξ}_{\mathrm{sp},L}$, $\tilde{Ξ}_{\mathrm{sp},R}$ | The parts of the field of value $L$ and of value $R$ |
| $\tilde{Q}^\flat = -\tilde{Q}^{*}$ | The algebra's real structure (not the mass term) |
| $\tilde{Ϛ}_{\Psi}(\vec u)$ | Spin state along a declared unit direction, in $\mathbb{B}_{\Psi}$ |
| $\mathrm{Sc}$, $\mathrm{Vect}$ | Scalar and vector parts of an algebra element |
| $\langle\tilde Q\rangle_\natural = \tilde Q\tilde Q^\natural$ | Quaternionic norm |
| $\mathrm{Tr}(\tilde Q_1\tilde Q_2)$ | Trace pairing, read as $2\,\mathrm{Sc}(\tilde Q_1\tilde Q_2)$ at normalisation |
| $\tilde{J}_{\Phi} = ic\,j_0 e_t + \vec j$ | Conserved four-current, in $\mathbb{B}_{\Phi}$ |
| $\tilde{F} = iϙ\vec u_x/(4\pi\sqrt{\epsilon}\|(r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z)\|^2)$ | Coulomb field of a point charge, in $\mathbb{B}_{\Psi}$; $\vec u_x$ the radial unit vector |
| $\tilde K_{\Phi}=\frac{\tilde P_{\Phi}}{\hbar}=i\,k_{t}^{\prime}e_t+\vec k_{\Phi}$ | Wave-number biquaternion; $k_{t}^{\prime}=E/(\hbar c)=\omega/c$, $\vec k_{\Phi}=\vec p/\hbar$ |
| $\mathrm{Sc}(\tilde K_{\Phi}\tilde R_\Phi^{\natural})=\vec k_{\Phi}\cdot\vec r-k_{t}^{\prime}r'_t$ | The phase of every plane wave in the article |
| $\varepsilon=(1,-1,-1,-1)$ | Sign weights of the $\mathbb{B}_{\Phi}$ frame; metric in the closing section |
| $m_e$, $e$, $\frac{m\,c}{k_m}$, $c$ | Electron mass, elementary charge, reduced Planck constant, speed of light |
| $\mathcal{N}F = (i\partial/\partial r'_t+\vec\nabla)F - k_{m_e}i\,\overline{F}\,\vec e_z$, $\vec\nabla=\sum_k\vec e_k\partial/\partial R_k$ | Two-sided Dirac equation of the dictionary form |
| $g$, $\mu_B = ec\dfrac{1}{2\,k_{m_e}}$ | Gyromagnetic factor; Bohr magneton |
| $\chi=i\tilde{Ζ}_{\mathrm{ad}}$, $\Gamma = -iR_{\mathrm{axf},\vec e_z}$ | Central chirality grading and its representative; closing section |
| $L_a$, $R_b$, $T_{a,b}=L_aR_b$ | Left and right multiplication and their cell; closing section |
| $C = -iL_{\mathrm{pau},\vec e_y}R_{\mathrm{pau},\vec e_z}$ | Charge-conjugation cell; closing section |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- P. A. M. Dirac, "The quantum theory of the electron," *Proceedings of the Royal Society A* **117** (1928) 610–624, for the original Dirac equation and the prediction $g=2$.
- P. A. M. Dirac, *The Principles of Quantum Mechanics* (Oxford, 1930), for the velocity operator and the spin-$\tfrac{1}{2}$ formalism.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the standard treatment of the electron, its current, and its magnetic moment.
- J. J. Sakurai, *Advanced Quantum Mechanics* (Addison-Wesley, 1967), for the non-relativistic limit, the Darwin term, and the Zitterbewegung.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, Vol. 1 (Cambridge, 1984), for the two-component spinor calculus and the Weyl spinors.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the spacetime-algebra account of the Dirac electron.
- V. V. Kravchenko, "On a Biquaternionic Bag Model," *Zeitschrift für Analysis und ihre Anwendungen* **14** (1995), no. 1, 3–14, for the two-sided biquaternionic Dirac equation with the conjugation in the mass term.
- CODATA Task Group on Fundamental Constants, *CODATA recommended values of the fundamental physical constants* (2018), for $m_e$, $e$, $\frac{m\,c}{k_m}$, and the measured electron magnetic moment.
- The companion articles of this series: [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html), [The Dirac Equation in Biquaternionic Form — Solutions and the Non-Relativistic Limit](the-dirac-equation-in-biquaternionic-form-solutions-and-the-non-relativistic-limit.html), [The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism](the-minimal-coupling-of-the-biquaternion-dirac-field-to-electromagnetism.html), [Zitterbewegung in Biquaternionic Form](zitterbewegung-in-biquaternionic-form.html), [Spin-1/2 Quantum Physics in Biquaternionic Form](spin-1-2-quantum-physics-in-biquaternionic-form.html), [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html), and [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html).
