# __The Two Sectors: Split and the Four Bridges__

## Introduction

The biquaternion algebra splits into the eigenspaces of Hermitian conjugation,

$$
\mathbb{B}=\mathbb{M}_-\oplus\mathbb{M}_+,\qquad
\mathbb{M}_\pm=\{\tilde Q:\tilde Q^{*}=\pm\tilde Q\},
$$

and the two summands are the material and the informational sectors of the framework. The preceding articles give each sector its physics. This one asks the question that neither of them owns: which operations of the algebra couple the two sectors, and which do not.

The answer has two halves. The **conjugations** — the identity, coefficient conjugation, quaternion conjugation and Hermitian conjugation — never cross the split, and neither does any observable. A small set of operations that are not conjugations couples the two sectors: the norm square, multiplication by the central $i$, the action of a Hermitian rotor, and the off-sector scalar part. The first half is rigidity and the second is coupling, and the two are not in tension. They are statements about different classes of operation.

The article is a catalogue in the genre of the subspace and obstruction catalogues. Every entry is owned by a mathematics article, linked in the table below, and the entry records the kind of the bridge and its boundary. The article owns no theorem and derives no dynamics.

## The Results It Uses

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| The sectors as the eigenspaces of Hermitian conjugation, their bases and dimensions | [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](../articles_maths/the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html) |
| The four conjugations as a Klein four-group, their commutativity and their fixed spaces | [The Group of Involutions](../articles_maths/the-group-of-involutions.html) |
| The norm, its multiplicativity and the identity $\tilde Q^{\natural}\tilde Q=\langle\tilde Q\rangle_{\natural}e_t$ | [Quaternionic Norm Regularity and Degeneracy in the Biquaternion Algebra](../articles_maths/quaternionic-norm-regularity-and-degeneracy-in-the-biquaternion-algebra.html) |
| The four general products and their behaviour on the sectors | [The Four General Products and Their Relations over the Biquaternion Algebra](../articles_maths/the-four-general-products-and-their-relations-over-the-biquaternion-algebra.html), [The Four General Products and Their Relations over the Biquaternion Algebra](../articles_maths/the-four-general-products-and-their-relations-over-the-biquaternion-algebra.html) |
| The sandwich by a Hermitian rotor and the adjoint action | [Two-Sided Operators on the General Plain Sesqualgebra](../articles_maths/two-sided-operators-on-the-general-plain-sesqualgebra.html), [Biquaternion Rotations and Lorentz Transformations](../articles_maths/biquaternion-rotations-and-lorentz-transformations.html) |

## The Split

### The Two Eigenspaces

Every biquaternion decomposes uniquely into a Hermitian and an anti-Hermitian part:

$$
\tilde Q=\tfrac12(\tilde Q+\tilde Q^{*})+\tfrac12(\tilde Q-\tilde Q^{*}),\qquad
\tfrac12(\tilde Q\pm\tilde Q^{*})\in\mathbb{M}_\pm .
$$

With $\tilde Q=z_0e_t+z_1\vec e_x+z_2\vec e_y+z_3\vec e_z$, the condition $\tilde Q^{*}=\tilde Q$ reads $z_0=\bar z_0$ and $z_k=-\bar z_k$: a real scalar and three imaginary vector coefficients. The informational sector therefore has the real basis $\{e_t,i\vec e_x,i\vec e_y,i\vec e_z\}$, and the material sector, with the opposite signs, has $\{ie_t,\vec e_x,\vec e_y,\vec e_z\}$. Each is four-real-dimensional.

Two properties of the split are used throughout.

- **It is a real subspace, not a complex one.** The sector $\mathbb{M}_+$ is closed under real linear combinations but not under multiplication by $i$: the element $i\vec e_x$ is Hermitian, and $i(i\vec e_x)=-\vec e_x$ is anti-Hermitian. Multiplication by $i$ exchanges the sectors, and no nontrivial complex subspace lies inside one of them.
- **It is not an ideal decomposition.** The product of two material elements need not be material. For $\tilde R_k=ict'_k+\vec v_k$ with real $t'_k$ and real $\vec v_k$,

$$
\tilde R_1\tilde R_2=\bigl(-c^2t'_1t'_2-(\vec v_1,\vec v_2)\bigr)
+i\bigl(ct'_1\vec v_2+ct'_2\vec v_1\bigr)+\vec v_1\times\vec v_2 .
$$

The first two terms are Hermitian and the last is anti-Hermitian, so the product has a Hermitian part and an anti-Hermitian part; it lies in a sector only when one of them vanishes, and in general it lies in neither. The split is a decomposition of the space, not of the algebra.

The second property is the reason the coupling question exists. If the sectors were ideals, every product would stay in its sector and there would be nothing to catalogue.

The centre does not supply a central decomposition. A central element $ze_t$ is Hermitian for real $z$ and anti-Hermitian for imaginary $z$, so the **real** centre splits along the sectors: $\mathbb{R}e_t\subset\mathbb{M}_+$ and $i\mathbb{R}e_t\subset\mathbb{M}_-$. A general central element is the sum of one part in each, so the complex centre straddles the split and supplies no complex central projection. The split is a real-structure grading, not a central projection, and this is the algebraic fact behind the superselection interpretation at the end.

### The Computational Split Is Not the Physical Split

The algebra also carries the **computational split** into its real and imaginary halves: every element is $q+i q'$ with $q,q'\in\mathbb{H}$, and the product respects the parity — even times even is even, even times odd is odd, odd times odd is even. This is a $\mathbb{Z}_2$ grading of the algebra, and it is the split a component calculation uses when it separates real and imaginary coefficients.

The **sector split** is a different structure. It is the eigenspace decomposition of the involution ${}^{*}$, and it is not a grading: the product of two material elements is not material. It is the split that carries the superselection rule, and its two halves are the physical sectors.

The two cannot be aligned. A sector would have to be homogeneous under the computational grading if the two splits agreed, but $\mathbb{M}_+$ contains the even element $e_t$ and the odd element $i\vec e_x$, and $\mathbb{M}_-$ contains the even element $\vec e_x$ and the odd element $i e_t$. Multiplication by $i$ is odd for the computational grading and exchanges the two sectors, so it relates the two structures without making them one. The four intersections are all nonzero — the real scalar line, the real vector subspace, the imaginary vector subspace and the imaginary scalar line — so neither split refines the other. A computation may use the real and imaginary parts, but the physical statement must use the sector split; the two $\mathbb{Z}_2$ structures are distinct, and multiplication by $i$ is the map that shows it.

**The boundary.** The computational split is a grading of the algebra over the real form; the sector split is a real-structure decomposition with a superselection reading. Neither is an ideal decomposition, and the caution is against reading a real/imaginary bookkeeping as the physical split.

### The Conjugations Preserve the Split

**Check.** Each of the four conjugations $1,\bar{\cdot},{}^{\natural},{}^{*}$ maps each sector into itself, and so does the real structure $\flat=-{}^{*}$. A sector is defined by the sign of the adjoint, and every conjugation commutes with ${}^{*}$: the four maps form the Klein four-group, and ${}^{*}={}^{\natural}\circ\bar{\cdot}$. For $c$ in that group and $\tilde Q\in\mathbb{M}_-$,

$$
c(\tilde Q)^{*}=c(\tilde Q^{*})=c(-\tilde Q)=-c(\tilde Q),
$$

so $c(\tilde Q)$ is again material. The argument for $\mathbb{M}_+$ is the same with the opposite sign, and $\flat$ inherits the property because $\flat(\tilde Q)=-{}^{*}\tilde Q$ and ${}^{*}$ commutes with every $c$.

The check is exact and it is narrow. It says that no operation built from the conjugations crosses the split. It says nothing about operations of another type, and the four couplings below are the other operations the corpus uses.

A numerical check makes the narrowness visible. Take $\tilde R=2ie_t+3\vec e_x$. Its adjoint is $-2ie_t-3\vec e_x=-\tilde R$, as it should be, and every conjugation of it stays anti-Hermitian. But the product $\tilde R\tilde R=-4e_t-9e_t+12i\vec e_x= -13e_t+12i\vec e_x$ is Hermitian, and $i\tilde R=-2e_t+3i\vec e_x$ is Hermitian as well. Neither operation is a conjugation, and both cross.

## The Four Kinds

A **bridge** is an operation that couples the two sectors: it either carries an element across the split or acts from one sector on the other. The catalogue contains four kinds — a map, a bijection, an action and a pairing — and one representative of each. The four are not four instances of one construction: each has its own domain, target and boundary.

### A Map: the Norm Square

For every biquaternion the quaternion conjugate multiplies to a central value:

$$
\boxed{\;\tilde Q^{\natural}\tilde Q=\langle\tilde Q\rangle_{\natural}e_t,\qquad
\langle\tilde Q\rangle_{\natural}=\sum_{\mu}Q_\mu^{2}\;}.
$$

For a material element $\tilde R=ict'+x\vec e_x+y\vec e_y+z\vec e_z$ the value is

$$
\langle\tilde R\rangle_{\natural}=-c^2{t'}^2+x^2+y^2+z^2,
$$

which is real and therefore lies in the informational sector. The norm square

$$
\tilde R\longmapsto\tilde R^{\natural}\tilde R=\langle\tilde R\rangle_{\natural}e_t
$$

is a map $\mathbb{M}_-\to\mathbb{M}_+$ with image the real scalar line $\mathbb{R}e_t$.

**Interpretation.** The norm square is the interval, and the interval is a value of the informational sector. The bridge is the minimal one the product supplies: a process is sent to the scalar that measures it, and no further structure is used. For $\tilde R=2ie_t+3\vec e_x$ the interval is $-4+9=5$, and the bridge sends the element to $5e_t$. A lightlike element is sent to $0$: the zero-divisor cone lies in the kernel of the bridge.

**Boundary.** The map is not an evolution, and the bare product of two material elements does not share its property: unless the spatial parts are parallel, the product carries both a Hermitian part and a material rotation part. The norm square is the coupling; the product is not. The same formula applied to an informational element returns $h_t^2-\lvert\vec h\rvert^2$, which is the determinant of the matrix of the state and not a probability. The map lands in the informational sector because its value is a scalar, not because every value is a weight.

**Remark (preparation).** The same map run backwards prepares a state. For a material element $\tilde R$, the element $\tilde H=-\tfrac{i}{2}\tilde R$ is Hermitian, with $\operatorname{Tr}\tilde H=ct'$ and $\langle\tilde H\rangle_{\natural}=-\tfrac14\langle\tilde R\rangle_{\natural}$. On the trace-one slice of the future cone it is a state of the Bloch ball. The map is a dictionary of preparation, not a dynamics, and it is a second instance of the map kind rather than a fifth kind.

### A Bijection: the Central Imaginary

The central scalar is anti-Hermitian, $i^{*}=-i$. For every $\tilde Q$,

$$
\boxed{\;(i\tilde Q)^{*}=\tilde Q^{*}i^{*}=-i\tilde Q^{*}\;},
$$

so multiplication by $i$ flips the sign of the adjoint and with it the sector: $i\mathbb{M}_+=\mathbb{M}_-$ and $i\mathbb{M}_-=\mathbb{M}_+$. The map is a bijection of the algebra, of order four, and it reverses the norm, $\langle i\tilde Q\rangle_{\natural}=-\langle\tilde Q\rangle_{\natural}$.

**Interpretation.** The two sectors are the two time directions, and the exchange reads one time against the other. Multiplication by $i$ is the relational clock: the quarter turn is the tick, and each sector is the other's clock.

**Boundary.** The exchange is invertible and periodic. It supplies no arrow by itself, because an arrow needs a non-invertible operation, and those live in the acting monoid, not in the central scalar. The map is also a bijection of the whole algebra and not a map of one sector onto the other only: it exchanges them.

### The Central Scalar as a Background Value

The centre is the complex line $\mathbb{C}e_t$, and the one number the whole algebra shares is the complex coefficient $z$ in $ze_t$. Read as a classical value, $ze_t$ is the framework's candidate for a **background field value**: it is the number the whole algebra shares, its phase $e^{i\alpha}=z/|z|$ is a gauge choice and not an observable, and it is what the complex time, the energy and the global phase have in common.

The algebra limits what such a value can be. The centre is a field, $\mathbb{C}e_t$, and has no nontrivial idempotent; a central value can therefore be a scalar expectation and not a projector. It cannot supply a central projection that would split the algebra, and it cannot break spontaneously: a symmetry-breaking order parameter would need a nontrivial central idempotent or a degenerate family of central values, and the centre has neither.

**The boundary.** The reading names a $c$-number value, not an operator and not an order parameter. The phase of the central scalar is a gauge choice; only a relative phase or a modulus is observable. No Higgs mechanism, no symmetry-breaking scale and no dynamics are derived here; the centre is minimal, and the value is a background of the framework, not a field with a potential.

### An Action: the Rotor

A unit-norm Hermitian element $\tilde U\in\mathbb{M}_+$ acts on the algebra by the sandwich. For $\tilde R\in\mathbb{M}_-$,

$$
(\tilde U\tilde R\tilde U^{*})^{*}=\tilde U\tilde R^{*}\tilde U^{*}
=-\tilde U\tilde R\tilde U^{*},
$$

because $(\tilde U^{*})^{*}=\tilde U$ and $\tilde R^{*}=-\tilde R$. The result is material: the action preserves the sector it acts on. The computation uses only the involution, so the congruence $\tilde Q\mapsto\tilde U\tilde Q\tilde U^{*}$ preserves both sectors for every invertible $\tilde U$, not only for the rotors; the restriction to the unit-norm slice is what makes it a frame change.

**Interpretation.** The informational sector supplies the boosts of the material sector. A Hermitian rotor is a boost, the sandwich is the change of frame, and the material element is the object transformed. The bridge is an action of one sector on the other, not a map between them; the frame and the object remain in their own sectors.

The Hermitian rotors are the boosts. A rotor with an imaginary vector part, $\cosh(\eta/2)+i\sinh(\eta/2)\vec e_x$, has unit norm, is Hermitian, and its sandwich mixes the time and the spatial components. A rotation rotor is a real quaternion, $\cos(\theta/2)+\sin(\theta/2)\vec e_z$; it is unitary but not Hermitian, it is not an element of $\mathbb{M}_+$, and its sandwich rotates the spatial part while fixing the time axis.

The rotation's sandwich preserves both sectors, as every congruence does; what it does not do is supply its parameter from $\mathbb{M}_+$. The distinction is the origin of the parameter and not the destination of the image: the boost is generated by an element of the informational sector, the rotation by an element of the material one. The Cartan exponents sharpen the same statement. The logarithm of the Hermitian factor is $\ln\tilde H=\ln r\,e_t+i\tfrac{\psi}{2}\vec u_{\mathrm b}\in\mathbb{M}_+$, and the logarithm of the unitary factor is $\ln\tilde U=i\alpha e_t+\tfrac{\theta}{2}\vec u_{\mathrm r}\in\mathbb{M}_-$: the boost generator is informational, while the rotation and the central phase are both material generators. The split is of the logarithms and not of the factors, because $\tilde U$ is unitary and not an element of $\mathbb{M}_-$. By the polar decomposition, a general unit-norm rotor is the product of a boost and a rotation, so its action composes a bridge with a motion that is not one.

**Boundary.** Only the unit-norm elements are rotors. The general element of $\mathbb{M}_+$ acts by a sandwich that is a congruence rescaling the interval and not an isometry, and the full action theory belongs to the geometry block, not here.

### A Pairing: the Off-Sector Scalar

For $\tilde R=ict'+\vec v\in\mathbb{M}_-$ and $\tilde H=h_te_t+i\vec h\in\mathbb{M}_+$, with real $t'$, $\vec v$, $h_t$ and $\vec h$, the scalar part of the plain product is

$$
\boxed{\;\operatorname{Sc}(\tilde R\tilde H)
=i\bigl(ct'\,h_t-(\vec v,\vec h)\bigr)\;}.
$$

It is purely imaginary, and it is a pairing $\mathbb{M}_-\times\mathbb{M}_+\to i\mathbb{R}$: it reads one element of each sector and returns a phase.

**Interpretation.** The pairing is the Minkowski pairing of the material four-vector $(ct',\vec v)$ with the informational four-vector $(h_t,\vec h)$, multiplied by $i$: the time components pair with the time component, the spatial components with the spatial components, and the indefiniteness of the interval is the relative sign. The result is a phase, not a probability. The norm reads the same two pairs with the opposite spatial sign: its cross term is $2i(ct'\,h_t+\vec v\cdot\vec h)$. The product squares the units and the norm squares the coefficients, and the sign of the spatial term is the difference.

**Boundary.** A pairing is not a product: it produces no element of either sector and does not compose. It is an interpretation of two objects, not an operation that turns one into the other. The pairing also depends on the product. The plain product and the product with the adjoint in the second slot give the Minkowski pairing; the product with the adjoint in the first slot gives its negative; the quaternionic product gives the Euclidean pairing, with the spatial sign reversed. The article uses the plain product and does not compare the four.

### The Excluded Operation: Left Multiplication

One operation of the algebra mixes the sectors and is not in the catalogue: left multiplication. The product $\vec e_x e_t=\vec e_x$ carries an informational element to a material one, and more generally the module action does not preserve the split. It is excluded because it is the action that builds the object on which the operations act, not an operation in the physical sense; the superselection statement below is about congruences, and the module action is not one. The exclusion is part of the catalogue: without it the table would be a list of every operation of the algebra, not a list of the physical couplings.

## The Catalogue in One Table

| Operation | Kind | Source and target | Boundary |
| --- | --- | --- | --- |
| Norm square | Map | $\mathbb{M}_-\to\mathbb{M}_+$, image $\mathbb{R}e_t$ | A map, not an evolution; the product of two material elements is not informational in general |
| Central multiplication | Bijection | $\mathbb{M}_-\leftrightarrow\mathbb{M}_+$ | Invertible, order four; no arrow |
| Rotor action | Action | $\mathbb{M}_+$ acts on $\mathbb{M}_-$ and preserves it | Unit-norm rotors only; a congruence rescaling the interval off the slice |
| Off-sector scalar | Pairing | $\mathbb{M}_-\times\mathbb{M}_+\to i\mathbb{R}$ | A pairing, produces no element, does not compose |

The table is exhaustive for the couplings the corpus uses. It is not exhaustive for every operation of the algebra: left multiplication is excluded above, and a map built by hand crosses the split by construction. Neither counts as a physical coupling.

## The Boundary

### The Superselection Statement

The four entries are maps, bijections, actions and pairings. None of the four operations is a measurement. An observable is a Hermitian element, and an expectation value is computed inside $\mathbb{M}_+$; no bridge is a process whose outcome could prepare or detect a coherence between the sectors.

The precise statement is the **superselection interpretation** of the split. The algebra is central simple, so there is no central projection that would split it into two ideals. What survives is a real-structure grading carried by $\flat=-{}^{*}$: the sectors are its eigenspaces, no congruence carries one into the other, and the only relative phase the algebra offers is the central phase $\exp(i\theta)$, which acts as a scalar on the module and is invisible on every ray. The module action, left multiplication, does mix the sectors, and it is not an operation in the physical sense.

### Rigidity and Coupling

The two halves of the answer must be read together.

- **Rigidity.** The conjugations preserve each sector, and so does every congruence, including every unitary evolution and every rotor. Nothing built from them crosses the split.
- **Coupling.** The norm square and the central $i$ carry an element across the split; the rotor and the off-sector scalar couple the sectors without carrying an element across. Each does so in its own way.

There is no contradiction because the two statements quantify over different classes. "No congruence crosses" does not say "no operation crosses", and "the norm square crosses" does not say "the norm square is observable". The physics needs both: the split is sharp enough to be a superselection rule and crossed enough to carry the dictionary between process and value.

### The Thermal Faces

Two further interpretations belong to the same split and are not new bridges. The material and informational ledgers are exchanged by the central $i$, which reverses the norm; the temperature is the thermodynamic rate at which one ledger is converted into the other, and erasure is the non-invertible operation that pays the price in the material ledger, $k_BT\log2$ per bit. The arrow that orders the exchange is the split of the acting monoid into units and non-units, not the central $i$, which is invertible. Both are thermodynamic interpretations of the split; neither adds a fifth kind to the catalogue.

## Limits

- **No coupling constant.** The catalogue names operations, not strengths. Nothing here gives a numerical coupling between the sectors, and the algebra has no parameter to give.
- **No dynamics.** Every entry is a map, a bijection, an action or a pairing. None is an equation of motion, and the arrow of time is not among them.
- **The tensor product is not used.** The article stays in the algebra. Composite systems, where a sector structure could be tensored, are outside its scope.
- **The scalar product is one of four.** The off-sector pairing is computed with the plain product. The quaternionic product gives the Euclidean pairing, and the two sesquilinear products give the Minkowski pairing up to sign; the article does not compare them.
- **The thermal reading is not a Wick rotation.** The Matsubara formalism complexifies the material time inside $\mathbb{M}_-$; it does not rotate the material sector into the informational one. The exchange here is the thermodynamic bookkeeping of the two ledgers, not a rotation of the time axis.

## Summary

The algebra splits into the material and the informational sectors, the eigenspaces of Hermitian conjugation. The split is a real subspace decomposition and not an ideal decomposition: the sectors are not complex subspaces, the product of two material elements is not in general material, and the real centre splits along the sectors. The conjugations preserve each sector, because each conjugation commutes with the involution that defines the sectors. That is the rigidity half of the answer. The bridge half is a catalogue of four kinds. The norm square is a map from the material sector to the real scalar line, and on a material element it is the interval. Multiplication by the central $i$ is a bijection that exchanges the sectors and reverses the norm, and it is the relational clock. A unit-norm Hermitian rotor acts by the sandwich; the sandwich preserves both sectors for every invertible parameter, so preservation alone does not single out the boost. What does is the sector of the generator: the boost's generator lies in $\mathbb{M}_+$, the rotation's in $\mathbb{M}_-$, so the boost is a bridge supplied by the informational sector and the rotation is a material motion. The boost factor itself is Hermitian and the rotation factor itself is a real quaternion: the boost factor shares the sector of its generator, the rotation factor does not. The off-sector scalar part is a pairing that returns a phase. None of the four operations is a measurement, and none supplies a dynamics. The superselection interpretation of the split and the four couplings are the two halves of one statement: the split is rigid for congruences and bridged by the four operations. The computational split into real and imaginary halves is a $\mathbb{Z}_2$ grading and not the sector split; the central scalar is read as a $c$-number background value, not as a projector.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $\mathbb{B}=\mathbb{C}\otimes_\mathbb{R}\mathbb{H}$ | The biquaternion algebra, isomorphic to $M_2(\mathbb{C})$ |
| ${}^{*}$ | Hermitian conjugation, with $\vec e_k^{*}=-\vec e_k$ and $i^{*}=-i$ |
| $\mathbb{M}_\pm=\{\tilde Q:\tilde Q^{*}=\pm\tilde Q\}$ | The material ($-$) and informational ($+$) sectors |
| ${}^{\natural}$, $\bar{\cdot}$, $\flat=-{}^{*}$ | Quaternion conjugation, coefficient conjugation and the real structure |
| $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^{2}$ | The biquaternion norm |
| $\tilde R=ict'+x\vec e_x+y\vec e_y+z\vec e_z$ | A material element |
| $\tilde H=h_te_t+i\vec h$ | An informational element |
| $\operatorname{Sc}$ | The scalar part of a biquaternion |

## Further Reading

- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](../articles_maths/the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the sectors, the conjugations and the trace.
- [The Group of Involutions](../articles_maths/the-group-of-involutions.html), for the Klein four-group and its fixed spaces.
- [Quaternionic Norm Regularity and Degeneracy in the Biquaternion Algebra](../articles_maths/quaternionic-norm-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the norm identity and its multiplicativity.
- [The Four General Products and Their Relations over the Biquaternion Algebra](../articles_maths/the-four-general-products-and-their-relations-over-the-biquaternion-algebra.html) and [The Four General Products and Their Relations over the Biquaternion Algebra](../articles_maths/the-four-general-products-and-their-relations-over-the-biquaternion-algebra.html), for the products and their sector behaviour.
- [Two-Sided Operators on the General Plain Sesqualgebra](../articles_maths/two-sided-operators-on-the-general-plain-sesqualgebra.html) and [Biquaternion Rotations and Lorentz Transformations](../articles_maths/biquaternion-rotations-and-lorentz-transformations.html), for the sandwich and the rotors.
- [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html), for the interval and the Lorentz action read at length.
- [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html), for the state space and the Born pairing.
- [The Material-Informational Split as a Superselection Structure in Biquaternionic Form](the-material-informational-split-as-a-superselection-structure-in-biquaternionic-form.html), for the negative statement and the real-structure grading.
- [Each Sector Is the Other's Clock: the Sector Exchange as Relational Time](each-sector-is-the-others-clock-the-sector-exchange-as-relational-time.html), for the clock interpretation of the central imaginary.
- [The Polar Decomposition and Its Three Pairings](the-polar-decomposition-and-its-three-pairings.html), §*The Three Splits*, for the Cartan exponents and the difference between a split and a pairing.
