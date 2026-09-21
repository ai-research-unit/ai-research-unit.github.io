
# __Hamiltonian Mechanics and Biquaternions — A Historical Note__

## Introduction

This note is a companion to *A Brief History of Biquaternions in Physics*. That article followed the biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ through its discovery, its use in electromagnetism, its moment as a language for special relativity, and its return. This note asks a narrower question: **what is the historical relation between Hamilton's mechanics and the biquaternion?** The answer is uncomfortable, and it is the substance of what follows: the relation is a person, not a theory.

Three different things are at issue, from three different hands, and two of them are only partly Hamilton's.

1. **The canonical (Hamiltonian) formulation of dynamics.** Hamilton's two essays of 1834 and 1835 introduced a method of reducing dynamics to a single characteristic function. The modern symmetric "canonical equations" and the class of canonical transformations that preserve them are Jacobi's (1837); the bracket that organizes the equations was published by Poisson in 1809, a quarter of a century earlier. The modern canonical equations are a composite, not the work of one author.
2. **The real quaternions.** Hamilton's discovery of 16 October 1843, and the algebra $\mathbb{H}$ he promoted for the rest of his life.
3. **The complex quaternion, or biquaternion.** The name is Hamilton's, and it appears in his *Lectures on Quaternions* (1853); the *theory* of the algebra — its variants and its identifications with matrix and Clifford algebras — is the work of W. K. Clifford (1873) and of later authors; and its first substantial use in physics is that of Arthur Conway and Ludwik Silberstein in the 1910s. The attribution is genuinely contested, and the section below gives the sources on each side rather than choosing silently.

The quaternion programme and the vector calculus that displaced it are the subject of the parent history; the vector revolt is recalled here only where it bears on the fate of the biquaternion. The Hamiltonian side is the part this note owns.

Two qualifications belong at the start. First, this is a history, so the structure of the biquaternion algebra is cited, not rederived; the algebra is the contract of the companion articles, and the historical question is what was known, by whom, and when. Second, a historical note that supplies a clean continuity between two bodies of work is the failure mode to avoid. The temptation is real here, because the same man gave his name to both a mechanics and an algebra, and the temptation is to write that the biquaternion completes the mechanics. The record does not support it, and where I cannot establish a connection I say so.

## Hamilton's Dynamics, 1833–1835

Hamilton's two dynamical essays, *On a General Method in Dynamics* and the *Second Essay on a General Method in Dynamics*, appeared in the *Philosophical Transactions* in 1834 and 1835; the reformulation is usually dated to 1833, when the method was first put forward. The method replaced the direct integration of the equations of motion by the search for a single function — Hamilton's characteristic function, in his later dynamical work the principal function — whose partial derivatives give the momenta and the configuration. In the modern notation the equations that carry his name are

$$
\dot q_i = \frac{\partial H}{\partial p_i}, \qquad \dot p_i = -\frac{\partial H}{\partial q_i},
$$

where $H$ is the Hamiltonian and the $(q_i, p_i)$ are canonical coordinates.

It is worth being exact about how much of this is Hamilton's. The function $H$ and the symmetric pair of first-order equations are the form the subject took after **Carl Gustav Jacob Jacobi**, whose 1837 paper in Crelle's journal introduced the transformations that preserve the canonical form — the canonical transformations; Jacobi's Königsberg lectures on dynamics (1842–43), published by Clebsch in 1866 as *Vorlesungen über Dynamik*, became its standard exposition. The bracket that organizes the equations is older still: **Siméon Denis Poisson** introduced it in his 1809 treatise on mechanics. What Hamilton contributed in 1834–35 was the characteristic-function method and the optical-mechanical analogy; what a modern textbook calls "Hamilton's equations" is a composition of Hamilton, Jacobi, and Poisson, and to attribute it to Hamilton alone is already a compression. This is the first of the three things, and it is the one that survived.

Hamilton's optical work and his dynamics are two faces of one idea: the paths of light and the trajectories of particles are both extremals, and the same characteristic function serves both. The partial differential equation for the principal function is now the **Hamilton–Jacobi equation**, named for both men; the standard accounts describe it as the closest approach of classical mechanics to quantum mechanics, and the optical-mechanical analogy has been read, since the 1920s, as an anticipation of wave mechanics. That reading is a later interpretation, not a claim that Hamilton made, and it belongs to the reception of the theory rather than to the theory.

What is not in the 1834–35 papers is any quaternion. They were written a decade before the quaternions existed, so the algebra cannot have been the instrument of Hamilton's mechanics; and when the algebra did arrive, it was pursued as a separate project, not fed back into the dynamical memoirs. The two bodies of Hamilton's work do not meet in the published record.

## The Quaternions of 1843

The discovery itself needs only a paragraph here, because the parent article tells it in full. On 16 October 1843, walking along the Royal Canal in Dublin, Hamilton saw how to multiply quadruples rather than triples, and carved the rules into Broom Bridge:

$$
i^2 = j^2 = k^2 = ijk = -1.
$$

Olinde Rodrigues had published formulas equivalent in substance to quaternion multiplication in 1840, without the algebra. Hamilton named the quadruple a **quaternion**, expounded it in the *Lectures on Quaternions* (1853), and left the *Elements of Quaternions* to appear posthumously in 1866, edited by his son William Edwin Hamilton, with a later edition by Charles Jasper Joly (1899–1901).

Two facts from this paragraph matter for the present note. First, the dates: the mechanics is 1833–35 and the quaternions are 1843. The algebra did not exist when the mechanics was made. Second, the subject: the quaternions were an algebra of space — rotations, versors, the geometry of three dimensions — and they were pursued as such. The quaternion treatises are not treatises on mechanics, and there is no quaternion reformulation of Hamilton's equations in them.

## The Complex Quaternion: Name, Theory, and Use Are Three Different Things

The word "biquaternion" is traditionally credited to Hamilton. The standard modern reference dates the ordinary biquaternions to 1844 and cites the *Lectures on Quaternions* (1853), where a quaternion with complex coefficients is written down and where Hamilton fixes the letter $h$ for the scalar square root of $-1$, to keep it apart from the quaternion unit $i$ — the convention that Arthur Conway would also use. On this account the word, and the first definition, are Hamilton's, and the parent history says so.

But the word is not the theory, and the theory is not Hamilton's. The biquaternion **algebra**, studied as an algebra — with its split and dual variants and its identification with matrix and Clifford algebras — is the work of **William Kingdon Clifford**, whose *Preliminary Sketch of Biquaternions* appeared in the *Proceedings of the London Mathematical Society* (vol. s1-4, pp. 381–395; the volume is dated variously 1871 and 1873). The *Encyclopædia Britannica* entry on Clifford credits him with having "developed the theory of biquaternions (a generalization of ... Hamilton's theory of quaternions)"; a study of Clifford's mathematics (Open University research archive, ORO 8455, chapter 4) states that the *idea* of the biquaternion as presented in Clifford's three papers originated with Clifford, "although the term 'biquaternion' had been used earlier by Hamilton." Clifford also proposed the split and dual variants that the modern convention distinguishes.

There are, then, two defensible statements and one indefensible one. It is defensible to say that Hamilton named the complex quaternion and treated it in 1853. It is defensible to say that the biquaternion as a *theory* is Clifford's. It is **not** defensible to say that "the biquaternion is Hamilton's" without qualification, as though the algebra, its group structure, and its physical use were all his. The parent history's sentence that the word and the surrounding vocabulary are Hamilton's is right about the words; the algebra those words came to denote is a later construction. The record is contested at the join, and this note leaves the contest visible rather than smoothing it.

The third hand is the physics. The biquaternion's first substantial physical use is neither Hamiltonian nor Hamilton's. It is the formulation of special relativity by **Arthur W. Conway** — an article of 1911, a priority claim against Silberstein in 1912, a 43-page tract *Relativity* in 1915 — and by **Ludwik Silberstein**, whose *Quaternionic form of relativity* appeared in the *Philosophical Magazine* in 1912, with a second memoir in 1913 and *The Theory of Relativity* in 1914; Silberstein's 1907 bivector paper and Cornelius Lanczos's 1929 reformulation of the Dirac equation stand at the two ends of the same line. That is the biquaternion's documented road into physics — relativity and the spinor algebra — and it is not the road of canonical mechanics.

## Did the Quaternion School Write Mechanics?

The question is worth asking directly, because the shared name invites the assumption that it did. The answer from the record is: scarcely at all.

The mechanical tradition of the nineteenth century was analytic. Lagrange, Poisson, Hamilton, and Jacobi wrote mechanics with real scalars and with the calculus of variations; the generalized coordinates and momenta are real, and no hypercomplex algebra appears. The quaternion tradition was geometric and, after Maxwell, electromagnetic. Hamilton's own quaternion work is the geometry of versors; Tait's books are the quaternion calculus; the applied literature of the school — Macfarlane's "Algebra of Physics," or Space Analysis, is its most systematic attempt — was directed at physical geometry and electromagnetism rather than at the canonical equations. I found no documented programme, in the school or after it, to write Hamilton's equations in quaternions. That is a negative claim, and it is offered as one, on the evidence of the standard history (Crowe) and of the treatises cited below.

There are, however, two *structural* bridges, and they are real. Both are facts of the modern algebra, not events in the history; the distinction is the point, and both are worked out in the companion articles rather than here.

The first is angular momentum. The components of $\mathbf{L} = \mathbf{r}\times\mathbf{p}$ close, under the canonical bracket, on the same $\mathfrak{so}(3)$ that the quaternion units span under commutation. The Poisson bracket of 1809 and the quaternion commutator of 1843 are the same Lie algebra, and what joins them is a modern recognition rather than a historical derivation; the correspondence is developed in *Similitudes Between the Poisson Bracket and the Quantum Commutator*, and the spin realization in *Angular Momentum and Spin in Biquaternionic Form*.

The second bridge is the single degree of freedom. The canonical, or symplectic, algebra of one phase plane is $\mathfrak{sp}(2,\mathbb{R})$, of real dimension $3$, and it is isomorphic to $\mathfrak{sl}(2,\mathbb{R})$ — the corpus records $Sp(2,\mathbb{R}) \cong SL_2(\mathbb{R})$ — which sits inside the six-real-dimensional $\mathfrak{sl}(2,\mathbb{C})$, itself inside $\mathbb{B}$. The biquaternion algebra can therefore carry the canonical structure of **one** phase plane; this is the sense in which a Hamiltonian flow is a biquaternionic rotation, and it is the exact island mapped in *Similitudes Between Biquaternion Rotors and Hamiltonian Flow* and in the harmonic-oscillator article's $Sp(2,\mathbb{R}) \cong SU(1,1)$ reading of the squeezes. The bridge does not extend. The real symplectic algebra $\mathfrak{sp}(2n,\mathbb{R})$ has dimension $n(2n+1)$: for $n = 1$ that is $3$, but for $n = 2$ it is already $10$, greater than the eight real dimensions of $\mathbb{B}$, and it grows from there. There is no room in the biquaternion algebra for the canonical structure of a general mechanical system, and this is an algebraic reason — independent of any historical accident — why a "biquaternion Hamiltonian mechanics" was never a natural programme and is still not one.

## Why the Quaternions Lost to the Vector Calculus

Hamilton's death in 1865 left the quaternions without their author but not without advocates. Peter Guthrie Tait, Maxwell's friend and the leading quaternionist after Hamilton, published an *Elementary Treatise on Quaternions* in 1867 — written with Hamilton's advice, though published after his death — and an *Introduction to Quaternions* with Philip Kelland in 1873. Maxwell's *Treatise on Electricity and Magnetism* (1873) used quaternion notation for some of its vector operations, and in the following decades topics now written with vectors, among them kinematics in space and Maxwell's equations, were described entirely in quaternion terms; quaternions were a required examination subject in Dublin. The school organized: the Quaternion Association was formed in 1896, at Alexander Macfarlane's prompting, with Macfarlane as its secretary, later its president (1909), and editor of its *Bibliography of Quaternions* (1904).

The displacement came from the mid-1880s, from vector analysis developed independently by Josiah Willard Gibbs, Oliver Heaviside, and Hermann von Helmholtz. Gibbs's lecture notes were privately printed in 1881 and 1884 and became, through Edwin Bidwell Wilson, the textbook *Vector Analysis* (1901); Heaviside's *Electromagnetic Theory* (1893) taught the field in vector form; and in the early 1890s Gibbs and Tait conducted a controversy in the pages of *Nature*. The vector calculus won for reasons that were notational and practical rather than algebraic: it separated the dot and cross products instead of carrying the full quaternion product, and the notation was correspondingly cleaner and better suited to electrical engineering and the emerging field theories. Crowe's *A History of Vector Analysis* (1967) is the standard account. Hamilton's own writing did not help his case: the standard reference observes that the transition left his work difficult for modern readers, because his definitions were unfamiliar and his prose was difficult to follow.

The scope of this quarrel matters here. It was a quarrel about the **real** quaternions and their vector part. The biquaternions played essentially no part in it; their appearance in physics was about relativity and came later. The quaternion programme lost the notation of mechanics and of field theory, and the algebra that lost was not the complexified one.

## The Biquaternion's Own Road: Relativity, Not Mechanics

The biquaternion's history in physics is the parent article's subject, and only its relation to mechanics is in question here. That relation is negative. When the complexified algebra finally entered physics in earnest, it was as the algebra of the Lorentz group: the unit-norm biquaternions are $SL(2,\mathbb{C})$, and they act on the material subspace $\mathbb{M}_-$ by the rotor conjugation

$$
\tilde{X} \;\longmapsto\; \tilde{\Lambda}\,\tilde{X}\,\tilde{\Lambda}^{\dagger},
$$

preserving the norm form $N(\tilde{X}) = \tilde{X}\bar{\tilde{X}}$. The physical works were Conway's and Silberstein's relativity, followed by Lanczos's 1929 reformulation of the Dirac equation and, later, by the quaternionic-quantum-mechanics, geometric-algebra, and twistor traditions. None of these is a reformulation of Hamilton's canonical mechanics; all of them rewrite theories that the canonical mechanics had to be generalized to accommodate.

One late title may mislead a reader and is mentioned so that it does not. Lanczos's 1933 paper *Die Wellenmechanik als Hamiltonsche Dynamik des Funktionenraumes* — "Wave mechanics as Hamiltonian dynamics of function space" — presents wave mechanics as Hamiltonian dynamics and offers a new derivation of the Dirac equation; on its title it belongs to the Hamiltonian line and not to the biquaternion one, and I did not read it for this note.

## What the History Shows and What It Does Not Show

The record shows the following. The canonical formulation of mechanics is a composite — Poisson's bracket (1809), Hamilton's characteristic function (1834–35), Jacobi's canonical transformations (1837) — and is not the work of any one of them. The real quaternions are Hamilton's (1843) and were displaced from the mid-1880s by the vector calculus of Gibbs and Heaviside. The complex quaternion is a third thing: the name is Hamilton's (1853), the theory is Clifford's (1873) and later authors', and the physics is Conway's and Silberstein's (1910s). The biquaternion's physical home is relativity and the spinor algebra, not canonical mechanics.

The record does not show any documented transfer between Hamiltonian mechanics and the biquaternion, in either direction. It does not contain a historical "biquaternion Hamiltonian formulation." The parent article's open question — that the biquaternion form of the relativistic Hamiltonian and the associated Hamilton equations have not been developed — is a statement about this corpus's programme, and the history agrees with it: the record does not contain such a formulation either. The two structural bridges found above, the angular-momentum algebra $\mathfrak{so}(3)$ and the one-degree-of-freedom algebra $\mathfrak{sp}(2,\mathbb{R}) \cong \mathfrak{sl}(2,\mathbb{R})$, are modern and partial; they show that the algebra can carry a piece of the canonical structure, not that the canonical structure is biquaternionic.

A clean narrative — Hamilton's mechanics, completed by Hamilton's algebra, lost only through the poor taste of the vectorists — is therefore not available. The mechanics was made a decade before the algebra. The algebra that was complexified was mostly Clifford's and its physics was Conway's and Silberstein's. And the symplectic structure of a general mechanical system has no room inside the biquaternions at all. The honest content of the history is the separation of the three things that the name conceals.

## Sources

- W. R. Hamilton, "On a General Method in Dynamics," *Philosophical Transactions of the Royal Society* (1834); "Second Essay on a General Method in Dynamics," ibid. (1835).
- S. D. Poisson, "Sur la variation des constantes arbitraires dans les questions de mécanique," *Journal de l'École Polytechnique* (1809), for the bracket.
- C. G. J. Jacobi, "Ueber die Reduction der Integration der partiellen Differentialgleichungen erster Ordnung zwischen irgend einer Zahl Variabeln," *Journal für die reine und angewandte Mathematik* **17** (1837) 97–162, DOI 10.1515/crll.1837.17.97, for the canonical transformations; *Vorlesungen über Dynamik*, ed. A. Clebsch (1866).
- W. K. Clifford, "Preliminary Sketch of Biquaternions," *Proceedings of the London Mathematical Society* **s1-4** (dated variously 1871 and 1873) 381–395, DOI 10.1112/plms/s1-4.1.381.
- P. G. Tait, *An Elementary Treatise on Quaternions* (1867); P. G. Tait and P. Kelland, *Introduction to Quaternions* (1873).
- J. C. Maxwell, *A Treatise on Electricity and Magnetism* (1873).
- J. W. Gibbs, privately printed lecture notes on vector analysis (1881, 1884); E. B. Wilson, *Vector Analysis* (1901); O. Heaviside, *Electromagnetic Theory* (1893).
- A. Macfarlane, *Bibliography of Quaternions* (Quaternion Association, 1904).
- M. J. Crowe, *A History of Vector Analysis* (University of Notre Dame Press, 1967).
- L. Silberstein, "Elektromagnetische Grundgleichungen in bivektorieller Behandlung," *Annalen der Physik* **327** (1907) 579–586; "Quaternionic form of relativity," *Philosophical Magazine* **23** (1912) 790–809; "Second memoir on quaternionic relativity," *Philosophical Magazine* **25** (1913) 135–144; *The Theory of Relativity* (Macmillan, 1914).
- A. W. Conway, *Relativity* (Edinburgh tract, 1915), and his priority claim of 1912, recorded in G. Temple, *100 Years of Mathematics*.
- C. Lanczos, "Die tensoranalytischen Beziehungen der Diracschen Gleichung," *Zeitschrift für Physik* **57** (1929) 447–473; "Die Wellenmechanik als Hamiltonsche Dynamik des Funktionenraumes," *Zeitschrift für Physik* **81** (1933) 703–732.
- For the contested attribution of the biquaternion and the frame of the vector revolt: *Encyclopædia Britannica*, "William Kingdon Clifford"; Open University research archive, ORO 8455, chapter 4 (Clifford's biquaternions); and the standard reference articles "Biquaternion" and "History of quaternions," which date the ordinary biquaternions to Hamilton in 1844 and cite his *Lectures on Quaternions* (1853), pp. 639 and 730.

## Summary

Hamilton's canonical mechanics and the biquaternion algebra share a name and nothing else that the record records. The mechanics is a composite: Poisson's bracket (1809), Hamilton's characteristic function (1834–35), and Jacobi's canonical form of the equations (1837). The real quaternions are Hamilton's (1843), and they lost the notation of mechanics and of field theory to the vector calculus of Gibbs and Heaviside from the mid-1880s. The complex quaternion is a third thing from a fourth decade: named by Hamilton in 1853, theorized by Clifford in 1873, and first put to physics by Conway and Silberstein in the 1910s, where its subject was relativity, not mechanics.

The biquaternion algebra contains the Lorentz group as the unit-norm elements $SL(2,\mathbb{C})$ acting on $\mathbb{M}_-$ by rotor conjugation, and it contains two pieces of canonical structure: the angular-momentum algebra $\mathfrak{so}(3)$, shared with the Poisson bracket, and the one-degree-of-freedom symplectic algebra $\mathfrak{sp}(2,\mathbb{R}) \cong \mathfrak{sl}(2,\mathbb{R})$. Neither is a historical transfer, and the second does not extend past one degree of freedom, because $\mathfrak{sp}(2n,\mathbb{R})$ outgrows the eight real dimensions of $\mathbb{B}$ as soon as $n \geq 2$.

The history does not support a biquaternionic completion of Hamilton's mechanics. It supports the separation of the three things his name conceals: a composite analytical mechanics, a real algebra of space that lost a notation war, and a complexified algebra whose home turned out to be spacetime.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra (complex quaternions) |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$; commutator $[e_i,e_j] = 2\sum_k \epsilon_{ijk} e_k$ |
| $i$ | Scalar imaginary, $i^2 = -1$ (Hamilton's $h$) |
| $\bar{\cdot}, {}^{\dagger}$ | Quaternion and Hermitian conjugations |
| $\mathbb{C}_{\mathbb{B}}, \mathbb{H}_{\mathbb{B}}$ | Complex subspace (center) and real quaternion subspace |
| $\mathbb{M}_{-}$ | Anti-Hermitian subspace (material sector): imaginary scalar, real vector |
| $\mathbb{M}_{+}$ | Hermitian subspace (informational sector; qubit operator algebra) |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2$ | Norm form (zero divisors where $N = 0$) |
| $SL(2,\mathbb{C}) = \{\tilde{\Lambda} : \tilde{\Lambda}\bar{\tilde{\Lambda}} = e_0\}$ | Unit-norm-form biquaternions; Lorentz double cover |
| $\tilde{X} \mapsto \tilde{\Lambda}\tilde{X}\tilde{\Lambda}^{\dagger}$ | Rotor conjugation on $\mathbb{M}_{-}$ |
| $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | Trace formula (Born rule), inherited from the companion articles |
| $q_i, p_i$; $\{f,g\}$ | Canonical coordinates and the Poisson bracket (Poisson 1809) |
| $H$; $\dot q_i = \partial H/\partial p_i$, $\dot p_i = -\partial H/\partial q_i$ | The Hamiltonian and the canonical equations (Hamilton 1834–35; Jacobi 1837) |
| $\mathfrak{so}(3)$; $\mathfrak{sp}(2,\mathbb{R}) \cong \mathfrak{sl}(2,\mathbb{R})$ | Angular-momentum algebra; one-degree-of-freedom symplectic algebra |

## Further Reading

- *Introduction to the Biquaternion Universe* — the framework and the notation contract.
- *$\mathbb{M}_-$ as the Material Space* — the material sector and the four-vectors.
- *$\mathbb{M}_+$ as the Informational Space* — the operator algebra and the Born-rule trace formula.
- *A Brief History of Biquaternions in Physics* — the parent history, whose biquaternion-in-relativity thread this note does not repeat.
- *Biquaternion Exponential and Lie Group Structure* — $\mathfrak{sl}(2,\mathbb{C})$, $SL(2,\mathbb{C})$, and rotor conjugation.
- *Relativistic Mechanics in Biquaternionic Form* — its open question on the biquaternion Hamiltonian is the starting point of this note.
- *Quaternion Algebra* — the real quaternion algebra and its basis.
- *Biquaternion Algebra* — the algebra and its four conjugations.
- *Clifford Algebras* — the identifications $\mathbb{B} \cong Cl_{3,0}(\mathbb{R})$ and the even subalgebra of $Cl_{1,3}$.
- *Lie Groups* — the symplectic groups, their dimensions, and $Sp(2,\mathbb{R}) \cong SL_2(\mathbb{R})$.
- *The Harmonic Oscillator in Biquaternionic Form* — the one-mode $Sp(2,\mathbb{R}) \cong SU(1,1)$ bridge between phase plane and boost.
- *Angular Momentum and Spin in Biquaternionic Form* — the angular-momentum algebra realized in the biquaternions.
- *Similitudes Between the Poisson Bracket and the Quantum Commutator* — the $\mathfrak{so}(3)$/$\mathfrak{su}(2)$ correspondence in full.
- *Similitudes Between Biquaternion Rotors and Hamiltonian Flow* — the rotor–flow correspondence, its exact island, and where it breaks.

