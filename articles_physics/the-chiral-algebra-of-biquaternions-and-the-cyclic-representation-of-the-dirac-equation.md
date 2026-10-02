# __The Chiral Algebra of Biquaternions and the Cyclic Representation of the Dirac Equation__

## Introduction

The corpus already carries several biquaternionic readings of the Dirac equation. *The Dirac Equation in Biquaternionic Form* writes it with the corpus's own basis $e_0, e_1, e_2, e_3$, the Hamilton product and the elliptic factorisation $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural}$. *The Dirac Algebra and Biquaternions — A Dictionary* records the isomorphism with $\mathrm{Cl}_{1,3}$. *Exercise: Chirality and the Weyl Spinors* treats the two chiral halves with the standard projectors $\tfrac12(1 \pm \gamma_5)$. The article recorded here is a fourth reading, and it is built on a purpose-made algebra rather than on the corpus's basis.

The source is Sergey Y. Kotkovskiy, *Chiral algebra of Dirac equation*, the version marked v3 (February 2026) of the file whose printed identifier is `2502.0126`; an earlier version, marked v2 (March 2025), is titled *Cyclic representation of the Dirac equation* and differs from the digested text in one mathematical place only — the map of the Appendix's second matrix isomorphism, which the author rewrote between the two versions — so the two are recorded here as one source. Twenty-eight pages in two parts. Part 1, *Chiral algebra*, constructs an **isotropic (light) basis** of the biquaternion space out of nullquaternions, defines **signed biquaternions** and **projectors**, introduces **four types of biquaternion multiplication** — outer, inner, diagonal and crossing — and three **exchange conjugations**. Part 2, *Dirac equation*, adds a fourth operation, **cyclic conjugation**, which is a four-cycle of the coordinates, and writes the Dirac equation as a single expression that contains both chiralities: the **cyclic representation**. The paper then derives an analogue of the Lorentz transformation, a **rotation transformation** that it reads as the creation of the particle's proper rotation, an expression of the cyclic transformation through a **complex Hadamard matrix**, and four equivalent representations in projectors; and it gives the concrete spin machinery — the spin-projection operators become the Pauli matrices under a further matrix correspondence, and the exchange conjugation is the longitudinal spin flip. The Appendix attaches a $2\times2$ matrix to every biquaternion and claims two isomorphisms — the outer product as the ordinary matrix product, and the inner product as a matrix product with the second term of each entry **subtracted**; the first is exact, the second is not (see *The Matrix Isomorphisms*), and the product that beside the outer one really is an ordinary matrix product is the **diagonal** one. The author identifies the isotropic-basis machinery with a model of the genetic code he has published elsewhere, and reads the Hadamard matrix as the informational aspect of the Dirac equation.

The article is written to separate three things. First, **the apparatus**, which is the real contribution: the isotropic basis, the four multiplication types, the three exchange conjugations, the cyclic conjugation and the matrix isomorphisms are all new to the corpus, and most of them are exactly verifiable. Second, **the reformulation**, which is a genuine equivalence: the component system the author writes out is exactly the Weyl system under his correspondence, and this was verified. Third, **the physical readings**, which are the author's speculations and are labelled as such here — the rotation transformation, the identification of spin with the cyclic operation, the superluminal variant, and the reading of the Hadamard matrix and the genetic code.

The plan is the basis, then the operations on it, then the representation, then the controls. The section *What Is Verified and What Is Not* collects every recomputation and every item that could not be read faithfully.

## The Chiral Algebra

### The Scalar-Vector Biquaternion and the Corpus Dictionary

The paper uses Silberstein's scalar-vector form throughout: a biquaternion is a pair

$$
\mathcal{B} = (s, \mathbf{u}), \qquad s \in \mathbb{C}, \quad \mathbf{u} \in \mathbb{C}^3,
$$

and the author calls the ordinary product the **outer product**,

$$
\mathcal{B}_1 \odot \mathcal{B}_2 = \bigl(s_1s_2 + \mathbf{u}_1 \cdot \mathbf{u}_2,\; s_1\mathbf{u}_2 + s_2\mathbf{u}_1 + i\,\mathbf{u}_1 \times \mathbf{u}_2\bigr),
\tag{1}
$$

with $i$ the central scalar imaginary unit. Three cautions belong here, because all three are sources of confusion between this article and the corpus.

**The name "outer product" is a false friend.** The corpus's outer product is the antisymmetric part $p \wedge q = \tfrac12(pq - qp)$, a grade-2 object (*Biquaternion Algebra*, *The Outer Product and the Grades*). The paper's outer product is the **full product**, grade-0 and grade-2 together. The two must not be conflated.

**The product itself is not the corpus's product.** The corpus's product is the Hamilton product extended complex-linearly, $Q_0R_0 - (\mathbf{Q},\mathbf{R})$ in the scalar slot and $Q_0\mathbf{R} + R_0\mathbf{Q} + [\mathbf{Q},\mathbf{R}]$ in the vector slot. The paper's (1) carries $+\mathbf{u}_1 \cdot \mathbf{u}_2$ and $+i\,\mathbf{u}_1 \times \mathbf{u}_2$. On pure vectors the paper's product is therefore the Pauli product,

$$
\mathbf{u}_1 \odot \mathbf{u}_2 = \mathbf{u}_1 \cdot \mathbf{u}_2 + i\,\mathbf{u}_1 \times \mathbf{u}_2 \quad \longleftrightarrow \quad (\boldsymbol{\sigma}\cdot\mathbf{u}_1)(\boldsymbol{\sigma}\cdot\mathbf{u}_2) = (\mathbf{u}_1\cdot\mathbf{u}_2)I + i\,\boldsymbol{\sigma}\cdot(\mathbf{u}_1\times\mathbf{u}_2),
$$

and it differs from the corpus's Hamilton product in the sign of **both** the dot and the cross term. This is checked in *What Is Verified and What Is Not*. It is also why the author's spin 4-gradient $D_s = (\partial_t, \boldsymbol{\sigma}\cdot\nabla)$ coincides with half his 4-gradient $D$ (his equation (39)): a Pauli-type product is what the Pauli matrices satisfy.

**The three conjugate signs.** Complex conjugation is $\mathcal{B}^* = (s^*, \mathbf{u}^*)$, vector conjugation is $\bar{\mathcal{B}} = (s, -\mathbf{u})$ — the corpus's quaternion conjugate — and the double conjugate is $(s^*, -\mathbf{u}^*)$, which is the corpus's Hermitian adjoint. The **square modulus** is the corpus's norm,

$$
|\mathcal{B}|^2 = \mathcal{B}\bar{\mathcal{B}} = s^2 - \mathbf{u}^2 \in \mathbb{C}.
$$

### The Isotropic (Light) Basis

The basis is built from the objects of vanishing square modulus, which the author calls **nullquaternions** (the corpus's *Biquaternion Zero Divisors* and *The Null Cone*). There are two kinds.

**Nullvectors** are complex vectors of zero square, and each is the sum of two mutually orthogonal real vectors of equal length,

$$
\mathbf{q} = \mathbf{A} + i\mathbf{B}, \qquad \mathbf{A}, \mathbf{B} \in \mathbb{R}^3, \quad |\mathbf{A}| = |\mathbf{B}|, \quad \mathbf{A} \perp \mathbf{B}, \qquad \mathbf{q}^2 = 0.
$$

**Uniform nullquaternions** are the biquaternions

$$
N = \lambda(1, \mathbf{n}), \qquad \mathbf{n} \in \mathbb{R}^3, \quad |\mathbf{n}| = 1, \quad \lambda \in \mathbb{C},
$$

with the property that $\mathcal{B}\bar{\mathcal{B}} = 0$. The author normalises to $\lambda = \tfrac12$ and takes a right-handed triad $(\mathbf{A}, \mathbf{B}, \mathbf{n})$ with $\mathbf{A} \times \mathbf{B} = \mathbf{n}$. The **isotropic basis** is then the four nullquaternions

$$
\mathbf{q} = \tfrac12(\mathbf{A} + i\mathbf{B}), \qquad \mathbf{q}^* = \tfrac12(\mathbf{A} - i\mathbf{B}), \qquad N = \tfrac12(1, \mathbf{n}), \qquad \bar{N} = \tfrac12(1, -\mathbf{n}),
\tag{2}
$$

and its defining relations are

$$
\mathbf{q}\,\mathbf{q}^* = N, \qquad \mathbf{q}^*\,\mathbf{q} = \bar{N}, \qquad \mathbf{q}^2 = (\mathbf{q}^*)^2 = 0, \qquad N^2 = N, \qquad \bar{N}^2 = \bar{N}, \qquad N\bar{N} = \bar{N}N = 0.
\tag{3}
$$

Every one of the relations (3), and the right-handedness of the triad, was recomputed exactly.

The basis is not orthogonal in the ordinary sense but it is a **basis**: every biquaternion has a unique decomposition

$$
\mathcal{B} = \alpha\mathbf{q} + \beta\mathbf{q}^* + \xi N + \eta \bar{N}, \qquad \alpha, \beta, \xi, \eta \in \mathbb{C},
\tag{4}
$$

which splits into a **transverse** part $\mathbf{u} = \alpha\mathbf{q} + \beta\mathbf{q}^*$ lying in the plane $\Pi$ spanned by $\mathbf{A}$ and $\mathbf{B}$, and a **longitudinal** part $\mathcal{P} = \xi N + \eta\bar{N}$ whose vector part is along $\mathbf{n}$. On space-time the coordinates are the light-cone coordinates

$$
\alpha = x - iy, \qquad \beta = x + iy, \qquad \xi = t + z, \qquad \eta = t - z,
\tag{5}
$$

whence the derivatives

$$
\partial_\alpha = \tfrac12(\partial_x + i\partial_y), \qquad \partial_\beta = \tfrac12(\partial_x - i\partial_y), \qquad \partial_\xi = \tfrac12(\partial_t + \partial_z), \qquad \partial_\eta = \tfrac12(\partial_t - \partial_z).
\tag{6}
$$

Two remarks fix the relation to the corpus. The coordinates (5) are the corpus's **null coordinates** on the light cone, so the isotropic basis is the light-cone basis used as a *computational basis for the Dirac problem* — a choice the corpus does not make, although it uses null bases and the null quadric elsewhere (in particular in *The Spinor Module in Biquaternionic Form and Its Lorentz Action*, where the corpus notes that "$\mathbb{B}$ is the complexified quaternion algebra and its null cone is the obstacle"). And the decomposition (4) is a **Peirce-type decomposition** into two commuting idempotents $N$ and $\bar{N}$ with $N + \bar{N} = 1$ and $N\bar{N} = 0$; the corpus's *Biquaternion Ideals and Peirce Decomposition* records the same split, but in the corpus's own basis $\{e_0, e_1\}$ rather than in the light-cone basis.

### Signed Biquaternions and Projectors

Grouping the terms of (4) the other way gives the **signed** biquaternions: a *positive* signed biquaternion is of the form $\mathcal{B}^+ = \beta\mathbf{q}^* + \eta\bar{N}$, and a *negative* one is of the form $\mathcal{B}^- = \alpha\mathbf{q} + \xi N$. Every biquaternion is the sum of one of each, $\mathcal{B} = \mathcal{B}^+ + \mathcal{B}^-$, and the signed objects are exactly the Peirce components of the decomposition (4) with respect to the two idempotents.

The signed biquaternions are **projectors** for the crossing product of the next section: a positive projector on the left of any biquaternion returns a positive signed biquaternion, a negative projector returns a negative one, and the action on the right side reverses the sign. In coordinates, with $\mathcal{P}^+ = \beta\mathbf{q}^* + \eta\bar{N}$ and $\mathcal{P}^- = \alpha\mathbf{q} + \xi N$,

$$
\mathcal{P}^+ \rightsquigarrow \mathcal{B} = \mathcal{B}^{'+}, \qquad \mathcal{P}^- \rightsquigarrow \mathcal{B} = \mathcal{B}^{'-}, \qquad \mathcal{B} \rightsquigarrow \mathcal{P}^+ = \mathcal{B}^{''-}, \qquad \mathcal{B} \rightsquigarrow \mathcal{P}^- = \mathcal{B}^{''+},
\tag{7}
$$

for every $\mathcal{B}$. This was verified for one hundred random $\mathcal{B}$ and random projectors; see the closing section.

The correspondence with the corpus is again a Peirce correspondence but not an identity. The corpus's projectors are $\pi_\pm = \tfrac12(1 \pm e_1)$, with $\pi_+ \pi_- = 0$; the paper's $N$ and $\bar{N}$ play the same role for the light-cone direction $\mathbf{n}$, and the author's chiral projectors turn out to be the signed parts themselves. The corpus's chirality projectors are the $\tfrac12(1 \pm \gamma_5)$ of the matrix representation (*The Dirac Algebra and Biquaternions — A Dictionary*, *gamma-five and the chirality projectors*); the paper's are not $\gamma_5$ but the two Peirce components of the light-cone decomposition, which is a different split.

### The Four Multiplication Types

The paper introduces four products on the same four-dimensional space. They are distinguished by which pairs of coordinates are multiplied, which the author motivates by the matrix isomorphisms of his Appendix: the outer product corresponds to ordinary matrix multiplication, the inner product to matrix multiplication with subtractions in place of the additions, the diagonal product to a diagonal pairing, and the crossing product to a combination of the first two. The four formulas, in the coordinates (4), are

$$
\begin{aligned}
\mathcal{B}_1 \odot \mathcal{B}_2 &= (\xi_1\alpha_2 + \alpha_1\eta_2)\,\mathbf{q} + (\eta_1\beta_2 + \beta_1\xi_2)\,\mathbf{q}^* + (\alpha_1\beta_2 + \xi_1\xi_2)\,N + (\beta_1\alpha_2 + \eta_1\eta_2)\,\bar{N}, \\[2pt]
\mathcal{B}_1 \otimes \mathcal{B}_2 &= (\alpha_1\alpha_2 + \xi_1\eta_2)\,\mathbf{q} + (\beta_1\beta_2 + \eta_1\xi_2)\,\mathbf{q}^* + (\beta_1\xi_2 + \xi_1\alpha_2)\,N + (\alpha_1\eta_2 + \eta_1\beta_2)\,\bar{N}, \\[2pt]
\mathcal{B}_1 \times \mathcal{B}_2 &= (\alpha_1\alpha_2 + \beta_1\xi_2)\,\mathbf{q} + (\alpha_1\beta_2 + \beta_1\eta_2)\,\mathbf{q}^* + (\xi_1\alpha_2 + \eta_1\xi_2)\,N + (\xi_1\beta_2 + \eta_1\eta_2)\,\bar{N}, \\[2pt]
\mathcal{B}_1 \rightsquigarrow \mathcal{B}_2 &= \eta_1\xi_2\,\mathbf{q} + \xi_1\eta_2\,\mathbf{q}^* + \alpha_1\beta_2\,N + \beta_1\alpha_2\,\bar{N}.
\end{aligned}
\tag{8}
$$

**Outer.** The first is a rewriting of (1) in the isotropic coordinates, and it is the one product that is known independently through the matrix isomorphism: $\mathcal{B} \leftrightarrow M = \left(\begin{smallmatrix}\xi & \alpha\\ \beta & \eta\end{smallmatrix}\right)$ turns the outer product into the ordinary product of $2\times2$ matrices. The identity of the coordinate formula with the direct Silberstein product was verified on one hundred random pairs to a residual of $2.5\times10^{-16}$. The outer product is associative, basis-independent, and reproduces the basis relations (3) — the last of which is the reason $N$ and $\bar{N}$ are idempotent.

**Inner.** The second product has the striking properties the author advertises, all of them verified exactly: $\mathbf{q} \otimes \mathbf{q} = \mathbf{q}$ and $\mathbf{q}^* \otimes \mathbf{q}^* = \mathbf{q}^*$ (the nullvectors are idempotent under it), $\mathbf{q} \otimes \mathbf{q}^* = \mathbf{q}^* \otimes \mathbf{q} = 0$, $N \otimes N = \bar{N} \otimes \bar{N} = 0$, $N \otimes \bar{N} = \mathbf{q}$ and $\bar{N} \otimes N = \mathbf{q}^*$, and the inner product of two complex numbers is a vector, $\lambda_1 \otimes \lambda_2 = \lambda_1\lambda_2 \mathbf{A}$. The author also advertises a failure of distributivity, and this requires care, because the product is bilinear and therefore distributive: it is **compatibility with scalar multiplication** that fails, not distributivity. For the scalar element $\lambda N + \lambda\bar{N}$ and a biquaternion $\mathcal{B} = \alpha\mathbf{q} + \beta\mathbf{q}^* + \xi N + \eta\bar{N}$ one has

$$
\lambda \otimes \mathcal{B} = \lambda\bigl(\eta\,\mathbf{q} + \xi\,\mathbf{q}^* + \alpha\,N + \beta\,\bar{N}\bigr) \neq \lambda\mathcal{B}
     = \lambda\alpha\,\mathbf{q} + \lambda\beta\,\mathbf{q}^* + \lambda\xi\,N + \lambda\eta\,\bar{N},
$$

a shift of the four coordinates, verified on one hundred random pairs; distributivity in the second argument was verified at the same time and holds. The source's phrasing is a slip, and the displayed rule is the property it points to. All the listed inner-product properties are exact. The inner product is neither associative nor basis-independent, in contrast with the outer product; the author states this and explains that the alternative matrix isomorphism reverses the two roles.

**Diagonal.** The third is the product the author uses for spin. The corpus has no analogue of it.

**Crossing.** The fourth combines the outer product of the transverse parts with the inner product of the longitudinal parts,

$$
\mathcal{B}_1 \rightsquigarrow \mathcal{B}_2 = \mathbf{u}_1 \odot \mathbf{u}_2 + \mathcal{P}_2 \otimes \mathcal{P}_1.
\tag{9}
$$

Two points must be recorded about (9). First, the **order of the inner factor**: the printed coordinates of the crossing product, in the extraction, match (9) with the inner factor in the order $\mathcal{P}_2 \otimes \mathcal{P}_1$, and not with the order $\mathcal{P}_1 \otimes \mathcal{P}_2$ (residual $1.7\times10^{-16}$ against residual $1.08$ on the same pair). Either the paper's inner product is ordered oppositely to (8), or the term order in the author's sentence "$\mathbf{u}_1 \odot \mathbf{u}_2 + \mathcal{P}_1 \otimes \mathcal{P}_2$" is a slip; the extraction cannot settle it, because the inner product is not commutative. Second, it is exactly this product, with the printed coordinate assignment, that makes the projector law (7) hold, and that law was verified for one hundred random biquaternions. So the printed coordinate formula is the correct one, whatever the term order in the sentence.

### The Basis Product Table

The source collects the pairwise products of the four basis elements under the outer and the inner product in a table (its Table 1), and the table is the clearest single statement of how the two products differ. Recomputed here in full, left factor by row and right factor by column:

| $\odot$ | $\mathbf{q}$ | $\mathbf{q}^*$ | $N$ | $\bar{N}$ |
|---|---|---|---|---|
| $\mathbf{q}$ | $0$ | $N$ | $0$ | $\mathbf{q}$ |
| $\mathbf{q}^*$ | $\bar{N}$ | $0$ | $\mathbf{q}^*$ | $0$ |
| $N$ | $\mathbf{q}$ | $0$ | $N$ | $0$ |
| $\bar{N}$ | $0$ | $\mathbf{q}^*$ | $0$ | $\bar{N}$ |

| $\otimes$ | $\mathbf{q}$ | $\mathbf{q}^*$ | $N$ | $\bar{N}$ |
|---|---|---|---|---|
| $\mathbf{q}$ | $\mathbf{q}$ | $0$ | $0$ | $\bar{N}$ |
| $\mathbf{q}^*$ | $0$ | $\mathbf{q}^*$ | $N$ | $0$ |
| $N$ | $N$ | $0$ | $0$ | $\mathbf{q}$ |
| $\bar{N}$ | $0$ | $\bar{N}$ | $\mathbf{q}^*$ | $0$ |

The structural reading is that **the two products exchange idempotents and nilpotents**: $N$ and $\bar{N}$ are idempotent for the outer product ($N\odot N = N$, $\bar{N}\odot\bar{N} = \bar{N}$) and nilpotent for the inner one ($N\otimes N = \bar{N}\otimes\bar{N} = 0$), while $\mathbf{q}$ and $\mathbf{q}^*$ do the opposite ($\mathbf{q}\odot\mathbf{q} = 0$ but $\mathbf{q}\otimes\mathbf{q} = \mathbf{q}$). The source's own summary of the table has this second half inverted: it says that $\mathbf{q}$ and $\mathbf{q}^*$ are nilpotent for the inner product and idempotent for the outer, which is the reverse of what its table and the formulas give, and it writes the outer-product symbol where the inner one is meant. The table is right and the sentence is not. Two further defects of the table as extracted: its outer block prints both $N\odot\mathbf{q} = \mathbf{q}$ and $N\odot\mathbf{q} = 0$, which cannot both hold, and the computation gives $N\odot\mathbf{q} = \mathbf{q}$ with $\bar{N}\odot\mathbf{q} = 0$ — so a bar is lost in one of the two — while the mirror entry of the same block is printed $\bar{N}\odot\mathbf{q}^* = 0$ where the computation gives $\bar{N}\odot\mathbf{q}^* = \mathbf{q}^*$ and $N\odot\mathbf{q}^* = 0$; in both places a bar is misplaced, in opposite directions.

### The Matrix Isomorphisms

The Appendix of the paper gives two isomorphisms of $\mathbb{B}$ with the $2\times2$ complex matrices, one attached to each of the two products it treats in matrix form; the first is correct, the second is not. The first is the one the whole paper uses:

$$
\mathcal{B} = \alpha\mathbf{q} + \beta\mathbf{q}^* + \xi N + \eta\bar{N} \;\longleftrightarrow\; M = \begin{pmatrix} \xi & \alpha \\ \beta & \eta \end{pmatrix},
$$

and it turns the **outer** product into the ordinary product of matrices. This was verified exactly, residual zero on one hundred random pairs, so the outer product is, through this correspondence, just matrix multiplication — which is the source of its associativity and its basis-independence. The second attaches to the **inner** product a product of matrices in which the second product of every entry is **subtracted** instead of added (the Appendix, equations (81)–(82)); its map is printed as

$$
M = \begin{pmatrix} \xi & \alpha \\ -\beta & -\eta \end{pmatrix}
\qquad (\text{v2}), \qquad
M = \begin{pmatrix} \alpha & -\eta \\ \xi & -\beta \end{pmatrix}
\qquad (\text{v3}),
$$

with the same subtractive rule in both versions: if the printed matrices are read as $M = \left(\begin{smallmatrix} a_{11} & a_{21}\\ a_{12} & a_{22}\end{smallmatrix}\right)$, entry $(i,j)$ of the product is $a_{i1}b_{1j} - a_{i2}b_{2j}$, addition replaced by subtraction in the second term. **Neither form makes the inner product into a matrix product, and no correction of the map can.** The check was exhaustive: over all $4!$ orders in which the four coordinates $(\alpha,\beta,\xi,\eta)$ may be placed in the four matrix slots, all $2^4$ choices of entry signs, and the four pairing rules (add and subtract, with the two index orders) — $1536$ combinations, each required to give residual zero on twenty random pairs — **no** map realises the inner product. The reason is visible in the formulas: across the four coordinates the first terms of the inner product carry all four coordinates of the second factor, $\alpha_2, \beta_2, \xi_2, \eta_2$, whereas the first term of the rule can carry only two of them. The author's own revision is evidence that he knew the map was wrong — he changed it from v2 to v3 — but the corrected form fails the same test.

What *is* true, and is verified exactly, is that the **diagonal** product is an ordinary matrix product: under
$\mathcal{B} \leftrightarrow \left(\begin{smallmatrix} \alpha & \beta\\ \xi & \eta\end{smallmatrix}\right)$, with $M_{11}\leftrightarrow\mathbf{q}$, $M_{12}\leftrightarrow\mathbf{q}^*$, $M_{21}\leftrightarrow N$, $M_{22}\leftrightarrow\bar{N}$, the product of the images is the image of $\mathcal{B}_1 \times \mathcal{B}_2$ with residual zero; this is one of the eight realisations the same exhaustive search returns for the diagonal product, and the diagonal and the outer product are between them the only two of the four that have any. So the source's Appendix sentence — "if we replace outer multiplication by inner multiplication, then another isomorphism is established" — is true with the word **diagonal** in place of **inner**; the exchange-of-roles reading that the author draws from it (the inner product associative and basis-independent under the alternative correspondence) has no support, because the correspondence he exhibits is not an isomorphism at all.

The correspondence used for the **spin operators**, which is a sign-variant of the diagonal map just given, is stated in *The Spin Operators and the Spin States* below.

### The Exchange Conjugations

Beyond the corpus's conjugations, the paper defines three more by **permuting the coordinates** of (4). In the order $(\alpha, \beta, \xi, \eta)$,

$$
\mathcal{B}^{\bigstar} : (\alpha, \beta, \xi, \eta) \mapsto (\beta, \alpha, \eta, \xi), \qquad
\tilde{\mathcal{B}} : (\alpha, \beta, \xi, \eta) \mapsto (\xi, \eta, \alpha, \beta), \qquad
\mathcal{B}^{\bigstar\bigstar} : (\alpha, \beta, \xi, \eta) \mapsto (\eta, \xi, \beta, \alpha).
\tag{10}
$$

The first two are transpositions, the third is their composition. Their structural properties were verified: each is self-inverse; $\bigstar \circ \bigstar\bigstar = \bigstar\bigstar \circ \bigstar = \tilde{\phantom{x}}$, so applying two different ones gives the third; and all three commute with each other in the sense that the composed operations are independent of the order.

These are **not** algebra anti-automorphisms of the kind the corpus uses. The corpus's conjugations (complex, quaternion, Hermitian, and the Peirce projections) are $\mathbb{R}$-linear maps of $\mathbb{B}$ that interact with the product by reversing it; the paper's exchange conjugations are coordinate permutations of the isotropic basis, and they interact with the products of (8) by **changing the product type** rather than by reversing the order. This distinction is the substance of the author's equation

$$
\mathcal{B}_1 \otimes \mathcal{B}_2 = \mathcal{B}_2 \odot (\text{conjugate of } \mathcal{B}_1),
\tag{11}
$$

which the author calls the reversal of the multipliers with a change of product type. **Equation (11) could not be reproduced.** A search over all twenty-four coordinate permutations, both argument orders, and both product types found no permutation that turns the extracted inner product into the extracted outer product; the only matches were the trivial identity. The extraction of (11) is garbled — the conjugation symbols in it are lost — so this is a reporting limit, not a refutation, but (11) must not be used until it is read from the published text. This is the first of the flagged items.

### Cyclic Conjugation

The operation on which the whole reformulation turns is the **cyclic conjugation**, a four-cycle of the coordinates:

$$
\overset{⤺}{\mathcal{B}} : (\alpha, \beta, \xi, \eta) \mapsto (\beta, \xi, \eta, \alpha),
\tag{12}
$$

that is, $\overset{⤺}{\mathcal{B}} = \beta\mathbf{q} + \xi\mathbf{q}^* + \eta N + \alpha\bar{N}$ for $\mathcal{B} = \alpha\mathbf{q} + \beta\mathbf{q}^* + \xi N + \eta\bar{N}$. The diagram of the paper is a rotation of the four coordinates around the basis, which stays in place. The properties were verified exactly: the fourth iterate is the identity, so the operation generates a cyclic group of order four on every biquaternion; the second iterate is the exchange conjugation of the second type,

$$
\overset{⤺⤺}{\mathcal{B}} = \tilde{\mathcal{B}},
\tag{13}
$$

so the pair $\{1, \overset{⤺}{\phantom{x}}, \overset{⤺⤺}{\phantom{x}}, \overset{⤺⤺⤺}{\phantom{x}}\}$ is exactly the four-element cycle $\{1, g, \tilde{\phantom{x}}, g^{-1}\}$ with $\tilde{\phantom{x}}$ the involution of (10). The author's decomposition of the cyclic conjugation into exchange conjugations is a restatement of the same cycle and is consistent with (13).

The second iterate being an involution is what makes the cyclic conjugation usable in a wave equation: it is not an involution itself, but it is a fourth root of unity on the coordinates, and the author reads it as the "cyclic development" of the wave function as against the "linear development" carried by the derivatives.

## The Cyclic Representation

### Weyl Spinors and the Biquaternion Wave Function

The paper starts from the Weyl form of the Dirac equation,

$$
\partial_t\psi_L = -(\boldsymbol{\sigma}\cdot\nabla)\psi_L - im\,\psi_R, \qquad
\partial_t\psi_R = +(\boldsymbol{\sigma}\cdot\nabla)\psi_R - im\,\psi_L,
\tag{14}
$$

with $\psi_L = (u, v)_L^{\mathsf T}$ and $\psi_R = (u', v')_R^{\mathsf T}$, and rewrites it in the isotropic derivatives (6) as

$$
\partial_\xi u + \partial_\beta v = -im\,u', \qquad
\partial_\eta v + \partial_\alpha u = -im\,v', \qquad
\partial_\eta u' - \partial_\beta v' = -im\,u, \qquad
\partial_\xi v' - \partial_\alpha u' = -im\,v.
\tag{15}
$$

The **biquaternion wave function** is

$$
F = \mathbf{q}f_\alpha + \mathbf{q}^*f_\beta + Nf_\xi + \bar{N}f_\eta,
\tag{16}
$$

with complex scalar functions $f_\alpha, f_\beta, f_\xi, f_\eta$ of space-time, and the two chiral states are the two signed parts of (16):

$$
F^- = \mathbf{q}f_\alpha + Nf_\xi, \qquad F^+ = \mathbf{q}^*f_\beta + \bar{N}f_\eta, \qquad F = F^+ + F^-.
\tag{17}
$$

The correspondence with the Weyl components is

$$
u = f_\alpha, \qquad v = -f_\xi, \qquad u' = -f_\beta, \qquad v' = f_\eta,
\tag{18}
$$

so that the right-chiral state is the positive projector and the left-chiral state is the negative one: $F^- \sim \psi_L$ and $F^+ \sim \psi_R$. This is the paper's central identification, and it is a genuine - and rather pretty - statement: **the Weyl chirality is the sign of the Peirce component in the light-cone basis.** The corpus reaches the same two components by a different route, through the $\tfrac12(1 \pm \gamma_5)$ projectors of *The Dirac Algebra and Biquaternions — A Dictionary* and the two Weyl halves of *Exercise: Chirality and the Weyl Spinors*; the two descriptions agree on the split and disagree on what carries it. The corpus's chirality is carried by $\gamma_5$ in the matrix representation; the paper's is carried by the two null idempotents of the light-cone basis. The corpus's *Chiral Fermions in the Biquaternion Framework* is about a different question again — which chiral representations the framework admits — and must not be confused with the paper's "chiral algebra", which is a computational basis choice.

### The Gradients

The 4-gradient and its vector conjugate, written in the isotropic basis, are

$$
D = 2(\mathbf{q}\,\partial_\beta + \mathbf{q}^*\,\partial_\alpha + N\,\partial_\xi + \bar{N}\,\partial_\eta), \qquad
\bar{D} = 2(-\mathbf{q}\,\partial_\beta - \mathbf{q}^*\,\partial_\alpha + N\,\partial_\eta + \bar{N}\,\partial_\eta).
\tag{19}
$$

The author notes the inversion that looks like a slip and is not: the derivative $\partial_\alpha$ stands on $\mathbf{q}^*$ and $\partial_\beta$ on $\mathbf{q}$, which is the transpose of the coordinate pairing. The reason is that $D$ must reproduce $\partial_t$ and $\nabla$, and the $\alpha, \beta$ slots are exchanged by the vector conjugation. The factor $2$ is the price of the $\tfrac12$ normalisations in (2). The author also notes that his spin 4-gradient $D_s = (\partial_t, \boldsymbol{\sigma}\cdot\nabla)$ coincides with $\tfrac12 D$, which is the expression of the Pauli-product remark of the first section. The identity (19) was not verified beyond the consistency of the factors; it is quoted as the paper's statement.

### The Single-String Representation

The result the paper is built to reach is the **cyclic representation**,

$$
F^- \odot \bar{D} + D \otimes F^+ = im\,\overset{⤺}{F},
\tag{20}
$$

the Dirac equation for the biquaternion wave function $F$, written as one expression in which the two chiralities appear as the two signed parts $F^\pm$, the two gradient orderings appear as the two products $\odot$ and $\otimes$, and the mass appears on the right through the cyclic conjugate of $F$. Its component form, as printed, is

$$
\partial_\xi f_\alpha - \partial_\beta f_\xi = im\,f_\beta, \qquad
\partial_\eta f_\xi - \partial_\alpha f_\alpha = im\,f_\eta, \qquad
\partial_\eta f_\beta + \partial_\beta f_\eta = im\,f_\alpha, \qquad
\partial_\xi f_\eta + \partial_\alpha f_\beta = im\,f_\xi.
\tag{21}
$$

**This system is exactly the Weyl system (15).** Substituting (18) into (21) turns each of the four equations into the corresponding equation of (15), up to an overall sign of the whole equation, which is immaterial: the four coefficient vectors were compared symbolically, including the mass terms, and each of the four row-by-row equalities holds exactly. This is the substantive verification of the article, and it confirms the author's own statement that (20) "is equivalent to the original Dirac equation in Weyl spinors". The reader should also note what (20) is and is not: it is a **compactness** statement of the same kind the corpus makes for Maxwell and Dirac elsewhere, not a claim that one chirality is redundant. The expression contains both chiralities implicitly through the two products and the right-hand side; the two-chirality content is unpacked in the next subsection.

### The Separated Reading

The author unpacks (20) into two equations, one per chirality, by expanding the cyclic conjugate through the exchange conjugations:

$$
F^- \odot \bar{D} = im\,F^{+\bigstar}, \qquad
\bar{D} \otimes F^+ = im\,\breve{F}^- .
\tag{22}
$$

In the first, both sides are negative signed biquaternions, that is left-chiral states; in the second, both sides are positive, right-chiral states. The author reads this as the precise sense in which (20) "implicitly contains both equations", and as the answer to the objection that a single-string form must be hiding one of the two Weyl equations. Whether the pairing is right depends on the sign conventions of the three exchange conjugations, which are exactly the symbols that could not be read from the extraction (see the first flagged item); the *structure* — one equation per chirality, both sides the same sign — is what (22) asserts, and it is consistent with the projector law (7) of the crossing product.

### The Boost and the Energy–Momentum Operators

The paper treats one special Lorentz transformation, the boost of velocity $V = \tanh 2\theta$ along the chosen longitudinal direction $\mathbf{n}$, with the wave function written in the chiral algebra. In Weyl components the boost is

$$
\psi_L = \begin{pmatrix} u \\ v \end{pmatrix} \mapsto \begin{pmatrix} e^{-\theta} u \\ e^{\theta} v \end{pmatrix}, \qquad
\psi_R = \begin{pmatrix} u' \\ v' \end{pmatrix} \mapsto \begin{pmatrix} e^{\theta} u' \\ e^{-\theta} v' \end{pmatrix},
\tag{23}
$$

and in the algebra it is generated by two **Lorentz operators**, the longitudinal and the transverse one,

$$
L = N e^{\theta} + \bar{N} e^{-\theta}, \qquad \breve{L} = \mathbf{q}\, e^{-\theta}\, \mathbf{q}^*\, e^{\theta}.
\tag{24}
$$

The author's rule for moving such an operator from one side of a product to the other is $\mathcal{B} \odot L = \breve{L} \otimes \mathcal{B}$ for every $\mathcal{B}$, and he writes the boost as

$$
F \mapsto F' = F \odot L = \breve{L} \otimes F, \qquad F \mapsto F' = P^+ \odot L + \breve{L} \otimes P^- .
\tag{25}
$$

Two remarks. First, **the right-multiplication by $L$ is a genuine boost, and it was verified**: with $L = Ne^{\theta} + \bar{N}e^{-\theta}$ the components of $F \odot L$ are $f_\alpha e^{-\theta}$, $f_\beta e^{\theta}$, $f_\xi e^{\theta}$, $f_\eta e^{-\theta}$, which under the correspondence (18) is exactly the Weyl transformation (23), row by row. Second, **the two-product identity that would make the second form of (25) valid was not reproduced.** It is the reversal law of the first section over again: a numerical fit shows that no fixed biquaternion $\breve{L}$ makes $\mathcal{B} \odot L$ equal $\breve{L} \otimes \mathcal{B}$ for all $\mathcal{B}$ with the printed formulas of (8) (best-fit residual $0.72$ on a random $\mathcal{B}$). What the source calls the transverse Lorentz operator therefore does not act as a second form of the boost within the printed products. The boost stands as $F \odot L$.

The energy-momentum biquaternion $K = k_\alpha\mathbf{q} + k_\beta\mathbf{q}^* + k_\xi N + k_\eta\bar{N}$ transforms **two-sidedly**, unlike the one-sided wave function,

$$
K \mapsto K' = L^* \odot K \odot L = T^* \otimes K \otimes T,
\tag{26}
$$

and the 4-coordinate $Z$ transforms the same way; (26) is quoted as printed and was not recomputed. The Lorentz invariant built from $K$ and $Z$ is the phase

$$
\Phi = \epsilon t - \mathbf{k}\cdot\mathbf{r} = \tfrac12\bigl(-k_\beta\alpha - k_\alpha\beta + k_\eta\xi + k_\xi\eta\bigr),
\tag{27}
$$

whose right-hand side was verified to reduce to $\epsilon t - k_x x - k_y y - k_z z$ identically in the isotropic coordinates of (5). (The extraction garbles the last term; the correct partner of $k_\eta\xi$ is $k_\xi\eta$.)

### Plane Waves and the Dispersion Relation

The paper's simplest solution of the cyclic representation is the plane wave

$$
F = A e^{i\Phi} + B e^{-i\Phi},
\tag{28}
$$

with $\Phi$ the invariant phase (27) and $A, B$ constant biquaternions, the positive-frequency and negative-frequency amplitudes. Substituting $F = A e^{i\Phi}$ into the component system (21) makes it algebraic in the amplitudes; with the phase normalised so that $\partial_\alpha\Phi = -k_\beta$ and $\partial_\xi\Phi = k_\eta$, the four equations read

$$
k_\eta a_\alpha + k_\alpha a_\xi = m a_\beta, \qquad k_\beta a_\alpha + k_\xi a_\xi = m a_\eta, \qquad
k_\xi a_\beta - k_\alpha a_\eta = m a_\alpha, \qquad -k_\beta a_\beta + k_\eta a_\eta = m a_\xi,
\tag{29}
$$

whose first two determine the longitudinal amplitudes $a_\xi, a_\eta$ from the free pair $a_\alpha, a_\beta$; the remaining two are then satisfied identically precisely when

$$
\epsilon^2 - \mathbf{k}^2 = k_\xi k_\eta - k_\alpha k_\beta = m^2 .
\tag{30}
$$

Both statements were verified: the identity $k_\xi k_\eta - k_\alpha k_\beta = \epsilon^2 - |\mathbf{k}|^2$ is exact for the coordinates of (5), and the system (29) closes on one hundred random on-shell momenta with residual below $10^{-14}$. The printed amplitude relations of the source are garbled in the extraction; (29) is their clean form, and it reproduces the one readable relation, $a_\xi = (m a_\beta - k_\eta a_\alpha)/k_\alpha$. The normalisation of the phase relative to (27) — the source's phase carries a factor $\tfrac12$ that the amplitude relations do not — is not settled by the extraction. At rest, $\mathbf{k} = 0$ and $k_\xi = k_\eta = m$, and the wave becomes $F = A_0 e^{imt} + B_0 e^{-imt}$ with constant coefficients, the author's starting point for the spin states below.

### The Spin Operators and the Spin States

The spin treatment is the paper's most concrete physical addition, and it rests on a **third matrix correspondence**, this one for the diagonal product. Writing the two chiral Weyl states as $2\times2$ matrices rather than columns,

$$
\psi_L = \begin{pmatrix} u & 0 \\ v & 0 \end{pmatrix}, \qquad
\psi_R = \begin{pmatrix} 0 & u' \\ 0 & v' \end{pmatrix}, \qquad
\psi = \psi_L + \psi_R = \begin{pmatrix} u & u' \\ v & v' \end{pmatrix},
\tag{31}
$$

the biquaternion $F$ maps to

$$
F = f_\alpha\mathbf{q} + f_\beta\mathbf{q}^* + f_\xi N + f_\eta\bar{N} \;\longleftrightarrow\; \psi = \begin{pmatrix} f_\alpha & -f_\beta \\ -f_\xi & f_\eta \end{pmatrix},
\tag{32}
$$

which is the correspondence (18) again, and the author's isomorphism is

$$
\psi_1\psi_2 \;\longleftrightarrow\; F_1 \times F_2 ,
\tag{33}
$$

ordinary matrix multiplication on the left and the **diagonal** product on the right. This was verified exactly — residual zero on one hundred random pairs — and it is a clean new result: the diagonal product is ordinary matrix multiplication, so outer ($\odot$) and diagonal ($\times$) are two different associative products on the same four-dimensional space, with different coordinate maps.

Under (33) the spin-projection operators become the Pauli matrices. The author writes them as biquaternions acting by the diagonal product on the left,

$$
\hat{S}_x = -(\mathbf{q}^* + N), \qquad \hat{S}_y = i(\mathbf{q}^* - N), \qquad
\hat{S}_z = \mathbf{q} - \bar{N}, \qquad \hat{S}_t = \mathbf{q} + \bar{N},
\tag{34}
$$

whose images under (32) are $\sigma_x$, $\sigma_y$, $\sigma_z$ and the identity, with $\hat{S}_t$ the unit of the diagonal product. Two bars are lost in the extraction, which prints $\hat{S}_z = \mathbf{q} - N$ and $\hat{S}_t = \mathbf{q} + N$, forms that do not map to $\sigma_z$ and the identity; (34) is the bar-restored version, and with it the images are exactly the Pauli matrices. The eigenstates are

$$
\begin{aligned}
F_{x\uparrow} &= f_\alpha\mathbf{q} + f_\beta\mathbf{q}^* - f_\alpha N - f_\beta\bar{N}, &\quad
F_{x\downarrow} &= f_\alpha\mathbf{q} + f_\beta\mathbf{q}^* + f_\alpha N + f_\beta\bar{N}, \\
F_{y\uparrow} &= f_\alpha\mathbf{q} + f_\beta\mathbf{q}^* - i f_\alpha N - i f_\beta\bar{N}, &\quad
F_{y\downarrow} &= f_\alpha\mathbf{q} + f_\beta\mathbf{q}^* + i f_\alpha N + i f_\beta\bar{N}, \\
F_{z\uparrow} &= f_\alpha\mathbf{q} + f_\beta\mathbf{q}^*, &\quad
F_{z\downarrow} &= f_\xi N + f_\eta\bar{N},
\end{aligned}
\tag{35}
$$

with the eigenvalue relations

$$
\hat{S}_j \times F_{j\uparrow} = F_{j\uparrow}, \qquad \hat{S}_j \times F_{j\downarrow} = -F_{j\downarrow}
\tag{36}
$$

for $j = x, y, z$. All six relations of (36) were verified with the bar-restored operators (34), which is what fixes (34); the extraction's unbarred forms do not satisfy them.

The author then reads the **exchange conjugation of the second type** as the longitudinal spin flip: it exchanges the two $z$ states, $\tilde{F}_{z\uparrow} = F_{z\downarrow}$ and $\tilde{F}_{z\downarrow} = F_{z\uparrow}$, verified exactly. Since this exchange conjugation is the square of the cyclic conjugation (13), and the cyclic conjugation is what stands on the right-hand side of the Dirac equation, he concludes that **cyclic conjugation is the operation that gives the particle its spin**, and reads the four-cycle as a half-flip that passes through a spin-zero state. The cyclic conjugate of the rest state $a_1\mathbf{q} + a_1\mathbf{q}^*$ is

$$
\overset{⤺}{F_{z\uparrow}} = a_1(\mathbf{q} + \bar{N}),
\tag{37}
$$

whose longitudinal spin vanishes, $\langle s_z\rangle = 0$ — verified from the matrix $\psi = a_1 I$ of (32), against which $\sigma_z$ has zero trace. (The extraction prints (37) with two components exchanged; the displayed form is the one the four-cycle (12) actually produces.) The author calls (37) the positive-frequency **zero state of spin**. The physical reading — spin created by the cyclic operation, halved by its square, and the two chiralities carried by the two products — is the author's; what is verified is the algebra of (31)–(37).

### Cyclic Conjugation in Cartesian Coordinates and the Hadamard Matrix

The author computes what the cyclic conjugation (12) becomes when the wave function is written in the Cartesian components $(f_x, f_y, f_z, f_t)$ rather than in the isotropic ones. Using the inverse of (5), the four-cycle becomes a matrix with entries in $\{\pm1, \pm i\}$, and the author's point is that this matrix is a **complex Hadamard matrix** $H_4$, with $H_4H_4^\dagger = 4I$ and all entries of modulus $1$; he then reads this as an informational aspect of the Dirac equation and connects it to Walsh functions, to noise-resistant coding, and to a genetic-code model he has published elsewhere.

The matrix is printed in the paper (equation (78)) as

$$
H_4 = \begin{pmatrix}
1 & i & 1 & 1 \\
i & -1 & -i & -i \\
-1 & i & -1 & 1 \\
1 & -i & -1 & 1
\end{pmatrix},
$$

and it satisfies both Hadamard properties: every entry has modulus $1$, and $H_4H_4^\dagger = 4I$, both recomputed here. It is **not** quite the matrix of the four-cycle (12) in the Cartesian components, and the difference is worth recording because it is invisible in the Hadamard property. Reading the four-cycle through the coordinates (5), it acts on the Cartesian components as $(f_x',f_y',f_z',f_t') = \tfrac12 D\,(f_x,f_y,f_z,f_t)$ with

$$
\tfrac12 D = \frac12\begin{pmatrix}
1 & i & 1 & 1 \\
-i & 1 & i & i \\
-1 & i & -1 & 1 \\
1 & -i & -1 & 1
\end{pmatrix},
$$

which is $H_4$ with the **second row negated**, and the overall factor $\tfrac12$ absent from the printed matrix. The sign of that row is the one obtained from $f_y' = \tfrac{i}{2}(\alpha' - \beta')$; the inverse of $f_y = (\alpha-\beta)/(2i)$ gives $\tfrac{i}{2}(\beta' - \alpha')$ instead. So the printed $H_4$ is the four-cycle composed with a reversal of the $y$ orientation. Since negating a whole row preserves both Hadamard properties, the author's mathematical claim — that the cyclic conjugation *is* a complex Hadamard transvection on the Cartesian components — holds whichever orientation is meant, and the discrepancy is a sign convention of the coordinate transformation rather than an error in the Hadamard statement. Whether the Hadamard structure "indicates the informational aspect of the Dirac equation" is a separate question, and it is the author's interpretation; the corpus records the Hadamard gate in the quantum-gates article in the standard real-valued setting, and nothing in the present article bears on that.

### The Lorentz Analogue, the Rotation Transformation and the Superluminal Variant

The remaining physical items are recorded as the author's claims. The boost, the plane-wave solutions and the spin operators are constructed in the sections above; the caveat here is that the machinery behind the following three was not verifiable from the extraction.

**The Lorentz analogue.** The boost is the construction of *The Boost and the Energy–Momentum Operators* above: the author writes it in the same two-product form as the cyclic representation and reads the structural similarity between the boost and the equation itself.

**The rotation transformation.** The author argues that because the cyclic conjugate sits on the right-hand side of (20), the left-hand side *is* the operation that creates it, and calls this the **rotation transformation**. Splitting the plane wave into its positive- and negative-frequency parts $Q_1 = Ae^{i\Phi}$ and $Q_2 = Be^{-i\Phi}$, he forms the **subtractive components** $Q^\pm = Q_1^\pm - Q_2^\pm$ and writes the transformation as $F \mapsto Q^- \odot K + \bar{K} \otimes Q^+$ with the energy-momentum biquaternion $K$. The claim is that this transformation is the analogue of the Lorentz boost for the particle's **proper rotation**, that is for spin, and the author states explicitly that the translational partner of the transformation "remains open". In the corpus, the corresponding machinery is rotor conjugation, $A \mapsto \Lambda A \Lambda^{*}$ (*The Lorentz Transformation as a Biquaternionic Rotation*); the paper's rotation transformation is not rotor conjugation — it uses two different products and the subtractive components, not a conjugate pair — so it is a candidate for a genuinely different construction. It should be checked against the corpus's rotor action before any claim of novelty is repeated.

**The superluminal variant.** Flipping the sign of the two products, $F^- \odot \bar{D} - D \otimes F^+ = im\overset{⤺}{F}$, gives the paper's **superluminal Dirac equation**, with the dispersion relation $\epsilon^2 - |\mathbf{k}|^2 = k_\xi k_\eta - k_\alpha k_\beta = -m^2$ in place of the subluminal one. The final algebraic step of this dispersion relation was verified — in the isotropic coordinates $k_\xi k_\eta - k_\alpha k_\beta = k_t^2 - k_x^2 - k_y^2 - k_z^2$ identically — so the superluminal branch follows from the sign as claimed. The physical reading of that branch is the author's, and the corpus's *Subluminal and Superluminal Electromagnetic Waves and the Lepton Mass Spectrum* records a different superluminal construction.

**The four representations.** The author states, without working them out, that the same treatment with the other three cyclic conjugations gives three more representations of the Dirac equation, all equivalent, and that the same holds for signed biquaternions in place of projectors. He also states that the representation has a form for a superluminal particle and that it "clearly reveals the time asymmetry" of the Dirac equation. These are announced, not developed.

## What Is Verified and What Is Not

**Verified by exact recomputation.** The isotropic basis and its relations (3), including the right-handedness of the triad; the identity of the isotropic coordinate formula for the outer product with the direct Silberstein product (1) — maximum residual $2.5\times10^{-16}$ over one hundred random pairs; the inner-product basis table, $\mathbf{q}\otimes\mathbf{q} = \mathbf{q}$, $\mathbf{q}^*\otimes\mathbf{q}^* = \mathbf{q}^*$, $\mathbf{q}\otimes\mathbf{q}^* = \mathbf{q}^*\otimes\mathbf{q} = 0$, $N\otimes N = \bar{N}\otimes\bar{N} = 0$, $N\otimes\bar{N} = \mathbf{q}$, $\bar{N}\otimes N = \mathbf{q}^*$; the announced properties of the inner product, $\lambda_1\otimes\lambda_2 = \lambda_1\lambda_2\mathbf{A}$ together with the failure of compatibility with scalar multiplication, distributivity in the second argument holding; the crossing product as $\mathbf{u}_1\odot\mathbf{u}_2 + \mathcal{P}_2\otimes\mathcal{P}_1$ (residual $1.7\times10^{-16}$); the projector law (7) for one hundred random biquaternions and random projectors; the self-inverse property, the transitivity, and the pair-composition of the three exchange conjugations; the four-cycle of the cyclic conjugation, $\overset{⤺}{}^{\,4} = 1$ and $\overset{⤺}{}^{\,2} = \tilde{\phantom{x}}$; the equivalence of the component system (21) with the Weyl system (15) row by row, including the mass terms; the sixteen pairwise products of the isotropic basis under the outer product and the sixteen under the inner product (the source's Table 1), each matching the coordinate formulas (23) and (24); the two matrix realisations that exist among the four products — the outer product equivalent to the ordinary $2\times2$ matrix product under $M = \left(\begin{smallmatrix}\xi & \alpha\\ \beta & \eta\end{smallmatrix}\right)$, and the diagonal product equivalent to the ordinary product under $M = \left(\begin{smallmatrix}\alpha & \beta\\ \xi & \eta\end{smallmatrix}\right)$ — and the non-existence of any realisation of the inner or the crossing product, by exhaustive search (see *The Matrix Isomorphisms*); the spin operators (34) mapping to the Pauli matrices and the six eigenvalue relations (36) with the bar-restored operators; the exchange conjugation swapping the two longitudinal spin states, and the vanishing of the longitudinal spin in the state (37); the boost as $F \odot L$ reproducing the Weyl transformation (23) component by component; the Lorentz-invariant phase identity (27); the closing of the plane-wave system (29) on one hundred random on-shell momenta to residual below $10^{-14}$; the Hadamard properties of the printed Cartesian matrix $H_4$, $|H_{4\,jk}| = 1$ and $H_4H_4^\dagger = 4I$, and its agreement with the matrix of the four-cycle up to the sign of one row; and the isotropic-coordinate identity behind the superluminal dispersion relation.

**Verified by computation, with a correction of the first reading.** Three extracted statements had to be corrected before they could be used, and this is recorded because the first readings, taken literally, fail. (a) **The crossing product's term order.** The coordinate formula matches the inner factor in the order $\mathcal{P}_2 \otimes \mathcal{P}_1$ and **not** $\mathcal{P}_1 \otimes \mathcal{P}_2$; the extracted coordinate formula is the one that makes the projector law hold, so it is used, and the extracted sentence's term order stays ambiguous. (b) **The inner product's advertised failure.** The source calls it a failure of distributivity; the product is distributive, and what fails is compatibility with scalar multiplication. (c) **Two lost bars in the spin operators.** The extracted $\hat{S}_z = \mathbf{q} - N$ and $\hat{S}_t = \mathbf{q} + N$ do not map to $\sigma_z$ and the identity, whereas the bar-restored forms of (34) do, and they are what makes the six eigenvalue relations (36) hold. In the same vein the state (37) is printed with two components exchanged, and the displayed form is the one the four-cycle produces.

**Not verified, and flagged.** (i) **The product-reversal law (11).** No coordinate permutation, in either argument order and for either product type, turns the extracted inner product into the extracted outer product; the only matches are trivial. The conjugation symbols in (11) are lost in the extraction, so the item is a reporting limit rather than a refutation, but (11) must not be used as quoted. (ii) **The signed-part assignment.** The extracted equation (18) of the source assigns the coordinates to the signed parts in a way that is inconsistent with the source's own equations (38) and (48) and with the projector law; the version used in this article is the one of (17), which is the internally consistent one. (iii) **The Appendix's second matrix isomorphism (81)–(82).** It is false, in both versions of the paper and for both of the maps printed (v2's $\left(\begin{smallmatrix}\xi & \alpha\\ -\beta & -\eta\end{smallmatrix}\right)$ and v3's $\left(\begin{smallmatrix}\alpha & -\eta\\ \xi & -\beta\end{smallmatrix}\right)$). No assignment of the four coordinates to the four matrix slots, with or without signs, realises the inner product as a matrix product with the printed subtractive rule, and the same holds for the additive rule; the reason is a counting one and is given in *The Matrix Isomorphisms*. What the Appendix should say is that the **diagonal** product is the second ordinary matrix product, and that statement is verified exactly. (iv) **The printed Hadamard matrix.** Read from both versions and verified: $|H_{4\,jk}| = 1$ and $H_4H_4^\dagger = 4I$ hold, and the matrix agrees with the four-cycle of (12) in the Cartesian components up to the sign of one row, so the Hadamard claim itself is sound. (v) **The gradient identity (19) and the claim $D_s = \tfrac12 D$.** Quoted from the source; only the factor structure was checked. (The factor of two is corroborated by the known Pauli-matrix relation $(\boldsymbol{\sigma}\cdot\mathbf{a})(\boldsymbol{\sigma}\cdot\mathbf{b}) = \mathbf{a}\cdot\mathbf{b} + i\boldsymbol{\sigma}\cdot(\mathbf{a}\times\mathbf{b})$, which is the pure-vector case of (1).) (vi) **The rotation transformation and the superluminal variant.** Recorded as the author's constructions; the rotation transformation's claimed difference from the corpus's rotor conjugation was not established. (vii) **The boost's two-product identity (25).** No fixed biquaternion $\breve{L}$ makes $\mathcal{B} \odot L$ equal $\breve{L} \otimes \mathcal{B}$ for all $\mathcal{B}$ with the printed products of (8); the numerical fit leaves a residual of $0.72$ on a random $\mathcal{B}$. It is the product-reversal law (11) in another guise, and like (11) it must not be used as quoted. The boost itself, as the right-multiplication $F \odot L$, is unaffected and was verified.

**What the source does not supply.** It does not work out the four alternative representations beyond their sign patterns, and it does not prove that they are equivalent to one another, only to the Weyl system. The construction of the Lorentz boost, the plane-wave solutions and the spin operators is present — the earlier sections of this article give it — but it rests on the exchange-conjugation identities that could not be read, so the boost's second form and the spin reading stand on the right-multiplication and the matrix isomorphism respectively. The paper does not present the inner product's non-associativity as a limitation, although it says the outer product is the associative one and the inner product is not, and it raises the division-algebra programme only in a closing paragraph. And the identification of the Hadamard structure with a genetic code is an external programme of the author's, cited in his bibliography, not a result of this article.

**The identifier.** The number printed on both versions is `2502.0126`, which is malformed — arXiv identifiers have a five-digit suffix. Queried on 27 September 2026, `arXiv:2502.0126` is *A Bayesian decision-theoretic approach to sparse estimation* by Li, Tokdar and Xu, an unrelated statistics paper, and a search of arXiv by the present title and by the author's name returns nothing on this work (only the author's *Nonlinear Maxwell equations*, arXiv:2403.00836, which the paper cites as reference [4]). So the paper appears not to be on arXiv under this number, and the identifier must not be propagated: cite the file, with its version, and treat the printed number as a typographical error of the author's.

**The two versions.** The corpus holds v2 (March 2025, *Cyclic representation of the Dirac equation*) and v3 (February 2026, *Chiral algebra of Dirac equation*), and they were compared word by word. The differences are seven and all small: the title; one clause of the abstract; the replacement of the Russian cross-reference placeholders ("source not found") by references to Appendix 1 and 2; the display of the Hadamard matrix, written for the Cartesian point coordinates in v2 and for the wave-function components in v3 (the same $H_4$ in both); the deletion of a stray clause; a change of e-mail address; and the map of the Appendix's second isomorphism, changed from $\left(\begin{smallmatrix}\xi & \alpha\\ -\beta & -\eta\end{smallmatrix}\right)$ to $\left(\begin{smallmatrix}\alpha & -\eta\\ \xi & -\beta\end{smallmatrix}\right)$. The last of these is the only mathematical change, and since both forms fail the same test it is a correction that did not repair the claim.

## Summary

The source builds a purpose-made **chiral algebra** of biquaternions and writes the Dirac equation in it as a single expression. The algebra starts from the light-cone basis: the four nullquaternions $\mathbf{q}$, $\mathbf{q}^*$, $N$, $\bar{N}$ of (2), with $\mathbf{q}\mathbf{q}^* = N$, $\mathbf{q}^*\mathbf{q} = \bar{N}$ and $N\bar{N} = 0$, in which every biquaternion has the unique light-cone decomposition (4) and splits into a transverse part in the null plane and a longitudinal part along the chosen real direction $\mathbf{n}$. That decomposition is the corpus's Peirce decomposition, moved to the light-cone basis. On it the paper defines three things new to the corpus. First, **four products** — outer, inner, diagonal and crossing — the outer one being the Pauli-type product $\mathbf{u}_1\cdot\mathbf{u}_2 + i\,\mathbf{u}_1\times\mathbf{u}_2$, which is not the corpus's Hamilton product and differs from it in the sign of the dot and the cross; the inner one having the remarkable properties $\mathbf{q}\otimes\mathbf{q} = \mathbf{q}$, $N\otimes\bar{N} = \mathbf{q}$, $\lambda_1\otimes\lambda_2 = \lambda_1\lambda_2\mathbf{A}$ and a genuine failure of compatibility with scalar multiplication; the crossing one being the projector law $\mathcal{P}^+\rightsquigarrow\mathcal{B} = \mathcal{B}^+$ that makes the two chiralities signed projectors. Second, **three exchange conjugations**, the coordinate permutations (10), which are not the corpus's conjugations but a change of product type. Third, **cyclic conjugation**, the four-cycle (12), whose fourth iterate is the identity and whose square is the exchange conjugation of the second type. The reformulation then reads: the biquaternion wave function (16) has the two Weyl chiralities as its two signed parts, $F^+ \sim \psi_R$ and $F^- \sim \psi_L$; the Dirac equation is the single expression $F^- \odot \bar{D} + D \otimes F^+ = im\overset{⤺}{F}$; its component form (21) is exactly the Weyl system under the correspondence (18), verified row by row; and the cyclic conjugation, read in Cartesian components, is the complex Hadamard matrix $H_4$. Around this the paper adds the machinery that makes the reading physical: the matrix picture, in which the outer product is the ordinary $2\times2$ matrix product and the diagonal product is the ordinary product under the map (32) — the Appendix's claimed second isomorphism, for the **inner** product, is false, and it is the diagonal that takes that place — a Lorentz boost acting by right-multiplication, whose components reproduce the Weyl boost, plane-wave solutions closing exactly on the mass shell $\epsilon^2 - \mathbf{k}^2 = m^2$, and the spin operators, which are the Pauli matrices under the diagonal-product isomorphism, with the exchange conjugation as the longitudinal spin flip. The apparatus is sound and largely verified; the equivalence is exact; the physical readings — the rotation transformation as the creator of the particle's proper rotation, the identification of the cyclic operation with spin, the superluminal branch, and the informational reading of the Hadamard matrix — are the author's. Three structural claims do not survive recomputation or could not be reproduced from the extracted text: the product-reversal law (11) and the boost's two-product identity (25), which could not be reproduced, and the Appendix's second matrix isomorphism (81)–(82), which is false in both printed forms.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra; the corpus's $e_0, e_1, e_2, e_3$ basis |
| $i$ | Central scalar imaginary unit, $i^2 = -1$ |
| $\mathcal{B} = (s, \mathbf{u})$ | Scalar-vector (Silberstein) form: complex scalar $s$, complex vector $\mathbf{u}$ |
| $\mathcal{B}^*, \bar{\mathcal{B}}, \bar{\mathcal{B}}^*$ | Complex, vector (quaternion), and double (Hermitian) conjugates |
| $\lvert\mathcal{B}\rvert^2 = \mathcal{B}\bar{\mathcal{B}} = s^2 - \mathbf{u}^2$ | Square modulus (complex) |
| $\mathbf{A}, \mathbf{B}, \mathbf{n}$ | Right-handed real triad, $\mathbf{A}\times\mathbf{B} = \mathbf{n}$, unit lengths |
| $\Pi$ | The null (transverse) plane spanned by $\mathbf{A}$ and $\mathbf{B}$ |
| $\mathbf{q} = \tfrac12(\mathbf{A}+i\mathbf{B}),\ \mathbf{q}^*$ | Nullvectors; $\mathbf{q}^2 = 0$ |
| $N = \tfrac12(1, \mathbf{n}),\ \bar{N}$ | Uniform nullquaternions (idempotents); $N^2 = N$, $N\bar{N} = 0$ |
| $\alpha, \beta, \xi, \eta$ | Isotropic coordinates: $\alpha = x-iy$, $\beta = x+iy$, $\xi = t+z$, $\eta = t-z$ |
| $\mathcal{B}^+, \mathcal{B}^-$ | Signed (positive, negative) biquaternions; the Peirce components |
| $\mathcal{P}^+, \mathcal{P}^-$ | Positive and negative projectors for the crossing product |
| $\odot, \otimes, \times, \rightsquigarrow$ | Outer, inner, diagonal and crossing products |
| $\bigstar, \tilde{\phantom{x}}, \bigstar\bigstar$ | The three exchange conjugations (coordinate permutations) |
| $\overset{⤺}{\phantom{x}}$ | Cyclic conjugation (the four-cycle) |
| $F = \mathbf{q}f_\alpha + \mathbf{q}^*f_\beta + Nf_\xi + \bar{N}f_\eta$ | Biquaternion wave function |
| $F^+ , F^-$ | Positive and negative signed parts; $\psi_R$ and $\psi_L$ |
| $u, v, u', v'$ | Weyl spinor components; $u = f_\alpha$, $v = -f_\xi$, $u' = -f_\beta$, $v' = f_\eta$ |
| $\boldsymbol{\sigma}$ | Pauli matrices, $\boldsymbol{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$ |
| $M = \left(\begin{smallmatrix}\xi & \alpha\\ \beta & \eta\end{smallmatrix}\right)$ | Matrix of $\mathcal{B}$; the outer product becomes the ordinary matrix product |
| $\psi = \left(\begin{smallmatrix} f_\alpha & -f_\beta\\ -f_\xi & f_\eta\end{smallmatrix}\right)$ | Matrix of $F$; the diagonal product becomes the ordinary matrix product |
| $k_\alpha, k_\beta, k_\xi, k_\eta, \epsilon$ | Energy-momentum in isotropic coordinates; $k_\xi k_\eta - k_\alpha k_\beta = \epsilon^2 - \mathbf{k}^2$ |
| $\Phi = \epsilon t - \mathbf{k}\cdot\mathbf{r}$ | Lorentz-invariant phase of the plane wave |
| $A, B$ | Positive- and negative-frequency amplitudes of the plane wave |
| $L = Ne^{\theta} + \bar{N}e^{-\theta},\ \breve{L}$ | Longitudinal and transverse Lorentz (boost) operators |
| $\hat{S}_x, \hat{S}_y, \hat{S}_z, \hat{S}_t$ | Spin-projection operators; the Pauli matrices under the diagonal isomorphism |
| $F_{j\uparrow}, F_{j\downarrow}$ | Spin eigenstates along $j = x, y, z$ |
| $D = (\partial_t, \nabla),\ \bar{D}$ | 4-gradient and its vector conjugate, in the paper's real-time convention |
| $D_s = \tfrac12 D$ | Spin 4-gradient, $D_s = (\partial_t, \boldsymbol{\sigma}\cdot\nabla)$ |
| $H_4$ | Complex Hadamard matrix of the cyclic conjugation in Cartesian components |
| $K$ | Energy-momentum biquaternion of the rotation transformation |
| $Q^\pm$ | Subtractive components in the rotation transformation |

## Further Reading

- Sergey Y. Kotkovskiy, *Chiral algebra of Dirac equation*, version v3 (February 2026); earlier version *Cyclic representation of the Dirac equation*, v2 (March 2025). The source of this article: the isotropic basis, the four multiplication types, the exchange and cyclic conjugations, the cyclic representation, the Hadamard expression, the matrix isomorphisms, the Lorentz boost, the plane waves, the spin operators and the rotation transformation. The paper prints the identifier `2502.0126`, which is malformed and belongs on arXiv to an unrelated statistics paper; no record of this work was found under that number, its title, or its author's name, so the two versions held in the corpus are the source of record.
- S. Ya. Kotkovsky, "Nullvector algebra", *Hypercomplex Numbers in Geometry and Physics* **2**(23) (2014), for the author's earlier nullvector algebra, the origin of the isotropic basis and the terminology of nullquaternions used throughout.
- V. V. Kravchenko, *Applied Quaternionic Analysis* (Heldermann, 2003), and the corpus's *The Dirac Equation in Biquaternionic Form* and *The Time-Harmonic Maxwell Operator and the Quaternionic Cauchy Integral*, for the standard biquaternionic Dirac machinery against which the paper's purpose-made algebra should be read.
- The corpus's *Biquaternion Algebra* (the Hamilton product and the corpus's outer product), *Biquaternion Ideals and Peirce Decomposition* (the idempotent split that the light-cone decomposition instances), *The Null Cone* and *Biquaternion Zero Divisors* (the vanishing-norm structure that the nullquaternions are), *The Spinor Module in Biquaternionic Form and Its Lorentz Action* (the chiral halves as left ideals), *Exercise: Chirality and the Weyl Spinors* and *The Dirac Algebra and Biquaternions — A Dictionary* (the $\gamma_5$ projectors, for comparison with the signed projectors used here), *Quantum Gates and Circuits in Biquaternionic Form* (the Hadamard gate in the ordinary setting), and *The Lorentz Transformation as a Biquaternionic Rotation* (rotor conjugation, the corpus's analogue of the paper's boost and the comparison object for its rotation transformation).
- P. A. M. Dirac, "The Quantum Theory of the Electron", *Proceedings of the Royal Society A* **117** (1928) 610–624, and L. Silberstein, "Quaternionic form of relativity", *Philosophical Magazine* **23** (1912) 790–809, for the Dirac equation and the scalar-vector biquaternion form the paper uses.
- K. J. Horadam, *Hadamard Matrices and Their Applications* (Princeton, 2007), for the complex Hadamard matrices of which the derived $H_4$ is an example, and for the standard theory behind the paper's informational reading.
