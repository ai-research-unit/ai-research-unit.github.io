# __The Biquaternion Space, the Group of Involutions and the Six Subspaces__

## Introduction

The biquaternion algebra is one object with eight real coordinates, and the corpus reads those coordinates as a physical dictionary. Four of them are two times, four are two spaces; the eight group into four blocks; the blocks combine into six remarkable subspaces; four involutions cut the subspaces out; and three decompositions pair the blocks. This article is the physical interpretation of that arrangement taken as a whole. It reads the dictionary as two ledgers, the six subspaces as six physical objects, the four real forms of the norm as the four signatures a physical theory can carry, the involutions as the algebra's discrete structure, and the central imaginary as the one map that exchanges the two readings.

The article owns no theorem. It states each result in a sentence, links the mathematics article that proves it, and gives the physical interpretation with its boundary.

The results used are these.

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| The algebra, its basis, its eight real coordinates and the complex structure $J:\tilde Q\mapsto i\tilde Q$ | [The Biquaternioid as a Vector Space over $\mathbb{R}$](../articles_maths/the-biquaternioid-vector-space-over-r.html), [The Biquaternioid as a Vector Space over $\mathbb{C}$](../articles_maths/the-biquaternioid-vector-space-over-c.html) |
| The involutions, the Klein four-group and the orbits of an element | [The Group of Involutions](../articles_maths/the-group-of-involutions.html) |
| The six subspaces, their bases and their defining conditions | [Introduction to the Remarkable Subspaces](../articles_maths/introduction-to-the-remarkable-subspaces.html) |
| The three decompositions of the algebra | [Decompositions Along the Remarkable Subspaces](../articles_maths/decompositions-along-the-remarkable-subspaces.html) |
| The four coordinate blocks, the intersections, the sums and the action of $J$ | [Comparison of the Remarkable Subspaces](../articles_maths/comparison-of-the-remarkable-subspaces.html) |
| The four forms, their restrictions and the alternating companion | [Remarkable Subspaces and the Four Forms](../articles_maths/remarkable-subspaces-and-the-four-forms.html) |

## The Results It Uses

### The Space

The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, of complex dimension four and real dimension eight, on the basis $e_t,\vec e_x,\vec e_y,\vec e_z$ with $\vec e_k^2=-e_t$ and $\vec e_x\vec e_y=\vec e_z$ cyclic. A general element is

$$
\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z,
$$

with complex coefficients $Q_\mu=q_\mu+iq'_\mu$. The **scalar part** is $Q_te_t$, the **vector part** is $Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$. The central imaginary $i$ commutes with the four units; multiplication by it is the real-linear map $J(\tilde Q)=i\tilde Q$, with $J^2=-\mathrm{id}$. The elements that commute with everything are the multiples of $e_t$, so the centre is the complex line $\mathbb{C}e_t$, of real dimension two, spanned by $e_t$ and $ie_t$.

The same eight real numbers can be gathered in three ways: as eight real coordinates on the eight basis elements $e_\mu,ie_\mu$; as four complex coordinates on the four $e_\mu$; or as two real quaternions on $e_t,ie_t$, since $\tilde Q=\tilde q+i\tilde q'$ with $\tilde q,\tilde q'\in\mathbb{H}$. The three writings are one object, and the physical dictionary uses the first two.

### The Physical Dictionary

The eight real parameters are named once and for all by

$$
q'_t=c\,t,\qquad (q_x,q_y,q_z)=(x,y,z),\qquad q_t=c\,t',\qquad (q'_x,q'_y,q'_z)=(x',y',z'),
$$

with $c$ the speed of light in the medium, $c=1/\sqrt{\epsilon\mu}$, and $c_0$ its vacuum value. The dictionary is displayed coefficient by coefficient.

| Coefficient | Complex | Real part | Imaginary part | Material writing | Informational writing |
| --- | --- | --- | --- | --- | --- |
| $Q_t$ | $q_t+iq'_t$ | $c\,t'$ | $c\,t$ | $ic\,t$ | $c\,t'$ |
| $Q_x$ | $q_x+iq'_x$ | $x$ | $x'$ | $x$ | $i\,x'$ |
| $Q_y$ | $q_y+iq'_y$ | $y$ | $y'$ | $y$ | $i\,y'$ |
| $Q_z$ | $q_z+iq'_z$ | $z$ | $z'$ | $z$ | $i\,z'$ |

The two ends of the table are the two coordinates of the framework,

$$
\tilde R=i c t\,e_t+x\vec e_x+y\vec e_y+z\vec e_z,\qquad \tilde Q=c t'\,e_t+i\bigl(x'\vec e_x+y'\vec e_y+z'\vec e_z\bigr),
$$

the **material coordinate**, with an imaginary time and a real space, and the **informational coordinate**, with a real time and an imaginary space.

**One element, one point, one label.** Every coefficient contributes exactly one real number to each writing, so one element of $\mathbb{B}$ carries a material four-coordinate and an informational four-coordinate at the same time. A material element is a spacetime event, $i c t\,e_t+x\vec e_x+y\vec e_y+z\vec e_z$, and the four informational parameters it also carries are its internal label; an informational element is a point $c t'\,e_t+i(x'\vec e_x+y'\vec e_y+z'\vec e_z)$ of the state side, and the four material parameters it also carries are its spacetime label. No coefficient is idle, and this is why one element can serve both as a four-vector and as a state.

**Why the material time is imaginary.** The factor $i$ in $i c t$ is what makes the temporal displacement count with the opposite sign to the spatial ones, because $i^2=-1$. With $c t$ real in the time slot the material sector would carry a Euclidean four-coordinate space and no causal cone. The Lorentzian signature is therefore a consequence of the complex structure on the time coordinate, not an independent axiom.

**The dictionary is local.** The identification of the scalar imaginary with the time direction is not rigid. In a material medium the scale $c=1/\sqrt{\epsilon\mu}$ varies from point to point, so the dictionary is local; the vacuum, $c=c_0$, is the limiting member of the family. The local freedom sits in the dictionary and not in $J$: multiplication by the central $i$ is constant, and it is the physical identification of that $i$ with time that varies.

**The anti-Hermitian convention.** The corpus takes the material sector to be the **anti-Hermitian** subspace, fixed by the reversal $\flat=-{}^{*}$, where the more familiar convention takes the Hermitian subspace as the real one. The two conventions differ by the central factor $i$ and neither is a mathematical error. The corpus fixes the anti-Hermitian one because the material sector is the fixed space of the algebra's real structure and is the space that carries the four-positions and the four-vectors. A reader who restores the Hermitian convention finds the whole dictionary inverted.

### The Involutions

Four maps act on the algebra: the complex conjugation $\bar{\cdot}$, the quaternion conjugation ${}^{\natural}$, the Hermitian conjugation ${}^{*}=\bar{\cdot}\circ{}^{\natural}$ and the reversal $\flat=-{}^{*}$. The first three, with the identity, form the Klein four-group; the reversal is not a fourth element of the group, it is minus the star.

| Map | Formula | $\mathbb{C}$-linearity | What it touches | Fixed space | Anti-fixed space |
| --- | --- | --- | --- | --- | --- |
| $\bar{\cdot}$ | $Q_\mu\mapsto\bar Q_\mu$ | antilinear | the complex scalars | $\mathbb{H}_{\mathbb{B}}$ | $i\mathbb{H}_{\mathbb{B}}$ |
| ${}^{\natural}$ | $Q_te_t-Q_k\vec e_k$ | linear | the quaternion directions | $\mathbb{C}_{\mathbb{B}}$ | $\mathrm{Vect}(\mathbb{B})$ |
| ${}^{*}=\bar{\cdot}\circ{}^{\natural}$ | $\bar Q_te_t-\bar Q_k\vec e_k$ | antilinear | both | $\mathbb{M}_+$ | $\mathbb{M}_-$ |
| $\flat=-{}^{*}$ | $-\bar Q_te_t+\bar Q_k\vec e_k$ | antilinear | both, with a sign | $\mathbb{M}_-$ | $\mathbb{M}_+$ |

Each map is an involution, so each cuts the algebra into a fixed space and an anti-fixed space. The six distinct spaces so obtained are the six remarkable subspaces. Each of the four maps preserves every remarkable subspace: no conjugation carries an element out of a subspace into another one.

The orbit of an element under the Klein four-group has size one, two or four. It is one on the real line $\mathbb{R}e_t$; it is two on the elements of $\mathbb{C}_{\mathbb{B}}$, of $\mathbb{H}_{\mathbb{B}}$ or of $\mathbb{M}_+$ that are not on that line; it is four elsewhere, and a generic material element is in that last case.

### The Six Subspaces and the Four Blocks

The eight real coordinates group into four blocks,

$$
A_1=\mathbb{R}e_t,\qquad A_2=\mathbb{R}(ie_t),\qquad B_1=\operatorname{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z\},\qquad B_2=\operatorname{span}_{\mathbb{R}}\{i\vec e_x,i\vec e_y,i\vec e_z\},
$$

two scalar blocks of dimension one and two vector blocks of dimension three. Every remarkable subspace is the sum of two blocks.

| Subspace | Blocks | Dimension over $\mathbb{R}$ | The quaternionic norm on it | Physical object |
| --- | --- | --- | --- | --- |
| $\mathbb{C}_{\mathbb{B}}$ | $A_1\oplus A_2$ | $2$ | not real | the clock plane and the global phase |
| $\mathrm{Vect}(\mathbb{B})$ | $B_1\oplus B_2$ | $6$ | not real | the complex three-vector: field strength, Lorentz generators, phase space |
| $\mathbb{H}_{\mathbb{B}}$ | $A_1\oplus B_1$ | $4$ | $(4,0)$ | the Euclidean four-coordinate space; the rotation rotors |
| $i\mathbb{H}_{\mathbb{B}}$ | $A_2\oplus B_2$ | $4$ | $(0,4)$ | the negative-definite four-coordinate space; the boost generators |
| $\mathbb{M}_+$ | $A_1\oplus B_2$ | $4$ | $(1,3)$ | the operator space: states and observables |
| $\mathbb{M}_-$ | $A_2\oplus B_1$ | $4$ | $(3,1)$ | the four-vector space: events and the interval |

Each block is the intersection of the three subspaces that contain it. Two distinct subspaces meet in the blocks they share, so an intersection has dimension zero, one or three, never two, four, five or six.

### The Three Decompositions

Each of the three involutions ${}^{\natural}$, $\bar{\cdot}$ and ${}^{*}$ splits the algebra into a fixed space and an anti-fixed space, and the two pieces are complementary.

| Involution | Decomposition | The two pairs of blocks | What the split separates | The operation that preserves it |
| --- | --- | --- | --- | --- |
| ${}^{\natural}$ | $\mathbb{B}=\mathbb{C}_{\mathbb{B}}\oplus\mathrm{Vect}(\mathbb{B})$ | $\{A_1,A_2\}$ against $\{B_1,B_2\}$ | time from space | spatial rotation |
| $\bar{\cdot}$ | $\mathbb{B}=\mathbb{H}_{\mathbb{B}}\oplus i\mathbb{H}_{\mathbb{B}}$ | $\{A_1,B_1\}$ against $\{A_2,B_2\}$ | the definite from the anti-definite | phase conjugation |
| ${}^{*}$ | $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$ | $\{A_1,B_2\}$ against $\{A_2,B_1\}$ | the informational from the material | Lorentz transformation |

There are exactly three, because a four-element set has exactly three pairings into two pairs.

### The Forms

The algebra carries four scalar-valued forms, one for each choice of conjugation in the two slots: the plain form $\langle\tilde Q_1,\tilde Q_2\rangle$, the quaternionic form $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}$, the Hermitian form $\langle\tilde Q_1,\tilde Q_2\rangle_{*}$ and the Krein form $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}$. Each has a real part and an imaginary part on a subspace. The imaginary part, for the two sesquilinear forms, is alternating; it is the **area pairing**.

The area pairing is non-degenerate exactly on the complex time sector, of rank $2$, and on the complex space sector, of rank $6$. It vanishes on the real sector, on the imaginary sector and on both physical sectors. The reason is one line: the pairing joins each direction to its partner under multiplication by $i$, and it is available exactly on the subspaces that contain both members of the pair.

## Interpretations

### The Eight Coordinates Are Two Clocks and Two Spaces

The dictionary gives every one of the eight coordinates the dimension of a length. The two times are $c t'$ and $c t$, the two spaces are $x,y,z$ and $x',y',z'$. This is why the central imaginary can exchange the two ledgers without a dimensional mismatch: the exchange is a quarter turn in a plane whose two axes carry the same dimension.

| Direction | Element contribution | Physical interpretation |
| --- | --- | --- |
| $e_t$ | $c t'$ | the informational time |
| $i e_t$ | $i c t$ | the material time |
| $\vec e_x,\vec e_y,\vec e_z$ | $x,y,z$ | the material space |
| $i\vec e_x,i\vec e_y,i\vec e_z$ | $i x',i y',i z'$ | the informational space |

The two times are one complex coordinate, $z=c t'+i c t$, and the two spaces are one complex vector, $x\vec e_x+y\vec e_y+z\vec e_z+i(x'\vec e_x+y'\vec e_y+z'\vec e_z)$. The first is the **clock plane**: one real axis is the clock of the informational sector, the other the clock of the material one, and the central imaginary turns one into the other. The second is the **complex space**: three real directions and their three imaginary partners.

The reading of the imaginary directions is the delicate one. In the sector dictionary the block $B_2$ is the **informational space**, the partner of the material space. In the phase-space reading of the complex space sector the same block is the **momentum half** of a configuration–momentum pair: the real direction carries the configuration and its imaginary partner carries the conjugate momentum. The two readings are of one block, and they must not be conflated. What both have in common is the algebraic fact that an imaginary direction is a direction the pairing uses, not a direction in which anything propagates; the Fourier reading of the same fact is that the imaginary axis is where the conjugate variable sits.

**The boundary.** The dictionary is a naming of the coordinates, and the names *material* and *informational* are the corpus's convention. It does not derive the existence of an informational sector of the world; that is the hypothesis stated and bounded in *The Informational Sector: States, Observables and Probability*. The identification of $B_2$ with momentum belongs to the phase-space reading of the complex space sector, not to the sector dictionary.

### The Six Subspaces Are Six Physical Objects

The six subspaces are not six arbitrary slices. Each is the fixed or anti-fixed space of one involution and the sum of two coordinate blocks, and each carries a definite physical structure.

| Subspace | Physical object | What it carries |
| --- | --- | --- |
| $\mathbb{C}_{\mathbb{B}}$ | the clock plane | the two times on one complex axis; the global phase; the energy–time pair |
| $\mathrm{Vect}(\mathbb{B})$ | the complex three-vector | the electromagnetic field strength, the six Lorentz generators, the phase space of a spatial direction |
| $\mathbb{H}_{\mathbb{B}}$ | the Euclidean four-coordinate space | the Wick-rotated reading; the rotation rotors |
| $i\mathbb{H}_{\mathbb{B}}$ | the negative-definite four-coordinate space | the material time with the informational space; the boost generators |
| $\mathbb{M}_+$ | the operator space | states, observables, probability |
| $\mathbb{M}_-$ | the four-vector space | events, four-vectors, the interval |

**The complex time sector is the clock plane.** Its two coordinates are the two times, $c t'$ on the real axis and $i c t$ on the imaginary one, and its element is $z e_t=(c t'+i c t)e_t$. It is the sector of a number rather than of an operator: a central scalar is the one quantity that can take a definite value at the same time as every other, and its phase $\exp(i\theta)e_t$ is a global phase that no interference experiment can detect. The area pairing has rank $2$ here, and its one non-zero entry pairs the two times. This is a different object from the global phase, and the two must not be conflated: the phase is a number, the area pairing is what makes the two times conjugate.

**The complex space sector is the complex three-vector.** Its six real directions carry the three material directions and their three informational partners. Multiplication by $i$ acts inside the sector as the **duality rotation** of the complex three-vector, which is the electric–magnetic duality of the field strength; the three real directions generate the rotations and the three imaginary ones the boosts, so one complex three-vector is at once a field configuration and the generator of the transformations that act on it. In the phase-space reading the same sector is $T^*\mathbb{R}^3$: the real direction is the configuration, the imaginary partner the momentum, and the area pairing of rank $6$ is the symplectic form. **The boundary:** this is the kinematic phase space; the Hamiltonian is not supplied by the algebra, and the identification of the imaginary partner with momentum is the fixed complex structure, not a dynamical Legendre transform.

**The real sector is the Euclidean four-coordinate space.** Its four coefficients are real, so the $ict$ writing is unavailable inside it: its element is $c t'\,e_t+x\vec e_x+y\vec e_y+z\vec e_z$, the norm is positive definite of signature $(4,0)$, there is no null direction and no light cone, and no direction is singled out as time. This is the Euclidean, or Wick-rotated, reading of the four-vector space, and it is the home of the rotation rotors, whose action is the rotation of the material space with the two-to-one cover of $SO(3)$. **The boundary:** it is not the physical spacetime, because its time is $c t'$ and its space is real; it is the Euclidean reading, not the Minkowski one.

**The imaginary sector is the negative-definite four-coordinate space.** Every coefficient carries the central imaginary, and its element is $i c t\,e_t+i(x'\vec e_x+y'\vec e_y+z'\vec e_z)$. It carries the material time with the informational space, the reverse assignment to the real sector, and its norm is negative definite of signature $(0,4)$. It is where the infinitesimal generators of the boosts lie, the three imaginary vector units. **The boundary:** a finite boost does not lie in the sector, because its scalar part is real; the sector holds the generators, and the boosts themselves are obtained by leaving it.

**The two sectors** are the two halves of the Hermitian split. The material sector $\mathbb{M}_-$ is the space of four-vectors and the interval, and the informational sector $\mathbb{M}_+$ is the space of states and observables. Each has its own article in this category, *The Material Sector: Four-Vectors, Interval and Lorentz Action* and *The Informational Sector: States, Observables and Probability*, and this article only places them in the table.

### The Four Real Forms Are the Four Signatures

The quaternionic norm is one complex quadratic form, and the four four-dimensional subspaces are its four real restrictions. The signature depends only on which real slice is taken.

| Subspace | Blocks | Norm on the subspace | Signature | Reading |
| --- | --- | --- | --- | --- |
| $\mathbb{H}_{\mathbb{B}}$ | $A_1\oplus B_1$ | $q_t^2+q_x^2+q_y^2+q_z^2$ | $(4,0)$ | Euclidean |
| $i\mathbb{H}_{\mathbb{B}}$ | $A_2\oplus B_2$ | $-\bigl((q'_t)^2+(q'_x)^2+(q'_y)^2+(q'_z)^2\bigr)$ | $(0,4)$ | anti-Euclidean |
| $\mathbb{M}_-$ | $A_2\oplus B_1$ | $-c^2t^2+x^2+y^2+z^2$ | $(3,1)$ | Lorentzian |
| $\mathbb{M}_+$ | $A_1\oplus B_2$ | $c^2t'^2-x'^2-y'^2-z'^2$ | $(1,3)$ | anti-Lorentzian |

The two definite slices are the two coefficient halves; the two indefinite slices are the two physical sectors. The Lorentzian signature of the material sector is not an independent axiom: it is what the norm becomes on the slice that carries the $i$ in the time slot, and the sign of the time direction is the sign of $i^2$. The light cone is the zero set of that form, and the causal structure is the sign of the form.

**The boundary.** The signature does not by itself select matter rather than information. It selects a real form, and the identification of one indefinite slice with matter and the other with information is the corpus's convention. A reader who swaps the two indefinite slices obtains the mirrored convention, not a different algebra.

### The Three Decompositions Are Three Questions

The three decompositions answer three different questions about the same eight coordinates. *Which part is time and which is space?* is the scalar-vector decomposition. *Which part is definite and which indefinite?* is the real-imaginary decomposition. *Which part is material and which informational?* is the Hermitian decomposition.

The three are not independent splits. They are the three ways of cutting the four blocks into two pairs, and a four-element set has no fourth. Each is also the split preserved by one basic operation of the framework: a spatial rotation preserves the scalar-vector split, a phase conjugation preserves the real-imaginary split, and a Lorentz transformation preserves the Hermitian split. The physical content is that the question *which half is the real one?* has exactly three answers — the centre, the real-coefficient half or the Hermitian half — and the framework chooses one of them. The choice is a convention; the consistency it forces is not.

**The boundary.** An element has a component in each pair of each decomposition, and the three readings of one element are simultaneous, not alternatives. A statement that uses two decompositions at once must say which component it means, or it will mix a temporal part with a definite part.

### The Involutions Are the Discrete Structure

Each of the four maps preserves every remarkable subspace, so the involutions act inside each physical object rather than moving it to another object. The three involutions with the identity form the Klein four-group, and its orbit on an element has size one, two or four.

| Map | Action on a central phase | Action on the vector directions | Physical shape |
| --- | --- | --- | --- |
| $\bar{\cdot}$ | $\theta\mapsto-\theta$ | none | phase conjugation |
| ${}^{\natural}$ | none | $\vec v\mapsto-\vec v$ | spatial reflection |
| ${}^{*}$ | $\theta\mapsto-\theta$ | $\vec v\mapsto-\vec v$ | the combined operation; self-adjointness |
| $\flat=-{}^{*}$ | a sign and a phase reflection | fixes the real vector directions | the real structure |

The orbit is the set of descriptions that the discrete operations produce from one element. Size one is the real line: the classical scale, on which no discrete operation acts. Size two is an element of the centre, of $\mathbb{H}_{\mathbb{B}}$ or of $\mathbb{M}_+$: one operation is invisible on it, so two of the four descriptions coincide. For a central element $z$ the pair is $z$ and $\bar z$. Size four is the generic element, and a generic material element is in this class: the four descriptions are distinct.

**The boundary.** The size of the orbit is not the size of a multiplet, and it carries no statistics. The assignment of parity, time reversal and charge conjugation to three of the four sign patterns is a separate labelling, and it is not a consequence of the group structure. The next section states it.

### The Klein Four Carries the Discrete Labels

The four involutions act on the four coordinate blocks, and each block is a joint eigenspace of the group: every involution acts on it by a sign. The four sign patterns that arise are the four characters of the Klein four. The blocks are ordered $A_1,A_2,B_1,B_2$: the informational time, the material time, the material space and the informational space.

| map | sign pattern $(A_1,A_2,B_1,B_2)$ | fixed space |
| --- | --- | --- |
| $1$ | $(+,+,+,+)$ | $\mathbb{B}$ |
| $\bar{\cdot}$ | $(+,-,+,-)$ | $\mathbb{H}_{\mathbb{B}}$ |
| ${}^{\natural}$ | $(+,+,-,-)$ | $\mathbb{C}_{\mathbb{B}}$ |
| ${}^{*}$ | $(+,-,-,+)$ | $\mathbb{M}_+$ |
| $\flat=-{}^{*}$ | $(-,+,+,-)$ | $\mathbb{M}_-$ |

The first four rows are the group; the fifth is the fourth non-trivial sign pattern, the negative of ${}^{*}$, and it is not a group element. The labels are read on those four non-trivial sign patterns:

- **Parity $P$ is ${}^{\natural}$.** It fixes both times and negates both spaces. On the material four-vector $ict\,e_t+x\,\vec e_x+y\,\vec e_y+z\,\vec e_z$ it keeps the time and reverses the space. It is $\mathbb{C}$-linear, which is the algebraic form of the unitarity of parity.
- **Time reversal $T$ is $\bar{\cdot}$.** On the material sector it negates the material time $A_2$ and fixes the material space $B_1$. It is antilinear, which is the algebraic form of the anti-unitarity of time reversal.
- **The full reflection $PT$ is ${}^{*}$.** It negates the material time and the material space, so it sends $x^{\mu}\mapsto-x^{\mu}$.
- **Charge conjugation is $\flat=-{}^{*}$.** It fixes the material sector and negates the informational one. It is a sign pattern and not a group element, which is the algebraic statement that $C$ does not join $\{1,P,T,PT\}$ as an independent factor but is the sign that turns $PT$ into its negative.

**Three corrections belong with the table.** First, $\flat$ is the fourth non-trivial **sign pattern**, not a fourth conjugation: it differs from ${}^{*}$ by the central sign, and the group has four elements and not five. Second, $\flat$ carries the **shape** of the charge-conjugation pairing; the operation called charge conjugation is the twisted map $\bar A=\Pi A^{*}\Pi^{-1}$, whose module real structure is $\bar{\cdot}$, and the four levels of the name are tabulated in *Antilinear Structure and the Two Kinds of Mass in Biquaternionic Form*. Third, parity exchanges the two conjugate spinor modules $S$ and $\bar S$, so the character label and the chirality action are not independent.

**The second dictionary.** The Clifford-algebra literature attaches the names to the same maps in the transpose order: with the generators $i\vec e_k$, the grade involution is $\bar{\cdot}$, the reversion is ${}^{*}$ and the Clifford conjugation is ${}^{\natural}$, so that dictionary reads $P=\bar{\cdot}$, $T={}^{*}$ and $PT={}^{\natural}$. Both dictionaries are labelled and neither is proved. The table is the fact; the naming is the interpretation, and the interpretation above is the one whose parity fixes time and negates space.

**The boundary.** The assignment is a labelled speculation, not a theorem. It is offered because it makes the four characters carry four physical names and because the linearity of each map matches the linearity of the symmetry it names. It does not derive the discrete symmetries, their conservation or their violation.

### The Central Imaginary Is One Generator with Four Names

Multiplication by $i$ is one map, and its restrictions to the subspaces carry four names.

| Subspace | Action of $J$ | Name |
| --- | --- | --- |
| $\mathbb{C}_{\mathbb{B}}$ | itself | the global phase |
| $\mathrm{Vect}(\mathbb{B})$ | itself | the duality rotation |
| $\mathbb{H}_{\mathbb{B}}$ and $i\mathbb{H}_{\mathbb{B}}$ | each other | the Wick rotation |
| $\mathbb{M}_+$ and $\mathbb{M}_-$ | each other | the material–informational exchange |

One generator gives a phase, a duality rotation, a Wick rotation and a sector exchange, because the generator is central and acts through the centre in every subspace. A non-central generator would give a different rotation in each carrier.

$J$ is invertible, so it is not a measurement and not a collapse. It reverses the sign of the two bilinear norms, $N(J\tilde Q)=-N(\tilde Q)$, so it is not an isometry of the interval. The exchange of the sectors is a change of writing of one element, not a process that converts matter into information. The local speed $c=1/\sqrt{\epsilon\mu}$ makes the physical identification of the time direction local, while $J$ remains the constant central imaginary.

**The boundary.** The four names are four readings of one map, not four independent operations. The exchange does not by itself give a dynamics or a coupling, and the equality $N(J\tilde Q)=-N(\tilde Q)$ is the reason the two sectors carry one quadratic form with opposite signs.

### The Intersections Are the Shared Objects

Two subspaces meet in the blocks they share, and each shared block is one physical object that two descriptions have in common.

| Intersection | Shared block | The common object |
| --- | --- | --- |
| $\mathbb{H}_{\mathbb{B}}\cap\mathbb{M}_-$ | $B_1$ | the real space |
| $\mathbb{H}_{\mathbb{B}}\cap\mathbb{M}_+$ | $A_1$ | the real time |
| $\mathbb{C}_{\mathbb{B}}\cap\mathbb{M}_-$ | $A_2$ | the material time |
| $\mathrm{Vect}(\mathbb{B})\cap\mathbb{M}_+$ | $B_2$ | the informational space |
| $\mathbb{M}_+\cap\mathbb{M}_-$ | $\{0\}$ | nothing: an element is material or informational, never both |

The table lists one row for each of the four blocks; every other intersection is zero. The pattern is the dictionary's grammar. A shared vector block has dimension three: two descriptions agree on a space. A shared scalar block has dimension one: they agree on a time. An empty intersection means the two descriptions are complementary, and the decomposition they form is a decomposition of the whole algebra. The three decompositions are the three complementary pairs, and their sums are all of $\mathbb{B}$.

**The boundary.** An intersection is a subspace of elements, not a set of physical objects. A shared time is one direction, not one clock reading; the two sectors carry different coordinates on the central time plane, $c t'$ and $i c t$.

### The Area Pairing Marks the Complex Sectors

The four forms are the scalar parts of the four products. On a subspace each form has a real part and an imaginary part, and the imaginary part of the two sesquilinear forms is alternating: it is the area pairing. The pairing is non-degenerate exactly on the complex time sector, of rank $2$, and on the complex space sector, of rank $6$; it vanishes on the real sector, on the imaginary sector and on both physical sectors.

The reason is the one already stated. The pairing joins each direction to its partner under multiplication by $i$. The complex time sector contains both times, so it has one pair to join; the complex space sector contains the three material directions and their three partners, so it has three; the real and imaginary sectors contain one member of each pair and never both; and the two physical sectors are exchanged by $i$, so no pair lies inside either. This is the sharpest algebraic sense in which the two physical sectors are phase-free.

The physical reading is a division of labour. The area pairing is the **symplectic form** of the phase plane and of the phase space: on the complex time sector it pairs the two times, on the complex space sector it pairs each spatial direction with its conjugate partner, and its primitive is the action. The physical sectors carry the **metric** and the **probability**, which are symmetric pairings, and no area. The two roles are distinct, and the complex sectors are where the area lives.

**The boundary.** The vanishing statement concerns the **scalar-valued** alternating part of the form. The **vector-valued** antisymmetric half of the product is not zero on a physical sector; on the informational sector it is the coherence, and it has its own article. A sector without an area pairing is not a sector without an antisymmetric structure. The area pairing is a property of the restriction of a form; it does not add a dynamics.

### The Relations Table Is an Index

The intersection table says which two subspaces share a block. Read as an index, it answers a prior question: **where can a proposed interpretation be posed at all?** A composition needs a subspace on which the product closes; an observable needs a subspace on which the Hermitian form is real; a state needs a subspace on which positivity makes sense; a gauge generator needs a subspace on which the bracket closes. The table does not supply those structures; it says which subspace carries which.

The three decompositions say which objects a change of frame acts on and which it keeps. Read together with the table, they give the grammar of the category: before asking what an object means, ask which subspace it lives in and which operation preserves that subspace. That is why the relations article is the reference table of the category, and why an interpretation that names a subspace without naming the operation that keeps it has not yet been posed.

**The boundary.** The index is a statement of where a question is well posed, not an answer to it. A subspace that carries a product does not thereby carry a dynamics, and a subspace that carries a form does not thereby carry a measurement.

## Limits

The article interprets the linear structure, the involutions and the real forms. It does not interpret the product, the cone, the topology or the analysis of the algebra; each belongs to another article of the category. The physical names are the coordinate dictionary of the corpus. The conventions article records which of them are forced and which are chosen, and the choice of the anti-Hermitian half as the material sector is a convention that the whole series inherits. The physical realisation of the informational sector is a hypothesis, stated and bounded in its own article. The discrete labels are a labelled speculation and add no theorem.

## Summary

- The eight real coordinates are two times and two spaces, grouped in four blocks: $A_1,A_2$ scalar and $B_1,B_2$ vector.
- The material sector is the imaginary time with the real space; the informational sector is the real time with the imaginary space.
- The six subspaces are six physical objects: the clock plane, the complex three-vector, the Euclidean four-space, the negative-definite four-space, the operator space and the four-vector space.
- The four four-dimensional subspaces are the four real forms of one quadratic form, of signatures $(4,0)$, $(0,4)$, $(3,1)$ and $(1,3)$; the two sectors are the two indefinite forms.
- The Lorentzian signature follows from the placement of $i$, not from an axiom.
- The three decompositions are the three pairings of the four blocks, and there is no fourth.
- The three involutions, with the identity, form a Klein four-group; they preserve every subspace and have orbits of size one, two or four.
- The four sign patterns on the coordinate blocks are its four characters; parity, time reversal and $PT$ are three of them, and $\flat=-{}^{*}$ is the fourth non-trivial pattern, the shape of charge conjugation and not a group element.
- The intersection table is an index of where an interpretation can be posed: the subspace names the object and the operation that preserves it names the question.
- Multiplication by $i$ is one map with four names: global phase, duality rotation, Wick rotation and sector exchange.
- The area pairing is non-degenerate exactly on the two complex sectors, of rank $2$ and rank $6$, and vanishes on the four others.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra, of real dimension eight |
| $Q_\mu=q_\mu+iq'_\mu$ | a complex coefficient, with real and imaginary parts |
| $J(\tilde Q)=i\tilde Q$ | the complex structure, $J^2=-\mathrm{id}$ |
| ${}^{\natural}$, $\bar{\cdot}$, ${}^{*}=\bar{\cdot}\circ{}^{\natural}$ | quaternion, complex and Hermitian conjugation |
| $\flat=-{}^{*}$ | the reversal, outside the Klein four |
| $\mathbb{C}_{\mathbb{B}}$, $\mathrm{Vect}(\mathbb{B})$ | the centre and the vector subspace |
| $\mathbb{H}_{\mathbb{B}}$, $i\mathbb{H}_{\mathbb{B}}$ | the quaternion and anti-quaternion subspaces |
| $\mathbb{M}_+$, $\mathbb{M}_-$ | the Hermitian and anti-Hermitian subspaces |
| $A_1,A_2$ | the scalar blocks $\mathbb{R}e_t$ and $\mathbb{R}(ie_t)$ |
| $B_1,B_2$ | the real and imaginary vector blocks |
| $c t'$, $i c t$ | the informational and material times |
| $N(\tilde Q)=\langle\tilde Q\rangle_{\natural}$ | the quaternionic norm |

## Further Reading

- [The Biquaternioid as a Vector Space over $\mathbb{R}$](../articles_maths/the-biquaternioid-vector-space-over-r.html) and [The Biquaternioid as a Vector Space over $\mathbb{C}$](../articles_maths/the-biquaternioid-vector-space-over-c.html), for the space, its basis and its complex structure.
- [The Group of Involutions](../articles_maths/the-group-of-involutions.html), for the Klein four-group, its subgroups and its orbits.
- [Introduction to the Remarkable Subspaces](../articles_maths/introduction-to-the-remarkable-subspaces.html), for the six subspaces one by one.
- [Decompositions Along the Remarkable Subspaces](../articles_maths/decompositions-along-the-remarkable-subspaces.html) and [Comparison of the Remarkable Subspaces](../articles_maths/comparison-of-the-remarkable-subspaces.html), for the three decompositions, the coordinate blocks and the intersection table.
- [Remarkable Subspaces and the Four Forms](../articles_maths/remarkable-subspaces-and-the-four-forms.html), for the restrictions of the forms and the area pairing.
- *Conventions in the Biquaternion Universe*, for the coordinate dictionary and the choice of the material sector.
- *The Material Sector: Four-Vectors, Interval and Lorentz Action* and *The Informational Sector: States, Observables and Probability*, for the two sectors.
