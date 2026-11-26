# __Conceptual Conventions__

## Introduction

**The rule.** A concept is used in this corpus only when two conditions hold together. It must be consistent with mathematics. And no result of experiment may contradict it. A concept that fails either condition is left out here.

**Why both conditions bite in this corpus.** These articles make physical claims, so neither condition can be met by silence. A concept that is mathematically inconsistent produces a wrong equation. A concept that a measurement contradicts produces a wrong prediction. There is no third shelter in which the question becomes purely mathematical.

**The two conditions are not a demand for derivation.** Most equations here are transcribed from the literature, and a transcribed equation is a correct one. The conditions ask only whether a concept is a sound object and a safe one. Where a claim comes from is a different question, and the corpus answers it in one line elsewhere: it derives the arena and imports the dynamics. That ledger classifies claims, not concepts. The field is an element whether the equation it appears in is derived or transcribed.

**Two ways of using a concept that passes.** A concept that passes both conditions is used in one of two ways. It is **preferred** when the algebra already contains it. It is **unpreferred** when it is a working tool that brings something the algebra does not contain: a chosen frame, a basis other than the multiplication table itself, a root, or a piece of the algebra printed as though it were the whole. An unpreferred concept is not false. It is used only when the article says what it brings.

**The two lists.** The next two sections give the lists, the one the corpus writes by default first and the one it writes only under a declaration second. The first holds the concepts it writes with no comment at all. The second holds the concepts it writes with the defect named. The order is that of a reader who wants the algebra first and the working tools after it. The summary states the result in a few lines.

**How a concept is presented.** The prose argues one claim from the start. Sentences are short, active, and carry one idea each. Every claim carries a warrant: a proof, a check, or a stated reading of the conventions. The vocabulary is plain and consistent from article to article. There is no filler and no flourish.

**No contravariant index appears in this article, and none appears anywhere in the series.** The one metric is the unit metric $\delta_{\mu\nu}=(1,1,1,1)$; a metric that is the identity raises nothing, so a raised index would name the same index twice. Every coefficient is written low, every contraction is written as a sum with the weight $\sum_\mu\varepsilon_\mu$, and no letter carries a raised spacetime index, in a display, in a table or in a definition.

## Preferred Concepts

These concepts are the algebra, its display and its two sectors, written down. Each one is read from an element, a form or the multiplication table itself, and none of them needs a root, an idempotent, an ideal, a gamma matrix or a metric supplied from outside.

- **Biquaternions.** The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with the four units $e_t=1\otimes1$, $\vec e_x=1\otimes\vec e_x$, $\vec e_y=1\otimes\vec e_y$, $\vec e_z=1\otimes\vec e_z$, and the element is $\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ with $Q_{\imath}=q_{\imath}+iq'_{\imath}$, that is eight real coordinates. One product fixes the rest: $e_{\imath} e_{\jmath}=\sum_\rho\varepsilon_{\imath\jmath}^{\ \ \rho}e_\rho$ with $\varepsilon_{\imath\jmath}^{\ \ \rho}\in\{0,+1,-1\}$. No complex number appears in the table, because $i$ is central and is carried by the coefficients. No matrix, column, ideal or projector appears in the definition.
- **The $4\times4$ AXF matrices.** The biquaternion algebra is four-dimensional over $\mathbb{C}$, so left multiplication is a linear map of a four-dimensional complex space, and one element is one $4\times4$ array with complex entries. That size is the natural one: the array is the element acting on the whole algebra, a square array with no compression and no half-object. In the coefficient basis the rule is one line, $L_{\mathrm{axf}}(\tilde Q)_{\imath\jmath}=[\tilde Qe_{\jmath}]_{\imath}$, the first column is the element itself, and the assignment is injective, multiplicative and lands on a four-dimensional subalgebra with unit $\mathrm I_4$. The display then has properties that no other frame has: the sixteen arrays of the four units are signed permutations with entries in $\{0,+1,-1\}$ that are the structure constants read by columns; they are orthogonal over $\mathbb{R}$ with determinant one; the transpose is the quaternion conjugation, $L^{\mathsf T}=L(\tilde Q^{\natural})$, and the dagger is the Hermitian conjugation, $L^{\dagger}=L(\tilde Q^{*})$; the eight matrices $\pm L_{\mathrm{axf},e_{\imath}}$ are the quaternion group $Q_8$; the real slice lands in $M_4(\mathbb{R})$; the trace is $4Q_t$, so the trace is the clock; the determinant is the squared quaternionic norm, $\det L=\langle\tilde Q\rangle_{\natural}^{2}$; the rank is even, hence $0$, $2$ or $4$; the right family is the transposed left one between $D$ and its inverse, $R_{\mathrm{axf}}(\tilde Q)=D\,L_{\mathrm{axf}}(\tilde Q)^{\mathsf T}D$ with $D=\operatorname{diag}(1,-1,-1,-1)$; each of the four norms is one quarter of a trace, $N=\tfrac14\operatorname{Tr}(M^{\mathsf T}M)$, $H=\tfrac14\operatorname{Tr}(M^{\dagger}M)$, $K=\tfrac14\operatorname{Tr}(M^{\mathsf T}M^{\dagger})$ and $P=\tfrac14\operatorname{Tr}(M^{2})$; the six subspaces are four entrywise conditions, and the vector condition $\operatorname{Tr}M=0$ and the antisymmetry $M^{\mathsf T}=-M$ coincide. The frame is also the only sparse one: a basis in which all sixteen arrays are signed permutations is this one up to a relabelling of the three directions and a sign on each vector, $f_t=\pm e_t$ and $f_{k}=\pm e_{\sigma(k)}$ with $\sigma\in S_3$, which is $96$ arrays, or $48$ with the scalar unit fixed. The display is preferred because it adds no datum of its own: its entries are the multiplication table, and it names no axis and imposes no metric.
- **The two sectors.** The anti-Hermitian subspace $\mathbb{B}_{\Phi}$ carries the four-vectors and the interval. The Hermitian subspace $\mathbb{B}_{\Psi}$ carries the observables, the states and the spin generators. The algebra supplies the subspaces and the forms on them, and the identification of a subspace with a physical role is the programme's step, stated at every use.
- **The unit metric of $\mathbb{B}$.** The quaternionic norm is $\langle\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}=Q_t^2+Q_x^2+Q_y^2+Q_z^2$, and all four coefficients are $+1$: the metric is the unit metric $\delta_{\mu\nu}=(1,1,1,1)$. On real coefficients that is the ordinary Euclidean metric, positive definite, and no direction is singled out by a sign. Here ${}^{\natural}$ keeps the scalar and negates the three vectors. The metric is the same on the two sectors: with $Q_t=i q'_t$ the time square is negative because $i^2=-1$, and the interval is $-{r'_{t}}^2+r_x^2+r_y^2+r_z^2$. Nothing is absorbed: the $i$ stays in the coefficient, and there is one metric.

## Unpreferred Concepts

Each concept below is used somewhere in the corpus, and each one brings something the algebra does not contain. The list names the defect. An unpreferred concept is admitted as a display when the article that prints it declares the missing piece once, at the head of the display.

- **The Pauli matrices $\sigma_\eta$.** *The defect:* the array carries a preferred axis, and neither the algebra nor the sentence names it. Isotropy is measured, so the axis is a defect and not a notation.
- **The gamma matrices $\gamma_\mu$.** *The defect:* the five basis operators carry a preferred frame, and with it a preferred axis, and the frame is not named. Isotropy is measured, so the frame is a defect and not a notation.
- **A Clifford algebra as a foundation.** *The defect:* it starts from a quadratic form, so a metric is imposed on the algebra before the algebra is read. The biquaternion algebra carries its own form, the norm $\tilde Q\tilde{Q}^{\natural}=\sum_\mu Q_\mu^2$, and the sector fixes the signs. A metric supplied from outside is a preferred datum, and nothing in the algebra asks for one.
- **The word gauge.** *The defect:* the word is doing too much work and carries a hundred years of confusing baggage. One sentence uses it for a frame, for a transformation, for a field, for an invariance and for a fixing, and nothing in the sentence says which. The reader has to guess, and the guess is often wrong. Each of the five objects has a plain name, and the plain name removes the guess. The corpus writes the plain name. It keeps the word *gauge* only where a transcribed result arrives under that word, and there it says so.
- **The Wick rotation, $r'_t\mapsto-i\tau$.** *The defect:* the series uses one name for two operations on the algebra. The contour rotation $r'_t\mapsto-i\tau$ continues the material coordinate off the real axis, and at real $\tau$ its source is not a point of $\mathbb{B}_{\Phi}$; it is not a map between the subspaces. The relabelling of one coefficient, $i r'_t\mapsto\tau$, is the map $W=\mathrm{diag}(-i,1,1,1)$, and it carries a point of $\mathbb{B}_{\Phi}$ to a point of $\mathbb{B}_{H}$, the inertia from $(3,1)$ to $(4,0)$, and the light cone away. That second operation is a change of the reality condition on one continued field, $\flat\to\bar{\cdot}$ with $\flat=\bar{\cdot}\circ W^{2}$, and not an identification of two objects of the algebra: $\mathbb{B}_{H}$ is closed under multiplication and $\mathbb{B}_{\Phi}$ is not, so no ring map carries one onto the other.

The gauge entry, in detail. The word covers five different objects, and each one has a plain name.

- *The choice of local frame.* Write local frame, local reference frame, local basis, internal frame, frame field in the tetrad sense, or section of a bundle, which is a choice of representative at each point.
- *The transformation.* Write local frame rotation, local rotation, local colour rotation for $SU(N)$, local change of basis, frame transformation, change of local frame, or reparameterisation.
- *The boson, the field $A_\mu$.* Write connection, connection field, parallel-transport field, frame connection, compensator, which is the field that compensates the derivative, or rotor field, which is the reading of this corpus.
- *The invariance.* Write local frame independence, local symmetry, frame covariance, or local basis independence.
- *The fixing.* Write choice of frame, choosing a representative, fixing the frame, or choosing a section.

This article adopts one plain name per object, and no other use of the word.

| where the word *gauge* appears | what this article writes |
| --- | --- |
| gauge transformation | local frame rotation |
| gauge field, gauge boson | connection |
| gauge invariance | local frame independence |
| gauge choice, fixing a gauge | choice of frame |
| gauge group | frame-rotation group |
| gauge theory | connection theory |

The rotor reading is the one that fits the algebra. The transformation is a rotor. The field is a rotor-valued connection. The invariance is the independence of the local frame. The sentence "the gauge field restores gauge invariance under local gauge transformations" then reads "the connection field restores independence of the local frame under local frame rotations". The physics is the same, and the word is gone.

The word stays where a result arrives named with it, and the article says which sense is meant: the electroweak gauge group, the gauge fixing of a path integral, and the gauge symmetry of a transcribed Lagrangian. Nothing is renamed against the literature; the corpus only declines to write the word where it is writing on its own.

## Summary

A concept is used in this corpus only when it agrees with mathematics and no result of experiment contradicts it. Both conditions bite here, because these articles make physical claims.

The concepts that pass are used in one of two ways. Preferred concepts are the algebra itself, and there are four: the biquaternion algebra, the $4\times4$ AXF display, the two sectors and the unit metric. Unpreferred concepts are working tools that bring a frame, a sign pattern, a dimension or an ambiguity: the Pauli matrices, the gamma matrices, the Clifford algebra as a foundation, the Wick rotation and the word *gauge*. Each is admitted only with the missing piece declared.

The AXF display is the model case: it prints the multiplication table and nothing else, so no axis, no frame and no metric enters with it. The Clifford entry is the one worth reading twice: the identification with $\mathrm{Cl}_{3,0}$ is exact, and it brings an inertia and a second simple factor that the algebra does not have.

## Further Reading

- [Algebra and Element Conventions](../articles_physics/algebra-and-element-conventions.html). The base, the glyphs, and the one metric of the series.
- [Product and Form Conventions](../articles_physics/product-and-form-conventions.html). The twelve products and the four forms, which are the four choices of conjugation on the two slots.
- [Norm and Pairing Conventions](../articles_physics/norm-and-pairing-conventions.html). The four norms, the polar word and the three pairings.
- [Special Element Conventions](../articles_physics/special-element-conventions.html). The central map, the chirality convention, where operator chirality — the side of a basis operator — is fixed, and the spin and spinor conventions.
- [Frame and Metric Conventions](../articles_physics/frame-and-metric-conventions.html). The two frames, the one metric they share, the Clifford map, and the rule that a frame is declared before it is used.
- [Matrix Representations Conventions](../articles_physics/matrix-representations-conventions.html). The three displays, the Pauli form, the Clifford structure and the legacy gamma block.
- [Operator and Calculus Conventions](../articles_physics/operator-and-calculus-conventions.html). The operator that is its element, the Fock exception and the calculus.
- [Physics Units and Common Elements Conventions](../articles_physics/physics-units-and-common-elements-conventions.html). The physical units and the common glyphs.
- [Index and Notation Conventions](../articles_physics/index-and-notation-conventions.html). The marks and the subscripts.
- [Conceptual Conventions](../articles_maths/conceptual-conventions.html). The same rule at the algebraic layer, where the three kinds of defect are stated in full.
- [The Differentiable Field: One Primary Equation and the Linear Sector](../articles_physics/the-differentiable-field-one-primary-equation-and-the-linear-sector.html). The ledger of the postulated, the derived and the imported, which classifies claims and not concepts.
- [The AXF Matrices: Axis-Free, Integer Entries](../articles_physics/the-axf-matrices-axis-free-integer-entries.html#why-the-pauli-and-the-gamma-displays-are-refused). The defect in full, the covariance test, and the frames that are not defects.
- [Biquaternion Physical Interpretation of Operator Chirality](../articles_physics/biquaternion-physical-interpretation-of-operator-chirality.html). The objects the physics does not need, and the limit of the copies.
