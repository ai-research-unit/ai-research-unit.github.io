# __The Algebraic Vocabulary: Element, Conjugations, Six Subspaces and Two Ledgers__

## Introduction

This entry reads the first section of the mathematical category: the algebra, the element, the four conjugations, the six subspaces, the square, the cone and the roots. Seven mathematics articles establish those objects. This entry states what they establish, once, and then gives the physical readings.

The section is the vocabulary of the whole category. Every later entry names an element, a subspace or a conjugation, and every physical name the corpus uses — material, informational, interval, observable, massless, invertible — is fixed here or nowhere. That is why the entry is long and why it comes first.

The single idea is that one element carries two ledgers. The eight real coordinates group into two times and two space triples. On one grouping the element is a spacetime event; on the other it is a state-side label. Both readings are of the same element, and neither is an approximation of the other. Everything else in the section — the involutions, the subspaces, the square, the cone — is the structure that makes the two readings consistent.

## The Source Table

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| the algebra as a tensor product, the basis, the multiplication table, associativity, the unit, the centre | [Introduction to the Algebra of Biquaternions](../articles_maths/introduction-to-the-algebra-of-biquaternions.html) |
| the general element, the three coordinate writings, the scalar–vector split, the four conjugations, the real form, the central complex structure | [The Element, the Coordinates and the Conjugations in the Biquaternion Algebra](../articles_maths/the-element-the-coordinates-and-the-conjugations-in-the-biquaternion-algebra.html) |
| the two conjugations, the Klein four-group, the three splittings, the orbits, the sign-twisted adjoint | [The Group of Involutions of the Biquaternion Algebra](../articles_maths/the-group-of-involutions-of-the-biquaternion-algebra.html) |
| the six remarkable subspaces, the four coordinate blocks, the three decompositions, and why there are exactly three | [Subspaces and Decompositions of the Biquaternion Algebra](../articles_maths/subspaces-and-decompositions-of-the-biquaternion-algebra.html) |
| the square, its two parts, the central square, the square-zero elements, the isotropic cone | [The Square of an Element in the Biquaternion Algebra](../articles_maths/the-square-of-an-element-in-the-biquaternion-algebra.html) |
| the two annihilators, the zero divisors, the invertibles and the criterion that separates them | [Zero Divisors and Invertibles in the Biquaternion Algebra](../articles_maths/zero-divisors-and-invertibles-in-the-biquaternion-algebra.html) |
| the reduction of the root problem, the classification of roots, the three central values | [The Square Roots of a General Element in the Biquaternion Algebra](../articles_maths/the-square-roots-of-a-general-element-in-the-biquaternion-algebra.html) |

The algebra comes first, then the element that inhabits it, then the maps that cut it, then the pieces the maps produce, then the two operations that are read: the square and the root.

## The Results in Brief

### The Algebra and the Element

**The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, of complex dimension four and real dimension eight.** The basis is $e_t,\vec e_x,\vec e_y,\vec e_z$, with $\vec e_k^2=-e_t$ and $\vec e_x\vec e_y=\vec e_z$ cyclic. The product is associative, has the unit $e_t$, and is not commutative. The centre is the complex line $\mathbb{C}e_t$, of real dimension two, spanned by $e_t$ and $ie_t$.

A general element and its three writings.

$$
\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z=\vec q+i\vec q'=\tilde q+i\tilde q' ,
$$

with $Q_{\imath}=q_{\imath}+iq'_{\imath}$. The first writing is four complex coordinates on the four units; the second is eight real coordinates on the eight basis elements $e_{\imath},ie_{\imath}$; the third is two real quaternions. The **scalar part** is $Q_te_t$, the **vector part** is $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$, and the **complex length** of the vector part is $B$, with

$$
B^2=Q_x^2+Q_y^2+Q_z^2=(\vec Q,\vec Q) .
$$

The quaternionic norm is the sum of the four squares.

$$
N(\tilde Q)=\langle\tilde Q\rangle_{\natural}=\sum_{\imath} Q_{\imath}^2=Q_t^2+B^2 .
$$

It is a complex quadratic form, not a positive one, and its vanishing is a condition and not a wall.

Multiplication by the central $i$ is a real-linear map. Write $J(\tilde Q)=i\tilde Q$. Then $J^2=-\mathrm{id}$ and $J$ commutes with everything, because $i$ is central. Applying $J$ twice reverses the sign of both bilinear norms, $\langle J\tilde Q\rangle_{\natural}=-\langle\tilde Q\rangle_{\natural}$.

### The Four Conjugations and the Klein Four

Four maps act on the algebra.

| map | formula | $\mathbb{C}$-linearity | fixed space | anti-fixed space |
| --- | --- | --- | --- | --- |
| $\bar{\cdot}$ | $Q_{\imath}\mapsto\bar Q_{\imath}$ | antilinear | $\mathbb{B}_{H}$ | $\mathbb{B}_{iH}$ |
| ${}^{\natural}$ | $Q_te_t-\sum_{k\in\{x,y,z\}} Q_k\vec e_k$ | linear | $\mathbb{B}_{C}$ | $\mathbb{B}_{V}$ |
| ${}^{*}=\bar{\cdot}\circ{}^{\natural}$ | $\bar Q_te_t-\sum_{k\in\{x,y,z\}}\bar Q_k\vec e_k$ | antilinear | $\mathbb{B}_{\Psi}$ | $\mathbb{B}_{\Phi}$ |
| $\flat=-{}^{*}$ | $-\bar Q_te_t+\sum_{k\in\{x,y,z\}}\bar Q_k\vec e_k$ | antilinear | $\mathbb{B}_{\Phi}$ | $\mathbb{B}_{\Psi}$ |

**The first three, with the identity, form a Klein four-group.** The fourth is not a group element: it is minus the third. Each map is an involution, so each cuts the algebra into a fixed space and an anti-fixed space, and the six distinct spaces so obtained are the six subspaces of the next subsection. Each of the four maps preserves every one of them.

The orbit of an element under the group has size one, two or four. Size one is the real line $\mathbb{R}e_t$. Size two is an element of $\mathbb{B}_{C}$, of $\mathbb{B}_{H}$ or of $\mathbb{B}_{\Psi}$ that is not on that line. Size four is the generic case.

### The Six Subspaces and the Four Blocks

The eight coordinates group into four blocks.

$$
A_1=\mathbb{R}e_t,\qquad A_2=\mathbb{R}(ie_t),\qquad B_1=\operatorname{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z\},\qquad B_2=\operatorname{span}_{\mathbb{R}}\{i\vec e_x,i\vec e_y,i\vec e_z\} .
$$

Two scalar blocks of dimension one and two vector blocks of dimension three. Every remarkable subspace is the sum of two blocks.

| subspace | defining condition | blocks | $\dim_{\mathbb{R}}$ | inertia of $N$ |
| --- | --- | --- | --- | --- |
| $\mathbb{B}_{C}$ | $\tilde Q^{\natural}=\tilde Q$ | $A_1\oplus A_2$ | $2$ | complex-valued |
| $\mathbb{B}_{V}$ | $\tilde Q^{\natural}=-\tilde Q$ | $B_1\oplus B_2$ | $6$ | complex-valued |
| $\mathbb{B}_{H}$ | $\bar{\tilde Q}=\tilde Q$ | $A_1\oplus B_1$ | $4$ | $(4,0)$ |
| $\mathbb{B}_{iH}$ | $\bar{\tilde Q}=-\tilde Q$ | $A_2\oplus B_2$ | $4$ | $(0,4)$ |
| $\mathbb{B}_{\Psi}$ | $\tilde Q^{*}=\tilde Q$ | $A_1\oplus B_2$ | $4$ | $(1,3)$ |
| $\mathbb{B}_{\Phi}$ | $\tilde Q^{*}=-\tilde Q$ | $A_2\oplus B_1$ | $4$ | $(3,1)$ |

**Two of the six are complex subspaces and four are real-type.** The complex subspaces are stable under $J$; the real-type ones are not, since $J$ carries each of them to its complement.

Two distinct subspaces meet in a block or in zero. An intersection therefore has dimension zero, one or three.

### The Three Decompositions

Each of ${}^{\natural}$, $\bar{\cdot}$ and ${}^{*}$ splits the algebra into a fixed and an anti-fixed part.

| involution | decomposition | what the split separates | the operation that preserves it |
| --- | --- | --- | --- |
| ${}^{\natural}$ | $\mathbb{B}=\mathbb{B}_{C}\oplus\mathbb{B}_{V}$ | the scalar blocks from the vector blocks | spatial rotation |
| $\bar{\cdot}$ | $\mathbb{B}=\mathbb{B}_{H}\oplus\mathbb{B}_{iH}$ | the definite from the anti-definite | phase conjugation |
| ${}^{*}$ | $\mathbb{B}=\mathbb{B}_{\Psi}\oplus\mathbb{B}_{\Phi}$ | the Hermitian from the anti-Hermitian | Lorentz transformation |

**There are exactly three, and no fourth.** A four-element set of blocks has exactly three pairings into two pairs.

### The Square

The square is the one operation the entry reads twice. With $\tilde Q=Q_te_t+\vec Q$,

$$
\boxed{\;\tilde Q^2=\bigl(Q_t^2-B^2\bigr)e_t+2Q_t\vec Q\;}.
$$

The vector part of the square is a complex multiple of the vector part of the element, so squaring does not turn the direction. The square is central exactly when $Q_t=0$ or $\vec Q=0$. And $\vec Q^2=-B^2e_t$, so the square of a pure element is central and negative.

**The isotropic cone is the set $B^2=0$.** In real coordinates it is the pair of equations

$$
(\vec q,\vec q)=(\vec q',\vec q'),\qquad (\vec q,\vec q')=0 ,
$$

two real equations in six real coordinates, hence a cone of real dimension four. The square-zero elements are its pure points, $Q_t=0$ and $B^2=0$.

### The Zero Divisors and the Invertibles

The non-zero elements split into two classes, and one complex number decides which.

$$
\tilde Q\ \text{is invertible}\iff Q_t^2+B^2\neq0,\qquad \tilde Q\ \text{is a zero divisor}\iff Q_t^2+B^2=0 .
$$

The criterion is the norm. Since $N(\tilde Q)=Q_t^2+B^2$, a non-zero element is invertible exactly when its norm is non-zero. The invertibles are the complement of the zero-divisor set, and that set is a complex cone of real dimension six, with the pure family as its subcone of real dimension four.

**The criterion is not a normalisation.** The complex length alone does not decide: $e_t+\vec e_x+i\vec e_y$ has $B^2=0$ and is invertible. The sum is what decides.

### The Square Roots

Every element falls into exactly one row.

| condition on $\tilde Q$ | number of roots |
| --- | --- |
| $\vec Q\neq0$, $(\vec Q,\vec Q)\neq0$, $n\neq0$ | four |
| $\vec Q\neq0$, $(\vec Q,\vec Q)\neq0$, $n=0$ | two |
| $\vec Q\neq0$, $(\vec Q,\vec Q)=0$, $Q_t\neq0$ | two |
| $\vec Q\neq0$, $n=0$, $Q_t=0$ | none |
| $\vec Q=0$ | a four-parameter family |

The generic case is four roots, and the roots come in pairs $\pm\tilde Z$. The complex square of the vector part decides whether a solution is lost at zero; the conjugate scalar $n$ decides whether the two solutions of the reduced quadratic are distinct. A complex scalar has the two scalar roots together with a four-real-parameter family of pure roots on a quadric.

**The three central values reproduce the degenerate cases.** The roots of $-e_t$ are the roots of $-1$, the roots of $0$ are the nilpotents, and the roots of $+e_t$ are the non-trivial roots of $+1$.

## The Interpretations

Twelve readings, each labelled, each with its boundary. They are grouped as the results are: the coordinates, the ledgers, the inertia, the subspaces and their intersections, the involutions, the square, the cone and the roots.

### I.1.a — The Eight Coordinates Are Two Clocks and Two Spaces

Read: the eight real coefficients are four lengths and four more lengths. Two of them are times, $h_t$ and $r'_t$; the other six are two space triples, $(r_x,r_y,r_z)$ and $(h'_x,h'_y,h'_z)$.

Why they can be exchanged at all. Every coefficient carries the dimension of a length, so the central $i$ can swap a time for a space and a space for a time without a dimensional mismatch. The exchange is a quarter turn in a plane whose two axes carry the same unit. An algebra whose coefficients carried different dimensions could not have a central complex structure at all.

The boundary. The identification of one time with $h_t$ and the other with $r'_t$ is a naming, and the names carry the sector each time belongs to. Nothing in the algebra distinguishes the two times before the corpus chooses which block is material.

### I.1.b — One Element, Two Ledgers

Read: every element is a spacetime event and a state-side label at the same time. The material coordinate is

$$
\tilde R_\Phi=i r'_t\,e_t+r_x\vec e_x+r_y\vec e_y+r_z\vec e_z ,
$$

an imaginary time and a real space. The informational element is

$$
\tilde H_\Psi=h_t\,e_t+i\bigl(h'_x\vec e_x+h'_y\vec e_y+h'_z\vec e_z\bigr) ,
$$

a real time and an imaginary space. The element is their sum, $\tilde Q=\tilde H_\Psi+\tilde R_\Phi$, and each part is the other's label.

**The two ledgers are the two projections of one element, not two elements.** The split is the Hermitian split, so it is exact and linear: the projections $\tfrac12(\tilde Q\pm\tilde Q^{*})$ recover the two parts, and no information is lost in either direction. A reader who reads the element as an event does not discard the state label; he reads one projection and calls the other the label of the event.

The boundary. The two ledgers do not split the norm. The quadratic form is complex bilinear, so

$$
N(\tilde H_\Psi+\tilde R_\Phi)=N(\tilde H_\Psi)+N(\tilde R_\Phi)+2i\bigl(h_tr'_t+\vec h'\cdot\vec r\bigr) ,
$$

and the cross term is generally non-zero. The interval of an element is not the sum of the intervals of its two parts, and an argument that treats the two ledgers as independent contributions to one invariant is wrong.

### I.1.c — The Imaginary Time Is the Sign Pattern

Read: the factor $i$ in $i r'_t$ is what makes the temporal displacement count with the opposite sign to the spatial ones, because $i^2=-1$. The Lorentzian sign pattern of the material sector is therefore not an independent axiom. It is what the norm becomes on the slice that carries the central $i$ in its time slot.

The four inertias are one form on four slices.

$$
\mathbb{B}_{H}:(4,0),\qquad \mathbb{B}_{iH}:(0,4),\qquad \mathbb{B}_{\Psi}:(1,3),\qquad \mathbb{B}_{\Phi}:(3,1) .
$$

The two definite slices are the two coefficient halves; the two indefinite slices are the two sectors. A causal cone exists on a slice exactly when the slice's inertia is indefinite, and the cone's opening is the sign of the time direction.

The boundary. The inertia does not by itself select matter rather than information. It selects a real slice. The identification of one indefinite slice with matter and the other with information is the corpus's convention, and a reader who swaps them obtains the mirrored convention and not a different algebra.

### I.1.d — The Six Subspaces Are Six Physical Objects

Read: each subspace is a physical object, and the pairing with its defining involution is what makes the object well posed.

| subspace | physical name | the object |
| --- | --- | --- |
| $\mathbb{B}_{C}$ | the complex time sector | the clock plane: two times, one global phase, and no operator |
| $\mathbb{B}_{V}$ | the complex space sector | the complex three-vector: three material directions with three informational partners |
| $\mathbb{B}_{H}$ | the real sector | the Euclidean four-coordinate space, the home of the rotation rotors |
| $\mathbb{B}_{iH}$ | the imaginary sector | the negative-definite four-coordinate space, the home of the boost generators |
| $\mathbb{B}_{\Psi}$ | the informational sector | the operator space: the states and the observables |
| $\mathbb{B}_{\Phi}$ | the material sector | the four-vector space: the events, the interval and the light cone |

**The centre is not the global phase.** The centre has two real dimensions, $e_t$ and $ie_t$. A central element $z e_t$ is a number and takes a definite value at the same time as everything else; its phase is a global phase that no interference experiment detects. The area pairing has rank two on the centre and pairs the two times, which is a different structure from the phase; its definition, and its rank on all six subspaces, is in I.7.

The complex space sector holds an object and its generators at once. Its three real directions generate the rotations and its three imaginary ones the boosts, so the same six-dimensional carrier holds a field configuration and the generators of the transformations that act on it. This is the reason the sector is complex and not real: it is the one space on which a field and its symmetry algebra are the same space.

The boundary. The sector names are forced by the involutions; the identification of one indefinite sector with matter is chosen. The real and imaginary sectors are the two definite readings of the same four-vector space, and neither is a spacetime: no null direction exists on them, so no light cone does.

### I.1.e — The Three Decompositions Are Three Questions

Read: the three splits of the algebra answer three different questions about one set of eight coordinates.

| decomposition | the question | the answer |
| --- | --- | --- |
| scalar–vector | which part is time and which is space? | $\mathbb{B}_{C}$ and $\mathbb{B}_{V}$ |
| real–imaginary | which part is definite and which indefinite? | $\mathbb{B}_{H}$ and $\mathbb{B}_{iH}$ |
| Hermitian | which part is material and which informational? | $\mathbb{B}_{\Phi}$ and $\mathbb{B}_{\Psi}$ |

**Each split is preserved by exactly one basic operation.** A spatial rotation preserves the scalar–vector split, a phase conjugation preserves the real–imaginary split, a Lorentz transformation preserves the Hermitian split. The three splits are therefore not three conventions of taste: each is the invariant decomposition of one transformation group.

The boundary. The three readings of one element are simultaneous, not alternatives. A sentence that uses two decompositions at once must say which component it means, or it mixes a temporal part with a definite part.

### I.1.f — The Involutions Are the Discrete Labels

Read: the three group elements and the fourth map carry the four discrete names.

| map | sign pattern on $(A_1,A_2,B_1,B_2)$ | physical name |
| --- | --- | --- |
| $1$ | $(+,+,+,+)$ | the identity |
| ${}^{\natural}$ | $(+,+,-,-)$ | parity $P$: fixes both times, negates both spaces |
| $\bar{\cdot}$ | $(+,-,+,-)$ | time reversal $T$: negates the material time, fixes the material space |
| ${}^{*}$ | $(+,-,-,+)$ | the full reflection $PT$ |
| $\flat=-{}^{*}$ | $(-,+,+,-)$ | charge conjugation $C$: fixes the material sector, negates the informational one |

The linearity matches the symmetry. Parity is $\mathbb{C}$-linear, which is the algebraic form of the unitarity of parity. Time reversal is antilinear, which is the algebraic form of its anti-unitarity. The match is the content of the table: the two facts are the same fact.

**Charge conjugation is not a fourth group element.** It is minus the third, so it is not a character of the group and there is no fourth factor. The algebra therefore says something specific: $C$ does not join $\{1,P,T,PT\}$ as an independent factor. It is the sign that turns $PT$ into its negative.

The orbit is a set of descriptions, not a set of states. The four maps act on one element, so they produce at most four descriptions of it, and the size of the orbit is the number of them that are distinct. Size one is the real line $\mathbb{R}e_t$: no discrete map moves it, which is the reason the central real scale is the one object with a single description. Size two is an element that one non-identity map cannot see, so two of the four descriptions coincide, and the central case $z$ and $\bar z$ is the clean one. Size four is the generic element, and the sectors are in that class: $\mathbb{B}_{V}$, $\mathbb{B}_{iH}$ and $\mathbb{B}_{\Phi}$ all have orbit four, so a sector element carries four distinct descriptions.

The size is a count of descriptions and not of objects. An orbit of size four is four describings of one element and not four elements, and the count carries no statistics. It is not the $2s+1$ of a multiplet, which counts the states of a carrier; the two numbers arise from two different actions and must not be identified.

The boundary. The assignment is a labelled interpretation and not a theorem. It is offered because it makes four maps carry four physical names and because the linearity of each map matches the linearity of the symmetry it names. It does not derive the discrete symmetries, their conservation or their violation, and a second dictionary — the one used in the Clifford-algebra literature — attaches the names in the transpose order. Both are labelled and neither is proved.

### I.1.g — The Central Imaginary Is One Generator with Four Names

Read: multiplication by $i$ is one map, and its restriction to each subspace carries a different name.

| subspace | action of $J$ | physical name |
| --- | --- | --- |
| $\mathbb{B}_{C}$ | itself | the global phase |
| $\mathbb{B}_{V}$ | itself | the duality rotation: electric for magnetic |
| $\mathbb{B}_{H}$ and $\mathbb{B}_{iH}$ | each other | the Wick rotation |
| $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{\Phi}$ | each other | the material–informational exchange |

One generator gives four operations because it is central. It acts through the centre in every subspace, so its restriction is the same map in all of them up to the name. A non-central generator would give a different rotation in each carrier, and the four names would be four unrelated operations.

The boundary. $J$ is invertible, so it is not a measurement and not a collapse. It reverses the sign of the two quadratic norms, so it is not an isometry of the interval. The exchange of the sectors is a change of writing of one element and not a process that converts matter into information; the corpus gives it no dynamics and no coupling.

### I.1.h — The Square Is the Clock and the Norm Is the Interval

Read: two different invariants are read from one element, and the two are read by two different operations.

For a material element $\tilde R_\Phi=i r'_t\,e_t+\vec r$ with $\vec r$ real, the norm and the scalar part of the square are

$$
N(\tilde R_\Phi)=-{r'_t}^{2}+\lvert\vec r\rvert^{2},\qquad \operatorname{Sc}\bigl(\tilde R_\Phi^{2}\bigr)=-\bigl({r'_t}^{2}+\lvert\vec r\rvert^{2}\bigr) .
$$

**The norm is the Lorentzian interval; the square is minus the Euclidean length.** The norm keeps the difference of the two squares and the square keeps their sum, so the two invariants read the same four numbers in the two geometries the algebra carries. The material sector is the one the norm measures; the real sector is the one the square measures.

The vector part of the square is a sweep. On the material sector $2Q_t\vec Q=2ir'_t\vec r$: the spatial displacement, carried into the informational ledger, scaled by twice the elapsed material time. Squaring therefore takes a displacement and returns the same direction swept over the interval and written in the other ledger.

The boundary. The identification holds for an element whose coefficients are a coordinate in the physical dictionary. For a general element $N$ is complex and neither reading applies. And the square is not the interval under any convention: no choice of branch turns $-(r'^2+\lvert\vec r\rvert^2)$ into $-r'^2+\lvert\vec r\rvert^2$.

### I.1.i — The Square of a Sector Element Is an Observable

Read: the square of an element of either sector lies in the informational sector.

The proof is one line. The star reverses a product, so $(\tilde Q^2)^{*}=(\tilde Q^{*})^2$. If $\tilde Q^{*}=\tilde Q$ the square is fixed; if $\tilde Q^{*}=-\tilde Q$ the square is $(-\tilde Q)^{2}=\tilde Q^{2}$, which is also fixed. Either way $\tilde Q^{2}\in\mathbb{B}_{\Psi}$.

**The material sector is therefore not closed under squaring, and the informational one is.** For a material element the square is $-({r'_t}^{2}+\lvert\vec r\rvert^{2})e_t+2ir'_t\vec r$, with a real scalar part in $A_1$ and an imaginary vector part in $B_2$: the two blocks of $\mathbb{B}_{\Psi}$. The asymmetry is exact and it is not a convention.

The boundary. "Observable" here means only Hermitian, which is what the informational sector is. The statement says nothing about which Hermitian element a measurement realises, and it supplies no expectation value; that belongs to the entry on the state space.

### I.1.j — The Cone Is the Horizon of Reversibility

Read: the zero-divisor set is the set of elements that cannot be undone, and the norm decides membership. An element is invertible exactly when $N\neq0$ and is a zero divisor exactly when $N=0$, so

$$
\boxed{\;\text{invertible}\iff N\neq0,\qquad \text{zero divisor}\iff N=0\;}.
$$

Invertibility is a norm condition and not a normalisation. This is the vocabulary the whole category uses: an element is regular when its norm is non-zero, and degenerate when the norm vanishes, and the two classes are the two sides of one cone. On the material sector that cone is the light cone, because $N=-{r'_t}^{2}+\lvert\vec r\rvert^{2}$; there the horizon of reversibility and the causal horizon are the same set.

The two families behave differently. A pure zero divisor annihilates itself on both sides and squares to zero; a non-pure one does not square to zero, its two annihilators are distinct planes, and its conjugate is the line they share. A product with a zero divisor is never an invertible element, so reaching the cone is irreversible: multiplication cannot leave it.

The boundary. On the informational sector the same cone is not a causal horizon. Its unit-weight slice bounds the state space and that boundary is the set of pure states. One set, two readings, and the entry says which one it is using.

### I.1.k — The Roots Are the Mass Shell and the Frame

Read: the root set of a value is the level set of the norm, and on the material sector that level set is the mass shell.

The generic case is the interesting one for physics. Four roots, in two pairs $\pm\tilde Z$. The two pairs are the two branches of the square root, and the freedom between them is a choice of frame and not a choice of physics. The rows with two roots are the degenerate values, the row with no roots is a value that the algebra refuses to halve, and the four-parameter family is the freedom a complex scalar leaves open.

**The rootless row is exact and it matters.** An element with $\vec Q\neq0$, $(\vec Q,\vec Q)=0$ and $Q_t=0$ has no square root at all. It is a pure element on the isotropic cone, and it is the case in which no half-angle exists. A corpus that assumes a square root always exists would be wrong on a set of real dimension four.

The boundary. The root of an element is not a mass. The mass reading is an extra identification, licensed on the four-momentum chart, and it makes the mass the modulus of the polar word rather than the root itself. The algebra is scale-free: it supplies the level set and no number.

### I.1.l — The Intersections Are the Shared Objects

Read: every intersection of two distinct subspaces is one block or zero, and a block that two subspaces share is one object that the two descriptions have in common.

| intersection | shared block | the common object |
| --- | --- | --- |
| $\mathbb{B}_{H}\cap\mathbb{B}_{\Phi}$ | $B_1$ | the material space |
| $\mathbb{B}_{H}\cap\mathbb{B}_{\Psi}$ | $A_1$ | the informational time |
| $\mathbb{B}_{C}\cap\mathbb{B}_{\Phi}$ | $A_2$ | the material time |
| $\mathbb{B}_{V}\cap\mathbb{B}_{\Psi}$ | $B_2$ | the informational space |
| $\mathbb{B}_{\Psi}\cap\mathbb{B}_{\Phi}$ | $\{0\}$ | nothing: no non-zero element is both material and informational |

The first four rows are one representative for each block and the fifth is a complementary pair. All fifteen pairs of distinct subspaces meet in one of the four blocks or in zero, so the table is the whole of the intersection structure.

**A shared space is agreement on a space, and a shared time is agreement on a time.** A shared vector block has dimension three, so two descriptions that contain it agree on a whole space; a shared scalar block has dimension one, so they agree on one direction of time. An empty intersection is the complementarity the decompositions are built on, and the three empty pairs are exactly the three decompositions, whose sums are all of $\mathbb{B}$.

The boundary. An intersection is a subspace and not a collection of physical objects. A shared time is one direction and not one clock reading: the two sectors carry different coordinates on the central plane, $h_t$ and $i r'_t$, and the shared block says only that both descriptions use that axis.

## The Limits

The entry reads the linear structure and the two operations. It does not read the product's full table, the spectrum, the norms beyond their definitions, the topology or the analysis. Each belongs to a later entry, and each entry that uses a result from this one links back to it.

The physical names are those of the corpus's conventions. The choice of the anti-Hermitian half as the material sector is a convention, inherited by the whole series; a reader who restores the Hermitian convention finds the entire dictionary inverted and nothing else changed.

**Two readings are labelled and not proved.** The assignment of $P$, $T$, $PT$ and $C$ to the four maps, and the identification of one sector with matter rather than information, are conventions with a stated reason. The entry marks them every time it uses them.

## Summary

- The section establishes seven objects: the algebra, the element, the four conjugations, the six subspaces, the square, the cone and the roots.
- One element carries two ledgers, the material four-coordinate and the informational label, and the two are its Hermitian projections. The norm does not split between them.
- The Lorentzian sign pattern follows from the placement of the central $i$ in the time slot of one sector, not from an independent axiom.
- The six subspaces are the fixed and anti-fixed spaces of four maps; three of those maps with the identity form a Klein four-group and carry $P$, $T$, $PT$; the fourth carries $C$ and is not a group element.
- There are exactly three decompositions, one for each pairing of the four coordinate blocks.
- Every intersection of two distinct subspaces is one block or zero: a shared vector block is agreement on a space, a shared scalar block agreement on a time, and the three empty pairs are the three decompositions.
- The orbit of an element under the Klein group has size one, two or four, and the size counts distinct descriptions: one on $\mathbb{R}e_t$, two when one map is invisible, four on the generic element and on both sectors.
- The square of an element of either sector is Hermitian, so the material sector is not closed under squaring.
- The norm separates the invertibles from the zero divisors: $N\neq0$ is invertibility and $N=0$ is the cone. On the material sector that cone is the light cone.
- On the material sector the norm is the interval and the square's scalar part is minus the Euclidean length: two geometries, one element.
- Every element has four roots, two or none, by the classification; the root set of a value is the level set of the norm.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra, complex dimension four, real dimension eight |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | the quaternion basis |
| $i$ | the central imaginary unit, $i^2=-1$ |
| $J(\tilde Q)=i\tilde Q$ | multiplication by the central unit, $J^2=-\mathrm{id}$ |
| $\tilde Q=Q_te_t+\vec Q$ | the scalar–vector split, $Q_{\imath}=q_{\imath}+iq'_{\imath}$ |
| $B^2=(\vec Q,\vec Q)=Q_x^2+Q_y^2+Q_z^2$ | the complex length squared of the vector part |
| $N(\tilde Q)=\langle\tilde Q\rangle_{\natural}=Q_t^2+B^2$ | the quaternionic norm |
| $\bar{\cdot}$, ${}^{\natural}$, ${}^{*}$, $\flat=-{}^{*}$ | complex, quaternion, Hermitian and anti-Hermitian conjugation |
| $A_1,A_2,B_1,B_2$ | the four coordinate blocks: informational time, material time, material space, informational space |
| $\mathbb{B}_{C},\mathbb{B}_{V},\mathbb{B}_{H},\mathbb{B}_{iH},\mathbb{B}_{\Psi},\mathbb{B}_{\Phi}$ | the six remarkable subspaces |
| $\tilde R_\Phi=ir'_te_t+\vec r$ | the material coordinate |
| $\tilde H_\Psi=h_te_t+i\vec h'$ | the informational element |

## Further Reading

In the mathematics corpus. The seven articles of the source table, and [The Spectrum](../articles_maths/the-spectrum-of-a-biquaternion.html) for the eigenvalue pair $\lambda_\pm=Q_t\pm iB$, which this entry names and does not read.

In this category. The entries that take up what this one states in brief are [The AXF Matrices: Axis-Free, Integer Entries](the-axf-matrices-axis-free-integer-entries.html) and [The Pauli Pair and the Gamma Frame: Which Statements Survive Conjugation](the-pauli-pair-and-the-gamma-frame-which-statements-survive-conjugation.html) for the two displays, [Idempotents, Ideals and Observables](idempotents-ideals-and-observables.html) for the idempotents and the Peirce corners, [The Spectrum and the Two Modes](the-spectrum-and-the-two-modes.html) for the eigenvalue pair and the two predicates, [The N Norm: Mass, Angle and the Cone](the-n-norm-mass-angle-and-the-cone.html) for the norm, [Four-Vectors and the Interval](four-vectors-and-the-interval.html) for the real slice and its metric, and [States, Observables and the Born Weight](states-observables-and-the-born-weight.html) for the Hermitian slice and the weight.

The sources of this entry. The two predicates and the modes, [The Spectrum and the Two Modes](the-spectrum-and-the-two-modes.html); the square-zero element and the cone, [The Vacuum and the Nilpotent Ladder](the-vacuum-and-the-nilpotent-ladder.html); the partition of the invertibility cut, [The Partition: Two Invariants and Four Regimes](the-partition-two-invariants-and-four-regimes.html).

The conventions. [Conventions in the Biquaternion Universe](algebra-and-element-conventions.html) records which of the physical names are forced by the algebra and which are chosen.
