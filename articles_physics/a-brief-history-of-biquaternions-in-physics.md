# __A Brief History of Biquaternions in Physics__

## Introduction

The biquaternion algebra $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ is the complexification of Hamilton's quaternions. In its complexified form it is older than the special theory of relativity and older by three quarters of a century than the quantum mechanics of spin; it is also the algebra in which the Pauli matrices, the two-component spinors, and the double cover of the Lorentz group are written. This article is a history of how $\mathbb{B}$ entered physics: how it was found, how it was used in electromagnetism, how it was published as a language for relativity and then displaced by vectors and tensors, and how it returned in the middle of the twentieth century.

Two qualifications belong at the start.

The first is scope. Most nineteenth-century physics that used "quaternions" used the **real** quaternions $\mathbb{H}$, not the biquaternions. The quaternion formulation of Maxwell's equations, the quaternionists' campaign, and the vector revolt all concern real quaternions and their vector parts. The **biquaternion** thread is narrower: it is the complexified algebra, and its principal physical use before 1950 is the formulation of special relativity by Conway and Silberstein. This article follows that narrower thread, keeping the real-quaternion context in view because the thread cannot be understood without it. A history that silently substituted the real quaternions for the biquaternions would be signing for more than the record contains.

The second is what a history can show. The algebra $\mathbb{B}$ *contains* $M_2(\mathbb{C})$, and therefore contains, as a matter of algebra, the objects that quantum mechanics later used. That is a structural fact. It is not the same as a historical fact — that anyone *intended* a quantum-mechanical application, or was on the verge of one. The word "near-miss" that this subject attracts is a retrospective description; where it is used below it is marked as such. Dates and attributions follow the standard references, and the few items that could not be pinned down are flagged in the text and recorded in the companion note.

## Hamilton's Quaternions and Their Complexification

William Rowan Hamilton discovered the quaternions on 16 October 1843, while walking along the Royal Canal in Dublin. The multiplication rules he carved into Broom Bridge (then Brougham Bridge) were

$$
i^2 = j^2 = k^2 = ijk = -1 .
$$

These are Hamilton's own letters: here $i, j, k$ are the three quaternion units. The article's notation, in which those units are written $e_1, e_2, e_3$ and $i$ denotes the scalar imaginary, is set out below.

Hamilton had spent years trying to multiply triples of numbers to represent points in space; the breakthrough was to give up triples for quadruples. He named the quadruple a **quaternion** and spent the rest of his life on it. The *Lectures on Quaternions* (1853) is the comprehensive treatise; the *Elements of Quaternions* appeared posthumously in 1866, edited by his son William Edwin Hamilton, with a later edition by Charles Jasper Joly (1899–1901). Olinde Rodrigues had published formulas equivalent in substance to quaternion multiplication in the composition of rotations in 1840, without the algebra; the composition law is accordingly shared, while the algebra is Hamilton's.

**Why the coefficients had to become complex.** Hamilton was studying the quaternion algebra and wanted to **solve equations** with it, and when he worked through the cases by degree he found that the algebra stops short.

- **Linear equations**: solved, and within $\mathbb{H}$ itself. If $ax = b$ with $a \neq 0$, then $x = a^{-1}b$, and if $xa = b$ then $x = ba^{-1}$, each unique. The side on which $a$ stands matters — $e_1^{-1}e_2 = -e_3$ while $e_2e_1^{-1} = +e_3$ — but every nonzero quaternion is invertible, so a linear equation asked on a definite side always has its answer in $\mathbb{H}$.
- **Quadratic equations**: no longer routine. There is no quadratic formula, and the solutions, when they are found, **sometimes require complex coefficients** — that is, complex quaternions rather than quaternions.
- **Higher degree**: worse. The root sets cease to be finite. The cubic $x^{3} = 1$ has the root $1$ and a whole sphere of further roots $x = -\tfrac{1}{2} + \tfrac{\sqrt{3}}{2}\mathbf{u}$, one for each unit pure quaternion $\mathbf{u}$, so a degree-$n$ equation over $\mathbb{H}$ cannot be reduced to $n$ linear factors.

The quadratic case fails at the first step of the classroom method. Completing the square requires

$$
\left(x + \frac{b}{2}\right)^{2} = x^{2} + b\,x + \frac{1}{2}\left(bx - xb\right) + \frac{b^{2}}{4},
$$

and the linear term disappears only if $x$ commutes with $b$, which is not the general case. With the commutator left standing there is no reduction to $y^{2} = \text{const}$, and hence no discriminant to compute with.

**A basic example.** The shortest way to see the obstruction is a quadratic with ordinary real quaternion coefficients:

$$
x^{2} + 2e_2\,x - 3 = 0 .
$$

Write $x = x_0 + x_1 e_1 + x_2 e_2 + x_3 e_3$ and separate the four components of the equation. The $e_1$- and $e_3$-components give $x_3 = -x_0 x_1$ and $x_1 = x_0 x_3$, hence $x_1 = x_3 = 0$; the $e_2$-component gives $x_0\,(x_2 + 1) = 0$, which leaves two branches.

**First branch, $x_2 = -1$.** The scalar component becomes $x_0^{2} = 2$, so $x_0 = \pm\sqrt{2}$ and

$$
x = \pm\sqrt{2} - e_2 ,
$$

two solutions in $\mathbb{H}$.

**Second branch, $x_0 = 0$.** The scalar component becomes

$$
x_2^{2} + 2x_2 + 3 = 0, \qquad \Delta = 4 - 12 = -8 < 0 ,
$$

which no real $x_2$ satisfies. The resolution is $x_2 = -1 \pm \sqrt{2}\,i$, so

$$
x = \left(-1 \pm \sqrt{2}\,i\right) e_2 ,
$$

two complex quaternions, not quaternions.

Substitution confirms all four. A quadratic with real quaternion coefficients has produced four solutions, two in $\mathbb{H}$ and two outside it — and the second branch is where the coefficients leave the algebra. It leaves because a single **scalar** equation, $x_2^{2} + 2x_2 + 3 = 0$, has a negative discriminant, and solving it calls for a scalar square root of $-1$: a number that commutes with everything, so that the ordinary algebra of equations still applies. The quaternion units are roots of $-1$ in abundance, but they are not central, and $\mathbb{H}$ contains no central root of $-1$ at all, since the only quaternions commuting with every element are the real numbers. Nothing in the reduction is repaired by a quaternion unit; the repair is to let the coefficients themselves be complex.

That the complexification is forced by this branch, rather than by a shortage of roots, is worth recording, since the point is often overstated. By the Eilenberg–Niven theorem a one-sided quaternion polynomial of positive degree always has a quaternion root, and the first branch above duly supplies two. What fails in $\mathbb{H}$ is the splitting: the quadratic has solutions galore but no factorisation into linear factors, and no scalar discriminant to separate them.

This is the precise content of the remark that the quaternions were "not enough": they are enough to solve the equation in one branch, and not enough to solve it as an equation.

The quaternions form a four-dimensional real division algebra. Making them complex produces the biquaternions: the four coefficients are allowed to be complex,

$$
\tilde{Q} = Q_0 e_0 + Q_1 e_1 + Q_2 e_2 + Q_3 e_3, \qquad Q_\mu \in \mathbb{C},
$$

with the quaternion units $e_0 = 1, e_1, e_2, e_3$ multiplying as in $\mathbb{H}$ and commuting with every complex scalar. Hamilton himself took this step and named the result: the **biquaternion** is the complex quaternion, and its fullest treatment in his own work is in the *Lectures on Quaternions* (1853). His motive was the algebraic one set out above: in the treatment of general quadratic equations with quaternion coefficients, the resolution called for complex coefficients. The word is his, and so is the surrounding vocabulary — he introduced *bivector*, *biconjugate*, *bitensor*, and *biversor* alongside it. Because the quaternion units were written $i, j, k$, Hamilton used the letter $h$ — not $i$ — for the square root of $-1$ in the coefficient field, to keep the two imaginary units apart, and Arthur W. Conway later followed the same convention. The companion articles write the quaternion units as $e_1, e_2, e_3$ and reserve $i$ for the scalar imaginary, which removes the clash that $h$ was introduced to avoid. The translation is

$$
e_0 \leftrightarrow 1, \qquad e_1 \leftrightarrow i, \qquad e_2 \leftrightarrow j, \qquad e_3 \leftrightarrow k, \qquad i \leftrightarrow h .
$$

The biquaternion algebra thus arrived with the quaternions themselves, within the first decade of their discovery. Nothing in its later physics was new algebra; what was new, repeatedly, was the recognition of where the algebra applied.

A terminological caution is necessary, because the word "biquaternion" has not been used uniformly. The modern convention distinguishes the three tensor products of $\mathbb{H}$ with the three two-dimensional commutative real algebras: the **biquaternions** $\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, the **split-biquaternions** $\mathbb{D}\otimes_\mathbb{R}\mathbb{H}$ (with $\mathbb{D}$ the split-complex numbers), and the **dual quaternions** $\mathbb{N}\otimes_\mathbb{R}\mathbb{H}$ (with $\mathbb{N}$ the dual numbers). William Kingdon Clifford, who noted that Hamilton's biquaternions were a tensor product of two known algebras, proposed the split and dual variants in his "Preliminary Sketch of Biquaternions" (*Proceedings of the London Mathematical Society*, vol. 4, pp. 381–395; the volume is dated variously 1871 and 1873). In older texts the words are not always used in this sense, and a reader meeting "biquaternion" in a nineteenth-century source should check which algebra is meant. This article follows the modern convention: the biquaternions are $\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$.

## The Algebra, in the Notation of the Companion Articles

The algebra and its subspaces are established in the companion articles and are recalled here only in the form the history needs. The notation is inherited, not redefined.

$\mathbb{B}$ is four-dimensional over $\mathbb{C}$ and eight-dimensional over $\mathbb{R}$. Its four natural conjugations have as fixed-point sets the distinguished real subspaces used throughout the corpus: the complex subspace $\mathbb{C}_{\mathbb{B}}$ (the complex scalars, the center of $\mathbb{B}$), the quaternion subspace $\mathbb{H}_{\mathbb{B}}$ (the real quaternions), the Hermitian subspace $\mathbb{M}_{+}$ (real scalar part, imaginary vector part, the informational sector), and the anti-Hermitian subspace $\mathbb{M}_{-}$ (imaginary scalar part, real vector part, the material sector). The natural quadratic form is the norm form

$$
N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_{\mu=0}^{3} Q_\mu^2 ,
$$

whose indefinite signature on $\mathbb{M}_{-}$ arises algebraically from $i^2 = -1$ in the imaginary time coefficient $ict$. The null elements $N(\tilde{Q}) = 0$, $\tilde{Q} \neq 0$, are the zero divisors; on $\mathbb{M}_{-}$ they are the light cone.

The single structural fact that organizes the whole subsequent history is the isomorphism

$$
\mathbb{B} \;\cong\; M_2(\mathbb{C}) ,
$$

realized by sending the quaternion units to $-i$ times the Pauli matrices, $e_k \mapsto -i\sigma_k$. Equivalently, $\mathbb{B}$ is the real Clifford algebra $Cl_{3,0}(\mathbb{R})$ — the **Pauli algebra** — and the even subalgebra of the spacetime algebra $Cl_{1,3}$. Under this isomorphism the norm form is the determinant, $N(\tilde{Q}) = \det\Phi(\tilde{Q})$, and the unit-norm-form elements

$$
SL(2,\mathbb{C}) = \{\tilde{\Lambda} \in \mathbb{B} : \tilde{\Lambda}\bar{\tilde{\Lambda}} = e_0\}
$$

are the double cover of the proper orthochronous Lorentz group $SO^{+}(1,3)$, acting on $\mathbb{M}_{-}$ by the rotor conjugation

$$
\tilde{X} \;\longmapsto\; \tilde{\Lambda}\,\tilde{X}\,\tilde{\Lambda}^{\dagger} .
$$

These are the facts that make the history intelligible. The algebra of Hamilton's complex quaternions *is* the algebra of the Pauli matrices; the group of unit biquaternions *is* the Lorentz double cover; the idempotents $\tilde{P}_\pm = \tfrac{1}{2}(e_0 \pm i\hat{\mu})$ in $\mathbb{M}_{+}$ are the pure states of a two-state system, with $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ as the Born rule written in the algebra (see the companion article *The Hermitian Subspace $\mathbb{M}_+$ as the Informational Sector*). None of these identifications was known to Hamilton.

## Quaternions in Electromagnetism, and the Vector Revolt

The first substantial physics to use quaternions was electromagnetism. James Clerk Maxwell's *A Treatise on Electricity and Magnetism* (1873) employed quaternion notation for some of its vector operations, and in the decades after his death the quaternion calculus became a standard language for the field: topics now written with vectors — kinematics in space and Maxwell's equations among them — were described in quaternion terms. Peter Guthrie Tait, Maxwell's friend and the leading quaternionist after Hamilton's death, published an *Elementary Treatise on Quaternions* in 1867 (written with Hamilton's advice and published after Hamilton's death) and an *Introduction to Quaternions* with Philip Kelland in 1873. The quaternion product was attractive because the dot and cross products are cut from a single operation, and the quaternion operator $\nabla$ carried gradient, divergence, and curl together.

The algebra's hold on physics did not last. From the mid-1880s, vector analysis — developed by Josiah Willard Gibbs and Oliver Heaviside — displaced the quaternions in physics and engineering. Heaviside's *Electromagnetic Theory* (1893) taught the field in vector form, and Gibbs's lectures, published as *Vector Analysis* by Edwin Bidwell Wilson (1901), gave the notation its textbook. The reasons were practical rather than algebraic: the vector calculus is notationally cleaner, it separates the dot and cross products instead of carrying the full quaternion product, and it suited the needs of electrical engineering and the emerging field theories. The transition was contested — the quaternionists, organized in a Quaternion Association (Alexander Macfarlane was its secretary from 1896, its president in 1909, and edited its *Bibliography of Quaternions* in 1904), argued the case for years — but the outcome was not close. Michael J. Crowe's *A History of Vector Analysis* (1967) is the standard account.

This part of the story concerns real quaternions and their vector parts almost entirely. The biquaternions played little role in the electromagnetic debates; their physics appearance came later and was about a different subject.

## The Biquaternion Formulation of Relativity

Special relativity is where the biquaternions came closest to becoming a standard physical language, and the closeness is structural before it is historical.

The structural fact is recorded above: the unit-norm-form biquaternions are $SL(2,\mathbb{C})$, the double cover of the Lorentz group, and they act on the four-dimensional real space $\mathbb{M}_{-}$ by rotor conjugation. A four-vector of relativistic physics is an element of $\mathbb{M}_{-}$; a Lorentz transformation is a unit biquaternion; the invariance of the interval is the invariance of the norm form under the action. The biquaternion algebra therefore contained the kinematics of special relativity as soon as the physics was written down — not because anyone looked for it there, but because the group of unit biquaternions had sat inside Hamilton's algebra since the 1840s.

The historical record then shows that this formulation was published, not merely available. Arthur W. Conway applied biquaternion algebra to special relativity, publishing an article in 1911 and in 1912 asserting priority over Ludwik Silberstein, who had independently applied biquaternions to relativity; Conway's claim was later backed by George Temple, and in 1915 Conway published a 43-page tract, *Relativity*, in Edinburgh. Silberstein's treatment appeared as "Quaternionic form of relativity" (*Philosophical Magazine* **23** (1912) 790–809), with a second memoir in 1913, and it became a textbook: *The Theory of Relativity* (Macmillan, 1914; second edition, 1924), which used biquaternions throughout. Silberstein had also introduced, in 1907, the complex three-vector $\mathbf{E} + ic\mathbf{B}$ of the electromagnetic field — now called the **Riemann–Silberstein vector**. The corpus's Maxwell article writes the same object, up to a normalisation, as $i\sqrt{\epsilon}\,\mathbf{E}-\sqrt{\mu}\,\mathbf{H}$. (The attribution of the name's "Riemann" to Bernhard Riemann I have not verified; the 1907 introduction is Silberstein's. This is flagged in the companion.)

Around the same time, Alexander Macfarlane developed his "space analysis," an adaptation of quaternions to physics; the historical record notes that his first publication on it preceded Minkowski's presentation of spacetime by seventeen years. Macfarlane's hyperbolic-quaternion program was not the biquaternion formulation, but it belongs to the same moment in which quaternion methods were being stretched toward the geometry of spacetime.

The displacement, when it came, was by Minkowski's four-dimensional tensor formulation (1908) and the four-vector calculus that grew from it. The tensor formalism was explicitly covariant, it generalized without alteration to curved spacetime, and it separated vectors, covectors, and tensors in a way the quaternion product did not. It is worth stating plainly, because "near-miss" suggests otherwise: the biquaternion relativity of Conway and Silberstein was a published, textbook-level formulation that lost a competition of notations, not a possibility that was never realized.

## The Later Recognition: Biquaternions and the Quantum Algebra

The connection of $\mathbb{B}$ to quantum mechanics is the sharpest structural fact in this history and the weakest historical one.

The structural fact is the isomorphism $\mathbb{B} \cong M_2(\mathbb{C})$: the biquaternion algebra is the algebra generated by the Pauli matrices, the algebra of operators on a two-state system. In the language of the companion articles, the Hermitian subspace $\mathbb{M}_{+}$ carries the observables, its idempotents the pure states, and the trace formula is the Born rule. Nothing in the algebra of a qubit lies outside $\mathbb{B}$.

The historical chronology, however, runs the other way, and by a wide margin. Élie Cartan introduced spinors in geometry in 1913, without physics. Wolfgang Pauli introduced the three spin matrices for the electron in 1927 ("Zur Quantenmechanik des magnetischen Elektrons," *Zeitschrift für Physik* **43** (1927) 601–623), and Paul Dirac gave the relativistic electron equation in 1928. In 1929 the Dirac equation was reformulated in tensor-analytic and covariant terms by Cornelius Lanczos ("Die tensoranalytischen Beziehungen der Diracschen Gleichung" and its companion, *Zeitschrift für Physik* **57** (1929) 447–473 and 474–483); Lanczos's doctoral dissertation (1921), *The Relation of Maxwell's Aether Equations to Functional Theory*, had already rewritten Maxwell's equations in quaternion terms and applied a relativistic variational principle to them. In the same year, Hermann Weyl and Bartel van der Waerden brought the two-component spinor into physics. The algebra these developments needed had existed since Hamilton; the developments did not derive from it, and the standard history of quantum mechanics does not run through the biquaternion literature.

Even the later quaternion work is a separate line: Conway returned to quaternions for quantum mechanics only at the end of his life, in work published in 1948 and cited in a 1950 thesis by Joachim Lambek, and the recognition that the biquaternion algebra and the Pauli algebra are the same became standard in the geometric-algebra literature of the 1960s. The honest statement is two-part: the algebra contains the quantum structures, and no one in the biquaternion tradition is documented as having used it to anticipate them. Only the second kind of connection would justify the word "anticipation."

## Why the Biquaternions Were Displaced

The biquaternions were not abandoned because the algebra failed. They were displaced by notations better suited to the practice of physics, for separable reasons.

**Vector analysis.** The vector calculus of Gibbs and Heaviside was easier to teach, easier to compute with, and adequate for the field theories of the period. It took the parts of the quaternion product that physics used — the dot and cross products — and discarded the rest, and it won on usability.

**Tensor calculus and differential geometry.** Minkowski's four-tensor formulation of relativity (1908) and the tensor calculus of Ricci and Levi-Civita made covariance manifest, distinguished vectors from covectors and one-forms, and generalized directly to the curved spacetime of general relativity. The quaternion product has no corresponding tensor apparatus; when physics moved to differential geometry, the quaternion notation had no place to stand.

**The $ict$ convention and its later abandonment.** The complex structure that the biquaternion formulation makes explicit appeared in mainstream practice as the $ict$ convention — the imaginary time coordinate that makes the Minkowski interval look Euclidean. The companion article *Why Complexify Spacetime?* records why that convention was given up: it is tied to a global inertial frame, it sits awkwardly with spinors and with curved spacetime, and in quantum field theory the Wick rotation is better understood as a change of causal structure than as a change of coordinates. The abandonment of $ict$ was not an abandonment of the complex structure, but it removed the one place where the complexification was visible in ordinary practice.

**Community and curriculum.** The quaternionists' program was a school with a doctrine; the vectorists' program was a tool set with users. Such a contest is settled by adoption, not by proof, and adoption followed the textbooks and the engineering curriculum.

The through-line is that the biquaternions lost on notation and practice, not on content — which is exactly what makes their return possible.

## The Return

The biquaternions and the closely related Clifford algebras returned to physics in the second half of the twentieth century, through several independent routes.

Feza Gürsey's work on conformal-invariant spinor and quaternion equations in the 1950s reopened the quaternion formulation of the Dirac field ("On a conform-invariant spinor wave equation," *Il Nuovo Cimento* **3** (1956)). In 1962, David Finkelstein, Josef Maria Jauch, Samuel Schiminovich, and David Speiser gave a systematic "Foundations of Quaternion Quantum Mechanics" (*Journal of Mathematical Physics* **3** (1962) 207–220), the first sustained attempt to build quantum theory on a quaternionic Hilbert space. In 1966 David Hestenes's *Space-Time Algebra* developed the Clifford algebra $Cl_{1,3}$ as the natural language of relativistic physics; the real Pauli algebra $Cl_{3,0}(\mathbb{R})$ is the biquaternion algebra in real form, and is used in physics under the name "algebra of physical space." Stephen Adler's *Quaternionic Quantum Mechanics and Quantum Fields* (Oxford, 1995) collected the mid-century program and examined its physical consequences.

A separate route is twistor theory: Roger Penrose's twistors live on complexified Minkowski space, with real Minkowski space as a slice, so the complexification that the biquaternion formulation makes algebraic is, in twistor theory, the fundamental arena. Modern biquaternionic treatments of the classical field equations — Silberstein's complex-vector Maxwell theory, the algebrodynamics of Vladimir Kassandrov and his collaborators, and the review work of Adrian Gsponer and Jean-Pierre Hurni — continue to use the algebra directly.

The framework developed in this corpus belongs to this return. The corpus reads the two subspaces $\mathbb{M}_{-}$ and $\mathbb{M}_{+}$ as a material sector and an informational sector, with the rotor conjugation as the coupling between them. That reading is a **proposal**: it is enabled by the algebra, and the algebra is old, but the historical record does not contain the proposal and nothing in the history vindicates it. The history establishes the existence and richness of the algebra, not the truth of the interpretation.

## What the History Does and Does Not Show

The record shows that the algebra was Hamilton's and was named by him; that its structural identifications with the Pauli algebra, the Lorentz double cover, and the qubit operator algebra are theorems about $\mathbb{B}$; that biquaternions were used for special relativity by Conway and Silberstein and then displaced by tensor and vector notation; and that the algebra returned in the mid-twentieth century through quaternionic quantum mechanics, geometric algebra, and twistor theory.

The record does not show that the biquaternion algebra is nature's, that any near-miss would have changed the physics, or that the biquaternion tradition anticipated quantum mechanics. The needed structures were in the algebra; no documented path runs from Hamilton's or Conway's work to Pauli's or Dirac's, and the connection is a structural identity recognized in retrospect. Nor does the record support the corpus's material/informational reading, which is a proposal placed on an old algebra.

The distinction on which this turns is between an algebra **containing** a structure and a person **using** it. Containment is a theorem of the 1840s; use is an event of the 1910s or the 1920s. "Near-miss" conflates the two, and this article uses it only where the documented record — the published relativity of Conway and Silberstein — justifies it.

## Summary

The biquaternions are the complex quaternions, $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$, introduced and named by Hamilton and treated at length in his *Lectures on Quaternions* (1853). The motive for the complexification was algebraic: in $\mathbb{H}$ a quadratic equation has no quadratic formula, its solution set need not be finite, and its resolution can call for a scalar square root of $-1$ — that is, for complex coefficients. As an algebra the biquaternions are $M_2(\mathbb{C})$, equivalently the Pauli algebra $Cl_{3,0}(\mathbb{R})$ and the even subalgebra of the spacetime algebra $Cl_{1,3}$. Their unit-norm-form elements are $SL(2,\mathbb{C})$, the double cover of the Lorentz group, acting on the material sector $\mathbb{M}_{-}$ by rotor conjugation; the full algebra $\mathbb{B}\cong M_2(\mathbb{C})$ is the operator algebra of a two-state system, of which $\mathbb{M}_{+}$ is the Hermitian subspace.

In physics, real quaternions first entered through Maxwell's electromagnetism and Tait's advocacy, and were displaced from the mid-1880s by the vector analysis of Gibbs and Heaviside. Biquaternions were applied to special relativity by Conway and by Silberstein in the 1910s, most fully in Silberstein's *The Theory of Relativity* (1914), and were displaced by Minkowski's tensor formalism. The algebra returned in the mid-twentieth century through quaternionic quantum mechanics, geometric algebra, twistor theory, and modern biquaternionic field theory.

The history shows that the algebra is old, rich, and structurally sufficient for relativity and for the qubit. It does not show that the algebra is nature's, nor that the biquaternion tradition anticipated the physics that later used it. The gap between containing a structure and having used it is the honest content of this history.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B} = \mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | Biquaternion algebra (complex quaternions) |
| $e_0 = 1, e_1, e_2, e_3$ | Quaternion basis, $e_k^2 = -e_0$ |
| $i$ | Scalar imaginary, $i^2 = -1$ (Hamilton's $h$) |
| $\bar{\cdot}, {}^{*}, {}^{\dagger}, {}^{\flat}$ | The four conjugations |
| $\mathbb{C}_{\mathbb{B}}$ | Complex subspace (complex scalars; center of $\mathbb{B}$) |
| $\mathbb{H}_{\mathbb{B}}$ | Quaternion subspace (real quaternions; norm $(4,0)$) |
| $\mathbb{M}_{+}$ | Hermitian subspace (informational sector; norm $(1,3)$) |
| $\mathbb{M}_{-}$ | Anti-Hermitian subspace (material sector; norm $(3,1)$) |
| $N(\tilde{Q}) = \tilde{Q}\bar{\tilde{Q}} = \sum_\mu Q_\mu^2$ | Norm form (zero divisors where $N=0$) |
| $\mathbb{B} \cong M_2(\mathbb{C}) \cong Cl_{3,0}(\mathbb{R})$ | Pauli algebra; $\Phi(e_k) = -i\sigma_k$ |
| $SL(2,\mathbb{C}) = \{\tilde{\Lambda} : \tilde{\Lambda}\bar{\tilde{\Lambda}} = e_0\}$ | Unit-norm-form biquaternions; Lorentz double cover |
| $\tilde{X} \mapsto \tilde{\Lambda}\tilde{X}\tilde{\Lambda}^{\dagger}$ | Rotor conjugation on $\mathbb{M}_{-}$ |
| $\tilde{P}_\pm = \tfrac{1}{2}(e_0 \pm i\hat{\mu})$ | Idempotent (pure state of $\mathbb{M}_{+}$) |
| $\mathrm{Tr}(\tilde{P}\tilde{H}) = 2\,\mathrm{Sc}(\tilde{P}\tilde{H})$ | Trace formula (Born rule) |
| $\mathbf{E} + ic\mathbf{B}$ | Riemann–Silberstein vector (Silberstein, 1907) |
| $\mathbb{H}$ | Real quaternion algebra (Hamilton 1843) |
| $ax = b$, $x = a^{-1}b$ | Linear equation in $\mathbb{H}$; the side on which $a$ stands matters |
| $x^{2} + bx + c = 0$ | Quaternion quadratic: no completing the square, no discriminant |
| $x^{2} + 2e_2x - 3 = 0$ | Worked quadratic: roots $\pm\sqrt{2} - e_2$ in $\mathbb{H}$, and $(-1 \pm \sqrt{2}\,i)e_2$ in $\mathbb{B}$ |

## Further Reading

- William Rowan Hamilton, *Lectures on Quaternions* (Hodges and Smith, Dublin, 1853), for the original treatment of quaternions and biquaternions, including the algebraic motive for the complex coefficients.
- Ivan Niven, "Equations in Quaternions," *American Mathematical Monthly* **48** (1941) 654–661, for the solution sets of quaternion equations, which may be a point, a circle, or a sphere.
- Samuel Eilenberg and Ivan Niven, "The Fundamental Theorem of Algebra for Quaternions," *Bulletin of the American Mathematical Society* **50** (1944) 246–248, for the existence of a quaternion root of a one-sided polynomial of positive degree.
- Peter Guthrie Tait, *An Elementary Treatise on Quaternions* (1867), for the leading nineteenth-century exposition after Hamilton.
- James Clerk Maxwell, *A Treatise on Electricity and Magnetism* (1873), for the quaternion notation in early electromagnetism.
- Michael J. Crowe, *A History of Vector Analysis* (University of Notre Dame Press, 1967), for the displacement of quaternions by vectors.
- Ludwik Silberstein, *The Theory of Relativity* (Macmillan, 1914), for the biquaternion formulation of special relativity.
- Élie Cartan, *Leçons sur la théorie des spineurs* (Hermann, 1938), for the spinors Cartan introduced in 1913.
- Cornelius Lanczos, "Die tensoranalytischen Beziehungen der Diracschen Gleichung," *Zeitschrift für Physik* **57** (1929) 447–473, for the early reformulation of the Dirac equation.
- David Finkelstein, Josef Maria Jauch, Samuel Schiminovich, and David Speiser, "Foundations of Quaternion Quantum Mechanics," *Journal of Mathematical Physics* **3** (1962) 207–220.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966; reissued Springer, 2015), for the Clifford-algebra formulation of relativistic physics.
- Stephen L. Adler, *Quaternionic Quantum Mechanics and Quantum Fields* (Oxford University Press, 1995).
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2001), for the identification of the biquaternion algebra with the Pauli algebra and the Lorentz double cover.
- Roger Penrose, *The Road to Reality* (Knopf, 2004), for complexified spacetime and twistor theory.
- Vladimir V. Kassandrov, "Relativistic Algebra of Space-Time and Algebrodynamics" (later published in *Gravitation and Cosmology*), for a modern biquaternionic approach.
- Adrian Gsponer and Jean-Pierre Hurni, "Cornelius Lanczos's Derivation of the Usual Action Integral of Classical Electrodynamics," *Foundations of Physics* **35** (2005), for Lanczos's quaternion electrodynamics.
