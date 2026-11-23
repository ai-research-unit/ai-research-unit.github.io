# __Mass in Motion: The Region of Both Invariants__

## Introduction

This entry reads the second of the five parts of the tenth section: the open stratum on which both predicates hold.

$$
\Sigma_{11}=\{N\neq0,\ B^{2}\neq0\},\qquad N=Q_t^{2}+B^{2},\qquad B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2}.
$$

The predicates are the ones the partition entry named. The norm $N$ asks whether the element has an invariant magnitude. The vector square $B^{2}$ asks whether its two eigenvalues are separated. On this stratum both answers are yes, and it is the only stratum on which both are yes. The other three strata are the walls, and the entries that follow this one read them.

The first claim is that this is the only stratum on which the phrase *two modes* is a statement about the element and not about an approximation. The spectral decomposition $\tilde Q=\lambda_+e_++\lambda_-e_-$ has two terms here, both coefficients non-zero, both idempotents non-trivial, and the writing is unique. Everywhere else in the algebra one of those four properties fails. So the two-mode picture is exact on this stratum and degenerate off it.

The second claim is that the region carries more than its spectrum. The spectrum fixes the trace and the norm and nothing else. The direction of the vector part is a second datum, and it is carried by the eigenprojections. An element of the region is a spectrum together with a frame, and the two are not interchangeable.

The third claim is that on the material sector the spectrum is the Doppler pair of one four-momentum. The two eigenvalues are the two light-cone frequencies of one momentum, multiplied by $i$. Their sum, difference, product and ratio are the energy, the momentum, the mass and the rapidity. Four kinematic quantities are four readings of one pair.

The fourth claim is that the region is inverse-closed and not product-closed, and that its wall $B^{2}=0$ is reached from inside by exactly one boost. The product of two elements of the region can land on the wall, and so can a boost. The boost that reaches it is the one that takes the particle to its rest frame. **The wall is therefore not an obstruction to motion; it is where motion stops.**

The fifth claim is that mass is not additive. The region is not closed under addition, and it does not need to be: the sum of two null momenta is null when the two are parallel and lies in the region otherwise. A system of two massless parts can carry a mass, and the mass belongs to the sum and to neither part.

The interpretation labels continue the section's sequence. The partition entry carries I.10.a to I.10.l, and this entry carries I.10.m to I.10.x, so that no label of the section is used twice and a reader who follows the section in order meets them in one sequence.

Nothing below is a model of a particle. The region is cut on the algebra by two equations, and each name comes from the part of it that matter reaches. The mass shell is a reading of $N$, the momentum is a reading of $B^{2}$, and §*The Limits* states what neither reading carries.

## The Source Table

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| the definition, the five descriptions, the geometry, the elements, the eigenbasis and the corners, the spinor spaces, the multiplication and inversion, the relation to the two cones | [The N-Regular, Spectrally Regular Sector](../articles_maths/the-n-regular-spectrally-regular-sector.html) |
| the characteristic polynomial, the eigenvalues, the spectral idempotents, the two-term writing | [The Biquaternion Eigenvalue Decomposition](../articles_maths/the-biquaternion-eigenvalue-decomposition.html) |
| the existence and uniqueness of the eigenbasis, the normalisation, the transverse construction | [The Eigenbasis of a Spectrally Regular Biquaternion](../articles_maths/the-eigenbasis-of-a-spectrally-regular-biquaternion.html) |
| the Peirce corners, the special decomposition and the corner generators | [The Peirce Decomposition of the Biquaternion Algebra](../articles_maths/the-peirce-decomposition-of-the-biquaternion-algebra.html) |
| the minimal left ideals, the polarized module, the two Peirce copies | [The Polarized Module of the Biquaternion Algebra](../articles_maths/the-polarized-module-of-the-biquaternion-algebra.html) |
| the multiplicative norm, the group of invertibles and the null cone | [N-Regularity and N-Degeneracy in the Biquaternion Algebra](../articles_maths/n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html) |
| the spectral criterion, the eigenvalues and the spectral-degenerate cone | [The Spectrum](../articles_maths/the-spectrum-of-a-biquaternion.html) |
| the two predicates, the independence of the cones, the chain of invariants | [Relations between the N Norm and Spectral Regularity and Degeneracy](../articles_maths/relations-between-the-n-norm-and-spectral-regularity-and-degeneracy.html) |
| the modulus, the unit factor and the three pairings of the complete polar decomposition | [The Complete Polar Decomposition of an N-Regular Biquaternion](../articles_maths/the-complete-polar-decomposition-of-an-n-regular-biquaternion.html) |
| the rank of left multiplication, the annihilators and the two-sided operator | [The Four General Products and Their Relations over the Biquaternion Algebra](../articles_maths/the-four-general-products-and-their-relations-over-the-biquaternion-algebra.html) |
| the scalar line and the Jordan part, which are the wall $B^{2}=0$ | [The N-Regular, Spectrally Degenerate Sector](../articles_maths/the-n-regular-spectrally-degenerate-sector.html) |
| the scaled idempotents, which are the wall $N=0$ | [The N-Degenerate, Spectrally Regular Sector](../articles_maths/the-n-degenerate-spectrally-regular-sector.html) |

The first row owns everything structural. The region is a particularisation of the sector article, and this entry does not reprove its theorems: it states them, computes the witnesses, and reads them. The rows after the first supply the three decompositions the entry uses — the spectral writing, the eigenbasis with its corners, and the polar word — and the two wall articles, which are cited only where a product or a boost crosses.

## The Results in Brief

### The Region

The region is the complement of the union of two cones.

$$
\Sigma_{11}=\mathbb{B}\setminus(\mathcal N\cup\mathcal S),\qquad
\mathcal N=\{N=0\},\qquad
\mathcal S=\{B^{2}=0\}.
$$

It is open and dense in $\mathbb{B}$, of complex dimension four and real dimension eight. Its complement is a complex hypersurface of real codimension two and of Lebesgue measure zero. The region is connected and it is not simply connected.

A hundred random draws with complex normal coefficients gave a hundred elements of the region. No draw landed on either cone. That is the numerical form of the statement that the union of two complex hypersurfaces has measure zero: a random element is invertible with two separated eigenvalues, and a degenerate element has to be arranged.

The identity is not in the region. $e_t$ has $B^{2}=0$, so it lies on the spectral wall. **The region contains no subgroup, because every subgroup contains the identity.** It is a symmetric subset of the group of invertibles and not a subgroup.

### The Spectrum and the Two Terms

The characteristic polynomial is squarefree on the region.

$$
p_{\tilde Q}(X)=X^{2}-2Q_tX+N(\tilde Q),\qquad
\operatorname{disc}p_{\tilde Q}=-4B^{2}\neq0,\qquad
\lambda_\pm=Q_t\pm iB,\qquad
\lambda_+\lambda_-=N\neq0.
$$

The two eigenvalues are distinct and non-zero. The spectral idempotents are unique,

$$
e_\pm=\frac{\tilde Q-\lambda_\mp e_t}{\lambda_\pm-\lambda_\mp},\qquad
\tilde Q=\lambda_+e_++\lambda_-e_-,
$$

and both coefficients are non-zero. In terms of the spectrum,

$$
N=\lambda_+\lambda_-,\qquad
B^{2}=-\left(\frac{\lambda_+-\lambda_-}{2}\right)^{2},\qquad
2Q_t=\lambda_++\lambda_-.
$$

So the two invariants are the two elementary symmetric functions of the pair: the product and minus a quarter of the squared difference. Both terms $\lambda_\pm e_\pm$ are null, because $N(e_\pm)=0$, and neither is zero.

### The Eigenbasis

Every element of the region carries a Peirce basis in which its own left multiplication is diagonal. With a fixed square root $B$ of $B^{2}$,

$$
\vec U=\frac{\vec Q}{B},\qquad
\vec{Ζ}=-i\vec U,\qquad
\tilde\Pi_{\mathrm{id},\pm}=\frac{e_t\pm\vec{Ζ}}{2},\qquad
\vec{Ζ}^{2}=e_t,
$$

and a pair of nilpotents $\vec\Pi_{\mathrm{nil},\pm}$ in the two mixed corners with

$$
\vec\Pi_{\mathrm{nil},+}\vec\Pi_{\mathrm{nil},-}=\tilde\Pi_{\mathrm{id},-},\qquad
\vec\Pi_{\mathrm{nil},-}\vec\Pi_{\mathrm{nil},+}=\tilde\Pi_{\mathrm{id},+},\qquad
\vec\Pi_{\mathrm{nil},\pm}^{2}=0.
$$

The four elements $(\tilde\Pi_{\mathrm{id},+},\vec\Pi_{\mathrm{nil},-},\vec\Pi_{\mathrm{nil},+},\tilde\Pi_{\mathrm{id},-})$ are a basis of $\mathbb{B}$, and

$$
\tilde Q\tilde\Pi_{\mathrm{id},+}=\lambda_+\tilde\Pi_{\mathrm{id},+},\quad
\tilde Q\vec\Pi_{\mathrm{nil},-}=\lambda_+\vec\Pi_{\mathrm{nil},-},\quad
\tilde Q\vec\Pi_{\mathrm{nil},+}=\lambda_-\vec\Pi_{\mathrm{nil},+},\quad
\tilde Q\tilde\Pi_{\mathrm{id},-}=\lambda_-\tilde\Pi_{\mathrm{id},-},
$$

so the matrix of left multiplication is $\operatorname{diag}(\lambda_+,\lambda_+,\lambda_-,\lambda_-)$. The same basis gives the right multiplication as $\operatorname{diag}(\lambda_+,\lambda_-,\lambda_+,\lambda_-)$.

The basis depends on the element. Its root $\vec{Ζ}$ is built from $\vec Q$, and the corners and the ideals move with it. The pair of nilpotents is unique up to the reciprocal rescaling $\vec\Pi_{\mathrm{nil},+}\mapsto\mu\vec\Pi_{\mathrm{nil},+}$, $\vec\Pi_{\mathrm{nil},-}\mapsto\mu^{-1}\vec\Pi_{\mathrm{nil},-}$, and a normalisation removes that freedom.

### The Two Spinor Spaces

The two minimal left ideals are the two spinor spaces, and each carries both eigenvalues.

$$
S_+=\mathbb{B}\tilde\Pi_{\mathrm{id},+}=\mathbb{C}\tilde\Pi_{\mathrm{id},+}\oplus\mathbb{C}\vec\Pi_{\mathrm{nil},+},\qquad
S_-=\mathbb{B}\tilde\Pi_{\mathrm{id},-}=\mathbb{C}\vec\Pi_{\mathrm{nil},-}\oplus\mathbb{C}\tilde\Pi_{\mathrm{id},-},\qquad
\mathbb{B}=S_+\oplus S_-.
$$

Each is a complex plane. On each, left multiplication by $\tilde Q$ is $\operatorname{diag}(\lambda_+,\lambda_-)$: a spinor of either copy carries both modes. The scalar action is on the right: $R_{\tilde Q}$ is $\lambda_+$ on $S_+$ and $\lambda_-$ on $S_-$. That right eigenvalue is the Peirce index, and it is what distinguishes the two copies.

### Products and Inverses

The norm is multiplicative, so a product of two elements of the region is invertible.

$$
N(\tilde Q_2\tilde Q)=N(\tilde Q_2)N(\tilde Q)\neq0,
\qquad
\Sigma_{11}\cdot\Sigma_{11}\subseteq\Sigma_{10}\cup\Sigma_{11}.
$$

Both outcomes occur. Two witnesses, both checked by hand:

$$
(e_t+\vec e_x)^{2}=2\vec e_x\in\Sigma_{11},\qquad
(e_t+2\vec e_x)(e_t-2\vec e_x)=5e_t\in\Sigma_{10}.
$$

Squaring separates the two cases by one condition.

$$
B^{2}(\tilde Q^{2})=4Q_t^{2}B^{2}(\tilde Q),
\qquad
\tilde Q^{2}\in\Sigma_{11}\iff Q_t\neq0,\qquad
\tilde Q^{2}=-B^{2}(\tilde Q)\,e_t\iff Q_t=0.
$$

The inverse stays in the region.

$$
\tilde Q^{-1}=\frac{\tilde Q^{\natural}}{N},\qquad
N(\tilde Q^{-1})=\frac{1}{N},\qquad
B^{2}(\tilde Q^{-1})=\frac{B^{2}(\tilde Q)}{N^{2}}.
$$

**So the region is inverse-closed and not product-closed, and it is not a subgroup.**

### The Material Face

On the material sector the chart is a four-momentum.

$$
\tilde P_\Phi=i\frac{E}{c}e_t+\vec p,\qquad
N=-\frac{E^{2}}{c^{2}}+\lvert\vec p\rvert^{2},\qquad
B^{2}=\lvert\vec p\rvert^{2}.
$$

The material part of the region is $\{\vec r\neq0,\ \lvert\vec r\rvert\neq\lvert q'_t\rvert\}$ in the coordinates $\tilde Q=iq'_te_t+\vec r$, and the spectrum is

$$
\lambda_\pm=i\left(\frac{E}{c}\pm\lvert\vec p\rvert\right)=i\,mc\,e^{\pm\theta_{\mathrm{rpd}}},
\qquad
\cosh\theta_{\mathrm{rpd}}=\frac{E}{mc^{2}}.
$$

A boost preserves $N$ and moves $B^{2}$. Over nine rapidities the norm was preserved to $9\times10^{-16}$ while $B^{2}$ ran from $0.0022$ to $110.3$. At the single rapidity $\theta=\operatorname{artanh}(\lvert\vec p\rvert c/E)$ the momentum vanishes and $B^{2}$ vanishes with it: the boost lands on the wall.

The sum of two null momenta is in the region unless the two are parallel.

$$
N(\tilde P_1+\tilde P_2)=-2E_1E_2\left(1-\cos\theta\right).
$$

One hundred random pairs reproduced the formula to $1.4\times10^{-14}$, and every sum had $B^{2}>0$ and $N<0$. Parallel rays sum to a null element, equal-energy antiparallel rays sum to a scalar multiple of $e_t$, and every other pair sums to an element of the region.

## The Region

### Dimension and Complement

The region is the complement of one hypersurface.

$$
\Sigma_{11}=\{\tilde Q:\ \langle\tilde Q\rangle_{\natural}\,B^{2}(\tilde Q)\neq0\},
\qquad
\dim_{\mathbb C}\Sigma_{11}=4,\qquad
\dim_{\mathbb R}\Sigma_{11}=8.
$$

The product $\langle\tilde Q\rangle_{\natural}B^{2}$ is a single polynomial of degree four in the four complex coordinates, and it vanishes exactly on the union of the two cones. So the complement of the region is a complex hypersurface: complex dimension three, real dimension six, real codimension two, measure zero. The region is Zariski-open and dense.

The dimension count is the first asymmetry between the four strata. The region has real dimension eight, the two mixed strata have six, and the doubly degenerate stratum has four. The partition entry stated these numbers; what matters here is their consequence. **A stratum of codimension two does not separate**: a path can pass from the region to the other side, but it does so at an isolated parameter value, and that value is where one of the two invariants vanishes. A stratum of codimension one would separate the algebra into two halves; these do not.

Two of the five descriptions of the region are worth restating in the language of this entry. An element of the region is invertible whose two eigenvalues are distinct; and it is the only kind of element that admits a spectral decomposition into two non-trivial idempotents with distinct non-zero coefficients. The second description is the algebraic form of the phrase *two modes*, and the other three strata are where it fails: no unit, no separation, or a vanishing coefficient.

### The Eigenvalue Parametrisation

The region is the image of a parameter space, and the parametrisation is unique.

$$
\tilde Q=\lambda_+e_++\lambda_-e_-,\qquad
\lambda_\pm\in\mathbb{C}^{\times},\quad
\lambda_+\neq\lambda_-,\quad
e_+^{2}=e_+,\quad e_+\neq0,e_t.
$$

Every element of the region has exactly one such writing, and every choice of the data gives an element of the region. The parameter space is a pair of non-zero complex numbers off the diagonal, together with a non-trivial idempotent.

The non-trivial idempotents form a quadric. They are $e_+=(e_t+\vec{Ζ})/2$ with $\vec{Ζ}^{2}=e_t$ and $\vec{Ζ}\neq\pm e_t$: a smooth connected complex surface with two points removed. That surface is the home of the direction of $\vec Q$, and it is why the region has four real dimensions more than its spectrum.

The parametrisation is not a group chart. The map $\tilde Q\mapsto(\lambda_+,\lambda_-)$ is surjective onto $\mathbb{C}^{\times}\times\mathbb{C}^{\times}$ minus the diagonal, it is not injective, and it is not a homomorphism. Products do not add or multiply eigenvalues in any coordinatewise way: the eigenvalues of a product are not determined by the eigenvalues of its factors. Only the product of the two eigenvalues is determined, and it is the norm.

### Connected and Not Simply Connected

The region is connected. It is the continuous image of a connected parameter space: the pair $(\lambda_+,\lambda_-)$ ranges over a complement of three complex lines, which is connected, and the idempotent ranges over a connected surface with two points removed.

It is not simply connected, and the loop that shows it is the axis turning once.

$$
\tilde Q(t)=e_t+\varepsilon e^{2\pi it}\vec e_x,\qquad 0\le t\le1,\qquad \varepsilon\neq0.
$$

The invariants along the loop are

$$
N(\tilde Q(t))=1+\varepsilon^{2}e^{4\pi it},\qquad
B^{2}(\tilde Q(t))=\varepsilon^{2}e^{4\pi it},
$$

neither of which vanishes. So the loop lies in the region. Its image under the invariant map winds twice around $1$ and twice around $0$, so it is not null-homotopic in the torus $\mathbb{C}^{\times}\times\mathbb{C}^{\times}$, and therefore not null-homotopic in the region.

The reading is that the invariants are quadratic in the element, so a turn of the vector part is a double turn of the invariants. $B^{2}$ is a square, and one turn of $\vec Q$ winds it twice around zero. A loop of winding two around the origin is not contractible in $\mathbb{C}^{\times}$, and that is the whole obstruction: the region fails to be simply connected because its invariants are squares, not because of any group acting on it.

### What the Region Excludes

Three exclusions, each by one equation.

| excluded object | equation | where it lives | why it is out |
| --- | --- | --- | --- |
| the scalar line $\mathbb{C}^{\times}e_t$ | $B^{2}=0$ | the spectral wall | its two eigenvalues coincide |
| the Jordan elements $Q_tu$, $u$ non-trivial unipotent | $B^{2}=0$ | the spectral wall | no eigenbasis exists |
| the scaled idempotents $c\tilde\Pi_{\mathrm{id}}$ | $N=0$ | the null wall | not invertible |

The identity is the first case. $e_t$ is a scalar, so its vector part is zero and the two eigenvalues coincide at $1$. A region that excluded the identity is a region of *changes*, and this is the algebraic reason the region is a symmetric subset and not a subgroup.

The second case is the one that matters for the two-mode picture. A non-trivial unipotent $u=e_t+\vec\Pi_{\mathrm{nil}}$ with $\vec\Pi_{\mathrm{nil}}^{2}=0$ has the double eigenvalue $1$ and the minimal polynomial $(X-1)^{2}$: it has one eigenvalue and no eigenbasis. It is invertible, and it is on the wall.

## The Spectrum and the Two Terms

### The Invariants as Symmetric Functions

The spectrum determines the two invariants and nothing more.

$$
N=\lambda_+\lambda_-,\qquad
B^{2}=-\frac{(\lambda_+-\lambda_-)^{2}}{4},\qquad
Q_t=\frac{\lambda_++\lambda_-}{2}.
$$

These are the three elementary symmetric functions of a two-element multiset, written in the algebra's variables: the product, minus a quarter of the discriminant, and half the trace. The region is exactly the set where the first is non-zero and the second is non-zero.

The square of the difference is what the two-mode picture measures. $B^{2}$ is not the difference; it is minus a quarter of its square. The square is why the sign of $B^{2}$ carries no information about the ordering of the two eigenvalues: exchanging them changes the sign of $\lambda_+-\lambda_-$ and leaves $B^{2}$ alone. The unordered pair is the datum, and $B$ is one of the two square roots of $B^{2}$.

The sign of $N$ is a second reading of the same region. $N=Q_t^{2}+B^{2}$ is a sum of two complex squares, and on the real slice of each it is a difference of two positive numbers. So the region splits into a part where the norm is negative, a part where it is positive, and a part where it is non-real. The material face of §*The Material Face* is where all three occur.

### Two Null Terms

Each term of the spectral decomposition is null.

$$
N(\lambda_+e_+)=\lambda_+^{2}N(e_+)=0,\qquad
N(\lambda_-e_-)=\lambda_-^{2}N(e_-)=0,
$$

because an idempotent has the eigenvalues $1$ and $0$, hence vanishing characteristic constant, hence vanishing norm. Both coefficients are non-zero and both idempotents are non-trivial, so neither term is zero.

Over a hundred elements the identities held to $3\times10^{-15}$:

$$
N(e_+)=N(e_-)=N(\lambda_+e_+)=N(\lambda_-e_-)=0,
\qquad
2Q_t=\lambda_++\lambda_-,\qquad
N=\lambda_+\lambda_-.
$$

So the region is the stratum on which one element is a sum of two null elements and of nothing else. That is the precise content of the phrase *two modes*: two null components, added. It is not a decomposition into two independent objects, because their coefficients are tied by the trace and their product is tied by the norm.

### The Fibre of the Spectrum

The spectrum is a projection with a four-dimensional fibre.

$$
\{\tilde Q\}\longrightarrow(\lambda_+,\lambda_-),\qquad
\dim_{\mathbb R}(\text{fibre})=4.
$$

The fibre over a pair of distinct non-zero eigenvalues is the set $\{\lambda_+e_++\lambda_-e_-\ :\ e_+\ \text{non-trivial idempotent}\}$, which is the idempotent quadric, of four real dimensions. Two elements with the same spectrum differ by the choice of $e_+$, and that choice is the direction of the vector part.

The fibre is a frame and not a degeneracy. Nothing in the fibre is redundant: each idempotent gives a different element. The spectrum is what a boost can change or preserve; the fibre is what a rotation moves. A rotation acts on the fibre and fixes the spectrum exactly, because the eigenvalues depend on $\vec Q$ only through $\vec Q^{2}$.

The physical reading of the fibre is the direction of motion. On the material sector the idempotents $e_\pm$ are the two null directions along $\vec p$. The spectrum fixes the two frequencies and the fibre fixes where the momentum points. A particle with a given energy and a given momentum magnitude can move in any direction, and those are different elements of the region with the same spectrum.

## The Eigenbasis

### The Root and the Idempotents

The root carried by the element is its own normalised vector part.

$$
\vec U=\frac{\vec Q}{B},\qquad
\vec{Ζ}=-i\vec U=-\frac{i\vec Q}{B},\qquad
\vec{Ζ}^{2}=e_t,\qquad
\tilde\Pi_{\mathrm{id},\pm}=\frac{e_t\pm\vec{Ζ}}{2}.
$$

Then $\tilde\Pi_{\mathrm{id},\pm}^{2}=\tilde\Pi_{\mathrm{id},\pm}$, $\tilde\Pi_{\mathrm{id},+}\tilde\Pi_{\mathrm{id},-}=0$, $\tilde\Pi_{\mathrm{id},++}\tilde\Pi_{\mathrm{id},-}=e_t$, and

$$
\tilde Q=\lambda_+\tilde\Pi_{\mathrm{id},++}\lambda_-\tilde\Pi_{\mathrm{id},-},\qquad
\vec{Ζ}\tilde\Pi_{\mathrm{id},\pm}=\tilde\Pi_{\mathrm{id},\pm}\vec{Ζ}=\pm\tilde\Pi_{\mathrm{id},\pm}.
$$

The pair $\tilde\Pi_{\mathrm{id},\pm}$ is the pair $e_\pm$ of §*The Spectrum and the Two Terms*; the two notations are the same idempotents, and the entry uses $\tilde\Pi_{\mathrm{id}}$ where the corner structure is in play.

This is the corner rule in one line. An element of the corner $\mathbb{B}_{st}=\tilde\Pi_{\mathrm{id},s}\mathbb{B}\tilde\Pi_{\mathrm{id},t}$ is multiplied on the left by $Q_t+i\,sB$ and on the right by $Q_t+i\,tB$. So the four corners carry two independent signs, and the four diagonal values of $L_{\tilde Q}$ and of $R_{\tilde Q}$ are those signs evaluated.

The other square root exchanges the labels. Replacing $B$ by $-B$ sends $\vec{Ζ}$ to $-\vec{Ζ}$, exchanges $\tilde\Pi_{\mathrm{id},+}$ and $\tilde\Pi_{\mathrm{id},-}$, and exchanges the two eigenvalues. The unordered pair of idempotents and the unordered spectrum are unchanged. Nothing in the entry depends on the choice, and the entries that follow make it once and keep it.

### The Corners and the Two Nilpotents

The mixed corners are square-zero, and each is one complex line.

$$
x\in\mathbb{B}_{st},\ s\neq t\ \Longrightarrow\ \operatorname{Sc}x=0,\quad x^{2}=0,
$$

because $x^{2}\in\tilde\Pi_{\mathrm{id},s}\mathbb{B}\tilde\Pi_{\mathrm{id},t}\tilde\Pi_{\mathrm{id},s}\mathbb{B}\tilde\Pi_{\mathrm{id},t}=0$. So the two off-diagonal corners hold nilpotents and only nilpotents.

The pair is forced. Choose a non-zero $\vec\Pi_{\mathrm{nil},+}\in\mathbb{B}_{-+}$. Left multiplication by it is a non-zero linear map from the line $\mathbb{B}_{+-}$ to the line $\mathbb{C}\tilde\Pi_{\mathrm{id},-}$, hence an isomorphism, so there is a unique $\vec\Pi_{\mathrm{nil},-}\in\mathbb{B}_{+-}$ with $\vec\Pi_{\mathrm{nil},+}\vec\Pi_{\mathrm{nil},-}=\tilde\Pi_{\mathrm{id},-}$. The other product is then forced to be $\tilde\Pi_{\mathrm{id},+}$: it lies in the line $\mathbb{C}\tilde\Pi_{\mathrm{id},+}$, say $\vec\Pi_{\mathrm{nil},-}\vec\Pi_{\mathrm{nil},+}=\alpha\tilde\Pi_{\mathrm{id},+}$, and $\vec\Pi_{\mathrm{nil},+}=\tilde\Pi_{\mathrm{id},-}\vec\Pi_{\mathrm{nil},+}=\vec\Pi_{\mathrm{nil},+}(\vec\Pi_{\mathrm{nil},-}\vec\Pi_{\mathrm{nil},+})=\alpha\vec\Pi_{\mathrm{nil},+}$ forces $\alpha=1$. Hence

$$
\vec\Pi_{\mathrm{nil},+}\vec\Pi_{\mathrm{nil},-}=\tilde\Pi_{\mathrm{id},-},\qquad
\vec\Pi_{\mathrm{nil},-}\vec\Pi_{\mathrm{nil},+}=\tilde\Pi_{\mathrm{id},+},\qquad
\vec\Pi_{\mathrm{nil},+}^{2}=\vec\Pi_{\mathrm{nil},-}^{2}=0.
$$

The two ideals are spanned by the corners.

$$
S_+=\mathbb{B}\tilde\Pi_{\mathrm{id},+}=\mathbb{C}\tilde\Pi_{\mathrm{id},+}\oplus\mathbb{C}\vec\Pi_{\mathrm{nil},+},\qquad
S_-=\mathbb{B}\tilde\Pi_{\mathrm{id},-}=\mathbb{C}\vec\Pi_{\mathrm{nil},-}\oplus\mathbb{C}\tilde\Pi_{\mathrm{id},-}.
$$

So the index of a nilpotent is fixed by the *left* ideal it generates and not by the corner it sits in: $\vec\Pi_{\mathrm{nil},+}$ sits in $\mathbb{B}_{-+}$ and generates $S_+$ together with $\tilde\Pi_{\mathrm{id},+}$. That is the single most easily misread point in the construction, and it is the reason §*The Two Spinor Spaces* states the left and right actions separately.

Over a hundred elements the corner identities held to $2\times10^{-15}$, with the pair built from a random transverse vector and normalised as in the next subsection.

### The Two Normalisations

The pair is fixed up to one rescaling.

$$
\vec\Pi_{\mathrm{nil},+}\longmapsto\mu\vec\Pi_{\mathrm{nil},+},\qquad
\vec\Pi_{\mathrm{nil},-}\longmapsto\mu^{-1}\vec\Pi_{\mathrm{nil},-},\qquad
\mu\in\mathbb{C}^{\times},
$$

which preserves both products and both squares. No other freedom exists, because the mixed corners are lines. The construction from $\vec\Pi_{\mathrm{nil},+}$ alone makes one choice and determines the rest; the rescaling appears only when the pair is parametrised by two arbitrary generators.

A transverse vector gives an explicit pair. For a pure $\vec X$ with $\vec X_\perp^{2}\neq0$, where $\vec X_\perp=\vec X-(\vec X\cdot\vec Q)\vec Q/B^{2}$, put

$$
u_+=\tilde\Pi_{\mathrm{id},-}\vec X\tilde\Pi_{\mathrm{id},+},\qquad
u_-=\tilde\Pi_{\mathrm{id},+}\vec X\tilde\Pi_{\mathrm{id},-},\qquad
u_+u_-=\vec X_\perp^{2}\,\tilde\Pi_{\mathrm{id},-},\qquad
u_-u_+=\vec X_\perp^{2}\,\tilde\Pi_{\mathrm{id},+} .
$$

Then $\vec\Pi_{\mathrm{nil},\pm}=u_\pm/\sqrt{\vec X_\perp^{2}}$ has the required products and squares. Two choices of $\vec X$ differ by the rescaling.

This is the construction the numerical check used, with $\vec X$ drawn at random and the scalar $\vec X_\perp^{2}$ read off the product. The squares, the cross products, the four diagonal left values and the four diagonal right values all closed to $2\times10^{-15}$.

### The Symmetric Form and Its Exceptional Cone

A closed form exists off one cone.

$$
\vec\Pi_{\mathrm{nil},\pm}=\frac{B\,\vec w-\dfrac{\Sigma}{B}\,\vec Q\pm\dfrac{i}{2}\,[\vec Q,\vec w]}{2\sqrt{\Sigma^{2}-3B^{2}}},
\qquad
\vec w=\vec e_x+\vec e_y+\vec e_z,\qquad
\Sigma=Q_x+Q_y+Q_z .
$$

The vector $\vec w$ is the only non-zero vector fixed by every permutation of the axes, so the formula is symmetric in $x,y,z$: a permutation permutes the three components of $\vec\Pi_{\mathrm{nil},\pm}$ and leaves $B$ and $\Sigma$ unchanged.

The denominator vanishes on a cone, and there the axis charts take over.

$$
\Sigma^{2}=3B^{2}
\iff
(Q_x-Q_y)^{2}+(Q_y-Q_z)^{2}+(Q_z-Q_x)^{2}=0,
$$

which for real $\vec Q$ is the line $Q_x=Q_y=Q_z$. On it,

$$
\vec\Pi_{\mathrm{nil},\pm}=\frac{B\,\vec e_{\imath}-\dfrac{Q_{\imath}}{B}\,\vec Q\pm\dfrac{i}{2}\,[\vec Q,\vec e_{\imath}]}{2\sqrt{Q_{\imath}^{2}-B^{2}}},
\qquad \mu\in\{x,y,z\},
$$

and at least one of the three charts is defined whenever $B\neq0$. The charts are the transverse construction with $\vec X=\vec e_{\imath}$.

The exceptional cone is not the spectral cone. It is not $B^{2}=0$ and it is not $N=0$; it is the locus where the symmetric auxiliary vector $\vec w$ becomes parallel to $\vec Q$. It is a defect of the formula, not of the object: the pair exists everywhere on the region, and the chart is what changes.

### Why No Formula Is Axis-Free

No closed form for the pair can avoid an auxiliary direction.

A map $F$ rational in $\vec Q$ and $B$, natural under rotations, would satisfy $F(S\vec Q)=S\,F(\vec Q)$ for every rotation $S$. By invariant theory the only such maps are $F(\vec Q)=f(B^{2})\vec Q$: the invariant tensors are $\delta_{ij}$ and $\epsilon_{ijk}$, and $\epsilon$ cannot build a vector from one vector. But the corner line is transverse to $\vec Q$, so such an $F$ would vanish, and the pair would be zero everywhere.

So every explicit generator uses an auxiliary vector. The symmetric formula uses the permutation-invariant $\vec w$; the axis charts use $\vec e_x,\vec e_y,\vec e_z$. The auxiliary vector is not a datum of the element and not a choice of the physicist: it is what a spinor line costs. A corner line is a spinor, and a spinor is not a function of the momentum alone.

This is the mathematical content behind a familiar physical fact. A frame that diagonalises a momentum cannot be built from the momentum alone; it needs one more direction. In the algebra the extra direction is free, and the freedom is exactly the reciprocal rescaling. The reading is stated as I.10.u.

### What Depends on the Element

The eigenbasis data are attached to $\tilde Q$ and are not canonical.

| object | depends on $\tilde Q$? |
| --- | --- |
| the root $\vec{Ζ}$ and the idempotents $\tilde\Pi_{\mathrm{id},\pm}$ | yes |
| the corner lines $\mathbb{B}_{+-},\mathbb{B}_{-+}$ as subspaces | yes |
| the ideals $S_\pm=\mathbb{B}\tilde\Pi_{\mathrm{id},\pm}$ | yes |
| the pair $(\vec\Pi_{\mathrm{nil},+},\vec\Pi_{\mathrm{nil},-})$ | yes, through the root; the residual scale is the normalisation |
| the diagonal values $(\lambda_+,\lambda_-)$ | yes |
| the Peirce coordinates of a second element | yes |

The eigenbasis coincides with the standard Peirce basis exactly on one locus. The standard pair is the one attached to the fixed root $i\vec e_z$; it agrees with the element's own pair, up to the reciprocal rescaling, exactly when $\vec Q$ is parallel to $\vec e_z$, that is when $Q_x=Q_y=0$. Everywhere else the two bases differ.

The dependence is not a defect of the construction. It is the statement that the region has no canonical frame: each element carries its own, and comparing the frames of two elements is a change of basis. §*The Two Spinor Spaces* shows that this change is precisely what the matrix model with respect to the basis does.

## The Two Spinor Spaces

### The Two Columns

Each minimal left ideal is a complex plane, and the algebra is their direct sum. In the eigenbasis,

$$
\mathcal{B}=(\tilde\Pi_{\mathrm{id},+},\vec\Pi_{\mathrm{nil},-},\vec\Pi_{\mathrm{nil},+},\tilde\Pi_{\mathrm{id},-}),
\qquad
\tilde\Pi_{\mathrm{id},+}\mapsto E_{11},\quad
\vec\Pi_{\mathrm{nil},-}\mapsto E_{12},\quad
\vec\Pi_{\mathrm{nil},+}\mapsto E_{21},\quad
\tilde\Pi_{\mathrm{id},-}\mapsto E_{22},
$$

every element has one expansion

$$
\tilde Q_2=Q_{2,11}\tilde\Pi_{\mathrm{id},++Q}_{2,12}\vec\Pi_{\mathrm{nil},-+Q}_{2,21}\vec\Pi_{\mathrm{nil},++Q}_{2,22}\tilde\Pi_{\mathrm{id},-},
$$

and the matrix $\mathsf M_2^{Q}(\tilde Q_2)=(Q_{2,ij})$ has the two ideals as its two columns. The element itself has

$$
\mathsf M_2^{Q}(\tilde Q)=\begin{pmatrix}\lambda_+&0\\0&\lambda_-\end{pmatrix}.
$$

So a general element is a pair of spinors and not a spinor. Its first column is a spinor of the first Peirce copy, its second column a spinor of the second, and each is a complex plane of two components. The algebra is the direct sum of the two, and no element of the region is confined to one.

### The Peirce Index

Left multiplication carries both eigenvalues on each ideal; right multiplication is scalar on each.

$$
L_{\tilde Q}\big|_{S_+}=L_{\tilde Q}\big|_{S_-}=\operatorname{diag}(\lambda_+,\lambda_-),
\qquad
R_{\tilde Q}\big|_{S_+}=\lambda_+,\qquad
R_{\tilde Q}\big|_{S_-}=\lambda_- .
$$

This asymmetry is the whole content of the Peirce index. A spinor of either copy has two components, and the left action mixes neither: it scales the first component by $\lambda_+$ and the second by $\lambda_-$. The two ideals are distinguished by the right action alone, which scales each ideal by one eigenvalue.

The two ideals are isomorphic as left modules. Right multiplication by $\vec\Pi_{\mathrm{nil},-}$ maps $S_+$ onto $S_-$, with inverse right multiplication by $\vec\Pi_{\mathrm{nil},+}$. So there is one simple module here, and the two copies are two embeddings of it. The label *first* versus *second* is a label of the embedding, fixed by the choice $\tilde\Pi_{\mathrm{id},+}=(e_t+\vec{Ζ})/2$.

The numerical check of these four statements closed to $2\times10^{-15}$ over a hundred elements: the diagonal left values on all four basis elements, the diagonal right values, and the action on a random spinor of $S_+$.

## Products and the Boundary

### The Product Law on the Region

The region is a subset of the group of invertibles, and the group of invertibles is the union of the region and the spectral wall.

$$
\mathbb{B}^{\times}=\Sigma_{11}\sqcup\Sigma_{10},\qquad
\Sigma_{11}\cdot\Sigma_{11}\subseteq\Sigma_{10}\cup\Sigma_{11}.
$$

The inclusion follows from multiplicativity of the norm alone. That both outcomes occur is a fact about the vector parts: the product of two vector parts can be a scalar.

Two witnesses, one for each outcome.

$$
(e_t+\vec e_x)^{2}=e_t+2\vec e_x+\vec e_x^{2}=2\vec e_x,\qquad
N=4,\quad B^{2}=4,
$$

which stays in the region; and

$$
(e_t+2\vec e_x)(e_t-2\vec e_x)=e_t-4\vec e_x^{2}=5e_t,\qquad
N=25,\quad B^{2}=0,
$$

which lands on the scalar line.

The second witness is the algebraic form of a cancellation. The two factors have opposite vector parts of equal magnitude, and their product is a pure scalar. The two modes have merged. So a product of two two-mode elements can be a one-mode element, and the region is not closed under composition.

### Squaring

Squaring doubles the spectral angle, and the two modes meet exactly when the trace vanishes.

$$
B^{2}(\tilde Q^{2})=4Q_t^{2}B^{2}(\tilde Q),
\qquad
\tilde Q^{2}=\lambda_+^{2}e_++\lambda_-^{2}e_-.
$$

The identity was checked to $3\times10^{-14}$ over a hundred elements. It says that squaring leaves the region exactly when the scalar part is non-zero, and that when the scalar part vanishes the square is a scalar:

$$
Q_t=0\ \Longrightarrow\ \lambda_-=-\lambda_+,\quad
\lambda_+^{2}=\lambda_-^{2}=-B^{2},\quad
\tilde Q^{2}=-B^{2}e_t .
$$

The witness is the simplest pure vector.

$$
(\vec e_x+\vec e_y)^{2}=\vec e_x^{2}+\vec e_x\vec e_y+\vec e_y\vec e_x+\vec e_y^{2}=-2e_t .
$$

The geometric statement is that the eigenvalue map is a squaring. The square of the pair $(\lambda_+,\lambda_-)$ is $(\lambda_+^{2},\lambda_-^{2})$, and the two squares coincide exactly when the two eigenvalues are opposite, which is $Q_t=0$. So the loss of a mode under squaring is an antipodal condition, not a magnitude condition: it does not matter how large the eigenvalues are, only that they point in opposite directions.

### Inversion

Inversion is a symmetry of the region.

$$
\tilde Q^{-1}=\lambda_+^{-1}e_++\lambda_-^{-1}e_-=\frac{\tilde Q^{\natural}}{N},
\qquad
N(\tilde Q^{-1})=N^{-1},\qquad
B^{2}(\tilde Q^{-1})=\frac{B^{2}}{N^{2}}.
$$

The second identity was checked to $5\times10^{-15}$ over a hundred elements. The inverse has the same two modes and the same idempotents, with the eigenvalues inverted; its spectrum is the reciprocal pair. So inversion acts on the spectrum and fixes the frame.

The region is symmetric and not a subgroup. It is closed under inversion, it excludes the identity, and it contains no subgroup. This is the precise algebraic form of the statement that the region is a set of *changes*: every element has an inverse in the region, the product of the two is the identity, and the identity is on the wall. So the region is closed under reversal and open under composition: the product of an element with its inverse is exactly the element that the region excludes.

## The Material Face

### The Four-Momentum Chart

The material sector is the chart in which the region reads as kinematics. With

$$
\tilde P_\Phi=i\frac{E}{c}e_t+\vec p,\qquad
E\in\mathbb{R},\quad\vec p\in\mathbb{R}^{3},
$$

the two invariants are

$$
N=-\frac{E^{2}}{c^{2}}+\lvert\vec p\rvert^{2},\qquad
B^{2}=\lvert\vec p\rvert^{2}\ge0 .
$$

So the material part of the region is

$$
\Sigma_{11}\cap\mathbb{B}_{\Phi}=\left\{\vec p\neq0,\ \lvert\vec p\rvert\neq\frac{\lvert E\rvert}{c}\right\},
$$

which is the material sector minus its two walls: the rest point $\vec p=0$ and the light cone $\lvert\vec p\rvert=\lvert E\rvert/c$.

The chart was checked on a hundred random real pairs $(E,\vec p)$. The membership rule agreed with the two predicates on all hundred, and the two walls were the only failures.

The region is not a causal class. It contains the timelike momenta $\lvert\vec p\rvert<\lvert E\rvert/c$ and the spacelike momenta $\lvert\vec p\rvert>\lvert E\rvert/c$, and they differ only in the sign of $N$. The name *mass in motion* describes the first; the second is in the same region, with an imaginary mass, $mc=\sqrt{-N}$, and a real polar scale $\varrho=\lvert N\rvert^{1/2}$, which on that branch is a proper length and not a mass.

### The Doppler Pair

The two eigenvalues are the two light-cone frequencies of one momentum.

$$
\lambda_\pm=i\left(\frac{E}{c}\pm\lvert\vec p\rvert\right)=i\,mc\,e^{\pm\theta_{\mathrm{rpd}}},
\qquad
\cosh\theta_{\mathrm{rpd}}=\frac{E}{mc^{2}},\qquad
\sinh\theta_{\mathrm{rpd}}=\frac{\lvert\vec p\rvert}{mc}.
$$

The four elementary readings of the pair are then

$$
\lambda_++\lambda_-=2i\frac{E}{c},\qquad
\lambda_+-\lambda_-=2i\lvert\vec p\rvert,\qquad
\lambda_+\lambda_-=-m^{2}c^{2},\qquad
\frac{\lambda_+}{\lambda_-}=e^{2\theta_{\mathrm{rpd}}}.
$$

The first two are the kinematics and the third is the invariant. The sum of the two frequencies is twice the energy, their difference is twice the momentum, and their product is minus the mass squared. The ratio is the square of the Doppler factor, which is why the pair is called the Doppler pair: the two eigenvalues are what one frequency becomes when it is read in the two null directions of the momentum.

The fourth reading is the coupling between the first three. A rapidity is a boost parameter, and it appears here as a ratio of eigenvalues. A boost preserves the product and shifts the logarithm of the ratio by twice the rapidity; that is rapidity addition, and it is a statement about the spectral pair and not about a coordinate transformation.

### The Causal Sign

The sign of $N$ separates the two branches of the region on the material sector.

| branch | condition | eigenvalues | mass $mc=\sqrt{-N}$ | reading |
| --- | --- | --- | --- | --- |
| timelike | $\lvert\vec p\rvert<\lvert E\rvert/c$ | both on the same imaginary half | real $mc>0$ | a massive particle in motion |
| light | $\lvert\vec p\rvert=\lvert E\rvert/c$ | one eigenvalue zero | $mc=0$ | the wall, not the region |
| spacelike | $\lvert\vec p\rvert>\lvert E\rvert/c$ | on opposite imaginary halves | imaginary $mc$ | a spacelike momentum |

One real letter, two readings, and the branch chooses. On the spacelike branch $\varrho\,e^{i\theta_{\mathrm{pha}}}=\sqrt N$ is real and positive, and $\varrho=\lvert N\rvert^{1/2}$ is a proper length; on the timelike branch $\varrho\,e^{i\theta_{\mathrm{pha}}}=imc$ is purely imaginary and $\varrho=mc$. The mass column above is $mc=\sqrt{-N}$, which is the reading the causal sign gives and not the modulus of the polar word.

The two branches are the same spectral type. Both have $N\neq0$ and $B^{2}\neq0$, both have two distinct eigenvalues, and both admit the two-term writing. The difference is the position of the eigenvalues on the imaginary axis and the sign of $N$.

The branch cannot be changed inside the real material sector without crossing the wall. A path from a timelike momentum to a spacelike one has $\lvert\vec p\rvert=\lvert E\rvert/c$ somewhere, and there $N=0$. In the complex algebra the two branches are connected, and the path passes through complex momenta; on the real chart they are two halves of one region separated by a wall.

### The Boost Reaches the Wall Once

A boost preserves the norm and moves the vector square.

$$
N(L\tilde P L^{*})=N(\tilde P),\qquad
B^{2}(L\tilde P L^{*})\neq B^{2}(\tilde P)\ \text{in general},
$$

for a boost rotor $L=\cosh\frac{\theta}{2}+i\sinh\frac{\theta}{2}\vec u$. Over nine rapidities from $-2$ to $2$, applied to the momentum with the energy in units of $mc^2$ and the momentum in units of $mc$, $E=1.6$ and $\lvert\vec p\rvert=1.249$, the norm was preserved to $9\times10^{-16}$ and $B^{2}$ ran from $0.0022$ to $110.3$.

At one rapidity the vector part vanishes.

$$
\theta_{\mathrm{rest}}=\operatorname{artanh}\frac{\lvert\vec p\rvert c}{E},
\qquad
B^{2}\bigl(L(\theta_{\mathrm{rest}})\tilde P L(\theta_{\mathrm{rest}})^{*}\bigr)=0 .
$$

At that value the computed momentum was $0$ to machine precision, the computed energy was $1.0000000000$, and the norm was unchanged. So the boost lands exactly on the wall, and on the scalar part of it.

This is the precise sense in which the wall is the rest frame. The wall is not an obstruction that a motion cannot reach; it is the endpoint of the boost that removes the motion. A particle in motion is in the region, its rest frame is on the wall, and the passage between them is a boost. The region is open, so the passage is a limit and not a jump: for every rapidity other than $\theta_{\mathrm{rest}}$ the element is still in the region.

The invariance statement is therefore a two-part statement. The norm is Lorentz-invariant and the vector square is not. The first is the mass; the second is the magnitude of the momentum, which is frame-dependent and vanishes at exactly one rapidity. So the mass shell survives every boost, and the two-mode splitting survives every boost except the one that reaches the wall.

### The Sum of Two Null Momenta

Two null momenta sum to a momentum whose invariant mass is the pairing.

$$
\tilde P_1=iE_1+E_1\vec n_1,\qquad
\tilde P_2=iE_2+E_2\vec n_2,\qquad
\lvert\vec n_1\rvert=\lvert\vec n_2\rvert=1,
$$

$$
N(\tilde P_1+\tilde P_2)=-\left(E_1+E_2\right)^{2}+\lvert E_1\vec n_1+E_2\vec n_2\rvert^{2}
=-2E_1E_2\left(1-\cos\theta\right),
$$

with $\theta$ the angle between the two directions. One hundred random pairs reproduced the formula to $1.4\times10^{-14}$.

The three cases are exhaustive.

| angle | $N$ | $B^{2}$ | stratum |
| --- | --- | --- | --- |
| $\theta=0$, parallel | $0$ | $\left(E_1+E_2\right)^{2}$ | the null wall $\Sigma_{01}$ |
| $\theta=\pi$ and $E_1=E_2$ | $-4E_1E_2$ | $0$ | the spectral wall $\Sigma_{10}$ |
| $0<\theta<\pi$ otherwise | $<0$ | $>0$ | the region $\Sigma_{11}$ |

All hundred random sums had $B^{2}>0$ and $N<0$, with $N$ between $-73.6$ and $-5\times10^{-4}$; the smallest magnitude occurred at the smallest angle.

The mass of the sum is not the sum of the masses. Neither addend has a mass, and the sum has the mass

$$
m^{2}c^{4}=2E_1E_2\left(1-\cos\theta\right),
$$

which is the invariant mass of the pair. At fixed energies it is largest for antiparallel directions, and it vanishes for parallel rays. So a region element with a mass can be built by adding two wall elements with no mass, and the mass belongs to the addition.

## The Polar Word and the Flow

The region is the domain of the polar word. With the modulus

$$
\varrho\,e^{i\theta_{\mathrm{pha}}}=\sqrt{N}\neq0,\qquad
\tilde Q=\varrho\,e^{i\theta_{\mathrm{pha}}}\,\tilde Q_1,\qquad N(\tilde Q_1)=1,
$$

every element of the region has a unique writing

$$
\tilde Q=\varrho\,e^{i\theta_{\mathrm{pha}}}\,\tilde U_{\Psi,\mathrm b}\,\tilde u_{\mathrm r},
$$

with $\varrho=\lvert N\rvert^{1/2}$, a central phase, a Hermitian boost and a real rotor. The check $N(\tilde Q/(\varrho\,e^{i\theta_{\mathrm{pha}}}))=1$ closed to $1\times10^{-15}$ over a hundred elements.

The region is the only stratum on which both decompositions exist. On $\Sigma_{01}$ the modulus vanishes and the polar word fails while the spectral decomposition survives. On $\Sigma_{10}$ the modulus survives and the spectral decomposition fails, either outright on the Jordan part or by becoming a one-term non-unique writing on the scalar line. The region is where an element has both a spectrum and a frame.

The flow generated by an element is unitary exactly on the material sector.

$$
\tilde X\longmapsto e^{\theta\tilde Q},\qquad
\langle e^{\theta\tilde Q}\rangle_{*}=\operatorname{Sc}\left(e^{\theta\tilde Q}e^{\theta\tilde Q^{*}}\right).
$$

For a material element, $\tilde Q^{*}=-\tilde Q$, so the flow is $*$-unitary and the Hermitian norm is constant. Measured over the parameter range $0\le\theta\le3$: for the material element $i\,1.3e_t+0.2\vec e_x+0.6\vec e_y-0.4\vec e_z$ the norm had spread $7\times10^{-16}$; for the complex element $0.3+0.2i$ on $e_t$ and complex vector part the norm grew by a factor $302$.

The general formula is a growth law.

$$
\langle e^{\theta\tilde Q}\rangle_{*}=\lvert e^{\theta Q_t}\rvert^{2}\left(\lvert\cos B\theta\rvert^{2}+\lvert\sin B\theta\rvert^{2}\,\lVert\vec U\rVert^{2}\right),
\qquad
\lVert\vec U\rVert^{2}\ge1,
$$

with equality exactly when $\vec U$ is real, that is when the element is normal, $\tilde Q\tilde Q^{*}=\tilde Q^{*}\tilde Q$. The computed $\lVert\vec U\rVert^{2}$ was $1.000000$ for a real axis and $1.305085$ for a complex one.

So the region contains both a conservative flow and a growing one. The cut is not between timelike and spacelike, and it is not between small and large: it is between the elements that lie in the material sector and the elements that do not. A generic element of the region has complex eigenvalues and a growing norm, and that growth is the algebraic form of a mode that is not a pure oscillation.

## The Reach of the Three Carriers

Only one of the three carriers reaches the region, and the two exclusions are structural.

| carrier | dimension | invariant on it | intersection with the region |
| --- | --- | --- | --- |
| the centre $\mathbb{C}e_t$ | $2$ real | $B^{2}=0$ at every point | empty |
| the ideals $S_\pm=\mathbb{B}\tilde\Pi_{\mathrm{id},\pm}$ | $4$ real | $N=0$ at every point | empty |
| the material sector $\mathbb{B}_{\Phi}$ | $4$ real | both vary | open dense in the sector |

The centre is excluded by its vector part. Every element of the centre is a scalar, so $B^{2}=0$ identically. No choice of the complex coefficient changes that, and no product inside the centre leaves it.

The ideals are excluded by their rank. Every element of $S_\pm$ is a product with a rank-one idempotent, so it has rank at most one as a matrix, so its determinant vanishes, and the determinant is the norm.

The material sector reaches the region, and inside it the region is everything but two walls. It is the only carrier of the three whose members can have a non-zero norm and a non-zero vector part at once.

The two exclusions are not statements that a scalar field or a spinor field cannot be massive. They are statements about a single value. An amplitude has no direction, so it cannot carry $B^{2}\neq0$, and its momentum is a separate element. A single spinor value is null, and a field value is not a single spinor value: the algebra is the sum $S_+\oplus S_-$, and the norm of a sum of two null elements is the pairing,

$$
N(\tilde\Xi_L+\tilde\Xi_R)=2\langle\tilde\Xi_L,\tilde\Xi_R\rangle
\qquad\text{when }N(\tilde\Xi_L)=N(\tilde\Xi_R)=0,
$$

which is non-zero in general. So the mass of a spinor field is in the sum and in neither summand. That is the same structure as §*The Material Face*: the region is reached by an addition.

## The Interpretations

### I.10.m — The Two Eigenvalues Are the Two Light-Cone Frequencies

Read: the spectrum $\{\lambda_+,\lambda_-\}$ on the material sector, with $\lambda_\pm=i(E/c\pm\lvert\vec p\rvert)$.

One momentum has two light-cone frequencies. A momentum with energy $E$ and magnitude $\lvert\vec p\rvert$ is crossed by two null directions, and the two frequencies $E/c+\lvert\vec p\rvert$ and $E/c-\lvert\vec p\rvert$ are the Doppler-shifted readings of one frequency in those two directions. The algebra produces exactly this pair, multiplied by $i$, and it produces nothing else: the pair is the whole spectrum.

The interpretation is that the region's spectrum is relativistic kinematics and not a model of it. Sum, difference, product and ratio are energy, momentum, mass and rapidity. There is no free parameter: once the element is given, all four numbers are fixed, and the four relations between them are the ones special relativity requires.

The pair is frame-dependent and the product is not. A boost multiplies both eigenvalues by a common factor and preserves their product. That is the algebraic statement that the mass is invariant and the two frequencies are not, and it needs no transformation law beyond the multiplication of the algebra.

The boundary. The identification uses the material chart. In the full algebra the eigenvalues are complex numbers with no frequency reading, and the names are readings of $N$ and $B^{2}$.

### I.10.n — Two Null Terms Are Not Two Particles

Read: $\tilde Q=\lambda_+e_++\lambda_-e_-$ with $N(e_\pm)=0$ and both coefficients non-zero.

Each term is null and neither term is an object. The term $\lambda_+e_+$ has vanishing norm, so if it were a particle it would be a massless one. But the two terms are tied: their coefficients are fixed by the trace and their product by the norm, so they cannot be varied independently. A two-particle reading would need two independent mass-shell conditions; the region has one.

The interpretation is that the two-term writing is a decomposition of one momentum into two null directions, not a partition of one object into two. The null directions are the two light-cone directions of the same momentum, and the coefficients are the two Doppler factors. Adding them returns the element; that is what a decomposition means.

A count of terms is not a count of particles. The number of terms is two on the region, one on the scalar line, one on the null wall, and none on the nilpotent wall. If terms were particles, the particle number would change under a boost, since a boost can reach the wall. It does not.

The boundary. The reading forbids a two-particle interpretation of the spectral writing. It does not forbid a two-particle state: a state is an element of a module, and the module is not the algebra.

### I.10.o — The Spectrum Is the Kinematics; the Fibre Is the Frame

Read: the projection $\tilde Q\mapsto(\lambda_+,\lambda_-)$ with a four-real-dimensional fibre.

The spectrum does not determine the element. Two elements with the same spectrum differ by the choice of the eigenprojections, and that choice is the direction of $\vec Q$. A hundred elements can share one spectrum.

The interpretation is that a kinematic state is a spectrum together with a frame, and the frame is not derivable from the spectrum. The mass and the two frequencies are numbers; the direction is a point of a quadric. Physics states this as the difference between a momentum magnitude and a momentum direction, and the algebra states it as the difference between the eigenvalue pair and the idempotent.

The fibre is acted on by the rotations and fixed by the boosts. A rotation moves $\vec Q$ and preserves $\vec Q^{2}$, so it moves the fibre and fixes the spectrum. A boost moves both. That is the algebraic split between the two kinds of Lorentz transformation, and it is visible on the region alone.

The boundary. The fibre is not a gauge orbit. Its points are distinct elements of the algebra, not descriptions of one element, and no quotient by rotations is taken here.

### I.10.p — The Mass Is the Product and the Energy Is the Sum

Read: $N=\lambda_+\lambda_-$ and $2Q_t=\lambda_++\lambda_-$ on the material chart.

The two invariants of the spectral pair are the two invariants of the momentum. The product of the eigenvalues is minus the mass squared, and their sum is twice the energy over $c$. So the mass and the energy are not two independent inputs that the algebra then combines: they are the product and the sum of one pair, and the pair is the element.

The interpretation is that the mass is the geometric mean of the two frequencies and the energy is their arithmetic mean. With $\lambda_\pm=i\omega_\pm$ and $\omega_\pm=E/c\pm\lvert\vec p\rvert$, the product is $-\omega_+\omega_-=-m^{2}c^{2}$ and the sum is $2E/c$. The mass is the geometric mean of the two light-cone frequencies, and the energy is their arithmetic mean. On the timelike branch the two frequencies are positive, and the inequality $mc^{2}\le E$ is then the arithmetic–geometric mean inequality: it is strict exactly when the two frequencies differ, that is when $\vec p\neq0$.

The inequality is the reason the wall is the rest frame. Equality in the mean inequality holds exactly when the two frequencies coincide, which is $\vec p=0$, which is $B^{2}=0$. So the wall is not an extra condition: it is the equality case of the mean inequality.

The boundary. The means are means of the two eigenvalues and not of two measurements. Nothing here says that a measurement returns one of the two frequencies; the reading is of the element, not of a protocol.

### I.10.q — Motion Is Generic and Rest Is a Wall

Read: $e_t\notin\Sigma_{11}$, so the region contains no subgroup and no identity.

The rest frame is not an element of the region. The rest momentum $imc\,e_t$ is a pure scalar multiple of $e_t$, so $B^{2}=0$, so it is on the wall. The region is the set of momenta with a non-zero spatial part.

The interpretation is that rest is a boundary case of motion and not the base case. A treatment that begins from the rest frame begins on a wall, and the generic element is not the one at rest. That is the opposite of the usual order of exposition, where the rest frame is the simple case and motion is a transformation of it. In the algebra the simple case is the wall, and the generic case has two modes.

The absence of a subgroup is the precise form of the statement. A subgroup would contain the identity, the identity is on the wall, and a wall has no interior. So no set of reversible motions that is closed under composition sits inside the region: every subgroup of the group of invertibles meets the wall. Composition always eventually returns to rest.

The boundary. The word *generic* is algebraic. A physical system can sit at rest by symmetry, and does; the claim is about the structure of the algebra, not about the frequency of rest in nature.

### I.10.r — One Rapidity Reaches the Wall, and It Is the Rest Frame

Read: $N$ is boost-invariant, $B^{2}$ is not, and $B^{2}$ vanishes at $\theta_{\mathrm{rest}}=\operatorname{artanh}(\lvert\vec p\rvert c/E)$.

The region is crossed by boosts and the crossing is a single point. A boost moves the element along a curve of constant $N$, and that curve meets the wall exactly once, at the rapidity that removes the momentum. The measured curve ran from $B^{2}=110.3$ to $B^{2}=0.0022$ over the sampled range, through zero at the rest rapidity.

The interpretation is that the mass shell is the orbit and the wall is one of its points. The set of momenta of a given mass is a boost orbit, the orbit is a three-dimensional hyperboloid, and the rest frame is the vertex. At the vertex the vector part vanishes and the element is a scalar. So the two-mode picture holds everywhere on the shell except at its vertex, and the vertex is reached by a finite boost.

The wall is therefore not a singularity of the motion, only of the description. The boost is defined at $\theta_{\mathrm{rest}}$ and beyond it; it is the two-term writing that fails at that one parameter value, and it fails because the two terms become equal.

The boundary. The statement is about one boost orbit. A general element of the region is not on a material boost orbit, and its vector part can be complex; the reading uses the material chart.

### I.10.s — Mass Is Not Additive

Read: $N(\tilde P_1+\tilde P_2)=-2E_1E_2(1-\cos\theta)$ for two null momenta.

The mass of a sum is not the sum of the masses. Two null momenta have no mass; their sum has the mass $mc^{2}=\sqrt{2E_1E_2(1-\cos\theta)}$, which vanishes only when the two are parallel. So an addition can produce a mass where neither addend had one, and it can destroy a mass when the addends are antiparallel and equal.

The interpretation is that the invariant mass is a property of a system and not of its parts. This is the algebraic form of the statement that the invariant mass of a system of two photons is not zero unless they are collinear. The algebra produces the formula from the norm alone: $N$ is a quadratic form, so $N(X+Y)=N(X)+N(Y)+2\langle X,Y\rangle$, and on the null cone the first two terms vanish and the pairing is all that is left.

The pairing is the mass. The polar form of the norm, evaluated on two null elements, is the invariant mass of their sum. So a mass is a correlation between two massless parts, and no part carries it.

The boundary. The reading is kinematic. It says what the invariant mass of a sum is; it does not say that the two parts interact, and it supplies no cross-section.

### I.10.t — A Spinor Carries Both Modes and the Peirce Index Is the Right Eigenvalue

Read: $L_{\tilde Q}$ is $\operatorname{diag}(\lambda_+,\lambda_-)$ on each $S_\pm$, and $R_{\tilde Q}$ is $\lambda_\pm$ on $S_\pm$.

A spinor is not a mode. Each minimal left ideal is a complex plane, and left multiplication by the element scales its two components by the two different eigenvalues. So one spinor carries both modes. The thing that distinguishes the two ideals is the right action, which scales each ideal by one eigenvalue.

The interpretation is that the two-component structure of a spinor is the two-component structure of the mode space, and the ideal label is a right-handed label. **The index is not the eigenvalue; it is the eigenvalue *of the other action*.** This is why two copies of one module can be distinct subspaces of the algebra while being isomorphic as modules.

The two ideals are not chiralities. They are isomorphic as left modules, exchanged by right multiplication by a nilpotent, and the algebra is their direct sum. A chirality would be a pair of inequivalent modules; here there is one simple module and two embeddings of it.

The boundary. The reading is algebraic. It gives the form of a two-component spinor; it does not give the spin-statistics theorem, and it does not identify the two copies with the two chiral halves of a Dirac field.

### I.10.u — A Mode Basis Is Not a Function of the Momentum

Read: the eigenbasis depends on $\tilde Q$, and no rotation-natural rational formula for its nilpotents exists.

**The frame that diagonalises an element cannot be built from the element alone.** The root $\vec{Ζ}$ is built from $\vec Q$, but the two nilpotents need one more direction: the symmetric formula uses $\vec w$, and the axis charts use $\vec e_{\imath}$. The obstruction is a theorem of invariant theory, not a failure of ingenuity.

The interpretation is that a mode basis is a gauge choice. Two physicists who diagonalise the same momentum with different auxiliary directions get two bases related by the reciprocal rescaling, and nothing in the algebra prefers one. The physical content — the spectrum, the idempotents, the two ideals as subspaces — does not depend on the choice.

The invariance statement is the useful one. The pair is unique up to one complex rescaling, and the normalisation removes it. So the gauge freedom is one complex number, it acts on the two nilpotents reciprocally, and it leaves every product and every square invariant.

The boundary. The freedom is not a physical gauge field. It is a choice of basis inside one element's own frame, and no connection or curvature is attached to it here.

### I.10.v — The Flow Is Unitary Only Where the Element Is Anti-Hermitian

Read: $\tilde Q^{*}=-\tilde Q$ iff $Q_t\in i\mathbb{R}$ and $\vec Q\in\mathbb{R}^{3}$, which is the material sector.

A generic element of the region generates a growing flow. The formula for the Hermitian norm of $e^{\theta\tilde Q}$ has a factor $\lvert e^{\theta Q_t}\rvert^{2}$, which is constant only when the scalar part is purely imaginary, and a second factor that is constant only when the axis $\vec U$ is real. Both conditions together are the material sector. The measured growth over $\theta\in[0,3]$ was a factor $302$.

The interpretation is that mass in motion is a conservative flow, and the region is larger than its conservative part. A material element generates a unitary one-parameter group: the frequencies are real, the norm is preserved, and the motion is reversible in the strong sense. A generic element generates a flow with a gain.

The second factor is a measure of non-normality. $\lVert\vec U\rVert^{2}\ge1$ with equality exactly when the element commutes with its adjoint. So the growth has two independent sources: a scalar part with a real part, and an axis that is not real. The first is a growth of the amplitude; the second is the failure of the eigenbasis to be orthogonal.

The boundary. A growing flow is not a decaying particle. The algebra gives one-parameter groups and their norms; it gives no lifetime, no decay rate and no arrow.

### I.10.w — Squaring Doubles the Angle and Can Merge the Two Modes

Read: $\tilde Q^{2}=\lambda_+^{2}e_++\lambda_-^{2}e_-$ and $B^{2}(\tilde Q^{2})=4Q_t^{2}B^{2}(\tilde Q)$.

Squaring is a map on the spectrum and the identity on the frame. The idempotents are unchanged and the eigenvalues are squared. In the complex plane of the eigenvalues, squaring doubles the argument and squares the modulus.

The interpretation is that the loss of a mode under squaring is an antipodal condition. The two squared eigenvalues coincide exactly when the two eigenvalues are opposite, and that is $Q_t=0$, not $B^{2}=0$ and not smallness. So a square leaves the region when the element is *balanced* — as much weight on one mode as on the other with opposite signs — and not when it is large or small.

The witness is the simplest pure vector. $(\vec e_x+\vec e_y)^{2}=-2e_t$: a vector of norm $-2$ whose square is a scalar. Nothing about the size of $\vec e_x+\vec e_y$ produces this; the two eigenmodes of a pure vector are always opposite, so the square of any pure vector with $B^{2}\neq0$ is a scalar.

The boundary. The statement is about one squaring. It does not say that a physical process squares an element, and the powers $\tilde Q^{n}$ for $n>2$ are not read here.

### I.10.x — Invertible Is Reversible, and the Product Can Leave the Region

Read: the region is inverse-closed, not product-closed, and $\Sigma_{11}\cdot\Sigma_{11}\subseteq\Sigma_{10}\cup\Sigma_{11}$.

Every element of the region has an opposite and a logarithm. The inverse is in the region, the element generates a one-parameter group, and the group is reversible. In this sense the region is the reversible part of the algebra: no element of it has a kernel.

The interpretation is that reversibility is not closed under composition, and that is not a paradox. Two reversible changes can compose into a change that is also reversible — that is the generic case — and they can compose into a change with one mode, which is still invertible. What cannot happen is a composition into a non-invertible element, because the norm is multiplicative and neither factor has a zero norm.

The region's failure to be product-closed is a failure of the two-mode property, not of invertibility. The product always has an inverse; it can lose its second mode. So the wall that a product can reach is $B^{2}=0$ and never $N=0$, and that asymmetry is the content of the theorem.

The boundary. Reversibility here is algebraic invertibility and the existence of a logarithm. It is not thermodynamic reversibility, and nothing in the entry orders the elements in time.

## The Limits

The names need the material chart. *Mass in motion* is the reading of a four-momentum, and a four-momentum is a point of the material sector. On the full complex algebra the region is a spectral type, and the names are readings of $N$ and $B^{2}$.

The two eigenvalues are not two energies. Their sum is twice the energy and their product is minus the mass squared; each of them separately is a frame-dependent null frequency with no independent meaning.

The region contains the spacelike branch. The name describes the timelike branch; a spacelike momentum is in the same region and has an imaginary mass, $mc=\sqrt{-N}$. The region is a spectral type, and the causal class is a second invariant read from the same element.

The spinor reading is algebraic. The two minimal ideals are two embeddings of one module and are not the two chiralities. The reading gives the form of a two-component spinor and stops there.

**No dynamics is supplied.** The entry describes one element at one instant, its spectrum, its frame and the two flows attached to it. **It gives no evolution equation, no mass spectrum and no particle count.**

The numerical checks are checks of identities, not of the reading. Every identity above was verified on at most a hundred elements; the readings are arguments from the identities and stand or fall with them.

## Summary

- $\Sigma_{11}=\{N\neq0,\ B^{2}\neq0\}$ is the complement of two cones: open, dense, connected, not simply connected, of real dimension eight.
- Its elements are invertible with two distinct non-zero eigenvalues $\lambda_\pm=Q_t\pm iB$, and $N=\lambda_+\lambda_-$, $B^{2}=-(\lambda_+-\lambda_-)^{2}/4$.
- The two-term writing $\tilde Q=\lambda_+e_++\lambda_-e_-$ is unique and both terms are null; the region is the only stratum where this holds with two non-zero coefficients.
- The spectrum fixes the invariants and not the element: the fibre is four-dimensional and carries the direction of $\vec Q$.
- The eigenbasis $(\tilde\Pi_{\mathrm{id},+},\vec\Pi_{\mathrm{nil},-},\vec\Pi_{\mathrm{nil},+},\tilde\Pi_{\mathrm{id},-})$ makes left multiplication $\operatorname{diag}(\lambda_+,\lambda_+,\lambda_-,\lambda_-)$ and right multiplication $\operatorname{diag}(\lambda_+,\lambda_-,\lambda_+,\lambda_-)$.
- The pair of nilpotents needs an auxiliary direction, because no rotation-natural rational formula exists; the pair is unique up to one complex rescaling.
- Each minimal left ideal carries both eigenvalues under left multiplication; the Peirce index is the right eigenvalue.
- The region is inverse-closed and not product-closed: a product lands in the region or on the wall $B^{2}=0$, and squaring leaves the region exactly when $Q_t=0$.
- On the material sector the spectrum is the Doppler pair $i\,mc\,e^{\pm\theta_{\mathrm{rpd}}}$; sum, difference, product and ratio are energy, momentum, mass and rapidity.
- A boost preserves $N$ and moves $B^{2}$, and the single rapidity $\operatorname{artanh}(\lvert\vec p\rvert c/E)$ lands the element on the wall: the rest frame is the vertex of the mass shell.
- Two null momenta sum to a region element unless they are parallel, with invariant mass $m^{2}c^{4}=2E_1E_2(1-\cos\theta)$; the mass belongs to the sum.
- The region is the domain of the polar word, and its flow is unitary exactly on the material sector.
- **Only the material sector reaches the region: the centre has $B^{2}=0$ identically and the ideals have $N=0$ identically.**

### What the Reader Should Retain

One element of the region is one spectrum and one frame, and the frame is not a function of the spectrum. The spectrum gives the two frequencies, hence the mass and the energy; the frame gives the direction. A boost changes the first and moves the second, and a rotation changes only the second.

**The two modes are two null components of one element.** They are not two objects: their coefficients are tied by the trace and their product by the norm. A statement about one component is not a statement about the element.

The wall $B^{2}=0$ is the rest frame, and it is reached by one boost. **The region is open, so rest is a limit and not an interior point; and the mass shell is a boost orbit whose vertex is on the wall.**

The mass of a sum is not the sum of the masses. Two massless addends can have a massive sum, and the mass is the pairing of the two null parts.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\Sigma_{11}$ | the region $N\neq0$, $B^{2}\neq0$ |
| $N=Q_t^{2}+B^{2}$ | the norm, the product of the eigenvalues |
| $B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2}$ | the vector square, minus a quarter of the squared spectral difference |
| $\lambda_\pm=Q_t\pm iB$ | the two eigenvalues |
| $B$ | a fixed square root of $B^{2}$ |
| $e_\pm$ | the spectral idempotents |
| $\vec{Ζ}=-i\vec Q/B$ | the root of $e_t$ carried by the element |
| $\tilde\Pi_{\mathrm{id},\pm}=(e_t\pm\vec{Ζ})/2$ | the same idempotents in Peirce notation |
| $\vec\Pi_{\mathrm{nil},\pm}$ | the two corner nilpotents, $\vec\Pi_{\mathrm{nil},+}\vec\Pi_{\mathrm{nil},-}=\tilde\Pi_{\mathrm{id},-}$ |
| $S_\pm=\mathbb{B}\tilde\Pi_{\mathrm{id},\pm}$ | the two minimal left ideals, the spinor spaces |
| $\mathsf M_2^{Q}$ | the matrix of an element in the eigenbasis |
| $\tilde P_\Phi=i\frac{E}{c}e_t+\vec p$ | a material four-momentum |
| $\theta_{\mathrm{rpd}}$ | the rapidity, $\cosh\theta_{\mathrm{rpd}}=E/(mc^{2})$ |
| $\theta_{\mathrm{rest}}$ | the rapidity that carries the momentum to rest |
| $\varrho\,e^{i\theta_{\mathrm{pha}}}=\sqrt{N}$, $\varrho=\lvert N\rvert^{1/2}$ | the modulus of the polar word |
| $\theta_{\mathrm{pha}}$ | the central phase of the polar word |
| $\langle\tilde X\rangle_{*}$ | the Hermitian norm $\operatorname{Sc}(\tilde X\tilde X^{*})$ |
| $\vec U=\vec Q/B$ | the normalised axis |
| $\vec w=\vec e_x+\vec e_y+\vec e_z$ | the permutation-invariant auxiliary vector |

## Further Reading

In this category. [The Partition: Two Invariants and Four Regimes](the-partition-two-invariants-and-four-regimes.html) is the parent entry: it states the two predicates, the four strata, their dimensions and the independence of the two conditions, and this entry reads the open stratum of that table. [The N Norm: Mass, Angle and the Cone](the-n-norm-mass-angle-and-the-cone.html) reads the first predicate alone, and [The Spectrum and the Two Modes](the-spectrum-and-the-two-modes.html) reads the second alone.

The three walls, in the entries that follow. [The Rest Frame and the Exceptional Point](the-rest-frame-and-the-exceptional-point.html) reads the wall $B^{2}=0$. [The Massless Regime](the-massless-regime.html) reads the wall $N=0$, and *The Vacuum and the Nilpotent Ladder* reads their intersection; those two are the entries that follow this one in the menu. They are the complements of this entry, and each of them states as a failure what this entry states as an absence. Until they are written, the archive versions named below carry the same content.

Mathematics. [The N-Regular, Spectrally Regular Sector](../articles_maths/the-n-regular-spectrally-regular-sector.html) is the source; [The Eigenbasis of a Spectrally Regular Biquaternion](../articles_maths/the-eigenbasis-of-a-spectrally-regular-biquaternion.html) owns the construction and the normalisation of the eigenbasis, and [The Peirce Decomposition of the Biquaternion Algebra](../articles_maths/the-peirce-decomposition-of-the-biquaternion-algebra.html) owns the corners.

The sources of this entry. [Four-Vectors and the Interval](four-vectors-and-the-interval.html) owns the four-momentum chart and the frequency pair. [The Exponential and Its Three Pairings](the-exponential-and-its-three-pairings.html) owns the polar word used in §*The Polar Word and the Flow*. [The Rotations, the Boosts and the Groups](../articles_internal/the-rotations-the-boosts-and-the-groups.html) owns the two-sided operator and the boost rotor. [Rotor, Spin, Pair and Carrier: A Survey of the Closure Block](rotor-spin-pair-and-carrier-a-survey-of-the-closure-block.html) owns the reach of the three carriers, which §*The Reach of the Three Carriers* summarises. [Norm and Pairing Conventions](norm-and-pairing-conventions.html) fixes the letters and the inertias.
