# __The Meaning of N Regularity and Degeneracy__

## Introduction

Two words, one number, and two sectors behind the second of them.

The biquaternion algebra carries four algebraic norms, and exactly one of them answers a question about invertibility. It is the quaternionic norm,

$$
N=\langle\tilde Q\rangle_{\natural}=Q_t^{2}+B^{2},
\qquad
B^{2}=(\vec Q,\vec Q)=Q_x^{2}+Q_y^{2}+Q_z^{2},
$$

and the vocabulary is fixed by its value: an element is **$N$-regular** when $N\neq0$ and **$N$-degenerate** when $N=0$. The pair is used everywhere in the corpus. It is the domain of the polar word, the domain of the logarithm, one of the two conditions that cut the four sectors, and the level set that carries the mass. What it *means* is stated in one line by *Norm and Pairing Conventions*, §*The Four Algebraic Norms and the Unitary Convention*: of the four algebraic norms, only $N$ decides invertibility.

This article works that line out and states the answer in full. The answer has four parts, and the fourth is the one usually left implicit.

**$N$ is the determinant.** So $N$-regular means invertible, and an invertible element is a bijection of the algebra onto itself: nothing is annihilated, the map can be undone, and it is a transformation. $N$-degenerate means singular: the element has a non-zero kernel, it annihilates something, and it cannot be undone. The pair is not a classification of elements into two convenient boxes. It is the algebraic form of the question *is anything lost?*

**Degeneracy has two strata, not one.** The cone is the origin, the pure elements with vanishing square, and the non-pure elements, which are non-zero multiples of idempotents. The pure part is a complex cone of real dimension four; the non-pure part is of real dimension six. The split is by the scalar part $Q_t$, and on the cone the two questions *is $Q_t$ zero?* and *is the spectrum degenerate?* coincide.

**Degeneracy of the norm has two sectors, and they are the cone cut by the spectrum.** On the cone the element is either a scalar multiple of a non-trivial idempotent, with eigenvalues $\{c,0\}$, or a nilpotent of index two, with the single eigenvalue $0$. These are $\Sigma_{01}$ and $\Sigma_{00}$, the two sectors of degeneracy. Their difference is not a detail: the first keeps a live direction beside its dead one, the second does not, and the two carry different kernels and different images.

**Degeneracy of the norm is not degeneracy of the spectrum.** $\Sigma_{01}$ is $N$-degenerate and spectrally regular. $\Sigma_{10}$ is $N$-regular and spectrally degenerate. The two conditions are independent off the cone and coincide on it, and that coincidence is why the two sectors of degeneracy can be named by the spectrum at all.

The article also states the two polar decompositions, because the corpus says "the polar decomposition" for two different things, and the degenerate case looks like a failure until the two are separated. One is defined on every element and survives on the cone with a Hermitian factor of rank one. The other is the four-factor word, and it is a parametrisation of the group of units.

The article is a reading article. It cites the mathematics, proves the small statements that are stated nowhere else, and says at each step whether the physical word in play — mass, reversibility, gauge — is supplied by the algebra or imported from the material sector.

The conventions are those of the read list. The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with $e_t=1$ and $\vec e_\mu^{2}=-e_t$; $i$ is the central scalar imaginary; $\natural$ is the quaternionic conjugation and $*$ the Hermitian conjugation; $\mathbb{B}^{\times}=\{\tilde Q:N\neq0\}$ is the group of units; $\tilde\Pi_\pm=\tfrac12(e_t\pm\vec Z)$ with $\vec Z^{2}=e_t$ are the primitive idempotents and $S_\pm=\mathbb{B}\tilde\Pi_\pm$ the minimal left ideals; $V=\ker\operatorname{tr}$ is the traceless part; and $\Sigma_{ij}$ is the sector with $N\neq0$ if $i=1$ and $B^{2}\neq0$ if $j=1$.

## The Results It Uses

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| The norm, its multiplicativity, the two cases, the group of units and the two strata of the cone | [N-Regularity and N-Degeneracy in the Biquaternion Algebra](../articles_maths/n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html) |
| The regular half: the unit group, its dimension, its topology and its two spectral cells | [The N-Regular Sector](../articles_maths/the-n-regular-sector.html) |
| The degenerate half: the cone, the three strata, the link $S^{2}\times S^{3}$, the rank-one model and the spinor reading | [The N-Degenerate Sector](../articles_maths/the-n-degenerate-sector.html) |
| The word on the units: the modulus, the unit factor and the four factors | [The Polar Decomposition of an N-Regular Biquaternion](../articles_maths/the-polar-decomposition-of-an-n-regular-biquaternion.html) |
| The two factors on the cone: the rank-one Hermitian factor, the partial isometry and the closed forms | [The Polar Decomposition of an N-Degenerate Biquaternion](../articles_maths/the-polar-decomposition-of-an-n-degenerate-biquaternion.html) |
| The four sectors, the characteristic polynomial, the independence of the two cones and the chain of invariants | [Relations between the N Norm and Spectral Regularity and Degeneracy](../articles_maths/relations-between-the-n-norm-and-spectral-regularity-and-degeneracy.html) |
| The four sectors one at a time | [The N-Regular, Spectrally Regular Sector](../articles_maths/the-n-regular-spectrally-regular-sector.html); [The N-Regular, Spectrally Degenerate Sector](../articles_maths/the-n-regular-spectrally-degenerate-sector.html); [The N-Degenerate, Spectrally Regular Sector](../articles_maths/the-n-degenerate-spectrally-regular-sector.html); [The N-Degenerate, Spectrally Degenerate Sector](../articles_maths/the-n-degenerate-spectrally-degenerate-sector.html) |
| The matrix model, with $\langle\tilde Q\rangle_{\natural}=\det\mathsf M_2(\tilde Q)$ and the units as the invertible matrices | [$M_2(\mathbb C)$ Pauli Representation](../articles_maths/m2c-pauli-representation.html) |
| The rank of $L_{\tilde Q}$, the images and the kernels of the four sectors | [Introduction to N and Spectrally Regular and Degenerate Operators](../articles_maths/introduction-to-n-and-spectrally-regular-and-degenerate-operators.html) |
| The idempotents, their isotropy and the minimal left ideals | [Square Roots of One and the Idempotents of the General Quaternionic Algebra](../articles_maths/square-roots-of-one-and-the-idempotents-of-the-general-quaternionic-algebra.html); [The Peirce Decomposition of the Biquaternion Algebra](../articles_maths/the-peirce-decomposition-of-the-biquaternion-algebra.html) |
| The exponential and the logarithm, with the units as the image and the cone as the complement | [Biquaternion Elementary Functions](../articles_maths/biquaternion-elementary-functions.html) |
| The two-factor decomposition on every element, and its uniqueness | [The Polar Decomposition of a Biquaternion](../articles_maths/the-polar-decomposition-of-a-biquaternion.html) |
| The three carriers, their dimensions and their spins | [Angular Momentum and Spin in the Biquaternion Algebra](../articles_maths/angular-momentum-and-spin-in-the-biquaternion-algebra.html); [Spin and the Three Elementary Carriers](spin-and-the-three-elementary-carriers.html) |
| The cone as the light cone of the material sector and the level set as the mass shell | [The Zero-Divisor Cone and the Massless Spectrum](the-zero-divisor-cone-and-the-massless-spectrum.html); [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html) |
| The massless limit as a boundary value of the word | [The Massless Limit as a Boundary Value of the Polar Word](the-massless-limit-as-a-boundary-value-of-the-polar-word.html) |
| The Hamilton modulus, the complex angle and the cross term in the mass of a sum | [The Hamilton Pairing: Mass as Modulus and the Complex Angle](the-hamilton-pairing-mass-as-modulus-and-the-complex-angle.html) |

The table is the contract: every statement below is either a theorem of one of these rows or a corollary drawn from two of them, and each section names the row it restates.

## The One Norm That Decides Invertibility

### The Norm and Its Identity

**Definition.** The **quaternionic norm** of $\tilde Q=Q_te_t+\vec Q$ is the complex scalar

$$
\langle\tilde Q\rangle_{\natural}=\sum_{\mu}Q_\mu^{2}=Q_t^{2}+(\vec Q,\vec Q).
$$

**The identity.** For a vector part $\vec Q^{2}=-(\vec Q,\vec Q)$, so $(Q_t-\vec Q)(Q_t+\vec Q)=Q_t^{2}-\vec Q^{2}$, that is

$$
\tilde Q\tilde Q^{\natural}=\tilde Q^{\natural}\tilde Q=\langle\tilde Q\rangle_{\natural}\,e_t .
$$

The value is a complex scalar and not a length, and its vanishing set is a cone and not a sphere. Three consequences follow at once, and they are the whole of the algebra used below.

**Multiplicativity.** The conjugation $\natural$ is an anti-automorphism, so

$$
\langle\tilde Q_2\tilde Q\rangle_{\natural}=\langle\tilde Q_2\rangle_{\natural}\langle\tilde Q\rangle_{\natural}.
$$

**Inversion.** Dividing the identity by the norm,

$$
\tilde Q^{-1}=\frac{\tilde Q^{\natural}}{\langle\tilde Q\rangle_{\natural}},
$$

which is defined exactly when $N\neq0$. The inverse is the conjugate over the norm: a vanishing norm is a division by zero and nothing subtler.

**The matrix reading.** Under $\mathsf M_2$ the norm is the determinant,

$$
\langle\tilde Q\rangle_{\natural}=\det\mathsf M_2(\tilde Q),
$$

so $N$-regular is the invertible matrix and $N$-degenerate is the singular one. Multiplicativity is the multiplicativity of the determinant, and the inverse above is the adjugate over the determinant.

### The Criterion, in Five Equivalent Forms

The pair is operational because five properties that look different are the same property.

**Criterion.** For $\tilde Q\in\mathbb{B}$ the following are equivalent:

(i) $\langle\tilde Q\rangle_{\natural}\neq0$;

(ii) $\tilde Q$ is invertible in the plain product;

(iii) $\det\mathsf M_2(\tilde Q)\neq0$;

(iv) the left translation $L_{\tilde Q}(\tilde X)=\tilde Q\tilde X$ is bijective;

(v) the right translation $R_{\tilde Q}(\tilde X)=\tilde X\tilde Q$ is bijective.

For $\tilde Q\neq0$ they are also equivalent to:

(vi) $\tilde Q$ is not a zero divisor.

*Proof.* (i)$\Rightarrow$(ii) is the inverse above. (ii)$\Rightarrow$(iii) is the determinant. (ii)$\Rightarrow$(iv),(v): multiplication by a unit is a bijection, of inverse multiplication by $\tilde Q^{-1}$. (iv)$\Rightarrow$(i): if $N=0$ and $\tilde Q\neq0$, the left translation kills the non-zero element $\tilde Q^{\natural}$; if $\tilde Q=0$, it is the zero map. The right translation is the same argument. (i)$\Rightarrow$(vi): a unit cannot annihilate a non-zero element. (vi)$\Rightarrow$(i): if $N=0$ and $\tilde Q\neq0$, then $\tilde Q\tilde Q^{\natural}=0$ with $\tilde Q^{\natural}\neq0$, so $\tilde Q$ is a left zero divisor.

The dichotomy is one line, and it is worth boxing, because every later section quotes it.

$$
\boxed{\;
N\neq0\iff\tilde Q\in\mathbb{B}^{\times}\iff L_{\tilde Q}\ \text{is a bijection},
\qquad
N=0\iff L_{\tilde Q}\ \text{has a non-zero kernel}\;}
$$

The two halves are exact negations of each other, and the middle term is what makes the pair operational: invertibility of the element and injectivity of the multiplication are one condition and not two.

**The one point where the words differ from ring theory.** In ring theory a regular element is a non-zero-divisor, and the origin qualifies, so the ring-regular set is $\mathbb{B}^{\times}\cup\{0\}$. The corpus's **$N$-regular** is the norm's word: the origin is $N$-degenerate. The two readings differ at one point, the apex, and this article follows the norm.

### What the Norm Does to Products

Multiplicativity has one consequence that deserves its own name, because it is the algebraic form of irreversibility.

**Proposition (the cone is absorbing).** If $N(\tilde Q)=0$ then $N(\tilde Q\tilde X)=N(\tilde X\tilde Q)=0$ for every $\tilde X$.

*Proof.* $N(\tilde Q\tilde X)=N(\tilde Q)N(\tilde X)=0$, and the same on the other side.

Read plainly: once an element is on the cone, every product it enters is on the cone. Composing a singular element with anything, on either side, cannot restore what it destroyed. In the language of ideals the cone is a two-sided ideal of the multiplicative semigroup, $\mathbb{B}\mathcal N\subseteq\mathcal N$ and $\mathcal N\mathbb{B}\subseteq\mathcal N$.

The property is not shared by the additive structure. The cone is not closed under addition, and the shortest witness is

$$
(\vec e_x+i\vec e_y)+(\vec e_x-i\vec e_y)=2\vec e_x,
\qquad
N(\vec e_x+i\vec e_y)=0,\quad N(2\vec e_x)=4 .
$$

So the cone is a cone over a curved base and not a subspace, and it is not an additive ideal. The algebra is simple and has none; the cone is the multiplicative shadow of the determinant.

## The Two Cases

### The Regular Case: the Group of Units

**Definition.** The **$N$-regular sector** is $\mathbb{B}^{\times}=\{\tilde Q:N\neq0\}$, and it is the group of units of the plain product.

**Theorem.** $\mathbb{B}^{\times}$ is a group. The product of two units is a unit by multiplicativity, the unit is $e_t$ with $N=1$, and the inverse is $\tilde Q^{\natural}/N$.

Four established properties of the sector are used in the readings below.

**It is the invertible half of the matrix algebra.** Under $\mathsf M_2$,

$$
\mathbb{B}^{\times}\cong GL_2(\mathbb{C}),
$$

with $\langle\tilde Q\rangle_{\natural}=\det\mathsf M_2(\tilde Q)$. The norm is the determinant sequence $\mathbb{B}^{\times}\to\mathbb{C}^{\times}$, and its fibre over one is

$$
\{\tilde Q:N=1\}\cong SL_2(\mathbb{C}).
$$

**It is open, dense and connected.** The complement is the zero set of one complex polynomial, so it is closed and of empty interior; the sector is its complement, hence open and dense. It has real dimension eight, the dimension of the algebra, and the removal of a closed subset of real codimension two leaves it connected.

**Its boundary is the cone.** $\partial\mathbb{B}^{\times}=\mathcal N$, and the cone has empty interior.

**Its topology is the topology of the phase and of the compact part.** The sector retracts onto the $*$-unitary group $\mathrm U(2)$, and

$$
\mathrm U(2)\cong\frac{S^{1}\times S^{3}}{\{\pm e_t\}},
\qquad
\pi_1(\mathbb{B}^{\times})\cong\mathbb{Z},
$$

the infinite cyclic group being carried by the central phase. The universal cover is $\mathbb{R}\times S^{3}$. The Euclidean sphere is not a group, and it is not the compact part of the sector.

**Its two spectral halves.** Inside the sector the spectrum cuts again,

$$
\mathbb{B}^{\times}=\Sigma_{11}\uplus\Sigma_{10},
\qquad
\Sigma_{11}=\{N\neq0,\ B^{2}\neq0\},
\qquad
\Sigma_{10}=\{N\neq0,\ B^{2}=0\}.
$$

On $\Sigma_{11}$ the eigenvalues $\lambda_\pm=Q_t\pm iB$ are distinct and non-zero, and the element is diagonalisable. On $\Sigma_{10}$ they coincide at $Q_t\neq0$, and the element is either the scalar $Q_te_t$ or a Jordan element $Q_te_t+\vec\Upsilon$ with $\vec\Upsilon\neq0$ and $\vec\Upsilon^{2}=0$. The split is not multiplicative: the product of two elements of $\Sigma_{10}$ can lie in $\Sigma_{11}$, and the product of two elements of $\Sigma_{11}$ can lie in $\Sigma_{10}$. It is a stratification of the sector, not a second partition of the algebra.

### The Degenerate Case: the Cone

**Definition.** The **$N$-degenerate sector** is the null cone

$$
\mathcal N=\{\tilde Q:\langle\tilde Q\rangle_{\natural}=0\},
$$

and the **zero-divisor set** is its punctured part $\mathcal Z=\mathcal N\setminus\{0\}$.

Three established properties are used below.

**It is a complex hypersurface of real codimension two.** One complex equation in four complex coefficients, of real dimension six, smooth off the origin, closed and of empty interior. On the punctured cone the gradient of the norm does not vanish, so the cone is a complex three-fold there and the origin is its only singular point.

**It is not a topological manifold at the apex.** Its link is

$$
L=\mathcal N\cap S^{7}_{E}\cong S^{2}\times S^{3},
\qquad
\pi_2(L)\cong\mathbb{Z},
$$

while a manifold point would have the link $S^{5}$, whose second homotopy group vanishes. The apex is a genuine singularity.

**It is contractible and projectively a quadric surface.** The straight-line homotopy $\tilde Q\mapsto(1-s)\tilde Q$ contracts the cone to the apex, and the quotient by the complex scalars is

$$
\mathbb{P}(\mathcal N)\cong\mathbb{P}^{1}\times\mathbb{P}^{1},
$$

whose real form is $S^{2}\times S^{2}$. The punctured cone is a $\mathbb{C}^{\times}$-bundle over it.

The two cases together are a partition, and it is worth writing as one display because the corpus quotes it in that form:

$$
\mathbb{B}=\underbrace{\{\tilde Q:N\neq0\}}_{\text{group of units}}\;\uplus\;\underbrace{\{\tilde Q:N=0\}}_{\text{null cone}}=\mathbb{B}^{\times}\uplus\mathcal N,
\qquad
\mathcal N=\{0\}\uplus\mathcal Z .
$$

### The Two Sides Compared

| | $\mathbb{B}^{\times}$, $N$-regular | $\mathcal N$, $N$-degenerate |
| --- | --- | --- |
| condition | $N\neq0$ | $N=0$ |
| real dimension | $8$ | $6$ |
| topology | open and dense, connected, $\simeq S^{1}\times S^{3}$ | closed cone, contractible, singular at the apex, link $S^{2}\times S^{3}$ |
| multiplication | group | semigroup with absorbing $0$ and no identity |
| inverse | two-sided, $\tilde Q^{\natural}/N$ | none |
| matrix model | invertible, rank $2$ | rank at most $1$ |
| spectrum | $\lambda_\pm\neq0$ | $0$ is an eigenvalue |
| rank of $L_{\tilde Q}$ | $4$ | $2$, or $0$ at the apex |
| polar factors | $\tilde Q_H$ positive definite, $\tilde Q_0$ $*$-unitary | $\tilde Q_H$ of rank one, $\tilde Q_0$ a partial isometry |
| boundary | $\partial\mathbb{B}^{\times}=\mathcal N$ | the cone is the boundary and has empty interior |

## The Two Strata of the Cone

### The Split by the Scalar Part

The cone is not homogeneous. Its own equation, $Q_t^{2}+\vec Q^{2}=0$, ties the scalar part to the vector part, and the scalar part alone cuts the cone into two pieces and an apex.

**Definition.** The **apex**, the **pure stratum** and the **non-pure stratum** are

$$
\{0\},\qquad
\mathcal N_{\mathrm p}=\{\tilde Q\in\mathcal N:Q_t=0,\ \tilde Q\neq0\},\qquad
\mathcal N_{\mathrm{np}}=\{\tilde Q\in\mathcal N:Q_t\neq0\}.
$$

**Theorem (the trichotomy).** $\mathcal N=\{0\}\uplus\mathcal N_{\mathrm p}\uplus\mathcal N_{\mathrm{np}}$, and for a non-zero point of the cone the following are equivalent:

(i) $Q_t=0$;

(ii) $\tilde Q^{2}=0$;

(iii) $\tilde Q$ lies in the pure stratum;

(iv) $B^{2}=0$, which is the spectral condition.

The negations are equivalent too: $Q_t\neq0$, $\tilde Q^{2}\neq0$, $B^{2}\neq0$, and the element lies in the non-pure stratum.

*Proof.* On the cone $Q_t^{2}=-B^{2}$, so $Q_t^{2}-B^{2}=2Q_t^{2}$ and

$$
\tilde Q^{2}=(Q_t^{2}-B^{2})e_t+2Q_t\vec Q=2Q_t\tilde Q,
$$

which vanishes exactly when $Q_t=0$; and $Q_t=0$ is $B^{2}=0$ on the cone.

That display is the whole of the section. On the cone every element satisfies $\tilde Q^{2}=2Q_t\tilde Q$, and the two strata are the two ways that identity can be read: at $Q_t\neq0$ it is an idempotent equation after rescaling, and at $Q_t=0$ it is a nilpotent equation.

### The Pure Stratum: the Nilpotents

**Theorem.** Every element of $\mathcal N_{\mathrm p}$ is a nilpotent of index two,

$$
\tilde Q=\vec Q\neq0,
\qquad
\vec Q^{2}=0,
\qquad
\tilde Q^{2}=0,
$$

and the stratum is a complex cone of complex dimension two and real dimension four, cut out in the three vector coefficients by the single quadratic equation

$$
Q_x^{2}+Q_y^{2}+Q_z^{2}=0 .
$$

In the matrix model it is the set of non-zero nilpotent matrices of rank one.

**Real coordinates.** Write $\vec Q=\vec\rho+i\vec\rho'$ with $\vec\rho,\vec\rho'\in\mathbb{R}^{3}$. Then

$$
\vec Q^{2}=\bigl(\lvert\vec\rho'\rvert^{2}-\lvert\vec\rho\rvert^{2}\bigr)e_t-2i(\vec\rho\cdot\vec\rho')\,e_t,
$$

so the pure stratum is the set of bivectors with

$$
\vec\rho\cdot\vec\rho'=0,
\qquad
\lvert\vec\rho\rvert=\lvert\vec\rho'\rvert .
$$

Equivalently it is the set of elements

$$
\tilde Q=r\bigl(\vec u+i\vec u_\perp\bigr),
\qquad
r>0,
$$

with $\vec u$ a real unit vector and $\vec u_\perp$ a real unit vector perpendicular to it. One radius, one direction and one perpendicular direction: $1+2+1=4$ real dimensions.

Read the content. A pure degenerate element is a **null bivector**: an electric part and a magnetic part of equal magnitude and perpendicular to one another. It has no scalar part, so it has no trace, and its square vanishes, so it annihilates its own output.

### The Non-Pure Stratum: the Idempotent Multiples

**Theorem.** Every element of $\mathcal N_{\mathrm{np}}$ is uniquely

$$
\tilde Q=c\,\tilde\Pi,
\qquad
c=2Q_t\neq0,
\qquad
\tilde\Pi=\frac{\tilde Q}{2Q_t},
\qquad
\tilde\Pi^{2}=\tilde\Pi,
\qquad
\tilde\Pi\neq0,e_t,
$$

and the idempotent has scalar part $1/2$. The stratum is open and dense in the punctured cone, of complex dimension three and real dimension six.

*Proof.* $\tilde\Pi^{2}=\tilde Q^{2}/(4Q_t^{2})=2Q_t\tilde Q/(4Q_t^{2})=\tilde\Pi$. The idempotent is neither $0$ nor $e_t$: the first gives $\tilde Q=0$, the second gives $\tilde Q=2Q_te_t$, of norm $4Q_t^{2}\neq0$. The map $\tilde Q\mapsto\tilde\Pi$ is continuous, and $Q_t\neq0$ is open in the cone with the pure stratum as its complement.

**The geometry of the idempotents.** The non-trivial idempotents form a complex surface of real dimension four, and they are exactly the rank-one idempotents. The map $\mathcal N_{\mathrm{np}}\to\{\tilde\Pi\}$ is a principal $\mathbb{C}^{\times}$-bundle, the fibre over $\tilde\Pi$ being the punctured complex line $\mathbb{C}^{\times}\tilde\Pi$. A non-trivial idempotent is a pair of a line and a transversal hyperplane, so the surface is $\mathbb{P}^{1}\times\mathbb{P}^{1}$ minus the diagonal.

**The Peirce factorisation.** Both strata sit in one Peirce framework. For a non-pure zero divisor, with $\tilde\Pi$ its idempotent, the mixed Peirce corners contain elements

$$
u\in\tilde\Pi\mathbb{B}(e_t-\tilde\Pi),
\qquad
w\in(e_t-\tilde\Pi)\mathbb{B}\tilde\Pi,
\qquad
uw=\tilde\Pi,
\qquad
u^{2}=w^{2}=0,
$$

so every non-pure zero divisor is a scalar multiple of a product of two nilpotents,

$$
\tilde Q=2Q_t\,uw .
$$

**What separates the strata.** Conjugation by the units acts on the punctured cone with the pure stratum as one orbit, and with each set $c\{\tilde\Pi\}$ of idempotent multiples as one orbit. The invariant that separates them is the scalar part $Q_t$: a non-zero nilpotent of index two has one Jordan form, and the idempotent multiples are the diagonalisable ones, scaled by $c$.

So the cone carries two shapes and not one. That is the answer to the question of what degeneracy looks like, and the reason the flat statement "a degenerate element is singular" is true and useless: it says nothing about which of the two shapes the element has.

## The Two Sectors of Degeneracy

### The Characteristic Polynomial Reads Both Conditions

The two strata are one cut. The two sectors of degeneracy are another, and to see why there are exactly two of them the right object is the characteristic polynomial.

**Definition.** For $\tilde Q=Q_te_t+\vec Q$,

$$
p_{\tilde Q}(X)=X^{2}-2Q_tX+\langle\tilde Q\rangle_{\natural}=X^{2}-2Q_tX+Q_t^{2}+B^{2},
\qquad
\operatorname{disc}p_{\tilde Q}=-4B^{2}.
$$

**Theorem (the spectrum reads both conditions).** With $\lambda_\pm=Q_t\pm iB$, where $B$ is a fixed square root of $B^{2}$,

$$
p_{\tilde Q}(X)=(X-\lambda_+)(X-\lambda_-),
\qquad
N=\lambda_+\lambda_-,
\qquad
2Q_t=\lambda_++\lambda_-,
\qquad
(\lambda_+-\lambda_-)^{2}=-4B^{2}.
$$

*Proof.* The product and the sum of the roots. The square of the difference is $(2iB)^{2}=-4B^{2}$.

The display is a dictionary, and it is exact:

| item | quaternionic norm | spectral condition |
| --- | --- | --- |
| quantity | $N=Q_t^{2}+B^{2}$ | $B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2}$ |
| role in $p_{\tilde Q}$ | the constant term | the discriminant, up to $-4$ |
| spectral reading | the product $\lambda_+\lambda_-$ | the difference $\lambda_+-\lambda_-=2iB$ |
| zero locus | $\mathcal N$ | $\mathcal S=\{B^{2}=0\}$ |
| vanishing means | one eigenvalue is $0$ | the two eigenvalues coincide |
| multiplicative | yes | no |
| decides | invertibility | separation of the spectrum |

So the two degenerations of an element are the two ways a monic quadratic over $\mathbb{C}$ can degenerate: **a zero root** is $N=0$, and **a double root** is $B^{2}=0$. The cone is the vanishing of the constant term; the spectral cone is the vanishing of the discriminant.

On the cone the constant term vanishes, so one root is zero, and there are only two ways for the other root to behave. Either it is non-zero — two distinct roots, one of them zero — or it vanishes as well — a double root at zero. Those are the two sectors of degeneracy.

### $\Sigma_{01}$: Two Distinct Roots, One of Them Zero

$$
\Sigma_{01}=\{N=0,\ B^{2}\neq0\}=\{\tilde Q=c\,\tilde\Pi:\ c\in\mathbb{C}^{\times},\ \tilde\Pi^{2}=\tilde\Pi,\ \tilde\Pi\neq0,e_t\}.
$$

This is the non-pure stratum, and the identification is the trichotomy read backwards: $B^{2}\neq0$ is $Q_t\neq0$, which is the idempotent case.

**In components.** With $\vec Z=\vec Q/Q_t$ the normal form is one line, and the conditions unfold to one equation each. A member of the sector is

$$
\tilde Q=Q_t\,(e_t+\vec Z)=2Q_t\,\tilde\Pi,
\qquad
\tilde\Pi=\tfrac12(e_t+\vec Z),
\qquad
(\vec Z,\vec Z)=-1,
$$

and the last equation written out is the component form of $N=0$:

$$
Q_x^{2}+Q_y^{2}+Q_z^{2}=-Q_t^{2},
\qquad
Q_t\neq0 .
$$

So a member is a scalar part together with a vector part whose Euclidean square is minus the square of the scalar part. The second display is one complex equation in the three complex coefficients of $\vec Z$, so it cuts the six real parameters of $\vec Z$ to four, and that surface is the one counted in §*The Non-Pure Stratum*.

**A member, checked.** Take $\vec Z=i\vec e_x$, so that $Q_t=1$, $c=2$ and $\tilde Q=e_t+i\vec e_x$. Then $N=1+i^{2}=0$ and $Q_t\neq0$, so the element is in the sector, and

$$
\tilde Q^{2}=e_t+2i\vec e_x+i^{2}\vec e_x^{2}=e_t+2i\vec e_x+e_t=2\tilde Q=2Q_t\tilde Q,
$$

which is the sector identity at $Q_t=1$. Every element of the sector is conjugate to $c\,\tilde\Pi(\vec e_x)$ for its own $c$, because every non-trivial idempotent is conjugate to $\tilde\Pi(\vec e_x)$.

**The spectrum.** The eigenvalues are $c=2Q_t\neq0$ and $0$, distinct, and the spectral decomposition exists,

$$
\tilde Q=c\,\tilde\Pi+0\cdot(e_t-\tilde\Pi),
$$

with the orthogonal idempotents $\tilde\Pi$ and $e_t-\tilde\Pi$. The minimal polynomial is $p_{\tilde Q}(X)=X(X-c)$, squarefree. The unordered pair $\{c,0\}$ is the whole similarity invariant, because conjugation preserves the trace $c$ and the determinant $0$.

**What the sector is.** A live mode of weight $c$ and a dead mode of weight $0$. The dead mode is a genuine spectral direction: it is present in the basis and absent from the element. This is the sector in which the element is a **scaled projection**: it selects a plane, scales it, and kills a transversal plane.

**Why it propagates and $\Sigma_{00}$ does not.** Because the two roots are distinct, the image and the kernel are complementary,

$$
\mathbb{B}=\ker L_{\tilde Q}\oplus\operatorname{im}L_{\tilde Q},
$$

so a live plane survives beside the annihilated one. That complementarity is the operator form of $\tilde Q^{2}=c\tilde Q$, and it is the reason this sector behaves like a ray with a direction.

**What it does to a test element.** Left multiplication by $\tilde Q$ is $c$ times left multiplication by $\tilde\Pi$, and $\tilde\Pi+(e_t-\tilde\Pi)=e_t$, so every $\tilde X$ splits as

$$
\tilde X=\tilde\Pi\tilde X+(e_t-\tilde\Pi)\tilde X ,
$$

one part scaled by $c$ and one part killed. The kept part runs over the image $\tilde\Pi\mathbb{B}$, a complex plane, and the killed part runs over the kernel. The two planes meet only at $0$ and fill the algebra.

**The physical interpretation.** A non-trivial idempotent is a ray. The Hermitian members of the family are the pure states, $\tilde\Pi(\pm\vec u)=\tfrac12(e_t\pm i\vec u)$ with $\vec u$ a real unit vector, and they are exactly the members with $\vec Z=\pm i\vec u$. A null four-momentum of the material sector is one of them with an imaginary weight, $\tilde P_\Phi=2i(E/c)\tilde\Pi(-\vec u)$, so the massless momentum sits in this sector. The sector keeps a direction and a weight and has no frame: that is what makes it the sector of a ray and not of a transformation. The weight is a complex number and the idempotent need not be Hermitian, so the reading of the whole sector is **scaled projection**, and *pure state* is the reading of the Hermitian subfamily. Boundary: the sector fixes the nullity and the plane that survives, and it fixes neither $c$ nor the polarisation inside that plane.

### $\Sigma_{00}$: a Double Root at Zero

$$
\Sigma_{00}=\{N=0,\ B^{2}=0\}=\{\tilde Q:\tilde Q^{2}=0\}=\mathcal N_{\mathrm p}\cup\{0\}.
$$

This is the pure stratum with the apex adjoined, and again the identification is the trichotomy: $B^{2}=0$ is $Q_t=0$, which is the nilpotent case.

**In components.** The scalar part is zero, so the sector is a condition on the vector alone:

$$
\tilde Q=\vec Q,
\qquad
(\vec Q,\vec Q)=0
\quad\Longleftrightarrow\quad
Q_t=0,\quad Q_x^{2}+Q_y^{2}+Q_z^{2}=0 .
$$

In the real coordinates $\vec Q=\vec\rho+i\vec\rho'$ of §*The Pure Stratum* the condition is $\lvert\vec\rho\rvert=\lvert\vec\rho'\rvert$ and $\vec\rho\cdot\vec\rho'=0$: an electric part and a magnetic part of equal magnitude and perpendicular, which is the null bivector found there. The parametrisation given there, $\tilde Q=r(\vec u+i\vec u_\perp)$ with $\vec u$ and $\vec u_\perp$ real orthonormal and $r>0$, is exactly this sector without the apex.

**A member, checked.** Take $\tilde Q=\vec e_x+i\vec e_y$. Then $Q_t=0$ and $Q_x^{2}+Q_y^{2}=1+i^{2}=0$, and

$$
\tilde Q^{2}=-e_t+i\left(\vec e_x\vec e_y+\vec e_y\vec e_x\right)+i^{2}\vec e_y^{2}=-e_t+0+e_t=0 ,
$$

the two cross terms cancelling because the quaternion units anticommute. The null field strength is a complex multiple of the same element. Write $\tilde F=i\sqrt{\epsilon}\,\vec E-\sqrt{\mu}\,\vec H$ and put $\vec V=\sqrt{\epsilon}\,\vec E$ and $\vec W=\sqrt{\mu}\,\vec H$. Then $(\vec F,\vec F)=-\lvert\vec V\rvert^{2}+\lvert\vec W\rvert^{2}-2i\,\vec V\cdot\vec W$, so the field is a nilpotent exactly when the two real vectors are perpendicular with equal lengths. Axes along them then give $\tilde F=iV\vec e_x-V\vec e_y=iV(\vec e_x+i\vec e_y)$ with $V=\lvert\vec V\rvert=\lvert\vec W\rvert$, and a complex multiple of a nilpotent is a nilpotent.

**The spectrum.** The only eigenvalue is $0$, the minimal polynomial is $X$ at the origin and $X^{2}$ off it, and off the origin there is no spectral decomposition at all: no non-trivial idempotent commutes with a non-zero nilpotent.

**What the sector is.** A two-step ladder with no live weight. The element annihilates what it produces, and the difference from the apex is only that the ladder has a rung.

**What it does to a test element.** $\tilde Q^{2}=0$ is the statement that the output of the map is annihilated by the map, so $\operatorname{im}L_{\tilde Q}\subseteq\ker L_{\tilde Q}$. The rank is two and the kernel is a plane, so the two subspaces coincide: the element maps the algebra onto the plane it kills, and nothing is kept at any scale.

**Why the two sectors cannot be confused.** In $\Sigma_{01}$ the rank of left multiplication is two and the image is complementary to the kernel. In $\Sigma_{00}$, off the origin, the rank is two and the kernel is a plane, so the image coincides with the kernel. The ranks agree and the geometry does not: one sector is a projection onto a plane along a plane, the other is a shift into a dead plane.

**The physical interpretation.** The element is pure, and a nilpotent is neither Hermitian nor anti-Hermitian, so it lies in neither $\mathbb{B}_\Phi$ nor $\mathbb{B}_\Psi$. A physical four-momentum has a non-zero scalar part, so no momentum is a nilpotent, and the massless momentum of the previous subsection is not one. Two physical objects do sit here: the null field strength, which is the radiative field with both invariants zero, and the lightlike displacement, which is the algebraic form of a direction that erases itself in one composition. The sector has a plane and no weight. Boundary: the nullity is fixed and the polarisation is not, so the cone does not separate the two helicities of a null field.

### Why There Are Exactly Two

**Theorem (the cone meets two sectors).** The cone is the disjoint union

$$
\mathcal N=\Sigma_{01}\uplus\Sigma_{00},
$$

and the other two sectors are disjoint from it, $\Sigma_{11}\cap\mathcal N=\Sigma_{10}\cap\mathcal N=\varnothing$.

*Proof.* On the cone $Q_t^{2}=-B^{2}$, hence $Q_t=0$ exactly when $B^{2}=0$, and $Q_t\neq0$ exactly when $B^{2}\neq0$.

**Corollary (the algebraic and spectral splits coincide on the cone).** On the cone the split by the scalar part and the split by the square of the vector part are the same split. Off the cone they are independent: $e_t$ has $Q_t=1$ and $B^{2}=0$, while $\vec e_x$ has $Q_t=0$ and $B^{2}=1$.

This corollary is why the two sectors of degeneracy can be named by the spectrum without ambiguity: on the cone, and only there, the two questions have the same answer. The corpus's warning that the two conditions are independent is a statement about the algebra, and the cone is exactly the set on which the warning does not bite.

| sector | condition | normal form | spectrum | minimal polynomial | real dimension | what survives |
| --- | --- | --- | --- | --- | --- | --- |
| $\Sigma_{01}$ | $N=0$, $B^{2}\neq0$ | $c\tilde\Pi$, $\tilde\Pi$ non-trivial | $\{c,0\}$, $c\neq0$ | $X(X-c)$, squarefree | $6$ | a direction and a scale |
| $\Sigma_{00}$ | $N=0$, $B^{2}=0$ | $0$, or $\tilde\nu$ with $\tilde\nu^{2}=0$ | $\{0\}$ | $X$ or $X^{2}$ | $4$ | a null bivector, and no scale |

The table is the answer to the question *what are the two cases of degeneracy*. They are not two degrees of badness. They are a projection and a nilpotent, and every difference between them in this article follows from that one.

## What the Degenerate Element Carries

### The Kernel and the Rank

The operational content of the dichotomy is a statement about what the element kills, and it is computed in *Introduction to N and Spectrally Regular and Degenerate Operators*, §*The Three Operators*.

| object | $\ker L_{\tilde Q}$ | $\operatorname{im}L_{\tilde Q}$ |
| --- | --- | --- |
| $\Sigma_{11}$, $\Sigma_{10}$ | $0$ | $\mathbb{B}$ |
| $\Sigma_{01}$, $\tilde Q=\kappa\tilde\Pi$ | a complex plane | the totally isotropic plane $\tilde Q\mathbb{B}$ |
| $\Sigma_{00}$, $\tilde Q=\tilde\nu$ nilpotent | a complex plane | $\mathbb{C}\tilde\nu\oplus\mathbb{C}\tilde\Pi_{+}=\ker L_{\tilde\nu}$ |
| $\tilde Q=0$ | $\mathbb{B}$ | $0$ |

One number summarises it:

$$
\operatorname{rank}L_{\tilde Q}=
\begin{cases}
4, & N\neq0,\
2, & N=0,\ \tilde Q\neq0,\
0, & \tilde Q=0.
\end{cases}
$$

The jumps are by two and by two. The regular element loses nothing, the degenerate one loses exactly half of its domain, and the zero element loses all of it. Because the algebra is four-dimensional over $\mathbb{C}$, half is a plane and not a line.

**The kernel is never odd-dimensional.** There is no element of $\mathbb{B}$ whose left multiplication annihilates exactly a line, and none that annihilates a three-dimensional subspace. The loss is quantised: nothing, or half, or everything. That is the sharpest quantitative statement of the article, and it is what makes the degenerate case rich: a plane has a direction, a transversal and a complement, while a line would have none.

**The two sectors differ by where the image sits.** In $\Sigma_{01}$ the image is complementary to the kernel; in $\Sigma_{00}$ it lies inside it. The operator form of the difference is $\tilde Q^{2}=c\tilde Q$ against $\tilde\nu^{2}=0$.

### The Product of a Spinor and a Co-Spinor

The cone has a second description, and it is the one that carries the physical reading. Fix the standard primitive idempotent $\tilde\Pi_{+}=\tfrac12(e_t+\vec e_z)$. The **spinor space** is the minimal left ideal

$$
S_{+}=\mathbb{B}\tilde\Pi_{+},
$$

of complex dimension two, and the **co-spinor space** is the row space

$$
S_{+}^{\vee}=\tilde\Pi_{+}\mathbb{B},
$$

of the same dimension. Take a spinor $\psi\in S_{+}$ and a co-spinor $\chi\in S_{+}^{\vee}$ and multiply:

$$
\mathcal N=\{\psi\chi:\psi\in S_{+},\ \chi\in S_{+}^{\vee}\}.
$$

**Why the product is on the cone.** In the Peirce coordinates of the pair $\tilde\Pi_\pm$ the product has

$$
Q_{++}=\psi_{1}\chi_{1},\quad
Q_{+-}=\psi_{1}\chi_{2},\quad
Q_{-+}=\psi_{2}\chi_{1},\quad
Q_{--}=\psi_{2}\chi_{2},
$$

which are the four entries of the outer product of the coefficient column with the coefficient row. Its determinant vanishes, and the determinant of the Peirce coordinates is the norm. So every product of a spinor with a co-spinor is a zero divisor, and conversely: a non-zero element of the cone has the rank-one matrix model $uv^{\mathsf T}$, and reading the column and the row gives the pair.

**The contraction.** The product in the other order is not an element of the cone but a multiple of the idempotent,

$$
\chi\psi=\varepsilon(\chi,\psi)\,\tilde\Pi_{+},
\qquad
\varepsilon(\chi,\psi)=\chi_{1}\psi_{1}+\chi_{2}\psi_{2},
$$

with $\varepsilon$ complex bilinear and carrying no conjugation. Its value is the scalar part,

$$
2Q_t=\varepsilon(\chi,\psi),
$$

which is the same identity as $2Q_t=v^{\mathsf T}u$ in the matrix model. **The trace is the contraction of the two factors.**

**The two strata in this language.** For $Q=\psi\chi\neq0$ the spinor line $[\psi]$ lies in the hyperplane $\ker\chi$ exactly when $Q$ is pure. Off the pure stratum the line and the hyperplane are transverse and meet only in zero. So

$$
\mathbb{P}(\mathcal N)\cong\mathbb{P}(S_{+})\times\mathbb{P}(S_{+}^{\vee})\cong\mathbb{P}^{1}\times\mathbb{P}^{1},
$$

and the projectivised pure stratum is the incidence variety — in rank two, the diagonal — while the non-pure stratum is its complement. An idempotent is a pair of a line and a distinct hyperplane; a nilpotent is a pair in which the two coincide.

This is the sharpest form of the statement that the cone is a product of two rays. It is also the reason the degenerate case is not a degenerate version of the regular one: the regular element is a transformation, and the degenerate one is a pair of a direction with a covector.

**The three non-zero sectors, in one glance.** $\Sigma_{01}$ is a scaled idempotent, with a live mode and a dead one. $\Sigma_{00}$ is a nilpotent, with the single eigenvalue $0$. $\Sigma_{10}$ is a unit with no eigenbasis: $N=Q_t^{2}\neq0$ and $B^{2}=0$, so the element is invertible and not diagonalisable. The cone contains elements of two spectral types and the complement contains elements of two spectral types. $N$ and $B^{2}$ are independent, and only $N$ answers the question of this article.

## Three Losses with One Source

Three constructions in the corpus need an inverse, and all three fail on the same set. The corpus states them in three places and never says they are one fact.

### No Inverse

Immediate from the determinant. In the algebra the candidate is

$$
\tilde Q^{-1}=\frac{\tilde Q^{\natural}}{\langle\tilde Q\rangle_{\natural}},
$$

which is undefined exactly at $N=0$. Note what the formula says: a vanishing norm is a division by zero and nothing subtler. There is no sense in which a degenerate element is almost invertible with a large inverse; the inverse does not exist, and a family approaching the cone has an inverse whose scale diverges.

### No Generator

The exponential has the group of units as its image and the cone as its complement (*The Exponential, the Logarithm and the Generator*). A degenerate element has no logarithm and therefore no generator: there is no $\tilde L$ with $\exp\tilde L=\tilde Q$. The physical reading is that the element cannot be written as the result of a continuous process of finite rate, and the corpus records the two ways out: a boundary value approached at infinite rate, or a Lindbladian superoperator in place of an element.

### No Polar Word

The four-factor word is

$$
\tilde Q=r\,e^{i\alpha}\,\tilde U_{\Psi,\mathrm b}\,\tilde u_{\mathrm r},
$$

and it exists on the complement of the cone and on no larger set. The reason is one line of multiplicativity:

$$
N\bigl(r\,e^{i\alpha}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}\bigr)
=r^{2}e^{2i\alpha}\cdot1\cdot1=r^{2}e^{2i\alpha}\neq0,
$$

because the boost has $N$-norm one and the rotor is a unit. **Every value of the word is a unit.** The cone is not a bad point of the chart; it is outside the chart's range. No branch, no extension of the parameter range and no change of order puts a zero divisor in the image.

### The One Source

The three failures are one fact. A bijection has an inverse; a group element has a logarithm, because the exponential is a local diffeomorphism onto the units; a unit has the four-factor word, because its factors are built by inverting and taking a square root of $\tilde Q\tilde Q^{*}$, which is positive definite exactly when $\tilde Q$ is invertible.

In each case the constructed object is a function of $\tilde Q^{-1}$, and $\tilde Q^{-1}$ does not exist. What the corpus presents as three domains is one domain, and any fourth construction built by inversion will inherit it.

## The Two Polar Decompositions

### One Pair, Two Regimes

The corpus says "the polar decomposition" for two different statements, and the degenerate case looks like a failure only while they are confused.

**The two-factor decomposition** is $\tilde Q=\tilde Q_H\tilde Q_0$ with $\tilde Q_H=(\tilde Q\tilde Q^{*})^{1/2}$ Hermitian positive semidefinite and $\tilde Q_0=\tilde Q_H^{+}\tilde Q$ a partial isometry. It exists for every element of the algebra, is unique, and is the matrix polar decomposition read in the algebra.

**The four-factor word** is a parametrisation of the group of units. It exists on $N\neq0$ and nowhere else.

The two answer different questions. The first asks *what is this operator, as a positive factor times an isometry*; it is available always. The second asks *which unit is this*; it is available only where there is a unit. The first is a decomposition of the element; the second is a coordinate system on the group.

| regime | $\tilde Q_H$ | $\tilde Q_0$ | four-factor word |
| --- | --- | --- | --- |
| $N\neq0$ | Hermitian positive definite | $*$-unitary | exists |
| $N=0$, $\tilde Q\neq0$ | Hermitian positive semidefinite of rank one | a partial isometry, not $*$-unitary | does not exist |
| $\tilde Q=0$ | $0$ | $0$ | does not exist |

### The Regular Case: the Word

On $N\neq0$ the pair sharpens. Write the modulus as a square root of the norm in the chosen half-plane,

$$
\Rho^{2}=\langle\tilde Q\rangle_{\natural},
\qquad
r=\lvert\Rho\rvert>0,
\qquad
e^{i\alpha}=\Rho/r,
$$

and the unit factor as $\tilde U=\tilde Q/\Rho$, of norm one. Then

$$
\tilde Q=\Rho\,\tilde U=r\,e^{i\alpha}\,\tilde U,
$$

and the unit factor splits into a Hermitian positive factor and a real rotor,

$$
\tilde U=\tilde U_{\Psi,\mathrm b}\,\tilde u_{\mathrm r},
\qquad
\tilde U_{\Psi,\mathrm b}=\bigl(\tilde U\tilde U^{*}\bigr)^{1/2},
\qquad
\tilde u_{\mathrm r}=\tilde U_{\Psi,\mathrm b}^{-1}\tilde U .
$$

Four properties of the pair are used below. The boost is Hermitian positive definite of norm one, and the set of such elements is the hyperbolic space $H^{3}$ of real dimension three. The rotor is a unit real quaternion, because $\tilde u_{\mathrm r}\tilde u_{\mathrm r}^{*}=e_t$ together with $\langle\tilde u_{\mathrm r}\rangle_{\natural}=1$ forces its imaginary part to vanish; it is a point of $SU(2)=S^{3}$. The two factors do not commute, and their order is part of the definition. And the dimensions add:

$$
8=\underbrace{1}_{r}+\underbrace{1}_{\alpha}+\underbrace{3}_{\text{boost}}+\underbrace{3}_{\text{rotor}},
$$

which is the count of the algebra, and the reason the word is a bijection onto the units rather than a description with a spare parameter.

### The Degenerate Case: Rank One and a Partial Isometry

On the cone the modulus vanishes, $\Rho^{2}=N=0$, so the modulus–unit writing and the four-factor word are both unavailable. What survives is the pair, with closed forms.

Write the Hermitian square as

$$
\tilde Q\tilde Q^{*}=\langle\tilde Q\rangle_{*}e_t+i\vec W,
\qquad
\vec W\ \text{real}.
$$

On the cone the identity $\langle\tilde Q\tilde Q^{*}\rangle_{\natural}=\langle\tilde Q\rangle_{*}^{2}-\lvert\vec W\rvert^{2}$ reads $\lvert\vec W\rvert=\langle\tilde Q\rangle_{*}$, and with

$$
a=\sqrt{\frac{\langle\tilde Q\rangle_{*}}{2}},
\qquad
\lvert\vec W\rvert=2a^{2},
$$

the Hermitian factor is

$$
\tilde Q_H=a\,e_t+\frac{i}{2a}\,\vec W
$$

for $\tilde Q\neq0$, and $\tilde Q_H=0$ at the apex. Its square is $\tilde Q\tilde Q^{*}$, its spectral values are $a\pm a$, that is $0$ and $2a$, so it is positive semidefinite of **rank one**, and its scalar part and the length of its vector part are both $a$.

The factor satisfies the quadratic identity $\tilde Q_H^{2}=2a\tilde Q_H$, hence

$$
\tilde Q_H^{+}=\frac{\tilde Q_H}{4a^{2}},
\qquad
\tilde Q_0=\tilde Q_H^{+}\tilde Q=\frac{\tilde Q_H\tilde Q}{4a^{2}},
$$

and the final projection is

$$
\tilde Q_0\tilde Q_0^{*}=\frac{\tilde Q_H}{2a},
$$

a rank-one projection and not the identity. That product is the whole proof that the isometry factor is not $*$-unitary: unitarity would require $e_t$, and the projection has rank one.

**What is continuous and what is not.** The Hermitian factor is the continuous limit of the regular one as the element approaches the cone. The isometry factor is not continuous there, and the reason is visible in the final projection: at the cone it has lost a dimension, and a rank-one projection cannot be approached continuously by the identity.

So the correct statement is not that a degenerate element has no polar decomposition. It is:

- the two-factor decomposition is defined on every element, the cone included;
- the four-factor word is defined only off the cone.

Confusing the two is what makes the degenerate case look like a failure of polar decomposition, when it is a failure of one chart on one group.

### The Limit of the Word

The word has boundary values on the cone. A family with $r=Re^{-\psi/2}$ and $\psi\to\infty$ reaches

$$
L=\frac{R\varkappa_{\mathrm{phs}}}{2}\bigl(e_t+i\vec u_{\mathrm b}\bigr)\tilde u_{\mathrm r},
\qquad
\varkappa_{\mathrm{phs}}=e^{i\alpha},
$$

a non-zero rank-one null element, with the idempotent stratum for $\operatorname{Sc}L\neq0$ and the nilpotent stratum for $\operatorname{Sc}L=0$ (*The Massless Limit as a Boundary Value of the Polar Word*). Two things follow.

**The element has a limit.** The cone is reachable, so the degenerate case is a boundary of the same theory and not a different one.

**The generator has no limit, and the limit is path-dependent.** The cone is not a graph over the units, so different families reach different boundary points, and the rate at which the wall is approached is extra data. The boundary value is not a value of the word: it is what the word does when its domain is exhausted.

## The Four Sectors

### The Grid

The two conditions together cut the algebra into four sectors, and the four are the four degeneration patterns of one quadratic.

| sector | conditions | spectrum | normal form | $N$ | minimal polynomial |
| --- | --- | --- | --- | --- | --- |
| $\Sigma_{11}$ | $N\neq0$, $B^{2}\neq0$ | $\{\lambda_+,\lambda_-\}$, distinct and non-zero | $\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-$, both terms non-zero | $\lambda_+\lambda_-\neq0$ | $p_{\tilde Q}$, squarefree |
| $\Sigma_{10}$ | $N\neq0$, $B^{2}=0$ | $\{Q_t\}$, $Q_t\neq0$ | $Q_te_t$, or $Q_tu$ with $u\neq e_t$ unipotent | $Q_t^{2}\neq0$ | $X-Q_t$ or $(X-Q_t)^{2}$ |
| $\Sigma_{01}$ | $N=0$, $B^{2}\neq0$ | $\{c,0\}$, $c\neq0$ | $c\tilde\Pi$, $\tilde\Pi$ non-trivial | $0$ | $p_{\tilde Q}$, squarefree |
| $\Sigma_{00}$ | $N=0$, $B^{2}=0$ | $\{0\}$ | $0$, or a non-zero nilpotent of index two | $0$ | $X$ or $X^{2}$ |

The four patterns are the four ways for the roots to degenerate: two distinct non-zero roots; a double non-zero root; two distinct roots, one zero; a double root at zero. There is no fifth.

**The same grid in components.** For $Q_t\neq0$ put $\vec Z=\vec Q/Q_t$. Then $(\vec Z,\vec Z)=-N/Q_t^{2}$, so both conditions are read from the scalar part and from one complex number.

| sector | $Q_t$ | $\vec Q$ | $(\vec Z,\vec Z)$ | real parameters |
| --- | --- | --- | --- | --- |
| $\Sigma_{11}$ | any | $(\vec Q,\vec Q)\neq0$ | neither $0$ nor $-1$ | $8$ |
| $\Sigma_{10}$ | $\neq0$ | $(\vec Q,\vec Q)=0$ | $0$ | $6$ |
| $\Sigma_{01}$ | $\neq0$ | $(\vec Q,\vec Q)=-Q_t^{2}$ | $-1$ | $6$ |
| $\Sigma_{00}$ | $0$ | $(\vec Q,\vec Q)=0$ | not formed | $4$ |

The fourth column needs $Q_t\neq0$, and in the last row it cannot be formed. The count of parameters is the count of the conditions: two real equations cut the eight real coefficients of $\tilde Q$ to the six of the cone, and in the pure stratum two more cut them to four.

### The Two Mixed Sectors

$\Sigma_{10}$ and $\Sigma_{01}$ are the independence witnesses, and they are worth naming because they are the sectors in which the two words *regular* and *degenerate* point in opposite directions.

**$\Sigma_{10}$: a unit with no eigenbasis.** $N=Q_t^{2}\neq0$ and $B^{2}=0$. The element is invertible and its two eigenvalues coincide, so it is either scalar or a Jordan element. It has a polar decomposition and no spectral decomposition. Its inverse and its word exist; its eigenbasis does not.

**$\Sigma_{01}$: a zero divisor with a full eigenbasis.** $N=0$ and $B^{2}\neq0$. The element is a scaled idempotent, its two eigenvalues are distinct, and it is diagonalisable. It has a spectral decomposition and no polar decomposition. Its eigenbasis exists; its word does not.

The two failures are independent and they occur in opposite sectors. That is the content of the warning that degeneracy of the norm is not degeneracy of the spectrum, and it is not a verbal warning: the two conditions have different zero sets and different physical readings.

### The Chain of Invariants

| invariant | data | number of types | what it separates |
| --- | --- | --- | --- |
| norm | $N$ | $2$ | the units from the cone |
| characteristic polynomial | $(2Q_t,N)$ | $4$ | the four sectors |
| minimal polynomial | $m_{\tilde Q}$ | $6$ | the six strata |

The count is of types and not of values. The chain is a chain of functions: the norm is the constant term of $p_{\tilde Q}$, and $p_{\tilde Q}$ is determined by $m_{\tilde Q}$. Read downward, information is lost. The norm forgets the sum of the eigenvalues; the characteristic polynomial forgets the defect; the minimal polynomial forgets nothing.

The six strata are the four sectors with two of them split. $\Sigma_{10}$ splits into the punctured scalar line $\Sigma_{10}^{\mathrm{s}}$ and the Jordan cone $\Sigma_{10}^{\mathrm{J}}$; $\Sigma_{00}$ splits into the apex and the non-zero nilpotents. The norm sees neither split: the scalar $Q_te_t$ and the Jordan element $Q_te_t+\vec\Upsilon$ have the same norm and the same characteristic polynomial, and the apex and every non-zero nilpotent have norm zero and the same characteristic polynomial $X^{2}$.

| stratum | spectral decomposition | polar word | modulus |
| --- | --- | --- | --- |
| $\Sigma_{11}$ | two terms, unique | yes | yes |
| $\Sigma_{10}^{\mathrm{s}}$ | one term | yes | yes |
| $\Sigma_{10}^{\mathrm{J}}$ | none | yes | yes |
| $\Sigma_{01}$ | two terms, unique | no | no |
| apex | one term, trivial | no | no |
| $\Sigma_{00}\setminus\{0\}$ | none | no | no |

The table is the shortest statement in the article of what degeneracy costs, and it costs two different things in two different places.

## Physical Readings

- **$N$-regular is a transformation; $N$-degenerate is a ray.** A unit is a change of frame — a boost, a rotation, a scale, a phase — and a zero divisor is a direction with an intensity and no frame. Boundary: the reading is of the element's operator, and a physical process described by a unit can still be dissipative when the unit is not the whole story.
- **The cone is the wall of reversibility.** No operation on the cone can be undone, and by the absorbing property no composition repairs it. Boundary: this is an algebraic statement about inverses; the thermodynamic reading is separate and cited, not derived.
- **Mass is the distance from the wall.** On the material sector $N=-m^{2}c^{2}$, so $m=0$ is the wall and $m^{2}$ measures how far outside it the four-momentum sits. Boundary: the identification needs the material slice; the value of the mass is an input, not a prediction.
- **Something is always annihilated on the cone, and it is a plane.** A degenerate element identifies half of its domain — a gauge redundancy, a decoupled polarisation, or a projection — and never a single direction, because the algebra is four-dimensional and the rank drops by two. Boundary: which physical mode is annihilated is representation data and is not fixed by the algebra.
- **The two sectors of degeneracy are two physical objects.** $\Sigma_{01}$, the scaled idempotent, is a polarisation: a selected plane with a weight, and a killed transversal. $\Sigma_{00}$, the nilpotent, is a nilpotent shift: it has no selected plane at all. A field strength and a null translation sit in different sectors, and the difference is not one of degree.
- **The degenerate element keeps a direction and a scale.** On $\Sigma_{01}$ the normal form $c\tilde\Pi$ is exact and exhaustive. Boundary: the rapidity is the parameter that is lost, so a family on the cone has no rate.
- **$\Sigma_{01}$ propagates; $\Sigma_{00}$ does not.** In the first the image and the kernel are complementary, so a live plane survives beside the annihilated one; in the second the image equals the kernel, so the element annihilates its own output.
- **Spin zero is a unit, half a spin is a ray, and one spin is a null cone.** A minimal left ideal is on the cone at every point, so a pure spin-$\tfrac12$ state is a ray whatever its amplitude; the centre is on the cone only at the origin, so a spin-$0$ state is a unit wherever it is non-zero; on the traceless part $N$ reduces to $B^{2}$, so a spin-$1$ state is on the cone exactly when it is null. Boundary: the correspondence runs from the carrier to the norm and not the other way.
- **Mass is interference.** For a spin-$\tfrac12$ field the two chiral parts are individually isotropic, so the norm of the sum is the cross term alone and the mass is the interference of two rays. Boundary: the two parts are the two components of one element, not two particles.
- **A photon is a single ray.** The field strength of a null wave is a zero divisor, so it has no second part and generates no mass. Boundary: this is the null condition of the field strength, not a statement about the four-momentum, which is a different element of the same cone.
- **The two polar decompositions answer two questions.** The two-factor pair is available on the cone and is the matrix polar decomposition; the four-factor word is not, and is a chart on the group of units. A statement that uses one and means the other is wrong on the whole cone.

## Limits

**The norm is algebraic; the words are sector-dependent.** $N=0$ is one complex equation. Reading it as *massless* needs the material sector, reading it as *non-reversible* needs the operator picture, and reading it as *nilpotent* needs the pure stratum. The three readings are not the same statement, and the algebra supplies only the common criterion.

**The cone is thin, and that is not a statement about importance.** The cone is a complex hypersurface of real codimension two, so a generic element is a unit. But the rest frame, the null field, the gauge redundancy and the exceptional point all lie on it or on its relatives. A thin set is not a negligible set.

**No dynamics, no particle content, no mass spectrum.** The article reads one element at one point. It supplies no equation of motion and predicts no mass values.

**Degeneracy of the norm is not degeneracy of the spectrum.** $\Sigma_{01}$ is spectrally regular and $N$-degenerate; $\Sigma_{10}$ is $N$-regular and spectrally degenerate. Any sentence that uses *degenerate* without its qualifier is ambiguous in this corpus, and the ambiguity is not verbal: the two conditions have different zero sets, and the coincidence on the cone is a theorem about the cone and not a general fact.

**The two-sector structure is a statement about the characteristic polynomial.** The four sectors are the four root patterns of a monic quadratic. A finer reading, splitting the scalar line from the Jordan part and the apex from the non-zero nilpotents, refines two sectors by the minimal polynomial. It adds no sector.

**The spinor reading is a reading of the cone, not a state space.** $S_{+}$ is a minimal left ideal on which the algebra acts irreducibly; a physical state is a normalised element of such a carrier with a metric added. The product description $\mathcal N=\{\psi\chi\}$ uses no metric and no conjugation, and it survives the addition of the metric, but the metric is not part of it.

**The absorbing property is not a conservation law.** That products of a degenerate element stay degenerate says nothing about whether a physical quantity is conserved; the conserved currents of the corpus are built from pairings, and their conservation is a separate computation.

## Summary

- The norm is the determinant, $N=\det\mathsf M_2(\tilde Q)$, and it is multiplicative; the inverse is $\tilde Q^{\natural}/N$.
- $N$-regular means invertible: the element is a bijection, nothing is annihilated, and the sector is the group $\mathbb{B}^{\times}\cong GL_2(\mathbb{C})$, open and dense, of real dimension eight, with $\partial\mathbb{B}^{\times}=\mathcal N$ and $\pi_1\cong\mathbb{Z}$.
- $N$-degenerate means singular: the sector is the cone $\mathcal N$, of real dimension six and codimension two, contractible, singular at the apex, of link $S^{2}\times S^{3}$, and absorbing under multiplication.
- The cone has three strata: the apex, the pure stratum of nilpotents of index two of real dimension four, and the non-pure stratum of idempotent multiples of real dimension six. The split is by the scalar part $Q_t$, and on the cone $Q_t=0$ is $B^{2}=0$.
- The cone has two sectors of degeneracy: $\Sigma_{01}$, the scaled non-trivial idempotents $c\tilde\Pi$ with spectrum $\{c,0\}$, and $\Sigma_{00}$, the nilpotents with spectrum $\{0\}$. The first is a projection, the second a nilpotent shift.
- $N=\lambda_+\lambda_-$ is the constant term of the characteristic polynomial and $-4B^{2}$ is the discriminant; the four sectors are the four root patterns, and there is no fifth. In components the sector is read from the scalar part and from the square of the vector part: $Q_t\neq0$ with $Q_x^{2}+Q_y^{2}+Q_z^{2}=-Q_t^{2}$ is $\Sigma_{01}$, and $Q_t=0$ with $Q_x^{2}+Q_y^{2}+Q_z^{2}=0$ is $\Sigma_{00}$.
- On a non-zero degenerate element the kernel is exactly a complex plane and the rank of left multiplication is $2$; it is $4$ on the units and $0$ at the apex. The loss is never one-dimensional.
- In $\Sigma_{01}$ the image is complementary to the kernel; in $\Sigma_{00}$ the image equals it. That is the operator form of $\tilde Q^{2}=c\tilde Q$ against $\tilde\nu^{2}=0$.
- The cone is the set of products of a spinor with a co-spinor, the trace is the contraction $2Q_t=\varepsilon(\chi,\psi)$, and the pure stratum is the incidence of a line with a hyperplane.
- Three failures have one source: no inverse, no generator and no polar word are all failures of a construction built from $\tilde Q^{-1}$.
- The two-factor decomposition is defined on every element; on the cone its Hermitian factor is $\tilde Q_H=ae_t+i\vec W/(2a)$ of rank one and its isometry is a partial isometry with final projection $\tilde Q_H/(2a)$.
- The four-factor word is a parametrisation of the group of units; every value of it is a unit, so the cone is outside its range and not inside its domain.
- The degenerate element keeps a direction and a scale on $\Sigma_{01}$ and loses the rapidity; the word has boundary values on the cone and the generator does not, and the limit is path-dependent.
- $N$ vanishes identically on a minimal left ideal, by multiplicativity and the isotropy of the idempotent: every pure spin-$\tfrac12$ state is a ray.
- The norm of a sum of one element from each ideal is the cross term alone, so the mass of a spin-$\tfrac12$ field is the interference of two rays; a null field strength is a single zero divisor and generates no mass.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\tilde Q=Q_te_t+\vec Q$ | a general biquaternion, $Q_t\in\mathbb{C}$, $\vec Q\in\mathbb{C}^{3}$ |
| $N=\langle\tilde Q\rangle_{\natural}$ | the quaternionic norm, $Q_t^{2}+B^{2}$; the determinant of $\mathsf M_2(\tilde Q)$ |
| $B^{2}=(\vec Q,\vec Q)$ | the square of the vector part; the discriminant is $-4B^{2}$ |
| $\mathbb{B}^{\times}$ | the group of units, $\{N\neq0\}$ |
| $\mathcal N=\{N=0\}$ | the null cone, apex included |
| $\mathcal N_{\mathrm p}$, $\mathcal N_{\mathrm{np}}$ | the pure and the non-pure strata |
| $\mathcal S=\{B^{2}=0\}$ | the spectral cone, the locus of the double root |
| $\Sigma_{ij}$ | the sector with $N\neq0$ if $i=1$ and $B^{2}\neq0$ if $j=1$ |
| $\lambda_\pm=Q_t\pm iB$ | the eigenvalues; $N=\lambda_+\lambda_-$ |
| $\operatorname{rank}L_{\tilde Q}$ | $4$ on the units, $2$ on the non-zero cone, $0$ at the apex |
| $\tilde Q^{\natural}$, $\tilde Q^{*}$ | the quaternionic and the Hermitian conjugates |
| $\tilde\Pi_\pm=\tfrac12(e_t\pm\vec Z)$, $\vec Z^{2}=e_t$ | the primitive idempotents, isotropic, $N(\tilde\Pi_\pm)=0$ |
| $S_\pm=\mathbb{B}\tilde\Pi_\pm$, $S_+^{\vee}=\tilde\Pi_+\mathbb{B}$ | the minimal left ideals and the co-spinor row space |
| $\varepsilon(\chi,\psi)$ | the contraction of a co-spinor with a spinor, $2Q_t$ |
| $c\tilde\Pi$ | the normal form on $\Sigma_{01}$, $c=2Q_t$ |
| $\Rho$, $r$, $\alpha$ | the modulus, the scale and the central phase of the word |
| $\tilde U_{\Psi,\mathrm b}$, $\tilde u_{\mathrm r}$ | the Hermitian boost and the real rotor |
| $\tilde Q_H$, $\tilde Q_0$ | the two-factor decomposition, defined on every element |

## Further Reading

- [N-Regularity and N-Degeneracy in the Biquaternion Algebra](../articles_maths/n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html), for the norm, its multiplicativity, the group of units and the two strata of the cone.
- [The N-Regular Sector](../articles_maths/the-n-regular-sector.html), for the unit group, its dimension, its topology and its two spectral cells.
- [The N-Degenerate Sector](../articles_maths/the-n-degenerate-sector.html), for the cone, the three strata, the link, the rank-one model and the spinor–co-spinor reading.
- [The Polar Decomposition of an N-Regular Biquaternion](../articles_maths/the-polar-decomposition-of-an-n-regular-biquaternion.html), for the modulus, the unit factor and the four factors.
- [The Polar Decomposition of an N-Degenerate Biquaternion](../articles_maths/the-polar-decomposition-of-an-n-degenerate-biquaternion.html), for the rank-one Hermitian factor, the partial isometry and the worked examples.
- [Relations between the N Norm and Spectral Regularity and Degeneracy](../articles_maths/relations-between-the-n-norm-and-spectral-regularity-and-degeneracy.html), for the four sectors, the characteristic polynomial and the chain of invariants.
- [Norm and Pairing Conventions](norm-and-pairing-conventions.html), for the four norms, the qualified regular and degenerate, and the domain of the word.
- [Introduction to N and Spectrally Regular and Degenerate Operators](../articles_maths/introduction-to-n-and-spectrally-regular-and-degenerate-operators.html), for the rank, the images and the kernels of the four sectors.
- [The Four Regimes of an Element: Mass and Motion](the-four-regimes-of-an-element-mass-and-motion.html), for the sector partition and its physical labels.
- [Physical Interpretation of Spectral Regularity and Degeneracy in the Biquaternion Algebra](physical-interpretation-of-spectral-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the spectral question and the warning that it is not the norm's question.
- [The Zero-Divisor Cone and the Massless Spectrum](the-zero-divisor-cone-and-the-massless-spectrum.html), for the cone as the light cone and the wall of invertibility.
- [The Exponential, the Logarithm and the Generator](the-exponential-the-logarithm-and-the-generator.html), for the units as the image of the exponential and the cone as its complement.
- [The Polar Decomposition and Its Three Pairings](the-polar-decomposition-and-its-three-pairings.html), for the word, its three bracketings and the table of domains.
- [The Massless Limit as a Boundary Value of the Polar Word](the-massless-limit-as-a-boundary-value-of-the-polar-word.html), for the boundary value, the two strata and the path dependence.
- [The Hamilton Pairing: Mass as Modulus and the Complex Angle](the-hamilton-pairing-mass-as-modulus-and-the-complex-angle.html), for the modulus $\Rho=\sqrt N$, the complex angle and the cross term in the mass of a sum.
- [Angular Momentum and Spin in the Biquaternion Algebra](../articles_maths/angular-momentum-and-spin-in-the-biquaternion-algebra.html), for the three carriers, their spins and the statement that the algebra determines no dynamics.
- [Spin and the Three Elementary Carriers](spin-and-the-three-elementary-carriers.html), for the carrier table and the identification with the observed spins.
- [Null Electromagnetic Fields and the Shear-Free Congruence](null-electromagnetic-fields-and-the-shear-free-congruence.html), for the null field strength as a zero divisor.
- [The Polar Decomposition of a Biquaternion](../articles_maths/the-polar-decomposition-of-a-biquaternion.html), for the two-factor decomposition defined on every element.
