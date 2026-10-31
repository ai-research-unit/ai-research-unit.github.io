# __The Iota Problem in Part VI and Physics: A Category Audit__

## Introduction

This audit covers two bodies of text and nothing else: the 884 articles of Part VI of the mathematical corpus, and the 403 articles of the physics corpus. No count from an earlier full-corpus scan is reused. The question is narrow. Where does $\iota$ carry more than one meaning, and in which article does it do so?

The answer is uneven. Physics is nearly clean. Part VI is not. Of the 1,287 distinct article files, 40 use $\iota$ at all, for 704 occurrences and 59 spellings. Twenty-two of those articles write a form that means something else elsewhere, and 198 occurrences are written in such a form.

The three uses in the original premise do not exhaust the letter, and they do not carry equal weight inside the restricted scope. The Clifford comparison is present, but almost always as $\iota_{\mathrm{Cl}}$. The interior product is present twice. No scanned article uses $\iota$ for an octonion imaginary unit. Meanwhile the bare letter alone has eleven readings.

The rest of the article follows the corpus categories. Each category has a table of its $\iota$ articles, the total count, the number of occurrences in an ambiguous form, the problematic spelling, and what the letter means in that article.

## Scope and Method

Part VI begins at the heading *PART VI: SYNTHETIC STUDIES* in `maths.md` and runs to the end of that menu. Its 884 articles fall into 24 categories, from Booleans to the structural comparison around biquaternions. The physics menu has 403 articles in 13 categories.

Three file names occur in both corpora, but each menu links its own copy. The scan follows the menu folder, so the 884 Part VI files and the 403 physics files give 1,287 distinct files.

The scan reads each Markdown file and counts every control sequence `\iota` that is not followed by a letter. It keeps the subscript and the superscript, including nested braces. It counts occurrences, not lines and not articles. The forms $\iota_{\mathrm{Cl}}$, $\iota_\nu$, $\iota_{\nu_1}$ and $\iota_k$ are four different spellings.

A spelling is problematic when the scanned corpus gives it more than one reading. Four spellings qualify. The bare letter has eleven readings. The forms $\iota_k$, $\iota_1$ and $\iota_2$ have two each. The forms $\iota_3$, $\iota_0$, $\iota_j$, $\iota_\nu$, $\iota_u$, $\iota_g$ and $\iota_{\mathrm{Cl}}$ have one reading in this scope.

The Clifford comparison can be checked against the earlier table. The full corpus has 166 occurrences in nine files. The eight physics files in this scope have 151. The ninth is the mathematics conventions article, which lies outside Part VI.

The readings are assigned from the definition in each article, not from the letter alone. Where an article defines two objects, both are recorded. The occurrence column is the total for the article, not only the problematic part.

## The Verdict

| Measure | Part VI | Physics | Total |
|---|---:|---:|---:|
| Distinct article files | 884 | 403 | 1287 |
| Articles using $\iota$ | 29 | 11 | 40 |
| Occurrences | 523 | 181 | 704 |
| Occurrences in an ambiguous form | 176 | 22 | 198 |
| Articles with an ambiguous form | 20 | 2 | 22 |
| Share of occurrences ambiguous | 34% | 12% | 28% |

The 884 Part VI files and the 403 physics files give 1,287 in all. Three names occur in both corpora; the files behind them are distinct.

Physics is nearly clean. Of its 181 occurrences, 159 are stable: 151 are the Clifford comparison $\iota_{\mathrm{Cl}}$, two are the interior product, one is an inner automorphism, and five are spinor variants. Only two articles are affected, and one of them contributes a single bare occurrence.

Part VI carries the problem. Of its 523 occurrences, 176 are written in an ambiguous form, and 20 of its 29 $\iota$ articles are affected. The worst category is Quaternions, with 110 ambiguous occurrences out of 353. The worst single article is *Quaternion Augmented Statistics*, with 61 ambiguous occurrences out of 138.

The bare letter is the main defect: 112 occurrences, 19 articles, eleven readings. The subscript collisions are smaller but sharper. $\iota_k$ is a corner embedding in one article and an axis involution in three others. $\iota_1$ and $\iota_2$ are axis involutions in three articles and spinor components in one.

The sharpest inconsistency across categories is the corner embedding. It is bare in $M_3(\mathbb{C})$ and $M_5(\mathbb{C})$, it is $\iota_k$ in $M_6(\mathbb{C})$, and $\iota_k$ is an axis involution in Quaternions.

## Coverage by Category

Only the categories that use the letter are listed one by one. The categories without it are grouped in one row per part: eleven Part VI categories with 309 articles, and seven physics categories with 189.

| Category | Part | Articles in category | Articles using $\iota$ | Occurrences | Ambiguous | Main reading |
|---|---|---:|---:|---:|---:|---|
| Integers | VI | 2 | 1 | 22 | 22 | embedding $\mathbb{N}\to\mathbb{Z}$ |
| Real Numbers | VI | 19 | 2 | 4 | 4 | inversion |
| Complex Numbers | VI | 34 | 3 | 6 | 6 | inversion; adjoined imaginary |
| Reduced Biquaternions | VI | 83 | 1 | 9 | 9 | idempotent representation |
| Quaternions | VI | 64 | 11 | 353 | 110 | axis involutions; 2×2 embedding |
| Quaternioid Algebraic Structures | VI | 49 | 2 | 75 | 0 | inner involutions |
| Split-Quaternions | VI | 46 | 1 | 15 | 0 | inner automorphism |
| Biquaternions | VI | 153 | 3 | 15 | 3 | inner automorphism; coefficient isometry |
| Split-Biquaternions | VI | 41 | 1 | 1 | 0 | inner automorphism |
| $M_3(\mathbb{C})$ | VI | 23 | 1 | 4 | 4 | corner embedding |
| $M_5(\mathbb{C})$ | VI | 23 | 1 | 6 | 5 | block embedding |
| $M_6(\mathbb{C})$ | VI | 24 | 1 | 11 | 11 | corner embeddings |
| Structural Comparison around Biquaternions | VI | 14 | 1 | 2 | 2 | 2×2 matrix model |
| Biquaternion Universe Conventions | Physics | 8 | 1 | 33 | 0 | Clifford comparison |
| Biquaternion Non Relativistic Non Quantum Theory | Physics | 25 | 1 | 2 | 0 | interior product |
| Biquaternion Relativistic Quantum Theory | Physics | 50 | 5 | 72 | 1 | Clifford comparison |
| Biquaternion Quantum Fields | Physics | 68 | 1 | 31 | 0 | Clifford comparison |
| Biquaternion Particle Physics and Gauge Fields | Physics | 52 | 1 | 1 | 0 | inner automorphism |
| Biquaternion Gravity and Cosmology | Physics | 11 | 2 | 42 | 21 | Clifford comparison; NP spinor |
| Other Part VI categories | VI | 309 | 0 | 0 | 0 | none |
| Other physics categories | Physics | 189 | 0 | 0 | 0 | none |
| **Total** | **—** | **1287** | **40** | **704** | **198** | **—** |

The column adds to 1,287, the number of distinct files.

## Part VI: Synthetic Studies

Part VI has 29 articles that use the letter, 523 occurrences in all, and 176 occurrences in an ambiguous form. The sections below follow the menu order.

### Integers

One article uses the letter, and it uses it 22 times for one map: the embedding $\iota:\mathbb{N}\to\mathbb{Z}$, $\iota(n)=[(n,0)]$. The article introduces the map in a display and never declares a scope. Inside the article there is no ambiguity. Against the other categories there is: the same bare letter is an inversion, a spinor, and four different embeddings.

| Article | Occurrences | Ambiguous | Problematic symbol | Reading |
|---|---:|---:|---|---|
| [The Integers ($\mathbb{Z}$)](../articles_maths/the-integers.html) | 22 | 22 | $\iota$ | the embedding $\mathbb{N}\to\mathbb{Z}$, $\iota(n)=[(n,0)]$ |

### Real Numbers

Two articles use the letter, for four occurrences and one object: the inversion $q\mapsto q^{-1}$ on $\mathbb{R}^\times$. *Real Polar Decomposition* repeats the same map in polar coordinates. The category is internally consistent, and it agrees with Complex Numbers. The collision is with the embeddings.

| Article | Occurrences | Ambiguous | Problematic symbol | Reading |
|---|---:|---:|---|---|
| [Real Norm and Invertibility](../articles_maths/real-norm-and-invertibility.html) | 3 | 3 | $\iota$ | the inversion $q\mapsto q^{-1}$ on $\mathbb{R}^\times$ |
| [Real Polar Decomposition](../articles_maths/real-polar-decomposition.html) | 1 | 1 | $\iota$ | the inversion, read in polar coordinates |

### Complex Numbers

Three articles use the letter, for six occurrences and two objects. *Complex Norm and Invertibility* and *Complex Exponential and Lie Group Structure* use $\iota$ for the inversion $Q\mapsto Q^{-1}$. *Spectral Regularity and Degeneracy in the Complex Algebra* uses $\iota$ for the adjoined imaginary, $\iota=1\otimes i$, in the idempotents $e_\pm=\tfrac12(1\mp i\iota)$. The same bare letter carries two objects in one category, and the article does not warn the reader.

| Article | Occurrences | Ambiguous | Problematic symbol | Reading |
|---|---:|---:|---|---|
| [Complex Norm and Invertibility](../articles_maths/complex-norm-and-invertibility.html) | 3 | 3 | $\iota$ | the inversion $Q\mapsto Q^{-1}$ on $\mathbb{C}^\times$ |
| [Spectral Regularity and Degeneracy in the Complex Algebra](../articles_maths/spectral-regularity-and-degeneracy-in-the-complex-algebra.html) | 2 | 2 | $\iota$ | the adjoined imaginary $\iota=1\otimes i$ |
| [Complex Exponential and Lie Group Structure](../articles_maths/complex-exponential-and-lie-group-structure.html) | 1 | 1 | $\iota$ | the inversion, as the inverse map of the Lie group |

### Reduced Biquaternions

One article, nine occurrences. Here $\iota$ is the idempotent-coordinate isomorphism $\mathbb{B}_{\mathrm{r}}\to\mathbb{C}\times\mathbb{C}$, $\iota(\breve Q)=(Q_+,Q_-)$. It is a canonical isomorphism, but not the canonical embedding of the other categories. The bare letter hides the codomain.

| Article | Occurrences | Ambiguous | Problematic symbol | Reading |
|---|---:|---:|---|---|
| [Reduced Biquaternion Versors and the Orthogonal Group](../articles_maths/reduced-biquaternion-other-algebraic-element-representations.html) | 9 | 9 | $\iota$ | the idempotent-coordinate isomorphism $\mathbb{B}_{\mathrm{r}}\to\mathbb{C}\times\mathbb{C}$ |

### Quaternions

Eleven of the 64 articles use the letter, for 353 occurrences. This is the largest block in the scope, and two objects share the letter.

The first is the inner automorphism, $\iota_u(\tilde q)=u\tilde q u^{-1}$ for a unit $u$. On a unit imaginary axis it is the involution $\iota_\nu(\tilde q)=\nu\tilde q\nu^{-1}$. It is written $\iota_\nu$, $\iota_u$, $\iota_k$, $\iota_j$, $\iota_0$, $\iota_1$, $\iota_2$, $\iota_3$, $\iota_{\vec e_k}$. These are one object with many spellings. Inside the category the reading is stable.

The second is the 2×2 matrix embedding $\mathbb{H}\to M_2(\mathbb{C})$, written bare in four articles, for 36 occurrences.

Against the rest of the corpus both readings collide. $\iota_k$ is a corner embedding in $M_6(\mathbb{C})$. $\iota_1$ and $\iota_2$ are spinor components in the Newman–Penrose article. The inner automorphism is consistent across the algebras, but its parameter letter changes from article to article.

| Article | Occurrences | Ambiguous | Problematic symbol | Reading |
|---|---:|---:|---|---|
| [Quaternion Augmented Statistics](../articles_maths/quaternion-augmented-statistics.html) | 138 | 61 | $\iota$; $\iota_k$, $\iota_1$, $\iota_2$ | axis involutions $\iota_k(\tilde q)=\vec e_k\tilde q\vec e_k^{-1}$; the bare letter once for a generic involution in a definition |
| [Quaternion Involutions and Projections](../articles_maths/quaternion-involutions-and-projections.html) | 97 | 7 | $\iota_k$, $\iota_1$, $\iota_2$ | axis involutions, the coordinate instances $\iota_k=\iota_{\vec e_k}$ of $\iota_\nu$ |
| [The Generalised Hamilton–Rodrigues Calculus](../articles_maths/the-generalised-hamilton-rodrigues-calculus.html) | 35 | 6 | $\iota_k$, $\iota_1$, $\iota_2$ | axis involutions $\iota_k$; and $\iota_{\tilde q_1^{-1}}$, an inner automorphism |
| [Quaternion Automorphisms and Derivations](../articles_maths/quaternion-automorphisms-and-derivations.html) | 23 | 0 | none | the inner automorphism $\iota_u$ |
| [Quaternion Other Algebraic Element Representations](../articles_maths/quaternion-other-algebraic-element-representations.html) | 16 | 16 | $\iota$ | the 2×2 matrix embedding $\mathbb{H}\to M_2(\mathbb{C})$ |
| [Decompositions Along the Remarkable Subspaces of the Quaternions](../articles_maths/decompositions-along-the-remarkable-subspaces-of-the-quaternions.html) | 15 | 0 | none | the inner involution $\iota_\nu$ |
| [Modulus–Unit Polar Decomposition of Quaternions](../articles_maths/modulus-unit-polar-decomposition-of-quaternions.html) | 12 | 12 | $\iota$ | the 2×2 matrix embedding $\mathbb{H}\to M_2(\mathbb{C})$ |
| [Comparison of the Remarkable Subspaces of the Quaternions](../articles_maths/comparison-of-the-remarkable-subspaces-of-the-quaternions.html) | 6 | 0 | none | the inner involution $\iota_\nu$ |
| [Exponential Polar Decomposition of Quaternions](../articles_maths/exponential-polar-decomposition-of-quaternions.html) | 5 | 5 | $\iota$ | the 2×2 matrix embedding $\mathbb{H}\to M_2(\mathbb{C})$ |
| [Rational-Chart Polar Decomposition of Quaternions](../articles_maths/rational-chart-polar-decomposition-of-quaternions.html) | 3 | 3 | $\iota$ | the 2×2 matrix embedding $\mathbb{H}\to M_2(\mathbb{C})$ |
| [Introduction to the 2×2 Matrix Element Representation of Quaternions](../articles_maths/introduction-to-the-2x2-matrix-element-representation-of-quaternions.html) | 3 | 0 | none | the inner involution $\iota_\nu$ |

### Quaternioid Algebraic Structures

Two articles, 75 occurrences, the inner automorphism again. *The Group of Involutions of the Quaternioid* writes the family $\iota_\nu$ and its products; *The Quaternioid as a Vector Space over $\mathbb{C}$* writes $\iota_a$ for a general unit $a$. The object is the same as in Quaternions. Only the parameter letter changes.

| Article | Occurrences | Ambiguous | Problematic symbol | Reading |
|---|---:|---:|---|---|
| [The Group of Involutions of the Quaternioid](../articles_maths/the-group-of-involutions-of-the-quaternioid.html) | 70 | 0 | none | the inner involutions $\iota_\nu$ and their products |
| [The Quaternioid as a Vector Space over $\mathbb{C}$](../articles_maths/the-quaternioid-as-a-vector-space-over-c.html) | 5 | 0 | none | the inner automorphism $\iota_a$ |

### Split-Quaternions

One article, 15 occurrences, the inner automorphism $\iota_g$. The category is clean.

| Article | Occurrences | Ambiguous | Problematic symbol | Reading |
|---|---:|---:|---|---|
| [Split-Quaternion Automorphisms and Derivations](../articles_maths/split-quaternion-automorphisms-and-derivations.html) | 15 | 0 | none | the inner automorphism $\iota_g$ |

### Biquaternions

Three articles, 15 occurrences, three readings. *Biquaternion Automorphisms and Derivations* uses $\iota_g$ for the inner automorphism; that is the same object as in Split-Quaternions. *The Euclidean Topology of the Biquaternion Algebra* uses bare $\iota$ for the coefficient isometry $\mathbb{B}\to\mathbb{R}^8$. *The Tomita Operator and the J-Modular Pair for the Biquaternion Algebra* uses bare $\iota$ in $\xi=\iota(1)=e_t$ and never defines it. That single occurrence is the only undefined use in the scope.

| Article | Occurrences | Ambiguous | Problematic symbol | Reading |
|---|---:|---:|---|---|
| [Biquaternion Automorphisms and Derivations](../articles_maths/biquaternion-automorphisms-and-derivations.html) | 12 | 0 | none | the inner automorphism $\iota_g$ |
| [The Euclidean Topology of the Biquaternion Algebra](../articles_maths/the-euclidean-topology-of-the-biquaternion-algebra.html) | 2 | 2 | $\iota$ | the coefficient isometry $\mathbb{B}\to\mathbb{R}^8$ |
| [The Tomita Operator and the J-Modular Pair for the Biquaternion Algebra](../articles_maths/the-tomita-operator-and-the-j-modular-pair-for-the-biquaternion-algebra.html) | 1 | 1 | $\iota$ | a unit map, $\iota(1)=e_t$, not defined in the article |

### Split-Biquaternions

One article, one occurrence, the inner automorphism $\iota_u$. The category is clean.

| Article | Occurrences | Ambiguous | Problematic symbol | Reading |
|---|---:|---:|---|---|
| [Split-Biquaternion Automorphisms and Derivations](../articles_maths/split-biquaternion-automorphisms-and-derivations.html) | 1 | 0 | none | the inner automorphism $\iota_u$ |

### $M_3(\mathbb{C})$

One article, four occurrences, all bare: the corner embedding $M_2(\mathbb{C})\to M_3(\mathbb{C})$, $B\mapsto\begin{pmatrix}B&0\\0&0\end{pmatrix}$. The image is the corner $P M_3 P$, and the map is unital onto that corner but not into $M_3$.

| Article | Occurrences | Ambiguous | Problematic symbol | Reading |
|---|---:|---:|---|---|
| [The $M_2$ Corner of $M_3(\mathbb{C})$](../articles_maths/the-m2-corner-of-m3c.html) | 4 | 4 | $\iota$ | the corner embedding $M_2(\mathbb{C})\to M_3(\mathbb{C})$ |

### $M_5(\mathbb{C})$

One article, six occurrences, five bare: the block embedding $M_2(\mathbb{C})\oplus M_3(\mathbb{C})\to M_5(\mathbb{C})$, $(A,B)\mapsto\operatorname{diag}(A,B)$. The same construction is written bare here and in $M_3(\mathbb{C})$.

| Article | Occurrences | Ambiguous | Problematic symbol | Reading |
|---|---:|---:|---|---|
| [The $M_2\oplus M_3$ Corner of $M_5(\mathbb{C})$](../articles_maths/the-m2-m3-corner-of-m5c.html) | 6 | 5 | $\iota$ | the block embedding $M_2(\mathbb{C})\oplus M_3(\mathbb{C})\to M_5(\mathbb{C})$ |

### $M_6(\mathbb{C})$

One article, eleven occurrences, all $\iota_k$: the corner embeddings $M_k(\mathbb{C})\to M_6(\mathbb{C})$. The same construction is bare in the two previous categories, and the same spelling is the axis involution in Quaternions. This is the sharpest collision in the scope: one symbol, two objects, two categories, and no signal in the article.

| Article | Occurrences | Ambiguous | Problematic symbol | Reading |
|---|---:|---:|---|---|
| [The $M_3\oplus M_3$ and $M_2\oplus M_4$ Corners of $M_6(\mathbb{C})$](../articles_maths/the-m3-m3-and-m2-m4-corners-of-m6c.html) | 11 | 11 | $\iota_k$ | the corner embeddings $M_k(\mathbb{C})\to M_6(\mathbb{C})$ |

### Structural Comparison around Biquaternions

One article, two occurrences, the 2×2 complex model of the quaternions. It is the same embedding as in the four Quaternion articles. The total for that object is 38 occurrences in five articles, all bare.

| Article | Occurrences | Ambiguous | Problematic symbol | Reading |
|---|---:|---:|---|---|
| [Comparison of Element Representations and Matrix Models](../articles_maths/comparison-of-element-representations-and-matrix-models.html) | 2 | 2 | $\iota$ | the 2×2 complex model $\mathbb{H}\to M_2(\mathbb{C})$ |

## Physics

Physics has eleven articles that use the letter, 181 occurrences in all, and only 22 occurrences in an ambiguous form. The stable part is dominated by the Clifford comparison, with the interior product, one inner automorphism and five spinor variants.

### Biquaternion Universe Conventions

One article, 33 occurrences, all $\iota_{\mathrm{Cl}}$. This is the defining article for the comparison map. The category is clean.

| Article | Occurrences | Ambiguous | Problematic symbol | Reading |
|---|---:|---:|---|---|
| [Conventions of the Matrix Models](../articles_physics/conventions-of-the-matrix-models.html) | 33 | 0 | none | the Clifford comparison $\iota_{\mathrm{Cl}}$ |

### Biquaternion Non Relativistic Non Quantum Theory

One article, two occurrences, $\iota_{X_f}\omega=df$. The letter is the interior product. The category is clean.

| Article | Occurrences | Ambiguous | Problematic symbol | Reading |
|---|---:|---:|---|---|
| [The Symplectic Form and the Biquaternion Norm Cone](../articles_physics/the-symplectic-form-and-the-biquaternion-norm-cone.html) | 2 | 0 | none | the interior product $\iota_{X_f}$ |

### Biquaternion Relativistic Quantum Theory

Five articles, 72 occurrences. Four are clean: *Reflection*, *Rarita–Schwinger*, *Dirac Path Integral* and *Foldy–Wouthuysen*, all with $\iota_{\mathrm{Cl}}$. *The Dirac Equation* uses $\iota_{\mathrm{Cl}}$ once and bare $\iota$ once, for the complexified extension of the comparison. That single bare occurrence is the only ambiguity in the category.

| Article | Occurrences | Ambiguous | Problematic symbol | Reading |
|---|---:|---:|---|---|
| [The Reflection and the Rotation in Biquaternionic Form](../articles_physics/the-reflection-and-the-rotation-in-biquaternionic-form.html) | 37 | 0 | none | the Clifford comparison $\iota_{\mathrm{Cl}}$ |
| [The Rarita–Schwinger Equation: Spin 3/2 in Biquaternionic Form](../articles_physics/the-rarita-schwinger-equation-spin-3-2-in-biquaternionic-form.html) | 20 | 0 | none | the Clifford comparison $\iota_{\mathrm{Cl}}$ |
| [The Dirac Path Integral in Biquaternionic Form](../articles_physics/the-dirac-path-integral-in-biquaternionic-form.html) | 7 | 0 | none | the Clifford comparison $\iota_{\mathrm{Cl}}$ |
| [The Foldy–Wouthuysen Transformation in Biquaternionic Form](../articles_physics/the-foldy-wouthuysen-transformation-in-biquaternionic-form.html) | 6 | 0 | none | the Clifford comparison $\iota_{\mathrm{Cl}}$ |
| [The Dirac Equation in Biquaternionic Form](../articles_physics/the-dirac-equation-in-biquaternionic-form.html) | 2 | 1 | $\iota$ | the Clifford comparison, written $\iota_{\mathrm{Cl}}$ once and bare once for its complexified extension |

### Biquaternion Quantum Fields

One article, 31 occurrences, all $\iota_{\mathrm{Cl}}$. The category is clean.

| Article | Occurrences | Ambiguous | Problematic symbol | Reading |
|---|---:|---:|---|---|
| [The Anomalous Magnetic Moment in Biquaternionic Form](../articles_physics/the-anomalous-magnetic-moment-in-biquaternionic-form.html) | 31 | 0 | none | the Clifford comparison $\iota_{\mathrm{Cl}}$ |

### Biquaternion Particle Physics and Gauge Fields

One article, one occurrence, the inner automorphism $\iota_\lambda$. It is the identity because $\lambda$ is central. The category is clean, but $\iota_\lambda$ is a fourth parameter letter for the inner automorphism, after $\iota_u$, $\iota_g$ and $\iota_a$.

| Article | Occurrences | Ambiguous | Problematic symbol | Reading |
|---|---:|---:|---|---|
| [Gauge Redundancy and the Information in the Gauge Orbit in Biquaternionic Form](../articles_physics/gauge-redundancy-and-the-information-in-the-gauge-orbit-in-biquaternionic-form.html) | 1 | 0 | none | the inner automorphism $\iota_\lambda$, the identity because $\lambda$ is central |

### Biquaternion Gravity and Cosmology

Two articles, 42 occurrences. *Curved Spacetime and the Biquaternion Framework* uses 16 $\iota_{\mathrm{Cl}}$ and is clean. *The Newman–Penrose Formalism in Biquaternionic Form* uses 26, of which 21 are ambiguous: bare $\iota$ 19, and $\iota_1$ and $\iota_2$ once each. Here $\iota$ is the second basis spinor, $(0,1)^T$, and $\iota_1,\iota_2$ are its components. The notation is standard in general relativity. The collision is with the quaternion axis involutions, not with the Clifford map.

| Article | Occurrences | Ambiguous | Problematic symbol | Reading |
|---|---:|---:|---|---|
| [The Newman–Penrose Formalism in Biquaternionic Form](../articles_physics/the-newman-penrose-formalism-in-biquaternionic-form.html) | 26 | 21 | $\iota$, $\iota_1$, $\iota_2$ | the Newman–Penrose spinor $\iota=(0,1)^T$ and its components |
| [Curved Spacetime and the Biquaternion Framework](../articles_physics/curved-spacetime-and-the-biquaternion-framework.html) | 16 | 0 | none | the Clifford comparison $\iota_{\mathrm{Cl}}$ |

## The Objects

Every occurrence belongs to one of thirteen objects or object families. The table gives the totals. The first row collects the inner automorphism and its involution cases: the quaternion axis family and the inner automorphisms of the other algebras. It is the largest class, and the one with the most spellings.

| Object | Occurrences | Main spellings |
|---|---:|---|
| inner automorphism and its involutions | 421 | $\iota_\nu$, $\iota_u$, $\iota_g$, $\iota_a$, $\iota_\lambda$, $\iota_k$, $\iota_j$, $\iota_0$, $\iota_1$, $\iota_2$, $\iota_3$, $\iota_{\vec e_k}$ |
| Clifford comparison | 152 | $\iota_{\mathrm{Cl}}$, and once bare |
| 2×2 matrix embedding $\mathbb{H}\to M_2(\mathbb{C})$ | 38 | bare $\iota$ |
| Newman–Penrose spinor | 26 | bare $\iota$, $\iota_1$, $\iota_2$, $\iota^A$, $\iota^\dagger$ |
| embedding $\mathbb{N}\to\mathbb{Z}$ | 22 | bare $\iota$ |
| corner or block embedding | 20 | bare $\iota$, $\iota_k$ |
| idempotent representation | 9 | bare $\iota$ |
| inversion | 8 | bare $\iota$ |
| coefficient isometry | 2 | bare $\iota$ |
| algebra element $1\otimes i$ | 2 | bare $\iota$ |
| interior product | 2 | $\iota_{X_f}$ |
| generic involution | 1 | bare $\iota$ |
| unit map | 1 | bare $\iota$ |
| **Total** | **704** | **—** |

## The Collisions

Four spellings have more than one reading. The table gives every reading and its count. A reading is a mathematical object, not a grammatical role.

| Spelling | Occurrences | Articles | Readings |
|---|---:|---:|---|
| $\iota$ | 112 | 19 | matrix embedding $\mathbb{H}\to M_2(\mathbb{C})$ 38; embedding $\mathbb{N}\to\mathbb{Z}$ 22; Newman–Penrose spinor 19; corner or block embedding 9; idempotent representation 9; inversion 8; coefficient isometry 2; algebra element 2; Clifford comparison 1; generic involution 1; unit map 1 |
| $\iota_k$ | 53 | 4 | axis involution 42; corner embedding 11 |
| $\iota_1$ | 17 | 4 | axis involution 16; Newman–Penrose component 1 |
| $\iota_2$ | 16 | 4 | axis involution 15; Newman–Penrose component 1 |

The bare letter is not one word with one meaning. It is eleven words written the same way. The largest blocks are the matrix embedding (38), the embedding of $\mathbb{N}$ into $\mathbb{Z}$ (22), and the Newman–Penrose spinor (19). None of those articles declares which object the letter denotes. The remaining eight readings are smaller but not negligible: corner and block embeddings 9, idempotent representation 9, inversion 8, coefficient isometry 2, algebra element 2, Clifford comparison 1, generic involution 1, undefined unit map 1.

The $\iota_k$ collision has two sides: 42 axis involutions in Quaternions, 11 corner embeddings in $M_6(\mathbb{C})$. The second side is one article and one construction. A rename there is cheap and closes the collision.

The numeral collision is small in counts and large in consequence. $\iota_1$ and $\iota_2$ are axis involutions 16 and 15 times, and spinor components once each. Both readings are "the first" or "the second" object in their formalism, so the reader has no way to choose without the surrounding text. $\iota_3$ is not used in the Newman–Penrose article, but it belongs to the same series and invites the same misreading.

## The Repairs

The repairs are local. A qualified subscript names the object, and the letter stays available for the standard uses.

| Object | Current form | Occurrences | Articles | Proposed form |
|---|---|---:|---:|---|
| 2×2 matrix embedding | $\iota$ | 38 | 5 | $\iota_{M_2}$ |
| embedding $\mathbb{N}\to\mathbb{Z}$ | $\iota$ | 22 | 1 | $\iota_{\mathbb Z}$ |
| corner or block embedding | $\iota$ | 9 | 2 | $\iota^{\mathrm{cor}}$ |
| corner embedding $M_k\to M_6$ | $\iota_k$ | 11 | 1 | $\iota^{\mathrm{cor}}_k$ |
| idempotent representation | $\iota$ | 9 | 1 | $\iota_{\mathrm{idem}}$ |
| inversion | $\iota$ | 8 | 4 | $\iota_{\mathrm{inv}}$ |
| coefficient isometry | $\iota$ | 2 | 1 | $\iota_{\mathbb R^8}$ |
| algebra element $1\otimes i$ | $\iota$ | 2 | 1 | $\varepsilon$ |
| generic involution | $\iota$ | 1 | 1 | $\sigma$ |
| unit map $\iota(1)=e_t$ | $\iota$ | 1 | 1 | define it or drop it |
| Newman–Penrose spinor | $\iota$ | 19 | 1 | keep, declare the scope |
| Clifford comparison | $\iota$ | 1 | 1 | write $\iota_{\mathrm{Cl}}$ |

The table covers 123 occurrences, of which 103 need an edit and 20 are already standard. The two component forms $\iota_1,\iota_2$ in the Newman–Penrose article are kept for the same reason. The matrix embedding is the largest single edit: 38 occurrences in five articles. The embedding of $\mathbb{N}$ into $\mathbb{Z}$ is second, with 22 occurrences in one article.

The quaternion axis family is not in the table. Its spellings are stable inside Quaternions, and a global rename would touch more than two hundred occurrences for no gain in that category. The collision is closed from the other side, by renaming the $M_6(\mathbb{C})$ embedding and by declaring the Newman–Penrose spinor. A scope sentence at the top of the Quaternion articles would make the numeral series safe as well.

The inner automorphism has one object and four parameter letters: $\iota_u$, $\iota_g$, $\iota_a$, $\iota_\lambda$. This is not a collision, because the construction is the same. It is an inconsistency. A single form, $\operatorname{Ad}_g$, would remove it, but the change is optional and touches 44 occurrences in nine articles.

## Summary

The audit scanned 1,287 article files: 884 in Part VI and 403 in physics. Forty articles use $\iota$, for 704 occurrences and 59 spellings.

The largest object class is the inner automorphism and its involution cases, with 421 occurrences. The Clifford comparison is second, with 152.

Twenty-two articles write a form with more than one reading, and 198 occurrences are in such a form. Part VI contributes 176 of the 198; physics contributes 22. The bare letter accounts for 112 occurrences and eleven readings. $\iota_k$ accounts for 53 occurrences and two readings. $\iota_1$ and $\iota_2$ account for 33 occurrences and two readings.

Physics is not the problem. Its 159 stable occurrences are the Clifford comparison, the interior product, one inner automorphism, and five spinor variants. The only physics defects are 21 occurrences in the Newman–Penrose article and one bare comparison in the Dirac article.

Part VI is the problem, and the Quaternions category is its centre: 110 ambiguous occurrences out of 353. The sharpest single collision is the corner embedding, written bare in $M_3(\mathbb{C})$ and $M_5(\mathbb{C})$, written $\iota_k$ in $M_6(\mathbb{C})$, and written $\iota_k$ for the axis involution in Quaternions.

## Summary of Notation

| Form | Reading | Where |
|---|---|---|
| $\iota$ | the letter under audit, quoted rather than used | throughout |
| $\iota_{\mathrm{Cl}}$ | the Clifford comparison | physics, 151 occurrences |
| $\iota_X$, $\iota_{X_f}$ | the interior product | physics |
| $\iota_\nu$ | the inner involution about the axis $\nu$ | Quaternions |
| $\iota_k$, $\iota_j$, $\iota_0$, $\iota_1$, $\iota_2$, $\iota_3$ | axis involutions | Quaternions |
| $\iota_1$, $\iota_2$ | components of the Newman–Penrose spinor | Newman–Penrose article |
| $\iota_k$ | the corner embedding $M_k(\mathbb{C})\to M_6(\mathbb{C})$ | $M_6(\mathbb{C})$ |
| $\iota_u$, $\iota_g$, $\iota_a$, $\iota_\lambda$ | the inner automorphism | several algebras |
| $\iota_{M_2}$ | proposed form for the 2×2 matrix embedding | this article |
| $\iota^{\mathrm{cor}}_k$ | proposed form for the corner embedding | this article |

## Further Reading

The conventions fix the forms that the repairs must respect:

- [Conventions of the Indices, the Notation and the Corpus](../articles_maths/conventions-of-the-indices-the-notation-and-the-corpus.html) gives the subscript rules and the admitted forms.
- [Conventions of the Matrix Models](../articles_maths/conventions-of-the-matrix-models.html) and its [physics counterpart](../articles_physics/conventions-of-the-matrix-models.html) define $\iota_{\mathrm{Cl}}$ and its cells.

The three exemplars of the audit are:

- [The Integers](../articles_maths/the-integers.html) for the bare embedding $\mathbb{N}\to\mathbb{Z}$.
- [Quaternion Involutions and Projections](../articles_maths/quaternion-involutions-and-projections.html) for the axis family and its numeral spellings.
- [The Newman–Penrose Formalism in Biquaternionic Form](../articles_physics/the-newman-penrose-formalism-in-biquaternionic-form.html) for the spinor $\iota$ and its components.

[The Upper Indexes Problem](the-upper-indexes-problem.html) applies the same audit method to the index conventions and is the model for this inventory.
