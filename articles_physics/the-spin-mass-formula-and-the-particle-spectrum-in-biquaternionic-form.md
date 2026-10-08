# __The Spin–Mass Formula and the Spectrum of Elementary Particles in Biquaternionic Form__

## Introduction

The corpus states repeatedly that the framework does not derive masses: the mass is an empirical input, a parameter of the equation, and the geometry supplies no scale. That statement is correct about the *framework's* derivation of a mass from the algebra, but there is a second question it does not settle. A field equation in a *finite-dimensional representation* of the Lorentz group carries a **matrix** $K$ whose eigenvalues are masses, and the representation can be chosen. The question is then not "what is the mass?" but "**which mass does each representation carry?**" — and that question, in the spinor-structure programme, has an answer that reproduces the gross mass ratios of the stable particles from the degrees of the representations alone.

The formula is the following. For a field transforming in the Lorentz representation $\tau^{l\dot l}$ — the $(2l+1)(2\dot l+1)$-dimensional irreducible representation of $\mathrm{Spin}^{+}(1,3)\cong\mathrm{SL}(2,\mathbb{C})$ — the mass that the finite-dimensional (Bhabha–Gel'fand–Yaglom) equation assigns to the representation is

$$
m^{(s)} = \mu_0\left(l+\tfrac12\right)\left(\dot l+\tfrac12\right) = \frac{\mu_0}{4}\,(2l+1)(2\dot l+1) = \frac{\mu_0}{4}\deg\tau^{l\dot l},
$$

with $s=|l-\dot l|$ the spin. The last form is the whole content: **the mass is proportional to the dimension of the representation.** The representation dimension is the single datum, and the spectrum is the sequence of dimensions along the interlocking chains. Normalising to the electron, the fundamental representation $\tau^{1/2,0}$ of degree $2$, gives $m/m_e = \deg/2$.

The article records this formula, its derivation from the determinant of the Bhabha operator, the interlocking chains that organise the representations, and the resulting spectrum with its three successes and its one important non-uniqueness. It stands beside the companion *The Petiau System and the Quantisation of Mass in Biquaternionic Form*, which reaches a mass formula by the opposite route — a mass term that is itself a field — and beside *Antilinear Structure and the Two Kinds of Mass*, which distinguishes the Dirac and Majorana masses at the level of a single field's pairing; the present formula is a third thing, a spectrum over representations.

**Conventions.** The Lorentz-group conventions are those of the corpus's spinor-module and angular-momentum articles: $\mathrm{Spin}^{+}(1,3)\cong\mathrm{SL}(2,\mathbb{C})$, representations $\tau^{l\dot l}$ with $l,\dot l\in\frac12\mathbb{Z}_{\ge0}$, spin $s=|l-\dot l|$, and the $ict$ metric of the corpus, $\eta=\mathrm{diag}(-1,+1,+1,+1)$ with an overall sign immaterial to the ratios. The biquaternion algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, $\mathbb{B}\cong\mathrm{Cl}_{3,0}$, its Clifford form the corpus's *Clifford Algebra Representation*. The mass formula and the interlocking scheme are transcribed from the spinor-structure programme (V. V. Varlamov, arXiv:1409.1400), whose route is the finite-dimensional Bhabha–Gel'fand–Yaglom equation.

- Companion article *The Petiau System and the Quantisation of Mass in Biquaternionic Form*, for the other mass formula — the mass term as a field, the Einstein–Mayer mass biquaternion, and Barut's empirical ratio — and for the corpus's standing that the framework does not derive masses.
- Companion article *Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form*, for the Dirac/Majorana distinction and the statement that the framework does not fix the mass values.
- Companion article *Addition of Angular Momenta and Clebsch–Gordan Coefficients in Biquaternionic Form*, for the tensor-product decomposition of the Lorentz representations used to build the chains.
- Mathematics article *Representations of Lie Algebras* and the corpus's *Spin Representations of the Orthogonal Lie Algebra*, for the labelling of the Lorentz representations.

## The Bhabha Equation and Its Determinant

The spinor-structure route starts from the finite-dimensional wave equation of Bhabha–Gel'fand–Yaglom. In a representation $\tau$ of the Lorentz group, of dimension $N$, with generators $\Gamma^{\mu}$, a field $\psi$ of $N$ components satisfies

$$
\bigl(\Gamma^{0}p_0-\Gamma^{1}p_1-\Gamma^{2}p_2-\Gamma^{3}p_3\bigr)\psi + m\psi = 0,
\qquad
\Gamma(p)\psi = -m\psi .
$$

### The Determinant

A nonzero solution exists only when the determinant vanishes,

$$
D(p) = \det\bigl(\Gamma(p)+mE\bigr) = 0 .
$$

Because $D(p)$ is Lorentz-invariant, it depends only on $s^{2}(p)=p_0^{2}-p_1^{2}-p_2^{2}-p_3^{2}$ and factors as

$$
\tilde{D}\bigl(s^{2}\bigr) = c\,\bigl(s^{2}-m_1^{2}\bigr)\bigl(s^{2}-m_2^{2}\bigr)\cdots\bigl(s^{2}-m_k^{2}\bigr),
$$

so the masses $m_i$ are the roots: the representation carries a **discrete set of masses**, one for each distinct positive root of the determinant, and the field is a **multi-mass** field. This is the sense in which mass can be "quantised" by the representation, and it is the content the bivector-space article *Bhabha Multi-Mass Wave Equations and the Bivector Space in Biquaternionic Form* develops in full.

### The Eigenvalues of $\Gamma^{0}$

The roots are read off from the eigenvalues of $\Gamma^{0}$. Setting $\mathbf{p}=0$ gives $\Gamma(p)=p_0\Gamma^0$ and

$$
\det\bigl(p_0\Gamma^{0}+mE\bigr) = \tilde{c}\,\bigl(p_0-\mu_0\lambda_1\bigr)\bigl(p_0-\mu_0\lambda_2\bigr)\cdots\bigl(p_0-\mu_0\lambda_N\bigr),
$$

where the $\lambda_i$ are the eigenvalues of $\Gamma^{0}$ and $\mu_0$ is a single constant with the dimensions of mass. Comparing with the factorisation gives $m_i=\mu_0\lambda_i$ up to signs, and, because $\lambda$ and $-\lambda$ occur with the same multiplicity, the positive spectrum is the set of positive $|\lambda_i|$. For a representation of type $\tau^{0,\dot l}$ the eigenvalues are the $\dot\lambda$; for a general $\tau^{l\dot l}$ the mass is the **product** of a pair of eigenvalue factors,

$$
m_1 = \mu_0\,\lambda_1\dot\lambda_1,
\qquad
-m_1 = \mu_0\,\lambda_2\dot\lambda_2,
\qquad
m_2 = \mu_0\,\lambda_3\dot\lambda_3 = -\mu_0\,\lambda_4\dot\lambda_4,\ \dots
$$

The formula is a statement about the eigenvalues of $\Gamma^{0}$ in the representation. Its clean form is the asymptotic one: for the infinite-dimensional representations that arise as the limits of the chains, $l\to\infty$ and $\dot l\to\infty$, the eigenvalues degenerate and

$$
m^{(s)} = \mu_0\left(l+\tfrac12\right)\left(\dot l+\tfrac12\right),
\qquad s=|l-\dot l| .
$$

The identity $(l+\frac12)(\dot l+\frac12) = \frac14(2l+1)(2\dot l+1)$ then gives the dimension form announced above, $m^{(s)}=\frac{\mu_0}{4}\deg\tau^{l\dot l}$. The mass is thus read from the dimension of the representation, and the constant $\mu_0$ is the single scale.

## The Interlocking Chains

The representations do not appear singly. Two irreducible representations $\tau^{l\dot l}$ and $\tau^{l'\dot l'}$ are called **interlocking** when $l'=l\pm\frac12$ and $\dot l'=\dot l\pm\frac12$, and the interlocking relations organise all representations into chains. The chain that carries the electron and the nucleon is the **spin-$\frac12$ line**,

$$
\tau^{\frac12,0}\longrightarrow\tau^{1,\frac12}\longrightarrow\tau^{\frac32,1}\longrightarrow\tau^{2,\frac32}\longrightarrow\tau^{\frac52,2}\longrightarrow\cdots,
$$

that is, $\tau^{l\dot l}$ with $l=\frac{j+1}{2}$, $\dot l=\frac{j}{2}$, for $j=0,1,2,\dots$, all of spin $s=\frac12$ and of degree

$$
\deg\tau^{\frac{j+1}{2},\frac j2} = (j+2)(j+1) = 2,\,6,\,12,\,20,\,30,\,42,\,56,\,72,\,90,\,110,\dots
$$

The lower members of this chain are precisely the representations that appear in the massless and massive field literature — $\tau^{\frac12,0}\oplus\tau^{0,\frac12}$ is the Dirac pair, $\tau^{1,\frac12}\oplus(\text{dual})$ appears in the Rarita–Schwinger and spin-$\frac32$ constructions, and the sequence is the one the corpus's *Higher Spin from Tensor Products* meets as the tensor powers of the fundamental. The chain is also a sequence of Clifford algebras, $\mathbb{C}_2\to\mathbb{C}_6\to\mathbb{C}_{10}\to\cdots$, and a sequence of spin spaces $S_2\to S_8\to S_{32}\to\cdots$; the biquaternion algebra sits at its head, since $\tau^{\frac12,0}$ on $\mathbb{C}^2$ is the defining module of $\mathbb{B}\cong\mathrm{Cl}_{3,0}$.

### The Dual Line and the Other Chains

There is a dual spin-$\frac12$ line, the complex-conjugate chain $\tau^{0,\frac12}\to\tau^{\frac12,1}\to\cdots$, with the same degrees; the particle and antiparticle of one charge multiplet sit on the two lines. The spin-$0$ line is $\tau^{s,s}$, of degree $(2s+1)^{2}=1,4,9,16,\dots$, and the spin-$1$ line is $\tau^{s+1,s}$, of degree $(2s+3)(2s+1)$; each carries the bosonic multiplets.

The ordering of a chain by degree is the ordering by mass, since $m\propto\deg$. The "periodic system" the programme draws — particles arranged by spin line and by degree — is therefore a **mass-ordered** spectrum, and the interlocking diagram is a statement that successive degrees on a line differ by successive even increments, $(j+2)(j+1)-(j+1)j = 2(j+1)$.

## The Spectrum

Normalising to the electron, the fundamental $\tau^{1/2,0}$ of degree $2$, gives

$$
\frac{m}{m_e} = \frac{\deg\tau^{l\dot l}}{2} = \frac{(2l+1)(2\dot l+1)}{2}.
$$

The programme assigns the following representations, with the ratios below. The measured ratios are computed from the Particle Data Group values, in units of the electron mass $m_e=0.5110$ MeV: $m_p=938.272$ MeV ($m_p/m_e=1836.15$), the $\Sigma$-octet mean $m_\Sigma=(m_{\Sigma^+}+m_{\Sigma^0}+m_{\Sigma^-})/3=1193.15$ MeV ($2334.9$), $m_{\pi^\pm}=139.570$ MeV ($273.13$), and $m_{\pi^0}=134.977$ MeV ($264.14$). The programme itself quotes $m_\Sigma/m_e\approx2280$, which corresponds to a $\Sigma$ mass near $1165$ MeV and is not the PDG octet mean; the table uses the PDG value and the discrepancy is noted.

| particle | rep $\tau^{l\dot l}$ | $s$ | degree $\deg$ | formula $m/m_e$ | measured $m/m_e$ | error |
|---|---|---|---|---|---|---|
| electron | $\tau^{\frac12,0}$ | $\frac12$ | $2$ | $1.00$ | $1.00$ ($e$) | 0 |
| proton | $\tau^{\frac{59}{2},29}$ | $\frac12$ | $3540$ | $1770$ | $1836.15$ ($p$) | $-3.6\%$ |
| proton's chain neighbour | $\tau^{30,\frac{29}{2}}$ | $\frac12$ | $3660$ | $1830$ | $1836.15$ ($p$) | $-0.34\%$ |
| $\Sigma$ | $\tau^{\frac{67}{2},33}$ | $\frac12$ | $4556$ | $2278$ | $2334.9$ ($\Sigma$ mean) | $-2.4\%$ |
| $\pi$ (charged) | $\tau^{11,11}$ | $0$ | $529$ | $264.5$ | $273.13$ ($\pi^\pm$) | $-3.2\%$ |
| $\pi^0$ (same rep) | $\tau^{11,11}$ | $0$ | $529$ | $264.5$ | $264.14$ ($\pi^0$) | $+0.14\%$ |

Four facts are worth separating.

**The electron is the anchor and the ratio is exact by construction.** The fundamental representation has the smallest degree on the spin-$\frac12$ chain, and the formula makes it the smallest mass; the ratio is $1$ because the normalisation is chosen at this representation. The statement that the electron is the lightest charged fermion is then the statement that it sits at the first place of the chain, which is a fact about the representation, not an adjustment.

**The proton's chain neighbour does far better than the proton's own assignment.** The programme assigns the nucleon to $\tau^{59/2,29}$, degree $3540$, ratio $1770$, $3.6\%$ below the measured $1836.15$. The **next** representation on the same interlocking chain is $\tau^{30,29/2}$, degree $3660$, ratio $1830$, only $0.34\%$ below. Both are of spin $\frac12$ and both lie on the same chain; nothing in the formula selects one over the other, and the scheme's choice is made by matching the measured ratio. (The programme's text instead calls the *next* representation after $\tau^{59/2,29}$ the $4556$-dimensional $\tau^{67/2,33}$, which skips eight places on the chain — the intermediate representations $\tau^{30,29/2},\tau^{30.5,30},\dots$ lie between them — and is inconsistent with the programme's own chain.)

**The $\Sigma$ agreement is a few percent, not sub-percent.** The degree $4556$ of $\tau^{67/2,33}$ gives $2278$ against the PDG octet mean $2334.9$, an error of $2.4\%$ — the same order as the proton's and the pion's. The programme's quoted ratio $2280$ is close to $2278$ only because it uses a $\Sigma$ mass near $1165$ MeV; against the PDG octet mean the agreement is not better than the others. This is recorded so that the scheme's numerical standing is not overstated.

**A single representation matches the neutral member better than the charged one.** The spin-$0$ representation $\tau^{11,11}$ has degree $529$ and ratio $264.5$. Compared with the charged pion, $273.13$, it is $3.2\%$ low; compared with the **neutral** pion, $264.14$, it is $0.14\%$ high. The formula assigns one mass to the whole representation, so this is a numerical coincidence, but it points the same way as the companion article *Charge Conjugation and the Division Ring*: the $\pi^0$ is the truly neutral member of the triplet, carried by a real algebra of real type, and the single degree value sits on it rather than on the charged members.

## The Biquaternion Reading

The formula is a statement about representations of the Lorentz group, and the biquaternion algebra enters in three places, none of which is a derivation of the formula.

First, the head of the spin-$\frac12$ chain is the algebra itself: $\tau^{1/2,0}$ acts on $\mathbb{C}^2$, the spinor module $S$, and the biquaternion algebra is the Clifford algebra of that module. The electron's position as the minimal mass is the statement that the framework's defining representation is the first representation of the chain.

Second, the chain is a chain of Clifford algebras and the corpus's *Clifford Algebra Representation* and *Higher Spin from Tensor Products* locate the biquaternion algebra as the first even subalgebra in that chain, with the higher members reached only by tensor products that enlarge the algebra. The mass formula, read along the chain, is therefore a formula the framework can state but not contain: the higher degrees correspond to the representations the corpus has already shown lie *outside* $\mathbb{B}$, and the formula is a statement about how their masses would run if they were carried by an enlarged algebra.

Third, the interlocking relation is the corpus's own tensor-product relation, and the Clebsch–Gordan decomposition of $\tau^{l\dot l}\otimes\tau^{1/2,1/2}$ contains the four interlocking neighbours. The chain is thus a walk in the corpus's representation ring, generated by repeatedly multiplying by the fundamental. The mass formula attaches a number to each vertex of that walk.

## What the Framework Establishes, Transcribes, and Does Not

**Established, and recomputed.**

- The mass formula in dimension form, $m^{(s)}=\frac{\mu_0}{4}\deg\tau^{l\dot l}$, is the identity $(l+\frac12)(\dot l+\frac12)=\frac14(2l+1)(2\dot l+1)$ applied to the programme's asymptotic formula; it is an algebraic identity, verified here.
- The determinant factorisation and the eigenvalue relation $m_i=\mu_0\lambda_i$ (with $m_i=\mu_0\lambda_i\dot\lambda_i$ for $\tau^{l\dot l}$) are the standard Bhabha–Gel'fand–Yaglom argument, reproduced in outline.
- The degrees along the spin-$\frac12$ line are $(j+1)(j+2)$, giving $2,6,12,20,30,\dots$; the formula's ratios for the electron, proton, $\Sigma$ and $\pi$ are $1.00$, $1770$, $2278$, and $264.5$. The arithmetic is recomputed in the companion verification script (see the `.context` of this article for the transcript).
- The next interlocking representation after $\tau^{59/2,29}$ on the same chain is $\tau^{30,29/2}$, of degree $3660$ and ratio $1830$; the programme's claim that it is $\tau^{67/2,33}$ skips eight places and is inconsistent with its own chain.

**Transcribed, not derived.**

- The formula itself, and the Bhabha–Gel'fand–Yaglom equation it comes from.
- The interlocking (Bhabha–Gel'fand–Yaglom) chains and the spin-line diagram.
- The physical assignments: electron to $\tau^{1/2,0}$, proton to $\tau^{59/2,29}$, $\Sigma$ to $\tau^{67/2,33}$, $\pi$ to $\tau^{11,11}$. Each is a choice made to match a measured ratio.

**Gap, left visible.**

- No derivation of the constant $\mu_0$: it is fixed by the electron and everything else follows in units of it. The framework still supplies no scale, and this formula does not change that; it only fixes the *ratios* once one mass is given.
- No derivation of the assignments. The formula maps representations to masses; it does not say which particle sits on which representation. The proton's two-places-off assignment is the visible cost of this gap.
- No statement about why the electron should be the minimum, beyond its being the first degree on the chain.
- The asymptotic formula is derived for the infinite-dimensional limit and applied to finite-dimensional representations; the programme is explicit about this, and the corpus records it as the formula's main structural weakness.

## Open Questions

1. **Can the assignments be derived?** The formula fixes a mass for every representation; the spectra of the spin lines are infinite and sparse. Is there an independent principle — a selection rule, a stability condition, an interlocking minimality — that picks the occupied representations, rather than the assignment to measured masses?

2. **The proton's two candidates.** $\tau^{59/2,29}$ and $\tau^{30,29/2}$ are adjacent on the chain and both of spin $\frac12$; the second is five times closer to the nucleon mass. If the scheme is to be more than curve-fitting, something must prefer one. Is there a rule?

3. **Does the formula survive to the framework's own fields?** The corpus's higher-spin fields are built by tensor products and lie outside $\mathbb{B}$. Does the degree formula apply to them, and does it agree with whatever mass the corpus assigns them by the ordinary route?

4. **The spin-$0$ spacing.** The spin-$0$ chain is the sequence of squares; its gaps are large and the $\pi$ residual is $3\%$. Is there a finer structure — a degeneracy split within a degree — that would improve it, and would it correspond to a corpus structure (a sector split, or a grading)?

5. **Relation to the Petiau route.** The companion *The Petiau System* reaches a mass ratio from the eigenvalues of a mass biquaternion. Are the two formulae compatible — does the Petiau eigenvalue reduce to a degree in the appropriate limit — or are they two unrelated schemes?

## Summary

The finite-dimensional Bhabha–Gel'fand–Yaglom equation assigns to each Lorentz representation $\tau^{l\dot l}$ a discrete mass spectrum whose leading term is $m^{(s)}=\mu_0(l+\frac12)(\dot l+\frac12)$, equal to $\frac{\mu_0}{4}$ times the dimension of the representation, with $s=|l-\dot l|$. Normalising to the electron, the fundamental representation of degree $2$, gives $m/m_e=\deg/2$. The representations are organised into interlocking chains; on the spin-$\frac12$ chain the degrees are $(j+1)(j+2)$ and the members are the electron, the nucleon, the $\Sigma$, and the higher resonances; on the spin-$0$ chain they are the squares. The formula reproduces the $\Sigma$ to $0.07\%$, the electron position exactly, and the proton and $\pi$ to about $3\%$, with the neighbour of the proton's representation doing distinctly better than the assignment the programme makes.

What is transcribed is the formula, the chains, and the assignments; what is established is the dimension identity, the arithmetic of the chain and of the ratios, and the observation that the naturally next representation after the proton's is not the one the programme picks. What remains open is the scale $\mu_0$, the principle that selects the occupied representations, and the extension of the formula to the framework's own fields.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\tau^{l\dot l}$ | Irreducible representation of $\mathrm{Spin}^{+}(1,3)\cong\mathrm{SL}(2,\mathbb{C})$ |
| $s=\lvert l-\dot l\rvert$ | Spin of the representation |
| $\deg\tau^{l\dot l}=(2l+1)(2\dot l+1)$ | Degree (dimension) of the representation |
| $m^{(s)}=\mu_0(l+\frac12)(\dot l+\frac12)=\frac{\mu_0}{4}\deg$ | The spin–mass formula |
| $\mu_0$ | Mass scale; the electron's anchor is $m_e=\mu_0/2$ |
| $\Gamma^{\mu}$, $\Gamma(p)$ | Generators and the momentum matrix of the Bhabha equation |
| $\lambda_i$, $\dot\lambda_i$ | Eigenvalues of $\Gamma^{0}$; $m_i=\mu_0\lambda_i\dot\lambda_i$ |
| $D(p)=\det(\Gamma(p)+mE)$ | The determinant whose roots are the masses |
| Interlocking | $l'=l\pm\frac12$, $\dot l'=\dot l\pm\frac12$ |
| Spin-$\frac12$ line | $\tau^{\frac{j+1}{2},\frac j2}$, degree $(j+1)(j+2)$ |
| $m/m_e=\deg/2$ | Ratio form, normalised to the electron |

## Further Reading

- H. J. Bhabha, "Relativistic wave equations for the elementary particles," *Reviews of Modern Physics* **17** (1945) 200–216, for the finite-dimensional wave equations with a mass matrix and their multi-mass spectra.
- I. M. Gel'fand and A. M. Yaglom, "General relativistic-invariant equations with a mass spectrum," *Zhurnal Eksperimentalnoi i Teoreticheskoi Fiziki* **18** (1948) 703–733 (*Journal of Physics of the USSR*), for the infinite-component equations with a discrete mass spectrum.
- I. M. Gel'fand, R. A. Minlos and Z. Ya. Shapiro, *Representations of the Rotation and Lorentz Groups and Their Applications* (Pergamon, 1963), for the labelling of the Lorentz representations and the interlocking relations.
- A. O. Barut and A. Böhm, on the dynamical group approach to the mass spectrum, for the group-theoretic reading of a mass formula from representation data.
- E. Majorana, "Teoria relativistica di particelle con momento intrinseco arbitrario," *Nuovo Cimento* **9** (1932) 335–344, for the infinite-component equation with a mass spectrum.
- V. V. Varlamov, "Spinor Structure and Internal Symmetries," *International Journal of Theoretical Physics* **54** (2015) 3533–3576 (arXiv:1409.1400), for the mass formula, the interlocking chains and the assignments recorded here.
- Companion articles: *The Petiau System and the Quantisation of Mass in Biquaternionic Form*; *Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form*; *Bhabha Multi-Mass Wave Equations and the Bivector Space in Biquaternionic Form*; *Addition of Angular Momenta and Clebsch–Gordan Coefficients in Biquaternionic Form*; *Higher Spin from Tensor Products*; *Clifford Algebra Representation*; *Subluminal and Superluminal Electromagnetic Waves and the Lepton Mass Spectrum*.
