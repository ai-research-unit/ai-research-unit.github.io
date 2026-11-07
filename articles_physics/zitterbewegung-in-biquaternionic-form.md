# __Zitterbewegung in Biquaternionic Form__

## Introduction

The **Zitterbewegung** — the "trembling motion" — is the oscillatory part of the position of a Dirac particle. It was found by Schrödinger in 1930, in the course of solving the free Dirac equation. In the single-particle theory the velocity operator has eigenvalues $\pm c$, so a Dirac particle cannot have a sharp velocity; a wave packet assembled from positive- and negative-frequency plane waves has a mean position whose expectation value carries a rapid oscillation. Its angular frequency is $2c\,k_{t}^{\prime}$, which equals $2c\,k_m$ for a particle at rest, and its amplitude is of the order of half the reduced Compton wavelength $\dfrac{1}{2\,k_m}$. Here $k_m=mc/\hbar$ and $k_{t}^{\prime}=E/(\frac{m\,c^{2}}{k_m})$ are the mass and energy wave numbers.

The biquaternion framework of these articles splits $\mathbb{B}$ by Hermitian conjugation into two sectors, $\mathbb{B} = \mathbb{B}_{\Psi} \oplus \mathbb{B}_{\Phi}$, which multiplication by the central $i$ exchanges. The natural suggestion is that this is the same split the Zitterbewegung exploits: that the positive- and negative-energy parts of the field *are* its $\mathbb{B}_{\Phi}$ and $\mathbb{B}_{\Psi}$ parts, and that the trembling is therefore the observable face of the complexification.

This article tests that suggestion rather than assuming it. The finding is mixed, and it is stated plainly from the outset. The oscillation can be derived and its frequency checked, and the mass does set the sector rotation: the rest-energy phase turns the two sectors into one another at $c\,k_m$; but the identification of the $\pm$-energy parts with the two sectors does **not** hold, because the energy sign is fixed by a map that multiplies the field on the right, while the sector is fixed by a conjugation of its value. The two splits have the same physical scale — the mass — and that is why the suggestion is tempting, but they are splits of different objects by different operations. Section *Does the Sector Split Do Real Work?* gives the argument, and Section *What Survives* separates the claims that hold from the one that does not.

The article is organised as follows. The next section recalls the standard picture, writes the Heisenberg velocity identity, and records the three contested readings of the effect. The section after fixes the biquaternion setting and the plane-wave branches, following the parent. The following section recomputes the oscillation with the maps written out, reduces every factor of $i$ with $i^2=-1$, and checks the frequency and the amplitude on cases chosen independently of the rest case. A short section then isolates the genuinely algebraic content — the real structure as a diagonal action with opposite signs on the sectors, and the rest-energy phase as a rotation between them — and shows that the Zitterbewegung phase is the square of the free-evolution phase, so its frequency is twice the sector-rotation frequency. The central section tests the sector identification and reports its failure. The closing sections record the relation to the companion article on the electron, set the cell notation alongside the standard Dirac notation in one place and for comparison only, and summarise the statements that survive. Nothing here depends on the electron article; the connection is noted where relevant.

## The Standard Picture

The dynamics in the algebra is the pair of the parent,

$$
\tilde{\nabla}\tilde{Ξ}_{\mathrm{sp},R} = k_m\tilde{Ξ}_{\mathrm{sp},L}, \qquad \tilde{\nabla}^{\natural}\tilde{Ξ}_{\mathrm{sp},L} = k_m\tilde{Ξ}_{\mathrm{sp},R}
$$

(*The Dirac Equation in Biquaternionic Form*, §*Statement*). The standard picture, which this section follows, reads the equation first order in time,

$$\frac{m\,c^{2}\,i}{k_m}\frac{\partial\tilde{Ξ}_{\mathrm{sp}}}{\partial  r'_t} = H\tilde{Ξ}_{\mathrm{sp}}, \qquad H = c\sum_{k=x,y,z} p_k\,\alpha_k + \beta\,mc^2,
$$

with $p_k=-\frac{m\,c\,i}{k_m}\partial/\partial r_k$ and the two maps

$$
\alpha_k:\ \tilde Q\mapsto\vec e_k\,\tilde Q\,\vec e_z, \qquad \beta:\ \tilde Q\mapsto i\,\tilde Q\,\vec e_x .
$$

The composition of two such maps is that of *Operator Family Conventions*, §*The Slots*, and is not restated here. The map $\beta$ multiplies on the right only: the time unit it would carry on the left adds nothing. The maps satisfy

$$
\{\alpha_j,\alpha_k\} = 2\delta_{jk}\,\mathrm{id}, \qquad \{\alpha_k,\beta\} = 0, \qquad (\alpha_k)^2 = \mathrm{id},
$$

so the velocity $c\alpha_k$ has eigenvalues $\pm c$ and the Hamiltonian has eigenvalues $\pm E$ with $E = \sqrt{\vec p^2c^2 + m^2c^4}$.

The oscillation follows from the Heisenberg equation. Because $\{\alpha_k,H\} = 2cp_k\,\mathrm{id}$, the velocity in the Heisenberg picture has the exact form, with $\frac{m\,c}{k_m}$ kept explicit

$$
\boxed{\;\alpha_k(r'_t) = \frac{cp_k}{H} + \exp(\frac{k_m\,i\,H\,r'_{t}}{m\,c^{2}})\Big(\alpha_k(0) - \frac{cp_k}{H}\Big)\exp(-\frac{k_m\,i\,H\,r'_{t}}{m\,c^{2}})\;},
$$

in which the first term is the constant drift velocity and the second is the *trembling* term; $cp_k/H$ is the operator $cp_kH^{-1} = cp_kH/E^2$. Write $A_k=\alpha_k(0)-cp_k/H$. Because $A_k$ anticommutes with $H$, the second term can be written in either of the equivalent forms

$$
\exp(\frac{k_m\,iHr'_{t}}{m\,c^{2}})\,A_k\,\exp(-\frac{k_m\,iHr'_{t}}{m\,c^{2}})=A_k\,\exp(-\frac{2\,k_m\,iHr'_{t}}{m\,c^{2}})=\exp(\frac{2\,k_m\,iHr'_{t}}{m\,c^{2}})\,A_k,
$$

and the last form is what makes the integration below elementary. On the two energy branches the eigenvalues of the oscillating factor are $\exp(\pm \frac{2\,k_m\,iEr'_{t}}{m\,c^{2}})$, so the angular frequency is $2c\,k_{t}^{\prime}$, and integrating once gives the position

$$
\boxed{\;r_k(r'_t) = r_k(0) + \frac{c^2p_k}{H}\,r'_t \;-\;\frac{m\,c^{2}\,i}{2\,k_m\,H}\Big(\exp(\frac{2\,k_m\,i\,H\,r'_{t}}{m\,c^{2}})-1\Big)A_k\;}.
$$

At rest, $H = \beta mc^2$ and the oscillating term has frequency $2c\,k_m$ and amplitude of order $\dfrac{1}{2\,k_m}$, half the reduced Compton wavelength. The interference interpretation is immediate: a positive-frequency component $\exp(-\frac{k_m\,iEr'_{t}}{m\,c^{2}})$ and a negative-frequency component $\exp(+\frac{k_m\,iEr'_{t}}{m\,c^{2}})$ beat at $2c\,k_{t}^{\prime}$, and the trembling term is exactly that beat.

The interpretation of this result is contested, and the article does not settle it. Three positions are in the literature. First, the trembling is an artefact of forcing a single-particle interpretation on a theory whose solutions include both signs of energy: the Foldy–Wouthuysen mean position, the observable position for a positive-energy particle, has no trembling at leading order, so the oscillation is removed rather than seen. Second, the effect is not entirely empty: the same elimination of the negative-frequency part that produces the mean position leaves the **Darwin term** at the next order in $1/c$, and the Darwin term and the Zitterbewegung are two faces of the same admixture of the negative-frequency part — the [exercise on the non-relativistic limit](exercise-the-non-relativistic-limit-and-the-pauli-equation.html) derives that term, and the derivation is not repeated here. Third, in quantum field theory the position operator of a single particle is not fundamental, the free-field Zitterbewegung is not directly observable, and the effect is reinterpreted (in some treatments absorbed, in others associated with virtual pair creation and annihilation). None of these interpretations denies the algebra above; they disagree about what it describes.

## The Biquaternionic Setting

The algebra, its units and its coefficients are those of *Algebra and Element Conventions*; the gradient, the two sides and the momentum operator those of *Operator and Calculus Conventions*; the coordinate, the metric and the frame those of *Frame and Metric Conventions*; the two sectors and the conjugation those of *Algebra and Element Conventions*, §*The Hermitian and Anti-Hermitian Subspaces* and §*The Conjugations*. No formula of theirs is restated here.

The biquaternionic Dirac equation is the parent's linear pair, off-diagonal in the value,

$$
\begin{aligned}
\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R} &= k_m\tilde{Ξ}_{\mathrm{sp},L},\\[2pt]
\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L} &= k_m\tilde{Ξ}_{\mathrm{sp},R},
\end{aligned}
$$

for a field of mass $m$. The field is one element $\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp},L}+\tilde{Ξ}_{\mathrm{sp},R}$ of $\mathbb{B}$, and its two parts carry the two values of the subscript. Each line multiplies the part with one value by the gradient and pairs it with the part of the other value; the mass is the term that carries the value across, and it is the only such term. At $m=0$ the pair decouples into the two one-sided equations $\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R}=0$ and $\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L}=0$, one for each value.

The conjugation $\flat$ is the algebra's real structure, not the mass term (§*The Conjugations* of the conventions article cited above). The corpus also carries a **two-sided** form of the same physics — Kravchenko's single equation on $\mathbb{B}$, in which the mass acts by right multiplication through $\vec e_z$ and a conjugation supplies the antilinear part — but the two forms are related by a dictionary and are not the same operator (parent, §*The One-Sided and the Two-Sided Equation*). The Zitterbewegung derivation below uses the pair.

The plane-wave solutions are

$$
\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp},0}\exp\!\Big(i\,\mathrm{Sc}\big(\tilde P_{\Phi}\tilde{R}_\Phi^{\natural}\big)\frac{k_m}{m\,c}\Big),\frac{k_m\,\tilde{P}_{\Phi}}{m\,c}=\frac{k_m\,e_{t}\,i\,E}{m\,c^{2}}+\vec k_\Phi,
\qquad
\tilde R_\Phi=e_t(i r'_t)+\vec r,
$$

with $\tilde{Ξ}_{\mathrm{sp},0}$ a constant element and $\vec r=r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z$. The single mass-shell condition is

$$
\tilde P_{\Phi}\tilde P_{\Phi}^{\natural}= -m^{2}\,c^{2}.
$$

The two roots of that condition — positive and negative frequency — are the two branches

$$
\tilde{Ξ}_{\mathrm{sp}}^{(+)}=\tilde{Ξ}_{\mathrm{sp},0}^{(+)}\exp\!\Big(-i\frac{Er'_t/c-\vec p\cdot\vec r}{\frac{m\,c}{k_m}}\Big),
\qquad
\tilde{Ξ}_{\mathrm{sp}}^{(-)}=\tilde{Ξ}_{\mathrm{sp},0}^{(-)}\exp\!\Big(+i\frac{Er'_t/c-\vec p\cdot\vec r}{\frac{m\,c}{k_m}}\Big),
$$

constructed in the parent, with $E = +\sqrt{\vec p^2c^2 + m^2c^4}$ and constant elements $\tilde{Ξ}_{\mathrm{sp},0}^{(\pm)}$. The normalisation and the non-relativistic reduction belong to the parent; the present article uses only the branches and the mass shell.

One fact about the field will be needed throughout, and it is the sector action of the real structure: $\flat$ acts as $-1$ on the $\mathbb{B}_{\Psi}$ part of the field and $+1$ on its $\mathbb{B}_{\Phi}$ part, so its fixed space is $\mathbb{B}_{\Phi}$ (§*The Conjugations*). The physical Majorana mass is a different object: it is built on charge conjugation, not on the algebra's $\flat$ (see *Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form*). What the diagonal action of the real structure, the mass coupling of the two values, and the rest-energy phase do to the sectors is the subject of the section *The Complexification and the Rest-Energy Phase*.

## Recomputing the Oscillation

The generators of the parent are the map $\beta$ of *The Standard Picture* and three spatial maps, written in cells as $iL_{\mathrm{axf},\vec e_k}R_{\mathrm{axf},\vec e_y}$. With the action, the composition and the unit of *Operator Family Conventions*, and with the structure constants of the units, they give

$$
\left(iR_{\mathrm{axf},\vec e_x}\right)^2 = \mathrm{id}, \qquad
\left(iL_{\mathrm{axf},\vec e_k}R_{\mathrm{axf},\vec e_y}\right)^2 = -\mathrm{id}, \qquad
\{iR_{\mathrm{axf},\vec e_x},\, iL_{\mathrm{axf},\vec e_k}R_{\mathrm{axf},\vec e_y}\} = 0,
$$

so the four maps carry the sign pattern of the frame, $\varepsilon=(1,-1,-1,-1)$. The product of the time map with a spatial map is the map $\alpha_k$ of the Hamiltonian. It is one line, the two factors $i$ and the order of the two spatial units,

$$
\beta\, iL_{\mathrm{axf},\vec e_k}R_{\mathrm{axf},\vec e_y}
= i^2\,L_{\mathrm{axf},\vec e_k}R_{\mathrm{axf},\vec e_y\vec e_x}
= -L_{\mathrm{axf},\vec e_k}R_{\mathrm{axf},-\vec e_z}
= L_{\mathrm{axf},\vec e_k}R_{\mathrm{axf},\vec e_z},
$$

because $\vec e_y\vec e_x=-\vec e_z$ and a cell is linear in its second multiplier; the last cell is the map $\alpha_k$ of *The Standard Picture*. The relations $\{\alpha_j,\alpha_k\} = 2\delta_{jk}\,\mathrm{id}$, $\{\alpha_k,\beta\} = 0$ and $H^2 = E^2\,\mathrm{id}$ all follow, and each was checked numerically.

The identity boxed in *The Standard Picture* is exact, and $cp_k/H$ in it denotes the operator $cp_kH^{-1} = cp_kH/E^2$ — not a multiple of the identity, since $H$ is an operator and not a scalar. The three equivalent forms of that section rest on $\{\alpha_k-cp_k/H,\,H\}=0$, which the relations above give.

The identity was checked by direct computation on a case chosen here rather than on the rest case that motivated it: momentum $\vec p/mc = (0.3,\,0.2,\,-0.1)$, so $|\vec p| = 0.374\,mc$ and $E = 1.0677\,mc^2$, at the three times $r'_t = 0.017, 0.05, 0.23$ in units of $1/k_m/c$. The left side $\exp(\frac{k_m\,iHr'_{t}}{m\,c^{2}})\alpha_k \exp(-\frac{k_m\,iHr'_{t}}{m\,c^{2}})$ and both equivalent forms on the right agreed to machine precision, the largest coefficient of the difference below $10^{-15}$ over all three components and all times. The integrated position formula was checked the same way, against a direct integration of $c\alpha_k(r'_t)$ from the eigen-decomposition of $H$; the largest coefficient of the difference was below $5\times10^{-16}$. The rest case is then a consequence, $E = mc^2$, not an input.

The frequency is $2c\,k_{t}^{\prime}$ on general grounds and $2c\,k_m$ at rest. The numbers for the electron, $m_ec^2 = 0.510998950$ MeV and $\frac{m\,c}{k_m}= 6.582119569\times10^{-22}$ MeV s, are

$$
\boxed{\;\omega_Z^{\text{rest}} = 2c\,k_{m_e} = 1.55269\times10^{21}\ \text{rad s}^{-1},
\qquad f_Z = \frac{\omega_Z}{2\pi} = 2.47118\times10^{20}\ \text{Hz}\;},
$$

Here $1/k_{m_e}=\hbar/(m_ec)$ is the electron mass length.

which is the standard value. On a relativistic case chosen independently, with Lorentz factor $2$ so $E = 2mc^2$, the formula gives $2c\,k_{t}^{\prime} = 4c\,k_m = 3.10538\times10^{21}\ \text{rad s}^{-1}$ — twice the rest value, as the formula requires and as the rest case alone would not reveal. The oscillation amplitude is $\dfrac{1}{2\,k_m}$, which for the electron is $193.1$ fm, half the reduced Compton wavelength $386.2$ fm. Both the frequency and the amplitude are the standard ones; the biquaternion notation reproduces them without alteration.

It should be said clearly that this derivation uses the map $\beta$ of *The Standard Picture*, which multiplies the field on the right, and that no left multiplication by an element of $\mathbb{B}$ does the same. That will matter in the test that follows.

## The Complexification and the Rest-Energy Phase

There is a genuinely algebraic statement available, and it is the strongest positive result of the article. It has two parts.

**The real structure is diagonal on the sectors.** The conjugation $\flat$ acts as $-1$ on the $\mathbb{B}_{\Psi}$ part of the field and $+1$ on its $\mathbb{B}_{\Phi}$ part: it **preserves** each sector and marks it with a sign. This is a property of the algebra's real structure, not of the mass term; the parent's mass is the linear term that couples the two values, and, being a real scalar, it leaves each element's sector membership untouched. The operation that exchanges the two sectors is multiplication by the central $i$ (§*The Conjugations*).

**The rest-energy phase rotates the sectors into one another.** Factoring out the rest energy writes the free phase as

$$
\exp(-i r'_t\,k_m) = \cos\!\Big(c\,k_m\,r'_{t}\Big)e_t \;-\; \sin\!\Big(c\,k_m\,r'_{t}\Big)(ie_t),
$$

and the two terms lie in different sectors: $e_t \in \mathbb{B}_{\Psi}$ and $ie_t \in \mathbb{B}_{\Phi}$ (an imaginary scalar is anti-Hermitian). The rest-energy phase is therefore a **rotation between the sectors**, at angular frequency $c\,k_m$: it takes the $\mathbb{B}_{\Psi}$ direction $e_t$ toward the $\mathbb{B}_{\Phi}$ direction $ie_t$ and back. This is the sense in which the complexification rotates one sector into the other; the rotation is the central phase, whose frequency the mass fixes through the mass shell.

The Zitterbewegung frequency is exactly twice this rate. That is not a coincidence of arithmetic but an algebraic relation: the oscillating factor of the velocity identity is $\exp(\frac{2\,k_m\,iHr'_{t}}{m\,c^{2}})$, the square of the free-evolution phase $\exp(\frac{k_m\,iHr'_{t}}{m\,c^{2}})$,

$$
\exp(\frac{2\,k_m\,iHr'_{t}}{m\,c^{2}})=\big(\exp(\frac{k_m\,iHr'_{t}}{m\,c^{2}})\big)^2.
$$

The rest-frame eigenvalues of the free-evolution phase are $\exp(\pm i r'_t\,k_m)$, one of which is the sector rotation above; the eigenvalues of the oscillating factor at general momentum are $\exp(\pm \frac{2\,k_m\,iEr'_{t}}{m\,c^{2}})$, the sign set by the energy branch, so only the magnitude of the frequency is physical. So the trembling is not the sector rotation itself; it is the second harmonic of it. The factor of two is the statement that the beat of two branches of opposite frequency is twice the frequency of either branch, and it is the same factor by which the rest-energy phase and the Zitterbewegung frequency differ.

Two consequences deserve emphasis. First, since the rest-energy phase rotates the sectors and its rate is the mass, the scale of the trembling — the mass gap $2mc^2$ — is set by the same quantity that sets the sector rotation. That is the real content of the suggestion that the trembling and the complexification are related. Second, a relation of scale is not a relation of identity: the trembling is a beat of two energy branches, the sector rotation is a rotation in the algebra, and the following section shows these are different decompositions.

## Does the Sector Split Do Real Work?

The claim to test is: *the positive- and negative-energy parts of the field are its $\mathbb{B}_{\Phi}$ and $\mathbb{B}_{\Psi}$ parts.* The test fails, and the reason is structural rather than numerical.

**They are splits of different objects.** The energy sign separates two terms of a solution by their dependence on $r'_t$: a term of positive frequency carries the factor $\exp(-\frac{k_m\,iEr'_{t}}{m\,c^{2}})$ and one of negative frequency the factor $\exp(+\frac{k_m\,iEr'_{t}}{m\,c^{2}})$, and $E$ moves with the momentum. It is a split of the solutions of the pair. The sector split separates the value of one element at one point, by Hermitian conjugation; it is pointwise and knows nothing of $r'_t$ or of $\vec p$. A split of a family of functions and a split of the values the functions take are different objects, and no dictionary is stated that would identify them.

**The energy sign is fixed by a multiplication on the right, the sector by an involution of the value.** The Hamiltonian contains the map $\beta$, which multiplies on the right by $\vec e_x$, and its kinetic terms multiply on the right by $\vec e_z$. No element of the algebra acts as $\beta$ by left multiplication, and two units already show it. If some $c$ gave $c\tilde Q=i\tilde Q\vec e_x$ for every $\tilde Q$, the value at $\tilde Q=e_t$ would force $c=i\vec e_x$; at $\tilde Q=\vec e_z$ that $c$ gives $c\vec e_z=i\vec e_x\vec e_z=-i\vec e_y$, while $\beta$ gives $i\vec e_z\vec e_x=+i\vec e_y$, and the two differ. A left multiplier that agrees with $\beta$ on one element fails on another. So the energy sign is decided by a map built from right multiplications, and the sector by the conjugation of the value, which is not a map at all. $\beta$ is a map on the algebra and not an element of it, so it lies in neither sector; the sectors are properties of elements.

**A momentum argument reinforces this.** The sector split is momentum-independent: whether an element is Hermitian is a property of the element, not of any wave it carries. The energy sign is momentum-dependent through the $\vec p$ of the kinetic term. A momentum-independent split cannot be a momentum-dependent one except at $\vec p = 0$, and even there the two rest branches land in the same sector, as the next paragraph shows.

**The natural dictionary the corpus supplies points the other way.** The parent's state construction reads an amplitude as the pure state $\tfrac12\big(e_t + i\vec u\big) \in \mathbb{B}_{\Psi}$, with $\vec u$ the direction the amplitude carries; the direction comes from the amplitude and not from the energy sign. Each of the two rest branches of the parent gives such an element, and neither gives an element of $\mathbb{B}_{\Phi}$. The sector $\mathbb{B}_{\Phi}$ is where the *current* lives, $\tilde J_{\Phi} = ic\,j_0e_t + \vec j \in \mathbb{B}_{\Phi}$, not where the negative-frequency branch lives. So on the dictionary actually available, the sector split tracks the state–current distinction, not the energy sign, and both energy signs land in the same sector.

The honest conclusion, then, is that the $\mathbb{B}_{\Psi}/\mathbb{B}_{\Phi}$ split **renames the Hermitian decomposition of the algebra and not the $\pm$-energy decomposition of the field**. It is not obviously "doing work": the two splittings share the mass scale, but the interference that produces the trembling is between energy branches, and the energy branches are not the sectors. The natural candidate for a splitting that does carry the interference is the value subscript. The pair carries it: the derivative multiplies on the left and keeps it, and the mass is the term that carries it across, so at $m=0$ each equation stands alone with one value, and in the massless limit the value is locked to the helicity. But each of the two equations has solutions of both frequency signs, since the massless dispersion relation admits both, so the value does not coincide with the energy sign either: it is a splitting of the field by the equation it obeys, not a splitting of the algebra into $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{\Phi}$. What is settled is that the $\pm$-energy split is neither the $\mathbb{B}_{\Psi}/\mathbb{B}_{\Phi}$ split nor the split by value, for the reasons above.

## What Survives

The following table separates the claims.

| Claim | Status |
|---|---|
| The trembling is an interference of $\pm$-frequency branches, frequency $2c\,k_{t}^{\prime}$ | Established; the standard result, recomputed here |
| Rest-frame frequency $2c\,k_m$, amplitude $\dfrac{1}{2\,k_m}$ | Established; checked numerically above |
| The real structure $\flat$ acts with opposite signs on $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{\Phi}$ | Established; it is the sector action of the conjugation |
| The rest-energy phase rotates the sectors at $c\,k_m$ | Established; with $\theta=r'_t\,k_m$, $\exp(-i\theta) = \cos\theta\,e_t - \sin\theta\,(ie_t)$ |
| The Zitterbewegung phase is the square of the free-evolution phase | Established; hence the frequency is doubled |
| $\pm$-energy parts **are** the $\mathbb{B}_{\Phi}$ and $\mathbb{B}_{\Psi}$ sectors | False as an identity; the energy sign is fixed by a map that multiplies on the right, the sector by a conjugation of the value |
| The $\mathbb{B}_{\Psi}/\mathbb{B}_{\Phi}$ split does work beyond relabelling the Hermitian decomposition | Not established; the interference is between energy branches, which are not the sectors |

What survives is a relation of *scale and phase*, not of identity. The mass sets both the sector-rotation rate and the gap whose interference is the trembling; the trembling frequency is twice the sector-rotation frequency because the trembling phase is the square of the evolution phase. This makes the Zitterbewegung a place where the mass term and the two sectors are simultaneously visible, and it is a legitimate point of contact between the Dirac solutions and the sector decomposition. It does not make the trembling the observable face of the complexification in the strong sense proposed.

## Zitterbewegung and the Electron

The Zitterbewegung is usually introduced as a property of the electron, and a [companion article on the electron in biquaternionic form](the-electron-in-biquaternionic-form.html) has since been written in this group. Nothing in the present article depends on it. The two agree on the result: the electron article records the same frequencies and amplitudes, reports that the identification of the energy branches with the sectors fails, and keeps the relation of scale and phase. Its electron gives the numbers $1.55269\times10^{21}\ \text{rad s}^{-1}$ and $193.1$ fm, which are the ones computed above, and its rest energy is the scale of both the sector rotation and the trembling.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The generators carry no frame label: $\gamma_\mu$ is one set of matrices, $\gamma_0^2=I_4$ and $\gamma_k^2=-I_4$. The frame belongs to the coordinate, not to the array.

The gammas are a frame of the cell algebra $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra. They are recorded here for comparison with the standard Dirac notation; the derivation above uses only the cells $\beta$ and $\alpha_k$.

Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\tilde{Ξ}_{\mathrm{sp}}=a\tilde{Ξ}_{\mathrm{sp}}$ and $R_b\tilde{Ξ}_{\mathrm{sp}}=\tilde{Ξ}_{\mathrm{sp}} b$, and $c(M)$ is the coefficient matrix of $M$ in the basis of the sixteen products.

$$
\begin{aligned}
\gamma_0 &= iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_x}, &\gamma_1 &= iL_{\mathrm{pau},\vec e_x}R_{\mathrm{pau},\vec e_y},\\[2pt]
\gamma_2 &= iL_{\mathrm{pau},\vec e_y}R_{\mathrm{pau},\vec e_y}, &\gamma_3 &= iL_{\mathrm{pau},\vec e_z}R_{\mathrm{pau},\vec e_y},\\[2pt]
\gamma_5 &= -iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_z}.
\end{aligned}
$$

The same in the axis-free display:

$$
\begin{aligned}
\gamma_0 &= iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_x}, &\gamma_1 &= iL_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_y},\\[2pt]
\gamma_2 &= iL_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_y}, &\gamma_3 &= iL_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y},\\[2pt]
\gamma_5 &= -iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_z}.
\end{aligned}
$$

They satisfy $\{\gamma_\mu,\gamma_\nu\}=2\varepsilon_\mu\delta_{\mu\nu}L_{\mathrm{pau},e_t}R_{\mathrm{pau},e_t}$ with $\varepsilon=(1,-1,-1,-1)$, the product $\gamma_5=i\gamma_0\gamma_1\gamma_2\gamma_3$ squares to the identity, and $\gamma_5$ anticommutes with all four: $\{\gamma_\mu,\gamma_5\}=0$.

A single cell $L_aR_b$ is a pure tensor; a single product is one cell up to a phase, the products form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and a general element is a sum of at most four, with $\ell(M)=\operatorname{rank}c(M)$.

$\gamma_5$ is the reference-frame cell of the chirality operator $\Gamma$; the central grading $\xi$ — the difference of the two central idempotents of the complexified algebra, so $\chi^2=e_t$ — is a different object, represented by $\gamma_5$ on the Dirac module.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{\mathrm{axf},e_\mu}=C_{\Pi}L_{\mathrm{pau},e_\mu}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

The Zitterbewegung was derived in the biquaternion notation of the series. The Heisenberg velocity satisfies the exact identity $\alpha_k(r'_t) = cp_k/H + \exp(\frac{k_m\,iHr'_{t}}{m\,c^{2}})(\alpha_k(0)-cp_k/H)\exp(-\frac{k_m\,iHr'_{t}}{m\,c^{2}})$, checked at momentum $|\vec p| = 0.374\,mc$ and three times, to machine precision (the largest coefficient of the difference below $10^{-15}$); the integrated position formula was checked against a direct integration on the same case, with the largest coefficient of the difference below $5\times10^{-16}$. The oscillating term has frequency $2c\,k_{t}^{\prime}$, equal to $2c\,k_m$ at rest, and the electron value $1.55269\times10^{21}\ \text{rad s}^{-1}$ and amplitude $\dfrac{1}{2\,k_m} = 193.1$ fm were confirmed.

The genuinely algebraic content is that the mass is the linear coupling between the two values of the subscript, that the real structure $\flat$ acts with opposite signs on the two sectors, and that the rest-energy phase $\exp(-i r'_t\,k_m) = \cos(r'_t\,k_m)e_t - \sin(r'_t\,k_m)(ie_t)$ rotates the two sectors into one another at $c\,k_m$. The Zitterbewegung phase is the square of this evolution phase, so its frequency is exactly twice the sector-rotation frequency.

The structural claim that motivated the article fails. The positive- and negative-energy parts of the field are **not** its $\mathbb{B}_{\Phi}$ and $\mathbb{B}_{\Psi}$ parts. The energy sign is the sign of the eigenvalue of a Hamiltonian that multiplies the field on the right, and no element of the algebra does that by left multiplication, while the sectors are fixed by the conjugation of the value; the two are splits of different objects, a family of solutions and the values it takes; and on the dictionary the series supplies, both energy branches correspond to $\mathbb{B}_{\Psi}$ elements while the current lives in $\mathbb{B}_{\Phi}$. The relation between the trembling and the complexification is therefore one of phase and scale — the trembling is the second harmonic of the sector rotation — and not the identity the strong form of the claim requires.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | The biquaternion algebra, *Algebra and Element Conventions* |
| $e_t, \vec e_x, \vec e_y, \vec e_z$ | Its four units, the coefficient basis |
| $i$ | The central scalar imaginary |
| $\mathbb{B}_{\Phi}$, $\mathbb{B}_{\Psi}$ | The anti-Hermitian (material) and Hermitian (informational) sectors |
| $\tilde{Ξ}_{\mathrm{sp}}$, $\tilde{Ξ}_{\mathrm{sp},L}$, $\tilde{Ξ}_{\mathrm{sp},R}$ | The field, one element of $\mathbb{B}$, and its two parts, one per value of the subscript |
| $\tilde{Ξ}_{\mathrm{sp}}^{(+)}, \tilde{Ξ}_{\mathrm{sp}}^{(-)}$ | The two frequency branches; $\tilde{Ξ}_{\mathrm{sp},0}^{(\pm)}$ their constant elements |
| $\tilde R_\Phi$ | The four-position biquaternion of the parent |
| $\tilde K_{\Phi}$ | The wave biquaternion of the parent, $\vec k_\Phi=\vec p\,\frac{k_m}{m\,c}$ |
| $\tilde P_{\Phi}\tilde P_{\Phi}^{\natural} = -m^{2}\,c^{2}$ | Biquaternionic mass-shell condition |
| $\flat$ | The anti-Hermitian conjugation (the algebra's real structure, not the mass term), *Algebra and Element Conventions* |
| $\tilde\nabla$ | The biquaternionic gradient (Dirac operator), *Operator and Calculus Conventions* |
| $L_{a}R_{b}$ | A two-sided cell; its action and its composition are *Operator and Calculus Conventions* and *Operator Family Conventions* |
| $\mathrm{id}$ | The identity map |
| $\beta:\tilde Q\mapsto i\tilde Q\vec e_x$ | The time map, one right multiplication |
| $\alpha_k:\tilde Q\mapsto\vec e_k\tilde Q\vec e_z$ | The three spatial maps |
| $H = c\sum_k p_k\,\alpha_k + \beta mc^2$ | Hamiltonian, $H^2 = E^2\,\mathrm{id}$ |
| $A_k = \alpha_k(0) - cp_k/H$ | Anticommuting part of the velocity, $\{A_k,H\}=0$ |
| $\omega_Z = 2c\,k_{t}^{\prime}$ | Zitterbewegung angular frequency |
| $\dfrac{1}{2\,k_m}$ | Zitterbewegung amplitude (order) |
| $c(M)$, $\ell(M)$ | Coefficient matrix of an element in the sixteen products, and its rank (length) |

Here $k_{\Phi}=\frac{k_m\,p}{m\,c}$ is the momentum wave number.

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- E. Schrödinger, "Über die kräftefreie Bewegung in der relativistischen Quantenmechanik," *Sitzungsberichte der Preußischen Akademie der Wissenschaften* (1930) 418–428, for the original discovery of the Zitterbewegung.
- P. A. M. Dirac, "The quantum theory of the electron," *Proceedings of the Royal Society A* **117** (1928) 610–624, for the Dirac equation and the velocity operator.
- L. L. Foldy and S. A. Wouthuysen, "On the Dirac theory of spin 1/2 particles and its non-relativistic limit," *Physical Review* **78** (1950) 29–36, for the mean position operator and the elimination of the trembling.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the standard Heisenberg-picture treatment and the Darwin term.
- J. J. Sakurai, *Advanced Quantum Mechanics* (Addison-Wesley, 1967), for the Zitterbewegung and the non-relativistic limit.
- W. Greiner, *Relativistic Quantum Mechanics: Wave Equations* (Springer, 2000), for a detailed step-by-step account of the trembling motion.
- P. A. M. Dirac, *The Principles of Quantum Mechanics* (Oxford, 1930), for the velocity operator and its eigenvalues.
- The companion articles of this series: [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html), [The Dirac Equation in Biquaternionic Form — Solutions and the Non-Relativistic Limit](the-dirac-equation-in-biquaternionic-form-solutions-and-the-non-relativistic-limit.html), [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html), [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html), [Exercise: The Non-Relativistic Limit and the Pauli Equation](exercise-the-non-relativistic-limit-and-the-pauli-equation.html), and [Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form](antilinear-structure-and-the-two-kinds-of-mass-in-biquaternionic-form.html).
