# __The Partition: Two Invariants and Four Regimes__

## Introduction

**This entry reads the tenth section of the mathematical category: the two invariants of one element taken together, and the four regimes their two truth values produce.**

**The pair is the norm and the square of the vector part.**

$$
N(\tilde Q)=Q_t^{2}+B^{2},\qquad B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2},\qquad \tilde Q=Q_te_t+\vec Q .
$$

**The norm is the measure of the previous entry.** The vector square is the discriminant of the characteristic polynomial up to a factor $-4$, and it vanishes exactly when the two eigenvalues coincide.

**Each invariant is a yes or a no, so the pair is one of four answers.** The answers are exhaustive and disjoint, because each element has one truth value for each predicate. The four classes are written $\Sigma_{11}$, $\Sigma_{10}$, $\Sigma_{01}$ and $\Sigma_{00}$, with the first index the norm and the second the spectrum.

**The four classes are of unequal size.** The generic class is open and dense, of real dimension eight. Two classes have real dimension six, and one has real dimension four. That is the first sign that the partition is not a partition into four comparable rooms.

**The claim of this entry is that the four answers are the physics and not a classification with labels added afterwards.** The norm asks whether the element has an invariant magnitude and which causal sign it carries. The vector square asks whether the element has two modes or one. On the material sector the first question is the mass and the second is the momentum, and the four regimes are mass in motion, the rest frame, the light ray and the vacuum.

**The second claim is that a regime is a pair of truth values and not a phase.** No regime is a connected component of the algebra, no regime is both open and closed, and the dimensions differ. Nothing passes continuously from one regime to another: every passage crosses a wall, and each wall has real codimension two.

**The third claim is that the two conditions are independent, and that the independence has one exception.** Off the square-zero set the gradients of the two invariants are independent, so the two numbers are separate dials. On the square-zero set the gradients coincide, so at a nilpotent the two dials are one dial.

**The fourth claim is that composition ignores the partition.** Two elements of one regime can compose into another. The computed case is the product of two unipotents, and one complex number, the pairing of the two nilpotent parts, decides whether the product is elliptic, hyperbolic or defective.

**Nothing below is a model of a particle.** The four regimes are cut on the algebra by two equations. Each name comes from the part of its regime that the material sector reaches, and §*The Limits* states what the names do not carry.

## The Source Table

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| the two predicates, the four sectors, the independence of the two cones, the nilpotent intersection and the tangency, the comparison of the sectors, the chain of invariants, the two decompositions, the two operator loci | [Relations between the N Norm and Spectral Regularity and Degeneracy](../articles_maths/relations-between-the-n-norm-and-spectral-regularity-and-degeneracy.html) |
| the product of two unipotent elements, its characteristic polynomial, the criterion, the three regular types, the two computed cases, the image theorem | [The Product of Two Unipotent Elements and Its Spectrum](../articles_maths/the-product-of-two-unipotent-elements-and-its-spectrum.html) |
| the multiplicative norm, the null cone, its two strata, the norm-one group | [N-Regularity and N-Degeneracy in the Biquaternion Algebra](../articles_maths/n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html) |
| the spectral criterion, the characteristic polynomial, the eigenvalues, the spectral-degenerate cone, the similarity classification | [The Spectrum](../articles_maths/the-spectrum.html) |
| the doubly regular sector | [The N-Regular, Spectrally Regular Sector](../articles_maths/the-n-regular-spectrally-regular-sector.html) |
| the scalar line and the Jordan part | [The N-Regular, Spectrally Degenerate Sector](../articles_maths/the-n-regular-spectrally-degenerate-sector.html) |
| the scaled idempotents and the spectrum of a null element | [The N-Degenerate, Spectrally Regular Sector](../articles_maths/the-n-degenerate-spectrally-regular-sector.html) |
| the nilpotent cone, the origin and the ladder | [The N-Degenerate, Spectrally Degenerate Sector](../articles_maths/the-n-degenerate-spectrally-degenerate-sector.html) |
| the eigenbasis, the spectral idempotents and the corners | [The Eigenbasis of a Spectrally Regular Biquaternion](../articles_maths/the-eigenbasis-of-a-spectrally-regular-biquaternion.html) |
| the Jordan basis, the obstruction and the adapted frame | [The Jordan Basis of a Spectrally Degenerate Biquaternion](../articles_maths/the-jordan-basis-of-a-spectrally-degenerate-biquaternion.html) |
| the modulus, the unit factor and the failure of the decomposition at $N=0$ | [The Complete Polar Decomposition of an N-Regular Biquaternion](../articles_maths/the-complete-polar-decomposition-of-an-n-regular-biquaternion.html) |
| the rank of left multiplication, the annihilators and the two-sided operator | [The Four General Products and Their Relations over the Biquaternion Algebra](../articles_maths/the-four-general-products-and-their-relations-over-the-biquaternion-algebra.html) |

**The rows are the entry's order.** The relations article comes first, because it owns the partition, the independence and the three invariants. The unipotent product comes second, because it owns the one theorem about moving between the regimes. The sector articles come third, one row for each regime, because the regime paragraphs of this entry are their summaries and not their proofs.

## The Results in Brief

### The Two Predicates

**The first predicate is $N\neq0$ and the second is $B^{2}\neq0$.**

$$
\Sigma_{11}=\{N\neq0,\ B^{2}\neq0\},\qquad
\Sigma_{10}=\{N\neq0,\ B^{2}=0\},\qquad
\Sigma_{01}=\{N=0,\ B^{2}\neq0\},\qquad
\Sigma_{00}=\{N=0,\ B^{2}=0\}.
$$

**In cone notation the four classes are the four pieces of the arrangement of two cones.** Writing $\mathcal N=\{N=0\}$ for the null cone and $\mathcal S=\{B^{2}=0\}$ for the spectral-degenerate cone,

$$
\Sigma_{11}=\mathbb B\setminus(\mathcal N\cup\mathcal S),\qquad
\Sigma_{10}=\mathcal S\setminus\mathcal N,\qquad
\Sigma_{01}=\mathcal N\setminus\mathcal S,\qquad
\Sigma_{00}=\mathcal N\cap\mathcal S .
$$

**The partition is by truth values, so it is exhaustive by construction and needs no theorem.** What needs a theorem is that the four truth values are four degeneration patterns of one quadratic, and that the two cones have the arrangement stated.

### The Four Regimes

**The characteristic polynomial reads both predicates at once.**

$$
p_{\tilde Q}(X)=X^{2}-2Q_tX+N,\qquad \operatorname{disc}p_{\tilde Q}=-4B^{2},\qquad \lambda_\pm=Q_t\pm iB .
$$

**The norm is the constant term and the vector square is the discriminant.** So $N=0$ is a root at zero and $B^{2}=0$ is a double root, and the four regimes are the four patterns a quadratic can show.

| regime | conditions | spectrum | the element | name |
| --- | --- | --- | --- | --- |
| $\Sigma_{11}$ | $N\neq0$, $B^{2}\neq0$ | two distinct non-zero roots | an invertible element with two modes | mass in motion |
| $\Sigma_{10}$ | $N\neq0$, $B^{2}=0$ | a double non-zero root | an invertible element with one mode | the rest frame and the exceptional point |
| $\Sigma_{01}$ | $N=0$, $B^{2}\neq0$ | two distinct roots, one at zero | a zero divisor with two modes | the light ray |
| $\Sigma_{00}$ | $N=0$, $B^{2}=0$ | a double root at zero | a zero divisor with one mode | the vacuum and the nilpotent ladder |

**The last column is the interpretation and the first four columns are algebra.** The entry argues the passage from one to the other and does not assume it.

### Independence

**Neither cone contains the other, and two witnesses settle it.**

$$
e_t+i\vec e_x\in\Sigma_{01}\quad(N=0,\ B^{2}=-1),\qquad
e_t+\vec e_x+i\vec e_y\in\Sigma_{10}\quad(N=1,\ B^{2}=0).
$$

**The first is null with a full eigenbasis and the second is invertible with none.** The eigenvalues of the first are $0$ and $2$. The minimal polynomial of the second is $(X-1)^{2}$.

**The two conditions are also functionally independent, and that is a statement about gradients.** With coordinates $(Q_t,Q_x,Q_y,Q_z)$,

$$
\vec\nabla_\Phi N=2(Q_t,Q_x,Q_y,Q_z),\qquad \vec\nabla_\Phi B^{2}=2(0,Q_x,Q_y,Q_z),
$$

**and the two are proportional only where $Q_t=0$, or where the vector part vanishes.** So the map $\tilde Q\mapsto(N,B^{2})$ has rank two except on the hyperplane $Q_t=0$ and on the scalar line, and it has rank one on those two sets.

### Where the Walls Meet

**The intersection of the two cones is the set of square-zero elements.**

$$
\mathcal N\cap\mathcal S=\{\tilde Q:\tilde Q^{2}=0\}=\{Q_t=0,\ \vec Q^{2}=0\}.
$$

**On that set, and only there, the two gradients are equal.** The cones are therefore tangent along the nilpotent cone away from the origin, and both are singular at the origin, where the gradients vanish.

**The coincidence is exact and not an accident.** A square-zero element has $Q_t=0$, so the scalar coordinate is absent from both invariants, and the two invariants become the same function of the vector part.

### The Chain of Invariants

**Three invariants separate three different numbers of types.**

| invariant | data | number of types | what the types are |
| --- | --- | --- | --- |
| norm | $N$ | $2$ | the invertibles and the null cone |
| characteristic polynomial | $(2Q_t,N)$ | $4$ | the four regimes |
| minimal polynomial | $m_{\tilde Q}$ | $6$ | the six strata |

**The count is of degeneration patterns and not of values.** The norm forgets the trace, the characteristic polynomial forgets the defect, and the minimal polynomial forgets nothing.

**The six strata are the four regimes with two of them split.** The regime $\Sigma_{10}$ splits into the punctured scalar line and the Jordan part, and the regime $\Sigma_{00}$ splits into the origin and the non-zero nilpotents.

### The Two Decompositions

**One decomposition follows the discriminant and the other follows the norm.**

| stratum | two-term spectral decomposition | modulus-unit polar decomposition |
| --- | --- | --- |
| $\Sigma_{11}$ | two terms, unique | yes |
| the punctured scalar line | one term | yes |
| the Jordan part | none | yes |
| $\Sigma_{01}$ | two terms, unique | no |
| the origin | one term | no |
| the non-zero nilpotents | none | no |

**The two failures sit in opposite mixed regimes.** The Jordan part is invertible with no eigenbasis. A null element with two modes is a zero divisor with no polar decomposition. Neither failure implies the other.

### The Two Operators

**Two operators attached to one element have their singular loci exactly on the two cones.**

$$
L_{\tilde Q}(\tilde X)=\tilde Q\tilde X,\qquad
\mathrm{Sd}_{\tilde Q}(\tilde X)=\tilde Q\tilde X\tilde Q^{*},\qquad
\mathrm{ad}_{\tilde Q}(\tilde X)=\tilde Q\tilde X-\tilde X\tilde Q .
$$

| operator | locus | value on the locus |
| --- | --- | --- |
| $L_{\tilde Q}$ | the null cone | rank $2$ off the origin, $0$ at the origin |
| $\mathrm{Sd}_{\tilde Q}$ | the null cone | rank $1$ off the origin, $0$ at the origin |
| $\mathrm{ad}_{\tilde Q}$ | the spectral-degenerate cone | zero on the scalar line, of index $3$ elsewhere |

**The sandwich is singular exactly on the norm cone and the derivation is nilpotent exactly on the discriminant cone.** Each operator therefore measures one predicate and is blind to the other, and the pair of them is a second reading of the partition.

### Two Unipotent Motions

**The product of two unipotents leaves its regime, and its type is decided by one number.**

$$
T=U_1U_2,\qquad U_i=e_t+\vec\Upsilon_i,\qquad \vec\Upsilon_i^{2}=0,\qquad s=\vec\Upsilon_1\cdot\vec\Upsilon_2,
$$

$$
Q_t(T)=1-s,\qquad B^{2}(T)=1-Q_t^{2}=s(2-s),\qquad N(T)=1 .
$$

**The product is regular except at $s=0$ and $s=2$.** It is elliptic on the interval $0<s<2$, hyperbolic outside it, and defective at the two endpoints.

**The interval is the whole content of the theorem, and the sign of $s$ is not the criterion.** A positive pairing gives the elliptic type on $(0,2)$ and the hyperbolic type on $(2,\infty)$.

## The Two Invariants

### The Norm and the Causal Sign

**The norm is the multiplicative quadratic form of the entry before this one, and its vanishing is the wall of invertibility.**

$$
N(\tilde Q)=Q_t^{2}+B^{2}=\sum_{\mu}Q_\mu^{2},\qquad N(\tilde P\tilde Q)=N(\tilde P)N(\tilde Q),\qquad \tilde Q^{-1}=\frac{\tilde Q^{\natural}}{N}.
$$

**On the material sector the norm is the interval.** With $\tilde P=ip_0e_t+\vec p$ and real $p_0,\vec p$, in units with $c=1$,

$$
N(\tilde P)=-p_0^{2}+\lvert\vec p\rvert^{2}=-m^{2}.
$$

**The sign of $N$ is the causal sign and the level sets are the mass shells.** That is the reading of the previous entry and it is not repeated here. What matters here is that the norm takes one complex value and that only its vanishing is invariant under the whole structure: the sign, and the word *mass*, belong to the real slice.

### The Vector Square and the Modes

**The vector square is the discriminant, and it involves no scalar part.**

$$
B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2},\qquad \operatorname{disc}p_{\tilde Q}=-4B^{2},\qquad \lambda_+-\lambda_-=2iB .
$$

**The difference of the eigenvalues is twice $iB$, so $B$ is half the gap of the spectrum.** The vanishing of $B^{2}$ is therefore the coincidence of the two eigenvalues, and nothing else.

**On the material sector the vector square is the momentum squared.**

$$
B^{2}(\tilde P)=\lvert\vec p\rvert^{2},
$$

**so $B^{2}=0$ is $\vec p=0$.** The second predicate is motion: a real four-momentum has two distinct eigenvalues exactly when it moves.

**The two invariants are of different kinds, and that is why four regimes exist.** The norm is multiplicative and its zero set is closed under products. The vector square is not multiplicative and its zero set is not stable under products. One condition is about the group and the other about the spectrum, and a group condition and a spectral condition do not determine each other.

### The Material Slice

**The four regimes are cut on the complex algebra, and a real four-momentum occupies a four-dimensional slice of it.** The slice meets all four regimes, and it meets two of them in a set of lower dimension than the regime itself.

| regime | on the material slice | condition |
| --- | --- | --- |
| $\Sigma_{11}$ | a timelike or spacelike momentum with $\vec p\neq0$ | $p_0^{2}\neq\lvert\vec p\rvert^{2}$ and $\vec p\neq0$ |
| $\Sigma_{10}$ | the rest line only | $\vec p=0$ and $p_0\neq0$ |
| $\Sigma_{01}$ | the light cone without its apex | $p_0^{2}=\lvert\vec p\rvert^{2}$ and $\vec p\neq0$ |
| $\Sigma_{00}$ | the origin only | $p_0=0$ and $\vec p=0$ |

**The Jordan part of $\Sigma_{10}$ is empty for matter.** A real spatial vector has $B^{2}=\lvert\vec p\rvert^{2}$, a sum of three real squares, so it is isotropic only when it vanishes, and then there is no nilpotent part. The exceptional point of that regime is a property of the complexified algebra.

**The same is true of the nilpotent ladder.** The non-zero nilpotents of $\Sigma_{00}$ are complex isotropic vectors, and no real four-momentum is one. The material share of the fourth regime is the single origin.

## The Four Regimes

**The four regimes are stated here as one table and one paragraph each.** The proofs are in the four sector articles. This section states what the table says and where the names come from.

| regime | real dimension | spectrum | invertible | eigenbasis | polar word | name |
| --- | --- | --- | --- | --- | --- | --- |
| $\Sigma_{11}$ | $8$, open and dense | $\{\lambda_+,\lambda_-\}$, distinct and non-zero | yes | yes, unique | yes | mass in motion |
| $\Sigma_{10}$ | $6$ | $\{Q_t\}$, $Q_t\neq0$ | yes | on the scalar line; none on the Jordan part | yes | the rest frame and the exceptional point |
| $\Sigma_{01}$ | $6$ | $\{2Q_t,0\}$, $2Q_t\neq0$ | no | yes, unique | no | the light ray |
| $\Sigma_{00}$ | $4$ | $\{0\}$ | no | only at the origin, trivially | no | the vacuum and the nilpotent ladder |

**The dimensions are counts of complex equations.** The norm is one complex equation whose gradient does not vanish off the origin, so its zero set has real dimension six. The vector square is one complex equation whose gradient does not vanish off the scalar line, so its zero set has real dimension six. The pair has real dimension four, because on the intersection the scalar coordinate is zero and the vector part is isotropic.

### The Generic Regime

**$\Sigma_{11}$ is the complement of the union of two cones, so it is open.** Its complement has real codimension two, so it is also dense, and an element drawn without a rule lies in it: a hundred random draws with complex normal coefficients gave a hundred elements of $\Sigma_{11}$.

**The element is invertible with two distinct eigenvalues.** It has two orthogonal spectral idempotents, a unique two-term decomposition, an eigenbasis, a modulus and a unit factor. Every description the category has built applies here, and applies here only.

**The physical name is mass in motion, and the name is exact.** On the material slice the element is a timelike momentum with a non-zero spatial part, or a spacelike one. The two eigenvalues are the two light-cone frequencies, their product is $-m^{2}$, and their ratio is the squared Doppler factor.

### The Rest Frame and the Exceptional Point

**$\Sigma_{10}$ is the set of invertibles whose two eigenvalues have merged.** The gradient of $B^{2}$ vanishes on the scalar line, so the regime is not a manifold there, and it has two faces that share no physics.

**The scalar line is the semisimple face.** The element is $Q_te_t$: one eigenvalue, repeated, and every basis is an eigenbasis. On the material slice this is the rest frame, the only frame in which the momentum is purely temporal.

**The Jordan part is the defective face.** The element is $Q_te_t+\vec\Upsilon$ with $\vec\Upsilon$ a non-zero pure nilpotent: one eigenvalue, one eigendirection, a single Jordan block, and no eigenbasis at all. Its reading is the exceptional point of a non-Hermitian operator, where two eigenvalues and two eigendirections have coalesced.

**The two faces have the same norm and the same characteristic polynomial.** They differ in the minimal polynomial, which is $X-Q_t$ on the line and $(X-Q_t)^{2}$ on the Jordan part. That is the sharpest statement in the entry: no function of the spectrum separates them.

### The Light Ray

**$\Sigma_{01}$ is the set of null elements with two distinct eigenvalues.** The gradient of $N$ does not vanish there, so the regime is a manifold of real dimension six, and the element is a non-zero multiple of a non-trivial idempotent.

$$
N(\tilde Q)=0,\quad B^{2}\neq0\quad\Longrightarrow\quad \tilde Q=\kappa\tilde\Pi,\qquad \kappa=2Q_t\neq0,\qquad \tilde\Pi^{2}=\tilde\Pi .
$$

**The spectrum is $\{\kappa,0\}$ and one eigenvalue is zero.** So the element has a unique two-term decomposition with one coefficient zero, an eigenbasis, no inverse, and no polar decomposition: a modulus would need a square root of zero.

**The physical name is the light ray.** On the material slice the regime is the light cone without its apex, and the element is a massless momentum: one light-cone eigenvalue vanishes and the other is twice the energy.

### The Vacuum

**$\Sigma_{00}$ is the set of square-zero elements, and it is the common boundary of the other three.**

$$
\tilde Q^{2}=0\iff \tilde Q\in\Sigma_{00},\qquad \Sigma_{00}=\{0\}\cup\{\vec\Upsilon:\vec\Upsilon\neq0,\ \vec\Upsilon^{2}=0\}.
$$

**Off the origin the element is a pure nilpotent, and the origin is the only semisimple point.** The minimal polynomial is $X^{2}$ off the origin and $X$ at it, and the two share the norm, the trace and the characteristic polynomial.

**The physical name is the vacuum together with its nilpotent ladder.** The origin is the unique element with zero momentum and zero scale. The nilpotents are the one-site ladder: two of them with anticommutator $e_t$ produce orthogonal idempotents, which are null elements of the previous regime.

## Independence

**The two conditions are independent in the strong sense: neither cone contains the other.**

$$
\mathcal N\not\subseteq\mathcal S,\qquad \mathcal S\not\subseteq\mathcal N .
$$

**The witnesses are the two mixed regimes, and each is a short element.** The element $e_t+i\vec e_x$ has $N=0$ and $B^{2}=-1$; it is null and its eigenvalues are $0$ and $2$, so it has a full eigenbasis. The element $e_t+\vec e_x+i\vec e_y$ has $N=1$ and $B^{2}=0$; it is invertible whose minimal polynomial is $(X-1)^{2}$, so it has no eigenbasis.

**A second pair of witnesses covers the degenerate corners.** The scalar $ie_t$ has $N=-1$ and $B^{2}=0$, and the nilpotent $\vec e_x+i\vec e_y$ has $N=0$ and $B^{2}=0$. The four elements together exhibit all four combinations, which is the proof that the partition is fourfold and not twofold.

**The independence of the conditions is not the independence of the numbers.** The map $\tilde Q\mapsto(N,B^{2})$ has rank two except on the hyperplane $Q_t=0$ and on the scalar line, so off those two sets the two values can be prescribed locally and independently. On the hyperplane the two gradients coincide and the rank is one; on the scalar line the second gradient vanishes and the rank is one again.

**The asymmetry of the two conditions is what forces four regimes rather than a dichotomy.** The norm is multiplicative and its zero set is a subsemigroup. The vector square is neither multiplicative nor additive. A product of two null elements is null, and the product can even be zero:

$$
(e_t+i\vec e_x)(e_t-i\vec e_x)=0 .
$$

**So the null cone is stable under products and the light-ray regime is not.** The product of two elements of $\Sigma_{01}$ has norm zero and lies in $\Sigma_{01}$ or in $\Sigma_{00}$, and both outcomes occur. The vector square has no such stability: two elements of $\Sigma_{10}$ can compose into $\Sigma_{11}$, which is the theorem of §*Two Unipotent Motions*.

**The zero product is worth stating as its own fact.** The two factors are null, non-zero, and their product vanishes. A semigroup with such pairs is a semigroup with annihilators, and the annihilator of a null element is another null element of the opposite phase.

## Where the Two Walls Meet

**The intersection of the two cones is the square-zero set, and the identification is exact in both directions.**

$$
\mathcal N\cap\mathcal S=\{\tilde Q:\tilde Q^{2}=0\}=\{Q_t=0,\ \vec Q^{2}=0\}.
$$

**The forward inclusion is a computation in two lines.** If $N=0$ and $B^{2}=0$ then $Q_t^{2}=N-B^{2}=0$, and the square of a pure vector is $-B^{2}e_t$, which vanishes. The converse uses the identity

$$
\tilde Q^{2}=(Q_t^{2}-B^{2})e_t+2Q_t\vec Q .
$$

**A vanishing square with a non-zero vector part forces $Q_t=0$ from the vector component, and then $B^{2}=0$ from the scalar component.** A vanishing square with a zero vector part is a scalar whose square is zero, that is the origin.

**On the intersection the two walls are tangent.** The gradients are

$$
\vec\nabla_\Phi N=2(Q_t,Q_x,Q_y,Q_z),\qquad \vec\nabla_\Phi B^{2}=2(0,Q_x,Q_y,Q_z),
$$

**and they coincide exactly where $Q_t=0$, which on the two cones is the intersection.** Away from the origin both gradients are non-zero, so both cones are smooth there and their tangent hyperplanes agree. At the origin both gradients vanish and both cones are singular.

**Tangency is a statement about first order, and it has a reading.** At a square-zero element, an infinitesimal displacement changes the two invariants by the same amount to first order. No first-order measurement can tell whether the mass or the splitting has moved, because the two move together.

**The intersection is not a fifth regime.** It is the doubly degenerate regime, and it is exactly the set on which both predicates are false. What the tangency adds is that the two walls are not in general position there: the arrangement has a stratum on which the two defining equations are dependent.

## The Chain of Invariants

**Three invariants, three counts, and each is a function of the one above it.**

$$
N=\text{constant term of }p_{\tilde Q},\qquad p_{\tilde Q}\in\{m_{\tilde Q},\,m_{\tilde Q}^{2}\}.
$$

**Read downward, information is lost and lost irreversibly.** The norm forgets the sum of the eigenvalues. The characteristic polynomial forgets whether the element is scalar or Jordan. The minimal polynomial forgets nothing.

| invariant | number of types | separates | fails to separate |
| --- | --- | --- | --- |
| norm $N$ | $2$ | units from null elements | the scalar line from the Jordan part; the origin from the nilpotents |
| characteristic polynomial | $4$ | the four regimes | the two faces of $\Sigma_{10}$ and of $\Sigma_{00}$ |
| minimal polynomial | $6$ | the six strata | nothing |

**The failure of the norm is a theorem and not an oversight.** For $Q_t\neq0$ and a non-zero pure nilpotent $\vec\Upsilon$, the scalar $Q_te_t$ and the Jordan element $Q_te_t+\vec\Upsilon$ have the same norm $Q_t^{2}$, the same trace $2Q_t$, and therefore the same characteristic polynomial $(X-Q_t)^{2}$. Their minimal polynomials are $X-Q_t$ and $(X-Q_t)^{2}$.

**The same computation at the origin gives the second pair.** The origin and every non-zero nilpotent have norm zero, trace zero and characteristic polynomial $X^{2}$. Their minimal polynomials are $X$ and $X^{2}$.

**So the chain is a chain of coarse-grainings.** A measurement of the norm is a measurement of one number; a measurement of the spectrum is a measurement of two; the defect is a third fact that neither sees.

**The chain also fixes what the partition is not.** A finer classification exists, by the minimal polynomial, and it cuts two of the four regimes in two. The partition of this entry is the coarsest cut that still separates invertibility from the spectrum, and the finer cut is a different question.

## The Two Decompositions

**The spectral decomposition follows the discriminant and the polar decomposition follows the norm.**

**The spectral side.** On $\Sigma_{11}$ and on $\Sigma_{01}$ there is a unique writing $\tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-$ with orthogonal idempotents summing to $e_t$, and the idempotents are

$$
\tilde\Pi_\pm=\frac{\tilde Q-\lambda_\mp e_t}{\lambda_\pm-\lambda_\mp}.
$$

**On the punctured scalar line the writing collapses to one term.** On the Jordan part no non-trivial idempotent commutes with the element, so no two-term writing exists. On the non-zero nilpotents the same failure occurs, and at the origin the trivial one-term writing $0=0\cdot e_t$ exists.

**The polar side.** A writing $\tilde Q=\varrho\,e^{i\theta_{\mathrm{pha}}}\tilde U$ with $\varrho\,e^{i\theta_{\mathrm{pha}}}\in\mathbb C$, $\varrho^{2}e^{2i\theta_{\mathrm{pha}}}=N(\tilde Q)$ and $N(\tilde U)=1$ exists exactly on $\Sigma_{11}\cup\Sigma_{10}$, and the modulus is a choice of square root.

**The two failures are in opposite mixed regimes.** The Jordan part is invertible with no eigenbasis. The light-ray regime is a zero divisor with an eigenbasis. So the two descriptions fail independently, and an element can have one without the other.

**Neither failure is a defect of the element.** Each is a defect of a description relative to a condition. The element exists in both cases; what does not exist is the coordinate system that the description assumes.

## The Two Operators

**Two operators read the two cones, and a third reads the strata.**

**Left multiplication has rank four on the units, two on the non-zero null elements, and zero at the origin.** So it measures invertibility and separates the origin from the null cone. It does not separate the scalar line from the Jordan part, because its rank is four on both.

**The sandwich is singular exactly on the null cone.** With $\mathrm{Sd}_{\tilde Q}(\tilde X)=\tilde Q\tilde X\tilde Q^{*}$, the proof is one line: if $N=0$ then

$$
\mathrm{Sd}_{\tilde Q}(\tilde Q^{\natural})=\tilde Q\tilde Q^{\natural}\tilde Q^{*}=N\tilde Q^{*}=0,
$$

**and if $N\neq0$ then the sandwich is invertible, with inverse $\mathrm{Sd}_{\tilde Q^{-1}}$.** Off the origin its rank is one, and at the origin it is zero.

**The inner derivation satisfies a closed identity, and the identity decides everything.**

$$
\mathrm{ad}_{\vec Q}^{3}=-4B^{2}\,\mathrm{ad}_{\vec Q},
$$

**so the derivation is nilpotent exactly when $B^{2}=0$.** On the scalar line it is zero. On the Jordan part and on the non-zero nilpotents its index is three. On the two regular regimes it is not nilpotent, because a nilpotent operator on a four-dimensional space would satisfy $\mathrm{ad}^{4}=0$, while the identity gives $\mathrm{ad}^{4}=-4B^{2}\mathrm{ad}^{2}\neq0$.

**The pair of loci is therefore a second reading of the partition, and a finer one.** The sandwich follows the norm and the derivation follows the discriminant. Together they separate the scalar line from the Jordan part and the origin from the non-zero nilpotents, which the norm alone cannot do.

**The sandwich is not a new object.** Its value at the identity is the weight of the previous entry,

$$
\operatorname{Sc}\mathrm{Sd}_{\tilde Q}(e_t)=\operatorname{Sc}(\tilde Q\tilde Q^{*})=H(\tilde Q),
$$

**so the operator whose singularity marks the massless wall is the operator that measures the amplitude.**

## Two Unipotent Motions

**A unipotent is $U=e_t+\vec\Upsilon$ with $\vec\Upsilon$ a non-zero pure nilpotent: a unit of norm one, with the double eigenvalue $1$ and no eigenbasis.** It is the shear of the algebra, and it lies in one of the two strata of the spectral wall.

**The product of two of them stays in the norm-one slice and leaves the wall.**

$$
T=U_1U_2=e_t+\vec\Upsilon_1+\vec\Upsilon_2+\vec\Upsilon_1\vec\Upsilon_2,\qquad \operatorname{Tr}T=2+t,\qquad \det T=1,
$$

$$
p_T(\lambda)=\lambda^{2}-(2+t)\lambda+1,\qquad t=2\,\mathrm{Sc}(\vec\Upsilon_1\vec\Upsilon_2)=-2s,\qquad s=\vec\Upsilon_1\cdot\vec\Upsilon_2 .
$$

**So the product is described by one complex number, and the criterion is one equation.**

$$
Q_t(T)=1+\frac{t}{2}=1-s,\qquad B^{2}(T)=-\frac{t(t+4)}{4}=s(2-s).
$$

**The product is regular exactly when $s\notin\{0,2\}$.** At $s=0$ the single eigenvalue is $1$: the product is $e_t$ when $\vec\Upsilon_2=-\vec\Upsilon_1$ and a non-trivial unipotent otherwise. At $s=2$ the single eigenvalue is $-1$ and the product is $-e_t$ times a non-trivial unipotent. The element $-e_t$ itself cannot occur, because a unipotent has scalar part one.

**On the regular set the type is decided by the interval and not by the sign.**

| $s$ | spectrum | type | name |
| --- | --- | --- | --- |
| $0<s<2$, real | non-real conjugates on the unit circle | elliptic | a rotation |
| $s<0$ or $s>2$, real | real and reciprocal; positive for $s<0$, negative for $s>2$ | hyperbolic | a boost, with a central $-1$ in the second case |
| $s$ not real | non-real and reciprocal, moduli not one | neither | a complex motion |
| $s=0$ | $\{1\}$ | degenerate | the identity or a shear |
| $s=2$ | $\{-1\}$ | degenerate | minus a shear |

**The warning is worth a sentence of its own.** A positive pairing does not mean the elliptic type: $s\in(0,2)$ is elliptic and $s\in(2,\infty)$ is hyperbolic, and both are positive. The criterion is the sign of $s(2-s)$, which is the sign of the vector square of the product on the real line.

### The Two Worked Cases

**Two pairings of the same nilpotent give the two regular types.**

$$
\vec\Upsilon_1=\frac{i}{2}\vec e_x-\frac{1}{2}\vec e_y,\qquad
\vec\Upsilon_2=-\frac{i}{2}\vec e_x-\frac{1}{2}\vec e_y,\qquad s=\frac{1}{2} .
$$

**Both are pure nilpotents, the pairing is one half, and the product is**

$$
T=\frac{1}{2}e_t-\vec e_y-\frac{i}{2}\vec e_z,\qquad Q_t=\frac{1}{2},\qquad B^{2}=\frac{3}{4},\qquad \lambda_\pm=e^{\pm i\pi/3},
$$

**which is elliptic: the eigenvalues are the sixth roots of unity.**

**Replacing the second nilpotent by its negative gives the other type.**

$$
\vec\Upsilon_3=-\vec\Upsilon_2,\qquad s=-\frac{1}{2},\qquad Q_t=\frac{3}{2},\qquad B^{2}=-\frac{5}{4},\qquad \lambda_\pm=\frac{3\pm\sqrt{5}}{2},
$$

**which is hyperbolic: real, reciprocal and positive.** The two products differ only in the pairing of the two nilpotent parts, and that difference is the difference between a rotation and a boost.

### The Image Theorem

**Every element of the norm-one group except $-e_t$ is a product of two non-trivial unipotents, and every invertible element is a central scalar times an element of the norm-one slice.**

**The mechanism is visible in the invariants.** On the slice $B^{2}=1-Q_t^{2}$, so the two invariants of a norm-one element are not independent: prescribing $Q_t$ prescribes $B^{2}$. The product law has $Q_t=1-s$ and $B^{2}=s(2-s)$, which is the same relation, so $s=1-Q_t$ reproduces both invariants. The single value that fails is $s=2$, that is $Q_t=-1$, and it fails because $B^{2}=0$ there and the product is defective.

**So the shear set generates the group except at one point.** The exception is the element that squares to $-e_t$: the central element that represents the full turn in the double cover.

## The Interpretations

### I.10.a — Two Questions, Not One: the Mass and the Motion

**Read:** two quadratic forms on one element, and two predicates that do not determine each other.

**A single invariant cannot ask two questions.** The norm is one complex number; it can be zero or not, and the sign of a real value adds a second bit, but it cannot say whether the spectrum is separated. The vector square is a second quadratic form, it is not a function of the first, and the pair of them is the smallest amount of data that answers both questions.

**The physical interpretation is that mass and motion are independent attributes of one object and not two names for one attribute.** A four-momentum has a mass and a direction. The mass is the invariant magnitude and the direction is the splitting. The algebra says that these are cut by two different equations, so a change of one does not force a change of the other.

**The reading is structural and it stops at the surface.** The two forms are fixed by the algebra and not chosen. No coefficient in them is free, so the independence is a property of the quaternion multiplication and not of a modelling decision.

**The boundary.** Independence of two predicates is not statistical independence and not causal independence. Nothing here says that a process changes the mass without changing the momentum. It says that the two conditions on an element are logically independent.

### I.10.b — The Four Names Are the Four Answers

**Read:** the table of §*The Four Regimes*, whose last column names each class after the part of it that matter reaches.

**A name is a compression of a regime, and it must be recoverable from the algebra.** Mass in motion is invertible with two modes on a timelike or spacelike momentum with a non-zero spatial part. The rest frame is the semisimple face of the invertibles with one mode. The light ray is a null element with two modes and one vanishing eigenvalue. The vacuum is the square-zero set, of which matter reaches only the origin.

**The physical interpretation is that the four regimes are the four kinematic situations of a four-momentum, extended to the complex algebra.** There is no fifth situation, because a quadratic has only four degeneration patterns: two distinct non-zero roots, a double non-zero root, two distinct roots with one at zero, and a double root at zero.

**The extension is what makes the table worth stating.** Two of the four regimes contain objects that no real momentum reaches: the Jordan part of the second and the nilpotents of the fourth. The table is the complexification of a kinematic classification, and the extra points are the price of working in an algebra that is closed under its operations.

**The boundary.** The names are names of regimes and not of particles. A regime is a set of elements, and nothing in the algebra counts them.

### I.10.c — The Generic Element Is Doubly Regular

**Read:** $\Sigma_{11}$ is open and dense, of real dimension eight, and its complement is the union of two cones of real codimension two.

$$
\dim_{\mathbb R}\Sigma_{11}=8,\qquad \dim_{\mathbb R}\Sigma_{10}=\dim_{\mathbb R}\Sigma_{01}=6,\qquad \dim_{\mathbb R}\Sigma_{00}=4 .
$$

**A hundred random draws with complex normal coefficients gave a hundred elements of $\Sigma_{11}$.** The degenerate regimes are not small in the sense of being rare in a discrete family. They are small in the sense of having no interior.

**The physical interpretation is that the exceptional regimes are walls and not rooms.** An element drawn without a rule is invertible with two modes. To be at rest, to be null, or to be square-zero is to satisfy an equation, and an equation is a wall.

**The reading gives a precise sense to the word exceptional.** The word does not mean improbable in the sense of a rare event with a probability. It means of empty interior and of lower dimension, so that a generic perturbation leaves the regime at once.

**The boundary.** Typicality in the algebra is not typicality in nature. A physical configuration is not drawn from a Gaussian on the coefficients, and a system can sit on a wall by symmetry: a particle at rest is a wall, and it is a stable physical situation.

### I.10.d — Neither Answer Implies the Other

**Read:** the two witnesses $e_t+i\vec e_x$ and $e_t+\vec e_x+i\vec e_y$, one in each mixed regime.

**One element is null and has a full eigenbasis; the other is invertible and has none.** The first is $2\tilde\Pi$ for a non-trivial idempotent, so its spectrum is $\{2,0\}$ and its spectral decomposition is unique. The second satisfies $(\tilde Q-e_t)^{2}=0$ with $\tilde Q\neq e_t$, so its minimal polynomial has degree two and no non-trivial idempotent commutes with it.

**The physical interpretation is that having a mass and having a mode basis are different achievements.** A massless element can be perfectly resolvable into two modes, and a massive element can be a single defective block. Neither property is a consequence of the other, and neither is a proxy for the other.

**The two witnesses are also the sharpest counterexamples to a tempting inference.** The tempting inference is that a zero divisor is a degenerate object in every sense. It is degenerate in invertibility and regular in spectrum, and the two words must be kept apart.

**The boundary.** A witness is one element, and it proves non-implication and not typicality. The mixed regimes are lower-dimensional, so the two witnesses are exceptional objects that prove a logical point.

### I.10.e — On the Nilpotent Cone the Two Dials Are One Dial

**Read:** $\vec\nabla_\Phi N=\vec\nabla_\Phi B^{2}$ exactly on $\{Q_t=0\}$, and on the two cones that set is $\Sigma_{00}$.

**The tangency is an exact statement about first order.** At a square-zero element a displacement changes the two invariants by the same amount to first order, because the scalar coordinate is absent from both gradients and the vector part enters both identically.

**The physical interpretation is that at a square-zero element the mass and the splitting cannot be moved separately.** An infinitesimal perturbation changes both or neither, and no first-order measurement distinguishes which one has moved.

**The reading explains what the doubly degenerate set is.** The two cones are two surfaces in an eight-dimensional space. Along the nilpotent cone they share a tangent hyperplane, so they touch and do not cross. The dimension of their intersection is nevertheless the one the codimensions predict, four real dimensions, because two sets of real codimension two meet in codimension four whether they are transverse or not. What the tangency changes is not the size of the intersection but the way a perturbation leaves it: to first order the two equations fail together.

**The boundary.** The statement is first order. At second order the two invariants separate again, because they differ by $Q_t^{2}$ and a displacement that creates a non-zero scalar part breaks the coincidence at once.

### I.10.f — The Norm Is Blind to the Defect

**Read:** $Q_te_t$ and $Q_te_t+\vec\Upsilon$ have the same norm, the same trace and the same characteristic polynomial, and different minimal polynomials.

**The two elements are indistinguishable by any function of the spectrum.** They differ in one bit: whether the element is a scalar or a single Jordan block. That bit is not in the norm and not in the characteristic polynomial.

**The physical interpretation is that a mass measurement does not report whether the object has a mode basis.** Two objects of the same mass and the same rate can differ in whether their description has two eigendirections or one, and no spectral measurement sees the difference.

**The same blindness occurs at the vacuum.** The origin and every non-zero nilpotent have norm zero and characteristic polynomial $X^{2}$, and they differ in the minimal polynomial, $X$ against $X^{2}$.

**The boundary.** The defect is visible to the element and to the derivation, which is nilpotent on one and zero on the other. So the blindness belongs to the invariants and not to the algebra: a finer operator reads what the numbers do not.

### I.10.g — The Chain of Invariants Is a Chain of Forgetting

**Read:** the norm gives two types, the characteristic polynomial four, the minimal polynomial six, and each is a function of the one above it.

**Reading down the chain loses information, and the loss is irreversible.** The norm forgets the trace. The characteristic polynomial forgets the defect. Nothing recovers what is forgotten.

**The physical interpretation is a hierarchy of coarse-grainings.** The mass is the coarsest observable of an element, the spectrum is finer, and the defect is the finest. A theory that records only the mass has thrown away the frame and the defect. A theory that records the spectrum has kept the two rates and thrown away the defect.

**The hierarchy is a hierarchy of measurements and not of systems.** The same element has all three descriptions, and the choice of description is a choice of what to measure.

**The boundary.** The counts two, four and six count types and not values. The characteristic polynomial takes infinitely many values and falls into four patterns, and the table counts the patterns.

### I.10.h — Two Descriptions Fail in Opposite Regimes

**Read:** the eigenbasis fails on the Jordan part, the polar decomposition fails on the null cone, and the Jordan part is invertible while a null element is not.

**The two failures are independent because the two conditions are.** an invertible element can fail to have an eigenbasis. A zero divisor can have one. The two descriptions are therefore not two names for one structure.

**The physical interpretation is that non-invertibility and non-diagonalisability are different obstructions.** An object can be irreversible and perfectly resolvable, or reversible and defective. The two words are used loosely in physics, and the algebra separates them.

**The reading is a warning about descriptions.** A description is a coordinate system: the eigenbasis assumes distinct eigenvalues, the polar word assumes a non-zero norm. A failure of a description is not a failure of the element, and the two failures do not coincide.

**The boundary.** Each description has its own replacement. On the Jordan part the Jordan basis replaces the eigenbasis. On the null cone the two-factor pair replaces the polar word. This entry states the failures; the replacements belong to the entries on the Jordan basis and on the null cone.

### I.10.i — The Channel Closes Where the Mass Closes, the Shear Stops Where the Modes Merge

**Read:** $\mathrm{Sd}_{\tilde Q}$ is singular exactly on $\mathcal N$, and $\mathrm{ad}_{\tilde Q}$ is nilpotent exactly on $\mathcal S$, of index three off the scalar line.

**The sandwich is singular on the massless wall and the derivation dies on the spectral wall.** Two operators, one for each predicate, and each is blind to the other condition.

**The nilpotence has a reading as a truncated series.** With $\mathrm{ad}^{3}=-4B^{2}\mathrm{ad}$, the conjugation by a degenerate element is a polynomial of degree two in the derivation,

$$
e^{t\,\mathrm{ad}_{\tilde Q}}=1+t\,\mathrm{ad}_{\tilde Q}+\frac{t^{2}}{2}\,\mathrm{ad}_{\tilde Q}^{2}\qquad (B^{2}=0),
$$

**so a degenerate element displaces other elements, but the displacement stops after the second power.** On the scalar line the series stops at the first term, because the derivation is zero.

**The physical interpretation is that a coalesced mode has a short memory of its action.** An element that acts by conjugation can carry a perturbation only to second order when its spectrum has merged, and to all orders when it has not.

**The boundary.** The identity is algebraic and it says nothing about a dynamics. The word *memory* is a reading of the length of a polynomial and not of a physical relaxation.

### I.10.j — Two One-Mode Motions Compose into a Two-Mode One

**Read:** $U_1U_2$ with $U_i=e_t+\vec\Upsilon_i$, both defective, and $B^{2}(U_1U_2)=s(2-s)$.

**The defect is not inherited.** Two elements of the spectral wall compose into an element off it whenever $s\notin\{0,2\}$, and the product is invertible with two distinct eigenvalues.

**The physical interpretation is that composing two shears produces a rotation or a boost, and never another shear.** A shear is a null transformation: it fixes one direction and displaces everything else along it. Two of them, about different null directions, compose into a transformation of the elliptic or the hyperbolic type.

**The composition is the elementary mechanism by which a two-mode object is built from one-mode objects.** The regime of the factors is not the regime of the product, so the partition is not preserved by multiplication.

**The boundary.** The composition is in the complexified group. On the material slice there are no non-zero nilpotents, so no real light ray is a shear, and the theorem does not describe the composition of two real massless momenta.

### I.10.k — The Interval Decides the Type, the Sign Does Not

**Read:** elliptic on $0<s<2$, hyperbolic on $s<0$ and on $s>2$, defective at the two endpoints.

**A pairing is a complex number, and the type of the product is decided by where it lies.** The sign of the real part is not the criterion. The criterion is the sign of $s(2-s)$, which is the sign of the vector square of the product.

**The physical interpretation is that two null rotations compose into a rotation when their null directions are close, and into a boost when they are not.** The threshold is a definite value of the pairing and not its sign, and there are two ways to exceed it.

**The reading corrects a plausible error.** The plausible error is that a positive pairing gives a rotation and a negative pairing a boost. The first statement is false on $(2,\infty)$, where the pairing is positive and the product is hyperbolic.

**The boundary.** The pairing is the complex bilinear dot product of the two nilpotent parts and not a Hermitian product. On a real slice the bilinear product changes sign with the metric, and the interval $(0,2)$ is stated for the complex form.

### I.10.l — Every Motion Is Two Null Motions, Except the Full Turn

**Read:** every element of the norm-one group except $-e_t$ is a product of two non-trivial unipotents, and every invertible element is a central scalar times such an element.

**One exception, and it is the element that squares to minus the identity.** The failure is not generic: it is a single point of the group, and the point is the central element that represents a full turn in the double cover.

**The physical interpretation is that the shear set generates the reversible motions, with one point missing.** A null transformation is the most degenerate reversible motion, and two of them generate a general one. The single element that is not generated is the one that a closed path of length $2\pi$ reaches.

**The reading is a statement about generation and not about the decomposition of a process.** Nothing says that a physical motion is performed as two null motions in sequence. The theorem says that the group is generated by them, which is a statement about the reach of the degenerate stratum.

**The boundary.** The exception is a fact about a set of generators and not about the sign of a spinor. The identification of $-e_t$ with the full turn is a reading of the double cover, and it does not convert the theorem into a statement about fermions.

## The Limits

**The partition is complete and it is not a classification of elements up to equivalence.** The four regimes are sets, and two elements of one regime can be inequivalent in every other respect. The partition answers two questions and no more.

**A regime is not a phase.** There is no order parameter, no free energy and no continuity between the regimes. Two regimes of different dimension cannot be connected by a path that stays inside their union, because the higher-dimensional one would have to contain the lower.

**The names do not extend over the complex algebra.** The words *rest frame*, *light ray* and *vacuum* name the parts of the regimes that the material slice reaches. The Jordan part and the nilpotent ladder are not matter, and a statement about them is a statement about the complexified algebra.

**The independence of the conditions is a statement about gradients and not about causes.** The two invariants are functionally independent off the square-zero set. They are not statistically independent, and nothing in the algebra says that a process can change one without the other.

**The product law is not a composition law for regimes.** The product of two elements of a regime can lie in another regime, and the product of two null elements can vanish. The partition is not a congruence of the multiplicative structure, and no reading may treat it as one.

**The type of the unipotent product is an interval of the complex pairing.** It is not a statement about real light rays, because the material slice has no non-zero nilpotent.

**The two operator loci are loci of linear maps on the algebra.** The singularity of the sandwich and the nilpotence of the derivation are properties of operators and not of states. No norm and no rank here is a probability, and no index here is a charge.

**The chain of invariants is finite and it ends.** Three invariants separate the six strata, and no further invariant of this kind refines them. That the chain ends is a theorem about polynomials of degree two, and it does not claim that no other invariant exists.

## Summary

**Two quadratic conditions cut the algebra into four regimes, and the four regimes are the four kinematic situations of one element.**

| item | result |
| --- | --- |
| the two predicates | $N\neq0$ and $B^{2}\neq0$, the norm and the discriminant |
| the four regimes | $\Sigma_{11},\Sigma_{10},\Sigma_{01},\Sigma_{00}$, the four patterns of a quadratic |
| the dimensions | $8$, $6$, $6$, $4$ real, with $\Sigma_{11}$ open and dense |
| the walls | two cones of real codimension two, $\mathcal N$ and $\mathcal S$ |
| independence | neither cone contains the other; witnesses $e_t+i\vec e_x$ and $e_t+\vec e_x+i\vec e_y$ |
| the intersection | $\mathcal N\cap\mathcal S=\{\tilde Q^{2}=0\}$, where the cones are tangent |
| the rank of the map | $2$ off $Q_t=0$ and off the scalar line, $1$ on them |
| the chain | norm $2$ types, characteristic polynomial $4$, minimal polynomial $6$ |
| the two decompositions | the eigenbasis follows the discriminant, the polar word follows the norm |
| the two operators | $\mathrm{Sd}$ singular on $\mathcal N$, $\mathrm{ad}$ nilpotent on $\mathcal S$ with index $3$ |
| two unipotents | $Q_t=1-s$, $B^{2}=s(2-s)$, elliptic on $0<s<2$, hyperbolic outside |
| the image theorem | the norm-one group is generated by two unipotents, except at $-e_t$ |
| the material slice | $\Sigma_{11}$ with $\vec p\neq0$; the rest line; the light cone; the origin |

**The pair of values decides everything downstream.** If both predicates are true the element is invertible with two modes and every description applies. If one fails, exactly one description fails, and which one fails is decided by which predicate failed. If both fail the element squares to zero, and no description applies at all.

### What the Reader Should Retain

**The three statements to carry away are these.** The partition is by two independent equations, so it has four parts and not two, and the mixed parts are what show the independence. A part is a pair of truth values: it has no interior in general, the dimensions differ, and the names come from the material share. And the partition is not preserved by multiplication, because two shears compose into a rotation or a boost, and the type is decided by an interval of one complex pairing.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\tilde Q=Q_te_t+\vec Q$ | the element, with complex coefficients |
| $N(\tilde Q)=Q_t^{2}+B^{2}$ | the norm, the constant term of the characteristic polynomial |
| $B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2}$ | the vector square, the discriminant up to $-4$ |
| $p_{\tilde Q}(X)=X^{2}-2Q_tX+N$ | the characteristic polynomial |
| $\lambda_\pm=Q_t\pm iB$ | the two eigenvalues, $\lambda_+\lambda_-=N$ |
| $\mathcal N=\{N=0\}$ | the null cone, the wall of invertibility |
| $\mathcal S=\{B^{2}=0\}$ | the spectral-degenerate cone, the wall of separation |
| $\Sigma_{ij}$ | the regime with $N\neq0$ iff $i=1$ and $B^{2}\neq0$ iff $j=1$ |
| $\Sigma_{10}^{\mathrm{s}}$, $\Sigma_{10}^{\mathrm{J}}$ | the scalar line and the Jordan part |
| $\vec\Upsilon$ | a non-zero pure nilpotent, $\vec\Upsilon^{2}=0$ |
| $U=e_t+\vec\Upsilon$ | a unipotent: a unit of norm one with the double eigenvalue $1$ |
| $s=\vec\Upsilon_1\cdot\vec\Upsilon_2$ | the pairing of two nilpotent parts, with $t=-2s$ |
| $L_{\tilde Q}$ | left multiplication, of rank $4$, $2$ or $0$ |
| $\mathrm{Sd}_{\tilde Q}(\tilde X)=\tilde Q\tilde X\tilde Q^{*}$ | the sandwich, singular exactly on $\mathcal N$ |
| $\mathrm{ad}_{\tilde Q}$ | the inner derivation, nilpotent exactly on $\mathcal S$ |
| $H(\tilde Q)=\operatorname{Sc}\mathrm{Sd}_{\tilde Q}(e_t)$ | the weight of the previous entry, the amplitude |
| $\tilde P=ip_0e_t+\vec p$ | a four-momentum on the material slice, in units with $c=1$ |
| $\mathbb B^{\times}_{1}$ | the norm-one group, isomorphic to $SL_2(\mathbb C)$ |

## Further Reading

**In the mathematics corpus.** [Relations between the N Norm and Spectral Regularity and Degeneracy](../articles_maths/relations-between-the-n-norm-and-spectral-regularity-and-degeneracy.html) owns what this entry states: the four sectors, the independence of the two cones, the nilpotent intersection, the tangency, the comparison of the sectors, the chain of invariants, the two decompositions and the two operator loci. [The Product of Two Unipotent Elements and Its Spectrum](../articles_maths/the-product-of-two-unipotent-elements-and-its-spectrum.html) owns the product law, the criterion, the three regular types and the image theorem, and it is the article to consult for the proofs of §*Two Unipotent Motions*. The four regimes are proved one to an article: [The N-Regular, Spectrally Regular Sector](../articles_maths/the-n-regular-spectrally-regular-sector.html), [The N-Regular, Spectrally Degenerate Sector](../articles_maths/the-n-regular-spectrally-degenerate-sector.html), [The N-Degenerate, Spectrally Regular Sector](../articles_maths/the-n-degenerate-spectrally-regular-sector.html) and [The N-Degenerate, Spectrally Degenerate Sector](../articles_maths/the-n-degenerate-spectrally-degenerate-sector.html). The spectrum and the cone are [The Spectrum](../articles_maths/the-spectrum.html); the two bases are [The Eigenbasis of a Spectrally Regular Biquaternion](../articles_maths/the-eigenbasis-of-a-spectrally-regular-biquaternion.html) and [The Jordan Basis of a Spectrally Degenerate Biquaternion](../articles_maths/the-jordan-basis-of-a-spectrally-degenerate-biquaternion.html); the two decompositions are [The Complete Polar Decomposition of an N-Regular Biquaternion](../articles_maths/the-complete-polar-decomposition-of-an-n-regular-biquaternion.html) and its degenerate counterpart; the ranks and the annihilators are [The Four General Products and Their Relations over the Biquaternion Algebra](../articles_maths/the-four-general-products-and-their-relations-over-the-biquaternion-algebra.html).

**In this category.** [The Element: the Six Subspaces and the Two Ledgers](the-algebraic-vocabulary-element-conjugations-six-subspaces-and-two-ledgers.html) supplies the coordinates in which the two invariants are written. [The Four Forms and the Four Norms](the-four-forms-and-the-four-norms.html) supplies the four measures and the proof that only the quaternionic one is multiplicative, which is why the first predicate is a group condition. [The Four Products: Composition, Probability, Causality and Gauge](the-four-products-composition-probability-causality-and-gauge.html) supplies the products whose scalar parts the measures are. [The Spectrum and the Two Modes](the-spectrum-and-the-two-modes.html) supplies the eigenvalues, the discriminant and the reading of $B$ as half the gap. [The H Norm: Amplitude and Frame](the-h-norm-amplitude-and-frame.html) supplies the weight that the sandwich reproduces at the identity. [The N Norm: Mass, Angle and the Cone](the-n-norm-mass-angle-and-the-cone.html) is the entry before this one and supplies the norm, its cone and its two strata. The four entries that follow read the four regimes one to an article: *Mass in Motion: The Region of Both Invariants*, *The Rest Frame and the Exceptional Point*, *The Massless Regime* and *The Vacuum and the Nilpotent Ladder*.

**The sources of this entry.** [Rotor, Spin, Pair and Carrier: A Survey of the Closure Block](rotor-spin-pair-and-carrier-a-survey-of-the-closure-block.html) states the reach of the three carriers, which this entry uses for the four regimes. [The Spectrum and the Two Modes](the-spectrum-and-the-two-modes.html) reads the second predicate as the two modes and the stopped clock. [Mass in Motion: The Region of Both Invariants](the-region-of-mass-in-motion.html), [The Rest Frame and the Exceptional Point](the-rest-frame-and-the-exceptional-point.html), [The Massless Regime](the-massless-regime.html) and [The Vacuum and the Nilpotent Ladder](the-vacuum-and-the-nilpotent-ladder.html) take the four regimes one each. [The Group of Invertibles, the Cone and the Orders](the-group-of-invertibles-the-cone-and-the-orders.html) places the massless content on the first cone. [Norm and Pairing Conventions](norm-and-pairing-conventions.html) fixes the letters and the inertias.
