# __Introduction to the Biquaternion Physical Interpretation of Mathematics__

## Introduction

The biquaternion algebra is one object, and it carries more than one physical interpretation. The Mathematical menu starts from the algebraic objects — the vector space, the product, the form, the involution — and proves their properties. This category runs the other way. It starts from the articles of the Mathematical menu and asks what each mathematical structure can be read as, physically. The unit of an article is a mathematical result, not a physical object.

The category carries thirty-six articles that interpret results in addition to this introduction. Each of the thirty-six follows the same form: it links one or several articles of the Mathematical menu, then gives the physical interpretations of that result. Such an article opens with the source table: the mathematical content it uses, each row linked to the mathematics article that owns it. It states those results in brief, with their sources. It then gives the physical interpretations, one by one, each labelled and each with its boundary. The article proves nothing: the proof is in the mathematics article, one click away.

The articles follow the four blocks of the Mathematical menu — algebra, topology, analysis and geometry — and the physics menu groups them by the block they read. The algebra block is the largest, because the same algebra carries the material sector, the informational sector and the operators between them.

The link is not a citation of convenience. It is the guarantee of the interpretation. A physical interpretation in this category is always an interpretation of a theorem that exists, and the reader can check the theorem before accepting the interpretation.

## The Form of an Article in This Category

Every article that interprets a result has four parts, in this order.

| Part | Content | Provided by |
| --- | --- | --- |
| The source table | the mathematical content used, with the article that owns each item | the mathematics corpus |
| The statement | the result in brief, with its hypotheses | the mathematics article |
| The interpretations | labelled physical interpretations of the result | this category |
| The limits | what each interpretation does not claim | this category |

### The Source Table

Each article opens with a table of two columns. **Mathematical Content** names the result in the terms in which the article uses it, and **Source Mathematical Article** links the mathematics article that states and proves it. The table is the contract of the article.

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| The subspace, its basis and its defining involution | [Subspaces and Decompositions](../articles_maths/subspaces-and-decompositions-of-the-biquaternion-algebra.html) |
| The norm, its signature and the inverse formula | [N-Regularity and N-Degeneracy in the Biquaternion Algebra](../articles_maths/n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html) |

The rows follow the order in which the article uses the results. A row without a link is not allowed: the reader must be able to open the proof of every item the article interprets. A result that the corpus does not contain is named as missing, not written as if it were proved.

### The Links

The source table is the list of links. An article links to at least one mathematics article, and to several when the interpretation needs several results. A product and its form are two results even when one article carries both; a cone and its projectivisation are two. The link points to the mathematics article, never to a physics article, because the mathematics article is where the proof lives.

The article names the part of the result it uses. A long article may carry ten theorems and one of them may be the one interpreted; the reader must be able to see which.

If an interpretation needs a result that the menu does not contain, the article says so. It does not state the missing result as if it were proved, and it does not borrow a proof from physics.

### The Interpretations

A physical interpretation names a physical object, process or quantity and identifies it with the mathematical structure. It is written as a sentence: *the norm is the interval*, *the minimal Hermitian idempotent is the pure state*, *the two-sided operator is the change of frame*. It is not a metaphor and not an analogy.

Each interpretation is labelled. Several interpretations of one result are allowed, and they are distinguished by the sector, the regime or the question they answer. The label is the reader's protection: it says which interpretation is meant at that point.

An interpretation does not derive the physics from the algebra. It identifies which physical object the algebraic structure is, and it leaves the dynamics to the other physics categories of the corpus.

### The Limits

Every interpretation carries its boundary. The boundary says what the interpretation does not claim: which object it does not identify, which regime it does not cover, which number it does not predict.

The boundary is not decoration. The zero-divisor cone is the light cone on the material sector; on the informational sector its trace-one slice bounds the state space, and that boundary is the set of pure states. The two interpretations are of one set, and the boundary states that the set is not the same physical object in the two cases.

## Why One Result Carries Several Interpretations

The category is not a dictionary of one-to-one correspondences. The algebra is one object and the physics reads it at several levels, so a single theorem can carry more than one interpretation.

The norm is the clearest case. $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^{2}$ is the interval on the material sector: for $\tilde Q=i r'_t\,e_t+r_x\,\vec e_x+r_y\,\vec e_y+r_z\,\vec e_z$ it is $-{r'_{t}}^{2}+x^{2}+y^{2}+z^{2}$. The same form read on a four-position is a squared length; read on a four-momentum, it is $-m^{2}c^{2}$, and the level set $\langle\tilde Q\rangle_{\natural}=-m^{2}c^{2}$ inside the material sector is the mass shell. Its zero set is the zero-divisor cone, the light cone of the material sector. The Hermitian form is the Born pairing up to the factor two. On the state $\tilde{Ϛ}_{\Psi}$ and a Hermitian observable $\tilde H_\Psi$, $\langle\tilde{Ϛ}_{\Psi},\tilde H_\Psi\rangle_{*}=\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde H_\Psi^{*})=\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde H_\Psi)$, and $\mathrm{Tr}(\tilde{Ϛ}_{\Psi}\tilde H_\Psi^{*})=2\,\mathrm{Sc}(\tilde{Ϛ}_{\Psi}\tilde H_\Psi^{*})$ is the probability weight, normalised by $\mathrm{Tr}\,\tilde{Ϛ}_{\Psi}=1$. Four interpretations, four questions, one algebra.

$$
\boxed{\;\langle\tilde Q\rangle_{\natural}=-m^{2}c^{2}\ \text{(mass shell)},\qquad \langle\tilde Q\rangle_{\natural}=0\ \text{(light cone)}\;}
$$

The idempotents are a second case. A minimal Hermitian idempotent is a pure state, a rank-one projector and a choice of vacuum, depending on which structure is interpreted. The three interpretations agree on the element and disagree on the physics, which is why each is labelled.

The two-sided operator is a third. $\mathrm{Sd}_{\tilde Q}(\tilde X)=\tilde Q\tilde X\tilde Q^{*}$ is a change of frame for a unit-norm rotor and a rotation with a dilation for a general unit. For a minimal Hermitian idempotent and a state, $\mathrm{Sd}_{\tilde\Pi}(\tilde{Ϛ}_{\Psi})=\tilde\Pi\tilde{Ϛ}_{\Psi}\tilde\Pi$ is the unnormalised post-measurement state. The same operator, three regimes of its parameter.

A reader who wants one interpretation per theorem will not find it here. A reader who wants to know which interpretation is meant will find the label and the boundary.

## The Place of the Category

The Mathematical menu proves the results; this category reads them physically. The two are independent entries into one corpus.

A reader can enter by the mathematical result and find the physics it carries, or by a physics article of another category and find the theorem behind it. The routes meet at the same theorem.

This category is not a prerequisite of any other, and no other category is a prerequisite of it. The same set is the light cone on the material sector, the purity boundary of the state space on the informational sector, and the support of the massless propagator in the analysis block.

## The Mathematical Corpus about Biquaternions

The list below reproduces the *Biquaternions* category of the Mathematical menu: one hundred and thirty-nine entries, grouped as the menu groups them. Every entry is a mathematics article, and every link opens it directly. The list is the source of this category: an article of the category links to one or several of these entries, and the entries it does not use are the part of the corpus that this category has not yet read.

The category reads a second corpus as well. The *Biquaternion Algebraic Structures* category of the Mathematical menu carries one hundred and thirty-five further entries, the derived structures of the biquaternion complex space: the general plain, quaternionic and sesquilinear algebras, their symmetric and antisymmetric parts, and the comparisons across the twelve. The list below does not reproduce them, because it is already long and the derived structures are read where they are used. An article of the category that interprets one of them links the entry directly, in the *Biquaternion Algebraic Structures* category, exactly as it links an entry of the list. The two corpora together carry two hundred and seventy-four entries, and they are the full mathematical source of the category.

### Algebra

#### The Algebra

- [The Biquaternion Algebra](../articles_maths/the-biquaternion-algebra.html)
- [The Element, the Coordinates and the Conjugations](../articles_maths/the-element-the-coordinates-and-the-conjugations.html)
- [The Group of Involutions](../articles_maths/the-group-of-involutions.html)
- [Subspaces and Decompositions](../articles_maths/subspaces-and-decompositions-of-the-biquaternion-algebra.html)
- [Matrix Representations Conventions](../articles_maths/matrix-representations-conventions.html)
- [The $M_4(\mathbb{C})$ Axis-Free Representation](../articles_maths/m4c-axis-free-representation.html)
- [The $M_4(\mathbb{C})$ Axis-Free Representation](../articles_maths/m4c-axis-free-representation.html)
- [The Square of an Element](../articles_maths/the-square-of-an-element.html)
- [Zero Divisors and Units](../articles_maths/zero-divisors-and-units.html)

#### The Frame

- [Nilpotents](../articles_maths/nilpotents.html)
- [Idempotents](../articles_maths/idempotents.html)
- [The Peirce Decomposition](../articles_maths/the-peirce-decomposition-of-the-biquaternion-algebra.html)
- [The Peirce Basis of a Peirce Decomposition of the Biquaternion Algebra](../articles_maths/the-peirce-basis-of-the-biquaternion-algebra.html)
- [The Polarized Module of the Biquaternion Algebra](../articles_maths/the-polarized-module-of-the-biquaternion-algebra.html)

#### The Modules

- [The Regular Module](../articles_maths/the-regular-module.html)
- [The Polarized Module of the Biquaternion Algebra](../articles_maths/the-polarized-module-of-the-biquaternion-algebra.html)
- [The Category of Modules](../articles_maths/the-category-of-modules.html)
- [The Unpolarized Module of the Biquaternion Algebra](../articles_maths/the-unpolarized-module-of-the-biquaternion-algebra.html)
- [Angular Momentum and Spin in the Biquaternion Algebra](../articles_maths/angular-momentum-and-spin-in-the-biquaternion-algebra.html)

#### The Element

- [The Spectrum](../articles_maths/the-spectrum.html)
- [Spectral Theory and the Spectral Projectors of $M_4(\mathbb{C})$](../articles_maths/spectral-theory-and-the-spectral-projectors-of-m4c.html)
- [The Centraliser](../articles_maths/the-centraliser.html)
- [The Centraliser](../articles_maths/the-centraliser.html)
- [The Semisimple–Nilpotent Split](../articles_maths/the-semisimple-nilpotent-split.html)
- [The Eigenbasis of a Spectrally Regular Biquaternion](../articles_maths/the-eigenbasis-of-a-spectrally-regular-biquaternion.html)
- [The Eigenbasis of a Spectrally Regular Biquaternion](../articles_maths/the-eigenbasis-of-a-spectrally-regular-biquaternion.html)
- [Worked Examples of an Eigenbasis of a Biquaternion](../articles_maths/worked-examples-of-an-eigenbasis-of-a-biquaternion.html)
- [The Jordan Basis of a Spectrally Degenerate Biquaternion](../articles_maths/the-jordan-basis-of-a-spectrally-degenerate-biquaternion.html)
- [The Jordan Basis of a Spectrally Degenerate Biquaternion](../articles_maths/the-jordan-basis-of-a-spectrally-degenerate-biquaternion.html)
- [Square Roots of an Element](../articles_maths/square-roots-of-an-element.html)
- [Worked Examples of an Eigenbasis of a Biquaternion](../articles_maths/worked-examples-of-an-eigenbasis-of-a-biquaternion.html)

#### The Four General Products

- [The Four General Products and Their Relations over the Biquaternion Algebra](../articles_maths/the-four-general-products-and-their-relations-over-the-biquaternion-algebra.html)
- [Symmetric and Antisymmetric Decomposition of the Four General Products](../articles_maths/symmetric-and-antisymmetric-decomposition-of-the-four-general-products.html)
- [The Vector Parts of the Products over the Biquaternion Algebra](../articles_maths/the-vector-parts-of-the-products-over-the-biquaternion-algebra.html)

#### The Four Forms and Their Algebraic Norms

- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](../articles_maths/the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html)
- [Adjoint Pair of $L$ and $R$ Operators](../articles_maths/adjoint-pair-of-l-and-r-operators.html)

- [The $M_4(\mathbb{C})$ Axis-Free Representation](../articles_maths/m4c-axis-free-representation.html)

#### Algebra with the H Norm

- [The Polar Decomposition of a Biquaternion](../articles_maths/the-polar-decomposition-of-a-biquaternion.html)
- [The Polar Decomposition of $M_4(\mathbb{C})$](../articles_maths/the-polar-decomposition-of-m4c.html)

#### Algebra with the N Norm

- [N-Regularity and N-Degeneracy in the Biquaternion Algebra](../articles_maths/n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html)
- [The N-Regular Sector](../articles_maths/the-n-regular-sector.html)
- [The N-Degenerate Sector](../articles_maths/the-n-degenerate-sector.html)
- [The Forms, the Norms and the Singular Set of $M_4(\mathbb{C})$](../articles_maths/the-forms-the-norms-and-the-singular-set-of-m4c.html)
- [The Polar Decomposition of an N-Regular Biquaternion](../articles_maths/the-polar-decomposition-of-an-n-regular-biquaternion.html)
- [The Polar Decomposition of an N-Degenerate Biquaternion](../articles_maths/the-polar-decomposition-of-an-n-degenerate-biquaternion.html)

#### The Spectral Strata and the N Norm

- [Relations between the N Norm and Spectral Regularity and Degeneracy](../articles_maths/relations-between-the-n-norm-and-spectral-regularity-and-degeneracy.html)
- [The N-Regular, Spectrally Regular Sector](../articles_maths/the-n-regular-spectrally-regular-sector.html)
- [The N-Regular, Spectrally Degenerate Sector](../articles_maths/the-n-regular-spectrally-degenerate-sector.html)
- [The N-Degenerate, Spectrally Regular Sector](../articles_maths/the-n-degenerate-spectrally-regular-sector.html)
- [The N-Degenerate, Spectrally Degenerate Sector](../articles_maths/the-n-degenerate-spectrally-degenerate-sector.html)
- [The Product of Two Unipotent Elements and Its Spectrum](../articles_maths/the-product-of-two-unipotent-elements-and-its-spectrum.html)

#### Algebra with the K Norm

- [Kr-Regularity and Degeneracy in the Biquaternion Algebra](../articles_maths/kr-regularity-and-degeneracy-in-the-biquaternion-algebra.html)
- [The Kr-Regular Sector](../articles_maths/the-kr-regular-sector.html)
- [The Kr-Degenerate Sector](../articles_maths/the-kr-degenerate-sector.html)

#### Remarkable Subspaces and the Forms

- [Adjoint Pair of $L$ and $R$ Operators](../articles_maths/adjoint-pair-of-l-and-r-operators.html)
- [Remarkable Subspaces and the Four General Products, Forms and Norms](../articles_maths/remarkable-subspaces-and-the-four-general-products-forms-and-norms.html)
- [The Polar Decomposition and Remarkable Subspaces](../articles_maths/the-polar-decomposition-and-remarkable-subspaces.html)

#### Operators

- [The Endomorphisms of the Biquaternion Algebra](../articles_maths/the-endomorphisms-of-the-biquaternion-algebra.html)
- [The Enveloping Operator Algebra of the Biquaternion Algebra and the Bi-module Structure](../articles_maths/the-enveloping-operator-algebra-of-the-biquaternion-algebra-and-the-bi-module-structure.html)
- [Adjoint Pair of $L$ and $R$ Operators](../articles_maths/adjoint-pair-of-l-and-r-operators.html)
- [Operators Acting on Two Sides](../articles_maths/operators-acting-on-two-sides.html)
- [Operators Acting on One Side](../articles_maths/operators-acting-on-one-side.html)
- [Introduction to N and Spectrally Regular and Degenerate Operators](../articles_maths/introduction-to-n-and-spectrally-regular-and-degenerate-operators.html)
- [N-Regular, Spectrally Regular Operators Acting on One Side](../articles_maths/n-regular-spectrally-regular-operators-acting-on-one-side.html)
- [Hermitian Pair of N-Regular, Spectrally Regular Operators Acting on Two Sides](../articles_maths/hermitian-pair-of-n-regular-spectrally-regular-operators-acting-on-two-sides.html)
- [N-Regular, Spectrally Degenerate Operators Acting on One Side](../articles_maths/n-regular-spectrally-degenerate-operators-acting-on-one-side.html)
- [Hermitian Pair of N-Regular, Spectrally Degenerate Operators Acting on Two Sides](../articles_maths/hermitian-pair-of-n-regular-spectrally-degenerate-operators-acting-on-two-sides.html)
- [N-Degenerate, Spectrally Regular Operators Acting on One Side](../articles_maths/n-degenerate-spectrally-regular-operators-acting-on-one-side.html)
- [Hermitian Pair of N-Degenerate, Spectrally Regular Operators Acting on Two Sides](../articles_maths/hermitian-pair-of-n-degenerate-spectrally-regular-operators-acting-on-two-sides.html)
- [N-Degenerate, Spectrally Degenerate Operators Acting on One Side](../articles_maths/n-degenerate-spectrally-degenerate-operators-acting-on-one-side.html)
- [Hermitian Pair of N-Degenerate, Spectrally Degenerate Operators Acting on Two Sides](../articles_maths/hermitian-pair-of-n-degenerate-spectrally-degenerate-operators-acting-on-two-sides.html)
- [The Hermitian Pair of Operators Acting on Two Sides](../articles_maths/the-hermitian-pair-of-operators-acting-on-two-sides.html)
- [Operators Acting on One Side](../articles_maths/operators-acting-on-one-side.html)
- [Operators Acting on Two Sides](../articles_maths/operators-acting-on-two-sides.html)
- [The Hermitian Pair of Operators Acting on Two Sides](../articles_maths/the-hermitian-pair-of-operators-acting-on-two-sides.html)

### Topology

#### Introduction to Topology on the Biquaternions

- [Topology in the Space of Biquaternions](../articles_maths/topology-in-the-space-of-biquaternions.html)

#### Topology of the Biquaternion Algebra

- [The Euclidean Topology of the Biquaternion Algebra](../articles_maths/the-euclidean-topology-of-the-biquaternion-algebra.html)
- [The Biquaternion Unit Group as a Topological Group](../articles_maths/the-biquaternion-unit-group-as-a-topological-group.html)
- [The Biquaternion Unit Group as a Topological Group](../articles_maths/the-biquaternion-unit-group-as-a-topological-group.html)
- [The Topology of the Zero-Divisor Cone](../articles_maths/the-topology-of-the-zero-divisor-cone.html)

### Analysis

- [Biquaternion Analysis](../articles_maths/biquaternion-analysis.html)
- [The First-Order Root of the Biquaternion D'Alembertian](../articles_maths/the-first-order-root-of-the-biquaternion-d-alembertian.html)
- [Biquaternion Regular Functions](../articles_maths/biquaternion-regular-functions.html)
- [Fueter Theory for Biquaternions](../articles_maths/fueter-theory-for-biquaternions.html)
- [The Two-Sided Derivative over the Biquaternion Algebra: Rank-One Gradients, the Complex Eikonal and the Linear Sector](../articles_maths/the-two-sided-derivative-over-the-biquaternion-algebra.html)
- [Biquaternion Integration](../articles_maths/biquaternion-integration.html)
- [Remarkable Subspaces and the Analysis](../articles_maths/remarkable-subspaces-and-the-analysis.html)
- [Biquaternion Lie Group and Exponential Structure](../articles_maths/biquaternion-lie-group-and-exponential-structure.html)
- [The Killing Form Operator](../articles_maths/the-killing-form-operator.html)
- [Biquaternion Elementary Functions](../articles_maths/biquaternion-elementary-functions.html)
- [Holomorphic Functional Calculus](../articles_maths/holomorphic-functional-calculus.html)
- [Biquaternion Higher Special Functions](../articles_maths/biquaternion-higher-special-functions.html)
- [Biquaternion Discrete Harmonic Analysis](../articles_maths/biquaternion-discrete-harmonic-analysis.html)
- [Biquaternion Continuous Harmonic Analysis](../articles_maths/biquaternion-continuous-harmonic-analysis.html)
- [Relations between the Biquaternion Exponential and the Fourier Kernel](../articles_maths/relations-between-the-biquaternion-exponential-and-the-fourier-kernel.html)
- [The Biquaternion Algebra and the Krein–von Neumann Property](../articles_maths/the-biquaternion-algebra-and-the-krein-von-neumann-property.html)
- [The Tomita Operator and the J-Modular Pair for the Biquaternion Algebra](../articles_maths/the-tomita-operator-and-the-j-modular-pair-for-the-biquaternion-algebra.html)

#### Exponential Polar Decomposition of an N-Regular, Spectrally Regular Biquaternion

- [Exponential Polar Decomposition of an N-Regular, Spectrally Regular Biquaternion](../articles_maths/exponential-polar-decomposition-of-an-n-regular-spectrally-regular-biquaternion.html)
- [Relations between Exponential Polar Decomposition and Eigenbasis of an N-Regular, Spectrally Regular Biquaternion](../articles_maths/relations-between-exponential-polar-decomposition-and-eigenbasis-of-an-n-regular-spectrally-regular-biquaternion.html)
- [Worked Examples of Exponential Polar Decomposition of an N-Regular, Spectrally Regular Biquaternion](../articles_maths/worked-examples-of-exponential-polar-decomposition-of-an-n-regular-spectrally-regular-biquaternion.html)
- [Worked Examples of Exponential Polar Decomposition with Eigenbasis of an N-Regular, Spectrally Regular Biquaternion](../articles_maths/worked-examples-of-exponential-polar-decomposition-with-eigenbasis-of-an-n-regular-spectrally-regular-biquaternion.html)
- [The Quaternion Pairing of the Polar Decomposition of an N-Regular, Spectrally Regular Biquaternion](../articles_maths/the-quaternion-pairing-of-the-polar-decomposition-of-an-n-regular-spectrally-regular-biquaternion.html)
- [The Hamilton Root Pairing of the Polar Decomposition of an N-Regular, Spectrally Regular Biquaternion](../articles_maths/the-hamilton-root-pairing-of-the-polar-decomposition-of-an-n-regular-spectrally-regular-biquaternion.html)
- [The Cartan Hermitian Pairing of the Polar Decomposition of an N-Regular, Spectrally Regular Biquaternion](../articles_maths/the-cartan-hermitian-pairing-of-the-polar-decomposition-of-an-n-regular-spectrally-regular-biquaternion.html)
- [The One-Sided Operator Exponential of an N-Regular, Spectrally Regular Biquaternion](../articles_maths/the-one-sided-operator-exponential-of-an-n-regular-spectrally-regular-biquaternion.html)
- [The Two-Sided Exponential of an N-Regular, Spectrally Regular Biquaternion](../articles_maths/the-two-sided-exponential-of-an-n-regular-spectrally-regular-biquaternion.html)

#### Exponential Polar Decomposition of an N-Regular, Spectrally Degenerate Biquaternion

- [Exponential Polar Decomposition of an N-Regular, Spectrally Degenerate Biquaternion](../articles_maths/exponential-polar-decomposition-of-an-n-regular-spectrally-degenerate-biquaternion.html)
- [Relations between Exponential Polar Decomposition and Eigenbasis of an N-Regular, Spectrally Degenerate Biquaternion](../articles_maths/relations-between-exponential-polar-decomposition-and-eigenbasis-of-an-n-regular-spectrally-degenerate-biquaternion.html)
- [Worked Examples of Exponential Polar Decomposition of an N-Regular, Spectrally Degenerate Biquaternion](../articles_maths/worked-examples-of-exponential-polar-decomposition-of-an-n-regular-spectrally-degenerate-biquaternion.html)
- [Worked Examples of Exponential Polar Decomposition with Eigenbasis of an N-Regular, Spectrally Degenerate Biquaternion](../articles_maths/worked-examples-of-exponential-polar-decomposition-with-eigenbasis-of-an-n-regular-spectrally-degenerate-biquaternion.html)
- [The Quaternion Pairing of the Polar Decomposition of an N-Regular, Spectrally Degenerate Biquaternion](../articles_maths/the-quaternion-pairing-of-the-polar-decomposition-of-an-n-regular-spectrally-degenerate-biquaternion.html)
- [The Hamilton Root Pairing of the Polar Decomposition of an N-Regular, Spectrally Degenerate Biquaternion](../articles_maths/the-hamilton-root-pairing-of-the-polar-decomposition-of-an-n-regular-spectrally-degenerate-biquaternion.html)
- [The Cartan Hermitian Pairing of the Polar Decomposition of an N-Regular, Spectrally Degenerate Biquaternion](../articles_maths/the-cartan-hermitian-pairing-of-the-polar-decomposition-of-an-n-regular-spectrally-degenerate-biquaternion.html)
- [The One-Sided Operator Exponential of an N-Regular, Spectrally Degenerate Biquaternion](../articles_maths/the-one-sided-operator-exponential-of-an-n-regular-spectrally-degenerate-biquaternion.html)
- [The Two-Sided Exponential of an N-Regular, Spectrally Degenerate Biquaternion](../articles_maths/the-two-sided-exponential-of-an-n-regular-spectrally-degenerate-biquaternion.html)

### Geometry

- [Biquaternion Rotations and Lorentz Transformations](../articles_maths/biquaternion-rotations-and-lorentz-transformations.html)
- [Biquaternion Automorphisms and Derivations](../articles_maths/biquaternion-automorphisms-and-derivations.html)
- [The Möbius Transformation as an Operator](../articles_maths/the-mobius-transformation-as-an-operator.html)
- [Biquaternion Versors and the Orthogonal Group](../articles_maths/biquaternion-versors-and-the-orthogonal-group.html)
- [The Unitary Group of the Biquaternion Algebra](../articles_maths/the-unitary-group-of-the-biquaternion-algebra.html)
- [The Krein Isometry Group and Its Cartan Decomposition](../articles_maths/the-krein-isometry-group-and-its-cartan-decomposition.html)
- [The Krein Level Sets and the Hyperbolic Structure](../articles_maths/the-krein-level-sets-and-the-hyperbolic-structure.html)

#### Fractal Geometry

- [The Biquaternion Quadratic Map and Its Julia Sets](../articles_maths/the-biquaternion-quadratic-map-and-its-julia-sets.html)
- [The Biquaternion Mandelbrot Set and the Connectedness Locus](../articles_maths/the-biquaternion-mandelbrot-set-and-the-connectedness-locus.html)
- [The Slices of the Biquaternion Julia Sets](../articles_maths/the-slices-of-the-biquaternion-julia-sets.html)
- [The Escape Radius and the Green's Function for the Biquaternions](../articles_maths/the-escape-radius-and-the-greens-function-for-the-biquaternions.html)
- [The Zero Divisors and the Singular Julia Sets](../articles_maths/the-zero-divisors-and-the-singular-julia-sets.html)
- [The Matrix Element Representation and the Biquaternion Dynamics](../articles_maths/the-matrix-element-representation-and-the-biquaternion-dynamics.html)
- [The Idempotent Decomposition and the Split Fractal of the Biquaternions](../articles_maths/the-idempotent-decomposition-and-the-split-fractal-of-the-biquaternions.html)
- [The Biquaternion Iterated Function Systems](../articles_maths/the-biquaternion-iterated-function-systems.html)
- [The Hausdorff Dimension of the Biquaternion Julia Sets](../articles_maths/the-hausdorff-dimension-of-the-biquaternion-julia-sets.html)
- [The Biquaternion Holomorphic Dynamics and the Jacobian](../articles_maths/the-biquaternion-holomorphic-dynamics-and-the-jacobian.html)

## What the Index Is For

The list has four blocks. The *Algebra* block fixes the vocabulary and the objects: the vector space, the four general products and their twelve readings, the forms, the norms, the involutions, the subspaces, the two sectors, the ideals and the representations. The three remaining blocks of the study are the three places a physical interpretation can land beyond the algebra. Topology gives the causal structure: the cone, its link and its projectivisation. Analysis gives the fields and their evolution: the regular functions, the operators and the propagators. Geometry gives the frames and their orbits: the rotations, the Lorentz group, the $*$-unitary and the Krein groups.

The grouping also tells the reader what kind of interpretation to expect. A general entry fixes a definition. An algebraic entry is read as an object or an operation. A topological entry is read as a locus or a boundary. An analytic entry is read as a field or a propagator. A geometric entry is read as a transformation or an orbit.

The index is not a publication plan. It is the map of the sources, and the category reads them as its articles require. Some entries will carry an interpretation and some will not. The fractal block, in particular, has no physical article in the corpus so far, and an article of this category may say so. The absence of an interpretation is a statement about the physics and not a defect of the mathematics.

## Summary

- The category reads the mathematics physically.
- It carries thirty-six articles that interpret results. Each links one or several articles of the Mathematical menu, states their results, then gives labelled physical interpretations with their boundaries.
- The category owns no theorem; the proof stays in the mathematics article.
- One result may carry several interpretations, and the interpretation names the sector, the regime and the question.
- The index lists the one hundred and thirty-nine entries of the *Biquaternions* category, grouped as the Mathematical menu groups them. The category also reads the one hundred and thirty-five entries of the *Biquaternion Algebraic Structures* category, two hundred and seventy-four in all.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra, of complex dimension four and real dimension eight |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | the quaternion basis, $e_t$ the unit and $\vec e_x,\vec e_y,\vec e_z$ the vector units |
| $i$ | the central imaginary unit, $i^{2}=-1$ |
| $\tilde Q=\sum_\mu Q_\mu e_\mu$ | a general element, with complex coefficients $Q_\mu$ |
| $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^{2}$ | the quaternionic norm, the form that carries the interval |
| $\tilde Q^{*}$ | the Hermitian conjugation, the anti-automorphism of the plain product |
| $\mathbb{B}_{\Phi}$, $\mathbb{B}_{\Psi}$ | the material and the informational sectors, the anti-Hermitian and the Hermitian halves |
| $\tilde{Ϛ}_{\Psi}$ | the state element, Hermitian and normalised by $\langle\tilde{Ϛ}_{\Psi},e_t\rangle_{*}=\tfrac12$ (trace one in the $2\times2$ image) |
| $\tilde\Pi$ | an idempotent; a rank-one Hermitian idempotent is a pure state |
| $\mathrm{Sd}_{\tilde Q}(\tilde X)=\tilde Q\tilde X\tilde Q^{*}$ | the two-sided operator, the change of frame on the unit-norm slice |

## Further Reading

- The Mathematical menu, *Biquaternions* category, which is the source of every mathematical link of this article, and its *Biquaternion Algebraic Structures* category, which supplies the derived structures read where they are used.
- [Conventions in the Biquaternion Universe](algebra-and-element-conventions.html), for the notation every article of the category assumes.
- [Introduction to the Biquaternion Universe](introduction-to-the-biquaternion-universe.html), for the algebra and the two sectors.
- [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html) and [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html), for the two sector articles of this category.
