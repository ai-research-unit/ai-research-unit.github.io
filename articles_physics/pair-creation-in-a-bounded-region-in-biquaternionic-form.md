# __Pair Creation in a Bounded Region in Biquaternionic Form__

## Introduction

The companion article *The Klein Paradox in Biquaternionic Form* treats the electrostatic step, and it states the finding in three parts: the potential is central, it shifts the mass shell, and the shifted state sits on the other root, so that the pair the step creates leaves for infinity. Its first open question records what the step cannot show. This article supplies one half of that answer by changing the potential and nothing else. The region of strong potential has a **finite width**, the created charge cannot escape, and the same central shift is read on a **bound level** rather than on a scattering state.

Three statements organise the article.

1. **The threshold is a level crossing, and it is exact.** As the well deepens, the lowest level descends, and at a definite depth it reaches the lower edge of the gap, $E=-mc^2$. That depth is computed in closed form, it exceeds $2mc^2$ by the confinement energy of the standing wave, and it tends to $2mc^2$ as the width grows. The step and the well are therefore one formula read at two ends, and $2mc^2$ is the floor that both approach and neither attains.

2. **The criterion is which side of the mass shell the confining term enters.** The electrostatic well shifts the energy, and the temporal coefficient of the wave number, the one whose sign selects the branch, is dragged with it. The Dirac oscillator's non-minimal substitution shifts the spatial part of the gradient instead, and in the product of the two shifted gradients the shift appears as a positive addition. The oscillator's spectrum is gapped for every frequency, no level ever enters the gap, and no pair is ever produced. A static confinement that acts on the spatial side cannot create pairs, however strong it is, which is why a magnetic field creates none; one that acts on the temporal side can, as soon as its strength passes the threshold, which is why an electric field does. The strength of a spatial confinement changes only the spacing of the levels.

3. **The vacuum becomes charged.** In the step the pair is emitted as a current and nothing holds the imbalance. In a bounded region the imbalance sits in a single level: once the level has crossed into the lower continuum it is degenerate with the filled sea, an electron occupies it at no cost, and the hole leaves as a positron. The region is left with a charge that does not decay. The one-particle equation records the crossing and says nothing about the occupation; the counting is the standard overcritical bookkeeping, and it is imported.

The article derives the matching, the threshold and the two tables of numbers. It does not derive the second-quantized statements: the pair number, the Bogoliubov mixing and the vacuum persistence amplitude are those of *Scalar Pair Creation in Biquaternionic Form*, the operator content of the sea is that of *The Dirac Sea, Hole Theory and Antimatter in Biquaternionic Form*, and the mode count of a cavity is that of *The Vacuum State and the Casimir Effect in Biquaternionic Form*. What the framework supplies is the location of the threshold on the mass shell, and the criterion that separates a confining model which can create pairs from one which cannot.

The conventions are those of the companion articles. The algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ with units $e_t=1,\vec e_x,\vec e_y,\vec e_z$, $\vec e_\eta^2=-e_t$ and central scalar imaginary $i$; $\mathbb{B}_{\Phi}$ is the anti-Hermitian subspace, the material sector, on which $Q_t=i r'_t$ and $\partial/\partial R_t=-i\,\partial/\partial r'_t$; the gradient is $\tilde\nabla=e_t\,\partial/\partial R_t+\sum_\eta\vec e_\eta\,\partial/\partial R_\eta$; the Dirac equation is the chiral pair $\tilde\nabla_\Phi\tilde{Ξ}_{\mathrm{sp},R}=k_m\tilde{Ξ}_{\mathrm{sp},L}$, $(\tilde\nabla^{\natural})_\Phi\tilde{Ξ}_{\mathrm{sp},L}=k_m\tilde{Ξ}_{\mathrm{sp},R}$ with $k_m=mc/\hbar$; and the minimal coupling replaces $\tilde\nabla_\Phi$ by $D=\tilde\nabla_\Phi+\frac{i\,ϙ}{\hbar}\tilde{A}_{\Phi}$. No array and no column is written below.

## The Well and the Gap

### The configuration

The potential energy is

$$
ϙ\xi(r_x)=-V_0\quad\text{for }\lvert r_x\rvert<\frac{L}{2},
\qquad
ϙ\xi(r_x)=0\quad\text{otherwise},
\qquad
V_0>0,
$$

a one-dimensional well of depth $V_0$ and width $L$, constant on each of its three regions and discontinuous at the two walls. The particle moves along $r_x$ and is taken to be in a spin state along the direction of motion, so the reduction of the companion article applies unchanged and the same two-component pair results:

$$
i\,\hbar\,c\,\frac{\partial\tilde{Ξ}_{\mathrm{sp},1}}{\partial r_x}=\bigl(E-V(r_x)+mc^{2}\bigr)\tilde{Ξ}_{\mathrm{sp},2},
\qquad
i\,\hbar\,c\,\frac{\partial\tilde{Ξ}_{\mathrm{sp},2}}{\partial r_x}=\bigl(E-V(r_x)-mc^{2}\bigr)\tilde{Ξ}_{\mathrm{sp},1},
$$

with $V(r_x)=ϙ\xi(r_x)$ and $E$ the total energy. The pair is the reduced equation of the parent, and the biquaternion field is recovered from it by the standing dictionary of *The Dirac Equation in Biquaternionic Form*. Nothing below uses a second reduction.

**The three regions and the two spectra.** Outside the well the equation is the free one, and a solution with $\lvert E\rvert<mc^{2}$ is evanescent: it is a bound level, and its energy lies in the **gap**, the open interval $(-mc^{2},mc^{2})$ in which no free state propagates. Above $mc^{2}$ lies the upper continuum, the scattering states of the electron; below $-mc^{2}$ lies the lower continuum, the branch that the companion article calls the antiparticle root. Inside the well, where the potential energy is $-V_0$, the local frequency is measured from $-V_0$ and a state there propagates whenever $\lvert E+V_0\rvert>mc^{2}$.

**One level to a state.** The problem is one-dimensional and the reduction has already spent the spin state, so each level is counted once. In three dimensions every level carries the spin degeneracy, which doubles the charge count and leaves the threshold untouched; §*The Charged Vacuum* returns to it.

### The two matching conditions

The well is symmetric, so every solution is even or odd. In the well the wave number is

$$
k_{\Phi,\mathrm{w}}=\frac{\sqrt{(E+V_0)^{2}-m^{2}c^{4}}}{\hbar c},
\qquad
\hbar c=\hbar\,c,
$$

the momentum wave number of the parent read at the shifted frequency, and outside the well the solution decays with

$$
k_{\Phi,\mathrm{ev}}=\frac{\sqrt{m^{2}c^{4}-E^{2}}}{\hbar c},
$$

which is real in the gap and is the inverse of the decay length. Both are inverse lengths: the first is a wave number and the second a decay constant, and it is the second that vanishes at the threshold.

Take the even solution, $\tilde{Ξ}_{\mathrm{sp},1}=\cos(k_{\Phi,\mathrm{w}}r_x)$ inside and $\tilde{Ξ}_{\mathrm{sp},1}=\exp(-k_{\Phi,\mathrm{ev}} r_x)$ outside. The second line of the pair fixes the other component in each region, and continuity of the ratio $\tilde{Ξ}_{\mathrm{sp},1}/\tilde{Ξ}_{\mathrm{sp},2}$ at the wall $r_x=a=L/2$ gives

$$
\frac{k_{\Phi,\mathrm{ev}}}{E+mc^{2}}=\frac{k_{\Phi,\mathrm{w}}\tan\bigl(k_{\Phi,\mathrm{w}}a\bigr)}{E+V_0+mc^{2}},
$$

and the same statement for the odd solution, $\tilde{Ξ}_{\mathrm{sp},1}=\sin(k_{\Phi,\mathrm{w}}r_x)$ inside, gives

$$
\frac{k_{\Phi,\mathrm{ev}}}{E+mc^{2}}=-\frac{k_{\Phi,\mathrm{w}}\cot\bigl(k_{\Phi,\mathrm{w}}a\bigr)}{E+V_0+mc^{2}}.
$$

The two lines are the whole of the problem. Each is the continuity of one ratio at one wall, the same statement the companion article writes for the transmitted amplitude at a step, with the discontinuity replaced by a wall and the exponential tail kept. No approximation enters: the potential is constant on each region, so the solutions are exact there, and the conditions are transcendental only because the wave number inside depends on the energy that is being solved for.

## The Threshold

### The condition at the lower edge

Let the energy approach the lower edge of the gap, $E\to-mc^{2}$ from above. The decay constant vanishes there, $k_{\Phi,\mathrm{ev}}\to0$, but the factor $E+mc^{2}$ vanishes faster, since

$$
\frac{k_{\Phi,\mathrm{ev}}}{E+mc^{2}}=\frac{1}{\hbar c}\sqrt{\frac{mc^{2}-E}{mc^{2}+E}}\;\longrightarrow\;\frac{1}{\hbar c}\sqrt{\frac{2mc^{2}}{\varepsilon}},
\qquad
\varepsilon=E+mc^{2},
$$

which diverges as $\varepsilon^{-1/2}$. The left side of each matching condition therefore diverges while the right side stays finite, so the tangent in the even condition must diverge and the cotangent in the odd condition must vanish:

$$
\cos\bigl(k_{\Phi,\mathrm{w}}a\bigr)=0\quad\text{(even)},
\qquad
\sin\bigl(k_{\Phi,\mathrm{w}}a\bigr)=0\quad\text{(odd)}.
$$

Both say the same thing: the wave number in the well is an integer multiple of $\pi/(2a)$,

$$
k_{\Phi,\mathrm{w}}a=n_{\mathrm{w}}\frac{\pi}{2},
\qquad
n_{\mathrm{w}}=1,2,3,\dots,
$$

with $n_{\mathrm{w}}$ counting half-wavelengths across the well. Odd $n_{\mathrm{w}}$ is the even solution, and the nodeless state of the well is $n_{\mathrm{w}}=1$. That is the kinematic content of the dive: at the threshold the state inside the well has fitted a whole number of half-wavelengths, and the state outside has stopped decaying.

### The depth

At $E=-mc^{2}$ the wave number inside is fixed by the depth alone,

$$
k_{\Phi,\mathrm{w}}^{2}=\frac{(V_0-mc^{2})^{2}-m^{2}c^{4}}{(\hbar c)^{2}},
\qquad
k_m^{2}=\frac{m^{2}c^{2}}{\hbar^{2}},
$$

so that $k_{\Phi,\mathrm{w}}a=n_{\mathrm{w}}\pi/2$ with $a=L/2$ becomes $(V_0/mc^{2}-1)^{2}=1+(n_{\mathrm{w}}\pi/(k_mL))^{2}$, and the depth follows in closed form:

$$
\boxed{\;V_0^{\mathrm{cr}}=mc^{2}\left[1+\sqrt{1+\left(\frac{n_{\mathrm{w}}\pi}{k_mL}\right)^{2}}\;\right]\;}
$$

**What the formula says.** Three things. First, the threshold depends on $n_{\mathrm{w}}$ and $L$ only through the ratio $n_{\mathrm{w}}/(k_mL)$, so the $n_{\mathrm{w}}$-th level of a well of width $L$ dives at the depth of the first level of a well of width $L/n_{\mathrm{w}}$; the tables below confirm the identity, $2.181010\,mc^{2}$ both ways. Second, the threshold lies above $2mc^{2}$ for every finite width, and the excess is the confinement energy of the standing wave that dives. Expanding the root for large $k_mL$,

$$
V_0^{\mathrm{cr}}-2mc^{2}=mc^{2}\left[\sqrt{1+\left(\frac{n_{\mathrm{w}}\pi}{k_mL}\right)^{2}}-1\right]\simeq\frac{n_{\mathrm{w}}^{2}\pi^{2}\hbar^{2}}{2mL^{2}},
$$

which is the kinetic energy of a particle confined to a region of width $L$. A bounded region therefore needs a deeper potential than a step, and the extra depth is exactly the price of confining the charge to the region; as the region narrows the price rises without bound, so a well much narrower than a Compton wavelength dives only many rest energies deep. Third, as $L\to\infty$ at fixed $n_{\mathrm{w}}$ the threshold tends to $2mc^{2}$ from above, and $2mc^{2}$ is a floor that no finite width attains. The same number is the step's critical height, $V_0>E+mc^{2}$ at $E\to mc^{2}$, and the agreement is in the number only: $2mc^{2}$ is the least potential that brings an edge of one branch onto an edge of the other, and the well reaches it through a bound level at the lower edge of the gap while the step reaches it through a scattering state at the upper edge. What the two faces share is the formula and the floor; what separates them is the width.

### The numbers

The formula was checked against the matching conditions solved numerically, with the wave number inside computed from the energy at each step and the ratio conditions bisected to machine precision. The first table gives the threshold depth in units of $mc^{2}$.

| $k_mL$ | $n_{\mathrm{w}}=1$ | $n_{\mathrm{w}}=2$ | $n_{\mathrm{w}}=3$ | $V_0^{\mathrm{cr}}(n_{\mathrm{w}}=1)/mc^{2}-2$ | $\pi^{2}/(2(k_mL)^{2})$ |
|---|---|---|---|---|---|
| $5$ | $2.181010$ | $2.605969$ | $3.133789$ | $0.181010$ | $0.197392$ |
| $10$ | $2.048187$ | $2.181010$ | $2.374141$ | $0.048187$ | $0.049348$ |
| $20$ | $2.012262$ | $2.048187$ | $2.105471$ | $0.012262$ | $0.012337$ |
| $40$ | $2.003080$ | $2.012262$ | $2.027383$ | $0.003080$ | $0.003084$ |
| $\infty$ | $2$ | $2$ | $2$ | $0$ | $0$ |

The excess column approaches the leading term of the expansion from below, and the agreement improves as the width grows, as the expansion requires. The degeneracy $V_0^{\mathrm{cr}}(n_{\mathrm{w}}=2,k_mL=10)=V_0^{\mathrm{cr}}(n_{\mathrm{w}}=1,k_mL=5)$ holds to all printed digits, which is the scaling remark of the previous subsection.

The second table follows the lowest even level of a well of width $k_mL=10$ as the depth approaches its threshold, $V_0^{\mathrm{cr}}=2.048187\,mc^{2}$.

| $(V_0^{\mathrm{cr}}-V_0)/mc^{2}$ | $E/mc^{2}$ | $(E+mc^{2})/mc^{2}$ |
|---|---|---|
| $0.1$ | $-0.902023$ | $9.798\times10^{-2}$ |
| $0.03$ | $-0.971095$ | $2.891\times10^{-2}$ |
| $0.01$ | $-0.990625$ | $9.375\times10^{-3}$ |
| $0.003$ | $-0.997334$ | $2.666\times10^{-3}$ |
| $0.001$ | $-0.999185$ | $8.149\times10^{-4}$ |
| $0.0003$ | $-0.999793$ | $2.067\times10^{-4}$ |

The level descends monotonically to the edge and does not jump: at $V_0^{\mathrm{cr}}$ the even condition vanishes at $E=-mc^{2}$ to $3\times10^{-10}$, and the three conditions of the threshold hold together — $k_{\Phi,\mathrm{ev}}=0$, $\cos(k_{\Phi,\mathrm{w}}a)=0$ to $-5\times10^{-15}$, and $V_0$ at its formula value. Above the threshold no even level remains in the gap: at $V_0=V_0^{\mathrm{cr}}+10^{-3}mc^{2}$ the lowest even level in the gap is $E=-0.697067\,mc^{2}$, which is the next state up, and the tracked level has left the gap for the lower continuum. The odd level behaves identically at $n_{\mathrm{w}}=2$, reaching $E=-0.999489\,mc^{2}$ at $V_0^{\mathrm{cr}}-10^{-3}mc^{2}$ with $V_0^{\mathrm{cr}}=2.181010\,mc^{2}$.

**What the crossing means.** Below the threshold the level is a normalizable state of the well, and its energy is a property of the well. At the threshold it is degenerate with the lower continuum; above it there is no normalizable state of that parity in the gap at all. The one-particle equation has not failed: it still has solutions. What has failed is that any of them is normalisable, and that the one which was normalisable is the ground state of one electron. The level has dissolved into the lower continuum, and the failure is the same one the companion article finds at the step. The difference is bookkeeping: at the step the pair leaves as a current and the account is closed at infinity, and here the positron leaves while the electron is held, so the account is closed by the charge of the region.

### How many levels have dived

**The threshold inverted.** The preceding subsection fixes the width and finds the depth. Put the fixed quantity on the other side instead: fix the depth and ask how many levels have crossed. The $n_{\mathrm{w}}$-th level dives when $V_0=V_0^{\mathrm{cr}}(n_{\mathrm{w}},L)$, and $V_0^{\mathrm{cr}}$ increases with $n_{\mathrm{w}}$, so the levels dive one after another as the depth grows, in the order of $n_{\mathrm{w}}$. Inverting the boxed formula, the $n_{\mathrm{w}}$-th level has crossed by depth $V_0$ whenever

$$
\frac{n_{\mathrm{w}}\pi}{k_mL}\le\sqrt{\left(\frac{V_0}{mc^{2}}-1\right)^{2}-1},
$$

so the number of levels that have left the gap is

$$
\boxed{\;N(V_0,L)=\left\lfloor\frac{k_mL}{\pi}\sqrt{\left(\frac{V_0}{mc^{2}}-1\right)^{2}-1}\;\right\rfloor\;}
$$

for $V_0>2mc^{2}$, and $N=0$ otherwise. The floor is a count of half-wavelengths, and it is the same half-wavelength count as in the threshold formula, read as a counting measure rather than as an equation.

**The width that allows a dive.** The count is zero until the root reaches $\pi/(k_mL)$, so at a fixed depth the first dive needs a width of at least

$$
L_{\min}=\frac{\pi\hbar c}{\sqrt{V_0^{2}-2V_0\,mc^{2}}},
$$

and the $n_{\mathrm{w}}$-th dive comes at $n_{\mathrm{w}}L_{\min}$ exactly. The dive widths are therefore equally spaced. Since the root is bounded by $V_0/mc^{2}-1$, nothing dives at any width unless $V_0>2mc^{2}$: a well shallower than twice the rest energy is Klein-stable however wide it is. The floor is the same $2mc^{2}$ that the step meets as a critical height, and here it appears as a depth below which no width dives.

**The count grows with the width, not with the narrowness.** This is worth stating plainly, because the opposite is often assumed. At a fixed depth the count rises as the box widens and falls to zero as it narrows. For $V_0=2.5\,mc^{2}$ the first dive needs $L_{\min}=2.810\,\hbar c/mc^{2}$, and the count runs $0,1,3,7$ at $k_mL=2.5,5,10,20$. The reason is the confinement energy, in the direction the reader may not expect: a narrow box raises the kinetic energy of the standing wave and pushes every level *up*, away from the lower edge, so a level needs room before it can sink to $-mc^{2}$. The same quantity $\hbar c/L$ that makes a small box relativistic is what keeps its vacuum intact. Smallness of $L$ changes which equation is needed; it does not by itself put a level into the lower continuum.

**The check.** The count was verified without using the closed form, by asking which level survives. If $N$ levels have crossed, the lowest level still in the gap is the $(N+1)$-th, so its wavelength inside the well must satisfy $k_{\Phi,\mathrm{w}}a$ just below $(N+1)\pi/2$. The levels were located numerically at $V_0=2.5\,mc^{2}$ and the surviving lowest one measured:

| $k_mL$ | $N$ from the formula | $k_{\Phi,\mathrm{w}}a$ of the lowest surviving level | $(N+1)\pi/2$ |
|---|---|---|---|
| $2.50$ | $0$ | $1.4913$ | $1.5708$ |
| $2.81$ | $1$ | $2.7275$ | $3.1416$ |
| $3.50$ | $1$ | $2.8615$ | $3.1416$ |
| $5.00$ | $1$ | $3.0474$ | $3.1416$ |
| $10.00$ | $3$ | $6.1800$ | $6.2832$ |
| $20.00$ | $7$ | $12.4582$ | $12.5664$ |

Each measured value lies just below the predicted multiple of $\pi/2$, as it must, since the level that crossed is the one that sat exactly on it. The formula is also confirmed at the boundary: at $V_0=2.01\,mc^{2}$ no level crosses at $k_mL=10$ and one crosses at $k_mL=30$, which is $N=0$ and $N=1$ from the count.

**What the wall's type does, and what its rigidity does not.** An infinitely deep *vector* wall would send $N\to\infty$ at every width, since the root in the count grows without bound; an infinitely deep well is overcritical at any $L$. Rigidity therefore does not protect the vacuum. What protects it is the *kind* of wall: a scalar step raises the local rest energy and shifts no frequency, so it never dives, at any depth or width. The dichotomy of §*The three confinements* holds at every depth, and the count is the quantitative form of the unstable side.

**The charge that follows.** In one dimension each crossed level contributes one unit, so the region carries $Q=-eN(V_0,L)$, and $-2eN$ in three dimensions where each level carries both spin projections. §*The Charged Vacuum* reads the same level, and the count says how many such levels a given well supports.

## Which Side of the Mass Shell

### The electrostatic shift

The mass shell of the parent is one equation, and it is worth writing in the form that separates the two sides:

$$
\tilde K_{\Phi}\tilde K_{\Phi}^{\natural}=-k_m^{2}
\qquad\Longleftrightarrow\qquad
k_{t}^{\prime\,2}=k_{\Phi}^{2}+k_m^{2},
\qquad
k_{t}^{\prime}=\frac{E}{\hbar\,c},
\qquad
k_{\Phi}=\frac{p}{\hbar},
$$

the temporal coefficient on the left and the spatial part on the right. The electrostatic potential enters as the time component of the four-potential, and on a state of energy $E$ it shifts the energy by the central scalar it carries,

$$
E\;\longmapsto\;E-ϙ\xi,
\qquad\text{hence}\qquad
k_{t}^{\prime}=\frac{E}{\hbar\,c}\;\longmapsto\;\frac{(E-ϙ\xi)}{\hbar\,c},
$$

a shift of the left side of the mass shell by a central scalar. The companion article writes the same shift as an exchange $\omega\mapsto\omega-\frac{ϙ\,\xi}{\hbar}$ of its frequency, and the two are the same statement with the energy and the frequency interchanged. A shift there moves the state along the two-rooted shell and can carry it past the point where the sign of $k_{t}^{\prime}$ is reversed; the companion article computes that reversal at the step, and this article computes it at the wall. The threshold of a bounded region is the same shift read on a bound level: the level is the value of $k_{t}^{\prime}$ at which the state fits the well and decays outside, and the shift drags that value down to $-k_m$.

### The oscillator's shift

The Dirac oscillator's substitution is a shift of the other side. Its non-minimal term replaces $\vec p$ by $\vec p-im\omega\beta\vec r$, so it acts on the spatial part of the gradient and on nothing else, and the shifted gradients are

$$
\vec\nabla_{\pm}=\vec\nabla\pm\frac{m\,\omega}{\hbar}\,\vec r .
$$

Multiplying the two shifts, as the companion article on the oscillator does, the cross terms reduce to a central commutator and a spin–orbit term, and the confining term that survives in the identity is a positive addition, $+m^{2}\omega^{2}r^{2}$:

$$
\mathcal Q_{+}\mathcal Q_{-}=\vec p^{\,2}+m^{2}\omega^{2}\vec r^{\,2}-3\,\hbar\,m\,\omega-2m\omega\sum_\eta L_{\mathrm{orb},\eta}\,i\vec e_\eta ,
\qquad
E^{2}=m^{2}c^{4}+c^{2}\,\mathcal Q_{+}\mathcal Q_{-}.
$$

The right-hand side is bounded below by zero, and its lowest eigenvalue is zero, attained on the aligned states with $n_r=0$. Hence $E^{2}\ge m^{2}c^{4}$ for every level and every frequency: the positive branch begins at $mc^{2}$, the negative branch ends at $-mc^{2}$, and the gap is empty for every value of $\omega$. The spectrum quoted by that article, $E^{2}=m^{2}c^{4}+4\,\hbar\,m\,c^{2}\,\omega\,n_r$ on the aligned branch, says the same thing in one line, and it says it for all $n_r$ at once.

**The criterion.** The two confinements differ in which side of the mass shell they act on, and that, and not their strength, decides whether the model can create pairs. A term that shifts $k_{t}^{\prime}$ moves the level along the shell and across the gap; a term that adds to $k_{\Phi}^{2}$ raises the right side and pushes every level away from the gap. The oscillator's substitution adds $+m^{2}\omega^{2}r^{2}$, which is positive whenever the oscillator frequency is, however small it is, so its confinement is Klein-stable at every frequency; the electrostatic well subtracts from $k_{t}^{\prime}$, which is indefinite in sign, so its confinement is Klein-unstable at every width once the depth passes the threshold. Neither statement is a numerical accident: both follow from where the term sits in $\tilde K_{\Phi}\tilde K_{\Phi}^{\natural}=-k_m^{2}$.

### The three confinements

Three models of confinement now have a place in the corpus, and the table sets them against one another.

| Confinement | Where the term enters | Mass shell | Level behaviour | Pairs |
|---|---|---|---|---|
| electrostatic well, depth $V_0$, width $L$ | energy, $E\mapsto E-ϙ\xi$, so the temporal coefficient | shifted | descend; cross at $V_0^{\mathrm{cr}}$ | created above the threshold |
| step in the mass (scalar confinement) | mass term, chirality-off-diagonal | local rest energy raised | transmitted wave evanescent, reflection total; no threshold crossing | none; no threshold |
| Dirac oscillator, frequency $\omega$ | spatial part, $+m^{2}\omega^{2}r^{2}$ | unshifted | $E^{2}\ge m^{2}c^{4}$ at every frequency; no level in the gap | none; no threshold |

The mass step is the bag-model mechanism of Bardeen, Chanowitz, Drell, Weinstein and Yan, which §*The converse step* of the companion article records: a scalar step shifts no frequency, so it has no Klein threshold. The oscillator is the third case, and the framework reads it as the second kind of stability. Two confinements are therefore stable and one is not, and the reading is uniform: the two stable ones act off the temporal coefficient, and the unstable one acts on it. The dichotomy is stated in the corpus for the step and the mass; this article extends it to a bounded region and to the oscillator, where the stable side is the side that is taken.

## The Charged Vacuum

**The step emits and does not keep.** In the companion article the transmitted wave is a negative-frequency state on the far side, and the current it carries runs away from the step to infinity. The negative-frequency branch is the branch of the antiparticle, so the current that leaves is a positron current, and the electron that is missing from the lower continuum is at infinity with it. The step therefore carries the charge away as a steady current, and nothing accumulates behind it.

**A bounded region keeps it in one level.** Here the imbalance sits in a single state. Once the level has crossed the threshold it is degenerate with the filled sea, so an electron can occupy it at no energy cost, and the sea is left with a hole. The hole is a positron, it appears where the level is, and in a well that sits in otherwise empty space it propagates away: that is **spontaneous positron emission**, the same process the overcritical Coulomb problem exhibits. What remains is the region with the crossed level occupied, that is one electron more than the neutral vacuum, so its field charge is $-e$ per crossed level, and $-2e$ in three dimensions where the level carries both spin projections. The escaping positron carries $+e$ and the total is unchanged. The state of least energy of the region is therefore charged, and it stays charged for as long as the depth is maintained. That is the **charged vacuum**, and its charge is a property of the occupation of one level, and not of the potential that produced it.

**The external source and the idealisation.** The well is external: it is produced by a charge distribution on the walls, and that distribution is not part of the field being solved for. It fixes the potential and it is an input, and this article never needs its value; the charge that compensates the region's is carried away by the emitted positron and not by the wall. Where the walls do enter is the idealisation. A well in otherwise empty space has a continuum on each side of the gap, and the positron has somewhere to go. A genuinely closed cavity has a discrete spectrum on both sides of the gap, so the emitted state has nothing to propagate into, and the bookkeeping then depends on the charge distribution of the walls themselves. That case is not treated here: what is computed is the level, in a well that sits in empty space.

**The Coulomb case is the same bookkeeping.** In the overcritical Coulomb problem the same account is applied to a nucleus: the dived $1s$ level is occupied in the vacuum, the positrons are emitted, and the atom is left with a charged vacuum. That problem's critical charge number, $\mathfrak{Z}\approx173$ for a realistic nuclear radius, is the three-dimensional instance of the threshold computed here, with the well replaced by the Coulomb field and the level by the $1s$ state. The companion article on the hydrogen atom records why the point-Coulomb formula stops earlier, at $E=0$ and $\mathfrak{Z}\alpha=1$, and why that stopping point is not the lower continuum.

**What the framework says and what it does not.** The algebra records the level, the gap and the crossing, and it records the current as the material-sector element $\tilde J_{\Phi}=ic\,j_0e_t+\vec j$ whose temporal component is the charge density, as in *Noether's Theorem in Biquaternionic Form*. It does not record the occupation: that the crossed level is filled in the state of least energy, and that the hole is a positron, are statements about the occupation of the roots, and the occupation is a second-quantized datum, as the companion articles on the sea and on scalar pair creation say. Nor does the algebra supply the external source, for the same reason that it does not supply the point-charge source of the Coulomb field: the potential is an input.

## What Is Standard and What Is Open

**Standard, and imported.** The two-component reduction of the Dirac equation at a constant potential; the matching of the two components at a discontinuity; the transcendental conditions and their half-wavelength limit at the bottom of the gap; the threshold depth and its $2mc^{2}$ limit; the count of crossed levels as a function of depth and width, which is elementary once the threshold is known and is a rearrangement rather than a new result; the identification of the crossed level with a charged vacuum; the critical charge number of the Coulomb problem. None of this is re-derived here, and none of it depends on the biquaternion structure beyond the kinematical conventions. The tables were computed here from the matching conditions, and the closed form agrees with them to the printed digits.

**Open in the biquaternion framework.**

- **The fermionic pair source.** The companion article's first open question is the biquaternion form of the step as a pair source, with the anomalous occupation of the two roots. The bounded case does not close it: here the source is stationary and there is no flux to compute, so the question becomes the occupation of one level, and that is not a one-particle statement either.
- **The thickness of the wall.** A wall smoothed over a Compton wavelength is the bounded analogue of Sauter's smoothed step. Whether the smoothing moves the threshold, or only turns the crossing into a resonance of finite width, is not worked out; the companion article records the same question for the step.
- **The width of a crossed level.** The one-particle operator here is Hermitian and its spectrum is real, so it has no width to give. A level embedded in the continuum must acquire one, and whether the second-quantized decay can be written as a complex shift of $k_{t}^{\prime}$ in the algebra, or only as a decay rate of an occupation, is not settled.
- **The spin count.** The factor of two in three dimensions is a spin degeneracy, and the framework's spin is the Hermitian element $\tilde S_{\Psi,\eta}$ of the informational sector. Whether the sector supplies the counting or merely accommodates it is the same question the spin articles leave open, and it is not decided by anything in this article.
- **The closed cavity.** A cavity with a discrete spectrum on both sides of the gap has no asymptotic region for the positron, and the charge bookkeeping then involves the walls themselves. Whether the algebra can state the difference between the two idealisations — a well in empty space and a closed cavity — is not shown, and the question has no counterpart in the step.

## Summary

A well of depth $V_0$ and width $L$ in the electrostatic potential is the Klein step with a finite region. The reduced Dirac pair is matched at the two walls, and the even and odd conditions are $\frac{k_{\Phi,\mathrm{ev}}}{E+mc^{2}}=\frac{k_{\Phi,\mathrm{w}}\tan(k_{\Phi,\mathrm{w}}a)}{E+V_0+mc^{2}}$ and $\frac{k_{\Phi,\mathrm{ev}}}{E+mc^{2}}=-\frac{k_{\Phi,\mathrm{w}}\cot(k_{\Phi,\mathrm{w}}a)}{E+V_0+mc^{2}}$, with $k_{\Phi,\mathrm{w}}=\frac{\sqrt{(E+V_0)^{2}-m^{2}c^{4}}}{\hbar c}$ and $k_{\Phi,\mathrm{ev}}=\frac{\sqrt{m^{2}c^{4}-E^{2}}}{\hbar c}$.

At the lower edge of the gap the left side diverges and the conditions reduce to $\cos(k_{\Phi,\mathrm{w}}a)=0$ and $\sin(k_{\Phi,\mathrm{w}}a)=0$, that is $k_{\Phi,\mathrm{w}}a=n_{\mathrm{w}}\pi/2$, and the threshold depth is

$$
V_0^{\mathrm{cr}}=mc^{2}\left[1+\sqrt{1+\left(\frac{n_{\mathrm{w}}\pi}{k_mL}\right)^{2}}\;\right],
$$

which exceeds $2mc^{2}$ by the confinement energy $\frac{n_{\mathrm{w}}^{2}\pi^{2}\hbar^{2}}{2mL^{2}}$ at leading order and tends to the floor $2mc^{2}$ as $L\to\infty$, the floor being the value that the step attains as its critical height and that no finite width reaches. Inverting the formula at fixed depth counts the levels that have crossed, $N(V_0,L)=\lfloor (k_mL/\pi)\sqrt{(V_0/mc^{2}-1)^{2}-1}\rfloor$ for $V_0>2mc^{2}$ and zero otherwise, with the dives equally spaced in width at multiples of $L_{\min}=\pi\hbar c/\sqrt{V_0^{2}-2V_0\,mc^{2}}$. The count rises with the width and vanishes as the box narrows, so a small box protects the vacuum rather than emptying it, and the region carries $Q=-eN$. The closed form was checked against the matched conditions: the level descends to $E=-mc^{2}$ without a jump, the threshold condition holds to $3\times10^{-10}$ there, and above it no level of that parity remains in the gap. For $k_mL=10$ the threshold is $2.048187\,mc^{2}$; for $k_mL=40$ it is $2.003080\,mc^{2}$; the scaling in $n_{\mathrm{w}}/(k_mL)$ is exact.

The criterion that separates this model from a stable confining model is which side of the mass shell the confining term enters. The electrostatic well shifts the energy, $E\mapsto E-ϙ\xi$, so that the temporal coefficient $k_{t}^{\prime}$ is the one whose sign is dragged, and the sign of $k_{t}^{\prime}$ is what selects the branch. The Dirac oscillator's non-minimal term shifts the spatial part instead, and its product adds $+m^{2}\omega^{2}r^{2}$, so that $E^{2}=m^{2}c^{4}+c^{2}\mathcal Q_{+}\mathcal Q_{-}$ with $\mathcal Q_{+}\mathcal Q_{-}\ge0$ and the spectrum is gapped for every frequency. A static spatial confinement cannot create pairs, which is why a magnetic field creates none; a temporal one can, given the depth. The mass step is the third case, stable for the same reason as the oscillator, and the three are tabulated above.

In a step the created pair leaves as a current and no level holds the imbalance. In a bounded region the imbalance sits in one level: the crossed level is occupied in the state of least energy, the hole is emitted as a positron, and the region is left with a field charge $-e$ per crossed level, $-2e$ with spin. The counting is the standard overcritical bookkeeping and is imported; the algebra supplies the level, the gap and the crossing, and the sector of the current, and nothing about occupation.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $e_t=1$, $\vec e_x,\vec e_y,\vec e_z$ | Quaternion units, $\vec e_\eta^{2}=-e_t$ |
| $\mathbb{B}_{\Phi}$ | Material sector, with $Q_t=i r'_t$ and $\partial/\partial R_t=-i\,\partial/\partial r'_t$ |
| $\tilde\nabla=e_t\,\partial/\partial R_t+\sum_\eta\vec e_\eta\,\partial/\partial R_\eta$ | Biquaternionic gradient |
| $\tilde{Ξ}_{\mathrm{sp},1}$, $\tilde{Ξ}_{\mathrm{sp},2}$ | The two components of the reduced spinor |
| $V_0$, $L$, $a=L/2$ | Well depth, width, and half-width |
| $ϙ\xi(r_x)=-V_0$ inside the well | Electrostatic potential energy |
| $E$, $mc^{2}$, $(-mc^{2},mc^{2})$ | Total energy, rest energy, and the gap |
| $k_{\Phi,\mathrm{w}}=\frac{\sqrt{(E+V_0)^{2}-m^{2}c^{4}}}{\hbar c}$ | Wave number inside the well |
| $k_{\Phi,\mathrm{ev}}=\frac{\sqrt{m^{2}c^{4}-E^{2}}}{\hbar c}$ | Decay constant outside the well; $1/k_{\Phi,\mathrm{ev}}$ the decay length |
| $n_{\mathrm{w}}=1,2,3,\dots$ | Half-wavelengths across the well; odd is the even solution |
| $V_0^{\mathrm{cr}}=mc^{2}[1+\sqrt{1+(n_{\mathrm{w}}\pi/(k_mL))^{2}}]$ | Threshold depth of the $n_{\mathrm{w}}$-th level |
| $N(V_0,L)=\lfloor\frac{k_mL}{\pi}\sqrt{(V_0/mc^{2}-1)^{2}-1}\rfloor$ | Number of levels that have crossed into the lower continuum; zero for $V_0\le2mc^{2}$ |
| $L_{\min}=\frac{\pi\hbar c}{\sqrt{V_0^{2}-2V_0\,mc^{2}}}$ | Least width at which one level dives at fixed depth; the $n_{\mathrm{w}}$-th dive is at $n_{\mathrm{w}}L_{\min}$ |
| $\tilde K_{\Phi}\tilde K_{\Phi}^{\natural}=-k_m^{2}$, $k_{t}^{\prime\,2}=k_{\Phi}^{2}+k_m^{2}$ | Mass shell, split into its two sides |
| $k_{t}^{\prime}=\frac{E}{\hbar\,c}$, $k_{\Phi}=\frac{p}{\hbar}$ | Temporal coefficient and momentum wave number |
| $\vec\nabla_{\pm}=\vec\nabla\pm\frac{m\,\omega}{\hbar}\vec r$ | The two non-minimal shifts of the oscillator |
| $\mathcal Q_{+}\mathcal Q_{-}\ge0$ | Oscillator identity: the gap is empty at every frequency |
| $\omega$ | Oscillator frequency, a real scalar; the pseudoscalar $\omega=-\vec e_z$ of the algebra is not used here |
| $\beta$ | The frame action of the oscillator, a right action equal to $\pm1$ on the two frame parts |
| $\tilde J_{\Phi}=ic\,j_0e_t+\vec j$ | Conserved material-sector current |
| $\mathfrak{Z}$, $\mathfrak{Z}\approx173$ | Nuclear charge number and the critical value of the Coulomb problem |

## Further Reading

- O. Klein, "Die Reflexion von Elektronen an einem Potentialsprung nach der relativistischen Dynamik von Dirac," *Zeitschrift für Physik* **53** (1929) 157–165, for the step and the paradox.
- F. Sauter, "Über das Verhalten eines Elektrons im homogenen elektrischen Feld nach der relativistischen Theorie Diracs," *Zeitschrift für Physik* **69** (1931) 742–764, for the smoothed step.
- A. Calogeracos and N. Dombey, "History and physics of the Klein paradox," *Contemporary Physics* **40** (1999) 313–321, for the modern reading of the step and the box.
- I. Pomeranchuk and Ya. Smorodinsky, "On the energy levels for a system of two charges $Ze$ and $e$," *Journal of Physics USSR* **9** (1945) 97, for the critical charge of the Coulomb problem.
- Ya. B. Zel'dovich and V. S. Popov, "Electronic structure of superheavy atoms," *Soviet Physics Uspekhi* **14** (1972) 673–694, for the diving of the level and the charged vacuum.
- J. Rafelski, B. Müller and W. Greiner, "The charged vacuum in over-critical fields," *Nuclear Physics B* **68** (1974) 585–604, for the vacuum charge and its compensation.
- W. Greiner, B. Müller and J. Rafelski, *Quantum Electrodynamics of Strong Fields* (Springer, 1985), for the overcritical well, the dive and the charged vacuum in full.
- W. Greiner, *Relativistic Quantum Mechanics: Wave Equations* (Springer, 2000), for the square well, the step and the Klein region.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the matching at a potential discontinuity and the hole-theoretic interpretation.
- M. Moshinsky and A. Szczepaniak, "The Dirac oscillator," *Journal of Physics A: Mathematical and General* **22** (1989) L817–L819, for the non-minimal substitution whose confinement is Klein-stable.
- F. Domínguez-Adame and M. A. González, "Solvable linear potentials in the Dirac equation," *Europhysics Letters* **13** (1990) 193–198, for the linear confining potential solved exactly, the ancestor of the oscillator's substitution.
- A. Bardeen, M. S. Chanowitz, S. D. Drell, M. Weinstein and T.-M. Yan, "Heavy quarks and strong binding: a field theory of hadron structure," *Physical Review D* **11** (1975) 1094–1136, for the scalar confinement whose step has no Klein threshold.
- The companion articles of this series: [The Klein Paradox in Biquaternionic Form](the-klein-paradox-in-biquaternionic-form.html), [The Dirac Oscillator in Biquaternionic Form](the-dirac-oscillator-in-biquaternionic-form.html), [The Dirac Sea, Hole Theory and Antimatter in Biquaternionic Form](the-dirac-sea-hole-theory-and-antimatter-in-biquaternionic-form.html), [Scalar Pair Creation in Biquaternionic Form](scalar-pair-creation-in-biquaternionic-form.html), [The Vacuum State and the Casimir Effect in Biquaternionic Form](the-vacuum-state-and-the-casimir-effect-in-biquaternionic-form.html), and [The Hydrogen Atom in Biquaternionic Form — The Relativistic Case](the-hydrogen-atom-in-biquaternionic-form-the-relativistic-case.html).
