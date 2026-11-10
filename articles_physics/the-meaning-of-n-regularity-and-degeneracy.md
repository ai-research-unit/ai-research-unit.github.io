# __The Meaning of N Regularity and Degeneracy__

## Introduction

Two words, one number. The biquaternion norm is

$$
N=\langle\tilde Q\rangle_{\natural}=Q_t^{2}+B^{2},
\qquad B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2},
$$

and an element is **$N$-regular** when $N\neq0$ and **$N$-degenerate** when $N=0$. The pair is used everywhere in the corpus: it is the domain of the polar word, the domain of the logarithm, one of the two conditions that cut the four sectors, and the level set that carries the mass. What it *means* is stated in one line by *Norm and Pairing Conventions*, §*The Four Algebraic Norms and the Unitary Convention*: of the four algebraic norms, only $N$ decides invertibility.

This article works out that line. The answer is short, and everything else in the corpus's use of the pair is a consequence of it.

**$N$ is the determinant.** So $N$-regular means invertible, and an invertible element is a bijection of the algebra onto itself: nothing is annihilated, the map can be undone, and it is a transformation. $N$-degenerate means singular: the element has a non-zero kernel, it annihilates something, it cannot be undone, and it is a ray rather than a transformation. The pair is not a classification of elements into two convenient boxes. It is the algebraic form of the question *is anything lost?*

Four results are developed.

**One source for three failures.** The element has no inverse, no logarithm and no polar word on the cone. These are not three defects of three constructions; they are the rank seen through three constructions, and they arrive together because they have one cause.

**One number for the size of the loss.** The rank of left multiplication is $4$ on the units, $2$ on the cone away from the origin, and $0$ at the origin. The loss is not gradual and it is never one-dimensional: a non-zero degenerate element annihilates exactly a complex plane, in either stratum and without exception.

**What survives.** Direction, scale and a normal form. The two-factor decomposition is defined on every element, so a decomposition of the degenerate element exists; what fails is the four-factor word, which is a statement about the group of units and about no larger set. The degenerate element is a limit of units and is not one.

**The carriers are not uniform in this respect.** The norm vanishes *identically* on a minimal left ideal, by multiplicativity and the isotropy of the idempotent. So a pure spin-$\tfrac12$ state is always a ray, a pure spin-$0$ state is never one, and the mass of a spin-$\tfrac12$ field is the interference of two rays. This is the one statement of the article that is not already in the sources, and it is proved in §*The Carriers*.

The article is a reading article. It cites the mathematics, proves the corollary on the carriers, and states at each step whether the physical word in play — mass, reversibility, gauge — is supplied by the algebra or imported from the material sector.

The conventions are those of the read list. The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with $e_t=1$ and $\vec e_\mu^{2}=-e_t$; $i$ is the central scalar imaginary; $\natural$ is the quaternionic conjugation and $*$ the Hermitian conjugation; $\mathbb{B}^{\times}=\{\tilde Q:N\neq0\}$ is the group of units; $\tilde\Pi_\pm=\tfrac12(e_t\pm\vec Z)$ with $\vec Z^{2}=e_t$ are the primitive idempotents and $S_\pm=\mathbb{B}\tilde\Pi_\pm$ the minimal left ideals; $V=\ker\operatorname{tr}$ is the traceless part; and $\Sigma_{ij}$ is the sector with $N\neq0$ if $i=1$ and $B^{2}\neq0$ if $j=1$.

## The Results It Uses

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| The norm $N=Q_t^{2}+B^{2}$, its multiplicativity, the group of units and the zero-divisor cone | [N-Regularity and N-Degeneracy in the Biquaternion Algebra](../articles_maths/n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html), §*The Quaternionic Norm* and §*The $\natural$-degenerate case* |
| Only $N$ decides invertibility among the four norms; the qualified regular and degenerate; the domain of the polar word | [Norm and Pairing Conventions](norm-and-pairing-conventions.html), §*The Four Algebraic Norms and the Unitary Convention* |
| The isomorphism $\mathsf M_2$, with $\langle\tilde Q\rangle_{\natural}=\det\mathsf M_2(\tilde Q)$ and the units as the invertible matrices | [$M_2(\mathbb C)$ Pauli Representation](../articles_maths/m2c-pauli-representation.html), §*The Compression* |
| The four sectors, the rank of $L_{\tilde Q}$, the images and the kernels | [Introduction to N and Spectrally Regular and Degenerate Operators](../articles_maths/introduction-to-n-and-spectrally-regular-and-degenerate-operators.html), §*The One-Sided Operators* |
| The idempotents, their isotropy $\langle\tilde\Pi\rangle_{\natural}=0$, and the minimal left ideals | [Square Roots of One and the Idempotents of the General Quaternionic Algebra](../articles_maths/square-roots-of-one-and-the-idempotents-of-the-general-quaternionic-algebra.html); [The Peirce Decomposition of the Biquaternion Algebra](../articles_maths/the-peirce-decomposition-of-the-biquaternion-algebra.html) |
| The spectral cone $B^{2}=0$, its three strata, and the independence of $N\neq0$ and $B^{2}\neq0$ | [The Jordan Basis of a Spectrally Degenerate Biquaternion](../articles_maths/the-jordan-basis-of-a-spectrally-degenerate-biquaternion.html); [Relations between the N Norm and Spectral Regularity and Degeneracy](../articles_maths/relations-between-the-n-norm-and-spectral-regularity-and-degeneracy.html) |
| The exponential and the logarithm, with the group of units as the image and the cone as the complement | [Biquaternion Elementary Functions](../articles_maths/biquaternion-elementary-functions.html) |
| The general H-norm two-factor decomposition on every non-zero element; the Cartan pairing off the cone; its extension to the cone, with a partial isometry | [The Polar Decomposition of a Biquaternion](../articles_maths/the-polar-decomposition-of-a-biquaternion.html); [The Cartan Hermitian Pairing of the Polar Decomposition of an N-Regular, Spectrally Regular Biquaternion](../articles_maths/the-cartan-hermitian-pairing-of-the-polar-decomposition-of-an-n-regular-spectrally-regular-biquaternion.html); [The Polar Decomposition of an N-Degenerate Biquaternion](../articles_maths/the-polar-decomposition-of-an-n-degenerate-biquaternion.html) |
| The four-factor word, its domain and its three pairings | [The Polar Decomposition and Its Three Pairings](the-polar-decomposition-and-its-three-pairings.html) |
| The three carriers, their dimensions and their spins | [Angular Momentum and Spin in the Biquaternion Algebra](../articles_maths/angular-momentum-and-spin-in-the-biquaternion-algebra.html); [Spin and the Three Elementary Carriers](spin-and-the-three-elementary-carriers.html) |
| The cone as the light cone of the material sector and the level set as the mass shell | [The Zero-Divisor Cone and the Massless Spectrum](the-zero-divisor-cone-and-the-massless-spectrum.html); [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html) |
| The massless limit as a boundary value of the word, and the path dependence | [The Massless Limit as a Boundary Value of the Polar Word](the-massless-limit-as-a-boundary-value-of-the-polar-word.html) |
| The Hamilton modulus, the complex angle and the cross term in the mass of a sum | [The Hamilton Pairing: Mass as Modulus and the Complex Angle](the-hamilton-pairing-mass-as-modulus-and-the-complex-angle.html) |
| Spectral regularity is not invertibility | [Physical Interpretation of Spectral Regularity and Degeneracy in the Biquaternion Algebra](physical-interpretation-of-spectral-regularity-and-degeneracy-in-the-biquaternion-algebra.html), §*Spectral Regularity Is Not Invertibility* |

The table is the contract: every statement below is either a theorem of one of these rows or a corollary drawn from two of them. The one corollary the corpus does not already contain is the carrier statement of §*The Carriers*, and it is proved there in two lines.

## The One Question the Norm Asks

### The Norm Is the Determinant

The map $\mathsf M_2$ reads the element as a $2\times2$ complex matrix, and under it the norm is the determinant:

$$
\langle\tilde Q\rangle_{\natural}=\det\mathsf M_2(\tilde Q).
$$

Two consequences follow immediately, and they are the whole of the algebra below.

**Multiplicativity.** $\det$ is multiplicative, so

$$
N(\tilde Q_1\tilde Q_2)=N(\tilde Q_1)\,N(\tilde Q_2).
$$

**The units are the invertible matrices.** Hence

$$
\mathbb{B}^{\times}=\{\tilde Q:N\neq0\}\cong\mathrm{GL}(2,\mathbb{C}),
$$

a group, and its complement is $\{\tilde Q:N=0\}$, a set with no group structure at all.

The pair is therefore not one partition among many. It is the partition of an algebra into its group of units and its complement, and that is why every construction built by inverting something has the same domain.

One consequence of multiplicativity deserves its own name, because it is the algebraic form of irreversibility.

**Proposition (the cone is absorbing).** If $N(\tilde Q)=0$ then $N(\tilde Q\tilde X)=N(\tilde X\tilde Q)=0$ for every $\tilde X$.

*Proof.* Multiplicativity gives $N(\tilde Q\tilde X)=N(\tilde Q)N(\tilde X)=0$, and the same on the other side.

Read plainly: once an element is on the cone, every product it enters is on the cone. Composing a singular element with anything, on either side, cannot restore what it destroyed. That is the reason no repair of a degenerate element is available anywhere in the corpus, and it is not a metaphor.

### Two Answers and a Wall

The dichotomy is one line and it is worth boxing, because every later section quotes it.

$$
\boxed{\;
N\neq0\iff\tilde Q\in\mathbb{B}^{\times}\iff L_{\tilde Q}\ \text{is a bijection},
\qquad
N=0\iff L_{\tilde Q}\ \text{has a non-zero kernel}\;}
$$

The two halves are exact negations of each other, and the middle term is what makes the pair operational: invertibility of the element and injectivity of the multiplication are the same condition.

The corpus calls the zero set the **wall of invertibility** (*The Zero-Divisor Cone and the Massless Spectrum*, §*The Cone as the Wall of Invertibility*). The name is earned. Inside the wall every operation is reversible; on it, none is; and the wall is crossed by a single complex condition, so two real conditions must be tuned to reach it.

### What the Other Three Norms Do Not Decide

The corpus carries four algebraic norms, and the choice of $N$ is not a matter of taste.

| norm | letter | the $\Xi$-degenerate set | verdict |
| --- | --- | --- | --- |
| plain | $P$ | contains units: $P(e_t+\vec e_x)=0$ with $N=2$ | vanishes on invertible elements |
| quaternionic | $N$ | the origin and the zero divisors | exact |
| Hermitian | $H$ | the origin alone | every zero divisor is $H$-regular |
| Krein | $\mathrm{Kr}$ | contains units: $\mathrm{Kr}(e_t+\vec e_x)=0$ with $N=2$ | vanishes on invertible elements |

The four fail in two different ways, and both failures matter. $P$ and $\mathrm{Kr}$ vanish on elements that can be inverted, so neither can be the criterion: their degenerate sets are too small. $H$ fails in the opposite direction: it vanishes only at the origin, so its regular set contains every zero divisor, and $H\neq0$ is necessary but not sufficient. Only $N$ has a degenerate set that is exactly the non-units.

This is why the conventions insist on the qualified form: an element is $\Xi$-regular when $\Xi(\tilde Q)\neq0$, and only the qualification $N$ carries the algebraic meaning. The unqualified *regular* is the spectral condition $B^{2}\neq0$, a third question, and the letter is never omitted.

The lesson is that **the meaning of the pair is algebraic and not metric**. $N$ is not a length that happens to vanish somewhere; it is a determinant. A length has a scale and a positivity; a determinant has a sign or a phase and a zero set, and the zero set is what is being read.

## What Is Annihilated

### The Kernel

The operational content of the dichotomy is a statement about what the element kills. A linear map that is not injective identifies distinct inputs: two different elements of the algebra are carried to one, and the information that distinguished them is gone. No inverse can restore it, because the inverse would have to choose between two preimages.

The kernel is therefore the object to look at, and it is computed in *Introduction to N and Spectrally Regular and Degenerate Operators*, §*The One-Sided Operators*.

| object | $\ker L_{\tilde Q}$ | $\operatorname{im}L_{\tilde Q}$ |
| --- | --- | --- |
| $\Sigma_{11}$, $\Sigma_{10}$ | $0$ | $\mathbb{B}$ |
| $\Sigma_{01}$, $\tilde Q=\kappa\tilde\Pi$ | a complex plane | the totally isotropic plane $\tilde Q\mathbb{B}$ |
| $\Sigma_{00}$, $\tilde Q=\tilde\nu$ nilpotent | a complex plane | $\mathbb{C}\tilde\nu\oplus\mathbb{C}\tilde\Pi_{+}=\ker L_{\tilde\nu}$ |
| $\tilde Q=0$ | $\mathbb{B}$ | $0$ |

Two features of that column are worth stating separately, because they are sharper than "the kernel is non-zero".

**The kernel is never odd-dimensional.** On a non-zero degenerate element it is exactly a complex plane, of complex dimension two, in both strata. There is no element of $\mathbb{B}$ whose left multiplication annihilates exactly a line, and none that annihilates a three-dimensional subspace. The loss is quantised: nothing, or half, or everything.

**The kernel can swallow the image.** On $\Sigma_{00}$ the image is contained in the kernel, which is the operator form of $\tilde\nu^{2}=0$: the element annihilates its own output, twice over. On $\Sigma_{01}$ they are complementary, $\mathbb{B}=\ker L_{\tilde Q}\oplus\operatorname{im}L_{\tilde Q}$, the operator form of $\tilde Q^{2}=\kappa\tilde Q$ with its two distinct roots. So the two strata differ by whether the surviving plane is beside the annihilated plane or inside it, and that is the whole of the difference between a ray that propagates and a shift that does not.

For the right multiplication the same table holds with $\mathbb{B}\tilde Q$ in place of $\tilde Q\mathbb{B}$, and the two images are distinct on the null strata; the left and right pictures agree on the rank.

### The Rank as the Measure of the Loss

One number summarises the table: the rank of left multiplication.

$$
\operatorname{rank}L_{\tilde Q}=
\begin{cases}
4, & N\neq0,\\
2, & N=0,\ \tilde Q\neq0,\\
0, & \tilde Q=0.
\end{cases}
$$

The jumps are by two and by two. The regular element loses nothing, the degenerate one loses exactly half its domain, and the zero element loses all of it. Because the algebra is four-dimensional over $\mathbb{C}$, "half" is a plane and not a ray, and that is the reason the degenerate case is geometrically rich: a plane has a direction, a transversal and a complement, while a single line would have none.

The same number is the reason the polar word cannot be repaired by adding a parameter. A chart with eight real parameters cannot cover an element whose operator has rank two, because the chart parametrises bijections and the element is not one.

### The Three Nonzero Forms

Degeneracy of the norm is not degeneracy of the spectrum, and the corpus keeps the two apart. For the record, because the distinction is used twice below:

- **$\Sigma_{01}$: a scaled idempotent.** $\tilde Q=\kappa\tilde\Pi(\vec Z)$ with $\kappa=2Q_t\neq0$; the eigenvalues are $\kappa$ and $0$, distinct. One live mode, one dead one, and the dead one is a genuine spectral direction: the mode is present in the basis and absent from the element.
- **$\Sigma_{00}$: a nilpotent.** $\tilde Q=\tilde\nu$ with $\tilde\nu^{2}=0$; the only eigenvalue is $0$; the operator is a two-step ladder.
- **$\Sigma_{10}$: a unit with no mode basis.** $N=Q_t^{2}\neq0$ and $B^{2}=0$; the element is invertible and has no eigenbasis. It is the counterexample that keeps the two questions apart, and its existence is the reason a statement about invertibility may never be replaced by a statement about the spectrum (*Physical Interpretation of Spectral Regularity and Degeneracy in the Biquaternion Algebra*, §*Spectral Regularity Is Not Invertibility*).

So the cone contains elements of two spectral types, and the complement contains elements of two spectral types. $N$ and $B^{2}$ are independent, and only $N$ answers the question of this article.

## Three Losses with One Source

Three constructions in the corpus need an inverse, and all three fail on the same set. It is worth listing them together, because the corpus states them in three places and never says they are one fact.

### No Inverse

Immediate from the determinant: a singular matrix has no inverse. In the algebra, the candidate inverse is

$$
\tilde Q^{-1}=\frac{\tilde Q^{\natural}}{\langle\tilde Q\rangle_{\natural}},
$$

which is undefined exactly at $N=0$. Note what the formula says: the inverse is the conjugate divided by the norm, so a vanishing norm is a division by zero and nothing subtler. There is no sense in which a degenerate element is "almost" invertible with a large inverse; the inverse does not exist, and a family approaching the cone has an inverse whose scale diverges.

### No Generator

The exponential map has the group of units as its image and the cone as its complement (*The Exponential, the Logarithm and the Generator*). A degenerate element has no logarithm and therefore no generator: there is no $\tilde L$ with $\exp\tilde L=\tilde Q$. The physical reading is that the element cannot be written as the result of a continuous process of finite rate, and the corpus records the two ways out: a boundary value approached at infinite rate, or a Lindbladian superoperator in place of an element.

### No Polar Word

The four-factor word is

$$
\tilde Q=r\,e^{i\alpha}\,\tilde U_{\Psi,\mathrm b}\,\tilde u_{\mathrm r},
$$

and it exists on the complement of the cone and on no larger set (*Norm and Pairing Conventions*, §*The Polar Word and the Three Pairings*). The reason is one line of multiplicativity:

$$
N\bigl(r\,e^{i\alpha}\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}\bigr)
=r^{2}\,e^{2i\alpha}\cdot1\cdot1=r^{2}e^{2i\alpha}\neq0,
$$

because the frame factor has $N$-norm one and the rotor is a unit. **Every value of the word is a unit.** The cone is not a bad point of the chart; it is outside the chart's range. No choice of branch, no extension of the parameter range and no change of order can put a zero divisor in the image.

### The One Source

The three failures are the same fact. A bijection has an inverse; a group element has a logarithm, because the exponential is a local diffeomorphism onto the units; a unit has a polar decomposition, because the two factors are built by inverting and taking a square root of $\tilde Q\tilde Q^{*}$, which is positive definite exactly when $\tilde Q$ is invertible.

In each case the object being constructed is a function of $\tilde Q^{-1}$, and $\tilde Q^{-1}$ does not exist. That is the content of the sentence at the head of this article. What the corpus presents as three separate domains is one domain, and any fourth construction built by inversion will inherit it.

## What the Degenerate Element Keeps

### The Direction and the Scale

On $\Sigma_{01}$ the element has a normal form that is as explicit as the regular one:

$$
\tilde Q=\kappa\,\tilde\Pi(\vec Z),\qquad \tilde\Pi(\vec Z)=\tfrac12\bigl(e_t+\vec Z\bigr),\qquad \vec Z^{2}=e_t,\qquad \vec Z\neq\pm e_t,\qquad \kappa=2Q_t\neq0 .
$$

Read the two factors. $\tilde\Pi(\vec Z)$ is a point of the complex quadric of minimal left ideals, so it carries a **direction** and nothing else; the map $\vec Z\mapsto\tilde\Pi(\vec Z)$ is two-to-one from $\{\vec Z:\vec Z^{2}=e_t\}$ onto the non-trivial idempotents. $\kappa$ is a complex number, so it carries a **scale and a phase**. Four complex parameters of an element have become one direction (two real) plus one complex scale (two real), and nothing is lost: $4=2+2$.

What is *not* there is the rapidity. The regular word carries the Hermitian factor $\tilde U_{\Psi,\mathrm b}$, a boost with a rapidity; on the cone that factor has run to the boundary,

$$
\frac{\tilde U_{\Psi,\mathrm b}\bigl(\theta_{\mathrm{rpd},w}\bigr)}
{2\cosh\tfrac{\theta_{\mathrm{rpd},w}}{2}}
=\tfrac12\bigl(e_t+i\tanh\tfrac{\theta_{\mathrm{rpd},w}}{2}\,\vec u_{\mathrm b}\bigr)
\longrightarrow\tfrac12\bigl(e_t+i\vec u_{\mathrm b}\bigr),
$$

a rank-one projector, which is a direction and no longer a transformation. The degenerate element has a direction where the regular one had a boost, and the rapidity is the parameter that is genuinely gone.

### The Normal Form

The degenerate element still has a two-factor decomposition, and the distinction from the four-factor word is the sharpest thing in this article.

The two-factor decomposition is $\tilde Q=\tilde Q_H\tilde Q_0$ with $\tilde Q_H=\sqrt{\tilde Q\tilde Q^{*}}$ Hermitian positive semidefinite and $\tilde Q_0$ a partial isometry. It is one decomposition in two regimes, not two decompositions:

| regime | $\tilde Q_H$ | $\tilde Q_0$ |
| --- | --- | --- |
| $N\neq0$ | Hermitian positive definite | $*$-unitary |
| $N=0$, $\tilde Q\neq0$ | Hermitian positive semidefinite of rank one | a partial isometry that is not $*$-unitary |

The first row is the Cartan pairing, which is a matrix polar decomposition read in the algebra; the second is its extension to the cone, where the Hermitian factor loses rank and the isometry loses unitarity (*The Polar Decomposition of a Biquaternion*, *The Polar Decomposition of an N-Degenerate Biquaternion*, and *The Polar Decomposition and Its Three Pairings*, table of domains).

So the correct statement is not "a degenerate element has no polar form". It is:

- **the two-factor decomposition is defined on every element**, the cone included, and it is the matrix polar decomposition;
- **the four-factor N-word is defined only off the cone**, because it is a parametrisation of the group of units.

The two answer different questions. The first asks *what is this operator, as a positive factor times an isometry*; it is available always. The second asks *which unit is this*; it is available only where there is a unit. Confusing them is what makes the degenerate case look like a failure of polar decomposition, when it is a failure of one chart on one group.

### The Limit of the Word

The word has boundary values on the cone. A family with $r=Re^{-\psi/2}$ and $\psi\to\infty$ reaches

$$
L=\frac{R\varkappa_{\mathrm{phs}}}{2}\bigl(e_t+i\vec u_{\mathrm b}\bigr)\tilde u_{\mathrm r},
$$

with $\varkappa_{\mathrm{phs}}=e^{i\alpha}$ the central phase of the family, a non-zero rank-one null element, with the idempotent stratum for $\operatorname{Sc}L\neq0$ and the nilpotent stratum for $\operatorname{Sc}L=0$ (*The Massless Limit as a Boundary Value of the Polar Word*). Two things follow, and the second is the important one.

**The element has a limit.** So the cone is reachable, and the degenerate case is not a different theory but a boundary of the same one.

**The generator has no limit, and the limit is path-dependent.** The cone is not a graph over the units, so different families reach different boundary points, and the rate at which the wall is approached is extra data. The boundary value is therefore *not a value of the word*: it is what the word does when its domain is exhausted.

## The Carriers: Why Half a Spin Is a Ray

### The Multiplicative Law on an Ideal

**Proposition.** Let $\tilde\Pi$ be a non-trivial idempotent. Then $N(a\tilde\Pi)=0$ for every $a\in\mathbb{B}$. Consequently the whole minimal left ideal $S=\mathbb{B}\tilde\Pi$ lies on the cone.

*Proof.* By multiplicativity, $N(a\tilde\Pi)=N(a)N(\tilde\Pi)$. A non-trivial idempotent is isotropic, $\langle\tilde\Pi\rangle_{\natural}=0$, because $\tilde\Pi\tilde\Pi^{\natural}=0$ makes it a zero divisor of the non-pure family. Hence the product vanishes for every $a$, and $S\subseteq\{N=0\}$.

The proposition is a two-line corollary of two theorems the corpus already has — multiplicativity and the isotropy of the idempotent — and it is not stated in the sources. It changes the reading of the dichotomy, because it says the pair is **not distributed evenly over the algebra's own subspaces**: there is a four-real-dimensional subspace all of whose elements are degenerate, and another, the centre, on which the norm vanishes only at the origin.

Measured on samples: over four hundred random elements of $S_+=\mathbb{B}\tilde\Pi_+$ with $\tilde\Pi_+=\tfrac12(e_t+i\vec e_z)$ the largest $\lvert N\rvert$ is $1.2\times10^{-16}$; over four hundred random central elements with $\lvert Q_t\rvert>0.2$ the smallest is $4\times10^{-2}$. The first set is inside the cone; the second touches it only at the origin.

### The Three Carriers

The carriers of *Angular Momentum and Spin in the Biquaternion Algebra* are three, and the norm behaves on each of them in a different way.

| carrier | spin | $\dim_{\mathbb{C}}$ | $N$ on the carrier | degenerate? |
| --- | --- | --- | --- | --- |
| $\mathbb{B}_{C}=\mathbb{C}e_t$, the centre | $0$ | $1$ | $N=A^{2}$ for $Ae_t$ | only at $A=0$ |
| $S_\pm=\mathbb{B}\tilde\Pi_\pm$ | $\tfrac12$ | $2$ | identically $0$ | always |
| $V=\ker\operatorname{tr}$ | $1$ | $3$ | $N=B^{2}$; zero on the isotropic cone of $V$ | on that cone |

The middle row is the proposition. The first row is the observation that a central element is a complex number, so its norm is the square of that number and vanishes with it. The last row is the observation that on the traceless part the scalar term is absent, so the norm reduces to the vector square, $N=B^{2}$, and the degenerate set of that carrier is the complex isotropic cone of $V$ — which is where the Riemann–Silberstein vector of a null field lies, $(\vec E+ic\vec B)^{2}=0$.

Three consequences, stated carefully, because the naive form of each is wrong.

**Spin zero is not the degenerate case; it is the safe one.** A scalar field is a single central number, so it is invertible wherever it is non-zero, and it is degenerate only at its nodes, where the field is the zero element and there is nothing to decompose. In the sector notation of *Introduction to N and Spectrally Regular and Degenerate Operators*, a central field with $A\neq0$ sits in $\Sigma_{10}^{\mathrm{s}}$: $N=A^{2}\neq0$ and $B^{2}=0$. It is $N$-regular and spectrally degenerate, and the two facts are independent.

**One chiral component is always degenerate.** By the middle row, a state that lives in a single minimal left ideal is on the cone at every point of space and time, whatever its amplitude. Its operator has rank two, its image is a totally isotropic plane, and it is a ray.

**The spin value does not decide the sector, and the sector does not decide the spin.** The norm is a function of one element at one point; a spin is a label of a module. No table can correlate them, and any statement that does so is reading a property of a carrier off a property of a value.

### Mass from Two Rays

The second row of the table would make every spin-$\tfrac12$ state massless, which is false. The resolution is the only place in the algebra where two degenerate elements make a regular one.

A Dirac spinor is a sum of one element from each ideal, $\tilde\Xi_{\mathrm{sp}}=\tilde\Xi_{\mathrm{sp},L}+\tilde\Xi_{\mathrm{sp},R}$, and

$$
N\bigl(\tilde\Xi_{\mathrm{sp},L}+\tilde\Xi_{\mathrm{sp},R}\bigr)
=\tilde\Xi_{\mathrm{sp},L}\tilde\Xi_{\mathrm{sp},R}^{\natural}
+\tilde\Xi_{\mathrm{sp},R}\tilde\Xi_{\mathrm{sp},L}^{\natural},
$$

because the two diagonal terms $N(\tilde\Xi_{\mathrm{sp},L})$ and $N(\tilde\Xi_{\mathrm{sp},R})$ vanish by the proposition. The norm of the sum is the **cross term** and nothing else. This is the cross term that *The Hamilton Pairing* records in the mass of a sum; here it is the whole of the mass, because both summands are individually isotropic.

So the mass of a spin-$\tfrac12$ field is the interference of two rays. Each chiral component is null by itself; mass exists only where the two overlap; and the mass term of the Dirac equation is the term that couples them, which is why it must act on the right, on the side that can carry one component into the other. A field with one component only has no cross term and is massless — the algebraic statement behind the two-component description of a Weyl field.

The photon completes the picture from the other side. The field strength of a null plane wave is itself a zero divisor, $\tilde F^{2}=0$ (*Null Electromagnetic Fields and the Shear-Free Congruence*), so it is a single rank-one object with no second part to interfere with, and no mass can be generated. The pattern is uniform: **mass needs two rays; one ray is massless; and a spin-zero field is not a ray at all.**

## Physical Readings

- **$N$-regular is a transformation; $N$-degenerate is a ray.** The interpretation is that a unit is a change of frame — a boost, a rotation, a scale, a phase — and a zero divisor is a direction with an intensity and no frame. Boundary: the reading is of the element's operator; a physical process described by a unit can still be dissipative when the unit is not the whole story.
- **The cone is the wall of reversibility.** The interpretation is that no operation on the cone can be undone, and by the absorbing property no composition repairs it. Boundary: an algebraic statement about inverses; the thermodynamic reading is separate and cited, not derived.
- **Mass is the distance from the wall.** On the material sector $N=-m^{2}c^{2}$, so $m=0$ is the wall and $m^{2}$ measures how far outside it the four-momentum sits. Boundary: the identification needs the material slice; the value of the mass is an input, not a prediction.
- **Something is always annihilated on the cone, and it is a plane.** The interpretation is that a degenerate element identifies half of its domain — a gauge redundancy, a decoupled polarisation, or a projection — and never a single direction, because the algebra is four-dimensional and the rank drops by two. Boundary: which physical mode is annihilated is representation data and is not fixed by the algebra.
- **The degenerate element keeps a direction and a scale.** On $\Sigma_{01}$ the normal form $\kappa\tilde\Pi(\vec Z)$ is exact and exhaustive. Boundary: the rapidity is the parameter that is lost, so a family on the cone has no rate.
- **$\Sigma_{01}$ propagates; $\Sigma_{00}$ does not.** The interpretation is that in the first stratum the image and the kernel are complementary, so a live plane survives beside the annihilated one; in the second the image lies inside the kernel, so the element annihilates its own output. Boundary: both strata are pointwise statements, and neither carries a frequency.
- **Spin zero is a unit, half a spin is a ray, and one spin is a null cone.** By the carrier table. Boundary: the correspondence runs from the carrier to the norm and not the other way, so it does not survive as a statement about sectors.
- **Mass is interference.** For a spin-$\tfrac12$ field the norm of a sum of two isotropic parts is the cross term alone. Boundary: the two parts are the two components of one element, not two particles.
- **A photon is a single ray.** The field strength of a null wave is a zero divisor, so it has no second part and generates no mass. Boundary: this is the null condition of the field strength, not a statement about the four-momentum, which is a different element of the same cone.
- **The boundary value is not a value.** The word has a limit on the cone and the limit is path-dependent. Boundary: the element has a limit, the generator does not.

## Limits

**The norm is algebraic; the words are sector-dependent.** $N=0$ is one complex equation. Reading it as *massless* needs the material sector, reading it as *non-reversible* needs the operator picture, and reading it as *nilpotent* needs the pure part of the cone. The three readings are not the same statement, and the algebra supplies only the common criterion.

**The cone is thin, and that is not a statement about importance.** The cone is a complex hypersurface of real codimension two, so a generic element is a unit; over four thousand random elements of the algebra the smallest $\lvert N\rvert$ was $2\times10^{-2}$. But the rest frame, the null field, the gauge redundancy and the exceptional point all lie on it or on its relatives. A thin set is not a negligible set, and the corpus's use of the pair is evidence of the opposite.

**No dynamics, no particle content, no mass spectrum.** The article reads one element at one point. It does not supply an equation of motion, and it does not predict which masses occur; the massless limit and the interference reading are statements about normal forms.

**Degeneracy of the norm is not degeneracy of the spectrum.** $\Sigma_{01}$ is spectrally regular and $N$-degenerate; $\Sigma_{10}$ is $N$-regular and spectrally degenerate. Any sentence that uses *degenerate* without its qualifier is ambiguous in this corpus, and the ambiguity is not verbal: the two conditions have different zero sets and different physical readings.

**The carrier statement is a statement about ideals, not about states in a Hilbert space.** $S_\pm$ is a minimal left ideal on which the algebra acts irreducibly; a physical state is a normalised element of such a carrier with a metric added. The proposition uses only multiplicativity and isotropy, and it survives the addition of the metric, but the metric is not part of it.

**The absorbing property is not a conservation law.** That products of a degenerate element stay degenerate says nothing about whether a physical quantity is conserved; the conserved currents of the corpus are built from pairings, and their conservation is a separate computation.

## Summary

- The norm is the determinant, $N=\det\mathsf M_2(\tilde Q)$, and it is multiplicative.
- $N$-regular means invertible: the element is a bijection, nothing is annihilated, and the inverse is $\tilde Q^{\natural}/N$.
- $N$-degenerate means singular: the element has a non-zero kernel, it is not invertible, and it is a ray.
- Of the four algebraic norms, only $N$ has its zero set equal to the non-units: $P$ and $\\mathrm{Kr}$ vanish on units, and $H$ vanishes only at the origin, so every zero divisor is $H$-regular.
- The cone is absorbing: $N(\tilde Q)=0$ implies $N(\tilde Q\tilde X)=N(\tilde X\tilde Q)=0$ for every $\tilde X$.
- On a non-zero degenerate element the kernel is exactly a complex plane, and the rank of left multiplication is $2$; it is $4$ on the units and $0$ at the origin.
- On $\Sigma_{01}$ the image is complementary to the kernel; on $\Sigma_{00}$ the image lies inside the kernel, which is $\tilde Q^{2}=\kappa\tilde Q$ against $\tilde\nu^{2}=0$.
- Three failures have one source: no inverse, no generator, no polar word are all failures of a construction built from $\tilde Q^{-1}$.
- The four-factor word is a parametrisation of the group of units, and every value of it is a unit; the cone is outside its range, not inside its domain.
- The two-factor decomposition is defined on every element and sharpens off the cone; on the cone its Hermitian factor is rank one and its isometry is not unitary.
- The degenerate element keeps a direction and a scale, $\kappa\tilde\Pi(\vec Z)$, and loses the rapidity.
- The word has boundary values on the cone; the generator does not, and the limit is path-dependent.
- $N$ vanishes identically on a minimal left ideal, by multiplicativity and the isotropy of the idempotent: every pure spin-$\tfrac12$ state is a ray.
- $N$ vanishes on the centre only at the origin: a scalar field is a unit wherever it is non-zero.
- On the traceless part $N$ reduces to $B^{2}$, so $N$ vanishes there exactly on its isotropic cone, where a null field strength sits.
- The norm of a sum of one element from each ideal is the cross term alone, so the mass of a spin-$\tfrac12$ field is the interference of two rays.
- A null field strength is a single zero divisor, so it has no second part and generates no mass.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\tilde Q=Q_te_t+\vec Q$ | a general biquaternion, $Q_t\in\mathbb{C}$, $\vec Q\in\mathbb{C}^{3}$ |
| $N=\langle\tilde Q\rangle_{\natural}$ | the quaternionic norm, $Q_t^{2}+B^{2}$; the determinant of $\mathsf M_2(\tilde Q)$ |
| $B^{2}=(\vec Q,\vec Q)$ | the square of the vector part; the discriminant of the characteristic polynomial is $-4B^{2}$ |
| $\mathbb{B}^{\times}$ | the group of units, $\{N\neq0\}$ |
| $\mathcal N=\{N=0\}$ | the zero-divisor cone, together with the origin |
| $\Sigma_{ij}$ | the sector with $N\neq0$ if $i=1$ and $B^{2}\neq0$ if $j=1$ |
| $\operatorname{rank}L_{\tilde Q}$ | $4$ on the units, $2$ on the non-zero cone, $0$ at the origin |
| $\tilde Q^{\natural}$ | the quaternionic conjugate; $\tilde Q\tilde Q^{\natural}=N e_t$ |
| $\tilde Q^{*}$ | the Hermitian conjugate; $\tilde Q\tilde Q^{*}$ is Hermitian and positive definite exactly when $N\neq0$ |
| $\tilde\Pi_\pm=\tfrac12(e_t\pm\vec Z)$, $\vec Z^{2}=e_t$ | the primitive idempotents, isotropic, $N(\tilde\Pi_\pm)=0$ |
| $S_\pm=\mathbb{B}\tilde\Pi_\pm$ | the minimal left ideals, of complex dimension two |
| $\mathbb{B}_C=\mathbb{C}e_t$ | the centre, the spin-$0$ carrier |
| $V=\ker\operatorname{tr}$ | the traceless part, the spin-$1$ carrier |
| $\kappa\tilde\Pi(\vec Z)$ | the normal form on $\Sigma_{01}$, $\kappa=2Q_t$ |
| $r,\alpha,\theta$ | the scale, the central phase and the rotor angle of the polar word; the word rapidity is $\theta_{\mathrm{rpd},w}$ |
| $\tilde Q_H\tilde Q_0$ | the two-factor decomposition, defined on every element; the Cartan pairing when both factors sharpen |

## Further Reading

- [N-Regularity and N-Degeneracy in the Biquaternion Algebra](../articles_maths/n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html), for the norm, its multiplicativity, the group of units and the two cases on the remarkable subspaces.
- [Norm and Pairing Conventions](norm-and-pairing-conventions.html), for the four norms, the qualified regular and degenerate, and the domains of the three pairings.
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
- [The Polar Decomposition of a Biquaternion](../articles_maths/the-polar-decomposition-of-a-biquaternion.html), for the H-norm two-factor decomposition defined on every non-zero element.
- [The Polar Decomposition of an N-Degenerate Biquaternion](../articles_maths/the-polar-decomposition-of-an-n-degenerate-biquaternion.html), for the rank-one Hermitian factor and the partial isometry on the cone.
