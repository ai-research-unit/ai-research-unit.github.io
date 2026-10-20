# __The Probability Band: No Clock, Three Species and the Geometric Phase__

## Introduction

The probability band is the general plain sesqualgebra,

$$
\tilde Q_1\star\tilde Q_2=\tilde Q_1\tilde Q_2^{*},
$$

whose scalar form is the positive definite Hermitian pairing and whose job in the framework is probability. It is one of the four general products, and this article reads what that product carries: a weight, a cone at the third power, three grades of reality, a purity gap, an arrow from a process to an observable, and a phase.

It also carries an absence, and the absence organises the rest. The band has no element whose square is $-e_t$, so it has no algebraic clock. The clock is owned by the composition band, where the central imaginary squares to minus the identity, and the probability band imports it as the parameter of a unitary family whose generator is material. A band that measures weights does not also generate the phase it measures.

The order is the order of the readings. Each section states the algebraic result first, the interpretation second, and its boundary last.

**Placement.** The article belongs to the Algebra block, after *The Krein Form and the Indefinite Structure*, because it closes the state side of the block. It is not a fifth product: the product is *The Four General Products: Composition, Probability, Causality, Gauge*, and this article reads the band that article names probability.

**Boundaries.** No dynamics is supplied. The Born rule is the normalised plain form, read as the trace formula, and is not derived here. The three species are grades of a reality condition, and the identification of a grade with a particle type is a hypothesis. The square is the minimal crossing of the sectors, not the only map that crosses them. The geometric phase is cited from its owners. The purity gap is a reading on the positive slice $\mathrm{Sc}=\tfrac12$ (trace one in the $2\times2$ image).

## The Results It Uses

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| The product, its right identity, its non-associativity and its zero divisors | [Introduction to the General Plain Sesqualgebra](../articles_maths/introduction-to-the-general-plain-sesqualgebra.html), [Zero Divisors of the General Plain Sesqualgebra](../articles_maths/zero-divisors-of-the-general-plain-sesqualgebra.html) |
| The Hermitian norm, its positivity and the invertibility criterion | [Norm and Invertibility in the General Plain Sesqualgebra](../articles_maths/norm-and-invertibility-in-the-general-plain-sesqualgebra.html) |
| The roots of $+1$ and the idempotents | [Square Roots of One and the Idempotents of the General Plain Sesqualgebra](../articles_maths/square-roots-of-one-and-the-idempotents-of-the-general-plain-sesqualgebra.html) |
| The roots of $0$ and the nilpotents of index three | [Square Roots of Zero and the Nilpotents of the General Plain Sesqualgebra](../articles_maths/square-roots-of-zero-and-the-nilpotents-of-the-general-plain-sesqualgebra.html) |
| The ternary product and the Jordan triple identity | [The Ternary Product and the Associator of the Biquaternioid Sesqualgebra](../articles_maths/the-ternary-product-and-the-associator-of-the-biquaternioid-sesqualgebra.html) |
| The type criterion for the one-sided operators of the quaternionic product | [One-Sided Operators on the General Quaternionic Algebra](../articles_maths/one-sided-operators-on-the-general-quaternionic-algebra.html) |
| The trace-one positive slice and the pure states | [Jordan Algebras and the Positive Cone](../articles_maths/jordan-algebras-and-the-positive-cone.html) |
| The connection, the curvature and the holonomy | [Fibre Bundles, Connections and Curvature](../articles_maths/fibre-bundles-connections-and-curvature.html) |

The physics sources are *The Four General Products*, *The Informational Sector*, *The Bloch Ball*, *Pancharatnam's Phase* and *The Hopf Fibration*.

## The Band and Its Neighbours

### The Product and the Norm

The product is the plain product with the star in the second slot. Its diagonal is the Hermitian square,

$$
\tilde Q\star\tilde Q=\tilde Q\tilde Q^{*},
$$

whose scalar part is a modulus,

$$
\mathrm{Sc}\bigl(\tilde Q\star\tilde Q\bigr)=\sum_\mu\lvert Q_\mu\rvert^{2}.
$$

The scalar is real and non-negative and vanishes only at $\tilde Q=0$, so the band's algebraic norm is positive definite and its square root is the topological norm.

The band has a right identity and no left one: $\tilde Q\star e_t=\tilde Q$, while $e_t\star\tilde Q=\tilde Q^{*}$. It is neither associative nor commutative. Its zero-divisor set is the parent's cone.

**The band measures and does not evolve.** The scalar of the product is a number, and a number selects no state. The states are the idempotents, the pure states are the trace-one idempotents of the Hermitian sector. The units are the reversible elements and the zero divisors are the maps that forget.

### The Two Neighbours

The **composition band** is the plain product $\tilde Q_1\tilde Q_2$. It is bilinear and associative, and its central imaginary is a root of $-1$: $(ie_t)^2=-e_t$. It carries the clock, the phase $e^{i\theta}$ and the differential calculus.

The **causality band** is the general quaternionic algebra $\tilde Q_1^{\natural}\tilde Q_2$, whose norm is the indefinite interval $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^{2}$ and whose null set is the causal cone. It carries the Lorentz action and the interval.

The probability band is the sesquilinear sibling of the first and the definite sibling of the second. Its square is the Hermitian square, its norm is the Hermitian norm, and its value is a weight. The three are three readings of one algebra, separated by the placement of the conjugations in the product.

## The Band Has No Clock

### The Central Square Is a Modulus

For a complex number $z$ the band's square of the central element is

$$
(ze_t)\star(ze_t)=ze_t\,\overline{ze_t}=z\bar z\,e_t=\lvert z\rvert^{2}e_t .
$$

The phase of $z$ disappears. A central value $\lambda e_t$ has a root exactly when $\lambda$ is a non-negative real number. For $\lambda>0$ the roots are the elements with $\tilde Q\tilde Q^{*}=\lambda e_t$, equivalently the matrices $\sqrt{\lambda}\,U$ with $U$ unitary; the central roots $z e_t$ with $\lvert z\rvert^{2}=\lambda$ are a subset, not the whole root set. The negative central values have no root. The central imaginary is the sharpest case:

$$
(ie_t)\star(ie_t)=ie_t\,\overline{ie_t}=i(-i)e_t=e_t .
$$

The element that generates the phase in the composition band squares to $+e_t$ here. It is not a root of $-e_t$; it is a unitary. The central phase $e^{i\theta}e_t$ is likewise a unitary, and its logarithm $i\theta e_t$ is a coefficient, not a band element with a negative square.

**Theorem (no clock element).** The band has no element $\tilde\Xi$ with $\tilde\Xi\star\tilde\Xi=-e_t$. The central values with a root in the band are exactly the non-negative real numbers.

*Proof.* If $\tilde\Xi\star\tilde\Xi=\tilde\Xi\tilde\Xi^{*}$ is central, its scalar part is $\sum_\mu\lvert\Xi_\mu\rvert^{2}$, non-negative and zero only at the origin, and its vector part vanishes; the value is a non-negative real scalar.

### The Clock Is Owned by the Composition Band

In the plain product the same central element has the other square,

$$
(ie_t)^{2}=-e_t,
$$

so $ie_t$ is a root of $-e_t$, the exponential $e^{i\theta}$ has an algebraic generator, and the phase is a one-parameter group inside the band. The composition band owns the clock in the strict sense.

The probability band owns the same centre but reads it as a modulus: it has the clock's values and not the clock's generator.

**The clock is imported as a material element.** A reversible family of the band is a family of unitaries $U(t')=e^{iHt'}$ with $H$ Hermitian. The family lies in the band, since $U(t')U(t')^{*}=e_t$, but its generator is $iH$, which is anti-Hermitian, that is, material. The band contains the clock's action and not the clock's element: time is the parameter of a family whose generator is material.

### The Interval Is a Clock and the Square a Ruler

The probability band's square is a **ruler**: the Hermitian norm is definite, it measures a length and it supplies the Born weight. The neighbouring quaternionic form is a **clock**: the interval is indefinite, it separates timelike from spacelike, and its zero set is the light cone. One element carries both because the grid carries both metrics. On the material sector the two read

$$
\langle\tilde R\rangle_{*}=c^{2}{t'}^{2}+\lvert\vec x\rvert^{2},
\qquad
\langle\tilde R\rangle_{\natural}=-c^{2}{t'}^{2}+\lvert\vec x\rvert^{2},
$$

so the ruler and the clock differ by twice the squared time, $\langle\tilde R\rangle_{*}-\langle\tilde R\rangle_{\natural}=2c^{2}{t'}^{2}$.

The reading is the instrument pair: the interval tells which events can be causally connected and how much proper time a worldline carries; the Hermitian square tells how long a vector is and, on the state slice, supplies the Born weight. The same algebra carries both because the four general products put the two forms on the same eight real coordinates. The pair is the transversal form of the no-clock theorem: the band has no clock element, but it has the ruler, and the clock is the interval of the neighbouring band.

**The boundary.** The clock is the causal structure of the interval, not a ticking device: no rate, no arrow and no dynamics are supplied. The ruler is the Born form, not a spatial metric; its length is a norm on the algebra and a probability only on the state slice. The two metrics are not two computations of one object; they are the two forms. On the material sector their difference is twice the squared time, and on the informational sector the same difference, $H-N$, is the purity gap of the state slice.

### The Causality Band Splits the Interval

The neighbour that carries the interval makes the split the probability band cannot make. In the general quaternionic algebra the product is $\tilde Q_1\star\tilde Q_2=\tilde Q_1^{\natural}\tilde Q_2$, and the natural form is $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{\natural})$. The adjoint of the plain left multiplication $L_{\tilde Q}(X)=\tilde Q X$ is $L_{\tilde Q^{\natural}}$.

**Proposition (the type criterion).** The left multiplication $L_{\tilde Q}$ is self-adjoint exactly when $\tilde Q$ is central, and skew-adjoint exactly when $\tilde Q$ is pure.

*Proof.* By the injectivity of the parameter map, $L_{\tilde Q^{\natural}}=L_{\tilde Q}$ is $\tilde Q^{\natural}=\tilde Q$, which is centrality; and $L_{\tilde Q^{\natural}}=-L_{\tilde Q}$ is $\tilde Q^{\natural}=-\tilde Q$, which is purity.

The centre $\mathbb{C}e_t$ is the two-real-dimensional time plane, carrying $ict'$ and $ct$; the pure part $\mathbb{C}\otimes\mathbb{R}^{3}$ is the six-real-dimensional space, carrying the three material and the three informational directions. The bracket of two pure elements is pure, because the scalar part of a commutator vanishes, so it touches no central coordinate.

**The interpretation.** The causality band's operator layer splits the interval into a central time plane and a pure spatial part: the self-adjoint parameter is time, the skew-adjoint parameter is space, and the bracket lives in the space. The probability band has no such split because its square is a modulus.

**The boundary.** The criterion concerns the one-sided operators of the quaternionic product. It does not derive the signature, the dimension four, or the names time and space; those names are the interpretation.

## The Cone Lives at the Third Power

### No Square-Zero Element

The band has no nonzero element whose square vanishes. The square is the Hermitian square, whose scalar part is $\sum_\mu\lvert Q_\mu\rvert^{2}$; that scalar vanishes only at the origin, and a vanishing Hermitian square has a vanishing scalar part. The root set of $0$ is therefore $\{0\}$ alone:

$$
\{\tilde\Xi:\tilde\Xi\star\tilde\Xi=0\}=\{0\}.
$$

The band has no nilpotent of index two. This is the first difference from the composition band, where the pure null elements are square-zero and the index is two; the band's square is $\tilde Q\tilde Q^{*}$ rather than $\tilde Q^{2}$, and it is positive semidefinite.

### The Nilpotents Are the Pure Cone at Index Three

The left-nested powers of the band are conjugate-linear iterations,

$$
\tilde Q^{\star k}=\tilde Q(\tilde Q^{*})^{k-1},
$$

so the index is a property of the pair $(\tilde Q,\tilde Q^{*})$ and can exceed two.

**Theorem (the nilpotents).** For a nonzero element the following are equivalent: it is a nilpotent of the band; its third power vanishes, $\tilde\Upsilon^{\star3}=0$; it is pure with vanishing central square, $\Upsilon_t=0$ and $(\vec\Upsilon,\vec\Upsilon)=0$; and it is a pure zero divisor of the plain product. When they hold, the index is exactly three: $\tilde\Upsilon^{\star2}\neq0$.

The nilpotent set is the parent's pure isotropic cone,

$$
\mathcal{N}_{\star}=\{\tilde\Upsilon\neq0:\ \Upsilon_t=0,\ (\vec\Upsilon,\vec\Upsilon)=0\},
$$

of complex dimension two. The non-pure zero divisors are zero divisors of the band and are not nilpotent. The set is inherited and the index is not: the same cone, one power further out.

**The witness.** The element $\tilde\Upsilon=\vec e_x+i\vec e_y$ has $\Upsilon_t=0$ and $(\vec\Upsilon,\vec\Upsilon)=1+i^{2}=0$. Its second power is nonzero,

$$
\tilde\Upsilon^{\star2}=\tilde\Upsilon\tilde\Upsilon^{*}=2e_t+2i\vec e_z,
$$

and its third power vanishes. The square is Hermitian, of rank one, and a positive multiple of an idempotent.

### The Square of a Nilpotent Is a Pure State up to Scale

The square $\tilde\Upsilon\star\tilde\Upsilon=\tilde\Upsilon\tilde\Upsilon^{*}$ is Hermitian and positive semidefinite. On the nilpotent cone it is nonzero and of rank one, so it is a positive multiple of a pure state. The band's nilpotent does not square to nothing; it squares to a state.

The two squares of the nilpotent are the two orders,

$$
\tilde\Upsilon\tilde\Upsilon^{*}
\qquad\text{and}\qquad
\tilde\Upsilon^{*}\tilde\Upsilon .
$$

They are a complete orthogonal pair. Each is a positive multiple of a pure state, their product vanishes, and their sum is the trace,

$$
\tilde\Upsilon\tilde\Upsilon^{*}+\tilde\Upsilon^{*}\tilde\Upsilon
=\mathrm{Tr}\bigl(\tilde\Upsilon\tilde\Upsilon^{*}\bigr)e_t
=2\langle\tilde\Upsilon\rangle_{*}e_t .
$$

Their difference is a traceless Hermitian element, an observable of square $+1$ up to scale:

$$
\tilde\Upsilon\tilde\Upsilon^{*}-\tilde\Upsilon^{*}\tilde\Upsilon
=2\langle\tilde\Upsilon\rangle_{*}\bigl(\tilde\Pi_+-\tilde\Pi_-\bigr),
$$

with $\tilde\Pi_\pm$ the two orthogonal pure states. The nilpotent therefore carries a **frame**: the two states its two squares produce, and the observable that distinguishes them. The frame is the band's version of the light cone's local structure.

**The boundary.** The frame is a pair of states and an observable, not a measurement; the algebra supplies no probability for either state and no dynamics that selects one. The zero-divisor cone is the parent's cone, but the nilpotency index is three: the wall is the same set, one power further out.

## The Three Species of Reality

### The Graded Reality Condition

The coefficients are complex, and the coefficient conjugation $\bar{\cdot}$ is an antilinear involution. A reality condition requires some coefficients to be fixed by it. There are three grades, and they are nested:

| condition on the coefficients | fixed set | real dimension | species |
| --- | --- | --- | --- |
| no coefficient real | $\mathbb{B}$ | $8$ | complex |
| the central coefficient real | $\{Q_t\in\mathbb{R}\}$ | $7$ | central |
| all four coefficients real | $\mathbb{R}^{4}$ | $4$ | real |

The first grade is no condition; the second fixes the scalar coordinate; the third fixes every coordinate. The sets are nested, $\mathbb{B}\supset\{Q_t\in\mathbb{R}\}\supset\mathbb{R}^{4}$, and the dimensions fall by one and then by three. The middle set is a real hyperplane, not a complex subspace; the last is the real form.

### The Three Species

- **Complex.** No coefficient is fixed: the generic complex spinor, eight real parameters, a phase in every coordinate.
- **Central.** The scalar is fixed: the clock is a real number and the three spatial coordinates are complex.
- **Real.** Every coefficient is fixed: the real spinor, four real parameters, the smallest of the three.

The taxonomy is the reading. The algebra fixes the grades; the identification of a grade with a particle type is a hypothesis, and no mass, charge or coupling is derived. The grade supplies a place in the classification, not a value.

**The ternary vertex.** The band carries the ternary product $\{\tilde Q_1,\tilde Q_2,\tilde Q_3\}=\tilde Q_1\tilde Q_2^{*}\tilde Q_3$, the middle model. It satisfies the Jordan triple identity, so the band is an algebraic $J^{*}$-algebra. A three-particle vertex read as this product is a three-slot coupling, and its coefficients are not the structure constants of a Lie algebra: a Lie bracket is binary and antisymmetric, while this is ternary and carries the involution in the middle slot. The reading explains the shape, not the value. The sibling gauge band's ternary product is the left model and fails the identity; that failure belongs to the gauge band.

### The Sector Is a Different Real Form

The informational sector is the fixed set of the star:

$$
\mathbb{M}_+=\{\tilde Q:\tilde Q^{*}=\tilde Q\}.
$$

It is also of real dimension four, and it is not the real grade. Its coordinates are a real central coefficient and three purely imaginary spatial coefficients; the real grade's are four real coefficients. The two forms intersect in $\mathbb{R}e_t$ and are otherwise distinct.

Both sit inside the central grade, since both have a real central coefficient; they are two slices of the same seven-dimensional hyperplane. The **real spinor** is the bar-fixed one, the **Hermitian spinor** the star-fixed one; the two are not interchangeable, and the trichotomy is a trichotomy of coefficient reality, not of the sector split.

**The boundary.** The grades classify spinors by how much of the coefficient vector is real; the sector split classifies by the star. A statement about one is not a statement about the other, and identifying the real grade with the informational sector is the mistake the distinction prevents.

## The Purity Gap Between the Two Metrics

### The Two Norms on the State Slice

Let $\tilde{Ϛ}$ be a trace-one positive element of the informational sector, written in the Bloch form

$$
\tilde{Ϛ}=\tfrac{1}{2}\bigl(e_t+i\vec r\bigr),
\qquad
\lvert\vec r\rvert\leq1 .
$$

The two norms give two different numbers on this one element. The probability norm is the Hermitian norm,

$$
P(\tilde{Ϛ})=\langle\tilde{Ϛ}\rangle_{*}
=\mathrm{Sc}\bigl(\tilde{Ϛ}\tilde{Ϛ}^{*}\bigr)
=\tfrac{1}{4}\bigl(1+\lvert\vec r\rvert^{2}\bigr),
$$

and the interval norm is the quaternionic norm,

$$
I(\tilde{Ϛ})=\langle\tilde{Ϛ}\rangle_{\natural}
=\mathrm{Sc}\bigl(\tilde{Ϛ}^{\natural}\tilde{Ϛ}\bigr)
=\tfrac{1}{4}\bigl(1-\lvert\vec r\rvert^{2}\bigr).
$$

The two are complementary on the slice:

$$
P+I=\tfrac{1}{2},
\qquad
P-I=\tfrac{1}{2}\lvert\vec r\rvert^{2}.
$$

The sum is constant because the trace is one; the difference is the purity. The half-difference is the information content:

$$
\tfrac{1}{2}\bigl(P-I\bigr)=\tfrac{1}{4}\lvert\vec r\rvert^{2}.
$$

| state | $P$ | $I$ | $P-I$ | $\tfrac{1}{2}(P-I)$ |
| --- | --- | --- | --- | --- |
| pure, $\lvert\vec r\rvert=1$ | $\tfrac{1}{2}$ | $0$ | $\tfrac{1}{2}$ | $\tfrac{1}{4}$ |
| maximally mixed, $\lvert\vec r\rvert=0$ | $\tfrac{1}{4}$ | $\tfrac{1}{4}$ | $0$ | $0$ |
| general | $\tfrac{1}{4}(1+\lvert\vec r\rvert^{2})$ | $\tfrac{1}{4}(1-\lvert\vec r\rvert^{2})$ | $\tfrac{1}{2}\lvert\vec r\rvert^{2}$ | $\tfrac{1}{4}\lvert\vec r\rvert^{2}$ |

The gap is maximal on the pure states, where the interval vanishes and the probability is one half; it vanishes at the maximally mixed element, where the two metrics agree. The gap is the **purity gap** and the interval is the mixedness. On the trace-one slice the gap is the trace purity shifted by one half,

$$
P-I=\operatorname{Tr}\bigl(\tilde{Ϛ}^{2}\bigr)-\tfrac12 ,
$$

while the trace purity is $2P=\tfrac12(1+\lvert\vec r\rvert^{2})$. The two differ by a constant on the slice: the gap is a monotone of purity, not the trace purity itself.

### The Purity Gap, Mixedness and the Two Limits

The trace of the square and the linear entropy are the same two numbers read from the other side:

$$
\mathrm{Tr}\bigl(\tilde{Ϛ}^{2}\bigr)=\tfrac{1}{2}\bigl(1+\lvert\vec r\rvert^{2}\bigr)=2P,
\qquad
S_{\mathrm{lin}}\bigl(\tilde{Ϛ}\bigr)=1-\mathrm{Tr}\bigl(\tilde{Ϛ}^{2}\bigr)
=\tfrac{1}{2}\bigl(1-\lvert\vec r\rvert^{2}\bigr)=2I .
$$

The gap is therefore $P-I=\tfrac{1}{2}-S_{\mathrm{lin}}$, and the half-gap is $\tfrac{1}{4}-\tfrac{1}{2}S_{\mathrm{lin}}$. The pure state has $S_{\mathrm{lin}}=0$ and the maximal gap; the maximally mixed element has $S_{\mathrm{lin}}=\tfrac{1}{2}$ and no gap. The purity gap is the probability metric's excess over the interval, and mixedness is the interval itself.

**The interpretation.** The probability norm is definite on the algebra; the interval is indefinite there and non-negative on the state slice. On a state their difference is the purity gap, an affine image of the trace purity; the half-difference is the information content, maximal for the pure states and vanishing at the maximally mixed element.

**The boundary.** The gap is a purity gap only on the trace-one positive slice; off it the two norms are not normalised to the same trace and the difference is not a purity. The identification with information content is the interpretation, and no entropy production, rate or dynamics is supplied.

## The Square Is the Minimal Arrow

### The Sector Crossing

The material sector is the anti-Hermitian subspace, $\mathbb{M}_-=\{\tilde Q:\tilde Q^{*}=-\tilde Q\}$. For an element of that sector the square is Hermitian:

$$
(\tilde Q^{2})^{*}=(\tilde Q^{*})^{2}=(-\tilde Q)^{2}=\tilde Q^{2}.
$$

The crossing alternates with the power:

| power | sector of $\tilde Q^{n}$ for $\tilde Q\in\mathbb{M}_-$ |
| --- | --- |
| odd | $\mathbb{M}_-$ |
| even | $\mathbb{M}_+$ |

The square is the **minimal** even power, and every even power factors through it:

$$
\tilde Q^{2k}=\bigl(\tilde Q^{2}\bigr)^{k}.
$$

The square is not the only map that crosses. The fourth power crosses, and every even power does; the Hermitian square $\tilde Q\tilde Q^{*}$ crosses for an arbitrary element, not only for a material one. What is unique is the degree: the square is the lowest crossing, and every other even power is a composite of it. The correct statement is therefore *minimal*, not *only*.

### The Weight and the Axis

Write a material four-vector in the physical coordinates,

$$
\tilde Q=ict'\,e_t+\vec x,
\qquad
\vec x=x\vec e_x+y\vec e_y+z\vec e_z .
$$

Its square and its negative are

$$
\tilde Q^{2}=-\bigl(c^{2}{t'}^{2}+\lvert\vec x\rvert^{2}\bigr)e_t+2ict'\,\vec x,
\qquad
-\tilde Q^{2}=\bigl(c^{2}{t'}^{2}+\lvert\vec x\rvert^{2}\bigr)e_t-2ict'\,\vec x .
$$

The scalar part of $-\tilde Q^{2}$ is the Hermitian norm,

$$
\mathrm{Sc}\bigl(-\tilde Q^{2}\bigr)=c^{2}{t'}^{2}+\lvert\vec x\rvert^{2}
=\langle\tilde Q\rangle_{*},
$$

the Euclidean weight of the four-vector. The vector part is

$$
\mathrm{Vect}\bigl(-\tilde Q^{2}\bigr)=-2ict'\,\vec x=-2Q_t\vec Q,
$$

the phase vector of the material element. The interval is not the square: it is the quaternionic norm,

$$
\langle\tilde Q\rangle_{\natural}=-c^{2}{t'}^{2}+\lvert\vec x\rvert^{2},
$$

and the gap between the two metrics on the material side is

$$
\langle\tilde Q\rangle_{*}-\langle\tilde Q\rangle_{\natural}=2c^{2}{t'}^{2}.
$$

The square gives the weight and the axis; the norm gives the interval.

**The square vanishes only at zero on the material sector.** If $\tilde Q^{2}=0$ then $-\tilde Q^{2}=\tilde Q\tilde Q^{*}=0$, and the positive definite Hermitian norm forces $\tilde Q=0$. The square has no nonzero kernel on $\mathbb{M}_-$, although it is not injective there: two distinct purely spatial vectors of equal length have the same square, $-\lvert\vec x\rvert^{2}e_t$. The light cone is the zero set of the interval, not of the square: a null four-vector has $\langle\tilde Q\rangle_{\natural}=0$ and $\tilde Q^{2}\neq0$ in general.

### The Arrow Reading

A material element is a process, or the generator of one; its square is a Hermitian element, an observable; the pairing of that observable with a state gives the weight. The square is the algebraic step that crosses from the process side to the observable side, and the Born rule is the normalised plain form, read as the trace pairing that reads the weight. The square names the shape of the step; the normalised plain form, read as the trace formula, supplies the probability.

The sign is the sector. On the material sector the plain square is negative semidefinite, because $\tilde Q^{2}=-\tilde Q\tilde Q^{*}$; the positive weight is the negative of the square, equivalently the Hermitian square $\tilde Q\tilde Q^{*}$. The arrow is the crossing, and the sign is the direction from which the weight is read.

**The boundary.** The Born rule is not derived from the square. The square is the minimal algebraic crossing, and the reading calls it the arrow; the trace formula remains the rule, and the identification of the crossing with the physical step from a process to a probability is the interpretation.

## The Argument Is the Geometric Phase

### The Amplitude and Its Two Parts

Let $\tilde\psi_1$ and $\tilde\psi_2$ be two spinors of the module, and let the amplitude be the band's pairing,

$$
A=\langle\tilde\psi_1,\tilde\psi_2\rangle_{*}
=\mathrm{Sc}\bigl(\tilde\psi_1\tilde\psi_2^{*}\bigr).
$$

The squared modulus is the probability of the transition, and the argument is the phase. The amplitude is a complex number; the phase is its argument, and the axis about which it turns is a property of the two rays, not of the amplitude.

Under a central phase on each spinor,

$$
\tilde\psi_1\mapsto e^{i\alpha_1}\tilde\psi_1,
\qquad
\tilde\psi_2\mapsto e^{i\alpha_2}\tilde\psi_2,
$$

the amplitude transforms as

$$
A\mapsto e^{i(\alpha_1-\alpha_2)}A .
$$

The modulus is invariant and the argument shifts by the relative phase. The phase of a pair is therefore gauge dependent: it depends on the two representatives, and only the modulus is a function of the two rays.

### The Axis of the Rotation

Two rays determine a rotation, and the rotation has an axis. In the algebra the axis is the vector part of the commutator of the two state idempotents,

$$
[\tilde\Pi_1,\tilde\Pi_2]=\tilde\Pi_1\tilde\Pi_2-\tilde\Pi_2\tilde\Pi_1
=-\tfrac{1}{2}\,\hat r_1\times\hat r_2 .
$$

The axis $\hat r_1\times\hat r_2$ is perpendicular to both Bloch vectors and is the pole of the great circle that joins them. The amplitude is a complex number and has no vector part; the axis belongs to the pair of states.

For unit spinors the modulus of the amplitude is $\cos(\theta/2)$, where $\theta$ is the angle between the two Bloch vectors, twice the angle between the rays. The argument is the phase about the axis, and the half-angle is the double cover: a rotation of the ray by $2\pi$ returns the spinor to minus itself.

**The interpretation.** The argument of the amplitude is the local phase of the pair, and the axis of the pair is the axis of the rotation carrying one ray to the other. The pair's phase is not the geometric phase: it is gauge dependent. The geometric phase is the gauge-invariant part, and it lives on a closed circuit.

### The Loop Is the Gauge-Invariant Phase

Take a closed sequence of states $\tilde\psi_1,\tilde\psi_2,\dots,\tilde\psi_n,\tilde\psi_1$ and the product of the overlaps around the loop,

$$
\Gamma=\arg\Bigl(\langle\tilde\psi_1,\tilde\psi_2\rangle_{*}
\langle\tilde\psi_2,\tilde\psi_3\rangle_{*}\cdots
\langle\tilde\psi_n,\tilde\psi_1\rangle_{*}\Bigr).
$$

Under a change of representative the factors shift by the telescoping phases $\alpha_{k}-\alpha_{k+1}$, and the product is unchanged. The loop phase is gauge invariant, and it is the Pancharatnam phase of the circuit. The connection is the imaginary part of the overlap with the derivative, its curvature is minus half the area form of the sphere, and the holonomy is minus one half of the enclosed solid angle:

$$
\Gamma=-\tfrac{1}{2}\Omega .
$$

The factor $\tfrac{1}{2}$ is the signature of the double cover, the same factor that appears in the rotor's two-to-one map and in the half-angle of the spinor.

**What the band owns and what it borrows.** The band owns the pairing and the modulus; the axis belongs to the pair of states, and the loop, the connection and the curvature belong to the phase articles. The geometric phase is the holonomy of the connection on the state space, and it is cited, not re-derived.

### The Phase Is Not a Band Element

The band has no clock element, and the phase is not one: the phase is the argument of a band value, and the axis belongs to the pair of states. Neither is an element whose square generates the phase. The band supplies the values; the composition band supplies the generator, and the state space supplies the loop.

**The boundary.** The pair phase is gauge dependent; only the loop phase is invariant. The algebra supplies no dynamics, no loop and no gauge field. The connection and the half-solid-angle rule are the owners' results.

## Limits

- **No clock element.** The band has no root of $-e_t$; the clock is imported as the parameter of a unitary family whose generator is material.
- **No derivation of the Born rule.** The pairing and the trace formula supply the weight; the identification with a frequency is the hypothesis of the informational sector.
- **The trichotomy is a grading.** The algebra fixes the three grades; the particle identification is a hypothesis, and no mass, charge or coupling is derived.
- **The purity gap is a reading.** The identity $\mathrm{Tr}(\tilde{Ϛ}^{2})=2P$ is exact on the trace-one slice, and the gap is $P-I=\mathrm{Tr}(\tilde{Ϛ}^{2})-\tfrac12$; it is the trace purity shifted by a constant, and the name information content is the interpretation.
- **The square is minimal, not unique.** Every even power crosses, and the Hermitian square crosses for every element; the square is the lowest crossing.
- **The phase is cited.** The amplitude's argument is the local phase; the gauge-invariant Pancharatnam phase is the loop holonomy, and the connection and curvature belong to their owners.

## Summary

The probability band is the general plain sesqualgebra $\tilde Q_1\star\tilde Q_2=\tilde Q_1\tilde Q_2^{*}$, and its scalar form is the positive definite Hermitian pairing. Its square is the Hermitian square, whose scalar part is $\sum_\mu\lvert Q_\mu\rvert^{2}$; its roots of $+1$ are the unitaries, its roots of $0$ are the origin alone, and its nilpotents are the parent's pure isotropic cone at index three. The band has no element of square $-e_t$: the central square is a modulus, the central imaginary squares to $+e_t$, and the clock is owned by the composition band. The causality band's type criterion shows the interval's split into a central time plane and a pure spatial part. The interval is read as a clock and the Hermitian square as a ruler: the two metrics differ by twice the squared time, and the pair is the instrument form of the no-clock theorem.

The three grades of coefficient reality are the complex, central and real species, of real dimensions eight, seven and four; the informational sector is a different real form of dimension four. On the trace-one state slice the probability norm is $P=\tfrac{1}{4}(1+\lvert\vec r\rvert^{2})$ and the interval is $I=\tfrac{1}{4}(1-\lvert\vec r\rvert^{2})$; their difference is the purity gap, the trace purity shifted by one half, and their half-difference is the information content, maximal at the pure states and zero at the maximally mixed element. The square is the minimal power that carries a material element to the informational sector, and on a material four-vector its scalar part is the Euclidean weight and its vector part the phase vector. The amplitude's argument is the local phase, and the axis of the pair is the vector part of the commutator of the two states; the gauge-invariant geometric phase is the loop holonomy, minus half the solid angle. The readings are interpretations of exact algebraic statements, and each carries the boundary that separates the algebra from the physical identification.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\tilde Q_1\star\tilde Q_2=\tilde Q_1\tilde Q_2^{*}$ | the general plain sesquilinear product, the probability band |
| $\tilde Q^{*}=\overline{\tilde Q^{\natural}}$ | the Hermitian conjugation, the star |
| $\bar{\cdot}$ | the coefficient conjugation, the bar |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\mathrm{Sc}(\tilde Q_1\tilde Q_2^{*})$ | the Hermitian form |
| $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=\mathrm{Sc}(\tilde Q_1^{\natural}\tilde Q_2)$ | the quaternionic form, the interval |
| $\langle\tilde Q\rangle_{*}$ | the Hermitian norm, the probability norm |
| $\langle\tilde Q\rangle_{\natural}$ | the quaternionic norm, the interval norm |
| $\mathbb{M}_-$, $\mathbb{M}_+$ | the anti-Hermitian and Hermitian sectors |
| $\tilde\Upsilon$ | a nilpotent of the probability band |
| $\{Q_1,Q_2,Q_3\}=Q_1Q_2^{*}Q_3$ | the ternary product of the band |
| $\tilde{Ϛ}=\tfrac{1}{2}(e_t+i\vec r)$ | a trace-one state in the Bloch form |
| $P$, $I$ | the probability norm and the interval norm on the state slice |
| $A=\langle\tilde\psi_1,\tilde\psi_2\rangle_{*}$ | the amplitude |
| $\Gamma$ | the Pancharatnam phase of a closed circuit |

## Further Reading

- [The Four General Products: Composition, Probability, Causality, Gauge](the-four-general-products-composition-probability-causality-gauge.html), for the place of the band among the four products.
- [The Eight Derived Structures: Symmetric and Antisymmetric](the-eight-derived-structures-symmetric-and-antisymmetric.html), for the GPS and GQA structures, their products, their roots and their nilpotents.
- [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html), for the state space and the trace-one slice.
- [The Bloch Ball as the Normalised Slice of the Future Light Cone](the-bloch-ball-as-the-trace-one-slice-of-the-future-light-cone.html), for the purity and the linear entropy.
- [Pancharatnam's Phase and the Polarization Sphere in Biquaternionic Form](pancharatnams-phase-and-the-polarization-sphere-in-biquaternionic-form.html), for the half-solid-angle rule.
- [The Hopf Fibration and the Biquaternion Gauge Bundle](the-hopf-fibration-and-the-biquaternion-gauge-bundle.html), for the phase fibre.
- [The Unit Group, the Cone and the Orders](the-unit-group-the-cone-and-the-orders.html), for the monoid of acting maps and the cone as the wall of reversibility.
