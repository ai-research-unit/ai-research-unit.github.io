# __The Hydrogen Atom in Biquaternionic Form — The Relativistic Case__

## Introduction

The relativistic hydrogen atom is the **Dirac–Coulomb problem**: a spin-$\tfrac12$ particle of mass $m$ bound by the central potential

$$
V(r) = -\frac{\kappa}{r}, \qquad \kappa = \frac{\mathfrak{Z}e^2}{4\pi\epsilon_0},
$$

with $\mathfrak{Z}$ the nuclear charge number (written $Z$ in the non-relativistic companion, and $\mathfrak{Z}$ here so that it cannot be read as a spatial index). It is the relativistic completion of the problem treated in the companion article *The Hydrogen Atom in Biquaternionic Form — The Non-Relativistic Case*, and the differences are structural rather than quantitative. There the Coulomb Hamiltonian was the central scalar $\tilde R_\Psi = r_t\,e_t$; the spin was a spectator, the orbital and spin operators occupied complementary slots that commuted, and the level depended on $n$ alone. Here the Hamiltonian is no longer central, the spin is dynamical, and the level depends on $n$ and $s_{\mathrm{tot}}$.

The article asks what the biquaternion framework contributes to this problem, and the honest answer is stated before the derivation.

- **Algebraic, and recomputed here.** The total angular momentum $\tilde S_{\Psi,\mathrm{tot},k} = L_{\mathrm{orb},k} e_t + \tilde S_{\Psi,k}$, with the orbital part in the scalar slot and the spin part in the vector slots, closes on the angular-momentum algebra. The spin–orbit operator $\sum_k (L_{\mathrm{orb},k}e_t)\tilde S_{\Psi,k}$ is a Hermitian element of the informational sector $\mathbb{B}_{\Psi}$; it commutes with $\tilde S_{\Psi,\mathrm{tot},k}$, but not with $L_{\mathrm{orb},k}$ or $\tilde S_{\Psi,k}$ separately, which is the algebraic statement that the spin is no longer a spectator. The relativistic level is labelled by $(n,s_{\mathrm{tot}})$ and not by $(n,l)$: at fixed $n$ the states of different $s_{\mathrm{tot}}$ separate in energy, and of the non-relativistic $l$-degeneracy there survives only the pair $l = s_{\mathrm{tot}}\mp\tfrac12$ at fixed $s_{\mathrm{tot}}<n-\tfrac12$. All of this is checked below.
- **Transcribed, not derived.** The exact bound-state energies are the standard Sommerfeld–Dirac spectrum, quoted in full in its place. The transcription reproduces them and predicts no deviation. Its non-relativistic limit and fine structure are worked through in the companion article *The Dirac Equation in Biquaternionic Form — Solutions and the Non-Relativistic Limit* and its exercise, which is where the elimination of the small component lives; the exact bound-state solution itself is the standard radial Dirac–Coulomb one, and the corpus carries a *transcription* of it — the radial system and its Laguerre solution rewritten in the algebra's notation — in the companion article *Biquaternion Representation of Spin One Half and the Relativistic One-Electron Atom*, but no derivation of it from the algebra's own equation. No independent biquaternionic derivation is claimed.
- **Gap, left visible.** The corpus's biquaternion Dirac equation carries the **linear**, chirality-off-diagonal mass pair $\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R} = k_m\tilde{Ξ}_{\mathrm{sp},L}$, $\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L} = k_m\tilde{Ξ}_{\mathrm{sp},R}$, and in the algebra reading this mass term passes through a local central phase: the vector $\mathrm{U}(1)$ (fermion number) is exact for the massive field, and the symmetry the mass breaks is the axial one. On the cell-frame reading of the element the same left multiplication is the axial rotation, so the choice is the matter-representation question recorded in the minimal-coupling article. The algebra-level electromagnetic coupling is therefore available in the massive case in the algebra reading, and its precise form is set out in the companion article *The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism*, which derives the coupled equation and proves it gauge covariant. What the corpus does not supply is the radial Dirac–Coulomb solution inside the algebra; the Coulomb field is introduced here in the **cell-frame transcription**, which is the form in which the standard Dirac–Coulomb solution is known, and the spectrum is transcribed. This is the gap that remains, and it is not closed by notation.
- **Conditional, and input.** The transcription is written for continuous functions, and a numerical realization of it needs a finite basis, which the corpus does not carry. The framework puts one condition on that basis — the small part must be generated from the large by the framework's own action — and the condition is the non-relativistic relation of the companion exercise read the other way round; with a field present the covariance identity forces the covariant version of the action and the phase of the basis. The basis sets themselves, and the variational argument that makes the condition necessary, are input.

The title covers the relativistic case as the framework's algebraic structures reach it; it is not a claim that the framework derives the Sommerfeld spectrum from its own algebra-level equation. That derivation is not carried out in the corpus, so the claim is not made.

## The Dirac–Coulomb Problem

### The potential in the framework's notation

The framework's four-potential is the material-sector object

$$
\tilde A_{\Phi} = i\,a'_t\,e_t + \vec A \in \mathbb{B}_{\Phi},
$$

and a static point nucleus is the special case $\vec A = 0$ with $\xi_{\mathrm{scl}} = \mathfrak{Z}e/(4\pi\epsilon_0 r)$, so that the potential energy of a charge $ϙ$ in it is $ϙ\xi_{\mathrm{scl}}$, which for the electron, $ϙ = -e$, is $ϙ\xi_{\mathrm{scl}} = -e\mathfrak{Z}e/(4\pi\epsilon_0 r) = -\kappa/r$. Two honest remarks, both inherited from the non-relativistic article, belong here. First, the $1/r$ form is **input**: the companion Maxwell article produces the field of a point charge as an imaginary vector in $\mathbb{B}_{\Psi}$, but the point-charge source is supplied, not derived. Second, the framework does not supply the value of $\kappa$ or of the dimensionless coupling

$$
\alpha =\frac{k_m\,e^{2}}{4\,m\,c^{2}\,\pi\,\epsilon_{0}}, \qquad \kappa = \mathfrak{Z}\frac{m\,c^{2}\,\alpha}{k_m},
$$

which enters the spectrum as a parameter.

### The algebra equation and its cell-frame reading

The framework's field is an element $\tilde{Ξ}_{\mathrm{sp}}$ of $\mathbb{B}$, and the position dependence is carried by its argument rather than by the finite-dimensional algebra. The internal two-valued index of the older literature is that element read in a frame fixed by a declared unit vector; it is a reading of the field and not the field. The standard equation carries four entries because the element carries four coefficients, and the two halves of that four are the chirality labels $L$ and $R$.

The coordinates are the corpus's, $Q_t = i r'_t$ and $Q_k = x_k$, with $r'_t$ the real time of the material sector. With that choice $\partial/\partial R_t = -i\partial/\partial r'_t$, so $\tilde\nabla\tilde\nabla^{\natural} = \partial^2/\partial R_t^2 + \nabla^2 = -\tfrac{1}{c^2}\partial^2/\partial {r'_t}^2 + \nabla^2$ is the d'Alembertian with no metric factor to put in by hand.

The free biquaternion Dirac equation is the one-sided chiral pair

$$
\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R} = k_m\tilde{Ξ}_{\mathrm{sp},L} ,
\qquad
\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L} = k_m\tilde{Ξ}_{\mathrm{sp},R} .
$$

It is a pair, not one equation, and the two-sided operator structure is why. The gradients act by left multiplication, and a left multiplication preserves each chiral half. The mass term must mix the halves, so it cannot be a left multiplication; it is the off-diagonal pairing $\tilde{Ξ}_{\mathrm{sp},R}\leftrightarrow\tilde{Ξ}_{\mathrm{sp},L}$, with the central scalar $m e_t$ as its coefficient. Chirality itself is the right multiplication $-iR_{\mathrm{axf},\vec e_z}$. The mass coefficient is central and does not disturb it, but the pairing is odd under it: the mass is off-diagonal in the chiral grading, and that oddness is what the axial current later measures. That is the algebraic content of the pair: at $m=0$ it decouples into two Weyl equations, one for each chirality.

A second form, Kravchenko's two-sided equation, is a change of representation rather than a second definition — the derivatives act from the left and the mass from the right through a conjugation — and it is not used here because it carries no continuous central phase to gauge (*The Dirac Equation in Biquaternionic Form*, §*The One-Sided and the Two-Sided Equation*).

Read in the cell frame, where a cell acts on the element as $\tilde Q\mapsto a\tilde Qb$, the pair becomes the standard Dirac–Coulomb equation. Write $\beta$ for the cell $\tilde Q\mapsto i\tilde Q\vec e_x$ and $\alpha_k$ for the cell $\tilde Q\mapsto\vec e_k\tilde Q\vec e_z$. Then

$$\frac{m\,c\,i}{k_m}\frac{\partial\tilde{Ξ}_{\mathrm{sp}}}{\partial  r'_t}
= -\frac{m\,c^{2}\,i}{k_m}\sum_k  \vec e_k\,\frac{\partial\tilde{Ξ}_{\mathrm{sp}}}{\partial x_k}\,\vec e_z
+ i mc^2\,\tilde{Ξ}_{\mathrm{sp}}\,\vec e_x + V(r)\,\tilde{Ξ}_{\mathrm{sp}} ,
$$

with $V(r) = ϙ\xi_{\mathrm{scl}} = -\kappa/r$. The cell $\beta$ acts on one side only — its left factor is the time unit, which multiplies as the identity — while the three $\alpha_k$ act on both sides. What the equation uses is their algebra: each squares to the identity action, and distinct ones anticommute,

$$
\alpha_k^2 = \beta^2 = 1 ,
\qquad
\alpha_i\alpha_j+\alpha_j\alpha_i = 0 \ \ (i\neq j),
\qquad
\alpha_k\beta+\beta\alpha_k = 0 ,
$$

the anticommutators because $\vec e_i\vec e_j=-\vec e_j\vec e_i$ with $\vec e_z\vec e_z=-e_t$ common to both terms, and because $\vec e_x\vec e_z=-\vec e_z\vec e_x$. So that $(c\sum_k\alpha_k p_k+\beta mc^2)^2 = c^2\vec p^{\,2}+m^2c^4$ on the free field.

In this frame the four generators have the Euclidean sign pattern, every square being the identity action. Multiplying the three $\alpha_k$ by $\beta$ on both sides flips them, $\beta\alpha_k\beta=-\alpha_k$, so the four generators

$$
\beta,\quad \beta\alpha_1,\quad \beta\alpha_2,\quad \beta\alpha_3
$$

have the Lorentzian pattern instead — one square the identity action and three its negative — and that is the frame of *The Legacy Pauli Gamma Formulation* below, where it is written in the algebra's own words. Both frames are frames of the same two-sided operator algebra $\mathbb{B}\otimes\mathbb{B}_{\mathrm{opp}}$, so nothing physical depends on which is written: the spectrum, the currents and the chiral structure are the same objects in either, the flip moving no level, so that no sign convention among the three is physical. The frame matters only in the algebra's own reading, where the two-sided cells are what carry the structure, and that reading is given once, in the gamma section.

The cell algebra acts on $\mathbb{B}$ by $\tilde{Ξ}_{\mathrm{sp}}\mapsto a\tilde{Ξ}_{\mathrm{sp}} b$, so reading $\tilde{Ξ}_{\mathrm{sp}}$ in the cell frame gives the four entries the standard equation carries, and the free part of that reading is the same chiral pair. The Coulomb term is a **central scalar**, $V(r)e_t \in \mathbb{B}_{C}$, so it multiplies the field without ambiguity of order, and in this respect its placement is the same as the non-relativistic potential's.

A structural caveat must accompany this transcription. The cell $\beta$ is a right multiplication by the element $i\vec e_x$ of $\mathbb{B}$, while the mass pair above is built from left multiplications alone; the two therefore sit on different sides of the field. The cell-frame reading uses the two-sided structure that the algebra-level equation does not itself contain: $\beta$ exchanges the two chiralities, since $R_{\vec e_x}$ anticommutes with the chirality cell $-iR_{\vec e_z}$, whereas every left multiplication preserves them. The mass is not the obstruction — both descriptions carry the same linear mass, and they agree on it — and the two-sided reading supplies the structure that the Hamiltonian's Foldy–Wouthuysen reduction needs. The transcription is the one the corpus's electron and solutions articles use, and it is adopted here on that basis, with the caveat recorded rather than hidden.

## The Hamiltonian Leaves the Scalar Slot

In the non-relativistic problem the Hamiltonian is a scalar multiple of the identity, $\tilde R_\Psi = r_t\,e_t$, and its vanishing vector part is what makes the spin a spectator. The relativistic corrections change this. The kinetic and Darwin corrections remain scalar; the spin–orbit correction occupies the vector slots of $\mathbb{B}_{\Psi}$, and that is the algebraic change. The Zeeman term below is non-central in the same way, but it vanishes in the Coulomb problem, where $\vec A = 0$ and hence $\vec B = 0$.

At relative order $c^{-2}$ the elimination of the small component produces the effective large-component Hamiltonian

$$
H =\frac{\vec \pi^{2}}{2\,m} + ϙ\xi_{\mathrm{scl}} - \frac{ϙ}{m}\sum_k  B_k\tilde S_{\Psi,k}
- \frac{\vec\pi^4}{8m^3c^2}
+ \frac{1}{8\,k_m^{2}}\nabla^2 V
- \frac{ϙ}{2m^2c^2}\sum_k  (\vec E\times\vec\pi)_k\tilde S_{\Psi,k},
$$

with $\vec\pi = \vec p - ϙ\vec A$ the kinetic momentum, whose last three terms are the relativistic kinetic correction, the Darwin term, and the spin–orbit coupling. It is derived in the companion exercise on the Pauli equation, which checks the coefficients against the exact spectrum; it is quoted here only for its structure. The **spin–orbit** term is the one that changes the character of the Hamiltonian. For a central potential it reads

$$
-\frac{ϙ}{2m^2c^2}\sum_k (\vec E\times\vec\pi)_k\tilde S_{\Psi,k}
= \frac{1}{2m^2c^2}\frac{1}{r}\frac{dV}{dr}\,\sum_k L_{\mathrm{orb},k}\tilde S_{\Psi,k} ,
$$

and in the framework's operators the coupling is

$$
\boxed{\;\sum_k  (L_{\mathrm{orb},k} e_t)\tilde S_{\Psi,k} =\frac{m\,c\,i}{2\,k_m}\,\sum_k  L_{\mathrm{orb},k} \vec e_k \in  \mathbb{B}_{\Psi}\;}
$$

where $\tilde S_{\Psi,k} =\frac{m\,c}{2\,k_m}i\vec e_k$ and the single $i$ is the central imaginary. This is a Hermitian element of the informational sector: its scalar part vanishes and its vector part is purely imaginary. It is therefore **not central** — a central element lies in the complex line $\mathbb{B}_{C}$, and $\sum_k (L_{\mathrm{orb},k}e_t)\tilde S_{\Psi,k}$ has a nonzero imaginary vector part whenever the orbital motion is non-trivial. The relativistic Coulomb Hamiltonian is not a scalar multiple of $e_t$.

**The spin is no longer a spectator.** The algebraic statement of this is the commutator structure of the spin–orbit operator. It is rotationally invariant,

$$
\bigl[\sum_k (L_{\mathrm{orb},k}e_t)\tilde S_{\Psi,k},\ \tilde S_{\Psi,\mathrm{tot},j}\bigr] = 0,
$$

so that the total angular momentum remains conserved, but it does not commute with the orbital or the spin operators separately,

$$
\bigl[\sum_k (L_{\mathrm{orb},k}e_t)\tilde S_{\Psi,k},\ L_{\mathrm{orb},j}\bigr] \neq 0, \qquad
\bigl[\sum_k (L_{\mathrm{orb},k}e_t)\tilde S_{\Psi,k},\ \tilde S_{\Psi,j}\bigr] \neq 0 .
$$

The two failures are not the same failure, and neither is the one that removes $l$. The second, $[\,\cdot,\tilde S_{\Psi,j}]\neq0$, is the statement that the spin has become dynamical: the spin–orbit part of the Hamiltonian does not commute with $\tilde S_{\Psi,j}$, so $m_s$ is not separately conserved. The first says the same for the orbital magnetic number: $m_l$ is lost, and only $m_j = m_l+m_s$ survives, which is why the coupled basis is the one that diagonalises the problem. Neither removes $l$ itself, because $\vec L\cdot\vec S$ is a scalar under simultaneous rotations of the two factors and so commutes with both Casimirs:

$$
\bigl[\sum_k (L_{\mathrm{orb},k}e_t)\tilde S_{\Psi,k},\ \bigl(L_{\mathrm{orb}}\bigr)^2\bigr] = 0,
\qquad
\bigl[\sum_k (L_{\mathrm{orb},k}e_t)\tilde S_{\Psi,k},\ \tilde S_{\Psi}^2\bigr] = 0 .
$$

What removes $l$ is the Dirac structure, and only in the exact problem. In a Dirac–Coulomb eigenstate the upper and lower components carry the two different orbital quantum numbers $l = j\mp\tfrac12$, so $L^2$ has no single eigenvalue on the state and $l$ cannot label it; the state is labelled by $(n,j,\pi)$, the two $l$ values being degenerate in energy. On the non-relativistic fine-structure Hamiltonian, which acts on the upper component alone, $L^2$ is still good, and the degeneracy of the two $l$ at fixed $j$ there is the residual Coulomb degeneracy rather than a rotational one.

All three statements were recomputed from the commutators of the three operators on the coupled states, where $\tilde S_{\Psi,\mathrm{tot},i}$ and $\tilde S_{\Psi,\mathrm{tot},j}$ close on $\frac{m\,c\,i\,\epsilon_{ijk}\,\tilde{S}_{\Psi,\mathrm{tot},k}}{k_m}$, the operator $\sum_k (L_{\mathrm{orb},k}e_t)\tilde S_{\Psi,k}$ commutes with every $\tilde S_{\Psi,\mathrm{tot},j}$, with $(L_{\mathrm{orb}})^2$ and with $(\tilde S_{\Psi})^2$, and its commutators with $L_{\mathrm{orb},j}$ and $\tilde S_{\Psi,j}$ are nonzero; at $l=1$ the eigenvalues of $\sum_k (L_{\mathrm{orb},k}e_t)\tilde S_{\Psi,k}$ are the two values $+\frac{m^{2}\,c^{2}}{2\,k_m^{2}}$ and $-\frac{m^{2}\,c^{2}}{k_m^{2}}$, for $s_{\mathrm{tot}} = \tfrac32$ and $s_{\mathrm{tot}} = \tfrac12$ respectively, in agreement with the general formula below.

## Total Angular Momentum and the Good Quantum Numbers

The **total angular-momentum operator** is the sum of the orbital and spin parts,

$$
\tilde S_{\Psi,\mathrm{tot},k} = L_{\mathrm{orb},k} e_t + \tilde S_{\Psi,k} ,
$$

Because the two parts commute and each satisfies the angular-momentum algebra, so does the sum:

$$
[\tilde S_{\Psi,\mathrm{tot},i},\tilde S_{\Psi,\mathrm{tot},j}] =\frac{m\,c\,i\,\epsilon_{ijk}\,\tilde{S}_{\Psi,\mathrm{tot},k}}{k_m}.
$$

The Casimir takes the value

$$
\tilde S_{\Psi,\mathrm{tot}}^{\,2} \;\longrightarrow\;\frac{m^{2}\,c^{2}\,s_{\mathrm{tot}}\,(s_{\mathrm{tot}}+1)}{k_m^{2}}$$

on the coupled states, with the two branches of the coupling

$$
s_{\mathrm{tot}} = l \pm \tfrac12 \ \ (l \ge 1), \qquad s_{\mathrm{tot}} = \tfrac12 \ \ (l = 0) .
$$

These are the framework's own statements, established in *Angular Momentum and Spin in Biquaternionic Form*; they are used here, not rederived.

The relativistic Coulomb eigenstates are the coupled states $|n,l,s_{\mathrm{tot}},s_{\mathrm{tot},z}\rangle$ built with the Clebsch–Gordan coefficients of $\tfrac12\otimes l$, the $l$ in the ket being the orbital quantum number of the upper component. The good quantum numbers are

$$
n, \quad s_{\mathrm{tot}}, \quad s_{\mathrm{tot},z},
$$

together with the parity, and with the ranges

$$
s_{\mathrm{tot}} = \tfrac12, \tfrac32, \dots, n-\tfrac12, \qquad s_{\mathrm{tot},z} = -s_{\mathrm{tot}},\dots,+s_{\mathrm{tot}} ,
$$

where $s_{\mathrm{tot}}$ is the corpus's name for the total angular momentum, written $j$ in the standard literature. The orbital quantum number $l$ is not among them, for two distinct reasons that are easy to run together. Within a single eigenstate the large component carries $l_+$ and the small component carries $l_- = 2s_{\mathrm{tot}}-l_+$, so $L^2$ has no single eigenvalue on the state. Across eigenstates, at fixed $n$ and $s_{\mathrm{tot}}<n-\tfrac12$, both values $l = s_{\mathrm{tot}}\mp\tfrac12$ occur, in two different states of equal energy; those two carry opposite parity, $\pi = (-1)^{l_+}$, so they are two states at one energy rather than one state with two $l$. The parity entry is what recovers $l$, which makes $(n,s_{\mathrm{tot}},s_{\mathrm{tot},z},\pi)$ a complete set — the standard $(n,j,m_j,\pi)$. At the top value $s_{\mathrm{tot}}=n-\tfrac12$ only $l=n-1$ occurs and there is no partner.

What the relativistic treatment breaks, then, is not the degeneracy inside a pair but the degeneracy across different $s_{\mathrm{tot}}$ at fixed $n$. The degeneracy inside a pair is the Coulomb accident: the rotation group knows only $s_{\mathrm{tot}}$ and keeps the $2s_{\mathrm{tot}}+1$ magnetic values together, while the two parities sitting at one energy is a property of the exact $1/r$ potential, and any departure from a point $1/r$ source — a finite nuclear radius, or the Lamb shift — separates them.

**What is algebraic and what is not.** The framework's contribution to this section is the spin factor: the $\tilde S_{\Psi,k} =\frac{m\,c}{2\,k_m}i\vec e_k$ in the vector slots, the commutator $[\tilde S_{\Psi,i},\tilde S_{\Psi,j}] =\frac{m\,c\,i\,\epsilon_{ijk}\,\tilde{S}_{\Psi,k}}{k_m}$, and the Hermitian placement of $\tilde S_{\Psi,\mathrm{tot},k}$ in $\mathbb{B}_{\Psi}$. The orbital factor is carried by the position dependence of the field, not by the finite-dimensional algebra, and the Clebsch–Gordan coefficients are the standard ones. As the companion article records, the algebra $\mathbb{B}$ carries as its own internal representations only $s = 0$ and $s = \tfrac12$; the orbital representation is external structure on which the algebra's spin acts. The coupling of the two, which is what makes this problem relativistic, is therefore only partly algebraic.

## The Exact Spectrum

### The Sommerfeld–Dirac formula

The companion non-relativistic article already quotes the following formula in its closing bridge to this case. It is restated here because the present article is where its labels, its domain, its degeneracy bookkeeping, and its derivation status are developed; the formula itself is inherited from that article and from the standard solution, not rederived.

The exact bound-state energies of the Dirac–Coulomb problem are

$$
\boxed{\;E_{n s_{\mathrm{tot}}} = mc^2\left[1 + \frac{(\mathfrak{Z}\alpha)^2}{\bigl(n - \delta_{s_{\mathrm{tot}}}\bigr)^2}\right]^{-1/2}\;}
$$

with the Sommerfeld parameter

$$
\delta_{s_{\mathrm{tot}}} = s_{\mathrm{tot}} + \tfrac12 - \sqrt{\bigl(s_{\mathrm{tot}} + \tfrac12\bigr)^2 - (\mathfrak{Z}\alpha)^2},
$$

and with the labels of the previous section. The spectrum depends on $n$ and $s_{\mathrm{tot}}$ only, which is the analytic statement of the degeneracy pattern: the two $l$ values at fixed $s_{\mathrm{tot}}<n-\tfrac12$ share an energy, and the $2s_{\mathrm{tot}}+1$ values of $s_{\mathrm{tot},z}$ do as well.

The formula is the standard exact Dirac–Coulomb result. It is quoted, not derived here, and it is not derived anywhere in the corpus from the algebra's own equation. The companion solutions article and its exercise carry out the non-relativistic limit and the $c^{-2}$ corrections and check them against this formula; the exact bound-state solution — the radial Dirac–Coulomb equations and their Laguerre solution — is transcribed in the algebra's notation in *Biquaternion Representation of Spin One Half and the Relativistic One-Electron Atom*, which re-encodes the matrix solution as a biquaternion and says so. What neither supplies is the derivation: the radial system obtained from the algebra's equation, with the mass term and the coupling as the corpus carries them. The domain of the formula is

$$
\mathfrak{Z}\alpha < s_{\mathrm{tot}} + \tfrac12 ,
$$

since otherwise the square root is imaginary. At the endpoint the root vanishes, and for the lowest state of that $s_{\mathrm{tot}}$, $n = s_{\mathrm{tot}}+\tfrac12$, the formula returns $E=0$; beyond it there is no normalizable bound state, the level having dived into the negative continuum. For $s_{\mathrm{tot}}=\tfrac12$ the bound is $\mathfrak{Z} < \alpha^{-1} \approx 137$, and the supercritical regime beyond it is outside the article.

### The non-relativistic limit and the fine structure

Expanding in powers of $(\mathfrak{Z}\alpha)^2$ reproduces the non-relativistic spectrum at leading order and the fine structure at the next.

$$
\boxed{\;
\begin{aligned}
E_{n s_{\mathrm{tot}}} &= mc^2 - \frac{mc^2(\mathfrak{Z}\alpha)^2}{2n^2}\\[2pt]
&\quad - \frac{mc^2(\mathfrak{Z}\alpha)^4}{2n^3}\left(\frac{1}{s_{\mathrm{tot}}+\tfrac12} - \frac{3}{4n}\right)
+ O\bigl((\mathfrak{Z}\alpha)^6\bigr) .
\end{aligned}\;}
$$

The leading term is the non-relativistic $E_n$ of the companion article,

$$
E_n = -\frac{k_m^{2}\,\kappa^{2}}{2\,m\,c^{2}\,n^{2}} = -\frac{mc^2(\mathfrak{Z}\alpha)^2}{2n^2},
$$

and the next is the **fine structure**

$$
\Delta E_{\text{fs}} = -\frac{mc^2(\mathfrak{Z}\alpha)^4}{2n^3}\left(\frac{1}{s_{\mathrm{tot}}+\tfrac12} - \frac{3}{4n}\right),
$$

whose $s_{\mathrm{tot}}$-dependence is the $l$-splitting read off the exact formula. The expansion was recomputed exactly, in rational arithmetic, for every $n \le 6$ and every $s_{\mathrm{tot}}$ allowed at that $n$, and again in closed form for general $n$ at $s_{\mathrm{tot}} = \tfrac12, \tfrac32, \tfrac52$: the coefficient of $(\mathfrak{Z}\alpha)^2$ is $-1/(2n^2)$ and the coefficient of $(\mathfrak{Z}\alpha)^4$ is $-\tfrac{1}{2n^3}(\tfrac{1}{s_{\mathrm{tot}}+1/2}-\tfrac{3}{4n})$ in every case, with no discrepancy.

The fine-structure shift decomposes into three physical contributions — the relativistic kinetic correction, the spin–orbit term, and the Darwin term — which the companion exercise obtains from the Foldy–Wouthuysen expansion. Their sum equals the exact $(\mathfrak{Z}\alpha)^4$ coefficient for every level with $n \le 6$, which was rechecked here in exact rational arithmetic; that agreement is the quantitative sense in which the framework's spin–orbit operator $\sum_k (L_{\mathrm{orb},k}e_t)\tilde S_{\Psi,k}$ carries the right coupling. The Darwin term is a pure scalar, and it is a contact term: $\nabla^2(1/r) = -4\pi\delta(\vec r)$ makes it act on $s$ states alone. The kinetic term is scalar too; only the spin–orbit term is a non-central $\mathbb{B}_{\Psi}$ observable, which is why the spin-dependent splitting is the part of the spectrum that the sector structure makes visible.

### Degeneracy and its redistribution

The relativistic spectrum has the same **total** state count at each $n$ as the non-relativistic one, redistributed across the new labels. At fixed $n$ the values of $s_{\mathrm{tot}}$ are $\tfrac12, \tfrac32, \dots, n-\tfrac12$. For each $s_{\mathrm{tot}} < n - \tfrac12$ there are two orbital values $l = s_{\mathrm{tot}} \mp \tfrac12$ and $2s_{\mathrm{tot}}+1$ magnetic values; for $s_{\mathrm{tot}} = n-\tfrac12$ only $l = n-1$ is available. Counting,

$$
2\sum_{s_{\mathrm{tot}}=1/2}^{n-3/2}(2s_{\mathrm{tot}}+1) \;+\; \bigl(2(n-\tfrac12)+1\bigr) = 2n^2 ,
$$

which was verified for $n \le 6$. So the framework's state space is not enlarged or reduced by the relativistic treatment; what changes is the **splitting** of the $2n^2$ states into levels $E_{n s_{\mathrm{tot}}}$ that depend on $s_{\mathrm{tot}}$ as well as $n$. The non-relativistic $l$-degeneracy among states of the same $n$ is gone, replaced by the $l = s_{\mathrm{tot}} \mp \tfrac12$ degeneracy at fixed $s_{\mathrm{tot}}<n-\tfrac12$, itself the Coulomb accident rather than a symmetry effect; in the limit $\mathfrak{Z}\alpha \to 0$ the $\delta_{s_{\mathrm{tot}}}$ corrections collapse and the full non-relativistic degeneracy is restored.

## Minimal Coupling and the Massive Sector

The Coulomb field is an electromagnetic field, and in a gauge theory it is introduced by minimal coupling. The framework's biquaternion Dirac equation carries a linear, chirality-off-diagonal mass pair, and the coupling is available at the algebra level: in the algebra reading the central phase passes through the mass term.

Let $\lambda = \exp(\frac{k_m\,i\,ϙ\,\Gamma}{m\,c})$ be a central phase, and let $\tilde A_{\Phi,2} = \tilde A_{\Phi} - \tilde\nabla\Gamma$ be the transformed connection. The covariant derivative

$$
\tilde\nabla_{\mathrm{gco}} = \tilde\nabla +\frac{k_m\,i\,ϙ}{m\,c}\tilde A_{\Phi}
$$

transforms homogeneously,

$$
\tilde\nabla_{\mathrm{gco},2}(\lambda\tilde{Ξ}_{\mathrm{sp}}) = \lambda\, \tilde\nabla_{\mathrm{gco}}\tilde{Ξ}_{\mathrm{sp}} ,
\qquad
\tilde\nabla_{\mathrm{gco},2} = \tilde\nabla +\frac{k_m\,i\,ϙ}{m\,c}\tilde A_{\Phi,2} ,
$$

with the connection transformation that the abelian gauge structure of the framework provides. This covariance, together with the Leibniz rule it needs, was machine-checked by finite differences at a point not used to fix the conventions. The mass term of *The Dirac Equation in Biquaternionic Form* is linear, so it carries the same factor. For the pair

$$
\tilde\nabla_{\mathrm{gco}}\tilde{Ξ}_{\mathrm{sp},R} = k_m\tilde{Ξ}_{\mathrm{sp},L} ,
\qquad
\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde{Ξ}_{\mathrm{sp},L} = k_m\tilde{Ξ}_{\mathrm{sp},R} ,
$$

with

$$
\tilde\nabla_{\mathrm{gco}}^{\natural} = \tilde\nabla^{\natural} +\frac{k_m\,i\,ϙ}{m\,c}\tilde A_{\Phi}^{\natural} ,
$$

the transformed left-hand side is $\lambda\,\tilde\nabla_{\mathrm{gco}}\tilde{Ξ}_{\mathrm{sp},R}$ and the transformed right-hand side is $m\lambda\tilde{Ξ}_{\mathrm{sp},L}$, because the central phase commutes with the mass. The two sides transform identically, so the massive coupled equation is **form-invariant** under the local phase and holds in every gauge when it holds in one. **In the algebra reading every local central phase is allowed, and the vector $\mathrm{U}(1)$ (fermion number) is exact for the massive field; in the cell-frame reading of the element the same left multiplication is the axial rotation, and the vector phase is not a left multiplication.**

The object the phase cannot pass through is not the mass but the algebra's real structure: a coupling built on $\flat = -{}^{*}$, which is antilinear, transforms as $(\lambda\tilde{Ξ}_{\mathrm{sp}})^\flat = \lambda^{*}\tilde{Ξ}_{\mathrm{sp}}^{\flat}$, so a Majorana-type mass $k_m\tilde{Ξ}_{\mathrm{sp}}^{\flat}$ would acquire the factor $\exp(\frac{2\,k_m\,i\,ϙ\,\Gamma}{m\,c})$ and be form-invariant only for $\lambda = \pm1$. That is a statement about the real structure, not about the linear mass term, and it belongs to the companion articles on the neutrino and on chirality. What the mass breaks is the **axial** symmetry,

$$
\sum_\mu\epsilon_\mu\,\frac{\partial j_{5\mu}}{\partial R_\mu} = 2im\,\tilde{Ξ}_{\mathrm{sp}}^{\natural}\bigl(-iR_{\mathrm{axf},\vec e_z}\bigr)\tilde{Ξ}_{\mathrm{sp}} ,
$$

with $\epsilon=(1,-1,-1,-1)$ the sign vector, $-iR_{\mathrm{axf},\vec e_z}$ the chirality cell — the representative on the field of the central grading $\chi=i\tilde{Ζ}_{\mathrm{ad}}$, $\chi^2=e_t$ — and $j_{5\mu}=\tilde{Ξ}_{\mathrm{sp}}^{\natural}G_\mu(-iR_{\mathrm{axf},\vec e_z})\tilde{Ξ}_{\mathrm{sp}}$, where $G_\mu$ are the four cell generators of *Noether's Theorem in Biquaternionic Form*: $G_t$ acts as $\tilde Q\mapsto i\tilde Q\vec e_x$ and $G_k$ as $\tilde Q\mapsto i\vec e_k\tilde Q\vec e_y$. These are the frame elements of *The Legacy Pauli Gamma Formulation*: $G_t$ is the $\beta$ of the Hamiltonian above, and $G_k$ is $\beta\alpha_k$, the Hamiltonian's $\alpha_k$ preceded by $\beta$ — so the two frames differ by that one factor and by nothing else. The vector current is the same expression with the chirality factor omitted. The right-hand side is proportional to $m$, so the axial current is conserved only in the massless limit, while the vector current is conserved for the massive field. This was verified numerically in the Noether article on a superposition of two on-shell plane waves (axial ratio $1.000000$, vector divergence $5.3\times10^{-10}$, both currents conserved at $m = 0$).

The consequences should be stated plainly. The Coulomb potential can be inserted into the algebra-level equation $\tilde\nabla_{\mathrm{gco}}\tilde{Ξ}_{\mathrm{sp},R} = k_m\tilde{Ξ}_{\mathrm{sp},L}$, $\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde{Ξ}_{\mathrm{sp},L} = k_m\tilde{Ξ}_{\mathrm{sp},R}$ by the standard minimal coupling, and in the algebra reading the central phase passes through the mass term; the charge is carried by the massive sector. The precise algebra-level transcription of the electromagnetic coupling — the biquaternion form of $\vec p \to \vec p - ϙ\vec A$ and $\frac{m\,c\,i}{k_m}\partial\frac{k_m}{m\,c\,\partial^{3}\,{r'_{t}}^{2}\,\to\,i}- ϙ\xi_{\mathrm{scl}}$ — is set out in the companion article *The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism*, which derives the coupled equation and proves it gauge covariant. What the corpus does not supply is the radial Dirac–Coulomb solution inside the algebra. Until it is supplied, the relativistic hydrogen atom in biquaternionic form is a transcription of the standard solution into the framework's algebra, not a derivation from the framework's own field equation.

## The Finite Basis and the Balance of the Two Parts

The transcription above is written for continuous fields, and a numerical realization of it needs an object the corpus does not carry: a **finite basis**. The field is expanded in a finite set of functions, the equation is assembled from them, and the levels are read from it. This section states the one condition the framework puts on the choice of basis, says which part of the condition is the framework's and which is input, and records what the condition does not give.

### The two expansions

The field splits into the two eigenspaces of $\beta$: the part $\beta$ fixes and the part it negates. That $\beta^2=1$ is what makes them complementary, and nothing below uses orthogonality — the split is a direct-sum decomposition, and neither the pair nor the condition depends on a Hermitian structure. Write the two parts $\tilde{Ξ}_{\mathrm{sp},\mathrm{lar}}$ and $\tilde{Ξ}_{\mathrm{sp},\mathrm{sml}}$, in the order used by the companion exercise on the non-relativistic limit, where they are called the large and small components. The rest energy dominates the dynamics, so write

$$
\tilde{Ξ}_{\mathrm{sp}} = \exp\!\left(-c\,k_m\,i\,r'_{t}\right)
\bigl(\tilde{Ξ}_{\mathrm{sp},\mathrm{lar}}+\tilde{Ξ}_{\mathrm{sp},\mathrm{sml}}\bigr).
$$

Substituting, cancelling the common phase and projecting onto the two eigenspaces gives the coupled pair; the projection is what puts the momentum term off-diagonal, since $\alpha_k$ carries one eigenspace into the other by $\alpha_k\beta=-\beta\alpha_k$,

$$\frac{m\,c\,i}{k_m}\frac{\partial\tilde{Ξ}_{\mathrm{sp},\mathrm{lar}}}{\partial  r'_t}
= c\sum_k  \pi_k\,\vec e_k\tilde{Ξ}_{\mathrm{sp},\mathrm{sml}}\,\vec e_z + V\tilde{Ξ}_{\mathrm{sp},\mathrm{lar}} ,
$$

$$\frac{m\,c\,i}{k_m}\frac{\partial\tilde{Ξ}_{\mathrm{sp},\mathrm{sml}}}{\partial  r'_t}
= c\sum_k  \pi_k\,\vec e_k\tilde{Ξ}_{\mathrm{sp},\mathrm{lar}}\,\vec e_z - 2mc^2\tilde{Ξ}_{\mathrm{sp},\mathrm{sml}} + V\tilde{Ξ}_{\mathrm{sp},\mathrm{sml}} ,
$$

with $V(r) = ϙ\xi_{\mathrm{scl}} = -\kappa/r$ and the kinetic momentum $\vec\pi = \vec p-ϙ\vec A$. The Coulomb problem has $\vec A = 0$, so that $\vec\pi = \vec p$ there. A finite basis chooses an expansion for each of the two parts — functions $\{f_\mu\}$ for the large part, and a set of its own for the small — and the two choices are independent unless a further condition is imposed.

The condition is read off the corpus's own elimination. Neglecting, in the second equation, the terms that are small compared with $2mc^2$ is what produces the Pauli Hamiltonian; it also produces the relation

$$
\tilde{Ξ}_{\mathrm{sp},\mathrm{sml}} =\frac{1}{2\,m\,c}\sum_k  \pi_k\,\vec e_k\tilde{Ξ}_{\mathrm{sp},\mathrm{lar}}\,\vec e_z + O(c^{-3}),
$$

in which the small part carries the momentum of the large one. **The small part is not an independent object.** A finite basis makes the two expansions independent by construction, so a basis drawn without attention to the relation violates it, and the violation is not harmless: a basis whose two expansions are unrelated exhibits the **variational collapse** of the Dirac problem — spurious solutions, and a computed spectrum that is not bounded below and does not converge to the correct levels (Stanton and Havriliak 1984; Dyall and Fægri 2007). The remedy is not a numerical device laid on the algebra; it is the relation above, imposed as a condition on the basis.

### The balancing action

Generate the small functions from the large ones by the action that stands in that relation. In the framework's terms the gradient's vector part, scaled by $c/k_m/2c$, is

$$
\dfrac{1}{2\,k_m}\sum_k \vec e_k\,\frac{\partial}{\partial x_k}
= \frac{i}{2mc}\sum_k p_k\vec e_k ,
$$

the second form because $\frac{m\,c}{k_m}\partial/\partial x_k = ip_k$. The relation carries $\vec p$ itself, so the action is that object with the factor $i$ removed: left multiplication by $\vec p/(2mc)$, followed by the right multiplier $\vec e_z$, which is what carries the large part into the small one, since $R_{\vec e_z}$ anticommutes with $\beta$ while $L_{\vec p}$ commutes with it. The constant $i$ is the one that carries $\partial_k$ to $\frac{k_m\,p_{k}}{m\,c}$; it multiplies every image alike and changes neither the span of the small space nor the condition, so the relation is what fixes the action and the other form differs from it by that convention alone. Applied to the large functions, the action produces the small ones: the condition is that the small expansion be the image of the large one under it, every large function $f_\mu$ contributing the two entries of

$$\frac{1}{2\,m\,c}\,\vec p\,f_\mu\,\vec e_z .
$$

The condition is called **kinetic balance** when the small set is any set that can represent those images, and **restricted kinetic balance** when it is taken to be exactly the images (Stanton and Havriliak 1984; Dyall and Fægri 2007). In the framework's words it is the non-relativistic relation of the companion exercise read as a condition on the basis rather than as a limit. Here $k_m=mc/\hbar$ is the mass wave number, the inverse of the mass length.

The framework's contribution is one identification and no more. The operator is the momentum's vector part — the gradient's, up to the constant $i$ — so the balance is a statement in the algebra's own slots; that the operator is spin-type is the corpus's placement of the spin in those same vector slots, since $\tilde S_{\Psi,k} =\frac{m\,c}{2\,k_m}i\vec e_k$; and that it is first order in the gradient is why the small functions carry one derivative more than the large. Nothing else in the condition is algebraic: the basis sets, and the variational argument that makes the condition necessary, belong to the literature quoted.

### The field, and the phase of the basis

With a field present the derivative in that action cannot be the ordinary one, and the reason is the covariance identity this article has already used. The minimal-coupling article replaces $\tilde\nabla$ by the covariant derivative

$$
\tilde\nabla_{\mathrm{gco}} = \tilde\nabla+\frac{k_m\,i\,ϙ}{m\,c}\tilde A_{\Phi} ,
$$

and the replacement is not optional for the basis. The sign is the corpus's, which the minimal-coupling article records as the opposite of the standard $\partial_\mu-\frac{k_m\,iϙA_{\mu}}{m\,c}$; the kinetic momentum written $\vec\pi=\vec p-ϙ\vec A$ above is in the standard convention, so the two are one coupling with the opposite sign of $ϙ$, and every statement below carries $\vec A=0$, where no sign can differ. Write

$$
\mathrm{Vect}(\tilde\nabla_{\mathrm{gco}}) = \mathrm{Vect}\!\left(\tilde\nabla\right)+\frac{k_m\,i\,ϙ}{m\,c}\,\mathrm{Vect}\!\left(\tilde A_{\Phi}\right)
$$

for the part of the covariant derivative that carries the spatial derivatives. Then, with the connection $\tilde A_{\Phi,2} = \tilde A_{\Phi}-\tilde\nabla\Gamma$ and the central phase $\lambda = \exp(\frac{k_m\,i\,ϙ\,\Gamma}{m\,c})$,

$$
\mathrm{Vect}(\tilde\nabla_{\mathrm{gco},2})\!\left(\lambda f\right) = \lambda\,\mathrm{Vect}(\tilde\nabla_{\mathrm{gco}})f ,
$$

which is the vector-part form of the covariance identity $\tilde\nabla_{\mathrm{gco},2}(\lambda\tilde{Ξ}_{\mathrm{sp}}) = \lambda \tilde\nabla_{\mathrm{gco}}\tilde{Ξ}_{\mathrm{sp}}$. Two consequences follow, and both are forced rather than chosen. First, the balancing action is built from $\tilde\nabla_{\mathrm{gco}}$ and not from $\tilde\nabla$. Second, the basis functions themselves carry the phase: if the large function is $\lambda f_\mu$ rather than $f_\mu$, then its balanced partner is $\lambda$ times the partner of $f_\mu$, so that the pair transforms homogeneously. A finite basis built in this way is gauge covariant term by term, which is what the gauge invariance of the computed magnetic properties requires.

The two replacements are the ones the literature makes under the names **restricted magnetic balance**, for the use of the covariant momentum in the balancing operator, and **London atomic orbitals**, for the phase-carrying basis functions (London 1937; Aucar, Saue, Jensen and Visscher 1999; Repisky, Komorovsky, Malkina and Malkin 2009; Komorovsky, Repisky, Malkina and Malkin 2010). Both were checked here at machine precision in the algebra's own notation: on a grid of $64$ points with random bandlimited fields, the identity $\tilde\nabla_{\mathrm{gco},2}(\lambda\tilde{Ξ}_{\mathrm{sp}}) = \lambda \tilde\nabla_{\mathrm{gco}}\tilde{Ξ}_{\mathrm{sp}}$ and its vector-part form $\mathrm{Vect}(\tilde\nabla_{\mathrm{gco},2})(\lambda f) = \lambda\,\mathrm{Vect}(\tilde\nabla_{\mathrm{gco}})f$ hold to $8\times10^{-14}$, and the two operator identities above are exact. The covariance could not have failed: $\lambda$ is central, so it passes through every left multiplication, and $\partial  \lambda/\partial x_\mu =\frac{k_m\,i\,ϙ}{m\,c}\lambda\,\partial  \Gamma/\partial x_\mu$ holds exactly, which makes $(\tilde\nabla\lambda)\tilde{Ξ}_{\mathrm{sp}}$ cancel the $-\frac{k_m\,i\,ϙ}{m\,c}(\tilde\nabla\Gamma)\lambda\tilde{Ξ}_{\mathrm{sp}}$ term line by line. The numerical check verifies the implementation, not a delicate cancellation.

### What the balance does and does not give

The condition supplies the basis, not the solution. It gives no radial function, no orbital dynamics, and no value for $\kappa$ or $\alpha$; the radial Dirac–Coulomb solution inside the algebra remains the gap named above, and a balanced basis is the workspace on which such a solution would be expanded rather than the solution itself. Nor is the condition an enlargement of the algebra: the balancing action is the momentum's vector part — the gradient's up to the constant $i$ — and the phase is the $\lambda$ of *The Covariant Derivative and Gauge Connection in Biquaternionic Form*; neither is a new element of $\mathbb{B}$.

What it does give is the statement that the transcription, once discretized, carries the framework's non-relativistic relation and the framework's gauge covariance by construction. Of the two, the relation is the corpus's own used as a condition, and the covariance is the corpus's own identity; the basis sets, and the numerical necessity of imposing them, are input.

## What the Framework Supplies and What It Does Not

The accounting can be put in one table, in the form used by the companion electron article.

| Feature of the relativistic Coulomb problem | Status | Where it comes from |
|---|---|---|
| Total angular momentum $\tilde S_{\Psi,\mathrm{tot},k}$, its algebra, $\tilde S_{\Psi,\mathrm{tot}}^{\,2} \to \frac{m^{2}\,c^{2}\,s_{\mathrm{tot}}\,(s_{\mathrm{tot}}+1)}{k_m^{2}}$ | Algebraic (inherited, rechecked) | $\tilde S_{\Psi,k} =\frac{m\,c}{2\,k_m}i\vec e_k$ in the vector slots; quaternion product |
| Spin–orbit operator $\sum_k (L_{\mathrm{orb},k}e_t)\tilde S_{\Psi,k}$ and its eigenvalues | Algebraic (inherited, rechecked) | $[\tilde S_{\Psi,\mathrm{tot},i},\tilde S_{\Psi,\mathrm{tot},j}] =\frac{m\,c\,i\,\epsilon_{ijk}\,\tilde{S}_{\Psi,\mathrm{tot},k}}{k_m}$; Casimir identity |
| Degeneracy in $l$ broken at fixed $n$; $s_{\mathrm{tot}}$ good, $l$ not; $(n,s_{\mathrm{tot}})$ label | Derived from the spectrum and the Dirac structure | exact $E_{n s_{\mathrm{tot}}}$ depends on $s_{\mathrm{tot}}$ only; the two $l=s_{\mathrm{tot}}\mp\tfrac12$ sit in the two parts of one eigenstate |
| Total state count $2n^2$ preserved, redistributed | Recomputed | sum over $s_{\mathrm{tot}}$ of $(2s_{\mathrm{tot}}+1)\times(\text{number of } l)$ |
| Exact spectrum $E_{n s_{\mathrm{tot}}}$ (Sommerfeld–Dirac) | Transcribed | standard Dirac–Coulomb solution; companion solutions article; radial solution transcribed in *Biquaternion Representation of Spin One Half and the Relativistic One-Electron Atom* |
| Fine-structure shift and its decomposition | Verified (transcribed) | companion Pauli exercise; exact rational check |
| Coulomb potential $V = -\kappa/r$, coupling $\kappa$, $\alpha$, $\mathfrak{Z}$ | Input | point-charge source; values inserted |
| Algebra-level minimal coupling of the massive field | Worked out; massive case covariant in the algebra reading | linear chiral pair; central phase passes through the mass; minimal-coupling article |
| Finite basis for the field | Not in the corpus | input; a basis is supplied, not derived |
| Balance of the large and small parts (kinetic balance) | Algebraic (the relation used as a condition) | $\tilde{Ξ}_{\mathrm{sp},\mathrm{sml}} =\frac{1}{2\,m\,c}\sum_k\pi_k\vec e_k\tilde{Ξ}_{\mathrm{sp},\mathrm{lar}}\vec e_z+O(c^{-3})$; the balancing action $\tilde Q\mapsto\frac{1}{2\,m\,c}\vec p\,\tilde Q\,\vec e_z$ |
| Magnetic balance and the phase of the basis | Forced by the covariance identity | $\tilde\nabla_{\mathrm{gco},2}(\lambda\tilde{Ξ}_{\mathrm{sp}}) = \lambda \tilde\nabla_{\mathrm{gco}}\tilde{Ξ}_{\mathrm{sp}}$, $\tilde A_{\Phi,2} = \tilde A_{\Phi}-\tilde\nabla\Gamma$; minimal-coupling article |
| Basis sets, and the variational collapse of an unbalanced basis | Input | Stanton and Havriliak 1984; Dyall and Fægri 2007 |
| Deviation from standard physics | None found | the spectrum is the standard one |

Three entries deserve a sentence. The first is that the algebraic content is real but narrow: the framework supplies the spin algebra, the sector placement of the spin–orbit coupling, and the bookkeeping of the levels; it does not supply the orbital dynamics, the radial equation, or the coupling constant. The second is the step that remains: the algebra-level coupling is consistent and covariant in the algebra reading, so the obstacle is no longer the mass term there; what the corpus does not supply is the derivation of the radial Dirac–Coulomb solution inside the algebra, and that is the step that would turn the transcription into a derivation. The third is the finite basis: the balance is a condition on the workspace rather than on the algebra, and the framework supplies the condition — its own non-relativistic relation and its own covariance identity — while the basis sets and the variational argument are input. That is the sense in which the title overpromises if read as "derived", and the article does not sign for it.

## Open Questions

1. **The algebra-level minimal coupling.** The coupled massive equation $\tilde\nabla_{\mathrm{gco}}\tilde{Ξ}_{\mathrm{sp},R} = k_m\tilde{Ξ}_{\mathrm{sp},L}$, $\tilde\nabla_{\mathrm{gco}}^{\natural}\tilde{Ξ}_{\mathrm{sp},L} = k_m\tilde{Ξ}_{\mathrm{sp},R}$ is set out in *The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism*, and is proved there to be gauge covariant. The choice of matter representation — left versus right action — remains open in that article and in open question 7 of *The Dirac Equation in Biquaternionic Form*.
2. **The nature of the mass term.** The mass term of *The Dirac Equation in Biquaternionic Form* is the linear, chirality-off-diagonal pair; the algebra's real structure $\flat$ is retained separately, and a coupling built on it — a Majorana-type mass — is a neutral-field pairing. Whether the real form of $\mathbb{B}$ forces a second, neutral massive sector alongside the charged one is open, and the two interpretations have different consequences for the charge sectors.
3. **A framework derivation of the spectrum.** The radial system has been written in the algebra — as the single biquaternion $R = \tfrac{\sqrt2}{r}(Fq_+ + Gq_-)$ of *Biquaternion Representation of Spin One Half and the Relativistic One-Electron Atom* — but that transcription begins from the matrix problem. Can the system be *obtained* from the algebra's own equation, and can the Sommerfeld formula then follow from the algebra's own operators rather than be matched to them?
4. **The supercritical regime.** For $\mathfrak{Z}\alpha$ beyond $s_{\mathrm{tot}}+\tfrac12$ the exact formula loses its bound states; how does the framework describe the diving of the level into the negative continuum?
5. **Radiative corrections.** The Lamb shift and the anomalous moment are loop effects; the framework's classical equation does not contain them (as the electron article records for $g-2$), and a framework account would require the quantized theory.
6. **Many-electron and finite-nuclear-size effects.** The article is for one electron in a fixed point-Coulomb field; the framework's account of the electron–electron interaction and of nuclear structure is not developed here.
7. **Empirical content.** The spectrum predicts nothing beyond standard relativistic quantum physics for hydrogen. Whether any framework-level effect distinguishes the two remains the standing open question.
8. **A complex self-dual Coulomb field.** The construction that generates the Dirac field from a scalar half — *Klein–Gordon from the Dirac Square in Biquaternionic Form*, §*The Converse Direction* — survives an external field only when the complex external field is (anti)self-dual, because minimal coupling makes the two generalized gradients stop commuting and the difference of their products is the field strength. Kassandrov (arXiv:1706.08397) gives the Coulomb case, and the condition takes a definite form: with $\xi_{\mathrm{scl}} = \mathfrak{Z}e/(4\pi\epsilon_0 r)$ and a vector potential whose only nonzero component is $A_{\theta_{\mathrm{azm}}} = i\xi_{\mathrm{scl}}\tan(\theta/2)$, the complex field is (anti)self-dual, $\vec B = i\vec E$. Its real part is the electric Coulomb field, its imaginary part is a magnetic monopole of imaginary strength, and the monopole's string lies on the negative $z$ axis. Whether the spectrum can then be obtained as the spectrum of a scalar equation in that complexified background, and what the imaginary part does to the levels, is not worked out anywhere in the corpus. Kassandrov poses the same question and calls it fundamental for the scheme. The question is worth recording because it makes the complexification a condition on the dynamics rather than a convenience of notation.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The generators carry no frame label: $\gamma_\mu$ is one set of matrices, $\gamma_0^2=I_4$ and $\gamma_k^2=-I_4$. The frame belongs to the coordinate, not to the array.

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra.

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

Because $L_{\mathrm{pau},e_t}$ is the identity of the cell algebra, two of them collapse: $\gamma_0=iR_{\mathrm{pau},\vec e_x}$, which is the $\beta$ of the Hamiltonian above, $\beta=\gamma_0$; and $\gamma_5=-iR_{\mathrm{pau},\vec e_z}$, which is the chirality cell of the axial current. The remaining three are genuinely two-sided.

The squares use $i^2=-1$, the cell rule $L_aR_bL_cR_d=L_{ac}R_{db}$, and $\vec e_k^2=-e_t$, with $L_{\mathrm{pau},e_t}R_{\mathrm{pau},e_t}$ the identity of the cell algebra:

$$
\gamma_0^2=i^2L_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_x\vec e_x}=-L_{\mathrm{pau},e_t}R_{\mathrm{pau},-e_t}=+L_{\mathrm{pau},e_t}R_{\mathrm{pau},e_t},
$$

In the axis-free display:

$$
\gamma_0^2=i^2L_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_x\vec e_x}=-L_{\mathrm{axf},e_t}R_{\mathrm{axf},-e_t}=+L_{\mathrm{axf},e_t}R_{\mathrm{axf},e_t},
$$

$$
\gamma_k^2=i^2L_{\mathrm{pau},\vec e_k\vec e_k}R_{\mathrm{pau},\vec e_y\vec e_y}=-L_{\mathrm{pau},-e_t}R_{\mathrm{pau},-e_t}=-L_{\mathrm{pau},e_t}R_{\mathrm{pau},e_t}.
$$

The same identities in the axis-free display:

$$
\gamma_k^2=i^2L_{\mathrm{axf},\vec e_k\vec e_k}R_{\mathrm{axf},\vec e_y\vec e_y}=-L_{\mathrm{axf},-e_t}R_{\mathrm{axf},-e_t}=-L_{\mathrm{axf},e_t}R_{\mathrm{axf},e_t}.
$$

The timelike generator squares to the identity and the three spatial ones to minus the identity, so the frame has the signature $(+,-,-,-)$. The mixed products vanish for the same reason: in $\{\gamma_0,\gamma_j\}$ the left factors $e_t$ and $\vec e_j$ commute while the right factors $\vec e_y\vec e_x$ and $\vec e_x\vec e_y$ cancel, and in $\{\gamma_i,\gamma_j\}$, $i\neq j$, the right factor $\vec e_y$ is common while the left factors $\vec e_i$ and $\vec e_j$ anticommute.

One product of all four is worth writing out, because it fixes the sign of the chirality cell:

$$
\gamma_0\gamma_1\gamma_2\gamma_3
= L_{\mathrm{pau},e_t\vec e_x\vec e_y\vec e_z}R_{\mathrm{pau},\vec e_y\vec e_y\vec e_y\vec e_x}
= L_{\mathrm{pau},-e_t}R_{\mathrm{pau},\vec e_z}
= -L_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_z},
$$

Read in the axis-free display:

$$
\gamma_0\gamma_1\gamma_2\gamma_3
= L_{\mathrm{axf},e_t\vec e_x\vec e_y\vec e_z}R_{\mathrm{axf},\vec e_y\vec e_y\vec e_y\vec e_x}
= L_{\mathrm{axf},-e_t}R_{\mathrm{axf},\vec e_z}
= -L_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_z},
$$

so that

$$
\gamma_5=i\gamma_0\gamma_1\gamma_2\gamma_3=-iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_z},
\qquad
\gamma_5^2=+L_{\mathrm{pau},e_t}R_{\mathrm{pau},e_t},
\qquad
\{\gamma_5,\gamma_\mu\}=0 .
$$

The same expressions, in the axis-free display:

$$
\gamma_5=i\gamma_0\gamma_1\gamma_2\gamma_3=-iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_z},
\qquad
\gamma_5^2=+L_{\mathrm{axf},e_t}R_{\mathrm{axf},e_t},
\qquad
\{\gamma_5,\gamma_\mu\}=0 .
$$

A single product is a pure tensor; the products form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and a general element is a sum of at most four, with $\ell(M)=\operatorname{rank}c(M)$.

$\gamma_5$ is the reference-frame cell of the chirality operator; the central grading $\chi=i\tilde{Ζ}_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi^2=e_t$ — is a different object, represented by $\gamma_5$ on the Dirac module.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{\mathrm{axf},e_\mu}=C_{\Pi}L_{\mathrm{pau},e_\mu}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

The relativistic hydrogen atom in biquaternionic form is the Dirac–Coulomb problem, and what the framework contributes to it is algebraic. The total angular momentum $\tilde S_{\Psi,\mathrm{tot},k} = L_{\mathrm{orb},k} e_t + \tilde S_{\Psi,k}$ has its orbital part in the scalar slot and its spin part in the vector slots, and it closes on $[\tilde S_{\Psi,\mathrm{tot},i},\tilde S_{\Psi,\mathrm{tot},j}] =\frac{m\,c\,i\,\epsilon_{ijk}\,\tilde{S}_{\Psi,\mathrm{tot},k}}{k_m}$ with $\tilde S_{\Psi,\mathrm{tot}}^{\,2} \to \frac{m^{2}\,c^{2}\,s_{\mathrm{tot}}\,(s_{\mathrm{tot}}+1)}{k_m^{2}}$. The spin–orbit operator $\sum_k  (L_{\mathrm{orb},k}e_t)\tilde S_{\Psi,k} =\frac{m\,c\,i}{2\,k_m} \sum_k  L_{\mathrm{orb},k}\vec e_k$ is a Hermitian element of $\mathbb{B}_{\Psi}$; it commutes with $\tilde S_{\Psi,\mathrm{tot},j}$ but not with $L_{\mathrm{orb},j}$ or $\tilde S_{\Psi,j}$, which is the algebraic content of "the spin is no longer a spectator". The relativistic level is labelled by $(n,s_{\mathrm{tot}},s_{\mathrm{tot},z})$; the degeneracy in $l$ at fixed $n$ is broken down to the pair $l = s_{\mathrm{tot}}\mp\tfrac12$ at fixed $s_{\mathrm{tot}}<n-\tfrac12$, two states of opposite parity at one energy, and the total count $2n^2$ is unchanged.

The exact bound-state energies are the Sommerfeld–Dirac formula

$$
E_{n s_{\mathrm{tot}}} = mc^2\left[1 + \frac{(\mathfrak{Z}\alpha)^2}{\bigl(n-\delta_{s_{\mathrm{tot}}}\bigr)^2}\right]^{-1/2},
$$

with

$$
\delta_{s_{\mathrm{tot}}} = s_{\mathrm{tot}}+\tfrac12 - \sqrt{\bigl(s_{\mathrm{tot}}+\tfrac12\bigr)^2 - (\mathfrak{Z}\alpha)^2},
$$

whose expansion

$$
E_{n s_{\mathrm{tot}}} = mc^2 - \frac{mc^2(\mathfrak{Z}\alpha)^2}{2n^2}
- \frac{mc^2(\mathfrak{Z}\alpha)^4}{2n^3}\left(\frac{1}{s_{\mathrm{tot}}+\tfrac12}-\frac{3}{4n}\right) + O\bigl((\mathfrak{Z}\alpha)^6\bigr)
$$

returns the non-relativistic $E_n$ at leading order and the fine structure at the next, the latter verified by exact rational arithmetic against the kinetic, spin–orbit, and Darwin terms of the companion exercise. The spectrum is the standard one and no deviation is predicted.

A numerical realization of the transcription needs one further object that the corpus does not carry, a **finite basis**: functions $\{f_\mu\}$ for the large part of the field, the functions of the small part being generated from them. The framework puts one condition on the choice. Its own non-relativistic relation, $\tilde{Ξ}_{\mathrm{sp},\mathrm{sml}} =\frac{1}{2\,m\,c}\sum_k\pi_k\vec e_k\tilde{Ξ}_{\mathrm{sp},\mathrm{lar}}\vec e_z+O(c^{-3})$, says that the small part is not independent of the large, and read as a condition on the basis it requires the small functions to be generated by the balancing action $\tilde Q\mapsto\frac{1}{2\,m\,c}\vec p\,\tilde Q\,\vec e_z$; this is the restricted kinetic balance of relativistic quantum chemistry, and without it a finite basis fails variationally. With a field present the momentum in that action is the kinetic one, $\vec p-ϙ\vec A$, and the basis functions themselves carry the central phase $\lambda$; both are forced by the covariance identity $\tilde\nabla_{\mathrm{gco},2}(\lambda\tilde{Ξ}_{\mathrm{sp}}) = \lambda \tilde\nabla_{\mathrm{gco}}\tilde{Ξ}_{\mathrm{sp}}$ with $\tilde A_{\Phi,2} = \tilde A_{\Phi}-\tilde\nabla\Gamma$, and these are the restricted magnetic balance and the London atomic orbitals of the same literature. The condition is on the workspace and not on the algebra, and it supplies no radial solution.

One gap is load-bearing and is left visible. The corpus's biquaternion Dirac equation carries the linear, chirality-off-diagonal mass pair $\tilde\nabla\tilde{Ξ}_{\mathrm{sp},R} = k_m\tilde{Ξ}_{\mathrm{sp},L}$, $\tilde\nabla^{\natural}\tilde{Ξ}_{\mathrm{sp},L} = k_m\tilde{Ξ}_{\mathrm{sp},R}$, through which a local central phase passes in the algebra reading; on the cell-frame reading of the element the same left multiplication is the axial rotation. The massive equation therefore admits the algebra-level minimal coupling in the algebra reading, and the vector $\mathrm{U}(1)$ (fermion number) is exact there, with the axial symmetry broken instead. What the corpus does not supply is the radial Dirac–Coulomb solution inside the algebra: the algebra-level form of the coupling is set out in *The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism*, and the spectrum above is obtained in the cell-frame transcription, which is the form in which the standard Dirac–Coulomb solution is known. The relativistic hydrogen atom is therefore, in this framework, an algebraically structured **transcription** of the standard solution — with the spin algebra, the sector placement, the good quantum numbers, and the level bookkeeping genuinely algebraic, and the derivation from the framework's own field equation an open problem.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_t = 1, \vec e_x, \vec e_y, \vec e_z$ | Quaternion basis, $\vec e_k^2 = -e_t$, $\vec e_\mu \vec e_\nu = \epsilon_{\mu\nu\lambda}\vec e_\lambda$ $(\mu\neq\nu)$ |
| $i$ | Central scalar imaginary, $i^2 = -1$ |
| $\mathbb{B}_{\Phi}$ | Anti-Hermitian subspace (material): imaginary scalar, real vector; $i\mathbb{B}_{\Psi} = \mathbb{B}_{\Phi}$ |
| $\mathbb{B}_{\Psi}$ | Hermitian subspace (informational): real scalar, imaginary vector |
| $\mathbb{B}_{C} = \operatorname{span}_\mathbb{R}\{e_t, ie_t\}$ | Centre of the algebra |
| $\mathsf{M}_2$ | The isomorphism with $M_2(\mathbb{C})$, named where a display is compared; no formula is used in this article |
| $L_{a}R_{b}$ | Two-sided multiplication by the pair $(a,b)$, written in the body as the action $\tilde Q\mapsto a\tilde Qb$; $L_{a}R_{b}L_{c}R_{d} = L_{ac}R_{db}$ |
| $\beta$, $\alpha_k$ | Cells of the frame: $\beta$ acts as $\tilde Q\mapsto i\tilde Q\vec e_x$, $\alpha_k$ as $\tilde Q\mapsto\vec e_k\tilde Q\vec e_z$; $\alpha$ without a subscript is the fine-structure constant |
| $\chi=i\tilde{Ζ}_{\mathrm{ad}}$, $\chi^2=e_t$ | The central grading (the axial generator); not an element of $\mathbb{B}$, represented on the field by the chirality cell $-iR_{\mathrm{axf},\vec e_z}$ |
| $Q_t = i r'_t$, $Q_k = x_k$ | Coordinates; $r'_t$ the real time of the material sector |
| $\tilde\nabla = e_t\partial/\partial R_t + \sum_{k=x,y,z}\vec e_k\partial/\partial R_k$ | Biquaternionic gradient (Dirac operator) |
| $\Box = \tilde\nabla\tilde\nabla^{\natural} = \tilde\nabla^{\natural}\tilde\nabla$ | d'Alembertian |
| $\tilde{Ξ}_{\mathrm{sp}}$, $\tilde{Ξ}_{\mathrm{sp}}^{\flat} = -\tilde{Ξ}_{\mathrm{sp}}^*$ | Biquaternion Dirac field and anti-Hermitian conjugate (the algebra's real structure; not the mass term) |
| $\tilde Q^\natural$ | Conjugate under the anti-automorphism $\natural$, which fixes the central $i$ and negates the spatial units; $\tilde\nabla^\natural$, $\tilde A_{\Phi}^\natural$, $\tilde\nabla_{\mathrm{gco}}^{\natural}$ are its images |
| $\tilde A_{\Phi} = i\,a'_t\,e_t + \vec A \in \mathbb{B}_{\Phi}$ | Electromagnetic four-potential |
| $V(r) = ϙ\xi_{\mathrm{scl}} = -\kappa/r$ | Coulomb potential energy |
| $\kappa = \mathfrak{Z}e^2/(4\pi\epsilon_0) = \mathfrak{Z}\frac{m\,c^{2}\,\alpha}{k_m}$ | Coulomb coupling |
| $\mathfrak{Z}$ | Nuclear charge number; $\kappa=\mathfrak{Z}\frac{m\,c^{2}\,\alpha}{k_m}$ |
| $ϙ$ | Electric charge (corpus convention, Greek koppa); $ϙ=-e$ for the electron |
| $\alpha = e^2/(\frac{4\,m\,c^{2}\,\pi\,\epsilon_{0}}{k_m})$ | Fine-structure constant |
| $L_{\mathrm{orb},k} = -\frac{m\,c\,i\,\epsilon_{klm}\,x_{l}}{k_m}\partial/\partial x_m$ | Orbital angular momentum |
| $L_{\mathrm{orb},k} e_t$ | Orbital operators, scalar slot, in $\mathbb{B}_{\Psi}$ |
| $\tilde S_{\Psi,k} =\frac{m\,c}{2\,k_m}i\vec e_k$ | Spin operators, vector slots, in $\mathbb{B}_{\Psi}$ |
| $\tilde S_{\Psi,\mathrm{tot},k} = L_{\mathrm{orb},k} e_t + \tilde S_{\Psi,k}$ | Total angular momentum; $[\tilde S_{\Psi,\mathrm{tot},i},\tilde S_{\Psi,\mathrm{tot},j}] =\frac{m\,c\,i\,\epsilon_{ijk}\,\tilde{S}_{\Psi,\mathrm{tot},k}}{k_m}$ |
| $\sum_k (L_{\mathrm{orb},k}e_t)\tilde S_{\Psi,k}$ | Spin–orbit operator, in $\mathbb{B}_{\Psi}$; eigenvalues $\frac{m^{2}\,c^{2}}{2\,k_m^{2}}[s_{\mathrm{tot}}(s_{\mathrm{tot}}+1)-l(l+1)-\tfrac34]$ |
| $\lvert n,l,s_{\mathrm{tot}},s_{\mathrm{tot},z}\rangle$ | Coupled relativistic basis |
| $E_{n s_{\mathrm{tot}}}$, $\delta_{s_{\mathrm{tot}}}$ | Exact Sommerfeld–Dirac energy and the Sommerfeld parameter |
| $\Delta E_{\text{fs}} = -\frac{mc^2(\mathfrak{Z}\alpha)^4}{2n^3}\bigl(\frac{1}{s_{\mathrm{tot}}+1/2}-\frac{3}{4n}\bigr)$ | Fine-structure shift |
| $\tilde\nabla_{\mathrm{gco}} = \tilde\nabla+\frac{k_m\,i\,ϙ}{m\,c}\tilde A_{\Phi}$ | Covariant derivative (minimal-coupling article) |
| $\tilde\nabla_{\mathrm{gco}}^{\natural} = \tilde\nabla^{\natural}+\frac{k_m\,i\,ϙ}{m\,c}\tilde A_{\Phi}^{\natural}$ | $\natural$-image of the covariant derivative; operator of the second chiral member |
| $j_{5\mu}=\tilde{Ξ}_{\mathrm{sp}}^{\natural}G_\mu(-iR_{\mathrm{axf},\vec e_z})\tilde{Ξ}_{\mathrm{sp}}$ | Axial current; $G_\mu$ the four cell generators, the vector current omitting the chirality cell |
| $\tilde{Ξ}_{\mathrm{sp},\mathrm{lar}}$, $\tilde{Ξ}_{\mathrm{sp},\mathrm{sml}}$ | Large and small parts of the field: the eigenspaces of $\beta$ for $+1$ and $-1$ (companion Pauli exercise; not the chiral pair) |
| $\{f_\mu\}$ | Large-part functions of the finite basis; the small-part functions are their image under the balancing action |
| $\tilde Q\mapsto\frac{1}{2\,m\,c}\vec p\,\tilde Q\,\vec e_z$ | Balancing action; the image of the large basis is the small basis (kinetic balance) |
| $\mathrm{Vect}(\tilde\nabla_{\mathrm{gco}})$ | Vector part of the covariant derivative; balancing operator with a field present (magnetic balance) |
| $\lambda = \exp(\frac{k_m\,i\,ϙ\,\Gamma}{m\,c})$, $\tilde A_{\Phi,2} = \tilde A_{\Phi}-\tilde\nabla\Gamma$ | Central phase and connection transformation (*The Covariant Derivative and Gauge Connection in Biquaternionic Form*); the phase a basis function carries |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- P. A. M. Dirac, "The quantum theory of the electron," *Proceedings of the Royal Society A* **117** (1928) 610–624, for the original Dirac equation and its hydrogen solution.
- P. A. M. Dirac, *The Principles of Quantum Mechanics* (Oxford, 1930), for the operator treatment of angular momentum and the relativistic hydrogen spectrum.
- H. A. Bethe and E. E. Salpeter, *Quantum Mechanics of One- and Two-Electron Atoms* (Springer, 1957), for the exact Dirac–Coulomb spectrum and its corrections.
- J. D. Bjorken and S. D. Drell, *Relativistic Quantum Mechanics* (McGraw-Hill, 1964), for the standard derivation of the Sommerfeld–Dirac formula.
- V. B. Berestetskii, E. M. Lifshitz, and L. P. Pitaevskii, *Relativistic Quantum Theory* (Pergamon, 1971), for the relativistic hydrogen atom and the supercritical discussion.
- Walter Greiner, *Relativistic Quantum Mechanics: Wave Equations* (Springer, 1990), for the Dirac–Coulomb problem solved in detail.
- J. J. Sakurai and Jim Napolitano, *Modern Quantum Mechanics* (Pearson, 2017), for the non-relativistic comparison and the fine structure.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the relation of biquaternions to $M_2(\mathbb{C})$ and the spinor representation.
- V. V. Kravchenko, "On a Biquaternionic Bag Model," *Zeitschrift für Analysis und ihre Anwendungen* **14** (1995), no. 1, 3–14, for the two-sided quaternionic Dirac equation, in which the mass term acts from the right through a conjugation.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the geometric-algebra treatment of the Coulomb problem and the spin–orbit coupling.
- R. E. Stanton and S. Havriliak, "Kinetic balance: a partial solution to the problem of variational safety in Dirac calculations," *The Journal of Chemical Physics* **81** (1984) 1910–1918, for kinetic balance.
- K. G. Dyall and K. Fægri Jr., *Introduction to Relativistic Quantum Chemistry* (Oxford University Press, 2007), for the balance conditions and the variational failure of an unbalanced basis.
- F. London, "Théorie quantique des courants interatomiques dans les combinaisons aromatiques," *Journal de Physique et le Radium* **8** (1937) 397–409, for the field-dependent phase of the basis functions.
- G. Aucar, T. Saue, H. J. Aa. Jensen, and L. Visscher, "On the origin and contribution of the diamagnetic term in four-component relativistic calculations of magnetic properties," *The Journal of Chemical Physics* **110** (1999) 6208–6218, for magnetic balance and gauge-invariant magnetic properties.
- M. Repisky, S. Komorovsky, O. L. Malkina, and V. G. Malkin, "Restricted magnetically balanced basis applied for relativistic calculations of indirect nuclear spin–spin coupling tensors in the matrix Dirac–Kohn–Sham framework," *Chemical Physics* **356** (2009) 236–242.
- S. Komorovsky, M. Repisky, O. L. Malkina, and V. G. Malkin, "Fully relativistic calculations of NMR shielding tensors using restricted magnetically balanced basis and gauge including atomic orbitals," *The Journal of Chemical Physics* **132** (2010) 154101.
- Sylvia Kaviraj, Stanislav Komorovsky, Trond Saue, and Michal Repisky, "Biquaternion algebra with bilinear multiplication: a general, elegant, and computationally advantageous framework for relativistic electronic structure calculations on CPUs and GPUs," arXiv:2609.02081 [physics.chem-ph] (2026), for the balance conditions in biquaternionic form.
- Companion articles: [The Hydrogen Atom in Biquaternionic Form — The Non-Relativistic Case](the-hydrogen-atom-in-biquaternionic-form-the-non-relativistic-case.html); [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html); [The Dirac Equation in Biquaternionic Form — Solutions and the Non-Relativistic Limit](the-dirac-equation-in-biquaternionic-form-solutions-and-the-non-relativistic-limit.html); [Exercise: The Non-Relativistic Limit and the Pauli Equation](exercise-the-non-relativistic-limit-and-the-pauli-equation.html); [The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism](the-minimal-coupling-of-the-biquaternion-dirac-field-to-electromagnetism.html); [The Electron in Biquaternionic Form](the-electron-in-biquaternionic-form.html); [Angular Momentum and Spin in Biquaternionic Form](angular-momentum-and-spin-in-biquaternionic-form.html); [Biquaternion Representation of Spin One Half and the Relativistic One-Electron Atom](biquaternion-representation-of-spin-one-half-and-the-relativistic-one-electron-atom.html); [Quantum Physics in Biquaternionic Form](quantum-physics-in-biquaternionic-form.html); [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html); [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html).
