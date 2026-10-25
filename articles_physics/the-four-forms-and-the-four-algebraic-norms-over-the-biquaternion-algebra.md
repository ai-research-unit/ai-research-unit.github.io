# __The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra__

## Introduction

The twelve products of the biquaternion complex space carry four **forms** and no more, and the four forms carry four **algebraic norms**. The form of a product is its scalar part, a function of two elements; the algebraic norm of a form is that form read at its two equal arguments, a function of one. The chain is short and rigid: twelve operations, four scalar parts, four functions of one element. This article reads the chain physically. The four forms are the **sector sign** $\langle\cdot,\cdot\rangle$, the **Born form** $\langle\cdot,\cdot\rangle_{*}$, the **interval** $\langle\cdot,\cdot\rangle_{\natural}$ and the **Krein form** $\langle\cdot,\cdot\rangle_{\natural*}$. They carry the letters $P$ for the plain, $N$ for the quaternionic, $H$ for the Hermitian and $K$ for the Krein, the letter naming the form with two arguments and the algebraic norm with one. The four algebraic norms are the four sums

$$
\boxed{\;\langle\tilde Q\rangle=\sum_\mu\varepsilon_\mu Q_\mu^{2},
\qquad
\langle\tilde Q\rangle_{*}=\sum_\mu\lvert Q_\mu\rvert^{2},
\qquad
\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^{2},
\qquad
\langle\tilde Q\rangle_{\natural*}=\sum_\mu\varepsilon_\mu\lvert Q_\mu\rvert^{2}\;},
$$

with $\varepsilon=(1,-1,-1,-1)$.

The article owns no new theorem. Each result is stated in a sentence, the mathematics article that proves it is linked, and the reading is given with its boundary.

## The Results It Uses

| Mathematical Content | Source Mathematical Article |
| --- | --- |
| The twelve products and the four distinct scalar parts | [Symmetric and Antisymmetric Decomposition of the Four General Products](../articles_maths/symmetric-and-antisymmetric-decomposition-of-the-four-general-products.html) |
| The four forms, their brackets, their Gram matrices, their signatures and their isometry groups | [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](../articles_maths/the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html) |
| The four algebraic norms, multiplicativity, definiteness and the impossibility of both | [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](../articles_maths/the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html) |
| The restrictions of the forms and the norms to the six remarkable subspaces | [Remarkable Subspaces and the Four General Products, Forms and Norms](../articles_maths/remarkable-subspaces-and-the-four-general-products-forms-and-norms.html) |
| Invertibility, the zero-divisor cone and the norm-one group | [Quaternionic Norm Regularity and Degeneracy in the Biquaternion Algebra](../articles_maths/quaternionic-norm-regularity-and-degeneracy-in-the-biquaternion-algebra.html) |
| The identities linking the four scalar parts | [The Four General Products and Their Relations over the Biquaternion Algebra](../articles_maths/the-four-general-products-and-their-relations-over-the-biquaternion-algebra.html) |

## The Forms

### From Twelve Operations to Four Forms

A form is the **scalar part** of a product. The twelve products split into four general products and their symmetrisations and antisymmetrisations, and the passage to the scalar part collapses them: the symmetrisation of a family keeps the scalar part of the general product, and the antisymmetrisation kills it. Hence the four general products and their four symmetrisations carry the four forms, two operations to a form, and the four antisymmetric operations carry the zero form. Four forms and no more.

The four forms are distinct as functions of two elements. On the pair $\tilde Q_1=\vec e_x$ and $\tilde Q_2=\vec e_x+i\vec e_x$ their values are $P=-(1+i)$, $H=1-i$, $N=1+i$ and $K=-(1-i)$, four different complex numbers. Each form is, up to the factor of the trace convention, the trace form of its own product:

$$
2\langle\tilde Q_1,\tilde Q_2\rangle=\mathrm{Tr}(\tilde Q_1\tilde Q_2),
\qquad
2\langle\tilde Q_1,\tilde Q_2\rangle_{*}=\mathrm{Tr}(\tilde Q_1\tilde Q_2^{*}),
$$
$$
2\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}=\mathrm{Tr}(\tilde Q_1^{\natural}\tilde Q_2),
\qquad
2\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}=\mathrm{Tr}(\tilde Q_1^{\natural}\tilde Q_2^{*}).
$$

| Form | Letter | Bracket | Pair | Coordinates | Symmetry | Gram | Signature over $\mathbb{R}$ | Null Set |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| the plain form, the sector sign | $P$ | $\langle\cdot,\cdot\rangle$ | $(\mathrm{id},\mathrm{id})$ | $Q_{1,0}Q_{2t}-(\vec Q_1,\vec Q_2)$ | symmetric | $\mathrm{E}$ | $(4,4)$ | the complex cone |
| the quaternionic form, the interval | $N$ | $\langle\cdot,\cdot\rangle_{\natural}$ | $({}^{\natural},\mathrm{id})$ | $Q_{1,0}Q_{2t}+(\vec Q_1,\vec Q_2)$ | symmetric | $\mathrm{I}_4$ | $(4,4)$ | $\mathcal{N}$, the $N$-degenerate set, the zero-divisor cone |
| the Hermitian form, the Born form | $H$ | $\langle\cdot,\cdot\rangle_{*}$ | $(\mathrm{id},{}^{*})$ | $Q_{1,0}\overline{Q_{2t}}+(\vec Q_1,\overline{\vec Q_2})$ | conjugate-symmetric | $\mathrm{I}_4$ | $(8,0)$ | $\{0\}$ |
| the quaternionic sesquilinear form, the Krein form | $K$ | $\langle\cdot,\cdot\rangle_{\natural*}$ | $({}^{\natural},{}^{*})$ | $Q_{1,0}\overline{Q_{2t}}-(\vec Q_1,\overline{\vec Q_2})$ | conjugate-symmetric | $\mathrm{E}$ | $(2,6)$ | $\mathcal{K}$ |

The **second slot** decides the symmetry: the two bilinear forms are symmetric, the two sesquilinear forms conjugate-symmetric, and only the sesquilinear ones have a real algebraic norm. The **first slot** decides the Gram matrix: $\mathrm{E}$ when the two slots are treated alike, $\mathrm{I}_4$ when exactly one is conjugated. Two forms share a Gram matrix and two share a symmetry, and no two share both. The two divisions are independent, and their product is the four.

### The Four Algebraic Norms

The **algebraic norm** of a form is that form at its two equal arguments. The four forms give four functions of one element, and the table of the four norms is the table of the four forms read on the diagonal.

| Algebraic Norm | Letter | Formula | Value | Gram | Signature over $\mathbb{R}$ | Vanishing Set | Multiplicative | Definite |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| $\langle\cdot\rangle$ | $P$ | $Q_t^{2}-Q_x^{2}-Q_y^{2}-Q_z^{2}$ | $\mathbb{C}$ | $\mathrm{E}$ | $(4,4)$ | the complex cone | no | — |
| $\langle\cdot\rangle_{\natural}$ | $N$ | $Q_t^{2}+Q_x^{2}+Q_y^{2}+Q_z^{2}$ | $\mathbb{C}$ | $\mathrm{I}_4$ | $(4,4)$ | $\mathcal{N}$, the $N$-degenerate set, the zero-divisor cone | **yes** | — |
| $\langle\cdot\rangle_{*}$ | $H$ | $\lvert Q_t\rvert^{2}+\lvert Q_x\rvert^{2}+\lvert Q_y\rvert^{2}+\lvert Q_z\rvert^{2}$ | $\mathbb{R}$ | $\mathrm{I}_4$ | $(8,0)$ | $\{0\}$ | no | **yes** |
| $\langle\cdot\rangle_{\natural*}$ | $K$ | $\lvert Q_t\rvert^{2}-\lvert Q_x\rvert^{2}-\lvert Q_y\rvert^{2}-\lvert Q_z\rvert^{2}$ | $\mathbb{R}$ | $\mathrm{E}$ | $(2,6)$ | $\mathcal{K}$ | no | no |

Two of the four have a property the others lack, and the two properties are different. The Hermitian algebraic norm $\langle\cdot\rangle_{*}$ is **positive definite**, and its square root is the unique topological norm of the space, $\lVert\tilde Q\rVert_E^{2}=\langle\tilde Q\rangle_{*}$. The quaternionic algebraic norm $\langle\cdot\rangle_{\natural}$ is **multiplicative**,

$$
\boxed{\;\langle\tilde Q_1\tilde Q_2\rangle_{\natural}=\langle\tilde Q_1\rangle_{\natural}\,\langle\tilde Q_2\rangle_{\natural}\;},
$$

and it is the quaternionic norm of the algebra, the determinant of the $2\times2$ representation $\mathsf{M}_2(\tilde Q)=Q_t\mathrm{I}_2-i\sum_kQ_k\sigma_k$. An element is $N$-regular, $\langle\tilde Q\rangle_{\natural}\neq0$, if and only if it is invertible. The $N$-regular set is the group of units $\{\langle\tilde Q\rangle_{\natural}\neq0\}$; its subgroup $\{\langle\tilde Q\rangle_{\natural}=1\}$ is a non-compact real six-manifold homotopy equivalent to $S^{3}$.

**No function is both definite and multiplicative.** The algebra has zero divisors, $(e_t+i\vec e_x)(e_t-i\vec e_x)=0$ with both factors non-zero and $\langle e_t\pm i\vec e_x\rangle_{\natural}=1-1=0$. A multiplicative function that is not constant has $\varphi(0)=0$, so it would give $\varphi(e_t+i\vec e_x)\varphi(e_t-i\vec e_x)=\varphi(0)=0$; one value would vanish on a non-zero element, and a definite function is non-zero off the origin. The multiplicative one and the definite one are different objects, and that difference is the failure of the biquaternions to be a normed division algebra. The four normed division algebras of the Hurwitz theorem are exactly the ones in which the two senses coincide.

**One letter, two arities.** A letter names the form when it carries two arguments and the algebraic norm when it carries one; the norm is the form of the same name with the arguments equated. The distinction is not cosmetic: $\langle\cdot\rangle_{\natural}$ is a pairing of two elements and $\langle\tilde Q\rangle_{\natural}$ is a single number, and the multiplicative law is a law of the second, not of the first.

## The Forms on the Two Sectors

The physical dictionary places the material element $\tilde R=ict'\,e_t+x\vec e_x+y\vec e_y+z\vec e_z$ in the anti-Hermitian sector $\mathbb{M}_-$ and the informational element in the Hermitian sector $\mathbb{M}_+$. The restrictions of the four forms are the algebra's own statement of which form belongs to which sector.

| Form | Signature on $\mathbb{M}_-$, material | Signature on $\mathbb{M}_+$, informational |
| --- | --- | --- |
| $P$: $\langle\cdot,\cdot\rangle$, the sector sign | $(0,4)$, negative definite | $(4,0)$, positive definite |
| $N$: $\langle\cdot,\cdot\rangle_{\natural}$, the interval | $(3,1)$ | $(1,3)$ |
| $H$: $\langle\cdot,\cdot\rangle_{*}$, the Born form | $(4,0)$, positive definite | $(4,0)$, positive definite |
| $K$: $\langle\cdot,\cdot\rangle_{\natural*}$, the Krein form | $(1,3)$ | $(1,3)$ |

Two pairs of coincidences hold on the sectors, and they are the reason the four names are easy to exchange. On the material sector the Born form is minus the sector sign and the Krein form is minus the interval,

$$
\langle\cdot,\cdot\rangle_{*}=-\langle\cdot,\cdot\rangle
\qquad\text{and}\qquad
\langle\cdot,\cdot\rangle_{\natural*}=-\langle\cdot,\cdot\rangle_{\natural}
\quad\text{on }\mathbb{M}_-,
$$

while on the informational sector the two pairs coincide,

$$
\langle\cdot,\cdot\rangle_{*}=\langle\cdot,\cdot\rangle
\qquad\text{and}\qquad
\langle\cdot,\cdot\rangle_{\natural*}=\langle\cdot,\cdot\rangle_{\natural}
\quad\text{on }\mathbb{M}_+.
$$

The four forms collapse to two pairs on each sector, and these identities are form-level statements read on the sector. They do not say that the four products agree there.

The collapse to two pairs holds on every remarkable subspace, but the pairing is not the same on all of them. On the centre $\mathbb{C}_{\mathbb{B}}$, $\langle\cdot,\cdot\rangle=\langle\cdot,\cdot\rangle_{\natural}$ and $\langle\cdot,\cdot\rangle_{*}=\langle\cdot,\cdot\rangle_{\natural*}$; on the vector subspace $\mathrm{Vect}(\mathbb{B})$, $\langle\cdot,\cdot\rangle=-\langle\cdot,\cdot\rangle_{\natural}$ and $\langle\cdot,\cdot\rangle_{*}=-\langle\cdot,\cdot\rangle_{\natural*}$; on the quaternion subspace $\mathbb{H}_{\mathbb{B}}$, $\langle\cdot,\cdot\rangle=\langle\cdot,\cdot\rangle_{\natural*}$ and $\langle\cdot,\cdot\rangle_{\natural}=\langle\cdot,\cdot\rangle_{*}$; on the anti-quaternion subspace $i\mathbb{H}_{\mathbb{B}}$, $\langle\cdot,\cdot\rangle=-\langle\cdot,\cdot\rangle_{\natural*}$ and $\langle\cdot,\cdot\rangle_{\natural}=-\langle\cdot,\cdot\rangle_{*}$; on the informational sector, $\langle\cdot,\cdot\rangle=\langle\cdot,\cdot\rangle_{*}$ and $\langle\cdot,\cdot\rangle_{\natural}=\langle\cdot,\cdot\rangle_{\natural*}$; and on the material sector, $\langle\cdot,\cdot\rangle=-\langle\cdot,\cdot\rangle_{*}$ and $\langle\cdot,\cdot\rangle_{\natural}=-\langle\cdot,\cdot\rangle_{\natural*}$. The grouping of the four into the two pairs therefore depends on the subspace, and it is the subspace's fingerprint. The Hermitian form is positive definite on every one of the six subspaces; the other three are indefinite on the algebra and may be definite on a restriction. The Krein form, for instance, is positive definite of signature $(2,0)$ on the centre, negative definite of signature $(0,6)$ on the vector subspace, and of signature $(1,3)$ on each of the other four.

**The boundary.** The signatures in the table are the signatures of the **restrictions** and not new forms. A restriction may be definite where the form is indefinite, and its definiteness says nothing about the form. The complex cone, the zero-divisor cone and the Krein cone are the null sets of the three indefinite forms on the whole algebra; the light cone is the cut of the zero-divisor cone by the material sector, not the null set of the form on the algebra.

## Interpretations

### The Sector Sign, $P$

The plain bilinear form is definite with opposite signs on the two sectors: negative on the material side, positive on the informational side. It is the one symmetric form that is definite with opposite signs and so tells them apart. On the material sector it is the negative Euclidean square, $\langle\tilde R,\tilde R\rangle=-c^{2}{t'}^{2}-x^{2}-y^{2}-z^{2}$, and it has no cone there. Its null set on the algebra is the complex cone of real dimension six, which is not the light cone, and it cuts across the invertible and the non-invertible elements alike.

The sector sign is read as a **flag** and not as a metric. It says which half an element belongs to and measures neither. The element $e_t+\vec e_x$ is a unit with $\langle e_t+\vec e_x,e_t+\vec e_x\rangle=0$, and $e_t+i\vec e_x$ is a zero divisor with $\langle e_t+i\vec e_x,e_t+i\vec e_x\rangle=2$; the form decides no inverse, and its null set is not the wall of invertibility. The metric of the material sector is the interval, and the interval is the next reading but one.

**The boundary.** The form is complex-valued on the centre and the vector subspace, where the coefficients are general complex numbers; on the four real-type subspaces it is real. "Definite" is a statement about the real part of the restriction, and the sign is the sign of that real part. The sector sign is not the Born form, not the interval and not the Krein form; the table of the four forms separates them.

### The Born Form, $H$

The Hermitian form is positive definite of signature $(8,0)$ on the real algebra, and it is the only one of the four that is definite on every subspace. Its square root is the unique topological norm, and it is the form a probability is built from. It is the **Born pairing** of a state and an observable, the form preserved by the unitary evolution, and the form whose isometry group is $\mathrm{U}(4)$.

It is blind to the sector: positive on the material and on the informational side alike. That blindness is the precise content of the corpus's rule that the material sector is invisible in the sesquilinear layer. On the material sector the Born form is the Euclidean square, $c^{2}{t'}^{2}+x^{2}+y^{2}+z^{2}$, and it is minus the sector sign; the sign of the sector lives in the bilinear layer, and the sesquilinear layer does not carry it.

The form supplies the weight, not the state. The pure states are the minimal Hermitian idempotents of the algebra, $\tfrac12(e_t+i\vec u)$ with $\vec u$ a real unit vector, and the Born weight is the pairing of a state with an observable. The state carries the axis $\vec u$ and no phase; the phase belongs to the spinor, not to the form.

**The boundary.** The identification of the definite Hermitian form with physical probability is the hypothesis of the informational sector, not a theorem of the algebra. The form proves that a positive definite pairing exists and that it is unique among the four; it does not prove the Born rule, the measurement postulate or the identification of an element with a state.

### The Interval, $N$

The quaternionic bilinear form is the **interval**. On the material sector it is the Minkowski metric of signature $(3,1)$,

$$
\langle\tilde R\rangle_{\natural}=-c^{2}{t'}^{2}+x^{2}+y^{2}+z^{2},
$$

its zero set is the light cone, and its level sets are the mass shells, $\{\langle\tilde Q\rangle_{\natural}=-m^{2}c^{2}\}$. On the informational sector the same form has signature $(1,3)$: the inertia is reversed by the sector, and the interval and the informational metric are one form.

The interval is **multiplicative**, and that is what makes it a causal structure rather than a quadratic decoration: the causal type of a composite is the product of the causal types. Its null set is closed under multiplication, as are the units and the zero divisors; the cut of the null set by the material sector is the light cone. The sector is not closed under the product, because two anti-Hermitian elements compose to an anti-Hermitian element only when they anticommute, so the closure belongs to the algebra and not to the sector. On the unit group the logarithm of the modulus is additive and reads as a dilation potential; the rapidity is the length of the pure part of the polar angle, not that potential. Invertibility is exactly the complement of the cone, which is therefore the wall of the reversible region.

The interval is the algebraic norm that carries the word **mass**. Its level set is the mass shell, its zero set the light cone, and its sign is the causal character of the displacement. The other three algebraic norms do not carry the mass: the definite one carries the probability, the sector sign carries the flag, and the Krein norm carries the constraint.

**The boundary.** The interval is real on the four real-type subspaces and complex on the centre and the vector subspace; the mass shell is a level set on the sector, not a value of the form on the whole algebra. The form detects no polarisation count and no charge label: those are the rank and the compact slice, and they are readings of the element beside the mass, not values of the norm. The interval does not derive a mass spectrum, and it does not say which element is a particle.

### The Krein Form, $K$

The Krein form is the indefinite Hermitian form of the fourth corner. It is real at the two equal arguments, of signature $(2,6)$ on the real algebra and $(1,3)$ on each of the four four-dimensional real-type subspaces, and it normalises nothing: an indefinite form has no positive unit sphere, so it cannot supply a probability. Its null set is the real cone $\mathcal{K}=\{\lvert c\rvert=\lvert v\rvert\}$ of the centre–vector split, of real dimension seven, and its positive and negative value-one sets are $S^{1}\times\mathbb{R}^{6}$ and $S^{5}\times\mathbb{R}^{2}$.

The reading is a **constraint**, not a state. A gauge calibration fixes a redundancy of the description; it does not prepare a state, and its form is the form of that redundancy. The signature is what an object is: a definite Hermitian form counts states, an indefinite one counts a constraint. The Krein form is the indefinite metric of an indefinite-metric quantum theory, and its fundamental symmetry is the natural conjugation ${}^{\natural}$, the operator that turns it into a definite form.

On the material sector the Krein form is minus the interval; on the informational sector it is the interval. The two are one form read with a sign, and on the informational side they are the same form. This is the algebraic reason the interval and the gauge form are easy to conflate, and the reason the sign of the sector must be named whenever the two are compared.

**The boundary.** The Krein column states the form alone. The indefinite structure — the Krein space, its fundamental symmetry, its signatures and its topology — is read in *The Krein Form and the Indefinite Structure*. The form does not derive a gauge group, a coupling or a field content, and its zero set is not the zero-divisor cone: $\mathcal{K}$ and $\mathcal{N}$ are different cones, of real dimensions seven and six.

## The Change of Scalars

The four forms are forms over $\mathbb{C}$. Realifying the space is what a computation, a simulation or a matrix model does, and it moves the forms by two rules. A symmetric bilinear form of complex rank $n$ realifies to the **split** signature $(n,n)$; a Hermitian form of inertia $(n,m)$ realifies by **doubling** its inertia, $(2n,2m)$. The four signatures over $\mathbb{R}$ are therefore

$$
\boxed{\;(4,4)\ \text{for}\ \langle\cdot,\cdot\rangle,
\qquad
(8,0)\ \text{for}\ \langle\cdot,\cdot\rangle_{*},
\qquad
(4,4)\ \text{for}\ \langle\cdot,\cdot\rangle_{\natural},
\qquad
(2,6)\ \text{for}\ \langle\cdot,\cdot\rangle_{\natural*}\;}.
$$

The change of scalars also collapses the count. On the real part of the space the coefficientwise conjugation is the identity, so $\langle\cdot,\cdot\rangle_{\natural*}=\langle\cdot,\cdot\rangle$ and $\langle\cdot,\cdot\rangle_{*}=\langle\cdot,\cdot\rangle_{\natural}$: a computation restricted to real coefficients sees two forms and hides the other two. It sees ten of the twelve products, the pairs $\mathrm{SPS}=\mathrm{SQA}$ and $\mathrm{APA}=\mathrm{AQS}$ having collapsed, and it does not see the complex witness of the Jacobi failure of $\mathrm{AQS}$. The count of twelve is the count over $\mathbb{C}$, and the difference of count is the algebraic size of the complex structure the grid carries.

**What the change of scalars is not.** The realification of $\mathbb{B}$ is $\mathbb{B}$ read over the reals, not the algebra of pairs of quaternions. The multiplication is the multiplication of the complex algebra with the scalars restricted; the centre stays the complex line $\mathbb{C}e_t$, read over $\mathbb{R}$ and not a split algebra; and every object read from the ring alone — the centre, the ideals, the idempotents, the zero divisors, the nilpotents, the units — is unchanged. The change is a change of the field of a module and of the dimension, not of the ring.

The two rules are also the framework's reading of why the interval is indefinite and the Euclidean form definite. The interval of signature $(3,1)$ is the restriction to the material sector of a realified complex bilinear form; the Euclidean form of signature $(8,0)$ is the realification of a Hermitian form. One is the restriction of a split form, the other the realification of a definite one, and the framework treats neither as the other. The signature $(4,4)$ of the interval on the real algebra and the signature $(3,1)$ of its restriction are not in contradiction: they are the same form at two different levels.

## The Four Readings of One Element

The four algebraic norms are four functions on the algebra. Beside them, the corpus reads **one element** four ways, and the two lists must not be confused. The readings are the norm, the rank, the charge and the scale.

| Reading | Object | What It Says | Where It Fails |
| --- | --- | --- | --- |
| norm | $\langle\tilde R\rangle_{\natural}=\sum_\mu R_\mu^{2}$ | the value and its sign; the mass shell as a level set | detects no polarisation count and no label |
| rank | $\operatorname{rank}\mathsf{M}_2(\tilde R\tilde R^{*})$ | the count of polarisations, two for the massive type and one for the massless type | fixes only whether the mass vanishes, never its value |
| charge | the compact slice $\{\tilde U:\tilde U\tilde U^{*}=e_t\}\cong\mathrm{U}(2)$ | the discrete internal label, discrete because the group is compact | says nothing about the cone |
| scale | the polar modulus $r$ | the unit of length, the dilation potential | is a unit and not a level set |

Only the first reading is the mass: $\langle\tilde R\rangle_{\natural}=-m^{2}c^{2}$ on shell. The other three are read beside it and are not three other kinds of mass. The rank reads the count of polarisations, two when $\langle\tilde R\rangle_{\natural}\neq0$ and at most one on the cone; the charge is the label of a representation of the compact internal group; the scale is the unit the mass is measured in, and for the four-momentum it is $r=mc$. The norm and the rank agree on the cone, and the charge and the scale are defined only off it: the compact slice lies inside the invertible elements, and the cone is the complement of the invertible elements.

**The boundary.** The four readings of one element are not the four algebraic norms. They are four questions asked of one element; the four algebraic norms are four functions on the algebra. Only $\langle\cdot\rangle_{\natural}$ belongs to both lists.

## Limits

The article reads the algebra's own chain: twelve products, four forms, four algebraic norms. The physics is the naming of the four forms and of the four norms, and the naming is a reading, not a theorem. The algebra proves the count, the Gram matrices, the signatures, the null sets, the multiplicativity of $\langle\cdot\rangle_{\natural}$ and the definiteness of $\langle\cdot\rangle_{*}$; it does not prove that these are the four quantities a physical theory evaluates, nor that the four jobs are the only four.

Three levels of signature must be kept apart. The **complex form** has a Gram matrix and a complex rank; its **realification** has a signature over $\mathbb{R}$, and the four are $(4,4)$, $(8,0)$, $(4,4)$ and $(2,6)$; its **restriction** to a sector has a signature of its own, and on the material sector the four are $(0,4)$, $(4,0)$, $(3,1)$ and $(1,3)$. The physical interval is the third level, not the second, and a reader who carries $(4,4)$ into a statement about spacetime has changed the object.

Two senses of *norm* must be kept apart. The **algebraic norm** is a map into the ring — $\mathbb{C}$ for the two bilinear forms, $\mathbb{R}$ for the two Hermitian ones — and it is algebra. The **topological norm** is the one selection of positive real values, $\lVert\tilde Q\rVert_E=(\langle\tilde Q\rangle_{*})^{1/2}$, and it is topology. Only the Hermitian form yields the second; the other three are algebraic norms and give no distance. A norm is not a distance until a square root is taken and a positivity is declared.

On the sectors the four forms coincide in pairs, and the coincidence is a statement about the forms. It does not make the four products agree, and it does not make the Krein form a probability or the sector sign an interval. The identities are read with both arguments on the sector; for a general element the four forms are four.

The article states no dynamics, no mass value, no spectrum and no gauge group. The Krein column states the form alone, and its indefinite structure is read in *The Krein Form and the Indefinite Structure*. The mass shell is a level set, not a derived spectrum; the charge is a label of a compact group, not a derived coupling; the interval is a metric, not an equation of motion.

## Regular and Degenerate Biquaternions

Each letter cuts the algebra in two by the value of its norm: a $\Phi$-regular biquaternion has $\Phi(\tilde Q)\neq0$ and a $\Phi$-degenerate one has $\Phi(\tilde Q)=0$. The four cuts are different cuts and must not be exchanged.

- $N$-regular is $N(\tilde Q)\neq0$, and it is exactly the set of invertible elements, the unit group $\mathbb{B}^{\times}$. $N$-degenerate is the null cone $\mathcal{N}$: the origin together with the zero divisors.
- $P$-degenerate is the complex cone, of real dimension six. It is not a wall of invertibility; it contains units, $P(e_t+\vec e_x)=0$ with $N(e_t+\vec e_x)=2$.
- $H$-degenerate is the origin alone, since the Hermitian norm is definite. Every nonzero biquaternion is $H$-regular.
- $K$-degenerate is the Krein cone $\mathcal{K}$, of real dimension seven. It is not the zero-divisor cone, and it also contains units.

Only the $N$ cut is the invertibility partition. A degenerate biquaternion is not the same object as a zero divisor: the origin is $N$-degenerate for every letter and is not a zero divisor, and $N$-degeneracy is $N(\tilde Q)=0$, while being a zero divisor is the annihilation $Q R=0$ or $R Q=0$ for a nonzero $R$. The two coincide off the origin in $\mathbb{B}$ for the plain product, and that coincidence is a theorem about $\mathcal{N}$, not the definition of the word.

## Summary

- The twelve products carry four forms and no more: the symmetrisation keeps the scalar part, the antisymmetrisation kills it, so the four general products and their four symmetrisations carry four forms two by two and the four antisymmetric operations carry the zero form.
- The four forms are the sector sign $\langle\cdot,\cdot\rangle$ written $P$, the interval $\langle\cdot,\cdot\rangle_{\natural}$ written $N$, the Born form $\langle\cdot,\cdot\rangle_{*}$ written $H$ and the Krein form $\langle\cdot,\cdot\rangle_{\natural*}$ written $K$, with Gram matrices $\mathrm{E}$, $\mathrm{I}_4$, $\mathrm{I}_4$ and $\mathrm{E}$.
- A $\Phi$-regular biquaternion has $\Phi(\tilde Q)\neq0$ and a $\Phi$-degenerate one has $\Phi(\tilde Q)=0$; only the $N$ cut is the invertibility partition, $N$-regular being the unit group and $N$-degenerate the null cone, the origin together with the zero divisors.
- The second slot decides the symmetry and the reality of the algebraic norm; the first slot decides the Gram matrix and the signature.
- The four algebraic norms are $\sum_\mu\varepsilon_\mu Q_\mu^{2}$, $\sum_\mu\lvert Q_\mu\rvert^{2}$, $\sum_\mu Q_\mu^{2}$ and $\sum_\mu\varepsilon_\mu\lvert Q_\mu\rvert^{2}$.
- $\langle\cdot\rangle_{*}$ is the definite one, and its square root is the unique topological norm; $\langle\cdot\rangle_{\natural}$ is the multiplicative one, the quaternionic norm and the criterion of invertibility.
- No function is both definite and multiplicative: the zero divisors forbid it, and the failure is the failure of the biquaternions to be a normed division algebra.
- On the material sector the forms are $(0,4)$, $(4,0)$, $(3,1)$ and $(1,3)$; on the informational sector they are $(4,0)$, $(4,0)$, $(1,3)$ and $(1,3)$.
- The Born form is minus the sector sign on the material sector and the sector sign on the informational one; the Krein form is minus the interval on the material sector and the interval on the informational one.
- The interval's level sets are the mass shells on the material sector, its zero set cut by the sector is the light cone, and its zero set on the algebra is the zero-divisor cone; the Krein cone is a different cone, of one more real dimension.
- On the real part the four forms collapse to two and the twelve products to ten; the count of twelve is a count over $\mathbb{C}$.
- The four readings of one element — norm, rank, charge and scale — are not the four algebraic norms; only the norm is the mass, and only the quaternionic algebraic norm belongs to both lists.

## Summary of Notation

| Symbol | Meaning |
| --- | --- |
| $P$, $N$, $H$, $K$ | the plain, quaternionic, Hermitian and Krein letter, naming the form with two arguments and the algebraic norm with one |
| $\langle\tilde Q_1,\tilde Q_2\rangle$, $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural}$, $\langle\tilde Q_1,\tilde Q_2\rangle_{*}$, $\langle\tilde Q_1,\tilde Q_2\rangle_{\natural*}$ | the sector sign, the interval, the Born form and the Krein form |
| $\langle\tilde Q\rangle$, $\langle\tilde Q\rangle_{\natural}$, $\langle\tilde Q\rangle_{*}$, $\langle\tilde Q\rangle_{\natural*}$ | the four algebraic norms, the same brackets at two equal arguments |
| $\varepsilon=(1,-1,-1,-1)$ | the sign vector of the natural conjugation |
| $\mathrm{E}=\operatorname{diag}(1,-1,-1,-1)$, $\mathrm{I}_4$ | the Gram matrices of the four forms |
| $(4,4)$, $(4,4)$, $(8,0)$, $(2,6)$ | the signatures of the realifications of the four forms |
| $(0,4)$, $(3,1)$, $(4,0)$, $(1,3)$ | their signatures on $\mathbb{M}_-$, in the same order |
| $(4,0)$, $(1,3)$, $(4,0)$, $(1,3)$ | their signatures on $\mathbb{M}_+$, in the same order |
| $\mathcal{N}$, $\mathcal{K}$ | the $N$-degenerate set, the zero-divisor cone, and the Krein cone |
| $\lVert\tilde Q\rVert_E$ | the Euclidean norm, the square root of $\langle\tilde Q\rangle_{*}$ |
| $\mathsf{M}_2(\tilde Q)=Q_t\mathrm{I}_2-i\sum_kQ_k\sigma_k$ | the $2\times2$ representation whose determinant is $\langle\tilde Q\rangle_{\natural}$ |
| $\mathbb{M}_-$, $\mathbb{M}_+$ | the anti-Hermitian (material) and Hermitian (informational) sectors |

## Further Reading

- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](../articles_maths/the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html), for the count of the four forms, the table and the isometry groups, and for the four algebraic norms, multiplicativity, definiteness and the zero divisors.
- [Remarkable Subspaces and the Four General Products, Forms and Norms](../articles_maths/remarkable-subspaces-and-the-four-general-products-forms-and-norms.html), for the restrictions on the six subspaces.
- [Quaternionic Norm Regularity and Degeneracy in the Biquaternion Algebra](../articles_maths/quaternionic-norm-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the quaternionic norm, the inverse and the norm-one group.
- [The Four General Products: Composition, Probability, Causality, Gauge](the-four-general-products-composition-probability-causality-gauge.html), for the four products whose scalar parts these forms are.
- [The Krein Form and the Indefinite Structure](the-krein-form-and-the-indefinite-structure.html), for the indefinite structure and the fundamental symmetry.
