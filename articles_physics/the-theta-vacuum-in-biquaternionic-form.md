# __The Theta Vacuum in Biquaternionic Form__

## Introduction

A gauge theory whose configuration space splits into topological sectors does not have a single vacuum. The classical vacua are labelled by an integer, the winding number, and the true vacuum of the quantum theory is a superposition of them,
$$
|\theta\rangle = \sum_{Q\in\mathbb{Z}} e^{\,i\theta Q}\,|Q\rangle ,
$$
weighted by a phase $e^{i\theta Q}$ built from the **topological angle** $\theta$. The phase is precisely the exponential of the topological term
$$
S_\theta = \frac{\theta}{16\pi^2}\int d^4x\;\mathrm{tr}\big(F_{\mu\nu}\tilde F^{\mu\nu}\big) = \theta\,Q ,
$$
whose integrand is a total derivative, whose integral is an integer $Q$, and which therefore contributes to the action only through the sectors. The construction is standard (Callan, Dashen, and Gross 1976; Jackiw and Rebbi 1976; 't Hooft 1976), and the angle is periodic, $\theta\sim\theta+2\pi$, because the phase is.

This article asks what the biquaternion framework contributes to that statement, and the answer is narrower than the subject might suggest. The findings are the following.

1. **The $\theta$ parameter's value space is the algebra's center.** The weighting is a phase, and the biquaternion algebra has a canonical central circle: the complex scalars $\mathbb{C}_{\mathbb{B}}=\mathrm{span}_\mathbb{R}\{e_0,ie_0\}$, the center of $\mathbb{B}$, with the central scalar imaginary $i$ generating the continuous symmetry. The $\theta$ phase $e^{i\theta Q}e_0$ is a **central unitary element**, and the framework therefore supplies the value space in which $\theta$ lives rather than importing it. This is the article's one genuinely algebraic point, and it is exact: centrality means the weighting commutes with every element of $\mathbb{B}$, hence with every module structure, every sector, and every Lorentz rotor, so the $\theta$ vacuum is a scalar phase attached to each topological sector and modifies no biquaternion object.

2. **The $\theta$ vacuum does not change the sector structure.** Because the weighting is central, it multiplies the two sectors identically. The sectors are graded parts of one field related by the central $i$, and a central phase does not disturb that relation: the $\theta$ weighting is blind to the split. The framework's statement is therefore that a $\theta$ vacuum is *compatible* with the sector structure rather than testing it. Nothing in this article requires a non-central operator; that is the trace anomaly's business, and the two are distinguished below.

3. **The $\theta$ angle is the phase of a determinant, and the framework has an account of where a determinant gets a phase.** From *The Functional Determinant in Biquaternionic Form*, a **central** fluctuation operator has a determinant that factors and is real and positive (in a suitable regularisation); a **non-central** operator — the chirality-off-diagonal Dirac mass is the example, since it is a right multiplication — has a determinant with a phase, the eta invariant of the operator family. The $\theta$ angle is read off that phase for the appropriate operator, and this is the structural statement that links the $\theta$ vacuum to the anomaly of the previous article: the anomaly is a scalar coefficient multiplying curvature invariants, the $\theta$ angle is the phase of the same determinant, and the two are different readings of one object.

4. **The framework contributes no new $\theta$ dynamics.** Where $\theta$ comes from, why it is small, and how it is relaxed (the strong-CP problem and the axion) are questions about the Standard Model's field content, and they are outside this subcategory. The framework's real structure $\flat$ has the shape of a charge-conjugation pairing, and the parity properties of the topological density can be read through it; that reading is recorded as interpretation, not as a derivation.

5. **The topology itself is the instanton article's.** The topological charge is the integral of a density whose biquaternion form is $\mathrm{Sc}(\tilde F\star\tilde F)$ in the abelian case and the trace of $\mathcal{F}\mathcal{F}$-linearly in the non-abelian case; the self-duality that saturates the bound uses $\star^2=-1$, which is the instanton article's result, inherited here. This article does not recompute the instanton.

The article proceeds as follows. The next section fixes the topological charge and the $\theta$ term in the framework's notation. A section constructs the $\theta$ vacuum and identifies the weighting as a central phase. A section relates the angle to the phase of the determinant and works the toy model that exhibits a determinant phase. A section treats periodicity and the parity reading of the topological density. A section separates what is established from what is interpretation, and the article closes with open questions.

**Conventions.** We use those of the companion articles, unchanged. The algebra is $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, with basis $e_0=1,e_1,e_2,e_3$, $e_k^2=-e_0$, and central scalar imaginary $i$, $i^2=-1$. The center is $\mathbb{C}_{\mathbb{B}}=\mathrm{span}_\mathbb{R}\{e_0,ie_0\}$; the sectors are $\mathbb{M}_-$ (anti-Hermitian, material, basis $ie_0,e_1,e_2,e_3$) and $\mathbb{M}_+$ (Hermitian, informational, basis $e_0,ie_1,ie_2,ie_3$), with $\mathbb{M}_-=i\mathbb{M}_+$. The trace pairing is $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$, so that $\mathrm{Tr}(e_0)=2$. The material coordinate is $\tilde X=ict\,e_0+\mathbf{x}$; the $ict$ metric is $\eta=\mathrm{diag}(-1,+1,+1,+1)$; the d'Alembertian is the series $\Box=\tilde\nabla\bar{\tilde\nabla}=\partial^2_{ict}+\Delta$. The abelian field strength is $\tilde F=i\sqrt{\epsilon}\,\mathbf{E}-\sqrt{\mu}\,\mathbf{H}$ with invariants $I_1=\mathbf{E}^2-c^2\mathbf{B}^2$ and $I_2=\mathbf{E}\cdot\mathbf{B}$, and the non-abelian curvature is $\mathcal{F}=\tfrac12\sum_{\mu\nu}F_{\mu\nu}\bar e_\mu e_\nu$, both as in *Instantons and Solitons in Biquaternionic Form*. The real structure is $\flat=-\dagger$. These are the conventions of *Conventions in the Biquaternion Universe*, *Instantons and Solitons in Biquaternionic Form*, *The Functional Determinant in Biquaternionic Form*, and *The Trace Anomaly in Biquaternionic Form*.

## The Topological Charge and the $\theta$ Term

The topological objects are fixed first, because the $\theta$ vacuum is a statement about them.

**The abelian density.** For an abelian field the parity-odd invariant is the second one of the instanton article,
$$
I_2 = \mathbf{E}\cdot\mathbf{B} ,
\qquad
\int d^4x\;\mathbf{E}\cdot\mathbf{B} \;=\; \text{(a total derivative)} ,
$$
and in biquaternion form the corresponding density is $\mathrm{Sc}(\tilde F\star\tilde F)$, with $\star$ the Hodge dual obeying $\star^2=-1$ on two-forms. The density is a level-1 scalar read with the trace pairing, so the topological charge is a real number and not a biquaternion: this is the same scalar extraction that makes every action in the series a number.

**The non-abelian charge.** For a non-abelian connection the charge is the second Chern number,
$$
Q = \frac{1}{16\pi^2}\int d^4x\;\mathrm{tr}\big(F_{\mu\nu}\tilde F^{\mu\nu}\big) \in\mathbb{Z},
$$
with $F_{\mu\nu}$ the components of the curvature and the trace over the gauge index. That gauge trace is written $\mathrm{tr}$, lower case, to distinguish it from the framework's own trace pairing $\mathrm{Tr}$; it is the same object *Instantons and Solitons in Biquaternionic Form* writes with the capital symbol, so the two articles' charges agree. In the framework's notation the curvature is $\mathcal{F}=\tfrac12\sum_{\mu\nu}F_{\mu\nu}\bar e_\mu e_\nu$, and the density is the trace of the product of $\mathcal{F}$ with its dual; the integral is an integer for a configuration that is pure gauge at infinity. This is standard (Belavin, Polyakov, Schwarz, and Tyupkin 1975; 't Hooft 1976), and the instanton article computes the explicit configuration and the value $Q=1$ for the one-instanton solution. That value is inherited here.

**The $\theta$ term.** The topological term is
$$
S_\theta = \frac{\theta}{16\pi^2}\int d^4x\;\mathrm{tr}\big(F_{\mu\nu}\tilde F^{\mu\nu}\big) = \theta\,Q ,
$$
a total derivative term that does not affect the equations of motion in any sector of fixed $Q$ but weights the sectors relative to one another in the path integral. It is this weighting, and only this weighting, that the $\theta$ vacuum encodes. The term is P- and T-odd, and it is the unique marginal operator built from the gauge fields that is a total derivative and does not change the perturbative theory.

**Why the framework's contribution is only the value space.** Nothing in the construction of $Q$ or $S_\theta$ uses a biquaternion-specific fact: the charge is a standard topological invariant, the dual is the standard Hodge dual, and the trace is the standard gauge trace. What the framework can supply is (i) the space in which the *phase* lives, which is its center, and (ii) the statement that the determinant whose phase the angle is has a phase only when the operator is non-central. Both are taken up in the next two sections.

## The $\theta$ Vacuum and the Central Phase

The construction is transcribed, and the algebra's contribution is identified within it.

**Sectors and the superposition.** Let $|Q\rangle$ denote a state of definite topological charge. The $\theta$ vacuum is the coherent superposition
$$
|\theta\rangle = \sum_{Q\in\mathbb{Z}} e^{\,i\theta Q}\,|Q\rangle ,
$$
and its defining property is that the topological charge operator acts on it by a phase, $\hat Q|\theta\rangle = -i\frac{\partial}{\partial\theta}|\theta\rangle$; the vacuum is an eigenstate of the large gauge transformation that shifts $Q$ by one, with eigenvalue $e^{-i\theta}$. This is standard, and it is the statement that the large gauge transformation is implemented on the vacuum by a phase rather than by the identity.

**The weighting is central.** The phase $e^{i\theta Q}$ is built from the central $i$, and the central scalars are exactly the center of the algebra:
$$
e^{\,i\theta Q}\,e_0 \in \mathbb{C}_{\mathbb{B}} ,
\qquad
\big[e^{\,i\theta Q}e_0,\;\tilde Q\big] = 0 \quad\text{for every } \tilde Q\in\mathbb{B}.
$$
Three consequences follow and are structural.

- **It commutes with the Lorentz rotors.** The rotor that carries the Lorentz action is a product of quaternion units and their reverses, and a central phase commutes with it; the $\theta$ weighting therefore does not disturb the covariance of any state.
- **It commutes with the module structure.** The module $\mathbb{B}P_+(\hat{\boldsymbol\mu})\cong\mathbb{C}^2$ is an image under the isomorphism $\Phi$, and a central phase acts as a scalar on that image; the weighting multiplies every component of a spinor equally.
- **It is blind to the sectors.** Since $i$ exchanges the sectors, $i\mathbb{M}_+=\mathbb{M}_-$, one might expect a phase built from $i$ to act with opposite signs on the two sectors. It does not: the sectors are the $\pm1$ eigenspaces of the *antilinear* involution $\flat$ and not of $i$, and $i$ is central rather than a grading operator. The phase is the same on both, and the $\theta$ vacuum does not test the sector split.

**The value space is supplied, not imported.** The point worth recording is the first of these consequences read backwards: a superposition of topological sectors requires a phase, a phase requires a unit-modulus group, and the framework has a canonical such group in its center. The $\theta$ parameter is an angle in $\mathbb{C}_{\mathbb{B}}$, and the periodicity $\theta\sim\theta+2\pi$ is the periodicity of the central circle. Nothing in the framework fixes the *value* of $\theta$; it fixes where $\theta$ lives.

**The state space.** The superposition lives in the Fock space of *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*, not in the finite-dimensional algebra. The algebra supplies the phase that weights the sectors and the sector structure of the states being weighted; it does not supply the sectors themselves. This is the module gap that every article in this group records, in its $\theta$-vacuum form.

## The Angle as the Phase of a Determinant

The structural link between the $\theta$ vacuum and the anomaly is that the angle is the phase of a determinant, and the framework has an explicit account of when a determinant has a phase.

**The determinant's phase.** From *The Functional Determinant in Biquaternionic Form*:

- a **central** fluctuation operator $S''=\kappa e_0$ has a determinant that factors; on the two-complex-dimensional module it is $\kappa^2$, real and positive for a positive operator, and its logarithm is the central scalar that enters the effective action;
- a **non-central** operator has a determinant that does not factor, and the determinant acquires a **phase**. The chirality-off-diagonal Dirac mass is the instance: the mass term is a right multiplication, it mixes the two minimal left ideals, and the determinant of the family $\mathcal{D}$ over the family's parameter has a phase given by the eta invariant, the spectral asymmetry of the family.

**The link.** For an operator family whose parameter is a background configuration, the phase of the determinant is the weighted count of spectral crossings, and the topological charge is what the phase counts. The $\theta$ angle enters as the coefficient of that phase. The trace anomaly of the previous article is the *modulus* statement about the same determinant (the conformal variation of $\log|\det|$), and the $\theta$ angle is the *phase* statement about it. This is the article's organising reading: one determinant, two anomalous readings, one central in character and one a phase.

**A toy model exhibiting the phase.** The essential mechanism can be exhibited in two complex dimensions, and it was verified explicitly. Take the chirality-off-diagonal family
$$
\mathcal{D}(\lambda) = \begin{pmatrix}\lambda & m\\ m & -\lambda\end{pmatrix},
\qquad
\det\mathcal{D}(\lambda) = -\lambda^2-m^2 ,
$$
which has the block structure of a mass term coupling two chiralities. Its determinant is negative real for large real $\lambda$ — its phase is $\pi$, not $0$ — and the phase is stable as $\lambda\to\infty$. By contrast the central family
$$
\mathcal{C}(\lambda) = \begin{pmatrix}\lambda & 0\\ 0 & \lambda\end{pmatrix},
\qquad
\det\mathcal{C}(\lambda) = \lambda^2 ,
$$
has a strictly positive determinant and no phase. The two are the framework's central and non-central cases in miniature: a determinant phase requires the operator to mix the two chiralities, which is exactly the non-centrality of the mass term. A *varying* phase requires the crossing itself: with the parameter taken through the degeneracy, as in $\mathcal{D}(\mu)=\left(\begin{smallmatrix}\lambda & i\mu\\ i\mu & -\lambda\end{smallmatrix}\right)$ at $\lambda=1$, the determinant vanishes at $\mu=1$ and its phase jumps from $\pi$ to $0$ across it, so the phase counts the crossing rather than merely reporting the sign of the determinant. The verification below records the numbers. The toy model does not compute a $\theta$ angle — that requires the gauge-field family — but it exhibits *which* operators can produce the phase that a $\theta$ angle is.

**What the phase is not.** The phase of the determinant is not the $i\epsilon$ prescription (which fixes a contour, not a topology), not the sign ambiguity of a fermion determinant (which is a boundary condition on the family, not a winding), and not the central phase of the previous section (which weights sectors and is an input to the state). The framework's cleanliness here is that the three are different objects: the central phase lies in the center, the determinant phase lies in the argument of a complex number computed from a non-central operator, and the $i\epsilon$ lies in the propagator's pole prescription.

## Periodicity and the Parity Reading

Two further standard features of the $\theta$ vacuum are worth stating in the framework's terms, one exactly and one as a reading.

**Periodicity.** The phase is periodic, $e^{i(\theta+2\pi)Q}=e^{i\theta Q}$ for integer $Q$, so the physical parameter space is a circle of circumference $2\pi$ and only $e^{i\theta}$ (and, with fermions, more refined combinations) is physical. In the framework this is the statement that the phase is an element of the central circle $\mathbb{C}_{\mathbb{B}}$'s unit subgroup, and that the circle has the period of the central imaginary; there is nothing further to derive, because the periodicity is the periodicity of $e^{i\cdot}$. The one refinement worth recording is that with a chiral fermion whose determinant also carries a phase, the physically invariant combination is $\bar\theta=\theta+\arg\det M$, the sum of the gauge angle and the fermion determinant's phase; the framework's division of labour makes the origin of the second term explicit, since it is the determinant phase of the previous section.

**The parity reading.** The topological density is parity- and time-reversal-odd, and the framework's real structure $\flat=-\dagger$ has the shape of a charge-conjugation pairing: it acts by a sign on the two sectors and its fixed space is the material sector. Reading the topological density through $\flat$, one finds that the density's behaviour under the conjugation is the framework's expression of its parity character: a P-odd, C-even object is one that acquires the sector sign under $\flat$ without a complex conjugation of the coefficients. This is a **reading** and not a derivation; the parity properties of $F\tilde F$ are the standard ones, and the framework's real structure is a repackaging of them into the algebra's two sectors. It is recorded because it is the only place in the article where the sectors enter, and because a reader should not mistake the reading for a claim that the framework derives the $\theta$ term's parity.

**The anomaly and the angle.** The two effects of this pair of articles are now separated cleanly. The **trace anomaly** is the failure of conformal invariance: a scalar coefficient multiplying curvature invariants, produced by any operator, central or not, and read from the modulus of the determinant. The **$\theta$ angle** is the phase of the determinant of a non-central operator, produced only when the operator mixes chiralities, and read from the determinant's argument. The determinant article's central/non-central distinction is exactly the line between them, and it is the reason this article has no non-central operator in its central-phase section: the $\theta$ vacuum's weighting is central, while the determinant whose phase *defines* $\theta$ is not.

## The Index, the Eta Invariant, and the Central Integer

The topological charge and the determinant's phase meet in the index theory of the Dirac operator, and the framework's statement is an exact one about the center.

**The charge as an index.** The topological charge is the index of a Dirac operator,
$$
Q = \mathrm{ind}\,\mathcal{D}_+ = \dim\ker\mathcal{D}_+-\dim\ker\mathcal{D}_- ,
$$
computed by the Atiyah–Singer theorem as $\frac{1}{8\pi^2}\int\mathrm{tr}(F\wedge F)$, the second Chern number, on a four-dimensional manifold without boundary; since $\mathrm{tr}(F\wedge F)=\tfrac12\,\mathrm{tr}(F_{\mu\nu}\tilde F^{\mu\nu})\,d^4x$, this is the same number as the previous section's $\frac{1}{16\pi^2}\int d^4x\,\mathrm{tr}(F\tilde F)$. Read in the framework, this says that the *sector label* $Q$ is a **central integer** — an element of $\mathbb{Z}e_0$ — and together with the previous section's result that the weighting $e^{i\theta Q}$ is a **central phase**, the two ingredients of the $\theta$ vacuum both lie in the center:
$$
Q\in\mathbb{Z}\,e_0\subset\mathbb{C}_{\mathbb{B}} ,
\qquad
e^{\,i\theta Q}\in U(1)\subset\mathbb{C}_{\mathbb{B}} .
$$
The topological sector label and its weight are central; only the states $|Q\rangle$ are not. This is a clean and exact framework statement, and it is the sharpest form of the article's general point that the $\theta$ vacuum's data live in the center.

**The eta invariant.** On a manifold with boundary the index acquires a boundary correction, and the relevant object is the **eta invariant**
$$
\eta(\mathcal{D}) = \lim_{s\to0^+}\sum_n \frac{\mathrm{sign}(\lambda_n)}{|\lambda_n|^s},
$$
the spectral asymmetry of the Dirac operator, which appears in the Atiyah–Patodi–Singer index theorem for the boundary problem. The eta invariant is the phase of the determinant of the operator family — the object of the previous section — and the $\theta$ angle is the coefficient of that phase. The framework's reading is therefore that the topological charge is the **interior, integer** half of the same information and the eta invariant is the **phase** half: one is the index, the other the argument of the determinant, and the $\theta$ angle couples them.

**Spectral flow counts the charge.** For a family $\mathcal{D}(s)$ interpolating between two configurations, the net number of eigenvalues crossing zero, counted with sign, is the **spectral flow**, and it equals the difference of the charges,
$$
\Delta Q = \mathrm{SF}\big(\mathcal{D}(s)\big).
$$
This is why a crossing of the family's determinant contributes a factor $-1$: each crossing adds $\pm1$ to the index and flips the sign of the determinant. The toy family of the previous section, whose determinant changes sign exactly once between $\mu=0$ and $\mu=2$ at $\lambda=1$, therefore exhibits one unit of spectral flow, and this is the correspondence in miniature between the central integer and the determinant's phase. Both facts were verified by explicit evaluation of $\det\mathcal{D}(\mu)=-\lambda^2+\mu^2$ at $\mu=0,2$.

## The Partition Function and the Topological Susceptibility

The $\theta$ vacuum's consequences are read from the partition function, and the framework's sector structure fixes its form.

**The $\theta$-dependent partition function.** Writing $Z_Q$ for the partition function in the sector of charge $Q$, the $\theta$-dependent partition function is the weighted sum
$$
Z(\theta) = \sum_{Q\in\mathbb{Z}} e^{\,i\theta Q}\,Z_Q ,
$$
a periodic function of $\theta$ with period $2\pi$, whose sectors are the same objects the $\theta$ vacuum superposes. In the framework, each $Z_Q$ is computed by the functional integral of *The Functional Integral in Biquaternionic Form* restricted to the sector, with the determinant of *The Functional Determinant in Biquaternionic Form* supplying the one-loop factor; the sector structure factorises in the way those articles describe, so $Z_Q$ is a central factor times a module factor, and the $\theta$ dependence enters only through the central phase. The consequence is worth recording: the $\theta$ dependence of the partition function is carried entirely by the center, and the module's contribution is $\theta$-independent.

**The topological susceptibility.** The physical measure of the $\theta$ dependence is the topological susceptibility,
$$
\chi = \frac{1}{V}\frac{\partial^2}{\partial\theta^2}\log Z(\theta)\bigg|_{\theta=0} ,
$$
which is (minus) the second cumulant of the charge per unit volume. Because the $\theta$ dependence sits in the phase alone, only the magnitudes $|Z_Q|$ — the sector distribution — contribute to $\chi$ at $\theta=0$: expanding the logarithm, the linear terms cancel by the sum's reality and the quadratic term is the variance of $Q$ in the distribution $|Z_Q|$. **Checked numerically** on a Gaussian model of the sector distribution, $|Z_Q|\propto e^{-Q^2/(2\sigma^2)}$ with $\sigma=2$: the finite-difference second derivative of $\log Z(\theta)$ at $\theta=0$ equals $-4.000000\ldots$, i.e. $-\sigma^2$, and the variance computed directly from the weights gives $4.000000\ldots$, so the second derivative is exactly minus that variance. The susceptibility therefore measures the width of the sector distribution and not the phases, which is the framework's $\theta$-independence of the module made quantitative.

**The $\theta$ term in the effective action.** Equivalently, the effective action acquires the term
$$
\Gamma_\theta = -i\log Z(\theta) \supset \frac{\theta^2}{2}\,\chi\,V
$$
at small $\theta$, so that a nonzero $\chi$ is what makes $\theta$ a physical parameter with observable consequences. This is standard and is the quantity that enters, for instance, the mass of the would-be Goldstone boson of the axial symmetry in the presence of the anomaly; that application belongs to the particle-physics category and is not pursued here.

## What Is Established and What Is Interpretation

**Established (framework and algebra).**

- The $\theta$ weighting is a **central unitary** element, $e^{i\theta Q}e_0\in\mathbb{C}_{\mathbb{B}}$, commuting with every element of $\mathbb{B}$, with every Lorentz rotor, with the module structure, and with the sector split; verified on explicit matrices ($\mathbb{Z}_4$ basis, $2\times2$ images).
- The central scalars are the center of $\mathbb{B}$ and are the framework's canonical circle; the $\theta$ parameter's value space is that circle, and the periodicity $\theta\sim\theta+2\pi$ is the circle's period.
- The $\theta$ vacuum does not require a non-central operator; its weighting is central and is therefore invisible to the sector structure.
- A determinant has a phase only for a **non-central** operator. Verified on the two-by-two families: $\det\mathcal{D}(\lambda)=-\lambda^2-m^2$ is negative real for real $\lambda$ away from the crossings (phase $\pi$: $-0.74$, $-4.49$, $-25.49$ at $\lambda=0.5,2,5$ with $m=0.7$); $\det\mathcal{C}(\lambda)=\lambda^2$ is positive real (phase $0$); and the phase jumps across a degeneracy, $\det\mathcal{D}(\mu)=-\lambda^2+\mu^2$ vanishing at $\mu=\lambda=1$ with the phase changing from $\pi$ to $0$.
- The topological charge is a **central integer**, $Q\in\mathbb{Z}e_0\subset\mathbb{C}_{\mathbb{B}}$, and the weighting is a **central phase**; both ingredients of the $\theta$ vacuum therefore lie in the center, and only the states $|Q\rangle$ do not.
- The determinant's sign flips once per crossing of the family; the toy family's $\det\mathcal{D}(\mu)=-\lambda^2+\mu^2$ changes sign exactly once between $\mu=0$ and $\mu=2$ (from $-1$ to $+3$ at $\lambda=1$), one unit of spectral flow consistent with $Q=1$.
- The $\theta$ term's integral is an integer (the topological charge), the abelian density is the invariant $I_2=\mathbf{E}\cdot\mathbf{B}=\mathrm{Sc}(\tilde F\star\tilde F)$, and $\star^2=-1$; all inherited from the instanton article.

**Standard, and transcribed.**

- The construction of the $\theta$ vacuum, the implementation of the large gauge transformation by a phase, and the $\theta$-term's status as a total derivative.
- The topological charge's integrality, the one-instanton value $Q=1$, and the second Chern number.
- The periodicity of $\theta$, the invariant combination $\bar\theta=\theta+\arg\det M$, the strong-CP problem, and the axion as a relaxation mechanism.
- The eta invariant and the phase of a determinant family; the parity and time-reversal properties of $F\tilde F$.
- The index theorem $\mathrm{ind}\,\mathcal{D}_+=\frac{1}{8\pi^2}\int\mathrm{tr}(F\wedge F)$, equivalently $\frac{1}{16\pi^2}\int d^4x\,\mathrm{tr}(F_{\mu\nu}\tilde F^{\mu\nu})$; the Atiyah–Patodi–Singer boundary correction and the eta invariant; spectral flow as the charge difference.
- The $\theta$-dependent partition function $Z(\theta)=\sum_Q e^{i\theta Q}Z_Q$; the topological susceptibility $\chi$ and the small-$\theta$ effective action; the role of $\chi$ in the axial-symmetry Goldstone mass.

**Interpretation.**

- Reading the topological density's parity through the real structure $\flat$ is a repackaging of the standard parity properties, not a derivation.
- Treating the $\theta$ angle as the phase reading of the determinant and the trace anomaly as its modulus reading is the organising claim of this pair of articles; the two readings are standard, their pairing here is the framework's presentation.

**Open.**

- Whether the framework has any statement about the *value* of $\theta$, beyond housing it in the center, is not addressed; the framework fixes the value space and not the value, exactly as it fixes the algebra and not the temperature.
- Whether a genuinely biquaternion-valued gauge configuration (as opposed to a gauge field written with biquaternion notation) produces a $\theta$ dependence with a framework-specific structure is not addressed; the instanton article's configurations are the standard ones.
- The construction of the large-gauge-transformation operator on the Fock module, and the precise sense in which it is implemented by the central phase, is left to the Fock and gauge-field articles.

## Summary

The $\theta$ vacuum in biquaternionic form is the standard superposition of topological sectors with the framework's value space for the angle. The topological term is
$$
S_\theta = \frac{\theta}{16\pi^2}\int d^4x\;\mathrm{tr}\big(F_{\mu\nu}\tilde F^{\mu\nu}\big) = \theta\,Q ,
\qquad Q\in\mathbb{Z},
$$
its abelian density is $\mathrm{Sc}(\tilde F\star\tilde F)=I_2=\mathbf{E}\cdot\mathbf{B}$, and the dual obeys $\star^2=-1$; the instanton article supplies the configurations and the integrality, inherited here. The vacuum is $|\theta\rangle=\sum_Q e^{i\theta Q}|Q\rangle$, and the weighting $e^{i\theta Q}e_0$ is a **central unitary** of $\mathbb{C}_{\mathbb{B}}$, commuting with every quaternion unit, every Lorentz rotor, every module component, and both sectors. The framework therefore supplies the angle's value space — its center — and shows that the $\theta$ vacuum does not disturb the sector structure. The angle is the **phase** of a determinant, and a determinant has a phase only for a **non-central** operator, as the toy families $\mathcal{D}(\lambda)$ (phase $\pi$) and $\mathcal{C}(\lambda)$ (phase $0$) exhibit; the trace anomaly of the previous article is the modulus reading of the same object. The topology, the integrality, the periodicity, the strong-CP problem, and the eta invariant are standard and transcribed.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra |
| $\mathbb{C}_{\mathbb{B}}=\mathrm{span}_\mathbb{R}\{e_0,ie_0\}$ | Center; the complex scalars; home of the central phase |
| $\mathbb{M}_-,\mathbb{M}_+$ | Material (anti-Hermitian) and informational (Hermitian) sectors |
| $\mathrm{Tr}(\tilde P\tilde H)=2\,\mathrm{Sc}(\tilde P\tilde H)$ | Trace pairing; $\mathrm{Tr}(e_0)=2$ |
| $Q$ | Topological charge, $\frac{1}{16\pi^2}\int d^4x\,\mathrm{tr}(F_{\mu\nu}\tilde F^{\mu\nu})\in\mathbb{Z}$; equals the second Chern number $\frac{1}{8\pi^2}\int\mathrm{tr}(F\wedge F)$ |
| $\mathrm{tr}$ | Gauge Lie-algebra trace in the fundamental representation, distinct from the framework's $\mathrm{Tr}$ |
| $\theta$ | Topological angle; $\theta\sim\theta+2\pi$; lives in the central circle |
| $S_\theta=\theta Q$ | Topological term; a total derivative |
| $\vert\theta\rangle=\sum_Q e^{i\theta Q}\vert Q\rangle$ | $\theta$ vacuum; central weighting |
| $\mathcal{F}=\tfrac12\sum_{\mu\nu}F_{\mu\nu}\bar e_\mu e_\nu$ | Non-abelian curvature in biquaternion form |
| $\star$ | Hodge dual on two-forms; $\star^2=-1$ in Lorentzian signature, $+1$ in Euclidean |
| $\flat=-\dagger$ | Real structure; sign on the sectors; charge-conjugation shape |
| $\bar\theta=\theta+\arg\det M$ | Physical angle with a chiral fermion |
| $\eta$ | Eta invariant; the phase of a determinant family |
| $\mathrm{ind}\,\mathcal{D}_+$ | Index of the Dirac operator; equals $Q$ |
| $\mathrm{SF}(\mathcal{D})$ | Spectral flow; equals a charge difference |
| $Z(\theta)=\sum_Q e^{i\theta Q}Z_Q$ | $\theta$-dependent partition function |
| $\chi_{\text{top}}=\frac{1}{V}\partial_\theta^2\log Z\vert_{\theta=0}$ | Topological susceptibility; the width of the sector distribution |

## Further Reading

- A. A. Belavin, A. M. Polyakov, A. S. Schwarz, and Yu. S. Tyupkin, "Pseudoparticle solutions of the Yang–Mills equations," *Physics Letters B* **59** (1975) 85–87, for the instanton and the topological charge.
- G. 't Hooft, "Symmetry breaking through Bell–Jackiw anomalies," *Physical Review Letters* **37** (1976) 8–11, for the $\theta$ dependence and the topological term's role.
- C. G. Callan, R. F. Dashen, and D. J. Gross, "The structure of the gauge theory vacuum," *Physics Letters B* **63** (1976) 334–340, for the $\theta$ vacuum as a superposition of winding sectors.
- R. Jackiw and C. Rebbi, "Vacuum periodicity in a Yang–Mills quantum theory," *Physical Review Letters* **37** (1976) 172–175, for vacuum periodicity and the large gauge transformation.
- S. Coleman, *Aspects of Symmetry* (Cambridge University Press, 1985), for the $\theta$ vacuum, the $\theta$ term, and the strong-CP discussion.
- R. D. Peccei and H. R. Quinn, "CP conservation in the presence of pseudoparticles," *Physical Review Letters* **38** (1977) 1440–1443, for the axion and the relaxation of $\theta$.
- M. F. Atiyah, V. K. Patodi, and I. M. Singer, "Spectral asymmetry and Riemannian geometry," *Mathematical Proceedings of the Cambridge Philosophical Society* **77** (1975) 43–69, for the eta invariant and the phase of a determinant family.
- M. Nakahara, *Geometry, Topology and Physics* (Institute of Physics, 2003), for the second Chern number, the instanton number, and the topological term.
- S. Weinberg, *The Quantum Theory of Fields*, Vol. 2 (Cambridge University Press, 1996), for the $\theta$ vacuum in the path-integral formulation and the anomaly's relation to it.
- Companion articles: *Instantons and Solitons in Biquaternionic Form*, for the configurations, the invariant $I_2$, and $\star^2=-1$; *The Functional Determinant in Biquaternionic Form*, for the central/non-central distinction and the determinant phase; *The Trace Anomaly in Biquaternionic Form*, for the modulus reading of the same determinant; *Fock Space and Creation/Annihilation Operators in Biquaternionic Form*, for the space the superposition lives in; *The S-Matrix in Biquaternionic Form*, for the sector structure of the asymptotic states; *Conventions in the Biquaternion Universe*, for the center, the trace pairing, and the real structure $\flat$.
