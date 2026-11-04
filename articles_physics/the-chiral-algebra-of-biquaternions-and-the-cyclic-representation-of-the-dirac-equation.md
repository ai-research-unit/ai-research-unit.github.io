# __The Chiral Algebra of Biquaternions and the Cyclic Representation of the Dirac Equation__

## Introduction

The corpus already carries several biquaternionic readings of the Dirac equation. *The Dirac Equation in Biquaternionic Form* writes it in the corpus's own units $e_t, \vec e_x, \vec e_y, \vec e_z$, with the Hamilton product and the elliptic factorisation $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural}$. *Matrix Representations Conventions*, §*The Clifford Structure and the Frame*, records the comparison with $\mathrm{Cl}_{1,3}$. *Exercise: Chirality and the Weyl Spinors* treats the two chiral halves by their two values. The article recorded here is a fourth interpretation, and it is built on a purpose-made algebra rather than on the corpus's units.

The source is Sergey Y. Kotkovskiy, *Chiral algebra of Dirac equation*, the version marked v3 (February 2026) of the file whose printed identifier is `2502.0126`; an earlier version, marked v2 (March 2025), is titled *Cyclic representation of the Dirac equation* and differs from the digested text in one mathematical place only — the map of the Appendix's second correspondence, which the author rewrote between the two versions — so the two are recorded here as one source. Twenty-eight pages in two parts. Part 1, *Chiral algebra*, constructs an **isotropic (light) basis** of the biquaternion space out of nullquaternions, defines **signed biquaternions**, introduces **four types of biquaternion multiplication** — outer, inner, diagonal and crossing — and three **exchange conjugations**. Part 2, *Dirac equation*, adds a fourth operation, **cyclic conjugation**, which is a four-cycle of the coordinates, and writes the Dirac equation as a single expression that contains both chiralities: the **cyclic representation**. The paper then derives an analogue of the Lorentz transformation, a **rotation transformation** that it reads as the creation of the particle's proper rotation, an expression of the cyclic transformation through a **complex Hadamard array**, and four equivalent representations of the same equation; and it gives the concrete spin machinery — the spin-projection operators become the three Pauli arrays under a further correspondence, and the exchange conjugation is the longitudinal spin flip. The Appendix attaches a two-by-two array to every biquaternion and claims two correspondences — the outer product as the ordinary product of arrays, and the inner product as a product with the second term of each entry **subtracted**; the first is exact, the second is not (see *The Appendix's Correspondences*), and the product that beside the outer one really is an ordinary product is the **diagonal** one. The author identifies the isotropic-basis machinery with a model of the genetic code he has published elsewhere, and reads the Hadamard array as the informational aspect of the Dirac equation.

The article is written to separate three things. First, **the apparatus**, which is the real contribution: the isotropic basis, the four multiplication types, the three exchange conjugations, the cyclic conjugation and the two correspondences of the Appendix are all new to the corpus, and most of them are exactly verifiable. Second, **the reformulation**, which is a genuine equivalence: the component system the author writes out is exactly the two-line chiral pair under his correspondence, and this was verified. Third, **the physical interpretations**, which are the author's speculations and are labelled as such here — the rotation transformation, the identification of spin with the cyclic operation, the superluminal variant, and the interpretation of the Hadamard array and the genetic code.

The plan is the basis, then the operations on it, then the representation, then the controls. The section *What Is Verified and What Is Not* collects every recomputation and every item that could not be read faithfully.

## The Chiral Algebra

**Notation, once.** The central imaginary unit is $i$, and $i^2=-1$. It is the only imaginary unit in the body: wherever two of them meet in a product they are reduced before the formula is read, $i\,i=-1$, and no formula below carries an unreduced $i^2$. Two elements of the algebra in one statement are numbered, $\mathcal{B}_1$ and $\mathcal{B}_2$, so the coordinates $\alpha_1,\beta_1,\xi_1,\eta_1$ and $\alpha_2,\beta_2,\xi_2,\eta_2$ always name the two factors and never a second component of one factor. The gammas are named once, in *The Legacy Pauli Gamma Formulation*. Every display below is an equation between elements; the arrays of the source are named where they are the subject of a sentence, and are not printed.

### The Scalar-Vector Biquaternion and the Corpus Dictionary

The paper uses Silberstein's scalar-vector form throughout: a biquaternion is a pair

$$
\mathcal{B} = (s, \vec q_a), \qquad s \in \mathbb{C}, \quad \vec q_a \in \mathbb{C}^3,
$$

and the author calls the ordinary product the **outer product**,

$$
\mathcal{B}_1 \odot \mathcal{B}_2 = \bigl(s_1s_2 + \vec q_{a,1} \cdot \vec q_{a,2},\; s_1\vec q_{a,2} + s_2\vec q_{a,1} + i\,\vec q_{a,1} \times \vec q_{a,2}\bigr),
\tag{1}
$$

with $i$ the central scalar imaginary unit. Three cautions belong here, because all three are sources of confusion between this article and the corpus.

**The name "outer product" is a false friend.** The corpus's outer product is the antisymmetric part $p \wedge q = \tfrac12(pq - qp)$, a grade-2 object (*Algebra and Element Conventions*, *The Outer Product and the Grades*). The paper's outer product is the **full product**, grade-0 and grade-2 together. The two must not be conflated.

**The product itself is not the corpus's product.** The corpus's product is the Hamilton product extended complex-linearly, $Q_tR_t - (\vec Q,\vec R)$ in the scalar slot and $Q_t\vec R + R_t\vec Q + [\vec Q,\vec R]$ in the vector slot. The paper's (1) carries $+\vec q_{a,1} \cdot \vec q_{a,2}$ and $+i\,\vec q_{a,1} \times \vec q_{a,2}$. On pure vectors the paper's product is therefore the one the three Pauli arrays satisfy,

$$
\vec q_{a,1} \odot \vec q_{a,2} = \vec q_{a,1} \cdot \vec q_{a,2} + i\,\vec q_{a,1} \times \vec q_{a,2},
$$

whereas the corpus's Hamilton product on the same two pure vectors is $-\vec q_{a,1}\cdot\vec q_{a,2} + \vec q_{a,1}\times\vec q_{a,2}$: the two differ in the sign of **both** the dot and the cross term. This is checked in *What Is Verified and What Is Not*. It is also why the author's spin gradient, which he writes as the scalar derivative $\partial/\partial t'$ beside the vector gradient $\nabla$, is the element $D$ of (18) itself in the paper's product, and not half of it: the algebra of his product is the algebra of that reading, and the source's own statement that the spin gradient is half of $D$ does not hold for the printed $D$ (see *What Is Verified and What Is Not*, item (v)).

**The three conjugations.** Complex conjugation is $\mathcal{B}^* = (s^*, \vec q_a^*)$, vector conjugation is $\bar{\mathcal{B}} = (s, -\vec q_a)$ — the corpus's quaternion conjugate — and the double conjugate is $(s^*, -\vec q_a^*)$, which is the corpus's Hermitian adjoint. The **square modulus** is

$$
|\mathcal{B}|^2 = \mathcal{B}\bar{\mathcal{B}} = s^2 - \vec q_a^2 \in \mathbb{C}, \qquad \vec q_a^2 \equiv \vec q_a\cdot\vec q_a = q_{a,x}^2 + q_{a,y}^2 + q_{a,z}^2 .
$$

The minus sign belongs to the paper's product, not to the corpus's: the scalar slot of (1) carries $+\vec q_{a,1}\cdot\vec q_{a,2}$, so $\mathcal{B}\bar{\mathcal{B}} = s^2 - \vec q_a^2$ in the dot square. The corpus's Hamilton product carries $-\vec q_{a,1}\cdot\vec q_{a,2}$ there and gives $s^2 + \vec q_a^2$, which is the biquaternion norm $\langle\tilde Q\rangle_{\natural} = Q_t^2 + Q_x^2 + Q_y^2 + Q_z^2$ of *Algebra and Element Conventions*. The flip is what the paper's construction needs: it is what makes the nullquaternions null, $N\bar{N} = \tfrac14(1 - \vec u\cdot\vec u) = 0$, and the isotropic basis rests on that.

### The Isotropic (Light) Basis

The basis is built from the objects of vanishing square modulus, which the author calls **nullquaternions** (the corpus's *N-Regularity and N-Degeneracy in the Biquaternion Algebra*, §*The Zero Divisors* and *The Null Cone*). There are two kinds.

**Nullvectors** are complex vectors of zero square, and each is the sum of two mutually orthogonal real vectors of equal length,

$$
\vec q = \vec A + i\vec B, \qquad \vec A, \vec B \in \mathbb{R}^3, \quad |\vec A| = |\vec B|, \quad \vec A \perp \vec B, \qquad \vec q^2 = 0.
$$

**Uniform nullquaternions** are the biquaternions

$$
N = \lambda(1, \vec u), \qquad \vec u \in \mathbb{R}^3, \quad |\vec u| = 1, \quad \lambda \in \mathbb{C},
$$

with the property that $\mathcal{B}\bar{\mathcal{B}} = 0$. The author normalises to $\lambda = \tfrac12$ and takes a right-handed triad $(\vec A, \vec B, \vec u)$ with $\vec A \times \vec B = \vec u$. The **isotropic basis** is then the four nullquaternions

$$
\vec q = \tfrac12(\vec A + i\vec B), \qquad \vec q^* = \tfrac12(\vec A - i\vec B), \qquad N = \tfrac12(1, \vec u), \qquad \bar{N} = \tfrac12(1, -\vec u),
\tag{2}
$$

and its defining relations are

$$
\vec q\,\vec q^* = N, \qquad \vec q^*\,\vec q = \bar{N}, \qquad \vec q^2 = (\vec q^*)^2 = 0, \qquad N^2 = N, \qquad \bar{N}^2 = \bar{N}, \qquad N\bar{N} = \bar{N}N = 0.
\tag{3}
$$

The basis is not orthogonal in the ordinary sense but it is a **basis**: every biquaternion has a unique decomposition

$$
\mathcal{B} = \alpha\vec q + \beta\vec q^* + \xi N + \eta \bar{N}, \qquad \alpha, \beta, \xi, \eta \in \mathbb{C},
\tag{4}
$$

which splits into a **transverse** part $\vec q_a = \alpha\vec q + \beta\vec q^*$ lying in the plane $\Pi$ spanned by $\vec A$ and $\vec B$, and a **longitudinal** part $\mathcal{P} = \xi N + \eta\bar{N}$ whose vector part is along $\vec u$. On space-time the coordinates are the light-cone coordinates

$$
\alpha = x - iy, \qquad \beta = x + iy, \qquad \xi = t' + z, \qquad \eta = t' - z,
\tag{5}
$$

whence the derivatives

$$
\partial/\partial\alpha = \tfrac12(\partial/\partial Q_x + i\partial/\partial Q_y), \qquad \partial/\partial\beta = \tfrac12(\partial/\partial Q_x - i\partial/\partial Q_y), \qquad \partial/\partial\xi = \tfrac12(\partial/\partial t' + \partial/\partial Q_z), \qquad \partial/\partial\eta = \tfrac12(\partial/\partial t' - \partial/\partial Q_z).
\tag{6}
$$

Two remarks fix the relation to the corpus. The coordinates (5) are the corpus's **null coordinates** on the light cone, so the isotropic basis is the light-cone basis used as a *computational basis for the Dirac problem* — a choice the corpus does not make, although it uses null bases and the null quadric elsewhere (in particular in *The Spinor Module in Biquaternionic Form and Its Lorentz Action*, where the corpus notes that "$\mathbb{B}$ is the complexified quaternion algebra and its null cone is the obstacle"). And the decomposition (4) is the light-cone writing of the corpus's **split into the two values of the subscript**: the two elements $N$ and $\bar{N}$ are the light-cone representatives of the two values, and the paper multiplies by them on the right, which is what makes its signed parts the two chiral halves. The corpus reads its own split on the left, and a left split is a **copy index**, not a value; that object plays no part in the paper, and the two must not be confused.

### Signed Biquaternions

Grouping the terms of (4) the other way gives the **signed** biquaternions: a *positive* signed biquaternion is of the form $\mathcal{B}^+ = \beta\vec q^* + \eta\bar{N}$, and a *negative* one is of the form $\mathcal{B}^- = \alpha\vec q + \xi N$. Every biquaternion is the sum of one of each, $\mathcal{B} = \mathcal{B}^+ + \mathcal{B}^-$, and the signed objects are the two **right components** of (4), $\mathcal{B}^+ = \mathcal{B}\bar{N}$ and $\mathcal{B}^- = \mathcal{B}N$: multiplication on the right by the two longitudinal elements. They are the two values of the chirality of the direction $\vec u$, as the paragraph after (7b) states.

The signed biquaternions are the two classes that the **crossing product** of the next section separates, but the two classes it preserves are not the two classes just named. With $\mathcal{P}^+ = \beta\vec q^* + \eta\bar{N}$ and $\mathcal{P}^- = \alpha\vec q + \xi N$, the crossing product defined in (8) gives, for every $\mathcal{B} = \alpha\vec q + \beta\vec q^* + \xi N + \eta\bar{N}$,

$$
\mathcal{P}^+ \rightsquigarrow \mathcal{B} = \eta_{\mathcal{P}^+}\,\xi\,\vec q + \beta_{\mathcal{P}^+}\,\alpha\,\bar{N}, \qquad
\mathcal{P}^- \rightsquigarrow \mathcal{B} = \xi_{\mathcal{P}^-}\,\eta\,\vec q^* + \alpha_{\mathcal{P}^-}\,\beta\,N,
\tag{7a}
$$

$$
\mathcal{B} \rightsquigarrow \mathcal{P}^+ = \xi\,\eta_{\mathcal{P}^+}\,\vec q^* + \alpha\,\beta_{\mathcal{P}^+}\,N, \qquad
\mathcal{B} \rightsquigarrow \mathcal{P}^- = \eta\,\xi_{\mathcal{P}^-}\,\vec q + \beta\,\alpha_{\mathcal{P}^-}\,\bar{N}.
\tag{7b}
$$

So the crossing product preserves the classes $\{\vec q,\bar{N}\}$ and $\{\vec q^*,N\}$, and it swaps them when the signed element moves from the left to the right; that is the precise content of the reversal the source states. The classes are **not** $\mathcal{B}^+$ and $\mathcal{B}^-$ of the line above, which are $\{\vec q^*,\bar{N}\}$ and $\{\vec q,N\}$: $\mathcal{P}^+\rightsquigarrow\mathcal{B}$ returns the coefficients $\xi,\alpha$ of $\mathcal{B}^-$, placed in the $\vec q,\bar{N}$ slots. The source writes the four relations with the labels $\mathcal{B}^{\pm}_{L,R}$, and the extraction does not settle the subscript convention; the algebra gives (7a)–(7b), and the labels of the source are the ones item (ii) of *What Is Verified* discusses. The article keeps the assignment (17) below, because that is the one that carries the two values.

The correspondence with the corpus is exact. The paper's $N=\tfrac12(1+\vec u)$ and $\bar N=\tfrac12(1-\vec u)$ are the light-cone elements for the direction $\vec u$, and under the dictionary that carries the paper's product into the Hamilton product, $\vec u\mapsto i\vec u$, they become the corpus's two light-cone elements. Read through the corpus's **chirality operator of the frame along $\vec u$** — the operator whose two values are the subscript, fixed in *Operator Chirality on the Biquaternion Algebra*, §*The Subscript on an Element*, and named $\chi_u$ below — the paper's two right components are the two values: $\mathcal{B}\bar N$ carries $R$ and $\mathcal{B}N$ carries $L$. The paper's signed split is therefore **the corpus's chirality split**, and the carrier of the split is the chirality operator of the frame along $\vec u$, not a second object beside it.

What is not the same is the corpus's older **left** split. The corpus's own two light-cone elements used on the left cut the algebra into two copies of one left-handed carrier, and that split is a copy index and not chirality. The paper's signed parts are right components, and they are chirality. The two splits are different, and only the second one is the one the paper needs.

### The Four Multiplication Types

The paper introduces four general products on the same four-dimensional space. They are distinguished by which pairs of coordinates are multiplied, which the author motivates by the correspondences of his Appendix: the outer product answers to the ordinary product of arrays, the inner product to a product with subtractions in place of the additions, the diagonal product to a diagonal pairing, and the crossing product to a combination of the first two. The four formulas, in the coordinates (4), are

$$
\begin{aligned}
\mathcal{B}_1 \odot \mathcal{B}_2 &= (\xi_1\alpha_2 + \alpha_1\eta_2)\,\vec q + (\eta_1\beta_2 + \beta_1\xi_2)\,\vec q^* + (\alpha_1\beta_2 + \xi_1\xi_2)\,N + (\beta_1\alpha_2 + \eta_1\eta_2)\,\bar{N}, \\[2pt]
\mathcal{B}_1 \otimes \mathcal{B}_2 &= (\alpha_1\alpha_2 + \xi_1\eta_2)\,\vec q + (\beta_1\beta_2 + \eta_1\xi_2)\,\vec q^* + (\beta_1\xi_2 + \xi_1\alpha_2)\,N + (\alpha_1\eta_2 + \eta_1\beta_2)\,\bar{N}, \\[2pt]
\mathcal{B}_1 \times \mathcal{B}_2 &= (\alpha_1\alpha_2 + \beta_1\xi_2)\,\vec q + (\alpha_1\beta_2 + \beta_1\eta_2)\,\vec q^* + (\xi_1\alpha_2 + \eta_1\xi_2)\,N + (\xi_1\beta_2 + \eta_1\eta_2)\,\bar{N}, \\[2pt]
\mathcal{B}_1 \rightsquigarrow \mathcal{B}_2 &= \eta_1\xi_2\,\vec q + \xi_1\eta_2\,\vec q^* + \alpha_1\beta_2\,N + \beta_1\alpha_2\,\bar{N}.
\end{aligned}
\tag{8}
$$

**Outer.** The first is a rewriting of (1) in the isotropic coordinates, and it is the one product that is known independently through the Appendix's first correspondence: the four coordinates placed in the four slots of a two-by-two array, $\xi$ and $\alpha$ in the first row and $\beta$ and $\eta$ in the second, turn the outer product into the ordinary product of arrays. The outer product is associative, basis-independent, and reproduces the basis relations (3) — the last of which is the reason $N$ and $\bar{N}$ square to themselves.

**Inner.** The second product has the striking properties the author advertises, all of them verified exactly: $\vec q \otimes \vec q = \vec q$ and $\vec q^* \otimes \vec q^* = \vec q^*$ (the nullvectors square to themselves under it), $\vec q \otimes \vec q^* = \vec q^* \otimes \vec q = 0$, $N \otimes N = \bar{N} \otimes \bar{N} = 0$, $N \otimes \bar{N} = \vec q$ and $\bar{N} \otimes N = \vec q^*$, and the inner product of two complex numbers is a vector, $\lambda_1 \otimes \lambda_2 = \lambda_1\lambda_2 \vec A$. The author also advertises a failure of distributivity, and this requires care, because the product is bilinear and therefore distributive: it is **compatibility with scalar multiplication** that fails, not distributivity. For the scalar element $\lambda N + \lambda\bar{N}$ and a biquaternion $\mathcal{B} = \alpha\vec q + \beta\vec q^* + \xi N + \eta\bar{N}$ one has

$$
\lambda \otimes \mathcal{B} = \lambda\bigl(\eta\,\vec q + \xi\,\vec q^* + \alpha\,N + \beta\,\bar{N}\bigr) \neq \lambda\mathcal{B}
= \lambda\alpha\,\vec q + \lambda\beta\,\vec q^* + \lambda\xi\,N + \lambda\eta\,\bar{N},
$$

a shift of the four coordinates, verified on one hundred random pairs; distributivity in the second argument was verified at the same time and holds. The source's phrasing is a slip, and the displayed rule is the property it points to. All the listed inner-product properties are exact. The inner product is neither associative nor basis-independent, in contrast with the outer product; the author states this and explains that the alternative correspondence reverses the two roles.

**Diagonal.** The third is the product the author uses for spin. The corpus has no analogue of it.

**Crossing.** The fourth combines the outer product of the transverse parts with the inner product of the longitudinal parts,

$$
\mathcal{B}_1 \rightsquigarrow \mathcal{B}_2 = \vec q_{a,1} \odot \vec q_{a,2} + \mathcal{P}_2 \otimes \mathcal{P}_1.
\tag{9}
$$

Two points must be recorded about (9). First, the **order of the inner factor**: the printed coordinates of the crossing product, in the extraction, match (9) with the inner factor in the order $\mathcal{P}_2 \otimes \mathcal{P}_1$, and not with the order $\mathcal{P}_1 \otimes \mathcal{P}_2$ (residual zero against a residual of order one on the same pair). Either the paper's inner product is ordered oppositely to (8), or the term order in the author's sentence "$\vec q_{a,1} \odot \vec q_{a,2} + \mathcal{P}_1 \otimes \mathcal{P}_2$" is a slip; the extraction cannot settle it, because the inner product is not commutative. So the printed coordinate formula is the correct one, whatever the term order in the sentence.

### The Basis Product Table

The source collects the pairwise products of the four basis elements under the outer and the inner product in a table (its Table 1), and the table is the clearest single statement of how the two products differ.

| $\odot$ | $\vec q$ | $\vec q^*$ | $N$ | $\bar{N}$ |
|---|---|---|---|---|
| $\vec q$ | $0$ | $N$ | $0$ | $\vec q$ |
| $\vec q^*$ | $\bar{N}$ | $0$ | $\vec q^*$ | $0$ |
| $N$ | $\vec q$ | $0$ | $N$ | $0$ |
| $\bar{N}$ | $0$ | $\vec q^*$ | $0$ | $\bar{N}$ |

| $\otimes$ | $\vec q$ | $\vec q^*$ | $N$ | $\bar{N}$ |
|---|---|---|---|---|
| $\vec q$ | $\vec q$ | $0$ | $0$ | $\bar{N}$ |
| $\vec q^*$ | $0$ | $\vec q^*$ | $N$ | $0$ |
| $N$ | $N$ | $0$ | $0$ | $\vec q$ |
| $\bar{N}$ | $0$ | $\bar{N}$ | $\vec q^*$ | $0$ |

The structural interpretation is that **the two products exchange the two uniform nullquaternions with the two nullvectors**: $N$ and $\bar{N}$ square to themselves under the outer product ($N\odot N = N$, $\bar{N}\odot\bar{N} = \bar{N}$) and to zero under the inner one ($N\otimes N = \bar{N}\otimes\bar{N} = 0$), while $\vec q$ and $\vec q^*$ do the opposite ($\vec q\odot\vec q = 0$ but $\vec q\otimes\vec q = \vec q$). The source's own summary of the table has this second half inverted: it says that $\vec q$ and $\vec q^*$ are null for the inner product and square to themselves for the outer, which is the reverse of what its table and the formulas give, and it writes the outer-product symbol where the inner one is meant. The table is right and the sentence is not.

Two entries of the outer table look contradictory, and are not: it gives $N\odot\vec q = \vec q$ while $\vec q\odot N = 0$, and $\bar{N}\odot\vec q^* = \vec q^*$ while $N\odot\vec q^* = 0$. Both are correct, because the outer product is **not commutative** — its vector slot carries $i\,\vec q_{a,1}\times\vec q_{a,2}$ — so the two orders name different products. All thirty-two entries of the two tables were recomputed from (8) and all agree.

### The Appendix's Correspondences

The Appendix of the paper gives two correspondences of $\mathbb{B}$ with the two-by-two complex arrays, one attached to each of the two products it treats in array form; the first is correct, the second is not. The first is the one the whole paper uses: the four coordinates $\alpha,\beta,\xi,\eta$ are placed in the four slots of an array as $\xi,\alpha$ in the first row and $\beta,\eta$ in the second, and the **outer** product becomes the ordinary product of arrays. The second attaches to the **inner** product a product of arrays in which the second product of every entry is **subtracted** instead of added (the Appendix, equations (81)–(82)); its map is printed in v2 with $\xi,\alpha$ in the first row and $-\beta,-\eta$ in the second, and in v3 with $\alpha,-\eta$ in the first row and $\xi,-\beta$ in the second, the subtractive rule unchanged: entry $(i,j)$ of the product is $a_{i1}b_{1j} - a_{i2}b_{2j}$, addition replaced by subtraction in the second term. **Neither form makes the inner product into a product of arrays, and no correction of the map can.** The check was exhaustive: over all $4!$ orders in which the four coordinates may be placed in the four slots, all $2^4$ choices of entry signs, and the four pairing rules (add and subtract, with the two index orders) — $1536$ combinations, each required to give residual zero on twenty random pairs — **no** map realises the inner product. The reason is visible in the formulas: across the four coordinates the first terms of the inner product carry all four coordinates of the second factor, $\alpha_2, \beta_2, \xi_2, \eta_2$, whereas the first term of the rule can carry only two of them. The author's own revision is evidence that he knew the map was wrong — he changed it from v2 to v3 — but the corrected form fails the same test.

What *is* true, and is verified exactly, is that the **diagonal** product is an ordinary product of arrays: with the four coordinates placed as $\alpha,\beta$ in the first row and $\xi,\eta$ in the second, the product of the two arrays is the array of $\mathcal{B}_1 \times \mathcal{B}_2$ with residual zero; this is one of the realisations the same exhaustive search returns for the diagonal product, and the diagonal and the outer product are between them the only two of the four that have any. So the source's Appendix sentence — "if we replace outer multiplication by inner multiplication, then another isomorphism is established" — is true with the word **diagonal** in place of **inner**; the exchange-of-roles reading that the author draws from it (the inner product associative and basis-independent under the alternative correspondence) has no support, because the correspondence he exhibits is not an isomorphism at all.

### The Exchange Conjugations

Beyond the corpus's conjugations, the paper defines three more by **permuting the coordinates** of (4). In the order $(\alpha, \beta, \xi, \eta)$,

$$
\mathcal{B}^{\bigstar} : (\alpha, \beta, \xi, \eta) \mapsto (\beta, \alpha, \eta, \xi), \qquad
\mathcal{B}^{\bullet} : (\alpha, \beta, \xi, \eta) \mapsto (\xi, \eta, \alpha, \beta), \qquad
\mathcal{B}^{\bigstar\bigstar} : (\alpha, \beta, \xi, \eta) \mapsto (\eta, \xi, \beta, \alpha).
\tag{10}
$$

Each is a product of two disjoint transpositions — in cycle notation $(\alpha\beta)(\xi\eta)$, $(\alpha\xi)(\beta\eta)$ and $(\alpha\eta)(\beta\xi)$ — so none of them is a single transposition, and the third is the composition of the other two. Their structural properties were verified: each is self-inverse; $\bigstar \circ \bigstar\bigstar = \bigstar\bigstar \circ \bigstar = \mathcal{B}^{\bullet}$, so applying two different ones gives the third; and the three commute pairwise.

These are **not** algebra anti-automorphisms of the kind the corpus uses. The corpus's conjugations are $\mathbb{R}$-linear maps of $\mathbb{B}$ that interact with the product by reversing it; the paper's exchange conjugations are coordinate permutations of the isotropic basis, and they interact with the products of (8) by **changing the product type** rather than by reversing the order. This distinction is the substance of the author's equation

$$
\mathcal{B}_1 \otimes \mathcal{B}_2 = \mathcal{B}_2 \odot (\text{conjugate of } \mathcal{B}_1),
\tag{11}
$$

which the author calls the reversal of the multipliers with a change of product type. **Equation (11) does not hold.** The paper's three exchange conjugations are coordinate permutations by definition, so the claim is checked in full by permuting: over all twenty-four permutations, in both argument orders and in both directions, no permutation carries the inner product to the outer or the outer to the inner. Nor is the failure special to these three: in the whole family of four products, the only cross-type matches relate the **outer** and the **diagonal** ones, which is the pair of correspondences of the Appendix over again. The extraction of (11) is garbled — the conjugation symbols in it are lost — so it remains possible that the source's conjugations change the coefficients as well as permuting them; as printed, (11) is false. This is the first of the flagged items.

### Cyclic Conjugation

The operation on which the whole reformulation turns is the **cyclic conjugation**, a four-cycle of the coordinates:

$$
\overset{\curvearrowleft}{\mathcal{B}} : (\alpha, \beta, \xi, \eta) \mapsto (\beta, \xi, \eta, \alpha),
\tag{12}
$$

that is, $\overset{\curvearrowleft}{\mathcal{B}} = \beta\vec q + \xi\vec q^* + \eta N + \alpha\bar{N}$ for $\mathcal{B} = \alpha\vec q + \beta\vec q^* + \xi N + \eta\bar{N}$. The diagram of the paper is a rotation of the four coordinates around the basis, which stays in place. The properties were verified exactly: the fourth iterate is the identity, so the operation generates a cyclic group of order four on every biquaternion; the second iterate is the exchange conjugation of the second type,

$$
\overset{\curvearrowleft\curvearrowleft}{\mathcal{B}} = \mathcal{B}^{\bullet},
\tag{13}
$$

so the set $\{1, \overset{\curvearrowleft}{\phantom{x}}, \overset{\curvearrowleft\curvearrowleft}{\phantom{x}}, \overset{\curvearrowleft\curvearrowleft\curvearrowleft}{\phantom{x}}\}$ is exactly the four-element group $\{1, g, \mathcal{B}^{\bullet}, g^{-1}\}$, with $\mathcal{B}^{\bullet}$ the involution of (10). The author's decomposition of the cyclic conjugation into exchange conjugations is a restatement of the same cycle and is consistent with (13).

The second iterate being an involution is what makes the cyclic conjugation usable in a wave equation: it is not an involution itself, but it is a fourth root of unity on the coordinates, and the author reads it as the "cyclic development" of the wave function as against the "linear development" carried by the derivatives.

## The Cyclic Representation

### The Two Chiral Components and the Biquaternion Wave Function

The paper starts from the two-line chiral pair of the older literature, where the field is written as a pair of two-component objects and the equation as a pair of first-order lines. In this corpus the same pair is written with one line per value, both acting from the left,

$$
\tilde\nabla\tilde\Psi_R = m\tilde\Psi_L, \qquad \tilde\nabla^{\natural}\tilde\Psi_L = m\tilde\Psi_R,
$$

and the corpus fixes the gradient, the two values and their names (*Operator and Calculus Conventions*, §*The Gradient*, §*The Dynamics*). Rewritten in the isotropic derivatives (6), the pair is

$$
\begin{aligned}
2\bigl(\partial/\partial\xi\,u + \partial/\partial\beta\,v\bigr) &= -im\,u_2, &\qquad
2\bigl(\partial/\partial\eta\,v + \partial/\partial\alpha\,u\bigr) &= -im\,v_2, \\[2pt]
2\bigl(\partial/\partial\eta\,u_2 - \partial/\partial\beta\,v_2\bigr) &= -im\,u, &\qquad
2\bigl(\partial/\partial\xi\,v_2 - \partial/\partial\alpha\,u_2\bigr) &= -im\,v.
\end{aligned}
\tag{14}
$$

The factor $2$ on the left is the $\tfrac12$ of the derivatives (6): with it, (14) is the two-line pair itself, term by term; without it the system is half of it. The printed source omits the factor. The omission is not cosmetic: it also halves the derivative side of (20), and that is why the source's amplitude relations seem to disagree with its phase (see *Plane Waves and the Dispersion Relation*).

The **biquaternion wave function** is

$$
F = \vec qf_\alpha + \vec q^*f_\beta + Nf_\xi + \bar{N}f_\eta,
\tag{15}
$$

with complex scalar functions $f_\alpha, f_\beta, f_\xi, f_\eta$ of space-time, and the two chiral states are the two signed parts of (15):

$$
F^- = \vec qf_\alpha + Nf_\xi, \qquad F^+ = \vec q^*f_\beta + \bar{N}f_\eta, \qquad F = F^+ + F^-.
\tag{16}
$$

The correspondence with the two components of each line is

$$
u = f_\alpha, \qquad v = -f_\xi, \qquad u_2 = -f_\beta, \qquad v_2 = f_\eta,
\tag{17}
$$

so that the right-chiral state is the positive signed part and the left-chiral state the negative one: $F^- \sim \psi_L$ and $F^+ \sim \psi_R$. This is the paper's central identification, and it is correct, though not under the name the author gives it. The two signed parts are **the two values of the chirality** of the frame along $\vec u$: the value is a property of the element and of the frame, a product takes the value of its right factor, and a left multiplication keeps it (*Operator Chirality on the Biquaternion Algebra*, §*The Subscript on an Element*). Read there, the part $F^+$ carries $R$ and the part $F^-$ carries $L$, which is the assignment (16) and the reason it is the one kept. The corpus reaches the same two halves through the chirality operator of the frame along $\vec u$, named $\chi_u$, and through the two chiral halves of *Exercise: Chirality and the Weyl Spinors*; there is one split here and one carrier, the chirality operator. What the source calls "the sign of the component" is the value of that operator. Multiplication on the right by $\bar N$ and by $N$ selects the two values; these are the chiral halves, not a split of a carrier by left multiplication. The corpus's older left split plays no part here. The corpus's *Chiral Fermions in the Biquaternion Framework* is about a different question again — which chiral representations the framework admits — and must not be confused with the paper's "chiral algebra", which is a computational basis choice.

### The Gradients

The 4-gradient and its vector conjugate, written in the isotropic basis, are

$$
D = 2(\vec q\,\partial/\partial\beta + \vec q^*\,\partial/\partial\alpha + N\,\partial/\partial\xi + \bar{N}\,\partial/\partial\eta), \qquad
\bar{D} = 2(-\vec q\,\partial/\partial\beta - \vec q^*\,\partial/\partial\alpha + N\,\partial/\partial\eta + \bar{N}\,\partial/\partial\xi).
\tag{18}
$$

The author notes the inversion that looks like a slip and is not: the derivative $\partial/\partial\alpha$ stands on $\vec q^*$ and $\partial/\partial\beta$ on $\vec q$, which is the transpose of the coordinate pairing. The reason is that $D$ must reproduce $\partial/\partial t'$ and $\nabla$, and the $\alpha, \beta$ slots are exchanged by the vector conjugation. The factor $2$ is the price of the $\tfrac12$ normalisations in (2), and it is exactly the right one: multiplying out (18) in the paper's product gives an element whose scalar part is $\partial/\partial t'$ and whose vector part is $\nabla$, which is the author's spin gradient itself, not half of it, and $\bar{D}$ carries the same scalar part and $-\nabla$. Both lines were recomputed coefficient by coefficient. Note in particular that the $\bar N$ slot of $\bar D$ carries $\partial/\partial\xi$, not a second copy of $\partial/\partial\eta$: with $\partial/\partial\eta$ in both longitudinal slots the second line would carry $\partial/\partial t'-\partial/\partial z$ in both scalar slots and would not be the vector conjugate at all. The element $D$ acts on the field by left multiplication in the paper's product, $\psi\mapsto D\psi$; the corpus's own gradient is a different element, acting in the Hamilton product.

### The Single-String Representation

The result the paper is built to reach is the **cyclic representation**,

$$
\boxed{\;F^- \odot \bar{D} + D \otimes F^+ = im\,\overset{\curvearrowleft}{F}\;},
\tag{19}
$$

the Dirac equation for the biquaternion wave function $F$, written as one expression in which the two chiralities appear as the two signed parts $F^\pm$, the two gradient orderings appear as the two products $\odot$ and $\otimes$, and the mass appears on the right through the cyclic conjugate of $F$. Its component form, with the factor $2$ that the halved derivatives of (6) require, is

$$
\boxed{\;
\begin{aligned}
2\bigl(\partial/\partial\xi\,f_\alpha - \partial/\partial\beta\,f_\xi\bigr) &= im\,f_\beta, &\qquad
2\bigl(\partial/\partial\eta\,f_\xi - \partial/\partial\alpha\,f_\alpha\bigr) &= im\,f_\eta, \\[2pt]
2\bigl(\partial/\partial\eta\,f_\beta + \partial/\partial\beta\,f_\eta\bigr) &= im\,f_\alpha, &\qquad
2\bigl(\partial/\partial\xi\,f_\eta + \partial/\partial\alpha\,f_\beta\bigr) &= im\,f_\xi .
\end{aligned}\;}
\tag{20}
$$

**This system is the chiral pair (14), twice.** Substituting (17) into (20) turns each of the four equations into the corresponding one of (14), coefficient for coefficient, including the mass terms, once the second and third are multiplied through by $-1$ — an overall sign on a single equation carries no content. The two systems differ only in that sign and in the factor $2$ that both carry. Since (14) is the two-line pair itself, (20) is the Dirac equation in its two chiral components, which is the author's own claim. The factor is the one already noted after (14): it is the $\tfrac12$ of the derivatives (6), and the printed source omits it from (20) as it omits it from (14). The omission is not cosmetic. With the printed (20) the plane wave of (28) closes on $\epsilon^2-\vec k^2=4m^2$ instead of the mass shell (30); with the factor restored the two agree.

**One step is not reproduced.** The expansion of (19) into (20) cannot be checked in full from the printed symbols. Reading each derivative in $\bar{D}$ and $D$ as acting on the coefficient it multiplies — the pairing that the outer and inner products of (8) dictate — the $N$ and $\bar{N}$ components of (19) reproduce the second and third equations of (20) exactly, factor $2$ and mass included. The two transverse components do not: the $\vec q^*$ component comes out $2\partial f_\eta/\partial\xi$ short of the fourth equation, and exactly that term appears in the $\vec q$ component, which carries it in excess of the first. Whether the second product in (19) is the inner product of (8) or another of the four is not settled by the extraction. The component system (20) is verified on its own, against (14) and against the two-line pair, and it is the object used below; (19) is quoted as the author's single-string form.

The reader should also note what (19) is and is not: it is a **compactness** statement of the same kind the corpus makes for Maxwell and Dirac elsewhere, not a claim that one chirality is redundant. The expression contains both chiralities implicitly through the two products and the right-hand side; the two-chirality content is unpacked in the next subsection.

### The Separated Reading

The author unpacks (19) into two equations, one per chirality, by expanding the cyclic conjugate through the exchange conjugations:

$$
F^- \odot \bar{D} = im\,F^{+\bigstar}, \qquad
\bar{D} \otimes F^+ = im\,\breve{F}^- .
\tag{21}
$$

In the first, both sides are negative signed biquaternions, that is left-chiral states; in the second, both sides are positive, right-chiral states. The author reads this as the precise sense in which (19) "implicitly contains both equations", and as the answer to the objection that a single-string form must be hiding one of the two lines. Whether the pairing is right depends on the sign conventions of the three exchange conjugations, which are exactly the symbols that could not be read from the extraction (see the first flagged item); the *structure* — one equation per chirality, both sides the same sign — is what (21) asserts, and it is the split that the relations (7a)–(7b) give, read with the source's labels.

### The Two Dirac Equations, and Where the Cyclic Form Sits

The corpus writes the massive Dirac equation twice, and the two writings are not one equation. The source's cyclic representation is a third packaging of the **first** of them, and saying which is which fixes what the two products of (19) mean.

**The one-sided chiral pair.** The field is an element on which the algebra acts, and the equation is the pair

$$
\tilde\nabla\tilde\Psi_R=m\tilde\Psi_L,\qquad \tilde\nabla^{\natural}\tilde\Psi_L=m\tilde\Psi_R ,
$$

one line per value. Both gradients act by left multiplication, so the pair is one-sided; at $m=0$ the two lines are the two massless equations, and the mass couples them off the diagonal. **Chirality is the two lines.**

**The two-sided single equation.** Read on the algebra itself, the same physics is one equation with a left and a right side,

$$
\tilde\nabla^{\natural}F=m\,\chi\,\bar F ,
$$

with the derivative on the left and the mass on the right, through the chirality operator $\chi$ of the corpus's frame along $\vec e_z$ (*Operator Family Conventions*, §*The Slot Label, Which Is the Chirality*) and the coefficient conjugate $\bar F$. The mass term is antilinear; the chirality sits in the right multiplication, not in a second field.

**The cyclic form.** The source's (19) belongs to the first family. Its two products carry the two chiralities, exactly as the two lines of the pair do; its two gradient orderings, $\bar D$ on the right of $F^-$ and $D$ on the left of $F^+$, are the two one-sided actions; and the mass sits on the right-hand side through the **cyclic conjugation** of $F$, which is a four-cycle of the coordinates and not a right multiplication by an element. It is therefore neither the two-sided equation nor a new operator: it is the chiral pair compressed into one expression, with the cyclic conjugation in place of the second field.

| | One-sided chiral pair | Two-sided single equation | Cyclic form (19) |
|---|---|---|---|
| Field | one element, two values | $F\in\mathbb{B}$ | $F\in\mathbb{B}$ |
| Derivative | left, by the gradient and its conjugate | left, by the conjugate gradient | two products, $\bar D$ and $D$ |
| Mass | off-diagonal pairing of the two values | right, $m\chi\bar F$ | right, $im\overset{\curvearrowleft}{F}$ |
| Chirality | the two lines | the operator $\chi$ | the two signed parts, $F^\pm$ |

The distinction matters for reading the source's claims. The two-sided equation's chirality is the frame's operator and its mass is a right multiplication with a conjugation; in the cyclic form the chirality is the same operator, read on the two signed parts $F^\pm$, and the mass is the cyclic conjugation. The two agree on the solutions — (20) is the two-line pair — and their mass terms are not the same operator. The corpus's *The Dirac Equation in Biquaternionic Form* states the pair, and the two-sided equation is stated in *Biquaternion Representation of Spin One-Half and the Relativistic One-Electron Atom*; the cyclic form is a third writing of the first, differing from the two-sided equation in the mass and not in the chirality.

### The Boost and the Energy–Momentum Operators

The paper treats one special Lorentz transformation, the boost of velocity $V = \tanh 2\theta$ along the chosen longitudinal direction $\vec u$, with the wave function written in the chiral algebra. In the two chiral components the boost is

$$
u \mapsto \exp(-\theta) u, \qquad v \mapsto \exp(\theta) v, \qquad u_2 \mapsto \exp(\theta) u_2, \qquad v_2 \mapsto \exp(-\theta) v_2,
\tag{22}
$$

and in the algebra the author writes two **Lorentz operators**, the longitudinal and the transverse one,

$$
L = N \exp(\theta) + \bar{N} \exp(-\theta), \qquad \breve{L} = \vec q\, \exp(-\theta)\, \vec q^*\, \exp(\theta).
\tag{23}
$$

**The printed $\breve{L}$ collapses.** The scalars commute and $\vec q\,\vec q^* = N$ under the outer product, so

$$
\breve{L} = \exp(-\theta)\exp(\theta)\,\vec q\,\vec q^* = N .
\tag{24}
$$

The printed formula therefore names the longitudinal element, not a transverse operator, and read literally it cannot be the partner of $L$, which has a transverse part. The author's own two-product identity shows what the expression must be: the sum, not the product, of the two transverse terms, $\breve{L} = \exp(-\theta)\vec q + \exp(\theta)\vec q^*$, a transverse element carrying the same two exponentials. The author's rule for moving such an operator from one side of a product to the other is $\mathcal{B} \odot L = \breve{L} \otimes \mathcal{B}$ for every $\mathcal{B}$, and he writes the boost in two forms,

$$
F \mapsto F_2 = F \odot L = \breve{L} \otimes F,
\tag{25a}
$$

$$
F \mapsto F_2 = P^+ \odot L + \breve{L} \otimes P^- .
\tag{25b}
$$

Two remarks. First, **the right-multiplication by $L$ is a genuine boost, and it was verified**: with $L = N\exp(\theta) + \bar{N}\exp(-\theta)$ the components of $F \odot L$ are $f_\alpha \exp(-\theta)$, $f_\beta \exp(\theta)$, $f_\xi \exp(\theta)$, $f_\eta \exp(-\theta)$, which under the correspondence (17) is exactly (22), row by row. Second, **the two-product identities (25a) and (25b) are exact once $\breve{L}$ is read as that sum.** For every $\mathcal{B}$, $\mathcal{B}\odot L = \breve{L}\otimes\mathcal{B}$ holds with residual zero, and so does (25b), $P^+\odot L + \breve{L}\otimes P^- = \mathcal{B}\odot L$; with the printed $\breve{L}=N$ the same computation misses by a residual of order $1.5$, which is what makes the printed form look false. The identity is the reversal of the multipliers that (11) claims in general, and it holds here because $L$ is longitudinal: for $L = xN + y\bar{N}$ the matching element is $\breve{L} = x\vec q^* + y\vec q$, which is $\mathcal{B}^{\bigstar\bigstar}$ read on the two transverse slots. The general law (11) still fails, since it asks for a coordinate permutation and none realises it; for a longitudinal multiplier the matching element exists, and only there. So the boost stands twice over: as the one-sided $F \odot L$, and as the two-product (25a) with the corrected $\breve{L}$.

The energy-momentum biquaternion $K = k_\alpha\vec q + k_\beta\vec q^* + k_\xi N + k_\eta\bar{N}$ transforms **two-sidedly**, unlike the one-sided wave function,

$$
K \mapsto K_2 = L^* \odot K \odot L ,
\tag{26}
$$

and the 4-coordinate $Z$ transforms the same way. The first form of (26) was recomputed in the paper's product: it multiplies $k_\alpha,k_\beta$ by $\exp(-2\theta),\exp(2\theta)$ and leaves $k_\xi,k_\eta$ unchanged, while the reversed order $L\odot K\odot L^*$ exchanges the two factors and leaves the same pair untouched. Either way the longitudinal pair is not scaled, so the phase (27) is not preserved by (26) as printed, and the author's invariance argument does not go through his own product. The printed second equality of (26) introduces a symbol $T$ that the extraction never defines, presumably $\breve{L}$; it was not evaluated. The Lorentz invariant built from $K$ and $Z$ is the phase

$$
\Phi = \epsilon t' - \vec k\cdot\vec r = \tfrac12\bigl(-k_\beta\alpha - k_\alpha\beta + k_\eta\xi + k_\xi\eta\bigr),
\tag{27}
$$

whose right-hand side was verified to reduce to $\epsilon t' - k_x x - k_y y - k_z z$ identically in the isotropic coordinates of (5). (The extraction garbles the last term; the correct partner of $k_\eta\xi$ is $k_\xi\eta$.)

### Plane Waves and the Dispersion Relation

The paper's simplest solution of the cyclic representation is the plane wave

$$
F = A \exp(i\Phi) + B \exp(-i\Phi),
\tag{28}
$$

with $\Phi$ the invariant phase (27) and $A, B$ constant biquaternions, the positive-frequency and negative-frequency amplitudes. Substituting $F = A \exp(i\Phi)$ into the component system (20) makes it algebraic in the amplitudes; with $\Phi$ the phase (27), so that $\partial\Phi/\partial\alpha = -\tfrac12 k_\beta$ and $\partial\Phi/\partial\xi = \tfrac12 k_\eta$, the four equations read

$$
k_\eta a_\alpha + k_\alpha a_\xi = m a_\beta, \qquad k_\beta a_\alpha + k_\xi a_\xi = m a_\eta, \qquad
k_\xi a_\beta - k_\alpha a_\eta = m a_\alpha, \qquad -k_\beta a_\beta + k_\eta a_\eta = m a_\xi,
\tag{29}
$$

whose first two determine the longitudinal amplitudes $a_\xi, a_\eta$ from the free pair $a_\alpha, a_\beta$; the remaining two are then satisfied identically precisely when

$$
\boxed{\;\epsilon^2 - \vec k^2 = k_\xi k_\eta - k_\alpha k_\beta = m^2\;}.
\tag{30}
$$

The printed amplitude relations of the source are garbled in the extraction; (29) is their clean form, and it reproduces the one readable relation, $a_\xi = (m a_\beta - k_\eta a_\alpha)/k_\alpha$. The phase normalisation is now fixed. With the factor $2$ of (20) restored, the derivatives of (27) are $\partial\Phi/\partial\alpha = -\tfrac12 k_\beta$ and $\partial\Phi/\partial\xi = \tfrac12 k_\eta$, the factor $2$ cancels them, and (29) follows from (20) with the same $\Phi$ as in (27); the printed source omits the factor $2$ from (20) while keeping the $\tfrac12$ in (27), which is what makes its amplitude equations carry $2m$ and puts the wave on $\epsilon^2-\vec k^2=4m^2$. The two factors have to be restored together. At rest, $\vec k = 0$ and $k_\xi = k_\eta = m$, and the wave becomes $F = A_0 \exp(imt') + B_0 \exp(-imt')$ with constant coefficients, the author's starting point for the spin states below.

### The Spin Operators and the Spin States

The spin treatment is the paper's most concrete physical addition, and it rests on a **third correspondence**, this one for the diagonal product. The author places the four coefficients in the four slots of a two-by-two array in the order fixed by (17), and under that reading the diagonal product becomes the ordinary product of arrays and the operators below become the three Pauli arrays and the identity. No array is needed for the algebra: the operators are elements, and they act on the field by the diagonal product on the left,

$$
S_x = -(\vec q^* + N), \qquad S_y = i(\vec q^* - N), \qquad
S_z = \vec q - \bar{N}, \qquad S_t = \vec q + \bar{N},
\tag{31}
$$

with $S_t$ the unit of the diagonal product. Two bars are lost in the extraction, which prints $S_z = \vec q - N$ and $S_t = \vec q + N$, forms that do not answer to the third array and the identity; (31) is the bar-restored version, and with it the reading is the one the author intends. The eigenstates are

$$
\begin{aligned}
F_{x\uparrow} &= f_\alpha\vec q + f_\beta\vec q^* - f_\alpha N - f_\beta\bar{N}, &\quad
F_{x\downarrow} &= f_\alpha\vec q + f_\beta\vec q^* + f_\alpha N + f_\beta\bar{N}, \\
F_{y\uparrow} &= f_\alpha\vec q + f_\beta\vec q^* - i f_\alpha N - i f_\beta\bar{N}, &\quad
F_{y\downarrow} &= f_\alpha\vec q + f_\beta\vec q^* + i f_\alpha N + i f_\beta\bar{N}, \\
F_{z\uparrow} &= f_\alpha\vec q + f_\beta\vec q^*, &\quad
F_{z\downarrow} &= f_\xi N + f_\eta\bar{N},
\end{aligned}
\tag{32}
$$

with the eigenvalue relations

$$
S_j \times F_{j\uparrow} = F_{j\uparrow}, \qquad S_j \times F_{j\downarrow} = -F_{j\downarrow}
\tag{33}
$$

for $j = x, y, z$. All six relations of (33) were verified with the bar-restored operators (31), which is what fixes (31); the extraction's unbarred forms do not satisfy them.

The author then reads the **exchange conjugation of the second type** as the longitudinal spin flip: it exchanges the two $z$ states, $\tilde{F}_{z\uparrow} = F_{z\downarrow}$ and $\tilde{F}_{z\downarrow} = F_{z\uparrow}$, verified exactly. Since this exchange conjugation is the square of the cyclic conjugation (13), and the cyclic conjugation is what stands on the right-hand side of the Dirac equation, he concludes that **cyclic conjugation is the operation that gives the particle its spin**, and reads the four-cycle as a half-flip that passes through a spin-zero state. The cyclic conjugate of the rest state $a_1\vec q + a_1\vec q^*$ is

$$
\overset{\curvearrowleft}{F_{z\uparrow}} = a_1(\vec q + \bar{N}),
\tag{34}
$$

whose longitudinal spin vanishes, $\langle s_z\rangle = 0$: computed from its four components, the two contributions cancel, one from the transverse pair and one from the longitudinal element. (The extraction prints (34) with two components exchanged; the displayed form is the one the four-cycle (12) actually produces.) The author calls (34) the positive-frequency **zero state of spin**. The **physical interpretation** — spin created by the cyclic operation, halved by its square, and the two chiralities carried by the two products — is the author's; what is verified is the algebra of (31)–(34).

### Cyclic Conjugation in Cartesian Coordinates and the Hadamard Array

The author computes what the cyclic conjugation (12) becomes when the wave function is written in the Cartesian components $(f_x, f_y, f_z, f_t)$ rather than in the isotropic ones. Using the inverse of (5), the four-cycle becomes an array with entries in $\{\pm1, \pm i\}$, and the author's point is that this array is a **complex Hadamard array** $H_4$, with $H_4H_4^\dagger = 4I$ and all entries of modulus $1$; he then reads this as an informational aspect of the Dirac equation and connects it to Walsh functions, to noise-resistant coding, and to a genetic-code model he has published elsewhere.

The array is printed in the paper (equation (78)), and it satisfies both Hadamard properties: every entry has modulus $1$, and $H_4H_4^\dagger = 4I$, both recomputed here. It is, up to the overall factor $2$, exactly the array of the four-cycle (12) in the Cartesian components. Reading the four-cycle through (5), with $f_\alpha = f_x-if_y$, $f_\beta=f_x+if_y$, $f_\xi=f_t+f_z$, $f_\eta=f_t-f_z$ and the inverse $f_y=(f_\beta-f_\alpha)/(2i)$, the cycle sends $(f_x,f_y,f_z,f_t)$ to $\tfrac12 H_4\,(f_x,f_y,f_z,f_t)$, and the factor $\tfrac12$ is the one already present in (5), not a second normalisation. The variant with the **second row negated** is what the opposite sign of $f_y$, $(f_\alpha-f_\beta)/(2i)$, produces: it is the four-cycle read with a reversal of the $y$ orientation, and it is not the transformation of (12). Since negating a row preserves both Hadamard properties, both arrays are Hadamard; the printed $H_4$ is the one the four-cycle gives, and the author's mathematical claim — that the cyclic conjugation *is* a complex Hadamard transvection on the Cartesian components — holds. Whether the Hadamard structure "indicates the informational aspect of the Dirac equation" is a separate question, and it is the author's interpretation; the corpus records the Hadamard gate in the quantum-gates article in the standard real-valued setting, and nothing in the present article bears on that.

### The Lorentz Analogue, the Rotation Transformation and the Superluminal Variant

The remaining physical items are recorded as the author's claims. The boost, the plane-wave solutions and the spin operators are constructed in the sections above; the caveat here is that the machinery behind the following three was not verifiable from the extraction.

**The Lorentz analogue.** The boost is the construction of *The Boost and the Energy–Momentum Operators* above: the author writes it in the same two-product form as the cyclic representation and reads the structural similarity between the boost and the equation itself.

**The rotation transformation.** The author argues that because the cyclic conjugate sits on the right-hand side of (19), the left-hand side *is* the operation that creates it, and calls this the **rotation transformation**. Splitting the plane wave into its positive- and negative-frequency parts $Q_x = A\exp(i\Phi)$ and $Q_y = B\exp(-i\Phi)$, he forms the **subtractive components** $Q^\pm = Q_x^\pm - Q_y^\pm$ and writes the transformation as $F \mapsto Q^- \odot K + \bar{K} \otimes Q^+$ with the energy-momentum biquaternion $K$. The claim is that this transformation is the analogue of the Lorentz boost for the particle's **proper rotation**, that is for spin, and the author states explicitly that the translational partner of the transformation "remains open". In the corpus, the corresponding machinery is rotor conjugation, $A \mapsto \Lambda A \Lambda^{*}$ (*The Lorentz Transformation as a Biquaternionic Rotation*); the paper's rotation transformation is not rotor conjugation — it uses two different products and the subtractive components, not a conjugate pair — so it is a candidate for a genuinely different construction. It should be checked against the corpus's rotor action before any claim of novelty is repeated.

**The superluminal variant.** Flipping the sign of the two products, $F^- \odot \bar{D} - D \otimes F^+ = im\overset{\curvearrowleft}{F}$, gives the paper's **superluminal Dirac equation**, with the dispersion relation $\epsilon^2 - |\vec k|^2 = k_\xi k_\eta - k_\alpha k_\beta = -m^2$ in place of the subluminal one. The final algebraic step of this dispersion relation was verified — in the isotropic coordinates $k_\xi k_\eta - k_\alpha k_\beta = k_t^2 - k_x^2 - k_y^2 - k_z^2$ identically — so the superluminal branch follows from the sign as claimed. The **physical interpretation** of that branch is the author's, and the corpus's *Subluminal and Superluminal Electromagnetic Waves and the Lepton Mass Spectrum* records a different superluminal construction.

**The four representations.** The author states, without working them out, that the same treatment with the other three cyclic conjugations gives three more representations of the Dirac equation, all equivalent, and that the same holds with signed biquaternions in place of the signed split. He also states that the representation has a form for a superluminal particle and that it "clearly reveals the time asymmetry" of the Dirac equation. These are announced, not developed.

## What Is Verified and What Is Not

**The checks, item by item.** (i) **The product-reversal law (11).** It is false as printed. The paper's exchange conjugations are coordinate permutations, so the law is tested exhaustively by permuting: over all twenty-four permutations, in both argument orders and in both directions, none carries the inner product to the outer or the outer to the inner. In the whole family of four products the only cross-type matches are between the **outer** and the **diagonal** ones, which is the Appendix's pair of correspondences. The conjugation symbols are lost in the extraction, so a conjugation that changes the coefficients as well as permuting them cannot be excluded; as written, the law does not hold and must not be used. (ii) **The signed-part assignment.** The extracted equation (17) of the source assigns the coordinates to the signed parts in a way that is inconsistent with the source's own equations (38) and (48) and with the relations (7a)–(7b); the version used in this article is the one of (16), which is the internally consistent one. (iii) **The Appendix's second correspondence (81)–(82).** It is false, in both versions of the paper and for both of the maps printed — v2's, with $\xi,\alpha$ in the first row and $-\beta,-\eta$ in the second, and v3's, with $\alpha,-\eta$ in the first row and $\xi,-\beta$ in the second. No assignment of the four coordinates to the four slots, with or without signs, realises the inner product as a product of arrays with the printed subtractive rule, and the same holds for the additive rule; the reason is a counting one and is given in *The Appendix's Correspondences*. What the Appendix should say is that the **diagonal** product is the second ordinary product of arrays, and that statement is verified exactly. (iv) **The printed Hadamard array.** Read from both versions and verified: every entry has modulus $1$, $H_4H_4^\dagger = 4I$ holds, and the array is exactly twice the four-cycle of (12) in the Cartesian components, with the inverse $f_y=(f_\beta-f_\alpha)/(2i)$. The variant with a negated second row is the four-cycle read with the opposite sign of $f_y$, that is with a reversed $y$ orientation, and it is not the transformation of (12). The Hadamard claim itself is sound. (v) **The gradient identity (18).** Recomputed coefficient by coefficient in the paper's product: the scalar part of $D$ is $\partial/\partial t'$ and its vector part is $\nabla$, while $\bar D$ carries the same scalar part and $-\nabla$, so $D$ *is* the author's spin gradient and the source's statement that the spin gradient is half of $D$ does not hold for the printed $D$ — the two coincide, which is what the factor $2$ of (18) is for. The printed second line of (18) also repeats $\partial/\partial\eta$ on the $\bar N$ slot; the vector conjugate requires $\partial/\partial\xi$ there, and (18) is given in that corrected form. The factor of two is corroborated by the pure-vector case of (1), $\vec q_{a,1}\odot\vec q_{a,2}=\vec q_{a,1}\cdot\vec q_{a,2}+i\,\vec q_{a,1}\times\vec q_{a,2}$, which is the product the author reads his gradient in. (vi) **The rotation transformation and the superluminal variant.** Recorded as the author's constructions; the rotation transformation's claimed difference from the corpus's rotor conjugation was not established. (vii) **The boost's two-product identities (25a)–(25b).** The printed $\breve{L}=\vec q\exp(-\theta)\vec q^*\exp(\theta)$ collapses to $N$, because $\vec q\vec q^*=N$ and the scalars commute (24), and with $\breve L=N$ the identity of (25a) gives $F\odot L\neq N\otimes F$ by a residual of order $1.5$. The expression is a misprint for the sum $\exp(-\theta)\vec q+\exp(\theta)\vec q^*$: with the sum, (25a) and (25b) hold exactly for every $\mathcal{B}$, both with residual zero on random pairs, and the sum is the element the reversal requires for a longitudinal $L$, since $L=xN+y\bar N$ is matched by $\breve L=x\vec q^*+y\vec q$. So the identities are correct and the collapse is a typographical error, not a mathematical one. The boost itself, as the right multiplication $F\odot L$, is verified and unaffected. (viii) **The expansion of (19) into (20).** The component system (20) is verified against (14) and against the two-line pair, but the literal expansion of the single-string (19) is not: with each derivative acting on the coefficient it multiplies, the $N$ and $\bar N$ components reproduce the second and third equations exactly, while the $\vec q^*$ component is short of the fourth by $2\partial f_\eta/\partial\xi$ and the $\vec q$ component carries that term in excess of the first. The extraction does not fix which of the four products is the second one in (19). (ix) **The name of the two signed parts.** The source calls the split "the sign of the component". Recomputed, the two right components $\mathcal{B}\bar N$ and $\mathcal{B}N$ are the two values of the chirality of the frame along $\vec u$ — $R$ on $\mathcal{B}\bar N$ and $L$ on $\mathcal{B}N$ — that is $F^+$ carries $R$ and $F^-$ carries $L$, and the carrier is the chirality operator of that frame. No split by left multiplication is involved: a left split is a copy index and gives two copies of one left-handed carrier.

**What the source does not supply.** It does not work out the four alternative representations beyond their sign patterns, and it does not prove that they are equivalent to one another, only to the two-line pair. The construction of the Lorentz boost, the plane-wave solutions and the spin operators is present, and the earlier sections of this article give it; what the source does not supply is the second form of the boost as printed — its own identities show that the expression is a sum, and the printed product is a slip. The boost itself stands on the right multiplication, the spin operators on the diagonal product, and the single-string (19) stands as the author's form rather than as a checked expansion. The paper does not present the inner product's non-associativity as a limitation, although it says the outer product is the associative one and the inner product is not, and it raises the division-algebra programme only in a closing paragraph. And the identification of the Hadamard structure with a genetic code is an external programme of the author's, cited in his bibliography, not a result of this article.

**The identifier.** The number printed on both versions is `2502.0126`, which is malformed — arXiv identifiers have a five-digit suffix. Queried on 27 September 2026, `arXiv:2502.0126` is *A Bayesian decision-theoretic approach to sparse estimation* by Li, Tokdar and Xu, an unrelated statistics paper, and a search of arXiv by the present title and by the author's name returns nothing on this work (only the author's *Nonlinear Maxwell equations*, arXiv:2403.00836, which the paper cites as reference [4]). So the paper appears not to be on arXiv under this number, and the identifier must not be propagated: cite the file, with its version, and treat the printed number as a typographical error of the author's.

**The two versions.** The corpus holds v2 (March 2025, *Cyclic representation of the Dirac equation*) and v3 (February 2026, *Chiral algebra of Dirac equation*), and they were compared word by word. The differences are seven and all small: the title; one clause of the abstract; the replacement of the Russian cross-reference placeholders ("source not found") by references to Appendix 1 and 2; the display of the Hadamard array, written for the Cartesian point coordinates in v2 and for the wave-function components in v3 (the same $H_4$ in both); the deletion of a stray clause; a change of e-mail address; and the map of the Appendix's second correspondence, changed from the v2 placement to the v3 placement. The last of these is the only mathematical change, and since both forms fail the same test it is a correction that did not repair the claim.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The generators carry no frame label: $\gamma_\mu$ is one set of matrices, and the frame is named on the coordinate and on the metric, $g[\mathbb{B}]$ or $g[\mathbb{M}_-]$.

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})=M_4(\mathbb{C})$, not a different algebra. The cells are named here and nowhere else, with $L_a\psi=a\psi$ and $R_b\psi=\psi b$:

$$
\gamma_0=iL_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}},\qquad \gamma_1=iL_{\vec e_x}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},
$$

The same in the axis-free display:

$$
\gamma_0=iL_{e_t}^{\mathrm{axf}}R_{\vec e_x}^{\mathrm{axf}},\qquad \gamma_1=iL_{\vec e_x}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},
$$

$$
\gamma_2=iL_{\vec e_y}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\qquad \gamma_3=iL_{\vec e_z}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}},\qquad \gamma_5=\chi=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}.
$$

In the axis-free display:

$$
\gamma_2=iL_{\vec e_y}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\qquad \gamma_3=iL_{\vec e_z}^{\mathrm{axf}}R_{\vec e_y}^{\mathrm{axf}},\qquad \gamma_5=\chi=-iL_{e_t}^{\mathrm{axf}}R_{\vec e_z}^{\mathrm{axf}}.
$$

The four frame cells satisfy the cell relation of $\varepsilon=(1,-1,-1,-1)$, and their squares are $\pm I_4$:

$$
\{\gamma_\mu,\gamma_\nu\}=2\varepsilon_\mu\delta_{\mu\nu}I_4,\qquad (\gamma_0)^2=I_4,\qquad (\gamma_k)^2=-I_4\quad(k=1,2,3),
\qquad \varepsilon=(1,-1,-1,-1),$$

The squares spend the central unit once, $i^2=-1$: the plain cells $L_{e_t}^{\mathrm{pau}}R_{\vec e_x}^{\mathrm{pau}}$ and $L_{\vec e_k}^{\mathrm{pau}}R_{\vec e_y}^{\mathrm{pau}}$ square to $I_4$, and the factor $i$ turns the second family into $-I_4$. The chirality is the cell $\chi=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}$, with $\chi^2=I_4$ and $\{\gamma_\mu,\chi\}=0$; $L_{e_t}^{\mathrm{pau}}$ is the identity, so the cell is a pure right multiplication, written in full to keep the frame uniform. It is the cell that the two-sided equation of *The Two Dirac Equations, and Where the Cyclic Form Sits* multiplies on the right. The body's longitudinal boost operator $L=N\exp(\theta)+\bar N\exp(-\theta)$ is a different symbol from the left cell $L_a$; the subscript distinguishes them, and no formula in the body mixes the two.

A single product $L_aR_b$ is a pure tensor; the products form the seven-dimensional cone $\operatorname{rank}c(M)\le1$, and a general element is a sum of at most four, with $\ell(M)=\operatorname{rank}c(M)$.

The central grading is a different object from the chirality cell. $\chi_{\mathrm{ad}}=i\tilde\Xi_{\mathrm{ad}}$ — the difference of the two central idempotents of the complexified algebra, so $\chi_{\mathrm{ad}}^2=e_t$ — is represented by $\gamma_5$ on the Dirac module, while $\chi=-iL_{e_t}^{\mathrm{pau}}R_{\vec e_z}^{\mathrm{pau}}$ is the module cell. The abstract sign is central and squares to the identity of the algebra; its representative is a cell and squares to the identity of the module.

The dictionary is complex-linear; over $\mathbb{R}$ the products span $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and the cells span $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the corpus. The two are carried into one another by $L_{e_\mu}^{\mathrm{axf}}=C_{\Pi}L_{e_\mu}^{\mathrm{pau}}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a cell named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

The source builds a purpose-made **chiral algebra** of biquaternions and writes the Dirac equation in it as a single expression. The algebra starts from the light-cone basis: the four nullquaternions $\vec q$, $\vec q^*$, $N$, $\bar{N}$ of (2), with $\vec q\vec q^* = N$, $\vec q^*\vec q = \bar{N}$ and $N\bar{N} = 0$, in which every biquaternion has the unique light-cone decomposition (4) and splits into a transverse part in the null plane and a longitudinal part along the chosen real direction $\vec u$. That decomposition is the light-cone writing of the corpus's split into the two values of the subscript. On it the paper defines three things new to the corpus. First, **four general products** — outer, inner, diagonal and crossing — the outer one being the product $\vec q_{a,1}\cdot\vec q_{a,2} + i\,\vec q_{a,1}\times\vec q_{a,2}$, which is not the corpus's Hamilton product and differs from it in the sign of the dot and the cross; the inner one having the remarkable properties $\vec q\otimes\vec q = \vec q$, $N\otimes\bar{N} = \vec q$, $\lambda_1\otimes\lambda_2 = \lambda_1\lambda_2\vec A$ and a genuine failure of compatibility with scalar multiplication; the crossing one preserving the two classes $\{\vec q,\bar{N}\}$ and $\{\vec q^*,N\}$ and swapping them from left to right, which are **not** the source's two signed parts — that distinction is one of the article's findings, and it is set out with the relations (7a)–(7b). Second, **three exchange conjugations**, the coordinate permutations (10), which are not the corpus's conjugations but a change of product type. Third, **cyclic conjugation**, the four-cycle (12), whose fourth iterate is the identity and whose square is the exchange conjugation of the second type. The reformulation then reads: the biquaternion wave function (15) has the two chiral halves as its two signed parts, $F^+ \sim \psi_R$ and $F^- \sim \psi_L$; the Dirac equation is the single expression $F^- \odot \bar{D} + D \otimes F^+ = im\overset{\curvearrowleft}{F}$; its component form (20) is the chiral pair (14), that is the two-line pair itself, under the correspondence (17), verified row by row; and the cyclic conjugation, read in Cartesian components, is, up to the factor $2$ of (5), the complex Hadamard array $H_4$. The single-string (19) is a third packaging of the one-sided chiral pair, not the two-sided equation: its two products carry the two chiralities, and its mass acts by the cyclic conjugation, not by the right multiplication $m\chi\bar F$. Around this the paper adds the machinery that turns the algebra into physics: the array picture, in which the outer product is the ordinary product of arrays and the diagonal product is the ordinary product under the author's third correspondence — the Appendix's claimed second correspondence, for the **inner** product, is false, and it is the diagonal that takes that place — a Lorentz boost acting by right-multiplication, whose components reproduce the boost (22), plane-wave solutions closing exactly on the mass shell $\epsilon^2 - \vec k^2 = m^2$, and the spin operators, which are the three Pauli arrays under the diagonal correspondence, with the exchange conjugation as the longitudinal spin flip. The apparatus is sound and largely verified; the equivalence is exact; the physical interpretations — the rotation transformation as the creator of the particle's proper rotation, the identification of the cyclic operation with spin, the superluminal branch, and the informational reading of the Hadamard array — are the author's. Three structural claims do not survive recomputation: the product-reversal law (11), which no coordinate permutation realises; the Appendix's second correspondence (81)–(82), false in both printed forms; and the literal expansion of the single-string (19) into the component system (20), where the $\vec q$ and $\vec q^*$ components do not match under the printed products. The printed $\breve{L}$ is a fourth item of a different kind: a misprint, repaired by restoring a sum, and the identities it was accused of breaking are exact once it is repaired.

Two corrections of computation run through the article. The first is the factor $2$ that the halved derivatives (6) require in (14) and (20): without it the plane wave closes on $\epsilon^2-\vec k^2=4m^2$ instead of the mass shell. The second is the sign of the vector term in $\mathcal{B}\bar{\mathcal{B}}$, which is the paper's product and not the corpus's Hamilton norm — it is what makes the nullquaternions null. A third correction is a correction of name: the two signed parts are the two values of the chirality of the light-cone direction, not a split by left multiplication, and the carrier of the split is the chirality operator. What survives intact is the machinery: the isotropic basis, the four products and their two array correspondences, the crossing relations, the cyclic conjugation and its Hadamard reading, the one-sided boost, and the spin operators.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | Biquaternion algebra; the corpus's $e_t, \vec e_x, \vec e_y, \vec e_z$ basis |
| $i$ | Central scalar imaginary unit, $i^2 = -1$ |
| $\mathcal{B} = (s, \vec q_a)$ | Scalar-vector (Silberstein) form: complex scalar $s$, complex vector $\vec q_a$ |
| $\mathcal{B}^*, \bar{\mathcal{B}}, \bar{\mathcal{B}}^*$ | Complex, vector (quaternion), and double (Hermitian) conjugates |
| $\lvert\mathcal{B}\rvert^2 = \mathcal{B}\bar{\mathcal{B}} = s^2 - \vec q_a^2$ | Square modulus (complex) |
| $\vec A, \vec B, \vec u$ | Right-handed real triad, $\vec A\times\vec B = \vec u$, unit lengths |
| $\Pi$ | The null (transverse) plane spanned by $\vec A$ and $\vec B$ |
| $\vec q = \tfrac12(\vec A+i\vec B),\ \vec q^*$ | Nullvectors; $\vec q^2 = 0$ |
| $N = \tfrac12(1, \vec u),\ \bar{N}$ | Uniform nullquaternions; $N^2 = N$, $N\bar{N} = 0$ |
| $\alpha, \beta, \xi, \eta$ | Isotropic coordinates: $\alpha = x-iy$, $\beta = x+iy$, $\xi = t'+z$, $\eta = t'-z$ |
| $\mathcal{B}^+, \mathcal{B}^-$ | Signed (positive, negative) biquaternions; the two chiral halves, $\mathcal{B}\bar N$ and $\mathcal{B}N$ |
| $\mathcal{P}^+, \mathcal{P}^-$ | The two signed elements of the crossing product |
| $\odot, \otimes, \times, \rightsquigarrow$ | Outer, inner, diagonal and crossing products |
| $\mathcal{B}^{\bigstar}, \mathcal{B}^{\bullet}, \mathcal{B}^{\bigstar\bigstar}$ | The three exchange conjugations (coordinate permutations) |
| $\overset{\curvearrowleft}{\phantom{x}}$ | Cyclic conjugation (the four-cycle) |
| $F = \vec qf_\alpha + \vec q^*f_\beta + Nf_\xi + \bar{N}f_\eta$ | Biquaternion wave function |
| $F^+ , F^-$ | Positive and negative signed parts; $\psi_R$ and $\psi_L$ |
| $\breve{F}^-$ | Partner of $F^-$ in the separated reading (21); not otherwise used |
| $\chi$, $\chi_u$ | The chirality operator of the corpus's frame along $\vec e_z$ and along $\vec u$; the two halves are its two values |
| $u, v, u_2, v_2$ | The two components of each chiral line; $u = f_\alpha$, $v = -f_\xi$, $u_2 = -f_\beta$, $v_2 = f_\eta$ |
| $\boldsymbol{\sigma}$ | Pauli matrices, $\boldsymbol{\sigma} = (\sigma_x, \sigma_y, \sigma_z)$ |
| $M$, $\psi$ | The two-by-two arrays the author attaches to $\mathcal{B}$ and to $F$ in the Appendix and in the spin section |
| $k_\alpha, k_\beta, k_\xi, k_\eta, \epsilon$ | Energy-momentum in isotropic coordinates; $k_\xi k_\eta - k_\alpha k_\beta = \epsilon^2 - \vec k^2$ |
| $\Phi = \epsilon t' - \vec k\cdot\vec r$ | Lorentz-invariant phase of the plane wave |
| $A, B$ | Positive- and negative-frequency amplitudes of the plane wave |
| $L = N\exp(\theta) + \bar{N}\exp(-\theta)$ | Longitudinal boost operator |
| $\breve{L}$ | The source's second Lorentz operator; printed so that it collapses to $N$ (24); the sum $\exp(-\theta)\vec q+\exp(\theta)\vec q^*$ is meant |
| $S_x, S_y, S_z, S_t$ | Spin operators; the three Pauli arrays and the identity under the diagonal correspondence |
| $F_{j\uparrow}, F_{j\downarrow}$ | Spin eigenstates along $j = x, y, z$ |
| $D = (\partial/\partial t', \nabla),\ \bar{D}$ | 4-gradient and its vector conjugate, in the paper's real-time convention |
| $H_4$ | Complex Hadamard array of the cyclic conjugation in Cartesian components; the cycle itself is $\tfrac12H_4$ |
| $K$ | Energy-momentum biquaternion of the rotation transformation |
| $Q^\pm$ | Subtractive components in the rotation transformation |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.
- Sergey Y. Kotkovskiy, *Chiral algebra of Dirac equation*, version v3 (February 2026); earlier version *Cyclic representation of the Dirac equation*, v2 (March 2025). The source of this article: the isotropic basis, the four multiplication types, the exchange and cyclic conjugations, the cyclic representation, the Hadamard expression, the two array correspondences, the Lorentz boost, the plane waves, the spin operators and the rotation transformation. The paper prints the identifier `2502.0126`, which is malformed and belongs on arXiv to an unrelated statistics paper; no record of this work was found under that number, its title, or its author's name, so the two versions held in the corpus are the source of record.
- S. Ya. Kotkovsky, "Nullvector algebra", *Hypercomplex Numbers in Geometry and Physics* **2**(23) (2014), for the author's earlier nullvector algebra, the origin of the isotropic basis and the terminology of nullquaternions used throughout.
- V. V. Kravchenko, *Applied Quaternionic Analysis* (Heldermann, 2003), and the corpus's [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html) and [The Time-Harmonic Maxwell Operator and the Quaternionic Cauchy Integral](the-time-harmonic-maxwell-operator-and-the-quaternionic-cauchy-integral.html), for the standard biquaternionic Dirac machinery against which the paper's purpose-made algebra should be read.
- The corpus's [Conventions in the Biquaternion Universe](algebra-and-element-conventions.html) (the Hamilton product and the corpus's outer product), [Peirce Decompositions of the Biquaternion Algebra](../articles_maths/the-peirce-decomposition-of-the-biquaternion-algebra.html) (the split by a left multiplication, against which the paper's right-handed split should be read), *The Null Cone* and [N-Regularity and N-Degeneracy in the Biquaternion Algebra](../articles_maths/n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html) (the vanishing-norm structure that the nullquaternions are), [The Spinor Module in Biquaternionic Form and Its Lorentz Action](the-spinor-module-in-biquaternionic-form-and-its-lorentz-action.html) (the two halves as the two values of the subscript), [Exercise: Chirality and the Weyl Spinors](exercise-chirality-and-the-weyl-spinors.html) and [Conventions of the Matrix Models](matrix-representations-conventions.html) (the chirality halves, for comparison with the signed parts used here), [Quantum Gates and Circuits in Biquaternionic Form](quantum-gates-and-circuits-in-biquaternionic-form.html) (the Hadamard gate in the ordinary setting), and [The Lorentz Transformation as a Biquaternionic Rotation](the-lorentz-transformation-as-a-biquaternionic-rotation.html) (rotor conjugation, the corpus's analogue of the paper's boost and the comparison object for its rotation transformation).
- P. A. M. Dirac, "The Quantum Theory of the Electron", *Proceedings of the Royal Society A* **117** (1928) 610–624, and L. Silberstein, "Quaternionic form of relativity", *Philosophical Magazine* **23** (1912) 790–809, for the Dirac equation and the scalar-vector biquaternion form the paper uses.
- K. J. Horadam, *Hadamard Matrices and Their Applications* (Princeton, 2007), for the complex Hadamard matrices of which the derived $H_4$ is an example, and for the standard theory behind the paper's informational interpretation.

