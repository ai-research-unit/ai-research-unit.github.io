# __The Clifford Layer of the Physics Corpus: Where It Is, the Odd Sector, and the Biquaternion Replacement__

## Introduction

The corpus states its foundational isomorphism in one line: the biquaternion algebra is the even part of the Clifford algebra of Minkowski space,

$$
\mathbb{B}\;\cong\;\mathrm{Cl}^{+}_{1,3}(\mathbb{R}).
$$

The line is a theorem. It is also a boundary. The Clifford algebra has sixteen real dimensions; the even part has eight. The other eight — the odd part, spanned by the four vectors $\gamma^\mu$ and the four trivectors — are **not** in $\mathbb{B}$. No product of even elements is odd, so no inner operation of $\mathbb{B}$ can produce an odd element. The odd part is a module over $\mathbb{B}$, not a subalgebra of it.

The physics needs that module. Parity is $\gamma^0$. Charge conjugation is $i\gamma^2$. Time reversal is $\gamma^1\gamma^3$. The Dirac adjoint is $\psi^\dagger\gamma^0$. A reflection with normal $u$ is $x\mapsto-\epsilon(u)\,u\,x\,u$. Every one of these is odd. Every one is outside $\mathbb{B}$ as an element. As an operation it is not: the star $\varkappa$ and left multiplication give it, as §*The Split: What Can Be Rewritten, and What Cannot* and §*The Gamma Matrices as Biquaternion Operations* show.

This article records how far the borrowing goes, and what can replace it.

**The counts.** A scan of the 395 physics articles finds **115** that carry a Clifford marker: an indexed $\gamma$, an explicit gamma-matrix representation, a Clifford symbol $\mathrm{Cl}_{p,q}$, or the dictionary map $\mathsf{M}_4$. Of these, **51** are structural (an explicit matrix block, at least ten indexed gamma occurrences, or at least five Clifford symbols), **47** use the layer in passing, and **17** name it only. **18** write an explicit gamma-matrix representation (the first pass counted 17; the Klein–Gordon article adds one). **52** contain $\gamma^5$ or $\gamma_5$. The borrowing reaches **9 of the 12** categories of `physics.md`. The first pass counted 109; the six additions are the Klein–Gordon square, the CKM matrix, the trace anomaly, the spinor representation of the Lorentz group, the scalar field in the centre, and the dual equivalence of the Dirac and topological massive gauge fields. Their bands are in the tables below.

**The sharp case.** *The Reflection and the Rotation in Biquaternionic Form* is the purest instance. Its subject is the part of the Clifford algebra that $\mathbb{B}$ does not contain, and it says so: "The odd elements are not in $\mathbb{B}$, so they have no biquaternion representative." The sentence is exact about elements. It is not a statement about operations: the article's own section *Conjugation by $\gamma^0$ Is Complex Conjugation* shows that the reflection is conjugation by $\gamma^0$, which is the star $\varkappa$ up to the sign $\epsilon(u)$. The odd generator is the intermediate; the operation is biquaternionic. This is the clearest case of the distinction, not the clearest case of an irreducible import.

The first part is an inventory. The second part is the replacement study. The answer is yes, but not uniformly: **32 of the 51 band-1 articles can be rewritten by substitution in the biquaternion formalism; 19 cannot without deleting their subject.** No article needs the odd generator $\mathbb{B}\oplus\mathbb{B}\gamma$ to do its physics. The star $\varkappa(b)=\bar b$ is needed only where an antilinear operation appears: parity, charge conjugation, time reversal, the Dirac adjoint, the real structure. The double is needed only where the odd element is the object. §*The Split: What Can Be Rewritten, and What Cannot* gives both lists and the reasons. §*The Gamma Matrices as Biquaternion Operations* gives the dictionary.

## The Split: What Can Be Rewritten, and What Cannot

The inventory counts symbols. This section counts roles. The same gamma matrix can be a name, a device, or the subject.

- A **name**. The article writes an object that the biquaternion algebra already has: the field, the operator, the bilinear, the projector. The rewrite replaces the name and keeps the equation.
- A **device**. The article uses the matrix representation to compute something the algebra can compute without it. The rewrite is local, but it must be checked line by line.
- The **subject**. The article is about the Clifford algebra, its grading, its Pin group, its classification, its trace, or a theorem about the representation. The rewrite would delete what the article proves.

Thirty-two of the 51 band-1 articles can be rewritten, or need no rewrite at all. Nineteen cannot: they are about the algebra, or about a comparison that a rewrite would destroy. The split is by substance, not by symbol count: an article with sixty gammas can be easy, and an article with six Clifford symbols can be impossible. The route census in Part II cuts by carrier; this cut is by what the article is about.

### A. Articles That Can Switch to the Biquaternion Formalism

The rewrite uses the operations of §*The Gamma Matrices as Biquaternion Operations*: the product, the left and right multiplications, and the star $\varkappa(b)=\bar b$ only where an antilinear operation appears. No article in this part needs the odd generator $\mathbb{B}\oplus\mathbb{B}\gamma$.

#### A1. The Dirac equation and its solutions (11)

| article | Clifford use | the rewrite |
|---|---|---|
| [The Dirac Equation](../articles_physics/the-dirac-equation-in-biquaternionic-form.html) | $\gamma^0,\gamma^5$, 3 matrix blocks | Already has the $\mathbb{B}$-only form; the matrix block stays as a translation. |
| [Exercise: Plane-Wave Solutions](../articles_physics/exercise-plane-wave-solutions-of-the-biquaternion-dirac-equation.html) | $\gamma^0,\gamma^5$, the full matrices | The matrices are displayed once, then translated: $\gamma^0=R_{i\vec e_x}$, $\gamma^k=L_{i\vec e_k}R_{\vec e_y}$, $\gamma_5=R_{-i\vec e_z}$. The spinor is one biquaternion. |
| [Solutions and the Non-Relativistic Limit](../articles_physics/the-dirac-equation-in-biquaternionic-form-solutions-and-the-non-relativistic-limit.html) | $\gamma^0,\gamma^5$, 1 matrix block | Same, plus the Pauli limit. |
| [Exercise: The Non-Relativistic Limit and the Pauli Equation](../articles_physics/exercise-the-non-relativistic-limit-and-the-pauli-equation.html) | $\gamma^0$, 1 matrix block | The Pauli matrices are the quaternion units; substitution. |
| [Klein–Gordon from the Dirac Square](../articles_physics/klein-gordon-from-the-dirac-square-in-biquaternionic-form.html) | $\gamma^\mu$, 5 matrix blocks | The square of the biquaternion operator; the identity is the check. |
| [The Foldy–Wouthuysen Transformation](../articles_physics/the-foldy-wouthuysen-transformation-in-biquaternionic-form.html) | $\gamma^0,\gamma^5$ | The energy projectors are $(1\pm\varkappa)/2$; the transformation is a biquaternion rotation. |
| [Zitterbewegung](../articles_physics/zitterbewegung-in-biquaternionic-form.html) | $\gamma^0,\gamma^5$, 1 matrix block | The velocity operator $\gamma^0\gamma^k$ is $L_{-i\vec e_k}$; the oscillation is a biquaternion rotation. |
| [The Dirac Path Integral](../articles_physics/the-dirac-path-integral-in-biquaternionic-form.html) | $\gamma^\mu,\gamma^5$, $\mathrm{Cl}$ | The Grassmann measure is untouched; only the Dirac operator is rewritten. |
| [Canonical Quantization](../articles_physics/canonical-quantization-of-the-biquaternion-dirac-field.html) | $\gamma^0,\gamma^5$ | The adjoint and the anticommutator; the quantization rule is unchanged. |
| [The Quantized Dirac Field](../articles_physics/the-quantized-dirac-field-in-biquaternionic-form.html) | $\gamma^0$ | The mode expansion; the modes are biquaternion spinors. |
| [Exercise: Chirality and the Weyl Spinors](../articles_physics/exercise-chirality-and-the-weyl-spinors.html) | $\gamma^0,\gamma^\mu,\gamma^5$, 1 matrix block | The projectors are $R_{(e_t\pm i\vec e_z)/2}$. |

Why these are easy: the equation, the plane waves, the non-relativistic limit and the energy split are statements about the biquaternion field and its products. The gamma matrices enter as the operator; replacing them by the complex-linear dictionary $\gamma^0=R_{i\vec e_x}$, $\gamma^k=L_{i\vec e_k}R_{\vec e_y}$, $\gamma_5=R_{-i\vec e_z}$ on the four-dimensional carrier changes no solution and no number. The real form $\varkappa$, $\varkappa L_{-i\vec e_k}$ is the same Clifford algebra when chirality is not needed. The one care point is the external $i$ of the chiral projector, which is not the biquaternion $i$.

#### A2. The field, its currents and its bilinears (7)

| article | Clifford use | the rewrite |
|---|---|---|
| [The Nonlinear Dirac Equation and the Thirring Model](../articles_physics/the-nonlinear-dirac-equation-and-the-thirring-model-in-biquaternionic-form.html) | $\gamma^0,\gamma^\mu,\gamma^5$ | The scalar and axial bilinears are biquaternion products. |
| [The Gordon Decomposition](../articles_physics/the-gordon-decomposition-in-biquaternionic-form.html) | $\gamma^0,\gamma^5$ | The current split is algebraic. |
| [The Anomalous Magnetic Moment](../articles_physics/the-anomalous-magnetic-moment-in-biquaternionic-form.html) | $\gamma^0,\gamma^\mu$, 1 matrix block | $\sigma^{\mu\nu}$ is even, a bivector; the form factor is unchanged. |
| [The Electric Dipole Moment](../articles_physics/the-electric-dipole-moment-and-the-biquaternion-anti-hermitian-structure.html) | $\gamma^0,\gamma^5$, 1 matrix block | The $CP$-odd bilinear is a biquaternion product; the external $i$ is the convention. |
| [The Proton](../articles_physics/the-proton-in-biquaternionic-form.html) | $\gamma^5$ | The chiral structure; no odd operator. |
| [The Rarita–Schwinger Equation](../articles_physics/the-rarita-schwinger-equation-spin-3-2-in-biquaternionic-form.html) | $\gamma^0,\gamma^\mu,\gamma^5$, $\mathrm{Cl}$ | The vector-spinor and the gamma-traceless constraint are biquaternion constraints. |
| [Matter Makes Space](../articles_physics/matter-makes-space-an-external-construction-from-quaternionic-spinors.html) | $\gamma^0,\gamma^\mu,\gamma^5$, 1 matrix block | The source already uses quaternionic spinors; the dictionary is local. |

Why: a bilinear is a product of the field and its conjugate. The gamma matrix in $\bar\psi\gamma^\mu\psi$ names the vector slot; in the biquaternion algebra the slot is the anti-Hermitian part of the product. The rewrite is local. The Rarita–Schwinger field is the one case with an extra index: the vector index is carried by the field, and the gamma-traceless constraint becomes a biquaternion constraint.

#### A3. Chirality and the gauge sector (6)

| article | Clifford use | the rewrite |
|---|---|---|
| [Chiral Fermions](../articles_physics/chiral-fermions-in-the-biquaternion-framework.html) | $\gamma^5$, 1 matrix block | The projectors and the chiral connection. |
| [The Chiral Condensate](../articles_physics/the-chiral-condensate-and-dynamical-symmetry-breaking-in-biquaternionic-form.html) | $\gamma^5$, 1 matrix block | The condensate is a chiral bilinear. |
| [Bosonization](../articles_physics/bosonization-in-biquaternionic-form.html) | $\gamma^5$, 1 matrix block | The chiral currents are biquaternion bilinears. |
| [Electroweak Theory](../articles_physics/electroweak-theory-under-the-biquaternion-framework-a-research-agenda.html) | $\gamma^5$ | The agenda is programmatic; $\gamma^5$ is the projector. |
| [The Standard Model](../articles_physics/the-standard-model-under-the-biquaternion-framework-a-research-agenda.html) | $\gamma^5$ | Same. |
| [Quantum Chromodynamics](../articles_physics/quantum-chromodynamics-under-the-biquaternion-framework-a-research-agenda.html) | $\gamma^5$ | Same. |

Why: chirality is the right action, not an extra structure. The projectors are $R_{(e_t\pm i\vec e_z)/2}$. The gauge group is external in both presentations, so the rewrite does not touch it. The work is the projector and the trace convention; the length is the article, not the obstacle.

#### A4. The carrier and the dictionary (2)

| article | Clifford use | why it comes first |
|---|---|---|
| [The Spinor Module](../articles_physics/the-spinor-module-in-biquaternionic-form-and-its-lorentz-action.html) | $\gamma^0,\gamma^5$, $\mathrm{Cl}$ | The carrier is the bimodule $\mathbb{B}$ with $L$ and $R$; the Lorentz action is the left action. |
| [The Daviau Map](../articles_physics/the-daviau-map-and-the-space-clifford-formulation-of-the-dirac-equation.html) | $\gamma^0$, $\mathrm{Cl}$ | Already the bridge; the map is the dictionary. |

These are the two articles where the biquaternion action is defined. They are the first to rewrite because every other article cites them.

#### A5. Already biquaternion, or no Clifford content (6)

| article | Clifford use | status |
|---|---|---|
| [The Conformal Group](../articles_physics/the-conformal-group-in-biquaternionic-form.html) | $\mathrm{Cl},\gamma,\gamma^5$ | Already a biquaternion article; the Clifford group is the comparison. |
| [The Algebrodynamical Programme](../articles_physics/the-algebrodynamical-programme-nonlinear-cauchy-riemann-and-self-quantized-charge.html) | $\mathrm{Cl}$ | Already quaternionic; the Clifford algebra is the comparison. |
| [The Biquaternion Basis of a Unified-Field Fibre Bundle](../articles_physics/the-biquaternion-basis-of-a-unified-field-fibre-bundle.html) | $\gamma^0,\gamma^\mu$, $\mathrm{Cl}$ | The basis is biquaternion; the Clifford content is the source's language. |
| [The Square-Zero Element](../articles_physics/the-square-zero-element-nilpotency-as-mode-differential-and-supercharge.html) | $\mathrm{Cl}$ | Nilpotents are in $\mathbb{B}$; no rewrite. |
| [The Wick Theorem](../articles_physics/the-wick-theorem-in-biquaternionic-form.html) | $\mathrm{Cl}$ | Combinatorics; no Clifford content. |
| [Fock Space](../articles_physics/fock-space-and-creation-annihilation-operators-in-biquaternionic-form.html) | $\mathrm{Cl}$ | Algebraic; no Clifford content. |

No rewrite is needed. These articles are already in the target formalism, or the Clifford symbols are comparisons. Check them for stray formulas; do not convert them.

### B. Articles That Cannot Switch Easily, and Why

These 19 are not a backlog. Each has an obstacle that a notation change does not remove.

#### B1. The Clifford algebra is the subject (8)

| article | why the rewrite fails |
|---|---|
| [The Reflection and the Rotation](../articles_physics/the-reflection-and-the-rotation-in-biquaternionic-form.html) | The Pin group, the grading and the determinant table are the theorem; the operations can be stated in $\mathbb{B}$, but the article is about the odd half. |
| [The Grading, Fermion Parity and the Two Sectors](../articles_physics/the-grading-and-fermion-parity-in-biquaternionic-form.html) | The $\mathbb{Z}/2$ grading and the odd slot are the object; $\mathbb{B}$ is the even slot. Its subject is the grading, so it stays in $\mathrm{Cl}$. |
| [The Superalgebra Reading and the Odd Extension](../articles_physics/the-superalgebra-reading-and-the-odd-extension-in-biquaternionic-form.html) | The graded commutator and the odd extension are the object; the double is the algebra being studied. |
| [Supersymmetric Quantum Physics](../articles_physics/supersymmetric-quantum-physics-in-the-biquaternion-framework.html) | The supercharge is odd; the graded algebra is the frame. |
| [The Spectral Triple](../articles_physics/the-spectral-triple-of-the-biquaternion-algebra.html) | The Dirac operator, the real structure and the grading define the triple; $\mathbb{B}$ has no Dirac operator without the module. |
| [Left-Right Symmetric Fermions](../articles_physics/left-right-symmetric-fermions-from-complex-split-biquaternions-and-bioctonions.html) | The bioctonion algebra is the point; it is larger than $\mathbb{B}$. |
| [The Number of Generations](../articles_physics/the-number-of-generations-and-the-biquaternion-algebra.html) | A classification theorem for $\mathrm{Cl}$; not a statement about $\mathbb{B}$. |
| [The Particle Roster of the Complex Octonionic Chain](../articles_physics/the-particle-roster-of-the-complex-octonionic-chain-algebra.html) | The octonionic chain is the point; it is larger than $\mathbb{B}$. |

Converting these would preserve the symbols and lose the theorem. The correct move is a cross-reference and, where useful, a biquaternion example alongside the Clifford statement.

#### B2. The trace and the measure (2)

| article | why the rewrite fails |
|---|---|
| [The Fujikawa Method](../articles_physics/the-fujikawa-method-and-the-path-integral-anomaly-in-biquaternionic-form.html) | The anomaly is the regulated Jacobian; the trace is over the Dirac module. |
| [Anomalies and Anomaly Cancellation](../articles_physics/anomalies-and-anomaly-cancellation-in-biquaternionic-form.html) | The cancellation is a sum of chiral traces. |

The biquaternion trace is not the Dirac trace. On $\mathbb{B}$ the regular trace is $\operatorname{Tr}_{\Delta}+\operatorname{Tr}_{\Delta,\gamma_5}$; the central $i$ has trace $4i$ in the regular trace and $0$ on $\Delta$. The anomaly coefficient depends on the trace, the measure and the factor of two from the real-linear determinant. These must be recomputed and checked against the known coefficient. Until that computation exists, the rewrite is a research task, not a substitution.

#### B3. The result is a representation-theoretic theorem (5)

| article | why the rewrite fails |
|---|---|
| [The CPT Theorem](../articles_physics/the-cpt-theorem-in-biquaternionic-form.html) | The antiunitary operations and their phases; the proof uses the representation. |
| [Charge Conjugation and the Division Ring](../articles_physics/charge-conjugation-and-the-division-ring-in-biquaternionic-form.html) | $C$ as a pseudoautomorphism of $\mathrm{Cl}_{n,m}$; the question is when it is trivial. |
| [The Spin–Statistics Theorem](../articles_physics/the-spin-statistics-theorem-in-biquaternionic-form.html) | The connection between spin and statistics is a theorem about the representation. |
| [The Majorana Equation](../articles_physics/the-majorana-equation-in-biquaternionic-form.html) | The real structure $\flat$ is not the star; a careless rewrite changes the physics. |
| [The Neutrino and Majorana Fermions](../articles_physics/the-neutrino-and-majorana-fermions-in-biquaternionic-form.html) | The same real structure, plus the physical distinction. |

The biquaternion form can state these results. It cannot yet prove them, because the proofs use the representation and, in the Majorana case, a real structure that is a different map from $\varkappa$. Rewriting the statement is easy; rewriting the proof is the work.

#### B4. The comparison is the subject (4)

| article | why the rewrite fails |
|---|---|
| [The Dirac Algebra and Biquaternions — A Dictionary](../articles_physics/the-dirac-algebra-and-biquaternions-a-dictionary.html) | The dictionary is the object; a rewrite is a research task, and its conventions propagate to every other article. |
| [Paravectors and the Geometry of Spacetime](../articles_physics/paravectors-and-the-geometry-of-spacetime.html) | The article works in the algebra of physical space; the paravector language is the subject. |
| [The Dirac–Hestenes Equation](../articles_physics/the-dirac-hestenes-equation-and-spacetime-algebra-in-biquaternionic-form.html) | Spacetime algebra is the subject; the biquaternion form is the comparison. |
| [Subluminal and Superluminal Electromagnetic Waves](../articles_physics/subluminal-and-superluminal-electromagnetic-waves-and-the-lepton-mass-spectrum.html) | The article records an external Clifford-bundle programme; the Clifford algebra is the source's framework. |

These articles exist to relate two formalisms, or to report a result in the other one. Converting them removes the relation. Keep them, and point to the biquaternion calculus.

### The Count

| group | articles | effort | obstacle |
|---|---:|---|---|
| A1 Dirac equation and solutions | 11 | local | none |
| A2 field and bilinears | 7 | local | none; one extra index |
| A3 chirality and gauge | 6 | local, long | none; the projector |
| A4 carrier and dictionary | 2 | local, first | none |
| A5 already biquaternion | 6 | none | none |
| B1 algebra is the subject | 8 | keep | the theorem |
| B2 trace and measure | 2 | research | the trace |
| B3 representation theorem | 5 | rebuild the proof | the representation |
| B4 comparison is the subject | 4 | keep | the relation |
| **total** | **51** | | |

Thirty-two can switch. Nineteen cannot: twelve because the Clifford algebra, or its relation to another formalism, is the subject; seven because a trace or a representation theorem must be recomputed.


## What the Layer Is

Six imports make up the layer.

| import | object | dimension | in $\mathbb{B}$? |
|---|---|---|---|
| the ambient algebra | $\mathrm{Cl}_{1,3}$ | 16 real | even part only |
| the generators | $\gamma^\mu$ | 4 odd | no |
| the pseudoscalar | $\omega=\gamma^0\gamma^1\gamma^2\gamma^3$ | grade 4, even | even, not odd |
| the chirality element | $\gamma^5=i\omega$ | grade 4, even | even, not odd |
| the reflection group | $\mathrm{Pin}(1,3)$ | odd coset of $\mathrm{Spin}$ | no |
| the dictionary map | $\mathsf{M}_4:\mathbb{B}\to\mathrm{Cl}^{+}_{1,3}$ | 8 real | isomorphism |

The even part is not the problem. $\omega$ and $\gamma^5$ are even, and the chirality projectors $\tfrac12(1\pm\gamma^5)$ are even. The problem is the first, second and fifth rows: the generators, the odd part they span, and the reflection group built from them.

The layer also imports a metric and a sign. The Clifford metric is $g=\mathrm{diag}(+1,-1,-1,-1)$ on the generators, and the Pin action carries the sign $\epsilon(u)=\pm1$ fixed by $u^2=\epsilon(u)I$. Neither is an element of $\mathbb{B}$; both are data of the Clifford algebra.

## The Odd-Sector Theorem

The obstruction is elementary and exact.

**Proposition.** Let $\mathbb{B}=\mathrm{Cl}^{+}_{1,3}$. Every element of $\mathbb{B}$ is even. The product of two even elements is even. Hence no odd element is a product of elements of $\mathbb{B}$, and no algebraic operation of $\mathbb{B}$ produces one.

*Proof.* The grading is $\mathrm{Cl}=\mathrm{Cl}^{0}\oplus\mathrm{Cl}^{1}$ with $\mathrm{Cl}^{i}\mathrm{Cl}^{j}\subseteq\mathrm{Cl}^{i+j}$. The even part is a subalgebra; the odd part is a two-sided module over it. $\mathbb{B}=\mathrm{Cl}^{0}$. $\square$

Three consequences follow, and together they are the content of this article.

- **The odd elements are not recoverable.** They are not hidden in $\mathbb{B}$ under another name. They are the other half of a larger algebra, and the isomorphism $\mathbb{B}\cong\mathrm{Cl}^{+}$ is precisely the statement that the other half is absent.
- **The operations that need them are not inner.** Parity, time reversal, charge conjugation, reflection and the Dirac adjoint are module maps. They act on the spinor module, not on $\mathbb{B}$ by left multiplication. They cannot be written as $X\mapsto UXU^{-1}$ or $X\mapsto UXU^{*}$ with $U\in\mathbb{B}$. As real-linear operations on $\mathbb{B}$ they are $\varkappa$ and $\varkappa L_b$; as elements they are inner in $\mathbb{B}\oplus\mathbb{B}\gamma$, but not in $\mathbb{B}$.
- **The absence is structural for elements, not for operations.** A change of basis inside $\mathbb{B}$ cannot supply an odd element. Only an enlargement of the algebra can, and the minimal enlargement is one generator, $\mathbb{B}\oplus\mathbb{B}\gamma$. The physics does not need the enlargement: parity, time reversal, charge conjugation and the Dirac adjoint are the star and left multiplication on $\mathbb{B}$, as §*Element, Operation, Carrier* shows. The enlargement is needed only when an odd *element* is wanted, as in the superalgebra.

The last point separates this layer from the gauge layer. The gauge articles write an external index $\mu$; the Clifford articles write an external grading. Both are outside $\mathbb{B}$ as elements. The gauge index has no known replacement inside the algebra; the odd sector has one: the operations $\varkappa L_b$ on $\mathbb{B}$.

## Element, Operation, Carrier

The odd-sector theorem is exact, and its scope must be read precisely. It answers three questions, and the replacement turns on the third.

| question | answer | object |
|---|---|---|
| Is there an odd element of $\mathbb{B}$? | no | element |
| Is an odd element produced by a product in $\mathbb{B}$? | no | inner operation |
| Is there an odd **action** on a biquaternion carrier? | yes | real-linear operator |
| Is there an algebra generated by $\mathbb{B}$ and one odd generator? | yes, $\mathbb{B}\oplus\mathbb{B}\gamma\cong\mathrm{Cl}_{1,3}$ | graded algebra |

The distinction is between an **element** and an **operation**. The star $\bar{\cdot}$ is not an element of $\mathbb{B}$; it is a real-linear operation on $\mathbb{B}$. The left multiplication $L_b$ is an operation; the element $b$ is its parameter. The odd generators are not elements of $\mathbb{B}$, but they are operations on $\mathbb{B}$:
$$
\gamma^0=\varkappa,\qquad \gamma^k=\varkappa L_{-i\vec e_k}=L_{i\vec e_k}\varkappa,
$$
with $\varkappa(b)=\bar b$. The algebra generated by these operations is $\mathrm{Cl}_{1,3}$; the carrier remains $\mathbb{B}$. The enlargement is of the operator algebra, not of the carrier.

The second distinction is between $\mathbb{B}$ as a **left module** and $\mathbb{B}$ as a **bimodule**. The left-regular module is the even sector: $\mathbb{B}$ acting on itself by left multiplication. The physical Dirac spinor is the bimodule $\Delta=S\oplus S^{\mathrm{c}}$, which the real-linear dictionary identifies with $\mathbb{B}$: left multiplication carries the Lorentz action, right multiplication carries the chirality. The two are the same eight-real-dimensional space with different actions, and the audit's phrase "the biquaternion field" covers both. The odd operations do not act on the left-regular module; they act on the bimodule and exchange its chiral halves.

The third distinction is between the **central imaginary** of $\mathbb{B}$ and the **volume element** of $\mathrm{Cl}$. In $\mathbb{B}$ the element $i$ is central. In $\mathrm{Cl}$ the element that represents it is the volume element $\omega$, which is even but **not central**: it anticommutes with the odd generators. The odd extension is exactly the algebra in which $i$ stops being central. This is the algebraic reason the odd sector is not an artefact of notation: it is what makes the volume element a chirality operator rather than a scalar.

These three distinctions are the content of the replacement. The first part of this article recorded where the layer is; the second part uses them to say what can replace it.

## The Worked Example: *The Reflection and the Rotation*

The article is organised around the grading, and the grading is exactly the odd sector. Its imports can be listed one by one.

| import | where it occurs | what it does |
|---|---|---|
| $\mathrm{Cl}_{1,3}=\mathrm{Cl}^{+}\oplus\mathrm{Cl}^{-}$ | boxed, §*The Grading by Reflection Count* | defines the even/odd split |
| $\mathbb{B}\cong\mathrm{Cl}^{+}_{1,3}$ | same section | identifies the algebra with the even half |
| $\gamma^0$ as frame | §*The Frame $\gamma^0$ and the Hermitian Sector* | reaches the odd part from the even part |
| $\mathsf{M}_4(\mathbb{M}_+)=\mathrm{span}\{I,\gamma^0\gamma^1,\gamma^0\gamma^2,\gamma^0\gamma^3\}$ | same section | identifies the Hermitian sector with the timelike bivectors |
| $N=\mathrm{diag}(+1,-1,-1,-1)=g$ | same section | derives the Clifford metric from the biquaternion norm |
| $\gamma^0\mathsf{M}_4(\tilde Q)\gamma^0=\mathsf{M}_4(\tilde Q^{*})$ | §*Conjugation by $\gamma^0$ Is Complex Conjugation* | makes the frame the complex conjugation |
| $\mathrm{rev}(\mathsf{M}_4(\tilde Q))=\mathsf{M}_4(\tilde Q^{\natural})$ | same section | makes Clifford reversal the quaternion conjugation |
| $\mathrm{Pin}(1,3)=\mathrm{Spin}(1,3)\cdot\{\text{unit vectors}\}$ | §*The Spaces of Rotations and of Reflections* | names the reflection group |
| $\rho(u):x\mapsto-\epsilon(u)\,u\,x\,u$ | §*One Algebra, Read Twice* | the reflection law |
| determinant table: odd $\to-1$, "in $\mathbb{B}$? no" | §*The Grading by Reflection Count* | states the obstruction in a table |

The decisive sentence is in §*One Algebra, Read Twice*:

> The odd elements are not in $\mathbb{B}$, so they have no biquaternion representative. They lie in the odd part of $\mathrm{Cl}_{1,3}$ and act on vectors by the two-sided map of the Pin group.

The article then builds the reflection group, the determinant table, the Pin action and the anti-linear case on that outside. The construction is correct. In the vocabulary fixed in §*The Operator Vocabulary*, the Pin map is an **inner conjugation** $T_{u,u^{-1}}$, up to the sign $\epsilon(u)$, not a generic two-sided operator with independent parameters. The title is right about operations: the article's own §*Conjugation by $\gamma^0$ Is Complex Conjugation* proves that conjugation by $\gamma^0$ is the star $\varkappa$ on $\mathbb{B}$, so the reflection is a biquaternion operation. The odd objects are not elements of $\mathbb{B}$; they are the real-linear operations $\varkappa$ and $\varkappa L_b$. Read as a statement about elements, the title is wrong; read as a statement about operations, it is right. The distinction is the one §*Element, Operation, Carrier* makes.

This is the clearest single case in the corpus because the subject and the obstruction coincide. In the other articles the odd element is a tool; here it is the topic.

## The Root: The Dictionary

*The Dirac Algebra and Biquaternions — A Dictionary* is where the boundary is drawn, and it draws it correctly. It states that the gamma matrices generate $\mathrm{Cl}_{1,3}$, that the biquaternions form the even subalgebra, and that the generators themselves are not biquaternions: they are obtained from the algebra by the frame $\gamma^0$.

As a dictionary, the article is exact. As a source, it is the root of the layer: once $\mathsf{M}_4$ is fixed, the odd part is available, and the downstream articles use it. The dictionary carries 41 Clifford symbols, 88 occurrences of $\mathsf{M}_4$ and four explicit matrix blocks. The Dirac equation article, which imports the same structure, is cited by 30 physics articles.

The distinction matters for the count. A dictionary is a bridge; the problem is that the bridge became the road. In the replacement interpretation, the dictionary is the even half of the isomorphism of Part II: it identifies $\mathbb{B}$ with $\mathrm{Cl}^+_{1,3}$, and the odd half is the operators $\varkappa L(\mathbb{B})$, or the single module $\mathbb{B}\gamma$ in the double presentation. The matrix dictionary becomes a translation table again, and the biquaternion algebra is the road.

## The Odd Part in Use

The articles below use odd elements as working objects. Each entry names the object and the operation it performs.

| article | odd object | role |
|---|---|---|
| [The Reflection and the Rotation](../articles_physics/the-reflection-and-the-rotation-in-biquaternionic-form.html) | $\gamma^0$, $\gamma^\mu$, $\mathrm{Pin}$ | reflections, parity, time reversal |
| [The CPT Theorem](../articles_physics/the-cpt-theorem-in-biquaternionic-form.html) | $\gamma^0$, $i\gamma^2$, $\gamma^1\gamma^3$ | $P$, $C$, $T$ on the spinor module |
| [Charge Conjugation and the Division Ring](../articles_physics/charge-conjugation-and-the-division-ring-in-biquaternionic-form.html) | $\Pi A^{*}\Pi^{-1}$ | pseudoautomorphism of $\mathrm{Cl}_{n,m}$ |
| [Antilinear Structure and the Two Kinds of Mass](../articles_physics/antilinear-structure-and-the-two-kinds-of-mass-in-biquaternionic-form.html) | $\Pi$ | charge-conjugation pseudoautomorphism |
| [The Grading, Fermion Parity and the Two Sectors](../articles_physics/the-grading-and-fermion-parity-in-biquaternionic-form.html) | $\mathrm{Cl}^{1}$ | parity grading |
| [The Superalgebra Reading and the Odd Extension](../articles_physics/the-superalgebra-reading-and-the-odd-extension-in-biquaternionic-form.html) | $\mathrm{Cl}^{1}$ | graded commutator, odd extension |
| [Zitterbewegung](../articles_physics/zitterbewegung-in-biquaternionic-form.html) | $\gamma^0$ | the odd element with no representative |
| [The Nonlinear Dirac Equation and the Thirring Model](../articles_physics/the-nonlinear-dirac-equation-and-the-thirring-model-in-biquaternionic-form.html) | $\gamma^0$ | Dirac adjoint, spinor bilinears |
| [The Anomalous Magnetic Moment](../articles_physics/the-anomalous-magnetic-moment-in-biquaternionic-form.html) | $\gamma^\mu$ ($\sigma^{\mu\nu}$ is even) | the generator and its commutator |
| [The Dirac–Hestenes Equation](../articles_physics/the-dirac-hestenes-equation-and-spacetime-algebra-in-biquaternionic-form.html) | $\gamma^\mu$ (STA) | spacetime-algebra vectors |


Four of the admissions are explicit. The CPT article writes that the internal matrices of $C$ and $P$ "are odd Clifford elements, outside $\mathbb{B}$". Zitterbewegung writes that $\gamma^0$ "is an **odd** element of the Clifford algebra" and that "an odd element has no representation" in $\mathbb{B}$. The nonlinear Dirac article writes that the Dirac adjoint carries the odd $\gamma^0$ and the axial current carries $\gamma_5$, and that "neither is in the even subalgebra". The reflection article writes the sentence quoted above.

The corpus knows the boundary. The counts measure how often it is crossed.

### The $\gamma^5$ Users

The chirality element needs a separate note, because it is **even**: $\gamma^5=i\omega=i\gamma^0\gamma^1\gamma^2\gamma^3$ is the scalar imaginary times the product of four generators, hence grade 4 and even. It is not an odd element, and its use is not an import of the odd part. It is the use of the matrix representation and of the trace.

Fifty-two articles contain the symbol. The heaviest are:

| article | $\gamma^5$ occurrences | what is computed |
|---|---:|---|
| [The Electric Dipole Moment](../articles_physics/the-electric-dipole-moment-and-the-biquaternion-anti-hermitian-structure.html) | 54 | the $CP$-odd bilinear and its form factor |
| [The Fujikawa Method](../articles_physics/the-fujikawa-method-and-the-path-integral-anomaly-in-biquaternionic-form.html) | 50 | the regulated Jacobian, $\operatorname{tr}\gamma_5\mathcal O$ |
| [Chiral Fermions](../articles_physics/chiral-fermions-in-the-biquaternion-framework.html) | 38 | the chiral projectors and the chiral connection |
| [The Chiral Condensate](../articles_physics/the-chiral-condensate-and-dynamical-symmetry-breaking-in-biquaternionic-form.html) | 30 | the condensate and its breaking pattern |
| [Anomalies and Anomaly Cancellation](../articles_physics/anomalies-and-anomaly-cancellation-in-biquaternionic-form.html) | 25 | the axial anomaly |
| [The Nonlinear Dirac Equation and the Thirring Model](../articles_physics/the-nonlinear-dirac-equation-and-the-thirring-model-in-biquaternionic-form.html) | 24 | the axial current |
| [The CPT Theorem](../articles_physics/the-cpt-theorem-in-biquaternionic-form.html) | 24 | the discrete operations |
| [Bosonization](../articles_physics/bosonization-in-biquaternionic-form.html) | 20 | the chiral current algebra |

The pattern is consistent: $\gamma^5$ enters where a trace over the Dirac module is taken. The trace is a property of the representation, not of $\mathbb{B}$, and it is the representation that carries the odd generators. The replacement does not remove $\gamma^5$; it identifies it with the volume element and the right action, and it moves the trace problem to the Dirac module. Part II returns to this.

## The Categories

Nine of the twelve categories use the layer. Three are clean: Non Relativistic Non Quantum Theory, Relativistic Non Quantum Theory, and Thermodynamics and Statistical Mechanics.

| category | `physics.md` | articles | band 1 | band 2 | band 3 |
|---|---:|---:|---:|---:|---:|
| Biquaternion Universe | 3 | 2 | 0 | 1 | 1 |
| Biquaternion Physical Interpretation of Mathematics | 42 | 3 | 1 | 1 | 1 |
| Biquaternion Non Relativistic Quantum Theory | 189 | 4 | 0 | 4 | 0 |
| Biquaternion Non Relativistic Non Quantum Theory | 426 | 0 | 0 | 0 | 0 |
| Biquaternion Electromagnetism | 513 | 4 | 2 | 2 | 0 |
| Biquaternion Relativity | 590 | 8 | 2 | 4 | 2 |
| Biquaternion Relativistic Quantum Theory | 652 | 36 | 18 | 14 | 4 |
| Biquaternion Relativistic Non Quantum Theory | 814 | 0 | 0 | 0 | 0 |
| Biquaternion Quantum Fields | 873 | 24 | 12 | 8 | 4 |
| Biquaternion Particle Physics and Gauge Fields | 1089 | 29 | 14 | 10 | 5 |
| Biquaternion Gravity and Cosmology | 1258 | 5 | 2 | 3 | 0 |
| Biquaternion Thermodynamics and Statistical Mechanics | 1293 | 0 | 0 | 0 | 0 |

## The Articles by Category

**Band 1** is structural: an explicit gamma-matrix block, at least ten indexed gamma occurrences, or at least five Clifford symbols. **Band 2** uses the layer in passing: three to nine indexed gammas, or one to four Clifford symbols. **Band 3** names it once or twice.

### Band 1 — structural

| article | category | subsection | $\gamma^0$ | $\gamma^\mu$ | $\gamma^5$ | matrices | $\mathrm{Cl}$ |
|---|---|---|---:|---:|---:|---:|---:|
| [The Square-Zero Element: Nilpotency as Mode, Differential and Supercharge](../articles_physics/the-square-zero-element-nilpotency-as-mode-differential-and-supercharge.html) | Physical Interpretation of Mathematics | Algebra | 0 | 0 | 3 | 0 | 19 |
| [Subluminal and Superluminal Electromagnetic Waves in Biquaternionic Form](../articles_physics/subluminal-and-superluminal-electromagnetic-waves-and-the-lepton-mass-spectrum.html) | Electromagnetism | — | 22 | 4 | 43 | 0 | 0 |
| [The Algebrodynamical Programme: Nonlinear Cauchy–Riemann Conditions, Self-Quantized Charge, and Induced Causal Geometry](../articles_physics/the-algebrodynamical-programme-nonlinear-cauchy-riemann-and-self-quantized-charge.html) | Electromagnetism | — | 0 | 0 | 0 | 0 | 6 |
| [The Conformal Group in Biquaternionic Form](../articles_physics/the-conformal-group-in-biquaternionic-form.html) | Relativity | — | 0 | 2 | 2 | 0 | 19 |
| [Paravectors and the Geometry of Spacetime](../articles_physics/paravectors-and-the-geometry-of-spacetime.html) | Relativity | — | 1 | 0 | 0 | 0 | 7 |
| [The Dirac Algebra and Biquaternions — A Dictionary](../articles_physics/the-dirac-algebra-and-biquaternions-a-dictionary.html) | Relativistic Quantum Theory | Particles of spin 1/2 | 62 | 0 | 22 | 4 | 41 |
| [The Reflection and the Rotation in Biquaternionic Form](../articles_physics/the-reflection-and-the-rotation-in-biquaternionic-form.html) | Relativistic Quantum Theory | Particles of spin 1/2 | 46 | 0 | 12 | 0 | 25 |
| [The Dirac Equation in Biquaternionic Form](../articles_physics/the-dirac-equation-in-biquaternionic-form.html) | Relativistic Quantum Theory | Particles of spin 1/2 | 29 | 0 | 17 | 3 | 24 |
| [The Dirac–Hestenes Equation and Spacetime Algebra in Biquaternionic Form](../articles_physics/the-dirac-hestenes-equation-and-spacetime-algebra-in-biquaternionic-form.html) | Relativistic Quantum Theory | Particles of spin 1/2 | 41 | 8 | 0 | 0 | 12 |
| [The Rarita–Schwinger Equation: Spin 3/2 in Biquaternionic Form](../articles_physics/the-rarita-schwinger-equation-spin-3-2-in-biquaternionic-form.html) | Relativistic Quantum Theory | Particles of spin 1 and above | 18 | 4 | 15 | 0 | 10 |
| [The Nonlinear Dirac Equation and the Thirring Model in Biquaternionic Form](../articles_physics/the-nonlinear-dirac-equation-and-the-thirring-model-in-biquaternionic-form.html) | Relativistic Quantum Theory | Particles of spin 1/2 | 16 | 3 | 24 | 0 | 0 |
| [Exercise: Plane-Wave Solutions of the Biquaternion Dirac Equation](../articles_physics/exercise-plane-wave-solutions-of-the-biquaternion-dirac-equation.html) | Relativistic Quantum Theory | Particles of spin 1/2 | 19 | 0 | 18 | 1 | 0 |
| [The Foldy–Wouthuysen Transformation in Biquaternionic Form](../articles_physics/the-foldy-wouthuysen-transformation-in-biquaternionic-form.html) | Relativistic Quantum Theory | Particles of spin 1/2 | 21 | 0 | 10 | 0 | 0 |
| [The Dirac Equation in Biquaternionic Form — Solutions and the Non-Relativistic Limit](../articles_physics/the-dirac-equation-in-biquaternionic-form-solutions-and-the-non-relativistic-limit.html) | Relativistic Quantum Theory | Particles of spin 1/2 | 14 | 0 | 11 | 1 | 0 |
| [Exercise: Chirality and the Weyl Spinors](../articles_physics/exercise-chirality-and-the-weyl-spinors.html) | Relativistic Quantum Theory | Particles of spin 1/2 | 1 | 2 | 14 | 1 | 0 |
| [The Dirac Path Integral in Biquaternionic Form](../articles_physics/the-dirac-path-integral-in-biquaternionic-form.html) | Relativistic Quantum Theory | Particles of spin 1/2 | 0 | 2 | 1 | 0 | 8 |
| [Zitterbewegung in Biquaternionic Form](../articles_physics/zitterbewegung-in-biquaternionic-form.html) | Relativistic Quantum Theory | Particles of spin 1/2 | 13 | 0 | 1 | 1 | 2 |
| [The Daviau Map and the Space Clifford Formulation of the Dirac Equation](../articles_physics/the-daviau-map-and-the-space-clifford-formulation-of-the-dirac-equation.html) | Relativistic Quantum Theory | Particles of spin 1/2 | 4 | 0 | 0 | 0 | 12 |
| [The Gordon Decomposition of the Dirac Current in Biquaternionic Form](../articles_physics/the-gordon-decomposition-in-biquaternionic-form.html) | Relativistic Quantum Theory | Particles of spin 1/2 | 9 | 0 | 5 | 0 | 0 |
| [Supersymmetric Quantum Physics in the Biquaternion Framework](../articles_physics/supersymmetric-quantum-physics-in-the-biquaternion-framework.html) | Relativistic Quantum Theory | Particles of spin 1/2 | 2 | 0 | 10 | 0 | 2 |
| [The Spinor Module in Biquaternionic Form and Its Lorentz Action](../articles_physics/the-spinor-module-in-biquaternionic-form-and-its-lorentz-action.html) | Relativistic Quantum Theory | Particles of spin 1/2 | 2 | 0 | 1 | 0 | 7 |
| [Exercise: The Non-Relativistic Limit and the Pauli Equation](../articles_physics/exercise-the-non-relativistic-limit-and-the-pauli-equation.html) | Relativistic Quantum Theory | Particles of spin 1/2 | 5 | 0 | 0 | 1 | 1 |
| [Klein–Gordon from the Dirac Square in Biquaternionic Form](../articles_physics/klein-gordon-from-the-dirac-square-in-biquaternionic-form.html) | Relativistic Quantum Theory | Particles of spin 1/2 | 0 | 18 | 0 | 5 | 0 |
| [The CPT Theorem in Biquaternionic Form](../articles_physics/the-cpt-theorem-in-biquaternionic-form.html) | Quantum Fields | Generalities | 37 | 0 | 24 | 1 | 20 |
| [The Anomalous Magnetic Moment in Biquaternionic Form](../articles_physics/the-anomalous-magnetic-moment-in-biquaternionic-form.html) | Quantum Fields | Particles of spin 1/2 | 14 | 9 | 0 | 1 | 0 |
| [The Grading, Fermion Parity and the Two Sectors in Biquaternionic Form](../articles_physics/the-grading-and-fermion-parity-in-biquaternionic-form.html) | Quantum Fields | Generalities | 1 | 1 | 2 | 0 | 27 |
| [Bosonization in Biquaternionic Form](../articles_physics/bosonization-in-biquaternionic-form.html) | Quantum Fields | Generalities | 4 | 0 | 20 | 1 | 2 |
| [The Superalgebra Reading and the Odd Extension in Biquaternionic Form](../articles_physics/the-superalgebra-reading-and-the-odd-extension-in-biquaternionic-form.html) | Quantum Fields | Generalities | 6 | 1 | 0 | 0 | 19 |
| [Charge Conjugation and the Division Ring: Charged, Neutral and Truly Neutral Particles in Biquaternionic Form](../articles_physics/charge-conjugation-and-the-division-ring-in-biquaternionic-form.html) | Quantum Fields | Generalities | 0 | 0 | 0 | 0 | 25 |
| [The Spin–Statistics Theorem in Biquaternionic Form](../articles_physics/the-spin-statistics-theorem-in-biquaternionic-form.html) | Quantum Fields | Generalities | 19 | 0 | 0 | 0 | 2 |
| [Canonical Quantization of the Biquaternion Dirac Field](../articles_physics/canonical-quantization-of-the-biquaternion-dirac-field.html) | Quantum Fields | Particles of spin 1/2 | 15 | 0 | 1 | 0 | 0 |
| [The Quantized Dirac Field in Biquaternionic Form](../articles_physics/the-quantized-dirac-field-in-biquaternionic-form.html) | Quantum Fields | Particles of spin 1/2 | 11 | 0 | 0 | 0 | 1 |
| [The Spectral Triple of the Biquaternion Algebra](../articles_physics/the-spectral-triple-of-the-biquaternion-algebra.html) | Quantum Fields | Generalities | 0 | 0 | 3 | 0 | 8 |
| [The Wick Theorem in Biquaternionic Form](../articles_physics/the-wick-theorem-in-biquaternionic-form.html) | Quantum Fields | Generalities | 0 | 0 | 0 | 0 | 8 |
| [Fock Space and Creation/Annihilation Operators in Biquaternionic Form](../articles_physics/fock-space-and-creation-annihilation-operators-in-biquaternionic-form.html) | Quantum Fields | Generalities | 0 | 0 | 0 | 0 | 5 |
| [Left-Right Symmetric Fermions from Complex Split Biquaternions and Bioctonions](../articles_physics/left-right-symmetric-fermions-from-complex-split-biquaternions-and-bioctonions.html) | Particle Physics and Gauge Fields | Particles of spin 1/2 | 1 | 0 | 2 | 0 | 76 |
| [The Electric Dipole Moment and the Biquaternion Anti-Hermitian Structure](../articles_physics/the-electric-dipole-moment-and-the-biquaternion-anti-hermitian-structure.html) | Particle Physics and Gauge Fields | Particles of spin 1/2 | 5 | 0 | 54 | 1 | 0 |
| [The Fujikawa Method and the Path-Integral Anomaly in Biquaternionic Form](../articles_physics/the-fujikawa-method-and-the-path-integral-anomaly-in-biquaternionic-form.html) | Particle Physics and Gauge Fields | Particles of spin 1/2 | 4 | 0 | 50 | 1 | 0 |
| [Chiral Fermions in the Biquaternion Framework](../articles_physics/chiral-fermions-in-the-biquaternion-framework.html) | Particle Physics and Gauge Fields | Particles of spin 1/2 | 4 | 0 | 38 | 1 | 0 |
| [The Majorana Equation in Biquaternionic Form](../articles_physics/the-majorana-equation-in-biquaternionic-form.html) | Particle Physics and Gauge Fields | Particles of spin 1/2 | 0 | 31 | 1 | 0 | 7 |
| [The Chiral Condensate and Dynamical Symmetry Breaking in Biquaternionic Form](../articles_physics/the-chiral-condensate-and-dynamical-symmetry-breaking-in-biquaternionic-form.html) | Particle Physics and Gauge Fields | Particles of spin 1/2 | 4 | 0 | 30 | 1 | 1 |
| [Anomalies and Anomaly Cancellation in Biquaternionic Form](../articles_physics/anomalies-and-anomaly-cancellation-in-biquaternionic-form.html) | Particle Physics and Gauge Fields | Particles of spin 1/2 | 4 | 0 | 25 | 1 | 0 |
| [The Neutrino and Majorana Fermions in Biquaternionic Form](../articles_physics/the-neutrino-and-majorana-fermions-in-biquaternionic-form.html) | Particle Physics and Gauge Fields | Particles of spin 1/2 | 9 | 3 | 6 | 1 | 0 |
| [The Proton in Biquaternionic Form](../articles_physics/the-proton-in-biquaternionic-form.html) | Particle Physics and Gauge Fields | Particles of spin 1/2 | 0 | 0 | 13 | 0 | 0 |
| [Electroweak Theory under the Biquaternion Framework — A Research Agenda](../articles_physics/electroweak-theory-under-the-biquaternion-framework-a-research-agenda.html) | Particle Physics and Gauge Fields | Generalities | 0 | 0 | 12 | 0 | 0 |
| [The Number of Generations and the Biquaternion Algebra](../articles_physics/the-number-of-generations-and-the-biquaternion-algebra.html) | Particle Physics and Gauge Fields | Particles of spin 1/2 | 0 | 0 | 0 | 0 | 11 |
| [The Standard Model under the Biquaternion Framework — A Research Agenda](../articles_physics/the-standard-model-under-the-biquaternion-framework-a-research-agenda.html) | Particle Physics and Gauge Fields | Generalities | 0 | 0 | 10 | 0 | 0 |
| [Quantum Chromodynamics under the Biquaternion Framework — A Research Agenda](../articles_physics/quantum-chromodynamics-under-the-biquaternion-framework-a-research-agenda.html) | Particle Physics and Gauge Fields | Generalities | 0 | 0 | 10 | 0 | 0 |
| [The Particle Roster of the Complex Octonionic Chain Algebra](../articles_physics/the-particle-roster-of-the-complex-octonionic-chain-algebra.html) | Particle Physics and Gauge Fields | Particles of spin 1/2 | 0 | 0 | 0 | 0 | 8 |
| [Matter Makes Space — An External Construction from Quaternionic Spinors](../articles_physics/matter-makes-space-an-external-construction-from-quaternionic-spinors.html) | Gravity and Cosmology | — | 2 | 5 | 7 | 1 | 0 |
| [The Biquaternion Basis of a Unified-Field Fibre Bundle](../articles_physics/the-biquaternion-basis-of-a-unified-field-fibre-bundle.html) | Gravity and Cosmology | — | 7 | 1 | 0 | 0 | 6 |

### Band 2 — in passing

| article | category | $\gamma$ | $\gamma^5$ | $\mathrm{Cl}$ |
|---|---|---:|---:|---:|
| [Conventions in the Biquaternion Universe](../articles_physics/conventions-in-the-biquaternion-universe.html) | Universe | 0 | 0 | 2 |
| [The Roots of a General Element: Mass, Frames and the Mass Shell](../articles_physics/the-roots-of-a-general-element-mass-frames-and-the-mass-shell.html) | Physical Interpretation of Mathematics | 3 | 3 | 0 |
| [The Bloch Ball as the Normalised Slice of the Future Light Cone](../articles_physics/the-bloch-ball-as-the-trace-one-slice-of-the-future-light-cone.html) | Non Relativistic Quantum Theory | 0 | 0 | 1 |
| [The Born Rule from the Hermitian Form — Derivation and Comparison](../articles_physics/the-born-rule-as-a-trace-formula-derivation-and-comparison.html) | Non Relativistic Quantum Theory | 0 | 0 | 1 |
| [Unitarity from Centrality: The Biquaternion Norm-Preservation Theorem](../articles_physics/unitarity-from-centrality-the-biquaternion-norm-preservation-theorem.html) | Non Relativistic Quantum Theory | 0 | 0 | 1 |
| [Squeezing Beyond the Biquaternion Algebra](../articles_physics/squeezing-beyond-the-biquaternion-algebra.html) | Non Relativistic Quantum Theory | 0 | 0 | 4 |
| [The Field-Strength Biquaternion and Its Invariants](../articles_physics/the-field-strength-biquaternion-and-its-invariants.html) | Electromagnetism | 5 | 0 | 0 |
| [The Lorentz Force in Biquaternion Form](../articles_physics/the-lorentz-force-in-biquaternion-form.html) | Electromagnetism | 0 | 0 | 3 |
| [Relativistic Mechanics in Biquaternionic Form](../articles_physics/relativistic-mechanics-in-biquaternionic-form.html) | Relativity | 0 | 0 | 2 |
| [The Lorentz Transformation as a Biquaternionic Rotation](../articles_physics/the-lorentz-transformation-as-a-biquaternionic-rotation.html) | Relativity | 0 | 0 | 1 |
| [The Lorentz Group in Biquaternionic Form — Structure and Representations](../articles_physics/the-lorentz-group-in-biquaternionic-form-structure-and-representations.html) | Relativity | 0 | 0 | 2 |
| [The Relativistic Particle in an External Field, in Biquaternionic Form](../articles_physics/the-relativistic-particle-in-an-external-field-in-biquaternionic-form.html) | Relativity | 0 | 0 | 1 |
| [The Dirac Oscillator in Biquaternionic Form](../articles_physics/the-dirac-oscillator-in-biquaternionic-form.html) | Relativistic Quantum Theory | 9 | 0 | 0 |
| [The s-Vector Representation of the Dirac Spinor in Biquaternionic Form](../articles_physics/the-s-vector-representation-of-the-dirac-spinor-in-biquaternionic-form.html) | Relativistic Quantum Theory | 8 | 6 | 0 |
| [The Electron in Biquaternionic Form](../articles_physics/the-electron-in-biquaternionic-form.html) | Relativistic Quantum Theory | 8 | 6 | 1 |
| [The Minimal Coupling of the Biquaternion Dirac Field to Electromagnetism](../articles_physics/the-minimal-coupling-of-the-biquaternion-dirac-field-to-electromagnetism.html) | Relativistic Quantum Theory | 7 | 0 | 1 |
| [The Chiral Algebra of Biquaternions and the Cyclic Representation of the Dirac Equation](../articles_physics/the-chiral-algebra-of-biquaternions-and-the-cyclic-representation-of-the-dirac-equation.html) | Relativistic Quantum Theory | 6 | 6 | 1 |
| [Møller Scattering in Biquaternionic Form](../articles_physics/moller-scattering-in-biquaternionic-form.html) | Relativistic Quantum Theory | 5 | 0 | 0 |
| [Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form](../articles_physics/antilinear-structure-and-the-two-kinds-of-mass-in-biquaternionic-form.html) | Relativistic Quantum Theory | 5 | 4 | 2 |
| [Parra's Four Options of the Dirac Equation and the Discrete Symmetries](../articles_physics/parras-four-options-of-the-dirac-equation-and-the-discrete-symmetries.html) | Relativistic Quantum Theory | 3 | 0 | 4 |
| [Triality and the Ding Construction for the Dirac Spinor in Biquaternionic Form](../articles_physics/triality-and-the-ding-construction-for-the-dirac-spinor-in-biquaternionic-form.html) | Relativistic Quantum Theory | 3 | 3 | 0 |
| [The Hydrogen Atom in Biquaternionic Form — The Relativistic Case](../articles_physics/the-hydrogen-atom-in-biquaternionic-form-the-relativistic-case.html) | Relativistic Quantum Theory | 3 | 1 | 2 |
| [Bispinor Fields and the Fundamental Solution of the Generalized Maxwell–Dirac Equation](../articles_physics/bispinor-fields-and-the-fundamental-solution-of-the-generalized-maxwell-dirac-equation.html) | Relativistic Quantum Theory | 0 | 0 | 2 |
| [The Self-Dual and Anti-Self-Dual Split: Spin 1 from the Biquaternion Material Sector](../articles_physics/the-self-dual-and-anti-self-dual-split-spin-1-from-the-biquaternion-material-sector.html) | Relativistic Quantum Theory | 0 | 0 | 1 |
| [Higher Spin from Tensor Products: Why the Biquaternion Algebra Admits Only Spin Zero and One-Half](../articles_physics/higher-spin-from-tensor-products-why-the-biquaternion-algebra-admits-only-spin-0-and-one-half.html) | Relativistic Quantum Theory | 0 | 0 | 3 |
| [The Material-Informational Split as a Superselection Structure in Biquaternionic Form](../articles_physics/the-material-informational-split-as-a-superselection-structure-in-biquaternionic-form.html) | Relativistic Quantum Theory | 0 | 0 | 1 |
| [Fermion Doubling and the Nielsen–Ninomiya Theorem in Biquaternionic Form](../articles_physics/fermion-doubling-and-the-nielsen-ninomiya-theorem-in-biquaternionic-form.html) | Quantum Fields | 9 | 5 | 0 |
| [The Feynman Propagator in Biquaternionic Form](../articles_physics/the-feynman-propagator-in-biquaternionic-form.html) | Quantum Fields | 6 | 0 | 0 |
| [The Schwinger–Dyson Equations and the Ward–Takahashi Identities in Biquaternionic Form](../articles_physics/the-schwinger-dyson-equations-and-the-ward-takahashi-identities-in-biquaternionic-form.html) | Quantum Fields | 4 | 4 | 0 |
| [The Fermionic Path Integral in Biquaternionic Form](../articles_physics/the-fermionic-path-integral-in-biquaternionic-form.html) | Quantum Fields | 4 | 0 | 0 |
| [Dirac Matter: Graphene, Dirac Cones and Topological Insulators in Biquaternionic Form](../articles_physics/dirac-matter-graphene-dirac-cones-and-topological-insulators-in-biquaternionic-form.html) | Quantum Fields | 3 | 0 | 0 |
| [The Jordan–Wigner Transformation in Biquaternionic Form](../articles_physics/the-jordan-wigner-transformation-in-biquaternionic-form.html) | Quantum Fields | 3 | 0 | 4 |
| [The Scalar Fock Space in Biquaternionic Form](../articles_physics/the-scalar-fock-space-in-biquaternionic-form.html) | Quantum Fields | 0 | 0 | 2 |
| [The Fermionic Fock Space in Biquaternionic Form](../articles_physics/the-fermionic-fock-space-in-biquaternionic-form.html) | Quantum Fields | 0 | 0 | 4 |
| [The Neutron in Biquaternionic Form](../articles_physics/the-neutron-in-biquaternionic-form.html) | Particle Physics and Gauge Fields | 7 | 7 | 0 |
| [The Pion and the Chiral Lagrangian in Biquaternionic Form](../articles_physics/the-pion-and-the-chiral-lagrangian-in-biquaternionic-form.html) | Particle Physics and Gauge Fields | 3 | 2 | 0 |
| [The Gauge Principle in Biquaternionic Form](../articles_physics/the-gauge-principle-in-biquaternionic-form.html) | Particle Physics and Gauge Fields | 2 | 2 | 2 |
| [The Gauge Group Ceiling: Why the Biquaternion Algebra Reaches SU(2) but Not SU(3)](../articles_physics/the-gauge-group-ceiling-why-the-biquaternion-algebra-reaches-su-2-but-not-su-3.html) | Particle Physics and Gauge Fields | 0 | 0 | 3 |
| [The Higgs Mechanism in Biquaternionic Form](../articles_physics/the-higgs-mechanism-in-biquaternionic-form.html) | Particle Physics and Gauge Fields | 0 | 0 | 3 |
| [The Spin–Mass Formula and the Spectrum of Elementary Particles in Biquaternionic Form](../articles_physics/the-spin-mass-formula-and-the-particle-spectrum-in-biquaternionic-form.html) | Particle Physics and Gauge Fields | 0 | 0 | 1 |
| [The Spin–Charge Hilbert Space and the SU(3) Supermultiplets in Biquaternionic Form](../articles_physics/the-spin-charge-hilbert-space-and-the-su3-supermultiplets-in-biquaternionic-form.html) | Particle Physics and Gauge Fields | 0 | 0 | 3 |
| [The Gluon: An Octet Outside the Biquaternion Algebra](../articles_physics/the-gluon-an-octet-outside-the-biquaternion-algebra.html) | Particle Physics and Gauge Fields | 0 | 0 | 1 |
| [Gauge Redundancy and the Information in the Gauge Orbit in Biquaternionic Form](../articles_physics/gauge-redundancy-and-the-information-in-the-gauge-orbit-in-biquaternionic-form.html) | Particle Physics and Gauge Fields | 0 | 0 | 1 |
| [The CKM Matrix and CP Violation in Biquaternionic Form](../articles_physics/the-ckm-matrix-and-cp-violation-in-biquaternionic-form.html) | Particle Physics and Gauge Fields | 5 | 0 | 0 |
| [Torsion, Contorsion and the Spin Connection in Biquaternionic Form](../articles_physics/torsion-contorsion-and-the-spin-connection-in-biquaternionic-form.html) | Gravity and Cosmology | 7 | 4 | 0 |
| [Curved Spacetime and the Biquaternion Framework](../articles_physics/curved-spacetime-and-the-biquaternion-framework.html) | Gravity and Cosmology | 5 | 0 | 0 |
| [Linearized Gravity in Biquaternionic Form](../articles_physics/linearized-gravity-in-biquaternionic-form.html) | Gravity and Cosmology | 0 | 0 | 1 |

### Band 3 — named only

| article | category | $\gamma$ | $\mathrm{Cl}$ |
|---|---|---:|---:|
| [What the Biquaternion Algebra Cannot Do: A Catalogue of Algebraic Obstructions](../articles_physics/what-the-biquaternion-algebra-cannot-do-a-catalogue-of-algebraic-obstructions.html) | Universe | 2 | 0 |
| [Element and Operator Representations: The Three Actions](../articles_physics/the-element-and-operator-representations.html) | Physical Interpretation of Mathematics | 0 | 0 |
| [Noether's Theorem in Biquaternionic Form](../articles_physics/noethers-theorem-in-biquaternionic-form.html) | Relativity | 2 | 0 |
| [The Spinor Representation of the Lorentz Group in Biquaternionic Form](../articles_physics/the-spinor-representation-of-the-lorentz-group-in-biquaternionic-form.html) | Relativity | 2 | 0 |
| [Biquaternion Representation of Spin One Half and the Relativistic One-Electron Atom](../articles_physics/biquaternion-representation-of-spin-one-half-and-the-relativistic-one-electron-atom.html) | Relativistic Quantum Theory | 2 | 0 |
| [Bhabha Scattering in Biquaternionic Form](../articles_physics/bhabha-scattering-in-biquaternionic-form.html) | Relativistic Quantum Theory | 1 | 0 |
| [The Scalar Field in the Centre: Why Spin 0 Escapes the Biquaternion State Module](../articles_physics/the-scalar-field-in-the-centre-why-spin-0-escapes-the-biquaternion-state-module.html) | Relativistic Quantum Theory | 1 | 0 |
| [Dual Equivalence of the Dirac and Topological Massive Gauge Fields](../articles_physics/dual-equivalence-of-the-dirac-and-topologically-massive-gauge-fields.html) | Relativistic Quantum Theory | 1 | 0 |
| [The S-Matrix in Biquaternionic Form](../articles_physics/the-s-matrix-in-biquaternionic-form.html) | Quantum Fields | 2 | 0 |
| [Canonical Quantization of the Biquaternion Rarita–Schwinger Field](../articles_physics/canonical-quantization-of-the-biquaternion-rarita-schwinger-field.html) | Quantum Fields | 2 | 0 |
| [The LSZ Reduction Formula in Biquaternionic Form](../articles_physics/the-lsz-reduction-formula-in-biquaternionic-form.html) | Quantum Fields | 1 | 0 |
| [The Trace Anomaly in Biquaternionic Form](../articles_physics/the-trace-anomaly-in-biquaternionic-form.html) | Quantum Fields | 1 | 0 |
| [The Index Theorem and the Zero-Mode Count in Biquaternionic Form](../articles_physics/the-index-theorem-and-the-zero-mode-count-in-biquaternionic-form.html) | Particle Physics and Gauge Fields | 2 | 0 |
| [The Theta Parameter and Strong CP in Biquaternionic Form](../articles_physics/the-theta-parameter-and-strong-cp-in-biquaternionic-form.html) | Particle Physics and Gauge Fields | 2 | 0 |
| [The W and Z Bosons in Biquaternionic Form](../articles_physics/the-w-and-z-bosons-in-biquaternionic-form.html) | Particle Physics and Gauge Fields | 2 | 0 |
| [Confinement and the Loss of Partonic Information in Biquaternionic Form](../articles_physics/confinement-and-the-loss-of-partonic-information-in-biquaternionic-form.html) | Particle Physics and Gauge Fields | 2 | 0 |
| [Bhabha Multi-Mass Wave Equations and the Bivector Space in Biquaternionic Form](../articles_physics/bhabha-multi-mass-wave-equations-and-the-bivector-space-in-biquaternionic-form.html) | Particle Physics and Gauge Fields | 1 | 0 |

## Part II — The Replacement Question

### Three Meanings of Replacement

A replacement can mean three different things, and the corpus's negative result is true for two of them.

1. **Element replacement.** Replace each odd Clifford element by an element of $\mathbb{B}$. Impossible: the odd part is not in $\mathbb{B}$, and no product of even elements is odd.
2. **Action replacement.** Replace the gamma matrices by operations on the biquaternion carrier. Possible, and no new symbol is needed. In the real-linear frame $\gamma^0=\varkappa$ and $\gamma^k=\varkappa L_{-i\vec e_k}$, with $\varkappa$ the coefficient conjugation; the carrier stays $\mathbb{B}$, eight real, and the algebra of operators is isomorphic to $\mathrm{Cl}_{1,3}$. In the complex-linear frame $\gamma^0=T_{1,i\vec e_x}$, $\gamma^k=T_{i\vec e_k,\vec e_y}$, $\gamma_5=T_{1,-i\vec e_z}$; the carrier is the enveloping algebra, and the gammas are four tensor-basis elements. The two frames are the same Clifford algebra; they differ in whether the coefficient $i$ is the quantum complex structure.
3. **Derivation replacement.** Derive the Clifford algebra, its odd sector and its classification from $\mathbb{B}$ alone. Impossible: the odd sector is an independent real structure, and the classification theorems are theorems about $\mathrm{Cl}$, not about $\mathbb{B}$.

The useful replacement is the second. It preserves the physics because it is an isomorphism of algebras; it changes the notation because the generators are no longer matrices. The first and third are the senses in which the audit's "no replacement" is correct. The second is the sense in which the answer is yes.

### The Odd Extension: $\mathbb{B}\oplus\mathbb{B}\gamma$

This section describes the clean presentation of the odd sector. It is **not** needed for the physics: the biquaternion product carries the even sector and the chirality, and the star carries the antilinear operations. The double is the natural presentation when the odd sector is the subject, and it is the form the superalgebra article uses. §*The Gamma Matrices as Biquaternion Operations* gives the operator form.

The corpus already contains the algebra. *The Superalgebra Reading and the Odd Extension* states that one odd generator suffices: $\mathrm{Cl}_{1,3}=\mathbb{B}\oplus\mathbb{B}\gamma$. What it does not state in the form needed here is the multiplication rule and the dictionary of the four generators. They are as follows.

**Theorem (the graded biquaternion form of $\mathrm{Cl}_{1,3}$).** Let $\gamma$ be an odd generator with
$$
\gamma^2=e_t,\qquad \gamma b=\bar b\,\gamma\quad(b\in\mathbb{B}),
$$
where $\bar b$ is the coefficient conjugation of $\mathbb{B}$, not the Dirac adjoint, and define on $\mathbb{B}\oplus\mathbb{B}\gamma$ the product
$$
(a+b\gamma)(c+d\gamma)=\bigl(ac+b\bar d\bigr)+\bigl(ad+b\bar c\bigr)\gamma .
$$
Then $\mathbb{B}\oplus\mathbb{B}\gamma\cong\mathrm{Cl}_{1,3}(\mathbb{R})$, with the generators
$$
\boxed{\;\gamma^0=\gamma,\qquad \gamma^k=i\vec e_k\,\gamma\quad(k=x,y,z)\;}
$$
and the volume element
$$
\omega=\gamma^0\gamma^1\gamma^2\gamma^3=\pm i.
$$
In the ordering above it is $+i$. The even part is $\mathbb{B}$; the odd part is $\mathbb{B}\gamma$. The element $i$ is the central imaginary of $\mathbb{B}$, and it is **not** central in the full algebra:
$$
i\gamma=-\gamma i.
$$
The centre of the full algebra is $\mathbb{R}$.

*Proof.* The product is the crossed product of $\mathbb{B}$ by the order-two automorphism $\varkappa(b)=\bar b$, so it is associative. The generators satisfy
$$
(\gamma^0)^2=e_t,\qquad (\gamma^k)^2=-e_t,\qquad \gamma^0\gamma^k+\gamma^k\gamma^0=0,\qquad \gamma^j\gamma^k+\gamma^k\gamma^j=-2\delta_{jk}e_t ,
$$
as follows from $\gamma b=\bar b\gamma$ and $\vec e_j\vec e_k+\vec e_k\vec e_j=-2\delta_{jk}e_t$. The volume element is central in $\mathbb{B}$ and anticommutes with every generator, since it is the product of all four. The algebra has real dimension $16$, and the relations are the defining relations of $\mathrm{Cl}_{1,3}$; the universal property gives the isomorphism. For the centre, an element $a+b\gamma$ that commutes with every element of $\mathbb{B}$ has $b=0$ and $a\in\mathbb{C}$; commuting with $\gamma$ then forces $a=\bar a$, so $a\in\mathbb{R}$. The non-centrality of $i$ is the rule $\gamma i=\bar i\gamma=-i\gamma$. $\square$

The theorem was checked on the eight-real basis: the product is associative on random elements, the four generators satisfy $\{\gamma^\mu,\gamma^\nu\}=2g^{\mu\nu}$ with $g=\mathrm{diag}(+1,-1,-1,-1)$, the volume element is $i$ in the ordering above, and it anticommutes with all four generators. The check is elementary and is recorded because the signs are easy to get wrong.

**What the theorem buys.** The four $4\times4$ gamma matrices are replaced by one odd unit $\gamma$ and the three biquaternion units $i\vec e_k$. The $4\times4$ matrix algebra is replaced by the $2\times2$ biquaternion multiplication table. The algebra is still sixteen-real-dimensional; the odd sector is still there, but it is **one generator**, not four matrices. The physical operations are read in this algebra, up to the phases fixed by the dictionary:

| Clifford object | biquaternion form in $\mathbb{B}\oplus\mathbb{B}\gamma$ |
|---|---|
| $\gamma^0$ | $\gamma$ |
| $\gamma^k$ | $i\vec e_k\gamma$ |
| $\gamma^0\gamma^k$ | $-i\vec e_k$ (even) |
| volume element $\omega$ | $\pm i$ (even; the chirality operator up to the convention sign) |
| even part | $\mathbb{B}$ |
| odd part | $\mathbb{B}\gamma$ |
| centre | $\mathbb{R}$ |

The chirality operator needs a word of caution. In the real algebra the volume element is an even element with $\omega^2=-1$; the physical chirality involution is the complexification $i_{\mathrm{ext}}\omega$, and the external $i_{\mathrm{ext}}$ is not the biquaternion scalar $i$ that represents $\omega$. The corpus fixes the relation in *The Dirac Algebra and Biquaternions — A Dictionary*; the replacement theorem is independent of the sign, but every rewrite must use the dictionary's convention and must not conflate the two $i$'s.

**The price of the double.** The double keeps the odd sector as an *element*. The carrier is $\mathbb{B}$ (eight real) and the odd slot is $\mathbb{B}\gamma$ (eight real); the full algebra is sixteen real. The $4\times4$ matrix representation is gone, but one odd symbol remains. The physics is preserved by the isomorphism; the interpretation changes: the gamma matrices are no longer a matrix representation of vectors, they are one odd unit times biquaternion elements.

### The Gamma Matrices as Biquaternion Operations

The odd symbol is not necessary for the physics. The product alone carries the even sector; the star is added only where an antilinear operation appears. On $\mathbb{B}$ define the coefficient conjugation $\varkappa(b)=\bar b$ and the left multiplication $L_a(b)=ab$. Then
$$
\Gamma^0=\varkappa,\qquad \Gamma^k=\varkappa L_{-i\vec e_k}=L_{i\vec e_k}\varkappa
$$
are real-linear operators on $\mathbb{B}$. They satisfy the Clifford relations
$$
(\Gamma^0)^2=\mathrm{id},\qquad (\Gamma^k)^2=-\mathrm{id},\qquad \Gamma^\mu\Gamma^\nu+\Gamma^\nu\Gamma^\mu=2g^{\mu\nu}\mathrm{id},
$$
and the sixteen products $\mathrm{id}$, $\Gamma^\mu$, $\Gamma^\mu\Gamma^\nu$, $\Gamma^\mu\Gamma^\nu\Gamma^\rho$, $\Gamma^0\Gamma^1\Gamma^2\Gamma^3$ are linearly independent. The carrier is $\mathbb{B}$ (eight real), the even operators are $L(\mathbb{B})$, the odd operators are $\varkappa L(\mathbb{B})$, and no symbol is added. The star is part of the biquaternion structure, not an extra import: it is the coefficient conjugation that distinguishes $\mathbb{B}=\mathbb{C}\otimes\mathbb{H}$ from $\mathbb{H}$. The identification of this left-regular model with the physical Dirac module $\Delta=S\oplus S^{\mathrm{c}}$ is the real-linear Daviau dictionary of §*The Bimodule Reading*, not the identity; the model is isomorphic to $\Delta$ as a $\mathrm{Cl}$-module, but the isomorphism is not $\mathbb{B}$-linear.

This was checked on the eight-real basis: the relations hold and the sixteen products have rank sixteen. The symbol $\varkappa$ is the coefficient conjugation; it is not the corpus's $J=L_{-i}$, the complex structure.

**Which complex structure, and which completion.** The $i_{\mathrm{ext}}$ of the table cannot be the coefficient $i$. With $\omega=L_i$ one has $i\omega=-1$, so that frame has no chirality. The chirality $R_{i\vec e_z}$ is $J\omega$ for the complex structure $J=R_{\vec e_z}$, which commutes with the generators and satisfies $J^2=-1$; the corpus's $J=L_{-i}$ equals $-\omega$, so $J\omega=1$, while $i\omega=-1$. The choice of $J$ is a choice of a real unit vector, $J=R_u$ with $u^2=-1$.

A dictionary that is complex-linear in the coefficient $i$ uses a right multiplication for the fourth generator instead. On $\mathbb{B}$ with the spin index on the rows and the chirality index on the columns,
$$
\gamma^0=R_{i\vec e_x},\qquad \gamma^k=L_{i\vec e_k}R_{\vec e_y},\qquad \gamma_5=R_{-i\vec e_z},
$$
where $\vec e_y$ is the chirality-space epsilon: on the chirality index, $R_{\vec e_y}$ is $i\sigma_y$. There the volume element is $\omega=L_iR_{i\vec e_z}$, not $L_i$, and $i\omega=\gamma_5$. The two frames are isomorphic as real Clifford modules and differ in which structure is manifest: the frame above makes the real algebra and the odd sector manifest, this one the complex Dirac equation and its chiral projectors.

**The tensor basis.** The four generators are single elements of the tensor basis of $\operatorname{End}_{\mathbb{C}}(\mathbb{B})$:
$$
\gamma^0=i\,T_{e_t,e_x},\qquad \gamma^k=i\,T_{e_k,e_y},\qquad \gamma_5=-i\,T_{e_t,e_z}.
$$
They are not sums, and they are not sandwiches. The sixteen operators $T_{e_\mu,e_\nu}$ are a basis of the operator algebra; in the coefficient matrix representation they are sixteen signed permutation matrices, and in the Peirce basis they are monomial with entries in $\{1,-1,i,-i\}$; the matrix units there are the sixteen products $L_{P_i}R_{P_j}$ of the four Peirce elements. The four generators are four of them up to the scalar $i$; $\gamma_5$ is a fifth, and the products of the generators, including the identity, give the remaining eleven. The simplicity of the gammas — one nonzero entry per row and per column — is a property of the coefficient basis; in the Peirce basis the same gammas are sums of matrix units.

**Three levels, not one.** The **operator algebra** is the abstract object: $\mathcal{E}=\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}$, generated by the two-sided operators, with the isomorphism $\mathcal{E}\to\operatorname{End}_{\mathbb{C}}(\mathbb{B})$, $a\otimes b\mapsto L_aR_b$. The **matrix representation** is $M_4(\mathbb{C})$, obtained by choosing a basis of $\mathbb{B}$; the coefficient basis gives the tensor matrices $T_{e_\mu,e_\nu}$, the Peirce basis the matrix units $L_{P_i}R_{P_j}$. The **carrier** is $\mathbb{B}\cong\mathbb{C}^4$, on which the operators act. $M_4(\mathbb{C})$ is the matrix representation of the operator algebra — not a different algebra, and not the carrier.

**Building the sixteen from the four.** The article *$M_4(\mathbb{C})_L$ Model : The Product, the Trace and the Determinant* gives the four left matrices $L_\mu=\mathsf M_4^L(e_\mu)$. The right matrices follow from $R_b=D\,L_{b^{\natural}}\,D$ with $D=\mathrm{diag}(1,-1,-1,-1)$: $R_t=I_4$ and $R_k=-D\,L_k\,D$ for $k=x,y,z$. Then
$$
T_{\mu\nu}=L_\mu R_\nu,\qquad \mu,\nu\in\{t,x,y,z\},
$$
are sixteen distinct signed permutation matrices, linearly independent, a basis of the matrix representation; in the Peirce basis they remain monomial, with entries in $\{1,-1,i,-i\}$. The tensor product of two $4\times4$ matrices is $16\times16$ and is not this construction; the Kronecker product appears at the $M_2$ level, $T_{a,b}=S\bigl(\mathsf M_2(b)^{\mathsf T}\otimes\mathsf M_2(a)\bigr)S^{-1}$, where $S$ is the Peirce change of the model article, with columns $\tilde\Pi_+,\vec\Upsilon_+,\vec\Upsilon_-,\tilde\Pi_-$ and $\det S=-\tfrac14$, and $S^{-1}$ carries the coefficients $(Q_t,Q_x,Q_y,Q_z)$ to $\mathrm{vec}\,\mathsf M_2(\tilde Q)$. The assignment is a **Clifford frame**: a choice of four anticommuting elements of the tensor basis, not an intrinsic structure of the two-sided family. The biquaternion structure fixes the frame up to a rotation of the spatial triple $(\vec e_x,\vec e_y,\vec e_z)$; the rotation is an algebra automorphism and carries one frame to an equivalent one. The construction is written out, with the sixteen matrices tabulated and checked, in *$M_4(\mathbb{C})_L$ Representation : The Two-Sided Operators on the Biquaternion Algebra*.

The algebra of this dictionary is the operator algebra, not one regular image. $L(\mathbb{B})$ and $R(\mathbb{B})$ have complex dimension four each and meet in the scalars, since $L_{e_t}=R_{e_t}=1$, so their sum is seven-dimensional. Their products span the operator algebra $\mathbb{B}\otimes\mathbb{B}^{\mathrm{opp}}$, whose matrix representation is $M_4(\mathbb{C})$, of complex dimension sixteen (real dimension thirty-two): on the Peirce basis the sixteen products $L_{P_i}R_{P_j}$ are the sixteen matrix units. This is why the gammas are $4\times4$, and why neither regular image alone can hold them. The corpus's $M_4(\mathbb{C})_L$ tables are the left factor; in the Peirce basis that image is $\mathrm{diag}(\mathsf M_2(b),\mathsf M_2(b))$, block diagonal, so it preserves the two chiral planes. The gammas exchange the planes and therefore lie outside it.

**The double is the same algebra, written as a direct sum.** $\mathbb{B}\oplus\mathbb{B}\gamma$ is convenient when an article needs the odd sector as an *element*: the supercharge, the graded algebra, a Dirac operator written as one object. It makes the grading manifest. It is not needed for the physics: every odd operator is $\varkappa L_b$, and every product of two odd operators is
$$
(\varkappa L_b)(\varkappa L_c)=L_{\varkappa(b)}\,\varkappa\,\varkappa\,L_c=L_{\varkappa(b)c},
$$
an even operator. The double buys one symbol and a direct-sum notation; it does not buy a physical result that the operator form cannot reach. The price of the double is the extra symbol and the sign conventions; the price of the operator form is that the odd generators are real-linear and antilinear, not elements.

| Clifford object | double $\mathbb{B}\oplus\mathbb{B}\gamma$ | operator on $\mathbb{B}$ |
|---|---|---|
| $\gamma^0$ | $\gamma$ | $\varkappa$ |
| $\gamma^k$ | $i\vec e_k\gamma$ | $\varkappa L_{-i\vec e_k}=L_{i\vec e_k}\varkappa$ |
| even part | $\mathbb{B}$ | $L(\mathbb{B})$ |
| odd part | $\mathbb{B}\gamma$ | $\varkappa L(\mathbb{B})$ |
| volume element | $\pm i$ (even) | $L_i$ (up to sign) |
| chirality | $i_{\mathrm{ext}}\omega$ | $R_{i\vec e_z}$ (up to sign) |

The right action $R(\mathbb{B})$ is not in the sixteen-dimensional algebra generated by $\varkappa$ and $L$; it is the commutant, and it supplies the chirality. The full carrier is $\mathbb{B}$ with $L$, $R$ and $\varkappa$.

The double and the operator form present the same Clifford algebra; the chirality is carried by the right action in the operator form and by the complexified volume element in the double. The rest of this article uses the double when it speaks of odd *elements* and the operator form when it speaks of odd *operations*. The distinction is the one §*Element, Operation, Carrier* makes.

### The Bimodule Reading: Chirality Is a Right Action

The Dirac spinor is not $\mathbb{B}$ as the left-regular module. It is the four-complex-dimensional module $\Delta=S\oplus S^{\mathrm{c}}$, on which $\mathbb{B}$ acts by $b$ on $S$ and by $\bar b$ on $S^{\mathrm{c}}$; the real-linear dictionary of the Daviau article identifies $\Delta$ with $\mathbb{B}$ (eight real). Under that dictionary the left action becomes a real-linear action on $\mathbb{B}$, and the right multiplication $R_{i\vec e_z}$ becomes the chirality. The algebra of complex-linear operators on $\mathbb{B}$ is $\mathbb{B}\otimes_\mathbb{C}\mathbb{B}^{\mathrm{opp}}\cong M_4(\mathbb{C})$; the left and right multiplications generate it. This is the precise sense in which $\mathbb{B}$ is a bimodule: it carries the operator algebra, not the left-regular representation of the spinor. The corpus's *Enveloping Operator Algebra* article proves this; the *Daviau Map* article uses it; the *Chiral Algebra* article reads the right action as the second chirality.

The dictionary in the bimodule picture is:

| Clifford object | biquaternion operation |
|---|---|
| $\gamma^0$ | $\varkappa$ (the star) |
| $\gamma^k$ | $J L_{-i\vec e_k}=L_{i\vec e_k}J$ |
| $\gamma^5$ | $R_{i\vec e_z}$ on $\mathbb{B}$ (the image of the grading on $\Delta$, up to the volume-element sign) |
| chiral projectors | $R_{(e_t\pm i\vec e_z)/2}$ |
| Lorentz action | the left action of $\mathbb{B}$ on $\Delta$ ($b$ on $S$, $\bar b$ on $S^{\mathrm{c}}$), a real-linear action on $\mathbb{B}$ under that dictionary |
| mass | $m\,\varphi^{*}$ (Daviau) or the off-diagonal chiral pairing |
| Dirac adjoint | the star composed with the Hermitian conjugation; a real-linear pairing |
| trace | the pair of Dirac traces (vector and axial) on $\Delta=S\oplus S^{\mathrm{c}}$, not the regular trace alone |

The trace is the delicate entry. The regular trace on $\mathbb{B}$ is the complex-linear trace of the left-regular representation: for $b=a_0+a_1\vec e_x+a_2\vec e_y+a_3\vec e_z$ it is $4a_0$, so the central $i$ has trace $4i$. On the Dirac module $\Delta=S\oplus S^{\mathrm{c}}$ the vector trace is $4\operatorname{Re}a_0$ and the axial trace with $\gamma_5$ is $4i\operatorname{Im}a_0$ (up to the overall sign of $\gamma_5$). The regular trace is their sum:
$$
\operatorname{Tr}_{\mathrm{reg}}(b)=\operatorname{Tr}_{\Delta}(b)+\operatorname{Tr}_{\Delta}(b\gamma_5).
$$
The central $i$ acts on $\Delta$ as $i\gamma_5$ and is traceless there. The anomaly articles need the pair (vector, axial), not the regular trace alone: using $\operatorname{Tr}_{\mathrm{reg}}$ as the $\gamma_5$ trace adds the vector part. The odd operators have zero trace in either trace.

**The correction to O22.** The obstruction catalogue states that "multiplication is chirality-blind" and that "a multiplication acts on the two chiral components with the same matrix." The conclusion — the chiral gauge structure is an import — is correct, but the wording is too strong.

- Left multiplication by $b$ on the Dirac module $\Delta=S\oplus S^{\mathrm{c}}$ acts as $b$ on $S$ and as $\bar b$ on $S^{\mathrm{c}}$. It is block diagonal and preserves each chiral half; it does not act with the same matrix on both, and it does not exchange them.
- Right multiplication supplies the chirality projectors and the mass pairing; it is not blind.
- What $\mathbb{B}$ does not supply is an **independent chiral gauge action** beyond the Lorentz action and its conjugate. The electroweak $SU(2)_L$ is an external gauge group in the Clifford approach as well; the replacement does not change that.

The correct statement is therefore: *left multiplication is chirality-preserving and cannot exchange the two halves; the full bimodule action is not chirality-blind; the chiral gauge group is an import.* The proof of O22 should be revised to use the Dirac module $S\oplus S^{\mathrm{c}}$, not the left-regular module $S\oplus S$.

### The Operator Vocabulary: Four Operator Types

Two different objects carry the name **two-sided** in the corpus, and **sandwich** has three senses; the Clifford layer inherits the confusion. The distinction is not cosmetic: it decides whether a rewrite has added a parameter that the physics does not have.

- The **two-sided operator** of a pair $(a,b)$ is $T_{a,b}(x)=a\,x\,b$. It has two independent parameters, it is bilinear in them, the sixteen $e_\mu[\,]e_\nu$ span the operator algebra $\mathbb{B}\otimes_{\mathbb{C}}\mathbb{B}^{\mathrm{opp}}\cong\mathrm{End}_{\mathbb{C}}(\mathbb{B})$, whose matrix representation in a basis of $\mathbb{B}$ is $M_4(\mathbb{C})$, composition reverses the pair, and every type criterion is a criterion on the pair: self-adjoint iff $b=\lambda a$; the form-preserving and multiplicative criteria are criteria on the product, $ba=\pm e_t$ and, for a nonzero operator, $ab=e_t$. The overview is *Two-Sided Operators on the Biquaternion Algebra*.
- The **sesquilinear sandwich** of a pair $(a,b)$ is $S_{a,b}=T_{a,b}\circ\varkappa$, that is $x\mapsto ax^{*}b$. The star acts on the argument; the two parameters are free. It is not an elementary tensor of the enveloping algebra: it is the two-sided operator composed with the star. The article is *The Sesquilinear Sandwich on the Biquaternion*.
- The **bilinear sandwich** of one element $Q$ is $\Theta_Q=T_{Q,Q^{*}}$, that is $x\mapsto QxQ^{*}$, or $X\mapsto MXM^{\dagger}$ in the matrix model. **It is the default: an article that writes *the sandwich* with no qualifier means this operator.** The qualifier *bilinear* names the family from which it is cut, the bilinear family $T_{a,b}$; it does not say that the operator is bilinear in $Q$, which it is not. The sector articles call it simply the **sandwich**, and the Hermitian-algebra layer calls the same operator the **Hermitian sandwich**. It has one parameter and is quadratic in it, $\Theta_{\lambda Q}=\lvert\lambda\rvert^{2}\Theta_Q$; the star is on the second parameter. It is the conformal Lorentz congruence, and its type criteria are criteria on $Q^{*}Q$. The six sector articles are *The Sandwich of a ... Biquaternion*.
- The **inner conjugation** of one element $Q$ is $T_{Q,Q^{-1}}$, that is $x\mapsto QxQ^{-1}$. The inverse sits in the second slot. It is an algebra automorphism for every unit, and the Pin reflection is its odd instance, $\rho_u(v)=-uvu^{-1}$ up to the sign $\epsilon(u)$.

A statement about one bivector or one spinor acting by $Q(\cdot)Q^{*}$ is a bilinear-sandwich statement, not a generic two-sided statement, because the second parameter is tied to the first by the star. The bilinear-sandwich family is the image of the graph $b=Q^{*}$ inside the eight-complex-dimensional pair; it is a real cone of dimension seven, and the Lorentz group is a three-complex-dimensional subgroup of it. The full operator algebra is the span of the two-sided family by linear combination, not the two-sided family itself: the family is the cone of decomposable tensors, of complex dimension seven (real dimension fourteen).

**The Clifford translation.** The gamma matrices have two completions, and they must not be conflated. In the real-linear frame the dictionary uses the star and left multiplications, $\gamma^0=\varkappa$ and $\gamma^k=\varkappa L_{-i\vec e_k}$ on the eight-real-dimensional $\mathbb{B}$. In the complex-linear frame it uses single two-sided operators,
$$
\gamma^0=T_{1,\,i\vec e_x},\qquad \gamma^k=T_{i\vec e_k,\,\vec e_y},\qquad \gamma_5=T_{1,\,-i\vec e_z},
$$
which are, up to the scalar $i$, five of the sixteen tensor-basis operators $T_{e_\mu,e_\nu}$. This frame keeps the coefficient $i$ as the quantum complex structure and the chiral projectors manifest. The gammas are **not sandwiches**: a sandwich is $T_{Q,Q^{*}}$, whose second slot is tied to the first, and every sandwich preserves the Hermitian sector $\mathbb{M}_+$; the gamma frame needs the second slot free, the gammas do not preserve the Hermitian sector, and they generate the full $M_4(\mathbb{C})$. The Lorentz congruence on the algebra is the sandwich; the spinor action is the gamma frame. Promoting a gamma to a two-parameter family $L_aR_b$ with free $a,b$ adds a parameter; the gamma itself is the single member whose pair is fixed by the index. The Pin reflection remains an inner conjugation, $\rho_u(v)=-uvu^{-1}$, not an element of the even algebra.

**What was renamed.** The six sector articles now carry *The Sandwich* in their titles, not *The Two-Sided Operator*:

| old title | new title |
|---|---|
| The Two-Sided Operator of a N-Regular, Spectrally Regular Biquaternion | The Sandwich of a N-Regular, Spectrally Regular Biquaternion |
| The Two-Sided Operator of a N-Regular, Spectrally Degenerate Biquaternion | The Sandwich of a N-Regular, Spectrally Degenerate Biquaternion |
| The Two-Sided Operator of a N-Degenerate, Spectrally Regular Biquaternion | The Sandwich of a N-Degenerate, Spectrally Regular Biquaternion |
| The Two-Sided Operator of a N-Degenerate, Spectrally Degenerate Biquaternion | The Sandwich of a N-Degenerate, Spectrally Degenerate Biquaternion |
| The Two-Sided Operator Exponential of a N-Regular, Spectrally Regular Biquaternion | The Sandwich Exponential of a N-Regular, Spectrally Regular Biquaternion |
| The Two-Sided Operator Exponential of a N-Regular, Spectrally Degenerate Biquaternion | The Sandwich Exponential of a N-Regular, Spectrally Degenerate Biquaternion |

The new titles use the sector's short name: the object is the bilinear sandwich $\Theta_Q=T_{Q,Q^{*}}$, not the sesquilinear sandwich $S_{a,b}(X)=aX^{*}b$. The operator's own name changed with them: what an earlier draft called the *dagger sandwich* is now the *bilinear sandwich*, in the articles and in the menus. The same correction was applied to *The Approaches to Spin: Weight, Half-Angle, Ladder and Adjoint*, *The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure*, *Bilinear Operators on the General Plain Sesqualgebra*, *The Four Adjoints of the Biquaternion Algebra in Examples*, and *Exercise: Plane-Wave Solutions of the Biquaternion Dirac Equation*.

The overview *Two-Sided Operators on the Biquaternion Algebra* was rewritten to define the family, its composition, its adjoint, the type criteria, the bilinear sandwich as its diagonal, and the isometry group. The conventions table now records $T_{\tilde Q_1,\tilde Q_2}$ with positional subscripts and $\Theta_{\tilde Q}=T_{\tilde Q,\tilde Q^{*}}$.

**What keeps the name.** The articles that study $T_{a,b}$ itself keep *two-sided*: the two-sided operators on the general plain sesqualgebra, on a Clifford algebra, on a Hermitian algebra, with the signed product, and the reflections as signed two-sided operators. The one-sided articles keep *one-sided*. The general-algebra articles of Part I call $T_{a,b}$ itself a *two-sided sandwich*; that is the two-sided operator under the older name. The general quaternionic articles call the distinguished member $\Theta_{\tilde Q_6}=L_{\tilde Q_6}R_{\tilde Q_6^{\natural}}$ a *twisted two-sided operator*; that is a bilinear sandwich with the natural conjugation in place of the star. The reservation of *sandwich* for the one-element bilinear case is the convention of the biquaternion operator layer. No article uses *dagger sandwich* as a name: the symbol $\dagger$ is the adjoint, in the matrix model and on the operators, and it is never part of an operator's name. The test is one question: where is the star, and what sits in the second slot? A star in the second slot gives the bilinear sandwich $\Theta_Q$; an inverse gives the inner conjugation $T_{Q,Q^{-1}}$; a free parameter with no star gives the two-sided operator $T_{a,b}$. If the star is on the argument, the operator is the sesquilinear sandwich $S_{a,b}=T_{a,b}\circ\varkappa$. In the regular sector the bilinear sandwich is the diagonal $\Theta_Q=T_{Q,Q^{*}}$, with the second parameter tied to the first. The general sesquilinear sandwich $S_{a,b}$ of *The Sesquilinear Sandwich on the Biquaternion* is a different operator: its star is on the argument, and it keeps both parameters free. The biquaternion layer's unqualified *sandwich* is the bilinear sandwich; the Part I *two-sided sandwich* is the ordinary $T$.

### Possible Routes to Migrate from Clifford to the Biquaternion Algebra

**Remark (the answer in one line).** Six routes are available. **B** is the biquaternion product with left and right multiplication; it covers the field, the equation, the bilinears, the chiral projectors and the traces. **C** adds the star, and is needed only for the antilinear operations. **D** adds one symbol and is a *presentation* of the same algebra, used when the odd element is the subject. The route is fixed by the operation the article performs, not by its family.

| route | algebra / carrier | new symbol? | captures | does not capture | use |
|---|---|---|---|---|---|
| A left regular | $\mathbb{B}$ acting on itself | no | even sector, Lorentz, gauge, mass | chirality, odd operations, Dirac adjoint | the current "$\mathbb{B}$-valued field" articles |
| B bimodule | $\mathbb{B}$ with $L$ and $R$ | no | even sector, chirality, $\gamma_5$, traces, mass pairing | antilinear $P/C/T$, odd operators | most of the physics |
| C $\mathbb{B}$ + star | $\mathbb{B}$ with $L$, $R$, $\varkappa$ | no | full $\mathrm{Cl}_{1,3}$ action: odd operators $\varkappa L_b$, $P$, $C$, $T$, Dirac adjoint | derivation of the gauge group; odd elements as elements | the star, for antilinear operations |
| D graded double | $\mathbb{B}\oplus\mathbb{B}\gamma$ | yes ($\gamma$) | the odd sector as an element, the graded algebra | $\mathbb{B}$-only purity | presentation for the superalgebra articles |
| E complexified $\mathbb{B}[j]$ | $\mathbb{B}[j]\cong\mathbb{B}\oplus\mathbb{B}$ | no | central chirality, chiral projectors, mass pairing | the odd sector | a chiral presentation; equivalent to $\mathbb{B}$ for the traces |
| F keep $\mathrm{Cl}$ | $\mathrm{Cl}_{1,3}$ | no | everything | $\mathbb{B}$-only purity | structural and classification articles |

The recommendation is route B for the product, route C for the star, route D only where the odd element is the subject, route E where the central chirality is the subject, and route F where the Clifford algebra is the subject. Route C is not a better B: it is B with the star turned on for the articles that perform an antilinear operation. Route D is a presentation of C, not a stronger route.

The article-by-article assignment is in §*The Split: What Can Be Rewritten, and What Cannot*.

### Does Any Article Need the Odd Generator?

No. The odd generator is needed only when the odd sector must be an *element*: the supercharge, the graded algebra, a Dirac operator written as one object. Two articles use it that way, and both are about the graded algebra; even they can be written in the operator form. The other forty-nine do not need it: thirty-two can be written with the product, adding the star only where an antilinear operation appears, and seventeen keep the Clifford algebra for their subject or their theorem. §*The Split: What Can Be Rewritten, and What Cannot* gives the article-by-article assignment.

**What changes in practice.** In the B route, the four $4\times4$ gamma matrices disappear into the product: the field, the bilinears and the projectors are products, and chirality is $R_{i\vec e_z}$. Where the article applies an odd generator or the adjoint, the star is added: $\gamma^0=\varkappa$, $\gamma^k=\varkappa L_{-i\vec e_k}$. In the D presentation, they become one odd unit $\gamma$ and the three biquaternion units $i\vec e_k$. The matrix algebra becomes the $2\times2$ biquaternion multiplication table. In D the chirality is the volume element up to the convention sign; in B and C it is $R_{i\vec e_z}$. The trace becomes the pair of vector and axial Dirac traces on $\Delta=S\oplus S^{\mathrm{c}}$, not the regular trace alone. The signs to fix are: $\varkappa(b)=\bar b$, $\omega=\pm i$, and the external $i$ of the chirality involution, which is not the biquaternion scalar $i$.

**What does not migrate.**

- The classification of the Clifford algebras $\mathrm{Cl}_{p,q}$ is a theorem about $\mathrm{Cl}$, not about $\mathbb{B}$.
- The index theorem and the Fredholm index are invariants of the Dirac module; a biquaternion computation can reproduce them, not derive them from $\mathbb{B}$ alone.
- The gauge group is external in both presentations. The replacement does not make $SU(2)_L$ or $SU(3)$ an element of the algebra.
- The $\mathbb{Z}$-grading is not manifest. $\mathbb{B}\oplus\mathbb{B}\gamma$ carries only the parity grading, so the split of the odd part into four vectors and four trivectors is recovered from the dictionary, not from the biquaternion product. The vector subspace survives; its display does not.

### What Is Preserved

| physical result | route | note |
|---|---|---|
| Dirac equation, mass shell, plane waves | A/B/C | the isomorphism preserves the equation |
| Lorentz covariance | A/B/C | the left action of the rotor on the module |
| chirality, chiral projectors | B/C/E | right multiplication or the central sign |
| parity, charge conjugation, time reversal, $CPT$ | C | odd operators $\varkappa L_b$; the exact phases are convention-dependent |
| Dirac adjoint and bilinears | C | star and Hermitian conjugation; real-linear |
| axial anomaly and $\gamma_5$ traces | B/C/E | the trace must be recomputed; the pair of vector and axial Dirac traces on $\Delta$ is the candidate, not the regular trace alone |
| spin–statistics | B/C | the graded bracket on the mode operators; $(-1)^F=i\vec e_z\in\mathbb{B}$ |
| chiral gauge couplings | B/E | the chiral halves are represented; the gauge group is external in both approaches |
| Pin group and reflections | C | the reflection is conjugation by $\gamma^0$, i.e. $\varkappa$ up to the sign $\epsilon(u)$; the Pin action is generated by the odd operators |
| index theorem, Clifford classification | F | a theorem about $\mathrm{Cl}$; not a $\mathbb{B}$-only result |
| Standard Model | all | transcribed, not derived; no new prediction |

The table is the answer to "does the replacement respect the physical results?" It does, for the results that are algebraic consequences of the Clifford action, because the action is isomorphic. It does not derive the inputs that the Clifford approach also imports: the gauge group, the scales, the spin–statistics theorem, the index theorem. Those remain imports in both presentations. The route column names the carrier; §*The Split: What Can Be Rewritten, and What Cannot* names the effort. An article can need C and still be hard, when its theorem is about the representation.

### Migration Order

The rewrite has a dependency order. The first step is the one the corpus is missing.

1. **Write the calculus.** Add a single article, or a long section of the dictionary, that states §*The Gamma Matrices as Biquaternion Operations*: the operator dictionary $\varkappa$, $L$ and $R$, the double as an optional presentation, the trace rules and the sign conventions. Every other article should cite it rather than repeat a gamma-matrix convention. This is the missing piece; the algebra itself is already in the corpus.
2. **Rewrite the dictionary.** *The Dirac Algebra and Biquaternions — A Dictionary* is the root. Replace the four matrices by $\varkappa$ and $\varkappa L_{-i\vec e_k}$, and keep the old matrix dictionary as a translation table for the articles not yet rewritten. The double $\mathbb{B}\oplus\mathbb{B}\gamma$ is the optional presentation for the two graded-algebra articles.
3. **Rewrite the Dirac equation and the spinor module.** These are the most cited and they fix the carrier: the bimodule, the left Lorentz action, the right chirality. The Daviau article is the model; it already writes the equation in the space-Clifford form.
4. **Settle the trace before rewriting the trace articles.** *The Fujikawa Method* and *Anomalies and Anomaly Cancellation* are research tasks, not substitutions: the biquaternion trace, the real-linear determinant and the factor of two must be computed and checked against the known coefficient. Until that check exists, leave them in $\mathrm{Cl}$. Then rewrite the EDM, the chiral condensate, the chiral fermions and the bosonization, which use the projector and the bilinear, not the measure.
5. **Rewrite the local odd operations.** Zitterbewegung, the nonlinear Dirac equation and canonical quantization are local: the odd operator is $\varkappa L_b$ and the phase is fixed by the dictionary. *The Reflection and the Rotation*, *The CPT Theorem* and *The Spin–Statistics Theorem* stay in $\mathrm{Cl}$ as the reference; add a biquaternion section to them, not a rewrite.
6. **Keep the structural articles in $\mathrm{Cl}$.** The reflection group as a subject, the division-ring classification, the index theorem, the spectral triple, the number of generations and the left-right bioctonion model are theorems about the Clifford algebra or about a larger algebra. Add a cross-reference to the calculus; do not claim a $\mathbb{B}$-only derivation.
7. **Check every rewrite against the old computation.** The *Klein–Gordon from the Dirac Square* article is the model: it computes the same identity in both languages and compares. A rewrite that changes a physical coefficient is wrong, because the algebra is isomorphic.

### Open Questions

1. **The phases of $C$, $P$ and $T$.** The structural form is clear: $P$, $C$ and $T$ are compositions of the star $\varkappa$ with left multiplications. The exact factors, the composition rule for the anti-linear parts and the sign of $\gamma_5$ are convention-dependent and need a dedicated dictionary. The CPT article's open question about a $\mathbb{B}$-intrinsic $C$ and $P$ is answered at the level of operations, not at the level of elements; the phase dictionary is not.
2. **The trace and the measure.** The regular trace on $\mathbb{B}$ is the sum of the vector and axial Dirac traces: $\operatorname{Tr}_{\mathrm{reg}}(b)=\operatorname{Tr}_{\Delta}(b)+\operatorname{Tr}_{\Delta}(b\gamma_5)$. The Fujikawa measure, the real-linear determinant and the factor of two must be fixed before the anomaly articles can be called rewritten.
3. **The chiral gauge group.** $\mathbb{B}[j]$ represents the two chiral halves and their projectors. It does not supply an independent $SU(2)_L$; the gauge group is external in both approaches. Whether the bimodule can host the gauge action more naturally than the Clifford module is open.
4. **The index theorem and the spectral triple.** The Dirac operator in the biquaternion language, the real structure $J$, the grading and the Fredholm index are not yet written. The index is a Clifford/module invariant; a biquaternion computation should reproduce it, but the spectral-triple article is the natural test.
5. **Spin–statistics.** The star and the graded bracket on the mode operators give the anticommutation and the odd slot. The theorem itself is an import; whether the biquaternion framework can derive the spin–statistics connection, rather than transcribe it, is open.
6. **The real structure $\flat$ and the star $\varkappa$.** The corpus's Majorana-type pairing $\flat=-{}^{*}$ and the star $\varkappa$ are different maps. The relation between them, and the charge conjugation $C$ built on each, is the subject of the neutrino article and is not settled.
7. **The Pin group.** The reflection group generated by the odd operators $\varkappa L_u$ or $\gamma b$ carries the sign $\epsilon(u)$ and the determinant table. The biquaternion form of the Pin group and its relation to the versors is open.
8. **The geometric interpretation.** The $\mathbb{Z}$-grading is not manifest: $\mathbb{B}\oplus\mathbb{B}\gamma$ carries only the parity grading, so the split of the odd part into four vectors and four trivectors is recovered from the dictionary, not from the biquaternion product. The algebra still contains the vector subspace, but the presentation does not display it. Whether the framework can supply a geometric interpretation that does not pass through the dictionary is the interpretive price of the route.

### Findings

- **The audit's headline is too strong.** "The odd sector cannot be removed by notation" is true for elements and for inner operations. It is too strong for actions: the odd generators are real-linear operations on $\mathbb{B}$, $\gamma^0=\varkappa$ and $\gamma^k=\varkappa L_{-i\vec e_k}$. The correct statement is: *the odd sector cannot be removed from the algebra, but it can be carried by the product, the star and left multiplication on $\mathbb{B}$; the odd generator is a presentation, and most articles do not need it.*
- **The rewrite is not uniform.** The biquaternion formalism carries 32 of the 51 articles: the field, the equation, the bilinears, the chiral projectors and the trace of a product; the star is added only where an antilinear operation appears. The star is needed only for the antilinear operations; the odd generator only where the odd element is the subject. Nineteen cannot be rewritten without deleting their subject: twelve are about the Clifford algebra or its relation to another formalism, and seven need a trace or a representation theorem rebuilt.
- **The obstruction catalogue's O22 needs a correction.** Left multiplication is chirality-preserving, not chirality-blind; on the Dirac module it acts as $b\oplus\bar b$, not with the same matrix on both halves. Right multiplication is chirality-sensitive. The conclusion — the chiral gauge group is an import — stands.
- **The operator vocabulary is fixed.** *Two-sided* is reserved for $T_{a,b}$ with independent parameters; the single-element congruence is a *sandwich*. The six sector articles have been renamed and the overview rewritten. The mismatch was not cosmetic: it made the Lorentz congruence look like a free two-parameter family and obscured that the gamma matrices are single two-sided operators $T_{a,b}$ in the complex-linear frame — four tensor-basis elements up to the scalar $i$ — and not sandwiches. In the real-linear frame they are star and left multiplications. Neither frame makes them free two-parameter families.
- **The trace is not the regular trace.** The regular trace on $\mathbb{B}$ is the sum of the vector and axial Dirac traces, $\operatorname{Tr}_{\mathrm{reg}}=\operatorname{Tr}_{\Delta}+\operatorname{Tr}_{\Delta,\gamma_5}$. The central $i$ has trace $4i$ in the regular trace and $0$ in the vector trace. A biquaternion anomaly computation must use the pair, not the regular trace alone.
- **The physics is preserved by construction.** The replacement is an isomorphism of real algebras. The results that depend on the Clifford action are preserved; the imports (gauge group, scales, spin–statistics, index theorem) remain imports. The replacement adds no prediction and removes none; the trace bullet above is the one representation-level exception.
- **The value is a simpler presentation.** Four $4\times4$ gamma matrices become the product, with the star only for antilinear operations; in the double they become one odd unit. The matrix algebra becomes the $2\times2$ biquaternion multiplication table; the odd sector becomes explicit instead of hidden in matrices. The price is a set of sign conventions, and one symbol in the two D articles.
- **The rewrite has a clear order.** Calculus first, then the dictionary, the Dirac equation and the spinor module, then the chirality/trace articles, then the odd-operation articles. The structural articles stay in $\mathrm{Cl}$.
- **The counts measure the rewrite, not the obstruction.** 115 articles carry the layer, 51 are structural; but the number of articles that *cannot* be rewritten in the biquaternion calculus is much smaller. It is the set whose subject is the Clifford algebra itself, not the set that uses a gamma matrix.

## What the Counts Do Not Say

- **They do not report a mathematical error.** The isomorphism $\mathbb{B}\cong\mathrm{Cl}^{+}_{1,3}$ is a theorem, the dictionary is exact, and the gamma-matrix computations are correct. Nothing in the corpus is numerically wrong because of this layer.
- **They do not count every mention as a use.** Band 3 contains articles that name Clifford once, often in a comparison or a further-reading line. The working set is band 1: 51 articles.
- **They do not single out the Dirac articles.** The layer is heaviest in Relativistic Quantum Theory (36 articles, 18 in band 1), Particle Physics and Gauge Fields (29, 14) and Quantum Fields (24, 12). It is not a defect of one series.
- **They do not prescribe one route.** The odd part cannot be removed from the algebra. The product carries the even sector; the star carries the antilinear operations; the double is the subject of two articles. The counts measure the size of the rewrite, not the impossibility of one.
- **They do not distinguish the element question from the action question.** The 115 articles use the odd sector as matrices; the replacement uses the product, the star, or one generator in the double. The count of articles is not the count of obstructions.

## Conclusion

The corpus is built on two layers that are not in the algebra it names.

The first is the tensor layer: an index $\mu$, a derivative $\partial_\mu$, four components for the connection and six for the curvature. The second is the Clifford layer: a grading, four odd generators, a Pin group and a sign. The first supplies the gauge sector with an external index; the second supplies the fermion sector with an external grading. Both are outside $\mathbb{B}$, and both are used as if they were inside it. The second has a minimal biquaternion form; the first does not.

The sharpest trace is the odd sector. $\mathbb{B}$ is the even half of $\mathrm{Cl}_{1,3}$; the physics of parity, charge conjugation and reflection lives in the other half. The articles say so, in the CPT theorem, in Zitterbewegung, and above all in *The Reflection and the Rotation*, whose subject is precisely the part that the biquaternion algebra does not contain.

The replacement is not a removal. The odd sector is real, and it is the reason the biquaternion algebra is not the whole story. The replacement is local: the product for the even sector, the star for the antilinear operations, one odd unit only where the odd element is the subject. The physics is preserved because the algebra is the same. The work is to write the corpus in the smaller presentation, not to pretend the odd sector is absent.

**115 articles carry the layer, 51 are structural, 18 write the matrices, 52 carry $\gamma^5$, and one article is about the odd part in substance. The layer is not an irreducible foreign body: 32 of the 51 structural articles can be rewritten with the biquaternion formalism, 19 cannot without deleting their subject, and no article needs the odd generator to do its physics. The odd generator is a presentation, not a requirement.**
