# __Zitterbewegung in Biquaternionic Form__

## Introduction

The **Zitterbewegung** — the "trembling motion" — is the oscillatory part of the position of a Dirac particle. It was found by Schrödinger in 1930, in the course of solving the free Dirac equation. In the single-particle theory the velocity operator has eigenvalues $\pm c$, so a Dirac particle cannot have a sharp velocity; a wave packet assembled from positive- and negative-frequency plane waves has a mean position whose expectation value carries a rapid oscillation. Its angular frequency is $2E/\hbar$, which equals $2mc^2/\hbar$ for a particle at rest, and its amplitude is of the order of half the reduced Compton wavelength $\hbar/(2mc)$.

The biquaternion framework of these articles splits $\mathbb{B}$ by Hermitian conjugation into two sectors, $\mathbb{B} = \mathbb{M}_+ \oplus \mathbb{M}_-$, which multiplication by the central $i$ exchanges. The natural suggestion is that this is the same split the Zitterbewegung exploits: that the positive- and negative-energy parts of the field *are* its $\mathbb{M}_-$ and $\mathbb{M}_+$ parts, and that the trembling is therefore the observable face of the complexification.

This article tests that suggestion rather than assuming it. The finding is mixed, and it is stated plainly from the outset. The oscillation can be derived and its frequency checked, and the mass does set the sector rotation: the rest-energy phase turns the two sectors into one another at $mc^2/\hbar$; but the identification of the $\pm$-energy parts with the two sectors does **not** hold, because the energy sign is fixed by a map that multiplies the field on the right, while the sector is fixed by a conjugation of its value. The two splits have the same physical scale — the mass — and that is why the suggestion is tempting, but they are splits of different objects by different operations. Section *Does the Sector Split Do Real Work?* gives the argument, and Section *What Survives* separates the claims that hold from the one that does not.

The article is organised as follows. The next section recalls the standard picture, writes the Heisenberg velocity identity, and records the three contested readings of the effect. The section after fixes the biquaternion setting and the plane-wave branches, following the parent. The following section recomputes the oscillation with the maps written out, reduces every factor of $i$ with $i^2=-1$, and checks the frequency and the amplitude on cases chosen independently of the rest case. A short section then isolates the genuinely algebraic content — the real structure as a diagonal action with opposite signs on the sectors, and the rest-energy phase as a rotation between them — and shows that the Zitterbewegung phase is the square of the free-evolution phase, so its frequency is twice the sector-rotation frequency. The central section tests the sector identification and reports its failure. The closing sections record the relation to the companion article on the electron, set the cell notation alongside the standard Dirac notation in one place and for comparison only, and summarise the statements that survive. Nothing here depends on the electron article; the connection is noted where relevant.

## The Standard Picture

The dynamics in the algebra is the pair of the parent,

$$
\tilde{\nabla}\tilde{Ξ}^{\mathrm{sp}}_R = m\tilde{Ξ}^{\mathrm{sp}}_L, \qquad \tilde{\nabla}^{\natural}\tilde{Ξ}^{\mathrm{sp}}_L = m\tilde{Ξ}^{\mathrm{sp}}_R
$$

(*The Dirac Equation in Biquaternionic Form*, §*Statement*). The standard picture, which this section follows, reads the equation first order in time,

$$
i\hbar\,\frac{\partial\tilde{Ξ}^{\mathrm{sp}}}{\partial r'_t} = H\tilde{Ξ}^{\mathrm{sp}}, \qquad H = c\sum_{k=x,y,z}p_k\,\alpha_k + \beta\,mc^2,
$$

with $p_k=-i\hbar\,\partial/\partial r_k$ and the two maps

$$
\alpha_k:\ \tilde Q\mapsto\vec e_k\,\tilde Q\,\vec e_z, \qquad \beta:\ \tilde Q\mapsto i\,\tilde Q\,\vec e_x .
$$

The composition of two such maps is that of *Operator Family Conventions*, §*The Slots*, and is not restated here. The map $\beta$ multiplies on the right only: the time unit it would carry on the left adds nothing. The maps satisfy

$$
\{\alpha_j,\alpha_k\} = 2\delta_{jk}\,\mathrm{id}, \qquad \{\alpha_k,\beta\} = 0, \qquad (\alpha_k)^2 = \mathrm{id},
$$

so the velocity $c\alpha_k$ has eigenvalues $\pm c$ and the Hamiltonian has eigenvalues $\pm E$ with $E = \sqrt{\vec p^2c^2 + m^2c^4}$.

The oscillation follows from the Heisenberg equation. Because $\{\alpha_k,H\} = 2cp_k\,\mathrm{id}$, the velocity in the Heisenberg picture has the exact form, with $\hbar$ kept explicit

$$
\boxed{\;\alpha_k(r'_t) = \frac{cp_k}{H} + \exp(iH r'_t/\hbar)\Big(\alpha_k(0) - \frac{cp_k}{H}\Big)\exp(-iH r'_t/\hbar)\;},
$$

in which the first term is the constant drift velocity and the second is the *trembling* term; $cp_k/H$ is the operator $cp_kH^{-1} = cp_kH/E^2$. Write $A_k=\alpha_k(0)-cp_k/H$. Because $A_k$ anticommutes with $H$, the second term can be written in either of the equivalent forms

$$
\exp(iHr'_t/\hbar)\,A_k\,\exp(-iHr'_t/\hbar)=A_k\,\exp(-2iHr'_t/\hbar)=\exp(2iHr'_t/\hbar)\,A_k,
$$

and the last form is what makes the integration below elementary. On the two energy branches the eigenvalues of the oscillating factor are $\exp(\pm 2iEr'_t/\hbar)$, so the angular frequency is $2E/\hbar$, and integrating once gives the position

$$
\boxed{\;r_k(r'_t) = r_k(0) + \frac{c^2p_k}{H}\,r'_t \;-\; \frac{i\hbar c}{2H}\Big(\exp(2iH r'_t/\hbar)-1\Big)A_k\;}.
$$

At rest, $H = \beta mc^2$ and the oscillating term has frequency $2mc^2/\hbar$ and amplitude of order $\hbar/(2mc)$, half the reduced Compton wavelength. The interference interpretation is immediate: a positive-frequency component $\exp(-iEr'_t/\hbar)$ and a negative-frequency component $\exp(+iEr'_t/\hbar)$ beat at $2E/\hbar$, and the trembling term is exactly that beat.

The interpretation of this result is contested, and the article does not settle it. Three positions are in the literature. First, the trembling is an artefact of forcing a single-particle interpretation on a theory whose solutions include both signs of energy: the Foldy–Wouthuysen mean position, the observable position for a positive-energy particle, has no trembling at leading order, so the oscillation is removed rather than seen. Second, the effect is not entirely empty: the same elimination of the negative-frequency part that produces the mean position leaves the **Darwin term** at the next order in $1/c$, and the Darwin term and the Zitterbewegung are two faces of the same admixture of the negative-frequency part — the [exercise on the non-relativistic limit](exercise-the-non-relativistic-limit-and-the-pauli-equation.html) derives that term, and the derivation is not repeated here. Third, in quantum field theory the position operator of a single particle is not fundamental, the free-field Zitterbewegung is not directly observable, and the effect is reinterpreted (in some treatments absorbed, in others associated with virtual pair creation and annihilation). None of these interpretations denies the algebra above; they disagree about what it describes.

## The Biquaternionic Setting

The algebra, its units and its coefficients are those of *Algebra and Element Conventions*; the gradient, the two sides and the momentum operator those of *Operator and Calculus Conventions*; the coordinate, the metric and the frame those of *Frame and Metric Conventions*; the two sectors and the conjugation those of *Algebra and Element Conventions*, §*The Hermitian and Anti-Hermitian Subspaces* and §*The Conjugations*. No formula of theirs is restated here.

The biquaternionic Dirac equation is the parent's linear pair, off-diagonal in the value,

$$
\begin{aligned}
\tilde\nabla\tilde{Ξ}^{\mathrm{sp}}_R &= m\tilde{Ξ}^{\mathrm{sp}}_L,\\[2pt]
\tilde\nabla^{\natural}\tilde{Ξ}^{\mathrm{sp}}_L &= m\tilde{Ξ}^{\mathrm{sp}}_R,
\end{aligned}
$$

for a field of mass $m$. The field is one element $\tilde{Ξ}^{\mathrm{sp}}=\tilde{Ξ}^{\mathrm{sp}}_L+\tilde{Ξ}^{\mathrm{sp}}_R$ of $\mathbb{B}$, and its two parts carry the two values of the subscript. Each line multiplies the part with one value by the gradient and pairs it with the part of the other value; the mass is the term that carries the value across, and it is the only such term. At $m=0$ the pair decouples into the two one-sided equations $\tilde\nabla\tilde{Ξ}^{\mathrm{sp}}_R=0$ and $\tilde\nabla^{\natural}\tilde{Ξ}^{\mathrm{sp}}_L=0$, one for each value.

The conjugation $\flat$ is the algebra's real structure, not the mass term (§*The Conjugations* of the conventions article cited above). The corpus also carries a **two-sided** form of the same physics — Kravchenko's single equation on $\mathbb{B}$, in which the mass acts by right multiplication through $\vec e_z$ and a conjugation supplies the antilinear part — but the two forms are related by a dictionary and are not the same operator (parent, §*The One-Sided and the Two-Sided Equation*). The Zitterbewegung derivation below uses the pair.

The plane-wave solutions are

$$
\tilde{Ξ}^{\mathrm{sp}}=\tilde{Ξ}^{\mathrm{sp}}_0\exp\!\Big(i\,\mathrm{Sc}\big(\tilde P\tilde{R}_\varphi^{\natural}\big)/\hbar\Big),
\qquad
\frac{\tilde P}{\hbar}=e_t\frac{iE}{\hbar c}+\vec k,
\qquad
\tilde R_\varphi=e_t(i c r'_t)+\vec r,
$$

with $\tilde{Ξ}^{\mathrm{sp}}_0$ a constant element and $\vec r=r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z$. The single mass-shell condition is

$$
\tilde P\tilde P^{\natural}=-m^2c^2.
$$

The two roots of that condition — positive and negative frequency — are the two branches

$$
\tilde{Ξ}^{\mathrm{sp}(+)}=\tilde{Ξ}^{\mathrm{sp}(+)}_0\exp\!\Big(-i\frac{Er'_t-\vec p\cdot\vec r}{\hbar}\Big),
\qquad
\tilde{Ξ}^{\mathrm{sp}(-)}=\tilde{Ξ}^{\mathrm{sp}(-)}_0\exp\!\Big(+i\frac{Er'_t-\vec p\cdot\vec r}{\hbar}\Big),
$$

constructed in the parent, with $E = +\sqrt{\vec p^2c^2 + m^2c^4}$ and constant elements $\tilde{Ξ}^{\mathrm{sp}(\pm)}_0$. The normalisation and the non-relativistic reduction belong to the parent; the present article uses only the branches and the mass shell.

One fact about the field will be needed throughout, and it is the sector action of the real structure: $\flat$ acts as $-1$ on the $\mathbb{M}_+$ part of the field and $+1$ on its $\mathbb{M}_-$ part, so its fixed space is $\mathbb{M}_-$ (§*The Conjugations*). The physical Majorana mass is a different object: it is built on charge conjugation, not on the algebra's $\flat$ (see *Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form*). What the diagonal action of the real structure, the mass coupling of the two values, and the rest-energy phase do to the sectors is the subject of the section *The Complexification and the Rest-Energy Phase*.

## Recomputing the Oscillation

The generators of the parent are the map $\beta$ of *The Standard Picture* and three spatial maps, written in cells as $iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}$. With the action, the composition and the unit of *Operator Family Conventions*, and with the structure constants of the units, they give

$$
\left(iR_{\vec e_x}^{\mathrm{axf}}\right)^2 = \mathrm{id}, \qquad
\left(iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\right)^2 = -\mathrm{id}, \qquad
\{iR_{\vec e_x}^{\mathrm{axf}},\, iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}\} = 0,
$$

so the four maps carry the sign pattern of the frame, $\varepsilon=(1,-1,-1,-1)$. The product of the time map with a spatial map is the map $\alpha_k$ of the Hamiltonian. It is one line, the two factors $i$ and the order of the two spatial units,

$$
\beta\, iL_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}
= i^2\,L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_y\vec e_x}^{\mathrm{axf}}
= -L_{\vec e_k}^{\mathrm{axf}}R_{-\vec e_z}^{\mathrm{axf}}
= L_{\vec e_k}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}},
$$

because $\vec e_y\vec e_x=-\vec e_z$ and a cell is linear in its second multiplier; the last cell is the map $\alpha_k$ of *The Standard Picture*. The relations $\{\alpha_j,\alpha_k\} = 2\delta_{jk}\,\mathrm{id}$, $\{\alpha_k,\beta\} = 0$ and $H^2 = E^2\,\mathrm{id}$ all follow, and each was checked numerically.

The identity boxed in *The Standard Picture* is exact, and $cp_k/H$ in it denotes the operator $cp_kH^{-1} = cp_kH/E^2$ — not a multiple of the identity, since $H$ is an operator and not a scalar. The three equivalent forms of that section rest on $\{\alpha_k-cp_k/H,\,H\}=0$, which the relations above give.

The identity was checked by direct computation on a case chosen here rather than on the rest case that motivated it: momentum $\vec p/mc = (0.3,\,0.2,\,-0.1)$, so $|\vec p| = 0.374\,mc$ and $E = 1.0677\,mc^2$, at the three times $r'_t = 0.017, 0.05, 0.23$ in units of $\hbar/(mc^2)$. The left side $\exp(iHr'_t/\hbar)\alpha_k \exp(-iHr'_t/\hbar)$ and both equivalent forms on the right agreed to machine precision, the largest coefficient of the difference below $10^{-15}$ over all three components and all times. The integrated position formula was checked the same way, against a direct integration of $c\alpha_k(r'_t)$ from the eigen-decomposition of $H$; the largest coefficient of the difference was below $5\times10^{-16}$. The rest case is then a consequence, $E = mc^2$, not an input.

The frequency is $2E/\hbar$ on general grounds and $2mc^2/\hbar$ at rest. The numbers for the electron, $m_ec^2 = 0.510998950$ MeV and $\hbar = 6.582119569\times10^{-22}$ MeV s, are

$$
\boxed{\;\omega_Z^{\text{rest}} = \frac{2m_ec^2}{\hbar} = 1.55269\times10^{21}\ \text{rad s}^{-1},
\qquad f_Z = \frac{\omega_Z}{2\pi} = 2.47118\times10^{20}\ \text{Hz}\;},
$$

which is the standard value. On a relativistic case chosen independently, with Lorentz factor $2$ so $E = 2mc^2$, the formula gives $2E/\hbar = 4m_ec^2/\hbar = 3.10538\times10^{21}\ \text{rad s}^{-1}$ — twice the rest value, as the formula requires and as the rest case alone would not reveal. The oscillation amplitude is $\hbar/(2mc)$, which for the electron is $193.1$ fm, half the reduced Compton wavelength $386.2$ fm. Both the frequency and the amplitude are the standard ones; the biquaternion notation reproduces them without alteration.

It should be said clearly that this derivation uses the map $\beta$ of *The Standard Picture*, which multiplies the field on the right, and that no left multiplication by an element of $\mathbb{B}$ does the same. That will matter in the test that follows.

## The Complexification and the Rest-Energy Phase

There is a genuinely algebraic statement available, and it is the strongest positive result of the article. It has two parts.

**The real structure is diagonal on the sectors.** The conjugation $\flat$ acts as $-1$ on the $\mathbb{M}_+$ part of the field and $+1$ on its $\mathbb{M}_-$ part: it **preserves** each sector and marks it with a sign. This is a property of the algebra's real structure, not of the mass term; the parent's mass is the linear term that couples the two values, and, being a real scalar, it leaves each element's sector membership untouched. The operation that exchanges the two sectors is multiplication by the central $i$ (§*The Conjugations*).

**The rest-energy phase rotates the sectors into one another.** Factoring out the rest energy writes the free phase as

$$
\exp(-imc^2r'_t/\hbar) = \cos\!\Big(\frac{mc^2r'_t}{\hbar}\Big)e_t \;-\; \sin\!\Big(\frac{mc^2r'_t}{\hbar}\Big)(ie_t),
$$

and the two terms lie in different sectors: $e_t \in \mathbb{M}_+$ and $ie_t \in \mathbb{M}_-$ (an imaginary scalar is anti-Hermitian). The rest-energy phase is therefore a **rotation between the sectors**, at angular frequency $mc^2/\hbar$: it takes the $\mathbb{M}_+$ direction $e_t$ toward the $\mathbb{M}_-$ direction $ie_t$ and back. This is the sense in which the complexification rotates one sector into the other; the rotation is the central phase, whose frequency the mass fixes through the mass shell.

The Zitterbewegung frequency is exactly twice this rate. That is not a coincidence of arithmetic but an algebraic relation: the oscillating factor of the velocity identity is $\exp(2iHr'_t/\hbar)$, the square of the free-evolution phase $\exp(iHr'_t/\hbar)$,

$$
\exp(2iHr'_t/\hbar)=\big(\exp(iHr'_t/\hbar)\big)^2.
$$

The rest-frame eigenvalues of the free-evolution phase are $\exp(\pm imc^2r'_t/\hbar)$, one of which is the sector rotation above; the eigenvalues of the oscillating factor at general momentum are $\exp(\pm 2iEr'_t/\hbar)$, the sign set by the energy branch, so only the magnitude of the frequency is physical. So the trembling is not the sector rotation itself; it is the second harmonic of it. The factor of two is the statement that the beat of two branches of opposite frequency is twice the frequency of either branch, and it is the same factor by which the rest-energy phase and the Zitterbewegung frequency differ.

Two consequences deserve emphasis. First, since the rest-energy phase rotates the sectors and its rate is the mass, the scale of the trembling — the mass gap $2mc^2$ — is set by the same quantity that sets the sector rotation. That is the real content of the suggestion that the trembling and the complexification are related. Second, a relation of scale is not a relation of identity: the trembling is a beat of two energy branches, the sector rotation is a rotation in the algebra, and the following section shows these are different decompositions.

## Does the Sector Split Do Real Work?

The claim to test is: *the positive- and negative-energy parts of the field are its $\mathbb{M}_-$ and $\mathbb{M}_+$ parts.* The test fails, and the reason is structural rather than numerical.

**They are splits of different objects.** The energy sign separates two terms of a solution by their dependence on $r'_t$: a term of positive frequency carries the factor $\exp(-iEr'_t/\hbar)$ and one of negative frequency the factor $\exp(+iEr'_t/\hbar)$, and $E$ moves with the momentum. It is a split of the solutions of the pair. The sector split separates the value of one element at one point, by Hermitian conjugation; it is pointwise and knows nothing of $r'_t$ or of $\vec p$. A split of a family of functions and a split of the values the functions take are different objects, and no dictionary is stated that would identify them.

**The energy sign is fixed by a multiplication on the right, the sector by an involution of the value.** The Hamiltonian contains the map $\beta$, which multiplies on the right by $\vec e_x$, and its kinetic terms multiply on the right by $\vec e_z$. No element of the algebra acts as $\beta$ by left multiplication, and two units already show it. If some $c$ gave $c\tilde Q=i\tilde Q\vec e_x$ for every $\tilde Q$, the value at $\tilde Q=e_t$ would force $c=i\vec e_x$; at $\tilde Q=\vec e_z$ that $c$ gives $c\vec e_z=i\vec e_x\vec e_z=-i\vec e_y$, while $\beta$ gives $i\vec e_z\vec e_x=+i\vec e_y$, and the two differ. A left multiplier that agrees with $\beta$ on one element fails on another. So the energy sign is decided by a map built from right multiplications, and the sector by the conjugation of the value, which is not a map at all. $\beta$ is a map on the algebra and not an element of it, so it lies in neither sector; the sectors are properties of elements.

**A momentum argument reinforces this.** The sector split is momentum-independent: whether an element is Hermitian is a property of the element, not of any wave it carries. The energy sign is momentum-dependent through the $\vec p$ of the kinetic term. A momentum-independent split cannot be a momentum-dependent one except at $\vec p = 0$, and even there the two rest branches land in the same sector, as the next paragraph shows.

**The natural dictionary the corpus supplies points the other way.** The parent's state construction reads an amplitude as the pure state $\tfrac12\big(e_t + i\vec u\big) \in \mathbb{M}_+$, with $\vec u$ the direction the amplitude carries; the direction comes from the amplitude and not from the energy sign. Each of the two rest branches of the parent gives such an element, and neither gives an element of $\mathbb{M}_-$. The sector $\mathbb{M}_-$ is where the *current* lives, $\tilde J = ic\,j_0e_t + \vec j \in \mathbb{M}_-$, not where the negative-frequency branch lives. So on the dictionary actually available, the sector split tracks the state–current distinction, not the energy sign, and both energy signs land in the same sector.

The honest conclusion, then, is that the $\mathbb{M}_\pm$ split **renames the Hermitian decomposition of the algebra and not the $\pm$-energy decomposition of the field**. It is not obviously "doing work": the two splittings share the mass scale, but the interference that produces the trembling is between energy branches, and the energy branches are not the sectors. The natural candidate for a splitting that does carry the interference is the value subscript. The pair carries it: the derivative multiplies on the left and keeps it, and the mass is the term that carries it across, so at $m=0$ each equation stands alone with one value, and in the massless limit the value is locked to the helicity. But each of the two equations has solutions of both frequency signs, since the massless dispersion relation admits both, so the value does not coincide with the energy sign either: it is a splitting of the field by the equation it obeys, not a splitting of the algebra into $\mathbb{M}_\pm$. What is settled is that the $\pm$-energy split is neither the $\mathbb{M}_\pm$ split nor the split by value, for the reasons above.

## What Survives

The following table separates the claims.

| Claim | Status |
|---|---|
| The trembling is an interference of $\pm$-frequency branches, frequency $2E/\hbar$ | Established; the standard result, recomputed here |
| Rest-frame frequency $2mc^2/\hbar$, amplitude $\hbar/(2mc)$ | Established; checked numerically above |
| The real structure $\flat$ acts with opposite signs on $\mathbb{M}_\pm$ | Established; it is the sector action of the conjugation |
| The rest-energy phase rotates the sectors at $mc^2/\hbar$ | Established; with $\theta=mc^2r'_t/\hbar$, $\exp(-i\theta) = \cos\theta\,e_t - \sin\theta\,(ie_t)$ |
| The Zitterbewegung phase is the square of the free-evolution phase | Established; hence the frequency is doubled |
| $\pm$-energy parts **are** the $\mathbb{M}_\mp$ sectors | False as an identity; the energy sign is fixed by a map that multiplies on the right, the sector by a conjugation of the value |
| The $\mathbb{M}_\pm$ split does work beyond relabelling the Hermitian decomposition | Not established; the interference is between energy branches, which are not the sectors |

What survives is a relation of *scale and phase*, not of identity. The mass sets both the sector-rotation rate and the gap whose interference is the trembling; the trembling frequency is twice the sector-rotation frequency because the trembling phase is the square of the evolution phase. This makes the Zitterbewegung a place where the mass term and the two sectors are simultaneously visible, and it is a legitimate point of contact between the Dirac solutions and the sector decomposition. It does not make the trembling the observable face of the complexification in the strong sense proposed.

## Zitterbewegung and the Electron

The Zitterbewegung is usually introduced as a property of the electron, and a [companion article on the electron in biquaternionic form](the-electron-in-biquaternionic-form.html) has since been written in this group. Nothing in the present article depends on it. The two agree on the result: the electron article records the same frequencies and amplitudes, reports that the identification of the energy branches with the sectors fails, and keeps the relation of scale and phase. Its electron gives the numbers $1.55269\times10^{21}\ \text{rad s}^{-1}$ and $193.1$ fm, which are the ones computed above, and its rest energy is the scale of both the sector rotation and the trembling.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The generators carry no frame label: $\gamma_\mu$ is one set of matrices, $\gamma_0^2=I_4$ and $\gamma_k^2=-I_4$. The frame belongs to the coordinate, not to the array.

The gammas are a frame of the cell algebra $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra. They are recorded here for comparison with the standard Dirac notation; the derivation above uses only the cells $\beta$ and $\alpha_k$.

Here $L_a$ and $R_b$ are the left and right multiplications, $L_a\tilde{Ξ}^{\mathrm{sp}}=a\tilde{Ξ}^{\mathrm{sp}}$ and $R_b\tilde{Ξ}^{\mathrm{sp}}=\tilde{Ξ}^{\mathrm{sp}} b$, and $c(M)$ is the coefficient matrix of $M$ in the basis of the sixteen products.

$$
\begin{aligned}
\gamma_0 &= iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}}, &\gamma_1 &= iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\\[2pt]
\gamma_2 &= iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}, &\gamma_3 &= iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\\[2pt]
\gamma_5 &= -iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}.
\end{aligned}
$$

The same in the axis-free display:

$$
\begin{aligned}
\gamma_0 &= iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}}, &\gamma_1 &= iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\\[2pt]
\gamma_2 &= iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}}, &\gamma_3 &= iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\\[2pt]
\gamma_5 &= -iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}.
\end{aligned}
$$

They satisfy $\{\gamma_\mu,\gamma_\nu\}=2\varepsilon_\mu\delta_{\mu\nu}L_{e_t}^{\mathrm{pau}}R_{e_t}^{\mathrm{pau}}$ with $\varepsilon=(1,-1,-1,-1)$, the product $\gamma_5=i\gamma_0\gamma_1\gamma_2\gamma_3$ squares to the identity, and $\gamma_5$ anticommutes with all four: $\{\gamma_\mu,\gamma_5\}=0$.

A single cell $L_aR_b$ is a pure tensor; a single product is one cell up to a phase, the products form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and a general element is a sum of at most four, with $\ell(M)=\operatorname{rank}c(M)$.

$\gamma_5$ is the reference-frame cell of the chirality operator $\Gamma$; the central grading $\xi$ — the difference of the two central idempotents of the complexified algebra, so $\chi^2=e_t$ — is a different object, represented by $\gamma_5$ on the Dirac module.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{e_\mu}^{\mathrm{axf}}=C_{\Pi}L_{e_\mu}^{\mathrm{pau}}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

The Zitterbewegung was derived in the biquaternion notation of the series. The Heisenberg velocity satisfies the exact identity $\alpha_k(r'_t) = cp_k/H + \exp(iHr'_t/\hbar)(\alpha_k(0)-cp_k/H)\exp(-iHr'_t/\hbar)$, checked at momentum $|\vec p| = 0.374\,mc$ and three times, to machine precision (the largest coefficient of the difference below $10^{-15}$); the integrated position formula was checked against a direct integration on the same case, with the largest coefficient of the difference below $5\times10^{-16}$. The oscillating term has frequency $2E/\hbar$, equal to $2mc^2/\hbar$ at rest, and the electron value $1.55269\times10^{21}\ \text{rad s}^{-1}$ and amplitude $\hbar/(2mc) = 193.1$ fm were confirmed.

The genuinely algebraic content is that the mass is the linear coupling between the two values of the subscript, that the real structure $\flat$ acts with opposite signs on the two sectors, and that the rest-energy phase $\exp(-imc^2r'_t/\hbar) = \cos(mc^2r'_t/\hbar)e_t - \sin(mc^2r'_t/\hbar)(ie_t)$ rotates the two sectors into one another at $mc^2/\hbar$. The Zitterbewegung phase is the square of this evolution phase, so its frequency is exactly twice the sector-rotation frequency.

The structural claim that motivated the article fails. The positive- and negative-energy parts of the field are **not** its $\mathbb{M}_-$ and $\mathbb{M}_+$ parts. The energy sign is the sign of the eigenvalue of a Hamiltonian that multiplies the field on the right, and no element of the algebra does that by left multiplication, while the sectors are fixed by the conjugation of the value; the two are splits of different objects, a family of solutions and the values it takes; and on the dictionary the series supplies, both energy branches correspond to $\mathbb{M}_+$ elements while the current lives in $\mathbb{M}_-$. The relation between the trembling and the complexification is therefore one of phase and scale — the trembling is the second harmonic of the sector rotation — and not the identity the strong form of the claim requires.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | The biquaternion algebra, *Algebra and Element Conventions* |
| $e_t, \vec e_x, \vec e_y, \vec e_z$ | Its four units, the coefficient basis |
| $i$ | The central scalar imaginary |
| $\mathbb{M}_-$, $\mathbb{M}_+$ | The anti-Hermitian (material) and Hermitian (informational) sectors |
| $\tilde{Ξ}^{\mathrm{sp}}$, $\tilde{Ξ}^{\mathrm{sp}}_L$, $\tilde{Ξ}^{\mathrm{sp}}_R$ | The field, one element of $\mathbb{B}$, and its two parts, one per value of the subscript |
| $\tilde{Ξ}^{\mathrm{sp}(+)}, \tilde{Ξ}^{\mathrm{sp}(-)}$ | The two frequency branches; $\tilde{Ξ}^{\mathrm{sp}(\pm)}_0$ their constant elements |
| $\tilde R_\varphi$ | The four-position biquaternion of the parent |
| $\tilde P/\hbar$ | The wave biquaternion of the parent, $\vec k=\vec p/\hbar$ |
| $\tilde P\tilde P^{\natural} = -m^2c^2$ | Biquaternionic mass-shell condition |
| $\flat$ | The anti-Hermitian conjugation (the algebra's real structure, not the mass term), *Algebra and Element Conventions* |
| $\tilde\nabla$ | The biquaternionic gradient (Dirac operator), *Operator and Calculus Conventions* |
| $L_{a}R_{b}$ | A two-sided cell; its action and its composition are *Operator and Calculus Conventions* and *Operator Family Conventions* |
| $\mathrm{id}$ | The identity map |
| $\beta:\tilde Q\mapsto i\tilde Q\vec e_x$ | The time map, one right multiplication |
| $\alpha_k:\tilde Q\mapsto\vec e_k\tilde Q\vec e_z$ | The three spatial maps |
| $H = c\sum_k p_k\,\alpha_k + \beta mc^2$ | Hamiltonian, $H^2 = E^2\,\mathrm{id}$ |
| $A_k = \alpha_k(0) - cp_k/H$ | Anticommuting part of the velocity, $\{A_k,H\}=0$ |
| $\omega_Z = 2E/\hbar$ | Zitterbewegung angular frequency |
| $\hbar/(2mc)$ | Zitterbewegung amplitude (order) |
| $c(M)$, $\ell(M)$ | Coefficient matrix of an element in the sixteen products, and its rank (length) |

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
